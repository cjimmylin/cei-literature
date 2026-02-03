# PDF Download Source Reference

Consolidated reference for downloading academic PDFs from various sources. Learned from Sessions 10-17.

## Quick Reference: Success Rates by Source

| Source | Success Rate | Best For | URL Pattern |
|--------|--------------|----------|-------------|
| **arXiv** | 95% | ML/AI preprints | `arxiv.org/abs/XXXX` → `arxiv.org/pdf/XXXX.pdf` |
| **ACL Anthology** | 90% | NLP/CL papers | `aclanthology.org/ID` → `aclanthology.org/ID.pdf` |
| **OpenReview** | 85% | ICLR, NeurIPS | `openreview.net/forum?id=X` → `openreview.net/pdf?id=X` |
| **PhilArchive** | 85% | Philosophy | Direct PDF links |
| **PhilPapers** | 80% | Philosophy | Some direct PDFs |
| **Nature Sci. Rep.** | 80% | Open access | `nature.com/articles/DOI.pdf` |
| **AAAI/AIES** | 85% | AI ethics conferences | `ojs.aaai.org` has PDFs |
| **CMU faculty pages** | 75% | Faculty papers | Check personal pages |
| **Springer OA** | 70% | OA articles only | `link.springer.com/content/pdf/DOI.pdf` |
| **Semantic Scholar** | 60% | Fallback discovery | API: openAccessPdf field |
| **ScienceDirect** | 30% | Usually paywalled | Institutional access |
| **SAGE Journals** | 20% | Usually paywalled | Institutional access |
| **Academia.edu** | 10% | Requires login | Rarely works |
| **ResearchGate** | 15% | Requires login | Rarely works |

## URL Conversion Patterns

### arXiv
```bash
# Abstract URL → PDF URL
https://arxiv.org/abs/2404.18460 → https://arxiv.org/pdf/2404.18460.pdf

# DOI pattern
DOI: 10.48550/arXiv.2404.18460 → https://arxiv.org/pdf/2404.18460.pdf
```

### ACL Anthology
```bash
# Landing page → PDF
https://aclanthology.org/2024.acl-long.123 → https://aclanthology.org/2024.acl-long.123.pdf
```

### OpenReview
```bash
# Forum URL → PDF URL
https://openreview.net/forum?id=abcd1234 → https://openreview.net/pdf?id=abcd1234
```

### DOI Resolution
```bash
# Generic DOI → Try Unpaywall or direct resolution
https://doi.org/10.xxxx/xxxxx → Follow redirects

# Special DOI patterns
10.48550/arXiv.* → arXiv PDF
10.31219/osf.io/* → OSF PDF
10.2139/ssrn.* → SSRN page
```

## API-Based Discovery

### Semantic Scholar API
```python
url = "https://api.semanticscholar.org/graph/v1/paper/search"
params = {
    'query': title,
    'fields': 'title,authors,openAccessPdf,externalIds',
    'limit': 5
}
# Returns: openAccessPdf.url if available
```

**Rate Limits**:
- Hard limit at ~10-15 requests
- HTTP 429 after limit exceeded
- **Requires 4+ second delays between requests**
- Cool-down period: 10+ minutes

### CrossRef API (DOI Discovery)
```python
url = f"https://api.crossref.org/works?query.title={title}&rows=5"
# Returns: DOI, title, authors
# Good for fuzzy title matching
```

## Paywalled Sources: Alternatives

When automated downloads fail (typically 15-20% of papers):

### Sci-Hub
- Use for papers with DOI
- Paste DOI directly: `sci-hub.se/10.xxxx/xxxxx`
- Mirrors change frequently

### Anna's Archive
- Search by DOI or title
- Best for books and book chapters
- `annas-archive.org`

### LibGen
- Books and some journals
- `libgen.is`

### Institutional Access
- University VPN/proxy
- Google Scholar "PDF" links sometimes work

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| HTTP 403 | Paywall/bot detection | Add User-Agent header; try Sci-Hub |
| HTTP 404 | Wrong URL pattern | Try alternative patterns |
| HTTP 429 | Rate limited | Add delays; use cool-down period |
| HTML returned | Landing page, not PDF | Append `.pdf`; use DOI resolution |
| 0-byte file | Failed download | Verify with `head -c 4` for `%PDF` |

## Verification Commands

```bash
# Check if file is actually PDF
head -c 4 "PDFs/file.pdf"  # Should show "%PDF"

# Find 0-byte files
find PDFs -name "*.pdf" -size 0

# Verify all PDFs are valid
file PDFs/*.pdf | grep -v "PDF document"

# Count PDFs
ls PDFs/*.pdf 2>/dev/null | wc -l
```

## curl Examples

```bash
# Basic download with headers
curl -L -H "User-Agent: Mozilla/5.0" -o "output.pdf" "URL"

# arXiv
curl -L -o "PDFs/2024-Author-Title.pdf" "https://arxiv.org/pdf/2404.18460.pdf"

# Springer OA
curl -L -o "PDFs/2024-Author-Title.pdf" "https://link.springer.com/content/pdf/10.1007/s00146-022-01545-5.pdf"

# ACL Anthology
curl -L -o "PDFs/2024-Author-Title.pdf" "https://aclanthology.org/2024.acl-long.123.pdf"
```

## Python Download Function

```python
import urllib.request
import urllib.error

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

def download_pdf(url: str, filepath: str) -> tuple[bool, str]:
    """Download PDF and verify it's valid."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()

            # Verify PDF magic bytes
            if not data.startswith(b'%PDF'):
                return False, "Not a PDF"

            with open(filepath, 'wb') as f:
                f.write(data)

            return True, f"Downloaded ({len(data)/(1024*1024):.2f} MB)"

    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)
```

## Session-Specific Learnings

### Session 16 (Virtue Ethics Batch Import)
- Semantic Scholar rate limits are strict (429 after ~10 requests)
- Pattern conversion is faster than API-based discovery
- arXiv should always be first attempt

### Session 15 (AI Labs Papers)
- Large PDFs common for AI lab papers (DeepMind: 20-30MB)
- System cards at specific CDNs (Anthropic: assets.anthropic.com)
- Model cards often in GitHub READMEs, not PDFs

### Session 10 (PDF Recovery)
- Multi-source fallback essential
- Checkpoint every 10 papers
- 82% automated recovery rate achievable

## Related Documentation

- [docs/PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) - Full recovery procedures
- [docs/WORKFLOWS.md](WORKFLOWS.md) - PDF download workflows
- [docs/SCRIPTS.md](SCRIPTS.md) - Script reference
