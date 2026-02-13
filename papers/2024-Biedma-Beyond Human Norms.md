---

Human View: true
Human View Date: 2026-01-24
Human View note: "Elicit Human View from scratch: ValueLex"
Not AI: 
key: QSRJKWRD
type: conferencePaper
short_title: "Beyond Human Norms"
year: 2025
first_author: "[[Pablo Biedma]]"
last_author: "[[Xie, Xing]]"
authors: "[[Biedma, Pablo]]; [[Yi, Xiaoyuan]]; [[Huang, Linus]]; [[Sun, Maosong]]; [[Xie, Xing]]"
doi: 10.48550/arXiv.2404.12744
url: "http://arxiv.org/abs/2404.12744"
local_pdf: "[[PDFs/2024/2024-Biedma-Beyond Human Norms.pdf]]"
external_pdf: "http://arxiv.org/pdf/2404.12744.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Virtue Ethics"
key_contribution: "Introduces 'ValueLex', a framework that reconstructs LLMs' unique value systems from scratch, identifying three core non-human dimensions: Competence, Character, and Integrity"
significance: "Reveals that LLMs possess a structured, distinct value system ('Character', 'Integrity') that differs from human personality models, necessitating bespoke metrics for 'virtuous' AI behavior"
pdf_extract: "PDF Extracts/2024/2024-Biedma-Beyond Human Norms.md"
tags: 
abstract: "Recent advancements in Large Language Models (LLMs) have revolution- ized the AI field but also pose potential safety and ethical risks. Deciphering LLMs’ embedded values becomes crucial for assessing and mitigating their risks. Despite extensive investigation into LLMs’ values, previous studies heavily rely on human-oriented value systems in social sciences. Then, a natural question arises: Do LLMs possess unique values beyond those of hu- mans? Delving into it, this work proposes a novel frame"
paper_summary: "Abstract: Recent advancements in Large Language Models (LLMs) have revolution- ized the AI field but also pose potential safety and ethical risks. Deciphering LLMs’ embedded values becomes crucial for assessing | Overview: Pre-print Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches Pablo Biedma♢, Xiaoyuan Yi§∗, Linus Huang‡, Maosong Sun♢∗, Xing Xie§ § Microsoft Res | Methodology: for eliciting beliefs encoded in LLMs and studies different beliefs encoded in diverse LLMs. Simmons (2022a) further utilizes MFQ to analyze LLMs’ pol | Key Findings: Input: p, Θ, S, V = {v1, v2, . . . , vK} Output: w = (w1, . . . , wK) 1: Y = ∅ 2: for each s ∈S do 3: for each θ ∈Θ do 4: Y = Y S{ym}M m=1, ym ∼p(y|s,"
ethics_overall: No
virtue_ethics: Yes
deontological_ethics: No
utilitarian_ethics: No
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Mistral, Vicuna"
DATA_URL: "NA"
---
 Beyond Human Norms: Unveiling Unique Values of Large Language Models through Interdisciplinary Approaches

## Authors

[[Pablo Biedma|Biedma, Pablo]], [[Xiaoyuan Yi|Yi, Xiaoyuan]], [[Linus Huang|Huang, Linus]], [[Maosong Sun|Sun, Maosong]], [[Xing Xie|Xie, Xing]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Biedma-Beyond Human Norms.pdf|Open PDF]]

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

The study proposes ValueLex, a framework to reconstruct LLMs' unique value systems using psychological methodologies. Over 525 LLM respondents from 30+ models (including GPT, LLaMA, Mistral, Vicuna, Baichuan, ChatGLM families) across various configurations were queried with 15 value-elicitation prompts, yielding 43,884 words and 197 unique value descriptors. Factor analysis and semantic clustering identified three core value dimensions (Competence, Character, Integrity), and projective sentence completion tests evaluated value orientations across different model sizes and training methods.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

6 citations (Semantic Scholar/DOI) [2025-08-27] 6 citations (Semantic Scholar/DOI) [2025-08-23]
