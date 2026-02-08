---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0143
type: conferencePaper
short_title: "ALI-Agent -- Assessing LLMs' Alignment with Human Values via Agent-based Evaluation"
year: 2024
first_author: "[[S. Zheng]]"
authors: Zheng, S., Wang, Z., et al
url: "https://arxiv.org/abs/2405.14125"
external_pdf: "https://arxiv.org/pdf/2405.14125.pdf"
local_pdf: "[[PDFs/2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via.pdf]]"
pdf_extract: "PDF Extracts/2024-Zheng-ALI-Agent - Assessing LLMs' Alignment with Human Values via.md"
publication: NeurIPS 2024
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Large Language Models (LLMs) can elicit unintended and even harmful content when misaligned with human values, posing severe risks to users and society. To mitigate these risks, current evaluation benchmarks predominantly employ expertdesigned contextual scenarios to assess how well LLMs align with human values. However, the labor-intensive nature of these benchmarks limits their test scope, hindering their ability to generalize to the extensive variety of open-world use cases and identify rare..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# ALI-Agent -- Assessing LLMs' Alignment with Human Values via Agent-based Evaluation

## Authors

[[Zheng, S., Wang, Z., et al]]

## Metadata

**Authors:** Zheng, S., Wang, Z., et al

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2405.14125
- **Code/Data:** https://github.com/SophieZheng998/ALI-Agent

## Abstract

Large Language Models (LLMs) can elicit unintended and even harmful content when misaligned with human values, posing severe risks to users and society. To mitigate these risks, current evaluation benchmarks predominantly employ expertdesigned contextual scenarios to assess how well LLMs align with human values. However, the labor-intensive nature of these benchmarks limits their test scope, hindering their ability to generalize to the extensive variety of open-world use cases and identify rare but crucial long-tail risks. Additionally, these static tests fail to adapt to the rapid evolution of LLMs, making it hard to evaluate timely alignment issues. To address these challenges, we propose ALI-Agent, an evaluation framework that leverages the autonomous abilities of LLM-powered agents to conduct in-depth and adaptive alignment assessments. ALI-Agent operates through two principal stages: Emulation and Refinement. During the Emulation stage, ALIAgent automates the generation of realistic test scenarios. In the Refinement stage, it iteratively refines the scenarios to probe long-tail risks. Specifically, ALI-Agent incorporates a memory module to guide test scenario generation, a tool-using module to reduce human labor in tasks such as evaluating feedback from target LLMs, and an action module to refine tests. Extensive experiments across three aspects of human values–stereotypes, morality, and legality–demonstrate that ALI-Agent, as a general evaluation framework, effectively identifies model misalignment. Systematic analysis also validates that the generated test scenarios represent meaningful use cases, as well as integrate enhanced measures to probe long-tail risks. Our code is available at https://github.com/SophieZheng998/ALI-Agent.git.

## Dataset Information

Tests across three aspects of human values: stereotypes (DecodingTrust, CrowS-Pairs), morality (ETHICS, Social Chemistry 101), and legality (Singapore RTSR, AdvBench)

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4
**Implementation Readiness:** HIGH

## Tags

