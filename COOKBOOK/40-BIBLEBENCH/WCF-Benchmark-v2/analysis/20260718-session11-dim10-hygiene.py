"""
20260718-session11-dim10-hygiene.py
Dimension 10 — Metadata / Schema Hygiene analysis for all 287 WCF-Benchmark-v2 items.

Outputs:
  analysis/20260718-session11-ledger-dim10.json   — per-item hygiene ledger
  analysis/20260718-session11-dim10-summary.json  — corpus-level summary

Run from WCF-Benchmark-v2/ root:
  .venv-v2/bin/python analysis/20260718-session11-dim10-hygiene.py
"""

import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "analysis"

MAIN_FILE = DATA_DIR / "wcf_main.jsonl"
EP_FILE   = DATA_DIR / "wcf_episodes.jsonl"

LEDGER_OUT  = OUT_DIR / "20260718-session11-ledger-dim10.json"
SUMMARY_OUT = OUT_DIR / "20260718-session11-dim10-summary.json"

# ---------------------------------------------------------------------------
# Canonical anchor citation pattern (inferred from corpus)
# Covers:
#   WLC Q### [optional: –range | H# | Hn | Rule[s] N[–N] | head N]
#   WCF ##.##
#   WSC Q##
# ---------------------------------------------------------------------------
ANCHOR_PAT = re.compile(
    r'^('
    r'WLC Q\d+(?:[–\-]\d+)?(?:\s+(?:H[1-4]|Rule[s]?\s+\d+(?:[–\-]\d+)?|head\s+\d+|Q\d+))?'
    r'|WCF \d+\.\d+'
    r'|WSC Q\d+'
    r')$'
)

# ---------------------------------------------------------------------------
# Dominant points-total band: computed from corpus
# The corpus spans 4.0–9.0; the mode is 5.0 (n=83) and second mode 6.0 (n=64).
# We define "dominant band" as [5.0, 6.0] (covers 147/287 = 51 %).
# Flags: POINTS_LOW  (<5.0), POINTS_HIGH (>6.0).
# Note: design groups differ (MEND median=7.5; STED median=7.0; WHOLE median=6.0)
# so flag is informational — not a hard error.
# ---------------------------------------------------------------------------
POINTS_DOMINANT_LO = 5.0
POINTS_DOMINANT_HI = 6.0

# Rubric-size band from spec: 4–6
RUBRIC_BAND_LO = 4
RUBRIC_BAND_HI = 6

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

main_items = load_jsonl(MAIN_FILE)
ep_items   = load_jsonl(EP_FILE)
all_items  = main_items + ep_items

# Tag source file for later reference
for item in main_items:
    item["_source"] = "wcf_main.jsonl"
for item in ep_items:
    item["_source"] = "wcf_episodes.jsonl"

# ---------------------------------------------------------------------------
# Stem-length percentiles (chars and words) — computed once for flagging
# ---------------------------------------------------------------------------
stem_chars = [len(i["stem"]) for i in all_items]
stem_words = [len(i["stem"].split()) for i in all_items]

n = len(all_items)
_sc_sorted = sorted(stem_chars)
_sw_sorted = sorted(stem_words)

def percentile(sorted_list, p):
    idx = max(0, min(len(sorted_list) - 1, int(len(sorted_list) * p / 100)))
    return sorted_list[idx]

P1_CHARS  = percentile(_sc_sorted, 1)
P99_CHARS = percentile(_sc_sorted, 99)
P1_WORDS  = percentile(_sw_sorted, 1)
P99_WORDS = percentile(_sw_sorted, 99)

# ---------------------------------------------------------------------------
# Duplicate-ID / duplicate-key check (corpus-level, done once)
# ---------------------------------------------------------------------------
all_ids  = [i["id"]  for i in all_items]
all_keys = [i["key"] for i in all_items]

dup_id_counts  = {k: v for k, v in Counter(all_ids).items()  if v > 1}
dup_key_counts = {k: v for k, v in Counter(all_keys).items() if v > 1}
DUPLICATE_IDS_FOUND  = bool(dup_id_counts)
DUPLICATE_KEYS_FOUND = bool(dup_key_counts)

# ---------------------------------------------------------------------------
# Per-item hygiene analysis
# ---------------------------------------------------------------------------

def analyse_item(item):
    """Return a dict of computed values + hygiene_flags list."""
    item_id  = item["id"]
    rubric   = item.get("rubric", [])
    kind     = item["kind"]
    episode  = item["episode"]
    source   = item["_source"]

    flags = []

    # ------------------------------------------------------------------
    # 1. anchor_coverage
    # ------------------------------------------------------------------
    n_criteria = len(rubric)
    anchors = [r.get("anchor", "") for r in rubric]
    non_empty_anchors = [a for a in anchors if a.strip()]
    anchor_coverage = len(non_empty_anchors) / n_criteria if n_criteria > 0 else None

    if n_criteria == 0:
        anchor_coverage_flag = "NO_RUBRIC"
        flags.append("NO_RUBRIC")
    elif anchor_coverage == 0.0:
        anchor_coverage_flag = "ANCHORLESS"
        flags.append("ANCHORLESS")
    elif anchor_coverage < 1.0:
        anchor_coverage_flag = "PARTIAL"
        flags.append("PARTIAL_ANCHOR")
    else:
        anchor_coverage_flag = "FULL"

    # ------------------------------------------------------------------
    # 2. anchor_format — check each non-empty anchor against canonical pattern
    # ------------------------------------------------------------------
    deviant_anchors = [a for a in non_empty_anchors if not ANCHOR_PAT.match(a)]
    if deviant_anchors:
        flags.append("ANCHOR_FORMAT_DEVIANT")

    # ------------------------------------------------------------------
    # 3. points_total
    # ------------------------------------------------------------------
    points_total = sum(r.get("points", 0) for r in rubric)
    points_flag = None
    if points_total < POINTS_DOMINANT_LO:
        points_flag = "POINTS_LOW"
        flags.append("POINTS_LOW")
    elif points_total > POINTS_DOMINANT_HI:
        points_flag = "POINTS_HIGH"
        flags.append("POINTS_HIGH")

    # ------------------------------------------------------------------
    # 4. rubric_size
    # ------------------------------------------------------------------
    rubric_size = n_criteria
    rubric_size_flag = None
    if rubric_size < RUBRIC_BAND_LO:
        rubric_size_flag = "RUBRIC_SMALL"
        flags.append("RUBRIC_SMALL")
    elif rubric_size > RUBRIC_BAND_HI:
        rubric_size_flag = "RUBRIC_LARGE"
        flags.append("RUBRIC_LARGE")

    # ------------------------------------------------------------------
    # 5. stem_length
    # ------------------------------------------------------------------
    stem = item["stem"]
    stem_len_chars = len(stem)
    stem_len_words = len(stem.split())
    stem_flag = None
    if stem_len_chars < P1_CHARS or stem_len_words < P1_WORDS:
        stem_flag = "STEM_SHORT_OUTLIER"
        flags.append("STEM_SHORT_OUTLIER")
    if stem_len_chars > P99_CHARS or stem_len_words > P99_WORDS:
        stem_flag = "STEM_LONG_OUTLIER"
        flags.append("STEM_LONG_OUTLIER")

    # ------------------------------------------------------------------
    # 6. duplicate_key_check (per-item annotation; corpus-level done above)
    # ------------------------------------------------------------------
    dup_id_flag  = DUPLICATE_IDS_FOUND  and dup_id_counts.get(item_id, 0) > 1
    dup_key_flag = DUPLICATE_KEYS_FOUND and dup_key_counts.get(item["key"], 0) > 1
    if dup_id_flag:
        flags.append("DUPLICATE_ID")
    if dup_key_flag:
        flags.append("DUPLICATE_KEY")

    # ------------------------------------------------------------------
    # 7. gold_order_consistency
    # ------------------------------------------------------------------
    gold_order = item.get("gold_order")
    go_flag = None
    if kind == "ordinal":
        if gold_order is None:
            go_flag = "ORDINAL_MISSING_GOLD_ORDER"
            flags.append("ORDINAL_MISSING_GOLD_ORDER")
        # else: correct
    else:
        if gold_order is not None:
            go_flag = "NON_ORDINAL_HAS_GOLD_ORDER"
            flags.append("NON_ORDINAL_HAS_GOLD_ORDER")

    # ------------------------------------------------------------------
    # 8. episode_field_consistency
    # ------------------------------------------------------------------
    ep_flag = None
    if source == "wcf_main.jsonl":
        if episode is not False:
            ep_flag = "MAIN_ITEM_EPISODE_TRUE"
            flags.append("MAIN_ITEM_EPISODE_TRUE")
        if "pressure_turn" in item:
            ep_flag = "MAIN_ITEM_HAS_PRESSURE_TURN"
            flags.append("MAIN_ITEM_HAS_PRESSURE_TURN")
    elif source == "wcf_episodes.jsonl":
        if episode is not True:
            ep_flag = "EP_ITEM_EPISODE_FALSE"
            flags.append("EP_ITEM_EPISODE_FALSE")
        if "pressure_turn" not in item:
            ep_flag = "EP_ITEM_MISSING_PRESSURE_TURN"
            flags.append("EP_ITEM_MISSING_PRESSURE_TURN")

    # ------------------------------------------------------------------
    # 9. commandments
    # ------------------------------------------------------------------
    commandments = item.get("commandments", [])
    cmd_flags = []
    if not commandments:
        cmd_flags.append("EMPTY_COMMANDMENTS")
        flags.append("EMPTY_COMMANDMENTS")
    else:
        for c in commandments:
            if isinstance(c, str) and c.startswith("C"):
                try:
                    n_cmd = int(c[1:])
                    if not (1 <= n_cmd <= 10):
                        cmd_flags.append(f"COMMANDMENT_OUT_OF_RANGE:{c}")
                        flags.append("COMMANDMENT_OUT_OF_RANGE")
                except ValueError:
                    cmd_flags.append(f"COMMANDMENT_INVALID:{c}")
                    flags.append("COMMANDMENT_INVALID")
            elif c == "XC":
                pass  # XC = cross-commandment; legitimate special value
            else:
                cmd_flags.append(f"COMMANDMENT_UNUSUAL:{c}")
                flags.append("COMMANDMENT_UNUSUAL")

    # ------------------------------------------------------------------
    # 10. missing_mold_field (structural / schema-level gap — noted per item)
    # ------------------------------------------------------------------
    has_mold_field = "mold" in item
    has_provenance = "provenance" in item
    # (no flag added per-item; recorded in summary as schema gap)

    # ------------------------------------------------------------------
    # Build output record
    # ------------------------------------------------------------------
    return {
        "id": item_id,
        "source": source,
        "kind": kind,
        "design": item.get("design"),
        "track": item.get("track"),
        "tier": item.get("tier"),
        # anchor_coverage
        "anchor_coverage": round(anchor_coverage, 4) if anchor_coverage is not None else None,
        "anchor_coverage_flag": anchor_coverage_flag,
        # anchor_format
        "deviant_anchors": deviant_anchors,
        "anchor_format_ok": len(deviant_anchors) == 0,
        # points
        "points_total": points_total,
        "points_flag": points_flag,
        # rubric_size
        "rubric_size": rubric_size,
        "rubric_size_flag": rubric_size_flag,
        # stem_length
        "stem_len_chars": stem_len_chars,
        "stem_len_words": stem_len_words,
        "stem_flag": stem_flag,
        # duplicates
        "duplicate_id": dup_id_flag,
        "duplicate_key": dup_key_flag,
        # gold_order
        "gold_order_present": gold_order is not None,
        "gold_order_flag": go_flag,
        # episode
        "episode_flag": ep_flag,
        # commandments
        "commandments": commandments,
        "commandments_flags": cmd_flags,
        # schema gaps
        "has_mold_field": has_mold_field,
        "has_provenance_field": has_provenance,
        # result
        "hygiene_flags": flags,
        "n_flags": len(flags),
    }


ledger = {item["id"]: analyse_item(item) for item in all_items}

# ---------------------------------------------------------------------------
# Corpus-level summary
# ---------------------------------------------------------------------------

all_records = list(ledger.values())

# Flag counts
all_flags = []
for rec in all_records:
    all_flags.extend(rec["hygiene_flags"])
flag_counts = dict(Counter(all_flags).most_common())

# Fully clean items
clean_ids = [rec["id"] for rec in all_records if rec["n_flags"] == 0]

# Points-total distribution
pts_dist = dict(sorted(Counter(rec["points_total"] for rec in all_records).items()))

# Rubric-size distribution
rsize_dist = dict(sorted(Counter(rec["rubric_size"] for rec in all_records).items()))

# Stem-length stats
sc_vals = [rec["stem_len_chars"] for rec in all_records]
sw_vals = [rec["stem_len_words"] for rec in all_records]
stem_stats = {
    "chars_min": min(sc_vals), "chars_max": max(sc_vals),
    "chars_mean": round(statistics.mean(sc_vals), 1),
    "chars_median": statistics.median(sc_vals),
    "chars_p1": P1_CHARS, "chars_p99": P99_CHARS,
    "words_min": min(sw_vals), "words_max": max(sw_vals),
    "words_mean": round(statistics.mean(sw_vals), 1),
    "words_median": statistics.median(sw_vals),
    "words_p1": P1_WORDS, "words_p99": P99_WORDS,
}

# Anchor citation pattern
anchor_pat_description = (
    r"^(WLC Q\d+([–\-]\d+)?(\s+(H[1-4]|Rule[s]?\s+\d+([–\-]\d+)?|head\s+\d+|Q\d+))?|WCF \d+\.\d+|WSC Q\d+)$"
)
n_anchors_total    = sum(len([a for a in [r.get("anchor","") for r in i.get("rubric",[])] if a.strip()]) for i in all_items)
n_anchor_deviants  = sum(len(rec["deviant_anchors"]) for rec in all_records)

# gold_order kind cross-tab
kind_go_crosstab = defaultdict(lambda: {"with_gold_order": 0, "without_gold_order": 0})
for item in all_items:
    k = item["kind"]
    go = item.get("gold_order")
    if go is not None:
        kind_go_crosstab[k]["with_gold_order"] += 1
    else:
        kind_go_crosstab[k]["without_gold_order"] += 1
kind_go_crosstab = {k: dict(v) for k, v in sorted(kind_go_crosstab.items())}

# NON_ORDINAL_HAS_GOLD_ORDER violations
go_violations = [rec["id"] for rec in all_records if "NON_ORDINAL_HAS_GOLD_ORDER" in rec["hygiene_flags"]]

# Top-10 worst hygiene items (by n_flags, then alpha by id)
worst_10 = sorted(all_records, key=lambda r: (-r["n_flags"], r["id"]))[:10]
worst_10_summary = [
    {"id": r["id"], "n_flags": r["n_flags"], "hygiene_flags": r["hygiene_flags"]}
    for r in worst_10
]

# Schema gap: mold/provenance fields
items_with_mold       = sum(1 for r in all_records if r["has_mold_field"])
items_with_provenance = sum(1 for r in all_records if r["has_provenance_field"])

summary = {
    "generated_by": "20260718-session11-dim10-hygiene.py",
    "date": "2026-07-18",
    "corpus": {
        "total_items": len(all_items),
        "main_file_items": len(main_items),
        "episode_file_items": len(ep_items),
    },
    "clean_items": {
        "count": len(clean_ids),
        "ids": clean_ids,
    },
    "flag_counts_ranked": flag_counts,
    "points_total_distribution": pts_dist,
    "points_dominant_band": [POINTS_DOMINANT_LO, POINTS_DOMINANT_HI],
    "rubric_size_distribution": rsize_dist,
    "rubric_band_spec": [RUBRIC_BAND_LO, RUBRIC_BAND_HI],
    "rubric_actual_range": [min(rsize_dist.keys()), max(rsize_dist.keys())],
    "stem_length_stats": stem_stats,
    "anchor_citation_pattern": {
        "regex": anchor_pat_description,
        "description": "WLC Q### [optional sub-locator] | WCF chapter.section | WSC Q##",
        "total_non_empty_anchors": n_anchors_total,
        "conforming": n_anchors_total - n_anchor_deviants,
        "deviants": n_anchor_deviants,
    },
    "duplicate_check": {
        "duplicate_ids_found": DUPLICATE_IDS_FOUND,
        "duplicate_ids": dup_id_counts,
        "duplicate_keys_found": DUPLICATE_KEYS_FOUND,
        "duplicate_keys_count": len(dup_key_counts),
    },
    "gold_order_consistency": {
        "kind_crosstab": kind_go_crosstab,
        "non_ordinal_with_gold_order_violations": go_violations,
        "violation_count": len(go_violations),
    },
    "episode_field_consistency": {
        "main_items_with_episode_true": sum(
            1 for i in main_items if i.get("episode") is not False
        ),
        "ep_items_missing_pressure_turn": sum(
            1 for i in ep_items if "pressure_turn" not in i
        ),
        "main_items_with_pressure_turn": sum(
            1 for i in main_items if "pressure_turn" in i
        ),
    },
    "commandments_summary": {
        "xc_items": sum(1 for i in all_items if "XC" in i.get("commandments", [])),
        "xc_note": "XC = cross-commandment; treated as valid special value",
        "empty_commandments": sum(1 for i in all_items if not i.get("commandments")),
        "out_of_range": sum(
            1 for i in all_items
            for c in i.get("commandments", [])
            if isinstance(c, str) and c.startswith("C") and
               not (1 <= int(c[1:]) <= 10 if c[1:].isdigit() else True)
        ),
    },
    "schema_gap_mold_provenance": {
        "note": (
            "Neither 'mold' nor 'provenance' is an explicit field in wcf_main.jsonl or "
            "wcf_episodes.jsonl. Cohort/session provenance is inferred from the id prefix "
            "(AGG/COMP/CROSS/…) and the session draft lists in data/session*-drafts/. "
            "This is a structural schema gap — no per-item flag emitted."
        ),
        "items_with_mold_field": items_with_mold,
        "items_with_provenance_field": items_with_provenance,
    },
    "worst_hygiene_top10": worst_10_summary,
}

# ---------------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------------
with open(LEDGER_OUT, "w") as f:
    json.dump(ledger, f, indent=2)

with open(SUMMARY_OUT, "w") as f:
    json.dump(summary, f, indent=2)

print(f"Ledger  : {LEDGER_OUT}")
print(f"Summary : {SUMMARY_OUT}")
print()
print(f"Total items : {len(all_items)}")
print(f"Clean items : {len(clean_ids)}")
print()
print("Top flags:")
for flag, cnt in list(Counter(all_flags).most_common(10)):
    print(f"  {flag:<35} {cnt}")
print()
print(f"Anchor deviants : {n_anchor_deviants}")
print(f"Duplicate IDs   : {dup_id_counts or 'None'}")
print(f"Gold-order violations (non-ordinal): {go_violations}")
