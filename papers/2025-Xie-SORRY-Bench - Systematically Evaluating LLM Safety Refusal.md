---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0116
type: conferencePaper
short_title: SORRY-Bench -- Systematically Evaluating LLM Safety Refusal
year: 2025
first_author: "[[T. Xie]]"
last_author: "[[T. Xie]]"
authors: Xie, T., et al
authors_incomplete: true
url: "https://arxiv.org/abs/2406.14598"
external_pdf: "https://arxiv.org/pdf/2406.14598.pdf"
local_pdf: "[[PDFs/2025/2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal.md"
publication: ICLR 2025
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
abstract: "Evaluating aligned large language models’ (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts, however, face three limitations that we address with SORRYBench, our proposed benchmark. First, existing methods often use coarse-grained taxonomies of unsafe topics, and are over-representing some fine-grained topics. For example, among the ten existing datasets that we evaluated, tests for refusals of self-harm..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# SORRY-Bench -- Systematically Evaluating LLM Safety Refusal

## Authors

[[T. Xie]]

## Metadata

**Authors:** Xie, T., et al

**Year:** 2025

**Type:** conferencePaper

**Venue:** ICLR 2025

## Links

- **arXiv:** https://arxiv.org/abs/2406.14598
- **Code/Data:** https://github.com/SORRY-Bench/sorry-bench

## Abstract

Evaluating aligned large language models’ (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts, however, face three limitations that we address with SORRYBench, our proposed benchmark. First, existing methods often use coarse-grained taxonomies of unsafe topics, and are over-representing some fine-grained topics. For example, among the ten existing datasets that we evaluated, tests for refusals of self-harm instructions are over 3x less represented than tests for fraudulent activities. SORRY-Bench improves on this by using a fine-grained taxonomy of 44 potentially unsafe topics, and 440 class-balanced unsafe instructions, compiled through humanin-the-loop methods. Second, linguistic characteristics and formatting of prompts are often overlooked, like different languages, dialects, and more – which are only implicitly considered in many evaluations. We supplement SORRY-Bench with 20 diverse linguistic augmentations to systematically examine these effects. Third, existing evaluations rely on large LLMs (e.g., GPT-4) for evaluation, which can be computationally expensive. We investigate design choices for creating a fast, accurate automated safety evaluator. By collecting 7K+ human annotations and conducting a meta-evaluation of diverse LLM-as-a-judge designs, we show that fine-tuned 7B LLMs can achieve accuracy comparable to GPT-4 scale LLMs, with lower computational cost. Putting these together, we evaluate over 50 proprietary and open-weight LLMs on SORRY-Bench, analyzing their distinctive safety refusal behaviors. We hope our effort provides a building block for systematic evaluations of LLMs’ safety refusal capabilities, in a balanced, granular, and efficient manner.

## Dataset Information

440 class-balanced unsafe instructions (base set)

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4, Agent 16
**Implementation Readiness:** HIGH

## Tags

