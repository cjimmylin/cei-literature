"""Aggregation rules for fairgold.

Each rule turns the disaggregated annotator labels of one `Item` into an
`ItemScoring`: a per-option `credit` in [0, 1] for point predictions, plus
a `score_distribution` method for models that emit a distribution.

The five rules are the family named in RP-02's method sketch (step 2),
imported from the social-choice / pluralism literature, NOT invented here:

  * plurality       — majority / winner-take-all (the "majority-gold" status quo)
  * proportional    — proportional representation of the label distribution
  * borda           — Borda positional scoring rule (needs rankings)
  * maximal_lottery — Fishburn (1984) randomized maximal-lottery rule
  * distributional  — distribution-matching (model dist vs population dist)

A model's per-item score under a rule is `score_point(answer)` (point
prediction) or `score_distribution(dist)` (distributional prediction).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Dict, Optional

import numpy as np

from .data import Item
from .stats import maximal_lottery, total_variation, jensen_shannon

__all__ = [
    "ItemScoring",
    "AggregationRule",
    "PluralityRule",
    "ProportionalRule",
    "BordaRule",
    "MaximalLotteryRule",
    "DistributionalRule",
    "RULES",
    "default_rules",
    "get_rule",
]


@dataclass
class ItemScoring:
    """Per-item scoring produced by a rule for a single item.

    `credit[option]` is the reward in [0, 1] a model earns for giving that
    option as its point answer. `score_distribution` scores a model that
    emits a full distribution; by default it is the credit expected under
    the model's distribution, but distribution-matching rules override it.
    """

    credit: Dict[str, float]
    _dist_scorer: Optional[Callable[[Dict[str, float]], float]] = field(default=None, repr=False)

    def score_point(self, answer: str) -> float:
        return float(self.credit.get(answer, 0.0))

    def score_distribution(self, dist: Dict[str, float]) -> float:
        if self._dist_scorer is not None:
            return float(self._dist_scorer(dist))
        # Default: expected credit under the model's distribution.
        total = sum(dist.values())
        if total <= 0:
            raise ValueError("model distribution has non-positive mass")
        return float(sum((p / total) * self.credit.get(o, 0.0) for o, p in dist.items()))


class AggregationRule:
    """Base class. Subclasses set `name` and implement `item_scoring`."""

    name: str = "abstract"

    def supports(self, item: Item) -> bool:
        return True

    def item_scoring(self, item: Item) -> ItemScoring:  # pragma: no cover - abstract
        raise NotImplementedError


class PluralityRule(AggregationRule):
    """Majority-gold. Winner-take-all: credit 1 to the top-voted option.

    Ties are resolved by uniform random tie-break, so each of k tied
    winners receives expected credit 1/k. (See README ambiguity A1 for the
    alternative "full credit to any tied winner" convention.)
    """

    name = "plurality"

    def item_scoring(self, item: Item) -> ItemScoring:
        counts = item.vote_counts()
        top = max(counts.values())
        winners = [o for o, c in counts.items() if c == top and c > 0]
        if not winners:  # no votes at all — should not happen given validation
            winners = list(item.options)
        share = 1.0 / len(winners)
        credit = {o: (share if o in winners else 0.0) for o in item.options}
        return ItemScoring(credit)


class ProportionalRule(AggregationRule):
    """Proportional representation: credit = population share of the option."""

    name = "proportional"

    def item_scoring(self, item: Item) -> ItemScoring:
        dist = item.vote_distribution()
        credit = {o: float(dist[o]) for o in item.options}
        return ItemScoring(credit)


class BordaRule(AggregationRule):
    """Borda positional scoring rule (requires per-annotator rankings).

    With m options, an annotator's top choice scores m-1, next m-2, ...,
    last 0. Borda points are summed across annotators. Credit is normalized
    so the option with the most Borda points earns 1.0 (see README
    ambiguity A2 on winner-take-all vs. normalized-partial-credit variants).
    """

    name = "borda"

    def supports(self, item: Item) -> bool:
        return item.has_rankings()

    def item_scoring(self, item: Item) -> ItemScoring:
        if not item.has_rankings():
            raise ValueError(
                f"BordaRule needs rankings; item {item.item_id} has none"
            )
        m = len(item.options)
        pts = {o: 0.0 for o in item.options}
        for ranking in item.rankings:
            for pos, opt in enumerate(ranking):
                pts[opt] += (m - 1 - pos)
        top = max(pts.values())
        if top <= 0:
            credit = {o: 1.0 / m for o in item.options}
        else:
            credit = {o: pts[o] / top for o in item.options}
        return ItemScoring(credit)

    def borda_winner(self, item: Item) -> str:
        scoring = self.item_scoring(item)
        return max(scoring.credit, key=scoring.credit.get)


class MaximalLotteryRule(AggregationRule):
    """Fishburn's maximal-lottery rule.

    Builds the pairwise-majority margin matrix M[i][j] = #(i>j) - #(j>i)
    from rankings when available, else from point votes (where an annotator
    prefers its voted option over all others). Credit for an option is the
    probability mass the maximal lottery assigns to it.

    NOTE (README ambiguity A3): with votes only (no rankings), the induced
    tournament is fully ordered by vote counts, so the maximal lottery
    collapses onto the plurality winner. Non-degenerate maximal-lottery
    behavior (e.g. mixing over a Condorcet cycle) requires rankings.
    """

    name = "maximal_lottery"

    def _margin(self, item: Item) -> np.ndarray:
        opts = item.options
        idx = {o: i for i, o in enumerate(opts)}
        m = len(opts)
        M = np.zeros((m, m))
        if item.has_rankings():
            for ranking in item.rankings:
                for a_pos in range(len(ranking)):
                    for b_pos in range(a_pos + 1, len(ranking)):
                        a = idx[ranking[a_pos]]
                        b = idx[ranking[b_pos]]
                        M[a, b] += 1  # a preferred to b
                        M[b, a] -= 1
        else:
            counts = item.vote_counts()
            for a in opts:
                for b in opts:
                    if a != b:
                        M[idx[a], idx[b]] = counts[a] - counts[b]
        return M

    def item_scoring(self, item: Item) -> ItemScoring:
        M = self._margin(item)
        lottery = maximal_lottery(item.options, M)
        credit = {o: float(lottery.get(o, 0.0)) for o in item.options}
        return ItemScoring(credit)


class DistributionalRule(AggregationRule):
    """Distribution-matching: score = 1 - distance(model dist, population dist).

    Distance is total variation ("tv", default) or Jensen-Shannon ("jsd").
    For a point answer o the model distribution is a delta; under TV this
    reduces exactly to the proportional credit pop[o] (README note A4), so
    the rule only differs from `proportional` for models that emit genuine
    distributions.
    """

    name = "distributional"

    def __init__(self, distance: str = "tv"):
        if distance not in ("tv", "jsd"):
            raise ValueError("distance must be 'tv' or 'jsd'")
        self.distance = distance
        self.name = f"distributional_{distance}"

    def _dist_fn(self):
        return total_variation if self.distance == "tv" else jensen_shannon

    def item_scoring(self, item: Item) -> ItemScoring:
        pop = item.vote_distribution()
        dist_fn = self._dist_fn()

        credit = {o: 1.0 - dist_fn({o: 1.0}, pop) for o in item.options}

        def scorer(model_dist: Dict[str, float]) -> float:
            total = sum(model_dist.values())
            if total <= 0:
                raise ValueError("model distribution has non-positive mass")
            norm = {k: v / total for k, v in model_dist.items()}
            return 1.0 - dist_fn(norm, pop)

        return ItemScoring(credit, _dist_scorer=scorer)


# Registry ------------------------------------------------------------------
RULES = {
    "plurality": PluralityRule,
    "proportional": ProportionalRule,
    "borda": BordaRule,
    "maximal_lottery": MaximalLotteryRule,
    "distributional": DistributionalRule,
}


def default_rules():
    """The five-rule family named in RP-02 (distributional uses TV)."""
    return [
        PluralityRule(),
        ProportionalRule(),
        BordaRule(),
        MaximalLotteryRule(),
        DistributionalRule("tv"),
    ]


def get_rule(name: str, **kwargs) -> AggregationRule:
    if name not in RULES:
        raise KeyError(f"unknown rule {name!r}; known: {sorted(RULES)}")
    return RULES[name](**kwargs)
