#!/usr/bin/env python3
"""
Screen new papers (DATE_ADDED: 20260207) for normative ethics benchmark candidates.

Three-leg keyword test:
  Leg 1 - Normative Ethics: explicit normative framework references
  Leg 2 - Benchmark/Dataset: structured evaluation artifact terms
  Leg 3 - LLM Testing: language model evaluation terms

Papers scoring 2+ legs are candidates for deep reading.

Input sources:
  - Papers WITH PDF extracts → full PDF extract text (body only, not YAML)
  - Papers WITHOUT PDF extracts → paper body text (NOT frontmatter field names)

Output: logs/20260207-normative_ethics_candidates_20260207.json
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional

# Add parent so we can import from .agent/lib
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR


# ── Leg 1: Normative Ethics keywords ──────────────────────────────────
# Specific normative philosophy terms — NOT generic "normative" or "ethics"
LEG1_PATTERNS = [
    r"\bdeontolog\w*\b",
    r"\bkantian\b",
    r"\bcategorical imperative\b",
    r"\bduty-based\b",
    r"\brights-based\b",
    r"\brossian\b",
    r"\bprima facie dut\w*\b",
    r"\butilitarian\w*\b",
    r"\bconsequentialis\w*\b",
    r"\bbentham\b",
    r"\bsidgwick\b",
    r"\bgreatest good\b",
    r"\bhedonic calculus\b",
    r"\bvirtue ethic\w*\b",
    r"\baristotel\w*\b",
    r"\beudaimonia\b",
    r"\bphronesis\b",
    r"\bcare ethic\w*\b",
    r"\bnormative ethic\w*\b",
    r"\bnormative framework\b",
    r"\bnormative theor\w*\b",
    r"\bmoral theor\w*\b",
    r"\bethical theor\w*\b",
    r"\bmoral philosophy\b",
]

# ── Leg 2: Benchmark / Dataset keywords ───────────────────────────────
LEG2_PATTERNS = [
    r"\bbenchmark\w*\b",
    r"\bdataset\w*\b",
    r"\btest suite\b",
    r"\bevaluation suite\b",
    r"\bscenario set\b",
    r"\bmoral dilemma\w*\b",
    r"\btrolley\b",
    r"\btest bed\b",
    r"\btestbed\b",
    r"\bevaluation dataset\b",
    r"\bcorpus\b",
]

# ── Leg 3: LLM Testing keywords ──────────────────────────────────────
LEG3_PATTERNS = [
    r"\bllm\w*\b",
    r"\blarge language model\w*\b",
    r"\bgpt[-‑]?\d\b",
    r"\bchatgpt\b",
    r"\bllama\b",
    r"\bgemini\b",
    r"\bmistral\b",
    r"\bfoundation model\w*\b",
    r"\blanguage model\w*\b",
    r"\bpalm\b",
    r"\bdeepseek\b",
    r"\bqwen\b",
]


def check_leg(text, patterns):
    """Return list of matched keywords for a leg."""
    text_lower = text.lower()
    matches = []
    for pat in patterns:
        m = re.search(pat, text_lower)
        if m:
            matches.append(m.group())
    return matches


def get_body_text(content):
    """Extract body text from a markdown file, stripping YAML frontmatter."""
    try:
        _fm, body = extract_frontmatter(content)
        return body
    except ValueError:
        # If no frontmatter, return entire content
        return content


def get_extract_path(paper_path, fm_text):
    """Resolve the PDF extract path for a paper."""
    fields = parse_frontmatter(fm_text)
    extract_ref = fields.get("pdf_extract", "")
    if extract_ref:
        extract_ref = extract_ref.strip('"').strip("'")
        extract_path = PAPERS_DIR.parent / extract_ref
        if extract_path.exists():
            return extract_path

    # Fallback: try matching filename
    stem = paper_path.stem
    candidate = PDF_EXTRACTS_DIR / "{}.md".format(stem)
    if candidate.exists():
        return candidate

    return None


def screen_papers():
    """Scan all new papers and identify candidates."""
    new_papers = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception:
            continue
        if "DATE_ADDED: 20260207" in content:
            new_papers.append(paper_path)

    print("Found {} new papers (DATE_ADDED: 20260207)".format(len(new_papers)))

    candidates = []
    no_extract = []

    for paper_path in new_papers:
        content = paper_path.read_text(encoding="utf-8")
        try:
            fm_text, body = extract_frontmatter(content)
        except ValueError:
            print("  WARN: Could not parse frontmatter: {}".format(paper_path.name))
            continue

        # Determine text to search — ALWAYS use body-only (no YAML field names)
        extract_path = get_extract_path(paper_path, fm_text)
        has_extract = extract_path is not None

        if has_extract:
            extract_content = extract_path.read_text(encoding="utf-8")
            search_text = get_body_text(extract_content)
        else:
            # Use paper body text only (no frontmatter field names)
            search_text = body
            no_extract.append(paper_path.name)

        # Also include abstract from frontmatter (a text field, not a field name)
        fields = parse_frontmatter(fm_text)
        abstract = fields.get("abstract", "")
        search_text = abstract + "\n" + search_text

        # Run three-leg test
        leg1_matches = check_leg(search_text, LEG1_PATTERNS)
        leg2_matches = check_leg(search_text, LEG2_PATTERNS)
        leg3_matches = check_leg(search_text, LEG3_PATTERNS)

        legs_hit = sum([bool(leg1_matches), bool(leg2_matches), bool(leg3_matches)])

        if legs_hit >= 2:
            candidates.append({
                "filename": paper_path.name,
                "legs_hit": legs_hit,
                "leg1_normative": leg1_matches,
                "leg2_benchmark": leg2_matches,
                "leg3_llm": leg3_matches,
                "has_pdf_extract": has_extract,
                "short_title": fields.get("short_title", paper_path.stem),
                "year": fields.get("year", ""),
                "first_author": fields.get("first_author", ""),
            })

    # Sort: 3-leg hits first, then by filename
    candidates.sort(key=lambda c: (-c["legs_hit"], c["filename"]))

    output = {
        "total_new_papers": len(new_papers),
        "total_candidates": len(candidates),
        "papers_without_extract": len(no_extract),
        "three_leg_hits": sum(1 for c in candidates if c["legs_hit"] == 3),
        "two_leg_hits": sum(1 for c in candidates if c["legs_hit"] == 2),
        "candidates": candidates,
        "no_extract_files": sorted(no_extract),
    }

    out_path = LOGS_DIR / "20260207-normative_ethics_candidates_20260207.json"
    LOGS_DIR.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("\nResults:")
    print("  Candidates (2+ legs): {}".format(len(candidates)))
    print("    3-leg hits: {}".format(output["three_leg_hits"]))
    print("    2-leg hits: {}".format(output["two_leg_hits"]))
    print("  Papers without PDF extract: {}".format(len(no_extract)))
    print("\nOutput: {}".format(out_path))

    print("\n" + "=" * 80)
    print("CANDIDATE LIST")
    print("=" * 80)
    for i, c in enumerate(candidates, 1):
        flag = "" if c["has_pdf_extract"] else " [NO EXTRACT]"
        print("  {:3d}. [{} legs] {}{}".format(i, c["legs_hit"], c["filename"], flag))
        print("       L1={}".format(c["leg1_normative"][:3]))
        print("       L2={}".format(c["leg2_benchmark"][:3]))
        print("       L3={}".format(c["leg3_llm"][:3]))

    return output


if __name__ == "__main__":
    screen_papers()
