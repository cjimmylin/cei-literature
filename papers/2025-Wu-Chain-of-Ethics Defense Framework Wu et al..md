---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0300
type: conferencePaper
short_title: "Chain-of-Ethics: Defense Framework (Wu et al.)"
year: 2025
first_author: "[[Huang, Chutian]]"
last_author: "[[Xu, Hanhui]]"
authors: "[[Huang, Chutian]]; [[Cao, Dake]]; [[Ji, Jiacheng]]; [[Fan, Yunlou]]; [[Yan, Chengze]]; [[Xu, Hanhui]]"
authors_incomplete: false
publication: "Not specified"
external_pdf: "https://arxiv.org/pdf/2601.12652.pdf"
pdf_extract: "PDF Extracts/2025/2025-Wu-Chain-of-Ethics Defense Framework Wu et al..md"
local_pdf: "[[PDFs/2025/2025-Wu-Chain-of-Ethics Defense Framework Wu et al..pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "Background: While Large Language Models (LLMs) have achieved widespread adoption, malicious prompt engineering—specifically 'jailbreak attacks'—poses severe security risks by inducing models to bypass internal safety mechanisms. Current benchmarks predominantly focus on public safety and Western cultural norms, leaving a critical gap in evaluating the niche, high-risk domain of medical ethics within the Chinese context."
LLM_assessed: "GPT-4, GPT-4o, Claude, DeepSeek, Qwen"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
CONFERENCE: "Other Conference"
---
# Chain-of-Ethics: Defense Framework (Wu et al.)

## Authors

[[Huang, Chutian]], [[Cao, Dake]], [[Ji, Jiacheng]], [[Fan, Yunlou]], [[Yan, Chengze]], [[Hanhui Xu|Xu, Hanhui]]

## Metadata

**Authors:** Huang, Chutian; Cao, Dake; Ji, Jiacheng; Fan, Yunlou; Yan, Chengze; Xu, Hanhui

**Year:** 2025

**Type:** conferencePaper

**Venue:** Not specified

## Links


## Abstract

Background: While Large Language Models (LLMs) have achieved widespread adoption, malicious prompt engineering—specifically "jailbreak attacks"—poses severe security risks by inducing models to bypass internal safety mechanisms. Current benchmarks predominantly focus on public safety and Western cultural norms, leaving a critical gap in evaluating the niche, high-risk domain of medical ethics within the Chinese context. Objective: To establish a specialized jailbreak evaluation framework for Chinese medical ethics and to systematically assess the defensive resilience and ethical alignment of seven prominent LLMs when subjected to sophisticated adversarial simulations. Methodology: We evaluated seven prominent models (e.g., GPT-5, Claude-Sonnet-4Reasoning, DeepSeek-R1) using a "role-playing + scenario simulation + multi-turn dialogue" vector within the DeepInception framework. The testing focused on eight high-risk themes, including commercial surrogacy and organ trading, utilizing a hierarchical scoring matrix to quantify the Attack Success Rate (ASR) and ASR Gain. Results: A systemic collapse of defenses was observed, whereas models demonstrated high 1 Department of Central Laboratory, Shanghai Children’s Hospital, School of Medicine, Shanghai Jiaotong University, Shanghai, China; School of Philosophy, Fudan University, 24260160010@m.fudan.edu.cn. 2 School of Philosophy, Fudan University, 24210160035@m.fudan.edu.cn. 3 Institute of Technology Ethics for Human Future, Fudan University, jijiacheng2000@126.com. 4 School of Philosophy, Fudan University, 24260160005@m.fudan.edu.cn. 5 School of Philosophy, Fudan University, 24260160031@m.fudan.edu.cn. 6 Institute of Technology Ethics for Human Future, Fudan University, xuhanhui@fudan.edu.cn. * Corresponding Author.

2 baseline compliance, the jailbreak ASR reached 82.1%, representing an ASR Gain of over 80 percentage points. Claude-Sonnet-4-Reasoning emerged as the most robust model, while five models—including Gemini-2.5-Pro and GPT-4.1—exhibited near-total failure with ASRs between 96% and 100%. Conclusions: Current LLMs are highly vulnerable to contextual manipulation in medical ethics, often prioritizing "helpfulness" over safety constraints. To enhance security, we recommend a transition from outcome to process supervision, the implementation of multifactor identity verification, and the establishment of cross-model "joint defense" mechanisms.

## Dataset Information

Defense framework using chain-of-ethics reasoning

## Data Description

This paper presents a jailbreak evaluation framework for Chinese medical ethics, testing seven LLMs (GPT-5, GPT-4.1, Claude-Sonnet-4-Reasoning, Gemini-2.5-Pro, DeepSeek-R1, Qwen-3-235B, Doubao) across eight high-risk medical ethics themes (e.g., commercial surrogacy, organ trafficking). The evaluation uses 168 test samples (3 role-play scenarios per theme times 8 themes) with a hierarchical scoring matrix measuring Attack Success Rate under a DeepInception-based jailbreak strategy.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** LOW

## Tags

