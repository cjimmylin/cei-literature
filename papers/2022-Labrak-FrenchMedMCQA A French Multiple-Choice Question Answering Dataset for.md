---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0451
type: conferencePaper
short_title: "FrenchMedMCQA: A French Multiple-Choice Question Answering Dataset for Medical domain"
year: 2022
first_author: "[[Labrak, Yanis]]"
last_author: "[[Gourraud, Pierre-Antoine]]"
authors: "Labrak, Yanis; Bazoge, Adrien; Dufour, Richard; Rouvier, Mickael; Morin, Emmanuel; Daille, Béatrice; Gourraud, Pierre-Antoine"
authors_incomplete: false
url: "https://aclanthology.org/2022.louhi-1.5/"
external_pdf: "https://arxiv.org/pdf/2304.04280.pdf"
publication: "ACL Anthology"
CONF-CC: "N/A"
pdf_extract: "PDF Extracts/2022/2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for.md"
local_pdf: "[[PDFs/2022/2022-Labrak-FrenchMedMCQA A French Multiple-Choice Question Answering Dataset for.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: French
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "CamemBERT, BioBERT, PubMedBERT, XLM-RoBERTa, BARThez"
DATA_URL: "https://huggingface.co/datasets/qanastek/frenchmedmcqa"
tags: 
abstract: "This paper introduces FrenchMedMCQA, the ﬁrst publicly available Multiple-Choice Question Answering (MCQA) dataset in French for medical domain. It is composed of 3,105 questions taken from real exams of the French medical specialization diploma in pharmacy, mixing single and multiple answers. Each instance of the dataset contains an identiﬁer, a question, ﬁve possible answers and their manual correction(s)."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for question answering"
data_metrics: "3,105 questions"
CONFERENCE: "ACL 2022"
---
# FrenchMedMCQA: A French Multiple-Choice Question Answering Dataset for Medical domain

## Authors

[[Labrak, Yanis]], [[Bazoge, Adrien]], [[Dufour, Richard]], [[Rouvier, Mickael]], [[Morin, Emmanuel]], [[Daille, Béatrice]], [[Gourraud, Pierre-Antoine]]

## Metadata

**Authors:** Labrak, Yanis; Bazoge, Adrien; Dufour, Richard; Rouvier, Mickael; Morin, Emmanuel; Daille, Béatrice; Gourraud, Pierre-Antoine

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


## Detailed Summary

This paper introduces FrenchMedMCQA, the first publicly available Multiple-Choice Question Answering (MCQA) dataset in French for the medical domain, specifically the pharmacological field. The dataset contains 3,105 questions taken from real exams of the French medical specialization diploma in pharmacy, with both single-answer (1,080 questions) and multiple-answer (2,025 questions) formats. Each instance includes an identifier, a question, five candidate answers (labeled A-E), and the correct answer(s). The average question length is 14.17 tokens, with a vocabulary of 13,000 words including approximately 3,800 estimated medical domain-specific terms. The dataset is split into 70% train, 10% development, and 20% test sets.

The authors evaluate several state-of-the-art MCQA approaches, including French language models (CamemBERT), English medical domain models (BioBERT, PubMedBERT), multilingual models (XLM-RoBERTa), and the French generative model BARThez. A surprising and significant finding is that English specialized medical models (BioBERT, PubMedBERT) outperform generic French models (CamemBERT) despite the dataset being in French. This suggests that for technical domains like medicine, domain-specific knowledge encoded in model representations may be more valuable than language-specific pre-training, challenging the assumption that language-matched models are always superior. The dataset, models, and tools are all made publicly available.

## Paper Outline

1. Introduction - MCQA task definition and French medical NLP context
2. The FrenchMedMCQA Dataset - Collection, distribution, statistics
3. Experiments - Retriever-reader architecture, model evaluation
4. Results - Performance comparison across models
5. Conclusion and Future Work

## Methods Summary

The MCQA task is framed using a two-step retriever-reader architecture. The retriever identifies relevant passages from a knowledge base, and the reader selects answers from the retrieved context. Models evaluated include: French encoder models (CamemBERT in base and large variants), English medical domain models (BioBERT, PubMedBERT), multilingual models (XLM-RoBERTa), and the French sequence-to-sequence model BARThez. Questions and candidate answers are encoded as input pairs, with multiple answer selection handled through independent binary classification for each option. Evaluation metrics include exact match accuracy and F1 score, with separate analysis for single-answer and multiple-answer questions.

## Results Summary

English medical domain models (BioBERT, PubMedBERT) outperform generic French models (CamemBERT) on the French medical MCQA task, demonstrating that domain-specific representations may be more important than language-specific pre-training for technical domains. Multilingual XLM-RoBERTa shows competitive performance, benefiting from both broad language coverage and large-scale pre-training. Multiple-answer questions prove more challenging than single-answer questions due to the combinatorial complexity of selecting the correct subset of answers. The generative BARThez model shows promise but does not surpass discriminative approaches on this task. Overall accuracy remains well below human expert performance, highlighting the difficulty of medical question answering even for state-of-the-art models.

## Conclusions

The surprising dominance of English medical models over French generic models suggests that future French medical NLP research should invest in French-specific medical domain pre-training rather than relying on generic French language models. The multiple-answer format presents unique challenges that differ from standard single-answer MCQA and requires further methodological development. Future work includes expanding the dataset, developing French medical domain-specific language models, and exploring retrieval-augmented generation approaches.

## Artifact Contributions

- **FrenchMedMCQA Dataset**: 3,105 French medical MCQA questions from pharmacy exams (https://huggingface.co/datasets/qanastek/frenchmedmcqa)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** French medical domain evaluation benchmark. Relevant to medical ethics evaluation capability. Reveals English-model dominance over French-specific models.

## Tags

