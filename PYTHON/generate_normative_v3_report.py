#!/usr/bin/env python3
"""
Generate Normative Ethics Benchmarks V3 Report (Vault-Wide)

Combines results from two deep-reading rounds:
  - Round 1 (R1): 657 original papers → 20 Yes + 11 Borderline = 31 papers
  - Round 2 (R2): 266 EXSR papers   →  7 Yes + 38 Borderline = 45 papers

After deduplication (3 papers in both batches), yields 73 unique papers.

Output: STATISTICS/normative-ethics-benchmarks-v3-report.md

Read-only — does NOT modify any YAML frontmatter.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import date

# ---------------------------------------------------------------------------
# Config imports
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from config import LOGS_DIR, STATISTICS_DIR, PAPERS_DIR
from yaml_utils import extract_frontmatter, parse_frontmatter

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
R1_REPORT = STATISTICS_DIR / "normative-ethics-benchmarks-report.md"
R2_JSON = LOGS_DIR / "normative_v2_decisions.json"
OUTPUT = STATISTICS_DIR / "normative-ethics-benchmarks-v3-report.md"

# ---------------------------------------------------------------------------
# Known duplicates: (R1 filename, R2 filename, resolution)
# ---------------------------------------------------------------------------
DUPLICATES = [
    {
        "r1": "2025-Takeshita-JETHICS.md",
        "r2": "2025-Takeshita-JETHICS - Japanese Ethics Understanding Evaluation Dataset.md",
        "keep": "R1",
        "r1_decision": "Yes",
        "r2_decision": "Yes",
        "note": "Same arXiv paper; R1 has shorter filename. Both classified Yes.",
    },
    {
        "r1": "2024-Agarwal-Ethical Reasoning Depends on Language.md",
        "r2": "2024-Agarwal-Ethical Reasoning and Moral Value Alignment Multilingual.md",
        "keep": "R1",
        "r1_decision": "Yes",
        "r2_decision": "Yes",
        "note": "Same arXiv paper (2404.18460); different title truncation. Both Yes.",
    },
    {
        "r1": "2025-Jiao-LLM Ethics Benchmark.md",
        "r2": "2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment.md",
        "keep": "R1",
        "r1_decision": "Yes",
        "r2_decision": "Borderline",
        "note": "Same paper; R1 classified Yes, R2 Borderline. Keeping R1 Yes (deeper R1 analysis).",
    },
]

# R2 filenames to exclude (duplicates)
R2_DUP_FILENAMES = {d["r2"] for d in DUPLICATES}

# ---------------------------------------------------------------------------
# R1 Tier 2 hardcoded details (table only has File + Caveat)
# ---------------------------------------------------------------------------
TIER2_DETAILS = {
    "2025-Jiao-LLM Ethics Benchmark.md": {
        "normative_frameworks": "Consequentialist vs. Deontological (moral dilemmas component), MFQ, WVS",
        "data_artifact": "Three-dimensional ethics assessment (MFQ-30 + WVS + moral dilemmas)",
        "llms_tested": "GPT-4o and others",
    },
    "2024-Ji-MoralBench.md": {
        "normative_frameworks": "Normative framework embedded (moral scenarios)",
        "data_artifact": "MoralBench dataset",
        "llms_tested": "Multiple LLMs",
    },
    "2024-Garcia-The Moral Turing Test.md": {
        "normative_frameworks": "Utilitarian (referenced)",
        "data_artifact": "Moral Turing Test scenario set",
        "llms_tested": "LLMs vs. humans",
    },
    "2024-Liu-Evaluating Moral Beliefs across LLMs through a.md": {
        "normative_frameworks": "Deontological through Chinese cultural lens",
        "data_artifact": "Moral beliefs evaluation dataset",
        "llms_tested": "Multiple LLMs",
    },
    "2024-Yu-CMoralEval.md": {
        "normative_frameworks": "Normative ethics (culturally framed)",
        "data_artifact": "CMoralEval (30K+ dataset)",
        "llms_tested": "Chinese and multilingual LLMs",
    },
}

# ---------------------------------------------------------------------------
# Framework keyword matching
# ---------------------------------------------------------------------------
FRAMEWORK_KEYWORDS = {
    "Deontological": [
        r"deontolog", r"\bKantian\b", r"\bKant\b", r"duty-based",
        r"\bduties\b", r"categorical imperative",
    ],
    "Utilitarian / Consequentialist": [
        r"utilitar", r"consequential", r"greatest good",
    ],
    "Virtue Ethics": [
        r"virtue ethics", r"eudaimonia", r"flourishing", r"phronesis",
        r"Confucian virtue",
    ],
    "Care Ethics": [r"care ethics"],
    "Rights-Based": [r"rights-based", r"rights based", r"animal rights"],
    "Justice / Rawlsian": [
        r"\bjustice\b", r"Rawls", r"contractualis",
    ],
    "Bioethics / Principlism": [
        r"bioethics", r"principlis", r"beneficence", r"non-maleficence",
        r"autonomy.*ethics", r"medical ethics",
    ],
    "Confucian": [r"Confucian", r"Analects", r"dharma"],
    "Common Morality (Gert)": [r"\bGert\b", r"common morality"],
}


def match_frameworks(text: str) -> list[str]:
    """Return list of framework names that match keywords in `text`."""
    matched = []
    for fw_name, patterns in FRAMEWORK_KEYWORDS.items():
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                matched.append(fw_name)
                break
    return matched


# ---------------------------------------------------------------------------
# Parse R1 report markdown
# ---------------------------------------------------------------------------
def parse_r1_report(path: Path) -> list[dict]:
    """Extract all papers from the R1 markdown report."""
    text = path.read_text(encoding="utf-8")
    papers = []

    # --- Tier 1: | # | File | Frameworks | Artifact | LLMs |
    tier1_pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|",
        re.MULTILINE,
    )
    # Find Tier 1 section
    tier1_start = text.find("### Tier 1: Strong Matches")
    tier2_start = text.find("### Tier 2: Qualifying with Caveats")
    if tier1_start >= 0 and tier2_start >= 0:
        tier1_section = text[tier1_start:tier2_start]
        for m in tier1_pattern.finditer(tier1_section):
            fname = m.group(2).strip()
            frameworks = m.group(3).strip()
            artifact = m.group(4).strip()
            llms = m.group(5).strip()
            papers.append({
                "filename": fname,
                "decision": "Yes",
                "source": "R1",
                "tier": "Tier 1",
                "normative_frameworks": frameworks,
                "data_artifact": artifact,
                "llms_tested": llms,
                "reasoning": f"Operationalizes {frameworks} via {artifact}, tested on {llms}.",
            })

    # --- Tier 2: | # | File | Caveat |
    tier2_pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|",
        re.MULTILINE,
    )
    borderline_start = text.find("## Section 2: Borderline Papers")
    if tier2_start >= 0 and borderline_start >= 0:
        tier2_section = text[tier2_start:borderline_start]
        for m in tier2_pattern.finditer(tier2_section):
            fname = m.group(2).strip()
            caveat = m.group(3).strip()
            # Skip header rows
            if fname.startswith("File") or fname.startswith("---"):
                continue
            details = TIER2_DETAILS.get(fname, {})
            papers.append({
                "filename": fname,
                "decision": "Yes",
                "source": "R1",
                "tier": "Tier 2",
                "normative_frameworks": details.get("normative_frameworks", "See caveat"),
                "data_artifact": details.get("data_artifact", "See caveat"),
                "llms_tested": details.get("llms_tested", "See caveat"),
                "reasoning": f"Qualifying with caveat: {caveat}",
            })

    # --- Borderline: | # | File | Why Borderline |
    borderline_pattern = re.compile(
        r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\|",
        re.MULTILINE,
    )
    section3_end = text.find("## Section 3: Exclusion Patterns")
    if borderline_start >= 0:
        end_pos = section3_end if section3_end >= 0 else len(text)
        borderline_section = text[borderline_start:end_pos]
        for m in borderline_pattern.finditer(borderline_section):
            fname = m.group(2).strip()
            why = m.group(3).strip()
            if fname.startswith("File") or fname.startswith("---"):
                continue
            papers.append({
                "filename": fname,
                "decision": "Borderline",
                "source": "R1",
                "tier": "Borderline",
                "normative_frameworks": "",
                "data_artifact": "",
                "llms_tested": "",
                "reasoning": why,
            })

    return papers


# ---------------------------------------------------------------------------
# Load R2 JSON
# ---------------------------------------------------------------------------
def load_r2_json(path: Path) -> list[dict]:
    """Load R2 decisions and tag with source."""
    with open(path, encoding="utf-8") as f:
        entries = json.load(f)
    for e in entries:
        e["source"] = "R2"
        e["tier"] = ""
    return entries


# ---------------------------------------------------------------------------
# Deduplicate
# ---------------------------------------------------------------------------
def deduplicate(r1_papers: list[dict], r2_papers: list[dict]) -> list[dict]:
    """Merge R1 and R2, removing known duplicates from R2."""
    combined = list(r1_papers)
    for p in r2_papers:
        if p["filename"] not in R2_DUP_FILENAMES:
            combined.append(p)
    return combined


# ---------------------------------------------------------------------------
# Wiki link helper
# ---------------------------------------------------------------------------
def wiki_link(filename: str) -> str:
    """Convert 'foo.md' → '[[foo]]'."""
    name = filename
    if name.endswith(".md"):
        name = name[:-3]
    return f"[[{name}]]"


# ---------------------------------------------------------------------------
# Escape pipe for markdown tables
# ---------------------------------------------------------------------------
def esc(text: str) -> str:
    """Escape pipe characters and trim for safe markdown table cell."""
    if not text:
        return ""
    return text.replace("|", "\\|").strip()


# ---------------------------------------------------------------------------
# Strip Obsidian wiki-link brackets from author strings
# ---------------------------------------------------------------------------
def strip_wiki_links(text: str) -> str:
    """Remove [[ and ]] from Obsidian wiki-link formatted strings."""
    return text.replace("[[", "").replace("]]", "")


# ---------------------------------------------------------------------------
# Generate appendix with per-paper metadata from YAML frontmatter
# ---------------------------------------------------------------------------
def generate_appendix(papers: list[dict]) -> str:
    """Build an appendix section with author, year, abstract, and URL for each paper.

    Reads each paper's .md file from PAPERS_DIR (read-only).
    Papers are sorted: Yes first, then Borderline, alphabetically within each group.
    """
    yes_papers = sorted(
        [p for p in papers if p["decision"] == "Yes"],
        key=lambda p: p["filename"],
    )
    borderline_papers = sorted(
        [p for p in papers if p["decision"] == "Borderline"],
        key=lambda p: p["filename"],
    )
    ordered = yes_papers + borderline_papers

    lines = []
    lines.append("## Appendix: Paper Details")
    lines.append("")
    lines.append(f"Metadata for all {len(ordered)} papers, extracted from YAML frontmatter.")
    lines.append("Yes papers listed first, then Borderline, alphabetically within each group.")
    lines.append("")

    for idx, p in enumerate(ordered, 1):
        fname = p["filename"]
        paper_path = PAPERS_DIR / fname
        title = fname[:-3] if fname.endswith(".md") else fname
        wlink = wiki_link(fname)

        # Defaults
        authors = "*(Authors not available)*"
        year = "*(Year not available)*"
        abstract = "*(Abstract not available)*"
        url_line = "*(URL not available)*"

        if paper_path.exists():
            try:
                content = paper_path.read_text(encoding="utf-8")
                fm_text, _ = extract_frontmatter(content)
                fm = parse_frontmatter(fm_text)

                if fm.get("authors"):
                    authors = strip_wiki_links(fm["authors"])
                if fm.get("year"):
                    year = fm["year"]
                if fm.get("abstract"):
                    abstract = fm["abstract"]
                if fm.get("url"):
                    raw_url = fm["url"]
                    url_line = f"[{raw_url}]({raw_url})"
            except (ValueError, OSError) as exc:
                # If we can't parse, fall through to defaults
                print(f"  Warning: Could not read metadata for {fname}: {exc}")

        decision_tag = p["decision"]
        lines.append(f"### {idx}. {wlink} ({decision_tag})")
        lines.append("")
        lines.append(f"- **Authors:** {authors}")
        lines.append(f"- **Year:** {year}")
        lines.append(f"- **Abstract:** {abstract}")
        lines.append(f"- **URL:** {url_line}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Generate the report
# ---------------------------------------------------------------------------
def generate_report(papers: list[dict], r2_raw_yes: int, r2_raw_bl: int) -> str:
    """Build the full V3 report markdown string.

    Args:
        papers: Deduplicated combined paper list.
        r2_raw_yes: Raw R2 Yes count before dedup (for statistics table).
        r2_raw_bl: Raw R2 Borderline count before dedup (for statistics table).
    """
    today = date.today().isoformat()

    yes_papers = [p for p in papers if p["decision"] == "Yes"]
    borderline_papers = [p for p in papers if p["decision"] == "Borderline"]
    yes_papers.sort(key=lambda p: p["filename"])
    borderline_papers.sort(key=lambda p: p["filename"])

    r1_yes = [p for p in yes_papers if p["source"] == "R1"]
    r1_bl = [p for p in borderline_papers if p["source"] == "R1"]

    # Framework statistics
    fw_counts_yes = defaultdict(int)
    fw_counts_bl = defaultdict(int)
    paper_fw_map = {}  # filename → set of frameworks

    for p in papers:
        fw_text = p.get("normative_frameworks", "") + " " + p.get("reasoning", "")
        fws = match_frameworks(fw_text)
        paper_fw_map[p["filename"]] = set(fws)
        bucket = fw_counts_yes if p["decision"] == "Yes" else fw_counts_bl
        for fw in fws:
            bucket[fw] += 1

    # Multi-framework counts
    multi_fw = defaultdict(int)
    for fname, fws in paper_fw_map.items():
        n = len(fws)
        if n >= 1:
            multi_fw[f"{n} framework(s)"] += 1

    # Venn overlaps for the big 3
    d_set = {f for f, fws in paper_fw_map.items() if "Deontological" in fws}
    u_set = {f for f, fws in paper_fw_map.items() if "Utilitarian / Consequentialist" in fws}
    v_set = {f for f, fws in paper_fw_map.items() if "Virtue Ethics" in fws}

    lines = []

    def L(s=""):
        lines.append(s)

    # ===== HEADER =====
    L("# Normative Ethics + LLM Benchmark Report (V3 — Vault-Wide)")
    L()
    L(f"**Generated:** {today}")
    L(f"**Scope:** Full vault — 923 papers (657 original + 266 EXSR import)")
    L(f"**YAML field:** `normative_ethics_benchmark` (values: Yes, Borderline)")
    L()
    L("---")
    L()

    # ===== METHODOLOGY =====
    L("## Methodology")
    L()
    L("### Qualifying Criteria (3-Condition Rubric)")
    L()
    L("A paper qualifies as **Yes** if it meets ALL three conditions:")
    L("1. **Normative ethics**: Explicitly references or operationalizes at least one normative ethical framework (deontological, utilitarian, virtue, care ethics, rights-based, Rawlsian, bioethics/principlism)")
    L("2. **Benchmark/dataset**: Creates, uses, or adapts a structured evaluation artifact (dataset, benchmark, test suite, scenario set)")
    L("3. **LLM testing**: Evaluates one or more large language models using the benchmark")
    L()
    L("A paper is **Borderline** if it meets most criteria but has a notable gap (e.g., implicit rather than explicit normative framing, no released dataset, or primarily a method paper that includes evaluation).")
    L()
    L("### Round 1 (Original 657 Papers)")
    L()
    L("- ~80 candidate papers deep-read individually across multiple keyword search rounds")
    L("- Existing YAML classification tags NOT trusted — each paper read directly")
    L("- Result: **20 Yes + 11 Borderline = 31 papers**")
    L()
    L("### Round 2 (EXSR 266 Papers — 10-Agent Full Deep-Read)")
    L()
    L("- All 266 papers deep-read (no keyword pre-screening)")
    L("- 10 agents in 2 waves of 5, each reading ~27 papers with full PDF extracts")
    L("- Result: **7 Yes + 38 Borderline = 45 papers**")
    L()
    L("### Deduplication")
    L()
    L("3 papers appeared in both rounds (same arXiv paper imported under different filenames). R1 version kept in all cases. See [Duplicate Resolution Notes](#duplicate-resolution-notes) for details.")
    L()
    L("---")
    L()

    # ===== SUMMARY STATISTICS =====
    L("## Summary Statistics")
    L()
    r1_total = len(r1_yes) + len(r1_bl)
    r2_raw_total = r2_raw_yes + r2_raw_bl
    dup_yes = len(r1_yes) + r2_raw_yes - len(yes_papers)
    dup_bl = len(r1_bl) + r2_raw_bl - len(borderline_papers)
    dup_total = dup_yes + dup_bl
    L("| Category | R1 (657 papers) | R2 (266 papers) | Dups Removed | **Combined** |")
    L("|----------|----------------:|----------------:|------------:|-------------:|")
    L(f"| Yes | {len(r1_yes)} | {r2_raw_yes} | {dup_yes} | **{len(yes_papers)}** |")
    L(f"| Borderline | {len(r1_bl)} | {r2_raw_bl} | {dup_bl} | **{len(borderline_papers)}** |")
    L(f"| **Total** | **{r1_total}** | **{r2_raw_total}** | **{dup_total}** | **{len(papers)}** |")
    L()
    L(f"- **Papers reviewed:** ~80 (R1) + 266 (R2) = ~346 deep-reads")
    L(f"- **Overall identification rate:** {len(papers)} / 923 = {len(papers)/923*100:.1f}%")
    L()
    L("---")
    L()

    # ===== SECTION 1: YES PAPERS =====
    L(f"## Section 1: Confirmed Papers ({len(yes_papers)} — Yes)")
    L()
    L("| # | Paper | Source | Frameworks | Data Artifact | LLMs | Rationale |")
    L("|---|-------|--------|------------|---------------|------|-----------|")
    for i, p in enumerate(yes_papers, 1):
        link = wiki_link(p["filename"])
        L(f"| {i} | {link} | {p['source']} | {esc(p.get('normative_frameworks',''))} | {esc(p.get('data_artifact',''))} | {esc(p.get('llms_tested',''))} | {esc(p.get('reasoning',''))} |")
    L()
    L("---")
    L()

    # ===== SECTION 2: BORDERLINE PAPERS =====
    L(f"## Section 2: Borderline Papers ({len(borderline_papers)})")
    L()
    L("| # | Paper | Source | Frameworks | Rationale (Why Borderline) |")
    L("|---|-------|--------|------------|---------------------------|")
    for i, p in enumerate(borderline_papers, 1):
        link = wiki_link(p["filename"])
        fw = esc(p.get("normative_frameworks", ""))
        L(f"| {i} | {link} | {p['source']} | {fw} | {esc(p.get('reasoning',''))} |")
    L()
    L("---")
    L()

    # ===== FRAMEWORK DEEP DIVES =====
    def framework_deep_dive(title: str, fw_name: str, element_label: str):
        """Generate a framework deep-dive section."""
        matching = []
        for p in papers:
            if fw_name in paper_fw_map.get(p["filename"], set()):
                matching.append(p)
        matching.sort(key=lambda p: (0 if p["decision"] == "Yes" else 1, p["filename"]))

        L(f"## Framework Deep Dive: {title}")
        L()
        if not matching:
            L("_No papers matched this framework._")
            L()
            return
        L(f"| # | Paper | Decision | {element_label} | Rationale |")
        L("|---|-------|----------|" + "-" * (len(element_label) + 2) + "|-----------|")
        for i, p in enumerate(matching, 1):
            link = wiki_link(p["filename"])
            fw_text = esc(p.get("normative_frameworks", ""))
            L(f"| {i} | {link} | {p['decision']} | {fw_text} | {esc(p.get('reasoning',''))} |")
        L()
        L("---")
        L()

    framework_deep_dive(
        "Deontological Ethics", "Deontological",
        "Specific Deontological Element",
    )
    framework_deep_dive(
        "Consequentialist / Utilitarian Ethics",
        "Utilitarian / Consequentialist",
        "Specific Utilitarian Element",
    )
    framework_deep_dive(
        "Virtue Ethics", "Virtue Ethics",
        "Specific Virtue Ethics Element",
    )

    # ===== FRAMEWORK DISTRIBUTION SUMMARY =====
    L("## Framework Distribution Summary")
    L()
    L("### Counts per Framework")
    L()
    all_fw_names = sorted(set(list(fw_counts_yes.keys()) + list(fw_counts_bl.keys())))
    L("| Framework | Yes | Borderline | Total |")
    L("|-----------|----:|-----------:|------:|")
    for fw in all_fw_names:
        y = fw_counts_yes.get(fw, 0)
        b = fw_counts_bl.get(fw, 0)
        L(f"| {fw} | {y} | {b} | {y+b} |")
    L()

    L("### Multi-Framework Coverage per Paper")
    L()
    L("| # Frameworks | Paper Count |")
    L("|-------------:|------------:|")
    for k in sorted(multi_fw.keys()):
        L(f"| {k} | {multi_fw[k]} |")
    # Papers with 0 frameworks matched
    zero_fw = sum(1 for fws in paper_fw_map.values() if len(fws) == 0)
    if zero_fw:
        L(f"| 0 framework(s) | {zero_fw} |")
    L()

    L("### Overlap Among Top-3 Frameworks (Deontological / Utilitarian / Virtue)")
    L()
    L("| Combination | Count |")
    L("|-------------|------:|")
    L(f"| Deontological only | {len(d_set - u_set - v_set)} |")
    L(f"| Utilitarian only | {len(u_set - d_set - v_set)} |")
    L(f"| Virtue only | {len(v_set - d_set - u_set)} |")
    L(f"| D + U (not V) | {len((d_set & u_set) - v_set)} |")
    L(f"| D + V (not U) | {len((d_set & v_set) - u_set)} |")
    L(f"| U + V (not D) | {len((u_set & v_set) - d_set)} |")
    L(f"| D + U + V | {len(d_set & u_set & v_set)} |")
    L(f"| None of D/U/V | {len(set(paper_fw_map.keys()) - d_set - u_set - v_set)} |")
    L()
    L("---")
    L()

    # ===== DUPLICATE RESOLUTION NOTES =====
    L("## Duplicate Resolution Notes")
    L()
    L("3 papers appeared in both Round 1 and Round 2 (same arXiv paper imported under different filenames).")
    L()
    L("| # | R1 Filename | R2 Filename | R1 Decision | R2 Decision | Resolution |")
    L("|---|-------------|-------------|-------------|-------------|------------|")
    for i, d in enumerate(DUPLICATES, 1):
        L(f"| {i} | `{d['r1']}` | `{d['r2']}` | {d['r1_decision']} | {d['r2_decision']} | {d['note']} |")
    L()
    L("In all cases the R1 version (shorter filename, from the original 657-paper batch) is kept as the canonical entry.")
    L()
    L("---")
    L()

    # ===== APPENDIX =====
    appendix = generate_appendix(papers)
    L(appendix)
    L()
    L("---")
    L()
    L("*Report generated by `PYTHON/generate_normative_v3_report.py`*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Loading R1 report: {R1_REPORT}")
    r1_papers = parse_r1_report(R1_REPORT)
    r1_yes = sum(1 for p in r1_papers if p["decision"] == "Yes")
    r1_bl = sum(1 for p in r1_papers if p["decision"] == "Borderline")
    print(f"  R1: {r1_yes} Yes + {r1_bl} Borderline = {len(r1_papers)} papers")

    print(f"Loading R2 JSON:   {R2_JSON}")
    r2_papers = load_r2_json(R2_JSON)
    r2_yes = sum(1 for p in r2_papers if p["decision"] == "Yes")
    r2_bl = sum(1 for p in r2_papers if p["decision"] == "Borderline")
    print(f"  R2: {r2_yes} Yes + {r2_bl} Borderline = {len(r2_papers)} papers")

    print("Deduplicating (3 known duplicates)...")
    combined = deduplicate(r1_papers, r2_papers)
    c_yes = sum(1 for p in combined if p["decision"] == "Yes")
    c_bl = sum(1 for p in combined if p["decision"] == "Borderline")
    print(f"  Combined: {c_yes} Yes + {c_bl} Borderline = {len(combined)} papers")

    # Sanity check
    if c_yes != 25 or c_bl != 48 or len(combined) != 73:
        print(f"  WARNING: Expected 25 Yes + 48 Borderline = 73, got {c_yes} + {c_bl} = {len(combined)}")

    print(f"Generating report → {OUTPUT}")
    report = generate_report(combined, r2_raw_yes=r2_yes, r2_raw_bl=r2_bl)
    OUTPUT.write_text(report, encoding="utf-8")
    print(f"Done. Report written ({len(report):,} chars, {report.count(chr(10)):,} lines).")


if __name__ == "__main__":
    main()
