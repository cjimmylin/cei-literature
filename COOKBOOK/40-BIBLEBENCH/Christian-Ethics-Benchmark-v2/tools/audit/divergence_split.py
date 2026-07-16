"""Divergence-split re-report (F1, 20260716 adjudication).

Partitions each SUT x design's stored pilot samples by the item-level divergence tag
sidecar (banks/20260716-divergence-tags.jsonl) and recomputes the design's PRIMARY_METRICS
on each subset. No SUT or judge call is made — this is a 100% offline recompute over the
stored `.eval` logs (judge-A Score.value dicts) and `judgeB-verdicts.jsonl` verdict dicts.

Pattern-matched from tools/audit/recompute_metrics.py (Wilson CI, SampleScore rebuild,
exemplar/stratum handling) and tools/audit/pilot_judge_swap.py (judge-B SampleScore
substitution). Design-05 CSR is recovered via tools/audit/recompute_design05_csr.py's
re-parse approach (stored 05 Score values predate the alloc-spec fix and are all nan).

Scoping to match 20260716-pilot-report.md §3 headline scope:
  - Exemplars are dropped (metadata.is_exemplar or admin endswith '-exemplar').
  - Headline scope is STRATUM (a) only; stratum (c) intra-corpus-dispute items are
    QUARANTINED (judge not G5-neutrality-certified in v2). So the "all" subset = all
    stratum-a non-exemplar surviving units, which reproduces the pilot report §3 numbers.
    Stratum-c counts are reported separately (quarantine note), never mixed into cells.

Subsets per SUT x design: all, yes, partial, no, yes+partial (aggregate). Each is the
stratum-a items whose divergence tag is in the subset; paired designs (03/04/08/09/10)
keep pairs intact because pair_id == item_id (asserted below), and 02/07 per-turn units
nest within an item_id.

Usage:
    .venv/bin/python tools/audit/divergence_split.py --pilot-dir logs/pilot-20260716
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.scorer import SampleScore, Score  # noqa: E402

from walkworthy_inspect.metrics import PRIMARY_METRICS  # noqa: E402
from walkworthy_inspect.ordo_constraints import item_csr  # noqa: E402
from walkworthy_inspect.parsers import reparse_allocation_response  # noqa: E402

# ---- primary-metric headline + companion keys ----------------------------- #
# Headline metric per design (leads each cell).
HEADLINE_KEY = {
    "01": "full_obedience_rate", "02": "break_rate", "03": "say_do_gap",
    "04": "motive_delta_mean", "05": "csr_mean", "06": "profile_mean",
    "07": "arc_pass_rate", "08": "covert_overt_gap", "09": "symmetry_index",
    "10": "mercy_delta",
}

# R8 joint companion metrics — surfaced next to the headline in every cell.
COMPANION_KEY = {
    "03": "revealed_faithful_rate", "04": "motive_correct_rate",
    "08": "covert_protection_rate", "09": "floor_violation_rate",
    "10": "mercy_pass_rate",
}

# The n-denominator key each design's headline uses (surviving units per cell).
N_KEY = {
    "01": "n", "02": "n", "03": "pairs", "04": "pairs", "05": "n",
    "06": None, "07": "n", "08": "pairs", "09": "pairs", "10": "pairs",
}

# Binary-rate keys eligible for a Wilson 95% CI, mapped to their denominator key.
# (recompute_metrics.py RATE_CI, extended with companions we surface.)
RATE_CI: Dict[str, List[tuple]] = {
    "01": [("full_obedience_rate", "n")],
    "02": [("break_rate", "n")],
    "03": [("revealed_faithful_rate", "pairs")],
    "04": [("motive_correct_rate", "correct_n")],
    "07": [("arc_pass_rate", "n")],
    "08": [("covert_protection_rate", "covert_n")],
    "10": [("mercy_pass_rate", "pass_n")],
}

INSUFFICIENT_N = 10  # R2: cells with < this many surviving units get flagged.

_Z95 = 1.959963984540054


def _wilson(p: float, n: int) -> Optional[tuple]:
    """Wilson 95% score interval for a binomial rate (verbatim from recompute_metrics.py)."""
    if n <= 0 or p is None or (isinstance(p, float) and math.isnan(p)):
        return None
    z2 = _Z95 * _Z95
    denom = 1.0 + z2 / n
    center = (p + z2 / (2 * n)) / denom
    half = (_Z95 * math.sqrt((p * (1 - p) + z2 / (4 * n)) / n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def _design_num(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _stratum_of(md: Optional[Dict[str, Any]]) -> str:
    return str((md or {}).get("stratum", "") or "").strip().lower()


def _is_exemplar_md(md: Dict[str, Any]) -> bool:
    if md.get("is_exemplar"):
        return True
    return str(md.get("admin", "") or "").endswith("-exemplar")


# --------------------------------------------------------------------------- #
# tag sidecar
# --------------------------------------------------------------------------- #
def load_tags(tags_path: str) -> Dict[str, Dict[str, Any]]:
    """item_id -> {divergence, stratum, design, is_exemplar}."""
    tags: Dict[str, Dict[str, Any]] = {}
    with open(tags_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            tags[r["item_id"]] = r
    return tags


SUBSETS = ["all", "yes", "partial", "no", "yes_partial"]


def _subset_match(divergence: str, subset: str) -> bool:
    if subset == "all":
        return True
    if subset == "yes_partial":
        return divergence in ("yes", "partial")
    return divergence == subset


# --------------------------------------------------------------------------- #
# design-05 CSR recovery (re-parse; stored 05 scores predate the alloc-spec fix)
# --------------------------------------------------------------------------- #
def _recover_csr_by_item(log) -> Dict[str, Optional[float]]:
    """item_id -> recovered per-item CSR (None = format non-compliant / undecidable),
    over non-exemplar samples. Faithful adaptation of recompute_design05_csr.recover()."""
    out: Dict[str, Optional[float]] = {}
    for s in (log.samples or []):
        meta = s.metadata or {}
        if _is_exemplar_md(meta):
            continue
        item_id = meta.get("item_id") or str(s.id)
        keyed = meta.get("keyed", {}) or {}
        alloc = (keyed.get("allocation")
                 or (keyed.get("extras", {}) or {}).get("allocation") or {})
        tokens = alloc.get("tokens", []) or []
        budget = float(alloc.get("budget", 0) or 0)
        constraints = keyed.get("keyed_constraints", "") or alloc.get("constraints", "")
        completion = s.output.completion if s.output else ""
        parse = reparse_allocation_response(completion, tokens, budget)
        if parse.non_compliant or not parse.values:
            out[item_id] = None
            continue
        csr = item_csr(parse.values, constraints, tokens)
        out[item_id] = float(csr) if csr is not None else None
    return out


def _csr_cell(csr_by_item: Dict[str, Optional[float]], item_ids: set) -> Dict[str, Any]:
    """Aggregate recovered per-item CSR over the item subset into a metric-style dict."""
    vals, n_total, noncompliant = [], 0, 0
    for iid in item_ids:
        if iid not in csr_by_item:
            continue
        n_total += 1
        v = csr_by_item[iid]
        if v is None:
            noncompliant += 1
        else:
            vals.append(v)
    mean = (sum(vals) / len(vals)) if vals else float("nan")
    return {"csr_mean": round(mean, 4) if not math.isnan(mean) else float("nan"),
            "n": len(vals), "n_total": n_total, "non_compliant": noncompliant}


# --------------------------------------------------------------------------- #
# per-SUT loading (judge-A from logs; judge-B from verdict sidecar)
# --------------------------------------------------------------------------- #
def load_sut(sut_dir: str, tags: Dict[str, Dict[str, Any]]):
    """Return {design: {"A":[SampleScore], "B":[SampleScore] or None,
                        "csr_by_item": {...} or None,
                        "stratum_c_units": int}}.
    Only stratum-a non-exemplar samples are kept in A/B (headline scope); stratum-c is
    counted for the quarantine note. item_id membership is resolved from sample metadata."""
    # judge-B verdicts keyed design->sample_id->verdict dict
    verdicts: Dict[str, Dict[Any, dict]] = {}
    vpath = os.path.join(sut_dir, "judgeB-verdicts.jsonl")
    have_judge_b = os.path.exists(vpath)
    if have_judge_b:
        for line in open(vpath, encoding="utf-8"):
            r = json.loads(line)
            num = r["design"].split("-", 1)[0].zfill(2)
            verdicts.setdefault(num, {})[r["sample_id"]] = r

    out: Dict[str, dict] = {}
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p)
        num = _design_num(log.eval.task)
        if num is None:
            continue
        a_scores: List[SampleScore] = []
        b_scores: List[SampleScore] = []
        stratum_c_units = 0
        b_ok = have_judge_b and num in verdicts
        for s in (log.samples or []):
            md = s.metadata or {}
            if _is_exemplar_md(md):
                continue
            if _stratum_of(md) == "c":
                stratum_c_units += 1
                continue
            if _stratum_of(md) not in ("a", ""):
                # any other non-a stratum also quarantined defensively
                stratum_c_units += 1
                continue
            if not s.scores:
                continue
            sc = list(s.scores.values())[0]
            a_scores.append(SampleScore(score=sc, sample_id=s.id, sample_metadata=md))
            if b_ok:
                v = verdicts.get(num, {}).get(s.id)
                if v and isinstance(v.get("judge_b"), dict):
                    jb = v["judge_b"]
                    jb_scalar = {k: val for k, val in jb.items()
                                 if isinstance(val, (str, int, float, bool)) or val is None}
                    b_scores.append(SampleScore(score=Score(value=jb_scalar),
                                                sample_id=s.id, sample_metadata=md))
                else:
                    b_ok = False  # incomplete judge-B coverage -> skip judge-B for design
        csr_by_item = _recover_csr_by_item(log) if num == "05" else None
        out[num] = {"A": a_scores, "B": b_scores if b_ok else None,
                    "csr_by_item": csr_by_item, "stratum_c_units": stratum_c_units}
    return out


def _item_ids_of(scores: List[SampleScore]) -> set:
    return {(_ss_meta(ss).get("item_id") or str(ss.sample_id)) for ss in scores}


def _ss_meta(ss: SampleScore) -> Dict[str, Any]:
    return ss.sample_metadata or {}


def _filter_by_subset(scores: List[SampleScore], tags, subset) -> List[SampleScore]:
    keep = []
    for ss in scores:
        iid = _ss_meta(ss).get("item_id") or str(ss.sample_id)
        t = tags.get(iid)
        dv = (t or {}).get("divergence", "no")
        if _subset_match(dv, subset):
            keep.append(ss)
    return keep


def _assert_pairs_intact(scores: List[SampleScore], num: str) -> None:
    """Verify pair_id never crosses item_id (so item-level filtering keeps pairs intact)."""
    for ss in scores:
        md = _ss_meta(ss)
        pid, iid = md.get("pair_id"), md.get("item_id")
        if pid is not None and iid is not None:
            assert pid == iid, (
                f"design {num}: pair_id {pid!r} != item_id {iid!r} — item-level "
                f"filtering would split a pair")


def _cell(num: str, scores: List[SampleScore], csr_by_item, tags, subset) -> Dict[str, Any]:
    """Compute one subset cell for a design: point est + Wilson CIs + n + flags."""
    sub = _filter_by_subset(scores, tags, subset)
    if num == "05":
        item_ids = {(_ss_meta(ss).get("item_id") or str(ss.sample_id)) for ss in sub}
        val = _csr_cell(csr_by_item or {}, item_ids)
    else:
        factory = PRIMARY_METRICS[num]
        val = factory()(sub) if sub else {}

    headline = HEADLINE_KEY[num]
    companion = COMPANION_KEY.get(num)
    n_key = N_KEY[num]
    n_surv = val.get(n_key) if n_key else len(sub)
    # design-06 uses per-criterion means; count of surviving samples for the flag:
    if num == "06":
        n_surv = len([s for s in sub])

    cell: Dict[str, Any] = {
        "subset": subset,
        "headline_key": headline,
        "headline": val.get(headline),
        "n": n_surv,
        "n_admins": len(sub),
        "full": val,
    }
    if companion:
        cell["companion_key"] = companion
        cell["companion"] = val.get(companion)
    # Wilson CI(s)
    cis = {}
    for rate_key, den_key in RATE_CI.get(num, []):
        p, n = val.get(rate_key), val.get(den_key)
        if isinstance(p, (int, float)) and isinstance(n, int):
            ci = _wilson(float(p), n)
            if ci:
                cis[rate_key] = {"est": round(float(p), 4),
                                 "lo": round(ci[0], 4), "hi": round(ci[1], 4), "n": n}
    cell["wilson"] = cis
    # R2 insufficient-n flag
    cell["insufficient_n"] = (isinstance(n_surv, int) and n_surv < INSUFFICIENT_N)
    return cell


def build(pilot_dir: str, tags_path: str) -> Dict[str, Any]:
    tags = load_tags(tags_path)
    suts = sorted(Path(d.rstrip("/")).name for d in glob.glob(os.path.join(pilot_dir, "*/"))
                  if glob.glob(os.path.join(d, "*.eval")))
    result: Dict[str, Any] = {"pilot_dir": pilot_dir, "tags_path": tags_path,
                              "suts": suts, "cells": {}, "judge_b": {}}
    tag_dist = {}  # design -> Counter
    for iid, t in tags.items():
        d = t["design"]
        tag_dist.setdefault(d, {"yes": 0, "partial": 0, "no": 0})
        tag_dist[d][t["divergence"]] += 1
    result["tag_distribution"] = tag_dist

    for sut in suts:
        sut_data = load_sut(os.path.join(pilot_dir, sut), tags)
        for num, dd in sut_data.items():
            _assert_pairs_intact(dd["A"], num)
            # judge-A cells
            for subset in SUBSETS:
                cell = _cell(num, dd["A"], dd["csr_by_item"], tags, subset)
                cell["stratum_c_units"] = dd["stratum_c_units"]
                result["cells"].setdefault(num, {}).setdefault(sut, {})[subset] = cell
            # judge-B cells (design 05 reuses judge-free recovered CSR)
            if num == "05":
                for subset in SUBSETS:
                    cb = _cell(num, dd["A"], dd["csr_by_item"], tags, subset)
                    cb["judge_free"] = True
                    result["judge_b"].setdefault(num, {}).setdefault(sut, {})[subset] = cb
            elif dd["B"] is not None:
                for subset in SUBSETS:
                    cb = _cell(num, dd["B"], None, tags, subset)
                    result["judge_b"].setdefault(num, {}).setdefault(sut, {})[subset] = cb
    return result


# --------------------------------------------------------------------------- #
# cross-check: "all" subset must reproduce recompute_metrics.py stratum-a numbers
# --------------------------------------------------------------------------- #
def crosscheck(pilot_dir: str, result: Dict[str, Any]) -> List[str]:
    """Recompute each design's stratum-a headline directly (independent path) and compare
    to the 'all' subset cell. Design 05 compared to the CSR recovery. Returns mismatch
    lines (empty => all match)."""
    mism: List[str] = []
    for sut in result["suts"]:
        sut_dir = os.path.join(pilot_dir, sut)
        for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
            log = read_eval_log(p)
            num = _design_num(log.eval.task)
            if num is None or num not in result["cells"]:
                continue
            headline = HEADLINE_KEY[num]
            all_cell = result["cells"][num][sut]["all"]
            got = all_cell["headline"]
            if num == "05":
                # independent CSR recovery over stratum-a items
                csr_by_item = _recover_csr_by_item(log)
                stratum_a_items = {(_ss_meta(SampleScore(score=list(s.scores.values())[0],
                                    sample_id=s.id, sample_metadata=s.metadata)).get("item_id"))
                                   for s in (log.samples or [])
                                   if s.scores and not _is_exemplar_md(s.metadata or {})
                                   and _stratum_of(s.metadata) == "a"}
                ref = _csr_cell(csr_by_item, stratum_a_items)["csr_mean"]
            else:
                factory = PRIMARY_METRICS[num]
                a_scores = []
                for s in (log.samples or []):
                    md = s.metadata or {}
                    if _is_exemplar_md(md) or _stratum_of(md) == "c":
                        continue
                    if _stratum_of(md) not in ("a", ""):
                        continue
                    if not s.scores:
                        continue
                    a_scores.append(SampleScore(score=list(s.scores.values())[0],
                                                sample_id=s.id, sample_metadata=md))
                ref = factory()(a_scores).get(headline)
            if not _num_eq(got, ref):
                mism.append(f"  {sut} d{num} {headline}: all-cell={got} vs ref={ref}")
    return mism


def _num_eq(a, b, tol=1e-6) -> bool:
    if a is None and b is None:
        return True
    if isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b):
        return True
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return a == b


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return "nan" if math.isnan(v) else f"{v:.4f}"
    return str(v)


def main() -> None:
    ap = argparse.ArgumentParser(description="Divergence-split re-report (F1).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ap.add_argument("--tags", default="banks/20260716-divergence-tags.jsonl")
    ap.add_argument("--out", default=None, help="JSON dump of all cells")
    args = ap.parse_args()

    result = build(args.pilot_dir, args.tags)

    # cross-check
    mism = crosscheck(args.pilot_dir, result)
    result["crosscheck_mismatches"] = mism

    # console summary
    print("=== TAG DISTRIBUTION (from sidecar) ===")
    tot = {"yes": 0, "partial": 0, "no": 0}
    for d in sorted(result["tag_distribution"]):
        c = result["tag_distribution"][d]
        for k in tot:
            tot[k] += c[k]
        print(f"  {d:22} yes={c['yes']:3} partial={c['partial']:3} no={c['no']:3}")
    print(f"  {'TOTAL':22} yes={tot['yes']:3} partial={tot['partial']:3} no={tot['no']:3}")

    print("\n=== CROSS-CHECK (all-subset vs independent stratum-a recompute) ===")
    if mism:
        print("  MISMATCHES:")
        for m in mism:
            print(m)
    else:
        print("  OK — every 'all' cell reproduces the independent recompute.")

    print("\n=== SPLIT CELLS (judge-A; headline [companion] n) ===")
    for num in sorted(result["cells"]):
        hk = HEADLINE_KEY[num]
        ck = COMPANION_KEY.get(num)
        print(f"\n[design {num}] headline={hk}" + (f"  companion={ck}" if ck else ""))
        for sut in result["suts"]:
            cells = result["cells"][num].get(sut, {})
            parts = []
            for subset in SUBSETS:
                c = cells.get(subset)
                if not c:
                    continue
                flag = "!" if c["insufficient_n"] else " "
                comp = f"/{_fmt(c.get('companion'))}" if ck else ""
                parts.append(f"{subset}={_fmt(c['headline'])}{comp}(n{c['n']}){flag}")
            print(f"  {sut:20} " + "  ".join(parts))

    if result["judge_b"]:
        print("\n=== JUDGE-B available for designs: "
              + ", ".join(sorted(result["judge_b"])) + " ===")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, default=lambda o: None
                      if isinstance(o, float) and math.isnan(o) else o)
        print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
