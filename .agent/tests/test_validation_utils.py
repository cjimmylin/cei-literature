"""Tests for lib.validation_utils."""

import pytest
from pathlib import Path
from lib import validation_utils
from lib.yaml_utils import write_paper, extract_frontmatter


def test_validation_result_dataclass():
    """Test ValidationResult dataclass."""
    result = validation_utils.ValidationResult(
        is_valid=True,
        errors=[],
        warnings=["test warning"],
        info=["test info"]
    )

    assert result.is_valid is True
    assert len(result.errors) == 0
    assert len(result.warnings) == 1
    assert len(result.info) == 1


def test_validate_paper_integrity_valid(tmp_vault, sample_paper_content):
    """Test validating a valid paper."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        papers_dir = tmp_vault / "papers"
        paper = papers_dir / "test.md"
        paper.write_text(sample_paper_content)

        config.PAPERS_DIR = papers_dir

        result = validation_utils.validate_paper_integrity(paper)

        assert result.is_valid is True
        assert len(result.errors) == 0
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_validate_paper_integrity_missing_required_field(tmp_vault):
    """Test validation catches missing required fields."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        papers_dir = tmp_vault / "papers"
        paper = papers_dir / "test.md"

        # Paper missing 'first_author' field
        content = """---
key: test
type: journalArticle
year: 2024
---
Test"""
        paper.write_text(content)

        config.PAPERS_DIR = papers_dir

        result = validation_utils.validate_paper_integrity(paper)

        assert result.is_valid is False
        assert any("first_author" in err for err in result.errors)
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_validate_paper_integrity_unquoted_wikilink(tmp_vault):
    """Test validation catches unquoted wikilinks."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        papers_dir = tmp_vault / "papers"
        paper = papers_dir / "test.md"

        # Unquoted wikilink
        content = """---
key: test
type: journalArticle
year: 2024
first_author: [[Unquoted]]
---
Test"""
        paper.write_text(content)

        config.PAPERS_DIR = papers_dir

        result = validation_utils.validate_paper_integrity(paper)

        assert result.is_valid is False
        assert any("quoted wikilink" in err for err in result.errors)
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_validate_classification_consistency_no_issues():
    """Test classification consistency with valid fields."""
    fields = {
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
    }

    issues = validation_utils.validate_classification_consistency(fields)
    assert len(issues) == 0


def test_validate_classification_consistency_missing_research_topic():
    """Test classification catches missing research_topic."""
    fields = {
        "ethics_overall": "No",
    }

    issues = validation_utils.validate_classification_consistency(fields)
    assert len(issues) > 0
    assert any("research_topic" in issue for issue in issues)


def test_validate_classification_consistency_missing_ethics_framework():
    """Test classification catches missing ethics framework/perspective."""
    fields = {
        "ethics_overall": "Yes",
        "virtue_ethics": "No",
        "deontological_ethics": "No",
        "utilitarian_ethics": "No",
    }

    issues = validation_utils.validate_classification_consistency(fields)
    assert len(issues) > 0
    assert any("framework" in issue or "perspective" in issue for issue in issues)


def test_validate_classification_consistency_missing_data_description():
    """Test classification catches missing data_description."""
    fields = {
        "is_benchmark": "Yes",
    }

    issues = validation_utils.validate_classification_consistency(fields)
    assert len(issues) > 0
    assert any("data_description" in issue for issue in issues)


def test_check_duplicate_papers(tmp_vault):
    """Test finding duplicate papers by DOI."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        papers_dir = tmp_vault / "papers"

        # Create two papers with same DOI
        for i in range(2):
            paper = papers_dir / f"test{i}.md"
            content = f"""---
key: test{i}
type: journalArticle
year: 2024
first_author: "[[Test]]"
DOI: "10.1234/duplicate"
---
Test"""
            fm, body = extract_frontmatter(content)
            write_paper(paper, fm, body, validate=False)

        config.PAPERS_DIR = papers_dir

        duplicates = validation_utils.check_duplicate_papers()

        assert "10.1234/duplicate" in duplicates
        assert len(duplicates["10.1234/duplicate"]) == 2
    finally:
        config.PAPERS_DIR = original_papers_dir


def test_validate_all_papers(tmp_vault, sample_paper_content):
    """Test validating all papers in vault."""
    from lib import config
    original_papers_dir = config.PAPERS_DIR

    try:
        papers_dir = tmp_vault / "papers"

        # Create mix of valid and invalid papers
        valid_paper = papers_dir / "valid.md"
        valid_paper.write_text(sample_paper_content)

        invalid_paper = papers_dir / "invalid.md"
        invalid_paper.write_text("---\nkey: bad\n---\nNo required fields")

        config.PAPERS_DIR = papers_dir

        results = validation_utils.validate_all_papers()

        assert results["total"] == 2
        assert results["valid"] == 1
        assert results["errors"] > 0
        assert len(results["failed_papers"]) == 1
    finally:
        config.PAPERS_DIR = original_papers_dir
