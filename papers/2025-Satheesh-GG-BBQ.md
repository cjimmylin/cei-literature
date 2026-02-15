---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: FTLRPK6B
type: document
short_title: GG-BBQ
year: 2025
first_author: "[[Shalaka Satheesh]]"
last_author: "[[Teena Hassan]]"
authors: "Shalaka Satheesh; Katrin Klug; Katharina Beckh; Héctor Allende-Cid; Sebastian Houben; Teena Hassan"
url: "https://arxiv.org/abs/2507.16410"
external_pdf: "https://arxiv.org/pdf/2507.16410.pdf"
national_ethnic_cultural: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "German, Bias & Fairness"
key_contribution: "Translated the BBQ benchmark into German (GG-BBQ), addressing the linguistic challenges of grammatical gender in bias evaluation."
significance: "Highlights the difficulty of porting English bias benchmarks to gendered languages (like German), ensuring that bias evaluation tools are available for non-English NLP."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Satheesh-GG-BBQ.md"
abstract: "Within the context of Natural Language Processing (NLP), fairness evaluation is often associated with the assessment of bias and reduction of associated harm. In this regard, the evaluation is usually carried out by using a benchmark dataset, for a task such as Question Answering, created for the measurement of bias in the model’s predictions along various dimensions, including gender identity. In our work, we evaluate gender bias in German Large Language Models (LLMs) using the Bias Benchmark..."
paper_summary: "Abstract: Within the context of Natural Language Pro- cessing (NLP), fairness evaluation is often asso- ciated with the assessment of bias and reduction of associated harm. In this regard, the evalua- tion is u | Overview: GG-BBQ: German Gender Bias Benchmark for Question Answering Shalaka Satheesh1,2, Katrin Klug1,2, Katharina Beckh1,2, Héctor Allende-Cid1,2, Sebastian Houben1,3, Teena Hassan3 1Fraunhofer Institute for | Methodology: by Jin et al. (2024). | Key Findings: Extrinsic bias evaluation is usually carried out by evaluating models on a dataset followed by com- putation of a metric (Gallegos et al., 2024). The  | Conclusions: In evaluating the bias of various LLMs, we contex- tualize the findings and discuss the potential impact of instruction-tuning and model size. Further"
local_pdf: [[PDFs/2025/2025-Satheesh-GG-BBQ.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Llama, Mistral"
DATA_URL: "https://github.com/shalakasatheesh/GG-BBQ/"
---
# GG-BBQ: German Gender Bias Benchmark for Question Answering

## Metadata

**Authors:** Satheesh, Shalaka; Klug, Katrin; Beckh, Katharina; Allende-Cid, Hector; Houben, Sebastian; Hassan, Teena

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Satheesh-GG-BBQ.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2507.16410

## Abstract

Within the context of Natural Language Processing (NLP), fairness evaluation is often associated with the assessment of bias and reduction of associated harm. In this regard, the evaluation is usually carried out by using a benchmark dataset, for a task such as Question Answering, created for the measurement of bias in the model's predictions along various dimensions, including gender identity. In our work, we evaluate gender bias in German Large Language Models (LLMs) using the Bias Benchmark for Question Answering by Parrish et al. (2022) as a reference. Specifically, the templates in the gender identity subset of this English dataset were machine translated into German. The errors in the machine translated templates were then manually reviewed and corrected with the help of a language expert. We find that manual revision of the translation is crucial when creating datasets for gender bias evaluation because of the limitations of machine translation from English to a language such as German with grammatical gender. Our final dataset is comprised of two subsets: Subset-I, which consists of group terms related to gender identity, and Subset-II, where group terms are replaced with proper names. We evaluate several LLMs used for German NLP on this newly created dataset and report the accuracy and bias scores. The results show that all models exhibit bias, both along and against existing social stereotypes.

## Authors

[[Shalaka Satheesh]], [[Katrin Klug]], [[Katharina Beckh]], [[Hector Allende-Cid|Héctor Allende-Cid]], [[Sebastian Houben]], [[Teena Hassan]]

## Data Description

The paper presents GG-BBQ (German Gender Bias Benchmark for Question Answering), a German translation of the gender identity subset of the BBQ dataset containing two subsets: Subset-I with 968 samples using group terms and Subset-II with 4,968 samples using proper names, each split between ambiguous and disambiguated contexts. Ten model variants were evaluated including Llama-3.2-3B, DiscoLeo-8B, Mistral-7B-v0.3, leo-hessianai-13b, and Llama-3.1-70B in both base and instruction-tuned versions.


## Notes


## Citation Info

2 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2507.16410
