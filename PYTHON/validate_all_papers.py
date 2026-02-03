#!/usr/bin/env python3
"""
Validate YAML frontmatter for all papers in the vault.
Reports any papers with YAML errors.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from PYTHON.yaml_frontmatter_utils import extract_frontmatter, validate_frontmatter
from PYTHON.vault_config import PAPERS_DIR


def validate_all_papers(papers_dir: Path):
    """Validate YAML frontmatter for all papers"""

    papers = sorted(papers_dir.glob('*.md'))
    errors = []
    valid_count = 0

    print(f"Validating {len(papers)} papers...\n")

    for i, filepath in enumerate(papers, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(papers)}")

        try:
            content = filepath.read_text(encoding='utf-8')
            fm, body = extract_frontmatter(content)

            is_valid, issues = validate_frontmatter(fm)

            if is_valid:
                valid_count += 1
            else:
                errors.append((filepath.name, issues))

        except Exception as e:
            errors.append((filepath.name, str(e)))

    print(f"\n{'='*60}")
    print("VALIDATION RESULTS")
    print(f"{'='*60}")
    print(f"Valid papers:     {valid_count}/{len(papers)}")
    print(f"Papers with errors: {len(errors)}")

    if errors:
        print(f"\n{'='*60}")
        print("PAPERS WITH ERRORS")
        print(f"{'='*60}")
        for paper_name, issue in errors:
            print(f"\n{paper_name}:")
            print(f"  {issue}")
    else:
        print("\n✓ All papers have valid YAML frontmatter!")

    print(f"{'='*60}\n")
    return len(errors) == 0


if __name__ == '__main__':
    success = validate_all_papers(PAPERS_DIR)
    sys.exit(0 if success else 1)
