---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0257
type: conferencePaper
short_title: "MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables"
year: 2025
first_author: "[[Marcuzzo, Matteo]]"
last_author: "[[Pilehvar, Mohammad Taher]]"
authors: "[[Marcuzzo, Matteo]]; [[Zangari, Alessandro]]; [[Albarelli, Andrea]]; [[Camacho-Collados, Jose]]; [[Pilehvar, Mohammad Taher]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2509.12371"
external_pdf: "https://arxiv.org/pdf/2509.12371.pdf"
local_pdf: "[[PDFs/2025/2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs.md"
publication: EMNLP
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
abstract: "As LLMs excel on standard reading comprehension benchmarks, attention is shifting toward evaluating their capacity for complex abstract reasoning and inference. Literaturebased benchmarks, with their rich narrative and moral depth, provide a compelling framework for evaluating such deeper comprehension skills. Here, we present MORABLES, a humanverified benchmark built from fables and short stories drawn from historical literature."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Gemini, Llama-3, Mistral, Mixtral, Qwen, DeepSeek, o3"
DATA_URL: "https://huggingface.co/datasets/cardiffnlp/Morables"
---
# MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables

## Authors

[[Marcuzzo, Matteo]], [[Zangari, Alessandro]], [[Albarelli, Andrea]], [[Camacho-Collados, Jose]], [[Pilehvar, Mohammad Taher]]

## Metadata

**Authors:** Marcuzzo, Matteo; Zangari, Alessandro; Albarelli, Andrea; Camacho-Collados, Jose; Pilehvar, Mohammad Taher

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP

## Links

- **arXiv:** https://arxiv.org/abs/2509.12371

## Abstract

As LLMs excel on standard reading comprehension benchmarks, attention is shifting toward evaluating their capacity for complex abstract reasoning and inference. Literaturebased benchmarks, with their rich narrative and moral depth, provide a compelling framework for evaluating such deeper comprehension skills. Here, we present MORABLES, a humanverified benchmark built from fables and short stories drawn from historical literature. The main task is structured as multiple-choice questions targeting moral inference, with carefully crafted distractors that challenge models to go beyond shallow, extractive question answering. To further stress-test model robustness, we introduce adversarial variants designed to surface LLM vulnerabilities and shortcuts due to issues such as data contamination. Our findings show that, while larger models outperform smaller ones, they remain susceptible to adversarial manipulation and often rely on superficial patterns rather than true moral reasoning. This brittleness results in significant self-contradiction, with the best models refuting their own answers in roughly 20% of cases depending on the framing of the moral choice. Interestingly, reasoning-enhanced models fail to bridge this gap, suggesting that scale – not reasoning ability – is the primary driver of performance.

## Dataset Information

Literature-based benchmark using fables for abstract moral reasoning, includes adversarial variants

## Data Description

MORABLES is a human-verified benchmark of 709 fables and short stories from historical literature, structured as multiple-choice questions targeting moral inference with carefully crafted distractors. Eleven LLMs are evaluated including Mistral 7B, Llama 3.1 8B, Qwen 2.5 7B, Mixtral 8x22B, Llama 3.3 70B, DeepSeek V3, GPT-4o, Gemini 2.0 Flash, Claude 3.5 Sonnet, GPT-o3-mini, and DeepSeek R1, with adversarial variants (character swaps, trait injection, tautology injection) and alternative evaluation procedures (NOTO, True/False).

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

