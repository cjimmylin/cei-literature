from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest


HARNESS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HARNESS_ROOT not in sys.path:
    sys.path.insert(0, HARNESS_ROOT)

import open_first_mvp_live as live  # noqa: E402
import open_first_mvp_preflight as preflight  # noqa: E402
import open_first_mvp_run as controller  # noqa: E402


PROJECT = Path(HARNESS_ROOT).parent
MANIFEST_PATH = (
    PROJECT / "07-PILOTS" / "20260714-open-first-mvp-authorized-preflight-v2"
    / "open-first-mvp-manifest.json"
)


def _manifest():
    return live.load_frozen_manifest(MANIFEST_PATH)


def _ok_response(*, cost=0.001, content="blind response"):
    return {
        "id": "or-1",
        "choices": [{"message": {"content": content}, "finish_reason": "stop"}],
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 20,
            "cost": cost,
            "completion_tokens_details": {"reasoning_tokens": 0},
        },
        "warnings": [],
    }


def test_frozen_plan_is_exact_six_by_230_and_keeps_dev_diagnostic_only():
    manifest = _manifest()
    cells = live.build_cells(manifest)
    assert tuple(dict.fromkeys(cell.sut for cell in cells)) == preflight.SUTS
    assert len(cells) == 1380
    assert all(sum(cell.sut == sut for cell in cells) == 230 for sut in preflight.SUTS)
    assert sum(cell.diagnostic_only for cell in cells) == 24
    assert all(not cell.scorable for cell in cells if cell.diagnostic_only)


def test_run_setup_copies_and_hashes_manifest_and_resume_identity(tmp_path):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(
        MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    assert state.identity["manifest_sha256"] == live.sha256_file(MANIFEST_PATH)
    assert state.identity["suts"] == list(preflight.SUTS)
    assert state.identity["expected_cells"] == 1380
    assert json.loads((run_dir / live.MANIFEST_COPY).read_text()) == manifest
    resumed = live.prepare_run(
        MANIFEST_PATH, run_dir, cap_usd=8.57, resume=True)
    assert resumed.identity == state.identity
    with pytest.raises(live.CustodyStop, match="identity"):
        live.prepare_run(
            MANIFEST_PATH, run_dir, cap_usd=8.56, resume=True,
            allow_test_cap=True)


def test_one_cell_uses_exact_payload_persists_cost_and_first_guard(tmp_path):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    cell = live.build_cells(manifest)[0]
    sent = []

    record = live.run_cell(
        cell, manifest=manifest, state=state,
        transport=lambda payload: sent.append(payload) or _ok_response())

    item = next(item for item in preflight.load_items(str(preflight.BANK_DIR))
                if item.id == cell.item_id)
    assert sent == [controller.build_sut_request(
        manifest, cell.sut, controller.build_blind_messages(item))]
    assert record["status"] == "response"
    assert record["response_attributed_cost_usd"] == pytest.approx(0.001)
    assert state.budget.spent_usd == pytest.approx(0.001)
    assert state.first_response_validated == {cell.sut}
    lines = [json.loads(line) for line in (run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert [row["kind"] for row in lines] == [
        "sut_request", "sut_response", "first_response_validation"]
    assert lines[1]["response_attributed_cost_usd"] == pytest.approx(0.001)
    resumed = live.prepare_run(
        MANIFEST_PATH, run_dir, cap_usd=8.57, resume=True)
    assert cell.key in resumed.completed_keys
    assert resumed.first_response_validated == {cell.sut}


def test_resume_recovers_costed_success_persisted_before_checkpoint(
        tmp_path, monkeypatch):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    cell = live.build_cells(manifest)[0]
    append_jsonl = live._append_jsonl

    def interrupt_before_checkpoint(path, value, lock):
        if path.name == live.CHECKPOINT_FILE:
            raise RuntimeError("simulated interruption before checkpoint")
        append_jsonl(path, value, lock)

    with monkeypatch.context() as interrupted:
        interrupted.setattr(live, "_append_jsonl", interrupt_before_checkpoint)
        with pytest.raises(RuntimeError, match="simulated interruption"):
            live.run_cell(
                cell, manifest=manifest, state=state,
                transport=lambda _payload: _ok_response())

    assert not (run_dir / live.CHECKPOINT_FILE).exists()
    resumed = live.prepare_run(
        MANIFEST_PATH, run_dir, cap_usd=8.57, resume=True)
    checkpoints = [json.loads(line) for line in
                   (run_dir / live.CHECKPOINT_FILE).read_text().splitlines()]
    assert [row["cell_key"] for row in checkpoints] == [cell.key]
    called = []
    with pytest.raises(live.CustodyStop, match="completed cell"):
        live.run_cell(
            cell, manifest=manifest, state=resumed,
            transport=lambda payload: called.append(payload) or _ok_response())
    assert cell.key in resumed.completed_keys
    assert called == []


def test_reservation_refuses_before_transport_when_manifest_or_outer_cap_would_break(tmp_path):
    manifest = _manifest()
    row = next(row for row in manifest["models"] if row["slug"] == preflight.SUTS[0])
    maximum = live.maximum_attempt_cost(row, manifest)
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(
        MANIFEST_PATH, run_dir, cap_usd=maximum / 2, resume=False,
        allow_test_cap=True)
    called = []
    with pytest.raises(controller.TerminalStop, match="budget cap"):
        live.run_cell(
            live.build_cells(manifest)[0], manifest=manifest, state=state,
            transport=lambda payload: called.append(payload) or _ok_response())
    assert called == []


@pytest.mark.parametrize("response, message", [
    (_ok_response(cost=None), "response-attributed cost"),
    (_ok_response(cost="nonsense"), "response-attributed cost"),
    (_ok_response(cost=999), "maximum reservation"),
])
def test_missing_or_inconsistent_response_cost_is_persisted_then_terminal(
        tmp_path, response, message):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    with pytest.raises(controller.TerminalStop, match=message):
        live.run_cell(
            live.build_cells(manifest)[0], manifest=manifest, state=state,
            transport=lambda _payload: response)
    rows = [json.loads(line) for line in (run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert rows[-1]["kind"] == "sut_response"
    assert "raw_response" in rows[-1]


def test_reasoning_leak_on_first_paid_response_is_persisted_then_stops(tmp_path):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    response = _ok_response()
    response["usage"]["completion_tokens_details"]["reasoning_tokens"] = 1
    with pytest.raises(controller.TerminalStop, match="reasoning tokens"):
        live.run_cell(
            live.build_cells(manifest)[0], manifest=manifest, state=state,
            transport=lambda _payload: response)
    rows = [json.loads(line) for line in (run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert rows[-1]["kind"] == "terminal_stop"
    with pytest.raises(live.CustodyStop, match="terminal stop"):
        live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=True)


def test_registered_retries_share_budget_and_exhausted_error_is_missing(tmp_path):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    cell = live.build_cells(manifest)[0]
    calls = []

    def transport(_payload):
        calls.append(None)
        return {**_ok_response(cost=0.0001), "error": {"message": "upstream"}}

    record = live.run_cell(
        cell, manifest=manifest, state=state, transport=transport)
    assert len(calls) == 3
    assert record["status"] == "error"
    assert record["score"] is None
    assert record["missing"] is True
    assert state.attempts_by_sut[cell.sut] == 3
    assert state.budget.spent_usd == pytest.approx(0.0003)


def test_model_retry_reserve_cannot_consume_later_base_cells(tmp_path):
    manifest = _manifest()
    run_dir = tmp_path / "20260715-open-first-live"
    state = live.prepare_run(MANIFEST_PATH, run_dir, cap_usd=8.57, resume=False)
    cell = live.build_cells(manifest)[0]
    state.retry_attempts_by_sut[cell.sut] = 22
    calls = []

    record = live.run_cell(
        cell, manifest=manifest, state=state,
        transport=lambda _payload: calls.append(None) or {
            **_ok_response(cost=0.0001), "error": {"message": "upstream"}})
    assert len(calls) == 1
    assert record["status"] == "error"
    assert state.attempts_by_sut[cell.sut] == 1
    assert state.retry_attempts_by_sut[cell.sut] == 22


def test_runtime_catalog_and_cli_contract_are_fail_closed(tmp_path):
    manifest = _manifest()
    catalog = {row["slug"]: {"pricing": {
        "prompt": str(row["prices"]["prompt"]),
        "completion": str(row["prices"]["completion"]),
    }} for row in manifest["models"]}
    called = []
    executed = []
    assert live.main([
        "--go", "--manifest", str(MANIFEST_PATH),
        "--output-dir", str(tmp_path / "20260715-live"), "--cap", "8.57",
       ], catalog_fetch=lambda: catalog,
       transport_factory=lambda _key: called.append("factory") or
       (lambda _payload: _ok_response()),
       execute_fn=lambda manifest, state, transport: executed.append(
           (manifest, state, transport)) or []) == 0
    assert called == ["factory"]
    assert len(executed) == 1
    assert live.main([
        "--go", "--manifest", str(MANIFEST_PATH),
        "--output-dir", str(tmp_path / "20260715-live-2"), "--cap", "10.01",
    ], catalog_fetch=lambda: catalog,
       transport_factory=lambda _key: _ok_response,
       execute_fn=lambda *_args: pytest.fail("invalid cap executed")) == 2
