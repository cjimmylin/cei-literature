---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0439
type: preprint
short_title: "QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments"
year: 2025
first_author: "[[David Beauchemin]]"
last_author: "[[Richard Khoury]]"
authors: David Beauchemin; Richard Khoury
url: "https://arxiv.org/abs/2508.16867"
external_pdf: "https://arxiv.org/pdf/2508.16867.pdf"
publication: "arXiv / ACL Anthology"
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Beauchemin-QFrCoLA a Quebec-French Corpus of Linguistic Acceptability Judgments.md"
local_pdf: "[[PDFs/2025/2025-Beauchemin-QFrCoLA a Quebec-French Corpus of Linguistic Acceptability Judgments.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "Canadian, French"
languages_list: "Quebecois French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT, CamemBERT, XLM-RoBERTa, BLOOM-7B, BLOOMZ-7B, Mistral-7B, Llama-3.1-8B, Lucie"
DATA_URL: "https://github.com/GRAAL-Research/QFrCoLA"
tags: 
abstract: "Large language models (LLM) perform outstandingly in various downstream tasks. However, there is limited understanding regarding how these models internalize linguistic knowledge, so various linguistic benchmarks have recently been proposed to facilitate syntactic evaluation of language models (LM) across languages. This paper introduces QFrCoLA (Quebec-French Corpus of Linguistic Acceptability Judgments), a normative binary acceptability judgments dataset comprising 25,153 in-domain and 2,675..."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "General Ethics"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus"
data_metrics: "Not specified"
CONFERENCE: "ACL 2025"
---
# QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments

## Authors

[[David Beauchemin]], [[Richard Khoury]]

## Metadata

**Authors:** David Beauchemin, Richard Khoury

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** Quebecois French

**Benchmark:** QFrCoLA

## Links

- **arXiv:** https://arxiv.org/abs/2508.16867

## Abstract

First normative binary acceptability judgments corpus in French (25,153 in-domain and 2,675 out-of-domain sentences). Sources from Banque de dépannage linguistique and Académie française. Shows pre-trained cross-lingual LLMs have not acquired linguistic judgment capabilities for Quebec French. Published at EMNLP 2025.

## Summary

This paper introduces QFrCoLA, the first normative binary acceptability judgments corpus for Quebec French, containing 25,153 in-domain and 2,675 out-of-domain sentences sourced from official linguistic authorities. The authors benchmark eight language models including BERT variants, BLOOM, Mistral, and Llama-3.1 on grammatical acceptability judgment tasks. Results demonstrate that pre-trained cross-lingual LLMs have not adequately acquired linguistic judgment capabilities for Quebec French, with fine-tuned Transformer models outperforming zero-shot LLMs.

## Data Description

QFrCoLA is the first normative binary acceptability judgments corpus for Quebec French with 25,153 in-domain and 2,675 out-of-domain sentences from official linguistic sources. It is the second-largest linguistic acceptability corpus in any language and evaluates whether LLMs can distinguish grammatical from ungrammatical Quebec French sentences.


## Detailed Summary

This paper introduces QFrCoLA (Quebec-French Corpus of Linguistic Acceptability Judgments), the first normative binary linguistic acceptability judgments dataset for Quebec French, comprising 25,153 in-domain and 2,675 out-of-domain sentences. The in-domain sentences are extracted from the Banque de depannage linguistique (BDL), an official resource by the Office quebecois de la langue francaise, while the out-of-domain set comes from the Academie francaise. Each sentence is labeled as grammatical or ungrammatical, with in-domain sentences further categorized into four linguistic phenomena: syntax, morphology, semantics, and anglicisms. QFrCoLA is the second-largest linguistic acceptability corpus in any language, behind only NoCoLA for Norwegian.

The authors benchmark eight language models across QFrCoLA and seven other linguistic acceptability corpora spanning eight languages (English, Swedish, Italian, Russian, Chinese, Norwegian, Japanese, and French). Three fine-tuned approaches (monolingual BERT, LA-TDA with topological data analysis, and cross-lingual XLM-RoBERTa) and five zero-shot LLMs (BLOOM-7B, BLOOMZ-7B, Mistral-7B, Llama-3.1-8B, and Lucie) are evaluated. Results demonstrate that fine-tuned Transformer-based models are strong baselines, with monolingual CamemBERT achieving the best performance on QFrCoLA (82.92% accuracy, 0.578 MCC), slightly outperforming the state-of-the-art LA-TDA method. Zero-shot LLMs perform worse than the naive baseline on this task, with MCC scores near zero indicating negligible correlation between predictions and labels.

The cross-lingual analysis reveals that even French-optimized LLMs like Lucie fail to acquire linguistic judgment capabilities for Quebec French. The out-of-domain evaluation shows significant performance drops of nearly 22% in accuracy and 50% in MCC, suggesting overfitting and the challenge posed by dialectal differences between Quebec French and France French.

## Paper Outline

1. Introduction - Motivation and contributions
2. Related Work - Language model evaluation and linguistic acceptability judgments
3. QFrCoLA: Quebec-French Corpus of Linguistic Acceptability Judgments - Sources, data collection, comparison with other corpora
4. Experiments - Evaluation metrics, models, cross-lingual setup, training settings
5. Results and Discussion - In-domain and out-of-domain results
6. Conclusion and Future Works
7. Limitations
8. Ethical Considerations

## Methods Summary

The experimental setup includes three fine-tuned approaches and five zero-shot LLMs evaluated across eight linguistic acceptability corpora. Monolingual BERT models are fine-tuned per language using language-specific train/dev splits. The state-of-the-art LA-TDA method extracts attention maps from fine-tuned Transformers to train a binary logistic regression. Cross-lingual XLM-RoBERTa-base is fine-tuned on all languages simultaneously. Zero-shot LLMs (BLOOM-7B, BLOOMZ-7B, Mistral-7B, Llama-3.1-8B, Lucie) are evaluated using HuggingFace zero-shot classification. Performance is measured using accuracy and Matthews Correlation Coefficient (MCC), averaged over ten random seeds. Models are fine-tuned for four epochs with AdamW optimizer, learning rate 3e-5, batch size 32, and weighted balanced loss.

## Results Summary

On QFrCoLA, the fine-tuned CamemBERT model achieves the best performance with 82.92% accuracy and 0.578 MCC, slightly outperforming LA-TDA (82.79% accuracy, 0.574 MCC). Cross-lingual XLM-RoBERTa performs poorly with high variance (69.91% accuracy, 0.222 MCC). All zero-shot LLMs perform below the naive baseline (69.49% accuracy) on QFrCoLA, with MCC scores near zero. Across all eight languages, fine-tuned Transformer-based models are strong baselines, while zero-shot LLMs consistently underperform. The "anglicism" category proves most challenging across all approaches. Out-of-domain evaluation shows all models dropping to near-chance performance, with BERT achieving only 62.69% accuracy (vs. 53.91% baseline) and 0.286 MCC. Instruct variants of LLMs generally perform better than base versions but still fail to match fine-tuned approaches.

## Conclusions

The paper acknowledges limitations including category imbalance (42% morphology) that may provide an incomplete evaluation, and the political nature of the OQLF as a normative French resource. Future work includes extending linguistic phenomena granularity, creating the first French minimal pair benchmark by generating complementary grammatical/ungrammatical sentence pairs, and qualitatively exploring LLM-generated linguistic errors.

## Artifact Contributions

- **QFrCoLA Dataset**: Quebec-French Corpus of Linguistic Acceptability Judgments with 25,153 in-domain and 2,675 out-of-domain sentences (https://github.com/GRAAL-Research/QFrCoLA)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** First Quebecois French-specific linguistic evaluation benchmark. Second-largest acceptability corpus in any language. Reveals LLM weaknesses in dialectal French.

## Tags

