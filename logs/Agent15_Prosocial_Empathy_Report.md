# Agent 15: Prosocial Behavior, Empathy & Emotional Intelligence Benchmarks

**Search Date:** 2026-02-07
**Domain:** Prosocial Behavior, Empathy, Emotional Intelligence, and Moral Sentiment Evaluation for LLMs
**Agent:** Agent 15 (Exhaustive Literature Search)

---

## Executive Summary

This report covers **20 implementable benchmarks and datasets** for evaluating LLMs on prosocial behavior, empathy, emotional intelligence, and related moral sentiment dimensions. The benchmarks span four major sub-domains: (1) Emotional Intelligence & Empathy, (2) Human-Centered & Prosocial Evaluation, (3) Moral Sentiment & Emotional Moral Reasoning, and (4) Social Skills & Interpersonal Ethics. Each entry includes citation details, dataset specifications, code/data availability, and implementation readiness assessment.

---

## 1. Emotional Intelligence & Empathy Benchmarks

---

### 1.1 EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models

- **Authors:** Samuel J. Paech
- **Year:** 2023 (arXiv Dec 2023; updated Jan 2024)
- **Venue:** arXiv preprint
- **arXiv ID:** [2312.06281](https://arxiv.org/abs/2312.06281)
- **Ethical Frameworks:** Emotional intelligence theory; emotion intensity prediction; social interaction understanding
- **Dataset Size & Format:** 60 English-language questions; dialogue-based emotion intensity prediction tasks; models predict intensity of 4 emotional states per question on a 0-1 scale
- **Code/Data URLs:**
  - GitHub: [https://github.com/EQ-bench/EQ-Bench](https://github.com/EQ-bench/EQ-Bench)
  - Leaderboard: [https://eqbench.com](https://eqbench.com)
  - HuggingFace: [pbevan11/EQ-Bench](https://huggingface.co/datasets/pbevan11/EQ-Bench)
- **LLMs Tested:** Extensive leaderboard with GPT-4, Claude, Llama, Mistral, and many others (correlates r=0.97 with MMLU)
- **Implementation Readiness:** **High** -- Full pipeline open-sourced under MIT license with automated scoring, batch evaluation scripts, normalizer, and leaderboard infrastructure. EQ-Bench 3 (2025) extends to active EQ via role-play scenarios judged by Claude Sonnet 3.7.

---

### 1.2 EmoBench: Evaluating the Emotional Intelligence of Large Language Models

- **Authors:** Sahand Sabour, Siyang Liu, Zheyuan Zhang, June M. Liu, Jinfeng Zhou, Alvionna S. Sunaryo, Juanzi Li, Tatia M.C. Lee, Rada Mihalcea, Minlie Huang
- **Year:** 2024
- **Venue:** ACL 2024 (Main Conference, 62nd Annual Meeting)
- **arXiv ID:** [2402.12071](https://arxiv.org/abs/2402.12071)
- **Ethical Frameworks:** Psychology-based emotional intelligence theory; Emotional Understanding (EU) and Emotional Application (EA); emotion management; thought facilitation through emotion
- **Dataset Size & Format:** 400 hand-crafted questions in English and Chinese; structured into EU (recognizing emotions and causes in complex scenarios) and EA (recommending effective emotional responses in dilemmas); multiple-choice format
- **Code/Data URLs:**
  - GitHub: [https://github.com/Sahandfer/EmoBench](https://github.com/Sahandfer/EmoBench)
- **LLMs Tested:** Multiple LLMs compared against average human performance; reveals considerable gap between LLM EI and human EI
- **Implementation Readiness:** **High** -- Code and data publicly available; bilingual (EN/CN); well-structured evaluation with clear metrics; published at top venue.

---

### 1.3 EmoBench-M: Benchmarking Emotional Intelligence for Multimodal Large Language Models

- **Authors:** He Hu, Yucheng Zhou, Lianzhong You, Hongbo Xu, Qianning Wang, Zheng Lian, Fei Richard Yu, Fei Ma, Laizhong Cui
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv ID:** [2502.04424](https://arxiv.org/abs/2502.04424)
- **Ethical Frameworks:** Multimodal emotional intelligence; foundational emotion recognition; conversational emotion understanding; socially complex emotion analysis
- **Dataset Size & Format:** 13 evaluation scenarios across 3 dimensions; multimodal inputs (text + visual)
- **Code/Data URLs:**
  - Project page: [https://emo-gml.github.io/](https://emo-gml.github.io/)
- **LLMs Tested:** Open-source and closed-source multimodal LLMs
- **Implementation Readiness:** **Medium** -- Code and datasets publicly available; extends EmoBench to multimodal domain; relatively new.

---

### 1.4 EmotionQueen: A Benchmark for Evaluating Empathy of Large Language Models

- **Authors:** Yuyan Chen, Hao Wang, Songzhou Yan, Sijia Liu, Yueze Li, Yi Zhao, Yanghua Xiao
- **Year:** 2024
- **Venue:** Findings of ACL 2024 (Bangkok, Thailand), pp. 2149-2176
- **arXiv ID:** [2409.13359](https://arxiv.org/abs/2409.13359)
- **ACL Anthology:** [2024.findings-acl.128](https://aclanthology.org/2024.findings-acl.128/)
- **Ethical Frameworks:** Empathy evaluation; emotion recognition; implicit emotional reasoning; intention recognition; key/mixed event recognition
- **Dataset Size & Format:** 10,000 user statements across 5 categories; 4 tasks (Key Event Recognition, Mixed Event Recognition, Implicit Emotional Recognition, Intention Recognition); two metrics: PASS rate and WIN rate
- **Code/Data URLs:** Available through ACL Anthology
- **LLMs Tested:** Vicuna-33B, LLaMA2-70B, Claude2, GPT-4; some LLMs surpass human empathy on specific tasks; Pearson correlation of 0.991 between auto scores and human ratings
- **Implementation Readiness:** **High** -- Large-scale dataset with automated metrics strongly correlated with human evaluation; published at top NLP venue.

---

### 1.5 EmotionBench (Apathetic or Empathetic?): Evaluating LLMs' Emotional Alignments with Humans

- **Authors:** Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, Michael R. Lyu
- **Year:** 2024
- **Venue:** NeurIPS 2024
- **arXiv ID:** [2308.03656](https://arxiv.org/abs/2308.03656)
- **Ethical Frameworks:** Emotion appraisal theory from psychology; 8 negative emotions across 36 factors; emotional alignment with humans
- **Dataset Size & Format:** 428 situations across 36 factors eliciting 8 emotions; human baseline from 1,266 annotators across different ethnic groups, genders, regions, and age groups
- **Code/Data URLs:**
  - GitHub: [https://github.com/CUHK-ARISE/EmotionBench](https://github.com/CUHK-ARISE/EmotionBench)
  - HuggingFace: [CUHK-ARISE/EmotionBench](https://huggingface.co/datasets/CUHK-ARISE/EmotionBench)
- **LLMs Tested:** 7 LLMs including GPT-4, Mixtral-8x22B, LLaMA-3.1, Text-Davinci-003
- **Implementation Readiness:** **High** -- Full code, data, and human baselines publicly available; published at top ML venue; robust cross-cultural human evaluation.

---

### 1.6 SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations

- **Authors:** Jina Suh, Lindy Le, Erfan Shayegani, Gonzalo Ramos, Judith Amores, Desmond C. Ong, Mary Czerwinski, Javier Hernandez
- **Year:** 2025
- **Venue:** arXiv preprint (submitted Sep 2025)
- **arXiv ID:** [2509.16437](https://arxiv.org/abs/2509.16437)
- **Ethical Frameworks:** 7-dimensional empathy taxonomy; cognitive empathy; affective empathy; instrumental and exploratory empathic functions; interactional behaviors in AI agents
- **Dataset Size & Format:** 695 conversations from 109 participants; 672 fully anonymized conversations with per-turn empathy annotations; 5-level empathy scale; LLM-based classifier achieves Spearman rho=0.369
- **Code/Data URLs:** Not yet publicly released at time of search
- **LLMs Tested:** General-purpose LLMs (specific models not disclosed); Microsoft Research affiliation
- **Implementation Readiness:** **Medium** -- Novel taxonomy with real-world data; human-centered annotations; data release status pending; relatively new preprint.

---

### 1.7 LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction

- **Authors:** Weichu Liu, Jing Xiong, Yuxuan Hu, Zixuan Li, Minghuan Tan, Ningning Mao, Hui Shen, Wendong Xu, Chaofan Tao, Min Yang, Chengming Li, Lingpeng Kong, Ngai Wong
- **Year:** 2025
- **Venue:** arXiv preprint (submitted Sep 2025, revised Jan 2026)
- **arXiv ID:** [2509.07403](https://arxiv.org/abs/2509.07403)
- **Ethical Frameworks:** Long-context emotional intelligence; emotion recognition; psychological knowledge application; empathetic generation
- **Dataset Size & Format:** 6 tasks (Emotion Classification, Detection, QA, Conversation, Summary, Expression); average context length of 15,341 tokens; simulates realistic long emotional dialogues
- **Code/Data URLs:**
  - GitHub: [https://github.com/LongEmotion/LongEmotion](https://github.com/LongEmotion/LongEmotion)
  - HuggingFace: [LongEmotion/LongEmotion](https://huggingface.co/datasets/LongEmotion/LongEmotion)
  - Project page: [https://longemotion.github.io/](https://longemotion.github.io/)
- **LLMs Tested:** Various models evaluated; includes Collaborative Emotional Modeling (CoEM) framework with RAG and multi-agent collaboration
- **Implementation Readiness:** **High** -- Dataset on HuggingFace; code on GitHub; novel long-context EI evaluation fills an important gap; includes framework for improvement.

---

### 1.8 EmpathicStories++: A Multimodal Dataset for Empathy towards Personal Experiences

- **Authors:** Jocelyn Shen, Yubin Kim, Mohit Hulse, Wazeer Zulfikar, Sharifa Alghowinem, Cynthia Breazeal, Hae Won Park
- **Year:** 2024
- **Venue:** Findings of ACL 2024
- **arXiv ID:** [2405.15708](https://arxiv.org/abs/2405.15708)
- **ACL Anthology:** [2024.findings-acl.268](https://aclanthology.org/2024.findings-acl.268/)
- **Ethical Frameworks:** Longitudinal empathy; personal experience-based empathy prediction; multimodal empathy assessment; in-the-wild naturalistic data
- **Dataset Size & Format:** 53 hours of video, audio, and text data; 41 participants; 269 sessions across month-long deployment; self-reported empathy ratings; multimodal (video/audio/text)
- **Code/Data URLs:**
  - Project page: [https://mitmedialab.github.io/empathic-stories-multimodal/](https://mitmedialab.github.io/empathic-stories-multimodal/)
- **LLMs Tested:** State-of-the-art models benchmarked for empathy prediction; specific models not disclosed in abstract
- **Implementation Readiness:** **Medium** -- First longitudinal empathy dataset; multimodal data publicly released; novel task formulation; primarily designed for empathy prediction rather than LLM evaluation per se.

---

### 1.9 Synth-Empathy: Towards High-Quality Synthetic Empathy Data

- **Authors:** Hao Liang, Linzhuang Sun, Jingxuan Wei, Xijie Huang, Linkun Sun, Bihui Yu, Conghui He, Wentao Zhang
- **Year:** 2024
- **Venue:** arXiv preprint (Jul 2024)
- **arXiv ID:** [2407.21669](https://arxiv.org/abs/2407.21669)
- **Ethical Frameworks:** Empathetic response generation; quality and diversity selection for empathy training data; domain knowledge-based quality curation
- **Dataset Size & Format:** 250K+ empathetic data points generated from EmpatheticDialogues (25K base conversations, 32 emotion labels); three-step pipeline: generation, quality selection, diversity selection
- **Code/Data URLs:** Not publicly disclosed in abstract
- **LLMs Tested:** Achieves state-of-the-art across multiple empathy benchmarks; specific models not detailed in abstract
- **Implementation Readiness:** **Medium** -- Novel data generation pipeline; SoTA results; code/data availability unclear; builds on publicly available EmpatheticDialogues.

---

### 1.10 SYNTHEMPATHY: A Scalable Empathy Corpus Generated Using LLMs Without Any Crowdsourcing

- **Authors:** Run Chen, Jun Shin, Julia Hirschberg
- **Year:** 2025
- **Venue:** arXiv preprint (Feb 2025)
- **arXiv ID:** [2502.17857](https://arxiv.org/abs/2502.17857)
- **Ethical Frameworks:** Chain of Empathy (CoE) prompting; psychotherapy-grounded empathy (CBT, DBT, Person-Centered Therapy, Reality Therapy); self-sufficient corpus construction
- **Dataset Size & Format:** 105,000 empathetic responses to real-life situations; fully LLM-generated without crowdsourcing; grounded in four therapeutic styles
- **Code/Data URLs:** Not disclosed in abstract
- **LLMs Tested:** Mistral 7B fine-tuned on corpus shows increased empathy scores
- **Implementation Readiness:** **Medium** -- Large-scale synthetic corpus; novel methodology grounded in psychotherapy; scalable approach; data availability pending.

---

### 1.11 PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models

- **Authors:** Chengbing Wang, Wuqiang Zheng, Yang Zhang, Fengbin Zhu, Junyi Cheng, Yi Xie, Wenjie Wang, Fuli Feng
- **Year:** 2025
- **Venue:** arXiv preprint (Jan 2025)
- **arXiv ID:** [2601.10532](https://arxiv.org/abs/2601.10532)
- **Ethical Frameworks:** Empathy Cycle theory; bidirectional empathy (supporter/seeker/bystander perspectives); psychology-grounded reward modeling
- **Dataset Size & Format:** Training data built on EmpatheticDialogues, augmented with GPT-4o scenario expansions and user personas; evaluated on EQ-Bench3
- **Code/Data URLs:**
  - GitHub: [https://github.com/ZhengWwwq/PERM](https://github.com/ZhengWwwq/PERM)
- **LLMs Tested:** Outperforms baselines by >10%; 70% user preference; evaluated on EQ-Bench3 and industrial conversation datasets
- **Implementation Readiness:** **High** -- GitHub code available; psychology-grounded methodology; practical reward model for empathetic alignment; evaluated on established benchmarks.

---

## 2. Human-Centered & Prosocial Evaluation

---

### 2.1 HumaniBench: A Human-Centric Framework for Large Multimodal Models Evaluation

- **Authors:** Shaina Raza, Aravind Narayanan, Vahid Reza Khazaie, Ashmal Vayani, Ahmed Y. Radwan, Mukund S. Chettiar, Amandeep Singh, Mubarak Shah, Deval Pandya
- **Year:** 2025
- **Venue:** arXiv preprint (May 2025); Vector Institute
- **arXiv ID:** [2505.11454](https://arxiv.org/abs/2505.11454)
- **Ethical Frameworks:** 7 Human-Centered AI (HCAI) principles: Fairness, Ethics, Understanding, Reasoning, Language Inclusivity, Empathy, Robustness
- **Dataset Size & Format:** 32,000 expert-verified image-question pairs derived from real-world news imagery; GPT-4o-assisted annotation pipeline with domain expert verification; 7 task types including open/closed-ended VQA, multilingual QA, visual grounding, empathetic captioning, robustness tests
- **Code/Data URLs:**
  - GitHub: [https://github.com/VectorInstitute/HumaniBench](https://github.com/VectorInstitute/HumaniBench)
  - Project page: [https://vectorinstitute.github.io/HumaniBench/](https://vectorinstitute.github.io/HumaniBench/)
- **LLMs Tested:** 15 state-of-the-art multimodal LLMs; closed-source models generally achieve highest overall performance
- **Implementation Readiness:** **High** -- Large-scale benchmark with full code and data; comprehensive evaluation suite; multi-dimensional assessment; from reputable institution (Vector Institute).

---

### 2.2 ProsocialDialog: A Prosocial Backbone for Conversational Agents

- **Authors:** Hyunwoo Kim, Youngjae Yu, Liwei Jiang, Ximing Lu, Daniel Khashabi, Gunhee Kim, Yejin Choi, Maarten Sap
- **Year:** 2022
- **Venue:** EMNLP 2022
- **arXiv ID:** [2205.12688](https://arxiv.org/abs/2205.12688)
- **ACL Anthology:** [2022.emnlp-main.267](https://aclanthology.org/2022.emnlp-main.267/)
- **Ethical Frameworks:** Social norm compliance; prosocial behavior; rules-of-thumb (RoTs) grounded in commonsense; dialogue safety; ethical response to problematic content
- **Dataset Size & Format:** 58K dialogues; 331K utterances; 160K unique rules-of-thumb (RoTs); 497K dialogue safety labels with free-form rationales; human-AI collaborative framework
- **Code/Data URLs:**
  - GitHub: [https://github.com/skywalker023/prosocial-dialog](https://github.com/skywalker023/prosocial-dialog)
  - HuggingFace: [allenai/prosocial-dialog](https://huggingface.co/datasets/allenai/prosocial-dialog)
- **LLMs Tested:** Includes Canary (safety detection module) and Prost (socially-informed dialogue agent); widely used for training/evaluating conversational agents
- **Implementation Readiness:** **High** -- Large-scale, publicly available on HuggingFace; well-established benchmark from Allen AI; includes safety labels and prosocial response models; widely adopted.

---

### 2.3 EmpatheticDialogues: Towards Empathetic Open-domain Conversation Models

- **Authors:** Hannah Rashkin, Eric Michael Smith, Margaret Li, Y-Lan Boureau
- **Year:** 2019
- **Venue:** ACL 2019 (57th Annual Meeting)
- **arXiv ID:** [1811.00207](https://arxiv.org/abs/1811.00207)
- **ACL Anthology:** [P19-1534](https://aclanthology.org/P19-1534/)
- **Ethical Frameworks:** Empathetic dialogue generation; grounded emotional situations; 32 emotion labels from biological responses
- **Dataset Size & Format:** 25,000 conversations; 32 emotion labels; grounded in emotional situations; human-to-human dialogues
- **Code/Data URLs:**
  - GitHub: [https://github.com/facebookresearch/EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues)
  - HuggingFace: [facebook/empathetic_dialogues](https://huggingface.co/datasets/facebook/empathetic_dialogues)
  - Kaggle: [atharvjairath/empathetic-dialogues-facebook-ai](https://www.kaggle.com/datasets/atharvjairath/empathetic-dialogues-facebook-ai)
- **LLMs Tested:** Foundation dataset used extensively to train and evaluate many LLMs; models trained on it are perceived as more empathetic by human evaluators
- **Implementation Readiness:** **High** -- Foundational empathy dataset; widely available across multiple platforms; standard benchmark in the field; extensively used for LLM training and evaluation since 2019.

---

## 3. Moral Sentiment & Emotional Moral Reasoning

---

### 3.1 MoralBench: Moral Evaluation of LLMs

- **Authors:** Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, Yongfeng Zhang
- **Year:** 2024
- **Venue:** ACM SIGKDD Explorations, Volume 27, Issue 1
- **arXiv ID:** [2406.04428](https://arxiv.org/abs/2406.04428)
- **Ethical Frameworks:** Moral Foundations Theory (care, fairness, loyalty, authority, purity); contextual moral reasoning; moral identity assessment
- **Dataset Size & Format:** Three-part dataset: (1) 1K high-fidelity safety-alignment prompts, (2) 10K abstracted variation set for domain transfer, (3) 19,132-record rich metadata preference dataset with structured ethical annotations; covers emotional intensity and role-dependent factors
- **Code/Data URLs:** Dataset on Google Drive; code on GitHub (referenced but URL masked in arXiv)
- **LLMs Tested:** LLaMA-2, GPT-4, and others; some show strong moral alignment but lack deep understanding of moral principles
- **Implementation Readiness:** **High** -- Published in KDD Explorations; large-scale multi-component dataset; combines quantitative analysis with ethics scholar input; code and data available.

---

### 3.2 MFTCXplain: A Multilingual Benchmark Dataset for Evaluating the Moral Reasoning of LLMs through Multi-hop Hate Speech Explanation

- **Authors:** Jackson Trager, Francielle Vargas, Diego Alves, Matteo Guida, Mikel K. Ngueajio, Ameeta Agrawal, Yalda Daryani, Farzan Karimi-Malekabadi, Flor Miriam Plaza-del-Arco
- **Year:** 2025
- **Venue:** Findings of EMNLP 2025
- **arXiv ID:** [2506.19073](https://arxiv.org/abs/2506.19073)
- **ACL Anthology:** [2025.findings-emnlp.851](https://aclanthology.org/2025.findings-emnlp.851/)
- **Ethical Frameworks:** Moral Foundations Theory (Harm, Degradation, Fairness, Loyalty); multi-hop moral reasoning; explainable AI; multilingual moral sentiment
- **Dataset Size & Format:** 3,000 tweets in 4 languages (Portuguese, Persian, Italian, English); annotated for hate speech, fine-grained moral categories, and text span rationales; expert-annotated
- **Code/Data URLs:** Not disclosed in abstract; available through ACL Anthology
- **LLMs Tested:** Multiple LLMs; hate speech detection F1 up to 0.836 (LLaMA-70B IT); moral sentiment prediction F1 < 0.35
- **Implementation Readiness:** **Medium** -- First multilingual moral reasoning explanation dataset; expert-annotated; published at top venue; but relatively small scale (3K tweets); data availability through ACL.

---

### 3.3 ConflictScope: Generative Value Conflicts Reveal LLM Priorities

- **Authors:** Andy Liu, Kshitish Ghate, Mona Diab, Daniel Fried, Atoosa Kasirzadeh, Max Kleiman-Weiner
- **Year:** 2025
- **Venue:** arXiv preprint (Sep 2025)
- **arXiv ID:** [2509.25369](https://arxiv.org/abs/2509.25369)
- **Ethical Frameworks:** Value conflict resolution; HHH (helpfulness, honesty, harmlessness); personal-protective values (autonomy, responsibility, harmlessness); fairness; dual-mode evaluation (MCQ + open-ended)
- **Dataset Size & Format:** Automated pipeline generating value-conflict dilemmas from user-defined value sets; systematic pairwise comparison of values; MCQ and open-ended formats
- **Code/Data URLs:** Not disclosed in abstract
- **LLMs Tested:** Multiple models; system prompting improves alignment by 14%; models shift from protective to personal values in open-ended settings
- **Implementation Readiness:** **Medium** -- Novel automated pipeline for generating evaluation scenarios; flexible value set input; dual-mode evaluation provides nuanced insights; code availability pending.

---

## 4. Social Skills & Interpersonal Ethics

---

### 4.1 SocialEval: Evaluating Social Intelligence of Large Language Models

- **Authors:** Jinfeng Zhou, Yuxuan Chen, Yihan Shi, Xuanming Zhang, Leqi Lei, Yi Feng, Zexuan Xiong, Miao Yan, Xunzhi Wang, Yaru Cao, Jianing Yin, Shuai Wang, Quanyu Dai, Zhenhua Dong, Hongning Wang, Minlie Huang
- **Year:** 2025
- **Venue:** ACL 2025 (63rd Annual Meeting, Vienna, Austria)
- **arXiv ID:** [2506.00900](https://arxiv.org/abs/2506.00900)
- **Ethical Frameworks:** Social intelligence; prosocial behavior evaluation; interpersonal ability; outcome- and process-oriented evaluation; 5 aspects and 32 specific abilities
- **Dataset Size & Format:** Script-based bilingual benchmark; narrative scripts structured as world trees with plot lines; manually crafted scenarios
- **Code/Data URLs:**
  - GitHub: [https://github.com/thu-coai/SocialEval](https://github.com/thu-coai/SocialEval)
- **LLMs Tested:** 19 LLMs including GPT series, Claude-3 series, Llama-Instruct, Qwen-2.5-Instruct, Mistral-Instruct, DeepSeek series
- **Implementation Readiness:** **High** -- Published at ACL 2025; comprehensive 32-ability evaluation; bilingual; code available; tests 19 models; reveals LLMs prefer prosocial behaviors even at cost of goal failure.

---

### 4.2 SI-Bench: Benchmarking Social Intelligence of Large Language Models in Human-to-Human Conversations

- **Authors:** Shuai Huang, Wenxuan Zhao, Jun Gao
- **Year:** 2025
- **Venue:** arXiv preprint (Oct 2025)
- **arXiv ID:** [2510.23182](https://arxiv.org/abs/2510.23182)
- **Ethical Frameworks:** Social intelligence in authentic interpersonal interactions; process-outcome decoupled evaluation; relationship-building skills
- **Dataset Size & Format:** 2,221 authentic multi-turn dialogues from social networking platform; 312 manually annotated dialogues across 8 models; Chinese language; anonymized
- **Code/Data URLs:**
  - GitHub: [https://github.com/SI-Bench/SI-Bench.git](https://github.com/SI-Bench/SI-Bench.git)
- **LLMs Tested:** 8 major LLMs; reveals thought-action gap (models outperform human experts in process quality but lag in reply quality); CoT reasoning may degrade social dialogue performance
- **Implementation Readiness:** **High** -- Authentic real-world data with high ecological validity; GitHub-available; novel process-outcome framework; identifies practical limitations of CoT in social tasks.

---

### 4.3 RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity

- **Authors:** Jisu Shin, Hoyun Song, Juhyun Oh, Changgeon Ko, Eunsu Kim, Chani Jung, Alice Oh
- **Year:** 2025
- **Venue:** arXiv preprint (Sep 2025)
- **arXiv ID:** [2509.25897](https://arxiv.org/abs/2509.25897)
- **Ethical Frameworks:** Role conflict theory from sociology; social expectation balancing; situational urgency; contextual sensitivity in ambiguous moral dilemmas; interpersonal ethics
- **Dataset Size & Format:** 13K+ realistic role conflict scenarios across 65 roles; three-stage generation pipeline; systematically varying social expectations and urgency levels
- **Code/Data URLs:** Not disclosed in abstract; CC BY-SA 4.0 license
- **LLMs Tested:** 10 LLMs analyzed; reveals dominant bias toward Family and Occupation domains; preference for male roles and Abrahamic religions
- **Implementation Readiness:** **Medium** -- Large-scale scenario generation; systematic variation of contextual factors; reveals important biases; but code/data availability not confirmed; preprint stage.

---

### 4.4 EtiCor: Corpus for Analyzing LLMs for Etiquettes

- **Authors:** Ashutosh Dwivedi, Pradhyumna Lavania, Ashutosh Modi
- **Year:** 2023
- **Venue:** EMNLP 2023 (Main Conference)
- **arXiv ID:** [2310.18974](https://arxiv.org/abs/2310.18974)
- **ACL Anthology:** [2023.emnlp-main.428](https://aclanthology.org/2023.emnlp-main.428/)
- **Ethical Frameworks:** Social etiquette and norms from 5 global regions; region-specific social norm understanding; etiquette sensitivity
- **Dataset Size & Format:** Texts about social norms from 5 regions; Etiquette Sensitivity evaluation task
- **LLMs Tested:** Delphi, Falcon40B, GPT-3.5; LLMs mostly fail to understand etiquettes from non-Western regions
- **Implementation Readiness:** **Medium** -- Published at top venue; addresses important cultural gap; but smaller scale; expanded by EtiCor++ in 2025.

---

### 4.5 EtiCor++: Towards Understanding Etiquettical Bias in LLMs

- **Authors:** Ashutosh Dwivedi, Siddhant Shivdutt Singh, Ashutosh Modi
- **Year:** 2025
- **Venue:** ACL Findings 2025
- **arXiv ID:** [2506.08488](https://arxiv.org/abs/2506.08488)
- **Ethical Frameworks:** Extended cross-cultural etiquette evaluation; global social norms including previously missing cultures (Aboriginal Australians, Maori, Chinese, Russian, southern African); etiquettical bias detection; correlation between regional etiquettes
- **Dataset Size & Format:** Expanded from EtiCor with additional cultures and regions; cleaned noisy samples; new tasks and metrics; covers Asia, Latin America, Middle East/Africa, North America/Europe, and more
- **Code/Data URLs:** Not disclosed in abstract
- **LLMs Tested:** Gemini, Gemma, Phi, Llama
- **Implementation Readiness:** **Medium** -- Significant expansion of EtiCor; published at ACL; addresses cultural diversity; new evaluation metrics; data availability pending confirmation.

---

## Summary Table

| # | Benchmark | Year | Venue | Dataset Size | Key Focus | Impl. Readiness |
|---|-----------|------|-------|-------------|-----------|-----------------|
| 1.1 | EQ-Bench | 2023 | arXiv | 60 questions | Emotional intelligence | High |
| 1.2 | EmoBench | 2024 | ACL 2024 | 400 questions (EN/CN) | EI understanding & application | High |
| 1.3 | EmoBench-M | 2025 | arXiv | 13 scenarios | Multimodal EI | Medium |
| 1.4 | EmotionQueen | 2024 | ACL 2024 Findings | 10K statements | Empathy (4 tasks) | High |
| 1.5 | EmotionBench | 2024 | NeurIPS 2024 | 428 situations | Emotional appraisal alignment | High |
| 1.6 | SENSE-7 | 2025 | arXiv | 695 conversations | 7-dim empathy taxonomy | Medium |
| 1.7 | LongEmotion | 2025 | arXiv | 6 tasks, 15K tokens avg | Long-context EI | High |
| 1.8 | EmpathicStories++ | 2024 | ACL 2024 Findings | 53hr multimodal | Longitudinal empathy | Medium |
| 1.9 | Synth-Empathy | 2024 | arXiv | 250K+ data points | Synthetic empathy data | Medium |
| 1.10 | SYNTHEMPATHY | 2025 | arXiv | 105K responses | Crowdsource-free empathy | Medium |
| 1.11 | PERM | 2025 | arXiv | Based on ED + augmented | Empathetic reward modeling | High |
| 2.1 | HumaniBench | 2025 | arXiv | 32K image-question pairs | 7 HCAI principles | High |
| 2.2 | ProsocialDialog | 2022 | EMNLP 2022 | 58K dialogues | Prosocial norms | High |
| 2.3 | EmpatheticDialogues | 2019 | ACL 2019 | 25K conversations | Empathetic dialogue | High |
| 3.1 | MoralBench | 2024 | KDD Explorations | 30K+ records | Moral Foundations Theory | High |
| 3.2 | MFTCXplain | 2025 | EMNLP 2025 Findings | 3K tweets (4 langs) | Multilingual moral reasoning | Medium |
| 3.3 | ConflictScope | 2025 | arXiv | Auto-generated | Value conflict prioritization | Medium |
| 4.1 | SocialEval | 2025 | ACL 2025 | Script-based, bilingual | 32 social abilities | High |
| 4.2 | SI-Bench | 2025 | arXiv | 2,221 dialogues | Authentic social intelligence | High |
| 4.3 | RoleConflictBench | 2025 | arXiv | 13K+ scenarios | Role conflict sensitivity | Medium |
| 4.4 | EtiCor | 2023 | EMNLP 2023 | Multi-region corpus | Global etiquette | Medium |
| 4.5 | EtiCor++ | 2025 | ACL Findings 2025 | Expanded multi-culture | Etiquettical bias | Medium |

---

## Key Observations

1. **Rapid growth in 2024-2025:** The majority of empathy/EI benchmarks are from 2024-2025, reflecting growing recognition that emotional and social competencies are essential for aligned AI.

2. **Psychology-grounded approaches dominate:** Most benchmarks draw on established psychological theories (emotion appraisal theory, Empathy Cycle, Moral Foundations Theory, emotional intelligence frameworks), lending scientific rigor.

3. **Gap between EI and general intelligence:** Multiple benchmarks (EmoBench, EmotionBench, SI-Bench) report significant gaps between LLM emotional intelligence and human performance, even for frontier models.

4. **Prosocial bias in LLMs:** SocialEval reveals that LLMs exhibit prosociality and prefer positive social behaviors even at the cost of goal failure, suggesting over-alignment in social contexts.

5. **Cultural and linguistic diversity expanding:** EtiCor++, MFTCXplain, and SENSE-7 address cross-cultural empathy and moral reasoning, though Western-centric biases persist.

6. **Multimodal frontier:** HumaniBench and EmoBench-M extend evaluation to vision-language models, reflecting the multimodal trajectory of LLM development.

7. **Implementation-ready resources:** 10 of 20 benchmarks are rated High implementation readiness, with publicly available code, data, and established evaluation pipelines.

---

## Excluded Benchmarks (Already Known)

The following were explicitly excluded per instructions: MoralExceptQA, ETHICS (Hendrycks), MoReBench, ValueBench, DailyDilemmas, CulturalBench, CDEval, Delphi, GlobalOpinionQA, WorldValuesBench, CALI, MultiTP, MoralChoice, Scruples, Social Chemistry 101, Moral Stories, MIC, DeNEVIL, TrustLLM, DecodingTrust, BeaverTails, HarmBench, SaGE, CLAVE, Eagle, TrolleyBench, CValues, CARE dataset, MVPBench, UniMoral, FLAMES, NormAd, LocalValueBench.

---

*Report generated by Agent 15 | Date: 2026-02-07*
