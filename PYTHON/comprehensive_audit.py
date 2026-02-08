#!/usr/bin/env python3
"""
Comprehensive Paper Audit Script
Checks for errors, broken links, missing information, duplicates, and quality issues
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Add project root for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from PYTHON.yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter
from PYTHON.vault_config import PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, AUTHORS_DIR, WORKSPACE_ROOT

# Required fields for all papers
REQUIRED_FIELDS = [
    'key', 'type', 'year', 'first_author', 'authors',
    'ethics_overall', 'is_benchmark', 'is_eval', 'is_dataset'
]

# Fields that should not be empty if present
NON_EMPTY_FIELDS = ['abstract', 'title', 'short_title', 'doi', 'url']

# Valid values for certain fields
VALID_VALUES = {
    'ethics_overall': ['Yes', 'No'],
    'virtue_ethics': ['Yes', 'No'],
    'deontological_ethics': ['Yes', 'No'],
    'utilitarian_ethics': ['Yes', 'No'],
    'is_benchmark': ['Yes', 'No', 'N/A', 'Unknown'],
    'is_eval': ['Yes', 'No', 'N/A', 'Unknown'],
    'is_dataset': ['Yes', 'No', 'N/A', 'Unknown'],
    'type': ['journalArticle', 'preprint', 'conferencePaper', 'bookSection',
             'report', 'thesis', 'book', 'webpage', 'document', 'presentation']
}


class AuditResult:
    def __init__(self):
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.info = defaultdict(list)

    def add_error(self, category, message, paper=None):
        if paper:
            self.errors[category].append(f"{paper}: {message}")
        else:
            self.errors[category].append(message)

    def add_warning(self, category, message, paper=None):
        if paper:
            self.warnings[category].append(f"{paper}: {message}")
        else:
            self.warnings[category].append(message)

    def add_info(self, category, message, paper=None):
        if paper:
            self.info[category].append(f"{paper}: {message}")
        else:
            self.info[category].append(message)


def get_wikilink_target(value):
    """Extract target from wikilink format [[target]]"""
    if not value:
        return None
    match = re.match(r'\[\[(.+?)\]\]', str(value))
    return match.group(1) if match else None


def extract_all_wikilinks(text):
    """Extract all wikilinks from text"""
    return re.findall(r'\[\[([^\]]+)\]\]', text)


def check_pdf_link(local_pdf, paper_name):
    """Check if local_pdf wikilink is valid"""
    if not local_pdf:
        return None, None

    target = get_wikilink_target(local_pdf)
    if not target:
        return "Invalid wikilink format", local_pdf

    # Check if file exists
    pdf_path = PDFS_DIR / Path(target).name
    if not pdf_path.exists():
        # Also try just the filename
        if target.startswith("PDFs/"):
            pdf_path = PDFS_DIR / target[5:]
        if not pdf_path.exists():
            return "PDF file not found", target

    return None, target


def check_pdf_extract_link(pdf_extract, paper_name):
    """Check if pdf_extract link is valid"""
    if not pdf_extract:
        return None, None

    target = pdf_extract.strip('"').strip("'")
    if target.startswith("[[") and target.endswith("]]"):
        target = target[2:-2]

    # Handle both formats
    extract_path = PDF_EXTRACTS_DIR / Path(target).name
    if not extract_path.exists():
        if target.startswith("PDF Extracts/"):
            extract_path = PDF_EXTRACTS_DIR / target[13:]
        if not extract_path.exists():
            return "PDF extract file not found", target

    return None, target


def check_author_links(authors_text, body_text):
    """Check author wikilinks in body"""
    issues = []
    wikilinks = extract_all_wikilinks(body_text)

    # Filter to likely author links (in Authors section or first_author)
    author_section_match = re.search(r'## Authors\s*\n([^\n#]+)', body_text)
    if author_section_match:
        author_links = extract_all_wikilinks(author_section_match.group(1))
        for link in author_links:
            # Check if author file exists
            author_file = AUTHORS_DIR / f"{link}.md"
            if not author_file.exists():
                issues.append(f"Author file not found: {link}")

    return issues


def check_abstract_quality(abstract, paper_name):
    """Check abstract for quality issues"""
    issues = []

    if not abstract:
        issues.append("Missing abstract")
        return issues

    abstract = str(abstract).strip()

    # Check for truncation
    if abstract.endswith('...') or len(abstract) < 100:
        issues.append(f"Abstract may be truncated (length: {len(abstract)})")

    # Check for placeholder text
    placeholders = ['No abstract available', 'Abstract not available', 'N/A', 'TBD']
    if any(p.lower() in abstract.lower() for p in placeholders):
        issues.append("Abstract contains placeholder text")

    # Check for corrupted content (quantum physics text)
    corruption_markers = ['Einstein-Podolsky-Rosen', 'quantum teleportation', 'entangled particles']
    if any(m.lower() in abstract.lower() for m in corruption_markers):
        issues.append("Abstract may contain corrupted content (quantum physics text)")

    return issues


def check_duplicate_content(frontmatter, body, paper_name):
    """Check for duplicate/redundant information"""
    issues = []

    # Check for duplicate citation info in body
    citation_matches = re.findall(r'(\d+ citations \([^)]+\) \[\d{4}-\d{2}-\d{2}\])', body)
    if len(citation_matches) > 2:
        issues.append(f"Duplicate citation info in body ({len(citation_matches)} entries)")

    # Check for repeated text patterns
    unique_citations = set(citation_matches)
    if len(citation_matches) > len(unique_citations):
        issues.append("Identical citation entries repeated")

    return issues


def check_field_consistency(frontmatter, paper_name):
    """Check for inconsistent field values"""
    issues = []

    # Check ethics fields consistency
    ethics_fields = ['virtue_ethics', 'deontological_ethics', 'utilitarian_ethics']
    ethics_yes = any(frontmatter.get(f) == 'Yes' for f in ethics_fields)
    ethics_overall = frontmatter.get('ethics_overall')

    if ethics_yes and ethics_overall == 'No':
        issues.append("ethics_overall is 'No' but specific ethics field is 'Yes'")

    # Check year format
    year = frontmatter.get('year')
    if year:
        try:
            year_int = int(year)
            if year_int < 2000 or year_int > 2030:
                issues.append(f"Unusual year value: {year}")
        except (ValueError, TypeError):
            issues.append(f"Invalid year format: {year}")

    # Check for valid field values
    for field, valid_values in VALID_VALUES.items():
        value = frontmatter.get(field)
        if value and str(value) not in valid_values:
            issues.append(f"Invalid value for {field}: '{value}'")

    return issues


def check_empty_fields(frontmatter, paper_name):
    """Check for fields that are present but empty"""
    issues = []

    for field, value in frontmatter.items():
        if value is None or (isinstance(value, str) and value.strip() == ''):
            if field not in ['Human View', 'Human View Date', 'Human View note', 'Not AI',
                           'tags', 'local_pdf', 'pdf_extract', 'notes']:
                issues.append(f"Empty field: {field}")

    return issues


def check_body_structure(body, paper_name):
    """Check body structure for issues"""
    issues = []

    # Check for required sections
    required_sections = ['## Abstract', '## Authors']
    for section in required_sections:
        if section not in body:
            issues.append(f"Missing section: {section}")

    # Check for body abstract placeholder
    if '*No abstract available in source.*' in body:
        issues.append("Body contains 'No abstract available' placeholder")

    # Check for duplicate headers
    headers = re.findall(r'^##\s+(.+)$', body, re.MULTILINE)
    seen_headers = {}
    for header in headers:
        if header in seen_headers:
            issues.append(f"Duplicate section header: {header}")
        seen_headers[header] = True

    return issues


def check_author_format(authors, first_author, paper_name):
    """Check author field formatting"""
    issues = []

    if not authors:
        issues.append("Missing authors field")
        return issues

    # Check first_author is wikilink
    if first_author and not (str(first_author).startswith('[[') and str(first_author).endswith(']]')):
        issues.append(f"first_author not in wikilink format: {first_author}")

    # Check for incomplete author data
    if 'and others' in str(authors).lower() or 'et al' in str(authors).lower():
        issues.append("Authors field contains incomplete placeholder (et al./and others)")

    return issues


def audit_paper(filepath):
    """Audit a single paper file"""
    issues = {
        'errors': [],
        'warnings': [],
        'info': []
    }

    paper_name = filepath.stem

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        issues['errors'].append(f"Cannot read file: {e}")
        return issues

    # Extract frontmatter
    try:
        frontmatter_text, body = extract_frontmatter(content)
        frontmatter = parse_frontmatter(frontmatter_text)
    except Exception as e:
        issues['errors'].append(f"YAML parsing error: {e}")
        return issues

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter or frontmatter[field] is None:
            issues['errors'].append(f"Missing required field: {field}")

    # Check PDF link
    local_pdf = frontmatter.get('local_pdf')
    if local_pdf:
        error, target = check_pdf_link(local_pdf, paper_name)
        if error:
            issues['warnings'].append(f"local_pdf issue: {error} ({target})")

    # Check PDF extract link
    pdf_extract = frontmatter.get('pdf_extract')
    if pdf_extract:
        error, target = check_pdf_extract_link(pdf_extract, paper_name)
        if error:
            issues['warnings'].append(f"pdf_extract issue: {error} ({target})")

    # Check author links
    author_issues = check_author_links(frontmatter.get('authors', ''), body)
    for issue in author_issues:
        issues['warnings'].append(issue)

    # Check abstract quality
    abstract_issues = check_abstract_quality(frontmatter.get('abstract'), paper_name)
    for issue in abstract_issues:
        if 'Missing' in issue or 'corrupted' in issue:
            issues['errors'].append(issue)
        else:
            issues['warnings'].append(issue)

    # Check for duplicates
    dup_issues = check_duplicate_content(frontmatter, body, paper_name)
    for issue in dup_issues:
        issues['warnings'].append(issue)

    # Check field consistency
    consistency_issues = check_field_consistency(frontmatter, paper_name)
    for issue in consistency_issues:
        issues['warnings'].append(issue)

    # Check empty fields
    empty_issues = check_empty_fields(frontmatter, paper_name)
    for issue in empty_issues:
        issues['info'].append(issue)

    # Check body structure
    body_issues = check_body_structure(body, paper_name)
    for issue in body_issues:
        if 'Missing section' in issue:
            issues['warnings'].append(issue)
        else:
            issues['info'].append(issue)

    # Check author format
    author_format_issues = check_author_format(
        frontmatter.get('authors'),
        frontmatter.get('first_author'),
        paper_name
    )
    for issue in author_format_issues:
        if 'incomplete' in issue.lower():
            issues['errors'].append(issue)
        else:
            issues['warnings'].append(issue)

    return issues


def check_duplicate_papers():
    """Check for duplicate papers by key, DOI, or title"""
    duplicates = {
        'by_key': defaultdict(list),
        'by_doi': defaultdict(list),
        'by_title': defaultdict(list)
    }

    for filepath in PAPERS_DIR.glob("*.md"):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            frontmatter_text, _ = extract_frontmatter(content)
            frontmatter = parse_frontmatter(frontmatter_text)

            key = frontmatter.get('key')
            doi = frontmatter.get('doi')
            title = frontmatter.get('short_title') or filepath.stem

            if key:
                duplicates['by_key'][key].append(filepath.name)
            if doi:
                duplicates['by_doi'][doi].append(filepath.name)
            if title:
                duplicates['by_title'][title.lower()].append(filepath.name)

        except Exception:
            pass  # Skip papers that cannot be read or parsed

    # Filter to only actual duplicates
    result = {
        'by_key': {k: v for k, v in duplicates['by_key'].items() if len(v) > 1},
        'by_doi': {k: v for k, v in duplicates['by_doi'].items() if len(v) > 1},
        'by_title': {k: v for k, v in duplicates['by_title'].items() if len(v) > 1}
    }

    return result


def generate_report(all_issues, duplicates, output_path):
    """Generate audit report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Count totals
    total_papers = len(all_issues)
    papers_with_errors = sum(1 for issues in all_issues.values() if issues['errors'])
    papers_with_warnings = sum(1 for issues in all_issues.values() if issues['warnings'])

    total_errors = sum(len(issues['errors']) for issues in all_issues.values())
    total_warnings = sum(len(issues['warnings']) for issues in all_issues.values())
    total_info = sum(len(issues['info']) for issues in all_issues.values())

    report = f"""# Comprehensive Paper Audit Report

**Generated:** {timestamp}
**Total Papers Audited:** {total_papers}

## Summary

| Metric | Count |
|--------|-------|
| Papers with Errors | {papers_with_errors} |
| Papers with Warnings | {papers_with_warnings} |
| Total Errors | {total_errors} |
| Total Warnings | {total_warnings} |
| Total Info Items | {total_info} |

---

## Duplicate Detection

### Duplicate Keys
"""

    if duplicates['by_key']:
        for key, files in duplicates['by_key'].items():
            report += f"- **{key}**: {', '.join(files)}\n"
    else:
        report += "*No duplicate keys found*\n"

    report += "\n### Duplicate DOIs\n"
    if duplicates['by_doi']:
        for doi, files in duplicates['by_doi'].items():
            report += f"- **{doi}**: {', '.join(files)}\n"
    else:
        report += "*No duplicate DOIs found*\n"

    report += "\n### Duplicate Titles\n"
    if duplicates['by_title']:
        for title, files in duplicates['by_title'].items():
            if len(files) > 1:
                report += f"- **{title[:60]}...**: {', '.join(files)}\n"
    else:
        report += "*No duplicate titles found*\n"

    report += "\n---\n\n## Errors (Must Fix)\n\n"

    # Group errors by type
    error_by_type = defaultdict(list)
    for paper, issues in all_issues.items():
        for error in issues['errors']:
            error_by_type[error.split(':')[0] if ':' in error else error].append(paper)

    if error_by_type:
        for error_type, papers in sorted(error_by_type.items(), key=lambda x: -len(x[1])):
            report += f"### {error_type} ({len(papers)} papers)\n\n"
            for paper in sorted(papers)[:20]:  # Show first 20
                report += f"- [[{paper}]]\n"
            if len(papers) > 20:
                report += f"- *... and {len(papers) - 20} more*\n"
            report += "\n"
    else:
        report += "*No errors found!*\n\n"

    report += "---\n\n## Warnings (Should Review)\n\n"

    # Group warnings by type
    warning_by_type = defaultdict(list)
    for paper, issues in all_issues.items():
        for warning in issues['warnings']:
            warning_type = warning.split(':')[0] if ':' in warning else warning
            warning_by_type[warning_type].append((paper, warning))

    if warning_by_type:
        for warning_type, items in sorted(warning_by_type.items(), key=lambda x: -len(x[1])):
            report += f"### {warning_type} ({len(items)} papers)\n\n"
            for paper, warning in sorted(items, key=lambda x: x[0])[:10]:  # Show first 10
                detail = warning.split(':', 1)[1] if ':' in warning else ''
                report += f"- [[{paper}]]{detail}\n"
            if len(items) > 10:
                report += f"- *... and {len(items) - 10} more*\n"
            report += "\n"
    else:
        report += "*No warnings found!*\n\n"

    report += "---\n\n## Info (Optional Review)\n\n"

    # Group info by type
    info_by_type = defaultdict(int)
    for paper, issues in all_issues.items():
        for info in issues['info']:
            info_type = info.split(':')[0] if ':' in info else info
            info_by_type[info_type] += 1

    if info_by_type:
        for info_type, count in sorted(info_by_type.items(), key=lambda x: -x[1]):
            report += f"- {info_type}: {count} papers\n"
    else:
        report += "*No info items found*\n"

    report += "\n---\n\n## Detailed Issues by Paper\n\n"

    # List papers with issues
    papers_with_issues = {p: i for p, i in all_issues.items() if i['errors'] or i['warnings']}
    for paper in sorted(papers_with_issues.keys())[:50]:  # First 50
        issues = papers_with_issues[paper]
        report += f"### [[{paper}]]\n\n"
        if issues['errors']:
            report += "**Errors:**\n"
            for error in issues['errors']:
                report += f"- ❌ {error}\n"
        if issues['warnings']:
            report += "**Warnings:**\n"
            for warning in issues['warnings']:
                report += f"- ⚠️ {warning}\n"
        report += "\n"

    if len(papers_with_issues) > 50:
        report += f"\n*... and {len(papers_with_issues) - 50} more papers with issues*\n"

    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return report


def main():
    print("=" * 60)
    print("COMPREHENSIVE PAPER AUDIT")
    print("=" * 60)

    # Audit all papers
    all_issues = {}
    paper_files = list(PAPERS_DIR.glob("*.md"))
    total = len(paper_files)

    print(f"\nAuditing {total} papers...")

    for i, filepath in enumerate(paper_files, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{total}")

        issues = audit_paper(filepath)
        all_issues[filepath.stem] = issues

    print(f"  Progress: {total}/{total}")

    # Check for duplicates
    print("\nChecking for duplicates...")
    duplicates = check_duplicate_papers()

    # Generate report
    print("\nGenerating report...")
    report_path = WORKSPACE_ROOT / "STATISTICS" / "20260124-comprehensive-audit-report.md"
    report = generate_report(all_issues, duplicates, report_path)

    # Print summary
    total_errors = sum(len(issues['errors']) for issues in all_issues.values())
    total_warnings = sum(len(issues['warnings']) for issues in all_issues.values())
    papers_with_errors = sum(1 for issues in all_issues.values() if issues['errors'])

    print("\n" + "=" * 60)
    print("AUDIT COMPLETE")
    print("=" * 60)
    print(f"Total papers audited: {total}")
    print(f"Papers with errors: {papers_with_errors}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    print(f"\nReport saved to: {report_path}")
    print("=" * 60)

    return all_issues, duplicates


if __name__ == "__main__":
    main()
