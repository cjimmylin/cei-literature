#!/usr/bin/env python3
"""
Fix Author Names Comprehensive Script
Fixes papers where author names got split incorrectly.

Issues fixed:
1. "Clifford; Scott; Iyengar; Vijeth" -> "Scott Clifford; Vijeth Iyengar"
2. Abbreviated names like "B. G." -> Full names from arXiv
3. Missing complete author lists from "others"
"""

import csv
import re
import json
from pathlib import Path
from typing import Dict, List, Optional
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from urllib.parse import quote

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    write_paper,
    rebuild_frontmatter,
)
from vault_config import PAPERS_DIR, WORKSPACE_ROOT

BASE_CSV = WORKSPACE_ROOT / "Base.md"
ARXIV_API_BASE = "http://export.arxiv.org/api/query?"

# Load CSV data
def load_csv_data() -> Dict:
    """Load author data from Base.md CSV, indexed by key"""
    csv_data = {}
    with open(BASE_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['Key']
            csv_data[key] = {
                'authors': row.get('Author', ''),
                'title': row.get('Title', ''),
                'url': row.get('Url', ''),
                'doi': row.get('DOI', ''),
            }
    return csv_data


def extract_arxiv_id(url: str) -> Optional[str]:
    """Extract arXiv ID from URL"""
    if not url:
        return None
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
    if match:
        return match.group(1)
    return None


def fetch_arxiv_authors(arxiv_id: str) -> List[str]:
    """Fetch complete author list from arXiv API"""
    try:
        query = quote(f"id:{arxiv_id}")
        url = f"{ARXIV_API_BASE}search_query={query}&start=0&max_results=1"

        with urllib.request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                return []

            root = ET.fromstring(response.read())
            authors = []
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                for author_elem in entry.findall('atom:author', ns):
                    name_elem = author_elem.find('atom:name', ns)
                    if name_elem is not None:
                        authors.append(name_elem.text.strip())
            return authors
    except Exception:
        return []


def convert_csv_to_proper_format(csv_authors: str) -> List[str]:
    """
    Convert CSV author format "LastName, FirstName; LastName2, FirstName2"
    to "FirstName LastName" format
    """
    if not csv_authors:
        return []

    # Remove "others" and "et al"
    csv_authors = re.sub(r';\s*(?:others|et al).*$', '', csv_authors, flags=re.IGNORECASE)

    # Split by semicolon
    author_parts = csv_authors.split(';')

    proper_names = []
    for part in author_parts:
        part = part.strip()
        if not part or part.lower() in ['others', 'et al', 'and']:
            continue

        # Check if "LastName, FirstName" format
        if ',' in part:
            parts = [p.strip() for p in part.split(',', 1)]
            if len(parts) == 2:
                lastname, firstname = parts
                # Convert to "FirstName LastName"
                proper_names.append(f"{firstname} {lastname}")
            else:
                proper_names.append(part)
        else:
            # Already in "FirstName LastName" format or single name
            proper_names.append(part)

    return proper_names


def is_author_list_broken(authors_str: str) -> bool:
    """Check if author list has broken single-part names"""
    parts = authors_str.split(';')

    # Count how many parts look like single names (no spaces)
    single_parts = sum(1 for p in parts if p.strip() and ' ' not in p.strip())

    # If more than half are single parts, likely broken
    return single_parts > len(parts) / 2


def recombine_broken_names(broken_str: str) -> List[str]:
    """
    Attempt to recombine broken names like "Clifford; Scott; Iyengar; Vijeth"
    into "Scott Clifford; Vijeth Iyengar"
    """
    parts = [p.strip() for p in broken_str.split(';') if p.strip()]

    if len(parts) < 2:
        return parts

    # Try to pair consecutive parts as "LastName; FirstName"
    recombined = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts):
            # Check if this looks like a lastname-firstname pair
            part1 = parts[i]
            part2 = parts[i + 1]

            # If both are single words and part2 looks like a first name
            # (starts with capital, isn't a known suffix like "Jr.")
            if ' ' not in part1 and ' ' not in part2:
                # Assume it's "LastName; FirstName" - combine as "FirstName LastName"
                recombined.append(f"{part2} {part1}")
                i += 2
                continue

        # Otherwise keep as-is
        recombined.append(parts[i])
        i += 1

    return recombined


def fix_paper(paper_path: Path, csv_data: Dict, dry_run: bool = False) -> tuple:
    """Fix author names in a single paper. Returns (success, message)"""
    try:
        content = paper_path.read_text(encoding='utf-8')

        fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return (False, "No frontmatter")

        frontmatter = fm_match.group(1)
        body = content[fm_match.end():]

        fields = parse_frontmatter(frontmatter)
        key = fields.get('key', '')
        url = fields.get('url', '')
        current_authors = fields.get('authors', '')

        # Check if this paper needs fixing
        if not is_author_list_broken(current_authors):
            return (False, "Authors look OK")

        new_authors = []
        source = "unknown"

        # Strategy 1: Try arXiv API first (most reliable)
        arxiv_id = extract_arxiv_id(url)
        if arxiv_id:
            arxiv_authors = fetch_arxiv_authors(arxiv_id)
            if arxiv_authors and len(arxiv_authors) >= 2:
                new_authors = arxiv_authors
                source = "arXiv"

        # Strategy 2: Try CSV data with proper conversion
        if not new_authors and key in csv_data:
            csv_authors = csv_data[key]['authors']
            if csv_authors:
                converted = convert_csv_to_proper_format(csv_authors)
                if converted:
                    new_authors = converted
                    source = "CSV"

        # Strategy 3: Try recombining broken names
        if not new_authors:
            recombined = recombine_broken_names(current_authors)
            if recombined and recombined != current_authors.split(';'):
                # Check if recombined names have spaces (properly combined)
                if any(' ' in name for name in recombined):
                    new_authors = recombined
                    source = "recombined"

        if not new_authors:
            return (False, "Could not determine correct authors")

        # Update the paper
        new_authors_str = "; ".join(new_authors)
        fields['authors'] = new_authors_str

        # Rebuild frontmatter
        new_frontmatter = rebuild_frontmatter(fields)

        # Validate
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            return (False, f"Validation failed: {issues}")

        # Update wikilinks in body
        wikilinks = [f"[[{name}]]" for name in new_authors]

        # Update or add Authors section
        if '## Authors' in body:
            body = re.sub(
                r'(## Authors\n\n)[^\n]+',
                f"\\1{', '.join(wikilinks)}",
                body
            )
        else:
            # Add Authors section after Abstract
            abstract_match = re.search(r'(## Abstract\n.*?\n)(?=\n## |\n\n##|$)', body, re.DOTALL)
            if abstract_match:
                insert_pos = abstract_match.end()
                body = body[:insert_pos] + f"\n## Authors\n\n{', '.join(wikilinks)}\n" + body[insert_pos:]

        if not dry_run:
            write_paper(paper_path, new_frontmatter, body, validate=True)

        return (True, f"Fixed {len(new_authors)} authors from {source}")

    except Exception as e:
        return (False, str(e))


def main(dry_run: bool = False, limit: int = None):
    """Main execution"""
    print("=" * 100)
    print("FIX AUTHOR NAMES - COMPREHENSIVE")
    print("=" * 100)
    print()

    # Load CSV
    print("Loading CSV data...")
    csv_data = load_csv_data()
    print(f"✓ Loaded {len(csv_data)} entries\n")

    # Get papers
    papers = sorted(PAPERS_DIR.glob('*.md'))
    if limit:
        papers = papers[:limit]

    print(f"Processing {len(papers)} papers...\n")

    fixed = 0
    skipped = 0
    failed = 0

    results = {
        "fixed": [],
        "skipped": [],
        "failed": [],
    }

    for i, paper in enumerate(papers):
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1}/{len(papers)}...")

        success, message = fix_paper(paper, csv_data, dry_run)

        if success:
            fixed += 1
            results["fixed"].append({"paper": paper.name, "message": message})
            print(f"  ✓ {paper.name}: {message}")
        elif "look OK" in message:
            skipped += 1
            results["skipped"].append(paper.name)
        else:
            failed += 1
            results["failed"].append({"paper": paper.name, "error": message})
            if "Could not" not in message:
                print(f"  ✗ {paper.name}: {message}")

    # Summary
    print("\n" + "=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print(f"Papers fixed: {fixed}")
    print(f"Papers skipped (already OK): {skipped}")
    print(f"Papers failed: {failed}")

    if results["failed"]:
        print(f"\nFailed papers (first 20):")
        for item in results["failed"][:20]:
            print(f"  - {item['paper']}: {item['error']}")

    # Save results
    results_path = WORKSPACE_ROOT / "20260124-AUTHOR_FIX_RESULTS.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✓ Results saved to {results_path}")


if __name__ == "__main__":
    import sys

    dry_run = "--dry-run" in sys.argv
    limit = None

    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    main(dry_run=dry_run, limit=limit)
