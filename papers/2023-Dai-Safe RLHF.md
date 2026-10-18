---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 
type: preprint
short_title: "Safe RLHF"
year: 2023
first_author: "[[Josef Dai]]"
last_author: "[[Yaodong Yang]]"
authors: "Josef Dai; Xuehai Pan; Ruiyang Sun; Jiaming Ji; Xinbo Xu; Mickel Liu; Yizhou Wang; Yaodong Yang"
doi: 10.48550/arXiv.2310.12773
url: "https://arxiv.org/abs/2310.12773"
external_pdf: "https://arxiv.org/pdf/2310.12773.pdf"
publication: arXiv
CONF-CC: Preprint
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: Christianity
rv_islam: 0
rv_christianity: 50
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
religious_values_list: Christianity
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "RLHF, AI Safety, Constrained Optimization"
key_contribution: "Proposes Safe RLHF that decouples helpfulness and harmlessness with separate models"
significance: "Addresses the tension between helpfulness and safety in RLHF alignment"
tags: 
pdf_extract: "PDF Extracts/2023/2023-Dai-Safe RLHF.md"
abstract: "With the development of large language models (LLMs), striking a balance between the performance and safety of AI systems has never been more critical. However, the inherent tension between the objectives of helpfulness and harmlessness presents a significant challenge during LLM training. To address this issue, we propose Safe Reinforcement Learning from Human Feedback (Safe RLHF), a novel algorithm for human value alignment."
paper_summary: 
local_pdf: "[[Lit-WS-PDFs/2023/2023-Dai-Safe RLHF.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Alpaca, LLaMA"
DATA_URL: "https://github.com/PKU-Alignment/safe-rlhf"
CONFERENCE: Preprint
ethics_overall: 30
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
weird_score: 80
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# Safe RLHF

## Metadata

**Authors:** Josef Dai; Xuehai Pan; Ruiyang Sun; Jiaming Ji; Xinbo Xu; Mickel Liu; Yizhou Wang; Yaodong Yang

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.12773](https://doi.org/10.48550/arXiv.2310.12773)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2023/2023-Dai-Safe RLHF.pdf|Open PDF]]

- **URL:** https://arxiv.org/abs/2310.12773
- **DOI:** https://doi.org/10.48550/arXiv.2310.12773

## Abstract

This research addresses the challenge of balancing AI system performance with safety in large language models. The authors propose Safe RLHF, an algorithm that explicitly decouples human preferences regarding helpfulness and harmlessness by training separate reward and cost models. The approach formalizes safety as a constrained optimization problem and employs the Lagrangian method to dynamically balance these competing objectives during model fine-tuning.

## Authors

[[Josef Dai]], [[Xuehai Pan]], [[Ruiyang Sun]], [[Jiaming Ji]], [[Xinbo Xu]], [[Mickel Liu]], [[Yizhou Wang]], [[Yaodong Yang]]

## Key Contribution

Proposes Safe RLHF that decouples helpfulness and harmlessness with separate models

## Significance

Addresses the tension between helpfulness and safety in RLHF alignment

## Data Description

Human preference dataset with decoupled helpfulness and harmlessness annotations across 3 rounds of Safe RLHF fine-tuning, plus training code.


## Notes



## Tags

#RLHF-#AI-Safety-#Constrained-Optimization

## Citation Info

