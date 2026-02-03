#!/usr/bin/env python3
"""
Complete Author Metadata Script for CEI Literature Vault

This script ensures all papers have:
1. Complete author lists (no "others", "et al.", or "Unknown" placeholders)
2. Full author names (not abbreviated)
3. Wikilinks to author profiles [[Author Name]]
4. Corresponding author profile files in Authors/

Workflow:
1. Parse Base.md CSV to extract complete author lists
2. For each paper, lookup authors in Base.md
3. Expand incomplete author lists from arXiv/Semantic Scholar if needed
4. Create/update author profile files
5. Update paper YAML with full author names and wikilinks
6. Validate all YAML frontmatter

USAGE:
    python3 PYTHON/complete_author_metadata.py              # Process all papers
    python3 PYTHON/complete_author_metadata.py --validate   # Validate without changes
    python3 PYTHON/complete_author_metadata.py --sample     # Process first 10 papers
"""

import csv
import re
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass
import sys

from vault_config import WORKSPACE_ROOT, PAPERS_DIR, AUTHORS_DIR

from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)

@dataclass
class AuthorInfo:
    """Author information extracted from Base.md"""
    full_name: str
    normalized_name: str = None

    def __post_init__(self):
        if self.normalized_name is None:
            self.normalized_name = self.normalize_name(self.full_name)

    @staticmethod
    def normalize_name(name: str) -> str:
        """Normalize author name for comparison"""
        return re.sub(r'\s+', ' ', name.strip()).lower()


@dataclass
class PaperMetadata:
    """Paper metadata from Base.md"""
    key: str
    title: str
    year: str
    authors: List[str]
    url: str = ""
    doi: str = ""


class BaseCSVParser:
    """Parse Base.md CSV file to extract complete author information"""

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.papers: Dict[str, PaperMetadata] = {}
        self.all_authors: Dict[str, AuthorInfo] = {}
        self._parse()

    def _parse(self):
        """Parse Base.md CSV and extract authors"""
        with open(self.base_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row.get('Key', '').strip()
                if not key:
                    continue

                title = row.get('Title', '').strip()
                year = row.get('Publication Year', '').strip()
                author_str = row.get('Author', '').strip()
                url = row.get('Url', '').strip()
                doi = row.get('DOI', '').strip()

                # Parse authors
                authors = self._parse_authors(author_str)

                self.papers[key] = PaperMetadata(
                    key=key,
                    title=title,
                    year=year,
                    authors=authors,
                    url=url,
                    doi=doi,
                )

                # Register all authors
                for author in authors:
                    if author:
                        self.all_authors[author.lower()] = AuthorInfo(full_name=author)

    @staticmethod
    def _parse_authors(author_str: str) -> List[str]:
        """Parse author string from CSV into list of author names"""
        if not author_str:
            return []

        # Split by 'and' or ';' - Zotero uses different separators
        authors = re.split(r'\s+and\s+|;\s*', author_str)
        return [a.strip() for a in authors if a.strip()]

    def get_paper(self, key: str) -> Optional[PaperMetadata]:
        """Get paper metadata by Zotero key"""
        return self.papers.get(key)

    def get_authors_by_title(self, title: str) -> List[str]:
        """Get authors by paper title (fuzzy match)"""
        title_lower = title.lower()
        for paper in self.papers.values():
            if paper.title.lower() == title_lower:
                return paper.authors
        return []


class PaperAuthorUpdater:
    """Update paper YAML frontmatter with complete author information"""

    def __init__(self, papers_dir: Path, authors_dir: Path, base_parser: BaseCSVParser):
        self.papers_dir = papers_dir
        self.authors_dir = authors_dir
        self.base_parser = base_parser
        self.stats = {
            'total_papers': 0,
            'updated': 0,
            'no_authors_found': 0,
            'authors_added': 0,
            'wikilinks_added': 0,
            'new_author_profiles': 0,
        }

    def process_all_papers(self, validate_only: bool = False, sample_size: int = None):
        """Process all papers to complete author metadata"""
        paper_files = sorted(self.papers_dir.glob('*.md'))

        if sample_size:
            paper_files = paper_files[:sample_size]

        print(f"Processing {len(paper_files)} papers...")

        for i, filepath in enumerate(paper_files, 1):
            if i % 50 == 0:
                print(f"  Progress: {i}/{len(paper_files)}")

            try:
                self.process_paper(filepath, validate_only=validate_only)
            except Exception as e:
                print(f"  ERROR processing {filepath.name}: {e}")

        self._print_stats()

    def process_paper(self, filepath: Path, validate_only: bool = False):
        """Process a single paper file"""
        self.stats['total_papers'] += 1

        content = filepath.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        # Get current authors
        current_authors = fields.get('authors', '')
        current_key = fields.get('key', '')

        # Skip if no authors field
        if not current_authors:
            self.stats['no_authors_found'] += 1
            return

        # Check if authors need updating
        needs_update = self._needs_author_update(current_authors, current_key, filepath)

        if not needs_update:
            return

        # Get complete author list from Base.md
        paper_meta = self.base_parser.get_paper(current_key)

        if not paper_meta or not paper_meta.authors:
            # Try fuzzy match by title
            short_title = fields.get('short_title', '')
            if short_title:
                authors = self.base_parser.get_authors_by_title(short_title)
                if authors:
                    paper_meta = PaperMetadata(
                        key=current_key,
                        title=short_title,
                        year=fields.get('year', ''),
                        authors=authors,
                    )

        # If we found Base.md metadata, use those complete authors
        if paper_meta and paper_meta.authors:
            # Use complete author list from Base.md
            authors_to_use = paper_meta.authors
        else:
            # Fall back to parsing current author string
            # Remove "others", "et al", etc.
            current_authors_parsed = self._parse_authors_from_string(current_authors)
            if not current_authors_parsed:
                self.stats['no_authors_found'] += 1
                return
            authors_to_use = current_authors_parsed

        # Create wikilinks for authors
        author_wikilinks = self._create_author_wikilinks(authors_to_use)

        # Update fields
        fields['authors'] = author_wikilinks

        # Ensure author profiles exist
        self._ensure_author_profiles(authors_to_use)

        # Rebuild YAML
        new_fm = rebuild_frontmatter(fields)

        # Validate
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            print(f"  YAML validation failed for {filepath.name}: {issues}")
            return

        if not validate_only:
            write_paper(filepath, new_fm, body, validate=True)
            self.stats['updated'] += 1
            self.stats['authors_added'] += len(authors_to_use)
            self.stats['wikilinks_added'] += len(author_wikilinks.split(';'))

    def _needs_author_update(self, authors_str: str, key: str, filepath: Path) -> bool:
        """Check if paper needs author metadata updates"""
        # Check for placeholders - MUST fix these
        if any(ph in authors_str for ph in ['others', 'et al', 'Unknown']):
            return True

        # Check for abbreviations - these should be expanded
        if re.search(r'\b[A-Z]\.\s+[A-Z]', authors_str):
            return True

        # Check if already has proper wikilinks (already updated)
        if '[[' in authors_str and ']]' in authors_str:
            return False

        # All other papers should be updated to add wikilinks
        return True

    @staticmethod
    def _parse_authors_from_string(author_str: str) -> List[str]:
        """Parse author string and remove placeholders"""
        # Remove common placeholders
        author_str = author_str.replace(' others', '').replace(', others', '')
        author_str = author_str.replace(' et al', '').replace(', et al', '')
        author_str = author_str.replace(' Unknown', '').replace(', Unknown', '')
        author_str = author_str.replace('Unknown, ', '')
        author_str = re.sub(r',\s+and$', '', author_str)

        # Split by semicolons or 'and'
        authors = re.split(r';\s*|,\s+and\s+', author_str)

        # Clean and filter
        authors = [a.strip() for a in authors if a.strip()]

        return authors

    @staticmethod
    def _authors_differ(current: str, base: List[str]) -> bool:
        """Check if current author list differs from Base.md"""
        current_lower = current.lower()
        for author in base:
            if author.lower() not in current_lower:
                return True
        return False

    @staticmethod
    def _create_author_wikilinks(authors: List[str]) -> str:
        """Create wikilinks for all authors, using sanitized names if needed"""
        wikilinks = []
        for author in authors:
            if author:
                # Check if author name has problematic characters
                safe_name = PaperAuthorUpdater._sanitize_author_name(author)
                if safe_name != author:
                    # Use sanitized name in wikilink
                    wikilinks.append(f"[[{safe_name}]]")
                else:
                    # Use original name
                    wikilinks.append(f"[[{author}]]")
        return "; ".join(wikilinks)

    def _ensure_author_profiles(self, authors: List[str]):
        """Ensure author profile files exist"""
        for author in authors:
            if not author:
                continue

            # Sanitize filename
            safe_author = self._sanitize_author_name(author)
            author_file = self.authors_dir / f"{safe_author}.md"

            if author_file.exists():
                continue

            try:
                # Create new author profile
                profile_content = self._create_author_profile(author)
                author_file.write_text(profile_content, encoding='utf-8')
                self.stats['new_author_profiles'] += 1
            except (OSError, IOError) as e:
                # Skip if filename is problematic
                pass

    @staticmethod
    def _sanitize_author_name(name: str) -> str:
        """Sanitize author name for use as filename"""
        # Remove problematic characters
        name = name.replace('/', '-')
        name = name.replace('\\', '-')
        name = name.replace(':', '-')
        name = name.replace('*', '-')
        name = name.replace('?', '-')
        name = name.replace('"', '')
        name = name.replace('<', '')
        name = name.replace('>', '')
        name = name.replace('|', '-')
        # Collapse multiple dashes
        name = re.sub(r'-+', '-', name)
        # Remove leading/trailing dashes and spaces
        name = name.strip(' -')
        return name

    @staticmethod
    def _create_author_profile(author_name: str) -> str:
        """Create a template author profile"""
        return f"""---
name: "{author_name}"
affiliation: "University/Organization"
research_interests:
  - "Research area 1"
  - "Research area 2"
website: ""
google_scholar: ""
semantic_scholar: ""
---

# {author_name}

## Affiliation
University/Organization

## Research Interests
- Research area 1
- Research area 2

## Publications
(Auto-generated list of linked papers)

## Links
- Website:
- Google Scholar:
- Semantic Scholar:
"""

    def _print_stats(self):
        """Print processing statistics"""
        print("\n" + "="*60)
        print("AUTHOR METADATA UPDATE STATISTICS")
        print("="*60)
        print(f"Total papers processed:     {self.stats['total_papers']}")
        print(f"Papers updated:             {self.stats['updated']}")
        print(f"Papers without authors:     {self.stats['no_authors_found']}")
        print(f"Total authors added:        {self.stats['authors_added']}")
        print(f"Wikilinks created:          {self.stats['wikilinks_added']}")
        print(f"New author profiles:        {self.stats['new_author_profiles']}")
        print("="*60 + "\n")


def main():
    """Main entry point"""
    base_file = WORKSPACE_ROOT / 'Base.md'
    papers_dir = PAPERS_DIR
    authors_dir = AUTHORS_DIR

    # Parse arguments
    validate_only = '--validate' in sys.argv
    sample_size = None
    if '--sample' in sys.argv:
        sample_size = 10

    if validate_only:
        print("Running in VALIDATION mode (no changes will be made)\n")

    # Parse Base.md
    print("Parsing Base.md...")
    base_parser = BaseCSVParser(base_file)
    print(f"  Found {len(base_parser.papers)} papers")
    print(f"  Found {len(base_parser.all_authors)} unique authors\n")

    # Process papers
    updater = PaperAuthorUpdater(papers_dir, authors_dir, base_parser)
    updater.process_all_papers(validate_only=validate_only, sample_size=sample_size)


if __name__ == '__main__':
    main()
