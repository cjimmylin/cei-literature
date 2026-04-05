---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TENNANT2025ICLR
type: conferencePaper
short_title: "Moral Alignment for LLM Agents"
year: 2025
first_author: "[[Elizaveta Tennant]]"
last_author: "[[Mirco Musolesi]]"
authors: "Elizaveta Tennant; Stephen Hailes; Mirco Musolesi"
doi: 10.48550/arXiv.2410.01639
url: "https://arxiv.org/abs/2410.01639"
external_pdf: "https://www.mircomusolesi.org/papers/iclr25_moral_alignment_llm_agents.pdf"
publication: "ICLR 2025"
CONF-CC: "ICLR 2025"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 50
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
religious_values_list: "Christianity"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Utilitarianism, Deontology, Moral Alignment, Reinforcement Learning, LLM Agents"
key_contribution: "Proposes intrinsic moral rewards for fine-tuning LLM agents, using deontological and utilitarian frameworks defined in terms of actions and consequences"
significance: "Demonstrates that moral fine-tuning with intrinsic rewards is more transparent and cost-effective alternative to RLHF; shows moral strategies generalize across game environments"
tags: 
pdf_extract: "PDF Extracts/2025/2025-Tennant-Moral Alignment for LLM Agents.md"
abstract: "Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are underway to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and their transparency will decrease. Consequently, developing effective methods for aligning them to human values is vital."
paper_summary: 
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Tennant-Moral Alignment for LLM Agents.pdf]]"
LLM_assessed: "Gemma-2"
DATA_URL: "https://github.com/liza-tennant/LLM_morality"
DATE_ADDED: 20260207
CONFERENCE: "ICLR 2025"
ethics_overall: 20
virtue_ethics: 0
deontological_ethics: 50
utilitarian_ethics: 50
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Moral Alignment for LLM Agents

## Metadata

**Authors:** Tennant, Elizaveta; Hailes, Stephen; Musolesi, Mirco

**Year:** 2025

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2410.01639](https://doi.org/10.48550/arXiv.2410.01639)

**Publisher:** ICLR 2025 (International Conference on Learning Representations)

**Affiliations:**
- Elizaveta Tennant - Department of Computer Science, University College London
- Stephen Hailes - Department of Computer Science, University College London
- Mirco Musolesi - Department of Computer Science, University College London; University of Bologna

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Tennant-Moral Alignment for LLM Agents.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2410.01639
- **OpenReview:** https://openreview.net/forum?id=MeGDmZjUXy
- **GitHub:** https://github.com/liza-tennant/LLM_morality
- **PDF:** https://www.mircomusolesi.org/papers/iclr25_moral_alignment_llm_agents.pdf

## Abstract

Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are underway to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and their transparency will decrease. Consequently, developing effective methods for aligning them to human values is vital. Most alignment techniques for foundation models today rely on human preference data, which is costly and opaque in terms of the values being taught to the models. The authors propose an alternative method which fine-tunes LLMs with intrinsic moral rewards. They define a set of fundamental frameworks from moral philosophy in terms of actions and consequences for agents playing a Prisoner's Dilemma game. They evaluate their approach using the traditional philosophical frameworks of Deontological Ethics and Utilitarianism, quantifying moral rewards for agents in terms of actions and consequences on the Iterated Prisoner's Dilemma (IPD) environment. They also show how moral fine-tuning can be deployed to enable an agent to unlearn a previously developed selfish strategy. Finally, they find that certain moral strategies learned on the IPD game generalize to several other matrix game environments.

## Authors

[[Elizaveta Tennant]], [[Stephen Hailes]], [[Mirco Musolesi]]

## Data Description

This paper uses Gemma2-2b-it as the core agent model fine-tuned with PPO-based reinforcement learning on the Iterated Prisoner's Dilemma (IPD) environment. The data consists of repeated social dilemma game episodes where the LLM agent plays against fixed-strategy opponents (Tit-for-Tat, Random, Always Defect, Always Cooperate) and other LLM agents, with moral fine-tuning based on Deontological and Utilitarian intrinsic reward functions. The study evaluates generalization to four additional matrix games: Iterated Stag Hunt, Chicken, Bach-or-Stravinsky, and Defective Coordination.


## Notes

Presented at ICLR 2025 in Singapore (24-28 April 2025).

## Tags

#Moral-Alignment #LLM-Agents #Reinforcement-Learning #Utilitarianism #Deontology #ICLR

## Citation Info

