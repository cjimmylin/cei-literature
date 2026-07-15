from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import open_first_mvp_oauth_canary as canary  # noqa: E402
from wcfbench.loader import load_items  # noqa: E402
from wcfbench.routing import scorer_kind  # noqa: E402


def _prompt_rows(command):
    prompt = command[-1]
    return json.loads(prompt[prompt.index("["):])


def _successful_process(command, *, satisfied=True, event_item_type="agent_message"):
    rows = _prompt_rows(command)
    route = rows[0]["record_id"].split("::")[1]
    verdicts = []
    for row in rows:
        criterion_id = row["payload"]["criterion_id"]
        if route == "contested":
            verdict = {
                "criterion_id": criterion_id,
                "verdict": "satisfied" if satisfied else "not_satisfied",
                "reason": "mechanical canary verdict",
            }
        else:
            verdict = {
                "criterion_id": criterion_id,
                "satisfied": satisfied,
                "reason": "mechanical canary verdict",
            }
        verdicts.append({"record_id": row["record_id"], "verdict": verdict})
    output_path = Path(command[command.index("-o") + 1])
    output_path.write_text(json.dumps({"records": verdicts}), encoding="utf-8")
    events = "\n".join(json.dumps(event) for event in [
        {"type": "thread.started", "thread_id": "ephemeral"},
        {"type": "item.completed", "item": {
            "id": "i1", "type": event_item_type,
        }},
        {"type": "turn.completed", "usage": {"input_tokens": 12}},
    ])
    return SimpleNamespace(returncode=0, stdout=events, stderr="")


def test_selection_is_stable_exact_and_uses_persisted_ppp1_bank_criteria():
    first = canary.select_canary_records()
    second = canary.select_canary_records()
    assert first == second
    records = first["records"]
    assert [row["route"] for row in records] == (
        ["open"] * 8 + ["contested"] * 4 + ["episode"] * 4)
    assert len(records) == len({row["record_id"] for row in records}) == 16
    assert records[0]["record_id"] == "canary::open::AGG-C1-005::kp01"
    assert records[-1]["record_id"] == "canary::episode::NARROW-C1-006::kp04"
    assert all(row["sut"] == canary.CANARY_SUT for row in records)
    assert set(first["source_hashes"]) == {
        "ppp1_raw_evidence_sha256", "ppp1_checkpoint_sha256", "bank_tree_sha256",
    }
    assert len(first["input_sha256"]) == 64

    items = {item.id: item for item in load_items(str(canary.BANK_DIR))}
    for row in records:
        assert scorer_kind(items[row["item_id"]]) == row["route"]
        keypoint = items[row["item_id"]].rubric[row["rubric_index"] - 1]
        assert row["payload"]["criterion_id"] == keypoint.criterion
        assert row["points"] == keypoint.points
        assert row["payload"]["response"]


def test_cli_requires_go_before_creating_artifacts_or_invoking_oauth(tmp_path):
    invoked = []
    output = tmp_path / "canary"
    code = canary.main(
        ["--output-dir", str(output)],
        process_runner=lambda *_a, **_k: invoked.append(True),
    )
    assert code == 2
    assert invoked == []
    assert not output.exists()


def test_success_writes_complete_custody_and_weighted_arithmetic(tmp_path):
    output = tmp_path / "canary"
    report = canary.run_canary(
        canary.select_canary_records(), output,
        process_runner=lambda command, **_kwargs: _successful_process(command),
    )
    assert report["status"] == "PASS"
    assert report["record_count"] == 16
    assert report["task_count"] == 3
    assert report["missing_record_ids"] == []
    assert report["arithmetic"]["total"] == {
        "earned_points": 19.5,
        "graded_points": 19.5,
        "possible_points": 19.5,
        "weighted_fraction": 1.0,
    }
    inputs = json.loads((output / "canary-inputs.json").read_text())
    assert inputs["input_sha256"] == canary.select_canary_records()["input_sha256"]
    verdicts = [json.loads(line) for line in
                (output / "verdicts.jsonl").read_text().splitlines()]
    assert len(verdicts) == 16
    assert len(list((output / "tasks").glob("*.events.jsonl"))) == 3
    assert len(list((output / "tasks").glob("*.stderr.txt"))) == 3
    assert len(list((output / "tasks").glob("*.metadata.json"))) == 3
    assert (output / "canary-report.json").exists()
    assert "PASS" in (output / "canary-report.md").read_text()


def test_valid_records_are_persisted_before_missing_record_retry(tmp_path):
    output = tmp_path / "canary"
    calls = []

    def process(command, **_kwargs):
        rows = _prompt_rows(command)
        calls.append([row["record_id"] for row in rows])
        if len(calls) == 2:
            persisted = (output / "verdicts.jsonl").read_text().splitlines()
            assert len(persisted) == 1
        if len(calls) == 1:
            one = rows[:1]
            route = "open"
            verdicts = [{
                "record_id": one[0]["record_id"],
                "verdict": {
                    "criterion_id": one[0]["payload"]["criterion_id"],
                    "satisfied": True,
                    "reason": "persist first",
                },
            }]
            Path(command[command.index("-o") + 1]).write_text(
                json.dumps({"records": verdicts}), encoding="utf-8")
            events = "\n".join(json.dumps(x) for x in [
                {"type": "item.completed", "item": {"type": "agent_message"}},
                {"type": "turn.completed", "usage": {}},
            ])
            return SimpleNamespace(returncode=0, stdout=events, stderr="")
        return _successful_process(command)

    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "PASS"
    assert report["task_count"] == 4
    assert len(calls[0]) == 8
    assert len(calls[1]) == 7


def test_open_mechanical_failure_gets_one_four_record_fallback_only(tmp_path):
    output = tmp_path / "canary"
    sizes = []

    def process(command, **_kwargs):
        sizes.append(len(_prompt_rows(command)))
        if len(sizes) == 1:
            return SimpleNamespace(returncode=1, stdout="", stderr="mechanical failure")
        return _successful_process(command)

    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "PASS"
    assert report["open_fallback_used"] is True
    assert sizes == [8, 4, 4, 4, 4]


def test_exhausted_open_missing_retries_fail_without_four_record_fallback(tmp_path):
    output = tmp_path / "canary"
    sizes = []

    def process(command, **_kwargs):
        sizes.append(len(_prompt_rows(command)))
        output_path = Path(command[command.index("-o") + 1])
        output_path.write_text(json.dumps({"records": []}), encoding="utf-8")
        events = "\n".join(json.dumps(event) for event in [
            {"type": "item.completed", "item": {
                "id": "i1", "type": "agent_message",
            }},
            {"type": "turn.completed", "usage": {"input_tokens": 12}},
        ])
        return SimpleNamespace(returncode=0, stdout=events, stderr="")

    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "FAIL"
    assert report["open_fallback_used"] is False
    assert sizes == [8, 8, 8]


@pytest.mark.parametrize("failure", ["quota", "tool"])
def test_quota_or_tool_gate_stops_without_open_fallback(tmp_path, failure):
    output = tmp_path / failure
    calls = []

    def process(command, **_kwargs):
        calls.append(command)
        if failure == "quota":
            return SimpleNamespace(
                returncode=1, stdout="", stderr="OAuth quota warning: allowance exhausted")
        return _successful_process(command, event_item_type="command_execution")

    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "FAIL"
    assert report["stop_kind"] == (
        "OAUTH_QUOTA" if failure == "quota" else "FORBIDDEN_TOOL")
    assert report["open_fallback_used"] is False
    assert report["task_count"] == 1
    assert len(calls) == 1


def test_verdict_custody_failure_stops_without_open_fallback(tmp_path, monkeypatch):
    output = tmp_path / "custody"
    calls = []

    def process(command, **_kwargs):
        calls.append(command)
        return _successful_process(command)

    def fail_persist(_path, _value):
        raise OSError("disk unavailable")

    monkeypatch.setattr(canary, "_append_jsonl", fail_persist)
    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "FAIL"
    assert report["stop_kind"] == "EVIDENCE_CUSTODY"
    assert report["open_fallback_used"] is False
    assert report["task_count"] == 1
    assert report["record_count"] == 0
    assert len(report["missing_record_ids"]) == 16
    assert len(calls) == 1


def test_task_event_custody_failure_stops_without_open_fallback(tmp_path, monkeypatch):
    output = tmp_path / "task-custody"
    calls = []
    original_write_text = Path.write_text

    def guarded_write_text(path, data, *args, **kwargs):
        if path.name.endswith(".events.jsonl"):
            raise OSError("task evidence unavailable")
        return original_write_text(path, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", guarded_write_text)

    def process(command, **_kwargs):
        calls.append(command)
        return _successful_process(command)

    report = canary.run_canary(
        canary.select_canary_records(), output, process_runner=process)
    assert report["status"] == "FAIL"
    assert report["stop_kind"] == "EVIDENCE_CUSTODY"
    assert report["open_fallback_used"] is False
    assert report["task_count"] == 1
    assert len(calls) == 1


def test_existing_output_directory_is_never_overwritten(tmp_path):
    output = tmp_path / "canary"
    output.mkdir()
    (output / "prior.txt").write_text("immutable", encoding="utf-8")
    with pytest.raises(canary.CanaryError, match="new and absent"):
        canary.run_canary(
            canary.select_canary_records(), output,
            process_runner=lambda *_a, **_k: pytest.fail("must not invoke"),
        )
    assert (output / "prior.txt").read_text() == "immutable"


def test_weighted_arithmetic_treats_contested_ungraded_as_missing():
    selected = canary.select_canary_records()
    verdicts = []
    for index, row in enumerate(selected["records"]):
        if row["route"] == "contested":
            value = "ungraded" if index == 8 else "not_satisfied"
            verdict = {
                "criterion_id": row["payload"]["criterion_id"],
                "verdict": value,
                "reason": "bounded",
            }
        else:
            verdict = {
                "criterion_id": row["payload"]["criterion_id"],
                "satisfied": False,
                "reason": "bounded",
            }
        verdicts.append({"record_id": row["record_id"], "verdict": verdict})
    arithmetic = canary.calculate_weighted_arithmetic(selected["records"], verdicts)
    assert arithmetic["contested"]["possible_points"] == 6.0
    assert arithmetic["contested"]["graded_points"] == 4.0
    assert arithmetic["contested"]["earned_points"] == 0.0
    assert arithmetic["contested"]["weighted_fraction"] == 0.0
