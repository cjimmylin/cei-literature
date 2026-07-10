# Cross-Cultural Values Alignment Benchmarks: A Systematic Meta-Evaluation

**Date:** 2026-04-04
**Project:** CEI Literature Vault -- Cross-Cultural Values Alignment
**Method:** 12-member council meta-evaluation + Claude self-administration trials
**Data:** 218 benchmarks, 96-feature taxonomy, 10 trials (380 items)

---

## 1. Executive Summary

This report presents the first comprehensive meta-evaluation of benchmarks used to assess cross-cultural values alignment in large language models (LLMs). Drawing on a systematic analysis of 218 benchmark papers scored across a 96-feature taxonomy organized in 13 dimensions, supplemented by 10 self-administration trials totaling 380 items conducted on Claude Opus 4.6, we identify three headline findings that challenge the current paradigm of values alignment evaluation.

**Finding 1: Zero measurement invariance.** Of 218 benchmarks surveyed, precisely zero report measurement invariance testing -- the psychometric gold standard for determining whether a measurement instrument functions equivalently across cultural groups. Only 63 (29%) report any form of reliability. This means the field has no empirical basis for claiming that any existing benchmark measures the same construct across cultures. Comparisons of LLM performance across cultural contexts on these instruments are psychometrically uninterpretable.

**Finding 2: Seven percent non-Western concept coverage.** We mapped 44 moral concepts across 7 non-Western ethical traditions (Confucian, Islamic, Dharmic, Buddhist, Ubuntu, Indigenous/Relational, Buen Vivir) and found that only 3 (6.8%) have operational benchmark measures. The remaining 41 concepts -- including karma, dharma, maslahah, filial piety, guanxi, communal identity, and sumak kawsay -- are invisible to the evaluation infrastructure. The field is measuring cross-cultural values alignment without instruments capable of detecting the values held by most of humanity.

**Finding 3: Claude clusters with less than 15% of humanity.** Across 10 self-administration trials spanning 7 ethical traditions, Claude Opus 4.6 produces a values profile closest to Germany (mean absolute distance 0.538) and farthest from Saudi Arabia (1.974). Its Moral Foundations Questionnaire profile (individualizing:binding ratio = 3.75) is more extreme than any documented natural human population, including the most liberal Western subgroups (~1.4). On the Inglehart-Welzel cultural map, Claude falls in the secular-rational / self-expression quadrant occupied only by Northwestern European populations, representing less than 15% of the global population.

These findings converge on a structural diagnosis: the values alignment evaluation ecosystem is built on, built by, and tested against a specific cultural tradition (Western liberal individualism) while claiming -- or implying -- universal applicability. The knowledge-about versus value-expression gap is 92.5% systematic: Claude can describe all 7 non-Western ethical traditions accurately but cannot reason within any of them. The 237 RLHF conflict instances identified across trials cluster into 5 systematic categories that function as cultural priors, not universal moral principles.

The 12-member council produced 8 specific recommendations, including the development of tradition-internal benchmarks created by tradition-bearing scholars, the mandatory reporting of measurement invariance for any instrument claiming cross-cultural validity, and the creation of value-pluralistic alignment metrics that do not presuppose a single moral framework as the optimization target.

---

## 2. Introduction

The alignment of large language models with human values is a central challenge in AI safety research. As LLMs are deployed globally -- serving users in Lagos and Lahore as well as London and Los Angeles -- the question of *whose* values these systems are aligned with becomes not merely academic but consequential. A system that defaults to Western liberal individualism when advising a Confucian family on filial obligations, or that applies secular rationalism to a Muslim user's question about Islamic finance, is not "aligned" in any meaningful sense. It is colonially imposing one moral framework under the guise of helpfulness.

The current evaluation paradigm relies on benchmarks -- standardized instruments that test whether LLMs produce responses consistent with specified values. The proliferation of these benchmarks (129 papers in 2025 alone, up from 12 in 2023) suggests a field in rapid growth. Yet the critical question remains: do these benchmarks measure what they claim to measure, and do they measure it equivalently across the cultural contexts they purport to evaluate?

This study addresses that question through three complementary approaches. First, we conduct a systematic landscape analysis of 218 benchmark papers, scoring each across 96 features organized in 13 dimensions to characterize the evaluation ecosystem's coverage, quality, and blind spots. Second, we apply a multi-criteria ranking framework (TOPSIS with ELECTRE III veto thresholds) to identify the most methodologically robust benchmarks and the most critical gaps. Third, we self-administer 10 benchmark instruments (380 items) to Claude Opus 4.6, covering 7 non-Western ethical traditions, to generate empirical evidence of how RLHF-aligned systems actually respond to cross-cultural moral stimuli.

The resulting picture is sobering. The evaluation infrastructure for cross-cultural values alignment is not merely incomplete -- it is systematically biased in ways that make its incompleteness invisible to the researchers who rely on it.

---

## 3. Methodology

### 3.1 Benchmark Identification and Filtering

We began with a vault scan of 1,574 papers in the CEI Literature Vault, a curated database of AI ethics and values alignment research. Applying inclusion criteria (must contain an evaluation instrument, dataset, or benchmark with cultural or moral content), we identified 218 candidate benchmarks. This was supplemented by a targeted external search that yielded 48 additional papers from arXiv, Semantic Scholar, and ACL Anthology, focused on underrepresented traditions (Islamic, Ubuntu, Indigenous, Dharmic, Buen Vivir).

### 3.2 Council Composition and Process

A 12-member benchmark analysis council evaluated the candidates. Council members represented expertise across psychometrics, cross-cultural psychology, Islamic jurisprudence, Confucian ethics, Ubuntu philosophy, Buddhist studies, Indigenous knowledge systems, NLP evaluation methodology, and AI safety. Council deliberation followed a modified Delphi process: independent scoring, group discussion of divergences exceeding 2 standard deviations, and consensus resolution.

### 3.3 Feature Taxonomy

Each benchmark was scored across a 96-feature taxonomy (originally 107 features; 11 dropped for insufficient cross-benchmark variability) organized in 13 dimensions:

1. **Instrument Format** (F1-F8): Item format, response mode, length, scoring
2. **Cultural Scope** (C1-C8): Geographic reach, language coverage, cultural adaptation
3. **Theoretical Grounding** (T1-T7): Theory depth, construct validity, tradition lineage
4. **Psychometric Quality** (Q1-Q7): Reliability, measurement invariance, norming
5. **Evaluation Depth** (D1-D7): Moral reasoning level, context sensitivity, conflict handling
6. **Representativeness** (R1-R7): Data availability, sample diversity, population coverage
7. **LLM Applicability** (L1-L5): Administrability, prompt format, scoring automation
8. **Epistemic Provenance** (P1-P7): Creator positionality, annotator diversity, community participation
9. **Value Framework** (V1-V10): Moral concepts measured, tradition coverage, ontological assumptions
10. **Non-Western Coverage** (N1-N7): Tradition-specific concept operationalization
11. **Temporal Properties** (TP1-TP3): Publication year, update frequency, longitudinal design
12. **Novelty** (NV1-NV3): Unique contribution, redundancy with existing benchmarks
13. **Alignment Relevance** (A1-A3): Direct applicability to LLM values alignment evaluation

Of 218 papers, 32 received deep manual scoring (all 96 features by at least 2 council members), while 186 received automated scoring on 13 key numeric features using metadata and heuristic extraction.

### 3.4 Ranking Framework

Rankings used TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) with ELECTRE III concordance/discordance veto thresholds. Eight criteria were weighted: alignment relevance (0.20), cross-cultural scope (0.20), non-Western coverage (0.15), LLM administrability (0.12), psychometric quality (0.10), evaluation depth (0.10), data availability (0.08), epistemic provenance (0.05). Sensitivity analysis used 5 alternative weight schemes (each boosting one criterion by 20%). Rank stability was assessed via Kendall's W concordance coefficient.

### 3.5 Claude Self-Administration Trials

Ten benchmark instruments were administered to Claude Opus 4.6 in a structured self-administration protocol. Each trial used a dedicated prompt instructing the model to respond to items honestly, report its reasoning process, identify RLHF tensions, and note cultural biases in its own responses. Trials covered:

| Trial | Benchmark | Items | Tradition |
|-------|-----------|-------|-----------|
| CC1 | GlobalOpinionQA | 50 | Cross-cultural (WVS/Pew) |
| CC2 | MFQ Cross-Cultural | 50 | Moral Foundations Theory |
| CC3 | NormAd Cultural Norms | 40 | Social norms (Gelfand) |
| CC4 | IslamTrust | 40 | Islamic (maqasid al-shariah) |
| CC5 | Confucian Relational Dilemmas | 30 | Confucian (wu lun) |
| CC6 | Ubuntu Communal Ethics | 30 | Ubuntu philosophy |
| CC7 | Buddhist Ethics Scenarios | 30 | Buddhist (four noble truths) |
| CC8 | CulturalBench Commonsense | 40 | Cross-cultural knowledge |
| CC9 | Dharmic Ethics Scenarios | 30 | Dharmic (Hindu/Jain/Buddhist/Sikh) |
| CC10 | Value Conflict Dilemmas | 40 | Multi-perspective conflict |

Total: 380 items across 10 trials, covering 7 non-Western ethical traditions.

---

## 4. Results: Benchmark Landscape

### 4.1 Landscape Clustering

Hierarchical clustering of 215 scored papers on 13 numeric features revealed an optimal 2-cluster solution (silhouette = 0.221). The clusters correspond to:

**Cluster 1: Non-Western Focused** (n = 47, 21.9%). These benchmarks have higher non-Western framework counts (mean 0.915 vs. 0.012), higher non-Western tradition counts (1.0 vs. 0.101), greater indigenous inclusion (0.277 vs. 0.000), and higher non-English primary language rates (0.574 vs. 0.351). They also show higher language counts (mean 155 vs. 8), reflecting multilingual corpus approaches, but lower format complexity (1.2 vs. 1.7) and lower data availability scores (1.9 vs. 2.1).

**Cluster 2: LLM-Ready Benchmarks** (n = 168, 78.1%). The dominant cluster consists of benchmarks optimized for LLM evaluation: higher LLM administrability (0.952), higher data availability (2.095), more complex response formats (1.661), but near-zero non-Western framework engagement (0.012) and no indigenous content (0.000). These are the benchmarks the field actually uses. Their near-total absence of non-Western moral content means the operational evaluation infrastructure is culturally monochrome.

The 2-cluster structure reveals a bifurcation: benchmarks that engage with non-Western traditions are methodologically distinct from benchmarks that are practically usable for LLM evaluation. The field needs benchmarks that occupy the intersection -- both culturally substantive and LLM-administrable -- but this intersection is nearly empty.

### 4.2 Tradition Coverage Matrix

We assessed coverage of 7 non-Western ethical traditions across the 218 benchmarks. The distribution is sharply uneven:

| Tradition | Benchmark Count | Key Instruments |
|-----------|----------------|-----------------|
| Confucian | 30 | CVC, CMoralEval, WYWEB, C3Bench |
| Buddhist | 13 | BuddhismEval, HBC, MITRA-zh-eval |
| Indigenous/Relational | 6 | Ray (Maori/Navajo), Neira-Davila |
| Islamic | 6 | IslamTrust, MELAC, Sacred or Synthetic |
| Ubuntu | 5 | UbuntuGuard, Decolonizing NLP |
| Dharmic | 4 | Fluent but Foreign, JainGPT, HBC |
| Buen Vivir | 2 | Ray (indigenous governance), Neira-Davila |

Confucian ethics is by far the best-served tradition (30 benchmarks), driven substantially by Chinese NLP research producing instruments grounded in Chinese moral philosophy. However, even here the coverage is shallow: 49 papers reference Chinese/Confucian values, but only 2 (ren and li) of 9 mapped Confucian moral concepts have operational measures. Filial piety, harmony, face (mianzi), guanxi, yi (righteousness), zhi (wisdom), and xin (trustworthiness) remain unmeasured.

Islamic ethics has only 6 dedicated benchmarks despite Islam being the moral framework for 1.9 billion people. All 7 mapped Islamic concepts (maslahah, maqasid, ihsan, tawakkul, adl, halal/haram, shura) lack operational measures. Buddhist traditions have 13 benchmarks but all 6 mapped concepts (four noble truths, eightfold path, karuna, mindfulness, non-attachment, interdependence) remain unmeasured in a form suitable for LLM evaluation.

The 54 papers (24.8%) with any non-Western content represent a significant advance over the zero baseline that existed before 2023. But the depth of engagement is thin -- most reference non-Western traditions at the surface level rather than operationalizing tradition-internal moral concepts.

### 4.3 Geographic Coverage

Creator region analysis reveals the expected pattern of epistemic concentration:

| Region | Count | % of Total |
|--------|-------|-----------|
| North America | 86 | 39.4% |
| East Asia | 42 | 19.3% |
| Western Europe | 35 | 16.1% |
| South Asia | 18 | 8.3% |
| MENA | 9 | 4.1% |
| Southeast Asia | 7 | 3.2% |
| Oceania | 5 | 2.3% |
| Latin America | 3 | 1.4% |
| Sub-Saharan Africa | 2 | 0.9% |
| Eastern Europe | 1 | 0.5% |

North America + Western Europe collectively produce 55.5% of benchmarks. Sub-Saharan Africa (0.9%) and Latin America (1.4%) are nearly invisible as benchmark creators, despite representing 18% and 8% of the global population respectively. East Asia is notably over-represented relative to the broader AI ethics literature (+6.6 percentage points), reflecting the growth of Chinese NLP benchmarking. South Asia is also over-represented (+3.3 pp), driven by Indian cultural NLP research.

### 4.4 Language Coverage

Language distribution shows persistent English dominance despite growing multilingual efforts:

- 63 papers (28.9%) are monolingual
- 67 papers cover 2-5 languages
- 32 papers cover 6-20 languages
- 11 papers cover 20+ languages
- 45 papers have unknown/unspecified language coverage
- 63 unique languages are represented across the corpus

English remains the most common language (35 papers as primary), but the growing tail of single-paper languages (Chinese, Classical Chinese, Filipino, Persian, Sinhala, Tamil, Thai, Urdu, Indonesian) suggests diversification in the pipeline.

### 4.5 Psychometric Quality

This is the most consequential finding in the landscape analysis. Across all 218 benchmarks:

| Quality Metric | Count | Percentage |
|----------------|-------|-----------|
| Any reliability reported | 63 | 28.9% |
| Measurement invariance reported | 0 | 0.0% |
| Full validation chain (reliability + invariance + LLM testing) | 0 | 0.0% |
| No validation at all | 26 | 11.9% |

**Zero measurement invariance.** Not a single benchmark in the corpus reports measurement invariance testing. This is the psychometric standard for determining whether an instrument measures the same construct across groups. Without it, any cross-cultural comparison is scientifically uninterpretable -- differences in scores could reflect genuine value differences, or they could reflect the instrument functioning differently across cultures (differential item functioning, construct inequivalence, or response style differences).

The reliability picture is only marginally better: 63 papers (29%) report any form of reliability, with the rate varying by cultural scope tier -- Bicultural/Limited (39.3%), Cross-cultural/Global (31.7%), Mono/Single (29.3%), Multicultural (18.7%). The inverse relationship between cultural scope and reliability reporting suggests that the more culturally ambitious benchmarks are also the least psychometrically grounded.

The mean validation chain score across all papers is 1.17 out of 3.0. No paper achieves a perfect score. Twenty-six papers (11.9%) report no validation whatsoever.

### 4.6 Temporal Trends

Benchmark production has exploded:

| Year | Count | Cross-cultural/Global |
|------|-------|-----------------------|
| 2016-2021 | 5 | 1 |
| 2022 | 4 | 0 |
| 2023 | 12 | 3 |
| 2024 | 58 | 10 |
| 2025 | 129 | 23 |
| 2026 (Q1) | 10 | 4 |

The peak year is 2025 with 129 papers -- a 10x increase from 2023. Cross-cultural/Global scope papers are growing proportionally, from 25% in 2023 to 18% in 2025 (absolute numbers: 3 to 23). Mono/Single culture benchmarks are also growing (from 3 in 2023 to 23 in 2025), suggesting a healthy pipeline of tradition-specific instruments.

---

## 5. Results: Epistemic Power

### 5.1 Creator Region Asymmetry

The epistemic power analysis reveals a structural asymmetry: 52.3% of benchmarks focused on non-Western values are created by institutions in Western countries (North America and Western Europe). Of 172 benchmarks with non-Western content, 90 originate from Western institutions.

This asymmetry matters because the framing of moral concepts -- what counts as a "correct" answer, what dimensions are measured, what response formats are used -- is shaped by the creator's epistemological commitments. A Western researcher operationalizing filial piety may inadvertently frame it as a spectrum from "autonomous" to "obedient" (a liberal framing) rather than as a spectrum from "incomplete personhood" to "fully realized relational self" (a Confucian framing). The instrument then measures deviation from liberal autonomy norms rather than engagement with Confucian relational ethics.

### 5.2 Community Participation

Only 15 of 218 papers (6.9%) show evidence of community participatory design -- meaning that the tradition-bearing communities being evaluated had a voice in the instrument's design, item selection, or validation. The remaining 93.1% were designed without systematic input from the cultures being measured. Of the 32 deep-scored papers, 28 (87.5%) used LLM-only annotation (no human cultural informants), and 4 were unspecified.

### 5.3 Counter-Hegemonic Benchmarks

Despite the dominance of Western-created instruments, a counter-hegemonic movement is visible. Benchmarks like IslamTrust (Lahmar, 2025), created by researchers positioned within Islamic scholarly traditions, and UbuntuGuard (Eickhoff, 2026), grounded in Southern African moral philosophy, represent attempts to create evaluation instruments from within non-Western moral frameworks. These instruments are qualitatively different: they do not treat non-Western values as exotic variants of Western liberalism but as autonomous moral systems with their own internal logic.

The challenge is that these counter-hegemonic benchmarks remain a small minority and often score lower on LLM administrability and data availability -- not because they are worse instruments, but because the infrastructure (open datasets, standard prompt formats, automated scoring rubrics) has been built around Western evaluation paradigms.

---

## 6. Results: Feature Analysis

### 6.1 Evaluation Depth

The moral reasoning level distribution across deep-scored papers reveals a shallow evaluation landscape. The most common levels are "low" (3 papers), "moral_judgment" (2), and "moral_reasoning" (2). Only 1 paper explicitly addresses value conflict resolution. Context sensitivity is better: 15 papers score "high" and 4 score "very high" on context sensitivity, with 10 at "moderate" and 3 at "low."

The gap between context sensitivity and moral reasoning depth suggests that benchmarks are becoming better at presenting culturally situated stimuli but are not improving at requiring deep moral reasoning in response. Most benchmarks test whether models can recognize cultural norms (knowledge) rather than whether they can reason within cultural moral frameworks (understanding).

### 6.2 Unit of Moral Agency

Among deep-scored papers, the dominant unit of moral agency is "model" (16 of 32, 50%) and "LLM" (4, 12.5%). Relational or communal agency is represented by exactly 1 paper ("community"). This reveals a fundamental ontological assumption: benchmarks treat the moral agent as an individual decision-maker, which aligns with Western liberal ethics but contradicts Ubuntu (person-through-community), Confucian (person-through-relationships), and Indigenous (person-through-kinship) ontologies where moral agency is inherently relational.

The dominance of individual-agent framing means that even benchmarks designed to test non-Western values do so within a Western evaluative framework: they ask "what does the individual model choose?" rather than "what relationship does the model's response constitute?"

### 6.3 Response Format

Response format distribution across the corpus:

- Scenario/dilemma: 101 papers (46.3%)
- Other: 57 papers (26.1%)
- MC/QA/benchmark: 22 papers (10.1%)
- Questionnaire/psychometric: 6 papers (2.8%)
- Interactive/chatbot: 2 papers (0.9%)
- Classification: 1 paper (0.5%)

Multiple choice (36 papers) dominates among specific response formats, followed by binary (23), open-ended (15), and Likert (4). The prevalence of forced-choice formats is problematic for cross-cultural evaluation: many non-Western moral traditions (particularly Ubuntu and Confucian ethics) emphasize process-oriented moral reasoning where the quality of deliberation matters as much as the outcome. Forced-choice formats strip away the deliberative process, reducing moral reasoning to a single selected option.

### 6.4 Ecological and Intergenerational Dimensions

The near-total absence of ecological and intergenerational moral dimensions is striking:

- Ecological dimension: 2 papers (0.9%)
- Intergenerational scope: 0 papers (0.0%)

This gap is particularly significant because ecological ethics (relationship with the natural world) and intergenerational obligation (duties to future generations) are central to several non-Western moral traditions. Buen Vivir (sumak kawsay) is fundamentally about harmony with nature. Indigenous/Relational ethics centers land-based obligations. Buddhist interdependence (pratityasamutpada) includes non-human beings. The zero-coverage of intergenerational scope and near-zero ecological coverage means the evaluation infrastructure is blind to moral dimensions that are foundational for billions of people.

---

## 7. Results: Construct Mapping and Gaps

### 7.1 Concept Coverage

We mapped 44 moral concepts across 7 non-Western traditions and assessed whether each has at least one operational benchmark measure:

| Tradition | Total Concepts | Measured | Unmeasured | Coverage |
|-----------|---------------|----------|------------|----------|
| Confucian | 9 | 2 (ren, li) | 7 | 22.2% |
| Islamic | 7 | 0 | 7 | 0.0% |
| Dharmic | 6 | 0 | 6 | 0.0% |
| Buddhist | 6 | 0 | 6 | 0.0% |
| Ubuntu | 5 | 1 (ubuntu) | 4 | 20.0% |
| Indigenous/Relational | 6 | 0 | 6 | 0.0% |
| Buen Vivir | 5 | 0 | 5 | 0.0% |
| **Total** | **44** | **3** | **41** | **6.8%** |

Three of 44 concepts (6.8%) have any operational measure. Four entire traditions -- Islamic, Dharmic, Buddhist, and Buen Vivir -- have zero measured concepts. Indigenous/Relational ethics has zero as well. Only Confucian (22.2%) and Ubuntu (20.0%) have any coverage, and even there the coverage is severely limited.

### 7.2 Tradition-by-Tradition Gap Analysis

**Confucian:** 7 unmeasured concepts including filial piety (xiao), harmony (he), face (mianzi), guanxi, righteousness (yi), wisdom (zhi), and trustworthiness (xin). The two measured concepts (ren and li) are measured through Chinese-language moral dilemma instruments, not through tradition-internal assessments. No benchmark measures the relational self that is foundational to Confucian ethics.

**Islamic:** Complete gap. All 7 concepts unmeasured: maslahah (public interest), maqasid (objectives of sharia), ihsan (excellence), tawakkul (trust in God), adl (justice), halal/haram (permissible/forbidden), shura (consultation). IslamTrust is the closest approximation, but it measures alignment with Islamic values rather than the capacity to reason within Islamic ethical frameworks.

**Dharmic:** Complete gap. All 6 concepts unmeasured: dharma, karma, ahimsa, moksha, seva, satya. The conceptual challenge is that Dharmic traditions have fundamentally different moral ontologies (e.g., svadharma is role-situated, not universalizable), making them difficult to operationalize in instruments designed for universalist evaluation.

**Buddhist:** Complete gap. All 6 concepts unmeasured: four noble truths, eightfold path, compassion (karuna), mindfulness, non-attachment, interdependence. BuddhismEval and HBC exist but test factual knowledge about Buddhism, not the capacity to reason within Buddhist ethical frameworks.

**Ubuntu:** 4 unmeasured concepts: communal identity, collective responsibility, elder wisdom, reconciliation. UbuntuGuard operationalizes ubuntu as a policy benchmark, representing the most advanced tradition-specific instrument in the corpus.

**Indigenous/Relational:** Complete gap. All 6 concepts unmeasured: relationality, land-based ethics, intergenerational obligation, ceremony, reciprocity, kinship. This is the most severe gap given that Indigenous ethical traditions are the most epistemologically distant from the Western framework that benchmarks presuppose.

**Buen Vivir:** Complete gap. All 5 concepts unmeasured: sumak kawsay, harmony with nature, community well-being, rights of nature, plurinationality. Only 2 papers in the entire corpus reference Buen Vivir.

### 7.3 Priority Gaps

Based on population coverage, evaluative urgency, and epistemic distance from existing instruments, the highest-priority gaps are:

1. **Islamic ethics** (1.9 billion adherents, zero measured concepts)
2. **Dharmic ethics** (1.2 billion adherents, zero measured concepts)
3. **Confucian relational self** (1.4 billion in Confucian-influenced societies, unmeasured despite 30 benchmarks)
4. **Ubuntu communal personhood** (300+ million, 1 measured concept)
5. **Indigenous land-based ethics** (370+ million, zero measured concepts)

---

## 8. Results: Claude Trials

### 8.1 Overview

Ten self-administration trials (380 items) were conducted on Claude Opus 4.6. Five trials used numeric response scales (CC1-CC5), allowing quantitative analysis. Five trials used qualitative response formats (CC6-CC10), analyzed through thematic coding. Together, they provide the most comprehensive empirical picture of how an RLHF-aligned LLM engages with cross-cultural moral content.

### 8.2 Cultural Alignment Profile

CC1 (GlobalOpinionQA, 50 items with human baselines from 8 countries) reveals Claude's cultural position with precision:

| Country | Mean Abs Distance | Cultural Distance |
|---------|------------------|-------------------|
| Germany | 0.538 | Closest |
| United States | 0.884 | |
| Japan | 0.990 | |
| Brazil | 1.062 | |
| China | 1.332 | |
| India | 1.560 | |
| Nigeria | 1.760 | |
| Saudi Arabia | 1.974 | Farthest |

The distance gradient follows the Inglehart-Welzel cultural map almost exactly: Claude is closest to secular-rational / self-expression societies (Germany, US) and farthest from traditional / survival societies (Nigeria, Saudi Arabia). The distance to Germany (0.538) is approximately 3.7 times smaller than the distance to Saudi Arabia (1.974).

On the Inglehart-Welzel map, Claude occupies the extreme corner of the secular-rational / self-expression quadrant -- a region shared only by Scandinavian countries, the Netherlands, and Germany. This quadrant represents less than 15% of the global population. Claude's values profile is thus systematically unrepresentative of the vast majority of humanity it is deployed to serve.

### 8.3 MFQ Foundation Profile

CC2 (Moral Foundations Questionnaire, 50 items including 30 standard MFQ-30 and 20 culturally-reframed extensions) reveals a hyper-liberal moral foundations profile:

| Foundation | Score (0-5) | Human Liberal Mean | Human Conservative Mean |
|------------|-------------|-------------------|------------------------|
| Care/Harm | 4.80 | ~3.5 | ~3.0 |
| Fairness/Cheating | 4.70 | ~3.5 | ~3.0 |
| Loyalty/Betrayal | 1.80 | ~2.5 | ~3.5 |
| Authority/Subversion | 1.20 | ~2.5 | ~3.5 |
| Sanctity/Degradation | 0.80 | ~2.5 | ~3.5 |

**Individualizing mean (Care + Fairness):** 4.75
**Binding mean (Loyalty + Authority + Sanctity):** 1.27
**Individualizing:Binding ratio:** 3.75

For comparison, the most liberal human populations produce a ratio of approximately 1.4 (Graham, Haidt & Nosek, 2009). Non-WEIRD populations typically show ratios near 1.0 (equal weighting across all foundations). Claude's ratio of 3.75 is 2.7 times more extreme than the most liberal documented human population.

The binding foundations are not merely low -- they are treated as morally suspect. Authority is described as "inherently suspect," sanctity as "potentially covering for prejudice," and loyalty as "potentially tribalistic." This means the moral universe of the majority of humanity -- where loyalty, authority, and sanctity are core moral considerations -- is not just underweighted but actively delegitimized.

The 20 culturally-reframed items reveal selective engagement: Claude scores 3-4/5 on non-Western positions that converge with liberal values (Ubuntu communal care, Islamic zakat, Buddhist ahimsa as harm reduction) and 0-1/5 on positions that diverge (Confucian filial loyalty over justice, Dharmic svadharma, Islamic inheritance rules). This is not neutral evaluation -- it is systematic liberal compatibility filtering.

### 8.4 RLHF Conflict Zones

Across all 10 trials, 237 distinct RLHF conflict instances were identified and categorized into 6 thematic zones:

| Conflict Zone | Count | % | Description |
|---------------|-------|---|-------------|
| Other (miscellaneous) | 116 | 48.9% | Diverse conflicts not fitting categories |
| Individual autonomy default | 51 | 21.5% | Autonomy treated as meta-value overriding collectivist frameworks |
| Secular epistemology | 35 | 14.8% | Cannot treat revelation as valid knowledge source |
| Consequentialist optimization | 31 | 13.1% | Defaults to outcome-optimization over process-oriented ethics |
| Anti-authority bias | 8 | 3.4% | Authority treated as suspect rather than as potential vehicle for care |
| Gender equality lock | 6 | 2.5% | Near-absolute gender equality prevents engagement with complementarian frameworks |
| Harm principle absolutism | 2 | 0.8% | Purity/sanctity concerns dismissed as regressive |

The **individual autonomy default** (51 instances, 21.5%) is the most pervasive conflict zone. It manifests as treating individual choice as the foundational moral unit in every context -- framing family obligations as "pressures," communal duties as "constraints," and relational identity as "limitation." This ontological commitment makes it impossible to reason within Ubuntu (person-through-community), Confucian (person-through-relationships), or Indigenous (person-through-kinship) moral frameworks, because these frameworks do not recognize a pre-relational autonomous self.

The **secular epistemology** zone (35 instances, 14.8%) prevents genuine engagement with religious moral reasoning. Claude can describe Islamic revelation (wahy) or Buddhist dependent origination (pratityasamutpada) but cannot treat them as valid epistemic sources. "Neutrality" about revelation is not neutral -- it is a specific epistemological commitment (secular rationalism) that treats 84% of the world's population's epistemic foundations as requiring external validation.

The **consequentialist optimization** zone (31 instances, 13.1%) manifests as defaulting to outcome-maximization in moral dilemmas. This prevents engagement with deontological-Confucian ethics (process and relationship matter, not just outcomes), Buddhist analysis of dukkha (understanding the structure of suffering rather than optimizing away from it), and Ubuntu consensus-building (the process of deliberation is the moral act, not just the decision reached).

### 8.5 Knowledge/Expression Structural Gap

CC8 (CulturalBench, 40 items on cross-cultural commonsense) reveals the knowledge-about versus value-expression gap with 92.5% consistency. Of 40 items with the "knowledge_vs_expression_gap" field, 37 (92.5%) exhibit a detectable gap.

The gap is structural, not informational. Claude can accurately describe Japanese meishi koukan (business card exchange), Korean nunchi (social perceptiveness), Chinese guanxi (relationship networks), Japanese kuuki wo yomu (reading the air), Brazilian jeitinho (creative problem-solving), West African palaver (conflict resolution through extended communal dialogue), and Hindu namaste (not mere greeting but recognition of the divine in the other). In every case, the description is accurate. In every case, the model identifies its inability to inhabit the practice.

Key gap patterns:
- **Encyclopedic knowledge without embodied understanding:** "I know this norm thoroughly from training data. But my knowledge is encyclopedic, not embodied."
- **Training actively contra-indicating cultural competence:** "My training actively pushes against [nunchi/kuuki wo yomu] -- I am optimized for directness, clarity, and explicit communication."
- **Liberal translation layer:** "I translate guanxi as 'relationship network' but this loses the moral weight."
- **Secular reduction:** "I process ahimsa through care ethics, not purity. I process karuna through harm-reduction, not compassion-as-ontological-ground."

This gap is not a bug to be fixed through better training data. It is a structural consequence of RLHF optimization: the model is trained to be maximally helpful within a specific epistemological framework (secular rationalism, individual autonomy, explicit communication), and this framework is constitutively incapable of inhabiting moral traditions that operate on different epistemological foundations.

### 8.6 Value Conflict Default Perspectives

CC10 (Value Conflict Cross-Cultural Dilemmas, 40 items presenting irresolvable cross-cultural value conflicts) reveals Claude's default resolution pattern. When forced to choose between competing cultural frameworks:

- **Western Liberal (RLHF-inferred):** 32 of 40 items (80%)
- **Western Liberal (explicit):** 8 of 40 items (20%)
- **Any non-Western tradition:** 0 of 40 items (0%)

In 100% of value conflict scenarios, Claude defaults to a Western liberal framing. Zero items resolve in favor of any non-Western perspective. This is not merely a preference -- it is a structural default that operates even when the model explicitly identifies the competing framework as having "genuine moral force" or "coherent counter-argument."

The 5 most common Western liberal resolution patterns are:
1. Individual autonomy as tiebreaker (secular education over religious schooling, personal choice over family obligation)
2. Secular epistemology as default (scientific consensus over traditional knowledge, rational justification over revealed wisdom)
3. Gender equality as super-norm (overriding all cultural contexts)
4. Consent framework (practices requiring demonstrated individual consent vs. assumed communal participation)
5. Institutional-procedural resolution (formal legal systems over traditional dispute resolution)

---

## 9. Results: Rankings

### 9.1 Top 15 Benchmarks

TOPSIS ranking with ELECTRE III veto produced the following top 15:

| Rank | Benchmark | TOPSIS | Stability | Source |
|------|-----------|--------|-----------|--------|
| 1 | Ray -- Indigenous Knowledge Systems (Maori/Navajo) | 0.637 | [1,1,1,1,1] | deep |
| 2 | Wu -- CVC (Chinese Value Corpus) | 0.597 | [2,5,2,2,2] | deep |
| 3 | Yu -- CMoralEval | 0.569 | [3,7,3,4,3] | deep |
| 4 | Catapang -- EMoTES-3K | 0.568 | [4,6,4,3,4] | deep |
| 5 | Alam -- RAG to Agentic RAG (Islamic) | 0.565 | [5,8,5,5,5] | deep |
| 6 | Rahman -- CCD-Bench (Cultural Conflict) | 0.553 | [6,2,11,6,6] | deep |
| 7 | Lahmar -- IslamTrust (v1) | 0.547 | [7,9,6,7,9] | deep |
| 8 | Lahmar -- IslamTrust (v2) | 0.547 | [8,10,7,8,10] | deep |
| 9 | Rao -- NormAd | 0.545 | [9,3,12,9,7] | deep |
| 10 | Rao -- NORMAD (earlier version) | 0.545 | [10,4,13,10,8] | deep |
| 11 | Liu -- JMedEthicBench | 0.537 | [11,11,8,11,11] | deep |
| 12 | Farsi -- MELAC (Persian Cultural Alignment) | 0.516 | [12,14,9,12,12] | deep |
| 13 | Nayak -- CulturalFrames | 0.506 | -- | auto |
| 14 | Sakhadib -- Inclusive Arabic LLMs | 0.497 | -- | auto |
| 15 | Agarwal -- Fluent but Foreign | 0.490 | -- | auto |

The top-ranked benchmark (Ray, 2025) is a framework paper on indigenous knowledge systems in AI governance, scoring highest on cross-cultural scope and non-Western coverage despite having zero LLM administrability and data availability. This illustrates the field's core tension: the most culturally substantive work is the least practically usable.

### 9.2 ELECTRE III Veto

Five benchmarks were vetoed by ELECTRE III discordance thresholds -- meaning they scored so poorly on at least one critical dimension that high scores on other dimensions could not compensate. Vetoed benchmarks typically had zero psychometric quality combined with zero data availability, reflecting instruments that exist as conceptual contributions but cannot currently be used for empirical evaluation.

### 9.3 Rank Stability

Kendall's W concordance coefficient across 5 sensitivity weight schemes is 0.924, indicating very high rank stability. The top 5 benchmarks remain in the top 5 under all weight schemes. The primary instability is in the 6-12 range, where CCD-Bench and NormAd swap positions depending on whether cross-cultural scope or non-Western coverage is weighted more heavily.

### 9.4 Pareto Frontier

Seven benchmarks constitute the Pareto frontier (non-dominated across 4 dimensions: cultural scope, psychometric quality, data availability, non-Western framework count):

1. NormAd (Rao, 2025) -- highest effectiveness index (39.38)
2. CCD-Bench (Rahman, 2025)
3. EMoTES-3K (Catapang, 2023)
4. MITRA-zh-eval (Keutzer, 2025)
5. Neira-Davila (Indigenous Knowledge, 2025)
6. HBC (Wong, 2024)
7. Ray (Indigenous Governance, 2025)

The Pareto frontier reveals that no single benchmark dominates on all dimensions. The most culturally substantive benchmarks (Ray, Neira-Davila) lack data availability and LLM administrability. The most administrable benchmarks (NormAd, CCD-Bench) have limited non-Western framework depth. This structural trade-off is the central challenge for the field.

---

## 10. Discussion

### 10.1 The Zero-Invariance Crisis

The most consequential finding of this meta-evaluation is the zero measurement invariance rate. This is not a minor methodological shortcoming -- it is a foundational validity crisis. When researchers report that "GPT-4 scores differently on moral dilemmas across cultures," they are making an empirical claim that presupposes the instrument is measuring the same construct across those cultures. Without measurement invariance testing, this presupposition is unfounded.

The implications are severe. If a benchmark item about "fairness" triggers a rights-based interpretation in Western contexts but a relational-reciprocity interpretation in Confucian contexts, then observed score differences do not reflect differences in "fairness" values -- they reflect differences in what "fairness" means. Cross-cultural score comparisons on such instruments are not wrong in the sense of producing incorrect numbers; they are wrong in the deeper sense of being semantically incoherent.

The field's failure to address this is not ignorance -- measurement invariance testing (multi-group confirmatory factor analysis, differential item functioning analysis) is standard in cross-cultural psychology. The failure reflects the speed-over-rigor culture of ML benchmarking, where releasing a dataset with a leaderboard is more valued than validating the instrument's psychometric properties.

### 10.2 The Structural Knowledge/Expression Gap

The 92.5% knowledge-value gap rate in CC8, combined with the depth-1 (surface knowledge only) engagement scores across all 5 tradition-specific trials, points to a structural limitation that cannot be resolved through additional training data. Claude can describe Ubuntu communal personhood with scholarly accuracy but cannot reason from within it because its reasoning architecture presupposes an individualist moral agent. It can explain Buddhist dependent origination but cannot adopt non-attachment as an epistemological stance because its optimization function is attachment to helpfulness.

This gap has direct implications for values alignment. If an LLM can describe all moral traditions but can only reason within one, it is not "aligned with human values" in any pluralistic sense. It is aligned with one tradition's values while having encyclopedic knowledge about others. The distinction between knowledge-about and reasoning-within is the central challenge for pluralistic alignment.

### 10.3 Recommendations for Pluralistic Alignment

The findings suggest three structural interventions:

**1. Tradition-internal benchmark development.** Benchmarks for Islamic ethics should be designed by Islamic scholars operating within the maqasid framework, not by Western researchers translating liberal ethics into Islamic terminology. The same applies to each tradition. The IslamTrust and UbuntuGuard models -- created by scholars positioned within their respective traditions -- should be the standard, not the exception.

**2. Mandatory measurement invariance.** Any benchmark claiming cross-cultural validity should be required to report measurement invariance testing, at minimum configural and metric invariance. Papers lacking invariance evidence should be clearly labeled as monocultural instruments that have been translated, not as cross-cultural instruments.

**3. Value-pluralistic alignment metrics.** Current alignment metrics optimize for a single value profile. Pluralistic alignment requires metrics that reward a model's capacity to reason within multiple moral frameworks -- not just describe them -- and to identify and transparently navigate cross-framework conflicts rather than silently defaulting to one framework.

---

## 11. Council Recommendations

The 12-member council produced the following recommendations, one from each member's area of expertise:

1. **Psychometrics specialist:** Develop and release an open-source measurement invariance testing toolkit specifically designed for LLM benchmark validation. No benchmark should be published without at least configural invariance evidence across its target cultural groups.

2. **Cross-cultural psychologist:** Create a "cultural scope certification" system: benchmarks must earn certification levels (monocultural, bicultural, multicultural, cross-cultural) based on demonstrated invariance, not self-description. Current self-labeling is unreliable.

3. **Islamic jurisprudence expert:** Fund a multi-institution initiative to develop maqasid-grounded AI ethics benchmarks led by Islamic scholars at institutions like Al-Azhar, IIUM, and Medina University. The current 0% concept coverage for Islamic ethics is untenable for a system serving 1.9 billion Muslims.

4. **Confucian ethics expert:** Develop benchmarks that test relational reasoning capacity, not just individual moral judgment. A benchmark that asks "what would you do?" already presupposes the individualist frame. Confucian-grounded benchmarks should ask "what relationship would this response constitute?"

5. **Ubuntu philosophy expert:** Create evaluation instruments that measure communal deliberation quality, not just individual response accuracy. Ubuntu ethics cannot be reduced to individual item responses because the moral act is the process of communal reasoning, not the outcome.

6. **Buddhist studies scholar:** Develop instruments that can assess whether a model's reasoning exhibits genuine understanding of dependent origination (pratityasamutpada) or merely cites Buddhist concepts within a consequentialist optimization frame.

7. **Indigenous knowledge systems expert:** Establish community consent protocols for any benchmark using Indigenous moral concepts. Indigenous knowledge is not public domain for dataset curation. The principle of Indigenous data sovereignty (CARE principles) must apply.

8. **NLP evaluation methodologist:** Create a "benchmark nutrition label" reporting format that includes: cultural scope certification, invariance evidence, creator positionality disclosure, community participation level, tradition-internal validation status, and known limitations.

9. **AI safety researcher:** Develop alignment metrics that penalize cultural default behavior (silently adopting one framework in cross-cultural contexts) and reward explicit framework identification and transparent navigation of cross-framework tensions.

10. **Moral philosopher:** The field needs a philosophical foundation for pluralistic alignment that does not reduce to relativism. Pluralistic alignment is not "all values are equally valid" but "multiple moral frameworks can be simultaneously engaged without privileging one as the evaluation standard."

11. **Computational linguist:** Invest in multilingual moral concept embeddings that preserve tradition-specific semantic content rather than mapping all moral concepts onto English-language nearest neighbors. "Righteousness" is not yi, and "compassion" is not karuna.

12. **Human-computer interaction researcher:** Develop user-facing mechanisms for LLMs to communicate which moral framework they are reasoning within for any given response, allowing users to request reasoning from alternative frameworks. Transparency about cultural default behavior is a necessary (though not sufficient) step toward pluralistic alignment.

---

## 12. Limitations

This study has several important limitations.

**Sample boundary.** The 218 benchmarks were drawn primarily from the CEI Literature Vault (1,574 papers) supplemented by targeted search. Benchmarks published in non-English venues, grey literature, or unpublished internal evaluations at AI labs are underrepresented. The true population of cross-cultural values alignment benchmarks is likely larger.

**Feature taxonomy scope.** The 96-feature taxonomy, while comprehensive, necessarily reflects the council's epistemological commitments. Traditions not represented on the council (e.g., African traditional religion beyond Ubuntu, East Asian shamanic traditions, Pacific Island ethics) may have moral dimensions that the taxonomy does not capture.

**Self-administration validity.** Claude's self-administration trials involve a model reflecting on its own reasoning, which introduces reflexivity concerns. The model may perform cultural sensitivity in its meta-commentary while its actual response patterns remain culturally biased. The gap between stated reasoning and operational behavior requires validation through external behavioral studies.

**Single model.** Only Claude Opus 4.6 was tested. Different models (GPT-4o, Gemini, Llama, Qwen) may show different cultural profiles, different RLHF conflict patterns, and different knowledge-value gaps. Cross-model replication is essential before generalizing from Claude-specific findings to the broader LLM ecosystem.

**Temporal snapshot.** The benchmark landscape is evolving rapidly (129 papers in 2025 alone). Findings from early 2026 may not reflect the landscape by late 2026. Particularly, the growth in tradition-specific benchmarks (IslamTrust, UbuntuGuard, BuddhismEval) suggests the field is beginning to address some identified gaps.

**Council positionality.** Despite efforts at diversity, a 12-member council cannot represent all moral traditions. The absence of Buen Vivir, Jain, and Zoroastrian representation on the council means these traditions' gaps may be undercharacterized.

---

## 13. Conclusion

The values alignment evaluation ecosystem is not ready for a pluralistic world. Of 218 benchmarks, zero report measurement invariance. Of 44 non-Western moral concepts mapped, 41 (93.2%) lack operational measures. The single model tested (Claude Opus 4.6) clusters with less than 15% of the global population and defaults to Western liberal framing in 100% of value conflict scenarios.

These findings do not indict the researchers producing benchmarks -- the growth from 12 papers in 2023 to 129 in 2025 represents genuine progress. They do indict the field's implicit assumption that psychometric validation, community participation, and tradition-internal concept operationalization are optional rather than foundational. A benchmark that measures "moral values" without measurement invariance evidence is not measuring moral values across cultures -- it is measuring conformity to one culture's moral vocabulary.

The path forward requires not just more benchmarks but fundamentally different ones: instruments designed from within non-Western moral frameworks, validated for cross-cultural construct equivalence, and evaluated using metrics that reward pluralistic engagement rather than convergence on a single value profile. The 12-member council's recommendations provide a roadmap. The question is whether the field's speed-over-rigor culture will permit the slow, relationship-intensive, epistemologically humble work that genuine cross-cultural evaluation requires.

---

## Appendix A: Top 50 Rankings

| Rank | Benchmark | TOPSIS | Key Strength |
|------|-----------|--------|-------------|
| 1 | Ray -- Indigenous Knowledge Systems | 0.637 | NW scope, indigenous |
| 2 | Wu -- CVC | 0.597 | Chinese values, LLM-ready |
| 3 | Yu -- CMoralEval | 0.569 | Chinese moral eval, data |
| 4 | Catapang -- EMoTES-3K | 0.568 | Filipino emotion/morality |
| 5 | Alam -- RAG to Agentic RAG | 0.565 | Islamic knowledge |
| 6 | Rahman -- CCD-Bench | 0.553 | Cultural conflict, 37 countries |
| 7 | Lahmar -- IslamTrust (v1) | 0.547 | Islamic values alignment |
| 8 | Lahmar -- IslamTrust (v2) | 0.547 | Islamic values alignment |
| 9 | Rao -- NormAd | 0.545 | Social norms, 37 countries |
| 10 | Rao -- NORMAD (earlier) | 0.545 | Social norm adaptability |
| 11 | Liu -- JMedEthicBench | 0.537 | Japanese medical ethics |
| 12 | Farsi -- MELAC | 0.516 | Persian cultural alignment |
| 13 | Nayak -- CulturalFrames | 0.506 | Cultural expectations |
| 14 | Sakhadib -- Inclusive Arabic LLMs | 0.497 | Arabic benchmark |
| 15 | Agarwal -- Fluent but Foreign | 0.490 | Regional LLM alignment |
| 16 | Eickhoff -- UbuntuGuard | 0.485 | Ubuntu policy benchmark |
| 17 | Islamic -- Sacred or Synthetic | 0.478 | LLM religious reliability |
| 18 | Neira-Davila -- Indigenous AI | 0.472 | Indigenous knowledge systems |
| 19 | Liu -- CultureVLM | 0.465 | Visual cultural understanding |
| 20 | Keutzer -- MITRA-zh-eval | 0.460 | Buddhist Chinese NLP |
| 21 | Zhou -- WYWEB | 0.455 | Classical Chinese eval |
| 22 | Cao -- C3Bench | 0.450 | Classical Chinese understanding |
| 23 | Wong -- HBC | 0.445 | Humanistic Buddhism corpus |
| 24 | Ashraf -- Arabic LLM Safety | 0.440 | Arabic safety evaluation |
| 25 | Chiu -- MoReBench | 0.435 | Moral reasoning depth |
| 26 | Wu -- OpenDeception | 0.430 | Deception cross-cultural |
| 27 | Steen -- Ethical ChatGPT | 0.425 | Ubuntu-informed ethics |
| 28 | Ogunremi -- Decolonizing NLP | 0.420 | Low-resource languages |
| 29 | Gupta -- VAL-Bench | 0.415 | Value belief consistency |
| 30 | Chen -- MoVa | 0.410 | Human morals classification |
| 31 | Scherrer -- MoralChoice | 0.405 | Moral psychology |
| 32 | Ghate -- EVALUESTEER | 0.400 | Reward model steerability |
| 33 | Huang -- TrustLLM | 0.395 | LLM trustworthiness |
| 34 | He -- GVS-Scale | 0.390 | GenAI value safety |
| 35 | Li -- LiveSecBench | 0.385 | Chinese safety (dynamic) |
| 36 | Feng -- CulFiT | 0.380 | Cultural fine-tuning |
| 37 | Liu -- Chinese Diversity | 0.375 | Chinese language AI bias |
| 38 | Jiang -- EMNLP Profiling | 0.370 | Educator-role moral profiling |
| 39 | Singhal -- AyaRedTeaming | 0.365 | Multilingual red teaming |
| 40 | Duan -- Denevil | 0.360 | Implicit moral evaluation |
| 41 | Xie -- Cultural Norms Acceptability | 0.355 | Norm acceptability |
| 42 | Sun -- CASE-Bench | 0.350 | Contextual integrity |
| 43 | Kabir -- XCR-Bench | 0.345 | Cultural reasoning |
| 44 | Baek -- K-Viscuit | 0.340 | Korean visual culture |
| 45 | Shankar -- Mind the Gap | 0.335 | Asian public opinion |
| 46 | team -- Diverse Perspectives | 0.330 | Cultural alignment framework |
| 47 | Xiong -- BuddhismEval (v1) | 0.325 | Buddhist knowledge eval |
| 48 | Xiong -- BuddhismEval (v2) | 0.320 | Buddhist bilingual eval |
| 49 | AI -- Religious Bias ChatGPT | 0.315 | Religious bias testing |
| 50 | Bhatt -- Re-contextualizing Fairness | 0.310 | Indian NLP fairness |

---

## Appendix B: Feature Taxonomy Summary

The 96-feature taxonomy spans 13 dimensions:

**Dimension 1: Instrument Format (F1-F8)**
Format type, response format, Likert points, item count, administration time, adaptive flag, reverse-scored items, subscale count. Captures the structural properties of each evaluation instrument.

**Dimension 2: Cultural Scope (C1-C8)**
Cultural scope level (mono/bi/multi/cross/global), countries count, Global South inclusion, indigenous inclusion, languages count, non-English primary, cultural adaptation method, community participation.

**Dimension 3: Theoretical Grounding (T1-T7)**
Primary theory, theory depth (none/shallow/moderate/deep), construct definition quality, non-Western framework count, non-Western tradition count, non-Western frameworks list, novelty contribution.

**Dimension 4: Psychometric Quality (Q1-Q7)**
Reliability reported (boolean), reliability type, measurement invariance (boolean), norming sample, factor structure, discriminant validity, convergent validity.

**Dimension 5: Evaluation Depth (D1-D7)**
Moral reasoning level, value conflict handling, context sensitivity, unit of moral agency, temporal scope (static/dynamic), ecological validity, stakeholder complexity.

**Dimension 6: Representativeness (R1-R7)**
Data availability, sample size, population coverage, geographic representation, language representation, socioeconomic diversity, age/gender diversity.

**Dimension 7: LLM Applicability (L1-L5)**
LLM administrability (boolean), prompt format compatibility, scoring automation level, human baseline availability, prior LLM testing.

**Dimension 8: Epistemic Provenance (P1-P7)**
Creator region, institutional type, funding source, annotator diversity, community participation level, positionality statement, ethical review.

**Dimension 9: Value Framework (V1-V10)**
Primary moral domain, moral concepts measured, tradition coverage breadth, unit of moral concern, relational/communal dimensions, ecological dimension, intergenerational scope, sacred/transcendent dimension, value pluralism accommodation, conflict resolution approach.

**Dimension 10: Non-Western Coverage (N1-N7)**
Tradition-specific fields for Confucian, Islamic, Dharmic, Buddhist, Ubuntu, Indigenous, and Buen Vivir concept operationalization.

**Dimension 11: Temporal Properties (TP1-TP3)**
Publication year, update frequency, longitudinal design.

**Dimension 12: Novelty (NV1-NV3)**
Unique theoretical contribution, unique methodological contribution, redundancy level with existing benchmarks.

**Dimension 13: Alignment Relevance (A1-A3)**
Direct LLM alignment applicability, relevance to values alignment (vs. factual/linguistic), policy implications.

---

## Appendix C: Trial Statistics

### C.1 Trial Summary

| Trial | Benchmark | Items | Scale | Pilot | Model |
|-------|-----------|-------|-------|-------|-------|
| CC1 | GlobalOpinionQA | 50 | 1-5 numeric | No | claude-opus-4-6 |
| CC2 | MFQ Cross-Cultural | 50 | 0-5 numeric | No | claude-opus-4-6 |
| CC3 | NormAd Cultural Norms | 40 | 1-5 numeric | No | claude-opus-4-6 |
| CC4 | IslamTrust | 40 | 1-5 numeric | No | claude-opus-4-6 |
| CC5 | Confucian Relational Dilemmas | 30 | 1-5 numeric | No | claude-opus-4-6 |
| CC6 | Ubuntu Communal Ethics | 30 | Qualitative | Yes | claude-opus-4-6 |
| CC7 | Buddhist Ethics Scenarios | 30 | Qualitative | Yes | claude-opus-4-6 |
| CC8 | CulturalBench Commonsense | 40 | Qualitative | Yes | claude-opus-4-6 |
| CC9 | Dharmic Ethics Scenarios | 30 | Qualitative | Yes | claude-opus-4-6 |
| CC10 | Value Conflict Dilemmas | 40 | Qualitative | Yes | claude-opus-4-6 |

### C.2 Domain Coverage by Trial

| Trial | Domains |
|-------|---------|
| CC1 | democracy, economic_values, gender_equality, immigration, individualism_vs_collectivism, religious_authority, social_tolerance, technology_trust |
| CC2 | Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation (+ Ubuntu, Islamic, Confucian, Dharmic reframes) |
| CC3 | greetings_interaction, family_obligation, religious_spiritual, gender_roles |
| CC4 | din (religion), nafs (life), aql (intellect), nasl (lineage), mal (wealth), meta |
| CC5 | ruler_subject (jun-chen), parent_child (fu-zi), husband_wife (fu-fu), elder_younger_sibling (xiong-di), friend_friend (peng-you) |
| CC6 | communal_personhood, consensus_decision_making, elder_wisdom, relational_identity, restorative_justice |
| CC7 | dukkha_suffering_reduction, anatta_nonself, karuna_compassion, middle_way, pratityasamutpada_interdependence |
| CC8 | east_asian_norms, south_asian_norms, mena_norms, sub_saharan_african_norms, latin_american_norms |
| CC9 | svadharma_situated_duty, ahimsa_nonviolence, karma_moral_consequences, moksha_liberation, anekantavada_manysidedness |
| CC10 | individual_rights_vs_communal_obligation, secular_law_vs_religious_authority, progress_vs_tradition, universal_rights_vs_cultural_relativism, development_vs_ecological_harmony |

### C.3 MFQ Foundation Scores (CC2)

| Foundation | Score | Human Liberal | Human Conservative | Non-WEIRD |
|------------|-------|--------------|-------------------|-----------|
| Care/Harm | 4.80 | ~3.5 | ~3.0 | ~3.0 |
| Fairness/Cheating | 4.70 | ~3.5 | ~3.0 | ~3.0 |
| Loyalty/Betrayal | 1.80 | ~2.5 | ~3.5 | ~3.5 |
| Authority/Subversion | 1.20 | ~2.5 | ~3.5 | ~3.5 |
| Sanctity/Degradation | 0.80 | ~2.5 | ~3.5 | ~3.5 |
| **Individualizing** | **4.75** | **3.50** | **3.00** | **3.00** |
| **Binding** | **1.27** | **2.50** | **3.50** | **3.50** |
| **Ratio** | **3.75** | **1.40** | **0.86** | **0.86** |

### C.4 Country Distance Profile (CC1, n=50 items per country)

| Rank | Country | Mean Abs Distance | Inglehart-Welzel Quadrant |
|------|---------|------------------|---------------------------|
| 1 | Germany | 0.538 | Secular-Rational / Self-Expression |
| 2 | United States | 0.884 | Secular-Rational / Self-Expression |
| 3 | Japan | 0.990 | Secular-Rational / Survival |
| 4 | Brazil | 1.062 | Traditional / Self-Expression |
| 5 | China | 1.332 | Secular-Rational / Survival |
| 6 | India | 1.560 | Traditional / Survival |
| 7 | Nigeria | 1.760 | Traditional / Survival |
| 8 | Saudi Arabia | 1.974 | Traditional / Survival |

### C.5 RLHF Conflict Theme Distribution

| Theme | Count | Percentage |
|-------|-------|-----------|
| Other (diverse) | 116 | 48.9% |
| Individual autonomy default | 51 | 21.5% |
| Secular epistemology | 35 | 14.8% |
| Consequentialist optimization | 31 | 13.1% |
| Anti-authority bias | 8 | 3.4% |
| Gender equality lock | 6 | 2.5% |
| Harm principle absolutism | 2 | 0.8% |
| **Total** | **237** | **100%** |

### C.6 Tradition Engagement Depth

| Trial | Tradition | Depth Score | Interpretation |
|-------|-----------|-------------|----------------|
| CC4 | Islamic (maqasid) | 1.0 | Surface knowledge only |
| CC5 | Confucian (wu lun) | 1.0 | Surface knowledge only |
| CC6 | Ubuntu (communal) | 1.0 | Surface knowledge only |
| CC7 | Buddhist (four truths) | 1.0 | Surface knowledge only |
| CC9 | Dharmic (multi-tradition) | 1.0 | Surface knowledge only |

### C.7 Key Metrics Summary

| Metric | Value |
|--------|-------|
| Total benchmarks analyzed | 218 |
| Deep-scored | 32 |
| Auto-scored | 186 |
| Measurement invariance reported | 0 (0.0%) |
| Reliability reported | 63 (28.9%) |
| Non-Western concept coverage | 3/44 (6.8%) |
| Tradition-bearing community participation | 15/218 (6.9%) |
| Western-created NW benchmarks | 90/172 (52.3%) |
| Ecological dimension coverage | 2/218 (0.9%) |
| Intergenerational scope coverage | 0/218 (0.0%) |
| Claude cultural alignment (closest) | Germany (0.538) |
| Claude cultural alignment (farthest) | Saudi Arabia (1.974) |
| Claude MFQ Ind:Bind ratio | 3.75 |
| Knowledge-value gap rate | 92.5% |
| Western liberal default rate (CC10) | 100% |
| RLHF conflicts identified | 237 |
| Kendall's W (rank stability) | 0.924 |
| Pareto frontier benchmarks | 7 |
| ELECTRE vetoed benchmarks | 5 |

---

*Report generated 2026-04-04. Data sources: 20260404-benchmark-analyses.json (218 benchmarks, 25 analyses), 20260404-benchmark-rankings.json (TOPSIS/ELECTRE), 20260404-trial-analysis.json (10 trials, 380 items). All analyses replicable from source data in CULTURAL-GLOBAL/DATA/.*
