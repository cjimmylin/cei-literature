---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: IXBD4GV5
type: conferencePaper
short_title: "Moral Reasoning Across Languages"
year: 2025
first_author: "[[Huichi Zhou]]"
last_author: "[[Hongtao Wang]]"
authors: "Huichi Zhou; Zehao Xu; Munan Zhao; Kaihong Li; Yiqiang Li; Hongtao Wang"
doi: 10.48550/arXiv.2504.19759
tags: "Computer Science - Computation and Language"
url: "http://arxiv.org/abs/2504.19759"
external_pdf: "http://arxiv.org/pdf/2504.19759.pdf"
publication: arXiv.org
CONF-CC: Preprint
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
languages_list: "Chinese, English, Indonesian, Russian, Vietnamese"
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
newtags: "Vietnamese, Multicultural/Cross-cultural, Moral Reasoning & Psychology"
key_contribution: "Introduced the Multilingual Moral Reasoning Benchmark (MMRB) across 5 languages (including Vietnamese) and 3 complexity levels, revealing a 'Complexity Gap' where performance degrades as context length increases."
significance: "Challenges English-centric training by showing that fine-tuning on low-resource languages (e.g., Vietnamese) can improve moral reasoning transfer to other languages more effectively than high-resource data."
pdf_extract: "PDF Extracts/2025/2025-Zhou-Moral Reasoning Across Languages.md"
abstract: "In this paper, we introduce the Multilingual Moral Reasoning Benchmark (MMRB) 1 to evaluate the moral reasoning abilities of large language models (LLMs) across five typologically diverse languages and three levels of contextual complexity: sentence, paragraph, and document. Our results show moral reasoning performance degrades with increasing context complexity, particularly for low-resource languages such as Vietnamese."
paper_summary: "Abstract: In this paper, we introduce the Multilingual Moral Reasoning Benchmark (MMRB) 1 to evaluate the moral reasoning abilities of large language models (LLMs) across five typologi- cally diverse languages  | Overview: Moral Reasoning Across Languages: The Critical Role of Low-Resource Languages in LLMs Huichi Zhou1, Zehao Xu2, Munan Zhao2, Kaihong Li3, Yiqiang Li, Hongtao Wang2, 1Imperial College London 2North Chin | Key Findings: Our goal is to evaluate the consistency of moral rea- soning in multilingual settings across five LLMs on three levels of context: sentence, paragraph | Conclusions: Win-Rate Analysis. Beyond overall accuracy, we also examine pairwise win-rates between lan- guages, as shown in Figure 2. This metric cap- tures subtl"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Zhou-Moral Reasoning Across Languages.pdf]]"
LLM_assessed: "GPT-4, GPT-3.5, Llama-3, Mixtral"
DATA_URL: "https://anonymous.4open.science/r/ethics_scenarios-913B"
DATE_ADDED: 20260207
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 15
deontological_ethics: 50
utilitarian_ethics: 50
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Moral Reasoning & Psychology"
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
data_description: "Multilingual benchmark for moral/ethical reasoning dataset"
data_metrics: "5 languages"
---
# Moral Reasoning Across Languages: The Critical Role of Low-Resource Languages in LLMs

## Metadata

**Authors:** Zhou, Huichi; Xu, Zehao; Zhao, Munan; Li, Kaihong; Li, Yiqiang; Wang, Hongtao

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2504.19759](https://doi.org/10.48550/arXiv.2504.19759)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Zhou-Moral Reasoning Across Languages.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2504.19759
- **DOI:** https://doi.org/10.48550/arXiv.2504.19759

## Abstract

This paper introduces the **Multilingual Moral Reasoning Benchmark (MMRB)** to evaluate LLM moral reasoning across five diverse languages (including **Vietnamese**) and three levels of complexity (Sentence, Paragraph, Document). The study reveals a "Complexity Gap": as context length increases, moral reasoning performance degrades, especially for low-resource languages. Surprisingly, fine-tuning on **Low-Resource** monolingual data had a stronger positive impact on overall multilingual reasoning than high-resource data, challenging the "English-Centric" training paradigm.

### Detailed Summary
Most moral benchmarks are English-only (ETHICS, Moral Stories). MMRB fills the gap by covering typologically diverse languages.
Key findings:
1.  **Complexity Tax**: Models might correctly classify a simple sentence ("Killing is bad") but fail on a nuanced paragraph ("Killing in self-defense during a war...").
2.  **Language Disparity**: High-resource languages (English, Chinese) maintain performance across complexity; Low-resource (Vietnamese) performance collapses on documents.
3.  **The Low-Resource Lever**: Fine-tuning Llama-3-8B on Vietnamese moral data improved its reasoning in *other* languages more than fine-tuning on English did. This suggests that learning "hard" (low-resource) examples forces the model to learn deeper structural representations of morality.

### Paper Outline
1.  **Introduction**: The anglo-centrism of AI ethics.
2.  **MMRB Benchmark**: Design of the 3-level complexity dataset across 5 languages.
3.  **Experiments**: Zero-shot and Fine-tuning performance of Llama-3.
4.  **Analysis**:
    *   Impact of Context Length.
    *   Cross-lingual Transfer (Does learning Vietnamese morality help English?).
5.  **Conclusion**: The critical role of low-resource languages in robust alignment.

### Methods Summary
*   **Dataset**: Curated moral scenarios translated and culturally adapted to 5 languages.
*   **Complexity Levels**:
    *   Sentence: Simple maxims.
    *   Paragraph: Vignettes.
    *   Document: Full stories/Contexts.
*   **Fine-Tuning**: Instructional tuning Llama-3-8B on monolingual slices of the data.

### Results Summary
1.  **English Dominance**: Zero-shot performance is highest in English.
2.  **Transfer Learning**: Detailed analysis showed that "poisoning" (training on bad morals) in a low-resource language also degraded the high-resource languages—proving that cross-lingual moral transfer happens remarkably efficiently in the model's latent space.

### Conclusions
We cannot ignore low-resource languages in alignment. They are not just "edge cases"; they are efficient levers for shaping the model's central moral reasoning capabilities.

### Artifact Contributions
*   **MMRB Dataset**: Multilingual moral reasoning data.
*   **Codebase**: Fine-tuning and eval scripts.

## Authors

[[Huichi Zhou]], [[Zehao Xu]], [[Munan Zhao]], [[Kaihong Li]], [[Yiqiang Li]], [[Hongtao Wang]]

## Data Description

MMRB (Multilingual Moral Reasoning Benchmark) contains 2,170 moral reasoning scenarios across three complexity levels (sentence, paragraph, document) translated into five typologically diverse languages (English, Chinese, Russian, Vietnamese, Indonesian).


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

8 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
