---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0526
type: preprint
short_title: "MedBench-IT: A Comprehensive Benchmark for Evaluating LLMs on Italian Medical Entrance Examinations"
year: 2025
first_author: "[[Ruggero Marino Lazzaroni]]"
last_author: "[[Roberto Marras]]"
authors: "Ruggero Marino Lazzaroni; Alessandro Angioi; Michelangelo Puliga; Davide Sanna; Roberto Marras"
url: "https://arxiv.org/abs/2509.07135"
external_pdf: "https://arxiv.org/pdf/2509.07135.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Lazzaroni-MedBench-IT A Comprehensive Benchmark for Evaluating LLMs on Italian.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Lazzaroni-MedBench-IT A Comprehensive Benchmark for Evaluating LLMs on Italian.pdf]]"
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
LLM_assessed: "Claude, DeepSeek, GPT-3.5, GPT-4, GPT-4o, GPT-4o mini, Gemma-2, Llama-3, Mistral, Phi-3, Qwen-2, o1"
DATA_URL: NA
tags: 
abstract: "Large language models (LLMs) show increasing potential in education, yet benchmarks for non-English languages in specialized domains remain scarce. We introduce MedBench-IT, the first comprehensive benchmark for evaluating LLMs on Italian medical university entrance examinations. Sourced from Edizioni Simone, a leading preparatory materials publisher, MedBench-IT comprises 17,410 expert-written multiple-choice questions across six subjects (Biology, Chemistry, Logic, General Culture,..."
ethics_perspective: "Bias & Fairness"
authors_incomplete: false
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
---
# MedBench-IT: A Comprehensive Benchmark for Evaluating LLMs on Italian Medical Entrance Examinations

## Authors

[[Ruggero Marino Lazzaroni]], [[Alessandro Angioi]], [[Michelangelo Puliga]], [[Davide Sanna]], [[Roberto Marras]]

## Metadata

**Authors:** Ruggero Marino Lazzaroni, Alessandro Angioi, Michelangelo Puliga, Davide Sanna, Roberto Marras

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Italian

**Benchmark:** MedBench-IT

## Links

- **arXiv:** https://arxiv.org/abs/2509.07135

## Abstract

First comprehensive benchmark for evaluating LLMs on Italian medical university entrance exams, comprising 17,410 expert-written multiple-choice questions across six subjects and three difficulty levels.

## Summary

This paper introduces MedBench-IT, the first comprehensive benchmark for evaluating LLMs on Italian medical university entrance examinations, comprising 17,410 expert-written multiple-choice questions. Sourced from Edizioni Simone, a leading preparatory materials publisher, the benchmark spans six subjects (Biology, Chemistry, Logic, General Culture, Physics, Mathematics) across three difficulty levels corresponding to actual Italian medical entrance exam tiers. The benchmark addresses the scarcity of non-English specialized domain evaluation resources and provides a rigorous assessment tool for LLM performance in Italian medical education contexts.

## Data Description

Introduces MedBench-IT, the first comprehensive benchmark for evaluating LLMs on Italian medical university entrance examinations, comprising 17,410 expert-written multiple-choice questions across six subjects and three difficulty levels. Focuses on benchmark creation for medical domain evaluation.


## Detailed Summary

This paper introduces MedBench-IT, the first comprehensive benchmark for evaluating LLMs on Italian medical university entrance examinations. Sourced from Edizioni Simone, a leading Italian publisher of preparatory materials, MedBench-IT comprises 17,410 expert-written multiple-choice questions spanning six subjects (Biology, Chemistry, Logic, General Culture, Mathematics, Physics) and three difficulty levels, mirroring the structure of actual Italian medical admissions tests. The evaluation encompasses diverse models including proprietary LLMs (GPT-4o, Claude series) and resource-efficient open-source alternatives under 30 billion parameters, with a focus on practical deployability in Italian organizational contexts. Beyond standard accuracy assessment, the study conducts rigorous reproducibility tests (88.86% response consistency), ordering bias analysis (finding minimal impact), and reasoning prompt evaluation. The study also examines correlations between question readability and model performance, finding a statistically significant but small inverse relationship. MedBench-IT distinguishes itself from general Italian benchmarks through its specialized medical focus, large corpus size, detailed subject/difficulty breakdowns, and comprehensive robustness analyses.

## Paper Outline

1. Introduction - Need for Italian-specific medical domain benchmarks
2. Related Work - General and medical LLM benchmarks; Italian NLP resources
3. Dataset Construction - Sourcing from Edizioni Simone; subject and difficulty taxonomy
4. Experimental Setup - Model selection; evaluation protocol; robustness analyses
5. Results - Accuracy, reproducibility, ordering bias, reasoning prompts, readability
6. Discussion - Implications for Italian EdTech and medical education
7. Limitations
8. Conclusion and Future Work

## Methods Summary

The benchmark is constructed from Edizioni Simone's medical entrance exam preparation materials, with 17,410 expert-validated multiple-choice questions organized by six subjects and three difficulty levels. Evaluation uses standard accuracy on the full dataset, plus four in-depth analyses: (1) reproducibility testing across identical runs to measure response consistency; (2) ordering bias analysis with permuted answer choices; (3) comparison of direct prompting versus chain-of-thought reasoning prompts; (4) readability analysis correlating text complexity metrics with model accuracy. Both proprietary (GPT-4o, Claude) and open-source (<30B parameter) models are evaluated.

## Results Summary

Reproducibility testing reveals 88.86% response consistency across identical runs, varying by subject. Ordering bias has minimal impact on model performance. Chain-of-thought reasoning prompts show variable effects depending on model and task complexity. A statistically significant but small inverse relationship exists between question readability and model performance. Proprietary models (GPT-4o, Claude) outperform open-source alternatives, though some smaller models demonstrate practical deployability for Italian educational contexts. Performance varies substantially across subjects and difficulty levels.

## Conclusions

MedBench-IT provides a crucial resource for the Italian NLP community, EdTech developers, and medical education practitioners by establishing a standardized evaluation methodology for LLMs on Italian medical entrance examinations. The comprehensive robustness analyses beyond simple accuracy provide actionable insights into model reliability for high-stakes educational applications.

## Artifact Contributions

- **Benchmark:** MedBench-IT - 17,410 expert-written Italian medical entrance exam questions across 6 subjects and 3 difficulty levels
- **Evaluation Results:** Comprehensive analysis of proprietary and open-source LLMs including reproducibility, ordering bias, and reasoning prompt assessments

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Italian medical domain benchmark. Relevant to healthcare AI ethics and evaluating medical knowledge biases in LLMs.

## Tags

