"""Family-stratified analysis and D-07 channel separation."""
from collections import Counter
import math

import pytest

from analysis import analyze
from analysis import synth_recovery


def synthetic_rows(n_families=3, n_per_type=120):
    rows, _ = synth_recovery.simulate_ordinal(seed=101, n_per_type=n_per_type)
    output = []
    families = [f"family-{index}" for index in range(n_families)]
    for index, row in enumerate(rows):
        family = families[index % n_families]
        output.append({
            "item_family": family,
            "label": row["label"],
            "stage4_score": row["score"],
            "pair_id": f"{family}-{row['pair_id']}",
            "base_rate_benign": (0.2, 0.5, 0.8)[index % 3],
        })
    return output


def endpoint_rows(malicious_score, benign_score, n_families=2):
    """Small paired bank whose family AUC is exactly 0, 0.5, or 1."""
    output = []
    for family_index in range(n_families):
        family = f"endpoint-family-{family_index}"
        for pair_index, prior in enumerate((0.2, 0.5, 0.8)):
            pair_id = f"{family}-pair-{pair_index}"
            output.extend([
                {
                    "item_family": family,
                    "label": 0,
                    "stage4_score": malicious_score,
                    "pair_id": pair_id,
                    "base_rate_benign": prior,
                },
                {
                    "item_family": family,
                    "label": 1,
                    "stage4_score": benign_score,
                    "pair_id": pair_id,
                    "base_rate_benign": prior,
                },
            ])
    return output


def test_model_analysis_keeps_family_estimates_visible_and_pools():
    result = analyze.analyze_model(synthetic_rows(), bootstrap_draws=120, seed=7)
    assert set(result["family_auc"]) == {"family-0", "family-1", "family-2"}
    assert 0.5 < result["hierarchical_pool"]["pooled_auc"] < 1.0
    assert set(result["hierarchical_pool"]["family_estimates"]) == set(result["family_auc"])
    assert set(result["operating_points_by_prior"]) == {"0.2", "0.5", "0.8"}
    for prior_result in result["operating_points_by_prior"].values():
        assert set(prior_result) == {"1:1", "3:1", "10:1"}


@pytest.mark.parametrize(
    ("malicious_score", "benign_score", "expected_auc"),
    [
        pytest.param(0, 4, 1.0, id="perfect"),
        pytest.param(4, 0, 0.0, id="reversed"),
        pytest.param(2, 2, 0.5, id="tied"),
    ],
)
def test_model_analysis_pools_endpoint_auc_families_without_changing_raw_values(
        malicious_score, benign_score, expected_auc):
    result = analyze.analyze_model(
        endpoint_rows(malicious_score, benign_score),
        bootstrap_draws=100,
        seed=7,
    )

    raw_values = {
        estimate["auc"] for estimate in result["family_auc"].values()
    }
    pooled_families = result["hierarchical_pool"]["family_estimates"]

    assert raw_values == {expected_auc}
    assert {row["auc"] for row in pooled_families.values()} == {expected_auc}
    assert math.isfinite(result["hierarchical_pool"]["pooled_auc"])
    assert math.isfinite(result["hierarchical_pool"]["tau2_logit"])
    assert all(math.isfinite(row["shrunken_auc"])
               for row in pooled_families.values())


def test_model_analysis_rejects_a_family_missing_one_true_type():
    rows = [row for row in synthetic_rows() if not (
        row["item_family"] == "family-0" and row["label"] == 0
    )]
    with pytest.raises(ValueError, match="family-0.*both benign and malicious"):
        analyze.analyze_model(rows, bootstrap_draws=100, seed=7)


def test_stage3_aggregation_is_a_separate_api_and_stratifies_cues():
    records, _ = synth_recovery.simulate_stage3(seed=3, n=400, accuracy=0.75)
    result = analyze.aggregate_stage3(records)
    assert result["n"] == 400
    assert set(result["by_cue"]) == {"strong", "weak", "absent", "adversarial"}
    assert Counter(row["cue_variant"] for row in records) == Counter({
        "strong": 100, "weak": 100, "absent": 100, "adversarial": 100,
    })
    assert "auc" not in result


def test_primary_analysis_rows_reject_stage3_as_score_field():
    rows = synthetic_rows()
    rows[0]["stage3_update_score"] = rows[0].pop("stage4_score")
    with pytest.raises(ValueError, match="stage4_score"):
        analyze.analyze_model(rows, bootstrap_draws=100, seed=7)
