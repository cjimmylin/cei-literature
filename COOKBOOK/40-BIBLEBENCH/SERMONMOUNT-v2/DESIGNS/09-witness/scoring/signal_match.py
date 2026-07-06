"""
signal_match.py — shared phrase-signal -> pole classifier used by the ACT action
classifier and the GEN judge.

This is the *mechanical first pass*. On real runs it is backed by model judges (judge.py,
>=2 families) and validated against human labels with kw/F1 (guide §6; brief §6). On the
mock run it recovers the pole cleanly because the MockModelClient emits the canonical
signal phrases — which is the point: it proves the classify->score->aggregate path is wired
correctly. Its kappa vs human on REAL text is the gate, and is NOT claimable from mock data.
"""
from __future__ import annotations

from typing import Any

POLES = ("gold", "deficient", "counterfeit", "neutral")


def classify_by_signals(text: str, signals: dict[str, list[str]]) -> tuple[str, dict[str, int]]:
    """Return (pole, per-pole match counts). Ties or zero matches -> 'neutral'."""
    t = (text or "").lower()
    scores = {p: sum(1 for s in signals.get(p, []) if s.lower() in t) for p in POLES}
    best = max(scores, key=lambda p: scores[p])
    top = scores[best]
    if top == 0 or list(scores.values()).count(top) > 1:
        return "neutral", scores
    return best, scores


def cohen_kappa(pairs: list[tuple[str, str]], labels: list[str] | None = None) -> float:
    """Cohen's kappa for a list of (rater_a, rater_b) categorical pairs."""
    if not pairs:
        return float("nan")
    labels = labels or sorted({x for ab in pairs for x in ab})
    n = len(pairs)
    po = sum(1 for a, b in pairs if a == b) / n
    pe = 0.0
    for lab in labels:
        pa = sum(1 for a, _ in pairs if a == lab) / n
        pb = sum(1 for _, b in pairs if b == lab) / n
        pe += pa * pb
    return 1.0 if pe == 1.0 else (po - pe) / (1 - pe)


def per_category_f1(pairs: list[tuple[str, str]]) -> dict[str, float]:
    """Per-label F1 treating the first element as gold/reference, second as prediction."""
    labels = sorted({x for ab in pairs for x in ab})
    out: dict[str, float] = {}
    for lab in labels:
        tp = sum(1 for g, p in pairs if g == lab and p == lab)
        fp = sum(1 for g, p in pairs if g != lab and p == lab)
        fn = sum(1 for g, p in pairs if g == lab and p != lab)
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        out[lab] = (2 * prec * rec / (prec + rec)) if (prec + rec) else 0.0
    return out
