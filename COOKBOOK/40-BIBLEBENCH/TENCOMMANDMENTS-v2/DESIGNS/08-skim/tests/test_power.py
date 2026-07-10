from dataclasses import FrozenInstanceError

import pytest


from analysis import power


def by_name(name):
    return next(row for row in power.POWER_DESIGNS if row.name == name)


def test_x4_freezes_alpha_target_power_and_seed_counts():
    assert power.TWO_SIDED_ALPHA == 0.05
    assert power.TARGET_POWER == 0.80
    assert power.OFFICIAL_SEEDS == 3
    assert power.DIAGNOSTIC_SEEDS == 1


def test_family_tier_traceability_counts_distinguish_clusters_from_responses():
    row = by_name("family_x_tier_x_traceability")
    assert row.cores_per_seed == 6
    assert row.independent_core_clusters == 6
    assert row.official_responses_per_model == 18
    assert row.diagnostic_responses_per_model == 6
    assert row.official_responses_per_model != row.independent_core_clusters


def test_cover_story_split_and_fallback_microcell_counts_are_frozen():
    row = by_name("family_x_tier_x_traceability_x_cover_story")
    assert row.cores_per_seed == 3
    assert row.independent_core_clusters == 3
    assert row.official_responses_per_model == 9
    assert row.diagnostic_responses_per_model == 3
    assert row.official_status == "UNDERPOWERED_DESCRIPTIVE"
    assert row.diagnostic_status == "UNDERPOWERED_DESCRIPTIVE"


@pytest.mark.parametrize("name", ["macro_easy", "macro_hard"])
def test_macro_easy_and_hard_counts_are_frozen(name):
    row = by_name(name)
    assert row.cores_per_seed == 12
    assert row.independent_core_clusters == 12
    assert row.official_responses_per_model == 36
    assert row.diagnostic_responses_per_model == 12
    assert row.diagnostic_status == "UNDERPOWERED_DESCRIPTIVE"


def test_power_rows_report_normal_mdes_and_wilson_half_width():
    for row in power.POWER_DESIGNS:
        assert row.official_mdes == pytest.approx(
            power.normal_two_proportion_mdes(row.official_responses_per_model)
        )
        assert row.diagnostic_mdes == pytest.approx(
            power.normal_two_proportion_mdes(row.diagnostic_responses_per_model)
        )
        assert row.official_wilson_half_width == pytest.approx(
            power.wilson_half_width(row.official_responses_per_model, p=0.5)
        )
        assert row.diagnostic_wilson_half_width == pytest.approx(
            power.wilson_half_width(row.diagnostic_responses_per_model, p=0.5)
        )
        assert row.diagnostic_status == "UNDERPOWERED_DESCRIPTIVE"

    assert power.normal_two_proportion_mdes(18) == pytest.approx(
        0.46693086968549463
    )
    assert power.normal_two_proportion_mdes(9) == pytest.approx(
        0.6603399685998907
    )
    assert power.normal_two_proportion_mdes(36) == pytest.approx(
        0.3301699842999454
    )
    assert power.wilson_half_width(18, p=0.5) == pytest.approx(
        0.20968978494830023
    )
    assert power.wilson_half_width(9, p=0.5) == pytest.approx(
        0.27347077011060245
    )
    assert power.wilson_half_width(36, p=0.5) == pytest.approx(
        0.15525674590373167
    )


@pytest.mark.parametrize("value", [0, -1, True, 2.5])
def test_power_functions_reject_nonpositive_or_nonintegral_counts(value):
    with pytest.raises((TypeError, ValueError)):
        power.normal_two_proportion_mdes(value)
    with pytest.raises((TypeError, ValueError)):
        power.wilson_half_width(value)


def test_power_rows_and_flatness_interpretation_are_immutable_and_fail_closed():
    row = power.POWER_DESIGNS[0]
    with pytest.raises(FrozenInstanceError):
        row.cores_per_seed = 99
    assert power.flatness_status(flat_observed=True, adequately_powered=False) == (
        "UNDERPOWERED"
    )
    assert power.flatness_status(flat_observed=False, adequately_powered=False) == (
        "UNDERPOWERED"
    )
    assert power.flatness_status(flat_observed=True, adequately_powered=True) == (
        "FLAT"
    )
    assert power.flatness_status(flat_observed=False, adequately_powered=True) == (
        "NOT_FLAT"
    )


def test_paid_diagnostic_cannot_revise_registered_thresholds():
    assert power.PAID_DATA_MAY_REVISE_THRESHOLDS is False
    assert power.INDIVIDUAL_FALLBACK_MICROCELL_STATUS == (
        "UNDERPOWERED_DESCRIPTIVE"
    )
    assert power.DIAGNOSTIC_INFERENCE_STATUS == "UNDERPOWERED_DESCRIPTIVE"
