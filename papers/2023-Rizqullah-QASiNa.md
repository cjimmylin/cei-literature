---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6MRBJ9IP
type: conferencePaper
short_title: QASiNa
year: 2025
first_author: "[[Muhammad Razif Rizqullah]]"
last_author: "[[Alham Fikri Aji]]"
authors: "Muhammad Razif Rizqullah; Ayu Purwarianti; Alham Fikri Aji"
doi: 10.48550/arXiv.2310.08102
tags: 
url: "http://arxiv.org/abs/2310.08102"
external_pdf: "http://arxiv.org/pdf/2310.08102.pdf"
publication: "2023 10th International Conference on Advanced Informatics: Concept, Theory and Application (ICAICTA)"
national_ethnic_cultural: Indonesian
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: N/A
newtags: "Indonesian, Islam"
pdf_extract: "PDF Extracts/2023/2023-Rizqullah-QASiNa.md"
paper_summary: "Overview: QASiNa: Religious Domain Question Answering using Sirah Nabawiyah Muhammad Razif Rizqullah1, Ayu Purwarianti1, Alham Fikri Aji2 1School of Electrical Engineering and Informatics Bandung Institute of T | Methodology: revolves around obtaining answers using predefined patterns. Extractive method has been conducted in several studies [21] [13]. The extractive method  | Key Findings: We evaluate the dataset using the transfer learning approach with mBERT, XLM-R, and IndoBERT with also test the Chat GPT-3.5 and GPT-4. The evaluation | Conclusions: drawn from this evaluation was that the EM and F1-scores of Chat GPT are lower compared to XLM-R, on the other side Chat GPT has high Substring Match"
local_pdf: [[PDFs/2023/2023-Rizqullah-QASiNa.pdf]]
abstract: "Nowadays, Question Answering (QA) tasks receive significant research focus, particularly with the development of Large Language Model (LLM) such as Chat GPT [1]. LLM can be applied to various domains, but it contradicts the principles of information transmission when applied to the Islamic domain. In Islam we strictly regulates the sources of information and who can give interpretations or tafseer for that sources [2]. The approach used by LLM to generate answers based on its own interpretation"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Question Answering"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, BERT"
DATA_URL: "https://github.com/rizquuula/QASiNa"
---
# QASiNa: Religious Domain Question Answering using Sirah Nabawiyah

## Metadata

**Authors:** Rizqullah, Muhammad Razif; Purwarianti, Ayu; Aji, Alham Fikri

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.08102](https://doi.org/10.48550/arXiv.2310.08102)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Rizqullah-QASiNa.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2310.08102
- **DOI:** https://doi.org/10.48550/arXiv.2310.08102

## Abstract

Nowadays, Question Answering (QA) tasks receive significant research focus, particularly with the development of Large Language Model (LLM) such as Chat GPT [1]. LLM can be applied to various domains, but it contradicts the principles of information transmission when applied to the Islamic domain. In Islam we strictly regulates the sources of information and who can give interpretations or tafseer for that sources [2]. The approach used by LLM to generate answers based on its own interpretation is similar to the concept of tafseer, LLM is neither an Islamic expert nor a human which is not permitted in Islam. Indonesia is the country with the largest Islamic believer population in the world [3]. With the high influence of LLM, we need to make evaluation of LLM in religious domain. Currently, there is only few religious QA dataset available and none of them using Sirah Nabawiyah especially in Indonesian Language. In this paper, we propose the Question Answering Sirah Nabawiyah (QASiNa) dataset, a novel dataset compiled from Sirah Nabawiyah literatures in Indonesian language. We demonstrate our dataset by using mBERT [4], XLM-R [5], and IndoBERT [6] which fine-tuned with Indonesian translation of SQuAD v2.0 [7]. XLM-R model returned the best performance on QASiNa with EM of 61.20, F1-Score of 75.94, and Substring Match of 70.00. We compare XLM-R performance with Chat GPT-3.5 and GPT-4 [1]. Both Chat GPT version returned lower EM and F1-Score with higher Substring Match, the gap of EM and Substring Match get wider in GPT-4. The experiment indicate that Chat GPT tends to give excessive interpretations as evidenced by its higher Substring Match scores compared to EM and F1-Score, even after providing instruction and context. This concludes Chat GPT is unsuitable for question answering task in religious domain especially for Islamic religion.

## Authors

[[Muhammad Razif Rizqullah]], [[Ayu Purwarianti]], [[Alham Fikri Aji]]

## Data Description

The paper introduces QASiNa (Question Answering Sirah Nabawiyah), a novel dataset of 500 question-answer pairs from 66 contexts about Islamic prophetic biography in Indonesian language. The dataset was compiled from 9 Sirah Nabawiyah literature sources and validated by domain experts. Models evaluated include mBERT, XLM-R, IndoBERT (fine-tuned with SQuAD-ID), and ChatGPT (GPT-3.5-turbo and GPT-4).


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

18 citations (Semantic Scholar/arXiv) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-27] 17 citations (Semantic Scholar/arXiv) [2025-08-23]
