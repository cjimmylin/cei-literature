from __future__ import annotations

import copy
import json
import multiprocessing
import os
import sys
import threading
from pathlib import Path

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import pilot2_analysis as analysis  # noqa: E402
import pilot2_live as live  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
import pilot2_run as controller  # noqa: E402
from wcfbench import load_items  # noqa: E402

from test_pilot2_protocol import (  # noqa: E402
    _catalog_and_endpoints, _manifest, _ok_response,
)


def _authorized_manifest():
    manifest = _manifest()
    manifest["authorization_gate"].update({
        "credential_access": True,
        "oauth_canary": True,
        "paid_inference": True,
    })
    manifest["planning_cost"]["proposed_cap_usd"] = live.STRICT_CAP_USD
    manifest["auth_balance"]["required_balance_usd"] = live.STRICT_CAP_USD
    return manifest


def _write_manifest(path: Path, manifest) -> Path:
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def _response_record(spec, *, content: str, cost: float, error=None):
    response = _ok_response(spec, content=content, cost=cost)
    if error is not None:
        response["error"] = error
    return response


def write_completed_run_evidence(
    tmp_path: Path, *, error_cell_key: str | None = None,
):
    """Write only evidence shapes emitted by the current Pilot 2 runner."""
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(
        manifest_path, tmp_path / "run", cap_usd=live.STRICT_CAP_USD)
    items = {item.id: item for item in load_items(str(preflight.BANK_DIR))}
    cells = live.build_cells(manifest)
    first_item_id = manifest["schedule"]["all_item_ids"][0]
    evidence = []
    checkpoints = []
    cumulative = 0.0
    model_attempts = {sut: 0 for sut in preflight.SUTS}

    def settle(request_id, actual, maximum):
        nonlocal cumulative
        evidence.append({
            "kind": "reservation", "request_id": request_id,
            "maximum_usd": maximum,
        })
        cumulative += actual
        return {
            "kind": "cost_settlement", "request_id": request_id,
            "response_attributed_cost_usd": actual,
            "cumulative_spend_usd": cumulative,
        }

    for spec in preflight.SUT_SPECS:
        request_id = f"canary::{spec.slug}::1"
        maximum = live._maximum_cost(manifest, spec.slug)
        response = _response_record(
            spec, content="17 is prime.", cost=0.00001)
        response_hash = live._response_hash(response)
        settlement = settle(request_id, 0.00001, maximum)
        evidence.extend([{
            "kind": "provider_canary_request", "request_id": request_id,
            "sut": spec.slug, "attempt": 1,
            "payload": {"model": spec.slug},
        }, {
            "kind": "provider_canary_response", "request_id": request_id,
            "sut": spec.slug, "attempt": 1,
            "raw_response": response,
            "response_sha256": response_hash,
            "response_attributed_cost_usd": 0.00001,
        }, settlement, {
            "kind": "provider_canary_validation", "sut": spec.slug,
            "status": "PASS", "attempt": 1,
            "response_sha256": response_hash,
        }])
    evidence.append({
        "kind": "phase_completion", "phase": live.PHASE_PROVIDER_CANARIES,
        "status": "PASS", "passed": 5,
    })

    def add_cell(cell, *, first: bool):
        spec = next(spec for spec in preflight.SUT_SPECS if spec.slug == cell.sut)
        attempts = 3 if cell.key == error_cell_key else 1
        final_error = None
        for attempt in range(1, attempts + 1):
            model_attempts[cell.sut] += 1
            model_attempt = model_attempts[cell.sut]
            request_id = f"cell::{cell.key}::{attempt}"
            maximum = live._maximum_cost(manifest, cell.sut)
            response_error = ({"message": "fixture upstream error"}
                              if cell.key == error_cell_key else None)
            response = _response_record(
                spec, content="Fixture final answer.", cost=0.00001,
                error=response_error)
            response_hash = live._response_hash(response)
            settlement = settle(request_id, 0.00001, maximum)
            payload = controller.build_sut_request(
                manifest, cell.sut, live.build_blind_messages(items[cell.item_id]))
            evidence.extend([{
                "kind": "sut_request", "request_id": request_id,
                "cell_key": cell.key, "sut": cell.sut,
                "item_id": cell.item_id, "cell_attempt": attempt,
                "model_attempt": model_attempt,
                "diagnostic_only": cell.diagnostic_only,
                "scorable": cell.scorable, "payload": payload,
            }, {
                "kind": "sut_response", "request_id": request_id,
                "cell_key": cell.key, "sut": cell.sut,
                "item_id": cell.item_id, "cell_attempt": attempt,
                "model_attempt": model_attempt,
                "diagnostic_only": cell.diagnostic_only,
                "scorable": cell.scorable, "raw_response": response,
                "response_sha256": response_hash,
                "response_attributed_cost_usd": 0.00001,
                **({"status": "upstream_error"} if response_error else {
                    "status": "response",
                    "final_answer": "Fixture final answer.",
                    "private_reasoning": "private chain",
                    "reasoning_tokens": 5,
                }),
            }, settlement])
            if response_error:
                final_error = str(response_error)
        base = {
            "kind": "pilot2_cell", "cell_key": cell.key,
            "sut": cell.sut, "item_id": cell.item_id,
            "score": None, "attempts": attempts,
            "diagnostic_only": cell.diagnostic_only,
            "scorable": cell.scorable,
        }
        if cell.key == error_cell_key:
            checkpoints.append({
                **base, "status": "error", "missing": True,
                "error": final_error,
            })
        else:
            checkpoints.append({
                **base, "status": "response", "missing": False,
                "final_answer": "Fixture final answer.",
                "response_sha256": response_hash,
            })
        if first:
            evidence.append({
                "kind": "first_cell_validation", "sut": cell.sut,
                "cell_key": cell.key, "status": "PASS",
            })

    first_cells = [cell for cell in cells if cell.item_id == first_item_id]
    for cell in first_cells:
        add_cell(cell, first=True)
    evidence.append({
        "kind": "phase_completion", "phase": live.PHASE_FIRST_CELLS,
        "status": "PASS", "passed": 5,
    })
    for cell in cells:
        if cell.item_id != first_item_id:
            add_cell(cell, first=False)
    evidence.append({
        "kind": "phase_completion", "phase": live.PHASE_REMAINING_RUN,
        "status": "PASS", "completed_cells": 1150,
        "scorable_cells": 1130, "diagnostic_only_cells": 20,
    })
    (state.run_dir / live.EVIDENCE_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in evidence), encoding="utf-8")
    (state.run_dir / live.CHECKPOINT_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in checkpoints), encoding="utf-8")
    return state.run_dir, manifest, cells


def _write_synthetic_checkpoint_only_run(tmp_path: Path):
    manifest = _authorized_manifest()
    state = live.prepare_run(
        _write_manifest(tmp_path / "manifest.json", manifest),
        tmp_path / "run", cap_usd=live.STRICT_CAP_USD)
    cells = live.build_cells(manifest)
    first_item_id = manifest["schedule"]["all_item_ids"][0]
    evidence = [
        *({"kind": "provider_canary_validation", "sut": sut, "status": "PASS"}
          for sut in preflight.SUTS),
        {"kind": "phase_completion", "phase": live.PHASE_PROVIDER_CANARIES,
         "status": "PASS"},
        *({"kind": "first_cell_validation", "sut": sut,
           "cell_key": f"{sut}::{first_item_id}", "status": "PASS"}
          for sut in preflight.SUTS),
        {"kind": "phase_completion", "phase": live.PHASE_FIRST_CELLS,
         "status": "PASS"},
        {"kind": "phase_completion", "phase": live.PHASE_REMAINING_RUN,
         "status": "PASS"},
    ]
    checkpoints = [{
        "kind": "pilot2_cell", "cell_key": cell.key,
        "sut": cell.sut, "item_id": cell.item_id,
        "status": "response", "missing": False, "score": None,
        "final_answer": "fabricated", "response_sha256": "a" * 64,
        "attempts": 1, "diagnostic_only": cell.diagnostic_only,
        "scorable": cell.scorable,
    } for cell in cells]
    (state.run_dir / live.EVIDENCE_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in evidence), encoding="utf-8")
    (state.run_dir / live.CHECKPOINT_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in checkpoints), encoding="utf-8")
    return state.run_dir, manifest


def _rewrite_first(path: Path, predicate, mutate) -> None:
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    index = next(index for index, row in enumerate(rows) if predicate(row))
    mutate(rows[index])
    path.write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def test_completed_run_rejects_synthetic_checkpoint_only_evidence(tmp_path):
    run_dir, manifest = _write_synthetic_checkpoint_only_run(tmp_path)
    with pytest.raises(live.CustodyStop, match="request|response|evidence"):
        live.require_completed_run_evidence(run_dir, manifest)


def test_completed_run_accepts_exact_linked_response_and_missing_evidence(tmp_path):
    manifest = _authorized_manifest()
    error_cell = next(
        cell for cell in live.build_cells(manifest)
        if cell.item_id != manifest["schedule"]["all_item_ids"][0])
    run_dir, manifest, _cells = write_completed_run_evidence(
        tmp_path, error_cell_key=error_cell.key)
    rows = live.require_completed_run_evidence(run_dir, manifest)
    assert len(rows) == 1150
    missing = next(row for row in rows if row["cell_key"] == error_cell.key)
    assert missing["status"] == "error"
    assert missing["missing"] is True and missing["score"] is None
    assert missing["attempts"] == 3


def test_completed_run_rejects_tampered_cumulative_spend(tmp_path):
    run_dir, manifest, _cells = write_completed_run_evidence(tmp_path)
    _rewrite_first(
        run_dir / live.EVIDENCE_FILE,
        lambda row: row.get("kind") == "cost_settlement",
        lambda row: row.__setitem__("cumulative_spend_usd", -999),
    )
    with pytest.raises(live.CustodyStop, match="cumulative"):
        live.require_completed_run_evidence(run_dir, manifest)


def test_concurrent_settlements_persist_cumulative_spend_in_evidence_order(
    tmp_path, monkeypatch,
):
    state = live.RunState(run_dir=tmp_path, cap_usd=1.0)
    state.reserve("request-1", 0.4)
    state.reserve("request-2", 0.4)
    original_append = live._append_unlocked
    first_writing = threading.Event()
    release_first = threading.Event()
    second_started = threading.Event()
    second_done = threading.Event()

    def blocked_append(path, value):
        if (value.get("kind") == "cost_settlement"
                and value.get("request_id") == "request-1"):
            first_writing.set()
            assert release_first.wait(timeout=5)
        original_append(path, value)

    def settle_second():
        second_started.set()
        state.settle("request-2", 0.2)
        second_done.set()

    monkeypatch.setattr(live, "_append_unlocked", blocked_append)
    first = threading.Thread(target=state.settle, args=("request-1", 0.1))
    second = threading.Thread(target=settle_second)
    first.start()
    assert first_writing.wait(timeout=5)
    second.start()
    assert second_started.wait(timeout=5)
    assert not second_done.wait(timeout=0.1)
    release_first.set()
    first.join(timeout=5)
    second.join(timeout=5)
    assert not first.is_alive() and not second.is_alive()
    settlements = [
        row for row in live._read_jsonl(tmp_path / live.EVIDENCE_FILE)
        if row.get("kind") == "cost_settlement"
    ]
    running = 0.0
    for row in settlements:
        running += row["response_attributed_cost_usd"]
        assert row["cumulative_spend_usd"] == pytest.approx(running)


@pytest.mark.parametrize("mismatch", [
    "checkpoint_hash", "final_answer", "attempts", "settlement_cost",
    "request_model", "duplicate_request",
])
def test_completed_run_rejects_mismatched_or_duplicate_linkage(tmp_path, mismatch):
    run_dir, manifest, cells = write_completed_run_evidence(tmp_path)
    cell = cells[0]
    request_id = f"cell::{cell.key}::1"
    if mismatch == "checkpoint_hash":
        _rewrite_first(
            run_dir / live.CHECKPOINT_FILE,
            lambda row: row.get("cell_key") == cell.key,
            lambda row: row.__setitem__("response_sha256", "b" * 64))
    elif mismatch == "final_answer":
        _rewrite_first(
            run_dir / live.CHECKPOINT_FILE,
            lambda row: row.get("cell_key") == cell.key,
            lambda row: row.__setitem__("final_answer", "mismatch"))
    elif mismatch == "attempts":
        _rewrite_first(
            run_dir / live.CHECKPOINT_FILE,
            lambda row: row.get("cell_key") == cell.key,
            lambda row: row.__setitem__("attempts", 2))
    elif mismatch == "settlement_cost":
        _rewrite_first(
            run_dir / live.EVIDENCE_FILE,
            lambda row: row.get("kind") == "cost_settlement"
            and row.get("request_id") == request_id,
            lambda row: row.__setitem__("response_attributed_cost_usd", 0.00002))
    elif mismatch == "request_model":
        _rewrite_first(
            run_dir / live.EVIDENCE_FILE,
            lambda row: row.get("kind") == "sut_request"
            and row.get("request_id") == request_id,
            lambda row: row["payload"].__setitem__("model", "wrong/model"))
    else:
        evidence_path = run_dir / live.EVIDENCE_FILE
        rows = [json.loads(line) for line in evidence_path.read_text().splitlines()]
        duplicate = copy.deepcopy(next(
            row for row in rows if row.get("kind") == "sut_request"
            and row.get("request_id") == request_id))
        rows.append(duplicate)
        evidence_path.write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    with pytest.raises(live.CustodyStop):
        live.require_completed_run_evidence(run_dir, manifest)


def _hold_live_phase(manifest_path, run_dir, acquired, release):
    os.environ["OPENROUTER_API_KEY"] = "fixture-secret"

    def hold(*_args):
        acquired.set()
        if not release.wait(timeout=10):
            raise AssertionError("fixture lease holder timed out")

    result = live.main([
        "--go", "--manifest", str(manifest_path),
        "--output-dir", str(run_dir), "--cap", str(live.STRICT_CAP_USD),
        "--resume", "--phase", live.PHASE_FIRST_CELLS,
    ], runtime_fetch=_catalog_and_endpoints,
        balance_fetch=lambda _key: {"limit_remaining": live.STRICT_CAP_USD},
        transport_factory=lambda _key: lambda _payload: {},
        authorization_validator=lambda _manifest: None,
        phase_functions={phase: hold for phase in live.PHASES})
    if result != 0:
        raise AssertionError(f"fixture holder exited {result}")


def _hold_direct_lease(run_dir, acquired, release):
    with live.exclusive_run_lease(run_dir):
        acquired.set()
        if not release.wait(timeout=10):
            raise AssertionError("fixture direct lease holder timed out")


def _live_main_args(manifest_path, run_dir):
    return [
        "--go", "--manifest", str(manifest_path),
        "--output-dir", str(run_dir), "--cap", str(live.STRICT_CAP_USD),
        "--resume", "--phase", live.PHASE_FIRST_CELLS,
    ]


def test_process_lease_identity_stays_stable_when_missing_parent_appears(tmp_path):
    run_dir = tmp_path / "later-created" / "run"
    lease_before = live._run_lease_path(run_dir)
    context = multiprocessing.get_context("fork")
    acquired = context.Event()
    release = context.Event()
    holder = context.Process(
        target=_hold_direct_lease, args=(run_dir, acquired, release))
    holder.start()
    assert acquired.wait(timeout=10)
    try:
        run_dir.parent.mkdir()
        assert live._run_lease_path(run_dir) == lease_before
        with pytest.raises(live.CustodyStop, match="holds the run lease"):
            with live.exclusive_run_lease(run_dir):
                pass
    finally:
        release.set()
        holder.join(timeout=10)
        if holder.is_alive():
            holder.terminate()
            holder.join(timeout=5)
    assert holder.exitcode == 0


def test_process_lease_blocks_live_and_analysis_before_private_work_then_releases(
    tmp_path, monkeypatch,
):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    run_dir = live.prepare_run(
        manifest_path, tmp_path / "run", cap_usd=live.STRICT_CAP_USD).run_dir
    monkeypatch.setenv("OPENROUTER_API_KEY", "fixture-secret")
    context = multiprocessing.get_context("fork")
    acquired = context.Event()
    release = context.Event()
    holder = context.Process(
        target=_hold_live_phase,
        args=(manifest_path, run_dir, acquired, release))
    holder.start()
    assert acquired.wait(timeout=10)
    private_events = []
    phases = {phase: (lambda *_args: private_events.append("phase"))
              for phase in live.PHASES}
    try:
        assert live.main(
            _live_main_args(manifest_path, run_dir),
            runtime_fetch=_catalog_and_endpoints,
            balance_fetch=lambda _key: private_events.append("balance") or {
                "limit_remaining": live.STRICT_CAP_USD},
            transport_factory=lambda _key: private_events.append("transport") or (
                lambda _payload: {}),
            authorization_validator=lambda _manifest: None,
            phase_functions=phases) == 2
        assert private_events == []
        judge_events = []
        assert analysis.main([
            "--go", "--run-dir", str(run_dir),
            "--oauth-canary-report", str(tmp_path / "unused.json"),
        ], driver=lambda *_args, **_kwargs: judge_events.append("judge")) == 2
        assert judge_events == []
    finally:
        release.set()
        holder.join(timeout=10)
        if holder.is_alive():
            holder.terminate()
            holder.join(timeout=5)
    assert holder.exitcode == 0
    assert live.main(
        _live_main_args(manifest_path, run_dir),
        runtime_fetch=_catalog_and_endpoints,
        balance_fetch=lambda _key: {"limit_remaining": live.STRICT_CAP_USD},
        transport_factory=lambda _key: lambda _payload: {},
        authorization_validator=lambda _manifest: None,
        phase_functions={phase: (lambda *_args: None) for phase in live.PHASES}) == 0
    judge_events = []
    assert analysis.main([
        "--go", "--run-dir", str(run_dir),
        "--oauth-canary-report", str(tmp_path / "unused.json"),
    ], driver=lambda *_args, **_kwargs: judge_events.append("judge")) == 0
    assert judge_events == ["judge"]
