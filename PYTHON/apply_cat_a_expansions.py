#!/usr/bin/env python3
"""
Apply Cat A Author Expansions

Reads the expansion results and applies resolved abbreviated → full name
replacements in paper YAML fields (authors, first_author, last_author).

Handles both Group 2b (reversed+abbreviated) and Group 3 (initials-only) names.
For Group 2b, the original name is in "Surname, Initial." format in the YAML.

YAML Safety: re.subn() + re.MULTILINE, atomic writes, quote validation.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/apply_cat_a_expansions.py --dry-run
    ../.venv/bin/python PYTHON/apply_cat_a_expansions.py
"""

import argparse
import functools
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

DATE_PREFIX = datetime.now().strftime("%Y%m%d")
LOG_FILE = LOGS_DIR / f"{DATE_PREFIX}-cat_a_expansions_applied.json"


def extract_frontmatter_parts(content):
    fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return None
    return fm_match.group(1), content[fm_match.end():]


def reassemble(frontmatter, body):
    return f"---\n{frontmatter}\n---\n{body}"


def validate_yaml_quotes(frontmatter):
    for line in frontmatter.split('\n'):
        if line.count('"') % 2 != 0:
            return False
    return True


def atomic_write(path, content):
    tmp = path.with_suffix(f".tmp.{os.getpid()}")
    tmp.write_text(content, encoding='utf-8')
    os.replace(str(tmp), str(path))


def replace_in_field(frontmatter, field, old_str, new_str):
    """Replace old_str with new_str within a specific YAML field's value."""
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
    parser = argparse.ArgumentParser(description="Apply abbreviated author expansions")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # Load expansion results
    candidates = sorted(LOGS_DIR.glob("*-cat_a_expansion_results.json"), reverse=True)
    if not candidates:
        print("ERROR: No expansion results found. Run expand_cat_a_authors.py first.")
        sys.exit(1)

    results_path = candidates[0]
    print(f"Loading expansion results: {results_path.name}")

    with open(results_path, 'r', encoding='utf-8') as f:
        expansion_data = json.load(f)

    # Filter to resolved entries only
    resolved = [r for r in expansion_data["results"] if r["status"] == "resolved"]
    print(f"Resolved entries to apply: {len(resolved)}")

    # Group by paper for efficient I/O
    paper_updates = defaultdict(list)
    for r in resolved:
        for paper_ref in r["papers"]:
            paper_updates[paper_ref["filename"]].append({
                "original_name": r["original_name"],
                "resolved_name": r["resolved_name"],
                "group": r["group"],
            })

    print(f"Papers to update: {len(paper_updates)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}\n")

    stats = {"fixed": 0, "skipped": 0, "errors": 0, "details": []}

    for filename, updates in sorted(paper_updates.items()):
        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            stats["errors"] += 1
            stats["details"].append({"paper": filename, "error": "file not found"})
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        modified = False
        replacements = []

        for upd in updates:
            old_name = upd["original_name"]
            new_name = upd["resolved_name"]

            # Replace in authors field
            frontmatter, changed = replace_in_field(frontmatter, "authors", old_name, new_name)
            if changed:
                modified = True
                replacements.append((old_name, new_name, "authors"))

            # Replace in first_author (handles wikilink: [[Name]])
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
                stats["errors"] += 1
                stats["details"].append({"paper": filename, "error": "quote validation"})
                continue

            if not args.dry_run:
                atomic_write(paper_path, reassemble(frontmatter, body))

            stats["fixed"] += 1
            stats["details"].append({
                "paper": filename,
                "replacements": replacements,
                "dry_run": args.dry_run,
            })
            print(f"  FIXED: {filename}")
            for old, new, field in replacements:
                print(f"    {field}: {old} → {new}")
        else:
            stats["skipped"] += 1

    print(f"\n=== APPLY SUMMARY ({'DRY RUN' if args.dry_run else 'LIVE'}) ===")
    print(f"  Fixed: {stats['fixed']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")

    # Save log
    log = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "dry_run": args.dry_run,
            "source": results_path.name,
        },
        "summary": {
            "resolved_entries": len(resolved),
            "papers_fixed": stats["fixed"],
            "papers_skipped": stats["skipped"],
            "errors": stats["errors"],
        },
        "details": stats["details"],
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nLog saved: {LOG_FILE.name}")


if __name__ == "__main__":
    main()
