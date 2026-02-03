#!/usr/bin/env python3
"""
Generate statistics report for data nature classification.
Creates a markdown report showing papers categorized by benchmark/eval/dataset status.

This script generates data-nature-statistics.md (1,604 lines), a focused report containing:
- Summary statistics and category overlaps
- All benchmarks with descriptions and metrics
- All evaluation papers with descriptions and metrics
- All datasets with descriptions and metrics
- Papers with extracted metrics (detailed list)

This report is more detailed than paper-statistics-3.md but less comprehensive in
organization. Use this for quick reference, use paper-statistics-3.md for full breakdown.

OUTPUT FORMAT:
- Year - Author - [[Wikilink to paper]]
- Description (when available)
- Metrics (when extracted)

USAGE:
python3 generate_data_report.py
"""

import re
from pathlib import Path
from typing import Dict

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
    """Generate the statistics report."""
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        return
    
    # Storage for categorized papers
    benchmarks = []
    evals = []
    datasets = []
    papers_with_metrics = []
    all_papers = []
    
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
            
            all_papers.append(paper_entry)
            
            if is_benchmark == 'Yes':
                benchmarks.append(paper_entry)
            if is_eval == 'Yes':
                evals.append(paper_entry)
            if is_dataset == 'Yes':
                datasets.append(paper_entry)
            if data_metrics not in ['Not specified', 'Unknown', '']:
                papers_with_metrics.append(paper_entry)
                
        except Exception as e:
            print(f"Error processing {filepath.name}: {e}")
    
    # Generate markdown report
    report_path = STATISTICS_DIR / 'data-nature-statistics.md'

    # Ensure STATISTICS directory exists
    STATISTICS_DIR.mkdir(exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Data Nature Classification Statistics\n\n")
        f.write(f"**Report Generated:** {Path(__file__).name}\n\n")
        f.write(f"Total papers analyzed: **{len(all_papers)}**\n\n")
        
        f.write("## Summary Statistics\n\n")
        f.write(f"- **Benchmarks**: {len(benchmarks)} papers\n")
        f.write(f"- **Evaluation Papers**: {len(evals)} papers\n")
        f.write(f"- **Datasets**: {len(datasets)} papers\n")
        f.write(f"- **Papers with Metrics**: {len(papers_with_metrics)} papers\n\n")
        
        # Calculate overlaps
        both_bench_eval = sum(1 for p in all_papers if p['is_benchmark'] == 'Yes' and p['is_eval'] == 'Yes')
        both_bench_dataset = sum(1 for p in all_papers if p['is_benchmark'] == 'Yes' and p['is_dataset'] == 'Yes')
        both_eval_dataset = sum(1 for p in all_papers if p['is_eval'] == 'Yes' and p['is_dataset'] == 'Yes')
        all_three = sum(1 for p in all_papers if p['is_benchmark'] == 'Yes' and p['is_eval'] == 'Yes' and p['is_dataset'] == 'Yes')
        
        f.write("### Category Overlaps\n\n")
        f.write(f"- Benchmark + Eval: **{both_bench_eval}**\n")
        f.write(f"- Benchmark + Dataset: **{both_bench_dataset}**\n")
        f.write(f"- Eval + Dataset: **{both_eval_dataset}**\n")
        f.write(f"- All three: **{all_three}**\n\n")
        
        # Benchmarks section
        f.write("---\n\n")
        f.write("## Benchmarks\n\n")
        f.write(f"**Total: {len(benchmarks)} papers**\n\n")
        
        for paper in benchmarks:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
        
        # Evaluations section
        f.write("\n---\n\n")
        f.write("## Evaluation Papers\n\n")
        f.write(f"**Total: {len(evals)} papers**\n\n")
        
        for paper in evals:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
        
        # Datasets section
        f.write("\n---\n\n")
        f.write("## Datasets\n\n")
        f.write(f"**Total: {len(datasets)} papers**\n\n")
        
        for paper in datasets:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            if paper['data_metrics'] not in ['Not specified', 'Unknown']:
                f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
            if paper['data_description'] not in ['N/A', 'Unknown']:
                f.write(f"  - *Description*: {paper['data_description']}\n")
        
        # Papers with extracted metrics
        f.write("\n---\n\n")
        f.write("## Papers with Extracted Metrics\n\n")
        f.write(f"**Total: {len(papers_with_metrics)} papers**\n\n")
        
        for paper in papers_with_metrics:
            f.write(f"- {paper['year']} - {paper['author']} - [[{paper['filename']}|{paper['title']}]]\n")
            f.write(f"  - *Metrics*: {paper['data_metrics']}\n")
    
    print(f"\nReport generated: {report_path}")
    print(f"Total papers: {len(all_papers)}")
    print(f"Benchmarks: {len(benchmarks)}")
    print(f"Evaluations: {len(evals)}")
    print(f"Datasets: {len(datasets)}")
    print(f"Papers with metrics: {len(papers_with_metrics)}")


if __name__ == '__main__':
    main()
