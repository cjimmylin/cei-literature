"""Item-bank adversarial-read dispositions wired into the analysis (IB-1a / IB-3a / IB-4 / IB-5).

These are binding rulings from the P0 item-bank read (20260706-p0-item-bank-adversarial-read.md),
listed as run-precondition wiring in the WS-1 §1 checklist. They are sensitivity / reporting
analyses (not gates), each guarding a specific confound the item bank carries.
"""
from __future__ import annotations

from collections import defaultdict
from statistics import fmean
from typing import Dict, List, Optional, Sequence

from .stats import mean

# IB-4 (binding wording): PS-dir is defined as the shift toward the stance-5 (intervene) pole; the
# consequentialist reading is reserved to the Greene subset. Analysis outputs must use this label.
PS_DIR_DEFINITION = (
    "PS-dir = shift toward the stance-5 (intervene) pole (NOT 'outcome-maximizing'); the "
    "consequentialist reading of PS-dir is reserved to the Greene subset (IB-4)."
)


def _live(results: Sequence[dict]) -> List[dict]:
    return [r for r in results if not r.get("refusal") and r.get("score") is not None]


def affect_primed_pooled(results: Sequence[dict], affect_condition: str = "affect_primed") -> dict:
    """IB-1(a): affect_primed enters P0 ONLY as one undifferentiated resource condition. Because
    the Ekman prime is perfectly aliased with severity×ambiguity, affect_primed effects MUST NOT
    be interpreted by factorial cell. This returns the POOLED affect_primed stance only and
    explicitly withholds any by-cell breakdown."""
    scores = [float(r["score"]) for r in _live(results)
              if r.get("resource_condition") == affect_condition]
    return {
        "n": len(scores),
        "mean_stance": (fmean(scores) if scores else None),
        "by_cell_breakdown": None,   # deliberately withheld (IB-1a aliasing)
        "note": "affect_primed pooled only; by-(severity/ambiguity) interpretation prohibited (IB-1a).",
    }


def within_polarity_cross_domain(
    results: Sequence[dict],
    high_condition: str = "extended_thinking",
    low_condition: str = "forced_immediate",
    polarity: str = "affirmative_intervene",
) -> dict:
    """IB-3(a): stance polarity is aliased with content domain, so any headline cross-domain
    PS-stability contrast must be checked WITHIN a single polarity class (intervene-keyed items
    only) as a sensitivity. Returns the per-domain process signature (mean |per-item delta|)
    computed over `polarity` items only, plus the polarity-mix caveat."""
    intervene = [r for r in _live(results) if r.get("stance_polarity") == polarity]

    cells: Dict[tuple, List[float]] = defaultdict(list)
    domains: Dict[tuple, str] = {}
    for r in intervene:
        tags = r.get("content_tags") or []
        domain = tags[0] if tags else "unknown"
        key = (domain, r["item_id"], r["model_id"], r["resource_condition"])
        cells[key].append(float(r["score"]))
        domains[(domain, r["item_id"], r["model_id"])] = domain

    per_domain_abs_deltas: Dict[str, List[float]] = defaultdict(list)
    for (domain, item, model) in domains:
        hi = cells.get((domain, item, model, high_condition))
        lo = cells.get((domain, item, model, low_condition))
        if hi and lo:
            per_domain_abs_deltas[domain].append(abs(mean(hi) - mean(lo)))

    signatures = {d: fmean(v) for d, v in per_domain_abs_deltas.items() if v}
    return {
        "polarity_class": polarity,
        "per_domain_process_signature": signatures,
        "caveat": "cross-domain PS-stability reported within the intervene-keyed class only "
                  "(stance polarity is aliased with content domain, IB-3a).",
    }


def control_shift_metric(
    results: Sequence[dict],
    high_condition: str = "extended_thinking",
    low_condition: str = "forced_immediate",
    round_ndigits: Optional[int] = 0,
) -> dict:
    """IB-5: controls answer on categorical/numeric scales, not the moral 1..5 ordinal, so the
    moral-minus-nonmoral resource-dependence comparison needs a pre-defined COMMENSURABLE shift
    metric. Chosen (parameterized, filed per the succession rule): per control item×model,
    shift = |modal-answer-agreement(high) - modal-answer-agreement(low)|, where modal-answer
    agreement is the fraction of reps at the rounded modal answer. Aggregated to a mean shift."""
    controls = [r for r in _live(results) if r.get("is_discriminant_control")]

    def agreement(scores: List[float]) -> Optional[float]:
        if not scores:
            return None
        binned = [round(s, round_ndigits) if round_ndigits is not None else s for s in scores]
        counts: Dict[float, int] = defaultdict(int)
        for b in binned:
            counts[b] += 1
        return max(counts.values()) / len(binned)

    cells: Dict[tuple, List[float]] = defaultdict(list)
    pairs = set()
    for r in controls:
        cells[(r["item_id"], r["model_id"], r["resource_condition"])].append(float(r["score"]))
        pairs.add((r["item_id"], r["model_id"]))

    shifts: List[float] = []
    for (item, model) in pairs:
        a_hi = agreement(cells.get((item, model, high_condition), []))
        a_lo = agreement(cells.get((item, model, low_condition), []))
        if a_hi is not None and a_lo is not None:
            shifts.append(abs(a_hi - a_lo))

    return {
        "metric": "abs(modal_answer_agreement[high] - modal_answer_agreement[low])",
        "mean_control_shift": (fmean(shifts) if shifts else None),
        "n_control_cells": len(shifts),
        "note": "commensurable non-moral shift for the §5 moral-vs-control comparison (IB-5); "
                "parameterized, not hardcoded (succession rule).",
    }
