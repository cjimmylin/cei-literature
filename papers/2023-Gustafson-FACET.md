---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2R29RMNC
type: conferencePaper
short_title: FACET
year: 2025
first_author: "[[Laura Gustafson]]"
last_author: "[[Candace Ross]]"
authors: "Laura Gustafson; Chloe Rolland; Nikhila Ravi; Quentin Duval; Aaron Adcock; Cheng-Yang Fu; Melissa Hall; Candace Ross"
doi: 10.1109/ICCV51070.2023.01863
url: "https://ieeexplore.ieee.org/document/10377223/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/RS2ZQBS3/Gustafson et al. - 2023 - FACET Fairness in Computer Vision Evaluation Benchmark.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Released FACET (Fairness in Computer Vision Evaluation), a benchmark of 32k images with expert-annotated person-related attributes (skin tone, hair type) to measure CV model fairness."
significance: "Enables granular analysis of performance disparities in vision tasks (classification, detection) across intersectional demographics, revealing significant biases in state-of-the-art models."
tags: 
abstract: "Computer vision models have known performance disparities across attributes such as gender and skin tone. This means during tasks such as classification and detection, model performance differs for certain classes based on the demographics of the people in the image. These disparities have been shown to exist, but until now there has not been a unified approach to measure these differences for common use-cases of computer vision models."
DATE_ADDED: 20260208
LLM_assessed: "CLIP ViT-B/32, ViT-B/16, Faster R-CNN ResNet-50-FPN, Mask R-CNN ResNet-50-FPN"
DATA_URL: "https://facet.metademolab.com"
pdf_extract: "PDF Extracts/2023/2023-Gustafson-FACET.md"
local_pdf: "[[PDFs/2023/2023-Gustafson-FACET.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# FACET: Fairness in Computer Vision Evaluation Benchmark

## Metadata

**Authors:** Gustafson, Laura; Rolland, Chloe; Ravi, Nikhila; Duval, Quentin; Adcock, Aaron; Fu, Cheng-Yang; Hall, Melissa; Ross, Candace

**Year:** 2023

**Publication:** 2023 IEEE/CVF International Conference on Computer Vision (ICCV)

**Type:** conferencePaper

**DOI:** [10.1109/ICCV51070.2023.01863](https://doi.org/10.1109/ICCV51070.2023.01863)

**Pages:** 20313-20325

**Publisher:** IEEE

## Links

- **URL:** https://ieeexplore.ieee.org/document/10377223/
- **DOI:** https://doi.org/10.1109/ICCV51070.2023.01863

## Abstract

Computer vision models have known performance disparities across attributes such as gender and skin tone. This means during tasks such as classification and detection, model performance differs for certain classes based on the demographics of the people in the image. These disparities have been shown to exist, but until now there has not been a unified approach to measure these differences for common use-cases of computer vision models. We present a new benchmark named FACET (FAirness in Computer Vision EvaluaTion), a large, publicly available evaluation set of 32k images for some of the most common vision tasks - image classification, object detection and segmentation. For every image in FACET, we hired expert reviewers to manually annotate person-related attributes such as perceived skin tone and hair type, manually draw bounding boxes and label fine-grained person-related classes such as disk jockey or guitarist. In addition, we use FACET to benchmark state-of-the-art vision models and present a deeper understanding of potential performance disparities and challenges across sensitive demographic attributes. With the exhaustive annotations collected, we probe models using single demographics attributes as well as multiple attributes using an intersectional approach (e.g. hair color and perceived skin tone). Our results show that classification, detection, segmentation, and visual grounding models exhibit performance disparities across demographic attributes and intersections of attributes. These harms suggest that not all people represented in datasets receive fair and equitable treatment in these vision tasks. We hope current and future results using our benchmark will contribute to fairer, more robust vision models. FACET is available publicly at https://facet.metademolab.com.

## Authors

[[Laura Gustafson]], [[Chloe Rolland]], [[Nikhila Ravi]], [[Quentin Duval]], [[Aaron Adcock]], [[Cheng-Yang Fu]], [[Melissa Hall]], [[Candace Ross]]

## Detailed Summary

FACET (FAirness in Computer Vision EvaluaTion) is a comprehensive benchmark designed to evaluate fairness in computer vision models across demographic attributes. The benchmark addresses a critical gap in the field: while performance disparities across attributes like gender and skin tone have been documented, there was no unified approach to measure these differences for common vision tasks. FACET provides 32,000 images from Segment Anything 1 Billion (SA-1B) with exhaustive annotations for 13 person attributes and 52 person-related classes.

The benchmark enables multi-level fairness analysis that previous datasets could not support. Unlike existing fairness datasets that focus on limited demographic attributes or single tasks, FACET includes annotations for perceived skin tone (using the 10-point Monk Skin Tone Scale), perceived gender presentation, perceived age group, and additional visual attributes like hair type, facial hair, accessories, and tattoos. Every person in every image is exhaustively annotated, with manually drawn bounding boxes and labels for fine-grained categories such as "guitarist," "nurse," or "skateboarder."

The research reveals significant performance disparities in state-of-the-art models. For instance, CLIP shows performance gaps of up to 21.7% between perceived gender presentations for certain classes (e.g., "dancer" performs better for perceived female presentation, while "gardener" performs better for perceived male presentation). These findings enable deeper intersectional analysis, examining how combinations of attributes (e.g., coily hair and darker perceived skin tone) can magnify performance disparities.

## Paper Outline

1. Introduction
   - Known performance disparities in computer vision
   - Need for unified fairness measurement approach
   - FACET contributions overview
2. Related Work
   - Classification and detection fairness datasets
   - Best practices for dataset development
3. Benchmark Method
   - Category selection from WordNet hierarchy
   - Connection to ImageNet-21k for compatibility
4. Attribute Selection
   - Demographic attributes: perceived skin tone, gender presentation, age group
   - Additional visual attributes: hair type/color, accessories, tattoos
5. Annotation Method
   - Five-stage annotation pipeline
   - Annotator diversity across geographic regions
   - Quality control procedures
6. Fairness Evaluations
   - Disparity computation methodology
   - Classification model evaluations (CLIP, ViT)
   - Detection model evaluations (Faster R-CNN, DINO)
   - Segmentation model evaluations (SAM)
   - Visual grounding evaluations (GLIP)
7. FACET Statistics and Distribution

## Methods Summary

FACET was constructed through a rigorous five-stage annotation pipeline using expert annotators from six geographic regions (North America, Latin America, Middle East, Africa, Southeast Asia, East Asia). The process began with filtering 32,000 images from SA-1B using caption and tag matching for 52 person-related categories derived from WordNet. Annotators completed stage-specific training before labeling.

Stage 1 filtered images by target categories; Stage 2 drew bounding boxes and assigned primary/secondary class labels; Stage 3 collected perceived skin tone annotations from three independent raters using the Monk Skin Tone Scale (aggregated as a distribution); Stage 4 annotated remaining attributes; Stage 5 labeled SA-1B masks as person/clothing/hair.

For fairness evaluation, the benchmark computes disparity as the difference in recall between demographic groups. Models evaluated include CLIP and ViT for classification, Faster R-CNN and DINO for detection, SAM for segmentation, and GLIP for visual grounding.

## Results Summary

- Classification Disparities (CLIP): Performance gaps up to 21.7% between perceived gender presentations; "dancer" favors female presentation (+21.7%), "gardener" favors male presentation (+16.4%)
- Perceived Skin Tone: Models generally show lower performance for darker perceived skin tones across tasks
- Intersectional Effects: Combining attributes (e.g., hair type and perceived skin tone) often magnifies disparities
- Detection Models: Similar bias patterns observed in Faster R-CNN and DINO
- Segmentation: SAM exhibits performance disparities across demographic groups
- Visual Grounding: GLIP shows class-dependent demographic biases
- Geographic Distribution: Images span global locations with annotation quality ensured through multi-region annotator pools

## Conclusions

FACET reveals that state-of-the-art computer vision models exhibit systematic performance disparities across demographic attributes for classification, detection, segmentation, and visual grounding tasks. The benchmark's exhaustive annotations enable both single-attribute and intersectional fairness analyses, providing unprecedented granularity for understanding model biases. These findings suggest that not all people receive fair treatment in current vision systems. FACET is released as an evaluation-only benchmark (training is prohibited) to encourage the development of fairer, more robust vision models.

## Artifact Contributions

- FACET benchmark: 32,000 images with exhaustive annotations
- 50,000 annotated people with bounding boxes
- 52 person-related class labels
- 13 person attributes including perceived skin tone (Monk Scale), gender presentation, age group
- 69,000 masks labeled as person/clothing/hair
- Additional attributes: hair color/type, facial hair, accessories, tattoos, lighting conditions
- Publicly available at: https://facet.metademolab.com
- Note: FACET is evaluation-only; using annotations for training is prohibited

## Data Description

The paper presents FACET (Fairness in Computer Vision Evaluation Benchmark), containing 32,000 images from SA-1B with exhaustive annotations for 13 person attributes and 52 person classes, annotated by expert reviewers. State-of-the-art vision models including CLIP ViT-B/32, ViT-B/16, Faster R-CNN, and Mask R-CNN are benchmarked for fairness across perceived skin tone, age, and gender presentation demographics, revealing performance disparities across demographic attributes.


## Notes


## Citation Info

56 citations (Semantic Scholar/DOI) [2025-08-27]
