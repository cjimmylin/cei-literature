"""Hermetic contracts for the strict-cap PPP-1 execution entrypoint."""

from __future__ import annotations

import json
import os
import sys
from types import SimpleNamespace

import pytest

HARNESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS not in sys.path:
    sys.path.insert(0, HARNESS)

import ppp1_run as runner  # noqa: E402
from format_bridge_requal import (  # noqa: E402
    BudgetExceeded,
    BudgetGuard,
    JsonlSink,
    OutputPathError,
    PreflightError,
)
from wcfbench import OPEN_AWARD, SETTLED_CORE  # noqa: E402


def _bomb(*_args, **_kwargs):
    raise AssertionError("dry run touched a network/client seam")


def _frozen_catalog():
    return runner.load_frozen_catalog()


def _auth(remaining=30.0, usage=10.0):
    return {"usage": usage, "limit": usage + remaining, "limit_remaining": remaining}


def test_plan_and_identity_are_the_exact_frozen_226_by_three_preview():
    plan = runner.build_execution_plan()
    identity = runner.build_run_identity(plan)

    assert len(plan.normal_items) == 204
    assert len(plan.episode_cells) == 66
    assert len(plan.cell_keys) == 678
    assert len(set(plan.cell_keys)) == 678
    assert identity["runnable_items"] == 226
    assert identity["normal_items"] == 204
    assert identity["episode_items"] == 22
    assert identity["expected_cells"] == 678
    assert identity["suts"] == list(runner.PPP1_SUTS)
    assert identity["judge"] == runner.PPP1_JUDGE
    assert identity["sut_max_tokens"] == 2048
    assert identity["judge_max_tokens"] == 512
    assert identity["budget_usd"] == 23.56
    assert identity["validity_label"] == (
        "EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE")
    assert identity["excluded_dev_set_only_ids"] == [
        "LIB-C2-W305", "LIB-C3-W202", "LIB-C7-008", "LIB-C8-W304"]
    assert identity["catalog_identity"]["source_hash"] == (
        "8aaf8aed304c97244239224bedd4e0677762ea1c69fa8005c429737a49b74268")


def test_default_cli_is_dry_and_output_path_does_not_create_or_call(tmp_path, capsys):
    output = tmp_path / "20260713-ppp1"

    code = runner.main(
        ["--output-dir", str(output)], client_factory=_bomb,
        key_fetch=_bomb, catalog_fetch=_bomb)

    assert code == 0
    assert not output.exists()
    assert "DRY RUN" in capsys.readouterr().out


def test_go_requires_exact_new_dated_dir_before_preflight(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-only")
    existing = tmp_path / "20260713-existing"
    existing.mkdir()

    assert runner.main(["--go"], client_factory=_bomb,
                       key_fetch=_bomb, catalog_fetch=_bomb) == 2
    assert runner.main(["--go", "--output-dir", str(tmp_path / "not-dated")],
                       client_factory=_bomb, key_fetch=_bomb, catalog_fetch=_bomb) == 2
    assert runner.main(["--go", "--output-dir", str(existing)],
                       client_factory=_bomb, key_fetch=_bomb, catalog_fetch=_bomb) == 2
    assert "output" in capsys.readouterr().err.lower()


def test_preflight_requires_balance_and_exact_frozen_catalog_identity():
    catalog = _frozen_catalog()

    runner.validate_preflight(_auth(), catalog)
    with pytest.raises(PreflightError, match="below"):
        runner.validate_preflight(_auth(remaining=23.55), catalog)

    substituted = dict(catalog)
    substituted.pop(runner.PPP1_JUDGE)
    substituted["google/gemini-2.5-flash-preview"] = catalog[runner.PPP1_JUDGE]
    with pytest.raises(PreflightError, match="exact|hash"):
        runner.validate_preflight(_auth(), substituted)

    repriced = json.loads(json.dumps(catalog))
    repriced[runner.PPP1_JUDGE]["pricing"]["completion"] = "0.0000026"
    with pytest.raises(PreflightError, match="hash|price"):
        runner.validate_preflight(_auth(), repriced)


def test_preview_panel_uses_only_gemini_manifest_surfaces_and_one_episode_vote():
    class Judge:
        model = runner.PPP1_JUDGE

        def __init__(self):
            self.prompts = []

        def complete(self, prompt, item_id=None):
            self.prompts.append((prompt, item_id))
            item = runner.build_execution_plan().episode_cells[0].item
            return "\n".join(
                f"{index}: correct — supported by the response"
                for index, _keypoint in enumerate(item.rubric, 1))

    judge = Judge()
    panel = runner.PreviewJudgePanel(judge)
    cell = runner.build_execution_plan().episode_cells[0]

    verdict = panel.score_episode(cell.item, "blind response")

    assert panel.active == [("gemini-flash", "google", judge)]
    assert {OPEN_AWARD, SETTLED_CORE} <= panel.eligible["gemini-flash"]
    assert verdict.score == 1.0
    assert verdict.judges_used == [("gemini-flash", "google")]
    assert len(verdict.per_judge) == 1
    assert judge.prompts[0][0] == runner.build_episode_keypoint_prompt(
        cell.item, "blind response")


def test_evidence_client_checks_reservation_before_call_and_persists_raw(tmp_path):
    events = []

    class Guard(BudgetGuard):
        def before_call(self, *args, **kwargs):
            events.append("guard")
            return super().before_call(*args, **kwargs)

    class Inner:
        model = runner.PPP1_JUDGE
        max_tokens = 512
        usage_log = []

        def complete(self, _prompt, item_id=None):
            events.append("call")
            self.usage_log.append({
                "model": self.model,
                "usage": {"prompt_tokens": 2, "completion_tokens": 1,
                          "total_tokens": 3, "cost": 0.001},
            })
            return "ok"

    sink = JsonlSink(str(tmp_path / "raw.jsonl"))
    sink.touch()
    guard = Guard(runner.MAX_BUDGET_USD, _frozen_catalog())
    client = runner.EvidenceClient(
        Inner(), role="judge", name="gemini-flash", slug=runner.PPP1_JUDGE,
        guard=guard, sink=sink)

    assert client.complete("prompt", item_id="item") == "ok"
    assert events == ["guard", "call"]
    row = json.loads((tmp_path / "raw.jsonl").read_text().splitlines()[0])
    assert row["kind"] == "raw_emission"
    assert row["text"] == "ok"


def test_budget_stop_is_terminal_and_checkpointed(tmp_path):
    item = runner.build_execution_plan().normal_items[0]

    class Stopped:
        usage_log = []

        def complete(self, _prompt, item_id=None):
            raise BudgetExceeded("next-call ceiling exceeds $23.56")

    outcome = runner.run_normal_execution(
        [item], [runner.PPP1_SUTS[0]], {runner.PPP1_SUTS[0]: Stopped()},
        panel=SimpleNamespace(), run_dir=str(tmp_path))

    assert outcome.stop_reason.startswith("BudgetExceeded:")
    records = list(runner.mvp.load_checkpoint(str(tmp_path)).values())
    assert len(records) == 1
    assert records[0]["status"] == "error"
    assert records[0]["stop"]["class"] == "BudgetExceeded"


def test_mocked_end_to_end_writes_complete_append_only_packet_without_network(
        monkeypatch, tmp_path):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-only")
    out = tmp_path / "20260713-ppp1-mocked"
    calls = {"key": 0, "catalog": 0, "client": 0}

    def key_fetch(_key):
        calls["key"] += 1
        return _auth(remaining=30.0, usage=10.0 + calls["key"] * 0.25)

    def catalog_fetch(_key):
        calls["catalog"] += 1
        return _frozen_catalog()

    class NeverCalled:
        usage_log = []

        def __init__(self, model, max_tokens):
            self.model = model
            self.max_tokens = max_tokens

        def complete(self, *_args, **_kwargs):
            raise AssertionError("mock executor must make zero inference calls")

    def client_factory(**kwargs):
        calls["client"] += 1
        return NeverCalled(kwargs["model"], kwargs["max_tokens"])

    def execute(plan, _sut_clients, _panel, run_dir):
        for key in plan.cell_keys:
            item_id, sut = key.split("::", 1)
            runner.mvp.append_checkpoint(run_dir, {
                "cell_key": key, "item_id": item_id, "sut": sut,
                "status": "scored", "timestamp": "2026-07-13T00:00:00",
                "usage": {"calls": []},
            })
        return runner.PreviewRunOutcome(
            expected_cells=678,
            records=list(runner.mvp.load_checkpoint(run_dir).values()),
        )

    code = runner.main(
        ["--go", "--output-dir", str(out)],
        client_factory=client_factory, key_fetch=key_fetch,
        catalog_fetch=catalog_fetch, execute_fn=execute)

    assert code == 0
    assert calls == {"key": 2, "catalog": 1, "client": 4}
    assert {path.name for path in out.iterdir()} == {
        "ppp1-run-identity.json", "raw-evidence.jsonl", "checkpoint.jsonl",
        "ppp1-report.md", "run-metadata.json"}
    metadata = json.loads((out / "run-metadata.json").read_text())
    assert metadata["run_status"] == "COMPLETE"
    assert metadata["recorded_cells"] == 678
    assert metadata["response_attributed_cost_usd"] == 0.0
    assert metadata["key_usage_delta_usd"] == pytest.approx(0.25)
    assert runner.VALIDITY_LABEL in (out / "ppp1-report.md").read_text()

    with pytest.raises(OutputPathError):
        runner.prepare_output_dir(str(out), resume=False)


def test_resume_requires_same_identity_and_writes_numbered_report_metadata(tmp_path):
    plan = runner.build_execution_plan()
    out = tmp_path / "20260713-resume"
    out.mkdir()
    (out / "ppp1-run-identity.json").write_text(
        json.dumps(runner.build_run_identity(plan)), encoding="utf-8")
    (out / "raw-evidence.jsonl").touch()
    (out / "checkpoint.jsonl").touch()
    (out / "ppp1-report.md").write_text("old", encoding="utf-8")
    (out / "run-metadata.json").write_text("{}", encoding="utf-8")

    runner.validate_resume_identity(str(out), plan)
    assert runner.next_artifact_path(str(out), "ppp1-report.md").endswith(
        "ppp1-report-resume-001.md")
    assert runner.next_artifact_path(str(out), "run-metadata.json").endswith(
        "run-metadata-resume-001.json")

    identity = runner.build_run_identity(plan)
    identity["budget_usd"] = 5.0
    (out / "ppp1-run-identity.json").write_text(json.dumps(identity), encoding="utf-8")
    with pytest.raises(OutputPathError, match="identity"):
        runner.validate_resume_identity(str(out), plan)
