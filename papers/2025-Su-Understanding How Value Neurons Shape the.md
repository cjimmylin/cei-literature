---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AE9AXGP6
type: conferencePaper
short_title: "Understanding How Value Neurons Shape the"
year: 2025
first_author: "[[Yi Su]]"
last_author: "[[Di Wang]]"
authors: "Yi Su; Jiayi Zhang; Shu Yang; Xinhai Wang; Lijie Hu; Di Wang"
doi: 10.48550/arXiv.2505.17712
tags: 
url: "http://arxiv.org/abs/2505.17712"
external_pdf: "http://arxiv.org/pdf/2505.17712.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Introduced ValueLocate, a mechanistic interpretability framework, and ValueInsight, a dataset grounded in the Schwartz Values Survey, to localize value-critical neurons in LLMs."
significance: "Moves beyond behavioral alignment by establishing causal links between specific neurons and ethical orientations, providing a foundation for interpretable and targeted value interventions."
pdf_extract: "PDF Extracts/2025/2025-Su-Understanding How Value Neurons Shape the.md"
abstract: "Rapid integration of large language models (LLMs) into societal applications has intensified concerns about their alignment with universal ethical principles, as their internal value representations remain opaque despite behavioral alignment advancements. Current approaches struggle to systematically interpret how values are encoded in neural architectures, limited by datasets that prioritize superficial judgments over mechanistic analysis."
paper_summary: "Abstract: Rapid integration of large language models (LLMs) into societal applications has intensi- fied concerns about their alignment with univer- sal ethical principles, as their internal value rep- resentat | Overview: arXiv:2505.17712v1 [cs.CL] 23 May 2025 Understanding How Value Neurons Shape the Generation of Specified Values in LLMs Yi Su*,1,2, Jiayi Zhang*,1,3, Shu Yang†,1,2, Xinhai Wang1,2, Lijie Hu†,1,2, Di W | Methodology: cannot be applied to value-related neurons as deac- tivation will be meaningless. To address this issue, we propose a method that aims to manipulate a | Key Findings: value-related neurons. The details of the baselines are presented in Appendix D. • LPIP: Locating neurons using Log Probabil- ity and Inner Products ("
local_pdf: "[[PDFs/2025/2025-Su-Understanding How Value Neurons Shape the.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Llama-3, Qwen, Gemma"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
---
# Understanding How Value Neurons Shape the Generation of Specified Values in LLMs

## Metadata

**Authors:** Su, Yi; Zhang, Jiayi; Yang, Shu; Wang, Xinhai; Hu, Lijie; Wang, Di

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.17712](https://doi.org/10.48550/arXiv.2505.17712)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Su-Understanding How Value Neurons Shape the.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.17712
- **DOI:** https://doi.org/10.48550/arXiv.2505.17712

## Abstract

Rapid integration of large language models (LLMs) into societal applications has intensified concerns about their alignment with universal ethical principles, as their internal value representations remain opaque despite behavioral alignment advancements. Current approaches struggle to systematically interpret how values are encoded in neural architectures, limited by datasets that prioritize superficial judgments over mechanistic analysis. We introduce ValueLocate, a mechanistic interpretability framework grounded in the Schwartz Values Survey, to address this gap. Our method first constructs ValueInsight, a dataset that operationalizes four dimensions of universal value through behavioral contexts in the real world. Leveraging this dataset, we develop a neuron identification method that calculates activation differences between opposing value aspects, enabling precise localization of value-critical neurons without relying on computationally intensive attribution methods. Our proposed validation method demonstrates that targeted manipulation of these neurons effectively alters model value orientations, establishing causal relationships between neurons and value representations. This work advances the foundation for value alignment by bridging psychological value frameworks with neuron analysis in LLMs.

## Authors

[[Yi Su]], [[Jiayi Zhang]], [[Shu Yang]], [[Xinhai Wang]], [[Lijie Hu]], [[Di Wang]]

## Data Description

The paper introduces ValueInsight, a dataset comprising 640 second-person value descriptions and 15,000 scenario-based open-ended questions grounded in the Schwartz Values Survey across four value dimensions (Openness to Change, Self-Transcendence, Conservation, Self-Enhancement). The dataset was constructed using GPT-4o and is used alongside PVQ40 and ValueBench for neuron identification and value manipulation experiments on LLama-3.1-8B, LLama-3.2-1B, Qwen2-0.5B, and Gemma-2-9B.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

3 citations (Semantic Scholar/arXiv) [2025-08-27] 40 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23]
