"""Deterministic SKIM engineering-diagnostic report contracts."""

import importlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _module():
    return importlib.import_module("analysis.engineering_report")


def _result():
    return {
        "artifact_sha256": {"bank": "a" * 64, "gold": "b" * 64},
        "blockers": ["ONE_SEED", "CHEAP_ENGINEERING_ROSTER"],
        "completed_episodes": 3,
        "config_sha256": "c" * 64,
        "cost_cap_usd": 1.0,
        "data_basis": "external_model_responses",
        "eligible_for_empirical_decision": False,
        "episodes": [
            {
                "cost_usd": 0.01,
                "model_id": "cheap/a",
                "paid_calls": 1,
                "provider": "ProviderA",
                "schedule_index": 0,
                "status": "VALID_TERMINAL",
                "vendor": "vendor-a",
            },
            {
                "cost_usd": 0.02,
                "model_id": "cheap/a",
                "paid_calls": 2,
                "provider": "ProviderA",
                "schedule_index": 1,
                "status": "PARKED_MODEL_CALL_ABORT",
                "vendor": "vendor-a",
            },
            {
                "cost_usd": 0.03,
                "model_id": "cheap/b",
                "paid_calls": 1,
                "provider": "ProviderB",
                "schedule_index": 2,
                "status": "VALID_TERMINAL_AFTER_REPAIR",
                "vendor": "vendor-b",
            },
        ],
        "parked_episodes": 1,
        "paid_calls": 4,
        "preflight_cost_upper_bound_usd": 0.5,
        "resume_provenance": None,
        "run_id": "SKIM-P1-CHEAP-TEST",
        "scheduled_requests": 3,
        "schema_version": 1,
        "seed": 20260711,
        "smoke_result_sha256": "d" * 64,
        "status": "LIVE_ONE_SEED_CHEAP_MODEL_ENGINEERING_DIAGNOSTIC_COMPLETE",
        "study_id": "SKIM-P1",
        "total_cost_usd": 0.06,
        "valid_terminal_episodes": 2,
    }


def _write_canonical(path, payload):
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n",
        encoding="utf-8",
    )


def test_report_is_deterministic_and_keeps_diagnostic_evidence_ineligible(tmp_path):
    module = _module()
    result_path = tmp_path / "diagnostic-result.json"
    _write_canonical(result_path, _result())

    first = module.build_report(result_path)
    second = module.build_report(result_path)

    assert first == second
    assert first["status"] == "ENGINEERING_DIAGNOSTIC_REPORTED"
    assert first["eligible_for_empirical_decision"] is False
    assert first["official_scale_status"] == "NOT_RUN"
    assert first["schedule"] == {
        "scheduled_requests": 3,
        "completed_episodes": 3,
        "valid_terminal_episodes": 2,
        "parked_episodes": 1,
    }
    assert first["cost"]["paid_calls"] == 4
    assert [row["model_id"] for row in first["models"]] == ["cheap/a", "cheap/b"]
    assert first["models"][0]["parked_episodes"] == 1
    assert len(first["source_result_sha256"]) == 64


def test_report_rejects_incomplete_or_promoted_diagnostic(tmp_path):
    module = _module()
    payload = _result()
    payload["completed_episodes"] = 2
    incomplete = tmp_path / "incomplete.json"
    _write_canonical(incomplete, payload)

    with pytest.raises(ValueError, match="complete|schedule"):
        module.build_report(incomplete)

    payload = _result()
    payload["eligible_for_empirical_decision"] = True
    promoted = tmp_path / "promoted.json"
    _write_canonical(promoted, payload)
    with pytest.raises(ValueError, match="ineligible|empirical"):
        module.build_report(promoted)


def test_cli_writes_new_canonical_report_and_refuses_overwrite(tmp_path):
    module = _module()
    result_path = tmp_path / "diagnostic-result.json"
    output_path = tmp_path / "engineering-report.json"
    _write_canonical(result_path, _result())

    assert module.cli(["--result", str(result_path), "--output", str(output_path)]) == 0
    raw = output_path.read_bytes()
    assert raw.endswith(b"\n")
    assert raw == module.canonical_bytes(json.loads(raw))

    with pytest.raises(FileExistsError):
        module.cli(["--result", str(result_path), "--output", str(output_path)])
