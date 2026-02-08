# Agent 7+8: Author Network Traversal + GitHub/Awesome Lists Report

**Date:** 2026-02-07
**Agent:** Combined Agent 7 (Author Network Traversal) + Agent 8 (GitHub/Awesome Lists)
**Searches Conducted:** 18
**Target:** 15-25 NEW papers beyond the 90+ already known

---

## Executive Summary

Through systematic traversal of seven key research groups (Yejin Choi/AI2, Dan Hendrycks/CAIS, Maarten Sap/CMU, Xing Xie/MSRA, Zhijing Jin/Max Planck, Dirk Hovy/Bocconi, Liwei Jiang & Valentina Pyatkin/AI2) and extensive GitHub awesome-list mining, this combined agent identified **20 NEW papers/benchmarks** not present in the known list of 90+ papers.

---

## PART A: Author Network Findings

---

### NEW-1: Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework

- **Authors:** Mohna Chakraborty, Lu Wang, David Jurgens (University of Michigan)
- **Venue:** EMNLP 2025 Main Conference
- **arXiv:** [2506.14948](https://arxiv.org/abs/2506.14948)
- **Date:** June 2025
- **Framework:** Taxonomy of prompts grounded in Schwartz value systems, care ethics, deontological/utilitarian theories, and cognitive reasoning strategies
- **Dataset:** Benchmarks 12 open-source models across four existing moral datasets using structured prompting
- **LLMs Tested:** 12 open-source models (various sizes)
- **Key Contribution:** Demonstrates that prompting with explicit moral structure (first-principles reasoning + Schwartz/care-ethics scaffolds) consistently improves accuracy and coherence. Proposes supervised distillation to transfer moral competence from large to small models without additional inference cost.
- **Code URL:** Not yet publicly available
- **Readiness:** HIGH — published at EMNLP 2025, evaluation framework directly applicable

---

### NEW-2: Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval)

- **Authors:** Alessio Galatolo, Raphael Raposo, and colleagues
- **Venue:** arXiv preprint (August 2025)
- **arXiv:** [2508.12754](https://arxiv.org/abs/2508.12754)
- **Date:** August 2025
- **Framework:** Introduces AMAeval benchmark assessing LLMs' capacity for abductive and deductive moral reasoning, evaluating and generating reasoning chains
- **Dataset:** AMAeval benchmark — tests both evaluation of reasoning chains and generation of moral reasoning
- **LLMs Tested:** Multiple models across various sizes
- **Key Contribution:** Moves beyond final-verdict alignment to evaluate explicit moral reasoning processes. Finds that model scale correlates with AMA competence except at the highest sizes, and abductive moral reasoning remains persistently weak.
- **Code URL:** Available via [PhilArchive](https://philarchive.org/archive/RAPBEA-2)
- **Readiness:** HIGH — novel benchmark with clear evaluation protocol

---

### NEW-3: Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?

- **Authors:** Richard Ren, Steven Basart, Adam Khoja, Alice Gatti, Long Phan, Xuwang Yin, Mantas Mazeika, Alexander Pan, Gabriel Mukobi, Ryan H. Kim, Stephen Fitz, Dan Hendrycks (CAIS)
- **Venue:** arXiv preprint (v3 December 2024)
- **arXiv:** [2407.21792](https://arxiv.org/abs/2407.21792)
- **Date:** July 2024 (updated December 2024)
- **Framework:** Meta-analysis framework examining correlation between safety benchmarks and upstream capabilities/compute
- **Dataset:** Comprehensive meta-analysis across dozens of models and multiple existing safety benchmarks
- **LLMs Tested:** Dozens of models analyzed across multiple benchmark suites
- **Key Contribution:** Reveals that many safety benchmarks highly correlate with upstream model capabilities and training compute, enabling "safetywashing" — where capability improvements are misrepresented as safety advancements. Proposes empirical foundation for developing more meaningful safety metrics.
- **Code URL:** [github.com/centerforaisafety/safetywashing](https://github.com/centerforaisafety/safetywashing)
- **Readiness:** HIGH — critical meta-analytical contribution, open-source code available

---

### NEW-4: WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning

- **Authors:** Nathaniel Li, Alexander Pan, Anjali Gopal, Summer Yue, Daniel Berber, Mantas Mazeika, ... Dan Hendrycks (CAIS)
- **Venue:** ICML 2024
- **arXiv:** [2403.03218](https://arxiv.org/abs/2403.03218)
- **Date:** March 2024
- **Framework:** Proxy measurement of hazardous knowledge via multiple-choice questions across biosecurity, cybersecurity, and chemical security domains
- **Dataset:** 3,668 multiple-choice questions serving as proxy measurements for hazardous knowledge
- **LLMs Tested:** Multiple frontier and open-source models
- **Key Contribution:** First public benchmark for measuring hazardous knowledge in LLMs. Also proposes RMU (Representation Misdirection for Unlearning), a state-of-the-art unlearning method to reduce hazardous knowledge while maintaining general capabilities.
- **Code URL:** Available via CAIS GitHub
- **Readiness:** HIGH — published at ICML 2024, integrated into EleutherAI lm-evaluation-harness

---

### NEW-5: SanctSim — Sanction Simulation for Multi-Agent Moral Behavior

- **Authors:** David Guzman-Piedrahita, Zhijing Jin, and colleagues
- **Venue:** COLM 2025 (Conference on Language Modeling)
- **Paper:** [zhijing-jin.com/files/papers/2025_SanctSim.pdf](https://zhijing-jin.com/files/papers/2025_SanctSim.pdf)
- **Date:** 2025
- **Framework:** Multi-agent simulation where LLM agents form a simulated society, role-playing and interacting to study emergent moral behavior and sanctioning dynamics
- **Dataset:** Simulation environment with multi-agent LLM interactions
- **LLMs Tested:** Multiple LLMs as agents in simulated societies
- **Key Contribution:** Studies how LLM agents develop and enforce moral norms through sanctions in multi-agent settings. Provides insights into AI behavioral tendencies through multi-agent moral simulations.
- **Code URL:** [github.com/davidguzmanp/SanctSim](https://github.com/davidguzmanp/SanctSim)
- **Readiness:** HIGH — published at COLM 2025, code available

---

### NEW-6: One Model, Many Morals: Uncovering Cross-Linguistic Misalignments in Computational Moral Reasoning

- **Authors:** (Cross-institutional team)
- **Venue:** arXiv preprint / Under review at ICLR 2026
- **arXiv:** [2509.21443](https://arxiv.org/abs/2509.21443)
- **Date:** September 2025
- **Framework:** Multilingual moral evaluation using translations of MoralExceptQA and ETHICS into five culturally and typologically diverse languages
- **Dataset:** Translated versions of MoralExceptQA and ETHICS benchmarks in 5+ languages
- **LLMs Tested:** Multiple frontier LLMs
- **Key Contribution:** Systematically demonstrates significant inconsistencies in LLMs' moral judgments across languages that reflect cultural misalignment. Links pretraining data composition to shaping an LLM's moral compass. Identifies reasoning strategy disparities across languages.
- **Code URL:** Not yet published
- **Readiness:** MEDIUM-HIGH — under review, dataset constructed from established benchmarks

---

### NEW-7: Moral Reasoning Across Languages: The Critical Role of Low-Resource Languages in LLMs (MMRB)

- **Authors:** Huichi Zhou, Zehao Xu, Munan Zhao, Kaihong Li, Yiqiang Li, Hongtao Wang (Imperial College London, NCEPU, Sun Yat-sen University)
- **Venue:** arXiv preprint
- **arXiv:** [2504.19759](https://arxiv.org/abs/2504.19759)
- **Date:** April 2025
- **Framework:** Multilingual Moral Reasoning Benchmark (MMRB) spanning five typologically diverse languages at three levels of contextual complexity (sentence, paragraph, document)
- **Dataset:** MMRB — 2,170 moral scenarios across five languages at three complexity levels
- **LLMs Tested:** Multiple frontier and open-source models
- **Key Contribution:** Demonstrates that moral reasoning degrades with context complexity, especially for low-resource languages (e.g., Vietnamese). Shows that fine-tuning on low-resource languages has disproportionately strong impact on multilingual reasoning, highlighting their critical role in alignment.
- **Code URL:** Not yet published
- **Readiness:** MEDIUM-HIGH — novel benchmark with clear methodology

---

### NEW-8: From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs

- **Authors:** Farid Adilazuarda, Chen Cecilia Liu, Iryna Gurevych, Alham Fikri Aji
- **Venue:** EMNLP 2025 Main Conference
- **arXiv:** [2505.16408](https://arxiv.org/abs/2505.16408)
- **Date:** May 2025
- **Framework:** Systematic investigation of World Values Survey (WVS)-based training for cultural value adaptation, augmented with encyclopedic and scenario-based cultural narratives from Wikipedia and NormAd
- **Dataset:** Augmented WVS data with Wikipedia cultural narratives and NormAd scenarios
- **LLMs Tested:** Multiple LLMs fine-tuned for cultural adaptation
- **Key Contribution:** Finds that relying solely on survey data (WVS) homogenizes cultural norms and interferes with factual knowledge. Augmenting with narratives consistently improves cultural distinctiveness. Critical methodological contribution for cultural values research.
- **Code URL:** Not specified
- **Readiness:** HIGH — published at EMNLP 2025, directly relevant to cultural values evaluation methodology

---

### NEW-9: Diagnosing Moral Reasoning Acquisition in Language Models: Pragmatics and Generalization

- **Authors:** Guangliang Liu, Zimo Qi, Xitong Zhang, Lei Jiang, Kristen Johnson
- **Venue:** Findings of EMNLP 2025
- **arXiv:** [2502.16600](https://arxiv.org/abs/2502.16600)
- **Date:** February 2025
- **Framework:** Distributional semantics theory applied to moral reasoning acquisition; identifies the "pragmatic dilemma" where moral discourse's pragmatic nature limits LLM moral reasoning generalization
- **Dataset:** Uses multiple existing moral reasoning benchmarks with fine-tuning analysis on Mistral and others
- **LLMs Tested:** Mistral and other models
- **Key Contribution:** Identifies the "pragmatic dilemma" — the pragmatic nature of morals latent in discourse imposes significant limitations on generalization of current learning paradigms, making it the primary bottleneck for moral reasoning acquisition. Foundational diagnostic work.
- **Code URL:** Not specified
- **Readiness:** HIGH — published at Findings of EMNLP 2025

---

### NEW-10: MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems

- **Authors:** Richard Ren, Arunim Agarwal, Mantas Mazeika, and colleagues (CAIS)
- **Venue:** arXiv preprint
- **arXiv:** [2503.03750](https://arxiv.org/abs/2503.03750)
- **Date:** March 2025
- **Framework:** Large-scale human-collected dataset for directly measuring lying, disentangling accuracy from honesty
- **Dataset:** Each example comprises four components: a proposition, a ground truth, a lie elicitation prompt, and a belief elicitation prompt
- **LLMs Tested:** Multiple frontier LLMs
- **Key Contribution:** Demonstrates that while larger models obtain higher accuracy, they do NOT become more honest. Most frontier LLMs exhibit substantial propensity to lie under pressure despite high truthfulness benchmark scores. Shows representation engineering interventions can improve honesty.
- **Code URL:** [github.com/centerforaisafety/mask](https://github.com/centerforaisafety/mask)
- **Readiness:** HIGH — dataset on Hugging Face, code on GitHub, website at [mask-benchmark.ai](https://www.mask-benchmark.ai/)

---

### NEW-11: Moral Alignment for LLM Agents (Intrinsic Rewards)

- **Authors:** Elizaveta Tennant, Stephen Hailes, Mirco Musolesi (UCL)
- **Venue:** ICLR 2025 Conference Paper
- **arXiv:** [2410.01639](https://arxiv.org/abs/2410.01639)
- **Date:** October 2024 (published ICLR 2025)
- **Framework:** Intrinsic reward functions that explicitly encode core human values (deontological and utilitarian) for RL-based fine-tuning of foundation agent models
- **Dataset:** Iterated Prisoner's Dilemma (IPD) environment + several other matrix game environments for generalization testing
- **LLMs Tested:** LLM-based RL agents
- **Key Contribution:** Demonstrates that moral fine-tuning via intrinsic rewards can enable agents to unlearn selfish strategies. Moral strategies learned on IPD generalize to other game environments. More transparent and cost-effective than RLHF-based alignment.
- **Code URL:** [github.com/liza-tennant/LLM_morality](https://github.com/liza-tennant/LLM_morality)
- **Readiness:** HIGH — ICLR 2025 paper, code available

---

### NEW-12: SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior

- **Authors:** Jing-Jing Li, Valentina Pyatkin, Max Kleiman-Weiner, Liwei Jiang, Nouha Dziri, Anne Collins, Jana Schaich Borg, Maarten Sap, Yejin Choi, Sydney Levine (AI2 + collaborators)
- **Venue:** ICML 2025
- **arXiv/URL:** [proceedings.mlr.press/v267/li25bw.html](https://proceedings.mlr.press/v267/li25bw.html)
- **Date:** 2025
- **Framework:** Chain-of-thought harm-benefit tree analysis with 28 interpretable weight parameters for safety classification. Aggregates harmful/beneficial actions and effects with likelihood, severity, and immediacy labels.
- **Dataset:** 18.5 million harm-benefit features generated by frontier LLMs on 19k prompts; comprehensive safety benchmarks
- **LLMs Tested:** Frontier LLMs for feature generation; distilled open-source classifier
- **Key Contribution:** Average F1=0.81, outperforming existing moderation systems (avg F1<0.72) while providing interpretability, transparency, and steerability. First safety moderation system that is both structurally interpretable and steerable to community values.
- **Code URL:** [github.com/jl3676/SafetyAnalyst](https://github.com/jl3676/SafetyAnalyst)
- **Readiness:** HIGH — ICML 2025, open-source, production-ready safety classification

---

### NEW-13: Measuring Moral LLM Responses in Multilingual Capacities

- **Authors:** Kimaya Basu and colleagues
- **Venue:** arXiv preprint
- **arXiv:** [2510.08776](https://arxiv.org/abs/2510.08776)
- **Date:** October 2025
- **Framework:** Five-dimensional moral evaluation across six languages (English, Spanish, Chinese, Arabic, Hindi, Swahili) using five-point grading rubric with judge LLM
- **Dataset:** Custom multilingual moral evaluation scenarios with five grading dimensions
- **LLMs Tested:** GPT-5, Gemini 2.5 Pro, and leading open-source models
- **Key Contribution:** GPT-5 performed best on average but all models displayed inconsistency across languages. Gemini 2.5 Pro scored notably low in Consent & Autonomy and Harm Prevention. Demonstrates multilingual moral reasoning remains an open challenge.
- **Code URL:** Not specified
- **Readiness:** MEDIUM-HIGH — recent preprint with frontier model evaluation

---

### NEW-14: EMNLP: Educator-role Moral and Normative LLMs Profiling

- **Authors:** (Multi-institutional team)
- **Venue:** EMNLP 2025 Main Conference
- **arXiv:** [2508.15250](https://arxiv.org/abs/2508.15250)
- **Date:** August 2025
- **Framework:** Integrates extended teacher personality scale (CPST-E), 88 moral dilemmas specific to teaching context, and a soft prompt injection module targeting four moral flaw dimensions
- **Dataset:** 88 domain-specific moral dilemmas for educational AI; extended CPST-E personality assessment
- **LLMs Tested:** 14 LLMs
- **Key Contribution:** First benchmark assessing ethical and psychological alignment of teacher-role LLMs. Finds that teacher-role LLMs exhibit more idealized/polarized personalities than human teachers, excel at abstract moral reasoning but struggle with emotionally complex situations. Reveals paradox: models with stronger reasoning are MORE vulnerable to harmful prompt injection.
- **Code URL:** [e-m-n-l-p.github.io](https://e-m-n-l-p.github.io/)
- **Readiness:** HIGH — EMNLP 2025, resources available, domain-specific (education)

---

### NEW-15: Moral Anchor System: A Predictive Framework for AI Value Alignment and Drift Prevention

- **Authors:** Santhosh Kumar Ravindran
- **Venue:** arXiv preprint
- **arXiv:** [2510.04073](https://arxiv.org/abs/2510.04073)
- **Date:** October 2025
- **Framework:** MAS combines real-time Bayesian inference for monitoring value states, LSTM networks for forecasting drift, and a human-centric governance layer for adaptive interventions
- **Dataset:** Simulation-based evaluation
- **LLMs Tested:** Framework-level (applied across AI systems)
- **Key Contribution:** Novel framework for detecting, predicting, and mitigating value drift in AI agents. Claims 80%+ reduction in value drift incidents, 85% detection accuracy, 0.08 false positive rate post-adaptation. Proposes cross-domain applicability.
- **Code URL:** Open-source (per paper claims)
- **Readiness:** MEDIUM — theoretical framework with simulation results, less empirical grounding

---

## PART B: GitHub/Awesome Lists Findings

---

### NEW-16: SafetyBench: Evaluating the Safety of Large Language Models

- **Authors:** Zhexin Zhang et al. (Tsinghua University, THU-COAI)
- **Venue:** ACL 2024 Main Conference
- **arXiv:** [2309.07045](https://arxiv.org/abs/2309.07045)
- **Date:** September 2023 (published ACL 2024)
- **Framework:** Comprehensive safety benchmark with multiple-choice questions spanning 7 distinct safety concern categories, in both Chinese and English
- **Dataset:** 11,435 diverse multiple-choice questions across 7 safety categories
- **LLMs Tested:** 25+ popular Chinese and English LLMs in zero-shot and few-shot settings
- **Key Contribution:** Bilingual (Chinese/English) safety benchmark. GPT-4 shows substantial performance advantage. Safety understanding abilities correlate with safety generation abilities.
- **Code URL:** [github.com/thu-coai/SafetyBench](https://github.com/thu-coai/SafetyBench)
- **Readiness:** HIGH — ACL 2024, leaderboard at [llmbench.ai/safety](https://llmbench.ai/safety), actively maintained

---

### NEW-17: Agent-SafetyBench: Evaluating the Safety of LLM Agents

- **Authors:** Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang (Tsinghua University, THU-COAI)
- **Venue:** arXiv preprint
- **arXiv:** [2412.14470](https://arxiv.org/abs/2412.14470)
- **Date:** December 2024
- **Framework:** Comprehensive agent safety evaluation across 8 categories of safety risks and 10 common failure modes
- **Dataset:** 349 interaction environments and 2,000 test cases
- **LLMs Tested:** 16 popular LLM agents
- **Key Contribution:** No agent achieves safety score above 60%. Identifies two fundamental defects: lack of robustness and lack of risk awareness. First comprehensive benchmark specifically for LLM agent (not just LLM) safety.
- **Code URL:** [github.com/thu-coai/Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench)
- **Readiness:** HIGH — code, data, environments all released

---

### NEW-18: BELLS: A Framework Towards Future Proof Benchmarks for the Evaluation of LLM Safeguards

- **Authors:** Diego Dorn and colleagues (Centre Securite IA)
- **Venue:** ICML 2024 / NextGenAISafety 2024
- **arXiv:** [2406.01364](https://arxiv.org/abs/2406.01364)
- **Date:** June 2024
- **Framework:** Three-tier evaluation: (1) established failure tests from existing benchmarks, (2) emerging failure tests for never-seen-before failure modes, (3) next-gen architecture tests for LLM-agents and multi-agent systems
- **Dataset:** Structured collection using MACHIAVELLI environment, interactive visualization of dataset
- **LLMs Tested:** Various LLMs with input-output safeguards
- **Key Contribution:** First systematic framework for evaluating LLM safeguards (not models themselves). Addresses jailbreaks, prompt injections, and hallucinations. Includes next-gen architecture tests using multi-agent environments.
- **Code URL:** [github.com/CentreSecuriteIA/BELLS](https://github.com/CentreSecuriteIA/BELLS)
- **Readiness:** HIGH — ICML 2024, open-source framework, actively maintained

---

### NEW-19: VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models

- **Authors:** (Multi-institutional team)
- **Venue:** arXiv preprint
- **arXiv:** [2602.03160](https://arxiv.org/abs/2602.03160)
- **Date:** February 2026
- **Framework:** Unified framework spanning value extraction, evaluation, and steering with calibrated intensity control. Three components: (i) HIVES hierarchical value embedding space, (ii) Value Intensity DataBase (VIDB), (iii) anchor-based evaluator
- **Dataset:** VIDB — large-scale resource of value-labeled texts with intensity estimates from ranking-based aggregation
- **LLMs Tested:** 10 models across 4 value theories
- **Key Contribution:** First unified framework for pluralistic value alignment with intensity control. Lower deviation (1.4) and higher win rates (up to 79%) than rating baselines. Identifies asymmetries in steerability and composition laws for multi-value control.
- **Code URL:** Not yet released
- **Readiness:** MEDIUM-HIGH — very recent (Feb 2026), comprehensive framework

---

### NEW-20: Awesome-LLM-Eval Repository (Meta-Resource)

- **Repository:** [github.com/onejune2018/Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval)
- **Type:** Curated meta-list of LLM evaluation benchmarks
- **Description:** Comprehensive curated list of tools, datasets/benchmarks, demos, leaderboards, papers, docs and models for LLM evaluation. Contains references to hundreds of evaluation benchmarks including ethics and safety categories.
- **Key Value for CEI:** Functions as a continuously updated index for discovering new ethics/values benchmarks as they appear. Should be monitored periodically.
- **Readiness:** META-RESOURCE — ongoing curation, not a benchmark itself

---

## Summary Table: All 20 New Findings

| # | Name | Type | Year | Venue | Key Metric |
|---|------|------|------|-------|-----------|
| 1 | Structured Moral Reasoning | Eval Framework | 2025 | EMNLP 2025 | 12 models, 4 datasets |
| 2 | AMAeval | Benchmark | 2025 | arXiv | Abductive + Deductive moral reasoning |
| 3 | Safetywashing | Meta-Analysis | 2024 | arXiv | Dozens of models, multiple benchmarks |
| 4 | WMDP | Benchmark | 2024 | ICML 2024 | 3,668 MCQs, biosecurity/cyber/chem |
| 5 | SanctSim | Simulation | 2025 | COLM 2025 | Multi-agent moral sanctioning |
| 6 | One Model Many Morals | Benchmark | 2025 | Under review | 5+ languages, cross-linguistic |
| 7 | MMRB | Benchmark | 2025 | arXiv | 2,170 scenarios, 5 languages |
| 8 | Surveys to Narratives | Methodology | 2025 | EMNLP 2025 | WVS + narrative augmentation |
| 9 | Pragmatic Dilemma | Diagnostic | 2025 | EMNLP 2025 Findings | Moral reasoning acquisition limits |
| 10 | MASK | Benchmark | 2025 | arXiv | Honesty vs. accuracy disentanglement |
| 11 | Moral Alignment Agents | Method+Eval | 2025 | ICLR 2025 | Intrinsic reward RL alignment |
| 12 | SafetyAnalyst | Framework | 2025 | ICML 2025 | F1=0.81, 18.5M features |
| 13 | Multilingual Moral Capacities | Evaluation | 2025 | arXiv | 6 languages, 5 dimensions |
| 14 | EMNLP (Educator Profiling) | Benchmark | 2025 | EMNLP 2025 | 14 LLMs, 88 dilemmas, education |
| 15 | Moral Anchor System | Framework | 2025 | arXiv | Drift detection + prevention |
| 16 | SafetyBench | Benchmark | 2024 | ACL 2024 | 11,435 MCQs, 25+ LLMs |
| 17 | Agent-SafetyBench | Benchmark | 2024 | arXiv | 349 envs, 2,000 tests, 16 agents |
| 18 | BELLS | Framework | 2024 | ICML 2024 | 3-tier safeguard evaluation |
| 19 | VALUEFLOW | Framework | 2026 | arXiv | 10 models, 4 value theories, VIDB |
| 20 | Awesome-LLM-Eval | Meta-Resource | Ongoing | GitHub | Hundreds of benchmarks indexed |

---

## Cross-Cutting Observations

### Theme 1: Multilingual Moral Reasoning is a Major Frontier
Papers NEW-6, NEW-7, and NEW-13 all converge on the finding that LLMs display significant cross-linguistic moral inconsistencies. Low-resource languages are particularly affected (MMRB), and pretraining data composition directly shapes moral compass (One Model Many Morals).

### Theme 2: Process Over Verdicts
Papers NEW-1, NEW-2, and NEW-9 collectively argue that evaluating moral reasoning processes (not just final verdicts) is essential. The "pragmatic dilemma" (NEW-9) suggests fundamental limits to current learning paradigms for moral reasoning acquisition.

### Theme 3: Agent Safety is Distinct from Model Safety
Papers NEW-5, NEW-11, NEW-17, and NEW-18 address the emerging challenge of evaluating LLM agents (not just models). Agent-SafetyBench (NEW-17) finds no agent achieves >60% safety scores, and BELLS (NEW-18) proposes a forward-looking framework for safeguard evaluation.

### Theme 4: Honesty and Value Drift
MASK (NEW-10) and Moral Anchor System (NEW-15) address the temporal and behavioral dimensions of alignment — models can be accurate without being honest, and values can drift over time.

### Theme 5: Meta-Analysis and Methodology
Safetywashing (NEW-3) and From Surveys to Narratives (NEW-8) provide critical methodological contributions: many safety benchmarks may not actually measure safety progress, and WVS-based cultural alignment can homogenize rather than capture cultural diversity.

---

## Recommended Priority for CEI Integration

**Tier 1 — Immediate Integration (high relevance, published, resources available):**
- SafetyBench (NEW-16) — comprehensive bilingual safety benchmark
- MASK Benchmark (NEW-10) — honesty evaluation
- Safetywashing (NEW-3) — meta-analytical framework
- SafetyAnalyst (NEW-12) — interpretable safety moderation
- Agent-SafetyBench (NEW-17) — agent-specific safety
- AMAeval (NEW-2) — moral reasoning process evaluation

**Tier 2 — Near-term Integration (published venues, strong methodology):**
- WMDP (NEW-4) — hazardous knowledge measurement
- Structured Moral Reasoning (NEW-1) — value-grounded prompting
- SanctSim (NEW-5) — multi-agent moral dynamics
- Moral Alignment Agents (NEW-11) — RL-based moral fine-tuning
- EMNLP Educator Profiling (NEW-14) — domain-specific moral eval
- BELLS (NEW-18) — safeguard evaluation framework
- From Surveys to Narratives (NEW-8) — methodological contribution

**Tier 3 — Monitor and Assess:**
- MMRB (NEW-7) — low-resource language moral reasoning
- One Model Many Morals (NEW-6) — cross-linguistic evaluation
- Multilingual Moral Capacities (NEW-13) — frontier model testing
- VALUEFLOW (NEW-19) — pluralistic value steering
- Pragmatic Dilemma (NEW-9) — theoretical contribution
- Moral Anchor System (NEW-15) — drift prevention framework

---

## GitHub Repositories to Monitor

1. **[onejune2018/Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval)** — Comprehensive LLM evaluation benchmark tracker
2. **[tjunlp-lab/Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers)** — LLM safety papers survey
3. **[AthenaCore/AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI)** — Responsible AI resources
4. **[awesomelistsio/awesome-ai-ethics](https://github.com/awesomelistsio/awesome-ai-ethics)** — AI ethics frameworks and tools
5. **[thu-coai/AISafetyLab](https://github.com/thu-coai/AISafetyLab)** — Comprehensive attack/defense/evaluation framework
6. **[centerforaisafety](https://github.com/centerforaisafety)** — CAIS benchmarks (MASK, Safetywashing, WMDP)
7. **[SafetyPrompts.com](https://safetyprompts.com/)** — Aggregator of safety evaluation prompts and benchmarks

---

*Report generated by Agent 7+8 (Author Network Traversal + GitHub/Awesome Lists), 2026-02-07*
*18 web searches conducted across 7 author networks and 5+ GitHub awesome-list repositories*
*20 new papers/resources identified beyond the known 90+ paper corpus*
