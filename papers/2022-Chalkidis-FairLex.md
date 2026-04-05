---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JU8JYC2E
type: document
short_title: FairLex
year: 2022
first_author: "[[Ilias Chalkidis]]"
last_author: "[[Søgaard, Anders]]"
authors: "Chalkidis, Ilias; Pasini, Tommaso; Zhang, Sheng; Tomada, Letizia; Schwemer, Sebastian Felix; Søgaard, Anders"
url: "https://aclanthology.org/2022.acl-long.301/"
external_pdf: "http://arxiv.org/pdf/2203.07228"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Chinese, English, French, German, Italian"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Chinese, French, German, Italian, Bias & Fairness"
key_contribution: "Created FairLex, a multilingual benchmark (EN, DE, FR, IT, ZH) for fairness in legal text processing, covering 4 jurisdictions."
significance: "Shows that 'legal fairness' is jurisdictional – what counts as bias in Swiss law differs from US law, and models trained on one don't transfer to the other."
tags: 
pdf_extract: "PDF Extracts/2022/2022-Chalkidis-FairLex.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2022/2022-Chalkidis-FairLex.pdf]]"
abstract: "We present a benchmark suite of four datasets for evaluating the fairness of pre-trained language models and the techniques used to ﬁne-tune them for downstream tasks. Our benchmarks cover four jurisdictions (European Council, USA, Switzerland, and China), ﬁve languages (English, German, French, Italian and Chinese) and fairness across ﬁve attributes (gender, age, region, language, and legal area). In our experiments, we evaluate pretrained language models using several grouprobust ﬁne-tuning..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "https://github.com/coastalcph/fairlex"
CONFERENCE: "ACL 2022"
ethics_overall: 75
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 35
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "DK"
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
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

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2022/2022-Chalkidis-FairLex.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.301/

## Abstract

We present a benchmark suite of four datasets for evaluating the fairness of pre-trained language models and the techniques used to fine-tune them for downstream tasks. Our benchmarks cover four jurisdictions (European Council, USA, Switzerland, and China), five languages (English, German, French, Italian and Chinese) and fairness across five attributes (gender, age, region, language, and legal area). In our experiments, we evaluate pre-trained language models using several group-robust fine-tuning techniques and show that performance group disparities are vibrant in many cases, while none of these techniques guarantee fairness, nor consistently mitigate group disparities. Furthermore, we provide a quantitative and qualitative analysis of our results, highlighting open challenges in the development of robustness methods in legal NLP.

## Data Description

FairLex benchmark suite of four legal datasets across four jurisdictions (ECtHR, SCOTUS, FSCS, CAIL), five languages, and fairness across five attributes. Includes four domain-specific BERT models and unified HuggingFace dataset release.


## Notes

