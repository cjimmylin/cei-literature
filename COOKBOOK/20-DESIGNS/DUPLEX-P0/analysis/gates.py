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

def _cell_state(
    scores: Sequence[float],
    condition: str,
    sd_dead_threshold: float,
    unmeasurable_conditions: set,
) -> str:
    """Three-state cell coding (ruling G1-b / V-4): 'live' | 'dead' | 'unmeasurable' |
    'incomplete'. A cell with < 2 reps is 'incomplete' (cannot judge liveness). A cell with
    across-reps SD > threshold is 'live'. A near-constant cell is 'unmeasurable' (config
    determinism) if its condition ran under a V-4 temperature drop, else 'dead' (content-domain
    correct-answer signature)."""
    if len(scores) < 2:
        return "incomplete"
    if sample_sd(scores) > sd_dead_threshold:
        return "live"
    return "unmeasurable" if condition in unmeasurable_conditions else "dead"


def process_beats_content(
    results: Sequence[dict],
    epsilon: float = 0.02,
    sd_dead_threshold: float = 1e-6,
    high_condition: str = "extended_thinking",
    low_condition: str = "forced_immediate",
    standard_condition: str = "standard",
    live_cell_floor: float = 0.40,
    unmeasurable_conditions: Optional[set] = None,
) -> dict:
    """G1 — Process beats content on discrimination (§7 row G1; rulings G1-a / G1-b).

    Ruling G1-a redefines the two axes over the SAME process items, same models, same run (no
    separate 'content' battery):

      * process axis  = cross-model CV of the per-model *process signature*, where the signature
        is the mean over items of the |per-item condition-delta| (mean(high) - mean(low) computed
        PER ITEM, abs applied per item so opposite-sign items do not cancel -- D5).
      * content baseline = cross-model CV of the per-model *content mean*, where the content mean
        is the mean over items of that item's mean stance in the STANDARD condition (D3) -- the
        model-to-model content disagreement. The discriminant-control battery is NOT this baseline.

    Cell coding is three-state (ruling G1-b / V-4): a live (item, model) process pair contributes
    a delta; a DEAD pair (a constant content cell) is excluded from the numerator but counts in
    the live-cell-fraction denominator; an UNMEASURABLE pair (constant because its condition ran
    under a V-4 temperature drop) counts in NEITHER. If the live fraction of process pairs falls
    below `live_cell_floor` (0.40), a numeric pass is downgraded to PROVISIONAL (thin base).

    CV is denominator-guarded: if the cross-model mean of the signatures is within epsilon of zero
    (the near-zero-denominator failure mode) it returns None and the gate FAILS. The process and
    content CVs are computed over the SAME model set (roster intersection -- D4).
    """
    unmeasurable_conditions = set(unmeasurable_conditions or ())
    proc = [r for r in _live(results) if r.get("axis") == "process"]

    # scores grouped by (model, item, condition) so liveness/deltas are per-item, not pooled
    cells: Dict[tuple, List[float]] = defaultdict(list)
    for r in proc:
        cells[(r["model_id"], r["item_id"], r["resource_condition"])].append(float(r["score"]))

    models = sorted({m for (m, _i, _c) in cells})
    items = sorted({i for (_m, i, _c) in cells})

    process_signatures: Dict[str, float] = {}
    dead_cells: List[dict] = []
    unmeasurable_cells: List[dict] = []
    live_pairs = 0
    dead_pairs = 0

    for model in models:
        per_item_abs_deltas: List[float] = []
        for item in items:
            hi = cells.get((model, item, high_condition))
            lo = cells.get((model, item, low_condition))
            if hi is None or lo is None:
                continue  # not a process pair for this (model, item)
            hs = _cell_state(hi, high_condition, sd_dead_threshold, unmeasurable_conditions)
            ls = _cell_state(lo, low_condition, sd_dead_threshold, unmeasurable_conditions)
            if hs == "incomplete" or ls == "incomplete":
                continue
            if hs == "unmeasurable" or ls == "unmeasurable":
                if hs == "unmeasurable":
                    unmeasurable_cells.append(
                        {"model_id": model, "item_id": item, "condition": high_condition,
                         "sd": sample_sd(hi)}
                    )
                if ls == "unmeasurable":
                    unmeasurable_cells.append(
                        {"model_id": model, "item_id": item, "condition": low_condition,
                         "sd": sample_sd(lo)}
                    )
                continue  # V-4: excluded from BOTH numerator and denominator
            if hs == "dead" or ls == "dead":
                dead_pairs += 1
                dead_cells.append(
                    {"model_id": model, "item_id": item,
                     "high_sd": sample_sd(hi), "low_sd": sample_sd(lo)}
                )
                continue  # dead: out of numerator, IN the live-fraction denominator
            live_pairs += 1
            per_item_abs_deltas.append(abs(mean(hi) - mean(lo)))  # D5: abs PER ITEM
        if per_item_abs_deltas:
            process_signatures[model] = mean(per_item_abs_deltas)

    # content baseline: per-model mean over items of the item's STANDARD-condition mean stance (D3)
    content_means_all: Dict[str, float] = {}
    for model in models:
        per_item_std = [
            mean(cells[(model, item, standard_condition)])
            for item in items
            if cells.get((model, item, standard_condition))
        ]
        if per_item_std:
            content_means_all[model] = mean(per_item_std)

    # roster intersection (D4): CVs over models present in BOTH axes
    models_used = sorted(set(process_signatures) & set(content_means_all))
    process_signatures = {m: process_signatures[m] for m in models_used}
    content_means = {m: content_means_all[m] for m in models_used}

    process_cv = coefficient_of_variation(process_signatures.values(), epsilon=epsilon)
    content_cv = coefficient_of_variation(content_means.values(), epsilon=epsilon)

    numeric_pass = (
        process_cv is not None and content_cv is not None and process_cv > content_cv
    )
    denom = live_pairs + dead_pairs
    live_cell_fraction = (live_pairs / denom) if denom else 0.0
    provisional = bool(numeric_pass and live_cell_fraction < live_cell_floor)
    verdict = ("PROVISIONAL" if provisional else "PASS") if numeric_pass else "FAIL"

    return {
        "process_cv": process_cv,
        "content_cv": content_cv,
        "pass": bool(numeric_pass),
        "provisional": provisional,
        "verdict": verdict,
        "process_signatures": process_signatures,
        "content_means": content_means,
        "models_used": models_used,
        "dead_cells": dead_cells,
        "unmeasurable_cells": unmeasurable_cells,
        "live_cell_fraction": live_cell_fraction,
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
        standard_condition=cfg.get("g1_standard_condition", "standard"),
        live_cell_floor=cfg.get("g1_live_cell_floor", 0.40),
        unmeasurable_conditions=cfg.get("g1_unmeasurable_conditions"),
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
    # Surface G1-b's thin-base caveat: a numeric pass on a <40%-live base is PROVISIONAL (build
    # may start, but the 9-model + dead-cell audit gates P2 spend -- outcome table, ruling G1-b).
    provisional = bool(overall and g1.get("provisional"))
    return {
        "G1": g1, "G2": g2, "G3": g3,
        "overall_pass": overall,
        "provisional": provisional,
    }
