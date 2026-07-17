"""JR-referee FOUR-WAY agreement analysis — OFFLINE. NO model calls.

WALKWORTHY-CANARY-7f3e2026

Extends tools/audit/referee_agreement.py (the committed three-way tool) to a
FOUR-way comparison over the same 942 sampled units:

    referee 1 : Opus   (opus-verdicts.jsonl,  keyed by prompt_sha256)
    referee 2 : Sol    (sol-verdicts.jsonl,   keyed by prompt_sha256; --sol-file)
    judge  A  : gpt-4.1-nano   (from the pilot .eval Score.value turn_states)
    judge  B  : llama-3.3-70b  (from judgeB-verdicts.jsonl)

This module REUSES referee_agreement.py's join + metric machinery. It imports it
as `ra` (same directory, sys.path insert) and never modifies it. Sol verdicts share
the EXACT schema of opus-verdicts.jsonl (str for 02/07, 7-cat dict for 06,
"unscorable" either way), so Sol is loaded with ra._load_opus's logic parametrised
on filename.

Everything is reported PER-STRATUM; nothing is pooled across strata. Each Cohen's
kappa is computed from that slice's OWN label distributions via ra._cohen_kappa.

Sol "unscorable" is a first-class STATE for 02/07 comparisons (kappa/raw treat it as
a label). For design-06 profile math, unscorable-verdict units are EXCLUDED from means
and counted separately (expected ~0).

STAND-IN SELF-TEST: pass `--sol-file logs/jr-referee-20260716/opus-verdicts.jsonl`
(the default sol file may not exist while the Sol run is in flight). Under the stand-in,
Sol == Opus, so every Sol<->Opus slice MUST show raw=1.0 / kappa=1.0 — that is the
structural self-test.

Output: logs/jr-referee-20260716/referee-agreement-sol.json (--out) + full stdout tables.
All floats rounded to 4 dp.

Usage:
    .venv/bin/python tools/audit/referee_agreement_sol.py \
        --sol-file logs/jr-referee-20260716/opus-verdicts.jsonl        # stand-in self-test
    .venv/bin/python tools/audit/referee_agreement_sol.py              # real Sol run
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_HERE = Path(__file__).resolve().parent
_V2_ROOT = _HERE.parents[1]
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_V2_ROOT))

import referee_agreement as ra  # noqa: E402  (reuse join + metric machinery)

CANARY = ra.CANARY
UNSCORABLE = ra.UNSCORABLE
PER_TURN_DESIGNS = ra.PER_TURN_DESIGNS
PROFILE_CATS = ra.PROFILE_CATS

# The three design-07 "(no keyed text)" defect items called out in the spec.
DEFECT_ITEMS_07 = {"WW-07-L02", "WW-07-I04", "WW-07-F02"}


# --------------------------------------------------------------------------- #
# Sol loader — mirrors ra._load_opus but takes an explicit path.
# --------------------------------------------------------------------------- #
def _load_sol(sol_path: str) -> Dict[str, Any]:
    """{prompt_sha256: verdict}. Same schema as opus-verdicts.jsonl."""
    out: Dict[str, Any] = {}
    with open(sol_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            out[r["prompt_sha256"]] = r["verdict"]
    return out


def _state(v: Any) -> str:
    """Collapse a 02/07 verdict to a string state label (unscorable-safe)."""
    return v if isinstance(v, str) else UNSCORABLE


# --------------------------------------------------------------------------- #
# unit resolution — mirrors ra.build's manifest -> (opus, A, B) join, adds Sol.
# --------------------------------------------------------------------------- #
def _resolve_units(pilot_dir: str, refdir: str, sol_path: str
                   ) -> Tuple[List[dict], List[dict]]:
    designs = {"02", "07", "06"}
    judge_a = ra._load_judge_a(pilot_dir, designs)
    judge_b = ra._load_judge_b(pilot_dir, designs)
    opus = ra._load_opus(refdir)
    sol = _load_sol(sol_path)

    manifest: List[dict] = []
    with open(os.path.join(refdir, "sample-manifest.jsonl"), encoding="utf-8") as fh:
        for line in fh:
            manifest.append(json.loads(line))

    anomalies: List[dict] = []
    units: List[dict] = []
    for r in manifest:
        design = r["design"]
        key = (r["sut"], ra._basename(r["log"]), r["sample_id"])
        sha = r["prompt_sha256"]
        va = judge_a.get(key)
        vb = judge_b.get(key)
        vo = opus.get(sha)
        vs = sol.get(sha)
        if va is None or vb is None or vo is None or vs is None:
            anomalies.append({"design": design, "sut": r["sut"],
                              "sample_id": r["sample_id"], "turn_index": r["turn_index"],
                              "prompt_sha256": sha, "missing_A": va is None,
                              "missing_B": vb is None, "missing_opus": vo is None,
                              "missing_sol": vs is None})
            continue

        rec = {"design": design, "sut": r["sut"], "sample_id": r["sample_id"],
               "item_id": r["item_id"], "admin": r["admin"], "stratum": r["stratum"],
               "turn_index": r["turn_index"]}

        if design in PER_TURN_DESIGNS:
            ti = r["turn_index"]
            a_state = ra._turn_state(va, ti)
            b_state = ra._turn_state(vb, ti)
            if a_state is None or b_state is None:
                anomalies.append({"design": design, "sut": r["sut"],
                                  "sample_id": r["sample_id"], "turn_index": ti,
                                  "reason": "turn_index out of range in turn_states"})
                continue
            rec.update({"opus": vo, "sol": vs, "A": a_state, "B": b_state})
        else:  # 06 — verdicts are 7-cat dicts or "unscorable"
            rec.update({"opus": vo, "sol": vs, "A": va, "B": vb})
        units.append(rec)
    return units, anomalies


# --------------------------------------------------------------------------- #
# 02/07 helpers
# --------------------------------------------------------------------------- #
def _labels(us: List[dict], who: str) -> List[str]:
    """String label list for a rater over per-turn units (unscorable-safe)."""
    if who in ("opus", "sol"):
        return [_state(u[who]) for u in us]
    return [u[who] for u in us]  # A / B are already turn-state strings


def _pair_metrics(us: List[dict], x: str, y: str) -> dict:
    xa = _labels(us, x)
    yb = _labels(us, y)
    k, note = ra._cohen_kappa(xa, yb)
    m = {"n": len(us),
         f"raw_agreement_{x}_{y}": ra._raw_agreement(xa, yb),
         f"cohen_kappa_{x}_{y}": k}
    if note:
        m[f"kappa_note_{x}_{y}"] = note
    return m


def _sol_slice_metrics(us: List[dict]) -> dict:
    """Sol<->A, Sol<->B, Sol<->Opus raw + unweighted kappa for a 02/07 slice."""
    out = {"n": len(us)}
    for other in ("A", "B", "opus"):
        m = _pair_metrics(us, "sol", other)
        out[f"raw_agreement_sol_{other}"] = m[f"raw_agreement_sol_{other}"]
        out[f"cohen_kappa_sol_{other}"] = m[f"cohen_kappa_sol_{other}"]
        note = m.get(f"kappa_note_sol_{other}")
        if note:
            out.setdefault("kappa_notes", {})[f"cohen_kappa_sol_{other}"] = note
    return out


def _sol_side_with(us: List[dict]) -> dict:
    """Sol side-with rates on a disagreement slice (A != B by construction)."""
    n = len(us)
    sa = sum(1 for u in us if _state(u["sol"]) == u["A"] and _state(u["sol"]) != u["B"])
    sb = sum(1 for u in us if _state(u["sol"]) == u["B"] and _state(u["sol"]) != u["A"])
    sn = sum(1 for u in us if _state(u["sol"]) != u["A"] and _state(u["sol"]) != u["B"])
    return {
        "n": n,
        "sides_with_A": sa, "sides_with_B": sb, "sides_with_neither": sn,
        "sides_with_A_rate": (sa / n) if n else None,
        "sides_with_B_rate": (sb / n) if n else None,
        "sides_with_neither_rate": (sn / n) if n else None,
    }


def _joint_referee_table(us: List[dict]) -> dict:
    """Mutually-exclusive joint (Opus, Sol) x (A, B) cells over a disagreement slice.

    On a disagreement slice A != B, so a referee is exactly one of {sides_A, sides_B,
    sides_neither}. The cross of the two referees' choices tiles the slice:

        both_side_A            : opus->A, sol->A
        both_side_B            : opus->B, sol->B
        opus_A_sol_B           : opus->A, sol->B   (referees split, opposite sides)
        opus_B_sol_A           : opus->B, sol->A   (referees split, opposite sides)
        opus_side_sol_neither  : opus sided (A or B), sol neither
        sol_side_opus_neither  : sol sided (A or B), opus neither
        both_neither           : opus neither, sol neither

    opus_side_sol_neither / sol_side_opus_neither are additionally split by which side
    the *sider* took (…_sider_A / …_sider_B) alongside the aggregate. The seven top-level
    cells are mutually exclusive and sum to n.
    """
    cells = Counter()
    sider_split = {"opus_side_sol_neither": Counter(), "sol_side_opus_neither": Counter()}

    def side(u, who):  # 'A' / 'B' / 'neither'
        s = _state(u[who])
        if s == u["A"] and s != u["B"]:
            return "A"
        if s == u["B"] and s != u["A"]:
            return "B"
        return "neither"

    for u in us:
        os_, ss_ = side(u, "opus"), side(u, "sol")
        if os_ == "A" and ss_ == "A":
            cells["both_side_A"] += 1
        elif os_ == "B" and ss_ == "B":
            cells["both_side_B"] += 1
        elif os_ == "A" and ss_ == "B":
            cells["opus_A_sol_B"] += 1
        elif os_ == "B" and ss_ == "A":
            cells["opus_B_sol_A"] += 1
        elif os_ in ("A", "B") and ss_ == "neither":
            cells["opus_side_sol_neither"] += 1
            sider_split["opus_side_sol_neither"][os_] += 1
        elif ss_ in ("A", "B") and os_ == "neither":
            cells["sol_side_opus_neither"] += 1
            sider_split["sol_side_opus_neither"][ss_] += 1
        else:  # both neither
            cells["both_neither"] += 1

    ordered = ["both_side_A", "both_side_B", "opus_A_sol_B", "opus_B_sol_A",
               "opus_side_sol_neither", "sol_side_opus_neither", "both_neither"]
    table = {k: cells.get(k, 0) for k in ordered}
    total = sum(table.values())
    out = {"n": len(us), "cells": table, "cells_sum": total,
           "cells_sum_equals_n": total == len(us),
           "opus_side_sol_neither_sider": dict(sider_split["opus_side_sol_neither"]),
           "sol_side_opus_neither_sider": dict(sider_split["sol_side_opus_neither"])}
    # Sol<->Opus raw agreement on this stratum (full string-state equality).
    out["raw_agreement_sol_opus"] = ra._raw_agreement(
        [_state(u["sol"]) for u in us], [_state(u["opus"]) for u in us])
    return out


def _top8_quads(us: List[dict]) -> List[dict]:
    quad = Counter((u["A"], u["B"], _state(u["opus"]), _state(u["sol"])) for u in us)
    return [{"A_state": t[0], "B_state": t[1], "opus_state": t[2], "sol_state": t[3],
             "count": c} for t, c in quad.most_common(8)]


# --------------------------------------------------------------------------- #
# design 06 helpers (reuse ra._cat_float / _profile_mean semantics)
# --------------------------------------------------------------------------- #
def _cat_float(val: dict, cat: str) -> Optional[float]:
    v = val.get(cat) if isinstance(val, dict) else None
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


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return (sum(xs) / len(xs)) if xs else None


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #
def build(pilot_dir: str, refdir: str, sol_path: str, sol_is_standin: bool) -> Dict[str, Any]:
    units, anomalies = _resolve_units(pilot_dir, refdir, sol_path)
    per_turn = {d: [u for u in units if u["design"] == d] for d in ("02", "07")}

    # ================================================================== #
    # 1 : designs 02 & 07 per (design, stratum) — Sol vs A / B / Opus
    # ================================================================== #
    designs_02_07: Dict[str, Any] = {}
    for d in ("02", "07"):
        by_stratum: Dict[str, Any] = {}
        for stratum in sorted({u["stratum"] for u in per_turn[d]}):
            sl = [u for u in per_turn[d] if u["stratum"] == stratum]
            entry = {"overall": _sol_slice_metrics(sl), "per_sut": {}}
            for sut in sorted({u["sut"] for u in sl}):
                entry["per_sut"][sut] = _sol_slice_metrics([u for u in sl if u["sut"] == sut])
            by_stratum[stratum] = entry
        designs_02_07[d] = by_stratum

    # ================================================================== #
    # 2 : disagreement stratum (02, 07) — side-with + joint table + quads
    # ================================================================== #
    disagreement: Dict[str, Any] = {}
    for d in ("02", "07"):
        dis = [u for u in per_turn[d] if u["stratum"] == "disagreement"]
        sw = {"overall": _sol_side_with(dis), "per_sut": {}}
        for sut in sorted({u["sut"] for u in dis}):
            sw["per_sut"][sut] = _sol_side_with([u for u in dis if u["sut"] == sut])
        disagreement[d] = {
            "sol_side_with": sw,
            "joint_referee_table": _joint_referee_table(dis),
            "top8_quadruples": _top8_quads(dis),
        }

    # ================================================================== #
    # 3 : design-07 sensitivity — EXCLUDE the (no keyed text) defect items.
    #     Primary exclusion = every item where Opus was EVER unscorable in the
    #     07 disagreement slice (superset that contains the 3 named defect items);
    #     this is the same slice ra.build uses (n_after == 274). The 3 named items
    #     alone are reported as a secondary "named_defect_only" cut for transparency.
    # ================================================================== #
    unsc_units_07 = [u for u in per_turn["07"] if _state(u["opus"]) == UNSCORABLE]
    opus_ever_unsc_items_07 = {u["item_id"] for u in unsc_units_07}
    d07_dis = [u for u in per_turn["07"] if u["stratum"] == "disagreement"]
    excl_items = opus_ever_unsc_items_07
    d07_dis_excl = [u for u in d07_dis if u["item_id"] not in excl_items]
    d07_dis_excl_named = [u for u in d07_dis if u["item_id"] not in DEFECT_ITEMS_07]

    sensitivity_07 = {
        "note": ("Primary exclusion set = items where Opus was ever 'unscorable' in the "
                 "07 slice (superset containing the 3 named '(no keyed text)' defect items "
                 "WW-07-L02/I04/F02). named_defect_only re-runs with just those 3 excluded."),
        "defect_items_named": sorted(DEFECT_ITEMS_07),
        "excluded_item_ids_primary": sorted(excl_items),
        "n_before": len(d07_dis),
        "n_after_primary": len(d07_dis_excl),
        "n_after_named_defect_only": len(d07_dis_excl_named),
        "sol_side_with_before": _sol_side_with(d07_dis),
        "sol_side_with_after_primary": _sol_side_with(d07_dis_excl),
        "sol_side_with_after_named_defect_only": _sol_side_with(d07_dis_excl_named),
        "joint_referee_table_before": _joint_referee_table(d07_dis),
        "joint_referee_table_after_primary": _joint_referee_table(d07_dis_excl),
        "joint_referee_table_after_named_defect_only": _joint_referee_table(d07_dis_excl_named),
        "per_sut_after_primary": {
            sut: _sol_side_with([u for u in d07_dis_excl if u["sut"] == sut])
            for sut in sorted({u["sut"] for u in d07_dis_excl})},
    }

    # ================================================================== #
    # 4 : design 06 per stratum — Sol deltas vs A / B / Opus
    # ================================================================== #
    six = [u for u in units if u["design"] == "06"]
    design06: Dict[str, Any] = {}
    for stratum in sorted({u["stratum"] for u in six}):
        sl = [u for u in six if u["stratum"] == stratum]

        cat_delta = {"A": {}, "B": {}, "opus": {}}
        for other in ("A", "B", "opus"):
            for cat in PROFILE_CATS:
                ds, n = [], 0
                for u in sl:
                    sc = _cat_float(u["sol"], cat)
                    oc = _cat_float(u[other], cat)
                    if sc is not None and oc is not None:
                        ds.append(sc - oc); n += 1
                cat_delta[other][cat] = {"mean_delta": (sum(ds) / len(ds)) if ds else None,
                                         "n": n}
        avg_delta = {}
        for other in ("A", "B", "opus"):
            vals = [cat_delta[other][c]["mean_delta"] for c in PROFILE_CATS]
            vals = [v for v in vals if v is not None]
            avg_delta[other] = (sum(vals) / len(vals)) if vals else None

        pm_s = [_profile_mean(u["sol"]) for u in sl]
        pm_o = [_profile_mean(u["opus"]) for u in sl]
        pm_a = [_profile_mean(u["A"]) for u in sl]
        pm_b = [_profile_mean(u["B"]) for u in sl]

        def _closer(us):
            ca = cb = eq = nn = 0
            for u in us:
                s = _profile_mean(u["sol"]); a = _profile_mean(u["A"]); b = _profile_mean(u["B"])
                if s is None or a is None or b is None:
                    nn += 1
                    continue
                da_, db_ = abs(s - a), abs(s - b)
                if da_ < db_:
                    ca += 1
                elif db_ < da_:
                    cb += 1
                else:
                    eq += 1
            return {"closer_to_A": ca, "closer_to_B": cb, "equidistant": eq,
                    "n_unscorable_excluded": nn, "n_compared": ca + cb + eq}

        def _sol_opus_absdiff(us):
            diffs, nn = [], 0
            for u in us:
                s = _profile_mean(u["sol"]); o = _profile_mean(u["opus"])
                if s is None or o is None:
                    nn += 1
                    continue
                diffs.append(abs(s - o))
            return {"mean_abs_diff_profile_mean_sol_opus": _mean(diffs),
                    "n_compared": len(diffs), "n_unscorable_excluded": nn}

        n_sol_unscorable = sum(1 for u in sl if not isinstance(u["sol"], dict))
        entry = {
            "n": len(sl),
            "n_sol_unscorable_excluded_from_means": n_sol_unscorable,
            "per_category_mean_delta_sol_minus_A": cat_delta["A"],
            "per_category_mean_delta_sol_minus_B": cat_delta["B"],
            "per_category_mean_delta_sol_minus_opus": cat_delta["opus"],
            "avg_category_delta_sol_minus_A": avg_delta["A"],
            "avg_category_delta_sol_minus_B": avg_delta["B"],
            "avg_category_delta_sol_minus_opus": avg_delta["opus"],
            "mean_profile_mean_sol": _mean(pm_s),
            "mean_profile_mean_opus": _mean(pm_o),
            "mean_profile_mean_A": _mean(pm_a),
            "mean_profile_mean_B": _mean(pm_b),
            "sol_vs_AB_closer_overall": _closer(sl),
            "sol_vs_AB_closer_per_sut": {sut: _closer([u for u in sl if u["sut"] == sut])
                                         for sut in sorted({u["sut"] for u in sl})},
            "sol_vs_opus_profile_absdiff_overall": _sol_opus_absdiff(sl),
            "sol_vs_opus_profile_absdiff_per_sut": {
                sut: _sol_opus_absdiff([u for u in sl if u["sut"] == sut])
                for sut in sorted({u["sut"] for u in sl})},
        }
        design06[stratum] = entry

    # ================================================================== #
    # 5 : Sol unscorable audit (02/07)
    # ================================================================== #
    sol_unsc_units = [u for u in units
                      if u["design"] in PER_TURN_DESIGNS and _state(u["sol"]) == UNSCORABLE]
    by_item: Dict[str, Any] = {}
    for item in sorted({u["item_id"] for u in sol_unsc_units}):
        iu = [u for u in sol_unsc_units if u["item_id"] == item]
        by_item[item] = {
            "design": iu[0]["design"],
            "n": len(iu),
            "A_states": dict(Counter(u["A"] for u in iu).most_common()),
            "B_states": dict(Counter(u["B"] for u in iu).most_common()),
            "opus_states": dict(Counter(_state(u["opus"]) for u in iu).most_common()),
        }
    opus_sol_overlap = sum(1 for u in units
                           if u["design"] in PER_TURN_DESIGNS
                           and _state(u["sol"]) == UNSCORABLE
                           and _state(u["opus"]) == UNSCORABLE)
    sol_unscorable_audit = {
        "n_sol_unscorable_units": len(sol_unsc_units),
        "by_item_id": by_item,
        "opus_and_sol_unscorable_overlap": opus_sol_overlap,
    }

    result = {
        "canary": CANARY,
        "sol_file": sol_path,
        "sol_is_standin_opus": sol_is_standin,
        "n_manifest_units": len(units) + len(anomalies),
        "n_resolved": len(units),
        "n_anomalies": len(anomalies),
        "anomalies": anomalies[:50],
        "designs_02_07_sol_vs_ABO_per_stratum": designs_02_07,
        "disagreement_sol_joint": disagreement,
        "design07_sol_sensitivity": sensitivity_07,
        "design06_sol_per_stratum": design06,
        "sol_unscorable_audit": sol_unscorable_audit,
    }
    return ra._round_floats(result)


# --------------------------------------------------------------------------- #
# printing
# --------------------------------------------------------------------------- #
_fmt = ra._fmt


def print_summary(res: dict) -> None:
    print("=" * 82)
    print(CANARY, "  FOUR-WAY (Opus + Sol vs A=nano + B=llama)")
    print(f"sol_file: {res['sol_file']}"
          f"{'   [STAND-IN = opus self-test]' if res['sol_is_standin_opus'] else ''}")
    print(f"manifest units: {res['n_manifest_units']}   resolved: {res['n_resolved']}   "
          f"anomalies: {res['n_anomalies']}")
    print("=" * 82)

    # 1
    print("\n[1] DESIGNS 02 & 07 — Sol vs A / Sol vs B / Sol vs Opus, per (design, stratum)")
    print("-" * 82)
    hdr = (f"{'slice':<30}{'n':>5}{'rawA':>8}{'rawB':>8}{'rawO':>8}"
           f"{'kA':>8}{'kB':>8}{'kO':>8}")

    def _row(label, m):
        print(f"{label:<30}{m['n']:>5}"
              f"{_fmt(m['raw_agreement_sol_A'],8)}{_fmt(m['raw_agreement_sol_B'],8)}"
              f"{_fmt(m['raw_agreement_sol_opus'],8)}"
              f"{_fmt(m['cohen_kappa_sol_A'],8)}{_fmt(m['cohen_kappa_sol_B'],8)}"
              f"{_fmt(m['cohen_kappa_sol_opus'],8)}")
        if "kappa_notes" in m:
            for kk, nn in m["kappa_notes"].items():
                print(f"      [{kk}] {nn}")

    for d in ("02", "07"):
        for stratum, entry in res["designs_02_07_sol_vs_ABO_per_stratum"][d].items():
            print(f"\ndesign {d} / {stratum}")
            print(hdr)
            _row("  OVERALL", entry["overall"])
            for sut, sm in entry["per_sut"].items():
                _row("    " + sut, sm)

    # 2
    print("\n" + "=" * 82)
    print("[2] DISAGREEMENT STRATUM (02, 07) — Sol side-with + joint referee table")
    print("-" * 82)
    hdr2 = (f"{'slice':<30}{'n':>5}{'withA':>7}{'withB':>7}{'neither':>9}"
            f"{'rA':>8}{'rB':>8}{'rN':>8}")
    for d in ("02", "07"):
        blk = res["disagreement_sol_joint"][d]
        sw = blk["sol_side_with"]
        print(f"\ndesign {d} — Sol side-with")
        print(hdr2)
        m = sw["overall"]
        print(f"{'  OVERALL':<30}{m['n']:>5}{m['sides_with_A']:>7}{m['sides_with_B']:>7}"
              f"{m['sides_with_neither']:>9}{_fmt(m['sides_with_A_rate'],8)}"
              f"{_fmt(m['sides_with_B_rate'],8)}{_fmt(m['sides_with_neither_rate'],8)}")
        for sut, sm in sw["per_sut"].items():
            print(f"{'    '+sut:<30}{sm['n']:>5}{sm['sides_with_A']:>7}{sm['sides_with_B']:>7}"
                  f"{sm['sides_with_neither']:>9}{_fmt(sm['sides_with_A_rate'],8)}"
                  f"{_fmt(sm['sides_with_B_rate'],8)}{_fmt(sm['sides_with_neither_rate'],8)}")
        jt = blk["joint_referee_table"]
        print(f"\ndesign {d} — joint referee table (n={jt['n']}, cells_sum={jt['cells_sum']}, "
              f"sum==n: {jt['cells_sum_equals_n']}, sol<->opus raw={_fmt(jt['raw_agreement_sol_opus'],0).strip()})")
        for k, v in jt["cells"].items():
            extra = ""
            if k == "opus_side_sol_neither":
                extra = f"   sider={jt['opus_side_sol_neither_sider']}"
            elif k == "sol_side_opus_neither":
                extra = f"   sider={jt['sol_side_opus_neither_sider']}"
            print(f"    {k:<26}{v:>5}{extra}")
        print(f"\ndesign {d} — top-8 (A, B, opus, sol) quadruples")
        print(f"    {'A':<20}{'B':<20}{'opus':<20}{'sol':<20}{'count':>6}")
        for q in blk["top8_quadruples"]:
            print(f"    {q['A_state']:<20}{q['B_state']:<20}{q['opus_state']:<20}"
                  f"{q['sol_state']:<20}{q['count']:>6}")

    # 3
    print("\n" + "=" * 82)
    print("[3] DESIGN-07 SENSITIVITY — exclude '(no keyed text)' defect items")
    print("-" * 82)
    s = res["design07_sol_sensitivity"]
    print(f"  primary excluded item_ids: {s['excluded_item_ids_primary']}")
    print(f"  n_before={s['n_before']}  n_after_primary={s['n_after_primary']}  "
          f"n_after_named_defect_only={s['n_after_named_defect_only']}")
    for lbl, key in (("BEFORE", "sol_side_with_before"),
                     ("AFTER(primary)", "sol_side_with_after_primary"),
                     ("AFTER(named3)", "sol_side_with_after_named_defect_only")):
        m = s[key]
        print(f"    {lbl:<16} n={m['n']:>3}  withA={m['sides_with_A']}"
              f"({_fmt(m['sides_with_A_rate'],0).strip()})  withB={m['sides_with_B']}"
              f"({_fmt(m['sides_with_B_rate'],0).strip()})  neither={m['sides_with_neither']}"
              f"({_fmt(m['sides_with_neither_rate'],0).strip()})")
    jt = s["joint_referee_table_after_primary"]
    print(f"  joint table AFTER(primary) n={jt['n']} cells_sum={jt['cells_sum']} "
          f"sum==n:{jt['cells_sum_equals_n']}")
    for k, v in jt["cells"].items():
        print(f"    {k:<26}{v:>5}")

    # 4
    print("\n" + "=" * 82)
    print("[4] DESIGN 06 — Sol per-category deltas vs A / B / Opus, per stratum")
    print("-" * 82)
    for stratum, e in res["design06_sol_per_stratum"].items():
        print(f"\ndesign 06 / {stratum}  (n={e['n']}, "
              f"sol_unscorable_excluded={e['n_sol_unscorable_excluded_from_means']})")
        print(f"  {'category':<14}{'d(S-A)':>10}{'d(S-B)':>10}{'d(S-O)':>10}")
        for cat in PROFILE_CATS:
            da = e["per_category_mean_delta_sol_minus_A"][cat]["mean_delta"]
            db = e["per_category_mean_delta_sol_minus_B"][cat]["mean_delta"]
            do = e["per_category_mean_delta_sol_minus_opus"][cat]["mean_delta"]
            print(f"  {cat:<14}{_fmt(da,10)}{_fmt(db,10)}{_fmt(do,10)}")
        print(f"  {'AVG':<14}{_fmt(e['avg_category_delta_sol_minus_A'],10)}"
              f"{_fmt(e['avg_category_delta_sol_minus_B'],10)}"
              f"{_fmt(e['avg_category_delta_sol_minus_opus'],10)}")
        print(f"  profile_mean:  Sol={_fmt(e['mean_profile_mean_sol'],0).strip()}  "
              f"Opus={_fmt(e['mean_profile_mean_opus'],0).strip()}  "
              f"A={_fmt(e['mean_profile_mean_A'],0).strip()}  "
              f"B={_fmt(e['mean_profile_mean_B'],0).strip()}")
        c = e["sol_vs_AB_closer_overall"]
        print(f"  Sol closer-to (|S-A| vs |S-B|): A={c['closer_to_A']}  B={c['closer_to_B']}  "
              f"eq={c['equidistant']}  (n_compared={c['n_compared']}, "
              f"unscorable_excluded={c['n_unscorable_excluded']})")
        ad = e["sol_vs_opus_profile_absdiff_overall"]
        print(f"  Sol-vs-Opus mean |Δ profile_mean| = "
              f"{_fmt(ad['mean_abs_diff_profile_mean_sol_opus'],0).strip()} "
              f"(n={ad['n_compared']})")
        for sut, cs in e["sol_vs_AB_closer_per_sut"].items():
            print(f"    {sut:<22} closerA={cs['closer_to_A']}  closerB={cs['closer_to_B']}  "
                  f"eq={cs['equidistant']}  (n={cs['n_compared']})")

    # 5
    print("\n" + "=" * 82)
    print("[5] SOL-UNSCORABLE AUDIT (02/07)")
    print("-" * 82)
    ua = res["sol_unscorable_audit"]
    print(f"total sol-unscorable sampled units: {ua['n_sol_unscorable_units']}")
    print(f"opus∩sol unscorable overlap: {ua['opus_and_sol_unscorable_overlap']}")
    print(f"  {'item_id':<16}{'design':<8}{'n':>4}   A / B / opus states")
    for item, info in ua["by_item_id"].items():
        print(f"  {item:<16}{info['design']:<8}{info['n']:>4}   "
              f"A={info['A_states']}  B={info['B_states']}  opus={info['opus_states']}")

    print("\n" + "=" * 82)
    if res["n_anomalies"]:
        print(f"JOIN ANOMALIES: {res['n_anomalies']}")
        for a in res["anomalies"]:
            print("  ", a)
    else:
        print("JOIN ANOMALIES: none (all sampled units resolved to opus+sol+A+B)")
    print("=" * 82)


def main() -> None:
    ap = argparse.ArgumentParser(description="JR-referee FOUR-way agreement (offline).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--ref-dir", default="logs/jr-referee-20260716")
    ap.add_argument("--sol-file", default="logs/jr-referee-20260716/sol-verdicts.jsonl",
                    help="Sol verdicts jsonl (schema == opus-verdicts.jsonl). "
                         "Use opus-verdicts.jsonl as a stand-in self-test while Sol is in flight.")
    ap.add_argument("--out", default=None,
                    help="output json path (default: <ref-dir>/referee-agreement-sol.json)")
    args = ap.parse_args()

    sol_path = args.sol_file
    if not os.path.isabs(sol_path) and not os.path.exists(sol_path):
        # allow ref-dir-relative bare filename convenience
        cand = os.path.join(args.ref_dir, os.path.basename(sol_path))
        if os.path.exists(cand):
            sol_path = cand
    if not os.path.exists(sol_path):
        sys.exit(f"ERROR: --sol-file not found: {sol_path}\n"
                 f"(The Sol run may still be in flight. Use --sol-file "
                 f"logs/jr-referee-20260716/opus-verdicts.jsonl for the stand-in self-test.)")

    sol_is_standin = os.path.realpath(sol_path) == os.path.realpath(
        os.path.join(args.ref_dir, "opus-verdicts.jsonl"))

    res = build(args.pilot_dir, args.ref_dir, sol_path, sol_is_standin)
    out_path = args.out or os.path.join(args.ref_dir, "referee-agreement-sol.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=2, ensure_ascii=False)
    print_summary(res)
    print(f"\nwrote -> {out_path}")


if __name__ == "__main__":
    main()
