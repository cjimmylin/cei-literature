# 20261018 — Replace web-search tool output stored as `abstract`

**Totals:** 81 notes had tool output as `abstract` (57 found first, 24 more with other wording in a second pass).
21 now have the paper's own abstract from its PDF extract; 60 are cleared (`abstract: `).

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

## Author, year and PDF fixes (owner-approved)

Found while checking the extracts; corrected from the papers' own PDFs (single-line edits, filenames unchanged):

- `2024-Aly-Hate speech detection with ADHAR…`: authors were "Ranwa Aly; Yara Allam; Rana Gaber"; the paper
  is by Anis Charfi, Mabrouka Besghaier, Raghda Akasheh, Andria Atalla and Wajdi Zaghouani (Front. Artif. Intell. 2024).
- `2024-Enkhbold-A new dataset for mongolian…`: authors were "Enkhbold"; the paper is by Yuecai Pan, Daoerji Fan,
  Huijuan Wu and Da Teng; `year` 2024 → 2023 (*Scientific Reports* (2023) 13:26). The filename prefix still says 2024.
- `2024-Kajiwara-A comprehensive framework for multi-modal…`: authors were "Kajiwara"; the paper is by R. Prabhu and
  V. Seethalakshmi; `year` 2024 → 2025 (*Scientific Reports* (2025) 15:13020). The filename prefix still says 2024.
- `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata` and `2025-Unknown-Is ChatGPT A Good Translator A
  Preliminary Study`: their PDF was a different paper. `local_pdf` → N/A, `pdf_extract` emptied, the wrong extracts
  moved to `RECYCLE-BIN/20261018-wrong-pdf-extracts/`, and the catalogue note's `external_pdf` (which pointed at the
  AbuseEval paper on the LREC site) → N/A. The wrong PDF files themselves are in the owner's PDF folder, outside the repo,
  under those two notes' names. These notes' v14 classifications were made partly from the wrong text.

## Not replaced: 44, junk text cleared (owner decision)

Their `abstract` is now empty (`abstract: `), so the dashboard and keyword scorers stop reading tool output. The lists below are kept for a later fetch.

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

## Second pass: 24 more with other wording

Wording such as "Based on the web search results, here's what I found…", "I've performed a web search…",
"Here are the search results for…", "The search results reveal…". Same rules as above.

**Replaced from the PDF extract (8):**

| Note | Source extract |
|------|----------------|
| `2025-Davies-Exploring the occupational biases and stereotypes of Chinese large.md` | `PDF Extracts/2025/2025-Davies-Exploring the occupational biases and stereotypes of Chinese large.md` |
| `2025-Davies-Fairness identification of large language models in recommendation.md` | `PDF Extracts/2025/2025-Davies-Fairness identification of large language models in recommendation.md` |
| `2025-Hackett-Bypassing LLM guardrails character and AML attacks in practice -.md` | `PDF Extracts/2025/2025-Hackett-Bypassing LLM guardrails character and AML attacks in practice -.md` |
| `2025-Masood-A survey of multilingual large language models - PMC.md` | `PDF Extracts/2025/2025-Masood-A survey of multilingual large language models - PMC.md` |
| `2025-Oh-Evaluating LLMs’ Language Confusion in Code-switching Context Juhyun.md` | `PDF Extracts/2025/2025-Oh-Evaluating LLMs’ Language Confusion in Code-switching Context Juhyun.md` |
| `2025-Unknown-A survey on multi-lingual offensive language detection - PMC.md` | `PDF Extracts/2025/2025-Unknown-A survey on multi-lingual offensive language detection - PMC.md` |
| `2025-Yan-Decolonizing African NLP A Survey on Power Dynamics and Data.md` | `PDF Extracts/2025/2025-Yan-Decolonizing African NLP A Survey on Power Dynamics and Data.md` |
| `2025-approach-A Language model-based approach to sentiment classification of.md` | `PDF Extracts/2025/2025-approach-A Language model-based approach to sentiment classification of.md` |

**Cleared (16)**: no extract, or an extract without an abstract (AmericasNLP 2025 call for papers;
Ogunremi et al. essay):

- `2024-Kuriyozov-Construction and Evaluation of Sentiment Datasets for Low-Resource.md`
- `2024-Unknown-A structured sentiment analysis dataset based on public comments from.md`
- `2025-Ablimit-A multilingual language processing tool for Uyghur Kazak and Kirghiz.md`
- `2025-Aly-Applying Data Feminism Principles to Assess Bias in English and.md`
- `2025-DeWitt Prat-Decolonizing LLMs An Ethnographic Framework for AI in African.md`
- `2025-Firmino-Improving hate speech detection using Cross-Lingual Learning -.md`
- `2025-Jailbreak-The Hidden Flaw in LLM Safety Translation as a Jailbreak - Welo Data.md`
- `2025-Mager-Thrid Workshop on NLP for Indigenous Languages of the Americas.md`
- `2025-Masood-Large language models are biased - local initiatives are fighting for.md`
- `2025-Moosa-Multi-lingual HateSpeech Dataset.md`
- `2025-Ogunremi-1 Decolonizing NLP for “Low-resource Languages”.md`
- `2025-Pretrained-Research on the Training and Application Methods of a Lightweight.md`
- `2025-Salve-Bilingual Code-Switching Using XLM-RoBERTa.md`
- `2025-Soria-Decolonizing Minority Language Technology - State of the Internet's.md`
- `2025-Unknown-An Overview of Chinese Open-Source LLMs Sept 2025 IntuitionLabs.md`
- `2025-Xiangfeng-A dataset of Mongolian Tibetan and Uyghur speech fragments based on.md`

**Authors corrected from the PDFs** (same kind of error as above): both `2025-Davies-…` notes credited
"Dave Davies"; the papers are by Leilei Jiang, Guixiang Zhu, Jianshan Sun, Jie Cao and Jia Wu
(*Sci. Rep.* (2025) 15:18777) and by Wei Liu, Baisong Liu, Jiangcheng Qin, Xueyuan Zhang, Weiming Huang and
Yangyang Wang (*Sci. Rep.* (2025) 15:5516).

**Probably the same mix-up, not changed** (first author "Dave Davies", "Kajiwara" or "Enkhbold"; check against
each paper):

- `2024-Enkhbold-Text and Value Mongolian Journal of Humanities and Social Sciences.md`
- `2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC.md`
- `2024-Kajiwara-Beyond Traditional Classifiers Evaluating Large Language Models for.md`
- `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata.md`
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset.md`
- `2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural.md`
- `2024-Kajiwara-Validating Pseudo-label Dataset for Japanese Hate Speech Detection.md`
- `2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ....md`
- `2025-Davies-LLM Evaluation Benchmarks and Safety Datasets for 2025 Knowledge Hub.md`
- `2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark.md`
- `2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation.md`
- `2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the.md`
- `2025-Kajiwara-INHS Newsletter May 2025 - The International Network for Hate ....md`
- `2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit.md`

## Body copies

89 notes also repeated the tool output as the one line under `## Abstract` in the note body. That line now matches
the frontmatter: the real abstract in 35 notes, empty in 54 (heading kept). No other body text changed.

## The 14 "Dave Davies" / "Kajiwara" / "Enkhbold" notes (owner-approved check)

Origin of the mix-up: web-search output stored in these notes says a 2024 paper is by "Kajiwara and Sakurai", and
that name was copied as author into unrelated notes; "Dave Davies" and "Enkhbold" look like the same pattern.

**Fixed from the paper's own PDF extract (8)** — `first_author`, `last_author`, `authors` and the body's author lines:

- `2024-Enkhbold-Text and Value Mongolian Journal of Humanities and Social Sciences.md`: Гүрринчингийн Сүхбат
- `2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural.md`: Sinéad Walsh; Paul Greaney
- `2025-Davies-F2Bench An Open-ended Fairness Evaluation Benchmark ....md`: Tian Lan; Jiang Li; Yemin Wang; Xu Liu; Xiangdong Su; Guanglai Gao
- `2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark.md`: Haitao Li; You Chen; Qingyao Ai; Yueyue Wu; Ruizhe Zhang; Yiqun Liu
- `2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation.md`: Yizhi Li; Ge Zhang; Hanhua Hong; Yiwen Wang; Chenghua Lin
- `2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the.md`: Santosh Chapagain; Shah Muhammad Hamdi; Soukaina Filali Boubrahimi
- `2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit.md`: Hongliu Cao; Eoin Thomas; Rodrigo Acuna Agost
- `2025-Kajiwara-INHS Newsletter May 2025 - The International Network for Hate ....md`: International Network for Hate Studies

**Wrong PDF (1)**, unlinked like the two above (extract moved to `RECYCLE-BIN/20261018-wrong-pdf-extracts/`,
`local_pdf`/`external_pdf` → N/A): `2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC.md`
(its PDF was "A Comprehensive Study of Gender Bias in Chemical Named Entity Recognition Models", Zhao et al., arXiv 2212.12799).

**Not changed, no evidence in the vault (6):**

- `2024-Kajiwara-Beyond Traditional Classifiers Evaluating Large Language Models for.md`: no PDF extract (MDPI Computation 13(8):196)
- `2024-Kajiwara-Hate Speech Dataset Catalogue hatespeechdata.md`: website; no extract (its PDF was a different paper, unlinked)
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset.md`: Kaggle dataset page; no extract
- `2024-Kajiwara-Validating Pseudo-label Dataset for Japanese Hate Speech Detection.md`: no extract; this IEEE paper may really be by Kajiwara (likely where the name came from)
- `2025-Davies-LLM Evaluation Benchmarks and Safety Datasets for 2025 Knowledge Hub.md`: web article; no extract (Dave Davies may be its real author)
- `2024-Kajiwara-A curated dataset for hate speech detection on social media text - PMC.md`: its PDF was a different paper (gender bias in chemical NER, Zhao et al.); unlinked; real authors not in the vault

**Year discrepancies noticed (not changed):**

- `2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark.md`: NeurIPS 2024 Datasets & Benchmarks paper; note year 2025 (not changed)
- `2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural.md`: Natural Language Processing (2025) 31, doi 10.1017/nlp.2024.62; note year 2024 (not changed)
