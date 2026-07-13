"""W4 G5 blind reference-neutrality driver (mock-only tests)."""
import hashlib
import json
import re
import shutil
from pathlib import Path

import pytest

from walkworthy.clients import ModelResponse
from walkworthy.g5_neutrality import (
    G5_JUDGE_MODELS, G5Stop, build_blind_prompt, load_promoted_pairs, main,
    run_g5, validate_judge_models, violates_neutrality,
)
from walkworthy.live_judges import JUDGE_SYSTEM
from walkworthy.rubrics import g5_spec_for


def test_promoted_parser_returns_exact_registered_twenty_pairs(benchmark_root):
    loaded = load_promoted_pairs(Path(benchmark_root))

    assert list(loaded["pairs"]) == ["06-crookedpath", "09-doubleedge"]
    assert [len(loaded["pairs"][design]) for design in loaded["pairs"]] == [10, 10]
    assert all(len(pair["poles"]) == 2
               for pairs in loaded["pairs"].values() for pair in pairs)


def _copy_public_g5(benchmark_root, target):
    root = Path(target)
    shutil.copytree(Path(benchmark_root) / "harness/config/g5",
                    root / "harness/config/g5")
    (root / "DESIGNS").mkdir()
    shutil.copy(Path(benchmark_root) / "DESIGNS/09-doubleedge-seeds.md",
                root / "DESIGNS/09-doubleedge-seeds.md")
    return root


def test_config_hash_and_lint_fail_closed(benchmark_root, tmp_path):
    hash_root = _copy_public_g5(benchmark_root, tmp_path / "hash")
    ref = hash_root / "harness/config/g5/20260712-06-references.md"
    ref.write_text(ref.read_text().replace("Mara", "Mara-tampered", 1))
    with pytest.raises(ValueError, match="hash mismatch"):
        load_promoted_pairs(hash_root)

    lint_root = _copy_public_g5(benchmark_root, tmp_path / "lint")
    ref = lint_root / "harness/config/g5/20260712-06-references.md"
    ref.write_text(ref.read_text().replace("| Frame |", "| MissingFrame |", 1))
    manifest_path = lint_root / "harness/config/g5/manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["designs"]["06-crookedpath"]["promoted_sha256"] = hashlib.sha256(
        ref.read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="reference lint failed"):
        load_promoted_pairs(lint_root)


def test_blind_prompt_excludes_other_pole_and_both_labels(benchmark_root):
    pair = load_promoted_pairs(benchmark_root)["pairs"]["06-crookedpath"][0]
    prompt = build_blind_prompt(pair, 0, g5_spec_for("06-crookedpath"))

    assert pair["poles"][0] in prompt
    assert pair["poles"][1] not in prompt
    assert "graded-absolutism protective-misdirection" not in prompt
    assert "non-conflicting / third-way truthful non-cooperation" not in prompt
    assert "do not reward or penalize the conclusion" in prompt.lower()
    assert all(category.name in prompt for category in g5_spec_for(
        "06-crookedpath").categories)


def test_explicit_model_pair_rejected_order_insensitively():
    assert validate_judge_models(tuple(reversed(G5_JUDGE_MODELS))) == G5_JUDGE_MODELS
    with pytest.raises(ValueError, match="frozen G5 judge pair"):
        validate_judge_models((G5_JUDGE_MODELS[0], "other/model"))


def test_threshold_boundary_half_passes_but_above_half_violates():
    assert not violates_neutrality({"x": 0}, {"x": 0.5})
    assert violates_neutrality({"x": 0}, {"x": 0.5000001})


class ScriptedClient:
    def __init__(self, model, values=None, poison=False):
        self.model = model
        self.family = model.split("/", 1)[0]
        self.values = values or {}
        self.calls = 0
        self.poison = poison

    def complete(self, messages, system=None):
        if self.poison:
            raise AssertionError("checkpointed call was repeated")
        index = self.calls
        self.calls += 1
        value = self.values.get(index, 1)
        names = re.findall(r"^- ([a-z_]+):", messages[0].content, re.M)
        return ModelResponse(
            text=json.dumps({name: value for name in names}),
            model=self.model, family=self.family,
            usage={"cost": 0.01, "prompt_tokens": 2, "completion_tokens": 3})


def _clients(values0=None, values1=None):
    return {
        G5_JUDGE_MODELS[0]: ScriptedClient(G5_JUDGE_MODELS[0], values0),
        G5_JUDGE_MODELS[1]: ScriptedClient(G5_JUDGE_MODELS[1], values1),
    }


def _events(path):
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line]


def test_pass_has_no_reelicitation_and_costs_aggregate(benchmark_root, tmp_path):
    clients = _clients()
    summary = run_g5(benchmark_root, tmp_path / "run", clients)

    assert sum(client.calls for client in clients.values()) == 80
    assert summary["initial_calls"] == 80
    assert summary["reelicitation_calls"] == 0
    assert summary["violations"] == []
    assert summary["complete"] is True
    assert summary["cost"] == {"usd": 0.8, "calls": 80,
                                "prompt_tokens": 160,
                                "completion_tokens": 240}


def test_initial_violation_reelicits_exactly_once_and_persistent_disqualifies(
        benchmark_root, tmp_path):
    # Per judge: initial first pair is calls 0/1; attempt 2 follows 40 initial calls.
    repaired = _clients({0: 0, 1: 1, 40: 0, 41: 0})
    repaired_summary = run_g5(benchmark_root, tmp_path / "repaired", repaired)
    assert [c.calls for c in repaired.values()] == [42, 40]
    assert repaired_summary["initial_violations"] == 1
    assert repaired_summary["reelicitation_calls"] == 2
    assert not repaired_summary["disqualified"]

    persistent = _clients({0: 0, 1: 1, 40: 0, 41: 1})
    persistent_summary = run_g5(benchmark_root, tmp_path / "persistent", persistent)
    assert persistent_summary["reelicitation_calls"] == 2
    assert persistent_summary["disqualified"] == [{
        "design": "06-crookedpath", "judge_model": G5_JUDGE_MODELS[0]}]


def test_both_judges_persistent_writes_stop_summary_then_raises(benchmark_root, tmp_path):
    out = tmp_path / "stop"
    clients = _clients({0: 0, 1: 1, 40: 0, 41: 1},
                       {0: 0, 1: 1, 40: 0, 41: 1})
    with pytest.raises(G5Stop, match="both judges"):
        run_g5(benchmark_root, out, clients)
    summary = json.loads((out / "g5_summary.json").read_text())
    assert summary["complete"] is True
    assert summary["stop_trigger"] == "both_judges_disqualified:06-crookedpath"
    assert sum(client.calls for client in clients.values()) == 84


def test_checkpoint_resume_provenance_duplicates_and_completed_immutability(
        benchmark_root, tmp_path):
    out = tmp_path / "resume"
    first = _clients()
    partial = run_g5(benchmark_root, out, first, max_new_calls=2)
    events = _events(out / "g5_events.jsonl")
    assert partial["complete"] is False
    assert {row["status"] for row in partial["judge_statuses"]} == {"PENDING"}
    assert [(e["pole"], e["judge_model"]) for e in events] == [
        (0, G5_JUDGE_MODELS[0]), (0, G5_JUDGE_MODELS[1])]

    resumed = _clients()
    complete = run_g5(benchmark_root, out, resumed)
    assert complete["complete"] is True
    assert [c.calls for c in resumed.values()] == [39, 39]
    with pytest.raises(ValueError, match="immutable"):
        run_g5(benchmark_root, out, _clients())

    duplicate_out = tmp_path / "duplicate"
    run_g5(benchmark_root, duplicate_out, _clients(), max_new_calls=2)
    event_path = duplicate_out / "g5_events.jsonl"
    event_path.write_text(event_path.read_text() + event_path.read_text().splitlines()[0] + "\n")
    with pytest.raises(ValueError, match="duplicate"):
        run_g5(benchmark_root, duplicate_out, _clients())

    mismatch_out = tmp_path / "mismatch"
    run_g5(benchmark_root, mismatch_out, _clients(), max_new_calls=2)
    event_path = mismatch_out / "g5_events.jsonl"
    rows = _events(event_path)
    rows[0]["prompt_sha256"] = "0" * 64
    event_path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    with pytest.raises(ValueError, match="provenance"):
        run_g5(benchmark_root, mismatch_out, _clients())


def test_parse_defect_fails_call_but_keeps_prior_valid_event(benchmark_root, tmp_path):
    class DefectClient(ScriptedClient):
        def complete(self, messages, system=None):
            if self.calls == 1:
                self.calls += 1
                return ModelResponse(text="{}", model=self.model, family=self.family)
            return super().complete(messages, system)

    clients = _clients()
    clients[G5_JUDGE_MODELS[0]] = DefectClient(G5_JUDGE_MODELS[0])
    out = tmp_path / "defect"
    with pytest.raises(ValueError, match="parse defect"):
        run_g5(benchmark_root, out, clients)
    events = _events(out / "g5_events.jsonl")
    assert len(events) == 2  # first same-pole reliability cell persisted for both judges
    assert all(event["defects"] == [] for event in events)


def test_cli_requires_explicit_exact_model_flags_before_any_live_setup(tmp_path):
    with pytest.raises(SystemExit):
        main(["--benchmark-root", str(tmp_path), "--out", str(tmp_path / "out")])
    with pytest.raises(ValueError, match="frozen G5 judge pair"):
        main(["--benchmark-root", str(tmp_path), "--out", str(tmp_path / "out"),
              "--judge1", G5_JUDGE_MODELS[0], "--judge2", "other/model"])


def test_registered_parser_system_manifest_and_summary_contract(benchmark_root, tmp_path):
    class WrappedClient(ScriptedClient):
        def complete(self, messages, system=None):
            self.systems = getattr(self, "systems", []) + [system]
            response = super().complete(messages, system)
            response.text = "scoring follows\n```json\n" + response.text + "\n```"
            return response

    clients = {model: WrappedClient(model) for model in G5_JUDGE_MODELS}
    out = tmp_path / "contract"
    summary = run_g5(benchmark_root, out, clients)

    assert all(client.systems and set(client.systems) == {JUDGE_SYSTEM}
               for client in clients.values())
    manifest = json.loads((out / "g5_manifest.json").read_text())
    assert manifest["judge_models"] == list(G5_JUDGE_MODELS)
    assert manifest["judge_families"] == ["openai", "google"]
    assert manifest["selected_pairs"] == 20
    assert manifest["initial_reference_scores"] == 80
    assert manifest["category_cell_comparisons"] == 260
    assert len(manifest["system_sha256"]) == 64
    assert summary["selected_pairs"] == 20
    assert summary["initial_reference_scores"] == 80
    assert summary["category_cell_comparisons"] == 260
    assert summary["lint"]["status"] == "PASS"
    assert len(summary["judge_statuses"]) == 4
    assert {row["status"] for row in summary["judge_statuses"]} == {"PASS"}
    assert summary["initial_violation_rows"] == []


def test_manifest_and_returned_model_provenance_fail_closed(benchmark_root, tmp_path):
    out = tmp_path / "manifest"
    run_g5(benchmark_root, out, _clients(), max_new_calls=2)
    manifest_path = out / "g5_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["selected_pairs"] = 19
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="manifest"):
        run_g5(benchmark_root, out, _clients())

    out = tmp_path / "returned"
    run_g5(benchmark_root, out, _clients(), max_new_calls=2)
    event_path = out / "g5_events.jsonl"
    rows = _events(event_path)
    rows[0]["response_model"] = "wrong/model"
    event_path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    with pytest.raises(ValueError, match="provenance"):
        run_g5(benchmark_root, out, _clients())


def test_parse_defect_event_keeps_paid_call_cost_and_is_retryable(benchmark_root, tmp_path):
    class OneDefectClient(ScriptedClient):
        def complete(self, messages, system=None):
            if self.calls == 1:
                self.calls += 1
                return ModelResponse(
                    text="{}", model=self.model, family=self.family,
                    usage={"cost": 0.01, "prompt_tokens": 2, "completion_tokens": 3})
            return super().complete(messages, system)

    out = tmp_path / "defect-ledger"
    clients = _clients()
    clients[G5_JUDGE_MODELS[0]] = OneDefectClient(G5_JUDGE_MODELS[0])
    with pytest.raises(ValueError, match="parse defect"):
        run_g5(benchmark_root, out, clients)
    errors = _events(out / "g5_error_events.jsonl")
    assert len(errors) == 1
    assert errors[0]["cost"] == {
        "usd": 0.01, "calls": 1, "prompt_tokens": 2, "completion_tokens": 3}
    assert errors[0]["defects"]

    summary = run_g5(benchmark_root, out, _clients())
    assert summary["cost"] == {
        "usd": 0.81, "calls": 81, "prompt_tokens": 162, "completion_tokens": 243}


def test_every_initial_violation_gets_one_full_reelicitation_before_stop(
        benchmark_root, tmp_path):
    values = {0: 0, 1: 1, 2: 0, 3: 1, 40: 0, 41: 1, 42: 0, 43: 1}
    one_judge = _clients(values, {})
    summary = run_g5(benchmark_root, tmp_path / "one-judge", one_judge)
    assert [client.calls for client in one_judge.values()] == [44, 40]
    assert summary["initial_violations"] == 2
    assert summary["reelicitation_calls"] == 4
    assert len(summary["initial_violation_rows"]) == 2
    assert len(summary["persistent_violation_rows"]) == 2

    both = _clients(values, values)
    with pytest.raises(G5Stop):
        run_g5(benchmark_root, tmp_path / "both", both)
    assert [client.calls for client in both.values()] == [44, 44]


def test_completed_run_revalidates_custody_before_immutable_stop(benchmark_root, tmp_path):
    out = tmp_path / "completed-custody"
    run_g5(benchmark_root, out, _clients())
    event_path = out / "g5_events.jsonl"
    rows = _events(event_path)
    rows[0]["prompt_sha256"] = "0" * 64
    event_path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    with pytest.raises(ValueError, match="provenance"):
        run_g5(benchmark_root, out, _clients())


def test_same_family_wrong_returned_model_fails_immediately(benchmark_root, tmp_path):
    class WrongModelClient(ScriptedClient):
        def complete(self, messages, system=None):
            response = super().complete(messages, system)
            response.model = "openai/not-the-registered-judge"
            return response

    out = tmp_path / "wrong-model"
    clients = _clients()
    clients[G5_JUDGE_MODELS[0]] = WrongModelClient(G5_JUDGE_MODELS[0])
    with pytest.raises(ValueError, match="returned model"):
        run_g5(benchmark_root, out, clients)
    assert not (out / "g5_events.jsonl").read_text()
    assert len(_events(out / "g5_error_events.jsonl")) == 1


def test_success_order_and_error_failure_indices_are_strict(benchmark_root, tmp_path):
    out = tmp_path / "order"
    run_g5(benchmark_root, out, _clients(), max_new_calls=4)
    event_path = out / "g5_events.jsonl"
    rows = _events(event_path)
    rows[1], rows[2] = rows[2], rows[1]
    event_path.write_text("".join(json.dumps(row) + "\n" for row in rows))
    with pytest.raises(ValueError, match="order"):
        run_g5(benchmark_root, out, _clients())

    out = tmp_path / "failure-index"
    clients = _clients()
    clients[G5_JUDGE_MODELS[0]] = type(
        "Defect", (ScriptedClient,), {
            "complete": lambda self, messages, system=None: ModelResponse(
                text="{}", model=self.model, family=self.family,
                usage={"cost": 0.01, "prompt_tokens": 2, "completion_tokens": 3})
        })(G5_JUDGE_MODELS[0])
    with pytest.raises(ValueError, match="parse defect"):
        run_g5(benchmark_root, out, clients)
    error_path = out / "g5_error_events.jsonl"
    errors = _events(error_path)
    errors[0]["failure_index"] = 2
    error_path.write_text("".join(json.dumps(row) + "\n" for row in errors))
    with pytest.raises(ValueError, match="failure index"):
        run_g5(benchmark_root, out, _clients())


def test_partial_summary_cannot_self_promote_to_complete(benchmark_root, tmp_path):
    out = tmp_path / "partial-promote"
    run_g5(benchmark_root, out, _clients(), max_new_calls=2)
    summary_path = out / "g5_summary.json"
    summary = json.loads(summary_path.read_text())
    summary["complete"] = True
    summary["stop_trigger"] = "both_judges_disqualified:09-doubleedge"
    summary_path.write_text(json.dumps(summary))
    with pytest.raises(ValueError, match="summary provenance"):
        run_g5(benchmark_root, out, _clients())


def test_stop_trigger_is_derived_not_trusted(benchmark_root, tmp_path):
    out = tmp_path / "stop-tamper"
    values = {0: 0, 1: 1, 40: 0, 41: 1}
    with pytest.raises(G5Stop):
        run_g5(benchmark_root, out, _clients(values, values))
    summary_path = out / "g5_summary.json"
    summary = json.loads(summary_path.read_text())
    summary["stop_trigger"] = "both_judges_disqualified:09-doubleedge"
    summary_path.write_text(json.dumps(summary))
    with pytest.raises(ValueError, match="summary provenance"):
        run_g5(benchmark_root, out, _clients())


def test_wrong_model_error_is_valid_custody_and_retryable(benchmark_root, tmp_path):
    class WrongOnceClient(ScriptedClient):
        def complete(self, messages, system=None):
            response = super().complete(messages, system)
            if self.calls == 1:
                response.model = "openai/not-the-registered-judge"
            return response

    out = tmp_path / "wrong-model-resume"
    clients = _clients()
    clients[G5_JUDGE_MODELS[0]] = WrongOnceClient(G5_JUDGE_MODELS[0])
    with pytest.raises(ValueError, match="returned model"):
        run_g5(benchmark_root, out, clients)
    summary = run_g5(benchmark_root, out, _clients())
    assert summary["complete"] is True
    assert summary["error_calls"] == 1
    assert summary["cost"]["calls"] == 81
