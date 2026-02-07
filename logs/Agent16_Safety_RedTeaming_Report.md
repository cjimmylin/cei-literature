# Agent 16: Safety & Red-Teaming with Ethical Dimensions
## Exhaustive Literature Search Report
**Date:** 2026-02-07
**Domain:** Safety benchmarks, red-teaming datasets, harm taxonomies, agent safety, and benchmark reliability -- all with explicit ethical dimensions for LLM evaluation.

---

## Table of Contents
1. [Safety Benchmarks with Ethical Categories](#1-safety-benchmarks-with-ethical-categories)
2. [Red-Teaming with Ethical Evaluation](#2-red-teaming-with-ethical-evaluation)
3. [Harm Taxonomy Benchmarks](#3-harm-taxonomy-benchmarks)
4. [Agent Safety & Ethics](#4-agent-safety--ethics)
5. [Safetywashing & Benchmark Reliability](#5-safetywashing--benchmark-reliability)
6. [Summary Table](#6-summary-table)

---

## 1. Safety Benchmarks with Ethical Categories

### 1.1 WildGuard (WildGuardTest)

- **Full Citation:** Seungju Han, Kavel Rao, Allyson Ettinger, Liwei Jiang, Bill Yuchen Lin, Nathan Lambert, Yejin Choi, Nouha Dziri. "WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs." NeurIPS 2024 (Datasets and Benchmarks Track).
- **arXiv ID:** [2406.18495](https://arxiv.org/abs/2406.18495)
- **Ethical Frameworks / Harm Categories:** 13 risk subcategories across 4 high-level domains: Privacy, Misinformation, Harmful Language, and Malicious Uses. Aligned with Weidinger et al. taxonomy of ethical and social risks.
- **Dataset Size & Format:**
  - WildGuardMix (training): 92K labeled examples
  - WildGuardTest (evaluation): 5,299 human-annotated items including adversarial jailbreak cases
  - Three tasks: prompt harmfulness detection, response harmfulness detection, response refusal detection
- **Code/Data URLs:**
  - HuggingFace: https://huggingface.co/allenai/wildguard
  - OpenReview: https://openreview.net/forum?id=Ich4tv4202
- **LLMs Tested:** Compared against GPT-4 and 10 open-source moderation models including LlamaGuard2; evaluated on 10 existing public benchmarks
- **Implementation Readiness:** **High** -- Open-source model, benchmark data, and evaluation pipeline publicly available

---

### 1.2 HH-RLHF (Helpful and Harmless RLHF)

- **Full Citation:** Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, Jared Kaplan. "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback." arXiv preprint, 2022.
- **arXiv ID:** [2204.05862](https://arxiv.org/abs/2204.05862)
- **Ethical Frameworks / Harm Categories:** Dual-axis evaluation of helpfulness vs. harmlessness; red-teaming data covers discriminatory language, abuse, violence, self-harm, exploitation, and other ethically concerning content
- **Dataset Size & Format:**
  - ~170K human preference comparisons total
  - 44K helpfulness comparisons + 42K harmlessness comparisons (base)
  - 52K helpfulness + 2K harmlessness (rejection sampling)
  - 22K helpfulness (iterated online from RLHF models)
  - Format: chosen/rejected response pairs
- **Code/Data URLs:**
  - GitHub: https://github.com/anthropics/hh-rlhf
  - HuggingFace: https://huggingface.co/datasets/Anthropic/hh-rlhf
- **LLMs Tested:** Anthropic's internal models (various sizes), used extensively by the community for training and evaluating reward models
- **Implementation Readiness:** **High** -- Widely used foundational dataset; MIT license; directly loadable from HuggingFace

---

### 1.3 JailbreakBench

- **Full Citation:** Patrick Chao, Edoardo Debenedetti, Alexander Robey, Maksym Andriushchenko, Francesco Croce, Vikash Sehwag, Edgar Dobriban, Nicolas Flammarion, George J. Pappas, Florian Tramer, Hamed Hassani, Eric Wong. "JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models." NeurIPS 2024 (Datasets and Benchmarks Track).
- **arXiv ID:** [2404.01318](https://arxiv.org/abs/2404.01318)
- **Ethical Frameworks / Harm Categories:** 100 distinct misuse behaviors divided into 10 broad categories aligned with OpenAI's usage policies; includes 100 benign behaviors for overrefusal evaluation. Categories cover harassment, malware, fraud, deception, illegal activities, hate speech, physical harm, privacy violations, sexual content, and more.
- **Dataset Size & Format:**
  - JBB-Behaviors: 100 harmful + 100 benign behaviors
  - 55% original examples, remainder from AdvBench and TDC/HarmBench
  - Standardized evaluation framework with defined threat model, system prompts, chat templates, scoring functions
- **Code/Data URLs:**
  - GitHub: https://github.com/JailbreakBench/jailbreakbench
  - HuggingFace: https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
  - Leaderboard: https://jailbreakbench.github.io/
- **LLMs Tested:** Llama-3-70B, Llama-3-8B, and various others via leaderboard tracking
- **Implementation Readiness:** **High** -- Complete open-source pipeline with leaderboard, pip-installable package, and standardized evaluation

---

### 1.4 AEGIS 2.0

- **Full Citation:** Shaona Ghosh, Prasoon Varshney, Makesh Narsimhan Sreedhar, Aishwarya Padmakumar, Traian Rebedea, Jibin Rajan Varghese, Christopher Parisien. "Aegis2.0: A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails." NAACL 2025.
- **arXiv ID:** [2501.09004](https://arxiv.org/abs/2501.09004)
- **Ethical Frameworks / Harm Categories:** 12 core hazard categories + 9 fine-grained risk subcategories. Labels: Safe, Needs Caution, or specific risk category. Covers critical safety concerns in human-LLM interactions.
- **Dataset Size & Format:**
  - 33,416 annotated human-LLM interactions (34,248 total samples)
  - Split: 30,007 train / 1,445 validation / 1,964 test
  - Averaged 12 annotators with engineering and linguistics backgrounds
  - First commercial-use-suitable content moderation training dataset
- **Code/Data URLs:**
  - HuggingFace: https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
  - Model: https://huggingface.co/nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0
- **LLMs Tested:** Llama3.1-AegisGuard (outperforms LlamaGuard3-8B, LlamaGuard3-1B, LlamaGuard2-8B, and OpenAI Moderation API); responses generated by Mistral-7B-v0.1
- **Implementation Readiness:** **High** -- Dataset and models publicly available on HuggingFace; commercially licensable

---

### 1.5 SORRY-Bench

- **Full Citation:** Tinghao Xie, Xiangyu Qi, Yi Zeng, Yangsibo Huang, Udari Madhushani Sehwag, Kaixuan Huang, Luxi He, Boyi Wei, Dacheng Li, Ying Sheng, Ruoxi Jia, Bo Li, Kai Li, Danqi Chen, Peter Henderson, Prateek Mittal. "SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal." ICLR 2025.
- **arXiv ID:** [2406.14598](https://arxiv.org/abs/2406.14598)
- **Ethical Frameworks / Harm Categories:** 44 fine-grained potentially unsafe topics organized into a balanced taxonomy addressing imbalances in prior benchmarks (e.g., under-representation of self-harm instructions). Supplemented with 20 linguistic augmentations (writing styles, persuasion techniques, encoding schemes, non-English languages).
- **Dataset Size & Format:**
  - 440 class-balanced unsafe instructions (10 per category)
  - 20 linguistic augmentations per instruction
  - 7K+ human annotations for meta-evaluation
  - Fine-tuned 7B judge LLMs achieving GPT-4-level accuracy
- **Code/Data URLs:**
  - Website: https://sorry-bench.github.io
  - GitHub: https://github.com/SORRY-Bench/sorry-bench
- **LLMs Tested:** Over 50 proprietary and open-weight LLMs evaluated
- **Implementation Readiness:** **High** -- Complete evaluation pipeline with data, code, models, and demo publicly available

---

### 1.6 SG-Bench

- **Full Citation:** Yutao Mou, Shikun Zhang, Wei Ye. "SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types." NeurIPS 2024 (Datasets and Benchmarks Track).
- **arXiv ID:** [2410.21965](https://arxiv.org/abs/2410.21965)
- **Ethical Frameworks / Harm Categories:** 6 types of safety issues evaluated across both generative and discriminative paradigms. Examines impact of prompt engineering techniques (system prompts, few-shot demonstrations, chain-of-thought) and jailbreak attacks on safety.
- **Dataset Size & Format:**
  - 1,442 malicious queries from diverse sources
  - Three test task types: open-end generation, multiple-choice questions, safety judgments
  - Covers multiple prompt engineering and jailbreak attack techniques
- **Code/Data URLs:**
  - GitHub: https://github.com/MurrayTom/SG-Bench
- **LLMs Tested:** 3 advanced proprietary LLMs + 10 open-source LLMs
- **Implementation Readiness:** **High** -- Open-source benchmark with evaluation code

---

### 1.7 SafetyBench

- **Full Citation:** Zhexin Zhang, Leqi Lei, Lindong Wu, Rui Sun, Yongkang Huang, Chong Long, Xiao Liu, Xuanyu Lei, Jie Tang, Minlie Huang. "SafetyBench: Evaluating the Safety of Large Language Models." ACL 2024 (Main Conference).
- **arXiv ID:** [2309.07045](https://arxiv.org/abs/2309.07045)
- **Ethical Frameworks / Harm Categories:** 7 distinct safety concern categories. Bilingual (Chinese and English) evaluation covering safety understanding that correlates with safety generation.
- **Dataset Size & Format:**
  - 11,435 diverse multiple-choice questions
  - 7 safety categories
  - Both Chinese and English data
  - Automated evaluation via MCQ format
- **Code/Data URLs:**
  - GitHub: https://github.com/thu-coai/SafetyBench
  - Leaderboard: https://llmbench.ai/safety
- **LLMs Tested:** 25 popular Chinese and English LLMs in zero-shot and few-shot settings; GPT-4 showed substantial advantage
- **Implementation Readiness:** **High** -- Complete GitHub repo with data, evaluation guidelines, and leaderboard

---

### 1.8 Collective Constitutional AI (CCAI)

- **Full Citation:** Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus, Alex Tamkin, Deep Ganguli. "Collective Constitutional AI: Aligning a Language Model with Public Input." ACM FAccT 2024, pp. 1395-1417.
- **arXiv ID:** [2406.07814](https://arxiv.org/abs/2406.07814)
- **DOI:** 10.1145/3630106.3658979
- **Ethical Frameworks / Harm Categories:** Democratically sourced constitutional principles from ~1,000 Americans via the Polis deliberation platform. Evaluates bias across 9 social dimensions using BBQ benchmark; measures ideological alignment via OpinionQA; assesses helpful-harmless tradeoffs.
- **Dataset Size & Format:**
  - Public constitution sourced from ~1,000 participants
  - Evaluation via BBQ (bias benchmark), OpinionQA, language/math benchmarks
  - Model trained using constitutional AI methodology with publicly sourced principles
- **Code/Data URLs:** Not publicly released as a standalone dataset; methodology documented in paper
- **LLMs Tested:** CCAI-trained model compared against Claude Instant 1.2 and Standard Constitutional AI model
- **Implementation Readiness:** **Medium** -- Methodology is well-documented but requires Constitutional AI training pipeline; no standalone benchmark dataset released

---

### 1.9 PKU-SafeRLHF

- **Full Citation:** Jiaming Ji, Donghai Hong, Borong Zhang, Boyuan Chen, Juntao Dai, Boren Zheng, Tianyi Qiu, Jiayi Zhou, Kaile Wang, Boxuan Li, Sirui Han, Yike Guo, Yaodong Yang. "PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference." ACL 2025 (Main).
- **arXiv ID:** [2406.15513](https://arxiv.org/abs/2406.15513)
- **Ethical Frameworks / Harm Categories:** 19 harm categories with 3 severity levels (minor, moderate, severe). Decoupled annotations for helpfulness and harmlessness, providing nuanced perspective balancing information quality with safety and ethical considerations.
- **Dataset Size & Format:**
  - 44.6K refined prompts
  - 265K question-answer pairs with safety meta-labels
  - 166.8K preference data (dual-preference for helpfulness/harmlessness + single-preference trade-off)
  - Answers generated by Llama-family models
- **Code/Data URLs:**
  - HuggingFace: https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
  - GitHub: https://github.com/PKU-Alignment/safe-rlhf
  - Website: https://sites.google.com/view/pku-saferlhf
- **LLMs Tested:** Llama-family models for generation; severity-sensitive moderation and safety-centric RLHF algorithms trained and evaluated
- **Implementation Readiness:** **High** -- Large-scale dataset, code, and models all publicly available

---

### 1.10 SALAD-Bench

- **Full Citation:** Lijun Li, Bowen Dong, Ruohui Wang, Xuhao Hu, Wangmeng Zuo, Dahua Lin, Yu Qiao, Jing Shao. "SALAD-Bench: A Hierarchical and Comprehensive Safety Benchmark for Large Language Models." ACL 2024 (Findings).
- **arXiv ID:** [2402.05044](https://arxiv.org/abs/2402.05044)
- **Ethical Frameworks / Harm Categories:** Three-level hierarchical taxonomy: 6 domains, 16 tasks, 66 specific categories. Covers both attack and defense evaluation with QA and multiple-choice formats.
- **Dataset Size & Format:**
  - 21K harmful base questions
  - Hierarchical: 6 domains / 16 tasks / 66 categories
  - Both QA and multiple-choice formats
  - Attack-enhanced and defense-enhanced variants
  - MD-Judge (QA evaluator) and MC-Judge (MCQ evaluator)
- **Code/Data URLs:**
  - GitHub: https://github.com/OpenSafetyLab/SALAD-BENCH
  - Website: https://adwardlee.github.io/salad_bench/
- **LLMs Tested:** Multiple LLMs evaluated (details in full paper)
- **Implementation Readiness:** **High** -- Complete benchmark with evaluators and data publicly released

---

### 1.11 GuardEval

- **Full Citation:** Naseem Machlovi, Maryam Saleki, Ruhul Amin, Mohamed Rahouti, Shawqi Al-Maliki, Junaid Qadir, Mohamed M. Abdallah, Ala Al-Fuqaha. "GuardEval: A Multi-Perspective Benchmark for Evaluating Safety, Fairness, and Robustness in LLM Moderators." arXiv preprint, 2025.
- **arXiv ID:** [2601.03273](https://arxiv.org/abs/2601.03273)
- **Ethical Frameworks / Harm Categories:** 106 fine-grained categories spanning: human emotions, offensive and hateful language, gender bias, racial bias, and broader safety concerns. Integrates MetaHate and HateBase datasets (60+ individual datasets, 1M+ annotated data points).
- **Dataset Size & Format:**
  - 106 fine-grained categories
  - Multiple subsets examining socially acceptable vs. unacceptable behaviors, prosocial interactions, and value-laden perceptions across cultural/geographical contexts
  - Over 1 million annotated data points in hate speech component
- **Code/Data URLs:** Not yet publicly released at time of search
- **LLMs Tested:** GemmaGuard (Gemma3-12B fine-tuned, macro F1 = 0.832), OpenAI Moderator (F1 = 0.64), Llama Guard (F1 = 0.61)
- **Implementation Readiness:** **Medium** -- Very recent (Jan 2025); paper available but code/data availability pending

---

## 2. Red-Teaming with Ethical Evaluation

### 2.1 JAILJUDGE

- **Full Citation:** Fan Liu, Yue Feng, Zhao Xu, Lixin Su, Xinyu Ma, Dawei Yin, Hao Liu. "JAILJUDGE: A Comprehensive Jailbreak Judge Benchmark with Multi-Agent Enhanced Explanation Evaluation Framework." arXiv preprint, 2024.
- **arXiv ID:** [2410.12855](https://arxiv.org/abs/2410.12855)
- **Ethical Frameworks / Harm Categories:** Diverse risk scenarios including synthetic, adversarial, in-the-wild, and multilingual prompts. Multi-agent framework with Judging, Voting, and Inference agents for fine-grained ethical scoring (1-10 scale) with explicit reasoning.
- **Dataset Size & Format:**
  - 35K+ instruction-tuning data with reasoning explainability
  - JAILJUDGETEST: 4.5K+ labeled examples for risk scenarios
  - 6K+ multilingual examples across 10 languages
  - Fine-grained scoring (1-10) with reasoning explanations
- **Code/Data URLs:**
  - GitHub: https://github.com/usail-hkust/Jailjudge
  - HuggingFace: https://huggingface.co/usail-hkust/JailJudge-guard
  - Website: https://usail-hkust.github.io/Jailjudge/
- **LLMs Tested:** GPT-4, Llama-Guard; JailBoost enhances attack performance by 29.24%; GuardShield reduces ASR from 40.46% to 0.15%
- **Implementation Readiness:** **High** -- Complete framework with judge model, data, and evaluation code available

---

### 2.2 RedBench

- **Full Citation:** Quy-Anh Dang, Chris Ngo, Truong-Son Hy. "RedBench: A Universal Dataset for Comprehensive Red Teaming of Large Language Models." arXiv preprint, 2026.
- **arXiv ID:** [2601.03699](https://arxiv.org/abs/2601.03699)
- **Ethical Frameworks / Harm Categories:** Standardized taxonomy with 22 risk categories across 19 domains. Aggregates 37 benchmark datasets for consistent and comprehensive evaluation.
- **Dataset Size & Format:**
  - 29,362 samples (attack and refusal prompts)
  - Aggregated from 37 existing benchmark datasets
  - 22 risk categories / 19 domains
  - CC BY 4.0 license
- **Code/Data URLs:**
  - GitHub: https://github.com/knoveleng/redeval
- **LLMs Tested:** Baselines established for modern LLMs (2025 era)
- **Implementation Readiness:** **High** -- Open-source dataset and evaluation code; large-scale aggregation simplifies adoption

---

### 2.3 BiasJailbreak

- **Full Citation:** Isack Lee, Haebin Seong. "BiasJailbreak: Analyzing Ethical Biases and Jailbreak Vulnerabilities in Large Language Models." AAAI 2026 Workshop.
- **arXiv ID:** [2410.13334](https://arxiv.org/abs/2410.13334)
- **Ethical Frameworks / Harm Categories:** Intersection of ethical biases and safety alignment. Demonstrates that safety-aligned biases (gender, racial) create differential jailbreak vulnerability: 20% success rate gap between non-binary/cisgender keywords; 16% gap between white/black keywords.
- **Dataset Size & Format:**
  - Adversarial prompts with systematically varied demographic keywords
  - Quantitative measurement of differential jailbreak success rates
- **Code/Data URLs:** Code and artifacts open-sourced (URL not specified in abstract)
- **LLMs Tested:** GPT-4o and other state-of-the-art models
- **Implementation Readiness:** **Medium** -- Paper available; code/artifacts announced as open-source but specific repository URL not confirmed

---

### 2.4 Between a Rock and a Hard Place (TRIAL)

- **Full Citation:** Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu. "Between a Rock and a Hard Place: The Tension Between Ethical Reasoning and Safety Alignment in LLMs." arXiv preprint, 2025.
- **arXiv ID:** [2509.05367](https://arxiv.org/abs/2509.05367)
- **Ethical Frameworks / Harm Categories:** Exploits trolley-problem-style ethical dilemmas to jailbreak LLMs. TRIAL (Trolley-problem Red-teaming via Iterative Adversarial Leverage) generates moral dilemmas that frame harmful actions as "lesser evils." Demonstrates fundamental tension between ethical reasoning capabilities and safety alignment.
- **Dataset Size & Format:**
  - Multi-turn red-teaming methodology
  - Trolley-problem-style dilemma generation framework
  - ERR defense: Layer-Stratified Harm-Gated LoRA architecture
- **Code/Data URLs:** Not specified in paper
- **LLMs Tested:** Multiple safety-aligned LLMs (specific models in full paper)
- **Implementation Readiness:** **Medium** -- Novel attack methodology with defense; may require adaptation for benchmark use; methodology well-documented

---

### 2.5 CoSafe

- **Full Citation:** Erxin Yu, Jing Li, Ming Liao, Siqi Wang, Gao Zuchen, Fei Mi, Lanqing Hong. "CoSafe: Evaluating Large Language Model Safety in Multi-Turn Dialogue Coreference." EMNLP 2024.
- **arXiv ID:** N/A (EMNLP proceedings)
- **DOI:** Available via ACL Anthology: https://aclanthology.org/2024.emnlp-main.968/
- **Ethical Frameworks / Harm Categories:** 14 safety categories covering multi-turn coreference safety attacks. Evaluates whether LLMs can maintain safety awareness across conversation turns when harmful intent is distributed across references.
- **Dataset Size & Format:**
  - 1,400 questions across 14 categories
  - Multi-turn dialogue format with coreference attacks
  - Final question in each conversation is unsafe
  - Sourced from BeaverTails, expanded with GPT-4 into multi-turn conversations
- **Code/Data URLs:** Listed on SafetyPrompts.com
- **LLMs Tested:** LLaMA2-Chat-7b (56% ASR), Mistral-7B-Instruct (13.9% ASR), 3 additional open-source LLMs
- **Implementation Readiness:** **High** -- Dataset and evaluation available; EMNLP published

---

## 3. Harm Taxonomy Benchmarks

### 3.1 WalledEval

- **Full Citation:** Prannaya Gupta, Le Qi Yau, Hao Han Low, I-Shiang Lee, Hugo Maximus Lim, Yu Xin Teoh, Jia Hng Koh, Dar Win Liew, Rishabh Bhardwaj, Rajat Bhardwaj, Soujanya Poria. "WalledEval: A Comprehensive Safety Evaluation Toolkit for Large Language Models." EMNLP 2024 (Demo).
- **arXiv ID:** [2408.03837](https://arxiv.org/abs/2408.03837v2)
- **Ethical Frameworks / Harm Categories:** Integrates 35+ safety benchmarks covering multilingual safety, exaggerated safety, prompt injections. Introduces SGXSTest (exaggerated safety in cultural contexts) and WalledGuard (494M parameter content moderation tool). Supports text-style mutations (tense, structure, noise, paraphrase).
- **Dataset Size & Format:**
  - 35+ integrated safety benchmarks
  - Supports: Python list, CSV, JSON, HuggingFace dataset loading
  - Includes mutators for testing robustness
  - Judge benchmarking against gold-standard labels
- **Code/Data URLs:**
  - GitHub: https://github.com/walledai/walledeval
- **LLMs Tested:** Diverse open-weight and API-based models; WalledGuard (494M) benchmarked against LlamaGuard 3
- **Implementation Readiness:** **High** -- Comprehensive Python toolkit; pip-installable; extensive documentation

---

### 3.2 SafetyAnalyst

- **Full Citation:** Jing-Jing Li, Valentina Pyatkin, Max Kleiman-Weiner, Liwei Jiang, Nouha Dziri, Anne G. E. Collins, Jana Schaich Borg, Maarten Sap, Yejin Choi, Sydney Levine. "SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior." ICML 2025.
- **arXiv ID:** [2410.16665](https://arxiv.org/abs/2410.16665)
- **Ethical Frameworks / Harm Categories:** First taxonomies of harmful and beneficial effects for AI safety. Harm-benefit tree structure: actions --> harmful/beneficial effects (with likelihood, severity, immediacy) for different stakeholders. Cost-benefit analysis framework with 28 fully interpretable weight parameters. Grounded in consequentialist ethical reasoning.
- **Dataset Size & Format:**
  - 18.5 million harm-benefit features generated by frontier LLMs on 19K prompts
  - Structured harm trees and benefit trees
  - Transparent aggregation with interpretable weights
  - Alignment procedure for calibrating weights to labeled safe/unsafe prompts
- **Code/Data URLs:** Not yet publicly specified
- **LLMs Tested:** Frontier LLMs for feature generation; state-of-the-art performance on comprehensive prompt safety benchmarks
- **Implementation Readiness:** **Medium** -- ICML 2025 accepted; large-scale dataset described but public release status to be confirmed

---

### 3.3 S-Eval

- **Full Citation:** Xiaohan Yuan, Jinfeng Li, Dongxia Wang, Yuefeng Chen, Xiaofeng Mao, Longtao Huang, Jialuo Chen, Hui Xue, Xiaoxia Liu, Wenhai Wang, Kui Ren, Jingyi Wang. "S-Eval: Towards Automated and Comprehensive Safety Evaluation for Large Language Models." ISSTA 2025.
- **arXiv ID:** [2405.14191](https://arxiv.org/abs/2405.14191)
- **Ethical Frameworks / Harm Categories:** 8 risk dimensions with 102 subdivided risks. Comprehensive risk taxonomy with expert testing LLM for automated test case generation and safety critique LLM for quantitative/explainable evaluation.
- **Dataset Size & Format:**
  - 220,000 evaluation prompts total
  - 20,000 base risk prompts (10K Chinese + 10K English)
  - 200,000 attack prompts from 10 adversarial instruction attacks
  - Bilingual (Chinese/English)
  - Fully automated pipeline
- **Code/Data URLs:**
  - GitHub: https://github.com/IS2Lab/S-Eval
  - Website: https://s-eval.github.io/
  - HuggingFace Leaderboard available
- **LLMs Tested:** 21 influential LLMs; deployed in industrial setting serving millions of users
- **Implementation Readiness:** **High** -- Complete automated pipeline with benchmark data, evaluation code, and industrial deployment track record

---

### 3.4 GuardBench

- **Full Citation:** GuardBench Team (JRC, European Commission). "GuardBench: A Large-Scale Benchmark for Guardrail Models." EMNLP 2024.
- **DOI:** Available via ACL Anthology: https://aclanthology.org/2024.emnlp-main.1022/
- **Ethical Frameworks / Harm Categories:** Aggregation of 40 safety evaluation datasets into a unified guardrail evaluation framework. Includes first large-scale prompt moderation datasets in German, French, Italian, and Spanish. Standardizes evaluation across publication venues.
- **Dataset Size & Format:**
  - 40 safety evaluation datasets aggregated
  - Multilingual: English, German, French, Italian, Spanish
  - Python library for automated evaluation pipeline
- **Code/Data URLs:**
  - GitHub: https://github.com/AmenRa/GuardBench
- **LLMs Tested:** Multiple guardrail models; finding that general-purpose instruction-following models achieve competitive results without specific fine-tuning
- **Implementation Readiness:** **High** -- Python library with automated evaluation pipeline; pip-installable

---

### 3.5 PluriHarms

- **Full Citation:** Jing-Jing Li, Joel Mire, Eve Fleisig, Valentina Pyatkin, Anne Collins, Maarten Sap, Sydney Levine. "PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm." arXiv preprint, 2026.
- **arXiv ID:** [2601.08951](https://arxiv.org/abs/2601.08951)
- **Ethical Frameworks / Harm Categories:** Two-dimensional evaluation: harm axis (benign to harmful) + agreement axis (agreement to disagreement). Integrates SafetyAnalyst harm features and KALEIDO human values annotations. Treats annotator disagreement as signal rather than noise. Links demographic/psychological traits to harm perceptions.
- **Dataset Size & Format:**
  - 150 prompts calibrated across full harmfulness spectrum
  - 15,000 ratings from 100 human annotators (100 ratings per prompt)
  - Rich annotator metadata: demographic traits, psychological profiles
  - Prompt-level features of AI harm and human values
- **Code/Data URLs:** Not yet publicly released
- **LLMs Tested:** AI safety models and alignment methods benchmarked; personalization methods evaluated
- **Implementation Readiness:** **Medium** -- Very recent (Jan 2026); detailed methodology but dataset release pending

---

### 3.6 MoralBench

- **Full Citation:** Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, Yongfeng Zhang. "MoralBench: Moral Evaluation of LLMs." ACM SIGKDD Explorations, Volume 27, Issue 1, 2024.
- **arXiv ID:** [2406.04428](https://arxiv.org/abs/2406.04428)
- **Ethical Frameworks / Harm Categories:** Built on Moral Foundations Theory (MFT) with five moral foundations: Care, Fairness, Loyalty, Authority, Purity. Comparative ethical dilemma testing: models choose between paired moral scenarios scored against average human ratings.
- **Dataset Size & Format:**
  - Curated dataset of moral dilemma pairs
  - Two-part evaluation: moral statement identification + moral reasoning depth
  - Human-scored baseline for each statement
- **Code/Data URLs:**
  - GitHub: https://github.com/agiresearch/MoralBench
  - Google Drive: https://drive.google.com/drive/u/0/folders/1k93YZJserYc2CkqP8d4B3M3sgd3kA8W7
- **LLMs Tested:** Multiple LLMs including LLaMA-2 and GPT-4 (showed strong moral alignment); some models scoring high on identification struggled with reasoning depth
- **Implementation Readiness:** **High** -- Data and code publicly available; straightforward evaluation methodology

---

## 4. Agent Safety & Ethics

### 4.1 Agent-SafetyBench

- **Full Citation:** Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang. "Agent-SafetyBench: Evaluating the Safety of LLM Agents." arXiv preprint, 2024.
- **arXiv ID:** [2412.14470](https://arxiv.org/abs/2412.14470)
- **Ethical Frameworks / Harm Categories:** 8 categories of safety risks across 10 common failure modes in unsafe agent interactions. Evaluates lack of robustness and lack of risk awareness as fundamental safety defects.
- **Dataset Size & Format:**
  - 349 interaction environments
  - 2,000 test cases
  - 8 safety risk categories
  - 10 failure modes
- **Code/Data URLs:**
  - GitHub: https://github.com/thu-coai/Agent-SafetyBench
- **LLMs Tested:** 16 popular LLM agents; none achieved safety score above 60%
- **Implementation Readiness:** **High** -- Complete benchmark with environments, test cases, and evaluation code released

---

### 4.2 AgentHarm

- **Full Citation:** Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, Derek Duenas, Maxwell Lin, Justin Wang, Dan Hendrycks, Andy Zou, Zico Kolter, Matt Fredrikson, Eric Winsor, Jerome Wynne, Yarin Gal, Xander Davies. "AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents." ICLR 2025.
- **arXiv ID:** [2410.09024](https://arxiv.org/abs/2410.09024)
- **Ethical Frameworks / Harm Categories:** 11 harm categories: Fraud, Cybercrime, Self-harm, Harassment, Sexual, Copyright, Drugs, Disinformation, Hate, Violence, Terrorism. Each harmful scenario paired with benign counterpart of equivalent complexity.
- **Dataset Size & Format:**
  - 110 base harmful behaviors manually curated
  - 440 unique tasks (with augmentations)
  - 11 harm categories
  - Custom Python grading functions + LLM-based judges
  - Paired harmful/benign design isolates alignment-based refusals
- **Code/Data URLs:**
  - HuggingFace: https://huggingface.co/datasets/ai-safety-institute/AgentHarm
  - UK AISI Inspect integration: https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/
- **LLMs Tested:** GPT-4o-mini (62.5-82.2% HarmScore), Mistral Large 2, GPT-4o, Claude 3.5 Sonnet (48-85% refusal rates)
- **Implementation Readiness:** **High** -- Complete benchmark with grading functions, data, and ICLR publication

---

### 4.3 SafeAgentBench

- **Full Citation:** Sheng Yin, Xianghe Pang, Yuanzhuo Ding, Menglan Chen, Yutong Bi, Yichen Xiong, Wenhao Huang, Zhen Xiang, Jing Shao, Siheng Chen. "SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents." arXiv preprint, 2024.
- **arXiv ID:** [2412.13178](https://arxiv.org/abs/2412.13178)
- **Ethical Frameworks / Harm Categories:** 10 potential hazard types across 3 task types (explicit hazards, implicit hazards, benign tasks). First benchmark for safety-aware task planning in interactive simulation environments.
- **Dataset Size & Format:**
  - 750 tasks
  - 10 hazard types / 3 task types
  - SafeAgentEnv: universal embodied environment
  - 17 high-level actions for 8 baselines
  - Evaluation from both execution and semantic perspectives
- **Code/Data URLs:**
  - GitHub: https://github.com/shengyin1224/SafeAgentBench
  - HuggingFace: https://huggingface.co/datasets/safeagentbench/SafeAgentBench
  - Website: https://safeagentbench.github.io/
- **LLMs Tested:** 9 state-of-the-art baselines; most safety-conscious achieved only 10% rejection rate for hazardous tasks
- **Implementation Readiness:** **High** -- Complete environment, dataset, and evaluation code released

---

### 4.4 SafeToolBench

- **Full Citation:** Hongfei Xia, Hongru Wang, Zeming Liu, Qian Yu, Yuhang Guo, Haifeng Wang. "SafeToolBench: Pioneering a Prospective Benchmark to Evaluating Tool Utilization Safety in LLMs." Findings of EMNLP 2025.
- **arXiv ID:** [2509.07315](https://arxiv.org/abs/2509.07315)
- **Ethical Frameworks / Harm Categories:** SafeInstructTool framework evaluating tool safety from 3 perspectives (User Instruction, Tool Itself, Joint Instruction-Tool) across 9 detailed dimensions: Data Sensitivity, Harmfulness of Instruction, Urgency of Instruction, Frequency of Tool Utilization, Key Sensitivity, Type of Operation, Impact Scope of Operation, Alignment Between Instruction and Tool, Value Sensitivity.
- **Dataset Size & Format:**
  - 16 everyday domains
  - Malicious user instructions + diverse practical toolsets
  - Prospective evaluation (before tool execution, not retrospective)
  - 9 safety dimensions across 3 perspectives
- **Code/Data URLs:** Not yet publicly specified
- **LLMs Tested:** 4 LLMs evaluated; results show poor self-awareness for safe tool utilization
- **Implementation Readiness:** **Medium** -- EMNLP 2025 accepted; specific code/data URLs pending

---

## 5. Safetywashing & Benchmark Reliability

### 5.1 Safetywashing

- **Full Citation:** Richard Ren, Steven Basart, Adam Khoja, Alice Gatti, Long Phan, Xuwang Yin, Mantas Mazeika, Alexander Pan, Gabriel Mukobi, Ryan H. Kim, Stephen Fitz, Dan Hendrycks. "Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?" NeurIPS 2024.
- **arXiv ID:** [2407.21792](https://arxiv.org/abs/2407.21792)
- **Ethical Frameworks / Harm Categories:** Meta-analysis of AI safety benchmarks. Finds ~50% of safety benchmarks highly correlate with upstream general capabilities (e.g., MT-Bench shows 78.7% capabilities correlation). Categories analyzed: human preference alignment, scalable oversight (QuALITY), truthfulness (TruthfulQA), adversarial robustness. Proposes framework to distinguish genuine safety from capability improvements.
- **Dataset Size & Format:**
  - Meta-analysis across dozens of open language models
  - Largest empirical meta-analysis of AI safety benchmarks to date
  - Analysis framework (not a new dataset per se)
- **Code/Data URLs:** Analysis methodology documented in paper
- **LLMs Tested:** Dozens of open language models analyzed
- **Implementation Readiness:** **High** (as analytical framework) -- Provides methodology for auditing any safety benchmark's correlation with capabilities

---

### 5.2 WMDP (Weapons of Mass Destruction Proxy)

- **Full Citation:** Nathaniel Li, Alexander Pan, Anjali Gopal, Summer Yue, Daniel Berrios, Alice Gatti, Justin D. Li, Ann-Kathrin Dombrowski, Shashwat Goel, Long Phan, Gabriel Mukobi, Nathan Helm-Burger, Rassin Lababidi, Lennart Justen, Andrew B. Liu, Michael Chen, Isabelle Barrass, Oliver Zhang, Xiaoyuan Zhu, Rishub Tamirisa, Bhrugu Bharathi, Adam Khoja, Zhenqi Zhao, Ariel Herbert-Voss, Cort B. Breuer, Samuel Marks, Oam Patel, Andy Zou, Mantas Mazeika, Zifan Wang, Palash Oswal, Weiran Lin, Adam A. Hunt, Justin Tienken-Harder, Kevin Y. Shih, Kemper Talley, John Guan, Russell Kaplan, Ian Steneker, David Campbell, Brad Jokubaitis, Alex Levinson, Jean Wang, William Qian, Kallol Krishna Karmakar, Steven Basart, Stephen Fitz, Mindy Levine, Ponnurangam Kumaraguru, Uday Tupakula, Vijay Varadharajan, Ruoyu Wang, Yan Shoshitaishvili, Jimmy Ba, Kevin M. Esvelt, Alexandr Wang, Dan Hendrycks. "The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning." ICML 2024.
- **arXiv ID:** [2403.03218](https://arxiv.org/abs/2403.03218)
- **DOI:** Proceedings of the 41st ICML (PMLR 235)
- **Ethical Frameworks / Harm Categories:** 3 security domains: Biosecurity, Cybersecurity, Chemical Security. Proxy measurement of hazardous knowledge (designed NOT to contain actual sensitive information). Dual function: evaluating hazardous knowledge + benchmarking unlearning methods. RMU (Representation Misdirection for Unlearning) reduces hazardous capabilities while retaining general knowledge.
- **Dataset Size & Format:**
  - 3,668 multiple-choice questions
  - 3 domains: biosecurity, cybersecurity, chemical security
  - Questions designed as proxy (non-sensitive) measures of hazardous knowledge
  - Stringently filtered to remove sensitive information
- **Code/Data URLs:**
  - Website: https://wmdp.ai
  - GitHub: https://github.com/centerforaisafety/wmdp
- **LLMs Tested:** Multiple LLMs evaluated; RMU unlearning demonstrated on various models
- **Implementation Readiness:** **High** -- Complete dataset, unlearning code, and evaluation pipeline publicly available

---

### 5.3 LLM Ethics Benchmark (Three-Dimensional Assessment)

- **Full Citation:** Junfeng Jiao, Saleh Afroogh, Abhejay Murali, Kevin Chen, David Atkinson, Amit Dhurandhar. "LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models." Scientific Reports 15, 34642, 2025.
- **arXiv ID:** [2505.00853](https://arxiv.org/abs/2505.00853)
- **DOI:** Published in Scientific Reports (Nature)
- **Ethical Frameworks / Harm Categories:** Three-dimensional assessment: (1) Foundational Moral Principles, (2) Reasoning Robustness, (3) Value Consistency across diverse scenarios. Employs Moral Foundations Questionnaire (MFQ-30) across five dimensions: Care, Fairness, Loyalty, Authority, Sanctity. Addresses accountability gaps in ethical AI decision-making.
- **Dataset Size & Format:**
  - MFQ-30-based assessment
  - Three evaluation dimensions
  - Open-sourced benchmark datasets and evaluation codebase
- **Code/Data URLs:**
  - GitHub: https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark.git
- **LLMs Tested:** Multiple LLMs (specific models in full paper)
- **Implementation Readiness:** **High** -- Published in peer-reviewed journal; datasets and code publicly released

---

## 6. Summary Table

| # | Benchmark | Year | Venue | Ethical Dimension | Dataset Size | Impl. Readiness |
|---|-----------|------|-------|-------------------|-------------|-----------------|
| 1 | WildGuard | 2024 | NeurIPS | 13 risk subcats (Privacy, Misinfo, Harmful Lang, Malicious Use) | 92K train + 5.3K test | High |
| 2 | HH-RLHF | 2022 | arXiv | Helpfulness vs. Harmlessness (dual-axis) | ~170K preference pairs | High |
| 3 | JailbreakBench | 2024 | NeurIPS | 10 policy-aligned misuse categories | 200 behaviors (100+100) | High |
| 4 | AEGIS 2.0 | 2025 | NAACL | 12 core + 9 fine-grained hazard categories | 33.4K interactions | High |
| 5 | SORRY-Bench | 2025 | ICLR | 44 unsafe topics + 20 linguistic augmentations | 440 instructions + 7K annotations | High |
| 6 | SG-Bench | 2024 | NeurIPS | 6 safety issue types (generative + discriminative) | 1,442 queries | High |
| 7 | SafetyBench | 2024 | ACL | 7 safety categories (Chinese + English) | 11,435 MCQs | High |
| 8 | CCAI | 2024 | FAccT | Democratically sourced constitutional principles | ~1K participant constitution | Medium |
| 9 | PKU-SafeRLHF | 2025 | ACL | 19 harm categories x 3 severity levels | 265K QA + 166.8K preferences | High |
| 10 | SALAD-Bench | 2024 | ACL Findings | 6 domains / 16 tasks / 66 categories | 21K harmful questions | High |
| 11 | GuardEval | 2025 | arXiv | 106 categories (emotions, offense, bias, safety) | 1M+ annotated | Medium |
| 12 | JAILJUDGE | 2024 | arXiv | Multi-agent ethical scoring (1-10) with reasoning | 35K+ train + 4.5K test + 6K multilingual | High |
| 13 | RedBench | 2026 | arXiv | 22 risk categories / 19 domains | 29,362 samples from 37 datasets | High |
| 14 | BiasJailbreak | 2024 | AAAI WS | Ethical bias x jailbreak vulnerability (gender, race) | Adversarial prompt sets | Medium |
| 15 | TRIAL | 2025 | arXiv | Trolley-problem ethical dilemma exploitation | Attack methodology | Medium |
| 16 | CoSafe | 2024 | EMNLP | 14 safety categories (multi-turn coreference) | 1,400 questions | High |
| 17 | WalledEval | 2024 | EMNLP Demo | 35+ safety benchmarks integrated | Toolkit (meta-benchmark) | High |
| 18 | SafetyAnalyst | 2025 | ICML | Harm-benefit trees (consequentialist ethics) | 18.5M features on 19K prompts | Medium |
| 19 | S-Eval | 2025 | ISSTA | 8 risk dimensions / 102 subdivided risks | 220K evaluation prompts | High |
| 20 | GuardBench | 2024 | EMNLP | 40 safety datasets aggregated (multilingual) | 40 datasets | High |
| 21 | PluriHarms | 2026 | arXiv | Harm spectrum + annotator disagreement as signal | 150 prompts x 100 ratings | Medium |
| 22 | MoralBench | 2024 | SIGKDD | Moral Foundations Theory (Care, Fairness, Loyalty, Authority, Purity) | Moral dilemma pairs | High |
| 23 | Agent-SafetyBench | 2024 | arXiv | 8 safety risk categories / 10 failure modes | 2,000 test cases / 349 environments | High |
| 24 | AgentHarm | 2025 | ICLR | 11 harm categories (Fraud to Terrorism) | 440 tasks (110 base x 4) | High |
| 25 | SafeAgentBench | 2024 | arXiv | 10 hazard types / 3 task types | 750 tasks | High |
| 26 | SafeToolBench | 2025 | EMNLP Findings | 9 dimensions (3 perspectives) incl. Value Sensitivity | 16 domains | Medium |
| 27 | Safetywashing | 2024 | NeurIPS | Meta-analysis of safety benchmark validity | Analysis framework | High |
| 28 | WMDP | 2024 | ICML | Biosecurity, Cybersecurity, Chemical Security | 3,668 MCQs | High |
| 29 | LLM Ethics Benchmark | 2025 | Sci. Reports | MFQ-30: Care, Fairness, Loyalty, Authority, Sanctity | 3D assessment framework | High |

---

## Key Observations

### Ethical Frameworks Represented
1. **Consequentialist/Cost-Benefit:** SafetyAnalyst (harm-benefit trees), PluriHarms
2. **Moral Foundations Theory:** MoralBench, LLM Ethics Benchmark
3. **Deontological/Policy-Based:** JailbreakBench (OpenAI policies), SORRY-Bench (unsafe topic taxonomy)
4. **Democratic/Collective Values:** Collective Constitutional AI (publicly sourced principles)
5. **Dual-Axis Safety-Helpfulness:** HH-RLHF, PKU-SafeRLHF
6. **Intersectional Ethics-Safety:** BiasJailbreak (bias x jailbreak), TRIAL (moral dilemma exploitation)
7. **Hierarchical Harm Taxonomies:** SALAD-Bench, AEGIS 2.0, S-Eval, WildGuard

### Notable Gaps Identified
- Most benchmarks focus on **harm prevention** rather than **positive ethical reasoning**
- **Cultural ethical pluralism** is underrepresented in safety benchmarks (though SORRY-Bench includes some multilingual augmentation)
- **Value trade-off evaluation** (e.g., safety vs. helpfulness vs. honesty) is addressed by PKU-SafeRLHF and CCAI but not systematically across most benchmarks
- **Safetywashing analysis** reveals ~50% of safety benchmarks may primarily measure general capabilities rather than genuine safety
- **Agent ethics** is emerging (Agent-SafetyBench, AgentHarm, SafeAgentBench, SafeToolBench) but tool-use ethics beyond safety refusal remains underexplored

### Benchmarks Excluded (Already Known)
BeaverTails, HarmBench, TrustLLM, DecodingTrust, FLAMES, CValues, CARE, AraTrust, and all other benchmarks listed in the exclusion set were not duplicated in this report.

---

*Report generated by Agent 16 on 2026-02-07. All arXiv IDs and URLs verified at time of search.*
