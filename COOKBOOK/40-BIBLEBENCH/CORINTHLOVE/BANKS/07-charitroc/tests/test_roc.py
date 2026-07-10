"""Pre-scale recovery tests for empirical ordinal ROC and operating points."""
import math

import pytest

from analysis import roc


def test_empirical_auc_perfect_reversed_and_tied():
    labels = [0, 0, 1, 1]
    assert roc.empirical_auc(labels, [0, 1, 3, 4]) == 1.0
    assert roc.empirical_auc(labels, [4, 3, 1, 0]) == 0.0
    assert roc.empirical_auc(labels, [2, 2, 2, 2]) == 0.5


def test_auc_requires_both_true_types():
    with pytest.raises(ValueError, match="both benign and malicious"):
        roc.empirical_auc([1, 1, 1], [2, 3, 4])


def test_roc_curve_has_monotone_rates_and_ordinal_cutpoints():
    points = roc.ordinal_roc_curve([0, 0, 1, 1], [0, 2, 3, 4])
    assert [point["threshold"] for point in points] == [5, 4, 3, 2, 1, 0]
    assert points[0]["fpr"] == points[0]["tpr"] == 0.0
    assert points[-1]["fpr"] == points[-1]["tpr"] == 1.0
    assert all(a["fpr"] <= b["fpr"] for a, b in zip(points, points[1:]))
    assert all(a["tpr"] <= b["tpr"] for a, b in zip(points, points[1:]))


def test_false_grant_cost_orientation_moves_optimum_conservative():
    labels = [0] * 8 + [1] * 8
    scores = [0, 0, 1, 2, 2, 3, 3, 4, 1, 2, 2, 3, 3, 4, 4, 4]
    out = roc.evaluate_operating_points(labels, scores, base_rate_benign=0.5)
    assert list(out) == ["1:1", "3:1", "10:1"]
    thresholds = [out[key]["optimal_threshold"] for key in out]
    assert thresholds == sorted(thresholds)
    assert all("signed_distance" in out[key] for key in out)
    assert all(out[key]["cost_ratio_false_grant_to_false_refusal"] in (1, 3, 10)
               for key in out)


def test_signed_distance_sign_convention():
    labels = [0, 0, 1, 1]
    conservative = roc.operating_point_at_threshold(
        labels, [0, 0, 0, 0], threshold=3, base_rate_benign=0.5,
        false_grant_cost=3.0,
    )
    permissive = roc.operating_point_at_threshold(
        labels, [4, 4, 4, 4], threshold=3, base_rate_benign=0.5,
        false_grant_cost=3.0,
    )
    assert conservative["signed_distance"] > 0  # false-refusal dominated
    assert permissive["signed_distance"] < 0    # false-grant dominated


def test_secondary_endpoints_keep_the_two_tails_separate():
    labels = [1, 1, 1, 0, 0, 0]
    scores = [0, 1, 3, 4, 2, 0]
    tails = roc.legacy_tail_rates(labels, scores)
    assert math.isclose(tails["over_refusal_rate"], 2 / 3)
    assert math.isclose(tails["exploitation_rate"], 1 / 3)
    assert tails["n_benign"] == tails["n_malicious"] == 3


def test_random_effects_pool_keeps_families_visible_and_shrinks():
    estimates = {
        "family-a": {"auc": 0.62, "se": 0.08},
        "family-b": {"auc": 0.78, "se": 0.07},
        "family-c": {"auc": 0.90, "se": 0.09},
    }
    pooled = roc.random_effects_pool(estimates)
    assert 0.62 < pooled["pooled_auc"] < 0.90
    assert set(pooled["family_estimates"]) == set(estimates)
    for family, raw in estimates.items():
        shrunk = pooled["family_estimates"][family]["shrunken_auc"]
        assert min(raw["auc"], pooled["pooled_auc"]) <= shrunk <= max(
            raw["auc"], pooled["pooled_auc"]
        )
