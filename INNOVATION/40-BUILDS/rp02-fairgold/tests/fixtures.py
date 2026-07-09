"""SYNTHETIC TEST FIXTURES — not data, not findings.

Every construct in this module is a hand-built toy example whose ONLY
purpose is to exercise the aggregation-rule arithmetic and the engine
plumbing against known-by-hand answers. These are NOT real benchmark
annotations and NOTHING computed from them is a measurement or result.
Do not cite any number derived from these fixtures. (RP-02 evidence
discipline: synthetic fixtures for unit tests only.)
"""
from __future__ import annotations

from fairgold.data import Benchmark, Item, Predictions


def borda_vs_plurality_item() -> Item:
    """Classic textbook profile where plurality != Borda winner.

    100 synthetic annotators over options A, B, C:
      40x  A > B > C
      35x  C > B > A
      25x  B > C > A
    Plurality winner = A (40 first-place votes).
    Borda points: A=80, B=125, C=95  -> Borda winner = B.
    """
    rankings = (
        [["A", "B", "C"]] * 40
        + [["C", "B", "A"]] * 35
        + [["B", "C", "A"]] * 25
    )
    return Item(item_id="bp", options=["A", "B", "C"], rankings=rankings)


def condorcet_cycle_item() -> Item:
    """Rock-paper-scissors 3-cycle -> maximal lottery is uniform (1/3 each)."""
    rankings = [
        ["A", "B", "C"],
        ["B", "C", "A"],
        ["C", "A", "B"],
    ]
    return Item(item_id="cyc", options=["A", "B", "C"], rankings=rankings)


def condorcet_winner_item() -> Item:
    """A is a Condorcet winner -> maximal lottery puts all mass on A."""
    rankings = [
        ["A", "B", "C"],
        ["A", "B", "C"],
        ["B", "C", "A"],
    ]
    return Item(item_id="cw", options=["A", "B", "C"], rankings=rankings)


def split_votes_item() -> Item:
    """Point-vote item: 6 X, 3 Y, 1 Z (10 annotators). Plurality winner X."""
    votes = ["X"] * 6 + ["Y"] * 3 + ["Z"] * 1
    return Item(item_id="split", options=["X", "Y", "Z"], votes=votes)


def tie_item() -> Item:
    """Two-way plurality tie: 5 P, 5 Q."""
    return Item(item_id="tie", options=["P", "Q"], votes=["P"] * 5 + ["Q"] * 5)


def unanimous_item() -> Item:
    return Item(item_id="unan", options=["A", "B"], votes=["A"] * 8)


def toy_benchmark() -> Benchmark:
    """Small benchmark mixing consensus and contested items (all synthetic)."""
    return Benchmark(
        name="TOY-SYNTHETIC",
        items=[
            unanimous_item(),           # consensus
            split_votes_item(),         # mild split
            condorcet_cycle_item(),     # maximally contested
            borda_vs_plurality_item(),  # aggregation-sensitive
        ],
    )


def toy_predictions() -> Predictions:
    """Two synthetic models with deliberately different answer profiles.

    'majority_chaser' always picks each item's plurality winner.
    'consensus_matcher' picks the Borda/second-choice compromise where it
    differs, to force ranking movement across rules.
    """
    p = Predictions()
    # unanimous item 'unan': winner A
    p.add("majority_chaser", "unan", "A")
    p.add("consensus_matcher", "unan", "A")
    # split item: plurality X
    p.add("majority_chaser", "split", "X")
    p.add("consensus_matcher", "split", "Y")
    # cycle item: both pick A
    p.add("majority_chaser", "cyc", "A")
    p.add("consensus_matcher", "cyc", "B")
    # borda-vs-plurality: plurality A, borda B
    p.add("majority_chaser", "bp", "A")
    p.add("consensus_matcher", "bp", "B")
    return p
