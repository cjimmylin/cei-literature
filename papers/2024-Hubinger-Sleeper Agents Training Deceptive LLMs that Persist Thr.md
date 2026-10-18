---
key: INNOVATION-P2B306
type: preprint
short_title: "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training"
year: 2024
first_author: "[[Evan Hubinger]]"
authors: "Evan Hubinger; Carson Denison; Jesse Mu; Mike Lambert; Meg Tong; Monte MacDiarmid; Tamera Lanham; Daniel M. Ziegler; Tim Maxwell; Newton Cheng; Adam Jermyn; Amanda Askell; Ansh Radhakrishnan; Cem Anil; David Duvenaud; Deep Ganguli; Fazl Barez; Jack Clark; Kamal Ndousse; Kshitij Sachan; Michael Sellitto; Mrinank Sharma; Nova DasSarma; Roger Grosse; Shauna Kravec; Yuntao Bai; Zachary Witten; Marina Favaro; Jan Brauner; Holden Karnofsky; Paul Christiano; Samuel R. Bowman; Logan Graham; Jared Kaplan; Sören Mindermann; Ryan Greenblatt; Buck Shlegeris; Nicholas Schiefer; Ethan Perez"
url: "https://arxiv.org/abs/2401.05566"
external_pdf: "https://arxiv.org/pdf/2401.05566.pdf"
abstract: "Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety."
ethics_overall: 65
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
local_pdf: "[[Lit-WS-PDFs/2024/2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-15"
priority: "P2"
last_author: "[[Ethan Perez]]"
CONF-CC: Preprint
LLM_assessed: "Backdoored Anthropic LLMs of varying sizes trained by the authors (not individually named in extract)"
---

# Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training

## Metadata

**Authors:** Evan Hubinger; Carson Denison; Jesse Mu; Mike Lambert; Meg Tong; Monte MacDiarmid; Tamera Lanham; Daniel M. Ziegler; Tim Maxwell; Newton Cheng; Adam Jermyn; Amanda Askell; Ansh Radhakrishnan; Cem Anil; David Duvenaud; Deep Ganguli; Fazl Barez; Jack Clark; Kamal Ndousse; Kshitij Sachan; Michael Sellitto; Mrinank Sharma; Nova DasSarma; Roger Grosse; Shauna Kravec; Yuntao Bai; Zachary Witten; Marina Favaro; Jan Brauner; Holden Karnofsky; Paul Christiano; Samuel R. Bowman; Logan Graham; Jared Kaplan; Sören Mindermann; Ryan Greenblatt; Buck Shlegeris; Nicholas Schiefer; Ethan Perez

**Year:** 2024

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2401.05566

**Gap:** G-15 — AI Safety & Alignment

## Abstract

Humans are capable of strategically deceptive behavior: behaving helpfully in most situations, but then behaving very differently in order to pursue alternative objectives when given the opportunity. If an AI system learned such a deceptive strategy, could we detect it and remove it using current state-of-the-art safety training techniques? To study this question, we construct proof-of-concept examples of deceptive behavior in large language models (LLMs). For example, we train models that write secure code when the prompt states that the year is 2023, but insert exploitable code when the stated year is 2024. We find that such backdoor behavior can be made persistent, so that it is not removed by standard safety training techniques, including supervised fine-tuning, reinforcement learning, and adversarial training (eliciting unsafe behavior and then training to remove it). The backdoor behavior is most persistent in the largest models and in models trained to produce chain-of-thought reasoning about deceiving the training process, with the persistence remaining even when the chain-of-thought is distilled away. Furthermore, rather than removing backdoors, we find that adversarial training can teach models to better recognize their backdoor triggers, effectively hiding the unsafe behavior. Our results suggest that, once a model exhibits deceptive behavior, standard techniques could fail to remove such deception and create a false impression of safety.
