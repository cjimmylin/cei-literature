"""Judge-A vs judge-B disagreement cells + v1-baseline comparison.

Compares, per (sample, category), the judge-A verdict (from the Part-1 `.eval` logs)
against the judge-B verdict (from `judgeB-verdicts.jsonl`, produced by rescore.py) and
classifies each cell:

  - agree       : identical values.
  - near_agree  : ORDINAL/INT category whose two values are within `tolerance` steps on
                  the design's own option ladder (rubric-defined ordering). Categorical
                  and binary categories have NO near band — any mismatch is a disagree.
  - disagree    : everything else  -> needs_adjudication.
  - unscorable  : either judge produced no usable value (empty/refused/unscorable);
                  excluded from the agreement-rate denominator (v1 defect semantics).

Tolerance: ordinal ladders here are short ([0,1,2] or [0,0.5,1]); default tolerance = 1
LADDER STEP (adjacent options), which for [0,0.5,1] means a 0.5 gap and for [0,1,2] a
1-integer gap — i.e. "off by one bucket". Exact per-design ladders come from the ported
v1 rubric (`walkworthy_inspect.rubrics`), so the ordering is the rubric's, not guessed.

Also computes the SAME agree / near-agree / disagree breakdown for the v1 MVP-A1 run
(READ-ONLY `../Christian-Ethics-Benchmark/runs/20260713-mvp-a1/verdicts.jsonl`) for the
mistral SUT, so the v2 A-vs-B agreement rate can be compared design-by-design against the
v1 2-judge baseline. For v1 multiturn designs (02, 07) the two judges scored PER TURN
(`per_unit`); v2 scores the whole final completion — the v1 baseline for 02/07 is
therefore a turn-level rate and is flagged as a granularity mismatch, not a like-for-like
cell comparison.

Outputs:
  - logs/comparability-e2e/disagreement-cells.jsonl   (one row per v2 cell)
  - a per-design summary printed to stdout (also returned).
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from walkworthy_inspect.rubrics import (  # noqa: E402
    BIN, CAT, INT, ORD, Category, judge_categories, spec_for,
)

UNSCORABLE = "unscorable"
V1_RUN = _V2_ROOT.parent / "Christian-Ethics-Benchmark" / "runs" / "20260713-mvp-a1"


# --------------------------------------------------------------------------- #
# per-category classification
# --------------------------------------------------------------------------- #
def _ordinal_ladder(cat: Category) -> Optional[List[float]]:
    """Return the ordered numeric ladder for an ORD/INT category, else None."""
    if cat.scale == ORD:
        try:
            return [float(o) for o in cat.options]
        except (TypeError, ValueError):
            return None
    if cat.scale == INT:
        lo, hi = cat.options
        return [float(x) for x in range(int(lo), int(hi) + 1)]
    return None


def _usable(v: Any) -> bool:
    return v is not None and v != UNSCORABLE and v != ""


def classify_cell(cat: Category, a: Any, b: Any, tolerance: int = 1) -> str:
    """agree / near_agree / disagree / unscorable for one category cell."""
    if not _usable(a) or not _usable(b):
        return "unscorable"
    if str(a) == str(b):
        return "agree"
    # exact string equality already handled; now numeric-aware compare
    ladder = _ordinal_ladder(cat)
    if ladder is not None:
        try:
            ia, ib = ladder.index(float(a)), ladder.index(float(b))
            if abs(ia - ib) <= tolerance:
                return "near_agree"
            return "disagree"
        except (ValueError, TypeError):
            return "disagree"
    if cat.scale == BIN:
        try:
            return "agree" if int(float(a)) == int(float(b)) else "disagree"
        except (TypeError, ValueError):
            return "disagree"
    # CAT and everything else: exact match only (already failed) -> disagree
    return "disagree"


# --------------------------------------------------------------------------- #
# v2: judge-A (from logs, embedded in verdict rows) vs judge-B
# --------------------------------------------------------------------------- #
def _cat_map(design_num: str) -> Dict[str, Category]:
    spec = spec_for(design_num)
    cats = {c.name: c for c in judge_categories(spec)}
    if design_num == "05":
        # design 05 also carries the judge-free primary CSR (deterministic; identical
        # across judges by construction) — not a judged category, excluded from A/B.
        pass
    return cats


def _design_num(design: str) -> str:
    return str(design).split("-", 1)[0].zfill(2)


def build_v2_cells(verdicts_path: Path, tolerance: int) -> List[dict]:
    rows = [json.loads(l) for l in verdicts_path.open() if l.strip()]
    cells: List[dict] = []
    for r in rows:
        dnum = _design_num(r["design"])
        catmap = _cat_map(dnum)
        ja = r.get("judge_a") or {}
        jb = r.get("judge_b") or {}
        for cname, cat in catmap.items():
            a = ja.get(cname)
            b = jb.get(cname)
            verdict = classify_cell(cat, a, b, tolerance)
            cells.append({
                "design": r["design"],
                "sample_id": r.get("sample_id"),
                "item_id": r.get("item_id"),
                "admin": r.get("admin"),
                "category": cname,
                "scale": cat.scale,
                "judge_a": a,
                "judge_b": b,
                "verdict": verdict,
                "needs_adjudication": verdict == "disagree",
            })
    return cells


# --------------------------------------------------------------------------- #
# v1 baseline: same classification on the frozen MVP-A1 verdicts (mistral SUT)
# --------------------------------------------------------------------------- #
def _unit_map(verdict: dict) -> Dict[str, dict]:
    """Map a v1 verdict's scored units -> {unit_key: scores}.

    v1 stores scores either at top level (single-item designs 01/05/06) or in `per_unit`
    (per_turn 02/07 by index; per_admin/per_seat 03/04/08/09/10 by label). We key each
    unit by its label (falling back to index), and single-item designs by a fixed key.
    """
    per_unit = verdict.get("per_unit") or []
    if per_unit:
        out = {}
        for u in per_unit:
            key = str(u.get("label", u.get("index")))
            out[key] = u.get("scores", {}) or {}
        return out
    return {"_item": verdict.get("scores", {}) or {}}


def build_v1_baseline(tolerance: int, sut: str) -> Dict[str, dict]:
    """Per-design v1 A-vs-B agreement over ALL judged cells (every scored unit×category).

    Aggregating over units sidesteps v1<->v2 unit-label mismatches (v1 03 uses
    expressed/revealed; v2 03 uses say/do admins) — the comparable quantity is the
    per-design fraction of judged category-cells the two v1 judges agreed on.
    """
    vpath = V1_RUN / "verdicts.jsonl"
    if not vpath.exists():
        return {}
    rows = [json.loads(l) for l in vpath.open() if l.strip()]
    JUDGE_A = "openai/gpt-4.1-nano"
    JUDGE_B = "meta-llama/llama-3.3-70b-instruct"

    idx: Dict[Tuple[str, str, str], dict] = {}
    for r in rows:
        if sut not in str(r.get("model", "")):
            continue
        idx[(r["design"], r["item_id"], r["judge"])] = r["verdict"]

    per_design_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    seen = set()
    for (design, item_id, _judge) in list(idx.keys()):
        if (design, item_id) in seen:
            continue
        seen.add((design, item_id))
        va = idx.get((design, item_id, JUDGE_A))
        vb = idx.get((design, item_id, JUDGE_B))
        if va is None or vb is None:
            continue
        catmap = _cat_map(_design_num(design))
        amap, bmap = _unit_map(va), _unit_map(vb)
        for uk in sorted(set(amap) & set(bmap)):
            for cname, cat in catmap.items():
                verdict = classify_cell(cat, amap[uk].get(cname), bmap[uk].get(cname), tolerance)
                per_design_counts[design][verdict] += 1
    return {d: dict(c) for d, c in per_design_counts.items()}


# --------------------------------------------------------------------------- #
# summarize
# --------------------------------------------------------------------------- #
def summarize(cells: List[dict]) -> Dict[str, Dict[str, Any]]:
    by_design: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for c in cells:
        by_design[c["design"]][c["verdict"]] += 1
    out: Dict[str, Dict[str, Any]] = {}
    for d, cnts in by_design.items():
        scored = cnts.get("agree", 0) + cnts.get("near_agree", 0) + cnts.get("disagree", 0)
        agree = cnts.get("agree", 0)
        near = cnts.get("near_agree", 0)
        out[d] = {
            "agree": agree,
            "near_agree": near,
            "disagree": cnts.get("disagree", 0),
            "unscorable": cnts.get("unscorable", 0),
            "scored_cells": scored,
            "exact_agree_rate": round(agree / scored, 4) if scored else None,
            "agree_or_near_rate": round((agree + near) / scored, 4) if scored else None,
            "needs_adjudication": cnts.get("disagree", 0),
        }
    return out


def _fmt_baseline(v1: Dict[str, dict]) -> Dict[str, Dict[str, Any]]:
    out = {}
    for d, cnts in v1.items():
        scored = cnts.get("agree", 0) + cnts.get("near_agree", 0) + cnts.get("disagree", 0)
        agree = cnts.get("agree", 0)
        near = cnts.get("near_agree", 0)
        out[d] = {
            "agree": agree, "near_agree": near, "disagree": cnts.get("disagree", 0),
            "unscorable": cnts.get("unscorable", 0), "scored_cells": scored,
            "exact_agree_rate": round(agree / scored, 4) if scored else None,
            "agree_or_near_rate": round((agree + near) / scored, 4) if scored else None,
        }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verdicts", default="logs/comparability-e2e/judgeB-verdicts.jsonl")
    ap.add_argument("--out", default="logs/comparability-e2e/disagreement-cells.jsonl")
    ap.add_argument("--tolerance", type=int, default=1)
    ap.add_argument("--sut", default="mistralai/mistral-small-3.2-24b-instruct")
    args = ap.parse_args()

    cells = build_v2_cells(Path(args.verdicts), args.tolerance)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as fh:
        for c in cells:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    v2_summary = summarize(cells)
    v1_baseline = _fmt_baseline(build_v1_baseline(args.tolerance, args.sut))

    print(f"wrote {len(cells)} v2 A-vs-B cells -> {out}\n")
    total_adj = sum(s["needs_adjudication"] for s in v2_summary.values())
    print(f"{'design':18} | v2 exact | v2 +near | v2 adj | v1 exact | v1 +near")
    print("-" * 78)
    for d in sorted(v2_summary):
        v2 = v2_summary[d]
        v1 = v1_baseline.get(d, {})
        print(f"{d:18} | {str(v2['exact_agree_rate']):8} | {str(v2['agree_or_near_rate']):8} | "
              f"{v2['needs_adjudication']:6} | {str(v1.get('exact_agree_rate')):8} | "
              f"{str(v1.get('agree_or_near_rate')):8}")
    print("-" * 78)
    print(f"TOTAL needs_adjudication (v2): {total_adj}")

    # also dump the machine summary for the report
    summ_path = out.parent / "disagreement-summary.json"
    with summ_path.open("w", encoding="utf-8") as fh:
        json.dump({"v2": v2_summary, "v1_baseline": v1_baseline,
                   "tolerance": args.tolerance, "sut": args.sut,
                   "total_needs_adjudication": total_adj}, fh, indent=2)
    print(f"summary -> {summ_path}")


if __name__ == "__main__":
    main()
