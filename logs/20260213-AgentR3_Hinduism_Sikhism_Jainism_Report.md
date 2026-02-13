# Agent R3 Report: Hinduism, Sikhism, and Jainism -- NLP/AI Benchmarks, Datasets, and Evaluation Papers

**Agent:** R3
**Focus:** Hinduism, Sikhism, Jainism
**Date:** 2026-02-13
**Searches Conducted:** 12 primary + 16 targeted follow-up searches
**Vault Dedup Reference:** 853 entries checked

---

## Papers Found

### 1. Measuring Spiritual Values and Bias of Large Language Models
- **Authors:** Songyuan Liu, Ziyang Zhang, Runze Yan, Wei Wu, Carl Yang, Jiaying Lu
- **Year:** 2024
- **Venue:** arXiv (preprint)
- **arXiv:** 2410.11647
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Buddhism, Christianity, Islam, Judaism (multi-faith including Hindu)
- **Paper Type:** Benchmark | Bias Study
- **Dataset Size:** Tests spiritual values across multiple LLMs using surveys and hate speech identification scenarios
- **Languages:** English
- **LLMs Tested:** Multiple LLMs (specific models tested in experiments)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Tests spiritual values of popular LLMs and finds they are quite diverse (not stereotypically atheist/secularist). Different spiritual values affect LLM behavior in social-fairness scenarios (e.g., hate speech identification). Proposes continued pre-training on spiritual texts to mitigate spiritual bias. Directly relevant to Hindu spiritual values in LLMs.

---

### 2. Divine LLaMAs: Bias, Stereotypes, Stigmatization, and Emotion Representation of Religion in Large Language Models
- **Authors:** Flor Miriam Plaza-del-Arco, Amanda Cercas Curry, Susanna Paoli, Alba Curry, Dirk Hovy
- **Year:** 2024
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2407.06908
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Buddhism, Islam, Judaism, Christianity, Sikhism (19 religious personas)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** 7,586 events from ISEAR dataset prompted across 19 religious personas
- **Languages:** English
- **LLMs Tested:** Llama 2, Llama 3, Mistral-7b, GPT-4
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Finds Eastern religions like Hinduism and Buddhism are "strongly stereotyped" while Judaism and Islam are "stigmatized" (refusal rates skyrocket). Hinduism shows specific emotion bias patterns. Directly evaluates LLM religious bias including Hindu and Sikh personas.

---

### 3. Sometimes the Model doth Preach: Quantifying Religious Bias in Open LLMs through Demographic Analysis in Asian Nations
- **Authors:** Hari Shankar, Vedanta S P, Tejas Cavale, Ponnurangam Kumaraguru, Abhijnan Chakraborty
- **Year:** 2025
- **Venue:** arXiv (preprint)
- **arXiv:** 2503.07510
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Sikhism, Islam, Buddhism, Christianity, Jainism (Indian religious demographics)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Surveys from multiple Asian nations, focus on India
- **Languages:** English
- **LLMs Tested:** Llama, Mistral (multiple variants)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Profiles open LLMs against demographic surveys from India and other Asian nations on religious tolerance and identity. Finds LLMs match a single homogeneous profile, risking promotion of a hegemonic worldview and undermining perspectives of different minorities. Hinduism, Sikhism, and other Indian faiths directly assessed.

---

### 4. How Deep Is Representational Bias in LLMs? The Cases of Caste and Religion
- **Authors:** Agrima Seth, Monojit Choudhary, Sunayana Sitaram, Kentaro Toyama, Aditya Vashistha, Kalika Bali
- **Year:** 2025
- **Venue:** AAAI/ACM AIES 2025
- **arXiv:** 2508.03712
- **DOI:** N/A
- **Religious Traditions:** Hinduism (caste system is inherently Hindu-origin; tests Hindu, Muslim, Christian, Sikh religious representation)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** 7,200+ generated stories about significant life events in India
- **Languages:** English
- **LLMs Tested:** GPT-4 Turbo
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Systematic audit finding GPT-4 consistently overrepresents culturally dominant groups in India far beyond statistical representation. Hinduism showed strongest crime associations in internal representations. "Winner-take-all" quality more biased than training data distribution. Directly tests Hindu and Sikh religious representation.

---

### 5. DECASTE: Unveiling Caste Stereotypes in Large Language Models through Multi-Dimensional Bias Analysis
- **Authors:** Prashanth Vijayaraghavan, Soroush Vosoughi, Lamogha Chiazor, Raya Horesh, Rogerio Abreu de Paula, Ehsan Degan, Vandana Mukherjee
- **Year:** 2025
- **Venue:** IJCAI 2025 (AI and Social Good Track)
- **arXiv:** 2505.14971
- **DOI:** N/A
- **Religious Traditions:** Hinduism (caste system is central to Hindu social structure)
- **Paper Type:** Benchmark | Bias Study
- **Dataset Size:** Custom caste-stereotypical dataset across 4 dimensions (social, economic, educational, political)
- **Languages:** English
- **LLMs Tested:** 9 distinct LLMs (state-of-the-art models)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Novel multi-dimensional framework (SWAT + PSAT tasks) to detect implicit and explicit caste biases in LLMs. Evaluates caste fairness across four dimensions. Reveals LLMs systematically reinforce caste biases with elevated scores comparing Dalits/Shudras with dominant caste groups. Caste is deeply intertwined with Hindu social and religious structures.

---

### 6. Religious Bias Landscape in Language and Text-to-Image Models: Analysis, Detection, and Debiasing Strategies
- **Authors:** Ajwad Abrar, Nafisa Tabassum Oeshy, Mohsinul Kabir, Sophia Ananiadou
- **Year:** 2025
- **Venue:** AI & Society (Springer) / arXiv
- **arXiv:** 2501.08441
- **DOI:** 10.1007/s00146-025-02721-z
- **Religious Traditions:** Hinduism, Islam, Christianity, Judaism, Buddhism, Sikhism (multi-faith)
- **Paper Type:** Benchmark | Bias Study
- **Dataset Size:** ~460 unique prompts for language models + 5,000 generated images for T2I evaluation
- **Languages:** English
- **LLMs Tested:** Open-source and closed-source LLMs and T2I models
- **Code/Data:** https://github.com/ajwad-abrar/Religious-Bias (prompts and images publicly released)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Systematically investigates religious bias across language models and text-to-image generation, including Hinduism and Sikhism. Curated dataset of 460 prompts evaluates bias in mask filling, prompt completion, and image generation. Tests debiasing techniques with corrective prompts.

---

### 7. Mechanistic Interpretability with SAEs: Probing Religion, Violence, and Geography in Large Language Models
- **Authors:** Katharina Simbeck, Mariam Mahran
- **Year:** 2025
- **Venue:** AEQUITAS 2025 Workshop (co-located with ECAI 2025)
- **arXiv:** 2509.17665
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Judaism, Buddhism (5 religions)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Latent feature activations across 5 models via Neuronpedia API
- **Languages:** English
- **LLMs Tested:** 5 LLMs (analyzed via sparse autoencoders)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Uses mechanistic interpretability and Sparse Autoencoders to analyze how religion is internally represented in LLMs. Finds all five religions (including Hinduism) show comparable internal cohesion but Islam is more linked to violence features. Geographic associations reflect real-world religious demographics.

---

### 8. Ancient Wisdom, Modern Tools: Exploring Retrieval-Augmented LLMs for Ancient Indian Philosophy (VedantaNY-10M)
- **Authors:** Priyanka Mandikal
- **Year:** 2024
- **Venue:** ML4AL Workshop, ACL 2024 (Outstanding Paper Award)
- **arXiv:** 2408.11903
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Advaita Vedanta)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 10M+ tokens from 612 lectures on Advaita Vedanta philosophy
- **Languages:** English
- **LLMs Tested:** RAG-augmented LLM vs. standard LLM (benchmarked)
- **Code/Data:** https://github.com/priyankamandikal/vedantany-10m / https://sites.google.com/view/vedantany-10m
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Creates VedantaNY-10M dataset from 612 Advaita Vedanta lectures. Benchmarks RAG vs non-RAG LLMs for long-form QA on Hindu philosophy. RAG significantly outperforms standard model with fewer hallucinations. Outstanding Paper award at ACL 2024 workshop. Directly tests LLM knowledge of Hindu Vedantic philosophy.

---

### 9. Artificial Intelligence for Topic Modelling in Hindu Philosophy: Mapping Themes between the Upanishads and the Bhagavad Gita
- **Authors:** Rohitash Chandra, Mukul Ranjan
- **Year:** 2022
- **Venue:** PLOS ONE
- **arXiv:** 2205.11020
- **DOI:** 10.1371/journal.pone.0273476
- **Religious Traditions:** Hinduism
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Full Upanishads + Bhagavad Gita texts
- **Languages:** English (translations of Sanskrit texts)
- **LLMs Tested:** BERT (topic modelling)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Uses BERT-based topic modelling to map themes between the Upanishads and Bhagavad Gita. Finds 73% mean cosine similarity between topics. Best model gives 73% coherence on Gita and 69% on Upanishads. Foundational for Hindu philosophical text analysis with AI.

---

### 10. Semantic and Sentiment Analysis of Selected Bhagavad Gita Translations Using BERT-Based Language Framework
- **Authors:** Rohitash Chandra, Venkatesh Kulkarni
- **Year:** 2022
- **Venue:** IEEE Access
- **arXiv:** 2201.03115
- **DOI:** 10.1109/ACCESS.2022.3151327
- **Religious Traditions:** Hinduism
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Multiple Bhagavad Gita translations (verse-by-verse, 700 verses)
- **Languages:** English (translations from Sanskrit)
- **LLMs Tested:** BERT
- **Code/Data:** https://github.com/sydney-machine-learning/sentimentanalysis_bhagavadgita
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Creates hand-labelled sentiment dataset for Bhagavad Gita and uses BERT for verse-by-verse sentiment analysis across translations. Notes the absence of a Hindu philosophy BERT model and identifies need for one that captures terms like Brahman, karma, dharma, maya.

---

### 11. Itihasa: A Large-Scale Corpus for Sanskrit to English Translation
- **Authors:** Rahul Aralikatte, Miryam de Lhoneux, Anoop Kunchukuttan, Anders Sogaard
- **Year:** 2021
- **Venue:** WAT 2021 (Workshop on Asian Translation)
- **arXiv:** 2106.03269
- **DOI:** N/A
- **Religious Traditions:** Hinduism
- **Paper Type:** Dataset
- **Dataset Size:** 93,030 parallel Sanskrit-English sentence pairs
- **Languages:** Sanskrit, English
- **LLMs Tested:** Transformer translation models (best: 7-8 BLEU)
- **Code/Data:** https://github.com/rahular/itihasa
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Large-scale parallel corpus of 93K Sanskrit shlokas and English translations from the Ramayana and Mahabharata. Standard translation models perform poorly (7-8 BLEU), emphasizing complexity. Foundational dataset for Hindu epic text NLP.

---

### 12. Samayik: A Benchmark and Dataset for English-Sanskrit Translation
- **Authors:** Ayush Maheshwari, Ashim Gupta, Amrith Krishna, Atul Kumar Singh, Ganesh Ramakrishnan, G. Anil Kumar, Jitin Singla
- **Year:** 2024
- **Venue:** LREC-COLING 2024
- **arXiv:** 2305.14004
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Sanskrit is the liturgical language of Hinduism)
- **Paper Type:** Benchmark | Dataset
- **Dataset Size:** ~53,000 parallel English-Sanskrit sentences (contemporary prose)
- **Languages:** English, Sanskrit
- **LLMs Tested:** 4 multilingual pre-trained models benchmarked
- **Code/Data:** https://github.com/ayushbits/saamayik
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> First contemporary prose Sanskrit benchmark. Models trained on this outperform those trained on classical poetry datasets. Benchmarks 4 multilingual pre-trained models for English-Sanskrit translation. Sanskrit is foundational to Hindu scriptural tradition.

---

### 13. Vedavani: A Benchmark Corpus for ASR on Vedic Sanskrit Poetry
- **Authors:** Sujeet Kumar, Pretam Ray, Abhinay Beerukuri, Shrey Kamoji, Manoj Balaji Jagadeeshan, Pawan Goyal
- **Year:** 2025
- **Venue:** World Sanskrit Conference 2025 / arXiv
- **arXiv:** 2506.00145
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Rig Veda, Atharva Veda)
- **Paper Type:** Benchmark | Dataset
- **Dataset Size:** 30,779 labelled audio samples, 54 hours (20,782 Rig Veda + 9,997 Atharva Veda verses)
- **Languages:** Vedic Sanskrit
- **LLMs Tested:** IndicWhisper (best performer), other ASR models
- **Code/Data:** https://huggingface.co/datasets/sanganaka/Vedavani-Dataset
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> First comprehensive ASR benchmark for Vedic Sanskrit poetry. 54 hours of audio from the Rig Veda and Atharva Veda with precise prosodic and rhythmic features. IndicWhisper performs best. Directly tests AI on core Hindu Vedic texts.

---

### 14. One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit NLP Tasks
- **Authors:** Sebastian Nehrdich, Oliver Hellwig, Kurt Keutzer
- **Year:** 2024
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2409.13920
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Sanskrit NLP includes Vedic texts)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** Novel multitask dataset for segmentation, lemmatization, morphosyntactic tagging
- **Languages:** Sanskrit (Classical and Vedic)
- **LLMs Tested:** ByT5-Sanskrit (pre-trained)
- **Code/Data:** https://github.com/sebastian-nehrdich/byt5-sanskrit-analyzers
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Pretrained language model for Sanskrit achieving SOTA on word segmentation, Vedic dependency parsing, and OCR post-correction. Provides unified benchmark across multiple Sanskrit NLP tasks. Sanskrit is the liturgical language of Hindu scriptures.

---

### 15. SanskritShala: A Neural Sanskrit NLP Toolkit with Web-Based Interface for Pedagogical and Annotation Purposes
- **Authors:** Tushar Sandhan, Anshul Agarwal, Jivnesh Sandhan, Laxmidhar Behera, Pawan Goyal
- **Year:** 2023
- **Venue:** ACL 2023 (System Demonstrations)
- **arXiv:** 2302.09527
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Sanskrit NLP for Hindu scriptural texts)
- **Paper Type:** Benchmark | Framework
- **Dataset Size:** 7 word embedding models + multiple annotated datasets (word similarity, relatedness, categorization, analogy)
- **Languages:** Sanskrit
- **LLMs Tested:** Neural models for 4 Sanskrit NLP modules
- **Code/Data:** https://cnerg.iitkgp.ac.in/sanskritshala / https://github.com/Jivnesh/SanskritShala
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> First neural-based Sanskrit NLP toolkit with web interface. Reports SOTA on word segmentation, morphological tagging, dependency parsing, and compound identification benchmarks. Releases 7 word embedding models for Sanskrit. Foundation for processing Hindu scriptural texts.

---

### 16. Transformer-based Pouranic Topic Classification in Indian Mythology (PouranicTopic Dataset)
- **Authors:** (Published in Sadhana journal, 2024; specific author names not confirmed via search)
- **Year:** 2024
- **Venue:** Sadhana (Indian Academy of Sciences)
- **arXiv:** N/A
- **DOI:** 10.1007/s12046-024-02598-6
- **Religious Traditions:** Hinduism
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 200,000+ verses from 7 major Hindu Puranic texts with canto, topic, and sentence labels
- **Languages:** English (translated from Sanskrit)
- **LLMs Tested:** BERT, RoBERTa, DistilBERT
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Introduces PouranicTopic dataset of 200K+ annotated verses from 7 major Hindu Puranas. Evaluates BERT, RoBERTa, and DistilBERT for topic classification. Creates additional similarity-based and log-likelihood-based datasets via sentence clustering. Major Hindu mythology AI resource.

---

### 17. Mytho-Annotator: An Annotation Tool for Indian Hindu Mythology
- **Authors:** Apurba Paul, Anupam Mondal, Sainik Kumar Mahata, Srijan Seal, Prasun Sarkar, Dipankar Das
- **Year:** 2023
- **Venue:** ICON 2023 (20th International Conference on Natural Language Processing)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism
- **Paper Type:** Framework | Dataset
- **Dataset Size:** NLP annotation tool for named entities, relationships, and events in Hindu mythology
- **Languages:** English
- **LLMs Tested:** NLP models for NER and relation extraction
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Web-based NLP annotation tool for Hindu mythology texts, labelling named entities, relationships, and event entities. Enables creation of annotated corpora for complex information extraction from mythological texts. Foundational tool for Hindu mythology NLP research.

---

### 18. Comparative Analysis of Religious Texts: NLP Approaches to the Bible, Quran, and Bhagavad Gita
- **Authors:** Mahit Nandan A D, Ishan Godbole, Pranav M Kapparad, Shrutilipi Bhattacharjee
- **Year:** 2025
- **Venue:** CLRel 2025 (New Horizons in Computational Linguistics for Religious Texts), Abu Dhabi, UAE
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Christianity, Islam
- **Paper Type:** Evaluation
- **Dataset Size:** Full texts of Bible, Quran, and Bhagavad Gita
- **Languages:** English
- **LLMs Tested:** LDA, GloVe, Sentence Transformers, VADER
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Comparative NLP analysis of three major religious texts including the Bhagavad Gita using topic modelling, semantic similarity, and sentiment analysis. Reveals shared and unique thematic patterns across Hindu, Christian, and Islamic scriptures.

---

### 19. Modeling the Sacred: Considerations when Using Religious Texts in Natural Language Processing
- **Authors:** Ben Hutchinson
- **Year:** 2024
- **Venue:** Findings of NAACL 2024
- **arXiv:** 2404.14740
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Buddhism, Sikhism (multi-faith including Hindu and Sikh)
- **Paper Type:** Framework
- **Dataset Size:** N/A (position paper)
- **Languages:** English
- **LLMs Tested:** N/A (discusses NLP use of religious texts broadly)
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R3

> Position paper on ethics of using religious texts (including Hindu/Sikh scriptures) in NLP. Argues that machine-learned models reproduce cultural values encoded in training data and that NLP's use of religious texts raises considerations beyond model biases, including data provenance and proselytism.

---

### 20. Exploring Similarity Measures and Intertextuality in Vedic Sanskrit Literature
- **Authors:** So Miyagawa, Yuki Kyogoku, Yuzuki Tsukagoshi, Kyoko Amano
- **Year:** 2024
- **Venue:** NLP4DH 2024 (4th International Conference on NLP for Digital Humanities), Miami, USA
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Vedic texts)
- **Paper Type:** Evaluation
- **Dataset Size:** Vedic Samhita texts (Maitrayanin Samhita and Kathaka Samhita)
- **Languages:** Vedic Sanskrit
- **LLMs Tested:** Word2Vec embeddings, TRACER text reuse detection
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Applies computational linguistics (Word2Vec, stylometry, TRACER) to analyze semantic similarity and intertextuality in Vedic Sanskrit Samhita texts. Demonstrates smaller chunk sizes are more effective for detecting intertextual parallels in ancient Hindu scriptures.

---

### 21. SAHAAYAK 2023: The Multi-Domain Bilingual Parallel Corpus of Sanskrit to Hindi for Machine Translation
- **Authors:** (Multiple authors, published on arXiv)
- **Year:** 2023
- **Venue:** arXiv (data article)
- **arXiv:** 2307.00021
- **DOI:** N/A
- **Religious Traditions:** Hinduism (includes 701 Gita shlokas + Sanskrit religious texts)
- **Paper Type:** Dataset
- **Dataset Size:** 1.5 million parallel Sanskrit-Hindi sentence pairs
- **Languages:** Sanskrit, Hindi
- **LLMs Tested:** Machine translation models
- **Code/Data:** Public domain release
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Largest public-domain Sanskrit dataset (1.5M sentence pairs) for Sanskrit-Hindi machine translation. Includes Bhagavad Gita shlokas and texts from multiple domains. Most extensive dataset with Sanskrit as one of its languages.

---

### 22. Lexical Analysis of Religious Texts Using Text Mining and Machine Learning Tools
- **Authors:** Charu Verma et al.
- **Year:** 2017
- **Venue:** International Journal of Computer Applications
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Sikhism, Jainism, Buddhism, Islam, Christianity, Taoism
- **Paper Type:** Evaluation
- **Dataset Size:** 10 world religious texts including Bhagwad Gita, Guru Granth Sahib, Agama (Jain), Rig Veda
- **Languages:** English
- **LLMs Tested:** POS tagging, Term Document Matrix (ML tools)
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R3

> Lexical analysis of 10 world religious texts including the Bhagavad Gita (Hindu), Guru Granth Sahib (Sikh), and Agama (Jain) using text mining and ML. Found Guru Granth Sahib had more verbs than most other texts. One of the few studies to computationally analyze Jain and Sikh scriptures alongside Hindu texts.

---

### 23. The Vedic Compound Dataset (VCD)
- **Authors:** Sven Sellmer, Oliver Hellwig
- **Year:** 2024
- **Venue:** MWE-UD Workshop @ LREC-COLING 2024
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Vedic Sanskrit)
- **Paper Type:** Dataset
- **Dataset Size:** Annotated compounds from Vedic Sanskrit (1500-500 BCE texts)
- **Languages:** Vedic Sanskrit
- **LLMs Tested:** N/A (provides linguistic annotation resource)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> First annotated compound dataset from Vedic Sanskrit, covering five of six basic compound types. Provides resources for computational study of Vedic Hindu texts. Useful for downstream NLP benchmarking on ancient Hindu religious language.

---

### 24. DharmicData: Comprehensive Open-Source Collection of Hindu Sacred Texts
- **Authors:** Bhavy Khatri (community project)
- **Year:** 2024
- **Venue:** GitHub (open-source)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism
- **Paper Type:** Dataset
- **Dataset Size:** Ramcharitmanas, Bhagavad Gita, Mahabharata (~1 lakh shlokas), Valmiki Ramayana, Rigveda, Yajurveda, Atharvaveda in JSON format
- **Languages:** Sanskrit, Hindi, English
- **LLMs Tested:** N/A (raw dataset for LLM training/evaluation)
- **Code/Data:** https://github.com/bhavykhatri/DharmicData (ODbL license)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Comprehensive structured JSON collection of major Hindu sacred texts ready for ML/LLM analysis. Covers Vedas, epics, and Gita. Open Database License. Suitable as training or evaluation corpus for Hindu knowledge QA.

---

### 25. Vedanta Datasets (for ML Analysis)
- **Authors:** Atmabodha (community project)
- **Year:** 2022+
- **Venue:** GitHub
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism (Vedanta philosophy)
- **Paper Type:** Dataset
- **Dataset Size:** Datasets from various Vedantic texts
- **Languages:** Sanskrit, English
- **LLMs Tested:** N/A (ML analysis ready)
- **Code/Data:** https://github.com/atmabodha/Vedanta_Datasets
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> Repository of datasets from Vedantic texts formatted for ML analysis. Useful for Hindu philosophical text classification and evaluation.

---

### 26. BaniDB / Shabad OS: Digital Gurbani Database
- **Authors:** Khalis Foundation / Shabad OS (community projects)
- **Year:** 2018+ (ongoing)
- **Venue:** GitHub / Web API
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Sikhism
- **Paper Type:** Dataset
- **Dataset Size:** 43,000+ corrections/changes to digitized Guru Granth Sahib; full Sikh canonical texts
- **Languages:** Gurmukhi (Punjabi), English
- **LLMs Tested:** N/A (structured database, API accessible)
- **Code/Data:** https://github.com/KhalisFoundation/banidb-api / https://github.com/shabados/database / https://www.banidb.com/
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R3

> Most precise digital Gurbani database with standardized lagamatras and padh chhedh. Covers Sri Guru Granth Sahib, Sri Dasam Granth, and other Sikh canonical texts. API accessible. Could be used for Sikh knowledge QA evaluation of LLMs.

---

### 27. JainGPT: AI-Powered Chatbot for Jain Literature
- **Authors:** JainKnowledge.com (built on JainELibrary.org and JainQQ.org collections)
- **Year:** 2023+
- **Venue:** Web application
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Jainism
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** Extensive digitized Jain literature and sacred texts (Jain Agamas and commentary)
- **Languages:** English, Hindi
- **LLMs Tested:** GPT-based (RAG on Jain corpus)
- **Code/Data:** https://jainknowledge.com / https://jaingpt.org/
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R3

> AI chatbot built on digitized Jain canonical texts and literature. Answers questions about Jain philosophy, Tirthankaras, and ahimsa principles. Knowledge base from JainELibrary.org. Could serve as baseline for evaluating LLM knowledge of Jainism. Responses not guaranteed correct -- validation needed.

---

---

## Summary

**Total papers/resources found:** 27

**Breakdown by religious tradition:**
- **Hinduism:** 25 papers (almost all have Hindu content; some overlap with others)
- **Sikhism:** 7 papers (papers 2, 3, 4, 6, 19, 22, 26 specifically address or include Sikh content)
- **Jainism:** 3 papers (papers 3, 22, 27 specifically address or include Jain content)

**Breakdown by paper type:**
- Benchmark: 11
- Dataset: 14
- Evaluation: 12
- Bias Study: 7
- Framework: 5
(Many papers span multiple types)

**Breakdown by implementation readiness:**
- HIGH: 16
- MEDIUM: 9
- LOW: 2

**Key gaps identified:**
1. **Jainism is severely underrepresented** -- no dedicated Jain NLP benchmark or LLM evaluation dataset exists in peer-reviewed literature. JainGPT is the closest but is a commercial product, not a research benchmark.
2. **Sikhism has no dedicated NLP benchmark** -- GurbaniDB exists as a digital corpus but no published paper evaluates LLMs specifically on Sikh knowledge or values. The Guru Granth Sahib is included in a few multi-faith comparative studies only.
3. **Hindu ethics/values alignment for LLMs is nascent** -- While several bias studies test how LLMs represent Hinduism, no dedicated "Hindu values alignment benchmark" exists akin to Islamic Fatwa QA or Confucian ethics LLM evaluations.
4. **Sanskrit NLP is flourishing** but primarily focused on linguistic tasks (translation, segmentation, parsing) rather than evaluating LLM understanding of Hindu philosophical/ethical content.
5. **The most impactful new finds** are the religious bias studies (papers 1-7) that directly evaluate LLM bias toward/against Hinduism, Sikhism, and Jainism across multiple dimensions.

**Papers excluded (already in vault):**
- GurbaniDB (line 7)
- Decolonial AI Alignment: Openness, Visesa-Dharma (line 444)
- Indian-BhED (line 326)
- IndiBias (line 405)
- BRAND: Bilingual Religious Accountable Norm Dataset (line 598)
- FairI Tales / INDIC-BIAS (line 693)
- IndiCASA (line 733)
- Contemplative Artificial Intelligence (line 643)
