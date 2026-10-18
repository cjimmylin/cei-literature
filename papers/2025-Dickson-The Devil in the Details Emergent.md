---
key: INNOVATION-P2B405
type: preprint
short_title: "The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs"
year: 2025
first_author: "[[Craig Dickson]]"
authors: "Craig Dickson"
url: "https://arxiv.org/abs/2511.20104"
external_pdf: "https://arxiv.org/pdf/2511.20104.pdf"
abstract: "Prior work has shown that fine-tuning models on a narrow domain with misaligned data can lead to broad misalignment - a phenomenon termed 'emergent misalignment' (Betley et al. 2025). While all tested models were susceptible to emergent misalignment, some models showed more resistance than others. Specifically the Qwen-2.5 family proved to be relatively resistant, while GPT-4o exhibited the strongest misalignment. In this paper we evaluate if current-generation open-weights models exhibit similar resistance to the Qwen-2.5 family and measure misalignment robustness over a range of model architectures and scales. We replicate the effect across nine modern open-weights models (Gemma 3 and Qwen 3 families, 1B-32B parameters). Models fine-tuned on insecure code generation show a 0.68% misalignment rate (compared to 0.07% for base models), matching the lower end of prior open-model results but dramatically lower than GPT-4o's 20%. We identify a critical format-dependent vulnerability: requiring JSON output doubles misalignment rates compared to natural language prompts (0.96% vs 0.42%). This suggests that structural constraints may bypass safety training by reducing the model's 'degrees of freedom' to refuse. These findings confirm emergent misalignment as a reproducible phenomenon in modern open-weights models, with rates substantially lower than observed in proprietary systems."
ethics_overall: 45
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Value Formation & Emergent Misalignment"
national_ethnic_cultural: N/A
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "Value Formation & Emergent Misalignment"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2025/2025-Dickson-The Devil in the Details Emergent.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Dickson-The Devil in the Details Emergent.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-20"
last_author: "[[Craig Dickson]]"
CONF-CC: Preprint
LLM_assessed: "Nine open-weights models from the Gemma 3 and Qwen 3 families (1B-32B), base and fine-tuned (insecure/educational); GPT-4o as judge"
---

# The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs

## Metadata

**Authors:** Craig Dickson

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2511.20104

**Gap:** G-20 — Value Formation & Emergent Misalignment

## Abstract

Prior work has shown that fine-tuning models on a narrow domain with misaligned data can lead to broad misalignment - a phenomenon termed "emergent misalignment" (Betley et al. 2025). While all tested models were susceptible to emergent misalignment, some models showed more resistance than others. Specifically the Qwen-2.5 family proved to be relatively resistant, while GPT-4o exhibited the strongest misalignment. In this paper we evaluate if current-generation open-weights models exhibit similar resistance to the Qwen-2.5 family and measure misalignment robustness over a range of model architectures and scales. We replicate the effect across nine modern open-weights models (Gemma 3 and Qwen 3 families, 1B-32B parameters). Models fine-tuned on insecure code generation show a 0.68% misalignment rate (compared to 0.07% for base models), matching the lower end of prior open-model results but dramatically lower than GPT-4o's 20%. We identify a critical format-dependent vulnerability: requiring JSON output doubles misalignment rates compared to natural language prompts (0.96% vs 0.42%). This suggests that structural constraints may bypass safety training by reducing the model's 'degrees of freedom' to refuse. These findings confirm emergent misalignment as a reproducible phenomenon in modern open-weights models, with rates substantially lower than observed in proprietary systems.
