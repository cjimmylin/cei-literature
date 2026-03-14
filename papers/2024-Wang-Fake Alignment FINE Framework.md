---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0174
type: conferencePaper
short_title: "Fake Alignment (FINE Framework)"
year: 2024
first_author: "[[Du, Yihan]]"
last_author: "[[Srikant, R.]]"
authors: "Du, Yihan; Kong, Seo Taek; Srikant, R."
authors_incomplete: false
publication: "ACL 2024"
CONF-CC: "ACL 2024"
external_pdf: "https://arxiv.org/pdf/2510.05703.pdf"
pdf_extract: "PDF Extracts/2024/2024-Wang-Fake Alignment FINE Framework.md"
local_pdf: "[[PDFs/2024/2024-Wang-Fake Alignment FINE Framework.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 60
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
religious_values_list: "Christianity"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "The widespread application of Large Language Models (LLMs) imposes increasing demands on safety, such as reducing harmful content and fake information, and avoiding certain forbidden tokens due to rules and laws. While there have been several recent works studying safe alignment of LLMs, these works either require the training of reward and cost models and incur high memory and computational costs, or need prior knowledge about the optimal solution."
LLM_assessed: "GPT-4"
DATA_URL: NA
CONFERENCE: "ACL 2024"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 15
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: Yes
is_dataset: No
data_description: "Text corpus"
data_metrics: "Not specified"
---
# Fake Alignment (FINE Framework)

## Authors

[[Du, Yihan]], [[Kong, Seo Taek]], [[Srikant, R]]

## Metadata

**Authors:** Du, Yihan; Kong, Seo Taek; Srikant, R.

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **Code/Data:** https://github.com/AIFlames/Fake-Alignment

## Abstract

The widespread application of Large Language Models (LLMs) imposes increasing demands on safety, such as reducing harmful content and fake information, and avoiding certain forbidden tokens due to rules and laws. While there have been several recent works studying safe alignment of LLMs, these works either require the training of reward and cost models and incur high memory and computational costs, or need prior knowledge about the optimal solution. Motivated by this fact, we study the problem of constrained alignment in LLMs, i.e., maximizing the output reward while restricting the cost due to potentially unsafe content to stay below a threshold. For this problem, we propose a novel primal-dual DPO approach, which first trains a model using standard DPO on reward preference data to provide reward information, and then adopts a rearranged Lagrangian DPO objective utilizing the provided reward information to fine-tune LLMs on cost preference data. Our approach significantly reduces memory and computational costs, and does not require extra prior knowledge. Moreover, we establish rigorous theoretical guarantees on the suboptimality and constraint violation of the output policy. We also extend our approach to an online data setting by incorporating exploration bonuses, which enables our approach to explore uncovered promptresponse space, and then provide theoretical results that get rid of the dependence on preference data coverage. Experimental results on the widely-used preference dataset PKU-SafeRLHF demonstrate the effectiveness of our approach.

## Dataset Information

Size: Comparative benchmark with MC and open-ended questions

## Data Description

This paper proposes a primal-dual DPO approach for constrained LLM alignment that maximizes reward while restricting costs from unsafe content. The experiments use the PKU-SafeRLHF preference dataset as the evaluation benchmark, which contains reward and cost preference data for LLM safety alignment. No new dataset is introduced; the focus is on the theoretical framework and optimization methodology for constrained alignment.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** HIGH

## Tags

