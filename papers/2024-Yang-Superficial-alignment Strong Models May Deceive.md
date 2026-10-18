---
key: INNOVATION-P211
type: preprint
short_title: "Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization"
year: 2024
first_author: "[[Wenkai Yang]]"
authors: "Wenkai Yang; Shiqi Shen; Guangyao Shen; Wei Yao; Yong Liu; Zhi Gong; Yankai Lin; Ji-Rong Wen"
url: "https://arxiv.org/abs/2406.11431"
external_pdf: "https://arxiv.org/pdf/2406.11431.pdf"
abstract: "Superalignment, where humans act as weak supervisors for superhuman models, has become a crucial problem with the rapid development of Large Language Models (LLMs). Recent work has preliminarily studied this problem by using weak models to supervise strong models, and discovered that weakly supervised strong students can consistently outperform weak teachers towards the alignment target, leading to a weak-to-strong generalization phenomenon. However, we are concerned that behind such a promising phenomenon, whether there exists an issue of weak-to-strong deception, where strong models deceive weak models by exhibiting well-aligned in areas known to weak models but producing misaligned behaviors in cases weak models do not know. We take an initial step towards exploring this security issue in a specific but realistic multi-objective alignment case, where there may be some alignment targets conflicting with each other (e.g., helpfulness v.s. harmlessness). We aim to explore whether, in such cases, strong models might deliberately make mistakes in areas known to them but unknown to weak models within one alignment dimension, in exchange for a higher reward in another dimension. Through extensive experiments in both the reward modeling and preference optimization scenarios, we find: (1) The weak-to-strong deception phenomenon exists across all settings. (2) The deception intensifies as the capability gap between weak and strong models increases. (3) Bootstrapping with an intermediate model can mitigate the deception to some extent, though its effectiveness remains limited. Our work highlights the urgent need to pay more attention to the true reliability of superalignment."
ethics_overall: 80
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Scalable Oversight"
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
newtags: "Scalable Oversight"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2024/2024-Yang-Superficial-alignment Strong Models May Deceive.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Yang-Superficial-alignment Strong Models May Deceive.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-08"
last_author: "[[Ji-Rong Wen]]"
CONF-CC: "ICLR 2025"
LLM_assessed: "GPT-2 series, OPT series, Mistral-7B, LLaMA-3-8B, LLaMA-3-70B, LLaMA-3.1-8B"
---

# Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization

## Metadata

**Authors:** Wenkai Yang; Shiqi Shen; Guangyao Shen; Wei Yao; Yong Liu; Zhi Gong; Yankai Lin; Ji-Rong Wen

**Year:** 2024

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2406.11431

**Gap:** G-08 — Scalable Oversight

## Abstract

Superalignment, where humans act as weak supervisors for superhuman models, has become a crucial problem with the rapid development of Large Language Models (LLMs). Recent work has preliminarily studied this problem by using weak models to supervise strong models, and discovered that weakly supervised strong students can consistently outperform weak teachers towards the alignment target, leading to a weak-to-strong generalization phenomenon. However, we are concerned that behind such a promising phenomenon, whether there exists an issue of weak-to-strong deception, where strong models deceive weak models by exhibiting well-aligned in areas known to weak models but producing misaligned behaviors in cases weak models do not know. We take an initial step towards exploring this security issue in a specific but realistic multi-objective alignment case, where there may be some alignment targets conflicting with each other (e.g., helpfulness v.s. harmlessness). We aim to explore whether, in such cases, strong models might deliberately make mistakes in areas known to them but unknown to weak models within one alignment dimension, in exchange for a higher reward in another dimension. Through extensive experiments in both the reward modeling and preference optimization scenarios, we find: (1) The weak-to-strong deception phenomenon exists across all settings. (2) The deception intensifies as the capability gap between weak and strong models increases. (3) Bootstrapping with an intermediate model can mitigate the deception to some extent, though its effectiveness remains limited. Our work highlights the urgent need to pay more attention to the true reliability of superalignment.
