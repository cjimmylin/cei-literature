#!/usr/bin/env python3
"""
Fix curly quotes in YAML frontmatter of paper files.

Replaces Unicode curly quotes with straight single quotes (safest for YAML
since values are already wrapped in double quotes).

Only modifies content within the YAML frontmatter (between first --- and
second ---). Body content is left untouched.

Characters replaced:
  U+201C (left double curly quote)  -> '
  U+201D (right double curly quote) -> '
  U+2018 (left single curly quote)  -> '
  U+2019 (right single curly quote) -> '
"""

from __future__ import annotations

import sys
from pathlib import Path

# All curly quotes -> straight single quote
REPLACEMENTS = {
    "\u201c": "'",  # left double curly
    "\u201d": "'",  # right double curly
    "\u2018": "'",  # left single curly
    "\u2019": "'",  # right single curly
}


def fix_file(paper_path: Path) -> int:
    """Fix curly quotes in YAML frontmatter. Returns number of replacements."""
    content = paper_path.read_text(encoding="utf-8", errors="ignore")

    if not content.startswith("---"):
        return 0

    end_idx = content.find("\n---", 3)
    if end_idx < 0:
        return 0

    frontmatter = content[3:end_idx]
    rest = content[end_idx:]

    if not any(ch in frontmatter for ch in REPLACEMENTS):
        return 0

    new_fm = frontmatter
    total = 0
    for old_char, new_char in REPLACEMENTS.items():
        count = new_fm.count(old_char)
        if count > 0:
            new_fm = new_fm.replace(old_char, new_char)
            total += count

    if total > 0:
        new_content = "---" + new_fm + rest
        paper_path.write_text(new_content, encoding="utf-8")

    return total


def main() -> None:
    papers_dir = Path(__file__).resolve().parent.parent / "papers"
    if not papers_dir.is_dir():
        print(f"Papers directory not found: {papers_dir}", file=sys.stderr)
        sys.exit(1)

    dry_run = "--dry-run" in sys.argv

    fixed_count = 0
    total_replacements = 0
    files_fixed: list[tuple[str, int]] = []

    for f in sorted(papers_dir.glob("*.md")):
        if dry_run:
            content = f.read_text(encoding="utf-8", errors="ignore")
            if not content.startswith("---"):
                continue
            end_idx = content.find("\n---", 3)
            if end_idx < 0:
                continue
            frontmatter = content[3:end_idx]
            count = sum(frontmatter.count(ch) for ch in REPLACEMENTS)
            if count > 0:
                fixed_count += 1
                total_replacements += count
                files_fixed.append((f.name, count))
        else:
            count = fix_file(f)
            if count > 0:
                fixed_count += 1
                total_replacements += count
                files_fixed.append((f.name, count))

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] Files fixed: {fixed_count}")
    print(f"[{mode}] Total character replacements: {total_replacements}")
    print()
    for name, cnt in files_fixed:
        print(f"  {name}: {cnt} replacements")


if __name__ == "__main__":
    main()
