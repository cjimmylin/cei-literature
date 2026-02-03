#!/usr/bin/env python3
"""
Fix author names with special characters that can't be used in filenames.

Some papers have author names with "/" or other special characters.
This script:
1. Sanitizes those names
2. Updates paper wikilinks
3. Creates author profiles with sanitized names
"""

import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter, rebuild_frontmatter, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR


def sanitize_filename(name: str) -> str:
    """Sanitize author name for use as filename"""
    # Remove problematic characters
    name = name.replace('/', '-')
    name = name.replace('\\', '-')
    name = name.replace(':', '-')
    name = name.replace('*', '-')
    name = name.replace('?', '-')
    name = name.replace('"', '')
    name = name.replace('<', '')
    name = name.replace('>', '')
    name = name.replace('|', '-')
    # Collapse multiple dashes
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing dashes and spaces
    name = name.strip(' -')
    return name


def process_papers(papers_dir: Path):
    """Find and fix papers with problematic author names"""

    papers = list(papers_dir.glob('*.md'))
    problematic_papers = []

    for filepath in papers:
        content = filepath.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        authors_str = fields.get('authors', '')

        # Extract wikilinks
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', authors_str)

        has_problems = False
        new_wikilinks = []

        for wikilink in wikilinks:
            # Check if name has special characters
            if any(c in wikilink for c in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
                has_problems = True
                sanitized = sanitize_filename(wikilink)
                new_wikilinks.append(sanitized)
                print(f"Problematic: {wikilink} -> {sanitized}")
            else:
                new_wikilinks.append(wikilink)

        if has_problems:
            # Rebuild authors string with sanitized wikilinks
            new_authors = '; '.join([f'[[{name}]]' for name in new_wikilinks])
            fields['authors'] = new_authors

            # Rebuild and validate YAML
            new_fm = rebuild_frontmatter(fields)
            is_valid, issues = validate_frontmatter(new_fm)
            if not is_valid:
                print(f"  ERROR validating {filepath.name}: {issues}")
                continue

            # Write back
            write_paper(filepath, new_fm, body, validate=True)
            problematic_papers.append((filepath.name, wikilinks, new_wikilinks))

    print(f"\n\nFixed {len(problematic_papers)} papers with problematic author names:")
    for paper_name, old, new in problematic_papers:
        print(f"  {paper_name}:")
        for old_name, new_name in zip(old, new):
            if old_name != new_name:
                print(f"    - {old_name} -> {new_name}")


if __name__ == '__main__':
    print("Finding and fixing problematic author names...\n")
    process_papers(PAPERS_DIR)
