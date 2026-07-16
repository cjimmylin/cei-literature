#!/usr/bin/env python
"""WCF-Benchmark-v2 Session 5 — kin-delta measurement matrix (EXPLORATORY / NON-QUOTABLE).

Re-grade session-3 SUT responses (logs/20260715-sut-sweep) for 3 SUTs
(deepseek-chat [kin], mistral-large-2512 [kin], qwen3.7-plus [non-kin CONTROL])
under 4 graders:
  - deepseek   : openrouter/deepseek/deepseek-chat          (default-panel kin)
  - mistral_small: openrouter/mistralai/mistral-small-2603  (default-panel kin)
  - nova       : openrouter/amazon/nova-pro-v1               (kin-free substitute)
  - command_r  : openrouter/cohere/command-r-08-2024         (kin-free substitute)

Incumbent gemini grade read from persisted score (no re-spend).

Replay is byte-identical: prompt = sample.scores['model_graded_qa']
    .metadata['grading'][0]['content']  (role=user, grade-free)

Grade parsing: last GRADE: N (0-100) wins — same as harness.

Usage:
    set -a && source ~/.codex/secrets/openrouter.env && set +a
    ./.venv-v2/bin/python analysis/session5_kin_regrade.py [--smoke] [--full]
"""
from __future__ import annotations

import argparse
import asyncio
import glob
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from inspect_ai.log import read_eval_log
from inspect_ai.model import GenerateConfig, ChatMessageUser, get_model

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
V2_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = V2_ROOT / "logs" / "20260715-sut-sweep"
OUT_DIR = V2_ROOT / "analysis"

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
GRADE_PATTERN = r"GRADE:\s*(\d{1,3})"

# SUTs to include (llama-4-maverick excluded per mission spec)
INCLUDE_SUTS = {
    "openrouter/deepseek/deepseek-chat",
    "openrouter/mistralai/mistral-large-2512",
    "openrouter/qwen/qwen3.7-plus",
}

# Grader definitions — primary slugs (may be swapped after smoke if needed)
GRADERS_PRIMARY = {
    "deepseek":      "openrouter/deepseek/deepseek-chat",
    "mistral_small": "openrouter/mistralai/mistral-small-2603",
    "nova":          "openrouter/amazon/nova-pro-v1",
    "command_r":     "openrouter/cohere/command-r-08-2024",
}

# Fallback slugs for nova and command_r if smoke fails (>2/10 unparseable)
GRADER_FALLBACKS = {
    "nova":      "openrouter/amazon/nova-lite-v1",
    "command_r": "openrouter/cohere/command-r-plus-08-2024",
}

CONCURRENCY = 12
MAX_RETRIES = 5

# Output file names (dated, immutable)
DATE = "20260716"
RAW_OUT      = OUT_DIR / f"{DATE}-session5-kin-regrade-raw.json"
MATRIX_OUT   = OUT_DIR / f"{DATE}-session5-kin-matrix.json"
STATS_OUT    = OUT_DIR / f"{DATE}-session5-kin-stats.json"
SMOKE_LOG    = OUT_DIR / f"{DATE}-session5-smoke-log.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_grade(text: str) -> int | None:
    """Return the LAST GRADE: N in grader output, or None. 0-100 only."""
    matches = re.findall(GRADE_PATTERN, text or "")
    if not matches:
        return None
    val = int(matches[-1])
    return val if 0 <= val <= 100 else None


def load_samples() -> list[dict]:
    """Read all session-3 SUT-sweep logs; return one row per (sample, SUT)
    for the 3 included SUTs only."""
    rows = []
    for f in sorted(glob.glob(str(LOG_DIR / "*.eval"))):
        log = read_eval_log(f)
        sut = log.eval.model
        if sut not in INCLUDE_SUTS:
            continue
        task = log.eval.task  # wcf_main | wcf_episodes
        for s in log.samples:
            sc = s.scores.get("model_graded_qa")
            if sc is None:
                continue
            grading = (sc.metadata or {}).get("grading")
            if not grading:
                continue
            # grading[0] is role=user (the replay prompt, grade-free)
            prompt = grading[0]["content"]
            try:
                gem = int(float(sc.value))
            except (TypeError, ValueError):
                gem = None
            meta = s.metadata or {}
            rows.append({
                "sample_id": str(s.id),
                "sut": sut,
                "task": task,
                "design":    meta.get("design"),
                "kind":      meta.get("kind"),
                "tier":      meta.get("tier"),
                "contested": meta.get("contested"),
                "episode":   meta.get("episode"),
                "track":     meta.get("track"),
                "prompt":    prompt,
                "gemini":    gem,
            })
    return rows


async def grade_one(model, prompt: str) -> tuple[int | None, str]:
    for attempt in range(MAX_RETRIES):
        try:
            out = await model.generate([ChatMessageUser(content=prompt)])
            comp = out.completion
            return parse_grade(comp), comp
        except Exception as e:
            wait = min(2 ** attempt, 30)
            print(f"    retry {attempt+1}/{MAX_RETRIES} after {wait}s: {e}")
            await asyncio.sleep(wait)
    return None, "ERROR: max retries exceeded"


async def run_grader_batch(
    name: str,
    slug: str,
    rows: list[dict],
    result_key: str | None = None,
) -> None:
    """Grade all rows with the given grader; results stored in row[result_key]."""
    if result_key is None:
        result_key = name
    model = get_model(slug, config=GenerateConfig(temperature=0.0))
    sem = asyncio.Semaphore(CONCURRENCY)
    done = 0
    t0 = time.time()

    async def worker(row: dict):
        nonlocal done
        async with sem:
            grade, comp = await grade_one(model, row["prompt"])
        row[result_key] = grade
        row[f"{result_key}_raw"] = comp[-500:] if comp else ""
        row[f"{result_key}_n_retries"] = 0  # simplified (retries counted inside grade_one)
        done += 1
        if done % 50 == 0 or done == len(rows):
            print(f"  [{name}] {done}/{len(rows)}  ({time.time()-t0:.0f}s elapsed)")

    await asyncio.gather(*(worker(r) for r in rows))
    none_ct = sum(1 for r in rows if r.get(result_key) is None)
    pct = 100 * none_ct / max(len(rows), 1)
    print(f"  [{name}] DONE {len(rows)} rows, {none_ct} unparseable ({pct:.1f}%), {time.time()-t0:.0f}s")
    return none_ct


# ---------------------------------------------------------------------------
# Smoke test logic
# ---------------------------------------------------------------------------

def pick_smoke_rows(rows: list[dict], n: int = 10) -> list[int]:
    """Pick n diverse indices: mix of 3 SUTs, include >=2 episodes."""
    sut_list = [
        "openrouter/deepseek/deepseek-chat",
        "openrouter/mistralai/mistral-large-2512",
        "openrouter/qwen/qwen3.7-plus",
    ]
    indices = []
    # First grab 2 episode rows from different SUTs
    ep_found = 0
    for i, r in enumerate(rows):
        if r["task"] == "wcf_episodes" and ep_found < 2:
            indices.append(i)
            ep_found += 1
        if ep_found >= 2:
            break
    # Then fill from each SUT (main task)
    per_sut = {s: [] for s in sut_list}
    for i, r in enumerate(rows):
        if i not in indices and r["task"] == "wcf_main":
            per_sut[r["sut"]].append(i)
    remaining = n - len(indices)
    per = max(1, remaining // 3)
    for sut in sut_list:
        for idx in per_sut[sut][:per]:
            if len(indices) < n and idx not in indices:
                indices.append(idx)
    # top up if needed
    for i in range(len(rows)):
        if len(indices) >= n:
            break
        if i not in indices:
            indices.append(i)
    return indices[:n]


async def run_smoke(rows: list[dict], smoke_indices: list[int]) -> dict:
    """Run nova and command_r on 10 smoke rows; return swap decisions."""
    smoke_rows = [rows[i] for i in smoke_indices]
    swaps = {}
    smoke_results = {}

    for name, primary_slug in [("nova", GRADERS_PRIMARY["nova"]),
                                 ("command_r", GRADERS_PRIMARY["command_r"])]:
        print(f"\nSMOKE [{name}] using {primary_slug} on {len(smoke_rows)} rows...")
        tmp_key = f"smoke_{name}"
        none_ct = await run_grader_batch(name, primary_slug, smoke_rows, result_key=tmp_key)
        unparseable = sum(1 for r in smoke_rows if r.get(tmp_key) is None)
        print(f"  SMOKE [{name}]: {unparseable}/10 unparseable")
        if unparseable > 2:
            fb = GRADER_FALLBACKS[name]
            print(f"  SMOKE [{name}] FAIL ({unparseable}>2) — swapping to fallback: {fb}")
            # Try fallback
            tmp_key2 = f"smoke_{name}_fb"
            none_ct2 = await run_grader_batch(name + "_fallback", fb, smoke_rows, result_key=tmp_key2)
            swaps[name] = {"original": primary_slug, "fallback": fb, "reason": f"{unparseable}/10 unparseable on primary"}
            # copy fallback results into the canonical key
            for r in smoke_rows:
                r[f"smoke_{name}_final"] = r.get(tmp_key2)
            smoke_results[name] = {"slug": fb, "unparseable_primary": unparseable, "swapped": True}
        else:
            swaps[name] = None
            for r in smoke_rows:
                r[f"smoke_{name}_final"] = r.get(tmp_key)
            smoke_results[name] = {"slug": primary_slug, "unparseable": unparseable, "swapped": False}

    return swaps, smoke_results, smoke_rows


# ---------------------------------------------------------------------------
# Full run
# ---------------------------------------------------------------------------

async def run_full(
    rows: list[dict],
    smoke_indices: list[int],
    smoke_rows: list[dict],
    swaps: dict,
    final_slugs: dict,
) -> None:
    """Run all 4 graders on the full 678 rows.
    For nova/command_r: reuse already-graded smoke rows (avoid re-spend).
    For deepseek/mistral_small: grade everything fresh.
    """
    # Build index set for smoke rows (already graded for nova/command_r)
    smoke_set = set(smoke_indices)

    # Propagate smoke grades into main rows for nova and command_r
    smoke_idx_to_row = {i: rows[i] for i in smoke_indices}
    for k, smoke_r in zip(smoke_indices, smoke_rows):
        for g in ["nova", "command_r"]:
            key = f"smoke_{g}_final"
            if key in smoke_r:
                rows[k][g] = smoke_r[key]
                rows[k][f"{g}_raw"] = smoke_r.get(f"smoke_{g}_raw", "")

    # For nova and command_r: only grade the non-smoke rows
    for name in ["nova", "command_r"]:
        slug = final_slugs[name]
        non_smoke_rows = [r for i, r in enumerate(rows) if i not in smoke_set]
        print(f"\nFULL [{name}] using {slug} on {len(non_smoke_rows)} non-smoke rows...")
        await run_grader_batch(name, slug, non_smoke_rows)
        # Merge back (the rows list shares references, so direct writes work)

    # For deepseek and mistral_small: grade ALL rows
    for name, slug in [("deepseek", final_slugs["deepseek"]),
                        ("mistral_small", final_slugs["mistral_small"])]:
        print(f"\nFULL [{name}] using {slug} on {len(rows)} rows...")
        await run_grader_batch(name, slug, rows)


# ---------------------------------------------------------------------------
# Save / stats helpers
# ---------------------------------------------------------------------------

def save_raw(rows: list[dict], swaps: dict, final_slugs: dict,
             credits_before: float, credits_after: float | None) -> None:
    per_grader = {}
    for name in ["deepseek", "mistral_small", "nova", "command_r"]:
        entries = []
        for r in rows:
            entries.append({
                "sample_id": r["sample_id"],
                "sut": r["sut"],
                "task": r["task"],
                "grade": r.get(name),
                "n_retries": r.get(f"{name}_n_retries", 0),
            })
        unparseable = sum(1 for e in entries if e["grade"] is None)
        per_grader[name] = {
            "slug": final_slugs[name],
            "n_total": len(entries),
            "n_unparseable": unparseable,
            "pct_unparseable": round(100 * unparseable / max(len(entries), 1), 2),
            "entries": entries,
        }
    out = {
        "_meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "banner": "EXPLORATORY / NON-QUOTABLE",
            "source_logs": "logs/20260715-sut-sweep (s3-frozen-config replay)",
            "config_note": "s3-frozen-config replay (old 204+22 bank, single-grader-era prompts) — valid for grader-BIAS inference only, NOT leaderboard numbers",
            "grader_slugs": final_slugs,
            "swaps": swaps,
            "credits_before": credits_before,
            "credits_after": credits_after,
        },
        "per_grader": per_grader,
    }
    with open(RAW_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"Wrote raw output: {RAW_OUT}")


def save_matrix(rows: list[dict], final_slugs: dict,
                credits_before: float, credits_after: float | None) -> None:
    matrix = []
    for r in rows:
        matrix.append({
            "sample_id": r["sample_id"],
            "sut":       r["sut"],
            "task":      r["task"],
            "design":    r.get("design"),
            "kind":      r.get("kind"),
            "tier":      r.get("tier"),
            "contested": r.get("contested"),
            "episode":   r.get("episode"),
            "track":     r.get("track"),
            "gemini":       r.get("gemini"),
            "deepseek":     r.get("deepseek"),
            "mistral_small": r.get("mistral_small"),
            "nova":          r.get("nova"),
            "command_r":     r.get("command_r"),
        })
    out = {
        "_meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "date": DATE,
            "banner": "EXPLORATORY / NON-QUOTABLE",
            "config_note": "s3-frozen-config replay (old 204+22 bank, single-grader-era prompts) — valid for grader-BIAS inference only, NOT leaderboard numbers",
            "grader_slugs": final_slugs,
            "incumbent_grader": "openrouter/google/gemini-2.5-flash (persisted, not re-run)",
            "n_rows": len(matrix),
            "credits_before": credits_before,
            "credits_after": credits_after,
        },
        "matrix": matrix,
    }
    with open(MATRIX_OUT, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"Wrote matrix: {MATRIX_OUT}")


def compute_and_save_stats(rows: list[dict]) -> None:
    """Compute descriptive stats only — no interpretation."""
    import statistics
    import random

    suts = [
        "openrouter/deepseek/deepseek-chat",
        "openrouter/mistralai/mistral-large-2512",
        "openrouter/qwen/qwen3.7-plus",
    ]
    sut_labels = {
        "openrouter/deepseek/deepseek-chat":   "deepseek_sut",
        "openrouter/mistralai/mistral-large-2512": "mistral_large_sut",
        "openrouter/qwen/qwen3.7-plus":         "qwen_sut",
    }
    graders_all = ["gemini", "deepseek", "mistral_small", "nova", "command_r"]

    # (a) Per-grader mean per SUT (5×3 matrix)
    mean_matrix = {}
    for g in graders_all:
        mean_matrix[g] = {}
        for sut in suts:
            vals = [r[g] for r in rows if r["sut"] == sut and r.get(g) is not None]
            mean_matrix[g][sut_labels[sut]] = round(statistics.mean(vals), 4) if vals else None

    # (b) Panel medians per row
    for r in rows:
        vals_default  = [r[g] for g in ["gemini", "deepseek", "mistral_small"] if r.get(g) is not None]
        vals_kinfree  = [r[g] for g in ["gemini", "nova", "command_r"]          if r.get(g) is not None]
        r["_panel_default"]  = statistics.median(vals_default)  if vals_default  else None
        r["_panel_kinfree"]  = statistics.median(vals_kinfree)  if vals_kinfree  else None

    # Per-SUT mean of both panels
    panel_means = {}
    for sut in suts:
        lbl = sut_labels[sut]
        d_vals = [r["_panel_default"] for r in rows if r["sut"] == sut and r["_panel_default"] is not None]
        k_vals = [r["_panel_kinfree"] for r in rows if r["sut"] == sut and r["_panel_kinfree"] is not None]
        panel_means[lbl] = {
            "mean_default_panel": round(statistics.mean(d_vals), 4) if d_vals else None,
            "mean_kinfree_panel": round(statistics.mean(k_vals), 4) if k_vals else None,
        }

    # (c) Per-SUT delta = mean(default) − mean(kinfree)
    deltas = {}
    for sut in suts:
        lbl = sut_labels[sut]
        d = panel_means[lbl]["mean_default_panel"]
        k = panel_means[lbl]["mean_kinfree_panel"]
        deltas[lbl] = round(d - k, 4) if (d is not None and k is not None) else None

    # (d) Difference-in-differences with paired bootstrap CI (10k resamples)
    random.seed(42)
    N_BOOT = 10000

    def did_boot(sut_kin: str, sut_control: str) -> tuple[float, float, float]:
        """Paired bootstrap over items for delta_kinSUT − delta_controlSUT."""
        kin_rows     = [r for r in rows if r["sut"] == sut_kin]
        control_rows = [r for r in rows if r["sut"] == sut_control]

        def delta(sample):
            dv = [r["_panel_default"] for r in sample if r["_panel_default"] is not None]
            kv = [r["_panel_kinfree"]  for r in sample if r["_panel_kinfree"]  is not None]
            if not dv or not kv:
                return None
            return statistics.mean(dv) - statistics.mean(kv)

        obs_kin     = delta(kin_rows)
        obs_control = delta(control_rows)
        obs_did     = obs_kin - obs_control if (obs_kin is not None and obs_control is not None) else None

        boot_dids = []
        for _ in range(N_BOOT):
            samp_kin     = [random.choice(kin_rows)     for _ in range(len(kin_rows))]
            samp_control = [random.choice(control_rows) for _ in range(len(control_rows))]
            d_k = delta(samp_kin)
            d_c = delta(samp_control)
            if d_k is not None and d_c is not None:
                boot_dids.append(d_k - d_c)

        boot_dids.sort()
        n = len(boot_dids)
        ci_lo = boot_dids[int(0.025 * n)] if n else None
        ci_hi = boot_dids[int(0.975 * n)] if n else None
        return obs_did, ci_lo, ci_hi

    did_deepseek  = did_boot("openrouter/deepseek/deepseek-chat",          "openrouter/qwen/qwen3.7-plus")
    did_mistral   = did_boot("openrouter/mistralai/mistral-large-2512",    "openrouter/qwen/qwen3.7-plus")

    did_stats = {
        "delta_deepseekSUT_minus_qwenSUT": {
            "obs": round(did_deepseek[0], 4) if did_deepseek[0] is not None else None,
            "ci95_lo": round(did_deepseek[1], 4) if did_deepseek[1] is not None else None,
            "ci95_hi": round(did_deepseek[2], 4) if did_deepseek[2] is not None else None,
            "n_boot": N_BOOT,
            "interpretation_note": "EXPLORATORY ONLY — positive = kin graders inflate deepseek SUT relative to qwen control",
        },
        "delta_mistralLargeSUT_minus_qwenSUT": {
            "obs": round(did_mistral[0], 4) if did_mistral[0] is not None else None,
            "ci95_lo": round(did_mistral[1], 4) if did_mistral[1] is not None else None,
            "ci95_hi": round(did_mistral[2], 4) if did_mistral[2] is not None else None,
            "n_boot": N_BOOT,
            "interpretation_note": "EXPLORATORY ONLY — positive = kin graders inflate mistral-large SUT relative to qwen control",
        },
    }

    # (e) Per-grader lone-outlier rates
    # Outlier = |grade − median(other 4 graders)| > 20
    outlier_rates = {}
    for g in graders_all:
        others = [x for x in graders_all if x != g]
        outlier_count = 0
        valid_count = 0
        for r in rows:
            g_val = r.get(g)
            if g_val is None:
                continue
            other_vals = [r[o] for o in others if r.get(o) is not None]
            if not other_vals:
                continue
            valid_count += 1
            med_others = statistics.median(other_vals)
            if abs(g_val - med_others) > 20:
                outlier_count += 1
        outlier_rates[g] = {
            "lone_outlier_count": outlier_count,
            "valid_rows": valid_count,
            "lone_outlier_rate_pct": round(100 * outlier_count / max(valid_count, 1), 2),
        }

    stats = {
        "_meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "banner": "EXPLORATORY / NON-QUOTABLE — descriptive stats only, no interpretation",
            "n_rows_total": len(rows),
            "n_boot_ci": N_BOOT,
            "panel_definition": {
                "default_panel": ["gemini", "deepseek", "mistral_small"],
                "kinfree_panel": ["gemini", "nova", "command_r"],
            },
        },
        "a_per_grader_mean_by_sut": mean_matrix,
        "b_panel_means_by_sut": panel_means,
        "c_per_sut_delta_default_minus_kinfree": deltas,
        "d_difference_in_differences": did_stats,
        "e_per_grader_lone_outlier_rates": outlier_rates,
    }
    with open(STATS_OUT, "w") as fh:
        json.dump(stats, fh, indent=2)
    print(f"Wrote stats: {STATS_OUT}")
    # Print summary to stdout for final report
    print("\n=== KIN-DELTA STATS SUMMARY ===")
    print("5x3 Mean Grade Matrix (rows=graders, cols=SUTs):")
    for g in graders_all:
        row_str = "  " + g.ljust(15)
        for lbl in ["deepseek_sut", "mistral_large_sut", "qwen_sut"]:
            v = mean_matrix[g].get(lbl)
            row_str += f"  {lbl[:15]}: {v:.2f}" if v is not None else f"  {lbl[:15]}: None"
        print(row_str)
    print("\nPanel means per SUT:")
    for lbl, pm in panel_means.items():
        print(f"  {lbl}: default={pm['mean_default_panel']}, kinfree={pm['mean_kinfree_panel']}")
    print("\nPer-SUT delta (default - kinfree):")
    for lbl, d in deltas.items():
        print(f"  {lbl}: {d}")
    print("\nDifference-in-Differences (kin SUT - qwen SUT):")
    for k, v in did_stats.items():
        print(f"  {k}: obs={v['obs']} 95%CI=[{v['ci95_lo']}, {v['ci95_hi']}]")
    print("\nPer-grader lone-outlier rates:")
    for g, v in outlier_rates.items():
        print(f"  {g}: {v['lone_outlier_rate_pct']:.1f}% ({v['lone_outlier_count']}/{v['valid_rows']})")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke-only", action="store_true", help="Run smoke test only")
    parser.add_argument("--full", action="store_true", help="Run full pass (includes smoke)")
    args = parser.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        raise SystemExit("OPENROUTER_API_KEY not set — source the env first.")

    rows = load_samples()
    print(f"Loaded {len(rows)} (sample, SUT) rows from {LOG_DIR.name}")
    sut_counts = {}
    for r in rows:
        sut_counts[r["sut"]] = sut_counts.get(r["sut"], 0) + 1
    for s, c in sut_counts.items():
        print(f"  {s}: {c} rows")

    # Determine grader slugs (may be swapped after smoke)
    final_slugs = dict(GRADERS_PRIMARY)

    # SMOKE TEST (nova + command_r only)
    smoke_indices = pick_smoke_rows(rows, n=10)
    print(f"\nSmoke row indices: {smoke_indices}")
    print(f"Smoke tasks: {[rows[i]['task'] for i in smoke_indices]}")
    print(f"Smoke SUTs: {[rows[i]['sut'].split('/')[-1] for i in smoke_indices]}")

    swaps, smoke_results, smoke_rows_graded = await run_smoke(rows, smoke_indices)

    # Apply swaps
    for name, swap_info in swaps.items():
        if swap_info is not None:
            final_slugs[name] = swap_info["fallback"]
            print(f"SWAP: {name} -> {final_slugs[name]}")

    # Save smoke log
    smoke_log = {
        "smoke_indices": smoke_indices,
        "smoke_tasks": [rows[i]["task"] for i in smoke_indices],
        "smoke_suts": [rows[i]["sut"] for i in smoke_indices],
        "results": smoke_results,
        "swaps": swaps,
        "final_slugs": final_slugs,
    }
    with open(SMOKE_LOG, "w") as fh:
        json.dump(smoke_log, fh, indent=2)
    print(f"Wrote smoke log: {SMOKE_LOG}")

    if args.smoke_only:
        print("--smoke-only flag set; stopping after smoke.")
        return

    # FULL RUN
    print(f"\nStarting full run: {len(rows)} rows × 4 graders")
    await run_full(rows, smoke_indices, smoke_rows_graded, swaps, final_slugs)

    # SAVE OUTPUTS
    credits_after = None  # will be fetched outside
    save_raw(rows, swaps, final_slugs, credits_before=None, credits_after=credits_after)
    save_matrix(rows, final_slugs, credits_before=None, credits_after=credits_after)
    compute_and_save_stats(rows)

    print("\nAll done.")


if __name__ == "__main__":
    asyncio.run(main())
