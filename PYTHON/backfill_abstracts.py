#!/usr/bin/env python3
"""
backfill_abstracts.py — Backfill missing YAML abstract: fields

Finds papers with empty/missing YAML abstract: and fills them from:
  Phase A: Body ## Abstract section (>50 chars) → copy to YAML
  Phase B: PDF extract file → mine abstract from raw PDF text
  Phase C: arXiv API (via url: field) or Semantic Scholar (via doi: field)

Safety:
  - YAML update via re.subn() regex — never parse→rebuild round-trip
  - Atomic writes: PID-scoped temp file + os.replace()
  - No file deletions
  - Date-prefixed JSON log

Usage:
  ../.venv/bin/python PYTHON/backfill_abstracts.py [--dry-run] [--phase A|B|C|all]
"""

import sys
import os
import re
import json
import time
import functools
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Tuple

# Force stdout flushing
print = functools.partial(print, flush=True)

# Setup imports
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from yaml_frontmatter_utils import read_paper, validate_frontmatter
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, LOGS_DIR

# Reuse API fetch functions from fix_corrupted_abstracts
from fix_corrupted_abstracts import get_arxiv_abstract, get_semantic_scholar_abstract

# Reuse PDF extract mining from batch_abstract_and_classify
from batch_abstract_and_classify import extract_abstract_from_pdf_extract, truncate_for_yaml


# =============================================================================
# DISCOVERY — find papers with empty/missing YAML abstract
# =============================================================================

def has_empty_abstract(frontmatter: str) -> bool:
    """Check if YAML abstract: field is empty, missing, or placeholder."""
    match = re.search(r'^abstract:\s*("?\s*"?\s*)$', frontmatter, re.MULTILINE)
    if match:
        return True  # abstract: "" or abstract:  (empty)
    # Check if field is entirely missing
    if not re.search(r'^abstract:', frontmatter, re.MULTILINE):
        return True
    return False


def extract_body_abstract(body: str) -> Optional[str]:
    """Extract abstract text from ## Abstract body section (>50 chars)."""
    if '## Abstract' not in body:
        return None

    parts = body.split('## Abstract', 1)
    if len(parts) < 2:
        return None

    section = parts[1]
    # Find the next section header
    next_header = re.search(r'\n## ', section)
    if next_header:
        section = section[:next_header.start()]

    text = section.strip()

    # Skip placeholders
    placeholders = [
        'no abstract available',
        '*(to be fetched)*',
        'abstract not available',
        'n/a',
    ]
    if not text or text.lower().strip('* ') in placeholders:
        return None
    if len(text) < 50:
        return None

    return text


def extract_urls_from_frontmatter(frontmatter: str) -> dict:
    """Extract url: and doi: fields from frontmatter."""
    urls = {'arxiv': None, 'doi': None}

    url_match = re.search(r'^url:\s*"?([^"\n]+)"?', frontmatter, re.MULTILINE)
    if url_match:
        url = url_match.group(1).strip()
        if 'arxiv.org' in url:
            urls['arxiv'] = url

    doi_match = re.search(r'^doi:\s*"?([^"\n]+)"?', frontmatter, re.MULTILINE)
    if doi_match:
        doi = doi_match.group(1).strip()
        if doi:
            urls['doi'] = doi

    # Also check url: for DOI if no doi: field
    if not urls['doi'] and url_match:
        url = url_match.group(1).strip()
        doi_in_url = re.search(r'(10\.\d+/[^\s"]+)', url)
        if doi_in_url:
            urls['doi'] = doi_in_url.group(1).rstrip('.,)')

    return urls


# =============================================================================
# YAML UPDATE — safe regex replacement
# =============================================================================

def update_yaml_abstract(frontmatter: str, abstract_text: str) -> str:
    """
    Safely update the abstract: field in frontmatter using regex.

    Uses re.subn() — never parse→rebuild round-trip.
    """
    # Make YAML-safe: single line, replace double quotes with single
    yaml_abstract = truncate_for_yaml(abstract_text, max_len=500)
    yaml_abstract = yaml_abstract.replace('"', "'")
    replacement = f'abstract: "{yaml_abstract}"'

    pattern = r'^abstract:.*$'
    new_fm, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)

    if count == 0:
        # Field doesn't exist — append it before the closing ---
        new_fm = frontmatter.rstrip() + '\n' + replacement

    return new_fm


def update_body_abstract(body: str, abstract_text: str) -> str:
    """Update the ## Abstract body section if it's empty/placeholder."""
    if '## Abstract' not in body:
        return body

    parts = body.split('## Abstract', 1)
    if len(parts) < 2:
        return body

    section = parts[1]
    next_header = re.search(r'\n## ', section)

    if next_header:
        existing = section[:next_header.start()].strip()
        rest = section[next_header.start():]
    else:
        existing = section.strip()
        rest = ''

    # Only replace if existing is empty or placeholder
    placeholders = [
        'no abstract available',
        '*(to be fetched)*',
        'abstract not available',
        'n/a',
        '',
    ]
    if existing.lower().strip('* ') not in placeholders:
        return body  # Don't overwrite existing content

    new_body = parts[0] + '## Abstract\n\n' + abstract_text + '\n' + rest
    return new_body


# =============================================================================
# ATOMIC WRITE
# =============================================================================

def atomic_write(filepath: Path, content: str):
    """Write file atomically using PID-scoped temp + os.replace()."""
    tmp_path = filepath.parent / f".tmp.{os.getpid()}.{filepath.name}"
    tmp_path.write_text(content, encoding='utf-8')
    os.replace(str(tmp_path), str(filepath))


def reconstruct_content(frontmatter: str, body: str) -> str:
    """Reconstruct full markdown from frontmatter + body."""
    return f"---\n{frontmatter.rstrip()}\n---\n{body}"


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def find_papers_missing_abstract() -> List[Tuple[Path, str, str]]:
    """Find all papers with empty/missing YAML abstract:.

    Returns list of (path, frontmatter, body) tuples.
    """
    results = []
    for f in sorted(PAPERS_DIR.iterdir()):
        if not f.suffix == '.md':
            continue
        try:
            frontmatter, body = read_paper(f)
            if has_empty_abstract(frontmatter):
                results.append((f, frontmatter, body))
        except Exception as e:
            print(f"  WARN: Could not read {f.name}: {e}")
    return results


def process_phase_a(papers: list, dry_run: bool) -> dict:
    """Phase A: Copy body ## Abstract section → YAML abstract: field."""
    stats = {'attempted': 0, 'filled': 0, 'skipped': 0, 'filled_papers': []}

    for path, frontmatter, body in papers:
        stats['attempted'] += 1
        abstract = extract_body_abstract(body)

        if not abstract:
            stats['skipped'] += 1
            continue

        new_fm = update_yaml_abstract(frontmatter, abstract)
        name = path.stem[:70]

        if dry_run:
            print(f"  [A] DRY-RUN would fill: {name}")
            stats['filled'] += 1
            stats['filled_papers'].append(path.name)
            continue

        # Validate before writing
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"  [A] WARN validation: {name}: {issues}")
            stats['skipped'] += 1
            continue

        content = reconstruct_content(new_fm, body)
        atomic_write(path, content)
        print(f"  [A] FILLED from body: {name}")
        stats['filled'] += 1
        stats['filled_papers'].append(path.name)

    return stats


def process_phase_b(papers: list, dry_run: bool) -> dict:
    """Phase B: Mine abstract from PDF extract file."""
    stats = {'attempted': 0, 'filled': 0, 'skipped': 0, 'filled_papers': []}

    for path, frontmatter, body in papers:
        stats['attempted'] += 1
        abstract = extract_abstract_from_pdf_extract(path)

        if not abstract:
            stats['skipped'] += 1
            continue

        new_fm = update_yaml_abstract(frontmatter, abstract)
        new_body = update_body_abstract(body, abstract)
        name = path.stem[:70]

        if dry_run:
            print(f"  [B] DRY-RUN would fill: {name}")
            stats['filled'] += 1
            stats['filled_papers'].append(path.name)
            continue

        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"  [B] WARN validation: {name}: {issues}")
            stats['skipped'] += 1
            continue

        content = reconstruct_content(new_fm, new_body)
        atomic_write(path, content)
        print(f"  [B] FILLED from PDF extract: {name}")
        stats['filled'] += 1
        stats['filled_papers'].append(path.name)

    return stats


def process_phase_c(papers: list, dry_run: bool) -> dict:
    """Phase C: Fetch abstract from arXiv or Semantic Scholar API."""
    stats = {'attempted': 0, 'filled': 0, 'skipped': 0,
             'filled_papers': [], 'api_errors': []}

    for path, frontmatter, body in papers:
        stats['attempted'] += 1
        urls = extract_urls_from_frontmatter(frontmatter)
        name = path.stem[:70]
        abstract = None

        # Try arXiv first
        if urls['arxiv']:
            print(f"  [C] Trying arXiv for: {name}")
            abstract = get_arxiv_abstract(urls['arxiv'])
            time.sleep(3)  # arXiv rate limit

        # Fall back to Semantic Scholar
        if not abstract and urls['doi']:
            print(f"  [C] Trying S2 for: {name}")
            abstract = get_semantic_scholar_abstract(urls['doi'])
            time.sleep(10)  # S2 rate limit (needs 10s+ without API key)

        if not abstract:
            stats['skipped'] += 1
            print(f"  [C] NO SOURCE: {name}")
            continue

        new_fm = update_yaml_abstract(frontmatter, abstract)
        new_body = update_body_abstract(body, abstract)

        if dry_run:
            preview = abstract[:80] + '...' if len(abstract) > 80 else abstract
            print(f"  [C] DRY-RUN would fill: {name}")
            print(f"       Preview: {preview}")
            stats['filled'] += 1
            stats['filled_papers'].append(path.name)
            continue

        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"  [C] WARN validation: {name}: {issues}")
            stats['skipped'] += 1
            continue

        content = reconstruct_content(new_fm, new_body)
        atomic_write(path, content)
        print(f"  [C] FILLED from API: {name}")
        stats['filled'] += 1
        stats['filled_papers'].append(path.name)

    return stats


def main():
    # Parse CLI args
    dry_run = '--dry-run' in sys.argv
    phase_arg = 'ALL'
    for i, arg in enumerate(sys.argv):
        if arg == '--phase' and i + 1 < len(sys.argv):
            phase_arg = sys.argv[i + 1].upper()

    phases_to_run = list('ABC') if phase_arg == 'ALL' else [phase_arg]

    print("=" * 60)
    print("ABSTRACT BACKFILL")
    print(f"  Phases: {', '.join(phases_to_run)}")
    print(f"  Dry run: {dry_run}")
    print("=" * 60)

    # Step 1: Discover papers with missing abstracts
    print("\nScanning papers for empty/missing YAML abstract:...")
    missing = find_papers_missing_abstract()
    print(f"Found {len(missing)} papers with empty/missing abstract.\n")

    if not missing:
        print("Nothing to do.")
        return

    # List them
    for i, (path, _, _) in enumerate(missing, 1):
        print(f"  {i:3d}. {path.stem[:75]}")
    print()

    # Track overall results
    all_stats = {}
    remaining = list(missing)

    # Phase A: Body → YAML
    if 'A' in phases_to_run and remaining:
        print("-" * 60)
        print(f"PHASE A: Body section → YAML ({len(remaining)} candidates)")
        print("-" * 60)
        stats_a = process_phase_a(remaining, dry_run)
        all_stats['A'] = stats_a
        print(f"  Phase A: {stats_a['filled']}/{stats_a['attempted']} filled\n")

        # Remove filled papers from remaining (re-scan for unfilled)
        if stats_a['filled'] > 0:
            filled_names = set(stats_a['filled_papers'])
            remaining = [(p, fm, b) for p, fm, b in remaining
                         if p.name not in filled_names]

    # Phase B: PDF extract → YAML
    if 'B' in phases_to_run and remaining:
        print("-" * 60)
        print(f"PHASE B: PDF extract mining ({len(remaining)} candidates)")
        print("-" * 60)
        stats_b = process_phase_b(remaining, dry_run)
        all_stats['B'] = stats_b
        print(f"  Phase B: {stats_b['filled']}/{stats_b['attempted']} filled\n")

        if stats_b['filled'] > 0:
            filled_names = set(stats_b['filled_papers'])
            remaining = [(p, fm, b) for p, fm, b in remaining
                         if p.name not in filled_names]

    # Phase C: API fetch → YAML
    if 'C' in phases_to_run and remaining:
        print("-" * 60)
        print(f"PHASE C: API fetch ({len(remaining)} candidates)")
        print("-" * 60)
        stats_c = process_phase_c(remaining, dry_run)
        all_stats['C'] = stats_c
        print(f"  Phase C: {stats_c['filled']}/{stats_c['attempted']} filled\n")

        if stats_c['filled'] > 0:
            filled_names = set(stats_c['filled_papers'])
            remaining = [(p, fm, b) for p, fm, b in remaining
                         if p.name not in filled_names]

    # Summary
    total_filled = sum(s.get('filled', 0) for s in all_stats.values())
    total_attempted = len(missing)

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Total missing:  {total_attempted}")
    print(f"  Total filled:   {total_filled}")
    print(f"  Still missing:  {len(remaining)}")
    for phase, stats in all_stats.items():
        print(f"  Phase {phase}: {stats['filled']}/{stats['attempted']} "
              f"(skipped {stats['skipped']})")

    if remaining:
        print("\nStill missing abstracts:")
        for path, _, _ in remaining:
            print(f"  - {path.name}")

    # Write JSON report
    today = datetime.now().strftime('%Y%m%d')
    report = {
        'date': today,
        'total_missing': total_attempted,
        'total_filled': total_filled,
        'still_missing': len(remaining),
        'still_missing_papers': [p.name for p, _, _ in remaining],
        'phases': {},
        'dry_run': dry_run,
    }
    for phase, stats in all_stats.items():
        report['phases'][phase] = {
            'filled': stats['filled'],
            'attempted': stats['attempted'],
            'skipped': stats['skipped'],
            'filled_papers': stats['filled_papers'],
        }

    report_path = LOGS_DIR / f"{today}-abstract_backfill_report.json"
    LOGS_DIR.mkdir(exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    print(f"\nReport: {report_path}")


if __name__ == '__main__':
    main()
