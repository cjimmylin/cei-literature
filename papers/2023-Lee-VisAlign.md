---






























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VVVLTVIR
type: journalArticle
year: 2023
short_title: VisAlign
first_author: "[[Jiyoung Lee]]"
last_author: "[[Edward Choi]]"
authors: "Jiyoung Lee; Seungho Kim; Seunghyun Won; Joonseok Lee; Marzyeh Ghassemi; James Thorne; Jaeseok Choi; O-Kil Kwon; Edward Choi"
external_pdf: "file:///Users/jimmylin/Zotero/storage/T6VNUFSA/Lee et al. - VisAlign Dataset for Measuring the Alignment between AI and Humans in Visual Perception.pdf"
pdf_extract: "PDF Extracts/2023/2023-Lee-VisAlign.md"
local_pdf: "[[PDFs/2023/2023-Lee-VisAlign.pdf]]"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Released VisAlign, a dataset for measuring 'AI-human visual alignment' by testing if models can correctly 'abstain' or express uncertainty on ambiguous images just like humans."
significance: "Extends the concept of alignment to visual perception, arguing that aligned models should not just classify correctly but also share human-like epistemic uncertainty."
tags: 
abstract: "AI alignment refers to models acting towards human-intended goals, preferences, or ethical principles. In this paper, we focus on the models’ visual perception alignment with humans, further referred to as AI-human visual alignment. Specifically, we propose a new dataset for measuring AI-human visual alignment in terms of image classiﬁcation. In order to evaluate AI-human visual alignment, a dataset should encompass samples with various scenarios and have gold human perception labels."
CONF-CC: "N/A"
DATE_ADDED: 20260129
LLM_assessed: "NA"
DATA_URL: "https://github.com/jiyounglee-0523/VisAlign"
CONFERENCE: "Journal"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
---
# VisAlign: Dataset for Measuring the Alignment between AI and Humans in Visual Perception

## Metadata

**Authors:** Lee, Jiyoung; Kim, Seungho; Won, Seunghyun; Lee, Joonseok; Ghassemi, Marzyeh; Thorne, James; Choi, Jaeseok; Kwon, O-Kil; Choi, Edward

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2308.01525
- **Github:** https://github.com/jiyounglee-0523/VisAlign

## Abstract

AI alignment refers to models acting towards human-intended goals, preferences, or ethical principles. In this paper, we focus on the models’ visual perception alignment with humans, further referred to as AI-human visual alignment. Specifically, we propose a new dataset for measuring AI-human visual alignment in terms of image classiﬁcation. In order to evaluate AI-human visual alignment, a dataset should encompass samples with various scenarios and have gold human perception labels. Our dataset consists of three groups of samples, namely Must-Act (i.e., Must-Classify), Must-Abstain, and Uncertain, and further divided into eight categories. All samples have a gold human perception label; even Uncertain (e.g., severely blurry) sample labels were obtained via crowd-sourcing. The validity of our dataset is veriﬁed by sampling theory, statistical theories related to survey design, and experts in the related ﬁelds. Using our dataset, we analyze the visual alignment and reliability of ﬁve popular visual perception models and eight abstention methods. Our code and data is available at https://github.com/jiyounglee-0523/VisAlign.

## Authors

[[Jiyoung Lee]], [[Seungho Kim]], [[Seunghyun Won]], [[Joonseok Lee]], [[Marzyeh Ghassemi]], [[James Thorne]], [[Jaeseok Choi]], [[O-Kil Kwon]], [[Edward Choi]]

## Detailed Summary

VisAlign is a dataset designed to measure AI-human visual alignment in image classification tasks. The dataset addresses a fundamental challenge: while humans naturally abstain from making predictions on unrecognizable or ambiguous images, machine learning models often produce overconfident outputs. The research proposes that AI systems should align with human visual perception behaviors to ensure safety across diverse use cases.

The dataset is organized into three groups: Must-Act (clearly identifiable photo-realistic images), Must-Abstain (images that qualified individuals would always abstain from classifying), and Uncertain (images that are cropped or corrupted in various ways). These groups are further divided into eight categories to cover diverse real-world scenarios. For the Uncertain group, 134 human annotations per image were collected via crowdsourcing to establish statistically robust ground truth distributions. The benchmark uses Hellinger distance to measure visual alignment between human label distributions and model output distributions.

## Paper Outline

1. Introduction - Defines AI-human visual alignment and its importance for safety
2. Related Works - Reviews existing datasets and visual alignment research
3. Dataset Construction - Details requirements, class selection, and category definitions
4. Metrics - Introduces Hellinger distance-based alignment metric and reliability score
5. Experiments - Benchmarks five baseline models with seven abstention functions
6. Results - Analysis of visual alignment and reliability across categories
7. Appendices - Survey design validation, prompts, statistical theory proofs

## Methods Summary

The dataset construction follows four requirements: clear class definitions, class familiarity to average individuals, coverage of diverse scenarios, and ground truth labels for each sample. Ten mammal classes were selected based on biological taxonomy and expert verification. Eight categories span Must-Act (ordinary images, spurious correlations, adversarial perturbations), Must-Abstain (out-of-class, chimeric features, near-miss biological relatives, non-photo-realistic), and Uncertain (cropped/corrupted with varying intensities). The Hellinger distance metric was chosen over KL divergence for its smoothness with extreme distributions and consideration of all class probabilities.

## Results Summary

The benchmark evaluated five visual perception models (various architectures) with eight abstention methods across all categories. Results showed that current robustness and OOD detection methods cannot be directly applied to AI-human visual alignment. The 8% pass rate on Category 8 (corrupted images) with intensity variations from 1-10 revealed significant gaps between model and human behavior on ambiguous inputs. The Uncertain category showed the most challenging alignment, with high variability in human annotations that models failed to replicate.

## Conclusions

The authors conclude that VisAlign is the first dataset to comprehensively measure AI-human visual perception alignment across diverse scenarios. Current state-of-the-art methods are inadequate for achieving visual alignment, highlighting the need for novel approaches. The dataset enables researchers to evaluate not just classification accuracy but also human-like abstention behavior and uncertainty calibration.

## Artifact Contributions

- VisAlign dataset: 900+ samples across 8 categories (10 mammal classes)
- Human annotations: 134 labels per Uncertain image (820,525+ total judgments from 2,716 participants)
- Code and data: https://github.com/jiyounglee-0523/VisAlign
- Training set: Subset of ImageNet-21K for Category 1 samples
- Open and closed test splits for external evaluation

## Data Description

The paper introduces VisAlign, a dataset for measuring AI-human visual alignment in image classification. It consists of three groups of samples (Must-Act, Must-Abstain, and Uncertain) across eight categories, with gold human perception labels obtained via crowd-sourcing (134 annotations per image). Five visual perception models and eight abstention methods are benchmarked. No LLMs are tested; the focus is on computer vision models.


## Notes

