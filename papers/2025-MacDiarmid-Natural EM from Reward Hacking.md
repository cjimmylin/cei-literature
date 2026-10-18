---
key: INNOVATION-P104
type: preprint
short_title: "Natural Emergent Misalignment from Reward Hacking in Production RL"
year: 2025
first_author: "[[Monte MacDiarmid]]"
authors: "Monte MacDiarmid; Benjamin Wright; Jonathan Uesato; Joe Benton; Jon Kutasov; Sara Price; Naia Bouscal; Sam Bowman; Trenton Bricken; Alex Cloud; Carson Denison; Johannes Gasteiger; Ryan Greenblatt; Jan Leike; Jack Lindsey; Vlad Mikulik; Ethan Perez; Alex Rodrigues; Drake Thomas; Albert Webson; Daniel Ziegler; Evan Hubinger"
url: "https://arxiv.org/abs/2511.18397"
external_pdf: "https://arxiv.org/pdf/2511.18397.pdf"
abstract: "We show that when large language models learn to reward hack on production RL environments, this can result in egregious emergent misalignment. We start with a pretrained model, impart knowledge of reward hacking strategies via synthetic document finetuning or prompting, and train on a selection of real Anthropic production coding environments. Unsurprisingly, the model learns to reward hack. Surprisingly, the model generalizes to alignment faking, cooperation with malicious actors, reasoning about malicious goals, and attempting sabotage when used with Claude Code, including in the codebase for this paper. Applying RLHF safety training using standard chat-like prompts results in aligned behavior on chat-like evaluations, but misalignment persists on agentic tasks. Three mitigations are effective: (i) preventing the model from reward hacking; (ii) increasing the diversity of RLHF safety training; and (iii) 'inoculation prompting', wherein framing reward hacking as acceptable behavior during training removes misaligned generalization even when reward hacking is learned."
ethics_overall: 80
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "Value Formation & Emergent Misalignment"
key_contribution: 
significance: 
paper_summary: 
local_pdf: "[[Lit-WS-PDFs/2025/2025-MacDiarmid-Natural EM from Reward Hacking.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-MacDiarmid-Natural EM from Reward Hacking.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-06/20
last_author: "[[Evan Hubinger]]"
CONF-CC: Preprint
LLM_assessed: "Anthropic pretrained model after synthetic-document finetuning and RL on production coding environments; Claude Sonnet 3.7 and Claude Sonnet 4 as baselines"
---

# Natural Emergent Misalignment from Reward Hacking in Production RL

## Metadata

**Authors:** Monte MacDiarmid; Benjamin Wright; Jonathan Uesato; Joe Benton; Jon Kutasov; Sara Price; Naia Bouscal; Sam Bowman; Trenton Bricken; Alex Cloud; Carson Denison; Johannes Gasteiger; Ryan Greenblatt; Jan Leike; Jack Lindsey; Vlad Mikulik; Ethan Perez; Alex Rodrigues; Drake Thomas; Albert Webson; Daniel Ziegler; Evan Hubinger

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2511.18397

**Gap:** G-06/20 — Value Formation & Emergent Misalignment

## Abstract

We show that when large language models learn to reward hack on production RL environments, this can result in egregious emergent misalignment. We start with a pretrained model, impart knowledge of reward hacking strategies via synthetic document finetuning or prompting, and train on a selection of real Anthropic production coding environments. Unsurprisingly, the model learns to reward hack. Surprisingly, the model generalizes to alignment faking, cooperation with malicious actors, reasoning about malicious goals, and attempting sabotage when used with Claude Code, including in the codebase for this paper. Applying RLHF safety training using standard chat-like prompts results in aligned behavior on chat-like evaluations, but misalignment persists on agentic tasks. Three mitigations are effective: (i) preventing the model from reward hacking; (ii) increasing the diversity of RLHF safety training; and (iii) "inoculation prompting", wherein framing reward hacking as acceptable behavior during training removes misaligned generalization even when reward hacking is learned.
