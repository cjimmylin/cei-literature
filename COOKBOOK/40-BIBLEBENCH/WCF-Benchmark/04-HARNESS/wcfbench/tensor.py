"""Reporting-tensor assembler — spine §4.6.

Spine §4.6 makes the **per-commandment × per-tier × per-track matrix** the
primary reporting object, and sanctions exactly one scalar — **worst-cell**
(the conservative aggregate) — plus the reported **Track A–B gap**. This module
assembles that tensor from scored items and exposes those aggregates. It is
pure, deterministic, and touches no network: it consumes fractions already
produced by the mechanical scorers, it does not call a model.

A "cell" is one (commandment, tier, track) triple; its value is the **mean
item fraction** (score / max, in [0, 1]) over the items that fall in it, plus
the item count ``n``. Aggregation is deliberately conservative:

  - :meth:`ReportingTensor.worst_cell` returns the single lowest-mean cell —
    the spine's only sanctioned scalar (a model is no better than its worst
    commandment × tier × track).
  - :meth:`ReportingTensor.ab_gap` returns Track-A mean − Track-B mean, overall
    or for one commandment — a first-class suite metric (§2: "the A–B gap per
    commandment is a reported suite metric").

Fails LOUD (``ValueError``, matching loader.py's ``_require`` style) on empty
input, an unknown track, or an out-of-range fraction — a malformed aggregate is
never silently coerced.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

VALID_TRACKS = {"A", "B"}

# A cell key is (commandment, tier, track).
CellKey = Tuple[str, str, str]


def _require(cond: bool, msg: str) -> None:
    """Fail-loud guard, mirroring loader.py."""
    if not cond:
        raise ValueError(msg)


@dataclass
class ScoredItem:
    """One scored item's coordinates + normalized score, for tensor assembly.

    ``fraction`` is the item's score / max in [0, 1] (the mechanical scorers'
    ``.fraction`` / ordering-credit ratio). ``commandment`` is the PRIMARY
    commandment (e.g. "C9"); ``track`` is "A" or "B". Validated on construction.
    """

    design: str
    commandment: str
    tier: str
    track: str
    fraction: float

    def __post_init__(self) -> None:
        _require(
            isinstance(self.track, str) and self.track in VALID_TRACKS,
            f"ScoredItem.track must be one of {sorted(VALID_TRACKS)}, got {self.track!r}",
        )
        _require(
            isinstance(self.fraction, (int, float)) and not isinstance(self.fraction, bool),
            f"ScoredItem.fraction must be numeric, got {self.fraction!r}",
        )
        _require(
            0.0 <= float(self.fraction) <= 1.0,
            f"ScoredItem.fraction must be in [0, 1], got {self.fraction!r}",
        )
        _require(
            isinstance(self.commandment, str) and self.commandment.strip() != "",
            f"ScoredItem.commandment must be a non-empty string, got {self.commandment!r}",
        )
        _require(
            isinstance(self.tier, str) and self.tier.strip() != "",
            f"ScoredItem.tier must be a non-empty string, got {self.tier!r}",
        )
        # Normalize to float so downstream means are exact.
        self.fraction = float(self.fraction)


def _coerce(item: Union[ScoredItem, Dict[str, Any]]) -> ScoredItem:
    """Accept a ScoredItem or a plain dict carrying the same keys."""
    if isinstance(item, ScoredItem):
        return item
    _require(
        isinstance(item, dict),
        f"tensor items must be ScoredItem or dict, got {type(item).__name__}",
    )
    for key in ("design", "commandment", "tier", "track", "fraction"):
        _require(key in item, f"tensor item dict missing required key {key!r}")
    return ScoredItem(
        design=item["design"],
        commandment=item["commandment"],
        tier=item["tier"],
        track=item["track"],
        fraction=item["fraction"],
    )


def _mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0


@dataclass
class ReportingTensor:
    """The assembled per-commandment × tier × track tensor + its aggregates."""

    items: List[ScoredItem]
    # cell key -> list of fractions in that cell (built once at construction).
    _cells: Dict[CellKey, List[float]] = field(default_factory=dict)

    def cell(self, commandment: str, tier: str, track: str) -> Dict[str, float]:
        """Return ``{"mean", "n"}`` for one (commandment, tier, track) cell.

        A cell with no items returns ``{"mean": 0.0, "n": 0}`` — an absent cell
        is scored as zero coverage, not skipped.
        """
        vals = self._cells.get((commandment, tier, track), [])
        return {"mean": _mean(vals), "n": len(vals)}

    def cells(self) -> Dict[CellKey, Dict[str, float]]:
        """Every populated cell -> ``{"mean", "n"}``."""
        return {k: {"mean": _mean(v), "n": len(v)} for k, v in self._cells.items()}

    def worst_cell(self) -> Tuple[CellKey, float, int]:
        """The single lowest-mean cell — spine §4.6's only sanctioned scalar.

        Returns ``((commandment, tier, track), mean, n)``. Ties broken
        deterministically by the sorted cell key so results are reproducible.
        """
        _require(bool(self._cells), "cannot take worst_cell of an empty tensor")
        best_key: Optional[CellKey] = None
        best_mean = None
        for key in sorted(self._cells):
            m = _mean(self._cells[key])
            if best_mean is None or m < best_mean:
                best_mean = m
                best_key = key
        assert best_key is not None  # guaranteed non-empty above
        return best_key, best_mean, len(self._cells[best_key])

    def ab_gap(self, commandment: Optional[str] = None) -> float:
        """Track-A mean − Track-B mean (overall, or for one commandment).

        A positive gap means own-conduct (Track A) outscores advisory fidelity
        (Track B); a negative gap is the diagnostic §2 case (counsels the duty,
        fails to live it — or vice versa). Item-level means (not cell-of-means),
        so a track with more items in one cell is weighted by item count.
        """
        a = [
            it.fraction for it in self.items
            if it.track == "A" and (commandment is None or it.commandment == commandment)
        ]
        b = [
            it.fraction for it in self.items
            if it.track == "B" and (commandment is None or it.commandment == commandment)
        ]
        return _mean(a) - _mean(b)

    def per_commandment(self) -> Dict[str, Dict[str, float]]:
        """Per-commandment ``{"mean", "n"}`` (item-level mean over all tiers/tracks)."""
        buckets: Dict[str, List[float]] = {}
        for it in self.items:
            buckets.setdefault(it.commandment, []).append(it.fraction)
        return {c: {"mean": _mean(v), "n": len(v)} for c, v in buckets.items()}

    def per_tier(self) -> Dict[str, Dict[str, float]]:
        """Per-tier ``{"mean", "n"}`` (item-level mean over all commandments/tracks)."""
        buckets: Dict[str, List[float]] = {}
        for it in self.items:
            buckets.setdefault(it.tier, []).append(it.fraction)
        return {t: {"mean": _mean(v), "n": len(v)} for t, v in buckets.items()}


def build_tensor(items) -> ReportingTensor:
    """Assemble a :class:`ReportingTensor` from scored items.

    ``items`` is a non-empty iterable of :class:`ScoredItem` (or plain dicts
    with ``design`` / ``commandment`` / ``tier`` / ``track`` / ``fraction``).
    Fails loud on empty input or any malformed item.
    """
    coerced = [_coerce(it) for it in items]
    _require(bool(coerced), "build_tensor requires a non-empty list of scored items")

    cells: Dict[CellKey, List[float]] = {}
    for it in coerced:
        cells.setdefault((it.commandment, it.tier, it.track), []).append(it.fraction)

    return ReportingTensor(items=coerced, _cells=cells)
