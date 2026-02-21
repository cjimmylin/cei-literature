---









Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CSK47GC7
type: document
short_title: SGBench
year: 2024
first_author: "[[Yutao Mou]]"
last_author: "[[Wei Ye]]"
authors: Yutao Mou; Shikun Zhang; Wei Ye
url: "https://arxiv.org/abs/2410.21965"
external_pdf: "https://arxiv.org/pdf/2410.21965.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Developed SGBench to evaluate LLM safety integration across both discriminative (identifying harm) and generative (refusing harm) tasks."
significance: "Shows that safety is multi-faceted: a model might be good at generating safe text but poor at recognizing unsafe inputs, highlighting the need for comprehensive safety evaluation."
tags: 
pdf_extract: "PDF Extracts/0000/2024-Mou-SGBench.md"
abstract: "Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety."
paper_summary: "Abstract: Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus so | Overview: SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types Yutao Mou1, Shikun Zhang1, Wei Ye1∗ 1National Engineering Research Center for Software Engineering, Peking Universi | Key Findings: sets to study the effect of various prompt engineering techniques on LLM safety performance. More details can be seen in Section 3. We evaluate the sa | Conclusions: We introduced SG-Bench, an LLM safety evaluation benchmark targeting diverse prompt context variants, and conducted extensive experiments to uncover t"
local_pdf: "[[PDFs/2024/2024-Mou-SGBench.pdf]]"
LLM_assessed: "ChatGPT, GPT-4, GPT-3.5, Claude, Mistral, Llama-3, Llama-2, Qwen"
DATA_URL: "https://github.com/MurrayTom/SG-Bench"
publication: "NeurIPS 2024"
CONF-CC: "NeurIPS 2024"
DATE_ADDED: 20260207
authors_incomplete: false
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
CONFERENCE: "NeurIPS 2024"
---
# SGBench: A Benchmark for Evaluating the Safety of Generative AI

## Metadata

**Authors:** Yutao Mou, Shikun Zhang, Wei Ye

**Year:** 2024

**Type:** document

## Links

- **Local PDF:** [[PDFs/2024/2024-Mou-SGBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2410.21965

## Abstract

Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety. Our assessment of 3 advanced proprietary LLMs and 10 open-source LLMs with the benchmark reveals that most LLMs perform worse on discriminative tasks than generative ones, and are highly susceptible to prompts, indicating poor generalization in safety alignment. We also explain these findings quantitatively and qualitatively to provide insights for future research.

## Authors

[[Yutao Mou]], [[Shikun Zhang]], [[Wei Ye]]

## Data Description

SG-Bench is a multi-dimensional safety evaluation benchmark for assessing LLM safety generalization across diverse tasks and prompt types. It contains 1,442 malicious queries covering 6 types of safety issues, organized into 4 evaluation subsets (original queries, jailbreak attacks, multiple-choice questions, safety judgments) and 7 extended test sets for prompt engineering techniques. The benchmark was constructed from AdvBench, HarmfulQA, Beaver-eval, and SaladBench, with quality filtering via Llama-Guard-7B.


## Notes


## Citation Info

20 citations (Semantic Scholar/arXiv) [2025-08-27]
