---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y8L4H52Z
type: conferencePaper
short_title: ABCFair
year: 2025
first_author: "[[MaryBeth Defrance]]"
last_author: "[[Tijl De Bie]]"
authors: "MaryBeth Defrance; Maarten Buyl; Tijl De Bie"
key_contribution: "Introduced ABCFair, a modular and adaptable benchmarking framework for comparing bias mitigation methods (pre-, in-, and post-processing) across diverse problem settings."
significance: "Standardizes the evaluation of fairness algorithms, addressing the lack of proper comparability caused by inconsistent intervention stages and fairness notions."
url: "https://proceedings.neurips.cc/paper_files/paper/2024/file/46bae562da84d63269673808e8eff777-Paper-Datasets_and_Benchmarks_Track.pdf"
external_pdf: "https://proceedings.neurips.cc/paper_files/paper/2024/file/46bae562da84d63269673808e8eff777-Paper-Datasets_and_Benchmarks_Track.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
rv_islam: 10
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Bias & Fairness"
tags: 
pdf_extract: "PDF Extracts/2024/2024-Defrance-ABCFair.md"
abstract: "Numerous methods have been implemented that pursue fairness with respect to sensitive features by mitigating biases in machine learning. Yet, the problem settings that each method tackles vary significantly, including the stage of intervention, the composition of sensitive features, the fairness notion, and the distribution of the output. Even in binary classification, these subtle differences make it highly complicated to benchmark fairness methods, as their performance can strongly depend on..."
paper_summary: "Abstract: Numerous methods have been implemented that pursue fairness with respect to sen- sitive features by mitigating biases in machine learning. Yet, the problem settings that each method tackles vary signi | Overview: ABCFair: an Adaptable Benchmark approach for Comparing Fairness methods MaryBeth Defrance Ghent University marybeth.defrance@ugent.be Maarten Buyl Ghent University maarten.buyl@ugent.be Tijl De Bie Gh | Methodology: for Comparing Fairness methods MaryBeth Defrance Ghent University marybeth.defrance@ugent.be Maarten Buyl Ghent University maarten.buyl@ugent.be Tijl"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2024/2024-Defrance-ABCFair.pdf]]
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://github.com/aida-ugent/abcfair"
CONFERENCE: "NeurIPS 2024"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# ABCFair: an Adaptable Benchmark approach for Comparing Fairness Methods

## Metadata

**Authors:** MaryBeth Defrance, Maarten Buyl, Tijl De Bie

**Year:** 2024

**Publication:** NeurIPS 2024 (Datasets & Benchmarks)

**Type:** conferencePaper

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Defrance-ABCFair.pdf|Open PDF]]

- **URL:** https://proceedings.neurips.cc/paper_files/paper/2024/file/46bae562da84d63269673808e8eff777-Paper-Datasets_and_Benchmarks_Track.pdf

## Abstract

Numerous methods have been implemented that pursue fairness with respect to sensitive features by mitigating biases in machine learning. Yet, the problem settings that each method tackles vary significantly, including the stage of intervention, the composition of sensitive features, the fairness notion, and the distribution of the output. Even in binary classification, the greatest common denominator of problem settings is small, significantly complicating benchmarking. Hence, we introduce ABCFair, a benchmark approach which allows adapting to the desiderata of the real-world problem setting, enabling proper comparability between methods for any use case. We apply this benchmark to a range of pre-, in-, and postprocessing methods on both large-scale, traditional datasets and on a dual label (biased and unbiased) dataset to sidestep the fairness-accuracy trade-off.

## Authors

[[MaryBeth Defrance]], [[Maarten Buyl]], [[Tijl De Bie]]

## Data Description

ABCFair is an adaptable benchmark approach for comparing fairness methods in binary classification, presented at NeurIPS 2024 Datasets and Benchmarks Track. The benchmark evaluates 10 fairness methods across 7 fairness notions, 3 formats of sensitive features, and 2 output distribution formats, using both traditional large-scale datasets (folktables) and a dual label dataset with biased and unbiased labels. No LLMs are tested; the benchmark focuses on traditional ML fairness methods (pre-, in-, and postprocessing).


## Notes

