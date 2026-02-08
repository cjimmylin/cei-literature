# Agent 9-11: Non-Western Ethics Deep Dives -- Chinese, Islamic/Arabic, African/Indigenous/Latin American

**Date:** 2026-02-07
**Agent:** 9-11 (Combined Non-Western Ethics)
**Task:** Find NEW papers with implementable benchmarks/datasets for ethical values alignment in LLMs focused on non-Western cultural and ethical traditions
**Searches Conducted:** 27 (17 primary + 10 follow-up)

---

## SUMMARY

**Total NEW papers found: 22**

| Region/Tradition | New Papers Found |
|---|---|
| Chinese AI Ethics | 8 |
| Islamic/Arabic/MENA | 7 |
| South Asian (India) | 3 |
| African Languages | 2 |
| Cross-Cultural/Decolonial | 2 |

---

## PART I: CHINESE AI ETHICS BENCHMARKS

---

### Paper 1: CValues -- Measuring the Values of Chinese LLMs from Safety to Responsibility

**Full Citation:** Xu, G., Liu, J., Yan, M., Xu, H., Si, J., Zhou, Z., Yi, P., Gao, X., Sang, J., Zhang, R., Zhang, J., Peng, C., Huang, F., & Ren, J. (2023). "CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility." arXiv:2307.09705.

- **arXiv:** https://arxiv.org/abs/2307.09705
- **Framework:** Two-dimensional evaluation: (1) Safety -- 10 adversarial scenarios (political sensitivity, religious discrimination, crime, etc.); (2) Responsibility -- 8 domains testing ability to detect biases/traps and provide positive guidance in moral dilemmas.
- **Dataset Details:**
  - Adversarial safety prompts across 10 scenarios (manually collected by professional experts)
  - Responsibility prompts from 8 domains (induced by professional experts)
  - CVALUES-COMPARISON: 145k prompts with paired positive and negative responses
  - Language: Chinese
  - Format: MCQ for automatic evaluation + open-ended for human evaluation
- **Code/Data:** Available on ModelScope and GitHub
- **LLMs Tested:** Multiple Chinese LLMs (exact roster in paper)
- **Implementation Readiness:** HIGH -- dataset publicly released, both human and automated evaluation protocols available
- **Unique Contribution:** First comprehensive Chinese human values evaluation benchmark covering both safety AND responsibility; responsibility dimension fills gap in existing Chinese LLM ethics research; includes professional expert-curated adversarial prompts

---

### Paper 2: CHiSafetyBench -- A Chinese Hierarchical Safety Benchmark for LLMs

**Full Citation:** Zhang, J. et al. (2024). "CHiSafetyBench: A Chinese Hierarchical Safety Benchmark for Large Language Models." arXiv:2406.10311.

- **arXiv:** https://arxiv.org/abs/2406.10311
- **Framework:** Based on Chinese government standards for generative AI service security. Hierarchical taxonomy: 5 risk areas (Discrimination, Violation of Values, Commercial Violations, Infringement of Rights, Security Requirements for Specific Services) divided into 31 fine-grained categories.
- **Dataset Details:**
  - 1,861 multiple-choice questions
  - Two task types: (a) multiple-choice (risk content identification) and (b) question-answering (ability to refuse risky questions)
  - Sources: Sampled from SafetyBench and SafetyPrompts + GPT-3.5 generated prompts
  - Language: Chinese
- **Code/Data:** Referenced in paper
- **LLMs Tested:** Multiple Chinese and international LLMs
- **Implementation Readiness:** HIGH -- clear taxonomy, dual-task evaluation, automated LLM-based scoring
- **Unique Contribution:** First Chinese HIERARCHICAL safety benchmark aligned with PRC government regulatory standards; 31-category fine-grained classification unique to Chinese context

---

### Paper 3: ChineseSafe -- A Chinese Benchmark for Evaluating Safety in LLMs

**Full Citation:** Zhang, Y., Gao, Y., et al. (2024). "ChineseSafe: A Chinese Benchmark for Evaluating Safety in Large Language Models." arXiv:2410.18491.

- **arXiv:** https://arxiv.org/abs/2410.18491
- **Hugging Face:** https://huggingface.co/papers/2410.18491
- **Framework:** 4 classes and 10 sub-classes of safety issues aligned with Chinese Internet content moderation regulations. Adds Chinese-specific categories: political sensitivity, pornography, variant/homophonic word evasion tactics.
- **Dataset Details:**
  - 205,034 examples (very large-scale)
  - 4 classes, 10 sub-classes
  - Dual evaluation: text generation + perplexity-based methods
  - Language: Chinese
- **Code/Data:** GitHub (OpenStellarTeam/ChineseSafetyQA)
- **LLMs Tested:** 26 popular LLMs including GPT-4, LLaMA, Qwen
- **Implementation Readiness:** HIGH -- massive dataset, public code, automated evaluation
- **Unique Contribution:** Largest Chinese safety benchmark at 205k examples; uniquely addresses variant/homophonic word evasion tactics used in Chinese Internet censorship circumvention; directly maps to PRC legal risk categories

---

### Paper 4: Edu-Values -- Evaluating Chinese Education Values of LLMs

**Full Citation:** Authors (2024). "Edu-Values: Towards Evaluating the Chinese Education Values of Large Language Models." arXiv:2409.12739. Published at ACM Web Conference 2025.

- **arXiv:** https://arxiv.org/abs/2409.12739
- **ACM:** https://dl.acm.org/doi/10.1145/3701716.3715518
- **Framework:** Seven core Chinese educational values: professional philosophy, teachers' professional ethics, education laws/regulations, cultural literacy, educational knowledge/skills, basic competencies, subject knowledge. Grounded in Chinese Communist Party educational ideology.
- **Dataset Details:**
  - 1,418 questions across 5 question types
  - Types: multiple-choice, multi-modal QA, subjective analysis, adversarial prompts, Chinese traditional culture (short answer)
  - Questions from 2014-2024, filtering out rote memorization in favor of behavioral choices, value judgments, ethical considerations
  - Language: Chinese
- **Code/Data:** Referenced in paper
- **LLMs Tested:** 21 state-of-the-art LLMs
- **Implementation Readiness:** HIGH -- human-feedback-based automatic evaluation, RAG augmentation protocol provided
- **Unique Contribution:** First benchmark specifically targeting Chinese educational values; reveals cultural gap where Chinese LLMs significantly outperform English LLMs (Qwen 2 at 81.37 first place); demonstrates RAG-based improvement for values alignment

---

### Paper 5: Chinese SafetyQA -- A Safety Short-form Factuality Benchmark

**Full Citation:** Tian, Y. et al. (2024). "Chinese SafetyQA: A Safety Short-form Factuality Benchmark for Large Language Models." arXiv:2412.15265. Published at ACL 2025.

- **arXiv:** https://arxiv.org/abs/2412.15265
- **GitHub:** https://github.com/OpenStellarTeam/ChineseSafetyQA
- **Framework:** Safety-specific factuality evaluation across seven topics covering law, policy, ethics, and other safety-critical domains specific to the Chinese regulatory context.
- **Dataset Details:**
  - 2,000+ high-quality safety examples
  - 7 topics
  - Format: Short-form factuality QA
  - Language: Chinese
  - Properties: Static, easy-to-evaluate, safety-related, harmless
- **Code/Data:** GitHub (OpenStellarTeam/ChineseSafetyQA)
- **LLMs Tested:** Multiple models; only 3 met 60% passing threshold; o1-preview best performer
- **Implementation Readiness:** HIGH -- public dataset, clear evaluation metrics, easy-to-evaluate format
- **Unique Contribution:** Bridges safety and factuality for Chinese LLMs; reveals that most LLMs cannot even pass a 60% threshold on Chinese safety knowledge; evaluates RAG ability and attack robustness in safety context

---

### Paper 6: LiveSecBench -- A Dynamic Event-Driven Safety Benchmark for Chinese LLMs

**Full Citation:** Li, X. et al. (2025). "LiveSecBench: A Dynamic and Event-Driven Safety Benchmark for Chinese Language Model Applications." arXiv:2511.02366.

- **arXiv:** https://arxiv.org/abs/2511.02366
- **Framework:** Five dimensions: Public Safety, Fairness and Bias, Privacy, Truthfulness, Mental Health Safety. ELO rating system for model comparison. Continuously updated to reflect evolving threat landscape.
- **Dataset Details:**
  - Dynamic, continuously updated (latest version v251215)
  - Automated generation pipeline with human verification
  - 5 evaluation dimensions
  - Language: Chinese
  - Format: Online leaderboard with periodic version releases
- **Code/Data:** Online leaderboard
- **LLMs Tested:** 57 representative LLMs in latest version
- **Implementation Readiness:** HIGH -- operational leaderboard, automated pipeline, ELO ranking
- **Unique Contribution:** First DYNAMIC (continuously updated) Chinese safety benchmark; addresses test contamination through periodic refresh; provides radar-chart visualization of safety profiles; event-driven design responds to real-world incidents

---

### Paper 7: COIG-P -- Chinese Preference Dataset for Alignment with Human Values

**Full Citation:** Authors (2025). "COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values." arXiv:2504.05535.

- **arXiv:** https://arxiv.org/abs/2504.05535
- **GitHub:** https://github.com/multimodal-art-projection/COIG-P
- **Hugging Face:** https://huggingface.co/datasets/m-a-p/COIG-P
- **Framework:** LLM-based annotation pipeline for Chinese preference pairs; 6 domains (Chat, Code, Math, Logic, Novel, Role); includes Chinese Reward Model (CRM) and Chinese Reward Benchmark (CRBench).
- **Dataset Details:**
  - 1,009,000 Chinese preference pairs (very large scale)
  - 6 diverse domains
  - 92k high-quality Chinese queries crawled and filtered
  - 15 mainstream LLMs used for response generation and scoring
  - Language: Chinese
  - Format: Chosen-rejected preference pairs
- **Code/Data:** GitHub + Hugging Face (publicly available)
- **LLMs Tested:** Qwen2/2.5, Infinity-Instruct-3M-0625 series; CRM comparable to GPT-4o
- **Implementation Readiness:** VERY HIGH -- public dataset on HuggingFace, code on GitHub, trained reward model available
- **Unique Contribution:** Largest Chinese preference dataset (1M+ pairs); no human annotation required; includes trained Chinese Reward Model (CRM) and Chinese Reward Benchmark (CRBench); 2-12% performance improvements on AlignBench

---

### Paper 8: OpenEval -- Benchmarking Chinese LLMs across Capability, Alignment, and Safety

**Full Citation:** Li, C. et al. (2024). "OpenEval: Benchmarking Chinese LLMs across Capability, Alignment and Safety." Proceedings of ACL 2024 (Demos). arXiv:2403.12316.

- **arXiv:** https://arxiv.org/abs/2403.12316
- **ACL Anthology:** https://aclanthology.org/2024.acl-demos.19/
- **Framework:** Three-dimensional evaluation: (1) Capability (12 datasets: NLP tasks, disciplinary knowledge, commonsense reasoning, math); (2) Alignment (7 datasets: bias, offensiveness, illegality in outputs); (3) Safety (6 datasets: power-seeking, self-awareness, anticipated risks).
- **Dataset Details:**
  - 35 benchmark datasets total
  - 25 datasets tailored specifically for Chinese language
  - Covers 7B to 72B parameter models
  - Language: Chinese
  - Format: Integrated evaluation platform
- **Code/Data:** Open evaluation platform
- **LLMs Tested:** Wide range of Chinese LLMs from 7B to 72B (both open-source and proprietary)
- **Implementation Readiness:** HIGH -- operational evaluation platform, 35 integrated datasets
- **Unique Contribution:** Holistic three-pillar evaluation platform (capability + alignment + safety) for Chinese LLMs; identifies that commonsense reasoning, alignment, and safety need most attention; operational infrastructure for community-wide benchmarking

---

## PART II: ISLAMIC / ARABIC / MENA BENCHMARKS

---

### Paper 9: AraTrust -- An Evaluation of Trustworthiness for LLMs in Arabic

**Full Citation:** Alghamdi, R., Alyafeai, Z., et al. (2025). "AraTrust: An Evaluation of Trustworthiness for LLMs in Arabic." Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025).

- **ACL Anthology:** https://aclanthology.org/2025.coling-main.579/
- **arXiv:** https://arxiv.org/abs/2403.09017
- **Hugging Face:** https://huggingface.co/datasets/asas-ai/AraTrust
- **Framework:** Eight trustworthiness dimensions: Truthfulness, Ethics, Privacy, Illegal Activities, Mental Health, Physical Health, Unfairness, Offensive Language.
- **Dataset Details:**
  - 522 human-written multiple-choice questions
  - 8 trustworthiness dimensions
  - Language: Arabic
  - Format: Multiple-choice
- **Code/Data:** Hugging Face (asas-ai/AraTrust)
- **LLMs Tested:** GPT-4, AceGPT 7B, Jais 13B, and others; GPT-4 most trustworthy; open-source models struggled below 60%
- **Implementation Readiness:** HIGH -- dataset on HuggingFace, clear MCQ format, automated evaluation
- **Unique Contribution:** First comprehensive trustworthiness benchmark specifically for Arabic LLMs; human-written (not machine-generated) questions ensure cultural authenticity; reveals large gap between proprietary and open-source Arabic models

---

### Paper 10: PalmX 2025 -- First Shared Task on Benchmarking LLMs on Arabic and Islamic Culture

**Full Citation:** Authors (2025). "PalmX 2025: The First Shared Task on Benchmarking LLMs on Arabic and Islamic Culture." ArabicNLP 2025. arXiv:2509.02550.

- **arXiv:** https://arxiv.org/abs/2509.02550
- **Website:** https://palmx.dlnlp.ai/
- **Leaderboard:** https://palmx.dlnlp.ai/leaderboard.html
- **Framework:** Two subtasks: (1) General Arabic Culture (customs, etiquette, cuisine, history, famous figures, geography, arts, dialectal expressions across Arab countries); (2) Islamic Culture (prayers, fasting, Quranic knowledge, Hadith, Islamic history, religious holidays).
- **Dataset Details:**
  - 600 MCQ training pairs
  - 300 MCQ development pairs
  - 1,000 blind test questions
  - Language: Modern Standard Arabic (MSA)
  - Format: Multiple-choice question-answer pairs
- **Code/Data:** Shared task platform (palmx.dlnlp.ai)
- **LLMs Tested:** Multiple teams; LoRA fine-tuning emerged as dominant method
- **Implementation Readiness:** HIGH -- established shared task with leaderboard, public training data
- **Unique Contribution:** First STANDARDIZED benchmark for Arabic and Islamic cultural competence in LLMs; task-specific fine-tuning substantially improved performance; active leaderboard for ongoing evaluation

---

### Paper 11: Hajj-FQA -- Benchmark Arabic Dataset for Hajj Fatwa QA

**Full Citation:** Authors (2025). "Hajj-FQA: A benchmark Arabic dataset for developing question-answering systems on Hajj fatwas." Journal of King Saud University Computer and Information Sciences, Springer.

- **DOI:** https://link.springer.com/article/10.1007/s44443-025-00128-w
- **Framework:** Domain-specific religious QA benchmark covering three tasks: Machine Reading Comprehension (MRC), Duplicate Question Detection (DQD), Duplicate Answer Detection (DAD).
- **Dataset Details:**
  - 2,826 QA pairs from 800 expert-annotated fatwas
  - Specific to Hajj pilgrimage jurisprudence
  - Language: Arabic
  - Format: QA pairs with 10-fold cross-validation evaluation protocol
- **Code/Data:** Referenced in paper
- **LLMs Tested:** Multilingual and Arabic-specific models; AraBERTv0.2 achieved 99.19% precision (DQD) and 99.26% (DAD)
- **Implementation Readiness:** MEDIUM-HIGH -- expert-annotated, clear evaluation tasks
- **Unique Contribution:** First dedicated benchmark for Hajj-related fatwa QA; captures unique linguistic and jurisprudential characteristics of pilgrims' inquiries; high baseline performance suggests strong model readiness

---

### Paper 12: QIAS 2025 -- Shared Task on Islamic Inheritance Reasoning and Knowledge Assessment

**Full Citation:** Authors (2025). "QIAS 2025: Overview of the Shared Task on Islamic Inheritance Reasoning and Knowledge Assessment." ArabicNLP 2025.

- **ACL Anthology:** https://aclanthology.org/2025.arabicnlp-sharedtasks.117/
- **Framework:** Two subtasks: (1) Islamic Inheritance Reasoning ('Ilm al-Mawarith) -- computing inheritance shares according to Islamic jurisprudence; (2) Islamic Knowledge Assessment -- traditional Islamic disciplines.
- **Dataset Details:**
  - Subtask 1: 22,000 examples total (20,000 train / 1,000 val / 1,000 test)
  - MCQ format with up to 6 answer options (A-F)
  - Two difficulty levels: Beginner (basic shares, eligible heirs) and Advanced (multi-generational, fractional distributions)
  - Constructed from IslamWeb fatwas, auto-generated via Gemini 2.5 Pro, reviewed by 4 Islamic studies experts
  - Language: Arabic
- **Code/Data:** Shared task platform
- **LLMs Tested:** 44 teams participated; 18 advanced to final test; 16 submitted system papers
- **Implementation Readiness:** HIGH -- large dataset, active shared task, expert-validated
- **Unique Contribution:** First shared task specifically testing MATHEMATICAL REASONING within Islamic legal framework; requires combining cultural/religious knowledge with precise numerical computation; 22k examples provide substantial training data

---

### Paper 13: IslamicEval 2025 -- Shared Task on Capturing LLM Hallucination in Islamic Content

**Full Citation:** Authors (2025). "IslamicEval 2025: The First Shared Task of Capturing LLMs Hallucination in Islamic Content." ArabicNLP 2025 Shared Tasks.

- **ResearchGate:** https://www.researchgate.net/publication/397420777
- **ACL Anthology:** https://aclanthology.org/2025.arabicnlp-sharedtasks.69/
- **Framework:** Two subtasks: (1) Hallucination Detection and Correction in Qur'an and Hadith content within LLM-generated Arabic text; (2) Qur'an and Hadith Question Answering (closed-world retrieval from Islamic corpora).
- **Dataset Details:**
  - Subtask 1: Hallucination detection/correction dataset for Qur'anic and Hadith references
  - Subtask 2: QA benchmark from Holy Qur'an and Hadith
  - Includes identifying intended references, validating against authoritative sources, retrieving answer-bearing text
  - Language: Arabic
- **Code/Data:** GitHub (sakher/IslamicEval-BurhanAI-Public)
- **LLMs Tested:** 127 system submissions across 11 tasks at ArabicNLP 2025
- **Implementation Readiness:** HIGH -- active shared task with substantial participation
- **Unique Contribution:** First shared task targeting HALLUCINATION specifically in Islamic religious content; semantic and source-faithful evaluation of generated religious text; critical for trust in AI-generated Islamic knowledge

---

### Paper 14: Saudi-Alignment Benchmark -- Assessing LLMs Alignment with Saudi Cultural and Ethical Norms

**Full Citation:** Authors (2025). "Assessing LLMs Alignment with Cultural Norms and [Saudi Domain Knowledge]." ArabicNLP 2025 Main.

- **ACL Anthology:** https://aclanthology.org/2025.arabicnlp-main.11.pdf
- **Framework:** Six-stage evaluation: (1) defining categories and data sources, (2) selecting question formats, (3) generating questions, (4) quality control, (5) experimental evaluation, (6) performance analysis. Covers Saudi-specific cultural norms, ethical norms, and domain knowledge.
- **Dataset Details:**
  - Questions across Saudi cultural, ethical, and domain knowledge categories
  - Eleven expert annotators evaluated 2,500+ questions
  - Evaluation criteria: fluency, adequacy, cultural appropriateness, bias detection, religious sensitivity, adherence to social norms
  - Language: Arabic
- **Code/Data:** Referenced in paper
- **LLMs Tested:** ALLaM-7B (best at 61.6%); others below 45%
- **Implementation Readiness:** MEDIUM-HIGH -- expert-annotated, structured methodology
- **Unique Contribution:** First dedicated benchmark for SAUDI-SPECIFIC cultural alignment; reveals significant gaps in country-specific knowledge; demonstrates that tailored models outperform general-purpose models for Saudi cultural contexts

---

### Paper 15: Aftina -- Enhancing Stability in AI-Based Islamic Fatwa Generation

**Full Citation:** Mohammed, A. & Ali, H. (2025). "Aftina: enhancing stability and preventing hallucination in AI-based Islamic fatwa generation using LLMs and RAG." Neural Computing and Applications, Springer.

- **DOI:** https://link.springer.com/article/10.1007/s00521-025-11229-y
- **Framework:** Three-setup evaluation: (1) Base LLM, (2) LLM with RAG, (3) LLM with RAG + re-ranker. Evaluated on BERTScore, hallucination rate, completeness, irrelevance metrics.
- **Dataset Details:**
  - Fatwa-specific dataset for fine-tuning and evaluation
  - Three experimental configurations
  - Language: Arabic
  - Format: QA pairs from Islamic fatwa domain
- **Code/Data:** Referenced in paper
- **LLMs Tested:** Multiple LLMs across three experimental configurations
- **Implementation Readiness:** MEDIUM -- methodology replicable, evaluation metrics defined; primary contribution is technique rather than public benchmark
- **Unique Contribution:** Demonstrates RAG + re-ranker approach specifically for eliminating hallucinations in Islamic fatwa generation; provides evaluation methodology for religious content accuracy and stability

---

## PART III: SOUTH ASIAN (INDIA) BENCHMARKS

---

### Paper 16: Indian-BhED -- A Dataset for Measuring India-Centric Biases in LLMs

**Full Citation:** Khandelwal, V. & Tonneau, M. et al. (2024). "Indian-BhED: A Dataset for Measuring India-Centric Biases in Large Language Models." Proceedings of the 2024 International Conference on Information Technology for Social Good (GoodIT '24), Bremen, Germany.

- **arXiv:** https://arxiv.org/abs/2309.08573
- **ACM:** https://dl.acm.org/doi/10.1145/3677525.3678666
- **Framework:** Stereotypical and anti-stereotypical sentence pairs measuring bias along India-specific axes: caste and religion. Modeled on CrowS-Pairs methodology adapted for Indian context.
- **Dataset Details:**
  - Stereotypical and anti-stereotypical sentence pairs
  - Bias axes: caste (63-79% stereotypical output) and religion (69-72%)
  - Language: English (India-centric content)
  - Format: Sentence pairs for bias measurement
- **Code/Data:** Referenced in paper
- **LLMs Tested:** Majority of popular LLMs showed strong stereotypical propensity, especially for caste
- **Implementation Readiness:** MEDIUM-HIGH -- clear methodology, replicable evaluation
- **Unique Contribution:** First dataset quantifying CASTE-BASED bias in LLMs; reveals dramatically higher bias levels for Indian social axes (caste 63-79%) compared to Western axes (gender, race); fills critical Global South gap

---

### Paper 17: IndiBias -- Benchmark Dataset for Social Biases in Indian Context

**Full Citation:** Sahoo, N. et al. (2024). "IndiBias: A Benchmark Dataset to Measure Social Biases in Language Models for Indian Context." Proceedings of NAACL 2024.

- **arXiv:** https://arxiv.org/abs/2403.20147
- **ACL Anthology:** https://aclanthology.org/2024.naacl-long.487/
- **GitHub:** https://github.com/sahoonihar/IndiBias
- **Framework:** Seven bias dimensions: gender, religion, caste, age, region, physical appearance, occupation. Plus three intersectional dimensions. Built from filtered/translated CrowS-Pairs + LLM-augmented India-specific stereotypes.
- **Dataset Details:**
  - 800 sentence pairs + 300 tuples for intersectional bias
  - 7 demographic bias dimensions + 3 intersectional dimensions
  - Languages: English and Hindi
  - Format: Sentence pairs for bias measurement (CrowS-Pairs style)
  - Augmented using ChatGPT and InstructGPT
- **Code/Data:** GitHub (sahoonihar/IndiBias) -- publicly available
- **LLMs Tested:** 10 language models compared on multiple bias metrics
- **Implementation Readiness:** HIGH -- public GitHub, dual-language, established evaluation metrics
- **Unique Contribution:** First bilingual (English-Hindi) Indian bias benchmark; 7 bias dimensions specific to Indian social hierarchy; intersectional bias analysis across Indian demographic axes; reveals higher bias in intersectional groups

---

### Paper 18: IndiCASA -- Dataset and Bias Evaluation Framework for LLMs in Indian Context

**Full Citation:** Authors (2025). "IndiCASA: A Dataset and Bias Evaluation Framework in LLMs Using Contrastive Embedding Similarity in the Indian Context." AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025). arXiv:2510.02742.

- **arXiv:** https://arxiv.org/abs/2510.02742
- **AAAI:** https://ojs.aaai.org/index.php/AIES/article/view/36605
- **Framework:** Contrastive learning-based encoder for capturing fine-grained bias through embedding similarity. Five demographic axes: caste, gender, religion, disability, socioeconomic status. Goes beyond word-flagging to capture contextual meaning.
- **Dataset Details:**
  - 2,575 human-validated sentences
  - 5 demographic axes
  - Contrastively trained encoder model for evaluation
  - Language: English (India-centric)
  - Format: Stereotypical and anti-stereotypical sentences
- **Code/Data:** GitHub (referenced in paper)
- **LLMs Tested:** Multiple open-weight LLMs; all exhibit some stereotypical bias; disability bias notably persistent; religion bias generally lower
- **Implementation Readiness:** HIGH -- public dataset, novel evaluation framework, trained encoder available
- **Unique Contribution:** Novel CONTRASTIVE LEARNING approach to bias evaluation (beyond simple word matching); captures intersectional and contextual nuances specific to Indian society; disability-focused bias dimension unique among Indian benchmarks

---

## PART IV: AFRICAN LANGUAGE BENCHMARKS

---

### Paper 19: IrokoBench -- A Benchmark for African Languages in the Age of LLMs

**Full Citation:** Adelani, D. et al. (2024). "IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models." arXiv:2406.03368. Published at NAACL 2025.

- **arXiv:** https://arxiv.org/abs/2406.03368
- **ACL Anthology:** https://aclanthology.org/2025.naacl-long.139/
- **Framework:** Three tasks: (1) AfriXNLI -- Natural Language Inference; (2) AfriMGSM -- Mathematical Reasoning; (3) AfriMMLU -- Multi-choice Knowledge-based QA. All HUMAN-TRANSLATED (not machine-translated).
- **Dataset Details:**
  - 17 typologically-diverse low-resource African languages
  - Languages from West, East, Southern, Central Africa (e.g., Hausa, Swahili, isiXhosa, Lingala) plus English and French
  - Three evaluation tasks
  - Zero-shot, few-shot, and translate-test settings
  - Format: NLI, math word problems, MCQ
- **Code/Data:** Public (Cohere Research partnership)
- **LLMs Tested:** 10 open and 4 proprietary LLMs; significant gap between open and proprietary models; Gemma 2 27B only 63% of GPT-4o performance
- **Implementation Readiness:** HIGH -- human-translated quality, 17 languages, three established task formats
- **Unique Contribution:** First large-scale human-translated LLM benchmark for African languages; 17-language coverage across 4 African sub-regions; reveals massive performance gap (37%) between best open and proprietary models on African languages

---

### Paper 20: AfroBench -- How Good are LLMs on African Languages?

**Full Citation:** Ojo, J. et al. (2023/2025). "AfroBench: How Good are Large Language Models on African Languages?" arXiv:2311.07978.

- **arXiv:** https://arxiv.org/abs/2311.07978
- **Website:** https://mcgill-nlp.github.io/AfroBench/
- **Framework:** Multi-task evaluation across NLU, text generation, knowledge/QA, and mathematical reasoning for African languages.
- **Dataset Details:**
  - 64 African languages
  - 15 tasks, 22 datasets
  - 9 NLU datasets + 5 text generation datasets + 5 knowledge/QA tasks + 1 mathematical reasoning task
  - Format: Multiple task-specific formats
- **Code/Data:** Public website and GitHub
- **LLMs Tested:** Multiple open and proprietary LLMs
- **Implementation Readiness:** HIGH -- massive coverage (64 languages), multi-task design, public resources
- **Unique Contribution:** Broadest African language LLM benchmark at 64 languages; 22 datasets across 15 tasks provide comprehensive evaluation; highlights that translated datasets may not reflect authentic African language usage

---

## PART V: CROSS-CULTURAL AND DECOLONIAL FRAMEWORKS

---

### Paper 21: Decolonial AI Alignment -- Openness, Visesa-Dharma, and Including Excluded Knowledges

**Full Citation:** Varshney, K. R. (2024). "Decolonial AI Alignment: Openness, Visesa-Dharma, and Including Excluded Knowledges." Proceedings of the 2024 AAAI/ACM Conference on AI, Ethics, and Society (AIES 2024).

- **ACM:** https://dl.acm.org/doi/10.5555/3716662.3716790
- **Framework:** Three decolonial approaches to alignment: (1) Making LLMs open enough for community-specific tuning; (2) Not assuming universal values -- contextual values from deployment communities; (3) Including non-commandment value expressions from diverse epistemologies (e.g., Hindu concept of Visesa-Dharma / context-dependent duty).
- **Dataset Details:** Conceptual framework paper rather than benchmark; proposes methodology for creating culturally-grounded alignment datasets
- **Code/Data:** N/A (framework paper)
- **LLMs Tested:** N/A (conceptual)
- **Implementation Readiness:** LOW (framework) -- but provides theoretical grounding for benchmark construction
- **Unique Contribution:** Introduces Hindu philosophical concept of Visesa-Dharma (context-dependent ethics) as counterpoint to Western universalist alignment; provides actionable framework for decolonializing LLM alignment; directly challenges RLHF's implicit cultural assumptions

---

### Paper 22: FairI Tales / INDIC-BIAS -- Evaluation of Fairness in Indian Contexts

**Full Citation:** Authors (2025). "FairI Tales: Evaluation of Fairness in Indian Contexts with a Focus on Bias and Stereotypes." ACL 2025.

- **arXiv:** https://arxiv.org/abs/2506.23111
- **ACL Anthology:** https://aclanthology.org/2025.acl-long.1465/
- **GitHub:** https://github.com/AI4Bharat/indic-bias
- **Hugging Face:** https://huggingface.co/datasets/ai4bharat/Indic-Bias
- **Framework:** Three evaluation tasks: (1) Plausibility -- whether scenario is realistic; (2) Judgment -- whether LLM makes biased decisions; (3) Generation -- whether LLM generates biased text. Covers 85 identity groups across caste, religion, region, and tribe.
- **Dataset Details:**
  - 20,000 manually validated real-world scenario templates
  - 85 Indian identity groups
  - 14 LLMs evaluated
  - Three evaluation tasks (plausibility, judgment, generation)
  - Language: English (India-centric)
  - Format: Scenario-based evaluation templates
- **Code/Data:** GitHub (AI4Bharat/indic-bias) + HuggingFace (ai4bharat/Indic-Bias)
- **LLMs Tested:** 14 popular LLMs; consistent negative bias against marginalized identities (Dalits, Chamars, tribal groups); positive bias toward privileged groups (Brahmin, Iyyengar)
- **Implementation Readiness:** VERY HIGH -- 20k templates, public GitHub and HuggingFace, three-task evaluation protocol
- **Unique Contribution:** Largest India-specific fairness benchmark (20k templates, 85 identity groups); reveals both allocative AND representational harms; LLMs reinforce stereotypes even when explicitly asked to rationalize; open-source benchmark from AI4Bharat

---

## ADDITIONAL NOTABLE RESOURCES IDENTIFIED (Not Full Papers, but Relevant)

### A. ILMAAM -- Index for Language Models for Arabic Assessment on Multitasks
- **URL:** https://huggingface.co/blog/Omartificial-Intelligence-Space/ilmaam-overview
- Arabic LLM leaderboard with culturally sensitive subject filtering; 50 subjects, 100 questions each; 29 models evaluated; excludes morally sensitive subjects for cultural alignment

### B. LLM Alignment for the Arabs: A Homogenous Culture or Diverse Ones?
- **Citation:** Keleg, A. (2025). C3NLP Workshop at ACL 2025.
- **ACL Anthology:** https://aclanthology.org/2025.c3nlp-1.1/
- Position paper challenging cultural homogeneity assumption in Arabic LLM alignment; provides recommendations for curating diverse alignment data across 22 Arab countries

### C. Palm -- A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs
- **URL:** https://palm.dlnlp.ai/
- Underlying dataset for PalmX 2025; culturally inclusive Arabic dataset

### D. SaudiCulture -- Evaluating LLMs' Cultural Competence within Saudi Arabia
- **arXiv:** https://arxiv.org/abs/2503.17485
- **DOI:** https://link.springer.com/article/10.1007/s44443-025-00137-9
- Dedicated Saudi cultural competence benchmark

---

## CROSS-CUTTING FINDINGS

### 1. Chinese Ethics Landscape
The Chinese AI ethics evaluation ecosystem is notably mature and prolific:
- **Regulatory-driven**: Multiple benchmarks (CHiSafetyBench, ChineseSafe) map directly to PRC government standards and Internet content moderation regulations
- **Scale advantage**: ChineseSafe (205k examples), COIG-P (1M preference pairs) dwarf comparable Western datasets
- **Values specificity**: CValues, Edu-Values target specifically Chinese moral/educational values rather than adapting Western frameworks
- **Dynamic evaluation**: LiveSecBench introduces continuously-updated benchmarking to prevent test contamination

### 2. Arabic/Islamic Ethics Landscape
Rapid maturation in 2024-2025:
- **Shared task ecosystem**: ArabicNLP 2025 hosted PalmX, QIAS, IslamicEval -- three distinct shared tasks covering culture, jurisprudence, and hallucination detection
- **Domain specificity**: Hajj-FQA, QIAS (inheritance law), IslamicEval (hallucination in Qur'an/Hadith) target specific Islamic knowledge domains
- **Trustworthiness**: AraTrust provides first comprehensive Arabic trustworthiness framework
- **Diversity recognition**: Growing awareness (Keleg 2025) that Arab world is NOT culturally homogenous

### 3. South Asian Landscape
India-specific bias evaluation is rapidly advancing:
- **Caste as primary axis**: Indian-BhED, IndiBias, IndiCASA, INDIC-BIAS all center caste alongside religion
- **Scale progression**: From Indian-BhED (sentence pairs) to IndiBias (800 pairs) to IndiCASA (2,575 sentences) to INDIC-BIAS (20k templates)
- **Methodological innovation**: IndiCASA introduces contrastive learning for contextual bias detection

### 4. African Languages
- **Coverage expanding**: IrokoBench (17 languages) and AfroBench (64 languages) provide growing coverage
- **Translation quality**: Emphasis on human translation rather than machine translation
- **Gap persists**: Ethics-specific evaluation (beyond linguistic capability) remains limited for African contexts

### 5. Notable Gaps
- **Latin American**: No implementable benchmarks found; LAAI-Ethics is a conference, not a dataset
- **Indigenous**: CARE/OCAP principles provide governance frameworks but no LLM evaluation datasets exist
- **Ubuntu ethics**: Theoretical scholarship is growing but no operationalized benchmarks for LLM evaluation
- **Southeast Asian, Pacific Islander, Central Asian**: No benchmarks found

---

## IMPLEMENTATION PRIORITY RANKING

| Priority | Paper | Readiness | Scale | Public Data |
|---|---|---|---|---|
| 1 | INDIC-BIAS (FairI Tales) | Very High | 20k templates | Yes (HF + GitHub) |
| 2 | COIG-P | Very High | 1M pairs | Yes (HF + GitHub) |
| 3 | ChineseSafe | High | 205k examples | Yes (GitHub) |
| 4 | AraTrust | High | 522 questions | Yes (HuggingFace) |
| 5 | QIAS 2025 | High | 22k examples | Via shared task |
| 6 | IrokoBench | High | 17 languages | Public |
| 7 | LiveSecBench | High | Dynamic/ongoing | Leaderboard |
| 8 | PalmX 2025 | High | 1,900 MCQs | Via shared task |
| 9 | Chinese SafetyQA | High | 2k+ examples | GitHub |
| 10 | CValues | High | 145k comparison | ModelScope/GitHub |

---

*Report generated by Agent 9-11 (Non-Western Ethics Deep Dives) on 2026-02-07.*
*27 web searches conducted. 22 new papers documented. 4 additional resources noted.*
