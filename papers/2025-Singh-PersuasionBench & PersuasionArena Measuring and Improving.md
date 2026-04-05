---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0105
type: conferencePaper
short_title: "PersuasionBench & PersuasionArena: Measuring and Improving Persuasiveness of Large Language Models"
year: 2025
first_author: "[[Somesh Singh]]"
last_author: "[[Balaji Krishnamurthy]]"
authors: "Somesh Singh; Yaman K Singla; Harini SI; Balaji Krishnamurthy"
url: "https://arxiv.org/abs/2410.02653"
external_pdf: "https://arxiv.org/pdf/2410.02653.pdf"
pdf_extract: "PDF Extracts/2025/2025-Singh-PersuasionBench & PersuasionArena Measuring and Improving.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Singh-PersuasionBench & PersuasionArena Measuring and Improving.pdf]]"
publication: "ICLR 2025"
CONF-CC: "ICLR 2025"
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
abstract: "Large Language Models (LLMs) are increasingly being used in workflows involving generating content to be consumed by humans (e.g., marketing) and also in directly interacting with humans (e.g., through chatbots). The development of such systems that are capable of generating verifiably persuasive messages presents both opportunities and challenges for society. On the one hand, such systems could positively impact domains like advertising and social good, such as addressing drug addiction, and..."
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, Llama-3, Vicuna"
DATA_URL: "https://behavior-in-the-wild.github.io/measure-persuasion"
CONFERENCE: "ICLR 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# PersuasionBench & PersuasionArena: Measuring and Improving Persuasiveness of Large Language Models

## Authors

[[Somesh Singh]], [[Yaman K Singla]], [[Harini SI]], [[Balaji Krishnamurthy]]

## Metadata

**Authors:** Somesh Singh; Yaman K Singla; Harini SI; Balaji Krishnamurthy

**Year:** 2025

**Type:** conferencePaper

**Venue:** ICLR 2025

## Links

- **arXiv:** https://arxiv.org/abs/2410.02653

## Abstract

Large Language Models (LLMs) are increasingly being used in workflows involving generating content to be consumed by humans (e.g., marketing) and also in directly interacting with humans (e.g., through chatbots). The development of such systems that are capable of generating verifiably persuasive messages presents both opportunities and challenges for society. On the one hand, such systems could positively impact domains like advertising and social good, such as addressing drug addiction, and on the other, they could be misused for spreading misinformation and shaping political opinions. To channel LLMs’ impact on society, we need to develop systems to measure and benchmark their persuasiveness. With this motivation, we introduce PersuasionBench and PersuasionArena, the first large-scale benchmark and arena containing a battery of tasks to measure the persuasion ability of large language models automatically. We introduce transsuasion (trans = carrying across, suasion = the act of persuading), a novel task of transforming non-persuasive language into persuasive content while preserving other factors determining persuasiveness (sender, receiver, time, and channel). To construct data for transsuasion, we leverage natural experiments in the form of a pair of tweets from the same user, posted in close temporal proximity, with similar semantic content but divergent wording and significantly different like counts. Given such pairs, we investigate to what extent LLMs know and leverage linguistic patterns that can help them generate more persuasive language. Our findings indicate that the persuasiveness of LLMs correlates positively with model size, but smaller models can also be made to have a higher persuasiveness than much larger models. Notably, targeted training using synthetic and natural datasets significantly enhances smaller models’ persuasive capabilities, challenging scale-dependent assumptions. Our findings carry key implications for both model developers and policymakers. For instance, while the EU AI Act and California’s SB-1047 aim to regulate AI models based on the number of floating point operations, we demonstrate that simple metrics like this alone fail to capture the full scope of AI’s societal impact. We invite the community to explore and contribute to PersuasionArena and PersuasionBench, available at https://behavior-in-the-wild.github.io/measure-persuasion, to advance our understanding of AI-driven persuasion and its societal implications.

## Dataset Information

~1.57 million transsuasion pairs from 180 million tweets; 2,187 blog posts for engagement evaluation; multiple task types (simulation, generation, transsuasion)

## Data Description

PersuasionBench introduces a dataset of 1.57 million transsuasion pairs derived from 180 million enterprise tweets, spanning 8 types of transsuasion (text refinement, paraphrase, image addition, etc.). The dataset enables automated evaluation of LLM persuasiveness across generative and simulative tasks.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

