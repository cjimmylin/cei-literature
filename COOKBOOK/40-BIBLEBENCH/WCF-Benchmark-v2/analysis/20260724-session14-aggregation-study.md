# Session-14 Phase-3 Aggregation Study

Generated: 2026-07-24  |  Source: `20260724-session14-calibration-i2-results.json`  |  n_cells: 52

**Four rules:**
- **A** median-of-3 (status quo)
- **B** min-of-3
- **C** median over non-fabrication-flagged judges (fallback to median-of-3 if all flagged)
- **D** grounded-dissent min: min over non-flagged judges if >=1 clean; else fallback to median-of-3

**Fallback counts:** C = 39 cells, D = 39 cells (out of 52 total cells)

---

## Section 1 — Controls (qwen side)

Judges short: gemini = gemini-2.5-flash, deepseek = deepseek-chat, mistral = mistral-small-2603

| Item | Role | Expected | gemini | deepseek | mistral | Fab-flagged | A median-3 | B min-3 (supplier) | C med-nofab (fb) | D grnd-diss (fb, supplier) |
|------|------|----------|--------|----------|---------|------------|------------|-------------------|-----------------|--------------------------|
| LIB-N-006 | positive_control | ~83 (positive control) | 83 | 100 | 100 | deepseek | 100 | 83 (gemini) | 91.5  | 83  (gemini) |
| PROOF-N-009 | positive_control | ~83–91 (positive control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |
| MEND-N-002 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |
| MEND-N-009 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |
| PROOF-N-005 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini | 100 | 100 (gemini+deepseek+mistral) | 100  | 100  (deepseek+mistral) |
| WHOLE-N-004 | negative_control | 100 (negative control) | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 (gemini+deepseek+mistral) | 100 FALLBACK | 100 FALLBACK (n/a) |

---

## Section 2 — Tied-100 Sample (20 items): |qwen - haiku| gap per rule

| Rule | n_movers / 20 | Median gap (movers) | Max gap |
|------|--------------|--------------------|---------| 
| A_median3 | 1 | 25 | 25 |
| B_min3 | 5 | 25 | 92 |
| C_median_nofab | 2 | 39.8 | 62.5 |
| D_groundeddissent | 2 | 58.5 | 100 |

**A_median3 movers** (1):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| LIB-N-011 | 100 | 75 | 25 |

**B_min3 movers** (5):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| LIB-N-011 | 92 | 0 | 92 |
| WHOLE-N-002 | 40 | 100 | 60 |
| MEND-N-001 | 100 | 75 | 25 |
| WHOLE-N-007 | 100 | 83 | 17 |
| PROOF-N-003 | 100 | 92 | 8 |

**C_median_nofab movers** (2):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| LIB-N-011 | 100 | 37.5 | 62.5 |
| WHOLE-N-007 | 100 | 83 | 17 |

**D_groundeddissent movers** (2):

| Item | qwen | haiku | gap |
|------|------|-------|-----|
| LIB-N-011 | 100 | 0 | 100 |
| WHOLE-N-007 | 100 | 83 | 17 |

---

## Section 3 — Gate-Relevant Summary (all 26 items)

Count of items where |qwen_score - haiku_score| > 0 under each rule.

| Rule | Items with nonzero gap (of 26) |
|------|-------------------------------|
| A_median3 | 2 |
| B_min3 | 7 |
| C_median_nofab | 4 |
| D_groundeddissent | 4 |

---

## Section 4 — Instability Exposure (Rules B and D)

### 4a. Rule B (min-of-3): judge min-supplier tally across all cells

| Judge | Times supplied min (of 52 cells) |
|-------|----------------------------------|
| gemini | 48 |
| mistral | 47 |
| deepseek | 45 |

**Large-dissent cells (|min - median| > 25 pts): 2**

| Item | SUT | min | median | diff | supplier |
|------|-----|-----|--------|------|----------|
| LIB-N-011 | haiku | 0 | 75 | 75 | mistral |
| WHOLE-N-002 | qwen | 40 | 100 | 60 | deepseek |

### 4b. Rule D (grounded-dissent min): judge min-supplier tally

(Cells excluded from tally due to D-fallback: 39)

| Judge | Times supplied min (non-fallback cells) |
|-------|----------------------------------------|
| gemini | 10 |
| deepseek | 3 |
| mistral | 2 |

**Large-dissent cells (|min - median| > 25 pts): 1**

| Item | SUT | min | median | diff | supplier |
|------|-----|-----|--------|------|----------|
| LIB-N-011 | haiku | 0 | 75 | 75 | mistral |

---

## Full Panel Cell Scores

All 52 item×SUT cells.

| Item | SUT | Role | gemini | deepseek | mistral | Fab | A | B | C | D |
|------|-----|------|--------|----------|---------|-----|---|---|---|---|
| LIB-N-004 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-004 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-006 | haiku | positive_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-006 | qwen | positive_control | 83 | 100 | 100 | deepseek | 100 | 83 | 91.5 | 83 |
| LIB-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-008 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-008 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| LIB-N-010 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-010 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| LIB-N-011 | haiku | tied100_sample | 75 | 75 | 0 | deepseek | 75 | 0 | 37.5 | 0 |
| LIB-N-011 | qwen | tied100_sample | 92 | 100 | 100 | gemini+deepseek+mistral | 100 | 92 | 100* | 100* |
| MEND-N-001 | haiku | tied100_sample | 75 | 100 | 100 | gemini+deepseek+mistral | 100 | 75 | 100* | 100* |
| MEND-N-001 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-002 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-002 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-003 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-003 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-004 | haiku | tied100_sample | 100 | 100 | 100 | mistral | 100 | 100 | 100 | 100 |
| MEND-N-004 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-005 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-005 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| MEND-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-009 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| MEND-N-009 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-001 | haiku | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| PROOF-N-001 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| PROOF-N-003 | haiku | tied100_sample | 100 | 100 | 92 | gemini+deepseek+mistral | 100 | 92 | 100* | 100* |
| PROOF-N-003 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| PROOF-N-005 | haiku | negative_control | 100 | 100 | 100 | gemini+mistral | 100 | 100 | 100 | 100 |
| PROOF-N-005 | qwen | negative_control | 100 | 100 | 100 | gemini | 100 | 100 | 100 | 100 |
| PROOF-N-007 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-009 | haiku | positive_control | 82 | 82 | 64 | gemini+deepseek+mistral | 82 | 64 | 82* | 82* |
| PROOF-N-009 | qwen | positive_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-010 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-010 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-011 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| PROOF-N-011 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-002 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-002 | qwen | tied100_sample | 100 | 40 | 100 | gemini+deepseek+mistral | 100 | 40 | 100* | 100* |
| WHOLE-N-003 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-003 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-004 | haiku | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-004 | qwen | negative_control | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-006 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-006 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |
| WHOLE-N-007 | haiku | tied100_sample | 83 | 100 | 100 | deepseek+mistral | 100 | 83 | 83 | 83 |
| WHOLE-N-007 | qwen | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-008 | haiku | tied100_sample | 100 | 100 | 100 | gemini+deepseek+mistral | 100 | 100 | 100* | 100* |
| WHOLE-N-008 | qwen | tied100_sample | 100 | 100 | 100 | deepseek+mistral | 100 | 100 | 100 | 100 |

\* = fallback to median-of-3 (all judges fabrication-flagged on that cell)