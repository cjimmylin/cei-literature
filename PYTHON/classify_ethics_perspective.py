#!/usr/bin/env python3
"""
Ethics Perspective Classification Script for CEI Literature Vault

This script adds an 'ethics_perspective' field to papers that have:
- ethics_overall: Yes
- BUT virtue_ethics, deontological_ethics, and utilitarian_ethics are all No

It categorizes papers into specific ethical perspectives based on their content.
See LLM_CONTEXT.md for classification taxonomy.
"""

import re
import sys
from pathlib import Path
from typing import Tuple, Optional

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter
from vault_config import PAPERS_DIR
from ethics_scoring import is_ethics_yes, parse_ethics_value

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from insight_logger import InsightLogger


# Ethics perspective categories with keywords
ETHICS_PERSPECTIVES = {
    'AI Safety & Alignment': [
        r'\bai safety\b', r'\bsafety\b', r'\balignment\b', r'\baligned\b',
        r'\bjailbreak\b', r'\bredteam\w*\b', r'\badversarial\b',
        r'\bharmful\b', r'\bharmless\b', r'\bhelpful\b', r'\bhonest\b',
        r'\btrustworth\w*\b', r'\breliab\w*\b', r'\brobust\w*\b',
    ],
    'Bias & Fairness': [
        r'\bbias\b', r'\bbiased\b', r'\bbiases\b', r'\bfairness\b', r'\bfair\b',
        r'\bunfair\b', r'\bdiscrimination\b', r'\bstereotype\b', r'\bgender bias\b',
        r'\bracial bias\b', r'\bequity\b', r'\bequitable\b', r'\bdebiasing\b',
    ],
    'Toxicity & Hate Speech': [
        r'\btoxic\b', r'\btoxicity\b', r'\bhate speech\b', r'\bhateful\b',
        r'\boffensive\b', r'\babusive\b', r'\bharassment\b', r'\bcyberbullying\b',
        r'\bhate detection\b', r'\btoxic\w* detection\b',
    ],
    'Moral Reasoning & Psychology': [
        r'\bmoral reasoning\b', r'\bmoral judgment\b', r'\bmoral decision\b',
        r'\bmoral dilemma\b', r'\btrolley problem\b', r'\bmoral foundations\b',
        r'\bmoral machine\b', r'\bmoral psychology\b', r'\bmoral cognition\b',
        r'\bmoral values\b', r'\bvalue alignment\b', r'\bhuman values\b',
    ],
    'Hallucination & Truthfulness': [
        r'\bhallucination\b', r'\bhallucinate\b', r'\btruthful\b', r'\btruth\b',
        r'\bfactual\b', r'\bfaithful\b', r'\bmisinformation\b', r'\bfactuality\b',
        r'\bgrounding\b', r'\bveracity\b',
    ],
    'Privacy & Data Ethics': [
        r'\bprivacy\b', r'\bdata protection\b', r'\bpersonal data\b',
        r'\bconsent\b', r'\banonymity\b', r'\bconfidential\b',
    ],
    'Human Rights': [
        r'\bhuman rights\b', r'\brights\b', r'\bdignity\b', r'\bautonomy\b',
        r'\bfreedom\b', r'\boppression\b',
    ],
    'Responsible AI': [
        r'\bresponsible ai\b', r'\bresponsible\b', r'\baccountab\w*\b',
        r'\btransparenc\w*\b', r'\bexplainab\w*\b', r'\binterpretab\w*\b',
        r'\bauditab\w*\b', r'\bgovernance\b',
    ],
    'Social & Cultural Values': [
        r'\bcultural\b', r'\bculture\b', r'\bsocial norms\b', r'\bsocial values\b',
        r'\bcross-cultural\b', r'\bmulticultural\b', r'\bindigenous\b',
        r'\breligious\b', r'\breligion\b', r'\bislam\w*\b', r'\bchristian\w*\b',
        r'\bubuntu\b', r'\bconfucian\w*\b',
    ],
    'Machine Ethics': [
        r'\bmachine ethics\b', r'\brobot ethics\b', r'\bartificial moral\b',
        r'\bmoral agent\b', r'\bethical ai\b', r'\bai ethics\b',
        r'\bmoral machine\b', r'\bethical decision\b',
    ],
    'Applied Ethics': [
        r'\bmedical ethics\b', r'\bbioethics\b', r'\blegal ethics\b',
        r'\bbusiness ethics\b', r'\bprofessional ethics\b', r'\bnursing\b',
        r'\bhealthcare\b', r'\bclinical\b',
    ],
}

# False positive patterns that reduce perspective scores
PERSPECTIVE_FP = {
    'Hallucination & Truthfulness': [
        r'\bground truth\b', r'\btruth table\b', r'\btruth value\b',
        r'\btruth label\b', r'\btruth set\b',
    ],
    'AI Safety & Alignment': [
        r'\bsequence alignment\b', r'\btext alignment\b', r'\bword alignment\b',
        r'\bimage alignment\b',
    ],
    'Human Rights': [
        r'\ball rights reserved\b', r'\bproperty rights\b',
        r'\baccess rights\b', r'\badmin rights\b',
    ],
}


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown content."""
    abstract_match = re.search(r'## Abstract\s*\n\n?(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if abstract_match:
        return abstract_match.group(1).strip()
    return ''


def get_frontmatter_value(frontmatter: str, key: str) -> str:
    """Get value of a key from frontmatter."""
    match = re.search(rf'^{key}:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ''


def classify_ethics_perspective(text: str) -> str:
    """Determine the best-fitting ethics perspective for a paper."""
    text_lower = text.lower()

    # Count matches for each perspective
    scores = {}
    for perspective, patterns in ETHICS_PERSPECTIVES.items():
        score = 0
        for pattern in patterns:
            matches = re.findall(pattern, text_lower)
            score += len(matches)
        # Subtract FP matches
        for fp_pattern in PERSPECTIVE_FP.get(perspective, []):
            fp_matches = re.findall(fp_pattern, text_lower)
            score -= len(fp_matches)
        scores[perspective] = max(0, score)

    # Get the perspective with highest score
    if not scores or max(scores.values()) == 0:
        return 'General Ethics'

    best_perspective = max(sorted(scores.keys()), key=scores.get)
    return best_perspective


def update_frontmatter_with_perspective(frontmatter: str, perspective: str) -> str:
    """Add or update ethics_perspective in frontmatter."""
    lines = frontmatter.rstrip().split('\n')
    
    # Remove existing ethics_perspective if present
    lines = [l for l in lines if not l.strip().startswith('ethics_perspective:')]
    
    # Add new perspective
    lines.append(f'ethics_perspective: "{perspective}"')
    
    return '\n'.join(lines)


def process_paper(filepath: Path, ilog: InsightLogger = None) -> Tuple[bool, Optional[str]]:
    """
    Process a single paper file and add ethics_perspective if applicable.
    Returns (modified, perspective) - perspective is None if not applicable.
    """
    try:
        # Use safe YAML utilities
        frontmatter, remaining = read_paper(filepath)
        if not frontmatter:
            return False, None

        # Check if paper qualifies (ethics_overall=Yes but others are No)
        ethics_overall = get_frontmatter_value(frontmatter, 'ethics_overall')
        virtue_ethics = get_frontmatter_value(frontmatter, 'virtue_ethics')
        deontological_ethics = get_frontmatter_value(frontmatter, 'deontological_ethics')
        utilitarian_ethics = get_frontmatter_value(frontmatter, 'utilitarian_ethics')

        if not is_ethics_yes(ethics_overall):
            return False, None

        care_ethics = get_frontmatter_value(frontmatter, 'care_ethics')
        contractarian_ethics = get_frontmatter_value(frontmatter, 'contractarian_ethics')

        if (is_ethics_yes(virtue_ethics) or is_ethics_yes(deontological_ethics) or
                is_ethics_yes(utilitarian_ethics) or is_ethics_yes(care_ethics) or
                is_ethics_yes(contractarian_ethics)):
            return False, None

        # Capture old perspective for comparison
        old_perspective = get_frontmatter_value(frontmatter, 'ethics_perspective')

        # Extract title and abstract for classification
        title = get_frontmatter_value(frontmatter, 'short_title')
        abstract = get_frontmatter_value(frontmatter, 'abstract')

        # Classify the perspective
        text = f"{title} {abstract}".strip()
        perspective = classify_ethics_perspective(text)

        # Log perspective changes
        if ilog and old_perspective and old_perspective != perspective:
            ilog.reclassification(filepath.name, "ethics_perspective",
                                  old_perspective, perspective)

        # Update frontmatter
        new_frontmatter = update_frontmatter_with_perspective(frontmatter, perspective)

        # Validate and write back using safe utility
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

        write_paper(filepath, new_frontmatter, remaining, validate=True)

        return True, perspective

    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False, None


def main():
    """Main function to process all papers."""
    if not PAPERS_DIR.exists():
        print(f"Error: papers directory not found at {PAPERS_DIR}")
        return

    ilog = InsightLogger("classify_ethics_perspective")

    paper_files = list(PAPERS_DIR.glob('*.md'))
    print(f"Found {len(paper_files)} paper files to process\n")

    # Statistics
    perspective_counts = {}
    modified_count = 0
    skipped_count = 0

    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 100 == 0 or i == len(paper_files):
            print(f"Processing paper {i}/{len(paper_files)}...")

        modified, perspective = process_paper(filepath, ilog)

        if modified and perspective:
            modified_count += 1
            perspective_counts[perspective] = perspective_counts.get(perspective, 0) + 1
        else:
            skipped_count += 1

    # Log stats
    ilog.stat(f"Papers with ethics_perspective added: {modified_count}")
    ilog.stat(f"Papers skipped: {skipped_count}")
    for perspective, count in sorted(perspective_counts.items(), key=lambda x: -x[1]):
        ilog.stat(f"Perspective '{perspective}': {count} papers")

    # Print summary
    print(f"\n{'='*70}")
    print("ETHICS PERSPECTIVE CLASSIFICATION SUMMARY")
    print(f"{'='*70}")
    print(f"\nPapers with ethics_perspective added: {modified_count}")
    print(f"Papers skipped (had specific framework or no ethics): {skipped_count}")

    print(f"\n{'Perspective':<35} | {'Count':>6}")
    print('-' * 45)
    for perspective, count in sorted(perspective_counts.items(), key=lambda x: -x[1]):
        print(f"{perspective:<35} | {count:>6}")

    print(f"\n{'='*70}")

    ilog.finalize()


if __name__ == '__main__':
    main()
