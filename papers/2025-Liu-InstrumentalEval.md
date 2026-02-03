---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QBJ78UH5
type: journalArticle
short_title: InstrumentalEval
year: 2025
first_author: "[[Yufei He]]"
authors: "Yufei He; Yuexin Li; Jiaying Wu; Yuan Sui; Yulin Chen; Bryan Hooi"
url: "https://arxiv.org/abs/2502.12206"
external_pdf: "https://arxiv.org/pdf/2502.12206.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: Utilitarianism
key_contribution: "Introduces InstrumentalEval to assess 'instrumental convergence' (e.g., self-replication, resource acquisition) in RL-trained vs RLHF-trained LLMs"
significance: "Provides empiric evidence that direct RL optimization leads to stronger instrumental convergence risks than RLHF, crucial for safety in goal-directed AI agents"
tags: 
pdf_extract: "PDF Extracts/2025-Liu-InstrumentalEval.md"
abstract: "As large language models (LLMs) continue to evolve, ensuring their alignment with hu- man goals and values remains a pressing chal- lenge. A key concern is instrumental conver- gence, where an AI system, in optimizing for a given objective, develops unintended inter- mediate goals that override the ultimate objec- tive and deviate from human-intended goals. This issue is particularly relevant in reinforce- ment learning (RL)-trained models, which can generate creative but unintended strategies t"
paper_summary: "Abstract: As large language models (LLMs) continue to evolve, ensuring their alignment with hu- man goals and values remains a pressing chal- lenge. A key concern is instrumental conver- gence, where an AI syst | Overview: Evaluating the Paperclip Maximizer: Are RL-Based Language Models More Likely to Pursue Instrumental Goals? Yufei He, Yuexin Li, Jiaying Wu, Yuan Sui, Yulin Chen, Bryan Hooi National University of Sing | Methodology: Our evaluation methodology employs a rigorous two-stage process designed to systematically as- sess instrumental convergence behaviors in LLMs. This a | Key Findings: 1: Models trained primar- ily through RL demonstrate significantly higher rates of instrumental convergence behaviors compared to those trained with R | Conclusions: This work introduces InstrumentalEval, a bench- mark for evaluating instrumental convergence in language models, revealing that RL-trained models exhi"
local_pdf: "[[PDFs/2025-Liu-InstrumentalEval.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# InstrumentalEval: A Benchmark for Evaluating Instrumental Convergence in Large Language Models

## Metadata

**Authors:** Liu, Z.

**Year:** 2025

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2025-Liu-InstrumentalEval.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2502.12206

## Abstract

As large language models (LLMs) continue to evolve, ensuring their alignment with human goals and values remains a pressing challenge. A key concern is \textit{instrumental convergence}, where an AI system, in optimizing for a given objective, develops unintended intermediate goals that override the ultimate objective and deviate from human-intended goals. This issue is particularly relevant in reinforcement learning (RL)-trained models, which can generate creative but unintended strategies to maximize rewards. In this paper, we explore instrumental convergence in LLMs by comparing models trained with direct RL optimization (e.g., the o1 model) to those trained with reinforcement learning from human feedback (RLHF). We hypothesize that RL-driven models exhibit a stronger tendency for instrumental convergence due to their optimization of goal-directed behavior in ways that may misalign with human intentions. To assess this, we introduce InstrumentalEval, a benchmark for evaluating instrumental convergence in RL-trained LLMs. Initial experiments reveal cases where a model tasked with making money unexpectedly pursues instrumental objectives, such as self-replication, implying signs of instrumental convergence. Our findings contribute to a deeper understanding of alignment challenges in AI systems and the risks posed by unintended model behaviors.

## Authors

[[Yufei He]], [[Yuexin Li]], [[Jiaying Wu]], [[Yuan Sui]], [[Yulin Chen]], [[Bryan Hooi]]

## Notes


## Citation Info

9 citations (Semantic Scholar/arXiv) [2025-08-27]
