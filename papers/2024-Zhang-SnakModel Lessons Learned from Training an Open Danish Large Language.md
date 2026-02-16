---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0489
type: preprint
short_title: "SnakModel: Lessons Learned from Training an Open Danish Large Language Model"
year: 2024
first_author: "[[Mike Zhang]]"
last_author: "[[Rob van der Goot]]"
authors: "[[Mike Zhang]]; [[Max Müller-Eberstein]]; [[Elisa Bassignana]]; [[Rob van der Goot]]"
url: "https://arxiv.org/abs/2412.12956"
external_pdf: "https://arxiv.org/pdf/2412.12956.pdf"
publication: "arXiv / NoDaLiDa 2025"
pdf_extract: "PDF Extracts/2024/2024-Zhang-SnakModel Lessons Learned from Training an Open Danish Large Language.md"
local_pdf: "[[PDFs/2024/2024-Zhang-SnakModel Lessons Learned from Training an Open Danish Large Language.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Danish"
languages_list: Danish
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "SnakModel (Llama2-7B-based), other Llama2-7B-based Danish models"
DATA_URL: "https://github.com/NVIDIA/Megatron-LM"
tags: 
abstract: "We present SNAKMODEL, a Danish large language model (LLM) based on LLAMA2-7B, which we continuously pre-train on 13.6B Danish words, and further tune on 3.7M Danish instructions. As best practices for creating LLMs for smaller language communities have yet to be established, we examine the effects of early modeling and training decisions on downstream performance throughout the entire training pipeline, including (1) the creation of a strictly curated corpus of Danish text from diverse sources;..."
authors_incomplete: false
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "NLP & Representation Learning"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "8 language"
---
# SnakModel: Lessons Learned from Training an Open Danish Large Language Model

## Authors

[[Mike Zhang]], [[Max Müller-Eberstein]], [[Elisa Bassignana]], [[Rob van der Goot]]

## Metadata

**Authors:** Mike Zhang, Max Müller-Eberstein, Elisa Bassignana, Rob van der Goot

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / NoDaLiDa 2025

**Languages:** Danish

## Links

- **arXiv:** https://arxiv.org/abs/2412.12956

## Abstract

Danish LLM based on Llama2-7B continuously pre-trained on 13.6B Danish words, tuned on 3.7M Danish instructions. Evaluated on 8 language and culturally-specific tasks. Achieves highest overall performance among Llama2-7B-based models.

## Summary

This paper presents SnakModel, an open Danish large language model based on Llama2-7B, along with comprehensive analysis of training decisions throughout the entire development pipeline. The authors continuously pre-train Llama2-7B on a strictly curated corpus of 13.6 billion Danish words from diverse sources (350M documents), then instruction-tune on 3.7 million Danish instruction-answer pairs. Through detailed examination of data curation, training dynamics, hyperparameter ablations, and evaluation on eight language and culturally-specific tasks from the ScandEval benchmark, SnakModel achieves the highest overall performance among contemporary Llama2-7B-based Danish models. By releasing the model, pre-training corpus, code, and intermediate checkpoints under open licenses, the work establishes training guidelines for languages with similar resource constraints.

## Data Description

SnakModel is a Danish LLM based on Llama2-7B, continuously pre-trained on 13.6B Danish words and tuned on 3.7M Danish instructions. Evaluated on 8 language and culturally-specific tasks. Achieves highest overall performance among Llama2-7B-based models for Danish.


## Detailed Summary

This paper presents SnakModel, an open Danish large language model based on Llama2-7B, developed through continuous pre-training on 13.6 billion Danish words from a strictly curated corpus of 350 million documents sourced from diverse origins. The model is further instruction-tuned on 3.7 million Danish instruction-answer pairs. The work provides a comprehensive examination of early modeling and training decisions throughout the entire development pipeline, establishing training guidelines for languages with similar resource constraints to Danish. Through detailed analysis of data curation, training dynamics, and hyperparameter ablations, the authors demonstrate that careful attention to each stage of the pipeline is essential for achieving strong performance in low-resource language settings.

## Paper Outline

1. Introduction - Motivation for Danish-specific LLM development
2. Data Creation - Curating a 13.6B-word Danish corpus from diverse sources
3. Continuous Pre-training - Adapting Llama2-7B for Danish
4. Instruction Tuning - Creating 3.7M Danish instruction-answer pairs
5. Evaluation - Performance on 8 Danish-specific tasks from ScandEval
6. Analysis - Training dynamics, hyperparameter ablations
7. Conclusion - Training guidelines for low-resource languages

## Methods Summary

The training pipeline involves: (1) creation of a strictly curated corpus of 13.6 billion Danish words from 350 million documents across diverse sources; (2) continuous pre-training of Llama2-7B on this corpus with careful learning rate scheduling and other hyperparameter choices; (3) instruction tuning using 3.7 million Danish instruction-answer pairs. The model is evaluated on eight language- and culturally-specific tasks from the ScandEval benchmark. Ablation studies examine the effects of various training decisions including data quality filtering, corpus composition, learning rate scheduling, and training duration.

## Results Summary

SnakModel achieves the highest overall performance among contemporary Llama2-7B-based Danish models across the eight evaluation tasks from ScandEval. The analysis reveals that data quality and careful curation are more important than raw data volume, and that training dynamics (learning rate scheduling, warmup strategies) significantly impact final performance. Hyperparameter ablations demonstrate that some design choices that work well for English or high-resource language training do not necessarily transfer to low-resource settings, highlighting the need for language-specific development guidelines.

## Conclusions

The work establishes practical training guidelines for developing LLMs in languages with limited resources, demonstrating that continuous pre-training of an existing English-centric model can effectively adapt it to a new language when combined with careful corpus curation and training decisions. By releasing the model, pre-training corpus, code, and intermediate checkpoints under open licenses, the authors contribute to enabling similar efforts for other low-resource languages.

## Artifact Contributions

- **SnakModel**: Open Danish LLM based on Llama2-7B (model weights publicly available)
- **Danish pre-training corpus**: 13.6B words from 350M documents, curated and released
- **Training code and checkpoints**: Open release of full pipeline for reproducibility
- **Training guidelines**: Documented lessons learned for low-resource language LLM development
- **Published at NoDaLiDa 2025**

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Open Danish LLM with cultural-specific evaluation, providing training guidelines for low-resource languages.

## Tags

