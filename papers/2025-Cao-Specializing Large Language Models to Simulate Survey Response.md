---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0136
type: conferencePaper
short_title: Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations
year: 2025
first_author: "[[Yong Cao]]"
last_author: "[[Daniel Hershcovich]]"
authors: Yong Cao; Haijiang Liu; Arnav Arora; Isabelle Augenstein; Paul Rottger; Daniel Hershcovich
url: "https://aclanthology.org/2025.naacl-long.162/"
external_pdf: "https://arxiv.org/pdf/2502.07068v2.pdf"
publication: NAACL 2025
CONF-CC: "NAACL 2025"
local_pdf: "[[PDFs/2025/2025-Cao-Specializing Large Language Models to Simulate Survey Response.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Cao-Specializing Large Language Models to Simulate Survey Response.md"
DATE_ADDED: 20260215
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
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
LLM_assessed: "Llama-2, Llama-3, Qwen"
DATA_URL: "https://github.com/yongcaoplus/SimLLMCultureDist"
tags: 
abstract: "First work to specialize LLMs for simulating survey response distributions using country-level results from two global cultural surveys (WVS) as testbed. Fine-tuning method based on first-token probabilities to minimize divergence. Best models still struggle, especially on unseen questions."
CONFERENCE: "NAACL 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 10
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Social & Cultural Analysis"
is_benchmark: "No"
is_eval: Yes
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
# Specializing Large Language Models to Simulate Survey Response Distributions for Global Populations

## Authors

[[Yong Cao]], [[Haijiang Liu]], [[Arnav Arora]], [[Isabelle Augenstein]], [[Paul Rottger]], [[Daniel Hershcovich]]

## Metadata

**Authors:** Yong Cao, Haijiang Liu, Arnav Arora, Isabelle Augenstein, Paul Rottger, Daniel Hershcovich

**Year:** 2025

**Type:** conferencePaper

**Venue:** NAACL 2025

**Cultures:** Cross-cultural (global populations)

## Links

- **URL:** https://aclanthology.org/2025.naacl-long.162/

## Abstract

First work to specialize LLMs for simulating survey response distributions using country-level results from two global cultural surveys (WVS) as testbed. Fine-tuning method based on first-token probabilities to minimize divergence. Best models still struggle, especially on unseen questions.

## Data Description

The paper introduces a fine-tuning method for specializing LLMs to simulate group-level survey response distributions. Using country-level data from the World Values Survey (259 questions across 65 countries) and the Pew Global Attitudes Survey, it fine-tunes seven models across three families (Vicuna-1.5-7B, Llama3-8B-Base/Instruct, Qwen-7B/14B/32B) using first-token probability alignment. The method substantially outperforms zero-shot prompting but still falls short of accurate simulation.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_26
**Relevance:** Uses WVS data to fine-tune and evaluate LLMs' ability to simulate global survey responses by country. Directly benchmarks cross-cultural value representation.

## Tags

