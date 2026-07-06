"""Small statistical helpers shared by the P0 gates.

Kept dependency-light: `statistics` (stdlib) for means/SD/CV, and scipy's Welch
t-test for pairwise separation (scipy is in the vault venv). The one thing we add
on top of scipy is explicit zero-variance handling so degenerate (dead) cells give a
well-defined p-value instead of NaN.
"""
from __future__ import annotations

import math
import statistics
from typing import Iterable, List, Optional, Sequence

from scipy import stats as _scipy_stats


def mean(values: Sequence[float]) -> float:
    return statistics.fmean(values)


def sample_sd(values: Sequence[float]) -> float:
    """Sample standard deviation (n-1). Returns 0.0 for <2 points."""
    vals = list(values)
    if len(vals) < 2:
        return 0.0
    return statistics.stdev(vals)


def coefficient_of_variation(
    values: Iterable[float], epsilon: float = 1e-6
) -> Optional[float]:
    """Cross-unit CV = SD / |mean|, with a non-degenerate-denominator guard (§4).

    Returns None (NOT a huge number off a near-zero denominator) when:
      - fewer than 2 values, or
      - |mean| <= epsilon  (the "93x off a near-zero denominator" trap doc 04 §4 warns about).
    """
    vals = [v for v in values if v is not None]
    if len(vals) < 2:
        return None
    m = mean(vals)
    if abs(m) <= epsilon:
        return None
    return sample_sd(vals) / abs(m)


def welch_p(a: Sequence[float], b: Sequence[float]) -> float:
    """Two-sided Welch's t-test p-value with explicit zero-variance handling.

    A pair whose two samples are constant (dead cells) would make scipy return NaN;
    we resolve it deterministically: equal constants -> p=1.0 (not separable),
    different constants -> p=0.0 (trivially separable). Samples too small to test
    return p=1.0 (treated as "not separated").
    """
    xa = [float(x) for x in a]
    xb = [float(x) for x in b]
    if len(xa) < 2 or len(xb) < 2:
        return 1.0
    va = statistics.pvariance(xa)
    vb = statistics.pvariance(xb)
    if va == 0.0 and vb == 0.0:
        return 0.0 if mean(xa) != mean(xb) else 1.0
    res = _scipy_stats.ttest_ind(xa, xb, equal_var=False)
    p = float(res.pvalue)
    if math.isnan(p):
        return 1.0
    return p


def sign(x: float, tol: float = 0.0) -> int:
    """Sign of x with a tolerance dead-band: +1, -1, or 0."""
    if x > tol:
        return 1
    if x < -tol:
        return -1
    return 0
