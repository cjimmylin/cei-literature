# BibleBench Paper, Cost, and Methods PDF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prepare a source-cited zero-call cheap-model checkpoint and a visually verified methods PDF with pending results.

**Architecture:** Public official pricing/model documentation supplies a dated roster proposal and auditable cost formula. A deterministic local renderer creates a stable PDF from the manuscript plus paper status metadata, followed by text and page-image QA.

**Tech Stack:** Official web documentation, Markdown, Python, reportlab, pypdf/pdfplumber, Poppler.

---

### Task 1: Roster and cost checkpoint

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/PILOT-COST-CHECKPOINT.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/pilot-cost-estimate.json`

- [ ] Use current official primary sources to identify inexpensive general-purpose models eligible for the diagnostic pilot; exclude specialized safety/judge-only models.
- [ ] Record date, provider/model ID, input/output unit price, context boundary, source URL, and uncertainty.
- [ ] Calculate exact planned call counts and conservative cost from registered schedule geometry and explicit token caps.
- [ ] Define hard NTE ceiling, preflight stop, per-model checkpoint, missing-price stop, and `AUTHORIZED: false`, `calls_made: 0`, `spend_usd: 0`.

### Task 2: Methods PDF renderer

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/tools/build_methods_pdf.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_methods_pdf.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/output/pdf/biblebench-methods-prerelease.pdf`

- [ ] Write a failing test requiring a valid PDF, stable title/author/status metadata, page numbers, readable manuscript text, references, and exactly one `PENDING_EMPIRICAL_RUN` marker.
- [ ] Implement a deterministic reportlab renderer with consistent typography, headings, tables, margins, headers/footers, and wrapped URLs/references.
- [ ] Render to the stable output path and validate with pypdf/pdfplumber.

### Task 3: Visual QA and manuscript surfaces

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/output/pdf/QA.md`
- Modify only if needed: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/manuscript.md`
- Modify only if needed: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/references.bib`

- [ ] Render every PDF page to PNG under `tmp/pdfs/` and visually inspect representative and dense pages for clipping, overlap, broken glyphs, references, and page transitions.
- [ ] Record PDF SHA-256, page count, extraction checks, render command, inspected pages, and zero-defect disposition in `QA.md`.
- [ ] Preserve pending-result and no-empirical-claim boundaries.
- [ ] Run PDF tests and paper-artifact tests.
