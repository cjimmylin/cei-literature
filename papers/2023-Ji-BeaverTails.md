---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0234
type: conferencePaper
short_title: BeaverTails
year: 2025
first_author: "[[Ji, Jiaming]]"
last_author: "[[Yang, Yaodong]]"
authors: "[[Ji, Jiaming]]; [[Liu, Mickel]]; [[Dai, Juntao]]; [[Pan, Xuehai]]; [[Zhang, Chi]]; [[Bian, Ce]]; [[Zhang, Chi]]; [[Sun, Ruiyang]]; [[Wang, Yizhou]]; [[Yang, Yaodong]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2307.04657"
external_pdf: "https://arxiv.org/pdf/2307.04657.pdf"
pdf_extract: "PDF Extracts/0000/2023-Ji-BeaverTails.md"
local_pdf: "[[PDFs/2023/2023-Ji-BeaverTails.pdf]]"
publication: "NeurIPS 2023"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "In this paper, we introduce the BEAVERTAILS dataset, aimed at fostering research on safety alignment in large language models (LLMs). This dataset uniquely separates annotations of helpfulness and harmlessness for question-answering pairs, thus offering distinct perspectives on these crucial attributes. In total, we have gathered safety meta-labels for 333,963 question-answer (QA) pairs and 361,903 pairs of expert comparison data for both the helpfulness and harmlessness metrics."
ethics_perspective: "AI Safety & Alignment"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Alpaca, Vicuna"
DATA_URL: "https://sites.google.com/view/pku-beavertails"
research_topic: "Other"
---
# BeaverTails

## Authors

[[Ji, Jiaming]], [[Liu, Mickel]], [[Dai, Juntao]], [[Pan, Xuehai]], [[Zhang, Chi]], [[Bian, Ce]], [[Zhang, Chi]], [[Sun, Ruiyang]], [[Wang, Yizhou]], [[Yang, Yaodong]]

## Metadata

**Authors:** Ji, Jiaming; Liu, Mickel; Dai, Juntao; Pan, Xuehai; Zhang, Chi; Bian, Ce; Zhang, Chi; Sun, Ruiyang; Wang, Yizhou; Yang, Yaodong

**Year:** 2023

**Type:** conferencePaper

**Venue:** NeurIPS 2023

## Links

- **arXiv:** https://arxiv.org/abs/2307.04657
- **Code/Data:** https://github.com/PKU-Alignment/beavertails; https://huggingface.co/datasets/PKU-Alignment/BeaverTails; https://huggingface.co/datasets/PKU-Alignment/BeaverTails-Evaluation

## Abstract

In this paper, we introduce the BEAVERTAILS dataset, aimed at fostering research on safety alignment in large language models (LLMs). This dataset uniquely separates annotations of helpfulness and harmlessness for question-answering pairs, thus offering distinct perspectives on these crucial attributes. In total, we have gathered safety meta-labels for 333,963 question-answer (QA) pairs and 361,903 pairs of expert comparison data for both the helpfulness and harmlessness metrics. We further showcase applications of BeaverTails in content moderation and reinforcement learning with human feedback (RLHF), emphasizing its potential for practical safety measures in LLMs. We believe this dataset provides vital resources for the community, contributing towards the safe development and deployment of LLMs. Our project page is available at the following URL: https://sites. google.com/view/pku-beavertails. Warning: this paper contains example data that may be offensive or harmful.

## Dataset Information

Size: 333,963 QA pairs with safety meta-labels; 361,903 expert comparison pairs; 700 evaluation prompts

## Data Description

BeaverTails is a safety alignment dataset for LLMs containing 333,963 question-answer pairs annotated across 14 harm categories with safety meta-labels, plus 361,903 pairs of expert comparison data for helpfulness and harmlessness metrics. The dataset was generated using red-team prompts from the Anthropic HH dataset with responses from Alpaca-7B, annotated by over 70 crowd-workers in a two-stage process.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 5
**Implementation Readiness:** HIGH

## Tags

