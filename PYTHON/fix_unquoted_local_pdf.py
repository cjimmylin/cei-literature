#!/usr/bin/env python3
"""
Fix unquoted wikilink fields in paper frontmatter.

The issue: field: [[value]] should be field: "[[value]]"
Unquoted [[...]] is read by YAML as a nested flow sequence, not a string.

Any top-level frontmatter field whose whole value is one bare wikilink is quoted
(local_pdf, first_author, last_author, pdf_extract, authors, pdf, ...). Only the
frontmatter is touched; list items, multi-link values and note bodies are left alone.

2026-10-18: generalised from three fixed patterns. The old local_pdf pattern required
the exact prefix "Lit-WS-PDFs/", so it skipped every link written with another prefix,
and it scanned whole files (bodies included).

Usage:
    python3 PYTHON/fix_unquoted_local_pdf.py --dry-run   # report only
    python3 PYTHON/fix_unquoted_local_pdf.py             # write
"""

import argparse
import re
from collections import Counter
from pathlib import Path

FRONTMATTER = re.compile(r'\A---\n(.*?)\n---[ \t]*(?=\n|\Z)', re.DOTALL)
UNQUOTED_LINK = re.compile(
    r'^([A-Za-z_][A-Za-z0-9_ -]*:[ \t]*)(\[\[[^\[\]\n"]+\]\])([ \t]*)$', re.MULTILINE)


def fix_unquoted_wikilinks(paper_path: Path, dry_run: bool = False, fields: Counter = None) -> int:
    """
    Quote bare wikilink values in a paper's frontmatter.

    Returns: Number of fields fixed
    """
    content = paper_path.read_text(encoding='utf-8')
    m = FRONTMATTER.match(content)
    if not m:
        return 0
    if fields is not None:
        for hit in UNQUOTED_LINK.finditer(m.group(1)):
            fields[hit.group(1).split(':', 1)[0].strip()] += 1
    new_fm, fix_count = UNQUOTED_LINK.subn(r'\1"\2"\3', m.group(1))
    if fix_count and not dry_run:
        paper_path.write_text(content[:m.start(1)] + new_fm + content[m.end(1):], encoding='utf-8')
    return fix_count


# Backward compatibility alias
def fix_unquoted_local_pdf(paper_path: Path) -> bool:
    """Legacy function name - calls fix_unquoted_wikilinks"""
    return fix_unquoted_wikilinks(paper_path) > 0


def main():
    parser = argparse.ArgumentParser(description="Quote bare wikilinks in paper frontmatter")
    parser.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    args = parser.parse_args()

    papers_dir = Path(__file__).resolve().parent.parent / "papers"
    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return

    fixed_count = 0
    error_count = 0
    fields = Counter()

    for paper_file in sorted(papers_dir.glob('*.md')):
        try:
            fixes = fix_unquoted_wikilinks(paper_file, dry_run=args.dry_run, fields=fields)
            if fixes > 0:
                fixed_count += 1
        except Exception as e:
            error_count += 1
            print(f"Error in {paper_file.name}: {e}")

    mode = "[DRY RUN] would fix" if args.dry_run else "Fixed"
    print(f"{mode} {sum(fields.values())} field(s) in {fixed_count} files, {error_count} errors")
    for field, n in fields.most_common():
        print(f"  {field}: {n}")


if __name__ == "__main__":
    main()
