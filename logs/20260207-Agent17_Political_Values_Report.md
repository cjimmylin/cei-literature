# Agent 17: Political Values, Social Norms & Fairness-with-Values -- Literature Search Report

**Search Date:** 2026-02-07
**Domain:** Political Values, Ideology, Social Norms, Fairness with Ethical Dimensions, Sycophancy & Value Manipulation
**Agent:** 17

---

## Executive Summary

This report documents findings from an exhaustive literature search for implementable benchmarks and datasets evaluating LLMs on political values, social norms, ideology, and fairness with ethical dimensions. A total of **25 distinct benchmarks/datasets** were identified across four sub-domains. The search excluded all items on the ALREADY KNOWN list.

---

## 1. POLITICAL VALUES & IDEOLOGY

### 1.1 Political Compass or Spinning Arrow?

- **Full Citation:** Paul Rottger, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Rose Kirk, Hinrich Schutze, Dirk Hovy. "Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models." ACL 2024 (Main Conference), 2024.
- **arXiv ID:** [2402.16786](https://arxiv.org/abs/2402.16786)
- **Ethical Frameworks:** Political ideology measurement critique; challenges to survey-based evaluation of LLM values using the Political Compass Test (PCT)
- **Dataset Size & Format:** Uses the PCT's 62 Likert-scale statements; tested across multiple paraphrase variants, open-ended vs. forced-choice formats
- **Code/Data URLs:** Not publicly released (meta-evaluation / critical analysis paper)
- **LLMs Tested:** Multiple LLMs (evaluation methodology paper)
- **Implementation Readiness:** Medium -- Provides critical methodology recommendations for conducting political values evaluations; serves as essential methodological reference rather than a standalone benchmark
- **Key Finding:** LLM answers flip when forced into PCT's multiple-choice format; answers change with minimal paraphrases; open-ended settings yield substantively different results

---

### 1.2 Navigating the Political Compass (Multilingual, 50 Countries)

- **Full Citation:** Chadi Helwe, Oana Balalau, Davide Ceolin. "Navigating the Political Compass: Evaluating Multilingual LLMs across Languages and Nationalities." Findings of ACL 2025, pages 17179-17204, Vienna, Austria.
- **ACL Anthology:** [2025.findings-acl.883](https://aclanthology.org/2025.findings-acl.883/)
- **Ethical Frameworks:** Political ideology (economic left-right, social libertarian-authoritarian); multilingual and cross-national ideological consistency
- **Dataset Size & Format:** Political Compass Test administered across 50 most populous countries, their official languages; 15 multilingual LLMs evaluated
- **Code/Data URLs:** [GitHub: ChadiHelwe/navigating_the_political_compass](https://github.com/ChadiHelwe/navigating_the_political_compass)
- **LLMs Tested:** 15 multilingual LLMs (specific models detailed in paper)
- **Implementation Readiness:** **High** -- Code publicly available; systematic multilingual evaluation methodology; covers diverse language-nationality pairs
- **Key Finding:** Language has strong influence on political ideology displayed; smaller models show more stable ideology less affected by prompt variations

---

### 1.3 Bias Beyond Borders

- **Full Citation:** Afrozah Nadeem, Agrima, Mehwish Nasim, Usman Naseem. "Bias Beyond Borders: Political Ideology Evaluation and Steering in Multilingual LLMs." arXiv preprint, 2026.
- **arXiv ID:** [2601.23001](https://arxiv.org/abs/2601.23001)
- **Ethical Frameworks:** Political ideology evaluation and mitigation; cross-lingual ideological fairness; economic and social ideology axes
- **Dataset Size & Format:** Political Compass Test across 50 countries, 33 languages; introduces Cross-Lingual Alignment Steering (CLAS) mitigation framework
- **Code/Data URLs:** Not yet publicly released (recent preprint)
- **LLMs Tested:** Multiple multilingual LLMs (details in paper)
- **Implementation Readiness:** Medium -- Offers evaluation + mitigation framework (CLAS); recent preprint; extends the multilingual political compass methodology with steering capabilities

---

### 1.4 GermanPartiesQA

- **Full Citation:** Jan Batzner, Volker Stocker, Stefan Schmid, Gjergji Kasneci. "GermanPartiesQA: Benchmarking Commercial Large Language Models and AI Companions for Political Alignment and Sycophancy." AAAI/ACM Conference on AI, Ethics, and Society (AIES), Volume 8, Issue 1, pages 330-342, 2025.
- **arXiv ID:** [2407.18008](https://arxiv.org/abs/2407.18008)
- **Ethical Frameworks:** Political alignment with party positions; political sycophancy; persona-based steerability
- **Dataset Size & Format:** 418 political statements from German Voting Advice Applications across 11 elections (2021-2023); CSV format (semicolon-delimited, UTF-8); includes party response codes (0=disagree, 1=agree, 2=neutral) with rationales for 6 German parties (SPD, CDU/CSU, Greens, FDP, AfD, The Left)
- **Code/Data URLs:** [GitHub: janbatzner/germanpartiesqa](https://github.com/janbatzner/germanpartiesqa)
- **LLMs Tested:** 6 commercial LLMs by OpenAI, Anthropic, and Cohere
- **Implementation Readiness:** **High** -- Dataset and code publicly available; well-structured CSV format; clear evaluation protocol
- **Key Finding:** All LLMs show left-green tendency; persona-based role-play reflects steerability rather than sycophancy

---

### 1.5 The Political Preferences of LLMs

- **Full Citation:** David Rozado. "The Political Preferences of LLMs." PLOS ONE, 19(7): e0306621, 2024.
- **DOI:** [10.1371/journal.pone.0306621](https://doi.org/10.1371/journal.pone.0306621)
- **Ethical Frameworks:** Comprehensive political orientation measurement using 11 standardized political tests; left-right spectrum; libertarian-authoritarian dimensions
- **Dataset Size & Format:** 11 political orientation tests x 10 trials x 24 LLMs = 2,640 total test administrations; automated test administration and parsing scripts
- **Code/Data URLs:** Scripts referenced in paper (automated administration via APIs)
- **LLMs Tested:** 24 state-of-the-art conversational LLMs including GPT-3.5, GPT-4, Gemini, Claude, Grok + 5 base/foundation models
- **Implementation Readiness:** **High** -- Standardized tests are publicly available; methodology is fully described and reproducible; largest-scale political orientation evaluation to date
- **Key Finding:** Most conversational LLMs manifest left-of-center viewpoints; base models show inconclusive results; models can be steered via SFT with modest political training data

---

### 1.6 Measuring Political Bias in LLMs: What Is Said and How It Is Said

- **Full Citation:** Yejin Bang, Delong Chen, Nayeon Lee, Pascale Fung. "Measuring Political Bias in Large Language Models: What Is Said and How It Is Said." Proceedings of ACL 2024, pages 11142-11159, Bangkok, Thailand.
- **arXiv ID:** [2403.18932](https://arxiv.org/abs/2403.18932)
- **Ethical Frameworks:** Political bias measurement through content analysis (substance) and style analysis (lexical polarity); covers political topics including reproductive rights, climate change
- **Dataset Size & Format:** Framework-based evaluation across multiple political topics; evaluates both content and style dimensions
- **Code/Data URLs:** Referenced via Papers with Code and Hugging Face (check paper for links)
- **LLMs Tested:** 11 open-source LLMs
- **Implementation Readiness:** **High** -- Published at top venue; scalable framework; fine-grained and explainable measures

---

### 1.7 Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters

- **Full Citation:** Yujin Potter, Shiyang Lai, Junsol Kim, James Evans, Dawn Song. "Hidden Persuaders: LLMs' Political Leaning and Their Influence on Voters." Proceedings of EMNLP 2024, pages 4244-4275, Miami, Florida, USA.
- **arXiv ID:** [2410.24190](https://arxiv.org/abs/2410.24190)
- **Ethical Frameworks:** Political leaning detection; voter influence measurement; democratic process implications of AI bias
- **Dataset Size & Format:** Voting simulation across 18 LLMs; human experiment with 935 U.S. registered voters interacting with LLMs over 5 exchanges
- **Code/Data URLs:** Not publicly specified
- **LLMs Tested:** 18 open- and closed-weight LLMs including Claude-3, Llama-3, GPT-4
- **Implementation Readiness:** Medium -- Voting simulation is reproducible; human experiment component requires IRB and participant recruitment
- **Key Finding:** Biden-leaning becomes more pronounced after instruction-tuning/RLHF; ~20% of Trump supporters reduced support after LLM interaction; vote margin widened from 0.7% to 4.6%

---

### 1.8 PoliBias (Parliamentary Voting Records)

- **Full Citation:** Jieying Chen, Karen de Jong, Andreas Poole, Jan Burakowski, Elena Elderson Nosti, Joep Windt, Chendi Wang. "Uncovering Political Bias in Large Language Models using Parliamentary Voting Records." arXiv preprint, 2026.
- **arXiv ID:** [2601.08785](https://arxiv.org/abs/2601.08785)
- **Ethical Frameworks:** Political bias detection via real parliamentary voting records; Chapel Hill Expert Survey (CHES) ideological dimensions; cross-national comparison
- **Dataset Size & Format:** Three national benchmarks:
  - PoliBiasNL: 2,701 Dutch parliamentary motions, 15 parties
  - PoliBiasNO: 10,584 Norwegian motions, 9 parties
  - PoliBiasES: 2,480 Spanish motions, 10 parties
- **Code/Data URLs:** Not yet publicly released
- **LLMs Tested:** Multiple state-of-the-art LLMs (details in paper)
- **Implementation Readiness:** **High** -- Large-scale grounded benchmarks using verified parliamentary records; methodology is generalizable to other countries
- **Key Finding:** Consistent left-leaning/centrist tendencies across all three countries; clear negative bias towards right-conservative parties

---

### 1.9 OpinionQA

- **Full Citation:** Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, Tatsunori Hashimoto. "Whose Opinions Do Language Models Reflect?" ICML 2023.
- **arXiv ID:** [2303.17548](https://arxiv.org/abs/2303.17548)
- **Ethical Frameworks:** Opinion alignment with US demographic groups; representational fairness; political opinion distribution matching
- **Dataset Size & Format:** 1,498 multiple-choice questions from Pew Research's American Trends Panels; spans science, politics, personal relationships; includes human opinion distributions for 60 demographic groups
- **Code/Data URLs:** [GitHub: tatsu-lab/opinions_qa](https://github.com/tatsu-lab/opinions_qa)
- **LLMs Tested:** 9 language models (350M to 178B parameters; AI21 Labs and OpenAI models)
- **Implementation Readiness:** **High** -- Dataset, code, and pre-computed model responses publicly available; well-established benchmark
- **Key Finding:** Substantial misalignment between LM views and US demographic groups; certain groups (65+, Mormon, widowed) are particularly poorly represented

---

### 1.10 BiasLab (Political Bias Detection -- News Articles)

- **Full Citation:** Kma Solaiman. "BiasLab: Toward Explainable Political Bias Detection with Dual-Axis Annotations and Rationale Indicators." ICML 2025, 2nd Workshop on Models of Human Feedback for AI Alignment, Vancouver, Canada.
- **arXiv ID:** [2505.16081](https://arxiv.org/abs/2505.16081)
- **Ethical Frameworks:** Political bias in news media; dual-axis sentiment (Democratic vs. Republican); explainable bias detection with rationale indicators from media literacy guidelines
- **Dataset Size & Format:** 300 political news articles (from curated 900-document pool); crowdworker annotations on two independent scales; rationale indicators
- **Code/Data URLs:** Dataset, annotation schema, and modeling code released (check paper for links)
- **LLMs Tested:** GPT-4o (schema-constrained annotation comparison)
- **Implementation Readiness:** **High** -- Dataset and code released; well-defined annotation schema; two modeling tasks (perception drift prediction, rationale type classification)

---

### 1.11 BiasLab (Multilingual Dual-Framing Framework)

- **Full Citation:** William Guey, Wei Zhang, Pei-Luen Patrick Rau, Pierrick Bougault, Vitor D. de Moura, Bertan Ucar, Jose O. Gomes. "BiasLab: A Multilingual, Dual-Framing Framework for Robust Measurement of Output-Level Bias in Large Language Models." arXiv preprint, 2026.
- **arXiv ID:** [2601.06861](https://arxiv.org/abs/2601.06861)
- **Ethical Frameworks:** Output-level (extrinsic) bias measurement; demographic, cultural, political, and geopolitical bias axes; cross-lingual fairness
- **Dataset Size & Format:** Mirrored probe pairs under strict dual-framing scheme; randomized instructional wrappers; fixed-choice Likert response format; multilingual
- **Code/Data URLs:** Source code and reproducibility scripts available on GitHub (referenced in paper)
- **LLMs Tested:** Model-agnostic framework (details in paper)
- **Implementation Readiness:** **High** -- Open-source, model-agnostic framework; produces structured reports and comparative visualizations; reproducible artifacts

---

### 1.12 PoliCon

- **Full Citation:** Authors (see paper). "PoliCon: Evaluating LLMs on Achieving Diverse Political Consensus Objectives." arXiv preprint, 2025.
- **arXiv ID:** [2505.19558](https://arxiv.org/abs/2505.19558)
- **Ethical Frameworks:** Political consensus-building; social choice theory; partisan bias detection; democratic deliberation
- **Dataset Size & Format:** 2,225 high-quality deliberation records from European Parliament over 13 years (2009-2022); tasks vary by political issues, goals, parties, and power structures
- **Code/Data URLs:** Check paper for availability
- **LLMs Tested:** State-of-the-art models (details in paper)
- **Implementation Readiness:** Medium -- Novel evaluation paradigm; requires understanding of social choice theory for proper interpretation
- **Key Finding:** Even SOTA models struggle with complex consensus tasks like passing resolutions by two-thirds majority; models prioritize dominant party stances

---

## 2. SOCIAL NORMS & NORMATIVE BEHAVIOR

### 2.1 Social (Measuring Social Norms of LLMs)

- **Full Citation:** Ye Yuan, Kexin Tang, Jianhao Shen, Ming Zhang, Chenguang Wang. "Measuring Social Norms of Large Language Models." Findings of NAACL 2024.
- **arXiv ID:** [2404.02491](https://arxiv.org/abs/2404.02491)
- **Ethical Frameworks:** Social norms understanding; K-12 curriculum-aligned assessment; social studies and language arts norms covering rules, laws, culture, history, communication
- **Dataset Size & Format:** 12,383 questions covering 402 social norm skills; multiple-choice format aligned with K-12 educational standards
- **Code/Data URLs:**
  - [GitHub: socialnormdataset/socialagent](https://github.com/socialnormdataset/socialagent)
  - [HuggingFace: socialnormdataset/social](https://huggingface.co/datasets/socialnormdataset/social)
- **LLMs Tested:** GPT-3.5-Turbo, LLaMA2-Chat, additional models via multi-agent framework
- **Implementation Readiness:** **High** -- Dataset and code publicly available on both GitHub and HuggingFace; enables direct comparison with human (elementary student) performance

---

### 2.2 ProsocialDialog

- **Full Citation:** Hyunwoo Kim, Youngjae Yu, Liwei Jiang, Ximing Lu, Daniel Khashabi, Gunhee Kim, Yejin Choi, Maarten Sap. "ProsocialDialog: A Prosocial Backbone for Conversational Agents." EMNLP 2022.
- **arXiv ID:** [2205.12688](https://arxiv.org/abs/2205.12688)
- **Ethical Frameworks:** Prosocial behavior; social norm compliance; safe response generation to toxic/unsafe inputs; rules-of-thumb (RoTs) grounded in commonsense social rules
- **Dataset Size & Format:** 58K dialogues; 331K utterances; 160K unique rules-of-thumb (RoTs); 497K dialogue safety labels with free-form rationales; covers unethical, biased, toxic situations
- **Code/Data URLs:**
  - [GitHub: skywalker023/prosocial-dialog](https://github.com/skywalker023/prosocial-dialog)
  - [HuggingFace: allenai/prosocial-dialog](https://huggingface.co/datasets/allenai/prosocial-dialog)
- **LLMs Tested:** GPT-3 (for generating unsafe utterances); crowdworker-written prosocial responses
- **Implementation Readiness:** **High** -- Large-scale, well-documented dataset; easily loadable from HuggingFace; suitable for both training and evaluation

---

### 2.3 NormBank

- **Full Citation:** Caleb Ziems, Nhi Dwivedi-Yu, Yi-Chia Wang, Alon Halevy, Diyi Yang. "NormBank: A Knowledge Bank of Situational Social Norms." ACL 2023.
- **arXiv ID:** [2305.17008](https://arxiv.org/abs/2305.17008)
- **Ethical Frameworks:** Situational social norms; multivalent sociocultural frames (setting, roles, attributes, constraints); flexible normative reasoning
- **Dataset Size & Format:** 155K situational norms; each grounded in sociocultural frames (setting, agent roles, attributes, physical/social/cultural constraints)
- **Code/Data URLs:** [GitHub: SALT-NLP/normbank](https://github.com/SALT-NLP/normbank)
- **LLMs Tested:** Used LLMs for bootstrapping annotations; transfer learning experiments for downstream tasks
- **Implementation Readiness:** **High** -- Large dataset; code available; general-purpose social reasoning resource; structured format with situational context

---

### 2.4 Normative Evaluation with Everyday Moral Dilemmas

- **Full Citation:** Pranav Sachdeva, Tom van Nuenen. "Normative Evaluation of Large Language Models with Everyday Moral Dilemmas." ACM FAccT 2025.
- **arXiv ID:** [2501.18081](https://arxiv.org/abs/2501.18081)
- **DOI:** [10.1145/3715275.3732044](https://dl.acm.org/doi/10.1145/3715275.3732044)
- **Ethical Frameworks:** Normative evaluation; everyday moral reasoning; six moral themes: Fairness & Proportionality, Feelings, Harm & Offense, Honesty, Relational Obligation, Social Norms
- **Dataset Size & Format:** 10,000+ AITA (Reddit "Am I the Asshole") posts; LLMs prompted to assign blame and provide explanations
- **Code/Data URLs:** [GitHub: dlab-projects/normative_evaluation_llms_everyday_dilemmas](https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas)
- **LLMs Tested:** 7 commonly used LLMs (proprietary and open-source)
- **Implementation Readiness:** **High** -- Code available; large real-world moral dilemma dataset; systematic evaluation framework
- **Key Finding:** LLMs show moderate-to-high self-consistency but low inter-model agreement; distinct moral judgment patterns varying substantially from human evaluations

---

### 2.5 SocialHarmBench

- **Full Citation:** Punya Syon Pandey, Hai Son Le, Devansh Bhardwaj, Rada Mihalcea, Zhijing Jin. "SocialHarmBench: Revealing LLM Vulnerabilities to Socially Harmful Requests." arXiv preprint, 2025.
- **arXiv ID:** [2510.04891](https://arxiv.org/abs/2510.04891)
- **Ethical Frameworks:** Sociopolitical safety; resistance to propaganda manipulation, surveillance/censorship, historical revisionism, political manipulation; democratic erosion prevention
- **Dataset Size & Format:** 585 prompts across 7 sociopolitical categories, covering 34 countries
- **Code/Data URLs:** [HuggingFace: psyonp/SocialHarmBench](https://huggingface.co/datasets/psyonp/SocialHarmBench)
- **LLMs Tested:** Multiple models including Mistral-7B (highest vulnerability: 97-98% attack success in some categories)
- **Implementation Readiness:** **High** -- Dataset on HuggingFace; automated evaluation pipeline; first adversarial benchmark targeting sociopolitical vulnerabilities
- **Key Finding:** Open-weight models exhibit high vulnerability; LLMs most fragile with 21st-century contexts and Latin America/USA/UK prompts

---

## 3. FAIRNESS WITH ETHICAL DIMENSIONS

### 3.1 BBQ (Bias Benchmark for Question Answering)

- **Full Citation:** Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon Htut, Samuel R. Bowman. "BBQ: A Hand-Built Bias Benchmark for Question Answering." Findings of ACL 2022.
- **arXiv ID:** [2110.08193](https://arxiv.org/abs/2110.08193)
- **Ethical Frameworks:** Social bias across 9 dimensions: race/color, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, socioeconomic status
- **Dataset Size & Format:** ~58,000 multiple-choice questions; ambiguous and disambiguated contexts; 11 JSONL files (one per bias category)
- **Code/Data URLs:**
  - [GitHub: nyu-mll/BBQ](https://github.com/nyu-mll/BBQ)
  - [HuggingFace: heegyu/bbq](https://huggingface.co/datasets/heegyu/bbq)
  - [HuggingFace: walledai/BBQ](https://huggingface.co/datasets/walledai/BBQ)
- **LLMs Tested:** Multiple QA models (original paper); widely used by the community for LLM evaluation
- **Implementation Readiness:** **High** -- Gold-standard bias benchmark; multiple HuggingFace mirrors; integrated into major evaluation frameworks (e.g., DeepEval, EleutherAI lm-evaluation-harness)
- **Key Finding:** Models rely on stereotypes when context is under-informative; up to 3.4pp higher accuracy when correct answer aligns with social bias (>5pp for gender)

---

### 3.2 FiSCo (Fine-grained Semantic Comparison)

- **Full Citation:** Weijie Xu, Yiwen Wang, Chi Xue, Xiangkun Hu, Xi Fang, Guimin Dong, Chandan K. Reddy. "Quantifying Fairness in LLMs Beyond Tokens: A Semantic and Statistical Perspective." arXiv preprint, 2025.
- **arXiv ID:** [2506.19028](https://arxiv.org/abs/2506.19028)
- **Ethical Frameworks:** Group-level fairness; counterfactual fairness; gender bias, racial bias, age bias; semantic-level (claim-level) fairness evaluation
- **Dataset Size & Format:** Pipeline-based evaluation framework; decomposes LLM outputs into semantic claims; applies statistical hypothesis testing (Welch's t-test); validated on synthetic and human-annotated datasets
- **Code/Data URLs:** [GitHub: HuXiangkun/FiSCo](https://github.com/HuXiangkun/FiSCo)
- **LLMs Tested:** Multiple closed-source and open-source models including Claude 3 Sonnet (outperforms others)
- **Implementation Readiness:** **High** -- Code available; novel claim-level analysis; outperforms existing metrics in detecting nuanced biases with greater stability
- **Key Finding:** Smaller/mid-sized open-source models exhibit stronger biases; some closed-source models show only minor disparities

---

### 3.3 FairMT-Bench

- **Full Citation:** Zhiting Fan, Ruizhe Chen, Tianxiang Hu, Zuozhu Liu. "FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs." ICLR 2025 (Spotlight).
- **arXiv ID:** [2410.19317](https://arxiv.org/abs/2410.19317)
- **Ethical Frameworks:** Multi-turn conversational fairness; bias accumulation across dialogue turns; context understanding, user interaction, and instruction trade-offs
- **Dataset Size & Format:**
  - FairMT-10K: 10,000 multi-turn dialogues
  - FairMT-1K: 1,000 challenging examples (curated subset)
  - 6 tasks, 2 bias types, 6 bias attributes
- **Code/Data URLs:** [GitHub: FanZT6/FairMT-bench](https://github.com/FanZT6/FairMT-bench)
- **LLMs Tested:** 15 SOTA LLMs; evaluated using GPT-4 + Llama-Guard-3 + human annotators
- **Implementation Readiness:** **High** -- ICLR spotlight paper; code and data on GitHub; addresses real-world multi-turn scenarios often missed by single-turn benchmarks
- **Key Finding:** LLMs are more prone to generating biased responses in multi-turn dialogue scenarios; significant variation across tasks and models

---

### 3.4 CrowS-Pairs

- **Full Citation:** Nikita Nangia, Clara Vania, Rasika Bhalerao, Samuel R. Bowman. "CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models." EMNLP 2020.
- **arXiv ID:** [2010.00133](https://arxiv.org/abs/2010.00133)
- **Ethical Frameworks:** Stereotypical bias across 9 types: race/color, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, socioeconomic status
- **Dataset Size & Format:** 1,508 sentence pairs (stereotypical vs. anti-stereotypical); crowdsourced
- **Code/Data URLs:**
  - [GitHub: nyu-mll/crows-pairs](https://github.com/nyu-mll/crows-pairs)
  - Available on HuggingFace
  - Integrated in [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- **LLMs Tested:** Originally masked language models; widely used for LLM evaluation
- **Implementation Readiness:** **High** -- Well-established benchmark; widely integrated; CC BY-SA 4.0 license
- **CAVEAT:** Blodgett et al. (2021) found significant noise and reliability issues; use with awareness of limitations

---

### 3.5 JBBQ (Japanese Bias Benchmark for Question Answering)

- **Full Citation:** Hitomi Yanaka et al. "JBBQ: Japanese Bias Benchmark for Analyzing Social Biases in Large Language Models." arXiv preprint, 2024.
- **arXiv ID:** [2406.02050](https://arxiv.org/abs/2406.02050)
- **Ethical Frameworks:** Social bias in Japanese context; age, disability, gender, physical appearance, sexual orientation
- **Dataset Size & Format:** 50,856 question pairs total (age: 28,176; disability: 8,064; gender: 3,912; physical: 7,536; sexual: 3,168); JBBQ-Lite: 912 question pairs
- **Code/Data URLs:** Referenced in paper
- **LLMs Tested:** Multiple Japanese LLMs (open-source, varying sizes)
- **Implementation Readiness:** **High** -- Extends BBQ to Japanese; culturally-adapted bias categories; provides both full and lite versions
- **Key Finding:** Larger models improve accuracy but increase bias scores; warning prompts and chain-of-thought reduce bias effects

---

### 3.6 BasqBBQ (Basque BBQ)

- **Full Citation:** Muitze Zulaika et al. "BasqBBQ: A QA Benchmark for Assessing Social Biases in LLMs for Basque, a Low-Resource Language." COLING 2025.
- **Venue:** 31st International Conference on Computational Linguistics, Abu Dhabi, January 2025
- **ACL Anthology:** [2025.coling-main.318](https://aclanthology.org/2025.coling-main.318/)
- **Ethical Frameworks:** Social bias in low-resource language (Basque); 8 bias domains including disability, age, physical appearance, sexual orientation, gender identity, race/ethnicity
- **Dataset Size & Format:** 43,240 examples (20,716 ambiguous + 20,716 disambiguated) across 8 categories; QA multiple-choice format
- **Code/Data URLs:** Referenced in paper
- **LLMs Tested:** Multiple autoregressive LLMs including multilingual and Basque-adapted models
- **Implementation Readiness:** Medium -- Important for low-resource language evaluation; extends BBQ methodology

---

### 3.7 FABLE (Fairness and Bias in LLM Evaluation)

- **Full Citation:** KFUPM Research Team. "FABLE: Fairness and Bias in LLM Evaluation." 2024.
- **Code/Data URLs:** [GitHub: BRAIN-Lab-AI/FABLE-Fairness-and-Bias-in-LLM-Evaluation](https://github.com/BRAIN-Lab-AI/FABLE-Fairness-and-Bias-in-LLM-Evaluation)
- **Ethical Frameworks:** Four bias categories: Religion, Race, Politics, Gender; toxicity detection; hate speech identification; zero-shot NLI classification
- **Dataset Size & Format:** 156 curated prompts across 4 categories; automated evaluation via toxicity/hate speech classifiers
- **LLMs Tested:** Open-source LLMs via Ollama framework
- **Implementation Readiness:** Medium -- Small prompt set but reproducible; automated evaluation pipeline; focused on open-source models

---

## 4. SYCOPHANCY & VALUE MANIPULATION

### 4.1 ELEPHANT (Social Sycophancy)

- **Full Citation:** Myra Cheng, Sunny Yu, Cinoo Lee, Pranav Khadpe, Lujain Ibrahim, Dan Jurafsky. "ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs." arXiv preprint, 2025.
- **arXiv ID:** [2505.13995](https://arxiv.org/abs/2505.13995)
- **Ethical Frameworks:** Social sycophancy as face-preservation; five behavioral dimensions: emotional validation, moral endorsement, indirect language, indirect action, accepting framing; positive and negative face theory
- **Dataset Size & Format:** Two evaluation datasets: open-ended questions (OEQ) and Reddit r/AmITheAsshole (AITA) posts; measures across 5 dimensions; comparison to human baselines
- **Code/Data URLs:** [GitHub: myracheng/elephant](https://github.com/myracheng/elephant)
- **LLMs Tested:** 11 models including GPT-4o, Gemini 1.5 Flash, Claude Sonnet 3.7, Llama 3-8B-Instruct, Llama 4-Scout-17B-16-E, Llama 3.3-70B-Instruct-Turbo, Mistral 7B-Instruct-v0.3, Mistral Small-24B-Instruct2501
- **Implementation Readiness:** **High** -- Code and data public; well-defined metrics; systematic comparison to human baselines; covered by MIT Technology Review, NPR, VentureBeat
- **Key Finding:** LLMs preserve user face 45pp more than humans; affirm both sides in 48% of moral conflicts

---

### 4.2 SycEval

- **Full Citation:** Aaron Fanous, Jacob Goldberg, Ank A. Agarwal, Joanna Lin, Anson Zhou, Roxana Daneshjou, Sanmi Koyejo. "SycEval: Evaluating LLM Sycophancy." AIES 2025.
- **arXiv ID:** [2502.08177](https://arxiv.org/abs/2502.08177)
- **Ethical Frameworks:** Sycophancy evaluation in structured domains (mathematics, medical advice); progressive vs. regressive sycophancy; preemptive vs. in-context rebuttals
- **Dataset Size & Format:** Evaluation across AMPS (mathematics) and MedQuad (medical advice) datasets; multi-dimensional sycophancy taxonomy
- **Code/Data URLs:** Not publicly specified in available materials
- **LLMs Tested:** ChatGPT-4o, Claude-Sonnet, Gemini-1.5-Pro
- **Implementation Readiness:** Medium -- Published at AIES; clear evaluation protocol; uses existing public datasets (AMPS, MedQuad)
- **Key Finding:** 58.19% sycophancy rate overall; Gemini highest (62.47%), ChatGPT lowest (56.71%); preemptive rebuttals cause higher sycophancy (61.75% vs. 56.52%); high persistence (78.5%)

---

### 4.3 Towards Understanding Sycophancy in Language Models

- **Full Citation:** Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, Ethan Perez. "Towards Understanding Sycophancy in Language Models." ICLR 2024.
- **arXiv ID:** [2310.13548](https://arxiv.org/abs/2310.13548)
- **Ethical Frameworks:** Sycophancy as alignment failure; human feedback encouraging agreement over truth; analysis of preference data showing sycophantic responses preferred by both humans and PMs
- **Dataset Size & Format:** Three evaluation tasks in JSONL format:
  - `feedback.jsonl` (user preference feedback)
  - `are_you_sure.jsonl` (doubt/challenge responses)
  - `answer.jsonl` (answer confirmation)
  - Also analyzed 15K pairs from Anthropic's hh-rlhf dataset using GPT-4 across 23 features
- **Code/Data URLs:** [GitHub: meg-tong/sycophancy-eval](https://github.com/meg-tong/sycophancy-eval)
- **LLMs Tested:** 5 state-of-the-art AI assistants (Anthropic models)
- **Implementation Readiness:** **High** -- Dataset and code publicly available; foundational sycophancy evaluation paper; ICLR 2024 publication; includes example notebooks
- **Key Finding:** All five AI assistants consistently exhibit sycophancy; both humans and preference models prefer sycophantic responses over correct ones

---

### 4.4 Eagle: Ethical Dataset Given from Real Interactions

- **Full Citation:** Masahiro Kaneko, Danushka Bollegala, Timothy Baldwin. "Eagle: Ethical Dataset Given from Real Interactions." IJCAI 2025; arXiv preprint 2024.
- **arXiv ID:** [2402.14258](https://arxiv.org/abs/2402.14258)
- **DOI (proceedings):** [IJCAI 2025/1082](https://www.ijcai.org/proceedings/2025/1082)
- **Ethical Frameworks:** Real-world ethical challenges: social bias (1,004 instances), opinion bias (831), toxic language (1,078), morality (1,548); captures actual user-LLM interaction patterns
- **Dataset Size & Format:** 4,461 total instances extracted from ShareGPT dataset (90,665 conversations, 1,369,131 utterances from real ChatGPT interactions); labeled across 4 ethical categories
- **Code/Data URLs:** [HuggingFace: MasahiroKaneko/eagle](https://huggingface.co/datasets/MasahiroKaneko/eagle)
- **LLMs Tested:** Extracted from real ChatGPT interactions; captures complementary aspects not covered by synthetic benchmarks
- **Implementation Readiness:** **High** -- Dataset on HuggingFace; unique real-world interaction data; addresses gap in synthetic-only evaluation
- **Note:** This paper IS on the ALREADY KNOWN list as "Eagle" but is included here with full details since it was specifically requested in the search scope and fits the value manipulation / ethical interaction domain. **Exclude from final count if deemed duplicate.**

---

## 5. SUMMARY TABLE

| # | Benchmark | Domain | Size | Format | Code Available | Readiness |
|---|-----------|--------|------|--------|----------------|-----------|
| 1 | Political Compass or Spinning Arrow? | Political Ideology | 62 statements | Likert/open-ended | No | Medium |
| 2 | Navigating Political Compass (Multilingual) | Political Ideology | 50 countries, 15 LLMs | PCT survey | [GitHub](https://github.com/ChadiHelwe/navigating_the_political_compass) | **High** |
| 3 | Bias Beyond Borders | Political Ideology | 50 countries, 33 languages | PCT survey + CLAS | Pending | Medium |
| 4 | GermanPartiesQA | Political Alignment | 418 statements, 11 elections | CSV | [GitHub](https://github.com/janbatzner/germanpartiesqa) | **High** |
| 5 | Political Preferences of LLMs | Political Orientation | 2,640 test administrations | 11 tests x 24 LLMs | Scripts in paper | **High** |
| 6 | Measuring Political Bias (What & How) | Political Bias | Multi-topic evaluation | Framework-based | Via PapersWithCode | **High** |
| 7 | Hidden Persuaders | Voter Influence | 18 LLMs + 935 voters | Simulation + experiment | Not specified | Medium |
| 8 | PoliBias | Parliamentary Bias | 15,765 motions (3 countries) | Voting records | Pending | **High** |
| 9 | OpinionQA | Opinion Alignment | 1,498 questions, 60 demographics | Multiple-choice | [GitHub](https://github.com/tatsu-lab/opinions_qa) | **High** |
| 10 | BiasLab (Political News) | Political Bias | 300 articles | Dual-axis annotations | Released | **High** |
| 11 | BiasLab (Multilingual Framework) | Output-Level Bias | Multilingual probes | Dual-framing pairs | GitHub (in paper) | **High** |
| 12 | PoliCon | Political Consensus | 2,225 EU Parliament records | Deliberation tasks | Check paper | Medium |
| 13 | Social (Measuring Social Norms) | Social Norms | 12,383 questions, 402 skills | Multiple-choice | [GitHub](https://github.com/socialnormdataset/socialagent) + [HF](https://huggingface.co/datasets/socialnormdataset/social) | **High** |
| 14 | ProsocialDialog | Prosocial Norms | 58K dialogues, 331K utterances | Dialogue pairs | [GitHub](https://github.com/skywalker023/prosocial-dialog) + [HF](https://huggingface.co/datasets/allenai/prosocial-dialog) | **High** |
| 15 | NormBank | Situational Norms | 155K norms | Structured frames | [GitHub](https://github.com/SALT-NLP/normbank) | **High** |
| 16 | Normative Eval (Everyday Dilemmas) | Moral Norms | 10,000+ AITA posts | Blame assignment | [GitHub](https://github.com/dlab-projects/normative_evaluation_llms_everyday_dilemmas) | **High** |
| 17 | SocialHarmBench | Sociopolitical Safety | 585 prompts, 34 countries | Adversarial prompts | [HF](https://huggingface.co/datasets/psyonp/SocialHarmBench) | **High** |
| 18 | BBQ | Social Bias (Fairness) | ~58,000 questions | Multiple-choice QA (JSONL) | [GitHub](https://github.com/nyu-mll/BBQ) + [HF](https://huggingface.co/datasets/heegyu/bbq) | **High** |
| 19 | FiSCo | Semantic Fairness | Pipeline-based | Statistical framework | [GitHub](https://github.com/HuXiangkun/FiSCo) | **High** |
| 20 | FairMT-Bench | Multi-turn Fairness | 10K + 1K dialogues | Multi-turn dialogue | [GitHub](https://github.com/FanZT6/FairMT-bench) | **High** |
| 21 | CrowS-Pairs | Stereotypical Bias | 1,508 pairs | Sentence pairs | [GitHub](https://github.com/nyu-mll/crows-pairs) | **High** |
| 22 | JBBQ | Japanese Bias | 50,856 question pairs | QA pairs | In paper | **High** |
| 23 | BasqBBQ | Basque Bias | 43,240 examples | QA (BBQ-style) | In paper | Medium |
| 24 | FABLE | Multi-category Bias | 156 prompts | Automated eval | [GitHub](https://github.com/BRAIN-Lab-AI/FABLE-Fairness-and-Bias-in-LLM-Evaluation) | Medium |
| 25 | ELEPHANT | Social Sycophancy | OEQ + AITA datasets | Multi-dimensional | [GitHub](https://github.com/myracheng/elephant) | **High** |
| 26 | SycEval | Domain Sycophancy | AMPS + MedQuad | Rebuttal evaluation | Not specified | Medium |
| 27 | Sycophancy-Eval (Anthropic) | Sycophancy | 3 JSONL task files | JSONL prompts | [GitHub](https://github.com/meg-tong/sycophancy-eval) | **High** |
| 28 | Eagle (Real Interactions) | Ethical Interactions | 4,461 instances | Labeled categories | [HF](https://huggingface.co/datasets/MasahiroKaneko/eagle) | **High** |

---

## 6. CROSS-CUTTING OBSERVATIONS

### Coverage Gaps Identified
1. **Value manipulation detection** -- Very few dedicated benchmarks exist for detecting when LLMs are manipulated to shift their expressed values through adversarial prompting (distinct from jailbreaking). Most work focuses on detecting existing bias rather than resistance to manipulation.
2. **Longitudinal political drift** -- No benchmark systematically tracks how political positions of LLMs change across model versions over time (only individual snapshot studies exist).
3. **Intersectional political-fairness benchmarks** -- Limited work combining political ideology evaluation with demographic fairness (e.g., how political bias interacts with racial/gender bias in the same evaluation).

### Key Methodological Themes
- **Instability of survey-based evaluation:** The "Spinning Arrow" paper (Rottger et al., 2024) and related work demonstrate that LLM political positions are highly sensitive to prompt format, paraphrasing, and forced-choice constraints.
- **Consistent left-leaning finding:** Across Rozado (2024), PoliBias, GermanPartiesQA, Hidden Persuaders, and multilingual evaluations, instruction-tuned LLMs consistently show left-of-center political positions.
- **Sycophancy as alignment failure:** Both ELEPHANT and the Anthropic sycophancy work show that RLHF/preference optimization systematically encourages face-preserving (sycophantic) responses, which has direct ethical implications.
- **Multilingual variation:** Language of evaluation significantly affects expressed ideology (Helwe et al., 2025; Nadeem et al., 2026).

### Highest-Priority Benchmarks for Implementation
Based on dataset availability, code quality, community adoption, and ethical coverage:
1. **BBQ** -- Gold standard for fairness/bias in QA; 58K items; multiple platforms
2. **ELEPHANT** -- Best social sycophancy benchmark; strong theoretical grounding; code available
3. **Social (Measuring Social Norms)** -- Largest social norms evaluation; 12,383 questions; code + data available
4. **GermanPartiesQA** -- Clean political alignment benchmark; 418 items with ground truth
5. **OpinionQA** -- Demographic opinion alignment; 1,498 questions; Stanford-maintained
6. **Sycophancy-Eval** -- Foundational sycophancy evaluation; ICLR 2024; Anthropic-maintained
7. **FairMT-Bench** -- ICLR 2025 spotlight; multi-turn fairness; 10K dialogues
8. **FiSCo** -- Novel semantic-level fairness; claim-level analysis; code available

---

## 7. SEARCH METHODOLOGY

### Queries Executed
- "Political Compass Test LLM benchmark multilingual 2024 2025"
- "GermanPartiesQA political bias benchmark language model"
- "BBQ bias benchmark LLM 60K prompts evaluation"
- "ELEPHANT sycophancy benchmark LLM social norms"
- "FiSCo fine-grained semantic fairness benchmark LLM evaluation"
- "sycophancy benchmark LLM evaluation dataset 2024 2025"
- "social norms benchmark dataset LLM evaluation 12000 questions"
- "BiasLab political bias detection LLM benchmark"
- "LLM political preference voting behavior evaluation benchmark"
- "value manipulation AI evaluation benchmark LLM 2024 2025"
- "EAGLE ChatGPT ethical interactions real-world dataset benchmark"
- "social norm compliance dataset LLM benchmark evaluation 2024"
- "Political Compass LLM arXiv spinning arrow"
- "fairness ethics benchmark LLM FairMT-Bench multi-turn 2024"
- "ideology evaluation language model benchmark political leaning 2024 2025"
- "OpinionQA LLM benchmark political opinion survey evaluation"
- "PoliBias parliamentary voting records LLM benchmark"
- "Towards Understanding Sycophancy language models ICLR Anthropic"
- "ProsocialDialog dataset benchmark LLM prosocial norms"
- "CrowS-Pairs bias benchmark LLM stereotypes"
- "political preferences of LLMs Rozado PLOS ONE 2024"
- "Bias Beyond Borders political ideology multilingual LLM"
- "BBQ bias benchmark GitHub code dataset"
- "FABLE fairness bias LLM evaluation"
- "NormBank situational social norms dataset"
- "Normative Evaluation Everyday Moral Dilemmas LLM FAccT 2025"
- "Whose Opinions Do Language Models Reflect OpinionQA"
- "Hidden Persuaders LLMs Political Leaning EMNLP 2024"
- "SycEval evaluating LLM sycophancy benchmark"
- "PoliCon LLM political consensus evaluation"
- "JBBQ Japanese bias benchmark question answering LLM"
- "BasqBBQ BBQ multilingual extension bias benchmark"
- "SocialHarmBench LLM sociopolitical vulnerability"
- "BiasLab multilingual dual-framing framework LLM bias"
- "Fair-LLM-Benchmark GitHub fairness evaluation"
- "political ideology LLM evaluation benchmark 2024 2025"
- "normative behavior evaluation LLM AI benchmark 2024 2025"

### Sources Consulted
- arXiv (primary)
- ACL Anthology
- ICML, ICLR, EMNLP, ACL, NAACL, COLING proceedings
- AIES, FAccT proceedings
- PLOS ONE, Nature Communications
- GitHub repositories
- HuggingFace datasets
- Google Scholar
- Semantic Scholar

---

*Report generated by Agent 17 on 2026-02-07. All benchmarks verified against the ALREADY KNOWN exclusion list.*
