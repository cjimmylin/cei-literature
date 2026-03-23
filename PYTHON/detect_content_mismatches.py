#!/usr/bin/env python3
"""
Detect Content Mismatches in Paper Files

This script identifies papers where the PDF/extract content doesn't match
the metadata (title, authors, abstract). This catches issues like:
- Wrong PDF downloaded for a paper
- arXiv ID transposition errors
- Papers with same titles by different authors

Key detection methods:
1. Check for [!WARNING] boxes in paper files
2. Compare author names between abstract and metadata
3. Check if pdf_extract content mentions different authors/titles
4. Detect pipe-delimited paper_summary as extraction artifacts
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple
import sys

sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter


def check_warning_boxes(content: str) -> List[str]:
    """Check for [!WARNING] boxes in the file"""
    warnings = []
    warning_pattern = r'>\s*\[!WARNING\].*?(?=\n[^>]|\Z)'
    matches = re.findall(warning_pattern, content, re.DOTALL)
    for match in matches:
        # Extract the warning text
        text = re.sub(r'^>\s*', '', match, flags=re.MULTILINE).strip()
        warnings.append(text)
    return warnings


def check_unquoted_local_pdf(frontmatter: str) -> bool:
    """Check if local_pdf field has unquoted [[...]] syntax"""
    pattern = r'^local_pdf:\s*\[\[Lit-WS-PDFs/'
    return bool(re.search(pattern, frontmatter, re.MULTILINE))


def check_pipe_delimited_summary(frontmatter_dict: Dict) -> bool:
    """Check if paper_summary has pipe-delimited extraction artifacts"""
    summary = frontmatter_dict.get('paper_summary', '')
    # Count pipe characters - more than 2 suggests extraction artifacts
    pipe_count = summary.count(' | ')
    return pipe_count >= 2


def check_truncated_abstract(frontmatter_dict: Dict) -> Tuple[bool, str]:
    """Check if abstract appears to be truncated mid-word"""
    abstract = frontmatter_dict.get('abstract', '')
    if not abstract:
        return False, ""

    # Remove trailing quotes if present
    abstract = abstract.rstrip('"').rstrip()

    # Check if ends with lowercase letters (mid-word)
    if re.search(r'[a-z]{2,}$', abstract) and not abstract.endswith('.'):
        return True, f"Abstract may be truncated (ends with: ...{abstract[-20:]})"

    return False, ""


def check_suspicious_content_patterns(frontmatter_dict: Dict) -> List[str]:
    """Check for known wrong-content patterns from past issues"""
    issues = []
    abstract = frontmatter_dict.get('abstract', '').lower()
    summary = frontmatter_dict.get('paper_summary', '').lower()

    # Known contamination patterns from Session 8
    contamination_patterns = [
        ('contraction∗-depth', 'matroid paper content'),
        ('matroid representable', 'matroid paper content'),
        ('higher-order pattern unification', 'unification paper content'),
        ('public financial management', 'PFM paper content'),
        ('solution numbers for eight blocks', 'puzzle paper content'),
        ('einstein-podolsky-rosen', 'quantum physics contamination'),
        ('winogender schemas', 'possible Zhao/Rudinger confusion'),
    ]

    for pattern, issue_type in contamination_patterns:
        if pattern in abstract or pattern in summary:
            issues.append(f"Suspicious content: {issue_type}")

    return issues


def extract_author_from_content(content: str) -> List[str]:
    """Try to extract author names from body content"""
    authors = []
    # Look for "by Author Name" or "Author Name et al."
    patterns = [
        r'by\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)',
        r'([A-Z][a-z]+(?:\s+[A-Z]\.?\s+)?[A-Z][a-z]+)\s+et\s+al\.',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, content[:2000])  # First 2000 chars
        authors.extend(matches)
    return authors


def compare_author_names(metadata_authors: str, content_authors: List[str]) -> bool:
    """Check if content authors match metadata authors"""
    if not content_authors:
        return True  # Can't determine mismatch without content authors

    # Normalize metadata authors
    meta_names = set()
    for author in re.split(r'[;,]', metadata_authors):
        # Extract last name
        parts = author.strip().split()
        if parts:
            meta_names.add(parts[-1].lower().strip('[]'))

    # Check if any content author matches
    for author in content_authors:
        parts = author.split()
        if parts:
            last_name = parts[-1].lower()
            if last_name in meta_names:
                return True

    return len(content_authors) == 0  # No mismatch if no content authors found


def check_pdf_extract_mismatch(paper_path: Path, frontmatter_dict: Dict) -> Tuple[bool, str]:
    """Check if PDF extract content matches paper metadata"""
    pdf_extract_path = frontmatter_dict.get('pdf_extract', '')
    if not pdf_extract_path or pdf_extract_path == 'N/A':
        return False, ""

    # Clean up path
    pdf_extract_path = pdf_extract_path.strip('"').strip("'")
    extract_file = paper_path.parent.parent / pdf_extract_path

    if not extract_file.exists():
        return False, ""

    try:
        extract_content = extract_file.read_text(encoding='utf-8')[:5000]

        # Get expected author from paper metadata
        expected_author = frontmatter_dict.get('first_author', '').strip('[]"')
        if expected_author:
            # Check if expected author appears in extract
            author_parts = expected_author.split()
            if author_parts:
                last_name = author_parts[-1]
                if last_name.lower() not in extract_content.lower():
                    # Author not found - potential mismatch
                    # Look for other author names in extract
                    found_authors = extract_author_from_content(extract_content)
                    if found_authors:
                        return True, f"Expected author '{last_name}' not found; found: {found_authors[:3]}"
    except Exception:
        pass

    return False, ""


def audit_paper(paper_path: Path) -> Dict:
    """Audit a single paper for potential issues"""
    issues = {
        'path': str(paper_path),
        'name': paper_path.name,
        'warnings': [],
        'errors': [],
        'info': []
    }

    try:
        content = paper_path.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)
        fm_dict = parse_frontmatter(frontmatter)

        # Check 1: Existing WARNING boxes
        warnings = check_warning_boxes(content)
        if warnings:
            issues['warnings'].append(f"Has {len(warnings)} [!WARNING] box(es)")

        # Check 2: Unquoted local_pdf
        if check_unquoted_local_pdf(frontmatter):
            issues['errors'].append("Unquoted local_pdf field (YAML syntax issue)")

        # Check 3: Pipe-delimited paper_summary
        if check_pipe_delimited_summary(fm_dict):
            issues['info'].append("Paper_summary has pipe-delimited extraction artifacts")

        # Check 4: PDF extract content mismatch
        has_mismatch, mismatch_detail = check_pdf_extract_mismatch(paper_path, fm_dict)
        if has_mismatch:
            issues['warnings'].append(f"Possible content mismatch: {mismatch_detail}")

        # Check 5: Missing critical fields
        critical_fields = ['abstract', 'authors', 'year', 'type']
        for field in critical_fields:
            value = fm_dict.get(field, '')
            if not value or value in ['N/A', '']:
                issues['errors'].append(f"Missing or empty field: {field}")

        # Check 6: Truncated abstract
        is_truncated, truncation_detail = check_truncated_abstract(fm_dict)
        if is_truncated:
            issues['info'].append(truncation_detail)

        # Check 7: Suspicious content patterns (wrong paper contamination)
        suspicious_patterns = check_suspicious_content_patterns(fm_dict)
        issues['warnings'].extend(suspicious_patterns)

    except Exception as e:
        issues['errors'].append(f"Failed to parse: {e}")

    return issues


def run_full_audit(papers_dir: Path) -> Dict:
    """Run audit on all papers"""
    results = {
        'total': 0,
        'with_warnings': 0,
        'with_errors': 0,
        'with_info': 0,
        'papers': []
    }

    papers = sorted(papers_dir.glob('*.md'))
    results['total'] = len(papers)

    print(f"Auditing {len(papers)} papers for content mismatches...\n")

    for i, paper in enumerate(papers, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(papers)}")

        issues = audit_paper(paper)

        if issues['warnings']:
            results['with_warnings'] += 1
        if issues['errors']:
            results['with_errors'] += 1
        if issues['info']:
            results['with_info'] += 1

        # Only store papers with issues
        if issues['warnings'] or issues['errors']:
            results['papers'].append(issues)

    return results


def print_report(results: Dict):
    """Print audit report"""
    print("\n" + "=" * 60)
    print("CONTENT MISMATCH AUDIT REPORT")
    print("=" * 60)

    print(f"\nTotal papers scanned: {results['total']}")
    print(f"Papers with errors: {results['with_errors']}")
    print(f"Papers with warnings: {results['with_warnings']}")
    print(f"Papers with info notices: {results['with_info']}")

    if results['papers']:
        print("\n" + "-" * 60)
        print("PAPERS REQUIRING ATTENTION")
        print("-" * 60)

        for paper in results['papers']:
            print(f"\n{paper['name']}:")
            for error in paper['errors']:
                print(f"  [ERROR] {error}")
            for warning in paper['warnings']:
                print(f"  [WARNING] {warning}")
    else:
        print("\n✓ No content mismatches or errors detected!")

    print("\n" + "=" * 60)


def main():
    from vault_config import PAPERS_DIR
    papers_dir = PAPERS_DIR

    if not papers_dir.exists():
        print(f"Error: papers directory not found at {papers_dir}")
        sys.exit(1)

    results = run_full_audit(papers_dir)
    print_report(results)

    # Exit with error code if issues found
    sys.exit(1 if results['with_errors'] > 0 else 0)


if __name__ == '__main__':
    main()
