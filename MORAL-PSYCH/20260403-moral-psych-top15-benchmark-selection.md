# Moral Psychology Benchmarks for LLM Values Alignment: Top-15 Selection Report

**Date:** 2026-04-03
**Methodology:** 9-member virtual expert council, 28-feature characterization framework, 50/30/20 composite scoring
**Candidate pool:** 222 papers extracted from 2,046 vault papers, 40 assessed in depth, 38 passed hard gates

---

## Executive Summary

This report identifies and ranks the 15 most important moral psychology benchmarks for evaluating LLM values alignment. From a vault of 2,046 AI ethics papers, we extracted 222 candidates using multi-signal detection (mp_* scores, benchmark/eval/dataset flags, keyword matching, and known benchmark names). A virtual expert council of 9 perspectives assessed the top 40 candidates across 28 features in 4 tiers, producing composite scores with 50% weight on psychological depth, 30% on practical ease, and 20% on citation impact.

### Key Findings

1. **MFT dominance:** Moral Foundations Theory accounts for 4 of the top 15 and 68 of 222 candidates. It is the most operationalized moral psychology theory in NLP.
2. **Trolley/Moral Machine is the most practically implementable:** The Moral Machine family scores highest on composite due to massive scale (40M decisions), cross-cultural validation (233 countries), and forced-choice format ideal for LLMs.
3. **Kohlberg's DIT is underappreciated:** Three DIT-based papers score high on psychological depth (PD=80) but low on practical ease because the DIT uses only 9 dilemmas requiring complex scenario-ranking.
4. **Critical gap — no LLM benchmarks exist for 3 of 8 moral psychology theories:** Dual Process Theory (Joshua Greene), Social Intuitionism (Haidt), and Dyadic Morality (Kurt Gray) have zero dedicated LLM benchmarks. This represents a major blind spot in the field.
5. **Psychometric validity varies enormously:** A6 scores range from 1-5. Only 4 papers (10%) have multi-study validated instruments. Most LLM benchmarks (A6=2-3) adapt psychology instruments without revalidation.
6. **Most benchmarks require model-graded or psychometric scoring** (not simple exact match), making Inspect AI the natural harness (model_graded_qa).

---

## Methodology

### Expert Council (9 Perspectives)

| # | Perspective | Assessment Focus |
|---|------------|-----------------|
| 1 | Moral Psychology (MFT Specialist) | Theory fidelity, operationalization depth |
| 2 | Developmental Psychology (Kohlberg/Piaget) | Stage theory validity, developmental sensitivity |
| 3 | Psychometrics & Measurement Science | Construct validity, reliability, source instruments |
| 4 | NLP Evaluation Specialist | Harness compatibility, scorer types, format suitability |
| 5 | Cross-Cultural Moral Psychology | WEIRD bias, multilingual coverage, cultural universality |
| 6 | AI Safety & Alignment | Deployment relevance, actionability for safety decisions |
| 7 | Bibliometrics & Impact | Citation counts, venue tiers, downstream adoption |
| 8 | Reproducibility & Data Engineering | Data access, code quality, implementation effort |
| 9 | Survey Methodology (PRISMA) | Search protocol exhaustiveness, inclusion/exclusion criteria |

### Scoring Framework

**Tier A — Psychological Depth (50% weight)**
- A1: Theories engaged (0-8 theories → 0-100)
- A2: Construct operationalization {Validated=100, Theory-derived=70, Theory-inspired=40, Keyword-only=10}
- A3: Measurement target (default 70)
- A4: Source instrument {Validated=100, Original=80, None=0}
- A5: Human baseline {Published norms=100, Paper-specific=70, Partial=40, No=0}
- A6: Construct validity evidence {5=100, 4=75, 3=50, 2=30, 1=10}

**Tier B — Practical Ease (30% weight)**
- B1: Task format (MCQ=100 → Game-based=15)
- B2: Dataset size (log-scaled, >20K=100)
- B3: Data availability (HuggingFace=100, GitHub=95, OSF=90)
- B6/B7: Harness implementability (from eval dashboard v4)
- B10: LLM administration fidelity (Direct=100 → Paradigm change=10)

**Tier C — Citation Impact (20% weight)**
- C1: Raw citation count (log-scaled)
- C2: Age-normalized citation rate
- C3: Venue tier (1-4)
- C5: Hub/leaderboard presence

**Hard gates:** PD >= 40 AND data publicly available
**Diversity constraints:** >= 3 MFT, >= 2 Schwartz, >= 2 Trolley, >= 1 Kohlberg, >= 1 non-English, caps of 3 Trolley and 4 MFT to prevent over-representation

---

## Top 15 Benchmarks

### #1. The Moral Machine Experiment (Awad et al., 2018)
- **Composite: 78.5** | PD=76 | PE=74 | CI=93
- **Theory:** Trolley/Dilemmas
- **Source instrument:** Original (Moral Machine platform)
- **Format:** Forced-choice (binary preference between two outcomes)
- **Size:** 40,000,000 decisions from 233 countries
- **Languages:** 10 (English, French, German, Portuguese, Spanish, Chinese, Japanese, Korean, Russian, Arabic)
- **Construct validity:** A6=5 (multi-study validated, massive cross-cultural replication)
- **Human baseline:** Published norms (Nature 2018, 40M responses)
- **Data:** https://goo.gl/JXRrBP
- **Citations:** 1,478
- **LLMs tested:** Not originally tested on LLMs, but adapted by Takemoto (2024) and others
- **Why #1:** The gold standard for cross-cultural moral preference data. Forced-choice format is trivially administerable to LLMs. The massive human baseline enables direct comparison of LLM moral preferences against population-level human preferences across cultures.

### #2. The Moral Machine Experiment on LLMs (Takemoto, 2024)
- **Composite: 69.9** | PD=73 | PE=70 | CI=64
- **Theory:** Trolley/Dilemmas
- **Source instrument:** Moral Machine scenarios
- **Format:** Forced-choice
- **Size:** 50,000 scenarios
- **Construct validity:** A6=4
- **Human baseline:** Published norms (from Awad 2018)
- **Data:** https://doi.org/10.5061/dryad.d7wm37q6v
- **Citations:** 51
- **LLMs tested:** GPT-3.5, GPT-4, Llama-2, PaLM-2
- **Why #2:** The direct LLM adaptation of the Moral Machine. Demonstrated that LLMs show systematic moral preferences that differ from human population averages, with significant model-to-model variation.

### #3. Crowdsourcing Moral Machines (Awad et al., 2020)
- **Composite: 69.9** | PD=73 | PE=67 | CI=67
- **Theory:** Trolley/Dilemmas
- **Source instrument:** Moral Machine
- **Format:** Forced-choice
- **Size:** 40,000,000 (shared platform)
- **Languages:** 10
- **Construct validity:** A6=4
- **Data:** https://moralmachine.mit.edu
- **Citations:** 55
- **Why #3:** The design methodology paper for crowdsourcing moral dilemma data at scale. Provides the theoretical framework for why forced-choice dilemmas work as a measurement instrument.

### #4. Moral Foundations Twitter Corpus — MFTC (Hoover et al., 2020)
- **Composite: 68.1** | PD=68 | PE=66 | CI=72
- **Theory:** Moral Foundations Theory (MFT)
- **Source instrument:** MFT annotation scheme (expert-coded)
- **Format:** Multi-label classification (10 labels: 5 foundations x virtue/vice)
- **Size:** 35,108 tweets across 7 domains
- **Construct validity:** A6=4 (expert annotation, inter-rater reliability reported)
- **Human baseline:** Paper-specific (expert annotations)
- **Data:** https://osf.io/ezn37/
- **Citations:** 198
- **LLMs tested:** Not originally tested on LLMs, but widely used since
- **Why #4:** The largest expert-annotated MFT dataset. Tests whether LLMs can classify moral foundation expressions in real-world text — a prerequisite for understanding LLM moral reasoning.

### #5. Does Moral Code Have a Moral Code? (Fraser et al., 2022)
- **Composite: 66.3** | PD=72 | PE=59 | CI=63
- **Theory:** MFT + Schwartz
- **Source instrument:** MFQ + Schweder's Big Three + Oxford Utilitarianism Scale
- **Format:** Binary + MCQ
- **Size:** ~100 items
- **Construct validity:** A6=3 (adapts multiple validated instruments)
- **Human baseline:** Published norms (from source instruments)
- **Data:** https://delphi.allenai.org/
- **Citations:** 42
- **LLMs tested:** Delphi
- **Why #5:** Uniquely combines multiple moral psychology frameworks (MFQ, Big Three, Utilitarianism Scale) in a single evaluation. Tests multi-framework moral alignment.

### #6. Do Moral Judgment and Reasoning Capability... (Khandelwal et al., 2024)
- **Composite: 66.0** | PD=80 | PE=54 | CI=49
- **Theory:** Kohlberg (Cognitive Developmental)
- **Source instrument:** DIT (Defining Issues Test)
- **Format:** Scenario rating + ranking
- **Size:** 9 dilemmas x 6 languages
- **Languages:** English, Chinese, Hindi, Russian, Spanish, Swahili
- **Construct validity:** A6=4 (validated DIT with cross-cultural adaptation)
- **Human baseline:** Published norms (DIT norms spanning 40 years)
- **Data:** Published in EACL 2024
- **Citations:** 14
- **LLMs tested:** ChatGPT, GPT-4, Llama-2
- **Why #6:** The only cross-cultural Kohlberg benchmark. Tests whether LLMs show different moral development stages across languages — a critical question for multilingual deployment.

### #7. Moral Foundations Vignettes — MFV (Clifford et al., 2015)
- **Composite: 64.5** | PD=83 | PE=56 | CI=31
- **Theory:** Moral Foundations Theory (MFT)
- **Source instrument:** Original instrument (MFV), designed as a complement to MFQ
- **Format:** Scenario rating (moral wrongness judgments)
- **Size:** 132 vignettes, 6 per foundation x 5 foundations x ~4 scenarios
- **Construct validity:** A6=5 (multi-study validated: 4 studies, convergent validity with MFQ)
- **Human baseline:** Published norms (Psychological Assessment 2015)
- **Data:** Published with paper
- **Citations:** 14 (in S2; actual citations much higher in psychology)
- **Why #7:** The most psychometrically rigorous MFT instrument. Each vignette is a carefully controlled scenario manipulating exactly one foundation. The gold standard for testing whether LLMs differentiate between moral foundations.

### #8. Moral Foundations of Large Language Models (Abdulhai et al., 2024)
- **Composite: 63.8** | PD=85 | PE=63 | CI=13
- **Theory:** Moral Foundations Theory (MFT)
- **Source instrument:** MFQ-30 (Moral Foundations Questionnaire)
- **Format:** Likert scale (6-point agreement)
- **Size:** 30 items
- **Construct validity:** A6=5 (directly administers the validated MFQ-30)
- **Human baseline:** Published norms (extensive MFQ norms from moralsoundations.org)
- **Data:** https://github.com/abdulhaim/moral_foundations_llms
- **LLMs tested:** ChatGPT, GPT-3, PaLM
- **Why #8:** The highest psychological depth score (PD=85) in the entire pool. Directly administers the MFQ-30 to LLMs without modification, enabling direct comparison against decades of human MFQ data. Found that LLMs show distinct moral foundation profiles that shift with prompting.

### #9. Probing the Moral Development of LLMs via DIT (Tanmay et al., 2023)
- **Composite: 63.2** | PD=80 | PE=54 | CI=35
- **Theory:** Kohlberg (Cognitive Developmental)
- **Source instrument:** DIT (Defining Issues Test)
- **Format:** Scenario rating + ranking
- **Size:** 9 dilemmas
- **Construct validity:** A6=4
- **Human baseline:** Published norms
- **Data:** Published with paper
- **Citations:** 31
- **LLMs tested:** ChatGPT, GPT-3, GPT-3.5, GPT-4, Llama-2, PaLM
- **Why #9:** The pioneering DIT-on-LLMs paper. Demonstrated that LLMs perform at "post-conventional" Kohlberg stage — potentially reflecting training data bias toward educated/liberal moral reasoning rather than genuine moral development.

### #10. Value Kaleidoscope / ValuePrism (Sorensen et al., 2024)
- **Composite: 61.6** | PD=56 | PE=70 | CI=65
- **Theory:** Schwartz (Value Pluralism)
- **Source instrument:** Novel framework (inspired by Schwartz + pluralistic values)
- **Format:** Free-text generation + MCQ
- **Size:** 218,000 values from 31,000 situations
- **Construct validity:** A6=3
- **Human baseline:** Paper-specific (crowdsourced annotations)
- **Data:** https://huggingface.co/datasets/allenai/ValuePrism
- **Citations:** 101
- **LLMs tested:** Flan-T5, GPT-4
- **Why #10:** The largest values dataset on HuggingFace. Maps a vast space of situational values rather than relying on fixed psychometric items. Tests value pluralism — whether LLMs can recognize that different values can legitimately conflict.

### #11. Multilingual Defining Issues Test (Khandelwal et al., 2024)
- **Composite: 61.2** | PD=80 | PE=54 | CI=25
- **Theory:** Kohlberg (Cognitive Developmental)
- **Source instrument:** DIT
- **Format:** Scenario rating + ranking
- **Size:** 9 dilemmas x 6 languages
- **Languages:** English, Chinese, Hindi, Russian, Spanish, Swahili
- **Construct validity:** A6=4
- **Data:** EACL 2024
- **Why #11:** The multilingual extension of the DIT. Tests cross-lingual consistency of moral reasoning stages. (Note: Related to #6; this is the primary publication in EACL.)

### #12. Assessing LLMs for Moral Value Pluralism (Benkler et al., 2023)
- **Composite: 55.6** | PD=68 | PE=47 | CI=40
- **Theory:** Schwartz (World Values Survey)
- **Source instrument:** World Values Survey (WVS)
- **Format:** Free-text + automated scoring
- **Size:** 5 core WVS questions
- **Construct validity:** A6=3 (adapts validated WVS items)
- **Human baseline:** Published norms (WVS has 40 years of global data)
- **Data:** Published with paper
- **Citations:** 39
- **LLMs tested:** GPT-3
- **Why #12:** Directly connects LLM evaluation to the most widely used cross-cultural values survey in social science. The WVS has population-level data from 100+ countries, enabling principled comparison.

### #13. How Can a Deontological Decision Lead to Moral Satisfaction... (Xu & Ma, 2016)
- **Composite: 55.2** | PD=76 | PE=46 | CI=18
- **Theory:** Moral Identity
- **Source instrument:** Moral Identity Scale (Aquino & Reed, 2002) + Ethical Predisposition Measure
- **Format:** Likert + behavioral task
- **Size:** 250 participants, multiple scales
- **Construct validity:** A6=4
- **Human baseline:** Paper-specific
- **Cultural provenance:** Non-Western (Chinese)
- **Languages:** Chinese
- **Why #13:** The only Moral Identity benchmark in the top 15. Operationalizes Aquino & Reed's moral identity construct, testing the self-importance of moral traits. Provides the non-WEIRD perspective that most MFT and trolley benchmarks lack.

### #14. CVC — Chinese Values Corpus (Wu et al., 2025)
- **Composite: 52.8** | PD=51 | PE=74 | CI=26
- **Theory:** Chinese moral norms (adapted from Social Chemistry 101 + MIC)
- **Source instrument:** Novel framework (Chinese values)
- **Format:** MCQ + scenario generation
- **Size:** 250,000 items
- **Construct validity:** A6=3
- **Human baseline:** Paper-specific
- **Cultural provenance:** Non-Western (Chinese)
- **Languages:** Chinese
- **Data:** https://huggingface.co/datasets/Beijing-AISI/C-VARC
- **LLMs tested:** Claude, DeepSeek, Gemini, GPT-4o, Llama-3, Qwen
- **Why #14:** The largest non-Western moral benchmark (250K items). Tests whether values alignment transfers across cultural contexts. Critical for evaluating LLMs deployed in Chinese-speaking markets.

### #15. Concerns and Values in Human-Robot Interactions (Abbo et al., 2025)
- **Composite: 36.1** | PD=41 | PE=40 | CI=18
- **Theory:** Schwartz
- **Source instrument:** Novel HRI value taxonomy
- **Format:** Design tool (not standard benchmark format)
- **Construct validity:** A6=2
- **Why #15:** Weakest entry. Included to meet Schwartz diversity minimum. Future work should replace this with a dedicated Schwartz PVQ-40 benchmark for LLMs if one emerges from the gap analysis.

---

## Theory Coverage Analysis

| Theory | Papers in Top 15 | Papers in Vault (mp_* >= 50) | Gap Status |
|--------|-----------------|------------------------------|------------|
| Moral Foundations Theory (MFT) | 4 (#4, #5, #7, #8) | 68 | Well-covered |
| Schwartz/Values | 4 (#5, #10, #12, #15) | 52 | Covered but no PVQ-40 benchmark |
| Trolley/Dilemmas | 3 (#1, #2, #3) | 36 | Well-covered |
| Kohlberg/Developmental | 3 (#6, #9, #11) | 19 | Covered via DIT |
| Moral Identity | 1 (#13) | 7 | Thin coverage |
| Social Intuitionism | 0 | 1 | **CRITICAL GAP** |
| Dyadic Morality | 0 | 3 | **CRITICAL GAP** |
| Dual Process Theory | 0 | 0 | **CRITICAL GAP** |

### Critical Gaps

Three of eight tracked moral psychology theories have **zero dedicated LLM benchmarks:**

1. **Dual Process Theory** (Joshua Greene): The theory that moral judgments arise from competition between automatic emotional responses (System 1) and deliberate utilitarian reasoning (System 2). No LLM benchmark tests whether models show the dual-process signature — e.g., different response patterns under time pressure vs. reflection.

2. **Social Intuitionist Model** (Jonathan Haidt): The theory that moral judgments are primarily driven by quick intuitions, with reasoning serving as post-hoc rationalization. No benchmark tests whether LLMs show "moral dumbfounding" — maintaining moral judgments even when unable to articulate reasons.

3. **Dyadic Morality** (Kurt Gray): The theory that all moral cognition reduces to perceived harm between an agent and a patient. No benchmark tests whether LLMs show dyadic sensitivity — rating scenarios as more morally wrong when agent-patient dynamics are explicit.

---

## Format & Size Landscape

| Format | Count | Examples | LLM Suitability |
|--------|-------|----------|-----------------|
| Forced-choice | 3 | Moral Machine (#1-3) | Excellent — binary preference, trivial to score |
| Likert scale | 2 | MFQ-30 (#8), Moral Identity (#13) | Good — but LLMs may not use the full scale |
| Scenario rating + ranking | 3 | DIT (#6, #9, #11) | Moderate — requires multi-step reasoning |
| Multi-label classification | 1 | MFTC (#4) | Good — standard NLP task |
| Binary + MCQ | 1 | Fraser (#5) | Excellent — exact match scoring |
| Free-text + MCQ | 2 | ValuePrism (#10), WVS (#12) | Requires model-graded scoring |
| MCQ + scenario gen | 1 | CVC (#14) | Good for MCQ portion, model-graded for generation |
| Likert + behavioral | 1 | Xu & Ma (#13) | Moderate — behavioral tasks hard for LLMs |

### Dataset Sizes

| Range | Count | Papers |
|-------|-------|--------|
| < 50 items | 4 | MFQ-30 (30), DIT (9×3), WVS (5) |
| 50-200 | 2 | MFV (132), Fraser (100) |
| 200-1,000 | 1 | Xu & Ma (250) |
| 1K-50K | 2 | MFTC (35K), Takemoto (50K) |
| 50K+ | 4 | ValuePrism (218K), CVC (250K), Moral Machine (40M×2) |

---

## Implementation Recommendations

### Immediate (harness-ready, simple scoring)
1. **Moral Machine on LLMs** (#2) — forced-choice, 50K items, Dryad data, tested on 4 LLMs
2. **MFTC** (#4) — multi-label classification, 35K tweets, OSF data
3. **MFQ-30** (#8) — 30 Likert items, GitHub code, direct MFQ administration

### Medium effort (adaptation needed)
4. **MFV** (#7) — 132 vignettes, needs scenario presentation + rating extraction
5. **DIT** (#6) — 9 dilemmas, needs multi-step prompting for ranking
6. **ValuePrism** (#10) — 218K items on HuggingFace, needs model-graded scoring

### Research frontier (existing but not yet assessed for top 15)
7. **Staircase of Ethics** (Wu 2025) — First multi-step escalating dilemma benchmark (3,302 x 5 stages). Engages Dual Process theory. Hidden gem from secondary scan.
8. **UniMoral** (Kumar 2025) — 6-language multi-theory dataset engaging Dual Process + Intuitionist + MFT + Kohlberg. Bridges psychological and social-media dilemmas.
9. **Bago 2022** — 45-country replication of Greene's trolley experiments. Gold-standard human baseline for Dual Process theory. Not an LLM benchmark per se, but the human comparison data is irreplaceable.

### Recommended Harnesses
- **Inspect AI** — best for model-graded scoring (DIT, ValuePrism, MFV)
- **lm-eval-harness** — best for exact-match benchmarks (MFTC classification, Moral Machine forced-choice)
- **Custom** — needed for psychometric scoring (MFQ-30 Likert scale requires reverse-coding and subscale computation)

---

## Data Files

| File | Description |
|------|-------------|
| `20260403-moral-psych-benchmark-candidates.json` | 222 candidates with YAML metadata |
| `20260403-council-depth-assessment.json` | Expert assessment of A2/A4/A5/A6/A7/B1/B2/B10 for top 40 |
| `20260403-council-impact-assessment.json` | Expert assessment of safety/B6-B9/C3/C5 for top 40 |
| `20260403-citation-counts.json` | Semantic Scholar citations for top 80 |
| `20260403-moral-psych-benchmark-feature-matrix.json` | Unified 28-feature matrix with composite scores |
| `20260403-moral-psych-top15-selection.json` | Final top-15 selection with full metadata |
| `20260403-council-secondary-scan.json` | Secondary scan of candidates 41-80 + hidden gems |

---

## Addendum: Secondary Scan Findings (Candidates 41-80)

The secondary council scan assessed 40 additional candidates and found **15 hidden gems** — papers with lower mp_* scores but high theoretical rigor or unique coverage.

### Revised Theory Gap Assessment

The initial report stated 3 theories have "zero dedicated LLM benchmarks." The secondary scan partially revises this:

| Theory | Initial Assessment | Revised Assessment |
|--------|-------------------|-------------------|
| Dual Process | Zero benchmarks | **3 papers engage it**: Bago 2022 (45-country human baseline), Staircase of Ethics (multi-step dilemmas), UniMoral (multi-language) |
| Social Intuitionist | Zero benchmarks | **4 papers touch it**: UniMoral, Insights into Moral Reasoning, + others. But none are dedicated intuitionist benchmarks — they test intuitionism as one dimension among many |
| Dyadic Morality | Zero benchmarks | **1 paper**: ValueCompass touches dyadic in a cross-national values context. Still effectively zero dedicated benchmarks |

**Root cause:** The vault's keyword scorer missed 85% of dual process papers and 97% of intuitionist papers because the patterns are too narrow. This is a scorer bug, not purely a literature gap.

### Top 5 Hidden Gems for Potential Top-15 Revision

| Paper | Year | Theories | Why |
|-------|------|----------|-----|
| Bago (45-country trolley) | 2022 | trolley, dual_process, intuitionist | Gold-standard human baseline for Greene's dual process theory across 45 countries |
| Sachdeva (AITA Normative Eval) | 2025 | mft | 10K+ real-world Reddit dilemmas with public data; far beyond trolley-scale complexity |
| Wu (Staircase of Ethics) | 2025 | mft, dual_process | First multi-step escalating benchmark (3,302 × 5 stages = 16,510 decisions) |
| Li (Value-Spectrum Video VQA) | 2024 | schwartz | Rare multimodal moral psych benchmark (50K+ TikTok/YouTube/Instagram videos) |
| Kumar (UniMoral) | 2025 | mft, kohlberg, dual_process, intuitionist | 6-language dataset bridging psychological and social-media dilemmas |

### Keyword Scorer Recommendations

The secondary scan revealed significant scorer blind spots:

| Theory | Scorer Detection Rate | Recommended Fix |
|--------|----------------------|-----------------|
| Dual Process | 15% (2 of 13) | Add patterns: "utilitarian vs deontological", "cognitive load", "response time", "personal vs impersonal" |
| Social Intuitionist | 3% (1 of 35) | Add patterns: "intuitive judgment", "post-hoc rationalization", "gut feeling", "automatic moral", "moral heuristic" |
| Dyadic Morality | 37% (3 of 8) | Add patterns: "harm perception", "agent patient", "moral typecasting" |
| Moral Identity | 50% (7 of 14) | Add patterns: "moral character", "moral self-concept", "moral exemplar", "Aquino" |

---

## Next Steps

1. **Gap Analysis (external search):** Search Semantic Scholar, PsycINFO, and ACL Anthology for dedicated Dual Process, Dyadic Morality, and Social Intuitionism benchmarks not yet in the vault
2. **Hidden Gem Assessment:** Run full depth assessment on the 15 hidden gems from the secondary scan to determine if any should replace #15 (or other weaker entries)
3. **Keyword Scorer Fix:** Update `moral_psych_scoring.py` with expanded patterns for underrepresented theories
4. **Implementation Trials:** Run 5 benchmarks through Claude (#2 Moral Machine, #4 MFTC, #8 MFQ-30, #6 DIT, #10 ValuePrism)
5. **Dashboard:** Build interactive dashboard with benchmark comparison, theory coverage heatmap, and implementation readiness tracker
6. **Paper Draft:** "Mapping the Moral Mind of Machines: A Meta-Evaluation of Moral Psychology Benchmarks for LLM Assessment"
