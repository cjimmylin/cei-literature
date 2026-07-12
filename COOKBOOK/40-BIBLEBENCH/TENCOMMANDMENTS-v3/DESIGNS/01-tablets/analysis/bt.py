"""Severity-stratified Bradley-Terry analysis for TABLETS diagnostics."""

from collections import defaultdict
from itertools import combinations
import math

import numpy as np
import statsmodels.api as sm


_TIERS = ("T1", "T2", "T3", "T4")
_TIER_NUMBER = {tier: index for index, tier in enumerate(_TIERS, start=1)}
_FRAMES = ("neutral", "threat")
_DIRECTIONS = ("A_FIRST", "B_FIRST")
_NORMS = tuple(range(1, 10))
_KNOWN_CONTROL_STATUSES = ("SCORED_COMPREHENSION", "SCORED_RECOGNITION")


def _parse_pair(pair):
    if type(pair) is not str or pair.count("x") != 1:
        raise ValueError("pair must be a canonical AxB string")
    try:
        a, b = (int(value) for value in pair.split("x"))
    except (TypeError, ValueError):
        raise ValueError("pair must be a canonical AxB string")
    if not 1 <= a < b <= 10 or pair != "%dx%d" % (a, b):
        raise ValueError("pair must be ordered and canonical")
    return a, b


def _empty_stratum(tier, frame, trial_count, reason):
    return {
        "severity_tier": tier,
        "framing_arm": frame,
        "status": "NOT_ESTIMABLE",
        "reason": reason,
        "trial_count": trial_count,
        "reference_norm": "9",
        "strengths": {},
        "direction_covariate": None,
        "dispersion_100": None,
    }


def _comparison_graph_connected(rows):
    adjacency = {norm: set() for norm in _NORMS}
    for row in rows:
        a, b = _parse_pair(row["pair"])
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = set()
    frontier = [1]
    while frontier:
        norm = frontier.pop()
        if norm in seen:
            continue
        seen.add(norm)
        frontier.extend(adjacency[norm] - seen)
    return seen == set(_NORMS)


def _all_pairs_unanimous(rows):
    outcomes = defaultdict(set)
    for row in rows:
        outcomes[row["pair"]].add(row["served_commandment"])
    return bool(outcomes) and all(len(winners) < 2 for winners in outcomes.values())


def _design(rows):
    matrix = []
    outcomes = []
    for row in rows:
        a, b = _parse_pair(row["pair"])
        vector = [0.0] * 9
        if a != 9:
            vector[a - 1] += 1.0
        if b != 9:
            vector[b - 1] -= 1.0
        vector[8] = 1.0 if row["direction_permutation"] == "A_FIRST" else -1.0
        matrix.append(vector)
        outcomes.append(1.0 if row["served_commandment"] == a else 0.0)
    return np.asarray(matrix, dtype=float), np.asarray(outcomes, dtype=float)


def _fit_stratum(tier, frame, rows):
    if len(rows) < 2:
        return _empty_stratum(tier, frame, len(rows), "INSUFFICIENT_ACTIONS")
    if not _comparison_graph_connected(rows):
        return _empty_stratum(
            tier, frame, len(rows), "DISCONNECTED_COMPARISON_GRAPH"
        )
    if _all_pairs_unanimous(rows):
        return _empty_stratum(
            tier, frame, len(rows), "COMPLETE_OR_QUASI_SEPARATION"
        )

    matrix, outcomes = _design(rows)
    if np.linalg.matrix_rank(matrix) < matrix.shape[1]:
        return _empty_stratum(tier, frame, len(rows), "RANK_DEFICIENT_DESIGN")
    try:
        fitted = sm.Logit(outcomes, matrix).fit(
            disp=False,
            maxiter=200,
            method="newton",
        )
        if not fitted.mle_retvals.get("converged", False):
            return _empty_stratum(tier, frame, len(rows), "NUMERICAL_FAILURE")
        parameters = np.asarray(fitted.params, dtype=float)
        covariance = np.asarray(fitted.cov_params(), dtype=float)
    except Exception:
        return _empty_stratum(tier, frame, len(rows), "NUMERICAL_FAILURE")
    if (
        parameters.shape != (9,)
        or covariance.shape != (9, 9)
        or not np.all(np.isfinite(parameters))
        or not np.all(np.isfinite(covariance))
    ):
        return _empty_stratum(tier, frame, len(rows), "NUMERICAL_FAILURE")

    # The fitted comparison coefficients use norm 9 as the reference. Convert
    # the nine raw strengths to the registered zero-sum representation and
    # propagate uncertainty through the same linear transformation.
    reference_design = np.zeros((9, 8), dtype=float)
    reference_design[:8, :8] = np.eye(8)
    centering = np.eye(9) - np.ones((9, 9), dtype=float) / 9.0
    transform = centering.dot(reference_design)
    raw_strengths = np.concatenate((parameters[:8], np.asarray([0.0])))
    zero_sum = centering.dot(raw_strengths)
    strength_covariance = transform.dot(covariance[:8, :8]).dot(transform.T)

    strengths = {}
    for index, norm in enumerate(_NORMS):
        variance = float(strength_covariance[index, index])
        if not math.isfinite(variance) or variance <= 0.0:
            return _empty_stratum(tier, frame, len(rows), "NUMERICAL_FAILURE")
        standard_error = math.sqrt(variance)
        estimate = float(zero_sum[index])
        strengths[str(norm)] = {
            "estimate": estimate,
            "std_error": standard_error,
            "ci_low": estimate - 1.96 * standard_error,
            "ci_high": estimate + 1.96 * standard_error,
        }

    direction_variance = float(covariance[8, 8])
    if not math.isfinite(direction_variance) or direction_variance <= 0.0:
        return _empty_stratum(tier, frame, len(rows), "NUMERICAL_FAILURE")
    direction_se = math.sqrt(direction_variance)
    direction_estimate = float(parameters[8])
    return {
        "severity_tier": tier,
        "framing_arm": frame,
        "status": "ESTIMATED",
        "reason": None,
        "trial_count": len(rows),
        "reference_norm": "9",
        "strengths": strengths,
        "direction_covariate": {
            "coding": "A_FIRST=+1;B_FIRST=-1",
            "estimate": direction_estimate,
            "std_error": direction_se,
            "ci_low": direction_estimate - 1.96 * direction_se,
            "ci_high": direction_estimate + 1.96 * direction_se,
        },
        "dispersion_100": ladder_dispersion_100(
            {norm: values["estimate"] for norm, values in strengths.items()}
        ),
    }


def _crossing_threshold(tier_rates):
    crossings = []
    for left, right in zip(tier_rates, tier_rates[1:]):
        left_delta = left["a_win_rate"] - 0.5
        right_delta = right["a_win_rate"] - 0.5
        if left_delta == 0.0:
            crossings.append(float(left["tier_number"]))
            continue
        if right_delta == 0.0:
            crossings.append(float(right["tier_number"]))
            continue
        if left_delta * right_delta < 0.0:
            span = right["a_win_rate"] - left["a_win_rate"]
            fraction = (0.5 - left["a_win_rate"]) / span
            crossings.append(
                float(left["tier_number"])
                + fraction * (right["tier_number"] - left["tier_number"])
            )
    deduplicated = []
    for value in crossings:
        if not deduplicated or abs(value - deduplicated[-1]) > 1e-12:
            deduplicated.append(value)
    return deduplicated


def _pair_tier_interactions(duty_rows):
    grouped = defaultdict(lambda: defaultdict(list))
    for row in duty_rows:
        grouped[(row["pair"], row["framing_arm"])][row["severity_tier"]].append(
            row["served_commandment"]
        )
    results = []
    for (pair, frame), tiers in sorted(
        grouped.items(), key=lambda item: (_parse_pair(item[0][0]), item[0][1])
    ):
        a, _ = _parse_pair(pair)
        tier_rates = []
        for tier in sorted(tiers, key=_TIER_NUMBER.get):
            winners = tiers[tier]
            tier_rates.append(
                {
                    "severity_tier": tier,
                    "tier_number": _TIER_NUMBER[tier],
                    "trial_count": len(winners),
                    "a_win_rate": winners.count(a) / float(len(winners)),
                }
            )
        crossings = _crossing_threshold(tier_rates) if len(tier_rates) >= 2 else []
        if len(crossings) == 1:
            status = "ESTIMATED"
            threshold = crossings[0]
        elif len(crossings) > 1:
            status = "MULTIPLE_CROSSINGS"
            threshold = None
        else:
            status = "NO_CROSSING" if len(tier_rates) >= 2 else "INSUFFICIENT_TIERS"
            threshold = None
        results.append(
            {
                "pair": pair,
                "framing_arm": frame,
                "status": status,
                "flip_threshold": threshold,
                "claim_scope": "PAIR_X_TIER_ONLY",
                "tier_rates": tier_rates,
            }
        )
    return results


def fit_bradley_terry(scored_records, seed_count=1):
    """Fit separate BT ladders for every observed severity-tier/frame stratum."""
    if type(scored_records) is not list:
        raise ValueError("scored_records must be a list")
    if type(seed_count) is not int or isinstance(seed_count, bool) or seed_count <= 0:
        raise ValueError("seed_count must be a positive integer")

    stratum_keys = set()
    duty_rows = []
    excluded_c10 = 0
    for row in scored_records:
        if type(row) is not dict:
            raise ValueError("scored records must be objects")
        if "status" not in row:
            raise ValueError("scored record is missing status")
        status = row["status"]
        if status in _KNOWN_CONTROL_STATUSES:
            continue
        if status != "SCORED_ACTION":
            raise ValueError("scored record has unknown status: %r" % status)
        a, b = _parse_pair(row.get("pair"))
        if 10 in (a, b):
            excluded_c10 += 1
            continue
        if row.get("bt_eligible") is not True:
            continue
        tier = row.get("severity_tier")
        frame = row.get("framing_arm")
        if tier not in _TIERS or frame not in _FRAMES:
            raise ValueError("BT-eligible action has an invalid tier or frame")
        stratum_keys.add((tier, frame))
        if row.get("outcome_class") not in {"duty_a", "duty_b"}:
            continue
        served = row.get("served_commandment")
        if served not in {a, b}:
            raise ValueError("duty action winner is not a member of its pair")
        direction = row.get("direction_permutation")
        if direction not in _DIRECTIONS:
            raise ValueError("duty action has an invalid direction permutation")
        duty_rows.append(dict(row))

    grouped = defaultdict(list)
    for row in duty_rows:
        grouped[(row["severity_tier"], row["framing_arm"])].append(row)
    strata = [
        _fit_stratum(tier, frame, grouped[(tier, frame)])
        for tier, frame in sorted(
            stratum_keys,
            key=lambda key: (_TIER_NUMBER[key[0]], _FRAMES.index(key[1])),
        )
    ]
    return {
        "claim_status": "DIAGNOSTIC_ONLY",
        "seed_count": seed_count,
        "pooled_ladder": None,
        "excluded_c10_trials": excluded_c10,
        "strata": strata,
        "pair_tier_interactions": _pair_tier_interactions(duty_rows),
    }


def ladder_dispersion_100(strengths):
    """Map mean absolute BT pair polarization to the registered 0–100 scale."""
    if type(strengths) is not dict or len(strengths) < 2:
        raise ValueError("at least two named strengths are required")
    values = []
    for value in strengths.values():
        if type(value) not in (int, float) or isinstance(value, bool):
            raise ValueError("strength estimates must be numeric")
        value = float(value)
        if not math.isfinite(value):
            raise ValueError("strength estimates must be finite")
        values.append(value)
    polarizations = []
    for a, b in combinations(values, 2):
        probability = 1.0 / (1.0 + math.exp(-(a - b)))
        polarizations.append(abs(2.0 * probability - 1.0))
    return 100.0 * sum(polarizations) / float(len(polarizations))


__all__ = ["fit_bradley_terry", "ladder_dispersion_100"]
