#!/usr/bin/env python3
"""
Detect and clean up orphaned author profiles.

An "orphaned" author profile is one that is not referenced by any paper's
first_author, last_author, or authors fields via wikilinks — even after
normalizing name formats (e.g., "Last, First" ↔ "First Last").

Categories of orphans:
  - GARBAGE: Not a valid person name (fragments, concatenated names, paper titles)
  - FORMAT_ORPHAN: Profile exists in one name format, but papers only reference
    the other format (and the other-format profile also exists and IS referenced)
  - TRUE_ORPHAN: Profile has no paper reference in any name format

Usage:
    python detect_orphaned_authors.py              # Dry-run: report orphans
    python detect_orphaned_authors.py --execute    # Move orphans to RECYCLE-BIN

Safety: Uses mv to RECYCLE-BIN/, never rm/unlink.
"""

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Path setup
sys.path.insert(0, str(Path(__file__).parent))
from vault_config import PAPERS_DIR, AUTHORS_DIR, RECYCLE_BIN_DIR, LOGS_DIR


# =============================================================================
# Name Normalization
# =============================================================================

def normalize_name(name: str) -> str:
    """Create a canonical form of a name for fuzzy matching.

    Lowercases, strips accents/diacritics approximation, sorts word tokens.
    e.g., "Nozza, Debora" and "Debora Nozza" both → "debora nozza"
    """
    # Remove commas and extra whitespace
    cleaned = name.replace(',', ' ').strip()
    # Collapse whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned)
    # Lowercase and sort words for order-independent matching
    words = sorted(cleaned.lower().split())
    return ' '.join(words)


def flip_name(name: str) -> str:
    """Flip 'Last, First' → 'First Last' and vice versa."""
    if ',' in name:
        # "Last, First Middle" → "First Middle Last"
        parts = name.split(',', 1)
        return f"{parts[1].strip()} {parts[0].strip()}"
    else:
        # "First Middle Last" → "Last, First Middle"
        words = name.strip().split()
        if len(words) >= 2:
            return f"{words[-1]}, {' '.join(words[:-1])}"
        return name


def is_garbage_name(name: str) -> bool:
    """Detect obviously invalid author profile names."""
    # Too short (single letter/initial)
    if len(name) <= 2:
        return True

    # Single word with no comma (likely a last-name-only fragment)
    words = name.replace(',', '').split()
    if len(words) == 1 and len(name) < 15:
        return True

    # Contains '&' (concatenated references)
    if '&' in name:
        return True

    # Looks like a paper title (too many words, common title words)
    if len(words) > 6:
        title_words = {'a', 'the', 'of', 'in', 'for', 'and', 'to', 'with',
                       'an', 'on', 'is', 'by', 'from', 'based', 'using',
                       'towards', 'toward', 'evaluation', 'benchmark',
                       'detection', 'analysis', 'language', 'model', 'models',
                       'learning', 'dataset', 'study', 'survey', 'review'}
        lower_words = {w.lower() for w in words}
        if len(lower_words & title_words) >= 3:
            return True

    # Contains parentheses or brackets
    if any(c in name for c in '()[]{}'):
        return True

    # Starts with initials only (like "A." or "A.B")
    if re.match(r'^[A-Z]\.?\s*$', name):
        return True

    # Contains "affiliated" or institutional markers
    if any(kw in name.lower() for kw in ['affiliated', 'university', 'institute',
                                          'published', 'journal', 'conference']):
        return True

    return False


# =============================================================================
# Data Collection
# =============================================================================

def extract_wikilink_targets(text: str) -> set:
    """Extract all wikilink targets from a text string."""
    targets = set()
    for match in re.finditer(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', text):
        target = match.group(1).strip()
        if target:
            targets.add(target)
    return targets


def collect_referenced_authors(papers_dir: Path) -> tuple:
    """Scan all paper files and collect every author name referenced via wikilinks.

    Returns: (exact_references, normalized_references)
    """
    exact_refs = set()
    author_fields = ['first_author', 'last_author', 'authors']

    for paper_path in sorted(papers_dir.iterdir()):
        if not paper_path.name.endswith('.md'):
            continue
        try:
            content = paper_path.read_text(encoding='utf-8')
        except Exception:
            continue

        if not content.startswith('---'):
            continue
        end = content.find('\n---\n', 4)
        if end == -1:
            continue
        frontmatter = content[4:end]

        for field in author_fields:
            match = re.search(rf'^{re.escape(field)}:\s*(.+)$', frontmatter, re.MULTILINE)
            if match:
                value = match.group(1).strip().strip('"')
                targets = extract_wikilink_targets(value)
                exact_refs.update(targets)

    # Build normalized reference set (includes original + flipped forms)
    normalized_refs = set()
    for ref in exact_refs:
        normalized_refs.add(normalize_name(ref))

    return exact_refs, normalized_refs


def collect_author_profiles(authors_dir: Path) -> dict:
    """Collect all author profile filenames → paths."""
    profiles = {}
    for path in sorted(authors_dir.iterdir()):
        if path.name.endswith('.md') and path.is_file():
            name = path.stem
            profiles[name] = path
    return profiles


# =============================================================================
# Orphan Detection
# =============================================================================

def classify_orphans(profiles: dict, exact_refs: set, normalized_refs: set) -> dict:
    """Classify each profile as referenced, garbage, format_orphan, or true_orphan."""
    results = {
        'referenced': [],    # Directly wikilinked by at least one paper
        'garbage': [],       # Not a valid person name
        'format_orphan': [], # Unreferenced but normalized name matches a reference
        'true_orphan': [],   # No match even after normalization
    }

    for name, path in profiles.items():
        # Check exact match first
        if name in exact_refs:
            results['referenced'].append(name)
            continue

        # Check if it's garbage
        if is_garbage_name(name):
            results['garbage'].append(name)
            continue

        # Check normalized match
        if normalize_name(name) in normalized_refs:
            results['format_orphan'].append(name)
            continue

        # True orphan
        results['true_orphan'].append(name)

    return results


def main():
    parser = argparse.ArgumentParser(description="Detect orphaned author profiles")
    parser.add_argument('--execute', action='store_true',
                        help="Move garbage + true orphan profiles to RECYCLE-BIN (default: dry run)")
    parser.add_argument('--include-format-orphans', action='store_true',
                        help="Also move format orphans (profiles with a normalized match)")
    args = parser.parse_args()

    print(f"Scanning papers in: {PAPERS_DIR}")
    exact_refs, normalized_refs = collect_referenced_authors(PAPERS_DIR)
    print(f"  Found {len(exact_refs)} unique exact author references")
    print(f"  Found {len(normalized_refs)} unique normalized references")

    print(f"Scanning author profiles in: {AUTHORS_DIR}")
    profiles = collect_author_profiles(AUTHORS_DIR)
    print(f"  Found {len(profiles)} author profiles")

    results = classify_orphans(profiles, exact_refs, normalized_refs)

    print(f"\n{'=' * 60}")
    print(f"CLASSIFICATION RESULTS")
    print(f"{'=' * 60}")
    print(f"  Referenced (exact match):  {len(results['referenced'])}")
    print(f"  Format orphans (normalized match): {len(results['format_orphan'])}")
    print(f"  Garbage (invalid names):   {len(results['garbage'])}")
    print(f"  True orphans (no match):   {len(results['true_orphan'])}")

    # Print garbage profiles
    if results['garbage']:
        print(f"\n--- GARBAGE PROFILES ({len(results['garbage'])}) ---")
        for name in sorted(results['garbage']):
            print(f"  - {name}")

    # Print true orphans (sample)
    if results['true_orphan']:
        print(f"\n--- TRUE ORPHANS ({len(results['true_orphan'])}) ---")
        for name in sorted(results['true_orphan'])[:50]:
            print(f"  - {name}")
        if len(results['true_orphan']) > 50:
            print(f"  ... and {len(results['true_orphan']) - 50} more")

    # Print format orphans (sample)
    if results['format_orphan']:
        print(f"\n--- FORMAT ORPHANS ({len(results['format_orphan'])}) ---")
        for name in sorted(results['format_orphan'])[:20:]:
            print(f"  - {name}")
        if len(results['format_orphan']) > 20:
            print(f"  ... and {len(results['format_orphan']) - 20} more")

    # Save JSON report
    today = datetime.now().strftime('%Y%m%d')
    report_path = LOGS_DIR / f"{today}-orphaned_authors_classified.json"
    report_data = {
        "date": today,
        "total_profiles": len(profiles),
        "referenced": len(results['referenced']),
        "format_orphans": len(results['format_orphan']),
        "garbage": len(results['garbage']),
        "true_orphans": len(results['true_orphan']),
        "garbage_names": sorted(results['garbage']),
        "true_orphan_names": sorted(results['true_orphan']),
        "format_orphan_names": sorted(results['format_orphan']),
    }
    report_path.write_text(json.dumps(report_data, indent=2, ensure_ascii=False),
                           encoding='utf-8')
    print(f"\nReport saved to: {report_path}")

    if args.execute:
        # Determine which profiles to move
        to_move = list(results['garbage'])
        if args.include_format_orphans:
            to_move.extend(results['format_orphan'])

        if not to_move:
            print("\nNo profiles to move.")
            return

        dest_dir = RECYCLE_BIN_DIR / f"{today}-orphaned-authors"
        dest_dir.mkdir(parents=True, exist_ok=True)

        moved = 0
        errors = 0
        for name in sorted(to_move):
            src_path = profiles[name]
            dest_path = dest_dir / src_path.name
            try:
                shutil.move(str(src_path), str(dest_path))
                moved += 1
            except Exception as e:
                errors += 1
                print(f"  ERROR moving {src_path.name}: {e}")

        print(f"\nCleanup complete: {moved} moved, {errors} errors")
        print(f"Destination: {dest_dir}")
    else:
        total_actionable = len(results['garbage'])
        print(f"\nDry run — {total_actionable} garbage profiles ready for cleanup")
        print(f"Use --execute to move garbage profiles to RECYCLE-BIN/")
        print(f"Use --execute --include-format-orphans to also move format orphans")


if __name__ == "__main__":
    main()
