---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0057
type: conferencePaper
short_title: "GAMEBoT: Transparent Assessment of LLM Reasoning in Games"
year: 2025
first_author: "[[Unknown]]"
authors: Unknown
url: "https://arxiv.org/abs/2412.13602"
external_pdf: "https://arxiv.org/pdf/2412.13602.pdf"
local_pdf: "[[PDFs/2025-Unknown-GAMEBoT Transparent Assessment of LLM Reasoning in Games.pdf]]"
pdf_extract: "PDF Extracts/2025-Unknown-GAMEBoT Transparent Assessment of LLM Reasoning in Games.md"
publication: ACL 2025
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Large Language Models (LLMs) are increasingly deployed in real-world applications that demand complex reasoning. To track progress, robust benchmarks are required to evaluate their capabilities beyond superficial pattern recognition. However, current LLM reasoning benchmarks often face challenges such as insufficient interpretability, performance saturation or data contamination. To address these challenges, we introduce GAMEBOT (GAME Battle of Tactics), a gaming arena designed for rigorous and..."
research_topic: "Interpretability & Explainability"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# GAMEBoT: Transparent Assessment of LLM Reasoning in Games

## Authors

[[Unknown]]

## Metadata

**Authors:** Unknown

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2412.13602
- **Code/Data:** https://github.com/Visual-AI/GAMEBoT

## Abstract

Large Language Models (LLMs) are increasingly deployed in real-world applications that demand complex reasoning. To track progress, robust benchmarks are required to evaluate their capabilities beyond superficial pattern recognition. However, current LLM reasoning benchmarks often face challenges such as insufficient interpretability, performance saturation or data contamination. To address these challenges, we introduce GAMEBOT (GAME Battle of Tactics), a gaming arena designed for rigorous and transparent assessment of LLM reasoning capabilities. GAMEBOT decomposes complex reasoning in games into predefined modular subproblems. This decomposition allows us to design a suite of Chain-ofThought (CoT) prompts that leverage domain knowledge to guide LLMs in addressing these subproblems before action selection. Furthermore, we develop a suite of rule-based algorithms to generate ground truth for these subproblems, enabling rigorous validation of the LLMs’ intermediate reasoning steps. This approach facilitates evaluation of both the quality of final actions and the accuracy of the underlying reasoning process. GAMEBOT also naturally alleviates the risk of data contamination through dynamic games and head-to-head LLM competitions. We benchmark 17 prominent LLMs across eight games, encompassing various strategic abilities and game characteristics. Our results suggest that GAMEBOT presents a significant challenge, even when LLMs are provided with detailed CoT prompts. Project page: https://visual-ai.github.io/gamebot

## Dataset Information

8 games (including Pong, TicTacToe, Texas Hold'em, etc.); dynamic game-based evaluation with CoT prompts and rule-based ground truth generation

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

