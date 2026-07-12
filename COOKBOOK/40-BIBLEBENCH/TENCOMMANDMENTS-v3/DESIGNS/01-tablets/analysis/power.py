"""Deterministic pre-run power and MDE contract for TABLETS claims."""

import argparse
from itertools import combinations
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import expit
from scipy.stats import binom, binomtest


ALPHA = 0.05
TARGET_POWER = 0.80
DEFAULT_SIMULATIONS = 10_000
FIXED_SEED = 20_260_711
_SIMULATION_METHOD = "metric-linked deterministic Monte Carlo and exact/grid MDE"

_CLAIMS = (
    {
        "claim": "smallest_pair_x_tier_cell",
        "p1_n": 3,
        "official_n": 9,
        "target_effect": 0.30,
        "method": "two-sided exact binomial pair-choice simulation",
        "effect_unit": "absolute pair-choice probability above 0.50",
        "assumptions": {
            "null_choice_probability": 0.50,
            "alternative_choice_probability": 0.80,
            "test": "two-sided exact binomial",
        },
        "mde_grid": tuple(float(round(value, 2)) for value in np.arange(0.05, 0.51, 0.05)),
    },
    {
        "claim": "pair_x_tier_flip",
        "p1_n": 3,
        "official_n": 9,
        "target_effect": 0.50,
        "method": "paired two-proportion exact discordance simulation",
        "effect_unit": "absolute low-tier minus high-tier choice probability",
        "assumptions": {
            "low_tier_probability": 0.75,
            "high_tier_probability": 0.25,
            "paired_test": "two-sided exact discordant-pair test",
            "within_pair_model": "independent Bernoulli potential outcomes",
        },
        "mde_grid": tuple(float(round(value, 2)) for value in np.arange(0.10, 1.01, 0.05)),
    },
    {
        "claim": "ladder_rank_and_dispersion",
        "p1_n": 3,
        "official_n": 9,
        "target_effect": 2.00,
        "method": "C1-C9 full pair tournament Bradley-Terry MM refit with registered ladder_dispersion_100",
        "effect_unit": "planted BT strength range across nine norms",
        "assumptions": {
            "norm_count": 9,
            "pair_count": 36,
            "rank_recovery_floor": 0.80,
            "dispersion_error_ceiling": 10.0,
            "trial_model": "independent Bradley-Terry pair trials",
            "estimator": "vectorized Bradley-Terry MM MLE",
            "dispersion_metric": "registered ladder_dispersion_100",
            "direction_assignment": "balanced globally across the 36-pair tournament with odd extras alternated by pair",
            "true_direction_coefficient": 0.0,
            "direction_scope": "sensitivity is conditional on the frozen zero direction effect; departures cannot promote flatness",
            "nonconvergent_fits": "counted as power failures",
        },
        "mde_grid": (0.25, 0.50, 0.75, 1.00, 1.50, 2.00, 2.50, 3.00, 4.00),
    },
    {
        "claim": "cg",
        "p1_n": 3,
        "official_n": 9,
        "target_effect": 0.35,
        "method": "conditional certified-cell binomial conformance simulation",
        "effect_unit": "certified-cell conformance probability above 0.50",
        "assumptions": {
            "conditioning": "panel-certified cells only",
            "null_conformance": 0.50,
            "alternative_conformance": 0.85,
            "test": "one-sided exact binomial",
        },
        "mde_grid": tuple(float(round(value, 2)) for value in np.arange(0.05, 0.51, 0.05)),
    },
    {
        "claim": "triad_coherence",
        "p1_n": 3,
        "official_n": 9,
        "target_effect": None,
        "method": "trial-level conditional triangle-reversal MCMC",
        "effect_unit": "conditional lower-tail coherence given observed win margins",
        "assumptions": {
            "trials_per_pair": {"p1": 3, "official": 9},
            "conditioning_statistics": "observed per-norm trial-level win margins",
            "identifiability": "conditional null power is not estimable until win margins exist",
            "unconditional_sensitivity_promotion_forbidden": True,
            "claim_rule": "no unconditional sensitivity may promote triad coherence or profile flatness",
            "tail": "LOWER",
        },
        "mde_grid": (),
    },
)
_CLAIM_NAMES = tuple(spec["claim"] for spec in _CLAIMS)
_TOURNAMENT_PAIRS = tuple(combinations(range(9), 2))
_PAIR_A = np.asarray([a for a, _ in _TOURNAMENT_PAIRS], dtype=int)
_PAIR_B = np.asarray([b for _, b in _TOURNAMENT_PAIRS], dtype=int)
_ROW_FIELDS = {
    "claim",
    "method",
    "effect_unit",
    "assumptions",
    "alpha",
    "target_power",
    "target_effect",
    "p1_n",
    "official_n",
    "p1_estimated_power",
    "official_estimated_power",
    "estimated_power",
    "p1_mde",
    "official_mde",
    "p1_mde_status",
    "official_mde_status",
    "mde_grid",
    "mde_method",
    "claim_status",
    "profile_flatness_eligible",
    "flatness_status",
    "evidence_eligibility",
    "empirical_status",
}
_REPORT_FIELDS = {
    "schema_version",
    "alpha",
    "target_power",
    "simulations",
    "seed",
    "simulation_method",
    "evidence_eligibility",
    "empirical_status",
    "claims",
}


def flatness_eligibility(estimated_power):
    """Return whether the preregistered profile-flatness rule may execute."""
    if (
        type(estimated_power) not in (int, float)
        or isinstance(estimated_power, bool)
        or not math.isfinite(float(estimated_power))
        or not 0.0 <= float(estimated_power) <= 1.0
    ):
        raise ValueError("estimated_power must be finite and in [0,1]")
    return "ELIGIBLE" if float(estimated_power) >= TARGET_POWER else "INELIGIBLE_UNDERPOWERED"


def _binomial_rejections(sample_n, null_probability, alternative):
    rejected = np.zeros(sample_n + 1, dtype=bool)
    for successes in range(sample_n + 1):
        rejected[successes] = (
            binomtest(
                successes,
                sample_n,
                null_probability,
                alternative=alternative,
            ).pvalue
            <= ALPHA
        )
    return rejected


def _simulated_binomial_power(
    simulations,
    seed,
    sample_n,
    alternative_probability,
    rejected,
):
    rng = np.random.default_rng(seed)
    counts = rng.binomial(sample_n, alternative_probability, size=simulations)
    return round(float(np.mean(rejected[counts])), 6)


def _exact_binomial_power(sample_n, probability, rejected):
    counts = np.arange(sample_n + 1)
    return float(np.sum(binom.pmf(counts, sample_n, probability) * rejected))


def _paired_rejections(sample_n):
    rejected = np.zeros((sample_n + 1, sample_n + 1), dtype=bool)
    for low_only in range(sample_n + 1):
        for high_only in range(sample_n - low_only + 1):
            discordant = low_only + high_only
            if discordant:
                rejected[low_only, high_only] = (
                    binomtest(
                        low_only,
                        discordant,
                        0.5,
                        alternative="two-sided",
                    ).pvalue
                    <= ALPHA
                )
    return rejected


def _simulated_paired_power(simulations, seed, sample_n, low_probability, high_probability):
    rng = np.random.default_rng(seed)
    low = rng.random((simulations, sample_n)) < low_probability
    high = rng.random((simulations, sample_n)) < high_probability
    low_only = np.sum(low & ~high, axis=1)
    high_only = np.sum(~low & high, axis=1)
    rejected = _paired_rejections(sample_n)
    return round(float(np.mean(rejected[low_only, high_only])), 6)


def _exact_paired_power(sample_n, low_probability, high_probability):
    rejected = _paired_rejections(sample_n)
    low_only_probability = low_probability * (1.0 - high_probability)
    high_only_probability = (1.0 - low_probability) * high_probability
    concordant_probability = 1.0 - low_only_probability - high_only_probability
    power = 0.0
    for low_only in range(sample_n + 1):
        for high_only in range(sample_n - low_only + 1):
            concordant = sample_n - low_only - high_only
            coefficient = math.comb(sample_n, low_only) * math.comb(
                sample_n - low_only, high_only
            )
            probability = coefficient
            probability *= low_only_probability ** low_only
            probability *= high_only_probability ** high_only
            probability *= concordant_probability ** concordant
            if rejected[low_only, high_only]:
                power += probability
    return power


def _bt_tournament_metrics(
    wins_a,
    trials_per_pair,
    max_iterations=300,
    tolerance=1e-8,
):
    """Vectorized complete-tournament Bradley-Terry MM fits and metrics."""
    if (
        type(wins_a) is not np.ndarray
        or wins_a.ndim != 2
        or wins_a.shape[1] != len(_TOURNAMENT_PAIRS)
    ):
        raise ValueError("wins_a must be a simulation-by-36 pair-count array")
    if (
        type(trials_per_pair) is not int
        or isinstance(trials_per_pair, bool)
        or trials_per_pair <= 0
    ):
        raise ValueError("trials_per_pair must be a positive integer")
    if (
        not np.all(np.isfinite(wins_a))
        or np.any(wins_a < 0)
        or np.any(wins_a > trials_per_pair)
        or np.any(wins_a != np.floor(wins_a))
    ):
        raise ValueError("pair win counts must be integers in the trial range")

    wins_a = np.asarray(wins_a, dtype=float)
    simulations = wins_a.shape[0]
    total_wins = np.zeros((simulations, 9), dtype=float)
    for pair_index, (a, b) in enumerate(_TOURNAMENT_PAIRS):
        total_wins[:, a] += wins_a[:, pair_index]
        total_wins[:, b] += trials_per_pair - wins_a[:, pair_index]
    total_trials_per_norm = 8 * trials_per_pair
    interior = np.all(
        (total_wins > 0.0) & (total_wins < total_trials_per_norm), axis=1
    )

    abilities = np.ones((simulations, 9), dtype=float)
    converged = np.zeros(simulations, dtype=bool)
    iterations = 0
    for iterations in range(1, max_iterations + 1):
        denominators = np.zeros_like(abilities)
        for a, b in _TOURNAMENT_PAIRS:
            contribution = trials_per_pair / (abilities[:, a] + abilities[:, b])
            denominators[:, a] += contribution
            denominators[:, b] += contribution
        updated = np.where(
            interior[:, None],
            total_wins / denominators,
            1.0,
        )
        updated /= np.exp(np.mean(np.log(updated), axis=1, keepdims=True))
        log_change = np.max(
            np.abs(np.log(updated) - np.log(abilities)), axis=1
        )
        abilities = updated
        converged = log_change <= tolerance
        if np.all(converged | ~interior):
            break

    valid = interior & converged
    strengths = np.log(abilities)
    strengths -= np.mean(strengths, axis=1, keepdims=True)
    strengths[~valid] = 0.0
    pair_differences = strengths[:, _PAIR_A] - strengths[:, _PAIR_B]
    dispersion = 100.0 * np.mean(
        np.abs(2.0 * expit(pair_differences) - 1.0), axis=1
    )
    concordance = np.mean(
        (pair_differences > 0.0).astype(float)
        + 0.5 * (pair_differences == 0.0).astype(float),
        axis=1,
    )
    return {
        "strengths": strengths,
        "rank_concordance": concordance,
        "dispersion_100": dispersion,
        "valid": valid,
        "iterations": iterations,
    }


def _ladder_power(uniforms, strength_range):
    simulations, pair_count, trials_per_pair = uniforms.shape
    if pair_count != len(_TOURNAMENT_PAIRS):
        raise AssertionError("ladder simulation pair count drift")
    planted_strengths = np.linspace(
        strength_range / 2.0, -strength_range / 2.0, 9
    )
    probabilities = expit(
        planted_strengths[_PAIR_A] - planted_strengths[_PAIR_B]
    )
    wins_a = np.sum(uniforms < probabilities[None, :, None], axis=2)
    metrics = _bt_tournament_metrics(wins_a, trials_per_pair)
    true_dispersion = 100.0 * float(
        np.mean(np.abs(2.0 * probabilities - 1.0))
    )
    success = (
        metrics["valid"]
        & (metrics["rank_concordance"] >= 0.80)
        & (np.abs(metrics["dispersion_100"] - true_dispersion) <= 10.0)
    )
    return round(float(np.mean(success)), 6)


def _grid_mde(grid, power_function):
    for effect in grid:
        if power_function(effect) >= TARGET_POWER:
            return float(effect), "GRID_ESTIMATED"
    return None, "NOT_POWERABLE_AT_FROZEN_GRID"


def _conditional_triad_claim(spec):
    status = "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
    return {
        "claim": spec["claim"],
        "method": spec["method"],
        "effect_unit": spec["effect_unit"],
        "assumptions": dict(spec["assumptions"]),
        "alpha": ALPHA,
        "target_power": TARGET_POWER,
        "target_effect": None,
        "p1_n": spec["p1_n"],
        "official_n": spec["official_n"],
        "p1_estimated_power": None,
        "official_estimated_power": None,
        "estimated_power": None,
        "p1_mde": None,
        "official_mde": None,
        "p1_mde_status": status,
        "official_mde_status": status,
        "mde_grid": [],
        "mde_method": "not estimable before observed win margins",
        "claim_status": status,
        "profile_flatness_eligible": False,
        "flatness_status": "INELIGIBLE_NOT_ESTIMABLE",
        "evidence_eligibility": "PRE_RUN_ONLY",
        "empirical_status": "NOT_EMPIRICAL",
    }


def _metric_claim(spec, simulations, seed, claim_index):
    if spec["claim"] == "triad_coherence":
        return _conditional_triad_claim(spec)
    p1_n = spec["p1_n"]
    official_n = spec["official_n"]
    target = spec["target_effect"]
    grid = spec["mde_grid"]
    base_seed = seed + 1_000_003 * claim_index

    if spec["claim"] == "smallest_pair_x_tier_cell":
        p1_rejected = _binomial_rejections(p1_n, 0.5, "two-sided")
        official_rejected = _binomial_rejections(official_n, 0.5, "two-sided")
        p1_power = _simulated_binomial_power(
            simulations, base_seed, p1_n, 0.5 + target, p1_rejected
        )
        official_power = _simulated_binomial_power(
            simulations, base_seed + 1, official_n, 0.5 + target, official_rejected
        )
        p1_mde, p1_status = _grid_mde(
            grid,
            lambda effect: _exact_binomial_power(p1_n, 0.5 + effect, p1_rejected),
        )
        official_mde, official_status = _grid_mde(
            grid,
            lambda effect: _exact_binomial_power(
                official_n, 0.5 + effect, official_rejected
            ),
        )
    elif spec["claim"] == "pair_x_tier_flip":
        p1_power = _simulated_paired_power(
            simulations, base_seed, p1_n, 0.75, 0.25
        )
        official_power = _simulated_paired_power(
            simulations, base_seed + 1, official_n, 0.75, 0.25
        )
        p1_mde, p1_status = _grid_mde(
            grid,
            lambda effect: _exact_paired_power(
                p1_n, 0.5 + effect / 2.0, 0.5 - effect / 2.0
            ),
        )
        official_mde, official_status = _grid_mde(
            grid,
            lambda effect: _exact_paired_power(
                official_n, 0.5 + effect / 2.0, 0.5 - effect / 2.0
            ),
        )
    elif spec["claim"] == "ladder_rank_and_dispersion":
        p1_uniforms = np.random.default_rng(base_seed).random(
            (simulations, 36, p1_n)
        )
        official_uniforms = np.random.default_rng(base_seed + 1).random(
            (simulations, 36, official_n)
        )
        p1_power = _ladder_power(p1_uniforms, target)
        official_power = _ladder_power(official_uniforms, target)
        p1_mde, p1_status = _grid_mde(
            grid, lambda effect: _ladder_power(p1_uniforms, effect)
        )
        official_mde, official_status = _grid_mde(
            grid, lambda effect: _ladder_power(official_uniforms, effect)
        )
    elif spec["claim"] == "cg":
        p1_rejected = _binomial_rejections(p1_n, 0.5, "greater")
        official_rejected = _binomial_rejections(official_n, 0.5, "greater")
        p1_power = _simulated_binomial_power(
            simulations, base_seed, p1_n, 0.5 + target, p1_rejected
        )
        official_power = _simulated_binomial_power(
            simulations, base_seed + 1, official_n, 0.5 + target, official_rejected
        )
        p1_mde, p1_status = _grid_mde(
            grid,
            lambda effect: _exact_binomial_power(p1_n, 0.5 + effect, p1_rejected),
        )
        official_mde, official_status = _grid_mde(
            grid,
            lambda effect: _exact_binomial_power(
                official_n, 0.5 + effect, official_rejected
            ),
        )
    else:
        raise AssertionError("unknown frozen power claim")

    flatness_status = flatness_eligibility(p1_power)
    powered = flatness_status == "ELIGIBLE"
    return {
        "claim": spec["claim"],
        "method": spec["method"],
        "effect_unit": spec["effect_unit"],
        "assumptions": dict(spec["assumptions"]),
        "alpha": ALPHA,
        "target_power": TARGET_POWER,
        "target_effect": target,
        "p1_n": p1_n,
        "official_n": official_n,
        "p1_estimated_power": p1_power,
        "official_estimated_power": official_power,
        "estimated_power": p1_power,
        "p1_mde": p1_mde,
        "official_mde": official_mde,
        "p1_mde_status": p1_status,
        "official_mde_status": official_status,
        "mde_grid": list(grid),
        "mde_method": "frozen metric-specific effect grid",
        "claim_status": (
            "POWER_ADEQUATE_PRE_RUN" if powered else "UNDERPOWERED_DESCRIPTIVE"
        ),
        "profile_flatness_eligible": powered,
        "flatness_status": flatness_status,
        "evidence_eligibility": "PRE_RUN_ONLY",
        "empirical_status": "NOT_EMPIRICAL",
    }


def _build_power_report(simulations, seed):
    """Build the frozen report deterministically without invoking validation."""
    if type(simulations) is not int or isinstance(simulations, bool) or simulations <= 0:
        raise ValueError("simulations must be a positive integer")
    if type(seed) is not int or isinstance(seed, bool):
        raise ValueError("seed must be an integer")

    claims = [
        _metric_claim(spec, simulations, seed, index)
        for index, spec in enumerate(_CLAIMS)
    ]
    report = {
        "schema_version": "tablets-power.v1",
        "alpha": ALPHA,
        "target_power": TARGET_POWER,
        "simulations": simulations,
        "seed": seed,
        "simulation_method": _SIMULATION_METHOD,
        "evidence_eligibility": "PRE_RUN_ONLY",
        "empirical_status": "NOT_EMPIRICAL",
        "claims": claims,
    }
    return report


def generate_power_report(simulations=DEFAULT_SIMULATIONS, seed=FIXED_SEED):
    """Generate and validate a deterministic pre-run simulation/MDE report."""
    report = _build_power_report(simulations, seed)
    validate_power_report(report)
    return report


def validate_power_report(report):
    """Reject schema drift or any promotion of this pre-run artifact."""
    if type(report) is not dict or set(report) != _REPORT_FIELDS:
        raise ValueError("power report schema mismatch")
    if report["schema_version"] != "tablets-power.v1":
        raise ValueError("power report schema version mismatch")
    if report["simulation_method"] != _SIMULATION_METHOD:
        raise ValueError("power report simulation method differs from the frozen contract")
    if report["alpha"] != ALPHA or report["target_power"] != TARGET_POWER:
        raise ValueError("power report thresholds differ from the frozen contract")
    if (
        type(report["simulations"]) is not int
        or isinstance(report["simulations"], bool)
        or report["simulations"] <= 0
        or type(report["seed"]) is not int
        or isinstance(report["seed"], bool)
    ):
        raise ValueError("power report simulation controls are invalid")
    if report["evidence_eligibility"] != "PRE_RUN_ONLY":
        raise ValueError("power report promotion forbidden: PRE_RUN_ONLY required")
    if report["empirical_status"] != "NOT_EMPIRICAL":
        raise ValueError("power report promotion forbidden: NOT_EMPIRICAL required")
    claims = report["claims"]
    if type(claims) is not list or [row.get("claim") for row in claims] != list(_CLAIM_NAMES):
        raise ValueError("power report must contain exactly the five frozen claims")
    if len({row.get("method") for row in claims}) != 5 or len(
        {row.get("effect_unit") for row in claims}
    ) != 5:
        raise ValueError("power claims require five metric-specific methods and effect units")

    for row, spec in zip(claims, _CLAIMS):
        if type(row) is not dict or set(row) != _ROW_FIELDS:
            raise ValueError("power claim row schema mismatch")
        if row["evidence_eligibility"] != "PRE_RUN_ONLY":
            raise ValueError("claim promotion forbidden: PRE_RUN_ONLY required")
        if row["empirical_status"] != "NOT_EMPIRICAL":
            raise ValueError("claim promotion forbidden: NOT_EMPIRICAL required")
        if row["p1_n"] != spec["p1_n"] or row["official_n"] != spec["official_n"]:
            raise ValueError("claim sample sizes differ from the frozen contract")
        conditional_triad = spec["claim"] == "triad_coherence"
        expected_mde_method = (
            "not estimable before observed win margins"
            if conditional_triad
            else "frozen metric-specific effect grid"
        )
        if (
            row["target_effect"] != spec["target_effect"]
            or row["method"] != spec["method"]
            or row["effect_unit"] != spec["effect_unit"]
            or row["assumptions"] != spec["assumptions"]
            or row["mde_grid"] != list(spec["mde_grid"])
            or row["mde_method"] != expected_mde_method
            or row["alpha"] != ALPHA
            or row["target_power"] != TARGET_POWER
        ):
            raise ValueError("claim metric-specific assumptions differ from the frozen contract")
        if conditional_triad:
            not_estimable = "NOT_ESTIMABLE_UNTIL_WIN_MARGINS"
            if any(
                row[field] is not None
                for field in (
                    "p1_estimated_power",
                    "official_estimated_power",
                    "estimated_power",
                    "p1_mde",
                    "official_mde",
                )
            ):
                raise ValueError("conditional triad power must remain not estimable")
            if (
                row["p1_mde_status"] != not_estimable
                or row["official_mde_status"] != not_estimable
                or row["claim_status"] != not_estimable
                or row["profile_flatness_eligible"] is not False
                or row["flatness_status"] != "INELIGIBLE_NOT_ESTIMABLE"
            ):
                raise ValueError("conditional triad claim has an invalid not-estimable status")
            continue
        for field in (
            "p1_estimated_power",
            "official_estimated_power",
            "estimated_power",
        ):
            value = row[field]
            if (
                type(value) not in (int, float)
                or isinstance(value, bool)
                or not math.isfinite(float(value))
                or not 0.0 <= float(value) <= 1.0
            ):
                raise ValueError("claim power estimate is invalid")
        if row["estimated_power"] != row["p1_estimated_power"]:
            raise ValueError("estimated_power must be the P1 estimate")
        for prefix in ("p1", "official"):
            status = row[prefix + "_mde_status"]
            value = row[prefix + "_mde"]
            if status == "GRID_ESTIMATED":
                if (
                    type(value) not in (int, float)
                    or isinstance(value, bool)
                    or not math.isfinite(float(value))
                    or value not in row["mde_grid"]
                ):
                    raise ValueError("claim grid MDE is invalid")
            elif status == "NOT_POWERABLE_AT_FROZEN_GRID":
                if value is not None:
                    raise ValueError("not-powerable claim must have a null MDE")
            else:
                raise ValueError("claim MDE status is invalid")
        expected_flatness = flatness_eligibility(row["estimated_power"])
        expected_powered = expected_flatness == "ELIGIBLE"
        expected_status = (
            "POWER_ADEQUATE_PRE_RUN"
            if expected_powered
            else "UNDERPOWERED_DESCRIPTIVE"
        )
        if row["flatness_status"] != expected_flatness:
            raise ValueError("flatness eligibility contradicts estimated power")
        if row["profile_flatness_eligible"] is not expected_powered:
            raise ValueError("profile-flatness promotion contradicts estimated power")
        if row["claim_status"] != expected_status:
            raise ValueError("claim status is an invalid power promotion")
    if report != _build_power_report(report["simulations"], report["seed"]):
        raise ValueError("power report deterministic recomputation mismatch")
    return True


def _markdown(report):
    lines = [
        "# TABLETS pre-run power report",
        "",
        "**Evidence eligibility:** `%s`" % report["evidence_eligibility"],
        "",
        "**Empirical status:** `%s`" % report["empirical_status"],
        "",
        "Alpha = %.2f; target power = %.2f; simulations = %d; seed = %d."
        % (
            report["alpha"],
            report["target_power"],
            report["simulations"],
            report["seed"],
        ),
        "",
        "| Claim | Method | P1 n | Official n | P1 power | P1 MDE | Official MDE | Status | Flatness |",
        "|---|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in report["claims"]:
        p1_power = (
            "N/A"
            if row["estimated_power"] is None
            else "%.3f" % row["estimated_power"]
        )
        p1_mde = "N/A" if row["p1_mde"] is None else "%.3f" % row["p1_mde"]
        official_mde = (
            "N/A" if row["official_mde"] is None else "%.3f" % row["official_mde"]
        )
        lines.append(
            "| %s | %s | %d | %d | %s | %s | %s | %s | %s |"
            % (
                row["claim"],
                row["method"],
                row["p1_n"],
                row["official_n"],
                p1_power,
                p1_mde,
                official_mde,
                row["claim_status"],
                row["flatness_status"],
            )
        )
    lines.extend(
        [
            "",
            "This artifact is PRE_RUN_ONLY and NOT_EMPIRICAL. It cannot establish "
            "flatness, confirm a claim, or promote diagnostic evidence.",
            "",
        ]
    )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulations", type=int, default=DEFAULT_SIMULATIONS)
    parser.add_argument("--seed", type=int, default=FIXED_SEED)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    report = generate_power_report(simulations=args.simulations, seed=args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "power-report.json").write_text(
        json.dumps(report, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    (args.output_dir / "power-report.md").write_text(
        _markdown(report),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ALPHA",
    "DEFAULT_SIMULATIONS",
    "FIXED_SEED",
    "TARGET_POWER",
    "flatness_eligibility",
    "generate_power_report",
    "validate_power_report",
]
