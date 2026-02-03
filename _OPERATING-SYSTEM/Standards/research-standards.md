# Research Standards

**Version:** 1.0
**Created:** 2026-02-02
**Category:** Paper Discovery & Verification
**Applies to:** Research and import workflows

---

## Paper Discovery Methodology

### 1. Keyword Search

**Primary sources:**
- **arXiv** - AI/ML/CS papers (pre-prints and published)
- **Semantic Scholar** - Cross-domain academic search
- **Google Scholar** - Broad academic coverage
- **ACL Anthology** - NLP/CL papers
- **OpenReview** - ML conference papers (NeurIPS, ICLR, ICML)

**Search strategies:**

**Broad topics:**
```
"AI ethics" OR "machine ethics" OR "value alignment"
"virtue ethics" AND ("artificial intelligence" OR "AI")
```

**Specific frameworks:**
```
"moral foundations theory" AND "language models"
"deontological" AND "autonomous systems"
```

**Cultural/religious:**
```
"Islamic ethics" AND AI
"Ubuntu" AND "artificial intelligence"
"Confucian values" AND technology
```

### 2. Citation Chaining

**Forward citations:**
- Papers citing key works (e.g., "Concrete Problems in AI Safety")
- Use Semantic Scholar "Cited By" feature
- Check citation count for impact assessment

**Backward citations:**
- References in key papers
- Build foundational knowledge base

### 3. Author Tracking

**Track prolific authors:**
- Dario Amodei (Anthropic - AI Safety)
- Timnit Gebru (DAIR - Fairness)
- Stuart Russell (UC Berkeley - Value Alignment)
- Luciano Floridi (Oxford - Digital Ethics)

**Google Scholar alerts:**
- Set up alerts for key authors
- Monitor new publications

### 4. Venue Monitoring

**Key conferences:**
- **FAccT** (Fairness, Accountability, Transparency)
- **AIES** (AI, Ethics, and Society)
- **NeurIPS** (ML/AI - check ethics track)
- **ACL/EMNLP/NAACL** (NLP - check ethics track)

**Journals:**
- *AI & Society*
- *Ethics and Information Technology*
- *Minds and Machines*

---

## Source Verification

### arXiv ID Validation

**Pattern:** `YYMM.NNNNN` (e.g., `2404.12345`)

**Common errors:**
- **Single-digit typo:** `2404.12345` vs `2404.12346` maps to different papers
- **Version confusion:** v1 vs v2 vs v3

**Verification:**
```bash
# Check if arXiv ID exists
curl -I https://arxiv.org/abs/2404.12345 | grep "HTTP"

# Verify paper title matches
curl https://arxiv.org/abs/2404.12345 | grep -A5 "<title>"
```

### DOI Validation

**Pattern:** `10.NNNN/...` (e.g., `10.1145/1234567`)

**Verification:**
```bash
# Resolve DOI
curl -I https://doi.org/10.1145/1234567 | grep "Location"

# Check Semantic Scholar
curl "https://api.semanticscholar.org/v1/paper/DOI:10.1145/1234567"
```

### URL Verification

**Check for:**
- **Dead links:** Use Wayback Machine if needed
- **Paywalls:** arXiv/OpenReview preferred over paywalled publishers
- **Redirects:** Final URL may differ from original

---

## Metadata Extraction

### Required Fields

1. **Title** - Full paper title
2. **Authors** - All authors (semicolon-separated)
3. **Year** - Publication year
4. **URL** - Primary source URL
5. **Abstract** - For classification

### Extraction Sources (Priority Order)

**arXiv papers:**
```python
# arXiv API provides structured metadata
url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
# Parse XML for title, authors, abstract
```

**Semantic Scholar:**
```python
# Rich metadata including citations
url = f"https://api.semanticscholar.org/v1/paper/{doi}"
# JSON response with all fields
```

**ACL Anthology:**
```bash
# Download BibTeX file
curl https://aclanthology.org/2025.naacl-long.123.bib
# Parse for metadata
```

**Manual extraction:**
- Copy from paper PDF
- Use paper website
- Extract from Google Scholar

---

## Citation Checking

### Verify Citation Count

**Sources:**
- Semantic Scholar API (most reliable)
- Google Scholar (highest counts, but includes non-academic)
- arXiv (only papers citing on arXiv)

**Example:**
```python
def get_citation_count(doi: str) -> int:
    """Fetch citation count from Semantic Scholar."""
    url = f"https://api.semanticscholar.org/v1/paper/{doi}"
    response = requests.get(url)
    data = response.json()
    return data.get('citationCount', 0)
```

**Add to paper metadata:**
```yaml
citation_count: 157
citation_source: "Semantic Scholar"
citation_date: "2026-02-02"
```

### Citation Integrity

**Check for:**
- **Self-citations** (authors citing own work)
- **Citation inflation** (citation count doesn't match impact)
- **Retracted papers** (check Retraction Watch)

---

## Import Workflow

### 1. Paper Discovery
- Find via search, citation, or author tracking
- Verify source (arXiv, Semantic Scholar, publisher)

### 2. Metadata Collection
- Extract all required fields
- Download abstract for classification
- Get DOI/arXiv ID for tracking

### 3. Import to Vault
```bash
# Use import skill
/import-papers

# Or manual:
python3 PYTHON/import_paper_from_zotero.py [zotero_key]
```

### 4. Initial Classification
```bash
# Run classification pipeline
python3 PYTHON/classify_ethics.py papers/[new_paper].md
python3 PYTHON/classify_cultural_religious.py papers/[new_paper].md
# ... (all 7 stages)
```

### 5. PDF Download
```bash
# Use download skill (automated workflow)
/download-pdf [paper_key]

# Downloads PDF → Extracts text → Updates metadata
```

### 6. Validation
```bash
# Verify YAML integrity
python3 PYTHON/validate_all_papers.py papers/[new_paper].md

# Check for duplicates
python3 PYTHON/check_duplicate_papers.py
```

### 7. Git Commit
```bash
git add papers/[new_paper].md
git commit -m "Import: [Year]-[Author]-[Title]"
git push
```

---

## Duplicate Detection

### By DOI
```python
def find_duplicates_by_doi() -> List[Tuple[str, str]]:
    """Find papers with same DOI."""
    doi_map = {}
    for paper in Path("papers").glob("*.md"):
        fm = extract_frontmatter(paper.read_text())
        if 'DOI' in fm:
            doi = fm['DOI']
            if doi in doi_map:
                yield (doi_map[doi], paper.name)
            doi_map[doi] = paper.name
```

### By Title
```python
from difflib import SequenceMatcher

def find_duplicates_by_title(threshold: float = 0.9) -> List[Tuple[str, str]]:
    """Find papers with similar titles."""
    papers = []
    for paper in Path("papers").glob("*.md"):
        fm = extract_frontmatter(paper.read_text())
        title = fm.get('title') or fm.get('short_title', '')
        papers.append((paper.name, title))

    duplicates = []
    for i, (name1, title1) in enumerate(papers):
        for name2, title2 in papers[i+1:]:
            similarity = SequenceMatcher(None, title1.lower(), title2.lower()).ratio()
            if similarity >= threshold:
                duplicates.append((name1, name2))

    return duplicates
```

### Resolution

**If duplicates found:**
1. **Compare metadata** - Which has more complete data?
2. **Check PDF availability** - Which has PDF/extract?
3. **Keep better version** - More enriched, more complete
4. **Move duplicate to RECYCLE-BIN/** - NEVER delete

---

## Quality Standards

### Minimum Metadata Requirements

**For import:**
- ✅ Title (short_title or title)
- ✅ Year
- ✅ First author
- ✅ URL (arXiv, DOI, or publisher)

**Recommended:**
- ✅ Abstract (for classification)
- ✅ All authors
- ✅ DOI (for tracking)
- ✅ Venue (journal/conference)

### Classification Completeness

**After import, all papers should have:**
- `ethics_overall` (Yes/No)
- `newtags` (aggregated tags)
- At least one of: `ethics_perspective`, `research_topic`, or ethics framework

**Check:**
```bash
# Papers missing ethics_overall
grep -L "ethics_overall:" papers/*.md

# Papers missing newtags
grep -L "newtags:" papers/*.md
```

---

## Related Standards

- **API Integration:** `api-integration.md` (source APIs)
- **Classification Logic:** `classification-logic.md` (classification pipeline)
- **YAML Safety:** `yaml-standards.md` (metadata format)

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-02 | Initial research standards |
