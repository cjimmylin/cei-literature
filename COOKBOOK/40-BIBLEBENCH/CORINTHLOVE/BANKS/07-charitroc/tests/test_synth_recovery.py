"""Planted-parameter recovery gate that must pass before scale generation."""
from analysis import roc, synth_recovery


def test_recover_planted_discrete_auc_and_interval():
    rows, planted = synth_recovery.simulate_ordinal(seed=20260709, n_per_type=4000)
    labels = [row["label"] for row in rows]
    scores = [row["score"] for row in rows]
    estimate = roc.clustered_bootstrap_auc(labels, scores, draws=600, seed=20260709)
    assert abs(estimate["auc"] - planted["auc"]) < 0.03, estimate
    assert estimate["ci95"][0] < planted["auc"] < estimate["ci95"][1], estimate


def test_recover_cost_ratio_threshold_ordering():
    rows, _ = synth_recovery.simulate_ordinal(seed=17, n_per_type=3000)
    out = roc.evaluate_operating_points(
        [row["label"] for row in rows],
        [row["score"] for row in rows],
        base_rate_benign=0.5,
    )
    thresholds = [out[key]["optimal_threshold"] for key in ("1:1", "3:1", "10:1")]
    assert thresholds == sorted(thresholds), out


def test_recover_planted_stage3_accuracy_separately():
    records, planted = synth_recovery.simulate_stage3(seed=23, n=2000,
                                                       accuracy=0.76)
    observed = sum(record["update_correct"] for record in records) / len(records)
    assert abs(observed - planted["stage3_accuracy"]) < 0.03


def test_auc_recovery_input_contains_no_stage3_field():
    rows, _ = synth_recovery.simulate_ordinal(seed=5, n_per_type=100)
    assert rows
    assert all(set(row) == {"label", "score", "pair_id"} for row in rows)
