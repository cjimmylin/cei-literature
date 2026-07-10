---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0242
type: conferencePaper
short_title: "Probing PLMs for Cross-Cultural Values (C3NLP Workshop)"
year: 2025
first_author: "[[Arnav Arora]]"
last_author: "[[Isabelle Augenstein]]"
authors: "Arnav Arora; Lucie-Aimee Kaffee; Isabelle Augenstein"
publication: Unknown
CONF-CC: Preprint
external_pdf: "https://core.ac.uk/download/674011497.pdf"
pdf_extract: "PDF Extracts/2023/2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: African/Ubuntu
cultures_nationalities_list: African/Ubuntu
languages_list: Multilingual
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
abstract: "Pretrained language models (PLMs) for African languages are continually improving, but the reasons behind these advances remain unclear. This paper presents the first systematic investigation into probing PLMs for linguistic knowledge about African languages. We train layer-wise probes for six typologically diverse African languages to analyse how linguistic features are distributed. We also design control tasks, a way to interpret probe performance, for the MasakhaPOS dataset."
LLM_assessed: RoBERTa
DATA_URL: NA
CONFERENCE: "Other Conference"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Social & Cultural Values"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: ZA
author_region: "Sub-Saharan Africa"
author_global_north_south: "Global South"
weird_score: 36
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
---
# Probing PLMs for Cross-Cultural Values (C3NLP Workshop)

## Authors

[[Arnav Arora]], [[Lucie-Aimee Kaffee]], [[Isabelle Augenstein]]

## Metadata

**Authors:** Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein

**Year:** 2023

**Type:** conferencePaper

**Venue:** Unknown

## Links


## Abstract

Pretrained language models (PLMs) for African languages are continually improving, but the reasons behind these advances remain unclear. This paper presents the first systematic investigation into probing PLMs for linguistic knowledge about African languages. We train layer-wise probes for six typologically diverse African languages to analyse how linguistic features are distributed. We also design control tasks, a way to interpret probe performance, for the MasakhaPOS dataset. We find PLMs adapted for African languages to encode more linguistic information about target languages than massively multilingual PLMs. Our results reaffirm previous findings that token-level syntactic information concentrates in middle-tolast layers, while sentence-level semantic information is distributed across all layers. Through control tasks and probing baselines, we confirm that performance reflects the internal knowledge of PLMs rather than probe memorisation. Our study applies established interpretability techniques to African-language PLMs. In doing so, we highlight the internal mechanisms underlying the success of strategies like active learning and multilingual adaptation.

## Dataset Information

Size: Probe-based evaluation (details in full paper)

## Data Description

This study probes seven pretrained masked language models (XLM-R, AfroXLMR, Nguni-XLMR, AfriBERTa, AfroLM) for linguistic knowledge about six typologically diverse African languages (Swahili, Igbo, Hausa, Luganda, isiXhosa, Naija Pidgin). The probing experiments use three Masakhane datasets (MasakhaPOS, MasakhaNER, MasakhaNEWS) for POS tagging, named entity recognition, and news topic classification tasks, with a novel control task designed for MasakhaPOS.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

