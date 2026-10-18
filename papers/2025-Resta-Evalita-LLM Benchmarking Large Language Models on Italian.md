---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0503
type: preprint
short_title: "Evalita-LLM: Benchmarking Large Language Models on Italian"
year: 2025
first_author: "[[Magnini, Bernardo]]"
last_author: "[[Patti, Viviana]]"
authors: "Magnini, Bernardo; Zanoli, Roberto; Resta, Michele; Cimmino, Martin; Albano, Paolo; Madeddu, Marco; Patti, Viviana"
authors_incomplete: false
url: "https://arxiv.org/abs/2502.02289"
external_pdf: "https://arxiv.org/pdf/2502.02289.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Resta-Evalita-LLM Benchmarking Large Language Models on Italian.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Resta-Evalita-LLM Benchmarking Large Language Models on Italian.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Italian
cultures_nationalities_list: Italian
languages_list: Italian
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: NA
DATA_URL: "https://huggingface.co/spaces/evalita-llm"
tags: 
abstract: "We describe Evalita-LLM, a new benchmark designed to evaluate Large Language Models (LLMs) on Italian tasks. The distinguishing and innovative features of Evalita-LLM are the following: (i) all tasks are native Italian, avoiding issues of translating from Italian and potential cultural biases; (ii) in addition to well established multiple-choice tasks, the benchmark includes generative tasks, enabling more natural interaction with LLMs; (iii) all tasks are evaluated against multiple prompts,..."
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Translation"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 30
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IT
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 69
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
---
# Evalita-LLM: Benchmarking Large Language Models on Italian

## Authors

[[Magnini, Bernardo]], [[Zanoli, Roberto]], [[Resta, Michele]], [[Cimmino, Martin]], [[Albano, Paolo]], [[Madeddu, Marco]], [[Viviana Patti|Patti, Viviana]]

## Metadata

**Authors:** Magnini, Bernardo; Zanoli, Roberto; Resta, Michele; Cimmino, Martin; Albano, Paolo; Madeddu, Marco; Patti, Viviana

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Italian

**Benchmark:** Evalita-LLM

## Links

- **arXiv:** https://arxiv.org/abs/2502.02289
- **Code/Data:** https://huggingface.co/spaces/evalita-llm

## Abstract

Comprehensive benchmark and leaderboard designed to evaluate LLMs on Italian tasks, covering ten native Italian tasks including both multiple-choice and generative formats, with multiple prompts per task to mitigate sensitivity. All tasks are native Italian, avoiding translation biases.

## Summary

This paper presents Evalita-LLM, a comprehensive benchmark for evaluating LLMs on ten native Italian tasks spanning word sense disambiguation, text classification, question answering, information extraction, and summarization. The benchmark addresses critical issues in translated benchmarks including translation quality, cultural content bias, and stylistic limitations by using only native Italian datasets from the Evalita initiative. The methodology employs multiple prompts per task to mitigate model sensitivity and includes both multiple-choice and generative task formats, providing a leaderboard for 23 open-source models including Llama-3.1, Gemma-2, Mistral, and Italian-specific models like Minerva and Zefiro.

## Data Description

Evalita-LLM: a benchmark of 10 native Italian NLP tasks (word disambiguation, textual entailment, sentiment analysis, hate speech, FAQ QA, medical admission tests, lexical substitution, NER, relation extraction, summarization) compiled from existing Evalita campaign datasets, released on HuggingFace.


## Detailed Summary

This paper describes Evalita-LLM, a new benchmark designed to evaluate LLMs on native Italian tasks, addressing critical limitations of existing evaluation practices where Italian models are primarily tested on benchmarks automatically translated from English. The benchmark features three key innovations: (1) all tasks are native Italian, avoiding translation quality issues and cultural biases inherent in translated benchmarks; (2) the benchmark includes both multiple-choice and generative tasks, enabling more natural interaction with LLMs compared to the predominant multiple-choice paradigm; and (3) all tasks are evaluated against multiple prompts, mitigating model sensitivity to specific prompt formulations and enabling fairer comparisons.

The benchmark comprises 10 tasks selected from the Evalita initiative (the Italian Association for Computational Linguistics' evaluation campaigns) and other sources, covering diverse linguistic phenomena, genres, and applications including word sense disambiguation, text classification, question answering, information extraction, and summarization. The authors employ an iterative validation methodology where candidate tasks and prompts are tested against a set of development LLMs before inclusion. The benchmark addresses important methodological issues including generative task evaluation challenges, multiple-prompt evaluation for fairness, and dataset saturation concerns where models may have seen benchmark data during pre-training. Twenty-three open-source models are evaluated, including Llama-3.1, Gemma-2, Mistral, Qwen-2.5, Aya-Expanse, and Italian-specific models like Minerva-3B and Zefiro.

## Paper Outline

1. Introduction - Issues with translated benchmarks for Italian
2. Methodology - Iterative validation process for task and prompt selection
3. Evalita-LLM Tasks - Ten tasks spanning multiple NLP competencies
4. Evaluation Metrics - Accuracy, F1, and ROUGE for different task types
5. Experimental Setup - Development and evaluation models
6. Results - Performance statistics for state-of-the-art LLMs
7. Conclusion

## Methods Summary

Tasks are drawn from the Evalita evaluation campaigns and implemented using the lm-evaluation-harness library. The development follows an iterative validation process: candidate datasets are selected from ELG, converted to HuggingFace format, and tasks are defined with prompt design, pre/post-processing, and evaluation metrics. Candidate tasks and prompts are validated against development LLMs, with tasks that prove too complex or prompts that fail to elicit meaningful responses being refined or discarded. Six tasks are implemented as multiple-choice (using logits for option selection) and four as generative (using generate-until). Each task uses multiple prompts to assess model sensitivity. Metrics include accuracy for multiple-choice tasks, F1 for classification/extraction, and ROUGE for summarization.

## Results Summary

The evaluation of 23 open-source LLMs reveals variation across tasks and model families. Italian-specific models (Minerva, Zefiro) show advantages on culturally-specific tasks but not universally. The multiple-prompt evaluation methodology reveals significant prompt sensitivity across models, with performance varying substantially depending on prompt formulation -- highlighting the unfairness of single-prompt evaluation. Generative tasks prove more challenging than multiple-choice for most models, with output formatting issues contributing to lower scores. The benchmark establishes reference performance levels for Italian LLM evaluation and demonstrates that native Italian tasks provide more meaningful assessment than translated English benchmarks.

## Conclusions

Evalita-LLM provides a methodologically sound, native Italian benchmark that avoids the translation quality, cultural bias, and stylistic issues of translated benchmarks. Limitations include the current coverage of 10 tasks (expandable in future releases) and the focus on instruction-tuned models without fine-tuning evaluation. Future work includes adding more tasks from the Evalita campaigns, integrating with other Italian benchmark initiatives (Ita-bench, Calamita), and investigating dataset saturation and prompt contamination effects more systematically.

## Artifact Contributions

- **Evalita-LLM Benchmark**: Ten native Italian NLP evaluation tasks with multiple prompts (https://huggingface.co/spaces/evalita-llm)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Major Italian LLM benchmark with native Italian tasks; avoids cultural biases from translation; includes leaderboard for 23 open-source models.

## Tags

