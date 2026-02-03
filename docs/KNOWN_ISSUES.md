# Known Issues & Prevention Guide

This document catalogs known data quality issues discovered during vault maintenance, their root causes, detection methods, and prevention strategies.

## Issue Categories

### 1. Content Mismatches (Critical)

**Description**: Paper metadata (title, authors) points to correct paper, but abstract/PDF contains content from a different paper.

**Root Causes**:
- **arXiv ID transposition**: Single digit errors (e.g., `2507.13208` vs `2507.13175`)
- **Same-title papers**: Concurrent publications with identical titles by different authors
- **PDF download errors**: Wrong PDF mapped to metadata during import

**Detection**:
```bash
# Run content mismatch detector
python3 PYTHON/detect_content_mismatches.py

# Manual check for known contamination patterns
grep -l "contraction.*depth\|matroid\|einstein-podolsky-rosen" papers/*.md
```

**Prevention**:
1. Always verify arXiv ID by checking author names match
2. For same-title papers, include institution or date in verification
3. After PDF download, spot-check that first author name appears in PDF

**Historical Examples**:
| Paper | Wrong ID | Correct ID | Issue |
|-------|----------|------------|-------|
| Brophy | 2507.13208 | 2507.13175 | Single digit transposition |
| Zhao | 1804.09301 | 1804.06876 | Same title, different authors |
| Conwill | 2501.09689 | 2501.10288 | ID transposition |
| Odero | 9-566 | 9-625 | Wellcome article ID wrong |

---

### 2. YAML Syntax Issues (Error)

**Description**: Unquoted Obsidian wikilinks `[[...]]` cause YAML parsing issues.

**Root Causes**:
- Import scripts not quoting wikilink values
- Manual edits forgetting quotes

**Affected Fields**:
- `local_pdf: [[PDFs/file.pdf]]` → should be `"[[PDFs/file.pdf]]"`
- `first_author: [[Name]]` → should be `"[[Name]]"`
- `pdf_extract: [[PDF Extracts/file.md]]` → should be `"[[...]]"`

**Detection**:
```bash
# Check for unquoted wikilinks
grep -l "^local_pdf: \[\[" papers/*.md
grep -l "^first_author: \[\[" papers/*.md
```

**Fix**:
```bash
python3 PYTHON/fix_unquoted_local_pdf.py
```

**Prevention**:
- All import scripts must use `yaml_frontmatter_utils.py`
- Pre-commit hook validates YAML before commit

---

### 3. Extraction Artifacts (Info)

**Description**: `paper_summary` fields contain pipe-delimited concatenated sections.

**Example**:
```yaml
paper_summary: "Abstract: ... | Overview: ... | Methodology: ... | Conclusions: ..."
```

**Root Cause**: PDF extraction pipeline concatenates sections with pipe delimiters.

**Detection**:
```bash
grep -c "paper_summary:.*|.*|" papers/*.md
```

**Status**: Known artifact, not critical. Would require regenerating summaries to fix.

---

### 4. Truncated Abstracts (Warning)

**Description**: Abstract field cut off mid-word or mid-sentence.

**Example**: `abstract: "...comprises 1,785 mul"` (should be "multi-turn dialogues")

**Root Cause**: Character limit during extraction or copy-paste errors.

**Detection**:
```bash
# Find abstracts ending with lowercase letters (possible mid-word)
grep -E 'abstract:.*[a-z]{2,}$' papers/*.md | grep -v '"\s*$'
```

**Fix**: Manually complete abstract from source (arXiv, DOI).

---

### 5. Missing Critical Fields (Error)

**Description**: Required metadata fields are empty or "N/A".

**Critical Fields**:
- `abstract` - Paper abstract
- `authors` - Author list
- `year` - Publication year
- `type` - Document type (journalArticle, conferencePaper, preprint)

**Detection**:
```bash
python3 PYTHON/validate_papers_enhanced.py
```

---

## Code Quality Issues (Session 9)

### 6. Bare Except Clauses (Fixed)

**Description**: Using `except:` without specifying exception types catches all errors, including KeyboardInterrupt and SystemExit.

**Root Cause**: Quick error handling without considering specific exception types.

**Detection**:
```bash
python3 PYTHON/code_quality_check.py
```

**Prevention**:
Always use specific exception types:
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
    logger.error(f"Failed to process data: {e}")
```

**Status**: All 8 instances fixed in Session 9.

---

### 7. Print Statements in Production Scripts (Fixed)

**Description**: Using `print()` instead of logging module makes output uncontrollable.

**Root Cause**: Quick debugging that remained in production code.

**Prevention**:
```python
# Use Python logging module
import logging
logger = logging.getLogger(__name__)

# Instead of print()
logger.info("Processing started")
logger.warning("Potential issue detected")
logger.error(f"Failed: {error}")
```

**Status**: All 28 files converted to logging in Session 9.

---

### 8. Unused Imports (Fixed)

**Description**: Imported modules that are never used in the code.

**Root Cause**: Code refactoring leaving orphaned imports.

**Detection**:
```bash
python3 PYTHON/code_quality_check.py
```

**Status**: All 111 instances cleaned in Session 9.

---

## Validation Scripts

| Script | Purpose | When to Run |
|--------|---------|-------------|
| `validate_all_papers.py` | Basic YAML syntax | After any edit |
| `validate_papers_enhanced.py` | Extended checks (7+ types) | Before commit |
| `detect_content_mismatches.py` | Content/metadata match | After import |
| `fix_unquoted_local_pdf.py` | Fix wikilink quoting | After import |
| `code_quality_check.py` | Code quality & safety | Before committing code |

## QC Process Checklist

### After Importing New Papers

1. [ ] Run `python3 PYTHON/validate_all_papers.py`
2. [ ] Run `python3 PYTHON/validate_papers_enhanced.py`
3. [ ] Run `python3 PYTHON/detect_content_mismatches.py`
4. [ ] Spot-check 3-5 papers: verify arXiv ID matches author names
5. [ ] Fix any errors before committing

### After PDF Downloads

1. [ ] Verify PDF first page shows expected author/title
2. [ ] Run text extraction
3. [ ] Check `pdf_extract` content mentions expected authors

### Monthly Health Check

```bash
# Full validation suite
python3 PYTHON/validate_all_papers.py && \
python3 PYTHON/validate_papers_enhanced.py && \
python3 PYTHON/detect_content_mismatches.py
```

## Key Learnings (Session 8)

1. **arXiv IDs are fragile** - A single digit error maps to completely different papers
2. **Same-title papers exist** - Always verify author names, not just title
3. **YAML wikilinks need quotes** - `[[...]]` without quotes breaks YAML
4. **PDF extraction fails silently** - Wrong content gets extracted without errors
5. **Prevention beats detection** - Validate at import time, not after problems appear


---

## PDF Download Issues

Common problems encountered during PDF downloads and their solutions.

### HTTP 403 Forbidden

**Cause**: Publisher paywall or bot detection

**Symptoms**:
- `HTTP Error 403: Forbidden`
- Access denied messages
- Empty response body

**Solutions**:
1. Add proper User-Agent header: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36`
2. Try Unpaywall API for open access version
3. Check institutional proxy/VPN
4. **Manual**: Use Sci-Hub with DOI
5. **Manual**: Search Anna's Archive

**Prevention**: Start with open access sources (arXiv, ACL, OpenReview)

### HTTP 404 Not Found

**Cause**: Wrong URL pattern, moved content, or invalid ID

**Symptoms**:
- `HTTP Error 404: Not Found`
- Page does not exist

**Solutions**:
1. Try alternative URL patterns for publisher
2. Use DOI resolution instead: `https://doi.org/{doi}`
3. Search paper title on publisher site
4. Check arXiv if academic paper
5. Try Internet Archive Wayback Machine

**Example Fix**:
```python
# Wrong
url = "https://aclanthology.org/2024.paper-1"

# Correct
url = "https://aclanthology.org/2024.paper-1.pdf"
```

### HTML Returned Instead of PDF

**Cause**: Landing page URL instead of direct PDF link

**Symptoms**:
- Response starts with `<!DOCTYPE html>` or `<html>`
- Not a PDF magic bytes `%PDF`

**Solutions**:
1. Append `.pdf` to URL
2. Look for "Download PDF" link in HTML
3. Use DOI resolution
4. Try publisher-specific PDF pattern

**Example Patterns**:
```python
# ACL Anthology
"https://aclanthology.org/{id}" → "https://aclanthology.org/{id}.pdf"

# arXiv
"https://arxiv.org/abs/{id}" → "https://arxiv.org/pdf/{id}.pdf"

# OpenReview
"https://openreview.net/forum?id={id}" → "https://openreview.net/pdf?id={id}"
```

### Invalid or Placeholder DOI

**Cause**: Unpublished paper or data entry error

**Symptoms**:
- DOI contains `xxxxx`: `10.48550/arXiv.2501.xxxxx`
- DOI not found in registries

**Solutions**:
1. Search by title + author on Google Scholar
2. Check preprint servers (arXiv, bioRxiv, SSRN)
3. Search author page on institutional website
4. Contact authors for preprint
5. Paper may not be published yet

**Prevention**: Validate DOIs during paper import

### Rate Limiting / 429 Errors

**Cause**: Too many requests too quickly

**Symptoms**:
- `HTTP Error 429: Too Many Requests`
- Temporary failures
- Slow response times

**Solutions**:
1. Add 0.3-0.5 second delays between requests
2. Use exponential backoff on failures: 1s, 2s, 4s
3. Reduce concurrent requests (max 3-5)
4. Implement checkpoint/resume functionality

**Example**:
```python
import time

for paper in papers:
    download(paper)
    time.sleep(0.5)  # Rate limiting
```

### Zero-Byte or Corrupted PDFs

**Cause**: Download interrupted, server error, or wrong content type

**Symptoms**:
- File size = 0 bytes
- File doesn't open
- `file` command shows: "empty" or "data"

**Solutions**:
1. Check PDF magic bytes: Must start with `%PDF`
2. Verify minimum size (>1KB for real PDFs)
3. Re-download with retry logic
4. Check server response headers

**Verification**:
```bash
# Find 0-byte PDFs
find PDFs -name "*.pdf" -size 0

# Verify PDF format
file PDFs/*.pdf | grep -v "PDF document"
```

### Unpaywall API 422 Errors

**Cause**: Invalid DOI format or API issues

**Symptoms**:
- `HTTP Error 422: Unprocessable Entity`
- Unpaywall can't process DOI

**Solutions**:
1. Validate DOI format: Must start with `10.`
2. Remove extra characters (spaces, quotes)
3. Try direct DOI resolution instead
4. Skip Unpaywall, try other methods

**Workaround**: Use CrossRef or Semantic Scholar instead

### Zotero file:// URLs

**Cause**: Local file paths from Zotero export

**Symptoms**:
- URL starts with `file:///`
- `external_pdf: "file:///Users/..."`

**Solutions**:
1. Use DOI discovery to find online version
2. Search paper title on Google Scholar
3. Check institutional repository
4. **Manual**: Download from publisher if accessible

**Prevention**: Update Zotero export to include online URLs

### Missing DOIs

**Cause**: Paper not in DOI registry, dataset/report, or pre-publication

**Symptoms**:
- `doi:` field empty or missing
- Can't use DOI-based download

**Solutions**:
1. Run `PYTHON/doi_discovery.py` to find DOI
2. Check URL for embedded DOI
3. Search CrossRef by title
4. Generate DOI from repository URL (arXiv, OSF, SSRN)
5. Download using title search

**DOI Generation Patterns**:
```python
# arXiv
"arxiv.org/abs/2401.12345" → "10.48550/arXiv.2401.12345"

# OSF
"osf.io/abc123" → "10.31219/osf.io/abc123"

# SSRN
"ssrn.com/abstract=1234567" → "10.2139/ssrn.1234567"
```

### SSL Certificate Errors

**Cause**: Expired or invalid SSL certificate on publisher site

**Symptoms**:
- `SSL: CERTIFICATE_VERIFY_FAILED`
- Certificate validation error

**Solutions**:
1. Update CA certificates on system
2. Try alternative URL (http vs https)
3. Use different mirror/repository
4. **Not recommended**: Disable SSL verification (security risk)

### Network Timeouts

**Cause**: Slow server, large file, or network issues

**Symptoms**:
- `timeout: timed out`
- `URLError: <urlopen error timed out>`

**Solutions**:
1. Increase timeout: `timeout=60` (60 seconds)
2. Retry with exponential backoff
3. Try during off-peak hours
4. Check network connection

### Redirect Loops or Infinite Redirects

**Cause**: Publisher authentication requirements or broken links

**Symptoms**:
- Too many redirects error
- URL keeps changing

**Solutions**:
1. Check if institutional login required
2. Try direct PDF URL instead of landing page
3. Use DOI resolution
4. Access through proxy/VPN

## Prevention Best Practices

1. **Start with open access** - arXiv, ACL, OpenReview (70%+ success)
2. **Use multiple fallbacks** - Try 3-5 sources before failing
3. **Validate downloads** - Check magic bytes and file size
4. **Rate limit properly** - 0.3-0.5s delays prevent bans
5. **Checkpoint frequently** - Save progress every 10-20 papers
6. **Log everything** - Detailed logs help debugging
7. **Verify DOIs first** - Run DOI discovery before downloading
8. **Exact filenames** - Match paper names exactly for automation

See [docs/PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) for complete troubleshooting guide.
