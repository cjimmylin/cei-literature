#!/usr/bin/env python3
"""
YAML Frontmatter Utilities for CEI Literature Vault

This module provides safe, validated functions for reading and writing YAML frontmatter
in paper markdown files. Use these functions in all scripts that modify paper metadata
to prevent YAML corruption.

KEY RULES:
1. Always use extract_frontmatter() to read YAML
2. Always use rebuild_frontmatter() to reconstruct YAML
3. Always use validate_frontmatter() before writing to file
4. Never write orphaned list items (e.g., "  - " without a parent key)
5. Never write incomplete closing markers (always "---\n")
6. Never mix list and scalar formats for the same key
"""

import re
from pathlib import Path
from typing import Tuple, Dict, List


# =============================================================================
# FRONTMATTER EXTRACTION & PARSING
# =============================================================================

def extract_frontmatter(content: str) -> Tuple[str, str]:
    """
    Extract YAML frontmatter from markdown content.

    Returns: (frontmatter_text, body_text)

    Handles both standard and malformed closing markers:
    - Standard: "---\nfrontmatter\n---\ncontent"
    - Attached: "---\nfrontmatter---\ncontent" (corrupted but recoverable)

    Raises: ValueError if no valid frontmatter found
    """
    if not content.startswith('---'):
        raise ValueError("Content does not start with YAML frontmatter marker (---)")

    # Try standard closing marker first
    match = re.search(r'\n---\s*\n', content[3:])
    if match:
        end_pos = match.start() + 3
        frontmatter = content[3:end_pos]
        body = content[end_pos + 5:]  # Skip \n---\n
        return frontmatter, body

    # Try attached closing marker (corrupted files)
    match = re.search(r'---\s*\n', content[3:])
    if match:
        end_pos = match.start() + 3
        frontmatter = content[3:end_pos]
        body = content[end_pos + 5:]  # Skip ---\n
        return frontmatter, body

    raise ValueError("Could not find valid YAML frontmatter closing marker")


def parse_frontmatter(frontmatter: str) -> Dict[str, str]:
    """
    Parse YAML frontmatter into a dictionary.

    Returns: Dict mapping field names to values (string values only)
    Note: Only handles simple key: value pairs, not complex nested structures
    """
    fields = {}
    lines = frontmatter.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines and list items (they're invalid orphaned items)
        if not line.strip() or line.strip().startswith('- '):
            i += 1
            continue

        # Look for key: value pattern
        if ':' in line and not line.startswith('  '):
            match = re.match(r'^([^:]+):\s*"?([^"\n]*)"?', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                fields[key] = value

        i += 1

    return fields


# =============================================================================
# FRONTMATTER VALIDATION
# =============================================================================

def validate_frontmatter(frontmatter: str) -> Tuple[bool, List[str]]:
    """
    Validate YAML frontmatter for common issues.

    Returns: (is_valid, list_of_issues)

    Checks for:
    - Orphaned list items (indented dashes without parent key)
    - Incomplete key-value pairs
    - Mismatched quotes
    - Hash prefixes in tags (should be removed)
    """
    issues = []
    lines = frontmatter.split('\n')

    for i, line in enumerate(lines):
        # Check for orphaned list items
        if line.startswith('  - ') and i > 0:
            # Look back to find parent key
            has_parent = False
            for j in range(i - 1, -1, -1):
                prev_line = lines[j].strip()
                if not prev_line:  # Skip empty lines
                    continue
                # Check if previous non-empty line is a proper parent (has ':' and isn't another list item)
                if ':' in prev_line and not prev_line.startswith('- '):
                    has_parent = True
                break

            if not has_parent:
                issues.append(f"Line {i+1}: Orphaned list item '  - ' without parent key")

        # Check for # prefixes in tags
        if line.startswith('  - #'):
            issues.append(f"Line {i+1}: Hash prefix found in tag: {line.strip()}")

        # Check for mismatched quotes
        if '"' in line and line.count('"') % 2 != 0:
            issues.append(f"Line {i+1}: Mismatched quotes: {line.strip()}")

    return len(issues) == 0, issues


# =============================================================================
# FRONTMATTER RECONSTRUCTION
# =============================================================================

def rebuild_frontmatter(fields: Dict[str, str], preserve_order: bool = False) -> str:
    """
    Rebuild YAML frontmatter from a dictionary of fields.

    Args:
        fields: Dictionary of key-value pairs
        preserve_order: If True, maintains the order of fields (Python 3.7+)

    Returns: YAML frontmatter string (without opening/closing ---)

    Rules:
    - All values are quoted as strings
    - No orphaned list items created
    - Proper YAML syntax guaranteed
    """
    lines = []

    for key, value in fields.items():
        # Skip empty keys
        if not key or not key.strip():
            continue

        # Quote the value if it contains special characters or is not already quoted
        if value is None:
            value = "N/A"
        else:
            value = str(value).strip()
            # Only quote if not already quoted and contains spaces or special chars
            if not (value.startswith('"') and value.endswith('"')):
                if ' ' in value or ':' in value or '"' in value:
                    value = value.replace('"', '\\"')  # Escape quotes
                    value = f'"{value}"'

        lines.append(f'{key}: {value}')

    return '\n'.join(lines)


def reconstruct_content(frontmatter: str, body: str) -> str:
    """
    Reconstruct full markdown content from frontmatter and body.

    CRITICAL: Ensures proper closing marker with newline.

    Returns: Full markdown content with proper YAML structure
    """
    # Ensure frontmatter doesn't have trailing newlines
    frontmatter = frontmatter.rstrip()

    # Reconstruct with proper spacing
    # Format: ---\nfrontmatter\n---\nbody
    return f"---\n{frontmatter}\n---\n{body}"


# =============================================================================
# SAFE FILE OPERATIONS
# =============================================================================

def read_paper(filepath: Path) -> Tuple[str, str]:
    """
    Safely read a paper file and extract frontmatter and body.

    Returns: (frontmatter, body)

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If YAML is malformed
    """
    if not filepath.exists():
        raise FileNotFoundError(f"Paper file not found: {filepath}")

    content = filepath.read_text(encoding='utf-8')
    return extract_frontmatter(content)


def write_paper(filepath: Path, frontmatter: str, body: str, validate: bool = True) -> bool:
    """
    Safely write a paper file with proper YAML structure.

    Args:
        filepath: Path to paper file
        frontmatter: YAML frontmatter string (without --- markers)
        body: Markdown body content
        validate: If True, validates frontmatter before writing

    Returns: True if successful, False otherwise

    Raises:
        ValueError: If validation fails and validate=True
    """
    # Validate before writing
    if validate:
        is_valid, issues = validate_frontmatter(frontmatter)
        if not is_valid:
            raise ValueError("Frontmatter validation failed:\n" + "\n".join(issues))

    # Reconstruct and write
    content = reconstruct_content(frontmatter, body)
    filepath.write_text(content, encoding='utf-8')
    return True


# =============================================================================
# COMMON OPERATIONS
# =============================================================================

def add_field(frontmatter: str, key: str, value: str, replace: bool = True) -> str:
    """
    Add or update a single field in frontmatter.

    Args:
        frontmatter: Current frontmatter string
        key: Field key (e.g., 'pdf_extract')
        value: Field value
        replace: If True, replaces existing field; if False, only adds if missing

    Returns: Updated frontmatter string

    LOSSY: rebuilds the whole frontmatter from parse_frontmatter(), which drops
    block lists and quotes and cuts values at an embedded quote. Do not use it
    to edit a note on disk; use paper_utils.update_paper_field (single-line edit).
    """
    fields = parse_frontmatter(frontmatter)

    if not replace and key in fields:
        return frontmatter

    fields[key] = value
    return rebuild_frontmatter(fields)


def remove_field(frontmatter: str, key: str) -> str:
    """Remove a field from frontmatter.

    LOSSY: rebuilds the whole frontmatter from parse_frontmatter(), which drops
    block lists and quotes and cuts values at an embedded quote. Do not use it
    to edit a note on disk; use paper_utils.update_paper_field (single-line edit).
    """
    fields = parse_frontmatter(frontmatter)
    fields.pop(key, None)
    return rebuild_frontmatter(fields)


def add_tags(frontmatter: str, new_tags: List[str], key: str = 'tags') -> str:
    """
    Add tags to frontmatter as a proper YAML list.

    Args:
        frontmatter: Current frontmatter string
        new_tags: List of tags to add
        key: Field key (default 'tags')

    Returns: Updated frontmatter string with proper tag formatting

    Important: Creates proper YAML list syntax, not orphaned items
    """
    lines = frontmatter.split('\n')
    new_lines = []
    skip_next_indent = False

    # Remove existing tags section
    i = 0
    while i < len(lines):
        line = lines[i]

        if skip_next_indent and line.startswith('  '):
            i += 1
            continue

        skip_next_indent = False

        if line.startswith(f'{key}:'):
            skip_next_indent = True
            i += 1
            continue

        new_lines.append(line)
        i += 1

    # Remove trailing blank lines
    while new_lines and not new_lines[-1].strip():
        new_lines.pop()

    # Add new tags section at the end
    if new_tags:
        new_lines.append(f'{key}:')
        for tag in new_tags:
            # Clean tag: remove # prefix if present, remove quotes
            clean_tag = tag.lstrip('#').strip('"\'')
            if clean_tag:
                new_lines.append(f'  - {clean_tag}')

    return '\n'.join(new_lines)


# =============================================================================
# MIGRATION & CLEANUP
# =============================================================================

def clean_orphaned_tags(frontmatter: str) -> Tuple[str, List[str]]:
    """
    Find and remove orphaned list items from frontmatter.

    Returns: (cleaned_frontmatter, extracted_tags)
    """
    lines = frontmatter.split('\n')
    cleaned_lines = []
    orphaned_tags = []
    in_proper_list = False

    for i, line in enumerate(lines):
        # Track if we're in a proper list section
        if line.startswith('tags:'):
            in_proper_list = True
            cleaned_lines.append(line)
            continue
        elif in_proper_list and line and not line.startswith('  '):
            in_proper_list = False

        # If it's a list item
        if line.startswith('  - '):
            if in_proper_list:
                # Part of proper tags section, keep it
                cleaned_lines.append(line)
            else:
                # Orphaned item, extract and remove
                tag = line[4:].strip().strip('"\'').lstrip('#').strip()
                if tag:
                    orphaned_tags.append(tag)
        else:
            cleaned_lines.append(line)

    # Remove trailing blank lines
    while cleaned_lines and not cleaned_lines[-1].strip():
        cleaned_lines.pop()

    return '\n'.join(cleaned_lines), orphaned_tags


# =============================================================================
# TESTING & DEBUG
# =============================================================================

def print_frontmatter_debug(filepath: Path):
    """Print debug information about a paper's frontmatter."""
    try:
        frontmatter, _ = read_paper(filepath)
        is_valid, issues = validate_frontmatter(frontmatter)

        print(f"\n=== {filepath.name} ===")
        print(f"Valid: {is_valid}")

        if issues:
            print(f"Issues ({len(issues)}):")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("No issues found")

        print(f"\nFrontmatter lines: {len(frontmatter.split(chr(10)))}")
        print(f"Parsed fields: {len(parse_frontmatter(frontmatter))}")

    except Exception as e:
        print(f"ERROR reading {filepath}: {e}")


if __name__ == "__main__":
    # Test on a sample paper
    import sys
    if len(sys.argv) > 1:
        paper_path = Path(sys.argv[1])
        print_frontmatter_debug(paper_path)
    else:
        print("Usage: python3 yaml_frontmatter_utils.py <paper_path>")
        print("Example: python3 yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md")
