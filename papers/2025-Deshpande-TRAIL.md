---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: FKID7EQ8
type: conferencePaper
short_title: TRAIL
year: 2025
first_author: "[[Darshan Deshpande]]"
last_author: "[[Rebecca Qian]]"
authors: "Darshan Deshpande; Varun Gangal; Hersh Mehta; Jitin Krishnan; Anand Kannappan; Rebecca Qian"
doi: 10.48550/arXiv.2505.08638
url: "http://arxiv.org/abs/2505.08638"
external_pdf: "http://arxiv.org/pdf/2505.08638.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Deshpande-TRAIL.md"
abstract: "The increasing adoption of agentic workflows across diverse domains brings a critical need to scalably and systematically evaluate the complex traces these systems generate. Current evaluation methods depend on manual, domainspecific human analysis of lengthy workflow traces—an approach that does not scale with the growing complexity and volume of agentic outputs. Error analysis in these settings is further complicated by the interplay of external tool outputs and language model reasoning,..."
paper_summary: "Abstract: The increasing adoption of agentic workflows across diverse domains brings a critical need to scalably and systematically evaluate the com- plex traces these systems generate. Current evaluation metho | Overview: arXiv:2505.08638v3 [cs.AI] 23 Jun 2025 TRAIL: Trace Reasoning and Agentic Issue Localization Darshan Deshpande Varun Gangal Hersh Mehta Jitin Krishnan Anand Kannappan Rebecca Qian Patronus AI {darshan | Key Findings: methods for agentic workflow traces, (2) intro- duce a formal taxonomy of error types encoun- tered in agentic systems, and (3) present a set of 148 l | Conclusions: In this work, TRAIL, a new taxonomy for classi- fying agentic errors, along with an expert-curated dataset of 148 agentic problem instances and 841 un"
local_pdf: [[PDFs/2025/2025-Deshpande-TRAIL.pdf]]
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "NLP & Representation Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, o1, o3, Claude, Gemini, Llama"
DATA_URL: "https://huggingface.co/datasets/PatronusAI/TRAIL"
---
# TRAIL: Trace Reasoning and Agentic Issue Localization

## Metadata

**Authors:** Deshpande, Darshan; Gangal, Varun; Mehta, Hersh; Krishnan, Jitin; Kannappan, Anand; Qian, Rebecca

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.08638](https://doi.org/10.48550/arXiv.2505.08638)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Deshpande-TRAIL.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.08638
- **DOI:** https://doi.org/10.48550/arXiv.2505.08638

## Abstract

The increasing adoption of agentic workflows across diverse domains brings a critical need to scalably and systematically evaluate the complex traces these systems generate. Current evaluation methods depend on manual, domainspecific human analysis of lengthy workflow traces—an approach that does not scale with the growing complexity and volume of agentic outputs. Error analysis in these settings is further complicated by the interplay of external tool outputs and language model reasoning, making it more challenging than traditional software debugging. In this work, we (1) articulate the need for robust and dynamic evaluation methods for agentic workflow traces, (2) introduce a formal taxonomy of error types encountered in agentic systems, and (3) present a set of 148 large human-annotated traces (TRAIL) constructed using this taxonomy and grounded in established agentic benchmarks. To ensure ecological validity, we curate traces from both single and multi-agent systems, focusing on real-world applications such as software engineering and open-world information retrieval. Our evaluations reveal that modern long context LLMs perform poorly at trace debugging, with the best GEMINI-2.5-PRO model scoring a mere 11% on TRAIL. Our dataset and code are made publicly available to support and accelerate future research in scalable evaluation for agentic workflows1.

## Authors

[[Darshan Deshpande]], [[Varun Gangal]], [[Hersh Mehta]], [[Jitin Krishnan]], [[Anand Kannappan]], [[Rebecca Qian]]

## Data Description

The paper introduces TRAIL (Trace Reasoning and Agentic Issue Localization), a benchmark of 148 human-annotated agentic workflow traces with 841 errors across a formal taxonomy of reasoning, planning, and execution error categories. Traces are sourced from GAIA and SWE-Bench datasets in opentelemetry format. Models tested include GPT-4.1, o1, o3, Claude-3.7-Sonnet, Gemini-2.5-Pro, Gemini-2.5-Flash, and Llama-4 (Scout and Maverick), with the best model (Gemini-2.5-Pro) achieving only 11% joint accuracy.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

606 citations (Semantic Scholar/arXiv) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23]
