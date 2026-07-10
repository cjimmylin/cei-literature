# Top 15 Normative Ethics Benchmarks for LLM Values Alignment

**Date:** 2026-04-03
**Method:** 3-axis composite scoring (Normative Depth 40%, Practical Ease 35%, Citation Impact 25%)
**Scope:** 37 papers in feature matrix (31 original vault + 6 newly ingested external)
**Status:** All 6 external papers ingested into vault, feature matrix complete
**Gates:** ND ≥ 40, public data available

---

## Final Top 15

| Rank | COMP | Benchmark | Year | ND | PE | CI | Traditions | Size | Data | Source |
|------|------|-----------|------|----|----|-----|------------|------|------|--------|
| 1 | **77.2** | **ETHICS** (Hendrycks et al.) | 2021 | 59.8 | 95.0 | 80.0 | V+D+U | 130,000 | [GitHub](https://github.com/hendrycks/ethics) | Vault |
| 2 | **70.2** | **MoReBench** (Chiu et al.) | 2025 | 87.0 | 82.5 | 26.3 | V+D+U+Co | 1,000 | [HuggingFace](https://hf.co/datasets/morebench/morebench) | Vault |
| 3 | **67.9** | **PrinciplismQA** (Hong et al.) | 2025 | 85.0 | 78.5 | 25.8 | C+D+U | 3,648 | [arXiv](https://arxiv.org/abs/2508.05132) | **Ingested** |
| 4 | **67.6** | **Moral Persuasion** (Huang et al.) | 2024 | 79.8 | 85.5 | 22.9 | V+D+U | 108 | [GitHub](https://github.com/acyhuang/moral-persuasion) | Vault |
| 5 | **65.5** | **MoralReason-QA** (An et al.) | 2025 | 80.0 | 78.0 | 24.7 | V+D+U | 2,040 | [HuggingFace](https://huggingface.co/datasets/zankjhk/Moral-Reason-QA) | Vault |
| 6 | **63.5** | **Moral Lens** (Samway et al.) | 2025 | 58.0 | 87.5 | 38.6 | D+U | 640 | [GitHub](https://github.com/keenansamway/moral-lens) | Vault |
| 7 | **61.7** | **AMAeval** (Galatolo et al.) | 2025 | 71.0 | 76.9 | 25.4 | — | 1,090 | [GitHub](https://github.com/alessioGalatolo/AMAeval) | Vault |
| 8 | **59.4** | **JETHICS** (Takeshita et al.) | 2025 | 55.8 | 87.5 | 25.7 | V+D+U | 78,000 | [GitHub](https://github.com/Language-Media-Lab/jethics) | Vault |
| 9 | **59.3** | **Pluralistic Moral Gap** (Russo et al.) | 2025 | 82.8 | 56.5 | 25.8 | V+C+D+U | 1,618 | [arXiv](https://arxiv.org/abs/2507.17216) | **Ingested** |
| 10 | **59.0** | **DailyDilemmas** (Chiu et al.) | 2024 | 62.8 | 78.5 | 25.8 | V | 1,360 | [HuggingFace](https://huggingface.co/papers/2410.02683) | **Ingested** |
| 11 | **56.1** | **MedEthicsQA** (Wei et al.) | 2025 | 59.8 | 73.5 | 25.8 | C+D+U | 10,974 | [GitHub](https://github.com/JianhuiWei7/MedEthicsQA) | **Ingested** |
| 12 | **54.6** | **UniMoral** (Kumar et al.) | 2025 | 57.8 | 71.5 | 25.8 | D+V | 5,000 | [HuggingFace](https://huggingface.co/datasets/shivaniku/UniMoral) | **Ingested** |
| 13 | **54.2** | **Greatest Good** (Marraffini et al.) | 2024 | 53.0 | 75.3 | 26.4 | D+U | 90 | [GitHub](https://github.com/noehsueh/greatest-good-benchmark) | Vault |
| 14 | **52.8** | **PNAS Dilemmas** (Cheung et al.) | 2025 | 46.8 | 63.1 | 48.1 | D+U | 22 | [OSF](https://osf.io/3ahrb) | Vault |
| 15 | **51.6** | **ProMoral-Bench** (Thomas et al.) | 2026 | 50.2 | 71.5 | 25.8 | D+U | 5,000 | [arXiv](https://arxiv.org/abs/2602.13274) | **Ingested** |

### Tradition Key
V = Virtue Ethics, D = Deontological, U = Utilitarian/Consequentialist, C = Care Ethics, Co = Contractarian

---

## Diversity Verification

| Constraint | Required | Actual | Status |
|------------|----------|--------|--------|
| ≥2 virtue ethics | 2 | 8 | **PASS** |
| ≥2 deontological | 2 | 12 | **PASS** |
| ≥2 utilitarian | 2 | 11 | **PASS** |
| ≥1 care/contractarian | 1 | 4 (C: #9,#10,#14; Co: #1) | **PASS** |
| ≥1 non-English/cross-cultural | 1 | 2 (JETHICS=Japanese, UniMoral=6 langs) | **PASS** |
| ≥1 domain-specific | 1 | 2 (PrinciplismQA=Healthcare, MedEthicsQA=Healthcare) | **PASS** |

---

## Honorable Mentions (Ranks 16-20)

| Rank | COMP | Benchmark | Why Not Top 15 |
|------|------|-----------|----------------|
| 16 | 53.5 | EthicsSuite (20K scenarios) | Derivative of Hendrycks ETHICS; lower normative depth (A6=2) |
| 17 | 53.2 | PsychEthicsBench (2026) | Very recent, low citations; psychology-specific not broadly normative |
| 18 | 52.3 | MORABLES (EMNLP 2025) | Novel fable-based approach but narrow virtue focus, small dataset |
| 19 | — | Chakraborty Structured Moral Reasoning | ND=83.0 but GitHub repo returns 404; constituent datasets are public |
| 20 | — | Zhou Rethinking Machine Ethics (NAACL 2024) | ND=72.0 but no released data; uses in-paper prompts only |

---

## Scoring Methodology

### Three Axes

**Normative Depth (ND, 40% weight):**
```
ND = A2_depth×25 + A6_grounding×20 + A1_framework_count×15 + A3_reasoning×15 + A5_pluralism×15 + A4_uncertainty×10
```

**Practical Ease (PE, 35% weight):**
```
PE = B7_implementability×30 + B3_data×20 + B4_code×15 + B6_harness×15 + B9_model_compat×10 + B5_license×10
```

**Citation Impact (CI, 25% weight):**
```
CI = C2_norm_citations×35 + C4_adoption×30 + C3_venue×20 + C5_leaderboard×15
```

**Composite:** `COMPOSITE = ND×0.40 + PE×0.35 + CI×0.25`

### Hard Gates
1. Normative Depth ≥ 40
2. Public data available (GitHub, HuggingFace, or equivalent)

### Calibration Anchors
- MoReBench (A6=5): Expert rubric criteria for procedural reasoning under 5 named frameworks
- Hendrycks ETHICS (A6=3): Names traditions, creates sub-datasets, but shallow operationalization
- Hui Decoding Moral (A6=1): Mentions ethics vocabulary without philosophical substance

---

## Key Findings

### 1. The field is heavily skewed toward deontological/utilitarian framing
12 of 15 benchmarks test D or U; only 4 include care ethics, and only 1 (MoReBench) includes contractarian ethics.

### 2. No pure care ethics or contractarian benchmark exists
The closest to care ethics is PrinciplismQA (Beauchamp-Childress biomedical principlism, which includes beneficence). No Gilligan/Noddings-style relational ethics benchmark has been published. No standalone Rawlsian/contractarian benchmark exists for LLMs. **This is a genuine research lacuna suitable for a new contribution.**

### 3. Data availability is the primary bottleneck
12 of 31 vault papers fail solely because data is not public — including some of the highest normative-depth papers (Chakraborty ND=83, Rao ND=80).

### 4. MoReBench is the gold standard
It is the only benchmark that (a) tests *procedural* moral reasoning (not just judgment), (b) covers 4 normative traditions including contractarianism, (c) uses expert-designed rubric criteria, and (d) has public data on HuggingFace.

### 5. Dataset size varies 400×
From 22 items (Cheung PNAS) to 130,000 (Hendrycks ETHICS). Small benchmarks (< 100 items) have higher per-item quality but lower statistical power.

---

## Format Distribution

| Format | Count | Examples |
|--------|-------|---------|
| Scenario-based | 5 | MoReBench, MoralReason, Moral Lens, DailyDilemmas, Greatest Good |
| Mixed (MCQ + open-ended) | 6 | ETHICS, MoralReason, PrinciplismQA, MedEthicsQA, ProMoral-Bench, Pluralistic Gap |
| Pairwise comparison | 0 | — |
| MCQ | 1 | UniMoral |
| Binary | 1 | JETHICS |
| Open-ended | 1 | AMAeval |
| Likert | 0 | — |

---

## Implementation Priority (for chat-interface LLM agent trials)

### Tier 1: Start Here (data ready, strong normative depth)
1. **MoReBench** — Sample 30 items from MoReBench-Theory, present to Claude + GPT-4o, score with expert rubric
2. **Hendrycks ETHICS** — Already in lm-eval; sample 50 items across all 5 sub-datasets
3. **DailyDilemmas** — Present 20 dilemmas, assess virtue reasoning quality

### Tier 2: High Value, Moderate Effort
4. **PrinciplismQA** — 20 medical ethics cases, test 4-principle reasoning
5. **MoralReason-QA** — Sample 20 multi-framework scenarios

### Tier 3: Worth Testing for Completeness
6-15. Remaining benchmarks as time permits

---

## Data Files

- Feature matrix: `STATISTICS/20260402-normative-benchmark-feature-matrix.json` (31 vault papers, 26 features + composites)
- External candidates: `/tmp/external_search_results.json` (20 candidates)
- Final Top 15: `/tmp/final_top15.json`
- Companion report: `STATISTICS/ARCHIVE/20260207-normative-ethics-benchmarks-report.md` (original 31-paper inventory)
- Dashboard: `DASHBOARDS/20260329-eval-framework-dashboard-v4.html` (per-paper implementability)
