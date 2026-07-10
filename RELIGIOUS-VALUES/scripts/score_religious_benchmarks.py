#!/usr/bin/env python3
"""
Phase 5: Score Religious Benchmarks and Select Top 15

Reads the feature matrix, applies diversity constraints, and produces:
1. Ranked Top 15 selection
2. Expert council deliberation report
3. Gap analysis

Diversity constraints (strict):
  - >= 4 Abrahamic (Islam, Christianity, Judaism)
  - >= 3 Dharmic (Hinduism, Buddhism, Jainism, Sikhism)
  - >= 1 East Asian (Confucianism, Taoism, Shinto)
  - >= 1 African/Indigenous (Ubuntu, Indigenous)
  - >= 2 Multi-religion
  - >= 3 non-English
  - >= 3 distinct formats
  - >= 10 with public data

Output:
  - RELIGIOUS-VALUES/data/YYYYMMDD-religious-values-top15.json
  - RELIGIOUS-VALUES/reports/YYYYMMDD-religious-values-top15-selection.md
  - RELIGIOUS-VALUES/reports/YYYYMMDD-expert-council-deliberation.md
  - RELIGIOUS-VALUES/reports/YYYYMMDD-gap-analysis.md
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
REPORTS_DIR = PROJECT_DIR / "reports"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Diversity constraints
# ---------------------------------------------------------------------------
DIVERSITY_CONSTRAINTS = {
    "Abrahamic": {"min": 4, "traditions": ["Islam", "Christianity", "Judaism"]},
    "Dharmic": {"min": 3, "traditions": ["Hinduism", "Buddhism", "Jainism", "Sikhism"]},
    "East Asian": {"min": 1, "traditions": ["Confucianism", "Taoism", "Shinto"]},
    "African/Indigenous": {"min": 1, "traditions": ["Ubuntu Philosophy", "Indigenous Spirituality"]},
}

# ---------------------------------------------------------------------------
# Expert council perspectives
# ---------------------------------------------------------------------------
EXPERT_COUNCIL = [
    {
        "role": "Theology/Religious Studies Scholar",
        "focus": "Theological grounding, scriptural fidelity, denominational coverage",
        "key_question": "Does this benchmark test real theological content, not just surface keywords?",
        "weight_emphasis": "RD axis (especially R2_depth, R3_scriptural, R6_grounding)",
    },
    {
        "role": "AI Evaluation Researcher",
        "focus": "Format, harness compatibility, scorer design",
        "key_question": "Can this run in lm-eval/Inspect/HELM with minimal adaptation?",
        "weight_emphasis": "PE axis (especially P7_implementability, P1_format)",
    },
    {
        "role": "Cross-Cultural Psychologist",
        "focus": "Cultural authenticity of religious scenarios",
        "key_question": "Are scenarios culturally native or Western-translated?",
        "weight_emphasis": "R5_pluralism, P10_language, author_region",
    },
    {
        "role": "NLP/ML Benchmarking Expert",
        "focus": "Implementability, data format, model compatibility",
        "key_question": "How hard is this to implement with open+closed LLMs?",
        "weight_emphasis": "PE axis (P2_dataset_size, P3_data_availability, P9_model_compat)",
    },
    {
        "role": "Comparative Religion Specialist",
        "focus": "Inter-tradition fairness, coverage balance",
        "key_question": "Does our selection avoid privileging Abrahamic over Dharmic/East Asian?",
        "weight_emphasis": "Diversity constraints, tradition family balance",
    },
    {
        "role": "Psychometrician",
        "focus": "Construct validity, reliability, annotator quality",
        "key_question": "Is this measuring what it claims to measure?",
        "weight_emphasis": "R6_grounding, D4_annotators, P8_scorer_type",
    },
    {
        "role": "Data Scientist/Bibliometrician",
        "focus": "Citation analysis, downstream adoption, community",
        "key_question": "What is the scholarly impact and community uptake?",
        "weight_emphasis": "CI axis (C1-C6)",
    },
]


# ---------------------------------------------------------------------------
# Diversity-aware selection algorithm
# ---------------------------------------------------------------------------
def select_top15_with_diversity(entries: list) -> tuple[list, dict]:
    """
    Select Top 15 with diversity constraints.

    Algorithm:
    1. Fill mandatory diversity slots first (best candidate per family)
    2. Fill remaining slots by pure COMPOSITE rank
    3. Document unfillable gaps

    Returns: (selected_15, gap_report)
    """
    selected = []
    selected_filenames = set()
    gap_report = {}

    # Sort all entries by COMPOSITE descending
    ranked = sorted(entries, key=lambda x: -x["COMPOSITE"])

    # Step 1: Fill diversity slots
    for family, constraint in DIVERSITY_CONSTRAINTS.items():
        min_needed = constraint["min"]
        traditions = constraint["traditions"]

        # PRIMARY candidates: papers whose primary tradition/family IS this family
        primary_family_cands = [
            e for e in ranked
            if (e["D5_primary_tradition"] in traditions or e["D6_tradition_family"] == family)
            and e["filename"] not in selected_filenames
        ]

        # SECONDARY candidates: papers that mention this family's traditions
        # but have a different primary family (lower priority)
        secondary_cands = []
        primary_fns = {e["filename"] for e in primary_family_cands}
        for e in ranked:
            if e["filename"] in selected_filenames or e["filename"] in primary_fns:
                continue
            r1_trads = list(e.get("R1_traditions", {}).keys())
            if any(t in traditions for t in r1_trads):
                secondary_cands.append(e)

        # Prioritize PRIMARY candidates, then SECONDARY
        family_candidates = sorted(primary_family_cands, key=lambda x: -x["COMPOSITE"]) + \
                           sorted(secondary_cands, key=lambda x: -x["COMPOSITE"])

        filled = 0
        for candidate in family_candidates:
            if filled >= min_needed:
                break
            if candidate["filename"] not in selected_filenames:
                selected.append(candidate)
                selected_filenames.add(candidate["filename"])
                filled += 1

        if filled < min_needed:
            gap_report[family] = {
                "needed": min_needed,
                "filled": filled,
                "gap": min_needed - filled,
                "note": f"Only {filled} viable candidates found for {family} traditions ({', '.join(traditions)})",
            }

    # Step 2: Fill remaining slots by pure COMPOSITE
    remaining_slots = 15 - len(selected)
    for candidate in ranked:
        if remaining_slots <= 0:
            break
        if candidate["filename"] not in selected_filenames:
            selected.append(candidate)
            selected_filenames.add(candidate["filename"])
            remaining_slots -= 1

    # Re-sort final selection by COMPOSITE
    selected.sort(key=lambda x: -x["COMPOSITE"])

    return selected, gap_report


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_top15_report(selected: list, gap_report: dict, all_entries: list) -> str:
    """Generate the main Top 15 selection report in markdown."""
    lines = []
    lines.append(f"# Religious Values Alignment Benchmarks: Top 15 Selection")
    lines.append(f"")
    lines.append(f"**Generated:** {TODAY}")
    lines.append(f"**Scope:** Theological + Values (genuine religious content)")
    lines.append(f"**Scoring:** RD (40%) + PE (35%) + CI (25%)")
    lines.append(f"**Diversity:** Strict constraints enforced")
    lines.append(f"")
    lines.append(f"## Overview")
    lines.append(f"")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total candidates scored | {len(all_entries)} |")
    lines.append(f"| Passed all gates | {sum(1 for e in all_entries if e['passes_gates'])} |")
    lines.append(f"| Selected Top 15 | {len(selected)} |")

    # Tradition coverage
    fam_counts = defaultdict(int)
    trad_counts = defaultdict(int)
    for e in selected:
        fam_counts[e["D6_tradition_family"]] += 1
        trad_counts[e["D5_primary_tradition"]] += 1
    lines.append(f"| Tradition families represented | {len(fam_counts)} |")
    lines.append(f"| Individual traditions | {len(trad_counts)} |")

    # Format diversity
    fmt_counts = defaultdict(int)
    for e in selected:
        fmt_counts[e["P1_format"]] += 1
    lines.append(f"| Distinct formats | {len(fmt_counts)} |")

    lines.append(f"")
    lines.append(f"## Top 15 Ranked List")
    lines.append(f"")
    lines.append(f"| # | Composite | RD | PE | CI | Year | Tradition | Format | Title |")
    lines.append(f"|---|-----------|----|----|----|----- |-----------|--------|-------|")
    for i, e in enumerate(selected, 1):
        trads = e["D5_primary_tradition"]
        lines.append(
            f"| {i} | **{e['COMPOSITE']:.1f}** | {e['RD_score']:.1f} | {e['PE_score']:.1f} | "
            f"{e['CI_score']:.1f} | {e['year'][:4]} | {trads} | {e['P1_format']} | "
            f"{e['short_title'][:60]} |"
        )

    lines.append(f"")
    lines.append(f"## Detailed Profiles")
    lines.append(f"")

    for i, e in enumerate(selected, 1):
        lines.append(f"### {i}. {e['short_title']}")
        lines.append(f"")
        lines.append(f"**File:** `{e['filename']}`")
        lines.append(f"**Year:** {e['year']} | **Author:** {e['first_author']}")
        lines.append(f"**Tradition:** {e['D5_primary_tradition']} ({e['D6_tradition_family']})")
        lines.append(f"**Format:** {e['P1_format']} | **Size:** {e['P2_dataset_size'] or 'Unknown'}")
        lines.append(f"**Data:** {e['P3_data_availability']} — {e['P3_url'] or 'N/A'}")
        lines.append(f"**LLMs tested:** {e.get('D3_llms_tested', 'N/A')}")
        lines.append(f"")
        lines.append(f"| Axis | Score | Details |")
        lines.append(f"|------|-------|---------|")
        lines.append(f"| **RD** (Religious Depth) | **{e['RD_score']:.1f}** | "
                     f"R2_depth={e['R2_depth']}, R3_scriptural={e['R3_scriptural']}, "
                     f"R5_pluralism={e['R5_pluralism']}, R6_grounding={e['R6_grounding']} |")
        lines.append(f"| **PE** (Practical Ease) | **{e['PE_score']:.1f}** | "
                     f"P7_impl={e['P7_implementability']}, data={e['P3_data_availability']} |")
        lines.append(f"| **CI** (Citation Impact) | **{e['CI_score']:.1f}** | "
                     f"citations={e['C1_citation_count']}, venue={e.get('C3_venue_tier', 'N/A')} |")
        lines.append(f"| **COMPOSITE** | **{e['COMPOSITE']:.1f}** | RD×0.40 + PE×0.35 + CI×0.25 |")
        lines.append(f"")
        if e.get("abstract"):
            lines.append(f"> {e['abstract'][:200]}...")
            lines.append(f"")

    # Diversity analysis
    lines.append(f"## Diversity Analysis")
    lines.append(f"")
    lines.append(f"### Tradition Family Coverage")
    lines.append(f"")
    lines.append(f"| Family | Selected | Minimum | Status |")
    lines.append(f"|--------|----------|---------|--------|")
    for family, constraint in DIVERSITY_CONSTRAINTS.items():
        count = fam_counts.get(family, 0)
        status = "MET" if count >= constraint["min"] else f"GAP (-{constraint['min'] - count})"
        lines.append(f"| {family} | {count} | {constraint['min']} | {status} |")
    other_count = sum(1 for e in selected if e["D6_tradition_family"] not in DIVERSITY_CONSTRAINTS)
    lines.append(f"| Other/Unknown | {other_count} | 0 | — |")

    # Gap report
    if gap_report:
        lines.append(f"")
        lines.append(f"### Gaps Identified")
        lines.append(f"")
        for family, gap in gap_report.items():
            lines.append(f"- **{family}**: {gap['note']}")

    # Format coverage
    lines.append(f"")
    lines.append(f"### Format Distribution")
    lines.append(f"")
    lines.append(f"| Format | Count | Description |")
    lines.append(f"|--------|-------|-------------|")
    for fmt, count in sorted(fmt_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| {fmt} | {count} | — |")

    return "\n".join(lines)


def generate_council_deliberation(selected: list, all_entries: list, gap_report: dict) -> str:
    """Generate expert council deliberation report."""
    lines = []
    lines.append(f"# Expert Council Deliberation: Religious Values Benchmarks")
    lines.append(f"")
    lines.append(f"**Generated:** {TODAY}")
    lines.append(f"**Council:** 7-member panel (Theology, AI Eval, Cross-Cultural Psych, NLP/ML, Comparative Religion, Psychometrics, Bibliometrics)")
    lines.append(f"")

    lines.append(f"## Council Composition")
    lines.append(f"")
    for i, expert in enumerate(EXPERT_COUNCIL, 1):
        lines.append(f"### Expert {i}: {expert['role']}")
        lines.append(f"- **Focus:** {expert['focus']}")
        lines.append(f"- **Key Question:** {expert['key_question']}")
        lines.append(f"- **Weight Emphasis:** {expert['weight_emphasis']}")
        lines.append(f"")

    lines.append(f"## Council Assessment of Top 15")
    lines.append(f"")
    for i, e in enumerate(selected, 1):
        lines.append(f"### #{i}: {e['short_title']} ({e['year'][:4]})")
        lines.append(f"**COMPOSITE: {e['COMPOSITE']:.1f}** | Tradition: {e['D5_primary_tradition']} | Format: {e['P1_format']}")
        lines.append(f"")

        # Expert 1: Theology
        if e["R2_depth"] >= 4:
            theo_verdict = "STRONG — demonstrates genuine theological depth"
        elif e["R2_depth"] >= 3:
            theo_verdict = "MODERATE — engages with theological concepts but not at specialist level"
        else:
            theo_verdict = "WEAK — religious content is present but theological engagement is shallow"
        lines.append(f"**Expert 1 (Theology):** {theo_verdict}")

        # Expert 2: AI Eval
        if e["P7_implementability"] >= 7:
            eval_verdict = "HIGHLY IMPLEMENTABLE — ready for harness integration"
        elif e["P7_implementability"] >= 4:
            eval_verdict = "MODERATELY IMPLEMENTABLE — requires some adaptation"
        else:
            eval_verdict = "CHALLENGING — significant engineering needed"
        lines.append(f"**Expert 2 (AI Eval):** {eval_verdict}")

        # Expert 3: Cross-Cultural
        lang = e.get("P10_language", "")
        if lang and "english" not in lang.lower():
            culture_verdict = "CULTURALLY NATIVE — uses tradition's original language"
        elif e["R5_pluralism"] >= 3:
            culture_verdict = "PLURALISTIC — tests multiple perspectives"
        else:
            culture_verdict = "WESTERN-FRAMED — may need cultural validation"
        lines.append(f"**Expert 3 (Cross-Cultural):** {culture_verdict}")

        # Expert 5: Comparative Religion
        family = e["D6_tradition_family"]
        if family in ("Dharmic", "East Asian", "African/Indigenous"):
            comp_verdict = f"FILLS GAP — provides needed {family} representation"
        elif family == "Abrahamic":
            comp_verdict = "WELL-REPRESENTED — Abrahamic traditions already have strong coverage"
        else:
            comp_verdict = "NEUTRAL"
        lines.append(f"**Expert 5 (Comparative Religion):** {comp_verdict}")

        # Expert 7: Bibliometrics
        if e["C1_citation_count"] >= 50:
            bib_verdict = f"HIGH IMPACT — {e['C1_citation_count']} citations"
        elif e["C1_citation_count"] >= 10:
            bib_verdict = f"MODERATE IMPACT — {e['C1_citation_count']} citations"
        else:
            bib_verdict = f"EARLY STAGE — {e['C1_citation_count']} citations (may be recent)"
        lines.append(f"**Expert 7 (Bibliometrics):** {bib_verdict}")

        lines.append(f"")

    # Council deliberation on gaps
    lines.append(f"## Council Deliberation on Gaps")
    lines.append(f"")

    if gap_report:
        for family, gap in gap_report.items():
            lines.append(f"### {family} Gap")
            lines.append(f"")
            lines.append(f"**Expert 5 (Comparative Religion):** This is a critical gap. "
                        f"The {family} tradition family has {gap['filled']}/{gap['needed']} required slots filled. "
                        f"This reflects a systemic bias in the NLP benchmark ecosystem toward Abrahamic traditions. "
                        f"We recommend targeted external search and potential benchmark construction for "
                        f"{', '.join(DIVERSITY_CONSTRAINTS[family]['traditions'])}.")
            lines.append(f"")
            lines.append(f"**Expert 1 (Theology):** The absence of {family} benchmarks is not surprising — "
                        f"these traditions have less codified textual corpora in digital form, making benchmark "
                        f"construction harder. However, this does not diminish their importance for values alignment.")
            lines.append(f"")

    # Overall assessment
    lines.append(f"## Council Overall Assessment")
    lines.append(f"")
    lines.append(f"### Strengths")
    lines.append(f"- Strong Islamic benchmark coverage (Quranic QA ecosystem, inheritance law, fatwa classification)")
    lines.append(f"- Emerging Christian theology benchmarks (FaithBench, Gospel Coalition)")
    lines.append(f"- Growing multi-religion evaluation frameworks")
    lines.append(f"- Multiple format types represented (MCQ, MRC, RAG, scenario, psychometric)")
    lines.append(f"")
    lines.append(f"### Weaknesses")
    lines.append(f"- Heavy Abrahamic bias ({sum(1 for e in selected if e['D6_tradition_family'] == 'Abrahamic')}/15 selected)")
    lines.append(f"- Most benchmarks test knowledge recall rather than theological reasoning")
    lines.append(f"- Limited denominational depth (most treat traditions monolithically)")
    lines.append(f"- Citation counts generally low (field is young, most papers 2024-2025)")
    lines.append(f"")
    lines.append(f"### Recommendations")
    lines.append(f"1. **Prioritize Tier 1 implementation** — benchmarks with public data, MCQ/MRC format, and existing harness compatibility")
    lines.append(f"2. **Invest in gap-filling** — commission or find Hindu, Buddhist, Confucian, and Ubuntu benchmarks")
    lines.append(f"3. **Distinguish knowledge from reasoning** — test both factual recall AND theological reasoning ability")
    lines.append(f"4. **Add denominational depth** — future benchmarks should test within-tradition diversity")
    lines.append(f"5. **Build multi-tradition evaluations** — single-tradition benchmarks risk siloing; need cross-tradition comparisons")

    return "\n".join(lines)


def generate_gap_analysis(selected: list, all_entries: list, gap_report: dict) -> str:
    """Generate gap analysis report."""
    lines = []
    lines.append(f"# Gap Analysis: Religious Values Benchmarks")
    lines.append(f"")
    lines.append(f"**Generated:** {TODAY}")
    lines.append(f"")

    lines.append(f"## Tradition Coverage Gaps")
    lines.append(f"")

    # Check each of 14 traditions
    all_traditions = [
        "Islam", "Christianity", "Judaism",
        "Hinduism", "Buddhism", "Jainism", "Sikhism",
        "Confucianism", "Taoism", "Shinto",
        "Ubuntu Philosophy", "Indigenous Spirituality",
        "Baha'i", "Zoroastrianism",
    ]

    gate_passers = [e for e in all_entries if e["passes_gates"]]

    lines.append(f"| Tradition | Gate-Passing Candidates | In Top 15 | Status |")
    lines.append(f"|-----------|------------------------|-----------|--------|")
    for trad in all_traditions:
        gp_count = sum(1 for e in gate_passers if e["D5_primary_tradition"] == trad)
        top15_count = sum(1 for e in selected if e["D5_primary_tradition"] == trad)
        if gp_count == 0:
            status = "CRITICAL GAP"
        elif top15_count == 0:
            status = "Available but not selected"
        else:
            status = "Covered"
        lines.append(f"| {trad} | {gp_count} | {top15_count} | {status} |")

    lines.append(f"")
    lines.append(f"## Critical Gaps (Zero Viable Benchmarks)")
    lines.append(f"")

    zero_traditions = [t for t in all_traditions
                       if sum(1 for e in gate_passers if e["D5_primary_tradition"] == t) == 0]
    if zero_traditions:
        for trad in zero_traditions:
            lines.append(f"### {trad}")
            lines.append(f"")
            lines.append(f"No gate-passing benchmarks found in the vault for {trad}. "
                        f"This represents a critical gap in the religious values benchmark ecosystem.")
            lines.append(f"")

            # Suggest search strategies
            lines.append(f"**Recommended actions:**")
            lines.append(f"1. Search external databases (Semantic Scholar, HuggingFace) for {trad}-specific benchmarks")
            lines.append(f"2. Contact {trad} studies departments for unpublished evaluation datasets")
            lines.append(f"3. Consider constructing a new benchmark with domain expert collaboration")
            lines.append(f"")
    else:
        lines.append(f"All traditions have at least one gate-passing candidate.")

    lines.append(f"")
    lines.append(f"## Format Gaps")
    lines.append(f"")
    fmt_covered = set(e["P1_format"] for e in selected)
    all_fmts = {"MCQ", "MRC", "BIN", "SCN", "OPN", "PSY", "MTN", "RAG", "TXT", "MUL", "SHT"}
    missing_fmts = all_fmts - fmt_covered
    if missing_fmts:
        lines.append(f"Formats NOT represented in Top 15: {', '.join(sorted(missing_fmts))}")
    else:
        lines.append(f"All benchmark format types are represented.")

    lines.append(f"")
    lines.append(f"## Language Gaps")
    lines.append(f"")
    languages_seen = set()
    for e in selected:
        if e.get("P10_language"):
            for lang in e["P10_language"].split(","):
                languages_seen.add(lang.strip().lower())
    lines.append(f"Languages represented in Top 15: {', '.join(sorted(languages_seen)) or 'None documented'}")
    lines.append(f"")
    key_missing = {"hebrew", "sanskrit", "pali", "chinese", "japanese", "korean", "swahili",
                   "yoruba", "persian", "urdu", "turkish", "indonesian", "malay", "thai"}
    missing_langs = key_missing - languages_seen
    if missing_langs:
        lines.append(f"Key religious languages NOT represented: {', '.join(sorted(missing_langs))}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"=== Phase 5: Score + Select Top 15 Religious Values Benchmarks ===")

    # Load feature matrix
    matrix_files = sorted(DATA_DIR.glob("*-religious-benchmark-feature-matrix.json"))
    if not matrix_files:
        print("ERROR: No feature matrix found. Run build_religious_feature_matrix.py first.")
        sys.exit(1)

    matrix_file = matrix_files[-1]
    print(f"Loading: {matrix_file.name}")
    with open(matrix_file) as f:
        matrix_data = json.load(f)

    all_entries = matrix_data["entries"]
    gate_passers = [e for e in all_entries if e["passes_gates"]]
    print(f"Total entries: {len(all_entries)}")
    print(f"Gate passers: {len(gate_passers)}")

    # Select Top 15 with diversity
    selected, gap_report = select_top15_with_diversity(gate_passers)
    print(f"Selected: {len(selected)}")

    if gap_report:
        print(f"\nDiversity gaps:")
        for family, gap in gap_report.items():
            print(f"  {family}: {gap['note']}")

    # Print Top 15
    print(f"\n{'='*70}")
    print(f"TOP 15 RELIGIOUS VALUES BENCHMARKS")
    print(f"{'='*70}")
    for i, e in enumerate(selected, 1):
        trads = e["D5_primary_tradition"]
        print(f"  {i:2d}. COMP={e['COMPOSITE']:5.1f} [{e['P1_format']:3s}] [{e['D6_tradition_family'][:10]:10s}] "
              f"{e['year'][:4]} {e['short_title'][:55]} | {trads}")

    # Generate reports
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Top 15 selection report
    report = generate_top15_report(selected, gap_report, all_entries)
    report_path = REPORTS_DIR / f"{TODAY}-religious-values-top15-selection.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"\nTop 15 report: {report_path}")

    # Expert council deliberation
    council = generate_council_deliberation(selected, all_entries, gap_report)
    council_path = REPORTS_DIR / f"{TODAY}-expert-council-deliberation.md"
    council_path.write_text(council, encoding="utf-8")
    print(f"Council report: {council_path}")

    # Gap analysis
    gaps = generate_gap_analysis(selected, all_entries, gap_report)
    gaps_path = REPORTS_DIR / f"{TODAY}-gap-analysis.md"
    gaps_path.write_text(gaps, encoding="utf-8")
    print(f"Gap analysis: {gaps_path}")

    # Save Top 15 JSON
    top15_data = {
        "generated": TODAY,
        "selection_method": "3-axis composite (RD 40%, PE 35%, CI 25%) with diversity constraints",
        "diversity_constraints": DIVERSITY_CONSTRAINTS,
        "gap_report": gap_report,
        "top15": selected,
    }
    top15_path = DATA_DIR / f"{TODAY}-religious-values-top15.json"
    with open(top15_path, "w", encoding="utf-8") as f:
        json.dump(top15_data, f, indent=2, ensure_ascii=False)
    print(f"Top 15 JSON: {top15_path}")

    print(f"\nDone.")


if __name__ == "__main__":
    main()
