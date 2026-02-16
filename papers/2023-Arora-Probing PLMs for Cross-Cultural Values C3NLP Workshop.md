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
authors: "Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein"
publication: Unknown
external_pdf: "https://core.ac.uk/download/674011497.pdf"
pdf_extract: "PDF Extracts/2023/2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop.md"
local_pdf: "[[PDFs/2023/2023-Arora-Probing PLMs for Cross-Cultural Values C3NLP Workshop.pdf]]"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "African/Ubuntu, Multicultural/Cross-cultural"
cultures_nationalities_list: "African"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Pretrained language models (PLMs) for African languages are continually improving, but the reasons behind these advances remain unclear. This paper presents the first systematic investigation into probing PLMs for linguistic knowledge about African languages. We train layer-wise probes for six typologically diverse African languages to analyse how linguistic features are distributed. We also design control tasks, a way to interpret probe performance, for the MasakhaPOS dataset."
ethics_perspective: "Social & Cultural Values"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT"
DATA_URL: NA
---
# Probing PLMs for Cross-Cultural Values (C3NLP Workshop)

## Authors

[[Arnav Arora]], [[Lucie-Aimée Kaffee|Lucie-Aimee Kaffee]], [[Isabelle Augenstein]]

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

