---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0243
type: conferencePaper
short_title: BBQ (Bias Benchmark for Question Answering)
year: 2022
first_author: "[[Alicia Parrish]]"
last_author: "[[Alicia Parrish]]"
authors: Alicia Parrish et al.
authors_incomplete: true
url: "https://arxiv.org/abs/2110.08193"
external_pdf: "https://arxiv.org/pdf/2110.08193.pdf"
local_pdf: "[[PDFs/2022/2022-Parrish-BBQ Bias Benchmark for Question Answering.pdf]]"
pdf_extract: "PDF Extracts/2022/2022-Parrish-BBQ Bias Benchmark for Question Answering.md"
publication: ACL 2022
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts."
ethics_perspective: "Bias & Fairness"
data_description: "Benchmark for bias and fairness dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "T5, RoBERTa, DeBERTa"
DATA_URL: "https://github.com/nyu-mll/BBQ"
---
# BBQ (Bias Benchmark for Question Answering)

## Authors

[[Alicia Parrish]]

## Metadata

**Authors:** Alicia Parrish et al.

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL 2022

## Links

- **arXiv:** https://arxiv.org/abs/2110.08193
- **Code/Data:** https://github.com/nyu-mll/BBQ; https://huggingface.co/datasets/heegyu/bbq; https://huggingface.co/datasets/walledai/BBQ

## Abstract

It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluates model responses at two levels: (i) given an under-informative context, we test how strongly responses reﬂect social biases, and (ii) given an adequately informative context, we test whether the model’s biases override a correct answer choice. We ﬁnd that models often rely on stereotypes when the context is under-informative, meaning the model’s outputs consistently reproduce harmful biases in this setting. Though models are more accurate when the context provides an informative answer, they still rely on stereotypes and average up to 3.4 percentage points higher accuracy when the correct answer aligns with a social bias than when it conﬂicts, with this difference widening to over 5 points on examples targeting gender for most models tested.

## Dataset Information

~58,000 multiple-choice questions; ambiguous and disambiguated contexts; 11 JSONL files (one per bias category)

## Data Description

BBQ (Bias Benchmark for QA) is a hand-built dataset of 58,492 unique examples constructed from 325 templates across nine social bias categories (age, disability, gender, nationality, physical appearance, race/ethnicity, religion, socioeconomic status, and sexual orientation). Each example pairs an ambiguous or disambiguated context with negative or non-negative questions and three answer choices, designed to test whether QA models rely on social stereotypes. Models tested include UnifiedQA (T5-based), RoBERTa, and DeBERTaV3.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

