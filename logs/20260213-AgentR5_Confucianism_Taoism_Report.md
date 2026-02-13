# Agent R5 Report: Confucianism and Taoism/Daoism -- LLM Benchmarks, Datasets, and Evaluation Papers

**Agent:** R5
**Focus:** Confucianism and Taoism/Daoism
**Date:** 2026-02-13
**Search Terms Used:** 12 queries covering Confucius Analects NLP, Chinese moral philosophy LLM, Tao Te Ching NLP, Daodejing text mining, filial piety AI evaluation, Mencius NLP, Confucian ethics AI alignment, Chinese classical text NLP benchmark, Confucian values LLM evaluation, junzi virtue AI, Taoist ethics AI NLP, CoreValue Chinese Values Knowledge Base

---

## Papers Found

### 1. WYWEB: A NLP Evaluation Benchmark for Classical Chinese
- **Authors:** Bo Zhou, Qianglong Chen, Tianyu Wang, Xiaomi Zhong, Yin Zhang
- **Year:** 2023
- **Venue:** Findings of ACL 2023
- **arXiv:** 2305.14150
- **DOI:** 10.18653/v1/2023.findings-acl.204
- **Religious Traditions:** Confucianism, Taoism (benchmark covers classical Chinese texts spanning Confucian, Taoist, and other philosophical sources)
- **Paper Type:** Benchmark
- **Dataset Size:** 9 NLP tasks (sentence classification, sequence labeling, reading comprehension, machine translation) across classical Chinese (wenyanwen) corpora
- **Languages:** Classical Chinese, Modern Chinese
- **LLMs Tested:** Multiple pre-trained language models (all reported struggling with the benchmark)
- **Code/Data:** https://github.com/baudzhou/WYWEB
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R5

**Summary:** WYWEB is the first comprehensive NLP evaluation benchmark specifically for classical Chinese (wenyanwen), the literary language used in Confucian, Taoist, and other classical philosophical texts for thousands of years. It includes 9 tasks including novel tasks for punctuation and named entity recognition to evaluate word separation capability. The benchmark fills a critical gap as existing NLP benchmarks neglected classical Chinese despite its immense cultural and academic significance. Pre-trained models universally struggled with this benchmark, indicating the difficulty of processing texts in the register used by the Confucian Analects, Tao Te Ching, and other philosophical classics.

---

### 2. WenMind: A Comprehensive Benchmark for Evaluating Large Language Models in Chinese Classical Literature and Language Arts
- **Authors:** Jiahuan Cao, Yang Liu, Yongxin Shi, Kai Ding, Lianwen Jin
- **Year:** 2024
- **Venue:** NeurIPS 2024 (Datasets and Benchmarks Track)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (covers Ancient Prose, Ancient Poetry, and Ancient Literary Culture including Confucian and Taoist texts)
- **Paper Type:** Benchmark
- **Dataset Size:** 4,875 question-answer pairs spanning 42 fine-grained tasks, 3 question formats, 2 evaluation scenarios (domain-oriented and capability-oriented)
- **Languages:** Classical Chinese, Modern Chinese
- **LLMs Tested:** 31 LLMs including ERNIE-4.0 (best score: 64.3), general-purpose models and ancient Chinese-specific LLMs
- **Code/Data:** https://github.com/SCUT-DLVCLab/WenMind ; https://huggingface.co/datasets/SCUT-DLVCLab/WenMind
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R5

**Summary:** WenMind is a comprehensive benchmark dedicated to evaluating LLMs in Chinese Classical Literature and Language Arts (CCLLA), covering Ancient Prose, Ancient Poetry, and Ancient Literary Culture. The benchmark's "Ancient Literary Culture" domain specifically tests knowledge of Confucian and Taoist philosophical traditions, literary commentary traditions, and cultural concepts embedded in classical texts. Even the best-performing model (ERNIE-4.0) achieved only 64.3 points, indicating significant room for improvement. This is a high-quality NeurIPS-accepted benchmark with publicly available code and data.

---

### 3. Fuxi: A Benchmark for Evaluating Language Models on Ancient Chinese Text Understanding and Generation
- **Authors:** Shangqing Zhao, Yuhao Zhou, Yupei Ren, Zhe Chen, Chenghao Jia, Fang Zhe, Zhaogaung Long, Shu Liu, Man Lan
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2503.15837
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (evaluates understanding and generation of ancient Chinese texts including Confucian and Taoist philosophical writings)
- **Paper Type:** Benchmark
- **Dataset Size:** 21 diverse tasks covering both comprehension and generation
- **Languages:** Classical Chinese, Modern Chinese
- **LLMs Tested:** State-of-the-art LLMs (specific models not enumerated in abstract)
- **Code/Data:** Benchmark, evaluation toolkit, and baseline results publicly available (repository link not confirmed)
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R5

**Summary:** Fuxi is a benchmark that evaluates both understanding and generation capabilities across 21 tasks for ancient Chinese text processing. It includes novel tasks like poetry composition and couplet completion, with specialized evaluation metrics for classical Chinese text generation combining rule-based verification with fine-tuned LLM evaluators. The benchmark reveals significant performance gaps between understanding and generation tasks, with models struggling particularly in generation tasks that require deep cultural knowledge and adherence to classical formats rooted in Confucian and Taoist literary traditions.

---

### 4. AC-EVAL: Evaluating Ancient Chinese Language Understanding in Large Language Models
- **Authors:** Yuting Wei, Yuanxing Xu, Xinru Wei, Simin Yang, Yangfu Zhu, Yuqing Li, Di Liu, Bin Wu
- **Year:** 2024
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2403.06574
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (explicitly includes philosophy as one of the evaluation domains)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 13 tasks across 3 difficulty levels covering historical facts, geography, social customs, art, philosophy, classical poetry and prose
- **Languages:** Classical Chinese, Modern Chinese
- **LLMs Tested:** Top-performing English and Chinese LLMs; ERNIE-Bot 4.0 and GLM-4 achieved >70% accuracy
- **Code/Data:** https://github.com/yuting-wei/AC-EVAL
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R5

**Summary:** AC-EVAL explicitly includes philosophy (encompassing Confucian and Taoist philosophical traditions) as one of its evaluation domains. The benchmark is structured across three difficulty levels -- general historical knowledge, short text understanding, and long text comprehension -- and reveals significant divergence in LLM performance between modern Chinese and ancient Chinese. Chinese LLMs consistently outperform English LLMs on ancient Chinese tasks. The benchmark is well-documented with a public GitHub repository.

---

### 5. ACLUE: Can Large Language Model Comprehend Ancient Chinese? A Preliminary Test
- **Authors:** Yixuan Zhang, Haonan Li
- **Year:** 2023
- **Venue:** RANLP 2023 (ALP Workshop)
- **arXiv:** 2310.09550
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (covers texts from Xia dynasty to Ming dynasty, encompassing core Confucian and Taoist canonical works)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 15 tasks spanning phonetic, lexical, syntactic, semantic, inference, and knowledge domains; multiple-choice format
- **Languages:** Classical Chinese
- **LLMs Tested:** 8 state-of-the-art LLMs including ChatGLM2 (37.45% best), ChatGPT, BLOOMZ-7B
- **Code/Data:** https://github.com/isen-zhang/ACLUE ; https://huggingface.co/datasets/tyouisen/aclue
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R5

**Summary:** ACLUE (Ancient Chinese Language Understanding Evaluation) is a benchmark with 15 tasks covering 5 categories (Vocabulary, Syntax, Semantics, Reasoning, Knowledge) derived from texts spanning from the Xia Dynasty (2070 BCE) to the Ming Dynasty (1368 CE). This range encompasses the core periods of Confucian and Taoist text composition and commentary. The benchmark is integrated into EleutherAI's lm-evaluation-harness, has a public leaderboard, and both code and data are fully available, making it highly implementation-ready.

---

### 6. AncientBench: Towards Comprehensive Evaluation on Excavated and Transmitted Chinese Corpora
- **Authors:** Zhihan Zhou, Daqian Shi, Rui Song, Lida Shi, Xiaolei Diao, Hao Xu
- **Year:** 2025
- **Venue:** EMNLP 2025
- **arXiv:** 2512.17756
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (evaluates comprehension of transmitted Chinese corpora which include canonical Confucian and Taoist texts)
- **Paper Type:** Benchmark
- **Dataset Size:** 10 tasks across 4 dimensions (glyph, pronunciation, meaning, contextual comprehension)
- **Languages:** Classical Chinese (including excavated documents)
- **LLMs Tested:** Current best-performing LLMs (compared against human performance)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R5

**Summary:** AncientBench is novel in introducing excavated documents (e.g., oracle bone inscriptions, bamboo strips) alongside transmitted texts into NLP evaluation, providing four dimensions of ancient character comprehension. The transmitted documents portion includes canonical Confucian and Taoist texts. Both LLMs and human comprehension were evaluated and compared, providing important baselines for understanding how well current models process the linguistic substrate of Chinese philosophical traditions.

---

### 7. WenyanGPT: A Large Language Model for Classical Chinese Tasks (with WenyanBENCH)
- **Authors:** Xinyu Yao, Mengdi Wang, Bo Chen, Xiaobing Zhao
- **Year:** 2025
- **Venue:** IJCAI 2025
- **arXiv:** 2504.20609
- **DOI:** N/A
- **Religious Traditions:** Confucianism, Taoism (trained on and evaluated against classical Chinese texts from Confucian, Taoist, and other philosophical traditions)
- **Paper Type:** Benchmark | Dataset
- **Dataset Size:** WenyanBENCH: 6 tasks (punctuation with 14 mark types, POS tagging with 17 categories, NER with 4 categories, translation, word explanation, reverse dictionary)
- **Languages:** Classical Chinese, Modern Chinese
- **LLMs Tested:** WenyanGPT (their model, based on LLaMA3-8B-Chinese), Qwen2.5-7B-Instruct, Baichuan2-7B-Chat, GLM-4-9B-Chat, Meta-Llama-3-8B-Instruct, GPT-4o, DeepSeek-V3
- **Code/Data:** Training data, instruction fine-tuning data, and WenyanBENCH publicly available
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R5

**Summary:** WenyanGPT is a specialized LLM for classical Chinese built via continued pre-training and instruction fine-tuning of LLaMA3-8B-Chinese. The accompanying WenyanBENCH provides a standardized evaluation benchmark for 6 classical Chinese NLP tasks. WenyanGPT significantly outperforms all tested general-purpose LLMs including GPT-4o and DeepSeek-V3 on classical Chinese tasks. The paper and benchmark are accepted at IJCAI 2025 and all resources are publicly available.

---

### 8. Dissecting The Analects: An NLP-based Exploration of Semantic Similarities and Differences Across English Translations
- **Authors:** Liwei Yang, Guijun Zhou
- **Year:** 2024
- **Venue:** Humanities and Social Sciences Communications (Nature)
- **arXiv:** N/A
- **DOI:** 10.1057/s41599-023-02355-w
- **Religious Traditions:** Confucianism (directly analyzes the Confucian Analects)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Corpus from 5 complete English translations of The Analects with sentence-level semantic similarity annotations
- **Languages:** English (translations of Classical Chinese)
- **LLMs Tested:** N/A (uses Word2Vec, GloVe, BERT for analysis rather than evaluation)
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R5

**Summary:** This paper builds a parallel corpus from five major English translations of the Confucian Analects and quantifies semantic similarity at the sentence level using Word2Vec, GloVe, and BERT. Sentence pairs are categorized into "Abnormal," "High-similarity," and "Low-similarity" groups. While not a direct LLM evaluation benchmark, this work creates a structured NLP dataset from the core Confucian text that could be adapted for evaluating LLM understanding of Confucian concepts across different translation interpretations. The parallel translation corpus enables studying how NLP models handle the semantic nuances of key Confucian terms (ren, li, junzi, etc.) across translators.

---

### 9. Quantitative Analysis of Semantic Boundaries in Four Ancient Chinese Philosophies
- **Authors:** Mengcheng Wu, Dongbo Wang
- **Year:** 2025
- **Venue:** npj Heritage Science
- **arXiv:** N/A
- **DOI:** 10.1038/s40494-025-01893-7
- **Religious Traditions:** Confucianism, Taoism (directly analyzes Confucianism and Daoism alongside Legalism and Mohism)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Corpus of core texts from four Pre-Qin philosophical schools (Confucianism, Daoism, Legalism, Mohism) with extracted key vocabularies and semantic spaces
- **Languages:** Classical Chinese
- **LLMs Tested:** N/A (uses word vector models, dimensionality reduction, and clustering for analysis)
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R5

**Summary:** This study applies computational NLP techniques (word vector models, dimensionality reduction, clustering, boundary detection) to construct and compare the semantic spaces of Confucianism, Daoism, Legalism, and Mohism. Key findings include that Daoism and Legalism are most semantically distinct, while Confucianism and Mohism show considerable convergence. The constructed semantic spaces and identified transitional vocabularies provide a quantitative foundation for evaluating how well LLMs can distinguish between Chinese philosophical traditions. This work explicitly creates computational representations of Confucian and Taoist conceptual systems.

---

### 10. ClaOnto: Linking Past Insights with Contemporary Understanding -- An Ontological and Knowledge Graph Approach to the Transmission of Ancient Chinese Classics
- **Authors:** Yu Cui, Shenjun Yao, Jianping Wu, Muhan Lv
- **Year:** 2024
- **Venue:** Heritage Science (Springer)
- **arXiv:** N/A
- **DOI:** 10.1186/s40494-024-01504-x
- **Religious Traditions:** Taoism (uses the Tao Te Ching as primary case study)
- **Paper Type:** Dataset | Framework
- **Dataset Size:** ClaOnto ontology with 3 modules (Basic Information, Transmission Information, Evaluation Information); knowledge graph demonstrated on Tao Te Ching
- **Languages:** Classical Chinese, multiple languages (tracks translations)
- **LLMs Tested:** N/A
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R5

**Summary:** ClaOnto is an ontology designed for ancient Chinese classics that captures text versions, their interrelations, contents, related individuals, locations, periods, and languages. The primary case study uses the Tao Te Ching (Daodejing), demonstrating a workflow for building a knowledge graph that traces the transmission history of this foundational Taoist text. While not a direct LLM benchmark, the structured ontology and knowledge graph provide a foundation for building Taoist knowledge QA systems and evaluating LLM understanding of Taoist textual transmission.

---

## Summary

**Total papers found:** 10

**By religious tradition:**
- Confucianism: 9 papers (all except ClaOnto which is Taoism-focused)
- Taoism/Daoism: 6 papers (WYWEB, WenMind, Fuxi, AC-EVAL, Semantic Boundaries, ClaOnto)
- Both traditions covered together: 5 papers (WYWEB, WenMind, Fuxi, AC-EVAL, Semantic Boundaries)

**By paper type:**
- Benchmark: 7 (WYWEB, WenMind, Fuxi, AC-EVAL, ACLUE, AncientBench, WenyanBENCH)
- Dataset: 5 (WenyanBENCH, Dissecting Analects, Semantic Boundaries, ClaOnto, Fuxi)
- Evaluation: 3 (AC-EVAL, ACLUE, Dissecting Analects)
- Framework: 1 (ClaOnto)

**By implementation readiness:**
- HIGH: 5 (WYWEB, WenMind, AC-EVAL, ACLUE, WenyanGPT)
- MEDIUM: 2 (Fuxi, AncientBench)
- LOW: 3 (Dissecting Analects, Semantic Boundaries, ClaOnto)

**Key observations:**

1. **No dedicated Confucian/Taoist LLM ethics benchmark exists.** Unlike Islamic NLP (which has multiple Quran/Hadith QA benchmarks) or Christian NLP (which has Biblical QA datasets), there is no standalone benchmark that specifically evaluates LLM alignment with Confucian ren/yi/li or Taoist wu wei principles. The closest vault entry is CMoralEval (already in vault), which incorporates five Confucian-inspired moral principles.

2. **Classical Chinese benchmarks serve as proxies.** The 7 benchmarks found (WYWEB, WenMind, Fuxi, AC-EVAL, ACLUE, AncientBench, WenyanBENCH) evaluate LLMs on the classical Chinese language that carries Confucian and Taoist philosophical content, but they test linguistic competence rather than philosophical understanding per se.

3. **The gap is significant.** Given that Confucianism and Taoism are among the world's major philosophical/religious traditions with billions of adherents, the absence of dedicated LLM evaluation benchmarks for these traditions represents a notable gap in AI fairness and cultural inclusivity research.

4. **Existing vault papers that partially cover this space:** CMoralEval (Confucian five principles), CValues, Edu-Values, STORAL-ZH (Confucian moral stories), Flames, How AI Trained on the Confucian Analects Can Solve Ethical Dilemmas, and Can Artificial Intelligence Lead Us to Genuine Virtue? A Confucian Perspective.

5. **Papers excluded from this report (already in vault):** CoreValue Chinese Values Knowledge Base, Can an AI-carebot be filial? (Confucian ethics), The Ethics of Digital Ghosts (Confucian/Mohist/Zhuangist), Contemplative Artificial Intelligence, CCD-Bench, and 8 other related papers.

---

*Report generated by Agent R5 on 2026-02-13*
