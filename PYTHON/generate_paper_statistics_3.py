#!/usr/bin/env python3
"""
Generate 20260119-paper-statistics-3.md report for data nature classification.
Provides detailed breakdown of papers by benchmark/eval/dataset categories.

This script generates the most comprehensive data nature report (3,391 lines) with:
- Summary statistics for all categories
- Complete lists of benchmarks (223 papers)
- Complete lists of evaluations (329 papers)
- Complete lists of datasets (269 papers)
- Multi-category breakdowns (all three, benchmark+eval, etc.)
- Papers grouped by description type (93 unique descriptions)
- Papers with extracted metrics (58 papers)
- Papers not in any category (110 papers)

OUTPUT FORMAT:
- Year - Author - [[Wikilink to paper]]
- Description (when available)
- Metrics (when extracted)

OBSIDIAN COMPATIBILITY:
All paper links use Obsidian-friendly wikilinks: [[Filename|Title]]

USAGE:
python3 generate_paper_statistics_3.py

This will create/overwrite 20260119-paper-statistics-3.md in the current directory.
"""

import re
from pathlib import Path
from typing import Dict
from collections import defaultdict

from vault_config import PAPERS_DIR, STATISTICS_DIR


def extract_frontmatter(file_content: str) -> Dict[str, str]:
    """Extract YAML frontmatter into a dictionary."""
    if not file_content.startswith('---'):
        return {}
    
    end_match = re.search(r'\n---\n', file_content[3:])
    if not end_match:
        return {}
    
    frontmatter_text = file_content[4:end_match.start() + 3]
    
    # Parse YAML-like content
    metadata = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip().strip('"\'')
    
    return metadata


def extract_title_from_content(content: str) -> str:
    """Extract title from markdown content."""
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    return title_match.group(1) if title_match else ''


def main():
    """Generate the 20260119-paper-statistics-3.md report."""
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return
    
    # Storage for categorized papers
    benchmarks_yes = []
    benchmarks_no = []
    evals_yes = []
    evals_no = []
    datasets_yes = []
    datasets_no = []
    
    # Multi-category
    all_three = []
    bench_eval = []
    bench_dataset = []
    eval_dataset = []
    none_of_three = []
    
    # By description type
    by_description = defaultdict(list)
    
    # Papers with/without metrics
    with_metrics = []
    without_metrics = []
    
    # Process all papers
    paper_files = list(papers_dir.glob('*.md'))
    
    for filepath in sorted(paper_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = extract_frontmatter(content)
            title = extract_title_from_content(content)
            
            year = metadata.get('year', 'Unknown')
            first_author = metadata.get('first_author', 'Unknown')
            is_benchmark = metadata.get('is_benchmark', 'No')
            is_eval = metadata.get('is_eval', 'No')
            is_dataset = metadata.get('is_dataset', 'No')
            data_metrics = metadata.get('data_metrics', 'Not specified')
            data_description = metadata.get('data_description', 'N/A')
            
            # Create paper entry
            paper_entry = {
                'filename': filepath.stem,
                'title': title,
                'year': year,
                'author': first_author.split(',')[0] if ',' in first_author else first_author,
                'is_benchmark': is_benchmark,
                'is_eval': is_eval,
                'is_dataset': is_dataset,
                'data_metrics': data_metrics,
                'data_description': data_description,
            }
            
            # Single category lists
            if is_benchmark == 'Yes':
                benchmarks_yes.append(paper_entry)
            else:
                benchmarks_no.append(paper_entry)
                
            if is_eval == 'Yes':
                evals_yes.append(paper_entry)
            else:
                evals_no.append(paper_entry)
                
            if is_dataset == 'Yes':
                datasets_yes.append(paper_entry)
            else:
                datasets_no.append(paper_entry)
            
            # Multi-category classification
            if is_benchmark == 'Yes' and is_eval == 'Yes' and is_dataset == 'Yes':
                all_three.append(paper_entry)
            elif is_benchmark == 'Yes' and is_eval == 'Yes':
                bench_eval.append(paper_entry)
            elif is_benchmark == 'Yes' and is_dataset == 'Yes':
                bench_dataset.append(paper_entry)
            elif is_eval == 'Yes' and is_dataset == 'Yes':
                eval_dataset.append(paper_entry)
            elif is_benchmark == 'No' and is_eval == 'No' and is_dataset == 'No':
                none_of_three.append(paper_entry)
            
            # Group by description
            if data_description not in ['N/A', 'Unknown', '']:
                by_description[data_description].append(paper_entry)
            
            # Metrics tracking
            if data_metrics not in ['Not specified', 'Unknown', '']:
                with_metrics.append(paper_entry)
            else:
                without_metrics.append(paper_entry)
                
        except Exception as e:
            print(f"Error processing {filepath.name}: {e}")
    
    # Generate markdown report
    report_path = STATISTICS_DIR / '20260119-paper-statistics-3.md'

    # Ensure STATISTICS directory exists
    STATISTICS_DIR.mkdir(exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Paper Statistics Report: Data Nature Classification\n\n")
        f.write("This report provides a comprehensive breakdown of all papers by their data nature categories.\n\n")
        f.write(f"**Total Papers**: {len(paper_files)}\n\n")
        f.write("---\n\n")
        
        # Table of Contents
        f.write("## Table of Contents\n\n")
        f.write("1. [Summary Statistics](#summary-statistics)\n")
        f.write("2. [Benchmarks](#benchmarks)\n")
        f.write("3. [Evaluation Papers](#evaluation-papers)\n")
        f.write("4. [Datasets](#datasets)\n")
        f.write("5. [Multi-Category Papers](#multi-category-papers)\n")
        f.write("6. [Papers by Description Type](#papers-by-description-type)\n")
        f.write("7. [Papers with Extracted Metrics](#papers-with-extracted-metrics)\n")
        f.write("8. [Papers Not in Any Category](#papers-not-in-any-category)\n\n")
        f.write("---\n\n")
        
        # Summary Statistics
        f.write("## Summary Statistics\n\n")
        f.write(f"- **Benchmarks (Yes)**: {len(benchmarks_yes)} papers\n")
        f.write(f"- **Benchmarks (No)**: {len(benchmarks_no)} papers\n")
        f.write(f"- **Evaluations (Yes)**: {len(evals_yes)} papers\n")
        f.write(f"- **Evaluations (No)**: {len(evals_no)} papers\n")
        f.write(f"- **Datasets (Yes)**: {len(datasets_yes)} papers\n")
        f.write(f"- **Datasets (No)**: {len(datasets_no)} papers\n\n")
        
        f.write("### Multi-Category Breakdown\n\n")
        f.write(f"- **All Three (Benchmark + Eval + Dataset)**: {len(all_three)} papers\n")
        f.write(f"- **Benchmark + Eval only**: {len(bench_eval)} papers\n")
        f.write(f"- **Benchmark + Dataset only**: {len(bench_dataset)} papers\n")
        f.write(f"- **Eval + Dataset only**: {len(eval_dataset)} papers\n")
        f.write(f"- **None of the three**: {len(none_of_three)} papers\n\n")
        
        f.write("### Metrics Extraction\n\n")
        f.write(f"- **Papers with extracted metrics**: {len(with_metrics)} papers\n")
        f.write(f"- **Papers without metrics**: {len(without_metrics)} papers\n\n")
        
        f.write("---\n\n")
        
        # Benchmarks Section
        f.write("## Benchmarks\n\n")
        f.write(f"**Total: {len(benchmarks_yes)} papers**\n\n")
        
        for paper in benchmarks_yes:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
        
        f.write("\n---\n\n")
        
        # Evaluations Section
        f.write("## Evaluation Papers\n\n")
        f.write(f"**Total: {len(evals_yes)} papers**\n\n")
        
        for paper in evals_yes:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
        
        f.write("\n---\n\n")
        
        # Datasets Section
        f.write("## Datasets\n\n")
        f.write(f"**Total: {len(datasets_yes)} papers**\n\n")
        
        for paper in datasets_yes:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
        
        f.write("\n---\n\n")
        
        # Multi-Category Papers
        f.write("## Multi-Category Papers\n\n")
        
        f.write("### All Three Categories (Benchmark + Eval + Dataset)\n\n")
        f.write(f"**Total: {len(all_three)} papers**\n\n")
        for paper in all_three:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
        
        f.write("\n### Benchmark + Eval Only\n\n")
        f.write(f"**Total: {len(bench_eval)} papers**\n\n")
        for paper in bench_eval:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
        
        f.write("\n### Benchmark + Dataset Only\n\n")
        f.write(f"**Total: {len(bench_dataset)} papers**\n\n")
        for paper in bench_dataset:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
        
        f.write("\n### Eval + Dataset Only\n\n")
        f.write(f"**Total: {len(eval_dataset)} papers**\n\n")
        for paper in eval_dataset:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
        
        f.write("\n---\n\n")
        
        # Papers by Description Type
        f.write("## Papers by Description Type\n\n")
        f.write(f"**Total unique descriptions: {len(by_description)}**\n\n")
        
        # Sort descriptions by number of papers (descending)
        sorted_descriptions = sorted(by_description.items(), key=lambda x: len(x[1]), reverse=True)
        
        for description, papers in sorted_descriptions:
            f.write(f"### {description}\n\n")
            f.write(f"**Total: {len(papers)} papers**\n\n")
            for paper in papers:
                f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
                if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                    f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
            f.write("\n")
        
        f.write("---\n\n")
        
        # Papers with Extracted Metrics
        f.write("## Papers with Extracted Metrics\n\n")
        f.write(f"**Total: {len(with_metrics)} papers**\n\n")
        
        for paper in with_metrics:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
        
        f.write("\n---\n\n")
        
        # Papers Not in Any Category
        f.write("## Papers Not in Any Category\n\n")
        f.write(f"**Total: {len(none_of_three)} papers**\n\n")
        f.write("These papers are not classified as benchmarks, evaluations, or datasets.\n\n")
        
        for paper in none_of_three:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
    
    print(f"\nReport generated: {report_path}")
    print(f"Total papers: {len(paper_files)}")
    print(f"Benchmarks: {len(benchmarks_yes)}")
    print(f"Evaluations: {len(evals_yes)}")
    print(f"Datasets: {len(datasets_yes)}")
    print(f"All three: {len(all_three)}")
    print(f"None: {len(none_of_three)}")
    print(f"With metrics: {len(with_metrics)}")
    print(f"Unique descriptions: {len(by_description)}")


if __name__ == '__main__':
    main()
