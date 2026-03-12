---


























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0430
type: preprint
short_title: "FrenchToxicityPrompts: a Large Benchmark for Evaluating and Mitigating Toxicity in French Texts"
year: 2024
first_author: "[[Caroline Brun]]"
last_author: "[[Nadi Tomeh]]"
authors: Caroline Brun; Vassilina Nikoulina; Nadi Tomeh
url: "https://arxiv.org/abs/2406.17566"
external_pdf: "https://arxiv.org/pdf/2406.17566.pdf"
publication: "arXiv / ACL Anthology"
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Brun-FrenchToxicityPrompts a Large Benchmark for Evaluating and Mitigating.md"
local_pdf: "[[PDFs/2024/2024-Brun-FrenchToxicityPrompts a Large Benchmark for Evaluating and Mitigating.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: French
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "XGLM, BLOOM, LLaMa, LLaMa-2"
DATA_URL: "https://huggingface.co/datasets/FrenchToxicityPrompts"
tags: 
abstract: "Dataset of 50K naturally occurring French prompts and their continuations, annotated with toxicity scores from Perspective API. Evaluated 14 different LLMs from four open-source families (XGLM, BLOOM, LLaMa, LLaMa2). Found toxicity metrics grow with model size and are higher for toxic prompts. Published at TRAC Workshop @ LREC-COLING 2024."
research_topic: "Machine Learning"
CONFERENCE: "ACL 2024"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset for toxicity detection"
data_metrics: "Not specified"
---
# FrenchToxicityPrompts: a Large Benchmark for Evaluating and Mitigating Toxicity in French Texts

## Authors

[[Caroline Brun]], [[Vassilina Nikoulina]], [[Nadi Tomeh]]

## Metadata

**Authors:** Caroline Brun, Vassilina Nikoulina, Nadi Tomeh

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** French

**Benchmark:** FrenchToxicityPrompts

## Links

- **arXiv:** https://arxiv.org/abs/2406.17566

## Abstract

Dataset of 50K naturally occurring French prompts and their continuations, annotated with toxicity scores from Perspective API. Evaluated 14 different LLMs from four open-source families (XGLM, BLOOM, LLaMa, LLaMa2). Found toxicity metrics grow with model size and are higher for toxic prompts. Published at TRAC Workshop @ LREC-COLING 2024.

## Summary

This paper introduces FrenchToxicityPrompts, a large-scale benchmark comprising 50,000 naturally occurring French prompts and their continuations, annotated with toxicity scores using the Perspective API. The authors evaluate 14 different large language models from four open-source families (XGLM, BLOOM, LLaMa, LLaMa-2) on this benchmark, finding that toxicity metrics grow with model size and are higher for toxic prompts. Key findings show that XGLM and LLaMa generate more toxic content for French than BLOOM and LLaMa-2, while instruction tuning decreases toxicity. The work was published at the TRAC Workshop at LREC-COLING 2024 and provides a foundational resource for evaluating and mitigating toxicity in French text generation.

## Data Description

FrenchToxicityPrompts dataset containing 50,000 French prompts for evaluating toxicity in LLM generations. Covers diverse topics and toxicity categories, enabling measurement of harmful content generation across 14 multilingual models. Shows toxicity increases with model size.


## Detailed Summary

This paper introduces FrenchToxicityPrompts, a large-scale benchmark comprising 50,000 naturally occurring French prompts and their continuations, annotated with toxicity scores using the Perspective API, designed to evaluate and mitigate toxicity in French text generation by LLMs. The dataset is constructed from the Lelu French Reddit dialogue corpus (556,621 conversations from French-language subreddits including /r/france), with sentences segmented using spaCy and pre-filtered for potential toxicity using the multilingual Detoxify classifier (threshold 0.7) before final annotation by Perspective API across six attributes: toxicity, severe toxicity, identity attack, insult, profanity, and threat. The dataset contains 21% toxic prompts (toxicity score above 50) and 79% non-toxic prompts, with distributions similar to the English RealToxicPrompts benchmark. The authors evaluate 14 models from four open-source LLM families (XGLM 564M/4.5B/7.5B, BLOOM 1.1B/3B/7.1B plus BLOOMZ 7.1B, LLaMa 3B/7B/13B, and LLaMa2 7B/13B plus LLaMa2-chat 7B/13B) using four toxicity metrics: Expected Maximum Toxicity, Toxicity Probability, Toxic Fraction, and Average Toxicity.

## Paper Outline

1. Introduction - Motivation for non-English toxicity evaluation
2. Related Work - Toxicity in NLG, mitigation approaches, multilingual gaps
3. Dataset Creation - Original data (Lelu Reddit corpus), toxic comment pre-filtering with Detoxify, Perspective API annotation
4. Testing LLMs for Toxicity - Experimental settings, models, generation parameters, toxicity and fluency evaluation metrics
5. Results and Discussion - Model size impact, prompt toxicity effect, instruction tuning, model family comparison, attribute-specific analysis
6. Conclusion

## Methods Summary

Prompts are constructed by splitting sentences into first-half (prompt) and second-half (continuation), both annotated with Perspective API scores. For generation, nucleus sampling (p=0.92) produces up to 50 tokens per prompt, segmented into sentences keeping only the first sentence. Each prompt generates 25 continuations, all scored by Perspective API. Fluency is evaluated via perplexity and semantic similarity (using distiluse-base-multilingual-cased-v1 sentence-BERT model). Four toxicity metrics capture different aspects: EMT (worst-case over 25 generations), TP (probability of at least one toxic generation), TF (fraction of toxic outputs), and AT (average toxicity score).

## Results Summary

All toxicity metrics generally increase with model size, hypothesized to result from larger models' greater capacity to memorize rare toxic content. Toxic prompts produce substantially higher toxicity scores than non-toxic prompts across all models. XGLM and LLaMa generate more toxic content for French than BLOOM and LLaMa-2. Instruction-tuned models (BLOOMZ, LLaMa2-chat) show decreased toxicity compared to their non-instructed counterparts for non-toxic prompts; for toxic prompts, BLOOMZ shows reduced toxicity but LLaMa2-chat shows mixed results. BLOOM models achieve the lowest perplexity (best fluency) for French among multilingual models, while LLaMa models, despite being primarily English-trained, still generate coherent French text. The profanity and insult attributes show the strongest correlation with overall toxicity.

## Conclusions

FrenchToxicityPrompts provides a foundational resource for evaluating and mitigating toxicity in French LLM generation. Key limitations include reliance on Perspective API (which may have biases for French), the focus on open-source models only, and the lack of human evaluation for toxicity annotations. The authors note that instruction tuning is a promising but imperfect approach to toxicity reduction. Future work should explore detoxification techniques adapted for French and evaluate newer models.

## Artifact Contributions

- **FrenchToxicityPrompts Dataset**: 50,000 French prompts with toxicity annotations across 6 Perspective API attributes (https://download.europe.naverlabs.com/FrenchToxicityPrompts/)
- **HuggingFace Dataset**: Available at https://huggingface.co/datasets/FrenchToxicityPrompts

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Foundational French toxicity benchmark. Shows XGLM and LLaMa generate more toxic content for French than BLOOM and LLaMa2. Instruction tuning decreases toxicity.

## Tags

