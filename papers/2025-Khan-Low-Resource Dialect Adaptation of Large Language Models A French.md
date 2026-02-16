---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0438
type: preprint
short_title: "Low-Resource Dialect Adaptation of Large Language Models: A French Dialect Case-Study"
year: 2025
first_author: "[[Khan, Eeham]]"
last_author: "[[Kosseim, Leila]]"
authors: "[[Khan, Eeham]]; [[Saidani, Firas]]; [[Van Esbroeck, Owen]]; [[Khoury, Richard]]; [[Kosseim, Leila]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.22747"
external_pdf: "https://arxiv.org/pdf/2510.22747.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Khan-Low-Resource Dialect Adaptation of Large Language Models A French.md"
local_pdf: "[[PDFs/2025/2025-Khan-Low-Resource Dialect Adaptation of Large Language Models A French.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: "French, Quebecois French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "CroissantLLM, Llama-3.1, Llama-3.2"
DATA_URL: "https://github.com/CLaC-Lab/QuebecLLM-CPT"
tags: 
abstract: "Despite the widespread adoption of large language models (LLMs), their strongest capabilities remain largely confined to a small number of high-resource languages for which there is abundant training data. Recently, continual pretraining (CPT) has emerged as a means to fine-tune these models to low-resource regional dialects. In this paper, we study the use of CPT for dialect learning under tight data and compute budgets."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# Low-Resource Dialect Adaptation of Large Language Models: A French Dialect Case-Study

## Authors

[[Khan, Eeham]], [[Saidani, Firas]], [[Van Esbroeck, Owen]], [[Khoury, Richard]], [[Kosseim, Leila]]

## Metadata

**Authors:** Eeham Khan; Firas Saidani; Owen Van Esbroeck; Richard Khoury; Leila Kosseim

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French, Quebecois French

## Links

- **arXiv:** https://arxiv.org/abs/2510.22747

## Abstract

Adapts three LLMs to Quebecois French dialect using a small dataset and benchmarks them on the COLE suite. Shows continued pre-training with LoRA achieves dialectal gains with minimal regression on prestige French. Highlights that systems defaulting to prestige French can normalize away regional features and reinforce linguistic hierarchies.

## Summary

This paper explores continual pre-training for dialect adaptation in low-resource settings, using Quebec French as a case study. The authors adapt three LLMs (CroissantLLM, Llama-3.2-1B, Llama-3.1-8B) using parameter-efficient fine-tuning with LoRA on a very small 86M token corpus, updating less than 1% of model parameters. Evaluation on the COLE benchmark suite demonstrates improved performance on Quebec French tasks with minimal regression on prestige French benchmarks, though gains are highly contingent on corpus composition, with the work highlighting how models defaulting to prestige variants can reinforce linguistic hierarchies by normalizing away regional features.

## Data Description

Introduces the first Quebecois French LLMs by adapting three base models (CroissantLLM, Llama-3.2-1B, Llama-3.1-8B) using continual pre-training with LoRA on a small 86M token corpus, evaluated on the COLE benchmark suite for both Quebec French and prestige French tasks.


## Detailed Summary

This paper explores the use of continual pre-training (CPT) to adapt LLMs to the Quebec French dialect under tight data and compute budgets. Using low-rank adaptation (LoRA) and gradient checkpointing as parameter-efficient fine-tuning strategies, the authors adapt three base models -- CroissantLLM, Llama-3.2-1B, and Llama-3.1-8B -- to Quebec French using a very small corpus of only 86 million tokens, which is significantly below typical CPT budgets. The adapted models are benchmarked on the COLE suite of French tasks, including both Quebec French and prestige French benchmarks.

The experiments demonstrate that CPT with parameter-efficient fine-tuning can narrow the dialect gap by improving performance on minority dialect benchmarks with minimal regression on prestige language benchmarks, updating less than 1% of model parameters. However, gains are highly contingent on corpus composition, suggesting that careful data curation is essential. The work highlights broader implications for linguistic equity: systems defaulting to prestige French can normalize away regional features and reinforce linguistic hierarchies, and training on dialectal data containing slang can potentially strengthen stereotypes linking dialectal features to class, region, or demographics. The authors release the first Quebec French LLMs on HuggingFace.

## Paper Outline

1. Introduction - Motivation for dialect adaptation and the dialect gap
2. Background and Related Work - Continual pre-training, parameter-efficient fine-tuning, dialect-specific LLMs
3. Data - Quebec French corpus composition and preprocessing
4. Methodology - CPT pipeline with LoRA and gradient checkpointing
5. Experimental Setup - Model configurations and evaluation benchmarks
6. Results and Discussion - Performance on COLE benchmark suite
7. Conclusion - Implications for linguistic equity

## Methods Summary

Three base models (CroissantLLM, Llama-3.2-1B, Llama-3.1-8B) are adapted using continual pre-training with LoRA, updating fewer than 1% of model parameters. Gradient checkpointing is employed to reduce memory requirements on modest hardware. The training corpus consists of 86 million tokens of Quebec French text. Models are evaluated on a subset of the COLE benchmark suite, which includes both Quebec French and prestige French tasks. The methodology is designed to be transferable to other dialects and low-resource language varieties, with complete training configurations, data-processing scripts, and evaluation pipelines released on GitHub.

## Results Summary

The adapted models show improved performance on Quebec French benchmarks with minimal regression on prestige French tasks. However, gains are highly contingent on corpus composition -- the specific mix of dialectal data significantly affects both dialect improvement and prestige language retention. Among the three base models, Llama-3.1-8B shows the strongest adaptation capability, while CroissantLLM benefits from its existing French-language focus. The results demonstrate that CPT with PEFT can provide cost-effective and sustainable language resource creation for minority linguistic communities, though the 86M token corpus represents a substantially smaller budget than most CPT studies in the literature.

## Conclusions

The work demonstrates that dialect adaptation is feasible with minimal compute and data resources, offering a practical path toward expanding high-quality LLM access to minority linguistic communities. Limitations include the very small corpus size (86M tokens), which may limit the depth of dialectal adaptation, and the risk that training on dialectal data containing stereotypical associations could reinforce linguistic biases. Future work includes expanding the training corpus, exploring more aggressive adaptation strategies, and investigating how dialectal training affects model biases and stereotypes.

## Artifact Contributions

- **Quebec French LLMs**: First open-weight LLMs adapted for Quebec French (https://huggingface.co/QuebecLLM)
- **Training Pipeline**: Complete training configurations, data-processing scripts, and evaluation pipelines (https://github.com/CLaC-Lab/QuebecLLM-CPT)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Directly addresses Quebecois French LLM evaluation. Shows training on Quebec slang can strengthen stereotypes linking dialectal features to class, region, or demographics.

## Tags

