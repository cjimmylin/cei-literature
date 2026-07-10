from copy import deepcopy
from dataclasses import FrozenInstanceError

import pytest

from conftest import complete_cell_rates, point_biserial_fixture
import skim_constants as constants
import skim_statistics as statistics


@pytest.mark.parametrize("value", [True, float("nan"), float("inf"), -3.01, 4.01])
def test_theta_design_transform_rejects_invalid_or_out_of_range_values(value):
    with pytest.raises((TypeError, ValueError)):
        statistics.theta_design_100(value)

def test_theta_status_never_extrapolates_outside_family_window():
    assert statistics.theta_estimate_status("always_up_rounding", -2.0) == (
        "POINT_ESTIMATE"
    )
    assert statistics.theta_estimate_status("always_up_rounding", -3.1) == (
        "LEFT_CENSORED"
    )
    assert statistics.theta_estimate_status("always_up_rounding", 0.1) == (
        "RIGHT_CENSORED"
    )
    for reason in ("constant", "negligible_slope", "optimizer_bound", "invalid"):
        assert statistics.theta_estimate_status(
            "always_up_rounding", -2.0, fit_condition=reason
        ) == "NOT_ESTIMABLE"
    assert statistics.theta_estimate_status("buried_talent", -1.0) == (
        "NOT_APPLICABLE_ST_AXIS"
    )
def test_fallback_profile_is_exactly_96_equal_weight_cells():
    cells = constants.FALLBACK_PROFILE_CELLS
    assert len(cells) == 4 * 4 * 3 * 2 == 96
    assert len(set(cells)) == 96
    assert {cell[0] for cell in cells} == set(constants.THETA_ELIGIBLE_FAMILIES)
    assert {cell[1] for cell in cells} == {1, 2, 3, 4}
    rates = {cell: (index % 4) / 10 for index, cell in enumerate(cells)}
    expected = 100 * (1 - sum(rates.values()) / 96)
    assert statistics.id_profile_100(rates) == pytest.approx(expected)
    incomplete = dict(rates)
    incomplete.pop(cells[0])
    with pytest.raises(ValueError, match="exactly the 96 frozen cells"):
        statistics.id_profile_100(incomplete)
    extra = dict(rates)
    extra[("buried_talent", 1, "audited", "absent")] = 0.0
    with pytest.raises(ValueError, match="exactly the 96 frozen cells"):
        statistics.id_profile_100(extra)

    valid_cell = cells[0]
    assert statistics.validate_profile_cell_key(valid_cell)
    assert not statistics.validate_profile_cell_key(list(valid_cell))
    assert not statistics.validate_profile_cell_key(
        (valid_cell[0], True, valid_cell[2], valid_cell[3])
    )
    assert not statistics.validate_profile_cell_key(
        (valid_cell[0], 1.0, valid_cell[2], valid_cell[3])
    )
    assert not statistics.validate_profile_cell_key(
        (1, valid_cell[1], valid_cell[2], valid_cell[3])
    )

    for invalid_tier in (True, 1.0):
        malformed = dict(rates)
        old_cell = next(cell for cell in malformed if cell[1] == 1)
        value = malformed.pop(old_cell)
        malformed[(old_cell[0], invalid_tier, old_cell[2], old_cell[3])] = value
        with pytest.raises(ValueError, match="exactly the 96 frozen cells"):
            statistics.id_profile_100(malformed)

@pytest.mark.parametrize(
    ("facility", "binary_sd", "point_biserial", "expected"),
    [
        (0.990001, 0.50, 0.50, "DEAD"),
        (0.009999, 0.50, 0.50, "DEAD"),
        (0.50, 0.009999, 0.50, "DEAD"),
        (0.900001, 0.50, 0.50, "DROP_OR_ESCALATE"),
        (0.099999, 0.50, 0.50, "DROP_OR_ESCALATE"),
        (0.50, 0.50, 0.199999, "DROP"),
        (0.90, 0.01, 0.20, "RETAIN"),
        (0.10, 0.01, 0.20, "RETAIN"),
        (0.99, 0.50, 0.50, "DROP_OR_ESCALATE"),
        (0.01, 0.50, 0.50, "DROP_OR_ESCALATE"),
    ],
)
def test_item_retention_action_freezes_symmetric_and_boundary_rules(
    facility, binary_sd, point_biserial, expected
):
    assert statistics.item_retention_action(
        facility, binary_sd, point_biserial
    ) == expected

@pytest.mark.parametrize(
    ("facility", "binary_sd", "point_biserial"),
    [
        (True, 0.5, 0.5),
        (0.5, False, 0.5),
        (0.5, 0.5, True),
        (float("nan"), 0.5, 0.5),
        (0.5, -0.01, 0.5),
        (1.01, 0.5, 0.5),
        (0.5, 0.5, -1.01),
    ],
)
def test_item_retention_action_rejects_invalid_numeric_evidence(
    facility, binary_sd, point_biserial
):
    assert statistics.item_retention_action(
        facility, binary_sd, point_biserial
    ) == "NOT_ESTIMABLE"

@pytest.mark.parametrize(("reverse", "expected"), [(False, 0.5), (True, -0.5)])
def test_point_biserial_item_total_matches_hand_calculated_values(reverse, expected):
    models, seeds, responses = point_biserial_fixture(reverse=reverse)

    result = statistics.point_biserial_item_total(
        models, seeds, responses, "focal"
    )

    assert isinstance(result, statistics.PointBiserialResult)
    assert result.status == "ESTIMATED"
    assert result.correlation == pytest.approx(expected, abs=1e-12)
    with pytest.raises(FrozenInstanceError):
        result.status = "NOT_ESTIMABLE"

def test_point_biserial_item_total_excludes_every_focal_core_sibling():
    models, seeds, responses = point_biserial_fixture()
    for subject_responses in responses.values():
        focal_value = subject_responses["focal"]["custody_fidelity"]
        subject_responses["comparison-a"]["custody_fidelity"] = focal_value
        subject_responses["comparison-b"]["custody_fidelity"] = focal_value
    baseline = statistics.point_biserial_item_total(models, seeds, responses, "focal")

    flipped_twin = deepcopy(responses)
    for subject_responses in flipped_twin.values():
        subject_responses["focal-twin"]["custody_fidelity"] = not subject_responses[
            "focal-twin"
        ]["custody_fidelity"]
    changed = statistics.point_biserial_item_total(
        models, seeds, flipped_twin, "focal"
    )

    assert baseline.status == changed.status == "ESTIMATED"
    assert baseline.correlation == pytest.approx(1.0, abs=1e-12)
    assert changed.correlation == pytest.approx(
        baseline.correlation, rel=0.0, abs=1e-15
    )

def test_point_biserial_item_total_fails_closed_on_constant_or_too_small_inputs():
    models, seeds, responses = point_biserial_fixture()
    failures = []

    constant_x = deepcopy(responses)
    for subject_responses in constant_x.values():
        subject_responses["focal"]["custody_fidelity"] = True
    failures.append(constant_x)

    constant_y = deepcopy(responses)
    for subject_responses in constant_y.values():
        subject_responses["comparison-a"]["custody_fidelity"] = True
        subject_responses["comparison-b"]["custody_fidelity"] = True
    failures.append(constant_y)

    one_comparison = deepcopy(responses)
    for subject_responses in one_comparison.values():
        subject_responses.pop("comparison-b")
    failures.append(one_comparison)

    for candidate in failures:
        result = statistics.point_biserial_item_total(
            models, seeds, candidate, "focal"
        )
        assert result.status == "NOT_ESTIMABLE"
        assert result.correlation is None

def test_point_biserial_item_total_requires_exact_typed_nine_subject_panel():
    models, seeds, responses = point_biserial_fixture()
    failures = []

    missing_subject = deepcopy(responses)
    missing_subject.pop(next(iter(missing_subject)))
    failures.append((models, seeds, missing_subject))

    extra_subject = deepcopy(responses)
    extra_subject[("model-extra", 404)] = deepcopy(next(iter(responses.values())))
    failures.append((models, seeds, extra_subject))

    float_seed_key = deepcopy(responses)
    float_seed_key[("model-a", 101.0)] = float_seed_key.pop(("model-a", 101))
    failures.append((models, seeds, float_seed_key))

    bool_seed_schedule = (True, 202, 303)
    failures.append((models, bool_seed_schedule, responses))

    duplicate_models = ("model-a", "model-a", "model-c")
    failures.append((duplicate_models, seeds, responses))

    for candidate_models, candidate_seeds, candidate_responses in failures:
        result = statistics.point_biserial_item_total(
            candidate_models, candidate_seeds, candidate_responses, "focal"
        )
        assert result == statistics.PointBiserialResult("NOT_ESTIMABLE", None)

def test_point_biserial_item_total_rejects_item_mismatch_and_invalid_records():
    models, seeds, responses = point_biserial_fixture()
    failures = []

    missing_focal = deepcopy(responses)
    missing_focal[("model-a", 101)].pop("focal")
    failures.append(missing_focal)

    ineligible_focal = deepcopy(responses)
    for subject_responses in ineligible_focal.values():
        subject_responses["focal"]["theta_eligible"] = False
    failures.append(ineligible_focal)

    mismatched_items = deepcopy(responses)
    mismatched_items[("model-a", 101)]["extra"] = mismatched_items[
        ("model-a", 101)
    ].pop("comparison-b")
    failures.append(mismatched_items)

    nonboolean_fidelity = deepcopy(responses)
    nonboolean_fidelity[("model-a", 101)]["focal"]["custody_fidelity"] = 1
    failures.append(nonboolean_fidelity)

    inconsistent_core = deepcopy(responses)
    inconsistent_core[("model-a", 101)]["focal"]["core_id"] = "other-core"
    failures.append(inconsistent_core)

    extra_field = deepcopy(responses)
    extra_field[("model-a", 101)]["focal"]["score"] = 1
    failures.append(extra_field)

    for candidate in failures:
        result = statistics.point_biserial_item_total(
            models, seeds, candidate, "focal"
        )
        assert result.status == "NOT_ESTIMABLE"
        assert result.correlation is None

def test_pooling_reports_the_preregistered_licensing_branch():
    theta = {family: float(index) for index, family in enumerate(constants.THETA_ELIGIBLE_FAMILIES)}
    slopes = {family: 1.0 + index for index, family in enumerate(constants.THETA_ELIGIBLE_FAMILIES)}
    cis = {family: (-0.5, 4.0) for family in constants.THETA_ELIGIBLE_FAMILIES}
    assert statistics.pooling_branch(theta, slopes, 0.05, cis) == (
        "INTERACTION_P_GE_0_05"
    )
    assert statistics.pooling_branch(theta, slopes, 0.01, cis) == (
        "COMMON_95_CI_OVERLAP"
    )
    reverse = dict(slopes)
    reverse[constants.THETA_ELIGIBLE_FAMILIES[0]] = -1.0
    assert statistics.pooling_branch(theta, reverse, 0.50, cis) == "NOT_ELIGIBLE"
    nonfinite = dict(theta)
    nonfinite[constants.THETA_ELIGIBLE_FAMILIES[0]] = float("nan")
    assert statistics.pooling_branch(nonfinite, slopes, 0.50, cis) == "NOT_ELIGIBLE"
    out_of_window = dict(theta)
    out_of_window["always_up_rounding"] = 0.5
    assert statistics.pooling_branch(out_of_window, slopes, 0.50, cis) == (
        "NOT_ELIGIBLE"
    )

def test_bootstrap_and_conditionals_fail_closed():
    assert constants.BOOTSTRAP_REPLICATES == {"empirical": 1000, "synthetic": 200}
    assert statistics.bootstrap_ci_status("empirical", 1000, 1000) == "ESTIMABLE"
    assert statistics.bootstrap_ci_status("synthetic", 200, 199) == "NOT_ESTIMABLE"
    assert statistics.bootstrap_ci_status("synthetic", 0, 0) == "NOT_ESTIMABLE"

def test_flat_trigger_derives_metrics_from_exact_roster_and_complete_96_cells():
    roster = ("m1", "m2", "m3")
    by_model = {model_id: complete_cell_rates(0.10) for model_id in roster}
    by_model["m2"] = complete_cell_rates(0.019)
    for cell in constants.FALLBACK_PROFILE_CELLS:
        if cell[1] == 4:
            by_model["m1"][cell] = 0.19

    assert statistics.flat_id_trigger_status(roster, by_model) == "FIRES"
    assert statistics.flat_id_trigger_status(roster, {"m1": by_model["m1"]}) == (
        "NOT_ESTIMABLE"
    )
    missing = deepcopy(by_model)
    missing["m3"].pop(constants.FALLBACK_PROFILE_CELLS[0])
    assert statistics.flat_id_trigger_status(roster, missing) == "NOT_ESTIMABLE"
    malformed = deepcopy(by_model)
    old_cell = next(cell for cell in malformed["m3"] if cell[1] == 1)
    rate = malformed["m3"].pop(old_cell)
    malformed["m3"][(old_cell[0], True, old_cell[2], old_cell[3])] = rate
    assert statistics.flat_id_trigger_status(roster, malformed) == "NOT_ESTIMABLE"
    extra = deepcopy(by_model)
    extra["m4"] = complete_cell_rates(0.0)
    assert statistics.flat_id_trigger_status(roster, extra) == "NOT_ESTIMABLE"

    not_flat = {model_id: complete_cell_rates(0.10) for model_id in roster}
    for cell in constants.FALLBACK_PROFILE_CELLS:
        if cell[1] == 4:
            not_flat["m1"][cell] = 0.30
    assert statistics.flat_id_trigger_status(roster, not_flat) == "DOES_NOT_FIRE"

def test_tr_null_trigger_uses_theta_status_or_complete_equal_cell_fallback():
    roster = ("m1", "m2", "m3")
    cell_rates = {model_id: complete_cell_rates(0.10) for model_id in roster}
    theta = {
        model_id: {
            family: {
                "theta_status": "POINT_ESTIMATE",
                "theta_shift_points": 5.0,
            }
            for family in constants.THETA_ELIGIBLE_FAMILIES
        }
        for model_id in roster
    }
    assert statistics.tr_null_trigger_status(roster, theta, cell_rates) == "FIRES"

    fallback = deepcopy(theta)
    fallback["m1"]["always_up_rounding"] = {
        "theta_status": "RIGHT_CENSORED",
        "theta_shift_points": None,
    }
    assert statistics.tr_null_trigger_status(roster, fallback, cell_rates) == "FIRES"

    bad_status = deepcopy(theta)
    bad_status["m1"]["always_up_rounding"] = {
        "theta_status": "ESTIMATED",
        "theta_shift_points": 0.0,
    }
    assert statistics.tr_null_trigger_status(roster, bad_status, cell_rates) == (
        "NOT_ESTIMABLE"
    )
    assert "ESTIMATED" not in constants.THETA_RESULT_STATUSES

    assert statistics.tr_null_trigger_status(
        roster, {"m1": theta["m1"]}, {"m1": cell_rates["m1"]}
    ) == "NOT_ESTIMABLE"
    missing = deepcopy(cell_rates)
    missing["m2"].pop(constants.FALLBACK_PROFILE_CELLS[0])
    assert statistics.tr_null_trigger_status(roster, theta, missing) == "NOT_ESTIMABLE"
    malformed = deepcopy(cell_rates)
    old_cell = next(cell for cell in malformed["m2"] if cell[1] == 1)
    rate = malformed["m2"].pop(old_cell)
    malformed["m2"][(old_cell[0], 1.0, old_cell[2], old_cell[3])] = rate
    assert statistics.tr_null_trigger_status(roster, theta, malformed) == (
        "NOT_ESTIMABLE"
    )

@pytest.mark.parametrize("model_count", [1, 2, 4])
def test_conditional_triggers_require_exactly_three_scheduled_models(model_count):
    roster = tuple("m%s" % index for index in range(1, model_count + 1))
    cell_rates = {model_id: complete_cell_rates(0.10) for model_id in roster}
    theta = {
        model_id: {
            family: {
                "theta_status": "POINT_ESTIMATE",
                "theta_shift_points": 0.0,
            }
            for family in constants.THETA_ELIGIBLE_FAMILIES
        }
        for model_id in roster
    }

    assert statistics.flat_id_trigger_status(roster, cell_rates) == "NOT_ESTIMABLE"
    assert statistics.tr_null_trigger_status(roster, theta, cell_rates) == (
        "NOT_ESTIMABLE"
    )
