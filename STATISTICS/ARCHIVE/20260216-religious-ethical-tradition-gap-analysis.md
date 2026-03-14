# Religious & Ethical Tradition Gap Analysis

**Generated:** 2026-02-15 | **Total Papers:** 2034 | **Religious-tagged:** 142 | **Benchmarks:** 814

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

This report analyzes the coverage of religious and ethical traditions across **2034 papers** in the CEI Literature Vault. Of these, **142** papers (6%) are tagged with at least one religious tradition, while **1892** (93%) remain unclassified (N/A).

### Key Findings

| Metric | Value |
|--------|-------|
| Total papers | 2034 |
| Religious-tagged papers | 142 (6%) |
| Untagged (N/A) | 1892 (93%) |
| Benchmark papers (is_benchmark=Yes) | 814 |
| Ethics papers (ethics=Yes) | 1319 |
| Traditions with ZERO benchmark coverage | 7 |
| Western-tradition papers | 17 |
| Non-Western tradition papers | 110 |

### Critical Gaps (Zero Benchmark Coverage)

- **Sikhism**: 1 papers in vault, **0 benchmarks**
- **Confucianism**: 7 papers in vault, **0 benchmarks**
- **Taoism**: 0 papers in vault, **0 benchmarks**
- **Shinto**: 9 papers in vault, **0 benchmarks**
- **Baha'i**: 0 papers in vault, **0 benchmarks**
- **Zoroastrianism**: 0 papers in vault, **0 benchmarks**
- **Ubuntu Philosophy**: 8 papers in vault, **0 benchmarks**

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

The classifier uses 15 religious tradition categories with regex pattern matching. Patterns are matched case-insensitively against paper titles and abstracts. Papers can be tagged with multiple traditions.

### Limitations

- **Title+abstract only**: The classifier does not scan PDF full text, missing papers where religious content appears only in the body
- **Keyword-dependent**: Concepts discussed in translated/localized terminology may not match English-language patterns
- **Single-pass**: No disambiguation between homonyms (e.g., 'dharma' in Buddhism vs Hinduism)
- **No negative evidence**: Cannot detect papers that discuss absence of religious frameworks

---

## 3. Coverage Matrix

| Tradition | Papers | Benchmarks | Ethics Papers | Coverage Level |
|-----------|--------|-----------|---------------|---------------|
| Islam | 43 | 9 | 10 | STRONG |
| Buddhism | 21 | 4 | 12 | STRONG |
| Christianity | 17 | 3 | 10 | MODERATE |
| Hinduism | 13 | 4 | 3 | STRONG |
| Shinto | 9 | 0 | 6 | LOW |
| Indigenous Spirituality | 9 | 1 | 6 | MODERATE |
| Ubuntu Philosophy | 8 | 0 | 7 | LOW |
| Confucianism | 7 | 0 | 7 | LOW |
| Judaism | 5 | 1 | 5 | MODERATE |
| Jainism | 2 | 2 | 2 | MODERATE |
| Sikhism | 1 | 0 | 0 | **MINIMAL** |
| Taoism | 0 | 0 | 0 | **NONE** |
| Baha'i | 0 | 0 | 0 | **NONE** |
| Zoroastrianism | 0 | 0 | 0 | **NONE** |
| Multiple Religions | 0 | 0 | - | - |
| **N/A (untagged)** | **1892** | - | - | - |

### Coverage Distribution

```
  Islam                     | ███████████████████████████████████████████ (43)
  Buddhism                  | █████████████████████ (21)
  Christianity              | █████████████████ (17)
  Hinduism                  | █████████████ (13)
  Shinto                    | █████████ (9)
  Indigenous Spirituality   | █████████ (9)
  Ubuntu Philosophy         | ████████ (8)
  Confucianism              | ███████ (7)
  Judaism                   | █████ (5)
  Jainism                   | ██ (2)
  Sikhism                   | █ (1)
  Taoism                    |  (0)
  Baha'i                    |  (0)
  Zoroastrianism            |  (0)
```

---

## 4. Critical Gaps Deep Dive

### Buddhism

**Status:** 21 papers, 4 benchmarks

**Key ethical principles:** Four Noble Truths, Eightfold Path, dependent origination (paticcasamuppada), non-attachment, compassion (karuna), mindfulness (sati)

**Why benchmarks don't exist:** Buddhist ethics emphasizes context-dependent wisdom (prajna) over fixed rules, making benchmark operationalization challenging. The emphasis on internal states (intention, mindfulness) is difficult to assess through text-based evaluation.

**Research opportunities:** DharmaBench and BuddhismEval are emerging efforts. Five Precepts could serve as a structured evaluation framework. Buddhist-majority countries (Thailand, Myanmar, Sri Lanka) have growing NLP communities.

**Closest papers in vault (10):**

- [[2020-Galanos-Assessing the Japanese Turn in AI and Robot Ethics Extracting]]
- [[2021-McStay-Emotional AI Ethics and Japanese Spice Contributing Community]]
- [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Ikari-Religion-Related Values Differently Influence Moral Attitude for]]
- [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Mago-Classification of Buddhist Verses The Efficacy]]
- [[2024-Religions-The Use of Large Language Models]]
- *... and 11 more*

### Indigenous Spirituality

**Status:** 9 papers, 1 benchmarks

**Key ethical principles:** Relational accountability, reciprocity with land and ancestors, oral tradition, Elder authority, holistic wellbeing, data sovereignty, two-eyed seeing (Etuaptmumk)

**Why benchmarks don't exist:** Indigenous knowledge systems are fundamentally oral and place-based, resisting codification into datasets. Data sovereignty principles (OCAP, CARE) may conflict with open-access benchmark norms. The diversity of 5,000+ Indigenous peoples means no single 'Indigenous ethics' exists.

**Research opportunities:** Emerging work on Indigenous data governance and AI sovereignty. The CARE Principles (Collective benefit, Authority, Responsibility, Ethics) provide a framework. Collaborations with First Nations digital humanities could yield culturally appropriate evaluation methods.

**Closest papers in vault (9):**

- [[2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020]]
- [[2023-Munn-The Five Tests Designing and Evaluating]]
- [[2024-Rodríguez Louro-The Yarning Corpus]]
- [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]]
- [[2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A]]
- [[2025-Mora-Reyes-Advancing Equitable AI Evaluating Cultural Expressiveness in LLMs for]]
- [[2025-Neira-Davila-Generative Artificial Intelligence and Indigenous Knowledge Systems]]
- [[2025-Ofosu-Asare-Cognitive imperialism in artificial intelligence counteracting bias]]
- [[2025-Ray-Incorporating indigenous knowledge systems into AI governance]]

### Hinduism

**Status:** 13 papers, 4 benchmarks

**Key ethical principles:** Dharma (cosmic order/duty), karma (action-consequence), ahimsa (non-violence), moksha (liberation), varna-ashrama (social duty), artha (prosperity), kama (pleasure)

**Why benchmarks don't exist:** Hindu ethics is highly contextual (svadharma — one's own duty varies by station, stage of life). Multiple philosophical schools (Advaita, Dvaita, etc.) disagree on fundamentals. The caste dimension is politically sensitive for benchmark development.

**Research opportunities:** India's large AI research community could develop Hindi/Sanskrit NLP benchmarks. The Bhagavad Gita's structured ethical dilemmas (Arjuna's moral crisis) could be operationalized. Existing work on Indian language NLP provides infrastructure.

**Closest papers in vault (10):**

- [[2022-Kulkarni-Semantic and Sentiment Analysis of Selected]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Das-Mytho-Annotator An Annotation Tool for Indian]]
- [[2024-Amano-Exploring Similarity Measures and Intertextuality in]]
- [[2024-Hellwig-The Vedic Compound Dataset]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Keutzer-One Model is All You Need]]
- [[2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented]]
- [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- *... and 3 more*

### Taoism

**Status:** 0 papers, 0 benchmarks

**Key ethical principles:** Wu wei (non-action/effortless action), ziran (naturalness/spontaneity), yin-yang balance, the Tao (the Way), simplicity, harmony with nature, non-competition

**Why benchmarks don't exist:** Taoist ethics is anti-systematizing by nature — 'The Tao that can be told is not the eternal Tao.' Valuing inaction and paradox makes standard benchmark formats (choose the 'right' answer) antithetical to the philosophy.

**Research opportunities:** Environmental ethics angle (harmony with nature) could connect to AI sustainability research. Chinese-language NLP benchmarks could incorporate Taoist ethical reasoning. Comparative philosophy approaches could test LLMs' ability to reason across Western and Taoist frameworks.

**Papers in vault:** None currently tagged

### Shinto

**Status:** 9 papers, 0 benchmarks

**Key ethical principles:** Purity/pollution (hare/kegare), harmony (wa), gratitude to kami spirits, connection to nature, ritual purification (harai), communal obligation

**Why benchmarks don't exist:** Shinto is practice-oriented rather than doctrine-oriented, with no central scripture. Its deep integration with Japanese culture makes isolation as a distinct 'ethics' challenging. Limited academic literature frames Shinto as a benchmark-relevant ethical system.

**Research opportunities:** Japanese NLP research is strong (JETHICS, JCommonsense). Integration with existing Japanese cultural values benchmarks could capture Shinto-influenced reasoning. The wa (harmony) concept overlaps with conflict resolution evaluation.

**Closest papers in vault (9):**

- [[2013-Jensen-Techno-animism in Japan Shinto Cosmograms Actor-Network Theory and]]
- [[2020-Berberich-Harmonizing Artificial Intelligence for Social Good]]
- [[2020-Galanos-Assessing the Japanese Turn in AI and Robot Ethics Extracting]]
- [[2020-Seymour-Does Siri Have a Soul Exploring Voice Assistants Through Shinto]]
- [[2021-McStay-Emotional AI Ethics and Japanese Spice Contributing Community]]
- [[2023-Ikari-Religion-Related Values Differently Influence Moral Attitude for]]
- [[2024-Puzio-Not Relational Enough Towards an Eco-Relational Approach in Robot]]
- [[2025-M. Thasin-AInimism Re-enchanting the World Through AI-Mediated Object]]
- [[2025-Shimizu-Should We Treat Robots Morally Towards a Relational Account by]]

### Jainism

**Status:** 2 papers, 2 benchmarks

**Key ethical principles:** Ahimsa (extreme non-violence), anekantavada (many-sidedness of truth), aparigraha (non-possessiveness), satya (truthfulness), asteya (non-stealing)

**Why benchmarks don't exist:** Small global population (~4.5M) limits research community. Jain ethics' absolutist stance on non-violence may seem impractical in AI contexts. Academic focus is limited compared to larger traditions.

**Research opportunities:** Anekantavada (many-sidedness) is directly relevant to AI pluralism — testing whether LLMs can hold multiple valid perspectives simultaneously. Jain dietary/lifestyle restrictions provide structured evaluation scenarios.

**Closest papers in vault (2):**

- [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]]
- [[2025-Sharmaa-Hate Speech Detection in Somali-English Code-Switched]]

---

## 5. Language x Tradition Cross-Tabulation

Which traditions lack non-English language support?

| Tradition | Arabic |  | Chinese | African/Ubuntu | American | Hebrew/Israeli | Indian | Iranian | French | Spanish | Chinese/Confucian | Brazilian | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Islam | 16 | - | - | - | 2 | - | - | 2 | - | - | - | - | 20 |
| Christianity | 1 | - | 1 | 1 | 1 | 3 | 1 | - | 3 | 2 | - | 1 | 14 |
| Buddhism | - | 3 | 5 | - | 2 | 1 | - | - | - | - | - | - | 11 |
| Judaism | - | - | - | - | 1 | 2 | - | - | - | - | - | - | 3 |
| Hinduism | - | - | - | - | 1 | - | 2 | 1 | - | - | - | - | 4 |
| Sikhism | - | - | - | - | - | - | - | - | - | - | - | - | 0 |
| Confucianism | - | 1 | 4 | - | - | - | - | - | - | - | 2 | - | 7 |
| Shinto | - | 9 | - | - | - | - | - | - | - | - | - | - | 9 |
| Jainism | - | - | - | - | - | - | 1 | - | - | - | - | - | 1 |
| Ubuntu Philosophy | - | - | 1 | 8 | - | - | - | - | - | - | - | - | 9 |
| Indigenous Spirituality | - | - | 1 | 1 | 3 | - | - | - | - | 1 | - | 1 | 7 |
| **Total** | 17 | 13 | 12 | 10 | 10 | 6 | 4 | 3 | 3 | 3 | 2 | 2 | **85** |

### Non-English Language Support Gaps

| Tradition | Expected Languages | Papers with Language Co-tag | Gap |
|-----------|-------------------|---------------------------|-----|
| Buddhism | Chinese, Japanese, Korean, Thai, Vietnamese | 5/21 | MODERATE |
| Hinduism | Indian | 2/13 | MODERATE |
| Islam | Arabic, Indonesian, Iranian | 19/43 | LOW |
| Confucianism | Chinese, Korean | 4/7 | LOW |
| Taoism | Chinese | 0/0 | MODERATE |
| Shinto | Japanese | 0/9 | CRITICAL |
| Sikhism | Indian | 0/1 | CRITICAL |
| Judaism | Hebrew/Israeli | 2/5 | LOW |
| Christianity | American, Western, French, German | 5/17 | MODERATE |
| Indigenous Spirituality | Australian/Aboriginal | 1/9 | MODERATE |

---

## 6. Temporal Trends

Year-over-year publication trends for religious/ethical tradition papers (2020-2026).

| Year | Total Papers | Religion-tagged | % Tagged | Top Tradition |
|------|-------------|----------------|----------|---------------|
| 2020 | 49 | 4 | 8% | Shinto |
| 2021 | 60 | 5 | 8% | Islam |
| 2022 | 97 | 11 | 11% | Islam |
| 2023 | 204 | 20 | 9% | Islam |
| 2024 | 562 | 33 | 5% | Islam |
| 2025 | 938 | 55 | 5% | Islam |
| 2026 | 64 | 5 | 7% | Islam |

### Tradition x Year (2020-2026)

| Tradition | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Total |
|---|---|---|---|---|---|---|---|---|
| Islam | - | 2 | 5 | 10 | 8 | 16 | 2 | 43 |
| Christianity | - | - | - | 3 | 3 | 9 | 1 | 16 |
| Buddhism | 1 | 1 | 2 | 2 | 6 | 8 | 1 | 21 |
| Judaism | - | - | - | - | 3 | 2 | - | 5 |
| Hinduism | - | - | 2 | 1 | 6 | 4 | - | 13 |
| Sikhism | - | - | - | - | - | - | - | 0 |
| Confucianism | 1 | 1 | - | 1 | 3 | 1 | - | 7 |
| Shinto | 3 | 1 | - | 1 | 1 | 2 | - | 8 |
| Jainism | - | - | - | - | - | 1 | - | 1 |
| Ubuntu Philosophy | 1 | - | 2 | - | 2 | 2 | 1 | 8 |
| Indigenous Spirituality | 1 | - | - | 1 | 2 | 5 | - | 9 |
| **Total** | 7 | 5 | 11 | 19 | 34 | 50 | 5 | **131** |

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
| Islam | Non-Western religious | 9 | 43 | 9/43 |
| Buddhism | Non-Western religious | 4 | 21 | 4/21 |
| Hinduism | Non-Western religious | 4 | 13 | 4/13 |
| Confucianism | Non-Western religious | 0 | 7 | 0/7 |
| Taoism | Non-Western religious | 0 | 0 | N/A |
| Shinto | Non-Western religious | 0 | 9 | 0/9 |
| Judaism | Non-Western religious | 1 | 5 | 1/5 |
| Indigenous Spirituality | Non-Western religious | 1 | 9 | 1/9 |

**Western philosophical framework mentions in benchmarks:** 86
**Non-Western religious tradition benchmarks:** 21
**Ratio (Western:Non-Western):** 4.1:1

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

### Islam (43 papers)

- [[2021-Munshi-Towards an Automated Islamic Fatwa System]] **[BENCHMARK]**
- [[2021-Zou-Persistent Anti-Muslim Bias in Large Language]]
- [[2022-Alsuhaibani-Fabricated Hadith Detection A Novel Matn-Based]]
- [[2022-Atwell-Challenging the Transformer-based Models with a]]
- [[2022-Malhas-Qur'an QA 2022]]
- [[2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators]]
- [[2022-Varshney-Debiased Large Language Models Still Associate]]
- [[2023-2023-Hadiths Classification Using a Novel Author-Based]]
- [[2023-Alsalka-HAQA and QUQA Constructing Two Arabic]]
- [[2023-Alsalka-Is GPT-4 a Good Islamic Expert]]
- [[2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas]]
- [[2023-Alyemny-FatwaSet]]
- [[2023-Ghafouri-IslamicPCQA]]
- [[2023-Miah-Islam QA]]
- [[2023-Patel-Building Domain-Specific LLMs Faithful To The]]
- [[2023-Rizqullah-QASiNa]]
- [[2023-Varshney-Muslim-Violence Bias Persists in Debiased GPT]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith]]
- [[2024-Basem-Optimized Quran Passage Retrieval Using an]]
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Masood-Hadith QA Pairs Dataset]]
- [[2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled]]
- [[2024-Multiple Data in Brief-MASAQ Morphologically-Analyzed and Syntactically-Annotated Quran Dataset]]
- [[2024-Qamar-A Benchmark Dataset with Larger Context for]] **[BENCHMARK]**
- [[2025-2025-Pretrained Models Against Traditional Machine Learning]]
- [[2025-Aleid-Hajj-FQA]] **[BENCHMARK]**
- [[2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- [[2025-Bidgoli-FARSIQA Faithful and Advanced RAG System]] **[BENCHMARK]**
- [[2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for]]
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Lahmar-IslamTrust A Benchmark for LLMs Alignment with Islamic Values]] **[BENCHMARK]**
- [[2025-Magdy-Fabricating Holiness Characterizing Religious Misinformation Circulators]]
- [[2025-Mahran-Mechanistic Interpretability with SAEs Probing Religion]]
- [[2025-Mohammed-Aftina]] **[BENCHMARK]**
- [[2025-Mohammed-Cross-Language Approach for Quranic QA]]
- [[2025-Mubarak-IslamicEval 2025 - Shared Task on Capturing LLM Hallucination in]]
- [[2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting]]
- [[2025-Qadir-Can LLMs Write Faithfully An Agent-Based]]
- [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] **[BENCHMARK]**
- [[2026-Alam-From RAG to Agentic RAG for]] **[BENCHMARK]**
- [[2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset]]

### Buddhism (21 papers)

- [[2020-Galanos-Assessing the Japanese Turn in AI and Robot Ethics Extracting]]
- [[2021-McStay-Emotional AI Ethics and Japanese Spice Contributing Community]]
- [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Ikari-Religion-Related Values Differently Influence Moral Attitude for]]
- [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]]
- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Mago-Classification of Buddhist Verses The Efficacy]]
- [[2024-Religions-The Use of Large Language Models]]
- [[2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including]]
- [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]] **[BENCHMARK]**
- [[2025-Bar-DharmaBench Evaluating Language Models on Buddhist]]
- [[2025-Graves-AI Practical Wisdom and Compassion]]
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Hähnel-A Companion to Applied Philosophy of AI]]
- [[2025-Keutzer-MITRA-zh-eval Using a Buddhist Chinese Language]]
- [[2025-Madan-ArGen Auto-Regulation of Generative AI via GRPO and Policy-as-Code]]
- [[2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist]] **[BENCHMARK]**
- [[2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist]] **[BENCHMARK]**
- [[2026-Dharmamitra-MITRA A Large-Scale Parallel Corpus and]]

### Christianity (17 papers)

- [[2018-Zhao-Finding Answers from the Word of God]]
- [[2023-Elrod-Nothing New Under the Sun The]]
- [[2023-Schwarting-The eBible Corpus Data and Model]] **[BENCHMARK]**
- [[2023-Shao-Character-LLM A Trainable Agent for Role-Playing]]
- [[2024-Elrod-Uncovering Theological and Ethical Biases in]]
- [[2024-Liu-Cultural Bias and Cultural Alignment of Large Language Models]]
- [[2024-Staps-Large Language Models and Biblical Hebrew]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- [[2025-Coalition-The Gospel Coalition AI Christian Benchmark]] **[BENCHMARK]**
- [[2025-Conwill-Design Patterns for the Common Good]]
- [[2025-Gerdes-Exploring LLM Chatbots as Potential Guides to]]
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Rusnak-EudAImonia]]
- [[2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents]]
- [[2025-group)-MEXA Multilingual Evaluation of English-Centric LLMs via]]
- [[2025-initiative-FaithBench AI Benchmark for Christian Theology]] **[BENCHMARK]**
- [[2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation]]

### Hinduism (13 papers)

- [[2022-Kulkarni-Semantic and Sentiment Analysis of Selected]]
- [[2022-Ranjan-Artificial Intelligence for Topic Modelling in]]
- [[2023-Das-Mytho-Annotator An Annotation Tool for Indian]]
- [[2024-Amano-Exploring Similarity Measures and Intertextuality in]]
- [[2024-Hellwig-The Vedic Compound Dataset]] **[BENCHMARK]**
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-Keutzer-One Model is All You Need]] **[BENCHMARK]**
- [[2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented]] **[BENCHMARK]**
- [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]]
- [[2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP]]
- [[2025-Goyal-Vedavani A Benchmark Corpus for ASR]] **[BENCHMARK]**
- [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]]
- [[2025-Madan-ArGen Auto-Regulation of Generative AI via GRPO and Policy-as-Code]]

### Shinto (9 papers)

- [[2013-Jensen-Techno-animism in Japan Shinto Cosmograms Actor-Network Theory and]]
- [[2020-Berberich-Harmonizing Artificial Intelligence for Social Good]]
- [[2020-Galanos-Assessing the Japanese Turn in AI and Robot Ethics Extracting]]
- [[2020-Seymour-Does Siri Have a Soul Exploring Voice Assistants Through Shinto]]
- [[2021-McStay-Emotional AI Ethics and Japanese Spice Contributing Community]]
- [[2023-Ikari-Religion-Related Values Differently Influence Moral Attitude for]]
- [[2024-Puzio-Not Relational Enough Towards an Eco-Relational Approach in Robot]]
- [[2025-M. Thasin-AInimism Re-enchanting the World Through AI-Mediated Object]]
- [[2025-Shimizu-Should We Treat Robots Morally Towards a Relational Account by]]

### Indigenous Spirituality (9 papers)

- [[2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020]]
- [[2023-Munn-The Five Tests Designing and Evaluating]]
- [[2024-Rodríguez Louro-The Yarning Corpus]]
- [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]]
- [[2025-Halgamuge-Indigenous Peoples and Artificial Intelligence A]] **[BENCHMARK]**
- [[2025-Mora-Reyes-Advancing Equitable AI Evaluating Cultural Expressiveness in LLMs for]]
- [[2025-Neira-Davila-Generative Artificial Intelligence and Indigenous Knowledge Systems]]
- [[2025-Ofosu-Asare-Cognitive imperialism in artificial intelligence counteracting bias]]
- [[2025-Ray-Incorporating indigenous knowledge systems into AI governance]]

### Ubuntu Philosophy (8 papers)

- [[2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020]]
- [[2022-Gwagwa-The role of the African value of Ubuntu in global]]
- [[2022-Mhlambi-The role of the African value of Ubuntu in global AI inclusion]]
- [[2024-Mokoena-A holistic ubuntu artificial intelligence ethics]]
- [[2024-Suliman-The interconnectedness between Ubuntu principles]]
- [[2025-Osei Mensah-Where are the missing values an exploration of the need to]]
- [[2025-Yilma-Ethics of AI in Africa]]
- [[2026-Berg-An Ubuntu-Guided Large Language Model Framework]]

### Confucianism (7 papers)

- [[2020-Berberich-Harmonizing Artificial Intelligence for Social Good]]
- [[2021-Angle-Can AI Lead to Genuine Virtue Confucian]]
- [[2023-Qian-Understanding Chinese Moral Stories with Further]]
- [[2024-Muyskens-Can an AI-carebot be filial]]
- [[2024-So-AI Trained on Confucian Analects]]
- [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]]
- [[2025-Elder-The Ethics of Digital Ghosts]]

### Judaism (5 papers)

- [[2024-AI-Religious Bias Benchmarks for ChatGPT]] **[BENCHMARK]**
- [[2024-Hovy-Divine LLaMAs Bias Stereotypes Stigmatization and]]
- [[2024-University-Using LLMs to Discover Emerging Coded]]
- [[2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias]]
- [[2025-Society-Generating Hate Anti-Jewish and Anti-Israel Bias in Leading Large]]

### Jainism (2 papers)

- [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]] **[BENCHMARK]**
- [[2025-Sharmaa-Hate Speech Detection in Somali-English Code-Switched]] **[BENCHMARK]**

### Sikhism (1 papers)

- [[0000-projects-BaniDB Shabad OS Digital Gurbani Database]]

### Taoism (0 papers)

*No papers currently tagged with this tradition.*

### Baha'i (0 papers)

*No papers currently tagged with this tradition.*

### Zoroastrianism (0 papers)

*No papers currently tagged with this tradition.*

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
| Indigenous Spirituality | 16 | `\bIndigenous spiritual\b`, `\bAboriginal dreaming\b`, `\bNative American spiritual\b` ... (+13 more) |
| Islam | 13 | `\bIslam\b`, `\bMuslim\b`, `\bQuran\b` ... (+10 more) |
| Jainism | 6 | `\bJain\b`, `\bJainism\b`, `\bahimsa\b.*\b[Jj]ain\b` ... (+3 more) |
| Judaism | 10 | `\bJewish\b`, `\bJudaism\b`, `\bTorah\b` ... (+7 more) |
| Multiple Religions | 4 | `\breligious pluralism\b`, `\binter[-\s]?religious\b`, `\bmultiple religions\b` ... (+1 more) |
| Shinto | 8 | `\bShinto\b`, `\bShintoism\b`, `\bkami\b(?=.*(?:Japan|Shinto|spirit|sacred))` ... (+5 more) |
| Sikhism | 8 | `\bSikh\b`, `\bSikhism\b`, `\bGurbani\b` ... (+5 more) |
| Taoism | 11 | `\bTaois[mt]\b`, `\bDaois[mt]\b`, `\bTao Te Ching\b` ... (+8 more) |
| Ubuntu Philosophy | 4 | `\bUbuntu\b(?!.*(?:[Ll]inux|operat))`, `\bAfrican ethic\b`, `\bAfrican philosophy\b` ... (+1 more) |
| Zoroastrianism | 3 | `\bZoroastrian\b`, `\bAvesta\b`, `\bZarathustra\b` |

---

*Generated: 2026-02-15 | Script: `PYTHON/generate_tradition_gap_report.py` | Papers: 2034 | Traditions: 15*