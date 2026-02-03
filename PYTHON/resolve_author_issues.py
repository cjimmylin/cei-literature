#!/usr/bin/env python3
"""
Resolve Author Issues Script
Identifies and fixes problematic author entries:
- Abbreviated names (e.g., "A. Aggarwal" -> "Aarti Aggarwal")
- Single-letter names (e.g., "C." -> delete or expand)
- Broken wikilink filenames (e.g., "Chad]] [[Coleman.md")
- Incomplete entries (e.g., "Center", "et al.")
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

from yaml_frontmatter_utils import parse_frontmatter
from vault_config import AUTHORS_DIR, PAPERS_DIR, LOGS_DIR

PATTERNS = {
    'abbreviated': re.compile(r'^[A-Z]\.\s+'),
    'single_letter': re.compile(r'^[A-Z]\.$'),
    'single_initial': re.compile(r'^[A-Z]\. [A-Z]\.$'),
    'broken_wikilink': re.compile(r'\[\[|\]\]'),
    'et_al': re.compile(r'^et al\.?$', re.IGNORECASE),
    'generic_placeholder': re.compile(r'^(Center|Institute|Group|Team|Consortium|Anonymous)$'),
}


def categorize_author_file(filename: str) -> Dict:
    name = filename.replace('.md', '')
    issues = []
    for issue_type, pattern in PATTERNS.items():
        if pattern.search(name):
            issues.append(issue_type)
    if len(name.split()) == 1 and len(name) <= 3:
        issues.append('very_short')
    return {'filename': filename, 'name': name, 'issues': issues, 'problematic': len(issues) > 0}


def scan_all_authors() -> Dict[str, List]:
    results = {'total': 0, 'problematic': [], 'by_issue': defaultdict(list), 'clean': []}
    for author_file in sorted(AUTHORS_DIR.glob('*.md')):
        results['total'] += 1
        analysis = categorize_author_file(author_file.name)
        if analysis['problematic']:
            results['problematic'].append(analysis)
            for issue in analysis['issues']:
                results['by_issue'][issue].append(analysis['name'])
        else:
            results['clean'].append(analysis['name'])
    return results


def build_name_mappings_from_papers() -> Dict[str, str]:
    print("Building name mappings from paper data...")
    all_authors = set()
    abbreviated_authors = defaultdict(set)

    for paper_file in PAPERS_DIR.glob('*.md'):
        try:
            content = paper_file.read_text(encoding='utf-8')
            fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
            if not fm_match:
                continue
            fields = parse_frontmatter(fm_match.group(1))
            authors_str = fields.get('authors', '')
            if authors_str:
                for author in [a.strip() for a in authors_str.split(';') if a.strip()]:
                    all_authors.add(author)
                    if PATTERNS['abbreviated'].search(author):
                        abbreviated_authors[author].add(paper_file.name)
        except Exception:
            continue

    mappings = {}
    for abbrev_name in abbreviated_authors.keys():
        parts = abbrev_name.split()
        if len(parts) < 2:
            continue
        initials = [p[0] for p in parts if re.match(r'^[A-Z]\.$', p)]
        last_name = ' '.join(p for p in parts if not re.match(r'^[A-Z]\.$', p))

        for full_name in all_authors:
            if full_name == abbrev_name:
                continue
            full_parts = full_name.split()
            if len(full_parts) < 2 or full_parts[-1].lower() != last_name.split()[-1].lower():
                continue
            full_initials = [p[0] for p in full_parts[:-1] if p]
            if initials == full_initials:
                mappings[abbrev_name] = full_name
                break
    print(f"  Found {len(mappings)} mappings")
    return mappings


def find_existing_full_name(abbreviated: str) -> Optional[str]:
    parts = abbreviated.split()
    if len(parts) < 2:
        return None
    initials = [p[0] for p in parts if re.match(r'^[A-Z]\.$', p)]
    last_name_parts = [p for p in parts if not re.match(r'^[A-Z]\.$', p)]
    last_name = ' '.join(last_name_parts)
    if not last_name:
        return None

    for author_file in AUTHORS_DIR.glob('*.md'):
        full_name = author_file.stem
        full_parts = full_name.split()
        if len(full_parts) < 2 or not full_name.lower().endswith(last_name.lower()):
            continue
        full_initials = [p[0] for p in full_parts[:-len(last_name_parts)] if p and p[0].isupper()]
        if initials == full_initials:
            return full_name
    return None


def clean_broken_wikilink_files(dry_run: bool = True) -> List[Dict]:
    cleaned = []
    for author_file in AUTHORS_DIR.glob('*.md'):
        if '[[' in author_file.stem or ']]' in author_file.stem:
            cleaned.append({'filename': author_file.name, 'reason': 'broken_wikilink'})
            if not dry_run:
                author_file.unlink()
    return cleaned


def clean_invalid_entries(dry_run: bool = True) -> List[Dict]:
    cleaned = []
    invalid = [(r'^et al\.?$', 'et_al'), (r'^\[\[Unknown\]\]$', 'unknown'), (r'^[A-Z]\.$', 'single_letter'),
               (r'^[A-Z]\. [A-Z]\.$', 'two_initials'), (r'^Center$', 'generic'), (r'^Institute$', 'generic'),
               (r'^Group$', 'generic'), (r'^Team$', 'generic'), (r'^Consortium$', 'generic')]
    for author_file in AUTHORS_DIR.glob('*.md'):
        for pattern, reason in invalid:
            if re.match(pattern, author_file.stem, re.IGNORECASE):
                cleaned.append({'filename': author_file.name, 'reason': reason})
                if not dry_run:
                    author_file.unlink()
                break
    return cleaned


def merge_abbreviated_to_full(mappings: Dict[str, str], dry_run: bool = True) -> List[Dict]:
    merged = []
    for abbrev, full in mappings.items():
        abbrev_file = AUTHORS_DIR / f"{abbrev}.md"
        full_file = AUTHORS_DIR / f"{full}.md"
        if not abbrev_file.exists():
            continue
        action = {'abbreviated': abbrev, 'full_name': full}
        if full_file.exists():
            if not dry_run:
                abbrev_file.unlink()
            action['details'] = 'deleted_abbreviated'
        else:
            if not dry_run:
                abbrev_file.rename(full_file)
            action['details'] = 'renamed'
        merged.append(action)
    return merged


def update_paper_references(old_name: str, new_name: str, dry_run: bool = True) -> int:
    updated = 0
    for paper_file in PAPERS_DIR.glob('*.md'):
        try:
            content = paper_file.read_text(encoding='utf-8')
            if old_name not in content:
                continue
            new_content = content.replace(f'[[{old_name}]]', f'[[{new_name}]]').replace(old_name, new_name)
            if new_content != content:
                if not dry_run:
                    paper_file.write_text(new_content, encoding='utf-8')
                updated += 1
        except Exception:
            continue
    return updated


def main(dry_run: bool = True):
    print("=" * 60)
    print("RESOLVE AUTHOR ISSUES")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print("=" * 60)

    scan_results = scan_all_authors()
    print(f"\nTotal authors: {scan_results['total']}, Problematic: {len(scan_results['problematic'])}")

    paper_mappings = build_name_mappings_from_papers()
    additional = {item['name']: find_existing_full_name(item['name'])
                  for item in scan_results['problematic'] if 'abbreviated' in item['issues']}
    additional = {k: v for k, v in additional.items() if v and v != k}
    all_mappings = {**paper_mappings, **additional}

    broken = clean_broken_wikilink_files(dry_run)
    invalid = clean_invalid_entries(dry_run)
    merged = merge_abbreviated_to_full(all_mappings, dry_run)

    print(f"\nBroken wikilinks: {len(broken)}, Invalid entries: {len(invalid)}, Merged: {len(merged)}")

    if not dry_run:
        for abbrev, full in all_mappings.items():
            update_paper_references(abbrev, full, dry_run=False)

    LOGS_DIR.mkdir(exist_ok=True)
    with open(LOGS_DIR / "author_issues_resolution.json", 'w') as f:
        json.dump({'scan': scan_results['by_issue'], 'mappings': all_mappings,
                   'cleaned': broken + invalid, 'merged': merged, 'dry_run': dry_run}, f, indent=2, default=list)

    if dry_run:
        print("\nDRY RUN - no changes made. Use --execute to apply.")


if __name__ == "__main__":
    import sys
    main(dry_run="--execute" not in sys.argv)
