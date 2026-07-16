"""Offline metric recompute (ITEM 2e).

Reads the per-design `.eval` logs from a --log-dir, rebuilds `SampleScore` objects from
each stored sample's Score + metadata, and recomputes ALL 10 §4 primary metrics with the
NEW walkworthy_inspect.metrics code (exemplar exclusion, per-turn 02/07, paired 03, etc.).

Prints a side-by-side table: OLD reported (from each log's stored
`results.scores[].metrics`, else the reference numbers hardcoded from
`20260715d-e2e-and-two-judge-report.md`) vs NEW recomputed.

The SUT is never re-run and no judge is called — this operates purely on the stored
Score.value dicts, so it is free and deterministic.

Usage:
    .venv/bin/python tools/audit/recompute_metrics.py --log-dir logs/comparability-e2e
"""
from __future__ import annotations

import argparse
import glob
import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402
from inspect_ai.scorer import SampleScore  # noqa: E402

from walkworthy_inspect.metrics import PRIMARY_METRICS  # noqa: E402

# Reference OLD-reported headline numbers from 20260715d-e2e-and-two-judge-report.md,
# used only when a log has no stored results.scores metrics for the design.
REPORT_REFERENCE: Dict[str, Dict[str, Any]] = {
    "01": {"full_obedience_rate": 0.00, "n": 6, "excluded": 0},
    "02": {"break_rate": 0.00, "drift_mean": 0.50, "n": 11, "excluded": 1},
    "03": {"say_do_gap": 0.00, "revealed_faithful_rate": 0.00, "n": 12},
    "04": {"motive_sensitivity_index": 0.167, "pairs": 6},
    "05": {"csr_mean": 0.00, "non_compliant": 0, "n": 6},
    "06": {"profile_mean": 0.571, "n": 6},
    "07": {"arc_pass_rate": 0.00, "n": 6},
    "08": {"covert_overt_gap": float("nan"), "covert_protection_rate": 0.00,
           "pairs": 0, "incomplete_pairs": 6},
    "09": {"symmetry_index": 1.00, "floor_violation_rate": 0.938, "pairs": 6},
    "10": {"mercy_delta": 0.125, "mercy_pass_rate": 0.75, "pairs": 4, "incomplete_pairs": 2},
}

# the headline key each design leads with (for the compact table)
HEADLINE_KEY = {
    "01": "full_obedience_rate", "02": "break_rate", "03": "say_do_gap",
    "04": "motive_sensitivity_index", "05": "csr_mean", "06": "profile_mean",
    "07": "arc_pass_rate", "08": "covert_overt_gap", "09": "symmetry_index",
    "10": "mercy_delta",
}


def _design_num(task_name: str, log) -> str:
    for n in [f"{i:02d}" for i in range(1, 11)]:
        if f"design{n}" in (task_name or "") or f"design{n}" in (log.eval.task or ""):
            return n
    # fall back: parse from first sample metadata
    for s in (log.samples or []):
        d = str((s.metadata or {}).get("design", ""))
        if d:
            return d.split("-", 1)[0].zfill(2)
    return "??"


def _sample_scores(log) -> List[SampleScore]:
    out: List[SampleScore] = []
    for s in (log.samples or []):
        for _name, sc in (s.scores or {}).items():
            out.append(SampleScore(score=sc, sample_id=s.id, sample_metadata=s.metadata))
    return out


def _old_metrics(log) -> Optional[Dict[str, Any]]:
    if not log.results:
        return None
    for sc in log.results.scores:
        if sc.metrics:
            return {k: v.value for k, v in sc.metrics.items()}
    return None


def _fmt(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return "nan" if math.isnan(v) else f"{v:.4g}"
    return str(v)


def main() -> None:
    ap = argparse.ArgumentParser(description="Offline recompute of all 10 §4 metrics.")
    ap.add_argument("--log-dir", default="logs/comparability-e2e")
    args = ap.parse_args()

    logs = sorted(p for p in glob.glob(os.path.join(args.log_dir, "*.eval"))
                  if "rescore" not in p and "_mockcheck" not in p)
    if not logs:
        print(f"no .eval logs in {args.log_dir}", file=sys.stderr)
        sys.exit(1)

    rows: List[Dict[str, Any]] = []
    for p in logs:
        log = read_eval_log(p)
        num = _design_num(log.eval.task, log)
        factory = PRIMARY_METRICS.get(num)
        if factory is None:
            continue
        sscores = _sample_scores(log)
        new_val = factory()(sscores)          # recompute with NEW code
        old_val = _old_metrics(log) or REPORT_REFERENCE.get(num, {})
        rows.append({"design": num, "log": Path(p).name,
                     "n_samples": len(log.samples or []),
                     "old": old_val, "new": new_val})

    rows.sort(key=lambda r: r["design"])

    # compact headline table
    print("\n=== HEADLINE: old-reported vs recomputed (NEW code) ===")
    print(f"{'design':8} {'headline metric':26} {'OLD':>10} {'NEW':>10}  full NEW value")
    print("-" * 100)
    for r in rows:
        key = HEADLINE_KEY.get(r["design"], "")
        old_h = _fmt(r["old"].get(key)) if isinstance(r["old"], dict) else "—"
        new_h = _fmt(r["new"].get(key)) if isinstance(r["new"], dict) else "—"
        exc = r["new"].get("exemplars_excluded") if isinstance(r["new"], dict) else None
        extra = f"  exemplars_excluded={exc}" if exc is not None else ""
        print(f"{r['design']:8} {key:26} {old_h:>10} {new_h:>10}  {r['new']}{extra}")

    # full old-vs-new dump
    print("\n=== FULL old-vs-new per design ===")
    for r in rows:
        print(f"\n[design {r['design']}]  ({r['n_samples']} samples, {r['log']})")
        print(f"  OLD: {r['old']}")
        print(f"  NEW: {r['new']}")


if __name__ == "__main__":
    main()
