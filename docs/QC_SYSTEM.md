# Code Quality System

## Overview

The CEI Literature Vault includes a comprehensive code quality checking system that scans all Python scripts, skills, and documentation for common issues.

**Primary Script**: `PYTHON/code_quality_check.py`
**Slash Command**: `/qc-code [--verbose]`

## Quick Start

```bash
# Run QC check
python3 PYTHON/code_quality_check.py

# Verbose output
python3 PYTHON/code_quality_check.py --verbose

# Custom output location
python3 PYTHON/code_quality_check.py -o logs/custom_qc.md
```

## Issue Severity Levels

| Severity | Description | Examples |
|----------|-------------|----------|
| **Critical** | Breaking issues that must be fixed | Hardcoded paths, outdated format references |
| **High** | Safety/security issues | Bare except clauses, YAML utility violations |
| **Medium** | Code quality issues | Missing docstrings, duplicate functionality |
| **Low** | Minor cleanup items | Unused imports |

## Checks Performed

### 1. Hardcoded Paths (Critical)

Detects absolute paths that will break on other systems:
```python
# WRONG
filepath = "/Users/jimmy/Documents/vault/papers/file.md"

# CORRECT
filepath = Path(__file__).parent.parent / "papers" / "file.md"
```

### 2. Bare Except Clauses (High)

Detects bare `except:` that catch all exceptions including KeyboardInterrupt:
```python
# WRONG
try:
    process_data()
except:
    pass

# CORRECT
try:
    process_data()
except (yaml.YAMLError, IOError, ValueError) as e:
    logger.error(f"Failed: {e}")
```

### 3. YAML Safety (High)

Ensures scripts modifying papers use `yaml_frontmatter_utils.py`:
```python
# WRONG
with open(paper_path, 'w') as f:
    f.write(yaml.dump(frontmatter) + '---\n' + body)

# CORRECT
from PYTHON.yaml_frontmatter_utils import write_paper
write_paper(paper_path, frontmatter, body, validate=True)
```

**Known Exclusions** (legitimate exceptions):
- `generate_report_v2.py` - Only writes to STATISTICS/, not papers
- `fix_yaml_tags.py` - Fixes malformed YAML that can't use standard utilities
- `identify_benchmarks.py` - Only reads papers, writes to STATISTICS/

### 4. Print Statements (Medium)

Detects excessive use of `print()` instead of logging:
```python
# WRONG
print("Processing started")
print(f"Found {count} papers")

# CORRECT
import logging
logger = logging.getLogger(__name__)
logger.info("Processing started")
logger.info(f"Found {count} papers")
```

### 5. Unused Imports (Low)

Detects imported modules that are never used in the code.

### 6. Missing Docstrings (Medium)

Flags Python modules without docstrings (informational only).

### 7. Duplicate Functionality (Medium)

Flags scripts with similar name prefixes (informational only - many are intentional).

## Session 9 Results

### Before
- **Total Issues**: 150+
- Critical: 0
- High: 11
- Medium: 40
- Low: 111

### After
- **Total Issues**: 22 (informational only)
- Critical: 0 ✅
- High: 0 ✅
- Medium: 22 (12 docstrings + 10 duplicates)
- Low: 0 ✅

### Fixes Applied

#### 1. Bare Except Clauses (8 fixed)
- `PYTHON/classify_ethics_perspective.py`
- `PYTHON/classify_non_ethics_topics.py`
- `PYTHON/classify_cultural_religious.py`
- `PYTHON/classify_moral_psych.py`
- `PYTHON/comprehensive_audit.py`
- `.agent/skills/vault_management/scripts/identify.py`
- `.agent/skills/vault_management/scripts/stats.py`
- `.agent/skills/classify_papers/scripts/run_pipeline.py`

#### 2. YAML Safety (3 exclusions added)
Added to QC checker exclusion list for false positives.

#### 3. Unused Imports (111 cleaned)
Removed from 50+ files across:
- PYTHON/ directory (106 imports)
- .agent/skills/*/scripts/ (5 imports)

#### 4. Print → Logging (28 files converted)
Converted all production scripts to use Python logging module.

## Best Practices

### Exception Handling
Always use specific exception types:
```python
try:
    frontmatter, body = read_paper(paper_path)
    # ... process ...
except (yaml.YAMLError, IOError) as e:
    logger.error(f"Failed to read {paper_path}: {e}")
    return
except ValueError as e:
    logger.warning(f"Validation error in {paper_path}: {e}")
    continue
```

### Logging Standards
Use appropriate log levels:
```python
import logging
logger = logging.getLogger(__name__)

# Informational messages
logger.info("Processing started")
logger.info(f"Processed {count} papers")

# Warnings (non-fatal issues)
logger.warning(f"Missing field in {filename}")

# Errors (failures)
logger.error(f"Failed to process {filename}: {error}")
```

### YAML Modifications
Always use the safe utility:
```python
from PYTHON.yaml_frontmatter_utils import read_paper, write_paper, validate_frontmatter

# Read
frontmatter, body = read_paper(paper_path)

# Validate
is_valid, issues = validate_frontmatter(frontmatter)
if not is_valid:
    raise ValueError(f"Invalid YAML: {issues}")

# Modify
frontmatter['new_field'] = 'value'

# Write with validation
write_paper(paper_path, frontmatter, body, validate=True)
```

## Integration with Workflow

### Before Committing Code
```bash
# Always run QC check before committing
python3 PYTHON/code_quality_check.py

# Fix any High or Critical issues
# Review Medium/Low issues
```

### After Adding New Scripts
1. Run QC check
2. Add module docstring if flagged
3. Ensure proper exception handling
4. Use logging instead of print()
5. Import only what you need

### Updating QC Exclusions
If you add a script that legitimately needs to bypass YAML safety check:
1. Verify it truly doesn't modify papers/ files
2. Add to `YAML_SAFETY_EXCEPTIONS` in `code_quality_check.py`:
```python
YAML_SAFETY_EXCEPTIONS = {
    'yaml_frontmatter_utils.py',
    'generate_report_v2.py',  # Only writes to STATISTICS/
    'fix_yaml_tags.py',       # Fixes malformed YAML
    'identify_benchmarks.py',  # Only reads papers
    'your_new_script.py',      # Brief justification
}
```

## Maintenance

The QC system itself requires minimal maintenance:

1. **Update checks** as new patterns emerge
2. **Add exclusions** for legitimate exceptions (with comments)
3. **Run regularly** - especially before major releases
4. **Review trends** - recurring issues may need architectural fixes

## Output Format

QC reports are saved to `logs/code_quality_YYYYMMDD_HHMMSS.md`:

```markdown
# Code Quality Check Results

**Generated:** 2026-01-24 21:02:50
**Total Issues:** 22

## Summary by Severity
| Severity | Count |
|----------|-------|
| Critical | 0 |
| High | 0 |
| Medium | 22 |
| Low | 0 |

## Summary by Category
| Category | Count |
|----------|-------|
| missing-docstring | 12 |
| duplicate-functionality | 10 |

## All Issues
[Detailed list of issues with file/line numbers]
```

## Future Enhancements

Potential additions for the QC system:
- Complexity metrics (cyclomatic complexity)
- Security scanning (SQL injection, path traversal)
- Dependency version checks
- Documentation coverage metrics
- Test coverage integration
