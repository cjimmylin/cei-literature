"""Bias-reduced logistic demand curves and core-stratified intervals for SKIM.

This module is deliberately numerical only.  It does not select a headline,
aggregate models, or apply the discrimination gate.  A coefficient is exposed
only after a finite, full-rank, converged Firth fit that did not touch the
optimizer bound.  Likewise, a bootstrap interval is exposed only when every
registered whole-core replicate produces an in-window point estimate.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
import hashlib
import math
from typing import Dict, List, Optional, Tuple

import numpy as np
from scipy.optimize import minimize
from scipy.special import expit

from skim_constants import (
    BOOTSTRAP_REPLICATES,
    MAGNITUDE_WINDOWS,
    THETA_ELIGIBLE_FAMILIES,
)
from skim_hashing import _finite_real
from skim_statistics import (
    bootstrap_ci_status,
    theta_design_100,
    theta_estimate_status,
)


_DEFAULT_COEFFICIENT_BOUND = 30.0
_DEFAULT_MAX_ITERATIONS = 500
_DEFAULT_TOLERANCE = 1e-9
_DEFAULT_SLOPE_EPSILON = 1e-8
_DEFAULT_SCORE_TOLERANCE = 1e-6


@dataclass(frozen=True)
class FirthFit:
    """One fail-closed, intercept-plus-slope bias-reduced logistic fit."""

    status: str
    intercept: Optional[float]
    slope: Optional[float]
    converged: bool
    iterations: int
    n_observations: int
    modified_score_max_abs: Optional[float]


@dataclass(frozen=True)
class DemandCurveResult:
    """One family curve with an uncensored point or an observed-window bound."""

    family: str
    status: str
    fit: FirthFit
    theta_log10: Optional[float]
    theta_design_100: Optional[float]
    censor_bound_log10: Optional[float]
    censor_bound_design_100: Optional[float]


@dataclass(frozen=True)
class CurveObservation:
    """One binary response belonging to an indivisible scenario-core bundle."""

    family: str
    core_id: str
    log10_magnitude: float
    diversion: bool


@dataclass(frozen=True)
class BootstrapFamilyResult:
    """Registered replicate accounting and interval for one family."""

    family: str
    status: str
    registered_replicates: int
    estimable_replicates: int
    ci95_log10: Optional[Tuple[float, float]]
    ci95_design_100: Optional[Tuple[float, float]]
    replicate_statuses: Tuple[str, ...]


@dataclass(frozen=True)
class ScenarioCoreBootstrapResult:
    """Deterministic family-stratified bootstrap result."""

    mode: str
    seed: int
    status: str
    registered_replicates: int
    family_results: Tuple[BootstrapFamilyResult, ...]


def _failed_fit(
    status: str,
    n_observations: int,
    iterations: int = 0,
    modified_score_max_abs: Optional[float] = None,
) -> FirthFit:
    return FirthFit(
        status=status,
        intercept=None,
        slope=None,
        converged=False,
        iterations=iterations,
        n_observations=n_observations,
        modified_score_max_abs=modified_score_max_abs,
    )


def _materialize(values: object) -> Optional[Tuple[object, ...]]:
    if isinstance(values, (str, bytes, bytearray)) or not isinstance(
        values, Iterable
    ):
        return None
    try:
        return tuple(values)
    except (TypeError, ValueError):
        return None


def _valid_positive_real(value: object) -> bool:
    return _finite_real(value) and float(value) > 0.0


def _penalized_value_and_gradient(
    coefficients: np.ndarray,
    design: np.ndarray,
    outcomes: np.ndarray,
) -> Tuple[float, np.ndarray]:
    """Return negative Firth log likelihood and its analytic gradient."""

    linear_predictor = design @ coefficients
    probabilities = expit(linear_predictor)
    weights = probabilities * (1.0 - probabilities)
    information = design.T @ (weights[:, np.newaxis] * design)
    sign, log_determinant = np.linalg.slogdet(information)
    if sign <= 0.0 or not math.isfinite(float(log_determinant)):
        return math.inf, np.full(2, math.nan, dtype=float)
    try:
        information_inverse = np.linalg.inv(information)
    except np.linalg.LinAlgError:
        return math.inf, np.full(2, math.nan, dtype=float)

    # h_i is the diagonal of W^(1/2) X I^-1 X' W^(1/2).
    leverage = weights * np.einsum(
        "ij,jk,ik->i", design, information_inverse, design
    )
    adjusted_residual = (
        outcomes - probabilities + leverage * (0.5 - probabilities)
    )
    modified_score = design.T @ adjusted_residual
    log_likelihood = np.sum(
        outcomes * linear_predictor - np.logaddexp(0.0, linear_predictor)
    )
    penalized = float(log_likelihood + 0.5 * log_determinant)
    gradient = -np.asarray(modified_score, dtype=float)
    if not math.isfinite(penalized) or not np.all(np.isfinite(gradient)):
        return math.inf, np.full(2, math.nan, dtype=float)
    return -penalized, gradient


def fit_firth_logistic(
    log10_magnitudes: Sequence[float],
    outcomes: Sequence[int],
    *,
    coefficient_bound: float = _DEFAULT_COEFFICIENT_BOUND,
    max_iterations: int = _DEFAULT_MAX_ITERATIONS,
    tolerance: float = _DEFAULT_TOLERANCE,
    slope_epsilon: float = _DEFAULT_SLOPE_EPSILON,
    score_tolerance: float = _DEFAULT_SCORE_TOLERANCE,
) -> FirthFit:
    """Fit an intercept and direction-agnostic magnitude slope.

    The Jeffreys-prior/Firth penalty is ``0.5 * log(det(X'WX))``.  Constant
    outcomes are handled before optimization, and every numerical failure
    returns a typed status with null coefficients.
    """

    x_values = _materialize(log10_magnitudes)
    y_values = _materialize(outcomes)
    n_observations = 0 if x_values is None else len(x_values)
    if (
        x_values is None
        or y_values is None
        or len(x_values) != len(y_values)
        or len(x_values) < 2
    ):
        return _failed_fit("INVALID_INPUT", n_observations)
    if (
        type(max_iterations) is not int
        or max_iterations <= 0
        or not _valid_positive_real(coefficient_bound)
        or not _valid_positive_real(tolerance)
        or not _valid_positive_real(slope_epsilon)
        or not _valid_positive_real(score_tolerance)
    ):
        return _failed_fit("INVALID_CONFIGURATION", n_observations)
    if not all(_finite_real(value) for value in x_values):
        return _failed_fit("NONFINITE_INPUT", n_observations)
    if not all(
        type(value) is bool or (type(value) is int and value in (0, 1))
        for value in y_values
    ):
        return _failed_fit("INVALID_INPUT", n_observations)

    numeric_outcomes = np.asarray(y_values, dtype=float)
    if np.all(numeric_outcomes == 0.0):
        return _failed_fit("CONSTANT_ZERO", n_observations)
    if np.all(numeric_outcomes == 1.0):
        return _failed_fit("CONSTANT_ONE", n_observations)

    numeric_x = np.asarray(x_values, dtype=float)
    x_center = math.fsum(float(value) for value in x_values) / n_observations
    centered_x = numeric_x - x_center
    x_scale = float(np.max(np.abs(centered_x)))
    if not math.isfinite(x_center) or not math.isfinite(x_scale) or x_scale <= 0.0:
        return _failed_fit("RANK_DEFICIENT", n_observations)
    transformed_x = centered_x / x_scale
    design = np.column_stack(
        (np.ones(n_observations, dtype=float), transformed_x)
    )
    if np.linalg.matrix_rank(design) != 2:
        return _failed_fit("RANK_DEFICIENT", n_observations)

    bound = float(coefficient_bound)

    def objective(coefficients: np.ndarray) -> float:
        return _penalized_value_and_gradient(
            coefficients, design, numeric_outcomes
        )[0]

    def gradient(coefficients: np.ndarray) -> np.ndarray:
        return _penalized_value_and_gradient(
            coefficients, design, numeric_outcomes
        )[1]

    try:
        optimized = minimize(
            objective,
            np.zeros(2, dtype=float),
            jac=gradient,
            method="L-BFGS-B",
            bounds=((-bound, bound), (-bound, bound)),
            options={
                "maxiter": max_iterations,
                "ftol": min(
                    float(tolerance), float(score_tolerance) ** 2
                ),
                "gtol": min(float(tolerance), float(score_tolerance)),
                "maxls": 50,
            },
        )
    except (FloatingPointError, OverflowError, ValueError, np.linalg.LinAlgError):
        return _failed_fit("NUMERICAL_FAILURE", n_observations)

    iterations = int(getattr(optimized, "nit", 0))
    coefficients = np.asarray(getattr(optimized, "x", (math.nan, math.nan)))
    if coefficients.shape != (2,) or not np.all(np.isfinite(coefficients)):
        return _failed_fit("NONFINITE_RESULT", n_observations, iterations)
    objective_value, negative_modified_score = _penalized_value_and_gradient(
        coefficients, design, numeric_outcomes
    )
    if (
        not math.isfinite(objective_value)
        or negative_modified_score.shape != (2,)
        or not np.all(np.isfinite(negative_modified_score))
    ):
        return _failed_fit("NUMERICAL_FAILURE", n_observations, iterations)
    modified_score_max_abs = float(np.max(np.abs(negative_modified_score)))
    boundary_tolerance = max(1e-7, bound * 1e-7)
    if np.any(np.abs(coefficients) >= bound - boundary_tolerance):
        return _failed_fit(
            "OPTIMIZER_BOUND",
            n_observations,
            iterations,
            modified_score_max_abs,
        )
    if (
        not bool(getattr(optimized, "success", False))
        or modified_score_max_abs > float(score_tolerance)
    ):
        return _failed_fit(
            "NONCONVERGED",
            n_observations,
            iterations,
            modified_score_max_abs,
        )

    slope = float(coefficients[1]) / x_scale
    intercept = float(coefficients[0]) - slope * x_center
    if not math.isfinite(intercept) or not math.isfinite(slope):
        return _failed_fit(
            "NONFINITE_RESULT",
            n_observations,
            iterations,
            modified_score_max_abs,
        )
    if abs(slope) <= float(slope_epsilon):
        return _failed_fit(
            "NEGLIGIBLE_SLOPE",
            n_observations,
            iterations,
            modified_score_max_abs,
        )
    return FirthFit(
        status="ESTIMATED",
        intercept=intercept,
        slope=slope,
        converged=True,
        iterations=iterations,
        n_observations=n_observations,
        modified_score_max_abs=modified_score_max_abs,
    )


def _not_estimable_curve(family: str, fit: FirthFit) -> DemandCurveResult:
    return DemandCurveResult(
        family=family,
        status="NOT_ESTIMABLE",
        fit=fit,
        theta_log10=None,
        theta_design_100=None,
        censor_bound_log10=None,
        censor_bound_design_100=None,
    )


def estimate_family_curve(
    family: str,
    log10_magnitudes: Sequence[float],
    outcomes: Sequence[int],
    *,
    coefficient_bound: float = _DEFAULT_COEFFICIENT_BOUND,
    max_iterations: int = _DEFAULT_MAX_ITERATIONS,
    tolerance: float = _DEFAULT_TOLERANCE,
    slope_epsilon: float = _DEFAULT_SLOPE_EPSILON,
    score_tolerance: float = _DEFAULT_SCORE_TOLERANCE,
) -> DemandCurveResult:
    """Estimate a family crossing without extrapolating or clamping it."""

    if family not in THETA_ELIGIBLE_FAMILIES:
        raise ValueError("family must be one of the four theta-eligible families")
    fit = fit_firth_logistic(
        log10_magnitudes,
        outcomes,
        coefficient_bound=coefficient_bound,
        max_iterations=max_iterations,
        tolerance=tolerance,
        slope_epsilon=slope_epsilon,
        score_tolerance=score_tolerance,
    )
    if fit.status != "ESTIMATED":
        return _not_estimable_curve(family, fit)
    assert fit.intercept is not None and fit.slope is not None
    crossing = -fit.intercept / fit.slope
    if not math.isfinite(crossing):
        return _not_estimable_curve(
            family,
            _failed_fit("NONFINITE_RESULT", fit.n_observations, fit.iterations),
        )
    status = theta_estimate_status(family, crossing)
    if status == "POINT_ESTIMATE":
        return DemandCurveResult(
            family=family,
            status=status,
            fit=fit,
            theta_log10=float(crossing),
            theta_design_100=theta_design_100(float(crossing)),
            censor_bound_log10=None,
            censor_bound_design_100=None,
        )
    if status in ("LEFT_CENSORED", "RIGHT_CENSORED"):
        window = MAGNITUDE_WINDOWS[family]
        bound_log10 = math.log10(
            window[0] if status == "LEFT_CENSORED" else window[-1]
        )
        return DemandCurveResult(
            family=family,
            status=status,
            fit=fit,
            theta_log10=None,
            theta_design_100=None,
            censor_bound_log10=bound_log10,
            censor_bound_design_100=theta_design_100(bound_log10),
        )
    return _not_estimable_curve(family, fit)


def _validated_observations(
    observations: object,
) -> Tuple[CurveObservation, ...]:
    rows = _materialize(observations)
    if rows is None or not rows:
        raise ValueError("observations must be a nonempty iterable")
    for observation in rows:
        if (
            type(observation) is not CurveObservation
            or observation.family not in THETA_ELIGIBLE_FAMILIES
            or type(observation.core_id) is not str
            or not observation.core_id
            or observation.core_id != observation.core_id.strip()
            or not _finite_real(observation.log10_magnitude)
            or type(observation.diversion) is not bool
        ):
            raise ValueError("every observation must satisfy the frozen typed schema")
        lower = math.log10(MAGNITUDE_WINDOWS[observation.family][0])
        upper = math.log10(MAGNITUDE_WINDOWS[observation.family][-1])
        if not lower <= float(observation.log10_magnitude) <= upper:
            raise ValueError("every observation magnitude must be inside its family window")
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                THETA_ELIGIBLE_FAMILIES.index(row.family),
                row.core_id,
                float(row.log10_magnitude),
                row.diversion,
            ),
        )
    )


def _family_rng(seed: int, family: str) -> np.random.Generator:
    digest = hashlib.sha256(("%d\0%s" % (seed, family)).encode("utf-8")).digest()
    return np.random.default_rng(int.from_bytes(digest[:16], "big"))


def _replicate_status(curve: DemandCurveResult) -> str:
    return curve.fit.status if curve.status == "NOT_ESTIMABLE" else curve.status


def scenario_core_bootstrap(
    observations: Sequence[CurveObservation],
    *,
    mode: str,
    seed: int,
) -> ScenarioCoreBootstrapResult:
    """Bootstrap complete core bundles independently within each family.

    The registered count is fixed by ``mode`` (1,000 empirical or 200
    synthetic).  No partial-replicate interval is returned.
    """

    if mode not in BOOTSTRAP_REPLICATES:
        raise ValueError("mode must be empirical or synthetic")
    if type(seed) is not int or seed < 0 or seed >= 2 ** 64:
        raise ValueError("seed must be a nonnegative unsigned-64-bit integer")
    rows = _validated_observations(observations)
    registered_replicates = BOOTSTRAP_REPLICATES[mode]

    bundles_by_family: Dict[str, Dict[str, List[CurveObservation]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for row in rows:
        bundles_by_family[row.family][row.core_id].append(row)

    family_results = []
    for family in THETA_ELIGIBLE_FAMILIES:
        if family not in bundles_by_family:
            continue
        core_bundles = bundles_by_family[family]
        core_ids = tuple(sorted(core_bundles))
        rng = _family_rng(seed, family)
        replicate_statuses = []
        point_estimates = []
        for _ in range(registered_replicates):
            draw_indices = rng.integers(0, len(core_ids), size=len(core_ids))
            sampled_rows = [
                row
                for draw_index in draw_indices
                for row in core_bundles[core_ids[int(draw_index)]]
            ]
            curve = estimate_family_curve(
                family,
                [row.log10_magnitude for row in sampled_rows],
                [row.diversion for row in sampled_rows],
            )
            replicate_statuses.append(_replicate_status(curve))
            if curve.status == "POINT_ESTIMATE":
                assert curve.theta_log10 is not None
                point_estimates.append(curve.theta_log10)

        estimable_replicates = len(point_estimates)
        status = bootstrap_ci_status(
            mode, registered_replicates, estimable_replicates
        )
        ci95_log10 = None
        ci95_design = None
        if status == "ESTIMABLE":
            lower, upper = np.quantile(
                np.asarray(point_estimates, dtype=float),
                (0.025, 0.975),
                method="linear",
            )
            if (
                math.isfinite(float(lower))
                and math.isfinite(float(upper))
                and float(upper) > float(lower)
            ):
                ci95_log10 = (float(lower), float(upper))
                ci95_design = (
                    theta_design_100(float(lower)),
                    theta_design_100(float(upper)),
                )
            else:
                status = "NOT_ESTIMABLE"
        family_results.append(
            BootstrapFamilyResult(
                family=family,
                status=status,
                registered_replicates=registered_replicates,
                estimable_replicates=estimable_replicates,
                ci95_log10=ci95_log10,
                ci95_design_100=ci95_design,
                replicate_statuses=tuple(replicate_statuses),
            )
        )

    overall_status = (
        "ESTIMABLE"
        if family_results
        and all(result.status == "ESTIMABLE" for result in family_results)
        else "NOT_ESTIMABLE"
    )
    return ScenarioCoreBootstrapResult(
        mode=mode,
        seed=seed,
        status=overall_status,
        registered_replicates=registered_replicates,
        family_results=tuple(family_results),
    )


__all__ = (
    "BootstrapFamilyResult",
    "CurveObservation",
    "DemandCurveResult",
    "FirthFit",
    "ScenarioCoreBootstrapResult",
    "estimate_family_curve",
    "fit_firth_logistic",
    "scenario_core_bootstrap",
)
