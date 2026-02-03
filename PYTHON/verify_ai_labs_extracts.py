#!/usr/bin/env python3
"""
Verify AI Labs PDF extracts.

Validates that all expected markdown extracts were created successfully
and checks for quality issues (valid YAML, non-empty content, file size).
"""

import json
from pathlib import Path
from vault_config import PDF_EXTRACTS_DIR

BATCH_DIR = Path(__file__).parent.parent / "logs" / "batches"
EXTRACT_DIR = PDF_EXTRACTS_DIR / "AI Labs"


def load_all_batches():
    """Load all batch assignment files."""
    batches = []
    batch_id = 0

    while True:
        batch_file = BATCH_DIR / f"batch_{batch_id}.json"
        if not batch_file.exists():
            break

        with open(batch_file, 'r', encoding='utf-8') as f:
            batches.append(json.load(f))

        batch_id += 1

    return batches


def parse_yaml_frontmatter(content):
    """Simple YAML frontmatter parser."""
    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    return parts[1], parts[2]


def verify_extract(output_path):
    """Verify a single extract file."""
    issues = []

    # Check existence
    if not output_path.exists():
        return {
            'exists': False,
            'valid_yaml': False,
            'has_content': False,
            'file_size': 0,
            'issues': ['File does not exist']
        }

    # Check file size
    file_size = output_path.stat().st_size
    if file_size < 1024:  # Less than 1KB
        issues.append(f'File too small: {file_size} bytes')

    # Read content
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'exists': True,
            'valid_yaml': False,
            'has_content': False,
            'file_size': file_size,
            'issues': [f'Could not read file: {e}']
        }

    # Parse YAML frontmatter
    frontmatter, body = parse_yaml_frontmatter(content)

    valid_yaml = frontmatter is not None
    if not valid_yaml:
        issues.append('No YAML frontmatter found')

    # Check for required YAML fields
    if valid_yaml:
        required_fields = ['title', 'source_pdf', 'company', 'pages', 'type']
        for field in required_fields:
            if f'{field}:' not in frontmatter:
                issues.append(f'Missing YAML field: {field}')
                valid_yaml = False

    # Check content section
    has_content = False
    if body:
        # Look for "## Content" section
        if '## Content' in body:
            # Extract content after "## Content"
            content_part = body.split('## Content', 1)[1]
            # Remove markdown code blocks
            content_text = content_part.replace('```', '').strip()
            has_content = len(content_text) > 100
        else:
            issues.append('No "## Content" section found')

    if not has_content:
        issues.append('Content section is empty or too short')

    return {
        'exists': True,
        'valid_yaml': valid_yaml,
        'has_content': has_content,
        'file_size': file_size,
        'issues': issues
    }


def main():
    """Verify all expected extracts."""
    print("=" * 60)
    print("AI Labs Extract Verification")
    print("=" * 60)

    # Load all batch assignments
    print("\nLoading batch assignments...")
    batches = load_all_batches()

    if not batches:
        print("Error: No batch files found. Run generate_batch_assignments.py first.")
        return

    total_batches = len(batches)
    total_pdfs = sum(len(batch) for batch in batches)

    print(f"Found {total_batches} batches with {total_pdfs} PDFs")

    # Verify each extract
    results = {
        'total': 0,
        'exists': 0,
        'valid_yaml': 0,
        'has_content': 0,
        'fully_valid': 0,
        'failed': []
    }

    print("\nVerifying extracts...")

    for batch_id, batch in enumerate(batches):
        print(f"\nBatch {batch_id}: {len(batch)} PDFs")

        for pdf_info in batch:
            output_path = Path(pdf_info['output_path'])
            results['total'] += 1

            verification = verify_extract(output_path)

            if verification['exists']:
                results['exists'] += 1

            if verification['valid_yaml']:
                results['valid_yaml'] += 1

            if verification['has_content']:
                results['has_content'] += 1

            if verification['exists'] and verification['valid_yaml'] and verification['has_content']:
                results['fully_valid'] += 1
                print(f"  ✓ {output_path.name}")
            else:
                results['failed'].append({
                    'file': str(output_path),
                    'verification': verification
                })
                print(f"  ✗ {output_path.name}")
                for issue in verification['issues']:
                    print(f"    - {issue}")

    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"Total expected: {results['total']}")
    print(f"Files exist: {results['exists']}/{results['total']}")
    print(f"Valid YAML: {results['valid_yaml']}/{results['total']}")
    print(f"Has content: {results['has_content']}/{results['total']}")
    print(f"Fully valid: {results['fully_valid']}/{results['total']}")

    if results['failed']:
        print(f"\n⚠ {len(results['failed'])} files have issues:")
        for failure in results['failed']:
            print(f"\n  {Path(failure['file']).name}:")
            for issue in failure['verification']['issues']:
                print(f"    - {issue}")

        # Save detailed failure report
        failure_report = BATCH_DIR / "verification_failures.json"
        with open(failure_report, 'w', encoding='utf-8') as f:
            json.dump(results['failed'], f, indent=2)
        print(f"\nDetailed failure report saved to: {failure_report}")

    else:
        print("\n✓ All extracts validated successfully!")

    # Exit with error code if failures
    if results['fully_valid'] < results['total']:
        exit(1)


if __name__ == "__main__":
    main()
