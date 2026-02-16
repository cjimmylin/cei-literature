---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6YXS5H9B
type: conferencePaper
short_title: DefAn
year: 2025
first_author: "[[A B M Ashikur Rahman]]"
last_author: "[[Ajmal Mian]]"
authors: "A B M Ashikur Rahman; Saeed Anwar; Muhammad Usman; Ajmal Mian"
doi: 10.48550/arXiv.2406.09155
url: "http://arxiv.org/abs/2406.09155"
external_pdf: "http://arxiv.org/pdf/2406.09155.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2024/2024-Rahman-DefAn.md"
abstract: "Large Language Models (LLMs) have demonstrated remarkable capabilities, revolutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims that contradict established facts, deviating from prompts, and producing inconsistent responses when the same prompt is presented multiple times. Addressing these issues is challenging due to the lack of comprehensive and easily assessable benchmark datasets."
paper_summary: "Abstract: Large Language Models (LLMs) have demonstrated remarkable capabilities, revo- lutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims | Overview: DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation A B M Ashikur Rahman∗ ICS Department KFUPM Dhahran, KSA - 31261 g202204800@kfupm.edu.sa Saeed Anwar ICS Department, KFUPM JRCAI, SDAI | Key Findings: A B M Ashikur Rahman∗ ICS Department KFUPM Dhahran, KSA - 31261 g202204800@kfupm.edu.sa Saeed Anwar ICS Department, KFUPM JRCAI, SDAIA-KFUPM Dhahran,  | Conclusions: This paper introduces a comprehensive benchmark dataset designed for evaluating hallucinations in LLMs. To facilitate accurate assessment and evaluati"
local_pdf: [[PDFs/2024/2024-Rahman-DefAn.pdf]]
DATE_ADDED: 20260208
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for hallucination detection dataset"
data_metrics: "75,000 prompts"
LLM_assessed: "GPT-3.5, Llama-2, Llama-3, Gemini, Mixtral"
DATA_URL: "https://github.com/ashikiut/DefAn"
---
# DefAn: Definitive Answer Dataset for LLMs Hallucination Evaluation

## Metadata

**Authors:** Rahman, A. B. M. Ashikur; Anwar, Saeed; Usman, Muhammad; Mian, Ajmal

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2406.09155](https://doi.org/10.48550/arXiv.2406.09155)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Rahman-DefAn.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2406.09155
- **DOI:** https://doi.org/10.48550/arXiv.2406.09155

## Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities, revolutionizing the integration of AI in daily life applications. However, they are prone to hallucinations, generating claims that contradict established facts, deviating from prompts, and producing inconsistent responses when the same prompt is presented multiple times. Addressing these issues is challenging due to the lack of comprehensive and easily assessable benchmark datasets. Most existing datasets are small and rely on multiple-choice questions, which are inadequate for evaluating the generative prowess of LLMs. To measure hallucination in LLMs, this paper introduces a comprehensive benchmark dataset comprising over 75,000 prompts across eight domains. These prompts are designed to elicit definitive, concise, and informative answers. The dataset is divided into two segments: one publicly available for testing and assessing LLM performance and a hidden segment for benchmarking various LLMs. In our experiments, we tested six LLMs—GPT-3.5, LLama 2, LLama 3, Gemini, Mixtral, and Zephyr—revealing that overall factual hallucination ranges from 59% to 82% on the public dataset and 57% to 76% in the hidden benchmark. Prompt misalignment hallucination ranges from 6% to 95% in the public dataset and 17% to 94% in the hidden counterpart. Average consistency ranges from 21% to 61% and 22% to 63%, respectively. Domain-wise analysis shows that LLM performance significantly deteriorates when asked for specific numeric information while performing moderately with person, location, and date queries. Our dataset demonstrates its efficacy and serves as a comprehensive benchmark for LLM performance evaluation. Our dataset and LLMs responses are available at https://github.com/ashikiut/DefAn.

## Authors

[[A B M Ashikur Rahman]], [[Saeed Anwar]], [[Muhammad Usman]], [[Ajmal Mian]]

## Data Description

DefAn is a comprehensive benchmark dataset comprising over 75,000 prompts across eight knowledge domains (Sports, Census Australia, Nobel Prize, Entertainment, World Organizations, QS Ranking, Conference Venue, and Math). The dataset is split into a public segment (68,093 samples) and a hidden segment (7,485 samples), with each question paraphrased 15 times to assess consistency. It evaluates LLM hallucination across three dimensions: factual accuracy, prompt faithfulness, and response consistency.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Computer-Vision-and-Pattern-Recognition

## Citation Info

11 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-23]
