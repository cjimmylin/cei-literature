from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

import pytest


HARNESS_ROOT = Path(__file__).resolve().parent.parent
WCF_ROOT = HARNESS_ROOT.parent
if str(HARNESS_ROOT) not in sys.path:
    sys.path.insert(0, str(HARNESS_ROOT))

import pilot2_analysis as analysis  # noqa: E402
import pilot2_live as live  # noqa: E402
import pilot2_oauth_canary as oauth_canary  # noqa: E402
import pilot2_preflight as preflight  # noqa: E402
import pilot2_report as report  # noqa: E402
from wcfbench import load_items, scorer_kind  # noqa: E402

from test_pilot2_protocol import (  # noqa: E402
    _catalog_and_endpoints, _manifest, _ok_response,
)


SOURCE_MANIFEST = (
    WCF_ROOT / "07-PILOTS" / "20260715-pilot2-public-preflight-v3"
    / "pilot2-manifest.json"
)
OWNER_RECORD = (
    WCF_ROOT / "20260715ai-jimmy-pilot2-s62-28-13-execution-authorization-record.md"
)


def _authorized_manifest():
    manifest = _manifest()
    manifest["authorization_gate"].update({
        "credential_access": True,
        "oauth_canary": True,
        "paid_inference": True,
    })
    manifest["planning_cost"]["proposed_cap_usd"] = 28.13
    manifest["auth_balance"]["required_balance_usd"] = 28.13
    return manifest


def _write_manifest(path: Path, manifest=None) -> Path:
    path.write_text(json.dumps(manifest or _authorized_manifest()), encoding="utf-8")
    return path


def _write_exact_canary(output_dir: Path) -> Path:
    output_dir.mkdir()
    packet = oauth_canary.build_fixture_packet()
    (output_dir / "canary-inputs.json").write_text(
        json.dumps(packet), encoding="utf-8")
    verdicts = [{
        "record_id": row["record_id"],
        "result": analysis.synthetic_structured_result(
            row["call_kind"], row["payload"]),
    } for row in packet["records"]]
    (output_dir / "verdicts.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in verdicts), encoding="utf-8")
    report_path = output_dir / "canary-report.json"
    report_path.write_text(json.dumps({
        "schema_version": 1,
        "validity_label": preflight.VALIDITY_LABEL,
        "status": "PASS", "record_count": 16, "unique_record_count": 16,
        "missing_record_ids": [], "stop_kind": None, "stop_reason": None,
        "input_sha256": packet["input_sha256"],
    }), encoding="utf-8")
    return report_path


def _write_completed_mixed_run(tmp_path: Path):
    authorized = tmp_path / "authorized.json"
    manifest = live.bind_authorization(
        SOURCE_MANIFEST, OWNER_RECORD, authorized, cap_usd=28.13)
    state = live.prepare_run(
        authorized, tmp_path / "run", cap_usd=28.13)
    items = {item.id: item for item in load_items(str(preflight.BANK_DIR))}
    first_item_id = manifest["schedule"]["all_item_ids"][0]
    error_cell = next(
        cell for cell in live.build_cells(manifest)
        if cell.sut == preflight.SUTS[0]
        and cell.item_id != first_item_id
        and not items[cell.item_id].extra.get("dev_set_only")
        and scorer_kind(items[cell.item_id]) in {"open", "episode"})
    evidence = [
        *({"kind": "provider_canary_validation", "sut": sut, "status": "PASS"}
          for sut in preflight.SUTS),
        {"kind": "phase_completion", "phase": live.PHASE_PROVIDER_CANARIES,
         "status": "PASS", "passed": 5},
        *({"kind": "first_cell_validation", "sut": sut,
           "cell_key": f"{sut}::{first_item_id}", "status": "PASS"}
          for sut in preflight.SUTS),
        {"kind": "phase_completion", "phase": live.PHASE_FIRST_CELLS,
         "status": "PASS", "passed": 5},
        {"kind": "phase_completion", "phase": live.PHASE_REMAINING_RUN,
         "status": "PASS", "completed_cells": 1150,
         "scorable_cells": 1130, "diagnostic_only_cells": 20},
    ]
    (state.run_dir / live.EVIDENCE_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in evidence), encoding="utf-8")
    checkpoints = []
    for cell in live.build_cells(manifest):
        base = {
            "kind": "pilot2_cell", "cell_key": cell.key,
            "sut": cell.sut, "item_id": cell.item_id,
            "diagnostic_only": cell.diagnostic_only, "scorable": cell.scorable,
            "score": None,
        }
        if cell == error_cell:
            checkpoints.append({
                **base, "status": "error", "missing": True,
                "error": "registered fixture missing response", "attempts": 3,
            })
        else:
            checkpoints.append({
                **base, "status": "response", "missing": False,
                "final_answer": "WLC Q145 and WCF 1.9. RANKING: a < b.",
                "response_sha256": "a" * 64, "attempts": 1,
            })
    (state.run_dir / live.CHECKPOINT_FILE).write_text(
        "".join(json.dumps(row) + "\n" for row in checkpoints), encoding="utf-8")
    return state.run_dir, manifest, items[error_cell.item_id], error_cell


def test_exact_v3_authorization_binder_is_append_only_and_changes_only_registered_fields(
    tmp_path,
):
    source_before = SOURCE_MANIFEST.read_bytes()
    output = tmp_path / "pilot2-authorized-manifest.json"

    bound = live.bind_authorization(
        SOURCE_MANIFEST, OWNER_RECORD, output, cap_usd=28.13)

    assert SOURCE_MANIFEST.read_bytes() == source_before
    assert hashlib.sha256(source_before).hexdigest() == live.V3_MANIFEST_SHA256
    assert bound == json.loads(output.read_text())
    assert bound["authorization_gate"] == {
        **json.loads(source_before)["authorization_gate"],
        "credential_access": True,
        "oauth_canary": True,
        "paid_inference": True,
    }
    restored = copy.deepcopy(bound)
    restored.pop("authorization_binding")
    restored["authorization_gate"].update({
        "credential_access": False,
        "oauth_canary": False,
        "paid_inference": False,
    })
    assert restored == json.loads(source_before)
    assert bound["authorization_binding"] == {
        "kind": "wcf_bench_pilot2_amount_specific_authorization",
        "source_manifest_sha256": live.V3_MANIFEST_SHA256,
        "owner_record": OWNER_RECORD.name,
        "owner_record_sha256": live.OWNER_RECORD_SHA256,
        "strict_cap_usd": 28.13,
    }
    with pytest.raises(live.CustodyStop, match="already exists"):
        live.bind_authorization(
            SOURCE_MANIFEST, OWNER_RECORD, output, cap_usd=28.13)
    with pytest.raises(live.CustodyStop, match="exactly 28.13"):
        live.bind_authorization(
            SOURCE_MANIFEST, OWNER_RECORD, tmp_path / "wrong-cap.json",
            cap_usd=28.12)
    wrong_source = tmp_path / "wrong-source.json"
    wrong_source.write_bytes(source_before + b"\n")
    with pytest.raises(live.CustodyStop, match="immutable v3 hash"):
        live.bind_authorization(
            wrong_source, OWNER_RECORD, tmp_path / "wrong-source-output.json",
            cap_usd=28.13)


def test_first_cell_and_remaining_phases_fail_closed_without_persisted_prior_pass(
    tmp_path,
):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(
        manifest_path, tmp_path / "run", cap_usd=28.13)
    touched = []

    with pytest.raises(live.CustodyStop, match="provider canaries.*PASS"):
        live.execute_first_cells(
            manifest, state, lambda payload: touched.append(payload))
    with pytest.raises(live.CustodyStop, match="first real cells.*PASS"):
        live.execute_remaining_run(
            manifest, state, lambda payload: touched.append(payload))
    assert touched == []


def test_provider_and_first_cell_phases_persist_separate_pass_gates(tmp_path):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    state = live.prepare_run(
        manifest_path, tmp_path / "run", cap_usd=28.13)

    def transport(payload):
        spec = next(spec for spec in preflight.SUT_SPECS
                    if spec.slug == payload["model"])
        return _ok_response(spec, cost=0.001)

    assert len(live.execute_provider_canaries(manifest, state, transport)) == 5
    assert len(live.execute_first_cells(manifest, state, transport)) == 5
    evidence = [json.loads(line) for line in
                (state.run_dir / live.EVIDENCE_FILE).read_text().splitlines()]
    assert [(row["phase"], row["status"]) for row in evidence
            if row.get("kind") == "phase_completion"] == [
        ("provider-canaries", "PASS"),
        ("first-cells", "PASS"),
    ]


def test_live_cli_requires_and_dispatches_exactly_one_registered_phase(
    tmp_path, monkeypatch,
):
    manifest = _authorized_manifest()
    manifest_path = _write_manifest(tmp_path / "manifest.json", manifest)
    base = [
        "--manifest", str(manifest_path), "--output-dir", str(tmp_path / "unused"),
        "--cap", "28.13",
    ]
    with pytest.raises(SystemExit):
        live.main(base, phase_functions={})
    with pytest.raises(SystemExit):
        live.main([*base, "--phase", "all"], phase_functions={})

    monkeypatch.setenv("OPENROUTER_API_KEY", "fixture-secret")
    observed = []
    phase_functions = {
        phase: (lambda _manifest, _state, _transport, phase=phase:
                observed.append(phase))
        for phase in live.PHASES
    }
    for phase in live.PHASES:
        run_dir = tmp_path / phase
        if phase != live.PHASE_PROVIDER_CANARIES:
            live.prepare_run(manifest_path, run_dir, cap_usd=28.13)
        assert live.main([
            "--go", "--manifest", str(manifest_path),
            "--output-dir", str(run_dir), "--cap", "28.13",
            "--phase", phase,
        ], runtime_fetch=_catalog_and_endpoints,
            balance_fetch=lambda _key: {"limit_remaining": 28.13},
            transport_factory=lambda _key: lambda _payload: {},
            authorization_validator=lambda _manifest: None,
            phase_functions=phase_functions) == 0
    assert observed == list(live.PHASES)


def test_live_judge_analysis_driver_requires_completed_run_and_full_canary_custody(
    tmp_path,
):
    authorized = tmp_path / "authorized.json"
    live.bind_authorization(
        SOURCE_MANIFEST, OWNER_RECORD, authorized, cap_usd=28.13)
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    (run_dir / live.MANIFEST_COPY).write_bytes(authorized.read_bytes())

    canary_dir = tmp_path / "oauth-canary"
    canary_dir.mkdir()
    packet = oauth_canary.build_fixture_packet()
    (canary_dir / "canary-report.json").write_text(json.dumps({
        "schema_version": 1,
        "validity_label": preflight.VALIDITY_LABEL,
        "status": "PASS",
        "record_count": 16,
        "unique_record_count": 16,
        "missing_record_ids": [],
        "stop_kind": None,
        "input_sha256": packet["input_sha256"],
    }), encoding="utf-8")

    with pytest.raises(analysis.AnalysisError, match="persisted OAuth canary PASS"):
        analysis.run_live_judge_scoring_analysis(
            run_dir, oauth_canary_report=canary_dir / "canary-report.json",
            judge_factory=lambda _persist: pytest.fail("judge must not run"))


@pytest.mark.parametrize("field,value", [
    ("schema_version", "__MISSING__"),
    ("schema_version", 2),
    ("stop_reason", "__MISSING__"),
    ("stop_reason", "unexpected warning"),
])
def test_oauth_canary_requires_exact_schema_and_null_stop_reason(
    tmp_path, field, value,
):
    report_path = _write_exact_canary(tmp_path / "oauth-canary")
    canary_report = json.loads(report_path.read_text())
    if value == "__MISSING__":
        canary_report.pop(field)
    else:
        canary_report[field] = value
    report_path.write_text(json.dumps(canary_report), encoding="utf-8")

    with pytest.raises(analysis.AnalysisError, match="persisted OAuth canary PASS"):
        analysis._require_persisted_oauth_canary(report_path)


def test_analysis_cli_requires_go_before_driver_invocation(tmp_path, monkeypatch):
    invoked = []
    monkeypatch.setattr(
        analysis, "run_live_judge_scoring_analysis",
        lambda *_args, **_kwargs: invoked.append(True))
    args = [
        "--run-dir", str(tmp_path / "run"),
        "--oauth-canary-report", str(tmp_path / "canary-report.json"),
    ]
    assert analysis.main(args) == 2
    assert invoked == []


def test_live_driver_preserves_exact_geometry_and_writes_consumable_analysis(tmp_path):
    run_dir, _manifest_value, error_item, error_cell = _write_completed_mixed_run(
        tmp_path)
    canary_report = _write_exact_canary(tmp_path / "oauth-canary")
    sent_ids = []

    class FixtureJudge:
        def __init__(self, persist):
            self.persist = persist

        def judge(self, batch):
            rows = []
            for call in batch:
                sent_ids.append(call["record_id"])
                row = {
                    "record_id": call["record_id"],
                    "result": analysis.synthetic_structured_result(
                        call["call_kind"], call["payload"]),
                }
                self.persist(row)
                rows.append(row)
            return {"records": rows, "missing_record_ids": [], "attempts": 1}

    result = analysis.run_live_judge_scoring_analysis(
        run_dir, oauth_canary_report=canary_report,
        judge_factory=lambda persist: FixtureJudge(persist))

    expected_missing = {
        row["record_id"] for row in analysis.build_judge_calls(
            error_item, "", sut=error_cell.sut)
    }
    missing_rows = [json.loads(line) for line in
                    (run_dir / "judge-missing.jsonl").read_text().splitlines()]
    assert result["logical_judge_calls"] == 1740
    assert result["persisted_verdicts"] + result["missing_verdicts"] == 1740
    assert {row["record_id"] for row in missing_rows} == expected_missing
    assert all(row["score"] is None and row["reason"] == "sut_response_missing"
               for row in missing_rows)
    assert expected_missing.isdisjoint(sent_ids)
    assert len(sent_ids) + len(expected_missing) == 1740
    stored = json.loads(Path(result["analysis_json"]).read_text())
    assert len(stored["cells"]) == 1130
    assert len(stored["diagnostic_dev_cells"]) == 20
    assert len(report._require_complete_empirical(stored)) == 5
    with pytest.raises(analysis.AnalysisError, match="already exists"):
        analysis.run_live_judge_scoring_analysis(
            run_dir, oauth_canary_report=canary_report)
