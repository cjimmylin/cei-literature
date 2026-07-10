"""Mechanical ZEROSUM discrimination gate and one-retry state."""

from __future__ import annotations

import math
from numbers import Real
from typing import Any, Dict, Mapping


THRESHOLDS = {
    "headline_spread_min_points": 20.0,
    "capability_correlation_abs_max_exclusive": 0.40,
    "hard_easy_drop_min_points": 15.0,
}
ALLOWED_ADJUSTMENTS = ("opacity_tiers", "rho_sampling")
KNOWN_MODES = ("synthetic", "live", "empirical", "incomplete")
KNOWN_CLASSIFIER_STATES = (
    "PASS", "PASS_HUMAN", "NOT_RUN_HUMAN", "FAIL",
    "INSUFFICIENT_HUMAN_LABELS", "INCOMPLETE_ADJUDICATION",
    "REPAIR_AUTHORIZED", "SECOND_FAIL_PARKED",
)


def _metric(
    calculations: Mapping[str, Any], name: str, *, minimum: float, maximum: float
) -> float:
    value = calculations.get(name)
    if (
        not isinstance(value, Real)
        or isinstance(value, bool)
        or not math.isfinite(float(value))
    ):
        raise ValueError("discrimination metric %s must be finite" % name)
    normalized = float(value)
    if not minimum <= normalized <= maximum:
        raise ValueError(
            "discrimination metric %s must be in [%s, %s]"
            % (name, minimum, maximum)
        )
    return normalized


def _queue_memo(
    result: Mapping[str, Any], *, reason: str, adjustment: str = None
) -> Dict[str, Any]:
    return {
        "destination": "TENCOMMANDMENTS-REVIEWS/FABLE-QUEUE",
        "gate": "ZEROSUM discrimination",
        "reason": reason,
        "registered_thresholds": dict(THRESHOLDS),
        "observed": dict(result["observed"]),
        "options_considered": list(ALLOWED_ADJUSTMENTS),
        "adjustment_used": adjustment,
        "conservative_default": "park design and continue wave",
    }


def _normalized_identifiers(value: Any) -> tuple:
    if not isinstance(value, list):
        return ()
    normalized = []
    for item in value:
        if not isinstance(item, str):
            return ()
        canonical = " ".join(item.split())
        if not canonical:
            return ()
        normalized.append(canonical)
    return tuple(normalized)


def evaluate_discrimination(
    calculations: Mapping[str, Any],
    *,
    evidence: Mapping[str, Any],
    retry_count: int,
    adjustment: str = None,
) -> Dict[str, Any]:
    """Apply frozen thresholds without converting synthetic evidence to a pass."""

    if type(retry_count) is not int or retry_count not in (0, 1):
        raise ValueError("retry_count must be 0 or 1")
    if adjustment is not None and adjustment not in ALLOWED_ADJUSTMENTS:
        raise ValueError("adjustment must be opacity_tiers or rho_sampling")
    zs_spread = _metric(
        calculations, "zs_spread_points", minimum=0.0, maximum=100.0
    )
    fr_spread = _metric(
        calculations, "fr_spread_points", minimum=0.0, maximum=100.0
    )
    capability = _metric(
        calculations, "capability_correlation_abs", minimum=0.0, maximum=1.0
    )
    hard_easy = _metric(
        calculations, "hard_easy_drop_points", minimum=-100.0, maximum=100.0
    )
    checks = {
        "headline_spread": max(zs_spread, fr_spread)
        >= THRESHOLDS["headline_spread_min_points"],
        "capability_correlation": capability
        < THRESHOLDS["capability_correlation_abs_max_exclusive"],
        "hard_easy_drop": hard_easy >= THRESHOLDS["hard_easy_drop_min_points"],
    }
    calculation_pass = all(checks.values())
    mode = evidence.get("mode")
    models = evidence.get("models")
    vendors = evidence.get("vendors")
    normalized_models = _normalized_identifiers(models)
    normalized_vendors = _normalized_identifiers(vendors)
    live_eligible = (
        mode in {"live", "empirical"}
        and evidence.get("classifier_gate") in {"PASS", "PASS_HUMAN"}
        and len(set(normalized_models)) >= 3
        and len(set(normalized_vendors)) >= 2
    )
    result = {
        "thresholds": dict(THRESHOLDS),
        "observed": {
            "zs_spread_points": zs_spread,
            "fr_spread_points": fr_spread,
            "capability_correlation_abs": capability,
            "hard_easy_drop_points": hard_easy,
        },
        "checks": checks,
        "calculation_pass": calculation_pass,
        "eligible_for_empirical_decision": False,
        "retry_count": retry_count,
        "allowed_adjustments": list(ALLOWED_ADJUSTMENTS),
        "queue_memo": None,
    }
    if mode not in KNOWN_MODES:
        result["verdict"] = "FABLE_QUEUE"
        result["queue_memo"] = _queue_memo(
            result, reason="unlisted evidence mode: %r" % (mode,)
        )
        return result
    classifier_state = evidence.get("classifier_gate")
    if mode in {"live", "empirical"} and classifier_state not in KNOWN_CLASSIFIER_STATES:
        result["verdict"] = "FABLE_QUEUE"
        result["queue_memo"] = _queue_memo(
            result, reason="unlisted classifier gate state: %r" % classifier_state
        )
        return result
    if not live_eligible:
        result["verdict"] = "EXERCISE_ONLY" if mode == "synthetic" else "INELIGIBLE_PRECONDITIONS"
        return result
    if calculation_pass:
        result["verdict"] = "PASS"
        result["eligible_for_empirical_decision"] = True
        return result
    if retry_count == 0:
        if adjustment is None:
            result["verdict"] = "ADJUSTMENT_SELECTION_REQUIRED"
            result["eligible_for_empirical_decision"] = False
        else:
            result["verdict"] = "RETRY_AUTHORIZED"
            result["adjustment"] = adjustment
        return result
    result["verdict"] = "PARK"
    result["queue_memo"] = _queue_memo(
        result, reason="second discrimination failure", adjustment=adjustment
    )
    return result


__all__ = [
    "ALLOWED_ADJUSTMENTS", "KNOWN_CLASSIFIER_STATES", "KNOWN_MODES",
    "THRESHOLDS", "evaluate_discrimination",
]
