---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0095
type: preprint
short_title: "Nicer Than Humans: How Do Large Language Models Behave in the Prisoner's Dilemma?"
year: 2025
first_author: "[[Nicoló Fontana]]"
last_author: "[[Luca Maria Aiello]]"
authors: "Nicoló Fontana; Francesco Pierri; Luca Maria Aiello"
url: "https://arxiv.org/abs/2406.13605"
external_pdf: "https://arxiv.org/pdf/2406.13605.pdf"
pdf_extract: "PDF Extracts/2025/2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the.md"
local_pdf: "[[PDFs/2025/2025-Fontana-Nicer Than Humans How Do Large Language Models Behave in the.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "The behavior of Large Language Models (LLMs) as artificial social agents is largely unexplored, and we still lack extensive evidence of how these agents react to simple social stimuli. Testing the behavior of AI agents in classic Game Theory experiments provides a promising theoretical framework for evaluating the norms and values of these agents in archetypal social situations. In this work, we investigate the cooperative behavior of three LLMs (Llama2, Llama3, and GPT3."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "Llama-2, Llama-3, GPT-3.5"
DATA_URL: "https://huggingface.co/inference-api/serverless"
---
# Nicer Than Humans: How Do Large Language Models Behave in the Prisoner's Dilemma?

## Authors

[[Nicoló Fontana]], [[Francesco Pierri]], [[Luca Maria Aiello]]

## Metadata

**Authors:** Nicoló Fontana; Francesco Pierri; Luca Maria Aiello

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2406.13605

## Abstract

The behavior of Large Language Models (LLMs) as artificial social agents is largely unexplored, and we still lack extensive evidence of how these agents react to simple social stimuli. Testing the behavior of AI agents in classic Game Theory experiments provides a promising theoretical framework for evaluating the norms and values of these agents in archetypal social situations. In this work, we investigate the cooperative behavior of three LLMs (Llama2, Llama3, and GPT3.5) when playing the Iterated Prisoner’s Dilemma against random adversaries displaying various levels of hostility. We introduce a systematic methodology to evaluate an LLM’s comprehension of the game rules and its capability to parse historical gameplay logs for decision-making. We conducted simulations of games lasting for 100 rounds and analyzed the LLMs’ decisions in terms of dimensions defined in the behavioral economics literature. We find that all models tend not to initiate defection but act cautiously, favoring cooperation over defection only when the opponent’s defection rate is low. Overall, LLMs behave at least as cooperatively as the typical human player, although our results indicate some substantial differences among models. In particular, Llama2 and GPT3.5 are more cooperative than humans, and especially forgiving and non-retaliatory for opponent defection rates below 30%. More similar to humans, Llama3 exhibits consistently uncooperative and exploitative behavior unless the opponent always cooperates. Our systematic approach to the study of LLMs in game theoretical scenarios is a step towards using these simulations to inform practices of LLM auditing and alignment.

## Dataset Information

Iterated Prisoner's Dilemma simulations with 100 rounds per game; systematic prompting with fixed/variable parts; adversaries at varying hostility levels

## Data Description

This study evaluates three LLMs (Llama-2-70b, Llama-3-70B, GPT-3.5-Turbo) in the Iterated Prisoner's Dilemma game over 100 rounds against adversaries with varying hostility levels. The study introduces a meta-prompting technique to verify LLM comprehension of game rules and analyzes behavioral dimensions (niceness, forgiveness, retaliation, troublemaking, emulation) defined in behavioral economics literature.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** MEDIUM

## Tags

