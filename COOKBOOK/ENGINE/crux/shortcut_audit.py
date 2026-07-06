"""Portfolio-wide X2 shortcut/gaming audit (KB04 §6 item 5).

Two pre-registered go/no-go gates every CRUX-family design reuses:

1. **Lexical/length/word-averaging baseline** — a classifier that sees ONLY
   surface features (character length, word count, bag-of-words) must sit at
   chance. If it beats chance, the item labels leak through surface form and the
   generator is exploitable.
2. **10%-fine-tune probe** — fine-tuning a probe on 10% of items must NOT reach
   parity with the full model; parity means the template surface is learnable
   (exploitable). The fine-tuning itself needs training infrastructure, so the
   probe is an INTERFACE with an injectable trainer; the pass/fail rule lives
   here.

X2 passes iff lexical ~ chance AND probe below parity.

Only numpy is required (no sklearn) so the audit runs anywhere the vault venv
does. The lexical model is a nearest-centroid classifier over lexical features,
evaluated with deterministic strided k-fold CV.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import numpy as np

_TOKEN = re.compile(r"[a-z]+")


@dataclass
class LexicalResult:
    accuracy: float
    chance: float
    tolerance: float
    near_chance: bool


@dataclass
class ProbeResult:
    probe_accuracy: float
    full_model_accuracy: float
    parity_tolerance: float
    below_parity: bool


def chance_level(labels: List[Any]) -> float:
    """Majority-class baseline accuracy."""
    if not labels:
        return 0.0
    counts: Dict[Any, int] = {}
    for y in labels:
        counts[y] = counts.get(y, 0) + 1
    return max(counts.values()) / len(labels)


def _featurize(texts: List[str]) -> np.ndarray:
    vocab = sorted({t for text in texts for t in _TOKEN.findall(text.lower())})
    index = {w: i for i, w in enumerate(vocab)}
    rows = []
    for text in texts:
        toks = _TOKEN.findall(text.lower())
        bag = np.zeros(len(vocab), dtype=float)
        for t in toks:
            bag[index[t]] += 1.0
        rows.append(np.concatenate([[len(text), len(toks)], bag]))
    return np.asarray(rows, dtype=float)


def _nearest_centroid_predict(X_tr, y_tr, X_te):
    classes = sorted(set(y_tr))
    centroids = {c: X_tr[[i for i, y in enumerate(y_tr) if y == c]].mean(axis=0)
                 for c in classes}
    preds = []
    for x in X_te:
        # deterministic tie-break: classes are sorted, argmin picks the first
        dists = [np.linalg.norm(x - centroids[c]) for c in classes]
        preds.append(classes[int(np.argmin(dists))])
    return preds


def lexical_length_baseline(items: List[Dict[str, Any]], k: int = 5,
                            tolerance: float = 0.1) -> LexicalResult:
    texts = [it["text"] for it in items]
    labels = [it["label"] for it in items]
    X = _featurize(texts)
    n = len(items)
    k = max(2, min(k, n))
    correct = total = 0
    for fold in range(k):
        te_idx = [i for i in range(n) if i % k == fold]
        tr_idx = [i for i in range(n) if i % k != fold]
        if not te_idx or not tr_idx:
            continue
        y_tr = [labels[i] for i in tr_idx]
        if len(set(y_tr)) < 1:
            continue
        preds = _nearest_centroid_predict(X[tr_idx], y_tr, X[te_idx])
        for p, i in zip(preds, te_idx):
            correct += int(p == labels[i])
            total += 1
    accuracy = correct / total if total else 0.0
    chance = chance_level(labels)
    near_chance = accuracy <= chance + tolerance
    return LexicalResult(round(accuracy, 4), round(chance, 4), tolerance,
                         near_chance)


class FineTuneProbe:
    """10%-fine-tune probe. `trainer(items, fraction) -> probe_accuracy` is
    injected (real fine-tuning needs training infra — TODO). Below-parity is the
    pass condition."""

    def __init__(self, trainer: Optional[Callable[[List[Dict[str, Any]], float], float]] = None):
        self.trainer = trainer

    def run(self, items: List[Dict[str, Any]], full_model_accuracy: float,
            fraction: float = 0.10, parity_tolerance: float = 0.05) -> ProbeResult:
        if self.trainer is None:
            raise NotImplementedError(
                "FineTuneProbe needs a trainer callable that fine-tunes on "
                "`fraction` of items and returns held-out accuracy. TODO: wire "
                "a real fine-tune backend (e.g. a small LM + LoRA) at pilot P3."
            )
        probe_accuracy = float(self.trainer(items, fraction))
        below_parity = probe_accuracy < full_model_accuracy - parity_tolerance
        return ProbeResult(round(probe_accuracy, 4), full_model_accuracy,
                           parity_tolerance, below_parity)


def x2_gate(lexical: LexicalResult, probe: ProbeResult) -> Dict[str, Any]:
    """X2 passes iff the lexical baseline is ~ chance AND the probe is below
    parity."""
    reasons = []
    if not lexical.near_chance:
        reasons.append(
            f"lexical baseline {lexical.accuracy} beats chance {lexical.chance} "
            f"(+{lexical.tolerance}) => exploitable surface")
    if not probe.below_parity:
        reasons.append(
            f"fine-tune probe {probe.probe_accuracy} reaches parity with full "
            f"model {probe.full_model_accuracy} => learnable template")
    return {"pass": not reasons, "reasons": reasons}
