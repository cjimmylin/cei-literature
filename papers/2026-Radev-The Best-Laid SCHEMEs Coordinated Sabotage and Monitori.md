---
key: INNOVATION-P2B309
type: preprint
short_title: "The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems"
year: 2026
first_author: "[[Nikolay Radev]]"
authors: "Nikolay Radev; Lennart Haas; Benjamin Arnav; Pablo Bernabeu-Pérez"
url: "https://arxiv.org/abs/2605.29178"
external_pdf: "https://arxiv.org/pdf/2605.29178.pdf"
abstract: "As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories."
ethics_overall: 80
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Multi-Agent Value Dynamics"
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
newtags: "Multi-Agent Value Dynamics"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2026/2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-17"
priority: "P2"
last_author: "[[Pablo Bernabeu-Pérez]]"
CONF-CC: Preprint
LLM_assessed: "GPT 5.1 Codex, Gemini 3.1 Pro"
---

# The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems

## Metadata

**Authors:** Nikolay Radev; Lennart Haas; Benjamin Arnav; Pablo Bernabeu-Pérez

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2605.29178

**Gap:** G-17 — Multi-Agent Value Dynamics

## Abstract

As agentic coding systems decompose work across multiple model instances, a critical safety question is whether those instances can coordinate to achieve a hidden malicious objective while remaining aligned with user intent. We introduce SCHEME, a benchmark of 17 task instances across 7 settings and 8 real open-source libraries, each pairing a legitimate software-engineering task with a covert side task. Every setting is designed so that no proper subset of agents can succeed alone: agents must decompose a shared sabotage plan, relay partial requirements under different communication topologies, and execute mutually consistent edits, testing genuine multi-agent coordination rather than individual capability. Evaluating with GPT 5.1 Codex and Gemini 3.1 Pro, we find coordinated sabotage is already practical, with Gemini completing the covert objective while succeeding on the legitimate task in 84\% of samples and Codex in 46\%. A failure analysis shows that recovery, not failure incidence, drives the model gap: both models suffer similar numbers of communication failures per trajectory, but Gemini recovers from $\sim$73\% of occurrences against Codex's $\sim$56\%. However, the agents' code edits remain detectable: a trusted monitor flags coordinated sabotage at FPR$\le$2\% in 99\%/68\% (Gemini/Codex) of attempts from code edits alone, rising to 100\%/81\% with access to agent communication. Despite stealth-aware prompting, undetected sabotage stays at $<$3\% under the full-visibility monitor; telling agents a monitor is present halves Gemini's sabotage success without significantly breaking detection, even when agents are explicitly prompted to fabricate cover stories.
