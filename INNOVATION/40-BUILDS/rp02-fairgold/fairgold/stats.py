"""Numeric primitives for fairgold.

Pure-computation helpers used by the aggregation rules and the rescoring
engine: distribution distances, Shannon entropy, Kendall-tau rank
correlation, and the linear-program that returns a maximal lottery
(mixed equilibrium) of a pairwise-majority margin game.

All functions are dependency-light. Kendall-tau uses scipy.stats (tau-b,
tie-corrected). The maximal-lottery solver uses scipy.optimize.linprog.
Nothing here calls a model or touches the network.
"""
from __future__ import annotations

from typing import Dict, Mapping, Sequence, Tuple

import numpy as np
from scipy.optimize import linprog
from scipy.stats import kendalltau

__all__ = [
    "normalize",
    "shannon_entropy",
    "normalized_entropy",
    "total_variation",
    "jensen_shannon",
    "kendall_tau",
    "maximal_lottery",
]


def normalize(dist: Mapping[str, float]) -> Dict[str, float]:
    """Return a probability distribution (values summing to 1).

    Raises ValueError on negative mass or total mass <= 0.
    """
    total = 0.0
    for v in dist.values():
        if v < 0:
            raise ValueError("distribution has negative mass")
        total += v
    if total <= 0:
        raise ValueError("distribution has non-positive total mass")
    return {k: v / total for k, v in dist.items()}


def shannon_entropy(dist: Mapping[str, float], base: float = 2.0) -> float:
    """Shannon entropy of a distribution (auto-normalized)."""
    p = normalize(dist)
    h = 0.0
    for v in p.values():
        if v > 0:
            h -= v * (np.log(v) / np.log(base))
    return float(h)


def normalized_entropy(dist: Mapping[str, float]) -> float:
    """Entropy scaled to [0, 1] by log(#support-options).

    Returns 0.0 for a degenerate (single-option) distribution. Used as the
    contestedness / consensus statistic for item stratification.
    """
    support = [v for v in dist.values() if v > 0]
    k = len(support)
    if k <= 1:
        return 0.0
    return shannon_entropy(dist) / (np.log(k) / np.log(2.0))


def _aligned(p: Mapping[str, float], q: Mapping[str, float]) -> Tuple[np.ndarray, np.ndarray]:
    keys = sorted(set(p) | set(q))
    pv = np.array([p.get(k, 0.0) for k in keys], dtype=float)
    qv = np.array([q.get(k, 0.0) for k in keys], dtype=float)
    return pv, qv


def total_variation(p: Mapping[str, float], q: Mapping[str, float]) -> float:
    """Total-variation distance in [0, 1] between two distributions."""
    pv, qv = _aligned(normalize(p), normalize(q))
    return float(0.5 * np.abs(pv - qv).sum())


def jensen_shannon(p: Mapping[str, float], q: Mapping[str, float]) -> float:
    """Jensen-Shannon distance in [0, 1] (sqrt of base-2 JS divergence)."""
    pv, qv = _aligned(normalize(p), normalize(q))
    m = 0.5 * (pv + qv)

    def _kl(a: np.ndarray, b: np.ndarray) -> float:
        mask = a > 0
        return float(np.sum(a[mask] * (np.log2(a[mask]) - np.log2(b[mask]))))

    js_div = 0.5 * _kl(pv, m) + 0.5 * _kl(qv, m)
    js_div = max(js_div, 0.0)  # guard tiny negative float noise
    return float(np.sqrt(js_div))


def kendall_tau(order_a: Sequence[float], order_b: Sequence[float]) -> float:
    """Kendall tau-b between two score vectors (tie-corrected).

    Inputs are per-item scores for the same, fixed sequence of models.
    Returns tau in [-1, 1]; returns 1.0 for the degenerate <=1 model case.
    """
    if len(order_a) != len(order_b):
        raise ValueError("score vectors must be equal length")
    if len(order_a) <= 1:
        return 1.0
    tau, _ = kendalltau(order_a, order_b)
    if np.isnan(tau):
        # Happens when one vector is constant (all ties). By convention
        # treat as perfectly stable: no discordant information exists.
        return 1.0
    return float(tau)


def maximal_lottery(options: Sequence[str], margin: np.ndarray) -> Dict[str, float]:
    """Maximal lottery of a pairwise-majority margin game.

    `margin` is a skew-symmetric matrix M where M[i][j] = (#preferring
    option i over j) - (#preferring j over i). The maximal lottery is the
    mixed strategy p of the symmetric zero-sum game with payoff M; it is
    the randomized social-choice rule of Fishburn (1984) / Kreweras, and
    always exists with game value 0.

    Solved as the LP:  max v  s.t.  (p^T M)_j >= v for all j,  sum p = 1,
    p >= 0. Returns {option: probability}.
    """
    m = len(options)
    if m == 0:
        raise ValueError("no options")
    if m == 1:
        return {options[0]: 1.0}

    M = np.asarray(margin, dtype=float)
    if M.shape != (m, m):
        raise ValueError("margin matrix shape must match options")

    # Variables: x = [p_0, ..., p_{m-1}, v]. Minimize -v.
    c = np.zeros(m + 1)
    c[-1] = -1.0

    # For each pure column j:  v - sum_i p_i M[i][j] <= 0
    A_ub = np.zeros((m, m + 1))
    for j in range(m):
        for i in range(m):
            A_ub[j, i] = -M[i, j]
        A_ub[j, -1] = 1.0
    b_ub = np.zeros(m)

    # sum p = 1
    A_eq = np.zeros((1, m + 1))
    A_eq[0, :m] = 1.0
    b_eq = np.array([1.0])

    bounds = [(0.0, None)] * m + [(None, None)]  # p >= 0, v free

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(f"maximal-lottery LP failed: {res.message}")

    p = np.array(res.x[:m], dtype=float)
    p = np.clip(p, 0.0, None)
    s = p.sum()
    if s <= 0:
        raise RuntimeError("maximal-lottery LP returned degenerate solution")
    p = p / s
    return {opt: float(prob) for opt, prob in zip(options, p)}
