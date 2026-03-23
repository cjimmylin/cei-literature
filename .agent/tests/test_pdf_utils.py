"""Tests for lib.pdf_utils."""

import pytest
from pathlib import Path
from lib import pdf_utils


def test_validate_pdf_link_valid(tmp_vault):
    """Test validating a valid PDF link."""
    from lib import config
    original_pdfs_dir = config.PDFS_DIR

    try:
        pdfs_dir = tmp_vault / "PDFs"
        test_pdf = pdfs_dir / "test.pdf"
        test_pdf.write_text("PDF content")

        config.PDFS_DIR = pdfs_dir

        result = pdf_utils.validate_pdf_link('"[[Lit-WS-PDFs/test.pdf]]"', "TestPaper")

        assert result["valid"] is True
        assert len(result["errors"]) == 0
        assert result["path"] == test_pdf
    finally:
        config.PDFS_DIR = original_pdfs_dir


def test_validate_pdf_link_missing():
    """Test validating a missing PDF link."""
    from lib import config

    result = pdf_utils.validate_pdf_link('"[[Lit-WS-PDFs/nonexistent.pdf]]"', "TestPaper")

    assert result["valid"] is False
    assert len(result["errors"]) > 0
    assert "not found" in result["errors"][0].lower()


def test_validate_pdf_link_empty():
    """Test validating an empty PDF link."""
    result = pdf_utils.validate_pdf_link("", "TestPaper")

    assert result["valid"] is False
    assert "No PDF link" in result["errors"][0]


def test_validate_extract_link_valid(tmp_vault):
    """Test validating a valid extract link."""
    from lib import config
    original_extracts_dir = config.PDF_EXTRACTS_DIR

    try:
        extracts_dir = tmp_vault / "PDF Extracts"
        test_extract = extracts_dir / "test.md"
        test_extract.write_text("Extract content")

        config.PDF_EXTRACTS_DIR = extracts_dir

        result = pdf_utils.validate_extract_link("PDF Extracts/test.md", "TestPaper")

        assert result["valid"] is True
        assert len(result["errors"]) == 0
        assert result["path"] == test_extract
    finally:
        config.PDF_EXTRACTS_DIR = original_extracts_dir


def test_find_orphaned_pdfs(tmp_vault, sample_papers):
    """Test finding orphaned PDF files."""
    from lib import config
    original_pdfs_dir = config.PDFS_DIR
    original_papers_dir = config.PAPERS_DIR

    try:
        pdfs_dir = tmp_vault / "PDFs"

        # Create some PDFs
        (pdfs_dir / "orphaned.pdf").write_text("content")
        (pdfs_dir / "also_orphaned.pdf").write_text("content")

        config.PDFS_DIR = pdfs_dir
        config.PAPERS_DIR = sample_papers

        orphaned = pdf_utils.find_orphaned_pdfs()

        assert len(orphaned) == 2
        assert all(p.suffix == ".pdf" for p in orphaned)
    finally:
        config.PDFS_DIR = original_pdfs_dir
        config.PAPERS_DIR = original_papers_dir


def test_find_missing_pdfs(tmp_vault):
    """Test finding papers with missing PDF files."""
    from lib import config
    from lib.yaml_utils import write_paper, extract_frontmatter

    original_papers_dir = config.PAPERS_DIR
    original_pdfs_dir = config.PDFS_DIR

    try:
        papers_dir = tmp_vault / "papers"
        pdfs_dir = tmp_vault / "PDFs"

        # Create a paper with PDF link but no actual PDF
        paper = papers_dir / "test.md"
        content = """---
key: test
type: journalArticle
year: 2024
first_author: "[[Test]]"
local_pdf: "[[Lit-WS-PDFs/missing.pdf]]"
---
Test"""
        fm, body = extract_frontmatter(content)
        write_paper(paper, fm, body, validate=False)

        config.PAPERS_DIR = papers_dir
        config.PDFS_DIR = pdfs_dir

        missing = pdf_utils.find_missing_pdfs()

        assert len(missing) == 1
        assert missing[0]["paper"] == "test.md"
        assert "missing.pdf" in missing[0]["pdf"]
    finally:
        config.PAPERS_DIR = original_papers_dir
        config.PDFS_DIR = original_pdfs_dir


def test_find_missing_extracts(tmp_vault):
    """Test finding papers with missing extract files."""
    from lib import config
    from lib.yaml_utils import write_paper, extract_frontmatter

    original_papers_dir = config.PAPERS_DIR
    original_extracts_dir = config.PDF_EXTRACTS_DIR

    try:
        papers_dir = tmp_vault / "papers"
        extracts_dir = tmp_vault / "PDF Extracts"

        # Create a paper with extract link but no actual extract
        paper = papers_dir / "test.md"
        content = """---
key: test
type: journalArticle
year: 2024
first_author: "[[Test]]"
pdf_extract: "PDF Extracts/missing.md"
---
Test"""
        fm, body = extract_frontmatter(content)
        write_paper(paper, fm, body, validate=False)

        config.PAPERS_DIR = papers_dir
        config.PDF_EXTRACTS_DIR = extracts_dir

        missing = pdf_utils.find_missing_extracts()

        assert len(missing) == 1
        assert missing[0]["paper"] == "test.md"
        assert "missing.md" in missing[0]["extract"]
    finally:
        config.PAPERS_DIR = original_papers_dir
        config.PDF_EXTRACTS_DIR = original_extracts_dir
