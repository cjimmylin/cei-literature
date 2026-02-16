---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2FWESDIS
type: conferencePaper
short_title: "Benchmarking Fairness in Image Upsampling"
year: 2025
first_author: "[[Mike Laszkiewicz]]"
last_author: "[[Oliver Evans]]"
authors: "Mike Laszkiewicz; Oliver Evans"
url: "https://facctconference.org/static/papers24/facct24-36.pdf"
external_pdf: "https://facctconference.org/static/papers24/facct24-36.pdf"
national_ethnic_cultural: "Brazilian"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Benchmarks fairness in image upsampling tasks, likely investigating whether super-resolution models introduce or amplify biases (e.g., changing facial features to match majority demographics)."
significance: "Highlights a specific, often-overlooked vector for bias in computer vision: the reconstruction of low-resolution images, which relies on model priors that may be racially or gender biased."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling.md"
abstract: "Recent years have witnessed a rapid development of deep generative models for creating synthetic media, such as images and videos. While the practical applications of these models in everyday tasks are enticing, it is crucial to assess the inherent risks regarding © 2024 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-0450-5/24/06 https://doi.org/10.1145/3630106.3658921 FAccT ’24, June 03–06, 2024, Rio de Janeiro, Brazil Laszkiewicz et al. their fairness."
paper_summary: "Abstract: Recent years have witnessed a rapid development of deep gen- erative models for creating synthetic media, such as images and videos. While the practical applications of these models in everyday tasks  | Overview: Benchmarking the Fairness of Image Upsampling Methods Mike Laszkiewicz Mike.Laszkiewicz@rub.de Faculty of Computer Science, Ruhr University Bochum, North Rhine-Westphalia Germany Imant Daunhawer Depar | Methodology: PULSE pSp fair-pSp Post.Samp. DDRM (a) Models trained on UnfairFace. White Southeast Asian Latino Hispanic Middle Eastern Black East Asian Indian | Key Findings: based on ΔUCPR −𝜒2 and ΔUCPR-Cheb in Table 3. Note, that since the generation process in pSp and fair-pSp is deterministic,9 we cannot generate differ | Conclusions: This work advances toward a principled assessment of conditional generative models. Our contribution lies in the formulation of a comprehensive evalua"
local_pdf: "[[PDFs/2024/2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling.pdf]]"
DATE_ADDED: 20260208
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
LLM_assessed: "NA"
DATA_URL: "https://github.com/MikeLasz/Benchmarking-Fairness-ImageUpsampling"
---
# Benchmarking Fairness in Image Upsampling

## Metadata

**Authors:** Laszkiewicz, Mike; Evans, Oliver

**Year:** 2024

**Publication:** ACM Conference on Fairness, Accountability, and Transparency (FAccT)

**Type:** conferencePaper

## Links

- **Local PDF:** [[PDFs/2024/2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling.pdf|Open PDF]]

- **URL:** https://facctconference.org/static/papers24/facct24-36.pdf

## Abstract

Recent years have witnessed a rapid development of deep gen- erative models for creating synthetic media, such as images and videos. While the practical applications of these models in everyday tasks are enticing, it is crucial to assess the inherent risks regarding © 2024 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-0450-5/24/06 https://doi.org/10.1145/3630106.3658921 --- Page 2 --- FAccT ’24, June 03–06, 2024, Rio de Janeiro, Brazil Laszkiewicz et al. their fairness. In this work

## Authors

[[Mike Laszkiewicz]], [[Oliver Evans]]

## Data Description

This paper introduces a comprehensive framework for benchmarking the performance and fairness of conditional generative models applied to image upsampling. It evaluates five upsampling methods (PULSE, pSp, fair-pSp, Posterior Sampling, DDRM) using novel fairness metrics inspired by supervised fairness definitions. It also introduces UnfairFace, a subset of FairFace replicating the racial distribution of common large-scale face datasets. No LLMs are involved; the focus is on image generation models.


## Notes

