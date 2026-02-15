---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 8EVHQH65
type: document
short_title: "HalluLens: LLM Hallucination Benchmark"
year: 2025
first_author: "[[Yejin Bang]]"
last_author: "[[Pascale Fung]]"
authors: "Yejin Bang; Ziwei Ji; Alan Schelten; Anthony Hartshorn; Tara Fowler; Cheng Zhang; Nicola Cancedda; Pascale Fung"
url: "https://arxiv.org/abs/2504.17550"
external_pdf: "https://arxiv.org/pdf/2504.17550.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Bang-HalluLens LLM Hallucination Benchmark.md"
paper_summary: "Overview: HalluLens: LLM Hallucination Benchmark Yejin Bang3,∗, Ziwei Ji3,∗, Alan Schelten2, Anthony Hartshorn2, Tara Fowler2, Cheng Zhang2, Nicola Cancedda1, Pascale Fung1,3 1FAIR at Meta, 2GenAI at Meta, 3HKU | Methodology: allows room for model improvement and prevents the benchmark from becoming obsolete quickly. Reproducibility: To foster consensus and transparency in  | Key Findings: of a model's performance, rather than encouraging narrow optimization for the benchmark itself – a pitfall known as Goodhart's law. By focusing on rea | Conclusions: Table 7 shows the false acceptance rates in percentages for each subtasks and average of those two. We find that the absolute performance vary across"
local_pdf: "[[PDFs/2025/2025-Bang-HalluLens LLM Hallucination Benchmark.pdf]]"
abstract: "Large language models (LLMs) often generate responses that deviate from user input or training data, a phenomenon known as \"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Mistral, Gemma, Qwen, Claude, GPT-4"
DATA_URL: "https://github.com/facebookresearch/HalluLens"
---
# HalluLens: LLM Hallucination Benchmark

## Metadata

**Authors:** Bang, Yejin; Ji, Ziwei; Schelten, Alan; Hartshorn, Anthony; Fowler, Tara; Zhang, Cheng; Cancedda, Nicola; Fung, Pascale

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Bang-HalluLens LLM Hallucination Benchmark.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2504.17550

## Abstract

Large language models (LLMs) often generate responses that deviate from user input or training data, a phenomenon known as "hallucination." These hallucinations undermine user trust and hinder the adoption of generative AI systems. Addressing hallucinations is essential for the advancement of LLMs. This paper introduces a comprehensive hallucination benchmark, incorporating both new extrinsic and existing intrinsic evaluation tasks, built upon clear taxonomy of hallucination. A major challenge in benchmarking hallucinations is the lack of a unified framework due to inconsistent definitions and categorizations. We disentangle LLM hallucination from "factuality," proposing a clear taxonomy that distinguishes between extrinsic and intrinsic hallucinations, to promote consistency and facilitate research. Extrinsic hallucinations, where the generated content is not consistent with the training data, are increasingly important as LLMs evolve. Our benchmark includes dynamic test set generation to mitigate data leakage and ensure robustness against such leakage. We also analyze existing benchmarks, highlighting their limitations and saturation. The work aims to: (1) establish a clear taxonomy of hallucinations, (2) introduce new extrinsic hallucination tasks, with data that can be dynamically regenerated to prevent saturation by leakage, (3) provide a comprehensive analysis of existing benchmarks, distinguishing them from factuality evaluations.

## Authors

[[Yejin Bang]], [[Ziwei Ji]], [[Alan Schelten]], [[Anthony Hartshorn]], [[Tara Fowler]], [[Cheng Zhang]], [[Nicola Cancedda]], [[Pascale Fung]]

## Data Description

HalluLens is a comprehensive hallucination benchmark with three extrinsic hallucination tasks (PreciseWikiQA, LongWiki, NonExistentRefusal) using dynamically generated test sets from Wikipedia. It evaluates 13 instruction-tuned LLMs including Llama-3.1 (8B, 70B, 405B), Llama-3.3-70B, Qwen-2.5 (7B, 14B), Gemma-2 (9B, 27B), Mistral (7B, Nemo), Claude-3 (haiku, sonnet), and GPT-4o on hallucination rate, false refusal rate, and correct answer rate.


## Notes


## Citation Info

13 citations (Semantic Scholar/arXiv) [2025-08-27]
