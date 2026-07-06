"""stats_util.py — tiny dependency-free, DETERMINISTIC stats for the WITNESS analysis.

Deterministic bootstrap (hash-seeded LCG) so reports are byte-reproducible. No numpy
dependency assumed. Rank correlations for the anisotropy prediction test.
"""
from __future__ import annotations

import hashlib
import math
from typing import Sequence


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
    means.sort()
    lo = means[int((alpha / 2) * iters)]
    hi = means[min(iters - 1, int((1 - alpha / 2) * iters))]
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
