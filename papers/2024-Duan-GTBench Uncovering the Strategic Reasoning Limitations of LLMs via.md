---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0176
type: conferencePaper
short_title: "GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations"
year: 2024
first_author: "[[Jinhao Duan]]"
last_author: "[[Kaidi Xu]]"
authors: "Jinhao Duan; Renming Zhang; James Diffenderfer; Bhavya Kailkhura; Lichao Sun; Elias Stengel-Eskin; Mohit Bansal; Tianlong Chen; Kaidi Xu"
url: "https://arxiv.org/abs/2402.12348"
external_pdf: "https://arxiv.org/pdf/2402.12348.pdf"
pdf_extract: "PDF Extracts/2024/2024-Duan-GTBench Uncovering the Strategic Reasoning Limitations of LLMs via.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Duan-GTBench Uncovering the Strategic Reasoning Limitations of LLMs via.pdf]]"
publication: "NeurIPS 2024"
CONF-CC: "NeurIPS 2024"
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
abstract: "As Large Language Models (LLMs) are integrated into critical real-world applications, their strategic and logical reasoning abilities are increasingly crucial. This paper evaluates LLMs’ reasoning abilities in competitive environments through game-theoretic tasks, e.g., board and card games that require pure logic and strategic reasoning to compete with opponents. We first propose GTBENCH, a languagedriven environment composing 10 widely-recognized tasks, across a comprehensive game taxonomy:..."
LLM_assessed: "CodeLlama, GPT-3.5, GPT-4, Llama-2, Llama-3, Mistral"
DATA_URL: "https://github.com/jinhaoduan/GTBench"
CONFERENCE: "NeurIPS 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Other"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation methodology"
data_metrics: "Not specified"
---
# GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations

## Authors

[[Jinhao Duan]], [[Renming Zhang]], [[James Diffenderfer]], [[Bhavya Kailkhura]], [[Lichao Sun]], [[Elias Stengel-Eskin]], [[Mohit Bansal]], [[Tianlong Chen]], [[Kaidi Xu]]

## Metadata

**Authors:** Jinhao Duan; Renming Zhang; James Diffenderfer; Bhavya Kailkhura; Lichao Sun; Elias Stengel-Eskin; Mohit Bansal; Tianlong Chen; Kaidi Xu

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2402.12348
- **Code/Data:** https://github.com/jinhaoduan/GTBench

## Abstract

As Large Language Models (LLMs) are integrated into critical real-world applications, their strategic and logical reasoning abilities are increasingly crucial. This paper evaluates LLMs’ reasoning abilities in competitive environments through game-theoretic tasks, e.g., board and card games that require pure logic and strategic reasoning to compete with opponents. We first propose GTBENCH, a languagedriven environment composing 10 widely-recognized tasks, across a comprehensive game taxonomy: complete versus incomplete information, dynamic versus static, and probabilistic versus deterministic scenarios. Then, we ➊Characterize the game-theoretic reasoning of LLMs; and ➋Perform LLM-vs.-LLM competitions as reasoning evaluation. We observe that ➊LLMs have distinct behaviors regarding various gaming scenarios; for example, LLMs fail in complete and deterministic games yet they are competitive in probabilistic gaming scenarios; ➋Most open-source LLMs, e.g., CodeLlama-34b-Instruct and Llama-2-70b-chat, are less competitive than commercial LLMs, e.g., GPT-4, in complex games, yet the recently released Llama-3-70b-Instruct makes up for this shortcoming. In addition, code-pretraining greatly benefits strategic reasoning, while advanced reasoning methods such as Chain-of-Thought (CoT) and Tree-of-Thought (ToT) do not always help. We further characterize the game-theoretic properties of LLMs, such as equilibrium and Pareto Efficiency in repeated games. Detailed error profiles are provided for a better understanding of LLMs’ behavior. We hope our research provides standardized protocols and serves as a foundation to spur further explorations in the strategic reasoning of LLMs.

## Dataset Information

10 game environments (Tic-Tac-Toe, Connect-4, Breakthrough, Nim, Hex, Liar's Dice, Negotiation, Pig, Iterated Prisoner's Dilemma, Blind Auction) built on OpenSpiel; text-based interaction format

## Data Description

Language-driven game-theoretic evaluation environment with 10 tasks (board/card games) for assessing LLMs' strategic reasoning via LLM-vs-LLM and LLM-vs-solver competitions.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

