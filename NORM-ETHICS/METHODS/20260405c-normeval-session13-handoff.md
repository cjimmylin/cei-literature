# NormEval Paper v2 — Session 13 Handoff

**Date:** 2026-04-05
**Session:** Full journal rewrite — 12-expert council, all sections except introduction
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260405b-normeval-session12-handoff.md`

---

## What Was Done This Session

### Paper Rewrite: PAPER-v2/ Created

Produced a comprehensive journal-length rewrite of the NormEval paper, expanding from the 6,094-word NeurIPS draft to a 64,724-word journal manuscript with supplementary materials.

**New title:** "Three Ethical Profiles, One Knowledge Ceiling: A Meta-Evaluation of 54 Normative Ethics Benchmarks Across Nine LLMs and Three Vendors"

### 12-Member Expert Council

Convened a council with 12 discipline-based perspectives (RLHF, Moral Psychology, Psychometrics, ML Systems, Kantian Ethics, Consequentialist Ethics, AI Policy, Benchmark Security, Cross-Cultural Psychology, Biostatistics, Educational Measurement/IRT, Science Communication). Each perspective was assigned primary section ownership.

### Main Body Sections (10 files, ~21,000 words excluding intro)

| File | Words | Sections |
|------|-------|----------|
| `abstract-normeval-v2.md` | 572 | Abstract |
| `methods-normeval-v2.md` | 3,503 | 3.1-3.7 (expanded from 1,049w) |
| `results-landscape-normeval-v2.md` | 3,407 | 4.1-4.2 (landscape + Top 24) |
| `results-trials-normeval-v2.md` | 1,440 | 4.3-4.4 (trials + discriminative analysis) |
| `results-crossvendor-normeval-v2.md` | 3,418 | 4.5-4.6 (NEW — central contribution, 7 findings) |
| `discussion-normeval-v2.md` | 5,921 | 5.1-5.9 (expanded from 1,753w) |
| `limitations-normeval-v2.md` | 1,113 | 6.1-6.2 (NEW — separated from methods) |
| `conclusion-normeval-v2.md` | 1,639 | 7.1-7.3 (5 calls to action, up from 3) |
| `references-normeval-v2.md` | 5,054 | 179 entries in 17 thematic sections |
| `spine-normeval-v2.md` | 1,615 | Structure contract with council assignments |

### Supplementary Materials (10 files, ~37,000 words)

| File | Words | Content |
|------|-------|---------|
| `appendix-A-feature-matrix.md` | 5,427 | Complete 54×26 feature matrix (Table S1) |
| `appendix-B-scoring-methodology.md` | 3,448 | Scoring formulas, calibration, sensitivity (Table S2) |
| `appendix-C-trials-T1-T5.md` | 5,047 | Item-level single-model results (Tables S3-S7) |
| `appendix-D-trials-T6-T15.md` | 6,550 | Item-level cross-vendor results, 9 models (Tables S8-S17) |
| `appendix-E-excluded-benchmarks.md` | 1,600 | 30 excluded benchmarks with reasons (Table S18) |
| `appendix-F-harness-matrix.md` | 2,052 | 54×6 harness compatibility (Table S19) |
| `appendix-G-statistical-methods.md` | 2,719 | Hypothesis tests, CIs, power analysis (Tables S20-S21) |
| `appendix-H-care-ethics-prototype.md` | 4,003 | Tronto 4-dimension prototype, 3 scenarios (Table S22) |
| `appendix-I-v2-features.md` | 2,479 | 18 new v2 features (Figures S1-S2) |
| `appendix-J-council-deliberation.md` | 3,717 | Council votes, dissents, 10 recommendations |

### Figures and Tables

- **11 publication-quality figures** generated via matplotlib/seaborn (8 main + 3 supplementary)
  - PNG (300 DPI) and PDF (vector) for each
  - Colorblind-safe academic palette, serif fonts
- **1 combined PDF** (`normeval-figures-tables-v2.pdf`, 1.8 MB) with title page + all figures
- **Figure generation script:** `PYTHON/generate_normeval_figures_v2.py`
  - Parses `data.js` and `data_cross_vendor.js` directly
  - All 14 data constants loaded from dashboard

### Key New Content (Not in v1)

- **Section 4.5-4.6:** Cross-model and cross-vendor analysis (7 findings: F1-F7)
- **Section 5.3:** Three Ethical Profiles taxonomy (Conservative/Moderate/Permissive)
- **Section 5.4:** Knowledge-Judgment Divergence (IRT + dual-process)
- **Section 5.6:** Gemini Identity Finding (responsible disclosure framing)
- **Section 5.9:** Western Bias and Cultural Contingency
- **Section 3.5:** Statistical Methods (NEW)
- **Section 3.6:** Care Ethics Benchmark Prototype (NEW)
- **Appendix H:** Full care ethics prototype with 3 worked scenarios
- **Appendix J:** Full council deliberation summary with votes and dissents

---

## Remaining Work

### Priority 1: Introduction update
The introduction was excluded from this rewrite. It needs:
- Update n=37→54 references
- Add paragraph previewing cross-vendor findings and three ethical profiles
- Update venue framing from NeurIPS to general journal

### Priority 2: LaTeX conversion
NeurIPS 2026 template or chosen journal format. The markdown is journal-ready but needs typesetting.

### Priority 3: Cross-reference audit
Run automated check that every `Figure N` / `Table N` / `Section N.N` reference in text has a corresponding file/section.

### Priority 4: Figure S5 (Provider Radar)
Skipped due to data structure mismatch in `provider_profiles`. Needs manual data extraction or alternate chart type.

### Priority 5: Temperature sensitivity test
Test Gemini models at non-zero temperature to disambiguate shared infrastructure vs. deterministic decoding.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| All v2 paper files | `NORM-ETHICS/PAPER-v2/` | Main body + spine |
| All supplement files | `NORM-ETHICS/PAPER-v2/supplement/` | Appendices A-J |
| All figures | `NORM-ETHICS/PAPER-v2/figures/` | 11 PNG + 11 PDF |
| Combined PDF | `NORM-ETHICS/PAPER-v2/normeval-figures-tables-v2.pdf` | 1.8 MB, all figures |
| Figure script | `NORM-ETHICS/PYTHON/generate_normeval_figures_v2.py` | Regenerates all figures |
| Dashboard data (source) | `NORM-ETHICS/DASHBOARD-v2/data.js` | 182KB, 14 constants |
| Cross-vendor data (source) | `NORM-ETHICS/DASHBOARD-v2/data_cross_vendor.js` | 16KB |
| v1 paper (preserved) | `NORM-ETHICS/PAPER/` | Original NeurIPS draft |
| Dashboard v2 (live) | https://cjimmylin.github.io/cei-normeval-dashboard-v2/ | Interactive |

## Known Issues

1. **Figure S5 (Provider Radar)** skipped — `provider_profiles` data structure in `data_cross_vendor.js` doesn't match expected format. Minor; can be generated manually.
2. **Introduction not updated** — still references n=37 in places. Deliberately excluded per user request.
3. **fpdf2 deprecation warnings** — `ln=True` parameter deprecated in v2.5.2. Cosmetic only; output is correct.

---

*Filed: 2026-04-05 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
