---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0451
type: conferencePaper
short_title: "FrenchMedMCQA: A French Multiple-Choice Question Answering Dataset for Medical domain"
year: 2022
first_author: "[[Yanis Labrak]]"
last_author: "[[Yanis Labrak]]"
authors: Yanis Labrak, et al.
url: "https://aclanthology.org/2022.louhi-1.5/"
external_pdf: "https://arxiv.org/pdf/2304.04280.pdf"
publication: ACL Anthology
local_pdf: "[[PDFs/2022/2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for.pdf]]"
pdf_extract: "PDF Extracts/2022/2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: "French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus for question answering"
data_metrics: "3,105 questions"
LLM_assessed: "CamemBERT, BioBERT, PubMedBERT, XLM-RoBERTa, BARThez"
DATA_URL: "https://huggingface.co/datasets/qanastek/frenchmedmcqa"
tags: 
abstract: "This paper introduces FrenchMedMCQA, the ﬁrst publicly available Multiple-Choice Question Answering (MCQA) dataset in French for medical domain. It is composed of 3,105 questions taken from real exams of the French medical specialization diploma in pharmacy, mixing single and multiple answers. Each instance of the dataset contains an identiﬁer, a question, ﬁve possible answers and their manual correction(s)."
research_topic: "Machine Learning"
---
# FrenchMedMCQA: A French Multiple-Choice Question Answering Dataset for Medical domain

## Authors

[[Yanis Labrak, et al.]]

## Metadata

**Authors:** Yanis Labrak, et al.

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** French

**Benchmark:** FrenchMedMCQA

## Links

- **arXiv:** https://arxiv.org/abs/2304.04280
- **URL:** https://aclanthology.org/2022.louhi-1.5/
- **Code/Data:** https://huggingface.co/datasets/qanastek/frenchmedmcqa

## Abstract

First publicly available MCQA dataset in French for medical domain. Contains 3,105 questions from real French medical specialization exams (pharmacy). Finds English specialized models yield better results than generic French ones despite the dataset being in French. Available on HuggingFace.

## Summary

This paper introduces FrenchMedMCQA, the first publicly available multiple-choice question answering dataset in French for the medical domain, containing 3,105 questions from real French pharmacy specialization exams with both single and multiple answer formats. Using a two-step retriever-reader architecture, the authors evaluate French models (CamemBERT) and English medical models (BioBERT, PubMedBERT) along with multilingual XLM-RoBERTa and generative BARThez. Surprisingly, they find that English specialized medical models outperform generic French models despite the dataset being in French, highlighting the importance of domain-specific representations over language-specific ones for technical medical content.

## Data Description

FrenchMedMCQA dataset of 3,105 French medical multiple-choice questions from pharmacy exams. Evaluates French (CamemBERT) and English medical models (BioBERT, PubMedBERT) plus multilingual XLM-RoBERTa and generative BARThez, finding English specialized models outperform French generic ones despite French dataset.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** French medical domain evaluation benchmark. Relevant to medical ethics evaluation capability. Reveals English-model dominance over French-specific models.

## Tags

