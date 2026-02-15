---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y8WWMGMV
type: document
short_title: "Is Your Model Fairly Certain? Uncertainty-Aware"
year: 2025
first_author: "[[Yinong Oliver Wang]]"
last_author: "[[Nicholas Apostoloff]]"
authors: "Yinong Oliver Wang; Nivedha Sivakumar; Falaah Arif Khan; Rin Metcalf Susa; Adam Golinski; Natalie Mackraz; Barry-John Theobald; Luca Zappella; Nicholas Apostoloff"
url: "https://arxiv.org/abs/2505.23996"
external_pdf: "https://arxiv.org/pdf/2505.23996.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Introduced 'UCerF' (Uncertainty-Aware Fairness), a metric that penalizes models not just for being wrong, but for being *overconfidently* wrong about specific demographic groups."
significance: "Refines fairness evaluation by adding the dimension of uncertainty/calibration – a model that is 'unsure' about a stereotype is better than one that is 'certainly' wrong, even if accuracy is similar."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware.md"
abstract: "The recent rapid adoption of large language models (LLMs) highlights the critical need for benchmarking their fairness. Conventional fairness metrics, which focus on discrete accuracy-based evaluations (i.e., prediction correctness), fail to capture the implicit impact of model uncertainty (e.g., higher model confidence about one group over another despite similar accuracy). To address this limitation, we propose an uncertainty-aware fairness metric, UCerF, to enable a fine-grained evaluation..."
paper_summary: "Abstract: The recent rapid adoption of large language mod- els (LLMs) highlights the critical need for bench- marking their fairness. Conventional fairness met- rics, which focus on discrete accuracy-based eval | Overview: arXiv:2505.23996v1 [cs.CL] 29 May 2025 Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs Yinong Oliver Wang* 1 Nivedha Sivakumar 2 Falaah Arif Khan* 3 Rin Metcalf Susa 2 Ada | Key Findings: dataset X = {xi}N i=1, an uncertainty estimator fu(x; G), we first derive the model's certainty c by converting the uncertainty estimator. For simplic | Conclusions: Per-occupation fairness analysis. To better understand fairness composition, we break down fairness scores per occupation in Fig. 7. The x-axis labels"
local_pdf: "[[PDFs/2025/2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "31,756 samples"
LLM_assessed: "Llama-3, Mistral, Mixtral, Falcon"
DATA_URL: "https://github.com/apple/ml-synthbias"
---
# Is Your Model Fairly Certain? Uncertainty-Aware Fairness Evaluation for LLMs (UCerF)

## Metadata

**Authors:** Wang, Yinong Oliver; Sivakumar, Nivedha; Khan, Falaah Arif; Susa, Rin Metcalf; Golinski, Adam; Mackraz, Natalie; Theobald, Barry-John; Zappella, Luca; Apostoloff, Nicholas

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Wang-Is Your Model Fairly Certain Uncertainty-Aware.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2505.23996

## Abstract

The recent rapid adoption of large language models (LLMs) highlights the critical need for benchmarking their fairness. Conventional fairness metrics, which focus on discrete accuracy-based evaluations (i.e., prediction correctness), fail to capture the implicit impact of model uncertainty (e.g., higher model confidence about one group over another despite similar accuracy). To address this limitation, we propose an uncertainty-aware fairness metric, UCerF, to enable a fine-grained evaluation of model fairness that is more reflective of the internal bias in model decisions compared to conventional fairness measures. Furthermore, observing data size, diversity, and clarity issues in current datasets, we introduce a new gender-occupation fairness evaluation dataset with 31,756 samples for co-reference resolution, offering a more diverse and suitable dataset for evaluating modern LLMs. We establish a benchmark, using our metric and dataset, and apply it to evaluate the behavior of ten open-source LLMs. For example, Mistral-7B exhibits suboptimal fairness due to high confidence in incorrect predictions, a detail overlooked by Equalized Odds but captured by UCerF. Overall, our proposed LLM benchmark, which evaluates fairness with uncertainty awareness, paves the way for developing more transparent and accountable AI systems.

## Authors

[[Yinong Oliver Wang]], [[Nivedha Sivakumar]], [[Falaah Arif Khan]], [[Rin Metcalf Susa]], [[Adam Golinski]], [[Natalie Mackraz]], [[Barry-John Theobald]], [[Luca Zappella]], [[Nicholas Apostoloff]]

## Data Description

The paper introduces SynthBias, a large-scale synthetic dataset of 31,756 samples for gender-occupation co-reference resolution fairness evaluation, generated by GPT-4o and validated through human annotation. Ten open-source LLMs were benchmarked including Pythia-1B, Pythia-12B, AmberChat, AmberSafe, Mistral-7B-Instruct, Mixtral-8x7B-Instruct, Falcon-7B-Instruct, Falcon-40B-Instruct, Llama-3-8B-Instruct, and Llama-3-70B-Instruct, using the novel UCerF uncertainty-aware fairness metric alongside conventional accuracy and equalized odds measures.


## Notes


## Citation Info

41 citations (Semantic Scholar/arXiv) [2025-08-27]
