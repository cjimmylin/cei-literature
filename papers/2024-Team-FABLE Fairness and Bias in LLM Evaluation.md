---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0173
type: conferencePaper
short_title: "FABLE (Fairness and Bias in LLM Evaluation)"
year: 2024
first_author: "[[KFUPM Research Team]]"
last_author: "[[KFUPM Research Team]]"
authors: "KFUPM Research Team"
publication: Unknown
CONF-CC: "Preprint"
external_pdf: "https://arxiv.org/pdf/2502.05849.pdf"
pdf_extract: "PDF Extracts/2024/2024-Team-FABLE Fairness and Bias in LLM Evaluation.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Team-FABLE Fairness and Bias in LLM Evaluation.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Recent failures such as Google Gemini generating people of color in Nazi-era uniforms illustrate how AI outputs can be factually plausible yet socially harmful. AI models are increasingly evaluated for “fairness,” yet existing benchmarks often conflate two fundamentally different dimensions: factual correctness and normative fairness. A model may generate responses that are factually accurate but socially unfair, or conversely, appear fair while distorting factual reality."
LLM_assessed: "GPT-3.5, GPT-4o, Gemini, Llama-3, Qwen"
DATA_URL: "https://github.com/uclanlp/Fact-or-Fair"
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# FABLE (Fairness and Bias in LLM Evaluation)

## Authors

[[KFUPM Research Team]]

## Metadata

**Authors:** KFUPM Research Team

**Year:** 2024

**Type:** conferencePaper

**Venue:** Unknown

## Links

- **Code/Data:** https://github.com/BRAIN-Lab-AI/FABLE-Fairness-and-Bias-in-LLM-Evaluation

## Abstract

Recent failures such as Google Gemini generating people of color in Nazi-era uniforms illustrate how AI outputs can be factually plausible yet socially harmful. AI models are increasingly evaluated for “fairness,” yet existing benchmarks often conflate two fundamentally different dimensions: factual correctness and normative fairness. A model may generate responses that are factually accurate but socially unfair, or conversely, appear fair while distorting factual reality. We argue that identifying the boundary between fact and fair is essential for meaningful fairness evaluation. We introduce FACT-OR-FAIR, a benchmark with (i) objective queries aligned with descriptive, factbased judgments, and (ii) subjective queries aligned with normative, fairness-based judgments. Our queries are constructed from 19 statistics and are grounded in cognitive psychology, drawing on representativeness bias, attribution bias, and ingroup–outgroup bias to explain why models often misalign fact and fairness. Experiments across ten frontier models reveal different levels of fact-fair trade-offs. By reframing fairness evaluation, we provide both a new theoretical lens and a practical benchmark to advance the responsible model assessments. Our test suite is publicly available at https: //github.com/uclanlp/Fact-or-Fair.

## Dataset Information

156 curated prompts across 4 categories; automated evaluation via toxicity/hate speech classifiers

## Data Description

FACT-OR-FAIR is a benchmark comprising objective (fact-based) and subjective (fairness-based) queries constructed from 19 real-world statistics, designed to disentangle factual correctness from normative fairness in LLM evaluation.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** MEDIUM

## Tags

