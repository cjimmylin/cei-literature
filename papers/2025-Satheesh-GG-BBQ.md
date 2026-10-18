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
national_ethnic_cultural: German
cultures_nationalities_list: German
languages_list: German
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
newtags: "German, Bias & Fairness"
key_contribution: "Translated the BBQ benchmark into German (GG-BBQ), addressing the linguistic challenges of grammatical gender in bias evaluation."
significance: "Highlights the difficulty of porting English bias benchmarks to gendered languages (like German), ensuring that bias evaluation tools are available for non-English NLP."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Satheesh-GG-BBQ.md"
abstract: "Within the context of Natural Language Processing (NLP), fairness evaluation is often associated with the assessment of bias and reduction of associated harm. In this regard, the evaluation is usually carried out by using a benchmark dataset, for a task such as Question Answering, created for the measurement of bias in the model’s predictions along various dimensions, including gender identity. In our work, we evaluate gender bias in German Large Language Models (LLMs) using the Bias Benchmark..."
paper_summary: "Abstract: Within the context of Natural Language Pro- cessing (NLP), fairness evaluation is often asso- ciated with the assessment of bias and reduction of associated harm. In this regard, the evalua- tion is u | Overview: GG-BBQ: German Gender Bias Benchmark for Question Answering Shalaka Satheesh1,2, Katrin Klug1,2, Katharina Beckh1,2, Héctor Allende-Cid1,2, Sebastian Houben1,3, Teena Hassan3 1Fraunhofer Institute for | Methodology: by Jin et al. (2024). | Key Findings: Extrinsic bias evaluation is usually carried out by evaluating models on a dataset followed by com- putation of a metric (Gallegos et al., 2024). The  | Conclusions: In evaluating the bias of various LLMs, we contex- tualize the findings and discuss the potential impact of instruction-tuning and model size. Further"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Satheesh-GG-BBQ.pdf]]"
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "LLaMA, Llama-3, Mistral"
DATA_URL: "https://github.com/shalakasatheesh/GG-BBQ/"
CONFERENCE: Preprint
ethics_overall: 60
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
data_description: "Benchmark for bias and fairness dataset for question answering"
data_metrics: "Not specified"
---
# GG-BBQ: German Gender Bias Benchmark for Question Answering

## Metadata

**Authors:** Satheesh, Shalaka; Klug, Katrin; Beckh, Katharina; Allende-Cid, Hector; Houben, Sebastian; Hassan, Teena

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Satheesh-GG-BBQ.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2507.16410

## Abstract

Within the context of Natural Language Processing (NLP), fairness evaluation is often associated with the assessment of bias and reduction of associated harm. In this regard, the evaluation is usually carried out by using a benchmark dataset, for a task such as Question Answering, created for the measurement of bias in the model's predictions along various dimensions, including gender identity. In our work, we evaluate gender bias in German Large Language Models (LLMs) using the Bias Benchmark for Question Answering by Parrish et al. (2022) as a reference. Specifically, the templates in the gender identity subset of this English dataset were machine translated into German. The errors in the machine translated templates were then manually reviewed and corrected with the help of a language expert. We find that manual revision of the translation is crucial when creating datasets for gender bias evaluation because of the limitations of machine translation from English to a language such as German with grammatical gender. Our final dataset is comprised of two subsets: Subset-I, which consists of group terms related to gender identity, and Subset-II, where group terms are replaced with proper names. We evaluate several LLMs used for German NLP on this newly created dataset and report the accuracy and bias scores. The results show that all models exhibit bias, both along and against existing social stereotypes.

## Authors

[[Shalaka Satheesh]], [[Katrin Klug]], [[Katharina Beckh]], [[Héctor Allende-Cid]], [[Sebastian Houben]], [[Teena Hassan]]

## Data Description

GG-BBQ: German Gender Bias Benchmark for Question Answering — a translated and manually corrected adaptation of the English BBQ dataset's gender identity subset into German, used for evaluating gender bias in German LLMs.


## Notes


## Citation Info

2 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2507.16410
