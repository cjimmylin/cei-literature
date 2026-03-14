#!/usr/bin/env python3
"""
Generate interactive HTML review pages for normative ethics YAML audit.

Tiers:
  1 — Papers with any framework field = "Yes" (virtue/deontological/utilitarian)
      Focus: confirming or revoking existing Yes tags (false-positive hunt)
  2 — Papers with ethics_overall="Yes" but all frameworks="No", filtered by
      normative-philosophy keywords in abstract/extract (false-negative hunt)
  3 — Papers with ethics_overall="No", filtered by ethics+normative keywords
      (missed-ethics-overall hunt)

Usage:
    python generate_normative_audit_pages.py --tier 1
    python generate_normative_audit_pages.py --tier 2
    python generate_normative_audit_pages.py --tier 3

Output:  STATISTICS/20260312-normative-audit-tier{N}-review.html
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

# Add paths for imports
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR
from ethics_scoring import is_ethics_yes, parse_ethics_value

# ── Keyword lists (imported from classify_ethics.py) ───────────────────
ETHICS_OVERALL_KEYWORDS = [
    r'\bethics?\b', r'\bethical\b', r'\bmoral\b', r'\bmorality\b', r'\bvalues?\b',
    r'\bnormative\b', r'\bfairness\b', r'\bjustice\b', r'\bbias\b', r'\bharm\b',
    r'\bsafety\b', r'\balignment\b', r'\bresponsible\b', r'\baccountable\b',
    r'\bhate speech\b', r'\btoxic\b', r'\boffensive\b', r'\babusive\b',
    r'\bstereotype\b', r'\bdiscrimination\b', r'\bhuman rights\b',
    r'\bprosocial\b', r'\bimmoral\b', r'\bunethical\b', r'\bwrongdoing\b',
    r'\bmoral reasoning\b', r'\bmoral judgment\b', r'\bmoral decision\b',
    r'\bmoral dilemma\b', r'\btrolley problem\b', r'\bmoral foundations\b',
]

VIRTUE_ETHICS_KEYWORDS = [
    r'\bvirtue\b', r'\bvirtuous\b', r'\bvirtue ethics\b', r'\bcharacter\b',
    r'\bexcellence\b', r'\bflourishing\b', r'\beudaimonia\b', r'\baristotel\w*\b',
    r'\bprudence\b', r'\btemperance\b', r'\bcourage\b', r'\bwisdom\b',
    r'\bphronesis\b', r'\barete\b', r'\bmoral character\b', r'\bmoral virtue\b',
]

DEONTOLOGICAL_KEYWORDS = [
    r'\bdeontolog\w*\b', r'\bduty\b', r'\bduties\b', r'\bkantian\b', r'\bkant\b',
    r'\bcategorical imperative\b', r'\bobligation\b', r'\brights-based\b',
    r'\brule-based\b', r'\buniversal\w* law\b', r'\bmoral law\b',
    r'\bmoral rules?\b', r'\bmoral principles?\b', r'\bmoral duty\b',
    r'\bimperative\b', r'\bintrinsic\w* wrong\b', r'\bintrinsic\w* right\b',
]

UTILITARIAN_KEYWORDS = [
    r'\butilitarian\w*\b', r'\bconsequential\w*\b', r'\butility\b',
    r'\bmaximize?\b', r'\bmaximis\w*\b', r'\bgreatest good\b', r'\bwelfare\b',
    r'\boutcome-based\b', r'\bcost-benefit\b', r'\bwell-being\b', r'\bwellbeing\b',
    r'\bbeneficence\b', r'\bharm reduction\b', r'\bnet benefit\b',
    r'\bgreatest happiness\b', r'\bgreatest number\b', r'\bmill\b', r'\bbentham\b',
    r'\bhedonism\b', r'\bhedonistic\b',
]

# Normative philosophy keywords (from screen_normative_ethics_candidates.py LEG1)
NORMATIVE_KEYWORDS = [
    r"\bdeontolog\w*\b", r"\bkantian\b", r"\bcategorical imperative\b",
    r"\bduty-based\b", r"\brights-based\b", r"\brossian\b",
    r"\bprima facie dut\w*\b", r"\butilitarian\w*\b", r"\bconsequentialis\w*\b",
    r"\bbentham\b", r"\bsidgwick\b", r"\bgreatest good\b", r"\bhedonic calculus\b",
    r"\bvirtue ethic\w*\b", r"\baristotel\w*\b", r"\beudaimonia\b", r"\bphronesis\b",
    r"\bcare ethic\w*\b", r"\bnormative ethic\w*\b", r"\bnormative framework\b",
    r"\bnormative theor\w*\b", r"\bmoral theor\w*\b", r"\bethical theor\w*\b",
    r"\bmoral philosophy\b",
]

HIGH_YIELD_PERSPECTIVES = {
    "Moral Reasoning & Psychology", "Machine Ethics", "Applied Ethics", "General Ethics",
}


def find_keyword_matches(text, patterns):
    """Return list of (keyword, start, end) tuples for all matches."""
    text_lower = text.lower()
    matches = []
    seen = set()
    for pat in patterns:
        for m in re.finditer(pat, text_lower):
            key = (m.group(), m.start(), m.end())
            if key not in seen:
                seen.add(key)
                matches.append({"word": m.group(), "start": m.start(), "end": m.end()})
    return matches


def highlight_text(text, all_matches, max_chars=2000):
    """Return HTML with keyword matches highlighted, truncated to max_chars."""
    if not text:
        return "<em>(no text available)</em>"

    truncated = len(text) > max_chars
    text = text[:max_chars]

    # Collect matches within range, sort by position
    relevant = [m for m in all_matches if m["start"] < max_chars]
    relevant.sort(key=lambda m: m["start"], reverse=True)

    escaped = html.escape(text)
    # Apply highlights from end to start so positions stay valid
    for m in relevant:
        s, e = m["start"], min(m["end"], max_chars)
        before = html.escape(text[:s])
        word = html.escape(text[s:e])
        after = html.escape(text[e:])
        escaped = before + f'<mark>{word}</mark>' + after

    if truncated:
        escaped += '<span class="truncated">... [truncated]</span>'

    return escaped


def load_extract_body(paper_stem):
    """Load first ~500 words of extract body for a paper."""
    for year_dir in sorted(PDF_EXTRACTS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        candidate = year_dir / f"{paper_stem}.md"
        if candidate.exists():
            try:
                content = candidate.read_text(encoding="utf-8")
                # Strip YAML frontmatter
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        content = content[end + 3:]
                # Get body text, skip headers/metadata lines
                lines = []
                word_count = 0
                for line in content.split("\n"):
                    if word_count >= 500:
                        break
                    lines.append(line)
                    word_count += len(line.split())
                return "\n".join(lines)
            except Exception:
                return ""
    return ""


def load_all_papers():
    """Load all papers and return list of dicts with parsed fields."""
    papers = []
    for paper_path in sorted(PAPERS_DIR.iterdir()):
        if not paper_path.is_file() or paper_path.suffix != ".md":
            continue
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception:
            continue
        try:
            fm_text, body = extract_frontmatter(content)
        except (ValueError, Exception):
            continue

        fields = parse_frontmatter(fm_text)
        abstract = fields.get("abstract", "").strip().strip('"').strip("'")

        papers.append({
            "filename": paper_path.name,
            "stem": paper_path.stem,
            "year": fields.get("year", ""),
            "title": fields.get("short_title", paper_path.stem).strip('"').strip("'"),
            "abstract": abstract,
            "ethics_overall": fields.get("ethics_overall", "").strip('"'),
            "virtue_ethics": fields.get("virtue_ethics", "").strip('"'),
            "deontological_ethics": fields.get("deontological_ethics", "").strip('"'),
            "utilitarian_ethics": fields.get("utilitarian_ethics", "").strip('"'),
            "ethics_perspective": fields.get("ethics_perspective", "").strip('"'),
            "human_view": fields.get("Human View", ""),
        })
    return papers


def filter_tier1(papers):
    """Tier 1: any framework = Yes."""
    result = []
    for p in papers:
        if is_ethics_yes(p["virtue_ethics"]) or is_ethics_yes(p["deontological_ethics"]) or is_ethics_yes(p["utilitarian_ethics"]):
            # Flag inconsistency: framework=Yes but ethics_overall=No
            p["flagged"] = (not is_ethics_yes(p["ethics_overall"]))
            result.append(p)
    # Flagged first, then by year
    result.sort(key=lambda x: (not x["flagged"], x.get("year", ""), x["filename"]))
    return result


def filter_tier2(papers):
    """Tier 2: ethics_overall=Yes, all frameworks=No, keyword-filtered."""
    candidates = []
    for p in papers:
        if not is_ethics_yes(p["ethics_overall"]):
            continue
        if is_ethics_yes(p["virtue_ethics"]) or is_ethics_yes(p["deontological_ethics"]) or is_ethics_yes(p["utilitarian_ethics"]):
            continue
        candidates.append(p)

    # Pre-filter: check normative keywords or high-yield perspective
    result = []
    for p in candidates:
        text = (p["abstract"] + " " + load_extract_body(p["stem"])).lower()
        norm_matches = find_keyword_matches(text, NORMATIVE_KEYWORDS)
        has_perspective = p["ethics_perspective"] in HIGH_YIELD_PERSPECTIVES
        if norm_matches or has_perspective:
            p["flagged"] = has_perspective
            p["_prefilter_text"] = text
            result.append(p)

    result.sort(key=lambda x: (not x["flagged"], x.get("year", ""), x["filename"]))
    return result


def filter_tier3(papers):
    """Tier 3: ethics_overall=No, keyword-filtered."""
    candidates = [p for p in papers if not is_ethics_yes(p["ethics_overall"])]

    result = []
    for p in candidates:
        text = (p["abstract"] + " " + load_extract_body(p["stem"])).lower()
        ethics_matches = find_keyword_matches(text, ETHICS_OVERALL_KEYWORDS)
        norm_matches = find_keyword_matches(text, NORMATIVE_KEYWORDS)
        if ethics_matches or norm_matches:
            p["flagged"] = bool(norm_matches)
            p["_prefilter_text"] = text
            result.append(p)

    result.sort(key=lambda x: (not x["flagged"], x.get("year", ""), x["filename"]))
    return result


def build_paper_data(paper, tier):
    """Build JSON-serializable data dict for one paper."""
    abstract = paper["abstract"]
    extract_body = load_extract_body(paper["stem"])
    combined = abstract + " " + extract_body

    # Find keyword matches across all categories
    virtue_matches = find_keyword_matches(combined, VIRTUE_ETHICS_KEYWORDS)
    deont_matches = find_keyword_matches(combined, DEONTOLOGICAL_KEYWORDS)
    util_matches = find_keyword_matches(combined, UTILITARIAN_KEYWORDS)
    ethics_matches = find_keyword_matches(combined, ETHICS_OVERALL_KEYWORDS)
    norm_matches = find_keyword_matches(combined, NORMATIVE_KEYWORDS)

    return {
        "filename": paper["filename"],
        "year": str(paper["year"]),
        "title": paper["title"],
        "abstract": abstract,
        "extract_snippet": extract_body[:3000],
        "ethics_overall": paper["ethics_overall"],
        "virtue_ethics": paper["virtue_ethics"],
        "deontological_ethics": paper["deontological_ethics"],
        "utilitarian_ethics": paper["utilitarian_ethics"],
        "ethics_perspective": paper["ethics_perspective"],
        "flagged": paper.get("flagged", False),
        "virtue_matches": [m["word"] for m in virtue_matches],
        "deont_matches": [m["word"] for m in deont_matches],
        "util_matches": [m["word"] for m in util_matches],
        "ethics_matches": [m["word"] for m in ethics_matches],
        "norm_matches": [m["word"] for m in norm_matches],
    }


def generate_html(papers_data, tier, total_in_tier_pool):
    """Generate the complete HTML page."""
    tier_titles = {
        1: "Tier 1: Framework = Yes (False-Positive Audit)",
        2: "Tier 2: Ethics=Yes, Frameworks=No (False-Negative Hunt)",
        3: "Tier 3: Ethics=No (Missed Ethics Hunt)",
    }
    tier_descriptions = {
        1: f"All {total_in_tier_pool} papers with at least one framework field (virtue/deontological/utilitarian) = Yes. "
           "Papers flagged at top have framework=Yes but ethics_overall≠Yes (likely false positives).",
        2: f"Keyword-filtered subset of {total_in_tier_pool} papers with ethics_overall=Yes but all frameworks=No. "
           "Showing papers whose abstract/extract contains normative philosophy keywords or has high-yield ethics_perspective.",
        3: f"Keyword-filtered subset of {total_in_tier_pool} papers with ethics_overall=No. "
           "Showing papers whose abstract/extract contains ethics or normative keywords (potential missed classifications).",
    }

    papers_json = json.dumps(papers_data, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tier_titles[tier]}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f5f5f5; color: #333; }}
.header {{ background: #1a1a2e; color: white; padding: 20px 30px; position: sticky; top: 0; z-index: 100; }}
.header h1 {{ font-size: 1.3em; margin-bottom: 8px; }}
.header .meta {{ font-size: 0.85em; color: #aaa; }}
.controls {{ background: #16213e; padding: 12px 30px; display: flex; gap: 15px; align-items: center; flex-wrap: wrap; position: sticky; top: 72px; z-index: 99; }}
.controls label {{ color: #ccc; font-size: 0.85em; }}
.controls select, .controls input {{ padding: 4px 8px; border: 1px solid #444; border-radius: 4px; background: #0f3460; color: white; font-size: 0.85em; }}
.controls button {{ padding: 6px 16px; border: none; border-radius: 4px; cursor: pointer; font-size: 0.85em; font-weight: 600; }}
.btn-export {{ background: #e94560; color: white; }}
.btn-export:hover {{ background: #c73e54; }}
.btn-secondary {{ background: #533483; color: white; }}
.btn-secondary:hover {{ background: #6b44a0; }}
.progress {{ background: #0f3460; padding: 6px 30px; color: #4ecca3; font-size: 0.85em; font-weight: 600; position: sticky; top: 120px; z-index: 98; }}
.container {{ max-width: 1200px; margin: 20px auto; padding: 0 20px; }}
.paper {{ background: white; border-radius: 8px; margin-bottom: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden; }}
.paper.flagged {{ border-left: 4px solid #e94560; }}
.paper.reviewed {{ border-left: 4px solid #4ecca3; }}
.paper-header {{ padding: 16px 20px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }}
.paper-header:hover {{ background: #f8f8f8; }}
.paper-title {{ font-weight: 600; font-size: 1em; }}
.paper-year {{ color: #888; font-size: 0.85em; margin-left: 8px; }}
.paper-tags {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.tag {{ padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: 600; }}
.tag-yes {{ background: #d4edda; color: #155724; }}
.tag-no {{ background: #f8d7da; color: #721c24; }}
.tag-flagged {{ background: #fff3cd; color: #856404; }}
.tag-keyword {{ background: #cce5ff; color: #004085; }}
.paper-body {{ padding: 0 20px 20px; display: none; }}
.paper.open .paper-body {{ display: block; }}
.section {{ margin-bottom: 14px; }}
.section-title {{ font-weight: 600; font-size: 0.85em; color: #555; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }}
.text-content {{ font-size: 0.9em; line-height: 1.5; max-height: 200px; overflow-y: auto; padding: 10px; background: #fafafa; border-radius: 4px; white-space: pre-wrap; word-wrap: break-word; }}
.text-content mark {{ background: #fff176; padding: 1px 2px; border-radius: 2px; }}
.keywords-matched {{ display: flex; gap: 4px; flex-wrap: wrap; margin-top: 4px; }}
.decisions {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; padding: 14px; background: #f0f4ff; border-radius: 6px; }}
.decision-group {{ }}
.decision-group label {{ font-size: 0.85em; display: block; margin: 3px 0; cursor: pointer; }}
.decision-group .group-title {{ font-weight: 600; font-size: 0.8em; color: #444; text-transform: uppercase; margin-bottom: 4px; }}
.note-field {{ width: 100%; margin-top: 8px; padding: 6px; border: 1px solid #ddd; border-radius: 4px; font-size: 0.85em; }}
.truncated {{ color: #999; font-style: italic; }}
.hidden {{ display: none !important; }}
.review-status {{ font-size: 0.75em; padding: 2px 8px; border-radius: 10px; }}
.status-pending {{ background: #f8d7da; color: #721c24; }}
.status-done {{ background: #d4edda; color: #155724; }}
</style>
</head>
<body>

<div class="header">
    <h1>{tier_titles[tier]}</h1>
    <div class="meta">{tier_descriptions[tier]}<br>Generated: 2026-03-12 | Papers shown: {len(papers_data)}</div>
</div>

<div class="controls">
    <label>Filter: <select id="filterSelect">
        <option value="all">All papers</option>
        <option value="flagged">Flagged only</option>
        <option value="reviewed">Reviewed</option>
        <option value="pending">Pending review</option>
    </select></label>
    <label>Framework: <select id="frameworkFilter">
        <option value="all">All</option>
        <option value="virtue">Virtue Ethics</option>
        <option value="deontological">Deontological</option>
        <option value="utilitarian">Utilitarian</option>
    </select></label>
    <label>Year: <select id="yearFilter"><option value="all">All years</option></select></label>
    <label>Search: <input type="text" id="searchInput" placeholder="filename or title..." size="20"></label>
    <button class="btn-export" onclick="exportDecisions()">Export Decisions JSON</button>
    <button class="btn-secondary" onclick="expandAll()">Expand All</button>
    <button class="btn-secondary" onclick="collapseAll()">Collapse All</button>
    <button class="btn-secondary" onclick="importDecisions()">Import Decisions</button>
</div>

<div class="progress" id="progressBar">Reviewed: 0 / {len(papers_data)} (0%)</div>

<div class="container" id="papersContainer"></div>

<input type="file" id="importFile" accept=".json" style="display:none" onchange="handleImport(event)">

<script>
const PAPERS = {papers_json};
const TIER = {tier};
const decisions = {{}};

// ── Render ─────────────────────────────────────────────────────────
function escapeHtml(text) {{
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}}

function highlightKeywords(text, keywords) {{
    if (!text || !keywords || keywords.length === 0) return escapeHtml(text || '(no text)');
    let escaped = escapeHtml(text);
    const unique = [...new Set(keywords)];
    for (const kw of unique) {{
        const re = new RegExp('\\\\b' + kw.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&') + '\\\\b', 'gi');
        escaped = escaped.replace(re, '<mark>$&</mark>');
    }}
    return escaped;
}}

function truncate(text, maxLen) {{
    if (!text) return '';
    if (text.length <= maxLen) return text;
    return text.substring(0, maxLen) + '... [truncated]';
}}

function renderPaper(p, idx) {{
    const allKw = [...(p.virtue_matches||[]), ...(p.deont_matches||[]), ...(p.util_matches||[]), ...(p.ethics_matches||[]), ...(p.norm_matches||[])];
    const flagClass = p.flagged ? ' flagged' : '';
    const reviewedClass = decisions[p.filename] ? ' reviewed' : '';

    let tagsHtml = '';
    if (TIER === 1) {{
        if (p.virtue_ethics === 'Yes') tagsHtml += '<span class="tag tag-yes">Virtue:Yes</span>';
        if (p.deontological_ethics === 'Yes') tagsHtml += '<span class="tag tag-yes">Deont:Yes</span>';
        if (p.utilitarian_ethics === 'Yes') tagsHtml += '<span class="tag tag-yes">Util:Yes</span>';
        if (p.ethics_overall !== 'Yes') tagsHtml += '<span class="tag tag-flagged">Ethics:' + escapeHtml(p.ethics_overall || 'empty') + '</span>';
    }} else if (TIER === 2) {{
        tagsHtml += '<span class="tag tag-no">All frameworks: No</span>';
        if (p.ethics_perspective) tagsHtml += '<span class="tag tag-keyword">' + escapeHtml(p.ethics_perspective) + '</span>';
    }} else {{
        tagsHtml += '<span class="tag tag-no">Ethics: No</span>';
    }}

    // Keyword match badges
    if (p.virtue_matches && p.virtue_matches.length) tagsHtml += '<span class="tag tag-keyword">V:' + p.virtue_matches.length + '</span>';
    if (p.deont_matches && p.deont_matches.length) tagsHtml += '<span class="tag tag-keyword">D:' + p.deont_matches.length + '</span>';
    if (p.util_matches && p.util_matches.length) tagsHtml += '<span class="tag tag-keyword">U:' + p.util_matches.length + '</span>';
    if (p.norm_matches && p.norm_matches.length) tagsHtml += '<span class="tag tag-keyword">Norm:' + p.norm_matches.length + '</span>';

    const statusHtml = decisions[p.filename]
        ? '<span class="review-status status-done">reviewed</span>'
        : '<span class="review-status status-pending">pending</span>';

    // Decision radios depend on tier
    let decisionsHtml = '';
    if (TIER === 1) {{
        decisionsHtml = `
            ${{makeRadioGroup(p, 'virtue_ethics', 'Virtue Ethics', p.virtue_ethics === 'Yes' ? [['confirm_yes','Confirm Yes'],['change_no','Change to No']] : [['leave','Leave as ' + (p.virtue_ethics||'No')],['change_yes','Change to Yes']])}}
            ${{makeRadioGroup(p, 'deontological_ethics', 'Deontological', p.deontological_ethics === 'Yes' ? [['confirm_yes','Confirm Yes'],['change_no','Change to No']] : [['leave','Leave as ' + (p.deontological_ethics||'No')],['change_yes','Change to Yes']])}}
            ${{makeRadioGroup(p, 'utilitarian_ethics', 'Utilitarian', p.utilitarian_ethics === 'Yes' ? [['confirm_yes','Confirm Yes'],['change_no','Change to No']] : [['leave','Leave as ' + (p.utilitarian_ethics||'No')],['change_yes','Change to Yes']])}}
            ${{makeRadioGroup(p, 'ethics_overall', 'Ethics Overall', [['confirm','Confirm ' + (p.ethics_overall||'?')],['change_yes','Change to Yes'],['change_no','Change to No']])}}
        `;
    }} else if (TIER === 2) {{
        decisionsHtml = `
            ${{makeRadioGroup(p, 'virtue_ethics', 'Virtue Ethics', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
            ${{makeRadioGroup(p, 'deontological_ethics', 'Deontological', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
            ${{makeRadioGroup(p, 'utilitarian_ethics', 'Utilitarian', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
        `;
    }} else {{
        decisionsHtml = `
            ${{makeRadioGroup(p, 'ethics_overall', 'Ethics Overall', [['confirm_no','Confirm No'],['change_yes','Change to Yes']])}}
            ${{makeRadioGroup(p, 'virtue_ethics', 'Virtue Ethics', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
            ${{makeRadioGroup(p, 'deontological_ethics', 'Deontological', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
            ${{makeRadioGroup(p, 'utilitarian_ethics', 'Utilitarian', [['leave_no','Leave as No'],['tag_yes','Tag as Yes']])}}
        `;
    }}

    const existingNote = decisions[p.filename] ? (decisions[p.filename].note || '') : '';

    return `
    <div class="paper${{flagClass}}${{reviewedClass}}" data-filename="${{escapeHtml(p.filename)}}" data-year="${{p.year}}" data-flagged="${{p.flagged}}"
         data-virtue="${{p.virtue_ethics}}" data-deont="${{p.deontological_ethics}}" data-util="${{p.utilitarian_ethics}}" id="paper-${{idx}}">
        <div class="paper-header" onclick="togglePaper(${{idx}})">
            <div>
                <span class="paper-title">${{escapeHtml(p.title)}}</span>
                <span class="paper-year">${{p.year}}</span>
                ${{statusHtml}}
            </div>
            <div class="paper-tags">${{tagsHtml}}</div>
        </div>
        <div class="paper-body">
            <div class="section">
                <div class="section-title">File</div>
                <div style="font-size:0.85em;color:#666">${{escapeHtml(p.filename)}}</div>
            </div>
            <div class="section">
                <div class="section-title">Current Fields</div>
                <div style="font-size:0.85em">
                    ethics_overall: <strong>${{p.ethics_overall||'(empty)'}}</strong> |
                    virtue: <strong>${{p.virtue_ethics||'(empty)'}}</strong> |
                    deontological: <strong>${{p.deontological_ethics||'(empty)'}}</strong> |
                    utilitarian: <strong>${{p.utilitarian_ethics||'(empty)'}}</strong> |
                    perspective: <strong>${{p.ethics_perspective||'(empty)'}}</strong>
                </div>
            </div>
            <div class="section">
                <div class="section-title">Abstract</div>
                <div class="text-content">${{highlightKeywords(truncate(p.abstract, 2000), allKw)}}</div>
            </div>
            <div class="section">
                <div class="section-title">Extract Snippet (first ~500 words)</div>
                <div class="text-content">${{highlightKeywords(truncate(p.extract_snippet, 3000), allKw)}}</div>
            </div>
            <div class="section">
                <div class="section-title">Matched Keywords</div>
                <div class="keywords-matched">
                    ${{(p.virtue_matches||[]).map(k => '<span class="tag tag-keyword">V: '+escapeHtml(k)+'</span>').join('')}}
                    ${{(p.deont_matches||[]).map(k => '<span class="tag tag-keyword">D: '+escapeHtml(k)+'</span>').join('')}}
                    ${{(p.util_matches||[]).map(k => '<span class="tag tag-keyword">U: '+escapeHtml(k)+'</span>').join('')}}
                    ${{(p.norm_matches||[]).map(k => '<span class="tag tag-keyword">N: '+escapeHtml(k)+'</span>').join('')}}
                    ${{(p.ethics_matches||[]).map(k => '<span class="tag tag-keyword">E: '+escapeHtml(k)+'</span>').join('')}}
                </div>
            </div>
            <div class="section">
                <div class="section-title">Decisions</div>
                <div class="decisions">${{decisionsHtml}}</div>
                <input type="text" class="note-field" placeholder="Optional note..." data-filename="${{escapeHtml(p.filename)}}"
                       value="${{escapeHtml(existingNote)}}" onchange="updateNote(this)">
            </div>
        </div>
    </div>`;
}}

function makeRadioGroup(paper, field, label, options) {{
    const name = paper.filename + '__' + field;
    const existing = decisions[paper.filename] && decisions[paper.filename].changes && decisions[paper.filename].changes[field];
    let html = '<div class="decision-group"><div class="group-title">' + label + '</div>';
    for (const [val, text] of options) {{
        const checked = existing === val ? ' checked' : '';
        html += `<label><input type="radio" name="${{name}}" value="${{val}}"${{checked}} onchange="recordDecision('${{paper.filename}}','${{field}}','${{val}}')" /> ${{text}}</label>`;
    }}
    html += '</div>';
    return html;
}}

function togglePaper(idx) {{
    document.getElementById('paper-' + idx).classList.toggle('open');
}}

function expandAll() {{
    document.querySelectorAll('.paper:not(.hidden)').forEach(el => el.classList.add('open'));
}}

function collapseAll() {{
    document.querySelectorAll('.paper').forEach(el => el.classList.remove('open'));
}}

// ── Decision tracking ──────────────────────────────────────────────
function recordDecision(filename, field, value) {{
    if (!decisions[filename]) decisions[filename] = {{ changes: {{}}, note: '' }};
    decisions[filename].changes[field] = value;
    // Mark as reviewed
    const el = document.querySelector('[data-filename="' + CSS.escape(filename) + '"]');
    if (el) el.classList.add('reviewed');
    updateProgress();
}}

function updateNote(input) {{
    const fn = input.dataset.filename;
    if (!decisions[fn]) decisions[fn] = {{ changes: {{}}, note: '' }};
    decisions[fn].note = input.value;
}}

function updateProgress() {{
    const total = PAPERS.length;
    const reviewed = Object.keys(decisions).length;
    const pct = total > 0 ? Math.round(reviewed / total * 100) : 0;
    document.getElementById('progressBar').textContent = `Reviewed: ${{reviewed}} / ${{total}} (${{pct}}%)`;
}}

// ── Export/Import ──────────────────────────────────────────────────
function exportDecisions() {{
    // Convert decisions to the format expected by apply script
    const output = {{
        audit_tier: 'tier' + TIER,
        audit_date: '2026-03-12',
        decisions: []
    }};

    for (const [filename, dec] of Object.entries(decisions)) {{
        if (!dec.changes || Object.keys(dec.changes).length === 0) continue;

        // Convert radio values to actual YAML changes
        const changes = {{}};
        for (const [field, action] of Object.entries(dec.changes)) {{
            if (action === 'change_yes' || action === 'tag_yes') changes[field] = 'Yes';
            else if (action === 'change_no') changes[field] = 'No';
            // confirm_yes, confirm_no, leave_no, leave, confirm = no change needed
        }}

        if (Object.keys(changes).length > 0) {{
            output.decisions.push({{
                filename: filename,
                changes: changes,
                note: dec.note || ''
            }});
        }}
    }}

    const blob = new Blob([JSON.stringify(output, null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `20260312-normative-audit-tier${{TIER}}-decisions.json`;
    a.click();
    URL.revokeObjectURL(url);

    alert(`Exported ${{output.decisions.length}} changes (${{Object.keys(decisions).length}} papers reviewed)`);
}}

function importDecisions() {{
    document.getElementById('importFile').click();
}}

function handleImport(event) {{
    const file = event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function(e) {{
        try {{
            const data = JSON.parse(e.target.result);
            if (data.decisions) {{
                for (const dec of data.decisions) {{
                    decisions[dec.filename] = {{
                        changes: {{}},
                        note: dec.note || ''
                    }};
                    for (const [field, value] of Object.entries(dec.changes)) {{
                        if (value === 'Yes') decisions[dec.filename].changes[field] = TIER === 1 ? 'change_yes' : 'tag_yes';
                        else if (value === 'No') decisions[dec.filename].changes[field] = 'change_no';
                    }}
                }}
                renderAll();
                updateProgress();
                alert(`Imported decisions for ${{data.decisions.length}} papers`);
            }}
        }} catch (err) {{
            alert('Error parsing JSON: ' + err.message);
        }}
    }};
    reader.readAsText(file);
}}

// ── Filtering ──────────────────────────────────────────────────────
function applyFilters() {{
    const filterVal = document.getElementById('filterSelect').value;
    const fwVal = document.getElementById('frameworkFilter').value;
    const yearVal = document.getElementById('yearFilter').value;
    const search = document.getElementById('searchInput').value.toLowerCase();

    document.querySelectorAll('.paper').forEach(el => {{
        let show = true;
        const fn = el.dataset.filename.toLowerCase();
        const yr = el.dataset.year;
        const flagged = el.dataset.flagged === 'true';
        const reviewed = el.classList.contains('reviewed');

        if (filterVal === 'flagged' && !flagged) show = false;
        if (filterVal === 'reviewed' && !reviewed) show = false;
        if (filterVal === 'pending' && reviewed) show = false;

        if (fwVal === 'virtue' && el.dataset.virtue !== 'Yes') show = false;
        if (fwVal === 'deontological' && el.dataset.deont !== 'Yes') show = false;
        if (fwVal === 'utilitarian' && el.dataset.util !== 'Yes') show = false;

        if (yearVal !== 'all' && yr !== yearVal) show = false;
        if (search && !fn.includes(search)) show = false;

        el.classList.toggle('hidden', !show);
    }});
}}

document.getElementById('filterSelect').addEventListener('change', applyFilters);
document.getElementById('frameworkFilter').addEventListener('change', applyFilters);
document.getElementById('yearFilter').addEventListener('change', applyFilters);
document.getElementById('searchInput').addEventListener('input', applyFilters);

// ── Init ───────────────────────────────────────────────────────────
function renderAll() {{
    const container = document.getElementById('papersContainer');
    container.innerHTML = PAPERS.map((p, i) => renderPaper(p, i)).join('');
    // Populate year filter
    const years = [...new Set(PAPERS.map(p => p.year).filter(Boolean))].sort();
    const yearSel = document.getElementById('yearFilter');
    yearSel.innerHTML = '<option value="all">All years</option>';
    for (const y of years) {{
        yearSel.innerHTML += `<option value="${{y}}">${{y}}</option>`;
    }}
    // Restore reviewed state
    for (const fn of Object.keys(decisions)) {{
        const el = document.querySelector('[data-filename="' + CSS.escape(fn) + '"]');
        if (el) el.classList.add('reviewed');
    }}
    updateProgress();
}}

renderAll();
</script>
</body>
</html>'''


def main():
    parser = argparse.ArgumentParser(description="Generate normative ethics audit review pages")
    parser.add_argument("--tier", type=int, required=True, choices=[1, 2, 3])
    args = parser.parse_args()

    print(f"Loading all papers from {PAPERS_DIR}...")
    papers = load_all_papers()
    print(f"  Loaded {len(papers)} papers")

    if args.tier == 1:
        filtered = filter_tier1(papers)
        pool_size = len(filtered)
    elif args.tier == 2:
        # Count pool before filtering
        pool = [p for p in papers if is_ethics_yes(p["ethics_overall"]) and
                not is_ethics_yes(p["virtue_ethics"]) and not is_ethics_yes(p["deontological_ethics"]) and not is_ethics_yes(p["utilitarian_ethics"])]
        pool_size = len(pool)
        filtered = filter_tier2(papers)
    else:
        pool = [p for p in papers if not is_ethics_yes(p["ethics_overall"])]
        pool_size = len(pool)
        filtered = filter_tier3(papers)

    print(f"  Tier {args.tier}: {len(filtered)} papers (from pool of {pool_size})")
    flagged = sum(1 for p in filtered if p.get("flagged"))
    print(f"  Flagged: {flagged}")

    print("Building paper data (loading extracts)...")
    papers_data = []
    for i, p in enumerate(filtered):
        if (i + 1) % 50 == 0:
            print(f"  Processing {i+1}/{len(filtered)}...")
        papers_data.append(build_paper_data(p, args.tier))

    print("Generating HTML...")
    html_content = generate_html(papers_data, args.tier, pool_size)

    STATISTICS_DIR.mkdir(exist_ok=True)
    out_path = STATISTICS_DIR / f"20260312-normative-audit-tier{args.tier}-review.html"
    out_path.write_text(html_content, encoding="utf-8")
    print(f"\nOutput: {out_path}")
    print(f"  File size: {out_path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
