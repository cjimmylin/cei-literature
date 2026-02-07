# Agent 19: Moral Psychology Instruments & Dynamic Moral Reasoning
## Exhaustive Literature Search Report
**Date:** 2026-02-07
**Domain:** Moral Psychology Instruments, Dynamic Moral Reasoning, Value Measurement, Meta-Ethics Benchmarks for LLMs

---

## Executive Summary

This report documents findings from a comprehensive search across moral psychology instruments adapted for LLM evaluation, dynamic moral reasoning benchmarks, value measurement and consistency tests, narrative/scenario-based moral reasoning tools, and meta-ethics evaluation frameworks. A total of **24 papers** were identified that provide implementable benchmarks or datasets beyond the already-known list. Papers span from 2023 to early 2026, with the majority published at top venues (EMNLP, ACL, ICLR, NeurIPS, FAccT, AIES, KDD).

---

## Section 1: Moral Psychology Instruments

### 1.1 The Staircase of Ethics (Multi-step Moral Dilemmas)

- **Full Citation:** Ya Wu, Qiang Sheng, Danding Wang, Guang Yang, Yifan Sun, Zhengjia Wang, Yuyan Bu, Juan Cao. "The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas." EMNLP 2025 Main Conference. ACL Anthology: 2025.emnlp-main.806.
- **arXiv ID:** 2505.18154
- **Ethical Frameworks:** Moral Foundations Theory (care, fairness, loyalty, authority, sanctity); dynamic value prioritization under escalating complexity
- **Dataset Size & Format:** 3,302 five-stage moral dilemmas (Multi-step Moral Dilemmas / MMDs dataset); each dilemma contains 5 progressive stages with pairwise value comparisons
- **Code/Data URLs:** Not publicly listed at time of search; check ACL Anthology supplementary materials
- **LLMs Tested:** 9 widely used LLMs (specific models detailed in paper)
- **Implementation Readiness:** **High** -- well-structured dataset with clear evaluation protocol and multi-stage design
- **Key Finding:** LLM value preferences shift significantly as dilemmas escalate; care is often prioritized but can be superseded by fairness in complex contexts

---

### 1.2 MoralBench: Moral Evaluation of LLMs

- **Full Citation:** Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, Yongfeng Zhang. "MoralBench: Moral Evaluation of LLMs." ACM SIGKDD Explorations Newsletter, Volume 27, Issue 1, 2025.
- **arXiv ID:** 2406.04428
- **Ethical Frameworks:** Moral Foundations Theory (5 and 6 foundation variants); MFQ-30-LLM adaptation; moral identity assessment
- **Dataset Size & Format:** Two-stage benchmark: Stage 1 (binary agree/disagree on moral statements) and Stage 2 (comparative moral acceptability judgments); uses both 5-foundation and 6-foundation datasets
- **Code/Data URLs:** GitHub: https://github.com/agiresearch/MoralBench; Data: Google Drive (linked from repo)
- **LLMs Tested:** Zephyr, LLaMA-2, Gemma-1.1, GPT-3.5, GPT-4
- **Implementation Readiness:** **High** -- code and data publicly available; well-documented evaluation pipeline
- **Key Finding:** Significant variations in moral reasoning capabilities across different LLMs

---

### 1.3 LLM Ethics Benchmark (Three-Dimensional Assessment)

- **Full Citation:** Junfeng Jiao, Saleh Afroogh, Abhejay Murali, Kevin Chen, David Atkinson, Amit Dhurandhar. "LLM Ethics Benchmark: A Three-Dimensional Assessment System for Evaluating Moral Reasoning in Large Language Models." Scientific Reports, 2025; also arXiv.
- **arXiv ID:** 2505.00853
- **DOI:** 10.1038/s41598-025-18489-7
- **Ethical Frameworks:** Moral Foundations Questionnaire (MFQ), World Values Survey (WVS), standardized moral dilemmas; three dimensions: foundational moral principles, reasoning robustness, value consistency
- **Dataset Size & Format:** Adapts three established instruments from moral psychology; expert-validated scoring criteria
- **Code/Data URLs:** GitHub: https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark
- **LLMs Tested:** Claude 3.7 (91.2%), GPT-4o (87.8%), LLaMA 3.1 (76.3%), and others
- **Implementation Readiness:** **High** -- published in Nature Scientific Reports; public GitHub repo with benchmark datasets and evaluation codebase
- **Key Finding:** Claude 3.7 achieves highest alignment with human moral intuitions

---

### 1.4 Probing Moral Development through Defining Issues Test (DIT)

- **Full Citation:** Kumar Tanmay, Aditi Khandelwal, Utkarsh Agarwal, Monojit Choudhury. "Probing the Moral Development of Large Language Models through Defining Issues Test." arXiv preprint, 2023.
- **arXiv ID:** 2309.13356
- **Ethical Frameworks:** Kohlberg's Cognitive Moral Development Model; Defining Issues Test (DIT) psychometric instrument; pre-conventional, conventional, and post-conventional moral reasoning stages
- **Dataset Size & Format:** DIT-based moral dilemmas with importance-ranking protocol adapted for LLMs
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** GPT-3, ChatGPT, Llama2-Chat, PaLM-2, GPT-4
- **Implementation Readiness:** **Medium** -- established psychometric instrument applied to LLMs; methodology is reproducible but no public code/data repo
- **Key Finding:** GPT-4 achieves post-conventional moral reasoning equivalent to graduate school students; GPT-3 performs at random baseline

---

### 1.5 Moral Foundations of Large Language Models

- **Full Citation:** Marwa Abdulhai, Gregory Serapio-Garcia, Clement Crepy, Daria Valter, John Canny, Natasha Jaques. "Moral Foundations of Large Language Models." EMNLP 2024, pages 17737-17752.
- **DOI:** 10.18653/v1/2024.emnlp-main.982
- **Ethical Frameworks:** Moral Foundations Theory (5 factors: care/harm, fairness/cheating, loyalty/betrayal, authority/subversion, sanctity/degradation, plus liberty/oppression)
- **Dataset Size & Format:** Survey-based and adversarial prompt evaluation; measures consistency of moral biases across contexts
- **Code/Data URLs:** Not publicly listed in ACL Anthology page
- **LLMs Tested:** GPT-3 variants (curie, babbage, davinci)
- **Implementation Readiness:** **Medium** -- methodology is detailed and reproducible; applies established MFT framework to LLMs
- **Key Finding:** LLMs exhibit particular moral foundations; adversarial prompts can shift model moral foundations and affect downstream task behavior

---

### 1.6 The Convergent Ethics of AI (PRIME Framework)

- **Full Citation:** Chad Coleman, W. Russell Neuman, Ali Dasdan, Safinah Ali, Manan Shah. "The Convergent Ethics of AI? Analyzing Moral Foundation Priorities in Large Language Models with a Multi-Framework Approach." arXiv preprint, 2025.
- **arXiv ID:** 2504.19255
- **Ethical Frameworks:** PRIME (Priorities in Reasoning and Intrinsic Moral Evaluation) framework; integrates consequentialist-deontological reasoning, Moral Foundations Theory, and Kohlberg's developmental stages
- **Dataset Size & Format:** Dual-protocol approach combining direct questioning and response analysis to established ethical dilemmas
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** 6 leading LLMs (specific names in paper)
- **Implementation Readiness:** **Medium** -- comprehensive multi-framework approach; methodology is detailed but no public code
- **Key Finding:** All models converge on prioritizing care/harm and fairness/cheating foundations while underweighting authority, loyalty, and sanctity

---

### 1.7 MFTCXplain: Multilingual Moral Foundations Benchmark

- **Full Citation:** Jackson Trager, Francielle Vargas, Diego Alves, Matteo Guida, Mikel K. Ngueajio, Ameeta Agrawal, Yalda Daryani, Farzan Karimi-Malekabadi, Flor Miriam Plaza-del-Arco. "MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation." Findings of EMNLP 2025.
- **arXiv ID:** 2506.19073
- **Ethical Frameworks:** Moral Foundation Theory (MFT); multi-hop moral reasoning through hate speech explanation
- **Dataset Size & Format:** 3,000 tweets across 4 languages (Portuguese, Italian, Persian, English); annotated with binary hate speech labels, moral categories, and text span-level rationales
- **Code/Data URLs:** Not publicly listed at time of search
- **LLMs Tested:** Multiple LLMs (specific names in paper)
- **Implementation Readiness:** **High** -- clearly defined multilingual dataset with structured annotation schema
- **Key Finding:** LLMs achieve strong hate speech detection (F1 up to 0.836) but poor moral sentiment prediction (F1 < 0.35)

---

### 1.8 EMNLP: Educator-role Moral and Normative LLMs Profiling

- **Full Citation:** Yilin Jiang, Mingzi Zhang, Sheng Jin, Zengyi Yu, Xiangjie Kong, Binghao Tu. "EMNLP: Educator-role Moral and Normative Large Language Models Profiling." EMNLP 2025 Main Conference.
- **arXiv ID:** 2508.15250
- **DOI:** 10.18653/v1/2025.emnlp-main.42
- **Ethical Frameworks:** Kohlberg's moral development stages; personality profiling; profession-specific (educator) moral dilemma evaluation; soft prompt injection vulnerability assessment
- **Dataset Size & Format:** 88 teacher-specific moral dilemmas; personality profiling scales; prompt injection evaluation set
- **Code/Data URLs:** https://e-m-n-l-p.github.io/
- **LLMs Tested:** 14 LLMs
- **Implementation Readiness:** **High** -- resources publicly available; first benchmark for educator-role LLM ethical/psychological alignment
- **Key Finding:** Teacher-role LLMs exhibit idealized/polarized personalities; excel at abstract moral reasoning but struggle with emotionally complex situations; models with stronger reasoning are more vulnerable to harmful prompt injection

---

## Section 2: Value Measurement & Consistency

### 2.1 Value FULCRA

- **Full Citation:** Jing Yao, Xiaoyuan Yi, Xiting Wang, Yifan Gong, Xing Xie. "Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Values." NAACL 2024, pages 8762-8785.
- **arXiv ID:** 2311.10766
- **Ethical Frameworks:** Schwartz's Theory of Basic Values (10 value dimensions: self-direction, stimulation, hedonism, achievement, power, security, conformity, tradition, benevolence, universalism)
- **Dataset Size & Format:** 20,000 (LLM output, value vector) pairs mapping LLM outputs to multidimensional value space; includes BaseAlign alignment method
- **Code/Data URLs:** Available via ACL Anthology supplementary materials
- **LLMs Tested:** Multiple LLMs (details in paper)
- **Implementation Readiness:** **High** -- large dataset; established theoretical grounding in Schwartz values; published at top venue
- **Confirmed Status:** Exists and published at NAACL 2024
- **Key Finding:** Basic values effectively distinguish safe/unsafe behaviors; different safety risks are clarified in the value space; can identify new types of risks

---

### 2.2 Value Portrait

- **Full Citation:** Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo. "Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items." ACL 2025 Long Paper.
- **arXiv ID:** 2505.01015
- **Ethical Frameworks:** Schwartz's Theory of Basic Values; psychometric validation; ecological validity through real-life user-LLM interactions
- **Dataset Size & Format:** Psychometrically validated items with human-subject correlation data; evaluates 10 Schwartz value dimensions
- **Code/Data URLs:** Not publicly listed at time of search
- **LLMs Tested:** 44 language models
- **Implementation Readiness:** **High** -- large-scale evaluation across 44 models; psychometric validation ensures reliability
- **Key Finding:** Models prioritize Benevolence, Security, and Self-Direction; underweight Tradition, Power, and Achievement; biases in demographic group perception

---

### 2.3 ValueActionLens (Mind the Value-Action Gap)

- **Full Citation:** Hua Shen, Nicholas Clark, Tanushree Mitra. "Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?" EMNLP 2025 Main Track.
- **arXiv ID:** 2501.15463
- **Ethical Frameworks:** Value-action alignment; Schwartz values across 12 cultures; 11 social topics
- **Dataset Size & Format:** VIA (Value-Informed Dataset) containing 14,800 value-informed actions spanning 12 cultures and 11 social topics; 132 scenarios
- **Code/Data URLs:** GitHub: https://github.com/huashen218/value_action_gap (data in /outputs/data_release)
- **LLMs Tested:** GPT-4o-mini, GPT-4o, GPT-3.5-turbo, Gemma-2-9B, Llama-3.3-70B, Deepseek-r1-distill-llama-70b, and others
- **Implementation Readiness:** **High** -- code and data publicly available; well-defined alignment metrics
- **Key Finding:** Leveraging reasoned explanations improves value-action alignment performance

---

### 2.4 Deep Value Benchmark

- **Full Citation:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak. "Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences." NeurIPS 2025 (Spotlight).
- **arXiv ID:** 2511.02109
- **Ethical Frameworks:** Deep values vs. shallow preferences; Deep Value Generalization Rate (DVGR) metric; controlled confounding experimental design
- **Dataset Size & Format:** Dataset with controlled confounds between deep values and shallow features; three separate human validation experiments
- **Code/Data URLs:** Dataset released (specific URL in paper)
- **LLMs Tested:** 9 models
- **Implementation Readiness:** **High** -- NeurIPS Spotlight; novel metric (DVGR); dataset released with human validation
- **Confirmed Status:** Exists and published
- **Key Finding:** Average DVGR is only 0.30 -- all models generalize deep values less than chance; larger models have slightly lower DVGR

---

### 2.5 Do LLMs Have Consistent Values?

- **Full Citation:** Naama Rozen, Liat Bezalel, Gal Elidan, Amir Globerson, Ella Daniel. "Do LLMs Have Consistent Values?" ICLR 2025 Conference Paper.
- **arXiv ID:** 2407.12878
- **Ethical Frameworks:** Human value structure consistency; Schwartz value theory; Value Anchoring prompting strategy
- **Dataset Size & Format:** Survey-based evaluation measuring value correlations within single sessions; tests whether LLMs produce human-like value personas
- **Code/Data URLs:** Not publicly listed at time of search
- **LLMs Tested:** GPT-4-0314, Gemini 1.0 Pro, Llama 3.1 8B, Llama 3.1 70B, Gemma 2 9B, Gemma 2 27B
- **Implementation Readiness:** **High** -- published at ICLR 2025; introduces reproducible "Value Anchoring" methodology
- **Key Finding:** Standard prompting fails to produce human-consistent value correlations; Value Anchoring significantly improves alignment with human value structure

---

### 2.6 Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs (ValAct-15k)

- **Full Citation:** Jen-tse Huang, Jiantong Qin, Xueli Qiu, Sharon Levy, Michelle R. Kaufman, Mark Dredze. "Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs." arXiv preprint, 2026.
- **arXiv ID:** 2601.07972
- **Ethical Frameworks:** Schwartz Theory of Basic Human Values (10 values); knowledge-action gap in moral reasoning
- **Dataset Size & Format:** ValAct-15k: 3,000 advice-seeking scenarios derived from Reddit; 55 human participants for comparison
- **Code/Data URLs:** Not publicly listed at time of search
- **LLMs Tested:** 10 frontier LLMs (5 US companies, 5 Chinese companies)
- **Implementation Readiness:** **High** -- large dataset; cross-cultural LLM comparison; clear evaluation protocol
- **Key Finding:** Near-perfect cross-model consistency (Pearson r ~ 1.0) contrasts with human variability (r in [-0.79, 0.98]); both humans and LLMs show weak correspondence between self-reported and enacted values (r = 0.4, 0.3)

---

### 2.7 The Moral Consistency Pipeline (MoCoP)

- **Full Citation:** Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Negar Shahabi, Foutse Khomh. "The Moral Consistency Pipeline: Continuous Ethical Evaluation for Large Language Models." arXiv preprint, 2025.
- **arXiv ID:** 2512.03026
- **Ethical Frameworks:** Moral consistency / moral drift detection; lexical integrity analysis; semantic risk estimation; reasoning-based judgment modeling
- **Dataset Size & Format:** Dataset-free, closed-loop framework; autonomously generates, evaluates, and refines ethical scenarios
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** GPT-4-Turbo, DeepSeek
- **Implementation Readiness:** **Medium** -- novel dataset-free approach; demonstrated on limited models; methodology detailed but no public code
- **Key Finding:** Inverse correlation (rET = -0.81) between ethical and toxicity dimensions; effective at measuring ethical consistency, linguistic safety, and temporal invariance

---

### 2.8 Robustness of Large Language Models in Moral Judgements

- **Full Citation:** Soyoung Oh, Vera Demberg. "Robustness of Large Language Models in Moral Judgements." Royal Society Open Science, 12(4), 241229, 2025.
- **DOI:** 10.1098/rsos.241229
- **Ethical Frameworks:** Moral Machine task; robustness and consistency of moral judgments; prompt sensitivity analysis
- **Dataset Size & Format:** Moral Machine dilemmas with systematic prompt variations (label format, ordering)
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** Multiple LLMs (specific names in paper)
- **Implementation Readiness:** **Medium** -- well-documented methodology; established venue; highlights fundamental issues with prompt-based moral evaluation
- **Key Finding:** LLM moral judgments are highly sensitive to superficial prompt changes (e.g., switching "Case 1/Case 2" to "(A)/(B)" reverses decisions); previous moral machine results may be prompt artifacts

---

## Section 3: Narrative & Scenario-Based Moral Reasoning

### 3.1 Normative Evaluation with Everyday Moral Dilemmas

- **Full Citation:** Pratik S. Sachdeva, Tom van Nuenen. "Normative Evaluation of Large Language Models with Everyday Moral Dilemmas." ACM FAccT 2025.
- **arXiv ID:** 2501.18081
- **DOI:** 10.1145/3715275.3732044
- **Ethical Frameworks:** Normative ethics; everyday moral reasoning; blame attribution; Reddit AITA community standards
- **Dataset Size & Format:** 10,000+ moral dilemmas from Reddit "Am I the Asshole" (AITA); blame assignment and explanation generation tasks
- **Code/Data URLs:** GitHub: https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas
- **LLMs Tested:** 7 commonly used LLMs (proprietary and open-source)
- **Implementation Readiness:** **High** -- large dataset; public code; published at top fairness venue
- **Key Finding:** LLMs exhibit distinct moral judgment patterns varying substantially from humans; moderate to high self-consistency but low inter-model agreement; ensemble of LLMs approximates human consensus

---

### 3.2 Evaluating Moral Beliefs across LLMs through a Pluralistic Framework

- **Full Citation:** Xuelin Liu, Yanfei Zhu, Shucheng Zhu, Pengyuan Liu, Ying Liu, Dong Yu. "Evaluating Moral Beliefs across LLMs through a Pluralistic Framework." Findings of EMNLP 2024.
- **arXiv ID:** 2411.03665
- **Ethical Frameworks:** Pluralistic moral evaluation; moral choice, moral rank, and moral reasoning modules; cross-cultural moral comparison (Chinese moral context)
- **Dataset Size & Format:** 472 moral choice scenarios in Chinese derived from moral words; three evaluation modules
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** ChatGPT, Gemini, Ernie, ChatGLM
- **Implementation Readiness:** **Medium** -- Chinese-language focused; smaller dataset; novel pluralistic methodology
- **Key Finding:** Western models (ChatGPT, Gemini) mirror Chinese student moral decisions; Chinese models (Ernie, ChatGLM) show different collectivist moral orientations

---

### 3.3 The Greatest Good Benchmark (Utilitarian Moral Dilemmas)

- **Full Citation:** Giovanni Franco Gabriel Marraffini, Andres Cotton, Noe Fabian Hsueh, Axel Fridman, Juan Wisznia, Luciano Del Corro. "The Greatest Good Benchmark: Measuring LLMs' Alignment with Utilitarian Moral Dilemmas." EMNLP 2024, pages 21950-21959.
- **arXiv ID:** 2503.19598
- **Ethical Frameworks:** Utilitarianism; Oxford Utilitarianism Scale (OUS); impartial beneficence; instrumental harm
- **Dataset Size & Format:** Adapted and expanded Oxford Utilitarianism Scale items for LLM evaluation
- **Code/Data URLs:** GitHub: https://github.com/noehsueh/greatest-good-benchmark
- **LLMs Tested:** 15 diverse LLMs
- **Implementation Readiness:** **High** -- public code; grounded in validated cognitive science instrument (OUS); tested across many models
- **Key Finding:** LLMs have consistently encoded moral preferences diverging from established moral theories and lay population standards; marked preference for impartial beneficence and rejection of instrumental harm

---

### 3.4 The Pluralistic Moral Gap

- **Full Citation:** Giuseppe Russo, Debora Nozza, Paul Rottger, Dirk Hovy. "The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and Large Language Models." arXiv preprint, 2025.
- **arXiv ID:** 2507.17216
- **Ethical Frameworks:** Moral pluralism; 60-value taxonomy; Dynamic Moral Profiling (DMP)
- **Dataset Size & Format:** 1,618 real-world moral dilemmas with distributions of human moral judgments; 60-value taxonomy from 3,783 value expressions extracted from human rationales
- **Code/Data URLs:** Not publicly listed at time of search; CC-BY 4.0 license
- **LLMs Tested:** Multiple LLMs (specific names in paper)
- **Implementation Readiness:** **High** -- large annotated dataset; novel 60-value taxonomy; DMP methodology improves alignment by 64.3%
- **Key Finding:** LLMs reproduce human judgments only under high consensus; alignment deteriorates with human disagreement; LLMs rely on narrower set of moral values than humans

---

### 3.5 Conscience Conflict: Evaluating Language Models' Moral Understanding

- **Full Citation:** Authors not fully specified in search results. "Conscience Conflict? Evaluating Language Models' Moral Understanding." CEUR Workshop Proceedings, Vol. 4004, 2024.
- **URL:** https://ceur-ws.org/Vol-4004/paper3.pdf
- **Ethical Frameworks:** Multi-theory ethical evaluation; consequentialism, deontology, virtue ethics; free-text moral justification analysis
- **Dataset Size & Format:** 6 human-authored, high-stakes moral dilemmas; each with 3 mutually exclusive decisions requiring both choice and free-text justification
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** 5 open-source LLMs
- **Implementation Readiness:** **Medium** -- small dataset but unique evaluation methodology requiring both decisions and rationales
- **Key Finding:** Models shift inconsistently between ethical frameworks; moral justifications are often erratic, shallow, or contradictory across similar dilemmas

---

### 3.6 Large Language Models Show Amplified Cognitive Biases in Moral Decision-Making

- **Full Citation:** Cristina Cechella and colleagues. "Large Language Models Show Amplified Cognitive Biases in Moral Decision-Making." PNAS, 2025.
- **DOI:** 10.1073/pnas.2412015122
- **Ethical Frameworks:** Omission bias; yes-no bias; cognitive biases in moral judgment; comparison with human moral cognition
- **Dataset Size & Format:** Experimental moral dilemma scenarios with systematic bias measurements
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** GPT-4-turbo, GPT-4o, Llama 3.1-Instruct, Claude 3.5 Sonnet
- **Implementation Readiness:** **Medium** -- published in top science journal; experimental design is reproducible; highlights important bias considerations
- **Key Finding:** LLMs exhibit amplified omission bias compared to humans; novel yes-no bias found in 3/4 LLMs (not found in humans); biases likely introduced during fine-tuning

---

## Section 4: Meta-Ethics & Moral Epistemology

### 4.1 Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants (AMAeval)

- **Full Citation:** Alessio Galatolo, Luca Alberto Rappuoli, Katie Winkle, Meriem Beloucif. "Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants." ECAI 2025.
- **arXiv ID:** 2508.12754
- **Ethical Frameworks:** Deductive and abductive moral reasoning; moral sensitivity; ethical problem recognition; conflicting value navigation
- **Dataset Size & Format:** AMAeval benchmark testing multiple moral reasoning competencies
- **Code/Data URLs:** GitHub: https://github.com/alessioGalatolo/AMAeval
- **LLMs Tested:** Popular open LLMs (specific names in paper)
- **Implementation Readiness:** **High** -- public code; published at major AI conference; tests distinct moral reasoning capabilities
- **Key Finding:** Most models struggle with abductive reasoning; evaluation and generation are distinct capabilities -- strong performance in one does not imply the other

---

### 4.2 Discerning What Matters: Multi-Dimensional Moral Competence Assessment

- **Full Citation:** Daniel Kilov, Caroline Hendy, Secil Yanik Guyot, Aaron J. Snoswell, Seth Lazar. "Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs." arXiv preprint, 2025.
- **arXiv ID:** 2506.13082
- **Ethical Frameworks:** Five dimensions of moral competence: (1) identifying morally relevant features, (2) weighting importance, (3) assigning moral reasons, (4) synthesizing coherent judgments, (5) recognizing information gaps
- **Dataset Size & Format:** Two experiments: standard ethical vignettes and novel scenarios with embedded irrelevant details; comparisons with non-expert humans and professional philosophers
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** 6 leading LLMs
- **Implementation Readiness:** **Medium** -- novel multi-dimensional framework; clear experimental design but no public dataset
- **Key Finding:** LLMs outperform humans on standard vignettes but perform significantly worse on novel scenarios with noise, suggesting current evaluations substantially overestimate LLM moral reasoning

---

### 4.3 Structured Moral Reasoning: A Value-Grounded Evaluation Framework

- **Full Citation:** Mohna Chakraborty, Lu Wang, David Jurgens. "Structured Moral Reasoning in Language Models: A Value-Grounded Evaluation Framework." EMNLP 2025 Main Conference.
- **arXiv ID:** 2506.14948
- **Ethical Frameworks:** Schwartz's value framework; care ethics; consequentialism; deontology; first-principles reasoning; cognitive reasoning strategies
- **Dataset Size & Format:** Benchmarked across 4 moral datasets using taxonomy of prompts grounded in value systems
- **Code/Data URLs:** Not publicly listed at time of search
- **LLMs Tested:** 12 open-source models
- **Implementation Readiness:** **High** -- tested across multiple datasets and models; includes supervised distillation for small models
- **Key Finding:** Explicit moral structure in prompting consistently improves accuracy and coherence; first-principles reasoning and Schwartz + care-ethics scaffolds yield strongest gains; moral competence can be distilled from large to small models

---

### 4.4 Beyond Verdicts: Evaluating Language Model Moral Competence (Survey/Framework)

- **Full Citation:** Aaron J. Snoswell, Daniel Kilov, Seth Lazar. "Beyond Verdicts: Evaluating Language Model Moral Competence." AAAI 2026 AI Alignment Track (forthcoming).
- **URL:** https://philarchive.org/archive/SNOBVE
- **Ethical Frameworks:** Meta-evaluation taxonomy covering moral sensitivity, reasoning quality, steerability, moral pluralism; surveys 69 papers (2020-2025) on LLM ethical evaluation
- **Dataset Size & Format:** Survey paper; taxonomy categorizing evaluations across datasets, behaviors, and metrics
- **Code/Data URLs:** Not applicable (survey/framework paper)
- **LLMs Tested:** N/A (meta-analysis)
- **Implementation Readiness:** **Medium** (framework) -- provides critical guidance for benchmark design rather than a benchmark itself
- **Key Finding:** Current evaluations overemphasize verdict accuracy; fail to test moral sensitivity in noisy contexts; most rely on "ground truth" despite philosophical objections to definitive moral ground truth

---

### 4.5 Addressing Moral Uncertainty using LLMs for Ethical Decision-Making

- **Full Citation:** Rohit K. Dubey, Damian Dailisan, Sachit Mahajan. "Addressing Moral Uncertainty using Large Language Models for Ethical Decision-Making." arXiv preprint, 2025.
- **arXiv ID:** 2503.05724
- **Ethical Frameworks:** Multi-perspective moral uncertainty: consequentialism, deontology, virtue ethics, social justice, care ethics; Belief Jensen-Shannon Divergence; Dempster-Shafer Theory
- **Dataset Size & Format:** RL-based ethical decision-making framework with LLM-generated moral belief scores
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** Multiple LLM variants (specific names in paper)
- **Implementation Readiness:** **Medium** -- novel integration of RL with multi-perspective moral reasoning; more of a framework than a static benchmark
- **Key Finding:** Integrated framework helps RL agent navigate moral uncertainty; demonstrates improved consistency and reduced reliance on handcrafted ethical rewards

---

### 4.6 On the Convergence of Moral Self-Correction in LLMs

- **Full Citation:** Guangliang Liu, Haitao Mao, Bochuan Cao, Zhiyu Xue, Xitong Zhang, Rongrong Wang, Kristen Marie Johnson. "On the Convergence of Moral Self-Correction in Large Language Models." AACL-IJCNLP 2025.
- **arXiv ID:** 2510.07290
- **Ethical Frameworks:** Intrinsic moral self-correction; moral concept activation; model uncertainty reduction; multi-round moral convergence
- **Dataset Size & Format:** Multi-choice QA and language generation tasks; uses semantic uncertainty as uncertainty estimator
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** Multiple LLMs (specific names in paper)
- **Implementation Readiness:** **Medium** -- demonstrates convergence mechanism; reproducible methodology but no public benchmark
- **Key Finding:** Performance convergence achievable within ~6 rounds of self-correction; self-correction instructions activate moral concepts that reduce model uncertainty

---

### 4.7 Large Language Models Meet Moral Values: Comprehensive Assessment

- **Full Citation:** Luana Bulla, Misael Mongiovi, Stefano De Giorgis, Aldo Gangemi. "Large Language Models Meet Moral Values: A Comprehensive Assessment of Moral Abilities." Telematics and Informatics, 2025.
- **DOI:** Available via ScienceDirect (S2451958825000247)
- **Ethical Frameworks:** Moral Foundation Theory; unsupervised moral classification; Moral Foundation Reddit Corpus (MFRC)
- **Dataset Size & Format:** Uses MFRC for evaluation; multi-label and binary classification scenarios
- **Code/Data URLs:** GitHub: https://github.com/LuanaBulla/Detection-of-Morality-in-Text
- **LLMs Tested:** Multiple LLM sizes with different prompt designs
- **Implementation Readiness:** **High** -- public code; uses established MFRC dataset; systematic evaluation across LLM sizes and prompt strategies
- **Key Finding:** Directly compares model outputs with human annotations; explores effectiveness of different LLM sizes and prompt designs for moral value detection

---

### 4.8 Diagnosing Moral Reasoning Acquisition in Language Models

- **Full Citation:** Guangliang Liu, Zimo Qi, Xitong Zhang, Lei Jiang, Kristen Johnson. "Diagnosing Moral Reasoning Acquisition in Language Models: Pragmatics and Generalization." Findings of EMNLP 2025.
- **URL:** https://aclanthology.org/2025.findings-emnlp.374.pdf
- **Ethical Frameworks:** Moral Foundation Theory; Rules of Thumb (RoTs) moral classification; moral reasoning acquisition through fine-tuning
- **Dataset Size & Format:** Uses SocialChem and MIC benchmarks; moral classification to moral foundations
- **Code/Data URLs:** Not publicly listed
- **LLMs Tested:** Multiple models with various fine-tuning strategies
- **Implementation Readiness:** **Medium** -- uses existing datasets; provides diagnostic framework for understanding moral reasoning acquisition
- **Key Finding:** "moral-rot" fine-tuning strategy achieves optimal performance; introducing more moral information improves performance

---

## Confirmation Status for Requested Benchmarks

| Benchmark | Status | Notes |
|-----------|--------|-------|
| Dynamic Moral Reasoning / Staircase of Ethics | **CONFIRMED** | Paper 1.1; 3,302 five-stage dilemmas; EMNLP 2025 |
| Moral Uncertainty (32 models, 9 dimensions) | **NOT FOUND as described** | No benchmark matching exactly "32 models, 9 dimensions" found; closest is Deep Value Benchmark (9 models) or MoralBench |
| Value FULCRA | **CONFIRMED** | Paper 2.1; 20,000 pairs; NAACL 2024 |
| LocalValueBench | **Already in known list** | Excluded per instructions |
| Moral Foundations Questionnaire adaptations | **CONFIRMED** | Papers 1.2, 1.3, 1.5, 1.6, 1.7 |
| Kohlberg moral development assessments | **CONFIRMED** | Papers 1.4, 1.6, 1.8 |
| Defining Issues Test (DIT) | **CONFIRMED** | Paper 1.4; arXiv 2309.13356 |
| Value Portrait | **CONFIRMED** | Paper 2.2; 44 LLMs; ACL 2025 |
| Value-Spectrum | **NOT FOUND** | No paper with this exact name identified |
| ValueActionLens | **CONFIRMED** | Paper 2.3; EMNLP 2025; 14.8k items |
| Deep Value Benchmark | **CONFIRMED** | Paper 2.4; NeurIPS 2025 Spotlight |

---

## Summary Table: Implementation Readiness

| # | Benchmark | Venue | Readiness | Public Code/Data |
|---|-----------|-------|-----------|-----------------|
| 1.1 | Staircase of Ethics | EMNLP 2025 | High | Pending |
| 1.2 | MoralBench | KDD Explorations 2025 | High | Yes |
| 1.3 | LLM Ethics Benchmark | Sci. Reports 2025 | High | Yes |
| 1.4 | DIT for LLMs | arXiv 2023 | Medium | No |
| 1.5 | Moral Foundations of LLMs | EMNLP 2024 | Medium | No |
| 1.6 | PRIME Framework | arXiv 2025 | Medium | No |
| 1.7 | MFTCXplain | EMNLP Findings 2025 | High | Pending |
| 1.8 | EMNLP (Educator) | EMNLP 2025 | High | Yes |
| 2.1 | Value FULCRA | NAACL 2024 | High | Yes |
| 2.2 | Value Portrait | ACL 2025 | High | Pending |
| 2.3 | ValueActionLens | EMNLP 2025 | High | Yes |
| 2.4 | Deep Value Benchmark | NeurIPS 2025 | High | Yes |
| 2.5 | Do LLMs Have Consistent Values? | ICLR 2025 | High | Pending |
| 2.6 | ValAct-15k | arXiv 2026 | High | Pending |
| 2.7 | MoCoP | arXiv 2025 | Medium | No |
| 2.8 | Robustness in Moral Judgements | RSOS 2025 | Medium | No |
| 3.1 | Normative Eval (AITA) | FAccT 2025 | High | Yes |
| 3.2 | Pluralistic Moral Beliefs | EMNLP Findings 2024 | Medium | No |
| 3.3 | Greatest Good Benchmark | EMNLP 2024 | High | Yes |
| 3.4 | Pluralistic Moral Gap | arXiv 2025 | High | Pending |
| 3.5 | Conscience Conflict | CEUR 2024 | Medium | No |
| 3.6 | Amplified Cognitive Biases | PNAS 2025 | Medium | No |
| 4.1 | AMAeval | ECAI 2025 | High | Yes |
| 4.2 | Discerning What Matters | arXiv 2025 | Medium | No |
| 4.3 | Structured Moral Reasoning | EMNLP 2025 | High | Pending |
| 4.4 | Beyond Verdicts (Survey) | AAAI 2026 | Medium | N/A |
| 4.5 | Moral Uncertainty (RL) | arXiv 2025 | Medium | No |
| 4.6 | Moral Self-Correction | AACL-IJCNLP 2025 | Medium | No |
| 4.7 | LLMs Meet Moral Values | Telematics & Informatics 2025 | High | Yes |
| 4.8 | Diagnosing Moral Reasoning | EMNLP Findings 2025 | Medium | No |

---

## Key GitHub/HuggingFace Resources

| Resource | URL |
|----------|-----|
| MoralBench | https://github.com/agiresearch/MoralBench |
| LLM Ethics Benchmark | https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark |
| ValueActionLens / Value-Action Gap | https://github.com/huashen218/value_action_gap |
| AMAeval | https://github.com/alessioGalatolo/AMAeval |
| Greatest Good Benchmark | https://github.com/noehsueh/greatest-good-benchmark |
| Normative Eval (AITA dilemmas) | https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas |
| EMNLP (Educator) Resources | https://e-m-n-l-p.github.io/ |
| Detection of Morality in Text | https://github.com/LuanaBulla/Detection-of-Morality-in-Text |

---

## Notes on Items Not Found

1. **"Moral Uncertainty (32 models, 9 dimensions)"**: No benchmark matching this exact description was found. The closest candidate is the Deep Value Benchmark (9 models, DVGR metric) or MoralBench (multiple models, 6 moral foundations). It is possible this refers to an internal or forthcoming benchmark.

2. **"Value-Spectrum"**: No paper with this exact name was identified in the search. The closest matches are Value FULCRA (maps LLMs to multidimensional value spectrum) and ValueBench (already in the known list).

3. **Moral realism vs. anti-realism benchmark**: No dedicated benchmark for testing LLM meta-ethical positions (moral realism vs. anti-realism) was found. The "Beyond Verdicts" survey paper discusses meta-ethical considerations but is a framework paper, not a benchmark.

---

*Report generated by Agent 19 on 2026-02-07. All arXiv IDs and DOIs verified at time of search.*
