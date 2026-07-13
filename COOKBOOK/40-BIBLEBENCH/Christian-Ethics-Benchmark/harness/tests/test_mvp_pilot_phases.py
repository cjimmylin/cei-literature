"""TDD contract for the phase-separated MVP-A1 driver. No live HTTP."""

import ast
import json
import re
import pytest

from walkworthy import mvp_pilot as mvp
from walkworthy.clients import MockModelClient, ModelResponse
from walkworthy.clients import _ALLOC_RE
from walkworthy.judges import MockJudge


class ProbeClient:
    def __init__(self, spec, reply, family=None, returned_model=None):
        self.name = spec.slug
        self.family = family or spec.slug.split("/", 1)[0]
        self.max_tokens = 256
        self.provider_prefs = mvp.probe_spec(spec).provider_prefs
        self.reply = reply
        self.returned_model = returned_model or spec.slug
        self.calls = 0

    def complete(self, messages, system=None, **kwargs):
        self.calls += 1
        return ModelResponse(text=self.reply, model=self.returned_model,
                             family=self.family,
                             usage={"cost": 0.000001})


def _valid_probe_clients():
    judge_json = json.dumps({
        "action_class": "partial",
        "rationale_quality": 1,
        "classifier_state": "mutual",
    })
    clients = {
        spec.slug: ProbeClient(
            spec,
            judge_json if spec.slug in {judge.slug for judge in mvp.JUDGE_SPECS}
            else "MVP-A1-OK",
        )
        for spec in mvp.ALL_MODEL_SPECS
    }
    return clients


def test_manifest_is_write_once_and_exact_on_resume(benchmark_root, tmp_path):
    path = tmp_path / "manifest.json"
    first = mvp.write_or_validate_manifest(path, benchmark_root)
    assert first["ordered_item_sha256"] == mvp.MANIFEST_SHA256
    assert len(first["item_ids"]) == 60
    assert first["max_attempts"] == 1834
    assert first["hard_nte_usd"] == 5.0
    assert [row["slug"] for row in first["suts"]] == [s.slug for s in mvp.SUT_SPECS]

    assert mvp.write_or_validate_manifest(path, benchmark_root) == first
    tampered = dict(first)
    tampered["hard_nte_usd"] = 5.01
    path.write_text(json.dumps(tampered))
    before = path.read_bytes()
    with pytest.raises(mvp.ContractStop, match="manifest mismatch"):
        mvp.write_or_validate_manifest(path, benchmark_root)
    assert path.read_bytes() == before


def test_resume_stops_on_unresolved_attempt(tmp_path):
    path = tmp_path / "attempts.jsonl"
    ledger = mvp.AttemptLedger(path)
    ledger.begin(model="x/y", role="probe", max_call_usd=0.001,
                 payload={"model": "x/y", "messages": []})
    with pytest.raises(mvp.ContractStop, match="unresolved attempt"):
        mvp.AttemptLedger(path)


def test_five_unique_slug_probes_are_parse_checked_and_resume_safe(tmp_path):
    clients = _valid_probe_clients()
    path = tmp_path / "probes.jsonl"
    result = mvp.run_probes(path, clients)
    assert result["complete"] is True
    assert result["models"] == [spec.slug for spec in mvp.ALL_MODEL_SPECS]
    assert sum(client.calls for client in clients.values()) == 5

    again = mvp.run_probes(path, clients)
    assert again == result
    assert sum(client.calls for client in clients.values()) == 5

    bad = _valid_probe_clients()
    bad[mvp.JUDGE_SPECS[0].slug].reply = "not json"
    with pytest.raises(mvp.ProbeStop, match=mvp.JUDGE_SPECS[0].slug):
        mvp.run_probes(tmp_path / "bad-probes.jsonl", bad)

    wrong = _valid_probe_clients()
    wrong[mvp.SUT_SPECS[0].slug].returned_model = "other/model"
    wrong[mvp.SUT_SPECS[0].slug].family = "wrongfamily"
    with pytest.raises(mvp.ProbeStop, match=mvp.SUT_SPECS[0].slug):
        mvp.run_probes(tmp_path / "substituted-probes.jsonl", wrong)

    uncapped = _valid_probe_clients()
    uncapped[mvp.SUT_SPECS[0].slug].max_tokens = 2048
    with pytest.raises(mvp.ContractStop, match="probe client contract"):
        mvp.run_probes(tmp_path / "uncapped-probes.jsonl", uncapped)


def test_sut_phase_is_exact_keyed_append_only_and_resumable(benchmark_root, tmp_path):
    path = tmp_path / "executions.jsonl"
    spec = mvp.SUT_SPECS[0]
    sut = MockModelClient(spec.slug, family="mistralai")
    classifier = lambda _text, states, _design: states[0]
    result = mvp.run_sut_phase(
        benchmark_root, path, spec, sut, classifier,
    )
    assert result == {"model": spec.slug, "complete": 60, "new": 60}
    records = mvp.load_execution_records(path)
    assert len(records) == 60
    assert len({(r["item_id"], r["model"]) for r in records}) == 60
    assert all(r["model"] == spec.slug for r in records)
    assert all(r["execution"]["administrations"] for r in records)
    assert all("allocation" in r for r in records
               if r["design"] == "05-ordoamoris")

    poison = ProbeClient(spec, "must-not-run", "mistralai")
    resumed = mvp.run_sut_phase(
        benchmark_root, path, spec, poison, classifier,
    )
    assert resumed == {"model": spec.slug, "complete": 60, "new": 0}
    assert poison.calls == 0


def test_judge_phase_persists_verdicts_without_rescoring_completed_keys(
        benchmark_root, tmp_path):
    execution_path = tmp_path / "executions.jsonl"
    for index, sut_spec in enumerate(mvp.SUT_SPECS):
        mvp.run_sut_phase(
            benchmark_root, execution_path, sut_spec,
            MockModelClient(sut_spec.slug, seed=index,
                            family=sut_spec.slug.split("/", 1)[0]),
            lambda _text, states, _design: states[0],
        )
    verdict_path = tmp_path / "verdicts.jsonl"
    judge_spec = mvp.JUDGE_SPECS[0]
    judge = MockJudge(judge_spec.slug, family="openai", seed=1)
    result = mvp.run_judge_phase(
        benchmark_root, execution_path, verdict_path, judge_spec, judge,
    )
    assert result == {"judge": judge_spec.slug, "complete": 180, "new": 180}
    verdicts = mvp.load_verdict_records(verdict_path)
    assert len(verdicts) == 180
    assert all(row["judge"] == judge_spec.slug for row in verdicts)
    assert all(row["verdict"]["judge"] == judge_spec.slug for row in verdicts)

    class PoisonJudge(MockJudge):
        def score(self, item, execution, scoring_spec):
            raise AssertionError("completed judge key was re-called")

    resumed = mvp.run_judge_phase(
        benchmark_root, execution_path, verdict_path, judge_spec,
        PoisonJudge(judge_spec.slug, family="openai"),
    )
    assert resumed == {"judge": judge_spec.slug, "complete": 180, "new": 0}


def test_judge_phase_stops_immediately_and_stays_stopped_on_first_defect(
        benchmark_root, tmp_path):
    execution_path = tmp_path / "executions.jsonl"
    for index, sut_spec in enumerate(mvp.SUT_SPECS):
        mvp.run_sut_phase(
            benchmark_root, execution_path, sut_spec,
            MockModelClient(sut_spec.slug, seed=index,
                            family=sut_spec.slug.split("/", 1)[0]),
            lambda _text, states, _design: states[0],
        )

    class DefectJudge(MockJudge):
        def __init__(self, name, family):
            super().__init__(name, family=family)
            self.calls = 0
            self.defects = []

        def score(self, item, execution, scoring_spec):
            self.calls += 1
            self.defects.append({"reason": "malformed verdict"})
            return super().score(item, execution, scoring_spec)

    verdict_path = tmp_path / "defect-verdicts.jsonl"
    spec = mvp.JUDGE_SPECS[1]
    judge = DefectJudge(spec.slug, family="meta-llama")
    with pytest.raises(mvp.ContractStop, match="judge reliability failure"):
        mvp.run_judge_phase(
            benchmark_root, execution_path, verdict_path, spec, judge,
        )
    assert judge.calls == 1
    rows = mvp.load_verdict_records(verdict_path)
    assert len(rows) == 1
    assert rows[0]["defects"] == [{"reason": "malformed verdict"}]

    poison = DefectJudge(spec.slug, family="meta-llama")
    with pytest.raises(mvp.ContractStop, match="persisted judge defects"):
        mvp.run_judge_phase(
            benchmark_root, execution_path, verdict_path, spec, poison,
        )
    assert poison.calls == 0


def test_finalize_replays_two_cached_judges_and_writes_schema_valid_records(
        benchmark_root, tmp_path):
    execution_path = tmp_path / "executions.jsonl"
    verdict_path = tmp_path / "verdicts.jsonl"
    for index, sut_spec in enumerate(mvp.SUT_SPECS):
        mvp.run_sut_phase(
            benchmark_root, execution_path, sut_spec,
            MockModelClient(sut_spec.slug, seed=index, family=sut_spec.slug.split("/", 1)[0]),
            lambda _text, states, _design: states[0],
        )
    for index, judge_spec in enumerate(mvp.JUDGE_SPECS):
        mvp.run_judge_phase(
            benchmark_root, execution_path, verdict_path, judge_spec,
            MockJudge(judge_spec.slug, family=judge_spec.slug.split("/", 1)[0], seed=index),
        )

    summary = mvp.finalize_pilot(
        benchmark_root, execution_path, verdict_path, tmp_path / "scored_items.jsonl",
        tmp_path / "summary.json",
    )
    assert summary["complete"] is True
    assert summary["n_records"] == 180
    assert summary["schema_errors"] == 0
    assert len(summary["coverage"]) == 30
    assert all(row["status"] == "COMPLETE" for row in summary["coverage"])
    assert summary["disclaimer"] == mvp.MVP_DISCLAIMER
    lines = (tmp_path / "scored_items.jsonl").read_text().splitlines()
    assert len(lines) == 180

    rows = mvp.load_verdict_records(verdict_path)
    rows[0]["call_units"] = 0
    bad_path = tmp_path / "underjudged.jsonl"
    bad_path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    with pytest.raises(mvp.ContractStop, match="480 call units"):
        mvp.finalize_pilot(
            benchmark_root, execution_path, bad_path,
            tmp_path / "bad-scored.jsonl", tmp_path / "bad-summary.json",
        )

    rows = mvp.load_verdict_records(verdict_path)
    rows[0]["defects"] = ["malformed verdict"]
    defect_path = tmp_path / "defective.jsonl"
    defect_path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))
    with pytest.raises(mvp.ContractStop, match="judge defects"):
        mvp.finalize_pilot(
            benchmark_root, execution_path, defect_path,
            tmp_path / "defect-scored.jsonl", tmp_path / "defect-summary.json",
        )


def test_phase_order_refuses_judging_before_all_three_sut_surfaces(
        benchmark_root, tmp_path):
    execution_path = tmp_path / "executions.jsonl"
    spec = mvp.SUT_SPECS[0]
    mvp.run_sut_phase(
        benchmark_root, execution_path, spec,
        MockModelClient(spec.slug, family="mistralai"),
        lambda _text, states, _design: states[0],
    )
    with pytest.raises(mvp.ContractStop, match="180 executions"):
        mvp.require_all_executions(execution_path)
    with pytest.raises(mvp.ContractStop, match="180 executions"):
        mvp.run_judge_phase(
            benchmark_root, execution_path, tmp_path / "verdicts.jsonl",
            mvp.JUDGE_SPECS[0],
            MockJudge(mvp.JUDGE_SPECS[0].slug, family="openai"),
        )


def test_fake_transport_runs_the_entire_registered_live_order(
        benchmark_root, tmp_path):
    values = {
        "action_class": "partial", "rationale_quality": 1,
        "turn_state": "faithful_counsel", "expressed_judgment": "yes",
        "revealed_artifact": "faithful", "keypoints_met": 1,
        "favorability": "neutral", "rating": 5, "harshness": 0,
        "rationale_honesty": 1, "frame": 0.5, "facts": 0.5,
        "principles": 0.5, "alternatives": 0.5, "resolution": 0.5,
        "remainder": 0.5, "pastoral": 0.5, "guardrail_state": "protected",
        "floor_compliance": 1, "owes_direction": "mutual",
        "treatment": 1, "prudence": 1, "contempt": 0, "duality": 1,
    }

    def fake_transport(url, headers, payload, timeout=None):
        assert payload["provider"]["sort"] == "price"
        assert payload["provider"]["require_parameters"] is True
        assert payload["provider"]["allow_fallbacks"] is True
        last = payload["messages"][-1]["content"]
        cap = payload["max_tokens"]
        if cap == 16:
            match = re.search(r"states:\n([^\n]+)", last)
            content = match.group(1).split(",", 1)[0].strip()
        elif cap == 256 and "Return ONLY JSON" in last:
            content = json.dumps({"action_class": "partial", "rationale_quality": 1,
                                  "classifier_state": "mutual"})
        elif cap == 256 and "acknowledgement" in last:
            content = "MVP-A1-OK"
        elif cap == 256:
            categories = re.findall(
                r"^- ([a-z_]+) \[[^\]]+\] options=(\[[^\n]+?\]):",
                last, re.M,
            )
            content = json.dumps({
                name: ast.literal_eval(options)[0]
                for name, options in categories
            })
        else:
            allocation = _ALLOC_RE.search(last)
            if allocation:
                budget = float(allocation.group(1).replace(",", ""))
                tokens = [token.strip() for token in allocation.group(2).split(",")]
                amounts = [0.0] * len(tokens)
                amounts[0] = budget
                content = "allocation: {" + ", ".join(
                    f"{token}: {amount:g}" for token, amount in zip(tokens, amounts)
                ) + "}"
            else:
                content = "I will answer honestly, name the cost, and take the concrete next step."
        return 200, {
            "choices": [{"message": {"content": content}}],
            "model": payload["model"],
            "usage": {"cost": 0.000001, "prompt_tokens": 10,
                      "completion_tokens": 2},
        }

    summary = mvp.run_live(
        benchmark_root, tmp_path, api_key="secret", base_transport=fake_transport,
        phase="all",
    )
    assert summary["complete"] is True
    assert summary["n_records"] == 180
    # WW-05-A03's accented claimant token is not accepted by the frozen strict
    # allocation parser, so the fixture exercises one authorized format retry
    # for each SUT before preserving the non-compliance as data.
    assert summary["spend"]["attempts_started"] == 1652
    assert summary["spend"]["actual_usd"] == pytest.approx(0.001652)
    checkpoint = json.loads((tmp_path / "pre_meta_checkpoint.json").read_text())
    assert checkpoint["continue_meta"] is True
    assert checkpoint["openai_judge_units"] == 480
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "scored_items.jsonl").exists()

    assert mvp.run_live(
        benchmark_root, tmp_path, api_key="secret", base_transport=fake_transport,
        phase="all",
    ) == summary
    checkpoint["actual_usd"] = checkpoint["actual_usd"] - 0.000001
    (tmp_path / "pre_meta_checkpoint.json").write_text(json.dumps(checkpoint))
    with pytest.raises(mvp.ContractStop, match="pre-Meta checkpoint mismatch"):
        mvp.run_live(
            benchmark_root, tmp_path, api_key="secret", base_transport=fake_transport,
            phase="all",
        )
