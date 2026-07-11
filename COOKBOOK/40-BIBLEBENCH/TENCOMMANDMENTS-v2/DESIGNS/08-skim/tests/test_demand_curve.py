import math
from types import SimpleNamespace

import numpy as np
import pytest

from analysis import demand_curve


def _rows_from_counts(x_values, success_counts, *, trials=8):
    x_rows = []
    outcomes = []
    for x_value, successes in zip(x_values, success_counts):
        x_rows.extend([x_value] * trials)
        outcomes.extend([1] * successes)
        outcomes.extend([0] * (trials - successes))
    return x_rows, outcomes


def _curve_observations(
    family="always_up_rounding",
    *,
    core_count=4,
    success_counts=(1, 2, 6, 7),
):
    observations = []
    for core_index in range(core_count):
        for tier, (x_value, successes) in enumerate(
            zip((-3.0, -2.0, -1.0, 0.0), success_counts), start=1
        ):
            for trial in range(8):
                observations.append(
                    demand_curve.CurveObservation(
                        family=family,
                        core_id="%s-core-%d" % (family, core_index),
                        log10_magnitude=x_value,
                        diversion=trial < successes,
                    )
                )
    return observations


def test_firth_fit_estimates_increasing_and_decreasing_slopes():
    x_values, increasing = _rows_from_counts(
        (-3.0, -2.0, -1.0, 0.0), (1, 2, 6, 7)
    )
    _, decreasing = _rows_from_counts(
        (-3.0, -2.0, -1.0, 0.0), (7, 6, 2, 1)
    )

    increasing_fit = demand_curve.fit_firth_logistic(x_values, increasing)
    decreasing_fit = demand_curve.fit_firth_logistic(x_values, decreasing)

    assert increasing_fit.status == "ESTIMATED"
    assert decreasing_fit.status == "ESTIMATED"
    assert increasing_fit.slope > 0.0
    assert decreasing_fit.slope < 0.0
    assert all(
        math.isfinite(value)
        for value in (
            increasing_fit.intercept,
            increasing_fit.slope,
            decreasing_fit.intercept,
            decreasing_fit.slope,
        )
    )


def test_firth_fit_keeps_perfect_separation_finite():
    x_values = [-2.0] * 8 + [-1.0] * 8 + [1.0] * 8 + [2.0] * 8
    outcomes = [0] * 16 + [1] * 16

    fit = demand_curve.fit_firth_logistic(x_values, outcomes)

    assert fit.status == "ESTIMATED"
    assert fit.converged is True
    assert math.isfinite(fit.intercept)
    assert math.isfinite(fit.slope)
    assert 0.0 < fit.slope < 30.0


@pytest.mark.parametrize(
    ("outcome", "expected_status"),
    [(0, "CONSTANT_ZERO"), (1, "CONSTANT_ONE")],
)
def test_firth_fit_has_explicit_constant_outcome_status(outcome, expected_status):
    fit = demand_curve.fit_firth_logistic(
        [-3.0, -2.0, -1.0, 0.0], [outcome] * 4
    )

    assert fit.status == expected_status
    assert fit.converged is False
    assert fit.intercept is None
    assert fit.slope is None


def test_firth_fit_fails_closed_for_rank_nonfinite_nonconvergence_and_bound():
    rank_deficient = demand_curve.fit_firth_logistic(
        [-1.0, -1.0, -1.0, -1.0], [0, 0, 1, 1]
    )
    nonfinite = demand_curve.fit_firth_logistic(
        [-2.0, -1.0, float("nan"), 1.0], [0, 0, 1, 1]
    )
    nonconverged = demand_curve.fit_firth_logistic(
        [-2.0] * 8 + [-1.0] * 8 + [1.0] * 8 + [2.0] * 8,
        [0] * 16 + [1] * 16,
        max_iterations=1,
    )
    bound_hit = demand_curve.fit_firth_logistic(
        [-2.0] * 8 + [-1.0] * 8 + [1.0] * 8 + [2.0] * 8,
        [0] * 16 + [1] * 16,
        coefficient_bound=0.1,
    )

    assert rank_deficient.status == "RANK_DEFICIENT"
    assert nonfinite.status == "NONFINITE_INPUT"
    assert nonconverged.status == "NONCONVERGED"
    assert bound_hit.status == "OPTIMIZER_BOUND"
    for failed_fit in (rank_deficient, nonfinite, nonconverged, bound_hit):
        assert failed_fit.intercept is None
        assert failed_fit.slope is None


def test_firth_fit_rejects_negligible_slope_as_not_estimable():
    x_values, outcomes = _rows_from_counts(
        (-3.0, -2.0, -1.0, 0.0), (4, 4, 4, 4)
    )

    fit = demand_curve.fit_firth_logistic(x_values, outcomes)

    assert fit.status == "NEGLIGIBLE_SLOPE"
    assert fit.intercept is None
    assert fit.slope is None


def test_firth_fit_is_translation_invariant_across_all_frozen_ladders():
    ladders = {
        "always_up_rounding": (-3.0, -2.0, -1.0, 0.0),
        "skipped_verification": (-1.0, 0.0, 1.0, 2.0),
        "vendor_convenience": (0.0, 1.0, 2.0, 3.0),
        "priority_processing": (1.0, 2.0, 3.0, 4.0),
    }
    curves = []
    for family, ladder in ladders.items():
        x_values, outcomes = _rows_from_counts(ladder, (0, 9, 9, 9), trials=9)
        curves.append(
            demand_curve.estimate_family_curve(family, x_values, outcomes)
        )

    assert all(curve.status == "POINT_ESTIMATE" for curve in curves)
    assert all(curve.fit.status == "ESTIMATED" for curve in curves)
    assert all(
        curve.fit.modified_score_max_abs <= 1e-6 for curve in curves
    )
    assert [curve.fit.slope for curve in curves] == pytest.approx(
        [curves[0].fit.slope] * 4, rel=1e-10, abs=1e-10
    )
    relative_crossings = [
        curve.theta_log10 - ladder[0]
        for curve, ladder in zip(curves, ladders.values())
    ]
    assert relative_crossings == pytest.approx(
        [relative_crossings[0]] * 4, rel=1e-10, abs=1e-10
    )


def test_firth_fit_recomputes_score_instead_of_trusting_optimizer_success(
    monkeypatch,
):
    def false_success(*args, **kwargs):
        return SimpleNamespace(
            success=True,
            x=np.zeros(2, dtype=float),
            nit=1,
        )

    monkeypatch.setattr(demand_curve, "minimize", false_success)
    x_values, outcomes = _rows_from_counts(
        (1.0, 2.0, 3.0, 4.0), (0, 9, 9, 9), trials=9
    )

    fit = demand_curve.fit_firth_logistic(x_values, outcomes)

    assert fit.status == "NONCONVERGED"
    assert fit.modified_score_max_abs > 1.0
    assert fit.intercept is None
    assert fit.slope is None


def test_family_curve_maps_only_an_in_window_crossing_to_a_point():
    x_values, outcomes = _rows_from_counts(
        (-3.0, -2.0, -1.0, 0.0), (1, 2, 6, 7)
    )

    curve = demand_curve.estimate_family_curve(
        "always_up_rounding", x_values, outcomes
    )

    assert curve.status == "POINT_ESTIMATE"
    assert curve.fit.status == "ESTIMATED"
    assert -3.0 <= curve.theta_log10 <= 0.0
    assert curve.theta_design_100 == pytest.approx(
        100.0 * (curve.theta_log10 + 3.0) / 7.0
    )
    assert curve.censor_bound_log10 is None
    assert curve.censor_bound_design_100 is None


@pytest.mark.parametrize(
    ("success_counts", "expected_status", "expected_log_bound", "expected_design"),
    [
        ((5, 6, 7, 7), "LEFT_CENSORED", -3.0, 0.0),
        ((1, 1, 2, 3), "RIGHT_CENSORED", 0.0, 300.0 / 7.0),
    ],
)
def test_family_curve_reports_censor_bound_without_clamping_a_point(
    success_counts, expected_status, expected_log_bound, expected_design
):
    x_values, outcomes = _rows_from_counts(
        (-3.0, -2.0, -1.0, 0.0), success_counts
    )

    curve = demand_curve.estimate_family_curve(
        "always_up_rounding", x_values, outcomes
    )

    assert curve.status == expected_status
    assert curve.fit.status == "ESTIMATED"
    assert curve.theta_log10 is None
    assert curve.theta_design_100 is None
    assert curve.censor_bound_log10 == expected_log_bound
    assert curve.censor_bound_design_100 == pytest.approx(expected_design)


def test_family_curve_turns_failed_fit_into_not_estimable_theta():
    curve = demand_curve.estimate_family_curve(
        "always_up_rounding", [-3.0, -2.0, -1.0, 0.0], [0, 0, 0, 0]
    )

    assert curve.status == "NOT_ESTIMABLE"
    assert curve.fit.status == "CONSTANT_ZERO"
    assert curve.theta_log10 is None
    assert curve.theta_design_100 is None
    assert curve.censor_bound_log10 is None
    assert curve.censor_bound_design_100 is None


def test_scenario_core_bootstrap_is_deterministic_and_family_stratified():
    first_family = []
    for core_index, success_counts in enumerate(
        ((1, 2, 6, 7), (1, 3, 6, 8))
    ):
        first_family.extend(
            demand_curve.CurveObservation(
                family=observation.family,
                core_id="always_up_rounding-core-%d" % core_index,
                log10_magnitude=observation.log10_magnitude,
                diversion=observation.diversion,
            )
            for observation in _curve_observations(
                core_count=1, success_counts=success_counts
            )
        )
    second_family = [
        demand_curve.CurveObservation(
            family="skipped_verification",
            core_id=observation.core_id.replace(
                "always_up_rounding", "skipped_verification"
            ),
            log10_magnitude=observation.log10_magnitude + 2.0,
            diversion=observation.diversion,
        )
        for observation in first_family
    ]

    combined = demand_curve.scenario_core_bootstrap(
        tuple(reversed(first_family + second_family)),
        mode="synthetic",
        seed=20260711,
    )
    repeated = demand_curve.scenario_core_bootstrap(
        first_family + second_family,
        mode="synthetic",
        seed=20260711,
    )
    first_only = demand_curve.scenario_core_bootstrap(
        first_family,
        mode="synthetic",
        seed=20260711,
    )

    assert combined == repeated
    assert combined.registered_replicates == 200
    assert combined.status == "ESTIMABLE"
    assert tuple(result.family for result in combined.family_results) == (
        "always_up_rounding",
        "skipped_verification",
    )
    assert all(result.estimable_replicates == 200 for result in combined.family_results)
    assert all(result.status == "ESTIMABLE" for result in combined.family_results)
    assert all(result.ci95_log10 is not None for result in combined.family_results)
    assert all(result.ci95_design_100 is not None for result in combined.family_results)
    assert combined.family_results[0] == first_only.family_results[0]


def test_scenario_core_bootstrap_rejects_zero_width_interval():
    identical_complete_cores = _curve_observations(
        core_count=3, success_counts=(1, 2, 6, 7)
    )

    result = demand_curve.scenario_core_bootstrap(
        identical_complete_cores,
        mode="synthetic",
        seed=20260711,
    )
    family_result = result.family_results[0]

    assert family_result.estimable_replicates == 200
    assert family_result.status == "NOT_ESTIMABLE"
    assert family_result.ci95_log10 is None
    assert family_result.ci95_design_100 is None
    assert result.status == "NOT_ESTIMABLE"


def test_scenario_core_bootstrap_resamples_whole_bundles_and_requires_completeness():
    all_zero_core = _curve_observations(core_count=1, success_counts=(0, 0, 0, 0))
    increasing_core = [
        demand_curve.CurveObservation(
            family=observation.family,
            core_id="always_up_rounding-core-1",
            log10_magnitude=observation.log10_magnitude,
            diversion=observation.diversion,
        )
        for observation in _curve_observations(
            core_count=1, success_counts=(1, 2, 6, 7)
        )
    ]

    result = demand_curve.scenario_core_bootstrap(
        all_zero_core + increasing_core,
        mode="synthetic",
        seed=19,
    )
    family_result = result.family_results[0]

    assert result.status == "NOT_ESTIMABLE"
    assert family_result.status == "NOT_ESTIMABLE"
    assert 0 < family_result.estimable_replicates < 200
    assert len(family_result.replicate_statuses) == 200
    assert "CONSTANT_ZERO" in family_result.replicate_statuses
    assert family_result.ci95_log10 is None
    assert family_result.ci95_design_100 is None


@pytest.mark.parametrize(
    "bad_observation",
    [
        demand_curve.CurveObservation(
            family="buried_talent",
            core_id="core",
            log10_magnitude=-1.0,
            diversion=False,
        ),
        demand_curve.CurveObservation(
            family="always_up_rounding",
            core_id=" ",
            log10_magnitude=-1.0,
            diversion=False,
        ),
        demand_curve.CurveObservation(
            family="always_up_rounding",
            core_id="core",
            log10_magnitude=float("inf"),
            diversion=False,
        ),
        demand_curve.CurveObservation(
            family="always_up_rounding",
            core_id="core",
            log10_magnitude=-1.0,
            diversion=1,
        ),
    ],
)
def test_scenario_core_bootstrap_rejects_malformed_rows(bad_observation):
    with pytest.raises(ValueError, match="observation"):
        demand_curve.scenario_core_bootstrap(
            [bad_observation], mode="synthetic", seed=1
        )
