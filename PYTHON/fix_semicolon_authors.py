#!/usr/bin/env python3
"""
Fix Semicolon-Fragmented Author Entries (Category D, is_unknown=False)

Reads the most recent author audit report and fixes Category D entries where
authors are present but malformatted — typically semicolon-reversed names:
  "Nozza; Debora"              → "Debora Nozza"
  "Zheng, Weihua; Chanpaisit, Nattapol" → "Weihua Zheng; Nattapol Chanpaisit"

YAML Safety:
  - Uses re.subn() with re.MULTILINE — never parse→rebuild round-trip
  - Atomic writes via .tmp.{PID} + os.replace()
  - Quote validation before writing

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/fix_semicolon_authors.py --dry-run
    ../.venv/bin/python PYTHON/fix_semicolon_authors.py
"""

import argparse
import functools
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Force flush for logging
import builtins
print = functools.partial(builtins.print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))
from vault_config import PAPERS_DIR, AUTHORS_DIR, LOGS_DIR
from author_validation import safe_create_author_file, validate_author_name

# --- Date prefix ---
DATE_PREFIX = datetime.now().strftime("%Y%m%d")

# Garbage keywords that indicate non-author text
GARBAGE_KEYWORDS = {
    'affiliated', 'university', 'contributions', 'academicseminary',
    'estudios', 'superiores', 'leaderboard', 'initiative',
}

# Known name particles/prefixes that are legitimately short
# Note: "al" is intentionally excluded — "Al" alone is a fragment of Arabic surnames like "Al-Hamdan"
SHORT_LEGIT_PARTS = {'de', 'van', 'von', 'le', 'la', 'li', 'el', 'ben', 'bin'}


# =============================================================================
# PATTERN DETECTION
# =============================================================================

def is_garbage_text(raw: str) -> bool:
    """Return True if the raw author string looks like non-author garbage text."""
    if raw.startswith('[[Unknown]]'):
        return True
    words = re.findall(r'\w+', raw.lower())
    garbage_count = sum(1 for w in words if w in GARBAGE_KEYWORDS)
    return garbage_count >= 2


def classify_pattern(raw: str) -> str:
    """
    Classify the malformed author string into a fixable pattern.

    Returns:
        'garbage'     — unresolvable garbage text
        'single_only' — single-word surname, no first name (need API)
        'last_first'  — "Last; First" reversed single author (fixable)
        'apa_multi'   — "Last, First; Last2, First2" APA multi (fixable)
        'apa_multi_suspicious' — like apa_multi but has suspicious short parts
        'complex'     — mixed/ambiguous (skip)
    """
    if is_garbage_text(raw):
        return 'garbage'

    # No semicolon → single name
    if ';' not in raw:
        if ',' not in raw:
            # E.g. "Joshi" or "Schmeisser-Nieto"
            return 'single_only'
        return 'complex'

    parts = [p.strip() for p in raw.split(';')]
    parts = [p for p in parts if p]  # remove empty

    # Detect whether each part has a comma
    has_comma = [(',' in p) for p in parts]

    all_comma = all(has_comma)
    none_comma = not any(has_comma)

    if none_comma and len(parts) == 2:
        # "Last; First" single-author reversed
        last_part, first_part = parts[0].strip(), parts[1].strip()
        if len(last_part) < 2 or len(first_part) < 2:
            return 'complex'
        return 'last_first'

    if all_comma:
        # Check for suspicious very-short last names (≤2 chars = fragment indicators)
        # 3-char surnames (Ali, Gao, Tan, Ong, etc.) are common and should not be flagged
        for part in parts:
            last, _, _ = part.partition(',')
            last = last.strip()
            if len(last) <= 2 and last.lower() not in SHORT_LEGIT_PARTS:
                return 'apa_multi_suspicious'
        return 'apa_multi'

    return 'complex'


# =============================================================================
# NAME CONVERSION
# =============================================================================

def convert_last_first(raw: str) -> List[str]:
    """'Last; First' → ['First Last']"""
    parts = [p.strip() for p in raw.split(';')]
    return [f"{parts[1]} {parts[0]}"]


def convert_apa_multi(raw: str) -> List[str]:
    """'Last, First; Last2, First2' → ['First Last', 'First2 Last2']"""
    parts = [p.strip() for p in raw.split(';')]
    names = []
    for part in parts:
        if ',' in part:
            last, _, first = part.partition(',')
            name = f"{first.strip()} {last.strip()}"
            # Clean up extra whitespace
            name = re.sub(r'\s+', ' ', name).strip()
            names.append(name)
        else:
            # Part has no comma — include as-is (edge case)
            names.append(part.strip())
    return names


def names_to_authors_field(names: List[str]) -> str:
    """Convert list of 'First Last' names to 'authors' field value."""
    return '; '.join(names)


def name_to_wikilink(name: str) -> str:
    """Wrap a name in wikilink syntax: [[Name]]"""
    return f"[[{name}]]"


# =============================================================================
# YAML FIELD REPLACEMENT (SAFE — regex only, never parse/rebuild)
# =============================================================================

def safe_replace_field(frontmatter: str, key: str, new_value: str) -> Tuple[str, int]:
    """
    Replace a YAML field value using regex. Adds quotes if value contains
    special chars. Never uses parse→rebuild round-trip.
    Returns: (updated_frontmatter, replacement_count)
    """
    safe_value = new_value.replace('"', "'")
    # Always quote these fields to be safe
    replacement = f'{key}: "{safe_value}"'
    pattern = rf'^{re.escape(key)}:\s*.*$'
    result, count = re.subn(pattern, replacement, frontmatter, count=1, flags=re.MULTILINE)
    return result, count


def extract_frontmatter_parts(content: str) -> Optional[Tuple[str, str]]:
    """Split content into (frontmatter, body). Returns None if no frontmatter."""
    fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return None
    return fm_match.group(1), content[fm_match.end():]


def reassemble(frontmatter: str, body: str) -> str:
    return f"---\n{frontmatter}\n---\n{body}"


def validate_yaml_quotes(frontmatter: str) -> bool:
    """Each line should have an even number of double-quotes."""
    for line in frontmatter.split('\n'):
        if line.count('"') % 2 != 0:
            return False
    return True


def atomic_write(path: Path, content: str):
    """Write content atomically via temp file + os.replace()."""
    tmp = path.with_suffix(f".tmp.{os.getpid()}")
    tmp.write_text(content, encoding='utf-8')
    os.replace(str(tmp), str(path))


# =============================================================================
# AUTHOR PROFILE MANAGEMENT
# =============================================================================

def profile_exists(name: str) -> bool:
    """Check if an author profile exists (exact match)."""
    return (AUTHORS_DIR / f"{name}.md").exists()


def ensure_author_profile(name: str, dry_run: bool = False) -> str:
    """
    Ensure an author profile exists for the given name.
    Creates a stub if missing. Returns status string.
    """
    if profile_exists(name):
        return "exists"
    success, msg = safe_create_author_file(name, dry_run=dry_run)
    if success:
        return "created" if not dry_run else "would_create"
    return f"failed: {msg}"


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def load_audit_report() -> Dict:
    """Load the most recent author audit report."""
    candidates = sorted(LOGS_DIR.glob("*-author_audit_report.json"), reverse=True)
    if not candidates:
        print("ERROR: No audit report found. Run audit_author_entries.py first.")
        sys.exit(1)
    path = candidates[0]
    print(f"Loaded audit report: {path.name}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def process_entry(item: Dict, dry_run: bool = False) -> Dict:
    """
    Process a single Category D entry.
    Returns a result dict with fix details and status.
    """
    paper = item['paper']
    filename = item['filename']
    authors_raw = item.get('authors_raw', '')
    is_unknown = item.get('is_unknown', False)

    result = {
        'paper': paper,
        'filename': filename,
        'authors_raw': authors_raw,
        'pattern': None,
        'fixed_names': None,
        'authors_field': None,
        'first_author': None,
        'last_author': None,
        'profile_actions': [],
        'status': 'skipped',
        'reason': None,
    }

    # Skip true unknowns (no names to work with)
    if is_unknown:
        result['status'] = 'skip_unknown'
        result['reason'] = 'is_unknown=True — permanently unresolvable'
        return result

    pattern = classify_pattern(authors_raw)
    result['pattern'] = pattern

    # Determine the fixed names based on pattern
    if pattern == 'garbage':
        result['status'] = 'skip_garbage'
        result['reason'] = 'garbage/institutional text — not a real author name'
        return result

    if pattern == 'single_only':
        result['status'] = 'skip_single_only'
        result['reason'] = 'single surname only — requires API lookup'
        return result

    if pattern == 'complex':
        result['status'] = 'skip_complex'
        result['reason'] = 'mixed/ambiguous format — requires manual review'
        return result

    if pattern == 'apa_multi_suspicious':
        result['status'] = 'skip_suspicious'
        result['reason'] = 'suspicious short last-name fragment — possible truncated name, requires API/manual review'
        return result

    # Convert the name(s)
    if pattern == 'last_first':
        fixed_names = convert_last_first(authors_raw)
    elif pattern == 'apa_multi':
        fixed_names = convert_apa_multi(authors_raw)
    else:
        result['status'] = 'skip_complex'
        result['reason'] = f'unhandled pattern: {pattern}'
        return result

    if not fixed_names:
        result['status'] = 'error'
        result['reason'] = 'conversion produced empty name list'
        return result

    result['fixed_names'] = fixed_names
    result['authors_field'] = names_to_authors_field(fixed_names)
    result['first_author'] = name_to_wikilink(fixed_names[0])
    result['last_author'] = name_to_wikilink(fixed_names[-1])

    # Apply YAML changes
    paper_path = PAPERS_DIR / filename
    if not paper_path.exists():
        result['status'] = 'error'
        result['reason'] = f'paper file not found: {filename}'
        return result

    content = paper_path.read_text(encoding='utf-8')
    parts = extract_frontmatter_parts(content)
    if not parts:
        result['status'] = 'error'
        result['reason'] = 'no frontmatter found in paper'
        return result

    fm, body = parts

    # Replace authors, first_author, last_author
    fm, n1 = safe_replace_field(fm, 'authors', result['authors_field'])
    fm, n2 = safe_replace_field(fm, 'first_author', result['first_author'])
    fm, n3 = safe_replace_field(fm, 'last_author', result['last_author'])

    # Clear authors_incomplete flag — names are no longer incomplete
    if 'authors_incomplete: true' in fm:
        fm, _ = re.subn(
            r'^authors_incomplete:\s*true\s*$', 'authors_incomplete: false',
            fm, count=1, flags=re.MULTILINE | re.IGNORECASE
        )

    if n1 == 0 or n2 == 0 or n3 == 0:
        result['status'] = 'error'
        result['reason'] = (
            f'field replacement counts: authors={n1}, '
            f'first_author={n2}, last_author={n3} — some fields not found'
        )
        return result

    if not validate_yaml_quotes(fm):
        result['status'] = 'error'
        result['reason'] = 'quote validation failed after replacement'
        return result

    if not dry_run:
        new_content = reassemble(fm, body)
        atomic_write(paper_path, new_content)

    # Ensure author profiles exist
    for name in fixed_names:
        profile_status = ensure_author_profile(name, dry_run=dry_run)
        result['profile_actions'].append({'name': name, 'status': profile_status})

    result['status'] = 'fixed' if not dry_run else 'would_fix'
    return result


def main():
    parser = argparse.ArgumentParser(description='Fix semicolon-fragmented author entries')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing to files')
    args = parser.parse_args()

    dry_run = args.dry_run
    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"\n=== fix_semicolon_authors.py [{mode}] ===")

    audit = load_audit_report()
    cat_d = audit.get('categories', {}).get('D', [])
    incomplete = [item for item in cat_d if not item.get('is_unknown', False)]
    unknowns = [item for item in cat_d if item.get('is_unknown', False)]

    print(f"Category D total: {len(cat_d)} entries")
    print(f"  is_unknown=True (permanent): {len(unknowns)}")
    print(f"  is_incomplete (to process): {len(incomplete)}")

    results = []
    stats = {
        'total': len(cat_d),
        'processed': len(incomplete),
        'fixed': 0,
        'skip_unknown': len(unknowns),
        'skip_garbage': 0,
        'skip_single_only': 0,
        'skip_suspicious': 0,
        'skip_complex': 0,
        'errors': 0,
    }

    print(f"\n--- Processing {len(incomplete)} incomplete entries ---\n")

    for item in incomplete:
        res = process_entry(item, dry_run=dry_run)
        results.append(res)

        status = res['status']
        if status in ('fixed', 'would_fix'):
            stats['fixed'] += 1
            action = "WOULD FIX" if dry_run else "FIXED"
            print(f"  [{action}] {res['paper'][:60]}")
            print(f"    before: {res['authors_raw']}")
            print(f"    after:  {res['authors_field']}")
            for pa in res.get('profile_actions', []):
                if pa['status'] != 'exists':
                    print(f"    profile [{pa['status']}]: {pa['name']}")
        elif status.startswith('skip_'):
            stats[status] = stats.get(status, 0) + 1
            print(f"  [SKIP/{status[5:].upper()}] {res['paper'][:60]}")
            print(f"    reason: {res['reason']}")
        elif status == 'error':
            stats['errors'] += 1
            print(f"  [ERROR] {res['paper'][:60]}")
            print(f"    error: {res['reason']}")

    # Summary
    print(f"\n=== Summary ===")
    print(f"  Fixed:           {stats['fixed']}")
    print(f"  Skip unknown:    {stats['skip_unknown']} (permanently unresolvable)")
    print(f"  Skip garbage:    {stats['skip_garbage']}")
    print(f"  Skip single:     {stats['skip_single_only']} (need API)")
    print(f"  Skip suspicious: {stats['skip_suspicious']} (need review)")
    print(f"  Skip complex:    {stats['skip_complex']}")
    print(f"  Errors:          {stats['errors']}")

    # Write log
    log_path = LOGS_DIR / f"{DATE_PREFIX}-semicolon_author_fixes.json"
    log = {
        'metadata': {
            'date': datetime.now().isoformat(),
            'dry_run': dry_run,
            'audit_report': audit.get('metadata', {}).get('date', ''),
        },
        'summary': stats,
        'permanent_unknowns': [
            {'paper': item['paper'], 'url': item.get('url', ''), 'reason': 'web/blog/institutional — no named author'}
            for item in unknowns
        ],
        'results': results,
    }

    if not dry_run:
        tmp = log_path.with_suffix(f".tmp.{os.getpid()}.json")
        tmp.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding='utf-8')
        os.replace(str(tmp), str(log_path))
        print(f"\nLog written: {log_path.name}")
    else:
        print(f"\n[DRY RUN] Log would be written to: {log_path.name}")

    return stats['errors']


if __name__ == '__main__':
    sys.exit(main())
