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
local_pdf: "[[PDFs/2026/2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Romanian"
languages_list: "Romanian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Recent advances in synthetic data generation have shown that compact language models can be trained effectively when the underlying corpus is structurally controlled and linguistically coherent. However, for morphologically rich and computationally under-resourced languages such as Romanian, there is still no openly documented, end-to-end pipeline that unifies tokenizer design, preprocessing, pretraining, compression, evaluation, and large-scale synthetic data generation in a reproducible..."
LLM_assessed: "ALBERT, BERT, DeepSeek, GPT-4, Gemma 2, Llama, Llama-3"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
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

TF3-RO presents an end-to-end pipeline for training compact Romanian language models on synthetic moral microfiction. The dataset consists of three million Romanian synthetic fables generated via a combinatorial prompting framework, built upon the TF2 bilingual corpus. A 51.65M-parameter LLaMA-style Transformer is trained from scratch on approximately one billion Romanian tokens and compressed via knowledge distillation into a 26.45M-parameter student model. The pipeline includes custom Romanian BPE and Unigram tokenizers optimized for Romanian morphology.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** LOW

## Tags

