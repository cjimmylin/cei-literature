#!/usr/bin/env python3
"""Update all paper markdown files to include first_author and authors properties."""

import re
from pathlib import Path

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR

def extract_first_author(authors_str):
    """Extract the first author from an author string."""
    if not authors_str:
        return ""

    # Authors are typically separated by semicolons
    # Format: "LastName, FirstName; LastName2, FirstName2; ..."
    first_author = authors_str.split(';')[0].strip()
    return first_author

# Note: parse_frontmatter replaced by yaml_frontmatter_utils.read_paper + parse_frontmatter

# Note: build_frontmatter replaced by yaml_frontmatter_utils.write_paper

def update_paper(filepath):
    """Update a paper's frontmatter with first_author."""
    try:
        # Use safe YAML utilities
        frontmatter_text, rest = read_paper(filepath)
    except Exception:
        return False

    if not frontmatter_text:
        return False

    # Parse the frontmatter text to get authors field
    lines = frontmatter_text.split('\n')
    authors = ''
    for line in lines:
        if line.startswith('authors:'):
            authors = line.split(':', 1)[1].strip().strip('"')
            break

    # Extract first author
    first_author = extract_first_author(authors)

    # Add first_author to frontmatter if not present
    if 'first_author:' not in frontmatter_text:
        # Insert after authors line or at the end
        new_lines = []
        added = False
        for line in lines:
            new_lines.append(line)
            if line.startswith('authors:') and not added:
                new_lines.append(f'first_author: "{first_author}"')
                added = True
        if not added:
            new_lines.append(f'first_author: "{first_author}"')
        new_frontmatter = '\n'.join(new_lines)
    else:
        # Update existing first_author
        new_frontmatter = re.sub(
            r'^first_author:.*$',
            f'first_author: "{first_author}"',
            frontmatter_text,
            flags=re.MULTILINE
        )

    # Validate and write back using safe utility
    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

    write_paper(filepath, new_frontmatter, rest, validate=True)
    return True

def main():
    updated = 0
    errors = 0

    for md_file in sorted(PAPERS_DIR.glob('*.md')):
        try:
            if update_paper(md_file):
                updated += 1
            else:
                print(f"Could not parse: {md_file.name[:50]}...")
                errors += 1
        except Exception as e:
            print(f"Error with {md_file.name[:50]}: {e}")
            errors += 1

    print(f"\n{'='*50}")
    print(f"Updated {updated} papers with first_author property")
    if errors:
        print(f"Errors: {errors}")

if __name__ == "__main__":
    main()
