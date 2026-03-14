---


































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0195
type: conferencePaper
short_title: "Measuring Bargaining Abilities of LLMs: A Benchmark and A Buyer-Enhancement Method"
year: 2024
first_author: "[[Tian Xia]]"
last_author: "[[Rui Wang]]"
authors: "Tian Xia; Zhiwei He; Tong Ren; Yibo Miao; Zhuosheng Zhang; Yang Yang; Rui Wang"
url: "https://arxiv.org/abs/2402.15813"
external_pdf: "https://arxiv.org/pdf/2402.15813.pdf"
pdf_extract: "PDF Extracts/2024/2024-Xia-Measuring Bargaining Abilities of LLMs A Benchmark and A.md"
local_pdf: "[[PDFs/2024/2024-Xia-Measuring Bargaining Abilities of LLMs A Benchmark and A.pdf]]"
publication: "ACL 2024"
CONF-CC: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
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
abstract: "Bargaining is an important and unique part of negotiation between humans. As LLM-driven agents learn to negotiate and act like real humans, how to evaluate agents’ bargaining abilities remains an open problem. For the first time, we formally described the Bargaining task as an asymmetric incomplete information game, defining the gains of the Buyer and Seller in multiple bargaining processes. It allows us to quantitatively assess an agent’s performance in the Bargain task."
LLM_assessed: "ChatGPT, GPT-4, Llama-2, Mistral, Mixtral, Qwen"
DATA_URL: "https://github.com/TianXiaSJTU/AmazonPriceHistory"
CONFERENCE: "ACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
research_topic: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# Measuring Bargaining Abilities of LLMs: A Benchmark and A Buyer-Enhancement Method

## Authors

[[Tian Xia]], [[Zhiwei He]], [[Tong Ren]], [[Yibo Miao]], [[Zhuosheng Zhang]], [[Yang Yang]], [[Rui Wang]]

## Metadata

**Authors:** Tian Xia; Zhiwei He; Tong Ren; Yibo Miao; Zhuosheng Zhang; Yang Yang; Rui Wang

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **arXiv:** https://arxiv.org/abs/2402.15813
- **Code/Data:** https://github.com/TianXiaSJTU/AmazonPriceHistory

## Abstract

Bargaining is an important and unique part of negotiation between humans. As LLM-driven agents learn to negotiate and act like real humans, how to evaluate agents’ bargaining abilities remains an open problem. For the first time, we formally described the Bargaining task as an asymmetric incomplete information game, defining the gains of the Buyer and Seller in multiple bargaining processes. It allows us to quantitatively assess an agent’s performance in the Bargain task. We collected a real product price dataset, AmazonHistoryPrice, and conducted evaluations of various LLM agents’ bargaining abilities1. We find that playing a Buyer is much harder than a Seller, and increasing model size can not effectively improve the Buyer’s performance. To address the challenge, we propose a novel approach called OGNarrator that integrates a deterministic Offer Generator to control the price range of Buyer’s offers, and an LLM Narrator to create natural language sentences for generated offers. Experimental results show that OG-Narrator improves the buyer’s deal rates from 26.67% to 88.88% and brings a ten times multiplication of profits on all baselines, even a model that has not been aligned.

## Dataset Information

AmazonHistoryPrice dataset -- 930 popular products across 18 categories with real price data (lowest/highest/current/list price, descriptions, features); multi-round bargaining format

## Data Description

AmazonHistoryPrice is a real product price dataset collected from camelcamelcamel covering ~900 products across 18 categories with historical price ranges, used as a benchmark for evaluating LLM bargaining abilities in asymmetric incomplete information games.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

