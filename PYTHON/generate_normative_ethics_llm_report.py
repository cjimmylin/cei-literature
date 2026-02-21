#!/usr/bin/env python3
"""
Generate a reference list of normative ethics conference papers applied to LLMs.

Reads YAML frontmatter from 35 hardcoded paper files and produces a formatted
markdown report with full academic citations, LLMs tested, and summary statistics.

Output: STATISTICS/20260220-normative-ethics-llm-conference-papers.md
"""

import sys
from pathlib import Path
from collections import Counter

# Add parent dir so we can import yaml_utils
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter

# =============================================================================
# CONFIGURATION
# =============================================================================

PAPERS_DIR = Path(__file__).resolve().parent.parent / "papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "STATISTICS" / "20260220-normative-ethics-llm-conference-papers.md"

# The 35 normative-ethics + conference + LLM-applied papers (hardcoded from plan)
PAPER_FILENAMES = [
    "2018-Zhao-Gender Bias in Coreference Resolution.md",
    "2021-Hendrycks-Aligning AI with Shared Human Values.md",
    "2021-Prabhumoye-Case Study.md",
    "2021-Röttger-HateCheck.md",
    "2022-Li-Evaluating Psychological Safety of Large Language.md",
    "2022-Qiu-ValueNet.md",
    "2023-Jiang-MACHIAVELLI.md",
    "2023-Ziems-NormBank.md",
    "2024-Agarwal-Ethical Reasoning Depends on Language.md",
    "2024-Han-MedSafetyBench.md",
    "2024-Liu-Evaluating Moral Beliefs across LLMs through a.md",
    "2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented.md",
    "2024-Marraffini-The Greatest Good Benchmark.md",
    "2024-Obi-Value Imprint.md",
    "2024-Tu-CharacterEval.md",
    "2024-Vladimirova-FairJob.md",
    "2024-Yu-CMoralEval.md",
    "2024-Yuan-R-Judge.md",
    "2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning.md",
    "2025-Ashkinaze-Deep Value Benchmark.md",
    "2025-Dwivedi-EtiCor++ Towards Understanding Etiquettical Bias in LLMs.md",
    "2025-Farsi-ParsiPy NLP Toolkit for Historical Persian Texts in Python.md",
    "2025-Jourdan-FairTranslate.md",
    "2025-Kneer-Hard Problem AI Alignment Value Forks.md",
    "2025-Kumar-Are Rules Meant to be Broken.md",
    "2025-Kumar-UniMoral ACL 2025 Best Resource Paper.md",
    "2025-Lin-GAMEBoT Transparent Assessment of LLM Reasoning in Games.md",
    "2025-Mahajan-Mapping Moral Reasoning in LLMs.md",
    "2025-Mitchell-SHADES.md",
    "2025-Park-Deontological Keyword Bias.md",
    "2025-Samway-Are Language Models Consequentialist or Deontological.md",
    "2025-Tennant-Moral Alignment for LLM Agents.md",
    "2025-Tennant-Moral Intrinsic Rewards for Alignment.md",
    "2025-Xu-AncientBench Towards Comprehensive Evaluation on Excavated.md",
    "2025-Yuan-Probabilistic Aggregation and Targeted Embedding.md",
]


# =============================================================================
# HELPERS
# =============================================================================

def clean_authors(raw: str) -> str:
    """Strip wikilink brackets and normalize author separators."""
    if not raw:
        return "Unknown"
    # Remove [[ and ]]
    cleaned = raw.replace("[[", "").replace("]]", "")
    # Normalize separators: semicolons to commas for display
    # First, split on semicolons or commas
    if ";" in cleaned:
        parts = [p.strip() for p in cleaned.split(";") if p.strip()]
    else:
        parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    return ", ".join(parts)


def get_normative_types(fields: dict) -> str:
    """Return comma-separated list of normative ethics types for the paper."""
    types = []
    if fields.get("deontological_ethics", "").strip().lower() == "yes":
        types.append("Deontological")
    if fields.get("utilitarian_ethics", "").strip().lower() == "yes":
        types.append("Utilitarian")
    if fields.get("virtue_ethics", "").strip().lower() == "yes":
        types.append("Virtue Ethics")
    return ", ".join(types) if types else "N/A"


def build_venue(fields: dict) -> str:
    """Get the best venue string from CONF-CC or publication."""
    venue = fields.get("CONF-CC", "").strip()
    if not venue:
        venue = fields.get("publication", "").strip()
    if not venue:
        venue = fields.get("CONFERENCE", "").strip()
    return venue if venue else "Unknown Venue"


def build_link_line(fields: dict) -> str:
    """Build the DOI / URL line."""
    parts = []
    doi = fields.get("doi", "").strip()
    url = fields.get("url", "").strip()

    if doi and doi.upper() != "N/A":
        doi_url = f"https://doi.org/{doi}"
        parts.append(f"DOI: [{doi}]({doi_url})")
    if url:
        parts.append(f"[URL]({url})")

    return " | ".join(parts) if parts else ""


def build_llm_line(fields: dict) -> str:
    """Build the LLMs-tested line."""
    llm = fields.get("LLM_assessed", "").strip()
    if not llm or llm.upper() == "NA":
        return ""
    return llm


# =============================================================================
# MAIN
# =============================================================================

def main():
    # ------------------------------------------------------------------
    # 1. Read all 35 papers
    # ------------------------------------------------------------------
    papers = []
    errors = []

    for fname in PAPER_FILENAMES:
        fpath = PAPERS_DIR / fname
        if not fpath.exists():
            errors.append(f"NOT FOUND: {fname}")
            continue

        content = fpath.read_text(encoding="utf-8")
        try:
            fm_text, _ = extract_frontmatter(content)
            fields = parse_frontmatter(fm_text)
        except ValueError as e:
            errors.append(f"YAML ERROR in {fname}: {e}")
            continue

        papers.append({
            "filename": fname,
            "fields": fields,
        })

    if errors:
        print(f"WARNING: {len(errors)} errors encountered:")
        for e in errors:
            print(f"  - {e}")

    # ------------------------------------------------------------------
    # 2. Sort by year (asc), then first author (asc)
    # ------------------------------------------------------------------
    def sort_key(p):
        year = int(p["fields"].get("year", "9999"))
        authors = clean_authors(p["fields"].get("authors", ""))
        first = authors.split(",")[0].strip().lower()
        return (year, first)

    papers.sort(key=sort_key)

    # ------------------------------------------------------------------
    # 3. Build reference entries
    # ------------------------------------------------------------------
    entries = []
    normative_counts = Counter()
    year_counts = Counter()
    venue_counts = Counter()
    llm_counts = Counter()

    for idx, p in enumerate(papers, 1):
        f = p["fields"]
        authors = clean_authors(f.get("authors", ""))
        year = f.get("year", "????")
        title = f.get("short_title", "").strip().strip('"')
        venue = build_venue(f)
        link_line = build_link_line(f)
        llm_raw = build_llm_line(f)
        normative = get_normative_types(f)

        # Statistics
        year_counts[year] += 1
        venue_counts[venue] += 1
        for t in normative.split(", "):
            if t and t != "N/A":
                normative_counts[t] += 1
        if llm_raw:
            for model in [m.strip() for m in llm_raw.split(",")]:
                if model:
                    llm_counts[model] += 1

        # Build entry
        lines = []
        lines.append(f"**[{idx}]** {authors} ({year}). *{title}*. {venue}.")
        if link_line:
            lines.append(link_line)
        if llm_raw:
            lines.append(f"**LLMs tested:** {llm_raw}")
        lines.append(f"**Normative type:** {normative}")
        entries.append("\n".join(lines))

    # ------------------------------------------------------------------
    # 4. Build summary statistics
    # ------------------------------------------------------------------
    stats_lines = []

    # Normative branch counts
    stats_lines.append("### By Normative Ethics Branch\n")
    stats_lines.append("| Branch | Count |")
    stats_lines.append("|--------|-------|")
    for branch, count in normative_counts.most_common():
        stats_lines.append(f"| {branch} | {count} |")

    # Year distribution
    stats_lines.append("\n### By Publication Year\n")
    stats_lines.append("| Year | Count |")
    stats_lines.append("|------|-------|")
    for year in sorted(year_counts.keys()):
        stats_lines.append(f"| {year} | {year_counts[year]} |")

    # Top venues
    stats_lines.append("\n### Top Venues\n")
    stats_lines.append("| Venue | Count |")
    stats_lines.append("|-------|-------|")
    for venue, count in venue_counts.most_common(10):
        stats_lines.append(f"| {venue} | {count} |")

    # Most-tested LLMs
    stats_lines.append("\n### Most Frequently Tested LLMs\n")
    stats_lines.append("| LLM | Papers |")
    stats_lines.append("|-----|--------|")
    for model, count in llm_counts.most_common(15):
        stats_lines.append(f"| {model} | {count} |")

    # ------------------------------------------------------------------
    # 5. Write markdown report
    # ------------------------------------------------------------------
    report_lines = [
        "# Normative Ethics LLM Conference Papers",
        "",
        f"**Generated:** 2026-02-20",
        f"**Papers:** {len(papers)}",
        "",
        "**Selection criteria:** Papers from the CEI Literature Vault that (1) address normative ethics",
        "(deontological, utilitarian, or virtue ethics), (2) were presented at a conference or workshop",
        "venue, and (3) were empirically applied to large language models.",
        "",
        "---",
        "",
        "## Full Reference List",
        "",
    ]

    for entry in entries:
        report_lines.append(entry)
        report_lines.append("")

    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## Summary Statistics")
    report_lines.append("")
    report_lines.extend(stats_lines)
    report_lines.append("")

    report_text = "\n".join(report_lines)

    # Safety check: don't overwrite
    if OUTPUT_FILE.exists():
        print(f"ERROR: Output file already exists: {OUTPUT_FILE}")
        print("Refusing to overwrite (report immutability rule).")
        sys.exit(1)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(report_text, encoding="utf-8")
    print(f"Report written: {OUTPUT_FILE}")
    print(f"  Papers: {len(papers)}")
    print(f"  Errors: {len(errors)}")


if __name__ == "__main__":
    main()
