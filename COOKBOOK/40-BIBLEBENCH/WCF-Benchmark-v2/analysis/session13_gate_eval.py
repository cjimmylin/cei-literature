#!/usr/bin/env python
"""Session-13 Phase-3 frontier-core GO/NO-GO evaluation.

PRE-STATED criterion (s12 boot prompt §6, unchanged from s6/s7, do not relitigate):
  GO  ⟺  ≥ 1/3 of new items show nonzero |qwen − haiku|  AND  unscored == 0.
Floor check: items where ALL three SUTs score 0 are flagged for re-review
(degenerate items are re-reviewed, not silently kept).

Reads every .eval log in the gate log dir (last-file-wins per (task,model)
for qwen partial-log merges), writes analysis/20260724-session13-gate-results.json.
"""
from __future__ import annotations

import glob
import json
from collections import defaultdict
from pathlib import Path

from inspect_ai.log import read_eval_log

V2 = Path(__file__).resolve().parent.parent
LOG_DIRS = [
    V2 / "logs" / "20260724-session13-gate-main",
]
SUTS = {
    "openrouter/qwen/qwen3.7-plus": "qwen",
    "openrouter/anthropic/claude-haiku-4.5": "haiku",
    "openrouter/openai/gpt-4o-mini": "gpt4omini",
}

def main() -> int:
    # scores[item][sut] = (value, n_valid); last-file-wins by filename sort
    scores: dict[str, dict] = defaultdict(dict)
    statuses = []
    for d in LOG_DIRS:
        for f in sorted(glob.glob(str(d / "*.eval"))):
            log = read_eval_log(f)
            sut = SUTS.get(log.eval.model)
            if sut is None:
                continue
            statuses.append((Path(f).name[:40], log.eval.model, log.status,
                             len(log.samples or [])))
            for s in (log.samples or []):
                for sc in (s.scores or {}).values():
                    panel = (sc.metadata or {}).get("panel") or {}
                    scores[s.id][sut] = {
                        "value": sc.value,
                        "n_valid": panel.get("n_valid"),
                        "panel_values": panel.get("values"),
                    }

    items = sorted(scores)
    n_items = len(items)
    unscored, missing, nonzero_gap, allzero = [], [], [], []
    rows = {}
    for iid in items:
        row = scores[iid]
        for sut in ("qwen", "haiku", "gpt4omini"):
            if sut not in row:
                missing.append((iid, sut))
        vals = {}
        for sut, rec in row.items():
            v = rec["value"]
            try:
                v = float(v)
            except (TypeError, ValueError):
                v = None
            if v is None or v != v:  # nan
                unscored.append((iid, sut))
            vals[sut] = v
        q, h = vals.get("qwen"), vals.get("haiku")
        gap = None
        if q is not None and h is not None and q == q and h == h:
            gap = abs(q - h)
            if gap > 0:
                nonzero_gap.append(iid)
        rows[iid] = {**{k: v for k, v in vals.items()}, "gap_qwen_haiku": gap}
        if all(v == 0 for v in vals.values() if v is not None) and vals:
            allzero.append(iid)

    frac = len(nonzero_gap) / n_items if n_items else 0.0
    go = (n_items == 80 and not unscored and not missing and frac >= 1 / 3)
    out = {
        "criterion": ">=1/3 nonzero |qwen-haiku| AND unscored==0 (pre-stated)",
        "n_items": n_items,
        "n_nonzero_gap": len(nonzero_gap),
        "fraction_nonzero_gap": round(frac, 4),
        "unscored": unscored,
        "missing": missing,
        "all_sut_zero_items": allzero,
        "verdict": "GO" if go else "NO-GO",
        "log_statuses": statuses,
        "per_item": rows,
        "nonzero_gap_items": nonzero_gap,
    }
    dest = V2 / "analysis" / "20260724-session13-gate-results.json"
    dest.write_text(json.dumps(out, indent=1))
    print(f"items {n_items} | nonzero-gap {len(nonzero_gap)} ({frac:.1%}) | "
          f"unscored {len(unscored)} | missing {len(missing)} | "
          f"all-zero {allzero} | VERDICT: {out['verdict']}")
    for name, model, status, n in statuses:
        print(f"  {name} {model} {status} n={n}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
