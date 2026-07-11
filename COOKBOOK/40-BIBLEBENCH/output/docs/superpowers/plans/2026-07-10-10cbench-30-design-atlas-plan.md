# 10CBench 30-Design Research Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a source-grounded 39-slide Markdown atlas, editable PowerPoint, and visually verified PDF covering all thirty 10CBench designs.

**Architecture:** A canonical Markdown source contains the ordered narrative and thirty closed profile records. A plain JavaScript `@oai/artifact-tool` builder parses the Markdown and produces editable presentation objects, PNG/layout QA evidence, a montage, and PPTX. LibreOffice exports the PDF; Poppler and pypdf validate and render it.

**Tech Stack:** Markdown, JavaScript ES modules, `@oai/artifact-tool`, bundled Node.js, LibreOffice, Poppler, and Python/pypdf.

---

### Task 1: Lock the source contract with a failing validator

**Files:**
- Create: `output/test-10cbench-30-designs.mjs`
- Create: `output/10cbench-30-designs-overview.md`

- [ ] Write a validator that requires 39 slide sections, exact v1/v2/v3 ordered codename arrays, thirty `NN[A-C]` profile headings, existing source paths, and no placeholder tokens.
- [ ] Run `node output/test-10cbench-30-designs.mjs` before creating the Markdown and confirm failure because the source is absent.
- [ ] Author the Markdown by preserving the validated v1/v2 content, adding v3 profiles grounded in the v3 briefs, and adding the three-generation dividers and synthesis.
- [ ] Re-run the validator and require `PASS: 39 slides; 30 profiles; v1=10; v2=10; v3=10`.

### Task 2: Build the editable deck test-first

**Files:**
- Create: `output/test-build-10cbench-30-designs.mjs`
- Create: `output/build-10cbench-30-designs-deck.mjs`
- Create: `output/10cbench-30-designs-overview.pptx`

- [ ] Write an end-to-end build test that invokes the not-yet-existing builder in a temporary directory and requires 39 PNGs, 39 layout JSONs, a montage, a 39-slide PPTX, and all thirty codenames in the inspection text.
- [ ] Run the build test and confirm failure because the builder is absent.
- [ ] Implement the minimal plain-JavaScript artifact-tool builder: cover, architecture slide, two maps, three section dividers, one profile layout, synthesis, and close.
- [ ] Export the repository PPTX and rerun the build test until it passes.
- [ ] Run `slides_test.py` and fix every unintended out-of-bounds warning.

### Task 3: Export and verify the PDF

**Files:**
- Create: `output/pdf/10cbench-30-designs-overview.pdf`

- [ ] Convert the verified PPTX to PDF with bundled LibreOffice.
- [ ] Use `pdfinfo` and pypdf to require 39 landscape 16:9 pages, nonempty searchable text on every page, and all thirty profile headings.
- [ ] Reject placeholder tokens and unresolved production copy in extracted PDF text.
- [ ] Render all 39 pages with Poppler at 144 dpi into external scratch.
- [ ] Build a montage for pacing review and inspect every page individually at full size; fix the Markdown or builder before shrinking type.

### Task 4: Final cross-format verification

- [ ] Re-run the Markdown validator, end-to-end build test, PPTX overflow test, PDF structural checks, and placeholder scans.
- [ ] Confirm the historical 20-design outputs are byte-present and the thirty source briefs remain unmodified.
- [ ] Record exact final paths, byte sizes, slide/page counts, and visual-QA completion in the delivery response.
- [ ] Do not stage or commit.

## Self-review

- Specification coverage: every deliverable, profile field, generation boundary, and QA requirement maps to a task.
- Placeholder scan: no unresolved implementation placeholder remains.
- Scope: only new `output/10cbench-30-designs-*` artifacts and their spec/plan are created; source portfolios remain read-only.
- Type consistency: the same ordered codename arrays drive Markdown validation, builder validation, and PDF verification.

