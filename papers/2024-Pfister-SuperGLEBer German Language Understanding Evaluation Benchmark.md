---

































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0464
type: conferencePaper
short_title: "SuperGLEBer: German Language Understanding Evaluation Benchmark"
year: 2024
first_author: "[[Jan Pfister]]"
last_author: "[[Andreas Hotho]]"
authors: Jan Pfister; Andreas Hotho
url: "https://aclanthology.org/2024.naacl-long.438/"
external_pdf: "https://aclanthology.org/2024.naacl-long.438.pdf"
publication: "ACL Anthology"
CONF-CC: "N/A"
pdf_extract: "PDF Extracts/2024/2024-Pfister-SuperGLEBer German Language Understanding Evaluation Benchmark.md"
local_pdf: "[[PDFs/2024/2024-Pfister-SuperGLEBer German Language Understanding Evaluation Benchmark.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT"
DATA_URL: "https://github.com/LSX-UniWue/SuperGLEBer"
tags: 
abstract: "We assemble a broad Natural Language Understanding benchmark suite for the German language and consequently evaluate a wide array of existing German-capable models in order to create a better understanding of the current state of German LLMs. Our benchmark consists of 29 different tasks ranging over different types such as document classification, sequence tagging, sentence similarity, and question answering, on which we evaluate 10 different German-pretrained models, thereby charting the..."
CONFERENCE: "ACL 2024"
ethics_overall: 60
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
ethics_perspective: "General Ethics"
---
# SuperGLEBer: German Language Understanding Evaluation Benchmark

## Authors

[[Jan Pfister]], [[Andreas Hotho]]

## Metadata

**Authors:** Jan Pfister, Andreas Hotho

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** German

**Benchmark:** SuperGLEBer

## Links

- **URL:** https://aclanthology.org/2024.naacl-long.438/
- **Code/Data:** https://github.com/LSX-UniWue/SuperGLEBer

## Abstract

Comprehensive German NLU benchmark with 29 tasks spanning document classification, sequence tagging, sentence similarity, and question answering. Evaluates 10 German-pretrained models. First comprehensive German-language benchmark for LLMs.

## Summary

This paper introduces SuperGLEBer, the first comprehensive Natural Language Understanding benchmark suite for the German language, addressing the lack of systematic evaluation frameworks for German LLMs. The benchmark comprises 29 diverse tasks across four types (document classification, sequence tagging, sentence similarity, and question answering) sourced from various domains, with tasks selected to have simple input/output formats and intuitive evaluation metrics. The authors evaluate 10 German-pretrained models (4 encoder-only, 3 decoder-only, 3 encoder-decoder) and find that encoder models generally perform best, though the largest encoder model does not consistently outperform smaller counterparts. The benchmark suite and leaderboard are publicly available to foster continued German LLM research.

## Data Description

SuperGLEBer is a comprehensive German NLU benchmark with 29 tasks spanning document classification, sequence tagging, sentence similarity, and question answering. Evaluates 10 German-pretrained models. First comprehensive German-language benchmark for LLMs.


## Detailed Summary

This paper introduces SuperGLEBer, the first comprehensive Natural Language Understanding benchmark suite specifically designed for the German language. The benchmark addresses a critical gap: newly introduced German BERT-based models have historically been evaluated on only two tasks each, insufficient for understanding their full capabilities. SuperGLEBer assembles 29 diverse tasks across four categories (document classification, sequence tagging, sentence similarity, and question answering), sourced from various domains including toxic/offensive language identification, sentiment analysis, named entity recognition, semantic textual similarity, and reading comprehension. All tasks use German-native or human-translated test sets (not machine-translated), and feature simple input/output formats with intuitive evaluation metrics. Ten German-pretrained models spanning encoder-only, decoder-only, and encoder-decoder architectures are comprehensively evaluated.

## Paper Outline

1. Introduction - Need for systematic German NLU evaluation
2. German Evaluation Tasks - Task descriptions across four categories
3. Model Selection - 10 German-pretrained models across three architectures
4. Experimental Setup - Training details, hyperparameters
5. Results - Comprehensive benchmark evaluation
6. Conclusion

## Methods Summary

The benchmark selects tasks meeting strict criteria: datasets must have human-translated or natively German-annotated test sets (no machine translation), simple input/output formats avoiding complex task-specific architectures, and evaluable with intuitive metrics (ruling out open-ended generation). The 29 tasks span five text classification domains (toxic/offensive language, sentiment analysis, news/topic classification, fact checking, other classification), sequence tagging (NER, POS, clause segmentation), sentence similarity (STS, paraphrase detection, NLI), and question answering (extractive, multiple choice). Models evaluated include 4 encoder-only (gBERT variants, gelectra, GPTBERT), 3 decoder-only (bloom-clp, mGPT, leo-7b), and 3 encoder-decoder (mT5, mBART, leo-hessianai-13b) architectures.

## Results Summary

Encoder models generally perform best and are usually consistently close to each other across tasks. Notably, the two largest models (mBART and leo-7b) also perform well despite not being encoder architectures, likely due to their larger size. However, the largest encoder model (gBERT-large) does not consistently profit from its larger size compared to smaller counterparts. The benchmark reveals that no single architecture dominates all task types, with different models excelling in different areas. The inclusion of toxic and offensive language identification tasks (Wiegand et al. 2018, Risch et al. 2021) provides evaluation of German hate speech detection capabilities.

## Conclusions

SuperGLEBer provides a much-needed comprehensive evaluation framework for German NLU, enabling systematic comparison of German-pretrained models across diverse tasks and domains. The open-source benchmark suite with public leaderboard (supergleber.professor-x.de) is designed for community expansion with additional tasks and models, fostering continued German LLM research. Published at NAACL 2024.

## Artifact Contributions

- **SuperGLEBer benchmark**: 29-task German NLU evaluation suite covering four task types
- **Comprehensive evaluation**: Results for 10 German-pretrained models across three architectures
- **Public leaderboard**: supergleber.professor-x.de for community contributions
- **Open-source code**: https://github.com/LSX-UniWue/SuperGLEBer

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** The most comprehensive German-language NLU benchmark, foundational for evaluating German LLMs across diverse tasks.

## Tags

