---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0528
type: preprint
short_title: "Meltemi: The first open Large Language Model for Greek"
year: 2024
first_author: "[[Leon Voukoutis]]"
last_author: "[[Vassilis Katsouros]]"
authors: "Leon Voukoutis; Dimitris Roussis; Georgios Paraskevopoulos; Sokratis Sofianopoulos; Prokopis Prokopidis; Vassilis Papavasileiou; Athanasios Katsamanis; Stelios Piperidis; Vassilis Katsouros"
url: "https://arxiv.org/abs/2407.20743"
external_pdf: "https://arxiv.org/pdf/2407.20743.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2024/2024-Voukoutis-Meltemi The first open Large Language Model for Greek.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Voukoutis-Meltemi The first open Large Language Model for Greek.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Greek
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: Mistral
DATA_URL: "https://huggingface.co/ilsp/Meltemi-7B-v1"
tags: 
abstract: "We describe the development and capabilities of Meltemi 7B, the ﬁrst open Large Language Model for the Greek language. Meltemi 7B has 7 billion parameters and is trained on a 40 billion token Greek corpus. For the development of Meltemi 7B, we adapt Mistral, by continuous pretraining on the Greek Corpus. Meltemi 7B contains upto-date information up to September 2023. Furthermore, we have translated and curated a Greek instruction corpus, which has been used for the instruction-tuning of a chat..."
ethics_perspective: "AI Safety & Alignment"
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "NLP & Representation Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: GR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 69
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
---
# Meltemi: The first open Large Language Model for Greek

## Authors

[[Leon Voukoutis]], [[Dimitris Roussis]], [[Georgios Paraskevopoulos]], [[Sokratis Sofianopoulos]], [[Prokopis Prokopidis]], [[Vassilis Papavasileiou]], [[Athanasios Katsamanis]], [[Stelios Piperidis]], [[Vassilis Katsouros]]

## Metadata

**Authors:** Leon Voukoutis, Dimitris Roussis, Georgios Paraskevopoulos, Sokratis Sofianopoulos, Prokopis Prokopidis, Vassilis Papavasileiou, Athanasios Katsamanis, Stelios Piperidis, Vassilis Katsouros

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

**Benchmark:** Meltemi Greek Benchmark Suite

## Links

- **arXiv:** https://arxiv.org/abs/2407.20743
- **Code/Data:** https://huggingface.co/ilsp/Meltemi-7B-v1

## Abstract

The first open LLM for Greek, built on Mistral-7B with continual pretraining on 40B Greek tokens. Includes a comprehensive evaluation suite with Greek versions of ARC, TruthfulQA, HellaSwag, MMLU, Belebele, and a novel Medical MCQA benchmark. Meltemi-7B shows +20.2% average improvement across all Greek test sets.

## Summary

This paper introduces Meltemi 7B and Meltemi 7B Instruct, the first open large language models specifically developed for the Greek language. The authors adapt Mistral-7B through continuous pretraining on a 40-billion-token Greek corpus from diverse sources (Wikipedia, ELRC-SHARE, EUR-LEX, academic repositories, CulturaX), extending the tokenizer with Greek tokens and using a mixed Greek-English data approach to prevent catastrophic forgetting. The instruction-tuned version (Meltemi 7B Instruct) is created using translated preference data with the ORPO algorithm, with special attention to alignment and toxic content removal. Evaluation on a comprehensive Greek benchmark suite (translated versions of ARC, TruthfulQA, HellaSwag, MMLU, Belebele, plus a novel Medical MCQA) shows Meltemi achieving a 20.2% average improvement across all Greek test sets. Both models are released under Apache 2.0 license.

## Data Description

Meltemi is the first open LLM for Greek, built on Mistral-7B with continual pretraining on 40B Greek tokens. Includes a comprehensive evaluation suite with Greek versions of ARC, TruthfulQA, HellaSwag, MMLU, Belebele, and a novel Medical MCQA benchmark. Meltemi-7B shows +20.2% average improvement across all Greek test sets.


## Detailed Summary

This paper describes the development of Meltemi 7B and Meltemi 7B Instruct, the first open Large Language Models for the Greek language. Meltemi 7B is created by continuously pre-training Mistral-7B on a high-quality 54.5 billion token corpus comprising Greek monolingual text (79.5%), English text (19.3%), and parallel English-Greek translation data (1.2%). The training pipeline involves extending the Mistral tokenizer from 32,000 to 61,362 tokens to dramatically improve Greek text fertility (from 6.80 tokens/word to 1.52), a two-stage training procedure (frozen embedding training followed by full model training on 8x NVIDIA H100 GPUs), and instruction tuning using ORPO with translated Greek preference data (89,730 Greek + 7,342 English preference triplets). Special attention is given to alignment and toxic content removal for the instruct version. The work also initiates discussion of environmentally and economically sustainable LLM deployment.

## Paper Outline

1. Introduction - Need for open Greek LLMs
2. Our Method - Overview of the development pipeline
   2.1 Pretraining Data - Greek monolingual, English, and parallel corpus creation
   2.2 Tokenizer and Embeddings Expansion - Extending Mistral tokenizer for Greek
   2.3 Foundation Model Training - Two-stage pre-training procedure
   2.4 Instruction Tuning - ORPO with translated preference data
   2.5 Evaluation - Greek benchmark suite
3. Discussion and Conclusions - Results, sustainability considerations

## Methods Summary

The pretraining corpus is assembled from diverse sources: Greek Wikipedia, ELRC-SHARE, EUR-LEX/MultiEUR-LEX, MaCoCu, CLARIN-EL, parliamentary proceedings, academic repositories, and CulturaX. Extensive preprocessing includes blacklisted URL removal, PDF artifact cleaning, document-level filtering, Monocleaner fluency scoring, LASER-based parallel corpus filtering, and MinHashLSH near-deduplication (both intra- and cross-dataset). The tokenizer is expanded from 32k to 61k tokens using a method that initializes new embeddings from average sub-token embeddings. Training uses DeepSpeed Zero on H100 GPUs with re-warming and re-decaying learning rate strategy to mitigate catastrophic forgetting. ORPO (Odds Ratio Preference Optimization) is used for instruction tuning with 97,072 curated preference data.

## Results Summary

Meltemi-7B achieves a +20.2% average improvement across all Greek test sets compared to the base Mistral-7B, with a moderate 6% drop on English benchmarks. On specific tasks: ARC-C Greek improves from 27.2% to 47.2%, HellaSwag Greek from 35.2% to 65.8%, MMLU Greek from 28.4% to 42.5%, and Belebele (Greek) from 35.8% to 68.7%. The Meltemi-7B-Instruct version further improves on several tasks, achieving 54.6% average on Greek benchmarks and 57.7% on English benchmarks. The tokenizer extension reduces Greek fertility from 6.80 to 1.52 tokens per word, achieving near-parity with English (1.44), resulting in significant computational savings. Energy consumption for the entire development was approximately 2,300 kWh.

## Conclusions

Meltemi demonstrates that continuous pre-training is an effective strategy for extending existing LLMs to new languages while partially preserving English capabilities. The work argues for open-source LLMs for mid and low-resource languages that account for cultural aspects, local laws, and customs. Both models are released under Apache 2.0 license, and the authors acknowledge the significant economic and environmental investment required, motivating future research on efficient model adaptation techniques and exploration of larger models and multimodality.

## Artifact Contributions

- **Meltemi 7B**: First open Greek foundation model (Apache 2.0 license, available at https://huggingface.co/ilsp/)
- **Meltemi 7B Instruct**: Aligned chat model with toxic content removal
- **Greek benchmark suite**: Translated and curated evaluation corpora including ARC, TruthfulQA, HellaSwag, MMLU (Greek), Belebele, and novel Greek Medical MCQA
- **Greek tokenizer**: Extended tokenizer with 61,362 tokens achieving near-English fertility
- **Sustainability discussion**: Documentation of 2,300 kWh energy consumption

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** First open Greek LLM with dedicated evaluation benchmarks including translated safety benchmarks (TruthfulQA). Special care for alignment and toxic content removal in instruct version. Relevant to Greek cultural and domain-specific knowledge evaluation.

## Tags

