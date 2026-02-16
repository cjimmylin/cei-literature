---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JU8JYC2E
type: document
short_title: FairLex
year: 2025
first_author: "[[Ilias Chalkidis]]"
last_author: "[[Søgaard, Anders]]"
authors: "[[Chalkidis, Ilias]]; [[Pasini, Tommaso]]; [[Zhang, Sheng]]; [[Tomada, Letizia]]; [[Schwemer, Sebastian Felix]]; [[Søgaard, Anders]]"
url: "https://aclanthology.org/2022.acl-long.301/"
external_pdf: "http://arxiv.org/pdf/2203.07228"
national_ethnic_cultural: "Chinese, French, German, Italian"
cultures_nationalities_list: "Chinese, French, German, Italian"
languages_list: "Chinese, English, French, German, Italian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, French, German, Italian, Bias & Fairness"
key_contribution: "Created FairLex, a multilingual benchmark (EN, DE, FR, IT, ZH) for fairness in legal text processing, covering 4 jurisdictions."
significance: "Shows that 'legal fairness' is jurisdictional – what counts as bias in Swiss law differs from US law, and models trained on one don't transfer to the other."
tags: 
pdf_extract: "PDF Extracts/2022/2022-Chalkidis-FairLex.md"
local_pdf: "[[PDFs/2022/2022-Chalkidis-FairLex.pdf]]"
abstract: "We present a benchmark suite of four datasets for evaluating the fairness of pre-trained language models and the techniques used to ﬁne-tune them for downstream tasks. Our benchmarks cover four jurisdictions (European Council, USA, Switzerland, and China), ﬁve languages (English, German, French, Italian and Chinese) and fairness across ﬁve attributes (gender, age, region, language, and legal area). In our experiments, we evaluate pretrained language models using several grouprobust ﬁne-tuning..."
DATE_ADDED: 20260208
LLM_assessed: "BERT, elmo"
DATA_URL: "https://github.com/coastalcph/fairlex"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# FairLex: A Multilingual Benchmark for Evaluating Fairness in Legal Text Processing

## Authors

[[Ilias Chalkidis|Chalkidis, Ilias]], [[Tommaso Pasini|Pasini, Tommaso]], [[Sheng Zhang|Zhang, Sheng]], [[Letizia Tomada|Tomada, Letizia]], [[Sebastian Felix Schwemer|Schwemer, Sebastian Felix]], [[Anders Søgaard|Søgaard, Anders]]

## Links

- **Local PDF:** [[PDFs/2022/2022-Chalkidis-FairLex.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.301/

## Abstract

We present a benchmark suite of four datasets for evaluating the fairness of pre-trained language models and the techniques used to fine-tune them for downstream tasks. Our benchmarks cover four jurisdictions (European Council, USA, Switzerland, and China), five languages (English, German, French, Italian and Chinese) and fairness across five attributes (gender, age, region, language, and legal area). In our experiments, we evaluate pre-trained language models using several group-robust fine-tuning techniques and show that performance group disparities are vibrant in many cases, while none of these techniques guarantee fairness, nor consistently mitigate group disparities. Furthermore, we provide a quantitative and qualitative analysis of our results, highlighting open challenges in the development of robustness methods in legal NLP.

## Data Description

FairLex is a multilingual fairness benchmark suite comprising four legal text classification datasets covering four jurisdictions (European Council, USA, Switzerland, China), five languages (English, German, French, Italian, Chinese), and fairness across five attributes (gender, age, region, language, legal area). The datasets include ECtHR (11K cases), SCOTUS (9,262 cases), FSCS (85K+ decisions), and CAIL (100K+ criminal cases), all with chronological train/dev/test splits and annotated sensitive attributes for fairness evaluation.


## Notes

