#!/usr/bin/env python3
"""
Fix Body Author Lines

Updates the **Authors:** line in the markdown body section to match
the authors from the frontmatter, removing "others" placeholders.

This script is safe: it uses the yaml_frontmatter_utils module.
"""

import re
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR


def format_authors_for_body(authors_str: str) -> str:
    """
    Format the authors field from frontmatter for the body's **Authors:** line.

    Input: "Dan Hendrycks; Collin Burns; Steven Basart"
    Output: "Hendrycks, Dan; Burns, Collin; Basart, Steven"
    """
    if not authors_str or authors_str == 'N/A':
        return 'Unknown'

    authors = []
    for author in authors_str.split(';'):
        author = author.strip()
        if not author or author.lower() in ['others', 'and others', 'et al.', 'et al']:
            continue

        # Convert "First Last" to "Last, First" if not already in that format
        if ',' not in author:
            parts = author.split()
            if len(parts) >= 2:
                # Handle names like "Dan Hendrycks" -> "Hendrycks, Dan"
                last = parts[-1]
                first = ' '.join(parts[:-1])
                author = f"{last}, {first}"

        authors.append(author)

    return '; '.join(authors) if authors else 'Unknown'


def fix_body_authors(filepath: Path, dry_run: bool = False) -> tuple[bool, str]:
    """
    Fix the **Authors:** line in a paper's body section.

    Returns: (changed, message)
    """
    content = filepath.read_text(encoding='utf-8')

    try:
        frontmatter, body = extract_frontmatter(content)
    except ValueError as e:
        return False, f"Failed to parse: {e}"

    fields = parse_frontmatter(frontmatter)
    authors_str = fields.get('authors', '')

    if not authors_str:
        return False, "No authors field in frontmatter"

    # Format authors for body
    formatted_authors = format_authors_for_body(authors_str)

    # Check if body has **Authors:** line with "others"
    old_pattern = r'\*\*Authors:\*\*\s*[^\n]+'
    match = re.search(old_pattern, body)

    if not match:
        return False, "No **Authors:** line found in body"

    old_line = match.group(0)

    # Skip if already correct (no "others")
    if 'others' not in old_line.lower():
        return False, "Authors line already complete"

    # Create new line
    new_line = f"**Authors:** {formatted_authors}"

    # Replace in body
    new_body = body[:match.start()] + new_line + body[match.end():]

    if dry_run:
        return True, f"Would update: {old_line[:60]}... -> {new_line[:60]}..."

    # Write back using safe utilities
    is_valid, issues = validate_frontmatter(frontmatter)
    if not is_valid:
        return False, f"Frontmatter invalid: {issues}"

    write_paper(filepath, frontmatter, new_body, validate=True)
    return True, f"Updated: {filepath.name}"


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fix body author lines')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--file', type=str, help='Process single file')
    args = parser.parse_args()

    if args.file:
        files = [PAPERS_DIR / args.file]
    else:
        files = sorted(PAPERS_DIR.glob('*.md'))

    changed = 0
    skipped = 0
    errors = 0

    for filepath in files:
        try:
            was_changed, msg = fix_body_authors(filepath, dry_run=args.dry_run)
            if was_changed:
                print(f"✓ {msg}")
                changed += 1
            else:
                if args.dry_run or 'others' in filepath.read_text():
                    print(f"  {filepath.name}: {msg}")
                skipped += 1
        except Exception as e:
            print(f"✗ {filepath.name}: {e}")
            errors += 1

    print(f"\nSummary: {changed} changed, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
