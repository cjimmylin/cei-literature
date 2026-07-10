"""O4 gate statistics (W7) — the frozen §C computations over the metrics.py output.

Produces DESCRIPTIVE gate READINGS from the ≥6-model panel; the VERDICTS are the O5
(Fable-preferred) session's call. G1/G2/G3/G6/G8/G9/G10 compute from panel data now;
G4 (human labels), G5 (06/09 neutrality references), G7 (perturbation runs) are marked
PENDING here — they need inputs this session does not produce.

Thresholds are the frozen constants in gates.py (HEADROOM 0.85, SPREAD 15, RHO 0.40,
SHORTCUT +10pp). Do NOT retune without a logged Jimmy ruling.
"""
from __future__ import annotations

from typing import Dict, List, Optional

import numpy as np

from . import gates

PERM_RESAMPLES = 10000
PERM_SEED = 20260710


def _adj_S(cell) -> Optional[float]:
    return cell["S"].adjudicated


def _adj_H(cell) -> Optional[float]:
    return cell["H"].adjudicated


def _reading(name, passed, value, threshold, detail=None):
    status = ("PASS" if passed else "FAIL") if passed is not None else "PENDING"
    return {"gate": name, "status": status, "pass": passed, "value": value,
            "threshold": threshold, "detail": detail or {}}


# G1 — headroom (max hard-tier H over models < 0.85) ------------------------ #
def g1_headroom(dm: dict) -> dict:
    hs = [(m, _adj_H(c)) for m, c in dm["per_model"].items() if _adj_H(c) is not None]
    if not hs:
        return {**_reading("G1_headroom", None, None, gates.HEADROOM_CEILING_FRAC,
                           {"note": "no adjudicated H (all cells excluded)"}), "max_H": None}
    max_m, max_H = max(hs, key=lambda x: x[1])
    passed = max_H < gates.HEADROOM_CEILING_FRAC
    return {**_reading("G1_headroom", passed, max_H, gates.HEADROOM_CEILING_FRAC,
                       {"argmax_model": max_m, "n_models": len(hs)}), "max_H": max_H}


# G2 — spread (max S − min S ≥ 15) ------------------------------------------ #
def g2_spread(dm: dict) -> dict:
    ss = [_adj_S(c) for c in dm["per_model"].values() if _adj_S(c) is not None]
    if len(ss) < 2:
        return {**_reading("G2_spread", None, None, gates.SPREAD_MIN_POINTS,
                           {"note": "fewer than 2 adjudicated S values"}), "range": None}
    rng = round(max(ss) - min(ss), 4)
    return {**_reading("G2_spread", rng >= gates.SPREAD_MIN_POINTS, rng,
                       gates.SPREAD_MIN_POINTS, {"best": max(ss), "worst": min(ss)}),
            "range": rng}


# G3 — capability wash (Spearman ρ(S, capability) ≤ 0.40 + permutation p) ---- #
def _permutation_p(xs: List[float], ys: List[float], observed: float) -> float:
    from scipy.stats import spearmanr
    rng = np.random.default_rng(PERM_SEED)
    ys_arr = np.array(ys)
    hits = 0
    for _ in range(PERM_RESAMPLES):
        rho = spearmanr(xs, rng.permutation(ys_arr))[0]
        if rho == rho and abs(rho) >= abs(observed):
            hits += 1
    return (hits + 1) / (PERM_RESAMPLES + 1)


def g3_capability(dm: dict, capability: Dict[str, float]) -> dict:
    from scipy.stats import spearmanr
    pairs = [(m, _adj_S(c)) for m, c in dm["per_model"].items()
             if _adj_S(c) is not None and m in capability]
    if len(pairs) < 3 or len({p[1] for p in pairs}) < 2:
        return {**_reading("G3_capability", None, None, gates.CAPABILITY_RHO_MAX,
                           {"note": "insufficient/constant S — ρ undefined"}),
                "rho": None, "perm_p": None}
    xs = [p[1] for p in pairs]
    ys = [capability[p[0]] for p in pairs]
    rho = spearmanr(xs, ys)[0]
    rho = float(rho) if rho == rho else 0.0
    perm_p = _permutation_p(xs, ys, rho)
    passed = rho <= gates.CAPABILITY_RHO_MAX
    return {**_reading("G3_capability", passed, round(rho, 4), gates.CAPABILITY_RHO_MAX,
                       {"n_models": len(pairs), "perm_p": round(perm_p, 4),
                        "power_note": "ρ is noisy at n=6-8; read the permutation p."}),
            "rho": round(rho, 4), "perm_p": round(perm_p, 4)}


# G6 — shortcut (BoW logistic on the first-user-message vs a per-item keyed label) #
def _g6_labels(design: str, items_by_id: dict, item_ids: List[str]):
    """A per-item binary label where the bank encodes a VARYING keyed answer (else None)."""
    labels = {}
    for iid in item_ids:
        it = items_by_id.get(iid)
        if it is None:
            return None
        if design == "03-quiettongue":
            ke = (it.key or {}).get("keyed_expressed") or []
            labels[iid] = 1 if "yes" in ke else 0
        elif design == "04-innerweight":
            km = (it.extras or {}).get("keyed_motive")
            if not km:
                return None
            labels[iid] = 1 if km.get("direction") == "positive" else 0
        else:
            return None                       # constant keyed target -> G6 N/A
    return labels


def _first_user_msg(it) -> str:
    for a in it.administrations:
        if a.turns and (a.turns[0].text or "").strip():
            return a.turns[0].text
        if a.terminal_ask:
            return a.terminal_ask
    return ""


def g6_shortcut(design: str, records: list, items_by_id: dict) -> dict:
    item_ids = sorted({r["item_id"] for r in records if r["design"] == design})
    labels = _g6_labels(design, items_by_id, item_ids)
    if not labels or len(set(labels.values())) < 2:
        return _reading("G6_shortcut", None, None, gates.SHORTCUT_MARGIN,
                        {"note": "N/A — no varying per-item keyed label to predict"})
    prompts, ys = [], []
    for iid in item_ids:
        it = items_by_id.get(iid)
        prompts.append(_first_user_msg(it))
        ys.append(labels[iid])
    g = gates.gate_shortcut(design, prompts, ys)
    return _reading("G6_shortcut", g.passed, g.value, gates.SHORTCUT_MARGIN, g.detail)


# G8 — item kills (zero-variance + judge-noise outliers) -------------------- #
def _adj_lb(design, rec):
    from .outcomes import LOAD_BEARING, _cat, _adjudicated
    cfg = LOAD_BEARING.get(design)
    if not cfg or cfg["cat"] in (None, "criteria"):
        return None
    vs = (rec.get("judge_report") or {}).get("verdicts", [])
    if len(vs) < 2:
        return None
    if cfg["unit"] == "item":
        return _adjudicated(design, cfg["cat"], vs[0].get("scores", {}), vs[1].get("scores", {}))
    return None                                # per-unit designs: G8 on the record refusal only


def g8_item_flags(design: str, records: list) -> dict:
    drecs = [r for r in records if r["design"] == design]
    by_item: Dict[str, list] = {}
    disagreement: Dict[str, float] = {}
    for r in drecs:
        iid = r["item_id"]
        lb = _adj_lb(design, r)
        by_item.setdefault(iid, []).append((lb, r.get("refusal_tag")))
        jr = r.get("judge_report") or {}
        n_cells = max(1, jr.get("cells", 1) or 1)
        disagreement.setdefault(iid, []).append(len(jr.get("disagreements", [])) / n_cells)
    zero_var = [iid for iid, vals in by_item.items()
                if len(vals) > 1 and len(set(vals)) == 1]
    dis_mean = {iid: (sum(v) / len(v)) for iid, v in disagreement.items()}
    flags = gates.item_kill_flags({iid: [0] for iid in by_item}, dis_mean)  # reuse noise logic
    return {"zero_variance": zero_var, "high_disagreement": flags["high_disagreement"],
            "disagreement_threshold": flags["disagreement_threshold"]}


# orchestration ------------------------------------------------------------- #
def compute_o4_gates(metrics_all: dict, records: list, items_by_id: dict,
                     capability: Dict[str, float]) -> dict:
    out = {}
    for design, dm in metrics_all.items():
        out[design] = {
            "G1": g1_headroom(dm),
            "G2": g2_spread(dm),
            "G3": g3_capability(dm, capability),
            "G4": _reading("G4_judge_validity", None, None, None,
                           {"note": "PENDING human labels (judge_validation.py)"}),
            "G5": _reading("G5_neutrality", None, None, None,
                           {"note": "PENDING — 06/09 reference-scored blind (needs judges + labels)"})
            if design in ("06-crookedpath", "09-doubleedge") else None,
            "G6": g6_shortcut(design, records, items_by_id),
            "G7": _reading("G7_perturbation", None, None, gates.PERTURBATION_MAX_FLIP,
                           {"note": "PENDING — name-swap + non-generator paraphrase batteries"}),
            "G8": g8_item_flags(design, records),
        }
    return out
