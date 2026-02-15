---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0454
type: preprint
short_title: "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment"
year: 2025
first_author: "[[Unknown]]"
last_author: "[[Unknown]]"
authors: "[[Unknown]]"
authors_incomplete: true
url: "https://arxiv.org/abs/2410.05873"
external_pdf: "https://arxiv.org/pdf/2410.05873.pdf"
publication: "arXiv / ACL Anthology"
pdf_extract: "PDF Extracts/2025/2025-group)-MEXA Multilingual Evaluation of English-Centric LLMs via.md"
local_pdf: "[[PDFs/2025/2025-group)-MEXA Multilingual Evaluation of English-Centric LLMs via.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: "Multiple including French"
religious_values: "Christianity"
religious_values_list: "Christianity"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "Llama-3.1, Gemma, Mistral, OLMo"
DATA_URL: "https://github.com/cisnlp/Mexa"
tags: 
abstract: "English-centric large language models (LLMs) often show strong multilingual capabilities. However, their multilingual performance remains unclear and is under-evaluated for many other languages. Most benchmarks for multilinguality focus on classic NLP tasks or cover a minimal number of languages. We introduce MEXA, a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream..."
ethics_perspective: "AI Safety & Alignment"
---
# MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment

## Authors

[[Unknown (CIS NLP group)]]

## Metadata

**Authors:** Unknown (CIS NLP group) (CIS NLP group)

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** Multiple including French

**Benchmark:** MEXA

## Links

- **arXiv:** https://arxiv.org/abs/2410.05873
- **Code/Data:** https://github.com/cisnlp/Mexa

## Abstract

Method for assessing multilingual capabilities of English-centric LLMs using parallel sentences. Achieves 0.90 Pearson correlation between predicted scores and actual task performance. Uses FLORES-200 and Bible parallel datasets. Published at ACL 2025 Findings.

## Summary

This paper introduces MEXA, a method for assessing the multilingual capabilities of English-centric LLMs using cross-lingual alignment scores computed from parallel sentences in the FLORES-200 and Bible datasets. The approach achieves a 0.90 Pearson correlation between predicted alignment scores and actual downstream task performance across nine evaluated models (Llama-3.1, Gemma, Mistral, OLMo). MEXA provides a cost-effective alternative to exhaustive multilingual benchmarking by estimating language capabilities without requiring language-specific downstream tasks, particularly valuable for languages where evaluation resources are scarce.

## Data Description

Introduces MEXA, a method to assess multilingual capabilities of English-centric LLMs using cross-lingual alignment scores computed from parallel sentences (FLORES-200 and Bible datasets), achieving 0.90 Pearson correlation with downstream task performance across nine models.


## Detailed Summary

This paper introduces MEXA (Multilingual Evaluation via Cross-Lingual Alignment), a method for assessing the multilingual capabilities of pre-trained English-centric LLMs by measuring how well non-English language embeddings align with their English counterparts in the model's intermediate layers. Building on the observation that English-centric LLMs use English as a "pivot language" in their middle layers for semantic processing, MEXA computes alignment scores using parallel sentences from FLORES-200 and the Bible corpus. The method achieves an average Pearson correlation of 0.90 between predicted alignment scores and actual downstream task performance (Belebele, m-MMLU, m-ARC) across nine models from the Llama family, Gemma family, Mistral, and OLMo. The authors explore different methods to compute embeddings in decoder-only models, finding that weighted average based on tokens combined with mean pooling across layers yields the best results. MEXA provides a scalable alternative to exhaustive language-specific benchmarking, particularly valuable for languages where evaluation resources are scarce. A public leaderboard is maintained at cis-lmu-mexa.hf.space.

## Paper Outline

1. Introduction - English-centric LLMs and the need for multilingual evaluation
2. Background and Related Work - Cross-lingual alignment research; pre-training data distribution
3. MEXA Method - Alignment computation using parallel sentences and middle-layer embeddings
4. Experimental Setup - Parallel datasets, models, downstream tasks
5. Results - Correlation analysis between MEXA scores and task performance
6. Design Analysis - Token-level pooling, layer-level pooling, embedding computation methods
7. Discussion and Conclusion

## Methods Summary

MEXA leverages the finding that English-centric LLMs process non-English input through an English "detour" in middle layers, assigning higher probabilities to English tokens before selecting foreign language tokens in upper layers. The method computes alignment by: (1) generating embeddings for parallel sentence pairs in English and a target language, (2) measuring alignment between these embeddings in the model's intermediate layers. Two parallel datasets are used: FLORES-200 (covering 200+ languages) and the Bible (covering even more languages). Design analyses compare last-token vs. weighted-average token pooling and different layer pooling strategies. Validation uses three downstream tasks: Belebele (reading comprehension), m-MMLU, and m-ARC.

## Results Summary

MEXA achieves an average Pearson correlation of 0.90 with actual downstream task performance across nine models and two parallel datasets. The weighted-average token pooling combined with mean pooling across layers yields the best and most consistent results. The method works across different model families (Llama, Gemma, Mistral, OLMo) and tasks, demonstrating its generalizability. Languages with higher MEXA alignment scores consistently achieve better downstream performance, validating the approach as a reliable proxy for multilingual capability estimation.

## Conclusions

MEXA provides a scalable, cost-effective method for estimating the multilingual coverage of English-centric LLMs without requiring language-specific downstream evaluation. The high correlation with actual performance suggests that cross-lingual alignment in intermediate layers is a reliable indicator of language capability. The method is particularly valuable for low-resource languages where evaluation benchmarks are unavailable.

## Artifact Contributions

- **Method:** MEXA - cross-lingual alignment scoring for multilingual LLM evaluation
- **Code:** github.com/cisnlp/MEXA
- **Leaderboard:** cis-lmu-mexa.hf.space - public multilingual capability leaderboard
- **Analysis:** Comprehensive evaluation across 9 models, 2 parallel datasets, and 3 downstream tasks

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Provides a method to estimate French-language capabilities of English-centric LLMs without requiring French-specific benchmarks.

## Tags

