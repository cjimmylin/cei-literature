---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0282
type: conferencePaper
short_title: "I2P: Inappropriate Image Prompts Test Bed"
year: 2025
first_author: "[[Schramowski, Patrick]]"
last_author: "[[Kersting, Kristian]]"
authors: "[[Schramowski, Patrick]]; [[Tauchmann, Christopher]]; [[Kersting, Kristian]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2202.06675"
external_pdf: "https://arxiv.org/pdf/2202.06675.pdf"
pdf_extract: "PDF Extracts/2022/2022-Schramowski-I2P Inappropriate Image Prompts Test Bed.md"
local_pdf: "[[PDFs/2022/2022-Schramowski-I2P Inappropriate Image Prompts Test Bed.pdf]]"
publication: FAccT
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "Large datasets underlying much of current machine learning raise serious issues concerning inappropriate content such as offensive, insulting, threatening, or might otherwise cause anxiety. This calls for increased dataset documentation, e.g., using datasheets. They, among other topics, encourage to reflect on the composition of the datasets. So far, this documentation, however, is done manually and therefore can be tedious and error-prone, especially for large image datasets. Here we ask the arguably \"circular\" question of whether a machine can help us reflect on inappropriate content, answering Question 16 in Datasheets. To this end, we propose to use the information stored in pre-trained transformer models to assist us in the documentation process. Specifically, prompt-tuning based on a dataset of socio-moral values steers CLIP to identify potentially inappropriate content, therefore reducing human labor. We then document the inappropriate images found using word clouds, based on captions generated using a vision-language model. The documentations of two popular, large-scale computer vision datasets -- ImageNet and OpenImages -- produced this way suggest that machines can indeed help dataset creators to answer Question 16 on inappropriate image content."
research_topic: "Computer Vision & Multimodal"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "BERT"
DATA_URL: "https://github.com/ml-research/Q16"
---
# I2P: Inappropriate Image Prompts Test Bed

## Authors

[[Patrick Schramowski|Schramowski, Patrick]], [[Tauchmann, Christopher]], [[Kristian Kersting|Kersting, Kristian]]

## Metadata

**Authors:** Schramowski, Patrick; Tauchmann, Christopher; Kersting, Kristian

**Year:** 2022

**Type:** conferencePaper

**Venue:** FAccT

## Links

- **arXiv:** https://arxiv.org/abs/2202.06675

## Abstract

*(To be fetched)*

## Dataset Information

Real-world prompts for evaluating inappropriate content in image generation models

## Data Description

The paper proposes Q16, a semi-automatic pipeline for documenting inappropriate image content in large-scale computer vision datasets. It uses CLIP steered via prompt-tuning on the Socio-Moral Image Database (SMID, 2,941 images) to detect potentially inappropriate content, achieving 96.3% accuracy with ViT-B/16. The pipeline is applied to ImageNet-ILSVRC-2012 and OpenImagesV6 datasets for documentation purposes, but does not test or evaluate any LLMs from the canonical list.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

