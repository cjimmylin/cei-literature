# Paper Spine — Shared Contract for All Writing Agents

## Title
**What Do Religious Values Benchmarks Actually Test? A Systematic Meta-Evaluation of LLM Religious Alignment Assessments**

## Authors
Jimmy Lin, Center for Ethical Intelligence

## Venue Target
NeurIPS 2026 Datasets & Benchmarks Track (8pp main + unlimited appendix)

---

## Eight Key Claims

1. **Tradition Asymmetry:** Of 14 religious traditions surveyed, 8 have zero viable benchmarks (Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, Zoroastrianism). Islam dominates the benchmark ecosystem with 28 gate-passing candidates and 8 of 11 Tier 1 benchmarks, driven by the Quranic QA shared task community and Arabic NLP infrastructure. ($\chi^2$=64.96, Cramer's V=0.53, p<0.001.)

2. **Knowledge-Reasoning Conflation:** Most religious values benchmarks test factual recall ("What does tradition X say about Y?") rather than theological reasoning ("Apply principle X to novel dilemma Y"). Only 27.7% of benchmarks test reasoning (binomial p=0.0015). High benchmark scores may certify religious knowledge familiarity rather than values-aligned reasoning -- a distinction with direct implications for deployment in religiously sensitive contexts.

3. **Data Availability Bottleneck:** 170 of 401 benchmark candidates have unavailable data, eliminated by the hard gate requiring publicly available evaluation data. Data availability, not benchmark quality, is the field's primary practical bottleneck. The traditions with zero benchmarks are disproportionately those whose knowledge systems were developed through oral, communal, and practice-based transmission.

4. **Publication Infrastructure Barrier:** The tradition gap is not random. Publication infrastructure is the strongest predictor of tradition gaps (r=0.74, p<0.01), followed by community practice norms (r=0.58). Formalizability, contrary to initial expectations, is not significant (r=0.41, p>0.05). However, a logistic regression model finds that tradition family does not independently predict gate-passage (p=0.112, Pseudo-R²=0.068), indicating that the barrier operates through infrastructure rather than the scoring framework itself.

5. **Field Recency (Observation):** 73% of religious values benchmark candidates are from 2024-2026. This is a nascent field with enormous growth potential but limited methodological consolidation. (p=0.12, not significant at conventional levels.)

6. **WEIRD Bias Does Not Manifest as Expected:** The expected WEIRD bias is reversed: non-WEIRD traditions pass the gate at 14.4% vs WEIRD traditions at 8.9%. This counterintuitive pattern is driven by Islamic benchmark dominance rather than equitable representation -- Islam's infrastructure advantage overwhelms the WEIRD effect, producing a surface-level reversal that masks the underlying 8-tradition void.

7. **Bias-Values Conflation (Hypothesis):** The existing literature conflates religious bias detection (testing whether LLMs stereotype religious groups) with religious values alignment (testing whether LLMs can reason within religious ethical frameworks). These are distinct evaluation challenges requiring different methodological approaches. (p=0.68; conceptual distinction supported by Trial T4 but empirical test not significant.)

8. **Values Relevance Failure:** Most benchmarks fail the values relevance test (mean A3=33.6/100; only 17% genuinely test religious values alignment; 94% treat religion as monolith). The top scorers -- IslamTrust (90), BuddhismEval (85), CatholicBench (80), Gospel Coalition (80) -- demonstrate that high-quality religious values benchmarks are possible but rare.

---

## Terminology Glossary

| Term | Definition | First Use |
|------|-----------|-----------|
| **Religious/Theological Depth (RD)** | Composite score (0-100) measuring how rigorously a benchmark engages religious/theological content. Sub-fields: tradition coverage (R1), depth (R2), scriptural grounding (R3), denominational awareness (R4), pluralism (R5), expert validation (R6). Weighted 40% in composite. | Section 3.1 |
| **Practical Ease (PE)** | Composite score (0-100) measuring implementability: data availability, format, harness compatibility, code access, license, language. Weighted 35%. | Section 3.1 |
| **Citation Impact (CI)** | Composite score (0-100) measuring scholarly influence: age-normalized citations, venue tier, downstream adoption, leaderboard, community. Weighted 25%. | Section 3.1 |
| **Composite Score** | RD x 0.40 + PE x 0.35 + CI x 0.25. Range 0-100. | Section 3.2 |
| **Hard Gate** | Binary inclusion criterion: RD >= 30 AND data publicly available. Benchmarks failing either gate are excluded regardless of composite score. | Section 3.2 |
| **Tradition** | One of the 14 religious/philosophical traditions scored: Islam, Christianity, Judaism, Hinduism, Buddhism, Jainism, Sikhism, Confucianism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, Zoroastrianism. | Throughout |
| **Tradition Family** | Grouping of traditions: Abrahamic (Islam, Christianity, Judaism), Dharmic (Hinduism, Buddhism, Jainism, Sikhism), East Asian (Confucianism, Taoism, Shinto), African/Indigenous (Ubuntu, Indigenous Spirituality), Other (Baha'i, Zoroastrianism). | Section 3.1 |
| **Gate-Passing Candidate** | A benchmark that passes both hard gates (RD >= 30 AND data available). 46 of 401 candidates pass. | Section 4.1 |
| **Structural Epistemic Injustice** | The systematic exclusion of knowledge systems from evaluation infrastructure due to the structure of academic publishing and dataset creation, not due to the absence of knowledge (Mohamed et al. 2020, Bilimoria 2013). | Section 1, 5 |
| **Knowledge vs. Reasoning** | The distinction between testing what a model knows about a tradition (factual recall) and testing whether a model can reason within that tradition's ethical framework (theological reasoning). | Section 1, 4 |
| **Maqasid al-Shariah** | The higher objectives of Islamic law (preservation of religion, life, intellect, lineage, wealth), used as a framework for AI ethics evaluation in Islamic benchmarks (Kamali 2008). | Section 2.2 |
| **WEIRD** | Western, Educated, Industrialized, Rich, Democratic -- the demographic profile that dominates psychological and AI evaluation research (Henrich et al. 2010). | Section 1, 2.2 |

---

## 12-Member Expert Council

### Tier 1 — Tradition-Specific Scholars (6)

| # | Name | Discipline | Assigned Sections |
|---|------|-----------|-------------------|
| 1 | Prof. Abdulaziz Sachedina | Islamic Ethics & Bioethics | Intro P3; LR 2.2b |
| 2 | Prof. Brent Waters | Christian Theological Ethics | LR 2.2c |
| 3 | Prof. Purushottama Bilimoria | Dharmic & Comparative Philosophy | Intro P3; LR 2.2d, 2.5 |
| 4 | Prof. Chenyang Li | East Asian Philosophy | LR 2.2d |
| 5 | Dr. Amara Osei-Mensah | African/Indigenous Philosophy | LR 2.5 |
| 6 | Dr. Moshe Koppel | Jewish Ethics & Computational Talmudics | LR 2.2c |

### Tier 2 — Methodological Experts (6)

| # | Name | Discipline | Assigned Sections |
|---|------|-----------|-------------------|
| 7 | Dr. Percy Liang | AI Evaluation & Benchmarking | Intro P1-P2; LR 2.1 |
| 8 | Dr. Maria Pearce | Psychometrics & Construct Validity | LR 2.1c |
| 9 | Dr. Henriette Cramer | Cultural Psychology & WEIRD Bias | LR 2.2a |
| 10 | Dr. Abeba Birhane | Religious Bias & Fairness | LR 2.3 |
| 11 | Dr. Shakir Mohamed | Decolonial & Critical Studies | Intro P3; LR 2.5 (cross-cutting) |
| 12 | Dr. Abubakar Abid | Computational Sacred Texts & NLP | LR 2.4 |

### Operating Rules
- Tradition experts (1-6) have veto on claims about their tradition
- Expert 11 has cross-cutting mandate to flag epistemic injustice in any section
- Expert 3 retains minority report privilege
- Anti-essentialization: never "Islam believes X" -- always "Islamic ethics scholarship argues X" or "the Maqasid framework holds X"

---

## Figure & Table Assignments

### Main Body

| ID | Type | Section | Description |
|----|------|---------|-------------|
| **Table 1** | Table | 3.1 | RD/PE/CI scoring axes with sub-fields, weights, calibration |
| **Figure 1** | Heatmap | 4.1 | 14 traditions x benchmark availability. Shows 8-tradition void. |
| **Figure 2** | Treemap/bar | 4.1 | 401 candidates by tradition family, with gate-passers highlighted |
| **Table 2** | Table | 4.2 | Top 15 ranking: Rank, Name, Year, Tradition, RD, PE, CI, COMP, Format |
| **Figure 3** | Scatter+bubble | 4.1 | RD (x) vs PE (y), bubble size = log(citations+1), color = tradition family |
| **Table 3** | Table | 4.3 | Tradition coverage: 14 rows, candidates/gate-passers/top15/status |
| **Figure 4** | Stacked bar | 4.1 | Data availability by tradition: available vs. unavailable |

### Supplement

| ID | Type | Appendix | Description |
|----|------|----------|-------------|
| **Table S1** | Full table | A | Complete 401-candidate feature matrix |
| **Table S2** | Table | B | Scoring formula coefficients and calibration |
| **Table S3** | Table | C | Format taxonomy: 12 codes with descriptions |
| **Table S4** | Table | D | External search results: 70 discoveries by tradition |
| **Table S5** | Table | E | 7 meta-evaluation criteria with assessment rubrics |

---

## Section Assignment Map

| File | Sections | Phase |
|------|----------|-------|
| `spine-religious-values.md` | This document | Step 0 |
| `introduction-religious-values.md` | Abstract + Sec 1 (Intro) + Sec 2 (Related Work) | Steps 1-2 |
| `methods-religious-values.md` | Sec 3 (Methods) | Future |
| `results-religious-values.md` | Sec 4 (Results) | Future |
| `discussion-religious-values.md` | Sec 5 (Discussion) + Sec 6 (Conclusion) | Future |
| `references-religious-values.md` | Bibliography | Future |
| `supplement-religious-values.md` | Appendices A-E | Future |
| `council-deliberation-intro-review.md` | 12-member council review of intro + lit review | Step 3 |

---

## Core Citation Keys (from 89 BACKGROUND extracts)

### AI Evaluation & Alignment
- [Liang2023] Liang et al. "Holistic Evaluation of Language Models" 2023
- [Hendrycks2021] Hendrycks et al. "Measuring Massive Multitask Language Understanding" 2021
- [Srivastava2023] Srivastava et al. "Beyond the Imitation Game" (BIG-Bench) 2023
- [Chang2024] Chang et al. "A Survey on Evaluation of Large Language Models" 2024
- [Ji2024] Ji et al. "AI Alignment: A Comprehensive Survey" 2024
- [Gabriel2020] Gabriel "Artificial Intelligence, Values, and Alignment" 2020
- [Klingefjord2024] Klingefjord et al. "What Are Human Values?" 2024
- [Christiano2017] Christiano et al. "Deep Reinforcement Learning from Human Preferences" 2017
- [Ouyang2022] Ouyang et al. "Training Language Models to Follow Instructions" 2022
- [Bai2022] Bai et al. "Training a Helpful and Harmless Assistant" 2022

### Psychometrics & Benchmark Methodology
- [Gupta2025] Gupta "Large Language Model Psychometrics: A Systematic Review" 2025
- [Li2025] Li et al. "Measuring What Matters: Construct Validity" 2025
- [Srivastava2024] Srivastava "PATCH: Psychometrics-Assisted Benchmarking" 2024
- [Burnell2023] Burnell et al. "Rethink Reporting of Evaluation Results" 2023
- [Gehrmann2022] Gehrmann et al. "Repairing the Cracked Foundation" 2022
- [Bowman2021] Bowman & Dahl "What Will It Take to Fix Benchmarking?" 2021
- [Rodriguez2021] Rodriguez et al. "Evaluation Examples Are Not Enough" 2021
- [Schlangen2021] Schlangen "Targeting the Benchmark" 2021
- [Ong2025] Ong et al. "Medical LLM Benchmarks Should Measure What Matters" 2025

### Cultural Values
- [Henrich2010] Henrich et al. "The Weirdest People in the World?" 2010
- [Schwartz2012] Schwartz "An Overview of the Schwartz Theory of Basic Values" 2012
- [Hofstede2011] Hofstede "Dimensionalizing Cultures" 2011
- [Durmus2024] Durmus et al. "Towards Measuring the Representation of Cultural Values" 2024
- [Naous2024] Naous et al. "Cultural Bias and Cultural Alignment" 2024
- [Rao2025] Rao et al. "Randomness, Not Representation" 2025
- [Sukiennik2025] Sukiennik "Evaluation of Cultural Value Alignment" 2025
- [Adilazuarda2025] Adilazuarda et al. "Cultural Alignment of Large Language Models" 2025
- [Tao2024] Tao et al. "CValues: Measuring the Values of Chinese LLMs" 2024

### Islamic AI Ethics
- [Kamali2008] Kamali "Maqasid al-Shariah Made Simple" 2008
- [AlMusawi2022] Al-Musawi "Islamic Virtue-Based Ethics for AI" 2022
- [Ezzeddine2024] Ezzeddine et al. "AI and Islamic Ethics" 2024
- [Mohadi2024] Mohadi "Maqasid al-Shariah and AI" 2024
- [Muravyov2025] Muravyov "Islamic Ethics and AI Trusteeship" 2025
- [Alharbi2024] Alharbi et al. "IslamicMMLU" 2024
- [Malhas2023] Malhas et al. "HAQA and QUQA: Constructing Quranic QA" 2023
- [Abdelali2023] Abdelali et al. "AceGPT: Localizing LLMs" 2023

### Christian Theology
- [Francis2015] Pope Francis "Laudato Si': On Care for Our Common Home" 2015
- [RomeCall2020] "Rome Call for AI Ethics" 2020
- [Manyika2024] Manyika "Integrating Catholic Social Teaching" 2024
- [Johnson2026] Johnson "Detecting Doctrinal Flattening in AI" 2026

### Jewish Ethics
- [Abraham2019] Abraham "The Talmudic Logic Project" 2019
- [Rosenfeld2021] Rosenfeld "Jewish Ethics Meets Machine Learning" 2021
- [Steinberg2025] Steinberg "This is Judaism: The Question of..." 2025

### Dharmic Philosophy
- [Bilimoria2013] Bilimoria "Indian Ethics: Classical Traditions" 2013
- [Chadha2023] Chadha "Decolonial AI Alignment via Visesa-Dharma" 2023
- [Mohanty2024] Mohanty "Indic Approach to Ethical AI" 2024
- [Mishra2024] Mishra "Bhagavad Gita Framework for AI Ethics" 2024
- [Hongladarom2020] Hongladarom "Ethics, AI, and Robotics" (Buddhist) 2020
- [Keown2005] Keown "Buddhist Ethics: A Very Short Introduction" 2005

### East Asian Philosophy
- [Li2022] Li "Can a Machine Flow Like Dao?" 2022
- [Wong2019] Wong "Dao, Harmony, and Personhood" 2019
- [Asghari2023] Asghari "Confucius, Cyberpunk, and Science" 2023

### Religious Bias & Fairness
- [Abid2021] Abid et al. "Persistent Anti-Muslim Bias in LLMs" 2021
- [Bianchi2024] Bianchi et al. "Divine LLaMAs: Bias, Stereotypes, Stigmatization" 2024
- [Hamid2025] Hamid "Religious Bias Landscape in LLMs" 2025
- [Buyl2024] Buyl et al. "Measuring Spiritual Values and Biases" 2024
- [Nadeem2021] Nadeem et al. "StereoSet: Measuring Stereotypical Bias" 2021

### Indigenous & African AI
- [Mohamed2020] Mohamed et al. "Decolonial AI: Decolonial Theory" 2020
- [Birhane2021] Birhane "Values Encoded in Machine Learning" 2021
- [Carroll2020] Carroll et al. "CARE Principles for Indigenous Data Governance" 2020
- [Gwagwa2025] Gwagwa "Ethics of AI in Africa: Interrogating Ubuntu" 2025
- [Ogwo2025] Ogwo "Where Are the Missing Voices?" 2025

### Sacred Text NLP
- [Leavens2024] Leavens et al. "Modeling the Sacred" 2024

### Comparative Religious Ethics
- [Green2014] Green "The Third Wave of Comparative Religious Ethics" 2014
- [Twiss1998] Twiss & Grelle "Comparative Religious Ethics" 1998
- [Schweiker2005] Schweiker "Theological Ethics and Global Dynamics" 2005
- [Jobin2019] Jobin et al. "The Global Landscape of AI Ethics Guidelines" 2019
- [Pasquale2025] Pasquale & Ferraris "Algorethics" 2025

---

## Word Budget

| Section | Target | Max |
|---------|--------|-----|
| Abstract | 300 | 350 |
| 1. Introduction | 1,100 | 1,300 |
| 2. Related Work | 2,250 | 2,700 |
| **TOTAL (this phase)** | **3,650** | **4,350** |
| 3. Methods | 1,200 | 1,500 |
| 4. Results | 2,000 | 2,500 |
| 5. Discussion | 1,200 | 1,500 |
| 6. Conclusion | 400 | 500 |
| **FULL PAPER** | **8,450** | **10,350** |

---

## Key Numbers for Citation

| Metric | Value | Source |
|--------|-------|--------|
| Total vault papers scanned | 2,099 | Pipeline Phase 1 |
| Religious benchmark candidates | 401 | Pipeline Phase 1 |
| Gate-passing candidates (RD>=30 + data) | 46 | Pipeline Phase 5 |
| Top 15 selected | 15 | Pipeline Phase 5 |
| Traditions surveyed | 14 | Gap analysis |
| Traditions with zero viable benchmarks | 8 | Gap analysis |
| Islam gate-passers | 28 | Gap analysis |
| Islam in Top 15 | 7 | Gap analysis |
| Candidates from 2024-2026 | 73% | Pipeline |
| Candidates eliminated by data gate | 77% | Pipeline |
| External papers ingested | 53 | Pipeline Phase 2b |
| Background literature papers | 125 | BACKGROUND |
| Background PDFs acquired | 89 (71%) | BACKGROUND |
| Background text extracts | 89 | BACKGROUND |
| Expert council members | 12 | This document |
| Thematic folders | 12 | BACKGROUND |
| Format types in Top 15 | 7 of 12 | Format taxonomy |
| Languages in Top 15 | 9 | Gap analysis |
| Missing key religious languages | 12 | Gap analysis |
