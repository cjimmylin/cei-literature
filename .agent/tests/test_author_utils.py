"""Tests for lib.author_utils."""

import pytest
from pathlib import Path
from lib import author_utils


def test_get_all_authors(sample_authors):
    """Test getting all author profiles."""
    from lib import config
    original_authors_dir = config.AUTHORS_DIR

    try:
        config.AUTHORS_DIR = sample_authors
        authors = author_utils.get_all_authors()

        assert len(authors) == 3
        assert all(a.suffix == ".md" for a in authors)
        assert all(a.exists() for a in authors)
    finally:
        config.AUTHORS_DIR = original_authors_dir


def test_find_orphaned_authors(sample_authors, sample_papers):
    """Test finding orphaned authors not referenced by papers."""
    from lib import config
    original_authors_dir = config.AUTHORS_DIR
    original_papers_dir = config.PAPERS_DIR

    try:
        config.AUTHORS_DIR = sample_authors
        config.PAPERS_DIR = sample_papers

        # All authors should be orphaned since sample papers reference different authors
        orphaned = author_utils.find_orphaned_authors()
        assert len(orphaned) == 3
    finally:
        config.AUTHORS_DIR = original_authors_dir
        config.PAPERS_DIR = original_papers_dir


def test_get_authors_by_enrichment_status(sample_authors):
    """Test finding authors by enrichment status."""
    from lib import config
    original_authors_dir = config.AUTHORS_DIR

    try:
        config.AUTHORS_DIR = sample_authors

        # All sample authors are enriched
        enriched = author_utils.get_authors_by_enrichment_status(enriched=True)
        assert len(enriched) == 3

        # None should be non-enriched
        not_enriched = author_utils.get_authors_by_enrichment_status(enriched=False)
        assert len(not_enriched) == 0
    finally:
        config.AUTHORS_DIR = original_authors_dir


def test_validate_author_profile(sample_authors):
    """Test validating author profile completeness."""
    from lib import config
    original_authors_dir = config.AUTHORS_DIR

    try:
        config.AUTHORS_DIR = sample_authors
        authors = author_utils.get_all_authors()

        result = author_utils.validate_author_profile(authors[0])

        assert result["valid"] is True
        assert len(result["errors"]) == 0
        # Should have no warnings since profile has institution and is enriched
        assert len(result["warnings"]) == 0
    finally:
        config.AUTHORS_DIR = original_authors_dir


def test_validate_author_profile_missing_header(tmp_vault):
    """Test validation catches missing header."""
    from lib import config
    original_authors_dir = config.AUTHORS_DIR

    try:
        authors_dir = tmp_vault / "Authors"
        bad_author = authors_dir / "BadAuthor.md"
        bad_author.write_text("No header here\n\nenriched: true")

        config.AUTHORS_DIR = authors_dir

        result = author_utils.validate_author_profile(bad_author)

        assert result["valid"] is False
        assert any("header" in err.lower() for err in result["errors"])
    finally:
        config.AUTHORS_DIR = original_authors_dir


def test_get_author_paper_count(sample_papers):
    """Test counting papers by author."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers

        # Sample papers' first authors are John Author0, John Author1, John Author2
        count = author_utils.get_author_paper_count("John Author0")
        assert count == 1

        # Non-existent author
        count = author_utils.get_author_paper_count("Nonexistent")
        assert count == 0
    finally:
        config.PAPERS_DIR = original_papers_dir
