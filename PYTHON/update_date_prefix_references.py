#!/usr/bin/env python3
"""Update cross-references after batch date-prefix rename of logs/ and STATISTICS/ files.

Reads the mapping JSON produced by batch_date_prefix_rename.py and updates all
references in Python scripts, Markdown files, and MEMORY.md.

Usage:
    python update_date_prefix_references.py <mapping.json>              # dry-run
    python update_date_prefix_references.py <mapping.json> --execute    # apply
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
MEMORY_MD = Path.home() / ".claude" / "projects" / "-Users-jimmy-lin-Documents-CEI-Literature-Vault" / "memory" / "MEMORY.md"

# Directories to scan for references
SCAN_DIRS = [
    (BASE / "PYTHON", "*.py"),
    (BASE / "STATISTICS", "*.md"),
    (BASE / "STATISTICS", "*.json"),
    (BASE / "STATISTICS", "*.txt"),
    (BASE / "logs", "*.md"),
    (BASE / "logs", "*.json"),
    (BASE / "logs", "*.txt"),
    (BASE / "logs", "*.log"),
    (BASE / "logs", "*.csv"),
    (BASE / "docs", "*.md"),
    (BASE / "_OPERATING-SYSTEM", "*.md"),
    (BASE / "_OPERATING-SYSTEM" / "Learnings", "*.md"),
    (BASE / "_OPERATING-SYSTEM" / "Standards", "*.md"),
    (BASE / "_OPERATING-SYSTEM" / "Maintenance", "*.md"),
]

# Additional individual files to scan
EXTRA_FILES = [
    MEMORY_MD,
]


def build_replacement_pairs(mapping: dict) -> List[Tuple[str, str]]:
    """Build (old_ref, new_ref) pairs sorted longest-first.

    For each renamed file, generate multiple reference forms:
    - dir/old_name -> dir/new_name  (e.g. logs/foo.json -> logs/20260208-foo.json)
    - bare "old_name" in string contexts
    """
    pairs = []
    for dir_name, renames in mapping.items():
        for old_name, new_name in renames.items():
            # Full path form: logs/old_name -> logs/new_name
            pairs.append((f"{dir_name}/{old_name}", f"{dir_name}/{new_name}"))
            # Bare filename form (for Path("logs") / "old_name" patterns)
            pairs.append((old_name, new_name))

    # Sort longest-first to avoid substring collisions
    # e.g. "normative_ethics_all_classifications_20260207.json" before "normative_ethics_decisions_20260207.json"
    pairs.sort(key=lambda p: len(p[0]), reverse=True)

    # Deduplicate (bare names might collide across dirs, but unlikely)
    seen = set()
    unique = []
    for old, new in pairs:
        if old not in seen:
            seen.add(old)
            unique.append((old, new))
    return unique


SKIP_FILES = {
    "batch_date_prefix_rename.py",
    "update_date_prefix_references.py",
}


def collect_files_to_scan(mapping_path: Path) -> List[Path]:
    """Collect all files that might contain cross-references."""
    files = []
    for scan_dir, pattern in SCAN_DIRS:
        if scan_dir.exists():
            files.extend(scan_dir.glob(pattern))

    for f in EXTRA_FILES:
        if f.exists():
            files.append(f)

    # Exclude the mapping JSON itself and the rename scripts
    files = [f for f in files
             if f.name not in SKIP_FILES
             and f.resolve() != mapping_path.resolve()]

    # Deduplicate and sort
    return sorted(set(files))


def update_file(filepath: Path, pairs: List[Tuple[str, str]], execute: bool) -> List[str]:
    """Apply replacements to a single file. Returns list of changes made."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return []

    original = content
    changes = []

    for old_ref, new_ref in pairs:
        if old_ref in content:
            count = content.count(old_ref)
            content = content.replace(old_ref, new_ref)
            changes.append(f"  '{old_ref}' → '{new_ref}' ({count}x)")

    if changes and execute:
        filepath.write_text(content, encoding="utf-8")

    return changes


def main():
    parser = argparse.ArgumentParser(description="Update cross-references after date-prefix rename")
    parser.add_argument("mapping_json", help="Path to rename mapping JSON (from batch_date_prefix_rename.py)")
    parser.add_argument("--execute", action="store_true", help="Actually modify files (default is dry-run)")
    args = parser.parse_args()

    mapping_path = Path(args.mapping_json)
    if not mapping_path.is_absolute():
        mapping_path = BASE / mapping_path

    if not mapping_path.exists():
        print(f"ERROR: Mapping file not found: {mapping_path}")
        sys.exit(1)

    with open(mapping_path) as f:
        mapping = json.load(f)

    pairs = build_replacement_pairs(mapping)
    print(f"Loaded {len(pairs)} replacement pairs from mapping")

    files = collect_files_to_scan(mapping_path)
    print(f"Scanning {len(files)} files for references...\n")

    total_files_changed = 0
    total_replacements = 0

    for filepath in files:
        changes = update_file(filepath, pairs, args.execute)
        if changes:
            total_files_changed += 1
            total_replacements += len(changes)
            # Show path relative to BASE if possible
            try:
                rel = filepath.relative_to(BASE)
            except ValueError:
                rel = filepath
            print(f"{rel}:")
            for c in changes:
                print(c)
            print()

    mode = "EXECUTED" if args.execute else "DRY-RUN"
    print(f"{'=' * 60}")
    print(f"SUMMARY ({mode}): {total_replacements} replacements in {total_files_changed} files")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
