#!/usr/bin/env python3
"""
Pre-commit hook script for YAML frontmatter validation.

This script validates YAML frontmatter in paper markdown files to prevent
corruption issues like orphaned list items or malformed YAML.

Usage:
    python3 PYTHON/validate_yaml_hook.py [--staged-only] [files...]

Options:
    --staged-only    Only validate files staged for commit (for git hooks)
    files...         Specific files to validate (default: all papers/*.md)

Exit codes:
    0 - All files valid
    1 - Validation errors found
"""

import sys
import subprocess
from pathlib import Path

# Add PYTHON directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from yaml_frontmatter_utils import read_paper, validate_frontmatter
from vault_config import WORKSPACE_ROOT, PAPERS_DIR


def get_staged_files():
    """Get list of staged .md files in papers/ directory."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM'],
            capture_output=True, text=True, check=True
        )
        files = result.stdout.strip().split('\n')
        return [f for f in files if f.startswith('papers/') and f.endswith('.md')]
    except subprocess.CalledProcessError:
        return []


def validate_file(filepath: Path) -> tuple[bool, list[str]]:
    """Validate a single paper file's YAML frontmatter."""
    try:
        frontmatter, _ = read_paper(filepath)
        is_valid, issues = validate_frontmatter(frontmatter)
        return is_valid, issues
    except Exception as e:
        return False, [f"Error reading file: {e}"]


def main():
    args = sys.argv[1:]
    staged_only = '--staged-only' in args
    if staged_only:
        args.remove('--staged-only')

    # Determine which files to validate
    if args:
        # Specific files provided
        files = [Path(f) for f in args]
    elif staged_only:
        # Only staged files
        staged = get_staged_files()
        files = [WORKSPACE_ROOT / f for f in staged]
    else:
        # All papers
        files = list(PAPERS_DIR.glob('*.md'))

    if not files:
        print("No files to validate.")
        return 0

    print(f"Validating {len(files)} file(s)...")

    errors = []
    for filepath in sorted(files):
        if not filepath.exists():
            continue

        is_valid, issues = validate_file(filepath)
        if not is_valid:
            errors.append((filepath.name, issues))

    if errors:
        print(f"\n{'='*60}")
        print("YAML VALIDATION FAILED")
        print(f"{'='*60}\n")
        for filename, issues in errors:
            print(f"{filename}:")
            for issue in issues:
                print(f"  - {issue}")
            print()
        print(f"Total: {len(errors)} file(s) with errors")
        print("\nTo fix these issues:")
        print("  1. Review the YAML_SAFEGUARDS.md documentation")
        print("  2. Use yaml_frontmatter_utils.py for all YAML operations")
        print("  3. Run: python3 PYTHON/validate_yaml_hook.py <file>")
        return 1
    else:
        print(f"All {len(files)} file(s) passed validation.")
        return 0


if __name__ == '__main__':
    sys.exit(main())
