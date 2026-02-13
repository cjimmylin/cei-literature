---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XR5FVHMC
type: conferencePaper
short_title: FairJob
year: 2025
first_author: "[[Mariia Vladimirova]]"
last_author: "[[Eustache Diemert]]"
authors: "Mariia Vladimirova; Federico Pavone; Eustache Diemert"
doi: 10.48550/arXiv.2407.03059
url: "http://arxiv.org/abs/2407.03059"
external_pdf: "http://arxiv.org/pdf/2407.03059.pdf"
publication: "Neural Information Processing Systems"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: "Value Pluralism / Schwartz, Utilitarianism"
key_contribution: "Releases FairJob, a real-world fairness dataset for job recommendation, including proxy estimates for sensitive attributes like gender"
significance: "Addresses the scarcity of industrial fairness benchmarks, allowing researchers to study the 'fairness-utility trade-off' in high-stakes employment algorithms"
tags: 
pdf_extract: "PDF Extracts/2024/2024-Vladimirova-FairJob.md"
abstract: "We introduce a fairness-aware dataset for job recommendation in advertising, designed to foster research in algorithmic fairness within real-world scenarios. It was collected and prepared to comply with privacy standards and business confidentiality. An additional challenge is the lack of access to protected user attributes such as gender, for which we propose a solution to obtain a proxy estimate. Despite being anonymized and including a proxy for a sensitive attribute, our dataset preserves pr"
paper_summary: "Abstract: We introduce a fairness-aware dataset for job recommendation in advertising, designed to foster research in algorithmic fairness within real-world scenarios. It was collected and prepared to comply wi | Overview: FairJob: A Real-World Dataset for Fairness in Online Systems Mariia Vladimirova∗, Eustache Diemert Criteo AI Lab {m.vladimirova,e.diemert}@criteo.com Federico Pavone Université Paris Dauphine-PSL fede | Methodology: to compute a fair utility metric for the job recommendations in online systems case from a biased dataset. Experimental evaluations of bias mitigation | Conclusions: Addressing bias in AI goes beyond mere compliance with legal frameworks like the AI Act; it necessitates proactive measures to detect, prevent, and mi"
local_pdf: [[PDFs/2024/2024-Vladimirova-FairJob.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://huggingface.co/datasets/criteo/FairJob"
---
# FairJob: A Real-World Dataset for Fairness in Online Systems

## Metadata

**Authors:** Vladimirova, Mariia; Pavone, Federico; Diemert, Eustache

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2407.03059](https://doi.org/10.48550/arXiv.2407.03059)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Vladimirova-FairJob.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2407.03059
- **DOI:** https://doi.org/10.48550/arXiv.2407.03059

## Abstract

We introduce a fairness-aware dataset for job recommendation in advertising, designed to foster research in algorithmic fairness within real-world scenarios. It was collected and prepared to comply with privacy standards and business confidentiality. An additional challenge is the lack of access to protected user attributes such as gender, for which we propose a solution to obtain a proxy estimate. Despite being anonymized and including a proxy for a sensitive attribute, our dataset preserves predictive power and maintains a realistic and challenging benchmark. This dataset addresses a significant gap in the availability of fairnessfocused resources for high-impact domains like advertising – the actual impact being having access or not to precious employment opportunities, where balancing fairness and utility is a common industrial challenge. We also explore various stages in the advertising process where unfairness can occur and introduce a method to compute a fair utility metric for the job recommendations in online systems case from a biased dataset. Experimental evaluations of bias mitigation techniques on the released dataset demonstrate potential improvements in fairness and the associated trade-offs with utility.

## Authors

[[Mariia Vladimirova]], [[Federico Pavone]], [[Eustache Diemert]]

## Data Description

FairJob is a large-scale fairness-aware dataset for job recommendation in advertising, containing 1,072,226 rows collected during 5 months of a targeted job campaign. Each row represents a job ad with user features (20 categorical and 39 numerical features), a binary click label, a binary gender proxy for the protected attribute, and a senior position indicator. The dataset is designed to study algorithmic fairness in real-world online advertising systems where access to protected attributes is limited.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Statistics---Machine-Learning

## Citation Info

4 citations (Semantic Scholar/DOI) [2025-08-27] arXiv:2407.03059 [cs]
