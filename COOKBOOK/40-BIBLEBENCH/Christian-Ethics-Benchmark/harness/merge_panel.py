#!/usr/bin/env python3
"""Merge per-SUT WALKWORTHY panel runs into one combined run dir.

The O4 panel runs one resumable process PER SUT (per-SUT parallelism, F-1) into its
own run dir; this concatenates their `scored_items.jsonl` into a combined dir and
aggregates cost/defects/schema-errors into a combined `panel_summary.json`. Same
pattern the P0 pilot used (3 per-SUT dirs -> 20260709-p0-pilot).

Usage:
    python merge_panel.py --out 20260711-o4-panel \
        --runs 20260711-o4-gpt41 20260711-o4-gemini ... (per-SUT dir names)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark-root", default="..")
    ap.add_argument("--out", required=True, help="combined run dir name under runs/")
    ap.add_argument("--runs", nargs="+", required=True, help="per-SUT run dir names under runs/")
    args = ap.parse_args(argv)

    root = Path(args.benchmark_root)
    out_dir = root / "runs" / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    all_records = []
    seen = set()  # (item_id, model) dedupe guard (resume-safe)
    cost = {"total_usd": 0.0, "calls": 0, "prompt_tokens": 0, "completion_tokens": 0}
    judge_defects, classifier_defects = [], []
    schema_errors = 0
    suts, judges = [], None
    per_run = {}

    for rn in args.runs:
        rd = root / "runs" / rn
        sp = rd / "scored_items.jsonl"
        if not sp.exists():
            print(f"  !! missing {sp} — skipping")
            continue
        recs = [json.loads(l) for l in sp.read_text().splitlines() if l.strip()]
        n_new = 0
        for r in recs:
            k = (r["item_id"], r["model"])
            if k in seen:
                continue
            seen.add(k)
            all_records.append(r)
            n_new += 1
            schema_errors += len(r.get("schema_errors") or [])
        per_run[rn] = n_new
        summ = rd / "panel_summary.json"
        if summ.exists():
            s = json.loads(summ.read_text())
            c = s.get("cost") or {}
            for kk in cost:
                cost[kk] += c.get(kk, 0) or 0
            d = s.get("defects") or {}
            judge_defects += d.get("judge", [])
            classifier_defects += d.get("classifier", [])
            for su in s.get("suts", []):
                if su not in suts:
                    suts.append(su)
            if judges is None and s.get("judge_pair"):
                judges = s["judge_pair"].get("judges")

    # write combined scored_items.jsonl
    out_sp = out_dir / "scored_items.jsonl"
    with out_sp.open("w", encoding="utf-8") as f:
        for r in all_records:
            f.write(json.dumps(r) + "\n")

    models = sorted({r["model"] for r in all_records})
    combined = {
        "panel": args.out, "kind": "o4-panel",
        "n_records": len(all_records), "n_models": len(models),
        "suts": suts or [{"name": m, "family": m.split("/")[0]} for m in models],
        "judge_pair": {"judges": judges} if judges else None,
        "total_schema_errors": schema_errors,
        "defects": {"judge": judge_defects, "classifier": classifier_defects},
        "cost": {**cost, "total_usd": round(cost["total_usd"], 4)},
        "per_run_new_records": per_run,
        "source_runs": args.runs,
    }
    (out_dir / "panel_summary.json").write_text(json.dumps(combined, indent=2), encoding="utf-8")

    print(f"[merge] {len(all_records)} records ({len(models)} models) -> {out_sp}")
    print(f"[merge] schema_errors={schema_errors} judge_defects={len(judge_defects)} "
          f"classifier_defects={len(classifier_defects)} cost=${cost['total_usd']:.4f}")
    print(f"[merge] per-run new: {per_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
