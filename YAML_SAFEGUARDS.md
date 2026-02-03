# YAML Frontmatter Safeguards

**⚠️ DEPRECATED:** This file is replaced by `_OPERATING-SYSTEM/Standards/yaml-standards.md`

**Please use the new standards file instead:** [_OPERATING-SYSTEM/Standards/yaml-standards.md](_OPERATING-SYSTEM/Standards/yaml-standards.md)

**Why the change:** Part of progressive disclosure architecture. See `_OPERATING-SYSTEM/README.md`.

---

# YAML Frontmatter Safeguards (Legacy)

## ⛔ CRITICAL: NO FILE DELETIONS

**NEVER use `rm` or delete commands.** Move files to `RECYCLE-BIN/` instead:
```bash
mv file-to-remove.pdf RECYCLE-BIN/
```

---

## The One Rule

**Always use `PYTHON/yaml_frontmatter_utils.py`** for YAML operations:

```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,
    parse_frontmatter,
    rebuild_frontmatter,
    write_paper,
    validate_frontmatter,
)

# Read
frontmatter, body = extract_frontmatter(content)
fields = parse_frontmatter(frontmatter)

# Modify
fields['new_field'] = 'value'

# Write (with validation)
new_frontmatter = rebuild_frontmatter(fields)
write_paper(filepath, new_frontmatter, body, validate=True)
```

## What NOT To Do

| Don't | Why |
|-------|-----|
| **Use `rm` to delete files** | **Destroyed 422 PDFs - use RECYCLE-BIN/** |
| Direct regex on frontmatter | Can corrupt YAML structure |
| String manipulation for reconstruction | Missing newlines cause corruption |
| Create list items without parent key | Orphaned tags break Obsidian |
| Use list format for `newtags` | Must be a string, not YAML list |
| Leave wikilinks unquoted | `[[...]]` without quotes breaks YAML parsing |
| Trust arXiv IDs blindly | Single digit errors map to different papers |

## Wikilink Quoting (Session 8 Learning)

Obsidian wikilinks MUST be quoted in YAML:

```yaml
# WRONG - breaks YAML parsing
local_pdf: [[PDFs/file.pdf]]
first_author: [[Author Name]]

# CORRECT - quoted
local_pdf: "[[PDFs/file.pdf]]"
first_author: "[[Author Name]]"
```

**Fix script**: `python3 PYTHON/fix_unquoted_local_pdf.py`

## Quick Validation

```bash
# Validate single file
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md

# Validate all papers (basic)
python3 PYTHON/validate_all_papers.py

# Enhanced validation (catches more issues)
python3 PYTHON/validate_papers_enhanced.py

# Check for unquoted wikilinks
grep -l "^local_pdf: \[\[" papers/*.md
grep -l "^first_author: \[\[" papers/*.md

# Check for orphaned list items
grep -n "^  - " papers/*.md | head -20
```

## Tag Formats

| Field | Format | Example |
|-------|--------|---------|
| `tags` | YAML list | `tags:\n  - TagOne\n  - TagTwo` |
| `newtags` | String | `newtags: "Virtue Ethics, Deontology"` |
| `manual_tags` | String | `manual_tags: "Ethics; AI Safety"` |

## Frontmatter Structure

```yaml
---
key: "string_value"
another_key: "another value"
nested_list:
  - item1
  - item2
---
```

Requirements:
- `---` markers must have newlines before/after
- List items need parent keys
- Quote strings with special characters

## History

**Session 8 (Jan 2026)**: 157 files with unquoted wikilinks fixed
- 146 `local_pdf` fields
- 11 `first_author` fields
- 5 content mismatches (wrong arXiv IDs) corrected

**Earlier Sessions**: ~530 papers corrupted by:
- Missing newlines in closing markers
- Orphaned list items (no parent key)
- `newtags` written as list instead of string

All fixed. Scripts now use `yaml_frontmatter_utils.py`.

See:
- [docs/SESSION_HISTORY.md](docs/SESSION_HISTORY.md) - Session logs
- [docs/KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md) - Issue catalog & prevention
