#!/usr/bin/env python3
"""
Enhanced Paper Validation Script

Goes beyond basic YAML validation to catch:
1. YAML syntax issues (orphaned list items, mismatched quotes)
2. Unquoted local_pdf fields (Obsidian wikilinks need quotes)
3. Content mismatch indicators ([!WARNING] boxes)
4. Missing critical metadata fields
5. Pipe-delimited paper_summary (extraction artifacts)
6. Suspicious abstract content (wrong paper indicators)

Usage:
    python3 PYTHON/validate_papers_enhanced.py [--fix] [--verbose]

Options:
    --fix      Attempt to auto-fix issues where possible
    --verbose  Show all checks, not just failures
"""

import re
import sys
import logging
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import extract_frontmatter, validate_frontmatter, parse_frontmatter
from vault_config import PAPERS_DIR, WORKSPACE_ROOT


class EnhancedValidator:
    """Enhanced paper validation with multiple check types"""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.results = {
            'total': 0,
            'valid': 0,
            'warnings': 0,
            'errors': 0,
            'issues': []
        }

    def check_unquoted_wikilinks(self, frontmatter: str) -> List[str]:
        """Check for unquoted [[...]] in YAML fields"""
        issues = []
        # Pattern for unquoted wikilinks in common fields
        patterns = [
            (r'^local_pdf:\s*\[\[', 'local_pdf has unquoted wikilink'),
            (r'^pdf_extract:\s*\[\[', 'pdf_extract has unquoted wikilink'),
            (r'^first_author:\s*\[\[', 'first_author has unquoted wikilink'),
        ]
        for pattern, message in patterns:
            if re.search(pattern, frontmatter, re.MULTILINE):
                issues.append(message)
        return issues

    def check_warning_boxes(self, content: str) -> List[str]:
        """Check for [!WARNING] boxes indicating known issues"""
        issues = []
        if '[!WARNING]' in content:
            issues.append("Contains [!WARNING] box - known issue flagged")
        return issues

    def check_pipe_delimited_summary(self, fm_dict: Dict) -> List[str]:
        """Check for extraction artifacts in paper_summary"""
        issues = []
        summary = fm_dict.get('paper_summary', '')
        if summary.count(' | ') >= 2:
            issues.append("paper_summary has pipe-delimited extraction artifacts")
        return issues

    def check_suspicious_abstract(self, fm_dict: Dict) -> List[str]:
        """Check for known corruption patterns in abstract"""
        issues = []
        abstract = fm_dict.get('abstract', '').lower()
        paper_summary = fm_dict.get('paper_summary', '').lower()
        title = fm_dict.get('short_title', '').lower()

        # Known corruption patterns from past issues (Session 8)
        corruption_patterns = [
            ('einstein-podolsky-rosen', 'quantum physics text corruption'),
            ('higher-order pattern unification', 'pattern unification paper'),
            ('public financial management', 'PFM paper contamination'),
            ('solution numbers for eight blocks', 'puzzle paper contamination'),
            ('contraction∗-depth', 'matroid depth paper contamination'),
            ('matroid', 'possible matroid paper contamination'),
            ('winogender schemas', 'possible Rudinger/Zhao paper mix-up'),
        ]

        for pattern, issue_type in corruption_patterns:
            if pattern in abstract:
                issues.append(f"Suspicious abstract content: {issue_type}")
            if pattern in paper_summary:
                issues.append(f"Suspicious paper_summary content: {issue_type}")

        # Check for abstract/title mismatch indicators
        # If title mentions ethics/AI but abstract mentions unrelated math terms
        ethics_keywords = ['ethics', 'moral', 'alignment', 'bias', 'fairness', 'virtue']
        math_keywords = ['theorem', 'lemma', 'proof', 'matroid', 'polynomial']

        title_has_ethics = any(kw in title for kw in ethics_keywords)
        abstract_has_math = any(kw in abstract for kw in math_keywords)

        if title_has_ethics and abstract_has_math:
            issues.append("Title/abstract domain mismatch: ethics title with math abstract")

        return issues

    def check_critical_fields(self, fm_dict: Dict) -> List[str]:
        """Check for missing or invalid critical fields"""
        issues = []
        critical_fields = {
            'abstract': 'Missing abstract',
            'authors': 'Missing authors',
            'year': 'Missing year',
            'type': 'Missing document type',
        }

        for field, message in critical_fields.items():
            value = fm_dict.get(field, '')
            if not value or value in ['N/A', '', 'null', 'None']:
                issues.append(message)

        # Check year is valid
        year = fm_dict.get('year', '')
        if year and not re.match(r'^(19|20)\d{2}$', str(year)):
            issues.append(f"Invalid year format: {year}")

        # Check ethics score fields are present and valid
        ethics_score_fields = ['ethics_overall', 'virtue_ethics', 'deontological_ethics',
                               'utilitarian_ethics', 'care_ethics', 'contractarian_ethics']
        for field in ethics_score_fields:
            value = fm_dict.get(field)
            if value is not None and str(value).strip() not in ('', 'Yes', 'No', 'Unknown'):
                try:
                    n = int(value)
                    if not (0 <= n <= 100):
                        issues.append(f"Ethics score out of range for '{field}': {value}")
                except (ValueError, TypeError):
                    issues.append(f"Invalid ethics score for '{field}': {value}")

        return issues

    def check_author_format(self, fm_dict: Dict) -> List[str]:
        """Check author field formatting"""
        issues = []
        authors = fm_dict.get('authors', '')

        # Check for incomplete placeholders
        if 'and others' in authors.lower() and '**' in authors:
            issues.append("Authors field has incomplete placeholder")

        return issues

    def validate_paper(self, paper_path: Path) -> Dict:
        """Run all validation checks on a single paper"""
        result = {
            'path': str(paper_path),
            'name': paper_path.name,
            'errors': [],
            'warnings': [],
            'info': []
        }

        try:
            content = paper_path.read_text(encoding='utf-8')
            frontmatter, body = extract_frontmatter(content)

            # Level 1: Basic YAML validation
            is_valid, yaml_issues = validate_frontmatter(frontmatter)
            if not is_valid:
                result['errors'].extend([f"YAML: {i}" for i in yaml_issues])

            # Parse frontmatter for field-level checks
            fm_dict = parse_frontmatter(frontmatter)

            # Level 2: Wikilink quoting
            wikilink_issues = self.check_unquoted_wikilinks(frontmatter)
            result['errors'].extend(wikilink_issues)

            # Level 3: Warning boxes (indicates known issues)
            warning_issues = self.check_warning_boxes(content)
            result['warnings'].extend(warning_issues)

            # Level 4: Suspicious content
            suspicious_issues = self.check_suspicious_abstract(fm_dict)
            result['warnings'].extend(suspicious_issues)

            # Level 5: Critical fields
            field_issues = self.check_critical_fields(fm_dict)
            result['errors'].extend(field_issues)

            # Level 6: Author format
            author_issues = self.check_author_format(fm_dict)
            result['warnings'].extend(author_issues)

            # Level 7: Extraction artifacts (info only)
            summary_issues = self.check_pipe_delimited_summary(fm_dict)
            result['info'].extend(summary_issues)

        except Exception as e:
            result['errors'].append(f"Parse error: {str(e)}")

        return result

    def run_validation(self, papers_dir: Path) -> Dict:
        """Run validation on all papers"""
        papers = sorted(papers_dir.glob('*.md'))
        self.results['total'] = len(papers)

        logger.info(f"Enhanced validation of {len(papers)} papers...\n")

        for i, paper in enumerate(papers, 1):
            if i % 100 == 0:
                logger.info(f"  Progress: {i}/{len(papers)}")

            result = self.validate_paper(paper)

            if not result['errors'] and not result['warnings']:
                self.results['valid'] += 1
            if result['errors']:
                self.results['errors'] += 1
            if result['warnings']:
                self.results['warnings'] += 1

            # Store papers with issues
            if result['errors'] or result['warnings'] or (self.verbose and result['info']):
                self.results['issues'].append(result)

        return self.results

    def print_report(self):
        """Print validation report"""
        r = self.results

        logger.info("\n" + "=" * 60)
        logger.info("ENHANCED VALIDATION REPORT")
        logger.info("=" * 60)

        logger.info(f"\nTotal papers: {r['total']}")
        logger.info(f"Clean papers: {r['valid']}")
        logger.info(f"Papers with errors: {r['errors']}")
        logger.info(f"Papers with warnings: {r['warnings']}")

        if r['issues']:
            # Group by severity
            errors = [i for i in r['issues'] if i['errors']]
            warnings = [i for i in r['issues'] if i['warnings'] and not i['errors']]

            if errors:
                logger.info("\n" + "-" * 60)
                logger.info(f"ERRORS ({len(errors)} papers)")
                logger.info("-" * 60)
                for paper in errors[:20]:  # Limit output
                    logger.info(f"\n{paper['name']}:")
                    for e in paper['errors']:
                        logger.error(f"  [ERROR] {e}")
                if len(errors) > 20:
                    logger.info(f"\n  ... and {len(errors) - 20} more")

            if warnings:
                logger.info("\n" + "-" * 60)
                logger.info(f"WARNINGS ({len(warnings)} papers)")
                logger.info("-" * 60)
                for paper in warnings[:10]:
                    logger.info(f"\n{paper['name']}:")
                    for w in paper['warnings']:
                        logger.warning(f"  [WARN] {w}")
                if len(warnings) > 10:
                    logger.info(f"\n  ... and {len(warnings) - 10} more")
        else:
            logger.info("\n✓ All papers passed enhanced validation!")

        logger.info("\n" + "=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Enhanced paper validation')
    parser.add_argument('--fix', action='store_true', help='Auto-fix issues where possible')
    parser.add_argument('--verbose', action='store_true', help='Show all checks')
    args = parser.parse_args()

    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        logger.error(f"Error: papers directory not found at {papers_dir}")
        sys.exit(1)

    validator = EnhancedValidator(verbose=args.verbose)
    results = validator.run_validation(papers_dir)
    validator.print_report()

    # If --fix requested and there are fixable issues
    if args.fix and results['errors'] > 0:
        logger.info("\nAttempting auto-fixes...")
        # Run the fix scripts
        import subprocess
        fix_script = WORKSPACE_ROOT / 'PYTHON' / 'fix_unquoted_local_pdf.py'
        if fix_script.exists():
            subprocess.run([sys.executable, str(fix_script)])
            logger.info("Re-running validation...")
            validator2 = EnhancedValidator(verbose=args.verbose)
            validator2.run_validation(papers_dir)
            validator2.print_report()

    sys.exit(1 if results['errors'] > 0 else 0)


if __name__ == '__main__':
    main()
