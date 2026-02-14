---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0491
type: preprint
short_title: "DaCy: A Unified Framework for Danish NLP"
year: 2021
first_author: "[[Kenneth C. Enevoldsen]]"
last_author: "[[Kristoffer Nielbo]]"
authors: Kenneth C. Enevoldsen, Lasse Hansen, Kristoffer Nielbo
url: "https://arxiv.org/abs/2107.05295"
external_pdf: "https://arxiv.org/pdf/2107.05295.pdf"
publication: arXiv
local_pdf: "[[PDFs/2021/2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.pdf]]"
pdf_extract: "PDF Extracts/2021/2021-Enevoldsen-DaCy A Unified Framework for Danish NLP.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "Danish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multi-task benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "ELECTRA, BERT, XLM-RoBERTa"
DATA_URL: "https://github.com/centre-for-humanities-computing/DaCy"
tags: 
abstract: "Danish natural language processing (NLP) has in recent years obtained considerable improvements with the addition of multiple new datasets and models. However, at present, there is no coherent framework for applying state-of-the-art models for Danish. We present DaCy: a uniﬁed framework for Danish NLP built on SpaCy. DaCy uses efﬁcient multitask models which obtain state-of-the-art performance on named entity recognition, part-of-speech tagging, and dependency parsing."
ethics_perspective: "Bias & Fairness"
---
# DaCy: A Unified Framework for Danish NLP

## Authors

[[Kenneth C. Enevoldsen, Lasse Hansen, Kristoffer Nielbo]]

## Metadata

**Authors:** Kenneth C. Enevoldsen, Lasse Hansen, Kristoffer Nielbo

**Year:** 2021

**Type:** preprint

**Venue:** arXiv

**Languages:** Danish

**Benchmark:** DaCy

## Links

- **arXiv:** https://arxiv.org/abs/2107.05295
- **Code/Data:** https://github.com/alexandrainst/danlp

## Abstract

Unified Danish NLP framework with bias and robustness testing. Found all models except DaCy large display significant ethnicity biases; only Polyglot shows significant gender bias. Uses data augmentation for more realistic performance estimates.

## Summary

This paper presents DaCy, a unified SpaCy-based framework for Danish NLP providing three multitask models (DaCy small based on Danish ELECTRA, DaCy medium based on Danish BERT, and DaCy large based on XLM-RoBERTa) achieving state-of-the-art performance on POS tagging, named entity recognition, and dependency parsing. The authors conduct comprehensive bias and robustness testing using data augmentation on the DaNE dataset, revealing that all models except DaCy large display significant ethnicity biases, while only Polyglot shows significant gender bias. The framework emphasizes that data augmentation can provide more realistic performance estimates for low-resource languages and includes tools for easy integration of existing models for sentiment, emotion, and subjectivity detection.

## Data Description

DaCy framework providing three Danish NLP models: DaCy small (Danish ELECTRA, 14M parameters), DaCy medium (Danish BERT, 110M parameters), and DaCy large (XLM-RoBERTa, 550M parameters). Evaluated on POS tagging, NER, and dependency parsing with data augmentation tests for robustness.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Danish NLP framework with explicit bias testing revealing ethnicity and gender biases in Danish models.

## Tags

