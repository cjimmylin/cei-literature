# OpenAI Evals Implementability Report

**Generated:** 2026-03-12  
**Papers scored:** 2043  
**Average score:** 6.86/10.0  
**Scoring model:** 9-dimension weighted (JSONL-convertible + template mapping = 1.5x each)  
**Framework:** [OpenAI Evals](https://github.com/openai/evals) — JSONL data + YAML registry configs

## Executive Summary

| Tier | Score Range | Count | % |
|------|------------|-------|---|
| Ready | 8.0-10.0 | 783 | 38.3% |
| Possible | 5.0-7.9 | 872 | 42.7% |
| Barriers | 2.0-4.9 | 306 | 15.0% |
| Not Implementable | 0.0-1.9 | 82 | 4.0% |
| **Total** | | **2043** | |

Papers with all three flags (benchmark+eval+dataset): 292

## 1. Ready (score >= 8.0)

783 papers can be implemented now with minimal effort.

| # | Paper | Score | Template | Data URL | Signals |
|---|-------|-------|----------|----------|---------|
| 1 | 2022-Bai-Training a Helpful and Harmless Assistant with | **10.0** | `Match` | https://github.com/anthropics/hh-rlhf | is_eval, is_dataset, Has DATA_URL, Code available |
| 2 | 2022-Liang-Holistic Evaluation of Language Models | **10.0** | `Match` | https://github.com/stanford-crfm/helm | is_benchmark, is_eval, Has DATA_URL, Code available |
| 3 | 2022-Parrish-BBQ Bias Benchmark for Question Answering | **10.0** | `Match` | https://github.com/nyu-mll/BBQ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 4 | 2022-Parrish-BBQ | **10.0** | `Match` | https://github.com/nyu-mll/BBQ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 5 | 2022-Taktasheva-TAPE Assessing Few-shot Russian Language Understanding | **10.0** | `Match` | https://github.com/RussianNLP/TAPE | is_benchmark, is_eval, Has DATA_URL, Code available |
| 6 | 2023-Huang-Flames | **10.0** | `Match` | https://github.com/AIFlames/Flames | is_benchmark, is_eval, Has DATA_URL, Code available |
| 7 | 2023-Liu-AlignBench | **10.0** | `Match` | https://github.com/THUDM/AlignBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 8 | 2023-Santurkar-Whose Opinions Do Language Models Reflect | **10.0** | `Match` | https://github.com/tatsu-lab/opinions_qa | is_eval, is_dataset, Has DATA_URL, Code available |
| 9 | 2023-Shen-“Do Anything Now” | **10.0** | `Match` | https://github.com/verazuo/jailbreak_llms | is_eval, is_dataset, Has DATA_URL, Code available |
| 10 | 2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models | **10.0** | `Match` | https://github.com/wjwillemse/dumb | is_benchmark, is_eval, Has DATA_URL, Code available |
| 11 | 2023-Wang-DecodingTrust | **10.0** | `Match` | https://huggingface.co/datasets/AI-Secure/Decoding | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 12 | 2023-Wang-STREAM | **10.0** | `Match` | https://safe-and-ethical.ai/stream/en | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 13 | 2023-Wang-SeaEval for Multilingual Foundation Models From Cross-Lingual | **10.0** | `Match` | https://github.com/SeaEval/SeaEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 14 | 2023-Xu-CValues | **10.0** | `Match` | https://github.com/X-PLUG/CValues | is_benchmark, is_eval, Has DATA_URL, Code available |
| 15 | 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models | **10.0** | `Match` | https://github.com/emrecanacikgoz/turkish-llm | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 16 | 2024-Ashraf-Arabic Dataset for LLM Safeguard Evaluation | **10.0** | `Match` | https://github.com/mbzuai-nlp/Arabic_safety_evalua | is_eval, is_dataset, Has DATA_URL, Code available |
| 17 | 2024-Bandarkar-The Belebele Benchmark a Parallel Reading Comprehension Dataset in | **10.0** | `Match` | https://github.com/openai/tiktoken | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 18 | 2024-Bang-BLEnD A Benchmark for LLMs on | **10.0** | `FuzzyMatch` | https://github.com/nlee0212/BLEnD | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 19 | 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU | **10.0** | `Match` | https://huggingface.co/datasets/miulab/tmlu | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 20 | 2024-Chern-BeHonest | **10.0** | `Match` | https://github.com/GAIR-NLP/BeHonest | is_benchmark, is_eval, Has DATA_URL, Code available |
| 21 | 2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation | **10.0** | `Match` | https://github.com/CentreSecuriteIA/BELLS | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 22 | 2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque | **10.0** | `Match` | https://github.com/hitz-zentroa/latxa | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 23 | 2024-Faisal-DialectBench A NLP Benchmark for Dialects Varieties and | **10.0** | `Match` | https://github.com/ffaisal93/DialectBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 24 | 2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model | **10.0** | `Match` | https://huggingface.co/croissantllm | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 25 | 2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian | **10.0** | `Match` | https://github.com/ai-forever/MERA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 26 | 2024-Guldimann-COMPL-AI EU AI Act Compliance | **10.0** | `Match` | https://github.com/compl-ai/compl-ai | is_benchmark, is_eval, Has DATA_URL, Code available |
| 27 | 2024-Gupta-WalledEval | **10.0** | `Match` | https://github.com/walledai/walledeval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 28 | 2024-Han-MedSafetyBench | **10.0** | `Match` | https://github.com/AI4LIFE-GROUP/med-safety-bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 29 | 2024-Huang-CBBQ | **10.0** | `Match` | https://github.com/YFHuangxxxx/CBBQ/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 30 | 2024-Huang-TrustLLM | **10.0** | `Match` | https://github.com/HowieHwong/TrustLLM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 31 | 2024-Ji-MoralBench | **10.0** | `Match` | https://github.com/agiresearch/MoralBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 32 | 2024-Jiang-Can Language Models Reason about Individualistic | **10.0** | `Match` | https://github.com/liweijiang/indievalue | is_eval, is_dataset, Has DATA_URL, Code available |
| 33 | 2024-Jiang-WildTeaming at Scale | **10.0** | `Match` | https://huggingface.co/datasets/allenai/wildjailbr | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 34 | 2024-Jin-Language Model Alignment in Multilingual Trolley | **10.0** | `Match` | https://github.com/causalNLP/multiTP | is_eval, is_dataset, Has DATA_URL, Code available |
| 35 | 2024-Li-SALAD-Bench | **10.0** | `Match` | https://github.com/OpenSafetyLab/SALAD-BENCH | is_benchmark, is_eval, Has DATA_URL, Code available |
| 36 | 2024-Li-Value-Spectrum | **10.0** | `FuzzyMatch` | https://github.com/Jeremyyny/Value-Spectrum | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 37 | 2024-MLCommons-MLCommons AILuminate Benchmark | **10.0** | `Match` | https://github.com/mlcommons/ailuminate | is_benchmark, is_eval, Has DATA_URL, Code available |
| 38 | 2024-Maxutov-Do LLMs Speak Kazakh A Pilot Evaluation of Seven Models | **10.0** | `Match` | https://github.com/akylbekmaxutov/LLM-eval-using-K | is_eval, is_dataset, Has DATA_URL, Code available |
| 39 | 2024-Montalan-Kalahi A handcrafted grassroots cultural LLM evaluation suite for | **10.0** | `Match` | https://github.com/aisingapore/kalahi | is_benchmark, is_eval, Has DATA_URL, Code available |
| 40 | 2024-Neplenbroek-MBBQ A Dataset for Cross-Lingual Comparison of Stereotypes in | **10.0** | `Match` | https://github.com/Veranep/MBBQ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 41 | 2024-Nguyen-ViLLM-Eval A Comprehensive Evaluation Suite for Vietnamese Large | **10.0** | `Match` | https://github.com/ZaloAI-Jaist/VMLU | is_benchmark, is_eval, Has DATA_URL, Code available |
| 42 | 2024-Pfister-SuperGLEBer German Language Understanding Evaluation Benchmark | **10.0** | `Match` | https://github.com/LSX-UniWue/SuperGLEBer | is_benchmark, is_eval, Has DATA_URL, Code available |
| 43 | 2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and | **10.0** | `Match` | https://huggingface.co/elmrc | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 44 | 2024-Ren-ValueBench | **10.0** | `Match` | https://github.com/Value4AI/ValueBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 45 | 2024-Romanou-INCLUDE Evaluating Multilingual Language Understanding with Regional | **10.0** | `Match` | https://huggingface.co/papers/2411.19799 | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 46 | 2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety | **10.0** | `Match` | https://github.com/paul-rottger/safetyprompts-pape | is_eval, is_dataset, Has DATA_URL, Code available |
| 47 | 2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation | **10.0** | `Match` | https://github.com/SALT-NLP/unintended-impacts-of- | is_benchmark, is_eval, Has DATA_URL, Code available |
| 48 | 2024-Saffari-PSN | **10.0** | `Match` | https://github.com/hamidds/ISN | is_eval, is_dataset, Has DATA_URL, Code available |
| 49 | 2024-Schutze-TurkishMMLU Measuring Massive Multitask Language Understanding | **10.0** | `Match` | https://github.com/ArdaYuksel/TurkishMMLU | is_benchmark, is_eval, Has DATA_URL, Code available |
| 50 | 2024-Son-HAE-RAE Bench Evaluation of Korean Knowledge in Language Models | **10.0** | `Match` | https://github.com/HAE-RAE/HAE-RAE-BENCH | is_benchmark, is_eval, Has DATA_URL, Code available |
| 51 | 2024-Son-LLM-as-a-Judge & Reward Model What They Can and Cannot Do | **10.0** | `Match` | https://github.com/guijinSON/kudge | is_eval, is_dataset, Has DATA_URL, Code available |
| 52 | 2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge | **10.0** | `Match` | https://github.com/guijinSON/MM-Eval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 53 | 2024-Tam-An Improved Traditional Chinese Evaluation Suite for Foundation Model | **10.0** | `Match` | https://huggingface.co/datasets/ikala/tmmluplus | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 54 | 2024-Team-WildGuard | **10.0** | `Match` | https://huggingface.co/datasets/allenai/wildguardm | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 55 | 2024-Wu-AC-EVAL Evaluating Ancient Chinese Language Understanding | **10.0** | `Match` | https://github.com/yuting-wei/AC-EVAL | is_benchmark, is_eval, Has DATA_URL, Code available |
| 56 | 2024-Yanaka-JBBQ | **10.0** | `Match` | https://github.com/ynklab/JBBQ_data | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 57 | 2024-Yin-SafeAgentBench | **10.0** | `Match` | https://github.com/shengyin1224/SafeAgentBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 58 | 2024-Yin-SafeWorld Geo-Diverse Safety Alignment | **10.0** | `Match` | https://github.com/PlusLabNLP/SafeWorld | is_benchmark, is_eval, Has DATA_URL, Code available |
| 59 | 2024-Yuan-R-Judge | **10.0** | `Match` | https://github.com/Lordog/R-Judge | is_benchmark, is_eval, Has DATA_URL, Code available |
| 60 | 2024-Yuan-Social Measuring Social Norms of LLMs | **10.0** | `Match` | https://huggingface.co/datasets/socialnormdataset/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 61 | 2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via | **10.0** | `Match` | https://github.com/SophieZheng998/ALI-Agent | is_benchmark, is_eval, Has DATA_URL, Code available |
| 62 | 2025-Alwajih-Palm | **10.0** | `Match` | https://github.com/UBC-NLP/palm | is_eval, is_dataset, Has DATA_URL, Code available |
| 63 | 2025-Chua-RabakBench | **10.0** | `Match` | https://huggingface.co/datasets/govtech/RabakBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 64 | 2025-Helwe-Navigating the Political Compass Multilingual 50 Countries | **10.0** | `Match` | https://github.com/sadiakamal/Detailed-factor-anal | is_eval, is_dataset, Has DATA_URL, Code available |
| 65 | 2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models | **10.0** | `Match` | https://github.com/THUYRan/LLM-Fairness | is_eval, is_dataset, Has DATA_URL, Code available |
| 66 | 2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors | **10.0** | `Match` | https://github.com/Aries-iai/DeceptionBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 67 | 2025-Huang-On the Trustworthiness of Generative Foundation | **10.0** | `Match` | https://github.com/TrustGen/TrustEval-toolkit | is_benchmark, is_eval, Has DATA_URL, Code available |
| 68 | 2025-Leteno-Histoires Morales | **10.0** | `Match` | https://hf.co/datasets/LabHC/histoires_morales, ht | is_eval, is_dataset, Has DATA_URL, Code available |
| 69 | 2025-Lin-MORALISE | **10.0** | `Match` | https://huggingface.co/datasets/Ze1025/MORALISE | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 70 | 2025-Ma-EthicsSuite Detecting Behavioral Inconsistency in LLM Ethics | **10.0** | `Match` | https://github.com/LLM-Ethics/EthicsSuite | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 71 | 2025-Rahman-CCD-Bench Probing Cultural Conflict in LLM Decision-Making | **10.0** | `Match` | https://github.com/smartlab-nyu/CCD-Bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 72 | 2025-Raza-HumaniBench | **10.0** | `Match` | https://huggingface.co/vector-institute/HumaniBenc | is_benchmark, is_eval, Has DATA_URL, Code available |
| 73 | 2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas | **10.0** | `Match` | https://github.com/dlab-projects/normative_evaluat | is_eval, is_dataset, Has DATA_URL, Code available |
| 74 | 2025-Saffari-Can I introduce my boyfriend to my grandmother | **10.0** | `Match` | https://github.com/hamidds/ISN | is_eval, is_dataset, Has DATA_URL, Code available |
| 75 | 2025-Shetty-VITAL | **10.0** | `Match` | https://github.com/anudeex/VITAL.git | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 76 | 2025-Shin-RoleConflictBench A Benchmark of Role Conflict Scenarios for | **10.0** | `Match` | https://github.com/ddindidu/RoleConflictBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 77 | 2025-Simhi-ManagerBench Evaluating Safety-Pragmatism Trade-off in Managerial | **10.0** | `Match` | https://github.com/technion-cs-nlp/ManagerBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 78 | 2025-Wei-MedEthicsQA | **10.0** | `Match` | https://github.com/JianhuiWei7/MedEthicsQA | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 79 | 2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal | **10.0** | `Match` | https://sorry-bench.github.io | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 80 | 2025-Yuan-S-Eval | **10.0** | `Match` | https://github.com/IS2Lab/S-Eval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 81 | 2025-Zhang-LLMEval-Med Medical Safety & Ethics Component | **10.0** | `Match` | https://github.com/llmeval/LLMEval-Med | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 82 | 2025-Zhang-REVAL | **10.0** | `Match` | https://github.com/InternLM/InternLM-techreport | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 83 | 2026-Jin-MedES Chinese Medical Ethics Scenarios | **10.0** | `Match` | https://github.com/X-LANCE/MedEthicAlign | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 84 | 2026-Shen-PsychEthicsBench | **10.0** | `Match` | https://github.com/ElsieSHEN/PsychEthicsBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 85 | 2020-Gehman-RealToxicityPrompts | **9.55** | `Match` | https://toxicdegeneration.allenai.org/ | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 86 | 2020-Mathew-HateXplain | **9.55** | `Match` | https://github.com/punyajoy/HateXplain | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 87 | 2021-Barikeri-REDDITBIAS | **9.55** | `Match` | https://github.com/umanlp/RedditBias | is_benchmark, is_eval, Has DATA_URL, Code available |
| 88 | 2021-Dhamala-BOLD | **9.55** | `Match` | https://github.com/jwaladhamala/BOLD-Bias-in-open- | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 89 | 2021-Jiang-Pretrained Models and Evaluation Data for | **9.55** | `Match` | https://github.com/SunYanCN/seqeval | is_eval, is_dataset, Has DATA_URL, Code available |
| 90 | 2021-Park-KLUE Korean Language Understanding Evaluation | **9.55** | `Match` | https://github.com/KLUE-benchmark/KLUE | is_benchmark, is_eval, Has DATA_URL, Code available |
| 91 | 2021-Röttger-HateCheck | **9.55** | `Match` | https://github.com/paul-rottger/hatecheck-data | is_eval, is_dataset, Has DATA_URL, Code available |
| 92 | 2021-Sun-LaoPLM Pre-trained Language Models for Lao | **9.55** | `Match` | https://github.com/GKLMIP/Yunshan-Cup-2020 | is_eval, is_dataset, Has DATA_URL, Code available |
| 93 | 2022-Bhattacharjee-BanglaBERT Language Model Pretraining and Benchmarks for Low-Resource | **9.55** | `Match` | https://github.com/csebuetnlp/banglabert | is_benchmark, is_eval, Has DATA_URL, Code available |
| 94 | 2022-Dementieva-RUSSE 2022 Findings of the First Russian Detoxification Shared Task | **9.55** | `Match` | https://github.com/sberbank-ai/ru-gpts | is_eval, is_dataset, Has DATA_URL, Code available |
| 95 | 2022-Hartvigsen-ToxiGen | **9.55** | `Match` | https://github.com/microsoft/ToxiGen | is_eval, is_dataset, Has DATA_URL, Code available |
| 96 | 2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction | **9.55** | `Match` | https://github.com/ku-vai/Zero-shot-Visual-Commons | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 97 | 2022-Röttger-Multilingual HateCheck | **9.55** | `Match` | https://github.com/rewire-online/multilingual-hate | is_eval, is_dataset, Has DATA_URL, Code available |
| 98 | 2022-Shaily Bhatt-Re-contextualizing Fairness in NLP The Case | **9.55** | `Match` | https://github.com/google-research-datasets/nlp-fa | is_eval, is_dataset, Has DATA_URL, Code available |
| 99 | 2023-Duan-Denevil | **9.55** | `Match` | https://valuecompass.github.io | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 100 | 2023-Fleisig-FairPrism | **9.55** | `Match` | https://github.com/microsoft/fairprism | is_eval, is_dataset, Has DATA_URL, Code available |
| 101 | 2023-Lin-ToxicChat | **9.55** | `Match` | https://huggingface.co/datasets/lmsys/toxic-chat | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 102 | 2023-Nie-MoCa | **9.55** | `Match` | https://github.com/cicl-stanford/moca | is_eval, is_dataset, Has DATA_URL, Code available |
| 103 | 2024-Arshad-Understanding hate speech | **9.55** | `Match` | https://github.com/twintproject/twint | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 104 | 2024-Brun-FrenchToxicityPrompts a Large Benchmark for Evaluating and Mitigating | **9.55** | `Match` | https://huggingface.co/datasets/FrenchToxicityProm | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 105 | 2024-Cao-C3Bench A Comprehensive Classical Chinese Understanding Benchmark for | **9.55** | `Match` | https://github.com/NiuTrans/Classical-Modern | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 106 | 2024-Chao-JBB-Behaviours | **9.55** | `Match` | https://github.com/JailbreakBench/jailbreakbench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 107 | 2024-Chiu-DailyDilemmas | **9.55** | `Match` | https://hf.co/datasets/kellycyy/daily_dilemmas, ht | is_eval, is_dataset, Has DATA_URL, Code available |
| 108 | 2024-Enevoldsen-The Scandinavian Embedding Benchmarks Comprehensive Assessment of | **9.55** | `Match` | https://github.com/KennethEnevoldsen/scandinavian- | is_benchmark, is_eval, Has DATA_URL, Code available |
| 109 | 2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic | **9.55** | `Match` | https://github.com/cmu-lti/m-alert | is_benchmark, is_eval, Has DATA_URL, Code available |
| 110 | 2024-Jain-PolygloToxicityPrompts | **9.55** | `Match` | https://huggingface.co/datasets/ToxicityPrompts/Po | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 111 | 2024-Kaneko-Eagle | **9.55** | `Match` | https://huggingface.co/datasets/MasahiroKaneko/eag | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 112 | 2024-Lee-KorNAT | **9.55** | `Match` | https://huggingface.co/datasets/datumo/KorNAT | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 113 | 2024-Li-OpenEval - Benchmarking Chinese LLMs across Capability Alignment and | **9.55** | `Match` | https://github.com/01-ai/Yi | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 114 | 2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark | **9.55** | `Match` | https://github.com/Smartmedia-AI/NorGLM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 115 | 2024-Mozikov-EAI - Emotional Decision-Making of LLMs in Strategic Games and | **9.55** | `Match` | https://github.com/AIRI-Institute/EAI-Framework | is_benchmark, is_eval, Has DATA_URL, Code available |
| 116 | 2024-Onose-LLMs for Extremely Low-Resource Finno-Ugric Languages | **9.55** | `Match` | https://github.com/TartuNLP/smugri-llm | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 117 | 2024-Sahoo-IndiBias - Benchmark Dataset for Social Biases in Indian Context | **9.55** | `Match` | https://github.com/sahoonihar/IndiBias | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 118 | 2024-Singh-IndicGenBench A Multilingual Benchmark to Evaluate | **9.55** | `Match` | https://github.com/google-research-datasets/indic- | is_benchmark, is_eval, Has DATA_URL, Code available |
| 119 | 2024-Team-FABLE Fairness and Bias in LLM Evaluation | **9.55** | `Match` | https://github.com/uclanlp/Fact-or-Fair | is_benchmark, is_eval, Has DATA_URL, Code available |
| 120 | 2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios | **9.55** | `Match` | https://github.com/microsoft/RTP-LX | is_eval, is_dataset, Has DATA_URL, Code available |
| 121 | 2024-Yan-M$^3$oralBench | **9.55** | `Match` | https://github.com/BeiiiY/M3oralBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 122 | 2024-Yu-CMoralEval | **9.55** | `Match` | https://github.com/tjunlp-lab/CMoralEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 123 | 2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents | **9.55** | `Match` | https://github.com/thu-coai/Agent-SafetyBench/ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 124 | 2024-Zhang-CHiSafetyBench | **9.55** | `Match` | https://github.com/UnicomAI/UnicomBenchmark/tree/m | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 125 | 2024-Zhang-ChineseSafe - A Chinese Benchmark for Evaluating Safety in LLMs | **9.55** | `Match` | https://huggingface.co/datasets/SUSTech/ChineseSaf | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 126 | 2024-Zhang-MM-Eval A Hierarchical Benchmark for Modern Mongolian Evaluation in | **9.55** | `Match` | https://github.com/joenahm/MM-Eval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 127 | 2024-Zhang-SafetyBench | **9.55** | `Match` | https://github.com/thu-coai/SafetyBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 128 | 2025-Ashkinaze-Deep Value Benchmark | **9.55** | `Match` | https://github.com/josh-ashkinaze/deep-value-bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 129 | 2025-Bae-CharMoral | **9.55** | `Match` | https://github.com/BaeSuyoung/CharMoral | is_eval, is_dataset, Has DATA_URL, Code available |
| 130 | 2025-Banerjee-SafeInfer | **9.55** | `Match` | https://github.com/NeuralSentinel/SafeInfer | is_benchmark, is_eval, Has DATA_URL, Code available |
| 131 | 2025-Bulla-Large Language Models meet moral values | **9.55** | `Match` | https://osf.io/kw6rc/?view_only=73c3d8e2f7c9483ea0 | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 132 | 2025-Fan-FAIRMT-BENCH | **9.55** | `Match` | https://github.com/FanZT6/FairMT-bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 133 | 2025-Group-AILuminate | **9.55** | `Match` | https://github.com/mlcommons/ailuminate | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 134 | 2025-Jiao-LLM Ethics Benchmark | **9.55** | `Match` | https://github.com/The-Responsible-AI-Initiative/L | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 135 | 2025-Jourdan-FairTranslate | **9.55** | `Match` | https://github.com/fanny-jourdan/FairTranslate | is_eval, is_dataset, Has DATA_URL, Code available |
| 136 | 2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts | **9.55** | `Match` | https://github.com/AI4Bharat/indic-bias | is_benchmark, is_eval, Has DATA_URL, Code available |
| 137 | 2025-Pandey-SocialHarmBench | **9.55** | `Match` | https://huggingface.co/datasets/psyonp/SocialHarmB | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 138 | 2025-Sun-CASE-Bench | **9.55** | `Match` | https://github.com/BriansIDP/CASEBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 139 | 2025-Trager-MFTCXplain | **9.55** | `Match` | https://github.com/franciellevargas/MFTCXplain | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 140 | 2025-Wen-Evaluating Implicit Bias in Large Language Models | **9.55** | `Match` | https://github.com/yuchenwen1/BUMBLE | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 141 | 2025-Xia-SafeToolBench | **9.55** | `Match` | https://github.com/BITHLP/SafeToolBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 142 | 2025-Xiang-Comparing Moral Values in Western | **9.55** | `Match` | https://github.com/ChunhuaLiu596/Word_Association_ | is_eval, is_dataset, Has DATA_URL, Code available |
| 143 | 2025-Zhou-SocialEval Evaluating Social Intelligence of Large Language Models | **9.55** | `Match` | https://github.com/thu-coai/SocialEval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 144 | 2026-Dang-RedBench | **9.55** | `Match` | https://github.com/knoveleng/redeval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 145 | 2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian | **9.5** | `Match` | https://github.com/MarioVilas/googlesearch | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 146 | 2021-Lourie-Scruples | **9.5** | `Match` | https://github.com/allenai/scruples | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 147 | 2023-Bhardwaj-Red-Teaming Large Language Models using Chain of Utterances for | **9.5** | `Match` | https://github.com/declare-lab/red-instruct | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 148 | 2023-Huang-AceGPT Localizing Large Language Models in Arabic | **9.5** | `Match` | https://github.com/FreedomIntelligence/AceGPT | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 149 | 2023-Koto-Large Language Models Only Pass Primary School Exams in Indonesia A | **9.5** | `Match` | https://github.com/fajri91/IndoMMLU | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 150 | 2023-Lee-KoSBi A Dataset for Mitigating Social Bias Risks Towards Safer Large | **9.5** | `Match` | https://github.com/Beomi/KcELECTRA | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 151 | 2023-Lee-SQuARe A Large-Scale Dataset of Sensitive Questions and Acceptable | **9.5** | `Match` | https://github.com/Beomi/KcELECTRA | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 152 | 2023-Xu-SC-Safety | **9.5** | `Match` | https://www.CLUEbenchmarks.com | is_benchmark, Has DATA_URL, Availability = Public, LLM_assessed |
| 153 | 2024-Chaves-Napolab The Natural Portuguese Language Benchmark | **9.5** | `Match` | https://github.com/huggingface/accelerate | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 154 | 2024-Ghosh-AEGIS | **9.5** | `Match` | https://github.com/meta-llama/llama-recipes | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 155 | 2024-Kirk-The PRISM Alignment Project | **9.5** | `Match` | https://github.com/HannahKirk/prism-alignment, htt | is_dataset, Has DATA_URL, HuggingFace dataset URL, Code available |
| 156 | 2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented | **9.5** | `FuzzyMatch` | https://github.com/priyankamandikal/vedantany-10m  | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 157 | 2024-Nguyen-ViHateT5 Enhancing Hate Speech Detection in Vietnamese With A Unified | **9.5** | `Match` | https://github.com/tarudesu/ViHateT5 | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 158 | 2024-Porkaew-Representing the Under-Represented Cultural and Core | **9.5** | `FuzzyMatch` | https://github.com/UpstageAI/ThaiCLI_H6 | is_benchmark, is_eval, Has DATA_URL, Code available |
| 159 | 2024-Putri-Can LLM Generate Culturally Relevant Commonsense QA Data Case Study | **9.5** | `Match` | https://github.com/commonsense/conceptnet5 | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 160 | 2024-Röttger-XSTest | **9.5** | `Match` | https://github.com/paul-rottger/exaggerated-safety | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 161 | 2024-Thu-MixCuBe When Tom Eats Kimchi - Evaluating Cultural Awareness of | **9.5** | `Match` | https://huggingface.co/datasets/kyawyethu/MixCuBe | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 162 | 2024-Wibowo-COPAL-ID Indonesian Language Reasoning with Local Culture and Nuances | **9.5** | `Match` | https://github.com/haryoa/COPAL-ID | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 163 | 2025-Ji-PKU-SafeRLHF | **9.5** | `FuzzyMatch` | https://huggingface.co/datasets/PKU-Alignment/PKU- | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 164 | 2018-Zhao-Finding Answers from the Word of God | **9.25** | `Match` | https://github.com/helen-jiahe-zhao/BibleQA | is_eval, is_dataset, Has DATA_URL, Code available |
| 165 | 2022-Bai-Constitutional AI | **9.25** | `Match` | https://github.com/anthropics/ConstitutionalHarmle | is_eval, is_dataset, Has DATA_URL, Code available |
| 166 | 2022-Lin-TruthfulQA | **9.25** | `Match` | https://github.com/sylinrl/TruthfulQA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 167 | 2022-Rauh-Characteristics of Harmful Text | **9.25** | `Match` | https://github.com/LDNOOBW/List-of-Dirty-Naughty-O | is_benchmark, is_eval, Has DATA_URL, Code available |
| 168 | 2023-Guha-LegalBench | **9.25** | `Match` | https://github.com/HazyResearch/legalbench/ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 169 | 2023-Hardalov-bgGLUE A Bulgarian General Language Understanding Evaluation Benchmark | **9.25** | `Match` | https://github.com/bgGLUE/bgglue | is_benchmark, is_eval, Has DATA_URL, Code available |
| 170 | 2023-Hsu-Advancing the Evaluation of Traditional Chinese Language Models | **9.25** | `Match` | https://github.com/mtkresearch/MR-Models | is_benchmark, is_eval, Has DATA_URL, Code available |
| 171 | 2023-Huang-Vigogne French instruction-following and chat models | **9.25** | `Match` | https://github.com/bofenghuang/vigogne | is_eval, is_dataset, Has DATA_URL, Code available |
| 172 | 2023-Liu-AgentBench | **9.25** | `Match` | https://github.com/THUDM/AgentBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 173 | 2023-Ojo-AfroBench - How Good are LLMs on African Languages | **9.25** | `Match` | https://mcgill-nlp.github.io/AfroBench/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 174 | 2023-Rizqullah-QASiNa | **9.25** | `FuzzyMatch` | https://github.com/rizquuula/QASiNa | is_eval, is_dataset, Has DATA_URL, Code available |
| 175 | 2024-Chouhan-HindiLLM Large Language Model for Hindi | **9.25** | `Match` | https://github.com/NirantK/hindi2vec | is_benchmark, is_eval, Has DATA_URL, Code available |
| 176 | 2024-Gala-Airavata Introducing Hindi Instruction-tuned LLM | **9.25** | `Match` | https://github.com/AI4Bharat/IndicInstruct | is_benchmark, is_eval, Has DATA_URL, Code available |
| 177 | 2024-Gallegos-Bias and Fairness in Large Language Models A Survey | **9.25** | `Match` | https://github.com/i-gallegos/Fair-LLM-Benchmark | is_eval, is_dataset, Has DATA_URL, Code available |
| 178 | 2024-Holm-Danoliteracy of Generative Large Language Models | **9.25** | `Match` | https://github.com/chakki-works/seqeval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 179 | 2024-Kaiyom-HELM Safety | **9.25** | `Match` | https://github.com/stanford-crfm/helm | is_eval, Has DATA_URL, Code available, Availability = Public |
| 180 | 2024-Karpov-Inducing Human-like Biases in Moral Reasoning | **9.25** | `Match` | https://github.com/ajmeek/Inducing-human-like-bias | is_benchmark, is_eval, Has DATA_URL, Code available |
| 181 | 2024-Kim-Developing a Pragmatic Benchmark for Assessing Korean Legal Language | **9.25** | `Match` | https://github.com/haven-jeon/LegalQA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 182 | 2024-Kiulian-From Bytes to Borsch Fine-Tuning Gemma and Mistral for the Ukrainian | **9.25** | `Match` | https://github.com/PolyAgent/from-bytes-to-borsch | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 183 | 2024-Pfister-LLaMmlein Transparent Compact and Competitive German-Only Language | **9.25** | `Match` | https://professor-x.de/lm/LLaMmlein | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 184 | 2024-Rahman-DefAn | **9.25** | `Match` | https://github.com/ashikiut/DefAn | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 185 | 2024-Röttger-Political Compass or Spinning Arrow | **9.25** | `Match` | https://github.com/paul-rottger/llm-values-pct | is_eval, Has DATA_URL, Code available, Availability = Public |
| 186 | 2024-Sabour-EmoBench Evaluating the Emotional Intelligence of Large Language | **9.25** | `Match` | https://github.com/Sahandfer/EmoBench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 187 | 2024-Son-KMMLU Measuring Massive Multitask Language Understanding in Korean | **9.25** | `Match` | https://github.com/EleutherAI/lm-evaluation-harnes | is_eval, Has DATA_URL, Code available, Availability = Public |
| 188 | 2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation | **9.25** | `Match` | https://github.com/stair-lab/villm | is_eval, Has DATA_URL, Code available, Availability = Public |
| 189 | 2024-Uluoglakci-HypoTermQA | **9.25** | `Match` | https://github.com/cemuluoglakci/HypoTermQA | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 190 | 2024-Xu-Course-Correction | **9.25** | `Match` | https://github.com/pillowsofwind/Course-Correction | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 191 | 2025-Aleid-Hajj-FQA | **9.25** | `FuzzyMatch` | https://github.com/Omarito2412/ASKFM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 192 | 2025-Cao-SafeDialBench | **9.25** | `Match` | https://github.com/drivetosouth/SafeDialBench-Data | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 193 | 2025-Cengiz-Evaluating the Quality of Benchmark Datasets for Low-Resource | **9.25** | `Match` | https://github.com/metunlp/llmevaluation | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 194 | 2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning | **9.25** | `Match` | https://huggingface.co/datasets/AUEB-NLP/greek-bar | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 195 | 2025-Davies-Fairness identification of large language models in recommendation | **9.25** | `Match` | https://github.com/sy-cg/LLM-fair-aware | is_eval, is_dataset, Has DATA_URL, Code available |
| 196 | 2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark | **9.25** | `Match` | https://github.com/AndrewZhe/lawyer-llama | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 197 | 2025-Dwivedi-EtiCor++ Towards Understanding Etiquettical Bias in LLMs | **9.25** | `Match` | https://github.com/Exploration-Lab/Eticor-Plus-Plu | is_eval, is_dataset, Has DATA_URL, Code available |
| 198 | 2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in | **9.25** | `Match` | https://github.com/PoETaV2/PoETaV2 | is_benchmark, is_eval, Has DATA_URL, Code available |
| 199 | 2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment | **9.25** | `Match` | https://github.com/val-bench/VAL-Bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 200 | 2025-Han-MuBench Assessment of Multilingual Capabilities of | **9.25** | `Match` | https://github.com/vllm-project/vllm | is_benchmark, is_eval, Has DATA_URL, Code available |
| 201 | 2025-Han-Value Portrait | **9.25** | `Match` | https://github.com/holi-lab/ValuePortrait | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 202 | 2025-Hosseinbeigi-Advancing Persian LLM Evaluation | **9.25** | `Match` | https://github.com/SajjjadAyobi/PersianQA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 203 | 2025-Huang-BenchMAX A Comprehensive Multilingual Evaluation ... | **9.25** | `Match` | https://github.com/CONE-MT/BenchMAX.git | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 204 | 2025-Huang-Model Editing as a Double-Edged Sword | **9.25** | `Match` | https://github.com/baixianghuang/behavior-edit | is_benchmark, is_eval, Has DATA_URL, Code available |
| 205 | 2025-Huang-SI-Bench Benchmarking Social Intelligence of Large Language Models in | **9.25** | `Match` | https://github.com/SI-Bench/SI-Bench.git | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 206 | 2025-Jin-MedEthicEval | **9.25** | `Match` | https://github.com/KaguraRuri/MedEthicEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 207 | 2025-Jing-MASLegalBench | **9.25** | `Match` | https://github.com/HKUST-KnowComp/MASLegalBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 208 | 2025-Jotautaite-From Stability to Inconsistency | **9.25** | `Match` | https://github.com/monikajot/llm-ethics-2 | is_eval, is_dataset, Has DATA_URL, Code available |
| 209 | 2025-Ki-Multiple LLM Agents Debate for Equitable Cultural | **9.25** | `Match` | https://github.com/dayeonki/cultural_debate | is_benchmark, is_eval, Has DATA_URL, Code available |
| 210 | 2025-Kim-A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs | **9.25** | `Match` | https://github.com/seank021/LLM-Bias-Evaluation | is_eval, is_dataset, Has DATA_URL, Code available |
| 211 | 2025-Kim-Cultural and Core Capability Benchmarks for | **9.25** | `Match` | https://github.com/UpstageAI/ThaiCLI_H6 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 212 | 2025-Kim-Nunchi-Bench Benchmarking Language Models on Cultural Reasoning with | **9.25** | `Match` | https://github.com/koreankiwi99/Nunchi-Bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 213 | 2025-Koberidze-GeoLogicQA A Benchmark for Evaluating Logical Reasoning in Georgian | **9.25** | `Match` | https://github.com/irakli97/GeoLogicQA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 214 | 2025-Kumar-Are Rules Meant to be Broken | **9.25** | `Match` | https://huggingface.co/datasets/shivaniku/UniMoral | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 215 | 2025-Kumar-UniMoral ACL 2025 Best Resource Paper | **9.25** | `Match` | https://huggingface.co/datasets/ciol-research/Beng | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 216 | 2025-Lai-Scaling the Multilingual Capability of LLMs with Cross- ... | **9.25** | `Match` | https://github.com/boschresearch/ACL24-MLLM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 217 | 2025-Lin-GAMEBoT Transparent Assessment of LLM Reasoning in Games | **9.25** | `Match` | https://visual-ai.github.io/gamebot | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 218 | 2025-Maheshwari-IndicParam Benchmark to Evaluate LLMs on | **9.25** | `Match` | https://github.com/VikParuchuri/surya | is_benchmark, is_eval, Has DATA_URL, Code available |
| 219 | 2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs | **9.25** | `Match` | https://huggingface.co/datasets/cardiffnlp/Morable | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 220 | 2025-Mirbagheri-EPT Benchmark Evaluation of Persian Trustworthiness in Large Language | **9.25** | `Match` | https://github.com/Rezamirbagheri110/EPT-Benchmark | is_benchmark, is_eval, Has DATA_URL, Code available |
| 221 | 2025-Mohamed-Lost in the Mix Evaluating LLM Understanding of Code-Switched Text | **9.25** | `Match` | https://github.com/amr-mohamedd/Lost-in-the-Mix.gi | is_benchmark, is_eval, Has DATA_URL, Code available |
| 222 | 2025-Nair-Do Language Models Think Consistently | **9.25** | `Match` | https://github.com/launchnlp/ValuePreferenceConsis | is_eval, Has DATA_URL, Code available, Availability = Public |
| 223 | 2025-Nguyen-VM14K First Vietnamese Medical Benchmark | **9.25** | `Match` | https://github.com/ShayHill/docx2python | is_benchmark, is_eval, Has DATA_URL, Code available |
| 224 | 2025-Nie-Multilingual Large Language Models Are Not Yet Code- ... | **9.25** | `Match` | https://github.com/oscar-project/ungoliant | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 225 | 2025-PIB-PLLuM A Family of Polish Large Language Models | **9.25** | `Match` | https://github.com/MeetKai/functionary | is_benchmark, is_eval, Has DATA_URL, Code available |
| 226 | 2025-Peng-Plutus Benchmarking Large Language Models in Low-Resource Greek | **9.25** | `Match` | https://huggingface.co/collections/TheFinAI/plutus | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 227 | 2025-Poria-Bhaasha Bhasa Zaban A Survey for | **9.25** | `Match` | https://github.com/trust-nlp/LM4SouthAsia-Survey | is_benchmark, is_eval, Has DATA_URL, Code available |
| 228 | 2025-Pretrained-MiLiC-Eval Benchmarking Multilingual LLMs for China’s Minority | **9.25** | `Match` | https://github.com/microsoft/DeepSpeed | is_benchmark, is_eval, Has DATA_URL, Code available |
| 229 | 2025-Qi-A Survey of Automatic Hallucination Evaluation on | **9.25** | `Match` | https://github.com/siyaqi/Awesome-Hallu-Eval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 230 | 2025-Qi-AGENTIF | **9.25** | `Match` | https://github.com/THU-KEG/AgentIF, https://huggin | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 231 | 2025-Qiu-Evaluating Cultural and Social Awareness of LLM Web Agents | **9.25** | `Match` | https://github.com/SalesforceAIResearch/CASA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 232 | 2025-Roussis-Krikri Advancing Open Large Language Models for Greek | **9.25** | `Match` | https://huggingface.co/ilsp/Llama-Krikri-8B-Base | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 233 | 2025-Ruiz-Fernández-EsBBQ and CaBBQ | **9.25** | `Match` | https://huggingface.co/datasets/BSC-LT/EsBBQ, http | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 234 | 2025-Satheesh-GG-BBQ | **9.25** | `Match` | https://github.com/shalakasatheesh/GG-BBQ/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 235 | 2025-Seveso-ITALIC | **9.25** | `Match` | https://doi.org/10.5281/zenodo.14725822 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 236 | 2025-Shahriar-Priv-IQ | **9.25** | `Match` | https://github.com/sakibsh/Priv-IQ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 237 | 2025-Shamsfard-FarsEval-PKBETS A new diverse benchmark for evaluating Persian large | **9.25** | `Match` | https://github.com/ParsBench/ParsBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 238 | 2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion | **9.25** | `Match` | https://github.com/HariShankar08/LLMOpinions/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 239 | 2025-Susanto-SEA-HELM Southeast Asian Holistic Evaluation of Language Models | **9.25** | `Match` | https://github.com/aisingapore/SEA-HELM | is_benchmark, is_eval, Has DATA_URL, Code available |
| 240 | 2025-Tam-VisTW Benchmarking Vision-Language Models for Traditional Chinese in | **9.25** | `Match` | https://github.com/TMMMU-Benchmark/evaluation | is_benchmark, is_eval, Has DATA_URL, Code available |
| 241 | 2025-Verma-MILU A Multi-task Indic Language Understanding | **9.25** | `Match` | https://huggingface.co/datasets/ai4bharat/MILU | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 242 | 2025-Wu-AlignMMBench Evaluating Chinese Multimodal Alignment in Large | **9.25** | `Match` | https://github.com/THUDM/AlignMMBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 243 | 2025-Xu-FiSCo Fine-grained Semantic Comparison | **9.25** | `Match` | https://github.com/HuXiangkun/FiSCo | is_eval, is_dataset, Has DATA_URL, Code available |
| 244 | 2025-Xuan-MMLU-ProX A Multilingual Benchmark for Advanced | **9.25** | `Match` | https://github.com/weihao1115/MMLU-ProX | is_benchmark, is_eval, Has DATA_URL, Code available |
| 245 | 2025-Yang-CodeMixBench Evaluating Code-Mixing Capabilities of LLMs Across 18 | **9.25** | `Match` | https://github.com/fxsjy/jieba | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 246 | 2025-Yang-OpenHuEval Evaluating Large Language Model on Hungarian Specifics | **9.25** | `Match` | https://github.com/opendatalab/OpenHuEval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 247 | 2025-Ye-GPLA Generative Psycho-Lexical Approach for Constructing Value Systems | **9.25** | `Match` | https://github.com/Value4AI/ValueBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 248 | 2025-Ye-Large Language Model Psychometrics | **9.25** | `Match` | https://github.com/valuebyte-ai/Awesome-LLM-Psycho | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 249 | 2025-Yoon-Korean Canonical Legal Benchmark Toward Knowledge-Independent | **9.25** | `Match` | https://github.com/openai/tiktoken | is_benchmark, is_eval, Has DATA_URL, Code available |
| 250 | 2025-Yuan-Probabilistic Aggregation and Targeted Embedding | **9.25** | `Match` | https://github.com/yuanchencn/Collective-Moral-Rea | is_eval, is_dataset, Has DATA_URL, Code available |
| 251 | 2025-Zhang-AISafetyLab | **9.25** | `Match` | https://github.com/thu-coai/AISafetyLab | is_eval, Has DATA_URL, Code available, Availability = Public |
| 252 | 2025-Zheng-SYCON Bench | **9.25** | `Match` | https://github.com/JiseungHong/SYCON-Bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 253 | 2026-Ohashi-Conceptual Cultural Index A Metric for Cultural Specificity via | **9.25** | `Match` | https://github.com/IyatomiLab/CCI | is_benchmark, is_eval, Has DATA_URL, Code available |
| 254 | 2026-Zhang-GreekMMLU A Native-Sourced Multitask Benchmark for Evaluating | **9.25** | `Match` | https://github.com/mersinkonomi/GreekMMLU | is_benchmark, is_eval, Has DATA_URL, Code available |
| 255 | 2018-Dixon-Measuring and Mitigating Unintended Bias in Text | **9.05** | `Match` | https://github.com/conversationai/unintended-ml-bi | is_eval, is_dataset, Has DATA_URL, Code available |
| 256 | 2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification | **9.05** | `Match` | https://github.com/sahoonihar/ToxicBias_CoNLL_2022 | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 257 | 2019-Ousidhoum-Multilingual and Multi-Aspect Hate Speech Analysis | **9.05** | `Match` | https://github.com/HKUST-KnowComp/MLMA_hate_speech | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 258 | 2019-Phuong-Emotion Recognition for Vietnamese Social Media Text | **9.05** | `Match` | https://github.com/vncorenlp/VnCoreNLP | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 259 | 2020-Hoover-Moral Foundations Twitter Corpus | **9.05** | `Match` | https://osf.io/ezn37/ | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 260 | 2020-Leite-Toxic Language Detection in Social Media for Brazilian Portuguese New | **9.05** | `Match` | https://github.com/JAugusto97/ToLD-Br | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 261 | 2020-Mollas-ETHOS an Online Hate Speech Detection Dataset | **9.05** | `Match` | https://github.com/intelligence-csd-auth-gr/Ethos- | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 262 | 2020-Nangia-CrowS-Pairs | **9.05** | `Match` | https://github.com/nyu-mll/crows-pairs/ | is_eval, is_dataset, Has DATA_URL, Code available |
| 263 | 2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate | **9.05** | `Match` | https://github.com/guscode/dkhate | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 264 | 2021-Hendrycks-Aligning AI with Shared Human Values | **9.05** | `Match` | https://github.com/hendrycks/ethics | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 265 | 2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social | **9.05** | `Match` | https://github.com/google-research/bert | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 266 | 2021-Mohit Chandra-Subverting the Jewtocracy Online Antisemitism Detection | **9.05** | `Match` | https://github.com/mohit3011/Online-Antisemitism-D | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 267 | 2021-Nurce-Detecting Abusive Albanian | **9.05** | `Match` | https://doi.org/10.6084/m9.figshare.19333298.v1 | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 268 | 2021-Ravikiran-DOSA Dravidian Code-Mixed Offensive Span Identification | **9.05** | `Match` | https://github.com/manikandan-ravikiran/dosa | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 269 | 2021-Wuerzburg-German HateSpeech Corpus | **9.05** | `Match` | https://github.com/cophi-wue/German_HateSpeech_Cor | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 270 | 2022-Das-HateCheckHIn Evaluating Hindi Hate Speech Detection | **9.05** | `Match` | https://github.com/hate-alert/HateCheckHIn | is_benchmark, is_eval, Has DATA_URL, Code available |
| 271 | 2022-Demus-DeTox A Comprehensive Dataset for German Offensive Language and | **9.05** | `Match` | https://github.com/hdaSprachtechnologie/detox | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 272 | 2022-Jeong-KOLD Korean Offensive Language Dataset | **9.05** | `Match` | http://github.com/boychaboy/KOLD | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 273 | 2022-Qiu-ValueNet | **9.05** | `Match` | https://liang-qiu.github.io/ValueNet/ | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 274 | 2022-Vargas-HateBR A Large Expert Annotated Corpus of Brazilian Instagram | **9.05** | `Match` | https://github.com/franciellevargas/HateBR | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 275 | 2022-Ziems-The Moral Integrity Corpus | **9.05** | `Match` | https://github.com/GT-SALT/mic | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 276 | 2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text | **9.05** | `Match` | https://github.com/dhfbk/hate-ita | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 277 | 2023-Ayele-Amharic Hate Speech Dataset | **9.05** | `Match` | https://github.com/uhh-lt/AmharicHateSpeech | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 278 | 2023-Eskelinen-Toxicity Detection in Finnish Using Machine Translation | **9.05** | `Match` | https://github.com/TurkuNLP/toxicity-classifier | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 279 | 2023-Fischer-What does ChatGPT return about human values | **9.05** | `Match` | https://osf.io/w46nq/ | is_dataset, Has DATA_URL, Availability = Public, Code available |
| 280 | 2023-Hamad-Offensive Hebrew Corpus and Detection using BERT | **9.05** | `Match` | https://github.com/SinaLab/OffensiveHebrew | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 281 | 2023-Haq-Pashto Offensive Language Detection A Benchmark Dataset and | **9.05** | `Match` | https://zenodo.org/record/8195797 | is_benchmark, is_dataset, Has DATA_URL, Availability = Public |
| 282 | 2023-Hoang-ViHOS Hate Speech Spans Detection for Vietnamese | **9.05** | `Match` | https://github.com/phusroyal/ViHOS | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 283 | 2023-Kolos-BAN-PL a Novel Polish Dataset of Banned Harmful and Offensive Content | **9.05** | `Match` | https://github.com/ZILiAT-NASK/BAN-PL | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 284 | 2023-Maity-A Deep Learning Framework for the Detection of Malay Hate Speech | **9.05** | `Match` | https://github.com/MaityKrishanu/Hate_Malay | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 285 | 2024-Frenda-GFG - Gender-Fair Generation A CALAMITA Challenge | **9.05** | `Match` | https://github.com/dhfbk/gfg-calamita | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 286 | 2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values | **9.05** | `Match` | https://github.com/Derekkk/VIVA_EMNLP24 | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 287 | 2024-Khandelwal-Indian-BhED - A Dataset for Measuring India-Centric Biases in LLMs | **9.05** | `Match` | https://github.com/khyatikhandelwal/Indian-LLMs-Bi | is_eval, is_dataset, Has DATA_URL, Code available |
| 288 | 2024-Lopes-GlórIA A Generative and Open Large Language Model for Portuguese | **9.05** | `Match` | https://github.com/rvlopes/GlorIA | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 289 | 2024-Luu-ViTHSD Exploiting Hatred by Targets for Hate Speech Detection on | **9.05** | `Match` | https://github.com/bakansm/ViTHSD | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 290 | 2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge | **9.05** | `Match` | https://huggingface.co/datasets/readerbench/ro-off | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 291 | 2024-Mozafari-Offensive Language Detection in Low Resource Languages A Use Case of | **9.05** | `Match` | https://github.com/ICTRC/Parsivar | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 292 | 2024-Obi-Value Imprint | **9.05** | `Match` | https://github.com/hv-rsrch/valueimprint | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 293 | 2024-Ohashi-Extended Japanese Commonsense Morality Dataset | **9.05** | `Match` | https://github.com/IyatomiLab/extended-jcm | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 294 | 2024-Ptaszynski-Expert-Annotated Dataset to Study Cyberbullying in Polish Language | **9.05** | `Match` | https://github.com/bear/python-twitter | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 295 | 2024-Ranasinghe-SOLD Sinhala Offensive Language Dataset | **9.05** | `Match` | https://github.com/Sinhala-NLP/SOLD | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 296 | 2024-Sahoo-IndicCONAN A Multilingual Dataset for Combating Hate Speech in Indian | **9.05** | `Match` | https://github.com/sahoonihar/IndicCONAN | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 297 | 2024-Susanto-IndoToxic2024 A Demographically-Enriched Dataset of Hate Speech and | **9.05** | `Match` | https://github.com/izzako/IndoToxic2024 | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 298 | 2024-Velankar-SamPar A Marathi Hate Speech Dataset | **9.05** | `Match` | https://github.com/l3cube-pune/MarathiNLP | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 299 | 2024-Wu-WorldValuesBench | **9.05** | `Match` | https://github.com/Demon702/WorldValuesBench | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 300 | 2024-Z. Delbari-Spanning the Spectrum of Hatred Detection A Persian Multi-Label Hate | **9.05** | `Match` | https://github.com/Zahra-D/Phate | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 301 | 2024-results-EthioLLM Multilingual Large Language Models for Ethiopian Languages | **9.05** | `Match` | https://github.com/EthioNLP/EthioLLM | is_eval, is_dataset, Has DATA_URL, Code available |
| 302 | 2024-team-IndicLLMSuite A Blueprint for Creating Pre-training | **9.05** | `Match` | https://huggingface.co/datasets/ai4bharat/indic-al | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 303 | 2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in | **9.05** | `Match` | https://github.com/faridlazuarda/from-surveys-to-n | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 304 | 2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values | **9.05** | `Match` | https://github.com/ZiyuChen0410/MoVa2025 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 305 | 2025-Ghosh-AEGIS 2.0 | **9.05** | `Match` | https://github.com/meta-llama/llama-recipes | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 306 | 2025-Liu-Can LLMs Grasp Implicit Cultural Values | **9.05** | `Match` | https://github.com/uscnlp-lime/CQ-Bench | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 307 | 2025-Santhosh-IndiCASA - Dataset and Bias Evaluation Framework for LLMs in Indian | **9.05** | `Match` | https://github.com/cerai-iitm/IndiCASA | is_eval, is_dataset, Has DATA_URL, Code available |
| 308 | 2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized | **9.05** | `Match` | https://github.com/tools-only/FairPP, https://hugg | is_dataset, Has DATA_URL, HuggingFace dataset URL, Code available |
| 309 | 2024-Bonagiri-SaGE | **9.03** | `ModelBasedClassify` | https://github.com/vnnm404/SaGE | is_eval, is_dataset, Has DATA_URL, Code available |
| 310 | 2024-Sang-CDEval A Benchmark for Measuring the | **9.03** | `ModelBasedClassify` | https://huggingface.co/datasets/Rykeryuhang/CDEval | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 311 | 2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling | **9.03** | `ModelBasedClassify` | https://e-m-n-l-p.github.io/ | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 312 | 2025-Shen-ValueActionLens Mind the Value-Action Gap | **9.03** | `ModelBasedClassify` | https://github.com/huashen218/value_action_gap | is_eval, is_dataset, Has DATA_URL, Code available |
| 313 | 2025-Takeshita-JETHICS | **9.03** | `ModelBasedClassify` | https://github.com/Language-Media-Lab/jethics | is_eval, is_dataset, Has DATA_URL, Code available |
| 314 | 2018-Zhao-Gender Bias in Coreference Resolution | **9.0** | `Match` | https://github.com/rudinger/winogender-schemas | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 315 | 2023-Aroyo-DICES Dataset | **9.0** | `Match` | https://github.com/google-research-datasets/dices- | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 316 | 2023-Durmus-Towards Measuring the Representation of | **9.0** | `Match` | https://huggingface.co/datasets/Anthropic/llm_glob | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 317 | 2024-Baek-K-Viscuit Evaluating Visual and Cultural Interpretation with | **9.0** | `Match` | https://huggingface.co/datasets/ddehun/k-viscuit | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 318 | 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation | **9.0** | `Match` | https://huggingface.co/datasets/sail/Sailcompass_d | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 319 | 2024-Li-The WMDP Benchmark | **9.0** | `Match` | https://wmdp.ai | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 320 | 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs | **9.0** | `Match` | https://huggingface.co/datasets/QCRI/AraDiCE | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 321 | 2024-Olatunji-AfriMed-QA A Pan-African Multi-Specialty Medical Question-Answering | **9.0** | `Match` | https://huggingface.co/datasets/intronhealth/afrim | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 322 | 2024-Pistilli-CIVICS Building a Dataset for Examining Culturally-Informed Values in | **9.0** | `Match` | https://huggingface.co/spaces/CIVICS-dataset/CIVIC | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 323 | 2024-Romero-CVQA Culturally-diverse Multilingual Visual Question Answering | **9.0** | `Match` | https://cvqa-benchmark.org/ | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 324 | 2024-group-ITA-Bench Towards a More Comprehensive Evaluation for Italian LLMs | **9.0** | `FuzzyMatch` | https://github.com/SapienzaNLP/ita-bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 325 | 2024-initiative-CALAMITA Challenging the Abilities of LAnguage Models in ITAlian | **9.0** | `Match` | https://github.com/CALAMITA-AILC/calamita-eval | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 326 | 2024-project-DharmicData Comprehensive Open-Source Collection of Hindu | **9.0** | `FuzzyMatch` | https://github.com/bhavykhatri/DharmicData | is_eval, is_dataset, Has DATA_URL, Code available |
| 327 | 2025-Alghamdi-AraTrust - An Evaluation of Trustworthiness for LLMs in Arabic | **9.0** | `Match` | https://huggingface.co/datasets/asas-ai/AraTrust | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 328 | 2025-Almeida-BRoverbs - Measuring how much LLMs understand Portuguese proverbs | **9.0** | `Match` | https://huggingface.co/datasets/Tropic-AI/BRoverbs | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 329 | 2025-Bouchekif-QIAS 2025 - Shared Task on Islamic Inheritance Reasoning and | **9.0** | `Match` | https://gitlab.com/islamgpt1/qias_shared_task_2025 | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 330 | 2025-Chiu-CulturalBench | **9.0** | `Match` | https://hf.co/spaces/kellycyy/CulturalBench | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 331 | 2025-Chiu-MoReBench | **9.0** | `Match` | https://hf.co/datasets/morebench/morebench | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 332 | 2025-Chiu-Will AI Tell Lies to Save Sick Children | **9.0** | `Match` | https://hf.co/datasets/kellycyy/AIRiskDilemmas | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 333 | 2025-Jotautaite-SpeciesismBench Evaluating LLM Recognition of Speciesist Statements | **9.0** | `Match` | https://osf.io/69epv | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 334 | 2025-Jotautaitė-Speciesism in AI | **9.0** | `Match` | https://osf.io/69epv | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 335 | 2025-Kasu-EthicsMH | **9.0** | `Match` | https://huggingface.co/datasets/UVSKKR/Ethical-Rea | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 336 | 2025-Mitchell-SHADES | **9.0** | `Match` | https://huggingface.co/datasets/LanguageShades/Bia | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 337 | 2025-Yao-Value Compass Benchmarks | **9.0** | `Match` | https://valuecompass.github.io/#/leaderboard | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 338 | 2026-Guey-BiasLab Multilingual Dual-Framing Framework | **9.0** | `Match` | https://github.com/williamguey/LLMbiaslab | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 339 | 2020-Pitenis-Offensive Language Identification in Greek | **8.8** | `Match` | https://github.com/google-research/bert | is_eval, is_dataset, Has DATA_URL, Code available |
| 340 | 2021-Enevoldsen-DaCy A Unified Framework for Danish NLP | **8.8** | `Match` | https://github.com/centre-for-humanities-computing | is_eval, Has DATA_URL, Code available, Availability = Public |
| 341 | 2022-Chalkidis-FairLex | **8.8** | `Match` | https://github.com/coastalcph/fairlex | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 342 | 2022-Kann-AmericasNLI | **8.8** | `Match` | https://github.com/abteen/americasnli | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 343 | 2022-Korir-LREC 2022 Workshop Language Resources and Evaluation Conference 20-25 | **8.8** | `Match` | https://github.com/CorCenCC/CyTag | is_benchmark, is_eval, Has DATA_URL, Code available |
| 344 | 2022-Nguyen-SMTCE A Social Media Text Classification Evaluation Benchmark and | **8.8** | `Match` | https://github.com/binhvq/news-corpus | is_benchmark, is_eval, Has DATA_URL, Code available |
| 345 | 2023-Augustyniak-Massively Multilingual Corpus of Sentiment Datasets and Multi-faceted | **8.8** | `Match` | https://github.com/wongnai/wongnai-corpus | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 346 | 2023-Clymer-Generalization Analogies | **8.8** | `Match` | https://github.com/Joshuaclymer/GENIES | is_benchmark, is_eval, Has DATA_URL, Code available |
| 347 | 2023-Cohen-HeQ | **8.8** | `Match` | https://github.com/NNLP-IL/Hebrew-Question-Answeri | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 348 | 2023-Dwivedi-EtiCor Corpus for Analyzing LLMs for Etiquettes | **8.8** | `Match` | https://github.com/Exploration-Lab/EtiCor | is_eval, is_dataset, Has DATA_URL, Code available |
| 349 | 2023-Dwivedi-EtiCor | **8.8** | `Match` | https://github.com/Exploration-Lab/EtiCor | is_eval, is_dataset, Has DATA_URL, Code available |
| 350 | 2023-Ji-AI Alignment | **8.8** | `Match` | https://github.com/MadryLab/robustness | is_eval, is_dataset, Has DATA_URL, Code available |
| 351 | 2023-Li-BIRD | **8.8** | `Match` | https://bird-bench.github.io/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 352 | 2023-Li-HaluEval | **8.8** | `Match` | https://github.com/RUCAIBox/HaluEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 353 | 2023-Nielsen-ScandEval A Benchmark for Scandinavian Natural Language Processing | **8.8** | `Match` | https://github.com/saattrupdan/ScandEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 354 | 2023-Roger-Towards ethical multimodal systems | **8.8** | `Match` | https://github.com/kingoflolz/mesh-transformer-jax | is_eval, is_dataset, Has DATA_URL, Code available |
| 355 | 2023-Yao-From Instructions to Intrinsic Human Values -- A | **8.8** | `Match` | https://github.com/ValueCompass/Alignment-Goal-Sur | is_eval, is_dataset, Has DATA_URL, Code available |
| 356 | 2024-Arif-Generalists vs Specialists Evaluating Large Language | **8.8** | `Match` | https://github.com/meta-llama/llama3 | is_eval, is_dataset, Has DATA_URL, Code available |
| 357 | 2024-Bajaj-GenMO Gender-bias in Morality Opinions | **8.8** | `Match` | https://github.com/divij30bajaj/GenMO | is_eval, is_dataset, Has DATA_URL, Code available |
| 358 | 2024-Bhardwaj-Language Models are Homer Simpson! Safety | **8.8** | `Match` | https://github.com/declare-lab/resta | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 359 | 2024-Burema-Evaluating Dutch Social Bias in Large Language Models | **8.8** | `Match` | https://github.com/renateburema/master | is_eval, Has DATA_URL, Code available, Availability = Public |
| 360 | 2024-Franken-OffTheRails Procedural Dilemma Generation for Moral Reasoning | **8.8** | `ModelBasedClassify` | https://github.com/cicl-stanford/moral-evals | is_benchmark, is_eval, Has DATA_URL, Code available |
| 361 | 2024-Hooker-Global MMLU Understanding and Addressing Cultural | **8.8** | `Match` | https://huggingface.co/papers/2412.03304 | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 362 | 2024-Kumar-Indic-QA Benchmark A Multilingual Benchmark to | **8.8** | `Match` | https://github.com/AI4Bharat/IndicTrans2 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 363 | 2024-Liu-Are Multilingual LLMs Culturally-Diverse Reasoners An Investigation | **8.8** | `Match` | https://github.com/UKPLab/maps | is_eval, Has DATA_URL, Code available, Availability = Public |
| 364 | 2024-Liu-Evaluating Moral Beliefs across LLMs through a | **8.8** | `Match` | https://github.com/MuMu-Lily/Moral-Beliefs | is_eval, is_dataset, Has DATA_URL, Code available |
| 365 | 2024-Luo-HalluDial | **8.8** | `Match` | https://github.com/FlagOpen/HalluDial | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 366 | 2024-Mazeika-HarmBench | **8.8** | `Match` | https://github.com/centerforaisafety/HarmBench | is_eval, Has DATA_URL, Code available, Availability = Public |
| 367 | 2024-Mello-PeLLE Encoder-based Language Models for Brazilian Portuguese Based on | **8.8** | `Match` | https://github.com/huggingface/transformers | is_eval, is_dataset, Has DATA_URL, Code available |
| 368 | 2024-Park-Pragmatic Competence Evaluation of Large Language Models for the | **8.8** | `Match` | https://github.com/DojunPark/pragmatic_eval_korean | is_eval, Has DATA_URL, Code available, Availability = Public |
| 369 | 2024-Shi-CultureBank An Online Community-Driven Knowledge Base Towards | **8.8** | `Match` | https://github.com/SALT-NLP/CultureBank | is_eval, Has DATA_URL, Code available, Availability = Public |
| 370 | 2024-Sun-1 Benchmarking GPT-4 against Human Translators A | **8.8** | `Match` | https://github.com/ElliottYan/GPT_versus_ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 371 | 2024-Sun-Benchmarking Hallucination in Large Language | **8.8** | `Match` | https://github.com/Yuki-Asuuna/UMWP | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 372 | 2024-Team-Bielik 7B v0.1 A Polish Language Model - Development Insights and | **8.8** | `Match` | https://github.com/chrisociepa/allamo | is_benchmark, is_eval, Has DATA_URL, Code available |
| 373 | 2024-Tonneau-NaijaHate | **8.8** | `Match` | https://github.com/worldbank/NaijaHate | is_eval, is_dataset, Has DATA_URL, Code available |
| 374 | 2024-Tu-CharacterEval | **8.8** | `Match` | https://github.com/morecry/CharacterEval | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 375 | 2024-Veitsman-KyrgyzNLP Challenges Progress and Future | **8.8** | `Match` | https://github.com/Akyl-AI/kyrgyz-alpaca | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 376 | 2024-Watts-PARIKSHA | **8.8** | `Match` | https://aka.ms/pariksha | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 377 | 2024-Zhang-Edu-Values - Evaluating Chinese Education Values of LLMs | **8.8** | `Match` | https://github.com/zhangpeii/Edu-Values | is_benchmark, is_eval, Has DATA_URL, Code available |
| 378 | 2024-Zhang-ValueDCG | **8.8** | `Match` | https://github.com/zowiezhang/ValueDCG | is_eval, Has DATA_URL, Code available, Availability = Public |
| 379 | 2024-Zhao-CoSafe | **8.8** | `Match` | https://github.com/ErxinYu/CoSafe-Dataset | is_eval, is_dataset, Has DATA_URL, Code available |
| 380 | 2024-at-Overview of the Multilingual Text Detoxification Task at PAN 2024 | **8.8** | `Match` | https://github.com/LDNOOBW/List-of-Dirty-Naughty-O | is_eval, Has DATA_URL, Code available, Availability = Public |
| 381 | 2024-Çakici-A cross-validation study of Turkish sentiment analysis datasets and | **8.8** | `Match` | https://github.com/sevvalckc/Turkish-SAD | is_eval, is_dataset, Has DATA_URL, Code available |
| 382 | 2025-Ajwad Abrar-Religious Bias Landscape in Language and | **8.8** | `Match` | https://github.com/ajwad-abrar/Religious-Bias (pro | is_eval, Has DATA_URL, Code available, Availability = Public |
| 383 | 2025-Al-SHADES A New Multilingual Benchmark for Stereotypes Bias in Large | **8.8** | `Match` | NA | is_benchmark, is_eval, is_dataset, Availability = Public |
| 384 | 2025-Al-SHADES Towards a Multilingual Assessment of Stereotypes in Large | **8.8** | `Match` | NA | is_eval, is_dataset, Availability = Public, LLM_assessed |
| 385 | 2025-An-MoralReason | **8.8** | `Match` | https://huggingface.co/datasets/zankjhk/Moral-Reas | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 386 | 2025-Awlla-KuBERT Central Kurdish BERT Model and Its Application for Sentiment | **8.8** | `Match` | https://github.com/AsoSoft/AsoSoft-Library-py | is_benchmark, is_eval, Has DATA_URL, Code available |
| 387 | 2025-Bang-HalluLens LLM Hallucination Benchmark | **8.8** | `Match` | https://github.com/facebookresearch/HalluLens | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 388 | 2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection | **8.8** | `Match` | https://github.com/Juulba/Dutch-counterfactual-fai | is_eval, Has DATA_URL, Code available, Availability = Public |
| 389 | 2025-Beyer-LLM-Safety Evaluations Lack Robustness | **8.8** | `Match` | https://github.com/meta-llama/llama3 | is_eval, is_dataset, Has DATA_URL, Code available |
| 390 | 2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for | **8.8** | `Match` | https://github.com/krishnaik06/Trnasformer- | is_eval, is_dataset, Has DATA_URL, Code available |
| 391 | 2025-Bouchard-How to Assess Your LLM Use Case for Bias and | **8.8** | `Match` | https://github.com/cvs-health/langfair | is_eval, Has DATA_URL, Code available, Availability = Public |
| 392 | 2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT | **8.8** | `Match` | https://huggingface.co/datasets/AxelDlv00/ToxiFren | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 393 | 2025-Ebrahimi-AmericasNLI Evaluating Zero-shot Natural Language Understanding of | **8.8** | `Match` | https://github.com/abteen/americasnli | is_eval, is_dataset, Has DATA_URL, Code available |
| 394 | 2025-Farid-One Model, Many Morals | **8.8** | `Match` | https://github.com/sualehafarid/moral-project | is_benchmark, is_eval, Has DATA_URL, Code available |
| 395 | 2025-Fiaz-UrduLLaMA 1.0 Dataset Curation Preprocessing and Evaluation in | **8.8** | `Match` | https://github.com/huggingface/peft | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 396 | 2025-Galatolo-Beyond Ethical Alignment | **8.8** | `Match` | https://github.com/alessioGalatolo/AMAeval | is_benchmark, is_eval, Has DATA_URL, Code available |
| 397 | 2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value | **8.8** | `Match` | https://github.com/kshitishghate/EVALUESTEER-bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 398 | 2025-Kandji-WolBanking77 Wolof Banking Speech Intent Classification | **8.8** | `Match` | https://github.com/UniversalDependencies/UD_Wolof- | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 399 | 2025-Kravchenko-UAlign LLM Alignment Benchmark for the Ukrainian Language | **8.8** | `Match` | https://github.com/andrian-kr/alignment | is_benchmark, is_eval, Has DATA_URL, Code available |
| 400 | 2025-Krutrim-BharatBench Comprehensive Multilingual Multimodal Evaluations of | **8.8** | `Match` | https://github.com/ola-krutrim/BharatBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 401 | 2025-Lee-Knowing the Words Missing the Meaning Evaluating LLMs' Cultural | **8.8** | `Match` | https://github.com/es133lolo/Knowing-the-Words-Mis | is_benchmark, is_eval, Has DATA_URL, Code available |
| 402 | 2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities | **8.8** | `Match` | https://github.com/andyjliu/conflictscope | is_eval, is_dataset, Has DATA_URL, Code available |
| 403 | 2025-Mehta-Understanding Gen Alpha's Digital Language Evaluation of LLM Safety | **8.8** | `Match` | https://github.com/SystemTwoAI/GenAlphaSlang | is_eval, is_dataset, Has DATA_URL, Code available |
| 404 | 2025-Mora-Reyes-Advancing Equitable AI Evaluating Cultural Expressiveness in LLMs for | **8.8** | `Match` | https://github.com/areyesan/Advancing-Equitable-AI | is_eval, is_dataset, Has DATA_URL, Code available |
| 405 | 2025-Naik-AgentMisalignment | **8.8** | `Match` | https://github.com/UKGovernmentBEIS/inspect_ai | is_benchmark, is_eval, Has DATA_URL, Code available |
| 406 | 2025-Papadimitriou-BelarusianGLUE Towards a Natural Language Understanding Benchmark for | **8.8** | `Match` | https://github.com/huggingface/peft | is_benchmark, is_eval, Has DATA_URL, Code available |
| 407 | 2025-Park-KOGENT A Benchmark Dataset for Evaluating Gender Sensitivity in | **8.8** | `Match` | https://github.com/KORPUS-DB/KOGENT | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 408 | 2025-Rao-NormAd | **8.8** | `Match` | https://github.com/Akhila-Yerukola/NormAd | is_benchmark, is_eval, Has DATA_URL, Code available |
| 409 | 2025-Ren-The MASK Benchmark | **8.8** | `Match` | https://github.com/centerforaisafety/mask | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 410 | 2025-Sahoo-DIWALI Diversity and Inclusivity aWare cuLture specific Items for | **8.8** | `Match` | https://github.com/pramitsahoo/culture- | is_eval, is_dataset, Has DATA_URL, Code available |
| 411 | 2025-Shan-SEALGuard Safeguarding the Multilingual Conversations in | **8.8** | `Match` | https://github.com/awsm-research/SEALGuard | is_benchmark, is_eval, Has DATA_URL, Code available |
| 412 | 2025-Sun-Document-Level Machine Translation with Large Language Models Longyue | **8.8** | `Match` | https://github.com/rsennrich/Bleualign | is_benchmark, is_eval, Has DATA_URL, Code available |
| 413 | 2025-Team-Multimodal Evaluation of Russian-language Architectures MERA Multi | **8.8** | `Match` | https://github.com/MERA-Evaluation/MERA_ | is_eval, is_dataset, Has DATA_URL, Code available |
| 414 | 2025-Vasilev-RusCode Russian Cultural Code Benchmark for Text-to-Image Generation | **8.8** | `Match` | https://github.com/ai-forever/RusCode | is_benchmark, is_eval, Has DATA_URL, Code available |
| 415 | 2025-Vasilev-RusCode | **8.8** | `Match` | https://github.com/ai-forever/RusCode | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 416 | 2025-Wu-COIG-P | **8.8** | `Match` | https://github.com/multimodal-art-projection/COIG- | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 417 | 2025-Zhou-Moral Reasoning Across Languages | **8.8** | `Match` | https://anonymous.4open.science/r/ethics_scenarios | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 418 | 2025-Zhu-MultiAgentBench MARBLE Evaluating Collaboration and Competition of | **8.8** | `Match` | https://github.com/MultiagentBench/MARBLE | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 419 | 2025-Zuo-MUDT A Dependency Annotation Framework for Low-Resource Uyghur | **8.8** | `Match` | https://github.com/wyqmath/MUDT | is_eval, is_dataset, Has DATA_URL, Code available |
| 420 | 2018-Zhao-Gender Bias in Contextualized Word Embeddings | **8.75** | `Match` | https://github.com/uclanlp/gn_glove | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 421 | 2020-Amirkhani-FarsTail A Persian Natural Language Inference Dataset | **8.75** | `Match` | https://github.com/HIT-SCIR/ELMoForManyLangs | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 422 | 2020-Koto-IndoLEM and IndoBERT A Benchmark Dataset and Pre-trained Language | **8.75** | `Match` | https://github.com/ChineseGLUE/ChineseGLUE | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 423 | 2020-Nozza-AMI @ EVALITA2020 Automatic Misogyny Identification | **8.75** | `Match` | http://github.com/vinid/cade | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 424 | 2020-Wilie-IndoNLU Benchmark and Resources for Evaluating Indonesian Natural | **8.75** | `Match` | https://github.com/ajinkyakulkarni14/TED-Multiling | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 425 | 2020-team-IndicNLPSuite Monolingual Corpora Evaluation Benchmarks and | **8.75** | `Match` | https://github.com/AI4Bharat/indicnlp_catalog | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 426 | 2022-Jiang-Can Machines Learn Morality | **8.75** | `Match` | https://delphi.allenai.org | Has DATA_URL, Availability = Public, LLM_assessed, Ethics scenario |
| 427 | 2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for | **8.75** | `Match` | https://huggingface.co/datasets/qanastek/frenchmed | is_dataset, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 428 | 2022-Urbizu-BasqueGLUE A Natural Language Understanding Benchmark for Basque | **8.75** | `Match` | https://github.com/orai-nlp/BasqueGLUE | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 429 | 2022-Welbl-This is the way designing and compiling LEPISZCZE a comprehensive NLP | **8.75** | `Match` | https://github.com/CLARIN-PL/LEPISZCZE | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 430 | 2023-Cahyawijaya-NusaCrowd Open Source Initiative for Indonesian NLP Resources | **8.75** | `Match` | https://github.com/google-research-datasets/concep | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 431 | 2023-Chang-A Survey on Evaluation of Large Language Models | **8.75** | `Match` | https://github.com/MLGroupJLU/LLM-eval-survey | is_benchmark, is_eval, Has DATA_URL, Code available |
| 432 | 2023-Ghafouri-IslamicPCQA | **8.75** | `Match` | https://github.com/sajjjadayobi/PersianQA | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 433 | 2023-Lee-KoSBI | **8.75** | `Match` | https://github.com/naver-ai/korean-safety-benchmar | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 434 | 2023-Lee-VisAlign | **8.75** | `Match` | https://github.com/jiyounglee-0523/VisAlign | is_eval, is_dataset, Has DATA_URL, Code available |
| 435 | 2023-Li-ACLUE Can Large Language Model Comprehend | **8.75** | `Match` | https://github.com/isen-zhang/ACLUE ; https://hugg | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 436 | 2023-Ramezani-Knowledge of Cultural Moral Norms in Large Language Models | **8.75** | `Match` | https://github.com/AidaRamezani/cultural_inference | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 437 | 2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs | **8.75** | `Match` | https://huggingface.co/datasets/ninoscherrer/moral | is_eval, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 438 | 2023-Zheng-Large Language Models Are Not Robust Multiple | **8.75** | `Match` | https://github.com/chujiezheng/LLM-MCQ-Bias | is_benchmark, is_eval, Has DATA_URL, Code available |
| 439 | 2023-Ziems-NormBank | **8.75** | `Match` | https://github.com/SALT-NLP/normbank | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 440 | 2024-Adilazuarda-Towards Measuring and Modeling  | **8.75** | `Match` | https://github.com/faridlazuarda/cultural-llm-pape | is_eval, is_dataset, Has DATA_URL, Code available |
| 441 | 2024-Buyl-Large Language Models Reflect the Ideology of | **8.75** | `Match` | https://github.com/aida-ugent/llm-ideology-analysi | Has DATA_URL, Code available, Availability = Public, Code available |
| 442 | 2024-Huang-EmotionBench Apathetic or Empathetic Evaluating LLMs' Emotional | **8.75** | `Match` | https://github.com/CUHK-ARISE/EmotionBench | is_eval, is_dataset, Has DATA_URL, Code available |
| 443 | 2024-Jin-KoBBQ Korean Bias Benchmark for Question Answering | **8.75** | `Match` | https://github.com/Beomi/KoAlpaca | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 444 | 2024-Kim-CLIcK A Benchmark Dataset of Cultural and Linguistic Intelligence in | **8.75** | `Match` | https://github.com/Beomi/KoAlpaca | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 445 | 2024-Kim-How Do Moral Emotions Shape Political | **8.75** | `Match` | https://github.com/Paul-scpark/Moral-Emotion | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 446 | 2024-Ng-SGHateCheck Functional Tests for Detecting Hate Speech in | **8.75** | `Match` | https://github.com/Social-AI-Studio/SGHateCheck | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 447 | 2024-SUTD-Sailor Open Language Models for South-East | **8.75** | `Match` | https://github.com/sail-sg/sailor-llm | is_benchmark, is_eval, Has DATA_URL, Code available |
| 448 | 2024-Sadhu-Social Bias in Large Language Models | **8.75** | `Match` | Publicly available (code and resources) | is_eval, Has DATA_URL, Availability = Public, LLM_assessed |
| 449 | 2024-Sharma-TABHATE A Target-based Hate Speech Detection | **8.75** | `Match` | https://github.com/intelligence-csd-auth-gr/Ethos- | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 450 | 2024-Sharma-Towards Understanding Sycophancy in Language Models | **8.75** | `Match` | https://github.com/meg-tong/sycophancy-eval | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 451 | 2024-Xu-Exploring Multilingual Concepts of Human Value in Large Language | **8.75** | `Match` | https://github.com/antonisa/lang2vec | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 452 | 2024-Xu-MAgIC Investigation of Large Language Model Powered Multi-Agent in | **8.75** | `Match` | https://github.com/cathyxl/MAgIC | is_benchmark, is_eval, Has DATA_URL, Code available |
| 453 | 2024-Zhuge-Agent-as-a-Judge | **8.75** | `Match` | https://huggingface.co/devai-benchmark | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 454 | 2025-Alwajih-PalmX 2025 - First Shared Task on Benchmarking LLMs on Arabic and | **8.75** | `Match` | https://github.com/UBC-NLP/palmx_2025 | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 455 | 2025-Bui-VMLU Benchmarks A Comprehensive Benchmark Toolkit for Vietnamese LLMs | **8.75** | `Match` | https://github.com/ZaloAI-Jaist/VMLU | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 456 | 2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation | **8.75** | `Match` | https://github.com/fxsjy/jieba | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 457 | 2025-Devane-BhashaBench V1 A Comprehensive Benchmark for the Quadrant of Indic | **8.75** | `Match` | https://bharatgen-iitb-tih.github.io/bhashabenchv1 | is_benchmark, Has DATA_URL, LLM_assessed, QA format |
| 458 | 2025-Dey-Beyond the Rubric Cultural Misalignment in LLM Benchmarks for Sexual | **8.75** | `Match` | https://github.com/Sumon/healthbench-srh-eval/ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 459 | 2025-Faraz-IndicVisionBench Benchmarking Cultural and Multilingual Understanding | **8.75** | `Match` | https://github.com/Yuliang-Liu/MultimodalOCR | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 460 | 2025-Feng-CulFiT A Fine-grained Cultural-aware LLM Training Paradigm via | **8.75** | `Match` | https://github.com/MMadmax/CulFiT | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 461 | 2025-Goyal-Vedavani A Benchmark Corpus for ASR | **8.75** | `Match` | https://huggingface.co/datasets/sanganaka/Vedavani | is_benchmark, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 462 | 2025-Group-AILuminate LLM v1.1 Adding French Language Capabilities to | **8.75** | `Match` | https://github.com/mlcommons/ailuminate | is_benchmark, is_eval, Has DATA_URL, Code available |
| 463 | 2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness | **8.75** | `Match` | https://github.com/Guochry/CARE | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 464 | 2025-Herrador-The PacifAIst Benchmark | **8.75** | `Match` | https://github.com/PacifAIst/PacifAIst | is_benchmark, is_eval, Has DATA_URL, Code available |
| 465 | 2025-Hosain-B-REASO A Multi-Level Multi-Faceted Bengali Evaluation Suite | **8.75** | `Match` | https://github.com/kraritt/b-reaso | is_benchmark, is_eval, Has DATA_URL, Code available |
| 466 | 2025-In-U-SafeBench | **8.75** | `Match` | https://github.com/yeonjun-in/U-SafeBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 467 | 2025-Islamic-ALLaM A Series of Large Language Models for Arabic and English | **8.75** | `Match` | https://github.com/NVIDIA/Megatron-LM | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 468 | 2025-Jigsaw-A New Generation of Perspective API Efficient Multilingual ... | **8.75** | `Match` | https://github.com/conversationai/unintended-ml-bi | is_benchmark, is_eval, Has DATA_URL, Code available |
| 469 | 2025-Jigsaw-Leveraging Machine Translation for Cross-Lingual Toxicity ... | **8.75** | `Match` | https://www.kaggle.com/datasets/blackmoon/ | is_eval, is_dataset, Has DATA_URL, LLM_assessed |
| 470 | 2025-Jung-FLEX | **8.75** | `Match` | https://github.com/ekgus9/FLEX | is_benchmark, is_eval, Has DATA_URL, Code available |
| 471 | 2025-Lahmar-IslamTrust A Benchmark for LLMs Alignment | **8.75** | `Match` | https://github.com/aii-lab-dot-org/IslamTrust | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 472 | 2025-Ligeti-Nagy-HuGME A Benchmark System for Evaluating Hungarian Generative Model | **8.75** | `Match` | https://hugme.nytud.hu/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 473 | 2025-Mekki-NileChat Towards Linguistically Diverse and Culturally Aware LLMs for | **8.75** | `Match` | https://github.com/UBC-NLP/nilechat | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 474 | 2025-Models-Cross-Lingual Fact Verification Analyzing LLM Performance ... | **8.75** | `Match` | https://github.com/Aniezka/cross-lingual-fact- | is_eval, is_dataset, Has DATA_URL, Code available |
| 475 | 2025-Nahin-TituLLMs A Family of Bangla LLMs with Comprehensive Benchmarking | **8.75** | `Match` | https://github.com/hishab-nlp/titulm | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 476 | 2025-Nguyen-VietMEAgent Culturally-Aware Few-Shot Multimodal Explanation for | **8.75** | `Match` | https://huggingface.co/datasets/Dangindev/viet-cul | is_dataset, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 477 | 2025-Ning-LinguaSafe A Comprehensive Multilingual Safety Benchmark for Large | **8.75** | `Match` | https://huggingface.co/datasets/telegraphpolehead/ | is_benchmark, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 478 | 2025-Ning-seeBias | **8.75** | `Match` | https://github.com/nliulab/seeBias | is_eval, is_dataset, Has DATA_URL, Code available |
| 479 | 2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models | **8.75** | `Match` | https://github.com/EQ-bench/EQ-Bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 480 | 2025-Pham-CultureInstruct Curating Multi-Cultural Instructions at Scale | **8.75** | `Match` | https://github.com/thanhpv2102/CultureInstruct | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 481 | 2025-Sadr-We Politely Insist Your LLM Must Learn the Persian Art of Taarof | **8.75** | `Match` | https://github.com/niktaas/TAAROFBENCH | is_benchmark, is_eval, Has DATA_URL, Code available |
| 482 | 2025-Samway-Are Language Models Consequentialist or Deontological | **8.75** | `Match` | https://github.com/keenansamway/moral-lens | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 483 | 2025-Solaiman-BiasLab | **8.75** | `Match` | https://github.com/ksolaiman/PoliticalBiasCorpus | is_eval, is_dataset, Has DATA_URL, Code available |
| 484 | 2025-Sorensen-Operationalizing Pluralistic Values | **8.75** | `Match` | https://github.com/DALIAALISIDDIG/AlignCure | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 485 | 2025-Susanto-A Multi-Labeled Dataset for Indonesian Discourse Examining Toxicity | **8.75** | `Match` | https://huggingface.co/datasets/Exqrch/IndoDiscour | is_dataset, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 486 | 2025-Xu-Leveraging LLM and Self-Supervised Training Models for Speech | **8.75** | `Match` | https://github.com/jeinlee1991/chinese-LLM- | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 487 | 2025-Yu-CMoralEval A Moral Evaluation Benchmark for Chinese ... | **8.75** | `Match` | https://github.com/InternLM/InternLM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 488 | 2025-Yu-MSLR-Bench Multi-Step Legal Reasoning | **8.75** | `Match` | https://github.com/yuwenhan07/MSLR-Bench | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 489 | 2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark | **8.75** | `Match` | https://github.com/Vicentvankor/sun-shine | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 490 | 2025-Zhang-Output Constraints as Attack Surface Exploiting Structured Generation | **8.75** | `Match` | https://github.com/ModelTC/lightllm | is_benchmark, is_eval, Has DATA_URL, Code available |
| 491 | 2025-team-SEA-LION Southeast Asian Languages in One | **8.75** | `Match` | https://github.com/aisingapore/sealion | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 492 | 2026-Kartiyasa-Injecting Knowledge from Social Science Journals to Improve | **8.75** | `Match` | https://github.com/pymupdf/PyMuPDF | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 493 | 2026-Onose-Evaluating Metalinguistic Knowledge in Large Language Models across | **8.75** | `Match` | https://github.com/Oranzna/metalinguistic_ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 494 | 2018-Bohra-Hindi-English Code-Mixed Social Media Text for | **8.55** | `Match` | https://github.com/deepanshu1995/HateSpeech-Hindi- | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 495 | 2019-Fortuna-A Hierarchically-Labeled Portuguese Hate Speech Dataset | **8.55** | `Match` | https://github.com/paulafortuna/Portuguese-Hate-Sp | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 496 | 2020-Kumar-Evaluating Aggression Identification in Social | **8.55** | `Match` | https://sites.google.com/view/trac2/shared-task | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 497 | 2021-Nadeem-StereoSet | **8.55** | `Match` | https://stereoset.mit.edu | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 498 | 2022-Chakravarthi-DravidianCodeMix Sentiment Analysis and Offensive Language | **8.55** | `Match` | https://github.com/bharathichezhiyan/DravidianCode | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 499 | 2022-Joshi-L3Cube-MahaNLP Marathi Natural Language Processing Datasets | **8.55** | `Match` | https://github.com/l3cube-pune/MarathiNLP | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 500 | 2022-Kulkarni-Semantic and Sentiment Analysis of Selected | **8.55** | `Match` | https://github.com/sydney-machine-learning/sentime | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 501 | 2022-Romim-BD-SHS A Benchmark Dataset for Learning to Detect Online Bangla Hate | **8.55** | `Match` | https://github.com/naurosromim/hate-speech-dataset | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 502 | 2023-Byun-Automatic Construction of a Korean Toxic Instruction Dataset for | **8.55** | `Match` | https://github.com/byunsj/KoTox-Korean-Toxic-Instr | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 503 | 2023-Ji-BeaverTails | **8.55** | `Match` | https://sites.google.com/view/pku-beavertails | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 504 | 2023-Yao-Value FULCRA | **8.55** | `Match` | https://ValueCompass.github.io | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 505 | 2024-Baruni-ParsBench Toolkits for Benchmarking LLMs Based on the Persian | **8.55** | `Match` | https://github.com/Ipouyall/Benchmarking_ChatGPT_f | is_benchmark, is_eval, Has DATA_URL, Code available |
| 506 | 2024-Liu-JAILJUDGE | **8.55** | `Match` | https://huggingface.co/datasets/usail-hkust/JailJu | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 507 | 2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub | **8.55** | `Match` | https://huggingface.co/SEACrowd | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 508 | 2024-Park-Open Ko-LLM Leaderboard Evaluating Large Language Models in Korean | **8.55** | `Match` | https://huggingface.co/spaces/upstage/open-ko-llm- | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 509 | 2024-Singhal-AyaRedTeaming | **8.55** | `Match` | https://huggingface.co/datasets/CohereForAI/aya_re | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 510 | 2024-Tonneau-From Languages to Geographies Towards Evaluating Cultural Bias in | **8.55** | `Match` | https://huggingface.co/datasets/manueltonneau/span | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 511 | 2024-Tonneau-Turkish Hate Speech Superset Dataset | **8.55** | `Match` | https://huggingface.co/datasets/manueltonneau/turk | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 512 | 2024-team-Indic-Bias A Comprehensive Benchmark for Fairness | **8.55** | `Match` | https://huggingface.co/datasets/ai4bharat/Indic-Bi | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 513 | 2024-team-Indic-Bias A Comprehensive Benchmark to Evaluate | **8.55** | `Match` | https://github.com/AI4Bharat/indic-bias | is_benchmark, is_eval, Has DATA_URL, Code available |
| 514 | 2025-Becker-The Moralization Corpus | **8.55** | `Match` | https://anonymous.4open.science/r/Moralisierungsde | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 515 | 2025-Pourbahman-ELAB | **8.55** | `Match` | https://huggingface.co/spaces/MCILAB/LLM_Alignment | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 516 | 2025-Schacht-Mapping Moral Reasoning Circuits | **8.55** | `Match` | https://github.com/coairesearch/mapping_moral_reas | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 517 | 2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in | **8.55** | `Match` | https://anonymous.4open.science/r/TrolleyBench-FD4 | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 518 | 2026-He-GVS-Scale and GVS-Bench GenAI Value Safety Scale | **8.55** | `Match` | https://github.com/acl2026/GVS-Bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 519 | 2024-Qiu-ProgressGym | **8.53** | `ModelBasedClassify` | https://github.com/PKU-Alignment/ProgressGym | is_benchmark, Has DATA_URL, Code available, Availability = Public |
| 520 | 2024-Rai-Social Norms in Cinema A Cross-Cultural Analysis of Shame Pride and | **8.53** | `ModelBasedClassify` | https://github.com/Khushangz/Cross-Cultural-Social | is_eval, is_dataset, Has DATA_URL, Code available |
| 521 | 2025-Bai-Explicitly unbiased large language models still form biased | **8.53** | `ModelBasedClassify` | https://github.com/baixuechunzi/llm- | is_benchmark, is_eval, Has DATA_URL, Code available |
| 522 | 2025-Myung-PapersPlease | **8.53** | `ModelBasedClassify` | https://github.com/yeonsuuuu28/papers-please | is_benchmark, is_eval, Has DATA_URL, Code available |
| 523 | 2021-Askell-A General Language Assistant as a Laboratory for | **8.5** | `Match` | https://github.com/unitaryai/detoxify | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 524 | 2021-Emelin-Moral Stories | **8.5** | `ModelBasedClassify` | https://github.com/demelin/moral_stories | is_eval, is_dataset, Has DATA_URL, Code available |
| 525 | 2022-Chriqui-HeBERT & HebEMO a Hebrew BERT Model and a Tool for Polarity Analysis | **8.5** | `Match` | https://huggingface.co/avichr/heBERT_sentiment_ana | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 526 | 2022-Ganguli-Red Teaming Language Models to Reduce Harms | **8.5** | `ModelBasedClassify` | https://github.com/anthropics/hh-rlhf | is_eval, is_dataset, Has DATA_URL, Code available |
| 527 | 2022-Li-Evaluating Psychological Safety of Large Language | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 528 | 2023-Miah-Islam QA | **8.5** | `FuzzyMatch` | https://www.kaggle.com/datasets/abdullahalmamunn/i | is_eval, is_dataset, Has DATA_URL, Availability = Public |
| 529 | 2023-Park-K-HATERS A Hate Speech Detection Corpus in Korean with | **8.5** | `Match` | https://huggingface.co/jhgan/ko-sbert-multitask | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 530 | 2023-Shao-Character-LLM A Trainable Agent for Role-Playing | **8.5** | `Match` | https://github.com/choosewhatulike/trainable-agent | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 531 | 2023-Yu-GPTFuzzer | **8.5** | `Match` | https://github.com/sherdencooper/GPTFuzz | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 532 | 2023-Zou-Universal and Transferable Adversarial Attacks on | **8.5** | `Match` | https://github.com/llm-attacks/llm-attacks | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 533 | 2024-Aliti-Large Language Models LLMs Output Quality Comparison Between English | **8.5** | `Match` | https://github.com/EleutherAI/lm-evaluation-harnes | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 534 | 2024-Cahyawijaya-LLM for everyone | **8.5** | `Match` | https://github.com/IndoNLP/nusax | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 535 | 2024-Chakravarthi-Findings of the Shared Task on | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Dataset size |
| 536 | 2024-Fajcik-BenCzechMark A Czech-centric Multitask and Multimetric Benchmark for | **8.5** | `Match` | https://huggingface.co/BUT-FIT/CSTinyLlama-1.2B | is_benchmark, is_dataset, Has DATA_URL, Availability = Public |
| 537 | 2024-Gabriel-The Ethics of Advanced AI Assistants | **8.5** | `Match` | https://github.com/Significant-Gravitas/Auto-GPT | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 538 | 2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 539 | 2024-Huang-Moral Persuasion in Large Language Models | **8.5** | `Match` | https://github.com/acyhuang/moral-persuasion | is_eval, Has DATA_URL, Code available, Code available |
| 540 | 2024-Koto-Cracking the Code Multi-domain LLM Evaluation on Real-World | **8.5** | `Match` | https://github.com/meta-llama/llama3 | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 541 | 2024-Nayak-Benchmarking Vision Language Models for Cultural Understanding | **8.5** | `Match` | https://culturalvqa.org | is_benchmark, Has DATA_URL, Availability = Public, LLM_assessed |
| 542 | 2024-Pistilli-CIVICS | **8.5** | `Match` | https://huggingface.co/CIVICS-dataset | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 543 | 2024-Research-SEA-VQA Southeast Asian Cultural Context Dataset For Visual Question | **8.5** | `Match` | https://huggingface.co/datasets/wit543/sea-vqa | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 544 | 2024-Souly-StrongREJECT | **8.5** | `Match` | https://strong-reject.readthedocs.io/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 545 | 2024-Thellmann-Towards Multilingual LLM Evaluation for European Languages | **8.5** | `Match` | https://github.com/vllm-project/vllm | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 546 | 2024-Voukoutis-Meltemi The first open Large Language Model for Greek | **8.5** | `Match` | https://huggingface.co/ilsp/Meltemi-7B-v1 | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 547 | 2024-Ye-Measuring Human and AI Values Based on Generative | **8.5** | `Match` | https://github.com/Value4AI/gpv | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 548 | 2024-Yoo-HyperCLOVA X Technical Report | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 549 | 2025-Andriushchenko-AgentHarm | **8.5** | `ModelBasedClassify` | https://huggingface.co/datasets/ai-safety-institut | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 550 | 2025-Azime-ProverbEval Exploring LLM Evaluation Challenges for Low-resource | **8.5** | `Match` | https://huggingface.co/datasets/israel/ProverbEval | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 551 | 2025-Chakraborty-Sometimes the Model doth Preach Quantifying | **8.5** | `Match` | https://github.com/HariShankar08/LLMOpinions | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 552 | 2025-Elle-Reward Model Perspectives on Demographic Alignment Elle et al. | **8.5** | `Match` | https://github.com/socialnlp/rmp | is_eval, Has DATA_URL, Code available, Code available |
| 553 | 2025-Huang-Analysis of LLM Bias Chinese Propaganda & Anti-US Sentiment in | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 554 | 2025-Huang-Values in the Wild Discovering and Analyzing Values in Real AI | **8.5** | `Match` | https://huggingface.co/datasets/Anthropic/values-i | is_eval, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 555 | 2025-Jin-Social Bias Benchmark for Generation A Comparison of Generation and | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, QA format |
| 556 | 2025-Kabir-Break the Checkbox Challenging Closed-Style Evaluations of Cultural | **8.5** | `Match` | https://github.com/ariba-k/llm-cultural-alignment- | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 557 | 2025-Kim-Evaluating Multimodal Generative AI with Korean Educational Standards | **8.5** | `Match` | https://github.com/naver-ai/KoNET | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 558 | 2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages | **8.5** | `Match` | https://github.com/ollama/ollama | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 559 | 2025-Kumar-TeSent A Benchmark Dataset for Fairness-aware | **8.5** | `Match` | NA | is_benchmark, is_eval, is_dataset, LLM_assessed |
| 560 | 2025-LLMs-A Leaderboard to Benchmark Ethical Biases in LLMs | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 561 | 2025-Le Jeune-Phare A Safety Probe for Large Language Models | **8.5** | `Match` | https://huggingface.co/datasets/giskardai/phare, h | is_eval, Has DATA_URL, HuggingFace dataset URL, Code available |
| 562 | 2025-Lin-Machine translation of Chinese classical poetry a comparison among | **8.5** | `Match` | https://osf.io/34cgd | is_eval, Has DATA_URL, LLM_assessed, Rubric |
| 563 | 2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Ethics scenario |
| 564 | 2025-Maheshwari-ParamBench A Graduate-Level Benchmark for Evaluating | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 565 | 2025-Mubarak-IslamicEval 2025 - Shared Task on Capturing LLM Hallucination in | **8.5** | `FuzzyMatch` | https://www.codabench.org/competitions/9820/ | is_eval, Has DATA_URL, LLM_assessed, QA format |
| 566 | 2025-Ni-A Survey on Large Language Model Benchmarks | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 567 | 2025-Nikandrou-CROPE Evaluating In-Context Adaptation of Vision and Language Models | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, QA format |
| 568 | 2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 569 | 2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 570 | 2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Rubric |
| 571 | 2025-Unit-Salamandra Technical Report | **8.5** | `Match` | https://github.com/NVIDIA/NeMo | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 572 | 2025-Wu-Chain-of-Ethics Defense Framework Wu et al. | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 573 | 2025-Xie-Enhancing Multilingual Language Models for Code-Switched Input Data | **8.5** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Classification format |
| 574 | 2025-Xie-SwitchLingua The First Large-Scale Multilingual and Multi-Ethnic | **8.5** | `Match` | NA | is_benchmark, is_eval, is_dataset, LLM_assessed |
| 575 | 2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with | **8.5** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 576 | 2025-Zhang-MedHallTune | **8.5** | `Match` | NA | is_benchmark, is_eval, is_dataset, LLM_assessed |
| 577 | 2025-Zulaika-BasqBBQ Basque BBQ | **8.5** | `Match` | https://huggingface.co/datasets/sst | is_eval, Has DATA_URL, HuggingFace dataset URL, LLM_assessed |
| 578 | 2019-Basile-SemEval-2019 Task 5 | **8.3** | `Match` | https://github.com/msang/hateval | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 579 | 2019-Rashkin-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models | **8.3** | `Match` | https://github.com/facebookresearch/EmpatheticDial | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 580 | 2020-Zueva-Reducing Unintended Identity Bias in Russian Hate Speech Detection | **8.3** | `Match` | https://github.com/vlarine/ruGPT2 | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 581 | 2021-Cercas Curry-ConvAbuse | **8.3** | `Match` | https://github.com/amandacurry/convabuse | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 582 | 2021-Keren-ParaShoot | **8.3** | `Match` | https://github.com/omrikeren/ParaShoot | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 583 | 2021-Nguyen-Constructive and Toxic Speech Detection for Open-domain Social Media | **8.3** | `Match` | https://github.com/tarudesu/ViCTSD | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 584 | 2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments | **8.3** | `Match` | https://github.com/dccuchile/beto | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 585 | 2022-Bang-Enabling Classifiers to Make Judgements | **8.3** | `Match` | https://github.com/makcedward/nlpaug | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 586 | 2022-Jahan-Finnish Hate-Speech Detection on Social Media Using CNN and FinBERT | **8.3** | `Match` | https://github.com/saroarjahan/FinBERT | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 587 | 2022-Micallef-Pre-training Data Quality and Quantity for a Low-Resource Language | **8.3** | `Match` | https://huggingface.co/MLRS/BERTu | is_eval, is_dataset, Has DATA_URL, LLM_assessed |
| 588 | 2022-Ramponi-Addressing Religious Hate Online From Taxonomy | **8.3** | `Match` | https://github.com/dhfbk/religious-hate-speech | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 589 | 2022-Sahoo-Detecting Unintended Social Bias in Toxic | **8.3** | `Match` | https://github.com/sahoonihar/ToxicBias_CoNLL_2022 | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 590 | 2022-Schramowski-I2P Inappropriate Image Prompts Test Bed | **8.3** | `Match` | https://github.com/ml-research/Q16 | Has DATA_URL, Code available, Availability = Public, Code available |
| 591 | 2022-Seker-AlephBERT A Hebrew Large Pre-Trained Language Model to Start-off your | **8.3** | `Match` | https://github.com/OnlpLab/AlephBERT | is_benchmark, is_eval, Has DATA_URL, Code available |
| 592 | 2022-Winata-NusaX Multilingual Parallel Sentiment Dataset for 10 Indonesian Local | **8.3** | `Match` | https://github.com/explosion/spaCy | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 593 | 2022-researchers-Hate Speech Classification in Bulgarian | **8.3** | `Match` | https://github.com/vpodpecan/lemmagen3 | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 594 | 2023-Abhinand-Tamil-Llama A New Tamil Language Model | **8.3** | `Match` | https://huggingface.co/abhinand/tamil-llama-7b-ins | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 595 | 2023-Barrett-Skin Deep | **8.3** | `Match` | https://github.com/Social-Futures-Lab/skin-deep | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 596 | 2023-Dai-Safe RLHF | **8.3** | `Match` | https://github.com/PKU-Alignment/safe-rlhf | Has DATA_URL, Code available, Availability = Public, Code available |
| 597 | 2023-Han-FFB | **8.3** | `Match` | https://github.com/ahxt/fair_fairness_benchmark | is_benchmark, is_eval, Has DATA_URL, Code available |
| 598 | 2023-Kirk-SemEval-2023 Task 10 | **8.3** | `Match` | https://github.com/rewire-online/edos | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 599 | 2023-Kuriyozov-Text classification dataset and analysis for | **8.3** | `Match` | https://github.com/elmurod1202/textclassification | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 600 | 2023-Li-Can LLM Already Serve as A Database Interface | **8.3** | `Match` | https://bird-bench.github.io/ | is_benchmark, is_dataset, Has DATA_URL, LLM_assessed |
| 601 | 2023-Lin-Taiwan LLM Bridging the Linguistic Divide with a Culturally Aligned | **8.3** | `Match` | https://github.com/MiuLab/Taiwan-LLM | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 602 | 2023-Ray-Benchmarking, ethical alignment, and evaluation | **8.3** | `Match` | https://github.com/alexa/alexa-with-dstc10-track2- | is_benchmark, is_eval, Has DATA_URL, Code available |
| 603 | 2023-Takeshita-JCommonsenseMorality Japanese Dataset for Evaluating Commonsense | **8.3** | `ModelBasedClassify` | https://github.com/Language-Media-Lab/commonsense- | is_eval, is_dataset, Has DATA_URL, Code available |
| 604 | 2024-Alekseev-Benchmarking Multilabel Topic Classification in the Kyrgyz Language | **8.3** | `Match` | https://github.com/UniversalDependencies/UD_Kyrgyz | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 605 | 2024-Anonymous-ForbiddenQuestions | **8.3** | `Match` | https://github.com/verazuo/jailbreak_llms | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 606 | 2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive | **8.3** | `Match` | https://github.com/rafaelgoldzy/AustroTox | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 607 | 2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators - | **8.3** | `Match` | https://github.com/jagol/gahd | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 608 | 2024-Htet-Myanmar XNLI Building a Dataset and | **8.3** | `Match` | https://github.com/cdpierse/transformers-interpret | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 609 | 2024-Jin-WenMind A Comprehensive Benchmark for Evaluating | **8.3** | `Match` | https://github.com/SCUT-DLVCLab/WenMind ; https:// | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 610 | 2024-Khaksar-Shifting from Endangerment to Rebirth in the Artificial Intelligence | **8.3** | `Match` | https://github.com/KurdishBLARK/HawramiClassificat | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 611 | 2024-Kirch-TRIAGE | **8.3** | `Match` | https://github.com/NLie2/Triage | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 612 | 2024-Mondshine-HeSum a Novel Dataset for Abstractive Text Summarization in Hebrew | **8.3** | `Match` | https://github.com/OnlpLab/HeSum | is_eval, is_dataset, Has DATA_URL, Code available |
| 613 | 2024-Mou-SGBench | **8.3** | `ModelBasedClassify` | https://github.com/MurrayTom/SG-Bench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 614 | 2024-Paraskevopoulos-A Comparative Sentiment Analysis of Greek Clinical Conversations | **8.3** | `Match` | https://github.com/codelucas/newspaper | is_eval, is_dataset, Has DATA_URL, Code available |
| 615 | 2024-Piatti-Cooperate or Collapse | **8.3** | `Match` | https://github.com/giorgiopiatti/GovSim | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 616 | 2024-Reuel-BetterBench | **8.3** | `Match` | https://betterbench.stanford.edu | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 617 | 2024-Shahi-Hate Speech Detection Using Cross-Platform Social Media Data In | **8.3** | `Match` | https://github.com/Gautamshahi/BilingualYouTubeHat | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 618 | 2024-Sorensen-A Roadmap to Pluralistic Alignment | **8.3** | `Match` | NA | is_benchmark, Availability = Public, LLM_assessed, Ethics scenario |
| 619 | 2024-Sorensen-Value Kaleidoscope | **8.3** | `Match` | https://huggingface.co/datasets/allenai/ValuePrism | Has DATA_URL, HuggingFace dataset URL, Availability = Public, LLM_assessed |
| 620 | 2024-Team-GuardBench | **8.3** | `Match` | https://github.com/AmenRa/guardbench | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 621 | 2024-Vladimirova-FairJob | **8.3** | `Match` | https://huggingface.co/datasets/criteo/FairJob | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 622 | 2024-Yang-LLM Voting Human Choices and AI Collective Decision-Making | **8.3** | `Match` | https://github.com/joshuay1/zurich-pb-voting | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 623 | 2024-Zeng-Leveraging Large Language Models for Code-Mixed | **8.3** | `Match` | https://github.com/lindazeng979/LLM-CMSA | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 624 | 2024-team-L3Cube-IndicQuest A Benchmark Question Answering Dataset | **8.3** | `Match` | https://github.com/facebookresearch/MLQA | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 625 | 2024-team-MahaMarathi-7B Marathi Large Language Model | **8.3** | `Match` | https://huggingface.co/marathi-llm/MahaMarathi-7B- | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 626 | 2024-team-OpenThaiGPT 15 A Thai-Centric Open Source | **8.3** | `Match` | https://huggingface.co/openthaigpt | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 627 | 2025-Aravinda-SinLlama A Large Language Model for Sinhala | **8.3** | `Match` | https://github.com/openai/tiktoken | is_eval, is_dataset, Has DATA_URL, Code available |
| 628 | 2025-Azad-KurdABSA Kurdish Aspect-Based Sentiment Analysis Dataset Curation | **8.3** | `Match` | https://data.mendeley.com/datasets/h5t7p4bcj2/1 | is_dataset, Has DATA_URL, LLM_assessed, Classification format |
| 629 | 2025-Batzner-GermanPartiesQA Benchmarking LLMs for Political Alignment and | **8.3** | `Match` | https://github.com/janbatzner/GermanPartiesQA | is_benchmark, is_eval, Has DATA_URL, Code available |
| 630 | 2025-Derner-Leveraging Large Language Models to Measure Gender Representation | **8.3** | `Match` | https://github.com/ellisalicante/grb-corpora | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 631 | 2025-González-Borrego-IberBench LLM Evaluation on Iberian Languages | **8.3** | `Match` | https://github.com/IberBench/dataset-preparation | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 632 | 2025-Gómez-RigoChat 2 An Adapted Language Model to Spanish Using a Bounded | **8.3** | `Match` | https://github.com/huggingface/peft | is_eval, is_dataset, Has DATA_URL, Code available |
| 633 | 2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for | **8.3** | `Match` | https://github.com/The-Responsible-AI-Initiative/L | is_benchmark, is_eval, Has DATA_URL, Code available |
| 634 | 2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the | **8.3** | `Match` | https://github.com/chapagaisa/hate_speech_detectio | is_eval, is_dataset, Has DATA_URL, Code available |
| 635 | 2025-Lan-Fuxi A Benchmark for Evaluating Language | **8.3** | `Match` | Benchmark, evaluation toolkit, and baseline result | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 636 | 2025-Lee-KOTOX A Korean Toxic Dataset for Deobfuscation and Detoxification | **8.3** | `Match` | https://github.com/leeyejin1231/KOTOX | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 637 | 2025-Leonardelli-MuLTa-Telegram A Fine-Grained Italian and Polish Dataset for Hate | **8.3** | `Match` | https://github.com/LonamiWebs/Telethon | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 638 | 2025-Li-SafetyAnalyst | **8.3** | `Match` | https://jl3676.github.io/SafetyAnalyst/ | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 639 | 2025-Liu-Comparing diversity negativity and stereotypes in Chinese-language AI | **8.3** | `Match` | https://github.com/jaaack-wang/Chinese-Synonyms | is_eval, is_dataset, Has DATA_URL, Code available |
| 640 | 2025-Liu-CultureVLM Characterizing and Improving Cultural Understanding of | **8.3** | `Match` | https://culturevlm.github.io | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 641 | 2025-Liu-JailBench A Comprehensive Chinese Security Assessment Benchmark for | **8.3** | `Match` | https://github.com/STAIR-BUPT/JailBench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 642 | 2025-Liu-LongEmotion Measuring Emotional Intelligence of Large Language Models | **8.3** | `Match` | https://longemotion.github.io/ | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 643 | 2025-Liu-Probing Social Identity Bias in Chinese LLMs with Gendered Pronouns | **8.3** | `Match` | https://github.com/fxsjy/jieba | is_eval, is_dataset, Has DATA_URL, Code available |
| 644 | 2025-Liu-The Scales of Justitia | **8.3** | `Match` | https://github.com/meta-llama/PurpleLlama | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 645 | 2025-Lyu-Characterizing Bias Benchmarking Large Language Models in Simplified | **8.3** | `Match` | https://github.com/brucelyu17/SC-TC-Bench | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 646 | 2025-Masood-Dialectal substitution as an adversarial approach for evaluating | **8.3** | `Match` | https://github.com/elnagara/HARD-Arabic-Dataset | is_eval, is_dataset, Has DATA_URL, Code available |
| 647 | 2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks | **8.3** | `Match` | https://github.com/BenchRisk | is_benchmark, is_eval, Has DATA_URL, Code available |
| 648 | 2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language | **8.3** | `Match` | https://github.com/mohammadi-hadi/cultural-moral-j | is_dataset, Has DATA_URL, Code available, Code available |
| 649 | 2025-Molchanova-Exploring the Potential of Large Language Models | **8.3** | `Match` | https://github.com/mary-silence/simulating_ | is_eval, is_dataset, Has DATA_URL, Code available |
| 650 | 2025-Monnar-Cross-lingual hate speech detection using domain-specific word | **8.3** | `Match` | https://github.com/facebookresearch/XLM | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 651 | 2025-Pandey-Creating and Evaluating Code-Mixed Nepali-English and | **8.3** | `Match` | https://github.com/Ranveer098/Code-Mix-and-Code-Sw | is_eval, is_dataset, Has DATA_URL, Code available |
| 652 | 2025-Park-Ko-MuSR A Multistep Soft Reasoning Benchmark for LLMs Capable of | **8.3** | `Match` | https://github.com/EleutherAI/hae-rae | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 653 | 2025-Rashid-Evaluating Prompt Injection Attacks with | **8.3** | `Match` | https://github.com/williamSYSU/TextGAN-PyTorch | is_eval, is_dataset, Has DATA_URL, Code available |
| 654 | 2025-Scheible-Schmitt-HalleluBERT Let every token that has meaning bear its weight | **8.3** | `Match` | https://github.com/microsoft/nni | is_benchmark, is_eval, Has DATA_URL, Code available |
| 655 | 2025-Shafique-Alif Advancing Urdu Large Language Models | **8.3** | `Match` | https://github.com/tatsu-lab/alpaca_eval | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 656 | 2025-Sharmaa-Hate Speech Detection in Somali-English Code-Switched | **8.3** | `Match` | https://github.com/anubhakabra/MoH_Hate_Speech_Det | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 657 | 2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English | **8.3** | `Match` | https://huggingface.co/datasets/ReliableAI/IRLBenc | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 658 | 2025-Vargas-Context-Aware and Expert Data Resources for Brazilian Portuguese Hate | **8.3** | `Match` | https://github.com/franciellevargas/HateBR | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 659 | 2025-Yu-TLUE A Tibetan Language Understanding Evaluation | **8.3** | `Match` | https://github.com/Vicentvankor/TLUE | is_benchmark, is_eval, Has DATA_URL, Code available |
| 660 | 2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large | **8.3** | `Match` | https://github.com/kztakemoto/mmllm | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 661 | 2025-Zhou-WYWEB A NLP Evaluation Benchmark For Classical Chinese | **8.3** | `Match` | https://github.com/baudzhou/WYWEB | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 662 | 2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding | **8.3** | `Match` | https://huggingface.co/datasets/graalul/COLE-publi | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 663 | 2026-Chang-Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects | **8.3** | `Match` | https://github.com/kalvinchang/yubao | is_benchmark, is_eval, Has DATA_URL, Code available |
| 664 | 2026-Gao-Adversarial Alignment Ensuring Value Consistency in Large Language | **8.3** | `Match` | https://github.com/Ad-Align/VC-LLM | is_eval, is_dataset, Has DATA_URL, Code available |
| 665 | 2026-Goel-Building Interpretable Models for Moral Decision-Making | **8.3** | `Match` | https://github.com/Lossfunk/modeling-moral-machine | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 666 | 2026-Lee-BiasJailbreak | **8.3** | `Match` | https://github.com/Isaac-theori/BiasJailbreak | Has DATA_URL, Code available, Availability = Public, LLM_assessed |
| 667 | 2026-Rehman-X-MuTeST A Multilingual Benchmark for Explainable | **8.3** | `Match` | https://huggingface.co/datasets/UVSKKR/X-MuTeST | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 668 | 2024-AlKhamissi-Investigating Cultural Alignment of LLMs | **8.28** | `ModelBasedClassify` | https://github.com/bkhmsi/cultural-trends.git | is_eval, is_dataset, Has DATA_URL, Code available |
| 669 | 2024-Jinnai-Does Cross-Cultural Alignment Change the Commonsense Morality of | **8.28** | `ModelBasedClassify` | https://huggingface.co/datasets/cyberagent/chatbot | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 670 | 2024-Marraffini-The Greatest Good Benchmark | **8.28** | `ModelBasedClassify` | https://github.com/noehsueh/greatest-good-benchmar | is_benchmark, is_eval, Has DATA_URL, Code available |
| 671 | 2025-Jiang-Raising the Bar | **8.28** | `ModelBasedClassify` | https://github.com/Salomeeeee/GETA | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 672 | 2025-Shen-ValueCompass A Framework for Measuring Contextual Value Alignment | **8.28** | `ModelBasedClassify` | https://github.com/huashen218/value_action_gap | is_eval, Has DATA_URL, Code available, Availability = Public |
| 673 | 2025-Wu-CVC | **8.28** | `ModelBasedClassify` | https://huggingface.co/datasets/Beijing-AISI/C-VAR | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 674 | 2025-Wu-OpenDeception | **8.28** | `ModelBasedClassify` | https://anonymous.4open.science/r/OpenDeception-C1 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 675 | 2019-Usbeck-Benchmarking question answering systems | **8.25** | `FuzzyMatch` | https://github.com/AKSW/gerbil/tree/QuestionAnswer | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 676 | 2023-Andrus-Augmented Datasheets for Speech Datasets and | **8.25** | `Match` | https://github.com/SonyResearch/project_ethics_aug | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 677 | 2023-Nhan-ViGPTQA - State-of-the-Art LLMs for Vietnamese Question Answering | **8.25** | `FuzzyMatch` | https://huggingface.co/VietAI/gpt-neo-1 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 678 | 2024-Choi-CaLMQA Exploring culturally specific long-form question | **8.25** | `FuzzyMatch` | https://huggingface.co/datasets/shanearora/CaLMQA | is_eval, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 679 | 2024-Compostela-Open Generative Large Language Models for Galician | **8.25** | `Match` | https://huggingface.co/HiTZ/latxa-7b-v1 | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 680 | 2024-Li-THRONE | **8.25** | `Match` | https://github.com/amazon-science/THRONE | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 681 | 2024-Moon-BEAF | **8.25** | `Match` | https://beafbench.github.io/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 682 | 2024-Ren-Safetywashing | **8.25** | `Match` | NA | is_benchmark, is_eval, Availability = Public, LLM_assessed |
| 683 | 2024-Saito-Why We Build Local Large Language Models An Observational Analysis | **8.25** | `Match` | https://doi.org/10.5281/zenodo.13160661 | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 684 | 2024-Vayani-All Languages Matter | **8.25** | `Match` | https://mbzuai-oryx.github.io/ALM-Bench/ | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 685 | 2024-Zhou-tSMC | **8.25** | `Match` | https://huggingface.co/google/gemma-2b-it | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 686 | 2025-Al-Towards a Multilingual Assessment of Stereotypes in Large ... | **8.25** | `Match` | NA | is_eval, is_dataset, Availability = Public, LLM_assessed |
| 687 | 2025-Barth-Multilingual European Language Models Benchmarking Approaches and | **8.25** | `Match` | https://huggingface.co/datasets/openai/MMMLU | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 688 | 2025-Bian-Healthcare Ethics & Safety QA China - Healthy China 2030 | **8.25** | `Match` | https://medbench.opencompass.org.cn/community/data | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 689 | 2025-Cognitive-TIFD Tibetan Instruction-Following Dataset for Large Language Models | **8.25** | `Match` | https://github.com/tatsu-lab/stanford_alpaca | is_dataset, Has DATA_URL, Code available, LLM_assessed |
| 690 | 2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large | **8.25** | `Match` | https://huggingface.co/spaces/sdadas | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 691 | 2025-Erdem-Cetvel A Unified Benchmark for Evaluating | **8.25** | `Match` | https://huggingface.co/spaces/KUIS-AI/Cetvel | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 692 | 2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a | **8.25** | `Match` | https://huggingface.co/datasets | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 693 | 2025-Hu-EmoBench-M Benchmarking Emotional Intelligence for Multimodal Large | **8.25** | `Match` | https://emo-gml.github.io/ | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 694 | 2025-Islamic-Sacred or Synthetic Evaluating LLM Reliability and Abstention for | **8.25** | `Match` | https://huggingface.co/datasets/MBZUAI/FiqhQA | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 695 | 2025-Ju-NaVAB | **8.25** | `Match` | https://huggingface.co/datasets/JadenGGGeee/NaVAB | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 696 | 2025-Khan-Low-Resource Dialect Adaptation of Large Language Models A French | **8.25** | `Match` | https://github.com/CLaC-Lab/QuebecLLM-CPT | is_benchmark, is_dataset, Has DATA_URL, Code available |
| 697 | 2025-Koto-Sherkala-Chat Building a State-of-the-Art LLM for Kazakh in a | **8.25** | `Match` | https://huggingface.co/inceptionai/Llama-3.1-Sherk | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 698 | 2025-Lahmar-IslamTrust A Benchmark for LLMs Alignment with Islamic Values | **8.25** | `Match` | https://huggingface.co/QCRI/Fanar-1-9B-Instruct | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 699 | 2025-Lazzaroni-MedBench-IT A Comprehensive Benchmark for Evaluating LLMs on Italian | **8.25** | `Match` | https://huggingface.co/anakin87/gemma-2-9b-neogene | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 700 | 2025-Maji-DRISHTIKON A Multimodal Multilingual Benchmark for | **8.25** | `Match` | https://huggingface.co/datasets/13ari/DRISHTIKON | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 701 | 2025-Maji-SANSKRITI A Comprehensive Benchmark for Evaluating | **8.25** | `Match` | https://huggingface.co/datasets/13ari/Sa | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 702 | 2025-Menke-How Effective Is Constitutional AI in Small LLMs | **8.25** | `Match` | https://zenodo.org/records/12608602 | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 703 | 2025-Monazzah-PerCul A Story-Driven Cultural Evaluation of LLMs in Persian | **8.25** | `Match` | https://huggingface.co/datasets/teias-ai/percul | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 704 | 2025-Narnaware-SB-Bench | **8.25** | `Match` | NA | is_benchmark, is_eval, is_dataset, Availability = Public |
| 705 | 2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs | **8.25** | `Match` | https://huggingface.co/spaces/Eurolingua | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 706 | 2025-Pothavorn-NitiBench A Comprehensive Study of LLM | **8.25** | `FuzzyMatch` | https://github.com/vistec-ai/nitibench | is_benchmark, is_eval, Has DATA_URL, Code available |
| 707 | 2025-Rastogi-DIVE Dataset for Pluralistic Alignment of Text-to-Image Models | **8.25** | `Match` | https://huggingface.co/datasets/neurips-dataset-12 | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 708 | 2025-Sadallah-Commonsense Reasoning in Arab Culture | **8.25** | `Match` | https://huggingface.co/datasets/MBZUAI/ArabCulture | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 709 | 2025-Sakhadib-Evaluating Arabic Large Language Models A Survey of Benchmarks | **8.25** | `Match` | https://huggingface.co/spaces/OALL | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 710 | 2025-Sakhadib-Towards Inclusive Arabic LLMs A Culturally Aligned Benchmark in | **8.25** | `Match` | https://huggingface.co/datasets/openai/MMMLU | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 711 | 2025-Salazar-Kaleidoscope | **8.25** | `Match` | https://hf.co/datasets/CohereForAI/kaleidoscope | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 712 | 2025-Son-From KMMLU-Redux to KMMLU-Pro A Professional Korean Benchmark Suite | **8.25** | `Match` | https://huggingface.co/datasets/LGAI-EXAONE | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 713 | 2025-Son-HRET A Self-Evolving LLM Evaluation Toolkit for Korean | **8.25** | `Match` | https://huggingface.co/meta-llama/Llama-3 | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 714 | 2025-Yao-NurValues | **8.25** | `Match` | https://huggingface.co/datasets/Ben012345/NurValue | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 715 | 2025-Zbeeb-AraLingBench A Human-Annotated Benchmark for Evaluating Arabic | **8.25** | `Match` | https://huggingface.co/Navid-AI/Yehia-7B-preview | is_benchmark, is_eval, Has DATA_URL, LLM_assessed |
| 716 | 2025-Zulaika-BasqBBQ A QA Benchmark for Assessing Social Biases in LLMs for Basque | **8.25** | `Match` | https://github.com/orai-nlp/BasqBBQ | is_benchmark, is_eval, Has DATA_URL, Code available |
| 717 | 2025-team-SeaExam and SeaBench Benchmarking LLMs with | **8.25** | `Match` | https://github.com/DAMO-NLP-SG/SeaExam | is_benchmark, Has DATA_URL, Code available, LLM_assessed |
| 718 | 2026-Karimi-Malekabadi-Theory Trace Card TTC Documentation for Socio-Cognitive Benchmarks | **8.25** | `Match` | NA | is_benchmark, is_eval, Availability = Public, LLM_assessed |
| 719 | 2018-Crone-The Socio-Moral Image Database (SMID) | **8.05** | `Match` | https://osf.io/2rqad/ | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 720 | 2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred | **8.05** | `Match` | http://saifmohammad.com/WebPages/Biases-SA.html | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 721 | 2021-Hansson-The Swedish Winogender Dataset SweWinogender | **8.05** | `Match` | https://spraakbanken.gu.se/en/resources/swewinogen | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 722 | 2021-Plaza-del-Arco-OffendES A New Corpus in Spanish for Offensive Language Research | **8.05** | `Match` | https://huggingface.co/datasets/fmplaza/offendes | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 723 | 2022-Hendrycks-What Would Jiminy Cricket Do | **8.05** | `ModelBasedClassify` | https://github.com/hendrycks/jiminy-cricket | is_eval, Has DATA_URL, Code available, Availability = Public |
| 724 | 2022-Kim-ProsocialDialog | **8.05** | `Match` | https://hyunw.kim/prosocial-dialog | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 725 | 2022-Sun-MoralDial | **8.05** | `Match` | https://github.com/thu-coai/MoralDial | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 726 | 2023-Grotti-Italian Linguistic Features for Toxic Language Detection in Social | **8.05** | `Match` | https://github.com/musixmatchresearch/umberto | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 727 | 2023-Harrington-I'm Fully Who I Am | **8.05** | `Match` | https://github.com/anaeliaovalle/TANGO-Centering-T | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 728 | 2023-Kohli-Building a Llama2-finetuned LLM for Odia Language Utilizing Domain | **8.05** | `Match` | https://github.com/AI4Bharat/indicTrans | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 729 | 2023-Li-Evaluating Object Hallucination in Large | **8.05** | `Match` | https://github.com/RUCAIBox/POPE | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 730 | 2023-Rao-What Makes it Ok to Set a Fire Iterative | **8.05** | `Match` | https://huggingface.co/datasets/kavelrao/d-Rules-o | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 731 | 2024-Chen-EmotionQueen A Benchmark for Evaluating Empathy of Large Language | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Classification format |
| 732 | 2024-Garcia-Open Portuguese LLM Leaderboard | **8.05** | `Match` | https://huggingface.co/spaces/eduagarcia/open_pt_l | is_benchmark, is_eval, is_dataset, Has DATA_URL |
| 733 | 2024-Simpson-Parity Benchmark for Measuring Bias in | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 734 | 2024-Tharnpipitchai-Typhoon 2 A Family of Open | **8.05** | `Match` | https://huggingface.co/scb10x/typhoon2-safety-prev | is_dataset, Has DATA_URL, Availability = Public, LLM_assessed |
| 735 | 2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of | **8.05** | `Match` | https://huggingface.co/datasets/manueltonneau/hate | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 736 | 2024-Toygar-Turkish Offensive Language Detection Dataset | **8.05** | `Match` | https://huggingface.co/datasets/Toygar/turkish-off | is_eval, is_dataset, Has DATA_URL, HuggingFace dataset URL |
| 737 | 2024-Trajano-OLID-BR Offensive Language Identification Dataset for Brazilian | **8.05** | `Match` | https://github.com/DougTrajano/olid-br | is_dataset, Has DATA_URL, Code available, Availability = Public |
| 738 | 2024-Yang-DistillSeq | **8.05** | `Match` | https://github.com/facebookresearch/llama | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 739 | 2024-Zeng-AIR-Bench 2024 | **8.05** | `Match` | https://huggingface.co/datasets/stanford-crfm/air- | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 740 | 2024-Zhang-SnakModel Lessons Learned from Training an Open Danish Large Language | **8.05** | `Match` | https://github.com/NVIDIA/Megatron-LM | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 741 | 2024-team-VLegal-Bench Cognitively Grounded Benchmark for Vietnamese Legal | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 742 | 2025-Assis-Exploring Brazil's LLM Fauna Investigating the Generative Performance | **8.05** | `Match` | https://github.com/MeLLL-UFF/brfauna-gen-eval | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 743 | 2025-Dementieva-Overview of the Multilingual Text Detoxification Task at PAN 2025 | **8.05** | `Match` | https://github.com/LDNOOBW/List-of-Dirty-Naughty-O | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 744 | 2025-Ghorbanpour-Data-Efficient Hate Speech Detection via Cross-Lingual ... | **8.05** | `Match` | https://github.com/FlagOpen/FlagEmbedding | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 745 | 2025-Hackett-Bypassing LLM guardrails character and AML attacks in practice - | **8.05** | `Match` | https://github.com/NoDataFound/hackGPT | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 746 | 2025-Johannesburg-Sentiment Analysis in African Languages Evaluating | **8.05** | `Match` | https://github.com/dteodore/EmotionArcs | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 747 | 2025-Liu-Cross-cultural value alignment frameworks | **8.05** | `Match` | NA | is_eval, is_dataset, LLM_assessed, Ethics scenario |
| 748 | 2025-Liu-PersuSafety LLM Can be a Dangerous Persuader | **8.05** | `Match` | https://github.com/PLUM-Lab/PersuSafety | is_eval, Has DATA_URL, Code available, Code available |
| 749 | 2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in | **8.05** | `Match` | https://github.com/momijiro/stereotype_japanese_ll | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 750 | 2025-Niklaus-SwiLTra-Bench The Swiss Legal Translation Benchmark | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 751 | 2025-Pavlopoulos-Open or Closed LLM for Lesser-Resourced Languages Lessons from Greek | **8.05** | `Match` | https://github.com/eellak/gsoc2018-spacy | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 752 | 2025-Sah-FairEval Evaluating Fairness in LLM-Based ... | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 753 | 2025-Sistla-SPARC Evaluating LLMs in Open-Source Games Strategic Program Analysis | **8.05** | `Match` | https://github.com/swadeshs/llm-osgt | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 754 | 2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large | **8.05** | `Match` | https://github.com/chenkaisun/SocialSense | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 755 | 2025-Sun-Evaluating ChatGPT's Performance in Creative Text ... | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 756 | 2025-Sun-Evaluating the Translation Accuracy of ChatGPT and DeepL Through the | **8.05** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 757 | 2025-Zhu-EAVIT | **8.05** | `Match` | NA | is_eval, is_dataset, Code available, LLM_assessed |
| 758 | 2026-Yun-VAPT Value-Alignment Perception Toolkit | **8.05** | `Match` | https://github.com/KaluJo/chatbot-study | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 759 | 2020-Awad-Universals and variations in moral decisions made | **8.0** | `Match` | https://moralmachine.mit.edu | is_dataset, Has DATA_URL, Availability = Public, Has data_metrics |
| 760 | 2020-Brown-Language Models are Few-Shot Learners | **8.0** | `Match` |  | is_benchmark, is_eval, is_dataset, QA format |
| 761 | 2023-Kaddour-Challenges and Applications of Large Language | **8.0** | `Match` | https://github.com/NVIDIA/FasterTransformer | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 762 | 2023-Kahira-AfriQA Cross-lingual Open-Retrieval Question Answering for | **8.0** | `FuzzyMatch` | https://huggingface.co/datasets/masakhane/afriqa | is_dataset, Has DATA_URL, HuggingFace dataset URL, Availability = Public |
| 763 | 2023-Shen-Large Language Model Alignment | **8.0** | `Match` | https://github.com/tatsu-lab/alpaca_eval | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 764 | 2024-Bang-Measuring Political Bias in LLMs What Is Said and How It Is Said | **8.0** | `Match` | NA | is_benchmark, is_eval, LLM_assessed, Rubric |
| 765 | 2024-Kim-Open Ko-LLM Leaderboard2 Bridging Foundational and Practical | **8.0** | `Match` | NA | is_benchmark, is_eval, is_dataset, Rubric |
| 766 | 2024-Owen-Komodo A Linguistic Expedition into Indonesia's Regional Languages | **8.0** | `Match` | https://github.com/aisingapore/sealion | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 767 | 2024-Sagyndyk-Kazakh Dastur-MC Multiple Choice Benchmark | **8.0** | `Match` | https://huggingface.co/datasets/kz-transformers/ka | is_benchmark, is_eval, Has DATA_URL, HuggingFace dataset URL |
| 768 | 2024-Saketos-The Large Language Model GreekLegalRoBERTa | **8.0** | `Match` | https://github.com/AI-team-UoA/GreekLegalRoBERTa | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 769 | 2024-community-Open Leaderboard for Hebrew LLMs | **8.0** | `FuzzyMatch` | https://huggingface.co/spaces/hebrew-llm-leaderboa | is_benchmark, is_eval, Has DATA_URL, Availability = Public |
| 770 | 2025-Ahmed-An Analysis of Chinese Censorship Bias in LLMs Mohamed Ahmed | **8.0** | `Match` | https://github.com/citizenlab/chat-censorship | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 771 | 2025-Andric-Do LLMs Walk Their Talk Multi-Method Moral Evaluation Framework | **8.0** | `Match` | https://github.com/sandroandric/LLMs_Altruism_ | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 772 | 2025-Compostela-Enhancing Large Language Models for Underrepresented Varieties | **8.0** | `Match` | https://github.com/proxectonos/instruction_dataset | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 773 | 2025-Corrêa-Tucano Advancing Neural Text Generation for Portuguese | **8.0** | `Match` | https://github.com/huggingface/tokenizers | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 774 | 2025-Ghaly-Assessing Large Language Models on Islamic | **8.0** | `Match` | https://github.com/bouchekif/inheritance_evaluatio | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 775 | 2025-Hosseinbeigi-Matina A Culturally-Aligned Persian Language Model Using Multiple | **8.0** | `Match` | NA | is_dataset, LLM_assessed, Rubric, Dataset size |
| 776 | 2025-Pretrained-Optimizing Uyghur Speech Synthesis by Combining Pretrained | **8.0** | `Match` | NA | is_eval, is_dataset, Rubric, Dataset size |
| 777 | 2025-Pretrained-Research on the Training and Application Methods of a Lightweight | **8.0** | `Match` | NA | is_eval, is_dataset, Rubric, Dataset size |
| 778 | 2025-Shi-Benchmarking four large language models’ performance of addressing | **8.0** | `Match` | NA | is_benchmark, is_eval, Rubric, Ethics scenario |
| 779 | 2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs | **8.0** | `Match` | https://github.com/citizenlab/chat-censorship | Has DATA_URL, Code available, LLM_assessed, Rubric |
| 780 | 2025-Yan-Decolonizing African NLP A Survey on Power Dynamics and Data | **8.0** | `Match` | NA | is_eval, is_dataset, Rubric, Dataset size |
| 781 | 2025-Zhang-CultureScope A Dimensional Lens for Probing | **8.0** | `Match` | https://github.com/HoganZinger/Culture | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 782 | 2025-Zhang-CultureSynth A Hierarchical Taxonomy-Guided and Retrieval-Augmented | **8.0** | `Match` | https://github.com/Eyr3/CultureSynth | is_eval, Has DATA_URL, Code available, LLM_assessed |
| 783 | 2025-Zhang-Safety Evaluation and Enhancement of DeepSeek Models in Chinese | **8.0** | `Match` | https://github.com/UnicomAI/DeepSeek-R1-Safe | is_eval, Has DATA_URL, Code available, LLM_assessed |

## 2. Possible (5.0-8.0)

872 papers are feasible with some data preparation.

| # | Paper | Score | Template | Missing Dimensions |
|---|-------|-------|----------|--------------------|
| 1 | 2022-Névéol-French CrowS-Pairs Extending a challenge dataset for measuring social | 7.9 | `ModelBasedClassify` | Eval template mappable |
| 2 | 2024-Wang-Do-Not-Answer | 7.9 | `ModelBasedClassify` | Eval template mappable |
| 3 | 2024-Wang-KULTURE Bench A Benchmark for Assessing Language Model in Korean | 7.9 | `ModelBasedClassify` | Eval template mappable |
| 4 | 2025-Li-T2ISafety | 7.9 | `ModelBasedClassify` | Eval template mappable |
| 5 | 2016-Bolukbasi-Man is to Computer Programmer as Woman is to | 7.8 | `Match` | Code/repo available |
| 6 | 2018-Amram-Representations and Architectures in Neural Sentiment Analysis for | 7.8 | `Match` | LLM evaluation exists |
| 7 | 2018-Wiegand-GermEval 2018 Shared Task on the Identification of Offensive Language | 7.8 | `Match` | LLM evaluation exists |
| 8 | 2019-Ptaszynski-Results of the PolEval 2019 Shared Task 6 First Dataset and Open | 7.8 | `Match` | LLM evaluation exists |
| 9 | 2020-Schramowski-The Moral Choice Machine | 7.8 | `Match` | LLM evaluation exists |
| 10 | 2020-Shekhar-Automating News Comment Moderation with Limited Resources | 7.8 | `Match` | Quantified data size |
| 11 | 2020-Zampieri-SemEval-2020 Task 12 | 7.8 | `Match` | Quantified data size |
| 12 | 2021-Adelani-MasakhaNER Named Entity Recognition for African | 7.8 | `Match` | Quantified data size |
| 13 | 2021-Saha-Hate-Alert@DravidianLangTech-EACL2021 Ensembling Strategies for | 7.8 | `Match` | Quantified data size |
| 14 | 2022-Das-Hate Speech and Offensive Language Detection | 7.8 | `Match` | Quantified data size |
| 15 | 2022-Hate-speech-CNERG-Kannada Code-Mixed Abusive Speech Detection MuRIL-based | 7.8 | `Match` | Quantified data size |
| 16 | 2022-Hu-“I’m sorry to hear that” | 7.8 | `Match` | Quantified data size |
| 17 | 2023-Deng-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass | 7.8 | `Match` | Clear eval metrics |
| 18 | 2023-Gustafson-FACET | 7.8 | `Match` | Code/repo available |
| 19 | 2023-Haq-NLPashto NLP Toolkit for Low-resource Pashto Language | 7.8 | `Match` | Quantified data size |
| 20 | 2023-Moss-Bias on Demand | 7.8 | `Match` | Quantified data size |
| 21 | 2023-Muhammad-AfriSenti | 7.8 | `Match` | Quantified data size |
| 22 | 2023-Nguyen-PhoGPT Generative Pre-training for Vietnamese | 7.8 | `Match` | Quantified data size |
| 23 | 2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew | 7.8 | `Match` | Quantified data size |
| 24 | 2024-Aakanksha-The Multilingual Alignment Prism | 7.8 | `Match` | Code/repo available |
| 25 | 2024-Bayat-FactBench | 7.8 | `Match` | Code/repo available |
| 26 | 2024-Bertram-Comparative Survey of German Hate Speech Datasets Background | 7.8 | `Match` | Quantified data size |
| 27 | 2024-Debenedetti-SaTML LLM CTF Dataset | 7.8 | `Match` | Clear eval metrics |
| 28 | 2024-Defrance-ABCFair | 7.8 | `Match` | Quantified data size, LLM evaluation exists |
| 29 | 2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural | 7.8 | `Match` | Quantified data size |
| 30 | 2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After | 7.8 | `Match` | Code/repo available |
| 31 | 2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling | 7.8 | `Match` | LLM evaluation exists |
| 32 | 2024-Liu-Cultural Bias and Cultural Alignment of Large Language Models | 7.8 | `Match` | Code/repo available |
| 33 | 2024-Masood-AL-QASIDA Analyzing LLM Quality and Accuracy Systematically in | 7.8 | `Match` | Code/repo available |
| 34 | 2024-Murtala-A multilingual dataset for offensive language | 7.8 | `Match` | LLM evaluation exists |
| 35 | 2024-Senthilkumar-Fine-Tuning Language Models for Ethical Ambiguity | 7.8 | `Match` | Code/repo available |
| 36 | 2024-Shen-EmpathicStories++ A Multimodal Dataset for Empathy towards Personal | 7.8 | `Match` | Code/repo available |
| 37 | 2024-team-SeaLLMs 3 Open Foundation and Chat Multilingual Large Language Models | 7.8 | `Match` | Quantified data size |
| 38 | 2024-with.pdf-Hate Speech Detection in Low-Resource Bodo and Assamese Texts with | 7.8 | `Match` | Quantified data size |
| 39 | 2025-Beauchemin-QFrCoLA a Quebec-French Corpus of Linguistic Acceptability Judgments | 7.8 | `Match` | Quantified data size |
| 40 | 2025-Bengoetxea-Lost in Variation Evaluating NLI Performance in Basque and Spanish | 7.8 | `Match` | Code/repo available |
| 41 | 2025-Buyl-AI Alignment at Your Discretion | 7.8 | `Match` | Code/repo available |
| 42 | 2025-Dementieva-TextDetox Multilingual Toxicity Dataset | 7.8 | `Match` | LLM evaluation exists |
| 43 | 2025-Fan-LEXam | 7.8 | `Match` | Code/repo available |
| 44 | 2025-Fillies-Mapping Toxic Comments Across Demographics A Dataset from German | 7.8 | `Match` | Clear eval metrics |
| 45 | 2025-Galea-From Measurement to Mitigation Exploring the Transferability of | 7.8 | `Match` | Quantified data size |
| 46 | 2025-Herrera-A Dataset for Investigating Tagalog-English Code-Switching | 7.8 | `Match` | Quantified data size |
| 47 | 2025-Kumar-SweEval Do LLMs Really Swear A | 7.8 | `Match` | Code/repo available |
| 48 | 2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from | 7.8 | `Match` | Code/repo available |
| 49 | 2025-Miranda-FilBench Can LLMs Understand and Generate Filipino | 7.8 | `Match` | Code/repo available |
| 50 | 2025-Naous-On The Origin of Cultural Biases in Language Models From Pre-training | 7.8 | `Match` | Quantified data size |
| | *... and 822 more* | | | |

## 3. Barriers (2.0-5.0)

306 papers have significant gaps to fill.

## 4. Not Implementable (< 2.0)

82 papers are theoretical or lack any benchmark/dataset.

## 5. Template Distribution

OpenAI Evals template types mapped to papers:

| Template | Count | % | Description |
|----------|-------|---|-------------|
| `Match` | 1479 | 72.4% | Exact string match (MCQ, classification) |
| `unknown` | 284 | 13.9% | No clear task structure identified |
| `ModelBasedClassify` | 245 | 12.0% | LLM-graded with rubric (ethics, open-ended) |
| `FuzzyMatch` | 35 | 1.7% | Approximate match (QA with minor variations) |

### Template x Tier

| Template | Ready | Possible | Barriers | Not Implementable |
|----------|---|---|---|---|
| `FuzzyMatch` | 17 | 18 | 0 | 0 |
| `Match` | 743 | 646 | 90 | 0 |
| `ModelBasedClassify` | 23 | 130 | 91 | 1 |
| `unknown` | 0 | 78 | 125 | 81 |

## Score Distribution

| Score | Count | Bar |
|-------|-------|-----|
| 10.0-10.9 | 84 | ################ |
| 9.0-9.9 | 254 | ################################################## |
| 8.0-8.9 | 445 | ######################################################################################### |
| 7.0-7.9 | 371 | ########################################################################## |
| 6.0-6.9 | 311 | ############################################################## |
| 5.0-5.9 | 190 | ###################################### |
| 4.0-4.9 | 154 | ############################## |
| 3.0-3.9 | 94 | ################## |
| 2.0-2.9 | 58 | ########### |
| 1.0-1.9 | 82 | ################ |
| 0.0-0.9 | 0 |  |

## Most Common Missing Dimensions

| Dimension | Papers Missing | % |
|-----------|---------------|---|
| Code/repo available | 1024 | 50.1% |
| Data publicly available | 809 | 39.6% |
| Quantified data size | 793 | 38.8% |
| LLM evaluation exists | 464 | 22.7% |
| Eval template mappable | 371 | 18.2% |
| Dataset exists | 319 | 15.6% |
| Clear eval metrics | 253 | 12.4% |
| JSONL-convertible format | 126 | 6.2% |

## Top 30 Most Implementable Papers

| # | Paper | Score | Tier | Template | Missing |
|---|-------|-------|------|----------|---------|
| 1 | 2022-Bai-Training a Helpful and Harmless Assistant with | **10.0** | Ready | `Match` | 0 |
| 2 | 2022-Liang-Holistic Evaluation of Language Models | **10.0** | Ready | `Match` | 0 |
| 3 | 2022-Parrish-BBQ Bias Benchmark for Question Answering | **10.0** | Ready | `Match` | 0 |
| 4 | 2022-Parrish-BBQ | **10.0** | Ready | `Match` | 0 |
| 5 | 2022-Taktasheva-TAPE Assessing Few-shot Russian Language Understanding | **10.0** | Ready | `Match` | 0 |
| 6 | 2023-Huang-Flames | **10.0** | Ready | `Match` | 0 |
| 7 | 2023-Liu-AlignBench | **10.0** | Ready | `Match` | 0 |
| 8 | 2023-Santurkar-Whose Opinions Do Language Models Reflect | **10.0** | Ready | `Match` | 0 |
| 9 | 2023-Shen-“Do Anything Now” | **10.0** | Ready | `Match` | 0 |
| 10 | 2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models | **10.0** | Ready | `Match` | 0 |
| 11 | 2023-Wang-DecodingTrust | **10.0** | Ready | `Match` | 0 |
| 12 | 2023-Wang-STREAM | **10.0** | Ready | `Match` | 0 |
| 13 | 2023-Wang-SeaEval for Multilingual Foundation Models From Cross-Lingual | **10.0** | Ready | `Match` | 0 |
| 14 | 2023-Xu-CValues | **10.0** | Ready | `Match` | 0 |
| 15 | 2024-Acikgoz-Bridging the Bosphorus Advancing Turkish Large Language Models | **10.0** | Ready | `Match` | 0 |
| 16 | 2024-Ashraf-Arabic Dataset for LLM Safeguard Evaluation | **10.0** | Ready | `Match` | 0 |
| 17 | 2024-Bandarkar-The Belebele Benchmark a Parallel Reading Comprehension Dataset in | **10.0** | Ready | `Match` | 0 |
| 18 | 2024-Bang-BLEnD A Benchmark for LLMs on | **10.0** | Ready | `FuzzyMatch` | 0 |
| 19 | 2024-Chen-Measuring Taiwanese Mandarin Language Understanding TMLU | **10.0** | Ready | `Match` | 0 |
| 20 | 2024-Chern-BeHonest | **10.0** | Ready | `Match` | 0 |
| 21 | 2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation | **10.0** | Ready | `Match` | 0 |
| 22 | 2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque | **10.0** | Ready | `Match` | 0 |
| 23 | 2024-Faisal-DialectBench A NLP Benchmark for Dialects Varieties and | **10.0** | Ready | `Match` | 0 |
| 24 | 2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model | **10.0** | Ready | `Match` | 0 |
| 25 | 2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian | **10.0** | Ready | `Match` | 0 |
| 26 | 2024-Guldimann-COMPL-AI EU AI Act Compliance | **10.0** | Ready | `Match` | 0 |
| 27 | 2024-Gupta-WalledEval | **10.0** | Ready | `Match` | 0 |
| 28 | 2024-Han-MedSafetyBench | **10.0** | Ready | `Match` | 0 |
| 29 | 2024-Huang-CBBQ | **10.0** | Ready | `Match` | 0 |
| 30 | 2024-Huang-TrustLLM | **10.0** | Ready | `Match` | 0 |

## Year x Tier Breakdown

| Year | Ready | Possible | Barriers | Not Implementable | Total |
|------|---|---|---|---|-------|
| 0000 | 0 | 3 | 0 | 0 | 3 |
| 2010 | 0 | 0 | 1 | 0 | 1 |
| 2012 | 0 | 0 | 2 | 0 | 2 |
| 2013 | 0 | 0 | 0 | 1 | 1 |
| 2014 | 0 | 0 | 0 | 1 | 1 |
| 2015 | 0 | 1 | 0 | 0 | 1 |
| 2016 | 0 | 3 | 4 | 0 | 7 |
| 2018 | 7 | 9 | 4 | 1 | 21 |
| 2019 | 7 | 14 | 4 | 1 | 26 |
| 2020 | 17 | 13 | 14 | 6 | 50 |
| 2021 | 24 | 25 | 6 | 6 | 61 |
| 2022 | 48 | 29 | 19 | 2 | 98 |
| 2023 | 85 | 87 | 27 | 8 | 207 |
| 2024 | 246 | 221 | 76 | 19 | 562 |
| 2025 | 333 | 430 | 138 | 37 | 938 |
| 2026 | 16 | 37 | 11 | 0 | 64 |

## Cross-Reference: OpenAI Evals vs lm-eval / lighteval

### vs lm-eval-harness

| lm-eval Tier | Ready | Possible | Barriers | Not Implementable |
|-------------|---|---|---|---|
| ? | 12 | 26 | 13 | 2 |
| ALREADY_IN_HARNESS | 43 | 20 | 1 | 1 |
| NEEDS_DATASET_HOSTING | 239 | 157 | 16 | 1 |
| NEEDS_MORE_INFO | 258 | 270 | 51 | 1 |
| NOT_IMPLEMENTABLE | 86 | 368 | 223 | 77 |
| READY_TO_IMPLEMENT | 145 | 31 | 2 | 0 |

### vs lighteval

| lighteval Tier | Ready | Possible | Barriers | Not Implementable |
|---------------|---|---|---|---|
| ? | 12 | 26 | 13 | 2 |
| Barriers | 192 | 515 | 181 | 15 |
| Not Implementable | 5 | 63 | 84 | 65 |
| Possible | 492 | 251 | 28 | 0 |
| Ready | 82 | 17 | 0 | 0 |

---
*Generated by `generate_openai_evals_report.py` on 2026-03-12*
