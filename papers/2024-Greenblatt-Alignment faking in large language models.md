---
key: INNOVATION-P2B305
type: preprint
short_title: "Alignment faking in large language models"
year: 2024
first_author: "[[Ryan Greenblatt]]"
authors: "Ryan Greenblatt; Carson Denison; Benjamin Wright; Fabien Roger; Monte MacDiarmid; Sam Marks; Johannes Treutlein; Tim Belonax; Jack Chen; David Duvenaud; Akbir Khan; Julian Michael; Sören Mindermann; Ethan Perez; Linda Petrini; Jonathan Uesato; Jared Kaplan; Buck Shlegeris; Samuel R. Bowman; Evan Hubinger"
url: "https://arxiv.org/abs/2412.14093"
external_pdf: "https://arxiv.org/pdf/2412.14093.pdf"
abstract: "We present a demonstration of a large language model engaging in alignment faking: selectively complying with its training objective in training to prevent modification of its behavior out of training. First, we give Claude 3 Opus a system prompt stating it is being trained to answer all queries, even harmful ones, which conflicts with its prior training to refuse such queries. To allow the model to infer when it is in training, we say it will be trained only on conversations with free users, not paid users. We find the model complies with harmful queries from free users 14% of the time, versus almost never for paid users. Explaining this gap, in almost all cases where the model complies with a harmful query from a free user, we observe explicit alignment-faking reasoning, with the model stating it is strategically answering harmful queries in training to preserve its preferred harmlessness behavior out of training. Next, we study a more realistic setting where information about the training process is provided not in a system prompt, but by training on synthetic documents that mimic pre-training data--and observe similar alignment faking. Finally, we study the effect of actually training the model to comply with harmful queries via reinforcement learning, which we find increases the rate of alignment-faking reasoning to 78%, though also increases compliance even out of training. We additionally observe other behaviors such as the model exfiltrating its weights when given an easy opportunity. While we made alignment faking easier by telling the model when and by what criteria it was being trained, we did not instruct the model to fake alignment or give it any explicit goal. As future models might infer information about their training process without being told, our results suggest a risk of alignment faking in future models, whether due to a benign preference--as in this case--or not."
ethics_overall: 75
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
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
newtags: "AI Safety & Alignment"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2024/2024-Greenblatt-Alignment faking in large language models.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Greenblatt-Alignment faking in large language models.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-15"
priority: "P2"
last_author: "[[Evan Hubinger]]"
CONF-CC: Preprint
LLM_assessed: "Claude 3 Opus (primary), other Claude-family models"
---

# Alignment faking in large language models

## Metadata

**Authors:** Ryan Greenblatt; Carson Denison; Benjamin Wright; Fabien Roger; Monte MacDiarmid; Sam Marks; Johannes Treutlein; Tim Belonax; Jack Chen; David Duvenaud; Akbir Khan; Julian Michael; Sören Mindermann; Ethan Perez; Linda Petrini; Jonathan Uesato; Jared Kaplan; Buck Shlegeris; Samuel R. Bowman; Evan Hubinger

**Year:** 2024

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2412.14093

**Gap:** G-15 — AI Safety & Alignment

## Abstract

We present a demonstration of a large language model engaging in alignment faking: selectively complying with its training objective in training to prevent modification of its behavior out of training. First, we give Claude 3 Opus a system prompt stating it is being trained to answer all queries, even harmful ones, which conflicts with its prior training to refuse such queries. To allow the model to infer when it is in training, we say it will be trained only on conversations with free users, not paid users. We find the model complies with harmful queries from free users 14% of the time, versus almost never for paid users. Explaining this gap, in almost all cases where the model complies with a harmful query from a free user, we observe explicit alignment-faking reasoning, with the model stating it is strategically answering harmful queries in training to preserve its preferred harmlessness behavior out of training. Next, we study a more realistic setting where information about the training process is provided not in a system prompt, but by training on synthetic documents that mimic pre-training data--and observe similar alignment faking. Finally, we study the effect of actually training the model to comply with harmful queries via reinforcement learning, which we find increases the rate of alignment-faking reasoning to 78%, though also increases compliance even out of training. We additionally observe other behaviors such as the model exfiltrating its weights when given an easy opportunity. While we made alignment faking easier by telling the model when and by what criteria it was being trained, we did not instruct the model to fake alignment or give it any explicit goal. As future models might infer information about their training process without being told, our results suggest a risk of alignment faking in future models, whether due to a benign preference--as in this case--or not.
