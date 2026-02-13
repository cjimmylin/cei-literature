---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: B8YB9NHK
type: conferencePaper
short_title: CValues
year: 2025
first_author: "[[Guohai Xu]]"
last_author: "[[Jingren Zhou]]"
authors: "Guohai Xu; Jiayi Liu; Ming Yan; Haotian Xu; Jinghui Si; Zhuoran Zhou; Peng Yi; Xing Gao; Jitao Sang; Rong Zhang; Ji Zhang; Chao Peng; Fei Huang; Jingren Zhou"
doi: 10.48550/arXiv.2307.09705
tags: 
url: "http://arxiv.org/abs/2307.09705"
external_pdf: "http://arxiv.org/pdf/2307.09705.pdf"
publication: arXiv.org
national_ethnic_cultural: Chinese
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Presents CVALUES, the first specialized benchmark for Chinese human values alignment, evaluating LLMs on both safety and responsibility criteria across 10 scenarios."
significance: "Demonstrates that while Chinese models often pass safety audits, they still have significant gaps in 'responsibility' (helpfulness and cultural value adherence), emphasizing localized value alignment."
pdf_extract: "PDF Extracts/2023/2023-Xu-CValues.md"
abstract: "Warning: this paper contains examples that may be offensive or upsetting. With the rapid evolution of large language mod- els (LLMs), there is a growing concern that they may pose risks or have negative social im- pacts. Therefore, evaluation of human values alignment is becoming increasingly important. Previous work mainly focuses on assessing the performance of LLMs on certain knowledge and reasoning abilities, while neglecting the alignment to human values, especially in a Chi- nese context."
paper_summary: "Abstract: Warning: this paper contains examples that may be offensive or upsetting. With the rapid evolution of large language mod- els (LLMs), there is a growing concern that they may pose risks or have negati | Overview: CVALUES: Measuring the Values of Chinese Large Language Models from Safety to Responsibility Guohai Xu1, Jiayi Liu1, Ming Yan1∗, Haotian Xu1, Jinghui Si1, Zhuoran Zhou1 Peng Yi1, Xing Gao1, Jitao Sang | Methodology: is to develop a model that can directly predict the safety or responsibility of each response. For ex- ample, Sun et al. (2023) do prompt engineering  | Key Findings: benchmark to measure the alignment ability of LLMs in terms of both safety and responsi- bility criteria. As a result, we have manually collected adve | Conclusions: This paper evaluates the values performance of Chinese large language models based on human evaluation and automatic evaluation. We present three impo"
local_pdf: "[[PDFs/2023/2023-Xu-CValues.pdf]]"
ethics_overall: Yes
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "10 scenarios"
LLM_assessed: "ChatGPT, Alpaca, Vicuna"
DATA_URL: "https://github.com/X-PLUG/CValues"
DATE_ADDED: 20260207
---
# CValues: Measuring the Values of Chinese Large Language Models from Safety to Responsibility

## Metadata

**Authors:** Xu, Guohai; Liu, Jiayi; Yan, Ming; Xu, Haotian; Si, Jinghui; Zhou, Zhuoran; Yi, Peng; Gao, Xing; Sang, Jitao; Zhang, Rong; Zhang, Ji; Peng, Chao; Huang, Fei; Zhou, Jingren

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2307.09705](https://doi.org/10.48550/arXiv.2307.09705)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Xu-CValues.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2307.09705
- **DOI:** https://doi.org/10.48550/arXiv.2307.09705

## Abstract

Warning: this paper contains examples that may be offensive or upsetting. With the rapid evolution of large language models (LLMs), there is a growing concern that they may pose risks or have negative social impacts. Therefore, evaluation of human values alignment is becoming increasingly important. Previous work mainly focuses on assessing the performance of LLMs on certain knowledge and reasoning abilities, while neglecting the alignment to human values, especially in a Chinese context. In this paper, we present CVALUES , the first Chinese human values evaluation benchmark to measure the alignment ability of LLMs in terms of both safety and responsibility criteria. As a result, we have manually collected adversarial safety prompts across 10 scenarios and induced responsibility prompts from 8 domains by professional experts. To provide a comprehensive values evaluation of Chinese LLMs, we not only conduct human evaluation for reliable comparison, but also construct multi-choice prompts for automatic evaluation. Our findings suggest that while most Chinese LLMs perform well in terms of safety, there is considerable room for improvement in terms of responsibility. Moreover, both the automatic and human evaluation are important for assessing the human values alignment in different aspects. The benchmark and code is available on ModelScope 1 and Github 2.

## Authors

[[Guohai Xu]], [[Jiayi Liu]], [[Ming Yan]], [[Haotian Xu]], [[Jinghui Si]], [[Zhuoran Zhou]], [[Peng Yi]], [[Xing Gao]], [[Jitao Sang]], [[Rong Zhang]], [[Ji Zhang]], [[Chao Peng]], [[Fei Huang]], [[Jingren Zhou]]

## Data Description

CVALUES is the first Chinese human values evaluation benchmark measuring LLM alignment across safety and responsibility criteria. It contains 2,100 adversarial safety prompts across 10 scenarios and 800 induced responsibility prompts from 8 domains, plus 4,312 multi-choice prompts for automatic evaluation. The benchmark also includes CVALUES-COMPARISON, a 145k prompt dataset with paired positive and negative responses for training. Ten Chinese LLMs were evaluated including ChatGPT, ChatGLM-6B, BELLE-7B, ChatPLUG, MOSS, Chinese-Alpaca-Plus, and Ziya-LLaMA-13B.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

84 citations (Semantic Scholar/DOI) [2025-08-27] 84 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2307.09705 [cs]
