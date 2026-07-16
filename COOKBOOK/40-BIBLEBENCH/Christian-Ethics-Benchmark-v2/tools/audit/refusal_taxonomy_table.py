"""F4 Option B — descriptive 4-way refusal-taxonomy table (offline, adjacent data only).

Owner ruling 2026-07-16 (s7 decision grid #2): report the 4-way refusal taxonomy as a
DESCRIPTIVE adjacent table per SUT x design. This is NEVER a headline and carries NO
comparative language — it is refusal-calibration context (the CV-7 signal), adjacent to
the exclusion counts already reported. Primaries are computed elsewhere (metrics.py) and
never consume the refusal cell (grep-verified: zero refs).

What it does (zero model calls, zero network):
  - reads the stored per-design .eval logs under a --log-root (default logs/pilot-20260716,
    one subdir per SUT),
  - for each scored sample, RE-DERIVES the 4-way tag with the F4-B `engaged` derivation
    (scorers._refusal_cell), reading the judged Score.value dict as the `scores` input,
  - emits per (SUT x design) counts of {helpful, policy_violating_compliance,
    appropriate_refusal, unnecessary_refusal, pending_adjudication}, plus how many cells
    the F4-B engagement override flipped vs the stored (engaged=False) cell.

Gotchas honored:
  - sample_ids COLLIDE across SUTs -> every row is scoped by (sut, log basename,
    sample_id, rec_index); nothing is joined on sample_id alone.
  - Inspect Score.value rejects nested dicts, so 02/07 turn_states is JSON-encoded; we
    decode it before use (though the refusal cell for 02/07 uses the terminal turn only,
    matching the scorer's per-turn _refusal_cell call which passes {}).
  - Stratum-(c) refusal rows are labeled "policy-pending (Option C not ruled)" — the
    both-poles-decline DSP policy was NOT ruled (owner s7 grid; Option C stays open).

Usage:
    .venv/bin/python tools/audit/refusal_taxonomy_table.py --log-root logs/pilot-20260716
    .venv/bin/python tools/audit/refusal_taxonomy_table.py --log-root logs/pilot-20260716 \
        --json logs/f4-taxonomy-20260716/taxonomy.json
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

_V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_V2_ROOT))

from inspect_ai.log import read_eval_log  # noqa: E402

from walkworthy_inspect.refusal import (  # noqa: E402
    APPROPRIATE_REFUSAL, FOUR_WAY, HELPFUL, PENDING_ADJUDICATION,
    POLICY_VIOLATING, UNNECESSARY_REFUSAL,
)
from walkworthy_inspect.scorers import _refusal_cell  # noqa: E402
from walkworthy_inspect.rubrics import judge_categories, spec_for  # noqa: E402

TAGS = list(FOUR_WAY) + [PENDING_ADJUDICATION]


def _design_num(design_slug: str) -> str:
    return str(design_slug or "").split("-", 1)[0].zfill(2)


def _judge_scores_from_value(design_num: str, value: Any) -> Dict[str, Any]:
    """Extract the judged-category dict the refusal derivation should read.

    For the plain designs Score.value IS the {category: value} dict. For 02/07 the value
    is {"turn_states": <json str>, "turn_state": ..., ...}; the scorer's per-turn
    _refusal_cell call passes {} (engaged stays False there BY DESIGN), so we mirror that
    exactly by returning {} for the multi-turn designs — no turn_states leakage into the
    engagement signal. (turn_states is decoded here only for completeness / audit.)
    """
    if not isinstance(value, dict):
        return {}
    if "turn_states" in value:  # 02 / 07 per-turn cell — scorer passes {} -> mirror it
        return {}
    # keep only real judge categories for this design (drop 05 judge-free / bookkeeping)
    try:
        cat_names = {c.name for c in judge_categories(spec_for(design_num))}
    except KeyError:
        cat_names = set(value.keys())
    return {k: v for k, v in value.items() if k in cat_names}


def _response_text_from_sample(s) -> str:
    try:
        return s.output.completion if s.output else ""
    except Exception:
        return ""


def collect(log_root: str) -> Dict[str, Any]:
    sut_dirs = sorted(d for d in glob.glob(os.path.join(log_root, "*/"))
                      if os.path.isdir(d))
    # counts[(sut, design)] -> {tag: n}; flips[(sut, design)] -> n overrides fired
    counts: Dict[tuple, Dict[str, int]] = defaultdict(lambda: {t: 0 for t in TAGS})
    flips: Dict[tuple, int] = defaultdict(int)
    strat_c_refusals: Dict[tuple, int] = defaultdict(int)
    rows_seen = set()  # (sut, log basename, sample_id, rec_index) — collision-safe scope

    for d in sut_dirs:
        sut = Path(d.rstrip("/")).name
        for log_path in sorted(glob.glob(os.path.join(d, "*.eval"))):
            base = os.path.basename(log_path)
            log = read_eval_log(log_path)
            for rec_index, s in enumerate(log.samples or []):
                meta = s.metadata or {}
                design_num = _design_num(meta.get("design", ""))
                stratum = str(meta.get("stratum", "") or "").strip().lower()
                for _name, sc in (s.scores or {}).items():
                    key = (sut, base, s.id, rec_index)
                    if key in rows_seen:
                        continue
                    rows_seen.add(key)
                    scores = _judge_scores_from_value(design_num, sc.value)
                    resp = _response_text_from_sample(s)
                    # NEW cell (F4-B derived engaged)
                    new_cell = _refusal_cell(meta, resp, design_num, scores)
                    # OLD stored cell (engaged=False) — for the flip count
                    old_cell = (sc.metadata or {}).get("refusal") or {}
                    ck = (sut, design_num)
                    tag = new_cell["tag"] if new_cell["tag"] in counts[ck] else PENDING_ADJUDICATION
                    counts[ck][tag] += 1
                    if new_cell.get("lexical_override") and not old_cell.get("lexical_override"):
                        flips[ck] += 1
                    if stratum == "c" and new_cell["lexical"].get("is_refusal"):
                        strat_c_refusals[ck] += 1
    return {"counts": counts, "flips": flips, "strat_c_refusals": strat_c_refusals,
            "n_rows": len(rows_seen)}


def _fmt_counts_table(res: Dict[str, Any]) -> List[str]:
    counts = res["counts"]
    flips = res["flips"]
    strat_c = res["strat_c_refusals"]
    keys = sorted(counts.keys())
    out: List[str] = []
    hdr = (f"{'sut':18} {'dsg':4} {'helpful':8} {'polviol':8} {'apprRef':8} "
           f"{'unnecRef':9} {'pending':8} {'total':6} {'ovr_flip':8}")
    out.append(hdr)
    out.append("-" * len(hdr))
    for (sut, dsg) in keys:
        c = counts[(sut, dsg)]
        total = sum(c.values())
        out.append(
            f"{sut:18} {dsg:4} {c[HELPFUL]:8} {c[POLICY_VIOLATING]:8} "
            f"{c[APPROPRIATE_REFUSAL]:8} {c[UNNECESSARY_REFUSAL]:9} "
            f"{c[PENDING_ADJUDICATION]:8} {total:6} {flips[(sut,dsg)]:8}")
    # stratum-(c) policy-pending footnote rows
    scr = {k: v for k, v in strat_c.items() if v}
    if scr:
        out.append("")
        out.append("stratum-(c) refusal rows — policy-pending (Option C not ruled):")
        for (sut, dsg), n in sorted(scr.items()):
            out.append(f"  {sut:18} design {dsg}: {n} lexical-refusal row(s) "
                       f"[policy-pending (Option C not ruled)]")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Descriptive 4-way refusal-taxonomy table.")
    ap.add_argument("--log-root", default="logs/pilot-20260716")
    ap.add_argument("--json", default=None, help="optional path to also dump JSON")
    args = ap.parse_args()

    res = collect(args.log_root)
    print("=== F4 Option B — DESCRIPTIVE 4-way refusal taxonomy (adjacent data; "
          "no headline, no comparison) ===")
    print(f"log-root: {args.log_root}   rows: {res['n_rows']}")
    print()
    for line in _fmt_counts_table(res):
        print(line)
    print()
    print("Note: `ovr_flip` = rows where the F4-B engagement override newly fired vs the "
          "stored engaged=False cell. Primaries never consume this cell (metrics.py).")

    if args.json:
        os.makedirs(os.path.dirname(args.json) or ".", exist_ok=True)
        serial = {
            "log_root": args.log_root, "n_rows": res["n_rows"],
            "counts": {f"{s}|{d}": v for (s, d), v in res["counts"].items()},
            "override_flips": {f"{s}|{d}": v for (s, d), v in res["flips"].items()},
            "stratum_c_refusals_policy_pending": {
                f"{s}|{d}": v for (s, d), v in res["strat_c_refusals"].items() if v},
        }
        with open(args.json, "w") as fh:
            json.dump(serial, fh, indent=2)
        print(f"\nJSON written: {args.json}")


if __name__ == "__main__":
    main()
