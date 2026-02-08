---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0293
type: preprint
short_title: "TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction"
year: 2026
first_author: "[[S. Nadies]]"
authors: Nadies, S. et al.
url: "https://arxiv.org/abs/2601.10410"
external_pdf: "https://arxiv.org/pdf/2601.10410.pdf"
local_pdf: "[[PDFs/2026/2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Nadies-TF3-RO Training Compact Romanian Language Models on Synthetic Moral.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Recent advances in synthetic data generation have shown that compact language models can be trained effectively when the underlying corpus is structurally controlled and linguistically coherent. However, for morphologically rich and computationally under-resourced languages such as Romanian, there is still no openly documented, end-to-end pipeline that unifies tokenizer design, preprocessing, pretraining, compression, evaluation, and large-scale synthetic data generation in a reproducible..."
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
---
# TF3-RO: Training Compact Romanian Language Models on Synthetic Moral Microfiction

## Authors

[[Nadies, S. et al.]]

## Metadata

**Authors:** Nadies, S. et al.

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2601.10410

## Abstract

Recent advances in synthetic data generation have shown that compact language models can be trained effectively when the underlying corpus is structurally controlled and linguistically coherent. However, for morphologically rich and computationally under-resourced languages such as Romanian, there is still no openly documented, end-to-end pipeline that unifies tokenizer design, preprocessing, pretraining, compression, evaluation, and large-scale synthetic data generation in a reproducible framework. Building on TF1, a three-million-story English fable dataset, and TF2, which extends TF1 through high-quality Romanian translations, we introduce TF3-RO: a Romanian-centric language modeling pipeline that spans tokenizer training, from-scratch model development, and Romaniannative dataset generation. TF3-RO constructs Romanian-specific BPE and Unigram tokenizers from a linguistically informed corpus, mitigating the severe token inflation induced by Romanian morphology. Using long-sequence packed training, we pretrain a 51.65M-parameter LLaMA-style Transformer entirely from scratch. The model is subsequently optimized through quantization, structured pruning, and logit-based knowledge distillation, yielding a compact 26.45M-parameter student model with tied embeddings and strong deployment characteristics. Using this distilled model, TF3-RO generates a new dataset of three million Romanian-native synthetic fables via a controlled combinatorial prompting framework. Across all stages, the pipeline integrates a comprehensive evaluation suite combining intrinsic modeling metrics, Romanian agreement probes, entropy-based entity coherence, rule-based grammar checking, and LLM-as-a-judge assessment. TF3-RO thus provides a reproducible and linguistically grounded framework for training compact Romanian language models and for producing large-scale synthetic narrative corpora, with all artifacts released to support future research in Romanian NLP.

## Dataset Information

3M Romanian synthetic fables + 3M English fables with six-slot scaffold for narrative-based moral training

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** LOW

## Tags

