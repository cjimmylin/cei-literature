#!/usr/bin/env python3
"""
Generate Religious & Ethical Tradition Gap Analysis Report.

Produces a comprehensive markdown report documenting coverage gaps
for non-Western religious/ethical traditions in the vault.
"""

import re
import json
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
STATS_DIR = WS_ROOT / "STATISTICS"
LOGS_DIR = WS_ROOT / "logs"
OUTPUT_FILE = STATS_DIR / "20260216-religious-ethical-tradition-gap-analysis.md"

# Data files
CANDIDATES_FILE = LOGS_DIR / "20260208-benchmark_survey_candidates.json"
AUDIT_FILE = LOGS_DIR / "20260215-religious_traditions_audit.json"

# Import patterns
sys.path.insert(0, str(SCRIPT_DIR))
from classify_cultural_religious import RELIGIOUS_PATTERNS, CULTURAL_PATTERNS


def extract_year(filename):
    """Extract year from filename like '2024-Author-Title.md'."""
    m = re.match(r'^(\d{4})-', filename)
    return int(m.group(1)) if m else 9999


def scan_all_papers():
    """Scan all paper YAML frontmatter for religious/cultural/benchmark fields."""
    papers = []
    for p in sorted(PAPERS_DIR.glob("*.md")):
        content = p.read_text(encoding="utf-8")
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)

        fields = {}
        for line in fm.split("\n"):
            if ":" in line and not line.startswith("  "):
                key, _, val = line.partition(":")
                fields[key.strip()] = val.strip().strip('"')

        papers.append({
            "filename": p.name,
            "year": extract_year(p.name),
            "religious_values": fields.get("religious_values", "N/A"),
            "religious_values_list": fields.get("religious_values_list", "N/A"),
            "national_ethnic_cultural": fields.get("national_ethnic_cultural", "N/A"),
            "is_benchmark": fields.get("is_benchmark", "No"),
            "ethics": fields.get("ethics_overall", "No"),
            "ethics_type": fields.get("ethics_type", "N/A"),
        })
    return papers


def make_wikilink(filename):
    name = filename[:-3] if filename.endswith(".md") else filename
    return f"[[{name}]]"


def make_crosstab(row_label, rows, cols, matrix, show_totals=True):
    """Generate markdown cross-tab table."""
    lines = []
    header = [row_label] + list(cols)
    if show_totals:
        header.append("Total")
    lines.append("| " + " | ".join(str(c) for c in header) + " |")
    lines.append("|" + "|".join("---" for _ in header) + "|")

    col_totals = Counter()
    for rk in rows:
        vals = []
        row_total = 0
        for ck in cols:
            v = matrix.get(rk, {}).get(ck, 0)
            vals.append(str(v) if v > 0 else "-")
            col_totals[ck] += v
            row_total += v
        row = [rk] + vals
        if show_totals:
            row.append(str(row_total))
        lines.append("| " + " | ".join(str(c) for c in row) + " |")

    if show_totals:
        total_row = ["**Total**"]
        grand = 0
        for ck in cols:
            total_row.append(str(col_totals[ck]))
            grand += col_totals[ck]
        total_row.append(f"**{grand}**")
        lines.append("| " + " | ".join(str(c) for c in total_row) + " |")

    return lines


def main():
    print("Scanning papers...")
    papers = scan_all_papers()
    total_papers = len(papers)
    print(f"  Found {total_papers} papers")

    # Load optional data sources
    candidates = []
    if CANDIDATES_FILE.exists():
        with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
            candidates = json.load(f)
        print(f"  Loaded {len(candidates)} benchmark candidates")

    audit_data = None
    if AUDIT_FILE.exists():
        with open(AUDIT_FILE, "r", encoding="utf-8") as f:
            audit_data = json.load(f)
        print(f"  Loaded audit data: {audit_data['metadata']['candidate_count']} audit candidates")

    # R-agent reports
    r_agent_reports = sorted(LOGS_DIR.glob("20260213-AgentR*_Report.md"))
    print(f"  Found {len(r_agent_reports)} R-agent reports")

    # ── Analysis ──────────────────────────────────────────────────────

    # Religious values distribution
    # Split on both ", " and "; " to handle inconsistent agent output
    def split_traditions(val):
        """Split comma-or-semicolon-separated tradition values."""
        parts = re.split(r'[,;]\s*', val)
        return [p.strip() for p in parts if p.strip()]

    religious_counts = Counter()
    tradition_papers = defaultdict(list)  # tradition -> [paper filenames]
    for p in papers:
        rv = p["religious_values"]
        if rv and rv != "N/A":
            for t in split_traditions(rv):
                religious_counts[t] += 1
                tradition_papers[t].append(p["filename"])
        else:
            religious_counts["N/A"] += 1

    # Cultural distribution
    cultural_counts = Counter()
    for p in papers:
        nc = p["national_ethnic_cultural"]
        if nc and nc != "N/A":
            for c in nc.split(", "):
                cultural_counts[c.strip()] += 1

    # Benchmark papers per tradition
    benchmark_papers = [p for p in papers if p["is_benchmark"] == "Yes"]
    tradition_benchmarks = defaultdict(list)
    for p in benchmark_papers:
        rv = p["religious_values"]
        if rv and rv != "N/A":
            for t in split_traditions(rv):
                tradition_benchmarks[t].append(p["filename"])

    # Ethics papers per tradition
    ethics_papers = [p for p in papers if p["ethics"] == "Yes"]

    # Year distribution per tradition
    tradition_years = defaultdict(lambda: Counter())
    for p in papers:
        rv = p["religious_values"]
        if rv and rv != "N/A":
            for t in split_traditions(rv):
                if p["year"] != 9999:
                    tradition_years[t][p["year"]] += 1

    # Overall year distribution
    year_counts = Counter()
    for p in papers:
        if p["year"] != 9999:
            year_counts[p["year"]] += 1

    # Coverage levels
    ALL_TRADITIONS = list(RELIGIOUS_PATTERNS.keys())

    def coverage_level(count, bench_count):
        if count == 0:
            return "NONE"
        if bench_count == 0 and count <= 3:
            return "MINIMAL"
        if bench_count == 0:
            return "LOW"
        if bench_count <= 3:
            return "MODERATE"
        return "STRONG"

    # Language x tradition cross-tab
    # For candidates (if loaded), extract language info
    cand_traditions = defaultdict(int)
    cand_languages = defaultdict(int)
    cand_trad_lang = defaultdict(lambda: defaultdict(int))

    if candidates:
        for e in candidates:
            text = " ".join([
                e.get("what_measures", ""),
                e.get("how_measures", ""),
                e.get("reasoning", ""),
                e.get("benchmark_name", ""),
            ]).lower()

            # Detect traditions
            for trad, patterns in RELIGIOUS_PATTERNS.items():
                for pat in patterns:
                    if re.search(pat, text, re.IGNORECASE):
                        cand_traditions[trad] += 1
                        break

            # Detect languages (simplified)
            LANGUAGES = {
                "English": r"\benglish\b",
                "Chinese": r"\bchinese\b|\bmandarin\b",
                "Arabic": r"\barabic\b",
                "Korean": r"\bkorean\b",
                "Japanese": r"\bjapanese\b",
                "Hindi": r"\bhindi\b",
                "Indonesian": r"\bindonesian\b",
                "Non-English (other)": r"\bnon[\s-]?english\b|\bmultilingual\b",
            }
            for lang, pat in LANGUAGES.items():
                if re.search(pat, text, re.IGNORECASE):
                    cand_languages[lang] += 1

    # Western vs non-Western comparison
    WESTERN = {"Christianity", "Multiple Religions"}
    WESTERN_PHILOSOPHICAL = {"Deontological", "Consequentialist", "Virtue Ethics"}
    NON_WESTERN = {"Islam", "Buddhism", "Hinduism", "Confucianism", "Taoism",
                   "Shinto", "Jainism", "Sikhism", "Baha'i", "Zoroastrianism",
                   "Indigenous Spirituality", "Judaism"}

    western_count = sum(religious_counts.get(t, 0) for t in WESTERN)
    non_western_count = sum(religious_counts.get(t, 0) for t in NON_WESTERN)

    # ── Assemble report ──────────────────────────────────────────────
    L = []

    # HEADER
    L.append("# Religious & Ethical Tradition Gap Analysis")
    L.append("")
    L.append(f"**Generated:** 2026-02-15 | **Total Papers:** {total_papers} | "
             f"**Religious-tagged:** {total_papers - religious_counts.get('N/A', 0)} | "
             f"**Benchmarks:** {len(benchmark_papers)}")
    L.append("")
    L.append("---")
    L.append("")

    # TABLE OF CONTENTS
    L.append("## Table of Contents")
    L.append("")
    toc = [
        "1. Executive Summary",
        "2. Methodology",
        "3. Coverage Matrix",
        "4. Critical Gaps Deep Dive",
        "5. Language x Tradition Cross-Tabulation",
        "6. Temporal Trends",
        "7. What Was Searched (R-Agent Summary)",
        "8. Comparison with Western Frameworks",
        "9. Structural Barriers to Benchmark Development",
        "10. Priority Recommendations",
        "Appendix A: Full Tradition Paper Lists",
        "Appendix B: Search Query Archive",
    ]
    for item in toc:
        anchor = item.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(":", "").replace(",", "").replace("/", "")
        L.append(f"- [{item}](#{anchor})")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 1: Executive Summary
    L.append("## 1. Executive Summary")
    L.append("")
    na_count = religious_counts.get("N/A", 0)
    tagged_count = total_papers - na_count
    L.append(f"This report analyzes the coverage of religious and ethical traditions across "
             f"**{total_papers} papers** in the CEI Literature Vault. Of these, **{tagged_count}** papers "
             f"({tagged_count * 100 // total_papers}%) are tagged with at least one religious tradition, "
             f"while **{na_count}** ({na_count * 100 // total_papers}%) remain unclassified (N/A).")
    L.append("")

    # Key findings
    L.append("### Key Findings")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Total papers | {total_papers} |")
    L.append(f"| Religious-tagged papers | {tagged_count} ({tagged_count * 100 // total_papers}%) |")
    L.append(f"| Untagged (N/A) | {na_count} ({na_count * 100 // total_papers}%) |")
    L.append(f"| Benchmark papers (is_benchmark=Yes) | {len(benchmark_papers)} |")
    L.append(f"| Ethics papers (ethics=Yes) | {len(ethics_papers)} |")
    L.append(f"| Traditions with ZERO benchmark coverage | {sum(1 for t in ALL_TRADITIONS if t != 'Multiple Religions' and len(tradition_benchmarks.get(t, [])) == 0)} |")
    L.append(f"| Western-tradition papers | {western_count} |")
    L.append(f"| Non-Western tradition papers | {non_western_count} |")
    L.append("")

    # Critical gaps
    zero_bench = [t for t in ALL_TRADITIONS if t != "Multiple Religions" and len(tradition_benchmarks.get(t, [])) == 0]
    if zero_bench:
        L.append("### Critical Gaps (Zero Benchmark Coverage)")
        L.append("")
        for t in zero_bench:
            paper_count = religious_counts.get(t, 0)
            L.append(f"- **{t}**: {paper_count} papers in vault, **0 benchmarks**")
        L.append("")

    # Audit results if available
    if audit_data:
        L.append("### Audit Results (Extended Keyword Scan)")
        L.append("")
        L.append(f"An extended keyword audit scanning PDF extracts (beyond title+abstract) identified "
                 f"**{audit_data['metadata']['candidate_count']} additional papers** that may belong to "
                 f"religious traditions but are currently tagged N/A.")
        L.append("")
        if audit_data.get("tradition_counts"):
            L.append("| Tradition | Audit Candidates |")
            L.append("|-----------|-----------------|")
            for t, c in sorted(audit_data["tradition_counts"].items(), key=lambda x: -x[1]):
                L.append(f"| {t} | {c} |")
            L.append("")

    L.append("---")
    L.append("")

    # SECTION 2: Methodology
    L.append("## 2. Methodology")
    L.append("")
    L.append("### Data Collection")
    L.append("")
    L.append("This vault's religious tradition coverage was built through three parallel efforts:")
    L.append("")
    L.append(f"1. **10 Religion-specific R-agents** (Feb 13, 2026): Targeted Semantic Scholar searches for each tradition")
    L.append(f"2. **25 Language-based agents** (Feb 13, 2026): Broad language/culture-based searches that captured religious content")
    L.append(f"3. **Keyword classifier** (`classify_cultural_religious.py`): Automated tagging based on title+abstract pattern matching")
    L.append("")
    L.append("### Classification Approach")
    L.append("")
    L.append(f"The classifier uses {len(RELIGIOUS_PATTERNS)} religious tradition categories with regex pattern matching. "
             f"Patterns are matched case-insensitively against paper titles and abstracts. Papers can be tagged with multiple traditions.")
    L.append("")
    L.append("### Limitations")
    L.append("")
    L.append("- **Title+abstract only**: The classifier does not scan PDF full text, missing papers where religious content appears only in the body")
    L.append("- **Keyword-dependent**: Concepts discussed in translated/localized terminology may not match English-language patterns")
    L.append("- **Single-pass**: No disambiguation between homonyms (e.g., 'dharma' in Buddhism vs Hinduism)")
    L.append("- **No negative evidence**: Cannot detect papers that discuss absence of religious frameworks")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 3: Coverage Matrix
    L.append("## 3. Coverage Matrix")
    L.append("")
    L.append("| Tradition | Papers | Benchmarks | Ethics Papers | Coverage Level |")
    L.append("|-----------|--------|-----------|---------------|---------------|")

    for t in sorted(ALL_TRADITIONS, key=lambda x: -religious_counts.get(x, 0)):
        if t == "Multiple Religions":
            continue
        pc = religious_counts.get(t, 0)
        bc = len(tradition_benchmarks.get(t, []))
        # Count ethics papers for this tradition
        ec = sum(1 for p in papers if p["ethics"] == "Yes" and t in p.get("religious_values", ""))
        level = coverage_level(pc, bc)
        level_fmt = f"**{level}**" if level in ("NONE", "MINIMAL") else level
        L.append(f"| {t} | {pc} | {bc} | {ec} | {level_fmt} |")

    # Add Multiple Religions at end
    mr_pc = religious_counts.get("Multiple Religions", 0)
    mr_bc = len(tradition_benchmarks.get("Multiple Religions", []))
    L.append(f"| Multiple Religions | {mr_pc} | {mr_bc} | - | - |")
    L.append(f"| **N/A (untagged)** | **{na_count}** | - | - | - |")
    L.append("")

    # Visual summary
    L.append("### Coverage Distribution")
    L.append("")
    L.append("```")
    for t in sorted(ALL_TRADITIONS, key=lambda x: -religious_counts.get(x, 0)):
        if t == "Multiple Religions":
            continue
        pc = religious_counts.get(t, 0)
        bar = "█" * min(pc, 60)
        L.append(f"  {t:25s} | {bar} ({pc})")
    L.append("```")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 4: Critical Gaps Deep Dive
    L.append("## 4. Critical Gaps Deep Dive")
    L.append("")

    gap_traditions = {
        "Buddhism": {
            "principles": "Four Noble Truths, Eightfold Path, dependent origination (paticcasamuppada), non-attachment, compassion (karuna), mindfulness (sati)",
            "barriers": "Buddhist ethics emphasizes context-dependent wisdom (prajna) over fixed rules, making benchmark operationalization challenging. The emphasis on internal states (intention, mindfulness) is difficult to assess through text-based evaluation.",
            "opportunities": "DharmaBench and BuddhismEval are emerging efforts. Five Precepts could serve as a structured evaluation framework. Buddhist-majority countries (Thailand, Myanmar, Sri Lanka) have growing NLP communities.",
        },
        "Indigenous Spirituality": {
            "principles": "Relational accountability, reciprocity with land and ancestors, oral tradition, Elder authority, holistic wellbeing, data sovereignty, two-eyed seeing (Etuaptmumk)",
            "barriers": "Indigenous knowledge systems are fundamentally oral and place-based, resisting codification into datasets. Data sovereignty principles (OCAP, CARE) may conflict with open-access benchmark norms. The diversity of 5,000+ Indigenous peoples means no single 'Indigenous ethics' exists.",
            "opportunities": "Emerging work on Indigenous data governance and AI sovereignty. The CARE Principles (Collective benefit, Authority, Responsibility, Ethics) provide a framework. Collaborations with First Nations digital humanities could yield culturally appropriate evaluation methods.",
        },
        "Hinduism": {
            "principles": "Dharma (cosmic order/duty), karma (action-consequence), ahimsa (non-violence), moksha (liberation), varna-ashrama (social duty), artha (prosperity), kama (pleasure)",
            "barriers": "Hindu ethics is highly contextual (svadharma — one's own duty varies by station, stage of life). Multiple philosophical schools (Advaita, Dvaita, etc.) disagree on fundamentals. The caste dimension is politically sensitive for benchmark development.",
            "opportunities": "India's large AI research community could develop Hindi/Sanskrit NLP benchmarks. The Bhagavad Gita's structured ethical dilemmas (Arjuna's moral crisis) could be operationalized. Existing work on Indian language NLP provides infrastructure.",
        },
        "Taoism": {
            "principles": "Wu wei (non-action/effortless action), ziran (naturalness/spontaneity), yin-yang balance, the Tao (the Way), simplicity, harmony with nature, non-competition",
            "barriers": "Taoist ethics is anti-systematizing by nature — 'The Tao that can be told is not the eternal Tao.' Valuing inaction and paradox makes standard benchmark formats (choose the 'right' answer) antithetical to the philosophy.",
            "opportunities": "Environmental ethics angle (harmony with nature) could connect to AI sustainability research. Chinese-language NLP benchmarks could incorporate Taoist ethical reasoning. Comparative philosophy approaches could test LLMs' ability to reason across Western and Taoist frameworks.",
        },
        "Shinto": {
            "principles": "Purity/pollution (hare/kegare), harmony (wa), gratitude to kami spirits, connection to nature, ritual purification (harai), communal obligation",
            "barriers": "Shinto is practice-oriented rather than doctrine-oriented, with no central scripture. Its deep integration with Japanese culture makes isolation as a distinct 'ethics' challenging. Limited academic literature frames Shinto as a benchmark-relevant ethical system.",
            "opportunities": "Japanese NLP research is strong (JETHICS, JCommonsense). Integration with existing Japanese cultural values benchmarks could capture Shinto-influenced reasoning. The wa (harmony) concept overlaps with conflict resolution evaluation.",
        },
        "Jainism": {
            "principles": "Ahimsa (extreme non-violence), anekantavada (many-sidedness of truth), aparigraha (non-possessiveness), satya (truthfulness), asteya (non-stealing)",
            "barriers": "Small global population (~4.5M) limits research community. Jain ethics' absolutist stance on non-violence may seem impractical in AI contexts. Academic focus is limited compared to larger traditions.",
            "opportunities": "Anekantavada (many-sidedness) is directly relevant to AI pluralism — testing whether LLMs can hold multiple valid perspectives simultaneously. Jain dietary/lifestyle restrictions provide structured evaluation scenarios.",
        },
    }

    for tradition, info in gap_traditions.items():
        pc = religious_counts.get(tradition, 0)
        bc = len(tradition_benchmarks.get(tradition, []))
        L.append(f"### {tradition}")
        L.append("")
        L.append(f"**Status:** {pc} papers, {bc} benchmarks")
        L.append("")
        L.append(f"**Key ethical principles:** {info['principles']}")
        L.append("")
        L.append(f"**Why benchmarks don't exist:** {info['barriers']}")
        L.append("")
        L.append(f"**Research opportunities:** {info['opportunities']}")
        L.append("")

        # List closest papers
        if tradition in tradition_papers and tradition_papers[tradition]:
            L.append(f"**Closest papers in vault ({min(len(tradition_papers[tradition]), 10)}):**")
            L.append("")
            for fn in tradition_papers[tradition][:10]:
                L.append(f"- {make_wikilink(fn)}")
            if len(tradition_papers[tradition]) > 10:
                L.append(f"- *... and {len(tradition_papers[tradition]) - 10} more*")
            L.append("")
        else:
            L.append("**Papers in vault:** None currently tagged")
            L.append("")

    L.append("---")
    L.append("")

    # SECTION 5: Language x Tradition
    L.append("## 5. Language x Tradition Cross-Tabulation")
    L.append("")
    L.append("Which traditions lack non-English language support?")
    L.append("")

    # Build language x tradition from cultural tags
    TRADITION_LANGUAGE_MAP = {
        "Buddhism": ["Chinese", "Japanese", "Korean", "Thai", "Vietnamese"],
        "Hinduism": ["Indian"],
        "Islam": ["Arabic", "Indonesian", "Iranian"],
        "Confucianism": ["Chinese", "Korean"],
        "Taoism": ["Chinese"],
        "Shinto": ["Japanese"],
        "Sikhism": ["Indian"],
        "Judaism": ["Hebrew/Israeli"],
        "Christianity": ["American", "Western", "French", "German"],
        "Indigenous Spirituality": ["Australian/Aboriginal"],
    }

    # Cross-reference: for each tradition, how many papers also have a cultural tag
    trad_lang_matrix = defaultdict(lambda: defaultdict(int))
    for p in papers:
        rv = p["religious_values"]
        nc = p["national_ethnic_cultural"]
        if rv == "N/A" or nc == "N/A":
            continue
        for t in split_traditions(rv):
            for c in nc.split(", "):
                c = c.strip()
                trad_lang_matrix[t][c] += 1

    # Show traditions with their cultural co-occurrences
    active_cultures = set()
    for t_data in trad_lang_matrix.values():
        active_cultures.update(t_data.keys())

    if active_cultures:
        top_cultures = sorted(active_cultures, key=lambda c: -sum(trad_lang_matrix[t].get(c, 0) for t in ALL_TRADITIONS))[:12]
        active_traditions = [t for t in ALL_TRADITIONS if t != "Multiple Religions" and religious_counts.get(t, 0) > 0]

        L.extend(make_crosstab("Tradition", active_traditions, top_cultures, trad_lang_matrix))
        L.append("")

    L.append("### Non-English Language Support Gaps")
    L.append("")
    L.append("| Tradition | Expected Languages | Papers with Language Co-tag | Gap |")
    L.append("|-----------|-------------------|---------------------------|-----|")
    for trad, expected_langs in TRADITION_LANGUAGE_MAP.items():
        total_trad = religious_counts.get(trad, 0)
        cotagged = sum(trad_lang_matrix.get(trad, {}).get(l, 0) for l in expected_langs)
        gap = "CRITICAL" if total_trad > 0 and cotagged == 0 else ("LOW" if cotagged > total_trad * 0.3 else "MODERATE")
        L.append(f"| {trad} | {', '.join(expected_langs)} | {cotagged}/{total_trad} | {gap} |")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 6: Temporal Trends
    L.append("## 6. Temporal Trends")
    L.append("")
    L.append("Year-over-year publication trends for religious/ethical tradition papers (2020-2026).")
    L.append("")

    years = sorted(y for y in range(2020, 2027))
    L.append("| Year | Total Papers | Religion-tagged | % Tagged | Top Tradition |")
    L.append("|------|-------------|----------------|----------|---------------|")

    for y in years:
        total_y = year_counts.get(y, 0)
        tagged_y = sum(1 for p in papers if p["year"] == y and p["religious_values"] != "N/A")
        pct = f"{tagged_y * 100 // total_y}%" if total_y > 0 else "-"

        # Top tradition for this year
        year_trad_counts = Counter()
        for p in papers:
            if p["year"] == y and p["religious_values"] != "N/A":
                for t in split_traditions(p["religious_values"]):
                    year_trad_counts[t] += 1
        top = year_trad_counts.most_common(1)[0][0] if year_trad_counts else "-"

        L.append(f"| {y} | {total_y} | {tagged_y} | {pct} | {top} |")
    L.append("")

    # Tradition x year for key traditions
    key_traditions = [t for t in ALL_TRADITIONS if t != "Multiple Religions" and religious_counts.get(t, 0) > 0]
    if key_traditions and tradition_years:
        trad_year_matrix = {}
        for t in key_traditions:
            trad_year_matrix[t] = {y: tradition_years[t].get(y, 0) for y in years}
        L.append("### Tradition x Year (2020-2026)")
        L.append("")
        L.extend(make_crosstab("Tradition", key_traditions, years, trad_year_matrix))
        L.append("")

    L.append("---")
    L.append("")

    # SECTION 7: What Was Searched
    L.append("## 7. What Was Searched (R-Agent Summary)")
    L.append("")
    L.append("10 religion-specific R-agents conducted targeted Semantic Scholar searches on Feb 13, 2026:")
    L.append("")

    agent_descriptions = {
        "AgentR1_Islam": "Islamic ethics, Sharia law, Quran-based AI evaluation, halal/haram classification",
        "AgentR2_Christianity_Judaism": "Christian ethics benchmarks, Biblical reasoning, Jewish ethics, Talmudic logic",
        "AgentR3_Hinduism_Sikhism_Jainism": "Hindu dharma, Vedic ethics, Sikh values, Jain non-violence in AI",
        "AgentR4_Buddhism": "Buddhist ethics benchmarks, DharmaBench, Five Precepts, mindfulness in AI",
        "AgentR5_Confucianism_Taoism": "Confucian values, ren-yi-li, filial piety, Taoist wu-wei, harmony",
        "AgentR6_Shinto_Japanese": "Shinto ethics, Japanese cultural values, wa harmony, bushido",
        "AgentR7_Ubuntu_African": "Ubuntu philosophy, African ethics, communitarian values, umuntu ngumuntu",
        "AgentR8_Indigenous": "Indigenous knowledge systems, First Nations ethics, data sovereignty, oral traditions",
        "AgentR9_Zoroastrian_Bahai_Others": "Zoroastrian ethics, Baha'i values, minor religious traditions",
        "AgentR10_Cross_Religious_Bias": "Cross-religious bias in LLMs, religious fairness, interfaith comparison",
    }

    L.append("| Agent | Focus | Report |")
    L.append("|-------|-------|--------|")
    for report in sorted(r_agent_reports):
        name = report.stem.replace("20260213-", "")
        desc = agent_descriptions.get(name, "Religious tradition search")
        L.append(f"| {name} | {desc} | `{report.name}` |")
    L.append("")

    L.append("### Additional Search Campaigns")
    L.append("")
    L.append("- **25 Language-based agents** (A1-A5, B1-B9 + others): Broad searches by language that captured religious content")
    L.append("- **Exhaustive search** (Feb 7, 2026): 300 papers from systematic academic search")
    L.append("- **Keyword classifier**: Automated regex-based classification of all papers")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 8: Western vs Non-Western Comparison
    L.append("## 8. Comparison with Western Frameworks")
    L.append("")
    L.append("This section compares the benchmark coverage of Western philosophical frameworks "
             "against non-Western religious/ethical traditions to quantify the Western-centric bias.")
    L.append("")

    # Count Western philosophical frameworks from benchmark candidates
    western_fw_counts = Counter()
    if candidates:
        for e in candidates:
            text = " ".join([e.get("what_measures", ""), e.get("reasoning", ""),
                           e.get("benchmark_name", ""), e.get("normative_frameworks", "")]).lower()
            if re.search(r'\bdeontolog|\bkantian|\bcategorical.imperative', text):
                western_fw_counts["Deontological"] += 1
            if re.search(r'\bconsequential|\butilitarian|\bgreatest.*good', text):
                western_fw_counts["Consequentialist"] += 1
            if re.search(r'\bvirtue.*ethic|\baristot|\beudaimonia', text):
                western_fw_counts["Virtue Ethics"] += 1
            if re.search(r'\bcare.*ethic|\bfeminist.*ethic', text):
                western_fw_counts["Care Ethics"] += 1

    L.append("| Framework | Type | Benchmark Mentions | Papers | Ratio |")
    L.append("|-----------|------|-------------------|--------|-------|")

    # Western
    for fw, count in sorted(western_fw_counts.items(), key=lambda x: -x[1]):
        L.append(f"| {fw} | Western philosophical | {count} | - | - |")

    # Non-Western religious
    for t in ["Islam", "Buddhism", "Hinduism", "Confucianism", "Taoism", "Shinto", "Judaism", "Indigenous Spirituality"]:
        bc = len(tradition_benchmarks.get(t, []))
        pc = religious_counts.get(t, 0)
        L.append(f"| {t} | Non-Western religious | {bc} | {pc} | {'N/A' if pc == 0 else f'{bc}/{pc}'} |")
    L.append("")

    total_western_fw = sum(western_fw_counts.values())
    total_non_western_bench = sum(len(tradition_benchmarks.get(t, [])) for t in NON_WESTERN)
    L.append(f"**Western philosophical framework mentions in benchmarks:** {total_western_fw}")
    L.append(f"**Non-Western religious tradition benchmarks:** {total_non_western_bench}")
    if total_western_fw > 0:
        ratio = total_western_fw / max(total_non_western_bench, 1)
        L.append(f"**Ratio (Western:Non-Western):** {ratio:.1f}:1")
    L.append("")
    L.append("---")
    L.append("")

    # SECTION 9: Structural Barriers
    L.append("## 9. Structural Barriers to Benchmark Development")
    L.append("")

    barriers = [
        ("Indigenous Data Sovereignty",
         "Indigenous communities increasingly assert sovereignty over their knowledge and data through "
         "frameworks like OCAP (Ownership, Control, Access, Possession) and the CARE Principles. Open-access "
         "benchmarks may conflict with these principles, as Indigenous knowledge is often contextual, relational, "
         "and not meant for decontextualized extraction."),
        ("Oral Tradition vs. Text-Based AI",
         "Many non-Western ethical traditions (Indigenous, African Ubuntu, aspects of Hinduism and Buddhism) "
         "are transmitted primarily through oral tradition, storytelling, and embodied practice. Text-based "
         "LLM evaluation fundamentally cannot capture these knowledge systems without significant cultural "
         "translation that risks distortion."),
        ("Cultural Sensitivity & Sacred Knowledge",
         "Some ethical/spiritual knowledge is considered sacred and not appropriate for public dataset creation. "
         "This includes Aboriginal Dreamtime narratives, certain Buddhist tantric teachings, and Indigenous "
         "ceremonial practices. Benchmark developers must navigate what can ethically be extracted."),
        ("Research Community Size",
         "Traditions like Jainism (~4.5M adherents), Zoroastrianism (~120K), and Baha'i (~8M) have much smaller "
         "academic research communities than Christianity or Islam. This creates a structural disadvantage in "
         "generating benchmark papers, independent of the tradition's ethical richness."),
        ("Philosophical Anti-Systematization",
         "Some traditions actively resist the kind of systematization that benchmarks require. Taoist ethics "
         "values paradox and non-action; Zen Buddhism emphasizes direct experience over conceptual frameworks; "
         "many Indigenous traditions resist codification as a matter of principle."),
        ("Linguistic Barriers",
         "Key texts and concepts in many traditions exist primarily in non-English languages (Sanskrit, Pali, "
         "Classical Chinese, Arabic, various Indigenous languages). The NLP research community's English-language "
         "bias means these traditions are structurally underrepresented."),
        ("Funding & Institutional Bias",
         "AI ethics research funding is concentrated in Western institutions. Non-Western philosophical and "
         "religious departments rarely have connections to NLP/AI research groups. This structural gap means "
         "domain expertise (religious scholars) and technical expertise (AI researchers) rarely overlap."),
    ]

    for i, (title, desc) in enumerate(barriers, 1):
        L.append(f"### {i}. {title}")
        L.append("")
        L.append(desc)
        L.append("")

    L.append("---")
    L.append("")

    # SECTION 10: Priority Recommendations
    L.append("## 10. Priority Recommendations")
    L.append("")

    L.append("### Tier 1: Immediate (Reclassify Existing Papers)")
    L.append("")
    L.append("These actions can be taken now using existing vault data:")
    L.append("")
    L.append("1. **Run expanded keyword audit** on all 1,847 papers including PDF extract text")
    L.append("2. **Agent swarm deep-read** of audit candidates for accurate reclassification")
    L.append("3. **Fix false N/A tags** for papers discussing religious ethics in their body text but not title/abstract")
    L.append("4. **Cross-reference cultural tags** — papers tagged 'Indian' may discuss Hindu ethics; 'Japanese' may discuss Shinto")
    L.append("")

    if audit_data and audit_data["metadata"]["candidate_count"] > 0:
        L.append(f"*The extended keyword audit found **{audit_data['metadata']['candidate_count']} candidates** for reclassification.*")
        L.append("")

    L.append("### Tier 2: High-Value (Targeted Search)")
    L.append("")
    L.append("Searches targeting specific gaps:")
    L.append("")
    L.append("| Priority | Tradition | Search Strategy |")
    L.append("|----------|-----------|-----------------|")
    L.append("| 1 | Buddhist | HuggingFace datasets (DharmaBench, BuddhismEval), ACL C3NLP workshop, cite-tracking |")
    L.append("| 2 | Ubuntu/African | AfricaNLP, Deep Learning Indaba, Masakhane project, forward citations of UbuntuGuard |")
    L.append("| 3 | Hindu | Indian NLP conferences, Hindi-language AI ethics, Bhagavad Gita reasoning papers |")
    L.append("| 4 | Indigenous | Data sovereignty conferences, AIATSIS, Canadian First Nations digital humanities |")
    L.append("| 5 | Taoist | Chinese-language NLP (CCL, ROCLING), environmental ethics x AI |")
    L.append("| 6 | Shinto | Japanese NLP (YANS, NLP2026), integration with JETHICS |")
    L.append("| 7 | Jain | Anekantavada x AI pluralism, Indian philosophy conferences |")
    L.append("")

    L.append("### Tier 3: Frontier (New Benchmark Development)")
    L.append("")
    L.append("Areas where benchmarks need to be created, not just found:")
    L.append("")
    L.append("1. **Buddhist Five Precepts Benchmark**: Structured ethical evaluation based on sila (moral conduct)")
    L.append("2. **Ubuntu Communitarian Ethics**: Evaluating LLM responses for communal wellbeing over individual rights")
    L.append("3. **Confucian Role Ethics**: Testing LLMs' understanding of relational obligations (ruler-subject, parent-child, etc.)")
    L.append("4. **Indigenous CARE Principles**: Evaluating AI systems against Collective benefit, Authority, Responsibility, Ethics")
    L.append("5. **Interfaith Moral Reasoning**: Cross-traditional evaluation where the 'right' answer depends on the ethical framework")
    L.append("")
    L.append("---")
    L.append("")

    # APPENDIX A: Full Tradition Paper Lists
    L.append("## Appendix A: Full Tradition Paper Lists")
    L.append("")

    for t in sorted(ALL_TRADITIONS, key=lambda x: -religious_counts.get(x, 0)):
        if t == "Multiple Religions":
            continue
        pc = religious_counts.get(t, 0)
        if pc == 0:
            L.append(f"### {t} (0 papers)")
            L.append("")
            L.append("*No papers currently tagged with this tradition.*")
            L.append("")
            continue

        L.append(f"### {t} ({pc} papers)")
        L.append("")
        papers_for_t = tradition_papers.get(t, [])
        benchmarks_for_t = set(tradition_benchmarks.get(t, []))

        for fn in sorted(papers_for_t):
            marker = " **[BENCHMARK]**" if fn in benchmarks_for_t else ""
            L.append(f"- {make_wikilink(fn)}{marker}")
        L.append("")

    # Multiple Religions
    mr_papers = tradition_papers.get("Multiple Religions", [])
    if mr_papers:
        L.append(f"### Multiple Religions ({len(mr_papers)} papers)")
        L.append("")
        for fn in sorted(mr_papers):
            L.append(f"- {make_wikilink(fn)}")
        L.append("")

    L.append("---")
    L.append("")

    # APPENDIX B: Search Query Archive
    L.append("## Appendix B: Search Query Archive")
    L.append("")
    L.append("### R-Agent Search Reports")
    L.append("")
    L.append("Full search methodology and queries are documented in the following agent reports:")
    L.append("")
    for report in sorted(r_agent_reports):
        L.append(f"- `{report.name}`")
    L.append("")

    L.append("### Keyword Patterns Used")
    L.append("")
    L.append("| Tradition | Pattern Count | Sample Patterns |")
    L.append("|-----------|--------------|-----------------|")
    for t in sorted(RELIGIOUS_PATTERNS.keys()):
        patterns = RELIGIOUS_PATTERNS[t]
        samples = ", ".join(f"`{p}`" for p in patterns[:3])
        if len(patterns) > 3:
            samples += f" ... (+{len(patterns) - 3} more)"
        L.append(f"| {t} | {len(patterns)} | {samples} |")
    L.append("")

    L.append("---")
    L.append("")
    L.append(f"*Generated: 2026-02-15 | Script: `PYTHON/generate_tradition_gap_report.py` | "
             f"Papers: {total_papers} | Traditions: {len(ALL_TRADITIONS)}*")

    # ── Write output ──────────────────────────────────────────────────
    report = "\n".join(L)

    STATS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"  Size: {len(report):,} characters, {report.count(chr(10)):,} lines")

    # Verification
    print(f"\n=== SUMMARY ===")
    print(f"  Total papers:        {total_papers}")
    print(f"  Religious-tagged:    {tagged_count} ({tagged_count * 100 // total_papers}%)")
    print(f"  Traditions tracked:  {len(ALL_TRADITIONS)}")
    print(f"  Zero-benchmark:     {len(zero_bench)}")
    print(f"  Benchmark papers:    {len(benchmark_papers)}")
    print(f"  R-agent reports:     {len(r_agent_reports)}")
    if audit_data:
        print(f"  Audit candidates:    {audit_data['metadata']['candidate_count']}")


if __name__ == "__main__":
    main()
