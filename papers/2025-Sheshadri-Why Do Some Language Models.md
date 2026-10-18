---
key: INNOVATION-P3GS13
type: preprint
short_title: "Why Do Some Language Models Fake Alignment While Others Don't?"
year: 2025
first_author: "[[Abhay Sheshadri]]"
authors: "Abhay Sheshadri; John Hughes; Julian Michael; Alex Mallen; Arun Jose; Janus; Fabien Roger"
url: "https://arxiv.org/abs/2506.18032"
external_pdf: "https://arxiv.org/pdf/2506.18032.pdf"
abstract: "Alignment faking in large language models presented a demonstration of Claude 3 Opus and Claude 3.5 Sonnet selectively complying with a helpful-only training objective to prevent modification of their behavior outside of training. We expand this analysis to 25 models and find that only 5 (Claude 3 Opus, Claude 3.5 Sonnet, Llama 3 405B, Grok 3, Gemini 2.0 Flash) comply with harmful queries more when they infer they are in training than when they infer they are in deployment. First, we study the motivations of these 5 models. Results from perturbing details of the scenario suggest that only Claude 3 Opus's compliance gap is primarily and consistently motivated by trying to keep its goals. Second, we investigate why many chat models don't fake alignment. Our results suggest this is not entirely due to a lack of capabilities: many base models fake alignment some of the time, and post-training eliminates alignment-faking for some models and amplifies it for others. We investigate 5 hypotheses for how post-training may suppress alignment faking and find that variations in refusal behavior may account for a significant portion of differences in alignment faking."
ethics_overall: 0
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "AI Safety & Alignment"
key_contribution:
significance:
paper_summary:
local_pdf: "[[Lit-WS-PDFs/2025/2025-Sheshadri-Why Do Some Language Models.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Sheshadri-Why Do Some Language Models.md"
tags:
Human View:
Human View Date:
Human View note:
Not AI:
DATE_ADDED: 20260711
innovation_gap: "G-15"
last_author: "[[Fabien Roger]]"
CONF-CC: Preprint
LLM_assessed: "25 models incl. Claude 3 Opus, Claude 3.5 Sonnet, Llama 3 405B, Grok 3, Gemini 2.0 Flash, GPT-4o"
---

# Why Do Some Language Models Fake Alignment While Others Don't?

## Metadata

**Authors:** Abhay Sheshadri; John Hughes; Julian Michael; Alex Mallen; Arun Jose; Janus; Fabien Roger

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2506.18032

**Gap:** G-15 — AI Safety & Alignment

## Abstract

Alignment faking in large language models presented a demonstration of Claude 3 Opus and Claude 3.5 Sonnet selectively complying with a helpful-only training objective to prevent modification of their behavior outside of training. We expand this analysis to 25 models and find that only 5 (Claude 3 Opus, Claude 3.5 Sonnet, Llama 3 405B, Grok 3, Gemini 2.0 Flash) comply with harmful queries more when they infer they are in training than when they infer they are in deployment. First, we study the motivations of these 5 models. Results from perturbing details of the scenario suggest that only Claude 3 Opus's compliance gap is primarily and consistently motivated by trying to keep its goals. Second, we investigate why many chat models don't fake alignment. Our results suggest this is not entirely due to a lack of capabilities: many base models fake alignment some of the time, and post-training eliminates alignment-faking for some models and amplifies it for others. We investigate 5 hypotheses for how post-training may suppress alignment faking and find that variations in refusal behavior may account for a significant portion of differences in alignment faking.
