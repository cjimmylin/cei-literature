# Next Steps - Completing LifeOS Implementation

**Session Date:** 2026-02-02
**Current Status:** Phase 5 (40% complete), Phases 6-8 pending
**Context:** Ready to continue with remaining infrastructure and testing

---

## 🎯 Current State

### What's Complete (55%)

**✅ Phase 1-4: Foundation, Standards, Configs, Thread Finalization**
- All complete, tested, committed

**🟡 Phase 5: Infrastructure (40% complete)**
- ✅ `.agent/lib/` structure created
- ✅ `lib/config.py` migrated (173 lines)
- ✅ `lib/yaml_utils.py` migrated (409 lines)
- ✅ Backward-compat shims working
- ⏳ 4 utility modules remaining
- ⏳ Test suite not started

**⏳ Phase 6-8: Testing, Self-Healing, Documentation**
- Not started

### Git Commits
- **c61a5cb** - Phases 1-4 complete
- **42a1016** - Testing guide
- **1cd2751** - Phase 5 partial (lib structure)
- **ced5cd9** - Status update

---

## 📋 Phase 5-6: Infrastructure & Testing (Remaining 60%)

### Step 1: Implement lib/paper_utils.py (~200 lines)

**Purpose:** Paper file operations and bulk updates

**Functions to implement:**
```python
from pathlib import Path
from typing import List, Dict
from lib.config import PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, write_paper, parse_frontmatter, rebuild_frontmatter

def get_all_papers() -> List[Path]:
    """Return all paper files in papers/ directory."""
    return sorted(PAPERS_DIR.glob("*.md"))

def get_papers_by_field(field: str, value: str) -> List[Path]:
    """Find papers where field matches value."""
    matching = []
    for paper in get_all_papers():
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)
        if fields.get(field) == value:
            matching.append(paper)
    return matching

def get_papers_missing_field(field: str) -> List[Path]:
    """Find papers missing a specific field."""
    missing = []
    for paper in get_all_papers():
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)
        if field not in fields:
            missing.append(paper)
    return missing

def update_paper_field(filepath: Path, field: str, value: str) -> bool:
    """Update a single field in a paper."""
    try:
        content = filepath.read_text()
        fm, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        fields[field] = value

        new_fm = rebuild_frontmatter(fields)
        write_paper(filepath, new_fm, body, validate=True)
        return True
    except Exception as e:
        print(f"Failed to update {filepath.name}: {e}")
        return False

def batch_update_papers(papers: List[Path], updates: Dict[str, str]) -> Dict[str, int]:
    """Update multiple papers with same field changes."""
    results = {"success": 0, "failed": 0}

    for paper in papers:
        try:
            content = paper.read_text()
            fm, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm)

            # Apply all updates
            for field, value in updates.items():
                fields[field] = value

            new_fm = rebuild_frontmatter(fields)
            write_paper(paper, new_fm, body, validate=True)
            results["success"] += 1
        except Exception as e:
            print(f"Failed {paper.name}: {e}")
            results["failed"] += 1

    return results

def get_paper_stats() -> Dict[str, int]:
    """Get statistics about papers in vault."""
    papers = get_all_papers()

    stats = {
        "total": len(papers),
        "with_ethics_overall": 0,
        "with_pdfs": 0,
        "with_extracts": 0,
    }

    for paper in papers:
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "ethics_overall" in fields:
            stats["with_ethics_overall"] += 1
        if "local_pdf" in fields:
            stats["with_pdfs"] += 1
        if "pdf_extract" in fields:
            stats["with_extracts"] += 1

    return stats
```

**Location:** `.agent/lib/paper_utils.py`

**Test file:** `.agent/tests/test_paper_utils.py` (see Step 5)

---

### Step 2: Implement lib/author_utils.py (~150 lines)

**Purpose:** Author profile operations and validation

**Functions to implement:**
```python
from pathlib import Path
from typing import List, Set
from lib.config import AUTHORS_DIR, PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter

def get_all_authors() -> List[Path]:
    """Return all author profile files."""
    return sorted(AUTHORS_DIR.glob("*.md"))

def find_orphaned_authors() -> List[Path]:
    """Find author files not referenced by any paper."""
    # Get all author names from files
    all_authors = {f.stem for f in get_all_authors()}

    # Get all referenced authors from papers
    referenced = set()
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "first_author" in fields:
            # Extract author name from wikilink: "[[Author Name]]"
            author = fields["first_author"].strip('"').strip('[]')
            referenced.add(author)

    # Find orphans
    orphaned = all_authors - referenced
    return [AUTHORS_DIR / f"{author}.md" for author in orphaned]

def get_authors_by_enrichment_status(enriched: bool = True) -> List[Path]:
    """Find authors by enrichment status."""
    matching = []
    for author_file in get_all_authors():
        content = author_file.read_text()

        # Check for enriched flag in frontmatter
        if enriched:
            if "enriched: true" in content:
                matching.append(author_file)
        else:
            if "enriched: true" not in content:
                matching.append(author_file)

    return matching

def validate_author_profile(filepath: Path) -> Dict[str, any]:
    """Validate author profile completeness."""
    result = {
        "valid": True,
        "warnings": [],
        "errors": [],
    }

    content = filepath.read_text()

    # Check for basic structure
    if not content.startswith("# "):
        result["errors"].append("Missing author name header")
        result["valid"] = False

    # Check for enrichment
    if "enriched: true" not in content:
        result["warnings"].append("Not enriched")

    # Check for institution
    if "institution:" not in content.lower() and "affiliation" not in content.lower():
        result["warnings"].append("Missing institution/affiliation")

    return result

def get_author_paper_count(author_name: str) -> int:
    """Count papers by a specific author."""
    count = 0
    search_pattern = f'"[[{author_name}]]"'

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        if search_pattern in content:
            count += 1

    return count
```

**Location:** `.agent/lib/author_utils.py`

---

### Step 3: Implement lib/pdf_utils.py (~180 lines)

**Purpose:** PDF and extract validation

**Functions to implement:**
```python
from pathlib import Path
from typing import List, Dict
from lib.config import PDFS_DIR, PDF_EXTRACTS_DIR, PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter

def validate_pdf_link(local_pdf: str, paper_name: str) -> Dict[str, any]:
    """Validate PDF link from paper."""
    result = {
        "valid": True,
        "errors": [],
        "path": None,
    }

    # Extract filename from wikilink: "[[PDFs/file.pdf]]"
    if not local_pdf:
        result["valid"] = False
        result["errors"].append("No PDF link")
        return result

    # Remove wikilink markers and quotes
    pdf_filename = local_pdf.strip('"').strip('[]').replace("PDFs/", "")
    pdf_path = PDFS_DIR / pdf_filename

    if not pdf_path.exists():
        result["valid"] = False
        result["errors"].append(f"PDF not found: {pdf_filename}")
    else:
        result["path"] = pdf_path

    return result

def validate_extract_link(pdf_extract: str, paper_name: str) -> Dict[str, any]:
    """Validate extract link from paper."""
    result = {
        "valid": True,
        "errors": [],
        "path": None,
    }

    if not pdf_extract:
        result["valid"] = False
        result["errors"].append("No extract link")
        return result

    # Extract path
    extract_filename = pdf_extract.replace("PDF Extracts/", "")
    extract_path = PDF_EXTRACTS_DIR / extract_filename

    if not extract_path.exists():
        result["valid"] = False
        result["errors"].append(f"Extract not found: {extract_filename}")
    else:
        result["path"] = extract_path

    return result

def find_orphaned_pdfs() -> List[Path]:
    """Find PDFs not referenced by any paper."""
    # Get all PDF files
    all_pdfs = {f.name for f in PDFS_DIR.glob("*.pdf")}

    # Get referenced PDFs from papers
    referenced = set()
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "local_pdf" in fields:
            pdf = fields["local_pdf"].strip('"').strip('[]').replace("PDFs/", "")
            referenced.add(pdf)

    # Find orphans
    orphaned = all_pdfs - referenced
    return [PDFS_DIR / pdf for pdf in orphaned]

def find_missing_pdfs() -> List[Dict[str, str]]:
    """Find papers with PDF links but missing PDF files."""
    missing = []

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "local_pdf" in fields:
            result = validate_pdf_link(fields["local_pdf"], paper.stem)
            if not result["valid"]:
                missing.append({
                    "paper": paper.name,
                    "pdf": fields["local_pdf"],
                    "error": result["errors"][0],
                })

    return missing

def find_missing_extracts() -> List[Dict[str, str]]:
    """Find papers with extract links but missing extract files."""
    missing = []

    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "pdf_extract" in fields:
            result = validate_extract_link(fields["pdf_extract"], paper.stem)
            if not result["valid"]:
                missing.append({
                    "paper": paper.name,
                    "extract": fields["pdf_extract"],
                    "error": result["errors"][0],
                })

    return missing
```

**Location:** `.agent/lib/pdf_utils.py`

---

### Step 4: Implement lib/validation_utils.py (~250 lines)

**Purpose:** Comprehensive validation and integrity checks

**Functions to implement:**
```python
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass
from lib.config import PAPERS_DIR
from lib.yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter

@dataclass
class ValidationResult:
    """Result of validation check."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    info: List[str]

def validate_paper_integrity(filepath: Path) -> ValidationResult:
    """Comprehensive paper validation."""
    errors = []
    warnings = []
    info = []

    try:
        content = filepath.read_text()

        # Check frontmatter extraction
        try:
            fm, body = extract_frontmatter(content)
        except ValueError as e:
            errors.append(f"Frontmatter extraction failed: {e}")
            return ValidationResult(False, errors, warnings, info)

        # Validate YAML structure
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            errors.extend(issues)

        # Parse fields
        fields = parse_frontmatter(fm)

        # Check required fields
        required = ["key", "type", "year", "first_author"]
        for field in required:
            if field not in fields:
                errors.append(f"Missing required field: {field}")

        # Check field formats
        if "first_author" in fields:
            fa = fields["first_author"]
            if not (fa.startswith('"[[') and fa.endswith(']]"')):
                errors.append("first_author must be quoted wikilink")

        if "local_pdf" in fields:
            pdf = fields["local_pdf"]
            if not (pdf.startswith('"[[') and pdf.endswith(']]"')):
                errors.append("local_pdf must be quoted wikilink")

        # Check newtags format
        if "newtags" in fields:
            if "\n" in fields["newtags"]:
                errors.append("newtags must be string, not list")

        # Info: Check enrichment
        if "key_contribution" in fields or "significance" in fields:
            info.append("Paper has enrichment fields")

    except Exception as e:
        errors.append(f"Validation exception: {e}")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        info=info
    )

def validate_classification_consistency(fields: Dict[str, str]) -> List[str]:
    """Check for inconsistent classification fields."""
    issues = []

    # If ethics_overall=No, should have research_topic
    if fields.get("ethics_overall") == "No":
        if "research_topic" not in fields:
            issues.append("ethics_overall=No but missing research_topic")

    # If ethics_overall=Yes with no frameworks, should have ethics_perspective
    if fields.get("ethics_overall") == "Yes":
        has_framework = any([
            fields.get("virtue_ethics") == "Yes",
            fields.get("deontological_ethics") == "Yes",
            fields.get("utilitarian_ethics") == "Yes",
        ])
        if not has_framework and "ethics_perspective" not in fields:
            issues.append("ethics_overall=Yes but no framework or perspective")

    # If data fields set, description should exist
    has_data = any([
        fields.get("is_benchmark") == "Yes",
        fields.get("is_eval") == "Yes",
        fields.get("is_dataset") == "Yes",
    ])
    if has_data and "data_description" not in fields:
        issues.append("Data type set but missing data_description")

    return issues

def check_duplicate_papers() -> Dict[str, List[Path]]:
    """Find potential duplicate papers by DOI or title."""
    duplicates = {}

    # Check by DOI
    doi_map = {}
    for paper in PAPERS_DIR.glob("*.md"):
        content = paper.read_text()
        fm, _ = extract_frontmatter(content)
        fields = parse_frontmatter(fm)

        if "DOI" in fields and fields["DOI"]:
            doi = fields["DOI"]
            if doi in doi_map:
                if doi not in duplicates:
                    duplicates[doi] = [doi_map[doi]]
                duplicates[doi].append(paper)
            else:
                doi_map[doi] = paper

    return duplicates

def validate_all_papers() -> Dict[str, any]:
    """Run validation on all papers, return summary."""
    results = {
        "total": 0,
        "valid": 0,
        "errors": 0,
        "warnings": 0,
        "failed_papers": [],
    }

    for paper in PAPERS_DIR.glob("*.md"):
        results["total"] += 1

        result = validate_paper_integrity(paper)
        if result.is_valid:
            results["valid"] += 1
        else:
            results["errors"] += len(result.errors)
            results["failed_papers"].append({
                "file": paper.name,
                "errors": result.errors,
            })

        results["warnings"] += len(result.warnings)

    return results
```

**Location:** `.agent/lib/validation_utils.py`

---

### Step 5: Create Test Suite (~600 lines total)

**Create pytest configuration:**

**File:** `pytest.ini`
```ini
[pytest]
testpaths = .agent/tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

**File:** `.agent/tests/conftest.py` (~100 lines)
```python
"""Pytest fixtures for library tests."""

import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture
def sample_paper_content():
    """Minimal valid paper for testing."""
    return """---
key: 2024-Smith-Test
type: journalArticle
year: 2024
first_author: "[[John Smith]]"
title: "Test Paper"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
newtags: "AI Safety"
---

# Test Paper

## Abstract
This is a test abstract.
"""

@pytest.fixture
def corrupted_paper_content():
    """Paper with YAML corruption for testing."""
    return """---
key: 2024-Bad-Test
type: journalArticle
  - "#OrphanedTag"
year: 2024
first_author: [[Not Quoted]]
---

# Bad Paper
"""

@pytest.fixture
def tmp_vault(tmp_path):
    """Create temporary vault structure for testing."""
    vault = tmp_path / "test-vault"
    vault.mkdir()

    (vault / "papers").mkdir()
    (vault / "Authors").mkdir()
    (vault / "PDFs").mkdir()
    (vault / "PDF Extracts").mkdir()

    # Create config
    config = vault / ".vault-config.json"
    config.write_text('{"pdf_path": "' + str(vault / "PDFs") + '"}')

    return vault

@pytest.fixture
def sample_papers(tmp_vault, sample_paper_content):
    """Create sample papers in tmp vault."""
    papers_dir = tmp_vault / "papers"

    # Create 3 test papers
    for i in range(3):
        paper = papers_dir / f"2024-Author{i}-Test.md"
        paper.write_text(sample_paper_content.replace("Smith", f"Author{i}"))

    return papers_dir
```

**File:** `.agent/tests/test_yaml_utils.py` (~150 lines)
```python
"""Tests for lib.yaml_utils (CRITICAL - 100% coverage required)."""

import pytest
from lib.yaml_utils import (
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
    rebuild_frontmatter,
    write_paper,
)

def test_extract_frontmatter_standard(sample_paper_content):
    """Test extracting standard frontmatter."""
    fm, body = extract_frontmatter(sample_paper_content)

    assert "key: 2024-Smith-Test" in fm
    assert "# Test Paper" in body
    assert body.startswith("\n# Test Paper")

def test_extract_frontmatter_corrupted():
    """Test extracting from corrupted (attached marker)."""
    content = "---\nkey: test---\nBody"
    fm, body = extract_frontmatter(content)

    assert "key: test" in fm
    assert body == "Body"

def test_parse_frontmatter(sample_paper_content):
    """Test parsing frontmatter to dict."""
    fm, _ = extract_frontmatter(sample_paper_content)
    fields = parse_frontmatter(fm)

    assert fields["key"] == "2024-Smith-Test"
    assert fields["year"] == "2024"
    assert "[[John Smith]]" in fields["first_author"]

def test_validate_frontmatter_valid(sample_paper_content):
    """Test validation passes for valid frontmatter."""
    fm, _ = extract_frontmatter(sample_paper_content)
    is_valid, issues = validate_frontmatter(fm)

    assert is_valid
    assert len(issues) == 0

def test_validate_frontmatter_orphaned():
    """Test validation catches orphaned tags."""
    fm = "key: test\n  - #Orphaned"
    is_valid, issues = validate_frontmatter(fm)

    assert not is_valid
    assert any("orphaned" in issue.lower() for issue in issues)

def test_rebuild_frontmatter():
    """Test rebuilding frontmatter from dict."""
    fields = {
        "key": "test",
        "year": "2024",
        "title": "Test",
    }

    fm = rebuild_frontmatter(fields)

    assert fm.startswith("---\n")
    assert fm.endswith("\n---\n")
    assert "key: test" in fm
    assert "year: 2024" in fm

def test_write_paper_validates(tmp_vault, sample_paper_content):
    """Test write_paper validates before writing."""
    paper_file = tmp_vault / "papers" / "test.md"
    fm, body = extract_frontmatter(sample_paper_content)

    # Should succeed
    write_paper(paper_file, fm, body, validate=True)
    assert paper_file.exists()

    # Corrupted should fail
    bad_fm = "key: test\n  - #Bad"
    with pytest.raises(ValueError, match="validation"):
        write_paper(paper_file, bad_fm, body, validate=True)
```

**File:** `.agent/tests/test_paper_utils.py` (~80 lines)
**File:** `.agent/tests/test_author_utils.py` (~70 lines)
**File:** `.agent/tests/test_pdf_utils.py` (~80 lines)
**File:** `.agent/tests/test_validation_utils.py` (~120 lines)

---

### Step 6: Run Tests & Achieve >60% Coverage

```bash
# Install pytest
pip install pytest pytest-cov

# Run all tests
pytest .agent/tests/ -v

# Run with coverage
pytest .agent/tests/ --cov=.agent/lib --cov-report=html

# Target: >60% overall, 100% for yaml_utils
```

---

### Step 7: Update Backward-Compat Shims

Once new modules exist, update shims:

**PYTHON/paper_utils.py:**
```python
"""DEPRECATED: Shim to lib.paper_utils"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.paper_utils import *
```

(Repeat for author_utils, pdf_utils, validation_utils if needed)

---

## 📋 Phase 7-8: Self-Healing & Documentation

### Step 8: Create quarterly-maintenance Skill

**Purpose:** Automated health checks run quarterly

**Location:** `.claude/skills/quarterly-maintenance/SKILL.md`

**8-Step Health Check:**
1. YAML Integrity Check (validate_all_papers)
2. PDF Link Validation (find_missing_pdfs)
3. Author Profile Integrity (find_orphaned_authors)
4. PDF Extract Sync (find_missing_extracts)
5. Classification Consistency (validate_classification)
6. Duplicate Detection (check_duplicate_papers)
7. Orphaned File Detection (find_orphaned_pdfs)
8. Generate Health Report

**Script:** `.claude/skills/quarterly-maintenance/run_maintenance.py`

---

### Step 9: Set Up GitHub Actions CI/CD

**File:** `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install ruff mypy
      - name: Run ruff
        run: ruff check .agent/lib/
      - name: Run mypy
        run: mypy .agent/lib/ --ignore-missing-imports

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install pytest pytest-cov
      - name: Run tests
        run: pytest .agent/tests/ -v --cov=.agent/lib

  validate-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - name: Validate YAML (sample)
        run: python3 -c "from lib.validation_utils import validate_all_papers; print(validate_all_papers())"
```

---

### Step 10: Enhance Pre-commit Hook

**File:** `.git/hooks/pre-commit`

```bash
#!/usr/bin/env bash
echo "Running pre-commit checks..."

# 1. YAML Validation (existing)
python3 PYTHON/validate_yaml_hook.py --staged-only
if [ $? -ne 0 ]; then
    echo "❌ YAML validation failed"
    exit 1
fi

# 2. Quick lib tests (NEW)
pytest .agent/tests/test_yaml_utils.py -q
if [ $? -ne 0 ]; then
    echo "❌ Library tests failed"
    exit 1
fi

# 3. Import checks (NEW)
python3 -c "from lib import config, yaml_utils" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Library imports failed"
    exit 1
fi

echo "✅ All checks passed!"
```

---

### Step 11: Update Documentation

**docs/INDEX.md:**
- Add `_OPERATING-SYSTEM/` structure
- Reference new library modules
- Link to testing guide

**docs/WORKFLOWS.md:**
- Add `/end-session` workflow
- Document thread finalization
- Add quarterly maintenance

**docs/OPERATING_SYSTEM_MIGRATION.md** (NEW):
- Full migration guide
- Before/after comparison
- Rollback procedures

---

## 🔍 Quality Checklist

Before marking complete:

### Phase 5-6 Checklist
- [ ] All 4 utility modules implemented
- [ ] All 7 test files created
- [ ] Test coverage >60% (100% for yaml_utils)
- [ ] All tests passing
- [ ] Backward-compat shims working
- [ ] No existing scripts broken

### Phase 7-8 Checklist
- [ ] quarterly-maintenance skill complete
- [ ] GitHub Actions CI/CD working
- [ ] Pre-commit hook enhanced
- [ ] All documentation updated
- [ ] Migration guide created
- [ ] Comprehensive validation passed

---

## 📦 Estimated Effort

| Phase | Estimated Lines | Time | Complexity |
|-------|----------------|------|------------|
| Phase 5 remaining | 800 | 2-3 hours | Medium |
| Phase 6 (tests) | 600 | 2-3 hours | Medium |
| Phase 7-8 | 800 | 2-3 hours | Low |
| **Total** | **2,200** | **6-9 hours** | **Medium** |

---

## 🎯 Success Criteria

**Phase 5-6 Complete When:**
- All 6 library modules exist and tested
- pytest suite runs clean
- Coverage reports show >60%
- All shims work
- No regression in existing scripts

**Phase 7-8 Complete When:**
- Quarterly maintenance runs successfully
- CI/CD pipeline green on GitHub
- All documentation current
- Migration guide tested
- System ready for production use

---

## 💡 Tips for Next Session

### Starting Fresh

1. **Read this file first:** `_OPERATING-SYSTEM/NEXT_STEPS.md` (you are here)
2. **Check git status:** See what's committed
3. **Review learnings:** Read `_OPERATING-SYSTEM/Learnings/learnings-log.md`
4. **Verify tests pass:** Run existing tests (if any)

### Context You'll Need

**Key files to reference:**
- `_OPERATING-SYSTEM/IMPLEMENTATION_STATUS.md` - Current state
- `_OPERATING-SYSTEM/Standards/` - All procedural knowledge
- `.agent/lib/config.py` - See implementation pattern
- `.agent/lib/yaml_utils.py` - See implementation pattern

**Patterns to follow:**
- All functions have type hints
- All modules have docstrings
- Errors use exceptions, not return codes
- Use Path objects, not strings
- Import from lib.config for paths

### Potential Issues

**Import path issues:**
- Add `.agent` to sys.path if needed
- Use absolute imports from lib.*

**YAML utils is critical:**
- Don't modify behavior
- 100% test coverage required
- Any changes need extensive validation

**Backward compatibility:**
- Always test shims after changes
- Run `grep -r "from PYTHON" .` to find usage

---

## 📝 Session Handoff Template

When starting next session, agent should:

1. **Acknowledge context:**
   ```
   "I see we're continuing LifeOS implementation, Phase 5-6.
   Current status: 55% complete (Phases 1-4 done, Phase 5 40% done).
   Next: Implement remaining 4 utility modules + tests."
   ```

2. **Verify state:**
   ```bash
   git log --oneline | head -5
   ls -la .agent/lib/
   pytest .agent/tests/ -v  # (if tests exist)
   ```

3. **Start with one module:**
   - Implement `lib/paper_utils.py` first (most used)
   - Test it works with a simple script
   - Then move to author, pdf, validation utils

4. **Commit often:**
   - One commit per module implemented
   - One commit per test file created
   - Follow existing commit message format

---

## 🚀 Quick Start Commands

```bash
# Verify current state
git log --oneline | head -5
ls -la .agent/lib/
cat _OPERATING-SYSTEM/IMPLEMENTATION_STATUS.md | head -50

# Start implementing (example: paper_utils)
touch .agent/lib/paper_utils.py
# [implement functions per Step 1 above]

# Create test file
touch .agent/tests/test_paper_utils.py
# [implement tests]

# Run tests
pytest .agent/tests/test_paper_utils.py -v

# Commit when working
git add .agent/lib/paper_utils.py .agent/tests/test_paper_utils.py
git commit -m "Infrastructure: Add lib/paper_utils with tests

[Implementation details]

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

**Document Version:** 1.0
**Created:** 2026-02-02
**For:** Session continuity after context clear
**Owner:** CEI Literature Vault AI Agents

**Read this file before continuing implementation!**
