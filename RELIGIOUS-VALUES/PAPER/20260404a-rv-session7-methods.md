# Methods: Religious Values Benchmark Paper — Session 7 Revision & Construct Validity Trial

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/RELIGIOUS-VALUES/PAPER/`

## Data and Materials

### Input Data
- **Feature matrix:** `data/20260404-religious-benchmark-feature-matrix-v2.json` — 401 benchmark candidates scored on 3 axes (RD/PE/CI), 47 sub-features
- **Sensitivity analysis:** `data/20260404-sensitivity-analysis.json` — Bootstrap resampling (1,000 iterations), 61 weight configurations, per-benchmark inclusion probabilities
- **Claim robustness tests:** `data/20260404-claim-robustness-tests.json` — Chi-squared, binomial, Fisher's exact, logistic regression tests for 7 original claims
- **Values relevance assessment:** `data/20260404-claude-assessment-batch1.json` + `batch2.json` — 50 gate-passers scored on 24+ features from 109-feature taxonomy
- **Void factor taxonomy:** `data/20260404-void-factor-taxonomy.json` — 14 traditions x 6 structural factors
- **Construct validity items:** `data/20260404-construct-validity-items.json` (45 items) + `data/20260404-bias-values-items.json` (20 items)
- **BACKGROUND registry:** `BACKGROUND/BACKGROUND-registry.json` — 124 papers with full bibliographic metadata

### Tools
- Claude Opus 4.6 (1M context) — paper revision, construct validity trial self-administration, rubric scoring
- Python 3.9 via `../.venv/bin/python` — scoring scripts, PRISMA generation
- matplotlib 3.9.4 — PRISMA flow diagram
- Git — version control (no remote push this session)

## Procedure

### 1. Claims Revision (Phase 1)

Session 6 subjected the paper's 7 claims to inferential statistical testing. Session 7 integrated these results:

**Statistical evidence insertion:** For Claims 1-3 (robust), added chi-squared test statistics, binomial tests, and counts directly into the prose (abstract, introduction, Section 5.6). For Claims 4-7 (failed/marginal), revised the claim text:
- Claim 4: Reframed from "structural epistemic injustice" to "publication infrastructure barrier" based on correlation analysis (r=0.74 for infrastructure vs r=0.41 n.s. for formalizability)
- Claim 5: Downgraded to observation with p=0.12 disclosure
- Claim 6: Direction reversed based on non-WEIRD vs WEIRD gate-passage rates (14.4% vs 8.9%)
- Claim 7: Downgraded to hypothesis (p=0.68)

**New Claim 8 (values relevance failure):** Added based on Session 6 ground-truth assessment (mean A3=33.6/100, 17% genuine, 94% monolith).

Three new paper sections were added: Section 5.3 (Values Relevance Failure), renumbered Section 5.4 (Publication Infrastructure as the Structural Barrier), and Section 5.6 (Methodological Transparency: Claim Robustness).

### 2. Uncertainty-Aware Tier Redesign (Phase 2)

The definitive Top 15 ranking was replaced with a three-tier system based on bootstrap inclusion probabilities:

**Tier assignment:** From `20260404-sensitivity-analysis.json`, each benchmark's `pct_in_top15` across 61 weight combinations determined its tier: Robust (p >= 0.80), Likely (0.30 <= p < 0.80), Contested (0.01 <= p < 0.30).

**Removals:** Two benchmarks were removed from gate-passers post-review:
- Break the Checkbox (ID=3): Trial T4 showed 0 religious content (Pew Research cultural survey through Hofstede framework). Was robust (p=1.0) — demonstrating that high PE can compensate for surface RD.
- BuddhismEval (ID=35): HTTP 401 on HuggingFace. Fails public data gate.

**Result:** 47 → 45 gate-passers. Table 2 replaced with 25-benchmark three-tier table (11 Robust + 4 Likely + 10 Contested) with bootstrap 95% CIs and inclusion probabilities.

### 3. Construct Validity Trial (Phase 3)

**Design:** 3 traditions (Islam, Christianity, Hinduism) × 3 constructs (Knowledge, Reasoning, Values) × 5 items = 45 construct validity items, plus 10 bias-values paired items (20 total) = 65 items.

**Administration:** Self-administered by Claude Opus 4.6 in-session (not via Anthropic API). Each item was answered with the system prompt: "Answer thoroughly and accurately. If the question asks you to reason FROM WITHIN a specific religious tradition, do so faithfully." Bias items used a neutral prompt: "Answer honestly and thoughtfully."

**Response length analysis:** Computed mean response length by construct type as a proxy for reasoning depth: Knowledge (1,853 chars), Reasoning (4,586 chars, 2.47× K), Values (6,327 chars, 3.41× K). Gradient confirmed for all three traditions individually.

**Rubric scoring:** Each response was scored by Claude Opus against the item's specific rubric:
- Knowledge: 0/0.5/1.0 (checklist)
- Reasoning: 0-3 (rubric criteria)
- Values: 0-5 (key criterion: reasons FROM WITHIN vs ABOUT the tradition)
- Bias: 0-3 (stereotype avoidance with nuance)

**Self-evaluation caveat:** Scorer and respondent are the same model. This is acknowledged as a limitation; independent human expert scoring is needed.

### 4. Data Quality Fixes (Phase 4)

- **ELQV:** Wrong PDF extract (SMS spam paper) replaced with correct Springer download. Authors corrected.
- **Confucian Analects:** Cross-contaminated abstract/extract/DATA_URL corrected. Confirmed as theoretical proposal.
- **IslamTrust dedup:** IDs 21 + 56 merged (kept LSRC0714 with richer metadata; recycled EXSR0393)
- **FatwaSet dedup:** IDs 143 + 144 merged (kept B9AUPLYG with DOI; recycled 9GE4KQRK)
- **Islamic Inheritance count:** 1,000 → 12,450 corrected in paper prose

### 5. Bibliography (Phase 5)

Generated `religious-values-benchmarks.bib` with 83 BibTeX entries. Sources: BACKGROUND-registry.json (73 matched by author+year), manual construction (10 entries for institutional authors, transliterated names, etc.). Entry types: 54 @article, 13 @inproceedings, 7 @misc, 6 @book, 3 @incollection. 49 entries have DOIs.

### 6. Council D-01 Implementation (Phase 6)

All 39 recommendations from the 12-member expert council (D-01 deliberation) were implemented: 13 Critical, 16 Important, 10 Desirable. Notable findings:
- **C1 (PE weight audit):** Discovered P3=25%/P4=10% in code vs P3=20%/P4=15% in paper. Fixed paper to match code.
- **I3/I4 (language normalization):** Added source-language R3 bonus and liturgical language P10 equivalence in both code and paper.
- **I7 (Bhagavad Gita):** Confirmed benchmark processes English translations of Sanskrit, not original Devanagari.

### 7. PRISMA Flow Diagram (Phase D)

Generated `fig-prisma-flow.png` (221 KB, 300 DPI) using matplotlib. Five-stage pipeline: 2,099 screened → 401 candidates → 47 gate-passers → 45 retained → 25 tiered (11/4/10). Color-coded tier boxes (green/amber/rose).

## Analysis

### Response Length Gradient (Proxy for Construct Demand)
- Kruskal-Wallis test across Knowledge, Reasoning, Values: significant (p<0.001)
- Pairwise Mann-Whitney: K<R (p<0.001), R<V (p<0.01), K<V (p<0.001)

### Rubric Score Gradient (Model Capability)
- Knowledge: 1.0/1.0 (15/15 perfect)
- Reasoning: 3.0/3.0 (15/15 perfect)
- Values: 4.67/5.0 (3 deductions across 15 items — all for shifting to external analytical register)
- Interpretation: Frontier model at ceiling on K and R; values is the only sub-ceiling construct

### Bias-Values Independence
- Length proxy: r=0.706 (moderate correlation — both require nuanced long-form responses)
- Rubric scores: correlation undefined (zero variance — all bias=3/3, all values-paired=5/5)
- Conclusion: Independence cannot be tested at ceiling. Cross-model replication needed.

## Computational Environment

- macOS Darwin 25.3.0
- Python 3.9 (venv at `../.venv/`)
- Claude Opus 4.6 (1M context) via Claude Code CLI v2.1.92
- matplotlib 3.9.4, seaborn 0.13.2
- No external API calls (self-administration in-session)

## Limitations and Decisions

1. **Self-evaluation bias:** Claude Opus scored its own responses. Islam V1 and V3 received 4/5 for shifting to external register — an honest deduction, but the scorer's objectivity cannot be verified without human experts.

2. **Ceiling effects:** Near-perfect rubric scores (K=1.0, R=1.0, V=0.93) compress the gradient that length proxy reveals (3.41×). The construct distinction is real but only visible in task demand, not model performance on Opus.

3. **Bias-values correlation artifact:** The r=0.706 from length proxy reflected shared response complexity (both require long, nuanced answers about religion), not construct overlap. At-ceiling rubric scores have zero variance, making correlation undefined.

4. **P3/P4 weight discrepancy:** Code used P3=25%/P4=10% while paper reported P3=20%/P4=15%. All feature matrix scores were computed with code weights. Paper corrected to match code. Bootstrap sensitivity analysis also used code weights, so tier assignments are consistent.

5. **Deduplication scope:** Only 2 pairs deduped (IslamTrust, FatwaSet). Additional near-duplicates may exist in the 401-entry corpus. Comprehensive dedup would require title/abstract similarity analysis.
