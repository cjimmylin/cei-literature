# Manual Browser Playbook

Generated: 2026-02-14T07:45:54

## Queue Snapshot
- Source CSV: `logs/20260214-browser-fetch-manual-plan-after-wave3-plus-europepmc-plus-wave4-remapped.csv`
- Total rows: **124**
- P2 rows: **21**
- P3 rows: **103**
- Recommended actions: **{'MANUAL_CHECK': 31, 'OPEN_LANDING_PAGE': 35, 'BROWSER_FETCH': 42, 'TRY_DOWNLOAD': 16}**

## Host Playbook
### `dl.acm.org` (19)
- Institution login likely required. Open DOI page; use PDF button or author-provided free copy.

### `link.springer.com` (18)
- Open article/chapter page first, then Download PDF in browser session.

### `www.mdpi.com` (10)
- Use article page PDF control (JS/cookie required).

### `www.semanticscholar.org` (7)
- Metadata-only page; pivot to DOI/arXiv/publisher links.

### `arxiv.org` (7)
- Use direct /pdf/<id>.pdf link and verify title.

### `doaj.org` (5)
- Open DOAJ record and follow Full Text to publisher PDF.

### `journals.sagepub.com` (5)
- Often auth-gated; use institution login for PDF.

### `www.tandfonline.com` (5)
- Often auth-gated; use institution login for PDF or accepted manuscript.

### `xplorestaging.ieee.org` (4)
- Prefer real IEEE Xplore page; staging links often return HTML.

### `papers.ssrn.com` (4)
- Open abstract page and download PDF (may require sign-in).

### `ieeexplore.ieee.org` (4)
- Use IEEE landing page with institution login, then PDF.

### `onlinelibrary.wiley.com` (3)
- Use DOI landing page with browser cookies and PDF/PDFDirect.

### `namespace.openaire.eu` (2)
- Namespace endpoint is not paper PDF; locate linked repository/publisher record.

### `www.sciencedirect.com` (2)
- Open article page in institutional session and click View PDF.

### `huggingface.co` (2)
- Resource/model page; extract linked paper DOI/arXiv/PDF.

### `www.techrxiv.org` (2)
- Open DOI page in browser and use PDF control.

### `linkinghub.elsevier.com` (2)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `ebooks.iospress.nl` (2)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `drive.usercontent.google.com` (2)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `scholarlypublishingcollective.org` (2)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `ceur-ws.org` (2)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `zenodo.org` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.yorku.ca` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.hindawi.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `downloads.hindawi.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `academic.oup.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.tara.tcd.ie` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `pmc.ncbi.nlm.nih.gov` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.authorea.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `static1.squarespace.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `assets.mofoprod.net` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.ibm.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.goodreads.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.degruyterbrill.com` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.acls.org` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

### `www.thegreenreport.blog` (1)
- Open in browser, locate PDF/download link, verify title, then update metadata fields.

## Produced Checklists
- `logs/20260214-manual-browser-p2-actionable.csv`
- `logs/20260214-manual-browser-p2-actionable.md`
- `logs/20260214-manual-browser-p2-blockers.csv`
- `logs/20260214-manual-browser-p2-execution-plan.md`
