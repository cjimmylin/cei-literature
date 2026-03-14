#!/usr/bin/env python3
"""
Audit papers for religious tradition keywords beyond title+abstract.

Scans papers + PDF extracts using rv_* confidence scores (0-100) from
religious_scoring.py to find misclassified papers tagged N/A.

Updated 2026-03-13: Uses rv_* integer score fields instead of flat
RELIGIOUS_PATTERNS regex matching.
"""

import re
import json
import sys
import functools
from pathlib import Path
from collections import defaultdict

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
LOGS_DIR = WS_ROOT / "logs"
OUTPUT_FILE = LOGS_DIR / "20260215-religious_traditions_audit.json"

sys.path.insert(0, str(SCRIPT_DIR))
from yaml_frontmatter_utils import read_paper, parse_frontmatter
from religious_scoring import (
    RV_FIELDS, FIELD_DISPLAY_NAMES,
    compute_all_rv_scores, is_rv_detected, parse_rv_value,
    DEFAULT_THRESHOLD,
)


def extract_title(body):
    """Extract title from the '# Title' heading in the paper body."""
    match = re.search(r'^# (.+?)$', body, re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_abstract(body):
    """Extract abstract text from the '## Abstract' section in the paper body."""
    match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', body, re.DOTALL)
    return match.group(1).strip() if match else ""


def load_extract(extract_path_value):
    """Load PDF extract text given the pdf_extract YAML field value."""
    if not extract_path_value or extract_path_value in ("N/A", ""):
        return ""
    # Strip quotes
    clean = extract_path_value.strip('"').strip("'")
    # Validate it looks like a path (not abstract text accidentally stored in this field)
    if len(clean) > 200 or not clean.startswith("PDF Extracts/"):
        return ""
    full_path = WS_ROOT / clean
    if full_path.exists():
        try:
            return full_path.read_text(encoding="utf-8")
        except Exception:
            return ""
    return ""


def score_paper(title, abstract, extract_text):
    """Score paper against all traditions using rv_* confidence scores.

    Returns {field: {score, display_name}} for fields with score > 0.
    """
    rv_scores = compute_all_rv_scores(title, abstract, extract_text)
    results = {}
    for field in RV_FIELDS:
        score = rv_scores[field]
        if score > 0:
            results[field] = {
                "score": score,
                "display_name": FIELD_DISPLAY_NAMES[field],
                "detected": score >= DEFAULT_THRESHOLD,
            }
    return results


def main():
    papers = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Found {len(papers)} papers to audit")

    candidates = []
    all_matches = []
    tradition_counts = defaultdict(int)

    for i, paper in enumerate(papers):
        if (i + 1) % 200 == 0:
            print(f"  Processing {i+1}/{len(papers)}...")

        try:
            frontmatter, body = read_paper(paper)
            fields = parse_frontmatter(frontmatter)

            # Check current rv_* scores — paper is "N/A" if no rv_* field is detected
            current_detected = []
            for rv_field in RV_FIELDS:
                if is_rv_detected(fields.get(rv_field, 0)):
                    current_detected.append(FIELD_DISPLAY_NAMES[rv_field])
            current_religious = ", ".join(current_detected) if current_detected else "N/A"

            title = extract_title(body)
            abstract = extract_abstract(body)
            extract_text = load_extract(fields.get("pdf_extract", ""))

            scores = score_paper(title, abstract, extract_text)

            if not scores:
                continue

            max_score = max(s["score"] for s in scores.values())
            top_field = max(scores, key=lambda f: scores[f]["score"])

            # Record all matches regardless of current tag
            entry = {
                "filename": paper.name,
                "current_religious_values": current_religious,
                "rv_scores": {f: s["score"] for f, s in scores.items()},
                "traditions": {FIELD_DISPLAY_NAMES[f]: s for f, s in scores.items()},
                "max_score": max_score,
                "top_tradition": FIELD_DISPLAY_NAMES[top_field],
            }
            all_matches.append(entry)

            # Candidates: currently no rv_* detected but text scoring >= 50
            if not current_detected:
                high_scoring = {f: s for f, s in scores.items()
                                if s["score"] >= DEFAULT_THRESHOLD}
                if high_scoring:
                    entry["candidate_traditions"] = {
                        FIELD_DISPLAY_NAMES[f]: s for f, s in high_scoring.items()
                    }
                    candidates.append(entry)
                    for f in high_scoring:
                        tradition_counts[FIELD_DISPLAY_NAMES[f]] += 1

        except Exception as e:
            print(f"  Error processing {paper.name}: {e}")

    # Summary
    print(f"\n{'='*60}")
    print(f"AUDIT RESULTS")
    print(f"{'='*60}")
    print(f"  Papers scanned:     {len(papers)}")
    print(f"  Papers with ANY religious keyword: {len(all_matches)}")
    print(f"  Candidates (undetected, score>={DEFAULT_THRESHOLD}): {len(candidates)}")
    print(f"\n  Tradition breakdown (candidates):")
    for trad, count in sorted(tradition_counts.items(), key=lambda x: -x[1]):
        print(f"    {trad}: {count}")

    # Write output
    output = {
        "metadata": {
            "date": "2026-02-15",
            "papers_scanned": len(papers),
            "total_with_keywords": len(all_matches),
            "candidate_count": len(candidates),
            "threshold": DEFAULT_THRESHOLD,
            "scoring": "rv_* confidence scores (0-100)",
        },
        "tradition_counts": dict(tradition_counts),
        "candidates": candidates,
        "all_matches": all_matches,
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput: {OUTPUT_FILE}")
    print(f"  Size: {OUTPUT_FILE.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
