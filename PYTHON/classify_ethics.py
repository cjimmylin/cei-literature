#!/usr/bin/env python3
"""
Ethics Classification Script for CEI Literature Vault

This script analyzes all papers in the papers/ directory and classifies each
according to four ethics-related properties:
1. Ethics Overall - Does the paper touch on ethics in general?
2. Virtue Ethics - Does the paper relate to virtue ethics?
3. Deontological Ethics - Does the paper discuss deontological/duty-based ethics?
4. Utilitarian Ethics - Does the paper address consequentialist or utilitarian ethics?

Each property is assigned: Yes, No, or Unknown.
See LLM_CONTEXT.md for classification taxonomy.
"""

import re
from pathlib import Path
from typing import Dict, Tuple

from vault_config import PAPERS_DIR

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

from ethics_scoring import score_paper, safe_yaml_set_int, ETHICS_FIELDS


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper
# Note: keyword lists and check_keywords() moved to ethics_scoring.py


def classify_paper(abstract: str, title: str = '') -> dict:
    """
    Classify a paper based on its abstract and title.
    Returns dict with integer scores (0-100) for each ethics category.
    """
    if not f"{title} {abstract}".strip():
        return {f: 0 for f in ETHICS_FIELDS}
    return compute_all_scores(title, abstract, "")


def add_classifications_to_frontmatter(frontmatter: str, classifications: dict) -> str:
    """Add classification properties to YAML frontmatter as unquoted integers."""
    fm = frontmatter
    for key, value in classifications.items():
        fm, replaced = safe_yaml_set_int(fm, key, value)
        if not replaced:
            # Field doesn't exist yet, append it
            fm = fm.rstrip() + f'\n{key}: {int(value)}'
    return fm


def process_paper(filepath: Path) -> Tuple[bool, Dict[str, str]]:
    """
    Process a single paper file and add ethics classifications.
    Returns (success, classifications)
    """
    try:
        # Use safe YAML utilities
        frontmatter, remaining = read_paper(filepath)
        if not frontmatter:
            print(f"  Warning: No frontmatter found in {filepath.name}")
            return False, {}

        # Extract title from YAML frontmatter short_title field
        title_match = re.search(r'^short_title:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ''

        # Extract abstract from YAML frontmatter abstract field
        abstract_match = re.search(r'^abstract:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
        abstract = abstract_match.group(1).strip() if abstract_match else ''

        # Score using full pipeline (loads PDF extract, respects pins)
        classifications = score_paper(str(filepath), title, abstract)

        # Update frontmatter with classifications
        new_frontmatter = add_classifications_to_frontmatter(frontmatter, classifications)

        # Validate before writing
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

        # Write back using safe utility
        write_paper(filepath, new_frontmatter, remaining, validate=True)

        return True, classifications

    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False, {}


def main():
    """Main function to process all papers."""
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return
    
    # Get all markdown files
    paper_files = list(papers_dir.glob('*.md'))
    print(f"Found {len(paper_files)} paper files to process\n")
    
    # Statistics
    stats = {
        'processed': 0,
        'failed': 0,
        'scores': {f: [] for f in ETHICS_FIELDS},
    }
    
    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 50 == 0 or i == len(paper_files):
            print(f"Processing paper {i}/{len(paper_files)}...")
        
        success, classifications = process_paper(filepath)
        
        if success:
            stats['processed'] += 1
            for key, value in classifications.items():
                stats['scores'][key].append(value)
        else:
            stats['failed'] += 1
    
    # Print summary
    print(f"\n{'='*60}")
    print("CLASSIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"\nTotal papers processed: {stats['processed']}")
    print(f"Failed to process: {stats['failed']}")
    
    for field in ETHICS_FIELDS:
        scores = stats['scores'][field]
        above = sum(1 for s in scores if s >= 50)
        below = sum(1 for s in scores if s < 50)
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{field:25} | >=50: {above:4} | <50: {below:4} | avg: {avg:.1f}")
    print(f"\n{'='*60}")


if __name__ == '__main__':
    main()
