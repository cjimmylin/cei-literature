#!/usr/bin/env python3
"""
Fix orphaned tags lists in paper YAML frontmatter.
Some papers have duplicate 'tags' keys - one as a string, one as an orphaned list.
This script removes the orphaned list items.
"""

from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import extract_frontmatter, validate_frontmatter, write_paper
from vault_config import PAPERS_DIR


def fix_orphaned_tags(papers_dir: Path):
    """Remove orphaned tags lists from YAML"""

    papers = sorted(papers_dir.glob('*.md'))
    fixed_count = 0

    for filepath in papers:
        content = filepath.read_text(encoding='utf-8')

        # Check if it has the orphaned tags pattern
        if not re.search(r'^tags:\s*\n\s+-\s+', content, re.MULTILINE):
            continue

        try:
            fm, body = extract_frontmatter(content)
        except Exception:
            continue

        # Split into lines
        lines = fm.split('\n')
        new_lines = []
        skip_tags_list = False

        for line in lines:
            # Check if this is an empty 'tags:' line
            if re.match(r'^tags:\s*$', line):
                skip_tags_list = True
                continue

            # Skip list items under empty tags
            if skip_tags_list and re.match(r'^\s+-\s+', line):
                continue

            # When we hit the next key, stop skipping
            if skip_tags_list and not re.match(r'^\s', line) and line.strip():
                skip_tags_list = False

            new_lines.append(line)

        new_fm = '\n'.join(new_lines)

        # Validate
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"  SKIP: {filepath.name} - validation failed: {issues}")
            continue

        # Write back
        write_paper(filepath, new_fm, body, validate=True)
        fixed_count += 1
        print(f"  Fixed: {filepath.name}")

    print(f"\nFixed {fixed_count} papers with orphaned tags lists")


if __name__ == '__main__':
    print("Fixing orphaned tags lists...\n")
    fix_orphaned_tags(PAPERS_DIR)
