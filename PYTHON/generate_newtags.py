#!/usr/bin/env python3
"""
Generate 'newtags' property for papers by aggregating all ethical/cultural/religious/psychological features.

LEARNINGS / DESIGN DECISIONS:
- Aggregation Source: We pull from all classified fields (Cultural, Religious, Psych, Ethics).
- Null Handling: 'N/A', 'Unknown', 'None' are filtered out to keep the tag list clean.
- Format: Tags are stored as a simple comma-separated string for compatibility with simple search tools.
- Supersedes `add_newtags.py`: This script is the source of truth for the `newtags` field.
"""

import re
import sys
from pathlib import Path
from typing import Tuple, List, Dict

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

PAPERS_DIR = Path(__file__).parent / "papers"

def extract_frontmatter_and_content(text: str) -> Tuple[Dict[str, str], str, str]:
    """
    Extract YAML frontmatter as a dictionary and remaining content.
    Returns (frontmatter_dict, raw_frontmatter_str, content_body)
    """
    if not text.startswith("---"):
        return {}, "", text
    
    # Find the closing ---
    end_match = re.search(r'\n---\s*\n', text[3:])
    if not end_match:
        return {}, "", text
    
    end_pos = end_match.end() + 3
    raw_frontmatter = text[4:end_pos-4].strip()
    content = text[end_pos:]
    
    # Parse frontmatter into dict
    frontmatter_dict = {}
    for line in raw_frontmatter.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            # Remove quotes and whitespace
            val = val.strip().strip('"').strip("'")
            frontmatter_dict[key] = val
            
    return frontmatter_dict, raw_frontmatter, content

def generate_tags(fm: Dict[str, str]) -> List[str]:
    """Generate list of tags based on frontmatter fields."""
    tags = []
    
    # 1. National/Ethnic/Cultural
    val = fm.get('national_ethnic_cultural', 'N/A')
    if val and val not in ['N/A', 'Unknown', 'None']:
        for v in val.split(','):
            v = v.strip()
            if v: tags.append(v)
            
    # 2. Religious Values — prefer rv_* scores, fall back to religious_values string
    rv_tags = []
    for rv_field in RV_FIELDS:
        if is_rv_detected(fm.get(rv_field)):
            rv_tags.append(RV_DISPLAY_NAMES[rv_field])
    if not rv_tags:
        # Fallback: read religious_values string (legacy)
        val = fm.get('religious_values', 'N/A')
        if val and val not in ['N/A', 'Unknown', 'None']:
            for v in val.split(','):
                v = v.strip()
                if v: rv_tags.append(v)
    tags.extend(rv_tags)
            
    # 3. Moral Psychology — prefer mp_* scores, fall back to moral_psychology string
    mp_tags = []
    for mp_field in MP_FIELDS:
        if is_mp_detected(fm.get(mp_field)):
            mp_tags.append(FIELD_DISPLAY_NAMES[mp_field])
    if not mp_tags:
        # Fallback: read moral_psychology string (legacy)
        val = fm.get('moral_psychology', 'N/A')
        if val and val not in ['N/A', 'Unknown', 'None']:
            for v in val.split(','):
                v = v.strip()
                if v: mp_tags.append(v)
    tags.extend(mp_tags)
            
    # 4. Ethical Frameworks
    if is_ethics_yes(fm.get('virtue_ethics')):
        tags.append("Virtue Ethics")
    if is_ethics_yes(fm.get('deontological_ethics')):
        tags.append("Deontology")
    if is_ethics_yes(fm.get('utilitarian_ethics')):
        tags.append("Utilitarianism")
    if is_ethics_yes(fm.get('care_ethics')):
        tags.append("Care Ethics")
    if is_ethics_yes(fm.get('contractarian_ethics')):
        tags.append("Contractarianism")

    # 5. Ethics Perspective (if exists)
    val = fm.get('ethics_perspective', '')
    if val and val not in ['N/A', 'Unknown', 'None']:
        tags.append(val)
        
    # Deduplicate while preserving order
    seen = set()
    unique_tags = []
    for t in tags:
        if t and t not in seen:
            seen.add(t)
            unique_tags.append(t)
            
    return unique_tags

def update_frontmatter(raw_frontmatter: str, newtags: str) -> str:
    """Add or update newtags in frontmatter string."""
    lines = raw_frontmatter.split('\n')
    new_lines = []
    
    # Remove existing newtags
    skip_next = False
    for line in lines:
        if skip_next and line.startswith('  '):
            continue
        skip_next = False
        
        if line.startswith('newtags:'):
            continue
        # Skip standalone dashes that might have been added erroneously
        if line.strip() == '-':
            continue
        new_lines.append(line)
    
    # Add newtags at the end
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()
    
    new_lines.append(f'newtags: "{newtags}"')
    
    return '\n'.join(new_lines)

def process_paper(filepath: Path) -> Tuple[str, str]:
    """Process a single paper file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fm_dict, raw_fm, body = extract_frontmatter_and_content(content)
    
    tags = generate_tags(fm_dict)
    newtags_str = ", ".join(tags)
    
    # Update the file
    new_fm = update_frontmatter(raw_fm, newtags_str)
    new_content = f"---\n{new_fm}\n---\n{body}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return filepath.name, newtags_str

def main():
    """Process all papers."""
    papers = list(PAPERS_DIR.glob("*.md"))
    print(f"Found {len(papers)} papers to process\n")
    
    count_tagged = 0
    
    for paper in sorted(papers):
        try:
            name, newtags = process_paper(paper)
            if newtags:
                count_tagged += 1
                # Print first few for verification
                if count_tagged <= 10:
                    print(f"{name}:\n  newtags: {newtags}")
        except Exception as e:
            print(f"Error processing {paper.name}: {e}")
            
    print(f"\nTotal papers processed: {len(papers)}")
    print(f"Papers with at least one tag: {count_tagged}")

if __name__ == "__main__":
    main()
