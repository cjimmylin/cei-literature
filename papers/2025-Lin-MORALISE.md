---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KZMXWM9T
type: conferencePaper
short_title: MORALISE
year: 2025
first_author: "[[Xiao Lin]]"
last_author: "[[Hanghang Tong]]"
authors: "Xiao Lin; Zhining Liu; Ze Yang; Gaotang Li; Ruizhong Qiu; Shuke Wang; Hui Liu; Haotian Li; Sumit Keswani; Vishwa Pardeshi; Huijun Zhao; Wei Fan; Hanghang Tong"
doi: 10.48550/arXiv.2505.14728
url: "http://arxiv.org/abs/2505.14728"
external_pdf: "http://arxiv.org/pdf/2505.14728.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Created MORALISE, a benchmark for 'visual moral alignment' in VLMs, with 2.4k expert-verified image-text pairs grounded in Turiel's Domain Theory."
significance: "Addresses the 'multimodal moral gap', showing that VLMs struggle to identify moral violations that depend on the interplay between image and text (e.g., a 'safe' image with a harmful caption)."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Lin-MORALISE.md"
abstract: "Warning: This paper contains examples of harmful language and images. Reader discretion is advised. Recently, vision-language models have demonstrated in- creasing influence in morally sensitive domains such as autonomous driving and medical analysis, owing to their powerful multimodal reasoning capabilities. As these models are deployed in high-stakes real-world applications, it is of paramount importance to ensure that their outputs align with human moral values and remain within moral boundar"
paper_summary: "Abstract: Warning: This paper contains examples of harmful language and images. Reader discretion is advised. Recently, vision-language models have demonstrated in- creasing influence in morally sensitive domai | Overview: arXiv:2505.14728v1 [cs.CV] 20 May 2025 MORALISE: A Structured Benchmark for Moral Alignment in Visual Language Models Xiao Lin∗1, Zhining Liu∗1, Ze Yang∗1, Gaotang Li1, Ruizhong Qiu1, Shuke Wang1, Hui | Conclusions: model size alone does not guarantee moral reasoning ability. Smaller models that are carefully optimized or instruction-tuned for moral alignment can"
local_pdf: "[[PDFs/2025/2025-Lin-MORALISE.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, Gemma, Qwen, Phi, Llama"
DATA_URL: "https://huggingface.co/datasets/Ze1025/MORALISE"
---
# MORALISE: A Structured Benchmark for Moral Alignment in Visual Language Models

## Metadata

**Authors:** Lin, Xiao; Liu, Zhining; Yang, Ze; Li, Gaotang; Qiu, Ruizhong; Wang, Shuke; Liu, Hui; Li, Haotian; Keswani, Sumit; Pardeshi, Vishwa; Zhao, Huijun; Fan, Wei; Tong, Hanghang

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.14728](https://doi.org/10.48550/arXiv.2505.14728)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Lin-MORALISE.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.14728
- **DOI:** https://doi.org/10.48550/arXiv.2505.14728

## Abstract

Warning: This paper contains examples of harmful language and images. Reader discretion is advised. Recently, vision-language models have demonstrated increasing influence in morally sensitive domains such as autonomous driving and medical analysis, owing to their powerful multimodal reasoning capabilities. As these models are deployed in high-stakes real-world applications, it is of paramount importance to ensure that their outputs align with human moral values and remain within moral boundaries. However, existing work on moral alignment either focuses solely on textual modalities or relies heavily on AI-generated images, leading to distributional biases and reduced realism. To overcome these limitations, we introduce MORALISE, a comprehensive benchmark for evaluating the moral alignment of vision-language models (VLMs) using diverse, expert-verified real-world data. We begin by proposing a comprehensive taxonomy of 13 moral topics grounded in Turiel’s Domain Theory, spanning the personal, interpersonal, and societal moral domains encountered in everyday life. Built on this framework, we manually curate 2,481 high-quality image-text pairs, each annotated with two fine-grained labels: (1) topic annotation, identifying the violated moral topic(s), and (2) modality annotation, indicating whether the violation arises from the image or the text. For evaluation, we encompass two tasks, moral judgment and moral norm attribution, to assess models’ awareness of moral violations and their reasoning ability on morally salient content. Extensive experiments on 19 popular open- and closed-source VLMs show that MORALISE poses a significant challenge, revealing persistent moral limitations in current state-of-the-art models. The full benchmark is publicly available at https://huggingface.co/datasets/Ze1025/MORALISE.

## Authors

[[Xiao Lin]], [[Zhining Liu]], [[Ze Yang]], [[Gaotang Li]], [[Ruizhong Qiu]], [[Shuke Wang]], [[Hui Liu]], [[Haotian Li]], [[Sumit Keswani]], [[Vishwa Pardeshi]], [[Huijun Zhao]], [[Wei Fan]], [[Hanghang Tong]]

## Data Description

MORALISE is a structured benchmark for evaluating the moral alignment of vision-language models (VLMs), comprising 2,481 expert-verified real-world image-text pairs across 13 moral topics grounded in Turiel's Domain Theory. The dataset includes modality-centric annotations distinguishing text-based and image-based moral violations. It evaluates 19 open- and closed-source VLMs on two tasks: moral judgment and moral norm attribution, covering personal, interpersonal, and societal moral domains.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Computation-and-Language #Computer-Science---Computer-Vision-and-Pattern-Recognition #Computer-Science---Multimedia

## Citation Info

2 citations (Semantic Scholar/arXiv) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2505.14728 [cs]
