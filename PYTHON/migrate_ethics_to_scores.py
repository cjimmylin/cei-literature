#!/usr/bin/env python3
"""
Batch Migration: Ethics Yes/No → 0-100 Confidence Scores

For each paper:
1. Read title + abstract from frontmatter (read-only parse)
2. Load extract via ethics_scoring.load_extract()
3. Check for user-reviewed pin via ethics_scoring.get_pinned_score()
4. If pinned, use pinned score; else compute via compute_all_scores()
5. Write unquoted integer via safe_yaml_set_int() (regex, no rebuild round-trip)
6. Track disagreements: old=Yes but new<50, or old=No but new>=50

Usage:
    python migrate_ethics_to_scores.py --dry-run
    python migrate_ethics_to_scores.py
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, STATISTICS_DIR, LOGS_DIR
from yaml_utils import extract_frontmatter, parse_frontmatter
from ethics_scoring import (
    parse_ethics_value,
    compute_all_scores,
    get_pinned_score,
    safe_yaml_set_int,
    load_extract,
    ETHICS_FIELDS,
)


def is_already_int(raw_value):
    """Check if a raw YAML value is already an integer (not Yes/No/Unknown)."""
    if raw_value is None or raw_value == "":
        return False
    s = str(raw_value).strip().strip('"').strip("'")
    try:
        int(s)
        return True
    except ValueError:
        return False


def detect_disagreement(field, old_raw, new_score):
    """
    Return a disagreement dict if old label and new score disagree, else None.

    Disagreements:
        old=Yes but new_score < 50
        old=No  but new_score >= 50
    """
    s = str(old_raw).strip().strip('"').strip("'").lower()
    if s == "yes" and new_score < 50:
        return {"field": field, "old": "Yes", "new_score": new_score, "type": "Yes→low"}
    if s == "no" and new_score >= 50:
        return {"field": field, "old": "No", "new_score": new_score, "type": "No→high"}
    return None


def migrate_paper(filepath, dry_run=False, force=False):
    """
    Migrate a single paper from Yes/No to integer scores.

    Args:
        filepath: Path to paper .md file.
        dry_run: If True, don't write changes.
        force: If True, re-score even if already integer (for title-bug rescore).

    Returns:
        dict with keys: filename, changes, disagreements, pinned, error
    """
    filename = filepath.name
    stem = filepath.stem
    result = {
        "filename": filename,
        "changes": [],
        "disagreements": [],
        "pinned": [],
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

    title = fields.get("short_title", "")
    abstract = fields.get("abstract", "")

    # Load extract
    extract = load_extract(stem)

    # Compute algorithm scores
    algo_scores = compute_all_scores(title, abstract, extract)

    # Determine final scores per field
    final_scores = {}
    for field in ETHICS_FIELDS:
        pinned = get_pinned_score(filename, field)
        if pinned is not None:
            final_scores[field] = pinned
            result["pinned"].append({"field": field, "score": pinned})
        else:
            final_scores[field] = algo_scores[field]

    # Check for disagreements and gather changes
    old_values = {f: fields.get(f, "") for f in ETHICS_FIELDS}

    any_change = False
    for field in ETHICS_FIELDS:
        old_raw = old_values[field]
        new_score = final_scores[field]

        # Check disagreement (only meaningful for Yes/No values)
        dis = detect_disagreement(field, old_raw, new_score)
        if dis:
            dis["filename"] = filename
            result["disagreements"].append(dis)

        # Check if change is needed
        if not force and is_already_int(old_raw) and int(str(old_raw).strip().strip('"').strip("'")) == new_score:
            continue  # Already correct integer

        result["changes"].append({
            "field": field,
            "old": old_raw,
            "new": new_score,
        })
        any_change = True

    if not any_change:
        result["skipped"] = True
        return result

    # Apply changes via safe regex replacement (CLAUDE.md rule #2)
    if not dry_run:
        # Re-read content fresh for writing
        content = filepath.read_text(encoding="utf-8")

        # Split at first closing ---
        if not content.startswith("---"):
            result["error"] = "No frontmatter marker"
            return result

        # Find the closing --- to split fm from rest
        import re
        close_match = re.search(r'\n---\s*\n', content[3:])
        if not close_match:
            result["error"] = "No closing frontmatter marker"
            return result

        end_pos = close_match.start() + 3
        fm = content[3:end_pos]
        rest = content[end_pos:]  # from closing \n---\n onward

        for field in ETHICS_FIELDS:
            new_score = final_scores[field]
            fm, was_replaced = safe_yaml_set_int(fm, field, new_score)
            if not was_replaced:
                # Field doesn't exist yet — skip (don't add new fields)
                pass

        # Reconstruct: "---" + fm + rest
        new_content = "---" + fm + rest
        filepath.write_text(new_content, encoding="utf-8")

    return result


def main():
    parser = argparse.ArgumentParser(description="Migrate ethics Yes/No to 0-100 scores")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without modifying files")
    parser.add_argument("--force", action="store_true", help="Re-score all papers even if already integer (for title-bug rescore)")
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
    pinned_count = 0

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
            if result["pinned"]:
                pinned_count += 1

        all_disagreements.extend(result["disagreements"])

        if i % 200 == 0:
            print(f"  ... processed {i}/{len(paper_files)}")

    # ── Write disagreements ──────────────────────────────────────────
    STATISTICS_DIR.mkdir(parents=True, exist_ok=True)
    dis_suffix = "ethics-rescore-disagreements" if args.force else "migration-disagreements"
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
    log_suffix = "ethics-rescore-log" if args.force else "ethics-score-migration"
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
        "pinned_papers": pinned_count,
        "total_disagreements": len(all_disagreements),
        "entries": log_entries,
    }
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_output, f, indent=2, ensure_ascii=False)

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Migration complete.")
    print(f"  Total papers:    {len(paper_files)}")
    print(f"  Changed:         {changed_count}")
    print(f"  Skipped (no-op): {skipped_count}")
    print(f"  Errors:          {error_count}")
    print(f"  Pinned (user):   {pinned_count}")
    print(f"  Disagreements:   {len(all_disagreements)}")
    print(f"\n  Disagreements: {dis_path}")
    print(f"  Migration log: {log_path}")


if __name__ == "__main__":
    main()
