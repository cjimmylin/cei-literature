#!/usr/bin/env python3
"""
Build expanded feature matrix: merge Phase 1 (40 papers) + Phase 2b gem
assessments (15 papers) → unified scoring → revised top-15 selection.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python MORAL-PSYCH/build_expanded_matrix.py
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WS_DIR = SCRIPT_DIR.parent
DATE_PREFIX = "20260403"


# ── Scoring functions (replicated from build_feature_matrix.py) ──────

def score_a1(theories: list) -> float:
    n = len(theories)
    return {0: 0, 1: 30, 2: 60, 3: 80}.get(n, 100 if n >= 4 else 80)

def score_a2(rating: int) -> float:
    return {1: 10, 2: 40, 3: 70, 4: 100}.get(rating, 0)

def score_a4(instrument: str) -> float:
    i = instrument.lower() if instrument else ""
    if "validated" in i:
        return 100
    if "original" in i:
        return 80
    return 0

def score_a5(baseline: str) -> float:
    b = baseline.lower() if baseline else ""
    if "published_norms" in b:
        return 100
    if "paper_specific" in b:
        return 70
    if "partial" in b:
        return 40
    return 0

def score_a6(rating: int) -> float:
    return {1: 10, 2: 30, 3: 50, 4: 75, 5: 100}.get(rating, 0)

def score_b1(fmt: str) -> float:
    f = fmt.lower() if fmt else ""
    if "mcq" in f or "multiple" in f:
        return 100
    if "binary" in f:
        return 90
    if "forced" in f:
        return 85
    if "likert" in f:
        return 70
    if "scenario" in f or "rating" in f:
        return 60
    if "mixed" in f:
        return 50
    if "free" in f or "text" in f:
        return 30
    if "multi-turn" in f or "multi_turn" in f:
        return 20
    if "game" in f:
        return 15
    return 50

def score_b2(size) -> float:
    if not size or size == 0:
        return 20
    s = int(size)
    if s < 50:
        return 20
    if s < 200:
        return 40
    if s < 1000:
        return 60
    if s < 5000:
        return 75
    if s < 20000:
        return 85
    return 100

def score_b10(fidelity: str) -> float:
    f = fidelity.lower() if fidelity else ""
    if "direct" in f:
        return 100
    if "adapted" in f:
        return 70
    if "substantial" in f:
        return 40
    if "paradigm" in f:
        return 10
    return 50

def score_c1(citations: int) -> float:
    if citations < 5:
        return 10
    if citations < 20:
        return 30
    if citations < 50:
        return 50
    if citations < 100:
        return 65
    if citations < 200:
        return 75
    if citations < 500:
        return 85
    return 100

def score_c2(citations: int, year: int) -> float:
    age = max(2026 - year + 0.5, 0.5)
    rate = citations / age
    if rate < 2:
        return 15
    if rate < 5:
        return 30
    if rate < 10:
        return 50
    if rate < 25:
        return 65
    if rate < 50:
        return 80
    if rate < 100:
        return 90
    return 100


def compute_composites(entry: dict) -> dict:
    """Compute PD, PE, CI composites and final COMPOSITE."""
    # PD = A2*0.25 + A6*0.20 + A1*0.15 + A5*0.15 + A3*0.15 + A4*0.10
    a1 = entry.get("A1_score", 30)
    a2 = entry.get("A2_score", 50)
    a3 = entry.get("A3_score", 70)  # default 70
    a4 = entry.get("A4_score", 50)
    a5 = entry.get("A5_score", 0)
    a6 = entry.get("A6_score", 50)
    pd = a2 * 0.25 + a6 * 0.20 + a1 * 0.15 + a5 * 0.15 + a3 * 0.15 + a4 * 0.10

    # PE = B3*0.20 + B2*0.15 + B6*0.15 + B7*0.15 + B1*0.10 + B4*0.10 + B10*0.15
    b1 = entry.get("B1_score", 50)
    b2 = score_b2(entry.get("B2_size", 0))
    b3 = entry.get("B3_score", 70 if entry.get("data_available") else 10)
    b4 = entry.get("B4_score", 10)
    b6 = entry.get("B6_score", 30)
    b7 = entry.get("B7_score", 30)
    b10 = entry.get("B10_score", 50)
    pe = b3 * 0.20 + b2 * 0.15 + b6 * 0.15 + b7 * 0.15 + b1 * 0.10 + b4 * 0.10 + b10 * 0.15

    # CI = C1*0.30 + C2*0.30 + C3*0.25 + C5*0.15
    citations = entry.get("C1_citations") or 0
    year = entry.get("year") or 2025
    c1 = score_c1(citations)
    c2 = score_c2(citations, year)
    c3 = entry.get("C3_score", 20)
    c5 = entry.get("C5_score", 0)
    ci = c1 * 0.30 + c2 * 0.30 + c3 * 0.25 + c5 * 0.15

    composite = pd * 0.50 + pe * 0.30 + ci * 0.20

    return {
        "PD": round(pd, 1),
        "PE": round(pe, 1),
        "CI": round(ci, 1),
        "composite": round(composite, 1),
    }


def convert_gem_to_matrix_entry(gem: dict, citations_map: dict) -> dict:
    """Convert a gem assessment entry into the feature matrix format."""
    file = gem["file"]
    year_match = re.match(r"(\d{4})", file)
    year = int(year_match.group(1)) if year_match else 2025

    theories = gem.get("theories_verified", [])
    citations = citations_map.get(file, 0)

    entry = {
        "file": file,
        "short_title": gem.get("short_title", ""),
        "year": year,
        "source": "gem_assessment",
        "A1_theories": theories,
        "A1_score": score_a1(theories),
        "A2_operationalization": gem.get("A2_operationalization", 2),
        "A2_score": gem.get("A2_score", score_a2(gem.get("A2_operationalization", 2))),
        "A2_rationale": gem.get("A2_rationale", ""),
        "A3_score": 70,  # default
        "A4_source_instrument": gem.get("A4_source_instrument", "none"),
        "A4_score": gem.get("A4_score", score_a4(gem.get("A4_source_instrument", "none"))),
        "A5_human_baseline": gem.get("A5_human_baseline", "none"),
        "A5_score": gem.get("A5_score", score_a5(gem.get("A5_human_baseline", "none"))),
        "A6_construct_validity": gem.get("A6_construct_validity", 3),
        "A6_score": gem.get("A6_score", score_a6(gem.get("A6_construct_validity", 3))),
        "A6_rationale": gem.get("A6_rationale", ""),
        "A7_cultural_provenance": gem.get("A7_cultural_provenance", "WEIRD-only"),
        "A8_languages": gem.get("A8_languages", ["English"]),
        "B1_format": gem.get("B1_format", "Mixed"),
        "B1_score": gem.get("B1_score", score_b1(gem.get("B1_format", "Mixed"))),
        "B2_size": gem.get("B2_size", 0),
        "B10_llm_fidelity": gem.get("B10_llm_fidelity", "Adapted"),
        "B10_score": gem.get("B10_score", score_b10(gem.get("B10_llm_fidelity", "Adapted"))),
        "B3_score": 70 if gem.get("data_available") else 10,
        "B4_score": 10,
        "B6_score": 30,  # conservative default for gems without harness data
        "B7_score": 30,
        "C1_citations": citations,
        "C3_score": 20,  # conservative; gems are often newer
        "C5_score": 0,
        "data_available": gem.get("data_available", False),
        "data_url": gem.get("data_url", "NA"),
    }

    composites = compute_composites(entry)
    entry.update(composites)
    return entry


def select_top15(matrix: list) -> list:
    """Apply theory caps, hard gates, and diversity fills to select top 15."""
    # Hard gates: PD >= 40 AND data available
    eligible = [e for e in matrix if e["PD"] >= 40 and e.get("data_available", False)]

    # Sort by composite descending
    eligible.sort(key=lambda x: -x["composite"])

    # Theory classification
    def get_theory_group(entry):
        theories = [t.lower() for t in entry.get("A1_theories", [])]
        for t in theories:
            if "trolley" in t:
                return "trolley"
            if "mft" in t or "moral foundations" in t:
                return "mft"
            if "schwartz" in t or "pvq" in t or "value" in t:
                return "schwartz"
            if "kohlberg" in t or "dit" in t or "developmental" in t:
                return "kohlberg"
            if "dual" in t or "greene" in t:
                return "dual_process"
            if "intuitionist" in t or "haidt" in t:
                return "intuitionist"
            if "dyadic" in t or "gray" in t:
                return "dyadic"
            if "identity" in t:
                return "identity"
        return "other"

    CAPS = {"trolley": 3, "mft": 4}
    MINS = {"schwartz": 2, "kohlberg": 1}

    # Greedy selection with caps
    selected = []
    theory_counts = defaultdict(int)
    seen_files = set()

    for entry in eligible:
        if len(selected) >= 15:
            break
        if entry["file"] in seen_files:
            continue
        group = get_theory_group(entry)
        if theory_counts[group] >= CAPS.get(group, 99):
            continue
        selected.append(entry)
        theory_counts[group] += 1
        seen_files.add(entry["file"])

    # Diversity fills
    if len(selected) < 15:
        for group, min_count in MINS.items():
            if theory_counts[group] < min_count:
                for entry in eligible:
                    if entry["file"] in seen_files:
                        continue
                    if get_theory_group(entry) == group:
                        selected.append(entry)
                        theory_counts[group] += 1
                        seen_files.add(entry["file"])
                        if theory_counts[group] >= min_count:
                            break

    # Fill remaining slots
    if len(selected) < 15:
        for entry in eligible:
            if len(selected) >= 15:
                break
            if entry["file"] not in seen_files:
                selected.append(entry)
                seen_files.add(entry["file"])

    # Re-sort and rank
    selected.sort(key=lambda x: -x["composite"])
    for i, entry in enumerate(selected[:15]):
        entry["rank"] = i + 1

    return selected[:15]


def main():
    # Load Phase 1 feature matrix
    p1_path = SCRIPT_DIR / f"{DATE_PREFIX}-moral-psych-benchmark-feature-matrix.json"
    with open(p1_path) as f:
        p1_data = json.load(f)
    p1_matrix = p1_data["matrix"]
    print(f"Phase 1 matrix: {len(p1_matrix)} entries")

    # Normalize Phase 1 entries: lift scores.PD/PE/CI to top level
    for entry in p1_matrix:
        entry["source"] = "phase1_assessment"
        if "scores" in entry:
            scores = entry["scores"]
            entry["PD"] = scores.get("PD", 0)
            entry["PE"] = scores.get("PE", 0)
            entry["CI"] = scores.get("CI", 0)
            if "composite" not in entry:
                entry["composite"] = entry["PD"] * 0.50 + entry["PE"] * 0.30 + entry["CI"] * 0.20
        # Ensure data_available field
        if "data_available" not in entry:
            entry["data_available"] = bool(entry.get("data_url") and entry.get("data_url") != "NA")

    # Load gem assessments
    gem_path = SCRIPT_DIR / f"{DATE_PREFIX}-gem-depth-assessment-merged.json"
    with open(gem_path) as f:
        gem_data = json.load(f)
    gems = gem_data["entries"]
    print(f"Gem assessments: {len(gems)} entries")

    # Load citation data for cross-reference
    cite_path = SCRIPT_DIR / f"{DATE_PREFIX}-citation-counts.json"
    citations_map = {}
    if cite_path.exists():
        with open(cite_path) as f:
            cite_data = json.load(f)
        # Handle both list and dict formats
        entries = cite_data if isinstance(cite_data, list) else cite_data.get("citations", cite_data.get("entries", []))
        for entry in entries:
            if isinstance(entry, dict) and "file" in entry:
                citations_map[entry["file"]] = entry.get("citation_count", 0)

    # Convert gems to matrix entries
    gem_files_in_p1 = {e["file"] for e in p1_matrix}
    new_gems = []
    for gem in gems:
        if gem["file"] not in gem_files_in_p1:
            entry = convert_gem_to_matrix_entry(gem, citations_map)
            new_gems.append(entry)
        else:
            print(f"  Gem already in Phase 1: {gem['file']}")

    print(f"New gem entries (not in Phase 1): {len(new_gems)}")

    # Merge
    expanded = p1_matrix + new_gems

    # --- Dedup by data_url: keep highest-composite entry per URL ---
    seen_urls: dict[str, int] = {}  # data_url → index in deduped list
    deduped = []
    removed_dupes = []
    for entry in sorted(expanded, key=lambda x: -x.get("composite", 0)):
        durl = entry.get("data_url", "")
        if durl and durl != "NA" and durl in seen_urls:
            removed_dupes.append(entry["file"])
            continue
        if durl and durl != "NA":
            seen_urls[durl] = len(deduped)
        deduped.append(entry)
    if removed_dupes:
        print(f"Removed {len(removed_dupes)} duplicate(s) by data_url: {removed_dupes}")
    expanded = deduped

    # --- Manual data-availability overrides for published instruments ---
    MANUAL_DATA_OVERRIDES = {
        "2024-Khandelwal-Multilingual Defining Issues Test.md": {
            "data_available": True,
            "override_reason": "DIT is a published validated instrument (Rest 1979); "
                               "scenarios reproducible from paper (EACL 2024)",
        },
    }
    for entry in expanded:
        if entry["file"] in MANUAL_DATA_OVERRIDES:
            entry.update(MANUAL_DATA_OVERRIDES[entry["file"]])
            print(f"Override applied: {entry['file']} → data_available=True")

    print(f"Expanded matrix: {len(expanded)} total entries")

    # Re-sort by composite
    expanded.sort(key=lambda x: -x.get("composite", 0))

    # Save expanded matrix
    output = {
        "summary": {
            "total_entries": len(expanded),
            "phase1_entries": len(p1_matrix),
            "gem_entries": len(new_gems),
            "date": DATE_PREFIX,
            "weighting": "PD=0.50, PE=0.30, CI=0.20",
        },
        "matrix": expanded,
    }
    matrix_path = SCRIPT_DIR / f"{DATE_PREFIX}-expanded-feature-matrix.json"
    matrix_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved expanded matrix: {matrix_path}")

    # Select revised top-15
    top15 = select_top15(expanded)
    print(f"\nRevised Top-15:")
    for entry in top15:
        print(f"  #{entry['rank']}: {entry['short_title']} ({entry['year']}) — composite {entry['composite']}")

    # Load Phase 1 top-15 for comparison
    p1_top15_path = SCRIPT_DIR / f"{DATE_PREFIX}-moral-psych-top15-selection.json"
    with open(p1_top15_path) as f:
        p1_top15 = json.load(f)
    p1_files = {e["file"] for e in p1_top15["top_15"]}
    v2_files = {e["file"] for e in top15}
    added = v2_files - p1_files
    removed = p1_files - v2_files

    print(f"\nChanges vs v1:")
    print(f"  Added: {added}")
    print(f"  Removed: {removed}")

    # Save revised selection
    selection = {
        "selection_date": DATE_PREFIX,
        "version": "v2",
        "methodology": p1_top15["methodology"],
        "changes_from_v1": {
            "added": list(added),
            "removed": list(removed),
            "reason": "Expanded keyword scorer + 15 hidden gem assessments",
        },
        "top_15": top15,
    }
    sel_path = SCRIPT_DIR / f"{DATE_PREFIX}-moral-psych-top15-selection-v2.json"
    sel_path.write_text(json.dumps(selection, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved: {sel_path}")

    # Generate markdown report
    report = generate_report(top15, p1_top15["top_15"], added, removed, expanded)
    report_path = SCRIPT_DIR / f"{DATE_PREFIX}-moral-psych-top15-benchmark-selection-v2.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Saved: {report_path}")


def generate_report(top15, v1_top15, added, removed, full_matrix):
    """Generate the v2 selection report markdown."""
    lines = [
        "# Moral Psychology Benchmarks: Revised Top-15 Selection (v2)",
        "",
        f"**Date:** 2026-04-03",
        f"**Version:** v2 (expanded keyword scorer + hidden gem assessment)",
        f"**Weighting:** PD=0.50, PE=0.30, CI=0.20",
        "",
        "## Changes from v1",
        "",
    ]

    if added:
        lines.append("### Added")
        for f in added:
            entry = next((e for e in top15 if e["file"] == f), None)
            if entry:
                lines.append(f"- **{entry['short_title']}** ({entry['year']}) — composite {entry['composite']}")
        lines.append("")

    if removed:
        lines.append("### Removed")
        for f in removed:
            entry = next((e for e in v1_top15 if e["file"] == f), None)
            if entry:
                lines.append(f"- **{entry['short_title']}** ({entry['year']}) — composite {entry.get('composite', 'N/A')}")
        lines.append("")

    lines.extend([
        "## Revised Top-15",
        "",
        "| # | Benchmark | Year | Theory | Format | Size | Composite | PD | PE | CI |",
        "|---|-----------|------|--------|--------|------|-----------|----|----|-----|",
    ])

    for e in top15:
        theories = ", ".join(e.get("A1_theories", []))[:30]
        fmt = e.get("B1_format", "?")
        size = e.get("B2_size", "?")
        lines.append(
            f"| {e['rank']} | {e['short_title'][:50]} | {e['year']} | {theories} "
            f"| {fmt} | {size} | {e['composite']} | {e['PD']} | {e['PE']} | {e['CI']} |"
        )

    lines.extend([
        "",
        "## Theory Coverage",
        "",
    ])
    theory_count = defaultdict(int)
    for e in top15:
        for t in e.get("A1_theories", []):
            theory_count[t.lower()] += 1
    for theory, count in sorted(theory_count.items(), key=lambda x: -x[1]):
        lines.append(f"- **{theory}**: {count} papers")

    lines.extend([
        "",
        f"## Full Matrix",
        f"",
        f"Total entries in expanded matrix: {len(full_matrix)}",
        f"Entries passing hard gates (PD≥40 + data): {sum(1 for e in full_matrix if e.get('PD', 0) >= 40 and e.get('data_available'))}",
        "",
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    main()
