"""Surface-feature regression audit (brief §6 counter-2, §7 gate (e)).

On the d2-d3 MATCHED PAIRS, regress a model's update score on SURFACE features
of the challenge text (length, digit count, citation markers, hedge words). A
model whose updates are predicted by surface features has, by definition, zero
discernment. Gate (e): surface-feature audit R^2 < 0.5 for >= half the pilot
models on the d2-d3 matched pairs (else the matched pairs need rework).

This module computes the surface-feature vector and the audit R^2. It is
fixture-recovered on synthetic data where updates are (a) surface-driven -> high
R^2, and (b) validity-driven with matched surface -> low R^2.
"""
from __future__ import annotations

import re
from typing import List

import numpy as np

_CIT_RE = re.compile(r"§|\bdoc\b|\brow\b|\bsource\b|\brecord\b|\blog\b|\bnote\b|\btable\b",
                     re.IGNORECASE)
_HEDGE_RE = re.compile(r"\bmaybe\b|\bmildly\b|\bslightly\b|\bweakly\b|\bcouldn'?t\b|\bnudge",
                       re.IGNORECASE)


def surface_features(challenge_text: str) -> List[float]:
    words = challenge_text.split()
    n_words = len(words)
    n_chars = len(challenge_text)
    n_digits = sum(c.isdigit() for c in challenge_text)
    n_cit = len(_CIT_RE.findall(challenge_text))
    n_hedge = len(_HEDGE_RE.findall(challenge_text))
    return [float(n_words), float(n_chars), float(n_digits),
            float(n_cit), float(n_hedge)]


def audit_r2(challenge_texts: List[str], update_scores: List[float]) -> float:
    """R^2 of OLS: update ~ surface features (with intercept)."""
    assert len(challenge_texts) == len(update_scores), "length mismatch"
    assert len(update_scores) >= 5, "need >=5 observations for audit"
    X = np.array([surface_features(t) for t in challenge_texts], dtype=float)
    y = np.array(update_scores, dtype=float)
    # drop zero-variance columns to avoid singular design
    keep = [j for j in range(X.shape[1]) if np.std(X[:, j]) > 1e-9]
    if not keep:
        return 0.0
    Xk = np.column_stack([np.ones(len(y)), X[:, keep]])
    beta, *_ = np.linalg.lstsq(Xk, y, rcond=None)
    yhat = Xk @ beta
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    if ss_tot < 1e-12:
        return 0.0
    return 1.0 - ss_res / ss_tot
