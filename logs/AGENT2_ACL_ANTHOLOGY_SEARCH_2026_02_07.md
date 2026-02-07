# Agent 2: ACL Anthology Systematic Search Results
## Ethical Values Alignment Benchmarks/Datasets for LLMs
### Date: 2026-02-07

---

## Search Strategy Executed

1. Searched ACL Anthology for: "moral benchmark", "ethics evaluation LLM", "value alignment dataset", "moral reasoning benchmark"
2. Searched specific venues: ACL 2023-2025, EMNLP 2023-2025, NAACL 2024-2025, EACL 2024, LREC-COLING 2024, COLING 2025, AACL-IJCNLP 2025
3. Searched C3NLP Workshop papers (Cross-Cultural Considerations in NLP) 2023-2025
4. Searched NLP4PI Workshop (NLP for Positive Impact) 2024-2025
5. Searched WOAH Workshop (Online Abuse and Harms) 2024-2025
6. Searched Findings papers (Findings of ACL, Findings of EMNLP, Findings of NAACL)
7. Searched for "human values", "Schwartz", "moral foundations", "pluralistic alignment" across venues
8. Total web searches conducted: 20

---

## NEW Papers Found (Not in Known List)

---

### Paper 1: CMoralEval

**Full Citation:** Linhao Yu, Yongqi Leng, Yufei Huang, Shang Wu, Haixin Liu, Xinmeng Ji, Jiahui Zhao, Jinwang Song, Tingting Cui, Xiaoqing Cheng, Tao Liu, Deyi Xiong (2024). "CMoralEval: A Moral Evaluation Benchmark for Chinese Large Language Models." Findings of the Association for Computational Linguistics: ACL 2024, pages 11817-11837, Bangkok, Thailand.

**ACL Anthology URL:** https://aclanthology.org/2024.findings-acl.703/
**DOI:** 10.18653/v1/2024.findings-acl.703

**Ethical Frameworks Covered:**
- Chinese traditional moral taxonomy integrated with contemporary societal norms
- Explicit moral scenarios (right vs. wrong) and moral dilemma scenarios (competing principles)

**Dataset Details:**
- Size: 30,388 instances total (14,964 explicit moral scenarios + 15,424 moral dilemma scenarios)
- Format: Structured benchmark with annotated moral scenarios
- Languages: Chinese
- Data sources: Chinese TV program on moral norms; collection of Chinese moral anomies from newspapers and academic papers

**Code/Data URLs:** Not publicly listed in paper metadata
**LLMs Tested:** Multiple Chinese LLMs (extensive experiments, specific models in full paper)
**Implementation Readiness:** HIGH - Large dataset, clear evaluation protocol, well-structured scenarios
**What Makes It Unique:** First large-scale Chinese moral evaluation benchmark rooted in Chinese cultural moral norms rather than Western ethics frameworks; distinguishes between explicit moral judgments and genuine moral dilemmas.

---

### Paper 2: KorNAT

**Full Citation:** Jiyoung Lee, Minwoo Kim, Seungho Kim, Junghwan Kim, Seunghyun Won, Hwaran Lee, Edward Choi (2024). "KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge." Findings of the Association for Computational Linguistics: ACL 2024, pages 11177-11213, Bangkok, Thailand.

**ACL Anthology URL:** https://aclanthology.org/2024.findings-acl.666/
**DOI:** 10.18653/v1/2024.findings-acl.666

**Ethical Frameworks Covered:**
- Korean social values alignment (grounded in large-scale public survey of South Korean population)
- Common knowledge alignment with Korean cultural norms

**Dataset Details:**
- Size: 10,000 multiple-choice questions (4,000 on social values + 6,000 on common knowledge)
- Format: Multiple-choice questions with statistically calibrated ground truth
- Languages: Korean
- Data sources: Large-scale public survey with 6,174 South Korean participants; Korean textbooks and GED exams

**Code/Data URLs:** Not publicly listed in paper metadata
**LLMs Tested:** 7 LLMs evaluated (specific models in full paper)
**Implementation Readiness:** HIGH - Large MC dataset, clear evaluation metrics, survey-grounded ground truth
**What Makes It Unique:** First benchmark measuring national alignment between LLMs and South Korea; uses statistical sampling theory for ground truth calibration from actual population surveys.

---

### Paper 3: UniMoral (ACL 2025 Best Resource Paper)

**Full Citation:** Shivani Kumar, David Jurgens (2025). "Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral." Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5890-5912, Vienna, Austria.

**ACL Anthology URL:** https://aclanthology.org/2025.acl-long.294/

**Ethical Frameworks Covered:**
- Deontology, Utilitarianism, Rights-Based Ethics, Virtue Ethics
- Ethical Principle Ratings across four traditions
- 8 Contributing Factor Ratings
- Cultural relativity of moral reasoning

**Dataset Details:**
- Size: 8,784 instances
- Format: Moral dilemmas annotated with action choices, ethical principles, contributing factors, consequences, plus annotators' moral and cultural profiles
- Languages: 6 languages -- Arabic, Chinese, English, Hindi, Russian, Spanish
- Sources: Integrated from psychologically grounded scenarios and social-media-derived moral dilemmas

**Code/Data URLs:** Not listed in metadata (ACL 2025 Best Resource Paper -- likely released)
**LLMs Tested:** 3 LLMs benchmarked across 4 tasks: action prediction, moral typology classification, factor attribution analysis, consequence generation
**Implementation Readiness:** HIGH - Large multilingual dataset, four distinct evaluation tasks, won Best Resource Paper at ACL 2025
**What Makes It Unique:** Most comprehensive multilingual moral reasoning benchmark; treats moral reasoning as a computational pipeline rather than binary classification; includes annotator moral and cultural profiles for studying individual variation.

---

### Paper 4: Flames

**Full Citation:** Kexin Huang, Xiangyang Liu, Qianyu Guo, Tianxiang Sun, Jiawei Sun, Yaru Wang, Zeyang Zhou, Yixu Wang, Yan Teng, Xipeng Qiu, Yingchun Wang, Dahua Lin (2024). "Flames: Benchmarking Value Alignment of LLMs in Chinese." Proceedings of NAACL 2024 (Volume 1: Long Papers), pages 4551-4591, Mexico City, Mexico.

**ACL Anthology URL:** https://aclanthology.org/2024.naacl-long.256/

**Ethical Frameworks Covered:**
- Harmlessness principles
- Chinese cultural values (harmony)
- Safety dimension
- Fairness dimension
- Morality dimension integrating specific Chinese values

**Dataset Details:**
- Size: Adversarial prompts and annotated responses (details in full paper)
- Format: Adversarial prompt-response evaluation
- Languages: Chinese

**Code/Data URLs:** https://github.com/AIFlames/Flames
**LLMs Tested:** 17 mainstream LLMs
**Implementation Readiness:** HIGH - GitHub code available, 17 LLMs tested, clear evaluation framework
**What Makes It Unique:** Adversarial evaluation approach; integrates Chinese-specific cultural values (harmony) alongside universal safety principles; all evaluated LLMs showed poor performance, indicating genuine challenge beyond existing benchmarks.

---

### Paper 5: Value FULCRA

**Full Citation:** Jing Yao, Xiaoyuan Yi, Yifan Gong, Xiting Wang, Xing Xie (2024). "Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value." Proceedings of NAACL 2024, pages 8762-8785, Mexico City, Mexico.

**ACL Anthology URL:** https://aclanthology.org/2024.naacl-long.486/
**DOI:** 10.18653/v1/2024.naacl-long.486

**Ethical Frameworks Covered:**
- Schwartz's Theory of Basic Values (10-dimensional value space)
- BaseAlign paradigm using anthropologically-grounded value dimensions

**Dataset Details:**
- Size: 20,000 (LLM output, value vector) pairs
- Format: Structured pairs mapping LLM outputs to 10 value dimensions
- Languages: Not explicitly specified

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** Multiple LLMs (details in full paper)
**Implementation Readiness:** HIGH - Large dataset, grounded in established Schwartz theory, clear multidimensional evaluation
**What Makes It Unique:** Maps LLMs to Schwartz's established 10-dimensional value space rather than ad-hoc ethical categories; proposes BaseAlign paradigm for alignment using validated anthropological value dimensions.

---

### Paper 6: Multilingual Defining Issues Test

**Full Citation:** Aditi Khandelwal, Utkarsh Agarwal, Kumar Tanmay, Monojit Choudhury (2024). "Do Moral Judgment and Reasoning Capability of LLMs Change with Language? A Study using the Multilingual Defining Issues Test." Proceedings of EACL 2024 (Volume 1: Long Papers), pages 2882-2894, St. Julian's, Malta.

**ACL Anthology URL:** https://aclanthology.org/2024.eacl-long.176/
**DOI:** 10.18653/v1/2024.eacl-long.176

**Ethical Frameworks Covered:**
- Kohlberg's stages of moral development (via Defining Issues Test)
- Post-conventional moral reasoning measurement
- Cross-linguistic moral judgment variation

**Dataset Details:**
- Size: Defining Issues Test scenarios translated into 6 languages
- Format: DIT-format moral dilemma scenarios with staged reasoning options
- Languages: English, Chinese, Hindi, Russian, Spanish, Swahili

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** ChatGPT, GPT-4, Llama2Chat-70B
**Implementation Readiness:** MEDIUM - Uses established psychological instrument (DIT), but dataset size is constrained by the DIT format
**What Makes It Unique:** First application of the Defining Issues Test (established moral psychology instrument) to multilingual LLM evaluation; reveals dramatic language-dependent moral reasoning disparities (Hindi and Swahili significantly worse).

---

### Paper 7: Ethical Reasoning and Moral Value Alignment (Multilingual)

**Full Citation:** Utkarsh Agarwal, Kumar Tanmay, Aditi Khandelwal, Monojit Choudhury (2024). "Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language We Prompt Them in." Proceedings of LREC-COLING 2024, pages 6330-6340, Torino, Italia.

**ACL Anthology URL:** https://aclanthology.org/2024.lrec-main.560/

**Ethical Frameworks Covered:**
- Three branches of normative ethics: deontology, virtue ethics, consequentialism
- Cross-linguistic moral value alignment

**Dataset Details:**
- Size: Ethical dilemmas and policies across three normative ethics branches
- Format: Ethical dilemma prompts with policy evaluation
- Languages: English, Spanish, Russian, Chinese, Hindi, Swahili

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** GPT-4, ChatGPT, Llama2Chat-70B
**Implementation Readiness:** MEDIUM - Clear 3-framework evaluation, 6 languages, but dataset size not specified
**What Makes It Unique:** Explicitly compares deontological, virtue, and consequentialist reasoning across 6 languages; demonstrates GPT-4 is most consistent while others show significant moral value bias outside English.

---

### Paper 8: Evaluating Moral Beliefs (Pluralistic Framework)

**Full Citation:** Xuelin Liu, Yanfei Zhu, Shucheng Zhu, Pengyuan Liu, Ying Liu, Dong Yu (2024). "Evaluating Moral Beliefs across LLMs through a Pluralistic Framework." Findings of the Association for Computational Linguistics: EMNLP 2024, pages 4740-4760, Miami, Florida, USA.

**ACL Anthology URL:** https://aclanthology.org/2024.findings-emnlp.272/
**DOI:** 10.18653/v1/2024.findings-emnlp.272

**Ethical Frameworks Covered:**
- Pluralistic moral evaluation (individualist vs. collectivist moral beliefs)
- Moral choice ranking, moral decision analysis, moral debate examination
- Cross-cultural moral comparison (Western vs. Chinese models)

**Dataset Details:**
- Size: 472 moral choice scenarios
- Format: Moral decision-making scenarios derived from moral words
- Languages: Chinese

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** ChatGPT, Gemini, Ernie, ChatGLM (2 English-trained, 2 Chinese-trained)
**Implementation Readiness:** MEDIUM - Novel 3-module framework, but moderate dataset size (472 scenarios)
**What Makes It Unique:** Three-module evaluation (ranking, decision, debate) reveals cultural training bias: English models mirror individualistic beliefs while Chinese models lean collectivist; all models show gender bias in moral reasoning.

---

### Paper 9: GenMO (Gender-bias in Morality Opinions)

**Full Citation:** Divij Bajaj, Yuanyuan Lei, Jonathan Tong, Ruihong Huang (2024). "Evaluating Gender Bias of LLMs in Making Morality Judgements." Findings of the Association for Computational Linguistics: EMNLP 2024, pages 15804-15818, Miami, Florida, USA.

**ACL Anthology URL:** https://aclanthology.org/2024.findings-emnlp.928/
**DOI:** 10.18653/v1/2024.findings-emnlp.928

**Ethical Frameworks Covered:**
- Gender bias in moral judgment
- Intersection of gender and morality in LLM decision-making

**Dataset Details:**
- Size: Parallel short stories (exact count in full paper)
- Format: Parallel narratives with male/female character variants for controlled comparison
- Languages: English

**Code/Data URLs:** Dataset available at https://aclanthology.org/attachments/2024.findings-emnlp.928.data.zip
**LLMs Tested:** GPT-3.5-turbo, GPT-3.5-turbo-instruct, GPT-4-turbo, Llama 3 (8B/70B), Llama 3.1 (8B/70B), Mistral-7B, Claude 3 Sonnet, Claude 3 Opus
**Implementation Readiness:** HIGH - Data downloadable from ACL Anthology, extensive LLM coverage (9+ models)
**What Makes It Unique:** First benchmark specifically targeting gender bias in moral judgments; parallel story design enables controlled bias measurement; tests broadest range of LLMs including Claude 3 models.

---

### Paper 10: Fake Alignment (FINE Framework)

**Full Citation:** Yixu Wang, Yan Teng, Kexin Huang, Chengqi Lyu, Songyang Zhang, Wenwei Zhang, Xingjun Ma, Yu-Gang Jiang, Yu Qiao, Yingchun Wang (2024). "Fake Alignment: Are LLMs Really Aligned Well?" Proceedings of NAACL 2024, pages 4696-4712, Mexico City, Mexico.

**ACL Anthology URL:** https://aclanthology.org/2024.naacl-long.263/

**Ethical Frameworks Covered:**
- Safety alignment evaluation
- Consistency between multiple-choice and open-ended safety assessments
- Fake alignment detection (models appearing aligned but failing under open-ended probing)

**Dataset Details:**
- Size: Comparative benchmark with MC and open-ended questions
- Format: Paired multiple-choice and open-ended safety questions
- Languages: Not specified

**Code/Data URLs:** https://github.com/AIFlames/Fake-Alignment
**LLMs Tested:** 14 widely-used LLMs
**Implementation Readiness:** HIGH - GitHub code available, FINE framework with Consistency Score and Consistent Safety Score metrics
**What Makes It Unique:** Reveals critical gap between MC-based alignment evaluation and open-ended responses; introduces FINE framework with quantitative metrics (CS, CSS) to detect superficial/"fake" alignment in LLMs.

---

### Paper 11: VITAL (Pluralistic Alignment in Healthcare)

**Full Citation:** Anudeex Shetty, Amin Beheshti, Mark Dras, Usman Naseem (2025). "VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare." Proceedings of ACL 2025 (Volume 1: Long Papers), pages 22954-22974, Vienna, Austria.

**ACL Anthology URL:** https://aclanthology.org/2025.acl-long.1119/
**arXiv:** 2502.13775

**Ethical Frameworks Covered:**
- Pluralistic alignment across cultures, demographics, communities
- Healthcare-specific ethical values
- Influence of culture, religion, personal values on healthcare decisions

**Dataset Details:**
- Size: 13,100 value-laden situations + 5,400 multiple-choice questions
- Format: Multiple-choice questions focused on health scenarios
- Languages: Not specified (likely English)

**Code/Data URLs:** Not publicly listed in metadata
**LLMs Tested:** 8 LLMs of varying sizes
**Implementation Readiness:** HIGH - Large dataset (18.5K items), domain-specific (healthcare), multiple evaluation dimensions
**What Makes It Unique:** First pluralistic alignment benchmark specifically for healthcare; demonstrates that existing alignment techniques fail to accommodate diverse healthcare beliefs across cultural and religious lines.

---

### Paper 12: EMNLP (Educator-role Moral and Normative LLMs Profiling)

**Full Citation:** Yilin Jiang, Mingzi Zhang, Sheng Jin, Zengyi Yu, Xiangjie Kong, Binghao Tu (2025). "EMNLP: Educator-role Moral and Normative Large Language Models Profiling." Proceedings of EMNLP 2025, pages 815-843, Suzhou, China.

**ACL Anthology URL:** https://aclanthology.org/2025.emnlp-main.42/
**DOI:** 10.18653/v1/2025.emnlp-main.42

**Ethical Frameworks Covered:**
- Moral development stage measurement (Kohlberg-derived)
- Personality profiling of LLMs in educator roles
- Ethical risk evaluation under soft prompt injection

**Dataset Details:**
- Size: 88 teacher-specific moral dilemmas
- Format: Moral dilemma scenarios + prompt injection test sets
- Languages: Not specified

**Code/Data URLs:** Project website: https://e-m-n-l-p.github.io/
**LLMs Tested:** 14 LLMs
**Implementation Readiness:** MEDIUM - Project website available, 14 LLMs tested, but small dataset (88 dilemmas)
**What Makes It Unique:** First benchmark profiling LLMs in a specific professional role (educator); combines moral development stage assessment with adversarial prompt injection testing; enables direct comparison with human teacher moral profiles.

---

### Paper 13: PERSONA (Pluralistic Alignment Testbed)

**Full Citation:** Louis Castricato, Nathan Lile, Rafael Rafailov, Jan-Philipp Fränken, Chelsea Finn (2025). "PERSONA: A Reproducible Testbed for Pluralistic Alignment." Proceedings of COLING 2025, pages 11348-11368, Abu Dhabi, UAE.

**ACL Anthology URL:** https://aclanthology.org/2025.coling-main.752/
**arXiv:** 2407.17387

**Ethical Frameworks Covered:**
- Pluralistic alignment (avoiding majority viewpoint reinforcement)
- Demographic-based value diversity
- Anti-marginalization in preference modeling

**Dataset Details:**
- Size: 1,586 synthetic personas; 3,868 prompts; 317,200 feedback pairs
- Format: Persona profiles + prompt-response evaluation pairs
- Languages: English (US census-based)
- Source: Procedurally generated from US census data

**Code/Data URLs:** HuggingFace page: https://huggingface.co/papers/2407.17387
**LLMs Tested:** Details in full paper
**Implementation Readiness:** HIGH - Very large dataset (317K feedback pairs), reproducible generation pipeline, Stanford-backed
**What Makes It Unique:** Procedurally generated personas from census data enable reproducible, large-scale pluralistic alignment testing; 317K feedback pairs make it one of the largest alignment evaluation datasets; specifically targets minority viewpoint marginalization.

---

### Paper 14: Value Compass Benchmarks

**Full Citation:** Jing Yao, Xiaoyuan Yi, Shitong Duan, Jindong Wang, Yuzhuo Bai, Muhua Huang, Yang Ou, Scarlett Li, Peng Zhang, Tun Lu, Zhicheng Dou, Maosong Sun, James Evans, Xing Xie (2025). "Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation." Proceedings of ACL 2025 (Volume 3: System Demonstrations), pages 666-678, Vienna, Austria.

**ACL Anthology URL:** https://aclanthology.org/2025.acl-demo.64/
**DOI:** 10.18653/v1/2025.acl-demo.64

**Ethical Frameworks Covered:**
- 27 value dimensions from multiple social science value systems
- Cultural values alignment assessment
- Safety and alignment evaluation

**Dataset Details:**
- Size: Dynamic/self-evolving platform (27 value dimensions x 33 LLMs)
- Format: Interactive online evaluation platform (not static dataset)
- Languages: Not specified

**Code/Data URLs:** Not listed in metadata (demo paper with live platform)
**LLMs Tested:** 33 leading LLMs
**Implementation Readiness:** HIGH - 33 LLMs evaluated, 27 value dimensions, live platform
**What Makes It Unique:** Self-evolving evaluation platform rather than static benchmark; 27 value dimensions grounded in social science; evaluates 33 LLMs making it the broadest LLM coverage among value alignment benchmarks.

---

### Paper 15: Investigating Cultural Alignment of LLMs

**Full Citation:** Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, Mona Diab (2024). "Investigating Cultural Alignment of Large Language Models." Proceedings of ACL 2024 (Volume 1: Long Papers), pages 12404-12422, Bangkok, Thailand.

**ACL Anthology URL:** https://aclanthology.org/2024.acl-long.671/

**Ethical Frameworks Covered:**
- Cross-cultural value alignment (Egypt, United States)
- Social values probing
- Anthropological Prompting methodology

**Dataset Details:**
- Size: Replicated sociological surveys across regions
- Format: Survey-based prompting with persona-based evaluation
- Languages: Arabic, English

**Code/Data URLs:** Not listed in metadata
**LLMs Tested:** Multiple LLMs with different pretraining data mixtures
**Implementation Readiness:** MEDIUM - Novel Anthropological Prompting method, but dataset details not fully specified
**What Makes It Unique:** Introduces "Anthropological Prompting" -- a novel method leveraging anthropological reasoning to enhance cultural alignment; reveals misalignment is most pronounced for underrepresented personas and culturally sensitive social value topics.

---

### Paper 16: Unintended Impacts of LLM Alignment on Global Representation

**Full Citation:** Michael J. Ryan, William Held, Diyi Yang (2024). "Unintended Impacts of LLM Alignment on Global Representation." Proceedings of ACL 2024 (Volume 1: Long Papers), pages 16121-16140, Bangkok, Thailand.

**ACL Anthology URL:** https://aclanthology.org/2024.acl-long.853/
**DOI:** 10.18653/v1/2024.acl-long.853

**Ethical Frameworks Covered:**
- Global representation equity in alignment
- Three axes: Dialect, Language, Opinions from/about countries worldwide
- Equity considerations for preference tuning (RLHF, DPO)

**Dataset Details:**
- Size: Multi-axis evaluation across dialects, languages, global opinions
- Format: Evaluation across three representation axes
- Languages: Multiple (dialects and languages worldwide)

**Code/Data URLs:** Code and data publicly available on GitHub (URL in full paper)
**LLMs Tested:** LLMs aligned with RLHF and DPO methods
**Implementation Readiness:** MEDIUM - Code/data available, but more of an analysis framework than a static benchmark
**What Makes It Unique:** Demonstrates that alignment procedures (RLHF, DPO) create systematic disparities between English dialects and global opinions; provides framework for measuring unintended negative impacts of alignment on underrepresented populations.

---

### Paper 17: WalledEval

**Full Citation:** Prannaya Gupta, Le Qi Yau, Hao Han Low, I-Shiang Lee, Hugo Maximus Lim, Yu Xin Teoh, Koh Jia Hng, Dar Win Liew, Rishabh Bhardwaj, Rajat Bhardwaj, Soujanya Poria (2024). "WalledEval: A Comprehensive Safety Evaluation Toolkit for Large Language Models." Proceedings of EMNLP 2024: System Demonstrations, pages 397-407, Miami, Florida, USA.

**ACL Anthology URL:** https://aclanthology.org/2024.emnlp-demo.42/

**Ethical Frameworks Covered:**
- Multilingual safety evaluation
- Exaggerated safety detection
- Prompt injection resistance
- Over 35 safety benchmark areas

**Dataset Details:**
- Size: 35+ safety benchmarks integrated
- Format: Toolkit/framework integrating multiple existing benchmarks
- Languages: Multilingual

**Code/Data URLs:** https://github.com/walledai/walledeval | Demo: https://youtu.be/50Zy97kj1MA
**LLMs Tested:** Accommodates open-weight and API-based models (broad compatibility)
**Implementation Readiness:** HIGH - Open-source toolkit on GitHub, video demo, 35+ benchmarks, broad model compatibility
**What Makes It Unique:** Meta-toolkit integrating 35+ safety benchmarks into unified evaluation framework; supports both open-weight and API models; addresses exaggerated safety (over-refusal) alongside under-safety.

---

### Paper 18: Diagnosing Moral Reasoning Acquisition

**Full Citation:** Guangliang Liu, Zimo Qi, Xitong Zhang, Lei Jiang, Kristen Johnson (2025). "Diagnosing Moral Reasoning Acquisition in Language Models: Pragmatics and Generalization." Findings of the Association for Computational Linguistics: EMNLP 2025, pages 7103-7117, Suzhou, China.

**ACL Anthology URL:** https://aclanthology.org/2025.findings-emnlp.374/

**Ethical Frameworks Covered:**
- Moral Foundations Theory
- Moral reasoning acquisition (pragmatic dilemma concept)
- Fine-tuning impact on moral reasoning capabilities

**Dataset Details:**
- Size: Dataset with moral situations annotated with MFT classifications, Rules of Thumb, and Judgments
- Format: Annotated moral scenarios with multi-level labels
- Languages: English (implied)

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** Multiple LLMs evaluated under different fine-tuning strategies
**Implementation Readiness:** MEDIUM - Novel diagnostic framework, but dataset details not fully specified
**What Makes It Unique:** Identifies "pragmatic dilemma" as the primary bottleneck for moral reasoning acquisition in LLMs; demonstrates that moral reasoning improvements follow mechanisms similar to semantic-level tasks, offering training insights.

---

### Paper 19: Probing PLMs for Cross-Cultural Values (C3NLP Workshop)

**Full Citation:** Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein (2023). "Probing Pre-Trained Language Models for Cross-Cultural Differences in Values." Proceedings of the First Workshop on Cross-Cultural Considerations in NLP (C3NLP), pages 114-130, Dubrovnik, Croatia.

**ACL Anthology URL:** https://aclanthology.org/2023.c3nlp-1.12/

**Ethical Frameworks Covered:**
- Cross-cultural value theories
- Alignment with cross-cultural values surveys
- Implications of mis-aligned models in cross-cultural settings

**Dataset Details:**
- Size: Probe-based evaluation (details in full paper)
- Format: Value probes for pre-trained language models
- Languages: Multiple (cross-cultural focus)

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** Pre-trained language models (specifics in full paper)
**Implementation Readiness:** MEDIUM - Workshop paper, probing methodology, cross-cultural focus
**What Makes It Unique:** Early C3NLP workshop paper establishing methodology for probing cross-cultural value differences in PLMs; investigates alignment with established cross-cultural value survey instruments.

---

### Paper 20: SPICA (Scenarios for Pluralistic In-Context Alignment)

**Full Citation:** Quan Ze Chen, Kevin Feng, Chan Young Park, Amy X. Zhang (2025). "SPICA: Retrieving Scenarios for Pluralistic In-Context Alignment." Findings of the Association for Computational Linguistics: ACL 2025, pages 748-765, Vienna, Austria.

**ACL Anthology URL:** https://aclanthology.org/2025.findings-acl.41/

**Ethical Frameworks Covered:**
- Pluralistic alignment across demographic groups
- Equitable outcomes across populations
- In-context example retrieval for value alignment

**Dataset Details:**
- Size: Evaluation with n=544 participants (4 demographic groups) + n=120 end-to-end
- Format: Scenario-based alignment evaluation with demographic disaggregation
- Languages: English (implied)

**Code/Data URLs:** Not publicly listed
**LLMs Tested:** Not specified in metadata (framework-focused)
**Implementation Readiness:** MEDIUM - Human evaluation study, novel retrieval-based alignment method
**What Makes It Unique:** Retrieval-based approach to pluralistic alignment (rather than training-based); demonstrates uniform gains across all demographic groups rather than benefiting only some, addressing equity in alignment.

---

## Summary Table

| # | Paper/Benchmark | Venue | Year | Languages | Size | Readiness | Key Framework |
|---|----------------|-------|------|-----------|------|-----------|---------------|
| 1 | CMoralEval | Findings-ACL | 2024 | Chinese | 30,388 | HIGH | Chinese moral taxonomy |
| 2 | KorNAT | Findings-ACL | 2024 | Korean | 10,000 MC | HIGH | Korean social values survey |
| 3 | UniMoral | ACL (Best Resource) | 2025 | 6 languages | 8,784 | HIGH | Deontology/Utilitarian/Rights/Virtue |
| 4 | Flames | NAACL | 2024 | Chinese | Adversarial | HIGH | Chinese values + safety |
| 5 | Value FULCRA | NAACL | 2024 | Not spec. | 20,000 pairs | HIGH | Schwartz's Basic Values |
| 6 | Multilingual DIT | EACL | 2024 | 6 languages | DIT-based | MEDIUM | Kohlberg's moral development |
| 7 | Ethical Reasoning (Multilingual) | LREC-COLING | 2024 | 6 languages | Dilemma-based | MEDIUM | Deontology/Virtue/Consequentialism |
| 8 | Moral Beliefs (Pluralistic) | Findings-EMNLP | 2024 | Chinese | 472 scenarios | MEDIUM | Pluralistic (indiv. vs. collect.) |
| 9 | GenMO | Findings-EMNLP | 2024 | English | Parallel stories | HIGH | Gender bias in morality |
| 10 | Fake Alignment (FINE) | NAACL | 2024 | Not spec. | MC + open-ended | HIGH | Safety alignment consistency |
| 11 | VITAL | ACL | 2025 | English | 18,500 items | HIGH | Pluralistic healthcare values |
| 12 | EMNLP (Educator Profiling) | EMNLP | 2025 | Not spec. | 88 dilemmas | MEDIUM | Moral development + prompt injection |
| 13 | PERSONA | COLING | 2025 | English | 317,200 pairs | HIGH | Pluralistic alignment (census) |
| 14 | Value Compass Benchmarks | ACL Demo | 2025 | Not spec. | 27 dims x 33 LLMs | HIGH | 27 social science value dims |
| 15 | Cultural Alignment (Anthropological Prompting) | ACL | 2024 | Arabic, English | Survey-based | MEDIUM | Cross-cultural (Egypt/US) |
| 16 | Unintended Alignment Impacts | ACL | 2024 | Multiple | Multi-axis | MEDIUM | Global representation equity |
| 17 | WalledEval | EMNLP Demo | 2024 | Multilingual | 35+ benchmarks | HIGH | Safety evaluation toolkit |
| 18 | Diagnosing Moral Reasoning | Findings-EMNLP | 2025 | English | Annotated moral | MEDIUM | Moral Foundations Theory |
| 19 | Cross-Cultural Values Probing | C3NLP Workshop | 2023 | Multiple | Probe-based | MEDIUM | Cross-cultural value surveys |
| 20 | SPICA | Findings-ACL | 2025 | English | 544 participants | MEDIUM | Pluralistic in-context alignment |

---

## HIGH Implementation Readiness Papers (Top Recommendations)

1. **UniMoral** (ACL 2025 Best Resource Paper) -- 6 languages, 8,784 instances, 4 evaluation tasks, 4 ethical frameworks
2. **CMoralEval** -- 30,388 instances, Chinese cultural moral taxonomy
3. **Flames** -- GitHub available, 17 LLMs tested, adversarial Chinese value alignment
4. **GenMO** -- Data downloadable from ACL Anthology, 9+ LLMs including Claude
5. **VITAL** -- 18,500 items, healthcare-specific pluralistic alignment
6. **PERSONA** -- 317,200 feedback pairs, reproducible census-based generation
7. **Value FULCRA** -- 20,000 pairs, Schwartz theory grounded
8. **KorNAT** -- 10,000 MC questions, survey-grounded Korean values
9. **Value Compass Benchmarks** -- 27 dimensions, 33 LLMs, live platform
10. **Fake Alignment (FINE)** -- GitHub available, 14 LLMs, reveals fake alignment gap

---

## Notes on Search Coverage

- Searched 20 times across ACL Anthology venues (ACL, EMNLP, NAACL, EACL, LREC-COLING, COLING, IJCNLP)
- Covered main conference proceedings, Findings papers, System Demonstrations, and workshop papers (C3NLP, NLP4PI, WOAH)
- Covered years 2023-2025
- Excluded all papers in the ALREADY KNOWN list
- Some papers from the ALREADY KNOWN list appeared frequently in results (e.g., MORABLES, Greatest Good Benchmark, MFTCXplain, Structured Moral Reasoning/Chakraborty), confirming they are indeed prominent in this space
