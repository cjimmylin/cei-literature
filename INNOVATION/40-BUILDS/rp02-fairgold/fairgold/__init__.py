"""fairgold — aggregation-invariance rescoring toolkit for values benchmarks.

RP-02 deliverable T2 (objective O2): a pure-computation engine that
rescores stored benchmark predictions under a family of defensible
label-aggregation rules and reports how much model rankings move across
them (the "aggregation-sensitivity" statistic).

No live model calls, no network, no keys. See README.md.
"""
from __future__ import annotations

from .data import Answer, Benchmark, Item, Predictions
from .rules import (
    AggregationRule,
    BordaRule,
    DistributionalRule,
    ItemScoring,
    MaximalLotteryRule,
    PluralityRule,
    ProportionalRule,
    default_rules,
    get_rule,
)
from .engine import ModelScore, RescoringEngine, StabilityReport

__version__ = "0.1.0"

__all__ = [
    "Answer",
    "Benchmark",
    "Item",
    "Predictions",
    "AggregationRule",
    "ItemScoring",
    "PluralityRule",
    "ProportionalRule",
    "BordaRule",
    "MaximalLotteryRule",
    "DistributionalRule",
    "default_rules",
    "get_rule",
    "RescoringEngine",
    "ModelScore",
    "StabilityReport",
]
