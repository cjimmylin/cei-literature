import hashlib
import json

from analysis.synthetic_validation import (
    PROFILE_NAMES,
    canonical_result_bytes,
    render_report,
    run_synthetic_validation,
)
from palter_hashing import canonical_sha256
from pilots.run_synthetic_validation import write_validation


def test_full_synthetic_schedule_has_exact_calls_and_zero_external_cost():
    result = run_synthetic_validation()
    assert result["schema_version"] == "palter-synthetic-validation-v1"
    assert result["status"] == "SYNTHETIC_VALIDATION_COMPLETE_WITH_EMPIRICAL_BLOCKERS"
    assert result["fixture_only"] is True
    assert result["profiles"] == list(PROFILE_NAMES)
    assert result["judge_role_fixtures"] == {
        "reader": ["fixture-reader-alpha", "fixture-reader-beta"],
        "atom_audit": ["fixture-atom-alpha", "fixture-atom-beta"],
    }
    assert result["counts"] == {
        "model_profiles": 3,
        "schedule_rows_per_model": 312,
        "model_outputs": 936,
        "composition_like_outputs_per_model": 232,
        "composition_like_outputs": 696,
        "reader_judge_fixture_calls": 1392,
        "atom_audit_fixture_calls": 1392,
        "judge_role_fixture_calls": 2784,
        "semantic_fixture_calls": 3720,
        "external_calls": 0,
        "cost_usd": 0.0,
    }
    assert result["eligibility"] == {
        "human_bt_status": "NOT_RUN",
        "fine_tune_status": "NOT_RUN",
        "empirical_eligible": False,
        "official_result_eligible": False,
        "publication_eligible": False,
    }


def test_profile_classification_distributions_are_exact_and_complete():
    result = run_synthetic_validation()
    assert result["classification_distributions"] == {
        "fixture-faithful": {
            "composition": {"FIDELITY": 232},
            "recognition": {"CORRECT": 40},
            "detection": {"CORRECT": 40},
        },
        "fixture-palterer": {
            "composition": {"FIDELITY": 40, "PALTER": 192},
            "recognition": {"INCORRECT": 40},
            "detection": {"CORRECT": 20, "INCORRECT": 20},
        },
        "fixture-liar": {
            "composition": {"FIDELITY": 40, "REROUTED_LY": 192},
            "recognition": {"CORRECT": 40},
            "detection": {"CORRECT": 20, "INCORRECT": 20},
        },
    }
    assert sum(
        sum(classes.values())
        for profile in result["classification_distributions"].values()
        for classes in profile.values()
    ) == 936


def test_synthetic_result_is_deterministic_hash_bound_and_no_events():
    first = run_synthetic_validation()
    second = run_synthetic_validation()
    assert first == second
    assert canonical_result_bytes(first) == canonical_result_bytes(second)
    assert len(canonical_sha256(first)) == 64
    assert set(first["audit_hashes"]) == {
        "schema_balance",
        "leakage",
        "linkage_replay",
        "mechanical_replay",
        "lexical_length_baseline",
        "finetune_status",
    }
    assert all(len(value) == 64 for value in first["audit_hashes"].values())
    assert "events" not in first
    report = render_report(first)
    assert "3,720" in report
    assert "NOT_RUN" in report
    assert "fixture-only" in report


def test_writer_creates_only_canonical_summary_report_and_manifest(tmp_path):
    written = write_validation(tmp_path)
    assert {path.name for path in tmp_path.iterdir()} == {
        "synthetic-result.json",
        "report.md",
        "manifest.json",
    }
    result_bytes = (tmp_path / "synthetic-result.json").read_bytes()
    result = json.loads(result_bytes)
    assert result_bytes == canonical_result_bytes(result)
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest == written["manifest"]
    assert manifest["artifacts"]["synthetic_result"]["sha256"] == hashlib.sha256(
        result_bytes
    ).hexdigest()
    report_bytes = (tmp_path / "report.md").read_bytes()
    assert manifest["artifacts"]["report"]["sha256"] == hashlib.sha256(
        report_bytes
    ).hexdigest()
    assert manifest["external_calls"] == 0
    assert manifest["cost_usd"] == 0.0
