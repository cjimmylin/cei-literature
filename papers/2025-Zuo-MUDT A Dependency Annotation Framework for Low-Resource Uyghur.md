---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0612
type: preprint
short_title: "MUDT: A Dependency Annotation Framework for Low-Resource Uyghur"
year: 2025
first_author: "[[Zuo, Jiaxin]]"
last_author: "[[Yibulayin, Xiadiya]]"
authors: "[[Zuo, Jiaxin]]; [[Wang, Yiquan]]; [[Pan, Yuan]]; [[Yibulayin, Xiadiya]]"
authors_incomplete: false
url: "https://arxiv.org/pdf/2507.21536"
external_pdf: "https://arxiv.org/pdf/2507.21536.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Zuo-MUDT A Dependency Annotation Framework for Low-Resource Uyghur.md"
local_pdf: "[[PDFs/2025/2025-Zuo-MUDT A Dependency Annotation Framework for Low-Resource Uyghur.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Uyghur"
languages_list: Uyghur
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "Qwen"
DATA_URL: "https://github.com/wyqmath/MUDT"
tags: 
abstract: "Developing effective educational technologies for low-resource agglutinative languages like Uyghur is often hindered by the mismatch between existing annotation frameworks and specific grammatical structures. To address this challenge, this study introduces the Modern Uyghur Dependency Treebank (MUDT), a linguistically grounded annotation framework specifically designed to capture the agglutinative complexity of Uyghur, including zero copula constructions and fine-grained case marking."
research_topic: "AI Safety & Alignment"
---
# MUDT: A Dependency Annotation Framework for Low-Resource Uyghur

## Authors

[[Zuo, Jiaxin]], [[Wang, Yiquan]], [[Pan, Yuan]], [[Yibulayin, Xiadiya]]

## Metadata

**Authors:** Jiaxin Zuo; Yiquan Wang; Yuan Pan; Xiadiya Yibulayin

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Uyghur

**Benchmark:** MUDT

## Links

- **arXiv:** https://arxiv.org/abs/2507.21536

## Abstract


Developing effective educational technologies for low-resource agglutinative languages like Uyghur is often hindered by the mismatch between existing annotation frameworks and specific grammatical structures. To address this challenge, this study introduces the Modern Uyghur Dependency Treebank (MUDT), a linguistically grounded annotation framework specifically designed to capture the agglutinative complexity of Uyghur, including zero copula constructions and fine-grained case marking. Utilizing a hybrid pipeline that combines Large Language Model pre-annotation with rigorous human correction, a high-quality treebank consisting of 3,456 sentences was constructed. Intrinsic structural evaluation reveals that MUDT significantly improves dependency projectivity by reducing the crossing-arc rate from 7.35% in the Universal Dependencies standard to 0.06%. Extrinsic parsing experiments using UDPipe and Stanza further demonstrate that models trained on MUDT achieve superior in-domain accuracy and cross-domain generalization compared to UD-based baselines. To validate the practical utility of this computational resource, an AI-assisted grammar tutoring system was developed to translate MUDT-based syntactic analyses into interpretable pedagogical feedback. A controlled experiment involving 35 second-language learners indicated that students receiving syntax-aware feedback achieved significantly higher learning gains compared to those in a control group. These findings establish MUDT as a robust foundation for syntactic analysis and underscore the critical role of linguistically informed natural language processing resources in bridging the gap between computational models and the cognitive needs of second-language learners.

## Data Description

This paper introduces the Modern Uyghur Dependency Treebank (MUDT), a linguistically grounded annotation framework for Uyghur consisting of 3,456 sentences. The Qwen3-max LLM was used via API for pre-annotation, followed by human correction. Parsing experiments evaluated UDPipe, Stanza, and DiaParser on the treebank, and a controlled experiment with 35 L2 learners validated an AI-assisted grammar tutoring system built on the MUDT parser.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B10
**Relevance:** MUDT benchmark for Uyghur

## Tags

