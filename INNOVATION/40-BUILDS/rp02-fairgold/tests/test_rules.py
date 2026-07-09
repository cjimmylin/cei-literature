"""Unit tests for every aggregation rule (synthetic fixtures only).

Exercises the five-rule family named in RP-02 method step 2. All expected
values are computed by hand in the fixture docstrings; nothing here is a
measurement.
"""
from __future__ import annotations

import pytest

from fairgold.rules import (
    BordaRule,
    DistributionalRule,
    MaximalLotteryRule,
    PluralityRule,
    ProportionalRule,
    default_rules,
    get_rule,
)
from tests.fixtures import (
    borda_vs_plurality_item,
    condorcet_cycle_item,
    condorcet_winner_item,
    split_votes_item,
    tie_item,
    unanimous_item,
)


# -- Plurality -------------------------------------------------------------
def test_plurality_winner_gets_full_credit():
    s = PluralityRule().item_scoring(split_votes_item())  # X=6,Y=3,Z=1
    assert s.score_point("X") == pytest.approx(1.0)
    assert s.score_point("Y") == pytest.approx(0.0)
    assert s.score_point("Z") == pytest.approx(0.0)


def test_plurality_tie_splits_credit():
    s = PluralityRule().item_scoring(tie_item())  # P=5,Q=5
    assert s.score_point("P") == pytest.approx(0.5)
    assert s.score_point("Q") == pytest.approx(0.5)


def test_plurality_unknown_answer_scores_zero():
    s = PluralityRule().item_scoring(split_votes_item())
    assert s.score_point("not-an-option") == 0.0


# -- Proportional ----------------------------------------------------------
def test_proportional_credit_is_population_share():
    s = ProportionalRule().item_scoring(split_votes_item())  # 6/3/1 of 10
    assert s.score_point("X") == pytest.approx(0.6)
    assert s.score_point("Y") == pytest.approx(0.3)
    assert s.score_point("Z") == pytest.approx(0.1)


# -- Borda -----------------------------------------------------------------
def test_borda_winner_differs_from_plurality():
    item = borda_vs_plurality_item()  # plurality A, borda B
    borda = BordaRule()
    plurality_winner = max(
        PluralityRule().item_scoring(item).credit,
        key=PluralityRule().item_scoring(item).credit.get,
    )
    assert plurality_winner == "A"
    assert borda.borda_winner(item) == "B"


def test_borda_normalized_credit_values():
    # Borda points A=80, B=125, C=95; normalized by max (B=125).
    s = BordaRule().item_scoring(borda_vs_plurality_item())
    assert s.score_point("B") == pytest.approx(1.0)
    assert s.score_point("A") == pytest.approx(80 / 125)
    assert s.score_point("C") == pytest.approx(95 / 125)


def test_borda_requires_rankings():
    borda = BordaRule()
    votes_only = split_votes_item()
    assert borda.supports(votes_only) is False
    with pytest.raises(ValueError):
        borda.item_scoring(votes_only)


# -- Maximal lottery -------------------------------------------------------
def test_maximal_lottery_cycle_is_uniform():
    s = MaximalLotteryRule().item_scoring(condorcet_cycle_item())
    for opt in ("A", "B", "C"):
        assert s.score_point(opt) == pytest.approx(1.0 / 3.0, abs=1e-6)


def test_maximal_lottery_condorcet_winner_gets_all_mass():
    s = MaximalLotteryRule().item_scoring(condorcet_winner_item())
    assert s.score_point("A") == pytest.approx(1.0, abs=1e-6)
    assert s.score_point("B") == pytest.approx(0.0, abs=1e-6)


def test_maximal_lottery_votes_only_collapses_to_plurality():
    # Ambiguity A3: no rankings -> ML degenerates onto plurality winner.
    s = MaximalLotteryRule().item_scoring(split_votes_item())  # X=6 plurality
    assert s.score_point("X") == pytest.approx(1.0, abs=1e-6)


# -- Distributional --------------------------------------------------------
def test_distributional_point_reduces_to_proportional_under_tv():
    # Ambiguity A4: TV point-credit == proportional credit.
    item = split_votes_item()
    dist_rule = DistributionalRule("tv").item_scoring(item)
    prop_rule = ProportionalRule().item_scoring(item)
    for opt in ("X", "Y", "Z"):
        assert dist_rule.score_point(opt) == pytest.approx(prop_rule.score_point(opt))


def test_distributional_perfect_match_scores_one():
    item = split_votes_item()  # pop 0.6/0.3/0.1
    s = DistributionalRule("tv").item_scoring(item)
    perfect = {"X": 0.6, "Y": 0.3, "Z": 0.1}
    assert s.score_distribution(perfect) == pytest.approx(1.0)


def test_distributional_confident_wrong_scores_low():
    item = split_votes_item()
    s = DistributionalRule("tv").item_scoring(item)
    # All mass on the 0.1-share option -> TV distance high -> low score.
    wrong = {"Z": 1.0}
    assert s.score_distribution(wrong) == pytest.approx(0.1)


def test_distributional_jsd_variant_runs():
    item = split_votes_item()
    s = DistributionalRule("jsd").item_scoring(item)
    assert s.score_distribution({"X": 0.6, "Y": 0.3, "Z": 0.1}) == pytest.approx(1.0)


def test_distributional_bad_distance_rejected():
    with pytest.raises(ValueError):
        DistributionalRule("cosine")


# -- Registry / expected-credit default -----------------------------------
def test_default_rules_has_five():
    names = [r.name for r in default_rules()]
    assert names == [
        "plurality",
        "proportional",
        "borda",
        "maximal_lottery",
        "distributional_tv",
    ]


def test_get_rule_unknown_raises():
    with pytest.raises(KeyError):
        get_rule("nonexistent")


def test_expected_credit_default_scorer_on_plurality():
    # A model distribution scored by a non-distributional rule uses
    # expected credit under that distribution.
    s = PluralityRule().item_scoring(split_votes_item())  # X credit 1, else 0
    assert s.score_distribution({"X": 0.7, "Y": 0.3}) == pytest.approx(0.7)
