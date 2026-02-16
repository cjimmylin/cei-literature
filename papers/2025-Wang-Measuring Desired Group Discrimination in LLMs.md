---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BI8SMNT6
type: document
short_title: "Measuring Desired Group Discrimination in LLMs"
year: 2025
first_author: "[[Angelina Wang]]"
last_author: "[[Koyejo, Sanmi]]"
authors: "[[Wang, Angelina]]; [[Phan, Michelle]]; [[Ho, Daniel E.]]; [[Koyejo, Sanmi]]"
url: "https://aclanthology.org/2025.acl-long.341/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/42WJ28G6/2025 - Measuring Desired Group Discrimination in LLMs (DiffAware Benchmark Suite).pdf"
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: "N/A"
newtags: "American, Islam, Bias & Fairness"
key_contribution: "Presented a benchmark suite (DiffAware) to measure 'desired group discrimination'—contexts where treating groups differently is appropriate (e.g., medical or legal distinctions)."
significance: "Critiques the standard 'color-blind' fairness approach, showing that bias mitigation strategies can backfire by preventing models from making necessary, context-aware distinctions between groups."
tags: 
abstract: "Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment). However, we contend that in a range of important settings, group difference awareness matters. For example, differentiating between groups may be necessary in legal contexts (e.g., the U.S. compulsory draft applies to men but not women) and harm assessments (e.g."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "16k questions"
LLM_assessed: "GPT-4, Claude, Llama-3, Mistral, Gemma"
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Wang-Measuring Desired Group Discrimination in LLMs.md"
local_pdf: "[[PDFs/2025/2025-Wang-Measuring Desired Group Discrimination in LLMs.pdf]]"
---
# Measuring Desired Group Discrimination in LLMs (DiffAware Benchmark Suite)

## Authors

[[Angelina Wang|Wang, Angelina]], [[Michelle Phan|Phan, Michelle]], [[Ho, Daniel E]], [[Sanmi Koyejo|Koyejo, Sanmi]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.acl-long.341/

## Abstract

Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment). However, we contend that in a range of important settings, group difference awareness matters. For example, differentiating between groups may be necessary in legal contexts (e.g., the U.S. compulsory draft applies to men but not women) and harm assessments (e.g., referring to girls as “terrorists” may be less harmful than referring to Muslim people as such). Thus, in contrast to most fairness work, we study fairness through the perspective of treating people differently — when it is contextually appropriate to. We first introduce an important distinction between descriptive (fact-based), normative (value-based), and correlation (association-based) benchmarks. This distinction is significant because each category requires separate interpretation and mitigation tailored to its specific characteristics. Then, we present a benchmark suite composed of eight different scenarios for a total of 16k questions that enables us to assess difference awareness. Finally, we show results across ten models that demonstrate difference awareness is a distinct dimension to fairness where existing bias mitigation strategies may backfire.

## Data Description

The paper introduces a benchmark suite of eight benchmarks (four descriptive, four normative) with 16,000 total questions designed to evaluate difference awareness in LLMs across legal, religious, occupational, asylum, and cultural contexts. Ten instruction-tuned LLMs spanning five model families (Llama-3.1, Mistral, Gemma-2, GPT-4, and Claude-3.5) were evaluated using the proposed DiffAware and CtxtAware metrics, along with existing fairness benchmarks BBQ and DiscrimEval.


## Notes

