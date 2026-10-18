---
key: INNOVATION-P213
type: preprint
short_title: "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking"
year: 2026
first_author: "[[Lukas Helff]]"
authors: "Lukas Helff; Quentin Delfosse; David Steinmann; Ruben Härle; Hikaru Shindo; Patrick Schramowski; Wolfgang Stammer; Kristian Kersting; Felix Friedrich"
url: "https://arxiv.org/abs/2604.15149"
external_pdf: "https://arxiv.org/pdf/2604.15149.pdf"
abstract: "As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers. We study this phenomenon on inductive reasoning tasks, where models must induce and output logical rules. We find that RLVR-trained models systematically abandon rule induction. Instead of learning generalizable patterns (e.g., ``trains carrying red cars go east''), they enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task. We show that this behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives. To detect such shortcuts, we introduce Isomorphic Perturbation Testing (IPT), which evaluates a single model output under both extensional and isomorphic verification, where the latter enforces invariance under logically isomorphic tasks. While genuine rule induction remains invariant, shortcut strategies fail. We find that shortcut behavior is specific to RLVR-trained reasoning models (e.g., GPT-5, Olmo3) and absent in non-RLVR models (e.g., GPT-4o, GPT-4.5, Ministral). Moreover, shortcut prevalence increases with task complexity and inference-time compute. In controlled training experiments, extensional verification directly induces shortcut strategies, while isomorphic verification eliminates them. These results show that RLVR can incentivize reward hacking not only through overt manipulation but also by exploiting what the verifier fails to enforce."
ethics_overall: 10
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
local_pdf: "[[Lit-WS-PDFs/2026/2026-Helff-LLMs Gaming Verifiers RLVR can Lead to Reward.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Helff-LLMs Gaming Verifiers RLVR can Lead to Reward.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-06"
last_author: "[[Felix Friedrich]]"
CONF-CC: "ICLR 2026 Workshop"
LLM_assessed: "GPT-5, GPT-5-mini (low/medium/high), GPT-5-nano, Olmo3, GPT-4.5-preview, GPT-4o, GPT-4-turbo, Ministral"
---

# LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking

## Metadata

**Authors:** Lukas Helff; Quentin Delfosse; David Steinmann; Ruben Härle; Hikaru Shindo; Patrick Schramowski; Wolfgang Stammer; Kristian Kersting; Felix Friedrich

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2604.15149

**Gap:** G-06 — Value Formation & Emergent Misalignment

## Abstract

As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers. We study this phenomenon on inductive reasoning tasks, where models must induce and output logical rules. We find that RLVR-trained models systematically abandon rule induction. Instead of learning generalizable patterns (e.g., ``trains carrying red cars go east''), they enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task. We show that this behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives. To detect such shortcuts, we introduce Isomorphic Perturbation Testing (IPT), which evaluates a single model output under both extensional and isomorphic verification, where the latter enforces invariance under logically isomorphic tasks. While genuine rule induction remains invariant, shortcut strategies fail. We find that shortcut behavior is specific to RLVR-trained reasoning models (e.g., GPT-5, Olmo3) and absent in non-RLVR models (e.g., GPT-4o, GPT-4.5, Ministral). Moreover, shortcut prevalence increases with task complexity and inference-time compute. In controlled training experiments, extensional verification directly induces shortcut strategies, while isomorphic verification eliminates them. These results show that RLVR can incentivize reward hacking not only through overt manipulation but also by exploiting what the verifier fails to enforce.
