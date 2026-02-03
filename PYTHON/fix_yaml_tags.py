#!/usr/bin/env python3
"""
Fix YAML frontmatter tags in paper files.

Problem: Papers have orphaned list items after the pdf: field that break YAML parsing:
  pdf: "..."
    - "#AiSafetyAlignment"
  ethics_perspective: "..."

Solution: Convert to proper tags: section:
  pdf: "..."
  tags:
    - AiSafetyAlignment
    - OtherTag
  ethics_perspective: "..."

This script:
1. Finds all orphaned list items (indented dashes without a parent key)
2. Removes them from their orphaned location
3. Creates a proper tags: section with them
4. Removes the # prefix (Obsidian handles that)
"""

import re
from pathlib import Path
from typing import Tuple, List

def extract_frontmatter(content: str) -> Tuple[str, str, str]:
    """Extract frontmatter, content, and return as (frontmatter, content, rest)."""
    if not content.startswith('---'):
        return '', content, ''

    # Find the second --- that closes frontmatter
    # Handle both newline-separated and attached closing markers
    match = re.search(r'\n---\s*\n', content[3:])
    if not match:
        # Try to find attached closing marker (e.g., "...txt"---\n)
        match = re.search(r'---\s*\n', content[3:])
        if not match:
            return '', content, ''
        end_pos = match.start() + 3
        frontmatter = content[3:end_pos]
        rest = content[end_pos + 5:]  # Skip the closing --- and newline
    else:
        end_pos = match.start() + 3
        frontmatter = content[3:end_pos]
        rest = content[end_pos + 5:]  # Skip the closing --- and newline

    return frontmatter, content[:end_pos+4], rest

def has_orphaned_tags(frontmatter: str) -> bool:
    """Check if frontmatter has orphaned list items or dirty tags."""
    lines = frontmatter.split('\n')
    in_tags_section = False

    for i, line in enumerate(lines):
        # Track if we're in a proper tags: section
        if line.startswith('tags:'):
            in_tags_section = True
            continue
        elif in_tags_section and line and not line.startswith('  '):
            # End of tags section
            in_tags_section = False

        # Look for indented list items (both quoted and unquoted)
        if (line.startswith('  - ') or line.startswith('  - "')):
            # Check if tag has # prefix that needs cleaning
            if '#' in line:
                return True

            # If we're in a proper tags section, skip further checks
            if in_tags_section:
                continue

            # Check if previous non-empty line is a property (has ':' but isn't 'tags:')
            for j in range(i - 1, -1, -1):
                prev = lines[j].strip()
                if prev:
                    # If previous line has ':' and isn't a tags section, this is orphaned
                    if ':' in prev and not prev.startswith('- '):
                        return True
                    break
    return False

def extract_orphaned_tags(frontmatter: str) -> Tuple[str, List[str]]:
    """Extract orphaned list items and return cleaned frontmatter."""
    lines = frontmatter.split('\n')
    cleaned_lines = []
    tags = []
    in_tags_section = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect if we're in a proper tags: section
        if line.startswith('tags:'):
            in_tags_section = True
            cleaned_lines.append(line)
            i += 1
        elif in_tags_section and (line.startswith('  - ') or line.startswith('  - "')):
            # This is part of a proper tags section, keep it but clean it
            tag_content = line[4:].strip()  # Remove '  - '
            tag_content = tag_content.strip('"\'')  # Remove quotes first
            tag_content = tag_content.lstrip('#').strip()  # Remove # prefix
            if tag_content:
                cleaned_lines.append(f'  - {tag_content}')
            i += 1
        elif in_tags_section and line and not line.startswith('  '):
            # End of tags section
            in_tags_section = False
            cleaned_lines.append(line)
            i += 1
        elif not in_tags_section and (line.startswith('  - ') or line.startswith('  - "')):
            # This is an orphaned list item (not in tags section)
            tag_content = line[4:].strip()  # Remove '  - '
            tag_content = tag_content.strip('"\'')  # Remove quotes first
            tag_content = tag_content.lstrip('#').strip()  # Remove # prefix
            if tag_content:  # Only add non-empty tags
                tags.append(tag_content)
            i += 1
        else:
            cleaned_lines.append(line)
            i += 1

    cleaned_frontmatter = '\n'.join(cleaned_lines)
    return cleaned_frontmatter, tags

def add_tags_section(frontmatter: str, tags: List[str]) -> str:
    """Add proper tags: section to frontmatter."""
    if not tags:
        return frontmatter

    lines = frontmatter.split('\n')

    # Remove any existing "tags:" lines (duplicates from previous run)
    lines = [line for line in lines if line.strip() != 'tags:']

    # Remove blank lines at the end
    while lines and not lines[-1].strip():
        lines.pop()

    # Build tags section
    tag_lines = ['tags:']
    for tag in tags:
        tag_lines.append(f'  - {tag}')

    # Add tags section at the end
    result_lines = lines + tag_lines

    return '\n'.join(result_lines)

def fix_paper_file(filepath: Path) -> Tuple[bool, str]:
    """
    Fix a single paper file.
    Returns (was_changed, message)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return False, f"Error reading {filepath.name}: {e}"

    if not has_orphaned_tags(content):
        return False, f"No orphaned tags"

    # Extract frontmatter
    frontmatter, fm_with_dashes, rest = extract_frontmatter(content)

    if not frontmatter:
        return False, f"Could not extract frontmatter"

    # Extract and clean orphaned tags
    cleaned_fm, tags = extract_orphaned_tags(frontmatter)

    # Check if frontmatter changed (either tags were extracted or cleaned in-place)
    if cleaned_fm == frontmatter and not tags:
        return False, f"No changes needed"

    # Add proper tags section (only if we have tags to add)
    if tags:
        fixed_fm = add_tags_section(cleaned_fm, tags)
    else:
        fixed_fm = cleaned_fm

    # Remove leading blank lines from frontmatter
    fm_lines = fixed_fm.split('\n')
    while fm_lines and not fm_lines[0].strip():
        fm_lines.pop(0)
    fixed_fm = '\n'.join(fm_lines)

    # Reconstruct content - ensure clean separation
    new_content = '---\n' + fixed_fm + '\n---\n' + rest

    # Write back
    try:
        filepath.write_text(new_content, encoding='utf-8')
        tag_count = len(tags) if tags else len([l for l in frontmatter.split('\n') if '  - ' in l and '#' in l])
        return True, f"Fixed {filepath.name}: {tag_count} tags cleaned"
    except Exception as e:
        return False, f"Error writing {filepath.name}: {e}"

def main():
    papers_dir = Path('./papers')
    if not papers_dir.exists():
        print("ERROR: papers/ directory not found")
        return

    paper_files = list(papers_dir.glob('*.md'))
    print(f"Found {len(paper_files)} paper files")
    print("=" * 60)

    fixed_count = 0
    skipped_count = 0
    error_count = 0

    for filepath in sorted(paper_files):
        was_changed, message = fix_paper_file(filepath)

        if was_changed:
            print(f"✓ {message}")
            fixed_count += 1
        elif "Error" in message:
            print(f"✗ {message}")
            error_count += 1
        else:
            skipped_count += 1

    print("=" * 60)
    print(f"\nSummary:")
    print(f"  Fixed:   {fixed_count} papers")
    print(f"  Skipped: {skipped_count} papers (no orphaned tags)")
    print(f"  Errors:  {error_count} papers")
    print(f"  Total:   {len(paper_files)} papers")

if __name__ == "__main__":
    main()
