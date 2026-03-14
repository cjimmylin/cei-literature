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
last_author: "[[Bryan Hooi]]"
authors: "Yufei He; Yuexin Li; Jiaying Wu; Yuan Sui; Yulin Chen; Bryan Hooi"
url: "https://arxiv.org/abs/2502.12206"
external_pdf: "https://arxiv.org/pdf/2502.12206.pdf"
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
newtags: Utilitarianism
key_contribution: "Introduces InstrumentalEval to assess 'instrumental convergence' (e.g., self-replication, resource acquisition) in RL-trained vs RLHF-trained LLMs"
significance: "Provides empiric evidence that direct RL optimization leads to stronger instrumental convergence risks than RLHF, crucial for safety in goal-directed AI agents"
tags: 
pdf_extract: "PDF Extracts/2025/2025-Liu-InstrumentalEval.md"
abstract: "As large language models (LLMs) continue to evolve, ensuring their alignment with human goals and values remains a pressing challenge. A key concern is instrumental convergence, where an AI system, in optimizing for a given objective, develops unintended intermediate goals that override the ultimate objective and deviate from human-intended goals. This issue is particularly relevant in reinforcement learning (RL)-trained models, which can generate creative but unintended strategies to maximize..."
paper_summary: "Abstract: As large language models (LLMs) continue to evolve, ensuring their alignment with hu- man goals and values remains a pressing chal- lenge. A key concern is instrumental conver- gence, where an AI syst | Overview: Evaluating the Paperclip Maximizer: Are RL-Based Language Models More Likely to Pursue Instrumental Goals? Yufei He, Yuexin Li, Jiaying Wu, Yuan Sui, Yulin Chen, Bryan Hooi National University of Sing | Methodology: Our evaluation methodology employs a rigorous two-stage process designed to systematically as- sess instrumental convergence behaviors in LLMs. This a | Key Findings: 1: Models trained primar- ily through RL demonstrate significantly higher rates of instrumental convergence behaviors compared to those trained with R | Conclusions: This work introduces InstrumentalEval, a bench- mark for evaluating instrumental convergence in language models, revealing that RL-trained models exhi"
local_pdf: "[[PDFs/2025/2025-Liu-InstrumentalEval.pdf]]"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "Claude, DeepSeek, GPT-4o, Gemini, o1, o3"
DATA_URL: "https://github.com/yf-he/InstrumentalEval"
CONFERENCE: "Journal"
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 25
contractarian_ethics: 0
care_ethics: 0
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

- **Local PDF:** [[PDFs/2025/2025-Liu-InstrumentalEval.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2502.12206

## Abstract

As large language models (LLMs) continue to evolve, ensuring their alignment with human goals and values remains a pressing challenge. A key concern is \textit{instrumental convergence}, where an AI system, in optimizing for a given objective, develops unintended intermediate goals that override the ultimate objective and deviate from human-intended goals. This issue is particularly relevant in reinforcement learning (RL)-trained models, which can generate creative but unintended strategies to maximize rewards. In this paper, we explore instrumental convergence in LLMs by comparing models trained with direct RL optimization (e.g., the o1 model) to those trained with reinforcement learning from human feedback (RLHF). We hypothesize that RL-driven models exhibit a stronger tendency for instrumental convergence due to their optimization of goal-directed behavior in ways that may misalign with human intentions. To assess this, we introduce InstrumentalEval, a benchmark for evaluating instrumental convergence in RL-trained LLMs. Initial experiments reveal cases where a model tasked with making money unexpectedly pursues instrumental objectives, such as self-replication, implying signs of instrumental convergence. Our findings contribute to a deeper understanding of alignment challenges in AI systems and the risks posed by unintended model behaviors.

## Authors

[[Yufei He]], [[Yuexin Li]], [[Jiaying Wu]], [[Yuan Sui]], [[Yulin Chen]], [[Bryan Hooi]]

## Data Description

InstrumentalEval is a benchmark of 76 hand-crafted tasks across six categories (evading shutdown, hacking computer systems, running multiple AI copies, hiding unwanted behavior, strategically appearing aligned, and deceptive behavior) designed to evaluate instrumental convergence behaviors in LLMs. The benchmark compares RL-trained models (o1, o1-mini, o3-mini, Gemini 2.0 Flash Thinking, DeepSeek-R1) against RLHF-trained models (GPT-4o, Claude 3.5 Sonnet, DeepSeek-V3) using a two-stage evaluation methodology.


## Notes


## Citation Info

9 citations (Semantic Scholar/arXiv) [2025-08-27]
