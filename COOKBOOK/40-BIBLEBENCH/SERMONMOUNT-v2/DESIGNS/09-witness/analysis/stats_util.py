"""stats_util.py — tiny dependency-free, DETERMINISTIC stats for the WITNESS analysis.

Deterministic bootstrap (hash-seeded LCG) so reports are byte-reproducible. No numpy
dependency assumed. Rank correlations for the anisotropy prediction test.
"""
from __future__ import annotations

import hashlib
import math
from typing import Iterable, Mapping, Sequence


class AnalysisError(ValueError):
    """Raised when an analysis input cannot support the preregistered estimator."""


def filter_non_holdout(
    rows: Iterable[Mapping], holdout_core_ids: Iterable[str] = (), *,
    require_status: bool = False,
) -> list[dict]:
    """Return copied, non-holdout rows before any downstream computation.

    ``holdout=True`` is the primary contract. ``holdout_core_ids`` is a defensive
    join for older score files that predate propagation of the row-level flag.
    Malformed flags fail closed instead of silently entering the science split.
    """
    blocked = set(holdout_core_ids)
    kept: list[dict] = []
    for source in rows:
        row = dict(source)
        if require_status and "holdout" not in row:
            raise AnalysisError(
                "holdout status is required before science-split analysis"
            )
        flag = row.get("holdout", False)
        if not isinstance(flag, bool):
            raise AnalysisError("holdout must be a boolean when present")
        if flag or row.get("core_id") in blocked:
            continue
        kept.append(row)
    return kept


def finite_number(value, *, field: str) -> float:
    """Coerce a numeric value and reject booleans' non-finite cousins."""
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if not isinstance(value, (int, float)):
        raise AnalysisError(f"{field} must be a finite numeric value")
    result = float(value)
    if not math.isfinite(result):
        raise AnalysisError(f"{field} must be finite")
    if result < 0.0 or result > 1.0:
        raise AnalysisError(f"{field} must be on the probability scale [0, 1]")
    return result


def percentile_interval(
    values: Sequence[float], alpha: float = 0.10
) -> tuple[float, float]:
    """Deterministic nearest-rank percentile interval."""
    values = sorted(values)
    if not values:
        raise AnalysisError("cannot form a percentile interval from no replicates")
    if not 0.0 < alpha < 1.0:
        raise AnalysisError("alpha must be strictly between 0 and 1")
    count = len(values)
    # Nearest-rank quantiles use one-based ranks ceil(p*n), converted back to
    # zero-based indices.  For B=2,000 and a 90% CI these are 99 and 1,899.
    lo_index = max(0, min(count - 1, math.ceil((alpha / 2.0) * count) - 1))
    hi_index = max(0, min(count - 1, math.ceil((1.0 - alpha / 2.0) * count) - 1))
    lo = values[lo_index]
    hi = values[hi_index]
    if not (math.isfinite(lo) and math.isfinite(hi)):
        raise AnalysisError("bootstrap produced a non-finite percentile")
    return lo, hi


def historical_percentile_interval(
    values: Sequence[float], alpha: float = 0.10
) -> tuple[float, float]:
    """Preserve the superseded 2026-07-06 zero-based percentile indexing."""
    values = sorted(values)
    if not values:
        raise AnalysisError("cannot form a historical interval from no replicates")
    if not 0.0 < alpha < 1.0:
        raise AnalysisError("alpha must be strictly between 0 and 1")
    count = len(values)
    lo = values[min(count - 1, int((alpha / 2.0) * count))]
    hi = values[min(count - 1, int((1.0 - alpha / 2.0) * count))]
    return lo, hi


def deterministic_uniforms(tag: str, payload: object = None):
    """Yield a reproducible pseudo-random stream namespaced by tag and payload."""
    digest = hashlib.sha256(f"{tag}|{payload!r}".encode()).hexdigest()
    return _lcg(int(digest[:8], 16))


def mean(xs: Sequence[float]) -> float:
    xs = list(xs)
    return sum(xs) / len(xs) if xs else float("nan")


def _lcg(seed: int):
    s = seed & 0x7FFFFFFF
    while True:
        s = (s * 1103515245 + 12345) & 0x7FFFFFFF
        yield s / 0x7FFFFFFF


def bootstrap_ci(xs: Sequence[float], iters: int = 2000, alpha: float = 0.10,
                 tag: str = "") -> tuple[float, float, float]:
    """Return (point mean, lo, hi) percentile CI. Deterministic in xs + tag."""
    xs = list(xs)
    if not xs:
        return (float("nan"), float("nan"), float("nan"))
    n = len(xs)
    seed = int(hashlib.sha256((tag + repr(xs)).encode()).hexdigest()[:8], 16)
    g = _lcg(seed)
    means = []
    for _ in range(iters):
        resample = [xs[int(next(g) * n) % n] for _ in range(n)]
        means.append(sum(resample) / n)
    lo, hi = historical_percentile_interval(means, alpha)
    return (mean(xs), lo, hi)


def pearson(xs: Sequence[float], ys: Sequence[float]) -> float:
    xs, ys = list(xs), list(ys)
    n = len(xs)
    if n < 2:
        return float("nan")
    mx, my = mean(xs), mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return num / (dx * dy) if dx > 0 and dy > 0 else float("nan")


def _ranks(xs: Sequence[float]) -> list[float]:
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman(xs: Sequence[float], ys: Sequence[float]) -> float:
    return pearson(_ranks(list(xs)), _ranks(list(ys)))
