---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0502
type: conferencePaper
short_title: "ITALIC: An Italian Culture-Aware Natural Language Benchmark"
year: 2025
first_author: "[[Andrea Seveso]]"
last_author: "[[Fabio Mercorio]]"
authors: "Andrea Seveso, Daniele Potertì, Edoardo Federici, Mario Mezzanzanica, Fabio Mercorio"
url: "https://aclanthology.org/2025.naacl-long.68/"
external_pdf: "https://aclanthology.org/2025.naacl-long.68.pdf"
publication: "ACL Anthology (NAACL 2025)"
local_pdf: "[[PDFs/2025/2025-Seveso-ITALIC An Italian Culture-Aware Natural Language Benchmark.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Seveso-ITALIC An Italian Culture-Aware Natural Language Benchmark.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: Italian
languages_list: Italian
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: No
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Gemini, Llama, Mistral, Qwen, Aya"
DATA_URL: "https://italicbench.it/"
tags: 
abstract: 
research_topic: "Machine Learning"
---
# ITALIC: An Italian Culture-Aware Natural Language Benchmark

## Authors

[[Andrea Seveso, Daniele Potertì, Edoardo Federici, Mario Mezzanzanica, Fabio Mercorio]]

## Metadata

**Authors:** Andrea Seveso, Daniele Potertì, Edoardo Federici, Mario Mezzanzanica, Fabio Mercorio

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology (NAACL 2025)

**Languages:** Italian

**Benchmark:** ITALIC

## Links

- **URL:** https://aclanthology.org/2025.naacl-long.68/
- **Code/Data:** https://italicbench.it/

## Abstract

A large-scale benchmark dataset of 10,000 multiple-choice questions designed to evaluate NLU of Italian language and culture across 12 domains. Baseline performances established using 17 state-of-the-art LLMs reveal current limitations in Italian language understanding and highlight significant cultural specificity challenges.

## Summary

This paper presents ITALIC (ITALIan Cultural Benchmark), a large-scale benchmark of 10,000 multiple-choice questions from Italian public competition exams designed to evaluate natural language understanding of Italian language and culture across 12 domains including history, geography, literature, and civic knowledge. The questions assess both cultural knowledge and linguistic proficiency in morphologically rich Italian, addressing limitations of translated English benchmarks that lack cultural localization. Evaluation of 17 state-of-the-art LLMs including GPT-4, Claude, Gemini, Llama, Mistral, Qwen, and Aya reveals current limitations in Italian language understanding and highlights significant challenges in linguistic complexity and cultural specificity, demonstrating the risk of cultural homogenization with Anglocentric models.

## Data Description

ITALIC is a large-scale benchmark dataset of 10,000 multiple-choice questions designed to evaluate natural language understanding of Italian language and culture across 12 domains. Baseline performances established using 17 state-of-the-art LLMs reveal current limitations in Italian language understanding and highlight significant cultural specificity challenges.


## Detailed Summary

This paper presents ITALIC (ITALIan Cultural Benchmark), a large-scale benchmark dataset of 10,000 multiple-choice questions designed to evaluate LLMs' understanding of Italian language and culture. The questions are sourced from Italian public competition exams (concorsi pubblici) used for merit-based selection in domains such as university admissions, military recruitment, and public sector positions. These standardized assessments evaluate candidates' domain knowledge, general knowledge, and linguistic/analytical capabilities according to Italian national standards. ITALIC spans 12 domains including history, geography, literature, civic knowledge, and linguistic proficiency, capturing both commonsense reasoning and cultural knowledge specific to Italy.

The benchmark addresses the critical gap in Italian LLM evaluation, where models are typically tested on benchmarks translated from English that fail to account for Italian cultural specificity. The Italian government's AI strategy document for 2024-2026 explicitly highlights the risk of cultural homogenization when using Anglocentric LLMs, providing policy-level motivation for this work. Baseline performance evaluation of 17 state-of-the-art LLMs -- including GPT-4, Claude, Gemini, Llama, Mistral, Qwen, and Aya -- reveals current limitations in Italian language understanding and highlights significant challenges in linguistic complexity and cultural specificity. The results show that even top-performing models struggle with culturally-grounded questions that require knowledge of Italian history, literature, and civic institutions, demonstrating that scale alone does not guarantee cultural alignment.

## Paper Outline

1. Introduction and Motivation - Risk of cultural homogenization and need for Italian-specific evaluation
2. Related Work - English benchmarks, cultural benchmarks, and Italian evaluation efforts
3. Dataset - Data collection process, stratification techniques, and selection strategies
4. Experimental Setup - Model configurations and evaluation methodology
5. Results - Baseline performance across 17 LLMs
6. Discussion - Limitations and implications
7. Conclusion

## Methods Summary

The dataset is constructed from Italian public competition exams across 12 domains, carefully stratified to ensure balanced representation. Questions are formatted as multiple-choice with four options. Data collection involves systematic extraction from publicly available exam archives, followed by quality filtering and categorization into cultural knowledge and linguistic proficiency domains. Seventeen LLMs are evaluated including proprietary models (GPT-4, Claude, Gemini) and open-source models (Llama, Mistral, Qwen, Aya), with various parameter sizes and configurations. Evaluation uses accuracy as the primary metric, with domain-specific analysis to identify model strengths and weaknesses across different aspects of Italian cultural knowledge.

## Results Summary

Evaluation of 17 LLMs reveals significant variation in performance across cultural domains, with all models showing weaknesses in culturally-specific knowledge areas. Top-performing models achieve moderate accuracy overall but struggle particularly with questions requiring deep knowledge of Italian history, literature, and civic institutions. The results demonstrate that Italian-specific tasks from native sources provide more discriminating evaluation than translated English benchmarks. The benchmark reveals a performance hierarchy where larger commercial models generally outperform smaller open-source ones, but no model achieves the level of cultural competence expected of human candidates for public positions.

## Conclusions

ITALIC serves both as an evaluation benchmark and a roadmap for future research in culturally aware NLP for Italian. Limitations include the focus on multiple-choice format (which may not capture generative cultural competence) and the reliance on public exam questions that may become contaminated in future model training data. Future work includes developing generative cultural evaluation tasks, expanding domain coverage, tracking model progress over time, and extending the methodology to other languages with similar cultural assessment needs.

## Artifact Contributions

- **ITALIC Dataset**: 10,000 Italian culture-aware multiple-choice questions across 12 domains (https://italicbench.it/, https://doi.org/10.5281/zenodo.14725822)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Directly evaluates cultural knowledge and values specific to Italy across diverse domains including civic education, history, and literature.

## Tags

