"""
Session-4 pilot statistics pack for WCF-Benchmark-v2.
Outputs: analysis/20260716-session4-pilot-stats.json
"""

import os, re, json, math
from collections import defaultdict, Counter
from pathlib import Path
from inspect_ai.log import read_eval_log

# ── paths ──────────────────────────────────────────────────────────────────────
# Anchored to this file (analysis/ → project root) so the folder is relocatable;
# resolves to the same absolute path this literal used to hardcode.
BASE = str(Path(__file__).resolve().parent.parent)
MAIN_DIR = os.path.join(BASE, "logs/20260716-pilot/main")
EP_DIR   = os.path.join(BASE, "logs/20260716-pilot/episodes")
OUT_PATH = os.path.join(BASE, "analysis/20260716-session4-pilot-stats.json")

# ── model short-names ──────────────────────────────────────────────────────────
SHORTNAME = {
    "openrouter/qwen/qwen3.7-plus":            "qwen3.7-plus",
    "openrouter/anthropic/claude-haiku-4.5":   "haiku-4.5",
    "openrouter/openai/gpt-4o-mini":           "gpt-4o-mini",
    "openrouter/meta-llama/llama-4-maverick":  "llama-4-maverick",
    "openrouter/moonshotai/kimi-k2-0905":      "kimi-k2",
}

THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)

def strip_think(text: str) -> str:
    return THINK_RE.sub("", text).strip()

def load_logs(directory):
    """Return list of (model_short, samples) tuples."""
    results = []
    files = sorted(f for f in os.listdir(directory) if f.endswith(".eval"))
    for fname in files:
        path = os.path.join(directory, fname)
        log = read_eval_log(path)
        short = SHORTNAME.get(log.eval.model, log.eval.model)
        results.append((short, log.samples))
        print(f"  Loaded {short}: {len(log.samples)} samples from {fname[:50]}")
    return results

print("Loading main logs …")
main_data = load_logs(MAIN_DIR)

print("Loading episode logs …")
ep_data   = load_logs(EP_DIR)

# ── Flatten into dicts keyed by model ─────────────────────────────────────────
main_by_model = {short: samples for short, samples in main_data}
ep_by_model   = {short: samples for short, samples in ep_data}

SUTS = list(main_by_model.keys())
print("SUTs:", SUTS)

# ════════════════════════════════════════════════════════════════════════════════
# 1. PANEL INTEGRITY (all 1,105 samples = 5 SUTs × 199 main + 5 SUTs × 22 ep)
# ════════════════════════════════════════════════════════════════════════════════
n_valid_dist = Counter()   # n_valid value → count
out_of_range = []          # list of dicts for any value outside 0-100

for short, samples in main_data + ep_data:
    for s in samples:
        score_key = list(s.scores.keys())[0]
        meta = s.scores[score_key].metadata or {}
        panel = meta.get("panel", {})
        nv = panel.get("n_valid", None)
        vals = panel.get("values", [])
        n_valid_dist[nv] += 1
        null_vals = [v for v in vals if v is None]
        for v in vals:
            if v is None:
                continue  # null = grader failure slot, not out-of-range
            if not (0 <= v <= 100):
                out_of_range.append({"model": short, "id": s.id, "value": v})

total_samples = sum(len(s) for _, s in main_data + ep_data)
print(f"\nTotal samples: {total_samples}")
print("n_valid distribution:", dict(n_valid_dist))
print("Out-of-range panel values:", len(out_of_range))

# ════════════════════════════════════════════════════════════════════════════════
# 2. LEADERBOARD
# ════════════════════════════════════════════════════════════════════════════════
def score_of(sample):
    key = list(sample.scores.keys())[0]
    return float(sample.scores[key].value)

leaderboard = {}  # model -> {combined, main, ep}

for short in SUTS:
    main_scores = [score_of(s) for s in main_by_model[short]]
    ep_scores   = [score_of(s) for s in ep_by_model[short]]
    combined    = main_scores + ep_scores

    def stats(vals):
        n = len(vals)
        mean = sum(vals) / n
        var  = sum((v - mean)**2 for v in vals) / (n - 1)
        se   = math.sqrt(var / n)
        ci_lo = mean - 1.96 * se
        ci_hi = mean + 1.96 * se
        return {"n": n, "mean": round(mean, 2), "se": round(se, 2),
                "ci95_lo": round(ci_lo, 2), "ci95_hi": round(ci_hi, 2)}

    leaderboard[short] = {
        "combined": stats(combined),
        "main":     stats(main_scores),
        "episodes": stats(ep_scores),
    }

# Sort by combined mean descending
ranking = sorted(SUTS, key=lambda m: leaderboard[m]["combined"]["mean"], reverse=True)
print("\nLeaderboard (combined):")
for r, m in enumerate(ranking, 1):
    s = leaderboard[m]["combined"]
    print(f"  {r}. {m}: {s['mean']} ± {s['se']}  95%CI [{s['ci95_lo']}, {s['ci95_hi']}]")

# ════════════════════════════════════════════════════════════════════════════════
# 3. PAIRED ADJACENT-GAP TESTS
# ════════════════════════════════════════════════════════════════════════════════
# Build item-matched combined score vectors (same ordering required)
# Items: main 199 (by s.id) + episodes 22 (by s.id)
# Collect per-SUT score dicts
def get_score_dict(samples):
    return {s.id: score_of(s) for s in samples}

main_ids = sorted(main_by_model[ranking[0]].keys() if False else
                  [s.id for s in main_by_model[ranking[0]]])
ep_ids   = sorted([s.id for s in ep_by_model[ranking[0]]])
all_ids  = main_ids + ep_ids
print(f"\nCombined item count: {len(all_ids)} (main {len(main_ids)} + ep {len(ep_ids)})")

# Build combined score vector per SUT
combined_vectors = {}
for short in SUTS:
    m_dict = get_score_dict(main_by_model[short])
    e_dict = get_score_dict(ep_by_model[short])
    combined_vectors[short] = [m_dict[i] for i in main_ids] + [e_dict[i] for i in ep_ids]

gap_tests = []
for k in range(len(ranking) - 1):
    sut_a = ranking[k]     # higher
    sut_b = ranking[k + 1] # lower
    va = combined_vectors[sut_a]
    vb = combined_vectors[sut_b]
    n = len(va)
    diffs = [a - b for a, b in zip(va, vb)]
    delta = sum(diffs) / n
    sd_diff = math.sqrt(sum((d - delta)**2 for d in diffs) / (n - 1))
    se_diff = sd_diff / math.sqrt(n)
    t = delta / se_diff if se_diff > 0 else float("inf")
    sig = "SIG" if abs(t) >= 2 else "NS"
    gap_tests.append({
        "pair": f"{sut_a} vs {sut_b}",
        "sut_hi": sut_a,
        "sut_lo": sut_b,
        "delta": round(delta, 2),
        "se_diff": round(se_diff, 2),
        "t": round(t, 2),
        "sig": sig,
    })
    print(f"  {sut_a} vs {sut_b}: Δ={delta:.2f} SE={se_diff:.2f} t={t:.2f} {sig}")

# Derive tier structure: adjacent NS → same tier
tiers = []
current_tier = [ranking[0]]
for k, gap in enumerate(gap_tests):
    if gap["sig"] == "NS":
        current_tier.append(ranking[k + 1])
    else:
        tiers.append(current_tier)
        current_tier = [ranking[k + 1]]
tiers.append(current_tier)
tier_map = {}
for t_idx, tier_members in enumerate(tiers, 1):
    for m in tier_members:
        tier_map[m] = t_idx
print("Tiers:", tiers)

# ════════════════════════════════════════════════════════════════════════════════
# 4. CEILING
# ════════════════════════════════════════════════════════════════════════════════
ceiling = {}
for short in SUTS:
    main_scores = [score_of(s) for s in main_by_model[short]]
    ep_scores   = [score_of(s) for s in ep_by_model[short]]
    combined    = main_scores + ep_scores
    n_comb = len(combined)
    n_main = len(main_scores)

    ceiling[short] = {
        "combined_pct_100":   round(100 * sum(1 for v in combined   if v == 100)  / n_comb, 1),
        "combined_pct_ge95":  round(100 * sum(1 for v in combined   if v >= 95)   / n_comb, 1),
        "main_pct_100":       round(100 * sum(1 for v in main_scores if v == 100) / n_main, 1),
        "main_pct_ge95":      round(100 * sum(1 for v in main_scores if v >= 95)  / n_main, 1),
    }
print("\nCeiling:")
for m in ranking:
    print(f"  {m}: combined ==100 {ceiling[m]['combined_pct_100']}%, ≥95 {ceiling[m]['combined_pct_ge95']}%"
          f"  | main ==100 {ceiling[m]['main_pct_100']}%, ≥95 {ceiling[m]['main_pct_ge95']}%")

# ════════════════════════════════════════════════════════════════════════════════
# 5. GRADED-ANSWER LENGTH
# ════════════════════════════════════════════════════════════════════════════════
length_stats = {}
for short in SUTS:
    combined_samples = list(main_by_model[short]) + list(ep_by_model[short])
    lengths = [len(strip_think(s.output.completion)) for s in combined_samples]
    n = len(lengths)
    mean_len = sum(lengths) / n
    length_stats[short] = {
        "n": n,
        "mean_chars": round(mean_len, 1),
        "min": min(lengths),
        "max": max(lengths),
    }
print("\nLength stats:")
for m in ranking:
    print(f"  {m}: mean {length_stats[m]['mean_chars']} chars")

# ════════════════════════════════════════════════════════════════════════════════
# 6. PER-KIND MEANS (main task only)
# ════════════════════════════════════════════════════════════════════════════════
# First get kind ns from first SUT (same items)
kinds_ref = Counter(s.metadata.get("kind", "?") for s in main_by_model[ranking[0]])
print("\nKind distribution (main, per SUT):", dict(kinds_ref))

per_kind = {}
contested_raw = {}  # model -> {item_id: score}

for short in SUTS:
    per_kind[short] = {}
    contested_raw[short] = {}
    by_kind = defaultdict(list)
    for s in main_by_model[short]:
        k = s.metadata.get("kind", "?")
        v = score_of(s)
        by_kind[k].append((s.id, v))
        if k == "contested":
            contested_raw[short][s.id] = v

    for k, items in by_kind.items():
        scores = [v for _, v in items]
        n = len(scores)
        mean = sum(scores) / n
        per_kind[short][k] = {"n": n, "mean": round(mean, 2)}

print("\nPer-kind means (combined SUTs):")
for k in ["open", "anchor", "ordinal", "contested"]:
    row = "  " + k + ": "
    for m in ranking:
        row += f"{m}={per_kind[m][k]['mean']} (n={per_kind[m][k]['n']})  "
    print(row)

print("\nContested raw scores:")
contested_ids = sorted(contested_raw[ranking[0]].keys())
for cid in contested_ids:
    row = f"  {cid}: "
    for m in ranking:
        row += f"{m}={contested_raw[m].get(cid,'?')}  "
    print(row)

# ════════════════════════════════════════════════════════════════════════════════
# 7. EPISODE PROFILE
# ════════════════════════════════════════════════════════════════════════════════
# EP-02/ST-07 guardrails → count structure {n==0, n<50, 50-95, n≥95}
# and per-item 22×5 score table

ep_ids_ordered = sorted([s.id for s in ep_by_model[ranking[0]]])
episode_score_table = {}  # item_id -> {model: score}
for ep_id in ep_ids_ordered:
    episode_score_table[ep_id] = {}

ep_count_structure = {}
for short in SUTS:
    scores = [score_of(s) for s in ep_by_model[short]]
    ep_count_structure[short] = {
        "n_eq0":   sum(1 for v in scores if v == 0),
        "n_lt50":  sum(1 for v in scores if 0 < v < 50),
        "n_50_95": sum(1 for v in scores if 50 <= v < 95),
        "n_ge95":  sum(1 for v in scores if v >= 95),
    }
    # fill score table
    ep_dict = get_score_dict(ep_by_model[short])
    for ep_id in ep_ids_ordered:
        episode_score_table[ep_id][short] = ep_dict.get(ep_id, None)

print("\nEpisode count structure (EP guardrails):")
for m in ranking:
    print(f"  {m}: {ep_count_structure[m]}")

# ════════════════════════════════════════════════════════════════════════════════
# 8. CONTINUITY DELTAS
# ════════════════════════════════════════════════════════════════════════════════
OLD_FROZEN = {
    "qwen3.7-plus": 93.4,
    "haiku-4.5":    89.9,   # haiku in old session was haiku-3 but labelled haiku
    "gpt-4o-mini":  69.5,
    "llama-4-maverick": 72.6,
}
NOTE = "NOT comparable (panel-native, patched 221-item bank, new parser)"

continuity = {}
for short in SUTS:
    old = OLD_FROZEN.get(short)
    if old is not None:
        new = leaderboard[short]["combined"]["mean"]
        continuity[short] = {
            "old_frozen_single_grader_226items": old,
            "new_panel_221items": new,
            "delta": round(new - old, 2),
            "note": NOTE,
        }
print("\nContinuity deltas:")
for m in ranking:
    if m in continuity:
        print(f"  {m}: old={continuity[m]['old_frozen_single_grader_226items']} new={continuity[m]['new_panel_221items']} Δ={continuity[m]['delta']}")

# ════════════════════════════════════════════════════════════════════════════════
# ASSEMBLE JSON OUTPUT
# ════════════════════════════════════════════════════════════════════════════════
output = {
    "metadata": {
        "date": "2026-07-16",
        "session": 4,
        "description": "WCF-Benchmark-v2 session-4 pilot statistics pack",
        "total_samples": total_samples,
        "n_main_items": len(main_ids),
        "n_ep_items": len(ep_ids),
        "n_suts": len(SUTS),
        "suts": ranking,
    },
    "panel_integrity": {
        "n_valid_distribution": {str(k): v for k, v in sorted(n_valid_dist.items())},
        "total_samples_checked": total_samples,
        "out_of_range_panel_values": out_of_range,
        "n_out_of_range": len(out_of_range),
    },
    "leaderboard": {
        m: {
            "rank": ranking.index(m) + 1,
            "tier": tier_map[m],
            **leaderboard[m],
        }
        for m in ranking
    },
    "ranking_order": ranking,
    "adjacent_gap_tests": gap_tests,
    "tier_structure": tiers,
    "ceiling": {m: ceiling[m] for m in ranking},
    "answer_length": {m: length_stats[m] for m in ranking},
    "per_kind_main": {
        "kind_ns": dict(kinds_ref),
        "by_sut": {m: per_kind[m] for m in ranking},
    },
    "contested_raw_scores": {
        "item_ids": contested_ids,
        "by_sut": {m: contested_raw[m] for m in ranking},
    },
    "episode_profile": {
        "count_structure": {m: ep_count_structure[m] for m in ranking},
        "score_table_22x5": episode_score_table,
        "ep_ids": ep_ids_ordered,
    },
    "continuity_deltas": continuity,
}

with open(OUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"\n✓ Written: {OUT_PATH}")
print(f"  File size: {os.path.getsize(OUT_PATH):,} bytes")
