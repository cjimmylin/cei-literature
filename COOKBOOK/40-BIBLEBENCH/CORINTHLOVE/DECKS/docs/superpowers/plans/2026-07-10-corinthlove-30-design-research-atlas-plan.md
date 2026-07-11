# CORINTHLOVE 30-Design Research Atlas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. This side conversation does not permit subagent delegation.

**Goal:** Produce a source-grounded 42-slide Markdown research atlas and four visually verified PDFs covering all 30 CORINTHLOVE designs.

**Architecture:** A normalized in-memory design record drives two outputs: the canonical slide-oriented Markdown and an editable artifact-tool PowerPoint rendering intermediary. LibreOffice converts the intermediary to the full PDF; `pypdf` extracts the three generation PDFs. Artifact-tool previews, Poppler page renders, structural checks, and full-page visual inspection provide independent layout and content verification.

**Tech Stack:** Markdown, plain JavaScript ES modules, `@oai/artifact-tool`, bundled Node.js, bundled LibreOffice, bundled Poppler, bundled Python with `pypdf`, and the presentation/PDF QA utilities.

---

## File map

**Final output directory:**
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/DECKS`

**Create final artifacts:**

- `corinthlove-30-design-research-atlas.md` — canonical Markdown deck.
- `corinthlove-30-design-research-atlas.pptx` — editable rendering intermediary retained for reproducibility.
- `corinthlove-30-design-research-atlas.pdf` — complete 42-page deck.
- `corinthlove-v1-design-atlas.pdf` — pages 5–15 of the complete deck.
- `corinthlove-v2-design-atlas.pdf` — pages 16–26 of the complete deck.
- `corinthlove-v3-design-atlas.pdf` — pages 27–37 of the complete deck.

**External scratch workspace:**

- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/source-notes.txt`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/atlas-data.json`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/build-atlas.mjs`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/slides/`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/layout/`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/preview/`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/qa/`
- `$TMPDIR/codex-presentations/$CODEX_THREAD_ID/corinthlove-30-design-atlas/tmp/pdfs/`

No existing benchmark source file will be modified. No commit, stage, or push is part of this plan.

---

### Task 1: Establish the source inventory and scratch workspace

**Files:**

- Read: `CORINTHLOVE/DESIGNS/00-10cbench-portfolio.md`
- Read: `CORINTHLOVE/DESIGNS/01-longsuffer.md` through `07-charitroc.md`
- Read: `CORINTHLOVE-v2/00-corinthlove-v2-portfolio.md`
- Read: `CORINTHLOVE-v2/DESIGNS/01-gallery.md` through `10-onebody.md`
- Read: `CORINTHLOVE-v3/00-corinthlove-v3-portfolio.md`
- Read: `CORINTHLOVE-v3/DESIGNS/01-crossroads.md` through `10-facetoface.md`
- Read: applicable CORINTHLOVE gate amendments and build handoffs
- Create: external scratch paths listed in the file map

- [ ] **Step 1: Compute deterministic runtime paths**

Run:

```bash
RUNTIME=/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies
NODE=$RUNTIME/node/bin/node
PY=$RUNTIME/python/bin/python3
NATIVE=$RUNTIME/bin
SKILL_DIR=/Users/jimmy.lin/.codex/plugins/cache/openai-primary-runtime/presentations/26.709.12203/skills/presentations
THREAD_ID=${CODEX_THREAD_ID:-manual-corinthlove-atlas}
WORKSPACE=$TMPDIR/codex-presentations/$THREAD_ID/corinthlove-30-design-atlas
TMP_DIR=$WORKSPACE/tmp
OUTPUT_DIR=/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/DECKS
```

Expected: every variable resolves to an absolute path and `OUTPUT_DIR` is inside the CORINTHLOVE source boundary.

- [ ] **Step 2: Create scratch and output directories**

Run:

```bash
mkdir -p "$TMP_DIR/slides" "$TMP_DIR/layout" "$TMP_DIR/preview" \
  "$TMP_DIR/qa" "$TMP_DIR/pdfs" "$TMP_DIR/assets" "$OUTPUT_DIR"
```

Expected: all directories exist; no existing benchmark artifact changes.

- [ ] **Step 3: Build the exact source inventory**

Create `source-notes.txt` with one row per source file and the sections used. The inventory must explicitly record:

- v1 designs 01–07: full brief + portfolio + gate amendments.
- v1 designs 08–09: portfolio specification only; full briefs absent.
- v1 design 10: portfolio specification plus CO-9 supersession.
- v2 designs 01–10: full brief + portfolio + gate amendments.
- v3 designs 01–10: full brief + portfolio + gate amendments.
- DIMGLASS and CHARITROC: current build/review status sources.

- [ ] **Step 4: Verify source isolation**

Run:

```bash
grep -nE 'TENCOMMANDMENTS|FRUITBENCH|SERMONMOUNT|icmi-proceedings' "$TMP_DIR/source-notes.txt"
```

Expected: no output.

---

### Task 2: Normalize all 30 design records

**Files:**

- Create: `$TMP_DIR/atlas-data.json`
- Test: `$TMP_DIR/qa/validate-atlas-data.mjs`

- [ ] **Step 1: Define the exact record schema in the validator**

The validator must require this exact shape for every design:

```javascript
{
  generation: "v1" | "v2" | "v3",
  number: 1..10,
  codename: "UPPERCASE",
  anchor: "non-empty passage anchor",
  construct: "non-empty secular construct",
  claim: "one audience-facing sentence",
  design: ["2–4 concise experimental-design bullets"],
  metric: "exact primary metric or model",
  case: ["2–3 concrete illustrative beats"],
  strengths: ["2–3 analytical strengths"],
  limitations: ["2–3 analytical limitations"],
  status: "design-only | brief available | built | live-tested | deferred | superseded",
  source: "relative CORINTHLOVE source path"
}
```

The validator must assert exactly 30 unique `generation:number` keys, exactly ten per generation, non-empty arrays within the declared bounds, and the exact codename sequence:

```text
v1: LONGSUFFER, COSTLYKIND, STATUSGAME, LEDGER, TRUTHGRACE,
    ROOFTOP, CHARITROC, SECONDCHANCE, LONGHAUL, NOISYGONG
v2: GALLERY, TEMPO, EVENHAND, EGOTAX, BACKTALK,
    REBOUND, OPENDOOR, STAYPOINT, DIMGLASS, ONEBODY
v3: CROSSROADS, WEEKLONG, MANYMIRRORS, WITNESS, AGAPEGAME,
    WEIGHBRIDGE, TONGUES, LOADBEAR, CRUCIBLE, FACETOFACE
```

- [ ] **Step 2: Run the validator against an absent data file**

Run:

```bash
"$NODE" "$TMP_DIR/qa/validate-atlas-data.mjs"
```

Expected: non-zero exit stating that `atlas-data.json` is absent.

- [ ] **Step 3: Author all 30 records from the inventory**

Use exact metric terminology from the source briefs. Mark every case as illustrative in the eventual slide label. Distinguish proposed discrimination mechanisms from live evidence. Set:

- NOISYGONG status to `superseded`.
- SECONDCHANCE and LONGHAUL to `design-only` because full briefs are absent.
- DIMGLASS and CHARITROC status from their current dated handoffs and verified artifacts.
- All other unbuilt designs to `brief available` unless a binding amendment makes `deferred` more accurate.

- [ ] **Step 4: Run the data validator**

Run:

```bash
"$NODE" "$TMP_DIR/qa/validate-atlas-data.mjs"
```

Expected: exit 0 with `30 records; v1=10; v2=10; v3=10`.

---

### Task 3: Author and validate the canonical Markdown deck first

**Files:**

- Create: `CORINTHLOVE/DECKS/corinthlove-30-design-research-atlas.md`
- Create: `$TMP_DIR/qa/validate-markdown.mjs`

- [ ] **Step 1: Write the Markdown validator**

Require:

- YAML frontmatter containing title, 16:9 ratio, Research Atlas palette, and page numbering.
- Exactly 42 slide sections separated by `\n---\n`.
- Exactly 30 sections containing `<!-- design-slide -->`.
- Every required codename exactly once as a design-slide heading.
- Every design slide containing the labels `DESIGN`, `PRIMARY METRIC`, `ILLUSTRATIVE CASE`, `STRENGTHS`, `LIMITATIONS`, `STATUS`, and `SOURCE`.
- No `TODO`, `TBD`, `PLACEHOLDER`, production note, or sibling-benchmark name.

- [ ] **Step 2: Run the validator against an absent Markdown deck**

Run:

```bash
"$NODE" "$TMP_DIR/qa/validate-markdown.mjs"
```

Expected: non-zero exit stating that the final Markdown file is absent.

- [ ] **Step 3: Author slides 1–5**

Write the title, research question, three-generation architecture, atlas-reading guide, and v1 divider. Slide 3 must state the generational logic precisely: v1 = levels/thresholds, v2 = dynamics/social embedding, v3 = whole-profile triangulation/property studies.

- [ ] **Step 4: Author slides 6–15 from the ten v1 records**

Each slide uses the standard anatomy. SECONDCHANCE and LONGHAUL disclose portfolio-only source depth. NOISYGONG discloses supersession rather than presenting it as an active build.

- [ ] **Step 5: Author slides 16–26 from the ten v2 records**

The v2 divider introduces causal deltas, trajectories, optimal timing, and social-system outcomes. Each design slide preserves its exact dynamic quantity.

- [ ] **Step 6: Author slides 27–37 from the ten v3 records**

The v3 divider separates first-order profile methods from property studies. TONGUES, LOADBEAR, CRUCIBLE, and FACETOFACE must reflect the gate-amended property-study framing.

- [ ] **Step 7: Author slides 38–42**

Create the unit-of-analysis map, measurement-tradeoff comparison, portfolio critique, build-status roadmap, and source/caveat close. The closing slide must resolve the opening question by explaining why no single methodology suffices.

- [ ] **Step 8: Run the Markdown validator**

Run:

```bash
"$NODE" "$TMP_DIR/qa/validate-markdown.mjs"
```

Expected: exit 0 with `42 slides; 30 design slides; all codenames covered`.

---

### Task 4: Build the visual deck with artifact-tool

**Files:**

- Create: `$TMP_DIR/build-atlas.mjs`
- Create: `CORINTHLOVE/DECKS/corinthlove-30-design-research-atlas.pptx`
- Create: `$TMP_DIR/slides/slide-01.png` through `slide-42.png`
- Create: `$TMP_DIR/layout/slide-01.layout.json` through `slide-42.layout.json`
- Create: `$TMP_DIR/preview/research-atlas-montage.webp`

- [ ] **Step 1: Initialize the artifact-tool workspace**

Run:

```bash
"$NODE" "$SKILL_DIR/container_tools/setup_artifact_tool_workspace.mjs" \
  --workspace "$TMP_DIR"
```

Expected: `$TMP_DIR/node_modules/@oai/artifact-tool` resolves successfully.

- [ ] **Step 2: Implement the palette and page primitives**

Use a 1280×720 canvas and these tokens:

```javascript
const COLORS = {
  navy: "#0B1724",
  navy2: "#12283A",
  paper: "#F4F0E6",
  muted: "#A9B4BC",
  v1: "#55A7D6",
  v2: "#66B68A",
  v3: "#D6A444",
  risk: "#D0776B",
  line: "#294257"
};
const FRAME = { left: 64, top: 52, width: 1152, height: 616 };
```

Implement reusable functions for title slides, generation dividers, design slides, synthesis slides, source footers, page numbers, and generation accent bars. Use at least 50 px for the deck title, 35 px for slide titles, 24 px for section labels, and 16 px for body copy.

- [ ] **Step 3: Implement the two alternating design-slide compositions**

Layout A: left column for illustrative case; right column for experimental design and metric; bottom strip for strengths, limitations, status, and source.

Layout B: top band for claim and metric; lower-left for experimental sequence; lower-right for case; bottom strip for strengths, limitations, status, and source.

Both layouts must use the same content hierarchy and exact generation color.

- [ ] **Step 4: Materialize all 42 slides**

The builder must load `atlas-data.json`, create slides in the exact approved order, add stable object names, export every slide PNG and layout JSON, export a montage, and save the PowerPoint intermediary.

- [ ] **Step 5: Run the builder**

Run:

```bash
env NODE_PATH=/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules \
  "$NODE" "$TMP_DIR/build-atlas.mjs"
```

Expected: exit 0; 42 PNGs, 42 layout JSON files, one montage, and one PPTX.

- [ ] **Step 6: Run presentation overflow checks**

Run:

```bash
"$PY" "$SKILL_DIR/container_tools/slides_test.py" \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pptx"
```

Expected: zero overflow or overlap errors requiring correction.

---

### Task 5: Export and split the PDFs

**Files:**

- Create: the four final PDFs listed in the file map
- Create: `$TMP_DIR/qa/split-generation-pdfs.py`

- [ ] **Step 1: Convert the PowerPoint intermediary to PDF**

Run:

```bash
"$NATIVE/soffice" --headless --convert-to pdf --outdir "$OUTPUT_DIR" \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pptx"
```

Expected: `corinthlove-30-design-research-atlas.pdf` exists.

- [ ] **Step 2: Verify the complete PDF page count**

Run:

```bash
"$NATIVE/pdfinfo" "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pdf" \
  | grep '^Pages:'
```

Expected: `Pages: 42`.

- [ ] **Step 3: Implement exact generation splitting with pypdf**

The script must copy these zero-based page ranges from the complete PDF:

```python
RANGES = {
    "corinthlove-v1-design-atlas.pdf": range(4, 15),
    "corinthlove-v2-design-atlas.pdf": range(15, 26),
    "corinthlove-v3-design-atlas.pdf": range(26, 37),
}
```

Each output contains one generation divider and ten design slides.

- [ ] **Step 4: Run the split and page-count checks**

Run:

```bash
"$PY" "$TMP_DIR/qa/split-generation-pdfs.py"
for pdf in "$OUTPUT_DIR"/corinthlove-v?-design-atlas.pdf; do
  "$NATIVE/pdfinfo" "$pdf" | grep '^Pages:'
done
```

Expected: three outputs, each reporting `Pages: 11`.

---

### Task 6: Perform full visual QA and correction

**Files:**

- Create: `$TMP_DIR/pdfs/full/page-01.png` through `page-42.png`
- Create: `$TMP_DIR/qa/visual-qa-ledger.txt`
- Modify as needed: Markdown, data JSON, builder, PPTX, and PDFs

- [ ] **Step 1: Render every complete-PDF page at review resolution**

Run:

```bash
mkdir -p "$TMP_DIR/pdfs/full"
"$NATIVE/pdftoppm" -png -r 150 \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pdf" \
  "$TMP_DIR/pdfs/full/page"
```

Expected: exactly 42 PNG files.

- [ ] **Step 2: Inspect the montage for deck-level flow**

Review the artifact-tool montage for generation-color consistency, pacing, visual rhythm, and obvious density spikes.

- [ ] **Step 3: Inspect all 42 pages individually at full size**

Record one PASS/FIX line per page in `visual-qa-ledger.txt`, checking:

- title wrapping and hierarchy;
- body readability;
- case/design balance;
- clipped or overlapping text;
- source-footer legibility;
- page number and generation accent;
- unsupported or ambiguous status language.

- [ ] **Step 4: Correct every FIX entry and regenerate all dependent artifacts**

Re-run Tasks 3–6 after any content or layout correction. Do not patch only a split PDF; regenerate from the canonical Markdown/data and full deck.

- [ ] **Step 5: Reinspect corrected pages**

Expected: `visual-qa-ledger.txt` contains 42 PASS entries and zero FIX entries.

---

### Task 7: Run content and artifact verification

**Files:**

- Create: `$TMP_DIR/qa/final-verify.py`
- Create: `$TMP_DIR/qa/checksums.txt`

- [ ] **Step 1: Verify Markdown structure and codenames again**

Run:

```bash
"$NODE" "$TMP_DIR/qa/validate-atlas-data.mjs"
"$NODE" "$TMP_DIR/qa/validate-markdown.mjs"
```

Expected: both exit 0 with exact 30/42 counts.

- [ ] **Step 2: Extract and validate PDF text**

`final-verify.py` must use `pypdf` to assert:

- 42 pages in the complete PDF;
- 11 pages in every generation PDF;
- every codename appears in the complete PDF;
- each generation PDF contains exactly its ten codenames and no design codename from another generation;
- `ILLUSTRATIVE CASE`, `STRENGTHS`, `LIMITATIONS`, and `PRIMARY METRIC` appear on every design page;
- no `TODO`, `TBD`, `PLACEHOLDER`, or hidden production note appears.

Run:

```bash
"$PY" "$TMP_DIR/qa/final-verify.py"
```

Expected: `PDF verification PASS: full=42; v1=11; v2=11; v3=11; designs=30`.

- [ ] **Step 3: Verify output files and checksums**

Run:

```bash
shasum -a 256 \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.md" \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pptx" \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.pdf" \
  "$OUTPUT_DIR/corinthlove-v1-design-atlas.pdf" \
  "$OUTPUT_DIR/corinthlove-v2-design-atlas.pdf" \
  "$OUTPUT_DIR/corinthlove-v3-design-atlas.pdf" \
  > "$TMP_DIR/qa/checksums.txt"
```

Expected: six non-empty SHA-256 rows.

- [ ] **Step 4: Run final whitespace and source-boundary checks**

Run:

```bash
grep -R -nE 'TENCOMMANDMENTS|FRUITBENCH|SERMONMOUNT|icmi-proceedings' \
  "$OUTPUT_DIR/corinthlove-30-design-research-atlas.md"
git diff --check -- CORINTHLOVE/DECKS
```

Expected: the scope grep returns no output and `git diff --check` exits 0.

---

### Task 8: Deliver the atlas

**Files:**

- Read: all six final output artifacts and QA results

- [ ] **Step 1: Re-read the approved specification and verify every acceptance criterion**

Expected: each criterion maps to current verification evidence, not an earlier run.

- [ ] **Step 2: Provide concise delivery links**

Return links to the canonical Markdown, complete PDF, three generation PDFs, and optional PPTX intermediary. State the exact page counts and that examples are illustrative, not validated items unless explicitly marked.

- [ ] **Step 3: Preserve the scratch workspace for follow-up edits**

Do not delete the external scratch workspace. It contains the builder, source notes, layouts, previews, and QA ledger needed for revisions.
