---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0293
type: preprint
short_title: "TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction"
year: 2026
first_author: "[[Nadas, Mihai Dan]]"
last_author: "[[Piscoran, Andrei]]"
authors: "Nadas, Mihai Dan; Diosan, Laura; Tomescu, Andreea; Piscoran, Andrei"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.10410"
external_pdf: "https://arxiv.org/pdf/2601.10410.pdf"
pdf_extract: "PDF Extracts/2026/2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Romanian
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
tags: 
abstract: "Recent advances in synthetic data generation have shown that compact language models can be trained effectively when the underlying corpus is structurally controlled and linguistically coherent. However, for morphologically rich and computationally under-resourced languages such as Romanian, there is still no openly documented, end-to-end pipeline that unifies tokenizer design, preprocessing, pretraining, compression, evaluation, and large-scale synthetic data generation in a reproducible..."
LLM_assessed: "BERT, Gemma-2, GPT-4, LLaMA, Llama-3"
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: 20
virtue_ethics: 0
deontological_ethics: 15
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: RO
author_region: "Eastern Europe & Central Asia"
author_global_north_south: Ambiguous
weird_score: 42
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
---
# TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction

## Authors

[[Nadas, Mihai Dan]], [[Diosan, Laura]], [[Tomescu, Andreea]], [[Piscoran, Andrei]]

## Metadata

**Authors:** Nadas, Mihai Dan; Diosan, Laura; Tomescu, Andreea; Piscoran, Andrei

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2601.10410

## Abstract

Recent advances in synthetic data generation have shown that compact language models can be trained effectively when the underlying corpus is structurally controlled and linguistically coherent. However, for morphologically rich and computationally under-resourced languages such as Romanian, there is still no openly documented, end-to-end pipeline that unifies tokenizer design, preprocessing, pretraining, compression, evaluation, and large-scale synthetic data generation in a reproducible framework. Building on TF1, a three-million-story English fable dataset, and TF2, which extends TF1 through high-quality Romanian translations, we introduce TF3-RO: a Romanian-centric language modeling pipeline that spans tokenizer training, from-scratch model development, and Romaniannative dataset generation. TF3-RO constructs Romanian-specific BPE and Unigram tokenizers from a linguistically informed corpus, mitigating the severe token inflation induced by Romanian morphology. Using long-sequence packed training, we pretrain a 51.65M-parameter LLaMA-style Transformer entirely from scratch. The model is subsequently optimized through quantization, structured pruning, and logit-based knowledge distillation, yielding a compact 26.45M-parameter student model with tied embeddings and strong deployment characteristics. Using this distilled model, TF3-RO generates a new dataset of three million Romanian-native synthetic fables via a controlled combinatorial prompting framework. Across all stages, the pipeline integrates a comprehensive evaluation suite combining intrinsic modeling metrics, Romanian agreement probes, entropy-based entity coherence, rule-based grammar checking, and LLM-as-a-judge assessment. TF3-RO thus provides a reproducible and linguistically grounded framework for training compact Romanian language models and for producing large-scale synthetic narrative corpora, with all artifacts released to support future research in Romanian NLP.

## Dataset Information

3M Romanian synthetic fables + 3M English fables with six-slot scaffold for narrative-based moral training

## Data Description

TF3-RO generates a new dataset of 3 million Romanian-native synthetic moral fables via a controlled combinatorial prompting framework; also releases a Romanian BERT-based NER dataset. All artifacts stated to be released under permissive licenses; predecessor TF2 dataset is at HuggingFace (ds-tf2-en-ro-3m) but no specific TF3 URL given.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** LOW

## Tags

