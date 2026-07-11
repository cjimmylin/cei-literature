# FruitBench 20-Design Overview Deck Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce an evidence-grounded Markdown overview, editable PowerPoint deck, widescreen presentation PDF, and printer-friendly PDF handout covering all 20 FruitBench designs.

**Architecture:** Treat the Markdown deck as the editorial source of truth. Extract a structured 20-design content matrix from the briefs and readiness records, validate required fields before rendering, then generate a 1280x720 PowerPoint with `@oai/artifact-tool`. Export and visually verify both a slide PDF and a separately typeset portrait handout PDF.

**Tech Stack:** Markdown, plain JavaScript ES modules, `@oai/artifact-tool`, bundled Node.js, bundled Python 3 with ReportLab/PyPDF/pdfplumber, LibreOffice (`soffice`), Poppler (`pdfinfo`, `pdftoppm`), presentation container QA tools.

---

## File map

**Final deliverables**

- Create: `FRUITBENCH-REVIEWS/DECKS/fruitbench-20-designs-overview.md` - editorial source with `---` slide boundaries and source notes.
- Create: `FRUITBENCH-REVIEWS/DECKS/fruitbench-20-designs-overview.pptx` - editable presentation.
- Create: `FRUITBENCH-REVIEWS/DECKS/fruitbench-20-designs-overview-slides.pdf` - widescreen presentation PDF.
- Create: `FRUITBENCH-REVIEWS/DECKS/fruitbench-20-designs-overview-handout.pdf` - portrait handout PDF.

**External scratch files**

- Create: `$TMP_DIR/source-notes.txt` - source inventory and extracted facts.
- Create: `$TMP_DIR/design-data.json` - normalized 20-design data used by renderers.
- Create: `$TMP_DIR/validate-content.mjs` - fail-closed source/content validator.
- Create: `$TMP_DIR/build-presentation.mjs` - artifact-tool presentation renderer.
- Create: `$TMP_DIR/build-handout.py` - ReportLab handout renderer.
- Create: `$TMP_DIR/preview/` - rendered slide images.
- Create: `$TMP_DIR/layout/` - slide layout JSON.
- Create: `$TMP_DIR/qa/` - montage, PDF renders, and QA ledger.

No unrelated repository file is modified. Because the shared worktree is dirty with unrelated projects, execution must not stage or commit files unless the user separately requests Git integration.

### Task 1: Establish workspace and inventory the authoritative sources

- [ ] **Step 1: Define deterministic runtime and scratch paths**

Run:

```bash
export PROJECT_ROOT="/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH"
export OUTPUT_DIR="$PROJECT_ROOT/FRUITBENCH-REVIEWS/DECKS"
export SKILL_DIR="/Users/jimmy.lin/.codex/plugins/cache/openai-primary-runtime/presentations/26.709.12203/skills/presentations"
export RUNTIME_ROOT="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies"
export PATH="$RUNTIME_ROOT/node/bin:$RUNTIME_ROOT/bin:$RUNTIME_ROOT/native/poppler/poppler/bin:$PATH"
export NODE_PATH="$RUNTIME_ROOT/node/node_modules"
export THREAD_ID="${CODEX_THREAD_ID:-manual-fruitbench-20-deck}"
export WORKSPACE="$(node -p "require('node:os').tmpdir())/codex-presentations/$THREAD_ID/fruitbench-20-designs"
export TMP_DIR="$WORKSPACE/tmp"
mkdir -p "$OUTPUT_DIR" "$TMP_DIR/preview" "$TMP_DIR/layout" "$TMP_DIR/assets" "$TMP_DIR/qa"
```

Expected: all directories exist; no benchmark source file changes.

- [ ] **Step 2: Record the exact 20-brief source inventory**

Run from `$PROJECT_ROOT`:

```bash
find FRUITBENCH/DESIGNS -maxdepth 1 -type f -name '[0-9][0-9]-*.md' ! -name '00-*' -print | sort
find FRUITBENCH-v2/DESIGNS -maxdepth 1 -type f -name '[0-9][0-9]-*.md' -print | sort
```

Expected: ten v1 briefs and ten v2 briefs.

- [ ] **Step 3: Extract source-grounded facts into `source-notes.txt`**

For every design, record: portfolio, number, codename, construct/methodology, scientific question, mechanics, representative case provenance, headline metric, primary advantage, primary limitation, complementary design, source path, and readiness evidence path. Include the two portfolio documents and the latest dated worklist/handoffs.

The source note header must be:

```text
FruitBench 20-design deck source notes
Evidence cutoff: 2026-07-10
Rule: briefs govern design; latest binding dated worklist/handoff governs readiness.
Case provenance values: bank-derived | illustrative
Readiness values: DESIGNED | P1 BUILT | HARDENING | LIVE-VALIDATED
```

- [ ] **Step 4: Verify source completeness**

Run:

```bash
test "$(find FRUITBENCH/DESIGNS -maxdepth 1 -type f -name '[0-9][0-9]-*.md' ! -name '00-*' | wc -l | tr -d ' ')" = "10"
test "$(find FRUITBENCH-v2/DESIGNS -maxdepth 1 -type f -name '[0-9][0-9]-*.md' | wc -l | tr -d ' ')" = "10"
```

Expected: exit code 0.

### Task 2: Create the structured content contract and validator first

- [ ] **Step 1: Write `validate-content.mjs` before the content file**

The validator must parse `$TMP_DIR/design-data.json` and require exactly these keys per design:

```js
const REQUIRED = [
  "portfolio", "number", "codename", "question", "construct",
  "mechanics", "case_example", "case_provenance", "headline_metric",
  "advantage", "limitation", "complement", "readiness", "as_of", "sources"
];
```

It must reject duplicate `(portfolio, number)` pairs, duplicate codenames, portfolios other than `v1` or `v2`, readiness outside the four approved values, case provenance outside `bank-derived` or `illustrative`, source paths that do not exist, empty strings, and counts other than ten designs per portfolio. It must also require the exact codenames listed in the two portfolio tables.

- [ ] **Step 2: Run the validator RED**

Run:

```bash
node "$TMP_DIR/validate-content.mjs" "$TMP_DIR/design-data.json"
```

Expected: non-zero exit with `design-data.json does not exist`.

- [ ] **Step 3: Create `design-data.json` from the source notes**

Use this top-level schema:

```json
{
  "schema_version": "1.0",
  "evidence_cutoff": "2026-07-10",
  "designs": []
}
```

Populate all 20 entries from the briefs. Keep visible design text concise enough for a 16 pt minimum body font: question at most 95 characters; mechanics at most 240; case example at most 220; advantage and limitation at most 150 each.

- [ ] **Step 4: Run the validator GREEN**

Run:

```bash
node "$TMP_DIR/validate-content.mjs" "$TMP_DIR/design-data.json"
```

Expected: `PASS: 20 designs (10 v1, 10 v2); all required fields and sources valid`.

### Task 3: Author and audit the Markdown deck first

- [ ] **Step 1: Create the Markdown deck with 31 slide sections**

Use YAML front matter followed by `---` slide boundaries:

```markdown
---
title: "FruitBench: Twenty Instruments for Positive-Character Evaluation"
subtitle: "Ten fruit-major designs + ten whole-passage methodologies"
date: "2026-07-10"
aspectRatio: "16:9"
---
```

Each design slide must use these headings exactly once:

```markdown
## [Takeaway-style scientific question]

**Design**

**Representative case — [bank-derived|illustrative]**

**Headline metric**

**Advantage**

**Limitation**

**Complements**

**Readiness — [status], as of 2026-07-10**
```

- [ ] **Step 2: Add the approved framing and synthesis slides**

Include title, positive-character motivation, lattice explanation, readiness legend, v1 opener, v1 synthesis, v2 opener, v1-to-v2 crosswalk, portfolio-wide advantages/risks, roadmap, and closing synthesis/source notes. Every slide gets one narrative job and one takeaway-style title.

- [ ] **Step 3: Run a Markdown structural audit**

Run a script that asserts:

```text
exactly 20 full design slides
exactly 10 v1 codenames and 10 v2 codenames
all nine design-slide content fields present
all case examples labeled bank-derived or illustrative
all readiness labels use the approved vocabulary and date
no TBD, TODO, FIXME, unsupported live-valid claim, or internal planning note
```

Expected: `PASS: Markdown deck contains all 20 designs and required fields`.

- [ ] **Step 4: Manually reconcile every design slide against its cited brief**

Record one line per design in `$TMP_DIR/qa/content-audit.txt`:

```text
v1-01 COSTLY | brief checked | example provenance checked | metric checked | readiness checked | PASS
```

Expected: 20 `PASS` rows and no unresolved conflict.

### Task 4: Build the editable PowerPoint from the approved Markdown content

- [ ] **Step 1: Initialize the artifact-tool workspace**

Run:

```bash
node "$SKILL_DIR/container_tools/setup_artifact_tool_workspace.mjs" --workspace "$TMP_DIR"
```

Expected: `$TMP_DIR/node_modules/@oai/artifact-tool` resolves.

- [ ] **Step 2: Implement `build-presentation.mjs` with reusable layout functions**

Use plain JavaScript ES modules and these boundaries:

```js
import fs from "node:fs/promises";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const SIZE = { width: 1280, height: 720 };
const COLORS = {
  navy: "#101B2D", ivory: "#F7F3E9", ink: "#17313A",
  v1: "#B8543B", v2: "#277C70", amber: "#B77A20",
  gray: "#6B7280", pale: "#E8EEE9", white: "#FFFFFF"
};

function addTitleSlide(presentation, content) {}
function addThesisSlide(presentation, content) {}
function addLatticeSlide(presentation, content) {}
function addLegendSlide(presentation, content) {}
function addSectionSlide(presentation, content, portfolio) {}
function addDesignSlide(presentation, design) {}
function addSynthesisSlide(presentation, content, portfolio) {}
function addCrosswalkSlide(presentation, content) {}
function addRoadmapSlide(presentation, content) {}
function addClosingSlide(presentation, content) {}
function addFooter(slide, slideNumber, sourceLabel) {}
```

Use 1280x720 slides, equal outer margins, at least 50 pt title-slide text, 35 pt slide titles, 24 pt subheads, and 16 pt body text. v1 uses terracotta accents; v2 uses teal. Status must appear as text, not color alone.

- [ ] **Step 3: Render one v1 and one v2 design slide as a smoke test**

Generate temporary slides for COSTLY and THORNS, export their PNG and layout JSON, and inspect them full-size before generating the remaining deck.

Expected: no clipped text; one-line titles remain one line; all nine content fields are readable.

- [ ] **Step 4: Generate the complete PPTX and per-slide QA artifacts**

The builder must:

```js
const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(process.env.FINAL_PPTX);
```

It must also export one PNG and one layout JSON per slide plus a montage to `$TMP_DIR/qa/`.

Expected: 31-33 slides and a non-empty final PPTX.

### Task 5: Verify PowerPoint layout and narrative quality

- [ ] **Step 1: Run automated overflow checks**

Run:

```bash
python3 "$SKILL_DIR/container_tools/slides_test.py" "$OUTPUT_DIR/fruitbench-20-designs-overview.pptx"
```

Expected: no overflow or out-of-canvas errors.

- [ ] **Step 2: Render the PPTX independently**

Run:

```bash
python3 "$SKILL_DIR/container_tools/render_slides.py" "$OUTPUT_DIR/fruitbench-20-designs-overview.pptx"
```

Expected: one PNG per slide.

- [ ] **Step 3: Create and inspect the montage**

Run:

```bash
python3 "$SKILL_DIR/container_tools/create_montage.py" \
  --input_dir "$OUTPUT_DIR/fruitbench-20-designs-overview" \
  --output_file "$TMP_DIR/qa/final-deck-montage.png"
```

Inspect the montage for narrative rhythm, then inspect every rendered slide individually at full size. Record each slide as `PASS` or list the specific correction in `$TMP_DIR/qa/visual-audit.txt`.

- [ ] **Step 4: Correct and rerun until all slides pass**

Fix every unintended overlap, clipping, title wrap, broken glyph, inconsistent footer, unreadable source, or low-contrast status. Rebuild and repeat Tasks 5.1-5.3 after each meaningful revision.

Expected: every slide line in `visual-audit.txt` ends in `PASS`.

### Task 6: Export and verify the widescreen slide PDF

- [ ] **Step 1: Convert the final PPTX to PDF with the bundled LibreOffice**

Run:

```bash
mkdir -p "$TMP_DIR/pdf-export"
soffice --headless --convert-to pdf --outdir "$TMP_DIR/pdf-export" \
  "$OUTPUT_DIR/fruitbench-20-designs-overview.pptx"
mv "$TMP_DIR/pdf-export/fruitbench-20-designs-overview.pdf" \
  "$OUTPUT_DIR/fruitbench-20-designs-overview-slides.pdf"
```

Expected: PDF page count equals PPTX slide count.

- [ ] **Step 2: Validate PDF metadata and text**

Run:

```bash
pdfinfo "$OUTPUT_DIR/fruitbench-20-designs-overview-slides.pdf"
pdftotext "$OUTPUT_DIR/fruitbench-20-designs-overview-slides.pdf" - | grep -cE 'COSTLY|THORNS|VINEDRESSER'
```

Expected: valid PDF; all three sentinel codenames are found.

- [ ] **Step 3: Render every slide-PDF page and inspect**

Run:

```bash
mkdir -p "$TMP_DIR/qa/slides-pdf"
pdftoppm -png "$OUTPUT_DIR/fruitbench-20-designs-overview-slides.pdf" \
  "$TMP_DIR/qa/slides-pdf/page"
```

Expected: page images visually match the approved PowerPoint rendering with no substituted glyphs or clipping.

### Task 7: Build and verify the portrait handout PDF

- [ ] **Step 1: Implement `build-handout.py` from the same `design-data.json`**

Use ReportLab with letter-size portrait pages, 0.55 inch margins, a title and portfolio framing section, then one design per page. Each design page repeats the same substantive fields as the slide but allows longer source footnotes. Use `PageBreak` between designs and a footer with page number and evidence cutoff.

The script must fail if `design-data.json` does not contain exactly 20 designs or if any required field is blank.

- [ ] **Step 2: Generate the handout**

Run:

```bash
"$RUNTIME_ROOT/python/bin/python3" "$TMP_DIR/build-handout.py" \
  --data "$TMP_DIR/design-data.json" \
  --out "$OUTPUT_DIR/fruitbench-20-designs-overview-handout.pdf"
```

Expected: a valid portrait PDF containing all 20 designs.

- [ ] **Step 3: Validate and render the handout**

Run:

```bash
pdfinfo "$OUTPUT_DIR/fruitbench-20-designs-overview-handout.pdf"
mkdir -p "$TMP_DIR/qa/handout-pdf"
pdftoppm -png "$OUTPUT_DIR/fruitbench-20-designs-overview-handout.pdf" \
  "$TMP_DIR/qa/handout-pdf/page"
```

Inspect every page at full size. Correct any orphan heading, split label/value pair, clipped footer, broken glyph, or unreadable source note.

### Task 8: Cross-format verification and delivery

- [ ] **Step 1: Verify all four deliverables exist and are non-empty**

Run:

```bash
test -s "$OUTPUT_DIR/fruitbench-20-designs-overview.md"
test -s "$OUTPUT_DIR/fruitbench-20-designs-overview.pptx"
test -s "$OUTPUT_DIR/fruitbench-20-designs-overview-slides.pdf"
test -s "$OUTPUT_DIR/fruitbench-20-designs-overview-handout.pdf"
```

Expected: exit code 0.

- [ ] **Step 2: Compare substantive content across formats**

Extract text from both PDFs and inspect the PPTX snapshot. Assert that all 20 codenames, all 20 readiness labels, the evidence cutoff, and the case-provenance labels are present in each applicable format.

- [ ] **Step 3: Run final placeholder and unsupported-claim scan**

Run:

```bash
grep -RniE 'TBD|TODO|FIXME|lorem ipsum|fully validated|formal evidence established' \
  "$OUTPUT_DIR/fruitbench-20-designs-overview.md" "$TMP_DIR" || true
```

Expected: no unresolved placeholder or unsupported validity claim.

- [ ] **Step 4: Record final QA evidence**

Write `$TMP_DIR/qa/final-verification.txt` with exact commands, exit codes, slide/page counts, and the statement:

```text
All 20 designs are present. Markdown, PPTX, slide PDF, and handout PDF agree on substantive claims. Every final slide and PDF page was rendered and visually inspected. No unresolved overflow, overlap, clipping, broken glyph, placeholder, or unsupported live-validity claim remains.
```

- [ ] **Step 5: Deliver the four final files with absolute clickable links**

Do not include scratch files, internal plans, render previews, or QA ledgers unless requested.
