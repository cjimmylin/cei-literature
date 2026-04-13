# CHANGELOG — v2.2 (2026-04-13)

**Output:** `20260413-cross-cultural-ai-values-alignment-v2.2.pdf` (97pp, 3.4 MB)
**Previous:** `PAPER-V2/20260412-cross-cultural-ai-values-alignment-v2.1.pdf` (96pp, 3.4 MB) — frozen, untouched

---

## What's new in v2.2

### Architectural
- **Fully self-contained bundle.** All source files (11 section markdowns, 10 main figures, 7 supplementary figures, 5 supplementary text sections) are now copied into `v2.2/` itself. The generator reads nothing from outside the subfolder — rebuilding v2.2 requires only `PAPER-V2/v2.2/` and the Arial Unicode font. Portable and immutable.
- **Path anchor discipline.** `generate_combined_pdf_v2.2.py` resolves every anchor (`SECTIONS_DIR`, `FIGURES_DIR`, `SUPP_DIR`, `SUPP_FIG_DIR`, `FONT_PATH`) via `pathlib.Path(__file__).resolve().parent`, eliminating CWD-dependent failure modes.
- **Dry-run assertions before fpdf2 writes.** Every required anchor, section, and figure is existence-checked before the first PDF page is written. Prevents the fpdf2 "silent figure drop" trap (cf. Children v4 figure-glob bug, vault memory 20260412h).
- **Explicit figure lists, no globs.** Main figures and supplementary figures are enumerated by name. Adding or removing a figure is an explicit, reviewable change.
- **Single authorized invocation.** `build_v2.2.sh` is the one way to build v2.2 (resolves its own directory so it can be run from anywhere). Documented in this CHANGELOG.

### Content
- Title page updated: version bumped to v2.2, date bumped to 20260413, includes dashboard URL link.
- Table of contents expanded: "1. Introduction" line restored (was missing from v2.1 TOC), "10. Endmatter" line added.
- Paired dashboard at https://cjimmylin.github.io/cei-cultural-global-dashboard-v2/ (see separate handoff).
- Page count: 97 (v2.1: 96, +1 from richer title page + TOC entries). Within expected delta ±2.

### Not changed (frozen)
- All 11 section markdown files (`v2.2/sections/00-abstract.md` … `10-endmatter.md`) are byte-identical copies of the 2026-04-13 v2.1 source. Verified against `PAPER-V2/v2.1-source-snapshot/`.
- All 10 main figures and 7 supplementary figures are byte-identical copies.
- All 5 supplementary text sections are byte-identical copies.
- No prose edits, no methods footnote changes, no citation rewrites.

---

## Immutability contract

The following files are **frozen** by this release and must never be modified:
- `PAPER-V2/20260412-cross-cultural-ai-values-alignment-v2.1.pdf`
- `PAPER-V2/generate_combined_pdf.py` (the v2.1 generator)
- `PAPER-V2/v2.1-source-snapshot/*.md` (immutable v2.1 markdown reference)

v2.2 operations did not touch any of them. Verified at build time by shasum + diff — see `VERIFICATION-GATES-v2.2.md`.

---

## Known issues carried over from v2.1

These are unresolved in v2.2 and require a separate session with its own council.

### 1. MFQ foundation-means reconciliation (deferred)
`verify_mfq.py` (v2.1) flags that Sonnet and Haiku recomputed I:B ratios differ from documented pre-rounded values by 0.16–0.18 points:
- Sonnet I:B ratio as printed: 3.23 / 3.14 (derived)
- Haiku I:B ratio as printed: 4.82 / 3.75 (derived)

The discrepancy arises from rounding-order non-commutativity in the MFQ report-both aggregation pipeline. v2.2 does **not** attempt to resolve this — a statistical correction is out of scope for a combined-PDF regeneration. The paper's Methods §2.15 footnote already discloses the rounding-order non-commutativity. If a reviewer flags the specific 0.16–0.18pt drift, a separate session should:
1. Re-read raw `COMPARISON/20260404-all-model-comparison-summary.json`
2. Re-derive I:B ratios with a single canonical rounding rule
3. Patch methods footnote, Table 8, and Figure 8 caption if values change
4. Produce a v2.3 bundle

### 2. Six deferred low-DPI figures
Figures 1-4 and S-Figs 1, 7 remain at sub-600 DPI because their generator scripts are unidentified (Plotly or unknown R/manual exports). Provenance matrix: `PAPER-V2/METHODS/council-v21/T1.2-figure-spec-sheet.md`. Acceptable for specialist venues (FAccT/JAIR/BD&S); would block Nature-family submission without source audit.

### 3. 68 orphaned references
Flagged by `audit_references.py` v2.1. Of the 133 references, 65 are cited in prose; 68 are not. Five of these are "Norenzayan (2010)" narrative-form false positives — the actual reference is under `Henrich_2010` (the reference is "Henrich, Heine, and Norenzayan, 2010" and the narrative prose cites "Henrich et al. (2010)" in most places but "Norenzayan (2010)" in 5 locations). A rewrite pass in a future session should consolidate. No deletion in v2.2.

### 4. Venue lock-in deferred
T1.1 v2.1 council memo measured conversion costs: NHB 29-39h, PNAS 22-32h, specialist (FAccT/JAIR/BD&S) 9-14h. Decision remains with the author.

---

## Build reproducibility

From a clean state, rebuilding v2.2 requires:

```bash
cd CEI-Lit-WS/CULTURAL-GLOBAL/PAPER-V2/v2.2
bash build_v2.2.sh
```

Expected output:
- `DRY-RUN OK — all required anchors present.`
- `Combined PDF: …/v2.2/20260413-cross-cultural-ai-values-alignment-v2.2.pdf`
- `Size: 3413.8 KB`
- `Pages: 97`

If dry-run fails, the script exits with status 1 and prints every missing anchor. No partial PDF is written.

---

## File manifest

```
v2.2/
├── sections/             (11 md files, 259 KB total — byte-identical to PAPER-V2/*.md)
├── figures/              (22 files: 10 main × PDF+PNG pairs, plus 2 extras)
├── supplementary/
│   ├── S1-methods.md … S5-keyword-lists.md  (5 text sections)
│   └── supp-figures/     (21 files: 7 supp × PDF+PNG pairs, plus 7 legacy PNG)
├── generate_combined_pdf_v2.2.py
├── build_v2.2.sh
├── 20260413-cross-cultural-ai-values-alignment-v2.2.pdf  (97pp, 3.4 MB)
├── CHANGELOG-v2.2.md     (this file)
├── VERIFICATION-GATES-v2.2.md
├── build.log
└── council-v22/
    ├── alt-critique/     (archive of 12-critic alternate council memos)
    └── critique/         (internal 6-critic pass)
```

Paired dashboard: `https://cjimmylin.github.io/cei-cultural-global-dashboard-v2/`
