---

























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0492
type: preprint
short_title: "The Scandinavian Embedding Benchmarks: Comprehensive Assessment of Multilingual and Monolingual Text Embedding"
year: 2024
first_author: "[[Kenneth Enevoldsen]]"
last_author: "[[Kristoffer Laigaard Nielbo]]"
authors: Kenneth Enevoldsen; Marton Kardos; Niklas Muennighoff; Kristoffer Laigaard Nielbo
url: "https://arxiv.org/abs/2406.02396"
external_pdf: "https://arxiv.org/pdf/2406.02396.pdf"
publication: "arXiv / NeurIPS 2024"
CONF-CC: "NeurIPS 2024"
pdf_extract: "PDF Extracts/2024/2024-Enevoldsen-The Scandinavian Embedding Benchmarks Comprehensive Assessment of.md"
local_pdf: "[[PDFs/2024/2024-Enevoldsen-The Scandinavian Embedding Benchmarks Comprehensive Assessment of.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Scandinavian"
languages_list: "Danish, Norwegian, Swedish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "E5-multilingual, Sentence-T5, LaBSE, multilingual-e5, Scandinavian sentence encoders"
DATA_URL: "https://github.com/KennethEnevoldsen/scandinavian-embedding-benchmark"
tags: 
abstract: "The evaluation of English text embeddings has transitioned from evaluating a handful of datasets to broad coverage across many tasks through benchmarks such as MTEB. However, this is not the case for multilingual text embeddings due to a lack of available benchmarks. To address this problem, we introduce the Scandinavian Embedding Benchmark (SEB). SEB is a comprehensive framework that enables text embedding evaluation for Scandinavian languages across 24 tasks, 10 subtasks, and 4 task categories."
CONFERENCE: "NeurIPS 2024"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Translation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# The Scandinavian Embedding Benchmarks: Comprehensive Assessment of Multilingual and Monolingual Text Embedding

## Authors

[[Kenneth Enevoldsen]], [[Marton Kardos]], [[Niklas Muennighoff]], [[Kristoffer Laigaard Nielbo]]

## Metadata

**Authors:** Kenneth Enevoldsen, Marton Kardos, Niklas Muennighoff, Kristoffer Laigaard Nielbo

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / NeurIPS 2024

**Languages:** Danish, Norwegian, Swedish

**Benchmark:** SEB (Scandinavian Embedding Benchmark)

## Links

- **arXiv:** https://arxiv.org/abs/2406.02396

## Abstract

Comprehensive text embedding evaluation framework for Scandinavian languages across 24 tasks, 10 subtasks, and 4 task categories. Evaluates 26+ models, uncovering significant performance disparities between public and commercial solutions.

## Summary

This paper introduces the Scandinavian Embedding Benchmark (SEB), a comprehensive framework for evaluating text embeddings across Scandinavian languages (Danish, Norwegian, Swedish, Icelandic, Faroese, and Norwegian Nynorsk). The benchmark encompasses 24 tasks, 10 subtasks, and 4 task categories including classification, retrieval, semantic similarity, and clustering, addressing the lack of multilingual benchmarks beyond English. The authors evaluate 26+ models including E5-multilingual, Sentence-T5, LaBSE, and various Scandinavian sentence encoders, uncovering significant performance disparities between public and commercial embedding solutions. Published at NeurIPS 2024, SEB enables the transition from evaluating a handful of datasets to broad task coverage for Scandinavian text embeddings, similar to how MTEB revolutionized English embedding evaluation.

## Data Description

Scandinavian Embedding Benchmark (SEB) evaluating sentence embeddings across 6 Scandinavian languages (Danish, Swedish, Norwegian, Icelandic, Faroese, Norwegian Nynorsk) on 24 diverse tasks including classification, retrieval, and semantic similarity.


## Detailed Summary

This paper introduces the Scandinavian Embedding Benchmark (SEB), a comprehensive framework for evaluating text embeddings across Scandinavian languages, published at NeurIPS 2024 Datasets and Benchmarks track. SEB addresses the lack of multilingual embedding evaluation beyond English by covering Danish, Swedish, Norwegian (Bokmal and Nynorsk), and the Danish dialect Bornholmsk across 24 tasks, 10 subtasks, and 4 task categories (classification, retrieval, clustering, and bitext mining). The benchmark spans at least 12 domains including academic, news, fiction, government, legal, medical, and social media content, prioritizing naturally occurring Scandinavian text over translated datasets to maintain cultural integrity and avoid artificially inflating multilingual model performance. SEB builds upon and extends MTEB (Massive Text Embedding Benchmark) by including a model registry for reproducibility and porting all tasks to enable MTEB's expansion to a fully multilingual benchmark. The authors evaluate 26+ representative models including self-supervised encoders (BERT variants for Danish, Norwegian, Swedish, XLM-R), supervised methods (LaBSE, MiniLM, MPNet, E5-multilingual), and commercial APIs (OpenAI, Cohere, Voyage), revealing significant performance disparities not previously captured by English-centric benchmarks.

## Paper Outline

1. Introduction - Motivation for Scandinavian embedding evaluation, MTEB shortcomings
2. Related Work - Benchmarks (BEIR, MTEB, SentEval), text embedding development, Scandinavian NLP benchmarks
3. The Benchmark - Design rationale (coverage, cultural integrity, cross-lingual generalization, reproducibility), dataset descriptions
4. Methodology - Model selection, evaluation metrics, scoring approach
5. Results - Performance across task types, languages, model categories
6. Conclusion - Key findings and future directions

## Methods Summary

SEB follows MTEB's evaluation approach for computing scores while adding a model registry documenting exact implementation details for all evaluated models. Datasets are limited to maximum 2,048 examples to enable benchmarking on consumer-grade hardware. The benchmark leverages cross-lingual transfer between Mainland Scandinavian languages (demonstrated by Nielsen 2023) to broaden coverage. Models are grouped into self-supervised (BERT encoders, SimCSE, fastText) and supervised categories (LaBSE, MiniLM, MPNet, E5 variants, commercial APIs). Performance is reported with 95% confidence intervals obtained by bootstrapping 100 repetitions with tasks. An interactive online dashboard provides additional model evaluations beyond those in the paper.

## Results Summary

Significant performance disparities exist between public and commercial embedding solutions. Among evaluated models, commercial APIs (OpenAI, Cohere embed-multilingual-v3.0) and supervised multilingual models (E5-multilingual variants) generally outperform self-supervised and monolingual approaches. However, the rankings differ substantially from English MTEB results, demonstrating that English benchmark performance does not reliably predict Scandinavian performance. Monolingual Scandinavian BERT models show competitive classification performance but lag significantly in retrieval and clustering tasks. The benchmark reveals that bitext mining tasks, which dominate MTEB's multilingual coverage, are poor proxies for real-world Scandinavian embedding applications.

## Conclusions

SEB fills a critical evaluation gap for Scandinavian text embeddings, enabling informed decisions about model selection for Scandinavian applications. The benchmark demonstrates that relying on English or bitext mining performance as proxies for Scandinavian embedding quality leads to suboptimal model choices. Key limitations include the current exclusion of Icelandic and Faroese (Insular Scandinavian) due to limited resources, and the focus on static evaluation without accounting for computational cost. Future work includes expanding language coverage, adding more task types, and developing dedicated Scandinavian embedding models.

## Artifact Contributions

- **SEB Benchmark**: Comprehensive Scandinavian embedding evaluation framework with 24 tasks (https://github.com/KennethEnevoldsen/scandinavian-embedding-benchmark)
- **Interactive Dashboard**: Online model evaluation results (https://kennethenevoldsen.github.io/scandinavian-embedding-benchmark/)
- **MTEB Integration**: All SEB tasks ported to MTEB for multilingual expansion

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Primary Scandinavian text embedding benchmark covering Danish, Swedish, and Norwegian.

## Tags

