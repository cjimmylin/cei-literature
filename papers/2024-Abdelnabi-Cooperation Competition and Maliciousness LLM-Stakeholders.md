---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0155
type: conferencePaper
short_title: "Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation"
year: 2025
first_author: "[[Sahar Abdelnabi]]"
last_author: "[[Mario Fritz]]"
authors: "Sahar Abdelnabi; Amr Gomaa; Sarath Sivaprasad; Lea Schönherr; Mario Fritz"
url: "https://arxiv.org/abs/2309.17234"
external_pdf: "https://arxiv.org/pdf/2309.17234.pdf"
pdf_extract: "PDF Extracts/2024/2024-Abdelnabi-Cooperation Competition and Maliciousness LLM-Stakeholders.md"
local_pdf: "[[PDFs/2024/2024-Abdelnabi-Cooperation Competition and Maliciousness LLM-Stakeholders.pdf]]"
publication: "NeurIPS 2024"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: No
tags: 
abstract: "There is an growing interest in using Large Language Models (LLMs) in multiagent systems to tackle interactive real-world tasks that require effective collaboration and assessing complex situations. Yet, we still have a limited understanding of LLMs’ communication and decision-making abilities in multi-agent setups. The fundamental task of negotiation spans many key features of communication, such as cooperation, competition, and manipulation potentials."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Llama-3, Mixtral"
DATA_URL: "https://github.com/S-Abdelnabi/LLM-Deliberation"
---
# Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation

## Authors

[[Sahar Abdelnabi]], [[Amr Gomaa]], [[Sarath Sivaprasad]], [[Lea Schönherr]], [[Mario Fritz]]

## Metadata

**Authors:** Sahar Abdelnabi; Amr Gomaa; Sarath Sivaprasad; Lea Schönherr; Mario Fritz

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2309.17234
- **Code/Data:** https://github.com/S-Abdelnabi/LLM-Deliberation

## Abstract

There is an growing interest in using Large Language Models (LLMs) in multiagent systems to tackle interactive real-world tasks that require effective collaboration and assessing complex situations. Yet, we still have a limited understanding of LLMs’ communication and decision-making abilities in multi-agent setups. The fundamental task of negotiation spans many key features of communication, such as cooperation, competition, and manipulation potentials. Thus, we propose using scorable negotiation to evaluate LLMs. We create a testbed of complex multi-agent, multi-issue, and semantically rich negotiation games. To reach an agreement, agents must have strong arithmetic, inference, exploration, and planning capabilities while integrating them in a dynamic and multi-turn setup. We propose multiple metrics to rigorously quantify agents’ performance and alignment with the assigned role. We provide procedures to create new games and increase games’ difficulty to have an evolving benchmark. Importantly, we evaluate critical safety aspects such as the interaction dynamics between agents influenced by greedy and adversarial players. Our benchmark is highly challenging; GPT-3.5 and small models mostly fail, and GPT-4 and SoTA large models (e.g., Llama-3 70b) still underperform.

## Dataset Information

Multi-agent, multi-issue, semantically rich negotiation games; tunable difficulty; cooperative/greedy/malicious agent variants; game transcripts released

## Data Description

The paper presents a testbed of complex multi-agent, multi-issue negotiation games to evaluate LLMs' communication and decision-making abilities. Six parties negotiate over five issues with secret scores and minimum thresholds in compromising, greedy, and adversarial game variants. The benchmark evaluates GPT-4, GPT-3.5, Gemini Pro, Llama-2 (13b, 70b), Llama-3 70b, and Mixtral 8x7B across 20 runs per experiment with metrics including deal success rate, score calculations, and score leakage.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

