---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0527
type: preprint
short_title: "GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek"
year: 2025
first_author: "[[Yang Zhang]]"
last_author: "[[Michalis Vazirgiannis]]"
authors: "Yang Zhang; Mersin Konomi; Christos Xypolopoulos; Konstantinos Divriotis; Konstantinos Skianis; Giannis Nikolentzos; Giorgos Stamou; Guokan Shang; Michalis Vazirgiannis"
url: "https://arxiv.org/abs/2602.05150"
external_pdf: "https://arxiv.org/pdf/2602.05150.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2026/2026-Zhang-GreekMMLU A Native-Sourced Multitask Benchmark for Evaluating.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Zhang-GreekMMLU A Native-Sourced Multitask Benchmark for Evaluating.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Greek
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
LLM_assessed: "GPT-4, GPT-4o, Claude-3 Opus, Gemini, Mistral, Llama-3"
DATA_URL: "https://github.com/mersinkonomi/GreekMMLU"
tags: 
abstract: "Large Language Models (LLMs) are commonly trained on multilingual corpora that include Greek, yet reliable evaluation benchmarks for Greek—particularly those based on authentic, native-sourced content—remain limited. Existing datasets are often machine-translated from English, failing to capture Greek linguistic and cultural characteristics. We introduce GreekMMLU1, a native-sourced benchmark for massive multitask language understanding in Greek, comprising 21,805 multiple-choice questions..."
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
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
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Multi-task benchmark"
data_metrics: "Not specified"
---
# GreekMMLU: A Native-Sourced Multitask Benchmark for Evaluating Language Models in Greek

## Authors

[[Yang Zhang]], [[Mersin Konomi]], [[Christos Xypolopoulos]], [[Konstantinos Divriotis]], [[Konstantinos Skianis]], [[Giannis Nikolentzos]], [[Giorgos Stamou]], [[Guokan Shang]], [[Michalis Vazirgiannis]]

## Metadata

**Authors:** Yang Zhang, Mersin Konomi, Christos Xypolopoulos, Konstantinos Divriotis, Konstantinos Skianis, Giannis Nikolentzos, Giorgos Stamou, Guokan Shang, Michalis Vazirgiannis

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

**Benchmark:** GreekMMLU

## Links

- **arXiv:** https://arxiv.org/abs/2602.05150
- **Code/Data:** https://huggingface.co/papers/2602.05150

## Abstract

A native-sourced benchmark for massive multitask language understanding in Greek, comprising 21,805 multiple-choice questions across 45 subject areas. All questions sourced or authored in Greek from academic, professional, and governmental exams. Evaluations of over 80 open- and closed-source LLMs reveal substantial performance gaps.

## Summary

This paper introduces GreekMMLU, the first large-scale, fully native-sourced benchmark for evaluating massive multitask language understanding in Greek, comprising 21,805 multiple-choice questions across 45 subject areas organized under STEM, Humanities, Social Sciences, and Other domains. All questions are sourced or authored in Greek from authentic academic, professional, and governmental examinations spanning primary school through professional certification levels, with eight Greek-specific subject areas requiring localized cultural knowledge. Evaluating over 80 open- and closed-source LLMs reveals substantial performance gaps between frontier and open-weight models and between Greek-adapted and general multilingual models, with 16,857 samples publicly released and 4,948 reserved for contamination-resistant evaluation.

## Data Description

Introduces GreekMMLU, a native-sourced benchmark for massive multitask language understanding in Greek, comprising 21,805 multiple-choice questions across 45 subject areas sourced from academic, professional, and governmental exams. Evaluates 80+ LLMs revealing substantial performance gaps between frontier and open-weight models, with 16,857 public and 4,948 private samples.


## Detailed Summary

This paper introduces GreekMMLU, the first large-scale, fully native-sourced benchmark for evaluating massive multitask language understanding in Greek. The benchmark comprises 21,805 multiple-choice questions across 45 manually defined subject areas organized under a newly defined taxonomy spanning STEM, Humanities, Social Sciences, and Other domains. All questions are sourced or authored in Greek from authentic academic, professional, and governmental examinations, covering educational difficulty levels from primary school through professional certification. Eight Greek-specific subject areas (Greek History, Greek Mythology, Greek Literature, Driving Rules, Citizenship Exams, etc.) require localized cultural knowledge. Of the total questions, 16,857 samples are publicly released while 4,948 are reserved for a private leaderboard to enable contamination-resistant evaluation. The benchmark addresses critical limitations of machine-translated MMLU variants, which fail to capture Greek linguistic characteristics (rich morphology, flexible word order, complex negation) and culturally grounded content (history, law, civics tied to national curricula). Evaluations of over 80 open- and closed-source LLMs reveal substantial performance gaps between frontier and open-weight models, and between Greek-adapted models and general multilingual ones.

## Paper Outline

1. Introduction - Limitations of translated benchmarks for Greek; motivation for native-sourced evaluation
2. Related Work - MMLU and its multilingual extensions; Greek NLP resources
3. Benchmark Design - Subject taxonomy; difficulty levels; data sources; quality control
4. Data Collection - Academic, professional, and governmental exam sources
5. Evaluation Setup - Model selection; prompting strategies; evaluation metrics
6. Results - Performance analysis of 80+ LLMs
7. Analysis - Effects of model scale, adaptation, and prompting on Greek performance
8. Conclusion

## Methods Summary

Questions are collected exclusively from sources released under open-access licenses or educational reuse terms. The 45 subject areas are organized under four broad domains (STEM, Humanities, Social Sciences, Other) with a dedicated Greek-specific category for eight culturally grounded subjects. Educational difficulty levels span primary school, secondary school, university, and professional examinations. A private leaderboard with 4,948 reserved samples enables contamination-resistant evaluation. Over 80 open- and closed-source LLMs are evaluated with systematic analysis of factors including model scale, Greek-specific adaptation, and prompting strategies.

## Results Summary

Closed-source frontier models substantially outperform open-weight alternatives on Greek tasks. Model scale strongly correlates with performance. Greek-adapted models show improvements over general multilingual models, but the gap with frontier models remains significant. Performance varies substantially across subject areas and difficulty levels, with Greek-specific subjects proving particularly challenging for models without cultural grounding. The benchmark reveals that incidental exposure to Greek in web-scale training corpora is insufficient for strong Greek language understanding.

## Conclusions

GreekMMLU provides the first rigorous, native-sourced evaluation framework for Greek language understanding, enabling systematic assessment of LLM capabilities in a language that has been underserved by existing benchmarks. The systematic analysis of factors influencing performance provides actionable insights for improving LLM capabilities in Greek, including the importance of dedicated Greek adaptation beyond general multilingual training.

## Artifact Contributions

- **Benchmark:** GreekMMLU - 21,805 native Greek MCQ across 45 subjects (https://github.com/mersinkonomi/GreekMMLU)
- **Public Leaderboard:** https://huggingface.co/spaces/yangzhang33/GreekMMLU-Leaderboard (4,948 private samples for contamination resistance)
- **Evaluation Results:** Comprehensive analysis of 80+ LLMs on Greek language understanding
- **Subject Taxonomy:** New 45-subject classification for Greek multitask evaluation

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** First native-sourced Greek MMLU benchmark. Includes cultural and educational content specific to Greece. Evaluates 80+ LLMs on Greek language understanding tasks spanning primary to professional examinations.

## Tags

