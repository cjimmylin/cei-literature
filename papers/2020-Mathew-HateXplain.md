---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JTP6EDJI
type: conferencePaper
short_title: HateXplain
year: 2025
first_author: "[[Binny Mathew]]"
last_author: "[[Animesh Mukherjee]]"
authors: "Binny Mathew; Punyajoy Saha; Seid Muhie Yimam; Chris Biemann; Pawan Goyal; Animesh Mukherjee"
doi: 10.48550/arXiv.2012.10289
url: "http://arxiv.org/abs/2012.10289"
external_pdf: "http://arxiv.org/pdf/2012.10289.pdf"
publication: "AAAI Conference on Artificial Intelligence"
national_ethnic_cultural: N/A
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: N/A
newtags: "Toxicity & Hate Speech"
key_contribution: "Released HateXplain, a benchmark dataset for *explainable* hate speech detection where posts are annotated with labels, target communities, and rationale spans."
significance: "Demonstrates that high-performing classifiers often relying on spurious cues faulty, and provides a resource to train models that can justify their decisions by highlighting relevant text spans."
tags: 
local_pdf: "[[PDFs/2020/2020-Mathew-HateXplain.pdf]]"
pdf_extract: "PDF Extracts/2020/2020-Mathew-HateXplain.md"
abstract: "Hate speech is a challenging issue plaguing the online so- cial media. While better models for hate speech detection are continuously being developed, there is little research on the bias and interpretability aspects of hate speech. In this paper, we introduce HateXplain, the ﬁrst benchmark hate speech dataset covering multiple aspects of the issue. Each post in our dataset is annotated from three different perspectives: the basic, commonly used 3-class classiﬁcation (i.e., hate, offen- sive or"
paper_summary: "Abstract: Hate speech is a challenging issue plaguing the online so- cial media. While better models for hate speech detection are continuously being developed, there is little research on the bias and interpre | Overview: HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection* Binny Mathew1†, Punyajoy Saha1†, Seid Muhie Yimam2 Chris Biemann2, Pawan Goyal1, Animesh Mukherjee1 1 Indian Institute of Technol | Key Findings: To build the HateXplain benchmark dataset, we consider multiple types of metrics to cover several aspects of hate speech. Taking inspiration from the"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness annotated dataset for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: "BERT"
DATA_URL: "https://github.com/punyajoy/HateXplain"
---
# HateXplain: A Benchmark Dataset for Explainable Hate Speech Detection

## Metadata

**Authors:** Mathew, Binny; Saha, Punyajoy; Yimam, Seid Muhie; Biemann, Chris; Goyal, Pawan; Mukherjee, Animesh

**Year:** 2022

**Type:** preprint

**DOI:** [10.48550/arXiv.2012.10289](https://doi.org/10.48550/arXiv.2012.10289)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2020/2020-Mathew-HateXplain.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2012.10289
- **DOI:** https://doi.org/10.48550/arXiv.2012.10289

## Abstract

Hate speech is a challenging issue plaguing the online social media. While better models for hate speech detection are continuously being developed, there is little research on the bias and interpretability aspects of hate speech. In this paper, we introduce HateXplain, the ﬁrst benchmark hate speech dataset covering multiple aspects of the issue. Each post in our dataset is annotated from three different perspectives: the basic, commonly used 3-class classiﬁcation (i.e., hate, offensive or normal), the target community (i.e., the community that has been the victim of hate speech/offensive speech in the post), and the rationales, i.e., the portions of the post on which their labelling decision (as hate, offensive or normal) is based. We utilize existing state-of-the-art models and observe that even models that perform very well in classiﬁcation do not score high on explainability metrics like model plausibility and faithfulness. We also observe that models, which utilize the human rationales for training, perform better in reducing unintended bias towards target communities. We have made our code and dataset public1 for other researchers.

## Authors

[[Binny Mathew]], [[Punyajoy Saha]], [[Seid Muhie Yimam]], [[Chris Biemann]], [[Pawan Goyal]], [[Animesh Mukherjee]]

## Data Description

HateXplain is a benchmark dataset of 20,148 posts from Twitter and Gab, annotated for three-class hate speech classification (hate, offensive, normal), target community identification across 10 communities, and word-level rationale annotations justifying labeling decisions. Each post was annotated by three Amazon Mechanical Turk workers, with a Krippendorff's alpha of 0.46.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language #Computer-Science---Social-and-Information-Networks

## Citation Info

606 citations (Semantic Scholar/arXiv) [2025-08-27] 605 citations (Semantic Scholar/arXiv) [2025-08-23]
