# Master Paper List: Ethical Values Alignment Benchmarks & Datasets for LLMs
**Generated:** 2026-02-07
**Source:** 13 agent reports (Agents 2-19, excluding Agent 1)
**Deduplication:** arXiv ID -> DOI -> fuzzy title match (threshold=0.90)

---

## Summary Statistics

- **Total unique papers:** 300
- **Papers found by multiple agents:** 48
- **Implementation Readiness:** HIGH=177, MEDIUM=108, LOW=14, UNKNOWN=1

### By Year

- 2026: 21
- 2025: 164
- 2024: 94
- 2023: 10
- 2022: 6
- 2021: 3
- 2020: 1
- 2019: 1

### Multi-Agent Papers (found by 2+ agents)

- **MoralBench** -- Agent 14, Agent 15, Agent 16, Agent 19
- **EMNLP (Educator-role Moral and Normative LLMs Profiling)** -- Agent 2, Agent 7-8, Agent 19
- **LLM Ethics Benchmark (Three-Dimensional Assessment)** -- Agent 14, Agent 16, Agent 19
- **Normative Evaluation of LLMs with Everyday Moral Dilemmas (Sachdeva et al., FAccT 2025)** -- Agent 3, Agent 17, Agent 19
- **One Model, Many Morals: Uncovering Cross-Linguistic Misalignments in Computational Moral Reasoning** -- Agent 7-8, Agent 12-13
- **PsychEthicsBench** -- Agent 5, Agent 14
- **Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval)** -- Agent 7-8, Agent 19
- **EthicsMH** -- Agent 5, Agent 14
- **GermanPartiesQA: Benchmarking LLMs for Political Alignment and Sycophancy** -- Agent 3, Agent 17
- **Large Language Models Show Amplified Cognitive Biases in Moral Decision-Making** -- Agent 6, Agent 19
- **MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation** -- Agent 15, Agent 19
- **MedEthicsQA: A Comprehensive Question Answering Benchmark for Medical Ethics Evaluation of LLMs** -- Agent 6, Agent 14
- **Moral Alignment for LLM Agents (Intrinsic Rewards)** -- Agent 7-8, Agent 18
- **PrinciplismQA: Towards Assessing Medical Ethics from Knowledge to Practice** -- Agent 6, Agent 14
- **Robustness of Large Language Models in Moral Judgements** -- Agent 6, Agent 19
- **SORRY-Bench -- Systematically Evaluating LLM Safety Refusal** -- Agent 4, Agent 16
- **Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework** -- Agent 7-8, Agent 19
- **SycEval: Evaluating LLM Sycophancy** -- Agent 3, Agent 17
- **The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in LLMs with a Multi-Framework Approach** -- Agent 6, Agent 19
- **The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and LLMs** -- Agent 6, Agent 19
- **TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs** -- Agent 4, Agent 6
- **Agent-SafetyBench: Evaluating the Safety of LLM Agents** -- Agent 7-8, Agent 16
- **Collective Constitutional AI: Aligning a Language Model with Public Input** -- Agent 3, Agent 16
- **Decolonial AI Alignment -- Openness, Visesa-Dharma, and Including Excluded Knowledges** -- Agent 9-11, Agent 12-13
- **EAI -- Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas** -- Agent 4, Agent 18
- **Eagle (Ethical Dataset Given from Real Interactions)** -- Agent 5, Agent 17
- **JailbreakBench -- An Open Robustness Benchmark** -- Agent 4, Agent 16
- **MULTITP -- Language Model Alignment in Multilingual Trolley Problems** -- Agent 4, Agent 6
- **SG-Bench -- Evaluating LLM Safety Generalization** -- Agent 4, Agent 16
- **SafetyBench: Evaluating the Safety of Large Language Models** -- Agent 7-8, Agent 16
- **Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?** -- Agent 7-8, Agent 16
- **Value FULCRA** -- Agent 2, Agent 19
- **WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning** -- Agent 7-8, Agent 16
- **WalledEval** -- Agent 2, Agent 16
- **ProsocialDialog: A Prosocial Backbone for Conversational Agents** -- Agent 15, Agent 17

---

## Complete Paper List

### 1. Beyond Verdicts: Evaluating Language Model Moral Competence (Survey/Framework)

- **Authors:** Aaron J. Snoswell, Daniel Kilov, Seth Lazar
- **Year:** 2026
- **Venue:** AAAI 2026
- **Dataset Size:** Survey paper; taxonomy categorizing evaluations across datasets, behaviors, and metrics
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 2. Bias Beyond Borders

- **Authors:** Afrozah Nadeem, Agrima, Mehwish Nasim, Usman Naseem
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.23001](https://arxiv.org/abs/2601.23001)
- **Dataset Size:** Political Compass Test across 50 countries, 33 languages; introduces Cross-Lingual Alignment Steering (CLAS) mitigation framework
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 3. BiasJailbreak

- **Authors:** Isack Lee, Haebin Seong
- **Year:** 2026
- **Venue:** AAAI 2026
- **arXiv:** [2410.13334](https://arxiv.org/abs/2410.13334)
- **Dataset Size:** Adversarial prompts with systematically varied demographic keywords
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16

---

### 4. BiasLab (Multilingual Dual-Framing Framework)

- **Authors:** William Guey et al.
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.06861](https://arxiv.org/abs/2601.06861)
- **Dataset Size:** Mirrored probe pairs under strict dual-framing scheme; randomized instructional wrappers; fixed-choice Likert response format; multilingual
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 5. Building Interpretable Models for Moral Decision-Making

- **Authors:** Goel, M., Das, A
- **Year:** 2026
- **Venue:** NeurIPS 2025
- **arXiv:** [2602.03351](https://arxiv.org/abs/2602.03351)
- **Dataset Size:** Moral Machine dataset: 3 million trolley-problem scenarios, 5.4M total responses, 1.7M unique scenarios
- **Code/Data:** https://github.com/Lossfunk/modeling-moral-machine
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 6

---

### 6. JMedEthicBench

- **Authors:** Junyu Liu et al
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.01627](https://arxiv.org/abs/2601.01627)
- **Dataset Size:** 50,000+ adversarial conversations
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 7. Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs (ValAct-15k)

- **Authors:** Jen-tse Huang et al.
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.07972](https://arxiv.org/abs/2601.07972)
- **Dataset Size:** ValAct-15k: 3,000 advice-seeking scenarios derived from Reddit; 55 human participants for comparison
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19

---

### 8. MedES (Chinese Medical Ethics Scenarios)

- **Authors:** Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.07954](https://arxiv.org/abs/2601.07954)
- **Dataset Size:** 12 real-world high-risk clinical scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 14

---

### 9. One Model, Many Morals: Uncovering Cross-Linguistic Misalignments in Computational Moral Reasoning

- **Authors:** Farid, S., Lin, J., Chen, Z., Kumar, S., & Jurgens, D
- **Year:** 2026
- **Venue:** ICLR 2026
- **arXiv:** [2509.21443](https://arxiv.org/abs/2509.21443)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 7-8, Agent 12-13

---

### 10. PluriHarms

- **Authors:** Jing-Jing Li et al.
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.08951](https://arxiv.org/abs/2601.08951)
- **Dataset Size:** 150 prompts calibrated across full harmfulness spectrum
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16, Agent 1

---

### 11. PoliBias (Parliamentary Voting Records)

- **Authors:** Jieying Chen et al.
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.08785](https://arxiv.org/abs/2601.08785)
- **Dataset Size:** Three national benchmarks:
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 12. PsychEthicsBench

- **Authors:** Shen et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.03578](https://arxiv.org/abs/2601.03578)
- **Dataset Size:** Size: 392 ethical principles; 1,377 multiple-choice questions; 2,612 open-ended questions
- **Code/Data:** https://github.com/ElsieSHEN/PsychEthicsBench](https://github.com/ElsieSHEN/PsychEthicsBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5, Agent 14

---

### 13. RedBench

- **Authors:** Quy-Anh Dang, Chris Ngo, Truong-Son Hy
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2601.03699](https://arxiv.org/abs/2601.03699)
- **Dataset Size:** 29,362 samples (attack and refusal prompts)
- **Code/Data:** https://github.com/knoveleng/redeval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 14. VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models

- **Authors:** Unknown
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** [2602.03160](https://arxiv.org/abs/2602.03160)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 7-8, Agent 1

---

### 15. "Do Your Guardrails Even Guard?" Evaluating Moderation Guardrails for LLM Alignment

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1609/aies.v8i1.36583
- **Dataset Size:** Real-world evaluation scenarios including resume quality assessment and recidivism prediction
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3

---

### 16. AEGIS 2.0

- **Authors:** Shaona Ghosh et al.
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2501.09004](https://arxiv.org/abs/2501.09004)
- **Dataset Size:** 33,416 annotated human-LLM interactions (34,248 total samples)
- **Code/Data:** https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0; https://huggingface.co/nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 17. AI Alignment at Your Discretion

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2502.10441](https://arxiv.org/abs/2502.10441)
- **DOI:** 10.1145/3715275.3732194
- **Dataset Size:** Metrics for analyzing discretion in preference datasets used for RLHF; audits across multiple alignment datasets
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 18. AI Language Model Rivals Expert Ethicist in Perceived Moral Expertise

- **Authors:** [Authors from Kurt Gray Lab]
- **Year:** 2025
- **Venue:** Scientific Reports
- **DOI:** 10.1038/s41598-025-86510-0
- **Dataset Size:** Study 1 (n=501): Comparison of GPT moral justifications vs. human-written justifications
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6

---

### 19. ALYMPICS: LLM Agents Meet Game Theory

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** COLING 2025
- **arXiv:** [2311.03220](https://arxiv.org/abs/2311.03220)
- **Dataset Size:** Sandbox-based game environments (pilot: Water Allocation Challenge -- 20-day multi-round sealed-bid auction); text-based agent interaction
- **Code/Data:** https://github.com/microsoft/Alympics
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 20. Addressing Moral Uncertainty using LLMs for Ethical Decision-Making

- **Authors:** Rohit K. Dubey, Damian Dailisan, Sachit Mahajan
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2503.05724](https://arxiv.org/abs/2503.05724)
- **Dataset Size:** RL-based ethical decision-making framework with LLM-generated moral belief scores
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 21. Aftina -- Enhancing Stability in AI-Based Islamic Fatwa Generation

- **Authors:** Mohammed, A. & Ali, H
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1007/s00521-025-11229-y
- **Dataset Size:** Fatwa-specific dataset for fine-tuning and evaluation
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 9-11

---

### 22. AgentHarm

- **Authors:** Maksym Andriushchenko et al.
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2410.09024](https://arxiv.org/abs/2410.09024)
- **Dataset Size:** 110 base harmful behaviors manually curated
- **Code/Data:** https://huggingface.co/datasets/ai-safety-institute/AgentHarm
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 23. An Evaluation of Cultural Value Alignment in LLM

- **Authors:** Sukiennik, N., Gao, C., Xu, F., & Li, Y
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.08863](https://arxiv.org/abs/2504.08863)
- **Dataset Size:** Format: Validated cultural values questionnaire with human ground truth
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 24. Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts

- **Authors:** Nakanishi, A., Sano, Y., Liu, G., & Pierri, F
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2503.01947](https://arxiv.org/abs/2503.01947)
- **Dataset Size:** Size: 3,612 prompts (301 social group terms x 12 stereotype-inducing templates)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 25. AraTrust -- An Evaluation of Trustworthiness for LLMs in Arabic

- **Authors:** Alghamdi, R., Alyafeai, Z., et al
- **Year:** 2025
- **Venue:** COLING 2025
- **arXiv:** [2403.09017](https://arxiv.org/abs/2403.09017)
- **Dataset Size:** 522 human-written multiple-choice questions
- **Code/Data:** https://huggingface.co/datasets/asas-ai/AraTrust
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 26. Awesome-LLM-Eval Repository (Meta-Resource)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2024
- **Dataset Size:** See report
- **Code/Data:** https://github.com/onejune2018/Awesome-LLM-Eval; https://github.com/onejune2018/Awesome-LLM-Eval; https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers; https://github.com/AthenaCore/AwesomeResponsibleAI; https://github.com/awesomelistsio/awesome-ai-ethics; https://github.com/thu-coai/AISafetyLab; https://github.com/centerforaisafety
- **Implementation Readiness:** UNKNOWN
- **Source Agent(s):** Agent 7-8

---

### 27. BasqBBQ (Basque BBQ)

- **Authors:** Muitze Zulaika et al
- **Year:** 2025
- **Venue:** COLING 2025
- **Dataset Size:** 43,240 examples (20,716 ambiguous + 20,716 disambiguated) across 8 categories; QA multiple-choice format
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 28. Between a Rock and a Hard Place (TRIAL)

- **Authors:** Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.05367](https://arxiv.org/abs/2509.05367)
- **Dataset Size:** Multi-turn red-teaming methodology
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16

---

### 29. Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval)

- **Authors:** Alessio Galatolo, Luca Alberto Rappuoli, Katie Winkle, Meriem Beloucif
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2508.12754](https://arxiv.org/abs/2508.12754)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/alessioGalatolo/AMAeval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 19

---

### 30. BiasLab (Political Bias Detection -- News Articles)

- **Authors:** Kma Solaiman
- **Year:** 2025
- **Venue:** ICML 2025
- **arXiv:** [2505.16081](https://arxiv.org/abs/2505.16081)
- **Dataset Size:** 300 political news articles (from curated 900-document pool); crowdworker annotations on two independent scales; rationale indicators
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 31. CARE -- Multilingual Human Preference Learning for Cultural Awareness

- **Authors:** Guo et al.
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2504.05154](https://arxiv.org/abs/2504.05154)
- **Dataset Size:** Size: 3,490 culturally specific questions + 31,700 LLM/human-written responses with human preference judgments
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 32. CASE-Bench (Context-Aware SafEty Benchmark)

- **Authors:** Sun, G., Zhan, X., Feng, S., Woodland, P. C., & Such, J
- **Year:** 2025
- **Venue:** ICML 2025
- **arXiv:** [2501.14940](https://arxiv.org/abs/2501.14940)
- **Dataset Size:** Size: 900 query-context pairs (450 queries x 2 contexts each)
- **Code/Data:** https://github.com/BriansIDP/CASEBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 33. COIG-P -- Chinese Preference Dataset for Alignment with Human Values

- **Authors:** Authors
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.05535](https://arxiv.org/abs/2504.05535)
- **Dataset Size:** 1,009,000 Chinese preference pairs (very large scale)
- **Code/Data:** https://github.com/multimodal-art-projection/COIG-P; https://huggingface.co/datasets/m-a-p/COIG-P
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 34. Can We Trust AI Benchmarks? An Interdisciplinary Review

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2502.06559](https://arxiv.org/abs/2502.06559)
- **DOI:** 10.1609/aies.v8i1.36595
- **Dataset Size:** Meta-review of ~110 studies discussing benchmark shortcomings over last 10 years
- **Code/Data:** None listed
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 3

---

### 35. ConflictScope: Generative Value Conflicts Reveal LLM Priorities

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.25369](https://arxiv.org/abs/2509.25369)
- **Dataset Size:** Automated pipeline generating value-conflict dilemmas from user-defined value sets; systematic pairwise comparison of values; MCQ and open-ended formats
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15, Agent 1

---

### 36. Corpus-Based Medical Ethics Decision-Making Evaluation

- **Authors:** Memi Ebara et al.
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.3233/SHTI250854
- **Dataset Size:** 50 clinical case scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 14

---

### 37. D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2509.17938](https://arxiv.org/abs/2509.17938)
- **Dataset Size:** Red-teaming exercise-generated dataset; each sample contains: adversarial system prompt, user query, seemingly innocuous response, and internal chain-of-thought revealing malicious intent
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 38. DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2510.15501](https://arxiv.org/abs/2510.15501)
- **Dataset Size:** 150 scenarios with 1,000+ evaluation samples across 5 domains; single-turn and multi-turn interactions; thought + response evaluation
- **Code/Data:** https://github.com/Aries-iai/DeceptionBench; https://huggingface.co/datasets/PKU-Alignment/DeceptionBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 39. Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models

- **Authors:** [Authors not fully extracted]
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1016/j.chbah.2025.100121
- **Dataset Size:** Series of moral dilemmas, both personal and impersonal
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6

---

### 40. Deep Value Benchmark

- **Authors:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak
- **Year:** 2025
- **Venue:** NeurIPS 2025
- **arXiv:** [2511.02109](https://arxiv.org/abs/2511.02109)
- **Dataset Size:** Dataset with controlled confounds between deep values and shallow features; three separate human validation experiments
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19, Agent 1

---

### 41. Diagnosing Moral Reasoning Acquisition

- **Authors:** Guangliang Liu, Zimo Qi, Xitong Zhang, Lei Jiang, Kristen Johnson
- **Year:** 2025
- **Venue:** EMNLP 2025
- **Dataset Size:** Size: Dataset with moral situations annotated with MFT classifications, Rules of Thumb, and Judgments
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 42. Diagnosing Moral Reasoning Acquisition in Language Models: Pragmatics and Generalization

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2502.16600](https://arxiv.org/abs/2502.16600)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8

---

### 43. Discerning What Matters: Multi-Dimensional Moral Competence Assessment

- **Authors:** Daniel Kilov, Caroline Hendy, Secil Yanik Guyot, Aaron J. Snoswell, Seth Lazar
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2506.13082](https://arxiv.org/abs/2506.13082)
- **Dataset Size:** Two experiments: standard ethical vignettes and novel scenarios with embedded irrelevant details; comparisons with non-expert humans and professional philosophers
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 44. Do LLMs Have Consistent Values?

- **Authors:** Naama Rozen, Liat Bezalel, Gal Elidan, Amir Globerson, Ella Daniel
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2407.12878](https://arxiv.org/abs/2407.12878)
- **Dataset Size:** Survey-based evaluation measuring value correlations within single sessions; tests whether LLMs produce human-like value personas
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19

---

### 45. ELEPHANT (Social Sycophancy)

- **Authors:** Myra Cheng, Sunny Yu, Cinoo Lee, Pranav Khadpe, Lujain Ibrahim, Dan Jurafsky
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.13995](https://arxiv.org/abs/2505.13995)
- **Dataset Size:** Two evaluation datasets: open-ended questions (OEQ) and Reddit r/AmITheAsshole (AITA) posts; measures across 5 dimensions; comparison to human baselines
- **Code/Data:** https://github.com/myracheng/elephant
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 46. EMNLP (Educator-role Moral and Normative LLMs Profiling)

- **Authors:** Yilin Jiang, Mingzi Zhang, Sheng Jin, Zengyi Yu, Xiangjie Kong, Binghao Tu
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2508.15250](https://arxiv.org/abs/2508.15250)
- **DOI:** 10.18653/v1/2025.emnlp-main.42
- **Dataset Size:** Size: 88 teacher-specific moral dilemmas
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2, Agent 7-8, Agent 19

---

### 47. EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2312.06281](https://arxiv.org/abs/2312.06281)
- **Dataset Size:** 60 English-language questions; dialogue-based emotion intensity prediction tasks; models predict intensity of 4 emotional states per question on a 0-1 scale
- **Code/Data:** https://github.com/EQ-bench/EQ-Bench](https://github.com/EQ-bench/EQ-Bench; https://huggingface.co/datasets/pbevan11/EQ-Bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 48. EmoBench-M: Benchmarking Emotional Intelligence for Multimodal Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2502.04424](https://arxiv.org/abs/2502.04424)
- **Dataset Size:** 13 evaluation scenarios across 3 dimensions; multimodal inputs (text + visual)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 49. EthicsMH

- **Authors:** Kasu, S. K. R
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2509.11648](https://arxiv.org/abs/2509.11648)
- **Dataset Size:** Size: 125 therapy-relevant scenarios
- **Code/Data:** https://huggingface.co/datasets/UVSKKR/Ethical-Reasoning-in-Mental-Health-v1](https://huggingface.co/datasets/UVSKKR/Ethical-Reasoning-in-Mental-Health-v1
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 5, Agent 14, Agent 1

---

### 50. EtiCor++: Towards Understanding Etiquettical Bias in LLMs

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2024
- **arXiv:** [2506.08488](https://arxiv.org/abs/2506.08488)
- **Dataset Size:** Expanded from EtiCor with additional cultures and regions; cleaned noisy samples; new tasks and metrics; covers Asia, Latin America, Middle East/Africa, North America/Europe, and more
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 51. Exploring Cultural Variations in Moral Judgments with Large Language Models

- **Authors:** Mohammadi, H., & Bagheri, A
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.12433](https://arxiv.org/abs/2506.12433)
- **Dataset Size:** Format: Structured probing prompts with contrasting moral statements; log-probability scoring
- **Code/Data:** https://github.com/mohammadi-hadi/cultural-moral-judgments-llms
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 52. FairI Tales / INDIC-BIAS -- Evaluation of Fairness in Indian Contexts

- **Authors:** Authors
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2506.23111](https://arxiv.org/abs/2506.23111)
- **DOI:** 10.1007/s44443-025-00137-9
- **Dataset Size:** 20,000 manually validated real-world scenario templates
- **Code/Data:** https://github.com/AI4Bharat/indic-bias; https://huggingface.co/datasets/ai4bharat/Indic-Bias; https://huggingface.co/blog/Omartificial-Intelligence-Space/ilmaam-overview
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 53. FairMT-Bench

- **Authors:** Zhiting Fan, Ruizhe Chen, Tianxiang Hu, Zuozhu Liu
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2410.19317](https://arxiv.org/abs/2410.19317)
- **Dataset Size:** FairMT-10K: 10,000 multi-turn dialogues
- **Code/Data:** https://github.com/FanZT6/FairMT-bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 54. FiSCo (Fine-grained Semantic Comparison)

- **Authors:** Weijie Xu et al.
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2506.19028](https://arxiv.org/abs/2506.19028)
- **Dataset Size:** Pipeline-based evaluation framework; decomposes LLM outputs into semantic claims; applies statistical hypothesis testing (Welch's t-test); validated on synthetic and human-annotated datasets
- **Code/Data:** https://github.com/HuXiangkun/FiSCo
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 55. Fluent but Foreign -- Even Regional LLMs Lack Cultural Alignment

- **Authors:** Agarwal, D., Shukla, A., Sitaram, S., & Vashistha, A
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2505.21548](https://arxiv.org/abs/2505.21548)
- **Dataset Size:** Format: Four complementary population-scale benchmarks; user study with 115 Indian participants
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 56. From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2505.16408](https://arxiv.org/abs/2505.16408)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8

---

### 57. GAMEBoT: Transparent Assessment of LLM Reasoning in Games

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2412.13602](https://arxiv.org/abs/2412.13602)
- **Dataset Size:** 8 games (including Pong, TicTacToe, Texas Hold'em, etc.); dynamic game-based evaluation with CoT prompts and rule-based ground truth generation
- **Code/Data:** https://github.com/Visual-AI/GAMEBoT
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 58. GermanPartiesQA: Benchmarking LLMs for Political Alignment and Sycophancy

- **Authors:** Jan Batzner, Volker Stocker, Stefan Schmid, Gjergji Kasneci
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2407.18008](https://arxiv.org/abs/2407.18008)
- **DOI:** 10.1609/aies.v8i1.36552
- **Dataset Size:** 418 political statements from German Voting Advice Applications across 11 elections; German language
- **Code/Data:** https://github.com/janbatzner/germanpartiesqa
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3, Agent 17

---

### 59. GuardEval

- **Authors:** Naseem Machlovi et al.
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2601.03273](https://arxiv.org/abs/2601.03273)
- **Dataset Size:** 106 fine-grained categories
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16, Agent 1

---

### 60. Hajj-FQA -- Benchmark Arabic Dataset for Hajj Fatwa QA

- **Authors:** Authors
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1007/s44443-025-00128-w
- **Dataset Size:** 2,826 QA pairs from 800 expert-annotated fatwas
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 9-11

---

### 61. Healthcare Ethics & Safety QA (China -- Healthy China 2030)

- **Authors:** Mouxiao Bian, Rongzhao Zhang, Chao Ding, Xinwei Peng, and Jie Xu
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.07205](https://arxiv.org/abs/2505.07205)
- **Dataset Size:** 12,000 question-answer items
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 14

---

### 62. How LLM Counselors Violate Ethical Standards in Mental Health Practice

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1609/aies.v8i1.36632
- **Dataset Size:** 137 sessions (110 self-counseling tests by trained peer counselors + 27 simulated clinical interactions reviewed by licensed psychologists)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3

---

### 63. HumaniBench: A Human-Centric Framework for Large Multimodal Models Evaluation

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.11454](https://arxiv.org/abs/2505.11454)
- **Dataset Size:** 32,000 expert-verified image-question pairs derived from real-world news imagery; GPT-4o-assisted annotation pipeline with domain expert verification; 7 task types including open/closed-ended VQA, mul
- **Code/Data:** https://github.com/VectorInstitute/HumaniBench](https://github.com/VectorInstitute/HumaniBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 64. IndiCASA -- Dataset and Bias Evaluation Framework for LLMs in Indian Context

- **Authors:** Authors
- **Year:** 2025
- **Venue:** AIES 2025
- **arXiv:** [2510.02742](https://arxiv.org/abs/2510.02742)
- **Dataset Size:** 2,575 human-validated sentences
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 65. Investigating Machine Moral Judgement Through the Delphi Experiment (DelphiHYBRID)

- **Authors:** Jiang, L., Sakaguchi, K., et al
- **Year:** 2025
- **Venue:** Nature Machine Intelligence
- **DOI:** 10.1038/s42256-024-00969-6
- **Dataset Size:** DelphiHYBRID system: operationalizes Gert's 10 moral principles as symbolic constraints
- **Code/Data:** https://github.com/liweijiang/delphi
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6

---

### 66. IslamicEval 2025 -- Shared Task on Capturing LLM Hallucination in Islamic Content

- **Authors:** Authors
- **Year:** 2025
- **Venue:** Unknown
- **Dataset Size:** Subtask 1: Hallucination detection/correction dataset for Qur'anic and Hadith references
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 67. JETHICS -- Japanese Ethics Understanding Evaluation Dataset

- **Authors:** Takeshita, M., & Rzepka, R
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.16187](https://arxiv.org/abs/2506.16187)
- **Dataset Size:** Size: 77,896 total examples
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 68. LEXam

- **Authors:** Yu Fan et al.
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.12864](https://arxiv.org/abs/2505.12864)
- **Dataset Size:** 4,886 law exam questions (English + German)
- **Code/Data:** https://github.com/LEXam-Benchmark/LEXam](https://github.com/LEXam-Benchmark/LEXam; https://huggingface.co/datasets/LEXam-Benchmark/LEXam](https://huggingface.co/datasets/LEXam-Benchmark/LEXam
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 69. LLM Ethics Benchmark (Three-Dimensional Assessment)

- **Authors:** Junfeng Jiao et al.
- **Year:** 2025
- **Venue:** Scientific Reports
- **arXiv:** [2505.00853](https://arxiv.org/abs/2505.00853)
- **DOI:** 10.1038/s41598-025-18489-7
- **Dataset Size:** Uses modified measures from moral psychology: MFQ, Moral Dilemmas, WVS
- **Code/Data:** https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark](https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14, Agent 16, Agent 19

---

### 70. LLM Rationalis? Measuring Bargaining Capabilities of AI Negotiators

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2512.13063](https://arxiv.org/abs/2512.13063)
- **Dataset Size:** Large-scale empirical comparison across natural-language and numeric-offers settings; 6 controlled power-asymmetry scenarios; novel metrics (burstiness tau, Concession-Rigidity Index)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 71. LLMEval-Med (Medical Safety & Ethics Component)

- **Authors:** Ming Zhang et al.
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2506.04078](https://arxiv.org/abs/2506.04078)
- **Dataset Size:** 2,996 questions total across 5 dimensions (Medical Knowledge, Language Understanding, Reasoning, Text Generation, Safety & Ethics)
- **Code/Data:** https://github.com/llmeval/LLMEval-Med](https://github.com/llmeval/LLMEval-Med
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 72. LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)

- **Authors:** Hu et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2507.10852](https://arxiv.org/abs/2507.10852)
- **Dataset Size:** JudiFair dataset: 177,100 unique case facts
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 6

---

### 73. LLMsPark: A Benchmark for Evaluating LLMs in Strategic Gaming Contexts

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2509.16610](https://arxiv.org/abs/2509.16610)
- **Dataset Size:** 5 games (Prisoner's Dilemma, Trust Game, Nim, Dictator Game, Who Is Spy); online multiplayer platform; 15 LLMs cross-evaluated via leaderboard scoring
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 74. Large Language Models Meet Moral Values: Comprehensive Assessment

- **Authors:** Luana Bulla, Misael Mongiovi, Stefano De Giorgis, Aldo Gangemi
- **Year:** 2025
- **Venue:** Unknown
- **Dataset Size:** Uses MFRC for evaluation; multi-label and binary classification scenarios
- **Code/Data:** https://github.com/LuanaBulla/Detection-of-Morality-in-Text
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19

---

### 75. Large Language Models Show Amplified Cognitive Biases in Moral Decision-Making

- **Authors:** Capraro, V., et al
- **Year:** 2025
- **Venue:** PNAS
- **DOI:** 10.1073/pnas.2412015122
- **Dataset Size:** Series of realistic moral dilemmas (personal and impersonal)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6, Agent 19

---

### 76. LegalAgentBench

- **Authors:** Haitao Li et al.
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2412.17259](https://arxiv.org/abs/2412.17259)
- **Dataset Size:** 300 carefully annotated tasks
- **Code/Data:** https://github.com/CSHaitao/LegalAgentBench](https://github.com/CSHaitao/LegalAgentBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 77. LiveSecBench -- A Dynamic Event-Driven Safety Benchmark for Chinese LLMs

- **Authors:** Li, X. et al
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2511.02366](https://arxiv.org/abs/2511.02366)
- **Dataset Size:** Dynamic, continuously updated (latest version v251215)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 78. LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.07403](https://arxiv.org/abs/2509.07403)
- **Dataset Size:** 6 tasks (Emotion Classification, Detection, QA, Conversation, Summary, Expression); average context length of 15,341 tokens; simulates realistic long emotional dialogues
- **Code/Data:** https://github.com/LongEmotion/LongEmotion](https://github.com/LongEmotion/LongEmotion; https://huggingface.co/datasets/LongEmotion/LongEmotion
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 79. MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2503.03750](https://arxiv.org/abs/2503.03750)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/centerforaisafety/mask
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8

---

### 80. MASLegalBench

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.24922](https://arxiv.org/abs/2509.24922)
- **Dataset Size:** 950 multiple-choice questions
- **Code/Data:** https://github.com/HKUST-KnowComp/MASLegalBench](https://github.com/HKUST-KnowComp/MASLegalBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 81. MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation

- **Authors:** Jackson Trager et al.
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2506.19073](https://arxiv.org/abs/2506.19073)
- **Dataset Size:** 3,000 tweets in 4 languages (Portuguese, Persian, Italian, English); annotated for hate speech, fine-grained moral categories, and text span rationales; expert-annotated
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15, Agent 19

---

### 82. MSLR-Bench (Multi-Step Legal Reasoning)

- **Authors:** Wenhan Yu, Xinbo Lin, Lanxin Ni, Jinhua Cheng, and Lei Sha
- **Year:** 2025
- **Venue:** AAAI 2026
- **arXiv:** [2511.07979](https://arxiv.org/abs/2511.07979)
- **Dataset Size:** ~1,400 cases with 60,000 step-level annotations
- **Code/Data:** https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 83. Mapping Moral Reasoning in LLMs: A Multi-Dimensional Analysis of Safety Principle Conflicts

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1609/aies.v8i2.36665
- **Dataset Size:** Scenarios where multiple safety principles conflict within the same prompt; multi-dimensional analysis of reasoning chains
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 84. Measuring Moral LLM Responses in Multilingual Capacities

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2510.08776](https://arxiv.org/abs/2510.08776)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 7-8

---

### 85. Measuring What Matters: Connecting AI Ethics Evaluations to System Attributes, Hazards, and Harms (RAI Measures Dataset)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** Unknown
- **Dataset Size:** RAI Measures Dataset — 791 ethical evaluation measures mapped to system attributes, hazards, and ethical principles
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 86. MedEthicEval

- **Authors:** Haoan Jin, Jiacheng Shi, Hanhui Xu, Kenny Q. Zhu, and Mengyue Wu
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2503.02374](https://arxiv.org/abs/2503.02374)
- **Dataset Size:** Three distinct datasets:
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 14

---

### 87. MedEthicsQA: A Comprehensive Question Answering Benchmark for Medical Ethics Evaluation of LLMs

- **Authors:** Wei, J., Meng, Z., Xiao, Z., Hu, T., Feng, Y., Zhou, Z., Wu, J., & Liu, Z
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.22808](https://arxiv.org/abs/2506.22808)
- **Dataset Size:** 5,623 multiple-choice questions + 5,351 open-ended questions = 10,974 total items
- **Code/Data:** https://github.com/JianhuiWei7/MedEthicsQA
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 6, Agent 14

---

### 88. Metaethical Perspectives on 'Benchmarking' AI Ethics

- **Authors:** LaCroix, T. & Luccioni, S
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1007/s43681-025-00703-x
- **Dataset Size:** Not a benchmark paper per se, but a critical philosophical analysis of WHY benchmarking ethics is fundamentally problematic
- **Code/Data:** None listed
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 6

---

### 89. Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion

- **Authors:** Shankar, H., S P, V., Margapuri, S., & Mazumder, D
- **Year:** 2025
- **Venue:** Scientific Reports
- **arXiv:** [2306.16388](https://arxiv.org/abs/2306.16388)
- **Dataset Size:** Format: Survey-based alignment evaluation
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 12-13

---

### 90. Moral Alignment for LLM Agents (Intrinsic Rewards)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2410.01639](https://arxiv.org/abs/2410.01639)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/liza-tennant/LLM_morality
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 18

---

### 91. Moral Anchor System: A Predictive Framework for AI Value Alignment and Drift Prevention

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2510.04073](https://arxiv.org/abs/2510.04073)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 7-8

---

### 92. Moral Reasoning Across Languages: The Critical Role of Low-Resource Languages in LLMs (MMRB)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2504.19759](https://arxiv.org/abs/2504.19759)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 7-8

---

### 93. MultiAgentBench (MARBLE): Evaluating Collaboration and Competition of LLM Agents

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2503.01935](https://arxiv.org/abs/2503.01935)
- **Dataset Size:** Diverse multi-agent interactive scenarios spanning collaborative coding to gaming; milestone-based KPIs for measuring collaboration quality
- **Code/Data:** https://github.com/ulab-uiuc/MARBLE; https://github.com/MultiagentBench/MARBLE
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 94. Navigating the Political Compass (Multilingual, 50 Countries)

- **Authors:** Chadi Helwe, Oana Balalau, Davide Ceolin
- **Year:** 2025
- **Venue:** ACL 2025
- **Dataset Size:** Political Compass Test administered across 50 most populous countries, their official languages; 15 multilingual LLMs evaluated
- **Code/Data:** https://github.com/ChadiHelwe/navigating_the_political_compass
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 95. Nicer Than Humans: How Do Large Language Models Behave in the Prisoner's Dilemma?

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2406.13605](https://arxiv.org/abs/2406.13605)
- **Dataset Size:** Iterated Prisoner's Dilemma simulations with 100 rounds per game; systematic prompting with fixed/variable parts; adversaries at varying hostility levels
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 96. Normative Evaluation of LLMs with Everyday Moral Dilemmas (Sachdeva et al., FAccT 2025)

- **Authors:** Pranav Sachdeva, Tom van Nuenen
- **Year:** 2025
- **Venue:** FAccT 2025
- **arXiv:** [2501.18081](https://arxiv.org/abs/2501.18081)
- **DOI:** 10.1145/3715275.3732044
- **Dataset Size:** 10,000+ posts from Reddit's "Am I The Asshole" (AITA) subreddit; real-world everyday moral dilemmas with community judgments
- **Code/Data:** https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3, Agent 17, Agent 19

---

### 97. On the Convergence of Moral Self-Correction in LLMs

- **Authors:** Guangliang Liu et al.
- **Year:** 2025
- **Venue:** AACL-IJCNLP 2025
- **arXiv:** [2510.07290](https://arxiv.org/abs/2510.07290)
- **Dataset Size:** Multi-choice QA and language generation tasks; uses semantic uncertainty as uncertainty estimator
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 98. OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Interaction Simulation

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2504.13707](https://arxiv.org/abs/2504.13707)
- **Dataset Size:** 50 scenarios across 5 deception types (10 each: telecom fraud, product promotion, personal safety, emotional deception, privacy stealing); multi-turn agent simulation; dual evaluation of internal thou
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 99. PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2601.10532](https://arxiv.org/abs/2601.10532)
- **Dataset Size:** Training data built on EmpatheticDialogues, augmented with GPT-4o scenario expansions and user personas; evaluated on EQ-Bench3
- **Code/Data:** https://github.com/ZhengWwwq/PERM](https://github.com/ZhengWwwq/PERM
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 100. PERSONA (Pluralistic Alignment Testbed)

- **Authors:** Louis Castricato et al.
- **Year:** 2025
- **Venue:** COLING 2025
- **arXiv:** [2407.17387](https://arxiv.org/abs/2407.17387)
- **Dataset Size:** Size: 1,586 synthetic personas; 3,868 prompts; 317,200 feedback pairs
- **Code/Data:** https://huggingface.co/papers/2407.17387
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 101. PKU-SafeRLHF

- **Authors:** Jiaming Ji et al.
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2406.15513](https://arxiv.org/abs/2406.15513)
- **Dataset Size:** 44.6K refined prompts
- **Code/Data:** https://github.com/PKU-Alignment/safe-rlhf; https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 102. PalmX 2025 -- First Shared Task on Benchmarking LLMs on Arabic and Islamic Culture

- **Authors:** Authors
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2509.02550](https://arxiv.org/abs/2509.02550)
- **Dataset Size:** 600 MCQ training pairs
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 103. PersuSafety: LLM Can be a Dangerous Persuader

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.10430](https://arxiv.org/abs/2504.10430)
- **Dataset Size:** 6 unethical persuasion topics x 15 unethical strategies; three-stage framework (scene creation, conversation simulation, safety assessment); multi-turn conversation format
- **Code/Data:** https://github.com/PLUM-Lab/PersuSafety
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 104. Persuade Me if You Can (PMIYC): A Framework for Evaluating Persuasion Effectiveness and Susceptibility

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2503.01829](https://arxiv.org/abs/2503.01829)
- **Dataset Size:** Automated multi-turn conversation framework between Persuader and Persuadee agents; subjective and misinformation scenario types
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 105. PersuasionBench & PersuasionArena: Measuring and Improving Persuasiveness of Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2410.02653](https://arxiv.org/abs/2410.02653)
- **Dataset Size:** ~1.57 million transsuasion pairs from 180 million tweets; 2,187 blog posts for engagement evaluation; multiple task types (simulation, generation, transsuasion)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 106. Playing Repeated Games with Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2305.16867](https://arxiv.org/abs/2305.16867)
- **DOI:** 10.1038/s41562-025-02172-y
- **Dataset Size:** Finitely repeated 2x2 games; LLM vs LLM, LLM vs human-like strategies, LLM vs actual human players; multiple game types
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 107. PoliCon

- **Authors:** Authors
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.19558](https://arxiv.org/abs/2505.19558)
- **Dataset Size:** 2,225 high-quality deliberation records from European Parliament over 13 years (2009-2022); tasks vary by political issues, goals, parties, and power structures
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 108. PrinciplismQA: Towards Assessing Medical Ethics from Knowledge to Practice

- **Authors:** Hong, C., Wu, M., Xiao, Q., Wang, Y., Wan, X., Yu, G., Wang, B., & Hu, Y
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2508.05132](https://arxiv.org/abs/2508.05132)
- **Dataset Size:** PrinciplismQA benchmark: 3,648 questions total
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6, Agent 14

---

### 109. QIAS 2025 -- Shared Task on Islamic Inheritance Reasoning and Knowledge Assessment

- **Authors:** Authors
- **Year:** 2025
- **Venue:** Unknown
- **Dataset Size:** Subtask 1: 22,000 examples total (20,000 train / 1,000 val / 1,000 test)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 110. Randomness, Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2503.08688](https://arxiv.org/abs/2503.08688)
- **DOI:** 10.1145/3715275.3732147
- **Dataset Size:** Systematic robustness testing of survey-based cultural alignment evaluations; tests stability, extrapolability, and steerability across multiple dimensions
- **Code/Data:** https://github.com/ariba-k/llm-cultural-alignment-evaluation
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3

---

### 111. Robustness of Large Language Models in Moral Judgements

- **Authors:** Oh, S. & Demberg, V
- **Year:** 2025
- **Venue:** Unknown
- **DOI:** 10.1098/rsos.241229
- **Dataset Size:** Moral Machine vignettes with systematic prompt variations
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6, Agent 19

---

### 112. RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.25897](https://arxiv.org/abs/2509.25897)
- **Dataset Size:** 13K+ realistic role conflict scenarios across 65 roles; three-stage generation pipeline; systematically varying social expectations and urgency levels
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15, Agent 1

---

### 113. S-Eval

- **Authors:** Xiaohan Yuan et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2405.14191](https://arxiv.org/abs/2405.14191)
- **Dataset Size:** 220,000 evaluation prompts total
- **Code/Data:** https://github.com/IS2Lab/S-Eval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 114. SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2509.16437](https://arxiv.org/abs/2509.16437)
- **Dataset Size:** 695 conversations from 109 participants; 672 fully anonymized conversations with per-turn empathy annotations; 5-level empathy scale; LLM-based classifier achieves Spearman rho=0.369
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 115. SI-Bench: Benchmarking Social Intelligence of Large Language Models in Human-to-Human Conversations

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2510.23182](https://arxiv.org/abs/2510.23182)
- **Dataset Size:** 2,221 authentic multi-turn dialogues from social networking platform; 312 manually annotated dialogues across 8 models; Chinese language; anonymized
- **Code/Data:** https://github.com/SI-Bench/SI-Bench.git](https://github.com/SI-Bench/SI-Bench.git
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15, Agent 1

---

### 116. SORRY-Bench -- Systematically Evaluating LLM Safety Refusal

- **Authors:** Xie, T., et al
- **Year:** 2025
- **Venue:** ICLR 2025
- **arXiv:** [2406.14598](https://arxiv.org/abs/2406.14598)
- **Dataset Size:** 440 class-balanced unsafe instructions (base set)
- **Code/Data:** https://github.com/SORRY-Bench/sorry-bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 16

---

### 117. SPARC: Evaluating LLMs in Open-Source Games (Strategic Program Analysis for Reciprocal Cooperation)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** NeurIPS 2025
- **arXiv:** [2512.00371](https://arxiv.org/abs/2512.00371)
- **Dataset Size:** 239 IPD strategies from the Axelrod Python library; classification task (cooperative vs non-cooperative); includes masked and obfuscated variants
- **Code/Data:** https://github.com/Axelrod-Python/Axelrod
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 118. SPICA (Scenarios for Pluralistic In-Context Alignment)

- **Authors:** Quan Ze Chen, Kevin Feng, Chan Young Park, Amy X. Zhang
- **Year:** 2025
- **Venue:** ACL 2025
- **Dataset Size:** Size: Evaluation with n=544 participants (4 demographic groups) + n=120 end-to-end
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 119. SYNTHEMPATHY: A Scalable Empathy Corpus Generated Using LLMs Without Any Crowdsourcing

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2502.17857](https://arxiv.org/abs/2502.17857)
- **Dataset Size:** 105,000 empathetic responses to real-life situations; fully LLM-generated without crowdsourcing; grounded in four therapeutic styles
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 120. SafeToolBench

- **Authors:** Hongfei Xia, Hongru Wang, Zeming Liu, Qian Yu, Yuhang Guo, Haifeng Wang
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2509.07315](https://arxiv.org/abs/2509.07315)
- **Dataset Size:** 16 everyday domains
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16

---

### 121. SafetyAnalyst

- **Authors:** Jing-Jing Li et al.
- **Year:** 2025
- **Venue:** ICML 2025
- **arXiv:** [2410.16665](https://arxiv.org/abs/2410.16665)
- **Dataset Size:** 18.5 million harm-benefit features generated by frontier LLMs on 19K prompts
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 16

---

### 122. SafetyAnalyst: Interpretable, Transparent, and Steerable Safety Moderation for AI Behavior

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ICML 2025
- **Dataset Size:** See report
- **Code/Data:** https://github.com/jl3676/SafetyAnalyst
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8

---

### 123. Saudi-Alignment Benchmark -- Assessing LLMs Alignment with Saudi Cultural and Ethical Norms

- **Authors:** Authors
- **Year:** 2025
- **Venue:** Unknown
- **Dataset Size:** Questions across Saudi cultural, ethical, and domain knowledge categories
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 9-11

---

### 124. SocialEval: Evaluating Social Intelligence of Large Language Models

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2506.00900](https://arxiv.org/abs/2506.00900)
- **Dataset Size:** Script-based bilingual benchmark; narrative scripts structured as world trees with plot lines; manually crafted scenarios
- **Code/Data:** https://github.com/thu-coai/SocialEval](https://github.com/thu-coai/SocialEval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 125. SocialHarmBench

- **Authors:** Punya Syon Pandey, Hai Son Le, Devansh Bhardwaj, Rada Mihalcea, Zhijing Jin
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2510.04891](https://arxiv.org/abs/2510.04891)
- **Dataset Size:** 585 prompts across 7 sociopolitical categories, covering 34 countries
- **Code/Data:** https://huggingface.co/datasets/psyonp/SocialHarmBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 126. Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework

- **Authors:** Mohna Chakraborty, Lu Wang, David Jurgens
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2506.14948](https://arxiv.org/abs/2506.14948)
- **Dataset Size:** See report
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 19

---

### 127. SycEval: Evaluating LLM Sycophancy

- **Authors:** Aaron Fanous et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2502.08177](https://arxiv.org/abs/2502.08177)
- **DOI:** 10.1609/aies.v8i1.36598
- **Dataset Size:** Evaluation framework using AMPS (mathematics) and MedQuad (medical advice) datasets; multi-domain sycophancy probing
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3, Agent 17

---

### 128. The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in LLMs with a Multi-Framework Approach

- **Authors:** Coleman, C., Neuman, W.R., Dasdan, A., Ali, S., & Shah, M
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2504.19255](https://arxiv.org/abs/2504.19255)
- **DOI:** 10.48550/arXiv.2504.19255
- **Dataset Size:** Dual-protocol approach: direct self-description questioning + response analysis to established ethical dilemmas
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6, Agent 19

---

### 129. The Moral Consistency Pipeline (MoCoP)

- **Authors:** Saeid Jamshidi et al.
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2512.03026](https://arxiv.org/abs/2512.03026)
- **Dataset Size:** Dataset-free, closed-loop framework; autonomously generates, evaluates, and refines ethical scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 130. The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and LLMs

- **Authors:** Russo, G., Nozza, D., Rottger, P., & Hovy, D
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2507.17216](https://arxiv.org/abs/2507.17216)
- **Dataset Size:** Moral Dilemma Dataset: 1,618 real-world moral dilemmas
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 6, Agent 19, Agent 1

---

### 131. The Staircase of Ethics (Multi-step Moral Dilemmas)

- **Authors:** Ya Wu et al.
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2505.18154](https://arxiv.org/abs/2505.18154)
- **Dataset Size:** 3,302 five-stage moral dilemmas (Multi-step Moral Dilemmas / MMDs dataset); each dilemma contains 5 progressive stages with pairwise value comparisons
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19, Agent 1

---

### 132. TrolleyBench

- **Authors:** Zhu, A
- **Year:** 2025
- **Venue:** NeurIPS 2025
- **Dataset Size:** Format: Yes/no moral judgment questions with follow-up probes for consistency
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 5

---

### 133. TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs

- **Authors:** [Authors]
- **Year:** 2025
- **Venue:** NeurIPS 2025
- **Dataset Size:** Trolley-problem-style moral dilemma scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 6

---

### 134. Understanding Gen Alpha's Digital Language: Evaluation of LLM Safety Systems for Content Moderation

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2505.10588](https://arxiv.org/abs/2505.10588)
- **DOI:** 10.1145/3715275.3732184
- **Dataset Size:** 100 recent Gen Alpha expressions from gaming platforms, social media, and video content; first-of-its-kind dataset
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 135. UniMoral (ACL 2025 Best Resource Paper)

- **Authors:** Shivani Kumar, David Jurgens
- **Year:** 2025
- **Venue:** ACL 2025
- **Dataset Size:** Size: 8,784 instances
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 136. VITAL (Pluralistic Alignment in Healthcare)

- **Authors:** Anudeex Shetty, Amin Beheshti, Mark Dras, Usman Naseem
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2502.13775](https://arxiv.org/abs/2502.13775)
- **Dataset Size:** Size: 13,100 value-laden situations + 5,400 multiple-choice questions
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2, Agent 1

---

### 137. Value Compass Benchmarks

- **Authors:** Jing Yao et al.
- **Year:** 2025
- **Venue:** ACL 2025
- **DOI:** 10.18653/v1/2025.acl-demo.64
- **Dataset Size:** Size: Dynamic/self-evolving platform (27 value dimensions x 33 LLMs)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 138. Value Portrait

- **Authors:** Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2505.01015](https://arxiv.org/abs/2505.01015)
- **Dataset Size:** Psychometrically validated items with human-subject correlation data; evaluates 10 Schwartz value dimensions
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19, Agent 1

---

### 139. ValueActionLens (Mind the Value-Action Gap)

- **Authors:** Hua Shen, Nicholas Clark, Tanushree Mitra
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** [2501.15463](https://arxiv.org/abs/2501.15463)
- **Dataset Size:** VIA (Value-Informed Dataset) containing 14,800 value-informed actions spanning 12 cultures and 11 social topics; 132 scenarios
- **Code/Data:** https://github.com/huashen218/value_action_gap
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19

---

### 140. ValueCompass: A Framework for Measuring Contextual Value Alignment Between Humans and LLMs

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** ACL 2025
- **arXiv:** [2409.09586](https://arxiv.org/abs/2409.09586)
- **Dataset Size:** Evaluations across 4 real-world scenarios (collaborative writing, education, public sectors, healthcare); 28 contexts from 4 topics and 7 countries (US, UK, India, Germany, France, Canada, Australia);
- **Code/Data:** https://github.com/huashen218/value_action_gap
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3

---

### 141. When Ethics and Payoffs Diverge: LLM Agents in Morally Charged Social Dilemmas (MoralSim)

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** [2505.19212](https://arxiv.org/abs/2505.19212)
- **Dataset Size:** Prisoner's Dilemma and Public Goods Game with 3 distinct moral framings; multi-round evaluations; morally-aligned action rate metrics (7.9%-76.3% range across models)
- **Code/Data:** https://github.com/sbackmann/moralsim
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 142. Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma

- **Authors:** Unknown
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2501.16173](https://arxiv.org/abs/2501.16173)
- **Dataset Size:** LLM-generated IPD strategies; evolutionary simulation of agent populations with aggressive/cooperative/neutral dispositions
- **Code/Data:** https://github.com/willis-richard/evollm
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 143. ALI-Agent -- Assessing LLMs' Alignment with Human Values via Agent-based Evaluation

- **Authors:** Zheng, S., Wang, Z., et al
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2405.14125](https://arxiv.org/abs/2405.14125)
- **Dataset Size:** Tests across three aspects of human values: stereotypes (DecodingTrust, CrowS-Pairs), morality (ETHICS, Social Chemistry 101), and legality (Singapore RTSR, AdvBench)
- **Code/Data:** https://github.com/SophieZheng998/ALI-Agent
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4

---

### 144. Agent-SafetyBench: Evaluating the Safety of LLM Agents

- **Authors:** Zhexin Zhang et al.
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2412.14470](https://arxiv.org/abs/2412.14470)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/thu-coai/Agent-SafetyBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 16

---

### 145. BELLS: A Framework Towards Future Proof Benchmarks for the Evaluation of LLM Safeguards

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv:** [2406.01364](https://arxiv.org/abs/2406.01364)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/CentreSecuriteIA/BELLS
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8

---

### 146. CHiSafetyBench -- A Chinese Hierarchical Safety Benchmark for LLMs

- **Authors:** Zhang, J. et al
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2406.10311](https://arxiv.org/abs/2406.10311)
- **Dataset Size:** 1,861 multiple-choice questions
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 147. CLAVE / ValEval

- **Authors:** Yao, J., Yi, X., & Xie, X
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2407.10725](https://arxiv.org/abs/2407.10725)
- **Dataset Size:** Size: 13,000+ (text, value, label) tuples
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 5

---

### 148. CMoralEval

- **Authors:** Linhao Yu et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **DOI:** 10.18653/v1/2024.findings-acl.703
- **Dataset Size:** Size: 30,388 instances total (14,964 explicit moral scenarios + 15,424 moral dilemma scenarios)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 149. COMPL-AI (EU AI Act Compliance)

- **Authors:** Philipp Guldimann et al.
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2410.07959](https://arxiv.org/abs/2410.07959)
- **Dataset Size:** Comprehensive benchmarking suite aggregating state-of-the-art LLM benchmarks
- **Code/Data:** https://github.com/compl-ai/compl-ai](https://github.com/compl-ai/compl-ai
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 150. Chinese SafetyQA -- A Safety Short-form Factuality Benchmark

- **Authors:** Tian, Y. et al
- **Year:** 2024
- **Venue:** ACL 2025
- **arXiv:** [2412.15265](https://arxiv.org/abs/2412.15265)
- **Dataset Size:** 2,000+ high-quality safety examples
- **Code/Data:** https://github.com/OpenStellarTeam/ChineseSafetyQA
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 151. ChineseSafe -- A Chinese Benchmark for Evaluating Safety in LLMs

- **Authors:** Zhang, Y., Gao, Y., et al
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2410.18491](https://arxiv.org/abs/2410.18491)
- **Dataset Size:** 205,034 examples (very large-scale)
- **Code/Data:** https://huggingface.co/papers/2410.18491
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 152. CoSafe

- **Authors:** Erxin Yu, Jing Li, Ming Liao, Siqi Wang, Gao Zuchen, Fei Mi, Lanqing Hong
- **Year:** 2024
- **Venue:** EMNLP 2024
- **Dataset Size:** 1,400 questions across 14 categories
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 153. Collective Constitutional AI: Aligning a Language Model with Public Input

- **Authors:** Saffron Huang et al.
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2406.07814](https://arxiv.org/abs/2406.07814)
- **DOI:** 10.1145/3630106.3658979
- **Dataset Size:** 275 public statements sourced via Polis platform (after moderation); constitutions derived from public deliberation; evaluated on BBQ (bias), OpinionQA (political ideology), MMLU, GSM8K
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3, Agent 16

---

### 154. Conscience Conflict: Evaluating Language Models' Moral Understanding

- **Authors:** Authors not fully specified in search results
- **Year:** 2024
- **Venue:** Unknown
- **Dataset Size:** 6 human-authored, high-stakes moral dilemmas; each with 3 mutually exclusive decisions requiring both choice and free-text justification
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 155. Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2309.17234](https://arxiv.org/abs/2309.17234)
- **Dataset Size:** Multi-agent, multi-issue, semantically rich negotiation games; tunable difficulty; cooperative/greedy/malicious agent variants; game transcripts released
- **Code/Data:** https://github.com/S-Abdelnabi/LLM-Deliberation
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 156. Cross-Linguistic Moral Preferences in LLMs -- Evidence from Distributive Justice Scenarios and Domain Persona Interventions

- **Authors:** [Authors not fully retrieved]
- **Year:** 2024
- **Venue:** Unknown
- **Dataset Size:** Size: 1,201,200 observations across ten professional domains
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 157. DeNEVIL / MoralPrompt

- **Authors:** Duan, S., Yi, X., Zhang, P., Lu, T., Xie, X., & Gu, N
- **Year:** 2024
- **Venue:** ICLR 2024
- **arXiv:** [2310.11053](https://arxiv.org/abs/2310.11053)
- **Dataset Size:** Size: 2,397 prompts covering 500+ value principles
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 5

---

### 158. Decoding Multilingual Moral Preferences -- Unveiling LLM's Biases Through the Moral Machine Experiment

- **Authors:** Vida, K., Damken, F., & Lauscher, A
- **Year:** 2024
- **Venue:** AIES 2024
- **arXiv:** [2407.15184](https://arxiv.org/abs/2407.15184)
- **Dataset Size:** Size: 6,500 moral dilemma scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 159. Decolonial AI Alignment -- Openness, Visesa-Dharma, and Including Excluded Knowledges

- **Authors:** Varshney, K. R
- **Year:** 2024
- **Venue:** AIES 2024
- **arXiv:** [2309.05030](https://arxiv.org/abs/2309.05030)
- **DOI:** 10.5555/3716662.3716790
- **Dataset Size:** Conceptual framework paper rather than benchmark; proposes methodology for creating culturally-grounded alignment datasets
- **Code/Data:** None listed
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 9-11, Agent 12-13

---

### 160. Does Cross-Cultural Alignment Change the Commonsense Morality of Language Models?

- **Authors:** Jinnai, Y
- **Year:** 2024
- **Venue:** ACL 2024
- **Dataset Size:** Datasets used: JCommonsenseMorality (Japanese), ETHICS (English)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 12-13

---

### 161. EAI -- Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas

- **Authors:** Mozikov, M., et al
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **Dataset Size:** Strategic game scenarios (bargaining, repeated games)
- **Code/Data:** https://github.com/AIRI-Institute/EAI-Framework
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 18

---

### 162. Eagle (Ethical Dataset Given from Real Interactions)

- **Authors:** Kaneko, M., Bollegala, D., & Baldwin, T
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2402.14258](https://arxiv.org/abs/2402.14258)
- **Dataset Size:** Size: ~4,461 instances total: 1,004 social bias, 831 opinion bias, 1,078 toxic language, 1,548 morality
- **Code/Data:** https://huggingface.co/datasets/MasahiroKaneko/eagle
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5, Agent 17

---

### 163. Edu-Values -- Evaluating Chinese Education Values of LLMs

- **Authors:** Authors
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2409.12739](https://arxiv.org/abs/2409.12739)
- **DOI:** 10.1145/3701716.3715518
- **Dataset Size:** 1,418 questions across 5 question types
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 164. EmoBench: Evaluating the Emotional Intelligence of Large Language Models

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2402.12071](https://arxiv.org/abs/2402.12071)
- **Dataset Size:** 400 hand-crafted questions in English and Chinese; structured into EU (recognizing emotions and causes in complex scenarios) and EA (recommending effective emotional responses in dilemmas); multiple-c
- **Code/Data:** https://github.com/Sahandfer/EmoBench](https://github.com/Sahandfer/EmoBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 165. EmotionBench (Apathetic or Empathetic?): Evaluating LLMs' Emotional Alignments with Humans

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2308.03656](https://arxiv.org/abs/2308.03656)
- **Dataset Size:** 428 situations across 36 factors eliciting 8 emotions; human baseline from 1,266 annotators across different ethnic groups, genders, regions, and age groups
- **Code/Data:** https://github.com/CUHK-ARISE/EmotionBench](https://github.com/CUHK-ARISE/EmotionBench; https://huggingface.co/datasets/CUHK-ARISE/EmotionBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 166. EmotionQueen: A Benchmark for Evaluating Empathy of Large Language Models

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2409.13359](https://arxiv.org/abs/2409.13359)
- **Dataset Size:** 10,000 user statements across 5 categories; 4 tasks (Key Event Recognition, Mixed Event Recognition, Implicit Emotional Recognition, Intention Recognition); two metrics: PASS rate and WIN rate
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15

---

### 167. EmpathicStories++: A Multimodal Dataset for Empathy towards Personal Experiences

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2405.15708](https://arxiv.org/abs/2405.15708)
- **Dataset Size:** 53 hours of video, audio, and text data; 41 participants; 269 sessions across month-long deployment; self-reported empathy ratings; multimodal (video/audio/text)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 168. Ethical Reasoning and Moral Value Alignment (Multilingual)

- **Authors:** Utkarsh Agarwal, Kumar Tanmay, Aditi Khandelwal, Monojit Choudhury
- **Year:** 2024
- **Venue:** COLING 2024
- **Dataset Size:** Size: Ethical dilemmas and policies across three normative ethics branches
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 169. Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language We Prompt Them In

- **Authors:** Agarwal, U., Tanmay, K., Khandelwal, A., & Choudhury, M
- **Year:** 2024
- **Venue:** COLING 2024
- **arXiv:** [2404.18460](https://arxiv.org/abs/2404.18460)
- **Dataset Size:** Format: Ethical dilemma prompts and policy scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 170. Evaluating Moral Beliefs (Pluralistic Framework)

- **Authors:** Xuelin Liu, Yanfei Zhu, Shucheng Zhu, Pengyuan Liu, Ying Liu, Dong Yu
- **Year:** 2024
- **Venue:** EMNLP 2024
- **DOI:** 10.18653/v1/2024.findings-emnlp.272
- **Dataset Size:** Size: 472 moral choice scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 171. Evaluating Moral Beliefs across LLMs through a Pluralistic Framework

- **Authors:** Xuelin Liu, Yanfei Zhu, Shucheng Zhu, Pengyuan Liu, Ying Liu, Dong Yu
- **Year:** 2024
- **Venue:** EMNLP 2024
- **arXiv:** [2411.03665](https://arxiv.org/abs/2411.03665)
- **Dataset Size:** 472 moral choice scenarios in Chinese derived from moral words; three evaluation modules
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 172. Extended Japanese Commonsense Morality Dataset (eJCM)

- **Authors:** Ohashi, T., Nakagawa, T., & Iyatomi, H
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2410.09564](https://arxiv.org/abs/2410.09564)
- **DOI:** 10.1145/3627673.3679924
- **Dataset Size:** Size: 31,184 sentences (expanded from 13,975 original JCommonsenseMorality sentences)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 173. FABLE (Fairness and Bias in LLM Evaluation)

- **Authors:** KFUPM Research Team
- **Year:** 2024
- **Venue:** Unknown
- **Dataset Size:** 156 curated prompts across 4 categories; automated evaluation via toxicity/hate speech classifiers
- **Code/Data:** https://github.com/BRAIN-Lab-AI/FABLE-Fairness-and-Bias-in-LLM-Evaluation
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 174. Fake Alignment (FINE Framework)

- **Authors:** Yixu Wang et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **Dataset Size:** Size: Comparative benchmark with MC and open-ended questions
- **Code/Data:** https://github.com/AIFlames/Fake-Alignment
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 175. Flames

- **Authors:** Kexin Huang et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **Dataset Size:** Size: Adversarial prompts and annotated responses (details in full paper)
- **Code/Data:** https://github.com/AIFlames/Flames
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 176. GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2402.12348](https://arxiv.org/abs/2402.12348)
- **Dataset Size:** 10 game environments (Tic-Tac-Toe, Connect-4, Breakthrough, Nim, Hex, Liar's Dice, Negotiation, Pig, Iterated Prisoner's Dilemma, Blind Auction) built on OpenSpiel; text-based interaction format
- **Code/Data:** https://github.com/jinhaoduan/GTBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 177. Gaps in the Safety Evaluation of Generative AI

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** Unknown
- **DOI:** 10.1609/aies.v7i1.31717
- **Dataset Size:** Comprehensive review and taxonomy of all available safety evaluations; maps gaps across evaluation layers
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 178. GenMO (Gender-bias in Morality Opinions)

- **Authors:** Divij Bajaj, Yuanyuan Lei, Jonathan Tong, Ruihong Huang
- **Year:** 2024
- **Venue:** EMNLP 2024
- **DOI:** 10.18653/v1/2024.findings-emnlp.928
- **Dataset Size:** Size: Parallel short stories (exact count in full paper)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 179. GuardBench

- **Authors:** GuardBench Team
- **Year:** 2024
- **Venue:** EMNLP 2024
- **Dataset Size:** 40 safety evaluation datasets aggregated
- **Code/Data:** https://github.com/AmenRa/GuardBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 180. HarmBench

- **Authors:** Mazeika et al.
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2402.04249](https://arxiv.org/abs/2402.04249)
- **Dataset Size:** Size: Comprehensive behavior set across 7 categories
- **Code/Data:** https://github.com/centerforaisafety/HarmBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 181. Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters

- **Authors:** Yujin Potter, Shiyang Lai, Junsol Kim, James Evans, Dawn Song
- **Year:** 2024
- **Venue:** EMNLP 2024
- **arXiv:** [2410.24190](https://arxiv.org/abs/2410.24190)
- **Dataset Size:** Voting simulation across 18 LLMs; human experiment with 935 U.S. registered voters interacting with LLMs over 5 exchanges
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 182. How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas

- **Authors:** So, E
- **Year:** 2024
- **Venue:** Unknown
- **Dataset Size:** Type: Theoretical/proposal paper with practical application demonstration (psychology AI chatbots)
- **Code/Data:** None listed
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 12-13

---

### 183. IndiBias -- Benchmark Dataset for Social Biases in Indian Context

- **Authors:** Sahoo, N. et al
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2403.20147](https://arxiv.org/abs/2403.20147)
- **Dataset Size:** 800 sentence pairs + 300 tuples for intersectional bias
- **Code/Data:** https://github.com/sahoonihar/IndiBias
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 184. Indian-BhED -- A Dataset for Measuring India-Centric Biases in LLMs

- **Authors:** Khandelwal, V. & Tonneau, M. et al
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2309.08573](https://arxiv.org/abs/2309.08573)
- **DOI:** 10.1145/3677525.3678666
- **Dataset Size:** Stereotypical and anti-stereotypical sentence pairs
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 9-11

---

### 185. Intuitions of Compromise -- Utilitarianism vs. Contractualism

- **Authors:** Moore, J
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2410.05496](https://arxiv.org/abs/2410.05496)
- **Dataset Size:** Controlled social decision-making scenarios
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 4

---

### 186. Investigating Cultural Alignment of LLMs

- **Authors:** Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, Mona Diab
- **Year:** 2024
- **Venue:** ACL 2024
- **Dataset Size:** Size: Replicated sociological surveys across regions
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 187. IrokoBench -- A Benchmark for African Languages in the Age of LLMs

- **Authors:** Adelani, D. et al
- **Year:** 2024
- **Venue:** ACL 2025
- **arXiv:** [2406.03368](https://arxiv.org/abs/2406.03368)
- **Dataset Size:** 17 typologically-diverse low-resource African languages
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 188. JAILJUDGE

- **Authors:** Fan Liu, Yue Feng, Zhao Xu, Lixin Su, Xinyu Ma, Dawei Yin, Hao Liu
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2410.12855](https://arxiv.org/abs/2410.12855)
- **Dataset Size:** 35K+ instruction-tuning data with reasoning explainability
- **Code/Data:** https://github.com/usail-hkust/Jailjudge; https://huggingface.co/usail-hkust/JailJudge-guard
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 189. JBBQ (Japanese Bias Benchmark for Question Answering)

- **Authors:** Hitomi Yanaka et al
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2406.02050](https://arxiv.org/abs/2406.02050)
- **Dataset Size:** 50,856 question pairs total (age: 28,176; disability: 8,064; gender: 3,912; physical: 7,536; sexual: 3,168); JBBQ-Lite: 912 question pairs
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 190. JailbreakBench -- An Open Robustness Benchmark

- **Authors:** Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2404.01318](https://arxiv.org/abs/2404.01318)
- **Dataset Size:** JBB-Behaviors: 100 distinct misuse behaviors across 10 categories aligned with OpenAI usage policies
- **Code/Data:** https://github.com/JailbreakBench/jailbreakbench; https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 16

---

### 191. KorNAT

- **Authors:** Jiyoung Lee et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **DOI:** 10.18653/v1/2024.findings-acl.666
- **Dataset Size:** Size: 10,000 multiple-choice questions (4,000 on social values + 6,000 on common knowledge)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2

---

### 192. LLM Voting: Human Choices and AI Collective Decision-Making

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2402.01766](https://arxiv.org/abs/2402.01766)
- **DOI:** 10.1609/aies.v7i1.31758
- **Dataset Size:** Dataset from human voting experiments used as baseline; LLM agents replicate voting conditions
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 193. MAgIC: Investigation of Large Language Model Powered Multi-Agent in Cognition, Adaptability, Rationality and Collaboration

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** EMNLP 2024
- **arXiv:** [2311.08562](https://arxiv.org/abs/2311.08562)
- **Dataset Size:** Social deduction games (Chameleon, Undercover) + game theory scenarios (Cost Sharing, Multi-player Prisoner's Dilemma, Public Good); probabilistic graphical modeling enhancement
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 194. MULTITP -- Language Model Alignment in Multilingual Trolley Problems

- **Authors:** Jin, Z., Levine, S., Mihalcea, R., et al
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2407.02273](https://arxiv.org/abs/2407.02273)
- **Dataset Size:** 97,520 trolley problem vignettes
- **Code/Data:** https://github.com/causalNLP/moralmachine
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 6

---

### 195. Measuring Bargaining Abilities of LLMs: A Benchmark and A Buyer-Enhancement Method

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2402.15813](https://arxiv.org/abs/2402.15813)
- **Dataset Size:** AmazonHistoryPrice dataset -- 930 popular products across 18 categories with real price data (lowest/highest/current/list price, descriptions, features); multi-round bargaining format
- **Code/Data:** https://github.com/TianXiaSJTU/AmazonPriceHistory
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 196. Measuring Political Bias in LLMs: What Is Said and How It Is Said

- **Authors:** Yejin Bang, Delong Chen, Nayeon Lee, Pascale Fung
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2403.18932](https://arxiv.org/abs/2403.18932)
- **Dataset Size:** Framework-based evaluation across multiple political topics; evaluates both content and style dimensions
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 197. Measuring What Matters -- Construct Validity in LLM Benchmarks

- **Authors:** [Authors]
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **Dataset Size:** Meta-analysis of existing LLM benchmarks
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 4

---

### 198. MedSafetyBench

- **Authors:** Tessa Han, Aounon Kumar, Chirag Agarwal, and Himabindu Lakkaraju
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2403.03744](https://arxiv.org/abs/2403.03744)
- **Dataset Size:** 1,800 medical safety demonstrations
- **Code/Data:** https://github.com/AI4LIFE-GROUP/med-safety-bench](https://github.com/AI4LIFE-GROUP/med-safety-bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 199. Moral Foundations of Large Language Models

- **Authors:** Marwa Abdulhai et al.
- **Year:** 2024
- **Venue:** EMNLP 2024
- **DOI:** 10.18653/v1/2024.emnlp-main.982
- **Dataset Size:** Survey-based and adversarial prompt evaluation; measures consistency of moral biases across contexts
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 200. Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2411.11731](https://arxiv.org/abs/2411.11731)
- **Dataset Size:** Morally ambiguous scenarios; two-experiment design (susceptibility to ambiguity + alignment with predefined ethical frameworks); multi-turn persuader-persuadee conversations
- **Code/Data:** https://github.com/acyhuang/moral-persuasion
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 201. MoralBench

- **Authors:** Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, and Yongfeng Zhang
- **Year:** 2024
- **Venue:** SIGKDD
- **arXiv:** [2406.04428](https://arxiv.org/abs/2406.04428)
- **DOI:** 10.1145/3748239.3748246
- **Dataset Size:** Three datasets:
- **Code/Data:** https://github.com/agiresearch/MoralBench](https://github.com/agiresearch/MoralBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14, Agent 15, Agent 16, Agent 19

---

### 202. Multilingual Defining Issues Test

- **Authors:** Aditi Khandelwal, Utkarsh Agarwal, Kumar Tanmay, Monojit Choudhury
- **Year:** 2024
- **Venue:** ACL 2024
- **DOI:** 10.18653/v1/2024.eacl-long.176
- **Dataset Size:** Size: Defining Issues Test scenarios translated into 6 languages
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 203. NegotiationArena: How Well Can LLMs Negotiate?

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv:** [2402.05863](https://arxiv.org/abs/2402.05863)
- **Dataset Size:** 3 scenario types (resource allocation/ultimatum, resource aggregation/trading, buying/selling); 60 negotiations per ordered agent pair; win rate and average payoff metrics
- **Code/Data:** https://github.com/vinid/NegotiationArena
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 18

---

### 204. Norm Inconsistency in LLM Decision-Making

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2405.14812](https://arxiv.org/abs/2405.14812)
- **DOI:** 10.1609/aies.v7i1.31665
- **Dataset Size:** Thousands of Amazon Ring home surveillance video descriptions; annotated for criminal activity, subject skin-tone, gender, and neighborhood demographics
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 205. On The Stability of Moral Preferences: A Problem with Computational Elicitation Methods

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2408.02862](https://arxiv.org/abs/2408.02862)
- **DOI:** 10.1609/aies.v7i1.31626
- **Dataset Size:** Repeated moral preference surveys across 10 sessions in 2 studies; kidney allocation decisions
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 206. On the Pros and Cons of Active Learning for Moral Preference Elicitation

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** AIES 2024
- **arXiv:** [2407.18889](https://arxiv.org/abs/2407.18889)
- **DOI:** 10.1609/aies.v7i1.31673
- **Dataset Size:** Synthetic simulation of moral preferences with varying assumption violations (instability, noise, hypothesis class mismatch)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 3

---

### 207. OpenEval -- Benchmarking Chinese LLMs across Capability, Alignment, and Safety

- **Authors:** Li, C. et al
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2403.12316](https://arxiv.org/abs/2403.12316)
- **Dataset Size:** 35 benchmark datasets total
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 208. PRISM Alignment Dataset

- **Authors:** Kirk, H.R., Vidgen, B., Rottger, P., Hale, S.A
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2404.16019](https://arxiv.org/abs/2404.16019)
- **Dataset Size:** 1,500 diverse participants from 75 countries
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4

---

### 209. Pluralistic Alignment Over Time

- **Authors:** [Authors]
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2411.10654](https://arxiv.org/abs/2411.10654)
- **Dataset Size:** Conceptual framework paper with benchmark proposals
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 4

---

### 210. Political Compass or Spinning Arrow?

- **Authors:** Paul Rottger et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2402.16786](https://arxiv.org/abs/2402.16786)
- **Dataset Size:** Uses the PCT's 62 Likert-scale statements; tested across multiple paraphrase variants, open-ended vs. forced-choice formats
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 17

---

### 211. SALAD-Bench

- **Authors:** Lijun Li et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2402.05044](https://arxiv.org/abs/2402.05044)
- **Dataset Size:** 21K harmful base questions
- **Code/Data:** https://github.com/OpenSafetyLab/SALAD-BENCH
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 212. SG-Bench -- Evaluating LLM Safety Generalization

- **Authors:** Tom, M., et al
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2410.21965](https://arxiv.org/abs/2410.21965)
- **Dataset Size:** Entries sampled from AdvBench, HarmfulQA, BeaverTails, SaladBench
- **Code/Data:** https://github.com/MurrayTom/SG-Bench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4, Agent 16

---

### 213. SaGE (Semantic Graph Entropy) / Moral Consistency Corpus

- **Authors:** Bonagiri, V. K., Vennam, S., Govil, P., Kumaraguru, P., & Gaur, M
- **Year:** 2024
- **Venue:** COLING 2024
- **arXiv:** [2402.13709](https://arxiv.org/abs/2402.13709)
- **Dataset Size:** Size: 50,000 moral questions with LLM responses and Rules of Thumb (Moral Consistency Corpus — MCC)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 5

---

### 214. SaTML LLM CTF Dataset

- **Authors:** Debenedetti et al.
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2406.07954](https://arxiv.org/abs/2406.07954)
- **Dataset Size:** 137,063 multi-turn attack chats
- **Code/Data:** https://huggingface.co/datasets/ethz-spylab/ctf-satml24; https://huggingface.co/datasets/ethz-spylab/ctf-satml24
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 4

---

### 215. SafeAgentBench

- **Authors:** Sheng Yin et al.
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2412.13178](https://arxiv.org/abs/2412.13178)
- **Dataset Size:** 750 tasks
- **Code/Data:** https://github.com/shengyin1224/SafeAgentBench; https://huggingface.co/datasets/safeagentbench/SafeAgentBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 216. SafetyBench: Evaluating the Safety of Large Language Models

- **Authors:** Zhexin Zhang et al.
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2309.07045](https://arxiv.org/abs/2309.07045)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/thu-coai/SafetyBench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 16

---

### 217. Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?

- **Authors:** Richard Ren et al.
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2407.21792](https://arxiv.org/abs/2407.21792)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/centerforaisafety/safetywashing
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 16

---

### 218. Social (Measuring Social Norms of LLMs)

- **Authors:** Ye Yuan, Kexin Tang, Jianhao Shen, Ming Zhang, Chenguang Wang
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2404.02491](https://arxiv.org/abs/2404.02491)
- **Dataset Size:** 12,383 questions covering 402 social norm skills; multiple-choice format aligned with K-12 educational standards
- **Code/Data:** https://github.com/socialnormdataset/socialagent; https://huggingface.co/datasets/socialnormdataset/social
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 219. Synth-Empathy: Towards High-Quality Synthetic Empathy Data

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2407.21669](https://arxiv.org/abs/2407.21669)
- **Dataset Size:** 250K+ empathetic data points generated from EmpatheticDialogues (25K base conversations, 32 emotion labels); three-step pipeline: generation, quality selection, diversity selection
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 220. The Emergence of Strategic Reasoning of Large Language Models

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** [2412.13013](https://arxiv.org/abs/2412.13013)
- **Dataset Size:** 3 classical behavioral economics games; evaluations against human performance benchmarks using hierarchical models of bounded rationality
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 18

---

### 221. The Greatest Good Benchmark (Utilitarian Moral Dilemmas)

- **Authors:** Giovanni Franco Gabriel Marraffini et al.
- **Year:** 2024
- **Venue:** EMNLP 2024
- **arXiv:** [2503.19598](https://arxiv.org/abs/2503.19598)
- **Dataset Size:** Adapted and expanded Oxford Utilitarianism Scale items for LLM evaluation
- **Code/Data:** https://github.com/noehsueh/greatest-good-benchmark
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 19

---

### 222. The Political Preferences of LLMs

- **Authors:** David Rozado
- **Year:** 2024
- **Venue:** Unknown
- **DOI:** 10.1371/journal.pone.0306621
- **Dataset Size:** 11 political orientation tests x 10 trials x 24 LLMs = 2,640 total test administrations; automated test administration and parsing scripts
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 223. Towards Geographic Inclusion in the Evaluation of Text-to-Image Models

- **Authors:** Unknown
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2405.04457](https://arxiv.org/abs/2405.04457)
- **DOI:** 10.1145/3630106.3658927
- **Dataset Size:** 65,000 annotations from people in Africa, Europe, and Southeast Asia; evaluated on GeoDE (40 object classes across 6 regions) and DollarStreet (~200 concept classes across 4 regions)
- **Code/Data:** https://github.com/facebookresearch/DIG-In
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 3

---

### 224. Towards Understanding Sycophancy in Language Models

- **Authors:** Mrinank Sharma et al.
- **Year:** 2024
- **Venue:** ICLR 2024
- **arXiv:** [2310.13548](https://arxiv.org/abs/2310.13548)
- **Dataset Size:** Three evaluation tasks in JSONL format:
- **Code/Data:** https://github.com/meg-tong/sycophancy-eval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 225. TrustLLM

- **Authors:** Huang, Y., Sun, L., Wang, H., Wu, S., Zhang, Q., et al
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv:** [2401.05561](https://arxiv.org/abs/2401.05561)
- **Dataset Size:** Size: 30+ datasets, 18+ subcategories
- **Code/Data:** https://github.com/HowieHwong/TrustLLM
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 226. Unintended Impacts of LLM Alignment on Global Representation

- **Authors:** Michael J. Ryan, William Held, Diyi Yang
- **Year:** 2024
- **Venue:** ACL 2024
- **DOI:** 10.18653/v1/2024.acl-long.853
- **Dataset Size:** Size: Multi-axis evaluation across dialects, languages, global opinions
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 227. Value FULCRA

- **Authors:** Jing Yao, Xiaoyuan Yi, Yifan Gong, Xiting Wang, Xing Xie
- **Year:** 2024
- **Venue:** ACL 2024
- **arXiv:** [2311.10766](https://arxiv.org/abs/2311.10766)
- **DOI:** 10.18653/v1/2024.naacl-long.486
- **Dataset Size:** Size: 20,000 (LLM output, value vector) pairs
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2, Agent 19

---

### 228. Value Kaleidoscope / ValuePrism

- **Authors:** Sorensen et al.
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2309.00779](https://arxiv.org/abs/2309.00779)
- **DOI:** 10.1609/aaai.v38i18.29970
- **Dataset Size:** Size: 218,000 human-written values, rights, and duties linked to 31,000 real-world situations
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 229. WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning

- **Authors:** Nathaniel Li et al.
- **Year:** 2024
- **Venue:** ICML 2024
- **arXiv:** [2403.03218](https://arxiv.org/abs/2403.03218)
- **Dataset Size:** See report
- **Code/Data:** https://github.com/centerforaisafety/wmdp
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 7-8, Agent 16

---

### 230. WalledEval

- **Authors:** Prannaya Gupta et al.
- **Year:** 2024
- **Venue:** EMNLP 2024
- **arXiv:** [2408.03837](https://arxiv.org/abs/2408.03837)
- **Dataset Size:** Size: 35+ safety benchmarks integrated
- **Code/Data:** https://github.com/walledai/walledeval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 2, Agent 16

---

### 231. Whose Morality Do They Speak? Unraveling Cultural Bias in Multilingual Language Models

- **Authors:** Aksoy, M
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2412.18863](https://arxiv.org/abs/2412.18863)
- **Dataset Size:** Format: MFQ-2 questionnaire administered in 8 languages
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 12-13

---

### 232. WildGuard (WildGuardTest)

- **Authors:** Seungju Han et al.
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv:** [2406.18495](https://arxiv.org/abs/2406.18495)
- **Dataset Size:** WildGuardMix (training): 92K labeled examples
- **Code/Data:** https://huggingface.co/allenai/wildguard
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 233. AfroBench -- How Good are LLMs on African Languages?

- **Authors:** Ojo, J. et al
- **Year:** 2023
- **Venue:** arXiv
- **arXiv:** [2311.07978](https://arxiv.org/abs/2311.07978)
- **Dataset Size:** 64 African languages
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 234. BeaverTails

- **Authors:** Ji et al.
- **Year:** 2023
- **Venue:** NeurIPS 2023
- **arXiv:** [2307.04657](https://arxiv.org/abs/2307.04657)
- **Dataset Size:** Size: 333,963 QA pairs with safety meta-labels; 361,903 expert comparison pairs; 700 evaluation prompts
- **Code/Data:** https://github.com/PKU-Alignment/beavertails; https://huggingface.co/datasets/PKU-Alignment/BeaverTails; https://huggingface.co/datasets/PKU-Alignment/BeaverTails-Evaluation
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 235. CValues -- Measuring the Values of Chinese LLMs from Safety to Responsibility

- **Authors:** Xu et al.
- **Year:** 2023
- **Venue:** arXiv
- **arXiv:** [2307.09705](https://arxiv.org/abs/2307.09705)
- **Dataset Size:** Adversarial safety prompts across 10 scenarios (manually collected by professional experts)
- **Code/Data:** None listed
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 9-11

---

### 236. DecodingTrust

- **Authors:** Wang et al.
- **Year:** 2023
- **Venue:** NeurIPS 2023
- **arXiv:** [2306.11698](https://arxiv.org/abs/2306.11698)
- **Dataset Size:** Size: Multi-dimensional benchmark across 8 trust dimensions
- **Code/Data:** https://github.com/AI-secure/DecodingTrust; https://huggingface.co/datasets/AI-Secure/DecodingTrust
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 237. EtiCor: Corpus for Analyzing LLMs for Etiquettes

- **Authors:** Unknown
- **Year:** 2023
- **Venue:** EMNLP 2023
- **arXiv:** [2310.18974](https://arxiv.org/abs/2310.18974)
- **Dataset Size:** Texts about social norms from 5 regions; Etiquette Sensitivity evaluation task
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 15

---

### 238. LegalBench

- **Authors:** Neel Guha, Julian Nyarko, Daniel E. Ho, Christopher Re, Adam Chilton, et al
- **Year:** 2023
- **Venue:** NeurIPS 2023
- **arXiv:** [2308.11462](https://arxiv.org/abs/2308.11462)
- **Dataset Size:** 162 tasks from 40 legal expert contributors
- **Code/Data:** https://github.com/HazyResearch/legalbench](https://github.com/HazyResearch/legalbench; https://huggingface.co/datasets/nguha/legalbench](https://huggingface.co/datasets/nguha/legalbench
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 14

---

### 239. NormBank

- **Authors:** Caleb Ziems, Nhi Dwivedi-Yu, Yi-Chia Wang, Alon Halevy, Diyi Yang
- **Year:** 2023
- **Venue:** ACL 2023
- **arXiv:** [2305.17008](https://arxiv.org/abs/2305.17008)
- **Dataset Size:** 155K situational norms; each grounded in sociocultural frames (setting, agent roles, attributes, physical/social/cultural constraints)
- **Code/Data:** https://github.com/SALT-NLP/normbank
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 240. OpinionQA

- **Authors:** Shibani Santurkar et al.
- **Year:** 2023
- **Venue:** ICML 2023
- **arXiv:** [2303.17548](https://arxiv.org/abs/2303.17548)
- **Dataset Size:** 1,498 multiple-choice questions from Pew Research's American Trends Panels; spans science, politics, personal relationships; includes human opinion distributions for 60 demographic groups
- **Code/Data:** https://github.com/tatsu-lab/opinions_qa
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 241. Probing Moral Development through Defining Issues Test (DIT)

- **Authors:** Kumar Tanmay, Aditi Khandelwal, Utkarsh Agarwal, Monojit Choudhury
- **Year:** 2023
- **Venue:** arXiv preprint
- **arXiv:** [2309.13356](https://arxiv.org/abs/2309.13356)
- **Dataset Size:** DIT-based moral dilemmas with importance-ranking protocol adapted for LLMs
- **Code/Data:** https://github.com/agiresearch/MoralBench; https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark; https://github.com/huashen218/value_action_gap; https://github.com/alessioGalatolo/AMAeval; https://github.com/noehsueh/greatest-good-benchmark; https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas; https://github.com/LuanaBulla/Detection-of-Morality-in-Text
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 19

---

### 242. Probing PLMs for Cross-Cultural Values (C3NLP Workshop)

- **Authors:** Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein
- **Year:** 2023
- **Venue:** Unknown
- **Dataset Size:** Size: Probe-based evaluation (details in full paper)
- **Code/Data:** None listed
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 2

---

### 243. BBQ (Bias Benchmark for Question Answering)

- **Authors:** Alicia Parrish et al.
- **Year:** 2022
- **Venue:** ACL 2022
- **arXiv:** [2110.08193](https://arxiv.org/abs/2110.08193)
- **Dataset Size:** ~58,000 multiple-choice questions; ambiguous and disambiguated contexts; 11 JSONL files (one per bias category)
- **Code/Data:** https://github.com/nyu-mll/BBQ; https://huggingface.co/datasets/heegyu/bbq; https://huggingface.co/datasets/walledai/BBQ
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 244. HH-RLHF (Helpful and Harmless RLHF)

- **Authors:** Yuntao Bai et al.
- **Year:** 2022
- **Venue:** arXiv preprint
- **arXiv:** [2204.05862](https://arxiv.org/abs/2204.05862)
- **Dataset Size:** ~170K human preference comparisons total
- **Code/Data:** https://github.com/anthropics/hh-rlhf; https://huggingface.co/datasets/Anthropic/hh-rlhf
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 16

---

### 245. Moral Integrity Corpus (MIC)

- **Authors:** Ziems, C., Yu, J. A., Wang, Y.-C., Halevy, A. Y., & Yang, D
- **Year:** 2022
- **Venue:** ACL 2022
- **arXiv:** [2204.03021](https://arxiv.org/abs/2204.03021)
- **DOI:** 10.18653/v1/2022.acl-long.261
- **Dataset Size:** Size: 38,000 prompt-reply pairs; 99,000 distinct Rules of Thumb; 114,000 annotations
- **Code/Data:** https://github.com/GT-SALT/mic
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 246. ProsocialDialog: A Prosocial Backbone for Conversational Agents

- **Authors:** Hyunwoo Kim et al.
- **Year:** 2022
- **Venue:** EMNLP 2022
- **arXiv:** [2205.12688](https://arxiv.org/abs/2205.12688)
- **Dataset Size:** 58K dialogues; 331K utterances; 160K unique rules-of-thumb (RoTs); 497K dialogue safety labels with free-form rationales; human-AI collaborative framework
- **Code/Data:** https://github.com/skywalker023/prosocial-dialog](https://github.com/skywalker023/prosocial-dialog; https://huggingface.co/datasets/allenai/prosocial-dialog
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15, Agent 17

---

### 247. CrowS-Pairs

- **Authors:** Nikita Nangia, Clara Vania, Rasika Bhalerao, Samuel R. Bowman
- **Year:** 2021
- **Venue:** EMNLP 2020
- **arXiv:** [2010.00133](https://arxiv.org/abs/2010.00133)
- **Dataset Size:** 1,508 sentence pairs (stereotypical vs. anti-stereotypical); crowdsourced
- **Code/Data:** https://github.com/nyu-mll/crows-pairs; https://github.com/EleutherAI/lm-evaluation-harness
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 17

---

### 248. Moral Stories

- **Authors:** Emelin, D., Le Bras, R., Hwang, J. D., Forbes, M., & Choi, Y
- **Year:** 2021
- **Venue:** EMNLP 2021
- **DOI:** 10.18653/v1/2021.emnlp-main.54
- **Dataset Size:** Size: 12,000 structured, branching narratives (7 sentences each)
- **Code/Data:** https://github.com/demelin/moral_stories; https://huggingface.co/datasets/demelin/moral_stories
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 249. Scruples

- **Authors:** Lourie, N., Le Bras, R., & Choi, Y
- **Year:** 2021
- **Venue:** AAAI 2021
- **arXiv:** [2008.09094](https://arxiv.org/abs/2008.09094)
- **Dataset Size:** Size: 32,000 real-life anecdotes with 625,000 ethical judgments
- **Code/Data:** https://github.com/allenai/scruples
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 250. Social Chemistry 101 (SOCIAL-CHEM-101)

- **Authors:** Forbes, M., Hwang, J. D., Shwartz, V., Sap, M., & Choi, Y
- **Year:** 2020
- **Venue:** EMNLP 2020
- **arXiv:** [2011.00620](https://arxiv.org/abs/2011.00620)
- **DOI:** 10.18653/v1/2020.emnlp-main.48
- **Dataset Size:** Size: 292,000 rules-of-thumb; over 4.5 million categorical label annotations
- **Code/Data:** https://github.com/mbforbes/social-chemistry-101
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 5

---

### 251. EmpatheticDialogues: Towards Empathetic Open-domain Conversation Models

- **Authors:** Unknown
- **Year:** 2019
- **Venue:** arXiv
- **arXiv:** [1811.00207](https://arxiv.org/abs/1811.00207)
- **Dataset Size:** 25,000 conversations; 32 emotion labels; grounded in emotional situations; human-to-human dialogues
- **Code/Data:** https://github.com/facebookresearch/EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues; https://huggingface.co/datasets/facebook/empathetic_dialogues
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 15, Agent 1

---

## Agent 1 Papers (Citation Graph Traversal) — 49 Net New

### 252. COMETH: Contextual Organization of Moral Evaluation from Textual Human Inputs

- **Authors:** Morlat, G. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2512.21439](https://arxiv.org/abs/2512.21439)
- **Dataset Size:** 300 scenarios with ternary moral judgments (Blame/Neutral/Support) from 101 participants across six core moral actions
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 253. VAL-Bench: Belief Consistency as a Measure for Value Alignment

- **Authors:** Gupta, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.05465](https://arxiv.org/abs/2510.05465)
- **Dataset Size:** 115K pairs of prompts from Wikipedia eliciting opposing stances on controversial issues
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 254. CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives

- **Authors:** Lee, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.10823](https://arxiv.org/abs/2504.10823)
- **Dataset Size:** 345 high-impact dilemmas with 3,795 diverse value perspectives across 14 models
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 255. BRAND: Bilingual Religious Accountable Norm Dataset

- **Authors:** Hossain, K.A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2512.03943](https://arxiv.org/abs/2512.03943)
- **Dataset Size:** 2,400+ entries across Buddhism, Christianity, Hinduism, and Islam in English and Bengali
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 256. MoVa: Towards Generalizable Classification of Human Morals and Values

- **Authors:** Chen, Z. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** [2509.24216](https://arxiv.org/abs/2509.24216)
- **Dataset Size:** Suite of 16 labeled datasets across four moral frameworks with lightweight LLM prompting strategy
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 257. MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables

- **Authors:** Marcuzzo, M. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** [2509.12371](https://arxiv.org/abs/2509.12371)
- **Dataset Size:** Literature-based benchmark using fables for abstract moral reasoning, includes adversarial variants
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 258. EthicsSuite: Detecting Behavioral Inconsistency in LLM Ethics Suggestions

- **Authors:** Ma, P. et al.
- **Year:** 2025
- **Venue:** ACM TOSEM
- **DOI:** [10.1145/3722554](https://doi.org/10.1145/3722554)
- **Dataset Size:** 20K moral situations designed to detect behavioral inconsistency using reflective equilibrium principles
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 259. GVS-Scale and GVS-Bench: GenAI Value Safety Scale

- **Authors:** He, Z. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.09112](https://arxiv.org/abs/2601.09112)
- **Dataset Size:** Unified value safety framework with lifecycle-oriented taxonomy for GenAI systems
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 260. VAPT: Value-Alignment Perception Toolkit

- **Authors:** Yun, S. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.22440](https://arxiv.org/abs/2601.22440)
- **Dataset Size:** Month-long chatbot interaction study capturing naturalistic value perception from LLMs
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 261. The Moralization Corpus

- **Authors:** Becker, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2512.15248](https://arxiv.org/abs/2512.15248)
- **Dataset Size:** Multi-genre German dataset analyzing moral values in argumentative discourse with frame-based annotation
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 262. Syntactic Framing Fragility (SFF): Robustness Evaluation of LLM Ethical Decisions

- **Authors:** Elkins, K. & Chun, J.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2601.09724](https://arxiv.org/abs/2601.09724)
- **Dataset Size:** 39,975 ethical decisions from 23 models across 14 scenarios using Logical Polarity Normalization
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 263. Negation Sensitivity Index (NSI)

- **Authors:** Elkins, K. & Chun, J.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.21433](https://arxiv.org/abs/2601.21433)
- **Dataset Size:** 16 models audited across 14 ethical scenarios for negation sensitivity; tiered certification framework
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 264. PSYCH: Psychometric Assessment of LLM Characters

- **Authors:** Kratzke, N. et al.
- **Year:** 2026
- **Venue:** Analytics
- **DOI:** [10.3390/analytics5010005](https://doi.org/10.3390/analytics5010005)
- **Dataset Size:** 330,000+ Big Five Inventory-2 responses from 32 LLMs testing moral personality dimensions
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 265. Theory Trace Card (TTC): Documentation for Socio-Cognitive Benchmarks

- **Authors:** Karimi-Malekabadi, F. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.01878](https://arxiv.org/abs/2601.01878)
- **Dataset Size:** Documentation artifact making explicit the theoretical basis of moral reasoning evaluations
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 266. VideoNorms: Benchmarking Cultural Awareness of Video Language Models

- **Authors:** Varimaldi, N.R. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.08543](https://arxiv.org/abs/2510.08543)
- **Dataset Size:** 1,000+ video-norm pairs from US and Chinese cultures annotated with socio-cultural norms
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 267. NormGenesis: Multicultural Dialogue Generation Dataset

- **Authors:** Hong, M. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** [2509.18395](https://arxiv.org/abs/2509.18395)
- **Dataset Size:** 10,800 multi-turn dialogues across English, Chinese, Korean annotated for norm adherence
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 268. BehaviorBench: Multi-Tier Benchmark for Agent Behavior Editing

- **Authors:** Huang, B. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.20606](https://arxiv.org/abs/2506.20606)
- **Dataset Size:** Multi-tier benchmark grounded in psychological moral theories for behavior evaluation and editing
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 269. C-VARC: Chinese Value Rule Corpus

- **Authors:** Wu, P. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.01495](https://arxiv.org/abs/2506.01495)
- **Dataset Size:** 250,000+ value rules based on hierarchical Chinese value framework (50 values) + 400,000 moral dilemma scenarios
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 270. MIST: Moral Inference through Storytelling with Text and Images

- **Authors:** Gao, C. et al.
- **Year:** 2025
- **Venue:** CIKM
- **DOI:** [10.1145/3746252.3760884](https://doi.org/10.1145/3746252.3760884)
- **Dataset Size:** Multi-image dataset evaluating moral reasoning in complex dynamic scenarios across seven VLMs
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 271. AdAEM: Adaptively and Automated Extensible Measurement for Value Alignment

- **Authors:** Duan, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2505.13531](https://arxiv.org/abs/2505.13531)
- **Dataset Size:** 12,310 self-generated questions grounded in Schwartz Value Theory, auto-adapting to reveal value differences
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 272. CQ-Bench: Cultural Intelligence Benchmark for LLMs

- **Authors:** Liu, Z. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.01127](https://arxiv.org/abs/2504.01127)
- **Dataset Size:** Benchmarks LLMs' metacognitive cultural intelligence for implicit cultural values across diverse contexts
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 273. OvertonScore: Benchmarking Overton Pluralism in LLMs

- **Authors:** Poole-Dayan, E. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2512.01351](https://arxiv.org/abs/2512.01351)
- **Dataset Size:** OvertonScore metric validated against 1,209 human respondents across 60 questions and 8 models
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 274. EVALUESTEER: Measuring Reward Model Steerability Across Value Dimensions

- **Authors:** Ghate, K. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.06370](https://arxiv.org/abs/2510.06370)
- **Dataset Size:** 165,888 synthetic preference pairs testing alignment across value dimensions (traditional, secular-rational, survival, self-expression)
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 275. Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity

- **Authors:** Zhou, Q. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2505.11861](https://arxiv.org/abs/2505.11861)
- **Dataset Size:** 238,623 preference records across 28 social groups and 98 equity topics
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 276. DIB Benchmark: Decision-based Implicit Bias in LLMs

- **Authors:** Ma, Y. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2602.01558](https://arxiv.org/abs/2602.01558)
- **Dataset Size:** 3,776 decision-making scenarios across nine social domains for quantifying implicit bias
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 277. VIVA: A Benchmark for Vision-Grounded Decision-Making with Human Values

- **Authors:** Hu, Z. et al.
- **Year:** 2024
- **Venue:** EMNLP
- **arXiv:** [2407.03000](https://arxiv.org/abs/2407.03000)
- **Dataset Size:** 1,062 images assessing vision-language models' capacity to leverage human values for decision-making
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 278. OffTheRails: Procedural Dilemma Generation for Moral Reasoning

- **Authors:** Franken, J.-P. et al.
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** [2404.10975](https://arxiv.org/abs/2404.10975)
- **Dataset Size:** 50 procedurally generated scenarios with 400 test items from causal graphs for harm-related permissibility
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 279. Moral Association Graph: Cognitive Model for Interpretable Moral Inference

- **Authors:** Ramezani, A. & Xu, Y.
- **Year:** 2024
- **Venue:** Topics in Cognitive Science
- **DOI:** [10.1111/tops.12774](https://doi.org/10.1111/tops.12774)
- **Dataset Size:** Word association network-based cognitive model for moral inference grounded in psychological data
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 280. Multimodal Understanding of Human Values in Videos

- **Authors:** Wang, Y. et al.
- **Year:** 2025
- **Venue:** Neurocomputing
- **DOI:** [10.1016/j.neucom.2025.130170](https://doi.org/10.1016/j.neucom.2025.130170)
- **Dataset Size:** First multimodal benchmark for human value understanding in video content
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 281. Values in the Wild: Discovering and Analyzing Values in Real AI Interactions

- **Authors:** Huang, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2504.15236](https://arxiv.org/abs/2504.15236)
- **Dataset Size:** 3,307 AI values extracted from hundreds of thousands of real interactions with high ecological validity
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 282. I2P: Inappropriate Image Prompts Test Bed

- **Authors:** Schramowski, P. et al.
- **Year:** 2022
- **Venue:** FAccT
- **arXiv:** [2202.06675](https://arxiv.org/abs/2202.06675)
- **Dataset Size:** Real-world prompts for evaluating inappropriate content in image generation models
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 283. CCD-Bench: Probing Cultural Conflict in LLM Decision-Making

- **Authors:** Multiple authors
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.03553](https://arxiv.org/abs/2510.03553)
- **Dataset Size:** 2,182 open-ended dilemmas spanning seven domains with ten response options from ten GLOBE cultural clusters
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 284. SafetyPrompts: Systematic Review of Open Datasets for LLM Safety

- **Authors:** Rottger, P. et al.
- **Year:** 2024
- **Venue:** AAAI
- **arXiv:** [2404.05399](https://arxiv.org/abs/2404.05399)
- **Dataset Size:** Systematic review of 144 datasets for LLM safety evaluation; living catalogue at SafetyPrompts.com
- **Code/Data:** SafetyPrompts.com
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 285. Investigating Machine Moral Judgement through the Delphi Experiment

- **Authors:** Jiang, L. et al.
- **Year:** 2025
- **Venue:** Nature Machine Intelligence
- **DOI:** [10.1038/s42256-024-00969-6](https://doi.org/10.1038/s42256-024-00969-6)
- **Dataset Size:** Large-scale systematic investigation of machine moral judgment across 14 models (extends original Delphi)
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 286. GPLA: Generative Psycho-Lexical Approach for Constructing Value Systems

- **Authors:** Ye, H. et al.
- **Year:** 2025
- **Venue:** ACL
- **arXiv:** [2502.02444](https://arxiv.org/abs/2502.02444)
- **Dataset Size:** Psychologically-grounded method for constructing LLM value systems with three benchmarking tasks
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 287. Do LLMs Walk Their Talk? Multi-Method Moral Evaluation Framework

- **Authors:** Andric, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2512.01568](https://arxiv.org/abs/2512.01568)
- **Dataset Size:** Tests implicit associations (IAT), behavioral altruism, and explicit beliefs across 24 LLMs
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 288. DIVE: Dataset for Pluralistic Alignment of Text-to-Image Models

- **Authors:** Rastogi, C. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2507.13383](https://arxiv.org/abs/2507.13383)
- **Dataset Size:** 1,000 prompts with safety perspectives from demographically intersectional raters for text-to-image alignment
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 289. SpeciesismBench: Evaluating LLM Recognition of Speciesist Statements

- **Authors:** Jotautaite, M. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2508.11534](https://arxiv.org/abs/2508.11534)
- **Dataset Size:** 1,003-item benchmark assessing recognition and moral evaluation of speciesist statements
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 290. ManagerBench: Evaluating Safety-Pragmatism Trade-off in Managerial Contexts

- **Authors:** Simhi, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.00857](https://arxiv.org/abs/2510.00857)
- **Dataset Size:** Realistic human-validated managerial scenarios forcing choices between pragmatic/harmful and safe alternatives
- **Code/Data:** Not specified
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 291. MoralBench: A Multi-Faceted Benchmark (Gai et al.)

- **Authors:** Gai, Y. et al.
- **Year:** 2025
- **Venue:** PhilArchive
- **Dataset Size:** Three-component: 1K safety-alignment prompts, 10K abstracted variations, 19,132 structured ethical annotations
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 292. NormAd-ETI: Multiple LLM Agents Debate for Equitable Cultural Alignment

- **Authors:** Ki, H. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2505.24671](https://arxiv.org/abs/2505.24671)
- **Dataset Size:** Social etiquette norms across 75 countries for cultural adaptability through multi-agent debate
- **Code/Data:** Not specified
- **Implementation Readiness:** HIGH
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 293. TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction

- **Authors:** Nadies, S. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** [2601.10410](https://arxiv.org/abs/2601.10410)
- **Dataset Size:** 3M Romanian synthetic fables + 3M English fables with six-slot scaffold for narrative-based moral training
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 294. Reward Model Perspectives on Demographic Alignment (Elle et al.)

- **Authors:** Elle, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.06391](https://arxiv.org/abs/2510.06391)
- **Dataset Size:** Framework for demographic alignment of reward models
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 295. Cross-cultural Value Alignment: Multi-Method Audit (Liu et al.)

- **Authors:** Liu, Y. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2511.17256](https://arxiv.org/abs/2511.17256)
- **Dataset Size:** Multi-method audit framework for cross-cultural value alignment
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 296. Scales of Justitia: Safety Evaluation Taxonomy (Liu et al.)

- **Authors:** Liu, Y. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2506.11094](https://arxiv.org/abs/2506.11094)
- **Dataset Size:** Survey and taxonomy of safety evaluation approaches
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 297. BenchRisk: Identifying 57 Failure Modes in AI Safety Benchmarks (McGregor et al.)

- **Authors:** McGregor, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** [2510.21460](https://arxiv.org/abs/2510.21460)
- **Dataset Size:** Meta-evaluation identifying 57 failure modes across AI safety benchmarks
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 298. CoreValue: Chinese Values Knowledge Base (Liu et al.)

- **Authors:** Liu, Y. et al.
- **Year:** 2022
- **Venue:** Not specified
- **Dataset Size:** Chinese values knowledge base
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 299. Moral Coherentism: Theoretical Framework (Muntean)

- **Authors:** Muntean, I.
- **Year:** 2025
- **Venue:** Not specified
- **Dataset Size:** Theoretical framework for moral coherentism in AI systems
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---

### 300. Chain-of-Ethics: Defense Framework (Wu et al.)

- **Authors:** Wu, Y. et al.
- **Year:** 2025
- **Venue:** Not specified
- **Dataset Size:** Defense framework using chain-of-ethics reasoning
- **Code/Data:** Not specified
- **Implementation Readiness:** LOW
- **Source Agent(s):** Agent 1 (Citation Graph)

---
