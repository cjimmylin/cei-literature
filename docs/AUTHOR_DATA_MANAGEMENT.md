# Author Data Management

This document provides comprehensive guidance for managing author data in the CEI Literature Vault.

## Overview

Author metadata in this vault requires careful handling due to:
- Different name formats from various sources (arXiv, CSV, DOI)
- Cultural naming conventions (Malay, Chinese, etc.)
- Edge cases (organizations, single names, usernames)

**Status (Jan 2026):** All 580 papers have complete author names with 100% completion rate.

## Author Data Structure

### Paper Metadata Fields

```yaml
first_author: "Lastname, Firstname"    # CSV format for sorting
authors: "Name One; Name Two; Name Three"   # Semicolon-separated proper names
```

### Paper Body Section

```markdown
## Authors

[[Name One]], [[Name Two]], [[Name Three]]
```

### Author Profile Files

Located in `Authors/`, each author has a profile:

```
Authors/
├── Dario Amodei.md
├── Chris Olah.md
├── Jacob Steinhardt.md
└── ...
```

## Fix Scripts

### 1. complete_author_data_fix.py

**Purpose:** Fetch and fix author data using arXiv API and CSV source.

**Location:** `PYTHON/complete_author_data_fix.py`

**What it does:**
- Extracts arXiv IDs from paper URLs
- Queries arXiv API for complete author lists
- Falls back to CSV data from `Base.md`
- Converts "LastName, FirstName" to "FirstName LastName"
- Updates `authors` and `first_author` fields

**Usage:**
```bash
python3 PYTHON/complete_author_data_fix.py
```

### 2. fix_author_names_comprehensive.py

**Purpose:** Fix incorrectly split author names.

**Location:** `PYTHON/fix_author_names_comprehensive.py`

**What it does:**
- Identifies split names like "Munshi; Amr A."
- Recombines to "Amr A. Munshi"
- Uses arXiv API as source of truth

**Usage:**
```bash
python3 PYTHON/fix_author_names_comprehensive.py
```

### 3. fix_remaining_authors.py

**Purpose:** Apply manual fixes for edge cases.

**Location:** `PYTHON/fix_remaining_authors.py`

**What it does:**
- Reads list of problematic papers
- Applies manual author mappings
- Handles edge cases that can't be auto-fixed

**Usage:**
```bash
python3 PYTHON/fix_remaining_authors.py
```

**Adding new mappings:**
```python
MANUAL_AUTHOR_FIXES = {
    "filename.md": ["Author One", "Author Two"],
}
```

### 4. update_author_wikilinks.py

**Purpose:** Add wikilinks to paper body sections.

**Location:** `PYTHON/update_author_wikilinks.py`

**What it does:**
- Reads `authors` field from frontmatter
- Generates wikilinks `[[Name]]`
- Updates `## Authors` section in paper body

**Usage:**
```bash
python3 PYTHON/update_author_wikilinks.py
```

## Full Workflow

Run scripts in this order:

```bash
# Stage 1: Fetch from arXiv + convert CSV
python3 PYTHON/complete_author_data_fix.py

# Stage 2: Recombine any split names
python3 PYTHON/fix_author_names_comprehensive.py

# Stage 3: Apply manual edge case fixes
python3 PYTHON/fix_remaining_authors.py

# Stage 4: Update wikilinks in paper bodies
python3 PYTHON/update_author_wikilinks.py
```

## Key Techniques

### arXiv API Author Fetching

```python
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import quote

ARXIV_API = "http://export.arxiv.org/api/query?"

def fetch_arxiv_authors(arxiv_id: str) -> list:
    """Fetch complete author list from arXiv API"""
    url = f"{ARXIV_API}search_query=id:{quote(arxiv_id)}&max_results=1"

    with urllib.request.urlopen(url, timeout=5) as response:
        root = ET.fromstring(response.read())
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        authors = []
        for entry in root.findall('atom:entry', ns):
            for author_elem in entry.findall('atom:author', ns):
                name_elem = author_elem.find('atom:name', ns)
                if name_elem is not None:
                    authors.append(name_elem.text.strip())

        return authors
```

### CSV Format Conversion

```python
def convert_csv_format(csv_authors: str) -> list:
    """Convert 'LastName, FirstName' to 'FirstName LastName'"""
    result = []
    for author in csv_authors.split(';'):
        author = author.strip()
        if ',' in author:
            parts = author.split(',', 1)
            lastname = parts[0].strip()
            firstname = parts[1].strip()
            result.append(f"{firstname} {lastname}")
        else:
            result.append(author)
    return result
```

### Name Recombination

```python
def recombine_split_names(authors_str: str) -> list:
    """Fix 'Munshi; Amr A.' -> 'Amr A. Munshi'"""
    parts = [p.strip() for p in authors_str.split(';') if p.strip()]
    result = []
    i = 0

    while i < len(parts):
        current = parts[i]
        # Single word followed by first name -> combine
        if ' ' not in current and i + 1 < len(parts):
            next_part = parts[i + 1]
            result.append(f"{next_part} {current}")
            i += 2
        else:
            result.append(current)
            i += 1

    return result
```

## Edge Cases

### Malay/Indonesian Names

Patronymic naming system where "bin/binti" means "son/daughter of":

| Paper Name | Incorrect | Correct |
|------------|-----------|---------|
| 2025-Zaim Bin Ahmad-... | "Zaim Bin Ahmad; Muhammad Shahrul" | "Muhammad Shahrul Zaim Bin Ahmad" |

**Rule:** Always use the complete legal name as found on the paper or arXiv.

### Organization Authors

Some papers list organizations as authors:

| Paper | Author |
|-------|--------|
| 2024-MLCommons-... | "MLCommons" |
| 2023-Standards-NIST... | "National Institute of Standards and Technology (NIST)" |
| 2023-Lakera-... | "Lakera AI" |

### Single-Name Researchers

Some researchers use only one name:

| Paper | Author |
|-------|--------|
| 2024-Aakanksha-... | "Aakanksha" (followed by co-authors) |

### Username Authors

Dataset papers may use Kaggle/GitHub usernames:

| Paper | Author |
|-------|--------|
| 2023-TheDevastator-HelpSteer... | "TheDevastator" |
| 2023-TheDevastator-OpenAssistant... | "TheDevastator" |

### Accented Characters

Preserve diacritics and special characters:

| Name | Notes |
|------|-------|
| Hal Daumé III | Roman numeral suffix |
| Raúl Cabeza | Spanish accent |
| Félix B. A. Flores | Portuguese/Spanish |
| Peter Øhrstrøm | Danish Ø |

## Validation

### Check for Incomplete Names

```bash
# Single-word author entries (may be split names)
grep -E "^authors:.*\"[A-Z][a-z]+\"$" papers/*.md

# Papers with "et al" or "others"
grep -l "et al\|others" papers/*.md

# Papers missing wikilinks
grep -L "\[\[" papers/*.md | head -20
```

### Validate YAML Structure

```bash
# Single paper
python3 PYTHON/yaml_frontmatter_utils.py papers/2024-Wang-Survey.md

# All papers
for f in papers/*.md; do
    python3 PYTHON/yaml_frontmatter_utils.py "$f" 2>&1 | grep -v "No issues"
done
```

## Author Name Validation (CRITICAL)

**Always validate author names before creating author files.**

### Using the Validation Utility

```python
from author_validation import (
    validate_author_name,      # Check if name is valid
    normalize_author_name,     # Clean up name
    find_full_name_match,      # Expand "A. Smith" -> "Alice Smith"
    safe_create_author_file,   # Create file with validation
)

# ALWAYS do this before creating author files:
is_valid, errors, warnings = validate_author_name(name)
if not is_valid:
    print(f"Invalid: {errors}")
    return  # Don't create the file!

# Or use the safe function:
success, msg = safe_create_author_file(name)
```

### Invalid Patterns (Auto-Rejected)

| Pattern | Example | Reason |
|---------|---------|--------|
| Single letter | `C.`, `M.` | Parse error, not a name |
| Two initials | `A. B.` | No last name |
| Broken wikilink | `Chad]] [[Coleman` | Filename corruption |
| Placeholder | `et al.` | Not a person |
| Generic word | `Center`, `Team` | Not a name |

### Warning Patterns (Review Needed)

| Pattern | Example | Action |
|---------|---------|--------|
| Abbreviated | `A. Smith` | Try `find_full_name_match()` |
| Very short | `Li`, `Kim` | May be legitimate Asian name |

### Scripts for Cleanup

```bash
# Check for issues (dry run)
python3 PYTHON/resolve_author_issues.py

# Apply fixes
python3 PYTHON/resolve_author_issues.py --execute

# Expand abbreviated names using arXiv
python3 PYTHON/expand_abbreviated_authors.py

# Clean orphaned files
python3 PYTHON/cleanup_orphaned_authors.py --execute
```

### Prevention Rules

**NEVER do this:**
```python
# BAD - No validation!
author_file = AUTHORS_DIR / f"{name}.md"
author_file.write_text(content)
```

**ALWAYS do this:**
```python
# GOOD - Validate first
from author_validation import safe_create_author_file
success, msg = safe_create_author_file(name, content)
if not success:
    print(f"Cannot create: {msg}")
```

## Best Practices

1. **Always use `yaml_frontmatter_utils.py`** for YAML operations
2. **Always use `author_validation.py`** before creating author files
3. **Check arXiv first** for papers with arXiv URLs
4. **Preserve accented characters** - use UTF-8 encoding
5. **Update wikilinks** after fixing author names
6. **Add manual mappings** for edge cases to `fix_remaining_authors.py`
7. **Validate YAML** before and after changes
8. **Run `resolve_author_issues.py`** monthly to clean up

## Rate Limits

- **arXiv API:** 0.3 second delay between requests
- No authentication required

## Full Fix Workflow

```bash
# Stage 1: Fetch from arXiv + convert CSV
python3 PYTHON/complete_author_data_fix.py

# Stage 2: Recombine any split names
python3 PYTHON/fix_author_names_comprehensive.py

# Stage 3: Apply manual edge case fixes
python3 PYTHON/fix_remaining_authors.py

# Stage 4: Update wikilinks in paper bodies
python3 PYTHON/update_author_wikilinks.py

# Stage 5: Clean up Authors/ directory
python3 PYTHON/resolve_author_issues.py --execute
```

## Results (Jan 2026)

| Metric | Value |
|--------|-------|
| Total papers | 580 |
| Complete author names | 580 (100%) |
| Author files | 2,894 |
| Wikilinks added | 4,918+ |
| Validation errors | 0 |

## Related Documentation

- `LLM_CONTEXT.md` Section 23 - Author Data Completeness learnings
- `YAML_SAFEGUARDS.md` - YAML frontmatter standards
- `.agent/skills/fix_authors/SKILL.md` - Agent skill
- `.claude/skills/fix-authors.md` - Claude Code skill
- `.claude/commands/fix-authors.md` - Slash command

---

**Last Updated:** January 2026
