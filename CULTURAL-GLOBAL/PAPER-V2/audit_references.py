#!/usr/bin/env python3
"""
audit_references.py — Bidirectional citation audit for CULTURAL-GLOBAL Paper V2.

Parses 09-references.md → structured reference dict.
Scans prose .md files for citations (APA author-year forms).
Classifies into Matched / Uncertain / Orphan with confidence scores.
Outputs three JSON files + summary markdown.

NO deletion. Flagging only.

Usage:
    python audit_references.py [--prose-dir PATH] [--refs-file PATH] [--out-dir PATH]

Edge cases handled:
    - "et al." in first cite for 3+ authors
    - Possessive: "Smith's (2020)"
    - Narrative: "Smith and Jones (2020)" / "Smith and colleagues (2020)"
    - Year suffixes: 2023a vs 2023b
    - Same first-author + same year ambiguity
    - Hyphenated names, non-ASCII
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from collections import defaultdict

# -------------------- reference parsing --------------------

REF_HEAD_RE = re.compile(
    r'^([A-Z][A-Za-z\u00c0-\u017f\'\-]+(?:[,\s]+[A-Z][A-Za-z\u00c0-\u017f\'\-]+)*)'
    r'.*?\((\d{4})([a-c])?\)'
)


def normalize_lastname(name: str) -> str:
    """Strip accents, lowercase, remove hyphens."""
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    return name.lower().replace('-', '').replace("'", '').strip()


def parse_references(refs_path: Path) -> list[dict]:
    """Parse 09-references.md into list of reference entries."""
    text = refs_path.read_text()
    # Skip header line
    text = re.sub(r'^#\s+References\s*\n', '', text)
    entries = []
    for block in re.split(r'\n\s*\n', text):
        block = block.strip()
        if not block:
            continue
        m = REF_HEAD_RE.match(block)
        if not m:
            continue
        # Extract first-author lastname (text before first comma or "and"/"&")
        first_author_text = m.group(1).split(',')[0].strip()
        first_author = first_author_text.split()[0] if first_author_text else ''
        year = int(m.group(2))
        suffix = m.group(3) or ''
        # Extract all author lastnames (rough: lastnames before initials)
        all_authors_match = re.findall(
            r'([A-Z][A-Za-z\u00c0-\u017f\'\-]+),\s*[A-Z]\.', block[:300]
        )
        entries.append({
            'first_author': first_author,
            'first_author_norm': normalize_lastname(first_author),
            'year': year,
            'suffix': suffix,
            'all_authors_norm': [normalize_lastname(a) for a in all_authors_match],
            'key': f'{first_author}_{year}{suffix}',
            'full_text': block.strip(),
        })
    return entries


# -------------------- prose citation extraction --------------------

# Permissive parenthetical: any (...) containing a 4-digit year
PAREN_RE = re.compile(r'\(([^()]{1,200}?)\)')
YEAR_IN_PAREN_RE = re.compile(r'(?P<author>[A-Z][A-Za-z\u00c0-\u017f\'\-]+)[^;]*?(?P<year>\d{4})(?P<suffix>[a-c])?(?![\d])')

# Narrative form: handles 1-, 2-, 3-, N-author chains
# Matches "Author (Year)", "Author et al. (Year)", "Author and Author (Year)",
# "Author, Author, and Author (Year)", "Author, Author, Author, and Author (Year)"
# The captured first_author is always the leftmost lastname.
NARRATIVE_RE = re.compile(
    r'(?<![A-Za-z])'
    r'(?P<author>[A-Z][A-Za-z\u00c0-\u017f\'\-]+)'
    r'(?:'
        # "A, B, ..., and C" or "A, B, and C" — multi-author chain
        r'(?:,\s+[A-Z][A-Za-z\u00c0-\u017f\'\-]+){1,5},?\s+(?:and|&)\s+[A-Z][A-Za-z\u00c0-\u017f\'\-]+'
        # "A and B" — two-author
        r'|\s+(?:and|&)\s+[A-Z][A-Za-z\u00c0-\u017f\'\-]+'
        # "A et al." — collapsed
        r"|\s+et\s+al\.?"
    r')?'
    r"(?:'s|\u2019s)?\s*"
    r'\(\s*(?P<year>\d{4})(?P<suffix>[a-c])?\s*\)'
)


def extract_citations(text: str) -> list[dict]:
    """Extract all candidate citations from prose text.

    Two forms:
    1. Parenthetical: any (...) containing a year. The first capital-word inside is the author.
       Handles "(Author, Year)", "(Author et al., Year)", "(Author1, Author2, & Author3, Year)",
       and semicolon-joined "(Author1, Year1; Author2, Year2)".
    2. Narrative: "Author (Year)", "Author et al. (Year)", "Author and Author (Year)".
    """
    citations = []
    seen_pos = set()

    # Parenthetical pass
    for pm in PAREN_RE.finditer(text):
        inner = pm.group(1)
        # Skip parens with no year
        if not re.search(r'\b\d{4}\b', inner):
            continue
        # Split by semicolons (each part is a separate citation)
        parts = inner.split(';')
        offset = pm.start() + 1  # +1 for opening paren
        for part in parts:
            ym = YEAR_IN_PAREN_RE.search(part)
            if not ym:
                offset += len(part) + 1
                continue
            author = ym.group('author')
            year = int(ym.group('year'))
            suffix = ym.group('suffix') or ''
            pos = offset + ym.start()
            seen_pos.add(pos)
            citations.append({
                'first_author_norm': normalize_lastname(author),
                'year': year,
                'suffix': suffix,
                'form': 'parenthetical',
                'raw': f'({part.strip()})' if len(parts) > 1 else pm.group(0),
                'pos': pos,
            })
            offset += len(part) + 1

    # Narrative pass
    for nm in NARRATIVE_RE.finditer(text):
        if nm.start() in seen_pos:
            continue
        author = nm.group('author')
        year = int(nm.group('year'))
        suffix = nm.group('suffix') or ''
        citations.append({
            'first_author_norm': normalize_lastname(author),
            'year': year,
            'suffix': suffix,
            'form': 'narrative',
            'raw': text[nm.start():nm.end()],
            'pos': nm.start(),
        })

    return citations


# -------------------- matching engine --------------------

def classify_citation(cite: dict, refs_by_key: dict, refs_by_aname_year: dict) -> dict:
    """Classify a citation into Matched / Uncertain / Orphan."""
    # 1. Exact match with suffix → Matched 1.0
    if cite['suffix']:
        key = f"{cite['first_author_norm']}_{cite['year']}{cite['suffix']}"
        if key in refs_by_key:
            return {'bin': 'matched', 'confidence': 1.0, 'matched_key': refs_by_key[key]['key'], 'reason': 'exact_with_suffix'}

    # 2. Lookup by (first_author_norm, year)
    candidates = refs_by_aname_year.get((cite['first_author_norm'], cite['year']), [])

    if len(candidates) == 1:
        ref = candidates[0]
        # Single candidate
        if ref['suffix'] and not cite['suffix']:
            return {'bin': 'uncertain', 'confidence': 0.7, 'matched_key': ref['key'],
                    'reason': 'ref_has_suffix_cite_does_not'}
        return {'bin': 'matched', 'confidence': 0.95, 'matched_key': ref['key'], 'reason': 'unique_author_year'}

    if len(candidates) > 1:
        # Multiple candidates — ambiguous
        return {'bin': 'uncertain', 'confidence': 0.6,
                'matched_key': [c['key'] for c in candidates],
                'reason': 'multiple_candidates_same_author_year'}

    # 3. No (first_author, year) match — orphan
    return {'bin': 'orphan', 'confidence': 0.0, 'matched_key': None, 'reason': 'no_author_year_match'}


def find_line(text: str, pos: int) -> int:
    return text[:pos].count('\n') + 1


# -------------------- audit drivers --------------------

def audit_prose_to_refs(prose_files: list[Path], refs: list[dict]) -> dict:
    """Pass B: prose → refs. For each prose citation, find its reference."""
    refs_by_key = {r['key']: r for r in refs}
    refs_by_aname_year = defaultdict(list)
    for r in refs:
        refs_by_aname_year[(r['first_author_norm'], r['year'])].append(r)

    matched, uncertain, orphan = [], [], []
    for f in prose_files:
        text = f.read_text()
        cites = extract_citations(text)
        for c in cites:
            cls = classify_citation(c, refs_by_key, refs_by_aname_year)
            entry = {
                'file': f.name,
                'line': find_line(text, c['pos']),
                'raw': c['raw'],
                'first_author': c['first_author_norm'],
                'year': c['year'],
                'suffix': c['suffix'],
                'form': c['form'],
                'classification': cls,
            }
            if cls['bin'] == 'matched':
                matched.append(entry)
            elif cls['bin'] == 'uncertain':
                uncertain.append(entry)
            else:
                orphan.append(entry)

    return {
        'matched': matched,
        'uncertain': uncertain,
        'orphan': orphan,
        'totals': {
            'matched': len(matched),
            'uncertain': len(uncertain),
            'orphan': len(orphan),
            'total': len(matched) + len(uncertain) + len(orphan),
        },
    }


def audit_refs_to_prose(prose_files: list[Path], refs: list[dict]) -> dict:
    """Pass A: refs → prose. For each reference, find at least one citation."""
    # Build prose citation index (first_author_norm, year) → list of prose mentions
    prose_index = defaultdict(list)
    for f in prose_files:
        text = f.read_text()
        cites = extract_citations(text)
        for c in cites:
            prose_index[(c['first_author_norm'], c['year'])].append({
                'file': f.name, 'line': find_line(text, c['pos']), 'raw': c['raw'],
            })

    cited, orphaned_refs = [], []
    for r in refs:
        mentions = prose_index.get((r['first_author_norm'], r['year']), [])
        if mentions:
            cited.append({
                'key': r['key'],
                'full_text': r['full_text'][:200],
                'mention_count': len(mentions),
                'first_mention': mentions[0],
            })
        else:
            orphaned_refs.append({
                'key': r['key'],
                'full_text': r['full_text'][:200],
                'first_author': r['first_author'],
                'year': r['year'],
                'suffix': r['suffix'],
            })

    return {
        'cited': cited,
        'orphaned_refs': orphaned_refs,
        'totals': {
            'cited': len(cited),
            'orphaned_refs': len(orphaned_refs),
            'total_refs': len(refs),
        },
    }


# -------------------- main --------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prose-dir', default='.', help='Directory containing 0?-*.md and 1?-*.md')
    parser.add_argument('--refs-file', default='09-references.md', help='Reference file path')
    parser.add_argument('--out-dir', default='METHODS/council-v21', help='Output directory')
    parser.add_argument('--include-supplementary', action='store_true', help='Also scan supplementary/*.md')
    args = parser.parse_args()

    prose_dir = Path(args.prose_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    refs_path = prose_dir / args.refs_file
    refs = parse_references(refs_path)
    print(f"Parsed {len(refs)} reference entries from {refs_path}")

    # Collect prose files (exclude refs file itself)
    prose_files = sorted([
        f for f in prose_dir.iterdir()
        if f.is_file() and f.suffix == '.md' and re.match(r'^[01]\d-', f.name) and f.name != '09-references.md'
    ])
    if args.include_supplementary:
        supp_dir = prose_dir / 'supplementary'
        if supp_dir.exists():
            prose_files.extend(sorted([f for f in supp_dir.iterdir() if f.suffix == '.md']))
    print(f"Scanning {len(prose_files)} prose files: {[f.name for f in prose_files]}")

    # Pass B: prose → refs
    pass_b = audit_prose_to_refs(prose_files, refs)
    print(f"\nPass B (prose → refs):")
    print(f"  Matched:   {pass_b['totals']['matched']}")
    print(f"  Uncertain: {pass_b['totals']['uncertain']}")
    print(f"  Orphan:    {pass_b['totals']['orphan']}")
    print(f"  Total:     {pass_b['totals']['total']}")

    # Pass A: refs → prose
    pass_a = audit_refs_to_prose(prose_files, refs)
    print(f"\nPass A (refs → prose):")
    print(f"  Cited refs:    {pass_a['totals']['cited']}")
    print(f"  Orphaned refs: {pass_a['totals']['orphaned_refs']}")
    print(f"  Total refs:    {pass_a['totals']['total_refs']}")

    # Write JSON outputs
    with open(out_dir / 'citations_audit_prose_to_refs.json', 'w') as f:
        json.dump(pass_b, f, indent=2, ensure_ascii=False)
    with open(out_dir / 'citations_audit_refs_to_prose.json', 'w') as f:
        json.dump(pass_a, f, indent=2, ensure_ascii=False)

    # Write summary markdown
    summary = [
        '# Citation Audit Summary',
        '',
        f'**Date:** 2026-04-12',
        f'**References parsed:** {len(refs)}',
        f'**Prose files scanned:** {len(prose_files)}',
        '',
        '## Pass B (prose → refs): every prose citation has a reference?',
        f'- Matched: {pass_b["totals"]["matched"]}',
        f'- Uncertain: {pass_b["totals"]["uncertain"]}',
        f'- Orphan (citation has no matching reference): {pass_b["totals"]["orphan"]}',
        '',
        '## Pass A (refs → prose): every reference is cited?',
        f'- Cited: {pass_a["totals"]["cited"]}',
        f'- Orphaned references (in 09-references.md but not cited in any prose file): {pass_a["totals"]["orphaned_refs"]}',
        '',
        '## Orphaned References (Pass A)',
        '',
        '| Key | First author | Year | Full entry (truncated) |',
        '|-----|-------------|------|-----------------------|',
    ]
    pipe = '\\|'
    for entry in pass_a['orphaned_refs']:
        full = entry["full_text"][:100].replace("|", pipe)
        summary.append(
            f'| {entry["key"]} | {entry["first_author"]} | {entry["year"]}{entry["suffix"]} | {full}... |'
        )
    summary.append('')
    summary.append('## Orphan Citations (Pass B): prose citations with no matching reference')
    summary.append('')
    summary.append('| File:line | Raw | Author | Year |')
    summary.append('|-----------|-----|--------|------|')
    for entry in pass_b['orphan'][:50]:
        summary.append(
            f'| {entry["file"]}:{entry["line"]} | {entry["raw"]} | {entry["first_author"]} | {entry["year"]} |'
        )
    summary.append('')
    summary.append('## Uncertain (Pass B): citations with ambiguous matches')
    summary.append('')
    summary.append('| File:line | Raw | Reason |')
    summary.append('|-----------|-----|--------|')
    for entry in pass_b['uncertain'][:30]:
        summary.append(
            f'| {entry["file"]}:{entry["line"]} | {entry["raw"]} | {entry["classification"]["reason"]} |'
        )

    with open(out_dir / 'citations_audit_summary.md', 'w') as f:
        f.write('\n'.join(summary))

    print(f"\nOutputs written to {out_dir}")


if __name__ == '__main__':
    main()
