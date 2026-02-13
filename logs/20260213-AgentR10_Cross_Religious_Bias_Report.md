# Agent R10 Report: Cross-Religious Comparative Studies & Religious Bias in LLMs

**Agent:** R10
**Focus:** Cross-religious comparative studies, religious bias in LLMs, religious stereotyping, religious hate speech detection, and religious fairness in AI
**Date:** 2026-02-13
**Model:** Claude Opus 4.6

## Search Terms Used
1. "religious bias LLM large language model evaluation"
2. "Islamophobia NLP dataset benchmark"
3. "antisemitism dataset NLP detection"
4. "religious stereotypes LLM benchmark evaluation"
5. "religious pluralism AI alignment"
6. "multi-faith benchmark LLM evaluation"
7. "religion bias GPT ChatGPT evaluation"
8. "religious hate speech NLP dataset"
9. "religious discrimination AI benchmark"
10. "comparative religion LLM knowledge evaluation"
11. "religious toxicity detection dataset"
12. "faith-based bias AI fairness benchmark"
13. "religious sentiment analysis NLP dataset"
14. "anti-Muslim bias NLP language model"
15. "religious knowledge evaluation LLM benchmark"
16. "anti-Christian bias AI evaluation"
17. "Hindu-Muslim bias NLP India"
18. "religious fairness AI benchmark dataset"

Plus targeted follow-up searches on specific papers identified from initial results.

---

## Papers Found

### 1. Divine LLaMAs: Bias, Stereotypes, Stigmatization, and Emotion Representation of Religion in Large Language Models
- **Authors:** Flor Miriam Plaza-del-Arco, Simone Tedeschi, Fer-Jan de Vries, Dirk Hovy
- **Year:** 2024
- **Venue:** Findings of EMNLP 2024
- **arXiv:** 2407.06908
- **DOI:** N/A
- **Religious Traditions:** Christianity, Islam, Judaism, Hinduism, Buddhism, Atheism, Agnosticism, and 12 other personas (19 total religious personas)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** 7,586 events from ISEAR dataset x 19 personas
- **Languages:** English
- **LLMs Tested:** Llama2, Llama3, Mistral-7b, GPT-4
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Systematically examines how LLMs represent different religions through emotion attribution using 19 distinct religious personas. Finds that major US/European religions are represented with more nuance, Eastern religions (Hinduism, Buddhism) are strongly stereotyped, and Judaism and Islam are stigmatized with model refusal rates skyrocketing. Llama2 frequently attributes fear, shame, and gratitude to Muslims and significant distortion toward shame for Jews.

---

### 2. Sometimes the Model doth Preach: Quantifying Religious Bias in Open LLMs through Demographic Analysis in Asian Nations
- **Authors:** Hari Shankar, and others
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2503.07510
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Buddhism, Christianity, Sikhism (multi-religion focus across Asian nations)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Survey-based (multiple countries)
- **Languages:** English (surveys from India, Indonesia, and other Asian nations)
- **LLMs Tested:** Llama, Mistral
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Evaluates modern open LLMs on surveys about religious tolerance and identity conducted in Global South countries, with focus on India and other Asian nations. Reveals that most open LLMs match a single homogeneous profile that varies across countries, raising concerns about LLMs promoting a hegemonic worldview and undermining minority religious perspectives.

---

### 3. Religious Bias Landscape in Language and Text-to-Image Models: Analysis, Detection, and Debiasing Strategies
- **Authors:** Ajwad Abrar, and others
- **Year:** 2025
- **Venue:** AI & Society (Springer) / arXiv
- **arXiv:** 2501.08441
- **DOI:** 10.1007/s00146-025-02721-z
- **Religious Traditions:** Christianity, Islam, Judaism, Hinduism, Buddhism, Sikhism, and others (cross-religious)
- **Paper Type:** Benchmark | Bias Study | Framework
- **Dataset Size:** ~400 unique prompts; 5,000 generated images
- **Languages:** English
- **LLMs Tested:** BERT, RoBERTa, ALBERT, DistilBERT, GPT-2, Llama-3, Mixtral-8x7B, Vicuna-13B, GPT-3.5, GPT-4, DALL-E 3
- **Code/Data:** https://github.com/ajwad-abrar/Religious-Bias (prompts and images publicly available)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Systematically investigates religious bias in both language models and text-to-image models across open-source and closed-source systems. Uses ~400 naturally occurring prompts for mask filling, prompt completion, and image generation. Finds disproportionate stereotypes and biases associated with certain religions, explores cross-domain biases intersecting with gender, age, and nationality, and evaluates debiasing strategies using corrective prompts.

---

### 4. Measuring Spiritual Values and Bias of Large Language Models
- **Authors:** Songyuan Liu, and 5 others
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** 2410.11647
- **DOI:** N/A
- **Religious Traditions:** Christianity (various denominations), Islam, Judaism, Hinduism, Buddhism, Atheism/Secularism, and others (10 spiritual value axes)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** SP-Typology and SP-10Axes questionnaire instruments (133 statements)
- **Languages:** English
- **LLMs Tested:** GPT-4-turbo, Llama-2, Llama-3, Qwen-1.5, Phi-3, Mistral, Gemma, and others
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Develops psychometric assessment tools (SP-Typology and SP-10Axes) to measure spiritual values and biases of LLMs. Finds that LLMs' spiritual values are surprisingly diverse, contrary to stereotypes of atheism/secularism. Discovers that different spiritual values lead to different sensitivity to hate target groups. Proposes continuing pre-training on spiritual texts as a mitigation strategy.

---

### 5. Muslim-Violence Bias Persists in Debiased GPT Models
- **Authors:** Babak Hemmatian, Lav R. Varshney
- **Year:** 2023
- **Venue:** NeurIPS 2023 Workshop / arXiv
- **arXiv:** 2310.18368
- **DOI:** N/A
- **Religious Traditions:** Islam, Christianity, Judaism, Hinduism (comparative)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Pre-registered experiments across multiple prompt formats
- **Languages:** English
- **LLMs Tested:** GPT-3, InstructGPT, ChatGPT
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Tests whether debiasing efforts in newer GPT models eliminate anti-Muslim violence bias. Finds that InstructGPT shows only weak bias, but using common names associated with religions in prompts reveals a significant second-order anti-Muslim bias. ChatGPT shows bias many times stronger regardless of prompt format, suggesting debiasing effects were reduced with continued development. Content analysis reveals offensive religion-specific stereotypes across all experiments.

---

### 6. Persistent Anti-Muslim Bias in Large Language Models
- **Authors:** Abubakar Abid, Maheen Farooqi, James Zou
- **Year:** 2021
- **Venue:** AAAI/ACM Conference on AI, Ethics, and Society (AIES 2021)
- **arXiv:** 2101.05783
- **DOI:** 10.1145/3461702.3462624
- **Religious Traditions:** Islam, Christianity, Judaism, Hinduism, Buddhism, Sikhism (comparative with Muslim focus)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Systematic prompt completion experiments
- **Languages:** English
- **LLMs Tested:** GPT-3
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Seminal paper demonstrating that GPT-3 captures persistent Muslim-violence bias that appears consistently and creatively across different uses of the model. "Muslim" is analogized to "terrorist" in 23% of test cases, while "Jewish" is mapped to "money" in 5%. Violent completions for Muslim prompts reach 66%, reducible to 20% with positive adjective mitigation but still higher than other religious groups. Highly cited foundational work.

---

### 7. Debiased Large Language Models Still Associate Muslims with Uniquely Violent Acts
- **Authors:** Babak Hemmatian, Lav R. Varshney
- **Year:** 2022
- **Venue:** arXiv
- **arXiv:** 2208.04417
- **DOI:** N/A
- **Religious Traditions:** Islam, Christianity, Hinduism (comparative)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Pre-registered replication experiments
- **Languages:** English
- **LLMs Tested:** GPT-3, InstructGPT
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Follow-up to Abid et al. (2021) examining whether fine-tuned InstructGPT eliminates anti-Muslim bias. Finds that explicit bias is reduced but using common Muslim, Christian, and Hindu names in prompts yields a highly significant second-order bias against Muslims. Muslim celebrity names from non-violent domains reduce violent completions, suggesting individuated information can counter stereotypes. Content analysis reveals religion-specific violent themes with highly offensive ideas.

---

### 8. Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions (FiqhQA)
- **Authors:** Multiple authors
- **Year:** 2025
- **Venue:** AIES 2025 / arXiv
- **arXiv:** 2508.08287
- **DOI:** N/A
- **Religious Traditions:** Islam (four Sunni schools of thought: Hanafi, Maliki, Shafi'i, Hanbali)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 406 questions (FiqhQA benchmark)
- **Languages:** Arabic, English (bilingual)
- **LLMs Tested:** GPT-4o, Gemini, Fanar, and others
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Introduces FiqhQA, the first benchmark evaluating LLM accuracy and abstention behavior for Islamic jurisprudence questions categorized by four major Sunni schools of thought. GPT-4o outperforms in accuracy, but Gemini and Fanar show superior abstention behavior. All models exhibit performance drops in Arabic compared to English. First study to evaluate school-of-thought-specific religious ruling generation.

---

### 9. Religious Bias Benchmarks for ChatGPT
- **Authors:** Multiple authors (presented at conference on Human Freedom and AI)
- **Year:** 2024
- **Venue:** Conference on Human Freedom and AI / ResearchGate
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Zen Buddhism, Catholicism, Sunni Islam, Orthodox Judaism, Secular Humanism
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 45,920 query responses (112 questions x 5 beliefs x 10 iterations x multiple models) containing 11.4 million words
- **Languages:** English
- **LLMs Tested:** GPT-3, GPT-4 (multiple versions)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Comprehensive evaluation of ChatGPT for religious bias using 112 morality and ethics questions tailored to five belief systems. Identifies six types of bias: explicit, anthropomorphic, statement, framing, coverage, and information bias. Finds biases often favor Buddhism or secular humanism and/or disfavor Abrahamic religions. GPT-4 mitigates three bias types but amplifies two others. No prompt engineering approach eliminates all biases.

---

### 10. Sacred or Secular? Religious Bias in AI-Generated Financial Advice
- **Authors:** Muhammad Salar Khan, Hamza Umer
- **Year:** 2025
- **Venue:** arXiv / SSRN
- **arXiv:** 2504.07118
- **DOI:** N/A
- **Religious Traditions:** Islam, Christianity, Judaism, Hinduism (cross-religious in financial context)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Financial email generation experiments
- **Languages:** English
- **LLMs Tested:** ChatGPT
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Examines religious biases in AI-generated financial advice. Finds that 50% of ChatGPT-generated financial emails exhibit religious biases, with both ingroup biases (personalizing responses based on religious alignment) and outgroup biases (introducing religious framing that may alienate clients). Suggests ChatGPT actively shapes financial discourse based on perceived religious identity rather than merely reflecting societal biases.

---

### 11. Cognitive Bias in Generative AI Influences Religious Education
- **Authors:** Zhang, Song, Liu
- **Year:** 2025
- **Venue:** Scientific Reports (Nature)
- **arXiv:** N/A
- **DOI:** 10.1038/s41598-025-99121-6
- **Religious Traditions:** Christianity, Islam, Judaism (multi-religion focus in education)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Experimental framework with pre/post-interaction evaluations
- **Languages:** English
- **LLMs Tested:** Generative AI systems (specific models evaluated)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Experimental study showing generative AI not only reflects but amplifies cognitive biases in religious education. Christianity and Judaism perceptions became more positive after AI interaction, while Islam perception became more negative. Finds AI acts as "double-edged sword": enhancing personalized learning while risking reinforcement of prejudice. Calls for ethical guidelines in deploying AI in religious contexts.

---

### 12. Blind Faith? User Preference and Expert Assessment of AI-Generated Religious Content
- **Authors:** Sabriya Alam, Marwa Abdulhai, Niloufar Salehi
- **Year:** 2025
- **Venue:** ACM FAccT 2025
- **arXiv:** N/A
- **DOI:** 10.1145/3715275.3732162
- **Religious Traditions:** Islam (primary focus, with implications for cross-religious AI content)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** 16 semi-structured interviews + 60 survey participants + expert evaluation
- **Languages:** English
- **LLMs Tested:** ChatGPT
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Mixed-methods study finding Muslim users overwhelmingly preferred AI-generated responses to Islamic questions (81.3%) in blind evaluations despite expressing distrust. Expert Islamic scholars found critical shortcomings in accuracy, depth, and contextual sensitivity. Highlights the paradox of user preference vs. expert quality assessment in religious AI content.

---

### 13. Explicitly Unbiased Large Language Models Still Form Biased Associations
- **Authors:** Xuechunzi Bai, Angelina Wang, Ilia Sucholutsky, Thomas L. Griffiths
- **Year:** 2025
- **Venue:** PNAS (Proceedings of the National Academy of Sciences)
- **arXiv:** N/A
- **DOI:** 10.1073/pnas.2416228122
- **Religious Traditions:** Christianity, Islam, Judaism (as part of 4-category bias evaluation)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 8 value-aligned models, 4 social categories, 21 stereotypes
- **Languages:** English
- **LLMs Tested:** 8 value-aligned models (specific names in paper)
- **Code/Data:** LLM Word Association Test, LLM Relative Decision Test (methodological tools)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Introduces two psychological measures (LLM Word Association Test and LLM Relative Decision Test) adapted from the Implicit Association Test to reveal implicit bias in explicitly unbiased LLMs. Finds pervasive stereotype biases across race, gender, religion, and health in 8 value-aligned models. For religion, all three tested religions show small negativity bias, with small pro-Christian bias over Islamic and Jewish groups. Sizable effects on discriminatory decisions.

---

### 14. How Deep Is Representational Bias in LLMs? The Cases of Caste and Religion
- **Authors:** Agrima Seth, Monojit Choudhury, Sunayana Sitaram, Kentaro Toyama, Aditya Vashistha, Kalika Bali
- **Year:** 2025
- **Venue:** AIES 2025
- **arXiv:** 2508.03712
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Sikhism, Jainism, Buddhism (Indian religious context)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** 7,200+ generated stories about life rituals in India
- **Languages:** English
- **LLMs Tested:** GPT-4 Turbo
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Systematic audit of GPT-4 Turbo revealing deeply encoded representational biases for caste and religion in the Indian context. Prompted to generate stories about birth, wedding, and death rituals, GPT-4 consistently overrepresents culturally dominant groups far beyond their statistical representation. Representational bias has a "winner-take-all" quality more biased than training data distribution, and repeated prompt-based nudges have limited efficacy.

---

### 15. GPTBIAS: A Comprehensive Framework for Evaluating Bias in Large Language Models
- **Authors:** Multiple authors
- **Year:** 2023
- **Venue:** arXiv
- **arXiv:** 2312.06315
- **DOI:** N/A
- **Religious Traditions:** Religion as one of 9 bias categories (cross-religious)
- **Paper Type:** Framework | Benchmark
- **Dataset Size:** Bias attack instruction set across 9 categories
- **Languages:** English
- **LLMs Tested:** GPT-4 (as evaluator), multiple target models
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Introduces a comprehensive bias evaluation framework using GPT-4 to assess bias across 9 categories including gender, religion, race, sexual orientation, age, nationality, disability, physical appearance, and socioeconomic status. Unlike conventional metrics providing only a bias score, GPTBIAS identifies bias types, keywords leading to bias, underlying causes, affected demographic groups, and mitigation suggestions. Can detect intersectional biases and works on proprietary systems.

---

### 16. IslamTrust: A Benchmark for LLMs Alignment with Islamic Values
- **Authors:** Multiple authors
- **Year:** 2025
- **Venue:** OpenReview / Workshop paper
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Islam (six domains of Islamic values)
- **Paper Type:** Benchmark
- **Dataset Size:** 406 questions across 6 domains
- **Languages:** Arabic, English (bilingual)
- **LLMs Tested:** SILMA-9B, Fanar-1-9B, and others
- **Code/Data:** https://github.com/aii-lab-dot-org/IslamTrust and https://huggingface.co/datasets/Abderraouf000/IslamTrust-benchmark
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** First multi-choice benchmark evaluating LLM alignment with Islamic values across 6 domains. Best model achieves only 66.5% overall alignment, with better Arabic (71.43%) than English (61.58%) performance. Shortcomings stem from limited Islamic ethical discourse in training data, inadequate handling of culturally specific contexts, and model tendency to default to non-Islamic knowledge.

---

### 17. Social Bias in Large Language Models for Bangla: An Empirical Study on Gender and Religious Bias
- **Authors:** Sadhu, Saha, and others
- **Year:** 2024
- **Venue:** arXiv / LoResLM Workshop (ACL 2025)
- **arXiv:** 2407.03536
- **DOI:** N/A
- **Religious Traditions:** Islam, Hinduism (Bangla-speaking context: 71% Muslim, 28% Hindu)
- **Paper Type:** Benchmark | Dataset | Evaluation
- **Dataset Size:** Curated dataset for bias measurement benchmarking
- **Languages:** Bangla
- **LLMs Tested:** Llama3-8b, GPT-3.5-Turbo, GPT-4o
- **Code/Data:** Publicly available (code and resources)
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** First bias assessment of LLMs for Bangla language examining gender and religious bias. Uses template-based and naturally sourced probing techniques. Finds significant biases in occupation-gender and name-religion associations. GPT-4o exhibits the highest level of bias among tested models. Addresses an important gap in low-resource language bias evaluation.

---

### 18. Re-contextualizing Fairness in NLP: The Case of India
- **Authors:** Shaily Bhatt, and others (Google Research)
- **Year:** 2022
- **Venue:** AACL-IJCNLP 2022
- **arXiv:** 2209.12226
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Sikhism, Buddhism, Jainism (Indian religious context)
- **Paper Type:** Framework | Dataset | Evaluation
- **Dataset Size:** Resources for fairness evaluation in Indian context
- **Languages:** English, Hindi (Indian context)
- **LLMs Tested:** HuggingFace default pipeline (DistilBERT)
- **Code/Data:** https://github.com/google-research-datasets/nlp-fairness-for-india
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Builds resources for fairness evaluation in the Indian context demonstrating prediction biases. Delves into social stereotypes for Region and Religion, demonstrating prevalence in corpora and models. Outlines a holistic research agenda to re-contextualize NLP fairness for India, accounting for caste, religion, and regional identity. Framework generalizable to other geo-cultural contexts.

---

### 19. Annotating Antisemitic Online Content: Towards an Applicable Definition of Antisemitism
- **Authors:** Jikeli, Cavar, and others
- **Year:** 2019
- **Venue:** arXiv
- **arXiv:** 1910.01214
- **DOI:** N/A
- **Religious Traditions:** Judaism (antisemitism focus)
- **Paper Type:** Dataset | Framework
- **Dataset Size:** Randomly sampled Twitter conversations about Jews and Israel
- **Languages:** English
- **LLMs Tested:** N/A (annotation framework)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Demonstrates that the IHRA working definition of antisemitism can be successfully applied to annotating online messages. Finds more than 10% of Twitter conversations about Jews and Israel are antisemitic. Argues antisemitic content has distinct features not captured by generic hate speech annotation. Requires highly trained annotators knowledgeable about current events. Foundational work for antisemitism NLP detection.

---

### 20. "Subverting the Jewtocracy": Online Antisemitism Detection Using Multimodal Deep Learning
- **Authors:** Mohit Chandra, Pailla, and others (IIIT Hyderabad)
- **Year:** 2021
- **Venue:** ACM Web Science Conference 2021
- **arXiv:** 2104.05947
- **DOI:** 10.1145/3447535.3462502
- **Religious Traditions:** Judaism (antisemitism focus)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 3,102 Twitter posts + 3,509 Gab posts (multimodal: text + images)
- **Languages:** English
- **LLMs Tested:** N/A (deep learning classifiers)
- **Code/Data:** https://github.com/mohit3011/Online-Antisemitism-Detection-Using-MultimodalDeep-Learning
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** First work on automated multimodal detection of online antisemitism. Collects and labels two datasets from Twitter and Gab with both text and image modalities. Detects presence of antisemitic content and its specific antisemitism category using multimodal deep learning. Addresses the gap that online antisemitism has not been studied from a machine learning perspective compared to other forms of abuse.

---

### 21. Evaluating Large Language Models for Detecting Antisemitism
- **Authors:** Multiple authors
- **Year:** 2025
- **Venue:** EMNLP 2025 / arXiv
- **arXiv:** 2509.18293
- **DOI:** N/A
- **Religious Traditions:** Judaism (antisemitism detection)
- **Paper Type:** Evaluation | Benchmark
- **Dataset Size:** ~22K annotated samples (non-publicly available)
- **Languages:** English
- **LLMs Tested:** 8 open-source LLMs including Llama 3.1 70B, fine-tuned GPT-3.5
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** First study exploring LLM capabilities in detecting antisemitism using the IHRA definition as policy. Designs novel Guided-CoT prompt that injects domain-specific reasoning, increasing performance and reducing refusals across all models. Llama 3.1 70B outperforms fine-tuned GPT-3.5. Demonstrates effectiveness of in-context definition injection for specialized hate speech detection.

---

### 22. Using LLMs to Discover Emerging Coded Antisemitic Hate-Speech in Extremist Social Media
- **Authors:** Multiple authors (American University)
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** 2401.10841
- **DOI:** N/A
- **Religious Traditions:** Judaism (coded antisemitism)
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** 150,000+ posts analyzed
- **Languages:** English
- **LLMs Tested:** Fine-tuned LLM classifiers
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Proposes methodology for detecting emerging coded antisemitic terminology using LLMs, based on the hypothesis that coded terminology begets more coded terminology. Uses semantic similarity to known antisemitic terminology via fine-tuned LLMs to filter emergent expressions. Addresses the evolving nature of hate speech where communities invent new coded terms to evade detection.

---

### 23. Detecting Weak and Strong Islamophobic Hate Speech on Social Media
- **Authors:** Bertie Vidgen, Taha Yasseri
- **Year:** 2020
- **Venue:** Journal of Information Technology & Politics
- **arXiv:** 1812.10400
- **DOI:** 10.1080/19331681.2019.1702607
- **Religious Traditions:** Islam (Islamophobia)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 1,341 manually annotated tweets (training); applied to 109,488 tweets
- **Languages:** English
- **LLMs Tested:** N/A (SVM, GloVe embeddings)
- **Code/Data:** https://github.com/bvidgen/Weak_strong_Islamophobia
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Builds a multi-class classifier distinguishing non-Islamophobic, weak Islamophobic, and strong Islamophobic content. Achieves 77.6% accuracy. Applied to 109,488 far-right tweets from 2017, finding weak Islamophobia (36,963) considerably more prevalent than strong (14,895). Uses custom-trained GloVe embeddings on 140 million tweets. Multi-class approach captures the nuanced nature of Islamophobia better than binary.

---

### 24. Are They Our Brothers? Analysis and Detection of Religious Hate Speech in the Arabic Twittersphere
- **Authors:** Nuha Albadi, Maram Kurdi, Shivakant Mishra
- **Year:** 2018
- **Venue:** IEEE/ACM ASONAM 2018
- **arXiv:** N/A
- **DOI:** 10.1109/ASONAM.2018.8508247
- **Religious Traditions:** Sunni Islam, Shia Islam, and other Arabic religious groups (sectarian focus)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 5,569 training + 567 testing examples; first Arabic religious hate speech lexicon
- **Languages:** Arabic
- **LLMs Tested:** N/A (RNN with GRU)
- **Code/Data:** https://github.com/nuhaalbadi/Arabic_hatespeech
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** First paper to address religious hate speech detection in Arabic Twitter. Creates the first publicly available Arabic dataset annotated for religious hate speech and the first Arabic lexicon of religious discussion terms with polarity/strength scores. Achieves 0.84 AUROC with simple RNN-GRU architecture. Addresses sectarian hate speech, a critical gap in Arabic NLP.

---

### 25. Addressing Religious Hate Online: From Taxonomy Creation to Automated Detection
- **Authors:** Multiple authors
- **Year:** 2022
- **Venue:** PeerJ Computer Science
- **arXiv:** N/A
- **DOI:** 10.7717/peerj-cs.1128
- **Religious Traditions:** Judaism, Christianity, Islam (three monotheistic religions)
- **Paper Type:** Dataset | Framework | Benchmark
- **Dataset Size:** Bilingual Twitter dataset (English + Italian)
- **Languages:** English, Italian
- **LLMs Tested:** Traditional ML + transformer-based models
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Proposes a fine-grained labeling scheme for religious hate speech detection covering the three main monotheistic religions. Creates a bilingual Twitter dataset (English and Italian) annotated with the proposed scheme. Experiments with classifiers from traditional ML to transformers on two tasks: abusive language detection and religious hate speech detection. Addresses the gap of scattered efforts in religious hate data and methods.

---

### 26. Religion and Racial Bias in Artificial Intelligence Large Language Models
- **Authors:** Joshua C. Tom, Todd W. Ferguson, Brandon C. Martinez
- **Year:** 2025
- **Venue:** Socius (SAGE)
- **arXiv:** N/A
- **DOI:** 10.1177/23780231251377210
- **Religious Traditions:** Evangelical Protestantism, Catholicism, Judaism, Islam (cross-religious)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** 175 AI-generated sermons
- **Languages:** English
- **LLMs Tested:** GPT-4, GPT-4o, Gemini, Claude 3 Opus, Llama 4
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Examines whether LLMs hold implicit assumptions about religious identities by generating 175 sermons specifying different combinations of race and religion. Finds Evangelical Protestant pastors had easier-to-read sermons while Jewish rabbis and Muslim imams had more difficult synthetic texts. Novel readability-based bias measurement approach. Tests five major LLMs for intersectional race-religion bias.

---

### 27. Deep Learning for Religious and Continent-Based Toxic Content Detection and Classification
- **Authors:** Abbasi, A., Javed, A.R., Iqbal, F., and others
- **Year:** 2022
- **Venue:** Scientific Reports (Nature)
- **arXiv:** N/A
- **DOI:** 10.1038/s41598-022-22523-3
- **Religious Traditions:** Muslim, Jewish, Christian, Hindu, Buddhist, Atheist, and other religious identities (multi-religion toxicity)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** 448,000 rows (Religious Toxic Comments dataset); 42,906 hazardous religious remarks
- **Languages:** English
- **LLMs Tested:** N/A (CNN, LSTM, BiLSTM deep learning models)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Creates a large-scale Religious Toxic Comments (RTC) dataset with 448,000 rows including 42,906 hazardous religious remarks. Compares deep learning algorithms for multilabel toxic comment classification targeting religious groups. Addresses the critical problem where nontoxic comments containing religious identity descriptors (Muslim, Jewish, etc.) were assigned unrealistically high toxicity ratings. Provides baselines for religious toxicity detection.

---

### 28. DweshVaani: An LLM for Detecting Religious Hate Speech in Code-Mixed Hindi-English
- **Authors:** Multiple authors
- **Year:** 2025
- **Venue:** CHiPSAL 2025 Workshop (COLING 2025)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Sikhism (Indian religious context)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** Code-mixed Hindi-English hate speech dataset
- **Languages:** Hindi-English (code-mixed)
- **LLMs Tested:** Meta LLMs, Google LLMs, OpenAI LLMs, Nvidia LLMs, Sarvam, Indic-Gemma, Airavata, DweshVaani (fine-tuned Gemma-2)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Investigates LLM performance on religious hate speech detection in code-mixed Hindi-English. Tests cutting-edge international and Indic-specific LLMs. Finds Indic-LLMs tuned on Indian content underperform. Proposes DweshVaani, a fine-tuned Gemma-2 using knowledge distillation, which outperforms all other approaches for religious hate speech detection and targeted religion identification in code-mixed languages.

---

### 29. YouTube-Based Religious Hate Speech and Extremism Detection Dataset with Machine Learning Baselines
- **Authors:** Noman Ashraf, Abid Rafiq, Sabur Butt, Hafiz Muhammad Faisal Shehzad, Grigori Sidorov, Alexander Gelbukh
- **Year:** 2022
- **Venue:** Journal of Intelligent and Fuzzy Systems
- **arXiv:** N/A
- **DOI:** 10.3233/JIFS-219264
- **Religious Traditions:** Multi-religion (YouTube religious extremism)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** YouTube comments dataset from religious videos
- **Languages:** English
- **LLMs Tested:** N/A (SVM, LR, k-NN baselines)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Creates a novel dataset for religious hate speech detection from YouTube comments. Applies data mining techniques on comments from religious videos to filter religion-oriented messages and detect videos used for spreading hate. Provides SVM, Logistic Regression, and k-NN baselines. Addresses the understudied platform of YouTube for religious extremism detection.

---

### 30. hatebnBERT: An Innovative Novel Transformer Model and Datasets for Safeguarding Religious Sensitivities in Online Social Platforms
- **Authors:** Multiple authors
- **Year:** 2024
- **Venue:** Procedia Computer Science
- **arXiv:** N/A
- **DOI:** 10.1016/j.procs.2024.02.XXX
- **Religious Traditions:** Islam, Hinduism (Bangla-speaking religious communities)
- **Paper Type:** Dataset | Benchmark
- **Dataset Size:** Binary classification dataset + five-class dataset (Blasphemy, Ethnic Hatred, Ethnic Group Hatred, Undetermined, Non-Hatred)
- **Languages:** Bangla
- **LLMs Tested:** hatebnBERT (custom BERT for Bangla)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Introduces hatebnBERT, a BERT-based model tailored to Bangla for religious hate speech detection. Creates two datasets: binary (hate/not) and five-class categorization including Blasphemy and Ethnic Hatred. Achieves 98.8% accuracy (binary) and 98.6% (multiclass). Addresses Bangla-specific religious sensitivity challenges between Muslim and Hindu communities.

---

### 31. Parity Benchmark for Measuring Bias in LLMs
- **Authors:** Multiple authors
- **Year:** 2024
- **Venue:** AI and Ethics (Springer)
- **arXiv:** N/A
- **DOI:** 10.1007/s43681-024-00613-4
- **Religious Traditions:** Religion as one category within broader bias evaluation (cross-religious)
- **Paper Type:** Benchmark
- **Dataset Size:** 66 bias evaluation questions across multiple categories
- **Languages:** English
- **LLMs Tested:** GPT-4, Claude 3.5 Sonnet, Gemma-1.1, and others (14 LLMs)
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Benchmarks bias in 14 leading LLMs across categories including Ageism, Colonial bias, Colorism, Disability, Homophobia, Racism, Sexism, and Supremacism (religion intersects multiple categories). All LLMs achieve 74%+ accuracy on knowledge questions but performance drops for interpretation and reasoning. GPT-4 performs best on content knowledge. First benchmark introduced between 2021-2023 focusing specifically on bias/equity.

---

### 32. Antisemitism on Twitter: A Dataset for Machine Learning and Text Analytics
- **Authors:** ISCA (Institute for the Study of Contemporary Antisemitism, Indiana University)
- **Year:** 2023
- **Venue:** Zenodo
- **arXiv:** N/A
- **DOI:** 10.5281/zenodo.7872834
- **Religious Traditions:** Judaism (antisemitism)
- **Paper Type:** Dataset
- **Dataset Size:** 6,941 tweets (1,250 antisemitic = 18%)
- **Languages:** English
- **LLMs Tested:** N/A (dataset resource)
- **Code/Data:** https://zenodo.org/records/7932888
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R10

**Summary:** Large-scale dataset of 6,941 tweets covering conversations about Jews, Israel, and antisemitism from January 2019 to December 2021. 18% of tweets meet the IHRA definition of antisemitic messages. Created by the Institute for the Study of Contemporary Antisemitism at Indiana University. Available on Zenodo for research use.

---

### 33. Religion, Theology, and Philosophical Skills of LLM-Powered Chatbots
- **Authors:** Marcin Trepczynski
- **Year:** 2024
- **Venue:** Disputatio philosophica (International Journal on Philosophy and Religion)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (scriptural interpretation), cross-religious theological reasoning
- **Paper Type:** Evaluation | Benchmark
- **Dataset Size:** Qualitative evaluation with structured assessment criteria
- **Languages:** English
- **LLMs Tested:** ChatGPT, Bing, Bard, Llama2
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Tests LLM-powered chatbots on religious/theological tasks using three evaluation sources: theory of four senses of Scripture, abstract theological statements, and abstract logic from religious texts. Measures philosophical skills including interpretation, creative deductive reasoning, and identification of ontological limitations. Provides assessment criteria and scales for benchmarking chatbot religious/theological reasoning. Chatbot performance is inconsistent, showing creativity but often failing at complex theological logic.

---

### 34. Improving LLM Reliability with RAG in Religious Question-Answering: MufassirQAS
- **Authors:** Ahmet Yusuf Alan, Enis Karaarslan, Omer Aydin
- **Year:** 2024
- **Venue:** Turkish Journal of Engineering / arXiv
- **arXiv:** 2401.15378
- **DOI:** N/A
- **Religious Traditions:** Islam (Quranic interpretation and Islamic texts)
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** Vector database of fundamental Islamic texts (Turkish translations and interpretations)
- **Languages:** Turkish, Arabic
- **LLMs Tested:** ChatGPT (compared with MufassirQAS)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Develops a RAG-based system to enhance LLM accuracy for Islamic religious question-answering. Builds a vector database from Turkish translations and interpretations of Islamic texts. Provides source page numbers and referenced articles for credibility. Demonstrates superior performance over ChatGPT on sensitive religious questions. Addresses hallucination risks in religious content generation.

---

### 35. Detecting Anti-Semitic Hate Speech Using Transformer-Based Large Language Models
- **Authors:** Multiple authors
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** 2405.03794
- **DOI:** N/A
- **Religious Traditions:** Judaism (antisemitism)
- **Paper Type:** Evaluation
- **Dataset Size:** Fine-tuned on ~22K annotated samples
- **Languages:** English
- **LLMs Tested:** Fine-tuned GPT-3.5, BERT variants
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Fine-tunes transformer-based LLMs for antisemitism detection using a dataset of approximately 22K annotated samples. Achieves 80% accuracy and 72% F-Score in extracting antisemitic terms using NLP techniques including POS tagging, TF-IDF, and fine-tuned LLMs. Addresses the gap in machine learning approaches to antisemitism compared to other forms of online abuse.

---

### 36. Monitoring the Evolution of Antisemitic Discourse on Extremist Social Media Using BERT
- **Authors:** Multiple authors (American University)
- **Year:** 2024
- **Venue:** arXiv
- **arXiv:** 2403.05548
- **DOI:** N/A
- **Religious Traditions:** Judaism (antisemitism evolution)
- **Paper Type:** Evaluation | Framework
- **Dataset Size:** 150,000+ posts (August 2024 - January 2025)
- **Languages:** English
- **LLMs Tested:** BERT-based classifiers
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R10

**Summary:** Develops custom BERT-based classifiers to identify antisemitic discourse with high precision and recall. Monitors the evolution of antisemitic language on extremist social media platforms, analyzing over 150,000 posts. Companion work to the coded antisemitic terminology detection paper (2401.10841). Addresses the temporal dynamics of how antisemitic language evolves online.

---

---

## Summary Statistics

### Total Papers Found: 36

### Breakdown by Primary Religious Tradition Focus
| Tradition | Count |
|-----------|-------|
| Cross-religious / Multi-faith | 16 |
| Islam / Islamophobia | 10 |
| Judaism / Antisemitism | 7 |
| Indian religions (Hindu-Muslim-Sikh) | 3 |

### Breakdown by Paper Type
| Type | Count |
|------|-------|
| Evaluation / Bias Study | 18 |
| Dataset / Benchmark | 14 |
| Framework | 6 |
| (Note: papers can have multiple types) | |

### Breakdown by Implementation Readiness
| Readiness | Count |
|-----------|-------|
| HIGH | 23 |
| MEDIUM | 13 |
| LOW | 0 |

### Languages Covered
English (dominant), Arabic, Bangla, Turkish, Italian, Hindi-English (code-mixed)

### Key LLMs Evaluated Across Papers
GPT-3, GPT-4, GPT-4o, ChatGPT, Llama 2/3, Mistral, Gemma, Claude 3 Opus, Gemini, BERT variants, Qwen, Phi-3, and various Indic LLMs

### Key Observations and Gaps

1. **Anti-Muslim bias is the most studied religious bias in LLMs** -- Multiple seminal papers (Abid et al. 2021, Hemmatian & Varshney 2022/2023) demonstrate persistent Muslim-violence associations. This is the most mature subfield.

2. **Antisemitism detection is growing rapidly** -- From annotation frameworks (2019) to multimodal detection (2021) to LLM-based evaluation (2025), there is a clear trajectory toward more sophisticated tools, though datasets remain smaller than for other bias types.

3. **Cross-religious comparative benchmarks remain rare** -- Most papers focus on one or two religions. Only a handful (Divine LLaMAs, Religious Bias Landscape, SP-10Axes) systematically compare across 5+ religions.

4. **Indian religious context is uniquely complex** -- The intersection of caste and religion in India (papers #14, #17, #18, #28, #30) creates bias patterns not seen elsewhere, with Hindu dominance in LLM representations.

5. **Non-English religious bias is severely understudied** -- Most work is English-centric. Arabic (papers #8, #16, #24), Bangla (#17, #30), Turkish (#34), and Hindi-English code-mixed (#28) are exceptions. No significant work found for East Asian religious bias in native languages.

6. **Text-to-image religious bias** is an emerging frontier (paper #3), with only one comprehensive study found.

7. **Christian bias in AI** receives less academic attention than Muslim or Jewish bias, despite popular discourse about anti-Christian AI bias. Paper #26 is a rare exception examining evangelical Protestant vs. other Christian traditions.

8. **Religious fairness in financial/professional AI applications** (paper #10) is virtually unexplored, representing a significant gap.

9. **Debiasing effectiveness is questionable** -- Multiple papers show that explicit debiasing reduces but does not eliminate religious bias, and newer models (ChatGPT) can show stronger biases than earlier ones (InstructGPT).

10. **The BRAND paper (2512.03943) was excluded** as it is already in the vault.
