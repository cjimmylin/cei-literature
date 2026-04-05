# Moral Psychology -- Session 18 Handoff: Paper v2.1 Mechanical Fixes

**Date:** 2026-04-05
**Session:** Fix 3 known issues from S17: table renumbering, figure reordering, table overflow
**Project:** `CEI-Lit-WS/MORAL-PSYCH/PAPER-v2/`
**Previous handoff:** `MORAL-PSYCH/METHODS/20260405d-moral-psych-session17-final-handoff.md`

---

## What Was Done This Session

### 1. Table Renumbering (Issue 1 from S17)

Resolved table numbering collisions caused by 12 parallel agents numbering tables independently per section. All 25 main-paper tables now use global sequential numbering (Table 1 through Table 25).

**Collision resolution:**

| Old Number | New Number | File | Content |
|------------|-----------|------|---------|
| Table 4 | Table 3 | methodology-empirical | Nine-Model Inventory |
| Table 5 | Table 4 | methodology-empirical | Twenty-Three-Benchmark Inventory |
| Table 2 | Table 5 | results-claims1-3 | Theory Representation |
| Table 3 | Table 6 | results-claims1-3 | Construct Validity |
| Table 4 | Table 7 | results-claims1-3 | Theory Gap Summary |
| Table 5 | Table 8 | results-claims4-5 | Human Baseline Availability |
| Table 6 | Table 9 | results-claims4-5 | Task Format Distribution |
| Table 5.1 | Table 10 | results-convergence | Convergence Ranking |
| Table 5.2 | Table 11 | results-convergence | Discrimination Tiers |
| Table 5.3 | Table 12 | results-convergence | RLHF Fingerprint |
| Table 5.3.2 | Table 13 | results-scale-cot | Scale-sensitivity patterns |
| Table 5.3.3 | Table 14 | results-scale-cot | Direction of scale effects |
| Table 5.4.1 | Table 15 | results-scale-cot | Dual-process results |
| Table 5.5.1--5.5.7 | Tables 16--22 | results-patterns | Theory-specific profiles |
| Table 5.6.1--5.6.3 | Tables 23--25 | results-patterns | Discrimination audit |

Cross-references updated in: methodology-empirical (1 ref), results-convergence (2 refs), results-scale-cot (1 ref), discussion (1 ref).

### 2. Figure Reordering (Issue 5 from S17)

Figures 3--6 appeared out of sequence in the assembled document. Renumbered to match appearance order:

| Appearance | Old # | New # | Content | File |
|-----------|-------|-------|---------|------|
| 3rd | Fig 5 | Fig 3 | Construct validity distribution | results-claims1-3 |
| 4th | Fig 3 | Fig 4 | Theory coverage heatmap | results-claims1-3 |
| 5th | Fig 6 | Fig 5 | Human baseline availability | results-claims4-5 |
| 6th | Fig 4 | Fig 6 | Implementation status grid | results-claims4-5 |

PNG filenames unchanged (descriptive enough; avoids breaking external refs). Supplementary figure descriptions in `supp-figures.md` also updated (4 edits).

### 3. Table Overflow Fix (Issue 6 from S17)

Added `\newpage` before Table 10 (convergence ranking, 20 rows) in `results-empirical-convergence.md`. This ensures the table starts at the top of a fresh page, preventing bottom-row collision on p.62.

### 4. Combined PDF Rebuilt

Updated build script: version `v2.0` → `v2.1`, output filename `20260405-mpbench-v2.1-combined.pdf`. PDF rebuilt clean (4,211 KB).

---

## Files Modified (8 section/supplementary files + 1 script + 1 PDF output)

| File | Edits | Changes |
|------|-------|---------|
| `sections/methodology-empirical-mpbench.md` | 3 | Table 4→3, Table 5→4, ref update |
| `sections/results-landscape-claims1-3.md` | 8 | Tables 2→5, 3→6, 4→7; Figs 5→3, 3→4 |
| `sections/results-landscape-claims4-5.md` | 4 | Tables 5→8, 6→9; Figs 6→5, 4→6 |
| `sections/results-empirical-convergence.md` | 6 | Tables 5.1→10, 5.2→11, 5.3→12; refs; \newpage |
| `sections/results-empirical-scale-cot.md` | 4 | Tables 5.3.2→13, 5.3.3→14, 5.4.1→15; ref |
| `sections/results-empirical-patterns.md` | 10 | Tables 5.5.1--5.6.3 → 16--25 |
| `sections/discussion-mpbench.md` | 1 | Table 5.1→10 ref |
| `supplementary/supp-figures.md` | 4 | Figure number updates for Figs 3--6 |
| `scripts/build_combined_pdf.py` | 2 | Version v2.1, output filename |

## Output

| File | Size | Notes |
|------|------|-------|
| `20260405-mpbench-v2.1-combined.pdf` | 4,211 KB | v2.1, all 3 issues fixed |
| `20260405-mpbench-v2-combined.pdf` | 4,212 KB | v2.0, prior version (retained) |

---

## Remaining Work (from S17, updated)

### Priority 1: Introduction Update
Introduction unchanged from v1. Needs 2--3 sentences in sections 1.5 and 1.6 previewing cross-vendor findings.

### Priority 2: Bibliography Update
Bibliography copied from v1 (155+ refs). Needs ~10--20 new citations for cross-vendor material added in v2 sections.

### Priority 3: Supplementary Figures SF1--SF4
Specifications written in supp-figures.md but generation scripts not yet built (need cross-vendor JSON data processing).

### Priority 4: Full PDF (with Intro + Related Work)
Current combined PDF excludes intro and related work per user request. A complete paper PDF will be needed for submission.

### Priority 5: Journal Trimming
54,623 words main text far exceeds Nature MI 5,000-word limit. Aggressive trimming needed (supplementary material absorbs most detail).

### Priority 6: LaTeX Conversion
For Nature MI submission, LaTeX formatting will eventually be needed.

## Known Issues (from S17, updated)

| # | Issue | Status |
|---|-------|--------|
| 1 | ~~Table numbering collisions~~ | **RESOLVED** (S18) |
| 2 | Gemini data provenance: 21/23 interpolated | Documented in paper |
| 3 | Self-administration confound | Documented in paper |
| 4 | Word count: 54,623 words needs trimming | Unresolved |
| 5 | ~~Figure ordering: Fig 4/6 out of sequence~~ | **RESOLVED** (S18) |
| 6 | ~~Table overflow on p.62~~ | **RESOLVED** (S18) |

---

*Filed: 2026-04-05 | CEI-Lit-WS/MORAL-PSYCH/METHODS/*
