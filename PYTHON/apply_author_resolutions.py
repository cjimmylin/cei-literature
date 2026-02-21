#!/usr/bin/env python3
"""
Apply Author Resolutions — Step 5 of the Author Verification Pipeline

Reads the consolidated resolution plan and applies YAML fixes + creates
missing author profiles.

Apply order (dependencies matter):
  F → A → D → B → C → E
  - Format normalization first (may resolve apparent B/C mismatches)
  - Abbreviated name resolution before missing profiles
  - Unknown resolution before missing profiles (creates new names)

YAML Safety:
  - All field updates use re.subn() with re.MULTILINE — never parse→rebuild
  - Quote validation before writing (even " count per line)
  - Atomic writes via .tmp.{PID} + os.replace()
  - first_author/last_author use wikilink format: "[[Name]]"
  - authors field uses plain text: "Name A; Name B"

USAGE:
    cd CEI-Lit-WS

    # Dry run (preview all changes)
    ../.venv/bin/python PYTHON/apply_author_resolutions.py --dry-run

    # Apply all categories
    ../.venv/bin/python PYTHON/apply_author_resolutions.py

    # Apply specific categories
    ../.venv/bin/python PYTHON/apply_author_resolutions.py --categories F,B,C

    # Only create missing profiles (Category E)
    ../.venv/bin/python PYTHON/apply_author_resolutions.py --categories E
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
from typing import Dict, List, Optional, Tuple

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR

# --- Date prefix ---
DATE_PREFIX = datetime.now().strftime("%Y%m%d")
APPLY_LOG = LOGS_DIR / f"{DATE_PREFIX}-author_resolutions_applied.json"


# =============================================================================
# YAML SAFETY — FIELD-LEVEL REGEX REPLACEMENT
# =============================================================================

def safe_replace_field(frontmatter: str, key: str, new_value: str) -> Tuple[str, int]:
    """
    Safely replace a YAML field value in-place using regex.
    NEVER uses parse→rebuild round-trip (would destroy list fields).

    Returns: (updated_frontmatter, replacement_count)
    """
    safe_value = new_value.replace('"', "'")  # Never use \" escaping
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        replacement = f'{key}: "{safe_value}"'
    else:
        replacement = f'{key}: {safe_value}'

    pattern = rf'^{re.escape(key)}:\s*.*$'
    result, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)
    return result, count


def add_field_after(frontmatter: str, after_key: str, new_key: str, new_value: str) -> Tuple[str, bool]:
    """Add a new YAML field after an existing field.
    Returns: (updated_frontmatter, success)"""
    safe_value = new_value.replace('"', "'")
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        new_line = f'{new_key}: "{safe_value}"'
    else:
        new_line = f'{new_key}: {safe_value}'

    pattern = rf'^({re.escape(after_key)}:\s*.*)$'
    result, count = re.subn(pattern, rf'\1\n{new_line}', frontmatter, count=1, flags=re.MULTILINE)
    return result, count > 0


def extract_frontmatter_parts(content: str) -> Optional[Tuple[str, str]]:
    """Split content into (frontmatter, body). Returns None if no frontmatter."""
    fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return None
    return fm_match.group(1), content[fm_match.end():]


def reassemble(frontmatter: str, body: str) -> str:
    """Reassemble frontmatter + body into full content."""
    return f"---\n{frontmatter}\n---\n{body}"


def validate_yaml_quotes(frontmatter: str) -> bool:
    """Basic quote validation: each line should have even number of "."""
    for line in frontmatter.split('\n'):
        if line.count('"') % 2 != 0:
            return False
    return True


def atomic_write(path: Path, content: str):
    """Write content atomically via temp file + os.replace()."""
    tmp = path.with_suffix(f".tmp.{os.getpid()}")
    tmp.write_text(content, encoding='utf-8')
    os.replace(str(tmp), str(path))


# =============================================================================
# CATEGORY APPLIERS
# =============================================================================

def apply_category_f(items: List[Dict], dry_run: bool = False) -> Dict:
    """Reformat authors fields to canonical "First Last; First Last" format."""
    stats = {"applied": 0, "skipped": 0, "errors": 0, "details": []}

    for item in items:
        if item.get("status") != "resolved" or item.get("action") != "reformat":
            stats["skipped"] += 1
            continue

        paper_path = PAPERS_DIR / item["filename"]
        if not paper_path.exists():
            stats["errors"] += 1
            stats["details"].append({"paper": item["paper"], "error": "file not found"})
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        new_value = item["new_value"]

        # Update authors field
        new_fm, count = safe_replace_field(frontmatter, "authors", new_value)
        if count == 0:
            stats["skipped"] += 1
            stats["details"].append({"paper": item["paper"], "skip": "field not found"})
            continue

        if not validate_yaml_quotes(new_fm):
            stats["errors"] += 1
            stats["details"].append({"paper": item["paper"], "error": "quote validation failed"})
            continue

        if dry_run:
            stats["applied"] += 1
            stats["details"].append({"paper": item["paper"], "action": "reformat", "dry_run": True})
            continue

        atomic_write(paper_path, reassemble(new_fm, body))
        stats["applied"] += 1

    return stats


def apply_category_a(items: List[Dict], dry_run: bool = False) -> Dict:
    """Replace abbreviated names in authors field with resolved full names."""
    stats = {"applied": 0, "skipped": 0, "errors": 0, "details": []}

    # Group by paper for efficient file I/O
    paper_updates = defaultdict(list)
    for item in items:
        if item.get("status") != "resolved" or not item.get("resolved_name"):
            stats["skipped"] += 1
            continue
        paper_updates[item["filename"]].append(item)

    for filename, updates in paper_updates.items():
        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            stats["errors"] += 1
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        modified = False

        for upd in updates:
            old_name = upd["original_name"]
            new_name = upd["resolved_name"]

            # Replace in authors field value
            # Match the full authors field line
            authors_match = re.search(r'^authors:\s*(.+)$', frontmatter, re.MULTILINE)
            if authors_match:
                old_authors_val = authors_match.group(1)
                # Replace the abbreviated name with full name
                new_authors_val = old_authors_val.replace(old_name, new_name)
                if new_authors_val != old_authors_val:
                    frontmatter = frontmatter.replace(old_authors_val, new_authors_val, 1)
                    modified = True

            # Also update first_author if it references the abbreviated name
            fa_match = re.search(r'^first_author:\s*(.+)$', frontmatter, re.MULTILINE)
            if fa_match and old_name in fa_match.group(1):
                old_fa = fa_match.group(1)
                new_fa = old_fa.replace(old_name, new_name)
                frontmatter = frontmatter.replace(old_fa, new_fa, 1)
                modified = True

            # Also update last_author if it references the abbreviated name
            la_match = re.search(r'^last_author:\s*(.+)$', frontmatter, re.MULTILINE)
            if la_match and old_name in la_match.group(1):
                old_la = la_match.group(1)
                new_la = old_la.replace(old_name, new_name)
                frontmatter = frontmatter.replace(old_la, new_la, 1)
                modified = True

        if modified:
            if not validate_yaml_quotes(frontmatter):
                stats["errors"] += 1
                stats["details"].append({"paper": updates[0]["paper"], "error": "quote validation"})
                continue

            if not dry_run:
                atomic_write(paper_path, reassemble(frontmatter, body))
            stats["applied"] += 1
            stats["details"].append({
                "paper": updates[0]["paper"],
                "replacements": [(u["original_name"], u["resolved_name"]) for u in updates],
                "dry_run": dry_run,
            })
        else:
            stats["skipped"] += 1

    return stats


def apply_category_d(items: List[Dict], dry_run: bool = False) -> Dict:
    """Apply resolved authors for unknown/incomplete papers."""
    stats = {"applied": 0, "skipped": 0, "errors": 0, "details": []}

    for item in items:
        if item.get("status") != "resolved" or not item.get("resolved_authors"):
            stats["skipped"] += 1
            continue

        paper_path = PAPERS_DIR / item["filename"]
        if not paper_path.exists():
            stats["errors"] += 1
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        authors = item["resolved_authors"]
        authors_str = "; ".join(authors)
        first_author = authors[0] if authors else ""
        last_author = authors[-1] if len(authors) > 1 else authors[0] if authors else ""

        # Update authors field
        frontmatter, _ = safe_replace_field(frontmatter, "authors", authors_str)

        # Update first_author (with wikilink)
        if first_author:
            fa_safe = first_author.replace('"', "'")
            fa_wikilink = f"[[{fa_safe}]]"
            frontmatter, count = safe_replace_field(frontmatter, "first_author", fa_wikilink)
            if count == 0:
                frontmatter, _ = add_field_after(frontmatter, "authors", "first_author", fa_wikilink)

        # Update last_author (with wikilink)
        if last_author:
            la_safe = last_author.replace('"', "'")
            la_wikilink = f"[[{la_safe}]]"
            frontmatter, count = safe_replace_field(frontmatter, "last_author", la_wikilink)
            if count == 0:
                frontmatter, _ = add_field_after(frontmatter, "first_author", "last_author", la_wikilink)

        # Set authors_incomplete to false
        frontmatter, count = safe_replace_field(frontmatter, "authors_incomplete", "false")

        if not validate_yaml_quotes(frontmatter):
            stats["errors"] += 1
            stats["details"].append({"paper": item["paper"], "error": "quote validation"})
            continue

        if not dry_run:
            atomic_write(paper_path, reassemble(frontmatter, body))

        stats["applied"] += 1
        stats["details"].append({
            "paper": item["paper"],
            "authors": authors,
            "source": item.get("source"),
            "dry_run": dry_run,
        })

    return stats


def apply_category_b(items: List[Dict], dry_run: bool = False) -> Dict:
    """Update first_author fields to match first entry in authors list."""
    stats = {"applied": 0, "skipped": 0, "errors": 0, "details": []}

    for item in items:
        if item.get("status") != "resolved" or item.get("action") == "skip":
            stats["skipped"] += 1
            continue

        paper_path = PAPERS_DIR / item["filename"]
        if not paper_path.exists():
            stats["errors"] += 1
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        new_value = item["new_value"]
        fa_safe = new_value.replace('"', "'")
        fa_wikilink = f"[[{fa_safe}]]"

        frontmatter, count = safe_replace_field(frontmatter, "first_author", fa_wikilink)
        if count == 0:
            # Field doesn't exist — add after authors
            frontmatter, _ = add_field_after(frontmatter, "authors", "first_author", fa_wikilink)

        if not validate_yaml_quotes(frontmatter):
            stats["errors"] += 1
            stats["details"].append({"paper": item["paper"], "error": "quote validation"})
            continue

        if not dry_run:
            atomic_write(paper_path, reassemble(frontmatter, body))

        stats["applied"] += 1
        stats["details"].append({
            "paper": item["paper"],
            "old": item.get("old_value"),
            "new": fa_wikilink,
            "dry_run": dry_run,
        })

    return stats


def apply_category_c(items: List[Dict], dry_run: bool = False) -> Dict:
    """Update/add last_author fields to match last entry in authors list."""
    stats = {"applied": 0, "skipped": 0, "errors": 0, "details": []}

    for item in items:
        if item.get("status") != "resolved" or item.get("action") == "skip":
            stats["skipped"] += 1
            continue

        paper_path = PAPERS_DIR / item["filename"]
        if not paper_path.exists():
            stats["errors"] += 1
            continue

        content = paper_path.read_text(encoding='utf-8')
        parts = extract_frontmatter_parts(content)
        if not parts:
            stats["errors"] += 1
            continue

        frontmatter, body = parts
        new_value = item["new_value"]
        la_safe = new_value.replace('"', "'")
        la_wikilink = f"[[{la_safe}]]"

        action = item.get("action", "update_last_author")

        if action == "add_last_author":
            # Field doesn't exist — add after first_author
            frontmatter, success = add_field_after(frontmatter, "first_author", "last_author", la_wikilink)
            if not success:
                # Try adding after authors
                frontmatter, success = add_field_after(frontmatter, "authors", "last_author", la_wikilink)
        else:
            frontmatter, count = safe_replace_field(frontmatter, "last_author", la_wikilink)

        if not validate_yaml_quotes(frontmatter):
            stats["errors"] += 1
            stats["details"].append({"paper": item["paper"], "error": "quote validation"})
            continue

        if not dry_run:
            atomic_write(paper_path, reassemble(frontmatter, body))

        stats["applied"] += 1
        stats["details"].append({
            "paper": item["paper"],
            "action": action,
            "old": item.get("old_value"),
            "new": la_wikilink,
            "dry_run": dry_run,
        })

    return stats


def apply_category_e(items: List[Dict], dry_run: bool = False) -> Dict:
    """Create stub author profiles for missing authors."""
    stats = {"created": 0, "skipped": 0, "errors": 0, "already_exists": 0, "details": []}

    for item in items:
        if item.get("status") != "resolved" or item.get("action") != "create_stub":
            stats["skipped"] += 1
            continue

        name = item["author_name"]
        author_file = AUTHORS_DIR / f"{name}.md"

        if author_file.exists():
            stats["already_exists"] += 1
            continue

        stub_content = f"""---
name: "{name}"
affiliation: ""
research_interests: []
website: ""
google_scholar: ""
semantic_scholar: ""
---

# {name}

## Affiliation


## Research Interests


## Publications
(Auto-generated list of linked papers)
"""

        if dry_run:
            stats["created"] += 1
            stats["details"].append({"name": name, "action": "create_stub", "dry_run": True})
            continue

        try:
            author_file.write_text(stub_content, encoding='utf-8')
            stats["created"] += 1
            stats["details"].append({"name": name, "action": "created"})
        except Exception as e:
            stats["errors"] += 1
            stats["details"].append({"name": name, "error": str(e)})

    return stats


# =============================================================================
# MAIN
# =============================================================================

def load_resolution_plan() -> Dict:
    """Load the most recent resolution plan."""
    # First look for consolidated plan
    candidates = sorted(LOGS_DIR.glob("*-author_resolution_plan.json"), reverse=True)
    if candidates:
        path = candidates[0]
    else:
        # Fall back to single-run plan
        candidates = sorted(LOGS_DIR.glob("*-author_resolution_plan_ABCDEF.json"), reverse=True)
        if not candidates:
            print("ERROR: No resolution plan found. Run resolve_author_issues.py first.")
            sys.exit(1)
        path = candidates[0]

    print(f"Loading resolution plan: {path.name}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Apply author resolutions to YAML files")
    parser.add_argument("--categories", default="F,A,D,B,C,E",
                        help="Comma-separated categories to apply in order (default: F,A,D,B,C,E)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing files")
    args = parser.parse_args()

    cats = [c.strip().upper() for c in args.categories.split(',')]
    plan = load_resolution_plan()

    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"Apply order: {' → '.join(cats)}\n")

    results = {}
    # Apply in specified order (default: F → A → D → B → C → E)
    APPLIERS = {
        'F': apply_category_f,
        'A': apply_category_a,
        'D': apply_category_d,
        'B': apply_category_b,
        'C': apply_category_c,
        'E': apply_category_e,
    }

    for cat in cats:
        items = plan.get(cat, [])
        if not items:
            print(f"Category {cat}: no items")
            results[cat] = {"applied": 0, "skipped": 0}
            continue

        applier = APPLIERS.get(cat)
        if not applier:
            print(f"Unknown category: {cat}")
            continue

        print(f"--- Applying Category {cat}: {len(items)} items ---")
        stats = applier(items, dry_run=args.dry_run)
        results[cat] = stats

        # Print category stats
        if cat == 'E':
            print(f"  Created: {stats.get('created', 0)}, "
                  f"Already exists: {stats.get('already_exists', 0)}, "
                  f"Skipped: {stats['skipped']}, Errors: {stats['errors']}")
        else:
            print(f"  Applied: {stats['applied']}, "
                  f"Skipped: {stats['skipped']}, Errors: {stats['errors']}")

    # Summary
    print(f"\n=== APPLY SUMMARY ({'DRY RUN' if args.dry_run else 'LIVE'}) ===")
    for cat in cats:
        s = results.get(cat, {})
        if cat == 'E':
            print(f"  {cat}: {s.get('created', 0)} created, "
                  f"{s.get('already_exists', 0)} existing, "
                  f"{s.get('errors', 0)} errors")
        else:
            print(f"  {cat}: {s.get('applied', 0)} applied, "
                  f"{s.get('skipped', 0)} skipped, "
                  f"{s.get('errors', 0)} errors")

    # Save application log
    log_data = {
        "metadata": {
            "date": datetime.now().isoformat(),
            "dry_run": args.dry_run,
            "categories": cats,
        },
        "results": results,
    }

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    tmp = APPLY_LOG.with_suffix(f".tmp.{os.getpid()}")
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False, default=str)
    os.replace(str(tmp), str(APPLY_LOG))
    print(f"\nApplication log: {APPLY_LOG.name}")


if __name__ == "__main__":
    main()
