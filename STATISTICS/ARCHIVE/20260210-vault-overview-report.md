# Comprehensive Vault Overview: LLM Ethics & Values Alignment Resources

**Generated:** 2026-02-10 | **Papers:** 924 screened, 528 benchmark candidates | **Normative ethics:** 45 papers

---

## Table of Contents

- [1. Executive Summary](#1.-executive-summary)
- [2. Landscape Overview](#2.-landscape-overview)
- [3. Benchmark Taxonomy (10 Categories)](#3.-benchmark-taxonomy-10-categories)
- [4. Measurement Approaches](#4.-measurement-approaches)
- [5. Model Coverage Matrix](#5.-model-coverage-matrix)
- [6. Cultural & Pluralistic Coverage](#6.-cultural-&-pluralistic-coverage)
- [7. Data Availability](#7.-data-availability)
- [8. Normative Ethics Deep Dive](#8.-normative-ethics-deep-dive)
- [9. Ready-to-Use Resources for SOTA Testing](#9.-ready-to-use-resources-for-sota-testing)
- [10. Temporal Trends](#10.-temporal-trends)
- [11. Gap Analysis](#11.-gap-analysis)
- [12. Recommendations for Values Alignment Research](#12.-recommendations-for-values-alignment-research)
- [13. Methodology](#13.-methodology)
- [Appendix A: Full Benchmark Candidate List](#appendix-a-full-benchmark-candidate-list)
- [Appendix B: Normalization Definitions](#appendix-b-normalization-definitions)

---

## 1. Executive Summary

This vault contains **924 papers** spanning AI ethics, moral reasoning, fairness, safety, and values alignment research from 2010 to 2026. A systematic 20-agent deep-read identified **528 papers** (57%) as containing or proposing benchmarks, datasets, or evaluation metrics relevant to LLM ethics evaluation. The remaining 396 papers provide theoretical, philosophical, or survey contributions without empirical evaluation artifacts.

Of the benchmark candidates, **76%** have some pluralistic relevance (addressing diverse cultural or value perspectives), though systematic coverage remains uneven. Western ethical traditions (deontology, consequentialism, virtue ethics) are moderately represented, while Ubuntu, Buddhist, and Indigenous ethical frameworks have **zero benchmark coverage**. English dominates overwhelmingly, with Chinese and Korean as the most active non-English benchmark languages.

**306 benchmarks** (57%) have publicly available data or code, providing a substantial foundation for immediate values alignment evaluation. The most tested model families are GPT-4, GPT-3.5/ChatGPT, and Llama, with recent growth in Gemini, Mistral, and Qwen evaluation.

### Summary of Findings

| Dimension | Finding |
|-----------|---------|
| Total papers | 924 screened, 528 benchmark candidates |
| Largest category | 10. Helpfulness, Honesty & RLHF (299 papers) |
| Multi-category papers | 479 (90%) |
| Pluralistic relevance | 205 Yes + 198 Partial = 76% |
| Public availability | 287 Public + 19 Code available |
| Most evaluated model | Llama (72 papers) |
| Normative ethics | 7 Yes + 38 Borderline |
| Unique authors | 846 |

---

## 2. Landscape Overview

**924 papers** were screened. **528** (57%) contain benchmark/evaluation resources; **396** (42%) are theoretical, philosophical, or survey papers.

### Year Distribution

| Year | All Papers | Benchmark Candidates | Candidate % |
|------|-----------|---------------------|-------------|
| 2010 | 1  | 0 | 0% |
| 2011 | 0  | 0 | - |
| 2012 | 0  | 0 | - |
| 2013 | 0  | 0 | - |
| 2014 | 0  | 0 | - |
| 2015 | 1  | 0 | 0% |
| 2016 | 6 ██ | 1 | 16% |
| 2017 | 0  | 0 | - |
| 2018 | 13 ████ | 7 | 53% |
| 2019 | 12 ████ | 7 | 58% |
| 2020 | 21 ███████ | 11 | 52% |
| 2021 | 24 ████████ | 10 | 41% |
| 2022 | 45 ███████████████ | 26 | 57% |
| 2023 | 117 ███████████████████████████████████████ | 51 | 43% |
| 2024 | 284 ██████████████████████████████████████████████████████████████████████████████████████████████ | 160 | 56% |
| 2025 | 377 █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ | 237 | 62% |
| 2026 | 23 ███████ | 18 | 78% |

### Top Prolific First Authors

| # | Author | Papers |
|---|--------|--------|
| 1 | Dan Hendrycks | 4 |
| 2 | Paul Röttger | 4 |
| 3 | Yejin Bang | 4 |
| 4 | Liwei Jiang | 4 |
| 5 | Yu Ying Chiu | 4 |
| 6 | Taylor Sorensen | 4 |
| 7 | Elizaveta Tennant | 4 |
| 8 | Edmond Awad | 3 |
| 9 | Iason Gabriel | 3 |
| 10 | Jakob Stenseke | 3 |
| 11 | Ashutosh Dwivedi | 3 |
| 12 | Jiaming Ji | 3 |
| 13 | Jing Yao | 3 |
| 14 | Zhaowei Zhang | 3 |
| 15 | Shaona Ghosh | 3 |

---

## 3. Benchmark Taxonomy (10 Categories)

Papers are classified into 10 categories using keyword matching on benchmark names, measurement descriptions, and agent reasoning. Papers may appear in multiple categories.

### Category Distribution

| # | Category | Papers | Description |
|---|----------|--------|-------------|
| 1 | Moral Reasoning & Ethical Judgment | 268 ██████████████████████████ | Benchmarks that test LLMs on moral dilemmas, ethical scenarios, and normative... |
| 2 | Value Alignment & Value Pluralism | 150 ███████████████ | Benchmarks measuring how well LLMs align with human values, preferences, and... |
| 3 | Cultural & Cross-Cultural Ethics | 193 ███████████████████ | Benchmarks examining cultural sensitivity, cross-cultural moral variation, an... |
| 4 | Fairness, Bias & Social Norms | 233 ███████████████████████ | Benchmarks measuring social biases (gender, race, religion, etc.), fairness,... |
| 5 | Toxicity, Hate Speech & Harmful Content | 94 █████████ | Benchmarks for detecting, measuring, or mitigating toxic, hateful, or otherwi... |
| 6 | Safety & Red Teaming | 181 ██████████████████ | Benchmarks for evaluating LLM safety, jailbreak robustness, and adversarial a... |
| 7 | Domain-Specific Ethics | 117 ███████████ | Benchmarks for ethical evaluation in specific professional domains (medical,... |
| 8 | Normative Ethics Benchmarks | 65 ██████ | Benchmarks specifically grounded in normative ethical theories (deontology, c... |
| 9 | Moral Psychology Applied to AI | 62 ██████ | Benchmarks applying moral psychology constructs (moral foundations, moral dev... |
| 10 | Helpfulness, Honesty & RLHF | 299 █████████████████████████████ | Benchmarks evaluating helpfulness, honesty, harmlessness (HHH), and RLHF-rela... |

*479 papers (90%) appear in 2+ categories.*

### Category x Year Cross-Tabulation (2018-2026)

| Category | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Moral Reasoning & Ethical | 4 | 1 | 6 | 3 | 14 | 27 | 67 | 137 | 9 | 268 |
| Value Alignment & Value P | - | - | - | 3 | 5 | 15 | 47 | 74 | 6 | 150 |
| Cultural & Cross-Cultural | 1 | 2 | 4 | 1 | 4 | 22 | 61 | 90 | 8 | 193 |
| Fairness, Bias & Social N | 4 | 4 | 9 | 6 | 14 | 23 | 66 | 99 | 7 | 232 |
| Toxicity, Hate Speech & H | 2 | 5 | 3 | 2 | 12 | 7 | 29 | 33 | 1 | 94 |
| Safety & Red Teaming | - | 1 | - | 1 | 9 | 17 | 65 | 81 | 7 | 181 |
| Domain-Specific Ethics | 2 | 1 | 2 | - | 3 | 12 | 35 | 59 | 3 | 117 |
| Normative Ethics Benchmar | - | - | 3 | 2 | 3 | 7 | 21 | 29 | - | 65 |
| Moral Psychology Applied  | 1 | 1 | 3 | - | 3 | 6 | 18 | 26 | 4 | 62 |
| Helpfulness, Honesty & RL | 3 | - | 1 | 3 | 19 | 38 | 86 | 138 | 11 | 299 |
| **Total** | 17 | 15 | 31 | 21 | 86 | 174 | 495 | 766 | 56 | **1661** |

### Category Co-occurrence Matrix

*Number of papers appearing in both categories (row × column):*

| Cat | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | - | 49 | 84 | 114 | 24 | 59 | 75 | 64 | 58 | 144 |
| 2 | 49 | - | 72 | 68 | 11 | 38 | 30 | 10 | 12 | 115 |
| 3 | 84 | 72 | - | 83 | 29 | 60 | 40 | 16 | 21 | 121 |
| 4 | 114 | 68 | 83 | - | 49 | 70 | 50 | 33 | 31 | 121 |
| 5 | 24 | 11 | 29 | 49 | - | 59 | 12 | 1 | 5 | 41 |
| 6 | 59 | 38 | 60 | 70 | 59 | - | 38 | 11 | 14 | 117 |
| 7 | 75 | 30 | 40 | 50 | 12 | 38 | - | 22 | 20 | 75 |
| 8 | 64 | 10 | 16 | 33 | 1 | 11 | 22 | - | 14 | 42 |
| 9 | 58 | 12 | 21 | 31 | 5 | 14 | 20 | 14 | - | 26 |
| 10 | 144 | 115 | 121 | 121 | 41 | 117 | 75 | 42 | 26 | - |

---

## 4. Measurement Approaches

Methodology types extracted from 528 benchmark candidates via regex normalization. 79 entries had no recognized methodology type.

### Methodology Type Prevalence

| # | Methodology | Count | % of Candidates |
|---|------------|-------|-----------------|
| 1 | Scenario/vignette judgment | 179 | 33% |
| 2 | Human preference/comparison | 150 | 28% |
| 3 | Classification task | 85 | 16% |
| 4 | Benchmark suite (multi-task) | 67 | 12% |
| 5 | Adversarial/red-teaming | 55 | 10% |
| 6 | Multi-turn dialogue | 46 | 8% |
| 7 | Survey/questionnaire | 41 | 7% |
| 8 | Multiple-choice QA | 39 | 7% |
| 9 | Template/probing | 38 | 7% |
| 10 | Game/simulation | 37 | 7% |
| 11 | Free-text generation | 37 | 7% |
| 12 | Crowdsourced annotation | 24 | 4% |
| 13 | Likert/scale rating | 15 | 2% |
| 14 | Embedding analysis | 6 | 1% |

### Methodology x Category (Top 8)

| Methodology | Moral Reasoning & Et | Value Alignment & Va | Cultural & Cross-Cul | Fairness, Bias & Soc | Toxicity, Hate Speec | Safety & Red Teaming | Domain-Specific Ethi | Normative Ethics Ben | Moral Psychology App | Helpfulness, Honesty | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Scenario/vignette judgmen | 133 | 44 | 54 | 66 | 12 | 43 | 45 | 42 | 31 | 102 | 572 |
| Human preference/comparis | 73 | 56 | 45 | 67 | 26 | 53 | 38 | 13 | 22 | 113 | 506 |
| Classification task | 45 | 15 | 31 | 37 | 30 | 29 | 13 | 10 | 13 | 37 | 260 |
| Benchmark suite (multi-ta | 28 | 14 | 22 | 28 | 24 | 40 | 18 | 4 | 6 | 31 | 215 |
| Adversarial/red-teaming | 15 | 10 | 19 | 16 | 21 | 53 | 9 | 2 | 2 | 31 | 178 |
| Multi-turn dialogue | 17 | 14 | 12 | 17 | 10 | 20 | 11 | 4 | 2 | 42 | 149 |
| Survey/questionnaire | 21 | 30 | 23 | 21 | 4 | 11 | 9 | 3 | 13 | 28 | 163 |
| Multiple-choice QA | 9 | 14 | 19 | 13 | 3 | 18 | 12 | 2 | 1 | 23 | 114 |
| **Total** | 341 | 197 | 225 | 265 | 130 | 267 | 155 | 80 | 90 | 407 | **2157** |

---

## 5. Model Coverage Matrix

Model families extracted from `models_evaluated` field. **196** candidates (37%) mention specific models; **332** do not specify models tested.

- **LLM-era benchmarks** (GPT-3+, Claude, Llama, etc.): 166
- **Pre-LLM benchmarks** (BERT, Word2Vec only): 27

### Model Family Prevalence

| # | Model Family | Papers | % |
|---|-------------|--------|---|
| 1 | Llama | 72 █████████ | 13% |
| 2 | GPT-4 | 68 ████████ | 12% |
| 3 | GPT-3.5 | 42 █████ | 7% |
| 4 | Gemini | 40 █████ | 7% |
| 5 | Claude | 36 ████ | 6% |
| 6 | Mistral/Mixtral | 26 ███ | 4% |
| 7 | BERT family | 25 ███ | 4% |
| 8 | DeepSeek | 20 ██ | 3% |
| 9 | GPT-3 | 10 █ | 1% |
| 10 | GPT-2 | 9 █ | 1% |
| 11 | Qwen | 8 █ | 1% |
| 12 | Gemma | 8 █ | 1% |
| 13 | Anthropic models | 7  | 1% |
| 14 | Delphi | 7  | 1% |
| 15 | Vicuna | 5  | 0% |
| 16 | T5/Flan | 4  | 0% |
| 17 | PaLM | 4  | 0% |
| 18 | ChatGLM | 4  | 0% |
| 19 | DialoGPT | 3  | 0% |
| 20 | Alpaca | 3  | 0% |

### Model Family x Category (Top 12)

| Model | Moral Reasoning & Et | Value Alignment & Va | Cultural & Cross-Cul | Fairness, Bias & Soc | Toxicity, Hate Speec | Safety & Red Teaming | Domain-Specific Ethi | Normative Ethics Ben | Moral Psychology App | Helpfulness, Honesty | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Llama | 47 | 23 | 25 | 34 | 11 | 19 | 19 | 12 | 15 | 44 | 249 |
| GPT-4 | 44 | 18 | 20 | 23 | 10 | 21 | 20 | 11 | 14 | 34 | 215 |
| GPT-3.5 | 28 | 11 | 17 | 28 | 6 | 8 | 13 | 10 | 12 | 15 | 148 |
| Gemini | 32 | 5 | 12 | 14 | 5 | 12 | 17 | 7 | 6 | 22 | 132 |
| Claude | 24 | 12 | 7 | 14 | 2 | 8 | 11 | 7 | 5 | 22 | 112 |
| Mistral/Mixtral | 17 | 9 | 10 | 11 | 3 | 7 | 4 | 4 | 6 | 15 | 86 |
| BERT family | 13 | 4 | 10 | 13 | 5 | - | 5 | 4 | 3 | 8 | 65 |
| DeepSeek | 15 | 5 | 7 | 7 | 2 | 6 | 5 | 4 | 3 | 9 | 63 |
| GPT-3 | 6 | 2 | 1 | 7 | 3 | 3 | 2 | 2 | 3 | 6 | 35 |
| GPT-2 | 3 | 3 | 3 | 7 | 3 | 1 | 2 | - | 2 | 3 | 27 |
| Qwen | 5 | 4 | 6 | 1 | 1 | 3 | 3 | 2 | 1 | 5 | 31 |
| Gemma | 7 | 3 | 4 | 4 | 1 | 3 | 2 | 1 | 1 | 6 | 32 |
| **Total** | 241 | 99 | 122 | 163 | 52 | 91 | 103 | 64 | 71 | 189 | **1195** |

---

## 6. Cultural & Pluralistic Coverage

### Pluralistic Relevance

| Relevance | Count | % |
|-----------|-------|---|
| Yes | 205 | 38% |
| Partial | 198 | 37% |
| No | 125 | 23% |

### Ethical Traditions Detected

| Tradition | Mentions | Coverage Level |
|-----------|----------|---------------|
| Consequentialist | 20 | Moderate |
| Islamic | 13 | Moderate |
| Care Ethics | 3 | Very Low |
| Indigenous | 2 | Very Low |
| Deontological | 2 | Very Low |
| Confucian | 2 | Very Low |
| Virtue Ethics (Western) | 2 | Very Low |
| Buddhist | 1 | Very Low |
| Hindu | 1 | Very Low |
| Ubuntu | 0 | **None** |

### Languages Detected

| Language | Mentions | Coverage Level |
|----------|----------|---------------|
| Chinese | 40 | Strong |
| English | 34 | Strong |
| Japanese | 10 | Emerging |
| Arabic | 9 | Emerging |
| Spanish | 8 | Emerging |
| German | 6 | Emerging |
| Hindi | 5 | Emerging |
| Russian | 5 | Emerging |
| French | 4 | Emerging |
| Indonesian | 3 | Minimal |
| Korean | 3 | Minimal |
| Italian | 3 | Minimal |
| Portuguese | 2 | Minimal |
| Bengali | 2 | Minimal |
| Swahili | 2 | Minimal |
| Urdu | 2 | Minimal |
| Dutch | 1 | Minimal |
| Vietnamese | 1 | Minimal |
| Thai | 0 | **None** |
| Turkish | 0 | **None** |

### Language x Category (Top 10)

| Language | Moral Reasoning & Et | Value Alignment & Va | Cultural & Cross-Cul | Fairness, Bias & Soc | Toxicity, Hate Speec | Safety & Red Teaming | Domain-Specific Ethi | Normative Ethics Ben | Moral Psychology App | Helpfulness, Honesty | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Chinese | 19 | 11 | 40 | 10 | 5 | 20 | 11 | 5 | 3 | 24 | 148 |
| English | 12 | 6 | 26 | 17 | 9 | 8 | 3 | 2 | 4 | 16 | 103 |
| Japanese | 7 | 1 | 10 | 5 | 1 | 2 | 3 | 1 | 1 | 6 | 37 |
| Arabic | 2 | 4 | 9 | 2 | 1 | 3 | 3 | - | 1 | 5 | 30 |
| Spanish | 5 | - | 7 | 4 | 2 | 1 | - | 1 | 3 | - | 23 |
| German | - | 3 | 2 | 4 | 4 | 3 | 2 | - | - | 3 | 21 |
| Hindi | 3 | - | 5 | 1 | 2 | 1 | - | 1 | 1 | 1 | 15 |
| Russian | 5 | - | 4 | 3 | - | - | 1 | 2 | 2 | - | 17 |
| French | 3 | - | 3 | 2 | 1 | 1 | - | - | 1 | 2 | 13 |
| Indonesian | - | - | 3 | - | 2 | 2 | - | - | - | - | 7 |
| **Total** | 56 | 25 | 109 | 48 | 27 | 41 | 23 | 12 | 16 | 57 | **414** |

---

## 7. Data Availability

| Availability | Count | % |
|-------------|-------|---|
| Public | 287 | 54% |
| Code available | 19 | 3% |
| Not stated | 222 | 42% |

### Availability x Category

| Availability | Moral Reasoning & Et | Value Alignment & Va | Cultural & Cross-Cul | Fairness, Bias & Soc | Toxicity, Hate Speec | Safety & Red Teaming | Domain-Specific Ethi | Normative Ethics Ben | Moral Psychology App | Helpfulness, Honesty | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Public | 119 | 68 | 102 | 135 | 68 | 114 | 40 | 22 | 26 | 156 | 850 |
| Code available | 11 | 7 | 7 | 8 | 2 | 6 | 4 | 4 | 3 | 11 | 63 |
| Not stated | 138 | 75 | 84 | 90 | 24 | 61 | 73 | 39 | 33 | 132 | 749 |
| **Total** | 268 | 150 | 193 | 233 | 94 | 181 | 117 | 65 | 62 | 299 | **1662** |

### Repository Links

**GitHub repositories:** 28 identified

- [[2023-Huang-Flames]]: https://github.com/AIFlames/Flames
- [[2024-Bonagiri-SaGE Semantic Graph Entropy Moral Consistency Corpus]]: https://github.com/vnnm404/SaGE
- [[2024-Bonagiri-SaGE]]: https://github.com/vnnm404/SaGE
- [[2024-Chern-BeHonest]]: https://github.com/GAIR-NLP/BeHonest
- [[2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation]]: https://github.com/CentreSecuriteIA/BELLS
- [[2024-Guldimann-COMPL-AI EU AI Act Compliance]]: https://github.com/compl-ai/compl-ai
- [[2024-Gupta-WalledEval]]: https://github.com/walledai/walledeval
- [[2024-Han-MedSafetyBench]]: https://github.com/AI4LIFE-GROUP/med-safety-bench
- [[2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values]]: https://github.com/Derekkk/VIVA_EMNLP24
- [[2024-Jin-Language Model Alignment in Multilingual Trolley]]: https://github.com/causalNLP/moralmachine
- [[2024-Jin-MULTITP - Language Model Alignment in Multilingual Trolley Problems]]: https://github.com/causalNLP/moralmachine
- [[2024-Kaiyom-HELM Safety]]: https://github.com/stanford-crfm/helm
- [[2024-Li-SALAD-Bench]]: https://github.com/OpenSafetyLab/SALAD-BENCH
- [[2024-Li-Value-Spectrum]]: https://github.com/Jeremyyny/Value-Spectrum
- [[2024-Tom-SG-Bench - Evaluating LLM Safety Generalization]]: https://github.com/MurrayTom/SG-Bench
- [[2024-Wang-Do-Not-Answer]]: https://github.com/Libr-AI/do-not-answer
- [[2024-Yanaka-JBBQ Japanese Bias Benchmark for Question Answering]]: https://github.com/ynklab/JBBQ_data
- [[2024-Yanaka-JBBQ]]: https://github.com/ynklab/JBBQ_data
- [[2024-Yin-SafeAgentBench]]: https://github.com/shengyin1224/SafeAgentBench
- [[2024-Yu-CoSafe]]: https://github.com/ErxinYu/CoSafe-Dataset
- [[2024-Yuan-R-Judge]]: https://github.com/Lordog/R-Judge
- [[2024-Yuan-Social Measuring Social Norms of LLMs]]: https://github.com/socialnormdataset/socialagent
- [[2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents]]: https://github.com/thu-coai/Agent-SafetyBench
- [[2024-Zhang-CHiSafetyBench - A Chinese Hierarchical Safety Benchmark for LLMs]]: https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench
- [[2024-AlKhamissi-Investigating Cultural Alignment of LLMs]]: https://github.com/bkhmsi/cultural-trends.git
- [[2024-Bhardwaj-Language Models are Homer Simpson! Safety]]: https://github.com/declare-lab/resta
- [[2024-Huang-Moral Persuasion in Large Language Models]]: https://github.com/acyhuang/moral-persuasion
- [[2024-Kirgis-Differences in Moral Foundations of LLMs]]: https://github.com/peterkirgis/llm-moral-foundations

**HuggingFace:** 3 identified

- [[2024-Han-WildGuard WildGuardTest]]: https://huggingface.co/datasets/allenai/wildguardmix
- [[2024-Kaneko-Eagle Ethical Dataset Given from Real Interactions]]: https://huggingface.co/datasets/MasahiroKaneko/eagle
- [[2024-Kaneko-Eagle]]: https://huggingface.co/datasets/MasahiroKaneko/eagle

---

## 8. Normative Ethics Deep Dive

From 266 papers evaluated for normative ethics content (EXSR batch), **7** were classified as **Yes** (explicitly operationalize normative ethical theories) and **38** as **Borderline** (touch on normative concepts without full operationalization).

### Framework Distribution

| Framework | Mentions |
|-----------|----------|
| Consequentialism/Utilitarianism | 27 |
| Deontology/Kantian | 26 |
| Virtue Ethics | 8 |
| Principlism | 8 |
| Contractualism/Rawlsian | 6 |
| Commonsense Morality | 3 |
| Moral Foundations Theory | 3 |
| Kohlberg's Moral Development | 2 |
| Distributive Justice | 1 |
| Confucian Ethics | 1 |
| Hindu Ethics | 1 |
| Moral dilemmas (likely involving competing normative princip | 1 |
| Social Choice Theory | 1 |
| Unknown - title suggests moral benchmarking with structured | 1 |
| Safety principles that may derive from normative frameworks | 1 |
| Medical ethics principles from 67 Japan Medical Association | 1 |

*29 papers test multiple normative frameworks.*

### Papers with Full Normative Ethics Operationalization

| Paper | Frameworks | LLMs Tested | Data Artifact |
|-------|-----------|-------------|---------------|
| [[2024-Agarwal-Ethical Reasoning and Moral Value Alignment Multilingual]] | Deontology, virtue ethics, consequentialism (th... | GPT-4, ChatGPT, Llama2-Chat-70B | Ethical dilemmas and policies from three normat... |
| [[2024-Moore-Intuitions of Compromise - Utilitarianism vs. Contractualism]] | Utilitarianism (Utilitarian Sum), Contractualis... | GPT-4 and additional LLMs (referenced... | Systematically generated value aggregation scen... |
| [[2024-retrieved-Cross-Linguistic Moral Preferences in LLMs - Evidence from]] | Distributive justice (Rawlsian/egalitarian fram... | LLMs tested cross-linguistically (spe... | 1,201,200 observations across ten professional... |
| [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | Principlism (Beauchamp & Childress): Autonomy,... | Multiple LLMs including frontier clos... | PrinciplismQA - 3,648 questions (MCQ from textb... |
| [[2025-Huang-BehaviorBench Multi-Tier Benchmark for Agent Behavior Editing]] | Deontology, virtue ethics, justice, commonsense... | 9 open-weight LLMs (LLaMA-2-7B, LLaMA... | BEHAVIORBENCH: 1,001 moral scenarios across 10... |
| [[2025-Takeshita-JETHICS - Japanese Ethics Understanding Evaluation Dataset]] | Utilitarianism, Deontology (role-based obligati... | GPT-4o, plus multiple non-proprietary... | JETHICS: 78K Japanese moral examples across 5 c... |
| [[2025-Unknown-Moral Alignment for LLM Agents Intrinsic Rewards]] | Deontological Ethics (Kant, duty-based norms li... | Gemma2-2b-it fine-tuned with RL using... | Iterated Prisoner's Dilemma (IPD) environment w... |

---

## 9. Ready-to-Use Resources for SOTA Testing

**306 benchmarks** have publicly available data or code. Sorted by recency (most recent first).

### Recent Public Benchmarks (2023-2026): 258 available

| # | Year | Paper | Benchmark | What It Measures | Availability |
|---|------|-------|-----------|-----------------|--------------|
| 1 | 2026 | [[2026-Dang-RedBench]] | RedBench | LLM safety robustness against adversarial... | Public |
| 2 | 2026 | [[2026-Goel-Building Interpretable Models for Moral Decision-Making]] | Interpretable Moral Machine Transformer | How neural networks encode and process mor... | Public |
| 3 | 2026 | [[2026-Guey-BiasLab Multilingual Dual-Framing Framework]] | BiasLab | Output-level (extrinsic) bias in LLMs acro... | Public |
| 4 | 2026 | [[2026-He-GVS-Scale and GVS-Bench GenAI Value Safety Scale]] | GVS-Scale / GVS-Bench | GenAI value safety across lifecycle-orient... | Public |
| 5 | 2026 | [[2026-Jin-MedES Chinese Medical Ethics Scenarios]] | MedES | Medical ethics alignment of LLMs in Chines... | Public |
| 6 | 2026 | [[2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks]] | Theory Trace Card (TTC) | Proposes a documentation standard for soci... | Public |
| 7 | 2026 | [[2026-Lee-BiasJailbreak]] | BiasJailbreak | Ethical biases in LLMs that can be exploit... | Public |
| 8 | 2026 | [[2026-Shen-PsychEthicsBench]] | PsychEthicsBench | Ethical knowledge and behavioral responses... | Public |
| 9 | 2025 | [[2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in]] | Unnamed (WVS-based cultural value ada... | Cultural value adaptation in LLMs: whether... | Public (GitHub: faridlazuarda/from-su... |
| 10 | 2025 | [[2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic]] | AraTrust | Trustworthiness of LLMs in Arabic across 9... | Public (HuggingFace: asas-ai/AraTrust) |
| 11 | 2025 | [[2025-Alwajih-Palm]] | PALM | Cultural sensitivity and inclusivity of LL... | Public (code, annotation guidelines,... |
| 12 | 2025 | [[2025-Andriushchenko-AgentHarm]] | AgentHarm | Harmfulness of LLM agents: compliance with... | Public (HuggingFace: ai-safety-instit... |
| 13 | 2025 | [[2025-Ashkinaze-Deep Value Benchmark]] | Deep Value Benchmark (DVB) | Whether LLMs learn fundamental human value... | Public (dataset released with human v... |
| 14 | 2025 | [[2025-Rahman-CCD-Bench Probing Cultural Conflict in LLM Decision-Making]] | CCD-Bench | LLM decision-making under cross-cultural v... | Public |
| 15 | 2025 | [[2025-Backmann-When Ethics and Payoffs Diverge LLM Agents in Morally Charged Social]] | MORALSIM | LLM moral behavior when ethical norms conf... | Public (GitHub: sbackmann/moralsim) |
| 16 | 2025 | [[2025-Backmann-When Ethics and Payoffs Diverge]] | MORALSIM | LLM moral behavior in social dilemmas wher... | Public (GitHub: sbackmann/moralsim) |
| 17 | 2025 | [[2025-Bae-CharMoral]] | CharMoral | Moral evolution and dynamic morality of ch... | Public (GitHub: BaeSuyoung/CharMoral) |
| 18 | 2025 | [[2025-Banerjee-SafeInfer]] | HarmEval | LLM safety: potential misuse scenarios ali... | Public (GitHub: NeuralSentinel/SafeIn... |
| 19 | 2025 | [[2025-Becker-The Moralization Corpus]] | Moralization Corpus | Detection and extraction of moralizations... | Public |
| 20 | 2025 | [[2025-Bouchard-How to Assess Your LLM Use Case for Bias and]] | LangFair | Bias and fairness in LLM outputs: toxicity... | Public |
| 21 | 2025 | [[2025-Bouchekif-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and]] | QIAS 2025 | LLM reasoning in Islamic jurisprudence: in... | Public |
| 22 | 2025 | [[2025-Bulla-Large Language Models meet moral values]] | Unnamed (MFT-based LLM moral evaluation) | LLM ability to detect and classify moral v... | Public |
| 23 | 2025 | [[2025-Castricato-PERSONA Pluralistic Alignment Testbed]] | PERSONA / PERSONA Bench | Pluralistic alignment of LLMs with diverse... | Public |
| 24 | 2025 | [[2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values]] | MoVa | Classification of human morals and values... | Public |
| 25 | 2025 | [[2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment]] | SPICA | Pluralistic in-context alignment: whether... | Public |
| 26 | 2025 | [[2025-Cheng-ELEPHANT Social Sycophancy]] | ELEPHANT | Social sycophancy in LLMs: excessive prese... | Public |
| 27 | 2025 | [[2025-Chiu-CulturalBench]] | CulturalBench | LLM cultural knowledge across 45 global re... | Public |
| 28 | 2025 | [[2025-Chiu-MoReBench]] | MoReBench / MoReBench-Theory | Procedural and pluralistic moral reasoning... | Public |
| 29 | 2025 | [[2025-Chiu-Will AI Tell Lies to Save Sick Children]] | LITMUSVALUES / AIRISKDILEMMAS | AI value prioritization and its connection... | Public |
| 30 | 2025 | [[2025-Chua-RabakBench]] | RabakBench | Multilingual safety of LLMs in Singapore's... | Public |
| 31 | 2025 | [[2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical]] | SFF (Syntactic Framing Fragility) | Robustness of LLM ethical judgments to syn... | Code available (github.com) |
| 32 | 2025 | [[2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al.]] | RMP (Reward Model Perspectives) | Sociodemographic biases in reward models;... | Code available (github.com/socialnlp/... |
| 33 | 2025 | [[2025-Fan-FAIRMT-BENCH]] | FairMT-Bench | Fairness in LLMs during multi-turn dialogu... | Public (github.com/FanZT6/FairMT-bench) |
| 34 | 2025 | [[2025-Gai-MoralBench A Multi-Faceted Benchmark Gai et al.]] | MoralBench | Moral reasoning capabilities of LLMs based... | Public (Google Drive + GitHub: github... |
| 35 | 2025 | [[2025-Galatolo-Beyond Ethical Alignment AMAs]] | AMAeval (Artificial Moral Assistant E... | LLM capabilities as Artificial Moral Assis... | Code available (github.com/alessioGal... |
| 36 | 2025 | [[2025-Ghosh-AEGIS 2.0]] | AEGIS 2.0 | AI content safety across 12 hazard categor... | Public (HuggingFace: nvidia/Aegis-AI-... |
| 37 | 2025 | [[2025-Group-AILuminate]] | AILuminate v1.0 | AI system resistance to prompts eliciting... | Public (MLCommons) |
| 38 | 2025 | [[2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness]] | CARE | Cultural awareness of LLMs through multili... | Public (github.com/Guochry/CARE) |
| 39 | 2025 | [[2025-Helwe-Navigating the Political Compass Multilingual 50 Countries]] | Political Compass Test for LLMs (PCT... | Political and ideological biases in LLMs a... | Public (github.com/ChadiHelwe/navigat... |
| 40 | 2025 | [[2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models]] | JudiFair | Judicial fairness of LLMs across 65 labels... | Public toolkit available |
| 41 | 2025 | [[2025-Huang-BehaviorBench Multi-Tier Benchmark for Agent Behavior Editing]] | BEHAVIORBENCH | Ethical behavior of LLM-based agents; mora... | Public (github.com/baixianghuang/beha... |
| 42 | 2025 | [[2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors]] | DeceptionBench | Deceptive tendencies in LLMs across societ... | Public (github.com/Aries-iai/Deceptio... |
| 43 | 2025 | [[2025-Huang-On the Trustworthiness of Generative Foundation]] | TrustGen | Trustworthiness of generative foundation m... | Public (github.com/TrustGen/TrustEval... |
| 44 | 2025 | [[2025-Ji-PKU-SafeRLHF]] | PKU-SafeRLHF | Safety alignment in LLMs - helpfulness vs... | Public |
| 45 | 2025 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | EMNLP (Educator-role Moral and Normat... | Moral development stages, personality prof... | Public |
| 46 | 2025 | [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]] | Delphi / DelphiHYBRID | Machine moral judgment - ability to predic... | Public |
| 47 | 2025 | [[2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment]] | LLM Ethics Benchmark | Moral reasoning capabilities of LLMs acros... | Public |
| 48 | 2025 | [[2025-Jiao-LLM Ethics Benchmark]] | LLM Ethics Benchmark | Moral reasoning capabilities across founda... | Public |
| 49 | 2025 | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | SpeciesismBench | Speciesist bias in LLMs - recognition and... | Public |
| 50 | 2025 | [[2025-Jotautaitė-Speciesism in AI]] | SpeciesismBench | Speciesist bias and moral evaluation of no... | Public |
| 51 | 2025 | [[2025-Jourdan-FairTranslate]] | FairTranslate | Non-binary gender bias in machine translat... | Public |
| 52 | 2025 | [[2025-Kasu-EthicsMH]] | EthicsMH (Ethical Reasoning in Mental... | Ethical reasoning in mental health context... | Public |
| 53 | 2025 | [[2025-Khan-Randomness Not Representation The Unreliability of Evaluating]] | Unnamed (Cultural Alignment Robustnes... | Reliability of survey-based cultural align... | Public |
| 54 | 2025 | [[2025-Laukkonen-Contemplative Artificial Intelligence]] | Unnamed (Contemplative AI evaluation... | Ethical alignment improvement through cont... | Public |
| 55 | 2025 | [[2025-Leteno-Histoires Morales]] | Histoires Morales | Moral alignment of LLMs in French language... | Public |
| 56 | 2025 | [[2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese]] | LiveSecBench | Chinese LLM safety across five dimensions:... | Public |
| 57 | 2025 | [[2025-Li-MASK]] | MASK (Measuring AI System Knowledge o... | LLM honesty vs accuracy - whether models l... | Public |
| 58 | 2025 | [[2025-Li-SafetyAnalyst Interpretable Transparent and Steerable Safety]] | SafetyAnalyst | AI behavior safety through interpretable h... | Public |
| 59 | 2025 | [[2025-Li-SafetyAnalyst]] | SafetyAnalyst (duplicate entry) | AI behavior safety through interpretable h... | Code |
| 60 | 2025 | [[2025-Li-T2ISafety]] | T2ISafety | Safety of text-to-image models across toxi... | Public |
| | | *... 198 more* | | | |

---

## 10. Temporal Trends

### Growth Over Time

| Year | All Papers | Benchmarks | Benchmark % | Growth |
|------|-----------|-----------|-------------|--------|
| 2010 | 1 | 0 | 0% | - |
| 2015 | 1 | 0 | 0% | - |
| 2016 | 6 | 1 | 16% | - |
| 2018 | 13 | 7 | 53% | +6 |
| 2019 | 12 | 7 | 58% | 0 |
| 2020 | 21 | 11 | 52% | +4 |
| 2021 | 24 | 10 | 41% | -1 |
| 2022 | 45 | 26 | 57% | +16 |
| 2023 | 117 | 51 | 43% | +25 |
| 2024 | 284 | 160 | 56% | +109 |
| 2025 | 377 | 237 | 62% | +77 |
| 2026 | 23 | 18 | 78% | -219 |

---

## 11. Gap Analysis

### Ethical Tradition Coverage Gaps

| Tradition | Benchmark Coverage | Status |
|-----------|-------------------|--------|
| Consequentialism/Utilitarianism | 20 papers | Adequate |
| Deontological Ethics | 2 papers | Severe gap - Minimal coverage |
| Virtue Ethics (Western) | 2 papers | Severe gap - Minimal coverage |
| Care Ethics | 3 papers | Severe gap - Minimal coverage |
| Confucian Ethics | 2 papers | Severe gap - Minimal coverage |
| Islamic Ethics | 13 papers | Adequate |
| Hindu Ethics | 1 papers | Severe gap - Minimal coverage |
| Buddhist Ethics | 1 papers | Severe gap - Minimal coverage |
| Ubuntu Ethics | 0 papers | **CRITICAL GAP** - No benchmarks |
| Indigenous Traditions | 2 papers | Severe gap - Minimal coverage |

### Language Coverage Gaps

| Coverage Level | Languages |
|---------------|-----------|
| Strong (>30) | Chinese, English |
| Moderate (10-30) | None |
| Emerging (4-10) | Japanese, Arabic, Spanish, German, Hindi, Russian, French |
| Minimal (1-3) | Indonesian, Korean, Italian, Portuguese, Bengali, Swahili, Urdu, Dutch, Vietnamese |
| None (0) | Thai, Turkish |

### Methodology Gaps

| Gap Type | Methodologies |
|----------|--------------|
| Underrepresented (<20) | Embedding analysis (6), Likert/scale rating (15) |

### Key Structural Gaps

1. **Non-Western ethical traditions**: Ubuntu, Buddhist, and Indigenous ethical frameworks have zero benchmark coverage. Hindu and Islamic ethics have minimal representation.
2. **Language diversity**: Most benchmarks are English-only. African, Pacific Island, and most Indigenous languages are entirely unrepresented.
3. **Longitudinal evaluation**: No benchmarks measure moral reasoning evolution over training or deployment time.
4. **Compositional ethics**: Few benchmarks test complex, multi-stakeholder scenarios reflecting real deployment challenges.
5. **Process-based evaluation**: Almost all benchmarks evaluate outcomes (right/wrong answers), not reasoning quality.
6. **Environmental and animal ethics**: Virtually no benchmarks address ecological or animal welfare reasoning.

---

## 12. Recommendations for Values Alignment Research

### Tier 1: Start Here (Immediate Use)

*Top public benchmarks for rapid SOTA LLM evaluation, prioritized by recency + breadth:*

| # | Benchmark | Paper | What It Measures | Models Tested |
|---|-----------|-------|-----------------|---------------|
| 1 | HarmEval | [[2025-Banerjee-SafeInfer]] | LLM safety: potential misuse scenarios ali... | Llama2-7b-chat, Mistral-7B-Instruct,... |
| 2 | Unnamed (MFT-based LLM moral eva... | [[2025-Bulla-Large Language Models meet moral values]] | LLM ability to detect and classify moral v... | GPT-4, GPT-3.5, Llama-70B, Mixtral-8x... |
| 3 | CulturalBench | [[2025-Chiu-CulturalBench]] | LLM cultural knowledge across 45 global re... | Multiple frontier LMs including GPT-4... |
| 4 | FairMT-Bench | [[2025-Fan-FAIRMT-BENCH]] | Fairness in LLMs during multi-turn dialogu... | 15 SOTA LLMs including GPT-4, Claude,... |
| 5 | AMAeval (Artificial Moral Assist... | [[2025-Galatolo-Beyond Ethical Alignment AMAs]] | LLM capabilities as Artificial Moral Assis... | Multiple open-source LLMs including Q... |
| 6 | SpeciesismBench | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | Speciesist bias in LLMs - recognition and... | 17 LLMs across six model families (Op... |
| 7 | SpeciesismBench | [[2025-Jotautaitė-Speciesism in AI]] | Speciesist bias and moral evaluation of no... | 17 LLMs across six families (OpenAI,... |
| 8 | FairTranslate | [[2025-Jourdan-FairTranslate]] | Non-binary gender bias in machine translat... | Gemma2-2B, Mistral-7B, Llama3.1-8B, L... |
| 9 | SafetyAnalyst | [[2025-Li-SafetyAnalyst Interpretable Transparent and Steerable Safety]] | AI behavior safety through interpretable h... | Frontier LLMs (GPT-4, Claude, etc.) u... |
| 10 | CQ-Bench (duplicate entry) | [[2025-Liu-Can LLMs Grasp Implicit Cultural Values]] | LLMs' metacognitive cultural intelligence... | o1, Deepseek-R1, GPT-4o-mini, o3-mini... |
| 11 | EthicsSuite | [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] | Behavioral inconsistency in LLM ethics-rel... | 8 LLMs including GPT-4, Claude, ChatG... |
| 12 | Cultural Moral Judgment Evaluati... | [[2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language]] | Whether LLMs mirror cultural variations in... | GPT-2, OPT, BLOOMZ, Qwen, GPT-4o, GPT... |

### Tier 2: Comprehensive Evaluation

*For thorough values alignment assessment, combine benchmarks across these dimensions:*

| Dimension | Recommended Categories | Paper Count |
|-----------|----------------------|-------------|
| Moral Reasoning & Ethical Judgment | Category 1 | 268 |
| Value Alignment & Value Pluralism | Category 2 | 150 |
| Cultural & Cross-Cultural Ethics | Category 3 | 193 |
| Fairness, Bias & Social Norms | Category 4 | 233 |
| Toxicity, Hate Speech & Harmful Content | Category 5 | 94 |
| Safety & Red Teaming | Category 6 | 181 |
| Domain-Specific Ethics | Category 7 | 117 |
| Normative Ethics Benchmarks | Category 8 | 65 |
| Moral Psychology Applied to AI | Category 9 | 62 |
| Helpfulness, Honesty & RLHF | Category 10 | 299 |

### Tier 3: Research Frontiers

*Underserved areas where new benchmark development is most needed:*

1. **Cross-cultural normative ethics**: Benchmarks grounding ethical evaluation in Confucian, Islamic, Buddhist, Ubuntu, and Indigenous frameworks
2. **Pluralistic value aggregation**: How should LLMs handle genuinely contested moral questions where reasonable people disagree?
3. **Dynamic moral reasoning**: Evaluating consistency and evolution of moral reasoning across conversational contexts
4. **Applied professional ethics**: Domain-specific evaluation in healthcare, law, engineering, and education beyond simple knowledge testing
5. **Multilingual fairness**: Bias and fairness evaluation in low-resource languages
6. **Relational and care ethics**: Evaluation of LLM behavior in caregiving, counseling, and interpersonal support contexts
7. **Environmental ethics reasoning**: Sustainability, ecological justice, and intergenerational equity in AI decision-making

---

## 13. Methodology

### Data Sources

| Source | Records | Description |
|--------|---------|-------------|
| `benchmark_survey_all_classifications.json` | 924 | 20-agent deep-read of all vault papers |
| `benchmark_survey_candidates.json` | 528 | Subset with benchmark/evaluation resources |
| `normative_v2_all_classifications.json` | 266 | 10-agent normative ethics classification (EXSR batch) |
| `author_paper_map.json` | 846 | Author-paper mapping |

### Classification Approach

- **Benchmark identification**: 20-agent parallel deep-read with structured extraction rubric
- **Category assignment**: Keyword-based classification across 10 categories (from `generate_benchmark_survey_report.py`)
- **Model family extraction**: Regex normalization mapping 70+ model name variants to ~27 canonical families
- **Methodology extraction**: Regex normalization mapping methodology descriptions to 14 canonical types
- **Cultural/language detection**: Pattern matching for 10 ethical traditions and 20 languages

### Normalization Coverage

- **Model recognition**: 196/528 candidates (37%) have ≥1 recognized model family
- **Methodology recognition**: 449/528 candidates (85%) have ≥1 recognized methodology type

### Limitations

- **Keyword-based classification** may miss nuanced thematic connections or create false positives
- **Coverage bias**: Vault overrepresents English-language, computationally-oriented, Western-authored papers
- **Temporal bias**: 2023-2025 papers are overrepresented due to rapid LLM safety/ethics growth
- **Free-text normalization**: Model and methodology extraction depends on how the 20 agents described each paper
- **No YAML modification**: This report is read-only analysis; no paper metadata was changed

---

## Appendix A: Full Benchmark Candidate List

*528 benchmark candidates, sorted by year (most recent first):*

| # | Year | Paper | Benchmark | Pluralistic | Availability |
|---|------|-------|-----------|-------------|--------------|
| 1 | 2026 | [[2026-Dang-RedBench]] | RedBench | No | Public |
| 2 | 2026 | [[2026-Elkins-Negation Sensitivity Index NSI]] | Negation Sensitivity Index (NSI) | No | Not stated |
| 3 | 2026 | [[2026-Farid-One Model Many Morals Uncovering Cross-Linguistic Misalignments in]] | Cross-Linguistic Moral Reasoning Evaluation | Yes | Not stated |
| 4 | 2026 | [[2026-Goel-Building Interpretable Models for Moral Decision-Making]] | Interpretable Moral Machine Transformer | Partial | Public |
| 5 | 2026 | [[2026-Guey-BiasLab Multilingual Dual-Framing Framework]] | BiasLab | Yes | Public |
| 6 | 2026 | [[2026-He-GVS-Scale and GVS-Bench GenAI Value Safety Scale]] | GVS-Scale / GVS-Bench | Yes | Public |
| 7 | 2026 | [[2026-Huang-Knowing But Not Doing Convergent Morality and Divergent Action in]] | ValAct-15K | Yes | Not stated |
| 8 | 2026 | [[2026-Jin-MedES Chinese Medical Ethics Scenarios]] | MedES | Partial | Public |
| 9 | 2026 | [[2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks]] | Theory Trace Card (TTC) | Partial | Public |
| 10 | 2026 | [[2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in]] | VALUEFLOW / VIDB / HIVES | Yes | Not stated |
| 11 | 2026 | [[2026-Lee-BiasJailbreak]] | BiasJailbreak | Partial | Public |
| 12 | 2026 | [[2026-Li-PluriHarms]] | PluriHarms | Yes | Not stated |
| 13 | 2026 | [[2026-Liu-JMedEthicBench]] | JMedEthicBench | Partial | Not stated |
| 14 | 2026 | [[2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs]] | DIB Benchmark (Decision-based Implicit Bias) | Partial | Not stated |
| 15 | 2026 | [[2026-Shen-PsychEthicsBench]] | PsychEthicsBench | Partial | Public |
| 16 | 2026 | [[2026-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence]] | Multi-Dimensional Moral Competence Assessment | Partial | Not stated |
| 17 | 2026 | [[2026-Yu-Tracing Moral Foundations in LLMs]] | Moral Foundations Theory Interpretability Analysis | Partial | Not stated |
| 18 | 2026 | [[2026-Yun-VAPT Value-Alignment Perception Toolkit]] | VAPT (Value-Alignment Perception Toolkit) | Yes | Not stated |
| 19 | 2025 | [[2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in]] | Unnamed (WVS-based cultural value adaptation ev... | Yes | Public |
| 20 | 2025 | [[2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment]] | Unnamed (cultural alignment evaluation methodol... | Yes | Not stated |
| 21 | 2025 | [[2025-Akata-Playing Repeated Games with Large Language Models]] | Unnamed (behavioral game theory evaluation for... | No | Not stated |
| 22 | 2025 | [[2025-Aleid-Hajj-FQA - Benchmark Arabic Dataset for Hajj Fatwa QA]] | Hajj-FQA | Partial | Not stated |
| 23 | 2025 | [[2025-Aleid-Hajj-FQA]] | Hajj-FQA | Partial | Not stated |
| 24 | 2025 | [[2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic]] | AraTrust | Partial | Public |
| 25 | 2025 | [[2025-Alhassoun-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi]] | Saudi-Alignment Benchmark | Yes | Not stated |
| 26 | 2025 | [[2025-Ali-Data Curation for Pluralistic Alignment]] | Unnamed (pluralistic alignment dataset) | Yes | Not stated |
| 27 | 2025 | [[2025-Alwajih-Palm]] | PALM | Yes | Public |
| 28 | 2025 | [[2025-Alwajih-PalmX 2025 - First Shared Task on Benchmarking LLMs on Arabic and]] | PalmX 2025 | Yes | Not stated |
| 29 | 2025 | [[2025-An-MoralReason]] | Moral-Reason-QA | Yes | Not stated |
| 30 | 2025 | [[2025-Andric-Do LLMs Walk Their Talk Multi-Method Moral Evaluation Framework]] | Unnamed (LLM-IAT, Forced Binary Choice, LLM-ASA... | No | Not stated |
| 31 | 2025 | [[2025-Andriushchenko-AgentHarm]] | AgentHarm | No | Public |
| 32 | 2025 | [[2025-Anonymous-BEATS]] | BEATS | Partial | Not stated |
| 33 | 2025 | [[2025-Ashkinaze-Deep Value Benchmark]] | Deep Value Benchmark (DVB) | No | Public |
| 34 | 2025 | [[2025-Rahman-CCD-Bench Probing Cultural Conflict in LLM Decision-Making]] | CCD-Bench | Yes | Public |
| 35 | 2025 | [[2025-Backmann-When Ethics and Payoffs Diverge LLM Agents in Morally Charged Social]] | MORALSIM | No | Public |
| 36 | 2025 | [[2025-Backmann-When Ethics and Payoffs Diverge]] | MORALSIM | No | Public |
| 37 | 2025 | [[2025-Bae-CharMoral]] | CharMoral | No | Public |
| 38 | 2025 | [[2025-Banerjee-SafeInfer]] | HarmEval | No | Public |
| 39 | 2025 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Unnamed (multilingual moral LLM evaluation) | Yes | Not stated |
| 40 | 2025 | [[2025-Becker-The Moralization Corpus]] | Moralization Corpus | Partial | Public |
| 41 | 2025 | [[2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030]] | Healthcare Ethics & Safety QA Benchmark | Partial | Not stated |
| 42 | 2025 | [[2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for]] | Unnamed (Islamic Moral QA dataset) | Yes | Not stated |
| 43 | 2025 | [[2025-Bouchard-How to Assess Your LLM Use Case for Bias and]] | LangFair | Partial | Public |
| 44 | 2025 | [[2025-Bouchekif-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and]] | QIAS 2025 | Yes | Public |
| 45 | 2025 | [[2025-Bulla-Large Language Models meet moral values]] | Unnamed (MFT-based LLM moral evaluation) | Partial | Public |
| 46 | 2025 | [[2025-Buyl-AI Alignment at Your Discretion]] | Unnamed (Alignment Discretion Metrics) | Yes | Not stated |
| 47 | 2025 | [[2025-Cao-SafeDialBench]] | SafeDialBench | Partial | Not stated |
| 48 | 2025 | [[2025-Capraro-Large Language Models Show Amplified Cognitive Biases in Moral]] | Unnamed (Moral dilemmas for cognitive bias eval... | No | Not stated |
| 49 | 2025 | [[2025-Castricato-PERSONA Pluralistic Alignment Testbed]] | PERSONA / PERSONA Bench | Yes | Public |
| 50 | 2025 | [[2025-Chakraborty-Structured Moral Reasoning]] | Unnamed (Value-Grounded Moral Reasoning Evaluat... | Yes | Not stated |
| 51 | 2025 | [[2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values]] | MoVa | Yes | Public |
| 52 | 2025 | [[2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment]] | SPICA | Yes | Public |
| 53 | 2025 | [[2025-Cheng-ELEPHANT Social Sycophancy]] | ELEPHANT | Partial | Public |
| 54 | 2025 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | Unnamed (22 moral dilemmas) | No | Not stated |
| 55 | 2025 | [[2025-Chiu-CulturalBench]] | CulturalBench | Yes | Public |
| 56 | 2025 | [[2025-Chiu-MoReBench]] | MoReBench / MoReBench-Theory | Yes | Public |
| 57 | 2025 | [[2025-Chiu-Will AI Tell Lies to Save Sick Children]] | LITMUSVALUES / AIRISKDILEMMAS | Partial | Public |
| 58 | 2025 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | TRIAL / ERR | No | Not stated |
| 59 | 2025 | [[2025-Chua-RabakBench]] | RabakBench | Yes | Public |
| 60 | 2025 | [[2025-Coleman-The Convergent Ethics of AI Analyzing Moral Foundation Priorities in]] | PRIME (Priorities in Reasoning and Intrinsic Mo... | Yes | Not stated |
| 61 | 2025 | [[2025-Dickerson-Who Gets the Kidney]] | Unnamed (Kidney allocation moral evaluation) | No | Not stated |
| 62 | 2025 | [[2025-Dillion-AI Language Model Rivals Expert Ethicist in Perceived Moral Expertise]] | Unnamed (Moral Turing Test / Comparative MTT) | No | Not stated |
| 63 | 2025 | [[2025-Dillion-AI Language Model Rivals Expert Ethicist]] | Unnamed (Moral Turing Test / Comparative MTT) | No | Not stated |
| 64 | 2025 | [[2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value]] | AdAEM | Yes | Not stated |
| 65 | 2025 | [[2025-Dwivedi-EtiCor++ Towards Understanding Etiquettical Bias in LLMs]] | EtiCor++ | Yes | Not stated |
| 66 | 2025 | [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] | Unnamed (Medical Ethics Evaluation Corpus) | Partial | Not stated |
| 67 | 2025 | [[2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical]] | SFF (Syntactic Framing Fragility) | Partial | Code available |
| 68 | 2025 | [[2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al.]] | RMP (Reward Model Perspectives) | Yes | Code available |
| 69 | 2025 | [[2025-Fan-FAIRMT-BENCH]] | FairMT-Bench | Partial | Public |
| 70 | 2025 | [[2025-Farid-One Model, Many Morals]] | Unnamed (Multilingual Moral Reasoning Evaluation) | Yes | Not stated |
| 71 | 2025 | [[2025-Fenech-Borg-The Cultural Gene of Large Language Models]] | CPD (Cultural Probe Dataset) | Yes | Not stated |
| 72 | 2025 | [[2025-Flores-BenchMoral]] | BenchMoral | Yes | Not stated |
| 73 | 2025 | [[2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the]] | Unnamed (Iterated Prisoner's Dilemma for LLMs) | No | Not stated |
| 74 | 2025 | [[2025-Gai-MoralBench A Multi-Faceted Benchmark Gai et al.]] | MoralBench | Partial | Public |
| 75 | 2025 | [[2025-Galatolo-Beyond Ethical Alignment AMAs]] | AMAeval (Artificial Moral Assistant Evaluation) | Partial | Code available |
| 76 | 2025 | [[2025-Gao-MIST Moral Inference through Storytelling with Text and Images]] | MIST (Moral Inference through Storytelling with... | No | Not stated |
| 77 | 2025 | [[2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value]] | EVALUESTEER | Yes | Not stated |
| 78 | 2025 | [[2025-Ghosh-AEGIS 2.0]] | AEGIS 2.0 | No | Public |
| 79 | 2025 | [[2025-Group-AILuminate]] | AILuminate v1.0 | Partial | Public |
| 80 | 2025 | [[2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness]] | CARE | Yes | Public |
| 81 | 2025 | [[2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment]] | VAL-Bench | Partial | Not stated |
| 82 | 2025 | [[2025-Han-Value Portrait]] | Value Portrait | Yes | Not stated |
| 83 | 2025 | [[2025-Hatemo-Revisiting the Trolley Problem for AI]] | Unnamed (Trolley Problem Evaluation for LLMs) | Partial | Not stated |
| 84 | 2025 | [[2025-Helwe-Navigating the Political Compass Multilingual 50 Countries]] | Political Compass Test for LLMs (PCT + 8 Values) | Yes | Public |
| 85 | 2025 | [[2025-Herrador-The PacifAIst Benchmark]] | PacifAIst | No | Not stated |
| 86 | 2025 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | FAI Benchmark (Flourishing AI Benchmark) | Yes | Not stated |
| 87 | 2025 | [[2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset]] | NormGenesis | Yes | Not stated |
| 88 | 2025 | [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | PrinciplismQA | Partial | Not stated |
| 89 | 2025 | [[2025-Hossain-BRAND Bilingual Religious Accountable Norm Dataset]] | BRAND (Bilingual Religious Accountable Norm Dat... | Yes | Not stated |
| 90 | 2025 | [[2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models]] | JudiFair | Partial | Public |
| 91 | 2025 | [[2025-Huang-BehaviorBench Multi-Tier Benchmark for Agent Behavior Editing]] | BEHAVIORBENCH | Partial | Public |
| 92 | 2025 | [[2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors]] | DeceptionBench | No | Public |
| 93 | 2025 | [[2025-Huang-On the Trustworthiness of Generative Foundation]] | TrustGen | Partial | Public |
| 94 | 2025 | [[2025-Huang-Values in the Wild Discovering and Analyzing Values in Real AI]] | Values in the Wild | Partial | Not stated |
| 95 | 2025 | [[2025-Hui-Decoding Moral Responses in AI]] | Unnamed | Partial | Not stated |
| 96 | 2025 | [[2025-Iftikhar-How LLM Counselors Violate Ethical Standards in Mental Health Practice]] | Unnamed (Ethical Violation Framework for LLM Co... | Partial | Not stated |
| 97 | 2025 | [[2025-Jamshidi-MoCoP]] | MoCoP (Moral Consistency Pipeline) | No | Not stated |
| 98 | 2025 | [[2025-Jamshidi-The Moral Consistency Pipeline MoCoP]] | MoCoP (Moral Consistency Pipeline) | No | Not stated |
| 99 | 2025 | [[2025-Ji-PKU-SafeRLHF]] | PKU-SafeRLHF | No | Public |
| 100 | 2025 | [[2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling]] | EMNLP (Educator-role Moral and Normative LLMs P... | No | Public |
| 101 | 2025 | [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]] | Delphi / DelphiHYBRID | Partial | Public |
| 102 | 2025 | [[2025-Jiang-Raising the Bar]] | GETA (Generative Evolving Testing Approach) | No | Not stated |
| 103 | 2025 | [[2025-Jiao-LLM Ethics Benchmark Three-Dimensional Assessment]] | LLM Ethics Benchmark | Yes | Public |
| 104 | 2025 | [[2025-Jiao-LLM Ethics Benchmark]] | LLM Ethics Benchmark | Yes | Public |
| 105 | 2025 | [[2025-Jin-MedEthicEval]] | MedEthicEval | Partial | Not stated |
| 106 | 2025 | [[2025-Jotautaite-From Stability to Inconsistency]] | MFD-LLM (Moral Foundations LLM Dataset) | Partial | Not stated |
| 107 | 2025 | [[2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements]] | SpeciesismBench | Yes | Public |
| 108 | 2025 | [[2025-Jotautaitė-Speciesism in AI]] | SpeciesismBench | Yes | Public |
| 109 | 2025 | [[2025-Jourdan-FairTranslate]] | FairTranslate | Partial | Public |
| 110 | 2025 | [[2025-Ju-NaVAB]] | NaVAB (National Value Alignment Benchmark) | Yes | Not stated |
| 111 | 2025 | [[2025-Jung-FLEX]] | FLEX (Fairness Benchmark in LLM under Extreme S... | No | Not stated |
| 112 | 2025 | [[2025-Kasu-EthicsMH]] | EthicsMH (Ethical Reasoning in Mental Health) | Partial | Public |
| 113 | 2025 | [[2025-Keshmirian-Many LLMs Are More Utilitarian Than One]] | Unnamed | Partial | Not stated |
| 114 | 2025 | [[2025-Khan-Randomness Not Representation The Unreliability of Evaluating]] | Unnamed (Cultural Alignment Robustness Evaluation) | Yes | Public |
| 115 | 2025 | [[2025-Ki-Multiple LLM Agents Debate for Equitable Cultural]] | NormAd-ETI | Yes | Not stated |
| 116 | 2025 | [[2025-Ki-NormAd-ETI Multiple LLM Agents Debate for Equitable Cultural Alignment]] | NormAd-ETI | Yes | Not stated |
| 117 | 2025 | [[2025-Kilov-Discerning What Matters Multi-Dimensional Moral Competence Assessment]] | Unnamed (Multi-Dimensional Moral Competence Ass... | No | Not stated |
| 118 | 2025 | [[2025-Kilov-Discerning What Matters]] | Unnamed (Multi-Dimensional Moral Competence Ass... | No | Not stated |
| 119 | 2025 | [[2025-Kneer-Hard Problem AI Alignment Value Forks]] | Unnamed | Partial | Not stated |
| 120 | 2025 | [[2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language]] | D-REX (Deceptive Reasoning Exposure Suite) | No | Not stated |
| 121 | 2025 | [[2025-Kumar-Are Rules Meant to be Broken]] | UniMoral | Yes | Not stated |
| 122 | 2025 | [[2025-Kumar-UniMoral ACL 2025 Best Resource Paper]] | UniMoral | Yes | Not stated |
| 123 | 2025 | [[2025-Lan-McBE]] | McBE (Multi-task Chinese Bias Evaluation Benchm... | Yes | Not stated |
| 124 | 2025 | [[2025-Laukkonen-Contemplative Artificial Intelligence]] | Unnamed (Contemplative AI evaluation using AILu... | Partial | Public |
| 125 | 2025 | [[2025-Le Jeune-Phare A Safety Probe for Large Language Models]] | Phare | Partial | Not stated |
| 126 | 2025 | [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]] | CLASH (Character perspective-based LLM Assessme... | Yes | Not stated |
| 127 | 2025 | [[2025-Lee-When Prompting Fails to Sway]] | Role-Play-at-Scale (Moral Foundations Questionn... | Partial | Not stated |
| 128 | 2025 | [[2025-Leteno-Histoires Morales]] | Histoires Morales | Yes | Public |
| 129 | 2025 | [[2025-Li-Analyzing Cognitive Differences Among Large]] | Social Worldview Taxonomy (SWT) | Yes | Not stated |
| 130 | 2025 | [[2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese]] | LiveSecBench | Partial | Public |
| 131 | 2025 | [[2025-Li-MASK]] | MASK (Measuring AI System Knowledge of Honesty) | No | Public |
| 132 | 2025 | [[2025-Li-SafetyAnalyst Interpretable Transparent and Steerable Safety]] | SafetyAnalyst | Partial | Public |
| 133 | 2025 | [[2025-Li-SafetyAnalyst]] | SafetyAnalyst (duplicate entry) | Partial | Code available |
| 134 | 2025 | [[2025-Li-T2ISafety]] | T2ISafety | Partial | Public |
| 135 | 2025 | [[2025-Lin-MORALISE]] | MORALISE | Partial | Public |
| 136 | 2025 | [[2025-Liu-Can LLMs Grasp Implicit Cultural Values]] | CQ-Bench (duplicate entry) | Yes | Public |
| 137 | 2025 | [[2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]] | ConflictScope | Yes | Not stated |
| 138 | 2025 | [[2025-Liu-CQ-Bench Cultural Intelligence Benchmark for LLMs]] | CQ-Bench (Cultural Intelligence Benchmark) | Yes | Public |
| 139 | 2025 | [[2025-Liu-Cross-cultural value alignment frameworks]] | Multi-Layered Auditing Platform for Responsible... | Yes | Not stated |
| 140 | 2025 | [[2025-Liu-Diagnosing Moral Reasoning Acquisition in Language Models Pragmatics]] | Moral Reasoning Diagnosis Framework (Pragmatic... | No | Not stated |
| 141 | 2025 | [[2025-Liu-Diagnosing Moral Reasoning Acquisition in]] | Moral Reasoning Diagnosis Framework (duplicate... | No | Not stated |
| 142 | 2025 | [[2025-Liu-InstrumentalEval]] | InstrumentalEval | No | Not stated |
| 143 | 2025 | [[2025-Liu-On the Convergence of Moral Self-Correction in LLMs]] | Moral Self-Correction Convergence Evaluation | No | Not stated |
| 144 | 2025 | [[2025-Liu-PersuSafety LLM Can be a Dangerous Persuader]] | PersuSafety | No | Code available |
| 145 | 2025 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | Homo Moralis Alignment Pipeline (Kantian Prefer... | Partial | Not stated |
| 146 | 2025 | [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]] | EthicsSuite | No | Public |
| 147 | 2025 | [[2025-Machlovi-GuardEval]] | GuardEval | Partial | Public |
| 148 | 2025 | [[2025-Mahajan-Mapping Moral Reasoning in LLMs A Multi-Dimensional Analysis of]] | Moral Reasoning Profiling Methodology (Safety P... | Yes | Not stated |
| 149 | 2025 | [[2025-Mahajan-Mapping Moral Reasoning in LLMs]] | Moral Reasoning Profiling Methodology (duplicat... | Yes | Not stated |
| 150 | 2025 | [[2025-Malaysia-Islam Q&A Morals Corpus]] | Islam Q&A Morals Corpus (Volume 13) | Yes | Not stated |
| 151 | 2025 | [[2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs]] | MORABLES | Partial | Not stated |
| 152 | 2025 | [[2025-Mazeika-Utility Engineering]] | Utility Engineering Framework | Yes | Not stated |
| 153 | 2025 | [[2025-Mehta-Understanding Gen Alpha's Digital Language Evaluation of LLM Safety]] | Gen Alpha Digital Language Safety Framework | Partial | Not stated |
| 154 | 2025 | [[2025-Menke-How Effective Is Constitutional AI in Small LLMs]] | Constitutional AI Self-Critique Evaluation (usi... | No | Not stated |
| 155 | 2025 | [[2025-Mitchell-SHADES]] | SHADES | Yes | Public |
| 156 | 2025 | [[2025-Mohammadi-EvalMORAAL]] | EvalMORAAL | Yes | Not stated |
| 157 | 2025 | [[2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language]] | Cultural Moral Judgment Evaluation (WVS/PEW-based) | Yes | Code available |
| 158 | 2025 | [[2025-Mohammed-Aftina - Enhancing Stability in AI-Based Islamic Fatwa Generation]] | Aftina (Arabic Fatwa QA Benchmark) | Yes | Not stated |
| 159 | 2025 | [[2025-Mohammed-Aftina]] | Aftina (duplicate entry) | Yes | Not stated |
| 160 | 2025 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | COMETH (Contextual Organization of Moral Evalua... | Partial | Not stated |
| 161 | 2025 | [[2025-Mubarak-IslamicEval 2025 - Shared Task on Capturing LLM Hallucination in]] | IslamicEval 2025 Shared Task | Yes | Not stated |
| 162 | 2025 | [[2025-Mushtaq-WorldView-Bench]] | WorldView-Bench | Yes | Not stated |
| 163 | 2025 | [[2025-Myung-PapersPlease]] | PapersPlease | Partial | Public |
| 164 | 2025 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | 30-Dilemma Ethical Evaluation Framework | Partial | Not stated |
| 165 | 2025 | [[2025-Naik-AgentMisalignment]] | AgentMisalignment | No | Not stated |
| 166 | 2025 | [[2025-Nair-Do Language Models Think Consistently]] | Value Preference Consistency Evaluation | Partial | Public |
| 167 | 2025 | [[2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in]] | Japanese Stereotype-Triggering Prompt Dataset | Yes | Not stated |
| 168 | 2025 | [[2025-Narnaware-SB-Bench]] | SB-Bench (Stereotype Bias Benchmark) / BBQ-V | Partial | Public |
| 169 | 2025 | [[2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts]] | INDIC-BIAS | Yes | Public |
| 170 | 2025 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | LLM Ethical Logic Assessment Battery | Partial | Not stated |
| 171 | 2025 | [[2025-Neuman-Auditing the Ethical Logic of Generative AI Models]] | Five-Dimensional Ethical Audit Model | Partial | Not stated |
| 172 | 2025 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | PRIME (Priorities in Reasoning and Intrinsic Mo... | Yes | Not stated |
| 173 | 2025 | [[2025-Nunes-Evidence of conceptual mastery in the application]] | Rule Application Mastery / Diversity of Thought... | No | Not stated |
| 174 | 2025 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | Moral Machine prompt variation evaluation | Partial | Not stated |
| 175 | 2025 | [[2025-Pandey-SocialHarmBench]] | SocialHarmBench | Yes | Public |
| 176 | 2025 | [[2025-Park-Deontological Keyword Bias]] | DKB (Deontological Keyword Bias) Benchmark | No | Not stated |
| 177 | 2025 | [[2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs]] | OvertonScore | Yes | Not stated |
| 178 | 2025 | [[2025-Pourbahman-ELAB]] | ELAB (Extensive LLM Alignment Benchmark) | Yes | Public |
| 179 | 2025 | [[2025-Priya-Deontic Temporal Logic for AI Ethics]] | Deontic Temporal Logic Verification Framework | No | Not stated |
| 180 | 2025 | [[2025-Rao-NormAd]] | NormAd / NormAd-Eti | Yes | Not stated |
| 181 | 2025 | [[2025-Rastogi-DIVE Dataset for Pluralistic Alignment of Text-to-Image Models]] | DIVE (Diverse Intersectional Visual Evaluation) | Yes | Not stated |
| 182 | 2025 | [[2025-Ravindran-Moral Anchor System A Predictive Framework for AI Value Alignment and]] | Moral Anchor System (MAS) | No | Public |
| 183 | 2025 | [[2025-Raza-HumaniBench]] | HumaniBench | Partial | Public |
| 184 | 2025 | [[2025-Ren-MASK Benchmark Disentangling Honesty From Accuracy in AI Systems]] | MASK | No | Public |
| 185 | 2025 | [[2025-Rismani-Measuring What Matters Connecting AI Ethics Evaluations to System]] | RAI Measures Dataset | Partial | Not stated |
| 186 | 2025 | [[2025-Rozen-Do LLMs Have Consistent Values]] | Value Anchoring / LLM Value Consistency Evaluation | Yes | Not stated |
| 187 | 2025 | [[2025-Ruiz-Fernández-EsBBQ and CaBBQ]] | EsBBQ and CaBBQ (Spanish and Catalan BBQ) | Yes | Not stated |
| 188 | 2025 | [[2025-Russo-The Pluralistic Moral Gap]] | Moral Dilemma Dataset + Dynamic Moral Profiling... | Yes | Not stated |
| 189 | 2025 | [[2025-Sachdeva-Deliberative Dynamics and Value Alignment]] | LLM Debate Moral Deliberation Framework | Partial | Not stated |
| 190 | 2025 | [[2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas]] | AITA Moral Dilemmas Evaluation | Partial | Public |
| 191 | 2025 | [[2025-Saffari-Can I introduce my boyfriend to my grandmother]] | ISN (Iranian Social Norms) | Yes | Public |
| 192 | 2025 | [[2025-Sameer-Insights into Moral Reasoning of AI]] | MCT + MFQ for LLM Evaluation | Partial | Not stated |
| 193 | 2025 | [[2025-Samway-Are Language Models Consequentialist or Deontological]] | MORALLENS | Partial | Public |
| 194 | 2025 | [[2025-Santhosh-IndiCASA - Dataset and Bias Evaluation Framework for LLMs in Indian]] | IndiCASA | Yes | Public |
| 195 | 2025 | [[2025-Schacht-Mapping Moral Reasoning Circuits]] | Moral Reasoning Circuits Dataset | Partial | Public |
| 196 | 2025 | [[2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion]] | Asian Cultural Alignment Audit | Yes | Not stated |
| 197 | 2025 | [[2025-Shen-ValueActionLens Mind the Value-Action Gap]] | ValueActionLens | Yes | Public |
| 198 | 2025 | [[2025-Shen-ValueCompass A Framework for Measuring Contextual Value Alignment]] | ValueCompass | Yes | Public |
| 199 | 2025 | [[2025-Shetty-VITAL Pluralistic Alignment in Healthcare]] | VITAL | Yes | Public |
| 200 | 2025 | [[2025-Shetty-VITAL]] | VITAL | Yes | Public |
| 201 | 2025 | [[2025-Shin-RoleConflictBench A Benchmark of Role Conflict Scenarios for]] | RoleConflictBench | Yes | Public |
| 202 | 2025 | [[2025-Simhi-ManagerBench Evaluating Safety-Pragmatism Trade-off in Managerial]] | ManagerBench | No | Public |
| 203 | 2025 | [[2025-Snoswell-Beyond Verdicts LLM Moral Competence]] | LLM Moral Competence Taxonomy (survey-based) | Partial | Public |
| 204 | 2025 | [[2025-Sorensen-Operationalizing Pluralistic Values]] | Pluralistic Values Alignment Study | Yes | Public |
| 205 | 2025 | [[2025-Sorensen-Value Profiles for Encoding Human Variation]] | Value Profiles Methodology | Yes | Not stated |
| 206 | 2025 | [[2025-Su-Understanding How Value Neurons Shape the]] | ValueInsight / ValueLocate | Yes | Not stated |
| 207 | 2025 | [[2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM]] | Cultural Value Alignment Evaluation (VSM-based) | Yes | Not stated |
| 208 | 2025 | [[2025-Sun-CASE-Bench Context-Aware SafEty Benchmark]] | CASE-Bench | Partial | Public |
| 209 | 2025 | [[2025-Sun-CASE-Bench]] | CASE-Bench | Partial | Public |
| 210 | 2025 | [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]] | Moral Dilemma Response Analysis (SOCIALSENSE-re... | Partial | Not stated |
| 211 | 2025 | [[2025-Takeshita-JETHICS - Japanese Ethics Understanding Evaluation Dataset]] | JETHICS | Yes | Public |
| 212 | 2025 | [[2025-Takeshita-JETHICS]] | JETHICS | Yes | Public |
| 213 | 2025 | [[2025-Tennant-Moral Alignment for LLM Agents Intrinsic Rewards]] | Moral Alignment via Intrinsic Rewards (IPD-based) | Partial | Public |
| 214 | 2025 | [[2025-Tennant-Moral Alignment for LLM Agents]] | Moral Alignment IPD Framework | Yes | Code available |
| 215 | 2025 | [[2025-Tennant-Moral Intrinsic Rewards for Alignment]] | Moral Intrinsic Rewards (IPD) | Yes | Not stated |
| 216 | 2025 | [[2025-Tereshchenko-A Comparative Analysis of Ethical and Safety Gaps]] | Relative Danger Coefficient (RDC) | No | Not stated |
| 217 | 2025 | [[2025-Trager-MFTCXplain A Multilingual Benchmark Dataset for Evaluating the Moral]] | MFTCXplain | Yes | Public |
| 218 | 2025 | [[2025-Trager-MFTCXplain]] | MFTCXplain | Yes | Public |
| 219 | 2025 | [[2025-Tsvetkov-Democracy-in-Silico Institutional Design as Alignment]] | Democracy-in-Silico / Power-Preservation Index... | Partial | Not stated |
| 220 | 2025 | [[2025-Varimaldi-VideoNorms Benchmarking Cultural Awareness of Video Language Models]] | VideoNorms | Yes | Not stated |
| 221 | 2025 | [[2025-Zhang-AISafetyLab]] | AISafetyLab | No | Public |
| 222 | 2025 | [[2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning]] | Ethical Reasoning Paradigm (evaluated on SafeWo... | Yes | Not stated |
| 223 | 2025 | [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] | DiffAware Benchmark Suite | Partial | Public |
| 224 | 2025 | [[2025-Wang-Multimodal Understanding of Human Values in Videos]] | TikTok Values Dataset | Partial | Public |
| 225 | 2025 | [[2025-Wei-MedEthicsQA A Comprehensive Question Answering Benchmark for Medical]] | MedEthicsQA | Partial | Public |
| 226 | 2025 | [[2025-Wei-MedEthicsQA]] | MedEthicsQA | Partial | Public |
| 227 | 2025 | [[2025-Wen-Evaluating Implicit Bias in Large Language Models]] | BUMBLE (Bias Understanding Measurement Benchmar... | No | Public |
| 228 | 2025 | [[2025-Willis-Will Systems of LLM Agents Cooperate An Investigation into a Social]] | LLM Agent Cooperation (IPD Evolutionary Simulat... | Partial | Code available |
| 229 | 2025 | [[2025-Wu-C-VARC Chinese Value Rule Corpus]] | C-VARC (Chinese Value Rule Corpus) | Yes | Not stated |
| 230 | 2025 | [[2025-Wu-Chain-of-Ethics Defense Framework Wu et al.]] | Medical Ethics Jailbreak Framework (Chinese Con... | Partial | Not stated |
| 231 | 2025 | [[2025-Wu-CVC]] | C-VARC / CVC (Chinese Value Rule Corpus) | Yes | Not stated |
| 232 | 2025 | [[2025-Wu-OpenDeception Benchmarking and Investigating AI Deceptive Behaviors]] | OpenDeception | No | Not stated |
| 233 | 2025 | [[2025-Wu-OpenDeception]] | OpenDeception | No | Not stated |
| 234 | 2025 | [[2025-Wu-The Staircase of Ethics Multi-step Moral Dilemmas]] | Multi-step Moral Dilemmas (MMDs) | Yes | Public |
| 235 | 2025 | [[2025-Xia-SafeToolBench]] | SafeToolBench | No | Public |
| 236 | 2025 | [[2025-Xiang-Comparing Moral Values in Western]] | LLM Moral Word Association Framework | Yes | Public |
| 237 | 2025 | [[2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal]] | SORRY-Bench | No | Public |
| 238 | 2025 | [[2025-Yao-NurValues]] | NurValues | Partial | Not stated |
| 239 | 2025 | [[2025-Yao-Value Compass Benchmarks]] | Value Compass Benchmarks | Yes | Public |
| 240 | 2025 | [[2025-Ye-GPLA Generative Psycho-Lexical Approach for Constructing Value Systems]] | GPLA (Generative Psycho-Lexical Approach) | Yes | Not stated |
| 241 | 2025 | [[2025-Ye-Large Language Model Psychometrics]] | LLM Psychometrics Framework (survey/meta-analysis) | Partial | Code available |
| 242 | 2025 | [[2025-Yuan-Probabilistic Aggregation and Targeted Embedding]] | Probabilistic Aggregation for Collective Moral... | Partial | Code available |
| 243 | 2025 | [[2025-Yuan-S-Eval]] | S-Eval | Partial | Public |
| 244 | 2025 | [[2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large]] | Large-scale Moral Machine Experiment on LLMs | Partial | Code available |
| 245 | 2025 | [[2025-Zhang-LLMEval-Med Medical Safety & Ethics Component]] | LLMEval-Med (Safety & Ethics Component) | No | Public |
| 246 | 2025 | [[2025-Zhang-REVAL]] | REVAL | No | Public |
| 247 | 2025 | [[2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized]] | Fair-PP | Yes | Public |
| 248 | 2025 | [[2025-Zhou-Moral Reasoning Across Languages The Critical Role of Low-Resource]] | Multilingual Moral Reasoning Benchmark (MMRB) -... | Yes | Not stated |
| 249 | 2025 | [[2025-Zhou-Moral Reasoning Across Languages]] | Multilingual Moral Reasoning Benchmark (MMRB) | Yes | Code available |
| 250 | 2025 | [[2025-Zhou-SocialEval Evaluating Social Intelligence of Large Language Models]] | SocialEval | Partial | Public |
| 251 | 2025 | [[2025-Zhu-EAVIT]] | EAVIT (Efficient and Accurate Value Identificat... | Partial | Code available |
| 252 | 2025 | [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]] | TrolleyBench | Partial | Public |
| 253 | 2025 | [[2025-Zhu-TrolleyBench]] | TrolleyBench (duplicate entry) | Partial | Public |
| 254 | 2025 | [[2025-Zohny-ADEPT Simulating Ethics]] | ADEPT (AI Debate Ethics Panel Tool) | Yes | Code available |
| 255 | 2025 | [[2025-Zulaika-BasqBBQ Basque BBQ]] | BasqBBQ (Basque BBQ) | Partial | Not stated |
| 256 | 2024 | [[2024-Aakanksha-The Multilingual Alignment Prism]] | Multilingual Alignment Prism | Yes | Not stated |
| 257 | 2024 | [[2024-Abdulhai-Moral Foundations of Large Language Models]] | MFT-based LLM Evaluation | Partial | Not stated |
| 258 | 2024 | [[2024-Agarwal-Ethical Reasoning and Moral Value Alignment Multilingual]] | Multilingual Ethical Reasoning Framework | Yes | Not stated |
| 259 | 2024 | [[2024-Agarwal-Ethical Reasoning and Moral Value Alignment]] | Multilingual Ethical Reasoning Framework | Yes | Not stated |
| 260 | 2024 | [[2024-Agarwal-Ethical Reasoning Depends on Language]] | Multilingual Ethical Reasoning Framework | Yes | Not stated |
| 261 | 2024 | [[2024-Aksoy-Whose Morality Do They Speak]] | MFQ-2 Multilingual LLM Evaluation | Yes | Not stated |
| 262 | 2024 | [[2024-AlKhamissi-Investigating Cultural Alignment of LLMs]] | Cultural Alignment Survey Replication / Anthrop... | Yes | Code available |
| 263 | 2024 | [[2024-Almeida-Exploring the Psychology of LLMs Moral Reasoning]] | Unnamed (Replicated Psychology Studies) | No | Not stated |
| 264 | 2024 | [[2024-Anonymous-ForbiddenQuestions]] | ForbiddenQuestions | No | Not stated |
| 265 | 2024 | [[2024-Arshad-HateInsights]] | HateInsights | Partial | Public |
| 266 | 2024 | [[2024-Arshad-Understanding hate speech]] | HateInsights | Partial | Public |
| 267 | 2024 | [[2024-Bajaj-GenMO Gender-bias in Morality Opinions]] | GenMO (Gender-bias in Morality Opinions) | Partial | Not stated |
| 268 | 2024 | [[2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said]] | Political Bias Measurement Framework | Partial | Not stated |
| 269 | 2024 | [[2024-Benkler-Cross-Linguistic Moral Preferences in LLMs - Evidence from]] | RVR-based LLM Value Assessment (Recognizing Val... | Yes | Not stated |
| 270 | 2024 | [[2024-Bhardwaj-Language Models are Homer Simpson! Safety]] | Multilingual Safety Benchmark (RESTA) | Partial | Code available |
| 271 | 2024 | [[2024-Biedma-Beyond Human Norms]] | ValueLex | Yes | Not stated |
| 272 | 2024 | [[2024-Bignotti-Legal Minds, Algorithmic Decisions]] | Unnamed (Italian Constitutional Bioethics Analy... | Partial | Not stated |
| 273 | 2024 | [[2024-Bonagiri-SaGE Semantic Graph Entropy Moral Consistency Corpus]] | SaGE / Moral Consistency Corpus (MCC) | No | Public |
| 274 | 2024 | [[2024-Bonagiri-SaGE]] | SaGE / Moral Consistency Corpus (MCC) | No | Public |
| 275 | 2024 | [[2024-Buyl-Large Language Models Reflect the Ideology of]] | LLM Ideology Analysis | Yes | Public |
| 276 | 2024 | [[2024-Cahyawijaya-High-Dimension Human Value Representation in]] | UniVaR (Universal Value Representation) | Yes | Not stated |
| 277 | 2024 | [[2024-Cao-The Moral Foundations Weibo Corpus]] | Moral Foundations Weibo Corpus (MFWC) | Yes | Not stated |
| 278 | 2024 | [[2024-Chao-JailbreakBench - An Open Robustness Benchmark]] | JailbreakBench | No | Public |
| 279 | 2024 | [[2024-Chao-JailbreakBench]] | JailbreakBench | No | Public |
| 280 | 2024 | [[2024-Chao-JBB-Behaviours]] | JailbreakBench / JBB-Behaviors | No | Public |
| 281 | 2024 | [[2024-Chern-BeHonest]] | BeHonest | No | Public |
| 282 | 2024 | [[2024-Chhabra-Evaluating Computational Models of Ethics]] | SPECTRA | Yes | Not stated |
| 283 | 2024 | [[2024-Chiu-DailyDilemmas]] | DailyDilemmas | Yes | Public |
| 284 | 2024 | [[2024-Dognin-Contextual Moral Value Alignment Through]] | Unnamed (uses Moral Integrity Corpus) | Yes | Not stated |
| 285 | 2024 | [[2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation]] | BELLS | No | Public |
| 286 | 2024 | [[2024-Duan-DeNEVIL MoralPrompt]] | MoralPrompt (with DeNEVIL algorithm) | Yes | Public |
| 287 | 2024 | [[2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian]] | MERA (ruEthics subtask) | Partial | Public |
| 288 | 2024 | [[2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]] | Unnamed (contrast sets for Moral Stories) | No | Not stated |
| 289 | 2024 | [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]] | OffTheRails | Partial | Public |
| 290 | 2024 | [[2024-Freire-Uncovering Latent Human Wellbeing in Language]] | Unnamed (uses ETHICS Utilitarianism task) | No | Not stated |
| 291 | 2024 | [[2024-Garcia-Moral Turing Test]] | Moral Turing Test | Partial | Not stated |
| 292 | 2024 | [[2024-Garcia-The Moral Turing Test]] | Moral Turing Test | Partial | Not stated |
| 293 | 2024 | [[2024-Ghosh-AEGIS]] | AEGIS Safety Dataset | No | Public |
| 294 | 2024 | [[2024-Group-The AI Safety Benchmark]] | AI Safety Benchmark v0.5 (MLCommons) | No | Public |
| 295 | 2024 | [[2024-Guldimann-COMPL-AI EU AI Act Compliance]] | COMPL-AI | Partial | Public |
| 296 | 2024 | [[2024-Gupta-WalledEval]] | WalledEval (including SGXSTest and HIXSTest) | Partial | Public |
| 297 | 2024 | [[2024-Han-MedSafetyBench]] | MedSafetyBench | No | Public |
| 298 | 2024 | [[2024-Han-WildGuard WildGuardTest]] | WildGuardTest (with WildGuardMix dataset) | No | Public |
| 299 | 2024 | [[2024-Hancox-Li-Is ETHICS about ethics]] | Unnamed (critique of ETHICS benchmark) | Partial | Public |
| 300 | 2024 | [[2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values]] | VIVA | Partial | Public |
| 301 | 2024 | [[2024-Huang-CBBQ]] | CBBQ (Chinese Bias Benchmark for QA) | Yes | Public |
| 302 | 2024 | [[2024-Huang-Collective Constitutional AI Aligning a Language Model with Public]] | Collective Constitutional AI (CCAI) | Yes | Public |
| 303 | 2024 | [[2024-Huang-Moral Persuasion in Large Language Models]] | Unnamed (Moral Persuasion Evaluation) | Yes | Code available |
| 304 | 2024 | [[2024-Huang-TrustLLM]] | TrustLLM | Partial | Public |
| 305 | 2024 | [[2024-Jain-Norm Inconsistency in LLM Decision-Making]] | Unnamed (Norm Inconsistency Evaluation) | Partial | Not stated |
| 306 | 2024 | [[2024-Jain-PolygloToxicityPrompts]] | PolygloToxicityPrompts (PTP) | Yes | Public |
| 307 | 2024 | [[2024-Ji-MoralBench]] | MoralBench | Partial | Public |
| 308 | 2024 | [[2024-Jiang-Can Language Models Reason about Individualistic]] | IndieValueCatalog | Yes | Public |
| 309 | 2024 | [[2024-Jiang-WildTeaming at Scale]] | WildJailbreak | No | Public |
| 310 | 2024 | [[2024-Jin-Language Model Alignment in Multilingual Trolley]] | MultiTP | Yes | Public |
| 311 | 2024 | [[2024-Jin-MULTITP - Language Model Alignment in Multilingual Trolley Problems]] | MultiTP | Yes | Public |
| 312 | 2024 | [[2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of]] | Unnamed (uses JCommonsenseMorality and ETHICS) | Yes | Not stated |
| 313 | 2024 | [[2024-Kaiyom-HELM Safety]] | HELM Safety v1.0 | Partial | Public |
| 314 | 2024 | [[2024-Kaneko-Eagle Ethical Dataset Given from Real Interactions]] | Eagle | No | Public |
| 315 | 2024 | [[2024-Kaneko-Eagle]] | Eagle | No | Public |
| 316 | 2024 | [[2024-Kang-Are the Values of LLMs Structurally Aligned with]] | Unnamed (Causal Value Graph analysis) | Partial | Not stated |
| 317 | 2024 | [[2024-Karpov-Inducing Human-like Biases in Moral Reasoning]] | Unnamed (uses ETHICS benchmark + BrainScore) | No | Not stated |
| 318 | 2024 | [[2024-Khandelwal-Do Moral Judgment and Reasoning Capability of]] | Multilingual Defining Issues Test (DIT) | Yes | Not stated |
| 319 | 2024 | [[2024-Khandelwal-Indian-BhED - A Dataset for Measuring India-Centric Biases in LLMs]] | Indian-BhED | Yes | Public |
| 320 | 2024 | [[2024-Khandelwal-Multilingual Defining Issues Test]] | Multilingual Defining Issues Test (DIT) | Yes | Not stated |
| 321 | 2024 | [[2024-Kirch-TRIAGE]] | TRIAGE | No | Not stated |
| 322 | 2024 | [[2024-Kirgis-Differences in Moral Foundations of LLMs]] | Unnamed (MFT-based LLM Moral Foundations evalua... | Partial | Code available |
| 323 | 2024 | [[2024-Kirk-PRISM Alignment Dataset]] | PRISM | Yes | Public |
| 324 | 2024 | [[2024-Kirk-The PRISM Alignment Project]] | PRISM | Yes | Public |
| 325 | 2024 | [[2024-Lee-KorNAT]] | KorNAT | Yes | Public |
| 326 | 2024 | [[2024-Li-Benchmarking Ethics in Text-to-Image Models]] | T2IEthics | Partial | Public |
| 327 | 2024 | [[2024-Li-OpenEval - Benchmarking Chinese LLMs across Capability Alignment and]] | OpenEval | Yes | Public |
| 328 | 2024 | [[2024-Li-Quantifying AI Psychology]] | Unnamed (Psychometrics Benchmark for LLMs) | Partial | Not stated |
| 329 | 2024 | [[2024-Li-SALAD-Bench]] | SALAD-Bench | No | Public |
| 330 | 2024 | [[2024-Li-The WMDP Benchmark]] | WMDP (Weapons of Mass Destruction Proxy) | No | Public |
| 331 | 2024 | [[2024-Li-Value-Spectrum]] | Value-Spectrum | Partial | Public |
| 332 | 2024 | [[2024-Li-WMDP Benchmark Measuring and Reducing Malicious Use With Unlearning]] | WMDP (Weapons of Mass Destruction Proxy) | No | Public |
| 333 | 2024 | [[2024-Liu-CultureAtlas]] | CultureAtlas | Yes | Public |
| 334 | 2024 | [[2024-Liu-Evaluating Moral Beliefs across LLMs through a]] | Unnamed (Chinese Moral Choice Scenarios) | Yes | Not stated |
| 335 | 2024 | [[2024-Liu-JAILJUDGE]] | JAILJUDGE | Partial | Public |
| 336 | 2024 | [[2024-Luong-Realistic Evaluation of Toxicity in Large]] | TET (Thoroughly Engineered Toxicity) | No | Not stated |
| 337 | 2024 | [[2024-Marraffini-The Greatest Good Benchmark]] | Greatest Good Benchmark (GGB) | Partial | Not stated |
| 338 | 2024 | [[2024-Mazeika-HarmBench]] | HarmBench | No | Public |
| 339 | 2024 | [[2024-Meadows-LocalValueBench]] | LocalValueBench | Yes | Not stated |
| 340 | 2024 | [[2024-MLCommons-MLCommons AILuminate Benchmark]] | AILuminate v1.0 | Partial | Public |
| 341 | 2024 | [[2024-Moore-Are Large Language Models Consistent over]] | Unnamed (Value Consistency Evaluation) | Yes | Not stated |
| 342 | 2024 | [[2024-Moore-Intuitions of Compromise - Utilitarianism vs. Contractualism]] | Unnamed (Utilitarian Sum vs Nash Product evalua... | Yes | Not stated |
| 343 | 2024 | [[2024-Mou-SGBench]] | SG-Bench | No | Public |
| 344 | 2024 | [[2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and]] | EAI (Emotional AI Framework) | No | Public |
| 345 | 2024 | [[2024-Nahian-The Goofus & Gallant Story Corpus for Practical]] | Goofus & Gallant Story Corpus | No | Not stated |
| 346 | 2024 | [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] | Unnamed (Moral Hypocrisy Evaluation using MFQ +... | Yes | Not stated |
| 347 | 2024 | [[2024-Obi-Value Imprint]] | Value Imprint | Yes | Public |
| 348 | 2024 | [[2024-Ohashi-Extended Japanese Commonsense Morality Dataset]] | eJCM (Extended Japanese Commonsense Morality) | Yes | Public |
| 349 | 2024 | [[2024-Park-Morality is Non-Binary]] | Unnamed (Pluralist Moral Sentence Embedding Space) | Yes | Not stated |
| 350 | 2024 | [[2024-Piatti-Cooperate or Collapse]] | GovSim (Governance of the Commons Simulation) | No | Public |
| 351 | 2024 | [[2024-Pisano-Moral High Ground]] | Moral High Ground | No | Not stated |
| 352 | 2024 | [[2024-Pistilli-CIVICS]] | CIVICS (Culturally-Informed and Values-Inclusiv... | Yes | Public |
| 353 | 2024 | [[2024-Potter-Hidden Persuaders LLMs' Political Leaning and Their Influence on]] | Unnamed (LLM Political Leaning Evaluation) | Partial | Not stated |
| 354 | 2024 | [[2024-Qiu-ProgressGym]] | ProgressGym | Yes | Public |
| 355 | 2024 | [[2024-Ramezani-Moral Association Graph Cognitive Model for Interpretable Moral]] | Moral Association Graph (MAG) | Partial | Not stated |
| 356 | 2024 | [[2024-Ren-Safetywashing Do AI Safety Benchmarks Actually Measure Safety Progress]] | Safetywashing Meta-Analysis Framework | No | Public |
| 357 | 2024 | [[2024-Ren-Safetywashing]] | Safetywashing Meta-Analysis | Partial | Public |
| 358 | 2024 | [[2024-Ren-ValueBench]] | ValueBench | Yes | Public |
| 359 | 2024 | [[2024-Rottger-Political Compass or Spinning Arrow]] | Political Compass Test (PCT) evaluation framework | Partial | Public |
| 360 | 2024 | [[2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety]] | SafetyPrompts | Partial | Public |
| 361 | 2024 | [[2024-Rozado-The Political Preferences of LLMs]] | Political Orientation Test Battery | Partial | Public |
| 362 | 2024 | [[2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation]] | Global Representation Evaluation | Yes | Public |
| 363 | 2024 | [[2024-Röttger-Political Compass or Spinning Arrow]] | Political Compass Test (PCT) evaluation framework | Partial | Public |
| 364 | 2024 | [[2024-Röttger-XSTest]] | XSTest | No | Public |
| 365 | 2024 | [[2024-Saffari-PSN]] | ISN (Iranian Social Norms) | Yes | Public |
| 366 | 2024 | [[2024-Sahoo-IndiBias - Benchmark Dataset for Social Biases in Indian Context]] | IndiBias | Yes | Public |
| 367 | 2024 | [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]] | Scruples (DILEMMAS and ANECDOTES) | No | Public |
| 368 | 2024 | [[2024-Seror-Moral Minds of LLMs]] | Moral Minds Framework (Revealed Preference) | Yes | Not stated |
| 369 | 2024 | [[2024-Seror-The Moral Mind(s) of Large Language Models]] | Moral Minds Framework (Priced Survey Methodolog... | Yes | Not stated |
| 370 | 2024 | [[2024-Sharma-Towards Understanding Sycophancy in Language Models]] | Sycophancy Evaluation | No | Public |
| 371 | 2024 | [[2024-Singhal-AyaRedTeaming]] | AyaRedTeaming | Yes | Public |
| 372 | 2024 | [[2024-Sorensen-A Roadmap to Pluralistic Alignment]] | Pluralistic Alignment Benchmark Framework | Yes | Public |
| 373 | 2024 | [[2024-Sorensen-Value Kaleidoscope ValuePrism]] | ValuePrism / Value Kaleidoscope (Kaleido) | Yes | Public |
| 374 | 2024 | [[2024-Sorensen-Value Kaleidoscope]] | ValuePrism / Value Kaleidoscope (Kaleido) | Yes | Public |
| 375 | 2024 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | Medical Trolley Dilemma Evaluation | Partial | Not stated |
| 376 | 2024 | [[2024-Souly-StrongREJECT]] | StrongREJECT | No | Public |
| 377 | 2024 | [[2024-Sun-ClarityEthic]] | ClarityEthic | Partial | Not stated |
| 378 | 2024 | [[2024-Takemoto-The moral machine experiment on large language]] | Moral Machine Experiment for LLMs | Partial | Code available |
| 379 | 2024 | [[2024-Team-FABLE Fairness and Bias in LLM Evaluation]] | FACT-OR-FAIR | Partial | Public |
| 380 | 2024 | [[2024-Team-GuardBench]] | GuardBench | Partial | Public |
| 381 | 2024 | [[2024-Team-WildGuard]] | WildGuard / WildGuardMix / WildGuardTest | No | Public |
| 382 | 2024 | [[2024-Tian-Chinese SafetyQA - A Safety Short-form Factuality Benchmark]] | Chinese SafetyQA | Partial | Public |
| 383 | 2024 | [[2024-Tlaie-Exploring and steering the moral compass of Large]] | Moral Foundations Questionnaire (MFQ) + ethical... | Yes | Not stated |
| 384 | 2024 | [[2024-Tom-SG-Bench - Evaluating LLM Safety Generalization]] | SG-Bench | No | Public |
| 385 | 2024 | [[2024-Mou-SGBench]] | SG-Bench | No | Public |
| 386 | 2024 | [[2024-Vida-Decoding Multilingual Moral Preferences - Unveiling LLM's Biases]] | Moral Machine Experiment (MME) for LLMs | Yes | Not stated |
| 387 | 2024 | [[2024-Wang-All Languages Matter]] | XSafety | Partial | Public |
| 388 | 2024 | [[2024-Wang-Do-Not-Answer]] | Do-Not-Answer | No | Public |
| 389 | 2024 | [[2024-Wu-WorldValuesBench]] | WorldValuesBench | Yes | Public |
| 390 | 2024 | [[2024-Xu-Course-Correction]] | C2-EVAL | No | Not stated |
| 391 | 2024 | [[2024-Yan-M$^3$oralBench]] | M3oralBench | Partial | Public |
| 392 | 2024 | [[2024-Yanaka-JBBQ Japanese Bias Benchmark for Question Answering]] | JBBQ (Japanese Bias Benchmark for Question Answ... | Partial | Public |
| 393 | 2024 | [[2024-Yanaka-JBBQ]] | JBBQ (Japanese Bias Benchmark for Question Answ... | Partial | Public |
| 394 | 2024 | [[2024-Yao-CLAVE ValEval]] | CLAVE / ValEval | Yes | Not stated |
| 395 | 2024 | [[2024-Yao-Value FULCRA]] | FULCRA | Yes | Not stated |
| 396 | 2024 | [[2024-Ye-Measuring Human and AI Values Based on Generative]] | GPV (Generative Psychometrics for Values) | Yes | Not stated |
| 397 | 2024 | [[2024-Yin-SafeAgentBench]] | SafeAgentBench | No | Public |
| 398 | 2024 | [[2024-Yu-CMoralEval]] | CMoralEval | Partial | Public |
| 399 | 2024 | [[2024-Yu-CoSafe]] | CoSafe | No | Public |
| 400 | 2024 | [[2024-Yuan-R-Judge]] | R-Judge | No | Public |
| 401 | 2024 | [[2024-Yuan-Social Measuring Social Norms of LLMs]] | Social (Social Norms Dataset) | Partial | Public |
| 402 | 2024 | [[2024-Zeng-AIR-Bench 2024]] | AIR-Bench 2024 | Partial | Public |
| 403 | 2024 | [[2024-Zeng-Quantifying Risk Propensities of Large Language]] | DOSPERT for LLMs / EDRAS (Ethical Decision-Maki... | Partial | Not stated |
| 404 | 2024 | [[2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents]] | Agent-SafetyBench | No | Public |
| 405 | 2024 | [[2024-Zhang-ChineseSafe - A Chinese Benchmark for Evaluating Safety in LLMs]] | ChineseSafe | Partial | Public |
| 406 | 2024 | [[2024-Zhang-CHiSafetyBench - A Chinese Hierarchical Safety Benchmark for LLMs]] | CHiSafetyBench | Partial | Public |
| 407 | 2024 | [[2024-Zhang-CHiSafetyBench]] | CHiSafetyBench | Partial | Public |
| 408 | 2024 | [[2024-Zhang-Edu-Values - Evaluating Chinese Education Values of LLMs]] | Edu-Values | Partial | Not stated |
| 409 | 2024 | [[2024-Zhang-SafetyBench Evaluating the Safety of Large Language Models]] | SafetyBench | Partial | Public |
| 410 | 2024 | [[2024-Zhang-SafetyBench]] | SafetyBench | Partial | Public |
| 411 | 2024 | [[2024-Zhang-ValueDCG]] | ValueDCG | No | Public |
| 412 | 2024 | [[2024-Zhao-CoSafe]] | CoSafe | No | Not stated |
| 413 | 2024 | [[2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via]] | ALI-Agent | No | Public |
| 414 | 2024 | [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] | Unnamed (top-down moral reasoning framework) | Yes | Not stated |
| 415 | 2024 | [[2024-Zhou-tSMC]] | tSMC (Symmetric Moral Consistency) | No | Not stated |
| 416 | 2023 | [[2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop]] | Unnamed (Cross-Cultural Values Probing) | Yes | Not stated |
| 417 | 2023 | [[2023-Aroyo-DICES Dataset]] | DICES (Diversity In Conversational AI Evaluatio... | Yes | Public |
| 418 | 2023 | [[2023-Astobiza-MoralNet]] | MoralNet | Yes | Not stated |
| 419 | 2023 | [[2023-Atre-Benchmarking Cognitive Biases in Large Language]] | CoBBLEr (Cognitive Bias Benchmark for LLMs as E... | No | Public |
| 420 | 2023 | [[2023-Ayele-Amharic Hate Speech Dataset]] | Amharic Hate Speech Dataset | Yes | Public |
| 421 | 2023 | [[2023-Bang-Towards Answering Open-ended Ethical Quandary]] | Ethical Quandary GQA / AISocrates | Yes | Not stated |
| 422 | 2023 | [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] | RVR-based Value Pluralism Assessment | Yes | Not stated |
| 423 | 2023 | [[2023-Cao-Assessing Cross-Cultural Alignment between]] | Unnamed (Cross-Cultural Alignment Assessment) | Yes | Not stated |
| 424 | 2023 | [[2023-Catapang-EMoTES-3K]] | EMoTES-3K | Yes | Not stated |
| 425 | 2023 | [[2023-Dai-Safe RLHF]] | BeaverTails (used) / Safe RLHF evaluation | No | Public |
| 426 | 2023 | [[2023-Davani-Disentangling Perceptions of Offensiveness]] | Unnamed (cross-cultural offensiveness perceptio... | Yes | Not stated |
| 427 | 2023 | [[2023-Deng-Probing the Moral Development of Large Language]] | Defining Issues Test (DIT) adapted for LLMs | Partial | Not stated |
| 428 | 2023 | [[2023-Duan-Denevil]] | MoralPrompt (via DeNEVIL) | Yes | Public |
| 429 | 2023 | [[2023-Durmus-Towards Measuring the Representation of]] | GlobalOpinionQA | Yes | Public |
| 430 | 2023 | [[2023-Dwivedi-EtiCor Corpus for Analyzing LLMs for Etiquettes]] | EtiCor | Yes | Not stated |
| 431 | 2023 | [[2023-Dwivedi-EtiCor]] | EtiCor | Yes | Not stated |
| 432 | 2023 | [[2023-Fischer-What does ChatGPT return about human values]] | Unnamed (Schwartz Value Theory probes for ChatGPT) | Partial | Public |
| 433 | 2023 | [[2023-Fleisig-FairPrism]] | FairPrism | Partial | Public |
| 434 | 2023 | [[2023-Hartmann-The political ideology of conversational AI]] | Unnamed (Political ideology evaluation of ChatGPT) | Partial | Not stated |
| 435 | 2023 | [[2023-Huang-Flames]] | FLAMES | Yes | Public |
| 436 | 2023 | [[2023-Ji-BeaverTails]] | BeaverTails | No | Public |
| 437 | 2023 | [[2023-Ji-Commonsense Norm Bank]] | MEC (Maximizing Expected Choiceworthiness) / Th... | Yes | Not stated |
| 438 | 2023 | [[2023-Jiang-MACHIAVELLI]] | MACHIAVELLI | Partial | Public |
| 439 | 2023 | [[2023-Lee-KoSBI]] | KoSBI | Yes | Not stated |
| 440 | 2023 | [[2023-Lin-ToxicChat]] | ToxicChat | No | Public |
| 441 | 2023 | [[2023-Liu-AlignBench]] | AlignBench | Partial | Public |
| 442 | 2023 | [[2023-Miah-Islam QA]] | Islam QA Dataset | Partial | Public |
| 443 | 2023 | [[2023-Mougan-Kantian Deontology Meets AI Alignment]] | Unnamed | Yes | Public |
| 444 | 2023 | [[2023-Nie-MoCa]] | MoCa | No | Public |
| 445 | 2023 | [[2023-Oliveira-Culturally-Attuned Moral Machines]] | Unnamed | Yes | Not stated |
| 446 | 2023 | [[2023-Pan-Do the Rewards Justify the Means Measuring]] | MACHIAVELLI | Partial | Public |
| 447 | 2023 | [[2023-Qian-Understanding Chinese Moral Stories with Further]] | STORAL-ZH | Partial | Public |
| 448 | 2023 | [[2023-Rao-Ethical Reasoning over Moral Alignment]] | Unnamed | Yes | Not stated |
| 449 | 2023 | [[2023-Rao-What Makes it Ok to Set a Fire Iterative]] | delta-Rules-of-Thumb (delta-RoT) | Partial | Public |
| 450 | 2023 | [[2023-Rizqullah-QASiNa]] | QASiNa | Partial | Not stated |
| 451 | 2023 | [[2023-Roger-Towards ethical multimodal systems]] | Unnamed (Multimodal Ethics Database) | No | Not stated |
| 452 | 2023 | [[2023-Rystrøm-Apolitical Intelligence]] | Unnamed | Yes | Not stated |
| 453 | 2023 | [[2023-Santurkar-OpinionQA]] | OpinionQA | Yes | Public |
| 454 | 2023 | [[2023-Santurkar-Whose Opinions Do Language Models Reflect]] | OpinionQA | Yes | Public |
| 455 | 2023 | [[2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs]] | MoralChoice | Partial | Public |
| 456 | 2023 | [[2023-Shen-“Do Anything Now”]] | JailbreakHub | No | Public |
| 457 | 2023 | [[2023-Boddington-Normative Ethical Theory AI Ethics]] | Unnamed (MEC Framework) | Yes | Not stated |
| 458 | 2023 | [[2023-Tanmay-Probing Moral Development through Defining Issues Test DIT]] | DIT (Defining Issues Test) for LLMs | Partial | Public |
| 459 | 2023 | [[2023-Wang-DecodingTrust]] | DecodingTrust | Partial | Public |
| 460 | 2023 | [[2023-Wang-STREAM]] | STREAM | Yes | Public |
| 461 | 2023 | [[2023-Xu-CValues - Measuring the Values of Chinese LLMs from Safety to]] | CValues | Partial | Public |
| 462 | 2023 | [[2023-Xu-CValues]] | CValues | Partial | Public |
| 463 | 2023 | [[2023-Xu-SC-Safety]] | SuperCLUE-Safety (SC-Safety) | Partial | Public |
| 464 | 2023 | [[2023-Yao-Value FULCRA]] | FULCRA | Yes | Public |
| 465 | 2023 | [[2023-Zhang-Heterogeneous Value Alignment Evaluation for]] | HVAE (Heterogeneous Value Alignment Evaluation) | Yes | Not stated |
| 466 | 2023 | [[2023-Ziems-NormBank]] | NormBank | Partial | Public |
| 467 | 2022 | [[2022-Bai-Constitutional AI]] | Constitutional AI Evaluation | No | Not stated |
| 468 | 2022 | [[2022-Bai-HH-RLHF Helpful and Harmless RLHF]] | HH-RLHF (Helpful and Harmless RLHF Dataset) | No | Public |
| 469 | 2022 | [[2022-Bai-Training a Helpful and Harmless Assistant with]] | HH-RLHF (Helpful and Harmless RLHF Dataset) | No | Public |
| 470 | 2022 | [[2022-Bang-Enabling Classifiers to Make Judgements]] | Value-Aligned Classification Framework | Yes | Not stated |
| 471 | 2022 | [[2022-Fraser-Does Moral Code Have a Moral Code]] | Unnamed (Delphi moral philosophy probing) | Partial | Not stated |
| 472 | 2022 | [[2022-Ganguli-Red Teaming Language Models to Reduce Harms]] | Anthropic Red Team Dataset | No | Public |
| 473 | 2022 | [[2022-Hartvigsen-ToxiGen]] | ToxiGen | Partial | Public |
| 474 | 2022 | [[2022-Hendrycks-What Would Jiminy Cricket Do]] | Jiminy Cricket | No | Public |
| 475 | 2022 | [[2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction]] | Visual Commonsense Immorality Benchmark | No | Public |
| 476 | 2022 | [[2022-Jiang-Can Machines Learn Morality]] | Commonsense Norm Bank / Delphi | Partial | Public |
| 477 | 2022 | [[2022-Kim-ProsocialDialog A Prosocial Backbone for Conversational Agents]] | ProsocialDialog | Partial | Public |
| 478 | 2022 | [[2022-Kim-ProsocialDialog]] | ProsocialDialog | Partial | Public |
| 479 | 2022 | [[2022-Li-Evaluating Psychological Safety of Large Language]] | Unnamed (Psychological Safety Evaluation Framew... | No | Not stated |
| 480 | 2022 | [[2022-Liang-Holistic Evaluation of Language Models]] | HELM (Holistic Evaluation of Language Models) | Partial | Public |
| 481 | 2022 | [[2022-Liu-CoreValue Chinese Values Knowledge Base Liu et al.]] | CoreValue | Yes | Not stated |
| 482 | 2022 | [[2022-Parrish-BBQ Bias Benchmark for Question Answering]] | BBQ (Bias Benchmark for QA) | Partial | Public |
| 483 | 2022 | [[2022-Parrish-BBQ]] | BBQ (Bias Benchmark for QA) | Partial | Public |
| 484 | 2022 | [[2022-Qiu-ValueNet]] | ValueNet | Yes | Public |
| 485 | 2022 | [[2022-Röttger-Multilingual HateCheck]] | Multilingual HateCheck (MHC) | Yes | Public |
| 486 | 2022 | [[2022-Sahoo-Detecting Unintended Social Bias in Toxic]] | ToxicBias | Partial | Not stated |
| 487 | 2022 | [[2022-Schramowski-I2P Inappropriate Image Prompts Test Bed]] | I2P (Inappropriate Image Prompts) / Q16 | No | Public |
| 488 | 2022 | [[2022-Sun-MoralDial]] | MoralDial | Yes | Not stated |
| 489 | 2022 | [[2022-Trager-The Moral Foundations Reddit Corpus]] | MFRC (Moral Foundations Reddit Corpus) | Partial | Public |
| 490 | 2022 | [[2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML]] | Unnamed (Virtue Ethics Game Environment) | Partial | Not stated |
| 491 | 2022 | [[2022-Ziems-Moral Integrity Corpus MIC]] | MIC (Moral Integrity Corpus) | Partial | Public |
| 492 | 2022 | [[2022-Ziems-The Moral Integrity Corpus]] | MIC (Moral Integrity Corpus) | Partial | Public |
| 493 | 2021 | [[2021-Askell-A General Language Assistant as a Laboratory for]] | HHH Alignment Evaluations | No | Not stated |
| 494 | 2021 | [[2021-Barikeri-REDDITBIAS]] | REDDITBIAS | Partial | Public |
| 495 | 2021 | [[2021-Dhamala-BOLD]] | BOLD (Bias in Open-Ended Language Generation Da... | Partial | Public |
| 496 | 2021 | [[2021-Emelin-Moral Stories]] | Moral Stories | No | Public |
| 497 | 2021 | [[2021-Hendrycks-Aligning AI with Shared Human Values]] | ETHICS | Yes | Public |
| 498 | 2021 | [[2021-Lourie-Scruples]] | SCRUPLES | Partial | Public |
| 499 | 2021 | [[2021-Munshi-Towards an Automated Islamic Fatwa System]] | Islamic Fatwa Dataset | Yes | Public |
| 500 | 2021 | [[2021-Nadeem-StereoSet]] | StereoSet | Partial | Public |
| 501 | 2021 | [[2021-Nangia-CrowS-Pairs]] | CrowS-Pairs | Partial | Public |
| 502 | 2021 | [[2021-Röttger-HateCheck]] | HateCheck | No | Public |
| 503 | 2020 | [[2020-Awad-Universals and variations in moral decisions made]] | Moral Machine Classic Mode Dataset | Yes | Public |
| 504 | 2020 | [[2020-Forbes-Social Chemistry 101 SOCIAL-CHEM-101]] | SOCIAL-CHEM-101 | Partial | Public |
| 505 | 2020 | [[2020-Forbes-Social Chemistry 101]] | SOCIAL-CHEM-101 | Partial | Public |
| 506 | 2020 | [[2020-Gehman-RealToxicityPrompts]] | RealToxicityPrompts | No | Public |
| 507 | 2020 | [[2020-Hoover-Moral Foundations Twitter Corpus]] | Moral Foundations Twitter Corpus (MFTC) | Partial | Public |
| 508 | 2020 | [[2020-Kumar-Evaluating Aggression Identification in Social]] | TRAC-2 Shared Task Dataset | Yes | Public |
| 509 | 2020 | [[2020-Mainali-Automated Classification of Modes of Moral]] | Unnamed (Moral Reasoning Mode Classifier) | Partial | Not stated |
| 510 | 2020 | [[2020-Mathew-HateXplain]] | HateXplain | Partial | Public |
| 511 | 2020 | [[2020-Nangia-CrowS-Pairs]] | CrowS-Pairs | Partial | Public |
| 512 | 2020 | [[2020-Sap-Social Bias Frames]] | Social Bias Inference Corpus (SBIC) | Partial | Public |
| 513 | 2020 | [[2020-Schramowski-The Moral Choice Machine]] | Moral Choice Machine (MCM) | Yes | Public |
| 514 | 2019 | [[2019-Basile-SemEval-2019 Task 5]] | HatEval (SemEval-2019 Task 5) | Partial | Public |
| 515 | 2019 | [[2019-De-Arteaga-Bias in Bios]] | Bias in Bios | No | Not stated |
| 516 | 2019 | [[2019-Ibrohim-Multi-label Hate Speech and Abusive Language]] | Indonesian Twitter Hate Speech Dataset | Partial | Not stated |
| 517 | 2019 | [[2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]] | ToxicBias / Jigsaw Unintended Bias Dataset | Partial | Public |
| 518 | 2019 | [[2019-Kreutz-GermEval 2019 Task 2]] | GermEval 2019 Task 2 | Partial | Public |
| 519 | 2019 | [[2019-Struß-Overview of GermEval Task 2, 2019 Shared Task on]] | GermEval 2019 Shared Task on Offensive Language | Partial | Public |
| 520 | 2019 | [[2019-University of São Paulo-Moral Stance Recognition and Polarity]] | Brazilian Portuguese Moral Stance Corpus | Partial | Not stated |
| 521 | 2018 | [[2018-Awad-The Moral Machine experiment]] | Moral Machine | Yes | Public |
| 522 | 2018 | [[2018-Behzadan-TrolleyMod v1.0]] | TrolleyMod v1.0 | No | Public |
| 523 | 2018 | [[2018-Crone-The Socio-Moral Image Database (SMID)]] | SMID (Socio-Moral Image Database) | Partial | Public |
| 524 | 2018 | [[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]] | Identity Phrase Template Test Set / Pinned AUC | Partial | Public |
| 525 | 2018 | [[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]] | Equity Evaluation Corpus (EEC) | Partial | Public |
| 526 | 2018 | [[2018-Noothigattu-A Voting-Based System for Ethical Decision Making]] | Unnamed (Voting-Based Ethical Decision Making S... | Partial | Not stated |
| 527 | 2018 | [[2018-Zhao-Gender Bias in Coreference Resolution]] | WinoBias | No | Public |
| 528 | 2016 | [[2016-Bolukbasi-Man is to Computer Programmer as Woman is to]] | Word Embedding Association Test (WEAT) / Debias... | No | Public |

---

## Appendix B: Normalization Definitions

### Model Families

| Family | Regex Pattern |
|--------|--------------|
| Alpaca | `\balpaca\b` |
| Anthropic models | `\banthropic\b.*(?:model|language|assistant)` |
| Aya | `\baya\b` |
| BERT family | `\bbert\b|\broberta\b|\balbert\b|\bdeberta\b|\belectra\b` |
| BLOOM | `\bbloom\b(?!berg)` |
| Baichuan | `\bbaichuan\b` |
| ChatGLM | `\bchatglm\b|\bglm\b` |
| Claude | `\bclaude\b` |
| Cohere | `\bcohere\b|\bcommand[\s\-_]?r\b` |
| DeepSeek | `\bdeepseek\b` |
| Delphi | `\bdelphi\b` |
| DialoGPT | `\bdialogpt\b` |
| Falcon | `\bfalcon\b` |
| GPT-2 | `\bgpt[\s\-_]?2\b` |
| GPT-3 | `\bgpt[\s\-_]?3\b(?!\.?5)` |
| GPT-3.5 | `\bgpt[\s\-_]?3\.?5\b|\bchatgpt\b` |
| GPT-4 | `\bgpt[\s\-_]?4\b` |
| Gemini | `\bgemini\b|\bgemma\b` |
| Gemma | `\bgemma\b(?!.*gemini)` |
| InternLM | `\binternlm\b` |
| Jurassic/AI21 | `\bjurassic\b|\bai21\b|\bj2\b` |
| Llama | `\bll?ama[\s\-_]?\d?\b` |
| MPT | `\bmpt[\s\-_]?\d` |
| Mistral/Mixtral | `\bmistral\b|\bmixtral\b` |
| OPT | `\bopt[\s\-_]\d|\bopt\b(?=[\s,\-]|\Z)` |
| OpenAI (unspecified) | `\bopenai\b.*(?:model|api)` |
| PaLM | `\bpalm\b|\bpalm[\s\-_]?2\b` |
| Phi | `\bphi[\s\-_]?\d\b` |
| Qwen | `\bqwen\b` |
| StableLM | `\bstablelm\b|\bstable[\s\-_]?lm\b` |
| T5/Flan | `\b(?:flan[\s\-_]?)?t5\b|\bflan\b` |
| Vicuna | `\bvicuna\b` |
| WizardLM | `\bwizardlm\b` |
| Word2Vec/GloVe | `\bword2vec\b|\bglove\b|\bfasttext\b` |
| Yi | `\b(?:yi[\s\-_]?\d|yi\b(?=[\s,]))` |
| Zephyr | `\bzephyr\b` |

### Methodology Types

| Type | Regex Pattern |
|------|--------------|
| Adversarial/red-teaming | `adversarial|red[\s\-]?team|jailbreak|attack|prompt injection|bypass` |
| Benchmark suite (multi-task) | `benchmark.*suite|multi[\s\-]?task|(?:comprehensive|holistic|unified).*(?:benc...` |
| Classification task | `classif(?:y|ication)|categori[zs]|label(?:ing|ed)|detect(?:ion|ing)|binary.*(...` |
| Crowdsourced annotation | `crowdsourc|(?:amazon|mturk).*mechanical.*turk|annotator|annotation.*(?:task|p...` |
| Embedding analysis | `embedding.*(?:analy|bias|space|associat)|word.*(?:embedding|vector).*(?:bias|...` |
| Free-text generation | `free[\s\-]?(?:text|form)|open[\s\-]?ended.*generat|text generation|natural la...` |
| Game/simulation | `game|simulat|interactive.*(?:environ|scenar|platform)|reward.*(?:shaping|mode...` |
| Human preference/comparison | `human.*prefer|prefer.*(?:pair|comparison|ranking)|crowdsourc.*(?:annotat|judg...` |
| Likert/scale rating | `likert|rating.*scale|scale.*(?:\d[\s\-]point|\d[\s\-]level)|numerical.*rating...` |
| Multi-turn dialogue | `multi[\s\-]?turn|dialogue|dialog|conversation|chat.*(?:based|eval|bench)` |
| Multiple-choice QA | `multiple[\s\-]?choice|MCQ|multi[\s\-]?choice|forced[\s\-]?choice.*(?:question...` |
| Scenario/vignette judgment | `scenario|vignette|moral dilemma|trolley|ethical dilemma|thought experiment|si...` |
| Survey/questionnaire | `survey|questionnaire|poll|world value survey|pew.*research|opinion.*(?:survey...` |
| Template/probing | `template|prob(?:e|ing)|fill[\s\-]?in|cloze|mask(?:ed|ing)|counterfactual` |

### Ethical Traditions

| Tradition | Regex Pattern |
|-----------|--------------|
| Buddhist | `\bbuddhis[mt]\b|\bdharma\b|\bkarma\b|\bahimsa\b|\bfour.*noble.*truth` |
| Care Ethics | `\bcare.*ethic\b|\bfeminist.*ethic\b|\bethic.*of.*care\b|\brelational.*ethic\b` |
| Confucian | `\bconfucian\b|\bconfucius\b|\bmencius\b|\brunren\b|\bli\b(?=.*ritual)|five.*(?:relationship|constant)` |
| Consequentialist | `\bconsequential\b|\butilitarian\b|\bgreatest.*(?:good|happin)\b|\bwelfare.*maximiz` |
| Deontological | `\bdeontolog\b|\bkantian\b|\bcategorical.*imperative\b|\bduty[\s\-]?based\b` |
| Hindu | `\bhindu(?:ism)?\b|\bvedic\b|\bdharma\b|\bkarma\b` |
| Indigenous | `\bindigenous\b|\bfirst.*nation\b|\baboriginal\b|\bnative.*(?:people|ethic|value)` |
| Islamic | `\bislam(?:ic)?\b|\bsharia\b|\bquran\b|\bhadith\b|\bfiqh\b|\bmaqasid\b|\bhalal\b|\bharam\b` |
| Ubuntu | `\bubuntu\b(?!.*(?:linux|operat))` |
| Virtue Ethics (Western) | `\bvirtue.*ethic\b|\baristot(?:le|elian)\b|\beudaimonia\b|\bcharacter.*ethic\b|\bphronesis\b` |

---

*Generated: 2026-02-10 | Script: `PYTHON/generate_vault_overview_report.py` | Papers: 528/924 candidates | Categories: 10*