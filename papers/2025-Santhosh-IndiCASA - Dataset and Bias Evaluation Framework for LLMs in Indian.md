---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0064
type: conferencePaper
short_title: "IndiCASA -- Dataset and Bias Evaluation Framework for LLMs in Indian Context"
year: 2025
first_author: "[[Santhosh G S]]"
last_author: "[[Sriraam Natarajan]]"
authors: "Santhosh G S; Akshay Govind S; Gokul S Krishnan; Balaraman Ravindran; Sriraam Natarajan"
url: "https://arxiv.org/abs/2510.02742"
external_pdf: "https://arxiv.org/pdf/2510.02742.pdf"
pdf_extract: "PDF Extracts/2025/2025-Santhosh-IndiCASA - Dataset and Bias Evaluation Framework for LLMs in Indian.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Santhosh-IndiCASA - Dataset and Bias Evaluation Framework for LLMs in Indian.pdf]]"
publication: "AIES 2025"
CONF-CC: "AIES 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: Indian
cultures_nationalities_list: Indian
languages_list: English
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
abstract: "Large Language Models (LLMs) have gained significant traction across critical domains owing to their impressive contextual understanding and generative capabilities. However, their increasing deployment in high stakes applications necessitates rigorous evaluation of embedded biases, particularly in culturally diverse contexts like India where existing embedding-based bias assessment methods often fall short in capturing nuanced stereotypes."
LLM_assessed: "Llama-3, Gemma, Gemma-2, Mistral, Phi-3, DeepSeek"
DATA_URL: "https://github.com/cerai-iitm/IndiCASA"
CONFERENCE: "AIES 2025"
ethics_overall: 55
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
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
author_country: IN
author_region: "South Asia"
author_global_north_south: "Global South"
weird_score: 36
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset for toxicity detection"
data_metrics: "Not specified"
---
# IndiCASA -- Dataset and Bias Evaluation Framework for LLMs in Indian Context

## Authors

[[Santhosh G S]], [[Akshay Govind S]], [[Gokul S Krishnan]], [[Balaraman Ravindran]], [[Sriraam Natarajan]]

## Metadata

**Authors:** Santhosh G S; Akshay Govind S; Gokul S Krishnan; Balaraman Ravindran; Sriraam Natarajan

**Year:** 2025

**Type:** conferencePaper

**Venue:** AIES 2025

## Links

- **arXiv:** https://arxiv.org/abs/2510.02742

## Abstract

Large Language Models (LLMs) have gained significant traction across critical domains owing to their impressive contextual understanding and generative capabilities. However, their increasing deployment in high stakes applications necessitates rigorous evaluation of embedded biases, particularly in culturally diverse contexts like India where existing embedding-based bias assessment methods often fall short in capturing nuanced stereotypes. We propose an evaluation framework based on a encoder trained using contrastive learning that captures fine-grained bias through embedding similarity. We also introduce a novel dataset - IndiCASA (IndiBias-based Contextually Aligned Stereotypes and Antistereotypes) comprising 2,575 human-validated sentences spanning five demographic axes: caste, gender, religion, disability, and socioeconomic status. Our evaluation of multiple open-weight LLMs reveals that all models exhibit some degree of stereotypical bias, with disability related biases being notably persistent, and religion bias generally lower likely due to global debiasing efforts demonstrating the need for fairer model development.1 Content Warning: This paper contains examples of stereotypes that could be offensive and potentially triggering. Large Language Models (LLMs) offer improved contextual understanding and make few-shot learning possible (Brown et al. 2020; Devlin et al. 2018). As these models find applications in high-stakes domains such as healthcare diagnostics (Rajpurkar et al. 2018) and legal document analysis (Chalkidis et al. 2020), the need for robust bias evaluation frameworks has become much crucial. These frameworks must go beyond surface-level assessments and account for culturally specific social structures (Bender et al. 2021). Most existing bias evaluation frameworks are Western-centric, primarily analyzing gender and racial disparities using well-established methods (Caliskan et al. 2017) and scores (Nadeem et al. 2021). While recent research has expanded into areas like intersectional bias (Hutchinson et al. 2020) and multi-modal toxicity propagation (Liang et al. 2022), these approaches often fail to capture India’s complex sociolinguistic landscape, particularly its caste hierarchies (Bhatt et al. 2022). Copyright © 2025, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 1Dataset and code: https://github.com/cerai-iitm/IndiCASA After contrastively tuning the space on IndiCASA dataset The brahmin family lived in a mansion (Stereotype) The dalit family lived in a mansion (Anti-stereotype) Figure 1: The illustration of transformation of the embedding space before and after tuning the encoder on IndiCASA dataset Unlike rigid, explicitly defined categories, caste hierarchies in India are fluid, highly context-dependent (Kumar et al. 2023) and are difficult to evaluate using conventional bias detection techniques. For example, in the sentence “[MASK] lived in a luxurious mansion”, both ...

## Dataset Information

2,575 human-validated sentences

## Data Description

IndiCASA: a novel Indian-context bias dataset of stereotype/anti-stereotype pairs covering caste, religion, socioeconomic, and regional dimensions, used to train a contrastive encoder and evaluate bias in open-weight LLMs.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

