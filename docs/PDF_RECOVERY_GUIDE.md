# PDF Recovery Guide

This document captures learnings from the 2026-01-24 PDF recovery session where 474 PDFs (82.3%) were successfully recovered after accidental deletion.

## Quick Stats from Recovery

- **Starting point**: 0 PDFs (all deleted)
- **Recovered**: 474 PDFs (82.3%)
- **Methods used**: 8+ different sources
- **Time**: ~2 hours automated + manual search prep
- **Success rate**: 82.3% automated recovery

## Effective Download Sources (In Order of Success)

### 1. arXiv (Highest Success Rate)
- **URL Pattern**: `https://arxiv.org/pdf/{arxiv_id}.pdf`
- **Success**: ~200+ papers
- **Notes**: Direct PDF access, no paywall, fast
- **ID extraction**: From DOI `10.48550/arXiv.{id}` or URLs

### 2. ACL Anthology (Very Reliable)
- **URL Pattern**: `https://aclanthology.org/{paper_id}.pdf`
- **Success**: ~60+ papers
- **Notes**: NLP/CL papers, reliable PDF access
- **ID extraction**: From DOI or conference URLs

### 3. OpenReview (Good for ML Conferences)
- **URL Pattern**: `https://openreview.net/pdf?id={paper_id}`
- **Success**: ~20+ papers
- **Notes**: NeurIPS, ICLR, other ML conferences

### 4. MDPI (Open Access Publisher)
- **URL Pattern**: `https://www.mdpi.com/{journal}/{volume}/{issue}/{article_number}/pdf`
- **Success**: Moderate
- **Notes**: Some papers paywalled, need exact URL
- **Alternative**: Add `?version={timestamp}` parameter

### 5. Nature/Springer (Mixed Results)
- **URL Pattern**: Variable
- **Success**: Low (mostly paywalled)
- **Notes**: Institutional access needed for most
- **Alternatives**: Check institutional repositories, author pages

### 6. Semantic Scholar (DOI Discovery)
- **API**: `https://api.semanticscholar.org/graph/v1/paper/search`
- **Use**: Finding DOIs when missing
- **Rate limit**: 100 requests/5min
- **Success**: Found 1 DOI in our session

### 7. CrossRef (DOI Discovery)
- **API**: `https://api.crossref.org/works?query.title={title}`
- **Use**: Finding DOIs from title
- **Rate limit**: None (polite usage)
- **Success**: Found 5 DOIs in our session

### 8. Unpaywall (Open Access Finder)
- **API**: `https://api.unpaywall.org/v2/{doi}?email={email}`
- **Use**: Finding OA versions of paywalled papers
- **Notes**: Had API issues during session (422 errors)
- **Alternative**: Check OA Button browser extension

## DOI Discovery Methods (When Missing)

### Method 1: URL Pattern Matching
Extract DOIs from URLs using regex patterns:

```python
# Pattern 1: doi.org/10.xxx
r'doi\.org/(10\.\d+/[^\s&?#]+)'

# Pattern 2: Embedded in path
r'/(10\.\d+/[a-zA-Z0-9._-]+)'

# Special cases:
# arXiv: arxiv.org/abs/{id} → 10.48550/arXiv.{id}
# OSF: osf.io/{id} → 10.31219/osf.io/{id}
# SSRN: ssrn.com/abstract={id} → 10.2139/ssrn.{id}
```

### Method 2: Paper Content Scanning
Search paper markdown for DOI patterns:

```python
patterns = [
    r'doi:\s*(10\.\d+/[^\s\n]+)',
    r'DOI:\s*(10\.\d+/[^\s\n]+)',
    r'https?://(?:dx\.)?doi\.org/(10\.\d+/[^\s\n]+)',
]
```

### Method 3: CrossRef Title Search
Search by title with fuzzy matching:

```python
url = f"https://api.crossref.org/works?query.title={title}&rows=3"
# Match if first 30 chars of title similar + year within 1 year
```

### Method 4: Semantic Scholar API
Search with title + author validation:

```python
url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}&limit=3"
# Check externalIds for DOI or ArXiv
```

### Method 5: PubMed Resolution
For biomedical papers with PMID:

```python
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
# Extract DOI from articleids
```

## Common Download Issues & Solutions

### Issue 1: HTTP 403 Forbidden
**Cause**: Publisher paywall or bot detection
**Solutions**:
1. Add proper User-Agent header
2. Try institutional proxy
3. Check for OA version on author page
4. Use Unpaywall API
5. Manual: Sci-Hub, Anna's Archive

### Issue 2: HTTP 404 Not Found
**Cause**: Wrong URL pattern, moved content
**Solutions**:
1. Try alternative URL patterns
2. Check DOI resolution
3. Search paper title on publisher site
4. Try Internet Archive Wayback Machine

### Issue 3: Not a PDF (HTML returned)
**Cause**: Landing page instead of PDF
**Solutions**:
1. Append `.pdf` to URL
2. Look for PDF link in HTML
3. Use DOI resolution instead of direct URL
4. Check URL pattern for publisher

### Issue 3b: Downloaded HTML Masquerading as PDF (Critical!)
**Cause**: curl downloads HTML error/paywall page but saves it as .pdf
**Detection**:
```bash
# Check file type - CRITICAL after every download
file "PDFs/downloaded-paper.pdf"
# Valid: "PDF document, version 1.4"
# Invalid: "HTML document text, ASCII text"

# Batch check for small/invalid files
for f in PDFs/*.pdf; do
  size=$(stat -f%z "$f")
  if [ "$size" -lt 10000 ]; then
    filetype=$(file "$f" | grep -c "PDF document")
    if [ "$filetype" -eq 0 ]; then
      echo "INVALID: $f"
    fi
  fi
done
```
**Cleanup**:
```bash
# NEVER use rm - always move to RECYCLE-BIN
mv "PDFs/invalid-file.pdf" RECYCLE-BIN/
```
**Prevention**: Always verify downloads immediately:
```bash
curl -L -o "file.pdf" "URL" && file "file.pdf" | grep -q "PDF document" && echo "SUCCESS" || echo "FAILED"
```

### Issue 4: Invalid/Placeholder DOI
**Examples**: `10.48550/arXiv.2501.xxxxx`, `10.1234/pending`
**Solutions**:
1. Search author + title on Google Scholar
2. Check preprint servers (arXiv, bioRxiv, etc.)
3. Contact authors
4. Paper may not be published yet

### Issue 5: Rate Limiting
**Symptoms**: Temporary failures, 429 errors
**Solutions**:
1. Add 0.3-0.5 second delays between requests
2. Use exponential backoff on failures
3. Batch processing with checkpoints
4. Consider parallel downloads (max 3-5 concurrent)

## Download Best Practices

### 1. URL Preprocessing
```python
# Convert http to https
url = url.replace('http://', 'https://')

# Clean whitespace
url = url.strip()

# URL encode special characters
from urllib.parse import quote
url = quote(url, safe=':/?#[]@!$&\'()*+,;=')
```

### 2. PDF Verification
```python
# Check magic bytes
if data.startswith(b'%PDF'):
    # Valid PDF

# Check minimum size (avoid error pages)
if len(data) > 1024:  # At least 1KB
    # Likely valid
```

### 3. Progress Tracking
```python
# Save progress every N papers
if i % 10 == 0:
    save_checkpoint()

# Log successes and failures separately
log = {
    "downloaded": {},
    "failed": {},
    "paywalled": {}
}
```

### 4. Retry Strategy
```python
max_retries = 3
backoff = [1, 2, 5]  # seconds

for retry in range(max_retries):
    try:
        download()
        break
    except Exception as e:
        if retry < max_retries - 1:
            time.sleep(backoff[retry])
```

## Batch Download Strategy

### Phase 1: Quick Wins (Open Access)
1. arXiv papers (DOI starts with `10.48550/arXiv`)
2. ACL Anthology papers (DOI contains `/W|P|D|N`)
3. OpenReview papers (URL contains `openreview.net`)
4. MDPI papers (DOI contains `10.3390`)

### Phase 2: DOI-Based Downloads
1. Extract all DOIs
2. Try direct DOI resolution
3. Check Unpaywall for OA versions
4. Use publisher-specific patterns

### Phase 3: URL-Based Downloads
1. Papers with `external_pdf` URLs
2. Clean and normalize URLs
3. Try multiple patterns per publisher
4. Handle redirects

### Phase 4: Manual Search Required
1. Paywalled journals → Sci-Hub, Anna's Archive
2. Missing DOIs → Search by title
3. Books/chapters → LibGen
4. Datasets/reports → Contact authors

## File Naming Convention

**CRITICAL**: Use exact paper filename from vault

```python
# Correct
pdf_path = Path('PDFs') / f"{paper_name}.pdf"

# Where paper_name comes from
paper_name = Path('papers/2024-Smith-Paper Title.md').stem
# Result: "2024-Smith-Paper Title.pdf"
```

**Common mistakes**:
- Don't add extra extensions: ❌ `paper.md.pdf`
- Don't change punctuation: ❌ replacing `:` with `-`
- Don't truncate: ❌ cutting off long titles
- Don't add spaces: ❌ `2024 - Smith - Paper Title.pdf`

## Useful Code Snippets

### Parallel Downloads (Be Careful!)
```python
from concurrent.futures import ThreadPoolExecutor
import time

def download_with_delay(paper):
    time.sleep(0.5)  # Rate limiting
    return download_pdf(paper)

# Max 3-5 workers to avoid rate limits
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(download_with_delay, papers)
```

### Smart Retry with Exponential Backoff
```python
import time
from functools import wraps

def retry_with_backoff(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        raise  # Don't retry 404s
                    if i == max_retries - 1:
                        raise
                    time.sleep(2 ** i)  # 1, 2, 4 seconds
            return None
        return wrapper
    return decorator
```

### Multiple Source Fallback
```python
def try_multiple_sources(doi, title):
    sources = [
        lambda: download_from_doi(doi),
        lambda: download_from_arxiv(doi),
        lambda: download_from_unpaywall(doi),
        lambda: search_and_download(title),
    ]

    for source in sources:
        try:
            result = source()
            if result:
                return result
        except:
            continue

    return None
```

## Manual Search Guide Template

When creating search guides for users:

```markdown
### Paper Title
- **DOI**: `10.xxxx/xxxxx` (if available)
- **Year**: 2024
- **Authors**: Smith et al.
- **Save as**: `EXACT-FILENAME.pdf`
- **Search query**: "Paper Title" Smith 2024
- **Try**:
  1. Sci-Hub: Enter DOI
  2. Anna's Archive: Search by DOI or title
  3. Google Scholar: Look for PDF links
```

## Recovery Statistics Reference

From 2026-01-24 session:

| Source | Papers | % of Total |
|--------|--------|------------|
| arXiv | 200+ | 35% |
| ACL Anthology | 60+ | 10% |
| OpenReview | 20+ | 4% |
| NeurIPS | 15+ | 3% |
| MDPI/Springer/Others | 170+ | 30% |
| **Total Automated** | **474** | **82.3%** |
| Manual needed | 102 | 17.7% |

## Future Improvements

### Priority 1: Automated
- [ ] Implement Unpaywall batch checking
- [ ] Add automatic DOI discovery to import pipeline
- [ ] Create checkpoint/resume for large batches
- [ ] Add duplicate detection (same DOI, different filename)

### Priority 2: Manual Tools
- [ ] Browser extension for one-click PDF save
- [ ] Batch download from Sci-Hub (with delays)
- [ ] Integration with Zotero for PDF recovery

### Priority 3: Monitoring
- [ ] Weekly check for new OA versions
- [ ] Monitor for broken URLs
- [ ] Track publisher URL pattern changes

## Key Learnings

1. **Start with open access sources** - 70%+ success rate
2. **DOI discovery is valuable** - Found 7 new DOIs, got 2 PDFs
3. **Multiple fallbacks essential** - Different publishers need different approaches
4. **Rate limiting prevents bans** - 0.3-0.5s delays work well
5. **Exact filenames critical** - Automation depends on it
6. **Progress tracking saves time** - Checkpoints prevent re-work
7. **API limitations exist** - Unpaywall had 422 errors
8. **Manual completion inevitable** - 15-20% needs human intervention

## Zotero Storage Recovery (Added Jan 2026)

When the user has a local Zotero installation, the Zotero storage folder (`~/Zotero/storage`) contains PDFs that can be recovered or matched to vault papers.

### Zotero Storage Structure

```
~/Zotero/
├── storage/           # PDF attachments (3,500+ items)
│   ├── 225L4DYU/     # 8-character folder IDs
│   │   └── Author et al. - 2024 - Paper Title.pdf
│   ├── 22JPUBT9/
│   │   └── Another Paper.pdf
│   └── ...
├── zotero.sqlite      # Main database
└── styles/            # Citation styles
```

### Matching Vault Papers to Zotero PDFs

**Method 1: CSV Export Matching**

The `Base Source from Zotero.md` CSV contains a `File Attachments` column with full paths:

```python
import csv

with open("Base Source from Zotero.md", 'r') as f:
    reader = csv.DictReader(f)
    for entry in reader:
        year = entry.get('Publication Year', '')
        author = entry.get('Author', '').split(';')[0].split(',')[0]
        files = entry.get('File Attachments', '')
        # Match by year + author last name + title similarity
```

**Method 2: Direct Filename Search**

Search Zotero storage PDFs by filename patterns:

```python
import os
from difflib import SequenceMatcher

zotero_storage = os.path.expanduser("~/Zotero/storage")

# Index all PDFs
zotero_pdfs = []
for folder in os.listdir(zotero_storage):
    folder_path = os.path.join(zotero_storage, folder)
    if os.path.isdir(folder_path):
        for f in os.listdir(folder_path):
            if f.endswith('.pdf'):
                zotero_pdfs.append((f, os.path.join(folder_path, f)))

# Match by year + author + title keywords
def match_paper(year, author, title_words):
    for pdf_name, pdf_path in zotero_pdfs:
        pdf_lower = pdf_name.lower()
        if year in pdf_name and author.lower() in pdf_lower:
            matching = sum(1 for w in title_words if w in pdf_lower)
            if matching / len(title_words) > 0.4:
                return pdf_path
    return None
```

### Recovery Workflow

**Step 1: Identify Missing PDFs**
```python
papers = {f[:-3] for f in os.listdir("papers") if f.endswith('.md')}
pdfs = {f[:-4] for f in os.listdir("PDFs") if f.endswith('.pdf')}
missing = papers - pdfs
print(f"Missing: {len(missing)} PDFs")
```

**Step 2: Match Against Zotero**
- Use CSV matching first (higher accuracy)
- Fall back to filename search for unmatched
- Combine results and calculate total size

**Step 3: Copy with Correct Names**
```python
import shutil

for paper_name, zotero_path in matches:
    dest = f"PDFs/{paper_name}.pdf"
    shutil.copy2(zotero_path, dest)
```

**Step 4: Create PDF Extracts**
```bash
# After copying, run extraction (requires .venv with PyMuPDF)
# Setup if needed: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py --verbose
```

**Step 5: Update Paper Profiles**
```python
from yaml_frontmatter_utils import write_paper, parse_frontmatter

fields['local_pdf'] = f'"[[PDFs/{paper_name}.pdf]]"'
fields['pdf_extract'] = f"PDF Extracts/{paper_name}.md"
```

### Results from Jan 29, 2026 Session

| Metric | Value |
|--------|-------|
| Papers missing PDFs | 134 |
| Matched in Zotero | 66 |
| Total size copied | 165.9 MB |
| Final PDF coverage | 94.9% |

### Key Learnings

1. **Zotero storage is gold mine**: 3,500+ PDFs available for matching
2. **CSV matching more accurate**: Use `File Attachments` column first
3. **Filename matching as fallback**: Works for ~60% of remaining
4. **Unicode issues**: Special characters (ö, í, ė) may cause set comparison mismatches in Python - files still exist
5. **Corrupt files exist**: Check file size - 16-byte files are failed downloads (error codes)
6. **Duplicates happen**: Same paper may exist with slightly different titles - consolidate to the complete version

### Handling Corrupt/Duplicate Files

**Identify corrupt PDFs:**
```bash
find PDFs -name "*.pdf" -size -100c  # Files under 100 bytes
```

**Check content of small files:**
```bash
cat "PDFs/suspect-file.pdf"  # May show "error code: 1020"
```

**Clean up:**
```bash
# NEVER use rm - move to RECYCLE-BIN
mv "PDFs/corrupt-file.pdf" RECYCLE-BIN/
mv "papers/duplicate-paper.md" RECYCLE-BIN/
```

---

## Related Documentation

- [WORKFLOWS.md](WORKFLOWS.md) - PDF download workflow
- [SCRIPTS.md](SCRIPTS.md) - Available download scripts
- [KNOWN_ISSUES.md](KNOWN_ISSUES.md) - Common problems
- [SESSION_HISTORY.md](SESSION_HISTORY.md) - Session logs
