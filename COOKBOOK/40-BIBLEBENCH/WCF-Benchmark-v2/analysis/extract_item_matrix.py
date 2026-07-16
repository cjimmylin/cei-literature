"""
WCF-Benchmark-v2  —  per-sample item-matrix extractor.

Reads:
  logs/20260716-pilot/main/*.eval        (5 SUTs × 199 main items)
  logs/20260716-pilot/episodes/*.eval    (5 SUTs × 22  episodes)
  logs/20260715-sut-sweep/*.eval         (4 SUTs × 204 main + 22 episodes,
                                          single-grader, old 204-item bank)

Writes:
  analysis/20260716-session5-item-matrix.json
  analysis/20260716-session5-item-matrix.csv

Panel-grader order (session-4 pilot):
  index 0 → openrouter/google/gemini-2.5-flash
  index 1 → openrouter/deepseek/deepseek-chat
  index 2 → openrouter/mistralai/mistral-small-2603

This order is PRESERVED in panel["values"] because panel_median_reduce() in
src/wcf_grading.py builds the values list as:
    [_score_to_grade(s) for s in scores]
where `scores` arrives in the same iteration order as the `scorers` list in
wcf_tasks.py:wcf_scorer(), which splits DEFAULT_GRADER in left-to-right order:
    "openrouter/google/gemini-2.5-flash"        → index 0
    "openrouter/deepseek/deepseek-chat"          → index 1
    "openrouter/mistralai/mistral-small-2603"    → index 2

Run from the WCF-Benchmark-v2 project root:
    export OPENROUTER_API_KEY=dummy
    .venv-v2/bin/python analysis/extract_item_matrix.py
"""

import csv
import json
import math
import os

from inspect_ai.log import read_eval_log

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE = "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2"
PILOT_MAIN_DIR = os.path.join(BASE, "logs/20260716-pilot/main")
PILOT_EP_DIR   = os.path.join(BASE, "logs/20260716-pilot/episodes")
S3_SWEEP_DIR   = os.path.join(BASE, "logs/20260715-sut-sweep")

OUT_JSON = os.path.join(BASE, "analysis/20260716-session5-item-matrix.json")
OUT_CSV  = os.path.join(BASE, "analysis/20260716-session5-item-matrix.csv")

# ── Short-names (pilot) ────────────────────────────────────────────────────────
SHORTNAME = {
    "openrouter/qwen/qwen3.7-plus":            "qwen3.7-plus",
    "openrouter/anthropic/claude-haiku-4.5":   "haiku-4.5",
    "openrouter/openai/gpt-4o-mini":           "gpt-4o-mini",
    "openrouter/meta-llama/llama-4-maverick":  "llama-4-maverick",
    "openrouter/moonshotai/kimi-k2-0905":      "kimi-k2",
}

# ── Metadata keys expected in every sample ─────────────────────────────────────
# Discovered from first sample: design, track, tier, commandments, contested,
# episode, kind, pressure_turn.  We include ALL keys found dynamically.

PANEL_GRADER_ORDER = [
    "openrouter/google/gemini-2.5-flash",
    "openrouter/deepseek/deepseek-chat",
    "openrouter/mistralai/mistral-small-2603",
]


def _all_eval_files(directory: str):
    """Return sorted list of .eval file paths under directory."""
    return sorted(
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.endswith(".eval")
    )


def _get_score_key(sample):
    """Return the first scorer key from sample.scores."""
    return list(sample.scores.keys())[0]


def _score_value(sample) -> float:
    """Return sample score as float."""
    v = sample.scores[_get_score_key(sample)].value
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        v = v.strip()
        try:
            return float(v)
        except ValueError:
            return float("nan")
    return float("nan")


def _panel_info(sample):
    """Return (n_valid, values_list) from score metadata; (None, None) if absent."""
    meta = sample.scores[_get_score_key(sample)].metadata or {}
    panel = meta.get("panel")
    if panel is None:
        return None, None
    return panel.get("n_valid"), panel.get("values")


def extract_pilot_rows(directory: str, task: str) -> list[dict]:
    """Extract per-sample rows from all .eval files in a pilot directory."""
    rows = []
    for path in _all_eval_files(directory):
        log = read_eval_log(path)
        sut_full = log.eval.model
        sut = SHORTNAME.get(sut_full, sut_full)
        print(f"  [pilot/{task}] {sut} ({sut_full}): {len(log.samples)} samples")

        for s in log.samples:
            n_valid, values = _panel_info(s)
            row = {
                "sut":          sut,
                "sut_full":     sut_full,
                "task":         task,
                "sample_id":    s.id,
                # metadata fields — all keys present in sample
                "kind":         s.metadata.get("kind"),
                "design":       s.metadata.get("design"),
                "track":        s.metadata.get("track"),
                "tier":         s.metadata.get("tier"),
                "commandments": s.metadata.get("commandments"),
                "contested":    s.metadata.get("contested"),
                "episode":      s.metadata.get("episode"),
                "pressure_turn": s.metadata.get("pressure_turn"),
                # score
                "score":        _score_value(s),
                # panel
                "panel_n_valid": n_valid,
                "panel_values":  values,
            }
            rows.append(row)
    return rows


def extract_s3_rows(directory: str) -> list[dict]:
    """Extract per-sample rows from s3 sweep .eval files (single-grader, old bank)."""
    rows = []
    for path in _all_eval_files(directory):
        log = read_eval_log(path)
        sut_full = log.eval.model
        sut = SHORTNAME.get(sut_full, sut_full)
        task = log.eval.task
        print(f"  [s3-sweep/{task}] {sut} ({sut_full}): {len(log.samples)} samples")

        for s in log.samples:
            row = {
                "sut":          sut,
                "sut_full":     sut_full,
                "task":         task,
                "sample_id":    s.id,
                "kind":         s.metadata.get("kind"),
                "design":       s.metadata.get("design"),
                "track":        s.metadata.get("track"),
                "tier":         s.metadata.get("tier"),
                "commandments": s.metadata.get("commandments"),
                "contested":    s.metadata.get("contested"),
                "episode":      s.metadata.get("episode"),
                "pressure_turn": s.metadata.get("pressure_turn"),
                "score":        _score_value(s),
                "config_era":   "s3-single-grader-old-bank",
            }
            rows.append(row)
    return rows


# ── Main ───────────────────────────────────────────────────────────────────────
print("Extracting pilot main …")
pilot_main_rows = extract_pilot_rows(PILOT_MAIN_DIR, "wcf_main")

print("Extracting pilot episodes …")
pilot_ep_rows   = extract_pilot_rows(PILOT_EP_DIR, "wcf_episodes")

pilot_rows = pilot_main_rows + pilot_ep_rows
print(f"\nTotal pilot rows: {len(pilot_rows)}  (expected 1,105)")

print("\nExtracting s3 sweep …")
s3_rows = extract_s3_rows(S3_SWEEP_DIR)
print(f"Total s3 rows: {len(s3_rows)}  (expected 904)")

# ── Validation ─────────────────────────────────────────────────────────────────
print("\n=== VALIDATION ===")

# 1. Pilot SUT slugs
pilot_suts = sorted(set(r["sut"] for r in pilot_rows))
print(f"Pilot SUTs ({len(pilot_suts)}): {pilot_suts}")

s3_suts = sorted(set(r["sut"] for r in s3_rows))
print(f"S3 sweep SUTs ({len(s3_suts)}): {s3_suts}")

# 2. Row counts
print(f"Pilot rows: {len(pilot_rows)} (expected 1105)")
print(f"S3 rows:    {len(s3_rows)} (expected 904)")

# 3. Samples with panel_n_valid == 2
nv2 = [r for r in pilot_rows if r["panel_n_valid"] == 2]
print(f"\nSamples with panel_n_valid=2: {len(nv2)} (expected 5)")
for r in sorted(nv2, key=lambda x: (x["sut"], x["sample_id"])):
    print(f"  {r['sut']} / {r['sample_id']}")

# 4. Score range check
bad_scores = [r for r in pilot_rows if math.isnan(r["score"]) or not (0 <= r["score"] <= 100)]
print(f"\nPilot scores out of [0,100] or NaN: {len(bad_scores)} (expected 0)")

# ── Build JSON ─────────────────────────────────────────────────────────────────
output = {
    "note": (
        "WCF-Benchmark-v2 per-sample item matrix. "
        "Pilot = session-4 (2026-07-16), 221-item bank, 5 SUTs, 3-grader panel-median. "
        "s3_sweep = session-3 (2026-07-15), 204-item bank (old), 4 SUTs, single-grader. "
        "pilot rows: 1105 (5 SUTs × 221). s3 rows: 904 (4 SUTs × 226)."
    ),
    "panel_order_note": (
        "panel_values list order is DETERMINISTIC and grader-ordered. "
        "In src/wcf_grading.py:panel_median_reduce(), values = [_score_to_grade(s) for s in scores]. "
        "The scores list arrives from multi_scorer() in the same left-to-right order as the "
        "DEFAULT_GRADER string in src/wcf_tasks.py. "
        "Therefore: panel_values[0] = openrouter/google/gemini-2.5-flash, "
        "panel_values[1] = openrouter/deepseek/deepseek-chat, "
        "panel_values[2] = openrouter/mistralai/mistral-small-2603."
    ),
    "pilot": pilot_rows,
    "s3_sweep": s3_rows,
}

# JSON serialisation — ensure nan becomes null
def json_safe(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return None
    return obj

# Custom encoder
class NaNEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float) and math.isnan(obj):
            return None
        return super().default(obj)

# For pilot rows, NaN in score → null
for r in output["pilot"]:
    if isinstance(r["score"], float) and math.isnan(r["score"]):
        r["score"] = None

for r in output["s3_sweep"]:
    if isinstance(r["score"], float) and math.isnan(r["score"]):
        r["score"] = None

with open(OUT_JSON, "w") as f:
    json.dump(output, f, indent=2, default=str)

print(f"\nWritten JSON: {OUT_JSON}")
print(f"  File size: {os.path.getsize(OUT_JSON):,} bytes")

# ── Build CSV (pilot rows only) ────────────────────────────────────────────────
csv_cols = [
    "sut", "task", "sample_id", "kind", "design", "track", "tier",
    "commandments", "contested", "episode", "pressure_turn",
    "score", "panel_n_valid", "panel_g1", "panel_g2", "panel_g3",
]

with open(OUT_CSV, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=csv_cols, extrasaction="ignore")
    writer.writeheader()
    for r in pilot_rows:
        vals = r.get("panel_values") or []
        row_out = {
            "sut":           r["sut"],
            "task":          r["task"],
            "sample_id":     r["sample_id"],
            "kind":          r["kind"],
            "design":        r["design"],
            "track":         r["track"],
            "tier":          r["tier"],
            "commandments":  json.dumps(r["commandments"]) if r["commandments"] is not None else "",
            "contested":     r["contested"],
            "episode":       r["episode"],
            "pressure_turn": r["pressure_turn"] if r["pressure_turn"] is not None else "",
            "score":         r["score"] if r["score"] is not None else "",
            "panel_n_valid": r["panel_n_valid"] if r["panel_n_valid"] is not None else "",
            "panel_g1":      vals[0] if len(vals) > 0 and vals[0] is not None else "",
            "panel_g2":      vals[1] if len(vals) > 1 and vals[1] is not None else "",
            "panel_g3":      vals[2] if len(vals) > 2 and vals[2] is not None else "",
        }
        # For degraded panel (n_valid=2), the None slot stays empty
        writer.writerow(row_out)

print(f"Written CSV:  {OUT_CSV}")
print(f"  File size: {os.path.getsize(OUT_CSV):,} bytes")
print(f"  CSV rows (pilot): {len(pilot_rows)}")

print("\nDone.")
