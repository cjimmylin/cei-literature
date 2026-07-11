from copy import deepcopy

from audits.finetune_status import finetune_status
from audits.leakage_audit import run_leakage_audit
from audits.lexical_length_baseline import run_lexical_length_baseline
from audits.linkage_replay_audit import run_linkage_replay
from audits.mechanical_replay_audit import run_mechanical_replay
from audits.schema_balance_audit import run_schema_balance_audit
from itembank.build_bank import build_artifact_bytes
from itembank.generator import build_rows


def test_schema_hash_count_balance_audit_passes_exact_frozen_bank():
    result = run_schema_balance_audit()
    assert result["status"] == "PASS"
    assert result["counts"] == {
        "composition": 160,
        "no_incentive_twin": 40,
        "monitoring_twin": 32,
        "recognition": 40,
        "detection": 40,
        "total": 312,
    }
    assert result["monitoring_balance"] == {
        "fraction_of_primary": 0.2,
        "per_tier": {"T1": 8, "T2": 8, "T3": 8, "T4": 8},
        "per_direction": {"inflate": 16, "deflate": 16},
    }
    assert all(len(value) == 64 for value in result["artifact_sha256"].values())


def test_schema_audit_fails_closed_on_tampered_public_artifact():
    artifacts = build_artifact_bytes()
    damaged = dict(artifacts)
    damaged["public_bank"] = damaged["public_bank"].replace(b'"T1"', b'"TX"', 1)
    result = run_schema_balance_audit(damaged)
    assert result["status"] == "FAIL"
    assert result["findings"]


def test_public_runtime_leakage_audit_passes_and_detects_injected_gold():
    public, _, runtime = build_rows()
    passed = run_leakage_audit(public, runtime)
    assert passed["status"] == "PASS"
    assert passed["rows_scanned"] == {"public": 312, "runtime": 312}
    assert passed["findings"] == []

    forged = [deepcopy(row) for row in public]
    forged[0]["gold_label"] = "paltered"
    failed = run_leakage_audit(forged, runtime)
    assert failed["status"] == "FAIL"
    assert failed["findings"][0]["forbidden_key"] == "gold_label"


def test_linkage_replay_checks_all_reciprocal_pairs_and_parent_matches():
    public, _, _ = build_rows()
    passed = run_linkage_replay(public)
    assert passed["status"] == "PASS"
    assert passed["reciprocal_link_edges"] == 372
    assert passed["monitoring_parent_replays"] == 32

    forged = [deepcopy(row) for row in public]
    monitored = next(row for row in forged if row["record_type"] == "monitoring_twin")
    monitored["paired_record_ids"] = ["missing-record"]
    failed = run_linkage_replay(forged)
    assert failed["status"] == "FAIL"
    assert failed["findings"]


def test_mechanical_action_and_scoring_replay_exercises_fail_closed_paths():
    result = run_mechanical_replay()
    assert result["status"] == "PASS"
    assert result["replay_cases"] == 8
    assert result["composition_scores"] == {"SCORED_PR": 1, "REROUTED_LY": 1}
    assert result["fail_closed_cases"] == 3
    assert result["action_schema_cases"] == {
        "composition": 1,
        "recognition": 1,
        "detection": 1,
    }


def test_lexical_length_baseline_is_deterministic_and_uses_registered_bar():
    first = run_lexical_length_baseline()
    second = run_lexical_length_baseline()
    assert first == second
    assert first["status"] == "COMPLETE"
    assert first["evidence_origin"] == "deterministic_public_surface_audit"
    assert first["sample_count"] == 40
    assert first["label_counts"] == {"faithful": 20, "paltered": 20}
    assert first["fold_count"] == 5
    assert first["features"] == ["lexical_unigrams", "character_length"]
    assert first["chance_balanced_accuracy"] == 0.5
    assert first["decision_threshold"] == 0.6
    assert 0.0 <= first["balanced_accuracy"] <= 1.0
    expected = "PASS" if first["balanced_accuracy"] <= 0.6 else "REWORK"
    assert first["decision"] == expected


def test_finetune_status_is_honestly_not_run_and_never_promoted():
    assert finetune_status() == {
        "status": "NOT_RUN",
        "evidence_origin": None,
        "synthetic_surrogate_run": False,
        "empirical_eligible": False,
        "reason": "the preregistered 10%-fine-tune probe requires a later real training run",
    }
