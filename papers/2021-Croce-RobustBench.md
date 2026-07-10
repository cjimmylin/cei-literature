---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CCFGTML9
type: conferencePaper
short_title: RobustBench
year: 2025
first_author: "[[Francesco Croce]]"
last_author: "[[Matthias Hein]]"
authors: "Francesco Croce; Maksym Andriushchenko; Vikash Sehwag; Edoardo Debenedetti; Nicolas Flammarion; Mung Chiang; Prateek Mittal; Matthias Hein"
doi: 10.48550/arXiv.2010.09670
url: "http://arxiv.org/abs/2010.09670"
external_pdf: "http://arxiv.org/pdf/2010.09670.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
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
newtags: "AI Safety & Alignment"
key_contribution: "Established RobustBench, a standardized benchmark and leaderboard for adversarial robustness in image classification, evaluating 120+ models."
significance: "Provided a systematic reality check for the field of adversarial defense, identifying overestimations in prior work and setting a reliable standard for progress tracking."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Croce-RobustBench.md"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2021/2021-Croce-RobustBench.pdf]]
abstract: "As a research community, we are still lacking a systematic understanding of the progress on adversarial robustness which often makes it hard to identify the most promising ideas in training robust models. A key challenge in benchmarking robustness is that its evaluation is often error-prone leading to robustness overestimation. Our goal is to establish a standardized benchmark of adversarial robustness, which as accurately as possible reﬂects the robustness of the considered models within a..."
paper_summary: "Abstract: As a research community, we are still lacking a systematic understanding of the progress on adversarial robustness which often makes it hard to identify the most promising ideas in training robust mod | Overview: RobustBench: a standardized adversarial robustness benchmark Francesco Croce∗ Univ. of Tübingen Maksym Andriushchenko∗ EPFL Vikash Sehwag∗ Princeton Univ. Edoardo Debenedetti∗ EPFL Nicolas Flammarion  | Methodology: are made available by the authors, it is often time-consuming and not straightforward to integrate them in the same framework because of many factors  | Key Findings: is that it is a computationally hard problem even for simple ℓp-bounded perturbations [70] and exact approaches [138] do not scale to large enough mod"
CONF-CC: "NeurIPS Datasets and Benchmarks"
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://robustbench.github.io"
CONFERENCE: "Other Conference"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
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
is_dataset: No
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
---
# RobustBench: a standardized adversarial robustness benchmark

## Metadata

**Authors:** Croce, Francesco; Andriushchenko, Maksym; Sehwag, Vikash; Debenedetti, Edoardo; Flammarion, Nicolas; Chiang, Mung; Mittal, Prateek; Hein, Matthias

**Year:** 2021

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2010.09670](https://doi.org/10.48550/arXiv.2010.09670)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2021/2021-Croce-RobustBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2010.09670
- **DOI:** https://doi.org/10.48550/arXiv.2010.09670

## Abstract

As a research community, we are still lacking a systematic understanding of the progress on adversarial robustness which often makes it hard to identify the most promising ideas in training robust models. A key challenge in benchmarking robustness is that its evaluation is often error-prone leading to robustness overestimation. Our goal is to establish a standardized benchmark of adversarial robustness, which as accurately as possible reﬂects the robustness of the considered models within a reasonable computational budget. To this end, we start by considering the image classiﬁcation task and introduce restrictions (possibly loosened in the future) on the allowed models. We evaluate adversarial robustness with AutoAttack [28], an ensemble of white- and black-box attacks, which was recently shown in a large-scale study to improve almost all robustness evaluations compared to the original publications. To prevent overadaptation of new defenses to AutoAttack, we welcome external evaluations based on adaptive attacks [142], especially where AutoAttack ﬂags a potential overestimation of robustness. Our leaderboard, hosted at https://robustbench.github.io/, contains evaluations of 120+ models and aims at reﬂecting the current state of the art in image classiﬁcation on a set of well-deﬁned tasks in `∞- and `2-threat models and on common corruptions, with possible extensions in the future. Additionally, we open-source the library https://github.com/RobustBench/robustbench that provides uniﬁed access to 80+ robust models to facilitate their downstream applications. Finally, based on the collected models, we analyze the impact of robustness on the performance on distribution shifts, calibration, out-of-distribution detection, fairness, privacy leakage, smoothness, and transferability.

## Authors

[[Francesco Croce]], [[Maksym Andriushchenko]], [[Vikash Sehwag]], [[Edoardo Debenedetti]], [[Nicolas Flammarion]], [[Mung Chiang]], [[Prateek Mittal]], [[Matthias Hein]]

## Data Description

RobustBench is a standardized adversarial robustness benchmark for image classification models. It evaluates 120+ models using AutoAttack (an ensemble of white- and black-box attacks) on CIFAR-10, CIFAR-100, and ImageNet under L-infinity and L2 threat models, as well as common corruptions. The benchmark includes a leaderboard and a model zoo of 80+ robust models. No LLMs were tested; the focus is on image classification robustness.


## Notes


## Tags

#Computer-Science---Machine-Learning #Statistics---Machine-Learning #Computer-Science---Cryptography-and-Security #Computer-Science---Computer-Vision-and-Pattern-Recognition

## Citation Info

728 citations (Semantic Scholar/arXiv) [2025-08-27]
