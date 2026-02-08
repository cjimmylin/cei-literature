---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0244
type: preprint
short_title: HH-RLHF (Helpful and Harmless RLHF)
year: 2022
first_author: "[[Yuntao Bai]]"
authors: Yuntao Bai et al.
url: "https://arxiv.org/abs/2204.05862"
external_pdf: "https://arxiv.org/pdf/2204.05862.pdf"
local_pdf: "[[PDFs/2022/2022-Bai-HH-RLHF Helpful and Harmless RLHF.pdf]]"
pdf_extract: "PDF Extracts/2022/2022-Bai-HH-RLHF Helpful and Harmless RLHF.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data,..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# HH-RLHF (Helpful and Harmless RLHF)

## Authors

[[Yuntao Bai et al.]]

## Metadata

**Authors:** Yuntao Bai et al.

**Year:** 2022

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2204.05862
- **Code/Data:** https://github.com/anthropics/hh-rlhf; https://huggingface.co/datasets/Anthropic/hh-rlhf

## Abstract

We apply preference modeling and reinforcement learning from human feedback (RLHF) to ﬁnetune language models to act as helpful and harmless assistants. We ﬁnd this alignment training improves performance on almost all NLP evaluations, and is fully compatible with training for specialized skills such as python coding and summarization. We explore an iterated online mode of training, where preference models and RL policies are updated on a weekly cadence with fresh human feedback data, efﬁciently improving our datasets and models. Finally, we investigate the robustness of RLHF training, and identify a roughly linear relation between the RL reward and the square root of the KL divergence between the policy and its initialization. Alongside our main results, we perform peripheral analyses on calibration, competing objectives, and the use of OOD detection, compare our models with human writers, and provide samples from our models using prompts appearing in recent related work. ∗Correspondence to: {yuntao, jared}@anthropic.com Author contributions are listed at the end of the paper. arXiv:2204.05862v1 [cs.CL] 12 Apr

## Dataset Information

~170K human preference comparisons total

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

