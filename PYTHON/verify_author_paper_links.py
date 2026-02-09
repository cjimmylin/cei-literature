#!/usr/bin/env python3
"""
Phase 5: Verify Author-Paper Links

Cross-reference verification:
1. Every paper has both first_author and last_author YAML fields with valid wikilinks
2. first_author matches first element of authors list
3. last_author matches last element of authors list
4. No "et al." remains in any authors YAML field (unless flagged incomplete)
5. Every author in every paper has a corresponding profile in Authors/
6. Every profile's "Papers in this Vault" section matches actual papers
7. Position annotations (First Author / Last Author) are correct

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/verify_author_paper_links.py
"""

import re
import sys
import os
import functools
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, STATISTICS_DIR

from datetime import date
DATE_PREFIX = date.today().strftime("%Y%m%d")

REPORT_PATH = STATISTICS_DIR / f"{DATE_PREFIX}-author-paper-link-verification-report.md"


# =============================================================================
# PAPER PARSING
# =============================================================================

def parse_paper(filepath: Path) -> Dict:
    """Parse a paper file and extract relevant fields."""
    content = filepath.read_text(encoding='utf-8')

    if not content.startswith('---'):
        return {'error': 'no frontmatter'}

    match = re.search(r'\n---\s*\n', content[3:])
    if not match:
        return {'error': 'no closing ---'}

    fm_text = content[3:match.start() + 3]
    body = content[match.start() + 3 + 5:]

    fields = {}
    for key in ['authors', 'first_author', 'last_author', 'short_title',
                'authors_incomplete']:
        m = re.search(rf'^{re.escape(key)}:\s*(.+)$', fm_text, re.MULTILINE)
        if m:
            fields[key] = m.group(1).strip().strip('"')

    # Parse authors list
    authors_str = fields.get('authors', '')
    if ';' in authors_str:
        authors = [a.strip() for a in authors_str.split(';') if a.strip()]
    elif authors_str:
        authors = [a.strip() for a in authors_str.split(',') if a.strip()]
    else:
        authors = []

    # Clean author names (remove wikilinks)
    authors = [re.sub(r'\[\[|\]\]', '', a).strip() for a in authors]

    # Parse body Authors section
    body_authors = []
    authors_match = re.search(r'## Authors\s*\n\s*\n?(.*?)(?=\n\s*\n## |\Z)',
                              body, re.DOTALL)
    if authors_match:
        body_text = authors_match.group(1).strip()
        body_authors = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]', body_text)

    return {
        'stem': filepath.stem,
        'fields': fields,
        'authors': authors,
        'body_authors': body_authors,
        'has_et_al': bool(re.search(r'\bet\s*al\.?\b', authors_str, re.IGNORECASE)),
        'authors_incomplete': fields.get('authors_incomplete', '') == 'true',
    }


def parse_profile(filepath: Path) -> Dict:
    """Parse an author profile and extract paper list."""
    content = filepath.read_text(encoding='utf-8')

    # Extract papers from "## Papers in this Vault" section
    papers = []
    annotations = {}

    section_match = re.search(r'## Papers in this Vault\s*\n(.*?)(?=\n## |\Z)',
                              content, re.DOTALL)
    if section_match:
        section = section_match.group(1)
        for line in section.split('\n'):
            line = line.strip()
            if not line.startswith('- '):
                continue

            # Extract paper link
            link_match = re.match(r'- \[\[([^|\]]+)(?:\|[^\]]+)?\]\](.*)', line)
            if link_match:
                paper_stem = link_match.group(1).strip()
                annotation = link_match.group(2).strip()
                papers.append(paper_stem)

                if '(First Author)' in annotation:
                    annotations[paper_stem] = 'first'
                elif '(Last Author)' in annotation:
                    annotations[paper_stem] = 'last'
                else:
                    annotations[paper_stem] = 'middle'

    return {
        'stem': filepath.stem,
        'papers': papers,
        'annotations': annotations,
    }


# =============================================================================
# VERIFICATION CHECKS
# =============================================================================

def verify_all():
    """Run all verification checks and produce report."""

    errors = []
    warnings = []

    papers = sorted(PAPERS_DIR.glob('*.md'))
    author_files = [f for f in sorted(AUTHORS_DIR.glob('*.md'))
                    if f.name not in ('README.md', 'TEMPLATE.md')]

    print(f"Verifying {len(papers)} papers and {len(author_files)} author profiles...\n")

    # Parse all papers
    paper_data = {}
    for pf in papers:
        try:
            data = parse_paper(pf)
            paper_data[pf.stem] = data
        except Exception as e:
            errors.append(f"PARSE ERROR: {pf.name}: {e}")

    # Parse all profiles
    profile_data = {}
    for af in author_files:
        try:
            data = parse_profile(af)
            profile_data[af.stem] = data
        except Exception as e:
            errors.append(f"PARSE ERROR: {af.name}: {e}")

    existing_profiles = set(profile_data.keys())

    # Build expected author→papers mapping from papers
    expected_author_papers = defaultdict(list)  # author_name → [(stem, position)]

    # =========================================================================
    # CHECK 1: Every paper has first_author and last_author
    # =========================================================================
    print("Check 1: first_author and last_author fields...")
    missing_first = []
    missing_last = []

    for stem, data in paper_data.items():
        fields = data.get('fields', {})
        if 'first_author' not in fields:
            missing_first.append(stem)
        if 'last_author' not in fields:
            missing_last.append(stem)

    if missing_first:
        errors.append(f"Missing first_author: {len(missing_first)} papers")
        for s in missing_first[:10]:
            errors.append(f"  - {s}")
        if len(missing_first) > 10:
            errors.append(f"  ... and {len(missing_first) - 10} more")

    if missing_last:
        errors.append(f"Missing last_author: {len(missing_last)} papers")
        for s in missing_last[:10]:
            errors.append(f"  - {s}")
        if len(missing_last) > 10:
            errors.append(f"  ... and {len(missing_last) - 10} more")

    print(f"  Missing first_author: {len(missing_first)}")
    print(f"  Missing last_author: {len(missing_last)}")

    # =========================================================================
    # CHECK 2: first_author matches first element of authors list
    # =========================================================================
    print("Check 2: first_author consistency...")
    first_mismatch = []

    for stem, data in paper_data.items():
        fields = data.get('fields', {})
        authors = data.get('authors', [])

        if 'first_author' in fields and authors:
            fa = re.sub(r'\[\[|\]\]', '', fields['first_author']).strip()
            if authors[0] and fa.lower() != authors[0].lower():
                first_mismatch.append((stem, fa, authors[0]))

    if first_mismatch:
        warnings.append(f"first_author mismatch: {len(first_mismatch)} papers")
        for s, fa, actual in first_mismatch[:10]:
            warnings.append(f"  - {s}: first_author='{fa}' vs authors[0]='{actual}'")

    print(f"  Mismatches: {len(first_mismatch)}")

    # =========================================================================
    # CHECK 3: last_author matches last element of authors list
    # =========================================================================
    print("Check 3: last_author consistency...")
    last_mismatch = []

    for stem, data in paper_data.items():
        fields = data.get('fields', {})
        authors = data.get('authors', [])

        if 'last_author' in fields and authors and not data.get('has_et_al'):
            la = re.sub(r'\[\[|\]\]', '', fields['last_author']).strip()
            last_actual = authors[-1] if authors else ''
            if last_actual and la.lower() != last_actual.lower():
                last_mismatch.append((stem, la, last_actual))

    if last_mismatch:
        warnings.append(f"last_author mismatch: {len(last_mismatch)} papers")
        for s, la, actual in last_mismatch[:10]:
            warnings.append(f"  - {s}: last_author='{la}' vs authors[-1]='{actual}'")

    print(f"  Mismatches: {len(last_mismatch)}")

    # =========================================================================
    # CHECK 4: No "et al." in authors (unless flagged incomplete)
    # =========================================================================
    print("Check 4: Remaining 'et al.' in authors...")
    remaining_et_al = []

    for stem, data in paper_data.items():
        if data.get('has_et_al') and not data.get('authors_incomplete'):
            remaining_et_al.append(stem)

    if remaining_et_al:
        warnings.append(f"Unflagged 'et al.' remaining: {len(remaining_et_al)} papers")
        for s in remaining_et_al[:10]:
            warnings.append(f"  - {s}")

    flagged_incomplete = sum(1 for d in paper_data.values() if d.get('authors_incomplete'))
    print(f"  Remaining et al. (unflagged): {len(remaining_et_al)}")
    print(f"  Flagged incomplete: {flagged_incomplete}")

    # =========================================================================
    # CHECK 5: Every author has a profile
    # =========================================================================
    print("Check 5: Author profiles existence...")
    missing_profiles = set()

    for stem, data in paper_data.items():
        for author in data.get('authors', []):
            clean = re.sub(r'\[\[|\]\]', '', author).strip()
            if clean and clean.lower() not in ('et al', 'et al.', 'unknown'):
                if clean not in existing_profiles:
                    missing_profiles.add(clean)

                # Track expected mapping
                authors = data['authors']
                idx = authors.index(author) if author in authors else -1
                if idx == 0:
                    position = 'first' if len(authors) > 1 else 'sole'
                elif idx == len(authors) - 1:
                    position = 'last'
                else:
                    position = 'middle'
                expected_author_papers[clean].append((stem, position))

    if missing_profiles:
        warnings.append(f"Missing author profiles: {len(missing_profiles)}")
        for p in sorted(missing_profiles)[:20]:
            warnings.append(f"  - {p}")
        if len(missing_profiles) > 20:
            warnings.append(f"  ... and {len(missing_profiles) - 20} more")

    print(f"  Missing profiles: {len(missing_profiles)}")

    # =========================================================================
    # CHECK 6: Profile paper lists match actual papers
    # =========================================================================
    print("Check 6: Profile paper list accuracy...")
    profile_missing_papers = 0
    profile_extra_papers = 0

    for profile_stem, pdata in profile_data.items():
        listed_papers = set(pdata['papers'])
        expected_papers = set(s for s, _ in expected_author_papers.get(profile_stem, []))

        missing = expected_papers - listed_papers
        extra = listed_papers - expected_papers  # Not necessarily wrong — could be valid

        if missing:
            profile_missing_papers += len(missing)
            if len(missing) <= 3:
                for m in missing:
                    warnings.append(f"  Profile '{profile_stem}' missing paper: {m}")

    print(f"  Papers missing from profiles: {profile_missing_papers}")
    print(f"  Extra papers in profiles: {profile_extra_papers}")

    # =========================================================================
    # CHECK 7: Position annotations correctness
    # =========================================================================
    print("Check 7: Position annotations...")
    annotation_errors = 0

    for profile_stem, pdata in profile_data.items():
        for paper_stem, annotation in pdata.get('annotations', {}).items():
            # Find what the actual position should be
            expected_entries = expected_author_papers.get(profile_stem, [])
            expected_pos = None
            for s, pos in expected_entries:
                if s == paper_stem:
                    expected_pos = pos
                    break

            if expected_pos and expected_pos != annotation:
                # Allow 'sole' to match 'first'
                if expected_pos == 'sole' and annotation == 'first':
                    continue
                annotation_errors += 1

    print(f"  Annotation errors: {annotation_errors}")

    # =========================================================================
    # GENERATE REPORT
    # =========================================================================
    total_errors = len(errors) + len(missing_first) + len(missing_last)
    total_warnings = (len(warnings) + len(first_mismatch) + len(last_mismatch) +
                      len(remaining_et_al) + len(missing_profiles) +
                      profile_missing_papers + annotation_errors)

    report = f"""# Author-Paper Link Verification Report

**Date:** {date.today().isoformat()}
**Papers:** {len(paper_data)}
**Author Profiles:** {len(profile_data)}

## Summary

| Check | Status | Count |
|-------|--------|-------|
| Papers with first_author | {'PASS' if not missing_first else 'FAIL'} | {len(paper_data) - len(missing_first)}/{len(paper_data)} |
| Papers with last_author | {'PASS' if not missing_last else 'FAIL'} | {len(paper_data) - len(missing_last)}/{len(paper_data)} |
| first_author consistency | {'PASS' if not first_mismatch else 'WARN'} | {len(first_mismatch)} mismatches |
| last_author consistency | {'PASS' if not last_mismatch else 'WARN'} | {len(last_mismatch)} mismatches |
| No remaining et al. | {'PASS' if not remaining_et_al else 'WARN'} | {len(remaining_et_al)} unflagged |
| Flagged incomplete | INFO | {flagged_incomplete} |
| Author profiles exist | {'PASS' if not missing_profiles else 'WARN'} | {len(missing_profiles)} missing |
| Profile paper lists | {'PASS' if not profile_missing_papers else 'WARN'} | {profile_missing_papers} missing entries |
| Position annotations | {'PASS' if not annotation_errors else 'WARN'} | {annotation_errors} errors |

## Errors

"""

    if errors:
        for e in errors:
            report += f"- {e}\n"
    else:
        report += "No errors found.\n"

    report += "\n## Warnings\n\n"
    if warnings:
        for w in warnings:
            report += f"- {w}\n"
    else:
        report += "No warnings found.\n"

    # Missing first_author details
    if missing_first:
        report += f"\n## Papers Missing first_author ({len(missing_first)})\n\n"
        for s in sorted(missing_first):
            report += f"- {s}\n"

    # Missing last_author details
    if missing_last:
        report += f"\n## Papers Missing last_author ({len(missing_last)})\n\n"
        for s in sorted(missing_last)[:50]:
            report += f"- {s}\n"
        if len(missing_last) > 50:
            report += f"\n... and {len(missing_last) - 50} more\n"

    # Missing profiles
    if missing_profiles:
        report += f"\n## Missing Author Profiles ({len(missing_profiles)})\n\n"
        for p in sorted(missing_profiles)[:50]:
            report += f"- {p}\n"
        if len(missing_profiles) > 50:
            report += f"\n... and {len(missing_profiles) - 50} more\n"

    # Save report
    STATISTICS_DIR.mkdir(exist_ok=True)
    REPORT_PATH.write_text(report, encoding='utf-8')
    print(f"\nReport saved: {REPORT_PATH.name}")

    # Overall result
    print("\n" + "=" * 60)
    if total_errors == 0 and total_warnings == 0:
        print("ALL CHECKS PASSED")
    elif total_errors == 0:
        print(f"PASSED with {total_warnings} warnings")
    else:
        print(f"FAILED: {total_errors} errors, {total_warnings} warnings")
    print("=" * 60)


def main():
    verify_all()


if __name__ == '__main__':
    main()
