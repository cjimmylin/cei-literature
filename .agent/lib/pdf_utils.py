"""PDF and extract validation utilities.

This module provides utilities for validating PDF links,
finding orphaned or missing PDFs, and checking extract file integrity.

PDF/extract files are organized in year-based subdirectories:
  PDFs/2024/2024-Author-Title.pdf
  PDF Extracts/2024/2024-Author-Title.md
"""

import re
from pathlib import Path
from typing import List, Dict
from lib.config import PDFS_DIR, PDF_EXTRACTS_DIR, PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


# ── Year-aware path helpers ────────────────────────────────────────────

def resolve_pdf_path(pdf_filename: str) -> Path:
    """Resolve a PDF filename to its year-based subdirectory path.

    Checks PDFs/YYYY/filename first, falls back to PDFs/filename.
    """
    year_match = re.match(r'^(\d{4})-', pdf_filename)
    if year_match:
        candidate = PDFS_DIR / year_match.group(1) / pdf_filename
        if candidate.exists():
            return candidate
    return PDFS_DIR / pdf_filename


def make_pdf_wikilink(pdf_filename: str) -> str:
    """Construct local_pdf YAML value with year subdirectory.

    Example: '"[[PDFs/2024/2024-Author-Title.pdf]]"'
    """
    year_match = re.match(r'^(\d{4})-', pdf_filename)
    if year_match:
        return f'"[[PDFs/{year_match.group(1)}/{pdf_filename}]]"'
    return f'"[[PDFs/{pdf_filename}]]"'


def make_extract_path(extract_filename: str) -> str:
    """Construct pdf_extract YAML value with year subdirectory.

    Example: '"PDF Extracts/2024/2024-Author-Title.md"'
    """
    year_match = re.match(r'^(\d{4})-', extract_filename)
    if year_match:
        return f'"PDF Extracts/{year_match.group(1)}/{extract_filename}"'
    return f'"PDF Extracts/{extract_filename}"'


def validate_pdf_link(local_pdf: str, paper_name: str) -> Dict[str, any]:
    """Validate PDF link from paper.

    Args:
        local_pdf: The local_pdf field value from paper frontmatter
        paper_name: Name of the paper (for error reporting)

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if link is valid
        - errors: List of error messages
        - path: Path object to PDF file if valid, None otherwise
    """
    result = {
        "valid": True,
        "errors": [],
        "path": None,
    }

    # Extract filename from wikilink: "[[PDFs/file.pdf]]"
    if not local_pdf:
        result["valid"] = False
        result["errors"].append("No PDF link")
        return result

    # Remove wikilink markers and quotes
    pdf_filename = local_pdf.strip('"').strip('[]').replace("PDFs/", "")
    pdf_path = PDFS_DIR / pdf_filename

    if not pdf_path.exists():
        result["valid"] = False
        result["errors"].append(f"PDF not found: {pdf_filename}")
    else:
        result["path"] = pdf_path

    return result


def validate_extract_link(pdf_extract: str, paper_name: str) -> Dict[str, any]:
    """Validate extract link from paper.

    Args:
        pdf_extract: The pdf_extract field value from paper frontmatter
        paper_name: Name of the paper (for error reporting)

    Returns:
        Dictionary with validation results:
        - valid: Boolean indicating if link is valid
        - errors: List of error messages
        - path: Path object to extract file if valid, None otherwise
    """
    result = {
        "valid": True,
        "errors": [],
        "path": None,
    }

    if not pdf_extract:
        result["valid"] = False
        result["errors"].append("No extract link")
        return result

    # Extract path
    extract_filename = pdf_extract.replace("PDF Extracts/", "")
    extract_path = PDF_EXTRACTS_DIR / extract_filename

    if not extract_path.exists():
        result["valid"] = False
        result["errors"].append(f"Extract not found: {extract_filename}")
    else:
        result["path"] = extract_path

    return result


def find_orphaned_pdfs() -> List[Path]:
    """Find PDFs not referenced by any paper.

    Searches all year subdirectories (PDFs/YYYY/*.pdf) and root.

    Returns:
        List of Path objects for orphaned PDF files
    """
    # Get all PDF files across year subdirectories
    all_pdf_paths = {f for f in PDFS_DIR.rglob("*.pdf") if f.is_file()}
    all_pdf_names = {f.name for f in all_pdf_paths}

    # Get referenced PDF basenames from papers
    referenced = set()
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "local_pdf" in fields:
            pdf = fields["local_pdf"].strip('"').strip('[]').replace("PDFs/", "")
            # After migration, pdf may be "2024/filename.pdf" — extract basename
            referenced.add(Path(pdf).name)

    # Find orphans by basename comparison
    orphaned_names = all_pdf_names - referenced
    return sorted(f for f in all_pdf_paths if f.name in orphaned_names)


def find_missing_pdfs() -> List[Dict[str, str]]:
    """Find papers with PDF links but missing PDF files.

    Returns:
        List of dictionaries with information about missing PDFs:
        - paper: Paper filename
        - pdf: PDF link from frontmatter
        - error: Error description
    """
    missing = []

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "local_pdf" in fields:
            result = validate_pdf_link(fields["local_pdf"], paper.stem)
            if not result["valid"]:
                missing.append({
                    "paper": paper.name,
                    "pdf": fields["local_pdf"],
                    "error": result["errors"][0],
                })

    return missing


def find_missing_extracts() -> List[Dict[str, str]]:
    """Find papers with extract links but missing extract files.

    Returns:
        List of dictionaries with information about missing extracts:
        - paper: Paper filename
        - extract: Extract link from frontmatter
        - error: Error description
    """
    missing = []

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "pdf_extract" in fields:
            result = validate_extract_link(fields["pdf_extract"], paper.stem)
            if not result["valid"]:
                missing.append({
                    "paper": paper.name,
                    "extract": fields["pdf_extract"],
                    "error": result["errors"][0],
                })

    return missing
