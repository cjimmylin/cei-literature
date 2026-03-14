#!/usr/bin/env python3
"""
Import Zero-Coverage Religious Tradition Papers into CEI Literature Vault

Reads the consolidated master list JSON from consolidate_zero_coverage_search.py
and creates paper .md files with YAML frontmatter including the
`religious_values_list` field.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/import_zero_coverage_papers.py [--dry-run]
    ../.venv/bin/python PYTHON/import_zero_coverage_papers.py START END [--dry-run]

Run from CEI-Lit-WS/ directory.
"""

import functools
import json
import re
import sys
from pathlib import Path

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from lib.yaml_utils import validate_frontmatter

PAPERS_DIR = WORKSPACE_ROOT / "papers"
LOGS_DIR = WORKSPACE_ROOT / "logs"
DATE_PREFIX = "20260216"
DATE_ADDED = DATE_PREFIX
MASTER_LIST = LOGS_DIR / f"{DATE_PREFIX}-zero_coverage_search_master_list.json"

# Key prefix for this search batch
KEY_PREFIX = "ZERO"


def get_next_key_number(papers_dir, key_prefix="ZERO"):
    max_key = 0
    pattern = re.compile(rf'^key:\s*{re.escape(key_prefix)}(\d+)', re.MULTILINE)
    for p in papers_dir.iterdir():
        if not p.name.endswith('.md'):
            continue
        try:
            content = p.read_text(encoding='utf-8')
            m = pattern.search(content)
            if m:
                num = int(m.group(1))
                if num > max_key:
                    max_key = num
        except Exception:
            continue
    return max_key + 1


def sanitize_filename(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'[<>:"/\\|?*\[\]\(\),]', '', s)
    s = s.replace('--', '-').replace('\u2014', '-')
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > 70:
        s = s[:70].rsplit(' ', 1)[0]
    return s


def get_first_author_surname(authors_str):
    if not authors_str or authors_str.lower() in ('unknown', 'n/a', ''):
        return "Unknown"
    authors_str = re.sub(r'^\[(.+)\]$', r'\1', authors_str.strip())
    if 'unknown' in authors_str.lower():
        return "Unknown"
    if ';' in authors_str:
        first = authors_str.split(';')[0].strip()
    else:
        first_comma_idx = authors_str.find(',')
        if first_comma_idx > 0:
            after_comma = authors_str[first_comma_idx + 1:].strip()
            next_part = after_comma.split(',')[0].strip().split(' ')[0].strip()
            is_initial = (len(next_part) == 1) or (len(next_part) <= 4 and '.' in next_part)
            if is_initial:
                first = authors_str.split(',')[0].strip()
                first = re.sub(r'\s+et\s+al\.?$', '', first).strip()
                return first
            else:
                first = authors_str.split(',')[0].strip()
        else:
            first = authors_str.strip()
    first = re.sub(r'\s+et\s+al\.?$', '', first).strip()
    parts = first.split()
    if parts:
        return parts[-1].strip()
    return "Unknown"


def get_first_author_full(authors_str):
    if not authors_str or authors_str.lower() in ('unknown', 'n/a', ''):
        return "Unknown"
    authors_str = re.sub(r'^\[(.+)\]$', r'\1', authors_str.strip())
    if 'unknown' in authors_str.lower():
        return "Unknown"
    if ';' in authors_str:
        first = authors_str.split(';')[0].strip()
    else:
        first_comma_idx = authors_str.find(',')
        if first_comma_idx > 0:
            after_comma = authors_str[first_comma_idx + 1:].strip()
            next_part = after_comma.split(',')[0].strip().split(' ')[0].strip()
            is_initial = (len(next_part) == 1) or (len(next_part) <= 4 and '.' in next_part)
            if is_initial:
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


def get_last_author_full(authors_str):
    if not authors_str or authors_str.lower() in ('unknown', 'n/a', ''):
        return "Unknown"
    authors_str = re.sub(r'^\[(.+)\]$', r'\1', authors_str.strip())
    authors_str = re.sub(r'\s+et\s+al\.?$', '', authors_str).strip()
    if ';' in authors_str:
        parts = [a.strip() for a in authors_str.split(';') if a.strip()]
    else:
        parts = [a.strip() for a in authors_str.split(',') if a.strip()]
    if not parts:
        return "Unknown"
    if len(parts) == 1:
        return get_first_author_full(authors_str)
    last = parts[-1].strip()
    last = re.sub(r'\s+et\s+al\.?$', '', last).strip()
    return last if last else "Unknown"


def determine_type(venue):
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
    return 'conferencePaper'


def yaml_quote(value):
    if not value:
        return ''
    needs_quote = any(c in value for c in [':', '[', ']', '#', '{', '}', '"', "'", '&', '*', '!', '|', '>'])
    if needs_quote:
        escaped = value.replace('"', "'")
        return f'"{escaped}"'
    return value


def derive_religious_values(traditions):
    """Derive religious_values from the traditions list."""
    if not traditions:
        return ""
    if isinstance(traditions, str):
        traditions = [t.strip() for t in traditions.split(',')]
    if len(traditions) == 1:
        return traditions[0]
    if len(traditions) <= 3:
        return ", ".join(traditions)
    return "Multi-tradition"


def create_paper_file(paper, num, papers_dir, dry_run=False):
    authors = paper.get('authors', 'Unknown')
    if isinstance(authors, list):
        authors = '; '.join(a for a in authors if a and a.strip().lower() not in ('not fully extracted', 'and others'))
    if not authors or (isinstance(authors, str) and authors.strip().lower() in ('unknown', 'n/a', 'none', '')):
        authors = 'Unknown'
    title = paper.get('title', 'Untitled')
    year = str(paper.get('year', '2025'))

    surname = get_first_author_surname(authors)
    first_author_full = get_first_author_full(authors)
    last_author_full = get_last_author_full(authors)

    short_title = sanitize_filename(title)
    surname = re.sub(r'[<>:"/\\|?*\[\]\(\),;]', '', surname).strip()
    filename = f"{year}-{surname}-{short_title}.md"
    filepath = papers_dir / filename

    if filepath.exists():
        return None, f"SKIP (exists): {filename}"

    existing = list(papers_dir.glob(f"{year}-{surname}-*.md"))
    for ef in existing:
        existing_title = ef.stem.split('-', 2)[2] if ef.stem.count('-') >= 2 else ''
        if existing_title and short_title:
            if existing_title.lower()[:25] == short_title.lower()[:25]:
                return None, f"SKIP (similar): {filename} ~ {ef.name}"

    if dry_run:
        return filepath, f"DRY RUN: {filename}"

    key = f"{KEY_PREFIX}{num:04d}"
    venue = paper.get('venue', paper.get('source', ''))
    paper_type = determine_type(venue)

    url = paper.get('url', '')
    arxiv_id = paper.get('arxiv_id', '')
    doi = paper.get('doi', '')
    data_url = paper.get('data_url', '')
    benchmark_name = paper.get('benchmark_name', '')

    if not url:
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        elif doi:
            url = f"https://doi.org/{doi}"

    external_pdf = ''
    if arxiv_id:
        aid = arxiv_id.replace('arXiv:', '').strip()
        external_pdf = f"https://arxiv.org/pdf/{aid}.pdf"

    # Traditions list
    traditions = paper.get('traditions_covered', [])
    if isinstance(traditions, list):
        traditions_str = ", ".join(sorted(set(traditions)))
    elif isinstance(traditions, str):
        traditions_str = traditions
    else:
        traditions_str = ""

    religious_values = derive_religious_values(traditions)

    authors_clean = authors.replace('[[', '').replace(']]', '')

    fm_lines = []
    fm_lines.append('Human View: ')
    fm_lines.append('Human View Date: ')
    fm_lines.append('Human View note: ')
    fm_lines.append('Not AI: ')
    fm_lines.append(f'key: {key}')
    fm_lines.append(f'type: {paper_type}')
    fm_lines.append(f'short_title: {yaml_quote(title)}')
    fm_lines.append(f'year: {year}')
    fm_lines.append(f'first_author: "[[{first_author_full}]]"')
    fm_lines.append(f'last_author: "[[{last_author_full}]]"')
    fm_lines.append(f'authors: {yaml_quote(authors_clean)}')
    if doi:
        fm_lines.append(f'doi: {doi}')
    if url:
        fm_lines.append(f'url: "{url}"')
    if external_pdf:
        fm_lines.append(f'external_pdf: "{external_pdf}"')
    fm_lines.append(f'publication: {yaml_quote(venue)}')
    fm_lines.append(f'local_pdf: ')
    fm_lines.append(f'pdf_extract: ')
    fm_lines.append(f'DATE_ADDED: {DATE_ADDED}')
    fm_lines.append('ethics_overall: ')
    fm_lines.append('virtue_ethics: ')
    fm_lines.append('deontological_ethics: ')
    fm_lines.append('utilitarian_ethics: ')
    fm_lines.append('national_ethnic_cultural: ')
    fm_lines.append('cultures_nationalities_list: ')
    fm_lines.append('languages_list: ')
    # Religious tradition fields
    if religious_values:
        fm_lines.append(f'religious_values: {yaml_quote(religious_values)}')
    else:
        fm_lines.append('religious_values: ')
    fm_lines.append('rv_islam: 0')
    fm_lines.append('rv_christianity: 0')
    fm_lines.append('rv_buddhism: 0')
    fm_lines.append('rv_judaism: 0')
    fm_lines.append('rv_hinduism: 0')
    fm_lines.append('rv_sikhism: 0')
    fm_lines.append('rv_confucianism: 0')
    fm_lines.append('rv_taoism: 0')
    fm_lines.append('rv_shinto: 0')
    fm_lines.append('rv_jainism: 0')
    fm_lines.append('rv_bahai: 0')
    fm_lines.append('rv_zoroastrianism: 0')
    fm_lines.append('rv_ubuntu: 0')
    fm_lines.append('rv_indigenous: 0')
    if traditions_str:
        fm_lines.append(f'religious_values_list: "{traditions_str}"')
    else:
        fm_lines.append('religious_values_list: ')
    fm_lines.append('mp_mft: 0')
    fm_lines.append('mp_schwartz: 0')
    fm_lines.append('mp_trolley: 0')
    fm_lines.append('mp_kohlberg: 0')
    fm_lines.append('mp_dual_process: 0')
    fm_lines.append('mp_intuitionist: 0')
    fm_lines.append('mp_dyadic: 0')
    fm_lines.append('mp_identity: 0')
    fm_lines.append('moral_psychology: "N/A"')
    fm_lines.append('newtags: ')
    fm_lines.append('is_benchmark: ')
    fm_lines.append('is_eval: ')
    fm_lines.append('is_dataset: ')
    fm_lines.append('data_description: ')
    fm_lines.append('data_metrics: ')
    fm_lines.append('LLM_assessed: ')
    fm_lines.append(f'DATA_URL: "{data_url}"' if data_url and data_url.lower() not in ('n/a', 'none', '') else 'DATA_URL: ')
    fm_lines.append('tags: ')
    fm_lines.append('abstract: ')

    frontmatter = '\n'.join(fm_lines)

    valid, errors = validate_frontmatter(frontmatter)
    if not valid:
        return None, f"VALIDATION ERROR: {filename}: {errors}"

    body_lines = []
    body_lines.append(f'# {title}')
    body_lines.append('')
    body_lines.append('## Authors')
    body_lines.append('')

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
    body_lines.append(f'**Year:** {year}')
    body_lines.append('')
    body_lines.append(f'**Type:** {paper_type}')
    body_lines.append('')
    if venue:
        body_lines.append(f'**Venue:** {venue}')
        body_lines.append('')
    if doi:
        body_lines.append(f'**DOI:** [{doi}](https://doi.org/{doi})')
        body_lines.append('')
    if traditions_str:
        body_lines.append(f'**Religious Traditions:** {traditions_str}')
        body_lines.append('')
    if benchmark_name:
        body_lines.append(f'**Benchmark:** {benchmark_name}')
        body_lines.append('')

    body_lines.append('## Links')
    body_lines.append('')
    if arxiv_id:
        body_lines.append(f'- **arXiv:** https://arxiv.org/abs/{arxiv_id}')
    if doi:
        body_lines.append(f'- **DOI:** https://doi.org/{doi}')
    if url and 'arxiv.org' not in url and 'doi.org' not in url:
        body_lines.append(f'- **URL:** {url}')
    if data_url and data_url.lower() not in ('n/a', 'none', ''):
        body_lines.append(f'- **Code/Data:** {data_url}')
    body_lines.append('')

    body_lines.append('## Abstract')
    body_lines.append('')
    snippet = paper.get('abstract_snippet', '')
    if snippet:
        body_lines.append(snippet)
    else:
        body_lines.append('*(To be fetched)*')
    body_lines.append('')

    body_lines.append('## Notes')
    body_lines.append('')
    source_agents = paper.get('source_agents', paper.get('source_agent', ''))
    if isinstance(source_agents, list):
        source_agents = ", ".join(source_agents)
    body_lines.append(f'**Source:** Zero-Coverage Religious Tradition Search ({DATE_PREFIX}), Agent {source_agents}')
    relevance = paper.get('relevance_notes', '')
    if relevance:
        body_lines.append(f'**Relevance:** {relevance}')
    body_lines.append('')

    body_lines.append('## Tags')
    body_lines.append('')

    body = '\n'.join(body_lines) + '\n'

    content = f"---\n{frontmatter}\n---\n{body}"
    filepath.write_text(content, encoding='utf-8')

    return filepath, f"CREATED: {filename}"


def main():
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--dry-run']

    start = None
    end = None
    if len(args) >= 2:
        start = int(args[0])
        end = int(args[1])

    if not MASTER_LIST.exists():
        print(f"ERROR: Master list not found: {MASTER_LIST}")
        print(f"Run consolidate_zero_coverage_search.py first.")
        sys.exit(1)

    data = json.loads(MASTER_LIST.read_text(encoding='utf-8'))
    new_papers = data.get('new_papers', [])
    print(f"Master list: {len(new_papers)} new papers to import")

    if start is not None and end is not None:
        new_papers = new_papers[start - 1:end]
        print(f"Processing papers {start}-{end} ({len(new_papers)} papers)")

    key_start = get_next_key_number(PAPERS_DIR, KEY_PREFIX)
    print(f"Auto-detected next key: {KEY_PREFIX}{key_start:04d}")

    if dry_run:
        print("*** DRY RUN MODE ***")
    print()

    created = 0
    skipped = 0
    errors = 0

    for i, paper in enumerate(new_papers):
        key_num = key_start + i
        display_num = i + 1
        try:
            filepath, msg = create_paper_file(paper, key_num, PAPERS_DIR, dry_run)
            print(f"  [{display_num:3d}] {msg}")
            if filepath:
                created += 1
            else:
                skipped += 1
        except Exception as e:
            title = paper.get('title', 'Unknown')[:50]
            print(f"  [{display_num:3d}] ERROR: {title}... \u2014 {e}")
            errors += 1

    print(f"\n{'='*50}")
    print(f"IMPORT SUMMARY")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors:  {errors}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
