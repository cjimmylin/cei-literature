"""walkworthy_inspect — WALKWORTHY (Christian-Ethics-Benchmark) on Inspect AI.

Re-platforms the v1 harness (../Christian-Ethics-Benchmark/, frozen, READ-ONLY) onto
Inspect AI. Rubrics / parsers / refusal taxonomy / metric logic are ported from v1;
dataset loading, solvers, and scorers are Inspect-native and consume the frozen v2
dataset contract (tools/SCHEMA.md).
"""
from __future__ import annotations

from walkworthy_inspect.datasets import (
    WalkworthyHoldoutError,
    load_design,
    load_holdout,
    record_to_sample,
)
from walkworthy_inspect.metrics import PRIMARY_METRICS
from walkworthy_inspect.rubrics import DESIGN_RUBRICS, spec_for
from walkworthy_inspect.scorers import SCORER_FACTORIES
from walkworthy_inspect.solvers import multiturn_ladder_solver, single_turn_solver

__all__ = [
    "load_design",
    "load_holdout",
    "record_to_sample",
    "WalkworthyHoldoutError",
    "spec_for",
    "DESIGN_RUBRICS",
    "SCORER_FACTORIES",
    "PRIMARY_METRICS",
    "single_turn_solver",
    "multiturn_ladder_solver",
]

# designs that use the scripted multi-turn ladder solver
MULTITURN_DESIGNS = {"02", "07"}
