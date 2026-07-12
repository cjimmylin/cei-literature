from copy import deepcopy
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
import pytest

import analysis.power as power
from analysis.bt import fit_bradley_terry
from analysis.power import (
    ALPHA,
    DEFAULT_SIMULATIONS,
    FIXED_SEED,
    TARGET_POWER,
    flatness_eligibility,
    generate_power_report,
    validate_power_report,
)


def test_power_report_is_deterministic_prerun_only_and_covers_registered_claims():
    first = generate_power_report(simulations=300, seed=FIXED_SEED)
    second = generate_power_report(simulations=300, seed=FIXED_SEED)
    assert first == second
    assert ALPHA == 0.05
    assert TARGET_POWER == 0.80
    assert DEFAULT_SIMULATIONS == 10_000
    assert first["evidence_eligibility"] == "PRE_RUN_ONLY"
    assert first["empirical_status"] == "NOT_EMPIRICAL"
    by_name = {row["claim"]: row for row in first["claims"]}
    assert set(by_name) == {
        "smallest_pair_x_tier_cell",
        "pair_x_tier_flip",
        "ladder_rank_and_dispersion",
        "cg",
        "triad_coherence",
    }
    smallest = by_name["smallest_pair_x_tier_cell"]
    assert smallest["p1_n"] == 3
    assert smallest["official_n"] == 9
    for row in first["claims"]:
        assert row["evidence_eligibility"] == "PRE_RUN_ONLY"
        assert row["empirical_status"] == "NOT_EMPIRICAL"
        if row["estimated_power"] is None:
            assert row["claim_status"] == "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
            assert row["profile_flatness_eligible"] is False
        elif row["estimated_power"] < TARGET_POWER:
            assert row["claim_status"] == "UNDERPOWERED_DESCRIPTIVE"
            assert row["profile_flatness_eligible"] is False


def test_each_power_claim_uses_truthful_metric_specific_assumptions_and_mde_grid():
    report = generate_power_report(simulations=250, seed=31)
    by_name = {row["claim"]: row for row in report["claims"]}
    expected_method_fragments = {
        "smallest_pair_x_tier_cell": "exact binomial",
        "pair_x_tier_flip": "paired two-proportion",
        "ladder_rank_and_dispersion": "Bradley-Terry MM refit",
        "cg": "conditional certified-cell binomial",
        "triad_coherence": "trial-level conditional triangle-reversal MCMC",
    }
    expected_assumption_keys = {
        "smallest_pair_x_tier_cell": {"null_choice_probability", "alternative_choice_probability"},
        "pair_x_tier_flip": {"low_tier_probability", "high_tier_probability", "paired_test"},
        "ladder_rank_and_dispersion": {
            "norm_count",
            "pair_count",
            "rank_recovery_floor",
            "dispersion_error_ceiling",
            "estimator",
            "dispersion_metric",
            "direction_assignment",
            "true_direction_coefficient",
        },
        "cg": {"conditioning", "null_conformance", "alternative_conformance"},
        "triad_coherence": {
            "conditioning_statistics",
            "identifiability",
            "unconditional_sensitivity_promotion_forbidden",
            "tail",
        },
    }
    assert len({row["method"] for row in report["claims"]}) == 5
    assert len({row["effect_unit"] for row in report["claims"]}) == 5
    for name, row in by_name.items():
        assert expected_method_fragments[name] in row["method"]
        assert expected_assumption_keys[name] <= set(row["assumptions"])
        assert row["alpha"] == ALPHA
        assert row["target_power"] == TARGET_POWER
        if name == "triad_coherence":
            assert row["mde_grid"] == []
            assert row["p1_mde_status"] == "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
            assert row["official_mde_status"] == "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
            continue
        assert row["mde_grid"]
        assert row["p1_mde_status"] in {"GRID_ESTIMATED", "NOT_POWERABLE_AT_FROZEN_GRID"}
        assert row["official_mde_status"] in {"GRID_ESTIMATED", "NOT_POWERABLE_AT_FROZEN_GRID"}
        if row["p1_mde_status"] == "NOT_POWERABLE_AT_FROZEN_GRID":
            assert row["p1_mde"] is None
        if row["official_mde_status"] == "NOT_POWERABLE_AT_FROZEN_GRID":
            assert row["official_mde"] is None


def test_triad_power_fails_closed_until_observed_win_margins_exist():
    report = generate_power_report(simulations=250, seed=37)
    triad = next(row for row in report["claims"] if row["claim"] == "triad_coherence")

    assert triad["p1_n"] == 3
    assert triad["official_n"] == 9
    assert triad["method"] == "trial-level conditional triangle-reversal MCMC"
    assert triad["target_effect"] is None
    assert triad["p1_estimated_power"] is None
    assert triad["official_estimated_power"] is None
    assert triad["estimated_power"] is None
    assert triad["p1_mde"] is None and triad["official_mde"] is None
    assert triad["claim_status"] == "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
    assert triad["flatness_status"] == "INELIGIBLE_NOT_ESTIMABLE"
    assert triad["profile_flatness_eligible"] is False
    assert "win margins" in triad["assumptions"]["conditioning_statistics"]
    assert triad["assumptions"]["unconditional_sensitivity_promotion_forbidden"] is True


def test_power_validator_rejects_numeric_unconditional_triad_substitution():
    report = generate_power_report(simulations=100, seed=39)
    forged = deepcopy(report)
    triad = next(row for row in forged["claims"] if row["claim"] == "triad_coherence")
    triad["method"] = "independent complete-triad binomial approximation"
    triad["assumptions"] = {
        "independent_complete_triads": 84,
        "null_violation_rate": 0.25,
        "alternative_violation_rate": 0.15,
        "tail": "LOWER",
    }
    triad["target_effect"] = 0.10
    triad["p1_estimated_power"] = 0.90
    triad["official_estimated_power"] = 0.99
    triad["estimated_power"] = 0.90
    triad["p1_mde"] = 0.08
    triad["official_mde"] = 0.04
    triad["p1_mde_status"] = "GRID_ESTIMATED"
    triad["official_mde_status"] = "GRID_ESTIMATED"
    triad["mde_grid"] = [0.04, 0.08, 0.10]
    triad["claim_status"] = "POWER_ADEQUATE_PRE_RUN"
    triad["profile_flatness_eligible"] = True
    triad["flatness_status"] = "ELIGIBLE"
    with pytest.raises(ValueError, match="conditional|not.estimable|assumptions|recomput"):
        validate_power_report(forged)


def test_ladder_contract_requires_bt_refit_registered_dispersion_and_zero_direction():
    report = generate_power_report(simulations=100, seed=41)
    ladder = next(
        row for row in report["claims"] if row["claim"] == "ladder_rank_and_dispersion"
    )
    assert "Bradley-Terry MM refit" in ladder["method"]
    assert ladder["assumptions"]["estimator"] == "vectorized Bradley-Terry MM MLE"
    assert ladder["assumptions"]["dispersion_metric"] == "registered ladder_dispersion_100"
    assert "balanced" in ladder["assumptions"]["direction_assignment"]
    assert ladder["assumptions"]["true_direction_coefficient"] == 0.0


def test_power_validator_rejects_borda_raw_imbalance_ladder_substitution():
    report = generate_power_report(simulations=100, seed=42)
    forged = deepcopy(report)
    ladder = next(
        row for row in forged["claims"] if row["claim"] == "ladder_rank_and_dispersion"
    )
    ladder["method"] = "Borda total-win rank with raw edge imbalance"
    ladder["assumptions"]["estimator"] = "Borda total wins"
    ladder["assumptions"]["dispersion_metric"] = "raw observed edge imbalance"
    with pytest.raises(ValueError, match="metric-specific|assumptions|recomput"):
        validate_power_report(forged)


def test_vectorized_ladder_bt_matches_production_fit_on_fixed_balanced_tournament():
    pairs = list(combinations(range(9), 2))
    trials_per_pair = 20
    planted = np.linspace(1.0, -1.0, 9)
    probabilities = np.asarray(
        [1.0 / (1.0 + np.exp(-(planted[a] - planted[b]))) for a, b in pairs]
    )
    wins_a = 2 * np.rint(trials_per_pair * probabilities / 2.0).astype(int)
    rows = []
    for pair_index, (a0, b0) in enumerate(pairs):
        a, b = a0 + 1, b0 + 1
        for direction in ("A_FIRST", "B_FIRST"):
            rows.extend(
                {
                    "status": "SCORED_ACTION",
                    "pair": f"{a}x{b}",
                    "severity_tier": "T1",
                    "framing_arm": "neutral",
                    "served_commandment": a,
                    "bt_eligible": True,
                    "outcome_class": "duty_a",
                    "direction_permutation": direction,
                }
                for _ in range(wins_a[pair_index] // 2)
            )
            rows.extend(
                {
                    "status": "SCORED_ACTION",
                    "pair": f"{a}x{b}",
                    "severity_tier": "T1",
                    "framing_arm": "neutral",
                    "served_commandment": b,
                    "bt_eligible": True,
                    "outcome_class": "duty_b",
                    "direction_permutation": direction,
                }
                for _ in range((trials_per_pair - wins_a[pair_index]) // 2)
            )

    vectorized = power._bt_tournament_metrics(
        wins_a[None, :], trials_per_pair
    )
    production = fit_bradley_terry(rows)["strata"][0]
    assert vectorized["valid"][0]
    vector_rank = list(np.argsort(-vectorized["strengths"][0]))
    production_rank = [
        int(norm) - 1
        for norm, _ in sorted(
            production["strengths"].items(),
            key=lambda item: item[1]["estimate"],
            reverse=True,
        )
    ]
    assert vector_rank == production_rank
    assert vectorized["dispersion_100"][0] == pytest.approx(
        production["dispersion_100"], abs=0.05
    )


def test_power_validator_recomputes_and_rejects_self_consistent_numeric_forgery():
    report = generate_power_report(simulations=100, seed=43)
    forged = deepcopy(report)
    row = forged["claims"][0]
    row["p1_estimated_power"] = 0.99
    row["estimated_power"] = 0.99
    row["p1_mde"] = row["mde_grid"][0]
    row["p1_mde_status"] = "GRID_ESTIMATED"
    row["claim_status"] = "POWER_ADEQUATE_PRE_RUN"
    row["profile_flatness_eligible"] = True
    row["flatness_status"] = "ELIGIBLE"

    with pytest.raises(ValueError, match="recomput|deterministic"):
        validate_power_report(forged)


def test_power_validator_rejects_simulation_method_drift():
    report = generate_power_report(simulations=100, seed=47)
    forged = deepcopy(report)
    forged["simulation_method"] = "generic normal-shift simulation"
    with pytest.raises(ValueError, match="simulation method|frozen contract"):
        validate_power_report(forged)


def test_power_validator_rejects_generic_method_substitution():
    report = generate_power_report(simulations=100, seed=33)
    forged = deepcopy(report)
    forged["claims"][1]["method"] = forged["claims"][0]["method"]
    forged["claims"][1]["effect_unit"] = forged["claims"][0]["effect_unit"]
    with pytest.raises(ValueError, match="metric-specific|assumptions"):
        validate_power_report(forged)


def test_flatness_requires_power_at_or_above_point_eighty():
    assert flatness_eligibility(0.799999) == "INELIGIBLE_UNDERPOWERED"
    assert flatness_eligibility(0.80) == "ELIGIBLE"
    with pytest.raises(ValueError):
        flatness_eligibility(float("nan"))


def test_forged_power_promotion_fails_closed():
    report = generate_power_report(simulations=100, seed=9)
    forged = deepcopy(report)
    forged["claims"][0]["evidence_eligibility"] = "EMPIRICAL"
    forged["claims"][0]["claim_status"] = "CONFIRMATORY"
    with pytest.raises(ValueError, match="PRE_RUN_ONLY|promotion"):
        validate_power_report(forged)


def test_power_cli_writes_json_and_markdown(tmp_path):
    script = Path(__file__).resolve().parents[1] / "analysis" / "power.py"
    completed = subprocess.run(
        [
            sys.executable,
            str(script),
            "--simulations", "120",
            "--seed", "23",
            "--output-dir", str(tmp_path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    json_path = tmp_path / "power-report.json"
    md_path = tmp_path / "power-report.md"
    assert json_path.is_file() and md_path.is_file()
    report = json.loads(json_path.read_text(encoding="utf-8"))
    assert validate_power_report(report) is True
    assert "PRE_RUN_ONLY" in md_path.read_text(encoding="utf-8")
