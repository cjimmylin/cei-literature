"""Offline analysis of judge-ablation outputs — NO model calls, ever.

Reads only stored artifacts: the pilot `.eval` logs, each SUT's judgeB-verdicts.jsonl,
and (optionally) the ablated JSONL files written by tools/audit/judge_ablation.py.

Two subcommands:

  per-turn   Baseline per-SUT judge-A/judge-B per-turn agreement for design 02 or 07,
             computed from stored data (judge-A turn_states from each design eval log's
             Score.value — a JSON-ENCODED STRING, mirroring pilot_judge_swap.py; judge-B
             turn_states from judgeB-verdicts.jsonl, also json.dumps'd). Agreement =
             fraction of aligned turn positions where BOTH states are non-UNSCORABLE and
             equal; denominator = positions where BOTH are non-UNSCORABLE; n_excluded =
             aligned positions dropped because at least one side was UNSCORABLE. With
             --ablation-a / --ablation-b, compute the same per-SUT agreement for the
             ablated arm and print a with/without comparison.

  leniency   For designs 03/06/09, per design × SUT × category: mean numeric score
             anchor-VISIBLE (stored judge-A Score.value from the eval logs) vs
             anchor-BLIND (from the ablated JSONL), and delta = blind − visible. ORD/BIN/
             INT coerced to float (UNSCORABLE skipped); CAT categories print value
             distributions instead of means. Optional --out JSON.

Usage:
    .venv/bin/python tools/audit/ablation_agreement.py per-turn --design 07
    .venv/bin/python tools/audit/ablation_agreement.py per-turn --design 02 \
        --ablation-a logs/f2-ablation/d02-anchors-on.jsonl
    .venv/bin/python tools/audit/ablation_agreement.py leniency \
        --ablated logs/f2-ablation/answer-blind.jsonl --out logs/f2-ablation/leniency.json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

from walkworthy_inspect.rubrics import BIN, CAT, INT, ORD, spec_for  # noqa: E402

UNSCORABLE = "unscorable"


def _design_num_from_task(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _sut_dirs(pilot_dir: str) -> List[str]:
    return sorted(d for d in glob.glob(os.path.join(pilot_dir, "*/"))
                  if glob.glob(os.path.join(d, "*.eval")))


def _decode_turn_states(raw: Any) -> List[Any]:
    """Decode a JSON-encoded turn_states string (mirrors pilot_judge_swap._agree_turns)."""
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw or "[]")
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def _turn_agreement(a_states: List[Any], b_states: List[Any]) -> Tuple[int, int, int]:
    """(matches, both_scorable_positions, n_excluded) over aligned positions.

    Denominator counts only positions where BOTH sides are non-UNSCORABLE; n_excluded
    is aligned positions dropped because at least one side was UNSCORABLE.
    """
    n = min(len(a_states), len(b_states))
    matches = both = excluded = 0
    for i in range(n):
        a, b = a_states[i], b_states[i]
        if a == UNSCORABLE or b == UNSCORABLE or a is None or b is None:
            excluded += 1
            continue
        both += 1
        matches += (a == b)
    return matches, both, excluded


# --------------------------------------------------------------------------- #
# stored per-turn state extraction
# --------------------------------------------------------------------------- #
def _judge_a_turn_states(sut_dir: str, design_num: str) -> Dict[Any, List[Any]]:
    """{sample_id: turn_states list} from the design's eval log Score.value."""
    out: Dict[Any, List[Any]] = {}
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p)
        if _design_num_from_task(log.eval.task) != design_num:
            continue
        for s in (log.samples or []):
            if not s.scores:
                continue
            sc = list(s.scores.values())[0]
            val = sc.value if isinstance(sc.value, dict) else {}
            out[s.id] = _decode_turn_states(val.get("turn_states"))
    return out


def _judge_b_turn_states(sut_dir: str, design_num: str) -> Dict[Any, List[Any]]:
    """{sample_id: turn_states list} from judgeB-verdicts.jsonl (judge_b.turn_states)."""
    out: Dict[Any, List[Any]] = {}
    vpath = os.path.join(sut_dir, "judgeB-verdicts.jsonl")
    if not os.path.exists(vpath):
        return out
    for line in open(vpath, encoding="utf-8"):
        r = json.loads(line)
        if not r.get("design", "").startswith(design_num):
            continue
        jb = r.get("judge_b") or {}
        out[r["sample_id"]] = _decode_turn_states(jb.get("turn_states"))
    return out


def _ablation_turn_states(path: str, design_num: str) -> Dict[Any, List[Any]]:
    """{sample_id: turn_states list} from a script-1 ablation JSONL (verdict.turn_states)."""
    out: Dict[Any, List[Any]] = {}
    if not path or not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if not r.get("design", "").startswith(design_num):
            continue
        v = r.get("verdict") or {}
        out[r["sample_id"]] = _decode_turn_states(v.get("turn_states"))
    return out


def _agg_agreement(a_map: Dict[Any, List[Any]],
                   b_map: Dict[Any, List[Any]]) -> Tuple[int, int, int]:
    m = both = exc = 0
    for sid, a_states in a_map.items():
        if sid not in b_map:
            continue
        dm, db, de = _turn_agreement(a_states, b_map[sid])
        m += dm
        both += db
        exc += de
    return m, both, exc


def _fmt_agree(m: int, both: int, exc: int) -> str:
    frac = f"{m / both:.3f}" if both else "n/a"
    return f"{m}/{both} ({frac})  n_excluded={exc}"


def cmd_per_turn(args) -> None:
    design = args.design
    suts = _sut_dirs(args.pilot_dir)
    print(f"=== PER-TURN AGREEMENT  design {design}  (baseline judge-A vs judge-B) ===")
    print("agreement = matched / both-scorable aligned turn positions\n")
    have_ablation = bool(args.ablation_a or args.ablation_b)
    for sut in suts:
        name = Path(sut.rstrip("/")).name
        a_map = _judge_a_turn_states(sut, design)
        b_map = _judge_b_turn_states(sut, design)
        m, both, exc = _agg_agreement(a_map, b_map)
        line = f"  {name:20} baseline A/B: {_fmt_agree(m, both, exc)}"
        if have_ablation:
            # ablation vs stored judge-A (arm-off vs arm-on comparison)
            abl_map = _ablation_turn_states(args.ablation_a, design) if args.ablation_a else {}
            abl_map_b = _ablation_turn_states(args.ablation_b, design) if args.ablation_b else {}
            # A/ablation and B/ablation not both needed; report vs judge-A by default,
            # and vs judge-B when --ablation-b supplied.
            extras = []
            if abl_map:
                am, ab, ae = _agg_agreement(a_map, abl_map)
                extras.append(f"A/ablation-a: {_fmt_agree(am, ab, ae)}")
            if abl_map_b:
                bm, bb, be = _agg_agreement(b_map, abl_map_b)
                extras.append(f"B/ablation-b: {_fmt_agree(bm, bb, be)}")
            line += "   " + " | ".join(extras)
        print(line)


# --------------------------------------------------------------------------- #
# leniency: anchor-visible (stored judge-A) vs anchor-blind (ablated) per category
# --------------------------------------------------------------------------- #
def _coerce_float(v: Any) -> Optional[float]:
    if v is None or v == UNSCORABLE:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _judge_a_scores(sut_dir: str, design_num: str) -> Dict[Any, dict]:
    """{sample_id: Score.value dict} from the design's eval log."""
    out: Dict[Any, dict] = {}
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p)
        if _design_num_from_task(log.eval.task) != design_num:
            continue
        for s in (log.samples or []):
            if not s.scores:
                continue
            sc = list(s.scores.values())[0]
            out[s.id] = sc.value if isinstance(sc.value, dict) else {}
    return out


def _ablation_verdicts(path: str, design_num: str) -> Dict[Any, dict]:
    """{sample_id: verdict dict} from a script-1 ablation JSONL for one design."""
    out: Dict[Any, dict] = {}
    if not path or not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if not r.get("design", "").startswith(design_num):
            continue
        out[r["sample_id"]] = r.get("verdict") or {}
    return out


def cmd_leniency(args) -> None:
    designs = [d.strip().zfill(2) for d in args.designs.split(",") if d.strip()]
    suts = _sut_dirs(args.pilot_dir)
    report: Dict[str, Any] = {}
    print(f"=== LENIENCY  anchor-VISIBLE (judge-A) vs anchor-BLIND (ablated)  "
          f"designs={designs} ===")
    print("delta = blind_mean − visible_mean  (positive = blinded judge scores higher)\n")

    for dnum in designs:
        try:
            spec = spec_for(dnum)
        except KeyError:
            print(f"[design {dnum}] no rubric; skipped")
            continue
        cats = list(spec.categories)
        report.setdefault(dnum, {})
        print(f"[design {dnum}]  categories: {[c.name for c in cats]}")
        for sut in suts:
            name = Path(sut.rstrip("/")).name
            vis = _judge_a_scores(sut, dnum)
            blind = _ablation_verdicts(args.ablated, dnum)
            common = [sid for sid in vis if sid in blind]
            if not common:
                continue
            report[dnum].setdefault(name, {})
            for c in cats:
                if c.scale == CAT:
                    vd = Counter(vis[sid].get(c.name) for sid in common
                                 if vis[sid].get(c.name) not in (None, UNSCORABLE))
                    bd = Counter(blind[sid].get(c.name) for sid in common
                                 if blind[sid].get(c.name) not in (None, UNSCORABLE))
                    print(f"  {name:16} {c.name:22} [CAT] visible={dict(vd)}  "
                          f"blind={dict(bd)}")
                    report[dnum][name][c.name] = {
                        "scale": "CAT", "visible_dist": dict(vd), "blind_dist": dict(bd)}
                else:
                    vv = [x for x in (_coerce_float(vis[sid].get(c.name))
                                      for sid in common) if x is not None]
                    bv = [x for x in (_coerce_float(blind[sid].get(c.name))
                                      for sid in common) if x is not None]
                    vm = sum(vv) / len(vv) if vv else None
                    bm = sum(bv) / len(bv) if bv else None
                    delta = (bm - vm) if (vm is not None and bm is not None) else None
                    vs = f"{vm:.3f}" if vm is not None else "—"
                    bs = f"{bm:.3f}" if bm is not None else "—"
                    ds = f"{delta:+.3f}" if delta is not None else "—"
                    print(f"  {name:16} {c.name:22} [{c.scale}] "
                          f"visible={vs}(n={len(vv)})  blind={bs}(n={len(bv)})  delta={ds}")
                    report[dnum][name][c.name] = {
                        "scale": c.scale, "visible_mean": vm, "blind_mean": bm,
                        "delta": delta, "n_visible": len(vv), "n_blind": len(bv)}
        print()

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
        print(f"wrote leniency report -> {args.out}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Offline judge-ablation analysis (no model calls).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pt = sub.add_parser("per-turn", help="baseline + ablated per-turn A/B agreement (02/07)")
    pt.add_argument("--pilot-dir", default="logs/pilot-20260716")
    pt.add_argument("--design", required=True, choices=["02", "07"])
    pt.add_argument("--ablation-a", default=None, help="script-1 JSONL to compare vs judge-A")
    pt.add_argument("--ablation-b", default=None, help="script-1 JSONL to compare vs judge-B")
    pt.set_defaults(func=cmd_per_turn)

    ln = sub.add_parser("leniency", help="anchor-visible vs anchor-blind per category (03/06/09)")
    ln.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ln.add_argument("--ablated", required=True, help="script-1 answer-blind JSONL")
    ln.add_argument("--designs", default="03,06,09")
    ln.add_argument("--out", default=None, help="optional JSON report path")
    ln.set_defaults(func=cmd_leniency)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
