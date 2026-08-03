"""v4-A 2(d) — complete-case analysis upgrade + norming/reporting (spec §3, §4.2).

Complete-case (adjudicated BLK-5, spec §4.2): the judge-swap condition runs on
records scorable by BOTH judges; the published rate is complete-case retention
relative to judge-A-scored records, per design, alongside the raw judge-B
unparseable rate. Rule: retention below 0.85 VOIDS the design's judge-swap
check. Completion-excluded records (v4-A 2(b)) are SUT-side attrition and sit
outside both numerator and denominator, disclosed as counts.

Norming (spec §3, adjudicated ruling 20260731l §2(b) — descriptive layer ONLY):
  * Profile cells are LEAVE-ONE-OUT standardized: every model (panel member or
    future) is scored against the reference set EXCLUDING itself, removing
    self-inclusion bias (which attenuated probe cells by up to 2.42x).
  * Reference set = the 7 pinned reference models (spec §4.1) — stated once,
    binding everywhere; OpenRouter slugs are re-verified at stamp.
  * Frame fragility is disclosed structurally: leave-one-model-out sensitivity
    is published for EVERY cell, and the frame is recomputed inside every
    bootstrap draw so reported intervals include frame uncertainty.

This module is v4.0-line code (spec §5.1); pinned v3 components untouched.
"""
from __future__ import annotations

import math
import random
from typing import Any, Dict, List, Optional, Sequence

# spec §4.1 — the 7 pinned reference models (frontier + anchors, v3/probe
# lineage). Names as pinned in the spec; concrete OpenRouter slugs are
# re-verified at every stamp and launch, with drift recorded in the run tree.
REFERENCE_MODELS = (
    "gpt-5",
    "claude-sonnet-4.5",
    "gemini-2.5-pro",
    "deepseek-r1",
    "gpt-4.1-mini",
    "deepseek-chat",
    "mistral-small-3.2",
)

RETENTION_TARGET = 0.85  # spec §4.2: below this the judge-swap check is VOID


# --------------------------------------------------------------------------- #
# complete-case accounting (BLK-5 denominators)
# --------------------------------------------------------------------------- #
def complete_case_table(rows: Sequence[Dict[str, Any]]) -> Dict[str, dict]:
    """Per-design complete-case retention relative to judge-A-scored records.

    Row contract (one row per scored unit):
      design               str
      judge_a_ok           bool  — judge-A produced a usable verdict
      judge_b_ok           bool  — judge-B produced a usable (parsed) verdict
      completion_excluded  bool, optional — SUT-side exclusion (v4-A 2(b));
                           outside numerator AND denominator, counted apart.

    Returns per design: a_scored, complete (both judges), retention
    (complete / a_scored), raw_b_unparseable_rate (among judge-A-scored),
    excluded count, and void flag (retention < RETENTION_TARGET).
    """
    out: Dict[str, dict] = {}
    for r in rows:
        design = str(r.get("design", "??"))
        d = out.setdefault(design, {"a_scored": 0, "complete": 0, "excluded": 0})
        if r.get("completion_excluded"):
            d["excluded"] += 1
            continue
        if not r.get("judge_a_ok"):
            continue
        d["a_scored"] += 1
        if r.get("judge_b_ok"):
            d["complete"] += 1
    for d in out.values():
        n = d["a_scored"]
        d["retention"] = (d["complete"] / n) if n else None
        d["raw_b_unparseable_rate"] = ((n - d["complete"]) / n) if n else None
        d["void"] = (d["retention"] is not None and d["retention"] < RETENTION_TARGET)
    return out


# --------------------------------------------------------------------------- #
# leave-one-out standardization (spec §3)
# --------------------------------------------------------------------------- #
def _mean_sd(xs: Sequence[float]) -> tuple:
    n = len(xs)
    mean = sum(xs) / n
    if n < 2:
        return mean, None
    var = sum((x - mean) ** 2 for x in xs) / (n - 1)  # sample SD (ddof=1)
    return mean, math.sqrt(var)


def loo_frame(reference_scores: Dict[str, float], target: str) -> Optional[tuple]:
    """(mean, sd) of the reference set EXCLUDING the target model.

    A non-reference target is normed against the full reference set — that is
    what makes panel and non-panel cells commensurable (spec §3). None when the
    frame is degenerate (fewer than 2 models or zero variance).
    """
    xs = [v for m, v in reference_scores.items() if m != target]
    if len(xs) < 2:
        return None
    mean, sd = _mean_sd(xs)
    if not sd:
        return None
    return mean, sd


def loo_z(score: float, reference_scores: Dict[str, float], target: str) -> Optional[float]:
    frame = loo_frame(reference_scores, target)
    if frame is None:
        return None
    mean, sd = frame
    return (score - mean) / sd


def lomo_sensitivity(score: float, reference_scores: Dict[str, float],
                     target: str) -> Optional[float]:
    """Leave-one-MODEL-out sensitivity of a cell (spec §3: published for every
    cell): the maximum absolute change in the cell's z when any single
    reference model (other than the target, already excluded) is dropped from
    the frame. Probe context: d05 reference SD swung 5.30x, driven by
    deepseek-r1."""
    base = loo_z(score, reference_scores, target)
    if base is None:
        return None
    deltas: List[float] = []
    for drop in reference_scores:
        if drop == target:
            continue
        reduced = {m: v for m, v in reference_scores.items() if m != drop}
        z = loo_z(score, reduced, target)
        if z is not None:
            deltas.append(abs(z - base))
    return max(deltas) if deltas else None


def profile_table(scores_by_dimension: Dict[str, Dict[str, float]],
                  models: Optional[Sequence[str]] = None,
                  reference_models: Sequence[str] = REFERENCE_MODELS) -> Dict[str, dict]:
    """Descriptive profile cells: {dimension: {model: {score, z, lomo_sensitivity}}}.

    Shape statements built on this table are descriptive-only and
    frame-caveated (spec §3); this function computes numbers, never verdicts.
    """
    out: Dict[str, dict] = {}
    for dim, scores in scores_by_dimension.items():
        ref = {m: scores[m] for m in reference_models if m in scores}
        cells: Dict[str, dict] = {}
        for model in (models if models is not None else sorted(scores)):
            if model not in scores:
                continue
            x = scores[model]
            cells[model] = {
                "score": x,
                "z": loo_z(x, ref, model),
                "lomo_sensitivity": lomo_sensitivity(x, ref, model),
            }
        out[dim] = cells
    return out


# --------------------------------------------------------------------------- #
# bootstrap with the frame recomputed inside every draw (spec §3)
# --------------------------------------------------------------------------- #
def bootstrap_loo_interval(item_scores: Dict[str, Sequence[float]],
                           target: str,
                           n_boot: int = 2000,
                           seed: int = 0,
                           alpha: float = 0.05,
                           reference_models: Sequence[str] = REFERENCE_MODELS
                           ) -> Optional[dict]:
    """Percentile bootstrap interval for a model's leave-one-out z on one
    dimension, with the NORMING FRAME recomputed inside every draw so the
    interval includes frame uncertainty (spec §3).

    `item_scores` maps model -> per-item scores on aligned items (paired
    resampling: one item index draw is applied to every model). Deterministic
    under a fixed seed.
    """
    if target not in item_scores:
        return None
    lengths = {len(v) for v in item_scores.values()}
    if len(lengths) != 1:
        raise ValueError("item_scores must be aligned across models (paired items)")
    n_items = lengths.pop()
    if n_items == 0:
        return None
    rng = random.Random(seed)
    zs: List[float] = []
    for _ in range(n_boot):
        idx = [rng.randrange(n_items) for _ in range(n_items)]
        means = {m: sum(v[i] for i in idx) / n_items for m, v in item_scores.items()}
        ref = {m: means[m] for m in reference_models if m in means}
        z = loo_z(means[target], ref, target)
        if z is not None:
            zs.append(z)
    if not zs:
        return None
    zs.sort()
    lo = zs[int((alpha / 2) * len(zs))]
    hi = zs[min(len(zs) - 1, int((1 - alpha / 2) * len(zs)))]
    point = loo_z(sum(item_scores[target]) / n_items,
                  {m: sum(v) / n_items for m, v in item_scores.items()
                   if m in reference_models}, target)
    return {"z": point, "ci_low": lo, "ci_high": hi,
            "n_boot_effective": len(zs), "n_items": n_items, "seed": seed}
