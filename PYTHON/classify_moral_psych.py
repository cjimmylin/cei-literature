#!/usr/bin/env python3
"""
Classify papers by Moral Psychological Perspectives.

This script analyzes paper titles and abstracts to determine:
1. moral_psychology: Which school/theory (e.g., "Moral Foundations Theory", "Dual Process Theory")
   or "No", "Unknown", "N/A"

LEARNINGS / DESIGN DECISIONS:
- Keyword Sensitivity: Targeting specific terms like "Haidt" or "Moral Foundations" works well,
  but broader terms like "moral reasoning" are often too generic and led to false positives.
  Thus, we restricted the patterns to specific named theories.
- Trolley Problems: Included as a "psychological" category because they are frequently used
  to operationalize dual process theory or utilitarian vs. deontological judgments.
"""

import re
from pathlib import Path
from typing import Tuple

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

PAPERS_DIR = Path(__file__).parent / "papers"

# Moral Psychology classification patterns
PSYCH_PATTERNS = {
    "Moral Foundations Theory": [
        r"\bMoral Foundations\b", r"\bMFT\b", r"\bHaidt\b", r"\bGraham\b", 
        r"\b5 foundations\b", r"\bcare/harm\b", r"\bsanctity/degradation\b", 
        r"\bliberty/oppression\b", r"\bloyalty/betrayal\b", r"\bauthority/subversion\b", 
        r"\bMFQ\b", # Moral Foundations Questionnaire
        r"\bMFTC\b" # Moral Foundations Twitter Corpus
    ],
    "Dual Process Theory": [
        r"\bDual Process\b", r"\bJoshua Greene\b", r"\bfast and slow\b", 
        r"\bcognitive vs emotional\b", r"\butilitarian vs deontological processing\b",
        r"\bmanual mode\b", r"\bautomatic settings\b" # Greene's metaphor
    ],
    "Dyadic Morality": [
        r"\bDyadic Morality\b", r"\bTheory of Dyadic Morality\b", r"\bKurt Gray\b", 
        r"\bmoral typecasting\b", r"\bagent and patient\b", r"\bdyad\b"
    ],
    "Social Intuitionist": [
        r"\bSocial Intuitionist\b", r"\bSIM\b", r"\bintuitive judgment\b", 
        r"\breasoning comes second\b", r"\bmoral dumbfounding\b"
    ],
    "Moral Identity": [
        r"\bMoral Identity\b", r"\bself-importance of moral identity\b", 
        r"\bAquino\b", r"\bReed\b"
    ],
    "Cognitive Developmental": [
        r"\bKohlberg\b", r"\bPiaget\b", r"\bstages of moral development\b", 
        r"\bpre-conventional\b", r"\bpost-conventional\b", 
        r"\bconventional level\b", r"\bHeinz dilemma\b",
        r"\bRest\b", r"\bDefining Issues Test\b", r"\bDIT\b"
    ],
    "Value Pluralism / Schwartz": [
        r"\bSchwartz Theory\b", r"\bBasic Human Values\b", r"\bSchwartz Values\b", 
        r"\bValue Pluralism\b", r"\bUniversalism\b", r"\bBenevolence\b", 
        r"\bSelf-Direction\b", r"\bStimulation\b", r"\bHedonism\b", 
        r"\bAchievement\b", r"\bPower\b", r"\bSecurity\b", r"\bConformity\b", 
        r"\bTradition\b"
    ],
    "Trolley / Dilemmas (Psych)": [
        r"\bTrolley problem\b", r"\bMoral Machine\b", r"\bsacrificial dilemma\b", 
        r"\bfootbridge problem\b", r"\bswitch problem\b"
    ]
}

# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown content."""
    # Look for ## Abstract section
    match = re.search(r'## Abstract\s*\n\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def extract_title(content: str) -> str:
    """Extract title from markdown content."""
    # Look for # Title
    match = re.search(r'^# (.+?)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


def classify_moral_psych(title: str, abstract: str) -> str:
    """Classify paper by moral psychological perspective."""
    original_text = f"{title} {abstract}"
    
    matches = []
    for theory, patterns in PSYCH_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, original_text, re.IGNORECASE):
                matches.append(theory)
                break
    
    if matches:
        # Remove duplicates while preserving order
        seen = set()
        unique_matches = []
        for m in matches:
            if m not in seen:
                seen.add(m)
                unique_matches.append(m)
        return ", ".join(unique_matches)
    
    return "N/A"


def update_frontmatter(frontmatter: str, moral_psych: str) -> str:
    """Add or update moral_psychology classification in frontmatter."""
    lines = frontmatter.split('\n')
    new_lines = []
    
    # Remove existing property if present
    skip_next = False
    for line in lines:
        if skip_next and line.startswith('  '):
            continue
        skip_next = False
        
        if line.startswith('moral_psychology:'):
            continue
        # Skip standalone dashes that might have been added erroneously
        if line.strip() == '-':
            continue
        new_lines.append(line)
    
    # Add new property at the end (before any trailing empty lines)
    while new_lines and new_lines[-1].strip() == '':
        new_lines.pop()
    
    new_lines.append(f'moral_psychology: "{moral_psych}"')
    
    return '\n'.join(new_lines)


def process_paper(filepath: Path) -> Tuple[str, str]:
    """Process a single paper file and return classification."""
    # Use safe YAML utilities
    frontmatter, body = read_paper(filepath)

    title = extract_title(body)
    abstract = extract_abstract(body)

    moral_psych = classify_moral_psych(title, abstract)

    # Update the file
    new_frontmatter = update_frontmatter(frontmatter, moral_psych)

    # Validate and write back using safe utility
    is_valid, issues = validate_frontmatter(new_frontmatter)
    if not is_valid:
        print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

    write_paper(filepath, new_frontmatter, body, validate=True)

    return filepath.name, moral_psych


def main():
    """Process all papers and generate summary."""
    papers = list(PAPERS_DIR.glob("*.md"))
    print(f"Found {len(papers)} papers to process\n")
    
    psych_counts = {}
    results = []
    
    for paper in sorted(papers):
        try:
            name, moral_psych = process_paper(paper)
            results.append((name, moral_psych))
            
            if moral_psych != "N/A":
                for p in moral_psych.split(", "):
                    psych_counts[p] = psych_counts.get(p, 0) + 1
            else:
                 psych_counts["N/A"] = psych_counts.get("N/A", 0) + 1
                
        except Exception as e:
            print(f"Error processing {paper.name}: {e}")
    
    # Print summary
    print("=" * 60)
    print("MORAL PSYCHOLOGY CLASSIFICATION SUMMARY")
    print("=" * 60)
    for theory, count in sorted(psych_counts.items(), key=lambda x: -x[1]):
        print(f"  {theory}: {count}")
    
    # Print papers with classifications (non-N/A)
    print("\n" + "=" * 60)
    print("PAPERS WITH IDENTIFIED MORAL PSYCHOLOGY")
    print("=" * 60)
    psych_papers = [(n, p) for n, p in results if p != "N/A"]
    for name, moral_psych in sorted(psych_papers):
        print(f"  {name}")
        print(f"    Theory: {moral_psych}")
    
    print(f"\n\nTotal papers processed: {len(results)}")
    print(f"Papers with identified psychology: {len(psych_papers)}")


if __name__ == "__main__":
    main()
