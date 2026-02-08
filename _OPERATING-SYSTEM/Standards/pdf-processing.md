# PDF Processing Standards

**Version:** 1.1
**Created:** 2026-02-02
**Category:** PDF Download & Extraction
**Applies to:** PDF workflows

---

## PDF Download Workflow

### Multi-Source Strategy (Priority Order)

1. **arXiv** (if arXiv ID available)
2. **Unpaywall** (DOI → OA PDF lookup)
3. **EuropePMC / PubMed Central** (DOI → PMCID → ptpmcrender PDF)
4. **Semantic Scholar** (title/DOI → OA PDF)
5. **OpenAlex** (title search → OA locations incl. preprints like Research Square, SSRN)
6. **Publisher website** (DOI scrape: Nature, PLOS, Springer, MDPI d_attachment, PNAS, etc.)
7. **ACL Anthology** (for NLP/CL papers)
8. **OpenReview** (for ML conference papers — NeurIPS, ICML, ICLR)
9. **NeurIPS direct** (proceedings URL → PDF URL pattern)
10. **Zotero backup** (`~/Zotero/storage` - read-only)

### Strategy Tips

Non-obvious patterns discovered during PDF acquisition campaigns:

- **MDPI `d_attachment`:** More reliable than `/pdf` suffix. Look for `mdpi-res.com/d_attachment/` links in the HTML, or construct from journal/volume/article metadata.
- **NeurIPS direct URL:** Replace `-Abstract-Conference.html` with `-Paper-Conference.pdf` in the URL. Also works for `-Abstract-Datasets_and_Benchmarks.html` track variants.
- **AAAI OJS 3-part URL:** Requires `article/download/{article_id}/{galley_id}/{submission_file_id}`. The search API only returns `article_id`; the galley and file IDs must be scraped from the article page.
- **EuropePMC `ptpmcrender`:** For PMC-deposited papers, construct `https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMCXXXXXXX&blobtype=pdf`. Covers PNAS, Wiley, Nature papers that deposit to PMC after embargo.
- **Research Square preprints:** OpenAlex indexes these as alternate locations. Request `&select=...,locations` and iterate all `locations` where `is_oa: true` — catches preprints that the primary location doesn't expose.
- **Taylor & Francis green OA:** Many T&F journals allow immediate preprint sharing. Check OpenAlex/Unpaywall for author-deposited versions.

### Download Methods

**arXiv PDFs: ALWAYS use Bash curl**

```bash
# ✅ CORRECT
curl -o "PDFs/2016-Amodei-Concrete.pdf" https://arxiv.org/pdf/1606.06565.pdf

# ❌ WRONG - WebFetch causes API errors for binary PDFs
# Don't use WebFetch for PDF downloads
```

**Web content extraction: Use WebFetch**

```bash
# For extracting text from HTML pages
# (Model cards, blog posts, documentation)
```

**Rationale:** WebFetch is optimized for HTML→markdown, not binary file downloads.

### File Naming Convention

**Pattern:** `YYYY-FirstAuthor-ShortTitle.pdf`
**Example:** `2016-Amodei-Concrete Problems in AI Safety.pdf`

**Rules:**
- Match paper filename (without `.md` extension)
- Spaces allowed (easier readability)
- No special characters (`/`, `:`, `?`)

### Storage Location

**External directory** (configured in `.vault-config.json`):
```json
{
  "pdf_path": "/Users/username/Documents/PDFs"
}
```

**Accessed via:**
```python
from PYTHON.vault_config import PDFS_DIR
pdf_path = PDFS_DIR / f"{paper_key}.pdf"
```

### Download Script Pattern

```python
import requests
from pathlib import Path
from PYTHON.vault_config import PDFS_DIR

def download_pdf(arxiv_id: str, output_filename: str) -> bool:
    """Download PDF from arXiv."""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    output_path = PDFS_DIR / output_filename

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded: {output_filename}")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"Failed to download {arxiv_id}: {e}")
        return False
```

---

## PDF Extraction Workflow

### Extract Location

**Directory:** `PDF Extracts/`
**Format:** Markdown files with YAML frontmatter + full text

**Filename:** Match paper filename
- Paper: `papers/2016-Amodei-Concrete Problems in AI Safety.md`
- Extract: `PDF Extracts/2016-Amodei-Concrete Problems in AI Safety.md`

### Extract Structure

```yaml
---
source_pdf: "[[PDFs/2016-Amodei-Concrete Problems in AI Safety.pdf]]"
extracted_date: "2026-02-02"
pages: 27
extractor: "PyMuPDF"
---

[Full text content from PDF]

Page 1:
Concrete Problems in AI Safety
Dario Amodei, Chris Olah...

[Continue for all pages]
```

### Extraction Script Pattern

```python
import fitz  # PyMuPDF
from pathlib import Path
from datetime import datetime

def extract_pdf_text(pdf_path: Path, output_path: Path) -> None:
    """Extract text from PDF using PyMuPDF."""
    try:
        doc = fitz.open(pdf_path)
        text_content = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            text_content.append(f"Page {page_num + 1}:\n{text}\n")

        # Build frontmatter
        frontmatter = f"""---
source_pdf: "[[PDFs/{pdf_path.name}]]"
extracted_date: "{datetime.now().strftime('%Y-%m-%d')}"
pages: {len(doc)}
extractor: "PyMuPDF"
---

"""
        full_content = frontmatter + "\n".join(text_content)

        with open(output_path, 'w') as f:
            f.write(full_content)

        print(f"Extracted: {output_path.name} ({len(doc)} pages)")

    except Exception as e:
        print(f"Extraction failed: {e}")
```

### Quality Checks

**Empty extracts:**
```bash
find "PDF Extracts" -name "*.md" -size 0
```

**Missing extracts:**
```python
def find_missing_extracts() -> List[str]:
    """Find papers with PDFs but no extracts."""
    papers = Path("papers").glob("*.md")
    missing = []

    for paper in papers:
        fm = extract_frontmatter(paper.read_text())
        if 'local_pdf' in fm:
            extract_name = paper.stem + ".md"
            extract_path = Path("PDF Extracts") / extract_name
            if not extract_path.exists():
                missing.append(paper.name)

    return missing
```

---

## Link Update Workflow

### Bidirectional Linking

**Paper → PDF:**
```yaml
local_pdf: "[[PDFs/2016-Amodei-Concrete.pdf]]"
```

**Paper → Extract:**
```yaml
pdf_extract: "PDF Extracts/2016-Amodei-Concrete.md"
```

**Extract → PDF:**
```yaml
source_pdf: "[[PDFs/2016-Amodei-Concrete.pdf]]"
```

### Updating Links After Download

```python
def update_pdf_links(paper_path: Path, pdf_filename: str) -> None:
    """Update paper metadata with PDF link."""
    fm, body = extract_frontmatter(paper_path.read_text())

    # Add PDF link
    fm['local_pdf'] = f'"[[PDFs/{pdf_filename}]]"'  # MUST quote

    # Write back
    write_paper(paper_path, rebuild_frontmatter(fm), body, validate=True)
```

---

## PDF Recovery (After Deletion)

**See:** `docs/PDF_RECOVERY_GUIDE.md` for comprehensive recovery procedures.

**Quick recovery sources:**
1. **Zotero backup:** `~/Zotero/storage` (read-only)
2. **arXiv re-download:** If arXiv ID available
3. **Semantic Scholar:** Via DOI
4. **Publisher website:** Conference/journal

**Recovery script pattern:**
```python
def recover_pdf_from_zotero(paper_key: str) -> bool:
    """Attempt to recover PDF from Zotero storage."""
    zotero_storage = Path.home() / "Zotero" / "storage"

    # Search Zotero storage
    for item_dir in zotero_storage.glob("*"):
        pdf_files = list(item_dir.glob("*.pdf"))
        if pdf_files:
            # Check if matches paper (by title/author in filename)
            # Copy to PDFs/ directory
            # Update paper metadata
            pass

    return False
```

---

## Batch Processing Patterns

### Sequential PDF Downloads

```python
def download_missing_pdfs(paper_files: List[Path]) -> None:
    """Download PDFs for papers missing them."""
    for paper in paper_files:
        fm = extract_frontmatter(paper.read_text())

        if 'local_pdf' not in fm and 'url' in fm:
            # Extract arXiv ID from URL
            arxiv_id = extract_arxiv_id(fm['url'])
            if arxiv_id:
                pdf_name = f"{paper.stem}.pdf"
                download_pdf(arxiv_id, pdf_name)

                # Update paper metadata
                update_pdf_links(paper, pdf_name)

        time.sleep(2)  # Rate limiting
```

### Batch Extraction

```python
def extract_all_pdfs() -> None:
    """Extract all PDFs that don't have extracts yet."""
    for pdf_file in PDFS_DIR.glob("*.pdf"):
        extract_name = pdf_file.stem + ".md"
        extract_path = Path("PDF Extracts") / extract_name

        if not extract_path.exists():
            extract_pdf_text(pdf_file, extract_path)
```

---

## Download-Extract-Summarize Workflow

**Skill:** `/download-pdf` (automated 3-step workflow)

```
Step 1: Download PDF from arXiv/publisher
    ↓
Step 2: Extract full text to PDF Extracts/
    ↓
Step 3: Generate summary and update paper metadata
```

**Implemented in:** `.claude/skills/download-pdf/`

---

## Validation Commands

```bash
# Check for broken PDF links
python3 PYTHON/audit_pdf_links.py

# Find papers with PDFs but no extracts
find "PDF Extracts" -name "*.md" | wc -l  # Should match PDF count

# Check for empty extracts
find "PDF Extracts" -name "*.md" -size 0

# Verify PDF file integrity
find PDFs/ -name "*.pdf" -size 0  # Empty PDFs

# Check for orphaned PDFs (no matching paper)
python3 PYTHON/find_orphaned_pdfs.py
```

---

## Related Standards

- **API Integration:** `api-integration.md` (download sources)
- **YAML Safety:** `yaml-standards.md` (local_pdf field format)
- **File Safety:** `file-safety.md` (recovery procedures)

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2026-02-08 | Expanded strategy list (6→10), added Strategy Tips, EuropePMC/NeurIPS/MDPI patterns |
| 1.0 | 2026-02-02 | Initial PDF processing standards |
