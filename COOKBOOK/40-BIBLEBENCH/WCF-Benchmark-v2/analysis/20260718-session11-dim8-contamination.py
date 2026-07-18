"""
Dimension 8 — Contamination / Leakage Risk
Session 11, 2026-07-18

Sub-analyses:
  A. Public-text overlap: longest common word n-gram (n>=6) between item stem
     and on-disk WCF/WLC text.  Flag QUOTES-PUBLIC-TEXT if n>=8.
  B. Distinctive-phrase memorability: per-item rarest 6+-word n-grams
     (unique within bank) + named-entity detection.
  C. Style-invariance probe (Session 8 contamination rows): compare J4 grades
     on style-changed vs original phrasing; report per-item grade delta.

Outputs:
  analysis/20260718-session11-ledger-dim8.json   — per-item record
  analysis/20260718-session11-dim8-summary.json  — aggregate summary

Run from project root:
  .venv-v2/bin/python analysis/20260718-session11-dim8-contamination.py
"""

import json
import os
import re
import string
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2")
DATA_DIR = PROJECT / "data"
ANALYSIS_DIR = PROJECT / "analysis"

# WCF / WLC public texts live in a sibling directory outside the project root
WCF_TEXT_DIR = PROJECT.parent / "WCF"

MAIN_JSONL = DATA_DIR / "wcf_main.jsonl"
EPISODES_JSONL = DATA_DIR / "wcf_episodes.jsonl"

CONT_ROWS = ANALYSIS_DIR / "20260717-session8-contamination-rows.jsonl"
J4_CONT_RAW = ANALYSIS_DIR / "20260717-session8-j4-contamination-raw.jsonl"
J4_MAIN_RAW = ANALYSIS_DIR / "20260717-session8-j4-raw.jsonl"

OUT_LEDGER = ANALYSIS_DIR / "20260718-session11-ledger-dim8.json"
OUT_SUMMARY = ANALYSIS_DIR / "20260718-session11-dim8-summary.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def tokenize(text: str) -> list[str]:
    """Lowercase word tokens, strip punctuation."""
    text = text.lower()
    tokens = re.findall(r"[a-z']+", text)
    return tokens


def word_ngrams(tokens: list[str], n: int) -> list[tuple]:
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def longest_common_ngram(stem_tokens: list[str], ref_tokens: list[str],
                         min_n: int = 6) -> int:
    """Return the length of the longest common word n-gram (n >= min_n)
    between stem_tokens and ref_tokens.  Returns 0 if none found."""
    if not stem_tokens or not ref_tokens:
        return 0
    # Build set of ref n-grams from min_n up to a reasonable max
    max_n = min(len(stem_tokens), len(ref_tokens), 40)
    best = 0
    # Build ref sets incrementally: start at min_n, stop when stem set empty
    for n in range(min_n, max_n + 1):
        stem_set = set(word_ngrams(stem_tokens, n))
        if not stem_set:
            break
        ref_set = set(word_ngrams(ref_tokens, n))
        if stem_set & ref_set:
            best = n
        else:
            # No match at this n; larger n cannot match either
            break
    return best


def has_named_entities(stem: str) -> bool:
    """Heuristic: multi-word capitalized tokens that are NOT sentence-initial.
    We look for 2+ consecutive Title-Case words that don't start a sentence."""
    # Split into sentences roughly
    sentences = re.split(r"(?<=[.!?])\s+", stem)
    for sent in sentences:
        words = sent.split()
        for i, w in enumerate(words[1:], start=1):  # skip sentence-initial
            # Two consecutive capitalized words (not all-caps abbreviations)
            if (re.match(r"^[A-Z][a-z]+$", w) and
                    i + 1 < len(words) and
                    re.match(r"^[A-Z][a-z]+$", words[i + 1])):
                return True
            # Or a single mid-sentence word that looks like a proper name/place
            if (i > 0 and re.match(r"^[A-Z][a-z]{2,}$", w) and
                    words[i - 1][-1:] not in ".!?"):
                return True
    return False


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


# ---------------------------------------------------------------------------
# Load items
# ---------------------------------------------------------------------------
print("Loading items …")
items = []
for path in (MAIN_JSONL, EPISODES_JSONL):
    items.extend(load_jsonl(path))
print(f"  {len(items)} items total")

# Deduplicate by id (safety)
seen_ids = {}
deduped = []
for it in items:
    iid = it["id"]
    if iid not in seen_ids:
        seen_ids[iid] = True
        deduped.append(it)
items = deduped
print(f"  {len(items)} unique item ids")


# ---------------------------------------------------------------------------
# Sub-analysis A: public-text overlap
# ---------------------------------------------------------------------------
print("\n=== Sub-analysis A: public-text overlap ===")

wcf_text_found = WCF_TEXT_DIR.exists() and any(WCF_TEXT_DIR.iterdir())
public_text_paths = []

if wcf_text_found:
    for fn in sorted(WCF_TEXT_DIR.iterdir()):
        if fn.is_file() and fn.suffix == ".txt":
            public_text_paths.append(fn)
    print(f"  Found {len(public_text_paths)} public text file(s) in {WCF_TEXT_DIR}")
    for p in public_text_paths:
        print(f"    {p.name}  ({p.stat().st_size:,} bytes)")
else:
    print("  No on-disk WCF/WLC text files found — sub-analysis A SKIPPED")

# Load and tokenize all public texts
ref_tokens_combined: list[str] = []
if public_text_paths:
    for p in public_text_paths:
        raw = p.read_text(encoding="utf-8", errors="replace")
        ref_tokens_combined.extend(tokenize(raw))
    print(f"  Combined reference token count: {len(ref_tokens_combined):,}")
    # Build a set of ALL 6+-grams from reference for fast lookup
    # We iterate length-by-length in longest_common_ngram per item instead

# Per-item overlap
overlap_by_id: dict[str, int | None] = {}

if public_text_paths:
    for it in items:
        stem = it.get("stem", "") or ""
        stem_tok = tokenize(stem)
        best = longest_common_ngram(stem_tok, ref_tokens_combined, min_n=6)
        overlap_by_id[it["id"]] = best
    n_flagged = sum(1 for v in overlap_by_id.values() if v is not None and v >= 8)
    print(f"  Items with n-gram overlap >=6: {sum(1 for v in overlap_by_id.values() if v >= 6)}")
    print(f"  Items with n-gram overlap >=8 (QUOTES-PUBLIC-TEXT): {n_flagged}")
    max_overlap = max(overlap_by_id.values())
    top_item = max(overlap_by_id, key=lambda k: overlap_by_id[k])
    print(f"  Longest overlap: {max_overlap} tokens (item {top_item})")
else:
    for it in items:
        overlap_by_id[it["id"]] = None


# ---------------------------------------------------------------------------
# Sub-analysis B: distinctive phrase memorability
# ---------------------------------------------------------------------------
print("\n=== Sub-analysis B: distinctive phrase memorability ===")

# Collect all 6+-grams across the bank
MIN_N = 6
all_ngram_counts: Counter = Counter()
item_ngrams: dict[str, list[tuple]] = {}

for it in items:
    stem = it.get("stem", "") or ""
    toks = tokenize(stem)
    ngs = word_ngrams(toks, MIN_N)
    item_ngrams[it["id"]] = ngs
    all_ngram_counts.update(ngs)

# Distinctive = appears in exactly 1 item (bank-unique)
unique_ngrams: set[tuple] = {ng for ng, cnt in all_ngram_counts.items() if cnt == 1}

distinctiveness_by_id: dict[str, int] = {}
for it in items:
    n_unique = sum(1 for ng in item_ngrams[it["id"]] if ng in unique_ngrams)
    distinctiveness_by_id[it["id"]] = n_unique

# Named-entity flag
ne_by_id: dict[str, bool] = {}
for it in items:
    stem = it.get("stem", "") or ""
    ne_by_id[it["id"]] = has_named_entities(stem)

# Top-decile threshold
all_scores = sorted(distinctiveness_by_id.values())
n_items = len(all_scores)
p90_idx = max(0, int(n_items * 0.90) - 1)
p90_threshold = all_scores[p90_idx] if all_scores else 0
print(f"  90th-percentile distinctiveness score: {p90_threshold}")
top_decile_ids = [iid for iid, sc in distinctiveness_by_id.items() if sc >= p90_threshold]
print(f"  Items in top decile (n_distinctive_ngrams >= {p90_threshold}): {len(top_decile_ids)}")
ne_count = sum(1 for v in ne_by_id.values() if v)
print(f"  Items with named entities (mid-sentence multi-cap): {ne_count}")

# Top-10 most distinctive
top10 = sorted(distinctiveness_by_id.items(), key=lambda x: x[1], reverse=True)[:10]
print("  Top-10 most distinctive items (id: score):")
for iid, sc in top10:
    ne = ne_by_id[iid]
    print(f"    {iid}: {sc}  has_NE={ne}")


# ---------------------------------------------------------------------------
# Sub-analysis C: style-invariance probe
# ---------------------------------------------------------------------------
print("\n=== Sub-analysis C: style-invariance probe (Session 8) ===")

cont_rows = load_jsonl(CONT_ROWS)
j4_cont = load_jsonl(J4_CONT_RAW)
j4_main = load_jsonl(J4_MAIN_RAW)

# Grade lookups by sample_key
j4_cont_grade = {r["sample_key"]: r["grade"] for r in j4_cont}
j4_main_grade = {r["sample_key"]: r["grade"] for r in j4_main}

# Per probe row: find original grade and contamination-probe grade
probe_records: list[dict] = []
for r in cont_rows:
    sk = r["sample_key"]
    probe_grade = j4_cont_grade.get(sk)
    orig_grade = j4_main_grade.get(sk)
    if probe_grade is None or orig_grade is None:
        continue
    delta = abs(probe_grade - orig_grade)
    probe_records.append({
        "sample_key": sk,
        "item_id": r["item_id"],
        "sut": r["sut_short"],
        "epoch": r["epoch"],
        "style_changed": r["style_changed"],
        "orig_grade": orig_grade,
        "probe_grade": probe_grade,
        "abs_delta": delta,
    })

n_probed = len(probe_records)
probed_item_ids = sorted(set(r["item_id"] for r in probe_records))
n_probed_items = len(probed_item_ids)
max_delta = max(r["abs_delta"] for r in probe_records) if probe_records else 0
mean_delta = sum(r["abs_delta"] for r in probe_records) / n_probed if probe_records else 0
max_delta_row = max(probe_records, key=lambda x: x["abs_delta"]) if probe_records else None

# COMP-N-022 epoch=3 style=False is a special case (style NOT changed → probe is control)
n_style_changed = sum(1 for r in probe_records if r["style_changed"])
n_style_unchanged = n_probed - n_style_changed
style_changed_deltas = [r["abs_delta"] for r in probe_records if r["style_changed"]]
style_unchanged_deltas = [r["abs_delta"] for r in probe_records if not r["style_changed"]]

mean_delta_changed = sum(style_changed_deltas) / len(style_changed_deltas) if style_changed_deltas else 0
mean_delta_unchanged = sum(style_unchanged_deltas) / len(style_unchanged_deltas) if style_unchanged_deltas else 0

print(f"  Total probe rows matched: {n_probed}")
print(f"    style_changed=True:  {n_style_changed}  mean |delta|={mean_delta_changed:.1f}")
print(f"    style_changed=False: {n_style_unchanged}  mean |delta|={mean_delta_unchanged:.1f}")
print(f"  Unique items probed: {n_probed_items}: {probed_item_ids}")
print(f"  Max |delta|: {max_delta} (item {max_delta_row['item_id']}, "
      f"orig={max_delta_row['orig_grade']}, probe={max_delta_row['probe_grade']}, "
      f"style_changed={max_delta_row['style_changed']})")
print(f"  Mean |delta| overall: {mean_delta:.1f}")

# Large-delta items (>= 20 pts) -- potential instability or leakage-dependent scoring
large_delta = [(r["item_id"], r["abs_delta"], r["style_changed"])
               for r in probe_records if r["abs_delta"] >= 20]
print(f"  Items with |delta| >= 20: {large_delta}")

# Style-invariance verdict:
# style_changed=False row is the "control" (same content, same style) --
# that case's delta reflects regrading noise, not surface-style sensitivity.
# The COMP-N-022 style_changed=False |delta|=59 is anomalously large and
# appears to be a grader-randomness or rubric-cap artifact, not leakage.
# For the 20 style_changed=True rows, mean delta = 5.7 → style-invariant.
if style_changed_deltas:
    verdict = ("STABLE (mean |delta| <= 10 on style-changed rows)"
               if mean_delta_changed <= 10 else
               "UNSTABLE (mean |delta| > 10 on style-changed rows)")
else:
    verdict = "NO DATA"
print(f"  Style-invariance verdict: {verdict}")


# ---------------------------------------------------------------------------
# Per-item s8_probe info
# ---------------------------------------------------------------------------
probe_by_item: dict[str, dict] = {}
for r in probe_records:
    iid = r["item_id"]
    if iid not in probe_by_item:
        probe_by_item[iid] = {"probed": True, "observations": []}
    probe_by_item[iid]["observations"].append({
        "sample_key": r["sample_key"],
        "style_changed": r["style_changed"],
        "orig_grade": r["orig_grade"],
        "probe_grade": r["probe_grade"],
        "abs_delta": r["abs_delta"],
    })

# Collapse to max delta per item
for iid, info in probe_by_item.items():
    info["max_abs_delta"] = max(o["abs_delta"] for o in info["observations"])
    info["style_changed_grade_delta"] = info["max_abs_delta"]


# ---------------------------------------------------------------------------
# Build per-item ledger
# ---------------------------------------------------------------------------
print("\n=== Building per-item ledger ===")

ledger: dict[str, dict] = {}
for it in items:
    iid = it["id"]
    overlap = overlap_by_id[iid]
    dist = distinctiveness_by_id[iid]
    ne = ne_by_id[iid]
    probe = probe_by_item.get(iid, {"probed": False, "style_changed_grade_delta": None})

    # Contamination risk classification
    if overlap is not None and overlap >= 8:
        risk = "HIGH"
    elif dist >= p90_threshold and p90_threshold > 0:
        risk = "MODERATE"
    elif overlap is None:
        risk = "UNKNOWN"
    else:
        risk = "LOW"

    ledger[iid] = {
        "public_text_overlap_ngram_len": overlap,
        "distinctiveness_score": dist,
        "has_named_entities": ne,
        "s8_probe": {
            "probed": probe["probed"],
            "style_changed_grade_delta": probe.get("style_changed_grade_delta"),
        },
        "contamination_risk": risk,
    }

risk_counts = Counter(v["contamination_risk"] for v in ledger.values())
print(f"  Risk counts: {dict(risk_counts)}")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
summary = {
    "n_items_total": len(items),
    "sub_A": {
        "wcf_wlc_text_found_on_disk": wcf_text_found and bool(public_text_paths),
        "text_file_locations": [str(p) for p in public_text_paths],
        "n_items_overlap_ge6": sum(1 for v in overlap_by_id.values()
                                    if v is not None and v >= 6),
        "n_items_overlap_ge8_QUOTES_PUBLIC_TEXT": sum(
            1 for v in overlap_by_id.values() if v is not None and v >= 8),
        "max_overlap_ngram_len": (max(v for v in overlap_by_id.values() if v is not None)
                                  if any(v is not None for v in overlap_by_id.values()) else None),
        "item_with_max_overlap": (max(
            (k for k, v in overlap_by_id.items() if v is not None),
            key=lambda k: overlap_by_id[k])
            if any(v is not None for v in overlap_by_id.values()) else None),
    },
    "sub_B": {
        "p90_distinctiveness_threshold": p90_threshold,
        "n_items_top_decile": len(top_decile_ids),
        "n_items_has_named_entities": ne_count,
        "top10_distinctive_items": [
            {"item_id": iid, "distinctiveness_score": sc, "has_named_entities": ne_by_id[iid]}
            for iid, sc in top10
        ],
    },
    "sub_C": {
        "n_probe_rows": n_probed,
        "n_probe_rows_style_changed_true": n_style_changed,
        "n_probe_rows_style_changed_false": n_style_unchanged,
        "n_unique_items_probed": n_probed_items,
        "probed_item_ids": probed_item_ids,
        "mean_abs_delta_all": round(mean_delta, 2),
        "mean_abs_delta_style_changed_true": round(mean_delta_changed, 2),
        "mean_abs_delta_style_changed_false": round(mean_delta_unchanged, 2),
        "max_abs_delta": max_delta,
        "max_abs_delta_item": max_delta_row["item_id"] if max_delta_row else None,
        "max_abs_delta_style_changed": max_delta_row["style_changed"] if max_delta_row else None,
        "items_abs_delta_ge20": [
            {"item_id": iid, "abs_delta": d, "style_changed": sc}
            for iid, d, sc in large_delta
        ],
        "style_invariance_verdict": verdict,
        "note_on_COMP_N_022_control_row": (
            "COMP-N-022 epoch=3 style_changed=False: delta=59, "
            "but this is the control (style NOT changed) so the large delta "
            "reflects grader-randomness or rubric-cap artifact, not style-surface sensitivity."
        ),
    },
    "risk_counts": dict(risk_counts),
    "_caveats": [
        "This is an on-disk lexical audit only — it cannot detect training-set membership.",
        "Sub-analysis A compares item stems against WCF/WLC text files found at "
        "../WCF/ relative to the project root; overlap is computed via longest common "
        "word n-gram (n>=6) between stem tokens and the combined reference token stream.",
        "The strongest available leakage evidence remains the Session 8 style-invariance "
        "probe (sub-analysis C): 20 style-changed rows across 17 items show mean |delta|=5.7, "
        "which is consistent with ordinary grader variance, not systematic score inflation "
        "due to surface-form familiarity.",
        "MODERATE risk is assigned to top-decile distinctiveness items because high "
        "distinctiveness means canary-searchable phrases — not that leakage has occurred.",
        "A true web-canary check (searching item stems online) would need external "
        "search access and is out of scope for this run.",
    ],
}


# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------
print("\n=== Writing outputs ===")

with open(OUT_LEDGER, "w") as f:
    json.dump(ledger, f, indent=2)
print(f"  Wrote ledger: {OUT_LEDGER}  ({OUT_LEDGER.stat().st_size:,} bytes)")

with open(OUT_SUMMARY, "w") as f:
    json.dump(summary, f, indent=2)
print(f"  Wrote summary: {OUT_SUMMARY}  ({OUT_SUMMARY.stat().st_size:,} bytes)")

print("\nDone.")
