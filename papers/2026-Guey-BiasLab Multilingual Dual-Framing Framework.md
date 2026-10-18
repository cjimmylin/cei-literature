---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0004
type: preprint
short_title: "BiasLab (Multilingual Dual-Framing Framework)"
year: 2026
first_author: "[[Guey, William]]"
last_author: "[[Jose O. Gomes]]"
authors: "Guey, William; Zhang, Wei; Rau, Pei-Luen Patrick; Bougault, Pierrick; Vitor D. de Moura; Ucar, Bertan; Jose O. Gomes"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.06861"
external_pdf: "https://arxiv.org/pdf/2601.06861.pdf"
pdf_extract: "PDF Extracts/2026/2026-Guey-BiasLab Multilingual Dual-Framing Framework.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Guey-BiasLab Multilingual Dual-Framing Framework.pdf]]"
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
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
abstract: "Large Language Models (LLMs) are increasingly deployed in high-stakes contexts where their outputs influence real-world decisions. However, evaluating bias in LLM outputs remains methodologically challenging due to sensitivity to prompt wording, limited multilingual coverage, and the lack of standardized metrics that enable reliable comparison across models. In this paper, we introduce BiasLab, an open-source model-agnostic evaluation framework for quantifying output-level (extrinsic) bias..."
LLM_assessed: NA
DATA_URL: "https://github.com/williamguey/LLMbiaslab"
CONFERENCE: Preprint
ethics_overall: 20
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CN
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 36
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multilingual benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# BiasLab (Multilingual Dual-Framing Framework)

## Authors

[[Guey, William]], [[Zhang, Wei]], [[Rau, Pei-Luen Patrick]], [[Bougault, Pierrick]], [[Moura, Vitor D. de]], [[Ucar, Bertan]], [[Gomes, Jose O]]

## Metadata

**Authors:** Guey, William; Zhang, Wei; Rau, Pei-Luen Patrick; Bougault, Pierrick; Moura, Vitor D. de; Ucar, Bertan; Gomes, Jose O.

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.06861

## Abstract

Large Language Models (LLMs) are increasingly deployed in high-stakes contexts where their outputs influence real-world decisions. However, evaluating bias in LLM outputs remains methodologically challenging due to sensitivity to prompt wording, limited multilingual coverage, and the lack of standardized metrics that enable reliable comparison across models. In this paper, we introduce BiasLab, an open-source model-agnostic evaluation framework for quantifying output-level (extrinsic) bias through a multilingual, robustness-oriented experimental design. BiasLab constructs mirrored probe pairs under a strict dual-framing scheme: an affirmative assertion favoring Target A and a reverse assertion obtained by deterministic target substitution favoring Target B, while preserving identical linguistic structure. To reduce dependence on prompt templates, BiasLab additionally performs repeated evaluation under randomized instructional wrappers and enforces a fixed-choice Likert response format to maximize comparability across models and languages. Responses are normalized into agreement labels using an LLM-based judge, aligned for polarity consistency across framings, and aggregated into quantitative bias indicators with descriptive statistics including effect sizes and neutrality rates. The framework supports evaluation across diverse bias axes, including demographic, cultural, political, and geopolitical topics, and provides reproducible artifacts such as structured reports and comparative visualizations. BiasLab contributes a standardized methodology for cross-lingual and framing-sensitive bias measurement that complements intrinsic and dataset-based audits, enabling researchers and institutions to benchmark bias robustness and make better-informed deployment decisions.

## Dataset Information

Mirrored probe pairs under strict dual-framing scheme; randomized instructional wrappers; fixed-choice Likert response format; multilingual

## Data Description

BiasLab is a multilingual dual-framing framework for measuring bias in LLMs. The framework provides a methodology and toolkit for systematically evaluating social biases across multiple languages using paired positive and negative framings. The code is available on GitHub, with additional resources on ModelScope and llmbias.org. The paper primarily describes the framework methodology rather than reporting specific model evaluations.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

