#!/usr/bin/env python3
"""
Author Name Validation Utilities
Validates and normalizes author names to prevent:
- Abbreviated names (e.g., "A. Smith")
- Single-letter/initial-only names
- Broken wikilink syntax
- Generic placeholders
- Invalid characters in filenames

Use these functions in all scripts that create author files or process author names.
"""

import re
from pathlib import Path
from typing import Tuple, List, Optional, Dict

from vault_config import AUTHORS_DIR

# Invalid patterns that should be rejected or flagged
INVALID_PATTERNS = {
    'single_letter': re.compile(r'^[A-Z]\.$'),
    'two_initials': re.compile(r'^[A-Z]\. [A-Z]\.$'),
    'three_initials': re.compile(r'^[A-Z]\. [A-Z]\. [A-Z]\.$'),
    'broken_wikilink': re.compile(r'\[\[|\]\]'),
    'et_al': re.compile(r'^et al\.?$', re.IGNORECASE),
    'generic': re.compile(r'^(Center|Institute|Group|Team|Consortium|Anonymous|Unknown)$', re.IGNORECASE),
    'invalid_filename_chars': re.compile(r'[<>:"/\\|?*]'),
}

# Warning patterns - not invalid but should be flagged for review
WARNING_PATTERNS = {
    'abbreviated': re.compile(r'^[A-Z]\.\s+\S'),  # "A. Smith"
    'very_short': re.compile(r'^\S{1,2}$'),  # One or two characters
    'all_caps': re.compile(r'^[A-Z]{2,}$'),  # "SMITH"
}


def validate_author_name(name: str) -> Tuple[bool, List[str], List[str]]:
    """
    Validate an author name for common issues.

    Returns:
        (is_valid, errors, warnings)
        - is_valid: True if the name can be used
        - errors: List of critical issues that make the name invalid
        - warnings: List of issues that should be reviewed
    """
    if not name or not name.strip():
        return False, ["Empty author name"], []

    name = name.strip()
    errors = []
    warnings = []

    # Check for invalid patterns
    for pattern_name, pattern in INVALID_PATTERNS.items():
        if pattern.search(name):
            errors.append(f"Invalid pattern: {pattern_name}")

    # Check for warning patterns
    for pattern_name, pattern in WARNING_PATTERNS.items():
        if pattern.search(name):
            warnings.append(f"Review needed: {pattern_name}")

    # Additional checks
    if len(name) < 2:
        errors.append("Name too short")

    if name.startswith('.') or name.endswith('.'):
        if not name.endswith('.') or len(name.split()) < 2:
            warnings.append("Name ends/starts with period")

    return len(errors) == 0, errors, warnings


def normalize_author_name(name: str) -> str:
    """
    Normalize an author name:
    - Strip whitespace
    - Fix common issues
    - Remove invalid characters for filenames
    """
    if not name:
        return ""

    name = name.strip()

    # Remove wikilink syntax if present
    name = re.sub(r'\[\[|\]\]', '', name)

    # Remove invalid filename characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)

    # Collapse multiple spaces
    name = re.sub(r'\s+', ' ', name)

    return name.strip()


def find_full_name_match(abbreviated: str) -> Optional[str]:
    """
    Search for a full name that matches an abbreviated name.
    E.g., "A. Smith" might match "Alice Smith" in the Authors directory.

    Returns the full name if found, None otherwise.
    """
    parts = abbreviated.split()
    if len(parts) < 2:
        return None

    # Extract initials and last name
    initials = []
    last_name_parts = []

    for part in parts:
        if re.match(r'^[A-Z]\.$', part):
            initials.append(part[0])
        else:
            last_name_parts.append(part)

    if not initials or not last_name_parts:
        return None

    last_name = ' '.join(last_name_parts)

    # Search existing author files
    for author_file in AUTHORS_DIR.glob('*.md'):
        full_name = author_file.stem
        full_parts = full_name.split()

        if len(full_parts) < 2:
            continue

        # Check if last name matches (case-insensitive)
        if not full_name.lower().endswith(last_name.lower()):
            continue

        # Extract initials from full name
        full_initials = [p[0] for p in full_parts[:-len(last_name_parts)]
                         if p and p[0].isupper()]

        if initials == full_initials:
            return full_name

    return None


def is_valid_author_filename(name: str) -> Tuple[bool, str]:
    """
    Check if a name is valid for use as an author filename.

    Returns:
        (is_valid, reason)
    """
    if not name:
        return False, "Empty name"

    # Check for invalid filename characters
    if INVALID_PATTERNS['invalid_filename_chars'].search(name):
        return False, "Contains invalid filename characters"

    # Check for wikilink syntax
    if '[[' in name or ']]' in name:
        return False, "Contains wikilink syntax"

    # Check minimum length
    if len(name) < 2:
        return False, "Name too short"

    return True, "Valid"


def validate_author_list(authors: List[str]) -> Dict:
    """
    Validate a list of author names.

    Returns a dict with:
        - valid: list of valid author names
        - invalid: list of (name, errors) tuples
        - warnings: list of (name, warnings) tuples
        - expanded: dict mapping abbreviated names to full names found
    """
    result = {
        'valid': [],
        'invalid': [],
        'warnings': [],
        'expanded': {}
    }

    for name in authors:
        is_valid, errors, warnings = validate_author_name(name)

        if not is_valid:
            result['invalid'].append((name, errors))

            # Try to find a full name match for abbreviated names
            if 'abbreviated' in str(errors) or any('abbreviated' in w for w in warnings):
                full_name = find_full_name_match(name)
                if full_name:
                    result['expanded'][name] = full_name
        else:
            result['valid'].append(name)

            if warnings:
                result['warnings'].append((name, warnings))

                # Also check for expansion if it's abbreviated
                if any('abbreviated' in w for w in warnings):
                    full_name = find_full_name_match(name)
                    if full_name:
                        result['expanded'][name] = full_name

    return result


def safe_create_author_file(name: str, content: str = None, dry_run: bool = False) -> Tuple[bool, str]:
    """
    Safely create an author file after validation.

    Returns:
        (success, message)
    """
    # Normalize the name
    normalized = normalize_author_name(name)

    # Validate
    is_valid, errors, warnings = validate_author_name(normalized)

    if not is_valid:
        return False, f"Invalid author name: {', '.join(errors)}"

    # Check filename validity
    filename_valid, filename_reason = is_valid_author_filename(normalized)
    if not filename_valid:
        return False, f"Invalid filename: {filename_reason}"

    # Check if file already exists
    author_file = AUTHORS_DIR / f"{normalized}.md"
    if author_file.exists():
        return False, "Author file already exists"

    if dry_run:
        return True, f"Would create: {author_file.name}"

    # Create default content if not provided
    if content is None:
        content = f"""---
name: "{normalized}"
affiliation: ""
research_interests: []
website: ""
google_scholar: ""
semantic_scholar: ""
---

# {normalized}

## Affiliation


## Research Interests


## Publications
(Auto-generated list of linked papers)
"""

    author_file.write_text(content, encoding='utf-8')
    return True, f"Created: {author_file.name}"


if __name__ == "__main__":
    # Test validation
    test_names = [
        "John Smith",
        "A. Smith",
        "J. K. Rowling",
        "C.",
        "et al.",
        "[[Unknown]]",
        "Center",
        "Chad]] [[Coleman",
        "Aníbal M. Astobiza",
    ]

    print("Author Name Validation Tests")
    print("=" * 50)

    for name in test_names:
        is_valid, errors, warnings = validate_author_name(name)
        status = "VALID" if is_valid else "INVALID"
        print(f"\n{name}: {status}")
        if errors:
            print(f"  Errors: {errors}")
        if warnings:
            print(f"  Warnings: {warnings}")

        # Try to find full name
        if not is_valid or warnings:
            full = find_full_name_match(name)
            if full:
                print(f"  -> Expands to: {full}")
