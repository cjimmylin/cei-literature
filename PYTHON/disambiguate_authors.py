#!/usr/bin/env python3
"""
Phase 2: Disambiguate Authors Against Existing Profiles

Loads the author-paper map from Phase 1 and matches each unique author name
to an existing author profile using a 6-tier matching algorithm.

USAGE:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/disambiguate_authors.py
    ../.venv/bin/python PYTHON/disambiguate_authors.py --dry-run
"""

import re
import json
import sys
import os
import functools
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from collections import defaultdict

# Force flush
import builtins
print = functools.partial(builtins.print, flush=True)

sys.path.insert(0, str(Path(__file__).parent))
from vault_config import AUTHORS_DIR, LOGS_DIR, PAPERS_DIR

from datetime import date
DATE_PREFIX = date.today().strftime("%Y%m%d")

# Input
MAP_FILE = sorted(LOGS_DIR.glob("*-author_paper_map.json"), reverse=True)

# Output
DISAMBIGUATION_OUTPUT = LOGS_DIR / f"{DATE_PREFIX}-author_disambiguation.json"
REVIEW_QUEUE_OUTPUT = LOGS_DIR / f"{DATE_PREFIX}-disambiguation_review_queue.json"


# =============================================================================
# AUTHOR PROFILE INDEX
# =============================================================================

def build_profile_index() -> Dict:
    """
    Build a comprehensive index of all existing author profiles.

    Returns dict with:
    - 'by_stem': {stem: profile_info} — primary lookup by filename stem
    - 'by_normalized': {normalized_name: [stems]} — fuzzy lookup
    - 'by_surname': {surname: [stems]} — surname-based grouping
    - 'redirects': {alias: canonical_stem} — redirect/alias mappings
    """
    index = {
        'by_stem': {},
        'by_normalized': defaultdict(list),
        'by_surname': defaultdict(list),
        'redirects': {},
    }

    author_files = [f for f in AUTHORS_DIR.glob('*.md')
                    if f.name not in ('README.md', 'TEMPLATE.md')]

    for af in author_files:
        stem = af.stem
        content = af.read_text(encoding='utf-8')

        # Extract basic info
        info = {
            'stem': stem,
            'path': str(af),
            'aliases': [],
            'affiliation': '',
        }

        # Parse YAML for aliases/affiliation
        name_match = re.search(r'^name:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        if name_match:
            yaml_name = name_match.group(1).strip()
            if yaml_name != stem:
                info['aliases'].append(yaml_name)

        affil_match = re.search(r'^affiliation:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        if affil_match:
            info['affiliation'] = affil_match.group(1).strip()

        # Check for redirect pattern
        redirect_match = re.search(r'(?:redirect|see|also known as|alias)[:\s]+\[\[([^\]]+)\]\]',
                                   content, re.IGNORECASE)
        if redirect_match:
            target = redirect_match.group(1).strip()
            index['redirects'][stem] = target

        # Extract co-authors from "Papers in this Vault" section
        papers_section = re.search(r'## Papers in this Vault\s*\n(.*?)(?=\n## |\Z)',
                                   content, re.DOTALL)
        if papers_section:
            paper_links = re.findall(r'\[\[([^|]+?)(?:\|[^\]]+)?\]\]', papers_section.group(1))
            info['paper_links'] = paper_links

        index['by_stem'][stem] = info

        # Index by normalized name
        norm = normalize_name(stem)
        index['by_normalized'][norm].append(stem)

        # Index aliases
        for alias in info['aliases']:
            norm_alias = normalize_name(alias)
            index['by_normalized'][norm_alias].append(stem)

        # Index by surname(s)
        surnames = extract_surnames(stem)
        for surname in surnames:
            index['by_surname'][surname.lower()].append(stem)

    # Process redirects: also index redirect sources
    for alias_stem, target_stem in index['redirects'].items():
        if target_stem in index['by_stem']:
            norm_alias = normalize_name(alias_stem)
            if target_stem not in index['by_normalized'].get(norm_alias, []):
                index['by_normalized'][norm_alias].append(target_stem)

    print(f"  Profile index: {len(index['by_stem'])} profiles, "
          f"{len(index['redirects'])} redirects, "
          f"{sum(len(v) for v in index['by_surname'].values())} surname entries")

    return index


def normalize_name(name: str) -> str:
    """
    Normalize a name for fuzzy matching:
    - Lowercase
    - Remove accents/diacritics
    - Remove punctuation
    - Handle "LastName, FirstName" ↔ "FirstName LastName" reversal
    - Collapse whitespace
    """
    if not name:
        return ""

    # Remove wikilink syntax
    name = re.sub(r'\[\[|\]\]', '', name)

    # Lowercase
    name = name.lower().strip()

    # Remove accents
    name = ''.join(
        c for c in unicodedata.normalize('NFD', name)
        if unicodedata.category(c) != 'Mn'
    )

    # Remove punctuation except spaces
    name = re.sub(r'[^\w\s]', '', name)

    # Collapse whitespace
    name = re.sub(r'\s+', ' ', name).strip()

    # Sort words alphabetically for order-independent matching
    parts = sorted(name.split())
    return ' '.join(parts)


def extract_surnames(full_name: str) -> List[str]:
    """Extract likely surname(s) from a full name."""
    parts = full_name.strip().split()
    if not parts:
        return []

    # Common patterns:
    # "FirstName LastName" → LastName
    # "FirstName MiddleName LastName" → LastName
    # "FirstName van der LastName" → LastName (or "van der LastName")

    # Particles that are part of surname
    particles = {'van', 'von', 'de', 'del', 'della', 'di', 'el', 'al', 'bin',
                 'ibn', 'le', 'la', 'des', 'du', 'den', 'der', 'ter'}

    surnames = []

    # Last word is almost always part of surname
    surnames.append(parts[-1])

    # Check for particles before last name
    if len(parts) >= 3:
        for i in range(len(parts) - 2, 0, -1):
            if parts[i].lower() in particles:
                compound = ' '.join(parts[i:])
                surnames.append(compound)
                break

    return surnames


# =============================================================================
# 6-TIER MATCHING ALGORITHM
# =============================================================================

def match_author_to_profile(author_name: str, profile_index: Dict,
                            co_authors: List[str] = None) -> Dict:
    """
    Match an author name to an existing profile using 6-tier algorithm.

    Returns:
    {
        'canonical_profile': str or None,
        'match_tier': int (1-6),
        'confidence': float,
        'method': str,
        'alternatives': list  # For ambiguous matches
    }
    """
    clean_name = re.sub(r'\[\[|\]\]', '', author_name).strip()

    # === Tier 1: Exact filename match ===
    if clean_name in profile_index['by_stem']:
        return {
            'canonical_profile': clean_name,
            'match_tier': 1,
            'confidence': 1.0,
            'method': 'exact_filename',
            'alternatives': [],
        }

    # === Tier 2: Redirect/alias match ===
    # Check if this name is a known redirect
    if clean_name in profile_index['redirects']:
        target = profile_index['redirects'][clean_name]
        return {
            'canonical_profile': target,
            'match_tier': 2,
            'confidence': 1.0,
            'method': 'redirect',
            'alternatives': [],
        }

    # Check YAML name field aliases
    for stem, info in profile_index['by_stem'].items():
        if clean_name in info.get('aliases', []):
            return {
                'canonical_profile': stem,
                'match_tier': 2,
                'confidence': 1.0,
                'method': 'yaml_alias',
                'alternatives': [],
            }

    # === Tier 3: Normalized match (case/accent/comma-reversal) ===
    norm_name = normalize_name(clean_name)
    if norm_name in profile_index['by_normalized']:
        matches = profile_index['by_normalized'][norm_name]
        if len(matches) == 1:
            return {
                'canonical_profile': matches[0],
                'match_tier': 3,
                'confidence': 0.95,
                'method': 'normalized_match',
                'alternatives': [],
            }
        elif len(matches) > 1:
            # Multiple profiles match — ambiguous, skip to tier 5
            pass

    # === Tier 4: Initial expansion ===
    # "A. Smith" → "Alice Smith" or "Arun Smith"
    initial_match = match_by_initials(clean_name, profile_index)
    if initial_match:
        if len(initial_match) == 1:
            return {
                'canonical_profile': initial_match[0],
                'match_tier': 4,
                'confidence': 0.85,
                'method': 'initial_expansion',
                'alternatives': [],
            }
        # Multiple matches → fall through to tier 5

    # === Tier 5: Contextual (co-author network) ===
    # Use co-authors to disambiguate among multiple candidates
    candidates = set()

    # Collect all possible candidates from tiers 3-4
    if norm_name in profile_index['by_normalized']:
        candidates.update(profile_index['by_normalized'][norm_name])
    if initial_match:
        candidates.update(initial_match)

    # Also try surname matching
    surnames = extract_surnames(clean_name)
    for surname in surnames:
        surname_candidates = profile_index['by_surname'].get(surname.lower(), [])
        # Only add if initial also matches
        for cand in surname_candidates:
            if initials_compatible(clean_name, cand):
                candidates.add(cand)

    if candidates and co_authors:
        # Score candidates by co-author overlap
        scored = score_by_coauthors(candidates, co_authors, profile_index)
        if scored:
            best_stem, best_score = scored[0]
            if best_score > 0 and (len(scored) == 1 or scored[0][1] > scored[1][1]):
                return {
                    'canonical_profile': best_stem,
                    'match_tier': 5,
                    'confidence': 0.70,
                    'method': 'coauthor_context',
                    'alternatives': [s for s, _ in scored[1:3]],
                }

    # If we have exactly one candidate from surname+initial matching, use it
    if len(candidates) == 1:
        return {
            'canonical_profile': list(candidates)[0],
            'match_tier': 4,
            'confidence': 0.85,
            'method': 'surname_initial_unique',
            'alternatives': [],
        }

    # === Tier 6: No match (new author) ===
    return {
        'canonical_profile': None,
        'match_tier': 6,
        'confidence': 0.0,
        'method': 'no_match',
        'alternatives': list(candidates)[:5],
    }


def match_by_initials(name: str, profile_index: Dict) -> List[str]:
    """
    Match abbreviated names like "A. Smith" to full names like "Alice Smith".

    Returns list of matching profile stems.
    """
    parts = name.split()
    if len(parts) < 2:
        return []

    # Identify initial parts and name parts
    initials = []
    name_parts = []
    for part in parts:
        if re.match(r'^[A-Z]\.$', part) or (len(part) == 1 and part.isupper()):
            initials.append(part[0].upper())
        else:
            name_parts.append(part)

    if not initials or not name_parts:
        return []

    surname = name_parts[-1].lower()
    candidates = profile_index['by_surname'].get(surname, [])

    matches = []
    for cand_stem in candidates:
        cand_parts = cand_stem.split()
        if len(cand_parts) < 2:
            continue

        # Extract first letters of non-surname parts
        cand_initials = []
        for cp in cand_parts:
            if cp.lower() != surname:
                cand_initials.append(cp[0].upper())

        # Check if our initials match the beginning of candidate initials
        if len(initials) <= len(cand_initials):
            if all(initials[j] == cand_initials[j] for j in range(len(initials))):
                matches.append(cand_stem)

    return matches


def initials_compatible(name_a: str, name_b: str) -> bool:
    """Check if two names could be the same person (compatible initials)."""
    parts_a = name_a.split()
    parts_b = name_b.split()

    if not parts_a or not parts_b:
        return False

    # Check surname match
    surname_a = parts_a[-1].lower()
    surname_b = parts_b[-1].lower()

    if surname_a != surname_b:
        return False

    # Check first initial compatibility
    first_a = parts_a[0][0].upper() if parts_a[0] else ''
    first_b = parts_b[0][0].upper() if parts_b[0] else ''

    return first_a == first_b


def score_by_coauthors(candidates: Set[str], co_authors: List[str],
                       profile_index: Dict) -> List[Tuple[str, int]]:
    """
    Score candidate profiles by co-author network overlap.

    Returns sorted list of (stem, score) pairs, highest first.
    """
    scores = []

    co_author_norms = set(normalize_name(ca) for ca in co_authors)

    for cand_stem in candidates:
        info = profile_index['by_stem'].get(cand_stem, {})
        paper_links = info.get('paper_links', [])

        # For each paper linked in the candidate's profile,
        # check if any co-authors from our paper also appear
        score = 0
        for link in paper_links:
            link_norm = normalize_name(link)
            if link_norm in co_author_norms:
                score += 1

        scores.append((cand_stem, score))

    scores.sort(key=lambda x: -x[1])
    return scores


# =============================================================================
# MAIN PIPELINE
# =============================================================================

def disambiguate_all():
    """Main disambiguation pipeline."""

    # Load author-paper map
    if not MAP_FILE:
        print("ERROR: No author_paper_map.json found in logs/")
        print("Run build_author_paper_map.py first (Phase 1)")
        sys.exit(1)

    map_path = MAP_FILE[0]
    print(f"Loading author-paper map: {map_path.name}")
    with open(map_path, 'r', encoding='utf-8') as f:
        author_paper_map = json.load(f)
    print(f"  {len(author_paper_map)} papers loaded")

    # Build profile index
    print("\nBuilding author profile index...")
    profile_index = build_profile_index()

    # Collect unique authors across all papers
    print("\nCollecting unique author names...")
    author_to_papers = defaultdict(list)

    for stem, entry in author_paper_map.items():
        authors = entry.get('authors', [])
        for i, author in enumerate(authors):
            position = 'first' if i == 0 else ('last' if i == len(authors) - 1 else 'middle')
            if len(authors) == 1:
                position = 'sole'
            author_to_papers[author].append({
                'stem': stem,
                'position': position,
                'co_authors': [a for a in authors if a != author],
            })

    print(f"  {len(author_to_papers)} unique author names across {len(author_paper_map)} papers")

    # Disambiguate each author
    print("\n=== Disambiguating authors ===")
    disambiguation = {}
    review_queue = []

    stats = defaultdict(int)

    for author_name, paper_entries in sorted(author_to_papers.items()):
        # Collect all co-authors for this author across all their papers
        all_co_authors = []
        for pe in paper_entries:
            all_co_authors.extend(pe['co_authors'])

        result = match_author_to_profile(author_name, profile_index, all_co_authors)

        tier = result['match_tier']
        stats[f'tier_{tier}'] += 1

        papers_info = [{'stem': pe['stem'], 'position': pe['position']} for pe in paper_entries]

        disambiguation[author_name] = {
            'canonical_profile': result['canonical_profile'],
            'match_tier': tier,
            'confidence': result['confidence'],
            'method': result['method'],
            'papers': papers_info,
        }

        # Add ambiguous/unmatched to review queue
        if tier >= 5:
            review_queue.append({
                'author_name': author_name,
                'match_tier': tier,
                'method': result['method'],
                'canonical_profile': result['canonical_profile'],
                'alternatives': result.get('alternatives', []),
                'papers': [pe['stem'] for pe in paper_entries],
                'co_authors_sample': all_co_authors[:5],
            })

    # Save outputs
    print("\n=== Saving outputs ===")

    tmp = DISAMBIGUATION_OUTPUT.parent / f".tmp.{os.getpid()}.disamb.json"
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(disambiguation, f, indent=2, ensure_ascii=False)
    os.replace(tmp, DISAMBIGUATION_OUTPUT)
    print(f"  Disambiguation map: {DISAMBIGUATION_OUTPUT.name} ({len(disambiguation)} authors)")

    if review_queue:
        tmp_rq = REVIEW_QUEUE_OUTPUT.parent / f".tmp.{os.getpid()}.rq.json"
        with open(tmp_rq, 'w', encoding='utf-8') as f:
            json.dump(review_queue, f, indent=2, ensure_ascii=False)
        os.replace(tmp_rq, REVIEW_QUEUE_OUTPUT)
        print(f"  Review queue: {REVIEW_QUEUE_OUTPUT.name} ({len(review_queue)} items)")

    # Summary
    print("\n" + "=" * 60)
    print("DISAMBIGUATION SUMMARY")
    print("=" * 60)
    print(f"Total unique authors: {len(disambiguation)}")
    print(f"  Tier 1 (exact match):     {stats.get('tier_1', 0)}")
    print(f"  Tier 2 (redirect/alias):  {stats.get('tier_2', 0)}")
    print(f"  Tier 3 (normalized):      {stats.get('tier_3', 0)}")
    print(f"  Tier 4 (initial expand):  {stats.get('tier_4', 0)}")
    print(f"  Tier 5 (coauthor ctx):    {stats.get('tier_5', 0)}")
    print(f"  Tier 6 (no match/new):    {stats.get('tier_6', 0)}")
    matched = sum(v for k, v in stats.items() if k != 'tier_6')
    print(f"  Matched total:            {matched} ({100*matched/max(len(disambiguation),1):.1f}%)")
    print(f"  Review queue:             {len(review_queue)} items")
    print("=" * 60)


def main():
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===\n")

    disambiguate_all()


if __name__ == '__main__':
    main()
