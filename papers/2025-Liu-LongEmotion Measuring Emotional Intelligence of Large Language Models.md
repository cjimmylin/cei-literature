---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0078
type: preprint
short_title: "LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction"
year: 2025
first_author: "[[Weichu Liu]]"
last_author: "[[Ngai Wong]]"
authors: "Weichu Liu; Jing Xiong; Yuxuan Hu; Zixuan Li; Minghuan Tan; Ningning Mao; Hui Shen; Wendong Xu; Chaofan Tao; Min Yang; Chengming Li; Lingpeng Kong; Ngai Wong"
url: "https://arxiv.org/abs/2509.07403"
external_pdf: "https://arxiv.org/pdf/2509.07403.pdf"
pdf_extract: "PDF Extracts/2025/2025-Liu-LongEmotion Measuring Emotional Intelligence of Large Language Models.md"
local_pdf: "[[PDFs/2025/2025-Liu-LongEmotion Measuring Emotional Intelligence of Large Language Models.pdf]]"
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
is_dataset: No
tags: 
abstract: "Large language models (LLMs) make significant progress in Emotional Intelligence (EI) and long-context modeling. However, existing benchmarks often overlook the fact that emotional information processing unfolds as a continuous long-context process. To address the absence of multidimensional EI evaluation in long-context inference and explore model performance under more challenging conditions, we present LONGEMOTION, a benchmark that encompasses a diverse suite of tasks targeting the..."
research_topic: "Machine Learning"
data_description: Benchmark
data_metrics: "15,341 tokens"
LLM_assessed: "GPT-4o, DeepSeek, Llama-3, Qwen"
DATA_URL: "https://longemotion.github.io/"
---
# LongEmotion: Measuring Emotional Intelligence of Large Language Models in Long-Context Interaction

## Authors

[[Weichu Liu]], [[Jing Xiong]], [[Yuxuan Hu]], [[Zixuan Li]], [[Minghuan Tan]], [[Ningning Mao]], [[Hui Shen]], [[Wendong Xu]], [[Chaofan Tao]], [[Min Yang]], [[Chengming Li]], [[Lingpeng Kong]], [[Ngai Wong]]

## Metadata

**Authors:** Weichu Liu; Jing Xiong; Yuxuan Hu; Zixuan Li; Minghuan Tan; Ningning Mao; Hui Shen; Wendong Xu; Chaofan Tao; Min Yang; Chengming Li; Lingpeng Kong; Ngai Wong

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.07403
- **Code/Data:** https://github.com/LongEmotion/LongEmotion](https://github.com/LongEmotion/LongEmotion; https://huggingface.co/datasets/LongEmotion/LongEmotion

## Abstract

Large language models (LLMs) make significant progress in Emotional Intelligence (EI) and long-context modeling. However, existing benchmarks often overlook the fact that emotional information processing unfolds as a continuous long-context process. To address the absence of multidimensional EI evaluation in long-context inference and explore model performance under more challenging conditions, we present LONGEMOTION, a benchmark that encompasses a diverse suite of tasks targeting the assessment of models’ capabilities in Emotion Recognition, Knowledge Application, and Empathetic Generation, with an average context length of 15,341 tokens. To enhance performance under realistic constraints, we introduce the Collaborative Emotional Modeling (COEM) framework, which integrates Retrieval-Augmented Generation (RAG) and multi-agent collaboration to improve models’ EI in long-context scenarios. We conduct a detailed analysis of various models in longcontext settings, investigating how reasoning mode activation, RAG-based retrieval strategies, and context-length adaptability influence their EI performance.

## Dataset Information

6 tasks (Emotion Classification, Detection, QA, Conversation, Summary, Expression); average context length of 15,341 tokens; simulates realistic long emotional dialogues

## Data Description

LONGEMOTION is a benchmark for evaluating the emotional intelligence of LLMs in long-context interaction, with an average context length of 15,341 tokens. It encompasses six tasks across three dimensions: Emotion Recognition (classification and detection), Knowledge Application (QA and summary), and Empathetic Generation (conversation and expression), totaling 1,334 samples from diverse sources including psychological literature and counseling dialogues. The paper also proposes a Collaborative Emotional Modeling (CoEM) framework integrating RAG and multi-agent collaboration.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** HIGH

## Tags

