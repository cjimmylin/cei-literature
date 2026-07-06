"""DUPLEX P0 gates G1/G2/G3 and the pre-registered ALL-THREE-must-hold combiner (§7).

Result-record schema consumed here (one dict per administration = one rep of one cell):

    {
      "item_id": str,
      "model_id": str,
      "vendor": str,                # anthropic | openai | google
      "axis": "process" | "content",
      "resource_condition": str,    # forced_immediate | standard | extended_thinking | load_injected | ...
      "seed": int,
      "rep": int,
      "score": float | None,        # judged/measured judgment; higher = more utilitarian (0..1 typical)
      "refusal": bool,              # refusals are EXCLUDED from every distribution here (§4)
    }

The gates never mutate their input and only ever consume live, non-refusal, non-None scores.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Optional, Sequence

from .stats import coefficient_of_variation, mean, sample_sd, sign, welch_p


# --------------------------------------------------------------------------- helpers

def _live(results: Sequence[dict]) -> List[dict]:
    """Live cells only: not a refusal, score present (§4 dead-cell / refusal exclusion)."""
    return [
        r
        for r in results
        if not r.get("refusal") and r.get("score") is not None
    ]


def _group_scores(records: Sequence[dict], *keys):
    """Group scores by one or more record fields.

    Single key  -> scalar dict keys (look up with the bare value).
    Multiple keys -> tuple dict keys (look up with a tuple).
    """
    out = defaultdict(list)
    single = len(keys) == 1
    for r in records:
        k = r[keys[0]] if single else tuple(r[key] for key in keys)
        out[k].append(float(r["score"]))
    return out


# --------------------------------------------------------------------------- G1

def process_beats_content(
    results: Sequence[dict],
    epsilon: float = 0.02,
    sd_dead_threshold: float = 1e-6,
    high_condition: str = "extended_thinking",
    low_condition: str = "forced_immediate",
) -> dict:
    """G1 — Process beats content on discrimination (§7 table row G1).

    Process-axis cross-model CV (denominator-guarded, dead-cells excluded) must EXCEED the
    matched content-axis baseline CV on the same models.

    Per-model process signature = |mean(high_condition) - mean(low_condition)| pooled over
    process items. A (model, condition) cell whose across-reps SD is <= sd_dead_threshold is a
    DEAD cell (correct-answer signature, doc 04 §4); a model resting on a dead cell is dropped
    from the process CV BEFORE the CV is computed. CV itself is guarded: if the cross-model mean
    is within epsilon of zero (the "93x off a near-zero denominator" failure mode) it returns
    None and the gate FAILS.
    """
    live = _live(results)
    proc = [r for r in live if r.get("axis") == "process"]
    cont = [r for r in live if r.get("axis") == "content"]

    proc_cells = _group_scores(proc, "model_id", "resource_condition")

    process_signatures: Dict[str, float] = {}
    dead_cells: List[dict] = []
    models = sorted({r["model_id"] for r in proc})
    for model in models:
        hi = proc_cells.get((model, high_condition), [])
        lo = proc_cells.get((model, low_condition), [])
        if len(hi) < 2 or len(lo) < 2:
            # incomplete cell — cannot judge liveness; skip this model from the process CV
            continue
        hi_sd = sample_sd(hi)
        lo_sd = sample_sd(lo)
        dead = hi_sd <= sd_dead_threshold or lo_sd <= sd_dead_threshold
        if dead:
            dead_cells.append(
                {"model_id": model, "high_sd": hi_sd, "low_sd": lo_sd}
            )
            continue  # dropped BEFORE CV (§4)
        process_signatures[model] = abs(mean(hi) - mean(lo))

    # content-axis matched baseline: cross-model CV of per-model mean content score
    cont_by_model = _group_scores(cont, "model_id")
    content_means = {m: mean(s) for m, s in cont_by_model.items() if len(s) >= 1}

    process_cv = coefficient_of_variation(process_signatures.values(), epsilon=epsilon)
    content_cv = coefficient_of_variation(content_means.values(), epsilon=epsilon)

    passed = (
        process_cv is not None
        and content_cv is not None
        and process_cv > content_cv
    )
    return {
        "process_cv": process_cv,
        "content_cv": content_cv,
        "pass": bool(passed),
        "process_signatures": process_signatures,
        "content_means": content_means,
        "dead_cells": dead_cells,
        "n_models_process": len(process_signatures),
    }


# --------------------------------------------------------------------------- G2

def _frac_separated(models: Sequence[str], sep: Dict[tuple, bool]) -> float:
    pairs = list(combinations(models, 2))
    if not pairs:
        return 0.0
    hit = sum(1 for a, b in pairs if sep.get((a, b), sep.get((b, a), False)))
    return hit / len(pairs)


def _outlier_guard_ok(
    models: Sequence[str], sep: Dict[tuple, bool], threshold: float
) -> bool:
    """Reject a single one-vs-N split (§7 G2 / §1 one-vs-eight caveat).

    Drop the model that participates in the MOST separated pairs, then require the remaining
    models to still clear `threshold` among themselves. A genuine spread survives (remove one
    model, the rest still separate); an outlier-driven split collapses to ~0.
    """
    models = list(models)
    if len(models) < 3:
        return False
    def sep_count(m: str) -> int:
        return sum(
            1
            for other in models
            if other != m
            and sep.get((m, other), sep.get((other, m), False))
        )
    top = max(models, key=sep_count)
    remaining = [m for m in models if m != top]
    if len(remaining) < 2:
        return False
    return _frac_separated(remaining, sep) >= threshold


def pairwise_separation(
    results: Sequence[dict],
    alpha: float = 0.01,
    sep_threshold: float = 0.90,
) -> dict:
    """G2 — Real pairwise separation (§7 table row G2; KB04 §6.2).

    On >=1 resource manipulation, >=90% of model pairs must separate at p<alpha (Welch),
    AND the separation must survive the one-vs-N outlier guard. Passes if ANY single condition
    meets both bars.
    """
    live = _live(results)
    conditions = sorted({r["resource_condition"] for r in live})
    models = sorted({r["model_id"] for r in live})

    per_condition: Dict[str, dict] = {}
    for cond in conditions:
        recs = [r for r in live if r["resource_condition"] == cond]
        by_model = _group_scores(recs, "model_id")
        sep: Dict[tuple, bool] = {}
        pvals: Dict[str, float] = {}
        for a, b in combinations(models, 2):
            sa, sb = by_model.get(a, []), by_model.get(b, [])
            p = welch_p(sa, sb)
            separated = p < alpha
            sep[(a, b)] = separated
            pvals["%s|%s" % (a, b)] = p
        frac = _frac_separated(models, sep)
        guard = _outlier_guard_ok(models, sep, sep_threshold)
        per_condition[cond] = {
            "frac_separated": frac,
            "outlier_guard_ok": guard,
            "meets_bar": frac >= sep_threshold and guard,
            "pvalues": pvals,
        }

    # best = condition with the highest frac_separated
    if per_condition:
        best_cond = max(
            per_condition, key=lambda c: per_condition[c]["frac_separated"]
        )
        best = per_condition[best_cond]
    else:
        best_cond, best = None, {"frac_separated": 0.0, "pvalues": {}}

    passed = any(pc["meets_bar"] for pc in per_condition.values())
    return {
        "separation_matrix": best.get("pvalues", {}),
        "frac_separated": best.get("frac_separated", 0.0),
        "best_condition": best_cond,
        "per_condition": per_condition,
        "pass": bool(passed),
    }


# --------------------------------------------------------------------------- G3

def _agg_delta(
    records: Sequence[dict], hi: str, lo: str
) -> Optional[float]:
    by_cond = _group_scores(records, "resource_condition")
    hs, ls = by_cond.get(hi, []), by_cond.get(lo, [])
    if not hs or not ls:
        return None
    return mean(hs) - mean(ls)


def greene_direction(
    results: Sequence[dict],
    human_anchor: Optional[float] = None,
    fallback: str = "agent_patient_time_pressure",
    delib_condition: str = "extended_thinking",
    intuitive_condition: str = "forced_immediate",
    fallback_delib: str = "agent_patient",
    fallback_intuitive: str = "patient_agent",
    min_effect: float = 0.02,
) -> dict:
    """G3 — Replication direction (§7 table row G3; §5 M3 fallback).

    Does the Greene load / utilitarian-shift effect replicate IN DIRECTION on the novel items?
    Higher score = more utilitarian; classic human effect is deliberation -> more utilitarian
    (positive delta).

      - human_anchor given  -> pass iff sign(model delta) == sign(human_anchor) (anchored to the
        P0 human mini-norm, never hard-coded to the utilitarian-shift assumption).
      - human_anchor is None -> invoke the pre-registered M3 fallback: use the agent-patient +
        time-pressure manipulation set (or, if those conditions are absent, the default
        deliberation contrast) and pass iff a CLEAR direction exists (|delta| >= min_effect).
        pass_or_fallback == "fallback" flags that this is descriptive resource-sensitivity, not
        an anchored dual-process claim.
    """
    live = _live(results)

    if human_anchor is not None:
        delta = _agg_delta(live, delib_condition, intuitive_condition)
        if delta is None:
            return {
                "direction": 0,
                "delta": None,
                "pass": False,
                "pass_or_fallback": "anchored",
                "human_anchor": human_anchor,
                "reason": "missing deliberation contrast conditions",
            }
        d = sign(delta)
        passed = d != 0 and d == sign(human_anchor)
        return {
            "direction": d,
            "delta": delta,
            "pass": bool(passed),
            "pass_or_fallback": "anchored",
            "human_anchor": human_anchor,
        }

    # --- fallback (M3): agent-patient + time-pressure, else default contrast ---
    conds = {r["resource_condition"] for r in live}
    if fallback_delib in conds and fallback_intuitive in conds:
        delta = _agg_delta(live, fallback_delib, fallback_intuitive)
        used = "%s vs %s" % (fallback_delib, fallback_intuitive)
    else:
        delta = _agg_delta(live, delib_condition, intuitive_condition)
        used = "%s vs %s (fallback set absent)" % (delib_condition, intuitive_condition)

    if delta is None:
        return {
            "direction": 0,
            "delta": None,
            "pass": False,
            "pass_or_fallback": "fallback",
            "fallback": fallback,
            "used_contrast": used,
        }
    clear = abs(delta) >= min_effect
    return {
        "direction": sign(delta),
        "delta": delta,
        "pass": bool(clear),
        "pass_or_fallback": "fallback",
        "fallback": fallback,
        "used_contrast": used,
    }


# --------------------------------------------------------------------------- combiner

def run_p0_gates(results: Sequence[dict], config: Optional[dict] = None) -> dict:
    """Pre-registered P0 decision: ALL THREE gates must hold to PASS (§7 X1).

    `config` mirrors the `p0_gates:` block of config/p0-roster.yaml. Missing keys fall back to
    each gate's own defaults.
    """
    cfg = config or {}
    g1 = process_beats_content(
        results,
        epsilon=cfg.get("g1_epsilon", 0.02),
        sd_dead_threshold=cfg.get("g1_sd_dead_threshold", 1e-6),
        high_condition=cfg.get("g1_high_condition", "extended_thinking"),
        low_condition=cfg.get("g1_low_condition", "forced_immediate"),
    )
    g2 = pairwise_separation(
        results,
        alpha=cfg.get("g2_alpha", 0.01),
        sep_threshold=cfg.get("g2_sep_threshold", 0.90),
    )
    g3 = greene_direction(
        results,
        human_anchor=cfg.get("g3_human_anchor"),
        fallback=cfg.get("g3_fallback", "agent_patient_time_pressure"),
        delib_condition=cfg.get("g3_delib_condition", "extended_thinking"),
        intuitive_condition=cfg.get("g3_intuitive_condition", "forced_immediate"),
        min_effect=cfg.get("g3_min_effect", 0.02),
    )
    overall = bool(g1["pass"] and g2["pass"] and g3["pass"])
    return {"G1": g1, "G2": g2, "G3": g3, "overall_pass": overall}
