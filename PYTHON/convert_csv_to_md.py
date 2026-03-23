#!/usr/bin/env python3
"""Convert Zotero CSV export to individual markdown files for Obsidian.

IMPORTANT: This script creates new paper files from Zotero export.
It includes validation to prevent common YAML issues discovered in Session 8:
- Wikilinks must be quoted: local_pdf: "[[Lit-WS-PDFs/file.pdf]]"
- Abstract truncation detection
- Proper YAML structure validation
"""

import csv
import re
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from yaml_frontmatter_utils import validate_frontmatter
from vault_config import PAPERS_DIR, WORKSPACE_ROOT


def quote_wikilink(value: str) -> str:
    """Ensure wikilinks are properly quoted for YAML.

    [[...]] syntax must be quoted or YAML interprets it as a flow sequence.
    """
    if not value:
        return value
    # If it contains wikilink syntax and isn't already quoted
    if '[[' in value and ']]' in value:
        if not (value.startswith('"') and value.endswith('"')):
            return f'"{value}"'
    return value


def check_abstract_truncation(abstract: str) -> bool:
    """Check if abstract appears truncated mid-word.

    Returns True if abstract looks truncated (potential issue to warn about).
    """
    if not abstract:
        return False
    abstract = abstract.rstrip()
    # Check if ends with lowercase letters (mid-word) and no period
    if re.search(r'[a-z]{2,}$', abstract) and not abstract.endswith('.'):
        return True
    return False


def sanitize_filename(title: str, key: str) -> str:
    """Create a safe filename from the paper title."""
    if not title:
        return f"paper_{key}"
    # Remove or replace problematic characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized = re.sub(r'\s+', ' ', sanitized).strip()
    # Truncate to reasonable length
    if len(sanitized) > 100:
        sanitized = sanitized[:100].rsplit(' ', 1)[0]
    return sanitized or f"paper_{key}"

def format_authors(authors: str) -> str:
    """Format author string for display."""
    if not authors:
        return ""
    return authors

def create_markdown(row: dict) -> tuple:
    """Create markdown content for a paper.

    Returns: (content, warnings) where warnings is a list of potential issues.
    """
    lines = []
    warnings = []

    # YAML frontmatter
    lines.append("---")
    lines.append(f"key: {row.get('Key', '')}")
    lines.append(f"type: {row.get('Item Type', '')}")

    year = row.get('Publication Year', '')
    if year:
        lines.append(f"year: {year}")

    # Handle authors - escape quotes in YAML
    authors = row.get('Author', '')
    if authors:
        authors_escaped = authors.replace('"', '\\"')
        lines.append(f'authors: "{authors_escaped}"')

    doi = row.get('DOI', '')
    if doi:
        lines.append(f"doi: {doi}")

    # Tags
    manual_tags = row.get('Manual Tags', '')
    auto_tags = row.get('Automatic Tags', '')
    all_tags = []
    if manual_tags:
        all_tags.extend([t.strip() for t in manual_tags.split(';') if t.strip()])
    if auto_tags:
        all_tags.extend([t.strip() for t in auto_tags.split(';') if t.strip()])
    if all_tags:
        # Format tags for YAML
        lines.append("tags:")
        for tag in all_tags[:20]:  # Limit to 20 tags
            tag_clean = tag.replace('"', '').replace(':', '-')
            lines.append(f"  - \"{tag_clean}\"")

    lines.append("---")
    lines.append("")

    # Title
    title = row.get('Title', 'Untitled')
    lines.append(f"# {title}")
    lines.append("")

    # Metadata section
    lines.append("## Metadata")
    lines.append("")

    if authors:
        lines.append(f"**Authors:** {authors}")
        lines.append("")

    if year:
        lines.append(f"**Year:** {year}")
        lines.append("")

    pub_title = row.get('Publication Title', '')
    if pub_title:
        lines.append(f"**Publication:** {pub_title}")
        lines.append("")

    item_type = row.get('Item Type', '')
    if item_type:
        lines.append(f"**Type:** {item_type}")
        lines.append("")

    if doi:
        lines.append(f"**DOI:** [{doi}](https://doi.org/{doi})")
        lines.append("")

    url = row.get('Url', '')
    if url and url != f"https://doi.org/{doi}":
        lines.append(f"**URL:** {url}")
        lines.append("")

    pages = row.get('Pages', '')
    if pages:
        lines.append(f"**Pages:** {pages}")
        lines.append("")

    volume = row.get('Volume', '')
    issue = row.get('Issue', '')
    if volume or issue:
        vol_issue = []
        if volume:
            vol_issue.append(f"Vol. {volume}")
        if issue:
            vol_issue.append(f"Issue {issue}")
        lines.append(f"**Volume/Issue:** {', '.join(vol_issue)}")
        lines.append("")

    publisher = row.get('Publisher', '')
    if publisher:
        lines.append(f"**Publisher:** {publisher}")
        lines.append("")

    # Abstract - with truncation check
    abstract = row.get('Abstract Note', '')
    if abstract:
        lines.append("## Abstract")
        lines.append("")
        lines.append(abstract)
        lines.append("")
        # Check for potential truncation
        if check_abstract_truncation(abstract):
            warnings.append(f"Abstract may be truncated (ends with: ...{abstract[-30:]})")

    # Notes section (for user annotations)
    lines.append("## Notes")
    lines.append("")
    lines.append("")

    # Tags display
    if all_tags:
        lines.append("## Tags")
        lines.append("")
        tag_links = [f"#{tag.replace(' ', '-').replace(':', '-')}" for tag in all_tags[:20]]
        lines.append(" ".join(tag_links))
        lines.append("")

    # Citation info from Extra field
    extra = row.get('Extra', '')
    if extra and 'citations' in extra.lower():
        lines.append("## Citation Info")
        lines.append("")
        lines.append(extra)
        lines.append("")

    content = '\n'.join(lines)

    # Validate the generated frontmatter
    try:
        # Extract just the frontmatter part for validation
        fm_start = content.index('---') + 3
        fm_end = content.index('---', fm_start)
        frontmatter = content[fm_start:fm_end].strip()
        is_valid, issues = validate_frontmatter(frontmatter)
        if not is_valid:
            warnings.extend([f"YAML issue: {issue}" for issue in issues])
    except Exception as e:
        warnings.append(f"Frontmatter validation error: {e}")

    return content, warnings

def main():
    csv_path = WORKSPACE_ROOT / "Base.md"
    output_dir = PAPERS_DIR

    output_dir.mkdir(exist_ok=True)

    # Read CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Found {len(rows)} papers")

    created = 0
    errors = 0
    all_warnings = []

    for row in rows:
        key = row.get('Key', '')
        title = row.get('Title', '')

        if not key:
            continue

        try:
            filename = sanitize_filename(title, key)
            filepath = output_dir / f"{filename}.md"

            # Handle duplicate filenames
            counter = 1
            original_filepath = filepath
            while filepath.exists():
                filepath = output_dir / f"{filename} ({counter}).md"
                counter += 1

            content, warnings = create_markdown(row)

            # Track any warnings for this paper
            if warnings:
                all_warnings.append({
                    'file': filepath.name,
                    'key': key,
                    'warnings': warnings
                })

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            created += 1

        except Exception as e:
            print(f"Error processing {key}: {e}")
            errors += 1

    print(f"Created {created} markdown files")
    if errors:
        print(f"Errors: {errors}")

    # Report warnings for manual review
    if all_warnings:
        print(f"\n⚠️  {len(all_warnings)} papers have potential issues requiring review:")
        for item in all_warnings:
            print(f"\n  {item['file']}:")
            for w in item['warnings']:
                print(f"    - {w}")
        print("\nRun 'python3 PYTHON/validate_papers_enhanced.py' after import for full validation.")

if __name__ == "__main__":
    main()
