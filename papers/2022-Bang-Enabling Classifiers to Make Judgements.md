---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: G38X86EQ
type: conferencePaper
short_title: "Enabling Classifiers to Make Judgements"
year: 2025
first_author: "[[Yejin Bang]]"
last_author: "[[Pascale Fung]]"
authors: "Yejin Bang; Tiezheng Yu; Andrea Madotto; Zhaojiang Lin; Mona Diab; Pascale Fung"
doi: 10.48550/arXiv.2210.07652
url: "http://arxiv.org/abs/2210.07652"
external_pdf: "http://arxiv.org/pdf/2210.07652.pdf"
publication: TRUSTNLP
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Proposed a framework for value-aligned classification that uses explicitly written human values in prompts to guide model predictions, rather than relying on implicit training data."
significance: "Demonstrates that explicitly instructing models with human values improves inclusivity and explainability in sensitive tasks like toxicity detection, surpassing baselines that rely solely on fine-tuning."
tags: 
pdf_extract: "PDF Extracts/2022/2022-Bang-Enabling Classifiers to Make Judgements.md"
abstract: "Many NLP classiﬁcation tasks, such as sexism/racism detection or toxicity detection, are based on human values. Yet, human values can vary under diverse cultural conditions. Therefore, we introduce a framework for valuealigned classiﬁcation that performs prediction based on explicitly written human values in the command. Along with the task, we propose a practical approach that distills value-aligned knowledge from large-scale language models (LLMs) to construct value-aligned classiﬁers in two..."
paper_summary: "Abstract: Many NLP classiﬁcation tasks, such as sex- ism/racism detection or toxicity detection, are based on human values. Yet, human values can vary under diverse cultural conditions. There- fore, we introduc | Overview: Enabling Classiﬁers to Make Judgements Explicitly Aligned with Human Values Yejin Bang1∗Tiezheng Yu1∗ Andrea Madotto2 Zhaojiang Lin2 Mona Diab2 Pascale Fung1† 1The Hong Kong University of Science and  | Methodology: avoids costly human labeling or crowd sourcing of values, allowing easier extensions to other value- aligned tasks in different domains. We further in | Key Findings: LLMs are powerful few-shot learners, yet they are not perfect. Thus, we conduct human evaluation on two categories' data (Inter- nalized sexism and Pa"
local_pdf: "[[PDFs/2022/2022-Bang-Enabling Classifiers to Make Judgements.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "OPT, ALBERT, RoBERTa, BART"
DATA_URL: "https://github.com/makcedward/nlpaug"
---
# Enabling Classifiers to Make Judgements Explicitly Aligned with Human Values

## Metadata

**Authors:** Bang, Yejin; Yu, Tiezheng; Madotto, Andrea; Lin, Zhaojiang; Diab, Mona; Fung, Pascale

**Year:** 2022

**Type:** preprint

**DOI:** [10.48550/arXiv.2210.07652](https://doi.org/10.48550/arXiv.2210.07652)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Bang-Enabling Classifiers to Make Judgements.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2210.07652
- **DOI:** https://doi.org/10.48550/arXiv.2210.07652

## Abstract

Many NLP classiﬁcation tasks, such as sexism/racism detection or toxicity detection, are based on human values. Yet, human values can vary under diverse cultural conditions. Therefore, we introduce a framework for valuealigned classiﬁcation that performs prediction based on explicitly written human values in the command. Along with the task, we propose a practical approach that distills value-aligned knowledge from large-scale language models (LLMs) to construct value-aligned classiﬁers in two steps. First, we generate value-aligned training data from LLMs by prompt-based few-shot learning. Next, we ﬁne-tune smaller classiﬁcation models with the generated data for the task. Empirical results show that our VA-MODELs surpass multiple baselines by at least 15.56% on the F1-score, including fewshot learning with OPT-175B and existing text augmentation methods. We suggest that using classiﬁers with explicit human value input improves both inclusivity & explainability in AI.

## Authors

[[Yejin Bang]], [[Tiezheng Yu]], [[Andrea Madotto]], [[Zhaojiang Lin]], [[Mona Diab]], [[Pascale Fung]]

## Data Description

The paper constructs a value-aligned sexism classification dataset using prompt-based data generation from OPT-175B. The training set contains 10,722 synthetic samples in triplet form (content, value, label) covering 19 sexism categories with 38 human values. The test set comprises 17,720 samples derived from existing multi-label sexism data, with value-aligned labels assigned based on explicit human values provided as instructions.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 14 citations (Semantic Scholar/DOI) [2025-08-27] 14 citations (Semantic Scholar/DOI) [2025-08-23]
