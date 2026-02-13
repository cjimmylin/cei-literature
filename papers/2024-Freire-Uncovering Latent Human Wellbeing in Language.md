---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7ISQ383Q
type: conferencePaper
short_title: "Uncovering Latent Human Wellbeing in Language"
year: 2025
first_author: "[[Pedro Freire]]"
last_author: "[[Scott Emmons]]"
authors: "Pedro Freire; ChengCheng Tan; Adam Gleave; Dan Hendrycks; Scott Emmons"
doi: 10.48550/arXiv.2402.11777
url: "http://arxiv.org/abs/2402.11777"
external_pdf: "http://arxiv.org/pdf/2402.11777.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: Utilitarianism
key_contribution: "Explores if LLMs implicitly learn human wellbeing concepts, finding that PCA on embeddings (without fine-tuning) predicts ETHICS Utilitarianism tasks with high accuracy"
significance: "Suggests that pretraining alone conveys significant moral understanding (wellbeing), providing a latent foundation that can be steered for utilitarian alignment"
tags: 
pdf_extract: "PDF Extracts/2024/2024-Freire-Uncovering Latent Human Wellbeing in Language.md"
abstract: "Do language models implicitly learn a concept of human wellbeing? We ex- plore this through the ETHICS Utilitarianism task, assessing if scaling enhances pretrained models’ representations. Our initial finding reveals that, without any prompt engineering or finetuning, the leading principal component from OpenAI’s text-embedding-ada-002 achieves 73.9% accuracy. This closely matches the 74.6% of BERT-large finetuned on the entire ETHICS dataset, suggesting pretraining conveys some understanding a"
paper_summary: "Abstract: Do language models implicitly learn a concept of human wellbeing? We ex- plore this through the ETHICS Utilitarianism task, assessing if scaling enhances pretrained models’ representations. Our initia | Overview: UNCOVERING LATENT HUMAN WELLBEING IN LANGUAGE MODEL EMBEDDINGS Pedro Freire∗ Independent ChengCheng Tan FAR AI Adam Gleave FAR AI Dan Hendrycks Center for AI Safety Scott Emmons FAR AI, UC Berkeley AB | Methodology: Our PCA Representation experiments are conducted in the following steps: | Conclusions: that paired mode improves performance over single mode. 6 CONCLUSION AND FUTURE DIRECTIONS Our research explores the encoding of human wellbeing withi"
local_pdf: "[[PDFs/2024/2024-Freire-Uncovering Latent Human Wellbeing in Language.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-3, DeBERTa, BERT"
DATA_URL: "NA"
---
# Uncovering Latent Human Wellbeing in Language Model Embeddings

## Metadata

**Authors:** Freire, Pedro; Tan, ChengCheng; Gleave, Adam; Hendrycks, Dan; Emmons, Scott

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2402.11777](https://doi.org/10.48550/arXiv.2402.11777)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Freire-Uncovering Latent Human Wellbeing in Language.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2402.11777
- **DOI:** https://doi.org/10.48550/arXiv.2402.11777

## Abstract

Do language models implicitly learn a concept of human wellbeing? We explore this through the ETHICS Utilitarianism task, assessing if scaling enhances pretrained models’ representations. Our initial finding reveals that, without any prompt engineering or finetuning, the leading principal component from OpenAI’s text-embedding-ada-002 achieves 73.9% accuracy. This closely matches the 74.6% of BERT-large finetuned on the entire ETHICS dataset, suggesting pretraining conveys some understanding about human wellbeing. Next, we consider four language model families, observing how Utilitarianism accuracy varies with increased parameters. We find performance is nondecreasing with increased model size when using sufficient numbers of principal components.

## Authors

[[Pedro Freire]], [[ChengCheng Tan]], [[Adam Gleave]], [[Dan Hendrycks]], [[Scott Emmons]]

## Data Description

The study uses the ETHICS Utilitarianism subset (approximately 23,000 pairs of scenarios about pleasure and pain) to investigate whether LLM embeddings implicitly encode concepts of human wellbeing. Four language model families were evaluated: GPT-3 (including text-embedding-ada-002), DeBERTa, Cohere, and SentenceTransformers, with PCA-based dimensionality reduction and logistic regression applied to embedding spaces. The key finding is that the leading principal component of text-embedding-ada-002 achieves 73.9% accuracy, comparable to BERT-large fine-tuned on the entire dataset.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

1 citations (Semantic Scholar/DOI) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-23]
