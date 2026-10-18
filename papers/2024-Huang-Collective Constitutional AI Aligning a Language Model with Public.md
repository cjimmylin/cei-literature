---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0153
type: preprint
short_title: "Collective Constitutional AI: Aligning a Language Model with Public Input"
year: 2024
first_author: "[[Saffron Huang]]"
last_author: "[[Deep Ganguli]]"
authors: "Saffron Huang; Divya Siddarth; Liane Lovitt; Thomas I. Liao; Esin Durmus; Alex Tamkin; Deep Ganguli"
doi: 10.1145/3630106.3658979
url: "https://arxiv.org/abs/2406.07814"
external_pdf: "https://arxiv.org/pdf/2406.07814.pdf"
pdf_extract: "PDF Extracts/2024/2024-Huang-Collective Constitutional AI Aligning a Language Model with Public.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Huang-Collective Constitutional AI Aligning a Language Model with Public.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
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
abstract: "There is growing consensus that language model (LM) developers should not be the sole deciders of LM behavior, creating a need for methods that enable the broader public to collectively shape the behavior of LM systems that affect them. To address this need, we present Collective Constitutional AI (CCAI): a multi-stage process for sourcing and integrating public input into LMs—from identifying a target population to sourcing principles to training and evaluating a model."
LLM_assessed: Claude
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: 75
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "General Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: BR
author_region: "Latin America & Caribbean"
author_global_north_south: "Global South"
weird_score: 45
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation methodology"
data_metrics: "Not specified"
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

