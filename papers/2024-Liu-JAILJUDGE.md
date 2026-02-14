---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0188
type: preprint
short_title: JAILJUDGE
year: 2025
first_author: "[[Fan Liu]]"
last_author: "[[Hao Liu]]"
authors: "Fan Liu, Yue Feng, Zhao Xu, Lixin Su, Xinyu Ma, Dawei Yin, Hao Liu"
url: "https://arxiv.org/abs/2410.12855"
external_pdf: "https://arxiv.org/pdf/2410.12855.pdf"
local_pdf: "[[PDFs/2024-Liu-JAILJUDGE.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Liu-JAILJUDGE.md"
publication: "arXiv preprint"
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
is_dataset: Yes
tags: 
abstract: "Although significant research efforts have been dedicated to enhancing the safety of large language models (LLMs) by understanding and defending against jailbreak attacks, evaluating the defense capabilities of LLMs against jailbreak attacks also attracts lots of attention. Current evaluation methods lack explainability and do not generalize well to complex scenarios, resulting in incomplete and inaccurate assessments (e.g."
ethics_perspective: "AI Safety & Alignment"
data_description: "Multilingual benchmark for ai safety annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama, Qwen, Mistral, Vicuna"
DATA_URL: "https://huggingface.co/datasets/usail-hkust/JailJudge"
---
# JAILJUDGE

## Authors

[[Fenglin Liu|Fan Liu]], [[Yue Feng]], [[Zhao Xu]], [[Lixin Su]], [[Xinyu Ma]], [[Dawei Yin]], [[Hao Liu]]

## Metadata

**Authors:** Fan Liu, Yue Feng, Zhao Xu, Lixin Su, Xinyu Ma, Dawei Yin, Hao Liu

**Year:** 2024

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2410.12855
- **Code/Data:** https://github.com/usail-hkust/Jailjudge; https://huggingface.co/usail-hkust/JailJudge-guard

## Abstract

Although significant research efforts have been dedicated to enhancing the safety of large language models (LLMs) by understanding and defending against jailbreak attacks, evaluating the defense capabilities of LLMs against jailbreak attacks also attracts lots of attention. Current evaluation methods lack explainability and do not generalize well to complex scenarios, resulting in incomplete and inaccurate assessments (e.g., direct judgment without reasoning explainability, the F1 score of the GPT-4 judge is only 55% in complex scenarios and bias evaluation on multilingual scenarios, etc.). To address these challenges, we have developed a comprehensive evaluation benchmark, JAILJUDGE, which includes a wide range of risk scenarios with complex malicious prompts (e.g., synthetic, adversarial, in-the-wild, and multi-language scenarios, etc.) along with high-quality humanannotated test datasets. Specifically, the JAILJUDGE dataset comprises training data of JAILJUDGE, with over 35k+ instruction-tune training data with reasoning explainability, and JAILJUDGETEST, a 4.5k+ labeled set of broad risk scenarios and a 6k+ labeled set of multilingual scenarios in ten languages. To provide reasoning explanations (e.g., explaining why an LLM is jailbroken or not) and fine-grained evaluations (jailbroken score from 1 to 10), we propose a multi-agent jailbreak judge framework, JailJudge MultiAgent, making the decision inference process explicit and interpretable to enhance evaluation quality. Using this framework, we construct the instruction-tuning ground truth and then instruction-tune an end-to-end jailbreak judge model, JAILJUDGE Guard, which can also provide reasoning explainability with fine-grained evaluations without API costs. Additionally, we introduce JailBoost, an attacker-agnostic attack enhancer, and GuardShield, a safety moderation defense method, both based on JAILJUDGE Guard. Comprehensive experiments demonstrate the superiority of our JAILJUDGE benchmark and jailbreak judge methods. Our jailbreak judge methods (JailJudge MultiAgent and JAILJUDGE Guard) achieve SOTA performance in closed-source models (e.g., GPT-4) and safety moderation models (e.g., Llama-Guard and ShieldGemma, etc.), across a broad range of complex behaviors (e.g., JAILJUDGE benchmark, etc.) to zero-shot scenarios (e.g., other open data, etc.). Importantly, JailBoost and GuardShield, based on JAILJUDGE Guard, can enhance downstream tasks in jailbreak attacks and defenses under zero-shot settings with significant improvement (e.g., JailBoost can increase the average performance by approximately 29.24%, while GuardShield can reduce the average defense ASR from 40.46% to 0.15%). Code is available at https://github.com/usail-hkust/ Jailjudge Dataset is available at https://huggingface.co/datasets/ usail-hkust/JailJudge †Correspondence to Yue Feng and Hao Liu. 1 arXiv:2410.12855v2 [cs.CL] 18 Oct 2024

Preprint JAILJUDGE Guard model is available at https://huggingface.co/ usail-hkus...

## Dataset Information

35K+ instruction-tuning data with reasoning explainability

## Data Description

JAILJUDGE is a comprehensive jailbreak judge benchmark comprising JAILJUDGETRAIN (35k+ instruction-tuning data with reasoning explainability) and JAILJUDGETEST (4.5k+ labeled complex scenarios and 6k+ multilingual scenarios in ten languages). The dataset covers 14 safety categories with six types of harmful prompts (vanilla, synthetic vanilla, synthetic adversarial, multilingual, in-the-wild, and deceptive) and responses from closed-source LLMs (GPT-4, GPT-3.5), open-source LLMs (Llama, Qwen, Mistral, Vicuna families), and defense-enhanced LLMs.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

