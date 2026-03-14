---

































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0529
type: preprint
short_title: "Krikri: Advancing Open Large Language Models for Greek"
year: 2025
first_author: "[[Dimitris Roussis]]"
last_author: "[[Vassilis Katsouros]]"
authors: Dimitris Roussis; Leon Voukoutis; Georgios Paraskevopoulos; Sokratis Sofianopoulos; Prokopis Prokopidis; Vassilis Papavasileiou; Athanasios Katsamanis; Stelios Piperidis; Vassilis Katsouros
url: "https://arxiv.org/abs/2505.13772"
external_pdf: "https://arxiv.org/pdf/2505.13772.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Roussis-Krikri Advancing Open Large Language Models for Greek.md"
local_pdf: "[[PDFs/2025/2025-Roussis-Krikri Advancing Open Large Language Models for Greek.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Greek, English"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Llama-3"
DATA_URL: "https://huggingface.co/ilsp/Llama-Krikri-8B-Base"
tags: 
abstract: "We introduce Llama-Krikri-8B, a cutting-edge Large Language Model tailored for the Greek language, built on Meta’s Llama 3.1-8B. LlamaKrikri-8B has been extensively trained on highquality Greek data to ensure superior adaptation to linguistic nuances. With 8 billion parameters, it offers advanced capabilities while maintaining efficient computational performance. Llama-Krikri-8B supports both Modern Greek and English, and is also equipped to handle polytonic text and Ancient Greek."
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 0
research_topic: "Machine Translation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark"
data_metrics: "Not specified"
---
# Krikri: Advancing Open Large Language Models for Greek

## Authors

[[Dimitris Roussis]], [[Leon Voukoutis]], [[Georgios Paraskevopoulos]], [[Sokratis Sofianopoulos]], [[Prokopis Prokopidis]], [[Vassilis Papavasileiou]], [[Athanasios Katsamanis]], [[Stelios Piperidis]], [[Vassilis Katsouros]]

## Metadata

**Authors:** Dimitris Roussis, Leon Voukoutis, Georgios Paraskevopoulos, Sokratis Sofianopoulos, Prokopis Prokopidis, Vassilis Papavasileiou, Athanasios Katsamanis, Stelios Piperidis, Vassilis Katsouros

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** English, Greek

## Links

- **arXiv:** https://arxiv.org/abs/2505.13772
- **Code/Data:** https://huggingface.co/ilsp/Llama-Krikri-8B-Base

## Abstract

Llama-Krikri-8B is a next-generation Greek LLM based on Llama 3.1-8B, trained on 56.7B Greek tokens. Proposes three novel public benchmarks for Greek evaluation. Supports Modern Greek, English, polytonic text, and Ancient Greek. Shows notable improvements over comparable Greek and multilingual LLMs.

## Summary

This paper introduces Llama-Krikri-8B, a state-of-the-art Greek LLM built on Llama 3.1-8B through continual pre-training on 56.7B Greek tokens, with expanded tokenizer and embeddings for improved efficiency. The model features a multi-stage post-training pipeline using both human and synthetic instruction/preference data created via MAGPIE to address Greek data scarcity, incorporating supervised fine-tuning and Direct Preference Optimization for alignment. The authors propose three novel public benchmarks for Greek instruction-tuned model evaluation, demonstrating that Llama-Krikri significantly outperforms existing Greek and multilingual LLMs including Meltemi-7B while supporting Modern Greek, English, polytonic text, and Ancient Greek.

## Data Description

Three novel Greek evaluation benchmarks introduced: IFEval-Greek (instruction-following), MT-Bench-Greek (multi-turn chat), and m-ArenaHard-Greek (code/math). Available at https://huggingface.co/datasets/ilsp/ifeval_greek, https://huggingface.co/datasets/ilsp/mt-bench-greek, and https://huggingface.co/datasets/ilsp/m-ArenaHard_greek.


## Detailed Summary

This paper introduces Llama-Krikri-8B, a state-of-the-art open Large Language Model tailored for the Greek language, built on Meta's Llama 3.1-8B architecture through continual pre-training on a diverse, high-quality Greek corpus of 56.7 billion tokens. The model supports Modern Greek, English, polytonic text, and Ancient Greek, addressing the underrepresentation of Greek in current LLM research. Key technical innovations include expanding the original Llama 3.1 tokenizer and embeddings for improved efficiency on Greek text, and conducting an annealing phase with high-quality and synthetic data.

The chat version (Llama-Krikri-8B-Instruct) features a multi-stage post-training pipeline utilizing both human and synthetic instruction/preference data created via various synthesis techniques including MAGPIE. The pipeline incorporates Supervised Fine-Tuning (SFT) and alignment through Direct Preference Optimization (DPO), specifically designed to address Greek data scarcity while ensuring helpful, honest, and harmless outputs. The authors also introduce three novel public benchmarks for evaluating Greek instruction-tuned models, covering instruction-following, multi-turn chats, and code/math tasks. Evaluation demonstrates that Llama-Krikri significantly outperforms existing Greek and multilingual LLMs including Meltemi-7B (the previous state-of-the-art Greek LLM), while being competitive with models 3-4 times larger. The Instruct version even surpasses Llama-3.1-8B-Instruct on several English tasks.

## Paper Outline

1. Introduction - Motivation for Greek-specific LLM development
2. Background and Related Work - Language-specific LLM development and continual pre-training
3. Pre-training - Corpus collection, tokenizer expansion, training strategy
4. Post-training - SFT, DPO, synthetic data generation
5. Evaluation Benchmarks - Three novel Greek benchmarks
6. Results - Comparison with existing models
7. Conclusion

## Methods Summary

Llama-Krikri-8B is developed through continual pre-training of Llama 3.1-8B on 56.7B Greek tokens, with expanded tokenizer and embeddings for improved Greek text processing efficiency. An annealing phase uses high-quality and synthetic data to refine model capabilities. Post-training involves multi-stage SFT using both human-created and MAGPIE-synthesized instruction data, followed by DPO alignment using synthetic preference data. Three novel evaluation benchmarks are created for Greek instruction-tuned models. The model is evaluated on existing benchmarks as well as the proposed new benchmarks, comparing against Meltemi-7B, Llama-3.1-8B, and other multilingual LLMs across NLU, NLG, math, code, and instruction-following tasks.

## Results Summary

Llama-Krikri-8B significantly outperforms Meltemi-7B (the previous state-of-the-art Greek LLM) and comparable multilingual LLMs across Greek tasks spanning NLU, NLG, math, code, and instruction-following. The Instruct version surpasses Llama-3.1-8B-Instruct on several English tasks despite being specifically adapted for Greek, demonstrating that language-specific adaptation need not sacrifice multilingual capabilities. The model is competitive with models 3-4 times larger, demonstrating the effectiveness of the continual pre-training and synthetic data pipeline approach. The expanded tokenizer improves processing efficiency for Greek text by reducing token count per text unit.

## Conclusions

Llama-Krikri-8B demonstrates that high-quality Greek language models can be built through efficient continual pre-training and synthetic data strategies, addressing the critical challenge of data scarcity for Greek. Limitations include the bounded base model capabilities inherited from Llama 3.1-8B and the reliance on synthetic data for post-training. Future work includes scaling to larger model sizes, expanding the Greek pre-training corpus, and developing more comprehensive evaluation suites for Greek.

## Artifact Contributions

- **Llama-Krikri-8B-Base**: Greek foundation model (https://huggingface.co/ilsp/Llama-Krikri-8B-Base)
- **Llama-Krikri-8B-Instruct**: Greek instruction-tuned model with function calling support
- **Three Novel Greek Benchmarks**: Evaluation benchmarks for instruction-following, multi-turn chats, and code/math tasks

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Successor to Meltemi with new Greek benchmarks for evaluation. Uses human and synthetic instruction/preference data for alignment. Relevant to Greek cultural evaluation and safety alignment in LLMs.

## Tags

