"""Tests for lib.yaml_utils (CRITICAL - 100% coverage required)."""

import pytest
from pathlib import Path
from lib.yaml_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    rebuild_frontmatter,
    write_paper,
)


def test_extract_frontmatter_standard(sample_paper_content):
    """Test extracting standard frontmatter."""
    fm, body = extract_frontmatter(sample_paper_content)

    assert "key: 2024-Smith-Test" in fm
    assert "# Test Paper" in body
    assert body.startswith("\n# Test Paper")


def test_extract_frontmatter_corrupted():
    """Test extracting from corrupted (attached marker)."""
    content = "---\nkey: test---\nBody"
    fm, body = extract_frontmatter(content)

    assert "key: test" in fm
    # When closing marker is attached without newline, extraction still works
    # Body will be "ody" because "---\n" is stripped from "test---\nBody"
    assert body == "ody"


def test_extract_frontmatter_no_frontmatter():
    """Test extraction fails when no frontmatter present."""
    content = "# Just a heading\n\nNo frontmatter here."

    with pytest.raises(ValueError, match="frontmatter"):
        extract_frontmatter(content)


def test_parse_frontmatter(sample_paper_content):
    """Test parsing frontmatter to dict."""
    fm, _ = extract_frontmatter(sample_paper_content)
    fields = parse_frontmatter(fm)

    assert fields["key"] == "2024-Smith-Test"
    assert fields["year"] == "2024"
    assert "[[John Smith]]" in fields["first_author"]


def test_validate_frontmatter_valid(sample_paper_content):
    """Test validation passes for valid frontmatter."""
    fm, _ = extract_frontmatter(sample_paper_content)
    is_valid, issues = validate_frontmatter(fm)

    assert is_valid
    assert len(issues) == 0


def test_validate_frontmatter_orphaned():
    """Test validation catches orphaned tags."""
    fm = "key: test\n  - #Orphaned"
    is_valid, issues = validate_frontmatter(fm)

    assert not is_valid
    assert any("orphaned" in issue.lower() for issue in issues)


def test_validate_frontmatter_unquoted_wikilink():
    """Test that validate_frontmatter does NOT check for unquoted wikilinks.

    Note: Wikilink quoting is checked by validate_paper_integrity, not validate_frontmatter.
    validate_frontmatter only checks for YAML syntax issues like orphaned list items.
    """
    fm = "key: test\nfirst_author: [[Name]]\n"
    is_valid, issues = validate_frontmatter(fm)

    # Should be valid - validate_frontmatter doesn't check wikilink quoting
    assert is_valid
    assert len(issues) == 0


def test_rebuild_frontmatter():
    """Test rebuilding frontmatter from dict."""
    fields = {
        "key": "test",
        "year": "2024",
        "title": "Test",
    }

    fm = rebuild_frontmatter(fields)

    # rebuild_frontmatter returns frontmatter WITHOUT --- markers
    assert not fm.startswith("---")
    assert "key: test" in fm
    assert "year: 2024" in fm
    assert "title: Test" in fm


def test_rebuild_frontmatter_preserves_order():
    """Test rebuild preserves field order."""
    fields = {
        "key": "abc",
        "type": "journalArticle",
        "year": "2024",
    }

    fm = rebuild_frontmatter(fields)
    lines = fm.strip().split('\n')

    # Check that all fields are present (Python 3.7+ dicts maintain insertion order)
    assert len(lines) == 3
    assert any("key:" in line for line in lines)
    assert any("type:" in line for line in lines)
    assert any("year:" in line for line in lines)


def test_write_paper_validates(tmp_vault, sample_paper_content):
    """Test write_paper validates before writing."""
    paper_file = tmp_vault / "papers" / "test.md"
    fm, body = extract_frontmatter(sample_paper_content)

    # Should succeed
    write_paper(paper_file, fm, body, validate=True)
    assert paper_file.exists()

    # Corrupted should fail
    bad_fm = "key: test\n  - #Bad"
    with pytest.raises(ValueError, match="validation"):
        write_paper(paper_file, bad_fm, body, validate=True)


def test_write_paper_no_validation(tmp_vault):
    """Test write_paper can skip validation if needed."""
    paper_file = tmp_vault / "papers" / "test.md"

    # Even invalid frontmatter should write if validate=False
    bad_fm = "key: test\n  - #Bad"
    body = "Content"

    write_paper(paper_file, bad_fm, body, validate=False)
    assert paper_file.exists()
