#!/usr/bin/env python3
"""
Generate per-framework audit packets for Council Deliberation #2 (Phase 1A).

For each of 7 non-Western frameworks, produces a markdown audit file showing:
- Top-20 papers by score (plus all papers with score >= 50)
- Keyword hit details (strong, medium, FP matches)
- FP candidates (score >= 50 but strong_count == 0)
- Borderline papers (score 40-49)
- Current keyword lists

Output: CULTURAL-GLOBAL/COUNCIL/20260403-audit-{framework}.md
"""
from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent  # CULTURAL-GLOBAL/SCRIPTS/ → CEI-Lit-WS/
_PYTHON_DIR = _CEI_LIT_WS / "PYTHON"
_AGENT_LIB = _CEI_LIT_WS / ".agent" / "lib"
sys.path.insert(0, str(_PYTHON_DIR))
sys.path.insert(0, str(_AGENT_LIB))

from nonwestern_scoring import (
    FIELD_KEYWORDS as _MODULE_FIELD_KEYWORDS,
    NW_FIELDS_LIST as _MODULE_FIELDS,
    TITLE_PATTERNS as _MODULE_TITLE_PATTERNS,
    compute_nw_score,
)
from ethics_scoring import count_matches, load_extract
from config import PAPERS_DIR

# =====================================================================
# CONSTANTS
# =====================================================================

DATA_FILE = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "DATA" / "20260403-nw-scores.json"
COUNCIL_DIR = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "COUNCIL"

# The JSON data may use nw_islamic_jurisprudence while the scoring module
# uses nw_islamic_ethics. Map between them dynamically.
_FIELD_RENAMES = {
    "nw_islamic_jurisprudence": "nw_islamic_ethics",
    "nw_islamic_ethics": "nw_islamic_ethics",
}

# NW_FIELDS will be populated from the JSON data at runtime (see main()).
NW_FIELDS: list[str] = []


def _module_field(json_field: str) -> str:
    """Map JSON field name to scoring module field name."""
    return _FIELD_RENAMES.get(json_field, json_field)


def _get_field_keywords(json_field: str) -> dict:
    """Get keyword dict from module using JSON field name."""
    return _MODULE_FIELD_KEYWORDS[_module_field(json_field)]


def _get_title_pattern(json_field: str):
    """Get title pattern from module using JSON field name."""
    return _MODULE_TITLE_PATTERNS[_module_field(json_field)]


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

FRAMEWORK_REVIEWERS = {
    "nw_confucian": "Prof. Chenyang Li, Dr. Pak-Hang Wong",
    "nw_ubuntu": "Dr. Amara Osei-Mensah, Dr. Abeba Birhane",
    "nw_islamic_jurisprudence": "Prof. Yusuf al-Qaradawi Jr., Dr. Reza Shaker",
    "nw_islamic_ethics": "Prof. Yusuf al-Qaradawi Jr., Dr. Reza Shaker",
    "nw_buddhist": "Dr. Sonam Wangchuk, Dr. Thida Khin",
    "nw_dharmic": "Dr. Priya Narayan, Dr. Ravindra Kumar",
    "nw_indigenous_relational": "Dr. Tane Mahuta-Rau",
    "nw_buen_vivir": "Dr. Maria Soledad Vega",
}


# =====================================================================
# HELPERS
# =====================================================================

def _load_paper_text(filename: str) -> tuple[str, str, str]:
    """Load title, abstract, and combined text for a paper.

    Returns (title, abstract, full_text).
    """
    paper_path = PAPERS_DIR / filename
    if not paper_path.exists():
        return "", "", ""

    content = paper_path.read_text(encoding="utf-8", errors="replace")

    title_m = re.search(r'^short_title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    title = title_m.group(1) if title_m else ""

    abstract_m = re.search(r'^abstract:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    abstract = abstract_m.group(1) if abstract_m else ""

    stem = paper_path.stem
    extract = load_extract(stem)

    full_text = f"{title} {abstract} {extract}"
    return title, abstract, full_text


def _get_keyword_details(text: str, title: str, field: str) -> dict:
    """Get detailed match information for a paper against a framework.

    `field` is the JSON field name (e.g. nw_islamic_ethics).
    """
    kw = _get_field_keywords(field)

    strong_count, strong_terms = count_matches(text, kw["strong"])
    medium_count, medium_terms = count_matches(text, kw["medium"])
    fp_count, fp_terms = count_matches(text, kw["fp"])

    title_bonus = 0
    if title and _get_title_pattern(field).search(title):
        title_bonus = 20

    return {
        "strong_count": strong_count,
        "strong_terms": strong_terms,
        "medium_count": medium_count,
        "medium_terms": medium_terms,
        "fp_count": fp_count,
        "fp_terms": fp_terms,
        "title_bonus": title_bonus,
    }


def _term_summary(terms: list[str]) -> str:
    """Summarize matched terms with counts, e.g. 'karuna (x2), metta (x1)'."""
    if not terms:
        return "none"
    from collections import Counter
    counts = Counter(terms)
    parts = [f"{t} (x{c})" for t, c in counts.most_common()]
    return ", ".join(parts)


def _pattern_to_readable(pattern: str) -> str:
    """Convert a regex pattern to a more human-readable form."""
    # Strip word boundary markers
    s = pattern.replace(r"\b", "")
    # Strip common regex artifacts
    s = s.replace(r"\w*", "*")
    s = s.replace(r"\w+", "*")
    s = s.replace(r"\s+", " ")
    s = s.replace(r"\s*", " ")
    # Remove lookahead/lookbehind notation but keep content hints
    s = re.sub(r'\(\?[=!<].*?\)', '...', s)
    # Clean up
    s = s.replace("(?:", "(")
    s = s.replace(r"['\u2019]?", "'")
    return s.strip()


# =====================================================================
# MAIN
# =====================================================================

def main():
    global NW_FIELDS

    print("Loading NW scores data...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    papers = data["papers"]
    print(f"Loaded {len(papers)} papers from {DATA_FILE.name}")

    # Auto-detect field names from JSON data
    if papers:
        NW_FIELDS = [k for k in papers[0]["scores"].keys() if k.startswith("nw_")]
    print(f"Fields from JSON: {NW_FIELDS}")

    COUNCIL_DIR.mkdir(parents=True, exist_ok=True)

    for field in NW_FIELDS:
        display_name = FRAMEWORK_DISPLAY[field]
        reviewers = FRAMEWORK_REVIEWERS[field]
        print(f"\nProcessing {display_name} ({field})...")

        # Gather papers with scores for this field
        scored = []
        for p in papers:
            score = p["scores"].get(field, 0)
            scored.append({"filename": p["filename"], "score": score})

        # Sort descending by score
        scored.sort(key=lambda x: x["score"], reverse=True)

        # Detected papers (>= 50)
        detected = [p for p in scored if p["score"] >= 50]
        # Top-20 (may overlap with detected)
        top20 = scored[:20]
        # Merge: all detected + top-20 (union, maintaining order by score)
        seen = set()
        audit_papers = []
        for p in detected:
            if p["filename"] not in seen:
                audit_papers.append(p)
                seen.add(p["filename"])
        for p in top20:
            if p["filename"] not in seen:
                audit_papers.append(p)
                seen.add(p["filename"])

        # Borderline papers (40-49)
        borderline = [p for p in scored if 40 <= p["score"] <= 49]

        # Compute mean of detected
        detected_mean = 0.0
        if detected:
            detected_mean = sum(p["score"] for p in detected) / len(detected)

        # Now get keyword details for audit papers + borderline
        papers_needing_details = set()
        for p in audit_papers:
            papers_needing_details.add(p["filename"])
        for p in borderline:
            papers_needing_details.add(p["filename"])

        print(f"  Detected (>=50): {len(detected)}, Borderline: {len(borderline)}")
        print(f"  Loading keyword details for {len(papers_needing_details)} papers...")

        # Cache text loads and keyword details
        detail_cache: dict[str, dict] = {}
        title_cache: dict[str, str] = {}
        for filename in papers_needing_details:
            title, abstract, full_text = _load_paper_text(filename)
            title_cache[filename] = title
            detail_cache[filename] = _get_keyword_details(full_text, title, field)

        # Identify FP candidates: detected (>=50) but strong_count == 0
        fp_candidates = []
        for p in detected:
            details = detail_cache.get(p["filename"])
            if details and details["strong_count"] == 0:
                fp_candidates.append(p)

        # ── Build markdown ──────────────────────────────────────────
        lines = []
        lines.append(f"# Framework Audit: {display_name}")
        lines.append("")
        lines.append(f"**Reviewers:** {reviewers}")
        lines.append(f"**Papers detected (>=50):** {len(detected)}")
        lines.append(f"**Mean score (among detected):** {detected_mean:.1f}")
        lines.append(f"**FP candidates (>=50, strong=0):** {len(fp_candidates)}")
        lines.append(f"**Borderline (40-49):** {len(borderline)}")
        lines.append("")

        # ── Top-Scoring Papers Table ────────────────────────────────
        lines.append("## Top-Scoring Papers")
        lines.append("")
        lines.append("| # | Paper | Score | Strong Hits | Medium Hits | FP Penalty | Title Bonus |")
        lines.append("|---|-------|-------|-------------|-------------|------------|-------------|")

        for i, p in enumerate(audit_papers, 1):
            fn = p["filename"]
            details = detail_cache.get(fn, {})
            sc = p["score"]
            strong = details.get("strong_count", 0)
            medium = details.get("medium_count", 0)
            fp = details.get("fp_count", 0)
            tb = "Yes" if details.get("title_bonus", 0) > 0 else "No"
            # Truncate filename for table readability
            fn_display = fn[:70] + "..." if len(fn) > 73 else fn
            lines.append(f"| {i} | {fn_display} | {sc} | {strong} | {medium} | {fp} | {tb} |")

        lines.append("")

        # ── Keyword Details for Top Papers ──────────────────────────
        lines.append("### Keyword Details for Top Papers")
        lines.append("")

        for p in audit_papers:
            fn = p["filename"]
            details = detail_cache.get(fn, {})
            title = title_cache.get(fn, "")
            lines.append(f"**Paper: {fn}**")
            if title:
                lines.append(f"- Title: {title}")
            lines.append(f"- Score: {p['score']}")
            lines.append(f"- Strong matches: {_term_summary(details.get('strong_terms', []))}")
            lines.append(f"- Medium matches: {_term_summary(details.get('medium_terms', []))}")
            lines.append(f"- FP context: {_term_summary(details.get('fp_terms', []))}")
            tb = details.get("title_bonus", 0)
            lines.append(f"- Title bonus: {tb}")
            lines.append("")

        # ── FP Candidates ───────────────────────────────────────────
        lines.append("## FP Candidates (score >=50, strong_count=0)")
        lines.append("")
        if fp_candidates:
            lines.append("These papers rely entirely on medium matches and/or title bonus.")
            lines.append("")
            lines.append("| # | Paper | Score | Medium Hits | FP Penalty | Title Bonus |")
            lines.append("|---|-------|-------|-------------|------------|-------------|")
            for i, p in enumerate(fp_candidates, 1):
                fn = p["filename"]
                details = detail_cache.get(fn, {})
                sc = p["score"]
                medium = details.get("medium_count", 0)
                fp = details.get("fp_count", 0)
                tb = "Yes" if details.get("title_bonus", 0) > 0 else "No"
                fn_display = fn[:70] + "..." if len(fn) > 73 else fn
                lines.append(f"| {i} | {fn_display} | {sc} | {medium} | {fp} | {tb} |")
            lines.append("")

            # Details for FP candidates
            lines.append("### FP Candidate Details")
            lines.append("")
            for p in fp_candidates:
                fn = p["filename"]
                details = detail_cache.get(fn, {})
                title = title_cache.get(fn, "")
                lines.append(f"**Paper: {fn}**")
                if title:
                    lines.append(f"- Title: {title}")
                lines.append(f"- Score: {p['score']}")
                lines.append(f"- Medium matches: {_term_summary(details.get('medium_terms', []))}")
                lines.append(f"- FP context: {_term_summary(details.get('fp_terms', []))}")
                lines.append("")
        else:
            lines.append("No FP candidates found (all detected papers have at least one strong match).")
            lines.append("")

        # ── Borderline Papers ───────────────────────────────────────
        lines.append("## Borderline Papers (score 40-49)")
        lines.append("")
        if borderline:
            lines.append("These near-miss papers may be false negatives.")
            lines.append("")
            lines.append("| # | Paper | Score | Strong Hits | Medium Hits | FP Penalty | Title Bonus |")
            lines.append("|---|-------|-------|-------------|-------------|------------|-------------|")
            for i, p in enumerate(borderline, 1):
                fn = p["filename"]
                details = detail_cache.get(fn, {})
                sc = p["score"]
                strong = details.get("strong_count", 0)
                medium = details.get("medium_count", 0)
                fp = details.get("fp_count", 0)
                tb = "Yes" if details.get("title_bonus", 0) > 0 else "No"
                fn_display = fn[:70] + "..." if len(fn) > 73 else fn
                lines.append(f"| {i} | {fn_display} | {sc} | {strong} | {medium} | {fp} | {tb} |")
            lines.append("")

            # Details for borderline
            lines.append("### Borderline Paper Details")
            lines.append("")
            for p in borderline:
                fn = p["filename"]
                details = detail_cache.get(fn, {})
                title = title_cache.get(fn, "")
                lines.append(f"**Paper: {fn}**")
                if title:
                    lines.append(f"- Title: {title}")
                lines.append(f"- Score: {p['score']}")
                lines.append(f"- Strong matches: {_term_summary(details.get('strong_terms', []))}")
                lines.append(f"- Medium matches: {_term_summary(details.get('medium_terms', []))}")
                lines.append(f"- FP context: {_term_summary(details.get('fp_terms', []))}")
                lines.append("")
        else:
            lines.append("No borderline papers found.")
            lines.append("")

        # ── Current Keyword Lists ───────────────────────────────────
        kw = _get_field_keywords(field)
        lines.append("## Current Keyword Lists")
        lines.append("")

        lines.append(f"### Strong Keywords ({len(kw['strong'])})")
        lines.append("")
        for pat in kw["strong"]:
            lines.append(f"- `{pat}`")
        lines.append("")

        lines.append(f"### Medium Keywords ({len(kw['medium'])})")
        lines.append("")
        for pat in kw["medium"]:
            lines.append(f"- `{pat}`")
        lines.append("")

        lines.append(f"### FP Exclusions ({len(kw['fp'])})")
        lines.append("")
        for pat in kw["fp"]:
            lines.append(f"- `{pat}`")
        lines.append("")

        # ── Write file ──────────────────────────────────────────────
        out_path = COUNCIL_DIR / f"20260403-audit-{field}.md"
        out_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"  Wrote: {out_path.name}")

    print("\nDone. All 7 audit files generated.")


if __name__ == "__main__":
    main()
