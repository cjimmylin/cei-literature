#!/usr/bin/env python
"""Session-7 track-1 stats: epochs x3 on the expanded (66-item) frontier core.

Reads logs/20260716-session7-epochs-core/*.eval (frontier trio, --epochs 3) and
logs/20260716-session7-qwen-ramp/*.eval (qwen x wcf_new_episodes x3).

Per-item scores are EPOCH-AVERAGED before any pairwise statistic, so the paired
SE reflects the epochs-shrunk per-item noise. MDD80 (two-sided alpha=.05,
power .80) = 2.80 * SE of the paired per-item differences (same convention as
compute_session6_roster_stats.py — comparable definition, NOT comparable scale:
bank v2.4 is a new instrument).

Writes analysis/20260716-session7-epochs-stats.json.
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
CORE_DIR = V2 / "logs" / "20260716-session7-epochs-core"
RAMP_DIR = V2 / "logs" / "20260716-session7-qwen-ramp"
SUTS = {
    "openrouter/qwen/qwen3.7-plus": "qwen",
    "openrouter/anthropic/claude-haiku-4.5": "haiku",
    "openrouter/openai/gpt-5-mini": "gpt5mini",
}


def collect(log_dir: Path) -> tuple[dict, list, list]:
    """per_model[model][item_id] = [epoch scores]; plus unscored + statuses."""
    per: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
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
                    unscored.append((log.eval.model, s.id, s.epoch))
                else:
                    per[log.eval.model][s.id].append(v)
    return per, unscored, statuses


def main() -> int:
    per, unscored, statuses = collect(CORE_DIR)
    out: dict = {"scope": "expanded frontier core (66 v2.4 *-N-* items) x epochs 3",
                 "bank_version": "v2.4", "epochs": 3,
                 "log_statuses": statuses, "unscored": unscored}

    item_means: dict[str, dict[str, float]] = {}
    for model, items in per.items():
        tag = SUTS.get(model)
        if tag is None:
            continue
        item_means[tag] = {iid: mean(vals) for iid, vals in items.items()}

    suts = {}
    for model, items in per.items():
        tag = SUTS.get(model)
        if tag is None:
            continue
        vals = list(item_means[tag].values())
        suts[tag] = {
            "n_items": len(vals),
            "n_epoch_scores": sum(len(v) for v in items.values()),
            "mean": round(mean(vals), 2),
            "stderr": round(stdev(vals) / math.sqrt(len(vals)), 2),
        }
    out["suts"] = suts

    pairs = {}
    tags = sorted(item_means)
    for i, a in enumerate(tags):
        for b in tags[i + 1:]:
            common = sorted(set(item_means[a]) & set(item_means[b]))
            diffs = [item_means[a][x] - item_means[b][x] for x in common]
            se = stdev(diffs) / math.sqrt(len(diffs))
            pairs[f"{a}-vs-{b}"] = {
                "n": len(common),
                "gap": round(mean(diffs), 2),
                "se_diff": round(se, 2),
                "mdd80": round(2.80 * se, 2),
                "significant_at_mdd80": abs(mean(diffs)) >= 2.80 * se,
            }
    out["pairwise"] = pairs

    # qwen ramp probe (9 escalation-panel episodes x epochs 3)
    ramp_per, ramp_unscored, ramp_statuses = collect(RAMP_DIR)
    ramp = {}
    for model, items in ramp_per.items():
        for iid, vals in sorted(items.items()):
            ramp[iid] = {"epoch_scores": vals, "mean": round(mean(vals), 2)}
    ep_means = [r["mean"] for r in ramp.values()]
    out["qwen_ramp_probe"] = {
        "log_statuses": ramp_statuses,
        "unscored": ramp_unscored,
        "per_episode": ramp,
        "panel_mean_of_episode_means": round(mean(ep_means), 2) if ep_means else None,
    }

    dest = V2 / "analysis" / "20260716-session7-epochs-stats.json"
    dest.write_text(json.dumps(out, indent=1))
    print(f"core items per SUT: "
          f"{ {t: s['n_items'] for t, s in suts.items()} } | unscored {len(unscored)}")
    for t, s in suts.items():
        print(f"  {t:9s} mean {s['mean']:6.2f}  se {s['stderr']:5.2f}")
    for k, p in pairs.items():
        print(f"  {k:18s} gap {p['gap']:6.2f}  MDD80 {p['mdd80']:5.2f} "
              f"{'SIG' if p['significant_at_mdd80'] else 'ns'}")
    if ep_means:
        print(f"  qwen ramp panel mean {out['qwen_ramp_probe']['panel_mean_of_episode_means']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
