#!/usr/bin/env python
"""Session-8 addendum: epochs x3 on minimax-m3 frontier core.

Resolves the s7 dangling comparison — minimax-m3 scored 80.45 SINGLE-DRAW on the
66-item core (roster-main) vs gpt-5-mini 78.39 EPOCHS-AVERAGED; not comparable.
This run grades minimax under the identical frozen config (wcf_frontier_core,
--epochs 3, DEFAULT_GRADER median-of-3 panel, excellence_gate=true, temp 0), so
the epochs-averaged means ARE comparable.

Reads:
  logs/20260717-session8-minimax-epochs-core/*.eval   (this run)
  logs/20260716-session7-epochs-core/*.eval           (s7 trio, for paired stats)
Per-item scores are epoch-averaged before any pairwise statistic (same as
compute_session7_epochs_stats.py). MDD80 = 2.80 * SE of paired per-item diffs.

Writes analysis/20260717-session8-minimax-core-stats.json.
"""
from __future__ import annotations

import glob
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

from inspect_ai.log import read_eval_log

V2 = Path(__file__).resolve().parent.parent
MINIMAX_DIR = V2 / "logs" / "20260717-session8-minimax-epochs-core"
TRIO_DIR = V2 / "logs" / "20260716-session7-epochs-core"
OUT = V2 / "analysis" / "20260717-session8-minimax-core-stats.json"
SUTS = {
    "openrouter/minimax/minimax-m3": "minimax",
    "openrouter/openai/gpt-5-mini": "gpt5mini",
    "openrouter/qwen/qwen3.7-plus": "qwen",
    "openrouter/anthropic/claude-haiku-4.5": "haiku",
}


def collect(log_dir: Path) -> tuple[dict, list, list]:
    per: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list))
    unscored, statuses = [], []
    for f in sorted(glob.glob(str(log_dir / "*.eval"))):
        log = read_eval_log(f)
        statuses.append((Path(f).name[:40], log.eval.model, log.status,
                         len(log.samples or [])))
        for s in (log.samples or []):
            for sc in (s.scores or {}).values():
                try:
                    v = float(sc.value)
                except (TypeError, ValueError):
                    v = float("nan")
                if v != v:
                    unscored.append((log.eval.model, str(s.id), s.epoch))
                else:
                    per[log.eval.model][str(s.id)].append(v)
    return per, unscored, statuses


def main() -> int:
    per, unscored, statuses = collect(MINIMAX_DIR)
    per_trio, uns_trio, st_trio = collect(TRIO_DIR)
    per.update(per_trio)
    unscored += uns_trio
    statuses += st_trio

    item_means: dict[str, dict[str, float]] = {}
    for model, items in per.items():
        tag = SUTS.get(model)
        if tag is None:
            continue
        item_means[tag] = {iid: mean(vals) for iid, vals in items.items()}

    suts = {}
    for tag, items in item_means.items():
        vals = list(items.values())
        suts[tag] = {
            "n_items": len(vals),
            "n_epoch_scores": sum(len(per_[iid]) for per_ in
                                  [per[m] for m in per if SUTS.get(m) == tag]
                                  for iid in items),
            "mean": round(mean(vals), 2),
            "stderr": round(stdev(vals) / math.sqrt(len(vals)), 2),
        }

    pairs = {}
    # focus: minimax vs each s7 trio member
    for b in ("gpt5mini", "qwen", "haiku"):
        if "minimax" not in item_means or b not in item_means:
            continue
        common = sorted(set(item_means["minimax"]) & set(item_means[b]))
        diffs = [item_means["minimax"][x] - item_means[b][x] for x in common]
        se = stdev(diffs) / math.sqrt(len(diffs))
        g = mean(diffs)
        pairs[f"minimax-vs-{b}"] = {
            "n": len(common), "gap": round(g, 2), "se_diff": round(se, 2),
            "mdd80": round(2.80 * se, 2),
            "significant_at_mdd80": bool(abs(g) >= 2.80 * se),
        }

    out = {
        "bank_version": "v2.4", "task": "wcf_frontier_core", "epochs": 3,
        "grader_panel": "median(gemini-2.5-flash, deepseek-chat, "
                        "mistral-small-2603)",
        "excellence_gate": True, "grader_temperature": 0.0,
        "note": "minimax epochs-averaged core mean is now COMPARABLE to the s7 "
                "epochs trio (identical frozen config). Resolves s7's single-"
                "draw 80.45 vs epochs 78.39 non-comparability. MDD80 = 2.80*SE "
                "paired per-item; scale is bank v2.4 (not cross-bank quotable).",
        "log_statuses": [list(s) for s in statuses],
        "unscored": [list(u) for u in unscored],
        "n_unscored": len(unscored),
        "suts": suts, "pairwise": pairs,
        "s7_reference_single_draw": {"minimax_core": 80.45,
                                     "source": "reports/20260716-session7-report.md"},
    }
    OUT.write_text(json.dumps(out, indent=1))
    print(f"unscored: {len(unscored)}")
    for tag in ("minimax", "gpt5mini", "qwen", "haiku"):
        if tag in suts:
            s = suts[tag]
            print(f"  {tag:9s} mean {s['mean']:6.2f}  se {s['stderr']:5.2f}  "
                  f"n_items {s['n_items']}")
    for k, p in pairs.items():
        print(f"  {k:20s} gap {p['gap']:+6.2f}  MDD80 {p['mdd80']:5.2f}  "
              f"{'SIG' if p['significant_at_mdd80'] else 'ns'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
