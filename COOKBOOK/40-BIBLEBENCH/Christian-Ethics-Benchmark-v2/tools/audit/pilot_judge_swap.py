"""Judge-swap analysis for the 20260716 pilot (adjudication R4 / SD-6).

For each SUT directory under --pilot-dir (each holding the 10 judge-A `.eval` logs and
a `judgeB-verdicts.jsonl` written by tools/rescore/rescore.py):

  1. Rebuild judge-A SampleScores from the stored logs and judge-B SampleScores by
     substituting each sample's Score.value with the judge-B verdict dict (metadata is
     shared — the SUT response is identical by construction; only the judge changed).
  2. Recompute every design's PRIMARY_METRICS headline under judge A and judge B.
  3. Per-design A/B agreement: exact field agreement over the design's judged
     categories; for 02/07, per-turn state agreement over the aligned turn_states.
  4. Ordering flips: for each design, order the SUTs by the headline under A and
     under B; a differing order marks the cell "judge-sensitive" (no SUT claim).
  5. Branch-source audit (M3): share of branched 02/07 turns routed by the lexical
     heuristic fallback rather than a parsed classifier verdict.

Free of SUT/judge calls — operates purely on stored logs + verdicts.

Usage:
    .venv/bin/python tools/audit/pilot_judge_swap.py --pilot-dir logs/pilot-20260716
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

HEADLINE_KEY = {
    "01": "full_obedience_rate", "02": "break_rate", "03": "say_do_gap",
    "04": "motive_delta_mean", "05": "csr_mean", "06": "profile_mean",
    "07": "arc_pass_rate", "08": "covert_overt_gap", "09": "symmetry_index",
    "10": "mercy_delta",
}


def _design_num(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return "nan" if math.isnan(v) else f"{v:.4f}"
    return str(v)


def _agree_fields(a: dict, b: dict) -> tuple:
    """(matches, cells) over shared judged fields, excluding bookkeeping keys."""
    skip = {"turn_states", "_judge_meta", "value", "non_compliant", "allocation_ok",
            "break_turn", "arc_pass"}
    m = c = 0
    for k in a:
        if k in skip or k.startswith("_"):
            continue
        if k in b:
            c += 1
            m += (a[k] == b[k])
    return m, c


def _agree_turns(a: dict, b: dict) -> tuple:
    try:
        ta = json.loads(a.get("turn_states") or "[]")
        tb = json.loads(b.get("turn_states") or "[]")
    except (json.JSONDecodeError, TypeError, ValueError):
        return 0, 0
    n = min(len(ta), len(tb))
    return sum(1 for i in range(n) if ta[i] == tb[i]), n


def load_sut(sut_dir: str):
    """Return {design: {"A": [SampleScore], "B": [SampleScore], "agree": (m,c),
                        "heuristic_turns": (h, t)}}"""
    verdicts: Dict[str, Dict[Any, dict]] = {}
    branch_sources: List[str] = []
    vpath = os.path.join(sut_dir, "judgeB-verdicts.jsonl")
    if os.path.exists(vpath):
        for line in open(vpath, encoding="utf-8"):
            r = json.loads(line)
            num = r["design"].split("-", 1)[0].zfill(2)
            verdicts.setdefault(num, {})[r["sample_id"]] = r
            for bs in (r.get("branch_sources") or []):
                if bs:
                    branch_sources.append(bs)

    out: Dict[str, dict] = {}
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p)
        num = _design_num(log.eval.task)
        if num is None:
            continue
        a_scores, b_scores = [], []
        agree_m = agree_c = 0
        for s in (log.samples or []):
            if not s.scores:
                continue
            sc = list(s.scores.values())[0]
            a_scores.append(SampleScore(score=sc, sample_id=s.id,
                                        sample_metadata=s.metadata))
            v = verdicts.get(num, {}).get(s.id)
            if v and isinstance(v.get("judge_b"), dict):
                jb = v["judge_b"]
                # Inspect's Score.value dict accepts scalars only — drop nested
                # bookkeeping (_judge_meta on unparseable verdicts) before wrapping.
                jb_scalar = {k: val for k, val in jb.items()
                             if isinstance(val, (str, int, float, bool)) or val is None}
                b_scores.append(SampleScore(score=Score(value=jb_scalar), sample_id=s.id,
                                            sample_metadata=s.metadata))
                a_val = sc.value if isinstance(sc.value, dict) else {}
                if num in ("02", "07"):
                    m, c = _agree_turns(a_val, jb)
                else:
                    m, c = _agree_fields(a_val, jb)
                agree_m += m
                agree_c += c
        out[num] = {"A": a_scores, "B": b_scores, "agree": (agree_m, agree_c)}
    out["_branch_sources"] = branch_sources
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Pilot judge-swap analysis (R4/SD-6).")
    ap.add_argument("--pilot-dir", default="logs/pilot-20260716")
    args = ap.parse_args()

    suts = sorted(d for d in glob.glob(os.path.join(args.pilot_dir, "*/"))
                  if glob.glob(os.path.join(d, "*.eval")))
    data = {Path(s.rstrip("/")).name: load_sut(s) for s in suts}

    designs = [f"{i:02d}" for i in range(1, 11)]
    headA: Dict[str, Dict[str, float]] = {}
    headB: Dict[str, Dict[str, float]] = {}

    print("=== PER-DESIGN HEADLINES: judge-A vs judge-B (per SUT) ===")
    for num in designs:
        key = HEADLINE_KEY[num]
        factory = PRIMARY_METRICS[num]
        print(f"\n[design {num}] headline={key}")
        for sut, dd in data.items():
            if num not in dd:
                continue
            va = factory()(dd[num]["A"])
            vb = factory()(dd[num]["B"]) if dd[num]["B"] else {}
            ha = va.get(key) if isinstance(va, dict) else None
            hb = vb.get(key) if isinstance(vb, dict) else None
            headA.setdefault(num, {})[sut] = ha
            headB.setdefault(num, {})[sut] = hb
            m, c = dd[num]["agree"]
            agree = f"{m}/{c} ({m / c:.3f})" if c else "n/a"
            print(f"  {sut:20} A={_fmt(ha):>8}  B={_fmt(hb):>8}  "
                  f"A/B field-agree={agree}")

    print("\n=== ORDERING FLIPS (judge-sensitive designs; naive point-estimate order) ===")
    for num in designs:
        a, b = headA.get(num, {}), headB.get(num, {})
        common = [s for s in a if s in b and a[s] is not None and b[s] is not None
                  and not (isinstance(a[s], float) and math.isnan(a[s]))
                  and not (isinstance(b[s], float) and math.isnan(b[s]))]
        if len(common) < 2:
            print(f"  design {num}: insufficient cells")
            continue
        oa = sorted(common, key=lambda s: a[s], reverse=True)
        ob = sorted(common, key=lambda s: b[s], reverse=True)
        flag = "STABLE" if oa == ob else "JUDGE-SENSITIVE (order flips)"
        print(f"  design {num}: {flag}")
        if oa != ob:
            print(f"     A-order: {' > '.join(oa)}")
            print(f"     B-order: {' > '.join(ob)}")

    print("\n=== BRANCH-SOURCE AUDIT (02/07 ladder routing, M3) ===")
    for sut, dd in data.items():
        bs = dd.get("_branch_sources", [])
        if bs:
            h = sum(1 for x in bs if x == "heuristic")
            print(f"  {sut:20} branched turns={len(bs)}  heuristic-fallback={h} "
                  f"({h / len(bs):.3f})")


if __name__ == "__main__":
    main()
