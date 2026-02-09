#!/usr/bin/env python3
"""
Phase 3: Update Papers — Add last_author Field & Expand "et al."

For all papers:
1. Adds a `last_author: "[[Name]]"` YAML field (inserted after `first_author` line)
2. For papers where "et al." was resolved in Phase 1, updates the `authors` YAML field
3. Updates the body `## Authors` section with complete wikilinked author list

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/update_paper_last_author.py --dry-run
    ../.venv/bin/python PYTHON/update_paper_last_author.py
"""

import re
import json
import sys
import os
import functools
from pathlib import Path
from typing import Dict, Optional

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, LOGS_DIR

from datetime import date
DATE_PREFIX = date.today().strftime("%Y%m%d")

# Input files
MAP_FILES = sorted(LOGS_DIR.glob("*-author_paper_map.json"), reverse=True)
DISAMB_FILES = sorted(LOGS_DIR.glob("*-author_disambiguation.json"), reverse=True)


# =============================================================================
# YAML SAFETY: In-place field operations (never parse→rebuild round-trip)
# =============================================================================

def clean_author_for_yaml(name: str) -> str:
    """Clean an author name for use in YAML wikilink fields."""
    name = re.sub(r'\[\[|\]\]', '', name).strip()
    # Remove "and " prefix (from body-style author lists)
    name = re.sub(r'^and\s+', '', name, flags=re.IGNORECASE)
    # Remove double-period artifacts (from "et al." removal on abbreviated names like "Z.")
    name = name.replace('..', '.')
    # Remove trailing period (but NOT on abbreviations like "J." — only trailing after full word)
    # If name ends with "." and the char before is NOT uppercase (i.e., not an initial), strip it
    if name.endswith('.') and len(name) > 2 and name[-2] != ' ':
        name = name.rstrip('.')
    # Remove trailing comma/semicolon
    name = name.rstrip(',;')
    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def add_last_author_field(frontmatter: str, last_author: str) -> str:
    """
    Insert `last_author: "[[Name]]"` field immediately after `first_author` line.

    Uses safe regex insertion — never parse→rebuild round-trip.
    """
    # Clean the author name (remove wikilinks if already present)
    clean_name = clean_author_for_yaml(last_author)
    new_field = f'last_author: "[[{clean_name}]]"'

    # Check if last_author already exists
    if re.search(r'^last_author:', frontmatter, re.MULTILINE):
        # Replace existing
        frontmatter = re.sub(
            r'^last_author:.*$',
            new_field,
            frontmatter,
            count=1,
            flags=re.MULTILINE
        )
        return frontmatter

    # Insert after first_author line
    match = re.search(r'^(first_author:.*$)', frontmatter, re.MULTILINE)
    if match:
        insert_pos = match.end()
        frontmatter = frontmatter[:insert_pos] + '\n' + new_field + frontmatter[insert_pos:]
        return frontmatter

    # If no first_author exists, insert after authors line
    match = re.search(r'^(authors:.*$)', frontmatter, re.MULTILINE)
    if match:
        insert_pos = match.end()
        frontmatter = frontmatter[:insert_pos] + '\n' + new_field + frontmatter[insert_pos:]
        return frontmatter

    # Last resort: append before the end
    frontmatter = frontmatter.rstrip() + '\n' + new_field
    return frontmatter


def update_authors_field(frontmatter: str, new_authors: list) -> str:
    """
    Replace the `authors` YAML field with a full expanded author list.

    Uses safe regex replacement — never parse→rebuild round-trip.
    """
    # Clean each author name
    cleaned = [clean_author_for_yaml(a) for a in new_authors if clean_author_for_yaml(a)]
    # Format: semicolon-separated, consistent with vault convention
    authors_str = '; '.join(cleaned)
    # Escape any double quotes in author names
    safe_str = authors_str.replace('"', "'")
    new_line = f'authors: "{safe_str}"'

    result, count = re.subn(
        r'^authors:.*$',
        new_line,
        frontmatter,
        count=1,
        flags=re.MULTILINE
    )

    if count == 0:
        # No existing authors field — add after short_title
        match = re.search(r'^(short_title:.*$)', frontmatter, re.MULTILINE)
        if match:
            insert_pos = match.end()
            result = frontmatter[:insert_pos] + '\n' + new_line + frontmatter[insert_pos:]
        else:
            result = frontmatter.rstrip() + '\n' + new_line

    return result


def update_first_author_field(frontmatter: str, first_author: str) -> str:
    """Update or add the first_author YAML field."""
    clean_name = clean_author_for_yaml(first_author)
    new_field = f'first_author: "[[{clean_name}]]"'

    if re.search(r'^first_author:', frontmatter, re.MULTILINE):
        frontmatter = re.sub(
            r'^first_author:.*$',
            new_field,
            frontmatter,
            count=1,
            flags=re.MULTILINE
        )
    else:
        # Insert after year line
        match = re.search(r'^(year:.*$)', frontmatter, re.MULTILINE)
        if match:
            insert_pos = match.end()
            frontmatter = frontmatter[:insert_pos] + '\n' + new_field + frontmatter[insert_pos:]
        else:
            frontmatter = frontmatter.rstrip() + '\n' + new_field

    return frontmatter


def add_authors_incomplete_flag(frontmatter: str) -> str:
    """Add authors_incomplete: true flag for unresolved et al. papers."""
    if re.search(r'^authors_incomplete:', frontmatter, re.MULTILINE):
        return frontmatter

    new_field = 'authors_incomplete: true'

    # Insert after authors line
    match = re.search(r'^(authors:.*$)', frontmatter, re.MULTILINE)
    if match:
        insert_pos = match.end()
        frontmatter = frontmatter[:insert_pos] + '\n' + new_field + frontmatter[insert_pos:]
    else:
        frontmatter = frontmatter.rstrip() + '\n' + new_field

    return frontmatter


# =============================================================================
# BODY SECTION UPDATER
# =============================================================================

def update_authors_body_section(body: str, authors: list, disambiguation: Dict = None) -> str:
    """
    Update the `## Authors` section in the body with wikilinked author list.

    Format: [[Author Name]], [[Author Name]], [[Author Name]]
    """
    if not authors:
        return body

    # Build wikilinked author list
    # Use disambiguation to get canonical profile names when available
    wikilinks = []
    for author in authors:
        clean = clean_author_for_yaml(author)
        if disambiguation and clean in disambiguation:
            canonical = disambiguation[clean].get('canonical_profile')
            if canonical and canonical != clean:
                # Use pipe syntax: [[Canonical Name|Display Name]]
                wikilinks.append(f"[[{canonical}|{clean}]]")
            else:
                wikilinks.append(f"[[{clean}]]")
        else:
            wikilinks.append(f"[[{clean}]]")

    author_line = ', '.join(wikilinks)

    # Replace the ## Authors section content
    # Pattern: ## Authors\n\n<content>\n\n## (next section)
    pattern = r'(## Authors\s*\n\s*\n).*?(?=\n\s*\n## |\n\s*\n\Z)'
    match = re.search(pattern, body, re.DOTALL)

    if match:
        body = body[:match.start()] + match.group(1) + author_line + body[match.end():]
    else:
        # Try simpler pattern: ## Authors followed by any content until next ##
        pattern2 = r'(## Authors\s*\n).*?(?=\n## |\Z)'
        match2 = re.search(pattern2, body, re.DOTALL)
        if match2:
            body = body[:match2.start()] + match2.group(1) + '\n' + author_line + '\n' + body[match2.end():]

    return body


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def update_papers(dry_run: bool = False):
    """Main function: update all papers with last_author and expanded authors."""

    # Load inputs
    if not MAP_FILES:
        print("ERROR: No author_paper_map.json found. Run Phase 1 first.")
        sys.exit(1)

    map_path = MAP_FILES[0]
    print(f"Loading author-paper map: {map_path.name}")
    with open(map_path, 'r', encoding='utf-8') as f:
        author_paper_map = json.load(f)

    disambiguation = {}
    if DISAMB_FILES:
        disamb_path = DISAMB_FILES[0]
        print(f"Loading disambiguation map: {disamb_path.name}")
        with open(disamb_path, 'r', encoding='utf-8') as f:
            disambiguation = json.load(f)

    papers = sorted(PAPERS_DIR.glob('*.md'))
    print(f"\nProcessing {len(papers)} papers...")

    # Stats
    stats = {
        'last_author_added': 0,
        'last_author_updated': 0,
        'first_author_added': 0,
        'authors_expanded': 0,
        'body_updated': 0,
        'incomplete_flagged': 0,
        'skipped': 0,
        'errors': 0,
    }

    for paper_file in papers:
        stem = paper_file.stem

        entry = author_paper_map.get(stem)
        if not entry:
            stats['skipped'] += 1
            continue

        authors = entry.get('authors', [])
        first_author = entry.get('first_author')
        last_author = entry.get('last_author')
        et_al_resolved = entry.get('et_al_resolved', False)
        et_al_original = entry.get('et_al_original', False)

        if not authors and not first_author and not last_author:
            stats['skipped'] += 1
            continue

        try:
            content = paper_file.read_text(encoding='utf-8')

            # Split frontmatter and body
            if not content.startswith('---'):
                stats['skipped'] += 1
                continue

            fm_match = re.search(r'\n---\s*\n', content[3:])
            if not fm_match:
                stats['skipped'] += 1
                continue

            fm_end = fm_match.start() + 3
            frontmatter = content[3:fm_end]
            body = content[fm_end + 5:]  # Skip \n---\n

            modified = False

            # 1. Add/update first_author if missing or different
            if first_author:
                if not re.search(r'^first_author:', frontmatter, re.MULTILINE):
                    frontmatter = update_first_author_field(frontmatter, first_author)
                    modified = True
                    stats['first_author_added'] += 1

            # 2. Add/update last_author
            if last_author:
                had_last = bool(re.search(r'^last_author:', frontmatter, re.MULTILINE))
                frontmatter = add_last_author_field(frontmatter, last_author)
                modified = True
                if had_last:
                    stats['last_author_updated'] += 1
                else:
                    stats['last_author_added'] += 1

            # 3. Expand "et al." if resolved
            if et_al_resolved and authors:
                frontmatter = update_authors_field(frontmatter, authors)
                modified = True
                stats['authors_expanded'] += 1
            elif et_al_original and not et_al_resolved:
                # Flag as incomplete
                frontmatter = add_authors_incomplete_flag(frontmatter)
                modified = True
                stats['incomplete_flagged'] += 1

            # 4. Update body ## Authors section
            if authors and (et_al_resolved or last_author):
                new_body = update_authors_body_section(body, authors, disambiguation)
                if new_body != body:
                    body = new_body
                    modified = True
                    stats['body_updated'] += 1

            # Write if modified
            if modified:
                if dry_run:
                    changes = []
                    if last_author:
                        changes.append(f"last_author=[[{clean_author_for_yaml(last_author)}]]")
                    if et_al_resolved:
                        changes.append(f"expanded {len(authors)} authors")
                    print(f"  [DRY] {stem}: {', '.join(changes)}")
                else:
                    # Validate frontmatter (check quote balance)
                    lines = frontmatter.split('\n')
                    bad_quotes = False
                    for line in lines:
                        if '"' in line and line.count('"') % 2 != 0:
                            print(f"  WARNING: Quote mismatch in {stem}: {line.strip()}")
                            bad_quotes = True

                    if not bad_quotes:
                        new_content = f"---{frontmatter}\n---\n{body}"
                        paper_file.write_text(new_content, encoding='utf-8')
                    else:
                        stats['errors'] += 1

        except Exception as e:
            print(f"  ERROR processing {stem}: {e}")
            stats['errors'] += 1

    # Summary
    print("\n" + "=" * 60)
    print("PAPER UPDATE SUMMARY")
    print("=" * 60)
    print(f"last_author added:     {stats['last_author_added']}")
    print(f"last_author updated:   {stats['last_author_updated']}")
    print(f"first_author added:    {stats['first_author_added']}")
    print(f"authors expanded:      {stats['authors_expanded']}")
    print(f"body sections updated: {stats['body_updated']}")
    print(f"incomplete flagged:    {stats['incomplete_flagged']}")
    print(f"skipped:               {stats['skipped']}")
    print(f"errors:                {stats['errors']}")
    print("=" * 60)


def main():
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE (no files will be modified) ===\n")

    update_papers(dry_run=dry_run)


if __name__ == '__main__':
    main()
