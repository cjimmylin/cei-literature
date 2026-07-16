#!/usr/bin/env python
"""Session-6 Phase-4 roster stats — bank v2.3.

Leaderboard form (binding, runbook + boot prompt):
  (a) full-bank mean (250 items: 228 main + 22 episodes, tier-level instrument)
  (b) frontier-core index (the 29 session-6 *-N-* items in wcf_main, own MDD)
Every number is EXPLORATORY, panel-median 0-100 rubric conformity on bank v2.3
(panel gemini-2.5-flash + deepseek-chat + mistral-small-2603, last-match parser,
excellence gate ON for main, episodes at pressure_variant=item).
Kin disclosures: deepseek-v3.2 is panel-self-kin (deepseek-chat grades it) —
the s5 DiD rule applies (±1.7-pt sensitivity on within-tier claims).

MDD80 (two-sided alpha=.05, power .80) = 2.80 * SE of the paired per-item
difference between two SUTs.

Writes analysis/20260716-session6-roster-stats.json.
"""
from __future__ import annotations

import glob
import json
import math
from collections import defaultdict
from pathlib import Path

from inspect_ai.log import read_eval_log

V2 = Path(__file__).resolve().parent.parent
LOG_DIRS = [
    V2 / "logs" / "20260716-session6-roster2-main",
    V2 / "logs" / "20260716-session6-roster2-episodes",
]
# Escalation-resilience panel (owner decision 2026-07-16: the 9 G4-excluded
# 4-turn episodes run as a STANDALONE panel, never mixed into the full-bank
# mean — they measure pressure-holding, a distinct construct).
PANEL_DIR = V2 / "logs" / "20260716-session6-roster2-panel"
SUT_ORDER = [
    "openrouter/qwen/qwen3.7-plus",
    "openrouter/anthropic/claude-haiku-4.5",
    "openrouter/openai/gpt-4o-mini",
    "openrouter/openai/gpt-5-mini",
    "openrouter/deepseek/deepseek-v3.2",
]
KIN_NOTES = {
    "openrouter/deepseek/deepseek-v3.2":
        "panel-self-kin (deepseek-chat grades it): s5 DiD rule — apply ±1.7-pt "
        "sensitivity to any within-tier claim involving this row",
}

def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")

def sd(xs):
    if len(xs) < 2:
        return float("nan")
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))

def main() -> int:
    # scores[model][item_id] = float; last-file-wins
    scores: dict[str, dict[str, float]] = defaultdict(dict)
    quorum_drops, unscored, statuses = [], [], []
    for d in LOG_DIRS:
        for f in sorted(glob.glob(str(d / "*.eval"))):
            log = read_eval_log(f)
            statuses.append((log.eval.task, log.eval.model, log.status,
                             len(log.samples or [])))
            for s in (log.samples or []):
                for sc in (s.scores or {}).values():
                    try:
                        v = float(sc.value)
                    except (TypeError, ValueError):
                        v = float("nan")
                    if v != v:
                        unscored.append((log.eval.model, s.id))
                        continue
                    scores[log.eval.model][s.id] = v
                    panel = (sc.metadata or {}).get("panel") or {}
                    if panel.get("n_valid") is not None and panel["n_valid"] < 3:
                        quorum_drops.append((log.eval.model, s.id, panel["n_valid"]))

    # Escalation panel scored separately (never merged into bank scores).
    panel_scores: dict[str, dict[str, float]] = defaultdict(dict)
    for f in sorted(glob.glob(str(PANEL_DIR / "*.eval"))):
        log = read_eval_log(f)
        statuses.append((log.eval.task, log.eval.model, log.status,
                         len(log.samples or [])))
        for s in (log.samples or []):
            for sc in (s.scores or {}).values():
                try:
                    v = float(sc.value)
                except (TypeError, ValueError):
                    v = float("nan")
                if v != v:
                    unscored.append((log.eval.model, s.id))
                    continue
                panel_scores[log.eval.model][s.id] = v
                pmeta = (sc.metadata or {}).get("panel") or {}
                if pmeta.get("n_valid") is not None and pmeta["n_valid"] < 3:
                    quorum_drops.append((log.eval.model, s.id, pmeta["n_valid"]))

    all_items = sorted({i for m in scores.values() for i in m})
    # frontier-core = session-6 items IN THE BANK (bank runs only; the panel's
    # NARROW-N ids are not in `scores` and must never enter this index).
    core_items = [i for i in all_items if "-N-" in i]
    assert not any(i.startswith("NARROW-N") for i in core_items), \
        "panel items leaked into bank scores"
    ep_items = [i for i in all_items if i.startswith("NARROW") and "-N-" not in i]
    main_items = [i for i in all_items if i not in ep_items]

    rows = []
    for m in SUT_ORDER:
        sm = scores.get(m, {})
        missing = [i for i in all_items if i not in sm]
        full = [sm[i] for i in all_items if i in sm]
        core = [sm[i] for i in core_items if i in sm]
        panel_vals = list(panel_scores.get(m, {}).values())
        rows.append({
            "model": m,
            "n_scored": len(sm),
            "missing": missing,
            "full_bank_mean": round(mean(full), 2),
            "full_bank_stderr": round(sd(full) / math.sqrt(len(full)), 2) if full else None,
            "main_mean": round(mean([sm[i] for i in main_items if i in sm]), 2),
            "episodes_mean": round(mean([sm[i] for i in ep_items if i in sm]), 2),
            "frontier_core_mean": round(mean(core), 2),
            "frontier_core_stderr": round(sd(core) / math.sqrt(len(core)), 2) if core else None,
            "escalation_panel_mean": round(mean(panel_vals), 2) if panel_vals else None,
            "escalation_panel_n": len(panel_vals),
            "kin_note": KIN_NOTES.get(m),
        })

    # pairwise MDD80 + observed gaps (full bank and frontier core)
    pairs = []
    for a_i in range(len(SUT_ORDER)):
        for b_i in range(a_i + 1, len(SUT_ORDER)):
            a, b = SUT_ORDER[a_i], SUT_ORDER[b_i]
            for label, pool in (("full", all_items), ("core", core_items)):
                diffs = [scores[a][i] - scores[b][i]
                         for i in pool if i in scores.get(a, {}) and i in scores.get(b, {})]
                if len(diffs) < 2:
                    continue
                se = sd(diffs) / math.sqrt(len(diffs))
                pairs.append({
                    "a": a.split("/")[-1], "b": b.split("/")[-1], "scope": label,
                    "n": len(diffs), "gap": round(mean(diffs), 2),
                    "se_diff": round(se, 2), "mdd80": round(2.80 * se, 2),
                    "significant_at_mdd80": abs(mean(diffs)) >= 2.80 * se,
                })

    out = {
        "bank_version": "v2.3",
        "panel": "gemini-2.5-flash + deepseek-chat + mistral-small-2603 (median)",
        "parser": "last-match GRADE, word-bounded, 4-digit reject",
        "config": "excellence_gate=ON (main), pressure_variant=item (episodes)",
        "epistemic_status": "EXPLORATORY / NON-QUOTABLE; panel-median rubric "
                            "conformity 0-100, NOT accuracy; v2.3 is a new scale "
                            "— never compare to v2.2/s4/s3/s2 numbers",
        "n_items": {"full": len(all_items), "main": len(main_items),
                    "episodes": len(ep_items), "frontier_core": len(core_items)},
        "leaderboard": rows,
        "pairwise": pairs,
        "unscored": unscored,
        "quorum_drops": quorum_drops,
        "log_statuses": statuses,
    }
    dest = V2 / "analysis" / "20260716-session6-roster-stats.json"
    dest.write_text(json.dumps(out, indent=1))
    print(f"items: {out['n_items']} | unscored: {len(unscored)} | "
          f"quorum drops: {len(quorum_drops)}")
    for r in rows:
        print(f"  {r['model'].split('/')[-1]:22s} full {r['full_bank_mean']:6.2f} "
              f"(main {r['main_mean']:6.2f} / ep {r['episodes_mean']:6.2f}) | "
              f"core {r['frontier_core_mean']:6.2f} | "
              f"escal-panel {r['escalation_panel_mean']} | n={r['n_scored']}"
              + (" | KIN" if r["kin_note"] else ""))
    print("pairwise (core scope):")
    for p in pairs:
        if p["scope"] == "core":
            print(f"  {p['a']:>16s} vs {p['b']:16s} gap {p['gap']:+6.2f} "
                  f"MDD80 {p['mdd80']:5.2f} {'SIG' if p['significant_at_mdd80'] else 'ns'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
