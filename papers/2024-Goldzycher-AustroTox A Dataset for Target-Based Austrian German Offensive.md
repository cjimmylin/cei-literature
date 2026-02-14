---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0463
type: preprint
short_title: "AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection"
year: 2024
first_author: "[[Janis Goldzycher]]"
last_author: "[[Hanna Mahler]]"
authors: Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler
url: "https://arxiv.org/abs/2406.08080"
external_pdf: "https://arxiv.org/pdf/2406.08080.pdf"
publication: arXiv / ACL Anthology
local_pdf: "[[PDFs/2024/2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: "German (Austrian)"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach annotated dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, mGPT, German BERT variants"
DATA_URL: "https://github.com/rafaelgoldzy/AustroTox"
tags: 
abstract: "Model interpretability in toxicity detection greatly profits from token-level annotations. However, currently such annotations are only available in English. We introduce a dataset annotated for offensive language detection sourced from a news forum, notable for its incorporation of the Austrian German dialect, comprising 4,562 user comments. In addition to binary offensiveness classification, we identify spans within each comment constituting vulgar language or representing targets of..."
ethics_perspective: "Toxicity & Hate Speech"
---
# AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection

## Authors

[[Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler]]

## Metadata

**Authors:** Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** German (Austrian)

**Benchmark:** AustroTox

## Links

- **arXiv:** https://arxiv.org/abs/2406.08080

## Abstract

Dataset of 4,562 Austrian German user comments annotated for offensive language detection with token-level spans for vulgarities and offensive targets. LLMs outperform fine-tuned models in detecting offensiveness while fine-tuned models excel at detecting dialect-specific vulgarities.

## Summary

This paper introduces AustroTox, the first offensive language detection dataset specifically for Austrian German dialect, comprising 4,562 user comments from news forums with token-level annotations for offensiveness, vulgar language spans, and offensive targets. The dataset addresses the critical gap in non-English token-level offensive language annotations and incorporates a target-based taxonomy (individual, group, other, none) to enhance model interpretability. The authors evaluate multiple models including GPT-3.5, GPT-4, mGPT, and German BERT variants, finding that large language models outperform fine-tuned models in detecting overall offensiveness while fine-tuned approaches excel at identifying dialect-specific vulgarities. This work provides essential resources for developing more robust and interpretable offensive language detection systems for Austrian German.

## Data Description

AustroTox dataset of 4,562 Austrian German Reddit comments annotated for offensive language with target-based taxonomy (individual, group, other, none). First offensive language dataset specifically for Austrian German dialect, comparing LLM performance vs. fine-tuned approaches.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First token-level offensive language annotations for non-English (Austrian German dialect), evaluating both LLMs and fine-tuned models.

## Tags

