"""Author profile operations and validation.

This module provides utilities for managing author profiles,
including finding orphaned authors, checking enrichment status,
and validating profile completeness.
"""

from pathlib import Path
from typing import List, Dict
from lib.config import AUTHORS_DIR, PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


def get_all_authors() -> List[Path]:
    """Return all author profile files.

    Returns:
        List of Path objects for all .md files in Authors directory, sorted by name.
    """
    return sorted(AUTHORS_DIR.glob("*.md"))


def find_orphaned_authors() -> List[Path]:
    """Find author files not referenced by any paper.

    Returns:
        List of Path objects for orphaned author files
    """
    # Get all author names from files
    all_authors = {f.stem for f in get_all_authors()}

    # Get all referenced authors from papers
    referenced = set()
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "first_author" in fields:
            # Extract author name from wikilink: "[[Author Name]]"
            author = fields["first_author"].strip('"').strip('[]')
            referenced.add(author)

    # Find orphans
    orphaned = all_authors - referenced
    return [AUTHORS_DIR / f"{author}.md" for author in orphaned]


def get_authors_by_enrichment_status(enriched: bool = True) -> List[Path]:
    """Find authors by enrichment status.

    Args:
        enriched: If True, find enriched authors; if False, find non-enriched

    Returns:
        List of Path objects for matching author files
    """
    matching = []
    for author_file in get_all_authors():
        content = author_file.read_text()

        # Check for enriched flag in frontmatter
        if enriched:
            if "enriched: true" in content:
                matching.append(author_file)
        else:
            if "enriched: true" not in content:
                matching.append(author_file)

    return matching


def validate_author_profile(filepath: Path) -> Dict[str, any]:
    """Validate author profile completeness.

    Args:
        filepath: Path to the author profile file

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if profile is valid
        - warnings: List of warning messages
        - errors: List of error messages
    """
    result = {
        "valid": True,
        "warnings": [],
        "errors": [],
    }

    content = filepath.read_text()

    # Check for basic structure
    if not content.startswith("# "):
        result["errors"].append("Missing author name header")
        result["valid"] = False

    # Check for enrichment
    if "enriched: true" not in content:
        result["warnings"].append("Not enriched")

    # Check for institution
    if "institution:" not in content.lower() and "affiliation" not in content.lower():
        result["warnings"].append("Missing institution/affiliation")

    return result


def get_author_paper_count(author_name: str) -> int:
    """Count papers by a specific author.

    Args:
        author_name: The author name to search for

    Returns:
        Number of papers authored by this author
    """
    count = 0
    search_pattern = f'"[[{author_name}]]"'

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        if search_pattern in content:
            count += 1

    return count
