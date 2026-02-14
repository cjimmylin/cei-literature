---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CQCXZGWI
type: document
short_title: "SemEval-2023 Task 10"
year: 2025
first_author: "[[Hannah Kirk]]"
last_author: "[[Röttger, Paul]]"
authors: "[[Kirk, Hannah]]; [[Yin, Wenjie]]; [[Vidgen, Bertie]]; [[Röttger, Paul]]"
url: "https://aclanthology.org/2023.semeval-1.305/"
external_pdf: "http://arxiv.org/pdf/2303.04222"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2023/2023-Kirk-SemEval-2023 Task 10.md"
local_pdf: "[[PDFs/2023/2023-Kirk-SemEval-2023 Task 10.pdf]]"
abstract: "Online sexism is a widespread and harmful phenomenon. Automated tools can assist the detection of sexism at scale. Binary detection, however, disregards the diversity of sexist con- tent, and fails to provide clear explanations for why something is sexist. To address this issue, we introduce SemEval Task 10 on the Explain- able Detection of Online Sexism (EDOS). We make three main contributions: i) a novel hi- erarchical taxonomy of sexist content, which includes granular vectors of sexism to ai"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Interpretability & Explainability"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
LLM_assessed: "DeBERTa, RoBERTa"
DATA_URL: "https://github.com/rewire-online/edos"
---
# SemEval-2023 Task 10: Explainable Detection of Online Sexism (EDOS)

## Authors

[[Hannah Kirk|Kirk, Hannah]], [[Wenjie Yin|Yin, Wenjie]], [[Bertie Vidgen|Vidgen, Bertie]], [[Paul Röttger|Röttger, Paul]]

## Links

- **Local PDF:** [[PDFs/2023/2023-Kirk-SemEval-2023 Task 10.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2023.semeval-1.305/

## Abstract

Online sexism is a widespread and harmful phenomenon. Automated tools can assist the detection of sexism at scale. Binary detection, however, disregards the diversity of sexist content, and fails to provide clear explanations for why something is sexist. To address this issue, we introduce SemEval Task 10 on the Explainable Detection of Online Sexism (EDOS). We make three main contributions: i) a novel hierarchical taxonomy of sexist content, which includes granular vectors of sexism to aid explainability; ii) a new dataset of 20,000 social media comments with fine-grained labels, along with larger unlabelled datasets for model adaptation; and iii) baseline models as well as an analysis of the methods, results and errors for participant submissions to our task.

## Data Description

The EDOS dataset consists of 20,000 social media comments from Reddit and Gab with fine-grained hierarchical labels for sexist content detection across three tasks: binary sexism detection (Task A), four-category classification (Task B), and 11 fine-grained sexism vectors (Task C). An additional 2 million unlabelled entries were provided for model adaptation. All entries were annotated by trained annotators who self-identify as women, with expert adjudication for disagreements.


## Notes

