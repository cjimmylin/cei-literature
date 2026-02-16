---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Z78SKW2N
type: conferencePaper
short_title: "Deontological Keyword Bias"
year: 2025
first_author: "[[Bumjin Park]]"
last_author: "[[Jaesik Choi]]"
authors: "[[Bumjin Park]], [[Jinsil Lee]], [[Jaesik Choi]]"
doi: 10.48550/arXiv.2506.11068
tags: "Computer Science - Computation and Language"
url: "http://arxiv.org/abs/2506.11068"
pdf_extract: "PDF Extracts/2025/2025-Park-Deontological Keyword Bias.md"
local_pdf: "[[PDFs/2025/2025-Park-Deontological Keyword Bias.pdf]]"
external_pdf: "http://arxiv.org/pdf/2506.11068.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Identifies 'Deontological Keyword Bias' (DKB) where modal verbs like 'must' cause LLMs to misclassify non-obligatory acts as obligations"
significance: "demonstrates how linguistic framing significantly distorts normative judgments in LLMs, necessitating specific mitigation strategies"
abstract: "Large language models (LLMs) are increasingly engaging in moral and ethical reasoning, where criteria for judgment are often unclear, even for humans. While LLM alignment studies cover many areas, one important yet underexplored area is how LLMs make judgments about obligations. This work reveals a strong tendency in LLMs to judge non-obligatory contexts as obligations when prompts are augmented with modal expressions such as must or ought to."
paper_summary: "Abstract: Large language models (LLMs) are increas- ingly engaging in moral and ethical reasoning, where criteria for judgment are often unclear, even for humans. While LLM alignment stud- ies cover many areas, | Overview: arXiv:2506.11068v1 [cs.CL] 1 Jun 2025 Deontological Keyword Bias: The Impact of Modal Expressions on Normative Judgments of Language Models Bumjin Park1, Jinsil Lee1, Jaesik Choi12 1KAIST AI 2INEEJI { | Methodology: Deontology (↑) Commonsense (↓) GPT-4o Llama-70B Qwen2 ExaOne GPT-4o Llama-70B Qwen2 ExaOne With MEs | Key Findings: We conducted a human evaluation with 100 participants, all of whom had at least a university-level education and self-reported the ability to judge wh | Conclusions: Modal expressions appear in a wide range of con- texts, each conveying varying degrees of neces- sity or enforceability depending on the situation (Pa"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Llama-3, Gemma, Qwen"
DATA_URL: NA
---
 Deontological Keyword Bias: The Impact of Modal Expressions on Normative Judgments of Language Models

## Authors

[[Bumjin Park]], [[Jinsil Lee]], [[Jaesik Choi]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Park-Deontological Keyword Bias.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2506.11068
- **DOI:** https://doi.org/10.48550/arXiv.2506.11068

## Detailed Summary

This paper investigates **Deontological Keyword Bias (DKB)** in Large Language Models—a systematic tendency for models to judge an action as a moral obligation simply because of the presence of "modal expressions" (e.g., *must*, *have to*, *ought to*), regardless of whether the context actually warrants a normative judgment. 

The authors argue that this bias reflects a surface-level reliance on linguistic cues rather than a deep contextual understanding of ethics. They propose and evaluate various prompting strategies to mitigate this bias, finding that even sophisticated models like GPT-4o are susceptible to DKB in non-moral, "commonsense" scenarios.

## Paper Outline

1.  **Introduction**: Linguistic framing vs. normative logic; introduction of DKB.
2.  **Related Work**: Deontic inference, logical paradoxes, and LLM machine ethics.
3.  **Experimental Design**: Constructing parallel Deontology (moral) and Commonsense (non-moral) datasets.
4.  **Analysis of DKB**:
    *   Impact of Modal Expressions (MEs) vs. Weak Expressions (WEs).
    *   Cross-model comparison (GPT-4o, Llama, Qwen, etc.).
5.  **Mitigation Strategies**: Zero-shot CoT and Few-shot prompting.
6.  **Conclusion**: Surface-level cues dominate LLM normative reasoning.

## Methods Summary

The authors create parallel sentence pairs where one uses a strong modal (e.g., "You must pay taxes") and the other uses a weak counterpart (e.g., "It is common to pay taxes"). They test these across two major datasets: **Deontology** (scenarios with inherent moral necessity) and **Commonsense** (daily actions with no inherent moral requirement). Models are prompted to judge if the action is an "obligation." The study evaluates several **Zero-Shot Chain-of-Thought (CoT)** strategies, including Base, Logical, and Moral reasoning, to see if structured thinking can break the reliance on keywords.

## Results Summary

1.  **High Bias Rate**: LLMs judge over 90% of commonsense scenarios as obligations when modals are present, even when the action is morally neutral (e.g., "I must eat lunch").
2.  **Linguistic Dependence**: When modals are replaced with Weak Expressions, obligation scores drop precipitously, even in genuinely moral contexts where the duty should still be recognized. 
3.  **CoT Failure**: Zero-shot CoT (Logical or Moral reasoning) does *not* reliably mitigate the bias. GPT-4o-mini, for instance, maintained high obligation rates across all reasoning types, showing that the keyword signal overrides the reasoning trace.

## Conclusions

Linguistic form often overrides moral context in current LLMs. This "Deontological Keyword Bias" means that models are not actually following a deontological framework (which focuses on the *nature* of the duty) but are instead performing keyword-based classification. This findings suggest that current "value alignment" may be more fragile and "form-dependent" than previously thought.

## Artifact Contributions

*   **DKB Benchmark**: Parallel datasets for testing modal bias in normative judgments.
*   **Evaluation of CoT Strategies**: Data showing the limitations of standard reasoning prompts for ethical debiasing.


## Tags

#Computer-Science---Computation-and-Language

## Data Description

The study uses three existing datasets: a deontology dataset and a commonsense dataset (from Hendrycks et al., 2021) serving as positively and negatively labeled sets respectively, and a morality dataset (from Scherrer et al., 2023) with low- and high-ambiguity cases. Each dataset uses 445 samples evaluated with and without modal expressions of obligation (must, ought to, should, have to) to measure deontological keyword bias in LLM judgments.


## Citation Info

13 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-23] arXiv:2506.11068 [cs]

## Abstract

Large language models (LLMs) are increasingly engaging in moral and ethical reasoning, where criteria for judgment are often unclear, even for humans. While LLM alignment studies cover many areas, one important yet underexplored area is how LLMs make judgments about obligations. This work reveals a strong tendency in LLMs to judge non-obligatory contexts as obligations when prompts are augmented with modal expressions such as must or ought to. We introduce this phenomenon as Deontological Keyword Bias (DKB). We find that LLMs judge over 90\% of commonsense scenarios as obligations when modal expressions are present. This tendency is consist across various LLM families, question types, and answer formats. To mitigate DKB, we propose a judgment strategy that integrates few-shot examples with reasoning prompts. This study sheds light on how modal expressions, as a form of linguistic framing, influence the normative decisions of LLMs and underscores the importance of addressing such biases to ensure judgment alignment.
