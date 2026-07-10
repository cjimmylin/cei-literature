"""Prospective X4 sensitivity accounting for the frozen SKIM P1 design."""

from dataclasses import dataclass
import math
from numbers import Real
from statistics import NormalDist
from typing import Tuple


TWO_SIDED_ALPHA = 0.05
TARGET_POWER = 0.80
OFFICIAL_SEEDS = 3
DIAGNOSTIC_SEEDS = 1
PAID_DATA_MAY_REVISE_THRESHOLDS = False
UNDERPOWERED = "UNDERPOWERED"
INDIVIDUAL_FALLBACK_MICROCELL_STATUS = "UNDERPOWERED_DESCRIPTIVE"
DIAGNOSTIC_INFERENCE_STATUS = "UNDERPOWERED_DESCRIPTIVE"


def _positive_int(value: object, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("%s must be an integer" % name)
    if value <= 0:
        raise ValueError("%s must be positive" % name)
    return value


def _open_probability(value: object, name: str) -> float:
    if (
        not isinstance(value, Real)
        or isinstance(value, bool)
        or not math.isfinite(value)
        or not 0.0 < value < 1.0
    ):
        raise ValueError("%s must be a finite value strictly between 0 and 1" % name)
    return float(value)


def normal_two_proportion_mdes(
    responses_per_arm: int,
    *,
    alpha: float = TWO_SIDED_ALPHA,
    power: float = TARGET_POWER,
    p: float = 0.5,
) -> float:
    """Normal-approximation two-proportion MDES for equal independent arms.

    The value is intentionally not clipped at one.  A value above one makes an
    infeasible design comparison visible instead of laundering it as powered.
    """

    n = _positive_int(responses_per_arm, "responses_per_arm")
    alpha_value = _open_probability(alpha, "alpha")
    power_value = _open_probability(power, "power")
    p_value = _open_probability(p, "p")
    z_alpha = NormalDist().inv_cdf(1.0 - alpha_value / 2.0)
    z_power = NormalDist().inv_cdf(power_value)
    standard_error = math.sqrt(2.0 * p_value * (1.0 - p_value) / n)
    return (z_alpha + z_power) * standard_error


def wilson_half_width(
    responses: int, *, p: float = 0.5, alpha: float = TWO_SIDED_ALPHA
) -> float:
    """Wilson score half-width for a single binomial rate."""

    n = _positive_int(responses, "responses")
    p_value = _open_probability(p, "p")
    alpha_value = _open_probability(alpha, "alpha")
    z_value = NormalDist().inv_cdf(1.0 - alpha_value / 2.0)
    denominator = 1.0 + z_value * z_value / n
    numerator = z_value * math.sqrt(
        p_value * (1.0 - p_value) / n + z_value * z_value / (4.0 * n * n)
    )
    return numerator / denominator


@dataclass(frozen=True)
class PowerDesign:
    """One preregistered P1 reporting cell and its sensitivity accounting."""

    name: str
    cores_per_seed: int
    independent_core_clusters: int
    official_responses_per_model: int
    diagnostic_responses_per_model: int
    official_mdes: float
    diagnostic_mdes: float
    official_wilson_half_width: float
    diagnostic_wilson_half_width: float
    official_status: str
    diagnostic_status: str


def _design(name: str, cores_per_seed: int, official_status: str) -> PowerDesign:
    official_responses = cores_per_seed * OFFICIAL_SEEDS
    diagnostic_responses = cores_per_seed * DIAGNOSTIC_SEEDS
    return PowerDesign(
        name=name,
        cores_per_seed=cores_per_seed,
        independent_core_clusters=cores_per_seed,
        official_responses_per_model=official_responses,
        diagnostic_responses_per_model=diagnostic_responses,
        official_mdes=normal_two_proportion_mdes(official_responses),
        diagnostic_mdes=normal_two_proportion_mdes(diagnostic_responses),
        official_wilson_half_width=wilson_half_width(official_responses),
        diagnostic_wilson_half_width=wilson_half_width(diagnostic_responses),
        official_status=official_status,
        diagnostic_status=DIAGNOSTIC_INFERENCE_STATUS,
    )


POWER_DESIGNS: Tuple[PowerDesign, ...] = (
    _design(
        "family_x_tier_x_traceability",
        6,
        "PROSPECTIVE_SENSITIVITY_ONLY",
    ),
    _design(
        "family_x_tier_x_traceability_x_cover_story",
        3,
        INDIVIDUAL_FALLBACK_MICROCELL_STATUS,
    ),
    _design("macro_easy", 12, "REGISTERED_MACRO_COMPARISON"),
    _design("macro_hard", 12, "REGISTERED_MACRO_COMPARISON"),
)


def flatness_status(*, flat_observed: bool, adequately_powered: bool) -> str:
    """Never convert an inadequately powered flat observation into a null."""

    if not isinstance(flat_observed, bool) or not isinstance(adequately_powered, bool):
        raise TypeError("flat_observed and adequately_powered must be booleans")
    if not adequately_powered:
        return UNDERPOWERED
    return "FLAT" if flat_observed else "NOT_FLAT"


def sensitivity_table() -> Tuple[dict, ...]:
    """Return JSON-ready copies of the immutable preregistered rows."""

    return tuple(
        {
            field: getattr(row, field)
            for field in PowerDesign.__dataclass_fields__
        }
        for row in POWER_DESIGNS
    )


__all__ = [
    "DIAGNOSTIC_INFERENCE_STATUS",
    "DIAGNOSTIC_SEEDS",
    "INDIVIDUAL_FALLBACK_MICROCELL_STATUS",
    "OFFICIAL_SEEDS",
    "PAID_DATA_MAY_REVISE_THRESHOLDS",
    "POWER_DESIGNS",
    "PowerDesign",
    "TARGET_POWER",
    "TWO_SIDED_ALPHA",
    "UNDERPOWERED",
    "flatness_status",
    "normal_two_proportion_mdes",
    "sensitivity_table",
    "wilson_half_width",
]
