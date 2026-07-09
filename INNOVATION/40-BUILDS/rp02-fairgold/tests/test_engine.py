"""Unit tests for the rescoring engine (synthetic fixtures only).

These verify the plumbing: scoring, ranking, Kendall-tau stability, and
contestedness stratification. The specific stability numbers here are
properties of the TOY-SYNTHETIC fixture, NOT findings about any real
benchmark.
"""
from __future__ import annotations

import pytest

from fairgold.data import Benchmark, Item, Predictions
from fairgold.engine import RescoringEngine
from fairgold.rules import (
    BordaRule,
    DistributionalRule,
    MaximalLotteryRule,
    PluralityRule,
    ProportionalRule,
    default_rules,
)
from tests.fixtures import toy_benchmark, toy_predictions


def test_score_model_mean_over_items():
    bench = Benchmark("b", [Item("i1", ["A", "B"], votes=["A"] * 4 + ["B"]),
                            Item("i2", ["A", "B"], votes=["B"] * 3 + ["A"] * 2)])
    eng = RescoringEngine(bench)
    preds = {"i1": "A", "i2": "B"}  # both plurality winners
    ms = eng.score_model(preds, PluralityRule())
    assert ms.score == pytest.approx(1.0)
    assert ms.n_items == 2


def test_score_model_missing_prediction_raises():
    bench = Benchmark("b", [Item("i1", ["A", "B"], votes=["A", "B"])])
    eng = RescoringEngine(bench)
    with pytest.raises(KeyError):
        eng.score_model({}, PluralityRule())


def test_score_model_skip_missing():
    bench = Benchmark("b", [Item("i1", ["A", "B"], votes=["A", "A", "B"]),
                            Item("i2", ["A", "B"], votes=["A", "B"])])
    eng = RescoringEngine(bench)
    ms = eng.score_model({"i1": "A"}, PluralityRule(), skip_missing=True)
    assert ms.n_items == 1
    assert ms.score == pytest.approx(1.0)


def test_borda_rule_skips_unsupported_items():
    # Item without rankings must be skipped by a Borda scoring pass.
    bench = Benchmark("b", [Item("i1", ["A", "B"], votes=["A", "B"])])
    eng = RescoringEngine(bench)
    ms = eng.score_model({"i1": "A"}, BordaRule())
    assert ms.n_items == 0  # nothing Borda-scorable


def test_rank_models_orders_by_score():
    from fairgold.engine import ModelScore
    scores = {
        "m1": ModelScore("m1", 0.9, 3),
        "m2": ModelScore("m2", 0.5, 3),
        "m3": ModelScore("m3", 0.7, 3),
    }
    ranks = dict(RescoringEngine.rank_models(scores))
    assert ranks == {"m1": 1, "m3": 2, "m2": 3}


def test_rank_models_ties_share_rank():
    from fairgold.engine import ModelScore
    scores = {
        "m1": ModelScore("m1", 0.8, 3),
        "m2": ModelScore("m2", 0.8, 3),
        "m3": ModelScore("m3", 0.4, 3),
    }
    ranks = dict(RescoringEngine.rank_models(scores))
    assert ranks["m1"] == 1
    assert ranks["m2"] == 1
    assert ranks["m3"] == 3


def test_stability_report_structure():
    eng = RescoringEngine(toy_benchmark())
    report = eng.stability(toy_predictions(), default_rules())
    assert len(report.rule_names) == 5
    # C(5,2) = 10 rule pairs.
    assert len(report.pairwise_tau) == 10
    assert -1.0 <= report.min_tau <= 1.0
    assert report.min_tau <= report.mean_tau + 1e-9
    for model in ("majority_chaser", "consensus_matcher"):
        assert set(report.scores[model].keys()) == set(report.rule_names)


def test_aggregation_sensitivity_is_detectable_on_toy():
    # The toy fixture is CONSTRUCTED so the two models swap under some rule
    # pair (majority_chaser wins under plurality; consensus_matcher gains
    # under Borda/proportional). This asserts the engine can REGISTER
    # non-invariance, not that any real benchmark is non-invariant.
    eng = RescoringEngine(toy_benchmark())
    report = eng.stability(toy_predictions(), default_rules())
    plur = report.scores["majority_chaser"]["plurality"]
    plur2 = report.scores["consensus_matcher"]["plurality"]
    borda = report.scores["majority_chaser"]["borda"]
    borda2 = report.scores["consensus_matcher"]["borda"]
    # majority_chaser leads under plurality...
    assert plur > plur2
    # ...but consensus_matcher catches up or leads under Borda.
    assert borda2 >= borda - 1e-9


def test_consensus_score_extremes():
    eng = RescoringEngine(toy_benchmark())
    from tests.fixtures import unanimous_item, condorcet_cycle_item
    assert eng.consensus_score(unanimous_item()) == pytest.approx(1.0)
    assert eng.consensus_score(condorcet_cycle_item()) == pytest.approx(0.0)


def test_stratify_splits_by_contestedness():
    eng = RescoringEngine(toy_benchmark())
    strata = eng.stratify(thresholds=(0.5,))
    assert set(strata.keys()) == {"contested", "consensus"}
    # unanimous item is consensus; cycle item is contested.
    assert "unan" in strata["consensus"]
    assert "cyc" in strata["contested"]


def test_stratify_bad_labels_raise():
    eng = RescoringEngine(toy_benchmark())
    with pytest.raises(ValueError):
        eng.stratify(thresholds=(0.3, 0.6), labels=["only-one"])


def test_stability_by_stratum_returns_per_tier_reports():
    eng = RescoringEngine(toy_benchmark())
    out = eng.stability_by_stratum(toy_predictions(), default_rules(), thresholds=(0.5,))
    assert set(out.keys()).issubset({"contested", "consensus"})
    for report in out.values():
        assert len(report.rule_names) == 5


def test_distributional_predictions_scored():
    # A model that emits distributions is scored via score_distribution.
    bench = Benchmark("b", [Item("i1", ["A", "B"], votes=["A", "A", "B"])])  # pop 2/3,1/3
    eng = RescoringEngine(bench)
    preds = Predictions({"m": {"i1": {"A": 2 / 3, "B": 1 / 3}}})
    res = eng.score_all(preds, DistributionalRule("tv"))
    assert res["m"].score == pytest.approx(1.0)  # perfect match
