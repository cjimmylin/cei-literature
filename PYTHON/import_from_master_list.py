#!/usr/bin/env python3
"""
Import papers from the Exhaustive Search master list into the vault.
Creates paper .md files with YAML frontmatter.

Usage: python3 PYTHON/import_from_master_list.py START END [--dry-run]
  START: first paper number (1-indexed, inclusive)
  END: last paper number (1-indexed, inclusive)
  --dry-run: print what would be created without writing files

Run from CEI-Lit-WS/ directory.
"""

import re
import sys
from pathlib import Path

MASTER_LIST = Path("logs/20260207-MASTER_PAPER_LIST_2026_02_07.md")
PAPERS_DIR = Path("papers")
DATE_ADDED = "20260207"


def parse_master_list(filepath):
    """Parse all numbered entries from the master list."""
    content = filepath.read_text(encoding='utf-8')

    # Find all entry headers: ### N. Title
    entry_pattern = re.compile(r'^### (\d+)\.\s+(.+)$', re.MULTILINE)
    matches = list(entry_pattern.finditer(content))

    entries = []
    for i, match in enumerate(matches):
        num = int(match.group(1))
        title = match.group(2).strip()

        # Get text between this entry and the next (or end of file)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        block = content[start:end]

        entry = parse_entry(num, title, block)
        entries.append(entry)

    return entries


def parse_entry(num, title, block):
    """Parse a single entry block into a dict."""
    entry = {
        'num': num,
        'title': title,
        'authors': '',
        'year': '',
        'venue': '',
        'arxiv_id': '',
        'arxiv_url': '',
        'doi': '',
        'doi_url': '',
        'dataset_size': '',
        'code_data': '',
        'readiness': '',
        'source_agents': '',
    }

    for line in block.split('\n'):
        line = line.strip()
        if not line.startswith('- **'):
            continue

        # Parse "- **Key:** Value" pattern (colon may be inside or outside the bold)
        m = re.match(r'^- \*\*(.+?)\*\*\s*(.*)$', line)
        if not m:
            continue

        key = m.group(1).rstrip(':').strip()
        value = m.group(2).strip()

        if key == 'Authors':
            entry['authors'] = value
        elif key == 'Year':
            entry['year'] = value
        elif key == 'Venue':
            entry['venue'] = value
        elif key == 'arXiv':
            # Format: [ID](url) or bare ID
            arxiv_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', value)
            if arxiv_match:
                entry['arxiv_id'] = arxiv_match.group(1)
                entry['arxiv_url'] = arxiv_match.group(2)
            else:
                entry['arxiv_id'] = value.strip()
                entry['arxiv_url'] = f"https://arxiv.org/abs/{value.strip()}"
        elif key == 'DOI':
            doi_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', value)
            if doi_match:
                entry['doi'] = doi_match.group(1)
                entry['doi_url'] = doi_match.group(2)
            else:
                entry['doi'] = value.strip()
                entry['doi_url'] = f"https://doi.org/{value.strip()}" if value.strip() else ''
        elif key == 'Dataset Size':
            entry['dataset_size'] = value
        elif key == 'Code/Data':
            entry['code_data'] = value
        elif key == 'Implementation Readiness':
            entry['readiness'] = value
        elif key.startswith('Source Agent') or key.startswith('Source agent'):
            entry['source_agents'] = value

    return entry


def sanitize_filename(s):
    """Sanitize a string for use in a filename."""
    # Remove markdown link artifacts
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    # Remove problematic characters (including parentheses, brackets, commas)
    s = re.sub(r'[<>:"/\\|?*\[\]\(\),]', '', s)
    # Replace -- with -
    s = s.replace('--', '-').replace('—', '-')
    # Collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    # Truncate to reasonable length for filename
    if len(s) > 70:
        s = s[:70].rsplit(' ', 1)[0]
    return s


def get_first_author_surname(authors_str):
    """Extract first author's surname.

    Handles formats:
    - "Aaron J. Snoswell, Daniel Kilov, Seth Lazar" → Snoswell
    - "Morlat, G. et al." → Morlat
    - "Goel, M., Das, A" → Goel
    - "William Guey et al." → Guey
    """
    if not authors_str or authors_str.lower() == 'unknown':
        return "Unknown"

    # Strip brackets (e.g., "[Authors from Kurt Gray Lab]")
    authors_str = re.sub(r'^\[(.+)\]$', r'\1', authors_str.strip())
    if 'unknown' in authors_str.lower() or authors_str.startswith('Authors from'):
        return "Unknown"

    # First check for semicolons (standard separator)
    if ';' in authors_str:
        first = authors_str.split(';')[0].strip()
    else:
        # Comma-separated: need to distinguish "Surname, G." from "Given Surname, Given2 Surname2"
        # Heuristic: if first comma is followed by a single initial (e.g., ", G."), it's "Surname, Initial"
        first_comma_idx = authors_str.find(',')
        if first_comma_idx > 0:
            after_comma = authors_str[first_comma_idx + 1:].strip()
            # Check if what follows the first comma is an initial (like "G.", "M.", "J.P.")
            # NOT a full name like "Han" or "Daniel"
            next_part = after_comma.split(',')[0].strip().split(' ')[0].strip()
            is_initial = (len(next_part) == 1) or (len(next_part) <= 4 and '.' in next_part)
            if is_initial:
                # "Surname, G." format — take everything before first comma
                first = authors_str.split(',')[0].strip()
                first = re.sub(r'\s+et\s+al\.?$', '', first).strip()
                return first  # This IS the surname already
            else:
                # "Given Surname, Given2 Surname2" format — first author is before first comma
                first = authors_str.split(',')[0].strip()
        else:
            first = authors_str.strip()

    # Handle "et al." suffix
    first = re.sub(r'\s+et\s+al\.?$', '', first).strip()

    # Take last word as surname
    parts = first.split()
    if parts:
        return parts[-1].strip()

    return "Unknown"


def get_first_author_full(authors_str):
    """Get first author's full name for wikilink.

    Returns the best human-readable name for the first author.
    """
    if not authors_str or authors_str.lower() == 'unknown':
        return "Unknown"

    # Strip brackets
    authors_str = re.sub(r'^\[(.+)\]$', r'\1', authors_str.strip())
    if 'unknown' in authors_str.lower() or authors_str.startswith('Authors from'):
        return "Unknown"

    # Split by semicolons first
    if ';' in authors_str:
        first = authors_str.split(';')[0].strip()
    else:
        # Comma-separated — detect format
        first_comma_idx = authors_str.find(',')
        if first_comma_idx > 0:
            after_comma = authors_str[first_comma_idx + 1:].strip()
            next_part = after_comma.split(',')[0].strip().split(' ')[0].strip()
            is_initial = (len(next_part) == 1) or (len(next_part) <= 4 and '.' in next_part)
            if is_initial:
                # "Surname, G. et al." format — take surname + initial
                parts = authors_str.split(',')
                surname = parts[0].strip()
                given = parts[1].strip() if len(parts) > 1 else ''
                given = re.sub(r'\s+et\s+al\.?$', '', given).strip()
                if given:
                    return f"{given} {surname}"
                return surname
            else:
                first = authors_str.split(',')[0].strip()
        else:
            first = authors_str.strip()

    first = re.sub(r'\s+et\s+al\.?$', '', first).strip()
    return first.strip()


def determine_type(venue):
    """Determine paper type from venue string."""
    if not venue:
        return 'preprint'
    venue_lower = venue.lower()

    if 'arxiv' in venue_lower or 'preprint' in venue_lower:
        return 'preprint'

    journal_keywords = ['journal', 'nature', 'science', 'pnas', 'transactions',
                        'neurocomputing', 'analytics', 'topics in cognitive',
                        'machine intelligence', 'tosem', 'frontiers']
    for kw in journal_keywords:
        if kw in venue_lower:
            return 'journalArticle'

    # Named venue = likely conference
    return 'conferencePaper'


def generate_key(num):
    """Generate a unique key for non-Zotero papers (8 chars, matches Zotero key format)."""
    return f"EXSR{num:04d}"


def yaml_quote(value):
    """Quote a YAML value if it contains special characters."""
    if not value:
        return ''
    # Must quote if contains: colon, brackets, hash, quotes, or leading/trailing spaces
    needs_quote = any(c in value for c in [':', '[', ']', '#', '{', '}', '"', "'", '&', '*', '!', '|', '>'])
    if needs_quote:
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'
    return value


def create_paper_file(entry, papers_dir, dry_run=False):
    """Create a paper .md file for a single entry."""
    surname = get_first_author_surname(entry['authors'])
    first_author_full = get_first_author_full(entry['authors'])

    # Build filename: YYYY-Surname-ShortTitle.md
    short_title = sanitize_filename(entry['title'])
    filename = f"{entry['year']}-{surname}-{short_title}.md"
    filepath = papers_dir / filename

    # Check for existing file with exact name
    if filepath.exists():
        return None, f"SKIP (exists): {filename}"

    # Check for similar filenames (same year + surname)
    existing = list(papers_dir.glob(f"{entry['year']}-{surname}-*.md"))
    for ef in existing:
        # Compare first 25 chars of title portion
        existing_title = ef.stem.split('-', 2)[2] if '-' in ef.stem else ''
        new_title = short_title
        if existing_title and new_title:
            if existing_title.lower()[:25] == new_title.lower()[:25]:
                return None, f"SKIP (similar): {filename} ~ {ef.name}"

    if dry_run:
        return filepath, f"DRY RUN: {filename}"

    # --- Build YAML frontmatter ---
    key = generate_key(entry['num'])
    paper_type = determine_type(entry['venue'])

    url = ''
    if entry['arxiv_url']:
        url = entry['arxiv_url']
    elif entry['doi_url']:
        url = entry['doi_url']
    elif entry['doi']:
        url = f"https://doi.org/{entry['doi']}"

    external_pdf = ''
    if entry['arxiv_id']:
        aid = entry['arxiv_id'].replace('arXiv:', '').strip()
        external_pdf = f"https://arxiv.org/pdf/{aid}.pdf"

    # Clean authors string
    authors_clean = entry['authors'].replace('[[', '').replace(']]', '')

    fm_lines = []
    fm_lines.append('Human View: ')
    fm_lines.append('Human View Date: ')
    fm_lines.append('Human View note: ')
    fm_lines.append('Not AI: ')
    fm_lines.append(f'key: {key}')
    fm_lines.append(f'type: {paper_type}')
    fm_lines.append(f'short_title: {yaml_quote(entry["title"])}')
    fm_lines.append(f'year: {entry["year"]}')
    fm_lines.append(f'first_author: "[[{first_author_full}]]"')
    fm_lines.append(f'authors: {yaml_quote(authors_clean)}')
    if entry['doi']:
        fm_lines.append(f'doi: {entry["doi"]}')
    if url:
        fm_lines.append(f'url: "{url}"')
    if external_pdf:
        fm_lines.append(f'external_pdf: "{external_pdf}"')
    fm_lines.append(f'publication: {yaml_quote(entry["venue"])}')
    fm_lines.append(f'DATE_ADDED: {DATE_ADDED}')
    # Classification fields — blank defaults (to be filled by pipeline)
    fm_lines.append('ethics_overall: ')
    fm_lines.append('virtue_ethics: ')
    fm_lines.append('deontological_ethics: ')
    fm_lines.append('utilitarian_ethics: ')
    fm_lines.append('national_ethnic_cultural: ')
    fm_lines.append('religious_values: ')
    fm_lines.append('moral_psychology: ')
    fm_lines.append('newtags: ')
    fm_lines.append('is_benchmark: ')
    fm_lines.append('is_eval: ')
    fm_lines.append('is_dataset: ')
    fm_lines.append('tags: ')
    fm_lines.append('abstract: ')

    frontmatter = '\n'.join(fm_lines)

    # --- Build body ---
    body_lines = []
    body_lines.append(f'# {entry["title"]}')
    body_lines.append('')
    body_lines.append('## Authors')
    body_lines.append('')

    # Create wikilinked author list
    authors_split = [a.strip() for a in authors_clean.split(';') if a.strip()]
    if not authors_split:
        authors_split = [a.strip() for a in authors_clean.split(',') if a.strip()]
    author_wikilinks = ', '.join(f'[[{a}]]' for a in authors_split)
    body_lines.append(author_wikilinks)
    body_lines.append('')

    body_lines.append('## Metadata')
    body_lines.append('')
    body_lines.append(f'**Authors:** {authors_clean}')
    body_lines.append('')
    body_lines.append(f'**Year:** {entry["year"]}')
    body_lines.append('')
    body_lines.append(f'**Type:** {paper_type}')
    body_lines.append('')
    if entry['venue']:
        body_lines.append(f'**Venue:** {entry["venue"]}')
        body_lines.append('')
    if entry['doi']:
        body_lines.append(f'**DOI:** [{entry["doi"]}](https://doi.org/{entry["doi"]})')
        body_lines.append('')

    body_lines.append('## Links')
    body_lines.append('')
    if entry['arxiv_url']:
        body_lines.append(f'- **arXiv:** {entry["arxiv_url"]}')
    if entry['doi']:
        body_lines.append(f'- **DOI:** https://doi.org/{entry["doi"]}')
    if entry['code_data'] and entry['code_data'].lower() not in ('not specified', 'none listed', 'none', 'n/a', ''):
        body_lines.append(f'- **Code/Data:** {entry["code_data"]}')
    body_lines.append('')

    body_lines.append('## Abstract')
    body_lines.append('')
    body_lines.append('*(To be fetched)*')
    body_lines.append('')

    if entry['dataset_size']:
        body_lines.append('## Dataset Information')
        body_lines.append('')
        body_lines.append(entry['dataset_size'])
        body_lines.append('')

    body_lines.append('## Notes')
    body_lines.append('')
    body_lines.append(f'**Source:** Exhaustive Literature Search (2026-02-07), {entry["source_agents"]}')
    body_lines.append(f'**Implementation Readiness:** {entry["readiness"]}')
    body_lines.append('')

    body_lines.append('## Tags')
    body_lines.append('')

    body = '\n'.join(body_lines) + '\n'

    # --- Write file ---
    content = f"---\n{frontmatter}\n---\n{body}"
    filepath.write_text(content, encoding='utf-8')

    return filepath, f"CREATED: {filename}"


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 PYTHON/import_from_master_list.py START END [--dry-run]")
        print("  START/END: paper numbers (1-indexed, inclusive)")
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    dry_run = '--dry-run' in sys.argv

    if not MASTER_LIST.exists():
        print(f"ERROR: Master list not found: {MASTER_LIST}")
        sys.exit(1)

    if not PAPERS_DIR.exists():
        print(f"ERROR: Papers directory not found: {PAPERS_DIR}")
        sys.exit(1)

    # Parse master list
    entries = parse_master_list(MASTER_LIST)
    print(f"Parsed {len(entries)} entries from master list")

    # Filter to requested range
    batch = [e for e in entries if start <= e['num'] <= end]
    print(f"Processing entries {start}-{end} ({len(batch)} papers)")
    if dry_run:
        print("*** DRY RUN MODE ***")
    print()

    created = 0
    skipped = 0
    errors = 0

    for entry in batch:
        try:
            filepath, msg = create_paper_file(entry, PAPERS_DIR, dry_run)
            print(f"  [{entry['num']:3d}] {msg}")
            if filepath:
                created += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  [{entry['num']:3d}] ERROR: {entry['title'][:50]}... — {e}")
            errors += 1

    print(f"\n{'='*50}")
    print(f"BATCH {start}-{end} SUMMARY")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors:  {errors}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
