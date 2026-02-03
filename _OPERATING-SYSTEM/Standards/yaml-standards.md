# YAML Frontmatter Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Data Integrity (CRITICAL)
**Applies to:** All paper metadata files in `papers/`

---

## The One Rule: Use yaml_frontmatter_utils.py

**ALWAYS use `PYTHON/yaml_frontmatter_utils.py`** for ALL YAML operations.

**NO EXCEPTIONS.**

---

## Why This Rule Exists

**January 2024:** 530+ papers had corrupted YAML frontmatter with:
1. **Orphaned list items** - `  - "#Tag"` without parent key
2. **Missing newlines** - Closing marker `---` without proper separation
3. **Wrong formats** - List items where strings were needed

This broke Obsidian's properties panel and risked data loss.

**Root Cause:** Scripts used regex and string concatenation on YAML.

**Solution:** Centralized library with validation + mandatory usage.

---

## Required Pattern

### Read → Modify → Write

```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)

# 1. READ - Extract frontmatter and body
with open(filepath, 'r') as f:
    content = f.read()
frontmatter, body = extract_frontmatter(content)
fields = parse_frontmatter(frontmatter)

# 2. MODIFY - Change fields
fields['ethics_overall'] = 'Yes'
fields['ethics_perspective'] = 'AI Safety & Alignment'

# 3. VALIDATE - Check structure
is_valid, issues = validate_frontmatter(fields)
if not is_valid:
    raise ValueError(f"YAML validation failed: {issues}")

# 4. WRITE - Rebuild and save
new_frontmatter = rebuild_frontmatter(fields)
write_paper(filepath, new_frontmatter, body, validate=True)
```

### Bulk Operations

```python
from pathlib import Path
from PYTHON.yaml_frontmatter_utils import extract_frontmatter, write_paper

papers_dir = Path("papers")
for paper_file in papers_dir.glob("*.md"):
    with open(paper_file, 'r') as f:
        content = f.read()

    frontmatter, body = extract_frontmatter(content)
    fields = parse_frontmatter(frontmatter)

    # Modify fields
    if fields.get('ethics_overall') == 'Yes':
        fields['newtags'] = fields.get('newtags', '') + ', Ethics'

    # Write with validation
    new_frontmatter = rebuild_frontmatter(fields)
    write_paper(paper_file, new_frontmatter, body, validate=True)
```

---

## What NOT To Do

| ❌ FORBIDDEN | ✅ REQUIRED | Why |
|-------------|------------|-----|
| Direct regex on frontmatter | Use `extract_frontmatter()` | Regex can't handle nested structures |
| String concatenation for reconstruction | Use `rebuild_frontmatter()` | Missing newlines cause corruption |
| Manual list creation | Use dict with lists | Creates orphaned items |
| `newtags` as YAML list | `newtags` as string | Field format is comma-separated |
| Unquoted wikilinks `[[...]]` | Quoted wikilinks `"[[...]]"` | YAML parser breaks on brackets |
| Skip validation | Always validate before write | Catches corruption early |

---

## YAML Structure Requirements

### Correct Format

```yaml
---
key: "string_value"
another_key: "another value"
list_parent:
  - item1
  - item2
newtags: "Tag1, Tag2, Tag3"    # String, not list
local_pdf: "[[PDFs/file.pdf]]"  # Quoted wikilink
first_author: "[[Author Name]]" # Quoted wikilink
---

## Abstract
Paper content starts here.
```

### Requirements

1. **Opening marker:** `---\n` (newline after)
2. **Closing marker:** `\n---\n` (newlines before AND after)
3. **List items:** Must have parent key, 2-space indent
4. **Strings:** Quote if contains special chars (`:`, `[`, `]`, `#`, `@`)
5. **Wikilinks:** Always quote `"[[...]]"`
6. **No orphaned items:** Every `  - ` needs parent key above it

---

## Common Corruption Patterns

### 1. Orphaned List Items

**WRONG:**
```yaml
---
local_pdf: "[[PDFs/file.pdf]]"
  - "#VirtueEthics"    # Orphaned - no parent key
  - "#AIAlignment"
---
```

**CORRECT:**
```yaml
---
local_pdf: "[[PDFs/file.pdf]]"
tags:
  - VirtueEthics
  - AIAlignment
---
```

**Fix:** Use `rebuild_frontmatter()` which structures lists correctly.

### 2. Missing Newlines

**WRONG:**
```yaml
---
key: "value"---

## Abstract
```

**CORRECT:**
```yaml
---
key: "value"
---

## Abstract
```

**Fix:** `rebuild_frontmatter()` adds proper newlines.

### 3. Unquoted Wikilinks

**WRONG:**
```yaml
---
local_pdf: [[PDFs/file.pdf]]
first_author: [[John Smith]]
---
```

**CORRECT:**
```yaml
---
local_pdf: "[[PDFs/file.pdf]]"
first_author: "[[John Smith]]"
---
```

**Detection:**
```bash
grep -l '^local_pdf: \[\[' papers/*.md
grep -l '^first_author: \[\[' papers/*.md
```

**Fix Script:** `PYTHON/fix_unquoted_local_pdf.py`

### 4. Wrong Field Format: newtags

**WRONG:**
```yaml
---
newtags:
  - VirtueEthics
  - AIAlignment
---
```

**CORRECT:**
```yaml
---
newtags: "VirtueEthics, AIAlignment"
---
```

**Rationale:** `newtags` aggregates classification tags as comma-separated string for compatibility with Obsidian's tag parsing.

### 5. Hash Prefix in Tags

**WRONG:**
```yaml
---
tags:
  - "#VirtueEthics"    # Hash prefix breaks Obsidian
  - "#AIAlignment"
---
```

**CORRECT:**
```yaml
---
tags:
  - VirtueEthics
  - AIAlignment
---
```

**Fix:** `yaml_frontmatter_utils.clean_orphaned_tags()` removes `#` prefixes.

---

## Validation Workflow

### Before Any YAML Edit

```python
from PYTHON.yaml_frontmatter_utils import validate_frontmatter

# Validate before modifying
frontmatter, body = extract_frontmatter(content)
fields = parse_frontmatter(frontmatter)

is_valid, issues = validate_frontmatter(fields)
if not is_valid:
    print(f"Pre-edit validation failed: {issues}")
    # Decide: fix issues or abort
```

### After Any YAML Edit

```python
# Always validate before writing
new_frontmatter = rebuild_frontmatter(fields)
is_valid, issues = validate_frontmatter(parse_frontmatter(new_frontmatter))
if not is_valid:
    raise ValueError(f"Post-edit validation failed: {issues}")

write_paper(filepath, new_frontmatter, body, validate=True)
```

### Bulk Validation

```bash
# Basic validation (all papers)
python3 PYTHON/validate_all_papers.py

# Enhanced validation (extended checks)
python3 PYTHON/validate_papers_enhanced.py

# Single file validation
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md
```

---

## Field Format Reference

| Field | Type | Format | Example |
|-------|------|--------|---------|
| `key` | String | Required, unique | `key: "2024-Smith-Ethics"` |
| `type` | String | Zotero item type | `type: "journalArticle"` |
| `title` | String | Quoted if special chars | `title: "Ethics in AI: A Survey"` |
| `first_author` | Wikilink | Quoted | `first_author: "[[John Smith]]"` |
| `local_pdf` | Wikilink | Quoted | `local_pdf: "[[PDFs/2024-Smith.pdf]]"` |
| `pdf_extract` | Wikilink | Quoted | `pdf_extract: "[[PDF Extracts/2024-Smith.md]]"` |
| `tags` | List | Proper list format | `tags:\n  - Ethics\n  - AI` |
| `newtags` | String | Comma-separated | `newtags: "VirtueEthics, AIAlignment"` |
| `ethics_overall` | String | Yes/No | `ethics_overall: "Yes"` |
| `ethics_perspective` | String | Category name | `ethics_perspective: "AI Safety & Alignment"` |
| `research_topic` | String | Category name | `research_topic: "Machine Learning"` |
| `national_ethnic_cultural` | List | Proper list | `national_ethnic_cultural:\n  - Chinese` |
| `religious_values` | List | Proper list | `religious_values:\n  - Islam` |

---

## Library Functions Reference

### extract_frontmatter(content: str) → Tuple[str, str]
Extracts YAML frontmatter and body from paper content.

**Returns:** `(frontmatter_string, body_string)`

### parse_frontmatter(frontmatter: str) → Dict
Parses YAML frontmatter string into dictionary.

**Returns:** `dict` of fields

### rebuild_frontmatter(fields: Dict) → str
Rebuilds YAML frontmatter from dictionary with proper formatting.

**Returns:** Correctly formatted YAML string with `---` markers

**Handles:**
- Proper newlines before/after markers
- List indentation (2 spaces)
- String quoting for special characters
- Field ordering (key first, then others)

### validate_frontmatter(frontmatter: Union[str, Dict]) → Tuple[bool, List[str]]
Validates YAML frontmatter structure.

**Returns:** `(is_valid: bool, issues: List[str])`

**Checks:**
- No orphaned list items
- Proper closing marker
- Valid YAML syntax
- Required fields present
- Correct field formats

### write_paper(filepath: Path, frontmatter: str, body: str, validate: bool = True) → None
Writes paper with validation.

**Parameters:**
- `filepath`: Path to paper file
- `frontmatter`: YAML frontmatter string (with markers)
- `body`: Paper body content
- `validate`: If True, validates before writing (RECOMMENDED)

**Raises:** `ValueError` if validation fails

### clean_orphaned_tags(content: str) → str
Removes orphaned tags and hash prefixes from frontmatter.

**Use case:** Fix legacy corruption

---

## Quick Validation Commands

```bash
# Check for unquoted wikilinks
grep -l "^local_pdf: \[\[" papers/*.md
grep -l "^first_author: \[\[" papers/*.md

# Check for orphaned list items
grep -n "^  - " papers/*.md | head -20

# Check for hash prefixes
grep -n '^  - "#' papers/*.md

# Validate YAML syntax
python3 PYTHON/validate_all_papers.py

# Enhanced validation
python3 PYTHON/validate_papers_enhanced.py

# Count valid papers
python3 PYTHON/validate_all_papers.py | grep "VALID" | wc -l
```

---

## Emergency Recovery

### If Corruption Detected

1. **Stop all operations immediately**
2. **Check git status:**
   ```bash
   git status
   git diff papers/
   ```
3. **If changes not committed, restore:**
   ```bash
   git checkout papers/corrupted-file.md
   ```
4. **If committed, revert:**
   ```bash
   git log --oneline papers/ | head -5
   git revert <commit-hash>
   ```
5. **Run diagnostics:**
   ```bash
   python3 PYTHON/validate_papers_enhanced.py > logs/corruption-report.txt
   ```
6. **Use repair script:**
   ```bash
   python3 PYTHON/repair_yaml_corruption.py
   ```

### Common Fixes

| Issue | Fix Script |
|-------|-----------|
| Unquoted wikilinks | `PYTHON/fix_unquoted_local_pdf.py` |
| Orphaned tags | `PYTHON/clean_orphaned_tags.py` |
| Missing newlines | `PYTHON/fix_yaml_markers.py` |
| Hash prefixes | `PYTHON/clean_orphaned_tags.py` |

---

## Testing New Scripts

Before running on all 657 papers:

```python
# Test on sample papers
test_papers = [
    "papers/2016-Amodei-Concrete.md",
    "papers/2024-Smith-Ethics.md",
    "papers/2020-Bender-Stochastic.md",
]

for paper in test_papers:
    try:
        # Your modification logic
        with open(paper, 'r') as f:
            content = f.read()
        frontmatter, body = extract_frontmatter(content)
        fields = parse_frontmatter(frontmatter)

        # Modify...
        fields['test_field'] = 'test_value'

        # Validate
        new_frontmatter = rebuild_frontmatter(fields)
        is_valid, issues = validate_frontmatter(parse_frontmatter(new_frontmatter))
        if not is_valid:
            print(f"FAIL: {paper} - {issues}")
        else:
            print(f"PASS: {paper}")

    except Exception as e:
        print(f"ERROR: {paper} - {e}")
```

---

## Historical Context

### Session 8 (Jan 2026): Unquoted Wikilinks
- **Issue:** 157 files with unquoted `[[wikilinks]]` in YAML
- **Impact:** YAML parsing errors in Obsidian
- **Fix:** `PYTHON/fix_unquoted_local_pdf.py` (146 local_pdf, 11 first_author)
- **Learning:** Always quote wikilinks in YAML frontmatter

### Earlier 2026: Mass Corruption
- **Issue:** 530+ papers with orphaned tags, missing newlines
- **Root Cause:** Scripts using regex on YAML
- **Fix:** Created `yaml_frontmatter_utils.py` library
- **Prevention:** Mandatory library usage + validation

See `Learnings/learnings-log.md` for detailed incident timeline.

---

## Related Standards

- **File Safety:** `file-safety.md` (NO DELETIONS rule)
- **Paper Metadata Schema:** `paper-metadata-schema.md` (field definitions)
- **Classification Logic:** `classification-logic.md` (when to set which fields)

---

## Enforcement

### Pre-commit Hook

```bash
# .git/hooks/pre-commit
# Check for YAML corruption patterns in staged files
if git diff --cached --name-only | grep '^papers/.*\.md$'; then
    python3 PYTHON/validate_yaml_hook.py --staged-only
    if [ $? -ne 0 ]; then
        echo "YAML validation failed - commit rejected"
        exit 1
    fi
fi
```

### Code Review Checklist

Before committing scripts that modify YAML:
- [ ] Uses `yaml_frontmatter_utils.py` library
- [ ] No regex on frontmatter
- [ ] No string concatenation for YAML
- [ ] Validation enabled (`validate=True`)
- [ ] Tested on sample papers first
- [ ] Passes `validate_all_papers.py`

---

**Remember:** YAML is fragile. Always use the library. Always validate. Always test on samples first.

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial standard (migrated from YAML_SAFEGUARDS.md) |
