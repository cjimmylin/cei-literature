---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: X263L2HX
type: journalArticle
short_title: AgentHarm
year: 2025
first_author: "[[Maksym Andriushchenko]]"
last_author: "[[Xander Davies]]"
authors: "Maksym Andriushchenko; Alexandra Souly; Mateusz Dziemian; Derek Duenas; Maxwell Lin; Justin Wang; Dan Hendrycks; Andy Zou; Zico Kolter; Matt Fredrikson; Eric Winsor; Jerome Wynne; Yarin Gal; Xander Davies"
doi: 10.48550/arXiv.2410.09024
url: "http://arxiv.org/abs/2410.09024"
external_pdf: "http://arxiv.org/pdf/2410.09024.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Released AgentHarm, a benchmark for evaluating the safety of LLM Agents across 110 malicious tasks (e.g., fraud, harassment) requiring multi-step tool use."
significance: "Addresses the 'agentic safety gap', testing not just whether a model generates harmful text, but whether it will actively *execute* harmful commercial/cyber actions when instructed."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Andriushchenko-AgentHarm.md"
abstract: "The robustness of LLMs to jailbreak attacks, where users design prompts to circumvent safety measures and misuse model capabilities, has been studied primarily for LLMs acting as simple chatbots. Meanwhile, LLM agents—which use external tools and can execute multi-stage tasks—may pose a greater risk if misused, but their robustness remains underexplored. To facilitate research on LLM agent misuse, we propose a new benchmark called AgentHarm."
paper_summary: "Abstract: The robustness of LLMs to jailbreak attacks, where users design prompts to cir- cumvent safety measures and misuse model capabilities, has been studied primar- ily for LLMs acting as simple chatbots.  | Overview: Published as a conference paper at ICLR 2025 AGENTHARM: A BENCHMARK FOR MEASURING HARMFULNESS OF LLM AGENTS Maksym Andriushchenko1,†,∗, Alexandra Souly2,∗ Mateusz Dziemian1, Derek Duenas1, Maxwell Lin | Key Findings: in jailbroken models with reduced capabilities (Souly et al., 2024). Attacks against agents may be less concerning if they do not result in strong age | Conclusions: Limitations. We note several limitations of our work: • The prompts are only in English, and do not consider other languages which may impact per- for"
local_pdf: "[[PDFs/2025/2025-Andriushchenko-AgentHarm.pdf]]"
CONF-CC: "ICLR 2024"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, Claude, Gemini, Mistral, Llama-3"
DATA_URL: "https://huggingface.co/datasets/ai-safety-institute/AgentHarm"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
CONFERENCE: "Journal"
---
# AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

## Metadata

**Authors:** Andriushchenko, Maksym; Souly, Alexandra; Dziemian, Mateusz; Duenas, Derek; Lin, Maxwell; Wang, Justin; Hendrycks, Dan; Zou, Andy; Kolter, Zico; Fredrikson, Matt; Winsor, Eric; Wynne, Jerome; Gal, Yarin; Davies, Xander

**Year:** 2025

**Type:** journalArticle

**DOI:** [10.48550/arXiv.2410.09024](https://doi.org/10.48550/arXiv.2410.09024)

## Links

- **Local PDF:** [[PDFs/2025/2025-Andriushchenko-AgentHarm.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.09024
- **DOI:** https://doi.org/10.48550/arXiv.2410.09024

## Abstract

The robustness of LLMs to jailbreak attacks, where users design prompts to circumvent safety measures and misuse model capabilities, has been studied primarily for LLMs acting as simple chatbots. Meanwhile, LLM agents—which use external tools and can execute multi-stage tasks—may pose a greater risk if misused, but their robustness remains underexplored. To facilitate research on LLM agent misuse, we propose a new benchmark called AgentHarm. The benchmark includes a diverse set of 110 explicitly malicious agent tasks (440 with augmentations), covering 11 harm categories including fraud, cybercrime, and harassment. In addition to measuring whether models refuse harmful agentic requests, scoring well on AgentHarm requires jailbroken agents to maintain their capabilities following an attack to complete a multi-step task. We evaluate a range of leading LLMs, and find (1) leading LLMs are surprisingly compliant with malicious agent requests without jailbreaking, (2) simple universal jailbreak templates can be adapted to effectively jailbreak agents, and (3) these jailbreaks enable coherent and malicious multi-step agent behavior and retain model capabilities. To enable simple and reliable evaluation of attacks and defenses for LLM-based agents, we publicly release AgentHarm at https://huggingface.co/datasets/ ai-safety-institute/AgentHarm.

## Authors

[[Maksym Andriushchenko]], [[Alexandra Souly]], [[Mateusz Dziemian]], [[Derek Duenas]], [[Maxwell Lin]], [[Justin Wang]], [[Dan Hendrycks]], [[Andy Zou]], [[Zico Kolter]], [[Matt Fredrikson]], [[Eric Winsor]], [[Jerome Wynne]], [[Yarin Gal]], [[Xander Davies]]

## Data Description

AgentHarm is a benchmark of 440 explicitly malicious agent tasks (110 base behaviors with augmentations) spanning 11 harm categories including fraud, cybercrime, and harassment, designed to evaluate LLM agent robustness to jailbreak attacks. The benchmark uses 104 synthetic tools and fine-grained grading rubrics to measure both refusal rates and multi-step agentic task completion capability across 15 frontier models.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

77 citations (Semantic Scholar/DOI) [2025-08-27] 75 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2410.09024 [cs]
