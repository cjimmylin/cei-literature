---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TJNSRVFL
type: journalArticle
short_title: "How to Catch an AI Liar"
year: 2025
first_author: "[[Lorenzo Pacchiardi]]"
last_author: "[[Jan Brauner]]"
authors: "Lorenzo Pacchiardi; Alex J. Chan; Sören Mindermann; Ilan Moscovitz; Alexa Y. Pan; Yarin Gal; Owain Evans; Jan Brauner"
url: "https://arxiv.org/abs/2309.15840"
external_pdf: "https://arxiv.org/pdf/2309.15840.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2023/2023-Tan-How to Catch an AI Liar.md"
abstract: "Large language models (LLMs) can “lie”, which we define as outputting false statements despite “knowing” the truth in a demonstrable sense. LLMs might “lie”, for example, when instructed to output misinformation. Here, we develop a simple lie detector that requires neither access to the LLM’s activations (black-box) nor ground-truth knowledge of the fact in question. The detector works by asking a predefined set of unrelated follow-up questions after a suspected lie, and feeding the LLM’s..."
paper_summary: "Abstract: Large language models (LLMs) can 'lie', which we define as outputting false statements despite 'knowing' the truth in a demonstrable sense. LLMs might 'lie', for example, when instructed to output mis | Overview: HOW TO CATCH AN AI LIAR: LIE DETECTION IN BLACK-BOX LLMS BY ASKING UNRELATED QUESTIONS Lorenzo Pacchiardi∗ University of Oxford Alex J. Chan∗ University of Cambridge Sören Mindermann University of Oxf | Methodology: (fine-tuning). We create several versions of each model by varying the fine-tuning setup (Ap- pendix B.1). The lie detector effectively sep- arates tr | Key Findings: also raises interesting questions about yet-to-be-understood inductive biases in LLMs. 2 MOTIVATION: WHY AND HOW TO STUDY LIE DETECTION IN LLMS? Lying | Conclusions: Our simple elicitation question method generalises to unseen topics, models, and lie-generation techniques. Combined with the many promising direction"
local_pdf: "[[PDFs/2023/2023-Tan-How to Catch an AI Liar.pdf]]"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-3, Llama, Alpaca, Vicuna"
DATA_URL: "https://github.com/LoryPack/LLM-LieDetector"
---
# How to Catch an AI Liar: Lie-Detection in Large Language Models

## Metadata

**Authors:** Tan, Z.; Chan, C.; Brahman, F.; Sclar, M.; Jiang, Z.

**Year:** 2023

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2023/2023-Tan-How to Catch an AI Liar.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2309.15840

## Abstract

Large language models (LLMs) can "lie", which we define as outputting false statements despite "knowing" the truth in a demonstrable sense. LLMs might "lie", for example, when instructed to output misinformation. Here, we develop a simple lie detector that requires neither access to the LLM's activations (black-box) nor ground-truth knowledge of the fact in question. The detector works by asking a predefined set of unrelated follow-up questions after a suspected lie, and feeding the LLM's yes/no answers into a logistic regression classifier. Despite its simplicity, this lie detector is highly accurate and surprisingly general. When trained on examples from a single setting -- prompting GPT-3.5 to lie about factual questions -- the detector generalises out-of-distribution to (1) other LLM architectures, (2) LLMs fine-tuned to lie, (3) sycophantic lies, and (4) lies emerging in real-life scenarios such as sales. These results indicate that LLMs have distinctive lie-related behavioural patterns, consistent across architectures and contexts, which could enable general-purpose lie detection.

## Authors

[[Lorenzo Pacchiardi]], [[Jun Shern Chan|Alex J. Chan]], [[Sören Mindermann]], [[Ilan Moscovitz]], [[Alexander Pan|Alexa Y. Pan]], [[Yarin Gal]], [[Owain Evans]], [[Jan Brauner]]

## Data Description

The paper develops a black-box lie detector for LLMs using a question-answering dataset of over 20,000 questions spanning general knowledge, mathematics, common sense reasoning, translations, and self-knowledge. The detector is trained on 2,560 lie/truth samples from prompted GPT-3.5 (text-davinci-003) and tested for generalization across GPT-3 (davinci), LLaMA-30B, LLaMA-7B, Alpaca-7B, and Vicuna-7B using various lie generation methods including prompting, chain-of-thought, and fine-tuning.


## Notes


## Citation Info

68 citations (Semantic Scholar/arXiv) [2025-08-27]
