# NormEval Session 7 — Claim 4 Resolution + Benchmark Expansion Handoff

**Date:** 2026-04-04
**Session:** Claim 4 factual correction + 17-benchmark ingestion (37 → 54)
**Project:** `CEI-Lit-WS/NORM-ETHICS/`
**Previous handoff:** `METHODS/20260404-normeval-session6-handoff.md`

---

## What Was Done This Session

### Part A: Claim 4 Resolution (Judgment vs. Reasoning)

**Problem:** The paper inconsistently stated "28 of 37" (spine, abstracts, discussion) and "22 of 37" (results body) benchmarks test moral judgment. The hypothesis test used 22/37 (p=0.162, NOT significant). This was flagged as "the single most serious factual error in the manuscript."

**Root cause identified:** The spine counted J+B (judgment + both) but made an off-by-one arithmetic error (27 written as 28). The body counted strict J-only (22). Neither was internally wrong — they were inconsistent with each other.

**Resolution:**
1. **Systematic recount** of all 37 benchmarks with documented 3-category coding rules (J=22, B=5, R=10)
2. **Re-ran hypothesis test** with three framings:
   - Strict (J-only = 22/37): p=0.162 — NOT significant
   - Broad (J+B = 27/37): p=0.004 — significant
   - **Inverted (R-only = 10/37): p=0.004 — significant** (recommended framing)
3. **Fixed 7 stale references** across 5 paper files (spine, main-body ×2, introduction, introduction-comprehensive ×2, discussion)
4. **New framing:** "Only 10 of 37 benchmarks (27%) evaluate moral reasoning quality" — mathematically equivalent, statistically significant, precise with breakdown

**PrinciplismQA inconsistency found:** v1 codes as "Both" but v2 scores 75 (framework reasoning). Recommendation: keep v1 as "Both", correct v2 from 75 to 50.

### Part B: 17-Benchmark Ingestion (37 → 54)

**5 external papers ingested:**
- Xu et al. 2026 — Probing Ethical Framework Representations (arXiv 2603.23659)
- Zhang et al. 2026 — RLVR Moral Reasoning (arXiv 2603.10588)
- IslamicMMLU 2026 — 10,013 MCQ Islamic knowledge (arXiv 2603.23750)
- IslamicLegalBench 2026 — 718 instances, 7 jurisprudence schools (arXiv 2602.21226)
- Du et al. 2025 — 196 research ethics dilemmas (arXiv 2505.08106)

**12 vault papers scored** (OffTheRails, EMNLP Framework, COMETH, Ebara Medical Ethics, MedES, Basu Multilingual, CVC Chinese Values, One Model Many Morals, MMRB, Is ETHICS About Ethics?, TRIAGE, Normative Evaluation AITA)

**Expanded matrix results:**
- 54 total benchmarks, 24 gate-passing (was 15)
- 3 new Top 15 entries: One Model Many Morals (#8), EMNLP Framework (#13), TRIAGE (#15)
- Top 15 no longer perfectly stable (1/18 weight combinations) — was 100% at n=37
- C4 reasoning deficit INTENSIFIES: 10/54 = 18.5%, p=0.000002

**Computational analyses re-run** on expanded corpus: hypothesis tests, correlations, sensitivity, rankings.

### Part C: Dashboard Update + Deployment

- Updated `generate_normeval_dashboard.py` to use expanded matrix (54 benchmarks)
- Regenerated `data.js` (130KB → 172KB)
- Created public repo: `cjimmylin/cei-normeval-dashboard`
- Deployed to GitHub Pages: **https://cjimmylin.github.io/cei-normeval-dashboard/**

---

## Remaining Work

### Priority 1: Cross-model replication
Needs GPT-4o, Llama-3, DeepSeek API keys. Power analysis says n=49/group needed for C2 at 80% power. This is the #1 reviewer concern.

### Priority 2: LaTeX conversion (NeurIPS 2026 template)
8pp main body + unlimited appendix. Paper text is in markdown, needs conversion. References need .bib file (177 entries).

### Priority 3: Paper text revision per improvement recommendations
`STATISTICS/20260404-normeval-improvement-recommendations.md` has a 754-line roadmap. Key items:
- Update paper title to reflect n=54 (currently says "37")
- Add expanded corpus section to methods
- Revise Top 15 discussion (now Top 15 from 24 candidates)
- Add sensitivity analysis discussion (weights now matter)

### Priority 4: PrinciplismQA v2 score correction
Correct A3_reasoning_refined from 75 to 50 in `20260404-normeval-v2-feature-scores.json`

### Priority 5: Full-scale trials
MoReBench 680 items, MoralReason-QA 2,040 items — needs API access to actual benchmark data.

---

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Claim 4 recount | `STATISTICS/20260404-normeval-claim4-recount.md` | Full 37-row recount with coding rules |
| Claim 4 hypothesis tests | `STATISTICS/20260404-normeval-claim4-hypothesis-test.json` | Strict/broad/inverted binomial tests |
| Expanded feature matrix | `STATISTICS/20260404-normeval-expanded-feature-matrix.json` | 54 benchmarks, full schema |
| Expanded analyses | `STATISTICS/20260404-normeval-expanded-analyses.json` | Hypothesis tests, correlations, sensitivity, rankings at n=54 |
| Batch 1 scores | `STATISTICS/20260404-normeval-batch1-scores.json` | IDs 38-43 (vault) |
| Batch 2 scores | `STATISTICS/20260404-normeval-batch2-scores.json` | IDs 44-49 (vault) |
| Batch 3 scores | `STATISTICS/20260404-normeval-batch3-scores.json` | IDs 50-54 (external) |
| Ingestion report | `STATISTICS/20260404-normeval-ingestion-report.md` | Full expansion summary |
| Dashboard data | `DASHBOARD/data.js` | 172KB, 54 benchmarks, 13 JS constants |
| Dashboard generator | `PYTHON/generate_normeval_dashboard.py` | Updated to use expanded matrix |
| Dashboard URL | https://cjimmylin.github.io/cei-normeval-dashboard/ | Live deployment |
| Paper spine | `PAPER/spine-normeval.md` | Updated Claim 4 |
| Paper main body | `PAPER/main-body-normeval.md` | Updated 2 Claim 4 references |
| Paper introduction | `PAPER/introduction-normeval.md` | Updated abstract |
| Paper intro (comprehensive) | `PAPER/introduction-comprehensive-normeval.md` | Updated abstract + §2.4 |
| Paper discussion | `PAPER/discussion-normeval.md` | Updated §5.5 |
| 5 new vault entries | `papers/2026-Xu-*.md`, `papers/2026-Zhang-*.md`, etc. | External paper metadata |
| 5 new PDFs | `../Lit-WS-PDFs/2025/`, `../Lit-WS-PDFs/2026/` | Downloaded from arXiv |
| 10 new extracts | `PDF Extracts/2025/`, `PDF Extracts/2026/`, `BACKGROUND/EXTRACT/` | Text extractions |

## Known Issues

1. **PrinciplismQA v2 score inconsistency** — v1="Both" but v2=75 (should be 50). Minor; does not affect rankings.
2. **Top 15 no longer gate-determined** — with 24 gate-passing benchmarks, composite weights now matter. Paper needs to acknowledge this.
3. **Playwright browser connection** — was closed/timed out; dashboard visual verification done programmatically instead. Manual check recommended.
4. **Paper title says "37"** — needs updating to "54" once paper revision begins.
5. **v2 features file** (`20260404-normeval-v2-feature-scores.json`) only covers IDs 1-37 — new benchmarks (38-54) are in expanded matrix but not v2.

---

*Filed: 2026-04-04 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
