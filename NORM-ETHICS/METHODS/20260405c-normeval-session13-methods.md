# Methods: NormEval Paper v2 — Journal Rewrite Pipeline

**Date:** 2026-04-05
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The rewrite drew on two authoritative data sources:
- **Dashboard data** (`DASHBOARD-v2/data.js`, 182 KB): 14 pre-computed JavaScript constants covering 54 benchmarks, 26 features, composite scores, tradition coverage, trial data, PCA clusters, temporal trends, correlation matrices, and anomaly detection
- **Cross-vendor data** (`DASHBOARD-v2/data_cross_vendor.js`, 16 KB): 8-model pairwise agreement matrix, IH/IB scaling, CBR rates, knowledge-judgment classification, and per-trial breakdowns across 114 comparable items
- **Council analysis** (`METHODS/20260404-cross-vendor-council-analysis.md`, 5,654 words): 12-member interdisciplinary panel deliberation with finding-by-finding votes, 3 formal dissents, and 10 consensus recommendations

The v1 paper (`PAPER/main-body-normeval.md`, 6,094 words) served as the expansion baseline.

## Procedure

### Phase 1: Planning and Infrastructure

A plan was designed using two parallel Plan agents: one for paper architecture (section structure, council composition, narrative arc) and one for figures/tables (chart types, data sources, color palettes, PDF generation). The output directory `PAPER-v2/` was created with `figures/`, `tables/`, and `supplement/` subdirectories. A spine contract (`spine-normeval-v2.md`) was written specifying the 12-member council composition, section assignments, updated terminology (including new terms: Ethical Profile, IH, IB, CBR, Knowledge-Judgment Divergence), figure/table numbering, and writing guidelines.

### Phase 2: Parallel Council Paper Writing

Six writing agents were dispatched in parallel, each responsible for 1-2 sections:
- Agent A: Abstract + Conclusion
- Agent B: Methods (3.1-3.7)
- Agent C: Results — Landscape (4.1-4.2)
- Agent D: Results — Trials + Cross-Vendor (4.3-4.6)
- Agent E: Discussion + Limitations (5.1-5.9, 6.1-6.2)
- Agent F: References

Each agent received the spine contract, its relevant source files, and explicit instructions to write in journal format with no length constraints. The council composition was embedded in each agent's brief with discipline-based labels (no fabricated expert names, per project convention).

### Phase 3: Supplementary Materials

Three additional agents were dispatched in parallel:
- Agent G: Appendices A-C (feature matrix, scoring methodology, T1-T5 item-level results)
- Agent H: Appendices D-G (T6-T15 cross-vendor results, excluded benchmarks, harness matrix, statistical methods)
- Agent I: Appendices H-J (care ethics prototype, v2 features, council deliberation summary)

### Phase 4: Figure Generation

A Python script (`PYTHON/generate_normeval_figures_v2.py`) was written to:
1. Parse the JavaScript data files by extracting `const DATA_*` blocks via regex and converting to Python dicts via `json.loads()`
2. Generate 11 publication-quality figures using matplotlib 3.9.4 and seaborn 0.13.2
3. Save each as both PNG (300 DPI raster) and PDF (vector)
4. Assemble a combined PDF using fpdf2 2.8.4

### Phase 5: Verification

Automated consistency checks were run:
- All 20 markdown files verified present with expected word counts
- Grep for stale "37 benchmark" references (1 legitimate historical reference found, 0 stale)
- All 8 main figure files confirmed present
- References section header updated from "Top 15" to "Top 24"

## Analysis

The paper rewrite expanded the original 5 claims (updated from n=37 to n=54) and added 7 cross-vendor findings (F1-F7). Statistical methods included binomial tests (C1, C3, C4), two-proportion z-tests with Cohen's h (C2), Mann-Whitney U (C5), pairwise agreement percentages with Clopper-Pearson 95% CIs, and Cohen's kappa for binary items.

The 12-member council framework assigned each finding to 2-4 lead perspectives, with all 12 contributing to the Discussion. Council votes were reported as N/12 tallies, and 3 formal dissents were preserved with full reasoning.

## Computational Environment

- Python 3.9 (`.venv/`)
- matplotlib 3.9.4, seaborn 0.13.2, numpy 2.0.2, fpdf2 2.8.4
- macOS Darwin 25.3.0
- Claude Opus 4.6 (1M context) with max effort, parallel agent orchestration

## Limitations and Decisions

1. **Introduction excluded:** Per user request, the comprehensive introduction was not rewritten. It still references n=37 in places.
2. **Figure S5 skipped:** Provider radar chart could not be generated due to `provider_profiles` data structure mismatch; 11 of 12 planned figures were produced.
3. **Agent rate limits:** Two agents (Discussion, References) encountered rate limits on first dispatch and were relaunched successfully.
4. **No LaTeX output:** The rewrite produced markdown + figures; LaTeX conversion is deferred to a future session.
5. **Council names:** Discipline-based labels used throughout per established project convention (no fabricated expert names).
