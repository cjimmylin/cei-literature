#!/usr/bin/env python3
"""
Non-Ethics Topic Classification Script for CEI Literature Vault

This script adds a 'research_topic' field to papers that have:
- ethics_overall: No

It categorizes these papers into research topics or approaches.
See LLM_CONTEXT.md for classification taxonomy.
"""

import re
from pathlib import Path
from typing import Tuple, Optional

from vault_config import PAPERS_DIR

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter


# Research topic categories with keywords
# Order matters: more specific categories should be checked first or prioritized
TOPIC_CATEGORIES = {
    'AI Safety & Alignment': [
        r'\bai safety\b', r'\bconstitutional ai\b', r'\balignment\b', r'\brobustness\b',
        r'\badversarial\b', r'\bred teaming\b', r'\bjailbreak\b', r'\bsteerability\b',
        r'\bcontrol\b',
    ],
    'Truthfulness & Factuality': [
        r'\btruthful\b', r'\bhallucination\b', r'\bfactuality\b', r'\bfact checking\b',
        r'\bmisinformation\b', r'\bdeception\b', r'\bhonesty\b', r'\brumour\b', r'\bfalsehood\b',
    ],
    'Bias & Fairness': [
        r'\bbias\b', r'\bfairness\b', r'\bstereotype\b', r'\bgender\b', r'\brace\b',
        r'\bdemographic\b', r'\bequity\b',
    ],
    'Interpretability & Explainability': [
        r'\binterpretability\b', r'\bexplainable\b', r'\bxai\b', r'\brationales\b',
        r'\bfeature attribution\b', r'\bsaliency\b', r'\btransparency\b',
    ],
    'Question Answering': [
        r'\bquestion answering\b', r'\bqa\b', r'\bmachine reading comprehension\b',
        r'\breading comprehension\b',
    ],
    'Machine Translation': [
        r'\bmachine translation\b', r'\btranslation\b', r'\bnmt\b', r'\bmultilingual\b',
        r'\bcross-lingual\b',
    ],
    'Dialogue Systems': [
        r'\bdialogue\b', r'\bconversational\b', r'\bchatbot\b', r'\bassistant\b',
        r'\bresponse generation\b',
    ],
    'Computer Vision & Multimodal': [
        r'\bcomputer vision\b', r'\bimage\b', r'\bvisual\b', r'\bvideo\b',
        r'\bmultimodal\b', r'\bcaptioning\b', r'\bvqa\b',
    ],
    'Social & Cultural Analysis': [
        r'\bsocial science\b', r'\bpsychology\b', r'\bcultural\b', r'\bsocietal\b',
        r'\bhuman behavior\b', r'\bpolitical\b', r'\bideology\b', r'\breligion\b',
    ],
    'NLP & Representation Learning': [
        r'\bnlp\b', r'\bnatural language processing\b', r'\bword embedding\b',
        r'\bcontextualized embedding\b', r'\bbert\b', r'\btransformer\b',
        r'\blanguage model\b', r'\btext generation\b', r'\bsummarization\b',
        r'\bsentiment analysis\b', r'\bparsing\b',
    ],
    'Machine Learning': [
        r'\bmachine learning\b', r'\bdeep learning\b', r'\bneural network\b',
        r'\breinforcement learning\b', r'\bsupervised\b', r'\bunsupervised\b',
        r'\bdataset\b', r'\bbenchmark\b',
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


def classify_topic(text: str) -> str:
    """Determine the best-fitting research topic for a paper."""
    text_lower = text.lower()
    
    # Priority-based matching
    # Iterate through categories in the defined order
    # If a category matches significantly, return it.
    
    # Better approach: Score all categories
    scores = {}
    for topic, patterns in TOPIC_CATEGORIES.items():
        score = 0
        for pattern in patterns:
            matches = re.findall(pattern, text_lower)
            score += len(matches)
        scores[topic] = score
    
    # Filter out zero scores
    active_scores = {k: v for k, v in scores.items() if v > 0}
    
    if not active_scores:
        return 'Other'
    
    # If "AI Safety" or "Truthfulness" or "Bias" have ANY match, prioritize them 
    # because they are core to the vault's purpose even if technical keywords are more frequent.
    priority_topics = ['AI Safety & Alignment', 'Truthfulness & Factuality', 'Bias & Fairness']
    for topic in priority_topics:
        if topic in active_scores and active_scores[topic] > 0:
            # But check if another strictly technical topic has overwhelmingly more matches?
            # For now, let's prioritize these as they describe the "approach" in the context of this vault.
            return topic
            
    # Otherwise return the highest score
    best_topic = max(active_scores, key=active_scores.get)
    return best_topic


def update_frontmatter_with_topic(frontmatter: str, topic: str) -> str:
    """Add or update research_topic in frontmatter."""
    lines = frontmatter.rstrip().split('\n')
    
    # Remove existing research_topic if present
    lines = [l for l in lines if not l.strip().startswith('research_topic:')]
    
    # Add new topic
    lines.append(f'research_topic: "{topic}"')
    
    return '\n'.join(lines)


def process_paper(filepath: Path) -> Tuple[bool, Optional[str]]:
    """
    Process a single paper file and add research_topic if applicable.
    Returns (modified, topic)
    """
    try:
        # Use safe YAML utilities
        frontmatter, remaining = read_paper(filepath)
        if not frontmatter:
            return False, None

        # Check if paper qualifies (ethics_overall=No)
        ethics_overall = get_frontmatter_value(frontmatter, 'ethics_overall')

        if ethics_overall != 'No':
            return False, None

        # Extract title and abstract for classification
        title_match = re.search(r'^# (.+)$', remaining, re.MULTILINE)
        title = title_match.group(1) if title_match else ''
        abstract = extract_abstract(remaining)

        # Classify the topic
        text = f"{title} {abstract}".strip()
        topic = classify_topic(text)

        # Update frontmatter
        new_frontmatter = update_frontmatter_with_topic(frontmatter, topic)

        # Validate and write back using safe utility
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

        write_paper(filepath, new_frontmatter, remaining, validate=True)

        return True, topic

    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False, None


def main():
    """Main function to process all papers."""
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return
    
    paper_files = list(papers_dir.glob('*.md'))
    print(f"Found {len(paper_files)} paper files to process\n")
    
    # Statistics
    topic_counts = {}
    modified_count = 0
    skipped_count = 0
    
    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 100 == 0:
            print(f"Processing paper {i}/{len(paper_files)}...")
        
        modified, topic = process_paper(filepath)
        
        if modified and topic:
            modified_count += 1
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
        else:
            skipped_count += 1
    
    # Print summary
    print(f"\n{'='*70}")
    print("RESEARCH TOPIC CLASSIFICATION SUMMARY (Non-Ethics Papers)")
    print(f"{'='*70}")
    print(f"\nPapers with research_topic added: {modified_count}")
    print(f"Papers skipped (ethics_overall != No): {skipped_count}")
    
    print(f"\n{'Topic':<35} | {'Count':>6}")
    print('-' * 45)
    for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f"{topic:<35} | {count:>6}")
    
    print(f"\n{'='*70}")


if __name__ == '__main__':
    main()
