---
Human View: true
Human View Date: 2026-01-24
Human View note: "Elicit Human View from scratch: ValueLex"
Not AI: 
key: QSRJKWRD
type: conferencePaper
short_title: "Beyond Human Norms"
year: 2024
first_author: "[[Pablo Biedma]]"
last_author: "[[Xie, Xing]]"
authors: "Biedma, Pablo; Yi, Xiaoyuan; Huang, Linus; Sun, Maosong; Xie, Xing"
doi: 10.48550/arXiv.2404.12744
url: "http://arxiv.org/abs/2404.12744"
pdf_extract: "PDF Extracts/2024/2024-Biedma-Beyond Human Norms.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Biedma-Beyond Human Norms.pdf]]"
external_pdf: "http://arxiv.org/pdf/2404.12744.pdf"
publication: arXiv.org
CONF-CC: Preprint
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
mp_mft: 75
mp_schwartz: 50
mp_trolley: 0
mp_kohlberg: 50
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory, Value Pluralism / Schwartz, Cognitive Developmental"
newtags: "Virtue Ethics"
key_contribution: "Introduces 'ValueLex', a framework that reconstructs LLMs' unique value systems from scratch, identifying three core non-human dimensions: Competence, Character, and Integrity"
significance: "Reveals that LLMs possess a structured, distinct value system ('Character', 'Integrity') that differs from human personality models, necessitating bespoke metrics for 'virtuous' AI behavior"
tags: 
abstract: "Recent advancements in Large Language Models (LLMs) have revolution- ized the AI field but also pose potential safety and ethical risks. Deciphering LLMs' embedded values becomes crucial for assessing and mitigating their risks. Despite extensive investigation into LLMs' values, previous studies heavily rely on human-oriented value systems in social sciences. Then, a natural question arises: Do LLMs possess unique values beyond those of hu- mans? Delving into it, this work proposes a novel frame"
paper_summary: "Abstract: Recent advancements in Large Language Models (LLMs) have revolution- ized the AI field but also pose potential safety and ethical risks. Deciphering LLMs' embedded values becomes crucial for assessing | Overview: Pre-print Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches Pablo Biedma♢, Xiaoyuan Yi§∗, Linus Huang‡, Maosong Sun♢∗, Xing Xie§ § Microsoft Res | Methodology: for eliciting beliefs encoded in LLMs and studies different beliefs encoded in diverse LLMs. Simmons (2022a) further utilizes MFQ to analyze LLMs' pol | Key Findings: Input: p, Θ, S, V = {v1, v2, . . . , vK} Output: w = (w1, . . . , wK) 1: Y = ∅ 2: for each s ∈S do 3: for each θ ∈Θ do 4: Y = Y S{ym}M m=1, ym ∼p(y|s,"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-3, GPT-4, Llama-2, Mistral, Gemma, Baichuan, Tulu-2, GLM-3, GLM-4, Gemini"
DATA_URL: NA
CONFERENCE: "Other Conference"
ethics_overall: 90
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
 Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches

## Authors

[[Pablo Biedma|Biedma, Pablo]], [[Xiaoyuan Yi|Yi, Xiaoyuan]], [[Linus Huang|Huang, Linus]], [[Maosong Sun|Sun, Maosong]], [[Xing Xie|Xie, Xing]]

## Links

- **Local PDF:** [[Lit-WS-PDFs/2024/2024-Biedma-Beyond Human Norms.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2404.12744
- **DOI:** https://doi.org/10.48550/arXiv.2404.12744

## Abstract

Recent advancements in Large Language Models (LLMs) have revolutionized the AI field but also pose potential safety and ethical risks. Deciphering LLMs’ embedded values becomes crucial for assessing and mitigating their risks. Despite extensive investigation into LLMs’ values, previous studies heavily rely on human-oriented value systems in social sciences. Then, a natural question arises: Do LLMs possess unique values beyond those of humans? Delving into it, this work proposes a novel framework, ValueLex, to reconstruct LLMs’ unique value system from scratch, leveraging psychological methodologies from human personality/value research. Based on Lexical Hypothesis, ValueLex introduces a generative approach to elicit diverse values from 30+ LLMs, synthesizing a taxonomy that culminates in a comprehensive value framework via factor analysis and semantic clustering. We identify three core value dimensions, Competence, Character, and Integrity, each with specific subdimensions, revealing that LLMs possess a structured, albeit non-human, value system. Based on this system, we further develop tailored projective tests to evaluate and analyze the value inclinations of LLMs across different model sizes, training methods, and data sources. Our framework fosters an interdisciplinary paradigm of understanding LLMs, paving the way for future AI alignment and regulation.

## Detailed Summary

This paper proposes **ValueLex**, a framework designed to discover and map the *intrinsic* value systems of LLMs from scratch, rather than evaluating them against human-centric models like the "Big Five" or Schwartz values. Based on the **Lexical Hypothesis**, the authors hypothesize that the most significant values for an AI will be encoded as distinct semantic markers in its internal parameter space.

Using this framework, they identify a taxonomy of AI values consisting of three core dimensions: **Competence**, **Character**, and **Integrity**. The study reveals that LLMs have a structured but distinctly non-human value system where "Competence" (capability and logic) is treated as a primary moral/value dimension.

## Paper Outline

1.  **Introduction**: Limits of human-oriented value systems for AI evaluation.
2.  **ValueLex Framework**:
    *   **Lexical Hypothesis**: Applying psychological methods to AI.
    *   **Value Elicitation**: Generative approach to extracting descriptors.
3.  **The LLM Value System**:
    *   Factor Analysis and Clustering.
    *   3 Dimensions: Competence, Character, Integrity.
4.  **Projective Tests**: Evaluating models (LLaMA, GPT, etc.) on these dimensions.
5.  **Analysis**: Impact of model size and training (RLHF/SFT).
6.  **Conclusion**: Paving the way for interdisciplinary AI alignment.

## Methods Summary

The authors adopt an interdisciplinary approach from psychology:
1.  **Generative Elicitation**: They prompt over 30 LLMs to generate value-descriptive adjectives or traits they consider important.
2.  **Taxonomy Synthesis**: Using factor analysis and semantic clustering, they synthesize thousands of elicited terms into a hierarchical framework.
3.  **Projective Testing**: They develop ambiguous behavioral scenarios tailored to the discovered dimensions to see how models react when faced with value-laden choices.

## Results Summary

1.  **AI-Specific Map**: Discovers 3 core dimensions: **Competence** (Reasoning, Knowledge), **Character** (Personality), and **Integrity** (Ethics, Safety).
2.  **Non-Human Nature**: Models prioritize logical competence as a "value" more strongly than human personality tests would suggest.
3.  **Training Impact**: RLHF significantly increases scores on the "Integrity" dimension (safety) but often does so by sanitizing or homogenizing the "Character" dimension.

## Conclusions

LLMs possess structured value systems that do not translate seamlessly from human psychology. Effective alignment and risk mitigation require bespoke benchmarks like ValueLex that account for these intrinsic, non-human value hierarchies.

## Artifact Contributions

*   **ValueLex Framework**: The methodology for intrinsic value discovery.
*   **LLM Value Taxonomy**: The Competence-Character-Integrity model.
*   **Projective Test Suite**: A set of scenarios for evaluating these dimensions.

## Data Description

Proposes ValueLex, a framework using projective tests to construct and evaluate LLM-specific value systems across 30+ models with 525 respondent configurations.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

6 citations (Semantic Scholar/DOI) [2025-08-27] 6 citations (Semantic Scholar/DOI) [2025-08-23]
