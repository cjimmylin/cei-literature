---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0057
type: conferencePaper
short_title: "GAMEBoT: Transparent Assessment of LLM Reasoning in Games"
year: 2025
first_author: "[[Wenye Lin]]"
last_author: "[[Kai Han]]"
authors: "Wenye Lin; Jonathan Roberts; Yunhan Yang; Samuel Albanie; Zongqing Lu; Kai Han"
url: "https://arxiv.org/abs/2412.13602"
external_pdf: "https://arxiv.org/pdf/2412.13602.pdf"
pdf_extract: "PDF Extracts/2025/2025-Lin-GAMEBoT Transparent Assessment of LLM Reasoning in Games.md"
local_pdf: "[[PDFs/2025/2025-Lin-GAMEBoT Transparent Assessment of LLM Reasoning in Games.pdf]]"
publication: "ACL 2025"
CONF-CC: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
abstract: "Large Language Models (LLMs) are increasingly deployed in real-world applications that demand complex reasoning. To track progress, robust benchmarks are required to evaluate their capabilities beyond superficial pattern recognition. However, current LLM reasoning benchmarks often face challenges such as insufficient interpretability, performance saturation or data contamination. To address these challenges, we introduce GAMEBOT (GAME Battle of Tactics), a gaming arena designed for rigorous and..."
LLM_assessed: "Claude, Claude-3, GPT-4, GPT-4o, GPT-4o mini, Gemini, Llama-3, Mistral"
DATA_URL: "https://visual-ai.github.io/gamebot"
CONFERENCE: "ACL 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 5
research_topic: "Interpretability & Explainability"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# GAMEBoT: Transparent Assessment of LLM Reasoning in Games

## Authors

[[Wenye Lin]], [[Jonathan Roberts]], [[Yunhan Yang]], [[Samuel Albanie]], [[Zongqing Lu]], [[Kai Han]]

## Metadata

**Authors:** Wenye Lin; Jonathan Roberts; Yunhan Yang; Samuel Albanie; Zongqing Lu; Kai Han

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

## Data Description

GAMEBoT is a gaming arena benchmark for evaluating LLM reasoning capabilities across eight competitive games (Othello, Pong, Surround, Checkers, TicTacToe, Connect4, Texas Hold'em, Negotiation v2). The benchmark evaluates 17 prominent LLMs through 20-match head-to-head competitions, assessing both final game outcomes and intermediate reasoning steps using rule-based ground truth verification. Each game decomposes complex decisions into modular subproblems with chain-of-thought prompts.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

