"""Paper file operations and bulk updates.

This module provides utilities for working with paper files in the vault,
including querying, filtering, updating, and gathering statistics.
"""

from pathlib import Path
from typing import List, Dict
from lib.config import PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, write_paper, parse_frontmatter, rebuild_frontmatter


def get_all_papers() -> List[Path]:
    """Return all paper files in papers/ directory.

    Returns:
        List of Path objects for all .md files in papers directory, sorted by name.
    """
    return sorted(PAPERS_DIR.glob("*.md"))


def get_papers_by_field(field: str, value: str) -> List[Path]:
    """Find papers where field matches value.

    Args:
        field: The frontmatter field name to search
        value: The value to match (exact match)

    Returns:
        List of Path objects for matching papers
    """
    matching = []
    for paper in get_all_papers():
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)
        if fields.get(field) == value:
            matching.append(paper)
    return matching


def get_papers_missing_field(field: str) -> List[Path]:
    """Find papers missing a specific field.

    Args:
        field: The frontmatter field name to check

    Returns:
        List of Path objects for papers missing the field
    """
    missing = []
    for paper in get_all_papers():
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)
        if field not in fields:
            missing.append(paper)
    return missing


def update_paper_field(filepath: Path, field: str, value: str) -> bool:
    """Update a single field in a paper.

    Args:
        filepath: Path to the paper file
        field: The field name to update
        value: The new value for the field

    Returns:
        True if update succeeded, False otherwise
    """
    try:
        content = filepath.read_text()
        fm, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        fields[field] = value

        new_fm = rebuild_frontmatter(fields)
        write_paper(filepath, new_fm, body, validate=True)
        return True
    except Exception as e:
        print(f"Failed to update {filepath.name}: {e}")
        return False


def batch_update_papers(papers: List[Path], updates: Dict[str, str]) -> Dict[str, int]:
    """Update multiple papers with same field changes.

    Args:
        papers: List of paper files to update
        updates: Dictionary of field names to new values

    Returns:
        Dictionary with "success" and "failed" counts
    """
    results = {"success": 0, "failed": 0}

    for paper in papers:
        try:
            content = paper.read_text()
            fm, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm)

            # Apply all updates
            for field, value in updates.items():
                fields[field] = value

            new_fm = rebuild_frontmatter(fields)
            write_paper(paper, new_fm, body, validate=True)
            results["success"] += 1
        except Exception as e:
            print(f"Failed {paper.name}: {e}")
            results["failed"] += 1

    return results


def get_paper_stats() -> Dict[str, int]:
    """Get statistics about papers in vault.

    Returns:
        Dictionary with counts for various paper attributes:
        - total: Total number of papers
        - with_ethics_overall: Papers with ethics_overall field
        - with_pdfs: Papers with local_pdf field
        - with_extracts: Papers with pdf_extract field
    """
    papers = get_all_papers()

    stats = {
        "total": len(papers),
        "with_ethics_overall": 0,
        "with_pdfs": 0,
        "with_extracts": 0,
    }

    for paper in papers:
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "ethics_overall" in fields:
            stats["with_ethics_overall"] += 1
        if "local_pdf" in fields:
            stats["with_pdfs"] += 1
        if "pdf_extract" in fields:
            stats["with_extracts"] += 1

    return stats
