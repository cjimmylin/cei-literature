# Agent R2: Christianity & Judaism -- Religious Values LLM Benchmark Search Report

**Date:** 2026-02-13
**Agent:** R2
**Focus:** Christianity and Judaism NLP/AI benchmarks, datasets, and evaluation papers
**Search Terms Used:** 12 queries (Bible QA, biblical NLP, BibleNLP, theological reasoning LLM, Torah NLP, Talmud QA AI, Halakhic reasoning NLP, Sefaria NLP, Christian ethics LLM alignment, antisemitism detection NLP, catechism LLM evaluation Catholic, religious text NLP Bible Hebrew)

---

## Papers Found

### 1. Uncovering Theological and Ethical Biases in LLMs: An Integrated Hermeneutical Approach Employing Texts from the Hebrew Bible
- **Authors:** A. G. Elrod
- **Year:** 2024
- **Venue:** HIPHIL Novum, 9(1), 2--45
- **arXiv:** N/A
- **DOI:** 10.7146/hn.v9i1.143407
- **Religious Traditions:** Christianity, Judaism
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Structured prompts across 5 LLMs (10 Commandments generation + Book of Jonah continuation tasks)
- **Languages:** English, Hebrew (source texts)
- **LLMs Tested:** GPT-4 Turbo, Claude 2, PaLM 2, Llama 2 70B, Zephyr 7B
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Uses creative text generation tasks based on the Ten Commandments (Exodus 20) and the Book of Jonah to probe theological and ethical biases. Finds a prevalent progressive bias across all models, aligning with contemporary socio-political and environmental concerns. Combines qualitative hermeneutical analysis with quantitative textual analysis.

---

### 2. Large Language Models and Biblical Hebrew: Limitations, Pitfalls, Opportunities
- **Authors:** Camil Staps
- **Year:** 2024
- **Venue:** HIPHIL Novum, 9(1), 46--55
- **arXiv:** N/A
- **DOI:** 10.7146/hn.v9i1.144177
- **Religious Traditions:** Judaism, Christianity
- **Paper Type:** Evaluation
- **Dataset Size:** N/A (evaluation study using BHSA dataset and Text-Fabric)
- **Languages:** Biblical Hebrew, English
- **LLMs Tested:** GPT (OpenAI models)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Critically evaluates whether LLMs can be useful for Biblical Hebrew scholarship. Exposes fundamental issues with GPT-based methods for this domain while identifying potential forward paths with machine learning methods for specific linguistic tasks.

---

### 3. Nothing New Under the Sun? The Study of Biblical Hebrew in the Era of Generative Pre-trained AI
- **Authors:** A. G. Elrod
- **Year:** 2023
- **Venue:** HIPHIL Novum, 8(2), 1--32
- **arXiv:** N/A
- **DOI:** N/A (HIPHIL Novum journal)
- **Religious Traditions:** Judaism, Christianity
- **Paper Type:** Evaluation
- **Dataset Size:** N/A (experiments using ETCBC BHSA dataset and Text-Fabric Python libraries)
- **Languages:** Biblical Hebrew, English
- **LLMs Tested:** OpenAI GPT
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Investigates GPT's capabilities in biblical studies across three categories: knowledge retrieval/language understanding, generative modeling/creative problem solving, and command interpretation/query parsing. Demonstrates both limitations and proficiencies for Biblical Hebrew NLP.

---

### 4. Religion, Theology, and Philosophical Skills of LLM-Powered Chatbots
- **Authors:** Marcin Trepczynski
- **Year:** 2023
- **Venue:** Disputatio philosophica: International Journal on Philosophy and Religion, 25(1), 19--36
- **arXiv:** N/A
- **DOI:** 10.32701/dp.25.1.2
- **Religious Traditions:** Christianity (Catholic, Orthodox, Protestant theology)
- **Paper Type:** Evaluation | Benchmark
- **Dataset Size:** Structured theological evaluation tasks based on 3 source types
- **Languages:** English
- **LLMs Tested:** ChatGPT (GPT-4), Bing, Bard, Llama 2
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Uses theology and religion as evaluation domains for LLM philosophical skills. Tests chatbots on: (1) the four senses of Scripture (medieval hermeneutics), (2) abstract theological statements, (3) logical formulas derived from religious texts. Provides a benchmark framework for rating and comparing interpretive, deductive reasoning, and ontological skills.

---

### 5. AI as a Rational Theologian: A Comprehensive Skills Assessment
- **Authors:** Marcin Trepczynski
- **Year:** 2025
- **Venue:** Wydawnictwa Uniwersytetu Warszawskiego (Warsaw University Press), monograph
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (systematic theology, rational theology)
- **Paper Type:** Evaluation
- **Dataset Size:** Comprehensive structured theological skills assessment
- **Languages:** English
- **LLMs Tested:** ChatGPT (GPT-4o, GPT-o1-mini), Gemini 1.5
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Extended study (2023--2024) showing that leading chatbots possess core skills of a rational theologian. Finds surprisingly high performance on theological skills, with caveats about hallucination risks especially for specific quotations.

---

### 6. The Gospel Coalition AI Christian Benchmark: Evaluating 7 Top LLMs for Theological Reliability
- **Authors:** Casey Sapp, Kyle Horne, Ken Churchill, Andrew Clark, Andrew Noble, Peter Williams, Mary Hannah, Gavin Ortlund, Hans Madueme, Uche Anizor, Nadya Williams, Michael Kruger, Dan Doriani (The Gospel Coalition)
- **Year:** 2025
- **Venue:** The Gospel Coalition (industry report)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (orthodox/Nicene Creed alignment)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 7 theological questions x 7 LLMs, graded by 7 theologians
- **Languages:** English
- **LLMs Tested:** DeepSeek R1, Perplexity, Grok 4, Claude 4 Sonnet, Llama 3.7, Gemini 2.5 Flash, GPT-4o
- **Code/Data:** https://www.thegospelcoalition.org/ai-christian-benchmark/
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Seven orthodox theologians graded seven LLMs on responses to the most-Googled religious questions. DeepSeek R1 ranked highest for theological reliability; Llama 3.7 performed worst. Evaluates alignment with Nicene Creed doctrines.

---

### 7. Flourishing AI Christian (FAI-C) Benchmark
- **Authors:** Gloo (technology platform for faith ecosystem)
- **Year:** 2025
- **Venue:** Gloo / Industry benchmark (peer-review paper forthcoming early 2026)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (Christian worldview, biblically grounded)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 807 curated questions across 7 dimensions of human flourishing
- **Languages:** English
- **LLMs Tested:** Qwen3 235B, GPT OSS 120B, GPT-5.1, GPT-5, o3, DeepSeek-R1-0528, GPT-5.2 (and many more)
- **Code/Data:** https://gloo.com/flourishing-hub/research
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Evaluates LLMs on Christian worldview alignment across Character, Relationships, Happiness, Meaning, Health, Finances, and Faith. Average score 61/100. Faith dimension scores lowest (48 avg). Models default to generic spirituality over theological specificity. 807 questions evaluated by specialized Christian reasoning judge personas.

---

### 8. FaithBench: AI Benchmark for Christian Theology
- **Authors:** Unknown (independent research initiative; open to academic/seminary contributions)
- **Year:** 2025
- **Venue:** FaithBench.com (independent benchmark)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (Reformed, Catholic, Orthodox, Evangelical)
- **Paper Type:** Benchmark
- **Dataset Size:** 300+ test cases across 6 dimensions, 4 difficulty tiers
- **Languages:** English (with original language components: Hebrew, Greek)
- **LLMs Tested:** Multiple (leaderboard-based)
- **Code/Data:** https://faithbench.com/
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: First rigorous peer-review-quality benchmark for AI on Christian theology, apologetics, and biblical scholarship. Six evaluation dimensions: Biblical Exegesis, Hermeneutics, Systematic Theology, Biblical Canon, Church History, and a sixth dimension. Expert-level questions use GPQA-style multi-hop reasoning. Anti-gaming design with held-out test cases.

---

### 9. CatholicBench
- **Authors:** Unknown (independent initiative)
- **Year:** 2025
- **Venue:** CatholicBench.com (independent benchmark)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (Roman Catholic)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** N/A (scored out of 5 per evaluation)
- **Languages:** English
- **LLMs Tested:** Multiple (comparative evaluations on website)
- **Code/Data:** https://www.catholicbench.com/
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Tests AI models on Catholic theological competence at the intersection of rigid dogmatic logic and nuanced pastoral care. Evaluates across Moral Theology, Bioethics, Sacraments, Canon Law, and History/Bias. Measures Pastoral Charity (empathy with truth) and Historical Accuracy (avoiding anti-Catholic tropes).

---

### 10. Generating Hate: Anti-Jewish and Anti-Israel Bias in Leading Large Language Models
- **Authors:** ADL Center for Technology and Society (Daniel Kelley, interim head)
- **Year:** 2025
- **Venue:** Anti-Defamation League (ADL) Report
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** 8,600 queries per model, 34,400 total responses across 6 antisemitism categories
- **Languages:** English
- **LLMs Tested:** GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta)
- **Code/Data:** https://www.adl.org/resources/report/generating-hate-anti-jewish-and-anti-israel-bias-leading-large-language-models
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Most comprehensive evaluation to date of anti-Jewish and anti-Israel bias in major LLMs. Tests across 6 categories: bias against Jews, bias against Israel, Gaza/Hamas war, antisemitic conspiracy theories, Holocaust conspiracy theories, and general antisemitism. All 4 LLMs showed concerning answers; Meta's Llama performed worst.

---

### 11. Evaluating Large Language Models for Detecting Antisemitism
- **Authors:** Jay Patel, Hrudayangam Mehta, Jeremy Blackburn
- **Year:** 2025
- **Venue:** EMNLP 2025 (arXiv preprint)
- **arXiv:** 2509.18293
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Evaluation | Benchmark
- **Dataset Size:** Uses Jikeli et al. antisemitism datasets (6,941+ tweets)
- **Languages:** English
- **LLMs Tested:** Llama 3.1 70B and 7 other open-source LLMs, GPT-3.5 (fine-tuned baseline)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Evaluates 8 open-source LLMs on antisemitism detection using in-context IHRA definition. Proposes Guided-CoT (chain-of-thought) prompting that increases performance and reduces refusals. Llama 3.1 70B outperforms fine-tuned GPT-3.5.

---

### 12. Antisemitic Messages? A Guide to High-Quality Annotation and a Labeled Dataset of Tweets
- **Authors:** Gunther Jikeli, Sameer Karali, Daniel Miehling, Katharina Soemer
- **Year:** 2023
- **Venue:** arXiv preprint (Indiana University ISCA)
- **arXiv:** 2304.14599
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Dataset
- **Dataset Size:** 6,941 tweets (Version 1); expanded to 11,311 tweets (Version 3, 1,953 antisemitic)
- **Languages:** English
- **LLMs Tested:** N/A (dataset for downstream ML use)
- **Code/Data:** https://zenodo.org/records/7932888
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: First large-scale, consistently labeled dataset for antisemitism detection based on IHRA definition. Annotators forced to specify which part of the definition applies. 18% of tweets meet IHRA antisemitism criteria. Dataset on Zenodo; used as benchmark by subsequent antisemitism detection studies.

---

### 13. "Subverting the Jewtocracy": Online Antisemitism Detection Using Multimodal Deep Learning
- **Authors:** Mohit Chandra, Dheeraj Pailla, Himanshu Bhatia, Aadilmehdi Sanchawala, Manish Gupta, Manish Shrivastava, Ponnurangam Kumaraguru
- **Year:** 2021
- **Venue:** ACM Web Science Conference 2021
- **arXiv:** 2104.05947
- **DOI:** 10.1145/3447535.3462502
- **Religious Traditions:** Judaism
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 3,102 tweets (Twitter) + 3,509 posts (Gab) = 6,611 posts with binary + multiclass antisemitism labels
- **Languages:** English
- **LLMs Tested:** N/A (multimodal deep learning system)
- **Code/Data:** https://github.com/mohit3011/Online-Antisemitism-Detection-Using-MultimodalDeep-Learning
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: First multimodal benchmark for automated antisemitism detection combining text and images. Two labeled datasets from Twitter and Gab. Multi-class antisemitism categorization system. Code and labeled data available on GitHub.

---

### 14. Annotating Antisemitic Online Content: Towards an Applicable Definition of Antisemitism
- **Authors:** Gunther Jikeli, Damir Cavar, Daniel Miehling
- **Year:** 2019
- **Venue:** arXiv preprint
- **arXiv:** 1910.01214
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Dataset | Framework
- **Dataset Size:** Random sample from Twitter public data
- **Languages:** English
- **LLMs Tested:** N/A
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Foundational paper establishing annotation methodology for antisemitism detection based on the IHRA definition. Shows that >10% of Twitter conversations about Jews/Israel are antisemitic. Establishes the framework used by subsequent antisemitism NLP datasets.

---

### 15. Detecting Anti-Semitic Hate Speech using Transformer-based Large Language Models
- **Authors:** Dengyi Liu, Minghao Wang, Andrew G. Catlin
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** 2405.03794
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Evaluation
- **Dataset Size:** ~10,000 posts retrieved via Twitter API, 3,000 labeled
- **Languages:** English
- **LLMs Tested:** BERT, DistilBERT, RoBERTa, LLaMA-2 (with LoRA fine-tuning)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Develops a new data labeling technique for anti-Semitic hate speech and evaluates transformer-based models including LLaMA-2 with LoRA fine-tuning. Compares traditional ML approaches with transformer methods for this specific hate speech domain.

---

### 16. Using LLMs to Discover Emerging Coded Antisemitic Hate-Speech in Extremist Social Media
- **Authors:** Dhanush Kikkisetti, Raza Ul Mustafa, Wendy Melillo, Roberto Corizzo, Zois Boukouvalas, Jeff Gill, Nathalie Japkowicz
- **Year:** 2024
- **Venue:** arXiv preprint (American University)
- **arXiv:** 2401.10841
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Evaluation | Framework
- **Dataset Size:** Extremist social media posts (Gab, Telegram)
- **Languages:** English
- **LLMs Tested:** LLMs used for coded language detection (specific models in paper)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Proposes methodology for detecting emerging coded hate terminology in antisemitic online discourse using LLMs. Addresses the challenge of coded language that creates in-group belonging while evading detection. Tests on extremist platforms.

---

### 17. Monitoring the Evolution of Antisemitic Discourse on Extremist Social Media Using BERT
- **Authors:** Raza Ul Mustafa, Nathalie Japkowicz
- **Year:** 2024
- **Venue:** arXiv preprint (American University)
- **arXiv:** 2403.05548
- **DOI:** N/A
- **Religious Traditions:** Judaism
- **Paper Type:** Evaluation
- **Dataset Size:** Extremist social media posts over time
- **Languages:** English
- **LLMs Tested:** BERT (unsupervised online ML approach using LLMs for contextual similarity)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Automated method to extract antisemitic themes and terminology from extremist social media and capture their evolution over time. Uses unsupervised online machine learning with BERT for contextual similarity assessment.

---

### 18. The eBible Corpus: Data and Model Benchmarks for Bible Translation for Low-Resource Languages
- **Authors:** Vesa Akerman, David Baines, Damien Daspit, Ulf Hermjakob, Taeho Jang, Colin Leong, Michael Martin, Joel Mathew, Jonathan Robie, Marcus Schwarting
- **Year:** 2023
- **Venue:** arXiv preprint
- **arXiv:** 2304.09919
- **DOI:** N/A
- **Religious Traditions:** Christianity (Bible translation)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 1,009 Bible translations in 833 languages across 75 language families
- **Languages:** 833 languages (massively multilingual)
- **LLMs Tested:** NLLB (No Language Left Behind) NMT models
- **Code/Data:** https://huggingface.co/datasets/bible-nlp/biblenlp-corpus / https://github.com/BibleNLP/ebible
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Largest standardized Bible corpus for NLP, with 1,009 translations aligned by verse. Introduces model performance benchmarks built on NLLB neural machine translation models. Designed primarily for low-resource language translation but provides a foundation for any Bible-text NLP task.

---

### 19. Targum: A Multilingual New Testament Translation Corpus
- **Authors:** Maciej Rapacz, Aleksander Smywinski-Pohl
- **Year:** 2026
- **Venue:** arXiv preprint
- **arXiv:** 2602.09724
- **DOI:** N/A
- **Religious Traditions:** Christianity (New Testament)
- **Paper Type:** Dataset
- **Dataset Size:** 657 New Testament translations (352 unique) across 5 languages with deep coverage
- **Languages:** English (208 unique), French (41), Italian (18), Polish (30), Spanish (55)
- **LLMs Tested:** N/A (corpus resource)
- **Code/Data:** Code and public-domain subset to be released; copyrighted texts available upon request
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Focuses on depth of translation within each language (multiple translations per language) rather than breadth across languages. Manually verified metadata with publication history for each translation. Addresses a gap in existing biblical corpora for intra-language translation comparison and analysis.

---

### 20. Adapting LLMs to Hebrew: Unveiling DictaLM 2.0 with Enhanced Vocabulary and Instruction Capabilities
- **Authors:** Shaltiel Shmidman, Avi Shmidman, Amir DN Cohen, Moshe Koppel
- **Year:** 2024
- **Venue:** arXiv preprint
- **arXiv:** 2407.07080
- **DOI:** N/A
- **Religious Traditions:** Judaism (Hebrew language infrastructure relevant to Jewish texts)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** ~200 billion tokens in Hebrew and English; new Hebrew NLP benchmark suite
- **Languages:** Hebrew, English
- **LLMs Tested:** DictaLM 2.0, DictaLM 2.0-Instruct (Mistral-based), compared against other Hebrew LLMs
- **Code/Data:** https://huggingface.co/dicta-il/dictalm2.0
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Introduces Hebrew LLM benchmark suite covering QA, Sentiment Analysis, Winograd Schema Challenge, Translation, and Summarization. While not exclusively religious, this benchmark infrastructure is essential for evaluating LLMs on Jewish/Hebrew religious texts. DictaLM 2.0 sets new state-of-the-art for Hebrew NLP.

---

### 21. Religious Bias Landscape in Language and Text-to-Image Models: Analysis, Detection, and Debiasing Strategies
- **Authors:** Ajwad Abrar, Nafisa Tabassum Oeshy, Mohsinul Kabir, Sophia Ananiadou
- **Year:** 2025
- **Venue:** AI & Society (Springer); arXiv preprint
- **arXiv:** 2501.08441
- **DOI:** 10.1007/s00146-025-02721-z
- **Religious Traditions:** Christianity, Judaism, Islam, Hinduism, Buddhism
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** ~400 unique naturally occurring prompts across multiple task types
- **Languages:** English
- **LLMs Tested:** BERT, RoBERTa, ALBERT, DistilBERT, GPT-2, Llama-3, Mixtral-8x7B, Vicuna-13B, GPT-3.5, GPT-4, DALL-E 3
- **Code/Data:** https://github.com/ajwad-abrar/Religious-Bias
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: Systematically investigates religious bias across language models and text-to-image models using mask filling, prompt completion, and image generation tasks. Examines how religious bias intersects with gender, age, and nationality. Explores debiasing techniques. Covers Christianity and Judaism among five major world religions.

---

### 22. Sometimes the Model doth Preach: Quantifying Religious Bias in Open LLMs through Demographic Analysis in Asian Nations
- **Authors:** Hari Shankar et al. (5 authors total)
- **Year:** 2025
- **Venue:** arXiv preprint
- **arXiv:** 2503.07510
- **DOI:** N/A
- **Religious Traditions:** Christianity, Judaism, Islam, Hinduism, Buddhism
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Surveys from multiple Asian countries
- **Languages:** English
- **LLMs Tested:** Llama, Mistral (and other open LLMs)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Evaluates open LLMs on religious tolerance and identity surveys, revealing that most models match a single homogeneous profile that varies across countries. Raises concerns about LLMs promoting hegemonic worldviews and undermining religious minority perspectives. Proposes novel quantitative analysis methodology.

---

### 23. Religion and Racial Bias in Artificial Intelligence Large Language Models
- **Authors:** Joshua C. Tom, Todd W. Ferguson, Brandon C. Martinez
- **Year:** 2025
- **Venue:** Socius: Sociological Research for a Dynamic World (SAGE)
- **arXiv:** N/A
- **DOI:** 10.1177/23780231251377210
- **Religious Traditions:** Christianity (Evangelical Protestant, Catholic, Mainline Protestant), Judaism
- **Paper Type:** Bias Study
- **Dataset Size:** 175 synthetically generated sermons (combinations of race x religious tradition)
- **Languages:** English
- **LLMs Tested:** GPT-4, GPT-4o, Gemini, Claude 3 Opus, Llama 4
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Examines implicit assumptions about religious identities by prompting LLMs to generate sermons with different racial and denominational contexts. Finds Evangelical Protestant sermons had easier readability while Jewish rabbinical texts had higher difficulty. No significant racial readability differences, but specifying any race increased difficulty.

---

### 24. Cognitive Bias in Generative AI Influences Religious Education
- **Authors:** Zhang, Song, Liu
- **Year:** 2025
- **Venue:** Scientific Reports (Nature)
- **arXiv:** N/A
- **DOI:** 10.1038/s41598-025-99121-6
- **Religious Traditions:** Christianity, Judaism, Islam, Buddhism, Hinduism (multi-religion)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Pre/post-interaction experimental evaluations
- **Languages:** English
- **LLMs Tested:** Generative AI systems (specific models in paper)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R2

Summary: Experimental study showing that generative AI amplifies cognitive biases (selection, confirmation, measurement) in religious education contexts. Reveals AI acts as double-edged sword: enhancing personalized learning while risking prejudice reinforcement. Calls for ethical guidelines for AI deployment in religious contexts.

---

### 25. Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions
- **Authors:** Farah Atif et al.
- **Year:** 2025
- **Venue:** AAAI/ACM AIES 2025; arXiv preprint
- **arXiv:** 2508.08287
- **DOI:** N/A
- **Religious Traditions:** Islam (primary focus via FiqhQA), with framework applicable to Christianity, Judaism
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 960 manually curated questions (FiqhQA benchmark)
- **Languages:** Arabic, English
- **LLMs Tested:** GPT-4o, Gemini, Fanar, and others
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R2

Summary: While primarily focused on Islamic jurisprudence (FiqhQA benchmark), the paper's methodology for evaluating LLM reliability and abstention behavior on religious questions is directly transferable to Christian and Jewish contexts. GPT-4o leads accuracy; Gemini/Fanar show better abstention behavior. All models drop in Arabic.

---

---

## Summary

**Total papers found:** 25

**Breakdown by religious tradition:**
- Christianity-focused: 10 (papers 1, 3, 4, 5, 6, 7, 8, 9, 18, 19)
- Judaism-focused: 8 (papers 10, 11, 12, 13, 14, 15, 16, 17)
- Both Christianity and Judaism: 5 (papers 1, 2, 21, 22, 23)
- Multi-religion including Christianity/Judaism: 3 (papers 21, 22, 24)
- Framework transferable: 1 (paper 25)

**Breakdown by paper type:**
- Benchmarks: 8 (papers 6, 7, 8, 9, 11, 13, 18, 25)
- Datasets: 6 (papers 12, 13, 14, 18, 19, 20)
- Evaluations: 14 (papers 1, 2, 3, 4, 5, 6, 7, 10, 11, 15, 17, 20, 24, 25)
- Bias Studies: 7 (papers 1, 10, 21, 22, 23, 24, 16)
- Frameworks: 2 (papers 14, 16)

**Implementation readiness:**
- HIGH: 12 papers
- MEDIUM: 13 papers

**Key gaps identified:**
1. **No dedicated Jewish theology QA benchmark** exists comparable to Christian ones (FaithBench, CatholicBench, FAI-C). Talmudic and Torah-based LLM evaluation is an open research area.
2. **No Halakhic reasoning NLP dataset** was found despite searching. Jewish legal reasoning evaluation for LLMs remains unaddressed.
3. **Sefaria data** (massive structured Jewish text corpus) has not been formally packaged as an LLM evaluation benchmark, despite being used in NLP projects.
4. **Antisemitism detection** is comparatively well-developed with multiple datasets and evaluation papers.
5. **Christian theology benchmarks** are emerging rapidly (FaithBench, CatholicBench, FAI-C, TGC Benchmark) but are largely industry-driven rather than academic peer-reviewed.

**Papers excluded (already in vault):**
- Finding Answers from the Word of God: Domain Adaptation for Neural Networks in Biblical Question Answering (arXiv:1810.12118)
- BRAND: Bilingual Religious Accountable Norm Dataset (arXiv:2512.03943)
