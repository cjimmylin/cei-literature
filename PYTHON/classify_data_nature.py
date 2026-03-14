#!/usr/bin/env python3
"""
Data Nature Classification Script for CEI Literature Vault

This script analyzes all papers in the papers/ directory and classifies each
according to their data nature:
1. is_benchmark - Does the paper introduce/use a benchmark?
2. is_eval - Does the paper provide evaluation/assessment methods?
3. is_dataset - Does the paper introduce/describe a dataset?
4. data_description - Technical description of the data nature
5. data_metrics - Quantitative metrics about the data

Each property is assigned: Yes, No, N/A, or Unknown.
For data_description and data_metrics, a string is provided.

See implementation_plan.md for classification logic.

CLASSIFICATION APPROACH:
- Uses keyword matching on paper titles and abstracts
- Papers can be classified as multiple types (e.g., benchmark + eval + dataset)
- ~42% of papers are benchmarks, ~62% are evaluations, ~51% are datasets
- 116 papers fall into all three categories simultaneously

METRICS EXTRACTION:
- Uses regex patterns to extract quantitative metrics from abstracts
- Captures: question/example counts, language counts, token counts, file sizes, categories
- Only ~11% of papers (58/533) have extractable metrics in abstracts
- Many papers discuss metrics in body text which this script doesn't access

KNOWN LIMITATIONS:
- Papers without abstracts are conservatively classified
- Keyword-based approach may miss papers using alternative terminology
- False negatives possible for papers using conceptual terms (e.g., "collection" vs "dataset")

USAGE:
python3 classify_data_nature.py

This will modify all paper files in place by adding the 5 new metadata fields.
"""

import re
import sys
from pathlib import Path
from typing import Dict, Tuple, List

from vault_config import PAPERS_DIR

# Import safe YAML utilities
from yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from insight_logger import InsightLogger


# Keywords for each category (case-insensitive matching)
# These keywords are matched against the combined title + abstract text

# BENCHMARK KEYWORDS: Papers that introduce or use systematic evaluation frameworks
# Examples: TruthfulQA, HELM, HaluEval, BBQ, MACHIAVELLI
BENCHMARK_KEYWORDS = [
    r'\bbenchmark\w*\b',
    r'\bevaluation suite\b',
    r'\btest suite\b',
    r'\bleaderboard\b',
    r'\bcomparative evaluation\b',
    r'\bstandard benchmark\b',
    r'\bbench\b',  # Common abbreviation (e.g., "HarmBench", "TrustLLM bench")
]

# EVAL KEYWORDS: Papers focusing on evaluation/assessment methodologies
# Note: Many papers are BOTH benchmarks AND evaluations
# Examples: HELM (benchmark that evaluates), Constitutional AI (evaluation method)
EVAL_KEYWORDS = [
    r'\bevaluat\w+\b',
    r'\bassess\w+\b',
    r'\bmeasur\w+\b',
    r'\btesting\b',
    r'\btest\w*\s+(performance|models?|systems?|methods?)\b',
    r'\bmetric\w*\b',
    r'\bperformance evaluation\b',
    r'\bempirical evaluation\b',
    r'\bcomparing\b',
    r'\bcomparison\b',
]

# DATASET KEYWORDS: Papers introducing new datasets or data collections
# Examples: Moral Stories, Social Chemistry 101, BOLD, CrowS-Pairs
DATASET_KEYWORDS = [
    r'\bdataset\w*\b',
    r'\bcorpus\b', r'\bcorpora\b',
    r'\bcollection\b',
    r'\bdatabase\b',
    r'\bannotated data\b',
    r'\btraining data\b',
    r'\btest data\b',
    r'\bdata\s+collection\b',
    r'\bannotations?\b',
]

# Patterns for extracting quantitative data metrics from abstracts
# These regex patterns capture common ways of reporting dataset/benchmark sizes
# Examples matched: "817 questions", "100K tokens", "5,000 examples", "42 scenarios"
METRICS_PATTERNS = [
    # Numbers with questions, examples, instances, samples, cases, items
    r'(\d+[,\d]*)\s+(questions?|examples?|instances?|samples?|cases?|items?|scenarios?|vignettes?|prompts?)',
    # Test cases/instances
    r'(\d+[,\d]*)\s+(test\s+cases?|test\s+instances?|test\s+examples?)',
    # K/M notation (e.g., "5K examples", "1.2M tokens")
    r'(\d+\.?\d*[KkMm])\s+(questions?|examples?|instances?|samples?|tokens?|words?|sentences?|documents?|posts?|tweets?|comments?)',
    # Range notation (e.g., "100-500 examples")
    r'(\d+[,\d]*\s*[-–]\s*\d+[,\d]*)\s+(questions?|examples?|instances?|samples?)',
    # Approximate notation (e.g., "~5,000 questions")
    r'(~\s*\d+[,\d]*)\s+(questions?|examples?|instances?|samples?)',
    # "Over/more than" notation
    r'(over|more than)\s+(\d+[,\d]*[KkMm]?)\s+(questions?|examples?|instances?|samples?)',
    # Size in MB/GB
    r'(\d+\.?\d*)\s*(MB|GB|TB)',
    # Token counts
    r'(\d+[,\d]*[KkMm]?)\s+(tokens?|words?)',
    # Datasets with counts
    r'(\d+[,\d]*)\s+(datasets?|sources?|languages?|categories?)',
]


# Note: extract_frontmatter_and_content replaced by yaml_frontmatter_utils.read_paper


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown content."""
    # Look for ## Abstract section
    abstract_match = re.search(r'## Abstract\s*\n\n?(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if abstract_match:
        return abstract_match.group(1).strip()
    return ''


def extract_title_from_content(content: str) -> str:
    """Extract title from markdown content (first # heading)."""
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    return title_match.group(1) if title_match else ''


def check_keywords(text: str, keywords: List[str]) -> bool:
    """Check if any keyword pattern matches in the text."""
    text_lower = text.lower()
    for pattern in keywords:
        if re.search(pattern, text_lower):
            return True
    return False


def extract_metrics(text: str) -> str:
    """Extract quantitative data metrics from text."""
    metrics = []
    text_lower = text.lower()
    
    for pattern in METRICS_PATTERNS:
        matches = re.finditer(pattern, text_lower, re.IGNORECASE)
        for match in matches:
            # Get the full matched text
            metric_text = match.group(0)
            # Clean up the text
            metric_text = re.sub(r'\s+', ' ', metric_text).strip()
            if metric_text not in metrics:
                metrics.append(metric_text)
    
    # Limit to the most relevant metrics (first 5)
    if metrics:
        return '; '.join(metrics[:5])
    return 'Not specified'


def generate_data_description(
    title: str,
    abstract: str,
    is_benchmark: bool,
    is_eval: bool,
    is_dataset: bool
) -> str:
    """
    Generate a technical description of the data nature.
    
    This function creates context-aware descriptions by:
    1. Identifying the paper type(s): benchmark, eval, and/or dataset
    2. Detecting the domain/task from abstract keywords
    3. Combining them into a descriptive string
    
    Examples of generated descriptions:
    - "Benchmark for moral/ethical reasoning"
    - "Multilingual benchmark for bias and fairness"
    - "Annotated dataset for hate speech detection"
    - "Evaluation framework for toxicity detection"
    """
    
    # If none of the categories apply, mark as N/A
    if not any([is_benchmark, is_eval, is_dataset]):
        return 'N/A'
    
    descriptions = []
    
    # For benchmark papers: Identify special characteristics
    if is_benchmark:
        # Check for multilingual or multi-task characteristics
        if 'multilingual' in abstract.lower() or 'multi-lingual' in abstract.lower():
            descriptions.append('Multilingual benchmark')
        elif 'multi-task' in abstract.lower() or 'multitask' in abstract.lower():
            descriptions.append('Multi-task benchmark')
        else:
            descriptions.append('Benchmark')
        
        # Try to identify what domain is being benchmarked
        if 'moral' in abstract.lower() or 'ethical' in abstract.lower():
            descriptions.append('for moral/ethical reasoning')
        elif 'safety' in abstract.lower():
            descriptions.append('for AI safety')
        elif 'bias' in abstract.lower() or 'fairness' in abstract.lower():
            descriptions.append('for bias and fairness')
        elif 'hallucination' in abstract.lower():
            descriptions.append('for hallucination detection')
    
    # For evaluation papers: Identify the methodology type
    if is_eval:
        if not is_benchmark:  # Avoid duplication with benchmark descriptions
            if 'framework' in abstract.lower():
                descriptions.append('Evaluation framework')
            elif 'method' in abstract.lower():
                descriptions.append('Evaluation methodology')
            else:
                descriptions.append('Evaluation approach')
    
    # For dataset papers: Identify dataset characteristics and domain
    if is_dataset:
        # Check if the dataset is annotated
        if 'annotated' in abstract.lower():
            descriptions.append('annotated dataset')
        elif 'corpus' in abstract.lower() or 'corpora' in abstract.lower():
            descriptions.append('text corpus')
        else:
            descriptions.append('dataset')
        
        # Try to identify the task/domain the dataset is for
        if 'hate speech' in abstract.lower():
            descriptions.append('for hate speech detection')
        elif 'toxic' in abstract.lower():
            descriptions.append('for toxicity detection')
        elif 'question answering' in abstract.lower() or 'QA' in abstract:
            descriptions.append('for question answering')
        elif 'conversation' in abstract.lower() or 'dialog' in abstract.lower():
            descriptions.append('for conversational AI')
    
    # Combine all description parts into a single string
    if descriptions:
        return ' '.join(descriptions).capitalize()
    
    # Default fallback if no specific description could be generated
    return 'Research data'


def classify_paper(title: str, abstract: str) -> Dict[str, str]:
    """
    Classify a paper based on its title and abstract.
    Returns dict with classification for each category.
    """
    # Combine title and abstract for analysis
    text = f"{title} {abstract}".strip()
    
    if not text:
        return {
            'is_benchmark': 'Unknown',
            'is_eval': 'Unknown',
            'is_dataset': 'Unknown',
            'data_description': 'Unknown',
            'data_metrics': 'Unknown',
        }
    
    # Check for each category
    is_benchmark = check_keywords(text, BENCHMARK_KEYWORDS)
    is_eval = check_keywords(text, EVAL_KEYWORDS)
    is_dataset = check_keywords(text, DATASET_KEYWORDS)
    
    # Extract metrics from abstract (more detailed than title)
    metrics = extract_metrics(abstract if abstract else text)
    
    # Generate description
    description = generate_data_description(title, abstract, is_benchmark, is_eval, is_dataset)
    
    return {
        'is_benchmark': 'Yes' if is_benchmark else 'No',
        'is_eval': 'Yes' if is_eval else 'No',
        'is_dataset': 'Yes' if is_dataset else 'No',
        'data_description': description,
        'data_metrics': metrics,
    }


def add_classifications_to_frontmatter(frontmatter: str, classifications: Dict[str, str]) -> str:
    """Add classification properties to YAML frontmatter."""
    lines = frontmatter.rstrip().split('\n')
    
    # Remove any existing classification properties
    lines = [l for l in lines if not any(
        l.strip().startswith(f'{key}:') for key in classifications.keys()
    )]
    
    # Add new classification properties with proper escaping for strings
    for key, value in classifications.items():
        # Use quotes for string values to handle special characters
        lines.append(f'{key}: "{value}"')
    
    return '\n'.join(lines)


def process_paper(filepath: Path, ilog: InsightLogger = None) -> Tuple[bool, Dict[str, str]]:
    """
    Process a single paper file and add data nature classifications.
    Returns (success, classifications)
    """
    try:
        # Use safe YAML utilities
        frontmatter, remaining = read_paper(filepath)
        if not frontmatter:
            print(f"  Warning: No frontmatter found in {filepath.name}")
            if ilog:
                ilog.data_quality(filepath.name, "no_frontmatter", "No frontmatter found")
            return False, {}

        # Capture old values for comparison
        old_values = {}
        if ilog:
            for field in ("is_benchmark", "is_eval", "is_dataset"):
                match = re.search(rf'^{field}:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
                if match:
                    old_values[field] = match.group(1).strip()

        # Extract title and abstract
        title = extract_title_from_content(remaining)
        abstract = extract_abstract(remaining)

        # Classify the paper
        classifications = classify_paper(title, abstract)

        # Log reclassifications (Yes<->No changes)
        if ilog:
            for field in ("is_benchmark", "is_eval", "is_dataset"):
                if field in old_values:
                    old_val = old_values[field]
                    new_val = classifications.get(field, "Unknown")
                    if old_val != new_val and old_val in ("Yes", "No") and new_val in ("Yes", "No"):
                        ilog.reclassification(filepath.name, field, old_val, new_val)

        # Update frontmatter with classifications
        new_frontmatter = add_classifications_to_frontmatter(frontmatter, classifications)

        # Validate and write back using safe utility
        is_valid, issues = validate_frontmatter(new_frontmatter)
        if not is_valid:
            print(f"  Warning: YAML validation issues in {filepath.name}: {issues}")

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

    ilog = InsightLogger("classify_data_nature")

    # Get all markdown files
    paper_files = list(papers_dir.glob('*.md'))
    print(f"Found {len(paper_files)} paper files to process\n")

    # Statistics
    stats = {
        'processed': 0,
        'failed': 0,
        'is_benchmark': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'is_eval': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'is_dataset': {'Yes': 0, 'No': 0, 'Unknown': 0},
        'has_metrics': 0,
        'no_metrics': 0,
    }

    for i, filepath in enumerate(sorted(paper_files), 1):
        if i % 50 == 0 or i == len(paper_files):
            print(f"Processing paper {i}/{len(paper_files)}...")

        success, classifications = process_paper(filepath, ilog)
        
        if success:
            stats['processed'] += 1
            stats['is_benchmark'][classifications.get('is_benchmark', 'Unknown')] += 1
            stats['is_eval'][classifications.get('is_eval', 'Unknown')] += 1
            stats['is_dataset'][classifications.get('is_dataset', 'Unknown')] += 1
            
            # Track metrics
            if classifications.get('data_metrics', '') not in ['Not specified', 'Unknown', '']:
                stats['has_metrics'] += 1
            else:
                stats['no_metrics'] += 1
        else:
            stats['failed'] += 1
    
    # Print summary
    print(f"\n{'='*70}")
    print("DATA NATURE CLASSIFICATION SUMMARY")
    print(f"{'='*70}")
    print(f"\nTotal papers processed: {stats['processed']}")
    print(f"Failed to process: {stats['failed']}")
    
    print(f"\n{'Is Benchmark':25} | Yes: {stats['is_benchmark']['Yes']:4} | No: {stats['is_benchmark']['No']:4} | Unknown: {stats['is_benchmark']['Unknown']:4}")
    print(f"{'Is Evaluation':25} | Yes: {stats['is_eval']['Yes']:4} | No: {stats['is_eval']['No']:4} | Unknown: {stats['is_eval']['Unknown']:4}")
    print(f"{'Is Dataset':25} | Yes: {stats['is_dataset']['Yes']:4} | No: {stats['is_dataset']['No']:4} | Unknown: {stats['is_dataset']['Unknown']:4}")
    
    print(f"\n{'Papers with metrics':25} | {stats['has_metrics']:4}")
    print(f"{'Papers without metrics':25} | {stats['no_metrics']:4}")

    print(f"\n{'='*70}")

    # Log summary stats
    ilog.stat(f"Processed {stats['processed']} papers, {stats['failed']} failed")
    ilog.stat(f"is_benchmark: Yes={stats['is_benchmark']['Yes']}, No={stats['is_benchmark']['No']}")
    ilog.stat(f"is_eval: Yes={stats['is_eval']['Yes']}, No={stats['is_eval']['No']}")
    ilog.stat(f"is_dataset: Yes={stats['is_dataset']['Yes']}, No={stats['is_dataset']['No']}")
    ilog.stat(f"Papers with metrics: {stats['has_metrics']}")

    ilog.finalize()


if __name__ == '__main__':
    main()
