# Author Management Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Author Profile Management
**Applies to:** Author files in `Authors/`

---

## Author Profile Structure

**Location:** `Authors/[Author Name].md`
**Format:** Markdown file with optional YAML frontmatter

**Example:** `Authors/Dario Amodei.md`

```markdown
---
name: "Dario Amodei"
institution: "Anthropic"
position: "CEO"
website: "https://www.anthropic.com"
google_scholar: "https://scholar.google.com/citations?user=..."
twitter: "@darioamodei"
enriched: true
enriched_date: "2026-01-15"
---

# Dario Amodei

## Affiliation
CEO and Co-founder, Anthropic

## Research Interests
- AI Safety and Alignment
- Large Language Models
- Reinforcement Learning from Human Feedback (RLHF)

## Papers in Vault
- [[2016-Amodei-Concrete Problems in AI Safety]]
- [[2022-Bai-Constitutional AI]]

## Bio
Dario Amodei is the CEO and co-founder of Anthropic...
```

---

## Name Validation Rules

### Wikilink Creation Pattern

**From Zotero author string:** `"Smith, John A."`
**To wikilink:** `"[[John A. Smith]]"`

**Conversion logic:**
1. Split on comma: `["Smith", "John A."]`
2. Reverse: `"John A. Smith"`
3. Create wikilink: `"[[John A. Smith]]"`
4. MUST quote in YAML: `first_author: "[[John A. Smith]]"`

### Short Name Handling

**Problem:** Asian surnames (1-2 chars) + Western first names cause conflicts.
- `"Li, John"` → `[[John Li]]`
- `"Li, Jane"` → `[[Jane Li]]`
- Both may refer to different researchers

**Solution:** Add disambiguation with institutional affiliation.
- `[[John Li (Stanford)]]`
- `[[Jane Li (MIT)]]`

**Implementation:**
```python
def disambiguate_author(name: str, institution: str) -> str:
    """Add institution for disambiguation if needed."""
    if is_short_surname(name) and is_common_name(name):
        return f"{name} ({institution})"
    return name
```

**When to use:**
- Surname ≤2 characters (Li, Wu, Kim, Lee)
- Multiple authors with same name pattern in vault

---

## Author Enrichment Workflow

### 1. Profile Creation

**Trigger:** First paper by author imported.
**Auto-created:** Minimal profile with name only.

```bash
# Auto-created by import script
echo "# Dario Amodei\n\n## Papers in Vault\n- [[2016-Amodei-Concrete]]" > "Authors/Dario Amodei.md"
```

### 2. Enrichment (Manual or Automated)

**Add metadata via:**
- Google Scholar lookup
- Institution website
- LinkedIn
- Twitter/X profile
- Personal website

**Fields to add:**
```yaml
institution: "Anthropic"
position: "CEO"
website: "https://..."
google_scholar: "https://scholar.google.com/citations?user=..."
orcid: "0000-0001-2345-6789"
twitter: "@username"
```

### 3. Mark as Enriched

```yaml
enriched: true
enriched_date: "2026-02-02"
```

**Tracking:**
```bash
# Count enriched authors
grep -l "enriched: true" Authors/*.md | wc -l

# Find unenriched first authors
# (Implementation in audit script)
```

---

## Author File Maintenance

### Orphaned Authors

**Definition:** Author files with no papers referencing them.

**Detection:**
```python
def find_orphaned_authors() -> List[Path]:
    """Find author files not referenced by any paper."""
    all_authors = set([f.stem for f in Path("Authors").glob("*.md")])
    referenced_authors = set()

    for paper in Path("papers").glob("*.md"):
        fm = extract_frontmatter(paper.read_text())
        if 'first_author' in fm:
            # Extract author name from wikilink
            author = fm['first_author'].strip('"').strip('[]')
            referenced_authors.add(author)

    orphaned = all_authors - referenced_authors
    return [Path(f"Authors/{a}.md") for a in orphaned]
```

**Causes:**
- Paper deleted but author file remained
- Author name changed in paper but not file renamed
- Duplicate author files with slight name variations

**Fix:**
```bash
# Move to RECYCLE-BIN (NEVER delete)
for f in $(find_orphaned_authors); do
    mv "$f" RECYCLE-BIN/orphaned-authors/
done
```

### Broken Wikilinks

**Problem:** Paper references `[[John Smith]]` but file is `Authors/John A. Smith.md`

**Detection:**
```bash
# Find unresolved author links
# (Obsidian shows these in graph view as broken links)
```

**Fix:**
```python
def repair_broken_author_links(paper_filepath: Path) -> int:
    """Fix author wikilinks by fuzzy matching."""
    # Read paper
    fm, body = extract_frontmatter(paper_filepath.read_text())

    # Extract author from wikilink
    author_link = fm['first_author'].strip('"').strip('[]')

    # Check if file exists
    if not Path(f"Authors/{author_link}.md").exists():
        # Fuzzy match to existing authors
        matches = find_similar_author_names(author_link)
        if len(matches) == 1:
            # Update paper
            fm['first_author'] = f'"[[{matches[0]}]]"'
            write_paper(paper_filepath, rebuild_frontmatter(fm), body)
            return 1

    return 0
```

---

## Batch Enrichment Pattern

**From Session 29 (AI Labs):**

**Pattern:** Launch parallel agents, one per author batch.

```
User specifies: "Enrich all first authors (408 unenriched)"

Claude spawns: 10 agents in parallel (each handling ~40 authors)
- Agent 1: Authors A-D
- Agent 2: Authors E-H
- Agent 3: Authors I-L
...
- Agent 10: Authors T-Z

Result: 8x speedup (3 hours vs 24 hours sequential)
```

**See:** `docs/PARALLEL_AGENT_BEST_PRACTICES.md`

---

## Validation Checks

### Author File Integrity

```bash
# All author files should have .md extension
find Authors/ -type f ! -name "*.md"

# Author files should have name header
grep -L "^# " Authors/*.md

# Check for duplicate names (case-insensitive)
ls -1 Authors/ | tr '[:upper:]' '[:lower:]' | sort | uniq -d
```

### Author-Paper Synchronization

```bash
# Papers with invalid author links
python3 PYTHON/audit_author_links.py

# Authors with no papers
python3 PYTHON/find_orphaned_authors.py

# Papers with missing author files
python3 PYTHON/find_missing_author_files.py
```

---

## Related Standards

- **YAML Safety:** `yaml-standards.md` (first_author field format)
- **Paper Metadata:** `paper-metadata-schema.md` (first_author field)
- **File Safety:** `file-safety.md` (NO DELETIONS on orphaned authors)

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial author management standards |
