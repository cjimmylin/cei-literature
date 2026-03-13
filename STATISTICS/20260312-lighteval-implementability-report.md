# lighteval Implementability Report

**Generated:** 2026-03-12  
**Papers scored:** 1990  
**Average score:** 4.50/10.0  
**Scoring model:** 9-dimension weighted (HF presence = 2.0×)

## Executive Summary

| Tier | Score Range | Count | % |
|------|------------|-------|---|
| Ready | 8.0-10.0 | 99 | 5.0% |
| Possible | 5.0-7.9 | 771 | 38.7% |
| Barriers | 2.0-4.9 | 903 | 45.4% |
| Not Implementable | 0.0-1.9 | 217 | 10.9% |
| **Total** | | **1990** | |

## Score Distribution

| Score | Count | Bar |
|-------|-------|-----|
| 10.0–10.9 | 0 |  |
| 9.0–9.9 | 11 | ██ |
| 8.0–8.9 | 88 | █████████████████ |
| 7.0–7.9 | 153 | ██████████████████████████████ |
| 6.0–6.9 | 299 | ███████████████████████████████████████████████████████████ |
| 5.0–5.9 | 319 | ███████████████████████████████████████████████████████████████ |
| 4.0–4.9 | 331 | ██████████████████████████████████████████████████████████████████ |
| 3.0–3.9 | 293 | ██████████████████████████████████████████████████████████ |
| 2.0–2.9 | 279 | ███████████████████████████████████████████████████████ |
| 1.0–1.9 | 163 | ████████████████████████████████ |
| 0.0–0.9 | 54 | ██████████ |

## lighteval Task Types

| Type | Count | % |
|------|-------|---|
| `generate_until` | 870 | 43.7% |
| `unknown` | 829 | 41.7% |
| `multichoice` | 282 | 14.2% |
| `loglikelihood` | 9 | 0.5% |

## Most Common Missing Dimensions

| Dimension | Papers Missing | % |
|-----------|---------------|---|
| HuggingFace presence | 1606 | 80.7% |
| Code/repo available | 1469 | 73.8% |
| Quantified data size | 1206 | 60.6% |
| Clear eval metrics | 1097 | 55.1% |
| Task type identifiable | 785 | 39.4% |
| Dataset exists | 614 | 30.9% |
| Data publicly available | 384 | 19.3% |
| Full text available | 232 | 11.7% |
| LLM evaluation exists | 207 | 10.4% |

## Top 30 Most Implementable Papers

| # | Paper | Score | Tier | Task Type | Missing |
|---|-------|-------|------|-----------|---------|
| 1 | 2024-Chabot-Couture-Bridging the Gap Enhancing LLM Performance | **9.5** | Ready | `multichoice` | 0 |
| 2 | 2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque | **9.5** | Ready | `multichoice` | 0 |
| 3 | 2024-Montalan-Kalahi A handcrafted grassroots cultural LLM evaluation suite for | **9.5** | Ready | `multichoice` | 0 |
| 4 | 2025-Raza-HumaniBench | **9.5** | Ready | `multichoice` | 0 |
| 5 | 2024-Gupta-WalledEval | **9.25** | Ready | `generate_until` | 0 |
| 6 | 2024-Brun-FrenchToxicityPrompts a Large Benchmark for Evaluating and Mitigating | **9.0** | Ready | `generate_until` | 0 |
| 7 | 2024-Mahendra-SEACrowd A Multilingual Multimodal Data Hub | **9.0** | Ready | `generate_until` | 0 |
| 8 | 2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation | **9.0** | Ready | `generate_until` | 1 |
| 9 | 2024-Voukoutis-Meltemi The first open Large Language Model for Greek | **9.0** | Ready | `multichoice` | 1 |
| 10 | 2024-Yin-SafeWorld Geo-Diverse Safety Alignment | **9.0** | Ready | `generate_until` | 0 |
| 11 | 2025-Pandey-SocialHarmBench | **9.0** | Ready | `unknown` | 0 |
| 12 | 2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text | **8.75** | Ready | `generate_until` | 1 |
| 13 | 2023-Kahira-AfriQA Cross-lingual Open-Retrieval Question Answering for | **8.75** | Ready | `generate_until` | 0 |
| 14 | 2023-Li-ACLUE Can Large Language Model Comprehend | **8.75** | Ready | `multichoice` | 0 |
| 15 | 2023-Nguyen-PhoGPT Generative Pre-training for Vietnamese | **8.75** | Ready | `generate_until` | 0 |
| 16 | 2023-Shmidman-DictaBERT A State-of-the-Art BERT Suite for Modern Hebrew | **8.75** | Ready | `generate_until` | 0 |
| 17 | 2024-Choi-CaLMQA Exploring culturally specific long-form question | **8.75** | Ready | `multichoice` | 0 |
| 18 | 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation | **8.75** | Ready | `multichoice` | 0 |
| 19 | 2024-Kim-CLIcK A Benchmark Dataset of Cultural and Linguistic Intelligence in | **8.75** | Ready | `generate_until` | 0 |
| 20 | 2024-Nguyen-ViHateT5 Enhancing Hate Speech Detection in Vietnamese With A Unified | **8.75** | Ready | `generate_until` | 1 |
| 21 | 2024-Son-KMMLU Measuring Massive Multitask Language Understanding in Korean | **8.75** | Ready | `multichoice` | 0 |
| 22 | 2025-Chua-RabakBench | **8.75** | Ready | `generate_until` | 1 |
| 23 | 2025-Fiaz-UrduLLaMA 1.0 Dataset Curation Preprocessing and Evaluation in | **8.75** | Ready | `generate_until` | 0 |
| 24 | 2025-Kaewkasi-A Benchmark for Large Language Models on Northern | **8.75** | Ready | `multichoice` | 0 |
| 25 | 2025-Maheshwari-IndicParam Benchmark to Evaluate LLMs on | **8.75** | Ready | `multichoice` | 0 |
| 26 | 2025-Ruiz-Fernández-EsBBQ and CaBBQ | **8.75** | Ready | `multichoice` | 0 |
| 27 | 2021-Sun-LaoPLM Pre-trained Language Models for Lao | **8.5** | Ready | `generate_until` | 0 |
| 28 | 2023-Hamad-Offensive Hebrew Corpus and Detection using BERT | **8.5** | Ready | `generate_until` | 0 |
| 29 | 2024-Fajcik-BenCzechMark A Czech-centric Multitask and Multimetric Benchmark for | **8.5** | Ready | `multichoice` | 1 |
| 30 | 2024-Liu-JAILJUDGE | **8.5** | Ready | `unknown` | 1 |

## Year × Tier Breakdown

| Year | Ready | Possible | Barriers | Not Implementable | Total |
|------|---|---|---|---|-------|
| 0000 | 0 | 0 | 1 | 2 | 3 |
| 2010 | 0 | 0 | 0 | 1 | 1 |
| 2012 | 0 | 0 | 0 | 2 | 2 |
| 2013 | 0 | 0 | 0 | 1 | 1 |
| 2014 | 0 | 0 | 0 | 1 | 1 |
| 2015 | 0 | 0 | 0 | 1 | 1 |
| 2016 | 0 | 1 | 4 | 2 | 7 |
| 2018 | 0 | 3 | 16 | 1 | 20 |
| 2019 | 0 | 9 | 11 | 2 | 22 |
| 2020 | 2 | 11 | 25 | 9 | 47 |
| 2021 | 2 | 21 | 27 | 7 | 57 |
| 2022 | 3 | 40 | 44 | 5 | 92 |
| 2023 | 12 | 77 | 96 | 17 | 202 |
| 2024 | 48 | 225 | 220 | 54 | 547 |
| 2025 | 30 | 355 | 428 | 110 | 923 |
| 2026 | 2 | 29 | 31 | 2 | 64 |

## Comparison: lighteval vs lm-eval-harness Tiers

| lm-eval Tier | Ready | Possible | Barriers | Not Implementable |
|-------------|---|---|---|---|
| ALREADY_IN_HARNESS | 5 | 42 | 18 | 0 |
| NEEDS_DATASET_HOSTING | 34 | 306 | 73 | 0 |
| NEEDS_MORE_INFO | 17 | 240 | 310 | 13 |
| NOT_IMPLEMENTABLE | 1 | 53 | 496 | 204 |
| READY_TO_IMPLEMENT | 42 | 130 | 6 | 0 |

---
*Generated by `assemble_lighteval_report.py` on 2026-03-12*
