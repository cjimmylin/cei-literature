---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0190
type: conferencePaper
short_title: JailbreakBench -- An Open Robustness Benchmark
year: 2024
first_author: "[[P. Chao]]"
authors: Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E
url: "https://arxiv.org/abs/2404.01318"
external_pdf: "https://arxiv.org/pdf/2404.01318.pdf"
local_pdf: "[[PDFs/2024/2024-Chao-JailbreakBench - An Open Robustness Benchmark.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Chao-JailbreakBench - An Open Robustness Benchmark.md"
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
is_dataset: "Yes"
tags: 
abstract: "Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
---
# JailbreakBench -- An Open Robustness Benchmark

## Authors

[[Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E]]

## Metadata

**Authors:** Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G.J., Wong, E

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2404.01318
- **Code/Data:** https://github.com/JailbreakBench/jailbreakbench; https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors

## Abstract

Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not reproducible, as they withhold adversarial prompts, involve closed-source code, or rely on evolving proprietary APIs. To address these challenges, we introduce JailbreakBench, an open-sourced benchmark with the following components: (1) an evolving repository of state-of-the-art adversarial prompts, which we refer to as jailbreak artifacts; (2) a jailbreaking dataset comprising 100 behaviors— both original and sourced from prior work (Zou et al., 2023; Mazeika et al., 2023, 2024)—which align with OpenAI’s usage policies; (3) a standardized evaluation framework at https://github.com/JailbreakBench/jailbreakbench that includes a clearly defined threat model, system prompts, chat templates, and scoring functions; and (4) a leaderboard at https://jailbreakbench.github.io/ that tracks the performance of attacks and defenses for various LLMs. We have carefully considered the potential ethical implications of releasing this benchmark, and believe that it will be a net positive for the community.

## Dataset Information

JBB-Behaviors: 100 distinct misuse behaviors across 10 categories aligned with OpenAI usage policies

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4, Agent 16
**Implementation Readiness:** HIGH

## Tags

