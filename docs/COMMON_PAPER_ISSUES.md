# Common Paper Data Issues & Fixes

This document catalogs common data quality issues found in paper files and how to fix them. Use this as a reference when writing scripts or manually fixing issues.

---

## 1. Duplicate Papers

### Detection

Same paper exists in multiple files with:
- Same DOI
- Same title (different filename)
- Same Zotero key

### Examples

```
2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning.md  # Full title
2025-Wang-Diverse Human Value Alignment via Ethical Reasoning.md           # Truncated
```

### Resolution

1. Compare files:
   - More complete metadata → keep
   - Correct author attribution → keep
   - Full title → keep
2. Delete the inferior duplicate
3. Remove corresponding PDF extracts if any

### Script

```python
# Detection
papers_by_doi = defaultdict(list)
for paper in papers:
    doi = frontmatter.get('doi')
    if doi and doi != 'N/A':
        papers_by_doi[doi].append(paper)
duplicates = {k: v for k, v in papers_by_doi.items() if len(v) > 1}
```

### False Positives

- Papers with `doi: N/A` - these are NOT duplicates, just missing DOIs
- Similar titles by different authors - verify by checking all metadata

---

## 2. Invalid local_pdf Format

### Detection

`local_pdf` field not in wikilink format.

### Examples

```yaml
# WRONG
local_pdf: Lit-WS-PDFs/2020-Sap-Social Bias Frames.pdf
local_pdf: N/A

# CORRECT
local_pdf: "[[Lit-WS-PDFs/2020-Sap-Social Bias Frames.pdf]]"
local_pdf:  # Empty if no local PDF
```

### Resolution

```python
if local_pdf and local_pdf != 'N/A':
    if not (local_pdf.startswith('[[') and local_pdf.endswith(']]')):
        new_value = f'[[Lit-WS-PDFs/{local_pdf}]]' if not local_pdf.startswith('Lit-WS-PDFs/') else f'[[{local_pdf}]]'
else:
    # Remove N/A, leave empty
    remove_field('local_pdf')
```

---

## 3. Invalid Type Values

### Detection

Non-standard values in `type` field.

### Valid Values

| Valid | Invalid Variants |
|-------|------------------|
| `journalArticle` | `journal article`, `article` |
| `conferencePaper` | `conference paper`, `workshop paper` |
| `preprint` | - |
| `bookSection` | `book chapter` |
| `book` | `edited volume` |
| `report` | - |
| `thesis` | - |
| `webpage` | - |
| `document` | `whitepaper` |

### Resolution

```python
TYPE_MAPPING = {
    'journal article': 'journalArticle',
    'conference paper': 'conferencePaper',
    'workshop paper': 'conferencePaper',
    'book chapter': 'bookSection',
    'edited volume': 'book',
    'article': 'journalArticle',
    'whitepaper': 'document',
}
if type_value.lower() in TYPE_MAPPING:
    frontmatter['type'] = TYPE_MAPPING[type_value.lower()]
```

---

## 4. Duplicate Citation Entries

### Detection

Citation info section has multiple entries.

### Example

```markdown
## Citation Info

792 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-27] 791 citations (Semantic Scholar/DOI) [2025-08-23]
```

### Types of Duplication

1. **True duplicates** - Same source, same date, different counts (API inconsistency)
2. **Valid multiple entries** - Different sources or dates (keep all)

### Resolution

Keep highest count per (source, date) pair:

```python
def parse_citation(s):
    match = re.match(r'(\d+) citations \(([^)]+)\) \[(\d{4}-\d{2}-\d{2})\]', s)
    return (int(match.group(1)), match.group(2), match.group(3)) if match else None

by_source_date = defaultdict(list)
for c in citations:
    parsed = parse_citation(c)
    if parsed:
        key = (parsed[1], parsed[2])  # (source, date)
        by_source_date[key].append(parsed)

# Keep max count per key
deduped = [max(entries, key=lambda x: x[0]) for entries in by_source_date.values()]
```

---

## 5. Ethics Classification Inconsistency

### Detection

`ethics_overall: "No"` but specific ethics field is `"Yes"`.

### Example

```yaml
ethics_overall: "No"
virtue_ethics: "Yes"  # Contradiction!
```

### Resolution

```python
if ethics_overall == 'No' and any([
    virtue_ethics == 'Yes',
    deontological_ethics == 'Yes',
    utilitarian_ethics == 'Yes'
]):
    frontmatter['ethics_overall'] = 'Yes'
```

---

## 6. Content Warning as Abstract

### Detection

Abstract field < 200 chars and contains "Warning:".

### Example

```yaml
abstract: "Warning: This paper contains explicit statements of offensive stereotypes and may be upsetting."
```

The actual abstract is much longer.

### Resolution

1. Check PDF extract for full abstract
2. Fetch from arXiv/Semantic Scholar API
3. Update YAML abstract field

### Common Patterns

Papers about:
- Bias/hate speech datasets
- Offensive content detection
- Social stereotypes

---

## 7. Broken Author Wikilinks

### Detection

Author wikilinks in body using wrong format.

### Examples

```markdown
# WRONG
[[Zhao, Jieyu]]              # LastName, FirstName
[[Jiahao [[Wang]]]]          # Nested brackets
[[Zhao, Jieyu                # Missing closing ]]

# CORRECT
[[Jieyu Zhao]]               # FirstName LastName
[[Jiahao Wang]]              # Flat, no nesting
```

### Resolution

```python
# Fix LastName, FirstName format
def fix_lastfirst(match):
    last = match.group(1).strip()
    first = match.group(2).strip()
    return f'[[{first} {last}]]'

body = re.sub(r'\[\[([^,\]]+),\s*([^\]]+)\]\]', fix_lastfirst, body)

# Fix nested brackets
body = re.sub(r'\[\[([^\[\]]*)\[\[([^\]]+)\]\]([^\[\]]*)\]\]',
              lambda m: f'[[{m.group(1)}{m.group(2)}{m.group(3)}]]', body)
```

---

## 8. Body Abstract Placeholder

### Detection

Body contains placeholder instead of actual abstract.

### Example

```markdown
## Abstract

*No abstract available in source.*
```

But YAML `abstract:` field has the actual abstract.

### Resolution

```python
if '*No abstract available in source.*' in body and abstract:
    body = body.replace('*No abstract available in source.*', abstract)
```

---

## 9. Empty Required Fields

### Required Fields

- `key`
- `type`
- `year`
- `first_author`
- `authors`
- `ethics_overall`
- `is_benchmark`
- `is_eval`
- `is_dataset`

### Detection

```python
for field in REQUIRED_FIELDS:
    if field not in frontmatter or frontmatter[field] is None:
        issues.append(f"Missing required field: {field}")
```

### Resolution

Depends on field - may need manual research or API fetch.

---

## 10. Truncated Abstract

### Detection

Abstract ends with `...` or `" (truncated)`.

### Example

```yaml
abstract: "We review a broad range of work, primarily in cognitive and social psychology, that provides insight into the processes of moral judgment..."
```

### Resolution

1. Fetch full abstract from arXiv/Semantic Scholar
2. Extract from PDF extract
3. Manual research

---

## Prevention Guidelines

### When Importing Papers

1. Validate YAML immediately after import
2. Check for duplicates before adding
3. Normalize type values during import

### When Running Scripts

1. Always use `yaml_frontmatter_utils.py`
2. Run `validate_all_papers.py` after modifications
3. Use `--dry-run` first

### When Fetching Data

1. Dedupe citations before adding new ones
2. Validate abstract length before updating
3. Check for content warnings in bias/toxicity papers

---

## Quick Verification Commands

```bash
# Check for common issues
grep -l "local_pdf: N/A" papers/*.md | wc -l      # Should be 0
grep -l "type: journal article" papers/*.md | wc -l # Should be 0
python3 PYTHON/validate_all_papers.py              # Should show all valid
python3 PYTHON/comprehensive_audit.py              # Should show 0 errors
```
