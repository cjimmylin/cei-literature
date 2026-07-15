from __future__ import annotations

import json
import sys
import threading
import time
from pathlib import Path
from types import SimpleNamespace

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import pilot2_analysis as analysis  # noqa: E402
import pilot2_live as live  # noqa: E402
import pilot2_oauth_canary as oauth_canary  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
from wcfbench import load_items  # noqa: E402

from test_pilot2_protocol import _manifest, _ok_response  # noqa: E402


def _authorized_manifest():
    manifest = _manifest()
    manifest["authorization_gate"]["paid_inference"] = True
    manifest["authorization_gate"]["credential_access"] = True
    manifest["planning_cost"]["proposed_cap_usd"] = 27.03
    manifest["auth_balance"]["required_balance_usd"] = 27.03
    return manifest


def _write_manifest(path, manifest=None):
    path.write_text(json.dumps(manifest or _authorized_manifest()), encoding="utf-8")
    return path


def _write_full_checkpoints(run_dir):
    items = load_items(str(preflight.BANK_DIR))
    rows = []
    for sut in preflight.SUTS:
        for item in items:
            rows.append({
                "kind": "pilot2_cell", "cell_key": f"{sut}::{item.id}",
                "sut": sut, "item_id": item.id, "status": "response",
                "final_answer": "Fixture final answer.",
                "response_sha256": "a" * 64,
            })
    (run_dir / live.CHECKPOINT_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def _write_oauth_pass(path):
    packet = oauth_canary.build_fixture_packet()
    path.write_text(json.dumps({
        "schema_version": 1,
        "validity_label": preflight.VALIDITY_LABEL,
        "status": "PASS",
        "record_count": 16,
        "unique_record_count": 16,
        "missing_record_ids": [],
        "stop_kind": None,
        "stop_reason": None,
        "input_sha256": packet["input_sha256"],
    }), encoding="utf-8")
    return path


def test_resume_recovers_settled_provider_canary_without_reissuing_transport(
    tmp_path, monkeypatch,
):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(manifest_path, tmp_path / "run", cap_usd=27.03)
    first_spec = preflight.SUT_SPECS[0]
    response = _ok_response(first_spec, cost=0.001)
    original_validate = live.controller.validate_provider_response

    def interrupt_after_settlement(_spec, _response):
        raise KeyboardInterrupt("fixture interruption after settlement")

    monkeypatch.setattr(
        live.controller, "validate_provider_response", interrupt_after_settlement)
    with pytest.raises(KeyboardInterrupt, match="after settlement"):
        live.run_provider_canaries(manifest, state, lambda _payload: response)

    monkeypatch.setattr(
        live.controller, "validate_provider_response", original_validate)
    resumed = live.prepare_run(
        manifest_path, state.run_dir, cap_usd=27.03, resume=True)
    resumed_calls = []

    def transport(payload):
        resumed_calls.append(payload["model"])
        spec = next(spec for spec in preflight.SUT_SPECS
                    if spec.slug == payload["model"])
        return _ok_response(spec, cost=0.001)

    outcomes = live.run_provider_canaries(manifest, resumed, transport)
    assert len(outcomes) == 5
    assert first_spec.slug not in resumed_calls
    evidence = [json.loads(line) for line in
                (state.run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert sum(row.get("kind") == "provider_canary_response"
               and row.get("sut") == first_spec.slug for row in evidence) == 1
    assert sum(row.get("kind") == "cost_settlement"
               and row.get("request_id") == f"canary::{first_spec.slug}::1"
               for row in evidence) == 1


def test_resume_reconstructs_duplicate_request_settlements_additively(tmp_path):
    manifest_path = _write_manifest(tmp_path / "manifest.json")
    state = live.prepare_run(manifest_path, tmp_path / "run", cap_usd=27.03)
    state.reserve("historical-duplicate-id", 0.01)
    state.settle("historical-duplicate-id", 0.001)
    state.reserve("historical-duplicate-id", 0.01)
    state.settle("historical-duplicate-id", 0.005)

    resumed = live.prepare_run(
        manifest_path, state.run_dir, cap_usd=27.03, resume=True)
    assert resumed.spent_usd == pytest.approx(0.006)


def test_terminal_shard_failure_stops_peers_before_another_cell_starts(
    monkeypatch,
):
    manifest = _authorized_manifest()
    state = SimpleNamespace(first_validated=set(), completed={})
    failure_observed = threading.Event()
    calls_after_failure = []
    first_item_by_sut = {}
    monkeypatch.setattr(live, "run_provider_canaries", lambda *_args: [])

    def fake_run_cell(cell, **kwargs):
        if kwargs.get("require_reasoning_gate"):
            first_item_by_sut[cell.sut] = cell.item_id
            state.first_validated.add(cell.sut)
            return {"status": "response"}
        if cell.sut == preflight.SUTS[0]:
            failure_observed.set()
            raise live.CustodyStop("fixture terminal shard failure")
        if not failure_observed.is_set():
            failure_observed.wait(timeout=2)
            time.sleep(0.1)
            return {"status": "response"}
        calls_after_failure.append(cell.key)
        raise AssertionError("peer started transport after terminal shard failure")

    monkeypatch.setattr(live, "run_cell", fake_run_cell)
    with pytest.raises(live.CustodyStop, match="terminal shard failure"):
        live.execute(manifest, state, lambda _payload: {})
    assert calls_after_failure == []


def test_peer_already_in_cell_does_not_retry_after_shard_cancellation(tmp_path):
    manifest = _authorized_manifest()
    state = live.prepare_run(
        _write_manifest(tmp_path / "manifest.json", manifest),
        tmp_path / "run", cap_usd=27.03)
    cell = live.build_cells(manifest)[0]
    spec = preflight.SUT_SPECS[0]
    cancelled = threading.Event()
    calls = []

    def transport(_payload):
        calls.append(True)
        cancelled.set()
        return {**_ok_response(spec, cost=0.001),
                "error": {"message": "retryable upstream error"}}

    with pytest.raises(live.CustodyStop, match="peer shard cancelled"):
        live.run_cell(
            cell, manifest=manifest, state=state, transport=transport,
            items={item.id: item for item in
                   load_items(str(preflight.BANK_DIR))},
            cancellation=cancelled)
    assert len(calls) == 1


@pytest.mark.parametrize("surface", ["canary", "cell"])
def test_ambiguous_transport_failure_is_terminal_without_zero_settlement(
    tmp_path, surface,
):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(manifest_path, tmp_path / "run", cap_usd=27.03)

    def timeout(_payload):
        raise live.TransportFailure("timeout after request submission")

    with pytest.raises(live.CustodyStop, match="ambiguous.*transport"):
        if surface == "canary":
            live.run_provider_canaries(manifest, state, timeout)
        else:
            cell = live.build_cells(manifest)[0]
            live.run_cell(
                cell, manifest=manifest, state=state, transport=timeout,
                items={item.id: item for item in
                       load_items(str(preflight.BANK_DIR))})
    evidence = [json.loads(line) for line in
                (state.run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert sum(row.get("kind") in {
        "provider_canary_request", "sut_request"} for row in evidence) == 1
    assert not any(row.get("kind") == "cost_settlement" for row in evidence)
    assert any(row.get("kind") == "terminal_stop" for row in evidence)


@pytest.mark.parametrize("authorized, canary_status", [
    (False, "PASS"),
    (True, "FAIL"),
])
def test_full_run_judge_requires_paid_manifest_and_registered_oauth_pass(
    tmp_path, authorized, canary_status,
):
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    manifest = _authorized_manifest()
    manifest["authorization_gate"]["paid_inference"] = authorized
    (run_dir / live.MANIFEST_COPY).write_text(
        json.dumps(manifest), encoding="utf-8")
    _write_full_checkpoints(run_dir)
    canary_path = _write_oauth_pass(tmp_path / "canary-report.json")
    if canary_status == "FAIL":
        report = json.loads(canary_path.read_text())
        report["status"] = "FAIL"
        canary_path.write_text(json.dumps(report), encoding="utf-8")
    judge_calls = []

    class MustNotRunJudge:
        def judge(self, batch):
            judge_calls.append(batch)
            raise AssertionError("judge invoked before authorization gates")

    with pytest.raises(analysis.AnalysisError, match=(
            "paid authorization" if not authorized else "OAuth canary PASS")):
        analysis.run_judge_driver(
            run_dir, oauth_canary_report=canary_path,
            judge_factory=lambda _persist: MustNotRunJudge())
    assert judge_calls == []
