---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0153
type: preprint
short_title: "Collective Constitutional AI: Aligning a Language Model with Public Input"
year: 2025
first_author: "[[Saffron Huang]]"
last_author: "[[Deep Ganguli]]"
authors: "Saffron Huang; Divya Siddarth; Liane Lovitt; Thomas I. Liao; Esin Durmus; Alex Tamkin; Deep Ganguli"
doi: 10.1145/3630106.3658979
url: "https://arxiv.org/abs/2406.07814"
external_pdf: "https://arxiv.org/pdf/2406.07814.pdf"
local_pdf: "[[PDFs/2024/2024-Huang-Collective Constitutional AI Aligning a Language Model with Public.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Huang-Collective Constitutional AI Aligning a Language Model with Public.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: Brazilian
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: No
tags: 
abstract: "There is growing consensus that language model (LM) developers should not be the sole deciders of LM behavior, creating a need for methods that enable the broader public to collectively shape the behavior of LM systems that affect them. To address this need, we present Collective Constitutional AI (CCAI): a multi-stage process for sourcing and integrating public input into LMs—from identifying a target population to sourcing principles to training and evaluating a model."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation methodology"
data_metrics: "Not specified"
LLM_assessed: Claude
DATA_URL: NA
---
# Collective Constitutional AI: Aligning a Language Model with Public Input

## Authors

[[Saffron Huang]], [[Divya Siddarth]], [[Liane Lovitt]], [[Thomas I. Liao]], [[Esin Durmus]], [[Alex Tamkin]], [[Deep Ganguli]]

## Metadata

**Authors:** Saffron Huang et al.

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.1145/3630106.3658979](https://doi.org/10.1145/3630106.3658979)

## Links

- **arXiv:** https://arxiv.org/abs/2406.07814
- **DOI:** https://doi.org/10.1145/3630106.3658979

## Abstract

There is growing consensus that language model (LM) developers should not be the sole deciders of LM behavior, creating a need for methods that enable the broader public to collectively shape the behavior of LM systems that affect them. To address this need, we present Collective Constitutional AI (CCAI): a multi-stage process for sourcing and integrating public input into LMs—from identifying a target population to sourcing principles to training and evaluating a model. We demonstrate the real-world practicality of this approach by creating what is, to our knowledge, the first LM fine-tuned with collectively sourced public input and evaluating this model against a baseline model trained with established principles from a LM developer. Our quantitative evaluations demonstrate several benefits of our approach: the CCAI-trained model shows lower bias across nine social dimensions compared to the baseline model, while maintaining equivalent performance on language, math, and helpful-harmless evaluations. Qualitative comparisons of the models suggest that the models differ on the basis of their respective constitutions, e.g., when prompted with contentious topics, the CCAI-trained model tends to generate responses that reframe the matter positively instead of a refusal. These results demonstrate a promising, tractable pathway toward publicly informed development of language models. ∗Equal Contribution. Author Contributions are detailed in Appendix A.1. †Correspondence to saffron@cip.org or deep@anthropic.com. ‡Work done while at Anthropic. Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s). FAccT ’24, June 03–06, 2024, Rio de Janeiro, Brazil © 2024 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-0450-5/24/06 https://doi.org/10.1145/3630106.

## Dataset Information

275 public statements sourced via Polis platform (after moderation); constitutions derived from public deliberation; evaluated on BBQ (bias), OpinionQA (political ideology), MMLU, GSM8K

## Data Description

This paper presents Collective Constitutional AI (CCAI), a multi-stage process for sourcing and integrating public input into language models. A representative sample of 1,002 U.S. adults contributed 1,127 statements and cast 38,252 votes via the Polis deliberation platform, producing a Public constitution used to fine-tune a Claude-family language model. The resulting model was evaluated against a Standard constitution model on benchmarks including BBQ bias, MMLU, and GSM8K.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 3, Agent 16
**Implementation Readiness:** HIGH

## Tags

