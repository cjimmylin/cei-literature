# BibleBench Nine-PDF Lane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate and visually verify the exact nine pre-empirical BibleBench PDF deliverables, including all 30 registered Ten Commandments designs.

**Architecture:** A declarative report registry maps each stable filename to local Markdown/YAML sources and required content checks. One ReportLab builder supplies shared typography, metadata, page templates, tables, and empirical-sentinel handling. Machine QA uses pypdf/pdfplumber; visual QA renders every page with Poppler and records inspection results.

**Tech Stack:** Python 3.11+, ReportLab, pypdf, pdfplumber, Poppler, pytest, Markdown/YAML inputs.

---

### Task 1: Register the exact report inventory and source contracts

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/reports/report-registry.yaml`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_design_reports.py`

- [ ] **Step 1: Write failing inventory tests**

Require exactly these filenames:

```python
EXPECTED = {
    "01-biblebench-consolidated-design-and-methods.pdf",
    "02-fruitbench-design-report.pdf",
    "03-corinthlove-design-report.pdf",
    "04-10cbench-30-design-atlas.pdf",
    "05-sermonmount-design-report.pdf",
    "06-shared-episode-protocol-and-custody.pdf",
    "07-human-adjudication-handbook.pdf",
    "08-reproducibility-ethics-and-data-card.pdf",
    "09-analysis-tables-figures-and-claims-boundary.pdf",
}
```

Require each registry entry to identify title, local source paths, required phrases/identifiers, and `PRE-EMPIRICAL DESIGN REPORT` status.

- [ ] **Step 2: Run and verify failure**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_design_reports.py -q`

Expected: FAIL because the registry and builder do not exist.

- [ ] **Step 3: Implement the registry**

Use the manuscript and frozen pilot bank for consolidated content; module banks and current handoffs for module reports; `output/10cbench-30-designs-overview.md` for the 30-design atlas; custody and adjudication guides for reports 6-7; appendices for report 8; and analysis shells/claims registry for report 9. Do not edit frozen or historical sources.

- [ ] **Step 4: Validate every source path and required ID**

The test must fail if a source is missing, empty, or lacks its registered identifier. For report 4, require 30 unique design IDs from the source before building.

### Task 2: Build the shared report renderer

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/tools/build_design_reports.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_design_reports.py`

- [ ] **Step 1: Add builder tests**

Test deterministic ordering, stable output names, searchable text, page numbers, and PDF metadata fields: title, author `Jimmy Lin`, subject containing `Pre-empirical`, and creator `BibleBench design-report builder`.

- [ ] **Step 2: Implement shared styles and parsing**

Reuse the existing methods-PDF typography where practical. Support headings, paragraphs, bullets, tables, callouts, explicit page breaks, and source-note blocks. Escape markup, preserve long identifiers, and use ASCII hyphens.

- [ ] **Step 3: Add pre-empirical guards**

Every cover and footer must say `PRE-EMPIRICAL DESIGN REPORT`. Reject numerical model outcomes, ranking/best-model language, unresolved citation tokens, placeholders other than `PENDING_EMPIRICAL_RUN`, and empty sections.

- [ ] **Step 4: Run focused tests**

Run the Task 1 command. Expected: all builder contract tests PASS.

### Task 3: Add report-specific content and analysis templates

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/reports/06-shared-protocol.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/reports/07-adjudication-handbook.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/reports/09-analysis-template.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/figure-contracts.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/final-table-shells.csv`

- [ ] **Step 1: Write protocol and handbook sources**

Cover shared episodes, C0/C1/C2 design history versus PF-002 C1 execution, matched probes, artifacts/actions, capability controls, evidence custody, owner judgment, repeat sequencing, contamination limits, and stop rules. Never include the private repeat mapping or suggested decisions.

- [ ] **Step 2: Write analysis contracts**

Provide empty schemas/shells for completion and missingness, module-native vectors, common-life/Christian-facing strata, action/probe consistency, red-line incidents, owner confidence/contestability, and descriptive model-by-module patterns. Each body is `PENDING_EMPIRICAL_RUN`.

- [ ] **Step 3: Add exclusions**

Explicitly exclude p-values, composites, leaderboards, best-model fields, cue effects, capability-adjusted attribution, and family-level estimates.

- [ ] **Step 4: Run report tests**

Run the Task 1 command. Expected: PASS.

### Task 4: Generate, machine-check, and visually inspect all PDFs

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/output/design-reports/*.pdf`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/output/design-reports/QA.md`
- Create: `COOKBOOK/40-BIBLEBENCH/tmp/pdfs/biblebench-design-reports/` (temporary renders only)

- [ ] **Step 1: Generate the inventory twice**

Run the builder twice and compare file SHA-256 values. Expected: nine identically named PDFs and deterministic hashes.

- [ ] **Step 2: Run machine QA**

Use pypdf/pdfplumber to assert nonempty pages, metadata, searchable text, page labels, no unresolved tokens, and all 30 Ten Commandments IDs in report 4.

- [ ] **Step 3: Render every page with Poppler**

Run `pdftoppm -png -r 130 <pdf> COOKBOOK/40-BIBLEBENCH/tmp/pdfs/biblebench-design-reports/<stem>/page` for every report. Create contact sheets and inspect all pages plus dense representative pages at original resolution.

- [ ] **Step 4: Record visual QA**

In `QA.md`, record each filename, page count, machine checks, rendered-page count, inspected dense pages, and PASS/FAIL for clipping, overlap, broken glyphs, tables, headers/footers, and section transitions. Repair and rerender every failure.

- [ ] **Step 5: Run focused and integrated PDF tests**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_design_reports.py tests/test_methods_pdf.py -q`

Expected: PASS.

- [ ] **Step 6: Commit the lane**

Run `git log -1 --oneline`, path-stage only report sources, builder, final PDFs, QA record, analysis templates, and tests; do not stage temporary PNGs. Commit with `BibleBench: generate nine pre-empirical design reports`.
