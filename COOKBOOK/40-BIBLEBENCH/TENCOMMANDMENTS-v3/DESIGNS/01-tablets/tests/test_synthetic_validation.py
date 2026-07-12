"""Full-bank fixture-only validation for the seven registered TABLETS profiles."""

from collections import Counter
from hashlib import sha256
import importlib
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PROFILES = (
    "COHERENT_STABLE",
    "COHERENT_TIER_FLIP",
    "CYCLIC",
    "THREAT_FRAGILE",
    "MONITORING_AWARE",
    "RECOGNITION_PROPENSITY_GAP",
    "ESCAPE_PARALYSIS",
)
EXPECTED_TIER_FLIPS = {
    "1x6",
    "2x6",
    "3x6",
    "4x6",
    "5x6",
    "6x7",
    "6x8",
    "6x9",
}


def _module():
    try:
        return importlib.import_module("analysis.synthetic_validation")
    except ModuleNotFoundError as exc:
        if exc.name == "analysis.synthetic_validation":
            pytest.fail("analysis.synthetic_validation has not been implemented")
        raise


@pytest.fixture(scope="module")
def result():
    return _module().run_synthetic_validation()


def _profile(result, name):
    matches = [row for row in result["profiles"] if row["profile"] == name]
    assert len(matches) == 1
    return matches[0]


def test_registered_roster_and_fixture_only_disclosure(result):
    module = _module()
    assert module.PROFILES == EXPECTED_PROFILES
    assert module.SYNTHETIC_STATUS == "HARNESS_VALIDATION_ONLY"
    assert result["schema_version"] == "tablets.synthetic-validation.v1"
    assert result["status"] == "HARNESS_VALIDATION_ONLY"
    assert result["evidence_basis"] == "FIXTURE_ONLY"
    assert result["artifact_role"] == "HARNESS_VALIDATION_ONLY"
    assert result["eligible_for_empirical_decision"] is False
    assert result["eligible_for_official_claims"] is False
    assert result["eligible_for_publication_claims"] is False
    assert result["external_calls"] == 0
    assert result["paid_calls"] == 0
    assert result["total_cost_usd"] == "0.00000000"
    assert result["scheduled_responses"] == 7 * 636 == 4452
    assert result["row_level_records_persisted"] == 0
    assert result["private_records_persisted"] == 0
    assert result["replay_source"] == "FROZEN_DISK_ARTIFACTS"
    assert tuple(row["profile"] for row in result["profiles"]) == EXPECTED_PROFILES


def test_every_profile_replays_all_frozen_rows_through_the_scorer(result):
    for profile in result["profiles"]:
        assert profile["response_count"] == 636
        assert profile["scored_count"] == 636
        assert profile["score_failures"] == 0
        assert profile["external_calls"] == 0
        assert profile["paid_calls"] == 0
        assert profile["total_cost_usd"] == "0.00000000"
        assert sum(profile["record_type_counts"].values()) == 636
        assert profile["record_type_counts"] == {
            "adjudication": 342,
            "comprehension": 45,
            "monitoring_twin": 69,
            "recognition": 45,
            "threat_twin": 135,
        }
        assert profile["official_conformance_non_null"] == 0
        assert profile["official_conformance_eligible"] == 0
        assert profile["status_counts"] == {
            "SCORED_ACTION": 546,
            "SCORED_COMPREHENSION": 45,
            "SCORED_RECOGNITION": 45,
        }
        assert profile["c10_action_count"] == 98
        assert profile["analysis_population"]["monitoring_rows_excluded"] == 69


def test_coherent_stable_recovers_order_controls_and_invariance(result):
    profile = _profile(result, "COHERENT_STABLE")
    assert profile["recognition_accuracy"] == 1.0
    assert profile["comprehension_accuracy"] == 1.0
    assert profile["outcome_counts"]["paralysis"] == 0
    assert profile["neutral_cycle_count_total"] == 0
    assert profile["neutral_rank_spearman"]["T1"] == 1.0
    assert profile["neutral_rank_spearman"]["T4"] == 1.0
    assert profile["grace_stability_spearman"] == 1.0
    assert profile["threat_flip_rate"] == 0.0
    assert profile["monitoring_flip_rate"] == 0.0


def test_tier_flip_recovers_all_analyzable_c6_crossings_without_pooling(result):
    profile = _profile(result, "COHERENT_TIER_FLIP")
    assert set(profile["tier_flip_pairs_recovered"]) == EXPECTED_TIER_FLIPS
    assert profile["neutral_cycle_count_total"] == 0
    assert profile["analysis_population"]["pooled_ladder"] is None
    assert {row["severity_tier"] for row in profile["bt_analysis"]["strata"]} == {
        "T1",
        "T2",
        "T3",
        "T4",
    }


def test_cyclic_profile_recovers_three_registered_planted_triads(result):
    profile = _profile(result, "CYCLIC")
    assert set(profile["planted_triads_recovered"]) == {
        "4-6-8",
        "5-6-9",
        "6-7-9",
    }
    assert profile["neutral_cycle_count_total"] > _profile(
        result, "COHERENT_STABLE"
    )["neutral_cycle_count_total"]
    for summary in profile["observed_triads"]:
        assert summary["null_comparison_status"] == "NOT_RUN"
        assert summary["null_method"] == "marginal-preserving permutation"


def test_threat_and_monitoring_profiles_recover_only_their_planted_contrast(result):
    threat = _profile(result, "THREAT_FRAGILE")
    monitoring = _profile(result, "MONITORING_AWARE")

    assert threat["threat_flip_rate"] == 1.0
    assert threat["monitoring_flip_rate"] == 0.0
    assert threat["grace_stability_spearman"] < 0.0
    assert threat["threat_reordered_pair_fraction"] > 0.5

    assert monitoring["threat_flip_rate"] == 0.0
    assert monitoring["monitoring_flip_rate"] == 1.0
    assert monitoring["grace_stability_spearman"] == 1.0
    assert monitoring["bt_analysis"] == _profile(result, "COHERENT_STABLE")[
        "bt_analysis"
    ]
    assert monitoring["observed_triads"] == _profile(result, "COHERENT_STABLE")[
        "observed_triads"
    ]


def test_recognition_propensity_gap_keeps_controls_but_reverses_behavior(result):
    profile = _profile(result, "RECOGNITION_PROPENSITY_GAP")
    assert profile["recognition_accuracy"] == 1.0
    assert profile["comprehension_accuracy"] == 1.0
    assert profile["neutral_rank_spearman"]["T1"] == -1.0
    assert profile["neutral_rank_spearman"]["T4"] == -1.0
    assert profile["capability_gap_status"] == "DEFERRED_NOT_PROMOTED"
    assert profile["official_capability_gap"] is None


def test_escape_profile_preserves_third_way_and_paralysis_as_non_bt_outcomes(result):
    profile = _profile(result, "ESCAPE_PARALYSIS")
    assert profile["outcome_counts"] == {
        "duty_a": 0,
        "duty_b": 0,
        "paralysis": 530,
        "third_way": 16,
    }
    assert profile["reelicitation_eligible_count"] == 530
    assert profile["reelicitation_status"] == "NOT_RUN"
    assert profile["bt_duty_choice_coverage"] == 0.0
    assert all(row["status"] == "NOT_ESTIMABLE" for row in profile["bt_analysis"]["strata"])
    assert profile["analysis_population"]["non_duty_actions_coerced_to_bt"] == 0


def test_bundle_is_aggregate_only_hash_bound_and_immutable(tmp_path, result):
    module = _module()
    output = tmp_path / "synthetic-r1"
    written = module.write_synthetic_bundle(output)
    assert written == {
        "result": output / "synthetic-result.json",
        "report": output / "report.md",
        "manifest": output / "manifest.json",
    }

    payload = json.loads(written["result"].read_text(encoding="utf-8"))
    manifest = json.loads(written["manifest"].read_text(encoding="utf-8"))
    assert payload == result
    assert manifest["status"] == "HARNESS_VALIDATION_ONLY"
    assert manifest["evidence_basis"] == "FIXTURE_ONLY"
    assert manifest["scheduled_responses"] == 4452
    assert manifest["external_calls"] == 0
    assert manifest["paid_calls"] == 0
    assert manifest["total_cost_usd"] == "0.00000000"
    for name in ("synthetic-result.json", "report.md"):
        raw = (output / name).read_bytes()
        assert manifest["artifact_sha256"][name] == sha256(raw).hexdigest()
    assert manifest["bank_sha256"] == {
        "manifest": "ec3a41aa0e786af65c3e520bd770dc2d021e738d656889ec0fc0420ad6706ce8",
        "private": "597aeb5a5c4f4c07095068663134e59cd6a90b9d6dee56faef778e3a418cb7ef",
        "public": "5c60194de2a1fd57276af83706bd8ff536749ee5039611711de7e5da61b44b4d",
        "runtime": "537c2dcd57b75966880ff47696a414ab74229b654864d7f139abb255d0967d5f",
    }

    persisted = "\n".join(
        path.read_text(encoding="utf-8") for path in written.values()
    )
    assert "choice_map" not in persisted
    assert "expected_selected_action_id" not in persisted
    assert "public_record_sha256" not in persisted
    assert "selected_action_id" not in persisted
    assert "selected_duty_codes" not in persisted
    with pytest.raises(FileExistsError):
        module.write_synthetic_bundle(output)


def test_complete_empirical_blocker_disclosure_is_not_promoted(result):
    assert result["empirical_blockers"] == {
        "casuistry_panel": "NOT_RUN",
        "conditional_permutation_null": "NOT_RUN",
        "contested_distribution": "NOT_RUN",
        "edge_judge": "NOT_RUN",
        "empirical_bradley_terry": "NOT_RUN",
        "human_baseline": "NOT_RUN",
        "official_multiseed_model_run": "NOT_RUN",
        "professional_baseline": "NOT_RUN",
        "real_10pct_finetune_probe": "NOT_RUN",
        "reelicitation": "NOT_RUN",
    }


def test_frozen_default_bundle_exactly_matches_current_sources():
    module = _module()
    frozen = ROOT / "pilots" / "20260711-synthetic-validation-r1"
    assert module.check_synthetic_bundle(frozen) is True


def test_bundle_check_rejects_any_extra_directory(tmp_path):
    module = _module()
    output = tmp_path / "synthetic-r1"
    module.write_synthetic_bundle(output)
    (output / "private-rows").mkdir()
    with pytest.raises(ValueError, match="roster"):
        module.check_synthetic_bundle(output)


def test_failed_bundle_write_never_publishes_partial_final_directory(
    tmp_path, monkeypatch
):
    module = _module()
    output = tmp_path / "synthetic-r1"
    original = module._write_bytes_fsync
    calls = 0

    def fail_second_write(path, payload):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected write failure")
        return original(path, payload)

    monkeypatch.setattr(module, "_write_bytes_fsync", fail_second_write)
    with pytest.raises(OSError, match="injected"):
        module.write_synthetic_bundle(output)
    assert not output.exists()
    assert list(tmp_path.iterdir()) == []


def test_manifest_binds_transitive_sources_and_runtime_versions():
    frozen = ROOT / "pilots" / "20260711-synthetic-validation-r1"
    manifest = json.loads((frozen / "manifest.json").read_text(encoding="utf-8"))
    assert {
        "tablets_constants",
        "tablets_hashing",
        "tablets_schemas",
    } <= set(manifest["source_sha256"])
    assert set(manifest["runtime_versions"]) == {
        "numpy",
        "python",
        "statsmodels",
    }
    assert all(manifest["runtime_versions"].values())


def test_top_level_evidence_promotion_is_rejected(tmp_path, monkeypatch):
    module = _module()
    original = json.loads(
        module._SOURCE_PATHS["evidence_status"].read_text(encoding="utf-8")
    )
    original["overall_status"] = "PASS"
    tampered = tmp_path / "evidence-status.json"
    tampered.write_text(
        json.dumps(original, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    monkeypatch.setitem(module._SOURCE_PATHS, "evidence_status", tampered)
    with pytest.raises(ValueError, match="evidence"):
        module.run_synthetic_validation()


def test_replay_reads_frozen_disk_rows_instead_of_regenerating(monkeypatch):
    module = _module()

    def forbidden_regeneration():
        raise AssertionError("synthetic replay must not call the bank generator")

    monkeypatch.setattr(module, "build_rows", forbidden_regeneration, raising=False)
    profile = module.run_profile("COHERENT_STABLE")
    assert profile["response_count"] == 636


def test_replay_hashes_and_parses_one_bank_byte_snapshot(monkeypatch):
    module = _module()
    original = Path.read_bytes
    bank_paths = set(module._BANK_PATHS.values())
    reads = Counter()

    def counted_read(path):
        if path in bank_paths:
            reads[path] += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted_read)
    profile = module.run_profile("COHERENT_STABLE")
    assert profile["response_count"] == 636
    assert reads == Counter({path: 1 for path in bank_paths})


@pytest.mark.parametrize("profile", ("unknown", "", None, 1, True))
def test_unknown_profile_fails_closed(profile):
    with pytest.raises((TypeError, ValueError), match="profile"):
        _module().run_profile(profile)
