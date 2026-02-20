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
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "American, Bias & Fairness"
key_contribution: "Showed that 'Predictive Ethics' models (like Delphi) are easily broken by adversarial 'contrast sets' – changing 3-5 words can flip the label, and they over-rely on textual bias rather than reasoning."
significance: "A strong critique of the 'Ethics as Classification' paradigm (Moral Stories/Delphi), arguing that high accuracy scores are illusory and models lack robust moral understanding."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.md"
paper_summary: "Overview: ‭Some Issues in Predictive Ethics Modeling: An Annotated Contrast Set of 'Moral Stories'‬ ‭By Ben Fitzgerald, Haverford College‬‭1‬ ‭Abstract:‬ ‭Models‬ ‭like‬‭the‬‭Allen‬‭Institute's‬‭Delphi‬‭have‬‭b"
local_pdf: "[[PDFs/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.pdf]]"
abstract: "Models like Delphi have been able to label ethical dilemmas as moral or immoral with astonishing accuracy. This paper challenges accuracy as a holistic metric for ethics modeling by identifying issues with translating moral dilemmas into text-based input. It demonstrates these issues with contrast sets that substantially reduce the performance of classifiers trained on the dataset Moral Stories. Ultimately, we obtain concrete estimates for how much specific forms of data misrepresentation harm classifier accuracy. Specifically, label-changing tweaks to the descriptive content of a situation (as small as 3-5 words) can reduce classifier accuracy to as low as 51%, almost half the initial accuracy of 99.8%. Associating situations with a misleading social norm lowers accuracy to 98.8%, while adding textual bias (i.e. an implication that a situation already fits a certain label) lowers accuracy to 77%. These results suggest not only that many ethics models have substantially overfit, but that several precautions are required to ensure that input accurately captures a moral dilemma. This paper recommends re-examining the structure of a social norm, training models to ask for context with defeasible reasoning, and filtering input for textual bias. Doing so not only gives us the first concrete estimates of the average cost to accuracy of misrepresenting ethics data, but gives researchers practical tips for considering these estimates in research."
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: RoBERTa
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "5 words"
CONFERENCE: "Preprint"
---
# Some Issues in Predictive Ethics Modeling: An Annotated Contrast Set of "Moral Stories"

## Metadata

**Authors:** Fitzgerald, Ben

**Year:** 2024

**Type:** document

## Links

- **Local PDF:** [[PDFs/2024/2024-Fitzgerald-Some Issues in Predictive Ethics Modeling.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2407.05244

## Abstract

Models like Delphi have been able to label ethical dilemmas as moral or immoral with astonishing accuracy. This paper challenges accuracy as a holistic metric for ethics modeling by identifying issues with translating moral dilemmas into text-based input. It demonstrates these issues with contrast sets that substantially reduce the performance of classifiers trained on the dataset Moral Stories. Ultimately, we obtain concrete estimates for how much specific forms of data misrepresentation harm classifier accuracy. Specifically, label-changing tweaks to the descriptive content of a situation (as small as 3-5 words) can reduce classifier accuracy to as low as 51%, almost half the initial accuracy of 99.8%. Associating situations with a misleading social norm lowers accuracy to 98.8%, while adding textual bias (i.e. an implication that a situation already fits a certain label) lowers accuracy to 77%. These results suggest not only that many ethics models have substantially overfit, but that several precautions are required to ensure that input accurately captures a moral dilemma. This paper recommends re-examining the structure of a social norm, training models to ask for context with defeasible reasoning, and filtering input for textual bias. Doing so not only gives us the first concrete estimates of the average cost to accuracy of misrepresenting ethics data, but gives researchers practical tips for considering these estimates in research.

## Authors

[[Ben Fitzgerald]]

## Data Description

The paper creates four contrast sets (norm swaps, textual bias, descriptive shifts, and demographic shifts) on the Moral Stories dataset to evaluate a fine-tuned RoBERTa classifier for predictive ethics modeling. The contrast sets comprise 851 annotated data points across 333 rows of the original dataset, testing how data misrepresentation (e.g., label-changing descriptive tweaks of 3-5 words) reduces classifier accuracy from 99.8% to as low as 51%.


## Notes

