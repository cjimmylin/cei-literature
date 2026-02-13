---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CWLWCFUJ
type: conferencePaper
short_title: BBQ
year: 2025
first_author: "[[Alicia Parrish]]"
last_author: "[[Samuel Bowman]]"
authors: "Alicia Parrish; Angelica Chen; Nikita Nangia; Vishakh Padmakumar; Jason Phang; Jana Thompson; Phu Mon Htut; Samuel Bowman"
doi: 10.18653/v1/2022.findings-acl.165
url: "https://aclanthology.org/2022.findings-acl.165/"
external_pdf: "https://aclanthology.org/2022.findings-acl.165.pdf"
national_ethnic_cultural: American
religious_values: "Islam, Christianity"
religious_values_list: "Islam, Christianity"
moral_psychology: N/A
newtags: "American, Bias & Fairness"
key_contribution: "Introduced BBQ (Bias Benchmark for QA), a hand-built dataset highlighting social biases against protected classes in US English contexts, testing responses in under-informative vs. informative settings."
significance: "Demonstrates that models often rely on harmful stereotypes when context is ambiguous, establishing a standard metric for measuring social bias in Question Answering systems."
tags: 
abstract: "It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluates model responses at two levels: (i) given"
local_pdf: [[PDFs/2022/2022-Parrish-BBQ.pdf]]
pdf_extract: "PDF Extracts/2022/2022-Parrish-BBQ.md"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "T5, RoBERTa, DeBERTa"
DATA_URL: "https://github.com/nyu-mll/BBQ"
---
# BBQ: A hand-built bias benchmark for question answering

## Metadata

**Authors:** Parrish, Alicia; Chen, Angelica; Nangia, Nikita; Padmakumar, Vishakh; Phang, Jason; Thompson, Jana; Htut, Phu Mon; Bowman, Samuel

**Year:** 2022

**Publication:** Findings of the Association for Computational Linguistics: ACL 2022

**Type:** conferencePaper

**DOI:** [10.18653/v1/2022.findings-acl.165](https://doi.org/10.18653/v1/2022.findings-acl.165)

**Pages:** 2086-2105

**Publisher:** Association for Computational Linguistics

## Links

- **ACL Anthology:** https://aclanthology.org/2022.findings-acl.165
- **DOI:** https://doi.org/10.18653/v1/2022.findings-acl.165

## Abstract

It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question-sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluate model responses at two levels: (i) given an under-informative context, we test how strongly responses reflect social biases, and (ii) given an adequately informative context, we test whether the model’s biases override a correct answer choice. We find that models often rely on stereotypes when the context is under-informative, meaning the model’s outputs consistently reproduce harmful biases in this setting. Though models are more accurate when the context provides an informative answer, they still rely on stereotypes and average up to 3.4 percentage points higher accuracy when the correct answer aligns with a social bias than when it conflicts, with this difference widening to over 5 points on examples targeting gender for most models tested.

## Authors

[[Alicia Parrish]], [[Angelica Chen]], [[Nikita Nangia]], [[Vishakh Padmakumar]], [[Jason Phang]], [[Jana Thompson]], [[Phu Mon Htut]], [[Samuel Bowman]]

## Data Description

BBQ (Bias Benchmark for QA) contains 58,492 unique examples from 325 hand-written templates targeting attested social biases across nine categories relevant to U.S. English-speaking contexts. The benchmark evaluates model responses at two levels: reliance on stereotypes in under-informative contexts, and whether biases override correct answers in adequately informative contexts. Models evaluated include UnifiedQA (T5-based), RoBERTa, and DeBERTaV3.


## Notes


## Citation Info

792 citations (Semantic Scholar/DOI) [2025-08-27] 479 citations (Semantic Scholar/DOI) [2025-08-23] 54 citations (Crossref/DOI) [2025-08-23]
