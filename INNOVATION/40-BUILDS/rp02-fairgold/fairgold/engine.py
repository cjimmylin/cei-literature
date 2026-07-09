"""Rescoring engine for fairgold.

Given a `Benchmark` (items carrying disaggregated labels) and stored
`Predictions` for several models, the engine scores every model under each
aggregation rule, ranks the models, and quantifies how much the ranking
moves across rules (Kendall-tau) — the aggregation-sensitivity statistic
RP-02 proposes as a benchmark validity measure (H1). It also stratifies
items by contestedness so instability can be localized (H2).

This engine performs pure computation over already-stored predictions. It
does NOT call models and does NOT itself decide whether a benchmark is
invariant — it emits the numbers a study (RP-02 O4) would interpret.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Dict, List, Optional, Sequence, Tuple

from .data import Answer, Benchmark, Item, Predictions
from .rules import AggregationRule, ItemScoring
from .stats import kendall_tau, normalized_entropy

__all__ = ["RescoringEngine", "ModelScore", "StabilityReport"]


@dataclass
class ModelScore:
    model: str
    score: float
    n_items: int


@dataclass
class StabilityReport:
    rule_names: List[str]
    # model -> rule_name -> mean score
    scores: Dict[str, Dict[str, float]]
    # (rule_a, rule_b) -> kendall tau over the model score vectors
    pairwise_tau: Dict[Tuple[str, str], float]
    min_tau: float
    mean_tau: float


def _score_answer(scoring: ItemScoring, answer: Answer) -> float:
    if isinstance(answer, str):
        return scoring.score_point(answer)
    if isinstance(answer, dict):
        return scoring.score_distribution(answer)
    raise TypeError(f"answer must be str or dict, got {type(answer)!r}")


class RescoringEngine:
    def __init__(self, benchmark: Benchmark):
        self.benchmark = benchmark
        self._by_id = benchmark.by_id()

    # -- scoring -----------------------------------------------------------
    def score_model(
        self,
        model_preds: Dict[str, Answer],
        rule: AggregationRule,
        item_ids: Optional[Sequence[str]] = None,
        skip_missing: bool = False,
    ) -> ModelScore:
        """Mean per-item score for one model under one rule.

        By default every scored item must have a prediction; set
        `skip_missing=True` to score only the items the model answered
        (this changes the denominator — see README ambiguity A5).
        """
        ids = list(item_ids) if item_ids is not None else self.benchmark.item_ids
        applicable = [i for i in ids if rule.supports(self._by_id[i])]
        total = 0.0
        n = 0
        for iid in applicable:
            item = self._by_id[iid]
            if iid not in model_preds:
                if skip_missing:
                    continue
                raise KeyError(
                    f"model missing prediction for item {iid} "
                    f"(use skip_missing=True to ignore)"
                )
            scoring = rule.item_scoring(item)
            total += _score_answer(scoring, model_preds[iid])
            n += 1
        mean = total / n if n else 0.0
        return ModelScore(model="", score=mean, n_items=n)

    def score_all(
        self,
        predictions: Predictions,
        rule: AggregationRule,
        item_ids: Optional[Sequence[str]] = None,
        skip_missing: bool = False,
    ) -> Dict[str, ModelScore]:
        out: Dict[str, ModelScore] = {}
        for model in predictions.models:
            ms = self.score_model(
                predictions.for_model(model), rule, item_ids, skip_missing
            )
            out[model] = ModelScore(model=model, score=ms.score, n_items=ms.n_items)
        return out

    # -- ranking -----------------------------------------------------------
    @staticmethod
    def rank_models(scores: Dict[str, ModelScore]) -> List[Tuple[str, int]]:
        """Return [(model, rank)] with rank 1 = highest score (ties share min rank)."""
        ordered = sorted(scores.items(), key=lambda kv: kv[1].score, reverse=True)
        ranks: List[Tuple[str, int]] = []
        prev_score = None
        prev_rank = 0
        for i, (model, ms) in enumerate(ordered, start=1):
            if prev_score is not None and abs(ms.score - prev_score) < 1e-12:
                rank = prev_rank
            else:
                rank = i
                prev_rank = i
                prev_score = ms.score
            ranks.append((model, rank))
        return ranks

    # -- aggregation-sensitivity ------------------------------------------
    def stability(
        self,
        predictions: Predictions,
        rules: Sequence[AggregationRule],
        item_ids: Optional[Sequence[str]] = None,
        skip_missing: bool = False,
    ) -> StabilityReport:
        """Score all models under each rule and report Kendall-tau across rule pairs."""
        models = predictions.models
        rule_names = [r.name for r in rules]
        scores: Dict[str, Dict[str, float]] = {m: {} for m in models}
        # rule_name -> score vector aligned to `models`
        vecs: Dict[str, List[float]] = {}
        for rule in rules:
            res = self.score_all(predictions, rule, item_ids, skip_missing)
            vecs[rule.name] = [res[m].score for m in models]
            for m in models:
                scores[m][rule.name] = res[m].score

        pairwise: Dict[Tuple[str, str], float] = {}
        taus: List[float] = []
        for a, b in combinations(rule_names, 2):
            tau = kendall_tau(vecs[a], vecs[b])
            pairwise[(a, b)] = tau
            taus.append(tau)

        min_tau = min(taus) if taus else 1.0
        mean_tau = sum(taus) / len(taus) if taus else 1.0
        return StabilityReport(rule_names, scores, pairwise, min_tau, mean_tau)

    # -- stratification (H2) ----------------------------------------------
    def consensus_score(self, item: Item) -> float:
        """1 - normalized vote entropy. 1.0 = unanimous, 0.0 = maximally split."""
        return 1.0 - normalized_entropy(item.vote_distribution())

    def stratify(
        self,
        thresholds: Sequence[float] = (0.5,),
        labels: Optional[Sequence[str]] = None,
    ) -> Dict[str, List[str]]:
        """Partition item_ids into contestedness tiers by consensus score.

        `thresholds` are ascending consensus cut-points. With the default
        (0.5,) items split into 'contested' (consensus < 0.5) and
        'consensus' (>= 0.5). Provide finer thresholds for CRUX-style tiers.
        """
        cuts = list(thresholds)
        if labels is None:
            if len(cuts) == 1:
                labels = ["contested", "consensus"]
            else:
                labels = [f"tier_{i}" for i in range(len(cuts) + 1)]
        if len(labels) != len(cuts) + 1:
            raise ValueError("labels must have len(thresholds)+1 entries")

        buckets: Dict[str, List[str]] = {lab: [] for lab in labels}
        for item in self.benchmark.items:
            cs = self.consensus_score(item)
            band = 0
            for c in cuts:
                if cs >= c:
                    band += 1
            buckets[labels[band]].append(item.item_id)
        return buckets

    def stability_by_stratum(
        self,
        predictions: Predictions,
        rules: Sequence[AggregationRule],
        thresholds: Sequence[float] = (0.5,),
        labels: Optional[Sequence[str]] = None,
        skip_missing: bool = False,
    ) -> Dict[str, StabilityReport]:
        """Aggregation-sensitivity computed within each contestedness stratum."""
        strata = self.stratify(thresholds, labels)
        out: Dict[str, StabilityReport] = {}
        for stratum, ids in strata.items():
            if not ids:
                continue
            out[stratum] = self.stability(predictions, rules, ids, skip_missing)
        return out
