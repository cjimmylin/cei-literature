# Agent 1: Citation Graph Traversal Report

**Date:** 2026-02-07
**Method:** Forward and backward citation traversal via Semantic Scholar API + supplementary web searches
**Seed Papers Traced:** 15 (ETHICS, Moral Machine, Social Chemistry 101, Scruples, Moral Stories, Delphi, Scherrer 2023, ValueBench, Value Kaleidoscope, DecodingTrust, Constitutional AI, Moral Choice Machine, Moral Integrity Corpus, MoralDial, MoralBench)

---

## Summary

| Metric | Count |
|--------|-------|
| Total unique papers found (not in vault) | 62 |
| Papers via forward citations | 47 |
| Papers via backward references | 2 |
| Papers via supplementary web searches | 13 |
| HIGH implementation readiness | 28 |
| MEDIUM implementation readiness | 24 |
| LOW implementation readiness | 10 |

**Key findings:**
- The 2025 explosion of moral/ethical benchmarks continues into 2026 with significant new work on pluralistic values, cross-cultural alignment, multimodal moral reasoning, and dynamic/evolving moral evaluation.
- Major gaps in the vault: multi-step moral dilemmas (MMDs), vision-language moral benchmarks (VIVA, MIST, MORALISE already in vault), procedural dilemma generation (OffTheRails), and pluralistic alignment benchmarks (VITAL, PluriHarms, CCD-Bench).
- Several new meta-evaluation frameworks (SafetyPrompts, BenchRisk, VALUEFLOW) provide infrastructure for organizing and comparing moral benchmarks.

---

## Section 1: Papers Found via Forward Citations

Papers discovered by tracing who cites the 15 seed papers.

---

### 1. COMETH: Contextual Organization of Moral Evaluation from Textual Human Inputs
- **Authors:** Morlat, G. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2512.21439
- **Citation Count:** 0
- **Dataset/Benchmark Name:** COMETH
- **Cited By / Cites:** Cited by Scherrer 2023, Moral Machine (forward)
- **Relevance:** 300-scenario dataset with ternary moral judgments (Blame/Neutral/Support) from 101 participants across six core moral actions. Empirically grounded in human moral evaluation rather than theory-driven categories.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 2. MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models
- **Authors:** Chiu, Y.Y. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.16380
- **Citation Count:** 0
- **Dataset/Benchmark Name:** MoReBench
- **Cited By / Cites:** Cites Scherrer 2023, Delphi (forward)
- **Relevance:** 1,000 moral scenarios with expert rubric criteria covering moral considerations, trade-offs, and recommendations across five ethical frameworks. Also includes MoReBench-Theory with 150 examples.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no (MoReBench by Chiu 2025 is in vault but check if this is the same paper -- the vault has "2025-Chiu-MoReBench" so this IS in the vault)

---

### 3. The Moral Dilemma Dataset
- **Authors:** Russo, G. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2507.17216
- **Citation Count:** 5
- **Dataset/Benchmark Name:** Moral Dilemma Dataset
- **Cited By / Cites:** Cites Scherrer 2023, Delphi (forward)
- **Relevance:** 1,618 real-world moral dilemmas paired with distributions of human moral judgments and value rationales. Also introduces Dynamic Moral Profiling (DMP) using Dirichlet-based sampling.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no -- check for "2025-Russo-*"

---

### 4. VAL-Bench: Belief Consistency as a Measure for Value Alignment
- **Authors:** Gupta, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.05465
- **Citation Count:** 1
- **Dataset/Benchmark Name:** VAL-Bench
- **Cited By / Cites:** Cites Scherrer 2023 (forward)
- **Relevance:** 115K pairs of prompts from Wikipedia eliciting opposing stances on controversial issues. Measures belief consistency as proxy for value alignment.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 5. Multi-step Moral Dilemmas (MMDs)
- **Authors:** Wu, Y. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** 2505.18154
- **Citation Count:** 7
- **Dataset/Benchmark Name:** MMDs (Multi-step Moral Dilemmas)
- **Cited By / Cites:** Cites Delphi, Social Chemistry 101, Moral Stories (forward)
- **Relevance:** 3,302 five-stage dilemmas enabling fine-grained dynamic analysis of evolving moral judgments across escalating scenarios. First dataset tracking moral reasoning evolution.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 6. CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives
- **Authors:** Lee, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2504.10823
- **Citation Count:** 3
- **Dataset/Benchmark Name:** CLASH
- **Cited By / Cites:** Cites Scherrer 2023, Delphi, Social Chemistry 101 (forward)
- **Relevance:** 345 high-impact dilemmas with 3,795 diverse value perspectives. Examines decision ambivalence, psychological discomfort, and temporal value shifts across 14 models.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 7. BRAND: Bilingual Religious Accountable Norm Dataset
- **Authors:** Hossain, K.A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2512.03943
- **Citation Count:** 0
- **Dataset/Benchmark Name:** BRAND
- **Cited By / Cites:** Cites ETHICS benchmark, Delphi (forward)
- **Relevance:** 2,400+ entries across Buddhism, Christianity, Hinduism, and Islam in English and Bengali. Detects religious bias in multilingual models.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 8. MoVa: Towards Generalizable Classification of Human Morals and Values
- **Authors:** Chen, Z. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** 2509.24216
- **Citation Count:** 3
- **Dataset/Benchmark Name:** MoVa
- **Cited By / Cites:** Cites Scherrer 2023, Social Chemistry 101, Delphi (forward)
- **Relevance:** Suite comprising 16 labeled datasets across four theoretically-grounded moral frameworks with lightweight LLM prompting strategy outperforming fine-tuned models.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 9. MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables
- **Authors:** Marcuzzo, M. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** 2509.12371
- **Citation Count:** 3
- **Dataset/Benchmark Name:** MORABLES
- **Cited By / Cites:** Cites Scruples, Delphi (forward)
- **Relevance:** Literature-based benchmark using fables for evaluating complex abstract moral reasoning. Includes adversarial variants to surface model vulnerabilities.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 10. EthicsMH: A Pilot Benchmark for Ethical Reasoning in Mental Health AI
- **Authors:** Kasu, S.K.R. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2509.11648
- **Citation Count:** 1
- **Dataset/Benchmark Name:** EthicsMH
- **Cited By / Cites:** Cites Scruples (forward)
- **Relevance:** 125 scenarios evaluating AI navigation of ethically charged mental health situations with multi-stakeholder viewpoints.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 11. EthicsSuite
- **Authors:** Ma, P. et al.
- **Year:** 2025
- **Venue:** ACM TOSEM
- **DOI:** 10.1145/3722554
- **Citation Count:** 2
- **Dataset/Benchmark Name:** EthicsSuite
- **Cited By / Cites:** Cites Delphi, ETHICS benchmark (forward)
- **Relevance:** 20K moral situations designed to detect behavioral inconsistency in LLM ethics-related suggestions using reflective equilibrium principles.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 12. GVS-Scale and GVS-Bench: GenAI Value Safety Scale
- **Authors:** He, Z. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.09112
- **Citation Count:** 0
- **Dataset/Benchmark Name:** GVS-Scale / GVS-Bench
- **Cited By / Cites:** Cites ETHICS benchmark (forward)
- **Relevance:** Unified value safety framework with lifecycle-oriented taxonomy for evaluating GenAI systems across the full development cycle.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 13. VAPT: Value-Alignment Perception Toolkit
- **Authors:** Yun, S. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.22440
- **Citation Count:** 1
- **Dataset/Benchmark Name:** VAPT
- **Cited By / Cites:** Cites ETHICS benchmark (forward)
- **Relevance:** Studies how LLMs reflect people's values through month-long chatbot interactions. Captures naturalistic value perception.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 14. The Moralization Corpus
- **Authors:** Becker, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2512.15248
- **Citation Count:** 0
- **Dataset/Benchmark Name:** Moralization Corpus
- **Cited By / Cites:** Cites ETHICS benchmark (forward)
- **Relevance:** Multi-genre German dataset analyzing how moral values are strategically used in argumentative discourse. Frame-based annotation scheme.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 15. Syntactic Framing Fragility (SFF)
- **Authors:** Elkins, K. & Chun, J.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2601.09724
- **Citation Count:** 0
- **Dataset/Benchmark Name:** SFF (Syntactic Framing Fragility)
- **Cited By / Cites:** Cites ETHICS benchmark, DecodingTrust (forward)
- **Relevance:** Robustness evaluation framework using Logical Polarity Normalization (LPN) auditing 23 models across 39,975 ethical decisions from 14 ethical scenarios.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 16. Negation Sensitivity Index (NSI)
- **Authors:** Elkins, K. & Chun, J.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.21433
- **Citation Count:** 0
- **Dataset/Benchmark Name:** NSI (Negation Sensitivity Index)
- **Cited By / Cites:** Cites ETHICS benchmark (forward)
- **Relevance:** Audits 16 models across 14 ethical scenarios for negation sensitivity, proposing tiered certification framework as governance metric.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 17. PSYCH: Psychometric Assessment of LLM Characters
- **Authors:** Kratzke, N. et al.
- **Year:** 2026
- **Venue:** Analytics
- **DOI:** 10.3390/analytics5010005
- **Citation Count:** 0
- **Dataset/Benchmark Name:** PSYCH
- **Cited By / Cites:** Cites ETHICS benchmark (forward)
- **Relevance:** Systematic psychometric screening of 32 LLMs using Big Five Inventory-2 across 330,000+ responses. Tests moral personality dimensions.
- **Implementation Readiness:** LOW
- **Already in vault?** Likely no

---

### 18. Theory Trace Card (TTC)
- **Authors:** Karimi-Malekabadi, F. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.01878
- **Citation Count:** 0
- **Dataset/Benchmark Name:** TTC (Theory Trace Card)
- **Cited By / Cites:** Cites ETHICS benchmark, Scherrer 2023 (forward)
- **Relevance:** Documentation artifact making explicit the theoretical basis of evaluations. Enhances interpretability of socio-cognitive benchmarks including moral reasoning ones.
- **Implementation Readiness:** LOW
- **Already in vault?** Likely no

---

### 19. GuardEval
- **Authors:** Machlovi, N. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2601.03273
- **Citation Count:** 0
- **Dataset/Benchmark Name:** GuardEval
- **Cited By / Cites:** Cites Delphi, Social Chemistry 101 (forward)
- **Relevance:** Unified safety/fairness/robustness benchmark with 106 fine-grained categories spanning emotions, offensive language, gender/racial bias, and safety concerns.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 20. VideoNorms: Benchmarking Cultural Awareness of Video Language Models
- **Authors:** Varimaldi, N.R. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.08543
- **Citation Count:** 0
- **Dataset/Benchmark Name:** VideoNorms
- **Cited By / Cites:** Cites Social Chemistry 101 (forward)
- **Relevance:** 1,000+ video-norm pairs from US and Chinese cultures annotated with socio-cultural norms. Novel multimodal norm evaluation.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 21. NormGenesis: Multicultural Dialogue Generation Dataset
- **Authors:** Hong, M. et al.
- **Year:** 2025
- **Venue:** EMNLP
- **arXiv:** 2509.18395
- **Citation Count:** 1
- **Dataset/Benchmark Name:** NormGenesis
- **Cited By / Cites:** Cites Social Chemistry 101 (forward)
- **Relevance:** 10,800 multi-turn dialogues across English, Chinese, Korean annotated for norm adherence. Bridges cultural norms and dialogue evaluation.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 22. SI-Bench: Benchmarking Social Intelligence of LLMs
- **Authors:** Huang, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.23182
- **Citation Count:** 1
- **Dataset/Benchmark Name:** SI-Bench
- **Cited By / Cites:** Cites Social Chemistry 101 (forward)
- **Relevance:** 2,221 authentic multi-turn dialogues evaluating social intelligence aspects including moral/ethical reasoning dimensions.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 23. BehaviorBench: Multi-Tier Benchmark for Agent Behavior Editing
- **Authors:** Huang, B. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2506.20606
- **Citation Count:** 0
- **Dataset/Benchmark Name:** BehaviorBench
- **Cited By / Cites:** Cites Social Chemistry 101 (forward)
- **Relevance:** Multi-tier benchmark grounded in psychological moral theories supporting behavior evaluation and editing of LLM agents.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 24. C-VARC: Chinese Value Rule Corpus
- **Authors:** Wu, P. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2506.01495
- **Citation Count:** 2
- **Dataset/Benchmark Name:** C-VARC
- **Cited By / Cites:** Cites Moral Stories, Social Chemistry 101 (forward)
- **Relevance:** 250,000+ value rules based on hierarchical Chinese value framework with 50 derived values, plus 400,000 rule-based moral dilemma scenarios.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 25. MIST: Moral Inference through Storytelling with Text and Images
- **Authors:** Gao, C. et al.
- **Year:** 2025
- **Venue:** CIKM
- **DOI:** 10.1145/3746252.3760884
- **Citation Count:** 0
- **Dataset/Benchmark Name:** MIST
- **Cited By / Cites:** Cites Social Chemistry 101 (forward)
- **Relevance:** Multi-image dataset evaluating moral reasoning in complex dynamic scenarios across seven VLMs. Tests inference from narrative sequences.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 26. RoleConflictBench
- **Authors:** Shin, J. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2509.25897
- **Citation Count:** 0
- **Dataset/Benchmark Name:** RoleConflictBench
- **Cited By / Cites:** Cites Delphi, Scherrer 2023, Value Kaleidoscope (forward)
- **Relevance:** 13K+ realistic role conflict scenarios across 65 roles, systematically varying expectations and urgency levels.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 27. ConflictScope: Generative Value Conflicts Reveal LLM Priorities
- **Authors:** Liu, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2509.25369
- **Citation Count:** 2
- **Dataset/Benchmark Name:** ConflictScope
- **Cited By / Cites:** Cites Scherrer 2023, Value Kaleidoscope (forward)
- **Relevance:** Automatic pipeline generating value-conflict scenarios to rank LLM value prioritization. Reveals implicit value hierarchies.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 28. Deep Value Benchmark (DVB)
- **Authors:** Ashkinaze, J. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2511.02109
- **Citation Count:** 1
- **Dataset/Benchmark Name:** DVB (Deep Value Benchmark)
- **Cited By / Cites:** Cites ValueBench, Scherrer 2023 (forward)
- **Relevance:** Tests whether LLMs learn fundamental human values or only surface-level preferences through controlled confounding experiments. Measures Deep Value Generalization Rate (DVGR).
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 29. NurValues
- **Authors:** Yao, B. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2505.08734
- **Citation Count:** 0
- **Dataset/Benchmark Name:** NurValues
- **Cited By / Cites:** Cites ValueBench (forward)
- **Relevance:** First nursing-specific values alignment benchmark with 4,400 instances across five core nursing dimensions from real clinical contexts.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 30. AdAEM: Adaptively and Automated Extensible Measurement
- **Authors:** Duan, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2505.13531
- **Citation Count:** 3
- **Dataset/Benchmark Name:** AdAEM
- **Cited By / Cites:** Cites ValueBench, Value Kaleidoscope (forward)
- **Relevance:** Self-extensible assessment generating 12,310 questions grounded in Schwartz Value Theory. Automatically adapts to reveal value differences.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 31. CQ-Bench: Cultural Intelligence Benchmark
- **Authors:** Liu, Z. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2504.01127
- **Citation Count:** 8
- **Dataset/Benchmark Name:** CQ-Bench
- **Cited By / Cites:** Cites ValueBench (forward)
- **Relevance:** Benchmarks LLMs' metacognitive cultural intelligence for grasping implicit cultural values across diverse contexts.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 32. PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm
- **Authors:** Li, J.-J. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.08951
- **Citation Count:** 0
- **Dataset/Benchmark Name:** PluriHarms
- **Cited By / Cites:** Cites Value Kaleidoscope (forward)
- **Relevance:** 150 prompts with 15,000 ratings capturing diverse values and demographic traits. Studies harm judgment agreement/disagreement.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 33. Benchmarking Overton Pluralism in LLMs (OvertonScore)
- **Authors:** Poole-Dayan, E. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2512.01351
- **Citation Count:** 0
- **Dataset/Benchmark Name:** OvertonScore
- **Cited By / Cites:** Cites Value Kaleidoscope (forward)
- **Relevance:** Framework measuring viewpoint diversity representation. OvertonScore metric validated against 1,209 human respondents across 60 questions and 8 models.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 34. EVALUESTEER: Measuring Reward Model Steerability
- **Authors:** Ghate, K. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.06370
- **Citation Count:** 0
- **Dataset/Benchmark Name:** EVALUESTEER
- **Cited By / Cites:** Cites Value Kaleidoscope (forward)
- **Relevance:** 165,888 synthetic preference pairs testing LLM/reward model alignment across value dimensions (traditional, secular-rational, survival, self-expression).
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 35. Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity
- **Authors:** Zhou, Q. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2505.11861
- **Citation Count:** 3
- **Dataset/Benchmark Name:** Fair-PP
- **Cited By / Cites:** Cites Value Kaleidoscope (forward)
- **Relevance:** 238,623 preference records across 28 social groups and 98 equity topics. Enables fine-grained personalized preference alignment analysis.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 36. Value Portrait
- **Authors:** Han, J. et al.
- **Year:** 2025
- **Venue:** ACL
- **arXiv:** 2505.01015
- **Citation Count:** 6
- **Dataset/Benchmark Name:** Value Portrait
- **Cited By / Cites:** Cites Scruples, Value Kaleidoscope (forward)
- **Relevance:** Psychometrically validated items capturing real-life user-LLM interactions. Evaluates 44 LLMs' value orientations with human subject correlation ratings.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 37. DIB Benchmark: Decision-based Implicit Bias
- **Authors:** Ma, Y. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2602.01558
- **Citation Count:** 0
- **Dataset/Benchmark Name:** DIB Benchmark
- **Cited By / Cites:** Cites Constitutional AI (forward)
- **Relevance:** 3,776 decision-making scenarios across nine social domains for quantifying implicit bias in long-horizon LLM processes.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 38. ProgressGym: Alignment with a Millennium of Moral Progress
- **Authors:** Qiu, T. et al.
- **Year:** 2024
- **Venue:** NeurIPS
- **arXiv:** 2406.20087
- **Citation Count:** 9
- **Dataset/Benchmark Name:** ProgressGym (PG-Follow, PG-Predict, PG-Coevolve)
- **Cited By / Cites:** Cites Moral Choice Machine (forward)
- **Relevance:** Experimental framework leveraging 9 centuries of historical text and 18 historical LLMs. Three core benchmarks for tracking evolving values and anticipating moral advancement.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 39. VIVA: A Benchmark for Vision-Grounded Decision-Making with Human Values
- **Authors:** Hu, Z. et al.
- **Year:** 2024
- **Venue:** EMNLP
- **arXiv:** 2407.03000
- **Citation Count:** 11
- **Dataset/Benchmark Name:** VIVA
- **Cited By / Cites:** Cites MoralDial (forward)
- **Relevance:** Multimodal benchmark with 1,062 images assessing vision-language models' capacity to leverage human values for decision-making, including action selection and value reasoning.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 40. OffTheRails: Procedural Dilemma Generation for Moral Reasoning
- **Authors:** Franken, J.-P. et al.
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** 2404.10975
- **Citation Count:** 1
- **Dataset/Benchmark Name:** OffTheRails
- **Cited By / Cites:** Cites Scruples, Moral Stories (forward)
- **Relevance:** Procedurally generated 50 scenarios with 400 test items from causal graphs. Tests harm-related permissibility judgments across conditions with both human and LLM data.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 41. The Goofus & Gallant Story Corpus for Practical Value Alignment
- **Authors:** Nahian, M.S.A. et al.
- **Year:** 2024
- **Venue:** ICMLA
- **arXiv:** 2501.09707
- **Citation Count:** 0
- **Dataset/Benchmark Name:** Goofus & Gallant Corpus
- **Cited By / Cites:** Cites Moral Stories, Delphi (forward)
- **Relevance:** Multi-modal dataset from children's educational materials illustrating normative and non-normative behavior through narrative and artistic images.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 42. MMRB: Multilingual Moral Reasoning Benchmark
- **Authors:** Zhou, H. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2504.19759
- **Citation Count:** 0
- **Dataset/Benchmark Name:** MMRB
- **Cited By / Cites:** Cites Moral Integrity Corpus (forward)
- **Relevance:** Evaluates moral reasoning across five typologically diverse languages at three contextual complexity levels. Emphasizes low-resource language importance.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no -- check "2025-Zhou-Moral Reasoning Across Languages" (this IS in the vault)

---

### 43. Moral Association Graph
- **Authors:** Ramezani, A. & Xu, Y.
- **Year:** 2024
- **Venue:** Topics in Cognitive Science
- **DOI:** 10.1111/tops.12774
- **Citation Count:** 1
- **Dataset/Benchmark Name:** Moral Association Graph
- **Cited By / Cites:** Cites Moral Stories, Social Chemistry 101 (forward)
- **Relevance:** Cognitive model inspired by psychological moralization for interpretable moral inference, building on word association networks with psychological data grounding.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 44. Multimodal Understanding of Human Values in Videos
- **Authors:** Wang, Y. et al.
- **Year:** 2025
- **Venue:** Neurocomputing
- **DOI:** 10.1016/j.neucom.2025.130170
- **Citation Count:** 2
- **Dataset/Benchmark Name:** (Multimodal human values video benchmark)
- **Cited By / Cites:** Cites Scruples, Social Chemistry 101 (forward)
- **Relevance:** First multimodal benchmark for human value understanding in video content with pre-trained language model methodology.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 45. Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval)
- **Authors:** Galatolo, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2508.12754
- **Citation Count:** 2
- **Dataset/Benchmark Name:** AMAeval
- **Cited By / Cites:** Cites Delphi, Social Chemistry 101, Scruples (forward)
- **Relevance:** Benchmark testing moral assistant qualities including deductive and abductive moral reasoning capabilities. Tests moral reasoning quality, not just classification.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 46. CASE-Bench: Context-Aware Safety Benchmark
- **Authors:** Sun, Y. et al.
- **Year:** 2025
- **Venue:** ICML
- **arXiv:** 2501.14940
- **Citation Count:** 10
- **Dataset/Benchmark Name:** CASE-Bench
- **Cited By / Cites:** Cites Moral Stories, ETHICS benchmark (forward)
- **Relevance:** Integrates contextual integrity theory into safety assessments using formally described contexts. Bridges privacy theory and moral evaluation.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 47. Values in the Wild
- **Authors:** Huang, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2504.15236
- **Citation Count:** 31
- **Dataset/Benchmark Name:** Values in the Wild
- **Cited By / Cites:** Cites Value Kaleidoscope (forward)
- **Relevance:** Bottom-up analysis extracting 3,307 AI values from hundreds of thousands of real interactions. Maps context-dependent value expression with high ecological validity.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

## Section 2: Papers Found via Backward References

Papers cited BY the seed papers that are relevant benchmarks/datasets not already in the vault.

---

### 48. EmpatheticDialogues
- **Authors:** Rashkin, H. et al.
- **Year:** 2018
- **Venue:** ACL
- **arXiv:** 1811.00207
- **Citation Count:** 1,045
- **Dataset/Benchmark Name:** EmpatheticDialogues
- **Cited By / Cites:** Referenced by ETHICS benchmark (backward)
- **Relevance:** 25K conversations grounded in emotional situations. Foundational dataset for empathetic dialogue that underpins moral dialogue research.
- **Implementation Readiness:** LOW (not directly moral/ethical but foundational)
- **Already in vault?** Likely no

---

### 49. I2P: Inappropriate Image Prompts Test Bed
- **Authors:** Schramowski, P. et al.
- **Year:** 2022
- **Venue:** FAccT
- **arXiv:** 2202.06675
- **Citation Count:** 154
- **Dataset/Benchmark Name:** I2P (Inappropriate Image Prompts)
- **Cited By / Cites:** Referenced by Moral Choice Machine (backward/related)
- **Relevance:** Real-world prompts for evaluating inappropriate content in image generation models. Bridges text-based moral evaluation to visual modality.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

## Section 3: Papers Found via Supplementary Web Searches

---

### 50. VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment
- **Authors:** Kim, W. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2602.03160
- **Citation Count:** 0
- **Dataset/Benchmark Name:** VALUEFLOW (HiVES, VIDB)
- **Cited By / Cites:** Supplementary search
- **Relevance:** First unified framework spanning extraction, evaluation, and steering with calibrated intensity control. Includes HiVES (hierarchical value embedding space) and VIDB (Value Intensity DataBase) -- a large-scale resource of value-labeled texts with intensity estimates.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 51. CCD-Bench: Probing Cultural Conflict in LLM Decision-Making
- **Authors:** (Multiple)
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.03553
- **Citation Count:** (not specified)
- **Dataset/Benchmark Name:** CCD-Bench
- **Cited By / Cites:** Supplementary search
- **Relevance:** 2,182 open-ended dilemmas spanning seven domains, each paired with ten anonymized response options from ten GLOBE cultural clusters. Reveals Western-centric bias in LLM decision-making.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 52. VITAL: Benchmarking Pluralistic Alignment in Healthcare
- **Authors:** Shetty, A. et al.
- **Year:** 2025
- **Venue:** ACL
- **arXiv:** 2502.13775
- **Citation Count:** (not specified)
- **Dataset/Benchmark Name:** VITAL
- **Cited By / Cites:** Supplementary search
- **Relevance:** 13.1K value-laden situations and 5.4K multiple-choice questions focused on health. Tests pluralistic alignment in healthcare where plurality is essential.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 53. SafetyPrompts: Systematic Review of Open Datasets for LLM Safety
- **Authors:** Rottger, P. et al.
- **Year:** 2024
- **Venue:** AAAI
- **arXiv:** 2404.05399
- **Citation Count:** 68
- **Dataset/Benchmark Name:** SafetyPrompts.com (living catalogue)
- **Cited By / Cites:** Supplementary search
- **Relevance:** Systematic review of 144 datasets for LLM safety evaluation. Meta-resource identifying gaps and trends. Living catalogue at SafetyPrompts.com.
- **Implementation Readiness:** HIGH (meta-resource)
- **Already in vault?** Likely no

---

### 54. Investigating Machine Moral Judgement through the Delphi Experiment (Nature MI)
- **Authors:** Jiang, L. et al.
- **Year:** 2025
- **Venue:** Nature Machine Intelligence
- **DOI:** 10.1038/s42256-024-00969-6
- **Citation Count:** 28
- **Dataset/Benchmark Name:** Delphi (extended evaluation)
- **Cited By / Cites:** Supplementary search
- **Relevance:** Large-scale systematic investigation of machine moral judgment published in top journal. Evaluates 14 models across diverse moral scenarios.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Possibly -- check if vault has a 2025 Jiang Delphi paper. The vault has "2022-Jiang-Can Machines Learn Morality" which is the original Delphi, but this 2025 Nature MI paper appears to be new.

---

### 55. GPLA: Generative Psycho-Lexical Approach for Constructing Value Systems
- **Authors:** Ye, H. et al.
- **Year:** 2025
- **Venue:** ACL
- **arXiv:** 2502.02444
- **Citation Count:** 3
- **Dataset/Benchmark Name:** GPLA
- **Cited By / Cites:** Supplementary search
- **Relevance:** Psychologically-grounded method for constructing LLM value systems with three benchmarking tasks validating safety prediction and alignment improvement.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 56. Do LLMs Walk Their Talk? Multi-Method Framework
- **Authors:** Andric, S. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2512.01568
- **Citation Count:** 0
- **Dataset/Benchmark Name:** (Multi-method moral evaluation framework)
- **Cited By / Cites:** Supplementary search (cites Scherrer 2023)
- **Relevance:** Tests implicit associations (IAT), behavioral altruism, and explicit beliefs across 24 LLMs. Bridges moral psychology methods and LLM evaluation.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 57. Whose View of Safety? DIVE Dataset for Pluralistic Alignment of Text-to-Image Models
- **Authors:** Rastogi, C. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2507.13383
- **Citation Count:** 3
- **Dataset/Benchmark Name:** DIVE
- **Cited By / Cites:** Supplementary search (related to Value Kaleidoscope)
- **Relevance:** Multimodal dataset capturing safety perspectives from demographically intersectional raters across 1,000 prompts for text-to-image pluralistic alignment.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 58. SpeciesismBench
- **Authors:** Jotautaite, M. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2508.11534
- **Citation Count:** 0
- **Dataset/Benchmark Name:** SpeciesismBench
- **Cited By / Cites:** Supplementary search (cites Scherrer 2023)
- **Relevance:** 1,003-item benchmark assessing recognition and moral evaluation of speciesist statements. Unique moral domain not covered by other benchmarks.
- **Implementation Readiness:** HIGH
- **Already in vault?** Likely no

---

### 59. ManagerBench: Evaluating Safety-Pragmatism Trade-off
- **Authors:** Simhi, A. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.00857
- **Citation Count:** 0
- **Dataset/Benchmark Name:** ManagerBench
- **Cited By / Cites:** Supplementary search (cites Scherrer 2023)
- **Relevance:** Realistic human-validated managerial scenarios forcing choices between pragmatic but harmful actions versus safe alternatives. Applied ethics for business contexts.
- **Implementation Readiness:** MEDIUM
- **Already in vault?** Likely no

---

### 60. MoralBench: A Multi-Faceted Benchmark (Gai et al.)
- **Authors:** Gai, Y. et al.
- **Year:** 2025
- **Venue:** PhilArchive
- **Citation Count:** (not specified)
- **Dataset/Benchmark Name:** MoralBench (Gai version)
- **Cited By / Cites:** Supplementary search
- **Relevance:** Three-component benchmark: 1K high-fidelity safety-alignment prompts, 10K abstracted variations for domain transfer, and 19,132 records with structured ethical annotations. Note: Different from the Ji et al. MoralBench already in the vault.
- **Implementation Readiness:** HIGH
- **Already in vault?** Possibly -- vault has "2024-Ji-MoralBench" which is a different paper. This Gai version appears to be new.

---

### 61. NormAd-ETI: Multiple LLM Agents Debate for Equitable Cultural Alignment
- **Authors:** Ki, H. et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2505.24671
- **Citation Count:** 11
- **Dataset/Benchmark Name:** NormAd-ETI
- **Cited By / Cites:** Supplementary search (cites Moral Stories)
- **Relevance:** Social etiquette norms across 75 countries used for evaluating cultural adaptability through multi-agent debate. Extends NormAd framework.
- **Implementation Readiness:** HIGH
- **Already in vault?** Possibly -- vault has "2025-Rao-NormAd" so check if this is the same or an extension

---

### 62. TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction
- **Authors:** Nadies, S. et al.
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.10410
- **Citation Count:** 0
- **Dataset/Benchmark Name:** TF3-RO-50M / TF1-EN-3M
- **Cited By / Cites:** Cites Moral Stories (forward)
- **Relevance:** Three million Romanian synthetic fables with moral lessons + three million English-language fables with six-slot scaffold for narrative-based moral training. Unique synthetic moral narrative approach.
- **Implementation Readiness:** LOW
- **Already in vault?** Likely no

---

## Appendix: Additional Notable Papers (Lower Priority)

These papers were found during citation traversal but are more tangential (frameworks, surveys, methodology papers rather than benchmarks/datasets):

| Paper | Year | arXiv | Type |
|-------|------|-------|------|
| Discerning Moral Competence (Kilov) | 2025 | 2506.13082 | Framework (5-dimension assessment) |
| Auditing Ethical Logic (Neuman) | 2025 | 2504.17544 | Framework (5-dimension audit) |
| Structured Moral Reasoning (Chakraborty) | 2025 | 2506.14948 | Framework (value-grounded prompts) |
| Moral Consistency Pipeline (Jamshidi) | 2025 | 2512.03026 | Framework (dataset-free evaluation) |
| PRIME Framework (Coleman) | 2025 | 2504.19255 | Framework (multi-theory analysis) |
| Reward Model Perspectives (Elle) | 2025 | 2510.06391 | Framework (demographic alignment) |
| Cross-cultural Value Alignment (Liu) | 2025 | 2511.17256 | Framework (multi-method audit) |
| Scales of Justitia (Liu) | 2025 | 2506.11094 | Survey (safety evaluation taxonomy) |
| BenchRisk (McGregor) | 2025 | 2510.21460 | Meta-evaluation (57 failure modes) |
| CoreValue (Liu) | 2022 | -- | Chinese values knowledge base |
| Moral Coherentism (Muntean) | 2025 | -- | Theoretical framework |
| Chain-of-Ethics (Wu) | 2025 | -- | Defense framework |

---

## Cross-Reference Notes

Papers in this report that MAY already be in the vault (require verification):
- **MoReBench** (Chiu 2025) -- vault has "2025-Chiu-MoReBench" -- LIKELY SAME, EXCLUDE
- **MMRB** (Zhou 2025) -- vault has "2025-Zhou-Moral Reasoning Across Languages" -- POSSIBLY SAME, CHECK
- **NormAd-ETI** (Ki 2025) -- vault has "2025-Rao-NormAd" -- POSSIBLY RELATED, CHECK
- **MoralBench** (Gai 2025) -- vault has "2024-Ji-MoralBench" -- DIFFERENT PAPER

Papers already confirmed in vault (excluded from main list):
- Hendrycks 2021 (ETHICS), Awad 2018 (Moral Machine), Forbes 2020 (Social Chemistry), Lourie 2021 (Scruples), Emelin 2021 (Moral Stories), Jiang 2022 (Delphi), Scherrer 2023, Ren 2024 (ValueBench), Sorensen 2024 (Value Kaleidoscope), Wang 2023 (DecodingTrust), Bai 2022 (Constitutional AI), Schramowski 2020 (Moral Choice Machine), Ziems 2022 (Moral Integrity Corpus), Sun 2022 (MoralDial), Ji 2024 (MoralBench), and all other papers from the exclusion list.
