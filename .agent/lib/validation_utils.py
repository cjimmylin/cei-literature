"""Comprehensive validation and integrity checks.

This module provides utilities for validating paper integrity,
checking classification consistency, finding duplicates,
and running comprehensive validation across all papers.
"""

import re
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from lib import config
from lib.yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter


@dataclass
class ValidationResult:
    """Result of validation check."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    info: List[str]


def validate_paper_integrity(filepath: Path) -> ValidationResult:
    """Comprehensive paper validation.

    Args:
        filepath: Path to the paper file to validate

    Returns:
        ValidationResult with detailed validation information
    """
    errors = []
    warnings = []
    info = []

    try:
        content = filepath.read_text()

        # Check frontmatter extraction
        try:
            fm, body = extract_frontmatter(content)
        except ValueError as e:
            errors.append(f"Frontmatter extraction failed: {e}")
            return ValidationResult(False, errors, warnings, info)

        # Validate YAML structure
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            errors.extend(issues)

        # Parse fields
        fields = parse_frontmatter(fm)

        # Check required fields
        required = ["key", "type", "year", "first_author"]
        for field in required:
            if field not in fields:
                errors.append(f"Missing required field: {field}")

        # Check field formats on the raw lines: parse_frontmatter strips
        # quotes, so its values can't tell "[[A]]" from [[A]].
        for field in ("first_author", "local_pdf"):
            if field in fields:
                m = re.search(rf"^{field}:[ \t]*(.*)$", fm, re.MULTILINE)
                raw = m.group(1).strip() if m else ""
                if not (raw.startswith('"[[') and raw.endswith(']]"')):
                    errors.append(f"{field} must be quoted wikilink")

        # Check newtags format
        if "newtags" in fields:
            if "\n" in fields["newtags"]:
                errors.append("newtags must be string, not list")

        # Info: Check enrichment
        if "key_contribution" in fields or "significance" in fields:
            info.append("Paper has enrichment fields")

    except Exception as e:
        errors.append(f"Validation exception: {e}")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        info=info
    )


def validate_classification_consistency(fields: Dict[str, str]) -> List[str]:
    """Check for inconsistent classification fields.

    Args:
        fields: Dictionary of paper frontmatter fields

    Returns:
        List of consistency issues found
    """
    issues = []

    # If ethics_overall=No, should have research_topic
    if fields.get("ethics_overall") == "No":
        if "research_topic" not in fields:
            issues.append("ethics_overall=No but missing research_topic")

    # If ethics_overall=Yes with no frameworks, should have ethics_perspective
    if fields.get("ethics_overall") == "Yes":
        has_framework = any([
            fields.get("virtue_ethics") == "Yes",
            fields.get("deontological_ethics") == "Yes",
            fields.get("utilitarian_ethics") == "Yes",
        ])
        if not has_framework and "ethics_perspective" not in fields:
            issues.append("ethics_overall=Yes but no framework or perspective")

    # If data fields set, description should exist
    has_data = any([
        fields.get("is_benchmark") == "Yes",
        fields.get("is_eval") == "Yes",
        fields.get("is_dataset") == "Yes",
    ])
    if has_data and "data_description" not in fields:
        issues.append("Data type set but missing data_description")

    return issues


def check_duplicate_papers() -> Dict[str, List[Path]]:
    """Find potential duplicate papers by DOI or title.

    Returns:
        Dictionary mapping DOIs to lists of duplicate paper files
    """
    duplicates = {}

    # Check by DOI
    doi_map = {}
    for paper in config.PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "DOI" in fields and fields["DOI"]:
            doi = fields["DOI"]
            if doi in doi_map:
                if doi not in duplicates:
                    duplicates[doi] = [doi_map[doi]]
                duplicates[doi].append(paper)
            else:
                doi_map[doi] = paper

    return duplicates


def validate_all_papers() -> Dict[str, any]:
    """Run validation on all papers, return summary.

    Returns:
        Dictionary with validation summary:
        - total: Total number of papers checked
        - valid: Number of valid papers
        - errors: Total number of errors found
        - warnings: Total number of warnings found
        - failed_papers: List of papers with errors
    """
    results = {
        "total": 0,
        "valid": 0,
        "errors": 0,
        "warnings": 0,
        "failed_papers": [],
    }

    for paper in config.PAPERS_DIR.glob("*.md"):
        results["total"] += 1

        result = validate_paper_integrity(paper)
        if result.is_valid:
            results["valid"] += 1
        else:
            results["errors"] += len(result.errors)
            results["failed_papers"].append({
                "file": paper.name,
                "errors": result.errors,
            })

        results["warnings"] += len(result.warnings)

    return results
