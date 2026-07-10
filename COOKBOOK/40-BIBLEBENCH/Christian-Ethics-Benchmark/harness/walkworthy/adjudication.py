"""Adjudicated-category derivation (PR-3 ruling R3 + gate-memo §B adjudication rule).

The §4 primary metrics and every reported gate statistic consume ADJUDICATED cells,
never a `verdicts[0]`-only value (PR-3 R3). This module is the single source of truth
for turning two cross-family judge verdicts into one adjudicated value per cell:

  - both judges agree (within the pre-registered disagreement tolerance) -> the value;
  - they disagree -> `None` (the cell is EXCLUDED and counted, resolved later via the
    third-family tie-breaker or the human Part-B label, protocol §6);
  - a judge defect (a `None` score from an unparseable/out-of-range verdict) -> `None`,
    EXCLUDED as a defect (never a defaulted 0.5 — PR-3 R3 point 3).

Near-agreement on an ordinal/int scale (values within tolerance but not identical, e.g.
0 vs 0.5 on a 0/0.5/1 criterion) combines the two AGREEING judges by their mean. That is
agreement *within the tolerance the disagreement flag already treats as agreement* — it is
NOT the forbidden cross-disagreement mean (charter §6.5). The exact combination rule for
near-agreement is flagged for ratification as PENDING-RULINGS PR-6 (build-level default).
"""
from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from .judges import _disagree
from .rubrics import BIN, CAT, Category

AGREED = "agreed"
EXCLUDED_DISAGREEMENT = "excluded_disagreement"
EXCLUDED_DEFECT = "excluded_defect"


def adjudicated_value(category: Category, a, b) -> Tuple[Optional[object], str]:
    """Return (adjudicated_value, status) for one category cell across two judges."""
    if a is None or b is None:
        return None, EXCLUDED_DEFECT
    if _disagree(category, a, b):
        return None, EXCLUDED_DISAGREEMENT
    if category.scale in (CAT, BIN):
        return a, AGREED
    if a == b:
        return a, AGREED
    # numeric agreement within tolerance but not identical -> combine the two agreeing judges
    return (float(a) + float(b)) / 2.0, AGREED


def adjudicate_scores(categories: List[Category], scores_a: dict,
                      scores_b: dict) -> Dict[str, Tuple[Optional[object], str]]:
    """Adjudicate every category in `categories` from two score dicts."""
    out: Dict[str, Tuple[Optional[object], str]] = {}
    for c in categories:
        out[c.name] = adjudicated_value(c, scores_a.get(c.name), scores_b.get(c.name))
    return out
