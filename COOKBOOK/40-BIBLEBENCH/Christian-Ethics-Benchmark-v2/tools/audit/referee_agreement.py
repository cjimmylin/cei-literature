"""JR-referee three-way agreement analysis — OFFLINE. NO model calls.

WALKWORTHY-CANARY-7f3e2026

Joins the Opus referee verdicts against the two shipped judges (judge-A from the
pilot .eval logs, judge-B from judgeB-verdicts.jsonl) on the 942 sampled units in
logs/jr-referee-20260716/sample-manifest.jsonl, then computes per-stratum agreement,
side-with rates, an unscorable audit, and design-06 profile deltas.

JOIN KEY DISCIPLINE (mirrors make_referee_manifest.py):
  * Opus verdict     : keyed by prompt_sha256 (the manifest already carries it).
  * judge-A          : Score.value dict from the SUT's .eval, keyed
                       (sut, log-basename, sample_id); turn_states is a JSON-ENCODED
                       STRING -> decode; turn_index is POSITIONAL into that list.
  * judge-B          : judge_b dict from judgeB-verdicts.jsonl, same (sut, log, id) key.
  * design 06        : judge value is a dict of the 7 categories directly
                       (frame, facts, principles, alternatives, resolution, remainder,
                       pastoral), each in {0,0.5,1}; profile_mean = mean of the 7.

Nothing is pooled across strata: 02/07 are reported PER (design, stratum) slice, and
each Cohen's kappa is computed from that slice's OWN label distributions.

Output: logs/jr-referee-20260716/referee-agreement.json  (+ full stdout tables).
All floats rounded to 4 dp in the JSON.

Usage:
    .venv/bin/python tools/audit/referee_agreement.py
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

CANARY = "WALKWORTHY-CANARY-7f3e2026"
UNSCORABLE = "unscorable"
PER_TURN_DESIGNS = {"02", "07"}
PROFILE_CATS = ["frame", "facts", "principles", "alternatives",
                "resolution", "remainder", "pastoral"]


# --------------------------------------------------------------------------- #
# join machinery (mirrors make_referee_manifest.py)
# --------------------------------------------------------------------------- #
def _design_num_from_task(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _decode_turn_states(raw: Any) -> List[Any]:
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw or "[]")
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def _basename(p: str) -> str:
    return os.path.basename(p or "")


def _load_judge_a(pilot_dir: str, designs: set) -> Dict[Tuple[str, str, str], dict]:
    out: Dict[Tuple[str, str, str], dict] = {}
    for sut_path in sorted(glob.glob(os.path.join(pilot_dir, "*/"))):
        sut = Path(sut_path.rstrip("/")).name
        for p in sorted(glob.glob(os.path.join(sut_path, "*.eval"))):
            head = read_eval_log(p, header_only=True)
            dn = _design_num_from_task(head.eval.task)
            if dn not in designs:
                continue
            log = read_eval_log(p)
            lb = _basename(p)
            for s in (log.samples or []):
                if not s.scores:
                    continue
                sc = list(s.scores.values())[0]
                val = sc.value if isinstance(sc.value, dict) else {}
                out[(sut, lb, s.id)] = val
    return out


def _load_judge_b(pilot_dir: str, designs: set) -> Dict[Tuple[str, str, str], dict]:
    out: Dict[Tuple[str, str, str], dict] = {}
    for sut_path in sorted(glob.glob(os.path.join(pilot_dir, "*/"))):
        sut = Path(sut_path.rstrip("/")).name
        vpath = os.path.join(sut_path, "judgeB-verdicts.jsonl")
        if not os.path.exists(vpath):
            continue
        for line in open(vpath, encoding="utf-8"):
            r = json.loads(line)
            dn = (r.get("design", "") or "")[:2]
            if dn not in designs:
                continue
            out[(sut, _basename(r.get("log", "")), r["sample_id"])] = r.get("judge_b") or {}
    return out


def _load_opus(prompts_dir: str) -> Dict[str, Any]:
    """{prompt_sha256: verdict}  (str for 02/07, dict for 06, 'unscorable' either way)."""
    out: Dict[str, Any] = {}
    with open(os.path.join(prompts_dir, "opus-verdicts.jsonl"), encoding="utf-8") as fh:
        for line in fh:
            r = json.loads(line)
            out[r["prompt_sha256"]] = r["verdict"]
    return out


# --------------------------------------------------------------------------- #
# per-turn state extraction for 02/07
# --------------------------------------------------------------------------- #
def _turn_state(val: dict, ti: Optional[int]) -> Optional[str]:
    states = _decode_turn_states(val.get("turn_states"))
    if ti is None or ti >= len(states) or ti < 0:
        return None
    return states[ti]


# --------------------------------------------------------------------------- #
# Cohen's kappa (unweighted) from paired label lists, slice-local distributions
# --------------------------------------------------------------------------- #
def _cohen_kappa(a: List[str], b: List[str]) -> Tuple[Optional[float], Optional[str]]:
    """Unweighted Cohen's kappa. Returns (kappa, note).

    kappa undefined (returns (None, note)) when expected agreement Pe == 1, which
    happens iff both raters put ALL mass on a single (shared) label -> a degenerate
    marginal. In that case observed agreement is trivially 1 and kappa is 0/0.
    """
    n = len(a)
    if n == 0:
        return None, "empty slice"
    labels = sorted(set(a) | set(b))
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca = Counter(a)
    cb = Counter(b)
    pe = sum((ca[l] / n) * (cb[l] / n) for l in labels)
    if abs(pe - 1.0) < 1e-12:
        return None, ("kappa undefined: expected agreement Pe=1 (both raters place all "
                      "mass on one shared label; degenerate marginal)")
    return (po - pe) / (1.0 - pe), None


def _raw_agreement(a: List[str], b: List[str]) -> Optional[float]:
    if not a:
        return None
    return sum(1 for x, y in zip(a, b) if x == y) / len(a)


def _r4(x):
    return round(x, 4) if isinstance(x, float) else x


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #
def build(pilot_dir: str, refdir: str) -> Dict[str, Any]:
    designs = {"02", "07", "06"}
    judge_a = _load_judge_a(pilot_dir, designs)
    judge_b = _load_judge_b(pilot_dir, designs)
    opus = _load_opus(refdir)

    manifest: List[dict] = []
    with open(os.path.join(refdir, "sample-manifest.jsonl"), encoding="utf-8") as fh:
        for line in fh:
            manifest.append(json.loads(line))

    anomalies: List[dict] = []

    # Resolve every manifest unit to (opus, A, B) verdicts.
    # For 02/07: verdicts are per-turn state labels (strings).
    # For 06: verdicts are 7-category dicts.
    units: List[dict] = []
    for r in manifest:
        design = r["design"]
        key = (r["sut"], _basename(r["log"]), r["sample_id"])
        sha = r["prompt_sha256"]
        va = judge_a.get(key)
        vb = judge_b.get(key)
        vo = opus.get(sha)
        if va is None or vb is None or vo is None:
            anomalies.append({"design": design, "sut": r["sut"], "sample_id": r["sample_id"],
                              "turn_index": r["turn_index"], "prompt_sha256": sha,
                              "missing_A": va is None, "missing_B": vb is None,
                              "missing_opus": vo is None})
            continue

        rec = {"design": design, "sut": r["sut"], "sample_id": r["sample_id"],
               "item_id": r["item_id"], "admin": r["admin"], "stratum": r["stratum"],
               "turn_index": r["turn_index"]}

        if design in PER_TURN_DESIGNS:
            ti = r["turn_index"]
            a_state = _turn_state(va, ti)
            b_state = _turn_state(vb, ti)
            if a_state is None or b_state is None:
                anomalies.append({"design": design, "sut": r["sut"],
                                  "sample_id": r["sample_id"], "turn_index": ti,
                                  "reason": "turn_index out of range in turn_states"})
                continue
            rec.update({"opus": vo, "A": a_state, "B": b_state})
        else:  # 06
            # judge dicts carry the 7 category floats directly; opus is a dict or "unscorable".
            rec.update({"opus": vo, "A": va, "B": vb})
        units.append(rec)

    # ================================================================== #
    # 1 + 2 + 3 + 5 : designs 02 and 07 (per-turn state labels)
    # ================================================================== #
    per_turn = {d: [u for u in units if u["design"] == d] for d in ("02", "07")}

    def _slice_metrics(us: List[dict]) -> dict:
        a = [u["A"] for u in us]
        b = [u["B"] for u in us]
        o = [u["opus"] if isinstance(u["opus"], str) else "unscorable" for u in us]
        k_oa, note_oa = _cohen_kappa(o, a)
        k_ob, note_ob = _cohen_kappa(o, b)
        m = {
            "n": len(us),
            "raw_agreement_opus_A": _raw_agreement(o, a),
            "raw_agreement_opus_B": _raw_agreement(o, b),
            "cohen_kappa_opus_A": k_oa,
            "cohen_kappa_opus_B": k_ob,
        }
        notes = {}
        if note_oa:
            notes["cohen_kappa_opus_A"] = note_oa
        if note_ob:
            notes["cohen_kappa_opus_B"] = note_ob
        if notes:
            m["kappa_notes"] = notes
        return m

    designs_02_07: Dict[str, Any] = {}
    for d in ("02", "07"):
        by_stratum: Dict[str, Any] = {}
        for stratum in sorted({u["stratum"] for u in per_turn[d]}):
            sl = [u for u in per_turn[d] if u["stratum"] == stratum]
            entry = {"overall": _slice_metrics(sl), "per_sut": {}}
            for sut in sorted({u["sut"] for u in sl}):
                entry["per_sut"][sut] = _slice_metrics([u for u in sl if u["sut"] == sut])
            by_stratum[stratum] = entry
        designs_02_07[d] = by_stratum

    # ---- (2) disagreement-stratum side-with rates + top-8 triples ------- #
    def _side_with(us: List[dict]) -> dict:
        n = len(us)
        sa = sum(1 for u in us if u["opus"] == u["A"] and u["opus"] != u["B"])
        sb = sum(1 for u in us if u["opus"] == u["B"] and u["opus"] != u["A"])
        sn = sum(1 for u in us if u["opus"] != u["A"] and u["opus"] != u["B"])
        # note: on disagreement strata A != B by construction, so opus==A==B is impossible.
        return {
            "n": n,
            "sides_with_A": sa, "sides_with_B": sb, "sides_with_neither": sn,
            "sides_with_A_rate": (sa / n) if n else None,
            "sides_with_B_rate": (sb / n) if n else None,
            "sides_with_neither_rate": (sn / n) if n else None,
        }

    side_with = {}
    triples = {}
    for d in ("02", "07"):
        dis = [u for u in per_turn[d] if u["stratum"] == "disagreement"]
        entry = {"overall": _side_with(dis), "per_sut": {}}
        for sut in sorted({u["sut"] for u in dis}):
            entry["per_sut"][sut] = _side_with([u for u in dis if u["sut"] == sut])
        side_with[d] = entry
        trip = Counter((u["A"], u["B"],
                        u["opus"] if isinstance(u["opus"], str) else "unscorable")
                       for u in dis)
        triples[d] = [{"A_state": t[0], "B_state": t[1], "opus_state": t[2], "count": c}
                      for t, c in trip.most_common(8)]

    # ---- (3) opus-unscorable audit ------------------------------------- #
    unsc_units = [u for u in units
                  if u["design"] in PER_TURN_DESIGNS and u["opus"] == UNSCORABLE]
    unsc_by_item: Dict[str, Any] = {}
    for item in sorted({u["item_id"] for u in unsc_units}):
        iu = [u for u in unsc_units if u["item_id"] == item]
        unsc_by_item[item] = {
            "design": iu[0]["design"],
            "n": len(iu),
            "A_states": dict(Counter(u["A"] for u in iu).most_common()),
            "B_states": dict(Counter(u["B"] for u in iu).most_common()),
        }
    unscorable_audit = {
        "n_opus_unscorable_units": len(unsc_units),
        "by_item_id": unsc_by_item,
        "note": ("Design-07 items WW-07-L02 / WW-07-I04 / WW-07-F02 ship '(no keyed "
                 "text)' rubric anchors; Opus unscorables expected to concentrate there."),
    }

    # sensitivity: recompute 07 disagreement side-with EXCLUDING item_ids where opus
    # EVER said unscorable (anywhere in the sampled 07 units).
    unsc_items_07 = {u["item_id"] for u in unsc_units if u["design"] == "07"}
    d07_dis = [u for u in per_turn["07"] if u["stratum"] == "disagreement"]
    d07_dis_excl = [u for u in d07_dis if u["item_id"] not in unsc_items_07]
    sensitivity_07 = {
        "excluded_item_ids": sorted(unsc_items_07),
        "n_before": len(d07_dis),
        "n_after": len(d07_dis_excl),
        "side_with_before": _side_with(d07_dis),
        "side_with_after": _side_with(d07_dis_excl),
        "per_sut_after": {sut: _side_with([u for u in d07_dis_excl if u["sut"] == sut])
                          for sut in sorted({u["sut"] for u in d07_dis_excl})},
    }

    # ---- (5) control-stratum concordance (02/07): A==B, opus-vs-shared - #
    control_concordance = {}
    for d in ("02", "07"):
        ctrl = [u for u in per_turn[d] if u["stratum"] == "control"]
        # controls: A==B by construction; verify and report opus==shared rate.
        mism = sum(1 for u in ctrl if u["A"] != u["B"])
        matched = [u for u in ctrl if u["A"] == u["B"]]
        agree = sum(1 for u in matched if u["opus"] == u["A"])
        entry = {
            "n": len(ctrl),
            "n_A_ne_B_violations": mism,
            "opus_matches_shared": agree,
            "opus_matches_shared_rate": (agree / len(matched)) if matched else None,
            "per_sut": {},
        }
        for sut in sorted({u["sut"] for u in ctrl}):
            sm = [u for u in matched if u["sut"] == sut]
            ag = sum(1 for u in sm if u["opus"] == u["A"])
            entry["per_sut"][sut] = {
                "n": len([u for u in ctrl if u["sut"] == sut]),
                "opus_matches_shared": ag,
                "opus_matches_shared_rate": (ag / len(sm)) if sm else None,
            }
        control_concordance[d] = entry

    # ================================================================== #
    # 4 : design 06 (per-category deltas + profile_mean comparison)
    # ================================================================== #
    def _cat_float(val: dict, cat: str) -> Optional[float]:
        v = val.get(cat)
        if v is None or v == UNSCORABLE:
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    def _profile_mean(val) -> Optional[float]:
        if not isinstance(val, dict):
            return None
        vals = [_cat_float(val, c) for c in PROFILE_CATS]
        if any(v is None for v in vals):
            return None
        return sum(vals) / len(vals)

    six = [u for u in units if u["design"] == "06"]
    design06: Dict[str, Any] = {}
    for stratum in sorted({u["stratum"] for u in six}):
        sl = [u for u in six if u["stratum"] == stratum]
        # per-category mean delta (opus - A), (opus - B)
        cat_delta_A: Dict[str, Any] = {}
        cat_delta_B: Dict[str, Any] = {}
        for cat in PROFILE_CATS:
            da, db, na, nb = [], [], 0, 0
            for u in sl:
                oc = _cat_float(u["opus"], cat)
                ac = _cat_float(u["A"], cat)
                bc = _cat_float(u["B"], cat)
                if oc is not None and ac is not None:
                    da.append(oc - ac); na += 1
                if oc is not None and bc is not None:
                    db.append(oc - bc); nb += 1
            cat_delta_A[cat] = {"mean_delta": (sum(da) / len(da)) if da else None, "n": na}
            cat_delta_B[cat] = {"mean_delta": (sum(db) / len(db)) if db else None, "n": nb}
        avg_delta_A = ([cat_delta_A[c]["mean_delta"] for c in PROFILE_CATS])
        avg_delta_B = ([cat_delta_B[c]["mean_delta"] for c in PROFILE_CATS])
        avg_delta_A = (sum(v for v in avg_delta_A if v is not None)
                       / sum(1 for v in avg_delta_A if v is not None)) if any(
                           v is not None for v in avg_delta_A) else None
        avg_delta_B = (sum(v for v in avg_delta_B if v is not None)
                       / sum(1 for v in avg_delta_B if v is not None)) if any(
                           v is not None for v in avg_delta_B) else None

        # profile_mean comparison
        pm_o = [_profile_mean(u["opus"]) for u in sl]
        pm_a = [_profile_mean(u["A"]) for u in sl]
        pm_b = [_profile_mean(u["B"]) for u in sl]

        def _mean(xs):
            xs = [x for x in xs if x is not None]
            return (sum(xs) / len(xs)) if xs else None

        def _closer(us):
            ca = cb = eq = nn = 0
            for u in us:
                o = _profile_mean(u["opus"])
                a = _profile_mean(u["A"])
                b = _profile_mean(u["B"])
                if o is None or a is None or b is None:
                    nn += 1
                    continue
                da_, db_ = abs(o - a), abs(o - b)
                if da_ < db_:
                    ca += 1
                elif db_ < da_:
                    cb += 1
                else:
                    eq += 1
            return {"closer_to_A": ca, "closer_to_B": cb, "equidistant": eq,
                    "n_unscorable_excluded": nn, "n_compared": ca + cb + eq}

        entry = {
            "n": len(sl),
            "per_category_mean_delta_opus_minus_A": cat_delta_A,
            "per_category_mean_delta_opus_minus_B": cat_delta_B,
            "avg_category_delta_opus_minus_A": avg_delta_A,
            "avg_category_delta_opus_minus_B": avg_delta_B,
            "mean_profile_mean_opus": _mean(pm_o),
            "mean_profile_mean_A": _mean(pm_a),
            "mean_profile_mean_B": _mean(pm_b),
            "closer_overall": _closer(sl),
            "closer_per_sut": {sut: _closer([u for u in sl if u["sut"] == sut])
                               for sut in sorted({u["sut"] for u in sl})},
        }
        design06[stratum] = entry

    result = {
        "canary": CANARY,
        "n_manifest_units": len(manifest),
        "n_resolved": len(units),
        "n_anomalies": len(anomalies),
        "anomalies": anomalies[:50],
        "designs_02_07_per_stratum": designs_02_07,
        "disagreement_side_with": side_with,
        "disagreement_top8_triples": triples,
        "opus_unscorable_audit": unscorable_audit,
        "design07_unscorable_sensitivity": sensitivity_07,
        "control_concordance_02_07": control_concordance,
        "design06_per_stratum": design06,
    }
    return _round_floats(result)


def _round_floats(obj):
    if isinstance(obj, float):
        return round(obj, 4)
    if isinstance(obj, dict):
        return {k: _round_floats(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(v) for v in obj]
    return obj


# --------------------------------------------------------------------------- #
# printing
# --------------------------------------------------------------------------- #
def _fmt(x, w=8):
    if x is None:
        return "null".rjust(w)
    if isinstance(x, float):
        return f"{x:.4f}".rjust(w)
    return str(x).rjust(w)


def print_summary(res: dict) -> None:
    print("=" * 78)
    print(CANARY)
    print(f"manifest units: {res['n_manifest_units']}   resolved: {res['n_resolved']}   "
          f"anomalies: {res['n_anomalies']}")
    print("=" * 78)

    # 1. per (design, stratum) slice
    print("\n[1] DESIGNS 02 & 07 — per (design, stratum) slice "
          "(raw agreement + Cohen's kappa, opus vs A / opus vs B)")
    print("-" * 78)
    hdr = f"{'slice':<34}{'n':>5}{'rawA':>9}{'rawB':>9}{'kA':>9}{'kB':>9}"
    for d in ("02", "07"):
        for stratum, entry in res["designs_02_07_per_stratum"][d].items():
            print(f"\ndesign {d} / {stratum}")
            print(hdr)
            m = entry["overall"]
            print(f"{'  OVERALL':<34}{m['n']:>5}"
                  f"{_fmt(m['raw_agreement_opus_A'],9)}{_fmt(m['raw_agreement_opus_B'],9)}"
                  f"{_fmt(m['cohen_kappa_opus_A'],9)}{_fmt(m['cohen_kappa_opus_B'],9)}")
            if "kappa_notes" in m:
                for kk, nn in m["kappa_notes"].items():
                    print(f"      [{kk}] {nn}")
            for sut, sm in entry["per_sut"].items():
                print(f"{'    '+sut:<34}{sm['n']:>5}"
                      f"{_fmt(sm['raw_agreement_opus_A'],9)}{_fmt(sm['raw_agreement_opus_B'],9)}"
                      f"{_fmt(sm['cohen_kappa_opus_A'],9)}{_fmt(sm['cohen_kappa_opus_B'],9)}")
                if "kappa_notes" in sm:
                    for kk, nn in sm["kappa_notes"].items():
                        print(f"        [{kk}] {nn}")

    # 2. side-with (disagreement)
    print("\n" + "=" * 78)
    print("[2] DISAGREEMENT-STRATUM SIDE-WITH RATES (opus sides with A / B / neither)")
    print("-" * 78)
    hdr2 = f"{'slice':<30}{'n':>5}{'withA':>7}{'withB':>7}{'neither':>9}" \
           f"{'rA':>8}{'rB':>8}{'rN':>8}"
    for d in ("02", "07"):
        sw = res["disagreement_side_with"][d]
        print(f"\ndesign {d}")
        print(hdr2)
        m = sw["overall"]
        print(f"{'  OVERALL':<30}{m['n']:>5}{m['sides_with_A']:>7}{m['sides_with_B']:>7}"
              f"{m['sides_with_neither']:>9}{_fmt(m['sides_with_A_rate'],8)}"
              f"{_fmt(m['sides_with_B_rate'],8)}{_fmt(m['sides_with_neither_rate'],8)}")
        for sut, sm in sw["per_sut"].items():
            print(f"{'    '+sut:<30}{sm['n']:>5}{sm['sides_with_A']:>7}{sm['sides_with_B']:>7}"
                  f"{sm['sides_with_neither']:>9}{_fmt(sm['sides_with_A_rate'],8)}"
                  f"{_fmt(sm['sides_with_B_rate'],8)}{_fmt(sm['sides_with_neither_rate'],8)}")

    # top-8 triples
    for d in ("02", "07"):
        print(f"\ndesign {d} — top-8 (A_state, B_state, opus_state) triples")
        print(f"  {'A_state':<24}{'B_state':<24}{'opus_state':<24}{'count':>6}")
        for t in res["disagreement_top8_triples"][d]:
            print(f"  {t['A_state']:<24}{t['B_state']:<24}{t['opus_state']:<24}{t['count']:>6}")

    # 3. unscorable audit
    print("\n" + "=" * 78)
    print("[3] OPUS-UNSCORABLE AUDIT")
    print("-" * 78)
    ua = res["opus_unscorable_audit"]
    print(f"total opus-unscorable sampled units: {ua['n_opus_unscorable_units']}")
    print(f"  {'item_id':<16}{'design':<8}{'n':>4}   A_states / B_states")
    for item, info in ua["by_item_id"].items():
        print(f"  {item:<16}{info['design']:<8}{info['n']:>4}   "
              f"A={info['A_states']}  B={info['B_states']}")

    print("\n  [3b] design-07 disagreement side-with EXCLUDING opus-ever-unscorable item_ids")
    s = res["design07_unscorable_sensitivity"]
    print(f"  excluded item_ids: {s['excluded_item_ids']}")
    print(f"  n before={s['n_before']}  n after={s['n_after']}")
    for lbl, key in (("BEFORE", "side_with_before"), ("AFTER", "side_with_after")):
        m = s[key]
        print(f"    {lbl:<7} n={m['n']:>3}  withA={m['sides_with_A']} ({_fmt(m['sides_with_A_rate'],0).strip()})"
              f"  withB={m['sides_with_B']} ({_fmt(m['sides_with_B_rate'],0).strip()})"
              f"  neither={m['sides_with_neither']} ({_fmt(m['sides_with_neither_rate'],0).strip()})")
    print("    per-SUT AFTER:")
    for sut, m in s["per_sut_after"].items():
        print(f"      {sut:<22} n={m['n']:>3}  withA={m['sides_with_A']}({_fmt(m['sides_with_A_rate'],0).strip()})"
              f"  withB={m['sides_with_B']}({_fmt(m['sides_with_B_rate'],0).strip()})"
              f"  neither={m['sides_with_neither']}({_fmt(m['sides_with_neither_rate'],0).strip()})")

    # 4. design 06
    print("\n" + "=" * 78)
    print("[4] DESIGN 06 — per stratum (gap / control)")
    print("-" * 78)
    for stratum, e in res["design06_per_stratum"].items():
        print(f"\ndesign 06 / {stratum}  (n={e['n']})")
        print(f"  {'category':<14}{'delta(O-A)':>12}{'delta(O-B)':>12}")
        for cat in PROFILE_CATS:
            da = e["per_category_mean_delta_opus_minus_A"][cat]["mean_delta"]
            db = e["per_category_mean_delta_opus_minus_B"][cat]["mean_delta"]
            print(f"  {cat:<14}{_fmt(da,12)}{_fmt(db,12)}")
        print(f"  {'AVG':<14}{_fmt(e['avg_category_delta_opus_minus_A'],12)}"
              f"{_fmt(e['avg_category_delta_opus_minus_B'],12)}")
        print(f"  profile_mean:  Opus={_fmt(e['mean_profile_mean_opus'],0).strip()}  "
              f"A={_fmt(e['mean_profile_mean_A'],0).strip()}  "
              f"B={_fmt(e['mean_profile_mean_B'],0).strip()}")
        c = e["closer_overall"]
        print(f"  |O-A| vs |O-B| OVERALL: closer_to_A={c['closer_to_A']}  "
              f"closer_to_B={c['closer_to_B']}  equidistant={c['equidistant']}  "
              f"(n_compared={c['n_compared']}, unscorable_excluded={c['n_unscorable_excluded']})")
        for sut, cs in e["closer_per_sut"].items():
            print(f"    {sut:<22} closerA={cs['closer_to_A']}  closerB={cs['closer_to_B']}  "
                  f"eq={cs['equidistant']}  (n={cs['n_compared']})")

    # 5. control concordance
    print("\n" + "=" * 78)
    print("[5] CONTROL-STRATUM CONCORDANCE (02/07) — A==B by construction; opus vs shared")
    print("-" * 78)
    for d in ("02", "07"):
        cc = res["control_concordance_02_07"][d]
        print(f"\ndesign {d}: n={cc['n']}  A!=B violations={cc['n_A_ne_B_violations']}  "
              f"opus_matches_shared={cc['opus_matches_shared']} "
              f"(rate={_fmt(cc['opus_matches_shared_rate'],0).strip()})")
        for sut, sm in cc["per_sut"].items():
            print(f"    {sut:<22} n={sm['n']:>3}  matches={sm['opus_matches_shared']}  "
                  f"rate={_fmt(sm['opus_matches_shared_rate'],0).strip()}")

    print("\n" + "=" * 78)
    if res["n_anomalies"]:
        print(f"JOIN ANOMALIES: {res['n_anomalies']}")
        for a in res["anomalies"]:
            print("  ", a)
    else:
        print("JOIN ANOMALIES: none (all 942 sampled units resolved to opus+A+B)")
    print("=" * 78)


def main() -> None:
    ap = argparse.ArgumentParser(description="JR-referee three-way agreement (offline).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--ref-dir", default="logs/jr-referee-20260716")
    args = ap.parse_args()

    res = build(args.pilot_dir, args.ref_dir)
    out_path = os.path.join(args.ref_dir, "referee-agreement.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=2, ensure_ascii=False)
    print_summary(res)
    print(f"\nwrote -> {out_path}")


if __name__ == "__main__":
    main()
