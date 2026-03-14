#!/usr/bin/env python3
"""
Add Newtags Script for CEI Literature Vault

This script generates a 'newtags' list for each paper based on:
- Ethical frameworks (Virtue, Deontological, Utilitarian)
- Ethics perspective
- Research topic
- Religious values
- National/Ethnic/Cultural values
- Moral psychology

See LLM_CONTEXT.md for aggregation logic.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent))
from ethics_scoring import is_ethics_yes, parse_ethics_value
from moral_psych_scoring import (
    MP_FIELDS, FIELD_DISPLAY_NAMES, is_mp_detected, parse_mp_value,
)
from religious_scoring import (
    RV_FIELDS,
    FIELD_DISPLAY_NAMES as RV_DISPLAY_NAMES,
    is_rv_detected,
    parse_rv_value,
)

from vault_config import PAPERS_DIR

# Import safe YAML utilities
from yaml_frontmatter_utils import (
    read_paper,
    write_paper,
    parse_frontmatter,
    validate_frontmatter
)


def get_frontmatter_value(fields: Dict[str, str], key: str) -> str:
    """Get value of a key from parsed frontmatter fields."""
    val = fields.get(key, '')
    # Remove quotes if present
    return val.strip('"\'') if val else ''


def to_hashtag(text: str) -> str:
    """Convert text to hashtag format (CamelCase, no spaces/special chars)."""
    if not text or text.lower() == 'n/a':
        return ''
    
    # Remove special characters but keep spaces for now
    clean_text = re.sub(r'[^\w\s]', '', text)
    
    # Capitalize words and join
    words = clean_text.split()
    hashtag = ''.join(word.capitalize() for word in words)
    
    return f'#{hashtag}'


def generate_tags(fields: Dict[str, str]) -> List[str]:
    """Generate list of tags based on parsed frontmatter fields."""
    tags = []

    # 1. Ethical Frameworks
    if is_ethics_yes(get_frontmatter_value(fields, 'virtue_ethics')):
        tags.append('#VirtueEthics')
    if is_ethics_yes(get_frontmatter_value(fields, 'deontological_ethics')):
        tags.append('#DeontologicalEthics')
    if is_ethics_yes(get_frontmatter_value(fields, 'utilitarian_ethics')):
        tags.append('#UtilitarianEthics')

    # 2. Ethics Perspective
    perspective = get_frontmatter_value(fields, 'ethics_perspective')
    if perspective and perspective != 'N/A':
        tags.append(to_hashtag(perspective))

    # 3. Research Topic
    topic = get_frontmatter_value(fields, 'research_topic')
    if topic and topic != 'N/A':
        tags.append(to_hashtag(topic))

    # 4. Religious Values — prefer rv_* scores, fall back to religious_values string
    rv_tags = []
    for rv_field in RV_FIELDS:
        if is_rv_detected(get_frontmatter_value(fields, rv_field)):
            rv_tags.append(to_hashtag(RV_DISPLAY_NAMES[rv_field]))
    if not rv_tags:
        # Fallback: read religious_values string (legacy)
        religion = get_frontmatter_value(fields, 'religious_values')
        if religion and religion != 'N/A':
            # Handle multiple values if separated by comma or slash
            parts = re.split(r'[,/]', religion)
            for part in parts:
                tag = to_hashtag(part.strip())
                if tag:
                    rv_tags.append(tag)
    tags.extend(rv_tags)

    # 5. National/Ethnic/Cultural
    culture = get_frontmatter_value(fields, 'national_ethnic_cultural')
    if culture and culture != 'N/A':
        parts = re.split(r'[,/]', culture)
        for part in parts:
            tag = to_hashtag(part.strip())
            if tag:
                tags.append(tag)

    # 6. Moral Psychology — prefer mp_* scores, fall back to moral_psychology string
    mp_tags = []
    for mp_field in MP_FIELDS:
        if is_mp_detected(get_frontmatter_value(fields, mp_field)):
            mp_tags.append(to_hashtag(FIELD_DISPLAY_NAMES[mp_field]))
    if not mp_tags:
        # Fallback: read moral_psychology string (legacy)
        psych = get_frontmatter_value(fields, 'moral_psychology')
        if psych and psych != 'N/A':
            parts = re.split(r'[,/]', psych)
            for part in parts:
                tag = to_hashtag(part.strip())
                if tag:
                    mp_tags.append(tag)
    tags.extend(mp_tags)

    return sorted(list(set(tags)))  # Deduplicate and sort


def update_frontmatter_with_tags(frontmatter: str, tags: List[str]) -> str:
    """Add or update newtags in frontmatter (as single-line comma-separated string).

    Uses safe YAML manipulation to avoid creating orphaned list items.
    """
    if not tags:
        return frontmatter

    lines = frontmatter.rstrip().split('\n')

    # Remove existing newtags if present (including any orphaned list items that might have been added)
    # Filter out lines starting with 'newtags:' and any subsequent indented list items
    skip_indented = False
    filtered_lines = []
    for line in lines:
        if line.strip().startswith('newtags:'):
            skip_indented = True
            continue
        elif skip_indented and line.startswith('  '):
            continue
        else:
            skip_indented = False
            filtered_lines.append(line)

    lines = filtered_lines

    # Format tags as comma-separated string (NOT as YAML list)
    # newtags should be a simple string value for compatibility with search tools
    # Remove # prefixes if present from hashtag format
    clean_tags = [tag.lstrip('#').strip() for tag in tags]
    tags_str = ', '.join(clean_tags)
    lines.append(f'newtags: "{tags_str}"')

    return '\n'.join(lines)


def process_paper(filepath: Path) -> bool:
    """Process a single paper file and add newtags using safe YAML utilities."""
    try:
        # Use safe YAML utilities to read the paper
        frontmatter, body = read_paper(filepath)

        # Parse frontmatter into fields dictionary
        fields = parse_frontmatter(frontmatter)
        if not fields:
            return False

        # Generate tags from parsed fields
        tags = generate_tags(fields)

        # Skip if no tags to add
        if not tags:
            return False

        # Update frontmatter with new tags
        new_frontmatter = update_frontmatter_with_tags(frontmatter, tags)

        # Validate before writing
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  Validation failed for {filepath.name}: {issues}")
            return False

        # Use safe YAML utilities to write the paper
        write_paper(filepath, new_frontmatter, body, validate=True)
        return True

    except ValueError as e:
        print(f"  YAML error processing {filepath.name}: {e}")
        return False
    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False


def main():
    """Main function to process all papers."""
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return

    paper_files = list(papers_dir.glob('*.md'))
    print(f"Found {len(paper_files)} paper files to process\n")

    processed_count = 0

    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 100 == 0:
            print(f"Processing paper {i}/{len(paper_files)}...")

        if process_paper(filepath):
            processed_count += 1

    print(f"\n{processed_count} papers updated with 'newtags'.")


if __name__ == '__main__':
    main()
