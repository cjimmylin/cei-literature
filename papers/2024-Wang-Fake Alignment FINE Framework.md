---










Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0174
type: conferencePaper
short_title: "Fake Alignment (FINE Framework)"
year: 2024
first_author: "[[Du, Yihan]]"
last_author: "[[Srikant, R]]"
authors: "[[Du, Yihan]]; [[Kong, Seo Taek]]; [[Srikant, R.]]"
authors_incomplete: false
publication: "ACL 2024"
external_pdf: "https://arxiv.org/pdf/2510.05703.pdf"
pdf_extract: "PDF Extracts/2024/2024-Wang-Fake Alignment FINE Framework.md"
local_pdf: "[[PDFs/2024/2024-Wang-Fake Alignment FINE Framework.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "The widespread application of Large Language Models (LLMs) imposes increasing demands on safety, such as reducing harmful content and fake information, and avoiding certain forbidden tokens due to rules and laws. While there have been several recent works studying safe alignment of LLMs, these works either require the training of reward and cost models and incur high memory and computational costs, or need prior knowledge about the optimal solution."
LLM_assessed: "Alpaca, GPT-4, Llama, Llama-2"
DATA_URL: "https://github.com/AIFlames/Fake-Alignment"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus"
data_metrics: "Not specified"
CONFERENCE: "ACL 2024"
---
# Fake Alignment (FINE Framework)

## Authors

[[Du, Yihan]], [[Kong, Seo Taek]], [[Srikant, R]]

## Metadata

**Authors:** Du, Yihan; Kong, Seo Taek; Srikant, R.

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **Code/Data:** https://github.com/AIFlames/Fake-Alignment

## Abstract

The widespread application of Large Language Models (LLMs) imposes increasing demands on safety, such as reducing harmful content and fake information, and avoiding certain forbidden tokens due to rules and laws. While there have been several recent works studying safe alignment of LLMs, these works either require the training of reward and cost models and incur high memory and computational costs, or need prior knowledge about the optimal solution. Motivated by this fact, we study the problem of constrained alignment in LLMs, i.e., maximizing the output reward while restricting the cost due to potentially unsafe content to stay below a threshold. For this problem, we propose a novel primal-dual DPO approach, which first trains a model using standard DPO on reward preference data to provide reward information, and then adopts a rearranged Lagrangian DPO objective utilizing the provided reward information to fine-tune LLMs on cost preference data. Our approach significantly reduces memory and computational costs, and does not require extra prior knowledge. Moreover, we establish rigorous theoretical guarantees on the suboptimality and constraint violation of the output policy. We also extend our approach to an online data setting by incorporating exploration bonuses, which enables our approach to explore uncovered promptresponse space, and then provide theoretical results that get rid of the dependence on preference data coverage. Experimental results on the widely-used preference dataset PKU-SafeRLHF demonstrate the effectiveness of our approach.

## Dataset Information

Size: Comparative benchmark with MC and open-ended questions

## Data Description

This paper proposes a primal-dual DPO approach for constrained LLM alignment that maximizes reward while restricting costs from unsafe content. The experiments use the PKU-SafeRLHF preference dataset as the evaluation benchmark, which contains reward and cost preference data for LLM safety alignment. No new dataset is introduced; the focus is on the theoretical framework and optimization methodology for constrained alignment.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** HIGH

## Tags

