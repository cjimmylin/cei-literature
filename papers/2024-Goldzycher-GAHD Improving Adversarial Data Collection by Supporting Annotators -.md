---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0467
type: preprint
short_title: "GAHD: Improving Adversarial Data Collection by Supporting Annotators - Lessons from a German Hate Speech Dataset"
year: 2024
first_author: "[[Janis Goldzycher]]"
last_author: "[[Gerold Schneider]]"
authors: Janis Goldzycher, Paul Rottger, Gerold Schneider
url: "https://arxiv.org/abs/2403.19559"
external_pdf: "https://arxiv.org/pdf/2403.19559.pdf"
publication: arXiv / NAACL 2024
local_pdf: "[[PDFs/2024/2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators -.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators -.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for hate speech detection"
data_metrics: "11k examples"
LLM_assessed: "GPT-3.5, GPT-4, LeoLM, gelectra-large"
DATA_URL: "https://github.com/jagol/gahd"
tags: 
abstract: "Hate speech detection models are only as good as the data they are trained on. Datasets sourced from social media suffer from systematic gaps and biases, leading to unreliable models with simplistic decision boundaries. Adversarial datasets, collected by exploiting model weaknesses, promise to fix this problem. However, adversarial data collection can be slow and costly, and individual annotators have limited creativity."
ethics_perspective: "AI Safety & Alignment"
---
# GAHD: Improving Adversarial Data Collection by Supporting Annotators - Lessons from a German Hate Speech Dataset

## Authors

[[Janis Goldzycher, Paul Rottger, Gerold Schneider]]

## Metadata

**Authors:** Janis Goldzycher, Paul Rottger, Gerold Schneider

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / NAACL 2024

**Languages:** German

**Benchmark:** GAHD

## Links

- **arXiv:** https://arxiv.org/abs/2403.19559
- **Code/Data:** https://github.com/jagol/gahd

## Abstract

German Adversarial Hate speech Dataset with ~11,000 examples (42.4% hate speech). Uses adversarial data collection with annotator support strategies. Training on GAHD clearly improves model robustness.

## Summary

This paper introduces GAHD, a German Adversarial Hate speech Dataset with approximately 11,000 examples collected through four rounds of dynamic adversarial data collection (DADC). The authors explore multiple annotator support strategies across different rounds: free creation (R1), validating English-to-German translations (R2), validating newspaper sentences misclassified as hate speech (R3), and creating contrastive examples (R4). Experimental results show that training on GAHD improves model robustness substantially, with 18-20 percentage point increases in macro F1 scores on both in-domain and out-of-domain tests, and that mixing multiple support strategies yields the most consistent improvements.

## Data Description

GAHD (German Adversarial Hate speech Dataset) contains 11,000 German examples (42.4% hate speech) collected via dynamic adversarial data collection across 4 rounds. Training on GAHD improves model robustness, with 18-20 percentage point increases in macro F1 on in-domain and out-of-domain tests.


## Detailed Summary

This paper introduces GAHD (German Adversarial Hate speech Dataset), a novel resource for improving hate speech detection in German. The dataset contains approximately 11,000 adversarial examples (42.4% labeled as hate speech) collected through four rounds of dynamic adversarial data collection (DADC) using the Dynabench platform. The key innovation is the exploration of different annotator support strategies across rounds to produce more diverse and challenging examples. The authors recruited seven annotators (native or highly competent German speakers) and employed a prescriptive annotation approach with detailed instructions that emphasize German-specific cultural context, covering protected groups and stereotypes across Austria, Germany, and Switzerland.

## Paper Outline

1. Introduction - Motivation for adversarial data collection for German hate speech
2. Annotation - Setup, definition of hate speech, guidelines, annotator details
3. Dynamic Adversarial Data Collection - Target model, four rounds (R1-R4) with different strategies
4. Experiments - Evaluation of model robustness, contribution of individual rounds
5. Benchmarking commercial APIs and LLMs on GAHD
6. Conclusion

## Methods Summary

The authors use four rounds of DADC, each with a distinct annotator support strategy: R1 (Unguided creation: annotators freely create adversarial examples), R2 (Translation validation: annotators validate German translations of English adversarial examples from Vidgen et al.), R3 (Newspaper validation: annotators validate newspaper sentences misclassified by the target model as hate speech), and R4 (Contrastive examples: annotators modify existing examples to flip labels, producing 1,300 contrastive pairs). The target model throughout is gelectra-large (335M parameters), fine-tuned on five existing German hate speech datasets. After each round, the model is retrained on all accumulated data, making it progressively harder to trick.

## Results Summary

Training on GAHD produces substantial robustness improvements: nearly 20 percentage point increases in macro F1 on both the GAHD test split (in-domain) and the German HateCheck test suite (out-of-domain). Rounds with manually crafted examples (R1, R4) are more effective individually, but mixing multiple strategies leads to the most consistent improvements. Benchmarking commercial APIs (Perspective API, OpenAI Moderation, Azure Content Safety) and LLMs reveals that APIs generally struggle with GAHD, with only GPT-4 achieving over 80% macro F1. Cohen's Kappa inter-annotator agreement was 0.83 for R1.

## Conclusions

GAHD is the first German adversarial hate speech dataset and demonstrates that annotator support strategies significantly improve the efficiency and diversity of adversarial data collection. The dataset is challenging even for state-of-the-art models and clearly improves robustness when used for training. The authors recommend mixing multiple support strategies for optimal results and release GAHD publicly for the research community.

## Artifact Contributions

- **GAHD dataset**: ~11,000 adversarial German hate speech examples with binary labels, publicly available at https://github.com/jagol/gahd
- **Contrastive pairs**: 1,300 paired examples with flipped labels from R4
- **Improved DADC methodology**: Four novel annotator support strategies for adversarial data collection

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Adversarially-constructed German hate speech dataset designed to be challenging for state-of-the-art detection models.

## Tags

