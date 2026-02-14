---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0481
type: preprint
short_title: "NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark"
year: 2025
first_author: [[Various]]
last_author: [[Various]]
authors: Various
url: "https://arxiv.org/abs/2504.07749"
external_pdf: "https://arxiv.org/pdf/2504.07749.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Various-NorEval A Norwegian Language Understanding and Generation Evaluation.md"
local_pdf: "[[PDFs/2025/2025-Various-NorEval A Norwegian Language Understanding and Generation Evaluation.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: Norwegian
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: NA
DATA_URL: NA
tags: 
abstract: "This paper introduces NorEval, a new and comprehensive evaluation suite for large-scale standardized benchmarking of Norwegian generative language models (LMs). NorEval consists of 24 high-quality human-created datasets – of which five are created from scratch. In contrast to existing benchmarks for Norwegian, NorEval covers a broad spectrum of task categories targeting Norwegian language understanding and generation, establishes human baselines, and focuses on both of the official written..."
research_topic: "Machine Learning"
---
# NorEval: A Norwegian Language Understanding and Generation Evaluation Benchmark

## Authors

[[Various]]

## Metadata

**Authors:** Various

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Norwegian

**Benchmark:** NorEval

## Links

- **arXiv:** https://arxiv.org/abs/2504.07749

## Abstract

Comprehensive evaluation suite with 24 high-quality human-created datasets for Norwegian generative LMs, of which 5 are new. Designed for large-scale standardized benchmarking of Norwegian LLMs.

## Summary

This paper introduces NorEval, a comprehensive evaluation suite for standardized benchmarking of Norwegian generative language models comprising 24 high-quality human-created datasets across nine task categories, with five datasets newly created from scratch. Covering both official Norwegian written standards (Bokmål and Nynorsk), NorEval addresses gaps in existing benchmarks through its broad task coverage, exclusive use of human-created data (avoiding machine translations), and establishment of human performance baselines. The benchmark evaluates 19 open-source pretrained and instruction-tuned LMs across tasks including sentiment analysis, Norwegian language knowledge, reading comprehension, commonsense reasoning, machine translation, and instruction following.

## Data Description

Introduces NorEval, a comprehensive evaluation suite with 24 high-quality human-created datasets (5 newly created) for standardized benchmarking of Norwegian generative language models across language understanding and generation tasks. Paper focuses on benchmark creation rather than specific model evaluations.


## Detailed Summary

This paper introduces NorEval, the largest and most comprehensive multi-task evaluation benchmark for Norwegian language models, comprising 24 high-quality human-created datasets across nine task categories -- of which five datasets are newly created from scratch. NorEval addresses four critical shortcomings of existing Norwegian benchmarks (NorBench, ScandEval, SEB, NLEBench): limited dataset overlap with low task variation, inclusion of machine-translated English datasets that introduce evaluation biases conflicting with Norwegian cultural values, underrepresentation of Nynorsk (the minority written standard), and absence of human performance baselines. The benchmark covers 16 datasets in Bokmal and 8 in Nynorsk, integrated into the LM Evaluation Harness framework for flexible and reproducible evaluation. Task categories include sentiment analysis, Norwegian language knowledge, Norwegian-specific and world knowledge, machine reading comprehension, commonsense reasoning, machine translation, text summarization, instruction following, and truthfulness. The authors benchmark 19 open-source pretrained and instruction-tuned LMs across various evaluation scenarios.

## Paper Outline

1. Introduction - Shortcomings of existing Norwegian benchmarks and motivation for NorEval
2. NorEval Design - Task categories, dataset selection, and new dataset creation
3. Existing Datasets - Description of 19 incorporated peer-reviewed datasets
4. New Datasets - Five datasets created from scratch with human baselines
5. Evaluation Framework - Integration with LM Evaluation Harness; prompt design
6. Experiments - Multi-prompt k-shot evaluation; side-by-side model comparison
7. Results - Benchmarking of 19 open-source LMs
8. Discussion and Conclusion

## Methods Summary

NorEval combines 19 existing peer-reviewed Norwegian datasets with five newly created datasets, all human-created to avoid machine-translation artifacts. The benchmark is integrated into the LM Evaluation Harness framework with over 100 dataset-specific human-written prompts for robust evaluation. Human baselines are established for the five new datasets. Evaluation scenarios range from multi-prompt k-shot evaluation to side-by-side LM comparison on diverse user instructions. The design follows principles of quality control, linguistic diversity (both Bokmal and Nynorsk), and comprehensive task coverage across language understanding and generation.

## Results Summary

The benchmark evaluates 19 open-source pretrained and instruction-tuned LMs for Norwegian, revealing performance patterns across task categories and written standards. NorEval significantly expands evaluation coverage compared to existing benchmarks: NorBench covers 10 datasets, ScandEval 10, SEB 14, and NLEBench 9, while NorEval provides 24 datasets with the broadest task category coverage. The inclusion of human baselines allows meaningful interpretation of model performance gaps.

## Conclusions

NorEval establishes a new standard for Norwegian LM evaluation, addressing critical gaps in existing benchmarks through comprehensive task coverage, exclusive use of human-created data, coverage of both Norwegian written standards, and human performance baselines. The publicly available benchmark, evaluation framework, and annotation materials provide the community with essential tools for systematic Norwegian LM development and comparison.

## Artifact Contributions

- **Benchmark:** NorEval - 24-dataset evaluation suite for Norwegian LMs (16 Bokmal, 8 Nynorsk)
- **Datasets:** 5 newly created Norwegian datasets with human baselines
- **Evaluation Framework:** 100+ human-written prompts integrated into LM Evaluation Harness
- **Annotation Materials:** Publicly available for reproducible evaluation

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Most recent comprehensive Norwegian LLM evaluation benchmark.

## Tags

