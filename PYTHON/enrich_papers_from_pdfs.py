#!/usr/bin/env python3
"""
Enrich Paper Files from PDF Extracts

This script uses extracted PDF text to enrich paper metadata with:
1. Abstracts (extracted from PDF content)
2. Structured summaries (overview, key findings, methodology, conclusions)

It safely updates paper YAML metadata using the utilities library.

Usage:
    python3 enrich_papers_from_pdfs.py                  # Process all papers
    python3 enrich_papers_from_pdfs.py --dry-run        # Preview changes
    python3 enrich_papers_from_pdfs.py --verbose        # Show progress
    python3 enrich_papers_from_pdfs.py "2016-Amodei"    # Process specific paper
"""

import os
import sys
import argparse
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# Import from same directory
from yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)


# Directories - use vault_config
from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR
PAPER_DIR = str(PAPERS_DIR)
EXTRACT_DIR = str(PDF_EXTRACTS_DIR)


class EnrichmentStats:
    """Track enrichment statistics."""
    def __init__(self):
        self.processed = 0
        self.abstracts_added = 0
        self.summaries_generated = 0
        self.errors = []
        self.skipped = 0

    def report(self):
        logger.info("=" * 60)
        logger.info("ENRICHMENT SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Papers processed: {self.processed}")
        logger.info(f"Abstracts extracted/added: {self.abstracts_added}")
        logger.info(f"Summaries generated: {self.summaries_generated}")
        logger.info(f"Papers skipped: {self.skipped}")
        logger.info(f"Errors: {len(self.errors)}")

        if self.errors:
            logger.info("Errors encountered:")
            for paper, error in self.errors:
                logger.error(f"  - {paper}: {error}")


stats = EnrichmentStats()


def extract_abstract_from_text(text):
    """
    Extract abstract section from PDF text.

    Returns: Abstract text (first 300-500 chars of relevant content)
    """
    # Look for "Abstract" section
    abstract_match = re.search(
        r'(?:Abstract|ABSTRACT)[:\s]*\n(.*?)(?:\n(?:1\.|Introduction|INTRODUCTION|$))',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if abstract_match:
        abstract_text = abstract_match.group(1).strip()
        # Clean up extra whitespace and newlines
        abstract_text = re.sub(r'\s+', ' ', abstract_text)
        # Remove quotes to avoid YAML issues
        abstract_text = abstract_text.replace('"', "'")
        # Limit to reasonable length
        abstract_text = abstract_text[:500]
        return abstract_text

    return None


def extract_key_sections(text):
    """
    Extract key sections and their content from PDF text.

    Returns: Dictionary with identified sections
    """
    sections = {}

    # Common section patterns
    section_patterns = {
        'methodology': r'(?:Method|Methodology|Approach)[:\s]*\n(.*?)(?:\n(?:\d\.|Conclusion|Result|$))',
        'results': r'(?:Result|Finding|Evaluation)[:\s]*\n(.*?)(?:\n(?:\d\.|Conclusion|Discussion|$))',
        'conclusion': r'(?:Conclusion|Discussion)[:\s]*\n(.*?)(?:\n(?:\d\.|Future|$))',
    }

    for section_name, pattern in section_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            content = match.group(1).strip()
            # Clean whitespace
            content = re.sub(r'\s+', ' ', content)
            # Limit length
            sections[section_name] = content[:300]

    return sections


def generate_summary(paper_stem, pdf_extract_path):
    """
    Generate a structured summary from PDF extract.

    Returns: Dictionary with summary sections or None if extract not found
    """
    if not os.path.exists(pdf_extract_path):
        return None

    try:
        with open(pdf_extract_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract the PDF text (between the code block markers)
        text_match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
        if not text_match:
            return None

        pdf_text = text_match.group(1)

        # Extract abstract
        abstract = extract_abstract_from_text(pdf_text)

        # Extract key sections
        sections = extract_key_sections(pdf_text)

        # Create summary
        summary = {
            'abstract': abstract,
            'overview': extract_overview(pdf_text),
            'methodology': sections.get('methodology'),
            'key_findings': sections.get('results'),
            'conclusions': sections.get('conclusion'),
        }

        return summary

    except Exception as e:
        stats.errors.append((paper_stem, f"Error generating summary: {e}"))
        return None


def extract_overview(text):
    """Extract an overview/introduction snippet."""
    # Get first meaningful paragraph after title
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        if len(para) > 100 and not para.startswith('---'):
            # Clean it up
            para_clean = re.sub(r'\s+', ' ', para.strip())
            return para_clean[:400]
    return None


def format_summary_for_yaml(summary_dict):
    """
    Format summary dictionary for YAML inclusion.

    Returns: YAML-safe string representation with proper quote escaping
    """
    if not summary_dict:
        return None

    parts = []

    if summary_dict.get('abstract'):
        # Strip and limit abstract
        abstract = summary_dict['abstract'][:200] if summary_dict['abstract'] else ""
        parts.append(f"Abstract: {abstract}")

    if summary_dict.get('overview'):
        overview = summary_dict['overview'][:200] if summary_dict['overview'] else ""
        parts.append(f"Overview: {overview}")

    if summary_dict.get('methodology'):
        methodology = summary_dict['methodology'][:150] if summary_dict['methodology'] else ""
        parts.append(f"Methodology: {methodology}")

    if summary_dict.get('key_findings'):
        findings = summary_dict['key_findings'][:150] if summary_dict['key_findings'] else ""
        parts.append(f"Key Findings: {findings}")

    if summary_dict.get('conclusions'):
        conclusions = summary_dict['conclusions'][:150] if summary_dict['conclusions'] else ""
        parts.append(f"Conclusions: {conclusions}")

    # Join with pipe separator
    formatted = ' | '.join(parts)

    # Remove problematic quotes to avoid YAML issues
    formatted = formatted.replace('"', "'")
    formatted = formatted.replace('\n', ' ')

    return formatted


def enrich_paper(paper_path, dry_run=False, verbose=False):
    """
    Enrich a single paper file with PDF extract content.

    Returns: (success, changes_made)
    """
    paper_stem = os.path.splitext(os.path.basename(paper_path))[0]
    extract_path = os.path.join(EXTRACT_DIR, paper_stem + ".md")

    try:
        # Read paper
        content = paper_path.read_text(encoding='utf-8')
        fm, body = extract_frontmatter(content)

        # Validate input
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            if verbose:
                logger.debug(f"  SKIP {paper_stem}: Already has YAML issues")
            stats.skipped += 1
            return False, 0

        fields = parse_frontmatter(fm)
        changes = 0

        # 1. Add abstract if missing
        if not fields.get('abstract') and os.path.exists(extract_path):
            summary = generate_summary(paper_stem, extract_path)
            if summary and summary.get('abstract'):
                fields['abstract'] = summary['abstract']
                changes += 1
                if verbose:
                    logger.debug(f"  Added abstract to {paper_stem}")

        # 2. Add structured summary if missing
        if not fields.get('paper_summary') and os.path.exists(extract_path):
            summary = generate_summary(paper_stem, extract_path)
            if summary:
                formatted_summary = format_summary_for_yaml(summary)
                if formatted_summary:
                    fields['paper_summary'] = formatted_summary
                    changes += 1
                    if verbose:
                        logger.debug(f"  Generated summary for {paper_stem}")

        if changes == 0:
            if verbose:
                logger.debug(f"  {paper_stem}: No enrichment needed")
            stats.skipped += 1
            return False, 0

        # Rebuild and validate
        new_fm = rebuild_frontmatter(fields)
        is_valid, issues = validate_frontmatter(new_fm)
        if not is_valid:
            stats.errors.append((paper_stem, f"YAML validation failed: {issues}"))
            return False, 0

        if dry_run:
            if verbose:
                logger.info(f"  [DRY RUN] Would enrich {paper_stem} ({changes} changes)")
            return True, changes

        # Write safely
        write_paper(paper_path, new_fm, body, validate=True)

        stats.processed += 1
        if changes >= 1:
            stats.abstracts_added += 1
        if changes >= 2:
            stats.summaries_generated += 1

        return True, changes

    except Exception as e:
        stats.errors.append((paper_stem, str(e)))
        return False, 0


def enrich_all_papers(target_paper=None, dry_run=False, verbose=False):
    """
    Enrich all papers or a specific paper.

    Args:
        target_paper: Optional paper stem to process
        dry_run: If True, don't write files
        verbose: If True, show detailed progress
    """
    if not os.path.exists(PAPER_DIR):
        logger.error(f"Error: Papers directory '{PAPER_DIR}' not found")
        sys.exit(1)

    if target_paper:
        # Process single paper
        paper_path = Path(PAPER_DIR) / (target_paper + ".md")
        if not paper_path.exists():
            logger.error(f"Error: Paper '{target_paper}.md' not found")
            sys.exit(1)

        logger.info(f"Enriching: {target_paper}")
        enrich_paper(paper_path, dry_run, verbose)
    else:
        # Process all papers
        papers = sorted(Path(PAPER_DIR).glob("*.md"))
        total = len(papers)

        logger.info(f"Found {total} papers to enrich")

        for i, paper_path in enumerate(papers, 1):
            if verbose or i % 50 == 0:
                logger.info(f"[{i}/{total}] {paper_path.name}")

            enrich_paper(paper_path, dry_run, verbose)

    stats.report()


def main():
    parser = argparse.ArgumentParser(
        description="Enrich papers with information from PDF extracts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 enrich_papers_from_pdfs.py                # Enrich all papers
  python3 enrich_papers_from_pdfs.py --dry-run      # Preview changes
  python3 enrich_papers_from_pdfs.py --verbose      # Show progress
  python3 enrich_papers_from_pdfs.py "2016-Amodei"  # Enrich specific paper
        """
    )
    parser.add_argument('paper', nargs='?', help='Specific paper stem to enrich')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help="Don't write files, just show what would happen")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Show detailed progress information")

    args = parser.parse_args()

    if args.dry_run:
        logger.info("=" * 60)
        logger.info("DRY RUN MODE - No files will be modified")
        logger.info("=" * 60)

    enrich_all_papers(
        target_paper=args.paper,
        dry_run=args.dry_run,
        verbose=args.verbose
    )


if __name__ == "__main__":
    main()
