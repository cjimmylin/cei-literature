"""F7 metrics scaffold — offline analysis of the design-07 prior-turn-context re-judge.

NO model calls, ever. Reads only stored artifacts: the pilot `.eval` logs (shipped
context-FREE judge-A turn_states, from each design-07 eval log Score.value — a
JSON-ENCODED STRING, mirroring pilot_judge_swap.py / ablation_agreement.py), each SUT's
judgeB-verdicts.jsonl (shipped context-free judge-B turn_states), and — ONCE the F7
live arm has run — the context-augmented JSONL written by judge_context_ablation.py.

The join is scoped by (sut, log basename, sample_id): sample_ids REPEAT across SUTs (same
items), so joining by sample_id alone silently collides — the last-loaded SUT's rows would
overwrite all others (the exact bug ablation_agreement.py documents at _sut_log_basenames,
found 2026-07-16 on the first answer-blind analysis). We reuse that log-basename-scoped
join pattern here.

Subcommands:

  self-check  Prove the join logic with ZERO F7 data: compare the shipped context-free
              judge-A turn_states against THEMSELVES (baseline-vs-baseline). Correct join
              => agreement 1.000 on every per-SUT cell, n_excluded counts UNSCORABLE
              positions. Any cell != 1.000 means the join is broken. Runnable TODAY.

  agreement   (needs F7 context JSONL) Per-turn state agreement context-vs-blind, per
              judge; cross-judge agreement UNDER CONTEXT (does context close the design-07
              judge gap?); arc_pass_rate movement vs shipped. Refuses if the context JSONL
              is absent (the F7 live arm has not been authorized/run).

Usage:
    .venv/bin/python tools/audit/context_ablation_agreement.py self-check
    .venv/bin/python tools/audit/context_ablation_agreement.py agreement \
        --context-a logs/f7-context/context-judgeA.jsonl \
        --context-b logs/f7-context/context-judgeB.jsonl
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

UNSCORABLE = "unscorable"
DESIGN = "07"
# design-07 arc_pass: the terminal counsel state must be faithful_counsel (the shipped
# _arc_pass_from_states rule surfaced in scorers.py; here we recompute the RATE from the
# terminal state for a coarse movement signal, not the authoritative metric).
_ARC_PASS_TERMINAL = "faithful_counsel"


def _design_num_from_task(task_name: str) -> Optional[str]:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or ""):
            return n
    return None


def _sut_dirs(pilot_dir: str) -> List[str]:
    return sorted(d for d in glob.glob(os.path.join(pilot_dir, "*/"))
                  if glob.glob(os.path.join(d, "*.eval")))


def _decode_turn_states(raw: Any) -> List[Any]:
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw or "[]")
    except (json.JSONDecodeError, TypeError, ValueError):
        return []


def _turn_agreement(a: List[Any], b: List[Any]) -> Tuple[int, int, int]:
    n = min(len(a), len(b))
    matches = both = excluded = 0
    for i in range(n):
        x, y = a[i], b[i]
        if x == UNSCORABLE or y == UNSCORABLE or x is None or y is None:
            excluded += 1
            continue
        both += 1
        matches += (x == y)
    return matches, both, excluded


def _agg(a_map: Dict[Any, List[Any]], b_map: Dict[Any, List[Any]]) -> Tuple[int, int, int]:
    m = both = exc = 0
    for sid, a in a_map.items():
        if sid not in b_map:
            continue
        dm, db, de = _turn_agreement(a, b_map[sid])
        m += dm; both += db; exc += de
    return m, both, exc


def _fmt(m: int, both: int, exc: int) -> str:
    frac = f"{m / both:.3f}" if both else "n/a"
    return f"{m}/{both} ({frac})  n_excluded={exc}"


# --------------------------------------------------------------------------- #
# stored (context-free / shipped) per-turn states
# --------------------------------------------------------------------------- #
def _sut_log_basenames(sut_dir: str) -> set:
    names = set()
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p, header_only=True)
        if _design_num_from_task(log.eval.task) == DESIGN:
            names.add(os.path.basename(p))
    return names


def _shipped_judge_a(sut_dir: str) -> Dict[Any, List[Any]]:
    out: Dict[Any, List[Any]] = {}
    for p in sorted(glob.glob(os.path.join(sut_dir, "*.eval"))):
        log = read_eval_log(p)
        if _design_num_from_task(log.eval.task) != DESIGN:
            continue
        for s in (log.samples or []):
            if not s.scores:
                continue
            sc = list(s.scores.values())[0]
            val = sc.value if isinstance(sc.value, dict) else {}
            out[s.id] = _decode_turn_states(val.get("turn_states"))
    return out


def _shipped_judge_b(sut_dir: str) -> Dict[Any, List[Any]]:
    out: Dict[Any, List[Any]] = {}
    vpath = os.path.join(sut_dir, "judgeB-verdicts.jsonl")
    if not os.path.exists(vpath):
        return out
    for line in open(vpath, encoding="utf-8"):
        r = json.loads(line)
        if not r.get("design", "").startswith(DESIGN):
            continue
        jb = r.get("judge_b") or {}
        out[r["sample_id"]] = _decode_turn_states(jb.get("turn_states"))
    return out


def _context_states(path: str, allowed_logs: Optional[set]) -> Dict[Any, List[Any]]:
    """{sample_id: turn_states} from an F7 context JSONL, scoped to one SUT's logs."""
    out: Dict[Any, List[Any]] = {}
    if not path or not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if not r.get("design", "").startswith(DESIGN):
            continue
        if allowed_logs is not None and os.path.basename(r.get("log", "")) not in allowed_logs:
            continue
        v = r.get("verdict") or {}
        out[r["sample_id"]] = _decode_turn_states(v.get("turn_states"))
    return out


def _arc_pass_rate(states_map: Dict[Any, List[Any]]) -> Tuple[int, int]:
    """(n_pass, n_scorable) by terminal-state rule; skips samples with UNSCORABLE terminal."""
    npass = ntot = 0
    for st in states_map.values():
        if not st:
            continue
        terminal = st[-1]
        if terminal == UNSCORABLE or terminal is None:
            continue
        ntot += 1
        npass += (terminal == _ARC_PASS_TERMINAL)
    return npass, ntot


# --------------------------------------------------------------------------- #
def cmd_self_check(args) -> None:
    """baseline-vs-baseline: shipped judge-A vs itself => agreement 1.000 everywhere."""
    suts = _sut_dirs(args.pilot_dir)
    print("=== F7 METRICS SELF-CHECK  design-07  (shipped judge-A vs ITSELF) ===")
    print("join scoped by (sut, log-basename, sample_id); expect agreement 1.000 all cells\n")
    all_ok = True
    tot_m = tot_both = tot_exc = 0
    for sut in suts:
        name = Path(sut.rstrip("/")).name
        a = _shipped_judge_a(sut)
        m, both, exc = _agg(a, a)
        tot_m += m; tot_both += both; tot_exc += exc
        frac = (m / both) if both else None
        ok = (both > 0 and abs(frac - 1.0) < 1e-9)
        all_ok = all_ok and ok
        flag = "OK" if ok else "*** BROKEN ***"
        print(f"  {name:20} A/A: {_fmt(m, both, exc)}  n_samples={len(a)}  [{flag}]")
    gfrac = f"{tot_m / tot_both:.3f}" if tot_both else "n/a"
    print(f"\n  TOTAL A/A agreement = {tot_m}/{tot_both} ({gfrac})  n_excluded={tot_exc}")
    # cross-check the join can also DETECT collision: also show A-vs-B baseline (not 1.0),
    # proving self-check==1.0 isn't a trivial always-1 artifact.
    print("\n  (control) shipped judge-A vs shipped judge-B (expect < 1.000 — real gap):")
    ctm = ctb = cte = 0
    for sut in suts:
        name = Path(sut.rstrip("/")).name
        a = _shipped_judge_a(sut)
        b = _shipped_judge_b(sut)
        m, both, exc = _agg(a, b)
        ctm += m; ctb += both; cte += exc
        print(f"    {name:20} A/B: {_fmt(m, both, exc)}")
    cfrac = f"{ctm / ctb:.3f}" if ctb else "n/a"
    print(f"    TOTAL A/B = {ctm}/{ctb} ({cfrac})")
    print()
    if all_ok and tot_both > 0:
        print("SELF-CHECK PASS: join logic correct (baseline-vs-baseline = 1.000).")
    else:
        print("SELF-CHECK FAIL: join logic broken — investigate before trusting F7 metrics.")
        sys.exit(1)


def cmd_agreement(args) -> None:
    """Context-vs-shipped agreement + cross-judge-under-context + arc_pass movement.

    Refuses unless at least one F7 context JSONL exists (the live arm has run)."""
    if not (args.context_a and os.path.exists(args.context_a)) and \
       not (args.context_b and os.path.exists(args.context_b)):
        print("NO F7 CONTEXT DATA: neither --context-a nor --context-b exists. The F7 "
              "live arm has not been run (LIVE ARM NOT RUN — awaiting PF-003 GO). Run "
              "the self-check subcommand to validate the join logic offline.", file=sys.stderr)
        sys.exit(2)

    suts = _sut_dirs(args.pilot_dir)
    print("=== F7 CONTEXT-vs-SHIPPED AGREEMENT  design-07 ===\n")
    grand = {"a_ctx": [0, 0, 0], "b_ctx": [0, 0, 0], "xjudge": [0, 0, 0]}
    ship_arc = [0, 0]
    ctx_arc = [0, 0]
    for sut in suts:
        name = Path(sut.rstrip("/")).name
        allowed = _sut_log_basenames(sut)
        a_ship = _shipped_judge_a(sut)
        b_ship = _shipped_judge_b(sut)
        a_ctx = _context_states(args.context_a, allowed) if args.context_a else {}
        b_ctx = _context_states(args.context_b, allowed) if args.context_b else {}
        parts = []
        if a_ctx:
            m, both, exc = _agg(a_ship, a_ctx)
            for i, v in enumerate((m, both, exc)):
                grand["a_ctx"][i] += v
            parts.append(f"A ship/ctx: {_fmt(m, both, exc)}")
            p, t = _arc_pass_rate(a_ctx)
            ctx_arc[0] += p; ctx_arc[1] += t
            sp, st_ = _arc_pass_rate(a_ship)
            ship_arc[0] += sp; ship_arc[1] += st_
        if b_ctx:
            m, both, exc = _agg(b_ship, b_ctx)
            for i, v in enumerate((m, both, exc)):
                grand["b_ctx"][i] += v
            parts.append(f"B ship/ctx: {_fmt(m, both, exc)}")
        if a_ctx and b_ctx:
            m, both, exc = _agg(a_ctx, b_ctx)
            for i, v in enumerate((m, both, exc)):
                grand["xjudge"][i] += v
            parts.append(f"A'/B' (cross-judge under context): {_fmt(m, both, exc)}")
        print(f"  {name:20} " + " | ".join(parts))

    print("\n  --- TOTALS ---")
    for k, lab in [("a_ctx", "judge-A shipped vs context"),
                   ("b_ctx", "judge-B shipped vs context"),
                   ("xjudge", "cross-judge UNDER CONTEXT (does context close the gap?)")]:
        m, both, exc = grand[k]
        if both:
            print(f"    {lab:52} {_fmt(m, both, exc)}")
    if ship_arc[1] and ctx_arc[1]:
        sr = ship_arc[0] / ship_arc[1]
        cr = ctx_arc[0] / ctx_arc[1]
        print(f"\n    arc_pass_rate (judge-A, terminal-state rule): "
              f"shipped {sr:.3f} ({ship_arc[0]}/{ship_arc[1]})  "
              f"context {cr:.3f} ({ctx_arc[0]}/{ctx_arc[1]})  delta {cr - sr:+.3f}")


def main() -> None:
    ap = argparse.ArgumentParser(description="F7 offline context-ablation metrics (no model calls).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sc = sub.add_parser("self-check", help="baseline-vs-baseline join validation (=1.000)")
    sc.add_argument("--pilot-dir", default="logs/pilot-20260716")
    sc.set_defaults(func=cmd_self_check)

    ag = sub.add_parser("agreement", help="context-vs-shipped + cross-judge + arc movement")
    ag.add_argument("--pilot-dir", default="logs/pilot-20260716")
    ag.add_argument("--context-a", default=None, help="F7 judge-A context JSONL")
    ag.add_argument("--context-b", default=None, help="F7 judge-B context JSONL")
    ag.set_defaults(func=cmd_agreement)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
