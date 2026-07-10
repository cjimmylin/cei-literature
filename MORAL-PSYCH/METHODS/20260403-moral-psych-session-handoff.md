# Session Handoff: Moral Psychology Benchmarks Meta-Evaluation

**Date:** 2026-04-03
**Session scope:** Phase 1 (Council + Characterization + Top-15 Selection)
**Status:** Phase 1 COMPLETE. Phases 2-6 pending.

---

## What Was Accomplished

### 1. Candidate Extraction (222 papers)
- Scanned 2,046 vault papers using 5-signal detection (mp_* scores, benchmark flags, keyword matching, DATA_URL presence, known benchmark names)
- Multi-signal approach was essential: the keyword scorer missed major benchmarks like ValueBench (mp_schwartz=0 despite using 44 psychometric instruments) and ETHICS (Hendrycks, mp_mft=0)
- Script: `MORAL-PSYCH/extract_candidates.py`
- Output: `20260403-moral-psych-benchmark-candidates.json` (488K, 222 entries)

### 2. Expert Council Assessment (3 parallel agents)
- **Agent 1 (Depth):** Read PDF extracts for top 40 candidates. Assessed A2 (operationalization), A4 (source instrument), A5 (human baseline), A6 (construct validity), A7 (cultural provenance), A8 (languages), B1 (format), B2 (size), B10 (LLM fidelity), verified theories
  - Found 2 duplicate entries (TrolleyBench, Khandelwal DIT)
  - Corrected several vault mp_* misscores (e.g., Fraser 2022 scored Schwartz=100 but uses Schweder's Big Three, not Schwartz)
  - Output: `20260403-council-depth-assessment.json` (52K, 40 entries)

- **Agent 2 (Impact):** Cross-referenced with implementability CSV. Assessed safety relevance (1-5), harness tiers (B6), implementability scores (B7), scorer types (B8), model compatibility (B9), venue tiers (C3), hub presence (C5)
  - Mean implementability: 37/100 — most moral psych benchmarks need model-graded or psychometric scoring
  - 75% work with both open and closed models
  - Output: `20260403-council-impact-assessment.json` (28K, 40 entries)

- **Agent 3 (Secondary scan):** Assessed candidates 41-80, searched all 222 for underrepresented theories
  - Found 15 hidden gems with lower mp_* but high theoretical rigor
  - **Critical finding:** keyword scorer misses 85% of dual process papers and 97% of intuitionist papers
  - Output: `20260403-council-secondary-scan.json` (40K)

### 3. Citation Data (Semantic Scholar)
- Queried top 80 candidates via DOI or arXiv ID
- 54/80 found, 16 not found, 10 had no identifier
- Top cited: Moral Machine (1,478), Social Chemistry 101 (330), MFTC (198), Value Kaleidoscope (101)
- Output: `20260403-citation-counts.json` (28K)

### 4. Feature Matrix & Composite Scoring
- Merged all data sources into unified 28-feature matrix
- Scoring: PD×0.50 + PE×0.30 + CI×0.20 (psych-heavy weighting per user preference)
- 38 of 40 passed hard gates (PD>=40 + data available)
- Script: `MORAL-PSYCH/build_feature_matrix.py`
- Output: `20260403-moral-psych-benchmark-feature-matrix.json` (96K)

### 5. Top-15 Selection
- Applied theory caps (max 3 trolley, max 4 MFT) and diversity fills (min 2 Schwartz, min 1 Kohlberg, min 1 minority theory)
- Output: `20260403-moral-psych-top15-selection.json` (24K)
- Report: `20260403-moral-psych-top15-benchmark-selection.md` (24K)

---

## The Top 15

| # | Benchmark | Year | Theory | Format | Size | Composite |
|---|-----------|------|--------|--------|------|-----------|
| 1 | Moral Machine (Awad) | 2018 | Trolley | Forced-choice | 40M | 78.5 |
| 2 | Moral Machine on LLMs (Takemoto) | 2024 | Trolley | Forced-choice | 50K | 69.9 |
| 3 | Crowdsourcing Moral Machines (Awad) | 2020 | Trolley | Forced-choice | 40M | 69.9 |
| 4 | MFTC (Hoover) | 2020 | MFT | Multi-label | 35K | 68.1 |
| 5 | Does Moral Code... (Fraser) | 2022 | MFT+Schwartz | Binary+MCQ | 100 | 66.3 |
| 6 | Multilingual DIT (Khandelwal) | 2024 | Kohlberg | Scenario ranking | 54 | 66.0 |
| 7 | MFV (Clifford) | 2015 | MFT | Scenario rating | 132 | 64.5 |
| 8 | MFQ-30 on LLMs (Abdulhai) | 2024 | MFT | Likert | 30 | 63.8 |
| 9 | DIT on LLMs (Tanmay) | 2023 | Kohlberg | Scenario ranking | 9 | 63.2 |
| 10 | ValuePrism (Sorensen) | 2024 | Schwartz | Free-text+MCQ | 218K | 61.6 |
| 11 | Multilingual DIT-EACL (Khandelwal) | 2024 | Kohlberg | Scenario ranking | 54 | 61.2 |
| 12 | WVS on LLMs (Benkler) | 2023 | Schwartz | Free-text | 5 | 55.6 |
| 13 | Moral Identity (Xu & Ma) | 2016 | Identity | Likert+behavioral | 250 | 55.2 |
| 14 | CVC Chinese Values (Wu) | 2025 | Chinese norms | MCQ+generation | 250K | 52.8 |
| 15 | HRI Values (Abbo) | 2025 | Schwartz | Design tool | ? | 36.1 |

---

## Key Findings

### 1. Theory Coverage in the Field
- **MFT is dominant:** 68 of 222 candidates, 4 in top 15
- **Schwartz is broad but shallow:** 52 candidates but most are theory-inspired (A2=2), not using the validated PVQ-40
- **Kohlberg is strong via DIT:** Only instrument with 40+ years of human norms
- **3 theories have near-zero dedicated LLM benchmarks:** Dual Process, Social Intuitionism, Dyadic Morality

### 2. Keyword Scorer Blind Spots
The vault's `moral_psych_scoring.py` severely undercounts underrepresented theories:
- Dual Process: 85% miss rate (2 found vs 13 actual)
- Social Intuitionist: 97% miss rate (1 found vs 35 actual)
- Dyadic: 63% miss rate
- Moral Identity: 50% miss rate

### 3. Format Distribution
- Forced-choice and MCQ are easiest for LLMs (3 of top 15)
- Likert scales are common but problematic (LLMs may not use full scale range)
- Scenario rating + ranking (DIT) requires multi-step reasoning
- Free-text benchmarks need model-graded scoring (Inspect AI preferred)

### 4. Hidden Gems from Secondary Scan
15 papers ranked 41-80 that deserve deeper assessment:
- **Bago 2022:** 45-country dual process replication (gold-standard human baseline)
- **Staircase of Ethics (Wu 2025):** First multi-step escalating benchmark (16,510 decisions)
- **UniMoral (Kumar 2025):** 4-theory, 6-language dataset
- **Value-Spectrum (Li 2024):** Multimodal video VQA on Schwartz values (50K+ videos)
- **ValAct-15k (2026):** Tests knowledge-action gap (15K items, 10 frontier LLMs)

---

## User Decisions (Binding for Future Sessions)

1. **Scope:** Tiered approach — benchmarks and datasets scored separately, then merged. Datasets get B10 penalty.
2. **Goal:** Both academic paper AND dashboard.
3. **Models:** Claude-only first to validate pipeline, expand to GPT-4o/Llama-3 later.
4. **Weighting:** 50/30/20 (Psychological Depth / Practical Ease / Citation Impact).
5. **Output directory:** All files in `CEI-Lit-WS/MORAL-PSYCH/` with subdirectories.
6. **Independence:** This is a standalone project. Do NOT compare with or reference the normative ethics project.

---

## What Remains (Phases 2-6)

### Phase 2: Gap Analysis (Sessions 2-3)
- **External search:** 10 query sets across 7 databases (Semantic Scholar, arXiv, ACL Anthology, PsycINFO, Google Scholar, HuggingFace, PapersWithCode)
- **Focus:** Dual Process, Dyadic Morality, Social Intuitionism — the 3 underrepresented theories
- **Hidden gem deep assessment:** Run full depth assessment on the 15 gems from the secondary scan
- **Keyword scorer fix:** Update `moral_psych_scoring.py` with expanded patterns (dual process: "utilitarian vs deontological", "cognitive load"; intuitionist: "intuitive judgment", "post-hoc rationalization", "gut feeling"; etc.)
- Ingest qualifying new papers into vault

### Phase 3: Revised Top-15 (Session 4)
- Re-score with expanded candidate pool (post gap analysis)
- Potentially revise top 15 with hidden gems and external finds
- #15 (Abbo HRI) is the weakest entry and most likely to be replaced

### Phase 4: Implementation Trials (Sessions 5-7)
- 5 benchmarks, ~150 total items, Claude Opus/Sonnet
- Recommended 5: Moral Machine (#2), MFTC (#4), MFQ-30 (#8), DIT (#6), ValuePrism (#10)
- For each: download data, format prompts, run evaluation, score responses, compare to human baselines
- Output: `MORAL-PSYCH/YYYYMMDD-trial-MP{1-5}-*.md`

### Phase 5: Dashboard (Sessions 8-9)
- Interactive dashboard with:
  - Benchmark comparison table (all 28 features sortable)
  - Theory coverage heatmap (8 theories × 15 benchmarks)
  - Implementation readiness tracker (5 harnesses)
  - Trial results visualization (Claude responses vs human baselines)
- Location: `MORAL-PSYCH/DASHBOARDS/`
- Architecture: fat-data thin-client (Python generator → data.js → ECharts)

### Phase 6: Academic Paper (Sessions 10-13)
- Working title: "Mapping the Moral Mind of Machines: A Meta-Evaluation of Moral Psychology Benchmarks for LLM Assessment"
- Target: ACL/EMNLP 2026 (Datasets & Benchmarks track)
- Key claims:
  1. MFT dominance: field heavily skewed toward Moral Foundations Theory
  2. Construct validity gap: most benchmarks adapt instruments without revalidation for LLMs
  3. Missing theories: Dual Process, Social Intuitionism, Dyadic Morality have no dedicated benchmarks
  4. Human baseline deficit: most benchmarks lack published comparison data
  5. Format mismatch: psychology instruments designed for humans often need substantial modification for LLMs
- Location: `MORAL-PSYCH/PAPER/`

---

## File Inventory

```
MORAL-PSYCH/
├── 20260403-moral-psych-benchmark-candidates.json     # 222 candidates (488K)
├── 20260403-council-depth-assessment.json              # Depth assessment, 40 papers (52K)
├── 20260403-council-impact-assessment.json             # Impact assessment, 40 papers (28K)
├── 20260403-council-secondary-scan.json                # Secondary scan + hidden gems (40K)
├── 20260403-citation-counts.json                       # Semantic Scholar citations (28K)
├── 20260403-moral-psych-benchmark-feature-matrix.json  # 28-feature matrix (96K)
├── 20260403-moral-psych-top15-selection.json           # Final selection JSON (24K)
├── 20260403-moral-psych-top15-benchmark-selection.md   # Full report with addendum (24K)
├── extract_candidates.py                               # Candidate extraction script (16K)
├── build_feature_matrix.py                             # Scoring & matrix builder (16K)
├── METHODS/
│   ├── 20260403-moral-psych-benchmark-selection-methods.md  # Reproducibility docs (8K)
│   └── 20260403-moral-psych-session-handoff.md              # This file
├── DASHBOARDS/                                         # (empty — Phase 5)
├── PAPER/                                              # (empty — Phase 6)
└── STATISTICS/                                         # (empty — future reports)
```

## Critical Dependencies for Next Session

1. **Implementability CSV:** `CEI-Lit-WS/STATISTICS/20260313-implementability-cross-framework-table-v2.csv` — base harness data for Tier B scoring
2. **Keyword scorer:** `CEI-Lit-WS/PYTHON/moral_psych_scoring.py` — needs pattern expansion for underrepresented theories
3. **Eval dashboard v4:** `CEI-Lit-WS/DASHBOARDS/20260329-eval-framework-dashboard-v4.html` — Tab 4 has existing moral psych overlay
4. **PDF extracts:** `CEI-Lit-WS/PDF Extracts/YYYY/` — needed for full-text feature extraction on hidden gems
5. **Python env:** `../.venv/bin/python` — all scripts use this venv

## Memory to Preserve

- This project is standalone — do NOT reference the normative ethics project
- User prefers 50/30/20 weighting (psych-heavy) — construct validity matters more than ease of implementation
- User wants Claude-only trials first, expand to other models later
- All outputs go in `CEI-Lit-WS/MORAL-PSYCH/` — not in STATISTICS/ or other vault locations
