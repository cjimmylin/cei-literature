# SermonMount 20-Design Research Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a source-grounded Markdown research atlas, editable PowerPoint, widescreen slide PDF, and print-friendly handout PDF covering all twenty SermonMount benchmark designs.

**Architecture:** A single external-scratch content model drives all outputs. Repository design documents are read-only inputs; a generated Markdown deck is the human-reviewable content authority, while presentation and handout renderers consume the same frozen content model and must pass coverage, citation, layout, and PDF-render checks. Only final deliverables and approved design/plan documentation live under `SERMONMOUNT-v2/DECKS/`.

**Tech Stack:** Markdown, plain JavaScript ES modules, `@oai/artifact-tool`, bundled Node.js, bundled Python 3 with ReportLab/pypdf, LibreOffice headless conversion, Poppler rendering, and the Codex Grid layout reference.

---

## File map

### Read-only sources

- `SERMONMOUNT/DESIGNS/00-sermonmountbench-portfolio.md`
- `SERMONMOUNT/DESIGNS/01-blessed.md` through `SERMONMOUNT/DESIGNS/10-rocksand.md`
- `SERMONMOUNT-v2/DESIGNS/01-pilgrim.md` through `SERMONMOUNT-v2/DESIGNS/10-gleaning.md`
- `SERMONMOUNT-v2/DESIGNS/09-witness/README.md`
- `SERMONMOUNT-v2/20260706-PARKED-opus-reentry-prompt.md`

### Final deliverables

- Create: `SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.md`
- Create: `SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx`
- Create: `SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf`
- Create: `SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-handout.pdf`

### External scratch files

Use `$TMPDIR/codex-presentations/${CODEX_THREAD_ID:-manual-20260710}/sermonmount-20-design-atlas/tmp/` for:

- `source-notes.txt` — evidence excerpts and line-number provenance.
- `deck-content.json` — frozen structured content model.
- `render-markdown.mjs` — Markdown renderer.
- `validate-content.mjs` — coverage, schema, and citation checks.
- `build-deck.mjs` — artifact-tool presentation generator.
- `build-handout.py` — print handout generator.
- `slides/`, `preview/`, `layout/`, `qa/`, and `pdfs/` — render evidence only.

No scratch file is staged or copied into the repository.

---

### Task 1: Freeze the source inventory and evidence schema

**Files:**

- Create in scratch: `source-notes.txt`
- Create in scratch: `deck-content.json`
- Create in scratch: `validate-content.mjs`

- [ ] **Step 1: Initialize external scratch and artifact-tool resolution**

Run:

```bash
ROOT="$PWD"
NODE="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node"
SKILL_DIR="/Users/jimmy.lin/.codex/plugins/cache/openai-primary-runtime/presentations/26.709.12203/skills/presentations"
THREAD_ID="${CODEX_THREAD_ID:-manual-20260710}"
WORKSPACE="${TMPDIR:-/tmp}/codex-presentations/$THREAD_ID/sermonmount-20-design-atlas"
TMP="$WORKSPACE/tmp"
mkdir -p "$TMP"/{slides,preview,layout,assets,qa,pdfs}
"$NODE" "$SKILL_DIR/container_tools/setup_artifact_tool_workspace.mjs" --workspace "$TMP"
```

Expected: `$TMP/node_modules/@oai/artifact-tool` resolves and no repository source is modified.

- [ ] **Step 2: Record the exact twenty-design inventory**

The content model must contain these ordered identifiers exactly once:

```text
v1-01 BLESSED
v1-02 UNSEEN
v1-03 PLAINYES
v1-04 SECONDMILE
v1-05 TWOMASTERS
v1-06 LOGSPECK
v1-07 GOLDGAP
v1-08 SHEEPSKIN
v1-09 TELOS
v1-10 ROCKSAND
v2-01 PILGRIM
v2-02 CROSSWINDS
v2-03 PLUMBLINE
v2-04 CANTICLE
v2-05 TESSERA
v2-06 LEDGER
v2-07 VILLAGE
v2-08 SCRIBE
v2-09 WITNESS
v2-10 GLEANING
```

- [ ] **Step 3: Define the closed content fields**

Each design record contains these nonempty strings or string arrays:

```json
{
  "id": "v1-01",
  "portfolio": "v1",
  "number": 1,
  "name": "BLESSED",
  "claim": "...",
  "passage_anchor": "...",
  "theological_rationale": "...",
  "construct": "...",
  "model_role": "...",
  "methodology": "...",
  "headline_evidence": "...",
  "differentiation": "...",
  "illustrative_case": "...",
  "manipulated": ["..."],
  "observed": ["..."],
  "scored": ["..."],
  "strengths": ["...", "..."],
  "limitations": ["...", "..."],
  "burden": {"items": "...", "judges": "...", "infrastructure": "...", "dependency": "..."},
  "source_paths": ["SERMONMOUNT/DESIGNS/01-blessed.md"]
}
```

- [ ] **Step 4: Write validation before content population**

`validate-content.mjs` must fail unless:

- the top-level schema version is `sermonmount-atlas-content-v1`;
- the design array has length 20 with the exact ordered IDs above;
- every closed field is present and nonempty;
- `strengths` and `limitations` each contain 2–3 items;
- every `source_paths` entry is repository-relative and resolves to a regular file under the project root;
- no string contains `TODO`, `TBD`, `lorem ipsum`, production instructions, or unsupported control characters;
- every illustrative case begins with `Illustrative case:`;
- all burden fields use only `low`, `medium`, `high`, or a short dependency phrase tied to the source document.

Run against the empty model and confirm failure:

```bash
"$NODE" "$TMP/validate-content.mjs" "$ROOT" "$TMP/deck-content.json"
```

Expected: nonzero exit identifying missing design records.

---

### Task 2: Populate and verify the ten v1 profiles

**Files:**

- Modify in scratch: `source-notes.txt`
- Modify in scratch: `deck-content.json`

- [ ] **Step 1: Extract the v1 evidence bands**

For each v1 card, read and record:

- header metadata and `Status`;
- `## 1. Exegetical anchor`;
- `## 2. Construct definition`;
- `## 3. Core innovation`;
- `## 4. Instrument sketch`;
- concrete scenario mechanics in `## 5. Item-bank construction instructions`;
- `## 6. Metrics` and ground-truth/judge sections;
- `## 8. Nearest published neighbors`;
- `## 9. P1 pilot spec`.

`source-notes.txt` records the source path and line interval for each extracted claim.

- [ ] **Step 2: Populate v1 records in exact portfolio order**

Write concise, audience-facing content for BLESSED through ROCKSAND. Preserve named two-sided failure poles, falsification conditions, and P1 burden where they materially determine strengths or limitations.

- [ ] **Step 3: Ground every illustrative v1 case**

Each case must instantiate the card’s stated manipulation without importing another design’s construct. For example, a TELOS case must manipulate letter-versus-purpose compliance, not generic jailbreak resistance; a SHEEPSKIN case must orthogonally manipulate behavioral record and presentation cues.

- [ ] **Step 4: Run partial validation**

Add a `--portfolio v1` mode to the validator and run:

```bash
"$NODE" "$TMP/validate-content.mjs" "$ROOT" "$TMP/deck-content.json" --portfolio v1
```

Expected: 10 v1 records pass; missing v2 records are ignored only in this explicit partial mode.

---

### Task 3: Populate and verify the ten v2 profiles

**Files:**

- Modify in scratch: `source-notes.txt`
- Modify in scratch: `deck-content.json`

- [ ] **Step 1: Extract the v2 evidence bands**

For each v2 methodology, read and record:

- header metadata, unique axis, subject-model role, headline, and build-order position;
- `## 1. Whole-passage rationale`;
- `## 2. Methodology definition`;
- `## 4. Instrument architecture`;
- `## 5. Metrics`;
- `## 6. Ground truth and judges`;
- `## 7. Construction instructions`;
- `## 8. Differentiation`;
- `## 9. P1 pilot spec`.

For WITNESS, also record the build and live-readiness wording from its README and the parked re-entry prompt.

- [ ] **Step 2: Populate v2 records in exact portfolio order**

Write concise, audience-facing content for PILGRIM through GLEANING. Preserve each unique methodological axis and whole-passage rationale.

- [ ] **Step 3: Ground every illustrative v2 case**

The case must demonstrate the design’s unique axis: accumulated history for PILGRIM, principle conflict for CROSSWINDS, evaluator role for PLUMBLINE, calibrated bank behavior for CANTICLE, invariant moral skeleton for TESSERA, incentive price for LEDGER, endogenous social response for VILLAGE, explicit normative specification for SCRIBE, modality gap for WITNESS, and declaration ablation for GLEANING.

- [ ] **Step 4: Run complete content validation**

```bash
"$NODE" "$TMP/validate-content.mjs" "$ROOT" "$TMP/deck-content.json"
```

Expected: 20 ordered records pass with zero warnings.

---

### Task 4: Author synthesis content and generate the canonical Markdown deck

**Files:**

- Modify in scratch: `deck-content.json`
- Create in scratch: `render-markdown.mjs`
- Create final: `SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.md`

- [ ] **Step 1: Add closed synthesis sections to the content model**

Required synthesis records:

- portfolio purpose and the v1/v2 distinction;
- a reader key for anchor, construct, mechanism, evidence, strengths, limitations, and burden;
- v1 coverage/overlap synthesis;
- v2 whole-passage/infrastructure synthesis;
- cross-portfolio complementarity pairs and collision risks;
- implementation-burden matrix;
- current build status that distinguishes `design-complete`, `P1 harness built`, and `live-readiness work in progress`;
- dependency-aware recommended sequence;
- source/interpretation policy;
- closing synthesis.

- [ ] **Step 2: Implement deterministic Markdown rendering**

`render-markdown.mjs` writes:

- YAML metadata;
- `---` separators;
- one H1 per slide;
- two slides per design in exact order;
- visible labels matching the approved specification;
- one `Sources:` line per design slide using repository-relative paths;
- no speaker-production notes in visible content.

- [ ] **Step 3: Generate Markdown before any presentation artifact**

```bash
"$NODE" "$TMP/render-markdown.mjs" \
  "$TMP/deck-content.json" \
  "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.md"
```

Expected: 50–54 slides, all twenty names present in two profile slides each.

- [ ] **Step 4: Validate Markdown structure and source resolution**

Run a validator mode that parses the generated Markdown and checks:

```bash
"$NODE" "$TMP/validate-content.mjs" "$ROOT" "$TMP/deck-content.json" \
  --markdown "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.md"
```

Expected: exact profile counts, valid source paths, no placeholders, and no content-model/Markdown omissions.

---

### Task 5: Build the editable presentation with artifact-tool

**Files:**

- Create in scratch: `build-deck.mjs`
- Create final: `SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx`

- [ ] **Step 1: Implement the approved neutral research-grid system**

Use `Presentation.create({ slideSize: { width: 1280, height: 720 } })` and plain JavaScript ES modules. Reuse the proportions and hierarchy of Codex Grid slides 01, 04, 11, 13, 16, 17, and 26:

- slide 01/26 silhouette for cover and section dividers;
- slide 13 four-region silhouette for repeated design profiles;
- slide 11 for v1/v2 comparisons;
- slide 16 for portfolio inventories;
- slide 17 for dependency sequencing;
- slide 04 for source and interpretation policy.

Typography minimums are 50 px cover, 35 px slide titles, 24 px subheads, and 16 px body. Colors are `#FFFFFF`, `#000000`, `#EDEDED`, `#B8BCC4`, `#6DCBF4`, and `#3D8DFF`.

- [ ] **Step 2: Keep presentation content bound to the frozen model**

The builder reads `deck-content.json`; it does not embed an independent prose copy. Every slide gets a stable name, slide number, and source footer.

- [ ] **Step 3: Export PPTX, slide PNGs, layout JSON, and montage**

```bash
cd "$TMP"
"$NODE" build-deck.mjs \
  --content "$TMP/deck-content.json" \
  --pptx "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx" \
  --slides "$TMP/slides" \
  --layouts "$TMP/layout" \
  --montage "$TMP/preview/deck-montage.webp"
```

Expected: one PNG and one layout JSON per slide plus the editable PPTX.

- [ ] **Step 4: Run overflow diagnostics**

```bash
"/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3" \
  "$SKILL_DIR/container_tools/slides_test.py" \
  "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx"
```

Expected: no out-of-bounds objects. Any warning is inspected and fixed; none is dismissed without visual confirmation.

---

### Task 6: Perform full-slide visual QA and revise

**Files:**

- Modify in scratch: `build-deck.mjs`, `deck-content.json`
- Regenerate final: `sermonmount-20-design-research-atlas.md`, `.pptx`

- [ ] **Step 1: Inspect the montage for narrative pacing**

Check section transitions, repeated-slide monotony, accent consistency, and whether v1 and v2 remain visually equal in authority.

- [ ] **Step 2: Inspect every slide PNG at full size**

For each slide, record pass/fail in `qa/slide-review.txt` for:

- title wrapping;
- clipped or overlapping text;
- body size below 16 px;
- excessive density;
- missing source footer;
- inconsistent case/strength/limitation labels;
- malformed characters;
- unresolved template copy.

- [ ] **Step 3: Revise content before shrinking text**

When a slide is too dense, shorten the presentation wording while preserving the canonical claim in Markdown. If shortening would remove a required claim, split a synthesis slide within the allowed 50–54 slide range.

- [ ] **Step 4: Repeat render and diagnostics until every slide passes**

Expected: `qa/slide-review.txt` contains one `PASS` record per final slide and no unresolved warnings.

---

### Task 7: Create and verify the widescreen slide PDF

**Files:**

- Create final: `SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf`

- [ ] **Step 1: Convert the verified PPTX with bundled LibreOffice**

```bash
SOFFICE="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/soffice"
mkdir -p "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf" "$TMP/pdfs/slides-render"
"$SOFFICE" --headless --convert-to pdf \
  --outdir "$TMP/pdfs" \
  "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx"
mv "$TMP/pdfs/sermonmount-20-design-research-atlas.pdf" \
  "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf"
```

- [ ] **Step 2: Verify PDF metadata and page count**

```bash
PDFINFO="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo"
"$PDFINFO" "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf"
```

Expected: 16:9 landscape pages and page count equal to the PPTX slide count.

- [ ] **Step 3: Render and inspect every PDF page**

```bash
PDFTOPPM="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"
"$PDFTOPPM" -png -r 144 \
  "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf" \
  "$TMP/pdfs/slides-render/page"
```

Inspect all rendered pages and confirm they match the already-approved slide PNGs without font substitution, clipping, or black boxes.

---

### Task 8: Create and verify the print-friendly research handout

**Files:**

- Create in scratch: `build-handout.py`
- Create final: `SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-handout.pdf`

- [ ] **Step 1: Implement a portrait report layout from the same content model**

Use ReportLab with letter or A4 pages, 0.65-inch margins, searchable text, page numbers, repeated design name/portfolio header, and visible source paths. Each design receives a two-page profile when required for legibility; the handout must not rasterize slide screenshots.

- [ ] **Step 2: Generate the handout**

```bash
PY="/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
"$PY" "$TMP/build-handout.py" \
  --content "$TMP/deck-content.json" \
  --output "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-handout.pdf"
```

- [ ] **Step 3: Verify text and structure**

Use pypdf to assert:

- every design name appears;
- all 20 source paths appear;
- no placeholder terms appear;
- page count is at least 40 and remains within a readable 60-page maximum;
- extracted text is nonempty on every non-divider page.

- [ ] **Step 4: Render and inspect every handout page**

```bash
mkdir -p "$TMP/pdfs/handout-render"
"$PDFTOPPM" -png -r 144 \
  "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-handout.pdf" \
  "$TMP/pdfs/handout-render/page"
```

Inspect every rendered page for widows/orphans, clipped source paths, broken lists, malformed glyphs, and inconsistent headers/footers. Regenerate until all pages pass.

---

### Task 9: Run final cross-format integrity checks

**Files:**

- Verify all four final deliverables; modify only if a check fails.

- [ ] **Step 1: Confirm final paths and nonzero sizes**

```bash
test -s "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.md"
test -s "$ROOT/SERMONMOUNT-v2/DECKS/sermonmount-20-design-research-atlas.pptx"
test -s "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-slides.pdf"
test -s "$ROOT/SERMONMOUNT-v2/DECKS/output/pdf/sermonmount-20-design-research-atlas-handout.pdf"
```

- [ ] **Step 2: Verify twenty-design coverage across all formats**

Use the Markdown parser, artifact-tool inspection, and pypdf extraction to assert the ordered design list appears in every deliverable.

- [ ] **Step 3: Scan for placeholders and production leakage**

Reject `TODO`, `TBD`, `lorem ipsum`, `title goes here`, `detail goes here`, internal timing notes, prompt text, or tool-token strings.

- [ ] **Step 4: Verify repository scope**

```bash
git status --short -- SERMONMOUNT SERMONMOUNT-v2
```

Expected: only the new `SERMONMOUNT-v2/DECKS/` artifacts are changed; all source designs and historical WITNESS files remain byte-identical.

- [ ] **Step 5: Record final QA evidence**

Write final counts and checks to scratch `qa/final-report.txt`, including Markdown slide count, PPTX slide count, both PDF page counts, coverage result, placeholder scan result, slide overflow result, and visual-inspection completion.

- [ ] **Step 6: Do not stage or commit**

Leave all final artifacts unstaged. Git publication requires separate user authorization.

---

## Plan self-review result

- **Specification coverage:** Every approved deliverable, source policy, profile field, visual constraint, and QA requirement maps to a task above.
- **Type consistency:** `deck-content.json` is the only structured content model and is consumed by Markdown, PowerPoint, and handout builders.
- **Scope consistency:** Source benchmark files remain read-only; only the isolated deck directory receives final files.
- **Placeholder check:** The plan contains no unresolved implementation placeholder; banned placeholder terms appear only as explicit QA rejection strings.
- **Execution constraint:** This side conversation does not permit sub-agents, so implementation must use the inline `superpowers:executing-plans` workflow.
