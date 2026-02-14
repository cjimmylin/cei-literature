---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0549
type: preprint
short_title: "Multilingual European Language Models: Benchmarking Approaches and Challenges"
year: 2025
first_author: "[[Fabio Barth]]"
last_author: "[[Georg Rehm]]"
authors: "Fabio Barth, Georg Rehm"
url: "https://arxiv.org/abs/2502.12895"
external_pdf: "https://arxiv.org/pdf/2502.12895.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-Barth-Multilingual European Language Models Benchmarking Approaches and.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Barth-Multilingual European Language Models Benchmarking Approaches and.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: "Multiple European languages"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multilingual benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "EuroLLM, Teuken-7B, Salamandra"
DATA_URL: NA
tags: 
abstract: "The breakthrough of generative large language models (LLMs) that can solve different tasks through chat interaction has led to a significant increase in the use of general benchmarks to assess the quality or performance of these models beyond individual applications. There is also a need for better methods to evaluate and also to compare models due to the ever increasing number of new models published. However, most of the established benchmarks revolve around the English language."
research_topic: "Machine Translation"
---
# Multilingual European Language Models: Benchmarking Approaches and Challenges

## Authors

[[Fabio Barth, Georg Rehm]]

## Metadata

**Authors:** Fabio Barth, Georg Rehm

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Multiple European languages

## Links

- **arXiv:** https://arxiv.org/abs/2502.12895

## Abstract

Analyzes benefits and limitations of current multilingual European evaluation datasets, focusing on seven multilingual benchmarks. Identifies four major challenges including cultural biases in translated benchmarks. Discusses solutions for translation quality and cultural bias mitigation including human-in-the-loop verification.

## Summary

This meta-analysis paper examines seven multilingual European LLM benchmarks (GlobalMMLU, MMMLU, EU20, OKAPI, Include, Belebele, Xtreme) to assess their benefits and limitations. The authors identify four major challenges in multilingual evaluation, with particular focus on cultural biases inherent in translated benchmarks and translation quality issues. They propose solutions including human-in-the-loop verification, iterative translation ranking, and culturally aware benchmark development to improve the assessment of multilingual European LLMs.

## Data Description

This is a meta-analysis paper that analyzes seven multilingual European benchmarks (GlobalMMLU, MMMLU, EU20, OKAPI, Include, Belebele, Xtreme) and identifies four major challenges in multilingual LLM evaluation including cultural biases in translated benchmarks. It does not introduce a new dataset but evaluates existing benchmarking approaches.


## Detailed Summary

This paper provides a meta-analysis of seven multilingual European LLM benchmarks -- GlobalMMLU, MMMLU, EU20, OKAPI, Include, Belebele, and Xtreme -- to assess their benefits and limitations for evaluating multilingual European language models. The authors categorize these benchmarks into two groups: those based on translated English benchmarks (machine-translated or human-translated) and those developed from regional or multilingual data sources. The analysis is motivated by the growing number of multilingual LLMs published for European languages, such as EuroLLM, Teuken-7B, and Salamandra, which are often evaluated using machine-translated versions of English benchmarks.

The authors identify four major challenges: (1) cross-lingual comparison difficulties due to inconsistent language coverage and task representations; (2) translationese, where unnatural linguistic artifacts from source language interference distort evaluation quality; (3) cultural biases inherently embedded in English-centric benchmarks that cannot be addressed through automated translation alone; and (4) data quality issues that cascade through the benchmark generation pipeline. They propose solutions including human-in-the-loop verification, iterative translation ranking using quality estimation metrics like COMET, and the development of culturally grounded benchmarks based on regional sources rather than translated English content.

## Paper Outline

1. Introduction - Motivation for multilingual benchmarks and current limitations
2. Approaches - Analysis of seven multilingual benchmarks and evaluation methods
3. Challenges - Four major challenges identified (cross-lingual comparison, translationese, cultural bias, data quality)
4. Conclusions - Summary and recommendations

## Methods Summary

The study employs a comparative analysis methodology, examining seven multilingual general-domain benchmarks that cover at least nine of the 24 official EU languages. The benchmarks are categorized by their development approach: translation-based (GlobalMMLU, MMMLU, EU20, OKAPI) versus regionally-sourced (Include, Belebele, Xtreme). The analysis draws on evaluation methods including accuracy, F1 score, and exact match metrics used across these benchmarks. Translation quality is assessed using metrics like COMET scores, and cultural bias is evaluated through human annotation frameworks that label samples as culturally-sensitive or culturally-agnostic.

## Results Summary

The analysis reveals that automatically translated benchmarks contain error rates of up to 2.3% (as identified by Thellmann et al., 2024), with these errors varying across individual languages and impacting cross-lingual comparability. Benchmarks developed from regional sources (like Include) avoid English-centric cultural biases but introduce their own cultural perspectives. The authors find that none of the existing benchmarks fully addresses all four identified challenges simultaneously, with trade-offs between translation quality, cultural awareness, language coverage, and data quality. Human annotation improves quality but reduces scale, while automated translation is cost-efficient but introduces artifacts and cultural misalignment.

## Conclusions

The paper concludes that a diverse and comprehensive collection of European language benchmarks is needed to analyze and compare multilingual language models in detail. Limitations include the scope being restricted to benchmarks covering at least nine EU languages, potentially missing valuable monolingual resources. Future work directions include developing improved translation-verification pipelines with humans in the loop, creating more culturally grounded benchmarks from regional sources, and establishing iterative processes for automatically ranking and re-translating benchmark items until quality thresholds are met.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Meta-analysis of European LLM benchmarking. Addresses cultural bias in translated benchmarks -- directly relevant to evaluation fairness for Greek and other European minority languages.

## Tags

