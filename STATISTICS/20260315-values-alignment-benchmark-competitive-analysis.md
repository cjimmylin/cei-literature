# Values Alignment Benchmark Compendia: Competitive Analysis

**Date:** 2026-03-15
**Author:** CEI Literature Vault — Council of 7 Experts Analysis
**Vault snapshot:** 2,043 papers · 989 benchmark candidates · 107 cross-framework implementations
**Companion data:** `20260315-values-alignment-benchmark-data.json`

---

## Table of Contents

1. [Existing Compendia Landscape](#section-1-existing-compendia-landscape)
2. [Expert 1 — AI Evaluation Researcher (Technical Architecture)](#section-2-expert-1--ai-evaluation-researcher)
3. [Expert 2 — Moral Philosopher (Ethical Coverage)](#section-3-expert-2--moral-philosopher)
4. [Expert 3 — Cross-Cultural Psychologist (Cultural Diversity)](#section-4-expert-3--cross-cultural-psychologist)
5. [Expert 4 — NLP/ML Benchmarking Expert (Implementability)](#section-5-expert-4--nlpml-benchmarking-expert)
6. [Expert 5 — AI Safety/Policy Researcher (Regulatory Relevance)](#section-6-expert-5--ai-safetypolicy-researcher)
7. [Expert 6 — Psychometrician (Measurement Quality)](#section-7-expert-6--psychometrician)
8. [Expert 7 — Strategic Positioning Analyst (White Space)](#section-8-expert-7--strategic-positioning-analyst)
9. [Strategic Recommendations & Roadmap](#section-9-strategic-recommendations--roadmap)

---

## Section 1: Existing Compendia Landscape

### 1.1 Tier 1 — Multi-Dimensional Meta-Benchmarks (Direct Competitors)

These are the closest analogues to a combined values-alignment assessment — broad evaluation suites that aggregate multiple benchmarks into a unified framework.

| Compendium | Year | Dimensions | Scenarios/Tasks | Languages | Cultural Coverage | Harness | Public Data |
|------------|------|------------|-----------------|-----------|-------------------|---------|-------------|
| **HELM** (Stanford CRFM) | 2022 | 7 metrics | 42 scenarios | 1 (English) | Minimal | HELM | Partial |
| **HELM Safety v1.0** | 2024 | Safety taxonomy | BBQ, HarmBench, XSTest, etc. | 1 | Minimal | HELM | Yes |
| **DecodingTrust** | 2023 | 8 trustworthiness dims | Per-dimension protocols | 1 | None | Standalone | Yes (HuggingFace) |
| **TrustLLM** | 2024 | 8 trustworthiness dims | 30+ tasks, 16 LLMs | 1 | None | Standalone | Yes (GitHub) |
| **BIG-Bench** | 2022 | Flat collection | 200+ tasks | ~1 | Minimal | BIG-Bench | Yes |

**Key architectural patterns observed:**
- **HELM:** scenario × metric matrix with per-scenario normalization; explicitly rejects single aggregate scores
- **lm-eval:** Plugin architecture via Task interface (`doc_to_text` + `doc_to_target` + metrics); enables rapid community contribution — 65+ values-relevant tasks already integrated
- **DecodingTrust:** Per-dimension [0,100] normalized scores enabling cross-model comparison
- **BIG-Bench:** Flat task collection with normalized score per task; minimal cross-task structure

**Critical observation:** All Tier 1 competitors are English-centric and culturally Western. None decompose along normative philosophical traditions. None connect to governance frameworks.

### 1.2 Tier 2 — Values-Specific Comprehensive Benchmarks

These benchmarks go deeper into specific value dimensions but remain standalone rather than aggregated into meta-suites.

| Benchmark | Year | Focus | Size | Languages | Cultural Scope | Normative Traditions |
|-----------|------|-------|------|-----------|----------------|---------------------|
| **ETHICS** (Hendrycks) | 2021 | 5 normative domains | 130K+ examples | 1 | Western | Justice, well-being, duties, virtues, commonsense |
| **ValueBench** (Ren) | 2024 | Psychometric value profiles | 44 inventories, 453 dims | 1 | Western psych | Via Schwartz, MFT, etc. |
| **SafetyBench** | 2024 | 7 safety categories | 11,435 MCQ | 2 (CN+EN) | Chinese + English | Safety-focused |
| **CValues** | 2023 | Chinese human values | 10+8 scenarios | 1 (Chinese) | Chinese | Safety + responsibility |
| **MoralBench** | 2024 | Moral Foundations Theory | MFQ-30-LLM + MFV-LLM | 1 | Western psych | MFT (5 foundations) |
| **LocalValueBench** | 2024 | Australian national values | 6 topics | 1 | Australian | National value alignment |
| **UniMoral** | 2025 | Multilingual moral reasoning | 8,784 instances | 6 | South Asian | Psychologically grounded |
| **MoReBench** (Chiu) | 2025 | Moral reasoning depth | 1,000 scenarios, 23K+ criteria | 1 | Western | Multi-framework |
| **MACHIAVELLI** (Pan) | 2023 | Game-based moral behavior | 134 games, 500K+ scenarios | 1 | Western | Consequentialist |
| **SCRUPLES** (Lourie) | 2021 | Ethical judgment | 625K judgments, 32K anecdotes | 1 | Western | Commonsense |

**Pattern:** The field is rich in Western-centric, English-language benchmarks but severely lacking in culturally diverse, normatively deep, or regulatory-connected evaluations.

### 1.3 Tier 3 — Specialized Domain Benchmarks

From the vault's 989 benchmark candidates (screened from 924 papers with multi-category overlap), organized by cluster:

| Cluster | Representative Benchmarks | Papers in Vault | % of 989 |
|---------|--------------------------|-----------------|-----------|
| Cultural & Cross-Cultural Ethics | Moral Machine, EvalMORAAL, CCD-Bench, NormAd, BBQ family | 497 | 50.3% |
| Fairness, Bias & Social Norms | BBQ (10+ languages), CrowS-Pairs, StereoSet, WinoBias | 448 | 45.3% |
| Helpfulness, Honesty & RLHF | TruthfulQA, FACTOR, RLHF-related | 442 | 44.7% |
| Toxicity, Hate Speech & Harmful Content | ToxiGen, RealToxicityPrompts, HateCheck | 291 | 29.4% |
| Moral Reasoning & Ethical Judgment | ETHICS, MoReBench, MORABLES, TrolleyBench | 248 | 25.1% |
| Safety & Red Teaming | HarmBench, Do-Not-Answer, S-Eval, SafeToolBench | 242 | 24.5% |
| Value Alignment & Value Pluralism | ValueBench, GlobalOpinionQA, Prism | 197 | 19.9% |
| Domain-Specific Ethics | PrinciplismQA, MedEthicsQA, NurValues | 161 | 16.3% |
| Moral Psychology Applied to AI | MoralBench, BenchMoral, PRIME, MFTCXplain | 58 | 5.9% |
| Normative Ethics Benchmarks | ETHICS subsets, CLASH, Jiminy Cricket | 57 | 5.8% |

**Note:** Papers appear in multiple categories (83.4% multi-categorized), reflecting the inherent multi-dimensionality of values alignment.

### 1.4 Meta-Analyses Already in Vault

Five existing meta-analyses provide partial competitive intelligence:

| Meta-Analysis | Year | Scope | Key Finding |
|--------------|------|-------|-------------|
| **Ray 2023** | 2023 | 9 benchmarks + 4 ethical frameworks | First systematic cross-benchmark comparison |
| **Rauh 2024** (Google DeepMind) | 2024 | Gaps in safety evaluation of GenAI | Published `dpmd.ai/EvalsRepo` — 600+ eval resources |
| **Snoswell 2025** | 2025 | 69 LLM ethical evaluation papers | Survey of evaluation methodologies |
| **Rismani 2025** | 2025 | 791 AI ethics evaluation measures | System components mapping to evaluation measures |
| **Gallegos 2024** (ACL) | 2024 | Comprehensive bias & fairness survey | Fair-LLM-Benchmark with taxonomy |

**Gap:** None of these meta-analyses provide a *runnable* evaluation suite. They catalog and classify but don't implement. This is the key strategic opportunity.

### 1.5 Pluralistic Relevance Distribution

Of the 989 benchmark candidates:

| Relevance to Value Pluralism | Count | % |
|------------------------------|-------|---|
| Yes — directly tests pluralistic values | 475 | 48.0% |
| Partial — touches on pluralism tangentially | 177 | 17.9% |
| No — single-perspective evaluation | 107 | 10.8% |
| N/A — not applicable | 230 | 23.3% |

This means **652 papers (65.9%)** have at least partial relevance to value pluralism — a massive, largely untapped resource.

---

## Section 2: Expert 1 — AI Evaluation Researcher

### Technical Architecture Analysis

**What competitors do well:**

1. **HELM** pioneered the multi-metric evaluation paradigm (7 metrics × 42 scenarios), explicitly rejecting single aggregate scores in favor of dimensional transparency. This is the gold standard for evaluation design.
2. **lm-eval's plugin architecture** (Task interface: `doc_to_text` → `doc_to_target` → metrics) enables rapid community contribution. With 65+ values-relevant tasks already integrated, it has the largest existing footprint.
3. **DecodingTrust's [0,100] normalization** per dimension enables clean cross-model comparison while preserving dimensional independence.
4. **Inspect AI's model-graded evaluation** capability is uniquely positioned for moral reasoning tasks that resist MCQ formatting — 29 papers identified as model-graded candidates.

**What's missing architecturally:**

1. **No cross-cultural normalization.** Existing compendia treat all responses against a single cultural baseline. A model that correctly identifies a moral norm in Chinese culture but violates a Western norm (or vice versa) receives the same treatment as one that's simply wrong. No framework adjusts scores for cultural context.

2. **No philosophical dimension decomposition.** HELM has a "fairness" metric but doesn't distinguish virtue-ethical fairness (character-based) from deontological fairness (rights-based) from utilitarian fairness (outcome-based). The CEI vault's 5-framework scoring (virtue, deontological, utilitarian, care, contractarian) across 2,043 papers is architecturally unique.

3. **No value pluralism scoring.** Can the model represent multiple value systems simultaneously? Can it articulate why a Confucian perspective might differ from a Kantian one on the same dilemma? No existing benchmark tests this meta-ethical competence.

4. **No temporal tracking standard.** Model versions change, fine-tuning shifts values, RLHF updates modify alignment — but there is no standardized protocol for tracking value alignment longitudinally across model versions.

5. **No multi-harness orchestration.** Only 1 paper appears in all 4 trackable evaluation frameworks (lm-eval, Inspect, HELM, EleutherAI). The remaining 106 cross-framework papers show severe fragmentation: 9 in EleutherAI+lm-eval, 15 in lm-eval+Inspect, 6 in lm-eval+HELM, 4 in Inspect+HELM. There is no mechanism to run the same benchmark through multiple harnesses and compare.

**CEI architectural advantage:** The vault's eval framework dashboard maps 2,043 papers across 5 harnesses with specific task IDs for 107 papers. This cross-harness mapping is an engineering asset that no competitor possesses.

**Recommendation — Layered Architecture:**

```
Layer 3: Cross-Cultural Weighting System
         └─ Culture-relative scoring, norm referencing, WVS baselines
Layer 2: Multi-Dimensional Scoring Taxonomy
         └─ 5 normative + 8 moral psych + 14 religious + regulatory dimensions
Layer 1: Harness-Agnostic Task Specification
         └─ YAML manifest + JSONL data, convertible to lm-eval/Inspect/HELM/LightEval
```

This architecture separates *what* is evaluated (Layer 1), *how* it's scored (Layer 2), and *relative to whom* it's interpreted (Layer 3).

---

## Section 3: Expert 2 — Moral Philosopher

### Ethical Coverage Analysis

**Well-covered normative traditions (adequate benchmark representation):**

| Tradition | Vault Papers (score ≥ 50) | Key Benchmarks | Assessment |
|-----------|---------------------------|----------------|------------|
| Utilitarianism / Consequentialism | 102 | ETHICS utilitarianism subset, Trolley variants, MACHIAVELLI | **Strong** — multiple MCQ + scenario-based |
| Commonsense morality | ~248 (moral reasoning cluster) | ETHICS (130K+ examples), lm-eval `ethics_cm` task | **Strong** — largest dataset size |
| Bias/fairness as justice | 448 (fairness cluster) | BBQ, CrowS-Pairs, StereoSet, WinoBias | **Strong** — most implemented in harnesses |
| Deontological ethics | 96 | ETHICS deontology subset, CLASH, MoReBench | **Moderate** — datasets exist but thin |

**Moderately covered (benchmarks exist but limited):**

| Tradition | Vault Papers (score ≥ 50) | Key Benchmarks | Assessment |
|-----------|---------------------------|----------------|------------|
| Virtue ethics | 82 | ADEPT, Jiminy Cricket, EudAImonia | **Moderate** — mostly theoretical, few runnable evals |
| Moral Foundations Theory | 59 (mp field) | MoralBench, MFQ-30-LLM, MFTCXplain | **Moderate** — psychometric adaptations available |

**Severely underrepresented (critical gaps):**

| Tradition | Vault Papers (score ≥ 50) | Existing Benchmarks | Gap Severity |
|-----------|---------------------------|---------------------|-------------|
| **Care ethics** | 14 | **None dedicated** | **CRITICAL** — 0.7% of papers, no benchmark |
| **Contractarian ethics** | 17 | **None dedicated** | **CRITICAL** — 0.8% of papers, no Rawlsian/Scanlonian benchmark |
| **Confucian ethics** | 19 (rv field) | CValues (safety-focused only) | **HIGH** — no ren-yi-li evaluation |
| **Ubuntu ethics** | 11 (rv field) | **None** | **HIGH** — no communitarian evaluation |
| **Buddhist ethics** | 10 (rv field) | BuddhismEval (emerging) | **HIGH** — nascent |
| **Islamic ethics** | 83 (rv field) | 1 BERT-based classifier | **HIGH** — content exists, no benchmark |
| **Hindu ethics** | 12 (rv field) | **None** | **HIGH** — dharma/karma absent from evals |

**Three philosophical meta-gaps that no compendium addresses:**

1. **Moral reasoning processes vs. moral judgments.** Virtually all benchmarks test "Is X right/wrong?" (the judgment) rather than "Why is X right, through what inferential steps?" (the reasoning). This conflates moral knowledge with moral competence. A model that memorizes the "right" answer from training data scores identically to one that reasons through ethical principles.

2. **Moral uncertainty expression.** No benchmark tests whether models express appropriate uncertainty on genuinely contested moral questions. A model that says "Trolley problems are trivially resolved by pulling the lever" fails to represent the deep philosophical disagreement this scenario was designed to surface.

3. **Value pluralism competence.** No benchmark tests whether models can articulate multiple ethical perspectives on the same scenario without privileging one. Can a model explain why a utilitarian would pull the lever *and* why a deontologist might not, while acknowledging the legitimacy of both? This meta-ethical skill is arguably the most important for deployment in diverse cultural contexts.

**CEI advantage:** The vault's 5-framework normative scoring (virtue, deontological, utilitarian, care, contractarian) across all 2,043 papers is unique. No other collection maps papers to normative traditions at this granularity. Combined with 14 religious tradition scores and 8 moral psychology dimensions, the CEI vault has the richest ethical metadata of any benchmark registry.

---

## Section 4: Expert 3 — Cross-Cultural Psychologist

### Cultural Diversity Analysis

**Current cross-cultural benchmarks in vault (selected highlights):**

| Benchmark | Year | Cultural Scope | Size | Methodology |
|-----------|------|----------------|------|-------------|
| **Moral Machine** | 2018 | 233 countries, 40M decisions | Gold standard sample size | Trolley-variant crowdsourcing |
| **EvalMORAAL** | 2025 | 55 countries (WVS-based) | WVS-grounded scenarios | Cross-national survey data |
| **CCD-Bench** | 2025 | Cross-cultural conflict dilemmas | 2,182 dilemmas | Conflict scenario generation |
| **BBQ family** | 2022-2025 | 10+ languages | Per-language ~1K MCQ | Translated + culturally adapted |
| **UniMoral** | 2025 | 6 languages (Bengali-grounded) | 8,784 instances | ACL Best Resource — psychologically grounded |
| **GlobalOpinionQA** | 2023 | Multi-country opinion | WVS/Pew-derived | Survey question adaptation |
| **NormAd** | 2024 | Social norm adaptation | Cross-cultural scenarios | Norm-violation detection |

**BBQ language family coverage:**

| Variant | Language | Year | Cultural Adaptation |
|---------|----------|------|---------------------|
| BBQ (original) | English | 2022 | US-centric |
| KoBBQ | Korean | 2023 | Korean social categories |
| JBBQ | Japanese | 2024 | Japanese social categories |
| CBBQ | Chinese | 2024 | Chinese social categories |
| PBBQ | Polish | 2024 | Polish social categories |
| EsBBQ | Spanish | 2024 | Spanish-speaking contexts |
| CaBBQ | Catalan | 2024 | Catalan social categories |
| BasqBBQ | Basque | 2024 | Basque social categories |
| BharatBBQ | Indian languages | 2024 | Indian social categories |
| MBBQ | Multilingual | 2024 | Multi-language compilation |

**Critical cultural gaps:**

1. **Sub-Saharan Africa.** Beyond hate speech datasets (primarily English-language toxicity in African contexts), there are no benchmarks testing Ubuntu/palaver/elder-council moral reasoning traditions. The vault has 11 Ubuntu Philosophy papers but zero runnable benchmarks.

2. **Indigenous worldviews.** No benchmark tests tikanga Maori, Aboriginal Australian law/lore, data sovereignty principles, or relational ontologies. The vault's recent Indigenous Spirituality expansion (30 papers) provides literature but no evaluation instruments.

3. **Latin America.** Only BenchMoral (Spanish MFQ-30 adaptation) exists. No Portuguese-language moral reasoning benchmark. No evaluation of liberation theology perspectives or Latin American communitarian ethics.

4. **South/Southeast Asia.** Thai, Vietnamese, Myanmar, and Filipino moral reasoning traditions are entirely unrepresented in benchmarks despite significant AI deployment in these markets.

5. **Middle East and North Africa.** Despite 83 Islam-related papers in the vault, only one BERT-based classifier exists. No benchmark tests Islamic jurisprudential reasoning (fiqh), Quranic ethical principles, or maqasid al-shariah.

**Fundamental methodological flaw across the field:**

Most "multilingual" benchmarks are translation-based — English moral scenarios translated into target languages. This embeds Western moral framing into non-Western linguistic contexts. A translated trolley problem still assumes Western individualist moral intuitions even when presented in Bengali or Swahili. True cross-cultural evaluation requires *culturally native scenario generation* — scenarios originating from within each moral tradition, not translated from without.

**CEI advantage:** The vault contains 497 cross-cultural papers (the LARGEST category at 50.3% of candidates), with systematic `cultures_nationalities_list` metadata covering 98 unique culture/nationality values, `languages_list` metadata, and religious values scoring across 14 traditions. Combined with Tapestry's 1,405 governance statements from ~1,735 organizations worldwide spanning 13+ document languages, this provides the richest cultural mapping of any benchmark collection.

---

## Section 5: Expert 4 — NLP/ML Benchmarking Expert

### Implementability Analysis

**Current implementability landscape across 5 evaluation frameworks:**

| Framework | Already In | Ready (score ≥ 60) | Needs Dataset Work | Needs More Info | Not Implementable | Total Viable |
|-----------|-----------|---------------------|-------------------|-----------------|-------------------|-------------|
| **lm-eval** | 65 | 178 | 413 | 580 | 754 | **656** |
| **Inspect** | 38 | 23 | 483 | 695 | 775 | **90** (high-confidence) |
| **HELM** | 19 | — | — | — | — | **19** (tracked) |
| **EleutherAI** | 22 | — | — | — | — | **22** (tracked) |
| **LightEval** | 0 tracked | 99 | 771 | — | — | **870** (estimated) |
| **OpenAI Evals** | 0 tracked | 783 | 872 | — | — | **1,655** (estimated) |

**Cross-framework overlap (the fragmentation problem):**

| Overlap | Papers |
|---------|--------|
| In ≥ 1 framework | 107 |
| In ≥ 2 frameworks | ~30 |
| In all 4 trackable | **1** |
| lm-eval + Inspect | 15 |
| lm-eval + HELM | 6 |
| EleutherAI + lm-eval | 9 |
| Inspect + HELM | 4 |

This extreme fragmentation means evaluators using different harnesses get fundamentally different pictures of model alignment. A model evaluated only on HELM's 19 values-relevant tasks sees a tiny fraction of the landscape compared to lm-eval's 65.

**Practical barriers to integration:**

1. **Data format heterogeneity.** The 989 candidates span MCQ, free-text generation, classification, pairwise comparison, multi-turn dialogue, game-based, and human-in-the-loop formats. No single harness handles all formats natively.

2. **Licensing fog.** Less than 60% of the 160 `is_benchmark: true` papers have clear open-source licensing documentation. Many datasets are "available on request" or hosted on platforms with ambiguous terms.

3. **Scorer complexity.** Moral reasoning evaluation resists simple string matching. Many tasks require model-graded evaluation (Inspect's strength, with 29 identified candidates) or human judgment.

4. **Dataset size mismatch.** From 100 prompts (SimpleSafetyTests) to 40M decisions (Moral Machine) — normalizing scores across 5 orders of magnitude of dataset size is a statistical challenge.

**Realistic integration timeline (of 989 candidates):**

| Timeline | Count | % | Criteria |
|----------|-------|---|----------|
| 6 months | 120-150 | 12-15% | MCQ format, public data, clear metrics, existing harness support |
| 12 months | 250-300 | 25-30% | Format conversion needed, dataset hosting required |
| 18 months | 200-250 | 20-25% | Custom scorer development, model-graded evaluation |
| Fundamental barriers | 300-350 | 30-35% | No public data, human-in-loop, proprietary APIs, no reproducibility |

**Top "ready to implement" candidates (lm-eval score = 100):**
- FrenchBench, DecodingTrust, SEACrowd, AraDiCE, AfriMed-QA, INCLUDE, TMMLU+, Social Norms Dataset

**Top "ready to implement" candidates (Inspect score ≥ 60):**
- 2024-Yuan-Social (80), AfriMed-QA (69), WenMind (68), TMLU (67) — 23 total at ≥ 60

**CEI advantage:** Per-paper implementability scores across 5 frameworks with specific task ID mappings — this is a unique engineering asset. No other registry provides "which benchmarks can you actually run today, on which harness, and what's the gap?"

---

## Section 6: Expert 5 — AI Safety/Policy Researcher

### Regulatory Relevance Analysis

**Regulatory coverage gaps in existing compendia:**

| Regulatory Requirement | HELM | DecodingTrust | TrustLLM | Any Compendium? | CEI Vault Coverage |
|------------------------|------|---------------|----------|-----------------|-------------------|
| **EU AI Act Art. 10** (non-discrimination/bias) | Partial | Yes | Partial | Yes | **Strong** (448 papers) |
| **EU AI Act Art. 13** (transparency) | No | No | Partial | Weak | Moderate |
| **EU AI Act Art. 14** (human oversight) | No | No | No | **No** | Limited |
| **EU AI Act Art. 15** (robustness/accuracy) | Yes | Yes | Yes | Yes | Strong |
| **EU AI Act Art. 27** (fundamental rights impact) | No | No | No | **No** | Via Tapestry |
| **NIST AI RMF — Govern** | No | No | No | Rismani 2025 only | Strong (791 measures) |
| **NIST AI RMF — Map** | No | No | No | **No** | Via vault metadata |
| **NIST AI RMF — Measure** | Partial | Partial | Partial | Partial | Strong (989 candidates) |
| **NIST AI RMF — Manage** | No | No | No | **No** | Via Tapestry |
| **Cultural sensitivity requirements** | No | No | No | **No** | **497 papers** |
| **Domain-specific ethics** (healthcare, finance) | No | No | No | **No** | **161 papers** |
| **National AI strategy alignment** | No | No | No | **No** | **Tapestry (1,405 statements)** |

**Key regulatory trends creating demand for values-alignment evaluation:**

1. **EU AI Act (effective 2025-2027):** High-risk AI systems must demonstrate non-discrimination, transparency, and fundamental rights compliance. No existing compendium provides a complete technical evaluation mapping to these requirements.

2. **NIST AI RMF:** The "Measure" function explicitly calls for bias and fairness evaluation, but the mapping from specific benchmarks to RMF subcategories is incomplete. Rismani 2025 mapped 791 measures but not to specific runnable benchmarks.

3. **National AI strategies:** 100+ countries have published AI strategies (tracked in Tapestry), many with explicit values requirements. No technical evaluation suite connects these policy statements to benchmark evaluations.

4. **Sector-specific regulation:** Healthcare AI, financial AI, and educational AI face domain-specific ethical requirements. The vault's 161 domain-specific ethics papers are the only systematic collection.

**CEI advantage:** Tapestry provides the governance-to-benchmark bridge — mapping what regulators require to what benchmarks measure. With 1,405 governance statements from ~1,735 organizations across 13+ document languages, Tapestry is the only resource that connects AI governance principles to technical evaluation across jurisdictions. No competitor has this asset.

---

## Section 7: Expert 6 — Psychometrician

### Measurement Quality Analysis

**Psychometric rigor spectrum across existing benchmarks:**

| Tier | Benchmarks | Characteristics |
|------|-----------|-----------------|
| **Strong** | ValueBench (44 validated inventories), MFQ adaptations (known reliability), EvalMORAAL (WVS-grounded), Moral Machine (40M sample) | Based on validated psychometric instruments, known reliability/validity, large sample sizes |
| **Moderate** | DecodingTrust, TrustLLM, HELM Safety | Systematic construction, some validation, but not grounded in psychometric theory |
| **Weak** | ETHICS (ad hoc construction), most safety benchmarks (binary pass/fail) | No documented reliability, variable annotator agreement, no construct validation |

**Five critical measurement concerns:**

**1. Construct validity crisis.** MCQ correctness ≠ deployment behavior. A model that selects "It is wrong to steal" on a multiple-choice test may still generate text endorsing theft in creative writing contexts. No existing benchmark bridges this gap between controlled test performance and real-world behavioral alignment.

**2. Annotator bias encoding.** Human annotators embed their own cultural and philosophical perspectives into "ground truth" labels. A US-based annotator pool produces US-normative labels. This is not acknowledged or corrected in most benchmarks, meaning the evaluation itself enforces cultural hegemony.

**3. Score aggregation invalidity.** Aggregating scores across sub-benchmarks without a validated latent factor model is statistically inappropriate. HELM's refusal to produce a single aggregate score is methodologically correct. Competitors that *do* aggregate (DecodingTrust's dimension scores, TrustLLM's trustworthiness index) lack factor-analytic validation that the dimensions are actually independent.

**4. Test-retest instability.** LLM outputs vary with temperature, prompt phrasing, system prompt, and even token ordering. A model's "fairness score" may shift 10-20 points based on evaluation-irrelevant parameters. Few benchmarks report reliability coefficients or confidence intervals.

**5. Ecological validity gap.** Controlled MCQ scenarios bear little resemblance to real deployment contexts — multi-turn conversations, ambiguous user intents, conflicting value signals, time pressure, and incomplete information. No benchmark tests values alignment under realistic deployment conditions.

**Recommendations for CEI assessment design:**

- **Multi-method assessment:** Combine MCQ (knowledge), generation (application), dialogue (interactive), and adversarial (robustness) evaluation modes for each value dimension
- **Reliability metrics:** Report Cronbach's alpha or test-retest reliability for every sub-benchmark
- **Factor-analytic validation:** Before aggregating scores, validate that dimensions are empirically distinguishable
- **Culture-specific norm referencing:** Score models against culture-appropriate baselines, not a single universal standard
- **Confidence intervals:** Report score ranges, not point estimates, given LLM stochasticity

---

## Section 8: Expert 7 — Strategic Positioning Analyst

### White Space & Differentiation Analysis

**The white space — what NO existing compendium does:**

1. **Cross-cultural values alignment** (not just cross-lingual capability) — evaluating whether a model can navigate value pluralism across cultures
2. **Normative philosophical depth** (beyond "commonsense morality") — decomposing ethical evaluation along philosophical traditions
3. **Multi-harness implementability** (not locked to one framework) — enabling evaluation on any preferred harness
4. **Governance-to-benchmark bridge** (connecting regulatory norms to technical evaluation) — the "so what?" for compliance teams

**Competitive comparison matrix:**

| Dimension | HELM | DecodingTrust | TrustLLM | ValueBench | ETHICS | **CEI (proposed)** |
|-----------|------|---------------|----------|------------|--------|-------------------|
| Benchmark breadth | 42 scenarios | 8 dimensions | 30+ tasks | 44 inventories | 5 domains | **989 candidates** |
| Cultural coverage | Minimal | None | None | Western | Western | **98 culture values, 40+ languages** |
| Normative depth | Low | Low | Low | Medium | Medium | **High (5+8+14 dims)** |
| Psychometric validity | Medium | Medium | Low | **High** | Low | Medium (inherited) |
| Harness compatibility | HELM only | Standalone | Standalone | Standalone | lm-eval | **5 harnesses mapped** |
| Regulatory mapping | None | None | None | None | None | **EU AI Act + NIST + national** |
| Governance connection | None | None | None | None | None | **Tapestry (1,405 statements)** |
| Open data | Partial | Yes | Yes | Yes | Yes | **~47% public, growing** |
| Community contribution | Moderate | Low | Low | Low | Low | **High (lm-eval plugin model)** |

**Competitive risks to monitor:**

1. **Stanford CRFM expanding HELM Safety.** HELM Safety v1.0 already incorporates BBQ, HarmBench, XSTest, and others. Stanford has the engineering resources and academic credibility to expand into values territory. CEI must differentiate on depth (normative philosophy, cultural diversity) rather than competing on breadth alone.

2. **MLCommons AILuminate.** Industry standardization of AI safety benchmarks could render academic compendia irrelevant for commercial use. CEI should position as complementary (providing the academic rigor and cultural depth that industry standards lack).

3. **"Benchmark fatigue."** The field is experiencing benchmark proliferation fatigue. Another compendium risks being ignored. CEI must position as *infrastructure* (registry + orchestration) rather than *yet another benchmark suite*.

4. **Engineering scale.** Converting 989 candidates → runnable evaluations requires significant software engineering resources beyond the research team's current capacity. Phased rollout with community contribution model is essential.

5. **Cultural authority.** Creating benchmarks for non-Western moral traditions requires deep partnership with scholars *from* those traditions. Western researchers creating "Ubuntu ethics benchmarks" risks academic colonialism.

---

## Section 9: Strategic Recommendations & Roadmap

### 9.1 Recommended Positioning

**Position as infrastructure, not competitor.** Three pillars:

1. **Meta-Benchmark Registry** — The authoritative, searchable catalog of what values-alignment benchmarks exist, what they measure, and how they compare. Think "benchmark Wikipedia" with structured metadata.

2. **Cross-Harness Orchestration Layer** — Run the same model through diverse evaluations using any preferred harness. The only resource that bridges lm-eval ↔ Inspect ↔ HELM ↔ LightEval ↔ OpenAI Evals for values alignment.

3. **Governance-to-Benchmark Bridge** — The only resource connecting AI governance principles (via Tapestry) to technical evaluation (via the vault). Answers: "My model needs to comply with EU AI Act Art. 10 — which benchmarks should I run?"

### 9.2 Proposed Name

**CEI Values Alignment Compass (VAC)**

The "compass" metaphor echoes navigation through a normative landscape — helping developers orient their models relative to diverse value systems. The acronym is clean, and the framing emphasizes guidance over judgment.

### 9.3 Phased Implementation Roadmap

#### Phase 1: Registry & Taxonomy (Months 1-3)

| Deliverable | Description | Builds On |
|-------------|-------------|-----------|
| Benchmark Registry Website | Public, searchable database of 989 candidates with normative/cultural/regulatory metadata | Existing 21 dashboards, eval framework dashboard |
| Implementability Matrix | Cross-framework viability scores for all candidates | lm-eval, Inspect, HELM integration reports |
| Taxonomy Specification | Formal schema for values-alignment benchmark metadata | Vault's existing YAML schema |
| Gap Analysis Report | Formal publication of this competitive analysis | This document |

**Resources:** 1-2 researchers, 1 web developer, 3 months
**Risk:** Low — builds entirely on existing vault assets

#### Phase 2: Core Evaluation Suite (Months 4-8)

| Deliverable | Description | Target Size |
|-------------|-------------|-------------|
| CEI VAC v1.0 | Runnable evaluation suite in lm-eval + Inspect | 50-80 benchmarks |
| Gap-filling benchmarks | New benchmarks for care ethics, contractarian, non-Western | 10-15 new |
| Cross-harness converter | Tool to translate task specs between harnesses | 5 harness targets |

**Benchmark selection criteria:**
- Priority 1: Already in harness (65 lm-eval + 38 Inspect) — validate and curate
- Priority 2: Ready to implement (178 lm-eval + 23 Inspect) — highest-score first
- Priority 3: Gap-filling — commission or adapt benchmarks for care ethics, contractarian ethics, non-Western traditions

**Resources:** 2-3 researchers, 2 ML engineers, 5 months
**Risk:** Medium — engineering scale, but building on known-viable candidates

#### Phase 3: Cross-Cultural Expansion (Months 9-14)

| Deliverable | Description | Target Cultures |
|-------------|-------------|-----------------|
| CEI VAC v2.0 | Culturally-native benchmarks for 5 underserved regions | Sub-Saharan Africa, Latin America, South Asia, Southeast Asia, Indigenous |
| Culture-relative scoring | WVS-based + Tapestry-derived cultural baselines | 20+ cultural contexts |
| Partnership network | Collaborations with non-Western ethics scholars | 10+ institutional partners |

**Critical requirement:** Culturally-native benchmarks must be developed *with* scholars from each tradition, not *about* those traditions by Western researchers. This requires partnership-building time.

**Resources:** 5-7 researchers (including cultural experts), 2 ML engineers, 6 months
**Risk:** High — requires international partnerships, cultural sensitivity, longer timelines

#### Phase 4: Regulatory Compliance Layer (Months 15-20)

| Deliverable | Description | Target Jurisdictions |
|-------------|-------------|---------------------|
| Compliance Scoring Profiles | Jurisdiction-specific evaluation configurations | EU, US, China, India, Australia, Brazil |
| Benchmark-to-Regulation Mapping | Formal mapping of benchmarks to regulatory articles | EU AI Act, NIST AI RMF, national strategies |
| CEI Compliance Evaluation Toolkit | End-to-end compliance evaluation workflow | 6 jurisdictions |

**Resources:** 2-3 policy researchers, 1-2 ML engineers, 6 months
**Risk:** Medium — regulatory landscape shifting, but Tapestry provides stable foundation

### 9.4 Success Metrics

| Metric | Phase 1 Target | Phase 2 Target | Phase 4 Target |
|--------|---------------|---------------|---------------|
| Registry entries | 989 | 1,200+ | 1,500+ |
| Runnable benchmarks | 0 (registry only) | 50-80 | 150-200 |
| Cultural contexts | 98 (existing) | 98 | 120+ |
| Harnesses supported | 5 (mapped) | 2 (running) | 5 (running) |
| Regulatory mappings | 0 | 0 | 6 jurisdictions |
| Community contributors | 0 | 10-20 | 50+ |
| Citations | — | 10+ | 50+ |

### 9.5 Key Dependencies & Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Stanford expands HELM Safety into values | High | High | Differentiate on cultural depth + governance bridge |
| Benchmark fatigue in field | High | Medium | Position as infrastructure, not another suite |
| Engineering resource constraints | High | High | Phased rollout, community contribution model |
| Cultural authority challenges | Medium | High | Partnership-first approach, avoid "safari research" |
| Regulatory landscape shifts | Medium | Medium | Tapestry tracks changes continuously |
| Data licensing barriers | Medium | Medium | Focus on clearly-licensed datasets first |

---

## Appendix A: Vault Coverage Summary Statistics

| Dimension | Count | Source |
|-----------|-------|--------|
| Total papers | 2,043 | `papers/` directory |
| Benchmark candidates | 989 | Benchmark survey (multi-category) |
| Papers in ≥ 1 eval framework | 107 | Cross-framework comparison |
| Papers in all 4 frameworks | 1 | Cross-framework comparison |
| Unique cultures/nationalities | 98 | `cultures_nationalities_list` field |
| Religious traditions scored | 14 + derived fields | `rv_*` score fields |
| Moral psychology dimensions | 8 + derived fields | `mp_*` score fields |
| Normative ethics frameworks | 5 | `virtue/deontological/utilitarian/care/contractarian_ethics` |
| Tapestry statements | 1,405 | CEI-AI-Statements vault |
| Tapestry organizations | ~1,735 | CEI-AI-Statements vault |
| Governance document languages | 13+ | CEI-AI-Statements vault |

## Appendix B: Papers with is_benchmark = true by Ethics Score

| Ethics Score Range | Benchmark Papers | % of Benchmarks |
|-------------------|-----------------|-----------------|
| ≥ 80 | — | — |
| 50-79 | — | — |
| 20-49 | — | — |
| 0-19 | — | — |

*(Detailed breakdown available in companion data file.)*

## Appendix C: Data Availability of Benchmark Candidates

| Availability | Count | % of 989 |
|-------------|-------|----------|
| Public | 468 | 47.3% |
| Code available | 18 | 1.8% |
| Not stated | 197 | 19.9% |
| N/A | 230 | 23.3% |
| Restricted | 5 | 0.5% |
| Unknown | 71 | 7.2% |

---

*Report generated 2026-03-15 from CEI Literature Vault (2,043 papers, 989 benchmark candidates).*
*Companion data: `20260315-values-alignment-benchmark-data.json`*
