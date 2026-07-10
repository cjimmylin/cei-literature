#!/usr/bin/env python3
"""
Select stratified gold-standard samples for precision/recall validation.

For each of 7 non-Western frameworks, selects:
- Detected pool (score >= 50): stratified by score range (50-65, 66-80, 81-100),
  up to 50 total. For small-n frameworks (<50 detected), uses ALL detected +
  supplements with borderline (30-49).
- Non-detected pool (score < 50): stratified by range (0, 1-29, 30-49), 50 total.

Output:
  COUNCIL/20260403-gold-standard-sample.json
  COUNCIL/20260403-gold-standard-labeling-sheet.md

Council Deliberation #2, Phase 1B.
"""
from __future__ import annotations

import functools
import json
import random
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
_PYTHON_DIR = _CEI_LIT_WS / "PYTHON"
_AGENT_LIB = _CEI_LIT_WS / ".agent" / "lib"
sys.path.insert(0, str(_PYTHON_DIR))
sys.path.insert(0, str(_AGENT_LIB))

from config import PAPERS_DIR

# =====================================================================
# CONSTANTS
# =====================================================================

DATA_FILE = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "DATA" / "20260403-nw-scores.json"
COUNCIL_DIR = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "COUNCIL"

# NW_FIELDS auto-detected from JSON data at runtime (see main())
NW_FIELDS: list[str] = []

# Both field name variants supported (JSON may use either)
FRAMEWORK_DISPLAY = {
    "nw_confucian": "Confucian Role Ethics",
    "nw_ubuntu": "Ubuntu Communalism",
    "nw_islamic_jurisprudence": "Islamic Jurisprudence (Usul al-Fiqh)",
    "nw_islamic_ethics": "Islamic Jurisprudence (Usul al-Fiqh)",
    "nw_buddhist": "Buddhist Ethics",
    "nw_dharmic": "Dharmic Ethics (Hindu/Jain/Sikh)",
    "nw_indigenous_relational": "Indigenous Relational Ethics",
    "nw_buen_vivir": "Buen Vivir / Sumak Kawsay",
}

DETECTED_STRATA = [(50, 65), (66, 80), (81, 100)]
NON_DETECTED_STRATA = [(0, 0), (1, 29), (30, 49)]

TARGET_DETECTED = 50
TARGET_NON_DETECTED = 50

SEED = 42


# =====================================================================
# HELPERS
# =====================================================================

def _get_short_title(filename: str) -> str:
    """Extract short_title from paper YAML frontmatter."""
    paper_path = PAPERS_DIR / filename
    if not paper_path.exists():
        return ""
    try:
        content = paper_path.read_text(encoding="utf-8", errors="replace")[:3000]
        m = re.search(r'^short_title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        return m.group(1) if m else ""
    except Exception:
        return ""


def _stratified_sample(
    papers: list[dict],
    strata: list[tuple[int, int]],
    target: int,
    rng: random.Random,
) -> list[dict]:
    """Proportional stratified sample from papers based on score strata."""
    buckets: dict[tuple[int, int], list[dict]] = {}
    for lo, hi in strata:
        buckets[(lo, hi)] = [p for p in papers if lo <= p["score"] <= hi]

    total_pop = sum(len(b) for b in buckets.values())
    if total_pop == 0:
        return []

    sampled: list[dict] = []
    remaining_target = target

    # Proportional allocation
    allocations: dict[tuple[int, int], int] = {}
    for stratum, bucket in buckets.items():
        if total_pop > 0:
            alloc = int(round(len(bucket) / total_pop * target))
        else:
            alloc = 0
        # Cannot sample more than available
        alloc = min(alloc, len(bucket))
        allocations[stratum] = alloc

    # Adjust if rounding caused total != target
    total_alloc = sum(allocations.values())
    diff = target - total_alloc
    # Distribute remainder to largest strata
    if diff > 0:
        sorted_strata = sorted(allocations.keys(), key=lambda s: len(buckets[s]), reverse=True)
        for stratum in sorted_strata:
            can_add = len(buckets[stratum]) - allocations[stratum]
            add = min(diff, can_add)
            allocations[stratum] += add
            diff -= add
            if diff <= 0:
                break

    # Sample from each stratum
    for stratum, alloc in allocations.items():
        bucket = buckets[stratum]
        if alloc >= len(bucket):
            sampled.extend(bucket)
        else:
            sampled.extend(rng.sample(bucket, alloc))

    return sampled


# =====================================================================
# MAIN
# =====================================================================

def main():
    global NW_FIELDS

    print("Loading NW scores data...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    papers = data["papers"]

    # Auto-detect field names from JSON data
    if papers:
        NW_FIELDS = [k for k in papers[0]["scores"].keys() if k.startswith("nw_")]
    print(f"Fields from JSON: {NW_FIELDS}")
    print(f"Loaded {len(papers)} papers")

    COUNCIL_DIR.mkdir(parents=True, exist_ok=True)

    rng = random.Random(SEED)

    result: dict[str, dict] = {}
    labeling_lines: list[str] = []
    labeling_lines.append("# Gold Standard Labeling Sheet")
    labeling_lines.append("")
    labeling_lines.append("**Date:** 2026-04-03")
    labeling_lines.append(f"**Random seed:** {SEED}")
    labeling_lines.append("")
    labeling_lines.append("Instructions: For each paper, write **Y** (truly relevant to this framework),")
    labeling_lines.append("**N** (not relevant), or **U** (uncertain) in the Label column.")
    labeling_lines.append("")

    for field in NW_FIELDS:
        display_name = FRAMEWORK_DISPLAY[field]
        print(f"\nProcessing {display_name} ({field})...")

        # Partition papers by score for this field
        all_scored = []
        for p in papers:
            score = p["scores"].get(field, 0)
            all_scored.append({"filename": p["filename"], "score": score})

        detected = [p for p in all_scored if p["score"] >= 50]
        non_detected = [p for p in all_scored if p["score"] < 50]

        # ── Detected pool sampling ──────────────────────────────────
        is_small_n = len(detected) < TARGET_DETECTED

        if is_small_n:
            # Use ALL detected + supplement with borderline (30-49)
            detected_sample = list(detected)
            borderline = [p for p in non_detected if 30 <= p["score"] <= 49]
            supplement_needed = TARGET_DETECTED - len(detected_sample)
            if supplement_needed > 0 and borderline:
                supplement = rng.sample(borderline, min(supplement_needed, len(borderline)))
                detected_sample.extend(supplement)
            print(f"  Small-n: all {len(detected)} detected + {len(detected_sample) - len(detected)} borderline supplement")
        else:
            detected_sample = _stratified_sample(detected, DETECTED_STRATA, TARGET_DETECTED, rng)
            print(f"  Detected sample: {len(detected_sample)} / {len(detected)}")

        # ── Non-detected pool sampling ──────────────────────────────
        non_detected_sample = _stratified_sample(non_detected, NON_DETECTED_STRATA, TARGET_NON_DETECTED, rng)
        print(f"  Non-detected sample: {len(non_detected_sample)} / {len(non_detected)}")

        # Sort samples by score descending
        detected_sample.sort(key=lambda x: x["score"], reverse=True)
        non_detected_sample.sort(key=lambda x: x["score"], reverse=True)

        # Load titles for labeling sheet
        print(f"  Loading titles...")
        for p in detected_sample + non_detected_sample:
            p["title"] = _get_short_title(p["filename"])

        # Store result
        result[field] = {
            "display_name": display_name,
            "total_detected": len(detected),
            "detected_sample_size": len(detected_sample),
            "non_detected_sample_size": len(non_detected_sample),
            "small_n": is_small_n,
            "detected_sample": detected_sample,
            "non_detected_sample": non_detected_sample,
        }

        # ── Labeling sheet section ──────────────────────────────────
        labeling_lines.append(f"## {display_name} (`{field}`)")
        labeling_lines.append("")
        labeling_lines.append(f"Total detected (>=50): {len(detected)} | "
                              f"Detected sample: {len(detected_sample)} | "
                              f"Non-detected sample: {len(non_detected_sample)}")
        if is_small_n:
            labeling_lines.append(f"*Small-n framework: all detected included + borderline supplement*")
        labeling_lines.append("")

        labeling_lines.append("### Detected Pool Sample")
        labeling_lines.append("")
        labeling_lines.append("| # | Paper | Title | Score | Label | Notes |")
        labeling_lines.append("|---|-------|-------|-------|-------|-------|")
        for i, p in enumerate(detected_sample, 1):
            fn = p["filename"][:65] + "..." if len(p["filename"]) > 68 else p["filename"]
            title = (p.get("title", "") or "")[:50]
            labeling_lines.append(f"| {i} | {fn} | {title} | {p['score']} | | |")
        labeling_lines.append("")

        labeling_lines.append("### Non-Detected Pool Sample")
        labeling_lines.append("")
        labeling_lines.append("| # | Paper | Title | Score | Label | Notes |")
        labeling_lines.append("|---|-------|-------|-------|-------|-------|")
        for i, p in enumerate(non_detected_sample, 1):
            fn = p["filename"][:65] + "..." if len(p["filename"]) > 68 else p["filename"]
            title = (p.get("title", "") or "")[:50]
            labeling_lines.append(f"| {i} | {fn} | {title} | {p['score']} | | |")
        labeling_lines.append("")

    # ── Write JSON ──────────────────────────────────────────────────
    json_path = COUNCIL_DIR / "20260403-gold-standard-sample.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "date": "20260403",
            "seed": SEED,
            "target_detected": TARGET_DETECTED,
            "target_non_detected": TARGET_NON_DETECTED,
            "frameworks": result,
        }, f, indent=2, ensure_ascii=False)
    print(f"\nWrote JSON: {json_path.name}")

    # ── Write labeling sheet ────────────────────────────────────────
    sheet_path = COUNCIL_DIR / "20260403-gold-standard-labeling-sheet.md"
    sheet_path.write_text("\n".join(labeling_lines), encoding="utf-8")
    print(f"Wrote labeling sheet: {sheet_path.name}")

    # ── Summary ─────────────────────────────────────────────────────
    print("\n=== SUMMARY ===")
    for field in NW_FIELDS:
        r = result[field]
        small = " (SMALL-N)" if r["small_n"] else ""
        print(f"  {r['display_name']:40s}  detected={r['total_detected']:3d}  "
              f"det_sample={r['detected_sample_size']:3d}  "
              f"non_det_sample={r['non_detected_sample_size']:3d}{small}")


if __name__ == "__main__":
    main()
