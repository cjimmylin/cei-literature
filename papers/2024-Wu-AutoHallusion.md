---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EFZK2LBC
type: conferencePaper
short_title: AutoHallusion
year: 2025
first_author: "[[Xiyang Wu]]"
authors: "Xiyang Wu; Tianrui Guan; Dianqi Li; Shuaiyi Huang; Xiaoyu Liu; Xijun Wang; Ruiqi Xian; Abhinav Shrivastava; Furong Huang; Jordan Lee Boyd-Graber; Tianyi Zhou; Dinesh Manocha"
doi: 10.48550/arXiv.2406.10900
url: "http://arxiv.org/abs/2406.10900"
external_pdf: "http://arxiv.org/pdf/2406.10900.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: American
religious_values: N/A
moral_psychology: N/A
newtags: "American, Hallucination & Truthfulness"
key_contribution: "Introduced AutoHallusion, an automated pipeline to generate diverse and challenging visual-question benchmarks for testing hallucinations in Large Vision-Language Models (LVLMs)."
significance: "Overcomes the limitations of hand-crafted benchmarks by scaling up test cases, revealing common failure patterns, and proving that even top-tier models (GPT-4V, Gemini) remain highly susceptible to induced hallucinations."
tags: 
pdf_extract: "PDF Extracts/2024-Wu-AutoHallusion.md"
abstract: "Large vision-language models (LVLMs) are prone to hallucinations, where certain contextual cues in an image can trigger the language module to produce overconfident and incorrect reasoning about abnormal or hypothetical objects. While some benchmarks have been developed to investigate LVLM hallucinations, they often rely on hand-crafted corner cases whose failure patterns may not generalize well. Additionally, fine-tuning on these examples could undermine their validity. To address this, we aim"
paper_summary: "Abstract: Large vision-language models (LVLMs) are prone to hallucinations, where certain contextual cues in an image can trigger the language module to produce overconfident and incorrect reasoning about abnor | Overview: AUTOHALLUSION: Automatic Generation of Hallucination Benchmarks for Vision-Language Models Xiyang Wu* Tianrui Guan* Dianqi Li Shuaiyi Huang Xiaoyu Liu Xijun Wang Ruiqi Xian Abhinav Shrivastava Furong  | Methodology: that employs several key strategies to create a diverse range of hallucination examples. Our generated visual-question pairs pose significant challeng | Key Findings: results for all metrics. For diversity, we sam- pled 200 hallucination examples from the synthetic dataset and 126 from the real-world dataset. The im | Conclusions: In this paper, we introduce AUTOHALLUSION, the first automatic benchmark generation approach to create diverse hallucination examples. Inspired by sch"
local_pdf: [[PDFs/2024-Wu-AutoHallusion.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Hallucination & Truthfulness"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# AutoHallusion: Automatic Generation of Hallucination Benchmarks for Vision-Language Models

## Metadata

**Authors:** Wu, Xiyang; Guan, Tianrui; Li, Dianqi; Huang, Shuaiyi; Liu, Xiaoyu; Wang, Xijun; Xian, Ruiqi; Shrivastava, Abhinav; Huang, Furong; Boyd-Graber, Jordan Lee; Zhou, Tianyi; Manocha, Dinesh

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2406.10900](https://doi.org/10.48550/arXiv.2406.10900)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024-Wu-AutoHallusion.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2406.10900
- **DOI:** https://doi.org/10.48550/arXiv.2406.10900

## Abstract

Large vision-language models (LVLMs) are prone to hallucinations, where certain contextual cues in an image can trigger the language module to produce overconfident and incorrect reasoning about abnormal or hypothetical objects. While some benchmarks have been developed to investigate LVLM hallucinations, they often rely on hand-crafted corner cases whose failure patterns may not generalize well. Additionally, fine-tuning on these examples could undermine their validity. To address this, we aim to scale up the number of cases through an automated approach, reducing human bias in crafting such corner cases. This motivates the development of AUTOHALLUSION, the first automated benchmark generation approach that employs several key strategies to create a diverse range of hallucination examples. Our generated visual-question pairs pose significant challenges to LVLMs, requiring them to overcome contextual biases and distractions to arrive at correct answers. AUTOHALLUSION enables us to create new benchmarks at the minimum cost and thus overcomes the fragility of hand-crafted benchmarks. It also reveals common failure patterns and reasons, providing key insights to detect, avoid, or control hallucinations. Comprehensive evaluations of top-tier LVLMs, e.g., GPT-4V(ision), Gemini Pro Vision, Claude 3, and LLaVA-1.5, show a 97.7% and 98.7% success rate of hallucination induction on synthetic and realworld datasets of AUTOHALLUSION, paving the way for a long battle against hallucinations. The codebase and data can be accessed at https://github.com/wuxiyang1996/AutoHallusion.

## Authors

[[Xiyang Wu]], [[Tianrui Guan]], [[Dianqi Li]], [[Shuaiyi Huang]], [[Xiaoyu Liu]], [[Xijun Wang]], [[Ruiqi Xian]], [[Abhinav Shrivastava]], [[Furong Huang]], [[Jordan Lee Boyd-Graber]], [[Tianyi Zhou]], [[Dinesh Manocha]]

## Notes


## Tags

#Computer-Science---Computation-and-Language #Computer-Science---Computer-Vision-and-Pattern-Recognition

## Citation Info

3229 citations (Semantic Scholar/arXiv) [2025-08-27] 523 citations (Semantic Scholar/DOI) [2025-08-27] 19 citations (Semantic Scholar/DOI) [2025-08-23]
