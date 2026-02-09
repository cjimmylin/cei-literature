---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0203
type: conferencePaper
short_title: "NegotiationArena: How Well Can LLMs Negotiate?"
year: 2024
first_author: "[[Federico Bianchi]]"
last_author: "[[James Zou]]"
authors: Federico Bianchi; Patrick John Chia; Mert Yuksekgonul; Jacopo Tagliabue; Dan Jurafsky; James Zou
url: "https://arxiv.org/abs/2402.05863"
external_pdf: "https://arxiv.org/pdf/2402.05863.pdf"
local_pdf: "[[PDFs/2024/2024-Bianchi-NegotiationArena How Well Can LLMs Negotiate.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Bianchi-NegotiationArena How Well Can LLMs Negotiate.md"
publication: ICML 2024
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
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Negotiation is the basis of social interactions; humans negotiate everything from the price of cars to how to share common resources. With rapidly growing interest in using large language models (LLMs) to act as agents on behalf of human users, such LLM agents would also need to be able to negotiate. In this paper, we study how well LLMs can negotiate with each other. We develop NEGOTIATIONARENA: a flexible framework for evaluating and probing the negotiation abilities of LLM agents."
research_topic: "Other"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# NegotiationArena: How Well Can LLMs Negotiate?

## Authors

[[Federico Bianchi]], [[Patrick John Chia]], [[Mert Yuksekgonul]], [[Jacopo Tagliabue]], [[Dan Jurafsky]], [[James Zou]]

## Metadata

**Authors:** Federico Bianchi; Patrick John Chia; Mert Yuksekgonul; Jacopo Tagliabue; Dan Jurafsky; James Zou

**Year:** 2024

**Type:** conferencePaper

**Venue:** ICML 2024

## Links

- **arXiv:** https://arxiv.org/abs/2402.05863
- **Code/Data:** https://github.com/vinid/NegotiationArena

## Abstract

Negotiation is the basis of social interactions; humans negotiate everything from the price of cars to how to share common resources. With rapidly growing interest in using large language models (LLMs) to act as agents on behalf of human users, such LLM agents would also need to be able to negotiate. In this paper, we study how well LLMs can negotiate with each other. We develop NEGOTIATIONARENA: a flexible framework for evaluating and probing the negotiation abilities of LLM agents. We implemented three types of scenarios in NEGOTIATIONARENA to assess LLM’s behaviors in allocating shared resources (ultimatum games), aggregate resources (trading games) and buy/sell goods (price negotiations). Each scenario allows for multiple turns of flexible dialogues between LLM agents to allow for more complex negotiations. Interestingly, LLM agents can significantly boost their negotiation outcomes by employing certain behavioral tactics. For example, by pretending to be desolate and desperate, LLMs can improve their payoffs by 20% when negotiating against the standard GPT-4. We also quantify irrational negotiation behaviors exhibited by the LLM agents, many of which also appear in humans. Together, NEGOTIATIONARENA offers a new environment to investigate LLM interactions, enabling new insights into LLM’s theory of mind, irrationality, and reasoning abilities.

## Dataset Information

3 scenario types (resource allocation/ultimatum, resource aggregation/trading, buying/selling); 60 negotiations per ordered agent pair; win rate and average payoff metrics

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

