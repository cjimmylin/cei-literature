---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XHC6ZWYU
type: conferencePaper
short_title: DistillSeq
year: 2025
first_author: "[[Mingke Yang]]"
last_author: "[[Ling Shi]]"
authors: "Mingke Yang; Yuqi Chen; Yi Liu; Ling Shi"
doi: 10.1145/3650212.3680304
tags: 
url: "http://arxiv.org/abs/2407.10106"
external_pdf: "http://arxiv.org/pdf/2407.10106.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Proposed DistillSeq, a cost-effective framework for safety alignment testing that uses knowledge distillation and automated red-teaming to generate effective test cases."
significance: "Reduces the computational cost of red-teaming while significantly improving the detection of safety vulnerabilities (higher attack success rate discovery) compared to baseline methods."
pdf_extract: "PDF Extracts/2024/2024-Yang-DistillSeq.md"
abstract: "Large Language Models (LLMs) have showcased their remarkable capabilities in diverse domains, encompassing natural language un- derstanding, translation, and even code generation. The potential for LLMs to generate harmful content is a significant concern. This risk necessitates rigorous testing and comprehensive evaluation of LLMs to ensure safe and responsible use. However, extensive testing of LLMs requires substantial computational resources, making it an expensive endeavor. Therefore, explo"
paper_summary: "Abstract: Large Language Models (LLMs) have showcased their remarkable capabilities in diverse domains, encompassing natural language un- derstanding, translation, and even code generation. The potential for LL | Overview: DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation Mingke Yang ShanghaiTech University Shanghai, China yangmk@shanghaitech.edu.cn Yuqi Chen∗ Sha | Methodology: This section initiates with an explanation of the problem and sub- sequently elaborates on the two stages in our proposed framework, DistillSeq. The p | Key Findings: In this section, we present our evaluation of DistillSeq. The im- plementation details of DistillSeq are available on our project website 2. To assess | Conclusions: In this paper, we introduce a novel framework named DistillSeq, designed to minimize the cost of testing LLMs. Our approach com- bines knowledge disti"
local_pdf: [[PDFs/2024/2024-Yang-DistillSeq.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation methodology"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, Vicuna, Llama"
DATA_URL: "NA"
---
# DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation

## Metadata

**Authors:** Yang, Mingke; Chen, Yuqi; Liu, Yi; Shi, Ling

**Year:** 2024

**Publication:** Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis

**Type:** conferencePaper

**DOI:** [10.1145/3650212.3680304](https://doi.org/10.1145/3650212.3680304)

**Pages:** 578-589

## Links

- **Local PDF:** [[PDFs/2024/2024-Yang-DistillSeq.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2407.10106
- **DOI:** https://doi.org/10.1145/3650212.3680304

## Abstract

Large Language Models (LLMs) have showcased their remarkable capabilities in diverse domains, encompassing natural language understanding, translation, and even code generation. The potential for LLMs to generate harmful content is a significant concern. This risk necessitates rigorous testing and comprehensive evaluation of LLMs to ensure safe and responsible use. However, extensive testing of LLMs requires substantial computational resources, making it an expensive endeavor. Therefore, exploring cost-saving strategies during the testing phase is crucial to balance the need for thorough evaluation with the constraints of resource availability. To address this, our approach begins by transferring the moderation knowledge from an LLM to a small model. Subsequently, we deploy two distinct strategies for generating malicious queries: one based on a syntax tree approach, and the other leveraging an LLM-based method. Finally, our approach incorporates a sequential filter-test process designed to identify test cases that are prone to eliciting toxic responses. By doing so, we significantly curtail unnecessary or unproductive interactions with LLMs, thereby streamlining the testing process. Our research evaluated the efficacy of DistillSeq across four LLMs: GPT-3.5, GPT-4.0, Vicuna-13B, and Llama-13B. In the absence of DistillSeq, the observed attack success rates on these LLMs stood at 31.5% for GPT-3.5, 21.4% for GPT-4.0, 28.3% for Vicuna-13B, and 30.9% for Llama-13B. However, upon the application of DistillSeq, these success rates notably increased to 58.5%, 50.7%, 52.5%, and 54.4%, respectively. This translated to an average escalation in attack success rate by a factor of 93.0% when compared to scenarios without the use of DistillSeq. Such findings highlight the significant enhancement DistillSeq offers in terms of reducing the time and resource investment required for effectively testing LLMs.

## Authors

[[Mingke Yang]], [[Yuqi Chen]], [[Yi Liu]], [[Ling Shi]]

## Data Description

DistillSeq is a framework for safety alignment testing of LLMs that uses knowledge distillation to transfer moderation knowledge from target LLMs to smaller distilled models, then applies sequential filter-test processes with syntax tree-based and LLM-based malicious query generation methods. The framework was evaluated on four LLMs (GPT-3.5, GPT-4, Vicuna-13B, and Llama-13B), demonstrating a 93% average increase in attack success rate while significantly reducing testing costs.


## Notes


## Tags

#Computer-Science---Software-Engineering

## Citation Info

2 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] 2 citations (Crossref/DOI) [2025-08-23] arXiv:2407.10106 [cs]
