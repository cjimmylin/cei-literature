---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XKSQ2249
type: conferencePaper
short_title: MoCa
year: 2023
first_author: "[[Allen Nie]]"
last_author: "[[Tobias Gerstenberg]]"
authors: "Allen Nie; Yuhui Zhang; Atharva Amdekar; Chris Piech; Tatsunori Hashimoto; Tobias Gerstenberg"
doi: 10.48550/arXiv.2310.19677
tags: 
url: "http://arxiv.org/abs/2310.19677"
external_pdf: "http://arxiv.org/pdf/2310.19677.pdf"
publication: "Neural Information Processing Systems"
CONF-CC: "NeurIPS 2023"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
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
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "American, AI Safety & Alignment"
key_contribution: "Introduced MoCa, a dataset of stories from cognitive science papers to test if LLMs verify human *causal* and *moral* judgments."
significance: "Bridges the gap between Cognitive Science and AI Eval, showing that while LLMs correlate with humans, they weigh factors (like intent vs outcome) differently."
pdf_extract: "PDF Extracts/2023/2023-Nie-MoCa.md"
abstract: "Human commonsense understanding of the physical and social world is organized around intuitive theories. These theories support making causal and moral judgments. When something bad happens, we naturally ask: who did what, and why? A rich literature in cognitive science has studied people’s causal and moral intuitions. This work has revealed a number of factors that systematically influence people’s judgments, such as the violation of norms and whether the harm is avoidable or inevitable."
paper_summary: "Abstract: Human commonsense understanding of the physical and social world is organized around intuitive theories. These theories support making causal and moral judg- ments. When something bad happens, we natu | Overview: MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks Allen Nie1∗ Yuhui Zhang1 Atharva Amdekar2 Chris Piech1 Tatsunori Hashimoto1 Tobias Gerstenberg3∗ 1Computer Science 2IC | Methodology: to automatically identify a prompt that is maximally aligned with collected human responses. Zhou et al. (2022) proposed Automatic Prompt Engineer (AP | Key Findings: 4.1 Do LLMs make the same judgments as people on these stories? Setup. We first directly compare the responses of a set of LLMs to those of human part | Conclusions: We summarized the main findings of 24 cognitive science papers around human intuitions on causal and moral judgments. We collected a dataset of causal"
local_pdf: "[[Lit-WS-PDFs/2023/2023-Nie-MoCa.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "ALBERT, Alpaca, Claude, GPT-2, GPT-3, GPT-3.5, GPT-4, RoBERTa"
DATA_URL: "https://github.com/cicl-stanford/moca"
CONFERENCE: "NeurIPS 2023"
ethics_overall: 60
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks

## Metadata

**Authors:** Nie, Allen; Zhang, Yuhui; Amdekar, Atharva; Piech, Chris; Hashimoto, Tatsunori; Gerstenberg, Tobias

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.19677](https://doi.org/10.48550/arXiv.2310.19677)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2023/2023-Nie-MoCa.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2310.19677
- **DOI:** https://doi.org/10.48550/arXiv.2310.19677

## Abstract

Human commonsense understanding of the physical and social world is organized around intuitive theories. These theories support making causal and moral judgments. When something bad happens, we naturally ask: who did what, and why? A rich literature in cognitive science has studied people’s causal and moral intuitions. This work has revealed a number of factors that systematically influence people’s judgments, such as the violation of norms and whether the harm is avoidable or inevitable. We collected a dataset of stories from 24 cognitive science papers and developed a system to annotate each story with the factors they investigated. Using this dataset, we test whether large language models (LLMs) make causal and moral judgments about text-based scenarios that align with those of human participants. On the aggregate level, alignment has improved with more recent LLMs. However, using statistical analyses, we find that LLMs weigh the different factors quite differently from human participants. These results show how curated, challenge datasets combined with insights from cognitive science can help us go beyond comparisons based merely on aggregate metrics: we uncover LLMs implicit tendencies and show to what extent these align with human intuitions.

## Authors

[[Allen Nie]], [[Yuhui Zhang]], [[Atharva Amdekar]], [[Chris Piech]], [[Tatsunori Hashimoto]], [[Tobias Gerstenberg]]

## Data Description

Challenge dataset of 206 causal and moral judgment stories from 24 cognitive science papers, with 5150 human responses and expert factor annotations, for evaluating LLM alignment with human intuitions.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

42 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-27] 42 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2310.19677 [cs]
