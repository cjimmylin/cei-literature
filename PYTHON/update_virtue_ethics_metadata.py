#!/usr/bin/env python3
"""Update metadata for virtue ethics papers with local PDF paths."""

import sys
from pathlib import Path

# Use vault_config for paths
from vault_config import PAPERS_DIR, PDFS_DIR

from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)

# Papers to update
PAPERS = [
    "2020-Gabriel-Artificial Intelligence Values and Alignment.md",
    "2025-Unknown-AI Alignment as Fair Treatment of Claims.md",
    "2018-Unknown-The Virtuous Machine - Old Ethics for New.md",
    "2024-Ober-AI Ethics with Aristotle.md",
    "2022-Unknown-A Virtue-Based Framework for AI Ethics in Practice.md",
    "2025-Unknown-LLM Ethics Benchmark - Three-Dimensional.md",
    "2024-Unknown-Ethical Reasoning and Moral Value Alignment.md",
    "2025-Unknown-AMULED - Addressing Moral Uncertainty with LLMs.md",
    "2024-Unknown-Moral Persuasion in Large Language Models.md",
    "2024-Unknown-Differences in Moral Foundations of LLMs.md",
    "2022-Unknown-Towards Artificial Virtuous Agents - Games and ML.md",
    "2024-Unknown-Computational Complexity of Ethics.md",
    "2025-Unknown-AI Practical Wisdom and Compassion.md",
    "2024-Tsai-Why AI May Undermine Phronesis.md",
]


def update_paper(paper_name: str):
    """Update a single paper's metadata with local PDF path."""
    paper_path = PAPERS_DIR / paper_name
    pdf_name = paper_name.replace('.md', '.pdf')
    pdf_path = PDFS_DIR / pdf_name

    if not paper_path.exists():
        print(f"  Paper not found: {paper_name}")
        return False

    if not pdf_path.exists():
        print(f"  PDF not found: {pdf_name}")
        return False

    content = paper_path.read_text(encoding='utf-8', errors='ignore')
    fm, body = extract_frontmatter(content)
    fields = parse_frontmatter(fm)

    # Update local_pdf field
    fields['local_pdf'] = f"[[PDFs/{pdf_name}]]"

    # Also set pdf_extract path
    extract_name = paper_name.replace('.md', '.md')
    fields['pdf_extract'] = f"PDF Extracts/{extract_name}"

    new_fm = rebuild_frontmatter(fields)
    is_valid, issues = validate_frontmatter(new_fm)

    if is_valid:
        write_paper(paper_path, new_fm, body, validate=True)
        return True
    else:
        print(f"  Validation failed: {issues}")
        return False


def main():
    print("Updating virtue ethics paper metadata...")
    updated = 0
    for paper in PAPERS:
        if update_paper(paper):
            print(f"  ✓ {paper}")
            updated += 1
    print(f"\nUpdated {updated}/{len(PAPERS)} papers")


if __name__ == "__main__":
    main()
