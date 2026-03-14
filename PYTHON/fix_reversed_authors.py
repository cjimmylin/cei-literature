#!/usr/bin/env python3
"""
Fix Reversed Author Names (Group 2a from Cat A triage)

Un-reverses "Last, First" → "First Last" in:
  - authors YAML field
  - first_author / last_author fields (wikilink format)
  - Author profile filenames (mv, not delete)

YAML Safety: re.subn() + re.MULTILINE, atomic writes, quote validation.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/fix_reversed_authors.py --dry-run
    ../.venv/bin/python PYTHON/fix_reversed_authors.py
"""

import argparse
import functools
import json
import os
import re
import shutil
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")
LOG_FILE = LOGS_DIR / f"{DATE_PREFIX}-reversed_authors_fixed.json"


def extract_frontmatter_parts(content: str):
    """Split content into (frontmatter, body). Returns None if no frontmatter."""
    fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return None
    return fm_match.group(1), content[fm_match.end():]


def reassemble(frontmatter: str, body: str) -> str:
    return f"---\n{frontmatter}\n---\n{body}"


def validate_yaml_quotes(frontmatter: str) -> bool:
    for line in frontmatter.split('\n'):
        if line.count('"') % 2 != 0:
            return False
    return True


def atomic_write(path: Path, content: str):
    tmp = path.with_suffix(f".tmp.{os.getpid()}")
    tmp.write_text(content, encoding='utf-8')
    os.replace(str(tmp), str(path))


def replace_in_field(frontmatter: str, field: str, old_str: str, new_str: str) -> tuple:
    """Replace old_str with new_str within a specific YAML field's value.
    Returns (new_frontmatter, was_changed)."""
    pattern = rf'^({re.escape(field)}:\s*)(.+)$'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if not match:
        return frontmatter, False

    old_value = match.group(2)
    new_value = old_value.replace(old_str, new_str)
    if new_value == old_value:
        return frontmatter, False

    full_old = match.group(0)
    full_new = match.group(1) + new_value
    result = frontmatter.replace(full_old, full_new, 1)
    return result, True


def main():
    parser = argparse.ArgumentParser(description="Fix reversed author names")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # Load triage data
    candidates = sorted(LOGS_DIR.glob("*-cat_a_triage.json"), reverse=True)
    if not candidates:
        print("ERROR: No triage file found. Run triage_cat_a_authors.py first.")
        sys.exit(1)

    triage_path = candidates[0]
    print(f"Loading triage: {triage_path.name}")

    with open(triage_path, 'r', encoding='utf-8') as f:
        triage = json.load(f)

    group2a = triage["groups"].get("2a_format_fix", [])
    print(f"Group 2a entries: {len(group2a)}")

    # Build unique name mappings: reversed → unreversed
    name_map = {}  # reversed_name → unreversed_name
    for entry in group2a:
        reversed_name = entry["author_name"]
        unreversed_name = entry["fix_info"]["unreversed_name"]
        name_map[reversed_name] = unreversed_name

    print(f"Unique reversed names to fix: {len(name_map)}")

    # Group entries by paper for efficient I/O
    paper_entries = defaultdict(list)
    for entry in group2a:
        paper_entries[entry["filename"]].append(entry)

    # --- Phase 1: Fix YAML fields ---
    print(f"\n--- Phase 1: Fix YAML fields ({'DRY RUN' if args.dry_run else 'LIVE'}) ---")
    yaml_stats = {"fixed": 0, "skipped": 0, "errors": 0, "details": []}

    for filename, entries in sorted(paper_entries.items()):
        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            yaml_stats["errors"] += 1
            yaml_stats["details"].append({"paper": filename, "error": "file not found"})
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            yaml_stats["errors"] += 1
            continue

        frontmatter, body = parts
        modified = False
        replacements = []

        for entry in entries:
            old_name = entry["author_name"]
            new_name = entry["fix_info"]["unreversed_name"]

            # Replace in authors field
            frontmatter, changed = replace_in_field(frontmatter, "authors", old_name, new_name)
            if changed:
                modified = True
                replacements.append((old_name, new_name, "authors"))

            # Replace in first_author (handles wikilink: [[Holyoak, Keith J.]])
            frontmatter, changed = replace_in_field(frontmatter, "first_author", old_name, new_name)
            if changed:
                modified = True
                replacements.append((old_name, new_name, "first_author"))

            # Replace in last_author
            frontmatter, changed = replace_in_field(frontmatter, "last_author", old_name, new_name)
            if changed:
                modified = True
                replacements.append((old_name, new_name, "last_author"))

        if modified:
            if not validate_yaml_quotes(frontmatter):
                yaml_stats["errors"] += 1
                yaml_stats["details"].append({"paper": filename, "error": "quote validation"})
                continue

            if not args.dry_run:
                atomic_write(paper_path, reassemble(frontmatter, body))

            yaml_stats["fixed"] += 1
            yaml_stats["details"].append({
                "paper": filename,
                "replacements": replacements,
                "dry_run": args.dry_run,
            })
        else:
            yaml_stats["skipped"] += 1

    print(f"  Papers fixed: {yaml_stats['fixed']}")
    print(f"  Papers skipped (already correct): {yaml_stats['skipped']}")
    print(f"  Errors: {yaml_stats['errors']}")

    # --- Phase 2: Rename author profiles ---
    print(f"\n--- Phase 2: Rename author profiles ({'DRY RUN' if args.dry_run else 'LIVE'}) ---")
    profile_stats = {"renamed": 0, "already_correct": 0, "errors": 0, "details": []}

    existing_profiles = set(f.stem for f in AUTHORS_DIR.iterdir() if f.suffix == '.md')

    for reversed_name, unreversed_name in sorted(name_map.items()):
        reversed_path = AUTHORS_DIR / f"{reversed_name}.md"
        unreversed_path = AUTHORS_DIR / f"{unreversed_name}.md"

        if reversed_path.exists() and not unreversed_path.exists():
            # Need to rename (mv, not delete!)
            if not args.dry_run:
                # Also update the name field inside the profile
                profile_content = reversed_path.read_text(encoding='utf-8')
                profile_content = profile_content.replace(reversed_name, unreversed_name)
                unreversed_path.write_text(profile_content, encoding='utf-8')
                # Move old to RECYCLE-BIN (never delete)
                recycle_dir = PAPERS_DIR.parent.parent / "RECYCLE-BIN"
                recycle_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(reversed_path), str(recycle_dir / reversed_path.name))

            profile_stats["renamed"] += 1
            profile_stats["details"].append({
                "old": reversed_name,
                "new": unreversed_name,
                "action": "renamed",
                "dry_run": args.dry_run,
            })
            print(f"  RENAME: {reversed_name} → {unreversed_name}")

        elif unreversed_path.exists():
            profile_stats["already_correct"] += 1

        elif reversed_path.exists() and unreversed_path.exists():
            # Both exist — need manual merge
            profile_stats["errors"] += 1
            profile_stats["details"].append({
                "old": reversed_name,
                "new": unreversed_name,
                "error": "both profiles exist — manual merge needed",
            })
            print(f"  CONFLICT: both {reversed_name}.md and {unreversed_name}.md exist")

        else:
            profile_stats["errors"] += 1
            profile_stats["details"].append({
                "old": reversed_name,
                "new": unreversed_name,
                "error": "neither profile exists",
            })

    print(f"  Renamed: {profile_stats['renamed']}")
    print(f"  Already correct: {profile_stats['already_correct']}")
    print(f"  Errors: {profile_stats['errors']}")

    # Save log
    log = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "dry_run": args.dry_run,
            "triage_source": triage_path.name,
        },
        "summary": {
            "unique_names": len(name_map),
            "papers_fixed": yaml_stats["fixed"],
            "profiles_renamed": profile_stats["renamed"],
        },
        "yaml_fixes": yaml_stats,
        "profile_renames": profile_stats,
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nLog saved: {LOG_FILE.name}")


if __name__ == "__main__":
    main()
