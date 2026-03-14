#!/usr/bin/env python3
"""
Batch Migration: Add mp_* score fields before moral_psychology line

For each paper:
1. Read title + abstract from frontmatter (read-only parse)
2. Load extract via load_extract()
3. Compute scores via compute_all_mp_scores()
4. Check if mp_* fields already exist (skip if already migrated)
5. Insert 8 new mp_* fields before moral_psychology: line
6. Update moral_psychology: derived string from scores >= 50
7. Track disagreements: old had theory X but new score < 50, or old N/A but new >= 50

Usage:
    python migrate_moral_psych_to_scores.py --dry-run
    python migrate_moral_psych_to_scores.py
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, STATISTICS_DIR, LOGS_DIR
from yaml_utils import extract_frontmatter, parse_frontmatter
from moral_psych_scoring import (
    MP_FIELDS,
    FIELD_DISPLAY_NAMES,
    DISPLAY_NAME_TO_FIELD,
    compute_all_mp_scores,
    load_extract,
    derive_moral_psychology_string,
    insert_mp_fields_before_moral_psychology,
    update_existing_mp_fields,
    parse_moral_psychology_string,
)


def has_mp_fields(fields):
    """Check if mp_* fields already exist in parsed frontmatter."""
    return any(fields.get(f, "") != "" for f in MP_FIELDS)


def detect_disagreements(old_theories, scores):
    """
    Compare old moral_psychology theories with new scores.

    Returns list of disagreement dicts:
    - Old had theory X but new score < 50
    - Old was N/A (empty) but new score >= 50 for some theory
    """
    disagreements = []

    # Map old theories to their field names
    old_fields = set()
    for theory in old_theories:
        field = DISPLAY_NAME_TO_FIELD.get(theory)
        if field:
            old_fields.add(field)

    for field in MP_FIELDS:
        score = scores.get(field, 0)
        display = FIELD_DISPLAY_NAMES[field]

        if field in old_fields and score < 50:
            disagreements.append({
                "field": field,
                "theory": display,
                "old": "present",
                "new_score": score,
                "type": "present->low",
            })
        elif field not in old_fields and score >= 50:
            disagreements.append({
                "field": field,
                "theory": display,
                "old": "absent",
                "new_score": score,
                "type": "absent->high",
            })

    return disagreements


def migrate_paper(filepath, dry_run=False, force=False):
    """
    Migrate a single paper: add mp_* fields before moral_psychology line.

    Args:
        filepath: Path to paper .md file.
        dry_run: If True, don't write changes.
        force: If True, re-score existing mp_* fields (for title-bug rescore).

    Returns:
        dict with keys: filename, changes, disagreements, skipped, error
    """
    filename = filepath.name
    stem = filepath.stem
    result = {
        "filename": filename,
        "changes": [],
        "disagreements": [],
        "skipped": False,
        "error": None,
    }

    try:
        content = filepath.read_text(encoding="utf-8")
        fm_text, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm_text)
    except Exception as e:
        result["error"] = str(e)
        return result

    # Check if already migrated (skip unless --force)
    already_migrated = has_mp_fields(fields)
    if already_migrated and not force:
        result["skipped"] = True
        return result

    title = fields.get("short_title", "")
    abstract = fields.get("abstract", "")
    old_mp_raw = fields.get("moral_psychology", "")

    # Load extract
    extract = load_extract(stem)

    # Compute scores
    scores = compute_all_mp_scores(title, abstract, extract)

    # Parse old theories for disagreement detection
    old_theories = parse_moral_psychology_string(old_mp_raw)

    # Detect disagreements
    disags = detect_disagreements(old_theories, scores)
    for d in disags:
        d["filename"] = filename
        d["old_moral_psychology"] = old_mp_raw
    result["disagreements"] = disags

    # Record changes
    new_derived = derive_moral_psychology_string(scores)
    for field in MP_FIELDS:
        result["changes"].append({
            "field": field,
            "new_score": scores[field],
        })
    result["changes"].append({
        "field": "moral_psychology",
        "old": old_mp_raw,
        "new": new_derived,
    })

    # Apply changes
    if not dry_run:
        # Re-read content fresh for writing
        content = filepath.read_text(encoding="utf-8")

        if not content.startswith("---"):
            result["error"] = "No frontmatter marker"
            return result

        # CRITICAL: Correct frontmatter split (see CLAUDE.md bug prevention)
        close_match = re.search(r'\n---\s*\n', content[3:])
        if not close_match:
            result["error"] = "No closing frontmatter marker"
            return result

        end_pos = close_match.start() + 3
        fm = content[3:end_pos]
        rest = content[end_pos:]  # from closing \n---\n onward

        # Insert or update mp_* fields
        if already_migrated and force:
            # Re-score: update existing fields
            new_fm = update_existing_mp_fields(fm, scores)
            success = True
        else:
            # First migration: insert fields before moral_psychology line
            new_fm, success = insert_mp_fields_before_moral_psychology(fm, scores)

        if not success:
            result["error"] = "moral_psychology field not found in frontmatter"
            return result

        # Reconstruct: "---" + fm + rest
        new_content = "---" + new_fm + rest

        # Atomic write: PID-scoped temp file + os.replace()
        tmp_path = filepath.with_suffix(f".tmp.{os.getpid()}.md")
        tmp_path.write_text(new_content, encoding="utf-8")
        os.replace(str(tmp_path), str(filepath))

    return result


def main():
    parser = argparse.ArgumentParser(description="Add mp_* score fields to all papers")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without modifying files")
    parser.add_argument("--force", action="store_true", help="Re-score all papers even if already migrated (for title-bug rescore)")
    args = parser.parse_args()

    today = date.today().isoformat()
    today_compact = today.replace("-", "")

    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    print(f"{'[DRY RUN] ' if args.dry_run else ''}Migrating {len(paper_files)} papers ...")

    all_results = []
    all_disagreements = []
    changed_count = 0
    skipped_count = 0
    error_count = 0

    for i, pf in enumerate(paper_files, 1):
        result = migrate_paper(pf, dry_run=args.dry_run, force=args.force)
        all_results.append(result)

        if result["error"]:
            error_count += 1
            print(f"  ERROR [{i}] {pf.name}: {result['error']}")
        elif result["skipped"]:
            skipped_count += 1
        else:
            changed_count += 1

        all_disagreements.extend(result["disagreements"])

        if i % 200 == 0:
            print(f"  ... processed {i}/{len(paper_files)}")

    # ── Write disagreements ──────────────────────────────────────────
    STATISTICS_DIR.mkdir(parents=True, exist_ok=True)
    dis_suffix = "mp-rescore-disagreements" if args.force else "mp-migration-disagreements"
    dis_path = STATISTICS_DIR / f"{today_compact}-{dis_suffix}.json"
    dis_output = {
        "date": today,
        "dry_run": args.dry_run,
        "total_disagreements": len(all_disagreements),
        "disagreements": all_disagreements,
    }
    with open(dis_path, "w", encoding="utf-8") as f:
        json.dump(dis_output, f, indent=2, ensure_ascii=False)

    # ── Write migration log ──────────────────────────────────────────
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_suffix = "mp-rescore-log" if args.force else "moral-psych-migration"
    log_path = LOGS_DIR / f"{today_compact}-{log_suffix}.json"

    # Compact results for the log (only papers with changes or errors)
    log_entries = [r for r in all_results if not r["skipped"] or r["error"]]

    log_output = {
        "date": today,
        "dry_run": args.dry_run,
        "total_papers": len(paper_files),
        "changed": changed_count,
        "skipped": skipped_count,
        "errors": error_count,
        "total_disagreements": len(all_disagreements),
        "entries": log_entries,
    }
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_output, f, indent=2, ensure_ascii=False)

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Migration complete.")
    print(f"  Total papers:    {len(paper_files)}")
    print(f"  Changed:         {changed_count}")
    print(f"  Skipped (already migrated): {skipped_count}")
    print(f"  Errors:          {error_count}")
    print(f"  Disagreements:   {len(all_disagreements)}")
    print(f"\n  Disagreements: {dis_path}")
    print(f"  Migration log: {log_path}")


if __name__ == "__main__":
    main()
