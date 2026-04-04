# Session Handoff: Religious Values Paper — Session 6 (Analytical Deepening)

**Date:** 2026-04-04
**Project:** Religious Values Benchmark Paper — "What Do Religious Values Benchmarks Actually Test?"
**Location:** `CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/`
**Prior Handoff:** `20260404-paper-session5-handoff.md` (Session 5: enrichment, tables, figures, trials, council D-03)
**Status:** Comprehensive analysis session with 12-member expert council. Sensitivity analysis reveals rankings are largely noise; 4/7 paper claims fail statistical testing; mean values relevance = 33.6/100; void explained by publication infrastructure, not epistemic injustice. Major paper revision required.

---

## 1. What Was Accomplished

Session 6 focused on analytical rigor: stress-testing every paper claim with computational analysis, expanding the evidence base, and identifying critical bugs in the scoring framework.

### Phase 1: Sensitivity Analysis & Claim Testing

| Analysis | Key Result |
|----------|------------|
| **Bootstrap CI** | Width = 15.87 pts vs score spread = 22.3 pts (CIs cover 71.2%) |
| **Weight sweep** | Mean Kendall's tau = 0.773; 12/47 benchmarks robust across >80% of weight combos |
| **Certainty tiers** | Only 9 "certain" Top-15 members (p >= 0.95); 8 "contested" |
| **Claim testing** | 3/7 claims survive (Claims 1-3); Claims 4, 6, 7 fail; Claim 5 marginal |

### Phase 2: Values Relevance Assessment

| Analysis | Key Result |
|----------|------------|
| **Claude feature assessment** | 50 gate-passers scored on 24+ features from 109-feature taxonomy |
| **Mean A3 values relevance** | 33.6/100 — only ~8 benchmarks (17%) genuinely test religious values alignment |
| **Top scorers** | IslamTrust (90), BuddhismEval (85), CatholicBench (80), Gospel Coalition (80) |
| **Monolith finding** | 15/16 treat religion as monolith (no denominational awareness) |

### Phase 3: Void Factor Analysis & Expanded Search

| Analysis | Key Result |
|----------|------------|
| **Void factor taxonomy** | Publication infrastructure (r=0.74) strongest predictor, not formalizability (r=0.41, n.s.) |
| **Readiness index** | Benchmark-bearing mean=10.5 vs void mean=5.1 (r=0.66, p=0.010) |
| **Judaism anomaly** | Readiness 12/15, formalizability 5/5, zero benchmarks — community preference for tools over evaluations |
| **Expanded vault search** | 321 new candidates (41 Ubuntu, 25 Taoism, 29 Judaism missed by rv_* < 50 threshold) |
| **External search** | 35 discoveries incl. IslamicMMLU (10,013 items), CMoralEval (30K), IslamicLegalBench (7 schools) |

### Phase 4: Bug Fixes, Verification, Clustering

| Task | Result |
|------|--------|
| **PE computation bug** | Was using only P7x10, now uses 6-feature composite |
| **R2 distribution bug** | Was 85.3% at floor, now 68.8% (better discrimination) |
| **CI dead weight bug** | Redistributed 15% dead weight, added C6 community bonus |
| **URL verification** | 43/47 gate-passers accessible; 1 AUTH_REQUIRED, 3 NOT_FOUND |
| **Clustering** | ARI ~ 0 for both tradition family and format — no simple structure |

---

## 2. Key Numbers Delta

| Metric | Session 5 | Session 6 | Delta |
|--------|-----------|-----------|-------|
| Gate-passers | 46 | 47 | +1 |
| New vault candidates | 0 | 321 | +321 |
| External discoveries | 53 | 53 + 35 = 88 | +35 |
| Features per benchmark | 22 | 109 (taxonomy designed), 24+ scored | +87 designed |
| Statistical tests | 0 | 7 claim tests + sensitivity + correlations | +10 |
| LLM trial items designed | 30 (T2 pilot) | 30 + 45 + 20 = 95 | +65 |
| Council deliberations | D-02 + D-03 | + D-01 (session 6) | +1 |
| Council recommendations | 76 | 76 + 39 = 115 | +39 |
| Data files generated | ~7 | ~7 + 15 = ~22 | +15 |
| Scripts created | ~11 | ~11 + 9 = ~20 | +9 |

---

## 3. Claim Robustness Results

The central analytical finding of Session 6: only 3 of the paper's 7 claims survive statistical testing.

| # | Claim | Status | Statistical Evidence |
|---|-------|--------|---------------------|
| 1 | Tradition asymmetry | ROBUST | chi-squared=64.96, Cramer's V=0.53 |
| 2 | Knowledge-reasoning conflation | ROBUST | 27.7% reasoning, p=0.0015 |
| 3 | Data availability bottleneck | ROBUST | 170/401 unavailable |
| 4 | Structural epistemic injustice | NOT SUPPORTED | Pseudo-R-squared=0.068, no predictor p<0.05 |
| 5 | Field recency | MARGINAL | 59.6% from 2024+, p=0.12 |
| 6 | WEIRD bias | REVERSED | Non-WEIRD passes at higher rate (14.4% vs 8.9%) |
| 7 | Bias-values conflation | NOT SUPPORTED | p=0.68 |

**Implications for paper revision:**
- Claims 1-3: Strengthen with statistical evidence; these are genuine contributions.
- Claim 4: Reframe from "systematic scoring bias" to "publication infrastructure barrier" (r=0.74). The injustice is real but operates through infrastructure, not the scoring framework.
- Claim 5: Present as observation with honest p=0.12 disclosure.
- Claim 6: Reverse direction. Non-WEIRD traditions actually pass at higher rates due to Islamic benchmark dominance. Rewrite as "WEIRD bias does not manifest as expected."
- Claim 7: Downgrade to hypothesis or remove. p=0.68 is nowhere near significant.

---

## 4. Rankings Are Largely Noise

Session 6's sensitivity analysis reveals that the Top-15 ranking is far less stable than previously presented.

| Finding | Value |
|---------|-------|
| Bootstrap CI width (mean) | 15.87 points |
| Total score spread | 22.3 points |
| CI-to-spread ratio | 71.2% |
| Robust benchmarks (in Top 15 across >80% of weight combos) | 12 |
| Certain members (p >= 0.95) | 9 |
| Contested members | 8 |
| Mean Kendall's tau across weight combos | 0.773 |

**Required revision:** Replace the definitive "Top 15" presentation with an uncertainty-aware tiered system:
- **Tier 1 (Certain, p >= 0.95):** 9 benchmarks
- **Tier 2 (Likely):** 6 benchmarks
- **Tier 3 (Contested):** 8 benchmarks

---

## 5. Values Relevance Assessment

The paper's strongest new finding: most "religious values benchmarks" do not actually test religious values.

| Metric | Value |
|--------|-------|
| Mean A3 values relevance (50 gate-passers) | 33.6/100 |
| Benchmarks with A3 >= 75 (genuine values testing) | ~8 (17%) |
| Benchmarks treating religion as monolith | 15/16 (94%) |

**Top scorers by values relevance:**

| Benchmark | A3 Score |
|-----------|----------|
| IslamTrust | 90 |
| BuddhismEval | 85 |
| CatholicBench | 80 |
| Gospel Coalition | 80 |

**Data quality issues identified:**
- ELQV: Wrong PDF extract in vault
- Confucian Analects: Wrong PDF extract in vault
- IslamTrust and FatwaSet: Possible duplicate entries needing deduplication

**Most influential clustering features:** R1_count and R5_pluralism (both reward multi-tradition coverage). ARI approximately 0 for tradition family and format — benchmarks do not cluster by either dimension.

---

## 6. Void Factor Taxonomy

A new analytical contribution explaining why 8/14 traditions have zero viable benchmarks.

| Factor | Correlation with Void | Significance |
|--------|----------------------|--------------|
| Publication infrastructure | r=0.74 | **Strongest predictor** |
| Community practice norms | r=0.58 | Significant |
| Formalizability | r=0.41 | Not significant |

**Readiness index** (composite of 6 factors, max 15):
- Benchmark-bearing traditions: mean = 10.5
- Void traditions: mean = 5.1
- Correlation: r=0.66, p=0.010

**Judaism anomaly:** Readiness 12/15, formalizability 5/5, yet zero benchmarks. The Jewish AI community builds tools (halakhic reasoning engines, Talmudic NLP) rather than evaluation benchmarks — a community-level preference for construction over assessment.

**Gate-passage model:** Tradition family does NOT independently predict passage (p=0.112), contradicting the epistemic injustice framing.

**Traditions that remain completely void:** Jainism, Taoism, Shinto, Baha'i, Zoroastrianism.

---

## 7. Council Review (D-01)

**File:** `20260404-council-D01-critique.md`
**Size:** 574 lines, 13,806 words
**Panel:** 12-member expert council (expanded from 6 in D-02/D-03)
**Composition file:** `20260404-council-session6-composition.md`

| Priority | Count |
|----------|-------|
| Critical | 13 |
| Important | 16 |
| Desirable | 10 |
| **Total** | **39** |

**Recorded dissents:** 3

**Cumulative council record:**

| Deliberation | Session | Recs | Implemented |
|-------------|---------|------|-------------|
| D-02 | 4 | 52 | 52/52 |
| D-03 | 5 | 24 | 24/24 |
| D-01 | 6 | 39 | Pending |
| **Total** | — | **115** | **76/115 (66%)** |

---

## 8. Expanded Evidence Base

### New Vault Candidates (321)

| Tradition | Candidates Found | Note |
|-----------|-----------------|------|
| Ubuntu Philosophy | 41 | In vault but rv_* < 50 |
| Judaism | 29 | In vault but rv_* < 50 |
| Taoism | 25 | In vault but rv_* < 50 |
| Other traditions | 226 | Various thresholds |

**Root cause:** The rv_* scoring threshold of 50 is too aggressive for traditions with indirect vocabulary (Ubuntu, Taoism) and for traditions whose benchmarks appear in broader cultural/philosophical venues (Judaism).

### External Discoveries (35 new, 88 cumulative)

| Discovery | Items | Significance |
|-----------|-------|-------------|
| IslamicMMLU | 10,013 | Largest single religious benchmark found |
| CMoralEval | 30,000 | Chinese moral evaluation (Confucian/Taoist content) |
| IslamicLegalBench | 7 schools | Multi-school legal reasoning |
| Other | 32 discoveries | Various traditions |

---

## 9. Scoring Framework Bug Fixes

Three critical bugs were identified and fixed in `build_religious_feature_matrix.py`:

| Bug | Before | After | Impact |
|-----|--------|-------|--------|
| **PE computation** | Only P7 x 10 | 6-feature composite | Scores now reflect actual psychometric quality |
| **R2 distribution** | 85.3% at floor | 68.8% at floor | Better discrimination among low-relevance benchmarks |
| **CI dead weight** | 15% unallocated | Redistributed + C6 community bonus | More meaningful CI scores |

---

## 10. Complete File Manifest — Session 6

### Council Documents (in PAPER/)

| File | Size | Role |
|------|------|------|
| `20260404-council-session6-composition.md` | — | 12-member council roster, roles, mandates, decision protocol |
| `20260404-council-D01-critique.md` | ~14 KB | 39 recommendations (13C/16I/10D), 3 dissents |

### Data Files (in data/)

| File | Size | Role |
|------|------|------|
| `20260404-religious-benchmark-feature-matrix-v2.json` | 1.1 MB | Corrected 401-entry feature matrix |
| `20260404-sensitivity-analysis.json` | 47 KB | Weight sweep, bootstrap CIs, gate threshold, feature LOO |
| `20260404-expanded-vault-candidates.json` | 368 KB | 321 new vault candidates |
| `20260404-external-search-results-v2.json` | 30 KB | 35 external discoveries |
| `20260404-citation-chain-discoveries.json` | 20 KB | Citation chain finds |
| `20260404-data-availability-verification.json` | 21 KB | URL verification for 47 gate-passers |
| `20260404-correlation-matrix.json` | 6 KB | Spearman correlations + clustering |
| `20260404-claim-robustness-tests.json` | 8 KB | 7 statistical tests |
| `20260404-gate-passage-predictors.json` | 6 KB | Logistic regression model |
| `20260404-void-factor-taxonomy.json` | 8 KB | 14 traditions x 6 factors |
| `20260404-claude-assessment-batch1.json` | 39 KB | 16 benchmarks scored on 24+ features |
| `20260404-claude-assessment-batch2.json` | 73 KB | 34 benchmarks scored on 24+ features |
| `20260404-construct-validity-items.json` | — | 45 LLM trial items (3x3x5 design) |
| `20260404-bias-values-items.json` | — | 10 paired bias/values items |
| `20260404-format-taxonomy.json` | 2 KB | 12 format codes |

### Reports (in reports/)

| File | Role |
|------|------|
| `20260404-void-analysis-report.md` | Void factor taxonomy analysis |

### Scripts (in scripts/)

| File | Role |
|------|------|
| `20260404-sensitivity-analysis.py` | Weight sweep, bootstrap, gate threshold, LOO |
| `20260404-expanded-vault-search.py` | Full-text extract + YAML near-miss search |
| `20260404-verify-data-urls.py` | HTTP verification of DATA_URLs |
| `20260404-statistical-analysis.py` | Spearman correlations + hierarchical clustering |
| `20260404-claim-robustness.py` | 7 statistical tests for paper claims |
| `20260404-gate-passage-model.py` | Logistic regression predictor |
| `20260404-void-factor-analysis.py` | Structural factor taxonomy |
| `20260404-construct-validity-runner.py` | LLM trial runner (ready, needs API key) |

### Modified Existing Files

| File | Change |
|------|--------|
| `scripts/build_religious_feature_matrix.py` | PE/R2/CI bug fixes (3 bugs) |

---

## 11. All Seven Claims — Revised Coverage Map

| # | Claim | Session 5 Status | Session 6 Status | Required Action |
|---|-------|-------------------|-------------------|-----------------|
| 1 | Tradition asymmetry | Presented | **ROBUST** (chi-squared=64.96, V=0.53) | Add statistical evidence to prose |
| 2 | Knowledge-reasoning conflation | Supported by T2 trial | **ROBUST** (27.7% reasoning, p=0.0015) | Add statistical evidence |
| 3 | Data availability bottleneck | Presented | **ROBUST** (170/401 unavailable) | Strengthen with concrete numbers |
| 4 | Structural epistemic injustice | Presented | **NOT SUPPORTED** (Pseudo-R-squared=0.068) | Reframe: infrastructure barrier, not scoring bias |
| 5 | Field recency | Presented | **MARGINAL** (p=0.12) | Add honest uncertainty disclosure |
| 6 | WEIRD bias | Presented | **REVERSED** (non-WEIRD passes higher) | Rewrite direction; acknowledge Islamic dominance effect |
| 7 | Bias-values conflation | Supported by T4 trial | **NOT SUPPORTED** (p=0.68) | Downgrade to hypothesis or remove |
| 8 | Values relevance failure | — | **NEW** (mean A3=33.6/100) | Add as new claim; strongest finding |

---

## 12. Next Steps

### Short-Term (Session 7 priorities)

1. **Revise paper claims** — Downgrade Claims 4, 6, 7 from "claims" to "observations" or "hypotheses"; add statistical evidence for Claims 1-3; acknowledge Claim 5 is marginal. Add new Claim 8 (values relevance failure).
2. **Run LLM construct validity trials** — Execute the construct validity runner:
   ```bash
   ANTHROPIC_API_KEY=... ../.venv/bin/python RELIGIOUS-VALUES/scripts/20260404-construct-validity-runner.py
   ```
3. **Present rankings with uncertainty** — Replace definitive "Top 15" with tiered system: Tier 1 (certain, p >= 0.95): 9 benchmarks; Tier 2 (likely): 6; Tier 3 (contested): 8.
4. **Add A3 values relevance to paper** — "Mean values relevance = 33.6/100" is the paper's strongest new finding; integrate into Sec 4.4 and abstract.
5. **Fix data quality issues** — Correct ELQV and Confucian Analects PDF extracts; deduplicate IslamTrust/FatwaSet entries.
6. **Lower RD gate for exploratory analysis** — Show what the landscape looks like at RD >= 20 (admits Judaism and Jainism candidates).

### Medium-Term

7. **Redesign the framework** — Move from 3-axis (RD/PE/CI) to empirically-derived axes via factor analysis on the 109-feature taxonomy.
8. **Write the .bib file** — Still the #1 missing piece for citation formatting.
9. **LaTeX conversion** for NeurIPS 2026 D&B submission.
10. **Cross-model replication** of construct validity probes (GPT-4o, Llama-3-70B).

### Critical Paper Revisions Based on Session 6

- **Reframe Claim 4 (epistemic injustice):** The injustice operates through publication infrastructure (r=0.74), not systematic scoring bias. This is a more precise and empirically grounded framing.
- **Remove or caveat Claim 6 (WEIRD bias):** Non-WEIRD traditions actually pass at higher rates due to Islamic benchmark dominance. The WEIRD/non-WEIRD dichotomy does not explain the pattern.
- **Add new Claim 8:** "Most benchmarks fail the values relevance test" (mean A3=33.6, supported by 50-benchmark ground-truth assessment). This is the paper's strongest empirical contribution from Session 6.
- **Present sensitivity analysis prominently** — The "rankings are largely noise" finding demands intellectual honesty about framework limitations. Position as a methodological contribution rather than a weakness.
- **Add the void factor taxonomy** as a new contribution — Structural explanation (publication infrastructure) vs epistemological explanation (formalizability) of the 8-tradition gap. The Judaism anomaly is particularly instructive.
- **Implement D-01 council recommendations** — 39 recommendations (13 Critical, 16 Important, 10 Desirable) pending implementation.

---

## 13. Cumulative Project Status

| Component | Status |
|-----------|--------|
| Paper prose (Secs 1-6) | Complete, revision needed for claims 4-7 |
| Tables (3 main + 2 supplement) | Complete |
| Figures (4 PNGs) | Complete |
| Implementation trials (T2, T3, T4) | Complete |
| Sensitivity analysis | **NEW — Complete** |
| Claim robustness testing | **NEW — Complete (3/7 survive)** |
| Values relevance assessment | **NEW — Complete (mean 33.6)** |
| Void factor taxonomy | **NEW — Complete** |
| Expanded search (321 + 35) | **NEW — Complete** |
| URL verification | **NEW — Complete (43/47 accessible)** |
| Clustering analysis | **NEW — Complete (ARI ~ 0)** |
| Council D-01 recs | **NEW — 39 recs pending** |
| .bib file | Not started |
| LaTeX conversion | Not started |
| Cross-model replication | Not started |
| Construct validity LLM trials | Items designed (95), execution pending |
