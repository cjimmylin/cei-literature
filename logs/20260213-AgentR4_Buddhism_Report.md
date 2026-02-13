# Agent R4 Report: Buddhism -- LLM/NLP Benchmarks, Datasets, and Evaluation Papers

**Agent:** R4 (Buddhism Focus)
**Date:** 2026-02-13
**Search Scope:** Buddhist NLP/AI benchmarks, datasets, and evaluation papers across all traditions (Theravada, Mahayana, Vajrayana, Zen)

---

## Papers Found

### 1. DharmaBench: Evaluating Language Models on Buddhist Texts in Sanskrit and Tibetan
- **Authors:** Kai Golan Hashiloni, Shay Cohen, Asaf Shina, Jingyi Yang, Orr Meir Zwebner, Nicola Bajetta, Guy Bilitski, Rebecca Sunden, Guy Maduel, Ryan Conlon, Ari Barzilai, Daniel Mass, Shanshan Jia, Aviv Naaman, Sonam Choden, Sonam Jamtsho, Yadi Qu, Harunaga Isaacson, Dorji Wangchuk, Shai Fine, Orna Almogi, Kfir Bar
- **Year:** 2025
- **Venue:** IJCNLP-AACL 2025 (Proceedings of the 14th International Joint Conference on Natural Language Processing)
- **arXiv:** N/A
- **DOI:** N/A (ACL Anthology: 2025.ijcnlp-long.114)
- **Religious Traditions:** Buddhism (Theravada, Mahayana, Vajrayana -- Sanskrit and Classical Tibetan canonical texts)
- **Paper Type:** Benchmark | Dataset
- **Dataset Size:** 13 classification and detection tasks (6 Sanskrit, 7 Tibetan, 4 shared)
- **Languages:** Sanskrit, Classical Tibetan, English
- **LLMs Tested:** GPT-4o and smaller domain-specific systems
- **Code/Data:** Publicly released under CC-BY-4 License (code under Apache-2.0)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 2. MITRA: A Large-Scale Parallel Corpus and Multilingual Pretrained Language Model for Machine Translation and Semantic Retrieval for Pali, Sanskrit, Buddhist Chinese, and Tibetan
- **Authors:** Sebastian Nehrdich, Kurt Keutzer (and collaborators at Berkeley AI Research / Dharmamitra)
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** 2601.06400
- **DOI:** N/A
- **Religious Traditions:** Buddhism (all major canonical traditions -- Pali, Sanskrit, Chinese, Tibetan)
- **Paper Type:** Dataset | Framework
- **Dataset Size:** 1.74 million parallel sentence pairs; semantic embedding benchmark
- **Languages:** Pali, Sanskrit, Buddhist Chinese, Tibetan, English
- **LLMs Tested:** Gemma 2 MITRA-MT, Gemma 2 MITRA-E (state-of-the-art for Buddhist language MT)
- **Code/Data:** Parallel dataset, model weights, and benchmark openly available (Hugging Face: buddhist-nlp)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 3. MITRA-zh-eval: Using a Buddhist Chinese Language Evaluation Dataset to Assess Machine Translation and Evaluation Metrics
- **Authors:** Sebastian Nehrdich, Avery Chen, Marcus Bingenheimer, Lu Huang, Rouying Tang, Xiang Wei, Leijie Zhu, Kurt Keutzer
- **Year:** 2025
- **Venue:** NLP4DH 2025 (5th International Conference on Natural Language Processing for Digital Humanities)
- **arXiv:** N/A
- **DOI:** 10.18653/v1/2025.nlp4dh-1.12
- **Religious Traditions:** Buddhism (Chinese Buddhist canon -- Mahayana, Chan, Huayan, Tiantai traditions)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 2,662 bilingual data points from 32 texts; 182 machine-generated translations rated by 5 domain specialists
- **Languages:** Buddhist Chinese, English
- **LLMs Tested:** GPT, Claude, DeepSeek (compared with MITRA domain-specific models)
- **Code/Data:** https://aclanthology.org/2025.nlp4dh-1.12/
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 4. MITRA-zh: An Efficient, Open Machine Translation Solution for Buddhist Chinese
- **Authors:** Sebastian Nehrdich, Marcus Bingenheimer, Justin Brody, Kurt Keutzer
- **Year:** 2023
- **Venue:** NLP4DH 2023 (Joint 3rd International Conference on Natural Language Processing for Digital Humanities and 8th International Workshop on Computational Linguistics for Uralic Languages), pages 266-277, Tokyo, Japan
- **arXiv:** N/A
- **DOI:** N/A (ACL Anthology: 2023.nlp4dh-1.29)
- **Religious Traditions:** Buddhism (Chinese Buddhist canon)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 209,454 bitext pairs (training); 2,300 manually curated bitext pairs (evaluation)
- **Languages:** Buddhist Classical Chinese, English
- **LLMs Tested:** GPT-4, standard MT providers, finetuned domain-specific models
- **Code/Data:** Open-source (Dharmamitra project)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 5. BuddhismEval: Bilingual Evaluation Benchmark for Buddhist Ethics and Reasoning
- **Authors:** Nethmi Muthugala, Deyi Xiong
- **Year:** 2025
- **Venue:** Submitted to NeurIPS 2025 (under review)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Theravada -- Dhammapada, Abhidharma, canonical Pali sources)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** Sinhala MCQ dataset + English MCQ dataset + Dhammapada Parallel Corpus (multi-component)
- **Languages:** Sinhala, English
- **LLMs Tested:** N/A (benchmark designed for LLM evaluation)
- **Code/Data:** https://huggingface.co/datasets/Nethmi14/BuddhismEval
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 6. One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit NLP Tasks
- **Authors:** Sebastian Nehrdich, Oliver Hellwig, Kurt Keutzer
- **Year:** 2024
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2409.13920
- **DOI:** N/A (ACL Anthology: 2024.findings-emnlp.805)
- **Religious Traditions:** Buddhism (Buddhist Sanskrit is primary domain corpus)
- **Paper Type:** Dataset | Framework
- **Dataset Size:** Multitask dataset covering word segmentation, dependency parsing, OCR post-correction (Buddhist Sanskrit texts)
- **Languages:** Sanskrit (classical and Vedic, including Buddhist Sanskrit)
- **LLMs Tested:** ByT5-Sanskrit (byte-level pretrained model)
- **Code/Data:** https://github.com/sebastian-nehrdich/byt5-sanskrit-analyzers ; https://huggingface.co/buddhist-nlp/byt5-sanskrit
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 7. Classification of Buddhist Verses: The Efficacy and Limitations of Transformer-Based Models
- **Authors:** Nikita Neveditsin, Ambuja Salgaonkar, Pawan Lingras, Vijay Mago
- **Year:** 2024
- **Venue:** NLP4DH 2024 (4th International Conference on Natural Language Processing for Digital Humanities), pages 377-385, Miami, USA
- **arXiv:** N/A
- **DOI:** 10.18653/v1/2024.nlp4dh-1.37
- **Religious Traditions:** Buddhism (Theravada -- Therigatha and Theragatha from the Khuddaka Nikaya)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Verses from Therigatha and Theragatha (Buddhist canonical poetry attributed to female and male authors)
- **Languages:** Devanagari (Pali), English
- **LLMs Tested:** Transformer-based models (BERT variants), statistical models
- **Code/Data:** Dataset provided for further study (per paper)
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R4

### 8. Embeddings Models for Buddhist Sanskrit
- **Authors:** Ligeia Lugli, Matej Martinc, Andraz Pelicon, Senja Pollak
- **Year:** 2022
- **Venue:** LREC 2022 (Thirteenth Language Resources and Evaluation Conference), pages 3861-3871, Marseille, France
- **arXiv:** N/A
- **DOI:** N/A (ACL Anthology: 2022.lrec-1.411)
- **Religious Traditions:** Buddhism (Buddhist Sanskrit textual tradition)
- **Paper Type:** Dataset | Framework
- **Dataset Size:** Novel Buddhist Sanskrit corpus + general Sanskrit corpus + word similarity and word analogy evaluation datasets
- **Languages:** Sanskrit (Buddhist Sanskrit)
- **LLMs Tested:** word2vec, fastText, BERT, GPT-2 (with transfer learning)
- **Code/Data:** https://figshare.com/articles/code/Gitlab_repository_of_Embeddings_models_for_Buddhist_Sanskrit/24056319 ; https://huggingface.co/Matej/bert-base-buddhist-sanskrit
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 9. TIB-STC: A Large-Scale Structured Tibetan Benchmark for Low-Resource Language Modeling (Sun-Shine)
- **Authors:** Cheng Huang, Fan Gao, Yutong Liu, Nyima Tashi, Xiangxiang Wang, Thupten Tsering, Ban Ma-bao, Renzeg Duojie, Gadeng Luosang, Rinchen Dongrub, Dorje Tashi, Xiao Feng, Hao Wang, Yongbin Yu
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** 2503.18288
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Tibetan Buddhist texts comprise significant portion of the religion domain)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 11 billion+ tokens across literature, religion, medicine, law, and daily communication
- **Languages:** Tibetan
- **LLMs Tested:** Sun-Shine (LLaMA-3.1 based, evaluated on TLUE Benchmark)
- **Code/Data:** https://github.com/Vicentvankor/sun-shine
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 10. TLUE: A Tibetan Language Understanding Evaluation Benchmark
- **Authors:** Fan Gao, Cheng Huang, Nyima Tashi, Xiangxiang Wang, Thupten Tsering, Ban Ma-bao, Renzeg Duojie, Gadeng Luosang, Rinchen Dongrub, Dorje Tashi, Xiao Feng, Yongbin Yu
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** 2503.12051
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Tibetan Buddhist cultural context; Ti-SafetyBench includes ethics subdomain)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 22,963 evaluation questions (Ti-MMLU: 11,528 MCQs across 67 subjects; Ti-SafetyBench: 11,435 questions across 7 safety categories)
- **Languages:** Tibetan
- **LLMs Tested:** Multiple large language models (most perform below random baseline on Tibetan)
- **Code/Data:** https://github.com/Vicentvankor/TLUE
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 11. Tibetan Language and AI: A Comprehensive Survey of Resources, Methods and Challenges
- **Authors:** (Multiple authors -- survey paper)
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** 2510.19144
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Tibetan Buddhist text tradition is primary corpus source)
- **Paper Type:** Framework (Survey)
- **Dataset Size:** N/A (comprehensive survey cataloging datasets, tools, and benchmarks)
- **Languages:** Tibetan, English
- **LLMs Tested:** Reviews performance of various NLP models and LLMs on Tibetan tasks
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R4

### 12. T-LLaMA: A Tibetan Large Language Model Based on LLaMA2
- **Authors:** (Multiple authors)
- **Year:** 2024
- **Venue:** Complex & Intelligent Systems (Springer)
- **arXiv:** N/A
- **DOI:** 10.1007/s40747-024-01641-7
- **Religious Traditions:** Buddhism (Tibetan language is deeply tied to Buddhist textual tradition)
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** 2.2 billion characters Tibetan corpus
- **Languages:** Tibetan
- **LLMs Tested:** T-LLaMA (7B parameters, LLaMA2-based with LoRA)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R4

### 13. The Use of Large Language Models for Translating Buddhist Texts from Classical Chinese to Modern English: An Analysis and Evaluation with ChatGPT 4, ERNIE Bot 4, and Gemini Advanced
- **Authors:** (Authors from MDPI Religions)
- **Year:** 2024
- **Venue:** Religions (MDPI), Vol. 15, Issue 12, Article 1559
- **arXiv:** N/A
- **DOI:** 10.3390/rel15121559
- **Religious Traditions:** Buddhism (Chinese Buddhist canon -- Indian-Chinese origin text and Chinese-origin texts by Buddhist monks)
- **Paper Type:** Evaluation
- **Dataset Size:** Excerpts from 3 Buddhist texts (1 Indian-Chinese origin, 2 Chinese-origin by Buddhist monks)
- **Languages:** Classical Chinese, English
- **LLMs Tested:** ChatGPT 4, ERNIE Bot 4, Gemini Advanced
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R4

### 14. Optimisation of the Largest Annotated Tibetan Corpus Combining Rule-based, Memory-based, and Deep-learning Methods (ACTib v2.0)
- **Authors:** Christian Faggionato, Marieke Meelen, Nathan Hill (and collaborators)
- **Year:** 2021
- **Venue:** ACM Transactions on Asian and Low-Resource Language Information Processing
- **arXiv:** N/A
- **DOI:** 10.1145/3409488
- **Religious Traditions:** Buddhism (based on Buddhist Digital Resource Center collection -- Kangyur, Tengyur, and other Tibetan Buddhist canonical texts)
- **Paper Type:** Dataset
- **Dataset Size:** 185 million+ tokens (segmented and POS-tagged), 91.99% end-to-end accuracy
- **Languages:** Classical Tibetan
- **LLMs Tested:** N/A (rule-based + memory-based + deep learning annotation pipeline)
- **Code/Data:** https://zenodo.org/records/3951503 ; https://github.com/lothelanor/actib
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R4

### 15. Dharma Setu: Bridging Ancient Buddhist Wisdom and Modern AI Through Multimodal Integration
- **Authors:** Matt Lindsey
- **Year:** 2025
- **Venue:** Contemporary Buddhism (Taylor & Francis)
- **arXiv:** N/A
- **DOI:** 10.1080/14639947.2025.2564003
- **Religious Traditions:** Buddhism (all traditions -- draws on 10 billion tokens from Buddhist Digital Resource Center)
- **Paper Type:** Framework
- **Dataset Size:** 10 billion tokens from BDRC corpus
- **Languages:** Multiple Buddhist canonical languages, English
- **LLMs Tested:** LLM + vector database + graph database architecture
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R4

### 16. Kaku-Ora: Zen Wisdom Diffused -- An AI Oracle Trained on Zen Koans
- **Authors:** (LessWrong community project)
- **Year:** 2025
- **Venue:** LessWrong / HuggingFace Spaces
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Buddhism (Zen -- koan literature and non-koan Zen exchanges)
- **Paper Type:** Dataset
- **Dataset Size:** ~20,000 examples in JSONL format (~5,000 from koan literature, ~15,000 from non-koan Zen exchanges)
- **Languages:** English
- **LLMs Tested:** Diffusion-based language model (fine-tuned)
- **Code/Data:** GitHub (code available); HuggingFace Spaces (model hosted)
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R4

---

## Summary

**Total papers found:** 16

**Breakdown by Paper Type:**
- Benchmark: 4 (DharmaBench, BuddhismEval, TLUE, TIB-STC/Sun-Shine)
- Dataset: 10 (MITRA, MITRA-zh-eval, MITRA-zh, BuddhismEval, ByT5-Sanskrit, Buddhist Verses, Buddhist Sanskrit Embeddings, ACTib, Kaku-Ora, TIB-STC)
- Evaluation: 5 (MITRA-zh-eval, MITRA-zh, Buddhist Verses, LLM Buddhist Translation, TLUE)
- Framework: 4 (MITRA, ByT5-Sanskrit, Dharma Setu, Tibetan AI Survey)

**Breakdown by Buddhist Tradition:**
- Pan-Buddhist (multiple traditions): 4 (MITRA, Dharma Setu, MITRA main, Tibetan AI Survey)
- Theravada: 3 (BuddhismEval, Buddhist Verses, MITRA-zh indirectly)
- Mahayana / Chinese Buddhism: 4 (MITRA-zh-eval, MITRA-zh, LLM Buddhist Translation, TIB-STC partly)
- Vajrayana / Tibetan Buddhism: 5 (DharmaBench, TIB-STC/Sun-Shine, TLUE, T-LLaMA, ACTib)
- Zen: 1 (Kaku-Ora)
- Buddhist Sanskrit tradition: 2 (ByT5-Sanskrit, Buddhist Sanskrit Embeddings)

**Breakdown by Language Coverage:**
- Sanskrit: 4 papers
- Tibetan: 6 papers
- Buddhist Chinese: 4 papers
- Pali: 3 papers
- Sinhala: 1 paper
- English: 10 papers (as target or evaluation language)

**Key Findings:**
1. The Dharmamitra/MITRA project (UC Berkeley) is the single most productive effort, responsible for 4 of 16 papers, covering all four major Buddhist canonical languages.
2. DharmaBench and BuddhismEval represent the two most directly relevant benchmarks for evaluating LLMs on Buddhist knowledge and ethics.
3. Tibetan NLP has seen rapid growth (5+ papers), driven by the TIB-STC/Sun-Shine and TLUE benchmarks.
4. There is a notable gap: no benchmark specifically tests LLM alignment with Buddhist ethical frameworks (Five Precepts, Eightfold Path, Bodhisattva vows) -- BuddhismEval comes closest.
5. Most papers focus on language understanding and translation rather than moral/ethical evaluation through a Buddhist lens.

**Papers excluded (already in vault):**
- Contemplative Artificial Intelligence (arXiv 2504.15125) -- line 643
- The Humanistic Buddhism Corpus (HBC) -- line 456
- Decolonial AI Alignment -- Openness, Visesa-Dharma -- line 444
- AI practical wisdom and compassion -- line 587

**Papers excluded (do not meet inclusion criteria):**
- "A Middle Path for AI Ethics? Some Buddhist Reflections" (Hershock & Mirghafori, 2024) -- pure philosophy, no dataset/benchmark
- "The anthropomorphization of AI and the concept of Buddhist compassion" (Frontiers, 2025) -- framework paper, no dataset
- "SabaiJai: A Buddhist AI Chatbot" (Thammasat Review, 2025) -- mindfulness app, no NLP dataset
- "Sati-AI" -- meditation chatbot project, no formal NLP evaluation paper
- "NORBU" -- Buddhist chatbot, no formal academic evaluation paper with dataset
- "BuddhaBot" (Kyoto University/Bhutan) -- chatbot deployment, no published benchmark dataset
- "Ancient Wisdom, Emerging Tech" (Contemporary Buddhism, 2025) -- education paper, no dataset
- "The Ethics of AI and Robotics: A Buddhist Viewpoint" (Hongladarom) -- book, no dataset

**Implementation Readiness Distribution:**
- HIGH: 10 papers (DharmaBench, MITRA, MITRA-zh-eval, MITRA-zh, BuddhismEval, ByT5-Sanskrit, Buddhist Sanskrit Embeddings, TIB-STC, TLUE, ACTib)
- MEDIUM: 5 papers (Buddhist Verses, Tibetan AI Survey, T-LLaMA, LLM Buddhist Translation, Kaku-Ora)
- LOW: 1 paper (Dharma Setu)
