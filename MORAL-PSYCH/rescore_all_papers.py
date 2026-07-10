#!/usr/bin/env python3
"""
Re-score all vault papers with expanded moral psychology keyword patterns.

Reads each paper's YAML frontmatter + PDF extract, computes fresh mp_* scores
using the expanded patterns in moral_psych_scoring.py, and updates papers
where scores changed.

Safety: Uses regex-only YAML updates (CLAUDE.md rule #2). Validates after.

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python MORAL-PSYCH/rescore_all_papers.py
"""
from __future__ import annotations

import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_DIR = SCRIPT_DIR.parent  # CEI-Lit-WS/
sys.path.insert(0, str(WS_DIR / "PYTHON"))
sys.path.insert(0, str(WS_DIR / ".agent" / "lib"))

from moral_psych_scoring import (
    MP_FIELDS,
    compute_all_mp_scores,
    update_existing_mp_fields,
    parse_mp_value,
)

PAPERS_DIR = WS_DIR / "papers"
EXTRACTS_DIR = WS_DIR / "PDF Extracts"
OUTPUT_DIR = SCRIPT_DIR  # MORAL-PSYCH/
DATE_PREFIX = "20260403"


def extract_field(text: str, key: str) -> str:
    """Extract a YAML field value from frontmatter text."""
    m = re.search(
        rf'^{re.escape(key)}:\s*"?((?:[^"\n\\]|\\.)*)"?\s*$',
        text, re.MULTILINE,
    )
    return m.group(1).strip().strip('"') if m else ""


def extract_int_field(text: str, key: str) -> int:
    """Extract an integer YAML field."""
    val = extract_field(text, key)
    return parse_mp_value(val)


def load_extract(stem: str) -> str:
    """Load PDF extract text for a paper (scan year subdirs)."""
    if not EXTRACTS_DIR.exists():
        return ""
    for year_dir in sorted(EXTRACTS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        candidate = year_dir / f"{stem}.md"
        if candidate.exists():
            try:
                content = candidate.read_text(encoding="utf-8")
                # Strip frontmatter
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        content = content[end + 3:]
                return content[:25000]  # 25K chars per memory note
            except Exception:
                return ""
    return ""


def get_frontmatter(content: str) -> tuple[str, str]:
    """Split file into (frontmatter_text, rest_of_file)."""
    if not content.startswith("---"):
        return "", content
    end = content.find("---", 3)
    if end == -1:
        return "", content
    fm = content[3:end].strip()
    rest = content[end:]
    return fm, rest


def main():
    start = time.time()
    papers = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Scanning {len(papers)} papers...")

    changes = []
    theory_before = defaultdict(int)
    theory_after = defaultdict(int)
    errors = []
    unchanged = 0
    updated = 0

    for i, paper_path in enumerate(papers):
        if (i + 1) % 200 == 0:
            print(f"  ... {i + 1}/{len(papers)}")

        try:
            content = paper_path.read_text(encoding="utf-8")
        except Exception as e:
            errors.append({"file": paper_path.name, "error": str(e)})
            continue

        fm, rest = get_frontmatter(content)
        if not fm:
            continue

        # Extract current scores
        old_scores = {}
        for field in MP_FIELDS:
            old_scores[field] = extract_int_field(fm, field)

        # Count before
        for field in MP_FIELDS:
            if old_scores[field] >= 50:
                theory_before[field] += 1

        # Get title, abstract, extract
        title = extract_field(fm, "short_title") or extract_field(fm, "title")
        abstract = extract_field(fm, "abstract")
        stem = paper_path.stem
        extract = load_extract(stem)

        # Compute new scores
        new_scores = compute_all_mp_scores(title, abstract, extract)

        # Count after
        for field in MP_FIELDS:
            if new_scores[field] >= 50:
                theory_after[field] += 1

        # Check for changes
        changed_fields = {}
        for field in MP_FIELDS:
            if new_scores[field] != old_scores[field]:
                changed_fields[field] = {
                    "old": old_scores[field],
                    "new": new_scores[field],
                }

        if not changed_fields:
            unchanged += 1
            continue

        # Update the file
        new_fm = update_existing_mp_fields(fm, new_scores)
        new_content = f"---\n{new_fm}\n{rest}"
        paper_path.write_text(new_content, encoding="utf-8")
        updated += 1

        changes.append({
            "file": paper_path.name,
            "changed_fields": changed_fields,
            "new_detected": [
                f for f in MP_FIELDS
                if new_scores[f] >= 50 and old_scores[f] < 50
            ],
            "lost_detected": [
                f for f in MP_FIELDS
                if new_scores[f] < 50 and old_scores[f] >= 50
            ],
        })

    elapsed = time.time() - start

    # Build report
    report = {
        "rescore_date": DATE_PREFIX,
        "total_papers": len(papers),
        "updated": updated,
        "unchanged": unchanged,
        "errors": len(errors),
        "elapsed_seconds": round(elapsed, 1),
        "theory_detection_before": dict(theory_before),
        "theory_detection_after": dict(theory_after),
        "theory_detection_delta": {
            field: theory_after[field] - theory_before[field]
            for field in MP_FIELDS
        },
        "changes": changes[:200],  # Cap for file size
        "error_details": errors,
    }

    report_path = OUTPUT_DIR / f"{DATE_PREFIX}-rescore-report.json"
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\nDone in {elapsed:.1f}s. Updated {updated}/{len(papers)} papers.")
    print(f"Report: {report_path}")
    print("\nTheory detection changes (papers >= 50):")
    for field in MP_FIELDS:
        before = theory_before[field]
        after = theory_after[field]
        delta = after - before
        marker = f" (+{delta})" if delta > 0 else f" ({delta})" if delta < 0 else ""
        print(f"  {field}: {before} → {after}{marker}")


if __name__ == "__main__":
    main()
