---

























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 55N7FPTB
type: conferencePaper
short_title: "Gender Bias in Coreference Resolution"
year: 2018
first_author: "[[Jieyu Zhao]]"
last_author: "[[Chang, Kai-Wei]]"
authors: "Zhao, Jieyu; Wang, Tianlu; Yatskar, Mark; Ordonez, Vicente; Chang, Kai-Wei"
doi: 10.18653/v1/N18-2003
url: "https://arxiv.org/abs/1804.06876"
pdf_extract: "PDF Extracts/2018/2018-Zhao-Gender Bias in Coreference Resolution.md"
local_pdf: "[[PDFs/2018/2018-Zhao-Gender Bias in Coreference Resolution.pdf]]"
external_pdf: "https://arxiv.org/pdf/1804.06876.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Creates WinoBias, a coreference resolution benchmark specifically designed to detect gender bias (stereotypical vs anti-stereotypical occupations)"
significance: "A foundational operationalization of the deontological duty of 'fairness' in NLP, moving from abstract bias to concrete measurable failure modes"
tags: 
abstract: "We present an empirical study of gender bias in coreference resolution systems. We ﬁrst introduce a novel, Winograd schema-style set of minimal pair sentences that differ only by pronoun gender. With these Winogender schemas, we evaluate and conﬁrm systematic gender bias in three publicly-available coreference resolution systems, and correlate this bias with real-world and textual gender statistics."
paper_summary: "Introduces WinoBias, a benchmark for coreference resolution focused on gender bias. Demonstrates that rule-based, feature-rich, and neural coreference systems link gendered pronouns to pro-stereotypical entities with higher accuracy than anti-stereotypical entities (21.1 F1 difference). Proposes a data-augmentation debiasing approach."
CONF-CC: "NAACL 2018"
DATE_ADDED: 20260208
LLM_assessed: "NA"
DATA_URL: "https://github.com/rudinger/winogender-schemas"
ethics_perspective: "Bias & Fairness"
CONFERENCE: "Other Conference"
helm: "incorporated"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness text corpus"
data_metrics: "Not specified"
---
 Gender Bias in Coreference Resolution: Evaluation and Debiasing Methods

## Authors

[[Jieyu Zhao|Zhao, Jieyu]], [[Tianlu Wang|Wang, Tianlu]], [[Mark Yatskar|Yatskar, Mark]], [[Vicente Ordonez|Ordonez, Vicente]], [[Kai-Wei Chang|Chang, Kai-Wei]]

## Links

- **Local PDF:** [[PDFs/2018/2018-Zhao-Gender Bias in Coreference Resolution.pdf|Open PDF]]

- **URL:** http://aclweb.org/anthology/N18-2003
- **DOI:** https://doi.org/10.18653/v1/N18-2003

## Abstract

We introduce a new benchmark, WinoBias, for coreference resolution focused on gender bias. Our corpus contains Winograd-schema style sentences with entities corresponding to people referred by their occupation (e.g. the nurse, the doctor, the carpenter). We demonstrate that a rule-based, a feature-rich, and a neural coreference system all link gendered pronouns to pro-stereotypical entities with higher accuracy than anti-stereotypical entities, by an average difference of 21.1 in F1 score. Finally, we demonstrate a data-augmentation approach that, in combination with existing word-embedding debiasing techniques, removes the bias demonstrated by these systems in WinoBias without signiﬁcantly affecting their performance on existing coreference benchmark datasets. Our dataset and code are available at http://winobias.org.

## Data Description

This paper introduces Winogender schemas, a Winograd schema-style challenge dataset of minimal pair sentences differing only by pronoun gender, designed to detect gender bias in coreference resolution systems. Three publicly available coreference systems are evaluated (rule-based Stanford CoreNLP, feature-driven statistical, and neural end-to-end), demonstrating systematic gender bias correlated with real-world employment statistics. No LLMs are tested.


## Notes
> [!INFO]
> **Issue Resolved (2026-01-24)**: The arXiv URL was corrected from 1804.09301 (Rudinger et al.) to 1804.06876 (Zhao et al.). Both papers have the same title but are different works published at NAACL 2018. Zhao's paper introduces WinoBias; Rudinger's introduces Winogender schemas. The abstract and paper_summary have been corrected. The local PDF extract may still reflect the Rudinger paper and should be regenerated.


## Citation Info

975 citations (Semantic Scholar/DOI) [2025-08-23] 193 citations (Crossref/DOI) [2025-08-23]
