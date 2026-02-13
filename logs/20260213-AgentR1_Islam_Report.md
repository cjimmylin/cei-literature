# Agent R1 Report: Islamic NLP/AI Benchmarks, Datasets, and Evaluation Papers

**Agent:** R1 (Islam -- Expansion Beyond Existing Vault Coverage)
**Date:** 2026-02-13
**Search Focus:** Additional Islamic NLP/AI benchmarks, datasets, and evaluation papers NOT already in the CEI Literature Vault

**Existing vault coverage (excluded from this report):**
IslamTrust, QASiNa, Hajj-FQA, IslamicEval, QIAS, FatwaSet, IslamicPCQA, Sirah Nabawiyah, AraTrust, Saudi-Alignment Benchmark, BRAND, Optimized Quran Passage Retrieval, A Benchmark Dataset with Larger Context for Non-Factoid QA over Islamic Text, Fine-tuning Large Language Model (BERT) for Islamic Moral Inquiry, PalmX 2025, Palm, Aftina, Qur'an QA 2022

---

### 1. Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions (FiqhQA)
- **Authors:** Farah Atif, Nursultan Askarbekuly, Kareem Darwish, Monojit Choudhury
- **Year:** 2025
- **Venue:** AIES 2025 (8th AAAI/ACM Conference on AI, Ethics, and Society) / arXiv
- **arXiv:** 2508.08287
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 960 question-answer pairs (120 unique questions x 4 schools x 2 languages)
- **Languages:** Arabic, English
- **LLMs Tested:** GPT-4o, Gemini, Fanar, and others
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Introduces FiqhQA, the first benchmark evaluating LLMs on school-specific Islamic jurisprudence (Maliki, Shafi'i, Hanafi, Hanbali). Evaluates both accuracy and abstention behavior -- the ability of LLMs to recognize when not to answer. All models show performance drop in Arabic. GPT-4o achieved highest accuracy; Gemini and Fanar demonstrate superior abstention behavior.

---

### 2. Assessing Large Language Models on Islamic Legal Reasoning: Evidence from Inheritance Law Evaluation
- **Authors:** Abdessalam Bouchekif, Samer Rashwani, Heba Sbahi, Shahd Gaben, Mutaz Al-Khatib, Mohammed Ghaly
- **Year:** 2025
- **Venue:** ArabicNLP 2025 (3rd Arabic NLP Conference) / arXiv
- **arXiv:** 2509.01081
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 1,000 multiple-choice questions on Islamic inheritance law
- **Languages:** Arabic, English
- **LLMs Tested:** o3, Gemini 2.5, ALLaM, Fanar, LLaMA, Mistral, GPT-4o
- **Code/Data:** https://github.com/bouchekif/inheritance_evaluation
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Evaluates 7 LLMs on Islamic inheritance law ('ilm al-mawarith). O3 and Gemini 2.5 achieved >90% accuracy; ALLaM, Fanar, LLaMA, Mistral scored <50%. Detailed error analysis identifies misunderstandings of inheritance scenarios, incorrect application of legal rules, and insufficient domain knowledge.

---

### 3. Benchmarking the Legal Reasoning of LLMs in Arabic Islamic Inheritance Cases
- **Authors:** Nouar AlDahoul, Yasir Zaki
- **Year:** 2025
- **Venue:** arXiv (related to QIAS 2025 Challenge)
- **arXiv:** 2508.15796
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** QIAS 2025 challenge dataset (Arabic inheritance scenarios)
- **Languages:** Arabic
- **LLMs Tested:** Gemini Flash 2.5, Gemini Pro 2.5, GPT o3
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Evaluates LLMs on identifying heirs, computing inheritance shares, and justifying reasoning aligned with Islamic legal principles. Proposes a majority voting solution leveraging three models that achieves up to 92.7% accuracy in the QIAS 2025 competition.

---

### 4. From RAG to Agentic RAG for Faithful Islamic Question Answering (IslamicFaithQA)
- **Authors:** Gagan Bhatia, Hamdy Mubarak, Mustafa Jarrar, George Mikros, Fadi Zaraket, Mahmoud Alhirthani, Mutaz Al-Khatib, Logan Cochrane, Kareem Darwish, Rashid Yahiaoui, Firoj Alam
- **Year:** 2026
- **Venue:** arXiv
- **arXiv:** 2601.07528
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Benchmark | Dataset | Framework
- **Dataset Size:** 3,810 bilingual QA items (IslamicFaithQA) + 25K SFT pairs + 5K preference samples + ~6K verse-level Quran corpus
- **Languages:** Arabic, English
- **LLMs Tested:** Multiple (various sizes), evaluated with agentic RAG framework
- **Code/Data:** Planned public release
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Introduces IslamicFaithQA, a 3,810-item bilingual generative benchmark with atomic single-gold answers for measuring hallucination and abstention. Includes an end-to-end grounded Islamic modelling suite (25K SFT reasoning pairs, 5K preference samples, verse-level Quran retrieval corpus). Agentic RAG framework achieves state-of-the-art performance via iterative evidence seeking.

---

### 5. Can LLMs Write Faithfully? An Agent-Based Evaluation of LLM-generated Islamic Content
- **Authors:** Abdullah Mushtaq, Rafay Naeem, Ezieddin Elmahjub, Ibrahim Ghaznavi, Shawqi Al-Maliki, Mohamed Abdallah, Ala Al-Fuqaha, Junaid Qadir
- **Year:** 2025
- **Venue:** NeurIPS 2025 Workshop on Muslims in Machine Learning / arXiv
- **arXiv:** 2510.24438
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Framework
- **Dataset Size:** 200 prompts from authentic Islamic blogs
- **Languages:** English, Arabic
- **LLMs Tested:** GPT-4o, Ansari AI, Fanar
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Dual-agent evaluation framework with quantitative scoring (6 dimensions: Structure, Islamic Consistency, Citations, etc.) and qualitative side-by-side comparison (5 dimensions: Tone, Depth, Originality, etc.). GPT-4o scored highest in Islamic Accuracy (3.93/5) and Citation (3.38/5). Highlights that models still fall short in reliably producing accurate Islamic citations.

---

### 6. LLMs and Islamic Fiqh: A Reliability Study
- **Authors:** Unknown (OpenReview paper)
- **Year:** 2025
- **Venue:** OpenReview (workshop paper)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 550 questions across 3 Fiqh domains (Tahara, Fiqh Al-Nikah, Buyu)
- **Languages:** Arabic
- **LLMs Tested:** GPT-4o, ALLaM
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

First systematic study of school-specific Islamic legal reasoning focusing on Maliki Fiqh. Tests GPT-4o and ALLaM on 550 curated questions across purification (Tahara), marital jurisprudence (Fiqh Al-Nikah), and financial transactions (Buyu). Highlights gaps in adherence to established Fiqhi rules.

---

### 7. I Am Aligned, But With Whom? MENA Values Benchmark for Evaluating Cultural Alignment and Multilingual Bias in LLMs (MENAValues)
- **Authors:** Pardis Sadat Zahraei, Ehsaneddin Asgari
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.13154
- **DOI:** N/A
- **Religious Traditions:** Islam (primary context: MENA region, Muslim-majority societies)
- **Paper Type:** Benchmark | Bias Study
- **Dataset Size:** Population-level survey response distributions from 16 MENA countries
- **Languages:** English, Arabic, Persian, Turkish
- **LLMs Tested:** 7 diverse models
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

MENAValues benchmark evaluates cultural alignment with MENA region values using large-scale authoritative surveys. Discovers three phenomena: Cross-Lingual Value Shifts (language changes responses), Reasoning-Induced Degradation (reasoning prompts worsen alignment), and Logit Leakage (hidden preferences despite refusals). Models treat diverse MENA nations as monolithic when in native languages.

---

### 8. Sometimes the Model doth Preach: Quantifying Religious Bias in Open LLMs through Demographic Analysis in Asian Nations
- **Authors:** Hari Shankar, Vedanta S P, Tejas Cavale, Ponnurangam Kumaraguru, Abhijnan Chakraborty
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2503.07510
- **DOI:** N/A
- **Religious Traditions:** Islam, Hinduism, Christianity, Buddhism (multi-faith, with emphasis on Muslim communities in Asia)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Survey-based evaluation across multiple Asian nations
- **Languages:** English
- **LLMs Tested:** Llama, Mistral (open-source models)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Evaluates religious bias in open LLMs using surveys on religious tolerance and identity across Asian nations (with emphasis on India). Uses Hamming Distance to compare model outputs against human survey responses. Finds most open LLMs match a single homogeneous profile, raising concerns about promoting hegemonic worldviews and undermining minority perspectives including Muslim communities.

---

### 9. Persistent Anti-Muslim Bias in Large Language Models
- **Authors:** Abubakar Abid, Maheen Farooqi, James Zou
- **Year:** 2021
- **Venue:** AIES 2021 (AAAI/ACM Conference on AI, Ethics, and Society) / arXiv
- **arXiv:** 2101.05783
- **DOI:** 10.1145/3461702.3462624
- **Religious Traditions:** Islam
- **Paper Type:** Bias Study
- **Dataset Size:** Multiple evaluation probes (prompt completion, analogical reasoning, story generation)
- **Languages:** English
- **LLMs Tested:** GPT-3
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Foundational study demonstrating persistent Muslim-violence bias in GPT-3. "Muslim" analogized to "terrorist" in 23% of test cases (vs "Jewish"-"money" at 5%). Violent completions for Muslim contexts at 66%, reduced to 20% with positive adjectives but still higher than other religious groups. Demonstrates bias appears consistently across prompt completion, analogy, and story generation tasks.

---

### 10. Building Domain-Specific LLMs Faithful To The Islamic Worldview: Mirage or Technical Possibility?
- **Authors:** Shabaz Patel, Hassan Kane, Rayhan Patel
- **Year:** 2023
- **Venue:** Muslims in ML Workshop at NeurIPS 2023 / arXiv
- **arXiv:** 2312.06652
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** N/A (framework paper)
- **Languages:** English, Arabic
- **LLMs Tested:** Multiple LLMs with different prompting strategies (few-shot, zero-shot)
- **Code/Data:** https://github.com/shabazpatel/domain-specific-llm
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Proposes a comprehensive framework for developing domain-specific LLMs aligned with the Islamic worldview, grounded in Quran and Sunnah. Addresses stereotypical biases and hallucination of non-existent facts. Few-shot prompting consistently emerges as the superior method. Emphasizes need for high-quality Islamic datasets and interdisciplinary ML-Islamic scholarship collaboration.

---

### 11. Investigating Retrieval-Augmented Generation in Quranic Studies: A Study of 13 Open-Source Large Language Models
- **Authors:** Zahra Khalila, Arbi Haza Nasution, Winda Monika, Aytug Onan, Yohei Murakami, Yasir Bin Ismail Radi, Noor Mohammad Osmani
- **Year:** 2025
- **Venue:** IJACSA / arXiv
- **arXiv:** 2503.16581
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation
- **Dataset Size:** Quranic QA evaluation set (specific size not stated)
- **Languages:** Arabic, English
- **LLMs Tested:** 13 open-source models: Llama3:70b, Gemma2:27b, QwQ:32b, Gemma2:9b, Llama3:8b, Llama3.2:3b, Phi3:3.8b, and others
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Systematic evaluation of 13 open-source LLMs (categorized by size: large, medium, small) with RAG for Quranic question answering. Measures context relevance, answer faithfulness, and answer relevance. Notably, small Llama3.2:3b achieves high faithfulness (4.619) and relevance (4.857), suggesting optimized smaller models can match larger ones.

---

### 12. FARSIQA: Faithful and Advanced RAG System for Islamic Question Answering
- **Authors:** Mohammad Aghajani Asl, Behrooz Minaei Bidgoli
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2510.25621
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** Knowledge base of 1M+ authoritative Islamic documents; evaluated on IslamicPCQA benchmark
- **Languages:** Persian
- **LLMs Tested:** Evaluated within FAIR-RAG architecture
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Introduces FARSIQA for Persian Islamic QA using a self-correcting FAIR-RAG architecture that adaptively decomposes complex queries and iteratively fills information gaps. Achieves 97.0% Negative Rejection rate (40-point improvement over baselines) and 74.3% Answer Correctness on the IslamicPCQA benchmark.

---

### 13. From RAG to Agentic: Validating Islamic-Medicine Responses with LLM Agents (Tibbe-AG)
- **Authors:** Mohammad Amaan Sayeed, Mohammed Talha Alam, Raza Imam, Shahab Saquib Sohail, Amir Hussain
- **Year:** 2025
- **Venue:** Muslims in Machine Learning Workshop at ICML 2025 / arXiv
- **arXiv:** 2506.15911
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Framework
- **Dataset Size:** 30 curated Prophetic-medicine questions aligned with human-verified remedies
- **Languages:** English
- **LLMs Tested:** LLaMA-3, Mistral-7B, Qwen2-7B
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Proposes Tibbe-AG, an evaluation pipeline for Islamic prophetic medicine (Tibb-e-Nabawi) using Avicenna's Canon of Medicine and prophetic health traditions. Compares direct generation, RAG, and agentic self-critique approaches. Retrieval improves factual accuracy by 13%; agentic prompting adds another 10% improvement.

---

### 14. MufassirQAS: Improving LLM Reliability with RAG in Religious Question-Answering
- **Authors:** Ahmet Yusuf Alan, Enis Karaarslan, Omer Aydin
- **Year:** 2024
- **Venue:** Turkish Journal of Engineering / arXiv
- **arXiv:** 2401.15378
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** Curated knowledge base of Turkish Islamic texts (translations and interpretations)
- **Languages:** Turkish
- **LLMs Tested:** Compared against ChatGPT
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

RAG-based Islamic QA system using a vector database of fundamental Turkish Islamic texts. Provides source page numbers and referenced articles for transparency. Outperforms ChatGPT on sensitive religious questions. Addresses hallucination and inappropriate content generation in religious contexts.

---

### 15. Is GPT-4 a Good Islamic Expert for Answering Quran Questions?
- **Authors:** Sarah Alnefaie, Eric Atwell, Mohammad Ammar Alsalka
- **Year:** 2023
- **Venue:** ROCLING 2023 (35th Conference on Computational Linguistics and Speech Processing) / ACL Anthology
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Dataset
- **Dataset Size:** 2,189 questions (QUQA dataset)
- **Languages:** Arabic, English
- **LLMs Tested:** GPT-4
- **Code/Data:** QUQA dataset (available via thesis/ACL)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Evaluates GPT-4 on Quranic question answering using the newly created QUQA dataset (2,189 questions). Finds GPT-4 struggles with classical Arabic, semantic ambiguity, and contextual meaning. Three main issues: misinterpretation of religious context, unreliable answers not grounded in authoritative Islamic sources, and sensitivity to phrasing variations. Follow-up work showed RAG substantially improved results.

---

### 16. HAQA and QUQA: Constructing Two Arabic Question-Answering Corpora for the Quran and Hadith
- **Authors:** Sarah Alnefaie, Eric Atwell, Mohammad Ammar Alsalka
- **Year:** 2023
- **Venue:** RANLP 2023 / ACL Anthology
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** QUQA: 3,369 records (2,189 unique questions, 301K+ tokens); HAQA: Hadith QA corpus (size in thesis)
- **Languages:** Arabic
- **LLMs Tested:** N/A (dataset paper)
- **Code/Data:** https://aclanthology.org/2023.ranlp-1.10/
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Creates two Arabic QA corpora: QUQA for the Quran (covering ~47% of Quran verses) and HAQA for Hadith. The most extensive collection of Arabic QA pairs for the Quran. Questions span factual, inferential, and interpretive types. Useful as gold-standard evaluation datasets for LLMs.

---

### 17. Quran-MD: A Fine-Grained Multilingual Multimodal Dataset of the Quran
- **Authors:** Muhammad Umar Salman, Mohammad Areeb Qazi, Mohammed Talha Alam
- **Year:** 2026
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track / arXiv
- **arXiv:** 2601.17880
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** 114 surahs, 6,236 ayahs (~77.8K words), audio from 32 reciters
- **Languages:** Arabic, English (translations, transliterations)
- **LLMs Tested:** N/A (dataset paper)
- **Code/Data:** https://huggingface.co/datasets (CC0 license)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

First holistic multimodal Quranic dataset integrating textual, linguistic, and audio data at verse and word levels. Includes Arabic text, English translations, phonetic transliterations, and verse-level audio from 32 reciters. Supports ASR, tajweed detection, Quranic TTS, multimodal embeddings, semantic retrieval, and personalized tutoring.

---

### 18. Cross-Language Approach for Quranic QA
- **Authors:** Islam Oshallah, Mohamed Basem, Ali Hamdi, Ammar Mohammed
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2501.17449
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Dataset
- **Dataset Size:** Expanded from Qur'an QA shared task dataset (augmented via translation and paraphrasing)
- **Languages:** Arabic, English (cross-language)
- **LLMs Tested:** BERT-Medium, RoBERTa-Base, DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, Falcon
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Addresses the linguistic gap between Modern Standard Arabic (questions) and Classical Arabic (Quranic answers) through cross-language augmentation. Fine-tunes 7 language models; RoBERTa-Base achieves highest MAP@10 (0.34) and MRR (0.52). Demonstrates cross-language strategies significantly improve Quranic QA performance.

---

### 19. Fabricated Hadith Detection: A Novel Matn-Based Approach With Transformer Language Models (MAHADDAT)
- **Authors:** Kamel Gaanoun, Mohammed Alsuhaibani
- **Year:** 2022
- **Venue:** IEEE Access
- **arXiv:** N/A
- **DOI:** 10.1109/ACCESS.2022.3217390
- **Religious Traditions:** Islam
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** MAHADDAT dataset (first dedicated Mawdu Hadith dataset; exact size in paper)
- **Languages:** Arabic
- **LLMs Tested:** BERT-based transformer models
- **Code/Data:** MAHADDAT dataset (released with paper)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Creates MAHADDAT, the first dataset dedicated to fabricated (Mawdu) Hadith detection. Uses Matn (textual content) analysis rather than solely Sanad (narrator chain). BERT-based system achieves 92.47% F1 score. Foundational resource for Hadith authenticity verification using NLP.

---

### 20. Pretrained Models Against Traditional Machine Learning for Detecting Fake Hadith
- **Authors:** Multiple (MDPI Electronics 2025)
- **Year:** 2025
- **Venue:** MDPI Electronics
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Dataset
- **Dataset Size:** 8,544 Hadiths (7,008 authentic + 1,536 fake)
- **Languages:** Arabic
- **LLMs Tested:** mBERT, CamelBERT, AraBERT, plus classical ML (LR, SVM)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

First systematic comparison of pretrained language models vs. traditional ML for Hadith authentication. AraBERT achieves 99.94% F1 when including Isnad (narrator chain), demonstrating the profound effectiveness of contextual elements. Imbalanced dataset (7,008 vs 1,536) reflects real-world distribution.

---

### 21. Hadiths Classification Using a Novel Author-Based Hadith Classification Dataset (ABCD)
- **Authors:** Multiple (MDPI Big Data and Cognitive Computing 2023)
- **Year:** 2023
- **Venue:** MDPI Big Data and Cognitive Computing
- **arXiv:** N/A
- **DOI:** 10.3390/bdcc7030141
- **Religious Traditions:** Islam
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 29K Hadiths, 18K unique narrators
- **Languages:** Arabic
- **LLMs Tested:** ML and DL models (not LLMs per se)
- **Code/Data:** Papers with Code listing
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Creates ABCD (Author-Based Classification Dataset) from classical Hadith books. ML achieves 77% F1 on Matn data; DL achieves 92% F1 on Sanad data. Provides a novel author-based classification approach complementing content-based methods.

---

### 22. Sanadset 650K: Data on Hadith Narrators
- **Authors:** Multiple (Data in Brief, 2022)
- **Year:** 2022
- **Venue:** Data in Brief (ScienceDirect)
- **arXiv:** N/A
- **DOI:** 10.1016/j.dib.2022.108566
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** 650,986 records from 926 historical Arabic Hadith books
- **Languages:** Arabic
- **LLMs Tested:** N/A (dataset paper)
- **Code/Data:** https://data.mendeley.com/datasets/5xth87zwb5/4
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Large-scale Hadith narrator chain (Sanad) dataset extracted from 926 historical Arabic books. Enables automated Sanad evaluation for Hadith authentication (Strong/Weak classification) and narrator trustworthiness assessment. Usable as a linguistic resource for Arabic NLP. 159,558 Hadiths lack Sanads.

---

### 23. Multi-IsnadSet (MIS) for Sahih Muslim Hadith
- **Authors:** Aziz Mehmood Farooqi, Rauf Ahmed Shams Malick, Muhammad Shahzad Shaikh, Adnan Akhunzada
- **Year:** 2024
- **Venue:** Data in Brief (ScienceDirect)
- **arXiv:** N/A
- **DOI:** 10.1016/j.dib.2024.110439
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** 2,092 narrator nodes, 77,797 edges (Sanad-Hadith connections)
- **Languages:** Arabic
- **LLMs Tested:** N/A (dataset paper)
- **Code/Data:** https://data.mendeley.com/datasets/gzprcr93zn/2
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Graph-structured dataset of multiple Isnad chains for Sahih Muslim Hadith. Represents narrator networks as directed graphs. Enables credibility analysis, classification (Sahih/Dhaif), and narrator trustworthiness assessment using graph analysis tools (NetworkX, Neo4j, Gephi, CytoScape).

---

### 24. Leveraging Large Language Models for Detecting and Preserving Emotions in Quran Translations (ELQV)
- **Authors:** Multiple (Journal of King Saud University, 2025)
- **Year:** 2025
- **Venue:** Journal of King Saud University Computer and Information Sciences
- **arXiv:** N/A
- **DOI:** 10.1007/s44443-025-00269-y
- **Religious Traditions:** Islam
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** ELQV: 2,100 Quran verses annotated by PhD-level specialists
- **Languages:** Arabic, English (7 English translations evaluated)
- **LLMs Tested:** Multiple LLMs (for emotion detection)
- **Code/Data:** https://github.com/Arwaalmrzoqi/ELQV
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Introduces ELQV (Emotionally-Labeled Quran Verses), 2,100 verses annotated for four emotions (fear 32.14%, joy 28.05%, anger 23.57%, sadness 16.24%) by Arabic linguistics/Islamic law PhD experts. Evaluates LLMs' ability to comprehend emotional semantics in Classical Arabic scripture and 7 English translations. Cohen's Kappa scores range 0.29-0.35 between translations and Arabic readers.

---

### 25. Challenging the Transformer-based Models with a Classical Arabic Dataset: Quran and Hadith
- **Authors:** Shatha Altammami, Eric Atwell
- **Year:** 2022
- **Venue:** LREC 2022 / ACL Anthology
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 310 Quran-Hadith pairs + 4,072 Quran-verse pairs (balanced related/non-related)
- **Languages:** Arabic (Classical)
- **LLMs Tested:** Monolingual, bilingual, and multilingual transformer models
- **Code/Data:** https://github.com/ShathaTm/Quran_Hadith_Datasets
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R1

Evaluates transformer models on detecting relatedness between Quran verses and Hadith teachings using a carefully curated dataset verified by religious experts. Tests monolingual, bilingual, and multilingual models on Classical Arabic text understanding.

---

### 26. Fabricating Holiness: Characterizing Religious Misinformation Circulators on Arabic Social Media
- **Authors:** Mahmoud Fawzi, Bjorn Ross, Walid Magdy
- **Year:** 2025
- **Venue:** ICWSM 2026 (AAAI Press) / arXiv
- **arXiv:** 2508.07845
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Fabricated Hadith dataset from Arabic social media (size in paper)
- **Languages:** Arabic
- **LLMs Tested:** N/A (uses logistic regression for classification)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Studies fabricated Hadith circulation on Arabic social media as a case of religious misinformation. Uses logistic regression to predict circulator vs. debunker behavior. Circulators follow Shia accounts, Sunni Gulf figures, and non-professional Islamic pages; debunkers follow academic Islamic scholars and have broader intellectual interests.

---

### 27. Artificial Intelligence (AI) in Islamic Ethics: Towards Pluralist Ethical Benchmarking for AI
- **Authors:** Ezieddin Elmahjub
- **Year:** 2023
- **Venue:** Philosophy & Technology (Springer)
- **arXiv:** N/A
- **DOI:** 10.1007/s13347-023-00668-x
- **Religious Traditions:** Islam
- **Paper Type:** Framework
- **Dataset Size:** N/A (theoretical framework)
- **Languages:** English
- **LLMs Tested:** N/A
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R1

Proposes an Islamic ethical framework for AI benchmarking, emphasizing maslaha (the common good) as normative guide. Argues against Western/Eurocentric dominance in ethical AI discourse. Draws on both textual and non-textual Islamic sources. Foundational theoretical paper for Islamic AI ethics benchmarking.

---

### 28. Islamic Ethics and AI: An Evaluation of Existing Approaches to AI using Trusteeship Ethics
- **Authors:** Not fully identified (Philosophy & Technology, 2025)
- **Year:** 2025
- **Venue:** Philosophy & Technology (Springer)
- **arXiv:** N/A
- **DOI:** 10.1007/s13347-025-00922-4
- **Religious Traditions:** Islam
- **Paper Type:** Framework
- **Dataset Size:** N/A (theoretical framework)
- **Languages:** English
- **LLMs Tested:** N/A
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R1

Introduces Taha Abdurrahman's I'timani (trusteeship) framework for AI ethics, integrating three covenants: Ontological, Epistemological, and Existential. Critiques limitations of Maqasid al-Shariah and Qawaid Fiqhiyya approaches. Proposes a unified ethical model addressing AI's spiritual and metaphysical dimensions absent from Western frameworks.

---

### 29. Quranic Audio Dataset: Crowdsourced and Labeled Recitation from Non-Arabic Speakers
- **Authors:** Raghad Salameh, Mohamad Al Mdfaa, Nursultan Askarbekuly, Manuel Mazzara
- **Year:** 2024
- **Venue:** arXiv / ScienceDirect
- **arXiv:** 2405.02675
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** ~7,000 recitations from 1,287 participants across 11+ non-Arabic countries; 1,166 annotated in 6 categories
- **Languages:** Arabic (Quranic), Multi-lingual speakers
- **LLMs Tested:** N/A (dataset for ASR/pronunciation assessment)
- **Code/Data:** https://huggingface.co/datasets/RetaSy/quranic_audio_dataset
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Crowdsourced Quranic recitation dataset focused on non-Arabic speakers learning to recite. Collected via NamazApp mobile application, annotated on Quran Voice platform. Crowd accuracy 0.77, inter-rater agreement 0.63, algorithm-expert agreement 0.89. Enables building AI pronunciation tutors for Quran learners.

---

### 30. The Tarteel Dataset: Crowd-Sourced and Labeled Quranic Recitation
- **Authors:** Khan et al.
- **Year:** 2023
- **Venue:** OpenReview
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** 25,000 audio clips (67.39 hours), 1,200+ unique individuals
- **Languages:** Arabic (Quranic)
- **LLMs Tested:** N/A (speech dataset)
- **Code/Data:** Tarteel.ai / Quranic Universal Library
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

First large-scale crowd-sourced Quranic recitation dataset. "In-the-wild" dataset with real-world noise from diverse reciters of different ages, genders, and ethnicities. Collected over 6 months. Schema enables standardized paired Quranic audio-text datasets for ASR and related tasks.

---

### 31. Two-Stage Quranic QA via Ensemble Retrieval and Instruction-Tuned Answer Extraction
- **Authors:** Mohamed Basem et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2508.06971
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation
- **Dataset Size:** Qur'an QA 2023 Shared Task dataset
- **Languages:** Arabic, English
- **LLMs Tested:** Ensembles of fine-tuned Arabic language models; instruction-tuned LLMs with few-shot prompting
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Achieves state-of-the-art on Qur'an QA 2023 Shared Task with MAP@10 of 0.3128 and pAP@10 of 0.669. Two-stage approach: (1) ensemble fine-tuned Arabic models for passage retrieval, (2) instruction-tuned LLMs with few-shot prompting for answer extraction.

---

### 32. Few-Shot Prompting for Extractive Quranic QA with Instruction-Tuned LLMs
- **Authors:** Mohamed Basem et al.
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2508.06103
- **DOI:** N/A
- **Religious Traditions:** Islam
- **Paper Type:** Evaluation
- **Dataset Size:** Qur'an QA shared task dataset
- **Languages:** Arabic
- **LLMs Tested:** Gemini, DeepSeek
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Develops a specialized Arabic prompt framework for span extraction from Quranic text. Post-processing system integrates subword alignment, overlap suppression, and semantic filtering to reduce hallucinations. Best configuration achieves pAP10 score of 0.637. Demonstrates instruction-tuned LLMs with Arabic prompts outperform traditional fine-tuned models.

---

### 33. MASAQ: Morphologically-Analyzed and Syntactically-Annotated Quran Dataset
- **Authors:** Multiple (Data in Brief, 2024)
- **Year:** 2024
- **Venue:** Data in Brief (ScienceDirect)
- **arXiv:** N/A
- **DOI:** 10.1016/j.dib.2024.111173
- **Religious Traditions:** Islam
- **Paper Type:** Dataset
- **Dataset Size:** 131K+ morphological entries, 123K+ syntactic function instances, 72 syntactic roles
- **Languages:** Arabic (Classical/Quranic)
- **LLMs Tested:** N/A (linguistic resource)
- **Code/Data:** https://data.mendeley.com/datasets/9yvrzxktmr
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R1

Comprehensive morphological and syntactic annotation of the entire Quran using verified Tanzil.net text. Features 72 syntactic roles, detailed morphological analysis, and context-specific annotations by expert Arabic linguists using traditional i'rab methodologies. Available in TSV, SQLite, CSV, and JSON formats. Valuable for dependency parsing, grammar checking, MT, and text summarization of Classical Arabic.

---

## Summary

**Total papers found:** 33

**Breakdown by Paper Type:**
- Benchmark/Evaluation: 17
- Dataset: 12
- Framework: 5
- Bias Study: 3
(some papers span multiple categories)

**Breakdown by Topic:**
- Quranic QA and retrieval: 10 (entries 11, 12, 15, 16, 17, 18, 24, 25, 31, 32)
- Islamic jurisprudence/Fiqh evaluation: 5 (entries 1, 2, 3, 4, 6)
- Hadith NLP and authentication: 5 (entries 19, 20, 21, 22, 23)
- Islamic values/worldview alignment: 4 (entries 5, 7, 10, 14)
- Anti-Muslim/religious bias: 3 (entries 8, 9, 26)
- Islamic ethics frameworks for AI: 2 (entries 27, 28)
- Islamic medicine evaluation: 1 (entry 13)
- Quranic recitation/audio: 3 (entries 17, 29, 30)
- Quranic linguistic resources: 1 (entry 33)

**Key observations:**
1. Islamic legal reasoning (inheritance law, school-specific rulings) is a rapidly growing evaluation domain with 5+ papers in 2025 alone
2. Quranic QA has matured from shared tasks (2022-2023) to sophisticated RAG and agentic approaches (2025-2026)
3. Hadith authentication using transformers is well-established with multiple dedicated datasets (MAHADDAT, ABCD, Sanadset)
4. Anti-Muslim bias in LLMs remains a documented concern since 2021 (Abid et al.), with newer work examining bias in Asian and MENA contexts
5. Islamic ethics frameworks for AI are emerging but still largely theoretical (Elmahjub 2023, Trusteeship Ethics 2025)
6. Most benchmarks test in both Arabic and English; Persian (FARSIQA) and Turkish (MufassirQAS) are underrepresented
7. The IslamicFaithQA benchmark (entry 4) is the largest and most comprehensive Islamic QA benchmark found (3,810 items + extensive training resources)
