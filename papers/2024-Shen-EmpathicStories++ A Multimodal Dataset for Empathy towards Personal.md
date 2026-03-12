---




























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0167
type: conferencePaper
short_title: "EmpathicStories++: A Multimodal Dataset for Empathy towards Personal Experiences"
year: 2024
first_author: "[[Jocelyn Shen]]"
last_author: "[[Hae Won Park]]"
authors: "Jocelyn Shen; Yubin Kim; Mohit Hulse; Wazeer Zulfikar; Sharifa Alghowinem; Cynthia Breazeal; Hae Won Park"
url: "https://arxiv.org/abs/2405.15708"
external_pdf: "https://arxiv.org/pdf/2405.15708.pdf"
pdf_extract: "PDF Extracts/2024/2024-Shen-EmpathicStories++ A Multimodal Dataset for Empathy towards Personal.md"
local_pdf: "[[PDFs/2024/2024-Shen-EmpathicStories++ A Multimodal Dataset for Empathy towards Personal.pdf]]"
publication: "ACL 2024"
CONF-CC: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Modeling empathy is a complex endeavor that is rooted in interpersonal and experiential dimensions of human interaction, and remains an open problem within AI. Existing empathy datasets fall short in capturing the richness of empathy responses, often being confined to in-lab or acted scenarios, lacking longitudinal data, and missing self-reported labels. We introduce a new multimodal dataset for empathy during personal experience sharing: the EMPATHICSTORIES++ dataset1 containing 53 hours of..."
LLM_assessed: "GPT-3, GPT-4"
DATA_URL: "https://mitmedialab.github.io/empathic-stories-multimodal/"
CONFERENCE: "ACL 2024"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Computer Vision & Multimodal"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# EmpathicStories++: A Multimodal Dataset for Empathy towards Personal Experiences

## Authors

[[Jocelyn Shen]], [[Yubin Kim]], [[Mohit Hulse]], [[Wazeer Zulfikar]], [[Sharifa Alghowinem]], [[Cynthia Breazeal]], [[Hae Won Park]]

## Metadata

**Authors:** Jocelyn Shen; Yubin Kim; Mohit Hulse; Wazeer Zulfikar; Sharifa Alghowinem; Cynthia Breazeal; Hae Won Park

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **arXiv:** https://arxiv.org/abs/2405.15708

## Abstract

Modeling empathy is a complex endeavor that is rooted in interpersonal and experiential dimensions of human interaction, and remains an open problem within AI. Existing empathy datasets fall short in capturing the richness of empathy responses, often being confined to in-lab or acted scenarios, lacking longitudinal data, and missing self-reported labels. We introduce a new multimodal dataset for empathy during personal experience sharing: the EMPATHICSTORIES++ dataset1 containing 53 hours of video, audio, and text data of 41 participants sharing vulnerable experiences and reading empathically resonant stories with an AI agent. EMPATHICSTORIES++ is the first longitudinal dataset on empathy, collected over a month-long deployment of social robots in participants’ homes, as participants engage in natural, empathic storytelling interactions with AI agents. We then introduce a novel task of predicting individuals’ empathy toward others’ stories based on their personal experiences, evaluated in two contexts: participants’ own personal shared story context and their reflections 1https://mitmedialab.github.io/ empathic-stories-multimodal/ on stories they read. We benchmark this task using state-of-the-art models to pave the way for future improvements in contextualized and longitudinal empathy modeling. Our work provides a valuable resource for further research in developing empathetic AI systems and understanding the intricacies of human empathy within genuine, real-world settings.

## Dataset Information

53 hours of video, audio, and text data; 41 participants; 269 sessions across month-long deployment; self-reported empathy ratings; multimodal (video/audio/text)

## Data Description

EmpathicStories++ is a multimodal dataset containing 53 hours of video, audio, and text data from 41 participants across 269 sessions over a month-long in-home deployment with social robots. Participants shared personal stories, read empathically similar stories, and self-rated their empathy on a 1-5 scale. The dataset includes 5,380 utterances, psychometric surveys (Big 5 personality, trait empathy, absorption), and extracted features from OpenFace, ResNet50, openSMILE, GloVe, and Sentence-BERT.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** MEDIUM

## Tags

