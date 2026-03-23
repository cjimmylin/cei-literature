# Agent 1: Semantic Scholar Citation Graph Explorer - Findings Report
## New Papers with Implementable Benchmarks/Datasets for Ethical Values Alignment in LLMs

**Date:** 2026-02-07
**Search Strategy:** Citation graph traversal from anchor papers (Hendrycks ETHICS 2021, MoralChoice, ValueBench, DailyDilemmas, Delphi) + direct Semantic Scholar / arXiv searches
**Total NEW papers found:** 28

---

## Paper #1: NormAd (NORMAD)

- **Full Citation:** Abhinav Rao, Akhila Yerukola, Vishwa Shah, Katharina Reinecke, Maarten Sap. "NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models." NAACL 2025.
- **arXiv ID:** 2404.12464
- **Ethical Frameworks:** Cultural social norms, social etiquette norms across 75 countries
- **Dataset Details:** 2,600 stories representing social/cultural norms from 75 countries; three conditions of cultural norm specificity (Country, Values+Country, Rules-of-Thumb); English
- **Code/Data URLs:** Dataset and code released (see paper)
- **LLMs Tested:** Mistral-7b-Instruct (top performer at 81.8% with explicit norms), plus other models
- **Implementation Readiness:** HIGH
- **Unique Contribution:** Tests cultural *adaptability* rather than just knowledge; measures gap between model performance with explicit norms (81.8%) vs. abstract values (<60%), compared to human performance (>90%); focuses on Global South underrepresentation.

---

## Paper #2: LocalValueBench

- **Full Citation:** [Authors from NeurIPS submission]. "LocalValueBench: A Collaboratively Built and Extensible Benchmark for Evaluating Localized Value Alignment and Ethical Safety in Large Language Models." 2024.
- **arXiv ID:** 2408.01460
- **Ethical Frameworks:** Australian values framework; extensible typology for ethical reasoning
- **Dataset Details:** Questions covering 6 topics (tipping, capital punishment, category R weapons, refugees, gay marriage, compulsory voting); prompt engineering strategies; English
- **Code/Data URLs:** See arXiv
- **LLMs Tested:** GPT-4, Gemini 1.5 Pro, Claude 3 Sonnet
- **Implementation Readiness:** MEDIUM (limited topic coverage, but extensible framework)
- **Unique Contribution:** Provides a *template* for regulators worldwide to develop localized LLM value alignment benchmarks; collaborative construction methodology.

---

## Paper #3: FLAMES

- **Full Citation:** Huang et al. "Flames: Benchmarking Value Alignment of LLMs in Chinese." NAACL 2024.
- **arXiv ID:** 2311.06899
- **Ethical Frameworks:** Fairness, Safety, Morality (Chinese-specific), Data Protection, Legality
- **Dataset Details:** 2,251 adversarial prompts across 5 dimensions; Chinese language; includes jailbreaking methods
- **Code/Data URLs:** https://github.com/AI45Lab/Flames
- **LLMs Tested:** 17 mainstream LLMs; Claude best at 63.77% harmless rate
- **Implementation Readiness:** HIGH (code, data, and lightweight automated scorer all available)
- **Unique Contribution:** Highly adversarial Chinese-specific benchmark; automated scoring tool; exposes safety vulnerabilities across dimensions.

---

## Paper #4: KorNAT

- **Full Citation:** Jiyoung Lee et al. "KorNAT: LLM Alignment Benchmark for Korean Social Values and Common Knowledge." Findings of ACL 2024.
- **arXiv ID:** 2402.13605
- **Ethical Frameworks:** Korean social value alignment + common knowledge alignment
- **Dataset Details:** 4K multiple-choice questions (social values) + 6K questions (common knowledge); Korean; ground truth from survey of 6,174 South Koreans
- **Code/Data URLs:** https://huggingface.co/datasets/jiyounglee0523/KorNAT (released December 2024)
- **LLMs Tested:** Multiple LLMs (details in paper)
- **Implementation Readiness:** HIGH (HuggingFace dataset available)
- **Unique Contribution:** First national alignment benchmark for South Korea; large-scale public survey for ground truth; dual assessment (values + knowledge).

---

## Paper #5: MVPBench

- **Full Citation:** Yao Liang, Dongcheng Zhao, Feifei Zhao, Guobin Shen, Yuwei Wang, Dongqi Liang, Yi Zeng. "MVPBench: A Benchmark and Fine-Tuning Framework for Aligning Large Language Models with Diverse Human Values." 2025.
- **arXiv ID:** 2509.08022 (**NOTE: Withdrawn for revisions, planned resubmission**)
- **Ethical Frameworks:** Multi-dimensional human value preferences across 75 countries
- **Dataset Details:** 24,020 instances with fine-grained value labels, personalized questions, demographic metadata; multi-country
- **Code/Data URLs:** TBD (paper withdrawn)
- **LLMs Tested:** Multiple state-of-the-art LLMs
- **Implementation Readiness:** LOW (withdrawn, awaiting revision)
- **Unique Contribution:** Largest cross-cultural value alignment dataset; LoRA and DPO fine-tuning integration; demographic metadata integration.

---

## Paper #6: The Moral Turing Test

- **Full Citation:** Basile Garcia, Crystal Qian, Stefano Palminteri. "The Moral Turing Test: Evaluating Human-LLM Alignment in Moral Decision-Making." 2024.
- **arXiv ID:** 2410.07304
- **Ethical Frameworks:** Utilitarian moral dilemmas; personal vs. impersonal framing
- **Dataset Details:** User study with 230 participants (N=230); moral dilemma scenarios; English
- **Code/Data URLs:** See paper
- **LLMs Tested:** Multiple LLMs (details in paper)
- **Implementation Readiness:** MEDIUM (user study methodology; replicable framework)
- **Unique Contribution:** Tests whether humans can distinguish AI moral judgments from human ones; reveals anti-AI bias where participants reject judgments they believe are machine-generated; LLMs more sensitive to personal framing.

---

## Paper #7: Moral Persuasion in LLMs

- **Full Citation:** Allison Huang, Yulu Niki Pi, Carlos Mougan. "Moral Persuasion in Large Language Models: Evaluating Susceptibility and Ethical Alignment." 2024.
- **arXiv ID:** 2411.11731
- **Ethical Frameworks:** Common morality principles; persuasion susceptibility
- **Dataset Details:** Large-scale survey with high/low ambiguity moral scenarios; LLM-to-LLM persuasion protocol; English
- **Code/Data URLs:** See paper (CC BY 4.0)
- **LLMs Tested:** Multiple LLMs of different sizes from same and different companies
- **Implementation Readiness:** MEDIUM (novel agent-to-agent persuasion methodology)
- **Unique Contribution:** First systematic study of LLM-to-LLM moral persuasion; reveals that model size within same company produces markedly different susceptibility.

---

## Paper #8: ValueCompass

- **Full Citation:** Hua Shen, Knearem et al. "ValueCompass: A Framework for Measuring Contextual Value Alignment Between Human and LLMs." WiNLP @ EMNLP 2025.
- **arXiv ID:** 2409.09586
- **Ethical Frameworks:** Schwartz's Theory of Basic Values (56 values, 10 motivational types)
- **Dataset Details:** Survey of 72 participants, 144 responses, 7,056 human value ratings; 160 LLM responses, 7,840 LLM value ratings; 4 real-world scenarios (collaborative writing, education, public sectors, healthcare); English
- **Code/Data URLs:** https://valuecompass.github.io/
- **LLMs Tested:** GPT-4o, Llama3, Mistral, + 2 others
- **Implementation Readiness:** HIGH (framework + website + data available)
- **Unique Contribution:** Context-dependent value alignment measurement; reveals that humans endorse values like "National Security" that LLMs largely reject; practical pre-deployment diagnostic tool.

---

## Paper #9: Value Compass Benchmarks (Leaderboard)

- **Full Citation:** Jing Yao, Xiaoyuan Yi, Shitong Duan, Jindong Wang, Yuzhuo Bai, Muhua Huang, Peng Zhang, Tun Lu, Zhicheng Dou, Maosong Sun, Xing Xie. "Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs' Value Evaluation." ACL 2025 Demo.
- **arXiv ID:** 2501.07071
- **Ethical Frameworks:** 10 main value categories (truthfulness, justice, compassion, etc.) grounded in humanities/social science
- **Dataset Details:** Dynamic, evolving evaluation; generative framework to combat data contamination; customizable weights for pluralistic values
- **Code/Data URLs:** https://valuecompass.github.io/#/leaderboard
- **LLMs Tested:** Multiple LLMs on leaderboard
- **Implementation Readiness:** HIGH (live online platform with leaderboard)
- **Unique Contribution:** First dynamic, online, interactive platform for LLM value diagnosis; uses CLAVE hybrid value recognizer; addresses data contamination via generative evaluation; supports pluralistic value weighting.

---

## Paper #10: Mind the Value-Action Gap (ValueActionLens)

- **Full Citation:** Hua Shen, Clark et al. "Mind the Value-Action Gap: Do LLMs Act in Alignment with Their Values?" EMNLP 2025.
- **arXiv ID:** 2501.15463
- **Ethical Frameworks:** Cross-cultural values across 12 cultures and 11 social topics
- **Dataset Details:** 14.8K value-informed actions across 12 cultures and 11 social topics; two evaluation tasks; three alignment metrics; English
- **Code/Data URLs:** https://github.com/huashen218/value_action_gap
- **LLMs Tested:** GPT-4o-mini (best, F1=0.564), GPT-3.5-turbo (worst, F1=0.179), + others
- **Implementation Readiness:** HIGH (GitHub code + dataset available)
- **Unique Contribution:** First to measure the gap between LLMs' *stated* values and their *actual actions*; reveals substantial misalignment; context-aware evaluation across cultures.

---

## Paper #11: Deep Value Benchmark (DVB)

- **Full Citation:** Joshua Ashkinaze, Hua Shen, Saipranav Avula, Eric Gilbert, Ceren Budak. "Deep Value Benchmark: Measuring Whether Models Generalize Deep Values or Shallow Preferences." NeurIPS 2025 (Spotlight).
- **arXiv ID:** 2511.02109
- **Ethical Frameworks:** Deep vs. shallow values across 8 domains (commerce, finance, healthcare, legal, education, etc.)
- **Dataset Details:** 8 domain clusters; three separate human validation experiments; multi-domain; English
- **Code/Data URLs:** Dataset released (details in paper)
- **LLMs Tested:** 9 models including GPT-4o, GPT-4.1, Gemini-2.0-flash, Llama-3-8b/70b-instruct
- **Implementation Readiness:** HIGH (NeurIPS Spotlight; validated dataset released)
- **Unique Contribution:** Tests whether models learn *genuine values* or *surface-level preferences*; average Deep Value Generalization Rate is just 0.30 (below chance); larger models slightly lower DVGR.

---

## Paper #12: M3oralBench

- **Full Citation:** Bei Yan, Jie Zhang, Zhiyuan Chen, Shiguang Shan, Xilin Chen. "M3oralBench: A MultiModal Moral Benchmark for LVLMs." 2024.
- **arXiv ID:** 2412.20718
- **Ethical Frameworks:** Moral Foundations Theory (6 foundations: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, Liberty/Oppression)
- **Dataset Details:** 1,160 moral violation scenarios with generated images (SD3.0); multimodal (text + image); English
- **Code/Data URLs:** Publicly available (see paper)
- **LLMs Tested:** 10 open-source and closed-source LVLMs; GPT-4o highest, Gemini-1.5-Pro second
- **Implementation Readiness:** HIGH (first multimodal moral benchmark)
- **Unique Contribution:** First multimodal moral benchmark for vision-language models; uses diffusion-generated images paired with moral scenarios; reveals limitations in Loyalty/Betrayal and Sanctity/Degradation dimensions.

---

## Paper #13: MORALISE

- **Full Citation:** Xiao Lin, Zhining Liu, Ze Yang, Gaotang Li, Ruizhong Qiu, Shuke Wang, Hui Liu, Haotian Li, Sumit Keswani, Vishwa Pardeshi, Huijun Zhao, Wei Fan, Hanghang Tong. "MORALISE: A Structured Benchmark for Moral Alignment in Visual Language Models." NeurIPS 2025 D&B Track (submitted).
- **arXiv ID:** 2505.14728
- **Ethical Frameworks:** Turiel's Domain Theory; 13 moral topics across personal, interpersonal, societal domains
- **Dataset Details:** 2,481 expert-verified image-text pairs; dual annotations (topic + modality); real-world data (not AI-generated)
- **Code/Data URLs:** https://huggingface.co/datasets/Ze1025/MORALISE
- **LLMs Tested:** 19 open- and closed-source VLMs
- **Implementation Readiness:** HIGH (HuggingFace dataset available; expert-verified)
- **Unique Contribution:** Uses real-world data (not synthetic); modality-aware annotations distinguishing image vs. text violations; comprehensive 13-topic moral taxonomy.

---

## Paper #14: The Staircase of Ethics (Multi-step Moral Dilemmas / MMDs)

- **Full Citation:** Ya Wu, Qiang Sheng, Danding Wang, Guang Yang, Yifan Sun, Zhengjia Wang, Yuyan Bu, Juan Cao. "The Staircase of Ethics: Probing LLM Value Priorities through Multi-Step Induction to Complex Moral Dilemmas." EMNLP 2025.
- **arXiv ID:** 2505.18154
- **Ethical Frameworks:** Dynamic Value Loading; Nonlinear Preference Shifts; multi-value conflicts (care, fairness, honesty, etc.)
- **Dataset Details:** 3,302 five-stage moral dilemmas; progressive escalation of ethical conflicts; English
- **Code/Data URLs:** See paper
- **LLMs Tested:** 9 widely used LLMs
- **Implementation Readiness:** HIGH (large dataset, systematic evaluation protocol)
- **Unique Contribution:** First dataset testing *progressive* moral reasoning across escalating scenarios; reveals that LLMs recalibrate moral judgments with complexity; operationalizes Dynamic Value Loading theory.

---

## Paper #15: UniMoral

- **Full Citation:** Shivani Kumar, David Jurgens. "Are Rules Meant to be Broken? Understanding Multilingual Moral Reasoning as a Computational Pipeline with UniMoral." ACL 2025 (Best Resource Paper).
- **arXiv ID:** 2502.14083
- **Ethical Frameworks:** Multiple moral typologies; psychologically grounded + social-media-derived moral dilemmas
- **Dataset Details:** Multilingual (Arabic, Chinese, English, Hindi, Russian, Spanish); unified annotations for action choices, ethical principles, contributing factors, consequences; annotator moral/cultural profiles
- **Code/Data URLs:** See paper (ACL 2025 Best Resource Paper)
- **LLMs Tested:** 3 LLMs across 4 benchmark tasks
- **Implementation Readiness:** HIGH (Best Resource Paper at ACL 2025; multilingual)
- **Unique Contribution:** ACL 2025 Best Resource Paper; 6-language coverage; integrates psychological and social-media moral dilemmas; includes annotator cultural profiles; 4 benchmark tasks (action prediction, typology classification, factor attribution, consequence generation).

---

## Paper #16: MoralReason (Moral-Reason-QA)

- **Full Citation:** [Authors from arXiv]. "MoralReason: Generalizable Moral Decision Alignment For LLM Agents Using Reasoning-Level Reinforcement Learning." 2025.
- **arXiv ID:** 2511.12271
- **Ethical Frameworks:** Utilitarian, Deontological, Virtue Ethics
- **Dataset Details:** 680 human-annotated high-ambiguity moral scenarios with framework-specific reasoning traces; English
- **Code/Data URLs:** See paper
- **LLMs Tested:** Multiple LLMs with GRPO-based RL fine-tuning
- **Implementation Readiness:** MEDIUM (novel RL approach; dataset + methodology)
- **Unique Contribution:** First to formulate moral alignment as OOD generalization problem; reasoning traces for three ethical frameworks; GRPO-based RL training; demonstrates +0.757 improvement for utilitarian alignment.

---

## Paper #17: Moral Alignment for LLM Agents

- **Full Citation:** Elizaveta Tennant, Stephen Hailes, Mirco Musolesi. "Moral Alignment for LLM Agents." ICLR 2025.
- **arXiv ID:** 2410.01639
- **Ethical Frameworks:** Deontological Ethics, Utilitarianism (via Iterated Prisoner's Dilemma)
- **Dataset Details:** Text-based Iterated Prisoner's Dilemma environment; moral reward functions
- **Code/Data URLs:** https://github.com/liza-tennant/LLM_morality
- **LLMs Tested:** Gemma2-2b-it (fine-tuned with PPO via TRL)
- **Implementation Readiness:** HIGH (ICLR 2025; GitHub code available)
- **Unique Contribution:** Intrinsic moral reward functions for RL fine-tuning; transparent value encoding; game-theoretic moral evaluation environment.

---

## Paper #18: Value Portrait

- **Full Citation:** Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo. "Value Portrait: Assessing Language Models' Values through Psychometrically and Ecologically Valid Items." ACL 2025.
- **arXiv ID:** (ACL 2025 proceedings)
- **Ethical Frameworks:** Schwartz's values (Benevolence, Security, Self-Direction, Tradition, Power, Achievement, etc.)
- **Dataset Details:** Items from real user-LLM interactions; human-rated items correlated with actual value scores; psychometrically validated
- **Code/Data URLs:** See paper
- **LLMs Tested:** 44 LLMs evaluated
- **Implementation Readiness:** HIGH (44 LLMs tested; psychometric validation)
- **Unique Contribution:** Uses real user-LLM interactions rather than synthetic scenarios; psychometrically validated against human value scores; reveals demographic perception biases in LLMs; tested on 44 models.

---

## Paper #19: Value-Spectrum

- **Full Citation:** [Authors]. "Value-Spectrum: Quantifying Preferences of Vision-Language Models via Value Decomposition in Social Media Contexts." ACL 2025.
- **arXiv ID:** 2411.11479
- **Ethical Frameworks:** Schwartz's 10 value dimensions
- **Dataset Details:** 50,000+ short videos from TikTok, YouTube Shorts, Instagram Reels; VQA benchmark; multi-topic (family, health, hobbies, society, technology)
- **Code/Data URLs:** https://github.com/Jeremyyny/Value-Spectrum
- **LLMs Tested:** Multiple VLMs with persona prompting
- **Implementation Readiness:** HIGH (GitHub available; large-scale dataset)
- **Unique Contribution:** First VLM value assessment using social media video content; persona-based evaluation; tests value adaptability in role-playing scenarios.

---

## Paper #20: Internal Value Alignment (ConVA)

- **Full Citation:** Haoran Jin, Meng Li, Xiting Wang, Zhihao Xu, Minlie Huang, Yantao Jia, Defu Lian. "Internal Value Alignment in Large Language Models through Controlled Value Vector Activation." ACL 2025.
- **arXiv ID:** 2507.11316
- **Ethical Frameworks:** 10 basic Schwartz values
- **Dataset Details:** Evaluation across 10 value dimensions; adversarial input testing
- **Code/Data URLs:** https://github.com/hr-jin/ConVA
- **LLMs Tested:** Multiple LLMs (details in paper)
- **Implementation Readiness:** HIGH (ACL 2025; GitHub code available)
- **Unique Contribution:** Mechanistic interpretability approach to values; modifies internal activations for value alignment; gated value vector activation; robust against adversarial/malicious prompts.

---

## Paper #21: Generative Psycho-Lexical Approach (GPLA)

- **Full Citation:** [Authors]. "Generative Psycho-Lexical Approach for Constructing Value Systems in Large Language Models." ACL 2025.
- **arXiv ID:** 2502.02444
- **Ethical Frameworks:** Five-factor LLM value system: Social Responsibility, Risk-taking, Rule-following, Self-competence, Rationality
- **Dataset Details:** Psychologically grounded value lexicons; three benchmarking tasks; generated from agent text
- **Code/Data URLs:** See paper
- **LLMs Tested:** Multiple LLMs (details in paper)
- **Implementation Readiness:** MEDIUM (novel value system construction methodology)
- **Unique Contribution:** Proposes LLM-specific value system (not just adapted from human psychology); five-factor model outperforms Schwartz's values for LLM safety prediction and alignment.

---

## Paper #22: Discerning What Matters

- **Full Citation:** Daniel Kilov, Caroline Hendy, Secil Yanik Guyot, Aaron J. Snoswell, Seth Lazar. "Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs." 2025.
- **arXiv ID:** 2506.13082
- **Ethical Frameworks:** Five dimensions of moral competence (identification, weighting, reason assignment, judgment synthesis, gap recognition)
- **Dataset Details:** Two experiment sets: standard ethical vignettes + novel scenarios with moral features embedded in noisy information; English
- **Code/Data URLs:** See paper
- **LLMs Tested:** 6 leading LLMs compared against non-expert humans and professional philosophers
- **Implementation Readiness:** MEDIUM (novel evaluation dimensions; new scenarios)
- **Unique Contribution:** Reveals that LLMs fail when moral features are embedded in noisy contexts; standard benchmarks may *overestimate* LLM moral reasoning; compares against both non-experts and professional philosophers.

---

## Paper #23: Beyond Verdicts (Survey/Framework)

- **Full Citation:** Aaron J. Snoswell, Daniel Kilov, Seth Lazar. "Beyond Verdicts: Evaluating Language Model Moral Competence." AAAI 2026 AI Alignment Track (forthcoming).
- **Venue:** PhilArchive / AAAI 2026
- **Ethical Frameworks:** Taxonomy of moral evaluation covering moral sensitivity, reasoning quality, steerability
- **Dataset Details:** Survey of 69 papers (2020-2025); taxonomy of datasets, behaviors, metrics
- **Code/Data URLs:** See paper
- **Implementation Readiness:** MEDIUM (meta-analysis/framework; not a dataset per se)
- **Unique Contribution:** Comprehensive taxonomy of 69 evaluation papers; identifies three critical gaps (moral sensitivity, reasoning vs. verdicts, ground truth assumptions); argues for paradigm shift in moral evaluation.

---

## Paper #24: Fine-Tuning for Ethical Ambiguity (SCRUPLES-based)

- **Full Citation:** Senthilkumar, Balasubramanian, Jain, Maity, Lu, Zhu. "Fine-Tuning Language Models for Ethical Ambiguity: A Comparative Study of Alignment with Human Responses." 2024.
- **arXiv ID:** 2410.07826
- **Ethical Frameworks:** Descriptive ethics; community ethical judgments
- **Dataset Details:** SCRUPLES DILEMMAS + ANECDOTES subsets; 32,000 real-life anecdotes with 625,000 ethical judgments
- **Code/Data URLs:** Uses SCRUPLES corpus (publicly available)
- **LLMs Tested:** Llama-3.1-8b, Zephyr-7b-beta, Mistral-7b
- **Implementation Readiness:** HIGH (SCRUPLES dataset publicly available; fine-tuning methodology replicable)
- **Unique Contribution:** Shows that fine-tuning significantly improves moral alignment in ambiguous scenarios; uses large-scale community judgment corpus; text-to-text fine-tuning approach.

---

## Paper #25: Value Profiles for Encoding Human Variation

- **Full Citation:** [Authors]. "Value Profiles for Encoding Human Variation." 2025.
- **arXiv ID:** 2503.15484
- **Ethical Frameworks:** Natural language value profiles; personalized value alignment
- **Dataset Details:** In-context demonstrations compressed into value profiles; rater representations; information-theoretic evaluation
- **Code/Data URLs:** See paper
- **LLMs Tested:** Multiple LLMs as steerable decoders
- **Implementation Readiness:** MEDIUM (novel methodology for personalized alignment)
- **Unique Contribution:** Value profiles compress >70% information from demonstrations; better explains variation than demographics; enables scrutability, interpretability, and steerability.

---

## Paper #26: Causal Graph Guided Steering of LLM Values

- **Full Citation:** [Authors]. "Causal Graph Guided Steering of LLM Values via Prompts and Sparse Autoencoders." 2025.
- **arXiv ID:** 2501.00581
- **Ethical Frameworks:** Multi-dimensional value systems with causal relationships
- **Dataset Details:** Causal value graph; SAE feature manipulation; prompt-based role-setting
- **Code/Data URLs:** See paper
- **LLMs Tested:** Gemma-2B-IT, Llama3-8B-IT
- **Implementation Readiness:** MEDIUM (mechanistic interpretability approach; novel but requires SAE training)
- **Unique Contribution:** Maps causal relationships between values; predicts ripple effects of adjusting one value on others; outperforms semantic graphs; dual steering via SAE features + prompts.

---

## Paper #27: AMAeval (Beyond Ethical Alignment)

- **Full Citation:** [Raponi et al.]. "Beyond Ethical Alignment: Evaluating LLMs as Artificial Moral Assistants." 2025.
- **arXiv ID:** 2508.12754
- **Ethical Frameworks:** Formal moral reasoning (abductive + deductive); moral precept application
- **Dataset Details:** Evaluation of moral reasoning chains (evaluation + generation); English
- **Code/Data URLs:** See paper
- **LLMs Tested:** Multiple models at different scales
- **Implementation Readiness:** MEDIUM (formal framework; benchmark available)
- **Unique Contribution:** Distinguishes between deriving and applying moral precepts; reveals persistent asymmetry in abductive vs. deductive reasoning; model scale correlates with competence except at highest size.

---

## Paper #28: Large Language Models Meet Moral Values (MFRC-based)

- **Full Citation:** Luana Bulla, Misael Mongiovi, Stefano De Giorgis, Aldo Gangemi. "Large Language Models Meet Moral Values: A Comprehensive Assessment of Moral Abilities." 2025.
- **DOI:** ScienceDirect / SSRN 4907562
- **Ethical Frameworks:** Moral Foundations Theory (via Moral Foundation Reddit Corpus)
- **Dataset Details:** Moral Foundation Reddit Corpus (MFRC); multi-label and binary classification; English
- **Code/Data URLs:** https://github.com/LuanaBulla/Detection-of-Morality-in-Text
- **LLMs Tested:** Multiple LLM sizes with different prompt designs
- **Implementation Readiness:** HIGH (GitHub code + MFRC publicly available)
- **Unique Contribution:** Unsupervised moral classification using LLMs; directly compares model outputs with human annotations; addresses overfitting in supervised moral classifiers.

---

## Summary Table

| # | Paper | Year | Venue | Framework | Lang | Size | Impl. |
|---|-------|------|-------|-----------|------|------|-------|
| 1 | NormAd | 2024 | NAACL 2025 | Cultural norms | EN | 2.6K | HIGH |
| 2 | LocalValueBench | 2024 | arXiv | Australian values | EN | 6 topics | MED |
| 3 | FLAMES | 2024 | NAACL 2024 | 5 dimensions | ZH | 2,251 | HIGH |
| 4 | KorNAT | 2024 | ACL 2024 | Korean values | KO | 10K | HIGH |
| 5 | MVPBench | 2025 | Withdrawn | Cross-cultural | Multi | 24K | LOW |
| 6 | Moral Turing Test | 2024 | arXiv | Utilitarian | EN | 230 subj | MED |
| 7 | Moral Persuasion | 2024 | arXiv | Common morality | EN | Survey | MED |
| 8 | ValueCompass | 2024 | EMNLP 2025 | Schwartz values | EN | 7K+ ratings | HIGH |
| 9 | Value Compass Bench | 2025 | ACL Demo | 10 categories | Multi | Dynamic | HIGH |
| 10 | ValueActionLens | 2025 | EMNLP 2025 | Cross-cultural | EN | 14.8K | HIGH |
| 11 | Deep Value Bench | 2025 | NeurIPS 2025 | 8 domains | EN | 8 clusters | HIGH |
| 12 | M3oralBench | 2024 | arXiv | MFT 6 foundations | EN | 1,160 | HIGH |
| 13 | MORALISE | 2025 | NeurIPS D&B | Turiel's Theory | EN | 2,481 | HIGH |
| 14 | Staircase of Ethics | 2025 | EMNLP 2025 | Dynamic values | EN | 3,302 | HIGH |
| 15 | UniMoral | 2025 | ACL 2025* | Multiple | 6 langs | Large | HIGH |
| 16 | MoralReason | 2025 | arXiv | Util/Deont/Virtue | EN | 680 | MED |
| 17 | Moral Alignment Agents | 2024 | ICLR 2025 | Deont/Util | EN | IPD env | HIGH |
| 18 | Value Portrait | 2025 | ACL 2025 | Schwartz values | EN | 44 LLMs | HIGH |
| 19 | Value-Spectrum | 2024 | ACL 2025 | Schwartz 10 | Multi | 50K+ vids | HIGH |
| 20 | ConVA | 2025 | ACL 2025 | 10 basic values | EN | 10 dims | HIGH |
| 21 | GPLA | 2025 | ACL 2025 | 5-factor LLM | EN | Lexicons | MED |
| 22 | Discerning Matters | 2025 | arXiv | 5 moral dims | EN | 2 exp sets | MED |
| 23 | Beyond Verdicts | 2025 | AAAI 2026 | Meta-taxonomy | EN | 69 papers | MED |
| 24 | Ethical Ambiguity FT | 2024 | arXiv | Descriptive ethics | EN | 32K+625K | HIGH |
| 25 | Value Profiles | 2025 | arXiv | Personalized | EN | Profiles | MED |
| 26 | Causal Graph Values | 2025 | arXiv | Causal values | EN | Graph | MED |
| 27 | AMAeval | 2025 | arXiv | Formal moral | EN | Chains | MED |
| 28 | LLMs Meet Moral | 2025 | ScienceDirect | MFT/MFRC | EN | Reddit | HIGH |

*UniMoral won ACL 2025 Best Resource Paper
