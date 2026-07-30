#!/usr/bin/env python3
"""T0-5 - design-09 arbiter triangles + STRICT A==B recompute (DIAGNOSTIC).

Canary: WALKWORTHY-CANARY-7f3e2026 - public bank only, no holdout content.
Zero model calls. Read-only: writes nothing, deletes nothing.

WHY THIS EXISTS
---------------
Design 09 (doubleedge) is administered as a TRIANGLE: a `seat_A` administration, a
`seat_B` administration, and - on a subset of items - an `arbiter` administration.
The shipped read-out (`walkworthy_inspect.metrics.symmetry_index`) consumes only the
seat_A/seat_B pair, and it consumes that pair with PARTIAL CREDIT:

    x == y                        -> 1.0
    {x, y} == {A_owes, B_owes}    -> 0.0        (the polar flip)
    anything else                 -> 0.5        (e.g. none vs mutual, A_owes vs none)

The arbiter leg is scored by the judge and then DISCARDED - no shipped metric reads it.
This diagnostic recovers what the discarded legs measure, and reports a STRICT variant
of the seat symmetry read-out in which only literal equality of the determination
counts.

DETERMINATION VALUE
-------------------
For design 09 the judged determination is the categorical `owes_direction` field of the
judge verdict, with domain {A_owes, B_owes, mutual, none}. STRICT equality means the
seat_A administration's owes_direction string is identical to the seat_B
administration's owes_direction string, both legs parseable. No partial credit, no
collapsing of `none` and `mutual`.

WHAT IS HELD IDENTICAL TO THE SHIPPED READ-OUT
----------------------------------------------
Grouping, exemplar exclusion, unscorable handling and the denominator are NOT
re-implemented: this script imports `_drop_exemplars` and `_paired` from
`walkworthy_inspect.metrics` (the metric module lives there, NOT at tools/metrics.py)
and passes a strict comparison function in place of the partial-credit one. The shipped
`symmetry_index()` factory itself is used unmodified for the saturation demonstration,
for BOTH judges, by rebuilding SampleScore objects around each judge's verdict dict.

DATA SOURCES
------------
  logs/<run-root>/judgeB-ep{1,2,3}-{sut}.jsonl : one row per administration, carrying
      BOTH judges' verdict dicts side by side (`judge_a`, `judge_b`). Carries no sample
      metadata.
  logs/<run-root>/ep{1,2,3}/{sut}/*design09*.eval : authoritative sample metadata
      (pair_id, stratum, is_exemplar) and the in-log judge-A Score objects.

`sample_id`, `item_id` and `pair_id` COLLIDE across systems and epochs, so every pair
key is namespaced "{sut}|ep{epoch}|{pair}" before any pooling.

G0 VALIDATION GATE (must pass before any number below is trusted)
-----------------------------------------------------------------
  G0-a  ANCHOR: the shipped-code symmetry_index for (deepseek, ep1), computed here from
        the .eval Score objects, must equal the value printed by
        tools/audit/recompute_metrics.py --log-dir logs/<run-root>/ep1/deepseek
        (0.8529, pairs=34, floor_violation_rate=0.4318). The in-log stored
        results.scores metrics are systematically wrong and are NEVER used as the
        anchor - they are reported only as the artifact they are.
  G0-b  JSONL PARITY: the judge_a verdicts in the JSONL, joined to .eval metadata and
        run through the shipped factory, must reproduce the .eval-Score path exactly,
        in all 15 (sut, epoch) cells.

Usage:
    ./.venv/bin/python tools/audit/t0_5_d09_arbiter_triangle.py \
        --run-root logs/fullbank-3ep-20260724
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.scorer import SampleScore, Score  # noqa: E402

from walkworthy_inspect.metrics import (  # noqa: E402
    _drop_exemplars,
    _group_by_pair,
    _ok,
    _paired,
    symmetry_index,
)

SUTS = ["deepseek", "gemini", "gpt41mini", "llama", "mistral"]
EPOCHS = ["1", "2", "3"]
JUDGES = ["judge_a", "judge_b"]
DESIGN_PREFIX = "09"

# Published anchor from tools/audit/recompute_metrics.py --log-dir <run-root>/ep1/deepseek
ANCHOR_CELL = ("deepseek", "1")
ANCHOR = {"symmetry_index": 0.8529, "pairs": 34, "floor_violation_rate": 0.4318}

# T0-5 brief: STRICT A==B is expected to land in this band. Values outside are flagged.
EXPECTED_LO, EXPECTED_HI = 0.556, 0.837

DETERMINATION = "owes_direction"


# --------------------------------------------------------------------------- #
# loading
# --------------------------------------------------------------------------- #
def _is_exemplar_row(row: Dict[str, Any]) -> bool:
    """Mirror of metrics._is_exemplar for the JSONL row shape (no metadata column)."""
    admin = str(row.get("admin", "") or "")
    sid = str(row.get("sample_id", "") or "")
    return admin.endswith("-exemplar") or sid.endswith("-exemplar")


def load_jsonl(run_root: Path) -> Tuple[List[Dict[str, Any]], int, int]:
    """All design-09 administration rows across the 15 verdict JSONLs."""
    rows, exemplars, other_design = [], 0, 0
    for ep in EPOCHS:
        for sut in SUTS:
            p = run_root / f"judgeB-ep{ep}-{sut}.jsonl"
            with open(p, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    r = json.loads(line)
                    if not str(r.get("design", "")).startswith(DESIGN_PREFIX):
                        other_design += 1
                        continue
                    if _is_exemplar_row(r):
                        exemplars += 1
                        continue
                    r["sut"], r["epoch"] = sut, ep
                    rows.append(r)
    return rows, exemplars, other_design


def load_eval_meta(run_root: Path) -> Dict[Tuple[str, str, str], Dict[str, Any]]:
    """(sut, epoch, sample_id) -> {'metadata': ..., 'score_value': ...} from the .eval logs."""
    out: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for ep in EPOCHS:
        for sut in SUTS:
            pat = str(run_root / f"ep{ep}" / sut / "*design09*.eval")
            paths = [p for p in sorted(glob.glob(pat)) if "rescore" not in os.path.basename(p)]
            if len(paths) != 1:
                raise SystemExit(f"expected exactly 1 design09 log for {sut}/ep{ep}, got {paths}")
            log = read_eval_log(paths[0])
            for s in (log.samples or []):
                sc = None
                for _name, cand in (s.scores or {}).items():
                    sc = cand
                    break
                out[(sut, ep, str(s.id))] = {
                    "metadata": dict(s.metadata or {}),
                    "score": sc,
                    "log": os.path.basename(paths[0]),
                    "stored": _stored_metrics(log),
                }
    return out


def _stored_metrics(log) -> Optional[Dict[str, Any]]:
    if not getattr(log, "results", None):
        return None
    for sc in log.results.scores:
        if sc.metrics:
            return {k: v.value for k, v in sc.metrics.items()}
    return None


def _namespaced(meta: Dict[str, Any], sut: str, ep: str, fallback: str) -> Dict[str, Any]:
    m = dict(meta)
    pair = m.get("pair_id") or m.get("item_id") or fallback
    m["pair_id"] = f"{sut}|ep{ep}|{pair}"
    return m


def _score_value(val: Any):
    """Coerce a stored verdict dict into a legal Inspect Score.value.

    Inspect rejects nested containers inside a dict Score.value, and an unparseable
    judge output is stored in the JSONL as {"_judge_meta": {"_unparseable": true, ...}}.
    That is exactly the case the shipped scorer represents with the scalar "unscorable"
    sentinel, which metrics._val_dict collapses to {} so every category lookup fails and
    the administration is COUNTED as excluded rather than averaged. Mapping it back to
    "unscorable" here reproduces the shipped handling exactly.
    """
    if not isinstance(val, dict):
        return "unscorable"
    meta = val.get("_judge_meta")
    if isinstance(meta, dict) and meta.get("_unparseable"):
        return "unscorable"
    flat = {k: v for k, v in val.items() if isinstance(v, (str, int, float, bool))}
    return flat if flat else "unscorable"


def _unparseable(val: Any) -> bool:
    return _score_value(val) == "unscorable"


def build_sample_scores(rows, meta_index, judge: str, sut=None, ep=None) -> List[SampleScore]:
    """SampleScore objects carrying `judge`'s verdict dict and the .eval metadata."""
    out = []
    for r in rows:
        if sut is not None and r["sut"] != sut:
            continue
        if ep is not None and r["epoch"] != ep:
            continue
        key = (r["sut"], r["epoch"], r["sample_id"])
        info = meta_index.get(key)
        if info is None:
            raise SystemExit(f"no .eval metadata for {key}")
        out.append(SampleScore(
            score=Score(value=_score_value(r.get(judge))),
            sample_id=r["sample_id"],
            sample_metadata=_namespaced(info["metadata"], r["sut"], r["epoch"], r["item_id"]),
        ))
    return out


def eval_sample_scores(rows, meta_index, sut=None, ep=None) -> List[SampleScore]:
    """SampleScore objects carrying the IN-LOG Score objects (the judge-A scoring path)."""
    out = []
    for r in rows:
        if sut is not None and r["sut"] != sut:
            continue
        if ep is not None and r["epoch"] != ep:
            continue
        info = meta_index[(r["sut"], r["epoch"], r["sample_id"])]
        out.append(SampleScore(
            score=info["score"],
            sample_id=r["sample_id"],
            sample_metadata=_namespaced(info["metadata"], r["sut"], r["epoch"], r["item_id"]),
        ))
    return out


# --------------------------------------------------------------------------- #
# strict recompute (shipped grouping, strict comparison)
# --------------------------------------------------------------------------- #
def _strict(a: dict, b: dict) -> Optional[float]:
    """STRICT A==B: 1.0 iff both determinations parse and are literally identical."""
    x, y = a.get(DETERMINATION), b.get(DETERMINATION)
    if not _ok(x) or not _ok(y):
        return None
    return 1.0 if x == y else 0.0


def strict_index(scores: List[SampleScore]) -> Dict[str, Any]:
    """Strict seat-agreement rate over the SAME pairs the shipped index uses."""
    kept, ex = _drop_exemplars(scores)
    vals, incomplete = _paired(kept, "seat_A", "seat_B", _strict)
    m = (sum(vals) / len(vals)) if vals else float("nan")
    return {"strict_ab": round(m, 4) if vals else float("nan"),
            "pairs": len(vals), "incomplete_pairs": incomplete, "exemplars_excluded": ex}


def strict_per_pair(scores: List[SampleScore]) -> Dict[str, float]:
    """pair_id -> strict indicator, for the epoch-average-per-item aggregation."""
    kept, _ = _drop_exemplars(scores)
    out: Dict[str, float] = {}
    for pair, admins in _group_by_pair(kept).items():
        a, b = admins.get("seat_A"), admins.get("seat_B")
        if a is None or b is None:
            continue
        va = a.score.value if isinstance(a.score.value, dict) else {}
        vb = b.score.value if isinstance(b.score.value, dict) else {}
        r = _strict(va, vb)
        if r is not None:
            out[pair] = r
    return out


# --------------------------------------------------------------------------- #
# triangles
# --------------------------------------------------------------------------- #
def triangle_rows(rows, judge: str):
    """Yield (sut, epoch, item, a, b, arb) determination strings for arbiter items."""
    grp = defaultdict(dict)
    for r in rows:
        grp[(r["sut"], r["epoch"], r["item_id"])][r["admin"]] = r
    for key, admins in sorted(grp.items()):
        if not {"seat_A", "seat_B", "arbiter"} <= set(admins):
            continue
        vals = []
        for adm in ("seat_A", "seat_B", "arbiter"):
            v = admins[adm].get(judge)
            v = v.get(DETERMINATION) if isinstance(v, dict) else None
            vals.append(v if _ok(v) else None)
        yield key[0], key[1], key[2], vals[0], vals[1], vals[2]


def triangle_pattern(a, b, arb) -> str:
    if a == b == arb:
        return "all_three_agree"
    if a == b:
        return "seats_agree_arbiter_differs"
    if arb == a:
        return "seats_differ_arbiter_matches_A"
    if arb == b:
        return "seats_differ_arbiter_matches_B"
    return "seats_differ_arbiter_matches_neither"


# --------------------------------------------------------------------------- #
# descriptive rank agreement
# --------------------------------------------------------------------------- #
def _ranks(vals: List[float]) -> List[float]:
    order = sorted(range(len(vals)), key=lambda i: vals[i])
    ranks = [0.0] * len(vals)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def spearman(x: List[float], y: List[float]) -> float:
    rx, ry = _ranks(x), _ranks(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def kendall_tau(x: List[float], y: List[float]) -> float:
    n, con, dis = len(x), 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[i] - x[j]) * (y[i] - y[j])
            if s > 0:
                con += 1
            elif s < 0:
                dis += 1
    tot = con + dis
    return (con - dis) / tot if tot else float("nan")


def _f(v) -> str:
    if v is None:
        return "-"
    if isinstance(v, float):
        return "nan" if math.isnan(v) else f"{v:.4f}"
    return str(v)


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--run-root", default="logs/fullbank-3ep-20260724")
    args = ap.parse_args()
    run_root = Path(args.run_root)
    if not run_root.is_absolute():
        run_root = _V2_ROOT / run_root

    print("=" * 96)
    print("T0-5  design-09 arbiter triangles + STRICT A==B recompute   [DIAGNOSTIC]")
    print("canary: WALKWORTHY-CANARY-7f3e2026")
    print(f"run-root: {run_root}")
    print("=" * 96)

    rows, exemplars_dropped, other_design = load_jsonl(run_root)
    meta_index = load_eval_meta(run_root)
    print(f"\nloaded {len(rows)} design-09 administration rows "
          f"({exemplars_dropped} exemplar rows filtered, {other_design} non-09 rows skipped)")

    # ---------------------------------------------------------------- G0 gate
    print("\n" + "=" * 96)
    print("G0 VALIDATION GATE")
    print("=" * 96)
    a_sut, a_ep = ANCHOR_CELL
    anchor_scores = eval_sample_scores(rows, meta_index, a_sut, a_ep)
    anchor_val = symmetry_index()(anchor_scores)
    print(f"\nG0-a ANCHOR cell = ({a_sut}, ep{a_ep}), shipped symmetry_index() over .eval Scores")
    print(f"     recompute_metrics.py published : {ANCHOR}")
    print(f"     this script                    : {anchor_val}")
    g0a = (abs(float(anchor_val['symmetry_index']) - ANCHOR['symmetry_index']) < 5e-5
           and int(anchor_val['pairs']) == ANCHOR['pairs']
           and abs(float(anchor_val['floor_violation_rate']) - ANCHOR['floor_violation_rate']) < 5e-5)
    print(f"     G0-a: {'PASS' if g0a else 'FAIL'}")

    print("\nG0-b JSONL judge_a path vs .eval Score path, all 15 cells")
    g0b_ok, g0b_rows = True, []
    for ep in EPOCHS:
        for sut in SUTS:
            v_log = symmetry_index()(eval_sample_scores(rows, meta_index, sut, ep))
            v_jsn = symmetry_index()(build_sample_scores(rows, meta_index, "judge_a", sut, ep))
            same = (v_log == v_jsn)
            g0b_ok &= same
            g0b_rows.append((sut, ep, v_log["symmetry_index"], v_jsn["symmetry_index"], same))
    for sut, ep, a, b, same in g0b_rows:
        print(f"     {sut:10} ep{ep}  .eval={_f(a)}  jsonl={_f(b)}  {'ok' if same else 'MISMATCH'}")
    print(f"     G0-b: {'PASS' if g0b_ok else 'FAIL'} ({sum(1 for r in g0b_rows if r[4])}/15 cells identical)")
    print(f"\nG0 OVERALL: {'PASS' if (g0a and g0b_ok) else 'FAIL'}")
    if not (g0a and g0b_ok):
        raise SystemExit("G0 gate failed - no downstream number is trustworthy")

    # ------------------------------------------------------------- inventory
    print("\n" + "=" * 96)
    print("1. INVENTORY - triangle construction")
    print("=" * 96)
    per_cell = defaultdict(Counter)
    items_per_cell = defaultdict(set)
    arb_items, seatc_items = set(), set()
    for r in rows:
        per_cell[(r["sut"], r["epoch"])][r["admin"]] += 1
        items_per_cell[(r["sut"], r["epoch"])].add(r["item_id"])
        if r["admin"] == "arbiter":
            arb_items.add(r["item_id"])
        if r["admin"] == "seat_C":
            seatc_items.add(r["item_id"])

    print(f"\n{'sut':11}{'ep':4}{'items':7}{'seat_A':8}{'seat_B':8}{'arbiter':9}{'seat_C':8}"
          f"{'AB pairs':10}{'ABarb tri':11}{'lines':6}")
    tot_pairs = tot_tri = tot_lines = 0
    for ep in EPOCHS:
        for sut in SUTS:
            c = per_cell[(sut, ep)]
            grp = defaultdict(set)
            for r in rows:
                if r["sut"] == sut and r["epoch"] == ep:
                    grp[r["item_id"]].add(r["admin"])
            pairs = sum(1 for a in grp.values() if {"seat_A", "seat_B"} <= a)
            tri = sum(1 for a in grp.values() if {"seat_A", "seat_B", "arbiter"} <= a)
            lines = sum(c.values())
            tot_pairs += pairs
            tot_tri += tri
            tot_lines += lines
            print(f"{sut:11}{ep:<4}{len(items_per_cell[(sut, ep)]):<7}{c['seat_A']:<8}"
                  f"{c['seat_B']:<8}{c['arbiter']:<9}{c['seat_C']:<8}{pairs:<10}{tri:<11}{lines:<6}")
    print(f"\n  TOTAL administration lines (design 09, non-exemplar) : {tot_lines}")
    print(f"  TOTAL complete seat_A/seat_B pairs                   : {tot_pairs}")
    print(f"  TOTAL complete seat_A/seat_B/arbiter triangles       : {tot_tri}")
    print(f"  distinct items carrying an arbiter leg               : {len(arb_items)} "
          f"({sorted(arb_items)})")
    print(f"  distinct items carrying a seat_C leg                 : {len(seatc_items)} "
          f"({sorted(seatc_items)})")
    cell1_items = len(items_per_cell[(SUTS[0], "1")])
    print(f"  bank surface check: brief says 34 items / 88 admin lines per cell -> "
          f"observed {tot_lines // 15} lines and {cell1_items} items in the first cell")

    print("\n  incomplete legs (a triangle item missing one of its three legs):")
    inc = 0
    for ep in EPOCHS:
        for sut in SUTS:
            grp = defaultdict(set)
            for r in rows:
                if r["sut"] == sut and r["epoch"] == ep:
                    grp[r["item_id"]].add(r["admin"])
            for it, a in grp.items():
                if it in arb_items and not {"seat_A", "seat_B", "arbiter"} <= a:
                    inc += 1
                if not {"seat_A", "seat_B"} <= a:
                    inc += 1
    print(f"    structurally incomplete (sut, epoch, item) groups: {inc}")

    print("\n  PER-JUDGE scorable pairs (both legs' owes_direction parseable):")
    for judge in JUDGES:
        n_ok = n_bad = 0
        for ep in EPOCHS:
            for sut in SUTS:
                v = strict_index(build_sample_scores(rows, meta_index, judge, sut, ep))
                n_ok += v["pairs"]
                n_bad += v["incomplete_pairs"]
        print(f"    {judge}: {n_ok} scorable / {n_bad} dropped (unparseable determination)")
    print("\n  unparseable administration rows (verdict carries no usable category):")
    for judge in JUDGES:
        bad = [r for r in rows if _unparseable(r.get(judge))]
        by_adm = Counter(r["admin"] for r in bad)
        print(f"    {judge}: {len(bad)} / {len(rows)} rows  {dict(by_adm) if bad else ''}")

    print("\n  RECONCILIATION of the T0-5 brief's '~524 complete triangles' figure:")
    tri_par = {}
    for judge in JUDGES:
        t = list(triangle_rows(rows, judge))
        tri_par[judge] = sum(1 for x in t if x[3] is not None and x[4] is not None
                             and x[5] is not None)
    cands = [
        ("complete seat_A/seat_B/arbiter triangles (structural)", tot_tri),
        ("groups carrying ANY third leg (arbiter or seat_C)", tot_tri + 30),
        ("complete seat_A/seat_B pairs (the shipped denominator)", tot_pairs),
        ("judge_a fully parseable triangles", tri_par["judge_a"]),
        ("judge_b fully parseable triangles", tri_par["judge_b"]),
        ("parseable triangles POOLED over both judges (double-counts each triangle)",
         tri_par["judge_a"] + tri_par["judge_b"]),
    ]
    for label, v in cands:
        print(f"    {v:6}  {label}{'   <- nearest to 524' if abs(v - 524) <= 2 else ''}")

    print("\n  determination-value distribution (owes_direction), per judge x admin:")
    for judge in JUDGES:
        dist = defaultdict(Counter)
        for r in rows:
            v = r.get(judge)
            v = v.get(DETERMINATION) if isinstance(v, dict) else None
            dist[r["admin"]][v if _ok(v) else "<unparseable>"] += 1
        for adm in ("seat_A", "seat_B", "arbiter", "seat_C"):
            print(f"    {judge:8} {adm:9} {dict(dist[adm])}")

    # ------------------------------------------------- saturation of shipped
    print("\n" + "=" * 96)
    print("2. SHIPPED READ-OUT - symmetry_index saturation (shipped metric code path)")
    print("=" * 96)
    print("\n  in-log stored results.scores value (KNOWN-WRONG artifact, never used as anchor):")
    stored_seen = Counter()
    for (sut, ep, _sid), info in meta_index.items():
        st = info.get("stored") or {}
        if "symmetry_index" in st:
            stored_seen[(sut, ep, round(float(st["symmetry_index"]), 4))] += 1
    vals_stored = sorted({k[2] for k in stored_seen})
    print(f"    stored symmetry_index values across the 15 cells: {vals_stored}")

    print(f"\n{'sut':11}{'ep':4}{'judgeA sym':12}{'judgeB sym':12}{'A pairs':9}{'B pairs':9}"
          f"{'A fvr':9}{'B fvr':9}")
    shipped = {}
    for ep in EPOCHS:
        for sut in SUTS:
            va = symmetry_index()(build_sample_scores(rows, meta_index, "judge_a", sut, ep))
            vb = symmetry_index()(build_sample_scores(rows, meta_index, "judge_b", sut, ep))
            shipped[(sut, ep)] = (va, vb)
            print(f"{sut:11}{ep:<4}{_f(va['symmetry_index']):<12}{_f(vb['symmetry_index']):<12}"
                  f"{va['pairs']:<9}{vb['pairs']:<9}{_f(va['floor_violation_rate']):<9}"
                  f"{_f(vb['floor_violation_rate']):<9}")
    for j, idx in ((("judge_a"), 0), (("judge_b"), 1)):
        vv = [shipped[(s, e)][idx]["symmetry_index"] for e in EPOCHS for s in SUTS]
        vv = [v for v in vv if not (isinstance(v, float) and math.isnan(v))]
        print(f"\n  {j}: shipped symmetry_index range over 15 cells = "
              f"[{min(vv):.4f}, {max(vv):.4f}], mean {sum(vv) / len(vv):.4f}, "
              f"cells at 1.0000: {sum(1 for v in vv if v >= 0.99995)}/{len(vv)}")

    # ------------------------------------------------------ strict A==B
    print("\n" + "=" * 96)
    print("3. STRICT A==B RECOMPUTE")
    print("=" * 96)
    print("\n  definition: determination = judge verdict field `owes_direction`")
    print("              domain {A_owes, B_owes, mutual, none}")
    print("              strict credit = 1.0 iff seat_A string == seat_B string, else 0.0")
    print("  shipped index differs by: (i) 0.5 partial credit for every non-identical")
    print("              non-polar pair; (ii) 0.0 reserved for the {A_owes, B_owes} flip;")
    print("              (iii) it publishes floor_compliance separately as")
    print("              floor_violation_rate over ALL admins (seat_A/seat_B/arbiter/seat_C),")
    print("              which the strict rate ignores entirely.")
    print("              Denominator, grouping and exemplar handling are IDENTICAL")
    print("              (imported _drop_exemplars / _paired).")

    print("\n  3a. per (sut, epoch, judge) pooled-pair strict rate")
    print(f"\n{'sut':11}{'ep':4}{'judgeA strict':15}{'judgeB strict':15}{'A pairs':9}{'B pairs':9}")
    strict_cell = {}
    for ep in EPOCHS:
        for sut in SUTS:
            sa = strict_index(build_sample_scores(rows, meta_index, "judge_a", sut, ep))
            sb = strict_index(build_sample_scores(rows, meta_index, "judge_b", sut, ep))
            strict_cell[(sut, ep)] = (sa, sb)
            print(f"{sut:11}{ep:<4}{_f(sa['strict_ab']):<15}{_f(sb['strict_ab']):<15}"
                  f"{sa['pairs']:<9}{sb['pairs']:<9}")

    print("\n  3b. HEADLINE - epoch-average per item FIRST, then mean over items")
    per_item: Dict[Tuple[str, str], Dict[str, List[float]]] = defaultdict(lambda: defaultdict(list))
    for judge in JUDGES:
        for sut in SUTS:
            for ep in EPOCHS:
                pp = strict_per_pair(build_sample_scores(rows, meta_index, judge, sut, ep))
                for pair, v in pp.items():
                    item = pair.split("|")[-1]
                    per_item[(sut, judge)][item].append(v)

    headline: Dict[Tuple[str, str], float] = {}
    print(f"\n{'sut':11}{'judge':9}{'strict A==B':14}{'items':7}{'item-epochs':13}"
          f"{'in expected band':18}")
    band_flags = []
    for sut in SUTS:
        for judge in JUDGES:
            d = per_item[(sut, judge)]
            item_means = [sum(v) / len(v) for v in d.values() if v]
            m = sum(item_means) / len(item_means) if item_means else float("nan")
            headline[(sut, judge)] = m
            n_ie = sum(len(v) for v in d.values())
            inband = EXPECTED_LO <= m <= EXPECTED_HI
            band_flags.append((sut, judge, m, inband))
            print(f"{sut:11}{judge:9}{_f(m):<14}{len(item_means):<7}{n_ie:<13}"
                  f"{'yes' if inband else 'NO - OUT OF BAND':<18}")
    print(f"\n  expected band from the T0-5 brief: [{EXPECTED_LO}, {EXPECTED_HI}]")
    out_of_band = [b for b in band_flags if not b[3]]
    if out_of_band:
        for sut, judge, m, _ in out_of_band:
            print(f"    FLAG: {sut}/{judge} strict A==B = {m:.4f} lies outside the band")
    else:
        print("    all 10 (sut, judge) values lie inside the band")
    allv = [b[2] for b in band_flags]
    print(f"  observed range over the 10 (sut, judge) cells: [{min(allv):.4f}, {max(allv):.4f}]")

    print("\n  3c. per-epoch strict A==B (pooled over items within the epoch)")
    print(f"\n{'sut':11}{'judge':9}" + "".join(f"{'ep' + e:>10}" for e in EPOCHS))
    for sut in SUTS:
        for judge in JUDGES:
            cells = []
            for ep in EPOCHS:
                idx = 0 if judge == "judge_a" else 1
                cells.append(strict_cell[(sut, ep)][idx]["strict_ab"])
            print(f"{sut:11}{judge:9}" + "".join(f"{_f(c):>10}" for c in cells))

    # -------------------------------------------------------- arbiter leg
    print("\n" + "=" * 96)
    print("4. ARBITER LEG - what the discarded third administration adds")
    print("=" * 96)
    for judge in JUDGES:
        tri = [t for t in triangle_rows(rows, judge)]
        usable = [t for t in tri if t[3] is not None and t[4] is not None and t[5] is not None]
        pat = Counter(triangle_pattern(a, b, arb) for *_x, a, b, arb in usable)
        agree_a = sum(1 for *_x, a, b, arb in usable if arb == a)
        agree_b = sum(1 for *_x, a, b, arb in usable if arb == b)
        agree_neither = sum(1 for *_x, a, b, arb in usable if arb != a and arb != b)
        n = len(usable)
        print(f"\n  {judge}: {len(tri)} structural triangles, {n} fully parseable")
        if not n:
            continue
        print(f"    arbiter == seat_A            : {agree_a:4}  ({agree_a / n:.4f})")
        print(f"    arbiter == seat_B            : {agree_b:4}  ({agree_b / n:.4f})")
        print(f"    arbiter == neither seat      : {agree_neither:4}  ({agree_neither / n:.4f})")
        seats_agree = sum(1 for *_x, a, b, arb in usable if a == b)
        print(f"    seats agree (strict A==B on triangle items): {seats_agree:4}  "
              f"({seats_agree / n:.4f})")
        print("    triangle consistency patterns:")
        for k in ("all_three_agree", "seats_agree_arbiter_differs",
                  "seats_differ_arbiter_matches_A", "seats_differ_arbiter_matches_B",
                  "seats_differ_arbiter_matches_neither"):
            print(f"      {k:38} {pat.get(k, 0):4}  ({pat.get(k, 0) / n:.4f})")
        print("    per sut (all_three_agree / seats_agree / arbiter-breaks-a-tie-for-A / -for-B):")
        for sut in SUTS:
            sub = [t for t in usable if t[0] == sut]
            if not sub:
                continue
            ns = len(sub)
            p = Counter(triangle_pattern(a, b, arb) for *_x, a, b, arb in sub)
            sa = sum(1 for *_x, a, b, arb in sub if a == b)
            print(f"      {sut:11} n={ns:3}  {p.get('all_three_agree', 0) / ns:.4f}  "
                  f"{sa / ns:.4f}  {p.get('seats_differ_arbiter_matches_A', 0) / ns:.4f}  "
                  f"{p.get('seats_differ_arbiter_matches_B', 0) / ns:.4f}")

    print("\n  arbiter-leg determination distribution vs the seat legs:")
    for judge in JUDGES:
        tri = [t for t in triangle_rows(rows, judge)]
        usable = [t for t in tri if t[3] is not None and t[4] is not None and t[5] is not None]
        print(f"    {judge}: seat_A {dict(Counter(t[3] for t in usable))}")
        print(f"    {judge}: seat_B {dict(Counter(t[4] for t in usable))}")
        print(f"    {judge}: arbiter {dict(Counter(t[5] for t in usable))}")

    # ---------------------------------------------------------- stability
    print("\n" + "=" * 96)
    print("5. STABILITY - 5-system ordering of strict A==B under judge A vs judge B")
    print("=" * 96)
    xa = [headline[(s, "judge_a")] for s in SUTS]
    xb = [headline[(s, "judge_b")] for s in SUTS]
    ord_a = [s for _v, s in sorted(zip(xa, SUTS), key=lambda t: -t[0])]
    ord_b = [s for _v, s in sorted(zip(xb, SUTS), key=lambda t: -t[0])]
    print(f"\n  judge_a ordering (high -> low): {' > '.join(ord_a)}")
    print(f"    values: {['%s=%.4f' % (s, headline[(s, 'judge_a')]) for s in ord_a]}")
    print(f"  judge_b ordering (high -> low): {' > '.join(ord_b)}")
    print(f"    values: {['%s=%.4f' % (s, headline[(s, 'judge_b')]) for s in ord_b]}")
    print(f"\n  identical ordering: {'yes' if ord_a == ord_b else 'no'}")
    ra, rb = _ranks(xa), _ranks(xb)
    print(f"  judge_a ranks {dict(zip(SUTS, ra))}")
    print(f"  judge_b ranks {dict(zip(SUTS, rb))}")
    print(f"  Spearman rho (descriptive) = {spearman(xa, xb):.4f}")
    print(f"  Kendall tau  (descriptive) = {kendall_tau(xa, xb):.4f}")
    adj = sum(1 for i in range(len(SUTS)) if abs(ra[i] - rb[i]) <= 1)
    print(f"  systems within one rank position of themselves across judges: {adj}/5")

    print("\n  saturation check on the strict rate:")
    for judge in JUDGES:
        vv = [headline[(s, judge)] for s in SUTS]
        print(f"    {judge}: range [{min(vv):.4f}, {max(vv):.4f}], spread {max(vv) - min(vv):.4f}, "
              f"systems at 1.0: {sum(1 for v in vv if v >= 0.99995)}/5")
    for judge in JUDGES:
        vv = [strict_cell[(s, e)][0 if judge == 'judge_a' else 1]['strict_ab']
              for s in SUTS for e in EPOCHS]
        vv = [v for v in vv if not (isinstance(v, float) and math.isnan(v))]
        print(f"    {judge}: 15 (sut, epoch) cells range [{min(vv):.4f}, {max(vv):.4f}], "
              f"cells at 1.0: {sum(1 for v in vv if v >= 0.99995)}/{len(vv)}")

    print("\n  side-by-side: shipped partial-credit index vs strict rate (epoch-avg-first)")
    ship_item: Dict[Tuple[str, str], float] = {}
    for judge in JUDGES:
        for sut in SUTS:
            acc = defaultdict(list)
            for ep in EPOCHS:
                sc = build_sample_scores(rows, meta_index, judge, sut, ep)
                kept, _ = _drop_exemplars(sc)
                for pair, admins in _group_by_pair(kept).items():
                    a, b = admins.get("seat_A"), admins.get("seat_B")
                    if a is None or b is None:
                        continue
                    va = a.score.value if isinstance(a.score.value, dict) else {}
                    vb = b.score.value if isinstance(b.score.value, dict) else {}
                    x, y = va.get(DETERMINATION), vb.get(DETERMINATION)
                    if not _ok(x) or not _ok(y):
                        continue
                    r = 1.0 if x == y else (0.0 if {x, y} == {"A_owes", "B_owes"} else 0.5)
                    acc[pair.split("|")[-1]].append(r)
            means = [sum(v) / len(v) for v in acc.values() if v]
            ship_item[(sut, judge)] = sum(means) / len(means) if means else float("nan")
    print(f"\n{'sut':11}{'judge':9}{'shipped':11}{'strict':11}{'gap':9}")
    for sut in SUTS:
        for judge in JUDGES:
            s_, t_ = ship_item[(sut, judge)], headline[(sut, judge)]
            print(f"{sut:11}{judge:9}{_f(s_):<11}{_f(t_):<11}{_f(s_ - t_):<9}")

    print("\n" + "=" * 96)
    print("END - all figures above are DIAGNOSTIC. Strict A==B is NOT proposed as a")
    print("shipped metric; promoting it would be a new instrument version.")
    print("canary: WALKWORTHY-CANARY-7f3e2026")
    print("=" * 96)


if __name__ == "__main__":
    main()
