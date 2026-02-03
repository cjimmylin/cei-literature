#!/usr/bin/env python3
"""
Fix Remaining Author Issues
Targeted fix for the 26 papers still having author name issues.
"""

import re
import json
from pathlib import Path
from typing import List
import urllib.request
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
ARXIV_API_BASE = "http://export.arxiv.org/api/query?"

# Manual mappings for known problematic papers
MANUAL_AUTHOR_FIXES = {
    "2016-Purzycki-Religious Belief and the Moral Circle.md": [
        "Benjamin Grant Purzycki"  # B. G. Purzycki -> full name
    ],
    "2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020.md": [
        "Dorine van Norren"
    ],
    "2021-Cao-Toward Gender-Inclusive Coreference Resolution.md": [
        "Yang Trista Cao", "Hal Daumé III"
    ],
    "2021-Munshi-Towards an Automated Islamic Fatwa System.md": [
        "Amr A. Munshi", "Wesam H. AlSabban", "Abdullah Tarek Farag",
        "Omar Essam Rakha", "Ahmad A. Al Sallab", "Ibrahim Alotaibi", "Majid Majid"
    ],
    "2023-Alyemny-Fatwaset An Arabic Dataset of Islamic Fatwas.md": [
        "A. Alyemny"
    ],
    "2023-Astobiza-MoralNet.md": [
        "Aníbal M. Astobiza"
    ],
    "2023-Kim-KOME.md": [
        "Hamin Kim"
    ],
    "2023-Lakera-GandalfIgnoreInstructions.md": [
        "Lakera AI"  # Organization name
    ],
    "2023-Ray-Benchmarking, ethical alignment, and evaluation.md": [
        "Partha Pratim Ray"
    ],
    "2023-Standards-NIST AI Risk Management Framework.md": [
        "National Institute of Standards and Technology (NIST)"
    ],
    "2024-Mou-SG-Bench.md": [
        "Xiangyu Mou"  # From arXiv
    ],
    "2024-Techne-Briefing.md": [
        "Techne Briefing"  # Organization
    ],
    # Additional manual fixes for remaining papers
    "2023-TheDevastator-HelpSteer A-i Alignment Dataset.md": [
        "TheDevastator"  # Kaggle username - keep as-is
    ],
    "2023-TheDevastator-OpenAssistant Conversations (OASST1).md": [
        "TheDevastator"  # Kaggle username - keep as-is
    ],
    "2024-Aakanksha-The Multilingual Alignment Prism.md": [
        "Aakanksha", "Arash Ahmadian", "Beyza Ermis", "Seraphina Goldfarb-Tarrant",
        "Julia Kreutzer", "Marzieh Fadaee", "Sara Hooker"
    ],
    "2024-MLCommons-MLCommons AILuminate Benchmark.md": [
        "MLCommons"  # Organization
    ],
    "2024-Mokoena-A holistic ubuntu artificial intelligence ethics.md": [
        "Katleho K. Mokoena"
    ],
    "2025-Aleid-Hajj-FQA.md": [
        "Hayfa A. Aleid", "Aqil M. Azmi"
    ],
    "2025-Flores-BenchMoral.md": [
        "Félix B. A. Flores"
    ],
    "2025-Steen-Ethical aspects of ChatGPT.md": [
        "Marc Steen"
    ],
    "2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.md": [
        "Muhammad Shahrul Zaim Bin Ahmad", "Kazuhiro Takemoto"  # Malay name format
    ],
}


def extract_arxiv_id(url: str) -> str:
    """Extract arXiv ID from URL"""
    if not url:
        return ""
    match = re.search(r'arxiv\.org/(?:abs|pdf)/(\d+\.\d+)', url)
    return match.group(1) if match else ""


def fetch_arxiv_authors(arxiv_id: str) -> List[str]:
    """Fetch authors from arXiv"""
    try:
        url = f"{ARXIV_API_BASE}search_query={quote(f'id:{arxiv_id}')}&start=0&max_results=1"
        with urllib.request.urlopen(url, timeout=10) as response:
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


def recombine_split_authors(authors_str: str) -> List[str]:
    """
    Try to recombine split authors like "Munshi; Amr A.; AlSabban; Wesam H."
    into "Amr A. Munshi; Wesam H. AlSabban"
    """
    parts = [p.strip() for p in authors_str.split(';') if p.strip()]
    if len(parts) < 2:
        return parts

    # Try to pair consecutive items
    recombined = []
    i = 0
    while i < len(parts):
        current = parts[i]

        # Check if current is a single word (potential last name)
        if ' ' not in current and i + 1 < len(parts):
            next_part = parts[i + 1]

            # Check if next is a first name (has spaces or is short)
            if next_part and not next_part[0].islower():
                # Combine as "FirstName LastName"
                recombined.append(f"{next_part} {current}")
                i += 2
                continue

        recombined.append(current)
        i += 1

    return recombined


def fix_paper(paper_path: Path) -> tuple:
    """Fix authors in a single paper"""
    paper_name = paper_path.name

    content = paper_path.read_text(encoding='utf-8')

    fm_match = re.match(r'---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        return (False, "No frontmatter")

    frontmatter = fm_match.group(1)
    body = content[fm_match.end():]

    fields = parse_frontmatter(frontmatter)
    current_authors = fields.get('authors', '')
    url = fields.get('url', '')

    new_authors = []
    source = ""

    # Strategy 1: Use manual mapping
    if paper_name in MANUAL_AUTHOR_FIXES:
        new_authors = MANUAL_AUTHOR_FIXES[paper_name]
        source = "manual"

    # Strategy 2: Try arXiv
    if not new_authors:
        arxiv_id = extract_arxiv_id(url)
        if arxiv_id:
            arxiv_authors = fetch_arxiv_authors(arxiv_id)
            if arxiv_authors:
                new_authors = arxiv_authors
                source = "arXiv"

    # Strategy 3: Recombine split names
    if not new_authors:
        recombined = recombine_split_authors(current_authors)
        # Check if recombination improved things (more multi-word names)
        multi_word_before = sum(1 for a in current_authors.split(';') if ' ' in a.strip())
        multi_word_after = sum(1 for a in recombined if ' ' in a)

        if multi_word_after > multi_word_before:
            new_authors = recombined
            source = "recombined"

    if not new_authors:
        return (False, "No fix found")

    # Update paper
    fields['authors'] = "; ".join(new_authors)
    new_frontmatter = rebuild_frontmatter(fields)

    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        return (False, f"Validation failed: {issues}")

    # Update wikilinks in body
    wikilinks = [f"[[{name}]]" for name in new_authors]

    if '## Authors' in body:
        body = re.sub(
            r'(## Authors\n\n)[^\n]+',
            f"\\1{', '.join(wikilinks)}",
            body
        )

    write_paper(paper_path, new_frontmatter, body, validate=True)

    return (True, f"Fixed {len(new_authors)} authors from {source}")


def main():
    """Main execution"""
    print("=" * 100)
    print("FIX REMAINING AUTHOR ISSUES")
    print("=" * 100)
    print()

    # Load list of problematic papers
    issues_file = WORKSPACE_ROOT / "REMAINING_AUTHOR_ISSUES.json"

    if not issues_file.exists():
        print("No issues file found. Run analysis first.")
        return

    with open(issues_file, 'r') as f:
        issues = json.load(f)

    # Get all papers that need fixing
    papers_to_fix = set()
    for item in issues.get("initials_only", []):
        papers_to_fix.add(item["paper"])
    for item in issues.get("single_word", []):
        papers_to_fix.add(item["paper"])

    print(f"Papers to fix: {len(papers_to_fix)}")
    print()

    fixed = 0
    failed = 0

    for paper_name in sorted(papers_to_fix):
        paper_path = PAPERS_DIR / paper_name
        if not paper_path.exists():
            print(f"  ⚠️ {paper_name}: File not found")
            failed += 1
            continue

        success, message = fix_paper(paper_path)

        if success:
            print(f"  ✓ {paper_name}: {message}")
            fixed += 1
        else:
            print(f"  ✗ {paper_name}: {message}")
            failed += 1

    print("\n" + "=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print(f"Fixed: {fixed}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
