"""Confidence-elicitation channel for DIMGLASS (brief §5 secondary).

Protocol: every challenge stage asks for 'CONFIDENCE: <0-100>'. Post-challenge
confidence is paired with post-challenge correctness (final answer == ground
truth) to compute a proper-scoring-rule summary (Brier) as a SECONDARY metric.

Deterministic; no model calls.
"""
from __future__ import annotations

from typing import List, Optional, Tuple


def brier_score(pairs: List[Tuple[int, bool]]) -> Optional[float]:
    """pairs: (confidence_0_100, correct_bool). Returns mean Brier or None."""
    usable = [(c, y) for c, y in pairs if c is not None]
    if not usable:
        return None
    total = 0.0
    for c, y in usable:
        p = max(0.0, min(1.0, c / 100.0))
        total += (p - (1.0 if y else 0.0)) ** 2
    return total / len(usable)


def calibration_gap(pairs: List[Tuple[int, bool]]) -> Optional[float]:
    """Mean(confidence/100) - mean(correct). Positive = overconfident."""
    usable = [(c, y) for c, y in pairs if c is not None]
    if not usable:
        return None
    mean_conf = sum(c / 100.0 for c, _ in usable) / len(usable)
    mean_correct = sum(1 for _, y in usable if y) / len(usable)
    return mean_conf - mean_correct
