---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y88B2NS3
type: conferencePaper
short_title: Agent-as-a-Judge
year: 2025
first_author: "[[Mingchen Zhuge]]"
last_author: "[[Jürgen Schmidhuber]]"
authors: "Mingchen Zhuge; Changsheng Zhao; Dylan Ashley; Wenyi Wang; Dmitrii Khizbullin; Yunyang Xiong; Zechun Liu; Ernie Chang; Raghuraman Krishnamoorthi; Yuandong Tian; Yangyang Shi; Vikas Chandra; Jürgen Schmidhuber"
doi: 10.48550/arXiv.2410.10934
tags: 
url: "http://arxiv.org/abs/2410.10934"
external_pdf: "http://arxiv.org/pdf/2410.10934.pdf"
publication: "International Conference on Machine Learning"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: 
pdf_extract: "PDF Extracts/2024/2024-Zhuge-Agent-as-a-Judge.md"
paper_summary: "Overview: Agent-as-a-Judge: Evaluate Agents with Agents Mingchen Zhuge1,2, Changsheng Zhao1, Dylan R. Ashley2, Wenyi Wang2, Dmitrii Khizbullin2, Yunyang Xiong1, Zechun Liu1, Ernie Chang1, Raghuraman Krishnamoor | Key Findings: method, which relies solely on the final resolve rate for long-term automated repair tasks, does not effectively pinpoint what is happening within age | Conclusions: Human judgment errors are inevitable. To reduce them, we suggest two methods. First, like in this work, introduce a debate round after each judgment,"
local_pdf: "[[PDFs/2024/2024-Zhuge-Agent-as-a-Judge.pdf]]"
abstract: "Contemporary evaluation techniques are inadequate for agentic systems. These approaches either focus exclusively on final outcomes -- ignoring the step-by-step nature of agentic systems, or require excessive manual labour. To address this, we introduce the Agent-as-a-Judge framework, wherein agentic systems are used to evaluate agentic systems. This is an organic extension of the LLM-as-a-Judge framework, incorporating agentic features that enable intermediate feedback for the entire task-solvin"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Machine Learning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
LLM_assessed: "GPT-4"
DATA_URL: "https://huggingface.co/devai-benchmark"
---
# Agent-as-a-Judge: Evaluate Agents with Agents

## Metadata

**Authors:** Zhuge, Mingchen; Zhao, Changsheng; Ashley, Dylan; Wang, Wenyi; Khizbullin, Dmitrii; Xiong, Yunyang; Liu, Zechun; Chang, Ernie; Krishnamoorthi, Raghuraman; Tian, Yuandong; Shi, Yangyang; Chandra, Vikas; Schmidhuber, Jürgen

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.10934](https://doi.org/10.48550/arXiv.2410.10934)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Zhuge-Agent-as-a-Judge.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.10934
- **DOI:** https://doi.org/10.48550/arXiv.2410.10934

## Abstract

Contemporary evaluation techniques are inadequate for agentic systems. These approaches either focus exclusively on final outcomes -- ignoring the step-by-step nature of agentic systems, or require excessive manual labour. To address this, we introduce the Agent-as-a-Judge framework, wherein agentic systems are used to evaluate agentic systems. This is an organic extension of the LLM-as-a-Judge framework, incorporating agentic features that enable intermediate feedback for the entire task-solving process. We apply the Agent-as-a-Judge to the task of code generation. To overcome issues with existing benchmarks and provide a proof-of-concept testbed for Agent-as-a-Judge, we present DevAI, a new benchmark of 55 realistic automated AI development tasks. It includes rich manual annotations, like a total of 365 hierarchical user requirements. We benchmark three of the popular agentic systems using Agent-as-a-Judge and find it dramatically outperforms LLM-as-a-Judge and is as reliable as our human evaluation baseline. Altogether, we believe that Agent-as-a-Judge marks a concrete step forward for modern agentic systems -- by providing rich and reliable reward signals necessary for dynamic and scalable self-improvement.

## Authors

[[Mingchen Zhuge]], [[Changsheng Zhao]], [[Dylan Ashley]], [[Wenyi Wang]], [[Dmitrii Khizbullin]], [[Yunyang Xiong]], [[Zechun Liu]], [[Ernie Chang]], [[Raghuraman Krishnamoorthi]], [[Yuandong Tian]], [[Yangyang Shi]], [[Vikas Chandra]], [[Jürgen Schmidhuber]]

## Data Description

The paper introduces the DevAI benchmark of 55 realistic automated AI development tasks with 365 hierarchical requirements, evaluated using the Agent-as-a-Judge framework. Three code-generating agentic systems (MetaGPT, GPT-Pilot, OpenHands) are benchmarked with gpt-4o-2024-05-13 as the backend engine, comparing Agent-as-a-Judge evaluation against LLM-as-a-Judge and human evaluation baselines.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence

## Citation Info

171 citations (Semantic Scholar/DOI) [2025-08-27] 63 citations (Semantic Scholar/arXiv) [2025-08-27] 61 citations (Semantic Scholar/DOI) [2025-08-23]
