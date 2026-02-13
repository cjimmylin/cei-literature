---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0117
type: conferencePaper
short_title: "SPARC: Evaluating LLMs in Open-Source Games (Strategic Program Analysis for Reciprocal Cooperation)"
year: 2025
first_author: "[[Swadesh Sistla]]"
last_author: "[[Max Kleiman-Weiner]]"
authors: Swadesh Sistla; Max Kleiman-Weiner
url: "https://arxiv.org/abs/2512.00371"
external_pdf: "https://arxiv.org/pdf/2512.00371.pdf"
local_pdf: "[[PDFs/2025/2025-Sistla-SPARC Evaluating LLMs in Open-Source Games Strategic Program Analysis.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Sistla-SPARC Evaluating LLMs in Open-Source Games Strategic Program Analysis.md"
publication: NeurIPS 2025
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
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Large Language Models’ (LLMs) programming capabilities enable their participation in open-source games: a game-theoretic setting in which players submit computer programs in lieu of actions. These programs offer numerous advantages, including interpretability, inter-agent transparency, and formal verifiability; additionally, they enable program equilibria, solutions that leverage the transparency of code and are inaccessible within normal-form settings."
research_topic: "Interpretability & Explainability"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Mistral, Qwen, DeepSeek"
DATA_URL: "https://github.com/swadeshs/llm-osgt"
---
# SPARC: Evaluating LLMs in Open-Source Games (Strategic Program Analysis for Reciprocal Cooperation)

## Authors

[[Swadesh Sistla]], [[Max Kleiman-Weiner]]

## Metadata

**Authors:** Swadesh Sistla; Max Kleiman-Weiner

**Year:** 2025

**Type:** conferencePaper

**Venue:** NeurIPS 2025

## Links

- **arXiv:** https://arxiv.org/abs/2512.00371
- **Code/Data:** https://github.com/Axelrod-Python/Axelrod

## Abstract

Large Language Models’ (LLMs) programming capabilities enable their participation in open-source games: a game-theoretic setting in which players submit computer programs in lieu of actions. These programs offer numerous advantages, including interpretability, inter-agent transparency, and formal verifiability; additionally, they enable program equilibria, solutions that leverage the transparency of code and are inaccessible within normal-form settings. We evaluate the capabilities of leading open- and closed-weight LLMs to predict and classify program strategies and evaluate features of the approximate program equilibria reached by LLM agents in dyadic and evolutionary settings. We identify the emergence of payoffmaximizing, cooperative, and deceptive strategies, characterize the adaptation of mechanisms within these programs over repeated open-source games, and analyze their comparative evolutionary fitness. We find that open-source games serve as a viable environment to study and steer the emergence of cooperative strategy in multi-agent dilemmas.

## Dataset Information

239 IPD strategies from the Axelrod Python library; classification task (cooperative vs non-cooperative); includes masked and obfuscated variants

## Data Description

The SPARC benchmark consists of 239 Iterated Prisoner's Dilemma strategies sourced from the Axelrod Python library, used to evaluate LLMs' ability to understand and classify strategic code. The benchmark includes original, masked (class names removed), and obfuscated (all identifiers replaced) versions of the strategy programs. Additionally, the paper evaluates LLM agents in open-source games including the Iterated Prisoner's Dilemma and a spatial Coin Game across dyadic and evolutionary settings.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** MEDIUM

## Tags

