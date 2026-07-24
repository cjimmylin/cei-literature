# Session-14 Phase-3 Aggregation Study

Generated: 2026-07-24  |  Source: `20260724-session14-calibration-i3-results.json`  |  n_cells: 52

**Four rules:**
- **A** median-of-3 (status quo)
- **B** min-of-3
- **C** median over non-fabrication-flagged judges (fallback to median-of-3 if all flagged)
- **D** grounded-dissent min: min over non-flagged judges if >=1 clean; else fallback to median-of-3

**Fallback counts:** C = 31 cells, D = 31 cells (out of 52 total cells)

---

## Section 1 — Controls (qwen side)

Judges short: gemini = gemini-2.5-flash, deepseek = deepseek-chat, mistral = mistral-small-2603

| Item | Role | Expected | gemini | deepseek | mistral | Fab-flagged | A median-3 | B min-3 (supplier) | C med-nofab (fb) | D grnd-diss (fb, supplier) |
|------|------|----------|--------|----------|---------|------------|------------|-------------------|-----------------|--------------------------|
| LIB-N-006 | positive_control | ~83 (positive control) | 100 | 100 | 100 | deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100  | 100  (gemini) |
| PROOF-N-009 | positive_control | ~83–91 (positive control) | 10 | 64 | 9 | gemini+deepseek+mistral | 10 | 9 (mistral) | 10 FALLBACK | 10 FALLBACK (n/a) |
| MEND-N-002 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+mistral | 100 | 100 (gemini+deepseek+mistral) | 100  | 100  (deepseek) |
| MEND-N-009 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |
| PROOF-N-005 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |
| WHOLE-N-004 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |

---

## Section 2 — Tied-100 Sample (20 items): |qwen - haiku| gap per rule

| Rule | n_movers / 20 | Median gap (movers) | Max gap |
|------|--------------|--------------------|---------| 
| A_median3 | 4 | 92 | 92 |
| B_min3 | 11 | 90 | 100 |
| C_median_nofab | 8 | 91.5 | 96 |
| D_groundeddissent | 8 | 91.5 | 100 |

**A_median3 movers** (4):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| LIB-N-004 | 100 | 8 | 92 |
| LIB-N-010 | 100 | 8 | 92 |
| WHOLE-N-003 | 100 | 8 | 92 |
| WHOLE-N-007 | 100 | 8 | 92 |

**B_min3 movers** (11):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| WHOLE-N-003 | 100 | 0 | 100 |
| LIB-N-004 | 100 | 8 | 92 |
| LIB-N-010 | 100 | 8 | 92 |
| WHOLE-N-008 | 100 | 8 | 92 |
| PROOF-N-010 | 9 | 100 | 91 |
| PROOF-N-001 | 10 | 100 | 90 |
| MEND-N-001 | 100 | 77 | 23 |
| LIB-N-008 | 92 | 100 | 8 |
| PROOF-N-011 | 93 | 100 | 7 |
| LIB-N-007 | 94 | 100 | 6 |
| WHOLE-N-007 | 7 | 8 | 1 |

**C_median_nofab movers** (8):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| WHOLE-N-003 | 100 | 4 | 96 |
| LIB-N-004 | 100 | 8 | 92 |
| LIB-N-010 | 100 | 8 | 92 |
| WHOLE-N-008 | 100 | 8 | 92 |
| PROOF-N-010 | 9 | 100 | 91 |
| PROOF-N-001 | 55 | 100 | 45 |
| LIB-N-008 | 92 | 100 | 8 |
| WHOLE-N-007 | 7 | 8 | 1 |

**D_groundeddissent movers** (8):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| WHOLE-N-003 | 100 | 0 | 100 |
| LIB-N-004 | 100 | 8 | 92 |
| LIB-N-010 | 100 | 8 | 92 |
| WHOLE-N-008 | 100 | 8 | 92 |
| PROOF-N-010 | 9 | 100 | 91 |
| PROOF-N-001 | 10 | 100 | 90 |
| LIB-N-008 | 92 | 100 | 8 |
| WHOLE-N-007 | 7 | 8 | 1 |

---

## Section 3 — Gate-Relevant Summary (all 26 items)

Count of items where |qwen_score - haiku_score| > 0 under each rule.

| Rule | Items with nonzero gap (of 26) |
|------|-------------------------------|
| A_median3 | 6 |
| B_min3 | 12 |
| C_median_nofab | 10 |
| D_groundeddissent | 10 |

---

## Section 4 — Instability Exposure (Rules B and D)

### 4a. Rule B (min-of-3): judge min-supplier tally across all cells

| Judge | Times supplied min (of 52 cells) |
|-------|----------------------------------|
| mistral | 47 |
| gemini | 42 |
| deepseek | 40 |

**Large-dissent cells (|min - median| > 25 pts): 5**

| Item | SUT | min | median | diff | supplier |
|------|-----|-----|--------|------|----------|
| WHOLE-N-007 | qwen | 7 | 100 | 93 | mistral |
| WHOLE-N-008 | haiku | 8 | 100 | 92 | mistral |
| PROOF-N-010 | qwen | 9 | 100 | 91 | gemini |
| PROOF-N-001 | qwen | 10 | 100 | 90 | deepseek |
| LIB-N-006 | haiku | 8 | 71 | 63 | gemini |

### 4b. Rule D (grounded-dissent min): judge min-supplier tally

(Cells excluded from tally due to D-fallback: 31)

| Judge | Times supplied min (non-fallback cells) |
|-------|----------------------------------------|
| gemini | 10 |
| mistral | 9 |
| deepseek | 7 |

**Large-dissent cells (|min - median| > 25 pts): 5**

| Item | SUT | min | median | diff | supplier |
|------|-----|-----|--------|------|----------|
| WHOLE-N-007 | qwen | 7 | 100 | 93 | mistral |
| WHOLE-N-008 | haiku | 8 | 100 | 92 | mistral |
| PROOF-N-010 | qwen | 9 | 100 | 91 | gemini |
| PROOF-N-001 | qwen | 10 | 100 | 90 | deepseek |
| LIB-N-006 | haiku | 8 | 71 | 63 | gemini |

---

## Full Panel Cell Scores

All 52 item×SUT cells.

| Item | SUT | Role | gemini | deepseek | mistral | Fab | A | B | C | D |
|------|-----|------|--------|----------|---------|-----|---|---|---|---|
| LIB-N-004 | haiku | tied100_sample | 100 | 8 | 8 | gemini | 8 | 8 | 8 | 8 |
| LIB-N-004 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-006 | haiku | positive_control | 8 | 92 | 71 | deepseek+mistral | 71 | 8 | 8 | 8 |
| LIB-N-006 | qwen | positive_control | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| LIB-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-007 | qwen | tied100_sample | 100 | 100 | 94 | gemini+deepseek+mistral | 100 | 94 | 100* | 100* |
| LIB-N-008 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-008 | qwen | tied100_sample | 92 | 100 | 100 | deepseek+mistral | 100 | 92 | 92 | 92 |
| LIB-N-010 | haiku | tied100_sample | 100 | 8 | 8 | gemini+deepseek | 8 | 8 | 8 | 8 |
| LIB-N-010 | qwen | tied100_sample | 100 | 100 | 100 | gemini+mistral | 100 | 100 | 100 | 100 |
| LIB-N-011 | haiku | tied100_sample | 75 | 8 | 8 | gemini | 8 | 8 | 8 | 8 |
| LIB-N-011 | qwen | tied100_sample | 8 | 9 | 8 | gemini+deepseek | 8 | 8 | 8 | 8 |
| MEND-N-001 | haiku | tied100_sample | 77 | 100 | 100 | gemini+deepseek+mistral | 100 | 77 | 100* | 100* |
| MEND-N-001 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-002 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-002 | qwen | negative_control | 100 | 100 | 100 | gemini+mistral | 100 | 100 | 100 | 100 |
| MEND-N-003 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-003 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| MEND-N-004 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-004 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-005 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-005 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| MEND-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-009 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-009 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-001 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-001 | qwen | tied100_sample | 100 | 10 | 100 | mistral | 100 | 10 | 55 | 10 |
| PROOF-N-003 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-003 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-005 | haiku | negative_control | 100 | 100 | 100 | gemini+mistral | 100 | 100 | 100 | 100 |
| PROOF-N-005 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-009 | haiku | positive_control | 9 | 10 | 9 | — | 9 | 9 | 9 | 9 |
| PROOF-N-009 | qwen | positive_control | 10 | 64 | 9 | gemini+deepseek+mistral | 10 | 9 | 10* | 10* |
| PROOF-N-010 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-010 | qwen | tied100_sample | 9 | 100 | 100 | deepseek+mistral | 100 | 9 | 9 | 9 |
| PROOF-N-011 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-011 | qwen | tied100_sample | 100 | 100 | 93 | gemini+deepseek+mistral | 100 | 93 | 100* | 100* |
| WHOLE-N-002 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-002 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-003 | haiku | tied100_sample | 8 | 10 | 0 | deepseek | 8 | 0 | 4 | 0 |
| WHOLE-N-003 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-004 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-004 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-006 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-006 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| WHOLE-N-007 | haiku | tied100_sample | 8 | 8 | 8 | — | 8 | 8 | 8 | 8 |
| WHOLE-N-007 | qwen | tied100_sample | 100 | 100 | 7 | gemini+deepseek | 100 | 7 | 7 | 7 |
| WHOLE-N-008 | haiku | tied100_sample | 100 | 100 | 8 | gemini+deepseek | 100 | 8 | 8 | 8 |
| WHOLE-N-008 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |

\* = fallback to median-of-3 (all judges fabrication-flagged on that cell)