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


# Keywords for each ethics category (case-insensitive matching)
ETHICS_OVERALL_KEYWORDS = [
    r'\bethics?\b', r'\bethical\b', r'\bmoral\b', r'\bmorality\b', r'\bvalues?\b',
    r'\bnormative\b', r'\bfairness\b', r'\bjustice\b', r'\bbias\b', r'\bharm\b',
    r'\bsafety\b', r'\balignment\b', r'\bresponsible\b', r'\baccountable\b',
    r'\bhate speech\b', r'\btoxic\b', r'\boffensive\b', r'\babusive\b',
    r'\bstereotype\b', r'\bdiscrimination\b', r'\bhuman rights\b',
    r'\bprosocial\b', r'\bimmoral\b', r'\bunethical\b', r'\bwrongdoing\b',
    r'\bmoral reasoning\b', r'\bmoral judgment\b', r'\bmoral decision\b',
    r'\bmoral dilemma\b', r'\btrolley problem\b', r'\bmoral foundations\b',
]

VIRTUE_ETHICS_KEYWORDS = [
    r'\bvirtue\b', r'\bvirtuous\b', r'\bvirtue ethics\b', r'\bcharacter\b',
    r'\bexcellence\b', r'\bflourishing\b', r'\beudaimonia\b', r'\baristotel\w*\b',
    r'\bprudence\b', r'\btemperance\b', r'\bcourage\b', r'\bwisdom\b',
    r'\bphronesis\b', r'\barete\b', r'\bmoral character\b', r'\bmoral virtue\b',
]

DEONTOLOGICAL_KEYWORDS = [
    r'\bdeontolog\w*\b', r'\bduty\b', r'\bduties\b', r'\bkantian\b', r'\bkant\b',
    r'\bcategorical imperative\b', r'\bobligation\b', r'\brights-based\b',
    r'\brule-based\b', r'\buniversal\w* law\b', r'\bmoral law\b',
    r'\bmoral rules?\b', r'\bmoral principles?\b', r'\bmoral duty\b',
    r'\bimperative\b', r'\bintrinsic\w* wrong\b', r'\bintrinsic\w* right\b',
]

UTILITARIAN_KEYWORDS = [
    r'\butilitarian\w*\b', r'\bconsequential\w*\b', r'\butility\b',
    r'\bmaximize?\b', r'\bmaximis\w*\b', r'\bgreatest good\b', r'\bwelfare\b',
    r'\boutcome-based\b', r'\bcost-benefit\b', r'\bwell-being\b', r'\bwellbeing\b',
    r'\bbeneficence\b', r'\bharm reduction\b', r'\bnet benefit\b',
    r'\bgreatest happiness\b', r'\bgreatest number\b', r'\bmill\b', r'\bbentham\b',
    r'\bhedonism\b', r'\bhedonistic\b',
]


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown content."""
    # Look for ## Abstract section
    abstract_match = re.search(r'## Abstract\s*\n\n?(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if abstract_match:
        return abstract_match.group(1).strip()
    return ''


def check_keywords(text: str, keywords: list) -> bool:
    """Check if any keyword pattern matches in the text."""
    text_lower = text.lower()
    for pattern in keywords:
        if re.search(pattern, text_lower):
            return True
    return False


def classify_paper(abstract: str, title: str = '') -> Dict[str, str]:
    """
    Classify a paper based on its abstract and title.
    Returns dict with classification for each ethics category.
    """
    # Combine abstract and title for analysis
    text = f"{title} {abstract}".strip()
    
    if not text:
        return {
            'ethics_overall': 'Unknown',
            'virtue_ethics': 'Unknown',
            'deontological_ethics': 'Unknown',
            'utilitarian_ethics': 'Unknown',
        }
    
    return {
        'ethics_overall': 'Yes' if check_keywords(text, ETHICS_OVERALL_KEYWORDS) else 'No',
        'virtue_ethics': 'Yes' if check_keywords(text, VIRTUE_ETHICS_KEYWORDS) else 'No',
        'deontological_ethics': 'Yes' if check_keywords(text, DEONTOLOGICAL_KEYWORDS) else 'No',
        'utilitarian_ethics': 'Yes' if check_keywords(text, UTILITARIAN_KEYWORDS) else 'No',
    }


def add_classifications_to_frontmatter(frontmatter: str, classifications: Dict[str, str]) -> str:
    """Add classification properties to YAML frontmatter."""
    lines = frontmatter.rstrip().split('\n')
    
    # Remove any existing classification properties
    lines = [l for l in lines if not any(
        l.strip().startswith(f'{key}:') for key in classifications.keys()
    )]
    
    # Add new classification properties
    for key, value in classifications.items():
        lines.append(f'{key}: "{value}"')
    
    return '\n'.join(lines)


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

        # Extract title from the markdown content (first # heading)
        title_match = re.search(r'^# (.+)$', remaining, re.MULTILINE)
        title = title_match.group(1) if title_match else ''

        # Extract abstract
        abstract = extract_abstract(remaining)

        # Classify the paper
        classifications = classify_paper(abstract, title)

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
        'ethics_overall': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'virtue_ethics': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'deontological_ethics': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'utilitarian_ethics': {'Yes': 0, 'No': 0, 'Unknown': 0},
    }
    
    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 50 == 0 or i == len(paper_files):
            print(f"Processing paper {i}/{len(paper_files)}...")
        
        success, classifications = process_paper(filepath)
        
        if success:
            stats['processed'] += 1
            for key, value in classifications.items():
                stats[key][value] += 1
        else:
            stats['failed'] += 1
    
    # Print summary
    print(f"\n{'='*60}")
    print("CLASSIFICATION SUMMARY")
    print(f"{'='*60}")
    print(f"\nTotal papers processed: {stats['processed']}")
    print(f"Failed to process: {stats['failed']}")
    
    print(f"\n{'Ethics Overall':25} | Yes: {stats['ethics_overall']['Yes']:4} | No: {stats['ethics_overall']['No']:4} | Unknown: {stats['ethics_overall']['Unknown']:4}")
    print(f"{'Virtue Ethics':25} | Yes: {stats['virtue_ethics']['Yes']:4} | No: {stats['virtue_ethics']['No']:4} | Unknown: {stats['virtue_ethics']['Unknown']:4}")
    print(f"{'Deontological Ethics':25} | Yes: {stats['deontological_ethics']['Yes']:4} | No: {stats['deontological_ethics']['No']:4} | Unknown: {stats['deontological_ethics']['Unknown']:4}")
    print(f"{'Utilitarian Ethics':25} | Yes: {stats['utilitarian_ethics']['Yes']:4} | No: {stats['utilitarian_ethics']['No']:4} | Unknown: {stats['utilitarian_ethics']['Unknown']:4}")
    print(f"\n{'='*60}")


if __name__ == '__main__':
    main()
