# Phase 2.5: Adjudication — Canonical Contracts

**Date:** 2026-04-12
**Purpose:** Resolve Phase 2 conflicts, freeze figure mapping, define agent output contracts.

---

## 1. Canonical Figure-to-Filename Mapping (FROZEN)

No agent may rename or renumber figures without updating this mapping.

| Paper Ref | Filename (in `PAPER-V2/figures/`) | Type | Target DPI | Target Width |
|-----------|-----------------------------------|------|-----------|-------------|
| Fig. 1 | `Figure1-world-map-weird.png` | Halftone | 300 | 180mm (double) |
| Fig. 2 | `Figure2-heatmap-regions.png` | Combination | 600 | 180mm (double) |
| Fig. 3 | `Figure3-dendrogram.png` | Line art | 600 | 88mm (single) |
| Fig. 4 | `Figure4-correspondence-biplot.png` | Combination | 600 | 180mm (double) |
| Fig. 5 | `Figure5-benchmark-clusters.png` | Combination | 600 | 180mm (double) |
| Fig. 6 | `Figure6-concept-coverage.png` | Line art | 600 | 88mm (single) |
| Fig. 7 | `Figure7-cultural-map.png` | Combination | 600 | 88mm (single) |
| Fig. 8 | `Figure8-mfq-profiles.png` | Line art | 600 | 180mm (double) |
| Fig. 9 | `Figure9-rlhf-taxonomy.png` | Combination | 600 | 180mm (double) |
| Fig. 10 | `Figure10-triple-bind.png` | Line art | 600 | 88mm (single) |
| S-Fig. 1 | `SFigure1-pipeline.png` | Line art | 600 | 180mm |
| S-Fig. 2 | `SFigure2-silhouette.png` | Line art | 600 | 88mm |
| S-Fig. 3 | `SFigure3-weird-histogram.png` | Line art | 600 | 180mm |
| S-Fig. 4 | `SFigure4-weird-radar.png` | Combination | 600 | 88mm |
| S-Fig. 5 | `SFigure5-north-south-radar.png` | Combination | 600 | 88mm |
| S-Fig. 6 | `SFigure6-nw-detection-bars.png` | Line art | 600 | 180mm |
| S-Fig. 7 | `SFigure7-bubble-world-map.png` | Halftone | 300 | 180mm |

All figures also output as PDF (vector) in same directory. TIFF deferred to submission.

---

## 2. Conflict Resolutions

| Conflict | Resolution | Rationale |
|----------|-----------|-----------|
| DPI: 300 vs 600 | 600 for line art, 300 for halftone (Figs 1, S7) | Expert 2 + Phase 2 critique aligned |
| Font: Helvetica vs Arial | Arial only (never plain Helvetica — .ttc breaks PDF) | Phase 2 confirmed Arial.ttf safe |
| Font fallback | `["Arial", "Helvetica Neue", "DejaVu Sans"]` | Phase 2 canonical recommendation |
| TIFF output | Defer to submission stage | Phase 2: unnecessary for polish pass |
| Fig 10 spiral icon | Drop — use text-box option only | Phase 2 wireframe review |
| Section 7.11 Limitations | NO — keep in 7.9 | Expert 3 + Phase 2 confirmed |
| Section 5.7 expansion | +100 words only (1 sentence/tradition) | Expert 3: preserve parallelism |
| MENA classification | Escalate to P0 — resolve as "Ambiguous" consistently | Phase 2 escalation |
| Effective N | Use placeholder "[N_eff]" until formalized; likely 3-4, not 5 | Phase 2 stats critique |
| RLHF counts | Use placeholder "[N_RLHF]" until computational reproduction | Confirmed arithmetic errors |
| Islamic *madhahib* | Add "across major schools" qualifier in 7.2 | Phase 2 anti-essentialization |

---

## 3. Agent Output Contracts

### 3.1 Figure Regeneration Agent
**Must produce:**
- `PAPER-V2/generate_figures_v2.py` — updated script for Figs 5-10
- `PAPER-V2/generate_legacy_figures_v2.py` — wrapper for legacy Figs 1-4, S1-S7
- All 17 PNG files with new names per canonical mapping (in `PAPER-V2/figures/` and `PAPER-V2/supplementary/supp-figures/`)
- All 17 PDF vector versions (same directories)
- Font verification output (print resolved font path)
**Must NOT:** change figure numbering or content; only visual/technical polish

### 3.2 Introduction Rewrite Agent
**Must produce:**
- `PAPER-V2/01-introduction.md` — rewritten introduction
**Must:** preserve substantive content; restructure 1.5 (RQs), 1.6 (contributions), 1.7 (roadmap); introduce "Triple Bind"; fix council size; use RLHF placeholder for conflict counts
**Must NOT:** edit any other PAPER-V2 files

### 3.6 Submission Components Agent
**Must produce:**
- `PAPER-V2/10-endmatter.md` — all 7 submission components
- `PAPER-V2/00-abstract-150w.md` — 150-word unstructured abstract
**Must NOT:** edit any other PAPER-V2 files

### 3.8 Computational Reproduction Agent
**Must produce:**
- `PAPER-V2/20260412-reproducibility-log.md` — verified counts from raw trial data
- Correct RLHF conflict total and per-category breakdown
- Correct per-model totals (Opus, Sonnet, Haiku)
- MFQ I:B ratio verification
- Pairwise correlation verification
**Must NOT:** edit any paper section files (outputs go to log only)

### 3.3 Text Copy Edit Agent (runs AFTER 3.2 + 3.8)
**Must produce:**
- In-place edits to all 16 section files in PAPER-V2/
- Fix RLHF counts per reproduction log
- Fix table numbering collisions
- Add missing citations to 09-references.md
- Resolve MENA classification
- Standardize terminology
**Must NOT:** expand content (that's 3.4's job)

### 3.4 Word Expansion Agent (runs AFTER 3.3)
**Must produce:**
- In-place edits to `05-results-trials.md`, `06-results-synthesis.md`, `07-discussion.md`
- Use approved prose from blueprint (with Phase 2 modifications applied)
**Must NOT:** edit other files; must use corrected RLHF counts from reproduction log

### 3.5 Statistical Formalization Agent (runs AFTER 3.8)
**Must produce:**
- Effective N formalization inserted into `05-results-trials.md` Section 5.6.4
- Power sensitivity table added to `supplementary/S2-results.md`
- Statistical Analysis subsection added to `02-methods.md`
**Must NOT:** change prose outside statistical content

### 3.7 Cross-Reference Reconciliation Agent (runs AFTER 3.1-3.5)
**Must produce:**
- Verification pass on all Fig/Table/Section references
- Fix any broken cross-references
- `PAPER-V2/20260412-polish-verification-report.md`
