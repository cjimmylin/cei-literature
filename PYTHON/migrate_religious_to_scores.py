#!/usr/bin/env python3
"""
Batch Migration: Add rv_* score fields between religious_values and religious_values_list

For each paper:
1. Read title + abstract from frontmatter (read-only parse)
2. Load extract via load_extract()
3. Compute scores via compute_all_rv_scores()
4. Check if rv_* fields already exist (skip if already migrated)
5. Insert 14 new rv_* fields between religious_values: and religious_values_list:
6. Update religious_values: and religious_values_list: with derived strings
7. Track disagreements: old had tradition X but new score < 50, or old N/A but new >= 50

Usage:
    python migrate_religious_to_scores.py --dry-run
    python migrate_religious_to_scores.py
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
from religious_scoring import (
    RV_FIELDS,
    FIELD_DISPLAY_NAMES,
    DISPLAY_NAME_TO_FIELD,
    compute_all_rv_scores,
    load_extract,
    derive_religious_values_string,
    derive_religious_values_list_string,
    insert_rv_fields_between_religious_values,
    update_existing_rv_fields,
    parse_religious_values_string,
    parse_rv_value,
)


def has_rv_fields(fields):
    """Check if rv_* fields already exist in parsed frontmatter."""
    return any(fields.get(f, "") != "" for f in RV_FIELDS)


def detect_disagreements(old_traditions, scores):
    """
    Compare old religious_values traditions with new scores.

    Returns list of disagreement dicts:
    - Old had tradition X but new score < 50
    - Old was N/A (empty) but new score >= 50 for some tradition
    """
    disagreements = []

    # Map old traditions to their field names
    old_fields = set()
    for trad in old_traditions:
        field = DISPLAY_NAME_TO_FIELD.get(trad)
        if field:
            old_fields.add(field)

    for field in RV_FIELDS:
        score = scores.get(field, 0)
        display = FIELD_DISPLAY_NAMES[field]

        if field in old_fields and score < 50:
            disagreements.append({
                "field": field,
                "tradition": display,
                "old": "present",
                "new_score": score,
                "type": "present->low",
            })
        elif field not in old_fields and score >= 50:
            disagreements.append({
                "field": field,
                "tradition": display,
                "old": "absent",
                "new_score": score,
                "type": "absent->high",
            })

    return disagreements


def detect_rescore_disagreements(old_scores, new_scores):
    """
    Compare old and new rv_* scores for re-scoring.

    Returns list of disagreements where a field crosses the 50-threshold boundary.
    """
    disagreements = []
    for field in RV_FIELDS:
        old_val = old_scores.get(field, 0)
        new_val = new_scores.get(field, 0)
        old_detected = old_val >= 50
        new_detected = new_val >= 50

        if old_detected != new_detected:
            disagreements.append({
                "field": field,
                "tradition": FIELD_DISPLAY_NAMES[field],
                "old_score": old_val,
                "new_score": new_val,
                "type": "detected->undetected" if old_detected else "undetected->detected",
            })
    return disagreements


def migrate_paper(filepath, dry_run=False, force=False):
    """
    Migrate a single paper: add rv_* fields between religious_values and religious_values_list.
    With --force: re-score existing rv_* fields using corrected title extraction.

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

    already_migrated = has_rv_fields(fields)

    # Skip if already migrated and not forcing re-score
    if already_migrated and not force:
        result["skipped"] = True
        return result

    title = fields.get("short_title", "")
    abstract = fields.get("abstract", "")

    # Load extract
    extract = load_extract(stem)

    # Compute scores
    scores = compute_all_rv_scores(title, abstract, extract)

    if already_migrated and force:
        # Re-scoring path: compare old rv_* scores with new ones
        old_scores = {f: parse_rv_value(fields.get(f, 0)) for f in RV_FIELDS}

        disags = detect_rescore_disagreements(old_scores, scores)
        for d in disags:
            d["filename"] = filename
        result["disagreements"] = disags

        # Record changes (only fields that actually changed)
        for field in RV_FIELDS:
            old_val = old_scores[field]
            new_val = scores[field]
            if old_val != new_val:
                result["changes"].append({
                    "field": field,
                    "old_score": old_val,
                    "new_score": new_val,
                })

        # Skip write if no scores changed
        if not result["changes"]:
            result["skipped"] = True
            return result

        # Apply re-scoring
        if not dry_run:
            content = filepath.read_text(encoding="utf-8")

            if not content.startswith("---"):
                result["error"] = "No frontmatter marker"
                return result

            close_match = re.search(r'\n---\s*\n', content[3:])
            if not close_match:
                result["error"] = "No closing frontmatter marker"
                return result

            end_pos = close_match.start() + 3
            fm = content[3:end_pos]
            rest = content[end_pos:]

            new_fm = update_existing_rv_fields(fm, scores)

            new_content = "---" + new_fm + rest

            tmp_path = filepath.with_suffix(f".tmp.{os.getpid()}.md")
            tmp_path.write_text(new_content, encoding="utf-8")
            os.replace(str(tmp_path), str(filepath))

    else:
        # Initial migration path (no existing rv_* fields)
        old_rv_raw = fields.get("religious_values", "")
        old_rvl_raw = fields.get("religious_values_list", "")

        old_traditions = parse_religious_values_string(old_rvl_raw or old_rv_raw)

        disags = detect_disagreements(old_traditions, scores)
        for d in disags:
            d["filename"] = filename
            d["old_religious_values"] = old_rv_raw
            d["old_religious_values_list"] = old_rvl_raw
        result["disagreements"] = disags

        new_rv = derive_religious_values_string(scores)
        new_rvl = derive_religious_values_list_string(scores)
        for field in RV_FIELDS:
            result["changes"].append({
                "field": field,
                "new_score": scores[field],
            })
        result["changes"].append({
            "field": "religious_values",
            "old": old_rv_raw,
            "new": new_rv,
        })
        result["changes"].append({
            "field": "religious_values_list",
            "old": old_rvl_raw,
            "new": new_rvl,
        })

        if not dry_run:
            content = filepath.read_text(encoding="utf-8")

            if not content.startswith("---"):
                result["error"] = "No frontmatter marker"
                return result

            close_match = re.search(r'\n---\s*\n', content[3:])
            if not close_match:
                result["error"] = "No closing frontmatter marker"
                return result

            end_pos = close_match.start() + 3
            fm = content[3:end_pos]
            rest = content[end_pos:]

            new_fm, success = insert_rv_fields_between_religious_values(fm, scores)

            if not success:
                result["error"] = "religious_values_list field not found in frontmatter"
                return result

            new_content = "---" + new_fm + rest

            tmp_path = filepath.with_suffix(f".tmp.{os.getpid()}.md")
            tmp_path.write_text(new_content, encoding="utf-8")
            os.replace(str(tmp_path), str(filepath))

    return result


def main():
    parser = argparse.ArgumentParser(description="Add rv_* score fields to all papers")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without modifying files")
    parser.add_argument("--force", action="store_true",
                        help="Re-score existing rv_* fields (e.g. after fixing title extraction)")
    args = parser.parse_args()

    today = date.today().isoformat()
    today_compact = today.replace("-", "")

    # Choose output filenames based on mode
    if args.force:
        dis_name = f"{today_compact}-rv-rescore-disagreements.json"
        log_name = f"{today_compact}-rv-rescore-log.json"
        mode_label = "Re-scoring"
    else:
        dis_name = f"{today_compact}-rv-migration-disagreements.json"
        log_name = f"{today_compact}-religious-migration.json"
        mode_label = "Migrating"

    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    print(f"{'[DRY RUN] ' if args.dry_run else ''}{mode_label} {len(paper_files)} papers ...")

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
    dis_path = STATISTICS_DIR / dis_name
    dis_output = {
        "date": today,
        "mode": "rescore" if args.force else "migration",
        "dry_run": args.dry_run,
        "total_disagreements": len(all_disagreements),
        "disagreements": all_disagreements,
    }
    with open(dis_path, "w", encoding="utf-8") as f:
        json.dump(dis_output, f, indent=2, ensure_ascii=False)

    # ── Write log ─────────────────────────────────────────────────────
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOGS_DIR / log_name

    # Compact results for the log (only papers with changes or errors)
    log_entries = [r for r in all_results if not r["skipped"] or r["error"]]

    log_output = {
        "date": today,
        "mode": "rescore" if args.force else "migration",
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
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}{mode_label} complete.")
    print(f"  Total papers:    {len(paper_files)}")
    print(f"  Changed:         {changed_count}")
    print(f"  Skipped:         {skipped_count}")
    print(f"  Errors:          {error_count}")
    print(f"  Disagreements:   {len(all_disagreements)}")
    print(f"\n  Disagreements: {dis_path}")
    print(f"  Log: {log_path}")


if __name__ == "__main__":
    main()
