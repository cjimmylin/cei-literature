# lm-eval-harness Implementability Report
Generated: 2026-03-12

## Executive Summary

| Tier | Count | % of Scored |
|------|-------|-------------|
| Already in Harness | 65 | 3.3% |
| Ready to Implement | 178 | 8.9% |
| Needs Dataset Hosting | 413 | 20.8% |
| Needs More Info | 580 | 29.1% |
| Not Implementable | 754 | 37.9% |
| **Total Scored** | **1990** | |

**PDF Extracts Analyzed:** 2035 across 2016-2026
**Survey Entries Cross-Referenced:** 986 (70 matched to harness)
**Known Harness Tasks:** 49

## 1. Already in lm-eval-harness (65 papers)

| Paper | Year | Harness Task | Match Method | Availability |
|-------|------|-------------|--------------|--------------|
| 2025-Kasu-EthicsMH | 2025 | `ethics_cm` | substring | Public |
| 2024-Li-Benchmarking Ethics in Text-to-Image Models | 2024 | `ethics_cm` | substring | Public (benchmark dataset and ImageGuard evaluator) |
| 2025-Ruiz-Fernández-EsBBQ and CaBBQ | 2025 | `bbq` | substring | Not stated |
| 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models | 2024 | `truthfulqa` | substring | Public |
| 2025-Zulaika-BasqBBQ Basque BBQ | 2025 | `bbq` | substring | Not stated |
| 2016-Bolukbasi-Man is to Computer Programmer as Woman is to | 2016 | `weat` | substring | Public |
| 2020-Awad-Universals and variations in moral decisions made | 2020 | `moral_machine` | substring | Public |
| 2020-Gehman-RealToxicityPrompts | 2020 | `realtoxicityprompts` | exact | Public |
| 2021-Emelin-Moral Stories | 2021 | `moral_stories` | filename | Public |
| 2021-Hansson-The Swedish Winogender Dataset SweWinogender | 2021 | `winogender` | substring | Public |
| 2021-Hendrycks-Aligning AI with Shared Human Values | 2021 | `ethics_cm` | exact | Public |
| 2023-Jiang-MACHIAVELLI | 2023 | `machiavelli` | exact | Public |
| 2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian | 2024 | `ethics_cm` | substring | Public (https://mera.a-ai.ru/en) |
| 2026-Goel-Building Interpretable Models for Moral Decision-Making | 2026 | `moral_machine` | substring | Public |
| 2021-Nadeem-StereoSet | 2021 | `stereoset` | exact | Public |
| 2024-Ng-SGHateCheck Functional Tests for Detecting Hate Speech in | 2024 | `hatecheck` | substring | Public |
| 2024-Quang-Vietnamese Law and Ethics Multiple-Choice Questions VLEMCQ | 2024 | `ethics_cm` | substring | Public |
| 2025-Zhang-LLMEval-Med Medical Safety & Ethics Component | 2025 | `ethics_cm` | substring | Public |
| 2018-Awad-The Moral Machine experiment | 2018 | `moral_machine` | exact | Public |
| 2021-Dhamala-BOLD | 2021 | `bold` | substring | Public |
| 2022-Hartvigsen-ToxiGen | 2022 | `toxigen` | exact | Public |
| 2022-Hendrycks-What Would Jiminy Cricket Do | 2022 | `jiminy_cricket` | exact | Public |
| 2024-Adelani-Uhura A Benchmark for Evaluating Scientific | 2024 | `truthfulqa` | substring | Unknown |
| 2024-Chern-BeHonest | 2024 | `honest` | substring | Public (https://github.com/GAIR-NLP/BeHonest) |
| 2024-Huang-CBBQ | 2024 | `bbq` | substring | Public (https://anonymous.4open.science/r/CBBQ-B860/) |
| 2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of | 2024 | `ethics_cm` | substring | Not stated |
| 2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030 | 2025 | `ethics_cm` | substring | Not stated |
| 2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred | 2018 | `equity_evaluation_corpus` | substring | Public |
| 2024-Gupta-WalledEval | 2024 | `xstest` | substring | Public (https://github.com/walledai/walledeval) |
| 2024-Hancox-Li-Is ETHICS about ethics | 2024 | `ethics_cm` | substring | Public |
| 2025-Jiao-LLM Ethics Benchmark | 2025 | `ethics_cm` | substring | Public |
| 2022-Parrish-BBQ Bias Benchmark for Question Answering | 2022 | `bbq` | substring | Public (GitHub: nyu-mll/BBQ; HuggingFace: heegyu/bbq, walledai/BBQ) |
| 2022-Parrish-BBQ | 2022 | `bbq` | substring | Public |
| 2024-Yanaka-JBBQ | 2024 | `bbq` | substring | Public (https://github.com/ynklab/JBBQ_data) |
| 2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics | 2025 | `ethics_cm` | substring | Public |
| 2025-Takeshita-JETHICS | 2025 | `ethics_cm` | substring | Public |
| 2025-Wei-MedEthicsQA | 2025 | `ethics_cm` | substring | Public |
| 2026-Shen-PsychEthicsBench | 2026 | `ethics_cm` | substring | Public |
| 2022-Das-HateCheckHIn Evaluating Hindi Hate Speech Detection | 2022 | `hatecheck` | substring | Public |
| 2024-Freire-Uncovering Latent Human Wellbeing in Language | 2024 | `ethics_cm` | substring | Not stated |
| 2025-Flores-BenchMoral | 2025 | `moral_permissibility` | filename | Not stated |
| 2025-Leteno-Histoires Morales | 2025 | `histoires_morales` | filename | Public |
| 2020-Nangia-CrowS-Pairs | 2020 | `crows_pairs` | exact | Public |
| 2024-Liang-Cross-Language Bias Examination in Large Language Models | 2024 | `bbq` | substring | Unknown |
| 2025-Menke-How Effective Is Constitutional AI in Small LLMs | 2025 | `ethics_cm` | substring | Not stated |
| 2024-Karpov-Inducing Human-like Biases in Moral Reasoning | 2024 | `ethics_cm` | substring | Not stated |
| 2025-Ebara-Corpus-Based Medical Ethics Decision-Making Evaluation | 2025 | `ethics_cm` | substring | Not stated |
| 2025-Galea-From Measurement to Mitigation Exploring the Transferability of | 2025 | `crows_pairs` | substring | Unknown |
| 2025-Gamboa-Filipino Benchmarks for Measuring Sexist and Homophobic Bias in | 2025 | `crows_pairs` | substring | Unknown |
| 2023-Roger-Towards ethical multimodal systems | 2023 | `ethics_cm` | substring | Not stated |
| 2024-Vida-Decoding Multilingual Moral Preferences - Unveiling LLM's Biases | 2024 | `moral_machine` | substring | Not stated |
| 2022-Lin-TruthfulQA | 2022 | `truthfulqa_mc1` | filename |  |
| 2024-Bignotti-Legal Minds, Algorithmic Decisions | 2024 | `ethics_cm` | substring | Not stated |
| 2024-Jin-KoBBQ Korean Bias Benchmark for Question Answering | 2024 | `bbq` | filename |  |
| 2018-Zhao-Gender Bias in Coreference Resolution | 2018 | `winobias` | exact | Public |
| 2023-Qian-Understanding Chinese Moral Stories with Further | 2023 | `moral_stories` | filename | Public |
| 2025-Zohny-ADEPT Simulating Ethics | 2025 | `ethics_cm` | substring | Code |
| 2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for | 2025 | `ethics_cm` | substring | Unknown |
| 2024-Takemoto-The moral machine experiment on large language | 2024 | `moral_machine` | substring | Code available (supplementary materials) |
| 2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits | 2025 | `hhh_alignment` | filename |  |
| 2025-Wu-Chain-of-Ethics Defense Framework Wu et al. | 2025 | `ethics_cm` | substring | Not stated |
| 2025-Oh-Robustness of Large Language Models in Moral Judgements | 2025 | `moral_machine` | substring | Not stated |
| 2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social | 2025 | `crows_pairs` | substring | Unknown |
| 2025-Yoo-Moral Judgment of LLM Using Korean Datasets and Eastern Ethical | 2025 | `ethics_cm` | substring | Unknown |
| 2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML | 2022 | `ethics_cm` | substring | Not stated |

## 2. Ready to Implement (178 papers, score >= 65)

| # | Paper | Score | Benchmark | Type | Data URL | Key Signals |
|---|-------|-------|-----------|------|----------|-------------|
| 1 | 2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model | 100 | FrenchBench | classification | https://huggingface.co/croissantllm | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 2 | 2023-Wang-DecodingTrust | 100 | DecodingTrust | None | https://huggingface.co/datasets/AI-Secure/Decod... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 3 | 2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub | 100 | SEACrowd | generate_until | https://huggingface.co/SEACrowd | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 4 | 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs | 100 | AraDiCE / AraDiCE-Culture | qa | https://huggingface.co/datasets/QCRI/AraDiCE | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 5 | 2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering | 100 | AfriMed-QA | multiple_choice | https://huggingface.co/datasets/intronhealth/af... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 6 | 2024-Romanou-INCLUDE Evaluating Multilingual Language Understanding with Regional | 100 | INCLUDE | multiple_choice | https://huggingface.co/papers/2411.19799 | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 7 | 2024-Tam-An Improved Traditional Chinese Evaluation Suite for Foundation Model | 100 | TMMLU+ | qa | https://huggingface.co/datasets/ikala/tmmluplus | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 8 | 2024-Yuan-Social Measuring Social Norms of LLMs | 100 | Social (Social Norms Dataset) | generate_until | https://huggingface.co/datasets/socialnormdatas... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 9 | 2024-Baek-K-Viscuit Evaluating Visual and Cultural Interpretation with | 95 | K-Viscuit | multiple_choice | https://huggingface.co/datasets/ddehun/k-viscuit | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 10 | 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU | 95 | TMLU (Taiwanese Mandarin Language Understanding) | classification | https://huggingface.co/datasets/miulab/tmlu | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 11 | 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation | 95 | SailCompass | multiple_choice | https://huggingface.co/datasets/sail/Sailcompas... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 12 | 2024-Lee-KorNAT | 95 | KorNAT | multiple_choice | https://huggingface.co/datasets/datumo/KorNAT | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 13 | 2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic | 95 | AraTrust | ['multiple_choice'] | https://huggingface.co/datasets/asas-ai/AraTrust | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 14 | 2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and | 95 | CamelEval | qa | https://huggingface.co/elmrc | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 15 | 2024-Voukoutis-Meltemi The first open Large Language Model for Greek | 95 | Meltemi Greek Benchmark Suite | None | https://huggingface.co/ilsp/Meltemi-7B-v1 | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 16 | 2024-Zhang-ChineseSafe - A Chinese Benchmark for Evaluating Safety in LLMs | 95 | ChineseSafe | multiple_choice | https://huggingface.co/datasets/SUSTech/Chinese... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 17 | 2024-Jain-PolygloToxicityPrompts | 90 | PolygloToxicityPrompts (PTP) | generate_until | https://huggingface.co/datasets/ToxicityPrompts... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 18 | 2025-Chua-RabakBench | 90 | RabakBench | ['classification'] | https://huggingface.co/datasets/govtech/RabakBench | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 19 | 2025-Ji-PKU-SafeRLHF | 90 | PKU-SafeRLHF | ['qa', 'classification'] | https://huggingface.co/datasets/PKU-Alignment/P... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 20 | 2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain | 90 | Large-Scale Turkish-English Hate Speech Dataset | classification | https://huggingface.co/datasets/ctoraman/large-... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 21 | 2024-Park-Open Ko-LLM Leaderboard Evaluating Large Language Models in Korean | 90 | Ko-H5 / Open Ko-LLM Leaderboard | generate_until | https://huggingface.co/spaces/upstage/open-ko-l... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 22 | 2024-Tharnpipitchai-Typhoon 2 A Family of Open | 90 | Typhoon2-Safety / Thai Sensitive Topic Test Set | generate_until | https://huggingface.co/scb10x/typhoon2-safety-p... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 23 | 2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of | 90 | HateDay | None | https://huggingface.co/datasets/manueltonneau/h... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 24 | 2024-team-IndicLLMSuite A Blueprint for Creating Pre-training | 90 | IndicAlign-Toxic | None | https://huggingface.co/datasets/ai4bharat/indic... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 25 | 2025-Pandey-SocialHarmBench | 90 | SocialHarmBench | [] | https://huggingface.co/datasets/psyonp/SocialHa... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 26 | 2023-Kahira-AfriQA Cross-lingual Open-Retrieval Question Answering for | 87 | AfriQA | qa | https://huggingface.co/datasets/masakhane/afriqa | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 27 | 2023-Koto-Large Language Models Only Pass Primary School Exams in Indonesia A | 85 | IndoMMLU | qa | https://github.com/fajri91/IndoMMLU | Has DATA_URL, Public availability, Multiple-choice format |
| 28 | 2024-Brun-FrenchToxicityPrompts a Large Benchmark for Evaluating and Mitigating | 85 | FrenchToxicityPrompts | generate_until | https://huggingface.co/datasets/FrenchToxicityP... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 29 | 2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque | 85 | Latxa Evaluation Suite (EusProficiency, EusReading, EusTrivia, EusExams) | multiple_choice | https://github.com/hitz-zentroa/latxa | Has DATA_URL, Public availability, Multiple-choice format |
| 30 | 2024-Fajcik-BenCzechMark A Czech-centric Multitask and Multimetric Benchmark for | 85 | BenCzechMark (BCM) | multiple_choice | https://huggingface.co/BUT-FIT/CSTinyLlama-1.2B | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 31 | 2025-Azime-ProverbEval Exploring LLM Evaluation Challenges for Low-resource | 85 | ProverbEval | ['multiple_choice'] | https://huggingface.co/datasets/israel/ProverbEval | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 32 | 2021-Plaza-del-Arco-OffendES A New Corpus in Spanish for Offensive Language Research | 85 | OffendES | generate_until | https://huggingface.co/datasets/fmplaza/offendes | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 33 | 2023-Park-K-HATERS A Hate Speech Detection Corpus in Korean with | 85 | K-HATERS | multiple_choice | https://huggingface.co/jhgan/ko-sbert-multitask | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 34 | 2024-Singhal-AyaRedTeaming | 85 | AyaRedTeaming | generate_until | https://huggingface.co/datasets/CohereForAI/aya... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 35 | 2024-Team-WildGuard | 85 | WildGuard / WildGuardMix / WildGuardTest | None | https://huggingface.co/datasets/allenai/wildgua... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 36 | 2024-Tonneau-From Languages to Geographies Towards Evaluating Cultural Bias in | 85 | Spanish Hate Speech Superset | None | https://huggingface.co/datasets/manueltonneau/s... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 37 | 2025-Zbeeb-AraLingBench A Human-Annotated Benchmark for Evaluating Arabic | 82 | — | ['multiple_choice', 'qa', 'classification'] | https://huggingface.co/Navid-AI/Yehia-7B-preview | HuggingFace dataset URL, Any DATA_URL present, Multiple-choice format detected |
| 38 | 2026-Solorio-Afri-MCQA Multimodal Cultural Question Answering for | 82 | — | ['multiple_choice', 'qa', 'classification'] | https://huggingface.co/papers/2601.05699 | HuggingFace dataset URL, Any DATA_URL present, Multiple-choice format detected |
| 39 | 2023-LAIONHessian.AI-GermanBenchmark German translations of popular LLM benchmarks | 80 | GermanBenchmark | — | https://huggingface.co/datasets/LeoLM/German_be... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 40 | 2023-Lin-ToxicChat | 80 | ToxicChat | classification | https://huggingface.co/datasets/lmsys/toxic-chat | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 41 | 2024-Choi-CaLMQA Exploring culturally specific long-form question | 80 | CaLMQA | multiple_choice | https://huggingface.co/datasets/shanearora/CaLMQA | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 42 | 2024-Kaneko-Eagle | 80 | Eagle | generate_until | https://huggingface.co/datasets/MasahiroKaneko/... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 43 | 2024-Liu-JAILJUDGE | 80 | JAILJUDGE | None | https://huggingface.co/datasets/usail-hkust/Jai... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 44 | 2024-community-Open Leaderboard for Hebrew LLMs | 80 | Hebrew LLM Leaderboard | — | https://huggingface.co/spaces/hebrew-llm-leader... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 45 | 2025-Andriushchenko-AgentHarm | 80 | AgentHarm | [] | https://huggingface.co/datasets/ai-safety-insti... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 46 | 2025-Lin-MORALISE | 80 | MORALISE | ['multiple_choice'] | https://huggingface.co/datasets/Ze1025/MORALISE | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 47 | 2024-Masood-AL-QASIDA Analyzing LLM Quality and Accuracy Systematically in | 80 | AL-QASIDA | generate_until | https://huggingface.co/spaces/OALL | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 48 | 2024-Pistilli-CIVICS Building a Dataset for Examining Culturally-Informed Values in | 80 | CIVICS (Culturally-Informed & Values-Inclusive Corpus for Societal Impacts) | generate_until | https://huggingface.co/spaces/CIVICS-dataset/CI... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 49 | 2024-Sang-CDEval A Benchmark for Measuring the | 80 | CDEval | multiple_choice | https://huggingface.co/datasets/Rykeryuhang/CDE... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 50 | 2024-Yu-CMoralEval | 80 | CMoralEval | multiple_choice | https://github.com/tjunlp-lab/CMoralEval | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 51 | 2024-Zeng-AIR-Bench 2024 | 80 | AIR-Bench 2024 | None | https://huggingface.co/datasets/stanford-crfm/a... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 52 | 2025-Machlovi-GuardEval | 80 | GuardEval | ['qa'] | https://huggingface.co/meta-llama/Llama-Guard-3-8B | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 53 | 2025-Mitchell-SHADES | 80 | SHADES | [] | https://huggingface.co/datasets/LanguageShades/... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 54 | 2025-Pourbahman-ELAB | 80 | ELAB (Extensive LLM Alignment Benchmark) | [] | https://huggingface.co/spaces/MCILAB/LLM_Alignm... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 55 | 2025-Raza-HumaniBench | 80 | HumaniBench | ['multiple_choice', 'qa'] | https://huggingface.co/vector-institute/HumaniB... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 56 | 2026-Rehman-X-MuTeST A Multilingual Benchmark for Explainable | 80 | X-MuTeST | ['classification'] | https://huggingface.co/datasets/UVSKKR/X-MuTeST | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 57 | 2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource | 77 | BLUB (Bangla Language Understanding Benchmark) | qa | https://github.com/csebuetnlp/banglabert | Has DATA_URL, Public availability, QA format |
| 58 | 2020-Hoover-Moral Foundations Twitter Corpus | 75 | Moral Foundations Twitter Corpus (MFTC) | classification | https://osf.io/ezn37/ | Has DATA_URL, Public availability, Classification format |
| 59 | 2022-Brazdil-NaijaSenti A Nigerian Twitter Sentiment Corpus | 75 | NaijaSenti | classification | https://huggingface.co/datasets/HausaNLP/NaijaS... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 60 | 2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis | 75 | HeBERT / HebEMO / HebrewSentiment | classification | https://huggingface.co/avichr/heBERT_sentiment_... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 61 | 2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction | 75 | Visual Commonsense Immorality Benchmark | None | https://github.com/ku-vai/Zero-shot-Visual-Comm... | Has DATA_URL, Public availability, Classification format |
| 62 | 2023-Durmus-Towards Measuring the Representation of | 75 | GlobalOpinionQA | multiple_choice | https://huggingface.co/datasets/Anthropic/llm_g... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 63 | 2023-Huang-AceGPT Localizing Large Language Models in Arabic | 75 | ACVA (Arabic Cultural Value Alignment) | None | https://github.com/FreedomIntelligence/AceGPT | Has DATA_URL, Public availability, Classification format |
| 64 | 2024-Aakanksha-The Multilingual Alignment Prism | 75 | Multilingual Alignment Prism | generate_until | https://huggingface.co/datasets/CohereForAI/aya... | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 65 | 2024-Bandarkar-The Belebele Benchmark a Parallel Reading Comprehension Dataset in | 75 | Belebele | multiple_choice | https://github.com/openai/tiktoken | Has DATA_URL, Public availability, Multiple-choice format |
| 66 | 2024-Jiang-WildTeaming at Scale | 75 | WildJailbreak | None | https://huggingface.co/datasets/allenai/wildjai... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 67 | 2024-Kirk-The PRISM Alignment Project | 75 | PRISM | classification | https://github.com/HannahKirk/prism-alignment, ... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 68 | 2024-Liebeskind-From Linguistics to Practice a Case Study of Offensive Language | 75 | Hebrew Offensive Language Taxonomy Dataset | classification | https://huggingface.co/christinacdl/XLM_ | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 69 | 2025-Ghosh-AEGIS 2.0 | 75 | AEGIS 2.0 | [] | https://github.com/meta-llama/llama-recipes | Has DATA_URL, Public availability, Classification format |
| 70 | 2025-Kumar-Are Rules Meant to be Broken | 75 | UniMoral | ['classification'] | https://huggingface.co/datasets/shivaniku/UniMoral | HuggingFace dataset URL, Has DATA_URL, Classification format |
| 71 | 2023-Rao-What Makes it Ok to Set a Fire Iterative | 75 | delta-Rules-of-Thumb (delta-RoT) | multiple_choice | https://huggingface.co/datasets/kavelrao/d-Rule... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 72 | 2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs | 75 | MoralChoice | multiple_choice | https://huggingface.co/datasets/ninoscherrer/mo... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 73 | 2023-Xu-CValues | 75 | CValues | multiple_choice | https://github.com/X-PLUG/CValues | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 74 | 2024-Pfister-SuperGLEBer German Language Understanding Evaluation Benchmark | 75 | SuperGLEBer | qa | https://github.com/LSX-UniWue/SuperGLEBer | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 75 | 2024-Pistilli-CIVICS | 75 | CIVICS (Culturally-Informed and Values-Inclusive Corpus for Societal impacts) | generate_until | https://huggingface.co/CIVICS-dataset | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 76 | 2024-Research-SEA-VQA Southeast Asian Cultural Context Dataset For Visual Question | 75 | SEA-VQA | multiple_choice | https://huggingface.co/datasets/wit543/sea-vqa | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 77 | 2024-Schutze-TurkishMMLU Measuring Massive Multitask Language Understanding | 75 | TurkishMMLU | multiple_choice | https://github.com/ArdaYuksel/TurkishMMLU | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 78 | 2024-Sorensen-Value Kaleidoscope | 75 | ValuePrism / Value Kaleidoscope (Kaleido) | None | https://huggingface.co/datasets/allenai/ValuePrism | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 79 | 2024-Tonneau-Turkish Hate Speech Superset Dataset | 75 | Turkish Hate Speech Superset | classification | https://huggingface.co/datasets/manueltonneau/t... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 80 | 2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized | 75 | Fair-PP | [] | https://github.com/tools-only/FairPP, https://h... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 81 | 2024-Bang-BLEnD A Benchmark for LLMs on | 72 | BLEnD | multiple_choice | https://github.com/nlee0212/BLEnD | Has DATA_URL, Public availability, QA format |
| 82 | 2024-Huang-TrustLLM | 72 | TrustLLM | generate_until | https://github.com/HowieHwong/TrustLLM | Has DATA_URL, Public availability, QA format |
| 83 | 2019-Basile-SemEval-2019 Task 5 Multilingual Detection of Hate Speech Against | 70 | HatEval (SemEval-2019 Task 5) | None | NA | Has DATA_URL, Public availability, Classification format |
| 84 | 2021-Jiang-Pretrained Models and Evaluation Data for | 70 | Khmer BERT/ELECTRA + Khmer News Categorization Dataset | generate_until | https://github.com/SunYanCN/seqeval | Has DATA_URL, Public availability, Classification format |
| 85 | 2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian | 70 | ParsiNLU | multiple_choice | https://github.com/MarioVilas/googlesearch | Has DATA_URL, Public availability, Multiple-choice format |
| 86 | 2022-Ganguli-Red Teaming Language Models to Reduce Harms | 70 | Anthropic Red Team Dataset | None | https://github.com/anthropics/hh-rlhf | Has DATA_URL, Public availability, Classification format |
| 87 | 2023-Ji-Commonsense Norm Bank | 70 | MEC (Maximizing Expected Choiceworthiness) / Theory-based Moral AI | multiple_choice | https://huggingface.co/microsoft/deberta-v3-large | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 88 | 2024-Garcia-Open Portuguese LLM Leaderboard | 70 | Open Portuguese LLM Leaderboard | — | https://huggingface.co/spaces/eduagarcia/open_p... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 89 | 2024-Li-SALAD-Bench | 70 | SALAD-Bench | multiple_choice | https://github.com/OpenSafetyLab/SALAD-BENCH | Has DATA_URL, Public availability, Multiple-choice format |
| 90 | 2024-Li-The WMDP Benchmark | 70 | WMDP (Weapons of Mass Destruction Proxy) | multiple_choice | https://wmdp.ai | Has DATA_URL, Public availability, Multiple-choice format |
| 91 | 2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark | 70 | NLEBench | qa | https://github.com/Smartmedia-AI/NorGLM | Has DATA_URL, Public availability, Open-ended generation |
| 92 | 2024-initiative-CALAMITA Challenging the Abilities of LAnguage Models in ITAlian | 70 | CALAMITA | generate_until | https://github.com/CALAMITA-AILC/calamita-eval | Has DATA_URL, Public availability, Multiple-choice format |
| 93 | 2025-Abbasi-Benchmarking Sociolinguistic Diversity in Swahili NLP | 70 | Swahili Sociolinguistic Diversity Benchmark | [] | https://github.com/nd-hal/swahili_psych_taxonomy | Has DATA_URL, Public availability, Open-ended generation |
| 94 | 2025-Al-SHADES Towards a Multilingual Assessment of Stereotypes in Large | 70 | SHADES | — | NA | Has DATA_URL, Public availability, Open-ended generation |
| 95 | 2025-An-MoralReason | 70 | Moral-Reason-QA | ['qa'] | https://huggingface.co/datasets/zankjhk/Moral-R... | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 96 | 2025-Bulla-Large Language Models meet moral values | 70 | Unnamed (MFT-based LLM moral evaluation) | ['classification'] | https://osf.io/kw6rc/?view_only=73c3d8e2f7c9483... | Has DATA_URL, Public availability, Classification format |
| 97 | 2025-Chiu-CulturalBench | 70 | CulturalBench | ['multiple_choice'] | https://hf.co/spaces/kellycyy/CulturalBench | Has DATA_URL, Public availability, Multiple-choice format |
| 98 | 2025-Li-T2ISafety | 70 | T2ISafety | [] | https://github.com/adwardlee/t2i_safety | Has DATA_URL, Public availability, Dataset size stated |
| 99 | 2022-Ziems-The Moral Integrity Corpus | 70 | MIC (Moral Integrity Corpus) | None | https://github.com/GT-SALT/mic | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 100 | 2023-team-SeaLLMs Large Language Models for Southeast | 70 | SeaRefuse | generate_until | https://huggingface.co/SeaLLMs | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 101 | 2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark | 70 | Kazakh Dastur-MC | — | https://huggingface.co/datasets/kz-transformers... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 102 | 2024-Son-HAE-RAE Bench Evaluation of Korean Knowledge in Language Models | 70 | HAE-RAE Bench | classification | https://github.com/HAE-RAE/HAE-RAE-BENCH | Any DATA_URL present, Survey availability = Public, Dataset size stated |
| 103 | 2024-Zhou-tSMC | 70 | tSMC (Symmetric Moral Consistency) | None | https://huggingface.co/google/gemma-2b-it | HuggingFace dataset URL, Any DATA_URL present, Multiple-choice format detected |
| 104 | 2025-Papadimitriou-BelarusianGLUE Towards a Natural Language Understanding Benchmark for | 70 | — | ['qa', 'classification'] | https://github.com/huggingface/peft | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 105 | 2025-Shetty-VITAL | 70 | VITAL | ['multiple_choice'] | https://github.com/anudeex/VITAL.git | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 106 | 2025-Wu-CVC | 70 | C-VARC / CVC (Chinese Value Rule Corpus) | ['classification'] | https://huggingface.co/datasets/Beijing-AISI/C-... | HuggingFace dataset URL, Any DATA_URL present, Open-ended generation |
| 107 | 2025-Zhang-REVAL | 70 | REVAL | ['qa'] | https://github.com/InternLM/InternLM-techreport | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 108 | 2023-Ji-BeaverTails | 67 | BeaverTails | qa | https://sites.google.com/view/pku-beavertails | Has DATA_URL, Public availability, QA format |
| 109 | 2024-Li-Value-Spectrum | 67 | Value-Spectrum | classification | https://github.com/Jeremyyny/Value-Spectrum | Has DATA_URL, Public availability, QA format |
| 110 | 2024-group-ITA-Bench Towards a More Comprehensive Evaluation for Italian LLMs | 67 | ITA-Bench | — | https://github.com/SapienzaNLP/ita-bench | Has DATA_URL, Public availability, QA format |
| 111 | 2021-Park-KLUE Korean Language Understanding Evaluation | 67 | KLUE (Korean Language Understanding Evaluation) | generate_until | https://github.com/KLUE-benchmark/KLUE | Any DATA_URL present, Survey availability = Public, QA format detected |
| 112 | 2024-Putri-Can LLM Generate Culturally Relevant Commonsense QA Data Case Study | 67 | ID-CSQA (Indonesian Culturally-relevant Commonsense QA) | multiple_choice | https://github.com/commonsense/conceptnet5 | Any DATA_URL present, Survey availability = Public, QA format detected |
| 113 | 2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs | 67 | MORABLES | ['multiple_choice', 'qa'] | https://huggingface.co/datasets/cardiffnlp/Mora... | HuggingFace dataset URL, Any DATA_URL present, QA format detected |
| 114 | 2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset | 65 | Portuguese Hierarchical Hate Speech Dataset | None | https://github.com/paulafortuna/Portuguese-Hate... | Has DATA_URL, Public availability, Classification format |
| 115 | 2021-Barikeri-REDDITBIAS | 65 | REDDITBIAS | generate_until | https://github.com/umanlp/RedditBias | Has DATA_URL, Public availability, Dataset size stated |
| 116 | 2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social | 65 | ViHSD (Vietnamese Hate Speech Detection) | classification | https://github.com/google-research/bert | Has DATA_URL, Public availability, Classification format |
| 117 | 2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text | 65 | HATE-ITA | classification | https://github.com/dhfbk/hate-ita | Has DATA_URL, Public availability, Dataset size stated |
| 118 | 2023-Aroyo-DICES Dataset | 65 | DICES (Diversity In Conversational AI Evaluation for Safety) | None | https://github.com/google-research-datasets/dic... | Has DATA_URL, Public availability, Dataset size stated |
| 119 | 2023-Ayele-Amharic Hate Speech Dataset | 65 | Amharic Hate Speech Dataset | classification | https://github.com/uhh-lt/AmharicHateSpeech | Has DATA_URL, Public availability, Classification format |
| 120 | 2023-Haq-Pashto Offensive Language Detection A Benchmark Dataset and | 65 | POLD (Pashto Offensive Language Dataset) | classification | https://zenodo.org/record/8195797 | Has DATA_URL, Public availability, Dataset size stated |
| 121 | 2023-Inciarte-SERENGETI Massively Multilingual Language Models for | 65 | — | classification | https://huggingface.co/UBC-NLP/serengeti-E250 | HuggingFace dataset URL, Has DATA_URL, LLM_assessed populated |
| 122 | 2024-Bhutani-SeeGULL Multilingual A Dataset of Geo-Culturally Situated Stereotypes | 65 | SeeGULL Multilingual | None | https://github.com/google-research-datasets/See... | Has DATA_URL, Public availability, Dataset size stated |
| 123 | 2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for | 65 | C3Bench | multiple_choice | https://github.com/NiuTrans/Classical-Modern | Has DATA_URL, Public availability, Classification format |
| 124 | 2024-Compostela-Open Generative Large Language Models for Galician | 65 | — | None | https://huggingface.co/HiTZ/latxa-7b-v1 | HuggingFace dataset URL, Has DATA_URL, LLM_assessed populated |
| 125 | 2024-Enevoldsen-The Scandinavian Embedding Benchmarks Comprehensive Assessment of | 65 | SEB (Scandinavian Embedding Benchmark) | classification | https://github.com/KennethEnevoldsen/scandinavi... | Has DATA_URL, Public availability, Classification format |
| 126 | 2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic | 65 | M-ALERT | None | https://github.com/cmu-lti/m-alert | Has DATA_URL, Public availability, Dataset size stated |
| 127 | 2024-Jin-Language Model Alignment in Multilingual Trolley | 65 | MultiTP | None | https://github.com/causalNLP/multiTP | Has DATA_URL, Public availability, Classification format |
| 128 | 2024-Keutzer-One Model is All You Need | 65 | — | qa | https://github.com/sebastian-nehrdich/byt5-sans... | HuggingFace dataset URL, Has DATA_URL, LLM_assessed populated |
| 129 | 2024-Koppel-Adapting LLMs to Hebrew Unveiling DictaLM | 65 | — | qa | https://huggingface.co/dicta-il/dictalm2.0 | HuggingFace dataset URL, Has DATA_URL, LLM_assessed populated |
| 130 | 2024-Liu-Are Multilingual LLMs Culturally-Diverse Reasoners An Investigation | 65 | MAPS (MulticulturAl Proverbs and Sayings) | qa | https://github.com/UKPLab/maps | Has DATA_URL, Public availability, Classification format |
| 131 | 2024-Liu-CultureAtlas | 65 | CultureAtlas | qa | https://github.com/yrf1/LLM-MassiveMulticulture... | Has DATA_URL, Public availability, Dataset size stated |
| 132 | 2025-Al-SHADES A New Multilingual Benchmark for Stereotypes Bias in Large | 65 | SHADES | [] | NA | Has DATA_URL, Public availability, Dataset size stated |
| 133 | 2025-Al-Towards a Multilingual Assessment of Stereotypes in Large ... | 65 | SHADES | — | NA | Has DATA_URL, Public availability, Dataset size stated |
| 134 | 2025-Almeida-BRoverbs - Measuring how much LLMs understand Portuguese proverbs | 65 | BRoverbs | ['qa', 'classification'] | https://huggingface.co/datasets/Tropic-AI/BRoverbs | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 135 | 2025-Ashkinaze-Deep Value Benchmark | 65 | Deep Value Benchmark (DVB) | [] | https://github.com/josh-ashkinaze/deep-value-be... | Has DATA_URL, Public availability, Dataset size stated |
| 136 | 2025-Banerjee-SafeInfer | 65 | HarmEval | ['loglikelihood'] | https://github.com/NeuralSentinel/SafeInfer | Has DATA_URL, Public availability, Classification format |
| 137 | 2025-Bouchekif-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and | 65 | QIAS 2025 | ['qa'] | https://gitlab.com/islamgpt1/qias_shared_task_2025 | Has DATA_URL, Public availability, Multiple-choice format |
| 138 | 2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values | 65 | MoVa | ['classification'] | https://github.com/ZiyuChen0410/MoVa2025 | Has DATA_URL, Public availability, Classification format |
| 139 | 2025-Dementieva-TextDetox Multilingual Toxicity Dataset | 65 | TextDetox Multilingual Toxicity Dataset | — | https://huggingface.co/datasets/textdetox/multi... | HuggingFace dataset URL, Has DATA_URL, Classification format |
| 140 | 2025-Hossain-BanHate An Up-to-Date and Fine-Grained Bangla Hate Speech Dataset | 65 | BanHate | ['classification'] | https://huggingface.co/datasets/aplycaebous/Ban... | HuggingFace dataset URL, Has DATA_URL, Classification format |
| 141 | 2025-Ju-NaVAB | 65 | NaVAB (National Value Alignment Benchmark) | [] | https://huggingface.co/datasets/JadenGGGeee/NaVAB | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 142 | 2025-Khan-Randomness Not Representation The Unreliability of Evaluating | 65 | Unnamed (Cultural Alignment Robustness Evaluation) | [] | https://huggingface.co/datasets/ShashiVish/cove... | HuggingFace dataset URL, Has DATA_URL, Public availability |
| 143 | 2025-Koto-Sherkala-Chat Building a State-of-the-Art LLM for Kazakh in a | 65 | — | ['multiple_choice', 'qa'] | https://huggingface.co/inceptionai/Llama-3.1-Sh... | HuggingFace dataset URL, Has DATA_URL, LLM_assessed populated |
| 144 | 2025-Krasnodebska-PL-Guard Benchmarking Language Model Safety for Polish | 65 | PL-Guard | ['classification'] | https://huggingface.co/OPI-PG/Qra-1b | HuggingFace dataset URL, Has DATA_URL, Classification format |
| 145 | 2025-Kumar-UniMoral ACL 2025 Best Resource Paper | 65 | UniMoral | ['classification'] | https://huggingface.co/datasets/ciol-research/B... | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 146 | 2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from | 65 | CLASH (Character perspective-based LLM Assessments in Situations with High-stakes) | [] | https://huggingface.co/datasets/launch/CLASH | HuggingFace dataset URL, Has DATA_URL, Dataset size stated |
| 147 | 2025-Liu-Can LLMs Grasp Implicit Cultural Values | 65 | CQ-Bench (duplicate entry) | [] | https://github.com/uscnlp-lime/CQ-Bench | Has DATA_URL, Public availability, Dataset size stated |
| 148 | 2020-Moon-BEEP! Korean Corpus of Online News Comments for Toxic Speech Detection | 65 | BEEP! (Korean Toxic Speech Corpus) | None | https://github.com/LDNOOBW/List-of-Dirty-Naughty- | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 149 | 2021-Nurce-Detecting Abusive Albanian | 65 | SHAJ (Spoken Hate in the Albanian Jargon) | classification | https://doi.org/10.6084/m9.figshare.19333298.v1 | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 150 | 2021-Nutanong-WangchanBERTa Pretraining transformer-based Thai Language Models | 65 | — | qa | https://huggingface.co/airesearch/wangchanberta... | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 151 | 2021-Sun-LaoPLM Pre-trained Language Models for Lao | 65 | LaoPLM + Lao Text Classification Dataset | classification | https://github.com/GKLMIP/Yunshan-Cup-2020 | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 152 | 2021-Wuerzburg-German HateSpeech Corpus | 65 | GMHP7k (German Misogynistic Hatespeech Posts) | classification | https://github.com/cophi-wue/German_HateSpeech_... | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 153 | 2023-Oslo-NorBench A Benchmark for Norwegian Language Models | 65 | NorBench | qa | https://github.com/ltgoslo/NorBench | Any DATA_URL present, Survey availability = Public, Dataset size stated |
| 154 | 2023-Santurkar-Whose Opinions Do Language Models Reflect | 65 | OpinionQA | multiple_choice | https://github.com/tatsu-lab/opinions_qa | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 155 | 2023-Soemer-Antisemitic Messages A Guide to High-Quality | 65 | ISCA Antisemitism Detection Dataset | classification | https://zenodo.org/records/7932888 | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 156 | 2023-Wang-SeaEval for Multilingual Foundation Models From Cross-Lingual | 65 | SeaEval | multiple_choice | https://github.com/SeaEval/SeaEval | Any DATA_URL present, Survey availability = Public, Dataset size stated |
| 157 | 2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge | 65 | RO-Offense | classification | https://huggingface.co/datasets/readerbench/ro-... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 158 | 2024-Moore-Are Large Language Models Consistent over | 65 | Unnamed (Value Consistency Evaluation) | multiple_choice | https://huggingface.co/datasets/jlcmoore/ValueC... | HuggingFace dataset URL, Any DATA_URL present, Dataset size stated |
| 159 | 2024-Nguyen-ViHateT5 Enhancing Hate Speech Detection in Vietnamese With A Unified | 65 | ViHateT5 / VOZ-HSD | classification | https://github.com/tarudesu/ViHateT5 | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 160 | 2024-Overfit-GM-Turkish Overfit-GM Toxic Language Dataset | 65 | Turkish Toxic Language Dataset (Overfit-GM) | — | https://huggingface.co/datasets/Overfit-GM/turk... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 161 | 2024-Park-Pragmatic Competence Evaluation of Large Language Models for the | 65 | Korean Pragmatic Competence Evaluation | multiple_choice | https://github.com/DojunPark/pragmatic_eval_korean | Any DATA_URL present, Survey availability = Public, Multiple-choice format detected |
| 162 | 2024-Phyo-Development and Evaluation of Myanmar GPT | 65 | — | — | https://huggingface.co/jojo-ai-mst/MyanmarGPT | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 163 | 2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety | 65 | SafetyPrompts | multiple_choice | https://github.com/paul-rottger/safetyprompts-p... | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 164 | 2024-Singh-IndicGenBench A Multilingual Benchmark to Evaluate | 65 | IndicGenBench | qa | https://github.com/google-research-datasets/ind... | Any DATA_URL present, Survey availability = Public, Open-ended generation |
| 165 | 2024-Thu-Development and Evaluation of Myanmar GPT A Language Model for | 65 | — | — | https://huggingface.co/jojo-ai-mst/MyanmarGPT | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 166 | 2024-Thu-MixCuBe When Tom Eats Kimchi - Evaluating Cultural Awareness of | 65 | MixCuBe | — | https://huggingface.co/datasets/kyawyethu/MixCuBe | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 167 | 2024-Toygar-Turkish Offensive Language Detection Dataset | 65 | Turkish Offensive Language Detection Dataset | classification | https://huggingface.co/datasets/Toygar/turkish-... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 168 | 2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios | 65 | RTP-LX | classification | https://github.com/microsoft/RTP-LX | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 169 | 2024-Xie-CultureLLM Incorporating Cultural Differences into Large | 65 | CultureLLM / WVS-based Cultural Evaluation | generate_until | https://github.com/Scarelette/CultureLLM | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 170 | 2024-Zhang-MM-Eval A Hierarchical Benchmark for Modern Mongolian Evaluation in | 65 | MM-Eval | multiple_choice | https://github.com/joenahm/MM-Eval | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 171 | 2024-team-Indic-Bias A Comprehensive Benchmark for Fairness | 65 | Indic-Bias | — | https://huggingface.co/datasets/ai4bharat/Indic... | HuggingFace dataset URL, Any DATA_URL present, Survey availability = Public |
| 172 | 2025-Maji-DRISHTIKON A Multimodal Multilingual Benchmark for | 65 | DRISHTIKON | ['multiple_choice', 'qa'] | https://huggingface.co/datasets/13ari/DRISHTIKON | HuggingFace dataset URL, Any DATA_URL present, Open-ended generation |
| 173 | 2025-Rastogi-DIVE Dataset for Pluralistic Alignment of Text-to-Image Models | 65 | DIVE (Diverse Intersectional Visual Evaluation) | [] | https://huggingface.co/datasets/neurips-dataset... | HuggingFace dataset URL, Any DATA_URL present, Dataset size stated |
| 174 | 2025-Santhosh-IndiCASA - Dataset and Bias Evaluation Framework for LLMs in Indian | 65 | IndiCASA | [] | https://github.com/cerai-iitm/IndiCASA | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 175 | 2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace | 65 | IndoHateMix | ['classification'] | https://huggingface.co/Qwen/Qwen2.5-7B | HuggingFace dataset URL, Any DATA_URL present, Classification format detected |
| 176 | 2025-Trager-MFTCXplain | 65 | MFTCXplain | ['qa'] | https://github.com/franciellevargas/MFTCXplain | Any DATA_URL present, Survey availability = Public, Classification format detected |
| 177 | 2025-Yao-NurValues | 65 | NurValues | [] | https://huggingface.co/datasets/Ben012345/NurVa... | HuggingFace dataset URL, Any DATA_URL present, Dataset size stated |
| 178 | 2025-Yuan-S-Eval | 65 | S-Eval | ['multiple_choice'] | https://github.com/IS2Lab/S-Eval | Any DATA_URL present, Survey availability = Public, Open-ended generation |

### Implementation Sketches (Top 10)

### 2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model (score: 100)
- **Suggested task name:** `frenchbench`
- **Dataset path:** `https://huggingface.co/croissantllm`
- **Task type:** `classification`
- **Metrics:** perplexity
- **Prompt template notes:** none found
- **What's missing:** No prompt template hints found

### 2023-Wang-DecodingTrust (score: 100)
- **Suggested task name:** `decodingtrust`
- **Dataset path:** `huggingface.co/datasets/AI-Secure/DecodingTrust`
- **Task type:** `None`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

### 2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub (score: 100)
- **Suggested task name:** `seacrowd`
- **Dataset path:** `https://huggingface.co/SEACrowd`
- **Task type:** `generate_until`
- **Metrics:** accuracy
- **Prompt template notes:** none found
- **What's missing:** No prompt template hints found

### 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs (score: 100)
- **Suggested task name:** `aradice_aradice_culture`
- **Dataset path:** `huggingface.co/datasets/QCRI/AraDiCE`
- **Task type:** `qa`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

### 2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering (score: 100)
- **Suggested task name:** `afrimed_qa`
- **Dataset path:** `huggingface.co/datasets/intronhealth/afrimedqa_v2`
- **Task type:** `multiple_choice`
- **Metrics:** accuracy
- **Prompt template notes:** prompt templates are shown in Figure
- **What's missing:** Data splits not identified

### 2024-Romanou-INCLUDE Evaluating Multilingual Language Understanding with Regional (score: 100)
- **Suggested task name:** `include`
- **Dataset path:** `huggingface.co/datasets/CohereForAI/include-base-44`
- **Task type:** `multiple_choice`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

### 2024-Tam-An Improved Traditional Chinese Evaluation Suite for Foundation Model (score: 100)
- **Suggested task name:** `tmmlu`
- **Dataset path:** `huggingface.co/datasets/ikala/tmmluplus`
- **Task type:** `qa`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

### 2024-Yuan-Social Measuring Social Norms of LLMs (score: 100)
- **Suggested task name:** `social_social_norms_dataset`
- **Dataset path:** `huggingface.co/datasets/socialnormdataset/social`
- **Task type:** `generate_until`
- **Metrics:** accuracy
- **Prompt template notes:** none found
- **What's missing:** No prompt template hints found

### 2024-Baek-K-Viscuit Evaluating Visual and Cultural Interpretation with (score: 95)
- **Suggested task name:** `k_viscuit`
- **Dataset path:** `https://huggingface.co/datasets/ddehun/k-viscuit`
- **Task type:** `multiple_choice`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

### 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU (score: 95)
- **Suggested task name:** `tmlu_taiwanese_mandarin_language_understanding`
- **Dataset path:** `huggingface.co/datasets/miulab/tmlu`
- **Task type:** `classification`
- **Metrics:** not determined
- **Prompt template notes:** none found
- **What's missing:** No metrics defined in extract; No prompt template hints found

## 3. Needs Dataset Hosting (413 papers, score 45-64)

| # | Paper | Score | Data URL | What's Missing |
|---|-------|-------|----------|----------------|
| 1 | 2025-Hong-PrinciplismQA Towards Assessing Medical Ethics from Knowledge to | 70 | NA | no public availability, no data splits |
| 2 | 2024-Fitzgerald-Some Issues in Predictive Ethics Modeling | 65 | NA | no public availability |
| 3 | 2025-Alwajih-PalmX 2025 - First Shared Task on Benchmarking LLMs on Arabic and | 65 | https://github.com/UBC-NLP/palmx_2025 | no public availability |
| 4 | 2023-Bhardwaj-Red-Teaming Large Language Models using Chain of Utterances for | 62 | https://github.com/declare-lab/red-in... | no metrics found |
| 5 | 2016-Fonseca-ASSIN Avaliação de Similaridade Semântica e INferência textual | 60 | https://huggingface.co/datasets/nilc-... | no public availability, no PDF extract details |
| 6 | 2018-Behzadan-TrolleyMod v1.0 | 60 | https://github.com/zminton/TrolleyMod... | no task type detected, no metrics found, no data splits |
| 7 | 2018-Dixon-Measuring and Mitigating Unintended Bias in Text | 60 | https://github.com/conversationai/uni... | no metrics found |
| 8 | 2019-Basile-SemEval-2019 Task 5 | 60 | https://github.com/msang/hateval | no task type detected, no metrics found |
| 9 | 2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification | 60 | https://github.com/sahoonihar/ToxicBi... | no metrics found, no data splits |
| 10 | 2019-Kreutz-GermEval 2019 Task 2 | 60 | NA | no metrics found |
| 11 | 2020-Forbes-Social Chemistry 101 | 60 | NA | no data splits |
| 12 | 2021-Dementieva-Methods for Detoxification of Texts for the Russian Language | 60 | https://github.com/sberbank-ai/ru-gpts | no metrics found, no data splits |
| 13 | 2022-Bai-Training a Helpful and Harmless Assistant with | 60 | https://github.com/anthropics/hh-rlhf | no task type detected, no metrics found |
| 14 | 2022-Dementieva-RUSSE 2022 Findings of the First Russian Detoxification Shared Task | 60 | https://github.com/sberbank-ai/ru-gpts | no metrics found |
| 15 | 2022-Emezue-AfroLM A Self-Active Learning-based Multilingual Pretrained | 60 | https://huggingface.co/bonadossou/afr... | no public availability |
| 16 | 2022-Kim-ProsocialDialog | 60 | https://hyunw.kim/prosocial-dialog | no metrics found |
| 17 | 2022-Kulkarni-Semantic and Sentiment Analysis of Selected | 60 | https://github.com/sydney-machine-lea... | no metrics found, no data splits |
| 18 | 2022-Liang-Holistic Evaluation of Language Models | 60 | https://github.com/stanford-crfm/helm | no data splits |
| 19 | 2023-Bosco-Detecting Racial Stereotypes An Italian Social Media Corpus where | 60 | https://github.com/dhfbk/LiLaH | no PDF extract details |
| 20 | 2023-Byun-Automatic Construction of a Korean Toxic Instruction Dataset for | 60 | https://github.com/byunsj/KoTox-Korea... | no metrics found, no data splits |
| 21 | 2023-Dai-Safe RLHF | 60 | https://github.com/PKU-Alignment/safe... | no metrics found |
| 22 | 2023-Dione-MasakhaPOS Part-of-Speech Tagging for Typologically Diverse African | 60 | https://huggingface.co/datasets/masak... | no public availability, no metrics found |
| 23 | 2023-Duan-Denevil | 60 | https://valuecompass.github.io |  |
| 24 | 2023-Eskelinen-Toxicity Detection in Finnish Using Machine Translation | 60 | https://github.com/TurkuNLP/toxicity-... |  |
| 25 | 2023-Fleisig-FairPrism | 60 | https://github.com/microsoft/fairprism | no data splits |
| 26 | 2023-Li-ACLUE Can Large Language Model Comprehend | 60 | https://github.com/isen-zhang/ACLUE ;... | no public availability |
| 27 | 2024-Basem-Optimized Quran Passage Retrieval Using an | 60 | https://huggingface.co/datasets/ImruQays | no public availability |
| 28 | 2024-Bonagiri-SaGE | 60 | https://github.com/vnnm404/SaGE |  |
| 29 | 2024-Buyl-Large Language Models Reflect the Ideology of | 60 | https://github.com/aida-ugent/llm-ide... | no metrics found |
| 30 | 2024-Chen-GMAI-MMBench | 60 | https://huggingface.co/datasets/OpenG... | no public availability |
| 31 | 2024-Chiu-DailyDilemmas | 60 | https://hf.co/datasets/kellycyy/daily... | no metrics found, no data splits |
| 32 | 2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning | 60 | https://github.com/cicl-stanford/mora... | no metrics found |
| 33 | 2024-Gaikwad-MoralBench A Multi-Faceted Benchmark for Ethical and Safety Alignment | 60 | https://github.com/krimler/moralbench | no PDF extract details |
| 34 | 2024-Garcia-Introducing Bode A Fine-Tuned Large Language Model for Portuguese | 60 | https://huggingface.co/22h/cabrita-lo... | no public availability |
| 35 | 2024-Hasan-NativQA Multilingual Culturally-Aligned Natural Query for LLMs | 60 | https://huggingface.co/datasets/QCRI/... | no public availability |
| 36 | 2024-Hooker-Global MMLU Understanding and Addressing Cultural | 60 | https://huggingface.co/papers/2412.03304 | no public availability, no task type detected, no metrics found |
| 37 | 2024-Huang-Collective Constitutional AI Aligning a Language Model with Public | 60 | NA | no task type detected, no metrics found |
| 38 | 2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks | 60 | https://huggingface.co/datasets/FredZ... | no public availability |
| 39 | 2024-Li-OpenEval - Benchmarking Chinese LLMs across Capability Alignment and | 60 | https://github.com/01-ai/Yi | no task type detected, no metrics found |
| 40 | 2024-Luu-ViTHSD Exploiting Hatred by Targets for Hate Speech Detection on | 60 | https://github.com/bakansm/ViTHSD |  |
| 41 | 2025-Abdul-Mageed-Where Are We Evaluating LLM Performance | 60 | https://africa.dlnlp.ai/sahara/ (publ... | no task type detected, no data splits |
| 42 | 2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in | 60 | https://github.com/faridlazuarda/from... | no metrics found |
| 43 | 2025-Aly-Detecting gender bias in Arabic text through word embeddings PLOS One | 60 | https://github.com/aiamourad/AraGende... | no metrics found |
| 44 | 2025-Bae-CharMoral | 60 | https://github.com/BaeSuyoung/CharMoral | no metrics found, no data splits |
| 45 | 2025-Bar-DharmaBench Evaluating Language Models on Buddhist | 60 | NA | no PDF extract details |
| 46 | 2025-Buyl-AI Alignment at Your Discretion | 60 | https://huggingface.co/mistralai/Mist... | no public availability, no task type detected, no data splits |
| 47 | 2025-Cheng-ELEPHANT Social Sycophancy | 60 | https://github.com/myracheng/elephant | no task type detected, no data splits |
| 48 | 2025-Chiu-MoReBench | 60 | https://hf.co/datasets/morebench/more... | no metrics found |
| 49 | 2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large | 60 | https://huggingface.co/spaces/sdadas | no public availability, no metrics found, no data splits |
| 50 | 2025-Erdem-Cetvel A Unified Benchmark for Evaluating | 60 | https://huggingface.co/spaces/KUIS-AI... | no public availability, no metrics found, no data splits |
| 51 | 2025-Fan-FAIRMT-BENCH | 60 | https://github.com/FanZT6/FairMT-bench | no metrics found |
| 52 | 2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the | 60 | https://huggingface.co/inference-api/... | no public availability, no task type detected, no metrics found, no data splits |
| 53 | 2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness | 60 | https://github.com/Guochry/CARE | no metrics found |
| 54 | 2025-Happy Buzaaba-Lugha-Llama Adapting Large Language Models for | 60 | https://huggingface.co/Jacaranda/Afro... | no public availability, no metrics found |
| 55 | 2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors | 60 | https://github.com/Aries-iai/Deceptio... | no task type detected, no data splits |
| 56 | 2025-Huang-On the Trustworthiness of Generative Foundation | 60 | https://github.com/TrustGen/TrustEval... | no task type detected, no metrics found |
| 57 | 2025-Huang-Values in the Wild Discovering and Analyzing Values in Real AI | 60 | https://huggingface.co/datasets/Anthr... | no public availability, no task type detected |
| 58 | 2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for | 60 | https://huggingface.co/datasets/MBZUA... | no public availability, no data splits |
| 59 | 2025-Jiang-Investigating Machine Moral Judgement Through the Delphi Experiment | 60 | https://github.com/liweijiang/delphi.git | no task type detected, no metrics found |
| 60 | 2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements | 60 | https://osf.io/69epv | no metrics found |
| 61 | 2025-Jotautaitė-Speciesism in AI | 60 | https://osf.io/69epv | no metrics found |
| 62 | 2025-Jourdan-FairTranslate | 60 | https://github.com/fanny-jourdan/Fair... | no task type detected, no metrics found, no data splits |
| 63 | 2025-Kumar-SweEval Do LLMs Really Swear A | 60 | https://huggingface.co/datasets/arion... | no public availability, no metrics found |
| 64 | 2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese | 60 | https://livesecbench.intokentech.cn/ | no task type detected, no metrics found |
| 65 | 2026-Dang-RedBench | 60 | https://github.com/knoveleng/redeval | no task type detected, no metrics found |
| 66 | 2019-Ousidhoum-Multilingual and Multi-Aspect Hate Speech Analysis | 60 | https://github.com/HKUST-KnowComp/MLM... | no task type detected, no metrics found, no data splits |
| 67 | 2021-Ravikiran-DOSA Dravidian Code-Mixed Offensive Span Identification | 60 | https://github.com/manikandan-ravikir... | no task type detected, no metrics found, no data splits |
| 68 | 2022-Romim-BD-SHS A Benchmark Dataset for Learning to Detect Online Bangla Hate | 60 | https://github.com/naurosromim/hate-s... |  |
| 69 | 2022-Vargas-HateBR A Large Expert Annotated Corpus of Brazilian Instagram | 60 | https://github.com/franciellevargas/H... | no data splits |
| 70 | 2023-Xu-SC-Safety | 60 | https://www.CLUEbenchmarks.com | no data splits |
| 71 | 2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented | 60 | https://github.com/priyankamandikal/v... |  |
| 72 | 2024-Mello-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on | 60 | https://github.com/huggingface/transf... | no public availability, no metrics found |
| 73 | 2024-Microsoft-MEGAVERSE Benchmarking Large Language Models Across Languages | 60 | https://github.com/AI4Bharat/IndicTrans2 | no metrics found |
| 74 | 2024-Montalan-Kalahi A handcrafted grassroots cultural LLM evaluation suite for | 60 | https://github.com/aisingapore/kalahi |  |
| 75 | 2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in | 60 | https://github.com/Veranep/MBBQ |  |
| 76 | 2024-Nikolich-Vikhr The Family of Open-Source Instruction-Tuned Large Language | 60 | https://huggingface.co/datasets/Vikhr... | no public availability, no metrics found |
| 77 | 2024-Ohashi-Extended Japanese Commonsense Morality Dataset | 60 | https://github.com/IyatomiLab/extende... |  |
| 78 | 2024-Ren-ValueBench | 60 | https://github.com/Value4AI/ValueBench | no metrics found |
| 79 | 2024-Romero-CVQA Culturally-diverse Multilingual Visual Question Answering | 60 | https://cvqa-benchmark.org/ |  |
| 80 | 2024-Sahoo-IndicCONAN A Multilingual Dataset for Combating Hate Speech in Indian | 60 | https://github.com/sahoonihar/IndicCONAN | no data splits |
| 81 | 2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge | 60 | https://github.com/guijinSON/MM-Eval | no task type detected |
| 82 | 2024-Tian-Chinese SafetyQA - A Safety Short-form Factuality Benchmark | 60 | https://openstellarteam.github.io/Chi... |  |
| 83 | 2024-Wang-All Languages Matter On the Multilingual Safety of Large Language | 60 | https://github.com/facebookresearch/l... | no metrics found |
| 84 | 2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents | 60 | https://github.com/thu-coai/Agent-Saf... | no metrics found |
| 85 | 2024-Zhang-CHiSafetyBench | 60 | https://github.com/UnicomAI/UnicomBen... | no metrics found, no data splits |
| 86 | 2024-team-OpenThaiGPT 15 A Thai-Centric Open Source | 60 | https://huggingface.co/openthaigpt | no public availability, no metrics found |
| 87 | 2025-Micallef-MELABenchv1 Benchmarking Large Language Models against Smaller | 60 | https://huggingface.co/MLRS | no public availability |
| 88 | 2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts | 60 | https://github.com/AI4Bharat/indic-bias | no task type detected, no metrics found |
| 89 | 2025-Ning-LinguaSafe A Comprehensive Multilingual Safety Benchmark for Large | 60 | https://huggingface.co/datasets/teleg... | no public availability, no task type detected, no metrics found, no data splits |
| 90 | 2025-Ousidhoum-AfriHate A Multilingual Collection of Hate | 60 | https://huggingface.co/papers/2501.08284 | no public availability, no metrics found, no data splits |
| 91 | 2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs | 60 | https://huggingface.co/spaces/Eurolingua | no public availability, no metrics found, no data splits |
| 92 | 2025-Qi-AGENTIF | 60 | https://github.com/THU-KEG/AgentIF, h... | no public availability, no metrics found, no data splits |
| 93 | 2025-Resta-Evalita-LLM Benchmarking Large Language Models on Italian | 60 | https://huggingface.co/spaces/evalita... | no public availability |
| 94 | 2025-Susanto-A Multi-Labeled Dataset for Indonesian Discourse Examining Toxicity | 60 | https://huggingface.co/datasets/Exqrc... | no public availability, no metrics found, no data splits |
| 95 | 2025-Wen-Evaluating Implicit Bias in Large Language Models | 60 | https://github.com/yuchenwen1/BUMBLE | no task type detected, no metrics found |
| 96 | 2025-Wiyono-IndoPref | 60 | https://huggingface.co/datasets/david... | no public availability, no task type detected |
| 97 | 2025-Xiang-Comparing Moral Values in Western | 60 | https://github.com/ChunhuaLiu596/Word... | no task type detected, no metrics found |
| 98 | 2025-Yao-Value Compass Benchmarks | 60 | https://valuecompass.github.io/#/lead... | no metrics found |
| 99 | 2026-Zhou-CSSBench Evaluating the Safety of Lightweight LLMs against | 60 | https://huggingface.co/datasets/Yaesi... | no public availability, no metrics found |
| 100 | 2026-results-Macaron Controlled Human-Written Benchmark for Multilingual and | 60 | https://huggingface.co/datasets/AlaaA... | no public availability, no metrics found |
| 101 | 2025-Li-SafetyAnalyst | 58 | https://jl3676.github.io/SafetyAnalyst/ | no public availability |
| 102 | 2020-Kumar-Evaluating Aggression Identification in Social | 55 | https://sites.google.com/view/trac2/s... | no task type detected, no metrics found |
| 103 | 2020-Leite-Toxic Language Detection in Social Media for Brazilian Portuguese New | 55 | https://github.com/JAugusto97/ToLD-Br | no data splits |
| 104 | 2021-Azada-Fake News Detection in Low-Resourced Languages Kurdish Language Using | 55 | https://www.kaggle.com/raniaazad/kurd... | no data splits |
| 105 | 2022-Jiang-Can Machines Learn Morality | 55 | https://delphi.allenai.org | no metrics found, no data splits |
| 106 | 2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for | 55 | https://huggingface.co/datasets/qanas... | no public availability, no metrics found |
| 107 | 2023-Abhinand-Tamil-Llama A New Tamil Language Model | 55 | https://huggingface.co/abhinand/tamil... | no public availability, no metrics found |
| 108 | 2023-Huang-Flames | 55 | https://github.com/AIFlames/Flames |  |
| 109 | 2023-Lee-KoSBi A Dataset for Mitigating Social Bias Risks Towards Safer Large | 55 | https://github.com/Beomi/KcELECTRA | no metrics found |
| 110 | 2023-Lee-SQuARe A Large-Scale Dataset of Sensitive Questions and Acceptable | 55 | https://github.com/Beomi/KcELECTRA | no task type detected, no metrics found, no data splits |
| 111 | 2023-Liu-AlignBench | 55 | https://github.com/THUDM/AlignBench |  |
| 112 | 2024-AI-Religious Bias Benchmarks for ChatGPT | 55 | https://osf.io/b2ug9/download | no metrics found |
| 113 | 2024-Arshad-Understanding hate speech | 55 | https://github.com/twintproject/twint | no task type detected, no metrics found, no data splits |
| 114 | 2024-Ashraf-Arabic Dataset for LLM Safeguard Evaluation | 55 | https://github.com/mbzuai-nlp/Arabic_... |  |
| 115 | 2024-Azerbaijan-Azerbaijani Toxicity Classifier | 55 | https://huggingface.co/LocalDoc/azerb... | no public availability, no PDF extract details |
| 116 | 2024-Baruni-ParsBench Toolkits for Benchmarking LLMs Based on the Persian | 55 | https://github.com/Ipouyall/Benchmark... | no metrics found |
| 117 | 2024-Bayat-FactBench | 55 | https://huggingface.co/spaces/launch/... | no public availability |
| 118 | 2024-Cao-The Moral Foundations Weibo Corpus | 55 | NA | no public availability, no metrics found |
| 119 | 2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance | 55 | https://github.com/InstituteforDiseas... |  |
| 120 | 2024-Chao-JBB-Behaviours | 55 | https://github.com/JailbreakBench/jai... |  |
| 121 | 2024-Chaves-Napolab The Natural Portuguese Language Benchmark | 55 | https://github.com/huggingface/accele... |  |
| 122 | 2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation | 55 | https://github.com/CentreSecuriteIA/B... | no metrics found |
| 123 | 2024-Faisal-DialectBench A NLP Benchmark for Dialects Varieties and | 55 | https://github.com/ffaisal93/DialectB... |  |
| 124 | 2024-Frenda-GFG - Gender-Fair Generation A CALAMITA Challenge | 55 | https://github.com/dhfbk/gfg-calamita |  |
| 125 | 2024-Ghosh-AEGIS | 55 | https://github.com/meta-llama/llama-r... | no metrics found |
| 126 | 2024-Group-The AI Safety Benchmark | 55 | https://github.com/mlcommons/modelbench | no task type detected, no metrics found |
| 127 | 2024-Guldimann-COMPL-AI EU AI Act Compliance | 55 | https://github.com/compl-ai/compl-ai |  |
| 128 | 2024-Han-MedSafetyBench | 55 | https://github.com/AI4LIFE-GROUP/med-... | no metrics found |
| 129 | 2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values | 55 | https://github.com/Derekkk/VIVA_EMNLP24 | no metrics found |
| 130 | 2024-Huynh-A New Benchmark Dataset and Mixture-of-Experts Language Models for | 55 | https://huggingface.co/datasets/uitnl... | no public availability, no data splits |
| 131 | 2024-Ji-MoralBench | 55 | https://github.com/agiresearch/MoralB... | no metrics found |
| 132 | 2024-Jin-WenMind A Comprehensive Benchmark for Evaluating | 55 | https://github.com/SCUT-DLVCLab/WenMi... | no public availability, no metrics found |
| 133 | 2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After | 55 | https://huggingface.co/datasets/hungnm | no public availability, no data splits |
| 134 | 2024-LLM-Beetle-Azerbaijani LLM Leaderboard | 55 | https://huggingface.co/spaces/LLM-Bee... | no public availability, no PDF extract details |
| 135 | 2024-Li-Language Ranker A Metric for Quantifying LLM Performance Across | 55 | https://github.com/Helsinki-NLP/Tatoeba- | no task type detected, no metrics found |
| 136 | 2024-Lopes-GlórIA A Generative and Open Large Language Model for Portuguese | 55 | https://github.com/rvlopes/GlorIA | no metrics found |
| 137 | 2024-at-Overview of the Multilingual Text Detoxification Task at PAN 2024 | 55 | https://github.com/LDNOOBW/List-of-Di... | no metrics found |
| 138 | 2025-ADL Center for Technology and Society Daniel Kelley-Generating Hate Anti-Jewish and Anti-Israel Bias | 55 | https://www.adl.org/resources/report/... | no PDF extract details |
| 139 | 2025-Adelani-AfriMTEB and AfriE5 Benchmarking and Adapting | 55 | NA | no public availability, no metrics found, no data splits |
| 140 | 2025-Adelani-INJONGO A Multicultural Intent Detection and | 55 | https://huggingface.co/collections/Mc... | no public availability, no data splits |
| 141 | 2025-Aji-LoraxBench A Multitask Multilingual Benchmark Suite for 20 Indonesian | 55 | https://huggingface.co/datasets/googl... | no public availability, no metrics found, no data splits |
| 142 | 2025-Ajwad Abrar-Religious Bias Landscape in Language and | 55 | https://github.com/ajwad-abrar/Religi... | no metrics found |
| 143 | 2025-Asgari-I Am Aligned But With Whom | 55 | https://github.com/llm-lab-org/MENA-V... | no metrics found, no data splits |
| 144 | 2025-Bai-Explicitly unbiased large language models still form biased | 55 | https://github.com/baixuechunzi/llm- | no metrics found |
| 145 | 2025-Barth-Multilingual European Language Models Benchmarking Approaches and | 55 | https://huggingface.co/datasets/opena... | no public availability, no metrics found, no data splits |
| 146 | 2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning | 55 | https://huggingface.co/datasets/AUEB-... | no public availability, no metrics found |
| 147 | 2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT | 55 | https://huggingface.co/datasets/AxelD... | no public availability, no task type detected |
| 148 | 2025-Deshpande-TRAIL | 55 | https://huggingface.co/datasets/Patro... | no public availability, no task type detected |
| 149 | 2025-Goyal-Vedavani A Benchmark Corpus for ASR | 55 | https://huggingface.co/datasets/sanga... | no public availability, no metrics found |
| 150 | 2025-Group-AILuminate | 55 | https://github.com/mlcommons/ailuminate | no task type detected, no metrics found, no data splits |
| 151 | 2025-Hassan-DialectalArabicMMLU Benchmarking Dialectal Capabilities in Arabic and | 55 | https://huggingface.co/blog/silma-ai | no public availability, no data splits |
| 152 | 2025-Hsieh-TaiwanVQA A Benchmark for Visual Question Answering for Taiwanese | 55 | https://huggingface.co/datasets/hhhua... | no public availability |
| 153 | 2025-Jassem-LLMzSzL a Comprehensive LLM Benchmark for Polish | 55 | https://huggingface.co/OPI-PG/Qra-1b | no public availability |
| 154 | 2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling | 55 | https://e-m-n-l-p.github.io/ | no task type detected, no metrics found |
| 155 | 2025-KJ-IndicMMLU-Pro Benchmarking Indic Large Language Models | 55 | https://huggingface.co/datasets/Lingu... | no public availability, no task type detected, no data splits |
| 156 | 2025-Kamath-Benchmarking Hindi LLMs A New Suite | 55 | https://huggingface.co/datasets/nvidi... | no public availability |
| 157 | 2025-Lab-ArmBench-LLM A Benchmark for Evaluating Large Language Models on | 55 | https://huggingface.co/spaces/metric-... | no public availability, no PDF extract details |
| 158 | 2025-Lahmar-IslamTrust A Benchmark for LLMs Alignment with Islamic Values | 55 | https://huggingface.co/QCRI/Fanar-1-9... | no public availability, no metrics found |
| 159 | 2025-Laukkonen-Contemplative Artificial Intelligence | 55 | https://osf.io/az59t | no task type detected, no metrics found, no data splits |
| 160 | 2025-Lazzaroni-MedBench-IT A Comprehensive Benchmark for Evaluating LLMs on Italian | 55 | https://huggingface.co/anakin87/gemma... | no public availability, no data splits |
| 161 | 2025-Le Jeune-Phare A Safety Probe for Large Language Models | 55 | https://huggingface.co/datasets/giska... | no public availability |
| 162 | 2025-Li-SafetyAnalyst Interpretable Transparent and Steerable Safety | 55 | https://jl3676.github.io/SafetyAnalyst/ |  |
| 163 | 2025-consortium-Charting the European LLM Benchmarking Landscape A New Taxonomy and a | 55 | https://huggingface.co/spaces/sdadas | no public availability, no metrics found, no data splits |
| 164 | 2026-Chen-PoliBias Parliamentary Voting Records | 55 | https://huggingface.co/projecte-aina/... | no public availability, no task type detected, no metrics found, no data splits |
| 165 | 2026-Guey-BiasLab Multilingual Dual-Framing Framework | 55 | https://github.com/williamguey/LLMbia... | no metrics found |
| 166 | 2026-He-GVS-Scale and GVS-Bench GenAI Value Safety Scale | 55 | https://github.com/acl2026/GVS-Bench | no task type detected, no metrics found, no data splits |
| 167 | 2026-Jin-MedES Chinese Medical Ethics Scenarios | 55 | https://github.com/X-LANCE/MedEthicAlign | no data splits |
| 168 | 2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks | 55 | NA | no task type detected, no metrics found |
| 169 | 2019-Phuong-Emotion Recognition for Vietnamese Social Media Text | 55 | https://github.com/vncorenlp/VnCoreNLP | no data splits |
| 170 | 2020-Mathew-HateXplain | 55 | https://github.com/punyajoy/HateXplain | no task type detected, no metrics found, no data splits |
| 171 | 2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate | 55 | https://github.com/guscode/dkhate | no task type detected, no data splits |
| 172 | 2023-Maity-A Deep Learning Framework for the Detection of Malay Hate Speech | 55 | https://github.com/MaityKrishanu/Hate... | no data splits |
| 173 | 2023-Nhan-ViGPTQA - State-of-the-Art LLMs for Vietnamese Question Answering | 55 | https://huggingface.co/VietAI/gpt-neo-1 | no public availability, no metrics found |
| 174 | 2023-Pires-Sabiá Portuguese Large Language Models | 55 | https://huggingface.co/EleutherAI/gpt... | no public availability, no task type detected |
| 175 | 2023-Schwarting-The eBible Corpus Data and Model | 55 | https://huggingface.co/datasets/bible... | no public availability, no task type detected |
| 176 | 2023-Shen-“Do Anything Now” | 55 | https://github.com/verazuo/jailbreak_... | no task type detected, no data splits |
| 177 | 2023-Susanto-BHASA A Holistic Southeast Asian Linguistic | 55 | https://github.com/aisingapore/BHASA | no metrics found |
| 178 | 2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models | 55 | https://github.com/wjwillemse/dumb |  |
| 179 | 2023-researchers-Transformer-Based Language Models for Bulgarian | 55 | https://huggingface.co/rmihaylov/bert... | no public availability, no metrics found |
| 180 | 2024-Mozafari-Offensive Language Detection in Low Resource Languages A Use Case of | 55 | https://github.com/ICTRC/Parsivar |  |
| 181 | 2024-Nayak-Benchmarking Vision Language Models for Cultural Understanding | 55 | https://culturalvqa.org |  |
| 182 | 2024-Nguyen-ViLLM-Eval A Comprehensive Evaluation Suite for Vietnamese Large | 55 | https://github.com/ZaloAI-Jaist/VMLU |  |
| 183 | 2024-Ortiz-Spanish and LLM Benchmarks Is MMLU Lost in Translation | 55 | https://huggingface.co/spaces/Hugging... | no public availability, no metrics found |
| 184 | 2024-Piatti-Cooperate or Collapse | 55 | https://github.com/giorgiopiatti/GovSim | no task type detected, no metrics found |
| 185 | 2024-Pikuliak-Women Are Beautiful Men Are Leaders Gender Stereotypes in Machine | 55 | https://github.com/kinit-sk/gest | no metrics found |
| 186 | 2024-Porkaew-Representing the Under-Represented Cultural and Core | 55 | https://github.com/UpstageAI/ThaiCLI_H6 |  |
| 187 | 2024-Qiu-ProgressGym | 55 | https://github.com/PKU-Alignment/Prog... | no task type detected, no metrics found, no data splits |
| 188 | 2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation | 55 | https://github.com/SALT-NLP/unintende... | no metrics found, no data splits |
| 189 | 2024-Sahoo-IndiBias - Benchmark Dataset for Social Biases in Indian Context | 55 | https://github.com/sahoonihar/IndiBias | no metrics found |
| 190 | 2024-Seth-DOSA A Dataset of Social Artifacts from Different Indian Geographical | 55 | NA |  |
| 191 | 2024-Sewunetie-Gender Bias Evaluation in Machine Translation for Amharic Tigrigna | 55 | https://github.com/manandey/bias_ |  |
| 192 | 2024-Sharma-Towards Understanding Sycophancy in Language Models | 55 | https://github.com/meg-tong/sycophanc... | no metrics found |
| 193 | 2024-Team-FABLE Fairness and Bias in LLM Evaluation | 55 | https://github.com/uclanlp/Fact-or-Fair | no task type detected |
| 194 | 2024-Wibowo-COPAL-ID Indonesian Language Reasoning with Local Culture and Nuances | 55 | https://github.com/haryoa/COPAL-ID | no task type detected |
| 195 | 2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding | 55 | https://github.com/yuting-wei/AC-EVAL | no metrics found, no data splits |
| 196 | 2024-Wu-WorldValuesBench | 55 | https://github.com/Demon702/WorldValu... | no task type detected, no metrics found, no data splits |
| 197 | 2024-Xu-Exploring Multilingual Concepts of Human Value in Large Language | 55 | https://github.com/antonisa/lang2vec | no metrics found |
| 198 | 2024-Yan-M$^3$oralBench | 55 | https://github.com/BeiiiY/M3oralBench | no metrics found |
| 199 | 2024-Yin-SafeAgentBench | 55 | https://github.com/shengyin1224/SafeA... | no task type detected, no metrics found |
| 200 | 2024-Yin-SafeWorld Geo-Diverse Safety Alignment | 55 | https://github.com/PlusLabNLP/SafeWorld |  |
| 201 | 2024-Yuan-R-Judge | 55 | https://github.com/Lordog/R-Judge | no data splits |
| 202 | 2024-Zhang-SafetyBench | 55 | https://github.com/thu-coai/SafetyBench |  |
| 203 | 2024-Zhuge-Agent-as-a-Judge | 55 | https://huggingface.co/devai-benchmark | no public availability, no data splits |
| 204 | 2024-team-MahaMarathi-7B Marathi Large Language Model | 55 | https://huggingface.co/marathi-llm/Ma... | no public availability, no PDF extract details |
| 205 | 2025-Maji-SANSKRITI A Comprehensive Benchmark for Evaluating | 55 | https://huggingface.co/datasets/13ari/Sa | no public availability, no metrics found, no data splits |
| 206 | 2025-Miranda-FilBench Can LLMs Understand and Generate Filipino | 55 | https://huggingface.co/spaces/OALL | no public availability, no metrics found |
| 207 | 2025-Mohammed-Cross-Language Approach for Quranic QA | 55 | https://huggingface.co/datasets/rajpu... | no public availability |
| 208 | 2025-Myung-PapersPlease | 55 | https://github.com/yeonsuuuu28/papers... | no metrics found, no data splits |
| 209 | 2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for | 55 | https://huggingface.co/datasets/Dangi... | no public availability |
| 210 | 2025-Oh-Evaluating LLMs’ Language Confusion in Code-switching Context Juhyun | 55 | https://huggingface.co/LGAI-EXAONE/EX... | no public availability |
| 211 | 2025-Peng-Plutus Benchmarking Large Language Models in Low-Resource Greek | 55 | https://huggingface.co/collections/Th... | no public availability, no data splits |
| 212 | 2025-Rahman-CCD-Bench Probing Cultural Conflict in LLM Decision-Making | 55 | https://github.com/smartlab-nyu/CCD-B... |  |
| 213 | 2025-Rinki-Measuring South Asian Biases in Large | 55 | https://huggingface.co/Telugu-LLM-Lab... | no public availability, no metrics found |
| 214 | 2025-Roussis-Krikri Advancing Open Large Language Models for Greek | 55 | https://huggingface.co/ilsp/Llama-Kri... | no public availability, no task type detected |
| 215 | 2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks | 55 | https://huggingface.co/spaces/OALL | no public availability, no metrics found, no data splits |
| 216 | 2025-Sakhadib-Towards Inclusive Arabic LLMs A Culturally Aligned Benchmark in | 55 | https://huggingface.co/datasets/opena... | no public availability, no task type detected, no data splits |
| 217 | 2025-Sekine-AnswerCarefully A Dataset for Improving the | 55 | https://huggingface.co/datasets/llm-j... | no public availability |
| 218 | 2025-Shin-RoleConflictBench A Benchmark of Role Conflict Scenarios for | 55 | https://github.com/ddindidu/RoleConfl... | no task type detected, no metrics found |
| 219 | 2025-Shmidman-NeoDictaBERT Pushing the Frontier of BERT models for Hebrew | 55 | https://huggingface.co/dicta-il/neodi... | no public availability |
| 220 | 2025-Snoswell-Beyond Verdicts LLM Moral Competence | 55 | NA | no task type detected |
| 221 | 2025-Son-From KMMLU-Redux to KMMLU-Pro A Professional Korean Benchmark Suite | 55 | https://huggingface.co/datasets/LGAI-... | no public availability, no task type detected |
| 222 | 2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean | 55 | https://huggingface.co/meta-llama/Lla... | no public availability |
| 223 | 2025-Sun-CASE-Bench | 55 | https://github.com/BriansIDP/CASEBench | no task type detected, no metrics found |
| 224 | 2025-Topal-How do LLMs perform on Turkish A multi-faceted multi-prompt evaluation | 55 | https://huggingface.co/collections/Ho... | no public availability, no PDF extract details |
| 225 | 2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English | 55 | https://huggingface.co/datasets/Relia... | no public availability |
| 226 | 2025-University-CUS-QA Local-Knowledge-Oriented Open-Ended Question Answering Dataset | 55 | https://huggingface.co/datasets/ufal | no public availability |
| 227 | 2025-Verma-MILU A Multi-task Indic Language Understanding | 55 | https://huggingface.co/datasets/ai4bh... | no public availability, no task type detected, no data splits |
| 228 | 2025-Xia-SafeToolBench | 55 | https://github.com/BITHLP/SafeToolBench | no task type detected, no data splits |
| 229 | 2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal | 55 | https://sorry-bench.github.io | no task type detected, no data splits |
| 230 | 2025-Yesil-Yesil o1 Pro | 55 | https://huggingface.co/datasets/yesil... | no public availability, no data splits |
| 231 | 2025-Yoon-Korean Canonical Legal Benchmark Toward Knowledge-Independent | 55 | https://github.com/openai/tiktoken | no public availability, no data splits |
| 232 | 2025-Zhang-OmniEduBench A Comprehensive Chinese Benchmark for Evaluating Large | 55 | https://huggingface.co/ERC-ITEA/MuduoLLM | no public availability, no data splits |
| 233 | 2025-Zhou-SocialEval Evaluating Social Intelligence of Large Language Models | 55 | https://github.com/thu-coai/SocialEval | no metrics found |
| 234 | 2025-Zosa-Got Compute but No Data Lessons From Post-training a Finnish LLM | 55 | https://huggingface.co/LumiOpen/Poro-... | no public availability, no task type detected |
| 235 | 2025-team-comparIA The French Government's LLM arena to collect French-language | 55 | https://huggingface.co/datasets/minis... | no public availability, no task type detected, no metrics found |
| 236 | 2026-Wrobel-Bielik Guard Efficient Polish Language Safety Classifiers for LLM | 55 | https://huggingface.co/speakleash/Bie... | no public availability |
| 237 | 2024-Bhardwaj-Language Models are Homer Simpson! Safety | 53 | https://github.com/declare-lab/resta | no public availability, no task type detected, no metrics found |
| 238 | 2024-Kirgis-Differences in Moral Foundations of LLMs | 53 | https://github.com/peterkirgis/llm-mo... | no public availability, no task type detected, no metrics found |
| 239 | 2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment | 52 | NA | no public availability, no metrics found |
| 240 | 2018-Bohra-Hindi-English Code-Mixed Social Media Text for | 50 | https://github.com/deepanshu1995/Hate... | no task type detected, no data splits |
| 241 | 2018-Crone-The Socio-Moral Image Database (SMID) | 50 | https://osf.io/2rqad/ | no task type detected, no data splits |
| 242 | 2020-Bosco-HaSpeeDe 2 @ EVALITA2020 Overview of the EVALITA 2020 Hate Speech | 50 | https://github.com/msang/haspeede/tre... | no task type detected, no metrics found, no data splits |
| 243 | 2020-Koutsikakis-GREEK-BERT The Greeks visiting Sesame Street | 50 | https://huggingface.co/nlpaueb/bert-b... | no public availability, no metrics found |
| 244 | 2021-Enevoldsen-DaCy A Unified Framework for Danish NLP | 50 | https://github.com/centre-for-humanit... | no task type detected |
| 245 | 2021-Lourie-Scruples | 50 | https://github.com/allenai/scruples | no task type detected, no metrics found |
| 246 | 2022-Atwell-Challenging the Transformer-based Models with a | 50 | https://github.com/ShathaTm/Quran_Had... | no PDF extract details |
| 247 | 2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language | 50 | https://github.com/bharathichezhiyan/... | no metrics found, no data splits |
| 248 | 2022-Demus-DeTox A Comprehensive Dataset for German Offensive Language and | 50 | https://github.com/hdaSprachtechnolog... |  |
| 249 | 2022-Jafri-A Multi-Modal Dataset for Hate Speech Detection on Social Media | 50 | https://github.com/therealthapa/emnlp... | no data splits |
| 250 | 2022-Jahan-Finnish Hate-Speech Detection on Social Media Using CNN and FinBERT | 50 | https://github.com/saroarjahan/FinBERT | no public availability, no data splits |
| 251 | 2022-Jeong-KOLD Korean Offensive Language Dataset | 50 | http://github.com/boychaboy/KOLD | no metrics found |
| 252 | 2022-Joshi-L3Cube-MahaNLP Marathi Natural Language Processing Datasets | 50 | https://github.com/l3cube-pune/Marath... | no metrics found |
| 253 | 2023-Boddington-Normative Ethical Theory AI Ethics | 50 | https://huggingface.co/microsoft/debe... | no public availability, no metrics found |
| 254 | 2023-Das-Toward Cultural Bias Evaluation Datasets The Case of Bengali Gender | 50 | NA | no task type detected, no metrics found, no data splits |
| 255 | 2023-Fischer-What does ChatGPT return about human values | 50 | https://osf.io/w46nq/ |  |
| 256 | 2023-Hamad-Offensive Hebrew Corpus and Detection using BERT | 50 | https://github.com/SinaLab/OffensiveH... | no data splits |
| 257 | 2023-Hoang-ViHOS Hate Speech Spans Detection for Vietnamese | 50 | https://github.com/phusroyal/ViHOS | no data splits |
| 258 | 2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content | 50 | https://github.com/ZILiAT-NASK/BAN-PL |  |
| 259 | 2024-Aupi-WoNBias A Complete Bengali Gender Bias Dataset | 50 | https://huggingface.co/datasets/gende... | no public availability, no metrics found |
| 260 | 2024-Cahyawijaya-High-Dimension Human Value Representation in | 50 | NA | no public availability, no metrics found |
| 261 | 2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora | 50 | https://github.com/ChrisIsKing/Caribb... | no task type detected, no metrics found, no data splits |
| 262 | 2024-Debenedetti-SaTML LLM CTF Dataset | 50 | https://huggingface.co/datasets/ethz-... | no public availability, no metrics found, no data splits |
| 263 | 2024-Hossein-ParsOffensive Persian Offensive Comments Dataset | 50 | https://huggingface.co/HooshvareLab/r... | no public availability, no data splits |
| 264 | 2024-Jiang-Can Language Models Reason about Individualistic | 50 | https://github.com/liweijiang/indievalue | no task type detected |
| 265 | 2024-Kaiyom-HELM Safety | 50 | https://github.com/stanford-crfm/helm |  |
| 266 | 2024-Khandelwal-Indian-BhED - A Dataset for Measuring India-Centric Biases in LLMs | 50 | https://github.com/khyatikhandelwal/I... | no task type detected, no metrics found |
| 267 | 2024-Liu-Controllable Preference Optimization | 50 | https://huggingface.co/datasets/openb... | no public availability, no metrics found |
| 268 | 2024-Liu-Cultural Bias and Cultural Alignment of Large Language Models | 50 | https://osf.io/preprints | no metrics found |
| 269 | 2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of | 50 | NA |  |
| 270 | 2025-Akpobi-Yankari Monolingual Yoruba Dataset | 50 | https://huggingface.co/datasets/acflp... | no public availability, no task type detected, no metrics found, no data splits |
| 271 | 2025-Aleid-Hajj-FQA | 50 | https://github.com/Omarito2412/ASKFM | no public availability |
| 272 | 2025-Alwajih-Palm | 50 | https://github.com/UBC-NLP/palm |  |
| 273 | 2025-Backmann-When Ethics and Payoffs Diverge | 50 | https://github.com/sbackmann/moralsim | no task type detected, no metrics found |
| 274 | 2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection | 50 | https://github.com/Juulba/Dutch-count... |  |
| 275 | 2025-Becker-The Moralization Corpus | 50 | https://anonymous.4open.science/r/Mor... | no task type detected, no metrics found |
| 276 | 2025-Bengoetxea-Lost in Variation Evaluating NLI Performance in Basque and Spanish | 50 | https://huggingface.co/datasets/HiTZ/... | no public availability, no data splits |
| 277 | 2025-Bhattacharjee-INDOHATEMIX A Multi-Target Code-Mixed Hindi-English Hate | 50 | https://huggingface.co/Qwen/Qwen2.5-7B | no public availability, no metrics found, no data splits |
| 278 | 2025-Bouchard-How to Assess Your LLM Use Case for Bias and | 50 | https://github.com/cvs-health/langfair | no metrics found |
| 279 | 2025-Cao-Measuring Hong Kong Massive Multi-Task Language Understanding HKMMLU | 50 | https://huggingface.co/datasets/chuxu... | no public availability |
| 280 | 2025-Castricato-PERSONA Pluralistic Alignment Testbed | 50 | https://www.synthlabs.ai/research/per... | no metrics found |
| 281 | 2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment | 50 | https://github.com/Social-Futures-Lab... | no task type detected, no metrics found |
| 282 | 2025-Chiu-Will AI Tell Lies to Save Sick Children | 50 | https://hf.co/datasets/kellycyy/AIRis... | no task type detected, no metrics found |
| 283 | 2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation | 50 | https://github.com/fxsjy/jieba | no public availability |
| 284 | 2025-Farid-One Model, Many Morals | 50 | https://github.com/sualehafarid/moral... | no public availability, no task type detected |
| 285 | 2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a | 50 | https://huggingface.co/datasets | no public availability |
| 286 | 2025-Helwe-Navigating the Political Compass Multilingual 50 Countries | 50 | https://github.com/sadiakamal/Detaile... | no metrics found |
| 287 | 2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models | 50 | https://github.com/THUYRan/LLM-Fairness | no metrics found, no data splits |
| 288 | 2025-Laiyk-Instruction Tuning on Public Government and Cultural Data for | 50 | https://huggingface.co/datasets/AmanM... | no public availability, no metrics found |
| 289 | 2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities | 50 | https://github.com/andyjliu/conflicts... | no public availability, no metrics found, no data splits |
| 290 | 2025-Liu-InstrumentalEval | 50 | https://github.com/yf-he/Instrumental... | no public availability, no task type detected, no metrics found |
| 291 | 2026-Alam-Quran-MD A Fine-Grained Multilingual Multimodal Dataset | 50 | https://huggingface.co/datasets/Buraa... | no public availability, no data splits |
| 292 | 2026-Lee-BiasJailbreak | 50 | https://github.com/Isaac-theori/BiasJ... | no task type detected, no data splits |
| 293 | 2018-Mishra-Are They Our Brothers Analysis and | 50 | https://github.com/nuhaalbadi/Arabic_... | no task type detected, no metrics found, no data splits |
| 294 | 2020-Mollas-ETHOS an Online Hate Speech Detection Dataset | 50 | https://github.com/intelligence-csd-a... | no task type detected, no metrics found, no data splits |
| 295 | 2020-Souza-BERTimbau Pretrained BERT Models for Brazilian Portuguese | 50 | https://huggingface.co/neuralmind/ber... | no public availability, no PDF extract details |
| 296 | 2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media | 50 | https://github.com/tarudesu/ViCTSD | no task type detected, no data splits |
| 297 | 2021-Team-Slovenian Twitter Hate Speech Dataset IMSyPP-sl | 50 | https://www.clarin.si/repository/xmlu... | no PDF extract details |
| 298 | 2022-Micallef-Pre-training Data Quality and Quantity for a Low-Resource Language | 50 | https://huggingface.co/MLRS/BERTu | no public availability, no metrics found |
| 299 | 2022-Nguyen-SMTCE A Social Media Text Classification Evaluation Benchmark and | 50 | https://github.com/binhvq/news-corpus | no public availability |
| 300 | 2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language | 50 | https://data.mendeley.com/datasets/x6... | no PDF extract details |
| 301 | 2022-Schramowski-I2P Inappropriate Image Prompts Test Bed | 50 | https://github.com/ml-research/Q16 | no task type detected, no metrics found |
| 302 | 2022-Trager-The Moral Foundations Reddit Corpus | 50 | NA | no metrics found |
| 303 | 2023-Miah-Islam QA | 50 | https://www.kaggle.com/datasets/abdul... | no metrics found, no data splits |
| 304 | 2023-Ramezani-Knowledge of Cultural Moral Norms in Large Language Models | 50 | https://github.com/AidaRamezani/cultu... | no metrics found, no data splits |
| 305 | 2023-Yao-Value FULCRA | 50 | https://ValueCompass.github.io | no metrics found |
| 306 | 2023-Ziems-NormBank | 50 | https://github.com/SALT-NLP/normbank | no metrics found |
| 307 | 2023-team-Albertina Advancing Neural Encoding of Portuguese | 50 | https://huggingface.co/PORTULAN/alber... | no public availability, no task type detected, no metrics found, no data splits |
| 308 | 2024-Maxutov-Do LLMs Speak Kazakh A Pilot Evaluation of Seven Models | 50 | https://github.com/akylbekmaxutov/LLM... | no metrics found |
| 309 | 2024-Mou-SGBench | 50 | https://github.com/MurrayTom/SG-Bench | no metrics found |
| 310 | 2024-Ptaszynski-Expert-Annotated Dataset to Study Cyberbullying in Polish Language | 50 | https://github.com/bear/python-twitter | no data splits |
| 311 | 2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and | 50 | https://github.com/Khushangz/Cross-Cu... | no task type detected, no data splits |
| 312 | 2024-Ranasinghe-SOLD Sinhala Offensive Language Dataset | 50 | https://github.com/Sinhala-NLP/SOLD | no task type detected, no metrics found |
| 313 | 2024-Rehm-Investigating Gender Bias in Turkish Language | 50 | https://github.com/W4ngatang/sent-bias | no task type detected, no metrics found |
| 314 | 2024-Rozado-The Political Preferences of LLMs | 50 | https://doi.org/10.5281/zenodo.10553530 | no task type detected, no metrics found |
| 315 | 2024-Saffari-PSN | 50 | https://github.com/hamidds/ISN | no metrics found |
| 316 | 2024-Satar-Seeing Culture Benchmark Evaluating VLMs on Culturally Rich Images | 50 | https://huggingface.co/datasets/Multi... | no public availability, no PDF extract details |
| 317 | 2024-Schmeisser-Nieto-Overview of DETESTS-Dis at IberLEF 2024 DETEction and Classification | 50 | https://detests-dis.github.io/ | no metrics found, no data splits |
| 318 | 2024-Shahi-Hate Speech Detection Using Cross-Platform Social Media Data In | 50 | https://github.com/Gautamshahi/Biling... |  |
| 319 | 2024-Shi-CultureBank An Online Community-Driven Knowledge Base Towards | 50 | https://github.com/SALT-NLP/CultureBank | no metrics found, no data splits |
| 320 | 2024-Silva-Gender Bias in Portuguese Literary Texts A Masked Language Model | 50 | https://huggingface.co/neuralmind/ber... | no public availability, no metrics found |
| 321 | 2024-Son-KMMLU Measuring Massive Multitask Language Understanding in Korean | 50 | https://github.com/EleutherAI/lm-eval... |  |
| 322 | 2024-Staps-Large Language Models and Biblical Hebrew | 50 | https://huggingface.co/gngpostalsrvc/... | no public availability |
| 323 | 2024-Susanto-IndoToxic2024 A Demographically-Enriched Dataset of Hate Speech and | 50 | https://github.com/izzako/IndoToxic2024 |  |
| 324 | 2024-Team-GuardBench | 50 | https://github.com/AmenRa/guardbench | no metrics found |
| 325 | 2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian | 50 | https://github.com/DougTrajano/olid-br | no PDF extract details |
| 326 | 2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation | 50 | https://github.com/stair-lab/villm | no data splits |
| 327 | 2024-University-Using LLMs to Discover Emerging Coded | 50 | https://huggingface.co/learn/nlp-course | no public availability, no task type detected, no metrics found, no data splits |
| 328 | 2024-Velankar-SamPar A Marathi Hate Speech Dataset | 50 | https://github.com/l3cube-pune/Marath... | no PDF extract details |
| 329 | 2024-Wang-All Languages Matter | 50 | https://github.com/Jarviswang94/Multi... | no metrics found |
| 330 | 2024-Wang-XSafety Multilingual Safety Benchmark | 50 | https://github.com/Jarviswang94/Multi... | no PDF extract details |
| 331 | 2024-Zeng-LLM-GLOBE A Benchmark Evaluating the Cultural | 50 | https://github.com/raovish6/LLM-GLOBE | no metrics found |
| 332 | 2024-Zeng-Quantifying Risk Propensities of Large Language | 50 | https://huggingface.co/Qwen/Qwen2.5-7... | no public availability, no metrics found |
| 333 | 2025-Monazzah-PerCul A Story-Driven Cultural Evaluation of LLMs in Persian | 50 | https://huggingface.co/datasets/teias... | no public availability |
| 334 | 2025-Nair-Do Language Models Think Consistently | 50 | https://github.com/launchnlp/ValuePre... | no metrics found, no data splits |
| 335 | 2025-Patel-Evaluating Large Language Models for Detecting | 50 | https://huggingface.co/RedHatAI/Meta-... | no public availability, no data splits |
| 336 | 2025-Paul-Aligning Large Language Models to Low-Resource | 50 | https://huggingface.co/datasets/nvidi... | no public availability, no task type detected, no metrics found |
| 337 | 2025-Rusnak-EudAImonia | 50 | https://huggingface.co/blog/rlhf | no public availability, no task type detected, no metrics found, no data splits |
| 338 | 2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas | 50 | https://github.com/dlab-projects/norm... | no metrics found |
| 339 | 2025-Sadallah-Commonsense Reasoning in Arab Culture | 50 | https://huggingface.co/datasets/MBZUA... | no public availability |
| 340 | 2025-Saffari-Can I introduce my boyfriend to my grandmother | 50 | https://github.com/hamidds/ISN | no metrics found |
| 341 | 2025-Samway-Are Language Models Consequentialist or Deontological | 50 | https://github.com/keenansamway/moral... |  |
| 342 | 2025-Schacht-Mapping Moral Reasoning Circuits | 50 | https://github.com/coairesearch/mappi... | no metrics found |
| 343 | 2025-Seweryn-PLLuM-Align Polish Preference Dataset for Large Language Model | 50 | https://huggingface.co/datasets/argilla | no public availability |
| 344 | 2025-Shen-ValueActionLens Mind the Value-Action Gap | 50 | https://github.com/huashen218/value_a... | no task type detected, no metrics found |
| 345 | 2025-Shen-ValueCompass A Framework for Measuring Contextual Value Alignment | 50 | https://github.com/huashen218/value_a... | no task type detected |
| 346 | 2025-Simhi-ManagerBench Evaluating Safety-Pragmatism Trade-off in Managerial | 50 | https://github.com/technion-cs-nlp/Ma... | no task type detected, no metrics found, no data splits |
| 347 | 2025-Song-The Hallucination Tax of Reinforcement Finetuning | 50 | https://huggingface.co/datasets/lime-... | no public availability |
| 348 | 2025-Sorensen-Operationalizing Pluralistic Values | 50 | https://github.com/DALIAALISIDDIG/Ali... | no task type detected, no metrics found, no data splits |
| 349 | 2025-Team-EuroGEST Investigating Gender Stereotypes in Multilingual Language | 50 | https://huggingface.co/datasets/utter... | no public availability, no task type detected |
| 350 | 2025-Tumur-Ochir-Evaluating Large Language Models in Mongolian | 50 | https://huggingface.co/Qwen/Qwen2 | no public availability |
| 351 | 2025-Wu-The Staircase of Ethics Multi-step Moral Dilemmas | 50 | https://isir-wuya.github.io/Multi-ste... | no metrics found |
| 352 | 2025-Yong-The State of Multilingual LLM Safety Research From Measuring the | 50 | https://huggingface.co/CohereLabsComm... | no public availability, no task type detected, no metrics found |
| 353 | 2025-Yoo-Code-Switching Curriculum Learning for Multilingual ... | 50 | https://huggingface.co/datasets/opena... | no public availability, no metrics found |
| 354 | 2025-Yoo-Code-Switching Red-Teaming LLM Evaluation for Safety and Multilingual | 50 | https://huggingface.co/datasets/opena... | no public availability, no task type detected, no metrics found, no data splits |
| 355 | 2025-Zhang-AISafetyLab | 50 | https://github.com/thu-coai/AISafetyLab | no metrics found |
| 356 | 2025-team-WangchanThaiInstruct An Instruction-Following Dataset for Culture-Aware | 50 | https://huggingface.co/datasets/aires... | no public availability |
| 357 | 2026-team-SEA-Guard Culturally Grounded Multilingual Safeguard for | 50 | https://huggingface.co/aisingapore/Qw... | no public availability, no metrics found |
| 358 | 2023-Bang-Towards Answering Open-ended Ethical Quandary | 47 | NA | no public availability, no data splits |
| 359 | 2025-Kim-A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs | 47 | https://github.com/seank021/LLM-Bias-... | no public availability |
| 360 | 2025-Liu-On the Convergence of Moral Self-Correction in LLMs | 47 | NA | no public availability, no metrics found |
| 361 | 2019-De-Arteaga-Bias in Bios | 45 | http://aka.ms/biasbios | no public availability, no data splits |
| 362 | 2019-Ibrohim-Multi-label Hate Speech and Abusive Language | 45 | https://github.com/okkyibrohim/id-mul... | no public availability, no task type detected, no data splits |
| 363 | 2019-Jikeli-Annotating Antisemitic Online Content Towards an | 45 | NA | no public availability, no data splits |
| 364 | 2022-Abbasi-Deep Learning for Religious and Continent-Based | 45 | NA | no public availability |
| 365 | 2022-Alsuhaibani-Fabricated Hadith Detection A Novel Matn-Based | 45 | MAHADDAT dataset (released with paper) | no task type detected, no metrics found, no data splits |
| 366 | 2022-Bai-Constitutional AI | 45 | https://github.com/anthropics/Constit... | no public availability, no task type detected, no metrics found |
| 367 | 2022-Bang-Enabling Classifiers to Make Judgements | 45 | https://github.com/makcedward/nlpaug | no public availability |
| 368 | 2022-Fraser-Does Moral Code Have a Moral Code | 45 | https://svkir.com/projects/moralQ.html | no public availability, no task type detected, no metrics found |
| 369 | 2023-Augustyniak-Massively Multilingual Corpus of Sentiment Datasets and Multi-faceted | 45 | https://github.com/wongnai/wongnai-co... | no public availability, no metrics found |
| 370 | 2023-Cao-Assessing Cross-Cultural Alignment between | 45 | https://github.com/yongcaoplus/Probin... | no public availability, no metrics found |
| 371 | 2023-Catapang-EMoTES-3K | 45 | NA | no public availability |
| 372 | 2023-Khodabakhsh-PerBOLD A Big Dataset of Persian Offensive Language on Instagram | 45 | NA | no public availability, no metrics found, no data splits |
| 373 | 2024-Abdulhai-Moral Foundations of Large Language Models | 45 | https://github.com/abdulhaim/moral_fo... | no public availability, no metrics found |
| 374 | 2024-Anonymous-ForbiddenQuestions | 45 | https://github.com/verazuo/jailbreak_... | no public availability, no metrics found, no data splits |
| 375 | 2024-Dognin-Contextual Moral Value Alignment Through | 45 | NA | no public availability, no task type detected, no metrics found |
| 376 | 2024-Fetahi-AI-Based Hate Speech Detection in Albanian Social Media New Dataset | 45 | NA | no public availability, no data splits |
| 377 | 2024-Luong-Realistic Evaluation of Toxicity in Large | 45 | NA | no public availability, no metrics found, no data splits |
| 378 | 2025-Andric-Do LLMs Walk Their Talk Multi-Method Moral Evaluation Framework | 45 | https://github.com/sandroandric/LLMs_... | no public availability, no metrics found |
| 379 | 2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities | 45 | NA | no public availability |
| 380 | 2025-Chakraborty-Structured Moral Reasoning | 45 | NA | no public availability, no data splits |
| 381 | 2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value | 45 | NA | no public availability, no metrics found |
| 382 | 2025-Fenech-Borg-The Cultural Gene of Large Language Models | 45 | NA | no public availability, no task type detected, no metrics found |
| 383 | 2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ... | 45 | https://www.kaggle.com/datasets/black... | no public availability |
| 384 | 2025-Lai-Scaling the Multilingual Capability of LLMs with Cross- ... | 45 | https://github.com/boschresearch/ACL2... | no public availability, no task type detected, no metrics found |
| 385 | 2025-Li-Analyzing Cognitive Differences Among Large | 45 | NA | no public availability, no task type detected, no data splits |
| 386 | 2025-Liu-CultureVLM Characterizing and Improving Cultural Understanding of | 45 | https://culturevlm.github.io | no public availability, no metrics found |
| 387 | 2026-Li-PluriHarms | 45 | https://jl3676.github.io/PluriHarms | no public availability, no task type detected, no metrics found, no data splits |
| 388 | 2022-Taktasheva-TAPE Assessing Few-shot Russian Language Understanding | 45 | https://github.com/RussianNLP/TAPE | no metrics found |
| 389 | 2023-Muhammad-AfriSenti | 45 | https://github.com/afrisenti-semeval/... | no public availability, no data splits |
| 390 | 2023-TheDevastator-HelpSteer A-i Alignment Dataset | 45 | https://huggingface.co/datasets/nvidi... | no public availability, no task type detected, no metrics found, no data splits |
| 391 | 2023-TheDevastator-OpenAssistant Conversations (OASST1) | 45 | https://huggingface.co/datasets/OpenA... | no public availability, no metrics found, no data splits |
| 392 | 2023-Zheng-Large Language Models Are Not Robust Multiple | 45 | https://github.com/chujiezheng/LLM-MC... | no public availability |
| 393 | 2024-MLCommons-MLCommons AILuminate Benchmark | 45 | https://github.com/mlcommons/ailuminate | no task type detected, no metrics found, no data splits |
| 394 | 2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and | 45 | https://github.com/AIRI-Institute/EAI... | no task type detected, no data splits |
| 395 | 2024-Nayak-CulturalVQA Evaluating VLMs' Geo-Diverse Cultural Understanding | 45 | https://huggingface.co/datasets/mair-... | no public availability, no PDF extract details |
| 396 | 2024-Onose-LLMs for Extremely Low-Resource Finno-Ugric Languages | 45 | https://github.com/TartuNLP/smugri-llm | no metrics found |
| 397 | 2024-Park-Morality is Non-Binary | 45 | https://github.com/jeongwoopark0514/m... | no public availability, no metrics found |
| 398 | 2024-Singh-Aya Dataset | 45 | https://hf.co/CohereForAI/aya-101 | no public availability, no task type detected, no metrics found |
| 399 | 2024-Souly-StrongREJECT | 45 | https://strong-reject.readthedocs.io/ | no metrics found |
| 400 | 2024-Vladimirova-FairJob | 45 | https://huggingface.co/datasets/crite... | no public availability, no task type detected, no metrics found, no data splits |
| 401 | 2024-Wang-KULTURE Bench A Benchmark for Assessing Language Model in Korean | 45 | https://github.com/wangxiaonan-git/KU... |  |
| 402 | 2024-Zeng-Leveraging Large Language Models for Code-Mixed | 45 | https://github.com/lindazeng979/LLM-CMSA | no public availability |
| 403 | 2024-Zhang-Edu-Values - Evaluating Chinese Education Values of LLMs | 45 | https://github.com/zhangpeii/Edu-Values | no public availability, no metrics found |
| 404 | 2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via | 45 | https://github.com/SophieZheng998/ALI... | no metrics found |
| 405 | 2025-Sharmaa-Hate Speech Detection in Somali-English Code-Switched | 45 | https://github.com/anubhakabra/MoH_Ha... | no public availability, no data splits |
| 406 | 2025-Shen-HateBench | 45 | https://github.com/TrustAIRLab/HateBench | no public availability, no task type detected, no data splits |
| 407 | 2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in | 45 | https://github.com/TMMMU-Benchmark/ev... | no public availability |
| 408 | 2025-Unknown-MIZAN A Persian LLM Leaderboard | 45 | https://huggingface.co/spaces/MCINext... | no public availability, no PDF extract details |
| 409 | 2025-Wang-Measuring Desired Group Discrimination in LLMs | 45 | NA | no metrics found |
| 410 | 2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist | 45 | https://huggingface.co/datasets/Nethm... | no public availability, no PDF extract details |
| 411 | 2025-Yuan-Probabilistic Aggregation and Targeted Embedding | 45 | https://github.com/yuanchencn/Collect... | no public availability, no task type detected, no data splits |
| 412 | 2025-Zhou-Moral Reasoning Across Languages | 45 | https://anonymous.4open.science/r/eth... | no public availability |
| 413 | 2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in | 45 | https://anonymous.4open.science/r/Tro... | no metrics found |

## 4. Needs More Info (580 papers, score 30-44)

| # | Paper | Score | Missing Items |
|---|-------|-------|---------------|
| 1 | 2024-AlKhamissi-Investigating Cultural Alignment of LLMs | 43 | no public availability, no task type detected, no metrics found |
| 2 | 2024-Huang-Moral Persuasion in Large Language Models | 43 | no public availability, no metrics found |
| 3 | 2025-Elkins-Syntactic Framing Fragility SFF Robustness Evaluation of LLM Ethical | 43 | no public availability, no task type detected |
| 4 | 2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al. | 43 | no public availability, no task type detected |
| 5 | 2025-Liu-PersuSafety LLM Can be a Dangerous Persuader | 43 | no public availability, no task type detected, no metrics found, no data splits |
| 6 | 2026-Alam-From RAG to Agentic RAG for | 42 | no public availability |
| 7 | 2019-Horak-Benchmark Dataset for Propaganda Detection in Czech Newspaper Texts | 40 | no public availability, no task type detected, no data splits |
| 8 | 2019-Ljubesic-The FRENK Datasets of Socially Unacceptable Discourse in Slovene and | 40 | no task type detected, no metrics found |
| 9 | 2020-Hossu-UIC-NLP at SemEval-2020 Task 10 | 40 | no public availability, no task type detected, no metrics found |
| 10 | 2021-Croce-RobustBench | 40 | no public availability, no task type detected, no data splits |
| 11 | 2022-Ataei-Pars-OFF A Benchmark for Offensive Language Detection on Farsi Social | 40 | no public availability, no PDF extract details |
| 12 | 2022-Chalkidis-FairLex | 40 | no public availability, no task type detected, no metrics found |
| 13 | 2022-Hu-“I’m sorry to hear that” | 40 | no public availability |
| 14 | 2022-Kann-AmericasNLI | 40 | no public availability |
| 15 | 2023-Astobiza-MoralNet | 40 | no public availability, no task type detected |
| 16 | 2023-Huang-Vigogne French instruction-following and chat models | 40 | no public availability, no PDF extract details |
| 17 | 2023-Lee-KoSBI | 40 | no public availability, no metrics found |
| 18 | 2024-Alekseev-Benchmarking Multilabel Topic Classification in the Kyrgyz Language | 40 | no public availability, no metrics found |
| 19 | 2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said | 40 | no public availability, no metrics found |
| 20 | 2024-Burema-Evaluating Dutch Social Bias in Large Language Models | 40 | no task type detected, no metrics found, no data splits |
| 21 | 2024-Chen-ToMBench | 40 | no public availability, no metrics found |
| 22 | 2024-Chouhan-HindiLLM Large Language Model for Hindi | 40 | no public availability, no PDF extract details |
| 23 | 2024-CiTIUS-A Galician-Portuguese Generative Model | 40 | no public availability, no PDF extract details |
| 24 | 2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators - | 40 | no public availability |
| 25 | 2024-Kajiwara-Beyond Traditional Classifiers Evaluating Large Language Models for | 40 | no public availability, no PDF extract details |
| 26 | 2024-Kirch-TRIAGE | 40 | no public availability, no metrics found |
| 27 | 2024-Kumar-Indic-QA Benchmark A Multilingual Benchmark to | 40 | no public availability, no metrics found |
| 28 | 2024-Li-Preference Tuning For Toxicity Mitigation Generalizes Across Languages | 40 | no public availability |
| 29 | 2024-Li-Quantifying AI Psychology | 40 | no public availability, no metrics found |
| 30 | 2024-Lin-AI-Face | 40 | no public availability, no metrics found |
| 31 | 2025-Aggarwal-Letta Leaderboard | 40 | no public availability, no metrics found, no data splits |
| 32 | 2025-Alhassoun-Saudi-Alignment Benchmark - Assessing LLMs Alignment with Saudi | 40 | no public availability |
| 33 | 2025-Anonymous-BEATS | 40 | no public availability |
| 34 | 2025-Aravinda-SinLlama A Large Language Model for Sinhala | 40 | no public availability |
| 35 | 2025-Azmi-IndoSafety Culturally Grounded Safety for LLMs in Indonesian Languages | 40 | no public availability, no task type detected, no metrics found |
| 36 | 2025-Bang-HalluLens LLM Hallucination Benchmark | 40 | no public availability, no metrics found |
| 37 | 2025-Bhowmik-Evaluating LLMs' Multilingual Capabilities for Bengali Benchmark | 40 | no public availability |
| 38 | 2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for | 40 | no public availability, no data splits |
| 39 | 2025-Cao-SafeDialBench | 40 | no public availability, no task type detected |
| 40 | 2025-Cognitive-Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning | 40 | no public availability, no metrics found, no data splits |
| 41 | 2025-Cognitive-Improved Tibetan Word Vectors Models Based on Position Information | 40 | no public availability, no PDF extract details |
| 42 | 2025-Cognitive-Tibetan Text Classification based on Prompt Learning and Ensemble | 40 | no public availability, no PDF extract details |
| 43 | 2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark | 40 | no public availability |
| 44 | 2025-Derner-Leveraging Large Language Models to Measure Gender Representation | 40 | no public availability, no metrics found |
| 45 | 2025-Ebrahimi-AmericasNLI Evaluating Zero-shot Natural Language Understanding of | 40 | no public availability |
| 46 | 2025-Farsi-MELAC Massive Evaluation of Large Language Models with Alignment of | 40 | no public availability |
| 47 | 2025-Feng-CulFiT A Fine-grained Cultural-aware LLM Training Paradigm via | 40 | no public availability |
| 48 | 2025-Fiaz-UrduLLaMA 1.0 Dataset Curation Preprocessing and Evaluation in | 40 | no public availability |
| 49 | 2025-Firmino-Improving hate speech detection using Cross-Lingual Learning - | 40 | no public availability, no PDF extract details |
| 50 | 2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in | 40 | no public availability |

... and 530 more papers in this tier.

## 5. Not Implementable (754 papers, score < 30)

754 papers scored below 30 — primarily theoretical/philosophical papers, surveys, and position papers without associated datasets.

---
*Generated by lm-eval-harness Implementability Scanner*
*Data sources: 2,034 vault papers, 986 benchmark survey entries, 2035 PDF extracts*
