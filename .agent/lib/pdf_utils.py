"""PDF and extract validation utilities.

This module provides utilities for validating PDF links,
finding orphaned or missing PDFs, and checking extract file integrity.
"""

from pathlib import Path
from typing import List, Dict
from lib.config import PDFS_DIR, PDF_EXTRACTS_DIR, PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter


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

    Returns:
        List of Path objects for orphaned PDF files
    """
    # Get all PDF files
    all_pdfs = {f.name for f in PDFS_DIR.glob("*.pdf")}

    # Get referenced PDFs from papers
    referenced = set()
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "local_pdf" in fields:
            pdf = fields["local_pdf"].strip('"').strip('[]').replace("PDFs/", "")
            referenced.add(pdf)

    # Find orphans
    orphaned = all_pdfs - referenced
    return [PDFS_DIR / pdf for pdf in orphaned]


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
