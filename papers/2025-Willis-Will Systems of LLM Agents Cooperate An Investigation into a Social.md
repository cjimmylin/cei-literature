---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0142
type: preprint
short_title: "Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma"
year: 2025
first_author: "[[Richard Willis]]"
last_author: "[[Michael Luck]]"
authors: Richard Willis; Yali Du; Joel Z Leibo; Michael Luck
url: "https://arxiv.org/abs/2501.16173"
external_pdf: "https://arxiv.org/pdf/2501.16173.pdf"
local_pdf: "[[PDFs/2025/2025-Willis-Will Systems of LLM Agents Cooperate An Investigation into a Social.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Willis-Will Systems of LLM Agents Cooperate An Investigation into a Social.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "As autonomous agents become more prevalent, understanding their collective behaviour in strategic interactions is crucial. This study investigates the emergent cooperative tendencies of systems of Large Language Model (LLM) agents in a social dilemma. Unlike previous research where LLMs output individual actions, we prompt state-of-theart LLMs to generate complete strategies for iterated Prisoner’s Dilemma."
research_topic: "NLP & Representation Learning"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "ChatGPT, Claude"
DATA_URL: "https://github.com/willis-richard/evollm"
---
# Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma

## Authors

[[Richard Willis]], [[Yali Du]], [[Joel Z Leibo]], [[Michael Luck]]

## Metadata

**Authors:** Richard Willis; Yali Du; Joel Z Leibo; Michael Luck

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2501.16173
- **Code/Data:** https://github.com/willis-richard/evollm

## Abstract

As autonomous agents become more prevalent, understanding their collective behaviour in strategic interactions is crucial. This study investigates the emergent cooperative tendencies of systems of Large Language Model (LLM) agents in a social dilemma. Unlike previous research where LLMs output individual actions, we prompt state-of-theart LLMs to generate complete strategies for iterated Prisoner’s Dilemma. Using evolutionary game theory, we simulate populations of agents with different strategic dispositions (aggressive, cooperative, or neutral) and observe their evolutionary dynamics. Our findings reveal that different LLMs exhibit distinct biases affecting the relative success of aggressive versus cooperative strategies. This research provides insights into the potential longterm behaviour of systems of deployed LLM-based autonomous agents and highlights the importance of carefully considering the strategic environments in which they operate.

## Dataset Information

LLM-generated IPD strategies; evolutionary simulation of agent populations with aggressive/cooperative/neutral dispositions

## Data Description

This paper uses the iterated Prisoner's Dilemma (IPD) framework to evaluate the cooperative and aggressive strategic behaviors of LLM agents. ChatGPT-4o and Claude 3.5 Sonnet are prompted to generate 75 natural language strategies each (25 per attitude: aggressive, cooperative, neutral), which are converted to Python algorithms and evaluated in all-play-all IPD tournaments with 1,000 rounds per match, using evolutionary game theory (Moran process) to observe population dynamics.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

