"""Tests for lib.paper_utils."""

import pytest
from pathlib import Path
from lib import paper_utils
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


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

        # Verify updates (check parsed values; rebuild_frontmatter leaves
        # single-word values unquoted)
        for paper in papers:
            fm, _ = extract_frontmatter(paper.read_text())
            fields = parse_frontmatter(fm)
            assert fields["year"] == "2025"
            assert fields["ethics_overall"] == "No"
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


# --- Single-line edits (2026-10-19): update functions must not rewrite other lines ---

RICH_NOTE = (
    "---\n"
    "key: 2024-Lee-Rich\n"
    'title: "A \\"quoted\\" title: with colon"\n'
    "year: 2024\n"
    'first_author: "[[Ann Lee]]"\n'
    "tags:\n"
    "  - ethics\n"
    "  - benchmark\n"
    "abstract: >-\n"
    "  Folded text\n"
    "  over two lines.\n"
    "ethics_overall: 80\n"
    "---\n"
    "\n"
    "# Body stays as is: ---\n"
)


def _rich(tmp_path):
    p = tmp_path / "2024-Lee-Rich.md"
    p.write_bytes(RICH_NOTE.encode("utf-8"))
    return p


def test_update_changes_only_target_line(tmp_path):
    p = _rich(tmp_path)
    assert paper_utils.update_paper_field(p, "ethics_overall", "0") is True
    assert p.read_text() == RICH_NOTE.replace("ethics_overall: 80", "ethics_overall: 0")


def test_update_appends_missing_field_and_quotes_when_needed(tmp_path):
    p = _rich(tmp_path)
    assert paper_utils.update_paper_field(p, "last_author", "[[Bo Kim]]") is True
    assert p.read_text() == RICH_NOTE.replace(
        "ethics_overall: 80\n---", 'ethics_overall: 80\nlast_author: "[[Bo Kim]]"\n---'
    )


def test_update_keeps_existing_quotes_and_escapes(tmp_path):
    p = _rich(tmp_path)
    assert paper_utils.update_paper_field(p, "first_author", "Ann Lee") is True
    assert 'first_author: "Ann Lee"\n' in p.read_text()
    assert paper_utils.update_paper_field(p, "title", 'Say "hi": now') is True
    assert 'title: "Say \\"hi\\": now"\n' in p.read_text()


def test_update_refuses_block_values_and_duplicates(tmp_path):
    p = _rich(tmp_path)
    for field in ("tags", "abstract"):
        assert paper_utils.update_paper_field(p, field, "x") is False
    assert paper_utils.update_paper_field(p, "year", "a\nb") is False
    assert p.read_text() == RICH_NOTE
    dup = tmp_path / "dup.md"
    dup.write_text("---\nyear: 2024\nyear: 2025\n---\nbody\n")
    assert paper_utils.update_paper_field(dup, "year", "2026") is False
    assert dup.read_text() == "---\nyear: 2024\nyear: 2025\n---\nbody\n"


def test_batch_update_is_all_or_nothing_per_paper(tmp_path):
    p = _rich(tmp_path)
    results = paper_utils.batch_update_papers([p], {"year": "2025", "tags": "x"})
    assert results == {"success": 0, "failed": 1}
    assert p.read_text() == RICH_NOTE


def test_update_preserves_crlf(tmp_path):
    p = tmp_path / "crlf.md"
    p.write_bytes(b"---\r\nyear: 2024\r\nkey: k\r\n---\r\nbody\r\n")
    assert paper_utils.update_paper_field(p, "year", "2025") is True
    assert paper_utils.update_paper_field(p, "url", "https://x.org/a") is True
    assert p.read_bytes() == b'---\r\nyear: 2025\r\nkey: k\r\nurl: "https://x.org/a"\r\n---\r\nbody\r\n'


def test_update_empty_value_follows_vault_convention(tmp_path):
    p = _rich(tmp_path)
    assert paper_utils.update_paper_field(p, "year", "") is True
    assert paper_utils.update_paper_field(p, "first_author", "") is True
    text = p.read_text()
    assert "\nyear: \n" in text and '\nfirst_author: ""\n' in text
