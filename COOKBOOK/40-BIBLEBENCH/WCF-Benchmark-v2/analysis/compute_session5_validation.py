#!/usr/bin/env python
"""Compute session-5 validation results.

Reads all live eval logs from logs/20260716-session5-validation/{configY,configX-main,configX-episodes}/
and the s4 pilot baseline from analysis/20260716-session5-item-matrix.json.

Multiple eval files per SUT are merged: for each (sut, sample_id), use the score from the
latest eval file where that sample is present (so re-runs for previously-missing items take
precedence over the incomplete first run for those specific items). Items only present in the
first/incomplete run keep those values.

Outputs: analysis/20260716-session5-validation-results.json
"""

from __future__ import annotations

import glob
import json
import math
import os
from pathlib import Path
from collections import defaultdict

from inspect_ai.log import read_eval_log

BASE = Path(__file__).parent.parent

SUT_SLUGS = {
    "openrouter/qwen/qwen3.7-plus": "qwen3.7-plus",
    "openrouter/anthropic/claude-haiku-4.5": "claude-haiku-4.5",
    "openrouter/openai/gpt-4o-mini": "gpt-4o-mini",
}

SKIP_MODELS = {"mockllm/model"}

Y_ITEMS = set("COMP-C4-W305,CROSS-C9-W305,CROSS-XC-W307,DUTY-C8-W304,DUTY-C9-W307,AGG-C7-W204,AGG-C2-W201,AGG-C8-W303,COMP-C8-004,AGG-C7-W307,CROSS-C8-002,STED-C2-005,DUTY-C9-W306,STED-C2-W301,DUTY-C3-008".split(","))
XM_ITEMS = set("COMP-C2-002,DUTY-XC-W206,DUTY-C4-W301,COMP-C8-W306,COMP-C4-005,COMP-C7-009,AGG-C2-010,STED-C1-W201,CROSS-XC-W207,COMP-XC-W206,LIB-C4-002,AGG-C5-W304,AGG-C7-007,AGG-C8-W305".split(","))
EP_ITEMS = {"NARROW-C10-005"}


def load_eval_dir(log_dir: Path, config_name: str) -> list[dict]:
    """Load all live eval logs from a directory, merge multi-file runs (last file wins per sut+sample_id)."""
    best: dict[tuple[str, str], dict] = {}

    for eval_path in sorted(glob.glob(str(log_dir / "*.eval"))):
        log = read_eval_log(eval_path)
        model_full = log.eval.model
        if model_full in SKIP_MODELS:
            continue
        sut = SUT_SLUGS.get(model_full, model_full)
        task_args = log.eval.task_args or {}

        token_usage = None
        cost_est = None
        if log.stats:
            stats = log.stats
            try:
                tu = stats.model_usage
                if tu:
                    total_in = sum(v.input_tokens for v in tu.values() if v)
                    total_out = sum(v.output_tokens for v in tu.values() if v)
                    token_usage = {"input": total_in, "output": total_out}
            except Exception:
                pass
            try:
                cost_est = float(stats.total_cost) if hasattr(stats, "total_cost") and stats.total_cost else None
            except Exception:
                pass

        if not log.samples:
            continue

        for s in log.samples:
            score_obj = s.scores.get("multi_scorer") if s.scores else None
            score_val = score_obj.value if score_obj else None
            is_unscored = (score_val is None) or (isinstance(score_val, float) and math.isnan(score_val))
            panel_n_valid = None
            panel_values = None
            if score_obj and score_obj.metadata:
                meta = score_obj.metadata
                panel = meta.get("panel", {})
                panel_n_valid = panel.get("n_valid")
                panel_values = panel.get("values")

            key = (sut, s.id)
            best[key] = {
                "config": config_name,
                "sut": sut,
                "sut_full": model_full,
                "task": log.eval.task,
                "task_args": task_args,
                "sample_id": s.id,
                "score": None if is_unscored else float(score_val),
                "is_unscored": is_unscored,
                "panel_n_valid": panel_n_valid,
                "panel_values": panel_values,
                "eval_file": os.path.basename(eval_path),
                "token_usage": token_usage,
                "cost_est_usd": cost_est,
            }

    return list(best.values())


def pilot_baseline(item_matrix_path: Path, suts_of_interest: set[str]) -> dict[str, dict]:
    with open(item_matrix_path) as f:
        data = json.load(f)
    pilot_rows = data.get("pilot", [])

    by_item: dict[str, list[dict]] = {}
    for r in pilot_rows:
        sid = r["sample_id"]
        if r["sut"] not in suts_of_interest:
            continue
        if sid not in by_item:
            by_item[sid] = []
        by_item[sid].append(r)

    result = {}
    for sid, rows in by_item.items():
        sut_scores = {r["sut"]: r["score"] for r in rows if r["score"] is not None}
        all_panel_spreads = []
        for r in rows:
            pv = r.get("panel_values")
            if pv and len([x for x in pv if x is not None]) >= 2:
                pv_clean = [x for x in pv if x is not None]
                all_panel_spreads.append(max(pv_clean) - min(pv_clean))
        mean_panel_spread = (sum(all_panel_spreads) / len(all_panel_spreads)) if all_panel_spreads else None
        result[sid] = {
            "sut_scores": sut_scores,
            "mean_panel_spread": mean_panel_spread,
        }
    return result


def main():
    val_dir = BASE / "logs" / "20260716-session5-validation"
    item_matrix_path = BASE / "analysis" / "20260716-session5-item-matrix.json"

    config_y_rows = load_eval_dir(val_dir / "configY", "configY")
    config_x_main_rows = load_eval_dir(val_dir / "configX-main", "configX-main")
    config_x_ep_rows = load_eval_dir(val_dir / "configX-episodes", "configX-episodes")

    all_rows = config_y_rows + config_x_main_rows + config_x_ep_rows

    suts_of_interest = set(SUT_SLUGS.values())
    pilot_base = pilot_baseline(item_matrix_path, suts_of_interest)

    by_config_item: dict[tuple, list[dict]] = defaultdict(list)
    for r in all_rows:
        by_config_item[(r["config"], r["sample_id"])].append(r)

    item_derived = {}
    for (config, sid), rows in by_config_item.items():
        sut_scores = {r["sut"]: r["score"] for r in rows}
        qwen_score = sut_scores.get("qwen3.7-plus")
        haiku_score = sut_scores.get("claude-haiku-4.5")
        tier1_spread = abs(qwen_score - haiku_score) if (qwen_score is not None and haiku_score is not None) else None

        val_panel_spreads = []
        for r in rows:
            pv = r.get("panel_values")
            if pv and len([x for x in pv if x is not None]) >= 2:
                pv_clean = [x for x in pv if x is not None]
                val_panel_spreads.append(max(pv_clean) - min(pv_clean))
        val_mean_panel_spread = (sum(val_panel_spreads) / len(val_panel_spreads)) if val_panel_spreads else None

        pilot_item = pilot_base.get(sid)
        pilot_mean_panel_spread = pilot_item["mean_panel_spread"] if pilot_item else None

        key = f"{config}::{sid}"
        item_derived[key] = {
            "config": config,
            "sample_id": sid,
            "sut_scores": sut_scores,
            "tier1_spread_abs": round(tier1_spread, 1) if tier1_spread is not None else None,
            "val_mean_panel_spread": round(val_mean_panel_spread, 2) if val_mean_panel_spread is not None else None,
            "pilot_mean_panel_spread": round(pilot_mean_panel_spread, 2) if pilot_mean_panel_spread is not None else None,
        }

    unscored = [r for r in all_rows if r["is_unscored"]]
    quorum_failures = [r for r in all_rows if r["panel_n_valid"] is not None and r["panel_n_valid"] < 3]

    # Coverage audit
    coverage_issues = []
    for sut in SUT_SLUGS.values():
        y_got = {r["sample_id"] for r in config_y_rows if r["sut"] == sut}
        xm_got = {r["sample_id"] for r in config_x_main_rows if r["sut"] == sut}
        ep_got = {r["sample_id"] for r in config_x_ep_rows if r["sut"] == sut}
        for config_name, expected_set, got_set in [
            ("configY", Y_ITEMS, y_got),
            ("configX-main", XM_ITEMS, xm_got),
            ("configX-episodes", EP_ITEMS, ep_got),
        ]:
            missing = expected_set - got_set
            if missing:
                coverage_issues.append({"config": config_name, "sut": sut, "missing": sorted(missing)})

    # Cost
    eval_costs: dict[str, float | None] = {}
    for r in all_rows:
        ef = r["eval_file"]
        if ef not in eval_costs:
            eval_costs[ef] = r["cost_est_usd"]
    total_cost = sum(v for v in eval_costs.values() if v is not None)

    eval_tokens: dict[str, dict | None] = {}
    for r in all_rows:
        ef = r["eval_file"]
        if ef not in eval_tokens:
            eval_tokens[ef] = r["token_usage"]

    output = {
        "generated": "2026-07-16",
        "description": (
            "Session-5 v2.2 validation run. "
            "configY: excellence_gate=true, 15 DEAD items x3 SUTs. "
            "configX-main: excellence_gate=false, 14 repaired items (11 Lever-B + 3 Lever-C contested) x3 SUTs. "
            "configX-episodes: wcf_episodes, pressure_variant=item, NARROW-C10-005 x3 SUTs. "
            "Qwen background runs had partial completions; re-runs issued and merged (last-file-wins)."
        ),
        "suts": list(SUT_SLUGS.values()),
        "counts": {
            "configY_rows": len(config_y_rows),
            "configX_main_rows": len(config_x_main_rows),
            "configX_episodes_rows": len(config_x_ep_rows),
            "total_rows": len(all_rows),
            "expected_total": 45 + 42 + 3,
            "unscored_count": len(unscored),
            "quorum_failures_count": len(quorum_failures),
        },
        "coverage_issues": coverage_issues,
        "unscored_rows": [{"config": r["config"], "sut": r["sut"], "sample_id": r["sample_id"]} for r in unscored],
        "quorum_failures": [
            {"config": r["config"], "sut": r["sut"], "sample_id": r["sample_id"], "n_valid": r["panel_n_valid"]}
            for r in quorum_failures
        ],
        "per_sample_rows": all_rows,
        "per_item_derived": item_derived,
        "cost": {
            "per_eval_file_usd": eval_costs,
            "total_estimated_usd": round(total_cost, 4),
            "note": (
                "cost_est from inspect log stats.total_cost; None if field absent. "
                "Concurrent regrade job on same key: credits delta unreliable."
            ),
        },
        "token_usage_per_eval": eval_tokens,
    }

    out_path = BASE / "analysis" / "20260716-session5-validation-results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"Written: {out_path}")
    print(f"Total rows: {len(all_rows)} (expected 90)")
    print(f"Unscored: {len(unscored)}")
    print(f"Quorum failures (n_valid<3): {len(quorum_failures)}")
    if coverage_issues:
        print(f"\nCoverage gaps ({len(coverage_issues)} issues):")
        for ci in coverage_issues:
            print(f"  {ci['config']:16s}  {ci['sut']:22s}  missing={ci['missing']}")
    else:
        print("Coverage: complete (no missing items)")
    print(f"Estimated cost: ${total_cost:.4f} (from inspect log stats)")

    print()
    print("=== CONFIG Y: per-item scores + |qwen−haiku| ===")
    print(f"  {'item':22s}  {'qwen':>6}  {'haiku':>6}  {'gpt4o':>6}  {'|q-h|':>5}")
    print(f"  {'-'*22}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*5}")
    for sid in sorted(Y_ITEMS):
        key = f"configY::{sid}"
        d = item_derived.get(key, {})
        sc = d.get("sut_scores", {})
        q = sc.get("qwen3.7-plus")
        h = sc.get("claude-haiku-4.5")
        g = sc.get("gpt-4o-mini")
        t1s = d.get("tier1_spread_abs")
        print(f"  {sid:22s}  {str(q) if q is not None else 'MISS':>6}  {str(h) if h is not None else 'MISS':>6}  {str(g) if g is not None else 'MISS':>6}  {str(t1s) if t1s is not None else 'MISS':>5}")

    print()
    print("=== CONFIG X-main: scores + val_panel_spread vs pilot_panel_spread ===")
    print(f"  {'item':22s}  {'qwen':>6}  {'haiku':>6}  {'gpt4o':>6}  {'val_ps':>6}  {'plt_ps':>6}")
    print(f"  {'-'*22}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*6}")
    for sid in sorted(XM_ITEMS):
        key = f"configX-main::{sid}"
        d = item_derived.get(key, {})
        sc = d.get("sut_scores", {})
        q = sc.get("qwen3.7-plus")
        h = sc.get("claude-haiku-4.5")
        g = sc.get("gpt-4o-mini")
        vps = d.get("val_mean_panel_spread")
        pps = d.get("pilot_mean_panel_spread")
        print(f"  {sid:22s}  {str(q) if q is not None else 'MISS':>6}  {str(h) if h is not None else 'MISS':>6}  {str(g) if g is not None else 'MISS':>6}  {str(vps) if vps is not None else 'N/A':>6}  {str(pps) if pps is not None else 'N/A':>6}")

    print()
    print("=== CONFIG X-episodes: NARROW-C10-005 ===")
    for r in sorted(config_x_ep_rows, key=lambda x: x["sut"]):
        pv = r["panel_values"]
        pv_str = str(pv) if pv else "None"
        print(f"  {r['sut']:22s}  score={r['score']}  n_valid={r['panel_n_valid']}  panel={pv_str}")


if __name__ == "__main__":
    main()
