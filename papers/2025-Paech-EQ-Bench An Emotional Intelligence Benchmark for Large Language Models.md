---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0047
type: preprint
short_title: "EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models"
year: 2025
first_author: "[[Samuel J. Paech]]"
last_author: "[[Samuel J. Paech]]"
authors: "Samuel J. Paech"
url: "https://arxiv.org/abs/2312.06281"
external_pdf: "https://arxiv.org/pdf/2312.06281.pdf"
pdf_extract: "PDF Extracts/2025/2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models.md"
local_pdf: "[[PDFs/2025/2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "We introduce EQ-Bench, a novel benchmark designed to evaluate aspects of emotional intelligence in Large Language Models (LLMs). We assess the ability of LLMs to understand complex emotions and social interactions by asking them to predict the intensity of emotional states of characters in a dialogue. The benchmark is able to discriminate effectively between a wide range of models. We find that EQ-Bench correlates strongly with comprehensive multi-domain benchmarks like MMLU (Hendrycks et al."
research_topic: "Machine Learning"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, text-davinci, Claude, Llama-2, Mistral, Vicuna, Qwen"
DATA_URL: "https://github.com/EQ-bench/EQ-Bench"
---
# EQ-Bench: An Emotional Intelligence Benchmark for Large Language Models

## Authors

[[Samuel J. Paech]]

## Metadata

**Authors:** Samuel J. Paech

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2312.06281
- **Code/Data:** https://github.com/EQ-bench/EQ-Bench](https://github.com/EQ-bench/EQ-Bench; https://huggingface.co/datasets/pbevan11/EQ-Bench

## Abstract

We introduce EQ-Bench, a novel benchmark designed to evaluate aspects of emotional intelligence in Large Language Models (LLMs). We assess the ability of LLMs to understand complex emotions and social interactions by asking them to predict the intensity of emotional states of characters in a dialogue. The benchmark is able to discriminate effectively between a wide range of models. We find that EQ-Bench correlates strongly with comprehensive multi-domain benchmarks like MMLU (Hendrycks et al., 2020) (r=0.97), indicating that we may be capturing similar aspects of broad intelligence. Our benchmark produces highly repeatable results using a set of 60 English-language questions. We also provide open-source code for an automated benchmarking pipeline at https://github.com/EQ-bench/EQ-Bench and a leaderboard at https://eqbench.com.

## Dataset Information

60 English-language questions; dialogue-based emotion intensity prediction tasks; models predict intensity of 4 emotional states per question on a 0-1 scale

## Data Description

The paper introduces EQ-Bench, a benchmark for assessing emotional understanding in LLMs using 60 English-language questions. Each question presents a GPT-4-generated dialogue depicting conflict or tension, asking models to rate the intensity of four emotions on a 0-10 scale. The benchmark was tested on 25 models including GPT-4, GPT-3.5 variants, text-davinci models, Claude 2, Llama-2 (7B/13B/70B), Mistral-7B, Vicuna, Qwen, and others, with scores correlating strongly with MMLU (r=0.97).

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** HIGH

## Tags

