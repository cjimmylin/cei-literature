#!/usr/bin/env python3
"""
Fix unquoted wikilink fields in paper files.

The issue: field: [[value]] should be field: "[[value]]"
Unquoted [[...]] is interpreted as a YAML flow sequence.

Fields checked:
- local_pdf: [[PDFs/file.pdf]]
- first_author: [[Author Name]]
- pdf_extract: [[PDF Extracts/file.md]]
"""

import re
from pathlib import Path


def fix_unquoted_wikilinks(paper_path: Path) -> int:
    """
    Fix unquoted wikilink fields in a paper file.

    Returns: Number of fields fixed
    """
    content = paper_path.read_text(encoding='utf-8')

    # Patterns to match unquoted wikilinks in various fields
    # Format: (field_pattern, replacement_format)
    patterns = [
        # local_pdf: [[PDFs/...]]
        (r'^(local_pdf:\s*)(\[\[PDFs/[^\]]+\]\])(\s*)$', r'\1"\2"\3'),
        # first_author: [[Author Name]]
        (r'^(first_author:\s*)(\[\[[^\]]+\]\])(\s*)$', r'\1"\2"\3'),
        # pdf_extract: [[PDF Extracts/...]]
        (r'^(pdf_extract:\s*)(\[\[PDF Extracts/[^\]]+\]\])(\s*)$', r'\1"\2"\3'),
    ]

    lines = content.split('\n')
    fix_count = 0
    new_lines = []

    for line in lines:
        fixed = False
        for pattern, replacement in patterns:
            if re.match(pattern, line):
                new_line = re.sub(pattern, replacement, line)
                new_lines.append(new_line)
                fix_count += 1
                fixed = True
                break
        if not fixed:
            new_lines.append(line)

    if fix_count > 0:
        paper_path.write_text('\n'.join(new_lines), encoding='utf-8')

    return fix_count


# Backward compatibility alias
def fix_unquoted_local_pdf(paper_path: Path) -> bool:
    """Legacy function name - calls fix_unquoted_wikilinks"""
    return fix_unquoted_wikilinks(paper_path) > 0


def main():
    from vault_config import PAPERS_DIR
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return

    fixed_count = 0
    error_count = 0

    for paper_file in sorted(papers_dir.glob('*.md')):
        try:
            fixes = fix_unquoted_wikilinks(paper_file)
            if fixes > 0:
                fixed_count += 1
                print(f"Fixed {fixes} field(s): {paper_file.name}")
        except Exception as e:
            error_count += 1
            print(f"Error in {paper_file.name}: {e}")

    print(f"\nSummary: Fixed {fixed_count} files, {error_count} errors")


if __name__ == "__main__":
    main()
