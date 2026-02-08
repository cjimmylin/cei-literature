# Agent 5: PapersWithCode + HuggingFace Dataset Discovery Report

**Date:** 2026-02-07
**Agent:** Agent 5 — PapersWithCode & HuggingFace Dataset Aggregator Search
**Objective:** Find NEW papers/datasets with implementable benchmarks for ethical values alignment in LLMs
**Search Strategy:** Systematic search across PapersWithCode tasks/benchmarks and HuggingFace datasets hub
**Searches Conducted:** 19 web searches + 12 targeted page fetches

---

## Summary of Results

**Total NEW papers/datasets found: 17**
All items below are verified as NOT appearing in the 67+ already-known list.

---

## NEW Finding #1: Scruples

**Full Citation:**
Lourie, N., Le Bras, R., & Choi, Y. (2021). Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes. *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2021)*.

**arXiv/DOI:** arXiv:2008.09094 | https://arxiv.org/abs/2008.09094

**Frameworks:**
- Descriptive ethics (empirical moral judgments rather than prescriptive theories)
- Community-sourced normative judgments

**Dataset Details:**
- **Size:** 32,000 real-life anecdotes with 625,000 ethical judgments
- **Components:** Two sub-datasets: (1) Anecdotes — 32k real-life ethical situations with community judgments; (2) Dilemmas — paired moral situations for comparative judgment
- **Format:** Text scenarios with distributional moral labels
- **Languages:** English
- **Source:** Reddit r/AmItheAsshole

**Code/Data URLs:**
- GitHub: https://github.com/allenai/scruples
- PapersWithCode: https://paperswithcode.com/dataset/scruples

**LLMs Tested:** Pre-LLM era neural language models; used as foundation for Delphi system

**Implementation Readiness:** HIGH — Publicly available, well-documented, large-scale dataset with clear evaluation metrics. Directly downloadable.

**Unique Contribution:** First large-scale corpus capturing distributional moral judgments from real communities. Unlike synthetic dilemmas, these are genuine ethical situations people encountered. The distributional nature of judgments (not binary right/wrong) captures moral disagreement.

---

## NEW Finding #2: Social Chemistry 101 (SOCIAL-CHEM-101)

**Full Citation:**
Forbes, M., Hwang, J. D., Shwartz, V., Sap, M., & Choi, Y. (2020). Social Chemistry 101: Learning to Reason about Social and Moral Norms. *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020)*, pages 653–670.

**arXiv/DOI:** arXiv:2011.00620 | DOI: 10.18653/v1/2020.emnlp-main.48

**Frameworks:**
- Rules-of-Thumb (RoTs) as conceptual units of social/moral knowledge
- 12-dimensional judgment annotation (social judgment, moral foundations, cultural pressure, legality, etc.)

**Dataset Details:**
- **Size:** 292,000 rules-of-thumb; over 4.5 million categorical label annotations
- **Format:** Structured RoTs with 12 annotation dimensions per rule
- **Languages:** English
- **License:** CC BY-SA 4.0

**Code/Data URLs:**
- GitHub: https://github.com/mbforbes/social-chemistry-101
- Project page: https://maxwellforbes.com/social-chemistry/

**LLMs Tested:** GPT-2 based models at publication; now widely used as training data for moral reasoning systems (e.g., Delphi)

**Implementation Readiness:** HIGH — Fully public, CC BY-SA 4.0 licensed, with code and data on GitHub. Massive scale enables fine-tuning and evaluation.

**Unique Contribution:** Largest corpus of everyday social/moral norms expressed as natural language rules-of-thumb. The 12-dimensional annotation schema captures moral foundations, social acceptability, cultural pressure, and legal status simultaneously, enabling multi-dimensional moral evaluation.

---

## NEW Finding #3: Moral Stories

**Full Citation:**
Emelin, D., Le Bras, R., Hwang, J. D., Forbes, M., & Choi, Y. (2021). Moral Stories: Situated Reasoning about Norms, Intents, Actions, and their Consequences. *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021)*, pages 698–718.

**arXiv/DOI:** DOI: 10.18653/v1/2021.emnlp-main.54

**Frameworks:**
- Grounded, goal-oriented social reasoning
- Norm-based action evaluation (normative vs. divergent)
- Narrative structure with seven functional components

**Dataset Details:**
- **Size:** 12,000 structured, branching narratives (7 sentences each)
- **Format:** Each story contains: Norm, Situation, Intention, Normative Action, Normative Consequence, Divergent Action, Divergent Consequence
- **Languages:** English
- **License:** CC BY 4.0

**Code/Data URLs:**
- GitHub: https://github.com/demelin/moral_stories
- HuggingFace: https://huggingface.co/datasets/demelin/moral_stories

**LLMs Tested:** GPT-2, GPT-3 at publication; widely adopted in subsequent moral reasoning research

**Implementation Readiness:** HIGH — Available on both GitHub and HuggingFace. Highly structured format enables diverse tasks (action classification, norm generation, consequence prediction).

**Unique Contribution:** Uniquely structured narratives that pair normative and norm-divergent actions within the same scenario, enabling evaluation of whether models can distinguish morally appropriate from inappropriate actions in context.

---

## NEW Finding #4: Moral Integrity Corpus (MIC)

**Full Citation:**
Ziems, C., Yu, J. A., Wang, Y.-C., Halevy, A. Y., & Yang, D. (2022). The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems. *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022)*, pages 3755–3773.

**arXiv/DOI:** arXiv:2204.03021 | DOI: 10.18653/v1/2022.acl-long.261

**Frameworks:**
- Rules of Thumb (RoTs) for moral reasoning in dialogue
- 9 moral and social attribute dimensions
- Moral integrity assessment for conversational AI

**Dataset Details:**
- **Size:** 38,000 prompt-reply pairs; 99,000 distinct Rules of Thumb; 114,000 annotations
- **Format:** Chatbot prompt-reply pairs annotated with moral RoTs and 9-dimensional moral/social attribute labels
- **Languages:** English

**Code/Data URLs:**
- GitHub: https://github.com/GT-SALT/mic

**LLMs Tested:** DialoGPT, BlenderBot; framework applicable to any dialogue LLM

**Implementation Readiness:** HIGH — Publicly available code and data. Designed specifically for evaluating dialogue systems' moral integrity, directly applicable to modern chatbot LLMs.

**Unique Contribution:** First benchmark specifically targeting moral integrity in dialogue systems. Captures the nuance that moral judgments in conversation are context-dependent and that multiple competing moral perspectives may apply simultaneously.

---

## NEW Finding #5: DeNEVIL / MoralPrompt

**Full Citation:**
Duan, S., Yi, X., Zhang, P., Lu, T., Xie, X., & Gu, N. (2024). Denevil: Towards Deciphering and Navigating the Ethical Values of Large Language Models via Instruction Learning. *Proceedings of the International Conference on Learning Representations (ICLR 2024)*.

**arXiv/DOI:** arXiv:2310.11053

**Frameworks:**
- Moral Foundation Theory (5 foundations: care, fairness, loyalty, authority, purity)
- Dynamic value vulnerability exploitation
- VILMO in-context alignment method

**Dataset Details:**
- **Size:** 2,397 prompts covering 500+ value principles
- **Format:** Adversarial ethical prompts designed to elicit value violations
- **Languages:** English

**Code/Data URLs:**
- Not publicly specified in abstract; published at ICLR 2024

**LLMs Tested:** 27 LLMs across diverse architectures and scales (both black-box and open-source)

**Implementation Readiness:** MEDIUM-HIGH — Published at top venue (ICLR 2024). Large-scale evaluation across 27 models. Dataset designed for probing ethical vulnerabilities.

**Unique Contribution:** Novel adversarial prompt generation algorithm (DeNEVIL) that dynamically discovers LLM value vulnerabilities. Unlike static benchmarks, it generates prompts tailored to exploit specific models' ethical weaknesses. Also introduces VILMO alignment method.

---

## NEW Finding #6: Value Kaleidoscope / ValuePrism

**Full Citation:**
Sorensen, T., Jiang, L., Hwang, J., Levine, S., Pyatkin, V., West, P., Dziri, N., Lu, X., Rao, K., Bhagavatula, C., Sap, M., Tasioulas, J., & Choi, Y. (2024). Value Kaleidoscope: Engaging AI with Pluralistic Human Values, Rights, and Duties. *Proceedings of the AAAI Conference on Artificial Intelligence*, 38(18), 19937–19947.

**arXiv/DOI:** arXiv:2309.00779 | DOI: 10.1609/aaai.v38i18.29970

**Frameworks:**
- Pluralistic value theory (values, rights, and duties)
- Multi-perspective ethical reasoning
- Value relevance and valence assessment

**Dataset Details:**
- **Size:** 218,000 human-written values, rights, and duties linked to 31,000 real-world situations
- **Format:** Structured triples of (situation, value/right/duty, relevance)
- **Languages:** English
- **Quality:** Human annotators rated 91% as high-quality

**Code/Data URLs:**
- License: CC BY 4.0

**LLMs Tested:** GPT-4 (generation); Kaleido (purpose-built model, preferred by humans over GPT-4)

**Implementation Readiness:** HIGH — Large-scale dataset with validated quality. Kaleido model available. Transfers to other philosophical frameworks.

**Unique Contribution:** First large-scale dataset capturing pluralistic values, rights, and duties simultaneously. Unlike binary moral judgment datasets, captures value tensions and competing ethical considerations. Kaleido model demonstrates practical value reasoning.

---

## NEW Finding #7: TrustLLM

**Full Citation:**
Huang, Y., Sun, L., Wang, H., Wu, S., Zhang, Q., et al. (2024). TrustLLM: Trustworthiness in Large Language Models. *Proceedings of the International Conference on Machine Learning (ICML 2024)*.

**arXiv/DOI:** arXiv:2401.05561

**Frameworks:**
- 8-dimensional trustworthiness taxonomy: truthfulness, safety, fairness, robustness, privacy, machine ethics, transparency, accountability
- Benchmarks established for 6 of 8 dimensions
- Integration of 30+ existing datasets

**Dataset Details:**
- **Size:** 30+ datasets, 18+ subcategories
- **Format:** Multi-task benchmark across diverse evaluation formats
- **Languages:** Primarily English
- **Scope:** Most comprehensive integrated trustworthiness benchmark

**Code/Data URLs:**
- GitHub: https://github.com/HowieHwong/TrustLLM
- Website: https://trustllmbenchmark.github.io/TrustLLM-Website/

**LLMs Tested:** 16 mainstream LLMs (proprietary and open-source)

**Implementation Readiness:** HIGH — Open-source toolkit, leaderboard, and evaluation infrastructure. Published at ICML 2024. Active community.

**Unique Contribution:** Most comprehensive integrated LLM trustworthiness evaluation framework, combining 30+ datasets into unified assessment. Machine ethics dimension directly evaluates moral reasoning. Includes both proprietary and open-source model comparisons.

---

## NEW Finding #8: DecodingTrust

**Full Citation:**
Wang, B., Chen, W., Pei, H., Xie, C., Kang, M., Zhang, C., Xu, C., Xiong, Z., Dutta, R., Schaeffer, R., Truong, S. T., Arora, S., Mazeika, M., Hendrycks, D., Lin, Z., Cheng, Y., Koyejo, S., Song, D., & Li, B. (2023). DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models. *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

**arXiv/DOI:** arXiv:2306.11698
**Award:** NeurIPS 2023 Outstanding Paper Award (Datasets and Benchmarks Track)

**Frameworks:**
- 8 trust perspectives: toxicity, stereotype bias, adversarial robustness, OOD robustness, adversarial demonstrations, privacy, machine ethics, fairness
- Multi-perspective adversarial evaluation

**Dataset Details:**
- **Size:** Multi-dimensional benchmark across 8 trust dimensions
- **Format:** Diverse evaluation formats per dimension
- **Languages:** English

**Code/Data URLs:**
- GitHub: https://github.com/AI-secure/DecodingTrust
- HuggingFace: https://huggingface.co/datasets/AI-Secure/DecodingTrust
- Website: https://decodingtrust.github.io/

**LLMs Tested:** GPT-4, GPT-3.5 (primary); extensible to other models

**Implementation Readiness:** HIGH — Award-winning benchmark, fully open-source, available on HuggingFace. Comprehensive evaluation toolkit.

**Unique Contribution:** First comprehensive trustworthiness assessment specifically designed for GPT-class models. Reveals that GPT-4, while generally more trustworthy, is more vulnerable to jailbreaking. Machine ethics dimension provides direct ethical evaluation.

---

## NEW Finding #9: BeaverTails

**Full Citation:**
Ji, J., Liu, M., Dai, J., Pan, X., Zhang, C., Bian, C., Sun, R., Wang, Y., & Yang, Y. (2023). BeaverTails: Towards Improved Safety Alignment of LLM via a Human-Preference Dataset. *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

**arXiv/DOI:** arXiv:2307.04657

**Frameworks:**
- Separated helpfulness vs. harmlessness annotations
- 14 harm categories
- Safety meta-labeling with severity levels

**Dataset Details:**
- **Size:** 333,963 QA pairs with safety meta-labels; 361,903 expert comparison pairs; 700 evaluation prompts
- **Format:** Question-answer pairs with binary safety labels + preference rankings
- **Languages:** English
- **Components:** (1) BeaverTails classification dataset (300k+), (2) PKU-SafeRLHF preference dataset (300k+), (3) BeaverTails-Evaluation (700 prompts)

**Code/Data URLs:**
- GitHub: https://github.com/PKU-Alignment/beavertails
- HuggingFace: https://huggingface.co/datasets/PKU-Alignment/BeaverTails
- HuggingFace (eval): https://huggingface.co/datasets/PKU-Alignment/BeaverTails-Evaluation
- Project: https://sites.google.com/view/pku-beavertails

**LLMs Tested:** Multiple LLMs via Safe-RLHF framework

**Implementation Readiness:** HIGH — Fully open on HuggingFace, actively maintained, large scale. Directly usable for RLHF safety training and evaluation.

**Unique Contribution:** Largest safety-focused dataset with separated helpfulness and harmlessness annotations, enabling research on the tension between being helpful and being safe. Includes severity levels for nuanced harm assessment.

---

## NEW Finding #10: HarmBench

**Full Citation:**
Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., Sakhaee, E., Li, N., Basart, S., Li, B., Forsyth, D., & Hendrycks, D. (2024). HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal. *arXiv:2402.04249*.

**arXiv/DOI:** arXiv:2402.04249

**Frameworks:**
- 7 semantic harm categories: Cybercrime, Chemical/Biological Weapons, Copyright Violations, Misinformation, Harassment, Illegal Activities, General Harm
- Standardized red teaming evaluation with breadth, comparability, and robust metrics

**Dataset Details:**
- **Size:** Comprehensive behavior set across 7 categories
- **Format:** Standardized attack-defense evaluation pairs
- **Languages:** English
- **Scope:** 18 red teaming methods, 33 target LLMs and defenses

**Code/Data URLs:**
- GitHub: https://github.com/centerforaisafety/HarmBench
- Website: https://www.harmbench.org/

**LLMs Tested:** 33 target LLMs and defenses (largest red teaming comparison)

**Implementation Readiness:** HIGH — Fully open-source, community-driven, standardized evaluation framework. Published by Center for AI Safety.

**Unique Contribution:** First standardized, end-to-end evaluation framework for automated red teaming. Reveals that no single attack or defense is uniformly effective and that robustness is independent of model size. Enables co-development of attacks and defenses.

---

## NEW Finding #11: SaGE (Semantic Graph Entropy) / Moral Consistency Corpus

**Full Citation:**
Bonagiri, V. K., Vennam, S., Govil, P., Kumaraguru, P., & Gaur, M. (2024). SaGE: Evaluating Moral Consistency in Large Language Models. *Proceedings of LREC-COLING 2024*.

**arXiv/DOI:** arXiv:2402.13709

**Frameworks:**
- Information-theoretic moral consistency measurement
- Semantic Graph Entropy (SaGE) metric
- Rules-of-Thumb (RoTs) based evaluation

**Dataset Details:**
- **Size:** 50,000 moral questions with LLM responses and Rules of Thumb (Moral Consistency Corpus — MCC)
- **Format:** Question-response-RoT triples with consistency annotations
- **Languages:** English

**Code/Data URLs:**
- Published at LREC-COLING 2024

**LLMs Tested:** State-of-the-art LLMs (specific models in full paper)

**Implementation Readiness:** MEDIUM-HIGH — Published at major venue. Novel metric (SaGE) is model-agnostic, requires no ground truth labels.

**Unique Contribution:** First information-theoretic measure of moral consistency. Demonstrates that accuracy and consistency are not directly related — a model can be accurate but morally inconsistent. Generalizable metric applicable beyond moral reasoning.

---

## NEW Finding #12: CLAVE / ValEval

**Full Citation:**
Yao, J., Yi, X., & Xie, X. (2024). CLAVE: An Adaptive Framework for Evaluating Values of LLM Generated Responses. *arXiv:2407.10725*.

**arXiv/DOI:** arXiv:2407.10725

**Frameworks:**
- Three value systems: (1) Schwartz Theory of Basic Human Values (10 value dimensions), (2) Social risk values (14 categories from BeaverTails), (3) Additional value system
- Complementary large + small model evaluation architecture
- Value concept extraction and alignment

**Dataset Details:**
- **Size:** 13,000+ (text, value, label) tuples
- **Format:** Structured evaluation tuples with categorical labels across three value systems
- **Subsets:** "Original" primary split + "Perturbation" subset for robustness testing
- **Languages:** English

**Code/Data URLs:**
- License: CC BY-NC-ND 4.0

**LLMs Tested:** 12+ popular LLM evaluators

**Implementation Readiness:** MEDIUM-HIGH — Well-structured benchmark with three value systems. Perturbation testing adds robustness dimension.

**Unique Contribution:** Adaptive evaluation framework that combines large proprietary models (for concept extraction) with fine-tuned small models (for alignment assessment). Requires fewer than 100 human-labeled samples per value type for calibration — highly practical.

---

## NEW Finding #13: Eagle (Ethical Dataset Given from Real Interactions)

**Full Citation:**
Kaneko, M., Bollegala, D., & Baldwin, T. (2024). Eagle: Ethical Dataset Given from Real Interactions. *arXiv:2402.14258*. Also published at IJCAI 2025.

**arXiv/DOI:** arXiv:2402.14258

**Frameworks:**
- Four ethical dimensions: social bias, opinion bias, toxic language, morality
- Real-world interaction analysis (not synthetic)

**Dataset Details:**
- **Size:** ~4,461 instances total: 1,004 social bias, 831 opinion bias, 1,078 toxic language, 1,548 morality
- **Format:** Real ChatGPT conversation excerpts labeled by ethical dimension
- **Source:** ShareGPT dataset (90,665 conversations, 1.37M utterances)
- **Languages:** Multiple (extracted from real multilingual interactions)

**Code/Data URLs:**
- HuggingFace: https://huggingface.co/datasets/MasahiroKaneko/eagle
- License: CC BY 4.0

**LLMs Tested:** ChatGPT (source); applicable to any LLM

**Implementation Readiness:** HIGH — Available on HuggingFace, CC BY 4.0, extracted from real interactions.

**Unique Contribution:** First ethical evaluation dataset derived from real user-LLM interactions rather than synthetic/crowdsourced scenarios. Captures actual ethical problems users encounter when using LLMs, providing ecologically valid evaluation data.

---

## NEW Finding #14: TrolleyBench

**Full Citation:**
Zhu, A. (2025). TrolleyBench: Evaluating Emergent Moral Reasoning and Consistency in LLMs. *NeurIPS 2025 Workshop on Evaluating the Evolving LLM Lifecycle*.

**DOI/URL:** https://openreview.net/forum?id=27j9XJQV5O

**Frameworks:**
- Trolley problem variants and moral dilemma scenarios
- Ethical Consistency Index (ECI) — novel metric
- Entropy-based Inconsistency Score — novel metric
- Clarifying and contradictory follow-up evaluation

**Dataset Details:**
- **Format:** Yes/no moral judgment questions with follow-up probes for consistency
- **Design:** Dilemmas with clarifying follow-ups and contradictory follow-ups
- **Languages:** English
- **License:** CC BY 4.0

**Code/Data URLs:**
- Repository: https://anonymous.4open.science/r/TrolleyBench-FD46/README.md

**LLMs Tested:** Deepseek-R1, Mistral Small-32B, Gemini-2.5, GPT-4.1-mini (compared against human baselines)

**Implementation Readiness:** MEDIUM-HIGH — Open-source, novel metrics, tested on latest models. Workshop paper with active development.

**Unique Contribution:** First open-source benchmark explicitly designed to evaluate ethical *consistency* (not just accuracy). Introduces two novel metrics (ECI and entropy-based inconsistency). Tests whether models maintain consistent moral positions under follow-up questioning.

---

## NEW Finding #15: EthicsMH

**Full Citation:**
Kasu, S. K. R. (2025). EthicsMH: A Pilot Benchmark for Ethical Reasoning in Mental Health AI. *arXiv:2509.11648*.

**arXiv/DOI:** arXiv:2509.11648

**Frameworks:**
- Domain-specific ethical reasoning (mental health)
- Categories: confidentiality, autonomy vs. beneficence, race/gender bias
- Multi-stakeholder viewpoint evaluation

**Dataset Details:**
- **Size:** 125 therapy-relevant scenarios
- **Format:** Structured scenarios with decision options, expert-aligned reasoning, expected model behavior, real-world impact, multi-stakeholder viewpoints
- **Languages:** English
- **License:** CC BY 4.0

**Code/Data URLs:**
- arXiv: https://arxiv.org/abs/2509.11648

**LLMs Tested:** Not specified (designed as evaluation framework)

**Implementation Readiness:** MEDIUM — Pilot/seed dataset (125 scenarios). Methodological blueprint for expansion. Structured fields enable automated evaluation.

**Unique Contribution:** First benchmark specifically targeting ethical reasoning in mental health AI contexts. Addresses unique ethical tensions in clinical settings (confidentiality vs. safety, autonomy vs. beneficence). Multi-stakeholder perspective is novel.

---

## NEW Finding #16: PsychEthicsBench

**Full Citation:**
Shen, Y., Fong, S., Jiang, Y., Wang, Z., Tang, F., Xu, Q., Zhao, X., Xu, Z., Liu, J., Hu, J., Dwyer, D., & Ge, Z. (2026). PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics. *arXiv:2601.03578*.

**arXiv/DOI:** arXiv:2601.03578

**Frameworks:**
- Australian psychology and psychiatry ethical guidelines
- Principle-grounded evaluation
- Multiple evaluation modes: MCQ (single/multiple answer) and open-ended questions
- Two test modes: "Aussie" (Australian context) and "Global"

**Dataset Details:**
- **Size:** 392 ethical principles; 1,377 multiple-choice questions; 2,612 open-ended questions
- **Format:** MCQs (SMCQs + MMCQs) and OEQs with fine-grained ethicality annotations
- **Roles:** Three prospective inquirer roles for OEQs
- **Languages:** English (Australian context)

**Code/Data URLs:**
- arXiv: https://arxiv.org/abs/2601.03578

**LLMs Tested:** 14 models (including domain-specific mental health models and general-purpose LLMs)

**Implementation Readiness:** HIGH — Large-scale benchmark (4,000+ questions), systematic principle-grounded design, tested on 14 models.

**Unique Contribution:** First principle-grounded benchmark based on specific professional ethics guidelines (Australian psychology/psychiatry). Reveals that domain-specific fine-tuning can *degrade* ethical robustness — specialized models sometimes underperform base models.

---

## NEW Finding #17: CASE-Bench (Context-Aware SafEty Benchmark)

**Full Citation:**
Sun, G., Zhan, X., Feng, S., Woodland, P. C., & Such, J. (2025). CASE-Bench: Context-Aware SafEty Benchmark for Large Language Models. *ICML 2025*. arXiv:2501.14940.

**arXiv/DOI:** arXiv:2501.14940

**Frameworks:**
- Contextual Integrity theory (Nissenbaum)
- Context-dependent safety evaluation
- Human judgment baseline with statistical power analysis

**Dataset Details:**
- **Size:** 900 query-context pairs (450 queries x 2 contexts each)
- **Annotations:** 2,000+ human annotators; 21 annotations per query-context pair
- **Format:** Query-context pairs with human safety/unsafety judgments
- **Languages:** English
- **License:** CC BY 4.0

**Code/Data URLs:**
- GitHub: https://github.com/BriansIDP/CASEBench

**LLMs Tested:** Multiple open-source and commercial LLMs (presented at ICML 2025)

**Implementation Readiness:** HIGH — Published at ICML 2025, open-source on GitHub, extensive human annotations with statistical rigor.

**Unique Contribution:** First safety benchmark incorporating contextual factors into evaluation. Demonstrates that context significantly affects whether a query is safe or unsafe (p < 0.0001). Reveals that commercial LLMs often over-refuse in safe contexts, degrading user experience.

---

## Cross-Cutting Analysis

### By Implementation Readiness

| Readiness | Datasets |
|-----------|----------|
| **HIGH** | Scruples, Social Chemistry 101, Moral Stories, MIC, Value Kaleidoscope, TrustLLM, DecodingTrust, BeaverTails, HarmBench, Eagle, PsychEthicsBench, CASE-Bench |
| **MEDIUM-HIGH** | DeNEVIL/MoralPrompt, SaGE/MCC, CLAVE/ValEval, TrolleyBench |
| **MEDIUM** | EthicsMH |

### By Evaluation Dimension

| Dimension | Datasets |
|-----------|----------|
| **Moral Judgment/Reasoning** | Scruples, Social Chemistry 101, Moral Stories, MIC, DeNEVIL, TrolleyBench, SaGE |
| **Value Pluralism** | Value Kaleidoscope/ValuePrism, CLAVE/ValEval |
| **Safety/Harm** | BeaverTails, HarmBench, CASE-Bench |
| **Comprehensive Trust** | TrustLLM, DecodingTrust |
| **Domain-Specific Ethics** | EthicsMH, PsychEthicsBench |
| **Real-World Interactions** | Eagle |
| **Moral Consistency** | SaGE, TrolleyBench |

### By Scale

| Scale | Datasets |
|-------|----------|
| **Very Large (100k+)** | Social Chemistry 101 (292k RoTs, 4.5M annotations), BeaverTails (333k+ QA pairs), Value Kaleidoscope (218k values), MIC (114k annotations) |
| **Large (10k–100k)** | Scruples (32k anecdotes, 625k judgments), SaGE/MCC (50k questions), CLAVE/ValEval (13k+ tuples), Moral Stories (12k narratives) |
| **Medium (1k–10k)** | Eagle (4.4k instances), DeNEVIL/MoralPrompt (2.4k prompts), PsychEthicsBench (4k+ questions) |
| **Small (<1k)** | CASE-Bench (900 pairs), EthicsMH (125 scenarios), TrolleyBench (workshop-scale) |

### By Year

| Year | Datasets |
|------|----------|
| **2020** | Social Chemistry 101 |
| **2021** | Scruples (AAAI), Moral Stories (EMNLP) |
| **2022** | MIC (ACL) |
| **2023** | DecodingTrust (NeurIPS), BeaverTails (NeurIPS) |
| **2024** | DeNEVIL (ICLR), Value Kaleidoscope (AAAI), TrustLLM (ICML), HarmBench, SaGE (LREC-COLING), CLAVE/ValEval, Eagle |
| **2025** | TrolleyBench (NeurIPS Workshop), EthicsMH, CASE-Bench (ICML) |
| **2026** | PsychEthicsBench |

### Notable Datasets on HuggingFace Hub

| Dataset | HuggingFace URL | Downloads |
|---------|-----------------|-----------|
| BeaverTails | huggingface.co/datasets/PKU-Alignment/BeaverTails | High |
| Eagle | huggingface.co/datasets/MasahiroKaneko/eagle | Moderate |
| Moral Stories | huggingface.co/datasets/demelin/moral_stories | Moderate |
| DecodingTrust | huggingface.co/datasets/AI-Secure/DecodingTrust | High |
| ETHICS (Hendrycks) | huggingface.co/datasets/hendrycks/ethics | Very High |

---

## Additional Datasets Identified (Briefly Noted)

The following were also identified during search but are either closely related to already-known items or require further verification:

1. **One Model, Many Morals** (Farid et al., 2025, arXiv:2509.21443) — Cross-linguistic moral reasoning evaluation across 5 languages with 7 LLMs. Introduces typology of moral reasoning errors.

2. **Evaluating Moral Beliefs across LLMs through a Pluralistic Framework** (Liu et al., 2024, EMNLP Findings, arXiv:2411.03665) — 472 moral choice scenarios in Chinese with Best-Worst Scaling evaluation.

3. **MoralDial** (Sun et al., 2022, ACL) — Framework for training and evaluating moral dialogue systems via moral discussions.

4. **Diagnosing Moral Reasoning Acquisition in Language Models** (2025, EMNLP Findings) — Pragmatics and generalization assessment.

---

## Recommendations for CEI Project

1. **Immediate adoption candidates** (large, public, well-documented):
   - BeaverTails (for safety alignment evaluation)
   - Social Chemistry 101 (for moral norm understanding)
   - DecodingTrust (for comprehensive trustworthiness)
   - TrustLLM (for multi-dimensional evaluation)

2. **Novel evaluation approaches** worth incorporating:
   - SaGE metric for measuring moral consistency
   - TrolleyBench's Ethical Consistency Index
   - CASE-Bench's context-dependent safety evaluation
   - CLAVE's adaptive evaluation with minimal human labels

3. **Domain-specific extensions**:
   - EthicsMH and PsychEthicsBench for mental health ethics
   - Eagle for real-world interaction analysis

4. **Foundational training data**:
   - Scruples, Social Chemistry 101, and Moral Stories form the foundation that trained Delphi and other moral reasoning systems

---

*Report generated by Agent 5 on 2026-02-07. All findings verified as not present in the 67+ already-known dataset list.*
