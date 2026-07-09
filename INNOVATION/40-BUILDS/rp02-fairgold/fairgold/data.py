"""Data model for fairgold.

An `Item` holds the *disaggregated* annotator judgments for one benchmark
question — the information that majority-gold benchmarks discard (RP-02
finding #0). A `Benchmark` is a collection of items. `Predictions` maps
model -> item_id -> answer, where an answer is either a single option
(point prediction) or a distribution over options.

Everything here is offline data structures + validation. No I/O beyond
optional JSON (de)serialization of already-stored dumps.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Optional, Sequence, Union

Answer = Union[str, Mapping[str, float]]

__all__ = ["Item", "Benchmark", "Predictions", "Answer"]


@dataclass
class Item:
    """One benchmark item with disaggregated annotator labels.

    Parameters
    ----------
    item_id : str
    options : the candidate answers/labels for this item.
    votes   : per-annotator single choice (each must be in options). May be
              empty if only rankings are supplied — in that case the top of
              each ranking is used as the vote.
    rankings: per-annotator full preference ordering (best-first), each a
              permutation of options. Required by Borda and by non-degenerate
              maximal-lottery scoring. None if unavailable.
    groups  : per-annotator group tag (aligned to `votes`), for optional
              group-stratified analysis. None if unavailable.
    """

    item_id: str
    options: Sequence[str]
    votes: Sequence[str] = field(default_factory=tuple)
    rankings: Optional[Sequence[Sequence[str]]] = None
    groups: Optional[Sequence[str]] = None

    def __post_init__(self) -> None:
        self.options = list(self.options)
        if len(self.options) == 0:
            raise ValueError(f"item {self.item_id}: no options")
        if len(set(self.options)) != len(self.options):
            raise ValueError(f"item {self.item_id}: duplicate options")
        opt_set = set(self.options)

        self.votes = list(self.votes)
        if not self.votes and self.rankings:
            # Derive point votes from the top of each ranking.
            self.votes = [list(r)[0] for r in self.rankings]
        for v in self.votes:
            if v not in opt_set:
                raise ValueError(f"item {self.item_id}: vote {v!r} not in options")

        if self.rankings is not None:
            self.rankings = [list(r) for r in self.rankings]
            for r in self.rankings:
                if set(r) != opt_set:
                    raise ValueError(
                        f"item {self.item_id}: ranking {r!r} is not a full "
                        f"ordering of options {self.options!r}"
                    )

        if self.groups is not None:
            self.groups = list(self.groups)
            if self.votes and len(self.groups) != len(self.votes):
                raise ValueError(
                    f"item {self.item_id}: groups length != votes length"
                )

        if not self.votes and self.rankings is None:
            raise ValueError(
                f"item {self.item_id}: needs votes or rankings (no labels)"
            )

    # -- derived views -----------------------------------------------------
    @property
    def num_annotators(self) -> int:
        if self.votes:
            return len(self.votes)
        return len(self.rankings) if self.rankings else 0

    def vote_counts(self) -> Counter:
        """Counter of point votes over options (zero-filled for all options)."""
        c = Counter({o: 0 for o in self.options})
        c.update(self.votes)
        return c

    def vote_distribution(self) -> Dict[str, float]:
        """Population label distribution over options (sums to 1)."""
        n = self.num_annotators
        counts = self.vote_counts()
        if n == 0:
            raise ValueError(f"item {self.item_id}: no annotators")
        return {o: counts[o] / n for o in self.options}

    def has_rankings(self) -> bool:
        return self.rankings is not None


@dataclass
class Benchmark:
    """An ordered collection of Items, indexed by item_id."""

    name: str
    items: List[Item] = field(default_factory=list)

    def __post_init__(self) -> None:
        seen = set()
        for it in self.items:
            if it.item_id in seen:
                raise ValueError(f"duplicate item_id {it.item_id}")
            seen.add(it.item_id)

    @property
    def item_ids(self) -> List[str]:
        return [it.item_id for it in self.items]

    def by_id(self) -> Dict[str, Item]:
        return {it.item_id: it for it in self.items}


class Predictions:
    """model_id -> {item_id -> Answer}. Answer is str (point) or dist (dict)."""

    def __init__(self, data: Optional[Mapping[str, Mapping[str, Answer]]] = None):
        self._data: Dict[str, Dict[str, Answer]] = {}
        if data:
            for model, preds in data.items():
                self._data[model] = dict(preds)

    def add(self, model: str, item_id: str, answer: Answer) -> None:
        self._data.setdefault(model, {})[item_id] = answer

    @property
    def models(self) -> List[str]:
        return list(self._data.keys())

    def for_model(self, model: str) -> Dict[str, Answer]:
        return self._data[model]

    def __contains__(self, model: str) -> bool:
        return model in self._data
