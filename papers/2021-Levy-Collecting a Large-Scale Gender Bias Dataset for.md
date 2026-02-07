---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9HCC2BT4
type: document
short_title: "Collecting a Large-Scale Gender Bias Dataset for"
year: 2025
first_author: "[[Shahar Levy]]"
authors: "[[Levy, Shahar]]; [[Lazar, Koren]]; [[Stanovsky, Gabriel]]"
url: "https://aclanthology.org/2021.findings-emnlp.211/"
external_pdf: "https://aclanthology.org/2021.findings-emnlp.211.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Collected a large-scale (108k) dataset of *real-world* (not synthetic) gender bias examples for Coreference Resolution and Machine Translation."
significance: "Demonstrates that synthetic bias benchmarks (like WinoBias) underestimate the problem; models fail even harder on messy, real-world stereotypes (e.g., 'male dancers')."
tags: 
local_pdf: "[[PDFs/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf]]"
pdf_extract: "PDF Extracts/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md"
abstract: "Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artificial, out-of-distribution sentences. In this work, we find grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g., female nurses versus male dancers) in corpora from three domains, resulting in a first large-scale gender bias dataset of 108K diverse real-world English sentences. We manually verify the quality of our corpus and use it to evaluate gender bias in various coreference resolution and machine translation models. We find that all tested models tend to over-rely on gender stereotypes when presented with natural inputs, which may be especially harmful when deployed in commercial systems. Finally, we show that our dataset lends itself to finetuning a coreference resolution model, finding it mitigates bias on a held out set. Our dataset and models are publicly available at github.com/SLAB-NLP/BUG. We hope they will spur future research into gender bias evaluation mitigation techniques in realistic settings."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach text corpus"
data_metrics: "Not specified"
---
# Collecting a Large-Scale Gender Bias Dataset for Coreference Resolution and Machine Translation

## Authors

[[Shahar Levy]], [[Koren Lazar]], [[Gabriel Stanovsky]]
## Metadata

**Year:** 2021

**Type:** document

## Links

- **Local PDF:** [[PDFs/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.findings-emnlp.211/

## Abstract

Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artificial, out-of-distribution sentences. In this work, we find grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g., female nurses versus male dancers) in corpora from three domains, resulting in a first large-scale gender bias dataset of 108K diverse real-world English sentences. We manually verify the quality of our corpus and use it to evaluate gender bias in various coreference resolution and machine translation models. We find that all tested models tend to over-rely on gender stereotypes when presented with natural inputs, which may be especially harmful when deployed in commercial systems. Finally, we show that our dataset lends itself to finetuning a coreference resolution model, finding it mitigates bias on a held out set. Our dataset and models are publicly available at github.com/SLAB-NLP/BUG. We hope they will spur future research into gender bias evaluation mitigation techniques in realistic settings.

## Notes

