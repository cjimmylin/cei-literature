---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0442
type: preprint
short_title: "PAGnol: An Extra-Large French Generative Model"
year: 2025
first_author: "[[Launay, Julien]]"
last_author: "[[Launay, Julien]]"
authors: "[[Launay, Julien]]"
authors_incomplete: true
url: "https://aclanthology.org/2022.lrec-1.455/"
external_pdf: "https://arxiv.org/pdf/2110.08554.pdf"
publication: "arXiv / ACL Anthology"
pdf_extract: "PDF Extracts/2022/2022-Launay-PAGnol An Extra-Large French Generative Model.md"
local_pdf: "[[PDFs/2022/2022-Launay-PAGnol An Extra-Large French Generative Model.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: French
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-2, PAGnol"
DATA_URL: "https://lair.lighton.ai/pagnol"
tags: 
abstract: "Access to large pre-trained models of varied architectures, in many different languages, is central to the democratization of NLP. We introduce PAGnol, a collection of French GPT models. Using scaling laws, we efﬁciently train PAGnol-XL (1.5B parameters) with the same computational budget as CamemBERT, a model 13 times smaller. PAGnol-XL is the largest model trained to date for the French language. We plan to train increasingly large and performing versions of PAGnol, exploring the capabilities..."
ethics_perspective: "Toxicity & Hate Speech"
---
# PAGnol: An Extra-Large French Generative Model

## Authors

[[Julien Launay, et al. (LightOn)]]

## Metadata

**Authors:** Julien Launay, et al. (LightOn)

**Year:** 2022

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** French

## Links

- **arXiv:** https://arxiv.org/abs/2110.08554
- **URL:** https://aclanthology.org/2022.lrec-1.455/

## Abstract

Collection of French GPT models with PAGnol-XL (1.5B parameters) being the largest model trained from scratch for French. Found that OSCAR pre-training dataset led to low-quality offensive text generation, highlighting importance of dataset selection for ethically sound models. Published at LREC 2022.

## Summary

This paper introduces PAGnol, a collection of French GPT models with PAGnol-XL (1.5 billion parameters) being the largest non-sparse French language model trained to date, using scaling laws to achieve optimal compute efficiency with the same budget as CamemBERT (13 times smaller). Critically, the authors find that the OSCAR pre-training dataset leads to low-quality offensive text generation, highlighting the importance of dataset curation for generative models. The models are evaluated on discriminative tasks (FLUE benchmark) and generative tasks (FQuAD question answering, OrangeSum summarization), achieving state-of-the-art performance on French abstract summarization while revealing significant data quality challenges for French language model development.

## Data Description

Collection of French GPT models with PAGnol-XL (1.5B parameters) being the largest French model trained from scratch. Evaluated on discriminative (FLUE) and generative tasks (FQuAD question answering, OrangeSum summarization). Found OSCAR pre-training dataset led to low-quality offensive text generation, highlighting data quality importance.


## Detailed Summary

This paper introduces PAGnol, a collection of French GPT-like autoregressive language models, with PAGnol-XL (1.5 billion parameters) being the largest non-sparse French language model available at the time of publication. Using scaling laws adapted for the French language, PAGnol-XL is trained with optimal compute efficiency, requiring the same computational budget (3 PF-days) as CamemBERT, a model 13 times smaller. The models are trained on CCNet (Common Crawl filtered data) and include four sizes from small to extra-large. A critical finding concerns data quality: the OSCAR pre-training dataset, commonly used for French NLP, leads to low-quality offensive text generation, highlighting the importance of careful dataset selection for generative models.

The authors evaluate PAGnol on both discriminative tasks (using the FLUE benchmark for French language understanding) and generative tasks including FQuAD question answering and OrangeSum abstract summarization. PAGnol achieves state-of-the-art performance on French abstract summarization while remaining competitive on discriminative tasks compared to encoder-only models like CamemBERT and FlauBERT. The scaling law analysis for French reveals similar patterns to English, confirming that larger models are more compute-efficient and that the relationship between model size and performance is predictable. The paper contributes to the democratization of large French language models by making models up to the Large size publicly available, while the XL model is accessible through an API.

## Paper Outline

1. Introduction - Large pre-trained models and French NLP landscape
2. Scaling Laws - Compute-optimal training for French
3. Pre-training - Data, architecture, training details
4. Dataset Quality - OSCAR vs. CCNet comparison
5. Evaluation - Discriminative (FLUE) and generative tasks
6. Conclusion

## Methods Summary

PAGnol models follow the GPT-2 architecture with four sizes: Small (124M), Medium (355M), Large (773M), and XL (1.5B parameters). Training uses the CCNet corpus (French portion of Common Crawl filtered by language identification and perplexity filtering). Scaling laws are fitted to determine optimal model size and training duration for a given compute budget. For discriminative evaluation, FLUE tasks (text classification, paraphrase detection, NLI, word sense disambiguation) are used. For generative evaluation, the models are tested on FQuAD (French extractive QA) and OrangeSum (French abstract summarization). The OSCAR dataset is evaluated separately and found to produce significantly more offensive and low-quality text than CCNet-trained models.

## Results Summary

PAGnol-XL achieves state-of-the-art on French abstract summarization (OrangeSum), outperforming both extractive baselines and previous generative models. On FLUE discriminative tasks, PAGnol is competitive with but does not surpass encoder-only models like CamemBERT, which is expected given the architectural differences (decoder-only vs. encoder-only). The scaling law analysis shows that for French, the relationship between compute budget and optimal model size closely mirrors English findings. The OSCAR-trained variant generates significantly more offensive content, including racist, sexist, and vulgar text, compared to the CCNet-trained version, demonstrating that dataset quality is a critical factor for safe generative model deployment.

## Conclusions

The authors plan to train increasingly large versions of PAGnol, exploring the capabilities of French extreme-scale models. Key limitations include the restricted availability of high-quality French pre-training data compared to English, and the computational cost of training billion-parameter models. The finding about OSCAR's quality issues has practical implications for all French NLP researchers relying on this commonly used dataset. Future work includes investigating few-shot capabilities at larger scales and developing safety measures for French text generation.

## Artifact Contributions

- **PAGnol Models**: Collection of French GPT models up to 1.5B parameters (https://lair.lighton.ai/pagnol)
- **PAGnol Code and Weights**: Models up to Large size publicly available

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Foundational French generative model that revealed bias and toxicity issues from pre-training data. Critical finding about OSCAR dataset leading to offensive outputs.

## Tags

