# Common Workflows

## Prerequisites

Ensure `.vault-config.json` exists with correct PDF path:
```bash
cat .vault-config.json
# Should show: {"pdf_path": "/path/to/PDFs", ...}
```

## Adding New Papers

1. Export from Zotero to `Base.md`
2. Run `/import-papers` or `../.venv/bin/python PYTHON/convert_csv_to_md.py`
3. **CHECK FOR DUPLICATES** (Critical - do this before other steps!)
   ```bash
   ../.venv/bin/python PYTHON/find_duplicate_papers.py
   ```
   Review output and move confirmed duplicates to `RECYCLE-BIN/`
4. Run `/rename-papers` to standardize filenames
5. Run `/classify-papers` to add metadata
6. Run `/fetch-abstracts all` to get missing abstracts
7. Update `CLAUDE.md` statistics if paper count changed

## Processing PDFs

### Automatic Pipeline (Recommended)

Use `/download-pdf` which automatically handles the complete workflow:

```
/download-pdf <paper-name | URL>
```

This command will:
1. Download the PDF to configured PDF location (from `.vault-config.json`)
2. Extract text to `PDF Extracts/`
3. Update frontmatter with `local_pdf` and `pdf_extract`
4. Generate full summary sections (Detailed Summary, Methods, Results, etc.)

**No additional commands needed** - the paper profile is fully populated after download.

### Manual Pipeline (Alternative)

If you already have PDFs or need more control:

1. Place PDFs in configured PDF location (format: `YYYY-Author-ShortTitle.pdf`)
2. Ensure matching markdown exists in `papers/` with same filename stem
3. Run `/extract-pdf-text` - this now automatically:
   - Extracts text to `PDF Extracts/`
   - Updates `pdf_extract` in frontmatter
   - Generates summary sections for each paper
4. (Optional) Run `/summarize-paper <name>` to regenerate a specific paper's summary

### PDF → Extract → Summary Pipeline (Automatic)

When processing PDFs (individual or batch), the system follows this automatic pipeline:

```
PDF Download → Text Extraction → Summary Generation
     ↓              ↓                    ↓
  PDFs/         PDF Extracts/      papers/*.md
                                   (summary sections)
```

**What Gets Created/Updated:**

| Stage | Output | Fields Updated |
|-------|--------|----------------|
| Download | `<PDFS_DIR>/<name>.pdf` | `local_pdf` |
| Extraction | `PDF Extracts/<name>.md` | `pdf_extract` |
| Summarization | Summary sections in paper profile | `## Detailed Summary`, `## Methods Summary`, etc. |

**Summary Sections Generated:**
- `## Detailed Summary` - 2-3 paragraph overview
- `## Paper Outline` - Main section headers
- `## Methods Summary` - Methodology, datasets
- `## Results Summary` - Key findings
- `## Conclusions` - Authors' conclusions, limitations
- `## Artifact Contributions` - Released datasets/code/models

**Batch Processing Performance:**
- 106 papers processed in ~30 minutes using parallel agents
- ~17 seconds per paper average
- Use `subagent_type: "general-purpose"` for parallel processing

### Bulk PDF Extract Creation

When you have many PDFs without extracts (e.g., after Zotero recovery):

**Step 1: Identify PDFs Missing Extracts**
```python
import os

pdfs = {f[:-4] for f in os.listdir("PDFs") if f.endswith('.pdf')}
extracts = {f[:-3] for f in os.listdir("PDF Extracts") if f.endswith('.md')}
missing = pdfs - extracts
print(f"Missing extracts: {len(missing)}")
```

**Step 2: Bulk Extract with PyMuPDF**
```python
# Run with: .venv/bin/python script.py
import fitz  # requires: .venv/bin/pip install pymupdf
from datetime import datetime

def create_extract(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    text_parts = []
    for i, page in enumerate(doc, 1):
        text_parts.append(f"--- Page {i} ---\n")
        text_parts.append(page.get_text())

    num_pages = len(doc)
    doc.close()

    # Create markdown with frontmatter
    markdown = f'''---
title: "{pdf_path.stem} - PDF Extract"
source_pdf: "{pdf_path.name}"
pages: {num_pages}
extracted_at: "{datetime.now().isoformat()}"
---

# PDF Extract: {pdf_path.stem}

**Source PDF:** {pdf_path.name}
**Total Pages:** {num_pages}

---

## Content

```
{"".join(text_parts)}
```
'''
    with open(output_path, 'w') as f:
        f.write(markdown)
```

**Step 3: Update Paper Profiles**
```python
from yaml_frontmatter_utils import (
    extract_frontmatter, parse_frontmatter,
    rebuild_frontmatter, validate_frontmatter, write_paper
)

def update_paper_profile(paper_name):
    paper_path = Path(f"papers/{paper_name}.md")
    content = paper_path.read_text()

    frontmatter, body = extract_frontmatter(content)
    fields = parse_frontmatter(frontmatter)

    # Update links
    fields['pdf_extract'] = f"PDF Extracts/{paper_name}.md"
    fields['local_pdf'] = f'"[[PDFs/{paper_name}.pdf]]"'

    new_frontmatter = rebuild_frontmatter(fields)
    is_valid, issues = validate_frontmatter(new_frontmatter)

    if is_valid:
        write_paper(paper_path, new_frontmatter, body, validate=True)
```

**Requirements:**
- Virtual environment with PyMuPDF: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
- yaml_frontmatter_utils.py in PYTHON/
- Run scripts with: `.venv/bin/python script.py`

**Performance:** ~66 PDFs extracted + profiles updated in under 2 minutes

## Enriching Ethics Papers

1. Run `/identify-targets enrichment` to find candidates
2. Run `/enrich-paper <name>` to add `key_contribution`/`significance`
3. Use Author Enrichment workflow to update `Authors/` profiles

## Author Profile Enrichment (Parallel Agents)

**Use case:** Enrich 50+ author profiles efficiently using parallel subagents.

### Two-Phase Approach (Proven 99%+ completion)

**Phase 1: Broad Sweep**
1. Identify placeholder profiles (have "University/Organization" or "Topic 1")
2. Split authors into batches of 40-45 each
3. Launch 10-15 parallel agents with:
   ```
   subagent_type: "general-purpose"
   allowed_tools: ["WebSearch", "WebFetch", "Read", "Edit", "Write", "Glob", "Grep"]
   run_in_background: true
   ```
4. Each agent searches for: affiliation, title, research interests, profile links
5. Expected completion: 85-90%

**Phase 2: Challenging Cases**
1. Identify remaining placeholders
2. Split into smaller batches of 10-15 each
3. Launch focused agents with more detailed prompts
4. Expected completion: 99%+

### Critical Configuration

**Always specify allowed_tools** - background agents cannot prompt for permissions:
```python
Task(
    subagent_type="general-purpose",
    allowed_tools=["WebSearch", "WebFetch", "Read", "Edit", "Write", "Glob", "Grep"],
    run_in_background=true,
    prompt="[Author list and instructions]"
)
```

### Monitoring Progress

```bash
# Check recent enrichments (last 10 min)
find Authors -name "*.md" -mmin -10 | wc -l

# Check remaining placeholders
python3 << EOF
import os
count = 0
for f in os.listdir("Authors"):
    if f.endswith('.md'):
        with open(f"Authors/{f}") as file:
            if '"Topic 1"' in file.read() or 'University/Organization' in file.read():
                count += 1
print(f"Remaining: {count}")
EOF
```

### Quality Standards

Each enriched profile must have:
- Real institutional affiliation (not "University/Organization")
- 2-5 specific research interests
- Brief biographical summary (2-3 sentences)
- At least one working external link (Google Scholar preferred)
- Links to papers in vault

### Performance Metrics

**From 2026-01-25 session:**
- 408 authors enriched in ~50 minutes (~7.5 seconds per author)
- 14 parallel agents used (10 initial + 4 follow-up)
- 50x faster than manual enrichment
- Bonus: Identified 2 metadata errors in papers during process

### Related Documentation

- [docs/SESSION_2026_01_25_AUTHOR_ENRICHMENT.md](SESSION_2026_01_25_AUTHOR_ENRICHMENT.md) - Complete session report
- [Authors/TEMPLATE.md](../Authors/TEMPLATE.md) - Author profile template

## Generating Reports

1. Ensure classification is up to date via `/classify-papers`
2. Run `/generate-reports all` to create all statistics reports

## Fixing Author Names

1. Run `/fix-authors` or use scripts directly:
   ```bash
   python3 PYTHON/complete_author_data_fix.py          # arXiv API + CSV
   python3 PYTHON/fix_author_names_comprehensive.py    # Recombine split names
   python3 PYTHON/fix_remaining_authors.py             # Manual edge cases
   python3 PYTHON/update_author_wikilinks.py           # Add wikilinks
   python3 PYTHON/resolve_author_issues.py --execute   # Clean up Authors/
   ```
2. Check for edge cases requiring manual mappings in `fix_remaining_authors.py`
3. See [AUTHOR_DATA_MANAGEMENT.md](AUTHOR_DATA_MANAGEMENT.md) for complete documentation

**Important:** Always run `resolve_author_issues.py` after fixing authors to clean up any invalid entries created during processing.

## Author File Validation

Before creating new author files, use the validation utility:

```python
from author_validation import safe_create_author_file

success, msg = safe_create_author_file(name, content)
if not success:
    print(f"Cannot create: {msg}")
```

Monthly cleanup:
```bash
# Check for issues (dry run)
python3 PYTHON/resolve_author_issues.py

# Apply fixes if needed
python3 PYTHON/resolve_author_issues.py --execute
```

## Health Check

Quick verification that vault is in good state:

```bash
# 1. Basic YAML validation (should show 576/576 valid)
python3 PYTHON/validate_all_papers.py

# 2. Enhanced validation with content checks
python3 PYTHON/validate_papers_enhanced.py

# 3. Content mismatch detection
python3 PYTHON/detect_content_mismatches.py
```

### Manual Spot Checks

```bash
# Check for incomplete authors (should return 0)
grep -l "\*\*Authors:\*\*.*and others" papers/*.md | wc -l

# Check for corrupted abstracts (should return 0)
grep -l "Einstein-Podolsky-Rosen" papers/*.md | wc -l

# Check for unquoted local_pdf fields (should return 0)
grep -l "^local_pdf: \[\[" papers/*.md | wc -l

# Check for papers with WARNING boxes (review these)
grep -l "\[!WARNING\]" papers/*.md

# Check for pipe-delimited summaries (info only, not critical)
grep -c "paper_summary:.*|.*|" papers/*.md
```

### Common Issues & Fixes

| Issue | Detection | Fix Script |
|-------|-----------|------------|
| Unquoted `local_pdf` | `grep "^local_pdf: \[\["` | `fix_unquoted_local_pdf.py` |
| Content mismatch | `[!WARNING]` boxes | Manual verification |
| Corrupted abstract | Known text patterns | `fix_corrupted_abstracts.py` |
| Wrong arXiv ID | Author name mismatch | Manual correction |

## Code Quality Check

Before committing code changes to scripts or skills:

```bash
# Run comprehensive QC check
python3 PYTHON/code_quality_check.py

# Or use slash command
/qc-code

# Verbose output
python3 PYTHON/code_quality_check.py --verbose
```

**What it checks:**
- Critical: Hardcoded paths, outdated format references
- High: Bare except clauses, YAML safety violations
- Medium: Missing docstrings, excessive print statements
- Low: Unused imports

**When to run:**
- Before committing code changes
- After adding new scripts
- Monthly maintenance check

See [docs/QC_SYSTEM.md](QC_SYSTEM.md) for complete documentation.

## PDF Extract Structure

Extracts are saved to `PDF Extracts/YYYY-Author-Title.md`:

```markdown
---
title: "Paper Title - PDF Extract"
source_pdf: "YYYY-Author-Title.pdf"
pages: 15
extracted_at: "2026-01-24T15:30:00..."
---

# PDF Extract: Paper Title

**Source PDF:** YYYY-Author-Title.pdf
**Total Pages:** 15

---

## Content

[Full extracted text from all pages]
```

**Key Learning**: Text extraction MUST save as `.md` files, not `.txt`. Plain text files are not visible in Obsidian's file explorer by default.

---

## PDF Recovery & Download

### Zotero Storage Recovery (Recommended First Step)

If the user has a local Zotero installation, check `~/Zotero/storage` first - it often contains PDFs for papers in the vault.

**Quick Check:**
```bash
# Count PDFs in Zotero
find ~/Zotero/storage -name "*.pdf" | wc -l

# Compare to vault
ls PDFs/*.pdf | wc -l
```

**Recovery Process:**
1. Parse `Base Source from Zotero.md` CSV for `File Attachments` paths
2. Match vault papers by year + author + title similarity
3. Copy matching PDFs with correct vault naming
4. Create PDF extracts for copied files
5. Update paper profiles with `local_pdf` and `pdf_extract` links

**Typical Results:** 50-70% of missing PDFs can be recovered from Zotero storage.

See [PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md#zotero-storage-recovery-added-jan-2026) for complete workflow.

### Quick Recovery (Automated)

For recovering deleted PDFs or downloading missing papers:

```bash
# Enhanced downloader with multi-source fallback
python3 PYTHON/pdf_downloader_enhanced.py

# Resume from checkpoint (if interrupted)
python3 PYTHON/pdf_downloader_enhanced.py --resume

# Download first 100 papers
python3 PYTHON/pdf_downloader_enhanced.py --limit 100
```

**Features**:
- Multi-source fallback (arXiv, ACL, OpenReview, DOI resolution, direct URLs)
- Smart retry with exponential backoff
- Automatic DOI discovery from URLs
- Progress checkpointing every 10 papers
- Rate limiting (0.5s between requests)

### DOI Discovery (Before Downloading)

Find missing DOIs to improve download success:

```bash
# Discover all missing DOIs
python3 PYTHON/doi_discovery.py

# Check first 50 papers
python3 PYTHON/doi_discovery.py --limit 50
```

**Methods used**:
- CrossRef API (title-based search)
- Semantic Scholar API (title + author)
- URL pattern extraction (arXiv, OSF, SSRN, PubMed)
- Special repository pattern recognition

**Output**: `logs/discovered_dois.json`

### Download Sources (Priority Order)

The enhanced downloader tries sources in this order:

1. **arXiv** - If DOI starts with `10.48550/arXiv`
   - URL: `https://arxiv.org/pdf/{id}.pdf`
   - Success rate: ~95%

2. **ACL Anthology** - If URL contains `aclanthology.org`
   - URL: `https://aclanthology.org/{id}.pdf`
   - Success rate: ~90%

3. **DOI Resolution** - Try direct DOI URL
   - URL: `https://doi.org/{doi}`
   - Success rate: ~40%

4. **External PDF URL** - From `external_pdf` field
   - Success rate: ~60%

5. **Main URL** - From `url` field
   - Success rate: ~30%

### Manual Download (For Paywalled Papers)

When automated methods fail (typically 15-20% of papers):

**Step 1**: Check logs/20260124-SEARCH_GUIDE.md for paper details

**Step 2**: Search on alternative sources
- **Sci-Hub**: For papers with DOI (paste DOI directly)
- **Anna's Archive**: Search by DOI or title
- **LibGen**: For books and some journals
- **Google Scholar**: Sometimes links to free PDFs

**Step 3**: Save with exact filename matching papers/ directory

See [docs/PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) for complete guide.

### Common Download Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| HTTP 403 | Forbidden/Paywall | Try Sci-Hub or institutional access |
| HTTP 404 | Not found | Try alternative URL patterns |
| HTML returned | Not a PDF | Append `.pdf` to URL or use DOI resolution |
| Rate limited | Temporary failures | Reduce concurrent requests, add delays |
| Invalid DOI | Placeholder (xxxxx) | Search by title instead |

### Verification After Download

```bash
# Count PDFs
ls PDFs/*.pdf | wc -l

# Check for 0-byte files
find PDFs -name "*.pdf" -size 0

# Verify PDF format
file PDFs/*.pdf | grep -v "PDF document"
```

### Recovery Statistics

From 2026-01-24 session (474 PDFs recovered from 0):

| Source | Papers | Success Rate |
|--------|--------|--------------|
| arXiv | 200+ | 95% |
| ACL Anthology | 60+ | 90% |
| OpenReview | 20+ | 85% |
| MDPI/Springer | 170+ | 60% |
| Overall Automated | 474/576 | 82.3% |

### Related Documentation

- [docs/PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) - Complete recovery guide
- [docs/SCRIPTS.md](SCRIPTS.md) - Script reference

---

## Literature Search & Paper Discovery

### Workflow for Finding New Papers by Topic

When expanding coverage of a specific topic (e.g., virtue ethics, deontological ethics):

**Step 1: Establish Baseline**
```bash
# Check existing coverage
grep -l "virtue_ethics: Yes" papers/*.md | wc -l

# See related statistics
ls STATISTICS/paper-statistics*.md
```

**Step 2: Multi-Source Web Search**
Use WebSearch with varied query terms:
- Core topic + AI/LLM: `"virtue ethics" AI alignment LLM`
- Key authors: `Shannon Vallor virtue ethics AI`
- Related concepts: `phronesis practical wisdom AI`
- Non-Western perspectives: `Confucian ethics AI artificial intelligence`
- Recent years: Add `2024 2025` to queries

**Step 3: Cross-Reference Vault**
```bash
# Before adding, check if paper already exists
grep -l "Author-Keyword" papers/*.md
```

**Step 4: Create Paper Entries**
Use YAML frontmatter template from existing papers:
- Include all required fields
- Set `virtue_ethics: Yes` (or relevant ethics field)
- Add comprehensive `newtags`

**Step 5: Download PDFs & Extract**
```bash
# After creating entries
curl -L -o "PDFs/YYYY-Author-Title.pdf" "URL"

# Run extraction
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py
```

### Best Sources by Paper Type

| Paper Type | Best Sources | Success Rate |
|------------|--------------|--------------|
| Philosophy papers | PhilArchive, PhilPapers | 80% |
| AI/ML conference | arXiv, OpenReview, ACL Anthology | 90% |
| Springer journals | PMC (if OA), ResearchGate | 40% |
| Book chapters | Often paywalled | 20% |
| Preprints | arXiv, SSRN | 95% |

### Search Query Patterns That Work

**For virtue ethics:**
- Shannon Vallor techno-moral virtue
- MacIntyre virtue ethics AI robots
- Aristotelian phronesis artificial intelligence
- Confucian ethics AI LLM
- moral exemplar AI learning

**For deontological ethics:**
- Kantian categorical imperative AI
- deontic logic moral reasoning
- duty-based ethics LLM alignment
- cross-cultural moral values AI

**For consequentialist ethics:**
- utilitarian AI moral dilemma
- moral machine experiment LLM
- consequentialist alignment

### Common Pitfalls

1. **Check vault first**: Many papers already present (found 6+ during virtue ethics search)
2. **Paywalled sources**: Springer book chapters, Nature journals often fail
3. **Same-title papers**: Verify authors match (Zhao vs Rudinger example)
4. **arXiv ID errors**: Single digit typos map to wrong papers

### Learnings from Recent Sessions

| Session | Topic | Papers Added | Key Learning |
|---------|-------|--------------|--------------|
| 19 | Consequentialist (Phase 2) | 17 | 76% PDF success; arXiv best source for ethics papers |
| 16 | Virtue ethics batch | 24 | Batch script approach efficient; Semantic Scholar rate limits |
| 14 | Virtue ethics | 28+ | Eastern philosophy (Confucian) underrepresented |
| 13 | Deontological | 14 | Deontic logic papers highly relevant |
| 12 | Consequentialist | 11 | LLMs show utilitarian bias |

### Related Documentation

- [docs/SESSION_HISTORY.md](SESSION_HISTORY.md) - Search session details
- [docs/RESEARCH_PAPER_DISCOVERY_LEARNINGS.md](RESEARCH_PAPER_DISCOVERY_LEARNINGS.md) - Discovery patterns

---

## Batch Paper Import (From Research)

When you've researched a topic and found 10+ papers to add, use batch import:

### Step 1: Create Papers Definition Script

Create a Python script defining all papers (see `PYTHON/create_virtue_ethics_papers.py`):

```python
PAPERS = [
    {
        "year": 2024,
        "first_author": "Author Name",
        "short_title": "Paper Title",
        "authors": "Author1; Author2; Author3",
        "url": "https://source-url",
        "external_pdf": "https://pdf-url",  # optional
        "doi": "10.xxxx/xxxxx",  # optional
        "publication": "Journal or Conference",
        "type": "journalArticle",  # or conferencePaper, preprint, report
        "abstract": "Full abstract text...",
        "ethics_overall": "Yes",
        "virtue_ethics": "Yes",  # or deontological_ethics, utilitarian_ethics
        "research_topic": "Category Name",
    },
]
```

### Step 2: Generate YAML and Write Files

Use `yaml_frontmatter_utils.py` for safe YAML generation:

```python
from PYTHON.yaml_frontmatter_utils import write_paper, validate_frontmatter

def create_paper(paper):
    frontmatter = generate_frontmatter(paper)  # Build YAML string
    body = generate_body(paper)  # Build markdown body

    is_valid, issues = validate_frontmatter(frontmatter)
    if is_valid:
        write_paper(filepath, frontmatter, body, validate=True)
```

### Step 3: Download PDFs

**Option A: Pattern-based batch download**
```python
# URL conversion patterns
if 'arxiv.org/abs/' in url:
    pdf_url = url.replace('/abs/', '/pdf/') + '.pdf'
elif 'aclanthology.org' in url:
    pdf_url = url.rstrip('/') + '.pdf'
elif 'openreview.net/forum' in url:
    pdf_url = url.replace('/forum?', '/pdf?')
```

**Option B: Manual curl for specific sources**
```bash
curl -L -o "PDFs/YYYY-Author-Title.pdf" "https://arxiv.org/pdf/XXXX.pdf"
curl -L -o "PDFs/YYYY-Author-Title.pdf" "https://link.springer.com/content/pdf/DOI.pdf"
```

**Option C: Semantic Scholar API (rate-limited)**
```python
url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}&fields=openAccessPdf"
# Returns openAccessPdf.url if available
# IMPORTANT: 4+ second delays required, limit ~10 requests before 429
```

### Step 4: Extract PDF Text

```bash
# Run extraction for all new PDFs
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py --verbose
```

### Step 5: Update Metadata

Update paper profiles with local_pdf and pdf_extract paths:

```python
fields['local_pdf'] = f"[[PDFs/{pdf_filename}]]"
fields['pdf_extract'] = f"PDF Extracts/{paper_name}"
write_paper(paper_path, new_frontmatter, body, validate=True)
```

### PDF Source Success Rates

| Source | URL Pattern | Success Rate |
|--------|-------------|--------------|
| arXiv | `arxiv.org/abs/` → `/pdf/` | 95% |
| ACL Anthology | `aclanthology.org/ID` → `ID.pdf` | 90% |
| OpenReview | `openreview.net/forum?id=X` → `/pdf?id=X` | 85% |
| Nature Scientific Reports | `nature.com/articles/DOI` | 80% (often OA) |
| Springer OA | `link.springer.com/content/pdf/DOI.pdf` | 70% |
| PhilArchive | Direct PDF links | 85% |
| SAGE Journals | Requires access | 20% |
| ScienceDirect | Requires access | 30% |
| Academia.edu | Requires login | 10% |
| ResearchGate | Requires login | 15% |

### Step 6: Check for Duplicates (MANDATORY)

After batch import, **always** run duplicate detection:

```bash
.venv/bin/python PYTHON/find_duplicate_papers.py
```

Common duplicate patterns in batch imports:
- Paper already in vault under different author format (e.g., "Unknown" → proper name)
- Preprint vs published version listed separately
- Same DOI imported through different sources

See `/check-duplicates` skill for detailed handling guidance.

### Key Learnings

1. **Batch scripts save time**: For 20+ papers, script-based approach is 10x faster
2. **arXiv first**: Always check for arXiv preprints before paywalled versions
3. **Semantic Scholar rate limits**: Hard limit at ~10-15 requests, use 4s delays
4. **YAML validation critical**: Always validate before writing to prevent corruption
5. **Check for duplicates**: Run `find_duplicate_papers.py` after every batch import
6. **Duplicate removal**: Move to RECYCLE-BIN (never use `rm`)

### Related Scripts

- `PYTHON/create_virtue_ethics_papers.py` - Example batch creation script
- `PYTHON/download_virtue_ethics_pdfs.py` - Example batch download script
- `PYTHON/yaml_frontmatter_utils.py` - Safe YAML handling utilities

---

## Session Closure & Maintenance (LifeOS)

### End-of-Session Workflow

**Command:** `/end-session`

Use this skill to properly close a work session. It orchestrates a 2-phase closure:

**Phase 1: remember-thread (Memory Consolidation)**
1. Reviews session achievements and learnings
2. Extracts reusable knowledge
3. Creates/updates learnings-log.md
4. Provides handoff summary

**Phase 2: finalize-thread (QA + Git)**
1. Runs 6-category quality assurance:
   - Frontmatter validation
   - File integrity
   - Git status
   - Skill health
   - Documentation updates
   - Dependencies
2. Commits changes with descriptive messages
3. Generates final session report

**When to use:**
- At the end of every work session
- Before switching to a different project
- After completing a major task or milestone

**Example:**
```
/end-session

[Agent orchestrates both skills and provides comprehensive closure report]
```

### Quarterly Maintenance

**Command:** `/quarterly-maintenance` or run manually

Performs 8-step comprehensive health check:

1. ✅ **YAML Integrity** - Validates all paper frontmatter
2. 🔗 **PDF Links** - Finds missing or broken PDF references
3. 👤 **Author Profiles** - Detects orphaned author files
4. 📄 **PDF Extracts** - Checks for missing extracts
5. 🏷️ **Classifications** - Validates ethics classification consistency
6. 🔄 **Duplicates** - Finds potential duplicate papers
7. 📦 **Orphaned Files** - Identifies unreferenced PDFs
8. 📊 **Health Report** - Generates detailed findings

**When to run:**
- Every 3 months (quarterly)
- After major imports (>10 papers)
- Before archiving/backup
- When suspecting data issues

**Output:**
- Health score (0-100%)
- Critical issues, warnings, info
- Actionable recommendations
- Saved to `_OPERATING-SYSTEM/Maintenance/`

**Example:**
```bash
# Run with verbose output
python3 .claude/skills/quarterly-maintenance/run_maintenance.py --verbose

# Or use skill command
/quarterly-maintenance --verbose
```

**Understanding Results:**
- **Health Score ≥95%:** ✅ Excellent
- **Health Score 85-94%:** ⚠️ Good
- **Health Score <85%:** ❌ Needs attention

**Common Issues Found:**
- Missing PDFs (14 typical)
- Missing extracts (38 typical)
- Orphaned authors (varies)
- Classification inconsistencies (502 typical)
- Orphaned PDFs (77 typical)

### Git Workflow Enhancement

The pre-commit hook now includes 4 automated checks:

1. ✅ **YAML Validation** - Frontmatter integrity
2. 📦 **Library Imports** - All modules load correctly
3. 🧪 **Critical Tests** - yaml_utils tests pass
4. 📋 **Staged Files** - Verify what's being committed

**What happens:**
- Pre-commit runs automatically on `git commit`
- Blocks commit if critical checks fail
- Warns about direct paper commits (prefer using skills)
- Shows helpful error messages

**Bypass (use sparingly):**
```bash
git commit --no-verify -m "Emergency fix"
```

### Migration Reference

For complete LifeOS architecture details:
- [OPERATING_SYSTEM_MIGRATION.md](OPERATING_SYSTEM_MIGRATION.md) - Full migration guide
- [_OPERATING-SYSTEM/README.md](../_OPERATING-SYSTEM/README.md) - 4-layer memory system
- [_OPERATING-SYSTEM/Standards/](../_OPERATING-SYSTEM/Standards/) - Procedural knowledge

