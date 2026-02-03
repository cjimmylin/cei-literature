# API Integration Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** External API Usage
**Applies to:** All scripts using arXiv, Semantic Scholar, ACL Anthology, OpenReview

---

## Overview

This standard documents API usage patterns, rate limits, error handling, and caching strategies for external research databases.

---

## arXiv API

### Endpoints
- **Abstract/Metadata:** `https://arxiv.org/abs/{arxiv_id}`
- **PDF Download:** `https://arxiv.org/pdf/{arxiv_id}.pdf`
- **API Query:** `http://export.arxiv.org/api/query?search_query=...`

### Rate Limits
- **No official limit**, but practice good citizenship
- **Recommended:** 1 request per 3 seconds
- **Bulk downloads:** Use delays, don't hammer server

### arXiv ID Format
- **Pattern:** `YYMM.NNNNN` (e.g., `2404.12345` = April 2024, paper #12345)
- **Older papers:** `category/YYMMNNN` (e.g., `cs.AI/0601001`)

### Version Management
Papers get updated on arXiv (v1 → v2 → v3):
- **URL:** `https://arxiv.org/abs/2404.12345v2` (version 2)
- **PDF:** `https://arxiv.org/pdf/2404.12345v2.pdf`
- **Latest:** Omit version number for latest: `https://arxiv.org/abs/2404.12345`

**Verification:**
```bash
# Check latest version
curl -I https://arxiv.org/abs/2404.12345 | grep -i location

# Download specific version
curl -o paper.pdf https://arxiv.org/pdf/2404.12345v2.pdf

# Verify with MD5 checksum
md5sum paper.pdf
```

**Examples of Updated Papers:**
- Llama 3 Herd: v1 → v3
- SAM 2: v1 → v2
- CyberSecEval 3: v1 → v2

### Error Handling

**404 Not Found:**
- Paper doesn't exist or arXiv ID is wrong
- **Common cause:** Single-digit typo (2404.12345 vs 2404.12346)
- **Fix:** Verify ID on arXiv website

**503 Service Unavailable:**
- arXiv server overloaded
- **Fix:** Retry with exponential backoff (wait 5s, 10s, 20s)

### Example Usage

```python
import requests
import time

def fetch_arxiv_abstract(arxiv_id: str) -> dict:
    """Fetch paper metadata from arXiv API."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse XML response
        # ... (implementation)

        return metadata

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"arXiv ID not found: {arxiv_id}")
        elif e.response.status_code == 503:
            print("arXiv server unavailable, retry later")
        raise

    finally:
        time.sleep(3)  # Rate limiting
```

---

## Semantic Scholar API

### Endpoints
- **Paper by DOI:** `https://api.semanticscholar.org/v1/paper/{DOI}`
- **Paper by arXiv:** `https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}`
- **Paper by ID:** `https://api.semanticscholar.org/v1/paper/{s2_id}`
- **Search:** `https://api.semanticscholar.org/graph/v1/paper/search?query=...`

### Rate Limits
- **Public API:** ~100 requests per 5 minutes
- **Response:** `429 Too Many Requests` when exceeded
- **Solution:** Exponential backoff + caching

### Error Handling

**429 Too Many Requests:**
```python
def fetch_with_backoff(url: str, max_retries: int = 5) -> dict:
    """Fetch with exponential backoff on 429."""
    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            wait_time = 2 ** attempt  # 1s, 2s, 4s, 8s, 16s
            print(f"Rate limited, waiting {wait_time}s...")
            time.sleep(wait_time)
            continue

        response.raise_for_status()

    raise Exception("Max retries exceeded")
```

**404 Not Found:**
- Paper not in Semantic Scholar database
- **Common for:** Recent preprints, non-CS papers, obscure venues
- **Fallback:** Use arXiv API or publisher website

### Caching Strategy

```python
import json
from pathlib import Path

CACHE_FILE = Path("logs/semantic_scholar_cache.json")

def get_cached_or_fetch(doi: str) -> dict:
    """Check cache before API call."""
    cache = {}
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r') as f:
            cache = json.load(f)

    if doi in cache:
        print(f"Cache hit: {doi}")
        return cache[doi]

    # Fetch from API
    data = fetch_semantic_scholar(doi)

    # Cache result
    cache[doi] = data
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)

    return data
```

**Cache Location:** `logs/semantic_scholar_cache.json`
**Retention:** Indefinite (results don't change often)

### Example Usage

```python
def update_publication_status(paper_key: str) -> None:
    """Check if preprint is now published."""
    # Get DOI or arXiv ID from paper
    # Query Semantic Scholar
    # Update venue, year if published

    url = f"https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}"

    try:
        data = fetch_with_backoff(url)

        if data.get('venue') and data['venue'] != 'ArXiv':
            # Paper is published!
            venue = data['venue']
            year = data['year']
            # Update paper metadata...

    except Exception as e:
        print(f"Failed to fetch: {e}")
```

---

## ACL Anthology

### URL Patterns
- **Paper Page:** `https://aclanthology.org/{anthology_id}/`
- **PDF:** `https://aclanthology.org/{anthology_id}.pdf`
- **BibTeX:** `https://aclanthology.org/{anthology_id}.bib`

**Anthology ID Format:** `YYYY.venue-type.number`
- Example: `2025.naacl-long.123` (NAACL 2025, long paper #123)

### No Official API
Use web scraping with caution:
- **Prefer:** Direct PDF download via URL pattern
- **Metadata:** Parse BibTeX file
- **Rate limit:** 1 request per 2 seconds

### Example Usage

```bash
# Download paper PDF
curl -o paper.pdf https://aclanthology.org/2025.naacl-long.123.pdf

# Download BibTeX
curl https://aclanthology.org/2025.naacl-long.123.bib
```

---

## OpenReview

### URL Patterns
- **Paper Page:** `https://openreview.net/forum?id={forum_id}`
- **PDF:** `https://openreview.net/pdf?id={forum_id}`
- **API:** `https://api.openreview.net/notes?id={forum_id}`

### API Access
- **Public API:** Available for published venues
- **Rate limits:** Unclear, practice caution
- **Authentication:** Not required for public papers

### Example Usage

```python
def fetch_openreview_abstract(forum_id: str) -> str:
    """Fetch abstract from OpenReview API."""
    url = f"https://api.openreview.net/notes?id={forum_id}"

    response = requests.get(url)
    data = response.json()

    if 'notes' in data and len(data['notes']) > 0:
        return data['notes'][0]['content']['abstract']

    return None
```

---

## Error Handling Best Practices

### Exponential Backoff Template

```python
import time
import requests
from typing import Optional

def fetch_with_retry(
    url: str,
    max_retries: int = 5,
    base_delay: int = 2
) -> Optional[requests.Response]:
    """Generic retry with exponential backoff."""

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                return response

            if response.status_code in [429, 503]:
                wait_time = base_delay ** attempt
                print(f"Retrying in {wait_time}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue

            response.raise_for_status()

        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            time.sleep(base_delay ** attempt)
            continue

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(base_delay ** attempt)
            continue

    return None
```

### Logging API Calls

```python
import logging

logging.basicConfig(
    filename='logs/api_calls.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_api_call(service: str, endpoint: str, status: int) -> None:
    """Log all API interactions."""
    logging.info(f"{service} | {endpoint} | Status: {status}")

# Usage
response = requests.get(url)
log_api_call("arXiv", url, response.status_code)
```

---

## Batch Processing Patterns

### Sequential with Delays

```python
import time

def process_papers_sequential(arxiv_ids: List[str]) -> None:
    """Process papers one at a time with delays."""
    for arxiv_id in arxiv_ids:
        try:
            fetch_arxiv_abstract(arxiv_id)
        except Exception as e:
            print(f"Failed {arxiv_id}: {e}")

        time.sleep(3)  # Rate limiting
```

### Batch with Progress Tracking

```python
from tqdm import tqdm

def process_papers_batch(arxiv_ids: List[str]) -> None:
    """Process with progress bar."""
    for arxiv_id in tqdm(arxiv_ids, desc="Fetching papers"):
        try:
            fetch_arxiv_abstract(arxiv_id)
        except Exception as e:
            print(f"\nFailed {arxiv_id}: {e}")

        time.sleep(3)
```

---

## Related Standards

- **PDF Processing:** `pdf-processing.md` (download workflows)
- **Research Standards:** `research-standards.md` (paper discovery)
- **Learnings:** `../Learnings/learnings-log.md` (API edge cases)

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial API integration standards |
