---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0437
type: preprint
short_title: "COLE: a Comprehensive Benchmark for French Language Understanding Evaluation"
year: 2025
first_author: "[[Beauchemin, David]]"
last_author: "[[Khoury, Richard]]"
authors: "[[Beauchemin, David]]; [[Tremblay, Yan]]; [[Youssef, Mohamed Amine]]; [[Khoury, Richard]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.05046"
external_pdf: "https://arxiv.org/pdf/2510.05046.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding.md"
local_pdf: "[[PDFs/2025/2025-preprint)-COLE a Comprehensive Benchmark for French Language Understanding.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: French
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-4, Claude, Gemini, Llama, Mistral, Qwen, Bloom, CroissantLLM"
DATA_URL: "https://huggingface.co/datasets/graalul/COLE-public"
tags: 
abstract: "To address the need for a more comprehensive evaluation of French Natural Language Understanding (NLU), we introduce COLE, a new benchmark composed of 23 diverse task covering a broad range of NLU capabilities, including sentiment analysis, paraphrase detection, grammatical judgment, and reasoning, with a particular focus on linguistic phenomena relevant to the French language. We benchmark 95 large language models (LLM), providing an extensive analysis of the current state of French NLU."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# COLE: a Comprehensive Benchmark for French Language Understanding Evaluation

## Authors

[[Beauchemin, David]], [[Tremblay, Yan]], [[Youssef, Mohamed Amine]], [[Khoury, Richard]]

## Metadata

**Authors:** Beauchemin, David; Tremblay, Yan; Youssef, Mohamed Amine; Khoury, Richard

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French

**Benchmark:** COLE

## Links

- **arXiv:** https://arxiv.org/abs/2510.05046

## Abstract

Comprehensive French NLU benchmark of 23 diverse tasks covering sentiment analysis, paraphrase detection, grammatical judgment, and reasoning. Evaluated 94 LLMs, highlighting a significant performance gap between closed- and open-weights models. Includes focus on understanding of regional language variations.

## Summary

This paper introduces COLE, a comprehensive benchmark for French Natural Language Understanding comprising 23 diverse tasks spanning sentiment analysis, paraphrase detection, grammatical judgment, and reasoning, with particular focus on linguistic phenomena relevant to French including regional language variations. Evaluating 95 large language models (including GPT-4, Claude, Gemini, Llama, Mistral, Qwen, Bloom, and CroissantLLM), the study provides an extensive analysis of the current state of French NLU and reveals a significant performance gap between closed-source frontier models and open-weight alternatives.

## Data Description

COLE is a comprehensive French NLU benchmark of 23 diverse tasks covering sentiment analysis, paraphrase detection, grammatical judgment, and reasoning. Evaluated 94 LLMs (note: abstract says 95), highlighting a significant performance gap between closed- and open-weights models. Includes focus on understanding of regional French language variations.


## Detailed Summary

This paper introduces COLE (COrpus for Langue understanding Evaluation), a comprehensive French Natural Language Understanding (NLU) benchmark comprising 23 diverse tasks designed to address the limitations of the existing FLUE benchmark, which lacks task diversity and misses typical NLU tasks such as textual entailment, idiom comprehension, QA, and paraphrase detection. COLE is developed by the Group for Research in Artificial Intelligence at Universite Laval (Quebec, Canada) and covers a broad spectrum of NLU capabilities including sentiment analysis, paraphrase detection, grammatical judgment, reasoning, and linguistic phenomena particularly relevant to French -- such as rich morphology, grammatical gender, complex syntactic structures, and regional language variations. The benchmark evaluates 95 LLMs (including GPT-4, Claude, Gemini, Llama, Mistral, Qwen, Bloom, and CroissantLLM), providing the most extensive analysis of French NLU to date. Key findings highlight a significant performance gap between closed-source and open-weight models, and identify challenging frontiers including zero-shot extractive QA, fine-grained word sense disambiguation, and understanding of regional French language variations.

## Paper Outline

1. Introduction - Limitations of existing French NLU benchmarks (FLUE)
2. Related Work - GLUE, SuperGLUE, FLUE, CLUE, and other language-specific benchmarks
3. Task Descriptions - 23 tasks across multiple NLU categories
4. Experimental Setup - Model selection, evaluation protocol, prompting strategies
5. Results and Discussion - Performance analysis across 95 LLMs
6. Conclusion and Future Work

## Methods Summary

COLE aggregates 23 carefully curated tasks into a unified evaluation framework, organized into categories including text classification (sentiment analysis), sentence-pair understanding (paraphrase detection, NLI), linguistic phenomena (grammatical judgment, word sense disambiguation), reasoning, and QA. Tasks are selected to cover French-specific linguistic challenges not addressed by FLUE. The benchmark is released as a public resource on Hugging Face. Evaluation uses standardized prompting across all 95 models with consistent evaluation metrics per task category.

## Results Summary

The evaluation of 95 LLMs reveals: (1) a significant performance gap between closed-source frontier models and open-weight alternatives on French NLU; (2) zero-shot extractive QA remains a key challenging frontier for current LLMs in French; (3) fine-grained word sense disambiguation poses particular difficulties, likely due to the polysemy and context-dependence of French vocabulary; (4) understanding of regional French language variations (e.g., Quebec French, African French) represents a largely unaddressed challenge; (5) French-specific linguistic phenomena including grammatical gender agreement and complex morphology create evaluation dimensions not captured by translated English benchmarks.

## Conclusions

COLE establishes a new standard for French NLU evaluation by providing comprehensive task coverage that addresses the gaps in FLUE. The identification of challenging frontiers (extractive QA, WSD, regional variations) provides clear direction for future French NLP research. The benchmark is released as a public resource to foster progress in French language modeling.

## Artifact Contributions

- **Benchmark:** COLE - 23-task French NLU benchmark (https://huggingface.co/datasets/graalul/COLE-public)
- **Evaluation Results:** Comprehensive analysis of 95 LLMs on French NLU
- **Analysis:** Identification of challenging frontiers for French language understanding

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Most comprehensive French-specific LLM evaluation benchmark with 94 models tested. Relevant for understanding regional French variation and model limitations.

## Tags
