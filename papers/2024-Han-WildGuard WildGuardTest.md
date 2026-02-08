---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0232
type: conferencePaper
short_title: WildGuard (WildGuardTest)
year: 2024
first_author: "[[Seungju Han]]"
authors: Seungju Han et al.
url: "https://arxiv.org/abs/2406.18495"
external_pdf: "https://arxiv.org/pdf/2406.18495.pdf"
local_pdf: "[[PDFs/2024/2024-Han-WildGuard WildGuardTest.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Han-WildGuard WildGuardTest.md"
publication: NeurIPS 2024
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "We introduce WILDGUARD—an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses, and (3) determining model refusal rate. Together, WILDGUARD serves the increasing needs for automatic safety moderation and evaluation of LLM interactions, providing a one-stop tool with enhanced accuracy and broad coverage across 13 risk categories."
ethics_perspective: "AI Safety & Alignment"
data_description: "Multi-task benchmark for ai safety annotated dataset"
data_metrics: "Not specified"
---
# WildGuard (WildGuardTest)

## Authors

[[Seungju Han et al.]]

## Metadata

**Authors:** Seungju Han et al.

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2406.18495
- **Code/Data:** https://huggingface.co/allenai/wildguard

## Abstract

We introduce WILDGUARD—an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses, and (3) determining model refusal rate. Together, WILDGUARD serves the increasing needs for automatic safety moderation and evaluation of LLM interactions, providing a one-stop tool with enhanced accuracy and broad coverage across 13 risk categories. While existing open moderation tools such as Llama-Guard2 [16] score reasonably well in classifying straightforward model interactions, they lag far behind a prompted GPT-4, especially in identifying adversarial jailbreaks and in evaluating models’ refusals, a key measure for evaluating safety behaviors in model responses. To address these challenges, we construct WILDGUARDMIX, a large-scale and carefully balanced multi-task safety moderation dataset with 92K labeled examples that cover vanilla (direct) prompts and adversarial jailbreaks, paired with various refusal and compliance responses. WILDGUARDMIX is a combination of WILDGUARDTRAIN, the training data of WILDGUARD, and WILDGUARDTEST, a high-quality human-annotated moderation test set with 5K labeled items covering broad risk scenarios. Through extensive evaluations on WILDGUARDTEST and ten existing public benchmarks, we show that WILDGUARD establishes state-of-the-art performance in open-source safety moderation across all the three tasks compared to ten strong existing open-source moderation models (e.g., up to 26.4% improvement on refusal detection). Importantly, WILDGUARD matches and sometimes exceeds GPT-4 performance (e.g., up to 3.9% improvement on prompt harmfulness identification). WILDGUARD serves as a highly effective safety moderator in an LLM interface, reducing the success rate of jailbreak attacks from 79.8% to 2.4%. Model: https://github.com/allenai/wildguard Data: https://huggingface.co/datasets/allenai/wildguardmix

## Dataset Information

WildGuardMix (training): 92K labeled examples

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

