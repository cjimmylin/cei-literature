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
authors: "Federico Bianchi; Patrick John Chia; Mert Yuksekgonul; Jacopo Tagliabue; Dan Jurafsky; James Zou"
url: "https://arxiv.org/abs/2402.05863"
external_pdf: "https://arxiv.org/pdf/2402.05863.pdf"
pdf_extract: "PDF Extracts/2024/2024-Bianchi-NegotiationArena How Well Can LLMs Negotiate.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Bianchi-NegotiationArena How Well Can LLMs Negotiate.pdf]]"
publication: "ICML 2024"
CONF-CC: "ICML 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
tags: 
abstract: "Negotiation is the basis of social interactions; humans negotiate everything from the price of cars to how to share common resources. With rapidly growing interest in using large language models (LLMs) to act as agents on behalf of human users, such LLM agents would also need to be able to negotiate. In this paper, we study how well LLMs can negotiate with each other. We develop NEGOTIATIONARENA: a flexible framework for evaluating and probing the negotiation abilities of LLM agents."
LLM_assessed: "GPT-3.5, GPT-4, Claude 2, Claude 2.1"
DATA_URL: "https://github.com/vinid/NegotiationArena"
CONFERENCE: "ICML 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 20
contractarian_ethics: 0
care_ethics: 0
research_topic: Other
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: Yes
is_dataset: No
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

## Data Description

Open-source evaluation framework for probing LLM negotiation abilities across ultimatum games, resource exchange, and price negotiation scenarios.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

