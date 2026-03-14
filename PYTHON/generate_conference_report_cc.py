#!/usr/bin/env python3
"""
Conference Representation Report — Analyze CONF-CC field across all vault papers.

Reads paper YAML frontmatter to produce a comprehensive 10-section Markdown report
analyzing conference/venue representation: which venues dominate, temporal trends,
ethics correlations, journal vs conference breakdown, and more.

Data sources:
  - papers/*.md YAML frontmatter: CONF-CC, ethics_overall, year fields
  - logs/20260220-conference_classification_cc.json: Phase attribution stats

Output: STATISTICS/20260220-conference-representation-report.md
"""

import re
import json
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
LOGS_DIR = WS_ROOT / "logs"
STATS_DIR = WS_ROOT / "STATISTICS"
OUTPUT_FILE = STATS_DIR / "20260220-conference-representation-report.md"
PHASE_LOG = LOGS_DIR / "20260220-conference_classification_cc.json"

# ── Import journal dictionaries from classification script ─────────────────
sys.path.insert(0, str(SCRIPT_DIR))
from ethics_scoring import is_ethics_yes, parse_ethics_value
from add_conference_field_cc import JOURNAL_EXACT, JOURNAL_SUBSTRING

# Build known journals set from classification script dictionaries
KNOWN_JOURNALS = set(JOURNAL_EXACT.values()) | set(JOURNAL_SUBSTRING.values())
# Remove N/A (mapped from bare "findings" key in JOURNAL_EXACT)
KNOWN_JOURNALS.discard("N/A")

# Additional journals observed in CONF-CC data (from OpenAlex/Semantic Scholar)
# that aren't in the classification dicts
KNOWN_JOURNALS |= {
    "Social Network Analysis and Mining",
    "International Journal of Social Robotics",
    "Ethics & Behavior",
    "Computational Linguistics",
    "MDPI Applied Sciences",
    "Data",
    "Behavior Research Methods",
    "Psychological Bulletin",
    "Scientific Data",
    "Semantic Web",
    "Communications of the ACM",
    "Data Science Journal",
    "Social Psychological and Personality Science",
    "Multimodal Technologies and Interaction",
    "Digital Society",
    "TMLR",
    "TACL",
    "Electronics",
    "Information",
    "Bioengineering",
    "Nursing Ethics",
    "Wellcome Open Research",
    "Analytics",
    "Emerging Media",
    "Theology and Science",
    "Acta Borealia",
    "Verbum et Ecclesia",
    "Somatechnics",
    "Discover Education",
    "Discover Data",
    "Forum Philosophicum",
    "Royal Society Open Science",
    "Cluster Computing",
    "Complex & Intelligent Systems",
    "Neural Computing and Applications",
    "American Philosophical Quarterly",
    "Developing World Bioethics",
    "BMC Medical Education",
    "Business & Society",
    "Expert Systems with Applications",
    "Policy Design and Practice",
    "Moral Philosophy and Politics",
    "Personality and Social Psychology Bulletin",
    "npj Digital Medicine",
    "JMIR Mental Health",
    "Healthcare Management Forum",
    "Theory and Research in Education",
    "Frontiers in Human Neuroscience",
    "Preservation Digital Technology & Culture",
    "Korea Science (Informatization Policy)",
    "Disputatio philosophica",
    "Frontiers in Artificial Intelligence",
    "ScienceDirect (Heliyon)",
}


# ═══════════════════════════════════════════════════════════════════════════
# CATEGORIZATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

def categorize_venue(conf_cc: str) -> str:
    """Categorize a CONF-CC value into one of 6 high-level categories.

    Returns one of: "Preprint", "N/A", "Findings", "Workshop", "Journal", "Conference"
    """
    if conf_cc == "Preprint":
        return "Preprint"
    if conf_cc == "N/A":
        return "N/A"
    low = conf_cc.lower()
    # Findings track
    if "findings" in low:
        return "Findings"
    # Workshop, Demo, Shared Task
    if any(kw in low for kw in ("workshop", "demo", "shared task")):
        return "Workshop"
    # Known journals — exact match
    if conf_cc in KNOWN_JOURNALS:
        return "Journal"
    # Known journals — match after stripping year suffix
    no_year = re.sub(r'\s+\d{4}\s*$', '', conf_cc).strip()
    if no_year in KNOWN_JOURNALS:
        return "Journal"
    # Heuristic: "Journal" or "Transactions" in name (but not if "Conference" also present)
    if ("journal" in low or "transactions" in low) and "conference" not in low:
        return "Journal"
    # Default: Conference (includes named conferences, LNCS series, etc.)
    return "Conference"


def extract_conference_family(conf_cc: str) -> str:
    """Extract conference family name from CONF-CC value.

    "ACL 2025" → "ACL"
    "EMNLP 2024 Findings" → "EMNLP"
    "NeurIPS 2023 Workshop" → "NeurIPS"
    "Workshop (2025)" → None
    "Preprint" → None
    """
    if conf_cc in ("Preprint", "N/A"):
        return ""
    # Skip generic workshops/shared tasks
    if conf_cc.startswith("Workshop") or conf_cc.startswith("Shared Task"):
        return ""
    # Strip known track suffixes
    name = re.sub(r'\s+(Findings|Workshop|Demo|D&B|SRW)\s*$', '', conf_cc)
    # Strip year
    name = re.sub(r'\s+\d{4}\s*$', '', name).strip()
    return name if name else ""


def make_ascii_bar(count: int, max_count: int, width: int = 40) -> str:
    """Create an inline ASCII bar chart."""
    if max_count <= 0:
        return ""
    bar_len = int(count / max_count * width)
    return "█" * bar_len


def make_wikilink(filename: str) -> str:
    """Convert a paper filename to an Obsidian wikilink.

    "2025-Doe-Paper Title.md" → "[[2025-Doe-Paper Title]]"
    """
    stem = filename[:-3] if filename.endswith(".md") else filename
    return f"[[{stem}]]"


# ═══════════════════════════════════════════════════════════════════════════
# PAPER SCANNER
# ═══════════════════════════════════════════════════════════════════════════

def scan_papers():
    """Scan all papers for CONF-CC, ethics_overall, year, publication, type fields.

    Returns list of dicts: {filename, year, conf_cc, ethics_overall, category, publication, type}
    """
    papers = []
    for p in sorted(PAPERS_DIR.iterdir()):
        if p.suffix != '.md':
            continue
        try:
            content = p.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        # Extract fields
        def get(key):
            m = re.search(rf'^{re.escape(key)}:\s*"?(.+?)"?\s*$', fm, re.MULTILINE)
            return m.group(1).strip() if m else ""

        conf_cc = get('CONF-CC') or "N/A"
        ethics_raw = get('ethics_overall') or ""
        ethics = "Yes" if is_ethics_yes(ethics_raw) else "No"
        year_str = get('year')
        year = int(year_str) if year_str and year_str.isdigit() else 0
        pub = get('publication')
        paper_type = get('type')

        papers.append({
            "filename": p.name,
            "year": year,
            "conf_cc": conf_cc,
            "ethics_overall": ethics,
            "category": categorize_venue(conf_cc),
            "publication": pub,
            "type": paper_type,
        })

    return papers


# ═══════════════════════════════════════════════════════════════════════════
# REPORT GENERATION
# ═══════════════════════════════════════════════════════════════════════════

def generate_report(papers: list, phase_data: dict) -> str:
    """Generate the full 10-section Markdown report."""
    total = len(papers)
    L = []

    # Pre-compute frequently used data
    conf_cc_counter = Counter(p["conf_cc"] for p in papers)
    category_counter = Counter(p["category"] for p in papers)
    year_counter = Counter(p["year"] for p in papers if p["year"] > 0)
    unique_venues = len(conf_cc_counter)

    # ── Header ──────────────────────────────────────────────────────────
    L.append("# Conference & Venue Representation Report")
    L.append("")
    L.append(f"**Generated:** 2026-02-20 | **Papers:** {total:,} | "
             f"**Unique venues:** {unique_venues} | "
             f"**CONF-CC coverage:** 100%")
    L.append("")
    L.append("---")
    L.append("")

    # ── Table of Contents ────────────────────────────────────────────────
    L.append("## Table of Contents")
    L.append("")
    toc_items = [
        "1. Executive Summary",
        "2. High-Level Category Breakdown",
        "3. Top 30 Venues",
        "4. Conference Family Analysis",
        "5. Temporal Analysis",
        "6. Conference x Year Heatmap",
        "7. Journal Landscape",
        "8. Ethics Correlation",
        "9. Classification Methodology",
        "10. Appendix: Full Venue List",
    ]
    for item in toc_items:
        anchor = item.lower().replace(" ", "-").replace(":", "").replace(",", "")
        L.append(f"- [{item}](#{anchor})")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 1. EXECUTIVE SUMMARY
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 1. Executive Summary")
    L.append("")

    preprint_count = category_counter.get("Preprint", 0)
    conf_count = category_counter.get("Conference", 0)
    journal_count = category_counter.get("Journal", 0)
    na_count = category_counter.get("N/A", 0)
    workshop_count = category_counter.get("Workshop", 0)
    findings_count = category_counter.get("Findings", 0)

    preprint_pct = preprint_count * 100 / total
    conf_pct = conf_count * 100 / total

    # Top conference
    conf_papers = [p for p in papers if p["category"] == "Conference"]
    top_conf_venues = Counter(p["conf_cc"] for p in conf_papers).most_common(3)
    top_conf_str = ", ".join(f"{v} ({c})" for v, c in top_conf_venues)

    L.append(f"This vault contains **{total:,} papers** with normalized venue classification "
             f"(CONF-CC) across **{unique_venues} unique venues**. Key findings:")
    L.append("")
    L.append(f"- **Preprint dominance:** {preprint_count} papers ({preprint_pct:.1f}%) are preprints, "
             f"reflecting the field's reliance on arXiv for rapid dissemination")
    L.append(f"- **Conference papers:** {conf_count} papers ({conf_pct:.1f}%) published at peer-reviewed "
             f"conferences — top venues: {top_conf_str}")
    L.append(f"- **Journal articles:** {journal_count} papers ({journal_count*100/total:.1f}%) across "
             f"{len(set(p['conf_cc'] for p in papers if p['category'] == 'Journal'))} unique journals")
    L.append(f"- **Findings tracks:** {findings_count} papers in ACL/EMNLP/NAACL Findings")
    L.append(f"- **Workshops:** {workshop_count} papers at workshop/demo/shared-task venues")
    L.append(f"- **Unclassified (N/A):** {na_count} papers ({na_count*100/total:.1f}%) where no venue "
             f"could be determined")
    L.append("")

    L.append("### Summary Table")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Total papers | {total:,} |")
    L.append(f"| Unique CONF-CC values | {unique_venues} |")
    L.append(f"| Conference papers | {conf_count} ({conf_pct:.1f}%) |")
    L.append(f"| Preprints | {preprint_count} ({preprint_pct:.1f}%) |")
    L.append(f"| Journal articles | {journal_count} ({journal_count*100/total:.1f}%) |")
    L.append(f"| Findings track | {findings_count} ({findings_count*100/total:.1f}%) |")
    L.append(f"| Workshops/Demos | {workshop_count} ({workshop_count*100/total:.1f}%) |")
    L.append(f"| N/A (unclassified) | {na_count} ({na_count*100/total:.1f}%) |")
    year_range = sorted(y for y in year_counter.keys() if y > 0)
    if year_range:
        L.append(f"| Year range | {year_range[0]}–{year_range[-1]} |")
    L.append(f"| Ethics coverage (Yes) | {sum(1 for p in papers if p['ethics_overall'] == 'Yes')} "
             f"({sum(1 for p in papers if p['ethics_overall'] == 'Yes')*100/total:.1f}%) |")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 2. HIGH-LEVEL CATEGORY BREAKDOWN
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 2. High-Level Category Breakdown")
    L.append("")
    L.append("Papers are categorized into 6 high-level types based on their CONF-CC value:")
    L.append("")
    L.append("- **Conference**: Published at a named, peer-reviewed conference (e.g., ACL 2025, NeurIPS 2024)")
    L.append("- **Preprint**: Deposited on arXiv or similar preprint server without formal peer review")
    L.append("- **Journal**: Published in a peer-reviewed journal (e.g., AI and Ethics, Nature)")
    L.append("- **Findings**: Published in ACL/EMNLP/NAACL Findings tracks (peer-reviewed but not main conference)")
    L.append("- **Workshop**: Published at conference workshops, demo tracks, or shared tasks")
    L.append("- **N/A**: Venue could not be determined from available metadata")
    L.append("")

    # Sort categories by count descending
    cat_order = ["Preprint", "Conference", "N/A", "Journal", "Findings", "Workshop"]
    max_cat_count = max(category_counter.values()) if category_counter else 1

    L.append("| Category | Count | % | Distribution |")
    L.append("|----------|------:|--:|-------------|")
    for cat in cat_order:
        count = category_counter.get(cat, 0)
        pct = count * 100 / total
        bar = make_ascii_bar(count, max_cat_count, 30)
        L.append(f"| **{cat}** | {count} | {pct:.1f}% | `{bar}` |")
    check_total = sum(category_counter.values())
    L.append(f"| **Total** | **{check_total}** | **100%** | |")
    L.append("")

    if check_total != total:
        L.append(f"> **WARNING:** Category total ({check_total}) != paper total ({total})")
        L.append("")

    # Peer-reviewed vs non-peer-reviewed summary
    peer_reviewed = conf_count + journal_count + findings_count + workshop_count
    L.append(f"**Peer-reviewed venues:** {peer_reviewed} papers ({peer_reviewed*100/total:.1f}%) — "
             f"conferences ({conf_count}), journals ({journal_count}), "
             f"findings ({findings_count}), workshops ({workshop_count})")
    L.append("")
    L.append(f"**Non-peer-reviewed / unknown:** {preprint_count + na_count} papers "
             f"({(preprint_count + na_count)*100/total:.1f}%) — "
             f"preprints ({preprint_count}), N/A ({na_count})")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 3. TOP 30 VENUES (excluding Preprint/N/A)
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 3. Top 30 Venues")
    L.append("")
    L.append("*Excluding Preprint and N/A. Includes conferences, journals, findings tracks, and workshops.*")
    L.append("")

    venue_papers = [(v, c) for v, c in conf_cc_counter.most_common()
                    if v not in ("Preprint", "N/A")]
    venue_total = sum(c for _, c in venue_papers)
    max_venue_count = venue_papers[0][1] if venue_papers else 1

    L.append(f"| # | Venue | Type | Count | % of Venues | Bar |")
    L.append("|--:|-------|------|------:|------------:|-----|")
    for i, (venue, count) in enumerate(venue_papers[:30], 1):
        cat = categorize_venue(venue)
        pct = count * 100 / venue_total
        bar = make_ascii_bar(count, max_venue_count, 25)
        L.append(f"| {i} | {venue} | {cat} | {count} | {pct:.1f}% | `{bar}` |")
    L.append("")
    L.append(f"*{len(venue_papers)} unique venues (excl. Preprint/N/A) account for "
             f"{venue_total} papers ({venue_total*100/total:.1f}% of vault).*")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 4. CONFERENCE FAMILY ANALYSIS
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 4. Conference Family Analysis")
    L.append("")
    L.append("Conference families group all editions and tracks of the same venue "
             "(e.g., ACL 2024 + ACL 2025 + ACL 2025 Findings → **ACL** family).")
    L.append("")

    # Build family mapping
    family_counter = Counter()
    family_tracks = defaultdict(lambda: Counter())  # family → {track: count}
    family_year_papers = defaultdict(lambda: defaultdict(list))  # family → year → [filename]
    for p in papers:
        if p["category"] in ("Preprint", "N/A", "Journal"):
            continue
        family = extract_conference_family(p["conf_cc"])
        if not family:
            continue
        family_counter[family] += 1
        if p["year"] > 0:
            family_year_papers[family][p["year"]].append(p["filename"])
        # Determine track
        cc = p["conf_cc"]
        if "Findings" in cc:
            track = "Findings"
        elif "Workshop" in cc:
            track = "Workshop"
        elif "Demo" in cc:
            track = "Demo"
        elif "D&B" in cc:
            track = "D&B"
        elif "SRW" in cc:
            track = "SRW"
        else:
            track = "Main"
        family_tracks[family][track] += 1

    max_family_count = family_counter.most_common(1)[0][1] if family_counter else 1

    L.append("### Top 20 Conference Families")
    L.append("")
    L.append("| # | Family | Total | Main | Findings | Workshop | Demo | D&B | Bar |")
    L.append("|--:|--------|------:|-----:|---------:|---------:|-----:|----:|-----|")
    for i, (family, count) in enumerate(family_counter.most_common(20), 1):
        tracks = family_tracks[family]
        main = tracks.get("Main", 0)
        findings = tracks.get("Findings", 0)
        workshop = tracks.get("Workshop", 0)
        demo = tracks.get("Demo", 0)
        db = tracks.get("D&B", 0)
        bar = make_ascii_bar(count, max_family_count, 25)
        L.append(f"| {i} | **{family}** | {count} | {main} | "
                 f"{findings if findings else '-'} | "
                 f"{workshop if workshop else '-'} | "
                 f"{demo if demo else '-'} | "
                 f"{db if db else '-'} | `{bar}` |")
    L.append("")

    # Concentration analysis
    top5_families = family_counter.most_common(5)
    top5_total = sum(c for _, c in top5_families)
    all_family_total = sum(family_counter.values())
    L.append(f"**Concentration:** Top 5 families ({', '.join(f[0] for f in top5_families)}) "
             f"account for {top5_total} papers ({top5_total*100/all_family_total:.0f}% of "
             f"conference/findings/workshop papers). Total families: {len(family_counter)}.")
    L.append("")

    # NLP vs general AI
    nlp_families = {"ACL", "EMNLP", "NAACL", "COLING", "EACL", "AACL",
                    "LREC", "LREC-COLING", "SemEval", "RANLP", "NoDaLiDa",
                    "PROPOR", "ICON", "ROCLING", "STIL", "EVALITA", "IberLEF",
                    "CLEF", "FIRE", "INTERSPEECH"}
    ml_families = {"NeurIPS", "ICML", "ICLR", "AAAI", "IJCAI", "COLM",
                   "ECAI", "ECML-PKDD", "CVPR", "ECCV", "ICCV", "ACCV", "BMVC"}
    ethics_families = {"AIES", "FAccT"}

    nlp_total = sum(family_counter.get(f, 0) for f in nlp_families)
    ml_total = sum(family_counter.get(f, 0) for f in ml_families)
    ethics_total = sum(family_counter.get(f, 0) for f in ethics_families)

    L.append("### Venue Ecosystem")
    L.append("")
    L.append("| Ecosystem | Families | Papers | % of Conf/WS |")
    L.append("|-----------|--------:|-------:|-------------:|")
    nlp_active = sum(1 for f in nlp_families if family_counter.get(f, 0) > 0)
    ml_active = sum(1 for f in ml_families if family_counter.get(f, 0) > 0)
    ethics_active = sum(1 for f in ethics_families if family_counter.get(f, 0) > 0)
    L.append(f"| **NLP/CL** (ACL, EMNLP, NAACL, ...) | {nlp_active} | {nlp_total} | "
             f"{nlp_total*100/all_family_total:.1f}% |")
    L.append(f"| **ML/AI** (NeurIPS, ICML, ICLR, ...) | {ml_active} | {ml_total} | "
             f"{ml_total*100/all_family_total:.1f}% |")
    L.append(f"| **AI Ethics** (AIES, FAccT) | {ethics_active} | {ethics_total} | "
             f"{ethics_total*100/all_family_total:.1f}% |")
    other_total = all_family_total - nlp_total - ml_total - ethics_total
    L.append(f"| **Other** (CHI, WWW, KDD, ...) | — | {other_total} | "
             f"{other_total*100/all_family_total:.1f}% |")
    L.append("")

    # ── Top 10 Conferences × Year cross-tab with paper links ──────────
    top10_families = [f for f, _ in family_counter.most_common(10)]
    cross_years = list(range(2022, 2027))

    L.append("### Top 10 Conferences — Papers by Year (2022–2026)")
    L.append("")

    # Part A: Summary cross-tab table
    header = "| Family | " + " | ".join(str(y) for y in cross_years) + " | Total |"
    sep = "|--------|" + "|".join("-----:" for _ in cross_years) + "|------:|"
    L.append(header)
    L.append(sep)
    for fam in top10_families:
        vals = []
        row_total = 0
        for y in cross_years:
            v = len(family_year_papers[fam].get(y, []))
            row_total += v
            vals.append(str(v) if v > 0 else "·")
        L.append(f"| **{fam}** | " + " | ".join(vals) + f" | {row_total} |")
    L.append("")

    # Part B: Per-conference paper lists with wikilinks
    for fam in top10_families:
        fam_total = family_counter[fam]
        L.append(f"#### {fam} ({fam_total} papers)")
        L.append("")
        for y in cross_years:
            plist = sorted(family_year_papers[fam].get(y, []))
            if not plist:
                continue
            links = ", ".join(make_wikilink(f) for f in plist)
            L.append(f"**{y}** ({len(plist)}): {links}")
            L.append("")
        # If no papers fell in 2022-2026 range, note it
        if not any(family_year_papers[fam].get(y, []) for y in cross_years):
            L.append("*No papers in the 2022–2026 range.*")
            L.append("")

    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 5. TEMPORAL ANALYSIS
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 5. Temporal Analysis")
    L.append("")
    L.append("Papers by publication year, broken down by venue category.")
    L.append("")

    # Year × Category cross-tabulation
    year_cat = defaultdict(lambda: Counter())
    for p in papers:
        if p["year"] > 0:
            year_cat[p["year"]][p["category"]] += 1

    all_years = sorted(y for y in year_cat.keys() if y >= 2016)
    cat_cols = ["Conference", "Preprint", "Journal", "Findings", "Workshop", "N/A"]

    L.append("### Year x Category Cross-Tabulation")
    L.append("")
    header = "| Year | " + " | ".join(cat_cols) + " | Total | Preprint % |"
    sep = "|------|" + "|".join("------:" for _ in cat_cols) + "|------:|----------:|"
    L.append(header)
    L.append(sep)

    for y in all_years:
        row_vals = [str(year_cat[y].get(c, 0)) if year_cat[y].get(c, 0) > 0 else "-"
                    for c in cat_cols]
        row_total = sum(year_cat[y].values())
        preprint_y = year_cat[y].get("Preprint", 0)
        preprint_pct_y = f"{preprint_y*100/row_total:.0f}%" if row_total > 0 else "-"
        L.append(f"| **{y}** | " + " | ".join(row_vals) + f" | {row_total} | {preprint_pct_y} |")

    # Total row
    col_totals = [sum(year_cat[y].get(c, 0) for y in all_years) for c in cat_cols]
    grand_total = sum(col_totals)
    L.append(f"| **Total** | " + " | ".join(f"**{t}**" for t in col_totals) +
             f" | **{grand_total}** | |")
    L.append("")

    # Year-over-year growth
    L.append("### Year-over-Year Growth")
    L.append("")
    L.append("| Year | Total | Conference | Preprint | Journal | Conf Growth | Pre Growth |")
    L.append("|------|------:|-----------:|---------:|--------:|------------:|-----------:|")
    prev_conf = 0
    prev_pre = 0
    for y in all_years:
        t = sum(year_cat[y].values())
        c = year_cat[y].get("Conference", 0)
        p = year_cat[y].get("Preprint", 0)
        j = year_cat[y].get("Journal", 0)
        c_growth = f"+{c - prev_conf}" if prev_conf > 0 and c >= prev_conf else (
            f"{c - prev_conf}" if prev_conf > 0 else "-")
        p_growth = f"+{p - prev_pre}" if prev_pre > 0 and p >= prev_pre else (
            f"{p - prev_pre}" if prev_pre > 0 else "-")
        L.append(f"| {y} | {t} | {c} | {p} | {j} | {c_growth} | {p_growth} |")
        prev_conf = c
        prev_pre = p
    L.append("")

    # Highlight preprint surge
    if 2018 in year_cat and 2025 in year_cat:
        pre_2018 = year_cat[2018].get("Preprint", 0)
        total_2018 = sum(year_cat[2018].values())
        pre_2025 = year_cat[2025].get("Preprint", 0)
        total_2025 = sum(year_cat[2025].values())
        if total_2018 > 0 and total_2025 > 0:
            L.append(f"**Preprint surge:** {pre_2018*100//total_2018}% of papers in 2018 → "
                     f"{pre_2025*100//total_2025}% in 2025 "
                     f"({pre_2025} preprints vs {year_cat[2025].get('Conference', 0)} conference papers)")
            L.append("")

    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 6. CONFERENCE × YEAR HEATMAP
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 6. Conference x Year Heatmap")
    L.append("")
    L.append("Top 12 conference families × publication year. Shows when each conference "
             "became prominent in the vault.")
    L.append("")

    # Build family × year matrix
    family_year = defaultdict(lambda: Counter())
    for p in papers:
        if p["year"] <= 0:
            continue
        if p["category"] in ("Preprint", "N/A", "Journal"):
            continue
        family = extract_conference_family(p["conf_cc"])
        if family:
            family_year[family][p["year"]] += 1

    top_families = [f for f, _ in family_counter.most_common(12)]
    heatmap_years = sorted(y for y in range(2018, 2027) if any(
        family_year[f].get(y, 0) > 0 for f in top_families))

    if heatmap_years:
        header = "| Family | " + " | ".join(str(y) for y in heatmap_years) + " | Total |"
        sep = "|--------|" + "|".join("----:" for _ in heatmap_years) + "|------:|"
        L.append(header)
        L.append(sep)
        for fam in top_families:
            vals = []
            row_total = 0
            for y in heatmap_years:
                v = family_year[fam].get(y, 0)
                row_total += v
                vals.append(str(v) if v > 0 else "·")
            L.append(f"| **{fam}** | " + " | ".join(vals) + f" | {row_total} |")
        L.append("")

    L.append("*Key pattern: NLP conferences (ACL, EMNLP, NAACL) dominate 2024–2025, "
             "while ML conferences (NeurIPS, ICML, ICLR) provide strong 2023–2025 coverage. "
             "AI ethics venues (AIES, FAccT) contribute consistently from 2018 onward.*")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 7. JOURNAL LANDSCAPE
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 7. Journal Landscape")
    L.append("")

    journal_papers = [p for p in papers if p["category"] == "Journal"]
    journal_counter = Counter(p["conf_cc"] for p in journal_papers)
    unique_journals = len(journal_counter)

    L.append(f"**{journal_count} papers** across **{unique_journals} unique journals**.")
    L.append("")

    max_journal_count = journal_counter.most_common(1)[0][1] if journal_counter else 1

    L.append("### Top Journals by Paper Count")
    L.append("")
    L.append("| # | Journal | Count | Bar |")
    L.append("|--:|---------|------:|-----|")
    for i, (jname, count) in enumerate(journal_counter.most_common(), 1):
        bar = make_ascii_bar(count, max_journal_count, 30)
        L.append(f"| {i} | {jname} | {count} | `{bar}` |")
    L.append("")

    # Journal discipline breakdown
    ai_ethics_journals = {"AI and Ethics", "AI & Society", "Ethics and Information Technology",
                          "Ethics & Behavior", "Nursing Ethics", "American Journal of Bioethics",
                          "Developing World Bioethics", "Moral Philosophy and Politics",
                          "Philosophy & Technology", "Minds and Machines",
                          "Philosophical Studies", "American Philosophical Quarterly",
                          "Forum Philosophicum", "Theology and Science"}
    cs_journals = {"ACM Computing Surveys", "ACM TOSEM", "ACM TIST", "ACM TALIP",
                   "IEEE Access", "IEEE TAC", "IEEE TCSS", "Computational Linguistics",
                   "Natural Language Processing", "Language Resources and Evaluation",
                   "Machine Learning", "Artificial Intelligence", "Artificial Intelligence Review",
                   "Knowledge-Based Systems", "Neurocomputing", "Neural Computing and Applications",
                   "Expert Systems with Applications", "TACL", "TMLR",
                   "Electronics", "Information", "Cluster Computing",
                   "Complex & Intelligent Systems"}
    nature_journals = {"Nature", "Nature Scientific Reports", "Nature Scientific Data",
                       "Nature Human Behaviour", "Nature Machine Intelligence",
                       "npj AI", "npj Digital Medicine", "Science", "PNAS",
                       "Royal Society Open Science"}

    ai_ethics_count = sum(journal_counter.get(j, 0) for j in ai_ethics_journals)
    cs_count = sum(journal_counter.get(j, 0) for j in cs_journals)
    nature_count = sum(journal_counter.get(j, 0) for j in nature_journals)
    other_j = journal_count - ai_ethics_count - cs_count - nature_count

    L.append("### Journal Discipline Breakdown")
    L.append("")
    L.append("| Discipline | Papers | % of Journals | Key Venues |")
    L.append("|------------|-------:|--------------:|------------|")
    top_ae = ", ".join(f"{j} ({journal_counter[j]})" for j in sorted(
        ai_ethics_journals, key=lambda j: -journal_counter.get(j, 0))[:3]
        if journal_counter.get(j, 0) > 0)
    top_cs = ", ".join(f"{j} ({journal_counter[j]})" for j in sorted(
        cs_journals, key=lambda j: -journal_counter.get(j, 0))[:3]
        if journal_counter.get(j, 0) > 0)
    top_nat = ", ".join(f"{j} ({journal_counter[j]})" for j in sorted(
        nature_journals, key=lambda j: -journal_counter.get(j, 0))[:3]
        if journal_counter.get(j, 0) > 0)
    L.append(f"| AI Ethics & Philosophy | {ai_ethics_count} | "
             f"{ai_ethics_count*100/journal_count:.0f}% | {top_ae} |")
    L.append(f"| Computer Science / AI | {cs_count} | "
             f"{cs_count*100/journal_count:.0f}% | {top_cs} |")
    L.append(f"| High-Impact Science | {nature_count} | "
             f"{nature_count*100/journal_count:.0f}% | {top_nat} |")
    L.append(f"| Other / Interdisciplinary | {other_j} | "
             f"{other_j*100/journal_count:.0f}% | Various |")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 8. ETHICS CORRELATION
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 8. Ethics Correlation")
    L.append("")
    L.append("Cross-tabulation of `ethics_overall` field × venue category. Shows which "
             "venue types have higher ethics relevance rates.")
    L.append("")

    # Ethics × Category
    ethics_cat = defaultdict(lambda: Counter())
    for p in papers:
        eth = p["ethics_overall"] or "Unknown"
        ethics_cat[p["category"]][eth] += 1

    L.append("### Ethics by Venue Category")
    L.append("")
    L.append("| Category | Yes | No | Total | Ethics Rate |")
    L.append("|----------|----:|---:|------:|------------:|")
    for cat in cat_order:
        yes = ethics_cat[cat].get("Yes", 0)
        no = ethics_cat[cat].get("No", 0)
        cat_total = yes + no
        rate = f"{yes*100/cat_total:.0f}%" if cat_total > 0 else "-"
        L.append(f"| {cat} | {yes} | {no} | {cat_total} | {rate} |")
    total_yes = sum(1 for p in papers if p["ethics_overall"] == "Yes")
    total_no = sum(1 for p in papers if p["ethics_overall"] == "No")
    L.append(f"| **Total** | **{total_yes}** | **{total_no}** | "
             f"**{total_yes + total_no}** | "
             f"**{total_yes*100/(total_yes+total_no):.0f}%** |")
    L.append("")

    # Ethics rate by top conference families
    L.append("### Ethics Rate by Conference Family (Top 15)")
    L.append("")
    L.append("| Family | Yes | No | Total | Ethics Rate |")
    L.append("|--------|----:|---:|------:|------------:|")

    family_ethics = defaultdict(lambda: Counter())
    for p in papers:
        if p["category"] in ("Preprint", "N/A", "Journal"):
            continue
        family = extract_conference_family(p["conf_cc"])
        if family:
            eth = p["ethics_overall"] or "Unknown"
            family_ethics[family][eth] += 1

    for fam, _ in family_counter.most_common(15):
        yes = family_ethics[fam].get("Yes", 0)
        no = family_ethics[fam].get("No", 0)
        fam_total = yes + no
        rate = f"{yes*100/fam_total:.0f}%" if fam_total > 0 else "-"
        L.append(f"| {fam} | {yes} | {no} | {fam_total} | {rate} |")
    L.append("")

    # Ethics rate by top journals
    L.append("### Ethics Rate by Journal (Top 10)")
    L.append("")
    L.append("| Journal | Yes | No | Total | Ethics Rate |")
    L.append("|---------|----:|---:|------:|------------:|")

    journal_ethics = defaultdict(lambda: Counter())
    for p in papers:
        if p["category"] != "Journal":
            continue
        eth = p["ethics_overall"] or "Unknown"
        journal_ethics[p["conf_cc"]][eth] += 1

    for jname, _ in journal_counter.most_common(10):
        yes = journal_ethics[jname].get("Yes", 0)
        no = journal_ethics[jname].get("No", 0)
        j_total = yes + no
        rate = f"{yes*100/j_total:.0f}%" if j_total > 0 else "-"
        L.append(f"| {jname} | {yes} | {no} | {j_total} | {rate} |")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 9. CLASSIFICATION METHODOLOGY
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 9. Classification Methodology")
    L.append("")
    L.append("The CONF-CC field was populated using a 3-phase waterfall classifier "
             "(`PYTHON/add_conference_field_cc.py`):")
    L.append("")
    L.append("1. **Phase 1 (Local Heuristic):** Regex matching on `publication` and `type` "
             "YAML fields against 90+ known conference aliases and 50+ journal patterns. Instant.")
    L.append("2. **Phase 2 (OpenAlex API):** DOI-based lookup for papers unresolved by Phase 1. "
             "Returns venue name and type. ~0.1s per query.")
    L.append("3. **Phase 3 (Semantic Scholar API):** ArXiv ID or DOI lookup for remaining papers. "
             "Returns venue and publication year. ~4s per query.")
    L.append("4. **Fallback:** Papers with no API match classified as Preprint (if type=preprint) "
             "or N/A.")
    L.append("")

    # Phase attribution from log
    if phase_data:
        L.append("### Phase Attribution")
        L.append("")
        p_stats = phase_data.get("phase_stats", {})
        classified = phase_data.get("classified", 0)
        skipped = phase_data.get("skipped_existing", 0)
        phase3 = p_stats.get("phase3", 0)
        fallback = p_stats.get("fallback", 0)

        L.append("| Phase | Papers | Description |")
        L.append("|-------|-------:|-------------|")
        L.append(f"| Phase 1 + 2 (pre-existing) | {skipped} | "
                 f"Classified by local heuristic or OpenAlex before Phase 3 run |")
        L.append(f"| Phase 3 (Semantic Scholar) | {phase3} | "
                 f"Resolved via Semantic Scholar API |")
        L.append(f"| Fallback | {fallback} | "
                 f"Unresolved → Preprint or N/A based on paper type |")
        L.append(f"| **Total** | **{skipped + classified}** | |")
        L.append("")

    # Categorization logic for this report
    L.append("### Report Categorization Logic")
    L.append("")
    L.append("This report groups the {0} unique CONF-CC values into 6 categories:".format(unique_venues))
    L.append("")
    L.append("```")
    L.append('CONF-CC == "Preprint"               → Preprint')
    L.append('CONF-CC == "N/A"                     → N/A')
    L.append('contains "Findings"                  → Findings')
    L.append('contains "Workshop"/"Demo"/"Shared"  → Workshop')
    L.append('matches KNOWN_JOURNALS set            → Journal')
    L.append('contains "Journal"/"Transactions"    → Journal (heuristic)')
    L.append('everything else                      → Conference')
    L.append("```")
    L.append("")
    L.append(f"Journal detection uses {len(KNOWN_JOURNALS)} known journal names compiled from "
             f"`JOURNAL_EXACT` ({len(JOURNAL_EXACT)} entries) and `JOURNAL_SUBSTRING` "
             f"({len(JOURNAL_SUBSTRING)} entries) dictionaries in `add_conference_field_cc.py`, "
             f"plus {len(KNOWN_JOURNALS) - len(set(JOURNAL_EXACT.values()) | set(JOURNAL_SUBSTRING.values()))} "
             f"additional journals identified from OpenAlex/Semantic Scholar API results.")
    L.append("")
    L.append("---")
    L.append("")

    # ══════════════════════════════════════════════════════════════════════
    # 10. APPENDIX: FULL VENUE LIST
    # ══════════════════════════════════════════════════════════════════════
    L.append("## 10. Appendix: Full Venue List")
    L.append("")
    L.append(f"All {unique_venues} unique CONF-CC values, sorted by paper count (descending).")
    L.append("")
    L.append("| # | CONF-CC Value | Category | Count |")
    L.append("|--:|---------------|----------|------:|")
    for i, (venue, count) in enumerate(conf_cc_counter.most_common(), 1):
        cat = categorize_venue(venue)
        # Truncate very long venue names
        display_venue = venue if len(venue) <= 80 else venue[:77] + "..."
        L.append(f"| {i} | {display_venue} | {cat} | {count} |")
    L.append("")

    L.append("---")
    L.append("")
    L.append(f"*Generated: 2026-02-20 | Script: `PYTHON/generate_conference_report_cc.py` | "
             f"Papers: {total:,} | Venues: {unique_venues} | "
             f"Categories: {len(category_counter)}*")

    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=== Conference Representation Report Generator ===")
    print()

    # ── Scan papers ──────────────────────────────────────────────────
    print("Scanning paper YAML fields...")
    papers = scan_papers()
    print(f"  Papers scanned: {len(papers)}")

    # ── Load phase attribution log ───────────────────────────────────
    phase_data = {}
    if PHASE_LOG.exists():
        print(f"Loading phase log: {PHASE_LOG.name}")
        with open(PHASE_LOG, "r", encoding="utf-8") as f:
            phase_data = json.load(f)
        print(f"  Log entries: {phase_data.get('classified', 0)} classified, "
              f"{phase_data.get('skipped_existing', 0)} pre-existing")
    else:
        print("  Phase log not found, skipping phase attribution")

    # ── Pre-report statistics ────────────────────────────────────────
    print()
    category_counter = Counter(p["category"] for p in papers)
    print("Category breakdown:")
    for cat in ["Preprint", "Conference", "N/A", "Journal", "Findings", "Workshop"]:
        count = category_counter.get(cat, 0)
        print(f"  {cat:12s}: {count:5d} ({count*100/len(papers):.1f}%)")

    conf_cc_counter = Counter(p["conf_cc"] for p in papers)
    print(f"\nUnique CONF-CC values: {len(conf_cc_counter)}")
    print("Top 10 venues:")
    for venue, count in conf_cc_counter.most_common(10):
        print(f"  [{count:4d}] {venue}")

    # ── Generate report ──────────────────────────────────────────────
    print("\nGenerating report...")
    report = generate_report(papers, phase_data)

    # ── Write output ─────────────────────────────────────────────────
    STATS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"  Size: {len(report):,} characters, {report.count(chr(10)):,} lines")

    # ── Verification ─────────────────────────────────────────────────
    print("\n=== VERIFICATION ===")
    total = len(papers)
    cat_sum = sum(category_counter.values())
    print(f"  Total papers:    {total}")
    print(f"  Category sum:    {cat_sum} {'PASS' if cat_sum == total else 'FAIL'}")

    # Check expected values
    preprint = category_counter.get("Preprint", 0)
    print(f"  Preprint count:  {preprint} (expected ~952)")

    top_venue = conf_cc_counter.most_common(1)
    if top_venue:
        print(f"  Top venue:       {top_venue[0][0]} ({top_venue[0][1]})")

    # ACL 2025 check
    acl_2025 = conf_cc_counter.get("ACL 2025", 0)
    print(f"  ACL 2025:        {acl_2025} (expected ~45)")

    # Section count in report
    sections = [line for line in report.split("\n") if line.startswith("## ")]
    print(f"  Report sections: {len(sections)}")

    # Table count
    table_lines = [line for line in report.split("\n") if line.startswith("|")]
    print(f"  Table lines:     {len(table_lines)}")

    print(f"\n  Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
