"""Tests for lib.paper_utils."""

import pytest
from pathlib import Path
from lib import paper_utils


def test_get_all_papers(sample_papers):
    """Test getting all papers from directory."""
    # Note: sample_papers fixture uses tmp_vault
    # We need to temporarily override PAPERS_DIR
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers
        papers = paper_utils.get_all_papers()

        assert len(papers) == 3
        assert all(p.suffix == ".md" for p in papers)
        assert all(p.exists() for p in papers)
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_get_papers_by_field(sample_papers, sample_paper_content):
    """Test finding papers by field value."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers

        # Search by year
        papers = paper_utils.get_papers_by_field("year", "2024")
        assert len(papers) == 3

        # Search by non-existent value
        papers = paper_utils.get_papers_by_field("year", "2099")
        assert len(papers) == 0
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_get_papers_missing_field(sample_papers):
    """Test finding papers missing a field."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers

        # All papers should have 'key' field
        missing = paper_utils.get_papers_missing_field("key")
        assert len(missing) == 0

        # No papers have 'nonexistent_field'
        missing = paper_utils.get_papers_missing_field("nonexistent_field")
        assert len(missing) == 3
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_update_paper_field(sample_papers):
    """Test updating a single field in a paper."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers
        papers = paper_utils.get_all_papers()
        test_paper = papers[0]

        # Update a field
        result = paper_utils.update_paper_field(test_paper, "year", "2025")
        assert result is True

        # Verify update
        content = test_paper.read_text()
        assert "year: 2025" in content
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_batch_update_papers(sample_papers):
    """Test batch updating multiple papers."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers
        papers = paper_utils.get_all_papers()

        # Update all papers
        updates = {"year": "2025", "ethics_overall": "No"}
        results = paper_utils.batch_update_papers(papers, updates)

        assert results["success"] == 3
        assert results["failed"] == 0

        # Verify updates
        for paper in papers:
            content = paper.read_text()
            assert "year: 2025" in content
            assert 'ethics_overall: "No"' in content
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_get_paper_stats(sample_papers):
    """Test getting paper statistics."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        config.PAPERS_DIR = sample_papers

        stats = paper_utils.get_paper_stats()

        assert stats["total"] == 3
        assert stats["with_ethics_overall"] == 3
        # Sample papers don't have PDFs or extracts
        assert stats["with_pdfs"] == 0
        assert stats["with_extracts"] == 0
    finally:
        config.PAPERS_DIR = original_papers_dir
