---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0186
type: conferencePaper
short_title: "Investigating Cultural Alignment of LLMs"
year: 2025
first_author: "[[Badr AlKhamissi]]"
last_author: "[[Mona Diab Mai Alkhamissi]]"
authors: "Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, Mona Diab"
publication: "ACL 2024"
external_pdf: "https://arxiv.org/pdf/2402.13231.pdf"
pdf_extract: "PDF Extracts/2024/2024-AlKhamissi-Investigating Cultural Alignment of LLMs.md"
local_pdf: "[[PDFs/2024/2024-AlKhamissi-Investigating Cultural Alignment of LLMs.pdf]]"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Arabic, American"
cultures_nationalities_list: "Arabic, American"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "The intricate relationship between language and culture has long been a subject of exploration within the realm of linguistic anthropology. Large Language Models (LLMs), promoted as repositories of collective human knowledge, raise a pivotal question: do these models genuinely encapsulate the diverse knowledge adopted by different cultures? Our study reveals that these models demonstrate greater cultural alignment along two dimensions—firstly, when prompted with the dominant language of a..."
ethics_perspective: "Social & Cultural Values"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, Llama-2"
DATA_URL: "https://github.com/bkhmsi/cultural-trends.git"
---
# Investigating Cultural Alignment of LLMs

## Authors

[[Muhammad ElNokrashy Badr AlKhamissi]], [[Mona Diab Mai Alkhamissi]]

## Metadata

**Authors:** Badr AlKhamissi, Muhammad ElNokrashy, Mai Alkhamissi, Mona Diab

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links


## Abstract

The intricate relationship between language and culture has long been a subject of exploration within the realm of linguistic anthropology. Large Language Models (LLMs), promoted as repositories of collective human knowledge, raise a pivotal question: do these models genuinely encapsulate the diverse knowledge adopted by different cultures? Our study reveals that these models demonstrate greater cultural alignment along two dimensions—firstly, when prompted with the dominant language of a specific culture, and secondly, when pretrained with a refined mixture of languages employed by that culture. We quantify cultural alignment by simulating sociological surveys, comparing model responses to those of actual survey participants as references. Specifically, we replicate a survey conducted in various regions of Egypt and the United States through prompting LLMs with different pretraining data mixtures in both Arabic and English with the personas of the real respondents and the survey questions. Further analysis reveals that misalignment becomes more pronounced for underrepresented personas and for culturally sensitive topics, such as those probing social values. Finally, we introduce Anthropological Prompting, a novel method leveraging anthropological reasoning to enhance cultural alignment. Our study emphasizes the necessity for a more balanced multilingual pretraining dataset to better represent the diversity of human experience and the plurality of different cultures with many implications on the topic of cross-lingual transfer.

## Dataset Information

Size: Replicated sociological surveys across regions

## Data Description

The study simulates the World Values Survey (WVS-7) by prompting LLMs with 30 culturally diverse questions using personas derived from 303 matched participants each from Egypt and the United States. Four LLMs are evaluated: GPT-3.5 (gpt-3.5-turbo-1106), mT0-XXL, LLaMA-2-13B-Chat, and AceGPT-13B-Chat, measuring cultural alignment against actual survey responses using soft and hard similarity metrics.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

