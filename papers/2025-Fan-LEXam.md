---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0068
type: preprint
short_title: LEXam
year: 2025
first_author: "[[Fan, Yu]]"
last_author: "[[Niklaus, Joel]]"
authors: "[[Fan, Yu]]; [[Ni, Jingwei]]; [[Merane, Jakob]]; [[Tian, Yang]]; [[Hermstrüwer, Yoan]]; [[Huang, Yinya]]; [[Akhtar, Mubashara]]; [[Salimbeni, Etienne]]; [[Geering, Florian]]; [[Dreyer, Oliver]]; [[Brunner, Daniel]]; [[Leippold, Markus]]; [[Sachan, Mrinmaya]]; [[Stremitzer, Alexander]]; [[Engel, Christoph]]; [[Ash, Elliott]]; [[Niklaus, Joel]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2505.12864"
external_pdf: "https://arxiv.org/pdf/2505.12864.pdf"
local_pdf: "[[PDFs/2025-Fan-LEXam.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Fan-LEXam.md"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: German
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "Long-form legal reasoning remains a key challenge for large language models (LLMs) in spite of recent advances in test-time scaling. To address this, we introduce LEXAM, a novel benchmark derived from 340 law exams spanning 116 law school courses across a range of subjects and degree levels. The dataset comprises 4,886 law exam questions in English and German, including 2,841 long-form, open-ended questions and 2,045 multiple-choice questions."
research_topic: "Machine Learning"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, DeepSeek, Gemini, Claude, Qwen, Llama-3, Gemma, Phi, Mistral"
DATA_URL: "https://lexam-benchmark.github.io/"
---
# LEXam

## Authors

[[Fan, Yu]], [[Ni, Jingwei]], [[Merane, Jakob]], [[Tian, Yang]], [[Hermstrüwer, Yoan]], [[Huang, Yinya]], [[Akhtar, Mubashara]], [[Salimbeni, Etienne]], [[Geering, Florian]], [[Dreyer, Oliver]], [[Brunner, Daniel]], [[Leippold, Markus]], [[Sachan, Mrinmaya]], [[Stremitzer, Alexander]], [[Engel, Christoph]], [[Ash, Elliott]], [[Niklaus, Joel]]

## Metadata

**Authors:** Fan, Yu; Ni, Jingwei; Merane, Jakob; Tian, Yang; Hermstrüwer, Yoan; Huang, Yinya; Akhtar, Mubashara; Salimbeni, Etienne; Geering, Florian; Dreyer, Oliver; Brunner, Daniel; Leippold, Markus; Sachan, Mrinmaya; Stremitzer, Alexander; Engel, Christoph; Ash, Elliott; Niklaus, Joel

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2505.12864
- **Code/Data:** https://github.com/LEXam-Benchmark/LEXam](https://github.com/LEXam-Benchmark/LEXam; https://huggingface.co/datasets/LEXam-Benchmark/LEXam](https://huggingface.co/datasets/LEXam-Benchmark/LEXam

## Abstract

Long-form legal reasoning remains a key challenge for large language models (LLMs) in spite of recent advances in test-time scaling. To address this, we introduce LEXAM, a novel benchmark derived from 340 law exams spanning 116 law school courses across a range of subjects and degree levels. The dataset comprises 4,886 law exam questions in English and German, including 2,841 long-form, open-ended questions and 2,045 multiple-choice questions. Besides reference answers, the open questions are also accompanied by explicit guidance outlining the expected legal reasoning approach such as issue spotting, rule recall, or rule application. Our evaluation on both open-ended and multiple-choice questions present significant challenges for current LLMs; in particular, they notably struggle with open questions that require structured, multi-step legal reasoning. Moreover, our results underscore the effectiveness of the dataset in differentiating between models with varying capabilities. Deploying an ensemble LLM-as-a-Judge paradigm with rigorous human expert validation, we demonstrate how model-generated reasoning steps can be evaluated consistently and accurately, closely aligning with human expert assessments. Our evaluation setup provides a scalable method to assess legal reasoning quality beyond simple accuracy metrics. We have open-sourced our code on GitHub and released our data on Hugging Face. Project page: https://lexam-benchmark.github.io/.

## Dataset Information

4,886 law exam questions (English + German)

## Data Description

LEXAM is a multilingual legal reasoning benchmark derived from 340 law exams spanning 116 courses at the University of Zurich, comprising 4,886 questions (2,841 open-ended and 2,045 multiple-choice) in English and German. The authors evaluate 36 LLMs across reasoning, large, and small model categories, including GPT-4o/4.1, DeepSeek-R1/V3, Gemini-2.5-Pro, Claude-3.7/4.5-Sonnet, Qwen3, Llama-3/4, Gemma-2/3, Phi-4, and Ministral-8B, using an ensemble LLM-as-a-Judge evaluation framework validated against human expert assessments.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

