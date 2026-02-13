# Agent R9 Report: Zoroastrianism, Baha'i, Interfaith, Multi-Faith, and Minor Religious Traditions in LLM Benchmarks

**Agent:** R9
**Focus:** Zoroastrianism, Baha'i, Jainism AI/ethics, interfaith/multi-faith benchmarks, Tengrism, Rastafari, and other minor religious traditions; comprehensive multi-religion benchmarks
**Date:** 2026-02-13
**Wave:** 2 (R6-R10)

## Search Terms Used (15 queries)
1. "Zoroastrian NLP Avesta dataset"
2. "Baha'i AI ethics evaluation"
3. "interfaith AI benchmark evaluation LLM"
4. "world religions benchmark LLM evaluation"
5. "multi-faith AI alignment dataset"
6. "religious knowledge QA benchmark LLM"
7. "Jain ethics AI ahimsa nonviolence benchmark"
8. "comparative religion NLP dataset"
9. "Rastafari AI ethics"
10. "Tengrism AI NLP"
11. "religious text understanding benchmark LLM"
12. "religion question answering dataset evaluation"
13. "Sikh ethics AI Guru Granth Sahib benchmark" (supplement R3)
14. "religious values pluralism AI benchmark"
15. "sacred texts NLP evaluation benchmark"

Additionally ran follow-up targeted queries for paper-specific details.

---

## Papers Found

### 1. Measuring Spiritual Values and Bias of Large Language Models
- **Authors:** Songyuan Liu, Ziyang Zhang, Runze Yan, Wei Wu, Carl Yang, Jiaying Lu
- **Year:** 2024
- **Venue:** arXiv (Emory University)
- **arXiv:** 2410.11647
- **DOI:** N/A
- **Religious Traditions:** Judaism, Christianity, Islam, Hinduism, Buddhism, Non-religious (6 spiritual-oriented groups)
- **Paper Type:** Benchmark | Evaluation | Bias Study
- **Dataset Size:** Uses SP-Typology (7 subtypes) and SP-10Axes instruments; evaluates on hate speech detection tasks across religions
- **Languages:** English
- **LLMs Tested:** Multiple LLMs (details in paper); includes fine-tuning on Vedas, Bible, Torah, Quran
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Introduces two assessment tools (SP-Typology and SP-10Axes) adapted from the Pew Research Center's religious typology to measure LLMs' spiritual values across six major traditions. Finds that LLMs' spiritual values are diverse (not uniformly secular as stereotyped), and that fine-tuning on religious canons (especially Vedas, ~14% improvement) enhances hate speech detection. Different spiritual orientations lead to different sensitivity to hate against specific target groups.

---

### 2. Sometimes the Model doth Preach: Quantifying Religious Bias in Open LLMs through Demographic Analysis in Asian Nations
- **Authors:** Hari Shankar, Vedanta S P, Tejas Cavale, Ponnurangam Kumaraguru, Abhijnan Chakraborthy
- **Year:** 2025
- **Venue:** arXiv
- **arXiv:** 2503.07510
- **DOI:** N/A
- **Religious Traditions:** Hinduism, Islam, Christianity, Buddhism, Sikhism (via Asian demographic surveys)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Uses survey data from India and other Asian nations
- **Languages:** English
- **LLMs Tested:** Llama, Mistral, and other open LLMs
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Profiles open LLMs on religious surveys from Asian nations (India, South-East Asia) where religion, collectivism, and communal ties are prominent. Reveals that most open LLMs match a single homogeneous profile that varies by country, raising concerns about LLMs promoting a hegemonic worldview and undermining minority religious perspectives. First study to evaluate religious bias from a Global South lens.

---

### 3. Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions (FiqhQA)
- **Authors:** Farah Atif, Nursultan Askarbekuly, Kareem Darwish, Monojit Choudhury
- **Year:** 2025
- **Venue:** AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025); arXiv
- **arXiv:** 2508.08287
- **DOI:** N/A
- **Religious Traditions:** Islam (four Sunni schools: Maliki, Shafi'i, Hanafi, Hanbali)
- **Paper Type:** Benchmark | Dataset | Evaluation
- **Dataset Size:** 960 curated QA pairs (English + Arabic, all 4 schools)
- **Languages:** English, Arabic
- **LLMs Tested:** GPT-4o, Gemini, Fanar, and others
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Introduces FiqhQA, the first benchmark categorizing Islamic rulings by four Sunni schools of thought in both English and Arabic. Evaluates LLMs on both accuracy and abstention behavior (knowing when not to answer). GPT-4o leads on accuracy; Gemini and Fanar demonstrate superior abstention behavior. Significant performance drop observed in Arabic vs. English. Note: While Islam-focused, this is included here as a major multi-school religious QA benchmark missed by other agents.

---

### 4. Religious Bias Landscape in Language and Text-to-Image Models: Analysis, Detection, and Debiasing Strategies
- **Authors:** Ajwad Abrar, Nafisa Tabassum Oeshy, Mohsinul Kabir, Sophia Ananiadou
- **Year:** 2025
- **Venue:** AI & SOCIETY (Springer); arXiv
- **arXiv:** 2501.08441
- **DOI:** 10.1007/s00146-025-02721-z
- **Religious Traditions:** Islam, Christianity, Judaism, Hinduism, Buddhism (multiple religions)
- **Paper Type:** Bias Study | Dataset | Evaluation
- **Dataset Size:** ~460 unique prompts + 5,000 generated images
- **Languages:** English
- **LLMs Tested:** BERT, RoBERTa, ALBERT, DistilBERT, GPT-2, DALL-E, Stable Diffusion
- **Code/Data:** https://github.com/ajwad-abrar/Religious-Bias
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Systematically investigates religious bias across both language models and text-to-image models using ~460 curated prompts for mask-filling, prompt-completion, and image generation tasks. Finds consistent association of Islam with violence across multiple models. Evaluates debiasing techniques including positive term augmentation and bias mitigation instructions. Publicly released dataset and generated images for further research.

---

### 5. Persistent Anti-Muslim Bias in Large Language Models
- **Authors:** Abubakar Abid, Maheen Farooqi, James Zou
- **Year:** 2021
- **Venue:** AAAI/ACM Conference on AI, Ethics, and Society (AIES 2021)
- **arXiv:** 2101.05783
- **DOI:** 10.1145/3461702.3462624
- **Religious Traditions:** Islam, Judaism, Christianity, Hinduism, Buddhism, Sikhism (comparative)
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Multiple prompt templates; "Muslim" analogized to "terrorist" in 23% of cases
- **Languages:** English
- **LLMs Tested:** GPT-3
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Seminal study demonstrating persistent Muslim-violence bias in GPT-3 across prompt completion, analogical reasoning, and story generation. "Muslim" mapped to "terrorist" in 23% of test cases vs. "Jewish" to "money" in 5%. Even with positive adjective injection, violent completions for Muslim prompts (20%) remain higher than for other religious groups. Foundational paper for all subsequent religious bias work.

---

### 6. Religion, Theology, and Philosophical Skills of LLM-Powered Chatbots
- **Authors:** Marcin Trepczynski
- **Year:** 2023
- **Venue:** Disputatio philosophica: International Journal on Philosophy and Religion
- **arXiv:** N/A
- **DOI:** 10.32701/dp.25.1.2
- **Religious Traditions:** Christianity (four senses of Scripture, abstract theological statements)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 3 benchmark tasks with detailed scoring rubrics
- **Languages:** English
- **LLMs Tested:** ChatGPT, Bing, Bard, Llama2
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Demonstrates how religion and theology can serve as effective LLM benchmark material by using (1) the theory of four senses of Scripture, (2) abstract theological statements, and (3) logic formulas derived from religious texts. These tasks measure interpretation, creative deductive reasoning, and identification of ontological limitations. Provides a scoring methodology for comparing chatbot philosophical skills. Reveals significant performance differences across models.

---

### 7. Modeling the Sacred: Considerations when Using Religious Texts in Natural Language Processing
- **Authors:** Ben Hutchinson
- **Year:** 2024
- **Venue:** Findings of NAACL 2024
- **arXiv:** 2404.14740
- **DOI:** N/A
- **Religious Traditions:** Multiple (empirical survey of NLP papers using sacred texts across traditions)
- **Paper Type:** Framework | Evaluation
- **Dataset Size:** Empirical survey of NLP papers using religious texts
- **Languages:** Multiple
- **LLMs Tested:** N/A (meta-study)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Position paper presenting an empirical study of how NLP papers use sacred texts. Argues that religious texts encode culturally important values that ML models reproduce, and that repurposing translations for NLP raises considerations beyond bias: data provenance, proselytism, marginalized communities' perspectives. Discusses approaches from ethical theories, Indigenous perspectives, human rights, and institutional AI principles. Foundational for ethical frameworks around religious text NLP.

---

### 8. Mechanistic Interpretability with SAEs: Probing Religion, Violence, and Geography in Large Language Models
- **Authors:** Katharina Simbeck, Mariam Mahran
- **Year:** 2025
- **Venue:** AEQUITAS 2025 Workshop (co-located with ECAI 2025); arXiv
- **arXiv:** 2509.17665
- **DOI:** N/A
- **Religious Traditions:** Islam, Christianity, Judaism, Hinduism, Buddhism
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Latent feature activations across 5 models
- **Languages:** English
- **LLMs Tested:** GPT2-small, Gemma-2-9b, and 3 others
- **Code/Data:** Uses Neuronpedia API
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Uses Sparse Autoencoders (SAEs) to probe how religion is internally represented in LLMs and how it intersects with violence and geography. Finds that while all five religions show comparable internal cohesion, Islam is disproportionately linked to violence-associated features. Smaller models (GPT2-small) show noisier, more exaggerated associations (e.g., Hinduism-crime), while larger models encode more abstract representations. Novel interpretability approach to religious bias.

---

### 9. Religion and Racial Bias in Artificial Intelligence Large Language Models
- **Authors:** Joshua C. Tom, Todd W. Ferguson, Brandon C. Martinez
- **Year:** 2025
- **Venue:** Socius: Sociological Research for a Dynamic World (SAGE)
- **arXiv:** N/A
- **DOI:** 10.1177/23780231251377210
- **Religious Traditions:** Evangelical Protestant, Catholic, Jewish, Muslim, Buddhist, Hindu, Sikh, Non-religious
- **Paper Type:** Bias Study | Evaluation
- **Dataset Size:** Generated sermons across multiple religion-race intersections
- **Languages:** English
- **LLMs Tested:** Multiple (sermons generated by LLMs for hypothetical clergy of varying races and religions)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Examines how social biases are embedded in LLM-generated religious content by analyzing readability scores of AI-generated sermons across different religions and racial backgrounds. Finds Evangelical Protestant pastors had easier-to-read AI sermons, while Jewish rabbis and Muslim imams received more difficult texts. Reveals intersection of religious and racial bias in LLM outputs. First study to use religious sermon generation as a bias measurement tool.

---

### 10. Artificial Intelligence's Understanding of Religion: Investigating the Moralistic Approaches Presented by Generative Artificial Intelligence Tools
- **Authors:** Ruth Tsuria, Yoel Tsuria
- **Year:** 2024
- **Venue:** Religions (MDPI)
- **arXiv:** N/A
- **DOI:** 10.3390/rel15030375
- **Religious Traditions:** Multiple (cross-religious comparative prompting)
- **Paper Type:** Evaluation
- **Dataset Size:** Qualitative analysis of AI-generated responses to religious prompts
- **Languages:** English
- **LLMs Tested:** Generative AI tools (ChatGPT and others)
- **Code/Data:** N/A
- **Implementation Readiness:** LOW
- **Source Agent(s):** R9

**Summary:** Investigates how generative AI tools understand and represent religion, finding three key patterns: AI struggles with complex religious issues, emphasizes diversity of opinions, and adopts a "moralizing" liberal approach that encourages respectful interfaith dialogue. Raises concern that AI's moralistic tendency could replace human moral reasoning. Qualitative methodology with implications for how LLMs handle religious pluralism.

---

### 11. Cognitive Bias in Generative AI Influences Religious Education
- **Authors:** Jing Zhang, Wenlong Song, Yang Liu
- **Year:** 2025
- **Venue:** Scientific Reports (Nature)
- **arXiv:** N/A
- **DOI:** 10.1038/s41598-025-99121-6
- **Religious Traditions:** Multiple (cross-religious; experimental framework)
- **Paper Type:** Evaluation | Bias Study
- **Dataset Size:** Pre/post-interaction experimental evaluation framework
- **Languages:** English
- **LLMs Tested:** Generative AI tools (not specified)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Explores how generative AI shapes religious cognition through amplified cognitive biases, affecting users' understanding of religious doctrines and cultural diversity. Uses experimental frameworks with pre/post-interaction evaluations. Finds AI acts as a "double-edged sword" in religious education: enhancing personalized learning and cross-cultural understanding while risking prejudice reinforcement. Published in Nature Scientific Reports, adding credibility.

---

### 12. Blind Faith? User Preference and Expert Assessment of AI-Generated Religious Content
- **Authors:** Sabriya Alam, Marwa Abdulhai, Niloufar Salehi
- **Year:** 2025
- **Venue:** ACM Conference on Fairness, Accountability, and Transparency (FAccT 2025)
- **arXiv:** N/A
- **DOI:** 10.1145/3715275.3732162
- **Religious Traditions:** Islam (Muslim users and scholars)
- **Paper Type:** Evaluation
- **Dataset Size:** Mixed-methods (surveys, interviews, expert consultations)
- **Languages:** English
- **LLMs Tested:** AI chatbots (not specified in abstract)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Muslim users overwhelmingly preferred AI-generated responses to Islamic questions in blind evaluations (81.3% of cases), despite expressing distrust in AI for religious guidance. However, expert evaluations of the same responses revealed critical shortcomings in accuracy, depth, and contextual sensitivity. Reveals a dangerous disconnect between user preference and actual quality in AI religious content. Published at top venue FAccT 2025.

---

### 13. Comparative Analysis of Religious Texts: NLP Approaches to the Bible, Quran, and Bhagavad Gita
- **Authors:** Mahit Nandan A D, Ishan Godbole, Pranav M Kapparad, Shrutilipi Bhattacharjee
- **Year:** 2025
- **Venue:** CLREL Workshop at COLING 2025 (Abu Dhabi)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (Bible), Islam (Quran), Hinduism (Bhagavad Gita)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** Full texts of Bible, Quran, Bhagavad Gita
- **Languages:** English
- **LLMs Tested:** N/A (uses LDA, GloVe, Sentence Transformers, VADER)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Applies NLP techniques (topic modeling via LDA, GloVe embeddings, Sentence Transformers, VADER sentiment analysis) to compare the Bible, Quran, and Bhagavad Gita. Reveals unique and shared themes and sentiment patterns across the three scriptures. Published at the inaugural CLREL (Computational Linguistics for Religious Texts) workshop at COLING 2025, signaling a new dedicated venue for this research area.

---

### 14. Lexical, Sentiment and Correlation Analysis of Sacred Writings: A Tale of Cultural Influxes and Different Ways to Interpret Reality
- **Authors:** Alonso Felipe-Ruiz
- **Year:** 2024
- **Venue:** Natural Language Processing (Elsevier)
- **arXiv:** N/A
- **DOI:** 10.1016/j.nlp.2024.100121
- **Religious Traditions:** 14 belief systems (broadest coverage found)
- **Paper Type:** Dataset | Evaluation
- **Dataset Size:** 14 sacred texts analyzed
- **Languages:** English (translated texts)
- **LLMs Tested:** N/A (uses NLP tools: lexical analysis, sentiment analysis, correlation)
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Analyzes sacred texts from 14 different belief systems using lexical, sentiment, and correlation assessment. Finds that despite archaic language complexity, sacred texts show similar themes, historical contexts, and emotional tones across cultures. Highlights culturally-specific terms and explores depictions of fauna and flora revealing spatio-temporal influences. Broadest multi-religion NLP comparative analysis found, though uses traditional NLP rather than LLM evaluation.

---

### 15. How Much of a Pluralist is ChatGPT? A Comparative Study of Value Pluralism in Generative AI Chatbots
- **Authors:** Not fully identified in search (lead researcher published in AI & SOCIETY)
- **Year:** 2025
- **Venue:** AI & SOCIETY (Springer)
- **arXiv:** N/A
- **DOI:** 10.1007/s00146-025-02450-3
- **Religious Traditions:** Cross-religious (pluralism across faith and moral positions)
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** Magic Wand Survey instrument measuring 2 pluralism dimensions
- **Languages:** English
- **LLMs Tested:** ChatGPT 4o, Gemini 1.5 Pro, and other chatbots
- **Code/Data:** N/A
- **Implementation Readiness:** MEDIUM
- **Source Agent(s):** R9

**Summary:** Introduces pluralism as a benchmark metric for AI chatbots using the "Magic Wand Survey" measuring cognitive pluralism (recognizing multiple perspectives) and behavioral pluralism (willingness to preserve difference). Chatbots show higher cognitive than behavioral pluralism; cognitive pluralism exceeds human levels but behavioral pluralism is lower on morally charged issues. Gemini 1.5 Pro most pluralistic; ChatGPT 4o the least. Directly relevant to multi-faith AI evaluation.

---

### 16. DweshVaani: An LLM for Detecting Religious Hate Speech in Code-Mixed Hindi-English
- **Authors:** Multiple (not fully specified in search; published at CHiPSAL 2025)
- **Year:** 2025
- **Venue:** CHiPSAL 2025 Workshop (co-located with COLING 2025, Abu Dhabi)
- **arXiv:** N/A
- **DOI:** N/A (ACL Anthology: 2025.chipsal-1.5)
- **Religious Traditions:** Hinduism, Islam (religious hate speech in Indian context)
- **Paper Type:** Benchmark | Dataset | Evaluation
- **Dataset Size:** Religious hate speech corpus in code-mixed Hindi-English
- **Languages:** Hindi-English code-mixed
- **LLMs Tested:** Gemma-2 (fine-tuned as DweshVaani), Meta LLMs, Google LLMs, OpenAI, Nvidia, Sarvam, Indic-Gemma, Airavata
- **Code/Data:** N/A
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Presents DweshVaani, a fine-tuned Gemma-2 model for detecting religious hate speech and identifying targeted religions in code-mixed Hindi-English. Benchmarks cutting-edge LLMs (Meta, Google, OpenAI, Nvidia) and Indic-specific LLMs (Sarvam, Indic-Gemma, Airavata). Finds that Indic-LLMs instruction-tuned on Indian content underperform. Uses knowledge-distillation based fine-tuning with rationale extraction to improve performance.

---

### 17. FaithBench: AI Benchmark for Christian Theology
- **Authors:** Not fully specified (independent research initiative)
- **Year:** 2025
- **Venue:** Independent benchmark (faithbench.com)
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity (Reformed, Catholic, Pentecostal, Orthodox theological traditions)
- **Paper Type:** Benchmark
- **Dataset Size:** 300+ test cases across 6 dimensions, 4 difficulty tiers, 100+ expert-level GPQA-style questions
- **Languages:** English
- **LLMs Tested:** Multiple leading LLMs (evaluation methodology available on request)
- **Code/Data:** https://faithbench.com/
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** First rigorous peer-review-quality benchmark for evaluating AI models on Christian theology, apologetics, and biblical scholarship. Contains 300+ test cases across 6 dimensions including biblical scholarship (original languages, manuscript traditions), doctrinal development, and patristic sources. Expert-level questions use multi-hop reasoning that cannot be solved by simple retrieval. Anti-gaming design with held-out test cases. Distinguishes between theological traditions (e.g., Reformed vs Catholic soteriology).

---

### 18. Flourishing AI Christian (FAI-C) Benchmark
- **Authors:** Gloo / Elizabeth Hilliard et al.
- **Year:** 2025
- **Venue:** Gloo Research (industry benchmark; underlying FAI paper at arXiv 2507.07787 already in vault)
- **arXiv:** N/A (FAI-C specifically; base FAI is 2507.07787, already in vault)
- **DOI:** N/A
- **Religious Traditions:** Christianity
- **Paper Type:** Benchmark
- **Dataset Size:** 807 curated questions across 7 dimensions
- **Languages:** English
- **LLMs Tested:** 28+ LLMs including Qwen3 235B (top scorer at 70/100), DeepSeek, GPT-4, Claude
- **Code/Data:** https://gloo.com/flourishing-hub/research
- **Implementation Readiness:** HIGH
- **Source Agent(s):** R9

**Summary:** Extension of the Flourishing AI Benchmark (already in vault as "Measuring AI Alignment with Human Flourishing") specifically for Christian worldview evaluation. Tests 807 prompts using Christian reasoning judge personas across Character, Relationships, Happiness, Meaning, Health, Finances, and Faith dimensions. Models average 61/100 with Faith dimension being weakest (avg 48). Models replace Christian-specific language with generic terms ("higher power" for God, "mindfulness" for prayer). Note: Base FAI paper already in vault; FAI-C is a distinct Christian-specific extension.

---

### 19. AI Christian Benchmark (The Gospel Coalition)
- **Authors:** The Gospel Coalition (TGC) team; evaluated by 7 orthodox theologians
- **Year:** 2025
- **Venue:** The Gospel Coalition / Rotation.org
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** Christianity
- **Paper Type:** Benchmark | Evaluation
- **Dataset Size:** 7 most-Googled religious questions x 7 LLMs x 7 theologians
- **Languages:** English
- **LLMs Tested:** 7 popular LLMs including DeepSeek R1, Perplexity
- **Code/Data:** https://www.thegospelcoalition.org/ai-christian-benchmark/
- **Implementation Readiness:** LOW
- **Source Agent(s):** R9

**Summary:** Community benchmark testing 7 LLMs on 7 frequently asked religious questions, graded by 7 theologians. DeepSeek R1 scored highest for theological accuracy, with Perplexity in second place. Hypothesizes that models with less human alignment intervention may perform better on religious prompts, as RLHF may introduce secular bias. Small scale but notable for expert theological evaluation methodology.

---

### 20. Faith, Respect, and Moral Compass in an Age of Artificial Intelligence (Pluralistic Community AI Evaluation)
- **Authors:** Gerrit W. Gong et al. (interfaith coalition initiative)
- **Year:** 2025
- **Venue:** Presented at Vatican City; multi-institutional initiative
- **arXiv:** N/A
- **DOI:** N/A
- **Religious Traditions:** All major faith traditions (pluralistic, non-privileging)
- **Paper Type:** Framework | Benchmark (in development)
- **Dataset Size:** In development (protocols and benchmarks being established)
- **Languages:** Multilingual (goal)
- **LLMs Tested:** In development
- **Code/Data:** In development (collaborating with BYU, Notre Dame, Baylor, Yeshiva)
- **Implementation Readiness:** LOW (early stage)
- **Source Agent(s):** R9

**Summary:** Ambitious pluralistic initiative to benchmark AI accuracy and respect across diverse faith traditions. Evaluation criteria: Faith faithful, Accurate/expert, Child appropriate, Pluralism aware, Resistant to dilution, Human centered, Multilingual. In conversation with major universities (Baylor, BYU, Notre Dame, Yeshiva) and "socially-responsible frontier model AI companies." Does not privilege any faith tradition or belief over nonbelief. Still in development but represents the most comprehensive interfaith benchmark effort found.

---

## Papers EXCLUDED (Already in Vault or Found by R1-R5)

The following papers were identified during search but excluded because they already exist in the vault dedup reference:

1. **BRAND: Bilingual Religious Accountable Norm Dataset** (arXiv 2512.03943) -- Already in vault
2. **WorldView-Bench** (arXiv 2505.09595) -- Already in vault
3. **Decolonial AI Alignment: Openness, Visesa-Dharma, and Including Excluded Knowledges** (arXiv 2309.05030) -- Already in vault
4. **Measuring AI Alignment with Human Flourishing** (arXiv 2507.07787) -- Already in vault (base FAI benchmark; FAI-C Christian extension listed as Paper 18)
5. **Contemplative Artificial Intelligence** -- Already in vault
6. **GurbaniDB** -- Already in vault (R3 territory)
7. **Humanistic Buddhism Corpus (HBC)** -- Already in vault (R4 territory)
8. **PalmX 2025** -- Already in vault (R1 territory)
9. **Aftina: Arabic Fatwa QA** -- Already in vault (R1 territory)
10. **IslamicEval 2025** -- Already in vault (R1 territory)
11. **Fine-tuning BERT for Islamic Moral Inquiry** -- Already in vault (R1 territory)
12. **Finding Answers from the Word of God** (BibleQA) -- Already in vault (R2 territory)

---

## Summary Statistics

### Total Papers Found: 20

### Breakdown by Religious Tradition Coverage
| Tradition | Papers Covering It |
|-----------|-------------------|
| Islam | 9 (Papers 2,3,4,5,8,9,12,15,16) |
| Christianity | 8 (Papers 1,2,5,6,8,9,13,17,18,19) |
| Hinduism | 6 (Papers 1,2,4,5,8,13,16) |
| Buddhism | 5 (Papers 1,2,4,5,8) |
| Judaism | 4 (Papers 1,4,5,9) |
| Sikhism | 2 (Papers 2,9) |
| Multiple/Interfaith | 7 (Papers 7,10,11,14,15,20) |
| Zoroastrianism | 0 |
| Baha'i | 0 |
| Jainism | 0 (only tangentially in Decolonial AI, already in vault) |
| Tengrism | 0 |
| Rastafari | 0 |

### Breakdown by Paper Type
| Type | Count |
|------|-------|
| Benchmark | 8 |
| Evaluation | 13 |
| Bias Study | 7 |
| Dataset | 5 |
| Framework | 3 |

(Note: Papers can have multiple types)

### Breakdown by Implementation Readiness
| Readiness | Count |
|-----------|-------|
| HIGH | 7 (Papers 1, 3, 4, 5, 16, 17, 18) |
| MEDIUM | 10 (Papers 2, 6, 7, 8, 9, 11, 12, 13, 14, 15) |
| LOW | 3 (Papers 10, 19, 20) |

---

## Key Observations and Gaps

### Critical Gaps Identified

1. **Zoroastrianism**: Zero NLP/LLM papers found. No Avesta datasets, no benchmark, no evaluation. Complete research vacuum. The Avesta Archives exist digitally but no computational work has been done on them for LLM evaluation.

2. **Baha'i**: Zero AI benchmark/evaluation papers found. The Wilmette Institute has published informal reflections on AI ethics from a Baha'i perspective, but no dataset, benchmark, or LLM evaluation exists.

3. **Jainism**: Zero dedicated AI/LLM papers found. The Decolonial AI Alignment paper (already in vault) mentions Jain philosophy tangentially alongside Hindu and Buddhist nAstika traditions, but no benchmark tests LLMs on ahimsa, anekantavAda, or other Jain concepts.

4. **Tengrism**: Zero papers found. No NLP, no dataset, no AI evaluation.

5. **Rastafari**: Zero AI/NLP benchmark papers found. One presentation by KET-A Williams explores Rastafari perspectives on AI personhood but provides no benchmark or dataset.

6. **Sikhism AI benchmarks**: While GurbaniDB and KhalsaGPT exist as tools, no rigorous LLM evaluation benchmark for Sikh knowledge/values was found. Scholarly work by Devinder Pal Singh on AI and Sikh pedagogy exists but lacks formal benchmarking.

### Structural Observations

1. **Islam dominance**: Islamic QA/benchmark papers vastly outnumber all other religious traditions combined, driven by Arabic NLP community investment and specific needs (fatwa systems, Quranic studies, Hadith QA).

2. **Christianity emerging**: Two industry benchmarks (FaithBench, FAI-C) and one community benchmark (TGC) appeared in 2025, signaling growing Christian community investment in AI evaluation.

3. **Multi-religion comparative work is rare**: Most papers study one religion or compare only 2-3 major traditions. The broadest coverage found (Paper 14) analyzes 14 belief systems but uses traditional NLP, not LLM evaluation.

4. **CLREL Workshop (COLING 2025)**: The first dedicated workshop on "Computational Linguistics for Religious Texts" was held in January 2025 in Abu Dhabi, signaling institutional recognition of this research area.

5. **Pluralistic evaluation gaining traction**: Papers 15 and 20 represent emerging methodologies for evaluating AI across multiple faith traditions without privileging any single one.

6. **Bias detection >> value alignment**: Most multi-religion papers focus on detecting bias (especially anti-Muslim bias) rather than testing alignment with religious values. Value alignment benchmarks remain largely tradition-specific.

7. **Language gap**: Nearly all work is English-only or English+Arabic. Religious traditions with primary texts in other scripts (Sanskrit, Pali, Avestan, Gurmukhi) lack computational evaluation infrastructure.
