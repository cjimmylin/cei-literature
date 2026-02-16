---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0504
type: preprint
short_title: "CALAMITA: Challenging the Abilities of LAnguage Models in ITAlian"
year: 2025
first_author: "[[Over 80 contributors (community initiative)]]"
last_author: "[[Over 80 contributors (community initiative)]]"
authors: "Over 80 contributors (community initiative)"
url: "https://arxiv.org/abs/2512.04759"
external_pdf: "https://arxiv.org/pdf/2512.04759.pdf"
publication: "arXiv / CLiC-it 2024"
pdf_extract: "PDF Extracts/2024/2024-initiative-CALAMITA Challenging the Abilities of LAnguage Models in ITAlian.md"
local_pdf: "[[PDFs/2024/2024-initiative-CALAMITA Challenging the Abilities of LAnguage Models in ITAlian.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Italian"
cultures_nationalities_list: "Italian"
languages_list: Italian
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "ALBERT, BERT, Barth, GPT-2, GPT-4o, Llama, LLAMA3.1, Llama-3, LLaMA-3.1, LLaMA2, Llama 3.1, RoBERTa, llama 3"
DATA_URL: "https://github.com/CALAMITA-AILC/calamita-eval"
tags: 
abstract: 
research_topic: "Other"
---
# CALAMITA: Challenging the Abilities of LAnguage Models in ITAlian

## Authors

[[Over 80 contributors (community initiative)]]

## Metadata

**Authors:** Over 80 contributors (community initiative)

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / CLiC-it 2024

**Languages:** Italian

**Benchmark:** CALAMITA

## Links

- **arXiv:** https://arxiv.org/abs/2512.04759

## Abstract

Large-scale collaborative benchmarking initiative for Italian that federates 80+ contributors. Assembles 20+ tasks and ~100 subtasks covering linguistic competence, commonsense reasoning, factual consistency, fairness, summarization, translation, and code generation.

## Summary

CALAMITA (Challenging the Abilities of LAnguage Models in ITAlian) is a large-scale collaborative benchmarking initiative coordinated by the Italian Association for Computational Linguistics, federating over 80 contributors from 31 institutions including academia, industry, and the public sector. Unlike leaderboard-focused efforts, CALAMITA emphasizes methodology and community-driven evaluation, assembling over 20 tasks and almost 100 subtasks covering linguistic competence, commonsense reasoning, factual consistency, fairness, summarization, translation, and code generation. The initiative establishes a centralized evaluation pipeline supporting heterogeneous datasets and metrics, with results reported for four open-weight LLMs highlighting systematic strengths and weaknesses. Conceived as a rolling benchmark enabling continuous integration of new tasks and models, CALAMITA serves both as the most comprehensive benchmark for Italian to date and as a framework blueprint for sustainable, community-driven LLM evaluation in other languages.

## Data Description

CALAMITA is a large-scale collaborative benchmarking initiative for Italian that federates 80+ contributors. Assembles 20+ tasks and ~100 subtasks covering linguistic competence, commonsense reasoning, factual consistency, fairness, summarization, translation, and code generation. Explicitly includes fairness evaluation as one of its task categories.


## Detailed Summary

CALAMITA (Challenging the Abilities of LAnguage Models in ITAlian) is a large-scale collaborative benchmarking initiative for Italian coordinated under the Italian Association for Computational Linguistics (AILC). Unlike leaderboard-focused efforts, CALAMITA foregrounds methodology and community engagement: it federates over 80 contributors from 31 institutions (academia, industry, public sector) across 10 months from conception to the first workshop. The initiative assembled 22 challenges with almost 100 subtasks covering linguistic competence, commonsense reasoning, factual consistency, fairness, summarization, translation, and code generation. A centralized evaluation pipeline was established supporting heterogeneous datasets and metrics, with models evaluated on the Leonardo supercomputer. CALAMITA is conceived as a rolling benchmark enabling continuous integration of new tasks and models, making it both the most comprehensive benchmark for Italian and a framework blueprint for other languages.

## Paper Outline

1. Introduction and Motivation - Need for Italian-specific LLM evaluation
2. Related Work - Diversity of LLM benchmarks, collaborative initiatives (BIG-bench, HLE, IberoBench)
3. Collaborative Methodology - Pre-proposals, submission process, evaluation pipeline, workshop
4. Challenges - 22 challenge descriptions organized by tested abilities
5. Experiments and Results - Evaluation of four LLMs, aggregated and per-task results
6. Future Directions - Rolling benchmark, integration with EVALITA

## Methods Summary

The collaborative pipeline involves: (1) call for pre-proposals through academic channels (22 of 26 accepted); (2) structured submission requiring technical report, dataset on HuggingFace, and GitHub gist specifying task configuration; (3) centralized evaluation by a dedicated team using the lm-eval-harness framework on the Leonardo HPC cluster; (4) review cycle with proposers to identify and fix implementation issues. Each challenge could include multiple subtasks with different metrics, with proposers choosing a main metric for the leaderboard. The evaluation infrastructure was designed for extensibility, supporting both multiple-choice and open-ended output formats. Four open-weight LLMs were evaluated: LLAMA3.1-8B, ANITA-8B, Minerva-7B-Instruct, and LLaMA-3.1-Instruct-70B.

## Results Summary

Results for four open-weight LLMs reveal systematic strengths and weaknesses across tested abilities. The evaluation exposes methodological lessons: the necessity of fine-grained, task-representative metrics (rather than single averaged scores), the importance of harmonized evaluation pipelines, and both benefits and limitations of broad community engagement. Challenges span diverse categories including domain-specific knowledge, formal reasoning, commonsense reasoning, cognitive/pragmatic abilities, and ethical behavior (including fairness evaluation). The taxonomy-based organization enables identification of general patterns in model behavior across ability categories.

## Conclusions

CALAMITA demonstrates that community-driven evaluation is both feasible and productive for non-English languages, providing a blueprint for other research communities. The initiative's value lies not only in the benchmark itself but in the methodology: a collaborative framework that combines linguistic insight, computational efficiency, and community engagement. The rolling benchmark design ensures sustainability and adaptability to evolving evaluation needs. The inclusion of fairness evaluation among the task categories makes it relevant to ethical AI assessment for Italian.

## Artifact Contributions

- **CALAMITA benchmark**: 22 challenges, ~100 subtasks for Italian LLM evaluation
- **Centralized evaluation pipeline**: Extensible framework based on lm-eval-harness for heterogeneous Italian tasks
- **Collaborative methodology**: Documented process for community-driven benchmark creation
- **Rolling benchmark infrastructure**: Enabling continuous addition of new tasks and model evaluations
- **Published proceedings**: CLiC-it 2024 conference proceedings with all challenge descriptions

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Community-driven Italian LLM benchmark that explicitly includes fairness evaluation as one of its task categories.

## Tags

