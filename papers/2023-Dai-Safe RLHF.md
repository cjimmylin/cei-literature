---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 
type: preprint
short_title: "Safe RLHF"
year: 2025
first_author: "[[Josef Dai]]"
last_author: "[[Yaodong Yang]]"
authors: "Josef Dai; Xuehai Pan; Ruiyang Sun; Jiaming Ji; Xinbo Xu; Mickel Liu; Yizhou Wang; Yaodong Yang"
doi: 10.48550/arXiv.2310.12773
url: "https://arxiv.org/abs/2310.12773"
external_pdf: "https://arxiv.org/pdf/2310.12773.pdf"
publication: arXiv
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "RLHF, AI Safety, Constrained Optimization"
key_contribution: "Proposes Safe RLHF that decouples helpfulness and harmlessness with separate models"
significance: "Addresses the tension between helpfulness and safety in RLHF alignment"
tags: 
pdf_extract: "PDF Extracts/2023/2023-Dai-Safe RLHF.md"
abstract: "This research addresses the challenge of balancing AI system performance with safety in large language models. The authors propose Safe RLHF, an algorithm that explicitly decouples human preferences regarding helpfulness and harmlessness by training separate reward and cost models. The approach formalizes safety as a constrained optimization problem and employs the Lagrangian method to dynamically balance these competing objectives during model fine-tuning...."
paper_summary: 
local_pdf: "[[PDFs/2023/2023-Dai-Safe RLHF.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "Alpaca, Llama"
DATA_URL: "https://github.com/PKU-Alignment/safe-rlhf"
---
# Safe RLHF

## Metadata

**Authors:** Josef Dai; Xuehai Pan; Ruiyang Sun; Jiaming Ji; Xinbo Xu; Mickel Liu; Yizhou Wang; Yaodong Yang

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.12773](https://doi.org/10.48550/arXiv.2310.12773)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Dai-Safe RLHF.pdf|Open PDF]]

- **URL:** https://arxiv.org/abs/2310.12773
- **DOI:** https://doi.org/10.48550/arXiv.2310.12773

## Abstract

This research addresses the challenge of balancing AI system performance with safety in large language models. The authors propose Safe RLHF, an algorithm that explicitly decouples human preferences regarding helpfulness and harmlessness by training separate reward and cost models. The approach formalizes safety as a constrained optimization problem and employs the Lagrangian method to dynamically balance these competing objectives during model fine-tuning.

## Authors

[[Josef Dai]], [[Xuehai Pan]], [[Rui Sun|Ruiyang Sun]], [[Jiaming Ji]], [[Xinbo Xu]], [[Mickel Liu]], [[Yizhou Wang]], [[Yaodong Yang]]

## Key Contribution

Proposes Safe RLHF that decouples helpfulness and harmlessness with separate models

## Significance

Addresses the tension between helpfulness and safety in RLHF alignment

## Data Description

The study uses human preference datasets decoupled into helpfulness and harmlessness dimensions, collected across three iterative rounds of Safe RLHF fine-tuning. The Alpaca-7B model (based on LLaMA-7B) is fine-tuned through three cycles, producing Beaver-v1, v2, and v3 models. The preference data covers 14 predefined safety categories with crowdworker annotations including safety meta-labels for each QA pair.


## Notes



## Tags

#RLHF-#AI-Safety-#Constrained-Optimization

## Citation Info

