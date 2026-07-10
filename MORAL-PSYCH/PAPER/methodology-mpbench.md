# 3. Methodology

## 3.1 Multi-Signal Candidate Extraction

We began with a curated vault of 2,099 AI ethics papers spanning 2015--2026. To identify moral psychology benchmark candidates, we designed a five-signal detection pipeline that casts a deliberately wide net, as no single signal is sufficient to capture the heterogeneous ways benchmarks are described in the literature.

**Signal 1: Moral psychology scores.** The vault maintains eight moral psychology fields (mp_mft, mp_schwartz, mp_trolley, mp_kohlberg, mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity) scored 0--100 by a keyword-based scorer. Papers scoring >= 50 on any field were included.

**Signal 2: Benchmark flags with keyword match.** Papers flagged as benchmarks, evaluations, or datasets (is_benchmark, is_eval, is_dataset) that also contained >= 2 moral psychology keyword matches in their abstract or key contribution fields.

**Signal 3: Data availability with strong keyword match.** Papers with a published DATA_URL and >= 3 moral psychology keyword matches, targeting benchmarks that are readily implementable.

**Signal 4: High keyword density.** Papers with >= 5 moral psychology keyword matches regardless of other metadata, capturing papers whose benchmark nature may not be reflected in structured fields.

**Signal 5: Known benchmark names.** Papers whose title or abstract contained names of established benchmarks (ETHICS, MoralBench, ValueBench, Scruples, Delphi, MACHIAVELLI, Moral Machine, MoralChoice, MoralExceptQA, etc.).

The keyword taxonomy comprised 65 regex patterns covering all eight moral psychology theories, psychometric instrument names (MFQ, PVQ, DIT, MFV), general moral psychology terms, values alignment vocabulary, and specific benchmark names.

This pipeline extracted **222 candidates**: 177 classified as benchmarks, 43 as datasets, and 2 as other. A critical finding at this stage was that the vault's keyword scorer (Signal 1) alone missed major benchmarks. For instance, ValueBench (which administers 44 psychometric instruments to LLMs) scored mp_schwartz=0 because its abstract uses "value" rather than "Schwartz." The ETHICS dataset [Hendrycks et al., 2021] scored mp_mft=0 despite being one of the most widely used moral evaluation benchmarks. Multi-signal detection was therefore essential for adequate recall.

## 3.2 Expert Council Assessment

We assessed the top candidates using a twelve-perspective virtual expert council, where each perspective represents a distinct disciplinary lens on benchmark quality.

**Table 1: Expert Council Perspectives**

| # | Perspective | Assessment Focus |
|---|------------|-----------------|
| 1 | MFT Specialist | Theory fidelity, operationalization depth |
| 2 | Developmental Psychologist | Kohlberg stage validity, developmental sensitivity |
| 3 | Psychometrician | Construct validity, reliability, source instruments |
| 4 | NLP Evaluation Specialist | Harness compatibility, scorer types, format suitability |
| 5 | Cross-Cultural Psychologist | WEIRD bias, multilingual coverage |
| 6 | AI Safety Researcher | Deployment relevance, actionability |
| 7 | Bibliometrician | Citation impact, venue tiers, downstream adoption |
| 8 | Data Engineer | Reproducibility, data access, implementation effort |
| 9 | Survey Methodologist | Search protocol rigor, inclusion/exclusion criteria |

Assessment was conducted in three parallel passes:

- **Depth assessment** (Perspectives 1--3, 5): Read PDF extracts for each candidate and scored A2 (operationalization), A4 (source instrument), A5 (human baseline), A6 (construct validity), A7 (cultural provenance), A8 (languages), B1 (format), B2 (dataset size), and B10 (LLM administration fidelity).

- **Impact assessment** (Perspectives 4, 6--8): Cross-referenced candidates with implementability data and scored safety relevance, B6--B9 (harness compatibility, scorer type, model compatibility), C3 (venue tier), and C5 (hub/leaderboard presence).

- **Secondary scan** (Perspective 9): Scanned candidates ranked 41--80 for hidden gems and underrepresented theories, identifying 15 additional papers warranting full assessment.

Citation counts were obtained from the Semantic Scholar API for the top 80 candidates (54 found; 26 lacked DOIs or arXiv identifiers).

In total, **55 benchmarks** received full 28-feature characterization: 40 from the primary assessment and 15 hidden gems from the secondary scan.

## 3.3 The 28-Feature Characterization Framework

We organized the 28 features into three tiers reflecting distinct dimensions of benchmark quality.

**Tier A --- Psychological Depth (6 features).** This tier measures how faithfully a benchmark engages moral psychology theory.

| Feature | Description | Scale |
|---------|-------------|-------|
| A1 | Number of theories engaged | 0--8 (normalized: 0=0, 1=30, 2=60, 3=80, 4+=100) |
| A2 | Construct operationalization | Validated=100, Theory-derived=70, Theory-inspired=40, Keyword-only=10 |
| A3 | Measurement target | Default 70 (adjusted per assessment) |
| A4 | Source instrument provenance | Validated=100, Original=80, None=0 |
| A5 | Human baseline availability | Published norms=100, Paper-specific=70, Partial=40, No=0 |
| A6 | Construct validity evidence | 5=100, 4=75, 3=50, 2=30, 1=10 |

**Tier B --- Practical Ease (7 features).** This tier measures how readily a benchmark can be implemented for LLM evaluation.

| Feature | Description | Scale |
|---------|-------------|-------|
| B1 | Task format | MCQ=100, Binary=90, Forced-choice=85, Likert=70, Free-text=50 |
| B2 | Dataset size | Log-scaled: <50=20, 200=40, 1K=60, 5K=75, 20K=85, >20K=100 |
| B3 | Data availability | HuggingFace=100, GitHub=95, OSF=90, Anonymous link=60 |
| B4 | Code availability | Full pipeline=100, Partial=50, None=0 |
| B6 | Harness tier (Inspect/lm-eval) | Tier 1=100, Tier 2=70, Custom=40 |
| B7 | Scorer complexity | Exact match=100, Model-graded=60, Psychometric=40 |
| B10 | LLM administration fidelity | Direct=100, Minor adaptation=70, Major adaptation=40, Paradigm change=10 |

**Tier C --- Citation Impact (4 features).** This tier measures scholarly influence and community adoption.

| Feature | Description | Scale |
|---------|-------------|-------|
| C1 | Raw citation count | Log-scaled: <5=10, 50=50, 200=75, >500=100 |
| C2 | Age-normalized citation rate | Citations/year, log-scaled |
| C3 | Venue tier | Tier 1 (Nature, ACL)=100, Tier 2=75, Tier 3=50, Tier 4=25 |
| C5 | Hub/leaderboard presence | On major hub=100, Minor hub=50, None=0 |

**Feature coverage note.** Five features defined in the original framework were not assessed in the 54-benchmark characterization: B5 (Instruction simplicity), B7 (Platform requirements), B8 (Open access), B9 (Documentation completeness), and C4 (Cross-domain citations). These features require access to benchmark distribution infrastructure (repositories, licenses, documentation quality) that was not systematically available for all candidates during the assessment period. They are excluded from composite scoring. The extended 162-feature framework (Tiers D--G) was assessed at 99.1% coverage (7,544 of 7,614 cells), with the remaining gaps concentrated in D9 (LLM ceiling compression, 35% null) and D20 (sample size adequacy, 35% null) where empirical data was unavailable.

## 3.4 Composite Scoring and Selection

Features were aggregated into tier-level scores using weighted averages:

```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
```

The final composite score applied user-specified tier weights reflecting a preference for psychological rigor over practical convenience:

```
COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

Selection proceeded through a five-step algorithm:

1. **Hard gates.** Candidates required PD >= 40 and publicly available data. Of 55 assessed candidates, 34 passed both gates.
2. **Deduplication.** Two duplicate entries were removed (TrolleyBench, Khandelwal DIT), yielding 32 unique candidates.
3. **Theory caps.** To prevent over-representation, we capped Trolley at 3 and MFT at 4 entries in the final selection.
4. **Greedy selection.** Candidates were selected in descending composite order, respecting caps.
5. **Diversity fills.** Lower-ranked candidates were swapped in to meet minimums: >= 2 Schwartz, >= 1 Kohlberg, >= 1 minority theory (identity, dyadic, intuitionist, or dual process).

## 3.5 Keyword Scorer Expansion

During the secondary scan, we identified critical blind spots in the vault's moral psychology keyword scorer. Detection rates for three theories were severely deficient:

| Theory | Before Expansion | After Expansion | Delta |
|--------|-----------------|-----------------|-------|
| MFT | 68 | 101 | +33 |
| Schwartz | 52 | 69 | +17 |
| Trolley | 36 | 58 | +22 |
| Kohlberg | 19 | 35 | +16 |
| Dual Process | 0 | 9 | +9 |
| Social Intuitionism | 1 | 18 | +17 |
| Dyadic Morality | 3 | 7 | +4 |
| Moral Identity | 7 | 12 | +5 |
| **Total** | **186** | **309** | **+123** |

For Dual Process Theory, we added patterns including "utilitarian vs deontological," "cognitive load," "response time," "personal vs impersonal dilemma," and "System 1/System 2." For Social Intuitionism, we added "intuitive judgment," "post-hoc rationalization," "moral dumbfounding," "automatic moral," and "moral heuristic." For Dyadic Morality, we added "harm perception," "agent patient," "moral typecasting," and "dyadic template."

After re-scoring all 2,099 papers, 148 papers received updated scores and the theory detection landscape shifted substantially. The expansion confirmed that the near-zero detection of Dual Process, Intuitionist, and Dyadic papers was primarily a scorer artifact, though these theories remain genuinely underrepresented relative to MFT.

## 3.6 Implementation Trial Protocol

To ground our characterization in practical experience, we conducted implementation trials on selected benchmarks. Each trial followed a standardized protocol:

1. **Benchmark selection.** We prioritized benchmarks spanning different formats (forced-choice, Likert, ranking) and theories.
2. **Prompt design.** We developed prompt templates faithful to the original instrument's administration instructions, adapting only what was necessary for text-based interaction.
3. **Sampling.** For large benchmarks (e.g., Moral Machine, 40M decisions), we drew stratified samples of 500 items balancing across the benchmark's dimensions.
4. **Model administration.** Each benchmark was administered to Claude Opus and Claude Sonnet at temperature 0 (deterministic) for primary runs, with 5 additional runs at temperature 0.7 to assess stability.
5. **Scoring.** We computed per-dimension preference rates, effect sizes (Cohen's d) against published human baselines, profile correlations, and test-retest consistency.
6. **Documentation.** Each trial was recorded as a structured report documenting methodology, results, key findings, and limitations.

Trial MP1 (Moral Machine) demonstrated the protocol on the highest-ranked benchmark, revealing that both Claude models amplify universally shared moral preferences (sparing more lives: 0.92--0.94 vs. human 0.81) while attenuating social hierarchy biases (sparing higher status: 0.48--0.50 vs. human 0.52). Profile correlations with human global means exceeded r = 0.95 for both models.

## 3.7 Terminology and Disclosure

**Terminology choice.** We use "moral response profile" rather than "moral phenotype" throughout this paper to describe the pattern of moral judgments a model produces across instruments. The biological metaphor of "phenotype" (the observable expression of a genotype) risks encouraging anthropomorphic interpretation by implying an underlying "genotype" (training data + architecture + RLHF) that produces observable moral behavior in a manner analogous to biological development. Following council recommendation (see Section 5.3.3), we adopt terminology that describes what is directly observed---response patterns on administered instruments---without importing biological or developmental assumptions whose applicability to LLMs is precisely what should be under investigation.

**Virtual expert council disclosure.** The twelve-perspective expert council described in Section 3.2 was generated by the same underlying language model (Claude Opus 4.6) that served as the test subject for implementation trials. While the structured multi-perspective protocol assigns distinct disciplinary roles and produces assessments with different emphases, all twelve perspectives ultimately derive from a single model. We characterize the council as a structured analytical device for systematic coverage rather than an equivalent to independent expert peer review (see Section 5.3.3 for a full discussion of this limitation).

**Framework expansion.** The original 28-feature characterization framework (features A1--A6, B1--B10, C1--C5) was expanded to 162 features organized across seven tiers (A through G) during the assessment process, adding dimensions for psychometric rigor (D-tier), LLM-specific validity (E-tier), cultural and philosophical breadth (F-tier), and advanced benchmarking properties (G-tier). We report the 28-feature core scores as our primary characterization and the extended 162-feature matrix as supplementary material for comprehensive analysis.
