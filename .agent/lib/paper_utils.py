"""Paper file operations and bulk updates.

This module provides utilities for working with paper files in the vault,
including querying, filtering, updating, and gathering statistics.
"""

import re
from pathlib import Path
from typing import List, Dict
from lib import config
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


def get_all_papers() -> List[Path]:
    """Return all paper files in papers/ directory.

    Returns:
        List of Path objects for all .md files in papers directory, sorted by name.
    """
    return sorted(config.PAPERS_DIR.glob("*.md"))


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


# Plain YAML scalars that need no quotes: words, numbers, dates, simple paths/URLs.
_PLAIN_VALUE = re.compile(r"[A-Za-z0-9_.\-/]+(?: [A-Za-z0-9_.\-/()&,]+)*")


def _format_value(value: str, was_quoted: bool) -> str:
    """Return value as it should appear after 'field: ' on a single frontmatter line.

    Keeps double quotes if the old value had them; adds them (escaping \\ and ")
    whenever a plain scalar could be misread (wikilinks, ': ', ' #', leading symbols).
    """
    if value == "":
        return '""' if was_quoted else ""  # vault convention for empty: 'field: '
    if not was_quoted and _PLAIN_VALUE.fullmatch(value) and not value.startswith(("-", ".")):
        return value
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _frontmatter_span(text: str):
    """Return (start, end) of the frontmatter lines, between the two '---' markers."""
    if not text.startswith("---"):
        raise ValueError("no YAML frontmatter (file does not start with ---)")
    first_nl = text.find("\n")
    close = re.compile(r"^---[ \t]*\r?$", re.MULTILINE).search(text, first_nl + 1)
    if first_nl < 0 or not close:
        raise ValueError("no closing --- for the frontmatter")
    return first_nl + 1, close.start()


def _set_field(text: str, field: str, value: str) -> str:
    """Set one frontmatter field in text, changing only that field's line.

    Replaces the value on the field's existing line, or adds 'field: value' as the
    last frontmatter line if the field is absent. Every other line, the body and
    the line endings stay byte-for-byte the same.

    Raises ValueError (and changes nothing) when the edit would not be a clean
    single-line edit: a value with a line break, a field that appears more than
    once, or a field holding a block list or multi-line value.
    """
    if "\n" in value or "\r" in value:
        raise ValueError(f"{field}: value contains a line break")
    start, end = _frontmatter_span(text)
    fm = text[start:end]
    line_re = re.compile(rf"^{re.escape(field)}[ \t]*:(?P<val>[^\r\n]*)", re.MULTILINE)
    hits = list(line_re.finditer(fm))
    if len(hits) > 1:
        raise ValueError(f"{field}: appears {len(hits)} times in the frontmatter")
    if not hits:
        nl = "\r\n" if fm.endswith("\r\n") else "\n"
        if fm and not fm.endswith("\n"):
            fm += nl
        new_fm = fm + f"{field}: {_format_value(value, False)}{nl}"
        return text[:start] + new_fm + text[end:]
    m = hits[0]
    old = m.group("val").strip()
    rest = fm[m.end():].split("\n", 2)
    following = rest[1] if len(rest) > 1 else ""
    if following[:1] in (" ", "\t") or (old in ("", "|", ">", "|-", ">-") and following[:1] == "-"):
        raise ValueError(f"{field}: holds a block list or multi-line value; not a single-line edit")
    was_quoted = len(old) >= 2 and old[0] == old[-1] == '"'
    new_line = f"{field}: {_format_value(value, was_quoted)}"
    new_fm = fm[:m.start()] + new_line + fm[m.end():]
    return text[:start] + new_fm + text[end:]


def update_paper_field(filepath: Path, field: str, value: str) -> bool:
    """Set a single frontmatter field in a paper, editing only that field's line.

    The line is replaced in place (or appended at the end of the frontmatter if the
    field is missing); the rest of the file is left byte-for-byte as it was.

    Args:
        filepath: Path to the paper file
        field: The field name to update
        value: The new value (a scalar; quotes are added when YAML needs them)

    Returns:
        True if the file was updated (or already held the value), False otherwise
    """
    try:
        text = filepath.read_bytes().decode("utf-8")
        new_text = _set_field(text, field, value)
        if new_text != text:
            filepath.write_bytes(new_text.encode("utf-8"))
        return True
    except Exception as e:
        print(f"Failed to update {filepath.name}: {e}")
        return False


def batch_update_papers(papers: List[Path], updates: Dict[str, str]) -> Dict[str, int]:
    """Apply the same field values to many papers, one single-line edit per field.

    A paper is written only if every update applies cleanly; otherwise it is left
    untouched and counted as failed.

    Args:
        papers: List of paper files to update
        updates: Dictionary of field names to new values

    Returns:
        Dictionary with "success" and "failed" counts
    """
    results = {"success": 0, "failed": 0}

    for paper in papers:
        try:
            text = paper.read_bytes().decode("utf-8")
            new_text = text
            for field, value in updates.items():
                new_text = _set_field(new_text, field, value)
            if new_text != text:
                paper.write_bytes(new_text.encode("utf-8"))
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
