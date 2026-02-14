---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JGLRT6FK
type: conferencePaper
short_title: "Value Profiles for Encoding Human Variation"
year: 2025
first_author: "[[Taylor Sorensen]]"
last_author: "[[Verena Rieser]]"
authors: "Taylor Sorensen; Pushkar Mishra; Roma Patel; Michael Henry Tessler; Michiel Bakker; Georgina Evans; Iason Gabriel; Noah Goodman; Verena Rieser"
doi: 10.48550/arXiv.2503.15484
url: "http://arxiv.org/abs/2503.15484"
external_pdf: "http://arxiv.org/pdf/2503.15484.pdf"
publication: "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Proposed using 'value profiles' (compressed natural language descriptions of underlying values) to model human variation in rating tasks, rather than just demographics."
significance: "Demonstrates that value profiles effectively compress rater information (>70% retention) and allow for steerable, interpretable personalization of model outputs that aligns better with individual rater variation than demographic groups."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Sorensen-Value Profiles for Encoding Human Variation.md"
abstract: "Modelling human variation in rating tasks is crucial for personalization, pluralistic model alignment, and computational social science. We propose representing individuals using nat- ural language value profiles – descriptions of underlying values compressed from in-context demonstrations – along with a steerable de- coder model that estimates individual ratings from a rater representation. To measure the predictive information in a rater representation, we introduce an information-theoretic me"
paper_summary: "Abstract: Modelling human variation in rating tasks is crucial for personalization, pluralistic model alignment, and computational social science. We propose representing individuals using nat- ural language va | Overview: Value Profiles for Encoding Human Variation Taylor Sorensen1†, Pushkar Mishra2, Roma Patel2, Michael Henry Tessler2, Michiel Bakker2, Georgina Evans2, Iason Gabriel2, Noah Goodman2, Verena Rieser2 1De | Methodology: Training details We split raters into 50/50 train/test splits and report results for training/test --- Page 4 --- Dataset Task Choices Dem. Inst. Rate | Key Findings: In the previous sections, we have established that value profiles are predictive of individual rater an- notations for a wide variety of relevant task | Conclusions: In conclusion, we proposed modeling human vari- ation via natural language value profiles. We also proposed a methodology to compare the usable inform"
local_pdf: "[[PDFs/2025/2025-Sorensen-Value Profiles for Encoding Human Variation.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation methodology"
data_metrics: "Not specified"
LLM_assessed: "Gemma, Gemini"
DATA_URL: NA
---
# Value Profiles for Encoding Human Variation

## Metadata

**Authors:** Sorensen, Taylor; Mishra, Pushkar; Patel, Roma; Tessler, Michael Henry; Bakker, Michiel; Evans, Georgina; Gabriel, Iason; Goodman, Noah; Rieser, Verena

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2503.15484](https://doi.org/10.48550/arXiv.2503.15484)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Sorensen-Value Profiles for Encoding Human Variation.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.15484
- **DOI:** https://doi.org/10.48550/arXiv.2503.15484

## Abstract

Modelling human variation in rating tasks is crucial for personalization, pluralistic model alignment, and computational social science. We propose representing individuals using natural language value profiles – descriptions of underlying values compressed from in-context demonstrations – along with a steerable decoder model that estimates individual ratings from a rater representation. To measure the predictive information in a rater representation, we introduce an information-theoretic methodology and find that demonstrations contain the most information, followed by value profiles, then demographics. However, value profiles effectively compress the useful information from demonstrations (>70% information preservation) and offer advantages in terms of scrutability, interpretability, and steerability. Furthermore, clustering value profiles to identify similarly behaving individuals better explains rater variation than the most predictive demographic groupings. Going beyond test set performance, we show that the decoder predictions change in line with semantic profile differences, are wellcalibrated, and can help explain instance-level disagreement by simulating an annotator population. These results demonstrate that value profiles offer novel, predictive ways to describe individual variation beyond demographics or group information.

## Authors

[[Taylor Sorensen]], [[Pushkar Mishra]], [[Roma Patel]], [[Michael Henry Tessler]], [[Michiel Bakker]], [[Georgina Evans]], [[Iason Gabriel]], [[Noah Goodman]], [[Verena Rieser]]

## Data Description

The paper uses six existing annotator disagreement datasets (OpinionQA, Hatespeech-Kumar, DICES, ValuePrism, Habermas-Likert, and Prism) spanning tasks in model alignment, content moderation, and computational social science. These datasets contain forced-choice selection tasks with annotator IDs and demographic information, totaling over 1 million ratings from thousands of raters. The models evaluated include Gemma-2-9b, Gemma-2-27b (as encoders/decoders), and Gemini-1.5 Pro (as encoder), fine-tuned to predict individual rater variation.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Human-Computer-Interaction
