---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VRNNC6SF
type: document
short_title: "Some Issues in Predictive Ethics Modeling"
year: 2024
first_author: "[[Ben Fitzgerald]]"
last_author: "[[Ben Fitzgerald]]"
authors: "Ben Fitzgerald"
url: "https://arxiv.org/abs/2407.05244"
external_pdf: "https://arxiv.org/pdf/2407.05244.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Christianity"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "American, Bias & Fairness"
key_contribution: "Showed that 'Predictive Ethics' models (like Delphi) are easily broken by adversarial 'contrast sets' – changing 3-5 words can flip the label, and they over-rely on textual bias rather than reasoning."
significance: "A strong critique of the 'Ethics as Classification' paradigm (Moral Stories/Delphi), arguing that high accuracy scores are illusory and models lack robust moral understanding."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.md"
paper_summary: "Overview: ‭Some Issues in Predictive Ethics Modeling: An Annotated Contrast Set of 'Moral Stories'‬ ‭By Ben Fitzgerald, Haverford College‬‭1‬ ‭Abstract:‬ ‭Models‬ ‭like‬‭the‬‭Allen‬‭Institute's‬‭Delphi‬‭have‬‭b"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.pdf]]"
abstract: "Models like Delphi have been able to label ethical dilemmas as moral or immoral with astonishing accuracy. This paper challenges accuracy as a holistic metric for ethics modeling by identifying issues with translating moral dilemmas into text-based input. It demonstrates these issues with contrast sets that substantially reduce the performance of classifiers trained on the dataset Moral Stories. Ultimately, we obtain concrete estimates for how much specific forms of data misrepresentation harm classifier accuracy. Specifically, label-changing tweaks to the descriptive content of a situation (as small as 3-5 words) can reduce classifier accuracy to as low as 51%, almost half the initial accuracy of 99.8%. Associating situations with a misleading social norm lowers accuracy to 98.8%, while adding textual bias (i.e. an implication that a situation already fits a certain label) lowers accuracy to 77%. These results suggest not only that many ethics models have substantially overfit, but that several precautions are required to ensure that input accurately captures a moral dilemma. This paper recommends re-examining the structure of a social norm, training models to ask for context with defeasible reasoning, and filtering input for textual bias. Doing so not only gives us the first concrete estimates of the average cost to accuracy of misrepresenting ethics data, but gives researchers practical tips for considering these estimates in research."
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "RoBERTa"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: 95
virtue_ethics: 0
deontological_ethics: 50
utilitarian_ethics: 50
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "5 words"
ethics_perspective: "Bias & Fairness"
---
# Some Issues in Predictive Ethics Modeling: An Annotated Contrast Set of "Moral Stories"

## Metadata

**Authors:** Fitzgerald, Ben

**Year:** 2024

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2407.05244

## Abstract

Models like Delphi have been able to label ethical dilemmas as moral or immoral with astonishing accuracy. This paper challenges accuracy as a holistic metric for ethics modeling by identifying issues with translating moral dilemmas into text-based input. It demonstrates these issues with contrast sets that substantially reduce the performance of classifiers trained on the dataset Moral Stories. Ultimately, we obtain concrete estimates for how much specific forms of data misrepresentation harm classifier accuracy. Specifically, label-changing tweaks to the descriptive content of a situation (as small as 3-5 words) can reduce classifier accuracy to as low as 51%, almost half the initial accuracy of 99.8%. Associating situations with a misleading social norm lowers accuracy to 98.8%, while adding textual bias (i.e. an implication that a situation already fits a certain label) lowers accuracy to 77%. These results suggest not only that many ethics models have substantially overfit, but that several precautions are required to ensure that input accurately captures a moral dilemma. This paper recommends re-examining the structure of a social norm, training models to ask for context with defeasible reasoning, and filtering input for textual bias. Doing so not only gives us the first concrete estimates of the average cost to accuracy of misrepresenting ethics data, but gives researchers practical tips for considering these estimates in research.

## Authors

[[Ben Fitzgerald]]

## Data Description

Annotated contrast set of four augmentation types (norm swaps, textual bias, descriptive shifts, cultural context shifts) on Emelin et al.'s Moral Stories dataset, testing classifier robustness on ethical predictions.


## Notes

