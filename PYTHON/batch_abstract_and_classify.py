#!/usr/bin/env python3
"""
batch_abstract_and_classify.py - Combined abstract extraction + 7-stage classification

Processes papers with DATE_ADDED: 20260207 and empty classification fields.

For each paper:
  1. Extract abstract from PDF extract file (if available)
  2. Update paper's ## Abstract section and YAML abstract field
  3. Run all 7 classification stages (keyword/heuristic-based, no LLM API calls):
     - Stage 1-2: ethics_overall, virtue_ethics, deontological_ethics, utilitarian_ethics
     - Stage 3: ethics_perspective (conditional: ethics=Yes, all 3 branches=No)
     - Stage 4: research_topic (conditional: ethics=No)
     - Stage 5: national_ethnic_cultural, religious_values
     - Stage 6: moral_psychology
     - Stage 7: is_benchmark, is_eval, is_dataset, data_description, data_metrics
  4. Update all YAML fields using safe regex-based replacement (no parse/rebuild round-trip)

Usage:
  ../.venv/bin/python PYTHON/batch_abstract_and_classify.py START END [--dry-run]

  START, END: 1-indexed positions in the sorted list of papers needing processing
"""

import sys
import os
import re
import time
from pathlib import Path

# Force stdout flushing to avoid buffering issues in parallel execution
import functools
print = functools.partial(print, flush=True)

# Setup imports from PYTHON/ directory
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR

# Import classification modules (all in same PYTHON/ directory)
import classify_ethics as ce
import classify_ethics_perspective as cep
import classify_non_ethics_topics as cnt
import classify_cultural_religious as ccr
import classify_moral_psych as cmp
import classify_data_nature as cdn


# =============================================================================
# ABSTRACT EXTRACTION FROM PDF EXTRACTS
# =============================================================================

def extract_abstract_from_pdf_extract(paper_path):
    """
    Extract abstract from the corresponding PDF extract file.

    Reads the pdf_extract field from paper YAML, opens the extract file,
    finds the "Abstract" section in the first ~3 pages of raw PDF text,
    and cleans it up (fixing hyphenated line breaks, joining lines, etc.).

    Returns the abstract text, or None if extraction fails.
    """
    content = paper_path.read_text(encoding='utf-8')

    # Find the pdf_extract field in YAML
    match = re.search(r'^pdf_extract:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    if not match or not match.group(1).strip():
        return None

    extract_rel_path = match.group(1).strip()
    extract_path = PAPERS_DIR.parent / extract_rel_path

    if not extract_path.exists():
        return None

    extract_content = extract_path.read_text(encoding='utf-8')

    # Get first ~3 pages of content (abstract is usually on page 1)
    pages_text = ""
    for page_num in range(1, 4):
        pattern = rf'--- Page {page_num} ---\n(.*?)(?=--- Page {page_num + 1} ---|\Z)'
        page_match = re.search(pattern, extract_content, re.DOTALL)
        if page_match:
            pages_text += page_match.group(1)

    if not pages_text:
        return None

    return _extract_abstract_from_text(pages_text)


def _extract_abstract_from_text(pages_text):
    """
    Extract abstract from raw PDF text.

    Handles common formats:
    - "Abstract" on its own line, followed by text
    - "Abstract" followed immediately by text on same line
    - "ABSTRACT" in all caps
    - Abstracts ending at section headings like "1 Introduction", "Keywords:", etc.
    """
    # Find "Abstract" marker (standalone line)
    match = re.search(
        r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*[:\.\-—]?\s*\n',
        pages_text
    )
    if not match:
        # Try "Abstract" followed by text on same line
        match = re.search(
            r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*[:\.\-—]+\s*',
            pages_text
        )
    if not match:
        # Try just "Abstract" as standalone word (common in ACL-style papers)
        match = re.search(
            r'(?:^|\n)\s*(?:Abstract|ABSTRACT)\s*\n',
            pages_text,
            re.IGNORECASE
        )
    if not match:
        return None

    start = match.end()
    remaining = pages_text[start:]

    # Find end of abstract (next section heading)
    end_patterns = [
        r'\n\s*\d+[\.\s]+(?:Introduction|Related|Background|Method|Approach|Problem|Motivation|Overview|Conclusion|Contribution|Preliminar|System|Model|Data|Setup|Experiment)',
        r'\n\s*(?:Introduction|INTRODUCTION|Related Work|RELATED WORK)\s*\n',
        r'\n\s*(?:Keywords|KEYWORDS|Key\s*[Ww]ords|KEY\s*WORDS)\s*[:\n]',
        r'\n\s*(?:CCS\s*Concepts|ACM\s*Reference|Index\s*Terms)\s*[:\n]',
        r'\n\s*(?:I\.?\s+(?:Introduction|INTRODUCTION))',
        r'\n\s*(?:Contents)\s*\n',
        r'\n\s*\d+\s*\n\s*(?:Introduction|INTRODUCTION)',  # page number before section
    ]

    end_pos = len(remaining)
    for pattern in end_patterns:
        m = re.search(pattern, remaining, re.IGNORECASE)
        if m and m.start() < end_pos:
            end_pos = m.start()

    raw = remaining[:end_pos].strip()

    if len(raw) < 30:
        return None

    # Clean up PDF artifacts
    # Fix hyphenated line breaks: "out-\nputs" → "outputs"
    cleaned = re.sub(r'(\w)-\n(\w)', r'\1\2', raw)
    # Fix hyphenated line breaks with trailing space
    cleaned = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', cleaned)
    # Join single newlines (PDF column wrapping)
    cleaned = re.sub(r'(?<!\n)\n(?!\n)', ' ', cleaned)
    # Normalize paragraph breaks
    cleaned = re.sub(r'\n\n+', '\n\n', cleaned)
    # Collapse multiple spaces
    cleaned = re.sub(r' {2,}', ' ', cleaned)
    # Clean up each line
    cleaned = '\n'.join(line.strip() for line in cleaned.split('\n'))
    cleaned = cleaned.strip()

    # Remove trailing footnote markers
    cleaned = re.sub(r'\s*\d+\s*$', '', cleaned)

    # Limit length
    if len(cleaned) > 3000:
        cleaned = cleaned[:3000] + '...'

    return cleaned if len(cleaned) > 50 else None


def truncate_for_yaml(text, max_len=500):
    """Create a YAML-safe single-line truncated version of text."""
    if not text:
        return ''
    single_line = re.sub(r'\s+', ' ', text).strip()
    if len(single_line) <= max_len:
        return single_line
    # Try to truncate at a sentence boundary
    for end in range(max_len, max(max_len - 100, 100), -1):
        if end < len(single_line) and single_line[end] in '.!?':
            return single_line[:end + 1]
    # Truncate at word boundary
    truncated = single_line[:max_len].rsplit(' ', 1)[0]
    return truncated + '...'


# =============================================================================
# SAFE YAML FIELD UPDATE
# =============================================================================

def update_field(frontmatter, key, value):
    """
    Safely update a single YAML field in frontmatter string.

    Uses regex replacement to update in-place, preserving all other fields
    and their order. If field doesn't exist, appends it at the end.

    CRITICAL: Does NOT use parse_frontmatter() → rebuild_frontmatter() round-trip,
    which would destroy list-based fields (tags, etc.).
    """
    # Make value YAML-safe (single-line, quotes replaced)
    if value is None:
        value = ''
    value_str = re.sub(r'\s+', ' ', str(value)).strip()
    # Replace double quotes with single quotes to avoid YAML quoting issues
    # (The vault's validate_frontmatter counts raw " chars and flags odd counts)
    value_str = value_str.replace('"', "'")
    replacement = f'{key}: "{value_str}"'

    # Try to find and replace existing field
    pattern = rf'^{re.escape(key)}:.*$'
    new_fm, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)

    if count == 0:
        # Field doesn't exist, append it
        new_fm = frontmatter.rstrip() + '\n' + replacement

    return new_fm


# =============================================================================
# PAPER DISCOVERY
# =============================================================================

def parse_date_arg(argv, default="20260207"):
    """Extract --date YYYYMMDD from argv, or return default."""
    for i, arg in enumerate(argv):
        if arg == '--date' and i + 1 < len(argv):
            return argv[i + 1]
    return default


def get_papers_needing_processing(date_added="20260207", all_papers=False):
    """Find papers needing classification processing.

    Args:
        date_added: Filter by DATE_ADDED value (default: 20260207)
        all_papers: If True, return ALL papers regardless of DATE_ADDED or field state
    """
    papers = []
    for f in sorted(PAPERS_DIR.glob('*.md')):
        try:
            if all_papers:
                papers.append(f)
            else:
                content = f.read_text(encoding='utf-8')
                if f'DATE_ADDED: {date_added}' in content:
                    # Check if classification fields are still empty
                    if re.search(r'^ethics_overall:\s*(""\s*)?$', content, re.MULTILINE):
                        papers.append(f)
        except Exception:
            pass
    return papers


# =============================================================================
# MAIN PROCESSING PIPELINE
# =============================================================================

def process_paper(paper_path, dry_run=False):
    """
    Process a single paper: extract abstract + run all classification stages.

    Returns dict with results summary.
    """
    frontmatter, body = read_paper(paper_path)

    # Guard: skip papers with manual Human View corrections
    hv_match = re.search(r'^Human View:[^\S\n]*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    if hv_match and hv_match.group(1).strip():
        return {
            'abstract_found': False,
            'ethics_overall': 'SKIP',
            'ethics_perspective': '',
            'cultural': 'SKIP',
            'religious': 'SKIP',
            'moral_psych': 'SKIP',
            'is_benchmark': 'SKIP',
        }

    # Extract title from body
    title_match = re.search(r'^# (.+)$', body, re.MULTILINE)
    title = title_match.group(1) if title_match else ''

    # --- Step 1: Extract abstract from PDF extract ---
    abstract = extract_abstract_from_pdf_extract(paper_path)
    abstract_found = abstract is not None

    if abstract:
        # Update body: replace placeholder with actual abstract
        body = body.replace('*(To be fetched)*', abstract)
        # Update YAML abstract field (truncated for YAML safety)
        yaml_abstract = truncate_for_yaml(abstract, max_len=500)
        frontmatter = update_field(frontmatter, 'abstract', yaml_abstract)

    # Build classification text (title + abstract)
    class_text = f"{title} {abstract or ''}".strip()

    # --- Step 2: Stage 1-2 - Ethics classification ---
    # ce.classify_paper(abstract, title) → dict with 4 ethics fields
    ethics_result = ce.classify_paper(abstract or '', title)
    for key, value in ethics_result.items():
        frontmatter = update_field(frontmatter, key, value)

    # --- Step 3: Stage 3 - Ethics perspective (conditional) ---
    ethics_perspective = ''
    if ethics_result.get('ethics_overall') == 'Yes' and all(
        ethics_result.get(k) == 'No'
        for k in ['virtue_ethics', 'deontological_ethics', 'utilitarian_ethics']
    ):
        ethics_perspective = cep.classify_ethics_perspective(class_text)
        frontmatter = update_field(frontmatter, 'ethics_perspective', ethics_perspective)

    # --- Step 4: Stage 4 - Research topic (for non-ethics papers) ---
    research_topic = ''
    if ethics_result.get('ethics_overall') == 'No':
        research_topic = cnt.classify_topic(class_text)
        frontmatter = update_field(frontmatter, 'research_topic', research_topic)

    # --- Step 5: Stage 5 - Cultural/Religious ---
    # Extract languages_list from YAML for cultural classification
    lang_match = re.search(r'^languages_list:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    languages_list = lang_match.group(1).strip() if lang_match else ""
    cultural = ccr.classify_cultural(title, abstract or '', languages_list)
    religious = ccr.classify_religious(title, abstract or '')
    religious_list = ccr.classify_religious_list(title, abstract or '')
    frontmatter = update_field(frontmatter, 'national_ethnic_cultural', cultural)
    frontmatter = update_field(frontmatter, 'religious_values', religious)
    frontmatter = update_field(frontmatter, 'religious_values_list', religious_list)

    # --- Step 6: Stage 6 - Moral psychology ---
    moral_psych = cmp.classify_moral_psych(title, abstract or '')
    frontmatter = update_field(frontmatter, 'moral_psychology', moral_psych)

    # --- Step 7: Stage 7 - Data nature ---
    # cdn.classify_paper(title, abstract) → dict with 5 data fields
    data_result = cdn.classify_paper(title, abstract or '')
    for key, value in data_result.items():
        frontmatter = update_field(frontmatter, key, value)

    # --- Write back ---
    if not dry_run:
        is_valid, issues = validate_frontmatter(frontmatter)
        if not is_valid:
            print(f"  WARN: {paper_path.name}: {issues}")
        write_paper(paper_path, frontmatter, body, validate=True)

    return {
        'abstract_found': abstract_found,
        'ethics_overall': ethics_result.get('ethics_overall', 'Unknown'),
        'ethics_perspective': ethics_perspective,
        'cultural': cultural,
        'religious': religious,
        'moral_psych': moral_psych,
        'is_benchmark': data_result.get('is_benchmark', 'Unknown'),
    }


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} START END [--dry-run] [--date YYYYMMDD] [--all]")
        print("  START, END: 1-indexed positions in paper list")
        print("  --date: filter by DATE_ADDED (default: 20260207)")
        print("  --all: process ALL papers regardless of DATE_ADDED or field state")
        sys.exit(1)

    date_added = parse_date_arg(sys.argv)
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    dry_run = '--dry-run' in sys.argv
    all_mode = '--all' in sys.argv

    # Get all papers needing processing
    if all_mode:
        print("Mode: ALL papers (re-classification)")
    else:
        print(f"Filtering by DATE_ADDED: {date_added}")
    all_papers = get_papers_needing_processing(date_added, all_papers=all_mode)
    total = len(all_papers)
    print(f"Total papers needing processing: {total}")

    # Select batch range (1-indexed)
    batch = all_papers[start - 1:end]
    print(f"Processing positions {start}-{end} ({len(batch)} papers)")
    if dry_run:
        print("DRY RUN: No files will be modified")
    print()

    # Process each paper
    abstracts_found = 0
    ethics_yes = 0
    errors = 0
    skipped = 0

    for i, paper_path in enumerate(batch, start):
        try:
            result = process_paper(paper_path, dry_run=dry_run)

            # Truncate filename for display
            name = paper_path.stem
            if len(name) > 80:
                name = name[:77] + '...'

            if result['ethics_overall'] == 'SKIP':
                skipped += 1
                print(f"  [{i:3d}] SKIP (Human View): {name}")
                continue

            if result['abstract_found']:
                abstracts_found += 1
            if result['ethics_overall'] == 'Yes':
                ethics_yes += 1

            abstract_flag = "ABS" if result['abstract_found'] else "---"
            ethics_flag = result['ethics_overall'][:3]
            print(f"  [{i:3d}] OK ({abstract_flag}, E={ethics_flag}): {name}")

        except Exception as e:
            errors += 1
            name = paper_path.stem[:60]
            print(f"  [{i:3d}] FAIL: {name}: {e}")

    # Summary
    processed = len(batch) - errors
    print()
    print("=" * 50)
    print(f"BATCH {start}-{end} SUMMARY")
    print(f"  Processed:       {processed}")
    print(f"  Errors:          {errors}")
    print(f"  Skipped:         {skipped}")
    print(f"  Abstracts found: {abstracts_found}/{processed}")
    print(f"  Ethics=Yes:      {ethics_yes}/{processed}")
    print("=" * 50)


if __name__ == '__main__':
    main()
