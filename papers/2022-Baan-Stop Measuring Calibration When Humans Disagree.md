---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: WLV875AC
type: conferencePaper
short_title: "Stop Measuring Calibration When Humans Disagree"
year: 2025
first_author: "[[Joris Baan]]"
last_author: "[[Raquel Fernández]]"
authors: "Joris Baan; Wilker Aziz; Barbara Plank; Raquel Fernández"
doi: 10.48550/arXiv.2210.16133
url: "http://arxiv.org/abs/2210.16133"
external_pdf: "http://arxiv.org/pdf/2210.16133.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2022/2022-Baan-Stop Measuring Calibration When Humans Disagree.md"
abstract: "Calibration is a popular framework to evalu- ate whether a classiﬁer knows when it does not know—i.e., its predictive probabilities are a good indication of how likely a prediction is to be correct. Correctness is commonly estimated against the human majority class. Recently, calibration to human majority has been measured on tasks where humans inher- ently disagree about which class applies. We show that measuring calibration to human ma- jority given inherent disagreements is theo- retically p"
paper_summary: "Abstract: Calibration is a popular framework to evalu- ate whether a classiﬁer knows when it does not know—i.e., its predictive probabilities are a good indication of how likely a prediction is to be correct. C | Overview: Stop Measuring Calibration When Humans Disagree Joris Baan1, Wilker Aziz1, Barbara Plank2,3,4, Raquel Fernández1 1University of Amsterdam, 2IT University of Copenhagen, 3MCML Munich, 4LMU Munich {j.s. | Methodology: We ﬁne-tune RoBERTa (Liu et al., 2019) on SNLI following the standard procedure de- scribed by Desai and Durrett (2020). We evalu- ate on the ChaosNLI | Key Findings: The OOD setting is interesting to evaluate uncer- tainty estimates, because it is especially important to have reliable uncertainty estimates for exam | Conclusions: We demonstrate a fundamental problem with mea- suring calibration to the human majority vote in settings with inherent disagreement in human la- bels."
local_pdf: "[[PDFs/2022/2022-Baan-Stop Measuring Calibration When Humans Disagree.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Machine Learning"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "RoBERTa"
DATA_URL: "https://github.com/jsbaan/calibration-on-disagreement-data"
---
# Stop Measuring Calibration When Humans Disagree

## Metadata

**Authors:** Baan, Joris; Aziz, Wilker; Plank, Barbara; Fernández, Raquel

**Year:** 2022

**Type:** preprint

**DOI:** [10.48550/arXiv.2210.16133](https://doi.org/10.48550/arXiv.2210.16133)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Baan-Stop Measuring Calibration When Humans Disagree.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2210.16133
- **DOI:** https://doi.org/10.48550/arXiv.2210.16133

## Abstract

Calibration is a popular framework to evaluate whether a classifier knows when it does not know - i.e., its predictive probabilities are a good indication of how likely a prediction is to be correct. Correctness is commonly estimated against the human majority class. Recently, calibration to human majority has been measured on tasks where humans inherently disagree about which class applies. We show that measuring calibration to human majority given inherent disagreements is theoretically problematic, demonstrate this empirically on the ChaosNLI dataset, and derive several instance-level measures of calibration that capture key statistical properties of human judgements - class frequency, ranking and entropy.

## Authors

[[Joris Baan]], [[Wilker Aziz]], [[Barbara Plank]], [[Raquel Fernández]]

## Data Description

The paper uses the ChaosNLI dataset, which contains approximately 4,645 natural language inference instances from SNLI and MNLI with 100 human annotations each, capturing inherent disagreement in human judgements. The authors fine-tune RoBERTa on these datasets to study calibration metrics and propose instance-level measures of calibration that capture key statistical properties of human judgement distributions including class frequency, ranking, and entropy.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

56 citations (Semantic Scholar/arXiv) [2025-08-27] 56 citations (Semantic Scholar/DOI) [2025-08-27] 56 citations (Semantic Scholar/DOI) [2025-08-23]
