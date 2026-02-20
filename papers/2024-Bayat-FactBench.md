---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: C8U952G6
type: conferencePaper
short_title: FactBench
year: 2024
first_author: "[[Farima Fatahi Bayat]]"
last_author: "[[Lu Wang]]"
authors: "Farima Fatahi Bayat; Lechen Zhang; Sheza Munir; Lu Wang"
doi: 10.48550/arXiv.2410.22257
tags: 
url: "http://arxiv.org/abs/2410.22257"
external_pdf: "http://arxiv.org/pdf/2410.22257.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
CONF-CC: "ACL 2024"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
pdf_extract: "PDF Extracts/2024/2024-Bayat-FactBench.md"
abstract: "The rapid adoption of language models (LMs) across diverse applications has raised concerns about their factuality, i.e., their consistency with real-world facts. We first present VERIFY (Verification and Evidence RetrIeval for FactualitY evaluation), a pipeline to evaluate LMs’ factuality in real-world user interactions. VERIFY considers the verifiability of LM-generated content and categorizes content units as supported, unsupported, or undecidable based on Web-retrieved evidence."
paper_summary: "Abstract: The rapid adoption of language models (LMs) across diverse applications has raised concerns about their factuality, i.e., their consistency with real-world facts. We first present VER- IFY (Verificati | Overview: FactBench: A Dynamic Benchmark for In-the-Wild Language Model Factuality Evaluation Farima Fatahi Bayat, Lechen Zhang, Sheza Munir, Lu Wang University of Michigan, Ann Arbor {farimaf, leczhang, shezam | Methodology: by labeling such cases as undecidable. While this evidence-based strategy may yield lower factuality scores, it ensures more trustworthy evaluations.  | Key Findings: Farima Fatahi Bayat, Lechen Zhang, Sheza Munir, Lu Wang University of Michigan, Ann Arbor {farimaf, leczhang, shezamnr, wangluxy}@umich.edu https://hu | Conclusions: We present VERIFY, a factuality evaluation pipeline that annotates LM responses in real-world settings by decomposing them into content units and labe"
local_pdf: "[[PDFs/2024/2024-Bayat-FactBench.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Gemini, Llama"
DATA_URL: "https://huggingface.co/spaces/launch/factbench"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for hallucination detection dataset"
data_metrics: "Not specified"
CONFERENCE: "ACL 2024"
---
# FactBench: A Dynamic Benchmark for In-the-Wild Language Model Factuality Evaluation

## Metadata

**Authors:** Bayat, Farima Fatahi; Zhang, Lechen; Munir, Sheza; Wang, Lu

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.22257](https://doi.org/10.48550/arXiv.2410.22257)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Bayat-FactBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.22257
- **DOI:** https://doi.org/10.48550/arXiv.2410.22257

## Abstract

The rapid adoption of language models (LMs) across diverse applications has raised concerns about their factuality, i.e., their consistency with real-world facts. We first present VERIFY (Verification and Evidence RetrIeval for FactualitY evaluation), a pipeline to evaluate LMs’ factuality in real-world user interactions. VERIFY considers the verifiability of LM-generated content and categorizes content units as supported, unsupported, or undecidable based on Web-retrieved evidence. Importantly, factuality judgment by VERIFY correlates better with human evaluations than existing methods. Using VERIFY, we identify “hallucination prompts” across diverse topics, i.e., those eliciting the highest rates of incorrect (unsupported) and inconclusive (undecidable) LM responses. These prompts form FACTBENCH, a dataset of 1K prompts across 150 fine-grained topics. Our dataset captures emerging factuality challenges in real-world LM interactions and can be regularly updated with new prompts. We benchmark widely-used LMs from GPT, Gemini, and Llama families on FACTBENCH, yielding the following key findings: (i) Proprietary models exhibit better factuality, with decreased performance from Easy to Hard hallucination prompts. (ii) Llama3.1-405B-Instruct shows comparable or lower factual precision than Llama3.1-70B-Instruct across all evaluation methods due to its higher subjectivity that leads to more content labeled as undecidable. (iii) Gemini1.5-Pro shows a significantly higher refusal rate, with over-refusal in 25% of cases.

## Authors

[[Farima Fatahi Bayat]], [[Lechen Zhang]], [[Sheza Munir]], [[Lu Wang]]

## Data Description

FACTBENCH is a dynamic benchmark of 1,000 diverse information-seeking prompts across 150 fine-grained topics, curated from real-world user-LLM interactions in the LMSYS-Chat-1M dataset. Prompts are categorized into three tiers (Hard, Moderate, Easy) based on their ability to elicit hallucinations from strong LLMs. The benchmark evaluates factuality of GPT-4o, Gemini1.5-Pro, Llama3.1-70B-Instruct, and Llama3.1-405B-Instruct using the VERIFY pipeline, which categorizes generated content units as supported, unsupported, or undecidable.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

9 citations (Semantic Scholar/DOI) [2025-08-27] 9 citations (Semantic Scholar/arXiv) [2025-08-27]
