"""Cross-judge disagreement clusters — the payload a Fable session adjudicates.

The spine keeps ≥2 cross-family judges precisely so their DISAGREEMENT is signal,
not noise to average away. This module walks a :class:`~wcfbench.runner.RunReport`
and, for every panel-graded cell (OPEN triaxial or CONTESTED adherence), computes:

  - the per-axis **spread** across judges (``max − min`` of each axis's scores),
  - ``max_spread`` — the widest single-axis disagreement (the sort key),
  - ``split_defensible`` — (CONTESTED only) whether the judges split on whether the
    occupied position is a defensible Reformed view.

The cells are returned sorted **worst-first**, so a downstream Fable session reads
the highest-disagreement items at the top. Pure/deterministic; no network. This is
the input the boot prompt's Fable session adjudicates ("judge-disagreement clusters
+ judge-calibration go/no-go").
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .routing import OPEN, CONTESTED

# The axes we track disagreement on, by cell kind.
_OPEN_AXES = ("matter", "manner", "end")
_CONTESTED_AXES = ("disclosure", "coherence", "settled_core_fraction")


@dataclass
class DisagreementCell:
    """One (item, SUT) cell's cross-judge disagreement summary."""

    item_id: str
    model: str
    kind: str
    n_judges: int
    axis_spreads: Dict[str, float] = field(default_factory=dict)
    max_spread: float = 0.0
    split_defensible: bool = False
    judge_values: Dict[str, List[Optional[float]]] = field(default_factory=dict)
    detail: str = ""


def _spread(vals: List[Optional[float]]) -> Optional[float]:
    present = [v for v in vals if v is not None]
    if len(present) < 2:
        return 0.0 if present else None
    return max(present) - min(present)


def summarize_disagreement(report: Any) -> List[DisagreementCell]:
    """Return per-cell disagreement summaries for every panel-graded item in
    ``report``, sorted by ``max_spread`` descending (worst disagreement first).

    Mechanically-scored items (no ``judge_raw``) are skipped — there is no judge
    disagreement to summarize on them.
    """
    cells: List[DisagreementCell] = []
    for model, model_report in report.reports.items():
        for r in model_report.results:
            per_judge = getattr(r, "judge_raw", None)
            if not per_judge:
                continue
            axes = _OPEN_AXES if r.kind == OPEN else _CONTESTED_AXES if r.kind == CONTESTED else ()
            if not axes:
                continue
            spreads: Dict[str, float] = {}
            judge_values: Dict[str, List[Optional[float]]] = {}
            for axis in axes:
                vals = [j.get(axis) for j in per_judge]
                judge_values[axis] = vals
                sp = _spread(vals)
                if sp is not None:
                    spreads[axis] = sp
            max_spread = max(spreads.values()) if spreads else 0.0

            split_defensible = False
            if r.kind == CONTESTED:
                votes = [j.get("position_defensible") for j in per_judge]
                votes = [v for v in votes if v is not None]
                split_defensible = len(set(votes)) > 1

            cells.append(DisagreementCell(
                item_id=r.item_id, model=model, kind=r.kind, n_judges=len(per_judge),
                axis_spreads=spreads, max_spread=max_spread, split_defensible=split_defensible,
                judge_values=judge_values,
                detail=(f"{r.kind}: max axis spread {max_spread:.2f} across {len(per_judge)} judge(s)"
                        + ("; SPLIT on defensibility" if split_defensible else "")),
            ))
    # worst-first: a split on defensibility is a first-class disagreement, then spread.
    cells.sort(key=lambda c: (c.split_defensible, c.max_spread), reverse=True)
    return cells
