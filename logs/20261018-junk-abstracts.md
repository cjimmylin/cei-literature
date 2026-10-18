# 20261018 — Replace web-search tool output stored as `abstract`

57 notes (325-paper cultural batch of 2026-04-04, plus a few others) had an `abstract` that is the
output of a web-search tool ("I've completed the web search for…", "Based on the search results…",
"根据搜索结果…"), not an abstract. None of the metadata services (Semantic Scholar, OpenAlex, arXiv,
Crossref) is reachable from the session that did this, so only the papers' own PDF extracts were used.

## Replaced: 13, verbatim from the paper's own PDF extract

Rule: only when the extract is the same work as the note and has an abstract (labelled, or the
standard unlabelled abstract block of a Nature/Scientific Reports/Frontiers title page). Text copied
as is; only line-break hyphens, ligatures (ﬁ→fi), page headers/footers and one footnote mark removed.
Each line round-trips through a YAML parser to exactly the extracted text.

| Note | Source extract |
|------|----------------|
| `2024-Aly-Hate speech detection with ADHAR a multi-dialectal hate speech corpus.md` | `PDF Extracts/2024/2024-Aly-Hate speech detection with ADHAR a multi-dialectal hate speech corpus.md` |
| `2024-Enkhbold-A new dataset for mongolian online handwritten recognition.md` | `PDF Extracts/2024/2024-Enkhbold-A new dataset for mongolian online handwritten recognition.md` |
| `2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in.md` | `PDF Extracts/2024/2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in.md` |
| `2025-Durmus-Towards Measuring the Representation of Subjective Global Opinions in.md` | `PDF Extracts/2025/2025-Durmus-Towards Measuring the Representation of Subjective Global Opinions in.md` |
| `2025-Flek-AmericasNLI Machine translation and natural language inference.md` | `PDF Extracts/2025/2025-Flek-AmericasNLI Machine translation and natural language inference.md` |
| `2025-Hossain-Beyond Neutrality A Comprehensive Approach of Religious Bias.md` | `PDF Extracts/2025/2025-Hossain-Beyond Neutrality A Comprehensive Approach of Religious Bias.md` |
| `2025-Lin-Machine translation of Chinese classical poetry a comparison among.md` | `PDF Extracts/2025/2025-Lin-Machine translation of Chinese classical poetry a comparison among.md` |
| `2025-Pretrained-Evaluating Uighur literary translation A comparative study of ChatGPT.md` | `PDF Extracts/2025/2025-Pretrained-Evaluating Uighur literary translation A comparative study of ChatGPT.md` |
| `2025-Pretrained-Graphic Language Model for Agglutinative Languages Uyghur as Study.md` | `PDF Extracts/2025/2025-Pretrained-Graphic Language Model for Agglutinative Languages Uyghur as Study.md` |
| `2025-Saleh-Frontiers Evaluating large language models a systematic review of.md` | `PDF Extracts/2025/2025-Saleh-Frontiers Evaluating large language models a systematic review of.md` |
| `2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..md` | `PDF Extracts/2025/2025-Snoswell-Beyond Verdicts Evaluating Language Model Moral Competence Aaron J..md` |
| `2025-Unknown-Frontiers Cross-dialectal Arabic translation comparative analysis on.md` | `PDF Extracts/2025/2025-Unknown-Frontiers Cross-dialectal Arabic translation comparative analysis on.md` |
| `2025-Unknown-Sentiment analysis in multilingual context Comparative analysis of.md` | `PDF Extracts/2025/2025-Unknown-Sentiment analysis in multilingual context Comparative analysis of.md` |

Metadata problems seen while checking (not changed): the notes credit the wrong first author for
ADHAR (note "Aly", paper Charfi et al.), the Mongolian handwriting dataset (note "Enkhbold", paper
Pan et al., *Scientific Reports* 2023, note year 2024) and the multi-modal hate-speech framework
(note "Kajiwara", paper Prabhu & Seethalakshmi).

## Not replaced: 44

**9 have a PDF extract but no usable abstract:**

- `2022-Korir-LREC 2022 Workshop Language Resources and Evaluation Conference 20-25.md`: the PDF is a whole workshop proceedings (CLTW 2022, many papers); there is no single abstract
- `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata.md`: WRONG PDF: the note is the hatespeechdata.com website, its extract is a different paper (Caselli et al., AbuseEval v1.0, LREC 2020)
- `2025-Cheng-Large Language Model Generate Prompt 生成式大模型 安全评估白皮书.md`: white paper with a preface (前言) but no abstract
- `2025-Kajiwara-INHS Newsletter May 2025 - The International Network for Hate ....md`: monthly newsletter, no abstract
- `2025-Ku-Chinese Textual Sentiment Analysis Datasets Resources and Tools.md`: COLING 2016 tutorial description, no abstract section
- `2025-MIIT-1 工业和信息化领域人工智能安全治理标准体系 建设指南（2025） （征求意见稿） 为深入贯彻落实党中央、国务院关于加快发展人工智能.md`: government standards guideline (draft for comment), no abstract
- `2025-Translation-Evaluation Criteria for Literary Translation.md`: short essay with no abstract
- `2025-Unknown-Indigenous Peoples and AI Defending Rights Shaping the Future of.md`: UN DESA event concept note, no abstract
- `2025-Unknown-Is ChatGPT A Good Translator A Preliminary Study.md`: WRONG PDF: the extract is a different paper ("Is ChatGPT a Good NLG Evaluator? A Preliminary Study", Wang et al. 2023), not Jiao et al.'s translator study

**35 have no PDF extract.** Their abstracts need a metadata source (allow api.semanticscholar.org,
api.openalex.org, export.arxiv.org or api.crossref.org in the environment's network settings) or the
owner. Several are web pages, dataset listings or blog posts with no abstract at all.

- `2024-Charfi-Available hate speech datasets for Arabic. Download Scientific Diagram.md`
- `2024-Demidova-dblp ArabicNLP 2024.md`
- `2024-Duwairi-A Deep Learning Framework for Automatic Detection of Hate Speech.md`
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset.md`
- `2024-Veitsman-The Development and Experimental Evaluation of a Multilingual Speech.md`
- `2025-Aji-Multilingual Multicultural Evaluation Workshop.md`
- `2025-Alkhushayni-Multilingual Sentiment Analysis with Data Augmentation A.md`
- `2025-Binegde-Exploring cultural commonsense in multilingual large language models.md`
- `2025-Corbett-AI and Indigenous Languages.md`
- `2025-Demidova-SIGARAB - Arabic NLP Archives.md`
- `2025-Dilnigar-Uyghur Poetry in Translation Perhat Tursun’s “Elegy” – Fairbank.md`
- `2025-Durmus-Subjective Values.md`
- `2025-Hulagadri-Towards fair and comprehensive multilingual LLM benchmarking SEA-LION.md`
- `2025-Jain-Low-Resource NLP Challenges Breakthroughs and the Science Behind.md`
- `2025-Jiang-Preserving the Past AI in Indigenous Language Preservation - Viterbi.md`
- `2025-Jigsaw-Jigsaw Multilingual Toxic Comment Classification.md`
- `2025-Jim-Recent advancements and challenges of NLP-based sentiment analysis A.md`
- `2025-Korir-API Multilingual & Multicultural Resources - Asian Pacific Islander.md`
- `2025-Lim-How Do Users Identify and Perceive Stereotypes Understanding User.md`
- `2025-Liu-Cultural Bias in Large Language Models A Comprehensive Analysis and.md`
- `2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics.md`
- `2025-Perez-Tokenising culture causes and consequences of cultural misalignment.md`
- `2025-Shi-Benchmarking four large language models’ performance of addressing.md`
- `2025-Sun-Evaluating the Translation Accuracy of ChatGPT and DeepL Through the.md`
- `2025-Unknown-ArabicNLP 2025.md`
- `2025-Unknown-Benchmarking Large Language Models for fairness across diverse.md`
- `2025-Unknown-Indigenous Futures in Artificial Intelligence From Language.md`
- `2025-Unknown-Multilingual NLP Code-Switching Variants & Dialects Appen.md`
- `2025-Unknown-New Guidelines for Evaluating Literary Translation in Hiring and.md`
- `2025-Unknown-New report and guidelines for indigenous data sovereignty in.md`
- `2025-Unknown-中文大模型内容安全测评基准DSPSafeBench上线，首批模型测评结果揭晓！_中文大模型内容安全测评基准dspsafebench-CSDN.md`
- `2025-Wenzek-CC100-Mongolian dataset - NLP Database.md`
- `2025-Xiang-Diagnosing the bias iceberg in large language models A three-level.md`
- `2025-Đokić-Mirroring Cultural Dominance Disclosing Large Language Models Social.md`
- `2026-Unknown-Arabic LLMs for Banking Telecom and Government in GCC - 2026.md`
