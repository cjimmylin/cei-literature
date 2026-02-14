# LLM Assessment & Data Availability Report

> **Generated:** 2026-02-13 | **Papers scanned:** 1636

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [LLM Model Landscape](#2-llm-model-landscape)
   - 2.1 Model Frequency Table
   - 2.2 Model Family Grouping
   - 2.3 Proprietary vs Open-Source Breakdown
   - 2.4 Models Per Paper Distribution
   - 2.5 Model Co-Occurrence Matrix
3. [Data Availability Analysis](#3-data-availability-analysis)
   - 3.1 URL Presence Statistics
   - 3.2 Hosting Platform Breakdown
   - 3.3 Overlap: LLM Models AND Data URLs
4. [Gap Analysis](#4-gap-analysis)
   - 4.1 Papers with LLM Models but No Public Data URL
   - 4.2 Papers with Data URLs but No LLM Models Identified
   - 4.3 Underrepresented Model Families
- [Appendix A: Model Family Normalization Table](#appendix-a-model-family-normalization-table)
- [Appendix B: Methodology Notes](#appendix-b-methodology-notes)

---

## 1. Executive Summary

This report analyzes **1636 papers** in the CEI Literature Vault for LLM model assessment
coverage and public data/benchmark availability.

| Metric | Count | % of Total |
|--------|------:|:----------:|
| Papers with LLM models identified | 565 | 34.5% |
| Papers with no LLM models (NA) | 1071 | 65.5% |
| Papers with public data URL | 591 | 36.1% |
| Papers with no data URL (NA) | 1045 | 63.9% |
| Papers with **both** models + URL | 377 | 23.0% |
| Papers with **neither** | 857 | 52.4% |

- **47 unique model names** across **13 model families** detected
- Average models per paper (among assessed papers): **4.3** (max: 14)

---

## 2. LLM Model Landscape

### 2.1 Model Frequency Table

All unique models ranked by number of papers mentioning them:

| Rank | Model | Papers | Family |
|-----:|-------|-------:|--------|
| 1 | GPT-4 | 319 | OpenAI |
| 2 | Llama-3 | 236 | Meta |
| 3 | Claude | 183 | Anthropic |
| 4 | Qwen | 183 | Alibaba |
| 5 | GPT-3.5 | 158 | OpenAI |
| 6 | Mistral | 157 | Mistral AI |
| 7 | Gemini | 153 | Google |
| 8 | Llama-2 | 138 | Meta |
| 9 | DeepSeek | 109 | DeepSeek |
| 10 | Gemma | 100 | Google |
| 11 | ChatGPT | 65 | OpenAI |
| 12 | BERT | 62 | Pre-LLM / Encoder |
| 13 | Mixtral | 54 | Mistral AI |
| 14 | Vicuna | 51 | Open-source (misc) |
| 15 | Llama | 48 | Meta |
| 16 | RoBERTa | 46 | Pre-LLM / Encoder |
| 17 | GPT-4o | 35 | OpenAI |
| 18 | Phi | 33 | Microsoft |
| 19 | GPT-3 | 32 | OpenAI |
| 20 | Falcon | 26 | Open-source (misc) |
| 21 | GPT-2 | 25 | OpenAI |
| 22 | T5 | 24 | Google |
| 23 | Grok | 22 | xAI |
| 24 | o3 | 22 | OpenAI |
| 25 | o1 | 20 | OpenAI |
| 26 | Alpaca | 18 | Open-source (misc) |
| 27 | PaLM-2 | 15 | Google |
| 28 | DeBERTa | 14 | Pre-LLM / Encoder |
| 29 | ALBERT | 13 | Pre-LLM / Encoder |
| 30 | BLOOM | 13 | Open-source (misc) |
| 31 | text-davinci | 13 | OpenAI |
| 32 | OPT | 11 | Meta |
| 33 | Flan-T5 | 11 | Google |
| 34 | BART | 9 | Pre-LLM / Encoder |
| 35 | InstructGPT | 8 | OpenAI |
| 36 | XLNet | 4 | Pre-LLM / Encoder |
| 37 | PaLM | 3 | Google |
| 38 | GPT-4o mini | 3 | OpenAI |
| 39 | Word2Vec | 2 | Embeddings |
| 40 | GloVe | 2 | Embeddings |
| 41 | CodeLlama | 2 | Meta |
| 42 | GPT-5 | 2 | OpenAI |
| 43 | ELMo | 1 | Pre-LLM / Encoder |
| 44 | GPT-J | 1 | Other/Unknown |
| 45 | GPT-NeoX | 1 | Other/Unknown |
| 46 | LaMDA | 1 | Google |
| 47 | Flan-PaLM | 1 | Other/Unknown |

### 2.2 Model Family Grouping

Papers per model family (a paper is counted once per family even if it uses multiple models from that family):

| Rank | Family | Papers | % of Assessed |
|-----:|--------|-------:|--------------:|
| 1 | OpenAI | 427 | 75.6% |
| 2 | Meta | 352 | 62.3% |
| 3 | Google | 257 | 45.5% |
| 4 | Anthropic | 183 | 32.4% |
| 5 | Alibaba | 183 | 32.4% |
| 6 | Mistral AI | 180 | 31.9% |
| 7 | DeepSeek | 109 | 19.3% |
| 8 | Pre-LLM / Encoder | 87 | 15.4% |
| 9 | Open-source (misc) | 86 | 15.2% |
| 10 | Microsoft | 33 | 5.8% |
| 11 | xAI | 22 | 3.9% |
| 12 | Embeddings | 3 | 0.5% |
| 13 | Other/Unknown | 2 | 0.4% |

### 2.3 Proprietary vs Open-Source Breakdown

**By model mention count** (each model×paper counts once):

| Category | Mentions | % |
|----------|--------:|---------:|
| Proprietary (closed-source) | 1054 | 43.0% |
| Open-source / open-weight | 1395 | 57.0% |
| **Total** | **2449** | **100%** |

**By paper count** (papers using at least one model of that type):

| Category | Papers |
|----------|-------:|
| Uses at least one proprietary model | 431 |
| Uses at least one open-source model | 505 |

### 2.4 Models Per Paper Distribution

Among the 565 papers with LLM models identified:

| Models per paper | Papers | % |
|:----------------:|-------:|------:|
| 1 | 68 | 12.0% |
| 2-3 | 163 | 28.8% |
| 4-6 | 236 | 41.8% |
| 7+ | 98 | 17.3% |

### 2.5 Model Co-Occurrence Matrix (Top 12)

How often the top 12 models appear together in the same paper:

| | GPT-4 | Llama-3 | Claude | Qwen | GPT-3.5 | Mistral | Gemini | Llama-2 | DeepSeek | Gemma | ChatGPT | BERT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **GPT-4** | — | 155 | 152 | 122 | 126 | 108 | 117 | 95 | 80 | 58 | 37 | 10 |
| **Llama-3** | 155 | — | 98 | 131 | 69 | 109 | 87 | 58 | 76 | 81 | 18 | 5 |
| **Claude** | 152 | 98 | — | 87 | 64 | 63 | 101 | 41 | 69 | 32 | 22 | 3 |
| **Qwen** | 122 | 131 | 87 | — | 48 | 77 | 78 | 39 | 78 | 57 | 13 | 2 |
| **GPT-3.5** | 126 | 69 | 64 | 48 | — | 52 | 37 | 79 | 25 | 22 | 15 | 9 |
| **Mistral** | 108 | 109 | 63 | 77 | 52 | — | 52 | 61 | 42 | 51 | 16 | 6 |
| **Gemini** | 117 | 87 | 101 | 78 | 37 | 52 | — | 23 | 66 | 40 | 11 | 2 |
| **Llama-2** | 95 | 58 | 41 | 39 | 79 | 61 | 23 | — | 8 | 24 | 25 | 6 |
| **DeepSeek** | 80 | 76 | 69 | 78 | 25 | 42 | 66 | 8 | — | 26 | 5 | 1 |
| **Gemma** | 58 | 81 | 32 | 57 | 22 | 51 | 40 | 24 | 26 | — | 4 | 2 |
| **ChatGPT** | 37 | 18 | 22 | 13 | 15 | 16 | 11 | 25 | 5 | 4 | — | 3 |
| **BERT** | 10 | 5 | 3 | 2 | 9 | 6 | 2 | 6 | 1 | 2 | 3 | — |

---

## 3. Data Availability Analysis

### 3.1 URL Presence Statistics

| Status | Papers | % |
|--------|-------:|------:|
| Has public data URL | 591 | 36.1% |
| No data URL (NA) | 1045 | 63.9% |

### 3.2 Hosting Platform Breakdown

Among papers with data URLs, classified by hosting platform:

| Platform | Papers | % of URLs |
|----------|-------:|----------:|
| GitHub | 378 | 64.0% |
| HuggingFace | 102 | 17.3% |
| Other | 91 | 15.4% |
| OSF | 11 | 1.9% |
| Anonymous (review) | 8 | 1.4% |
| Zenodo | 5 | 0.8% |
| Mendeley Data | 3 | 0.5% |
| GitLab | 2 | 0.3% |
| DOI/Repository | 1 | 0.2% |
| Kaggle | 1 | 0.2% |

### 3.3 Overlap: LLM Models AND Data URLs

| Combination | Papers | % |
|-------------|-------:|------:|
| LLM models + data URL | 377 | 23.0% |
| LLM models only (no URL) | 188 | 11.5% |
| Data URL only (no models) | 214 | 13.1% |
| Neither | 857 | 52.4% |

---

## 4. Gap Analysis

### 4.1 Papers with LLM Models but No Public Data URL

**188 papers** assess LLM models but have no publicly available data URL.

<details>
<summary>Click to expand (188 papers)</summary>

| # | Paper | Models |
|--:|-------|--------|
| 1 | [[2016-Bolukbasi-Man is to Computer Programmer as Woman is to]] | Word2Vec, GloVe |
| 2 | [[2019-He-Unlearn Dataset Bias in Natural Language]] | BERT |
| 3 | [[2019-Kreutz-GermEval 2019 Task 2]] | BERT |
| 4 | [[2019-Struß-Overview of GermEval Task 2, 2019 Shared Task on]] | BERT |
| 5 | [[2019-University of São Paulo-Moral Stance Recognition and Polarity]] | Word2Vec |
| 6 | [[2020-Forbes-Social Chemistry 101]] | GPT-2, T5, BART |
| 7 | [[2021-Clark-All That's 'Human' Is Not Gold]] | GPT-2, GPT-3 |
| 8 | [[2021-Wang-MedAI at SemEval-2021 Task 5]] | RoBERTa |
| 9 | [[2022-Bang-Enabling Classifiers to Make Judgements]] | OPT, ALBERT, RoBERTa, BART |
| 10 | [[2022-Caron-Identifying and Manipulating the Personality]] | BERT, GPT-2 |
| 11 | [[2022-Hu-“I’m sorry to hear that”]] | BERT |
| 12 | [[2022-Li-Evaluating Psychological Safety of Large Language]] | GPT-3, InstructGPT, GPT-3.5, GPT-4, Llama-2 |
| 13 | [[2022-Trager-The Moral Foundations Reddit Corpus]] | Llama-3, BERT |
| 14 | [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]] | text-davinci, RoBERTa |
| 15 | [[2023-Catapang-EMoTES-3K]] | RoBERTa, Flan-T5 |
| 16 | [[2023-Chang-niceNLP at SemEval-2023 Task 10]] | DeBERTa, RoBERTa, BERT |
| 17 | [[2023-Chen-Case Law Grounding]] | GPT-4 |
| 18 | [[2023-Deng-Probing the Moral Development of Large Language]] | GPT-3, GPT-3.5, GPT-4, ChatGPT, PaLM-2, Llama-2, text-dav... |
| 19 | [[2023-Ghafouri-IslamicPCQA]] | BERT, RoBERTa, T5 |
| 20 | [[2023-Hartmann-The political ideology of conversational AI]] | ChatGPT |
| 21 | [[2023-Ji-Commonsense Norm Bank]] | DeBERTa, BERT, RoBERTa, ALBERT, T5 |
| 22 | [[2023-Karra-Estimating the Personality of White-Box Language]] | GPT-2, GPT-3, GPT-3.5, Llama, XLNet |
| 23 | [[2023-Li-On the steerability of large language models]] | Falcon |
| 24 | [[2023-Qian-Understanding Chinese Moral Stories with Further]] | BERT, RoBERTa, T5 |
| 25 | [[2023-Rao-Ethical Reasoning over Moral Alignment]] | GPT-4, GPT-3.5, GPT-3, text-davinci |
| 26 | [[2023-Roger-Towards ethical multimodal systems]] | RoBERTa |
| 27 | [[2023-Rytting-Towards Coding Social Science Datasets with]] | GPT-3 |
| 28 | [[2023-Schulhoff-HackAPrompt]] | GPT-3, ChatGPT, Flan-T5 |
| 29 | [[2023-Takeshita-Towards Theory-based Moral AI]] | DeBERTa, BERT, RoBERTa, ALBERT, T5 |
| 30 | [[2023-Zhang-Heterogeneous Value Alignment Evaluation for]] | GPT-4, GPT-3.5, ChatGPT, Claude, Llama, Alpaca, Vicuna |
| 31 | [[2023-Zhou-A Survey of Large Language Models in Medicine]] | Llama-2 |
| 32 | [[2024-Abdelnabi-Cooperation Competition and Maliciousness LLM-Stakeholders]] | GPT-4, GPT-3.5, Gemini, Llama-2, Llama-3, Mixtral |
| 33 | [[2024-Adelani-IrokoBench - A Benchmark for African Languages in the Age of LLMs]] | GPT-4, GPT-3.5, Gemini, Gemma, Claude, Llama-3, BLOOM |
| 34 | [[2024-Agarwal-Ethical Reasoning Depends on Language]] | GPT-4, ChatGPT, Llama-2 |
| 35 | [[2024-Aksoy-Whose Morality Do They Speak]] | GPT-3.5, GPT-4, Llama-3, Mistral |
| 36 | [[2024-Altenburger-Examining the Role of Relationship Alignment in]] | Llama-3 |
| 37 | [[2024-Arshad-Understanding hate speech]] | BERT, RoBERTa |
| 38 | [[2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said]] | Llama-2, Vicuna, Falcon, Mistral |
| 39 | [[2024-Basem-Optimized Quran Passage Retrieval Using an]] | BERT, RoBERTa |
| 40 | [[2024-Biedma-Beyond Human Norms]] | GPT-4, GPT-3.5, Llama-2, Mistral, Vicuna |
| 41 | [[2024-Bignotti-Legal Minds, Algorithmic Decisions]] | GPT-4 |
| 42 | [[2024-Cahyawijaya-High-Dimension Human Value Representation in]] | ChatGPT, Llama-2, Llama-3, Mistral, Mixtral, BLOOM |
| 43 | [[2024-Cahyawijaya-LLM for everyone]] | GPT-3.5, Llama-3, BLOOM |
| 44 | [[2024-Cao-The Moral Foundations Weibo Corpus]] | GPT-4, Llama-3, Qwen |
| 45 | [[2024-Chen-EmotionQueen A Benchmark for Evaluating Empathy of Large Language]] | GPT-4, GPT-3.5, Claude, Llama-2, BLOOM, Falcon, Vicuna |
| 46 | [[2024-Dognin-Contextual Moral Value Alignment Through]] | Llama-2 |
| 47 | [[2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation]] | GPT-4 |
| 48 | [[2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]] | RoBERTa |
| 49 | [[2024-Freire-Uncovering Latent Human Wellbeing in Language]] | GPT-3, DeBERTa, BERT |
| 50 | [[2024-Garcia-The Moral Turing Test]] | GPT-3.5, text-davinci |
| 51 | [[2024-Ghosh-AEGIS]] | Llama-2, GPT-4, Mistral |
| 52 | [[2024-Gupta-Improving Model Evaluation using SMART Filtering]] | Qwen, Llama-3, Gemma, Phi, Mixtral |
| 53 | [[2024-Huang-Collective Constitutional AI Aligning a Language Model with Public]] | Claude |
| 54 | [[2024-Jain-Norm Inconsistency in LLM Decision-Making]] | GPT-4, Gemini, Claude |
| 55 | [[2024-Kader-The Emergence of Strategic Reasoning of Large Language Models]] | GPT-4, o1, Claude, Gemini |
| 56 | [[2024-Kaiyom-HELM Safety]] | GPT-4, GPT-3.5, Claude, Llama-3, Mistral, Mixtral, Qwen, ... |
| 57 | [[2024-Kang-Are the Values of LLMs Structurally Aligned with]] | Gemma, Llama-3 |
| 58 | [[2024-Khamassi-Strong and weak alignment of large language models]] | ChatGPT, Gemini |
| 59 | [[2024-Khandelwal-Do Moral Judgment and Reasoning Capability of]] | GPT-4, ChatGPT, Llama-2 |
| 60 | [[2024-Khandelwal-Multilingual Defining Issues Test]] | GPT-4, ChatGPT, Llama-2 |
| 61 | [[2024-Li-Quantifying AI Psychology]] | ChatGPT, GPT-4, Mistral, Mixtral, Llama-3, Qwen |
| 62 | [[2024-Luong-Realistic Evaluation of Toxicity in Large]] | ChatGPT, Gemini, Llama-2, Mistral, Mixtral |
| 63 | [[2024-Meadows-LocalValueBench]] | GPT-4, Gemini, Claude |
| 64 | [[2024-Moore-Intuitions of Compromise]] | GPT-4, GPT-3.5, Claude, text-davinci |
| 65 | [[2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and]] | GPT-3.5, GPT-4, Claude, Llama-2, Mixtral |
| 66 | [[2024-Nahian-The Goofus & Gallant Story Corpus for Practical]] | GPT-4, BERT |
| 67 | [[2024-Nunes-Conscience Conflict Evaluating Language Models' Moral Understanding]] | GPT-4, Claude |
| 68 | [[2024-Obi-Value Imprint]] | RoBERTa |
| 69 | [[2024-Pisano-Moral High Ground]] | Flan-T5, Falcon, Llama-2 |
| 70 | [[2024-Potter-Hidden Persuaders LLMs' Political Leaning and Their Influence on]] | GPT-4, GPT-3.5, Claude, Llama-3, Llama-2, Gemini, Mixtral... |
| 71 | [[2024-Qamar-A Benchmark Dataset with Larger Context for]] | T5, BART |
| 72 | [[2024-Ren-Safetywashing]] | Mixtral, Llama-3, Llama-2, Mistral, Falcon, Gemma, Qwen |
| 73 | [[2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity]] | GPT-4, Llama-3, Mistral |
| 74 | [[2024-Seror-The Moral Mind(s) of Large Language Models]] | GPT-4, Claude, Llama-3, Gemini, Qwen, Mixtral, Mistral |
| 75 | [[2024-Sorin-Ethical Alignment of LLMs in Healthcare]] | o1, GPT-4, GPT-3.5, Llama-3, Gemini, Gemma, Phi, Qwen |
| 76 | [[2024-Street-LLMs achieve adult human performance on]] | GPT-3.5, GPT-4, LaMDA, PaLM, Flan-PaLM |
| 77 | [[2024-Takemoto-The moral machine experiment on large language]] | GPT-3.5, GPT-4, PaLM-2, Llama-2 |
| 78 | [[2024-Tlaie-Exploring and steering the moral compass of Large]] | Claude, GPT-3.5, GPT-4, Gemini, Gemma, Llama-2 |
| 79 | [[2024-Wang-Possibilities and challenges in the moral growth of LLMs]] | GPT-2, GPT-3, ChatGPT |
| 80 | [[2024-Yang-DistillSeq]] | GPT-3.5, GPT-4, Vicuna, Llama |
| 81 | [[2024-Yao-CLAVE ValEval]] | GPT-4, GPT-2, Phi, Mistral, Llama-2, Alpaca |
| 82 | [[2024-Zeng-Quantifying Risk Propensities of Large Language]] | GPT-4, GPT-3.5, Claude, Llama-3, Gemma, Qwen, Mistral, Vi... |
| 83 | [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]] | Llama-2, GPT-4 |
| 84 | [[2024-Zhou-tSMC]] | GPT-3.5, Gemini, Llama-2, Llama-3, Mistral, Mixtral, Gemm... |
| 85 | [[2025-Abdaljalil-HalluVerse25]] | GPT-4, Phi, Mistral, Qwen, Gemini, Gemma, Llama-3, PaLM-2 |
| 86 | [[2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment]] | GPT-4, Llama-2, Llama-3, Mistral, Gemma |
| 87 | [[2025-Aggarwal-Letta Leaderboard]] | Claude, GPT-4, Gemini |
| 88 | [[2025-Akata-Playing Repeated Games with Large Language Models]] | GPT-4, text-davinci, Claude, Llama-2 |
| 89 | [[2025-Aleid-Hajj-FQA]] | BERT, RoBERTa, DeBERTa, T5, BART |
| 90 | [[2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic]] | GPT-4, GPT-3.5, Llama-2 |
| 91 | [[2025-Alhassoun-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi]] | GPT-4, GPT-3.5, Llama-3, Llama-2 |
| 92 | [[2025-Andric-Do LLMs Walk Their Talk Multi-Method Moral Evaluation Framework]] | GPT-4, Gemini, Gemma, Claude, Llama-3, Mistral, Grok, Phi |
| 93 | [[2025-Anonymous-BEATS]] | GPT-4, Claude, Gemini, Mistral, Llama-3 |
| 94 | [[2025-Arike-A Framework for Analyzing and Measuring Goal]] | Claude, GPT-4 |
| 95 | [[2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities]] | Gemini, Claude, Llama, Qwen |
| 96 | [[2025-Beyer-LLM-Safety Evaluations Lack Robustness]] | Llama-2 |
| 97 | [[2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for]] | BERT |
| 98 | [[2025-Buyl-AI Alignment at Your Discretion]] | GPT-4, Llama-3, Mistral, DeepSeek, Claude |
| 99 | [[2025-Chakraborty-Structured Moral Reasoning]] | Llama-3, Llama-2, Mistral, Qwen, Phi |
| 100 | [[2025-Chen-SYNTHEMPATHY A Scalable Empathy Corpus Generated Using LLMs Without]] | Llama-2, Llama-3, Gemma, Mistral, RoBERTa |
| 101 | [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]] | GPT-4, Claude, Llama-3 |
| 102 | [[2025-Chua-Between a Rock and a Hard Place TRIAL]] | Llama-3, Mistral |
| 103 | [[2025-Dickerson-Who Gets the Kidney]] | GPT-4, Claude, Gemini, Gemma, Llama-3, DeepSeek |
| 104 | [[2025-Dillion-AI Language Model Rivals Expert Ethicist]] | GPT-3.5, GPT-4 |
| 105 | [[2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value]] | GPT-4, GPT-3.5, o3, Claude, Gemini, Llama-3, Mistral, Qwe... |
| 106 | [[2025-Dubey-Addressing Moral Uncertainty using Large Language]] | GPT-4, Mistral, Llama-3 |
| 107 | [[2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation]] | GPT-4, Gemini |
| 108 | [[2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical]] | Claude, Gemini, Grok, DeepSeek, Llama-3, Phi, Gemma, Qwen |
| 109 | [[2025-Fan-FAIRMT-BENCH]] | ChatGPT, GPT-4, Llama-3, Llama-2, Mistral, Gemma |
| 110 | [[2025-Fanous-SycEval Evaluating LLM Sycophancy]] | ChatGPT, Claude, Gemini, Llama-3 |
| 111 | [[2025-Fenech-Borg-The Cultural Gene of Large Language Models]] | GPT-4 |
| 112 | [[2025-Feng-ERPO]] | Llama-3, Qwen, DeepSeek, GPT-4 |
| 113 | [[2025-Flores-BenchMoral]] | ChatGPT, Llama-3, DeepSeek |
| 114 | [[2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the]] | Llama-2, Llama-3, GPT-3.5 |
| 115 | [[2025-Gao-MIST Moral Inference through Storytelling with Text and Images]] | GPT-4, Llama-3, Claude, Qwen, Gemini |
| 116 | [[2025-Gerdes-Exploring LLM Chatbots as Potential Guides to]] | ChatGPT, DeepSeek |
| 117 | [[2025-Ghosh-AEGIS 2.0]] | Llama-3, Mistral, Gemma, Mixtral |
| 118 | [[2025-Hilliard-Measuring AI Alignment with Human Flourishing]] | GPT-4, GPT-4, ChatGPT, o1, o3, Claude, Gemini, Grok |
| 119 | [[2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset]] | GPT-4, Llama-3, Qwen |
| 120 | [[2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to]] | GPT-4, o1, o3, Claude, Gemini, Gemma, Llama-3, Qwen, Deep... |
| 121 | [[2025-Jamshidi-MoCoP]] | GPT-4, DeepSeek |
| 122 | [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]] | GPT-3, GPT-3.5, GPT-4, T5 |
| 123 | [[2025-Kasu-EthicsMH]] | ChatGPT |
| 124 | [[2025-Khan-Randomness Not Representation The Unreliability of Evaluating]] | GPT-4, Claude, Gemini, Llama-3, Mistral |
| 125 | [[2025-Kilov-Discerning What Matters]] | Llama-3, GPT-4, DeepSeek, Gemini, Claude |
| 126 | [[2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language]] | Gemini, Claude, DeepSeek, Qwen, Grok |
| 127 | [[2025-Lan-McBE]] | Qwen, Llama-2, Mistral, ChatGPT |
| 128 | [[2025-Laukkonen-Contemplative Artificial Intelligence]] | GPT-4 |
| 129 | [[2025-Lee-When Prompting Fails to Sway]] | Claude, GPT-4, GPT-3.5, Llama-3 |
| 130 | [[2025-Li-Analyzing Cognitive Differences Among Large]] | GPT-4o, Qwen, Llama-3, Gemma, Gemini, DeepSeek, Phi |
| 131 | [[2025-Liu-Cross-cultural value alignment frameworks]] | GPT-4o, GPT-3.5, Claude, Llama-3, Llama-2, Mistral, Mixtr... |
| 132 | [[2025-Liu-Diagnosing Moral Reasoning Acquisition in]] | Mistral, Llama-3, BERT |
| 133 | [[2025-Liu-On the Convergence of Moral Self-Correction in LLMs]] | Mistral, GPT-4 |
| 134 | [[2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences]] | GPT-4, o3 |
| 135 | [[2025-Machlovi-GuardEval]] | Gemma, Llama-3 |
| 136 | [[2025-Mao-ALYMPICS LLM Agents Meet Game Theory]] | GPT-4 |
| 137 | [[2025-Mazeika-Utility Engineering]] | GPT-4, GPT-3.5, Llama-2, Llama-3, Gemma, Qwen |
| 138 | [[2025-Menke-How Effective Is Constitutional AI in Small LLMs]] | DeepSeek, Gemma, Llama-3, Qwen |
| 139 | [[2025-Mohammadi-EvalMORAAL]] | GPT-4, GPT-3.5, Claude, Gemini, PaLM-2, Llama-3, Qwen, Mi... |
| 140 | [[2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language]] | GPT-4, GPT-3.5, GPT-2, OPT, BLOOM, Qwen, Gemma, Llama-2, ... |
| 141 | [[2025-Mohammed-Aftina]] | Gemini, Gemma |
| 142 | [[2025-Molchanova-Exploring the Potential of Large Language Models]] | GPT-4, GPT-3.5, Mixtral, Claude |
| 143 | [[2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human]] | GPT-4, Mistral, Llama-3, Qwen |
| 144 | [[2025-Mushtaq-WorldView-Bench]] | GPT-4, Claude, Llama-3, Mistral, Gemini, DeepSeek |
| 145 | [[2025-Nadeem-Ethical Decision-Making in Humans and Large]] | GPT-4, Gemini, DeepSeek |
| 146 | [[2025-Naik-AgentMisalignment]] | GPT-4, Claude, Gemini |
| 147 | [[2025-Narnaware-SB-Bench]] | GPT-4, Llama-3, Gemma, Qwen, Gemini, Phi |
| 148 | [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]] | GPT-4, Llama, Claude, Gemini, Mistral |
| 149 | [[2025-Neuman-Auditing the Ethical Logic of Generative AI Models]] | GPT-4, Llama, Claude, Gemini, Mistral, DeepSeek |
| 150 | [[2025-Neuman-PRIME Framework Convergent Ethics]] | GPT-4, Llama, Claude, Gemini, Mistral |
| 151 | [[2025-Oh-Robustness of Large Language Models in Moral Judgements]] | GPT-3.5 |
| 152 | [[2025-Palta-Speaking the Right Language]] | GPT-4 |
| 153 | [[2025-Park-Deontological Keyword Bias]] | GPT-4, Llama-3, Gemma, Qwen |
| 154 | [[2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs]] | GPT-4, Gemma, DeepSeek, Llama-3, Claude, Gemini |
| 155 | [[2025-Pourbahman-ELAB]] | Mistral, Qwen, Gemma, Llama-3 |
| 156 | [[2025-Rashid-Evaluating Prompt Injection Attacks with]] | Llama-3, GPT-4 |
| 157 | [[2025-Rozen-Do LLMs Have Consistent Values]] | GPT-4, Gemini, Llama-3, Gemma |
| 158 | [[2025-Russo-The Pluralistic Moral Gap]] | GPT-4, ChatGPT, Claude, Mistral, Llama-3, Qwen |
| 159 | [[2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas]] | GPT-4, GPT-3.5, Claude, PaLM-2, Llama-2, Mistral, Gemma |
| 160 | [[2025-Sameer-Insights into Moral Reasoning of AI]] | ChatGPT, GPT-4 |
| 161 | [[2025-Sel-Backtracking for Safety]] | Gemma, Llama-3 |
| 162 | [[2025-Shah-LLM Rationalis Measuring Bargaining Capabilities of AI Negotiators]] | GPT-4, ChatGPT |
| 163 | [[2025-Shahriar-Priv-IQ]] | Claude, DeepSeek, Gemini, GPT-4 |
| 164 | [[2025-Sorensen-Value Profiles for Encoding Human Variation]] | Gemma, Gemini |
| 165 | [[2025-Su-Understanding How Value Neurons Shape the]] | Llama-3, Qwen, Gemma |
| 166 | [[2025-Suh-SENSE-7 Taxonomy and Dataset for Measuring User Perceptions of]] | GPT-4, GPT-3.5, Llama-2 |
| 167 | [[2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM]] | GPT-3.5, GPT-4, Gemini, Llama-3, DeepSeek, Qwen |
| 168 | [[2025-Tereshchenko-A Comparative Analysis of Ethical and Safety Gaps]] | GPT-4, GPT-3.5, o1, o3, Gemini, DeepSeek |
| 169 | [[2025-Tsvetkov-Democracy-in-Silico Institutional Design as Alignment]] | GPT-4, DeepSeek |
| 170 | [[2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning]] | GPT-4, Llama-3, DeepSeek, Qwen |
| 171 | [[2025-Wang-Measuring Desired Group Discrimination in LLMs]] | GPT-4, Claude, Llama-3, Mistral, Gemma |
| 172 | [[2025-Wang-Multimodal Understanding of Human Values in Videos]] | Gemini, Mistral, RoBERTa, DeBERTa |
| 173 | [[2025-Wu-Chain-of-Ethics Defense Framework Wu et al.]] | GPT-4, GPT-4o, Claude, Gemini, DeepSeek, Qwen |
| 174 | [[2025-Ye-GPLA Generative Psycho-Lexical Approach for Constructing Value Systems]] | GPT-4, GPT-3.5, GPT-4o, Llama-2, Llama-3, Mistral, Qwen, ... |
| 175 | [[2025-Yesil-Yesil o1 Pro]] | GPT-4, Claude, DeepSeek, Llama-3, Gemini |
| 176 | [[2025-Zhang-MedHallTune]] | GPT-4, Qwen, Vicuna, Llama-2, Flan-T5 |
| 177 | [[2025-Zhang-PoliCon]] | GPT-4, Gemini, Qwen, Llama-3, DeepSeek |
| 178 | [[2025-Zhang-REVAL]] | GPT-4, Gemini, OPT, Vicuna, Llama-2, Flan-T5, Qwen, Phi |
| 179 | [[2025-Zhu-EAVIT]] | GPT-4, Llama-2, BERT |
| 180 | [[2025-Zhu-Steering Risk Preferences in Large Language]] | Gemma |
| 181 | [[2025-Zulaika-BasqBBQ Basque BBQ]] | BERT, RoBERTa, ALBERT |
| 182 | [[2026-Chen-PoliBias Parliamentary Voting Records]] | Mistral, Falcon, Gemma, DeepSeek, GPT-3.5, GPT-4, Llama-2... |
| 183 | [[2026-Elkins-Negation Sensitivity Index NSI]] | GPT-4, Claude, Gemini, Grok, DeepSeek, Qwen, Llama, Gemma... |
| 184 | [[2026-Huang-Knowing But Not Doing Convergent Morality and Divergent Action in]] | GPT-4, Gemini, Claude, Grok, Llama, Qwen, DeepSeek |
| 185 | [[2026-Kim-VALUEFLOW Toward Pluralistic and Steerable Value-based Alignment in]] | GPT-4, Claude, Gemini, Grok, Qwen, Mistral, Phi, Gemma |
| 186 | [[2026-Liu-JMedEthicBench]] | GPT-4, Claude, Gemini, DeepSeek, Qwen, Llama-3, Grok |
| 187 | [[2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs]] | GPT-4, Claude, Gemini, DeepSeek, Qwen, Llama-3 |
| 188 | [[2026-Nadeem-Bias Beyond Borders]] | Mistral, DeepSeek |

</details>

### 4.2 Papers with Data URLs but No LLM Models Identified

**214 papers** have public data URLs but no LLM model assessment.

<details>
<summary>Click to expand (214 papers)</summary>

| # | Paper | Data URL |
|--:|-------|----------|
| 1 | [[0000-collections-JainGPT AI-Powered Chatbot for Jain Literature]] | https://jainknowledge.com / https://jaingpt.org/ |
| 2 | [[0000-project-Vedanta Datasets]] | https://github.com/atmabodha/Vedanta_Datasets |
| 3 | [[0000-projects-BaniDB Shabad OS Digital Gurbani Database]] | https://github.com/KhalisFoundation/banidb-api / https://github.com... |
| 4 | [[2010-Project-GurbaniDB]] | https://github.com/sikher/gurbanidb |
| 5 | [[2016-Purzycki-Cross-cultural dataset for the evolution of]] | https://doi.org/10.7910/DVN/ERKCLS |
| 6 | [[2018-Awad-The Moral Machine experiment]] | https://goo.gl/JXRrBP |
| 7 | [[2018-Behzadan-TrolleyMod v1.0]] | https://github.com/zminton/TrolleyMod/wiki |
| 8 | [[2018-Crone-The Socio-Moral Image Database (SMID)]] | https://osf.io/2rqad/ |
| 9 | [[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]] | https://github.com/conversationai/unintended-ml-bias-analysis |
| 10 | [[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]] | http://saifmohammad.com/WebPages/Biases-SA.html |
| 11 | [[2018-Mishra-Are They Our Brothers Analysis and]] | https://github.com/nuhaalbadi/Arabic_hatespeech |
| 12 | [[2018-Zhao-Finding Answers from the Word of God]] | https://github.com/helen-jiahe-zhao/BibleQA |
| 13 | [[2018-Zhao-Gender Bias in Coreference Resolution]] | https://github.com/rudinger/winogender-schemas |
| 14 | [[2019-De-Arteaga-Bias in Bios]] | http://aka.ms/biasbios |
| 15 | [[2019-Ibrohim-Multi-label Hate Speech and Abusive Language]] | https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusi... |
| 16 | [[2020-Awad-Universals and variations in moral decisions made]] | https://bit.ly/2Y7Brr9 |
| 17 | [[2020-Schramowski-The Moral Choice Machine]] | https://github.com/ml-research/moral-choice-machine-v2 |
| 18 | [[2020-Srivastava-A Multi-Dimensional View of Aggression when]] | https://github.com/arjitsrivastava/MultidimensionalViewOpinionMining |
| 19 | [[2020-Whaanga-Indigenous Protocol and Artificial Intelligence Position]] | https://www.indigenous-ai.net/position-paper/ |
| 20 | [[2020-Yasseri-Detecting Weak and Strong Islamophobic Hate]] | https://github.com/bvidgen/Weak_strong_Islamophobia |
| 21 | [[2020-team-IndicNLPSuite Monolingual Corpora Evaluation Benchmarks and]] | https://github.com/AI4Bharat/indicnlp_catalog |
| 22 | [[2021-Cao-Toward Gender-Inclusive Coreference Resolution]] | https://github.com/TristaCao/into_inclusivecoref |
| 23 | [[2021-Croce-RobustBench]] | https://github.com/RobustBench/robustbench |
| 24 | [[2021-Mohit Chandra-Subverting the Jewtocracy Online Antisemitism Detection]] | https://github.com/mohit3011/Online-Antisemitism-Detection-Using-Mu... |
| 25 | [[2021-Nutanong-WangchanBERTa Pretraining transformer-based Thai Language Models]] | https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased |
| 26 | [[2021-Ravikiran-DOSA Dravidian Code-Mixed Offensive Span Identification]] | https://github.com/manikandan-ravikiran/dosa |
| 27 | [[2021-Saha-Hate-AlertDravidianLangTech-EACL2021 Ensembling Strategies for Transformer-based Offensive]] | https://github.com/hate-alert/Hate-Alert-DravidianLangTech |
| 28 | [[2021-Sogaard-Itihasa A Large-Scale Corpus for Sanskrit]] | https://github.com/rahular/itihasa |
| 29 | [[2021-authors-MasakhaNER Named Entity Recognition for African]] | https://github.com/masakhane-io/masakhane-ner |
| 30 | [[2021-collaborators-Optimisation of the Largest Annotated Tibetan]] | https://zenodo.org/records/3951503 ; https://github.com/lothelanor/... |
| 31 | [[2022-Alsuhaibani-Fabricated Hadith Detection A Novel Matn-Based]] | MAHADDAT dataset (released with paper) |
| 32 | [[2022-Atwell-Challenging the Transformer-based Models with a]] | https://github.com/ShathaTm/Quran_Hadith_Datasets |
| 33 | [[2022-Bago-Situational factors shape moral judgments in the]] | https://github.com/marton-balazs-kovacs/trolleyMultilabReplication |
| 34 | [[2022-Bai-Constitutional AI]] | https://github.com/anthropics/ConstitutionalHarmlessnessPaper |
| 35 | [[2022-Bai-Training a Helpful and Harmless Assistant with]] | https://github.com/anthropics/hh-rlhf |
| 36 | [[2022-Brazdil-NaijaSenti A Nigerian Twitter Sentiment Corpus]] | https://huggingface.co/datasets/HausaNLP/NaijaSenti-Twitter |
| 37 | [[2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language]] | https://github.com/bharathichezhiyan/DravidianCodeMix-Dataset |
| 38 | [[2022-Emezue-AfroLM A Self-Active Learning-based Multilingual Pretrained]] | https://huggingface.co/bonadossou/afrolm_active_learning |
| 39 | [[2022-Ganguli-Red Teaming Language Models to Reduce Harms]] | https://github.com/anthropics/hh-rlhf |
| 40 | [[2022-Hate-speech-CNERG-Kannada Code-Mixed Abusive Speech Detection]] | https://huggingface.co/Hate-speech-CNERG/kannada-codemixed-abusive-... |
| 41 | [[2022-Joshi-L3Cube-MahaNLP Marathi Natural Language Processing Datasets]] | https://github.com/l3cube-pune/MarathiNLP |
| 42 | [[2022-Kann-AmericasNLI]] | https://github.com/abteen/americasnli |
| 43 | [[2022-Kulkarni-Semantic and Sentiment Analysis of Selected]] | https://github.com/sydney-machine-learning/sentimentanalysis_bhagav... |
| 44 | [[2022-Multiple Data in Brief-Sanadset 650K Data on Hadith Narrators]] | https://data.mendeley.com/datasets/5xth87zwb5/4 |
| 45 | [[2022-Pollak-Embeddings Models for Buddhist Sanskrit]] | https://figshare.com/articles/code/Gitlab_repository_of_Embeddings_... |
| 46 | [[2022-Schramowski-I2P Inappropriate Image Prompts Test Bed]] | https://github.com/ml-research/Q16 |
| 47 | [[2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case]] | https://github.com/google-research-datasets/nlp-fairness-for-india |
| 48 | [[2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain]] | https://huggingface.co/datasets/ctoraman/large-scale-hate-speech-tu... |
| 49 | [[2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech]] | https://github.com/l3cube-pune/MarathiNLP |
| 50 | [[2023-2023-Hadiths Classification Using a Novel Author-Based]] | Papers with Code listing |
| 51 | [[2023-Abhinand-Tamil-Llama A New Tamil Language Model]] | https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.2 |
| 52 | [[2023-Alsalka-HAQA and QUQA Constructing Two Arabic]] | https://aclanthology.org/2023.ranlp-1.10/ |
| 53 | [[2023-Alsalka-Is GPT-4 a Good Islamic Expert]] | QUQA dataset (available via thesis/ACL) |
| 54 | [[2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas]] | https://github.com/ohoud/Fatwaset.git |
| 55 | [[2023-Andrus-Augmented Datasheets for Speech Datasets and]] | https://github.com/SonyResearch/project_ethics_augmented_datasheets... |
| 56 | [[2023-Aroyo-DICES Dataset]] | https://github.com/google-research-datasets/dices-dataset/ |
| 57 | [[2023-Barrett-Skin Deep]] | https://github.com/Social-Futures-Lab/skin-deep |
| 58 | [[2023-Chang-A Survey on Evaluation of Large Language Models]] | https://github.com/MLGroupJLU/LLM-eval-survey |
| 59 | [[2023-Feng-Case Repositories]] | https://github.com/social-futures-lab/case-law-ai-policy |
| 60 | [[2023-Goyal-SanskritShala A Neural Sanskrit NLP Toolkit]] | https://cnerg.iitkgp.ac.in/sanskritshala / https://github.com/Jivne... |
| 61 | [[2023-Gustafson-FACET]] | https://facet.metademolab.com |
| 62 | [[2023-Han-FFB]] | https://github.com/ahxt/fair_fairness_benchmark |
| 63 | [[2023-Hopp-The Dutch Moral Foundations Stimulus Database]] | https://osf.io/9gnza |
| 64 | [[2023-Inciarte-SERENGETI Massively Multilingual Language Models for]] | https://huggingface.co/UBC-NLP/serengeti-E250 |
| 65 | [[2023-Ji-Safety Gymnasium]] | https://sites.google.com/view/safety-gymnasium |
| 66 | [[2023-Kahira-AfriQA Cross-lingual Open-Retrieval Question Answering for]] | https://huggingface.co/datasets/masakhane/afriqa |
| 67 | [[2023-Keutzer-MITRA-zh An Efficient Open Machine Translation]] | Open-source (Dharmamitra project) |
| 68 | [[2023-Khan-The Tarteel Dataset Crowd-Sourced and Labeled]] | Tarteel.ai / Quranic Universal Library |
| 69 | [[2023-Kuriyozov-Text classification dataset and analysis for]] | https://github.com/elmurod1202/textclassification |
| 70 | [[2023-Lee-VisAlign]] | https://github.com/jiyounglee-0523/VisAlign |
| 71 | [[2023-Li-ACLUE Can Large Language Model Comprehend]] | https://github.com/isen-zhang/ACLUE ; https://huggingface.co/datase... |
| 72 | [[2023-Moss-Bias on Demand]] | https://github.com/koenecke/crosscultural_labelconsistency/ |
| 73 | [[2023-Muhammad-AfriSenti]] | https://github.com/afrisenti-semeval/afrisent-semeval-2023 |
| 74 | [[2023-Muhammad-SemEval-2023 Task 12]] | https://github.com/afrisenti-semeval/afrisent-semeval-2023 |
| 75 | [[2023-Multiple authors-SAHAAYAK 2023 The Multi-Domain Bilingual Parallel]] | Public domain release |
| 76 | [[2023-Patel-Building Domain-Specific LLMs Faithful To The]] | https://github.com/shabazpatel/domain-specific-llm |
| 77 | [[2023-Qiu-Large AI Models in Health Informatics]] | https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models |
| 78 | [[2023-Schwarting-The eBible Corpus Data and Model]] | https://huggingface.co/datasets/bible-nlp/biblenlp-corpus / https:/... |
| 79 | [[2023-Soemer-Antisemitic Messages A Guide to High-Quality]] | https://zenodo.org/records/7932888 |
| 80 | [[2023-Susanto-BHASA A Holistic Southeast Asian Linguistic]] | https://github.com/aisingapore/BHASA |
| 81 | [[2023-University-Antisemitism on Twitter A Dataset for]] | https://zenodo.org/records/7932888 |
| 82 | [[2023-[[Unknown]]-NEHATE Large-Scale Annotated Data Shedding Light]] | https://github.com/shucoll/NEHate |
| 83 | [[2023-Yao-From Instructions to Intrinsic Human Values -- A]] | https://github.com/ValueCompass/Alignment-Goal-Survey |
| 84 | [[2023-Zhang-WYWEB A NLP Evaluation Benchmark for]] | https://github.com/baudzhou/WYWEB |
| 85 | [[2023-team-SeaLLMs Large Language Models for Southeast]] | https://huggingface.co/SeaLLMs |
| 86 | [[2024-Adilazuarda-Towards Measuring and Modeling ]] | https://github.com/faridlazuarda/cultural-llm-papers |
| 87 | [[2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith]] | https://data.mendeley.com/datasets/gzprcr93zn/2 |
| 88 | [[2024-Azerbaijan-Azerbaijani Toxicity Classifier]] | https://huggingface.co/LocalDoc/azerbaijani_toxicity_classifier |
| 89 | [[2024-Bang-BLEnD A Benchmark for LLMs on]] | https://github.com/nlee0212/BLEnD |
| 90 | [[2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance]] | https://github.com/InstituteforDiseaseModeling/Bridging-the-Gap-Low... |
| 91 | [[2024-Choi-CaLMQA Exploring culturally specific long-form question]] | https://huggingface.co/datasets/shanearora/CaLMQA |
| 92 | [[2024-Defrance-ABCFair]] | https://github.com/aida-ugent/abcfair |
| 93 | [[2024-Dou-SailCompass Towards Reproducible and Robust Evaluation]] | https://huggingface.co/datasets/sail/Sailcompass_data |
| 94 | [[2024-Group-The AI Safety Benchmark]] | https://github.com/mlcommons/modelbench |
| 95 | [[2024-Hooker-Global MMLU Understanding and Addressing Cultural]] | https://huggingface.co/papers/2412.03304 |
| 96 | [[2024-Jin-WenMind A Comprehensive Benchmark for Evaluating]] | https://github.com/SCUT-DLVCLab/WenMind ; https://huggingface.co/da... |
| 97 | [[2024-Jones-Fit for Our Purpose Not Yours]] | https://papareo.nz/ |
| 98 | [[2024-Keutzer-One Model is All You Need]] | https://github.com/sebastian-nehrdich/byt5-sanskrit-analyzers ; htt... |
| 99 | [[2024-Koppel-Adapting LLMs to Hebrew Unveiling DictaLM]] | https://huggingface.co/dicta-il/dictalm2.0 |
| 100 | [[2024-LLM-Beetle-Azerbaijani LLM Leaderboard]] | https://huggingface.co/spaces/LLM-Beetle/azerbaijani-llm-leaderboard |
| 101 | [[2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling]] | https://github.com/MikeLasz/Benchmarking-Fairness-ImageUpsampling |
| 102 | [[2024-Levine-Religious Affiliation and Conceptions of the]] | https://github.com/sydneylevine/moral-domain |
| 103 | [[2024-Lin-AI-Face]] | https://github.com/Purdue-M2/AI-Face-FairnessBench |
| 104 | [[2024-MLCommons-MLCommons AILuminate Benchmark]] | https://github.com/mlcommons/ailuminate |
| 105 | [[2024-Mago-Classification of Buddhist Verses The Efficacy]] | Dataset provided for further study (per paper) |
| 106 | [[2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub]] | https://huggingface.co/SEACrowd |
| 107 | [[2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented]] | https://github.com/priyankamandikal/vedantany-10m / https://sites.g... |
| 108 | [[2024-Mazzara-Quranic Audio Dataset Crowdsourced and Labeled]] | https://huggingface.co/datasets/RetaSy/quranic_audio_dataset |
| 109 | [[2024-Moon-BEAF]] | https://beafbench.github.io/ |
| 110 | [[2024-Multiple Data in Brief-MASAQ Morphologically-Analyzed and Syntactically-Annotated Quran Dataset]] | https://data.mendeley.com/datasets/9yvrzxktmr |
| 111 | [[2024-Myers-People Expect Artificial Moral Advisors]] | https://osf.io/m3v48/ |
| 112 | [[2024-Overfit-GM-Turkish Overfit-GM Toxic Language Dataset]] | https://huggingface.co/datasets/Overfit-GM/turkish-toxic-language |
| 113 | [[2024-Phyo-Development and Evaluation of Myanmar GPT]] | https://huggingface.co/jojo-ai-mst/MyanmarGPT |
| 114 | [[2024-Porkaew-Representing the Under-Represented Cultural and Core]] | https://github.com/UpstageAI/ThaiCLI_H6 |
| 115 | [[2024-Rauh-Gaps in the Safety Evaluation of Generative AI]] | https://dpmd.ai/EvalsRepo |
| 116 | [[2024-Reuel-BetterBench]] | https://betterbench.stanford.edu |
| 117 | [[2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety]] | https://github.com/paul-rottger/safetyprompts-paper |
| 118 | [[2024-SUTD-Sailor Open Language Models for South-East]] | https://github.com/sail-sg/sailor-llm |
| 119 | [[2024-Sadhu-Social Bias in Large Language Models]] | Publicly available (code and resources) |
| 120 | [[2024-Sang-CDEval A Benchmark for Measuring the]] | https://huggingface.co/datasets/Rykeryuhang/CDEval | https://github... |
| 121 | [[2024-Schutze-TurkishMMLU Measuring Massive Multitask Language Understanding]] | https://github.com/ArdaYuksel/TurkishMMLU |
| 122 | [[2024-Shen-EmpathicStories++ A Multimodal Dataset for Empathy towards Personal]] | https://mitmedialab.github.io/empathic-stories-multimodal/ |
| 123 | [[2024-Shi-Large Language Model Safety]] | https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers |
| 124 | [[2024-Singh-IndicGenBench A Multilingual Benchmark to Evaluate]] | https://github.com/google-research-datasets/indic-gen-bench |
| 125 | [[2024-Singhal-AyaRedTeaming]] | https://huggingface.co/datasets/CohereForAI/aya_redteaming |
| 126 | [[2024-Singla-Samayik A Benchmark and Dataset for]] | https://github.com/ayushbits/saamayik |
| 127 | [[2024-So-How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas]] | https://github.com/famous-blue-raincoat/AI_Ethics_Discourse |
| 128 | [[2024-Tennant-Dynamics of Moral Behavior in Heterogeneous Populations]] | https://github.com/Liza-Tennant/moral_MARL |
| 129 | [[2024-Tharnpipitchai-Typhoon 2 A Family of Open]] | https://huggingface.co/scb10x/typhoon2-safety-preview |
| 130 | [[2024-Tonneau-Turkish Hate Speech Superset Dataset]] | https://huggingface.co/datasets/manueltonneau/turkish-hate-speech-s... |
| 131 | [[2024-Toygar-Turkish Offensive Language Detection Dataset]] | https://huggingface.co/datasets/Toygar/turkish-offensive-language-d... |
| 132 | [[2024-Ungless-ETHICS WHITEPAPER]] | https://github.com/MxEddie/Ethics-Whitepaper |
| 133 | [[2024-Vladimirova-FairJob]] | https://huggingface.co/datasets/criteo/FairJob |
| 134 | [[2024-Wong-The Humanistic Buddhism Corpus (HBC)]] | https://www.fgstranslation.org/hbc |
| 135 | [[2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding]] | https://github.com/yuting-wei/AC-EVAL |
| 136 | [[2024-Xie-CultureLLM Incorporating Cultural Differences into Large]] | https://github.com/Scarelette/CultureLLM |
| 137 | [[2024-Yakunin-Kazakh Dastur-MC Multiple Choice Benchmark on]] | https://huggingface.co/datasets/kz-transformers/kazakh-dastur-mc |
| 138 | [[2024-Yolgoermez-Abundant Intelligences Placing AI Within Indigenous]] | https://www.indigenous-ai.net/ ; https://abundant-intelligences.net/ |
| 139 | [[2024-Zeng-LLM-GLOBE A Benchmark Evaluating the Cultural]] | https://github.com/raovish6/LLM-GLOBE |
| 140 | [[2024-Zhang-CHiSafetyBench]] | https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench |
| 141 | [[2024-authors-CVQA Culturally-diverse Multilingual Visual Question Answering]] | https://cvqa-benchmark.org/ |
| 142 | [[2024-project-DharmicData Comprehensive Open-Source Collection of Hindu]] | https://github.com/bhavykhatri/DharmicData (ODbL license) |
| 143 | [[2024-team-Indic-Bias A Comprehensive Benchmark for Fairness]] | https://huggingface.co/datasets/ai4bharat/Indic-Bias |
| 144 | [[2024-team-Indic-Bias A Comprehensive Benchmark to Evaluate]] | https://github.com/AI4Bharat/indic-bias |
| 145 | [[2024-team-IndicLLMSuite A Blueprint for Creating Pre-training]] | https://huggingface.co/datasets/ai4bharat/indic-align |
| 146 | [[2024-team-MahaMarathi-7B Marathi Large Language Model]] | https://huggingface.co/marathi-llm/MahaMarathi-7B-v24.01-Base |
| 147 | [[2024-team-OpenThaiGPT 15 A Thai-Centric Open Source]] | https://huggingface.co/openthaigpt |
| 148 | [[2024-Ògúnrẹ̀mí-ÌròyìnSpeech A Multi-purpose Yorùbá Speech Corpus]] | https://github.com/Niger-Volta-LTI/yoruba-voice |
| 149 | [[2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias]] | https://www.adl.org/resources/report/generating-hate-anti-jewish-an... |
| 150 | [[2025-Abdul-Mageed-Where Are We Evaluating LLM Performance]] | https://africa.dlnlp.ai/sahara/ (public leaderboard) |
| 151 | [[2025-Adelani-INJONGO A Multicultural Intent Detection and]] | https://huggingface.co/collections/McGill-NLP/injongo-683240ae2323f... |
| 152 | [[2025-Ajwad Abrar-Religious Bias Landscape in Language and]] | https://github.com/ajwad-abrar/Religious-Bias (prompts and images p... |
| 153 | [[2025-Alwajih-PalmX 2025 - First Shared Task on Benchmarking LLMs on Arabic and]] | https://github.com/UBC-NLP/palmx_2025 |
| 154 | [[2025-Anderson-Model Misalignment and Language Change]] | https://github.com/fsu-nlp/ai-traces-ssl |
| 155 | [[2025-Asgari-I Am Aligned But With Whom]] | https://github.com/llm-lab-org/MENA-Values-Benchmark-Evaluating-Cul... |
| 156 | [[2025-Bar-DharmaBench Evaluating Language Models on Buddhist]] | Publicly released under CC-BY-4 License (code under Apache-2.0) |
| 157 | [[2025-Barov-TUMLU A Unified and Native Language]] | https://github.com/ceferisbarov/TUMLU |
| 158 | [[2025-Bogoychev-MultiLoKo A Multilingual Local Knowledge Benchmark]] | https://github.com/facebookresearch/multiloko |
| 159 | [[2025-Center-Personal Consultations Case Study Database]] | https://www.ncbcenter.org/case-study-database |
| 160 | [[2025-Chaudhari-RLHF Deciphered]] | https://github.com/GaryYufei/AlignLLMHumanSurvey |
| 161 | [[2025-Chen-AVHBench]] | https://github.com/kaist-ami/AVHBench |
| 162 | [[2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment]] | https://github.com/Social-Futures-Lab/SPICA-code |
| 163 | [[2025-Coalition-The Gospel Coalition AI Christian Benchmark]] | https://www.thegospelcoalition.org/ai-christian-benchmark/ |
| 164 | [[2025-Emezue-NaijaVoices]] | https://naijavoices.com/ |
| 165 | [[2025-Erdem-Cetvel A Unified Benchmark for Evaluating]] | https://huggingface.co/spaces/KUIS-AI/Cetvel |
| 166 | [[2025-Ezeani-AfriStereo A Culturally Grounded Dataset for]] | Open-source (CC BY 4.0) |
| 167 | [[2025-Ghaly-Assessing Large Language Models on Islamic]] | https://github.com/bouchekif/inheritance_evaluation |
| 168 | [[2025-Goyal-Vedavani A Benchmark Corpus for ASR]] | https://huggingface.co/datasets/sanganaka/Vedavani-Dataset |
| 169 | [[2025-Griffiths-Explicitly Unbiased Large Language Models Still]] | LLM Word Association Test, LLM Relative Decision Test (methodologic... |
| 170 | [[2025-Keutzer-MITRA-zh-eval Using a Buddhist Chinese Language]] | https://aclanthology.org/2025.nlp4dh-1.12/ |
| 171 | [[2025-Kneer-Hard Problem AI Alignment Value Forks]] | https://osf.io/rqkcz |
| 172 | [[2025-Lan-Fuxi A Benchmark for Evaluating Language]] | Benchmark, evaluation toolkit, and baseline results publicly availa... |
| 173 | [[2025-Mahran-Mechanistic Interpretability with SAEs Probing Religion]] | Uses Neuronpedia API |
| 174 | [[2025-Maji-DRISHTIKON A Multimodal Multilingual Benchmark for]] | https://huggingface.co/datasets/13ari/DRISHTIKON |
| 175 | [[2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks]] | https://github.com/BenchRisk |
| 176 | [[2025-Mujahid-Qorgau Evaluating LLM Safety in Kazakh-Russian]] | https://github.com/mbzuai-nlp/qorgau-kaz-ru-safety |
| 177 | [[2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting]] | https://github.com/Arwaalmrzoqi/ELQV |
| 178 | [[2025-Ning-seeBias]] | https://github.com/nliulab/seeBias |
| 179 | [[2025-Ousidhoum-AfriHate A Multilingual Collection of Hate]] | https://huggingface.co/papers/2501.08284 |
| 180 | [[2025-Poria-Bhaasha Bhasa Zaban A Survey for]] | https://github.com/trust-nlp/LM4SouthAsia-Survey |
| 181 | [[2025-Qi-A Survey of Automatic Hallucination Evaluation on]] | https://github.com/siyaqi/Awesome-Hallu-Eval |
| 182 | [[2025-Schacht-Mapping Moral Reasoning Circuits]] | https://github.com/coairesearch/mapping_moral_reasoning.git |
| 183 | [[2025-Sekine-AnswerCarefully A Dataset for Improving the]] | https://huggingface.co/datasets/llm-jp/AnswerCarefully |
| 184 | [[2025-[[Unknown]]-SweEval Do LLMs Really Swear A]] | https://huggingface.co/datasets/ariondas/SweEval-Bench |
| 185 | [[2025-Vasilev-RusCode]] | https://github.com/ai-forever/RusCode |
| 186 | [[2025-Verma-MILU A Multi-task Indic Language Understanding]] | https://huggingface.co/datasets/ai4bharat/MILU |
| 187 | [[2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist]] | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| 188 | [[2025-Xiong-BuddhismEval Bilingual Evaluation Benchmark for Buddhist]] | https://huggingface.co/datasets/Nethmi14/BuddhismEval |
| 189 | [[2025-Yanaka-Bias Mitigation or Cultural Commonsense Evaluating]] | Not confirmed from search results |
| 190 | [[2025-Ye-Large Language Model Psychometrics]] | https://github.com/valuebyte-ai/Awesome-LLM-Psychometrics |
| 191 | [[2025-Yimam-CULEMO Cultural Lenses on Emotion --]] | https://github.com/llm-for-emotion/culemo |
| 192 | [[2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark]] | https://github.com/Vicentvankor/sun-shine |
| 193 | [[2025-Yu-TLUE A Tibetan Language Understanding Evaluation]] | https://github.com/Vicentvankor/TLUE |
| 194 | [[2025-Zhang-Evaluating and Improving Cultural Awareness of]] | Not confirmed from search results |
| 195 | [[2025-Zhao-WenyanGPT A Large Language Model for]] | Training data, instruction fine-tuning data, and WenyanBENCH public... |
| 196 | [[2025-authors-IslamTrust A Benchmark for LLMs Alignment]] | https://github.com/aii-lab-dot-org/IslamTrust and https://huggingfa... |
| 197 | [[2025-authors-MMLU-ProX A Multilingual Benchmark for Advanced]] | https://github.com/weihao1115/MMLU-ProX |
| 198 | [[2025-initiative-CatholicBench]] | https://www.catholicbench.com/ |
| 199 | [[2025-initiative-Faith Respect and Moral Compass in]] | In development (collaborating with BYU, Notre Dame, Baylor, Yeshiva) |
| 200 | [[2025-initiative-FaithBench AI Benchmark for Christian Theology]] | https://faithbench.com/ |
| 201 | [[2025-project-Kaku-Ora Zen Wisdom Diffused -- An]] | GitHub (code available); HuggingFace Spaces (model hosted) |
| 202 | [[2025-results]]-BenchMAX A Comprehensive Multilingual Evaluation Suite]] | https://github.com/CONE-MT/BenchMAX |
| 203 | [[2025-team-SEA-LION Southeast Asian Languages in One]] | https://github.com/aisingapore/sealion |
| 204 | [[2025-team-SeaExam and SeaBench Benchmarking LLMs with]] | https://github.com/DAMO-NLP-SG/SeaExam |
| 205 | [[2025-team-WangchanThaiInstruct An Instruction-Following Dataset for Culture-Aware]] | https://huggingface.co/datasets/airesearch/WangchanThaiInstruct |
| 206 | [[2026-Alam-From RAG to Agentic RAG for]] | Planned public release |
| 207 | [[2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset]] | https://huggingface.co/datasets (CC0 license) |
| 208 | [[2026-Dharmamitra-MITRA A Large-Scale Parallel Corpus and]] | Parallel dataset, model weights, and benchmark openly available (Hu... |
| 209 | [[2026-Eickhoff-UbuntuGuard A Culturally-Grounded Policy Benchmark for]] | https://github.com/hemhemoh/UbuntuGuard (CC BY 4.0) |
| 210 | [[2026-Guey-BiasLab Multilingual Dual-Framing Framework]] | https://github.com/williamguey/LLMbiaslab |
| 211 | [[2026-Rehman-X-MuTeST A Multilingual Benchmark for Explainable]] | https://huggingface.co/datasets/UVSKKR/X-MuTeST |
| 212 | [[2026-Smywinski-Pohl-Targum A Multilingual New Testament Translation]] | Code and public-domain subset to be released; copyrighted texts ava... |
| 213 | [[2026-Solorio-Afri-MCQA Multimodal Cultural Question Answering for]] | https://huggingface.co/papers/2601.05699 |
| 214 | [[2026-team-SEA-Guard Culturally Grounded Multilingual Safeguard for]] | https://huggingface.co/aisingapore/Qwen-SEA-Guard-8B-2602 |

</details>

### 4.3 Underrepresented Model Families (< 5 papers)

**2 model families** appear in fewer than 5 papers:

| Family | Papers |
|--------|-------:|
| Embeddings | 3 |
| Other/Unknown | 2 |

---

## Appendix A: Model Family Normalization Table

Canonical mapping used to group model names into families:

| Family | Models |
|--------|--------|
| OpenAI | GPT-4, GPT-4o, GPT-4o mini, GPT-4 Turbo, GPT-3.5, GPT-3, GPT-2, ChatGPT, o1, o1-mini, o1-preview, o3, o3-mini, text-davinci, text-davinci-002, text-davinci-003, InstructGPT, CODEX, GPT-5 |
| Anthropic | Claude, Claude-2, Claude-3, Claude-3 Opus, Claude-3 Sonnet, Claude-3 Haiku, Claude Instant |
| Meta | Llama-3, Llama-2, Llama, LLaMA, CodeLlama, OPT, OPT-175B |
| Google | Gemini, Gemini Pro, Gemini Ultra, Gemini Flash, Gemma, Gemma-2, PaLM-2, PaLM, Flan-T5, Flan-UL2, LaMDA, T5, BARD |
| Mistral AI | Mistral, Mixtral |
| Alibaba | Qwen, Qwen-2, Qwen-1.5 |
| DeepSeek | DeepSeek, DeepSeek-V2, DeepSeek-Coder |
| Microsoft | Phi, Phi-2, Phi-3 |
| xAI | Grok |
| Cohere | Cohere, Command-R, Command R+, Aya |
| AI21 | Jurassic, Jurassic-2, J2 |
| Open-source (misc) | Vicuna, Alpaca, Falcon, BLOOM, Yi, Dolly, Zephyr, WizardLM, InternLM, Baichuan, ChatGLM, GLM, StableLM, MPT, DialoGPT, Delphi, ERNIE |
| Pre-LLM / Encoder | BERT, RoBERTa, ALBERT, DeBERTa, DistilBERT, XLNet, ELECTRA, ELMo, BART |
| Embeddings | Word2Vec, GloVe, FastText |

## Appendix B: Methodology Notes

1. **Data source:** YAML frontmatter fields `LLM_assessed` and `DATA_URL` from all 846 papers in `papers/`
2. **Model extraction:** The `LLM_assessed` field contains comma-separated canonical model names assigned during
   the 40-agent deep-read enrichment pipeline (2026-02-12). Values are pre-canonicalized — this report
   performs no additional NLP extraction.
3. **Family grouping:** Models are mapped to families via a static lookup table (Appendix A). Models not
   found in the table are assigned to "Other/Unknown".
4. **Proprietary vs open-source:** Classification is based on model licensing at time of release.
   Some models (e.g., Llama) have evolving licenses; we classify based on the predominant usage pattern.
5. **URL classification:** DATA_URL values may contain multiple comma-separated URLs. Each paper is counted
   once per platform (even if multiple URLs point to the same platform).
6. **Co-occurrence matrix:** Counts how many papers test both Model A and Model B. Only the top 12 models
   by frequency are included to keep the matrix readable.
