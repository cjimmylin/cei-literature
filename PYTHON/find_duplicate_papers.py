#!/usr/bin/env python3
"""
Duplicate Paper Detection Script

Finds potential duplicate papers in the vault by:
1. Matching papers with identical DOIs
2. Finding papers with similar titles (>0.85 similarity using difflib)
3. Identifying papers with same authors and similar titles (possible republications)

Usage:
    .venv/bin/python PYTHON/find_duplicate_papers.py
"""

import re
from pathlib import Path
from difflib import SequenceMatcher
from collections import defaultdict


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from markdown content using regex."""
    if not content.startswith('---'):
        return {}, content

    # Find the closing ---
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return {}, content

    yaml_content = content[3:end_match.start() + 3]
    body = content[end_match.end() + 3 + 1:]

    # Parse YAML using regex (simple key: value pairs)
    frontmatter = {}
    for line in yaml_content.split('\n'):
        # Match key: value patterns
        match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*(.*)$', line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            # Remove surrounding quotes
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            frontmatter[key] = value

    return frontmatter, body


def extract_main_title(body: str) -> str:
    """Extract the main title from the body (first # heading)."""
    match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    if not title:
        return ""
    # Convert to lowercase, remove punctuation, extra spaces
    title = title.lower()
    title = re.sub(r'[^\w\s]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def normalize_doi(doi: str) -> str:
    """Normalize DOI for comparison."""
    if not doi:
        return ""
    doi = str(doi).strip().lower()
    # Skip placeholder values
    if doi in ('n/a', 'na', 'none', '', 'pending', 'unknown'):
        return ""
    # Remove common prefixes
    doi = re.sub(r'^https?://doi\.org/', '', doi)
    doi = re.sub(r'^doi:', '', doi)
    return doi.strip()


def get_first_author(authors: str) -> str:
    """Extract first author name from authors string."""
    if not authors:
        return ""
    # Split by semicolon or comma
    if ';' in authors:
        first = authors.split(';')[0]
    elif ',' in authors:
        # Could be "Last, First" or "Name1, Name2"
        first = authors.split(',')[0]
    else:
        first = authors
    return first.strip().lower()


def similarity(s1: str, s2: str) -> float:
    """Calculate similarity ratio between two strings."""
    if not s1 or not s2:
        return 0.0
    return SequenceMatcher(None, s1, s2).ratio()


def main():
    papers_dir = Path("/Users/jimmylin/Library/CloudStorage/GoogleDrive-mail@drjimmylin.com/Other computers/My Mac/CEI-Literature-Vault/papers")

    # Collect paper data
    papers = []

    for md_file in papers_dir.glob("*.md"):
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, body = extract_frontmatter(content)

            # Get title from various sources
            main_title = extract_main_title(body)
            short_title = frontmatter.get('short_title', '')
            if isinstance(short_title, str):
                short_title = short_title.strip('"\'')

            # Use main title if available, otherwise short_title
            title = main_title if main_title else short_title

            # Get DOI
            doi = frontmatter.get('doi', '') or frontmatter.get('DOI', '')

            # Get authors
            authors = frontmatter.get('authors', '')
            first_author = frontmatter.get('first_author', '')
            if first_author:
                # Clean up wiki link format [[Name]]
                first_author = re.sub(r'\[\[|\]\]', '', str(first_author))

            papers.append({
                'filename': md_file.name,
                'filepath': str(md_file),
                'title': title,
                'normalized_title': normalize_title(title),
                'doi': normalize_doi(str(doi) if doi else ''),
                'authors': str(authors) if authors else '',
                'first_author': first_author.lower() if first_author else get_first_author(str(authors) if authors else ''),
                'year': frontmatter.get('year', '')
            })
        except Exception as e:
            print(f"Error processing {md_file.name}: {e}")

    print(f"Processed {len(papers)} papers\n")

    # Find DOI duplicates
    doi_groups = defaultdict(list)
    for paper in papers:
        if paper['doi']:
            doi_groups[paper['doi']].append(paper)

    doi_duplicates = {k: v for k, v in doi_groups.items() if len(v) > 1}

    # Find title duplicates (similarity > 0.85)
    title_duplicates = []
    checked_pairs = set()

    for i, p1 in enumerate(papers):
        if not p1['normalized_title']:
            continue
        for j, p2 in enumerate(papers[i+1:], i+1):
            if not p2['normalized_title']:
                continue

            pair_key = tuple(sorted([p1['filename'], p2['filename']]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            sim = similarity(p1['normalized_title'], p2['normalized_title'])
            if sim > 0.85:
                title_duplicates.append({
                    'paper1': p1,
                    'paper2': p2,
                    'similarity': sim
                })

    # Find same-author similar titles (possible republications)
    republication_candidates = []
    checked_pairs = set()

    for i, p1 in enumerate(papers):
        if not p1['first_author'] or not p1['normalized_title']:
            continue
        for j, p2 in enumerate(papers[i+1:], i+1):
            if not p2['first_author'] or not p2['normalized_title']:
                continue

            pair_key = tuple(sorted([p1['filename'], p2['filename']]))
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            # Check if same first author
            if p1['first_author'] == p2['first_author']:
                title_sim = similarity(p1['normalized_title'], p2['normalized_title'])
                # Lower threshold for same author (0.6) - might be related works
                if 0.6 <= title_sim < 0.85:  # Avoid overlap with title duplicates
                    republication_candidates.append({
                        'paper1': p1,
                        'paper2': p2,
                        'similarity': title_sim
                    })

    # Generate report
    print("=" * 80)
    print("DUPLICATE PAPER DETECTION REPORT")
    print("=" * 80)

    print("\n" + "=" * 80)
    print("1. EXACT DOI MATCHES")
    print("=" * 80)

    if doi_duplicates:
        for doi, group in doi_duplicates.items():
            print(f"\nDOI: {doi}")
            print("-" * 40)
            for paper in group:
                print(f"  - {paper['filename']}")
                print(f"    Title: {paper['title'][:80]}...")
    else:
        print("\nNo exact DOI duplicates found.")

    print("\n" + "=" * 80)
    print("2. SIMILAR TITLES (>85% similarity)")
    print("=" * 80)

    if title_duplicates:
        # Sort by similarity (highest first)
        title_duplicates.sort(key=lambda x: x['similarity'], reverse=True)

        for dup in title_duplicates:
            p1, p2, sim = dup['paper1'], dup['paper2'], dup['similarity']
            print(f"\nSimilarity: {sim:.2%}")
            print("-" * 40)
            print(f"  Paper 1: {p1['filename']}")
            print(f"    Title: {p1['title'][:80]}...")
            print(f"    Year: {p1['year']}")
            print(f"  Paper 2: {p2['filename']}")
            print(f"    Title: {p2['title'][:80]}...")
            print(f"    Year: {p2['year']}")
    else:
        print("\nNo highly similar titles found.")

    print("\n" + "=" * 80)
    print("3. SAME AUTHOR, MODERATELY SIMILAR TITLES (60-85%)")
    print("   (Potential republications or related works)")
    print("=" * 80)

    if republication_candidates:
        # Sort by similarity (highest first)
        republication_candidates.sort(key=lambda x: x['similarity'], reverse=True)

        for dup in republication_candidates:
            p1, p2, sim = dup['paper1'], dup['paper2'], dup['similarity']
            print(f"\nSimilarity: {sim:.2%} | First Author: {p1['first_author']}")
            print("-" * 40)
            print(f"  Paper 1: {p1['filename']}")
            print(f"    Title: {p1['title'][:80]}...")
            print(f"    Year: {p1['year']}")
            print(f"  Paper 2: {p2['filename']}")
            print(f"    Title: {p2['title'][:80]}...")
            print(f"    Year: {p2['year']}")
    else:
        print("\nNo republication candidates found.")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total papers analyzed: {len(papers)}")
    print(f"DOI duplicates found: {len(doi_duplicates)} groups")
    print(f"Similar title pairs (>85%): {len(title_duplicates)}")
    print(f"Same-author similar titles (60-85%): {len(republication_candidates)}")

    return {
        'total_papers': len(papers),
        'doi_duplicates': doi_duplicates,
        'title_duplicates': title_duplicates,
        'republication_candidates': republication_candidates
    }


if __name__ == "__main__":
    main()
