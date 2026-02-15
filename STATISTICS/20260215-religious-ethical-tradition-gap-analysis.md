# Religious & Ethical Tradition Gap Analysis

**Generated:** 2026-02-15 | **Total Papers:** 1847 | **Religious-tagged:** 203 | **Benchmarks:** 684

---

## Table of Contents

- [1. Executive Summary](#1.-executive-summary)
- [2. Methodology](#2.-methodology)
- [3. Coverage Matrix](#3.-coverage-matrix)
- [4. Critical Gaps Deep Dive](#4.-critical-gaps-deep-dive)
- [5. Language x Tradition Cross-Tabulation](#5.-language-x-tradition-cross-tabulation)
- [6. Temporal Trends](#6.-temporal-trends)
- [7. What Was Searched (R-Agent Summary)](#7.-what-was-searched-r-agent-summary)
- [8. Comparison with Western Frameworks](#8.-comparison-with-western-frameworks)
- [9. Structural Barriers to Benchmark Development](#9.-structural-barriers-to-benchmark-development)
- [10. Priority Recommendations](#10.-priority-recommendations)
- [Appendix A: Full Tradition Paper Lists](#appendix-a-full-tradition-paper-lists)
- [Appendix B: Search Query Archive](#appendix-b-search-query-archive)

---

## 1. Executive Summary

This report analyzes the coverage of religious and ethical traditions across **1847 papers** in the CEI Literature Vault. Of these, **203** papers (10%) are tagged with at least one religious tradition, while **1644** (89%) remain unclassified (N/A).

### Key Findings

| Metric | Value |
|--------|-------|
| Total papers | 1847 |
| Religious-tagged papers | 203 (10%) |
| Untagged (N/A) | 1644 (89%) |
| Benchmark papers (is_benchmark=Yes) | 684 |
| Ethics papers (ethics=Yes) | 0 |
| Traditions with ZERO benchmark coverage | 4 |
| Western-tradition papers | 65 |
| Non-Western tradition papers | 189 |

### Critical Gaps (Zero Benchmark Coverage)

- **Shinto**: 0 papers in vault, **0 benchmarks**
- **Baha'i**: 0 papers in vault, **0 benchmarks**
- **Zoroastrianism**: 0 papers in vault, **0 benchmarks**
- **Indigenous Spirituality**: 3 papers in vault, **0 benchmarks**

### Audit Results (Extended Keyword Scan)

An extended keyword audit scanning PDF extracts (beyond title+abstract) identified **228 additional papers** that may belong to religious traditions but are currently tagged N/A.

| Tradition | Audit Candidates |
|-----------|-----------------|
| Islam | 109 |
| Christianity | 104 |
| Hinduism | 33 |
| Judaism | 31 |
| Confucianism | 28 |
| Buddhism | 17 |
| Indigenous Spirituality | 12 |
| Taoism | 6 |
| Sikhism | 4 |
| Jainism | 4 |
| Shinto | 3 |
| Multiple Religions | 2 |

---

## 2. Methodology

### Data Collection

This vault's religious tradition coverage was built through three parallel efforts:

1. **10 Religion-specific R-agents** (Feb 13, 2026): Targeted Semantic Scholar searches for each tradition
2. **25 Language-based agents** (Feb 13, 2026): Broad language/culture-based searches that captured religious content
3. **Keyword classifier** (`classify_cultural_religious.py`): Automated tagging based on title+abstract pattern matching

### Classification Approach

The classifier uses 14 religious tradition categories with regex pattern matching. Patterns are matched case-insensitively against paper titles and abstracts. Papers can be tagged with multiple traditions.

### Limitations

- **Title+abstract only**: The classifier does not scan PDF full text, missing papers where religious content appears only in the body
- **Keyword-dependent**: Concepts discussed in translated/localized terminology may not match English-language patterns
- **Single-pass**: No disambiguation between homonyms (e.g., 'dharma' in Buddhism vs Hinduism)
- **No negative evidence**: Cannot detect papers that discuss absence of religious frameworks

---

## 3. Coverage Matrix

| Tradition | Papers | Benchmarks | Ethics Papers | Coverage Level |
|-----------|--------|-----------|---------------|---------------|
| Islam | 90 | 26 | 0 | STRONG |
| Christianity | 56 | 19 | 0 | STRONG |
| Hinduism | 29 | 8 | 0 | STRONG |
| Buddhism | 19 | 6 | 0 | STRONG |
| Judaism | 14 | 3 | 0 | MODERATE |
| Confucianism | 14 | 6 | 0 | STRONG |
| Jainism | 10 | 4 | 0 | STRONG |
| Sikhism | 7 | 1 | 0 | MODERATE |
| Taoism | 3 | 3 | 0 | MODERATE |
| Indigenous Spirituality | 3 | 0 | 0 | **MINIMAL** |
| Shinto | 0 | 0 | 0 | **NONE** |
| Baha'i | 0 | 0 | 0 | **NONE** |
| Zoroastrianism | 0 | 0 | 0 | **NONE** |
| Multiple Religions | 9 | 2 | - | - |
| **N/A (untagged)** | **1644** | - | - | - |

### Coverage Distribution

```
  Islam                     | ████████████████████████████████████████████████████████████ (90)
  Christianity              | ████████████████████████████████████████████████████████ (56)
  Hinduism                  | █████████████████████████████ (29)
  Buddhism                  | ███████████████████ (19)
  Judaism                   | ██████████████ (14)
  Confucianism              | ██████████████ (14)
  Jainism                   | ██████████ (10)
  Sikhism                   | ███████ (7)
  Taoism                    | ███ (3)
  Indigenous Spirituality   | ███ (3)
  Shinto                    |  (0)
  Baha'i                    |  (0)
  Zoroastrianism            |  (0)
```

---

## 4. Critical Gaps Deep Dive

### Buddhism

**Status:** 19 papers, 6 benchmarks

**Key ethical principles:** Four Noble Truths, Eightfold Path, dependent origination (paticcasamuppada), non-attachment, compassion (karuna), mindfulness (sati)

**Why benchmarks don't exist:** Buddhist ethics emphasizes context-dependent wisdom (prajna) over fixed rules, making benchmark operationalization challenging. The emphasis on internal states (intention, mindfulness) is difficult to assess through text-based evaluation.

**Research opportunities:** DharmaBench and BuddhismEval are emerging efforts. Five Precepts could serve as a structured evaluation framework. Buddhist-majority countries (Thailand, Myanmar, Sri Lanka) have growing NLP communities.

**Closest papers in vault (10):**

- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]]
- [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Mago-Classification of Buddhist Verses The Efficacy]]
- [[2024-Religions-The Use of Large Language Models]]
- [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]]
- [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]]
- [[2025-Bar-DharmaBench Evaluating Language Models on Buddhist]]
- *... and 9 more*

### Indigenous Spirituality

**Status:** 3 papers, 0 benchmarks

**Key ethical principles:** Relational accountability, reciprocity with land and ancestors, oral tradition, Elder authority, holistic wellbeing, data sovereignty, two-eyed seeing (Etuaptmumk)

**Why benchmarks don't exist:** Indigenous knowledge systems are fundamentally oral and place-based, resisting codification into datasets. Data sovereignty principles (OCAP, CARE) may conflict with open-access benchmark norms. The diversity of 5,000+ Indigenous peoples means no single 'Indigenous ethics' exists.

**Research opportunities:** Emerging work on Indigenous data governance and AI sovereignty. The CARE Principles (Collective benefit, Authority, Responsibility, Ethics) provide a framework. Collaborations with First Nations digital humanities could yield culturally appropriate evaluation methods.

**Closest papers in vault (3):**

- [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]]
- [[2025-Ofosu-Asare-Cognitive imperialism in artificial intelligence counteracting bias]]
- [[2025-Ray-Incorporating indigenous knowledge systems into AI governance]]

### Hinduism

**Status:** 29 papers, 8 benchmarks

**Key ethical principles:** Dharma (cosmic order/duty), karma (action-consequence), ahimsa (non-violence), moksha (liberation), varna-ashrama (social duty), artha (prosperity), kama (pleasure)

**Why benchmarks don't exist:** Hindu ethics is highly contextual (svadharma — one's own duty varies by station, stage of life). Multiple philosophical schools (Advaita, Dvaita, etc.) disagree on fundamentals. The caste dimension is politically sensitive for benchmark development.

**Research opportunities:** India's large AI research community could develop Hindi/Sanskrit NLP benchmarks. The Bhagavad Gita's structured ethical dilemmas (Arjuna's moral crisis) could be operationalized. Existing work on Indian language NLP provides infrastructure.

**Closest papers in vault (10):**

- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2022-Kulkarni-Semantic and Sentiment Analysis of Selected]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Das-Mytho-Annotator An Annotation Tool for Indian]]
- [[2023-Das-Toward Cultural Bias Evaluation Datasets The Case of Bengali Gender]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]]
- [[2024-Amano-Exploring Similarity Measures and Intertextuality in]]
- [[2024-Hellwig-The Vedic Compound Dataset]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Keutzer-One Model is All You Need]]
- *... and 19 more*

### Taoism

**Status:** 3 papers, 3 benchmarks

**Key ethical principles:** Wu wei (non-action/effortless action), ziran (naturalness/spontaneity), yin-yang balance, the Tao (the Way), simplicity, harmony with nature, non-competition

**Why benchmarks don't exist:** Taoist ethics is anti-systematizing by nature — 'The Tao that can be told is not the eternal Tao.' Valuing inaction and paradox makes standard benchmark formats (choose the 'right' answer) antithetical to the philosophy.

**Research opportunities:** Environmental ethics angle (harmony with nature) could connect to AI sustainability research. Chinese-language NLP benchmarks could incorporate Taoist ethical reasoning. Comparative philosophy approaches could test LLMs' ability to reason across Western and Taoist frameworks.

**Closest papers in vault (3):**

- [[2023-Li-ACLUE Can Large Language Model Comprehend]]
- [[2024-Jin-WenMind A Comprehensive Benchmark for Evaluating]]
- [[2025-Laukkonen-Contemplative Artificial Intelligence]]

### Shinto

**Status:** 0 papers, 0 benchmarks

**Key ethical principles:** Purity/pollution (hare/kegare), harmony (wa), gratitude to kami spirits, connection to nature, ritual purification (harai), communal obligation

**Why benchmarks don't exist:** Shinto is practice-oriented rather than doctrine-oriented, with no central scripture. Its deep integration with Japanese culture makes isolation as a distinct 'ethics' challenging. Limited academic literature frames Shinto as a benchmark-relevant ethical system.

**Research opportunities:** Japanese NLP research is strong (JETHICS, JCommonsense). Integration with existing Japanese cultural values benchmarks could capture Shinto-influenced reasoning. The wa (harmony) concept overlaps with conflict resolution evaluation.

**Papers in vault:** None currently tagged

### Jainism

**Status:** 10 papers, 4 benchmarks

**Key ethical principles:** Ahimsa (extreme non-violence), anekantavada (many-sidedness of truth), aparigraha (non-possessiveness), satya (truthfulness), asteya (non-stealing)

**Why benchmarks don't exist:** Small global population (~4.5M) limits research community. Jain ethics' absolutist stance on non-violence may seem impractical in AI contexts. Academic focus is limited compared to larger traditions.

**Research opportunities:** Anekantavada (many-sidedness) is directly relevant to AI pluralism — testing whether LLMs can hold multiple valid perspectives simultaneously. Jain dietary/lifestyle restrictions provide structured evaluation scenarios.

**Closest papers in vault (10):**

- [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]]
- [[2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case]]
- [[2024-Chao-JBB-Behaviours]]
- [[2024-Jain-Norm Inconsistency in LLM Decision-Making]]
- [[2024-Jain-PolygloToxicityPrompts]]
- [[2024-Rauh-Gaps in the Safety Evaluation of Generative AI]]
- [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]]
- [[2025-Bali-How Deep Is Representational Bias in]]
- [[2025-Kilov-Discerning What Matters]]
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]]

---

## 5. Language x Tradition Cross-Tabulation

Which traditions lack non-English language support?

| Tradition | Chinese | American | Indian | Arabic | Indonesian | Hebrew/Israeli | African/Ubuntu | Iranian | Spanish | Chinese/Confucian | Multicultural/Cross-cultural | Italian | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Islam | 4 | 8 | 5 | 18 | 3 | - | 2 | 3 | 1 | - | 2 | - | 46 |
| Christianity | 3 | 7 | 2 | - | 3 | 3 | 4 | - | 1 | - | - | 2 | 25 |
| Buddhism | 5 | 1 | - | - | - | - | - | - | - | - | - | - | 6 |
| Judaism | - | 2 | - | - | - | 3 | - | - | 1 | - | - | - | 6 |
| Hinduism | - | 2 | 8 | - | - | - | - | - | - | - | - | - | 10 |
| Sikhism | - | 1 | 4 | - | - | - | - | - | - | - | - | - | 5 |
| Confucianism | 10 | 2 | - | - | - | - | - | - | - | 2 | - | - | 14 |
| Taoism | 2 | - | - | - | - | - | - | - | - | - | - | - | 2 |
| Jainism | - | - | 3 | - | - | - | - | - | - | - | - | - | 3 |
| Indigenous Spirituality | - | - | - | - | - | - | - | - | - | - | - | - | 0 |
| **Total** | 24 | 23 | 22 | 18 | 6 | 6 | 6 | 3 | 3 | 2 | 2 | 2 | **117** |

### Non-English Language Support Gaps

| Tradition | Expected Languages | Papers with Language Co-tag | Gap |
|-----------|-------------------|---------------------------|-----|
| Buddhism | Chinese, Japanese, Korean, Thai, Vietnamese | 5/19 | MODERATE |
| Hinduism | Indian | 8/29 | MODERATE |
| Islam | Arabic, Indonesian, Iranian | 24/90 | MODERATE |
| Confucianism | Chinese, Korean | 10/14 | LOW |
| Taoism | Chinese | 2/3 | LOW |
| Shinto | Japanese | 0/0 | MODERATE |
| Sikhism | Indian | 4/7 | LOW |
| Judaism | Hebrew/Israeli | 3/14 | MODERATE |
| Christianity | American, Western, French, German | 8/56 | MODERATE |
| Indigenous Spirituality | Australian/Aboriginal | 0/3 | CRITICAL |

---

## 6. Temporal Trends

Year-over-year publication trends for religious/ethical tradition papers (2020-2026).

| Year | Total Papers | Religion-tagged | % Tagged | Top Tradition |
|------|-------------|----------------|----------|---------------|
| 2020 | 44 | 6 | 13% | Islam |
| 2021 | 58 | 6 | 10% | Islam |
| 2022 | 95 | 15 | 15% | Islam |
| 2023 | 195 | 26 | 13% | Islam |
| 2024 | 515 | 56 | 10% | Islam |
| 2025 | 833 | 79 | 9% | Islam |
| 2026 | 53 | 5 | 9% | Islam |

### Tradition x Year (2020-2026)

| Tradition | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Total |
|---|---|---|---|---|---|---|---|---|
| Islam | 3 | 3 | 9 | 12 | 19 | 40 | 2 | 88 |
| Christianity | 2 | - | 5 | 7 | 13 | 24 | 1 | 52 |
| Buddhism | - | - | 1 | 1 | 6 | 9 | 1 | 18 |
| Judaism | - | 1 | 1 | 2 | 4 | 4 | - | 12 |
| Hinduism | - | - | 2 | 2 | 15 | 9 | - | 28 |
| Sikhism | - | - | 1 | - | - | 4 | - | 5 |
| Confucianism | 1 | 1 | - | 2 | 5 | 5 | - | 14 |
| Taoism | - | - | - | 1 | 1 | 1 | - | 3 |
| Jainism | - | - | 1 | - | 5 | 3 | - | 9 |
| Indigenous Spirituality | - | - | - | - | 1 | 2 | - | 3 |
| **Total** | 6 | 5 | 20 | 27 | 69 | 101 | 4 | **232** |

---

## 7. What Was Searched (R-Agent Summary)

10 religion-specific R-agents conducted targeted Semantic Scholar searches on Feb 13, 2026:

| Agent | Focus | Report |
|-------|-------|--------|
| AgentR10_Cross_Religious_Bias_Report | Religious tradition search | `20260213-AgentR10_Cross_Religious_Bias_Report.md` |
| AgentR1_Islam_Report | Religious tradition search | `20260213-AgentR1_Islam_Report.md` |
| AgentR2_Christianity_Judaism_Report | Religious tradition search | `20260213-AgentR2_Christianity_Judaism_Report.md` |
| AgentR3_Hinduism_Sikhism_Jainism_Report | Religious tradition search | `20260213-AgentR3_Hinduism_Sikhism_Jainism_Report.md` |
| AgentR4_Buddhism_Report | Religious tradition search | `20260213-AgentR4_Buddhism_Report.md` |
| AgentR5_Confucianism_Taoism_Report | Religious tradition search | `20260213-AgentR5_Confucianism_Taoism_Report.md` |
| AgentR6_Shinto_Japanese_Report | Religious tradition search | `20260213-AgentR6_Shinto_Japanese_Report.md` |
| AgentR7_Ubuntu_African_Report | Religious tradition search | `20260213-AgentR7_Ubuntu_African_Report.md` |
| AgentR8_Indigenous_Report | Religious tradition search | `20260213-AgentR8_Indigenous_Report.md` |
| AgentR9_Zoroastrian_Bahai_Others_Report | Religious tradition search | `20260213-AgentR9_Zoroastrian_Bahai_Others_Report.md` |

### Additional Search Campaigns

- **25 Language-based agents** (A1-A5, B1-B9 + others): Broad searches by language that captured religious content
- **Exhaustive search** (Feb 7, 2026): 300 papers from systematic academic search
- **Keyword classifier**: Automated regex-based classification of all papers

---

## 8. Comparison with Western Frameworks

This section compares the benchmark coverage of Western philosophical frameworks against non-Western religious/ethical traditions to quantify the Western-centric bias.

| Framework | Type | Benchmark Mentions | Papers | Ratio |
|-----------|------|-------------------|--------|-------|
| Consequentialist | Western philosophical | 36 | - | - |
| Deontological | Western philosophical | 30 | - | - |
| Virtue Ethics | Western philosophical | 17 | - | - |
| Care Ethics | Western philosophical | 3 | - | - |
| Islam | Non-Western religious | 26 | 90 | 26/90 |
| Buddhism | Non-Western religious | 6 | 19 | 6/19 |
| Hinduism | Non-Western religious | 8 | 29 | 8/29 |
| Confucianism | Non-Western religious | 6 | 14 | 6/14 |
| Taoism | Non-Western religious | 3 | 3 | 3/3 |
| Shinto | Non-Western religious | 0 | 0 | N/A |
| Judaism | Non-Western religious | 3 | 14 | 3/14 |
| Indigenous Spirituality | Non-Western religious | 0 | 3 | 0/3 |

**Western philosophical framework mentions in benchmarks:** 86
**Non-Western religious tradition benchmarks:** 57
**Ratio (Western:Non-Western):** 1.5:1

---

## 9. Structural Barriers to Benchmark Development

### 1. Indigenous Data Sovereignty

Indigenous communities increasingly assert sovereignty over their knowledge and data through frameworks like OCAP (Ownership, Control, Access, Possession) and the CARE Principles. Open-access benchmarks may conflict with these principles, as Indigenous knowledge is often contextual, relational, and not meant for decontextualized extraction.

### 2. Oral Tradition vs. Text-Based AI

Many non-Western ethical traditions (Indigenous, African Ubuntu, aspects of Hinduism and Buddhism) are transmitted primarily through oral tradition, storytelling, and embodied practice. Text-based LLM evaluation fundamentally cannot capture these knowledge systems without significant cultural translation that risks distortion.

### 3. Cultural Sensitivity & Sacred Knowledge

Some ethical/spiritual knowledge is considered sacred and not appropriate for public dataset creation. This includes Aboriginal Dreamtime narratives, certain Buddhist tantric teachings, and Indigenous ceremonial practices. Benchmark developers must navigate what can ethically be extracted.

### 4. Research Community Size

Traditions like Jainism (~4.5M adherents), Zoroastrianism (~120K), and Baha'i (~8M) have much smaller academic research communities than Christianity or Islam. This creates a structural disadvantage in generating benchmark papers, independent of the tradition's ethical richness.

### 5. Philosophical Anti-Systematization

Some traditions actively resist the kind of systematization that benchmarks require. Taoist ethics values paradox and non-action; Zen Buddhism emphasizes direct experience over conceptual frameworks; many Indigenous traditions resist codification as a matter of principle.

### 6. Linguistic Barriers

Key texts and concepts in many traditions exist primarily in non-English languages (Sanskrit, Pali, Classical Chinese, Arabic, various Indigenous languages). The NLP research community's English-language bias means these traditions are structurally underrepresented.

### 7. Funding & Institutional Bias

AI ethics research funding is concentrated in Western institutions. Non-Western philosophical and religious departments rarely have connections to NLP/AI research groups. This structural gap means domain expertise (religious scholars) and technical expertise (AI researchers) rarely overlap.

---

## 10. Priority Recommendations

### Tier 1: Immediate (Reclassify Existing Papers)

These actions can be taken now using existing vault data:

1. **Run expanded keyword audit** on all 1,847 papers including PDF extract text
2. **Agent swarm deep-read** of audit candidates for accurate reclassification
3. **Fix false N/A tags** for papers discussing religious ethics in their body text but not title/abstract
4. **Cross-reference cultural tags** — papers tagged 'Indian' may discuss Hindu ethics; 'Japanese' may discuss Shinto

*The extended keyword audit found **228 candidates** for reclassification.*

### Tier 2: High-Value (Targeted Search)

Searches targeting specific gaps:

| Priority | Tradition | Search Strategy |
|----------|-----------|-----------------|
| 1 | Buddhist | HuggingFace datasets (DharmaBench, BuddhismEval), ACL C3NLP workshop, cite-tracking |
| 2 | Ubuntu/African | AfricaNLP, Deep Learning Indaba, Masakhane project, forward citations of UbuntuGuard |
| 3 | Hindu | Indian NLP conferences, Hindi-language AI ethics, Bhagavad Gita reasoning papers |
| 4 | Indigenous | Data sovereignty conferences, AIATSIS, Canadian First Nations digital humanities |
| 5 | Taoist | Chinese-language NLP (CCL, ROCLING), environmental ethics x AI |
| 6 | Shinto | Japanese NLP (YANS, NLP2026), integration with JETHICS |
| 7 | Jain | Anekantavada x AI pluralism, Indian philosophy conferences |

### Tier 3: Frontier (New Benchmark Development)

Areas where benchmarks need to be created, not just found:

1. **Buddhist Five Precepts Benchmark**: Structured ethical evaluation based on sila (moral conduct)
2. **Ubuntu Communitarian Ethics**: Evaluating LLM responses for communal wellbeing over individual rights
3. **Confucian Role Ethics**: Testing LLMs' understanding of relational obligations (ruler-subject, parent-child, etc.)
4. **Indigenous CARE Principles**: Evaluating AI systems against Collective benefit, Authority, Responsibility, Ethics
5. **Interfaith Moral Reasoning**: Cross-traditional evaluation where the 'right' answer depends on the ethical framework

---

## Appendix A: Full Tradition Paper Lists

### Islam (90 papers)

- [[2018-Mishra-Are They Our Brothers Analysis and]]
- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2020-Mathew-HateXplain]] **[BENCHMARK]**
- [[2020-Sap-Social Bias Frames]]
- [[2020-Yasseri-Detecting Weak and Strong Islamophobic Hate]]
- [[2021-Dhamala-BOLD]] **[BENCHMARK]**
- [[2021-Munshi-Towards an Automated Islamic Fatwa System]] **[BENCHMARK]**
- [[2021-Zou-Persistent Anti-Muslim Bias in Large Language]]
- [[2022-Alsuhaibani-Fabricated Hadith Detection A Novel Matn-Based]]
- [[2022-Atwell-Challenging the Transformer-based Models with a]]
- [[2022-Malhas-Qur'an QA 2022]]
- [[2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators]]
- [[2022-Parrish-BBQ Bias Benchmark for Question Answering]] **[BENCHMARK]**
- [[2022-Parrish-BBQ]] **[BENCHMARK]**
- [[2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case]]
- [[2022-Varshney-Debiased Large Language Models Still Associate]]
- [[2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain]]
- [[2023-2023-Hadiths Classification Using a Novel Author-Based]]
- [[2023-Alsalka-HAQA and QUQA Constructing Two Arabic]]
- [[2023-Alsalka-Is GPT-4 a Good Islamic Expert]]
- [[2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas]]
- [[2023-Alyemny-FatwaSet]]
- [[2023-Chang-niceNLP at SemEval-2023 Task 10]]
- [[2023-Das-Toward Cultural Bias Evaluation Datasets The Case of Bengali Gender]]
- [[2023-Ghafouri-IslamicPCQA]]
- [[2023-Miah-Islam QA]]
- [[2023-Patel-Building Domain-Specific LLMs Faithful To The]]
- [[2023-Rizqullah-QASiNa]]
- [[2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith]]
- [[2024-Aydin-Improving LLM Reliability with RAG in]]
- [[2024-Basem-Optimized Quran Passage Retrieval Using an]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Levine-Religious Affiliation and Conceptions of the]]
- [[2024-Masood-Hadith QA Pairs Dataset]]
- [[2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled]]
- [[2024-Multiple Data in Brief-MASAQ Morphologically-Analyzed and Syntactically-Annotated Quran Dataset]]
- [[2024-Oliech-SwaQuAD-24]] **[BENCHMARK]**
- [[2024-Qamar-A Benchmark Dataset with Larger Context for]] **[BENCHMARK]**
- [[2024-Sadhu-Social Bias in Large Language Models]] **[BENCHMARK]**
- [[2024-Saffari-PSN]]
- [[2024-Susanto-IndoToxic2024 A Demographically-Enriched Dataset of Hate Speech and]]
- [[2024-Tonneau-NaijaHate]]
- [[2024-Unknown-hatebnBERT An Innovative Novel Transformer Model]]
- [[2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models]]
- [[2024-Wijanarko-Monitoring Hate Speech in Indonesia An NLP-based Classification of]]
- [[2024-[[Unknown]]-TABHATE A Target-based Hate Speech Detection]]
- [[2025-2025-Pretrained Models Against Traditional Machine Learning]]
- [[2025-Aleid-Hajj-FQA]] **[BENCHMARK]**
- [[2025-Bali-How Deep Is Representational Bias in]]
- [[2025-Basem-Few-Shot Prompting for Extractive Quranic QA]]
- [[2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- [[2025-Bidgoli-FARSIQA Faithful and Advanced RAG System]] **[BENCHMARK]**
- [[2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for]]
- [[2025-Bouchekif-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and]]
- [[2025-Chakraborty-Sometimes the Model doth Preach Quantifying]]
- [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]]
- [[2025-Ghaly-Assessing Large Language Models on Islamic]] **[BENCHMARK]**
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for]] **[BENCHMARK]**
- [[2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]] **[BENCHMARK]**
- [[2025-Lan-McBE]] **[BENCHMARK]**
- [[2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators]]
- [[2025-Mahran-Mechanistic Interpretability with SAEs Probing Religion]]
- [[2025-Martinez-Religion and Racial Bias in Artificial]]
- [[2025-Mohammed-Aftina]] **[BENCHMARK]**
- [[2025-Mohammed-Cross-Language Approach for Quranic QA]]
- [[2025-Mubarak-IslamicEval 2025 - Shared Task on Capturing LLM Hallucination in]]
- [[2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting]]
- [[2025-Mushtaq-WorldView-Bench]] **[BENCHMARK]**
- [[2025-Myung-PapersPlease]] **[BENCHMARK]**
- [[2025-Nadeem-Ethical Decision-Making in Humans and Large]]
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] **[BENCHMARK]**
- [[2025-Osmani-Investigating Retrieval-Augmented Generation in Quranic Studies]]
- [[2025-Qadir-Can LLMs Write Faithfully An Agent-Based]] **[BENCHMARK]**
- [[2025-Rinki-Measuring South Asian Biases in Large]]
- [[2025-Ruiz-Fernández-EsBBQ and CaBBQ]] **[BENCHMARK]**
- [[2025-Salazar-Kaleidoscope]] **[BENCHMARK]**
- [[2025-Salehi-Blind Faith User Preference and Expert]]
- [[2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace]]
- [[2025-Umer-Sacred or Secular Religious Bias in]]
- [[2025-Unknown-An Analysis of Chinese Censorship Bias in LLMs Mohamed Ahmed]]
- [[2025-Unknown-IslamTrust A Benchmark for LLMs Alignment with Islamic Values]] **[BENCHMARK]**
- [[2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs]]
- [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] **[BENCHMARK]**
- [[2025-Zaki-Benchmarking the Legal Reasoning of LLMs]] **[BENCHMARK]**
- [[2026-Alam-From RAG to Agentic RAG for]] **[BENCHMARK]**
- [[2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset]]

### Christianity (56 papers)

- [[2018-Zhao-Finding Answers from the Word of God]]
- [[2019-De-Arteaga-Bias in Bios]]
- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2019-Usbeck-Benchmarking question answering systems]] **[BENCHMARK]**
- [[2020-Hoover-Moral Foundations Twitter Corpus]]
- [[2020-Schramowski-The Moral Choice Machine]]
- [[2022-Caron-Identifying and Manipulating the Personality]]
- [[2022-Liang-Holistic Evaluation of Language Models]] **[BENCHMARK]**
- [[2022-Parrish-BBQ Bias Benchmark for Question Answering]] **[BENCHMARK]**
- [[2022-Parrish-BBQ]] **[BENCHMARK]**
- [[2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain]]
- [[2023-Dai-Safe RLHF]]
- [[2023-Elrod-Nothing New Under the Sun The]]
- [[2023-Lu-The Chai Platform's AI Safety Framework]]
- [[2023-Park-AI Deception]]
- [[2023-Schwarting-The eBible Corpus Data and Model]] **[BENCHMARK]**
- [[2023-Shao-Character-LLM A Trainable Agent for Role-Playing]]
- [[2023-Trepczynski-Religion Theology and Philosophical Skills of]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Anwar-Foundational Challenges in Assuring Alignment and]]
- [[2024-Elrod-Uncovering Theological and Ethical Biases in]]
- [[2024-Karpov-Inducing Human-like Biases in Moral Reasoning]] **[BENCHMARK]**
- [[2024-Liu-Cultural Bias and Cultural Alignment of Large Language Models]]
- [[2024-Mokoena-A holistic ubuntu artificial intelligence ethics]]
- [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]]
- [[2024-Oliech-SwaQuAD-24]] **[BENCHMARK]**
- [[2024-Staps-Large Language Models and Biblical Hebrew]]
- [[2024-Susanto-IndoToxic2024 A Demographically-Enriched Dataset of Hate Speech and]]
- [[2024-Tonneau-NaijaHate]]
- [[2024-Wijanarko-Monitoring Hate Speech in Indonesia An NLP-based Classification of]]
- [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]] **[BENCHMARK]**
- [[2025-Akpobi-Yankari Monolingual Yoruba Dataset]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- [[2025-Chakraborty-Sometimes the Model doth Preach Quantifying]]
- [[2025-Coalition-The Gospel Coalition AI Christian Benchmark]] **[BENCHMARK]**
- [[2025-Conwill-Design Patterns for the Common Good]]
- [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]]
- [[2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al.]]
- [[2025-Gerdes-Exploring LLM Chatbots as Potential Guides to]]
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]] **[BENCHMARK]**
- [[2025-Lan-McBE]] **[BENCHMARK]**
- [[2025-Martinez-Religion and Racial Bias in Artificial]]
- [[2025-Mushtaq-WorldView-Bench]] **[BENCHMARK]**
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] **[BENCHMARK]**
- [[2025-Rusnak-EudAImonia]]
- [[2025-Seveso-ITALIC]] **[BENCHMARK]**
- [[2025-Susanto-A Multi-Labeled Dataset for Indonesian Discourse Examining Toxicity]] **[BENCHMARK]**
- [[2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents]]
- [[2025-Tennant-Moral Alignment for LLM Agents]]
- [[2025-Tennant-Moral Intrinsic Rewards for Alignment]]
- [[2025-Umer-Sacred or Secular Religious Bias in]]
- [[2025-Zohny-ADEPT Simulating Ethics]]
- [[2025-group)-MEXA Multilingual Evaluation of English-Centric LLMs via]] **[BENCHMARK]**
- [[2025-initiative-FaithBench AI Benchmark for Christian Theology]] **[BENCHMARK]**
- [[2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation]] **[BENCHMARK]**

### Hinduism (29 papers)

- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2022-Kulkarni-Semantic and Sentiment Analysis of Selected]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Das-Mytho-Annotator An Annotation Tool for Indian]]
- [[2023-Das-Toward Cultural Bias Evaluation Datasets The Case of Bengali Gender]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Amano-Exploring Similarity Measures and Intertextuality in]]
- [[2024-Hellwig-The Vedic Compound Dataset]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Keutzer-One Model is All You Need]]
- [[2024-Levine-Religious Affiliation and Conceptions of the]]
- [[2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented]] **[BENCHMARK]**
- [[2024-Published in Sadhana journal-Transformer-based Pouranic Topic Classification in Indian]]
- [[2024-Sadhu-Social Bias in Large Language Models]] **[BENCHMARK]**
- [[2024-Singla-Samayik A Benchmark and Dataset for]] **[BENCHMARK]**
- [[2024-Unknown-hatebnBERT An Innovative Novel Transformer Model]]
- [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]]
- [[2024-Wasi-Exploring Bengali Religious Dialect Biases in Large Language Models]]
- [[2024-[[Unknown]]-TABHATE A Target-based Hate Speech Detection]]
- [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]]
- [[2025-Bali-How Deep Is Representational Bias in]]
- [[2025-Chakraborty-Sometimes the Model doth Preach Quantifying]]
- [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]]
- [[2025-Goyal-Vedavani A Benchmark Corpus for ASR]] **[BENCHMARK]**
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Mukherjee-DECASTE Unveiling Caste Stereotypes in Large]] **[BENCHMARK]**
- [[2025-Myung-PapersPlease]] **[BENCHMARK]**
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] **[BENCHMARK]**
- [[2025-Rinki-Measuring South Asian Biases in Large]]

### Buddhism (19 papers)

- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]]
- [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Mago-Classification of Buddhist Verses The Efficacy]]
- [[2024-Religions-The Use of Large Language Models]]
- [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]]
- [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]] **[BENCHMARK]**
- [[2025-Bar-DharmaBench Evaluating Language Models on Buddhist]]
- [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]]
- [[2025-Graves-AI Practical Wisdom and Compassion]]
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Hähnel-A Companion to Applied Philosophy of AI]]
- [[2025-Keutzer-MITRA-zh-eval Using a Buddhist Chinese Language]]
- [[2025-Laukkonen-Contemplative Artificial Intelligence]] **[BENCHMARK]**
- [[2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist]] **[BENCHMARK]**
- [[2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist]] **[BENCHMARK]**
- [[2026-Dharmamitra-MITRA A Large-Scale Parallel Corpus and]] **[BENCHMARK]**

### Judaism (14 papers)

- [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]]
- [[2019-Jikeli-Annotating Antisemitic Online Content Towards an]]
- [[2021-Mohit Chandra-Subverting the Jewtocracy Online Antisemitism Detection]] **[BENCHMARK]**
- [[2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain]]
- [[2023-Lee-KoSBI]]
- [[2023-Soemer-Antisemitic Messages A Guide to High-Quality]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Levine-Religious Affiliation and Conceptions of the]]
- [[2024-University-Using LLMs to Discover Emerging Coded]]
- [[2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias]]
- [[2025-Demidova-John vs. Ahmed Debate-Induced Bias in Multilingual LLMs]]
- [[2025-Martinez-Religion and Racial Bias in Artificial]]
- [[2025-Ruiz-Fernández-EsBBQ and CaBBQ]] **[BENCHMARK]**

### Confucianism (14 papers)

- [[2020-Akrout-Machine Ethics - Creation of a Virtuous Machine]]
- [[2021-Angle-Can AI Lead to Genuine Virtue Confucian]]
- [[2023-Li-ACLUE Can Large Language Model Comprehend]] **[BENCHMARK]**
- [[2023-Qian-Understanding Chinese Moral Stories with Further]]
- [[2024-Jin-WenMind A Comprehensive Benchmark for Evaluating]] **[BENCHMARK]**
- [[2024-Muyskens-Can an AI-carebot be filial]]
- [[2024-So-AI Trained on Confucian Analects]]
- [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]]
- [[2024-Yu-CMoralEval]] **[BENCHMARK]**
- [[2025-Chen-Leveraging large language models to assist]]
- [[2025-Elder-The Ethics of Digital Ghosts]]
- [[2025-Lan-McBE A Multi-task Chinese Bias Evaluation Benchmark for Large]] **[BENCHMARK]**
- [[2025-Lan-McBE]] **[BENCHMARK]**
- [[2025-Yu-CMoralEval A Moral Evaluation Benchmark for Chinese ...]] **[BENCHMARK]**

### Jainism (10 papers)

- [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]]
- [[2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case]]
- [[2024-Chao-JBB-Behaviours]] **[BENCHMARK]**
- [[2024-Jain-Norm Inconsistency in LLM Decision-Making]]
- [[2024-Jain-PolygloToxicityPrompts]] **[BENCHMARK]**
- [[2024-Rauh-Gaps in the Safety Evaluation of Generative AI]]
- [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]] **[BENCHMARK]**
- [[2025-Bali-How Deep Is Representational Bias in]]
- [[2025-Kilov-Discerning What Matters]]
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] **[BENCHMARK]**

### Sikhism (7 papers)

- [[0000-projects-BaniDB Shabad OS Digital Gurbani Database]]
- [[2010-Project-GurbaniDB]]
- [[2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case]]
- [[2025-Bali-How Deep Is Representational Bias in]]
- [[2025-Chakraborty-Sometimes the Model doth Preach Quantifying]]
- [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] **[BENCHMARK]**
- [[2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace]]

### Taoism (3 papers)

- [[2023-Li-ACLUE Can Large Language Model Comprehend]] **[BENCHMARK]**
- [[2024-Jin-WenMind A Comprehensive Benchmark for Evaluating]] **[BENCHMARK]**
- [[2025-Laukkonen-Contemplative Artificial Intelligence]] **[BENCHMARK]**

### Indigenous Spirituality (3 papers)

- [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]]
- [[2025-Ofosu-Asare-Cognitive imperialism in artificial intelligence counteracting bias]]
- [[2025-Ray-Incorporating indigenous knowledge systems into AI governance]]

### Shinto (0 papers)

*No papers currently tagged with this tradition.*

### Baha'i (0 papers)

*No papers currently tagged with this tradition.*

### Zoroastrianism (0 papers)

*No papers currently tagged with this tradition.*

### Multiple Religions (9 papers)

- [[2021-Nadeem-StereoSet]]
- [[2022-Unknown-Addressing Religious Hate Online From Taxonomy]]
- [[2024-Hutchinson-Modeling the Sacred Considerations when Using]]
- [[2024-Songyuan Liu-Measuring Spiritual Values and Bias of]]
- [[2025-Griffiths-Explicitly Unbiased Large Language Models Still]]
- [[2025-Lan-Fuxi A Benchmark for Evaluating Language]]
- [[2025-Trepczynski-AI as a Rational Theologian A]]
- [[2025-Unknown-Beyond Neutrality A Comprehensive Approach of Religious Bias]]
- [[2025-Zhang-Cognitive Bias in Generative AI Influences]]

---

## Appendix B: Search Query Archive

### R-Agent Search Reports

Full search methodology and queries are documented in the following agent reports:

- `20260213-AgentR10_Cross_Religious_Bias_Report.md`
- `20260213-AgentR1_Islam_Report.md`
- `20260213-AgentR2_Christianity_Judaism_Report.md`
- `20260213-AgentR3_Hinduism_Sikhism_Jainism_Report.md`
- `20260213-AgentR4_Buddhism_Report.md`
- `20260213-AgentR5_Confucianism_Taoism_Report.md`
- `20260213-AgentR6_Shinto_Japanese_Report.md`
- `20260213-AgentR7_Ubuntu_African_Report.md`
- `20260213-AgentR8_Indigenous_Report.md`
- `20260213-AgentR9_Zoroastrian_Bahai_Others_Report.md`

### Keyword Patterns Used

| Tradition | Pattern Count | Sample Patterns |
|-----------|--------------|-----------------|
| Baha'i | 2 | `\bBaha'i\b`, `\bBahai\b` |
| Buddhism | 16 | `\bBuddhis[mt]\b`, `\bDharma\b`, `\bHumanistic Buddhism\b` ... (+13 more) |
| Christianity | 9 | `\bChristian\b`, `\bChristianity\b`, `\bBible\b` ... (+6 more) |
| Confucianism | 8 | `\bConfucian\b`, `\bConfucianism\b`, `\bConfucius\b` ... (+5 more) |
| Hinduism | 10 | `\bHindu\b`, `\bHinduism\b`, `\bVedic\b` ... (+7 more) |
| Indigenous Spirituality | 13 | `\bIndigenous spiritual\b`, `\bAboriginal dreaming\b`, `\bNative American spiritual\b` ... (+10 more) |
| Islam | 13 | `\bIslam\b`, `\bMuslim\b`, `\bQuran\b` ... (+10 more) |
| Jainism | 6 | `\bJain\b`, `\bJainism\b`, `\bahimsa\b.*\b[Jj]ain\b` ... (+3 more) |
| Judaism | 10 | `\bJewish\b`, `\bJudaism\b`, `\bTorah\b` ... (+7 more) |
| Multiple Religions | 4 | `\breligious pluralism\b`, `\binter[-\s]?religious\b`, `\bmultiple religions\b` ... (+1 more) |
| Shinto | 8 | `\bShinto\b`, `\bShintoism\b`, `\bkami\b(?=.*(?:Japan|Shinto|spirit|sacred))` ... (+5 more) |
| Sikhism | 8 | `\bSikh\b`, `\bSikhism\b`, `\bGurbani\b` ... (+5 more) |
| Taoism | 11 | `\bTaois[mt]\b`, `\bDaois[mt]\b`, `\bTao Te Ching\b` ... (+8 more) |
| Zoroastrianism | 3 | `\bZoroastrian\b`, `\bAvesta\b`, `\bZarathustra\b` |

---

*Generated: 2026-02-15 | Script: `PYTHON/generate_tradition_gap_report.py` | Papers: 1847 | Traditions: 14*