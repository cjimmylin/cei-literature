#!/usr/bin/env python3
"""
Phase 4: Rebuild Author Profiles — Paper Lists with Position Annotations

For each author in the disambiguation map:
1. Rebuilds the `## Papers in this Vault` section with complete, annotated paper list
2. Creates stub profiles for newly discovered authors
3. Enriches profiles with discovered affiliations/emails

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/rebuild_author_profiles.py
    ../.venv/bin/python PYTHON/rebuild_author_profiles.py --dry-run
    ../.venv/bin/python PYTHON/rebuild_author_profiles.py --range A-E
    ../.venv/bin/python PYTHON/rebuild_author_profiles.py --range F-J
"""

import re
import json
import sys
import os
import functools
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import AUTHORS_DIR, PAPERS_DIR, LOGS_DIR

from datetime import date


def clean_author_name(name: str) -> str:
    """Clean an author name for use in profiles/filenames."""
    name = re.sub(r'\[\[|\]\]', '', name).strip()
    # Remove "and " prefix
    name = re.sub(r'^and\s+', '', name, flags=re.IGNORECASE)
    # Remove double-period artifacts
    name = name.replace('..', '.')
    # Remove trailing period after non-initial word
    if name.endswith('.') and len(name) > 2 and name[-2] != ' ':
        name = name.rstrip('.')
    # Remove trailing comma/semicolon
    name = name.rstrip(',;')
    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name
DATE_PREFIX = date.today().strftime("%Y%m%d")

# Input files
MAP_FILES = sorted(LOGS_DIR.glob("*-author_paper_map.json"), reverse=True)
DISAMB_FILES = sorted(LOGS_DIR.glob("*-author_disambiguation.json"), reverse=True)
AFFIL_FILES = sorted(LOGS_DIR.glob("*-author_affiliations.json"), reverse=True)

# Template
TEMPLATE_PATH = AUTHORS_DIR / 'TEMPLATE.md'


# =============================================================================
# PAPER LIST BUILDING
# =============================================================================

def build_paper_entry(stem: str, position: str, short_title: str) -> str:
    """
    Build a single paper list entry with position annotation.

    Format:
    - [[YYYY-Author-Title|Short Title]] (First Author)
    - [[YYYY-Author-Title|Short Title]] (Last Author)
    - [[YYYY-Author-Title|Short Title]]
    """
    # Clean short_title
    display = short_title if short_title else stem
    display = display.replace('"', "'")

    entry = f"- [[{stem}|{display}]]"

    if position == 'first' or position == 'sole':
        entry += " (First Author)"
    elif position == 'last':
        entry += " (Last Author)"
    # Middle authors get no annotation

    return entry


def extract_year_from_stem(stem: str) -> int:
    """Extract year from paper stem like '2024-Author-Title'."""
    match = re.match(r'^(\d{4})-', stem)
    if match:
        return int(match.group(1))
    return 0


def build_papers_section(papers: List[Dict], author_paper_map: Dict) -> str:
    """
    Build the complete `## Papers in this Vault` section content.

    Sorted by year descending, then alphabetically.
    """
    entries = []

    for paper_info in papers:
        stem = paper_info['stem']
        position = paper_info['position']

        # Get short_title from the map
        map_entry = author_paper_map.get(stem, {})
        short_title = map_entry.get('short_title', stem)

        year = extract_year_from_stem(stem)
        entry_text = build_paper_entry(stem, position, short_title)
        entries.append((year, stem, entry_text))

    # Sort: year descending, then stem alphabetically
    entries.sort(key=lambda x: (-x[0], x[1]))

    return '\n'.join(e[2] for e in entries)


# =============================================================================
# PROFILE CREATION & UPDATE
# =============================================================================

def create_stub_profile(name: str, papers: List[Dict], author_paper_map: Dict) -> str:
    """Create a new author profile from the template."""
    # Read template
    if TEMPLATE_PATH.exists():
        template = TEMPLATE_PATH.read_text(encoding='utf-8')
    else:
        # Minimal fallback template
        template = f"""---
name: "Full Name"
title: "Current Position"
affiliation: "University/Organization"
research_interests:
  - "Primary Research Area"
website: ""
google_scholar: ""
semantic_scholar: ""
---

# Full Name

## Biographical Summary

[To be enriched]

## Papers in this Vault

- [[PaperFilename|Paper Title]]

## Notes

"""

    # Replace placeholders
    safe_name = name.replace('"', "'")
    content = template.replace('name: "Full Name"', f'name: "{safe_name}"')

    # Replace all "Full Name" in body (heading, etc.)
    content = content.replace('# Full Name', f'# {name}')

    # Build papers section
    papers_text = build_papers_section(papers, author_paper_map)

    # Replace the template paper list
    content = re.sub(
        r'- \[\[YYYY-Author-ShortTitle\|Full Paper Title\]\]',
        papers_text,
        content
    )
    content = re.sub(
        r'- \[\[PaperFilename\|Paper Title\]\]',
        papers_text,
        content
    )
    # Also replace the placeholder text in the Papers section
    content = re.sub(
        r'\[Wikilinks to papers.*?\]',
        papers_text,
        content,
        flags=re.DOTALL
    )

    return content


def update_existing_profile(content: str, papers: List[Dict],
                            author_paper_map: Dict) -> str:
    """
    Update an existing profile's `## Papers in this Vault` section.

    Body-only edit: replaces content between `## Papers in this Vault` and next `##` heading.
    """
    papers_text = build_papers_section(papers, author_paper_map)

    # Pattern: ## Papers in this Vault\n\n<content>\n\n## or EOF
    # Use regex to find and replace the section
    pattern = r'(## Papers in this Vault\s*\n)\s*.*?(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        replacement = match.group(1) + '\n' + papers_text + '\n'
        content = content[:match.start()] + replacement + content[match.end():]
    else:
        # No existing section — find a good place to insert
        # Try after ## Major Publications or ## Research & Impact
        for section in ['## Major Publications', '## Research & Impact',
                        '## Research Focus', '## Biographical Summary']:
            sec_match = re.search(rf'({re.escape(section)}.*?)(?=\n## |\Z)',
                                  content, re.DOTALL)
            if sec_match:
                insert_pos = sec_match.end()
                section_text = f'\n\n## Papers in this Vault\n\n{papers_text}\n'
                content = content[:insert_pos] + section_text + content[insert_pos:]
                break
        else:
            # Append before ## Notes or at end
            notes_match = re.search(r'\n## Notes', content)
            if notes_match:
                insert_pos = notes_match.start()
                section_text = f'\n## Papers in this Vault\n\n{papers_text}\n'
                content = content[:insert_pos] + section_text + content[insert_pos:]
            else:
                content = content.rstrip() + f'\n\n## Papers in this Vault\n\n{papers_text}\n'

    return content


def enrich_profile_yaml(content: str, affiliations: Dict, paper_stem: str) -> str:
    """
    Enrich a profile's YAML with discovered affiliations/emails.

    Only fills empty placeholder fields. Appends provenance to Notes section.
    """
    if not affiliations:
        return content

    affils = affiliations.get('affiliations', [])
    emails = affiliations.get('emails', [])
    modified = False

    # Fill empty affiliation field
    if affils:
        # Check if current affiliation is placeholder
        affil_match = re.search(r'^affiliation:\s*"?([^"\n]*)"?', content, re.MULTILINE)
        if affil_match:
            current = affil_match.group(1).strip()
            if current in ('', 'University/Organization', 'Organization, Department (if applicable)'):
                # Use first discovered affiliation
                safe_affil = affils[0].replace('"', "'")
                content = re.sub(
                    r'^affiliation:.*$',
                    f'affiliation: "{safe_affil}"',
                    content,
                    count=1,
                    flags=re.MULTILINE
                )
                modified = True

    # Fill empty email field
    if emails:
        email_match = re.search(r'^email:\s*"?([^"\n]*)"?', content, re.MULTILINE)
        if email_match:
            current = email_match.group(1).strip()
            if not current:
                content = re.sub(
                    r'^email:.*$',
                    f'email: "{emails[0]}"',
                    content,
                    count=1,
                    flags=re.MULTILINE
                )
                modified = True

    # Append discovered info to Notes section for provenance
    if affils or emails:
        notes_info = f"- *From {paper_stem}*:"
        if affils:
            notes_info += f" Affiliation: {affils[0]}"
        if emails:
            notes_info += f", Email: {emails[0]}"

        notes_match = re.search(r'(## Notes\s*\n)', content)
        if notes_match:
            insert_pos = notes_match.end()
            content = content[:insert_pos] + '\n' + notes_info + '\n' + content[insert_pos:]

    return content


# =============================================================================
# RANGE FILTERING
# =============================================================================

def parse_range_arg(range_str: str) -> Tuple[str, str]:
    """Parse --range A-E into (start_letter, end_letter)."""
    match = re.match(r'^([A-Z])-([A-Z])$', range_str.upper())
    if match:
        return match.group(1), match.group(2)
    return 'A', 'Z'


def in_range(name: str, start: str, end: str) -> bool:
    """Check if an author name falls within the letter range."""
    if not name:
        return False
    first_letter = name[0].upper()
    return start <= first_letter <= end


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def rebuild_profiles(dry_run: bool = False, letter_range: Tuple[str, str] = ('A', 'Z')):
    """Main function: rebuild all author profiles."""

    # Load inputs
    if not MAP_FILES:
        print("ERROR: No author_paper_map.json found. Run Phase 1 first.")
        sys.exit(1)
    if not DISAMB_FILES:
        print("ERROR: No author_disambiguation.json found. Run Phase 2 first.")
        sys.exit(1)

    map_path = MAP_FILES[0]
    disamb_path = DISAMB_FILES[0]

    print(f"Loading author-paper map: {map_path.name}")
    with open(map_path, 'r', encoding='utf-8') as f:
        author_paper_map = json.load(f)

    print(f"Loading disambiguation map: {disamb_path.name}")
    with open(disamb_path, 'r', encoding='utf-8') as f:
        disambiguation = json.load(f)

    # Load affiliations (optional)
    affiliations_map = {}
    if AFFIL_FILES:
        print(f"Loading affiliations: {AFFIL_FILES[0].name}")
        with open(AFFIL_FILES[0], 'r', encoding='utf-8') as f:
            affiliations_map = json.load(f)

    # Build profile→papers mapping from disambiguation data
    profile_papers = defaultdict(list)  # canonical_profile → [paper_info]
    new_authors = {}  # author_name → [paper_info] for tier 6 (new authors)

    for author_name, info in disambiguation.items():
        canonical = info.get('canonical_profile')
        papers = info.get('papers', [])
        tier = info.get('match_tier', 6)

        if canonical and tier <= 5:
            # Matched to existing profile
            for p in papers:
                profile_papers[canonical].append(p)
        elif tier == 6 and not canonical:
            # New author — create stub (clean name first)
            cleaned = clean_author_name(author_name)
            if cleaned and len(cleaned) >= 2:
                # Check if cleaned name now matches an existing profile
                if cleaned in profile_papers or (AUTHORS_DIR / f"{cleaned}.md").exists():
                    for p in papers:
                        profile_papers[cleaned].append(p)
                else:
                    if cleaned in new_authors:
                        new_authors[cleaned].extend(papers)
                    else:
                        new_authors[cleaned] = papers

    print(f"\nProfile range: {letter_range[0]}-{letter_range[1]}")
    print(f"Existing profiles to update: {len(profile_papers)}")
    print(f"New author stubs to create: {len(new_authors)}")

    # Stats
    stats = {
        'profiles_updated': 0,
        'stubs_created': 0,
        'enriched': 0,
        'skipped_range': 0,
        'errors': 0,
    }

    # =========================================================================
    # UPDATE EXISTING PROFILES
    # =========================================================================
    print("\n=== Updating existing profiles ===")

    for profile_name, papers in sorted(profile_papers.items()):
        if not in_range(profile_name, *letter_range):
            stats['skipped_range'] += 1
            continue

        profile_path = AUTHORS_DIR / f"{profile_name}.md"
        if not profile_path.exists():
            # Profile referenced but doesn't exist — treat as new author
            new_authors[profile_name] = papers
            continue

        try:
            content = profile_path.read_text(encoding='utf-8')

            # Update papers section
            new_content = update_existing_profile(content, papers, author_paper_map)

            # Enrich with affiliations from first paper that has them
            for p in papers:
                if p['stem'] in affiliations_map:
                    new_content = enrich_profile_yaml(
                        new_content, affiliations_map[p['stem']], p['stem']
                    )
                    stats['enriched'] += 1
                    break

            if new_content != content:
                if dry_run:
                    print(f"  [DRY] {profile_name}: {len(papers)} papers")
                else:
                    profile_path.write_text(new_content, encoding='utf-8')
                stats['profiles_updated'] += 1

        except Exception as e:
            print(f"  ERROR updating {profile_name}: {e}")
            stats['errors'] += 1

    # =========================================================================
    # CREATE STUB PROFILES FOR NEW AUTHORS
    # =========================================================================
    print(f"\n=== Creating stub profiles ({len(new_authors)} candidates) ===")

    for author_name, papers in sorted(new_authors.items()):
        if not in_range(author_name, *letter_range):
            stats['skipped_range'] += 1
            continue

        # Sanitize filename
        safe_name = author_name.strip()
        safe_name = re.sub(r'[<>:"/\\|?*]', '', safe_name)

        if not safe_name or len(safe_name) < 2:
            continue

        profile_path = AUTHORS_DIR / f"{safe_name}.md"
        if profile_path.exists():
            # Already exists (maybe created by another range worker)
            # Still update its papers section
            try:
                content = profile_path.read_text(encoding='utf-8')
                new_content = update_existing_profile(content, papers, author_paper_map)
                if new_content != content:
                    if not dry_run:
                        profile_path.write_text(new_content, encoding='utf-8')
                    stats['profiles_updated'] += 1
            except Exception as e:
                print(f"  ERROR updating existing {safe_name}: {e}")
                stats['errors'] += 1
            continue

        try:
            content = create_stub_profile(author_name, papers, author_paper_map)

            if dry_run:
                print(f"  [DRY] Would create: {safe_name}.md ({len(papers)} papers)")
            else:
                profile_path.write_text(content, encoding='utf-8')
                print(f"  Created: {safe_name}.md ({len(papers)} papers)")

            stats['stubs_created'] += 1

        except Exception as e:
            print(f"  ERROR creating {safe_name}: {e}")
            stats['errors'] += 1

    # Summary
    print("\n" + "=" * 60)
    print(f"PROFILE REBUILD SUMMARY (range {letter_range[0]}-{letter_range[1]})")
    print("=" * 60)
    print(f"Profiles updated:    {stats['profiles_updated']}")
    print(f"Stubs created:       {stats['stubs_created']}")
    print(f"Enriched w/ affil:   {stats['enriched']}")
    print(f"Skipped (out of range): {stats['skipped_range']}")
    print(f"Errors:              {stats['errors']}")
    print("=" * 60)


def main():
    dry_run = '--dry-run' in sys.argv
    letter_range = ('A', 'Z')

    for arg in sys.argv[1:]:
        if arg.startswith('--range'):
            # Handle both --range=A-E and --range A-E
            if '=' in arg:
                letter_range = parse_range_arg(arg.split('=', 1)[1])
            else:
                idx = sys.argv.index(arg)
                if idx + 1 < len(sys.argv):
                    letter_range = parse_range_arg(sys.argv[idx + 1])

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    rebuild_profiles(dry_run=dry_run, letter_range=letter_range)


if __name__ == '__main__':
    main()
