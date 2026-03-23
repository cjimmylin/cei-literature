---
title: "Overview of GermEval Task 2, 2019 Shared Task on the Identification of Offensive Language"
source_pdf: "[[Lit-WS-PDFs/2019-Kreutz-GermEval 2019 Task 2.pdf]]"
pages: 12
extracted_at: 2025-01-29
---

# Overview of GermEval Task 2, 2019 Shared Task on the Identification of Offensive Language

## Authors
Julia Maria Struß (Potsdam University of Applied Sciences), Melanie Siegel (Darmstadt University of Applied Sciences), Josef Ruppenhofer (Leibniz Institute for German Language), Michael Wiegand (Leibniz ScienceCampus Heidelberg/Mannheim), Manfred Klenner (University of Zurich)

## Abstract
We present the second edition of the GermEval Shared Task on the Identification of Offensive Language. This shared task deals with the classification of German tweets from Twitter. Two subtasks were continued from the first edition, namely a coarse-grained binary classification task and a fine-grained multi-class classification task. As a novel subtask, we introduce the classification of offensive tweets as explicit or implicit.

The shared task had 13 participating groups submitting 28 runs for the coarse-grained task, another 28 runs for the fine-grained task, and 17 runs for the implicit-explicit task.

## Key Content

### Task Description
**Subtask 1: Coarse-grained Binary Classification**
- Classify tweets into OFFENSE vs OTHER
- OFFENSE category covers abusive language, insults, and profane statements

**Subtask 2: Fine-grained 4-way Classification**
- Four categories: ABUSE, INSULT, PROFANITY, OTHER
- PROFANITY: profane words used without intent to insult
- INSULT: clearly wants to offend someone, ascription of negatively evaluated qualities
- ABUSE: stronger form degrading based on group membership or dehumanization

**Subtask 3: Implicit vs. Explicit Classification**
- Implicit offensive language requires inference from context
- Includes figurative language like irony, sarcasm, or wordplay

### Dataset
- Source: Twitter (German tweets)
- Total: ~12,000 tweets across 2018 and 2019 data
- 2019 data: 7,025 new tweets manually annotated
- Training set: 3,994 tweets; Test set: 3,031 tweets
- Inter-annotator agreement: κ = 0.59 (moderate)

### Results Summary
- 13 participating teams
- Best F-score for coarse-grained: 76.95 (UPB team using BERT)
- Best F-score for fine-grained: 53.59 (UPB team)
- Best F-score for implicit/explicit: 73.11 (hpiDEDIS team)

### Key Findings
- BERT-based systems (especially pre-trained on German tweets) achieved best results
- Traditional classifiers (SVMs) still competitive within 1% of top systems
- Implicit offensive language detection remains challenging (best F-score for IMPLICIT class: 53.93)
- Problem of offensive language detection is "far from solved"

## References
Key citations include works on hate speech detection (Schmidt & Wiegand, 2017), BERT (Devlin et al., 2019), and related shared tasks (SemEval 2019, TRAC, AMI).
