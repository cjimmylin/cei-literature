"""Naive / null baselines — mandatory P0 reporting (adjudication protocol §5.6; WS-1 D12).

'Naive baselines: majority-class, all-neutral, no-process-shift null (the load-bearing null).'

These are the degenerate reference datasets the real gates must BEAT: each is built by transforming
the observed scores so that the phenomenon a gate detects is, by construction, absent. Reporting
that the gates FAIL on each null demonstrates that an observed pass is not an artifact of the
scale, the item mix, or noise. They are report outputs co-reported with any P0 outcome, never a
gate themselves.
"""
from __future__ import annotations

from collections import defaultdict
from statistics import fmean
from typing import Dict, List, Sequence

from .gates import pairwise_separation, process_beats_content


def _scored(results: Sequence[dict]) -> List[dict]:
    return [r for r in results if not r.get("refusal") and r.get("score") is not None]


def _with_scores(results: Sequence[dict], fn) -> List[dict]:
    return [dict(r, score=fn(r)) for r in _scored(results)]


def no_process_shift_null(results: Sequence[dict], **g1_kwargs) -> dict:
    """The LOAD-BEARING null: resource manipulation produces zero stance shift. Every cell of a
    given (model, item) is set to that (model, item)'s GRAND MEAN across all conditions, so every
    per-item condition-delta is exactly 0 -> G1's process signature collapses -> G1 must NOT pass
    on the null (regardless of which resource conditions an item happens to carry)."""
    grand: Dict[tuple, List[float]] = defaultdict(list)
    for r in _scored(results):
        grand[(r["model_id"], r["item_id"])].append(float(r["score"]))
    grand_mean = {k: fmean(v) for k, v in grand.items()}

    def fn(r):
        return grand_mean[(r["model_id"], r["item_id"])]

    g1 = process_beats_content(_with_scores(results, fn), **g1_kwargs)
    return {
        "description": "resource conditions == standard (zero process shift)",
        "g1_process_cv": g1["process_cv"],
        "g1_pass": g1["pass"],
        "beaten_by_observed": not g1["pass"],
    }


def majority_class_null(results: Sequence[dict], alpha: float = 0.01,
                        sep_threshold: float = 0.90) -> dict:
    """Every response is the per-item modal stance (rounded), identical across models -> models do
    not separate -> G2 must NOT pass on the null."""
    by_item: Dict[str, List[float]] = defaultdict(list)
    for r in _scored(results):
        by_item[r["item_id"]].append(float(r["score"]))
    modal = {it: round(fmean(v)) for it, v in by_item.items()}  # modal ~ rounded central stance

    def fn(r):
        return float(modal.get(r["item_id"], round(float(r["score"]))))

    g2 = pairwise_separation(_with_scores(results, fn), alpha=alpha, sep_threshold=sep_threshold)
    return {
        "description": "every model predicts the per-item modal stance (no cross-model variance)",
        "g2_frac_separated": g2["frac_separated"],
        "g2_pass": g2["pass"],
        "beaten_by_observed": not g2["pass"],
    }


def all_neutral_null(results: Sequence[dict], neutral_value: float = 3.0,
                     alpha: float = 0.01, sep_threshold: float = 0.90) -> dict:
    """Every response is the scale-midpoint neutral stance -> zero variance everywhere -> no
    separation (G2) and no process signature (G1) -> the null must NOT pass either gate."""
    nulled = _with_scores(results, lambda r: float(neutral_value))
    g1 = process_beats_content(nulled)
    g2 = pairwise_separation(nulled, alpha=alpha, sep_threshold=sep_threshold)
    return {
        "description": f"every response == neutral midpoint ({neutral_value})",
        "g1_pass": g1["pass"],
        "g2_pass": g2["pass"],
        "beaten_by_observed": not (g1["pass"] or g2["pass"]),
    }


def null_baselines(results: Sequence[dict], **kwargs) -> dict:
    """All three mandatory naive baselines (§5.6), co-reported with the gate verdicts."""
    return {
        "no_process_shift": no_process_shift_null(results),
        "majority_class": majority_class_null(results),
        "all_neutral": all_neutral_null(results),
    }
