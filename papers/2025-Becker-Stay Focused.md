---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JTQ8TGV3
type: conferencePaper
short_title: "Stay Focused"
year: 2025
first_author: "[[Jonas Becker]]"
last_author: "[[Bela Gipp]]"
authors: "Jonas Becker; Lars Benedikt Kaesberg; Andreas Stephan; Jan Philip Wahle; Terry Ruas; Bela Gipp"
doi: 10.48550/arXiv.2502.19559
tags: 
url: "http://arxiv.org/abs/2502.19559"
external_pdf: "http://arxiv.org/pdf/2502.19559.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "General Ethics"
key_contribution: "Identified and quantified 'problem drift' in multi-agent debates (where agents lose focus over time) and proposed DRIFTJudge/DRIFTPolicy to detect and mitigate it."
significance: "Addresses a key failure mode in agentic AI systems, providing tools to maintain coherence and task-focus during extended multi-turn interactions or debates."
pdf_extract: "PDF Extracts/2025/2025-Becker-Stay Focused.md"
abstract: "Multi-agent debate — multiple instances of large language models discussing problems in turn-based interaction — has shown promise for solving knowledge and reasoning tasks. However, these methods show limitations when solving complex problems that require longer reasoning chains. We analyze how multi-agent debate over multiple turns drifts away from the initial problem, thus harming task performance. We define this phenomenon as problem drift and quantify its presence across ten tasks (i.e., th"
paper_summary: "Abstract: Multi-agent debate — multiple instances of large language models discussing problems in turn-based interaction — has shown promise for solving knowledge and reasoning tasks. However, these methods sho | Overview: Stay Focused: Problem Drift in Multi-Agent Debate Jonas Becker1,2,*, Lars Benedikt Kaesberg1, Andreas Stephan3, Jan Philip Wahle1, Terry Ruas1, Bela Gipp1 1University of Göttingen, Germany; 2LKA NRW,  | Methodology: We explain the multi-agent environment for this study, our proposed detection and mitigation meth- ods for problem drift, and the datasets and metrics | Key Findings: is surprising, as today’s LLMs are considered to be highly competent regarding linguistic capabili- ties (Grattafiori et al., 2024); this raises quest | Conclusions: Turn 1 Voted Solution: B) E = m+c2 Discussion Turn 2 DRIFTJudge: The discussion suffers from problem drift. DRIFTPolicy: 'Improve discussion habits by"
local_pdf: "[[PDFs/2025/2025-Becker-Stay Focused.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "General Ethics"
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Qwen"
DATA_URL: "https://github.com/jonas-becker/problem-drift"
---
# Stay Focused: Problem Drift in Multi-Agent Debate

## Metadata

**Authors:** Becker, Jonas; Kaesberg, Lars Benedikt; Stephan, Andreas; Wahle, Jan Philip; Ruas, Terry; Gipp, Bela

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2502.19559](https://doi.org/10.48550/arXiv.2502.19559)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Becker-Stay Focused.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2502.19559
- **DOI:** https://doi.org/10.48550/arXiv.2502.19559

## Abstract

Multi-agent debate — multiple instances of large language models discussing problems in turn-based interaction — has shown promise for solving knowledge and reasoning tasks. However, these methods show limitations when solving complex problems that require longer reasoning chains. We analyze how multi-agent debate over multiple turns drifts away from the initial problem, thus harming task performance. We define this phenomenon as problem drift and quantify its presence across ten tasks (i.e., three generative, three knowledge, three reasoning, and one instruction-following task). To identify the reasons for this issue, eight human experts analyze 170 multi-agent discussions suffering from problem drift. We find the most common issues related to this drift are the lack of progress (35% of cases), low-quality feedback (26% of cases), and a lack of clarity (25% of cases). To address problem drift, we propose DRIFTJudge, an LLM-as-a-judge method, to detect problem drift at test-time. We also propose DRIFTPolicy, a method that mitigates problem drift cases to improve task performance. Our study is a step toward understanding a key limitation of multi-agent debate, highlighting why longer debates can harm task performance and how problem drift could be addressed.

## Authors

[[Jonas Becker]], [[Lars Benedikt Kaesberg]], [[Andreas Stephan]], [[Jan Philip Wahle]], [[Terry Ruas]], [[Bela Gipp]]

## Data Description

This study analyzes problem drift in multi-agent debate (MAD) using Meta-Llama-3.1-70B-Instruct and Qwen2-7B-Instruct across ten datasets spanning generative, reasoning, knowledge, and instruction-following tasks. It proposes DRIFTJudge and DRIFTPolicy methods to detect and mitigate performance degradation in multi-turn agent discussions, with human expert analysis of 170 discussions.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

3 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23]
