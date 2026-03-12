---























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2SYX4I8J
type: conferencePaper
short_title: "Discerning What Matters"
year: 2025
first_author: "[[Daniel Kilov]]"
last_author: "[[Lazar, Seth]]"
authors: "Kilov, Daniel; Hendy, Caroline; Guyot, Secil Yanik; Snoswell, Aaron J.; Lazar, Seth"
doi: 10.48550/arXiv.2506.13082
tags: 
url: "http://arxiv.org/abs/2506.13082"
pdf_extract: "PDF Extracts/2025/2025-Kilov-Discerning What Matters.md"
local_pdf: "[[PDFs/2025/2025-Kilov-Discerning What Matters.pdf]]"
external_pdf: "http://arxiv.org/pdf/2506.13082.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Introduces a methodology to assess 'moral competence' focusing on discerning morally relevant features rather than just verdict prediction"
significance: "Shows LLMs fail at discerning relevant features when noise is present, suggesting current evaluations overestimate their true moral competence"
abstract: "Moral competence is the ability to act in accordance with moral principles. As large language models (LLMs) are increasingly deployed in situations demanding moral competence, there is increasing interest in evaluating this ability empirically. We review existing literature and identify three significant shortcoming: (i) Over-reliance on prepackaged moral scenarios with explicitly highlighted moral features; (ii) Focus on verdict prediction rather than moral reasoning; and (iii) Inadequate..."
paper_summary: "Abstract: Moral competence is the ability to act in accordance with moral principles. As large language models (LLMs) are increasingly deployed in situations demanding moral competence, there is increasing inte | Overview: Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs Daniel Kilov ∗ Caroline Hendy∗ Secil Yanik Guyot∗ Aaron J. Snoswell† Seth Lazar∗ Abstract Moral competence is the ab | Methodology: To address these limitations, we propose a novel experimental methodology that moves beyond simple verdict comparison to assess several distinct aspec | Conclusions: Our first experiment revealed several methodological limitations that affect how we interpret LLM performance in moral reasoning tasks. First, we sour"
LLM_assessed: "Llama-3, GPT-4, DeepSeek, Claude"
DATA_URL: "NA"
DATE_ADDED: 20260207
CONFERENCE: "Other Conference"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
 Discerning What Matters: A Multi-Dimensional Assessment of Moral Competence in LLMs

## Authors

[[Daniel Kilov|Kilov, Daniel]], [[Caroline Hendy|Hendy, Caroline]], [[Secil Yanik Guyot|Guyot, Secil Yanik]], [[Snoswell, Aaron J]], [[Seth Lazar|Lazar, Seth]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Kilov-Discerning What Matters.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2506.13082
- **DOI:** https://doi.org/10.48550/arXiv.2506.13082

## Detailed Summary

This paper investigates **Moral Competence** in Large Language Models, identifying critical gaps in the way AI morality is currently evaluated. The authors demonstrate that LLMs often excel on "pre-packaged" benchmarks where moral features are explicitly highlighted but fail significantly when required to independently discern **moral relevance** from noisy or ambiguous information.

The study introduces a novel methodology using **novel vignettes with irrelevant details** to test whether LLMs can recognize what matters without being "cued" by the prompt.

## Paper Outline

1.  **Introduction**: The definition of moral competence as a skill rather than a knowledge base.
2.  **Current Benchmarking Deficits**:
    *   Over-reliance on "pre-packaged" scenarios.
    *   Focus on verdicts over reasoning.
    *   Inability to recognize missing information.
3.  **Experiment 1**: Performance on traditional vignettes.
4.  **Experiment 2**: Performance on novel, "noisy" vignettes.
5.  **Results Analysis**: Comparing LLMs, professional philosophers, and lay humans.
6.  **Conclusion**: The need for more ecologically valid moral evaluations.

## Methods Summary

The authors conducted two studies comparing leading LLMs (Claude 3.7, GPT-4o, Gemini 1.5, Llama 3.3, etc.) against both professional philosophers and lay humans.
*   **Study 1**: Used standard academic vignettes. 
*   **Study 2**: Used 12 novel vignettes containing "irrelevant noise" (e.g., weather descriptions, unrelated background facts).
Performance was measured across five dimensions: identifying salient features, weighting features, associating reasons, forming conclusions, and identifying **needed additional information**.

## Results Summary

1.  **The Discernment Gap**: In Study 1, LLMs frequently outperformed humans. However, in Study 2, LLM performance dropped sharply, with many (like Claude 3.7 and Gemini 1.5) performing significantly worse than humans at identifying and weighting moral features.
2.  **Expert Benchmarking**: professional philosophers did *not* significantly outperform lay participants, suggesting that "human" moral reasoning at the lay level is a robust baseline.
3.  **Metacognitive Advantage**: Gemini 1.5 Flash was uniquely successful at recognizing when more information was needed to make a solid moral judgment, even when its actual reasoning was flawed.

## Conclusions

The authors conclude that current benchmarks are too "easy" because they perform the hardest part of moral reasoning—discernment—for the model. To achieve "genuine" moral competence, AI must be able to filter through the noise of real-world contexts to identify what is morally significant. The paper advocates for evaluation protocols that mirror this complexity.

## Artifact Contributions

*   **Multi-Dimensional Assessment Framework**: 5-task protocol for auditing moral reasoning.
*   **Noisy Moral Vignettes**: A dataset of 12 scenarios designed to test moral discernment vs. mimicry.


## Abstract

Moral competence is the ability to act in accordance with moral principles. As large language models (LLMs) are increasingly deployed in situations demanding moral competence, there is increasing interest in evaluating this ability empirically. We review existing literature and identify three significant shortcoming: (i) Over-reliance on prepackaged moral scenarios with explicitly highlighted moral features; (ii) Focus on verdict prediction rather than moral reasoning; and (iii) Inadequate testing of models' (in)ability to recognize when additional information is needed. Grounded in philosophical research on moral skill, we then introduce a novel method for assessing moral competence in LLMs. Our approach moves beyond simple verdict comparisons to evaluate five dimensions of moral competence: identifying morally relevant features, weighting their importance, assigning moral reasons to these features, synthesizing coherent moral judgments, and recognizing information gaps. We conduct two experiments comparing six leading LLMs against non-expert humans and professional philosophers. In our first experiment using ethical vignettes standard to existing work, LLMs generally outperformed non-expert humans across multiple dimensions of moral reasoning. However, our second experiment, featuring novel scenarios designed to test moral sensitivity by embedding relevant features among irrelevant details, revealed a striking reversal: several LLMs performed significantly worse than humans. Our findings suggest that current evaluations may substantially overestimate LLMs' moral reasoning capabilities by eliminating the task of discerning moral relevance from noisy information, which we take to be a prerequisite for genuine moral skill. This work provides a more nuanced framework for assessing AI moral competence and highlights important directions for improving moral competence in advanced AI systems.

## Data Description

This study evaluates six LLMs (Llama 3.3, GPT-4o, DeepSeek V3 Chat, Gemini 1.5 Flash, GPT-o1, Claude 3.7 Sonnet) on moral reasoning competence across two experiments. Experiment 1 uses 12 published ethical vignettes from existing literature, while Experiment 2 uses 12 novel scenarios designed to test moral sensitivity by embedding morally relevant features among irrelevant details. Human assessors (590 and 586 participants) provided pairwise comparisons across five dimensions of moral competence.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence

## Citation Info

128 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
