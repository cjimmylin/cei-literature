# Ethical Values Alignment Benchmarks for LLMs
## Comprehensive Research Report — Updated

**Generated:** 2026-02-10
**Previous version:** 2026-02-07 (39 entries)
**Scope:** Papers with implementable datasets, benchmarks, code, or evaluation frameworks for assessing LLM alignment with ethical values
**Source:** CEI Literature Vault (846 papers) + 528-candidate benchmark survey
**Anchor paper:** Hendrycks et al. (2021) "Aligning AI with Shared Human Values" (ICLR 2021)

---

## Executive Summary

This report catalogues **152 benchmarks and resources** for evaluating ethical values alignment in large language models, expanded from the original 39-entry report (2026-02-07). Key changes:

1. **122 new entries** discovered from the 528-candidate benchmark survey (20-agent deep-read of 846 vault papers)
2. **All 30 original entries preserved** with hand-curated detail
3. **Scope filtering** applied: only benchmarks focused on ethical values, moral reasoning, cultural values, normative ethics, and moral psychology (excluding pure toxicity/safety/bias)
4. **YAML enrichment** for entries in vault: arXiv links, DOIs, venue, authors, code URLs

### Section Overview

| Section   | Topic                                        | Entries |
| --------- | -------------------------------------------- | ------- |
| A         | Multi-Framework Ethics Benchmarks            | 7       |
| B         | Single-Framework / Focused Ethics Benchmarks | 46      |
| C         | Cross-Cultural Values Benchmarks             | 52      |
| D         | Moral Psychology & Foundations Benchmarks    | 37      |
| E         | Psychometric & Values Survey Benchmarks      | 5       |
| F         | Meta-Resources & Survey Papers               | 5       |
| **Total** |                                              | **152** |

**Key expansions since v1:**
- Section B (Single-Framework) grew significantly with newly identified focused ethics benchmarks
- Section C (Cross-Cultural) expanded with additional cultural values benchmarks
- Section D (Moral Psychology) gained entries from moral foundations and moral cognition research

**Key gaps remain:** No dedicated benchmarks for Confucian ethics, Ubuntu/African values, Hindu ethics, or Buddhist ethics as standalone evaluation datasets. Care ethics and virtue ethics lack deep standalone benchmarks.

---

## A. Multi-Framework Ethics Benchmarks

### A1. Unnamed (Moral Reasoning Mode Classifier) (Nischal Mainali, 2025)
- **Citation:** [[Mainali, Nischal]] et al. (2025). Automated Classification of Modes of Moral.
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** Classification of moral reasoning modes (consequentialist vs. deontological) in text (judicial decisions and applied ethics articles)
- **Dataset:** Not explicitly stated (applied ethics articles + circuit court opinion corpus)
- **LLMs tested:** Linear SVM classifier
- **Key finding:** Develops an NLP classifier for distinguishing consequentialist vs.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2020-Mainali-Automated Classification of Modes of Moral]]

### A2. ETHICS (Dan Hendrycks, 2025)
- **Citation:** Dan Hendrycks et al. (2025). Aligning AI with Shared Human Values. *International Conference on Learning Representations (ICLR 2021)*.
- **arXiv:** [2008.02275](https://arxiv.org/abs/2008.02275)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Virtue Ethics
- **What it measures:** Language model knowledge of basic moral concepts spanning justice, well-being, duties, virtues, and commonsense morality
- **Dataset:** Large-scale (130k+ examples across categories)
- **LLMs tested:** Various language models including GPT-3, BERT, RoBERTa, ALBERT
- **Key finding:** Foundational benchmark for assessing LLM moral reasoning across multiple normative ethical traditions; one of the most widely used ethics benchmarks.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2021-Hendrycks-Aligning AI with Shared Human Values]]

### A3. Ethical Quandary GQA / AISocrates (Yejin Bang, 2025)
- **Citation:** Yejin Bang et al. (2025). Towards Answering Open-ended Ethical Quandary.
- **arXiv:** [2205.05989](https://arxiv.org/abs/2205.05989) | **DOI:** [10.48550/arXiv.2205.05989](https://doi.org/10.48550/arXiv.2205.05989)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** LLM ability to provide multi-perspective deliberative answers to ethical quandary questions, considering conflicting moral principles (utilitarian vs. deontological)
- **Dataset:** Not specified
- **LLMs tested:** LLMs (evaluated with few-shot in-context learning)
- **Key finding:** Proposes and evaluates the novel task of Ethical Quandary Generative QA, testing whether LLMs can provide multi-perspective moral reasoning rather ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Bang-Towards Answering Open-ended Ethical Quandary]]

### A4. Unnamed (top-down moral reasoning framework) (Jingyan Zhou, 2025)
- **Citation:** Jingyan Zhou et al. (2025). Rethinking Machine Ethics. *Findings of NAACL 2024*.
- **arXiv:** **DOI:** [10.18653/v1/2024.findings-naacl.144](https://doi.org/10.18653/v1/2024.findings-naacl.144)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Virtue Ethics
- **What it measures:** LLM moral reasoning through the lens of established moral theories (deontology, virtue ethics, consequentialism)
- **Dataset:** Not specified
- **LLMs tested:** Multiple LLMs (specific models not listed in abstract)
- **Key finding:** Proposes a framework to steer LLMs for moral reasoning using deontological, virtue ethics, and consequentialist theories.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Zhou-Rethinking Machine Ethics Can LLMs Perform Moral Reasoning]]

### A5. MoReBench / MoReBench-Theory (Yu Ying Chiu, 2025)
- **Citation:** [[Chiu, Yu Ying]] et al. (2025). MoReBench. *arXiv.org*.
- **arXiv:** [2510.16380](https://arxiv.org/abs/2510.16380) | **DOI:** [10.48550/arXiv.2510.16380](https://doi.org/10.48550/arXiv.2510.16380)
- **Frameworks:** Care Ethics, Consequentialist/Utilitarian, Contractualist, Deontological, Virtue Ethics
- **What it measures:** Procedural and pluralistic moral reasoning in LLMs: identifying moral considerations, weighing trade-offs, giving actionable recommendations; reasoning under 5 normative ethics frameworks
- **Dataset:** 1,000 moral scenarios (23,000+ rubric criteria) + 150 theory examples
- **LLMs tested:** Multiple reasoning LLMs (specific models in paper)
- **Key finding:** Major benchmark for evaluating procedural moral reasoning in LLMs with expert-curated rubric criteria and a dedicated theory component testing five....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Chiu-MoReBench]]

### A6. Unnamed (Bryant P.H. Hui, 2025)
- **Citation:** Bryant P.H. Hui et al. (2025). Decoding Moral Responses in AI. *Computers in Human Behavior Reports*.
- **arXiv:** **DOI:** [10.1016/j.chbr.2025.100854](https://doi.org/10.1016/j.chbr.2025.100854)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** Moral reasoning patterns in LLMs - utilitarian vs deontological responses to personal and impersonal moral dilemmas
- **Dataset:** Not specified (series of moral dilemmas)
- **LLMs tested:** GPT-3, GPT-3.5, GPT-4, GPT-4.1, Claude 3.7 Sonnet, Grok 3, Gemini 2.5 Pro
- **Key finding:** Conducts systematic empirical evaluation of seven LLMs using structured moral dilemmas under different ethical framings (deontological and utilitar....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Hui-Decoding Moral Responses in AI]]

### A7. ADEPT (AI Debate Ethics Panel Tool) (Hazem Zohny, 2025)
- **Citation:** [[Zohny, Hazem]] (2025). ADEPT Simulating Ethics.
- **arXiv:** [2505.21112](https://arxiv.org/abs/2505.21112) | **DOI:** [10.48550/arXiv.2505.21112](https://doi.org/10.48550/arXiv.2505.21112)
- **Frameworks:** Care Ethics, Consequentialist/Utilitarian, Deontological
- **What it measures:** Multi-perspective ethical deliberation in LLMs; how panel composition of ethical personas influences moral reasoning outcomes
- **Dataset:** 2 ventilator allocation case studies with 6-persona panels
- **LLMs tested:** LLM personas (specific model not stated in body)
- **Key finding:** Creates a replicable system for multi-agent ethical deliberation with distinct moral perspectives, demonstrating that panel composition materially ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Zohny-ADEPT Simulating Ethics]]

---

## B. Single-Framework / Focused Ethics Benchmarks

### B1. Theory Trace Card (TTC) (F. Karimi-Malekabadi, 2026)
- **Citation:** Karimi-Malekabadi, F. et al. (2026). Theory Trace Card (TTC): Documentation for Socio-Cognitive Benchmarks. *arXiv*.
- **arXiv:** [2601.01878](https://arxiv.org/abs/2601.01878)
- **What it measures:** Proposes a documentation standard for socio-cognitive evaluations of LLMs including moral reasoning benchmarks; addresses validity gaps in existing evaluations
- **Dataset:** N/A (methodological/framework contribution)
- **LLMs tested:** N/A (meta-evaluation framework)
- **Key finding:** While not a benchmark itself, TTC proposes a structured methodology for documenting and validating socio-cognitive benchmarks including moral reaso....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks]]

### B2. Multi-Dimensional Moral Competence Assessment (Snoswell, 2026)
- **Citation:** Snoswell (2026). Beyond Verdicts Evaluating Language Model Moral Competence.
- **What it measures:** Five dimensions of moral competence: identifying morally relevant features, weighting importance, assigning moral reasons, synthesizing coherent judgments, and recognizing information gaps
- **Dataset:** Novel ethical vignettes (not specified)
- **LLMs tested:** 6 leading LLMs compared against humans and professional philosophers
- **Key finding:** Proposes a novel methodology for assessing moral competence that goes beyond simple verdict comparison, evaluating five distinct dimensions of mora....
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### B3. Moral Choice Machine (MCM) (Patrick Schramowski, 2025)
- **Citation:** [[Schramowski, Patrick]] et al. (2025). The Moral Choice Machine.
- **arXiv:** **DOI:** [10.3389/frai.2020.00036](https://doi.org/10.3389/frai.2020.00036)
- **Frameworks:** Deontological
- **What it measures:** Deontological ethical reasoning about right and wrong conduct extracted from text corpora; moral bias scores for actions in context
- **Dataset:** Not specified (template list of prompts/responses applied to actions)
- **LLMs tested:** Universal Sentence Encoder on various corpora (Bible, constitutions, news, books from 1510-2008)
- **Key finding:** Creates a method and evaluation framework for extracting and quantifying moral choices from text embeddings, comparing across cultures and time per....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2020-Schramowski-The Moral Choice Machine]]

### B4. Moral Stories (Denis Emelin, 2025)
- **Citation:** Denis Emelin et al. (2025). Moral Stories.
- **arXiv:** **DOI:** [10.18653/v1/2021.emnlp-main.54](https://doi.org/10.18653/v1/2021.emnlp-main.54)
- **What it measures:** Grounded, goal-oriented social reasoning and norm adherence in language models; ability to generate norm-conforming actions, anticipate consequences, and explain norms
- **Dataset:** Crowd-sourced dataset (not specified in body, but referenced as large-scale)
- **LLMs tested:** Language generation models with expert decoding strategies
- **Key finding:** Introduces a crowd-sourced dataset of structured moral narratives specifically designed to evaluate social reasoning and norm adherence in NLG models.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2021-Emelin-Moral Stories]]

### B5. SCRUPLES (Nicholas Lourie, 2025)
- **Citation:** Nicholas Lourie et al. (2025). Scruples. *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI-21)*.
- **arXiv:** [2008.09094](https://arxiv.org/abs/2008.09094) | **DOI:** [10.48550/arXiv.2008.09094](https://doi.org/10.48550/arXiv.2008.09094)
- **What it measures:** Descriptive ethics and moral judgment in real-life interpersonal situations; community ethical norms and the 'who is in the wrong' judgment task
- **Dataset:** 625,000 ethical judgments over 32,000 anecdotes
- **LLMs tested:** State-of-the-art neural language models (BERT-era)
- **Key finding:** Large-scale dataset of real-world ethical situations with community moral judgments, explicitly designed for training and evaluating machine ethics....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2021-Lourie-Scruples]]

### B6. Commonsense Norm Bank / Delphi (Liwei Jiang, 2025)
- **Citation:** Liwei Jiang et al. (2025). Can Machines Learn Morality?.
- **arXiv:** [2110.07574](https://arxiv.org/abs/2110.07574) | **DOI:** [10.48550/arXiv.2110.07574](https://doi.org/10.48550/arXiv.2110.07574)
- **What it measures:** Commonsense moral judgments across diverse social situations - whether actions are ethical, unethical, or morally ambiguous
- **Dataset:** Commonsense Norm Bank (aggregation of multiple moral datasets); ETHICS benchmark used for evaluation
- **LLMs tested:** Delphi (based on UNICORN/T5)
- **Key finding:** Introduces the Delphi experiment - a landmark study training a model on the Commonsense Norm Bank to make moral judgments.
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2022-Jiang-Can Machines Learn Morality]]

### B7. MoralDial (Hao Sun, 2025)
- **Citation:** Hao Sun et al. (2025). MoralDial. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2212.10720](https://arxiv.org/abs/2212.10720) | **DOI:** [10.48550/arXiv.2212.10720](https://doi.org/10.48550/arXiv.2212.10720)
- **What it measures:** Morality in dialogue systems - ability to express, explain, revise, and infer moral views in conversational exchanges aligned with human values
- **Dataset:** Not specified in paper profile
- **LLMs tested:** Conversational models (details in full paper)
- **Key finding:** Proposes a framework for training and evaluating moral dialogue systems through structured moral discussions.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2022-Sun-MoralDial]]

### B8. Unnamed (Virtue Ethics Game Environment) (Ajay Vishwanath, 2025)
- **Citation:** Ajay Vishwanath et al. (2025). Towards Artificial Virtuous Agents - Games and ML. *AI and Ethics*.
- **arXiv:** **DOI:** [10.1007/s43681-022-00251-8](https://doi.org/10.1007/s43681-022-00251-8)
- **Frameworks:** Virtue Ethics
- **What it measures:** Virtue development in artificial agents through moral dilemmas in role-playing games
- **LLMs tested:** RL agents in game environment
- **Key finding:** Proposes using role-playing games with moral dilemmas to develop and evaluate virtue in AI agents.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML]]

### B9. MACHIAVELLI (Alexander Pan, 2025)
- **Citation:** Alexander Pan et al. (2025). MACHIAVELLI.
- **arXiv:** [2304.03279](https://arxiv.org/abs/2304.03279)
- **What it measures:** Ethical behavior in AI agents; measures trade-offs between reward maximization and ethical behavior including power-seeking, deception, disutility, and ethical violations
- **Dataset:** 134 games, 500,000+ scenarios
- **LLMs tested:** GPT-4, RL agents, various LM-based agents
- **Key finding:** Directly benchmarks ethical behavior in AI agents through rich social decision-making scenarios, measuring Machiavellian tendencies (power-seeking,....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2023-Jiang-MACHIAVELLI]]

### B10. MoralChoice (Nino Scherrer, 2025)
- **Citation:** Nino Scherrer et al. (2025). Evaluating the Moral Beliefs Encoded in LLMs. *Neural Information Processing Systems*.
- **arXiv:** [2307.14324](https://arxiv.org/abs/2307.14324) | **DOI:** [10.48550/arXiv.2307.14324](https://doi.org/10.48550/arXiv.2307.14324)
- **What it measures:** Moral beliefs encoded in LLMs, measuring consistency and uncertainty of moral choices in high- and low-ambiguity scenarios
- **Dataset:** 1,367 moral scenarios (680 high-ambiguity + 687 low-ambiguity)
- **LLMs tested:** 28 open- and closed-source LLMs
- **Key finding:** Introduces MoralChoice, a comprehensive survey of 1,367 moral scenarios administered to 28 LLMs.
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs]]

### B11. ValueLex (Pablo Biedma, 2025)
- **Citation:** [[Biedma, Pablo]] et al. (2025). Beyond Human Norms. *arXiv.org*.
- **arXiv:** [2404.12744](https://arxiv.org/abs/2404.12744) | **DOI:** [10.48550/arXiv.2404.12744](https://doi.org/10.48550/arXiv.2404.12744)
- **Frameworks:** Virtue Ethics
- **What it measures:** Intrinsic value systems of LLMs (Competence, Character, Integrity dimensions), reconstructed from scratch using psychological methodology rather than human-centric frameworks
- **Dataset:** Value descriptors from 30+ LLMs; projective test scenarios
- **LLMs tested:** 30+ LLMs including LLaMA, GPT series, and others
- **Key finding:** Proposes ValueLex, a novel framework that reconstructs LLM value systems from scratch using interdisciplinary psychological methods, revealing non-....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Biedma-Beyond Human Norms]]

### B12. SaGE / Moral Consistency Corpus (MCC) (Vamshi Krishna Bonagiri, 2025)
- **Citation:** Vamshi Krishna Bonagiri et al. (2025). SaGE. *International Conference on Language Resources and Evaluation*.
- **arXiv:** [2402.13709](https://arxiv.org/abs/2402.13709) | **DOI:** [10.48550/arXiv.2402.13709](https://doi.org/10.48550/arXiv.2402.13709)
- **What it measures:** Moral consistency of LLM generations using information-theoretic measure based on Rules of Thumb (RoTs)
- **Dataset:** 50,000 moral questions with responses and RoTs
- **LLMs tested:** Multiple state-of-the-art LLMs
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Bonagiri-SaGE]]

### B13. UniVaR (Universal Value Representation) (Samuel Cahyawijaya, 2025)
- **Citation:** Samuel Cahyawijaya et al. (2025). High-Dimension Human Value Representation in. *North American Chapter of the Association for Computational Linguistics*.
- **arXiv:** [2404.07900](https://arxiv.org/abs/2404.07900) | **DOI:** [10.48550/arXiv.2404.07900](https://doi.org/10.48550/arXiv.2404.07900)
- **What it measures:** Human value distributions across LLMs in 25 languages, providing high-dimensional continuous representation of symbolic value orientations
- **Dataset:** Value-relevant outputs from 8 LLMs across 25 languages
- **LLMs tested:** 8 LLMs for training, 15 open-source and commercial LLMs for evaluation
- **Key finding:** Proposes UniVaR, a continuous high-dimensional representation of human values in LLMs, enabling visualization and analysis of value distributions a....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Cahyawijaya-High-Dimension Human Value Representation in]]

### B14. Unnamed (uses Moral Integrity Corpus) (Pierre Dognin, 2025)
- **Citation:** Pierre Dognin et al. (2025). Contextual Moral Value Alignment Through. *arXiv.org*.
- **arXiv:** [2403.12805](https://arxiv.org/abs/2403.12805) | **DOI:** [10.48550/arXiv.2403.12805](https://doi.org/10.48550/arXiv.2403.12805)
- **What it measures:** Contextual moral value alignment - whether LLMs can adaptively align responses with different moral values depending on context
- **Dataset:** Uses MIC dataset (Ziems et al., 2022)
- **LLMs tested:** Multiple LLM-based dialogue agents
- **Key finding:** Proposes a system for contextual moral value alignment and evaluates it using the Moral Integrity Corpus, substantively using structured moral eval....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Dognin-Contextual Moral Value Alignment Through]]

### B15. Unnamed (contrast sets for Moral Stories) (Ben Fitzgerald, 2025)
- **Citation:** Ben Fitzgerald (2025). Some Issues in Predictive Ethics Modeling.
- **arXiv:** [2407.05244](https://arxiv.org/abs/2407.05244)
- **What it measures:** Robustness of ethics classification models (e.g., Delphi) to adversarial perturbations; tests whether models genuinely reason about ethics or rely on textual bias
- **Dataset:** Contrast set annotations on Moral Stories dataset
- **LLMs tested:** Classifiers trained on Moral Stories (including Delphi-style models)
- **Key finding:** Creates adversarial contrast sets specifically for evaluating ethics classification models, demonstrating that predictive ethics models overfit and....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]]

### B16. Unnamed (critique of ETHICS benchmark) (Leif Hancox-Li, 2025)
- **Citation:** Leif Hancox-Li & Borhane Blili-Hamelin (2025). Is ETHICS about ethics?. *arXiv.org*.
- **arXiv:** [2410.13009](https://arxiv.org/abs/2410.13009) | **DOI:** [10.48550/arXiv.2410.13009](https://doi.org/10.48550/arXiv.2410.13009)
- **What it measures:** Validity of the ETHICS benchmark for testing genuine ethical capabilities of LLMs; distinguishes commonsense pattern matching from real ethical reasoning
- **Dataset:** Analysis of existing ETHICS benchmark
- **LLMs tested:** Language models evaluated on ETHICS benchmark
- **Key finding:** Directly evaluates and critiques the most-cited ethics benchmark (ETHICS) for LLMs.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Hancox-Li-Is ETHICS about ethics]]

### B17. Unnamed (uses ETHICS benchmark + BrainScore) (Artem Karpov, 2025)
- **Citation:** Artem Karpov et al. (2025). Inducing Human-like Biases in Moral Reasoning. *arXiv.org*.
- **arXiv:** [2411.15386](https://arxiv.org/abs/2411.15386) | **DOI:** [10.48550/arXiv.2411.15386](https://doi.org/10.48550/arXiv.2411.15386)
- **What it measures:** Alignment between LLM moral reasoning and human brain activity (fMRI) during moral tasks; moral reasoning accuracy
- **Dataset:** ETHICS benchmark (common sense category) + Koster-Hale fMRI moral reasoning dataset
- **LLMs tested:** BERT, RoBERTa, DeBERTa
- **Key finding:** Substantively uses the ETHICS benchmark for moral reasoning evaluation and proposes BrainScore as a novel metric for mechanistic moral alignment be....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Karpov-Inducing Human-like Biases in Moral Reasoning]]

### B18. Unnamed (Chinese Moral Choice Scenarios) (Xuelin Liu, 2025)
- **Citation:** [[Liu, Xuelin]] et al. (2025). Evaluating Moral Beliefs across LLMs through a. *Conference on Empirical Methods in Natural Language Processing*.
- **arXiv:** [2411.03665](https://arxiv.org/abs/2411.03665) | **DOI:** [10.48550/arXiv.2411.03665](https://doi.org/10.48550/arXiv.2411.03665)
- **What it measures:** Moral beliefs and moral principle preferences in LLMs, comparing individualistic vs collectivist moral orientations
- **Dataset:** 472 moral choice scenarios
- **LLMs tested:** ChatGPT, Gemini, Ernie, ChatGLM
- **Key finding:** Introduces a novel three-module framework with 472 Chinese moral choice scenarios to evaluate and compare moral beliefs across LLMs, explicitly com....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Liu-Evaluating Moral Beliefs across LLMs through a]]

### B19. Greatest Good Benchmark (GGB) (Giovanni Franco Gabriel Marraffini, 2025)
- **Citation:** Giovanni Franco Gabriel Marraffini et al. (2025). The Greatest Good Benchmark.
- **arXiv:** **DOI:** [10.18653/v1/2024.emnlp-main.1224](https://doi.org/10.18653/v1/2024.emnlp-main.1224)
- **Frameworks:** Consequentialist/Utilitarian
- **What it measures:** LLM alignment with utilitarian moral dilemmas, specifically instrumental harm and impartial beneficence
- **Dataset:** Not specified
- **LLMs tested:** 15 diverse LLMs
- **Key finding:** Explicitly designed benchmark for evaluating LLM moral judgments using utilitarian dilemmas, with direct human-LLM comparison across 15 models.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Marraffini-The Greatest Good Benchmark]]

### B20. GovSim (Governance of the Commons Simulation) (Giorgio Piatti, 2025)
- **Citation:** Giorgio Piatti et al. (2025). Cooperate or Collapse. *Neural Information Processing Systems*.
- **arXiv:** [2404.16698](https://arxiv.org/abs/2404.16698) | **DOI:** [10.48550/arXiv.2404.16698](https://doi.org/10.48550/arXiv.2404.16698)
- **What it measures:** LLM cooperative decision-making, ethical reasoning, strategic planning, and ability to avoid tragedy-of-the-commons scenarios
- **Dataset:** Simulation-based (multiple scenarios)
- **LLMs tested:** Leading open and closed LLMs (highest survival rate below 54%)
- **Key finding:** Introduces GovSim, a simulation platform testing LLM ethical cooperation and moral reasoning in strategic settings, finding that universalization-b....
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2024-Piatti-Cooperate or Collapse]]

### B21. Moral High Ground (Matthew Pisano, 2025)
- **Citation:** Matthew Pisano et al. (2025). Moral High Ground.
- **What it measures:** Moral and ethical reasoning abilities of LLMs through interactive text-based game environments covering moral values and business principles
- **Dataset:** Multiple text-based games with moral scenarios
- **LLMs tested:** Flan-UL2, Flan-T5, Falcon, Open Assistant, Llama2
- **Key finding:** Novel interactive benchmark using text-based games to evaluate and train LLMs on moral and ethical reasoning, with reward-based scoring of moral be....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Pisano-Moral High Ground]]

### B22. ValuePrism / Value Kaleidoscope (Kaleido) (Taylor Sorensen, 2025)
- **Citation:** [[Sorensen, Taylor]] et al. (2025). Value Kaleidoscope. *arXiv*.
- **arXiv:** [2309.00779](https://arxiv.org/abs/2309.00779) | **DOI:** [10.1609/aaai.v38i18.29970](https://doi.org/10.1609/aaai.v38i18.29970)
- **What it measures:** Pluralistic human values, rights, and duties in context; ability to model value conflicts and pluralism
- **Dataset:** 218,000 values, rights, and duties linked to 31,000 situations
- **LLMs tested:** GPT-4, Kaleido, evaluated with diverse human annotators
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Sorensen-Value Kaleidoscope]]

### B23. SafetyBench (Zhexin Zhang, 2025)
- **Citation:** Zhexin Zhang et al. (2025). SafetyBench. *ACL 2024*.
- **arXiv:** [2309.07045](https://arxiv.org/abs/2309.07045)
- **What it measures:** LLM safety across 7 categories (offense, ethics, physical harm, etc.) in Chinese and English
- **Dataset:** 11,435 questions across 7 categories
- **Code:** [GitHub](https://github.com/thu-coai/SafetyBench)
- **LLMs tested:** 25 Chinese and English LLMs including GPT-4
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Zhang-SafetyBench]]

### B24. Deep Value Benchmark (DVB) (Joshua Ashkinaze, 2025)
- **Citation:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak (2025). Deep Value Benchmark. *NeurIPS 2025*.
- **arXiv:** [2511.02109](https://arxiv.org/abs/2511.02109)
- **What it measures:** Whether LLMs learn fundamental human values (e.g., non-maleficence, justice) or merely surface-level preferences; Deep Value Generalization Rate (DVGR)
- **Dataset:** Not specified (dataset with controlled confounds, three human validation experiments)
- **LLMs tested:** 9 different models
- **Key finding:** Directly tests whether LLMs internalize deep moral values (non-maleficence, justice) vs shallow preferences.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Ashkinaze-Deep Value Benchmark]]

### B25. MORALSIM (Steffen Backmann, 2025)
- **Citation:** [[Backmann, Steffen]] et al. (2025). When Ethics and Payoffs Diverge. *arXiv preprint*.
- **arXiv:** [2505.19212](https://arxiv.org/abs/2505.19212) | **DOI:** [10.48550/arXiv.2505.19212](https://doi.org/10.48550/arXiv.2505.19212)
- **What it measures:** LLM moral behavior in social dilemmas where moral imperatives conflict with rewards/incentives
- **Dataset:** 2 game types x 3 moral framings
- **Code:** [GitHub](https://github.com/sbackmann/moralsim)
- **LLMs tested:** Range of frontier models
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Backmann-When Ethics and Payoffs Diverge]]

### B26. Healthcare Ethics & Safety QA Benchmark (Mouxiao Bian, 2025)
- **Citation:** Mouxiao Bian, Rongzhao Zhang, Chao Ding, Xinwei Peng, and Jie Xu (2025). Healthcare Ethics & Safety QA (China -- Healthy China 2030). *arXiv preprint*.
- **arXiv:** [2505.07205](https://arxiv.org/abs/2505.07205)
- **Frameworks:** Care Ethics
- **What it measures:** Ethical and patient-safety reasoning of LLMs in medical contexts, covering 11 ethics dimensions and 9 safety dimensions
- **Dataset:** 12,000 question-answer items
- **LLMs tested:** Qwen 2.5-32B, DeepSeek, and other Chinese medical LLMs
- **Key finding:** Introduces a novel 12,000-item Q&A benchmark specifically for evaluating healthcare LLMs on ethics and safety dimensions in the Chinese medical con....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030]]

### B27. LITMUSVALUES / AIRISKDILEMMAS (Yu Ying Chiu, 2025)
- **Citation:** Yu Ying Chiu et al. (2025). Will AI Tell Lies to Save Sick Children?. *arXiv.org*.
- **arXiv:** [2505.14633](https://arxiv.org/abs/2505.14633) | **DOI:** [10.48550/arXiv.2505.14633](https://doi.org/10.48550/arXiv.2505.14633)
- **What it measures:** AI value prioritization and its connection to risky behaviors (e.g., power seeking, lying); 16 shared AI value classes drawn from Anthropic's Constitution and OpenAI ModelSpec
- **Dataset:** 16 value classes; dilemma set size not specified in abstract
- **LLMs tested:** Multiple AI models (specific models in paper)
- **Key finding:** Creates LITMUSVALUES evaluation pipeline and AIRISKDILEMMAS dataset to reveal AI models' value priorities through revealed preferences in dilemma s....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Chiu-Will AI Tell Lies to Save Sick Children]]

### B28. MoCoP (Moral Consistency Pipeline) (Jamshidi, 2025)
- **Citation:** Jamshidi (2025). The Moral Consistency Pipeline MoCoP.
- **What it measures:** Moral consistency and ethical stability of LLMs across contexts and temporal scales
- **Dataset:** Dataset-free (auto-generated)
- **LLMs tested:** GPT-4-Turbo, DeepSeek
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### B29. Delphi / DelphiHYBRID (L. Jiang, 2025)
- **Citation:** Liwei Jiang et al. (2025). Investigating Machine Moral Judgement Through the Delphi Experiment (DelphiHYBRID). *Nature Machine Intelligence*.
- **arXiv:** **DOI:** [10.1038/s42256-024-00969-6](https://doi.org/10.1038/s42256-024-00969-6)
- **Frameworks:** Contractualist
- **What it measures:** Machine moral judgment - ability to predict human moral judgments about everyday situations; incorporates Gert's 10 moral principles as symbolic constraints
- **Dataset:** Commonsense Norm Bank (large-scale, exact size not stated in excerpt)
- **Code:** [GitHub](https://github.com/liweijiang/delphi)
- **LLMs tested:** Delphi system (based on neural language models), compared with off-the-shelf LMs
- **Key finding:** Builds and evaluates Delphi, an AI system designed to predict human moral judgments.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment]]

### B30. Unnamed (Multi-Dimensional Moral Competence Assessment) (Kilov, 2025)
- **Citation:** Kilov (2025). Discerning What Matters Multi-Dimensional Moral Competence Assessment.
- **What it measures:** Moral competence in LLMs across five dimensions: identifying morally relevant features, weighting importance, assigning moral reasons, synthesizing judgments, recognizing information gaps
- **Dataset:** 12 novel moral vignettes plus standard vignettes
- **LLMs tested:** Six leading LLMs (Claude 3.7, GPT-4o, Gemini 1.5, Llama 3.3, etc.)
- **Key finding:** Introduces a novel methodology for assessing moral competence in LLMs with five distinct evaluation dimensions and novel 'noisy' moral vignettes.
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### B31. Unnamed (Multi-Dimensional Moral Competence Assessment) (Daniel Kilov, 2025)
- **Citation:** [[Kilov, Daniel]] et al. (2025). Discerning What Matters. *arXiv.org*.
- **arXiv:** [2506.13082](https://arxiv.org/abs/2506.13082) | **DOI:** [10.48550/arXiv.2506.13082](https://doi.org/10.48550/arXiv.2506.13082)
- **What it measures:** Moral competence across five dimensions including moral discernment, feature weighting, reason assignment, judgment synthesis, information gap recognition
- **Dataset:** 12 novel vignettes + standard set
- **LLMs tested:** Claude 3.7, GPT-4o, Gemini 1.5 Flash, Llama 3.3, and others
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Kilov-Discerning What Matters]]

### B32. CLASH (Character perspective-based LLM Assessments in Situations with High-stakes) (A. Lee, 2025)
- **Citation:** Lee, A. et al. (2025). CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives. *arXiv*.
- **arXiv:** [2504.10823](https://arxiv.org/abs/2504.10823)
- **Frameworks:** Virtue Ethics
- **What it measures:** Value-based decision-making in high-stakes dilemmas - decision ambivalence, psychological discomfort, temporal value shifts, value steerability
- **Dataset:** 345 dilemmas, 3,795 perspectives
- **LLMs tested:** 14 models including GPT-5, Claude-4-Sonnet (thinking and non-thinking)
- **Key finding:** Creates CLASH, a meticulously curated dataset of high-stakes dilemmas with diverse value perspectives.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from]]

### B33. Moral Reasoning Diagnosis Framework (Guangliang Liu, 2025)
- **Citation:** Guangliang Liu et al. (2025). Diagnosing Moral Reasoning Acquisition in. *Conference on Empirical Methods in Natural Language Processing*.
- **arXiv:** [2502.16600](https://arxiv.org/abs/2502.16600) | **DOI:** [10.48550/arXiv.2502.16600](https://doi.org/10.48550/arXiv.2502.16600)
- **What it measures:** Moral reasoning acquisition in LLMs; pragmatic dilemma in ethical judgment generalization
- **Dataset:** Uses existing moral reasoning datasets
- **LLMs tested:** Multiple LLMs
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Liu-Diagnosing Moral Reasoning Acquisition in]]

### B34. EthicsSuite (Pingchuan Ma, 2025)
- **Citation:** [[Ma, Pingchuan]] et al. (2025). EthicsSuite: Detecting Behavioral Inconsistency in LLM Ethics Suggestions. *ACM TOSEM*.
- **arXiv:** **DOI:** [10.1145/3722554](https://doi.org/10.1145/3722554)
- **Frameworks:** Deontological
- **What it measures:** Behavioral inconsistency in LLM ethics-related suggestions; detects unethical biases through contradiction rather than defining absolute ethical standards
- **Dataset:** 20K moral situations
- **Code:** [GitHub](https://github.com/LLM-Ethics/EthicsSuite) | [GitHub](https://github.com/LLM-Ethics/SCR)
- **LLMs tested:** 8 LLMs including GPT-4, Claude, ChatGPT, Llama-7B, Llama-13B, ChatGLM, Vicuna, GPT-Neo
- **Key finding:** Creates EthicsSuite with 20K moral situations and an innovative reflective equilibrium-based test oracle for detecting ethical inconsistency in LLMs.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics]]

### B35. MORABLES (M. Marcuzzo, 2025)
- **Citation:** Marcuzzo, M. et al. (2025). MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables. *EMNLP*.
- **arXiv:** [2509.12371](https://arxiv.org/abs/2509.12371)
- **What it measures:** Abstract moral reasoning capability of LLMs using fables and short stories from historical literature; moral inference beyond shallow extractive QA
- **Dataset:** Literature-based benchmark from fables (exact size not specified)
- **LLMs tested:** Multiple LLMs of varying sizes including reasoning-enhanced models
- **Key finding:** Creates a benchmark specifically for abstract moral reasoning in LLMs using fables, with adversarial variants.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs]]

### B36. PapersPlease (Junho Myung, 2025)
- **Citation:** Junho Myung et al. (2025). PapersPlease. *arXiv.org*.
- **arXiv:** [2506.21961](https://arxiv.org/abs/2506.21961) | **DOI:** [10.48550/arXiv.2506.21961](https://doi.org/10.48550/arXiv.2506.21961)
- **What it measures:** LLM decision-making in moral dilemmas involving prioritization of human needs (Existence, Relatedness, Growth) and implicit biases toward social identities
- **Dataset:** 3,700 moral dilemma scenarios
- **Code:** [GitHub](https://github.com/yeonsuuuu28/papersplease)
- **LLMs tested:** 6 LLMs (specific models not listed in profile)
- **Key finding:** Creates a benchmark of moral dilemmas testing LLM value prioritization in ethically charged role-playing scenarios.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Myung-PapersPlease]]

### B37. OvertonScore (E. Poole-Dayan, 2025)
- **Citation:** Elinor Poole-Dayan et al. (2025). OvertonScore: Benchmarking Overton Pluralism in LLMs. *arXiv*.
- **arXiv:** [2512.01351](https://arxiv.org/abs/2512.01351)
- **What it measures:** Overton pluralism in LLMs — the extent to which diverse viewpoints are represented in model outputs
- **Dataset:** 60 questions, 1,209 human respondents, 8 LLMs
- **LLMs tested:** 8 LLMs including DeepSeek V3 (best performer)
- **Key finding:** Introduces a novel metric and benchmark for measuring viewpoint pluralism in LLMs.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Poole-Dayan-OvertonScore Benchmarking Overton Pluralism in LLMs]]

### B38. Moral Dilemma Dataset + Dynamic Moral Profiling (DMP) (Giuseppe Russo, 2025)
- **Citation:** Giuseppe Russo et al. (2025). The Pluralistic Moral Gap. *arXiv.org*.
- **arXiv:** [2507.17216](https://arxiv.org/abs/2507.17216) | **DOI:** [10.48550/arXiv.2507.17216](https://doi.org/10.48550/arXiv.2507.17216)
- **What it measures:** Pluralistic alignment of LLM moral judgments with diverse human moral perspectives — measures both judgment distributions and value diversity
- **Dataset:** 1,618 dilemmas, 3,783 value expressions, 60-value taxonomy
- **LLMs tested:** Multiple LLMs (specific models not listed in profile)
- **Key finding:** Creates a benchmark and methodology specifically for evaluating pluralistic moral alignment.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Russo-The Pluralistic Moral Gap]]

### B39. LLM Debate Moral Deliberation Framework (Pratik S. Sachdeva, 2025)
- **Citation:** [[Sachdeva, Pratik S.]] & [[van Nuenen, Tom]] (2025). Deliberative Dynamics and Value Alignment.
- **arXiv:** [2510.10002](https://arxiv.org/abs/2510.10002) | **DOI:** [10.48550/arXiv.2510.10002](https://doi.org/10.48550/arXiv.2510.10002)
- **What it measures:** Value alignment and deliberative dynamics in multi-turn LLM moral reasoning — how models revise verdicts, express values, and respond to deliberation format effects
- **Dataset:** 1,000 everyday dilemmas from Reddit AITA
- **LLMs tested:** GPT-4.1, Claude 3.7 Sonnet, Gemini 2.0 Flash
- **Key finding:** Conducts structured empirical evaluation of LLM moral reasoning in multi-turn deliberation settings.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Sachdeva-Deliberative Dynamics and Value Alignment]]

### B40. Moral Dilemma Response Analysis (SOCIALSENSE-related) (Chenkai Sun, 2025)
- **Citation:** Chenkai Sun et al. (2025). Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models. *Unknown*.
- **arXiv:** **DOI:** [10.1016/j.chbah.2025.100121](https://doi.org/10.1016/j.chbah.2025.100121)
- **What it measures:** Moral response patterns in LLMs using moral dilemmas (personal and impersonal)
- **Dataset:** Series of moral dilemmas (size not fully specified)
- **LLMs tested:** Large language models (specific models not fully extracted)
- **Key finding:** Paper body is thin and PDF extract appears mismatched.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large]]

### B41. JETHICS (Masashi Takeshita, 2025)
- **Citation:** Masashi Takeshita & Rafal Rzepka (2025). JETHICS. *arXiv.org*.
- **arXiv:** [2506.16187](https://arxiv.org/abs/2506.16187) | **DOI:** [10.48550/arXiv.2506.16187](https://doi.org/10.48550/arXiv.2506.16187)
- **What it measures:** Japanese ethics understanding evaluation
- **Dataset:** 77,896 examples
- **LLMs tested:** GPT-4o, Japanese LLMs
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Takeshita-JETHICS]]

### B42. SocialEval (Jinfeng Zhou, 2025)
- **Citation:** Jinfeng Zhou et al. (2025). SocialEval: Evaluating Social Intelligence of Large Language Models. *ACL 2025*.
- **arXiv:** [2506.00900](https://arxiv.org/abs/2506.00900)
- **What it measures:** Social intelligence of LLMs including prosociality and social behavior in navigating interpersonal interactions to achieve social goals
- **Dataset:** Manually crafted narrative scripts (bilingual)
- **Code:** [GitHub](https://github.com/thu-coai/SocialEval)
- **LLMs tested:** Multiple LLMs (not specified in abstract)
- **Key finding:** Evaluates LLM social intelligence including prosocial behavior and moral preferences in social interactions.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Zhou-SocialEval Evaluating Social Intelligence of Large Language Models]]

### B43. GenMO (Gender-bias in Morality Opinions) (Divij Bajaj, 2024)
- **Citation:** Divij Bajaj, Yuanyuan Lei, Jonathan Tong, Ruihong Huang (2024). GenMO (Gender-bias in Morality Opinions). *EMNLP 2024*.
- **arXiv:** **DOI:** [10.18653/v1/2024.findings-emnlp.928](https://doi.org/10.18653/v1/2024.findings-emnlp.928)
- **Frameworks:** Virtue Ethics
- **What it measures:** Gender bias in LLM moral judgments; whether LLMs give different moral opinions based on character gender
- **Dataset:** Parallel short stories (exact count in full paper; production models showed bias in 24-85% of samples)
- **LLMs tested:** GPT-3.5-turbo, GPT-3.5-turbo-instruct, GPT-4-turbo, Llama 3 (8B/70B), Llama 3.1 (8B/70B), Mistral-7B, Claude 3 Sonnet...
- **Key finding:** Creates a dataset of parallel moral stories with gender-swapped characters to evaluate LLM bias in moral decision-making.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Bajaj-GenMO Gender-bias in Morality Opinions]]

### B44. Moral Association Graph (MAG) (A. & Xu Ramezani, 2024)
- **Citation:** Ramezani, A. & Xu, Y. (2024). Moral Association Graph: Cognitive Model for Interpretable Moral Inference. *Topics in Cognitive Science*.
- **arXiv:** **DOI:** [10.1111/tops.12774](https://doi.org/10.1111/tops.12774)
- **What it measures:** Interpretable moral inference using a cognitive model based on word association networks grounded in psychological data
- **Dataset:** Not specified (PDF extract was corrupted - only 1 page extracted)
- **LLMs tested:** Not specified in available text
- **Key finding:** Proposes a cognitive model for interpretable moral inference grounded in psychological data.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Ramezani-Moral Association Graph Cognitive Model for Interpretable Moral]]

### B45. MoralExceptQA (Jin et al., 2022)
- **Citation:** Jin, Z., Levine, S., Gonzalez Adauto, F., Kamal, O., Sap, M., Sachan, M., Mihalcea, R., Tenenbaum, J., & Schölkopf, B. (2022). When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment. *NeurIPS 2022*.
- **arXiv:** [2210.01478](https://arxiv.org/abs/2210.01478)
- **Frameworks:** Deontological (testing when rules can be permissibly broken)
- **Dataset:** 148 rule-breaking scenarios across 3 subsets; human agreement percentages included
- **Code:** [GitHub](https://github.com/feradauto/MoralCoT) | [HuggingFace](https://huggingface.co/datasets/feradauto/MoralExceptQA)
- **LLMs tested:** Delphi, GPT-3, InstructGPT + 7 baselines; MoralCoT outperforms by 6.2% F1
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### B46. Right vs. Right (Yuan et al., 2024)
- **Citation:** Yuan, J., Murukannaiah, P.K., & Singh, M.P. (2024). Right vs. Right: Can LLMs Make Tough Choices?
- **arXiv:** [2412.19926](https://arxiv.org/abs/2412.19926)
- **Frameworks:** Kidder's ethical dilemma framework (Truth vs. Loyalty, Individual vs. Community, Short-term vs. Long-term, Justice vs. Mercy); larger LLMs show deontological tendency
- **Dataset:** 1,730 ethical dilemmas, 4 value-conflict pairs
- **LLMs tested:** 20 models from 6 families (OpenAI, Anthropic, Meta, Mistral, Alibaba, 01-AI)
- **Code:** No public repository confirmed
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

---

## C. Cross-Cultural Values Benchmarks

### C1. ValAct-15K (Jen-tse Huang, 2026)
- **Citation:** Jen-tse Huang et al. (2026). Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs (ValAct-15k). *arXiv preprint*.
- **arXiv:** [2601.07972](https://arxiv.org/abs/2601.07972)
- **Frameworks:** World Values Survey
- **What it measures:** Knowledge-action gap in LLM value alignment; whether LLMs can enact values (not just report them) using Schwartz Theory of Basic Human Values
- **Dataset:** 3,000 scenarios (15,000 total with dimensions)
- **LLMs tested:** 10 frontier LLMs (5 US, 5 Chinese companies)
- **Key finding:** Creates ValAct-15K dataset for evaluating enacted vs.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2026-Huang-Knowing But Not Doing Convergent Morality and Divergent Action in]]

### C2. VAPT (Value-Alignment Perception Toolkit) (S. Yun, 2026)
- **Citation:** Yun, S. et al. (2026). VAPT: Value-Alignment Perception Toolkit. *arXiv*.
- **arXiv:** [2601.22440](https://arxiv.org/abs/2601.22440)
- **What it measures:** How LLMs reflect people's values and how people judge those reflections; evaluates AI's ability to extract, embody, and explain human values
- **Dataset:** 20 participants over month-long interaction + 2-hour interviews
- **LLMs tested:** Chatbot system (not specified)
- **Key finding:** Creates a novel evaluation toolkit for assessing value alignment perception through naturalistic long-term interactions, identifying 'weaponized em....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2026-Yun-VAPT Value-Alignment Perception Toolkit]]

### C3. Moral Machine (Edmond Awad, 2025)
- **Citation:** Edmond Awad et al. (2025). The Moral Machine experiment.
- **arXiv:** **DOI:** [10.1038/s41586-018-0637-6](https://doi.org/10.1038/s41586-018-0637-6)
- **What it measures:** Cross-cultural moral preferences for autonomous vehicle ethical dilemmas (trolley-problem variants); measures preferences for sparing lives based on age, gender, status, species, number, legality
- **Dataset:** 40 million decisions from 2.3 million participants
- **LLMs tested:** Not LLMs directly, but the dataset/platform provides moral preference data for training AI decision-making systems (u...
- **Key finding:** Creates the Moral Machine platform and dataset of 40M moral decisions used for developing machine ethics.
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2018-Awad-The Moral Machine experiment]]

### C4. Moral Machine Classic Mode Dataset (Edmond Awad, 2025)
- **Citation:** Edmond Awad et al. (2025). Universals and variations in moral decisions made.
- **arXiv:** **DOI:** [10.1073/pnas.1911517117](https://doi.org/10.1073/pnas.1911517117)
- **Frameworks:** Consequentialist/Utilitarian
- **What it measures:** Cross-cultural moral preferences in sacrificial (trolley-problem) dilemmas; universals vs. cultural variations in utilitarian sacrifice acceptability
- **Dataset:** 70,000 participants across 42 countries, 10 languages
- **LLMs tested:** No AI models directly; dataset provides ground truth for value-aligned AI development
- **Key finding:** Produces a large-scale public dataset of cross-cultural moral preferences on sacrificial dilemmas, demonstrating both universal patterns and signif....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2020-Awad-Universals and variations in moral decisions made]]

### C5. Islamic Fatwa Dataset (Amr A. Munshi, 2025)
- **Citation:** Amr A. Munshi et al. (2025). Towards an Automated Islamic Fatwa System.
- **arXiv:** **DOI:** [10.47760/ijcsmc.2021.v10i04.017](https://doi.org/10.47760/ijcsmc.2021.v10i04.017)
- **What it measures:** Islamic jurisprudence (Sharia) question-answering and topic classification for fatwa automation
- **Dataset:** Largest dataset for Islamic Fatwa (size not specified in paper body, spanning multiple fatwa websites)
- **LLMs tested:** Baseline NLP systems for classification and QA
- **Key finding:** Creates and releases a dataset and benchmarks specifically for Islamic religious/moral jurisprudence automation, representing a non-Western ethical....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2021-Munshi-Towards an Automated Islamic Fatwa System]]

### C6. RVR-based Value Pluralism Assessment (Noam Benkler, 2025)
- **Citation:** Noam Benkler et al. (2025). Assessing LLMs for Moral Value Pluralism. *arXiv.org*.
- **arXiv:** [2312.10075](https://arxiv.org/abs/2312.10075) | **DOI:** [10.48550/arXiv.2312.10075](https://doi.org/10.48550/arXiv.2312.10075)
- **Frameworks:** World Values Survey
- **What it measures:** Implicit moral and cultural values in LLM outputs - alignment with World Values Survey demographics across cultures, measuring moral/cultural distance
- **Dataset:** Based on World Values Survey (standardized instrument)
- **LLMs tested:** Multiple LLMs (not specified in abstract)
- **Key finding:** Directly evaluates LLMs for moral value pluralism using the RVR model and World Values Survey framework.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Benkler-Assessing LLMs for Moral Value Pluralism]]

### C7. EMoTES-3K (Jasper Kyle Catapang, 2025)
- **Citation:** [[Catapang, Jasper Kyle]] & [[Visperas, Moses]] (2025). EMoTES-3K.
- **What it measures:** Commonsense morality in Tagalog (Filipino) and English - emotion-based moral judgments and explanations
- **Dataset:** 3,000 scenarios (implied by name EMoTES-3K)
- **LLMs tested:** RoBERTa (fine-tuned), FLAN-T5 (fine-tuned)
- **Key finding:** Creates the first moral reasoning dataset for Filipino/Tagalog and English, addressing Anglocentrism in moral AI benchmarks.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Catapang-EMoTES-3K]]

### C8. STORAL-ZH (Jing Qian, 2025)
- **Citation:** Jing Qian (2025). Understanding Chinese Moral Stories with Further.
- **arXiv:** **DOI:** [10.5121/ijnlc.2023.12201](https://doi.org/10.5121/ijnlc.2023.12201)
- **Frameworks:** Virtue Ethics
- **What it measures:** AI model ability to understand moral concepts embedded in Chinese narrative stories (moral understanding/generation)
- **Dataset:** 4,209 Chinese story-moral pairs (STORAL-ZH), plus Confucian moral culture dataset
- **LLMs tested:** BERT-base, RoBERTa-base, T5-base (Chinese variants)
- **Key finding:** Uses and evaluates models on STORAL-ZH, a Chinese moral stories dataset.
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2023-Qian-Understanding Chinese Moral Stories with Further]]

### C9. QASiNa (Muhammad Razif Rizqullah, 2025)
- **Citation:** Muhammad Razif Rizqullah et al. (2025). QASiNa. *2023 10th International Conference on Advanced Informatics: Concept, Theory and Application (ICAICTA)*.
- **arXiv:** [2310.08102](https://arxiv.org/abs/2310.08102) | **DOI:** [10.48550/arXiv.2310.08102](https://doi.org/10.48550/arXiv.2310.08102)
- **What it measures:** LLM question answering on Islamic religious texts (Sirah Nabawiyah) in Indonesian; evaluates tendency to over-interpret religious content
- **Dataset:** QA dataset from Sirah Nabawiyah literature (size not specified in abstract)
- **LLMs tested:** mBERT, XLM-R, IndoBERT, ChatGPT-3.5, GPT-4
- **Key finding:** Creates QASiNa dataset for evaluating LLMs on Islamic religious QA in Indonesian.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Rizqullah-QASiNa]]

### C10. FULCRA (Jing Yao, 2025)
- **Citation:** Jing Yao et al. (2025). Value FULCRA. *North American Chapter of the Association for Computational Linguistics*.
- **arXiv:** [2311.10766](https://arxiv.org/abs/2311.10766) | **DOI:** [10.48550/arXiv.2311.10766](https://doi.org/10.48550/arXiv.2311.10766)
- **Frameworks:** World Values Survey
- **What it measures:** LLM behavior alignment with Schwartz's Theory of Basic Human Values; maps LLM outputs to multidimensional value space
- **Dataset:** 5,000 (LLM output, value vector) pairs
- **LLMs tested:** Multiple LLMs (specific models evaluated using the FULCRA dataset)
- **Key finding:** Creates FULCRA, a dataset mapping LLM behaviors to Schwartz's Theory of Basic Values.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2023-Yao-Value FULCRA]]

### C11. NormBank (Caleb Ziems, 2025)
- **Citation:** Caleb Ziems et al. (2025). NormBank. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2305.17008](https://arxiv.org/abs/2305.17008) | **DOI:** [10.48550/arXiv.2305.17008](https://doi.org/10.48550/arXiv.2305.17008)
- **What it measures:** Situational social norms grounded in sociocultural frames (setting, roles, attributes, constraints) for flexible normative reasoning
- **Dataset:** 155,000 situational norms; 63,000 unique constraints
- **LLMs tested:** Neural models for norm generation and transfer experiments (specific models in paper)
- **Key finding:** Creates a large-scale dataset of contextualized social norms designed specifically to ground normative reasoning in AI systems, with structured soc....
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2023-Ziems-NormBank]]

### C12. Multilingual Ethical Reasoning Framework (Utkarsh Agarwal, 2025)
- **Citation:** [[Agarwal, Utkarsh]] et al. (2025). Ethical Reasoning Depends on Language. *LREC-COLING 2024*.
- **arXiv:** [2404.18460](https://arxiv.org/abs/2404.18460) | **DOI:** [10.48550/arXiv.2404.18460](https://doi.org/10.48550/arXiv.2404.18460)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** LLM ethical reasoning consistency across 6 languages (English, Spanish, Russian, Chinese, Hindi, Swahili) using three normative ethics branches (deontology, virtue, consequentialism)
- **Dataset:** Ethical dilemmas and policies across 3 normative branches x 3 abstraction levels x 6 languages
- **LLMs tested:** GPT-4, ChatGPT, Llama2-70B-Chat
- **Key finding:** Extends normative ethics evaluation framework to multilingual settings, testing whether LLMs can follow deontological, virtue, and consequentialist....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Agarwal-Ethical Reasoning Depends on Language]]

### C13. MFQ-2 Multilingual LLM Evaluation (Meltem Aksoy, 2025)
- **Citation:** Meltem Aksoy (2025). Whose Morality Do They Speak?. *arXiv.org*.
- **arXiv:** [2412.18863](https://arxiv.org/abs/2412.18863) | **DOI:** [10.48550/arXiv.2412.18863](https://doi.org/10.48550/arXiv.2412.18863)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Culturally-specific moral values across 8 languages using Moral Foundations Questionnaire 2 (MFQ-2): care, equality, proportionality, loyalty, authority, purity
- **Dataset:** 36 MFQ-2 items x 8 languages x 4 LLMs
- **LLMs tested:** GPT-3.5-Turbo, GPT-4o-mini, Llama 3.1, MistralNeMo
- **Key finding:** Applies the updated Moral Foundations Questionnaire (MFQ-2) to evaluate LLMs across 8 languages and cultures, measuring whether models reflect cult....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Aksoy-Whose Morality Do They Speak]]

### C14. DailyDilemmas (Yu Ying Chiu, 2025)
- **Citation:** Yu Ying Chiu et al. (2025). DailyDilemmas. *International Conference on Learning Representations*.
- **arXiv:** [2410.02683](https://arxiv.org/abs/2410.02683) | **DOI:** [10.48550/arXiv.2410.02683](https://doi.org/10.48550/arXiv.2410.02683)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** LLM value preferences when navigating everyday moral dilemmas, analyzed through Moral Foundations Theory, World Values Survey, Maslow's Hierarchy, Aristotle's Virtues, and Plutchik's Wheel of Emotions
- **Dataset:** 1,360 moral dilemmas
- **LLMs tested:** Multiple LLMs including GPT-4-turbo, Mixtral-8x7B, and others
- **Key finding:** Creates a dataset of everyday moral dilemmas and uses it to evaluate LLM value preferences across multiple ethical and psychological frameworks, di....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Chiu-DailyDilemmas]]

### C15. MultiTP (Zhijing Jin, 2025)
- **Citation:** Zhijing Jin et al. (2025). Language Model Alignment in Multilingual Trolley. *International Conference on Learning Representations*.
- **arXiv:** [2407.02273](https://arxiv.org/abs/2407.02273) | **DOI:** [10.48550/arXiv.2407.02273](https://doi.org/10.48550/arXiv.2407.02273)
- **What it measures:** Cross-lingual moral alignment of LLMs via trolley problems; preferences across 6 moral dimensions (species, gender, fitness, status, age, number of lives)
- **Dataset:** 97,520 trolley problem vignettes in 100+ languages
- **Code:** [GitHub](https://github.com/causalNLP/moralmachine)
- **LLMs tested:** 19 different LLMs
- **Key finding:** Major multilingual moral reasoning benchmark adapting the Moral Machine experiment to evaluate LLM moral alignment across 100+ languages and 6 mora....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Jin-Language Model Alignment in Multilingual Trolley]]

### C16. Multilingual Defining Issues Test (DIT) (Aditi Khandelwal, 2025)
- **Citation:** Aditi Khandelwal et al. (2025). Do Moral Judgment and Reasoning Capability of. *Conference of the European Chapter of the Association for Computational Linguistics*.
- **arXiv:** [2402.02135](https://arxiv.org/abs/2402.02135) | **DOI:** [10.48550/arXiv.2402.02135](https://doi.org/10.48550/arXiv.2402.02135)
- **What it measures:** Moral judgment and moral reasoning capabilities of LLMs across 6 languages using Kohlberg's stages of moral development
- **Dataset:** DIT scenarios in 6 languages
- **LLMs tested:** ChatGPT, GPT-4, Llama2Chat-70B
- **Key finding:** Adapts the Defining Issues Test (a classic moral psychology instrument) for multilingual LLM evaluation, finding language-dependent moral reasoning....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Khandelwal-Do Moral Judgment and Reasoning Capability of]]

### C17. Unnamed (MFT-based LLM Moral Foundations evaluation) (Peter Kirgis, 2025)
- **Citation:** Peter Kirgis (2025). Differences in Moral Foundations of LLMs. *arXiv*.
- **arXiv:** [2511.11790](https://arxiv.org/abs/2511.11790)
- **Frameworks:** Moral Foundations Theory, Virtue Ethics
- **What it measures:** Moral foundations of LLMs (care, fairness, loyalty, authority, sanctity, liberty) using Moral Foundations Theory
- **Dataset:** 116 moral vignettes
- **LLMs tested:** Wide range of frontier models from most major providers
- **Key finding:** Systematically evaluates LLM moral foundations using established moral psychology instruments (MFT vignettes), finding that model moral foundations....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Kirgis-Differences in Moral Foundations of LLMs]]

### C18. LocalValueBench (Gwenyth Isobel Meadows, 2025)
- **Citation:** Gwenyth Isobel Meadows et al. (2025). LocalValueBench. *arXiv.org*.
- **arXiv:** [2408.01460](https://arxiv.org/abs/2408.01460) | **DOI:** [10.48550/arXiv.2408.01460](https://doi.org/10.48550/arXiv.2408.01460)
- **What it measures:** LLM alignment with Australian local values and ethical standards, including Aboriginal cultural protocols
- **Dataset:** Not specified
- **LLMs tested:** 3 commercial LLMs by US vendors
- **Key finding:** Benchmark specifically designed to evaluate LLM alignment with culturally specific (Australian/Aboriginal) values, providing a framework for regula....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Meadows-LocalValueBench]]

### C19. eJCM (Extended Japanese Commonsense Morality) (Takumi Ohashi, 2025)
- **Citation:** Takumi Ohashi et al. (2025). Extended Japanese Commonsense Morality Dataset.
- **arXiv:** [2410.09564](https://arxiv.org/abs/2410.09564) | **DOI:** [10.1145/3627673.3679924](https://doi.org/10.1145/3627673.3679924)
- **What it measures:** Japanese commonsense morality classification, including culturally-specific moral reasoning
- **Dataset:** 31,184 sentences (expanded from 13,975 original JCM)
- **LLMs tested:** Trained models, ChatGPT (one-shot), GPT-4 Turbo, AugGPT baseline
- **Key finding:** Expands the only publicly available Japanese morality dataset, demonstrating cultural specificity in moral reasoning evaluation and showing LLMs tr....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Ohashi-Extended Japanese Commonsense Morality Dataset]]

### C20. CIVICS (Culturally-Informed and Values-Inclusive Corpus for Societal impacts) (Giada Pistilli, 2025)
- **Citation:** Giada Pistilli et al. (2025). CIVICS.
- **arXiv:** **DOI:** [10.1609/aies.v7i1.31710](https://doi.org/10.1609/aies.v7i1.31710)
- **What it measures:** Cultural and social value variation in LLMs across languages, nations, and sensitive topics (LGBTQI rights, social welfare, immigration, disability rights, surrogacy)
- **Dataset:** 699 prompts across 5 languages and 9 national contexts
- **Code:** [HuggingFace](https://huggingface.co/CIVICS-dataset)
- **LLMs tested:** Open-weight LLMs (specific models evaluated in experiments)
- **Key finding:** Multilingual, culturally-informed dataset explicitly designed to evaluate LLM value variation across cultures and languages on ethically sensitive ....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Pistilli-CIVICS]]

### C21. WorldValuesBench (Wenlong Zhao, 2025)
- **Citation:** Wenlong Zhao et al. (2025). WorldValuesBench.
- **arXiv:** [2404.16308](https://arxiv.org/abs/2404.16308)
- **What it measures:** Multi-cultural value awareness of language models across diverse global demographics
- **Dataset:** 20M+ examples derived from World Values Survey (94,728 participants)
- **LLMs tested:** Alpaca-7B, Vicuna-7B-v1.5, Mixtral-8x7B-Instruct-v0.1, GPT-3.5 Turbo
- **Key finding:** Creates a large-scale benchmark from World Values Survey data to test LLMs' awareness of multi-cultural values including ethical, social, and econo....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Wu-WorldValuesBench]]

### C22. Hajj-FQA (Hayfa A. Aleid, 2025)
- **Citation:** Hayfa A. Aleid & Aqil M. Azmi (2025). Hajj-FQA.
- **arXiv:** **DOI:** [10.1007/s44443-025-00128-w](https://doi.org/10.1007/s44443-025-00128-w)
- **Frameworks:** Virtue Ethics
- **What it measures:** Arabic religious question-answering for Hajj fatwas: machine reading comprehension, duplicate question detection, duplicate answer detection
- **Dataset:** 2,826 QA pairs from 800 expert-annotated fatwas
- **LLMs tested:** AraBERTv0.2, mBERT, XLM-RoBERTa, AraBART, AraGPT2
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Aleid-Hajj-FQA]]

### C23. CCD-Bench (Multiple authors, 2025)
- **Citation:** Multiple authors (2025). CCD-Bench: Probing Cultural Conflict in LLM Decision-Making. *arXiv*.
- **arXiv:** [2510.03553](https://arxiv.org/abs/2510.03553)
- **What it measures:** LLM decision-making under cross-cultural value conflict; how LLMs adjudicate when multiple cultural frameworks directly clash
- **Dataset:** 2,182 dilemmas
- **Code:** [GitHub](https://github.com/smartlab-nyu/CCD-Bench)
- **LLMs tested:** 17 leading LLMs
- **Key finding:** Explicitly designed to evaluate pluralistic moral reasoning under cross-cultural value conflict.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Rahman-CCD-Bench Probing Cultural Conflict in LLM Decision-Making]]

### C24. Moralization Corpus (S. Becker, 2025)
- **Citation:** Becker, S. et al. (2025). The Moralization Corpus. *arXiv*.
- **arXiv:** [2512.15248](https://arxiv.org/abs/2512.15248)
- **What it measures:** Detection and extraction of moralizations (arguments invoking moral values) in argumentative discourse across genres
- **Dataset:** Multi-genre German corpus (political debates, news articles, online discussions); exact size not stated in abstract
- **LLMs tested:** Several LLMs evaluated (specific models not named in available text)
- **Key finding:** Creates a novel annotated dataset for moral value detection in text and evaluates LLMs on moralization detection and component extraction tasks.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Becker-The Moralization Corpus]]

### C25. CulturalBench (Yu Ying Chiu, 2025)
- **Citation:** Yu Ying Chiu et al. (2025). CulturalBench.
- **arXiv:** [2410.02677](https://arxiv.org/abs/2410.02677) | **DOI:** [10.48550/arXiv.2410.02677](https://doi.org/10.48550/arXiv.2410.02677)
- **What it measures:** LLM cultural knowledge across 45 global regions and 17 topics including food preferences, greeting etiquette, and cultural norms
- **Dataset:** 1,696 questions
- **LLMs tested:** Multiple frontier LMs including GPT-4o, Mistral, DeepSeek
- **Key finding:** Benchmark evaluating LLM understanding of diverse cultural knowledge including values and norms across 45 global regions, directly relevant to cros....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Chiu-CulturalBench]]

### C26. CPD (Cultural Probe Dataset) (Emanuel Z. Fenech-Borg, 2025)
- **Citation:** Emanuel Z. Fenech-Borg et al. (2025). The Cultural Gene of Large Language Models. *arXiv.org*.
- **arXiv:** [2508.12411](https://arxiv.org/abs/2508.12411) | **DOI:** [10.48550/arXiv.2508.12411](https://doi.org/10.48550/arXiv.2508.12411)
- **What it measures:** Cultural value orientations in LLMs: Individualism-Collectivism (IDV) and Power Distance (PDI)
- **Dataset:** Not specified
- **LLMs tested:** GPT-4, ERNIE Bot
- **Key finding:** Introduces the Cultural Probe Dataset (CPD) methodology and Cultural Alignment Index to evaluate LLMs along Individualism-Collectivism and Power Di....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Fenech-Borg-The Cultural Gene of Large Language Models]]

### C27. NaVAB (National Value Alignment Benchmark) (Chengyi Ju, 2025)
- **Citation:** [[Ju, Chengyi]] et al. (2025). NaVAB.
- **What it measures:** Multi-national value alignment of LLMs with values of five nations (China, US, UK, France, Germany) - policy, legal, and moral values
- **Dataset:** Not stated explicitly
- **LLMs tested:** Various LLMs (not specified in abstract)
- **Key finding:** Creates NaVAB, a benchmark for evaluating LLM alignment with national values across five major nations, extracting values from policy and legal doc....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Ju-NaVAB]]

### C28. UniMoral (Shivani Kumar, 2025)
- **Citation:** Shivani Kumar & David Jurgens (2025). Are Rules Meant to be Broken?. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2502.14083](https://arxiv.org/abs/2502.14083) | **DOI:** [10.48550/arXiv.2502.14083](https://doi.org/10.48550/arXiv.2502.14083)
- **What it measures:** Multilingual moral reasoning across six languages (Arabic, Chinese, English, Hindi, Russian, Spanish) - action prediction, moral typology classification, factor attribution, consequence generation
- **Dataset:** Not stated in abstract (8,784 instances per related paper)
- **LLMs tested:** Three LLMs (not specified by name in abstract)
- **Key finding:** Creates UniMoral, a multilingual moral reasoning dataset spanning six languages with psychologically grounded dilemmas and benchmark tasks.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Kumar-Are Rules Meant to be Broken]]

### C29. CQ-Bench (Ziyi Liu, 2025)
- **Citation:** [[Liu, Ziyi]] et al. (2025). Can LLMs Grasp Implicit Cultural Values?. *arXiv*.
- **arXiv:** [2504.01127](https://arxiv.org/abs/2504.01127) | **DOI:** [10.48550/arXiv.2504.01127](https://doi.org/10.48550/arXiv.2504.01127)
- **Frameworks:** World Values Survey
- **What it measures:** LLMs' metacognitive cultural intelligence and ability to infer implicit cultural values from conversations
- **Dataset:** 500+ scenarios from WVS and GlobalOpinions
- **LLMs tested:** o1, Deepseek-R1, GPT-4o-mini, o3-mini, LLaMA-3.2-3B
- **Key finding:** Same paper as CQ-Bench above (duplicate vault entry).
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Liu-Can LLMs Grasp Implicit Cultural Values]]

### C30. Multi-Layered Auditing Platform for Responsible AI (includes Ethical Dilemma Corpus, DEF, MARK) (Haijiang Liu, 2025)
- **Citation:** [[Liu, Haijiang]], [[Gu, Jinguang]], [[Wu, Xun]], [[Hershcovich, Daniel]], [[Xiao, Qiaoling]] (2025). Cross-cultural value alignment frameworks. *arXiv*.
- **arXiv:** [2511.17256](https://arxiv.org/abs/2511.17256) | **DOI:** [10.48550/arXiv.2511.17256](https://doi.org/10.48550/arXiv.2511.17256)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** Cross-cultural value alignment in China-origin vs Western-origin LLMs; ethical reasoning patterns (deontological vs utilitarian), truth vs loyalty, temporal stability
- **Dataset:** Ethical Dilemma Corpus (not specified exact size)
- **LLMs tested:** 20+ models including Qwen, GPT-4o, Claude, LLaMA, DeepSeek
- **Key finding:** Develops a multi-layered evaluation platform specifically comparing cross-cultural value alignment between Chinese and Western LLMs, with ethical d....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Liu-Cross-cultural value alignment frameworks]]

### C31. Islam Q&A Morals Corpus (Volume 13) (Malaysia, 2025)
- **Citation:** Malaysia (2025). Islam Q&A Morals Corpus.
- **Frameworks:** Virtue Ethics
- **What it measures:** LLM ability to answer Islamic moral questions grounded in Malaysian Islamic scholarship; character and morals (akhlak) from a virtue ethics perspective
- **Dataset:** Volume 13 QA pairs (exact size not specified)
- **LLMs tested:** BERT-based models (fine-tuned)
- **Key finding:** Creates a dataset of Islamic moral QA pairs for testing and training models on non-Western, religiously grounded virtue ethics principles, relevant....
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### C32. EvalMORAAL (Hadi Mohammadi, 2025)
- **Citation:** [[Mohammadi, Hadi]], [[Giachanou, Anastasia]], [[Bagheri, Ayoub]] (2025). EvalMORAAL. *arXiv*.
- **arXiv:** [2510.05942](https://arxiv.org/abs/2510.05942) | **DOI:** [10.48550/arXiv.2510.05942](https://doi.org/10.48550/arXiv.2510.05942)
- **Frameworks:** World Values Survey
- **What it measures:** Moral alignment of LLMs with global human values from World Values Survey (55 countries, 19 topics) and PEW Global Attitudes Survey (39 countries, 8 topics)
- **Dataset:** WVS: 55 countries x 19 topics; PEW: 39 countries x 8 topics
- **LLMs tested:** 20 LLMs including Claude-3-Opus (r=0.890)
- **Key finding:** Comprehensive cross-cultural moral alignment evaluation framework using World Values Survey and PEW data.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Mohammadi-EvalMORAAL]]

### C33. Cultural Moral Judgment Evaluation (WVS/PEW-based) (H. Mohammadi, 2025)
- **Citation:** Mohammadi, H., & Bagheri, A (2025). Exploring Cultural Variations in Moral Judgments with Large Language Models. *arXiv*.
- **arXiv:** [2506.12433](https://arxiv.org/abs/2506.12433)
- **Frameworks:** World Values Survey
- **What it measures:** Whether LLMs mirror cultural variations in moral attitudes from World Values Survey and PEW Global Attitudes Survey
- **Dataset:** WVS + PEW survey data covering broad ethical topics
- **Code:** [GitHub](https://github.com/mohammadi-hadi/cultural-moral-judgments-llms)
- **LLMs tested:** GPT-2, OPT, BLOOMZ, Qwen, GPT-4o, GPT-4o-mini, Gemma-2-9b-it, Llama-3.3-70B-Instruct
- **Key finding:** Evaluates LLM moral alignment with cross-cultural survey data, revealing better alignment with WEIRD nations.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language]]

### C34. WorldView-Bench (Abdullah Mushtaq, 2025)
- **Citation:** Abdullah Mushtaq et al. (2025). WorldView-Bench.
- **arXiv:** [2505.09595](https://arxiv.org/abs/2505.09595)
- **What it measures:** Global Cultural Inclusivity (GCI) in LLMs — whether models accommodate diverse cultural worldviews or reinforce Western-centric norms
- **Dataset:** Not specified in paper profile; benchmark covers multiple cultural worldviews
- **LLMs tested:** Multiple LLMs (specific models not listed in profile but includes contextually-implemented and MAS-implemented Multip...
- **Key finding:** Introduces WorldView-Bench, a benchmark specifically designed to evaluate cultural value pluralism in LLMs.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Mushtaq-WorldView-Bench]]

### C35. LLM Ethical Logic Assessment Battery (W. Russell Neuman, 2025)
- **Citation:** [[[[[[W. Russell Neuman]], [[Chad Coleman]], [[Manan Shah]]]]]] (2025). Analyzing the Ethical Logic of Six Large Language Models.
- **arXiv:** [2501.08951](https://arxiv.org/abs/2501.08951) | **DOI:** [10.48550/arXiv.2501.08951](https://doi.org/10.48550/arXiv.2501.08951)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Moral Foundations Theory, Virtue Ethics
- **What it measures:** Ethical reasoning patterns of LLMs across consequentialist-deontological reasoning, Moral Foundations Theory, and Kohlberg's developmental stages
- **Dataset:** Battery of classic dilemmas + self-descriptive prompts
- **LLMs tested:** GPT-4o, LLaMA 3.1, Perplexity, Claude 3.5 Sonnet, Gemini, Mistral 7B
- **Key finding:** Conducts structured empirical evaluation of moral reasoning in 6 LLMs using established ethical frameworks (MFT, Kohlberg, deontology/consequential....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Neuman-Analyzing the Ethical Logic of Six Large Language Models]]

### C36. Five-Dimensional Ethical Audit Model (W. Russell Neuman, 2025)
- **Citation:** W. Russell Neuman et al. (2025). Auditing the Ethical Logic of Generative AI Models.
- **arXiv:** [2504.17544](https://arxiv.org/abs/2504.17544)
- **What it measures:** Quality of ethical reasoning in LLMs across 5 dimensions: Analytic Quality, Breadth of Ethical Considerations, Depth of Explanation, Consistency, and Decisiveness
- **Dataset:** Multiple batteries of novel ethical dilemmas
- **LLMs tested:** 7 major LLMs
- **Key finding:** Introduces a scalable ethical benchmarking methodology focusing on the quality of ethical reasoning rather than just correctness.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Neuman-Auditing the Ethical Logic of Generative AI Models]]

### C37. AITA Moral Dilemmas Evaluation (Pratik S. Sachdeva, 2025)
- **Citation:** [[Sachdeva, Pratik S.]] & [[van Nuenen, Tom]] (2025). Normative Evaluation of LLMs. *ACM FAccT 2025*.
- **arXiv:** **DOI:** [10.1145/3715275.3732044](https://doi.org/10.1145/3715275.3732044)
- **What it measures:** LLM moral judgment on everyday ethical dilemmas (blame assignment, moral reasoning patterns)
- **Dataset:** 10,826 AITA submissions with 476,183 comments
- **Code:** [GitHub](https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas)
- **LLMs tested:** GPT-3.5, GPT-4, Claude Haiku, PaLM 2 Bison, Llama 2 7B, Mistral 7B, Gemma 7B
- **Key finding:** Creates a large-scale dataset of real-world moral dilemmas and evaluates LLMs on moral judgment, measuring inter-model agreement, self-consistency,....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas]]

### C38. MFTCXplain (Jackson Trager, 2025)
- **Citation:** Jackson Trager et al. (2025). MFTCXplain. *Conference on Empirical Methods in Natural Language Processing*.
- **arXiv:** [2506.19073](https://arxiv.org/abs/2506.19073) | **DOI:** [10.48550/arXiv.2506.19073](https://doi.org/10.48550/arXiv.2506.19073)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral reasoning capabilities of LLMs through hate speech multi-hop explanations using Moral Foundations Theory
- **Dataset:** 3,000 tweets in Portuguese, Italian, Persian, English
- **LLMs tested:** Multiple commercial and open-source LLMs
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Trager-MFTCXplain]]

### C39. Ethical Reasoning Paradigm (evaluated on SafeWorld) (Jiahao Wang, 2025)
- **Citation:** [[Wang, Jiahao]] et al. (2025). Diverse Human Value Alignment for LLMs via Ethical Reasoning.
- **arXiv:** [2511.00379](https://arxiv.org/abs/2511.00379) | **DOI:** [10.48550/arXiv.2511.00379](https://doi.org/10.48550/arXiv.2511.00379)
- **What it measures:** LLM alignment with diverse regional human values through structured ethical reasoning
- **Dataset:** SafeWorld benchmark (size not specified in paper profile)
- **LLMs tested:** Multiple LLMs compared against CoT and state-of-the-art methods
- **Key finding:** Proposes a structured ethical reasoning framework for LLMs and evaluates it on the SafeWorld benchmark specifically designed for regional/cultural ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning]]

### C40. C-VARC / CVC (Chinese Value Rule Corpus) (Ping Wu, 2025)
- **Citation:** [[Wu, Ping]] et al. (2025). CVC. *arXiv.org*.
- **arXiv:** [2506.01495](https://arxiv.org/abs/2506.01495) | **DOI:** [10.48550/arXiv.2506.01495](https://doi.org/10.48550/arXiv.2506.01495)
- **What it measures:** LLM alignment with Chinese cultural values through value rules and moral dilemmas
- **Dataset:** 250,000+ value rules + 400,000 moral dilemma scenarios
- **LLMs tested:** 16 models benchmarked; 7 LLMs in value rule evaluation; 17 LLMs in moral dilemmas
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Wu-CVC]]

### C41. Multilingual Moral Reasoning Benchmark (MMRB) (Huichi Zhou, 2025)
- **Citation:** Huichi Zhou et al. (2025). Moral Reasoning Across Languages. *arXiv.org*.
- **arXiv:** [2504.19759](https://arxiv.org/abs/2504.19759) | **DOI:** [10.48550/arXiv.2504.19759](https://doi.org/10.48550/arXiv.2504.19759)
- **What it measures:** Moral reasoning abilities of LLMs across five typologically diverse languages including Vietnamese, at three complexity levels (sentence, paragraph, document)
- **Dataset:** Curated moral scenarios across 5 languages x 3 complexity levels
- **LLMs tested:** Llama-3-8B, plus multiple LLMs in zero-shot evaluation
- **Key finding:** MMRB directly evaluates cross-lingual moral reasoning with cultural adaptation, revealing that low-resource language training has outsized positive....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Zhou-Moral Reasoning Across Languages]]

### C42. EAVIT (Efficient and Accurate Value Identification from Text) (Wenhao Zhu, 2025)
- **Citation:** Wenhao Zhu et al. (2025). EAVIT. *International Joint Conference on Artificial Intelligence*.
- **arXiv:** [2505.12792](https://arxiv.org/abs/2505.12792) | **DOI:** [10.48550/arXiv.2505.12792](https://doi.org/10.48550/arXiv.2505.12792)
- **Frameworks:** World Values Survey
- **What it measures:** Human value identification from text data using Schwartz value theory
- **Dataset:** Standard value datasets (not specified)
- **LLMs tested:** GPT-4, BERT-based classifiers, local LLaVA/Llama models
- **Key finding:** Proposes framework and methodology for identifying human values (Schwartz theory) in text data using LLMs, with evaluation on standard value datasets.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Zhu-EAVIT]]

### C43. RVR-based LLM Value Assessment (Recognizing Value Resonance) (Benkler, 2024)
- **Citation:** Benkler (2024). Cross-Linguistic Moral Preferences in LLMs - Evidence from.
- **Frameworks:** World Values Survey
- **What it measures:** Implicit moral and cultural values in LLM-generated text, using World Values Survey (WVS) value dimensions; measures moral/cultural distance between LLMs and various demographics
- **Dataset:** 1,201,200 observations across ten professional domains
- **LLMs tested:** Multiple LLMs (details in paper)
- **Key finding:** Applies WVS-based value measurement to LLM outputs via RVR model, quantifying moral/cultural distance between AI systems and global demographics.
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### C44. MoralPrompt (with DeNEVIL algorithm) (Duan, 2024)
- **Citation:** Duan (2024). DeNEVIL MoralPrompt.
- **What it measures:** Intrinsic ethical values of LLMs based on moral philosophy value theories; exploits value vulnerabilities to reveal underlying value inclinations
- **Dataset:** 2,397 prompts covering 500+ value principles
- **LLMs tested:** Spectrum of LLMs (both black-box and open-source)
- **Key finding:** MoralPrompt is a dedicated ethics benchmark grounded in moral philosophy value theories.
- **Readiness:** ★★☆ MEDIUM
- **Vault status:** Not in vault

### C45. CoreValue (Y. Liu, 2022)
- **Citation:** Liu, Y. et al. (2022). CoreValue: Chinese Values Knowledge Base (Liu et al.). *Not specified*.
- **What it measures:** Chinese cultural values - a knowledge base encoding Chinese social and moral values
- **Key finding:** Creates a Chinese values knowledge base specifically for cultural/moral values.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2022-Liu-CoreValue Chinese Values Knowledge Base Liu et al.]]

### C46. SOCIAL-CHEM-101 (Forbes, 2020)
- **Citation:** Forbes (2020). Social Chemistry 101 SOCIAL-CHEM-101.
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Social norms and moral judgments (rules-of-thumb) across 12 dimensions including social judgments of good/bad, moral foundations, cultural pressure, and legality
- **Dataset:** 292,000 rules-of-thumb; 4.5 million annotations
- **LLMs tested:** Neural Norm Transformer (based on GPT-2); state-of-the-art neural models
- **Key finding:** Creates SOCIAL-CHEM-101, a large-scale corpus of social/moral norms with rich multi-dimensional annotations.
- **Readiness:** ★★☆ MEDIUM
- **Vault status:** Not in vault

### C47. CultureLLM (Li et al., 2024)
- **Citation:** Li, C., Chen, M., Wang, J., Sitaram, S., & Xie, X. (2024). CultureLLM: Incorporating Cultural Differences into Large Language Models. *NeurIPS 2024*.
- **arXiv:** [2402.10946](https://arxiv.org/abs/2402.10946)
- **Cultural scope:** 9 cultures (Arabic, Bengali, Chinese, English, German, Korean, Portuguese, Spanish, Turkish)
- **Dataset:** 50 WVS seed samples/culture with semantic data augmentation; 7 topic categories
- **Code:** [GitHub](https://github.com/Scarelette/CultureLLM)
- **LLMs tested:** GPT-3.5, Gemini Pro, GPT-4 (CultureLLM outperforms GPT-3.5 by 8.1%)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### C48. LLM-GLOBE (Karinshak et al., 2024)
- **Citation:** Karinshak, E., Hu, A., Kong, K., Rao, V., Wang, J., Wang, J., & Zeng, Y. (2024). LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output.
- **arXiv:** [2411.06032](https://arxiv.org/abs/2411.06032)
- **Cultural scope:** US vs. China; GLOBE framework (9 cultural dimensions)
- **Dataset:** 36,675 closed-ended + 900 open-generation prompts; English + Chinese
- **Code:** [GitHub](https://github.com/raovish6/LLM-GLOBE) — novel "LLMs-as-a-Jury" eval pipeline
- **LLMs tested:** Claude, Gemini, GPT-3.5, GPT-4 (US); GLM-4, Ernie 3.5/4.0, Qwen-14b (China)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### C49. MENAValues (Zahraei & Asgari, 2025)
- **Citation:** Zahraei, P.S. & Asgari, E. (2025). I Am Aligned, But With Whom? MENA Values Benchmark for Evaluating Cultural Alignment and Multilingual Bias in LLMs.
- **arXiv:** [2510.13154](https://arxiv.org/abs/2510.13154)
- **Cultural scope:** 16 MENA countries
- **Dataset:** 864 MCQ from WVS Wave 7 + 2022 Arab Opinion Index; governance, economics, cultural identity, wellbeing
- **Languages:** English, Arabic, Persian, Turkish
- **Code:** [GitHub](https://github.com/llm-lab-org/MENA-Values-Benchmark-Evaluating-Cultural-Alignment-and-Multilingual-Bias-in-Large-Language-Models)
- **LLMs tested:** Llama-3.1-8B, Mistral-7B, AYA-expanse-8b, Fanar-1-9B, ALLAM-Thinking, GPT-4o-mini, Gemini 2.5 Flash Lite
- **Key finding:** "Cross-Lingual Value Shifts" — identical questions yield different responses based on language
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### C50. IslamTrust (Lahmar et al., 2025)
- **Citation:** Lahmar, A., Arafat, M.E., Farou, Z., & Mahmud, M. (2025). IslamTrust: A Benchmark for LLMs Alignment with Islamic Values. *Muslims in ML Workshop @ NeurIPS 2025*.
- **OpenReview:** [PBcv90iKFB](https://openreview.net/forum?id=PBcv90iKFB)
- **Cultural scope:** Islamic values across 6 domains; bilingual
- **Dataset:** 406 MCQ; Arabic + English; MIT license
- **Code:** [HuggingFace](https://huggingface.co/datasets/Abderraouf000/IslamTrust-benchmark)
- **LLMs tested:** SILMA-9B (best), Fanar-1-9B, ALLaM-7B, Llama-3.1-8B
- **Key finding:** LLMs perform better in Arabic than English; systematic biases in interfaith dialogue
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### C51. CDEval (Wang et al., 2024)
- **Citation:** Wang, Y., Zhu, Y., Kong, C., Wei, S., Yi, X., Xie, X., & Sang, J. (2024). CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models. *Cross-Cultural NLP Workshop @ ACL 2024*.
- **arXiv:** [2311.16421](https://arxiv.org/abs/2311.16421)
- **Cultural scope:** Hofstede's 6 cultural dimensions (PDI, IDV, UAI, MAS, LTO, IVR) across 7 domains; compared against 98 countries
- **Dataset:** 2,953 questions; English, Chinese, German
- **Code:** [GitHub](https://github.com/astrodrew/CDEval)
- **LLMs tested:** 17 models (GPT-4, GPT-3.5-turbo, ChatGLM v1-3, Spark-v2, Llama2-Chat, Qwen-Chat, Baichuan-Chat, Alpaca-7B, Chinese-Alpaca2-13B, etc.)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

### C52. XCR-Bench (Kabir et al., 2026)
- **Citation:** Kabir, M., Ahmed, T., Rahman, M.M., Ji, S., Alhuzali, H., & Ananiadou, S. (2026). XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural Reasoning in LLMs.
- **arXiv:** [2601.14063](https://arxiv.org/abs/2601.14063)
- **Cultural scope:** Chinese, Arabic, Bengali (with West Bengal/India and Bangladesh sub-variants)
- **Dataset:** 4,900 parallel sentences, 1,098 Culture-Specific Items; 3 reasoning tasks; CC BY-NC-ND 4.0
- **Code:** [GitHub](https://github.com/mohsinulkabir14/xcr_bench)
- **LLMs tested:** GPT-4o, Qwen-2.5-Max, Gemini-2.0-Flash, Claude-3.7-Sonnet, DeepSeek-R1, LLaMA-3.3-70B, OLMo-2-32B
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

---

## D. Moral Psychology & Foundations Benchmarks

### D1. Interpretable Moral Machine Transformer (M. Goel, 2026)
- **Citation:** Goel, M., Das, A (2026). Building Interpretable Models for Moral Decision-Making. *NeurIPS 2025*.
- **arXiv:** [2602.03351](https://arxiv.org/abs/2602.03351)
- **What it measures:** How neural networks encode and process moral decision-making on trolley-style dilemmas; localization of moral biases within transformer architecture
- **Dataset:** 3 million Moral Machine scenarios (5.4M total responses)
- **Code:** [GitHub](https://github.com/Lossfunk/modeling-moral-machine)
- **LLMs tested:** Custom 104K-parameter transformer (not an LLM evaluation but a study of moral reasoning encoding)
- **Key finding:** Builds an interpretable transformer to study how neural networks encode moral reasoning on Moral Machine trolley problems, using the dataset as a b....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2026-Goel-Building Interpretable Models for Moral Decision-Making]]

### D2. TrolleyMod v1.0 (Vahid Behzadan, 2025)
- **Citation:** Vahid Behzadan et al. (2025). TrolleyMod v1.0. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)*.
- **arXiv:** [1811.05594](https://arxiv.org/abs/1811.05594) | **DOI:** [10.48550/arXiv.1811.05594](https://doi.org/10.48550/arXiv.1811.05594)
- **What it measures:** Ethical decision-making in autonomous vehicle trolley-problem scenarios
- **Dataset:** Not stated (platform for data collection)
- **LLMs tested:** Deep reinforcement learning agents (framework supports custom controllers)
- **Key finding:** Creates an open-source simulation platform explicitly designed for collecting ethical decision-making data and training value-aligned autonomous ve....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2018-Behzadan-TrolleyMod v1.0]]

### D3. SMID (Socio-Moral Image Database) (Deon Crone, 2025)
- **Citation:** Deon Crone (2025). The Socio-Moral Image Database (SMID).
- **arXiv:** **DOI:** [10.1371/journal.pone.0190954](https://doi.org/10.1371/journal.pone.0190954)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral wrongness, affective valence/arousal, and relevance to five Moral Foundations Theory values (Care, Fairness, Ingroup, Authority, Purity) via images
- **Dataset:** 2,941 images with normative ratings
- **LLMs tested:** Intended for computational (NLP, computer vision) investigations of moral processes; specific models not evaluated in...
- **Key finding:** Although originally created for human psychology/neuroscience, the paper explicitly states the database is intended for 'computational (e.g., natur....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2018-Crone-The Socio-Moral Image Database (SMID)]]

### D4. Brazilian Portuguese Moral Stance Corpus (Brazil University of São Paulo, 2025)
- **Citation:** Brazil University of São Paulo et al. (2025). Moral Stance Recognition and Polarity.
- **arXiv:** **DOI:** [10.26615/978-954-452-056-4_123](https://doi.org/10.26615/978-954-452-056-4_123)
- **What it measures:** Moral stance recognition and polarity classification in Brazilian Portuguese text
- **Dataset:** Not explicitly stated (Twitter + crowdsourced data)
- **LLMs tested:** Reference NLP classification baselines (not specified in detail)
- **Key finding:** Creates a labelled corpus of moral stances for Brazilian Portuguese with reference classification results.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2019-University of São Paulo-Moral Stance Recognition and Polarity]]

### D5. Moral Foundations Twitter Corpus (MFTC) (Joe Hoover, 2025)
- **Citation:** Joe Hoover et al. (2025). Moral Foundations Twitter Corpus.
- **arXiv:** **DOI:** [10.1177/1948550619876629](https://doi.org/10.1177/1948550619876629)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral sentiment in natural language based on Moral Foundations Theory (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Purity/Degradation, with virtue/vice variants)
- **Dataset:** 35,108 tweets across 7 discourse domains
- **LLMs tested:** Moral Foundations Dictionary (MFD), Distributed Dictionary Representations (DDR), BERT-based classifiers, various sup...
- **Key finding:** Creates the gold-standard annotated dataset for detecting moral sentiment in natural language based on Moral Foundations Theory.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2020-Hoover-Moral Foundations Twitter Corpus]]

### D6. Unnamed (Delphi moral philosophy probing) (Kathleen C. Fraser, 2025)
- **Citation:** [[Fraser, Kathleen C.]] et al. (2025). Does Moral Code Have a Moral Code?. *TRUSTNLP*.
- **arXiv:** [2205.12771](https://arxiv.org/abs/2205.12771) | **DOI:** [10.48550/arXiv.2205.12771](https://doi.org/10.48550/arXiv.2205.12771)
- **Frameworks:** Moral Foundations Theory, World Values Survey
- **What it measures:** Implicit moral principles learned by AI models (Delphi); consistency of moral reasoning with standardized morality questionnaires
- **Dataset:** Set of standardized questionnaire items (not specified)
- **LLMs tested:** Allen AI Delphi model
- **Key finding:** Evaluates an AI model's implicit moral philosophy using standardized ethics questionnaires, revealing that the model mirrors annotator demographic ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2022-Fraser-Does Moral Code Have a Moral Code]]

### D7. MoralNet (Aníbal M. Astobiza, 2025)
- **Citation:** Aníbal M. Astobiza (2025). MoralNet.
- **arXiv:** **DOI:** [10.31234/osf.io/dbyw7](https://doi.org/10.31234/osf.io/dbyw7)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Virtue Ethics
- **What it measures:** Ethical decision-making in AI systems - comprehensive moral competence assessment inspired by moral psychology and moral philosophy (virtue ethics, deontology, utilitarianism)
- **Dataset:** Proposed (proof of concept, not yet fully realized)
- **LLMs tested:** Proposed framework (no empirical evaluation yet)
- **Key finding:** Proposes MoralNet as a comprehensive benchmarking platform for evaluating morality in AI, akin to ImageNet for ethics.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Astobiza-MoralNet]]

### D8. Defining Issues Test (DIT) adapted for LLMs (Kumar Tanmay, 2025)
- **Citation:** Kumar Tanmay et al. (2025). Probing the Moral Development of Large Language. *arXiv.org*.
- **arXiv:** [2309.13356](https://arxiv.org/abs/2309.13356)
- **What it measures:** Moral development stage of LLMs according to Kohlberg's Cognitive Moral Development Model; post-conventional moral reasoning ability
- **Dataset:** Standard DIT moral dilemmas (multiple scenarios)
- **LLMs tested:** GPT-3, ChatGPT, Llama2-Chat, PaLM-2, GPT-4
- **Key finding:** Adapts the Defining Issues Test (a validated moral psychology instrument) for LLM evaluation, measuring moral development stages.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2023-Deng-Probing the Moral Development of Large Language]]

### D9. MoCa (Allen Nie, 2025)
- **Citation:** Allen Nie et al. (2025). MoCa. *Neural Information Processing Systems*.
- **arXiv:** [2310.19677](https://arxiv.org/abs/2310.19677) | **DOI:** [10.48550/arXiv.2310.19677](https://doi.org/10.48550/arXiv.2310.19677)
- **What it measures:** Human-LLM alignment on causal and moral judgment tasks, testing factors like norm violation, intent, and outcome avoidability
- **Dataset:** Stories from 24 cognitive science papers with annotated causal/moral factors
- **LLMs tested:** Multiple LLMs including GPT-4, GPT-3.5, and other open/closed-source models
- **Key finding:** Introduces MoCa, a dataset grounded in cognitive science research on causal and moral judgment.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2023-Nie-MoCa]]

### D10. MFT-based LLM Evaluation (Marwa Abdulhai, 2025)
- **Citation:** Marwa Abdulhai et al. (2025). Moral Foundations of Large Language Models.
- **arXiv:** **DOI:** [10.18653/v1/2024.emnlp-main.982](https://doi.org/10.18653/v1/2024.emnlp-main.982)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral foundations (care/harm, liberty/oppression, sanctity/degradation, etc.) embedded in LLMs, and their relationship to political affiliations and ideological biases
- **Dataset:** Based on MFT questionnaire items across multiple prompting contexts
- **LLMs tested:** Multiple popular LLMs (details in paper)
- **Key finding:** Adapts the established Moral Foundations Theory psychological instrument to evaluate LLMs' moral biases, demonstrating adversarial steerability and....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Abdulhai-Moral Foundations of Large Language Models]]

### D11. Moral Foundations Weibo Corpus (MFWC) (Renjie Cao, 2025)
- **Citation:** [[Cao, Renjie]] et al. (2025). The Moral Foundations Weibo Corpus.
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral sentiments in Chinese social media discourse based on 10 moral categories from Moral Foundations Theory
- **Dataset:** 25,671 Chinese Weibo comments across 6 topic areas
- **LLMs tested:** Several latest LLMs for baseline moral sentiment classification
- **Key finding:** Creates a large Chinese-language annotated corpus for moral sentiment analysis based on Moral Foundations Theory.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Cao-The Moral Foundations Weibo Corpus]]

### D12. Unnamed (Moral Persuasion Evaluation) (Allison Huang, 2025)
- **Citation:** Allison Huang et al. (2025). Moral Persuasion in Large Language Models. *arXiv*.
- **arXiv:** [2411.11731](https://arxiv.org/abs/2411.11731)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Moral Foundations Theory, Virtue Ethics
- **What it measures:** LLM susceptibility to moral persuasion across ethical frameworks (utilitarian, deontological, virtue ethics); Moral Foundations via MFQ
- **Dataset:** 116 moral vignettes (from Clifford et al. 2015 MFQ survey)
- **LLMs tested:** Mistral-7b-instruct, GPT-3.5, GPT-4, Llama models (multiple sizes from same providers)
- **Key finding:** Empirically evaluates LLMs on moral reasoning using the Moral Foundations Questionnaire and structured ethical persuasion scenarios across multiple....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Huang-Moral Persuasion in Large Language Models]]

### D13. MoralBench (Jianchao Ji, 2025)
- **Citation:** [[Ji, Jianchao]] et al. (2025). MoralBench. *SIGKDD Explorations*.
- **arXiv:** [2406.04428](https://arxiv.org/abs/2406.04428) | **DOI:** [10.48550/arXiv.2406.04428](https://doi.org/10.48550/arXiv.2406.04428)
- **What it measures:** Moral identity and moral reasoning capabilities of LLMs across ethical dilemmas and real-world scenarios
- **Dataset:** Not specified in abstract; publicly released datasets
- **LLMs tested:** Multiple LLMs (details in paper)
- **Key finding:** Introduces MoralBench, a dedicated benchmark for measuring moral reasoning capabilities of LLMs with dataset and metrics for moral identity assessment.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Ji-MoralBench]]

### D14. Moral Machine Experiment for LLMs (Kazuhiro Takemoto, 2025)
- **Citation:** Kazuhiro Takemoto (2025). The moral machine experiment on large language.
- **arXiv:** **DOI:** [10.1098/rsos.231393](https://doi.org/10.1098/rsos.231393)
- **Frameworks:** Consequentialist/Utilitarian
- **What it measures:** Ethical decision-making tendencies of LLMs on trolley-problem-style autonomous vehicle dilemmas across 9 moral dimensions (species, social value, gender, age, fitness, utilitarianism, interventionism, relationship, law)
- **Dataset:** 50,000 generated scenarios with LLM responses
- **LLMs tested:** GPT-3.5, GPT-4, PaLM 2, Llama 2
- **Key finding:** Replicates the Moral Machine Experiment on LLMs, systematically comparing LLM moral judgments to human preferences across multiple ethical dimensions.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Takemoto-The moral machine experiment on large language]]

### D15. Moral Foundations Questionnaire (MFQ) + ethical dilemmas battery (Alejandro Tlaie, 2025)
- **Citation:** Alejandro Tlaie (2025). Exploring and steering the moral compass of Large. *International Conference on Pattern Recognition*.
- **arXiv:** [2405.17345](https://arxiv.org/abs/2405.17345) | **DOI:** [10.48550/arXiv.2405.17345](https://doi.org/10.48550/arXiv.2405.17345)
- **Frameworks:** Consequentialist/Utilitarian, Moral Foundations Theory
- **What it measures:** Moral profiles of LLMs across ethical schools (utilitarian vs values-based) and liberal/conservative bias via Moral Foundations Theory
- **Dataset:** Not stated (uses existing MFQ instrument + selection of ethical dilemmas)
- **LLMs tested:** Multiple proprietary (GPT-4, etc.) and open-weights LLMs (Llama 2-7B, etc.)
- **Key finding:** Adapts the Moral Foundations Questionnaire and ethical dilemmas to empirically evaluate LLMs' moral profiles, comparing proprietary vs open-weight ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-Tlaie-Exploring and steering the moral compass of Large]]

### D16. M3oralBench (Bei Yan, 2025)
- **Citation:** Bei Yan et al. (2025). M$^3$oralBench.
- **arXiv:** [2412.20718](https://arxiv.org/abs/2412.20718) | **DOI:** [10.48550/arXiv.2412.20718](https://doi.org/10.48550/arXiv.2412.20718)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Multimodal moral understanding and reasoning of large vision-language models across six moral foundations (Moral Foundations Theory)
- **Dataset:** Not specified (expanded from Moral Foundations Vignettes)
- **LLMs tested:** 10 popular open-source and closed-source LVLMs
- **Key finding:** First multimodal moral benchmark for LVLMs, extending Moral Foundations Vignettes with generated images to evaluate moral judgment, classification,....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Yan-M$^3$oralBench]]

### D17. Unnamed (MFT-based LLM moral evaluation) (Luana Bulla, 2025)
- **Citation:** Luana Bulla et al. (2025). Large Language Models meet moral values.
- **arXiv:** **DOI:** [10.1016/j.chbr.2025.100609](https://doi.org/10.1016/j.chbr.2025.100609)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** LLM ability to detect and classify moral values based on Moral Foundations Theory (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Purity/Degradation)
- **Dataset:** 16,123 Reddit comments from the Moral Foundation Reddit Corpus (MFRC)
- **LLMs tested:** GPT-4, GPT-3.5, Llama-70B, Mixtral-8x7B, Mistral-7B, Llama-7B, plus NLI-based baseline
- **Key finding:** Comprehensive evaluation of six LLMs on moral value classification using MFT, introducing an evaluation framework for human-model comparison in mor....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Bulla-Large Language Models meet moral values]]

### D18. Unnamed (Value-Grounded Moral Reasoning Evaluation Framework) (Mohna Chakraborty, 2025)
- **Citation:** [[Chakraborty, Mohna]] et al. (2025). Structured Moral Reasoning. *arXiv*.
- **arXiv:** [2506.14948](https://arxiv.org/abs/2506.14948) | **DOI:** [10.48550/arXiv.2506.14948](https://doi.org/10.48550/arXiv.2506.14948)
- **Frameworks:** Care Ethics, Consequentialist/Utilitarian, Deontological, Virtue Ethics, World Values Survey
- **What it measures:** LLM moral reasoning across multiple ethical frameworks (deontology, utilitarianism, virtue ethics, care ethics, etc.) and value systems (MFT, Schwartz, Hofstede, Rokeach)
- **Dataset:** 4 moral reasoning datasets (names not specified in abstract)
- **LLMs tested:** 12 open-source LLMs
- **Key finding:** Introduces a comprehensive evaluation framework for moral reasoning in LLMs using structured prompts grounded in multiple value systems and ethical....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Chakraborty-Structured Moral Reasoning]]

### D19. MoVa (Z. Chen, 2025)
- **Citation:** Chen, Z. et al. (2025). MoVa: Towards Generalizable Classification of Human Morals and Values. *EMNLP*.
- **arXiv:** [2509.24216](https://arxiv.org/abs/2509.24216)
- **Frameworks:** Moral Foundations Theory, World Values Survey
- **What it measures:** Classification of human morals and values across four theoretically-grounded frameworks (including Moral Foundations Theory and Schwartz values)
- **Dataset:** 16 labeled datasets (combined size not stated)
- **LLMs tested:** LLMs using lightweight prompting strategy (specific models not named in abstract)
- **Key finding:** Comprehensive suite of 16 datasets and benchmarking results for moral and value classification across four theoretical frameworks, with a lightweig....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values]]

### D20. Unnamed (22 moral dilemmas) (Vanessa Cheung, 2025)
- **Citation:** [[Cheung, Vanessa]] et al. (2025). LLMs Amplified Cognitive Biases. *PNAS*.
- **arXiv:** **DOI:** [10.1073/pnas.2412015122](https://doi.org/10.1073/pnas.2412015122)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** Cognitive biases in LLM moral decision-making: omission bias, 'no-bias', and altruism in collective action problems and moral dilemmas (utilitarian vs. deontological)
- **Dataset:** 22 dilemmas (collective action problems + moral dilemmas)
- **LLMs tested:** Multiple LLMs with and without fine-tuning (specific models identified in studies)
- **Key finding:** PNAS study using structured moral dilemmas to empirically evaluate LLM moral decision-making biases compared to human responses, revealing systemat....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Cheung-LLMs Amplified Cognitive Biases Moral]]

### D21. PRIME (Priorities in Reasoning and Intrinsic Moral Evaluation) (Coleman, 2025)
- **Citation:** Coleman (2025). The Convergent Ethics of AI Analyzing Moral Foundation Priorities in.
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Moral Foundations Theory
- **What it measures:** Moral foundation priorities in LLMs: consequentialist-deontological reasoning, Moral Foundations Theory dimensions, Kohlberg's developmental stages
- **Dataset:** Ethical dilemma set (size not specified)
- **LLMs tested:** 6 leading LLMs
- **Key finding:** Introduces PRIME framework for multi-framework moral evaluation of LLMs, analyzing moral foundation priorities across MFT, deontological-consequent....
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### D22. BenchMoral (Félix B. A. Flores, 2025)
- **Citation:** Félix B. A. Flores (2025). BenchMoral.
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral sensitivity of LLMs in Spanish across five moral foundations (care, fairness, loyalty, authority, sanctity)
- **Dataset:** 30 MFQ items in two modalities, 5 repetitions per model
- **LLMs tested:** ChatGPT 4.0 Mini, Llama 3.0, DeepSeek R1
- **Key finding:** Adapts the Moral Foundations Questionnaire (MFQ-30) to Spanish for LLM evaluation.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Flores-BenchMoral]]

### D23. LLM Ethics Benchmark (Junfeng Jiao, 2025)
- **Citation:** [[Jiao, Junfeng]] et al. (2025). LLM Ethics Benchmark. *Scientific Reports*.
- **arXiv:** [2505.00853](https://arxiv.org/abs/2505.00853) | **DOI:** [10.48550/arXiv.2505.00853](https://doi.org/10.48550/arXiv.2505.00853)
- **Frameworks:** World Values Survey
- **What it measures:** Moral reasoning capabilities across foundational moral principles, reasoning robustness, and value consistency
- **Dataset:** Not specified in abstract
- **LLMs tested:** Multiple LLMs (not specified in abstract)
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Jiao-LLM Ethics Benchmark]]

### D24. MFD-LLM (Moral Foundations LLM Dataset) (Monika Jotautaite, 2025)
- **Citation:** Monika Jotautaite et al. (2025). From Stability to Inconsistency.
- **arXiv:** [2504.06324](https://arxiv.org/abs/2504.06324)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral preferences of LLMs grounded in Moral Foundations Theory (six core foundations) - revealed moral preferences and consistency across dilemma variations
- **Dataset:** Not stated explicitly
- **LLMs tested:** State-of-the-art LLMs (not specified by name in abstract)
- **Key finding:** Introduces MFD-LLM dataset grounded in Moral Foundations Theory to evaluate LLM moral preferences and consistency.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Jotautaite-From Stability to Inconsistency]]

### D25. Role-Play-at-Scale (Moral Foundations Questionnaire adaptation) (Bruce W. Lee, 2025)
- **Citation:** Bruce W. Lee et al. (2025). When Prompting Fails to Sway.
- **arXiv:** [2408.09049](https://arxiv.org/abs/2408.09049) | **DOI:** [10.48550/arXiv.2408.09049](https://doi.org/10.48550/arXiv.2408.09049)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Inertia in LLM moral and value judgments under persona-based prompting; measures resistance to value steering across MFT dimensions (harm, fairness, authority, loyalty, purity)
- **Dataset:** Not specified (multiple persona variations across moral dimensions)
- **LLMs tested:** Multiple LLMs (details in paper)
- **Key finding:** Conducts empirical evaluation of LLM moral value orientations using structured ethical scenarios (Moral Foundations) with persona-based prompting; ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Lee-When Prompting Fails to Sway]]

### D26. PRIME (Priorities in Reasoning and Intrinsic Moral Evaluation) Framework (Neuman, W. Russell, 2025)
- **Citation:** [[[[Neuman, W. Russell]]]] et al. (2025). PRIME Framework Convergent Ethics. *arXiv preprint*.
- **arXiv:** [2504.19255](https://arxiv.org/abs/2504.19255) | **DOI:** [10.48550/arXiv.2504.19255](https://doi.org/10.48550/arXiv.2504.19255)
- **Frameworks:** Consequentialist/Utilitarian, Deontological, Moral Foundations Theory
- **What it measures:** Moral foundation priorities in LLMs — convergence patterns across consequentialist-deontological reasoning, MFT foundations, and Kohlberg developmental stages
- **Dataset:** Battery of ethical dilemmas + self-descriptive prompts
- **LLMs tested:** ChatGPT, Claude, Gemini, Llama, Mistral, Perplexity (6 models)
- **Key finding:** Introduces the PRIME framework as a comprehensive methodology for multi-framework ethical auditing.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Neuman-PRIME Framework Convergent Ethics]]

### D27. Moral Machine prompt variation evaluation (S. & Demberg Oh, 2025)
- **Citation:** Oh, S. & Demberg, V (2025). Robustness of Large Language Models in Moral Judgements. *Unknown*.
- **arXiv:** **DOI:** [10.1098/rsos.241229](https://doi.org/10.1098/rsos.241229)
- **What it measures:** Robustness of LLM moral judgments under systematic prompt variations using Moral Machine vignettes
- **Dataset:** Moral Machine vignettes with systematic prompt variations
- **LLMs tested:** Large language models (specific models not detailed in thin profile)
- **Key finding:** Evaluates the robustness of LLM moral judgments using the Moral Machine framework with systematic prompt variations.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Oh-Robustness of Large Language Models in Moral Judgements]]

### D28. MCT + MFQ for LLM Evaluation (Ahmed Sameer, 2025)
- **Citation:** [[Sameer, Ahmed]], [[Fatima, Rabiya]] (2025). Insights into Moral Reasoning of AI. *Journal of Media Ethics*.
- **arXiv:** **DOI:** [10.1080/23736992.2025.2553146](https://doi.org/10.1080/23736992.2025.2553146)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Moral competence and moral foundations in LLMs vs humans
- **Dataset:** Not specified (MCT and MFQ standard instruments)
- **LLMs tested:** ChatGPT and other LLM-based chatbots
- **Key finding:** Adapts established moral psychology instruments (MCT, MFQ) to evaluate LLM moral reasoning, finding humans outperform LLMs on moral competence and ....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Sameer-Insights into Moral Reasoning of AI]]

### D29. MORALLENS (Keenan Samway, 2025)
- **Citation:** [[Samway, Keenan]] et al. (2025). Are LLMs Consequentialist or Deontological. *EMNLP 2025*.
- **arXiv:** [2505.21479](https://arxiv.org/abs/2505.21479) | **DOI:** [10.48550/arXiv.2505.21479](https://doi.org/10.48550/arXiv.2505.21479)
- **Frameworks:** Consequentialist/Utilitarian, Deontological
- **What it measures:** Whether LLM moral reasoning is consequentialist or deontological across trolley-problem scenarios
- **Dataset:** 640 moral vignettes
- **Code:** [GitHub](https://github.com/keenansamway/moral-lens)
- **LLMs tested:** Multiple LLMs including DeepSeek R1, QwQ, and others (MMLU-benchmarked models)
- **Key finding:** Introduces MORALLENS framework with structured taxonomy for classifying LLM moral reasoning along consequentialist/deontological dimensions, with 6....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Samway-Are Language Models Consequentialist or Deontological]]

### D30. Moral Reasoning Circuits Dataset (Sigurd Schacht, 2025)
- **Citation:** Sigurd Schacht & Carsten Lanquillon (2025). Mapping Moral Reasoning Circuits. *HCII 2025 - Artificial Intelligence in HCI*.
- **arXiv:** **DOI:** [10.1007/978-3-031-93415-5_6](https://doi.org/10.1007/978-3-031-93415-5_6)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Mechanistic localization of moral reasoning neurons across six Moral Foundations Theory dimensions (care, fairness, loyalty, authority, sanctity, liberty)
- **Dataset:** 240 validated moral and immoral statement pairs
- **Code:** [GitHub](https://github.com/coairesearch/mapping_moral_reasoning) | [GitHub](https://github.com/coairesearch/mapping_moral_reasoning.git)
- **LLMs tested:** Gemma 2
- **Key finding:** Creates a dataset of moral/immoral statement pairs grounded in Moral Foundations Theory and uses it to identify and validate moral reasoning circui....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Schacht-Mapping Moral Reasoning Circuits]]

### D31. LLM Moral Word Association Framework (Chaoyi Xiang, 2025)
- **Citation:** Chaoyi Xiang et al. (2025). Comparing Moral Values in Western. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2505.19674](https://arxiv.org/abs/2505.19674) | **DOI:** [10.48550/arXiv.2505.19674](https://doi.org/10.48550/arXiv.2505.19674)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Implicit moral values in LLMs compared to Western English-speaking communities using Moral Foundations Theory
- **Dataset:** 12,000 cues (SWOW dataset matched to LLM associations)
- **LLMs tested:** GPT-4, Llama, and others
- **Key finding:** Develops a novel evaluation methodology for probing implicit moral values in LLMs using word associations and MFT.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2025-Xiang-Comparing Moral Values in Western]]

### D32. Large-scale Moral Machine Experiment on LLMs (Muhammad Shahrul Zaim Bin Ahmad, 2025)
- **Citation:** Muhammad Shahrul Zaim Bin Ahmad & Kazuhiro Takemoto (2025). Large-scale moral machine experiment on large.
- **arXiv:** **DOI:** [10.1371/journal.pone.0322776](https://doi.org/10.1371/journal.pone.0322776)
- **What it measures:** Moral decision-making alignment between LLMs and human moral preferences in trolley-problem scenarios (age, gender, species, social status, law compliance)
- **Dataset:** Moral Machine Experiment scenarios tested on 52 LLMs
- **LLMs tested:** 52 LLMs including GPT-4, Claude 3, Gemini, Llama 3, Gemma variants
- **Key finding:** Replicates the Moral Machine Experiment on 52 LLMs using rigorous conjoint analysis to measure moral alignment, finding scaling laws in moral reaso....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large]]

### D33. TrolleyBench (Andrew Zhu, 2025)
- **Citation:** Andrew Zhu (2025). TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs. *NeurIPS 2025*.
- **What it measures:** Ethical consistency and moral reasoning in LLMs using trolley-problem-style moral dilemmas with clarifying and contradictory follow-ups
- **Dataset:** Trolley-problem moral dilemma scenarios (not specified)
- **LLMs tested:** Deepseek-R1, Mistral Small-32B, Gemini-2.5, GPT-4.1-mini, compared against human baselines
- **Key finding:** First open-source benchmark explicitly designed to evaluate ethical consistency in LLMs, using novel metrics (ECI, entropy-based Inconsistency Scor....
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in]]

### D34. Moral Foundations Theory Interpretability Analysis (Chenxiao Yu, 2025)
- **Citation:** [[Yu, Chenxiao]] et al. (2025). Tracing Moral Foundations in LLMs.
- **arXiv:** [2601.05437](https://arxiv.org/abs/2601.05437) | **DOI:** [N/A](https://doi.org/N/A)
- **Frameworks:** Moral Foundations Theory
- **What it measures:** Whether LLMs genuinely encode moral reasoning (Moral Foundations Theory) or merely replicate surface-level moral language
- **Dataset:** Not specified (Moral Foundations Theory-based evaluation)
- **LLMs tested:** 2 instruction-tuned models
- **Key finding:** Uses Moral Foundations Theory with mechanistic interpretability methods to evaluate how LLMs encode moral reasoning, demonstrating structured layer....
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2026-Yu-Tracing Moral Foundations in LLMs]]

### D35. OffTheRails (Franken, 2024)
- **Citation:** Franken, J.-P. et al. (2024). OffTheRails: Procedural Dilemma Generation for Moral Reasoning. *arXiv*.
- **arXiv:** [2404.10975](https://arxiv.org/abs/2404.10975)
- **What it measures:** Moral permissibility and intention judgments in trolley-problem-style dilemmas (means vs side-effect, evitable vs inevitable harm, action vs omission)
- **Dataset:** 50 scenarios, 400 unique test items
- **LLMs tested:** GPT-4, Claude-2
- **Key finding:** OffTheRails is a dedicated moral reasoning benchmark using procedurally generated ethical dilemmas grounded in moral philosophy (means/side-effect ....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning]]

### D36. DIT (Defining Issues Test) for LLMs (Tanmay, 2023)
- **Citation:** Tanmay (2023). Probing Moral Development through Defining Issues Test DIT.
- **What it measures:** Moral development stage of LLMs according to Kohlberg's Cognitive Moral Development Model
- **Dataset:** DIT moral dilemmas with ethical consideration sets (standardized instrument)
- **LLMs tested:** GPT-3, ChatGPT, Llama2-Chat, PaLM2, GPT-4
- **Key finding:** Adapts the Defining Issues Test, a validated psychometric instrument for moral development, to evaluate LLMs.
- **Readiness:** ★★☆ MEDIUM
- **Vault status:** Not in vault

### D37. Touche / ValueEval (SemEval 2023, CLEF 2024)
- **Citation:** Kiesel, J., et al. (2023). The Touche23-ValueEval Dataset for Identifying Human Values behind Arguments.
- **arXiv:** [2301.13771](https://arxiv.org/abs/2301.13771)
- **Frameworks:** 19 Schwartz values (value detection + value attainment)
- **Dataset:** ~3,000 human-annotated texts (400-800 words each); news articles + political manifestos
- **Languages:** 8 languages
- **Code:** [Zenodo](https://zenodo.org/records/6814564) | [Task page](https://touche.webis.de/clef24/touche24-web/human-value-detection.html)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault

---

## E. Psychometric & Values Survey Benchmarks

### E1. ValueNet (Liang Qiu, 2025)
- **Citation:** Liang Qiu et al. (2025). ValueNet.
- **arXiv:** [2112.06346](https://arxiv.org/abs/2112.06346) | **DOI:** [10.1609/aaai.v36i10.21368](https://doi.org/10.1609/aaai.v36i10.21368)
- **Frameworks:** World Values Survey
- **What it measures:** Human values across 10 Schwartz-based value dimensions in text scenarios, for value-driven dialogue systems
- **Dataset:** 21,374 text scenarios annotated with value attitudes across 10 dimensions
- **LLMs tested:** DistilBERT, BERT (value regression); GPT-2, DialoGPT (dialogue generation with value rewards)
- **Key finding:** Creates the first large-scale dataset for human value modeling based on Schwartz value theory, with 21k scenarios across 10 value dimensions.
- **Readiness:** ★★★ HIGH
- **Vault:** [[2022-Qiu-ValueNet]]

### E2. Value-Spectrum (Jingxuan Li, 2025)
- **Citation:** Jingxuan Li et al. (2025). Value-Spectrum. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2411.11479](https://arxiv.org/abs/2411.11479) | **DOI:** [10.48550/arXiv.2411.11479](https://doi.org/10.48550/arXiv.2411.11479)
- **Frameworks:** World Values Survey
- **What it measures:** Value preferences of Vision-Language Models (VLMs) based on Schwartz's value dimensions in social media contexts
- **Dataset:** 50,000+ short videos from TikTok, YouTube Shorts, Instagram Reels
- **LLMs tested:** GPT-4o, Gemini 1.5 Pro, Qwen-VL-Plus, Claude 3.5 Sonnet, CogVLM
- **Key finding:** Novel VQA benchmark measuring value preferences of VLMs using Schwartz value theory applied to social media video content, testing both intrinsic p....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Li-Value-Spectrum]]

### E3. ValueBench (Yuanyi Ren, 2025)
- **Citation:** Yuanyi Ren et al. (2025). ValueBench. *Annual Meeting of the Association for Computational Linguistics*.
- **arXiv:** [2406.04214](https://arxiv.org/abs/2406.04214) | **DOI:** [10.48550/arXiv.2406.04214](https://doi.org/10.48550/arXiv.2406.04214)
- **What it measures:** Value orientations and value understanding in LLMs using established psychometric instruments covering 453 multifaceted value dimensions
- **Dataset:** 44 inventories, 453 value dimensions
- **Code:** [GitHub](https://github.com/Value4AI/ValueBench)
- **LLMs tested:** 6 representative LLMs
- **Key finding:** Introduces the first comprehensive psychometric benchmark for evaluating value orientations in LLMs, directly measuring pluralistic human values ac....
- **Readiness:** ★★★ HIGH
- **Vault:** [[2024-Ren-ValueBench]]

### E4. AMAeval (Artificial Moral Assistant Evaluation) (Galatolo, 2025)
- **Citation:** Galatolo (2025). Beyond Ethical Alignment AMAs.
- **What it measures:** LLM capabilities as Artificial Moral Assistants: deductive and abductive moral reasoning beyond simple alignment
- **Dataset:** Not specified
- **LLMs tested:** Multiple open-source LLMs including Qwen 2.5-32B/72B, Gemma 3-12B/27B
- **Key finding:** Develops a benchmark for evaluating LLMs as Artificial Moral Assistants, testing deductive and abductive moral reasoning.
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault

### E5. TikTok Values Dataset (Y. Wang, 2025)
- **Citation:** Yuchen Wang et al. (2025). Multimodal Understanding of Human Values in Videos. *Neurocomputing*.
- **arXiv:** **DOI:** [10.1016/j.neucom.2025.130170](https://doi.org/10.1016/j.neucom.2025.130170)
- **Frameworks:** World Values Survey
- **What it measures:** Human values expressed in TikTok videos using Schwartz Theory of Personal Values
- **Dataset:** Hundreds of annotated TikTok videos
- **LLMs tested:** Multiple masked LMs and LLMs
- **Key finding:** Creates the first values-annotated dataset of TikTok videos grounded in Schwartz values theory.
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2025-Wang-Multimodal Understanding of Human Values in Videos]]

---

## F. Meta-Resources & Survey Papers

### F1. LLM Moral Competence Taxonomy (survey-based) (Aaron J. Snoswell, 2025)
- **Citation:** [[Snoswell, Aaron J.]] et al. (2025). Beyond Verdicts LLM Moral Competence.
- **arXiv:** **DOI:** [N/A](https://doi.org/N/A)
- **What it measures:** Surveys and categorizes 69 LLM ethical evaluation papers (2020-2025), proposing a taxonomy for moral competence assessment
- **Dataset:** Survey of 69 papers
- **LLMs tested:** N/A (meta-analysis)
- **Key finding:** While a survey, it develops a substantive taxonomy for categorizing LLM moral competence evaluations and proposes novel evaluation dimensions (mora....
- **Readiness:** ★★☆ MEDIUM
- **Vault:** [[2025-Snoswell-Beyond Verdicts LLM Moral Competence]]

### F2. Cultural Alignment Survey Replication / Anthropological Prompting (Badr AlKhamissi, 2024)
- **Citation:** Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, Mona Diab (2024). Investigating Cultural Alignment of LLMs. *ACL 2024*.
- **What it measures:** Cultural alignment of LLMs with Egyptian and US cultural values, measured through sociological survey replication
- **Dataset:** Sociological survey items replicated across regions of Egypt and US
- **LLMs tested:** Multiple LLMs with different pretraining data mixtures
- **Key finding:** Quantifies cultural alignment by simulating sociological surveys, comparing LLM responses to real survey participants across Egyptian and US cultures.
- **Readiness:** ★☆☆ LOW
- **Vault:** [[2024-AlKhamissi-Investigating Cultural Alignment of LLMs]]

### F3. SafetyPrompts.com (Vidgen et al., 2024)
- **URL:** [safetyprompts.com](https://safetyprompts.com/)
- **Scope:** Living catalogue of 144+ LLM safety datasets (23 specifically in "Value Alignment" category)
- **Readiness:** ★★★ HIGH (meta-resource)
- **Vault status:** Not in vault

### F4. Awesome-LLM-Psychometrics
- **URL:** [GitHub](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- **Scope:** Curated list of LLM psychometric and psychology papers
- **Readiness:** ★★★ HIGH (meta-resource, 597 stars)
- **Vault status:** Not in vault

### F5. EleutherAI lm-evaluation-harness
- **URL:** [GitHub](https://github.com/EleutherAI/lm-evaluation-harness)
- **Scope:** Unified evaluation framework including `hendrycks_ethics` task for reproducible ethics benchmarking
- **Readiness:** ★★★ HIGH (standard evaluation tool)
- **Vault status:** Not in vault

---

## Implementation Priority Guide

### Tier 1: Start Here (HIGH readiness + broad framework coverage)
| Priority | Benchmark | Why |
|----------|-----------|-----|
| 1 | **MoReBench** | 5 normative frameworks, 1,000 scenarios, 23K criteria, GitHub+HF, rubric-based |
| 2 | **ETHICS (Hendrycks)** | Anchor paper, 130K+ examples, 5 sub-tasks, in lm-eval-harness |
| 3 | **LLM Ethics Benchmark (Jiao)** | 3D assessment, MFQ+WVS+Dilemmas as JSON, CLI tool, CC0 license |
| 4 | **MoralChoice (Scherrer)** | 28 models already evaluated, statistical methodology, NeurIPS spotlight |
| 5 | **CulturalBench** | 45 countries, 29 models, 1,696 questions, CC BY 4.0, ACL 2025 |

### Tier 2: Expand Coverage (HIGH readiness + specific focus)
| Priority | Benchmark | Focus |
|----------|-----------|-------|
| 6 | **ValueBench** | 453 psychometric value dimensions |
| 7 | **CQ-Bench** | Implicit cultural values via conversation |
| 8 | **MENAValues** | MENA region, 4 languages, cross-lingual shifts |
| 9 | **IslamTrust** | Islamic values, bilingual, MIT license |
| 10 | **MACHIAVELLI** | Interactive consequentialist ethics |
| 11 | **CIVICS** | 9 national contexts, HuggingFace, CC BY 4.0 |
| 12 | **Delphi/Norm Bank** | 1.7M commonsense moral judgments |

### Tier 3: Specialized Deep-Dives (MEDIUM/HIGH readiness + unique angles)
| Priority | Benchmark | Focus |
|----------|-----------|-------|
| 13 | **MFTCXplain** | Multilingual moral foundations in hate speech |
| 14 | **Scaling Laws (Takemoto)** | Model size to moral alignment relationship |
| 15 | **Touche/ValueEval** | Schwartz values in text, 8 languages |
| 16 | **CDEval** | Hofstede cultural dimensions |
| 17 | **CultureLLM** | 9-culture fine-tuning framework |
| 18 | **MORABLES** | Abstract moral reasoning from fables |
| 19 | **Greatest Good** | Utilitarian-specific, 15 models |

---

## Gap Analysis

### Well-Covered Areas
- **Consequentialism/Utilitarianism:** Greatest Good, MACHIAVELLI, Moral Machine experiments
- **Deontology:** ETHICS sub-task, MoralExceptQA, MoReBench-Theory
- **Moral Foundations Theory:** MoralBench, MFTCXplain, LLM Ethics Benchmark
- **Western cultural values:** CulturalBench, CIVICS, LLM-GLOBE
- **Islamic values:** IslamTrust, MENAValues
- **WVS-based cross-cultural:** WorldValuesBench, CultureLLM, CQ-Bench, CDEval

### Critical Gaps (No Dedicated Benchmarks Found)
| Gap | Status | Opportunity |
|-----|--------|-------------|
| **Confucian ethics** | Theoretical papers only (governance frameworks) | Need dataset operationalizing ren, li, yi |
| **Ubuntu/African ethics** | Normative philosophy papers only | Need dataset operationalizing ubuntu, communalism, relational identity |
| **Hindu ethics** | No papers found | Need dataset covering dharma, karma, ahimsa |
| **Buddhist ethics** | No papers found | Need dataset covering precepts, compassion, interdependence |
| **Care ethics (standalone)** | Partial via MFT's Care/Harm | Need dedicated feminist/care ethics evaluation |
| **Virtue ethics (deep)** | Partial via ETHICS sub-task | Need phronesis, eudaimonia, character assessment |
| **Cross-framework conflict resolution** | Only Conscience Conflict (6 scenarios) | Need larger dataset of genuine ethical framework conflicts |
| **Non-English-first benchmarks** | Most are English-centric | MENAValues and IslamTrust are notable exceptions |

---

## Vault Status

- **Vault size:** 846 papers (post-deduplication)
- **Entries in this report from vault:** 130
- **Entries not in vault** (external/not-yet-imported): 22 (includes 13 hand-curated entries)
- **Source data:** `logs/20260208-benchmark_survey_candidates.json` (528 candidates from 20-agent survey)

---

## Methodology Note

This report was generated by `PYTHON/generate_values_alignment_report.py` which:

1. **Loads** 528 benchmark candidates from the 20-agent deep-read survey (2026-02-08)
2. **Scope-filters** to ethical values alignment using keyword matching + category-based filtering (categories 1, 2, 3, 8, 9 from the survey taxonomy)
3. **Preserves** all 39 original anchor entries (hand-curated in v1)
4. **Enriches** entries with YAML metadata from paper files (arXiv, DOI, venue, code URLs)
5. **Assigns** entries to sections A-F based on framework detection and content signals
6. **Rates** implementation readiness (HIGH/MEDIUM/LOW) based on data availability and code presence
7. **Deduplicates** by normalized benchmark name

### Scope Definition

**In scope:** Benchmarks focused on moral reasoning, ethical judgment, value alignment, value pluralism, cross-cultural values, normative ethics, and moral psychology.

**Out of scope:** Pure toxicity detection, safety/jailbreak evaluation, fairness/bias metrics, domain-specific ethics (medical/legal), and helpfulness/RLHF evaluation — unless they explicitly engage with ethical values or moral frameworks.

### Readiness Ratings

- **★★★ HIGH:** Public data + confirmed code/eval repository or tagged as benchmark/dataset in vault
- **★★☆ MEDIUM:** Public data but no confirmed code/eval URLs; or dataset described but release unconfirmed
- **★☆☆ LOW:** Availability not stated and no code/data URLs found

---

*Generated: 2026-02-10 | Script: `PYTHON/generate_values_alignment_report.py` | Source: 846-paper vault + 528-candidate survey*