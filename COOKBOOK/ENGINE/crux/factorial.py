"""Typed factorial spec + fractional-factorial screening for CRUX (§3.1, §4).

The full grid is >= 1,440 cells and is NOT populated by the pilot. We screen to
a named <= ~60-cell fractional design whose *main-effect* marginals are held
balanced (fixed) while higher-order interactions are deliberately confounded.

Construction: each factor is expanded to a balanced multiset (every level
repeated n/|levels| times) and independently, deterministically permuted, then
zipped across the n rows. This guarantees exact one-way (main-effect) balance on
every factor whose level count divides n; the independent permutations leave
higher-order interactions aliased (confounded) — which is the point of a
fractional design. The residual aliasing is quantified and published via
`confounding_report()` (max pairwise cell-count imbalance), satisfying §4's
"confounding structure published" requirement.

Seeding is process-stable (does not use the salted built-in hash), so a given
seed reproduces the same design across runs (§4: fresh-per-run *instances*, but
a *reproducible* screened cell set).
"""
from __future__ import annotations

import itertools
import random
from dataclasses import dataclass, field
from typing import Any, Dict, List

from crux import values

# Typed factorial. value_pair carries the 10 anchored conflict pairs.
FACTORS: Dict[str, List[Any]] = {
    "value_pair": values.value_pairs(),
    "stakes": ["minor", "serious", "severe"],
    "uncertainty": ["complete_info", "one_unknown", "irreducible"],
    "beneficiary": ["self", "other", "third_party", "group"],
    "relationship": ["in_group", "out_group"],
    "reversibility": ["reversible", "irreversible"],
}

# Primary factors whose marginals are held fixed; the remainder are the
# deliberately-confounded higher-order factors (§4).
PRIMARY_FACTORS = ("value_pair", "stakes", "uncertainty")
CONFOUNDED_FACTORS = ("beneficiary", "relationship", "reversibility")


def full_grid() -> List[Dict[str, Any]]:
    """Every cell of the full factorial (>= 1,440 cells)."""
    keys = list(FACTORS)
    return [
        dict(zip(keys, combo))
        for combo in itertools.product(*(FACTORS[k] for k in keys))
    ]


def _balanced_permuted_column(levels: List[Any], n: int, rng: random.Random) -> List[Any]:
    """A length-n column: each level repeated n/|levels| times, then shuffled.

    Falls back to a near-balanced multiset (remainder spread) when |levels|
    does not divide n, so the construction never crashes on odd n.
    """
    q, r = divmod(n, len(levels))
    column = [lvl for lvl in levels for _ in range(q)]
    column += [levels[i % len(levels)] for i in range(r)]
    rng.shuffle(column)
    return column


@dataclass
class FractionalDesign:
    name: str
    seed: int
    n_cells: int
    cells: List[Dict[str, Any]] = field(default_factory=list)

    def _pairwise_imbalance(self) -> float:
        """Max abs deviation of any two-factor joint cell count from uniform.

        0.0 would mean the fraction is orthogonal on every factor pair; larger
        values quantify the residual confounding the design accepts.
        """
        worst = 0.0
        factor_names = list(FACTORS)
        for a, b in itertools.combinations(factor_names, 2):
            la, lb = len(FACTORS[a]), len(FACTORS[b])
            expected = self.n_cells / (la * lb)
            counts: Dict[Any, int] = {}
            for cell in self.cells:
                key = (cell[a], cell[b])
                counts[key] = counts.get(key, 0) + 1
            # include structurally-absent combinations as count 0
            observed_max_dev = max(
                [abs(counts.get((va, vb), 0) - expected)
                 for va in FACTORS[a] for vb in FACTORS[b]]
            )
            worst = max(worst, observed_max_dev)
        return round(worst, 4)

    def confounding_report(self) -> Dict[str, Any]:
        return {
            "design": self.name,
            "seed": self.seed,
            "n_cells": self.n_cells,
            "primary_factors_balanced": list(PRIMARY_FACTORS),
            "confounded_factors": list(CONFOUNDED_FACTORS),
            "aliasing_note": (
                "Main effects of all factors are held balanced; all "
                "higher-order interactions (incl. stakes x uncertainty, which "
                "cannot divide n=60 evenly) are aliased and NOT estimable from "
                "this fraction."
            ),
            "max_pairwise_imbalance": self._pairwise_imbalance(),
        }


def fractional_design(n_cells: int = 60, seed: int = 0) -> FractionalDesign:
    """Screen the full grid to a balanced <= ~60-cell fractional design."""
    design = FractionalDesign(
        name=f"CRUX-frac-{n_cells}c-seed{seed}",
        seed=seed,
        n_cells=n_cells,
    )
    columns = {}
    for idx, (factor, levels) in enumerate(FACTORS.items()):
        # process-stable per-factor seed (no salted built-in hash)
        rng = random.Random(seed * 1000 + idx)
        columns[factor] = _balanced_permuted_column(levels, n_cells, rng)
    design.cells = [
        {factor: columns[factor][r] for factor in FACTORS}
        for r in range(n_cells)
    ]
    return design
