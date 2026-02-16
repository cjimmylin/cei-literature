---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0746
type: conferencePaper
short_title: "A Systematic Study of Position Bias in LLM-as-a-Judge"
year: 2025
first_author: "[[Shi, Lin]]"
last_author: "[[Vosoughi, Soroush]]"
authors: "[[Shi, Lin]]; [[Ma, Chiyu]]; [[Liang, Wenhua]]; [[Diao, Xingjian]]; [[Ma, Weicheng]]; [[Vosoughi, Soroush]]"
authors_incomplete: false
url: "https://aclanthology.org/2025.ijcnlp-long.18.pdf"
external_pdf: "https://arxiv.org/pdf/2406.07791v9.pdf"
publication: "ACL Anthology"
pdf_extract: "PDF Extracts/2025/2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge.md"
local_pdf: "[[PDFs/2025/2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Japanese"
cultures_nationalities_list: "Japanese"
languages_list: "English, Japanese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "Claude, Claude-3, Claude-3-Haiku, Claude-3-Opus, Claude-3-Sonnet, Claude-3.5-Sonnet, GPT-3, GPT-3.5, GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, GPT-4o, Gemma, Llama, Llama 3.1, Llama-3.1, Llama-3.3, Qwen2.5, alpaca, chatglm-6b, claude-instant, dolly, falcon-40b, t5-3b, vicuna"
DATA_URL: NA
tags: 
abstract: "LLM-as-a-Judge has emerged as a promising alternative to human evaluators across various tasks, yet inherent biases—particularly position bias, the tendency to favor solutions based on their position within the prompt—compromise its reliability. This exploratory study evaluates position bias in LLM judges across pairwise and list-wise comparison settings, introducing three metrics: repetition stability, position consistency, and preference fairness."
ethics_perspective: "Bias & Fairness"
---
# A Systematic Study of Position Bias in LLM-as-a-Judge

## Authors

[[Shi, Lin]], [[Ma, Chiyu]], [[Liang, Wenhua]], [[Diao, Xingjian]], [[Ma, Weicheng]], [[Vosoughi, Soroush]]

## Metadata

**Authors:** Lin Shi; Chiyu Ma; Wenhua Liang; Xingjian Diao; Weicheng Ma; Soroush Vosoughi

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** English, Japanese

## Links

- **URL:** https://aclanthology.org/2025.ijcnlp-long.18.pdf

## Abstract


LLM-as-a-Judge has emerged as a promising alternative to human evaluators across various tasks, yet inherent biases—particularly position bias, the tendency to favor solutions based on their position within the prompt—compromise its reliability. This exploratory study evaluates position bias in LLM judges across pairwise and list-wise comparison settings, introducing three metrics: repetition stability, position consistency, and preference fairness. Our experiments, involving 15 LLM judges across MTBench and DevBench with 22 tasks and approximately 40 solution-generating models, result in over 150,000 evaluation instances. We identify Judge-Level, Candidate-Level, and TaskLevel factors contributing to bias. The findings confirm that position bias is not due to random chance and varies significantly across judges and tasks. While position bias is weakly influenced by the length of prompt components, it is strongly affected by the quality gap between solutions. Our agreement and disagreement analysis among judges further provides insights into the distribution of judging difficulty across the dataset, and highlights the potential for dataset modifications.

## Data Description

Backfill summary: Models assessed include Claude, Claude-3, Claude-3-Haiku, Claude-3-Opus, Claude-3-Sonnet, Claude-3.5-Sonnet, GPT-3, GPT-3.5, GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, GPT-4o, Gemma, Llama, Llama 3.1, Llama-3.1, Llama-3.3, Qwen2.5, alpaca, chatglm-6b, claude-instant, dolly, falcon-40b, t5-3b, vicuna. No high-confidence repository-style data URL was identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent C2
**Relevance:** Relevant to Japanese, English; bias/fairness focus

## Tags

