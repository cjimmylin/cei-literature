"""Pytest fixtures for library tests."""

import pytest
from pathlib import Path
import tempfile
import shutil


@pytest.fixture
def sample_paper_content():
    """Minimal valid paper for testing."""
    return """---
key: 2024-Smith-Test
type: journalArticle
year: 2024
first_author: "[[John Smith]]"
title: "Test Paper"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
newtags: "AI Safety"
---

# Test Paper

## Abstract
This is a test abstract.
"""


@pytest.fixture
def corrupted_paper_content():
    """Paper with YAML corruption for testing."""
    return """---
key: 2024-Bad-Test
type: journalArticle
  - "#OrphanedTag"
year: 2024
first_author: [[Not Quoted]]
---

# Bad Paper
"""


@pytest.fixture
def tmp_vault(tmp_path):
    """Create temporary vault structure for testing."""
    vault = tmp_path / "test-vault"
    vault.mkdir()

    (vault / "papers").mkdir()
    (vault / "Authors").mkdir()
    (vault / "PDFs").mkdir()
    (vault / "PDF Extracts").mkdir()

    # Create config
    config = vault / ".vault-config.json"
    config.write_text('{"pdf_path": "' + str(vault / "PDFs") + '"}')

    return vault


@pytest.fixture
def sample_papers(tmp_vault, sample_paper_content):
    """Create sample papers in tmp vault."""
    papers_dir = tmp_vault / "papers"

    # Create 3 test papers
    for i in range(3):
        paper = papers_dir / f"2024-Author{i}-Test.md"
        content = sample_paper_content.replace("Smith", f"Author{i}")
        paper.write_text(content)

    return papers_dir


@pytest.fixture
def sample_author_profile():
    """Sample author profile content."""
    return """# John Smith

**Institution:** Stanford University

## Research Interests
- AI Ethics
- Machine Learning

enriched: true
"""


@pytest.fixture
def sample_authors(tmp_vault, sample_author_profile):
    """Create sample author profiles in tmp vault."""
    authors_dir = tmp_vault / "Authors"

    # Create 3 test authors
    for i in range(3):
        author = authors_dir / f"Author{i}.md"
        content = sample_author_profile.replace("John Smith", f"Author{i}")
        author.write_text(content)

    return authors_dir
