#!/usr/bin/env python3
"""
Validate YAML frontmatter for all papers in the vault.
Reports any papers with YAML errors.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from PYTHON.yaml_frontmatter_utils import extract_frontmatter, validate_frontmatter, parse_frontmatter
from PYTHON.vault_config import PAPERS_DIR

# Ethics fields that use the 0-100 integer scoring system
ETHICS_SCORE_FIELDS = ['ethics_overall', 'virtue_ethics', 'deontological_ethics', 'utilitarian_ethics',
                       'care_ethics', 'contractarian_ethics']

# Moral psychology fields that use the 0-100 integer scoring system
MP_SCORE_FIELDS = ['mp_mft', 'mp_schwartz', 'mp_trolley', 'mp_kohlberg',
                   'mp_dual_process', 'mp_intuitionist', 'mp_dyadic', 'mp_identity']

# Religious values fields that use the 0-100 integer scoring system
RV_SCORE_FIELDS = ['rv_islam', 'rv_christianity', 'rv_buddhism', 'rv_judaism',
                   'rv_hinduism', 'rv_sikhism', 'rv_confucianism', 'rv_taoism',
                   'rv_shinto', 'rv_jainism', 'rv_bahai', 'rv_zoroastrianism',
                   'rv_ubuntu', 'rv_indigenous']


def _is_valid_ethics_value(v):
    """Validate ethics field value: accepts 0-100 int or legacy 'Yes'/'No'/'Unknown'."""
    if isinstance(v, int) and 0 <= v <= 100:
        return True
    s = str(v).strip().strip('"')
    if s in ("Yes", "No", "Unknown"):
        return True
    try:
        n = int(s)
        return 0 <= n <= 100
    except ValueError:
        return False


def _validate_ethics_fields(fields):
    """Check ethics score fields for valid values. Returns list of issues."""
    issues = []
    for field in ETHICS_SCORE_FIELDS:
        if field in fields:
            val = fields[field]
            if val is not None and str(val).strip() != '' and not _is_valid_ethics_value(val):
                issues.append(
                    f"Invalid ethics value for '{field}': {val!r} "
                    f"(expected integer 0-100 or legacy 'Yes'/'No'/'Unknown')"
                )
    return issues


def _validate_mp_fields(fields):
    """Check moral psychology score fields for valid values. Returns list of issues."""
    issues = []
    for field in MP_SCORE_FIELDS:
        if field in fields:
            val = fields[field]
            if val is not None and str(val).strip() != '':
                try:
                    n = int(val)
                    if not (0 <= n <= 100):
                        issues.append(
                            f"Invalid mp score for '{field}': {val!r} "
                            f"(expected integer 0-100)"
                        )
                except (ValueError, TypeError):
                    issues.append(
                        f"Invalid mp score for '{field}': {val!r} "
                        f"(expected integer 0-100)"
                    )
    # Warn if not all 8 mp fields are present (may be pre-migration)
    present = [f for f in MP_SCORE_FIELDS if f in fields]
    if 0 < len(present) < len(MP_SCORE_FIELDS):
        missing = [f for f in MP_SCORE_FIELDS if f not in fields]
        issues.append(
            f"Incomplete mp_* fields: missing {', '.join(missing)} "
            f"(may be pre-migration)"
        )
    return issues


def _validate_rv_fields(fields):
    """Check religious values score fields for valid values. Returns list of issues."""
    issues = []
    for field in RV_SCORE_FIELDS:
        if field in fields:
            val = fields[field]
            if val is not None and str(val).strip() != '':
                try:
                    n = int(val)
                    if not (0 <= n <= 100):
                        issues.append(
                            f"Invalid rv score for '{field}': {val!r} "
                            f"(expected integer 0-100)"
                        )
                except (ValueError, TypeError):
                    issues.append(
                        f"Invalid rv score for '{field}': {val!r} "
                        f"(expected integer 0-100)"
                    )
    # Warn if not all 14 rv fields are present (may be pre-migration)
    present = [f for f in RV_SCORE_FIELDS if f in fields]
    if 0 < len(present) < len(RV_SCORE_FIELDS):
        missing = [f for f in RV_SCORE_FIELDS if f not in fields]
        issues.append(
            f"Incomplete rv_* fields: missing {', '.join(missing)} "
            f"(may be pre-migration)"
        )
    return issues


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

            # Additional ethics field validation
            fields = parse_frontmatter(fm)
            ethics_issues = _validate_ethics_fields(fields)
            if ethics_issues:
                is_valid = False
                if isinstance(issues, list):
                    issues.extend(ethics_issues)
                else:
                    issues = [issues] + ethics_issues if issues else ethics_issues

            # Moral psychology field validation
            mp_issues = _validate_mp_fields(fields)
            if mp_issues:
                is_valid = False
                if isinstance(issues, list):
                    issues.extend(mp_issues)
                else:
                    issues = [issues] + mp_issues if issues else mp_issues

            # Religious values field validation
            rv_issues = _validate_rv_fields(fields)
            if rv_issues:
                is_valid = False
                if isinstance(issues, list):
                    issues.extend(rv_issues)
                else:
                    issues = [issues] + rv_issues if issues else rv_issues

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
