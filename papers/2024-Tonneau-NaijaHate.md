---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: M4GJQXAY
type: conferencePaper
short_title: NaijaHate
year: 2025
first_author: "[[Manuel Tonneau]]"
authors: "Manuel Tonneau; Pedro Vitor Quinta de Castro; Karim Lasri; Ibrahim Farouq; Lakshminarayanan Subramanian; Victor Orozco-Olvera; Samuel P. Fraiberger"
doi: 10.48550/arXiv.2403.19260
tags: 
url: "http://arxiv.org/abs/2403.19260"
external_pdf: "http://arxiv.org/pdf/2403.19260.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: "African/Ubuntu, American"
religious_values: N/A
moral_psychology: N/A
newtags: "African/Ubuntu, American, Toxicity & Hate Speech"
key_contribution: "Created NaijaHate, the first representative dataset for hate speech detection on Nigerian Twitter, and trained a domain-adapted model (NaijaXLM-T)."
significance: "Demonstrates that standard Western hate speech detectors fail on Nigerian dialects (Pidgin/English), proving the necessity of regionally representative datasets for global content moderation."
pdf_extract: "PDF Extracts/2024/2024-Tonneau-NaijaHate.md"
abstract: "To address the global issue of online hate, hate speech detection (HSD) systems are typi- cally developed on datasets from the United States, thereby failing to generalize to En- glish dialects from the Majority World. Fur- thermore, HSD models are often evaluated on non-representative samples, raising concerns about overestimating model performance in real-world settings. In this work, we intro- duce NAIJAHATE, the first dataset annotated for HSD which contains a representative sam- ple of Nige"
paper_summary: "Abstract: To address the global issue of online hate, hate speech detection (HSD) systems are typi- cally developed on datasets from the United States, thereby failing to generalize to En- glish dialects from t | Overview: NAIJAHATE: Evaluating Hate Speech Detection on Nigerian Twitter Using Representative Data Manuel Tonneau 1, 2, 3, Pedro Vitor Quinta de Castro 1, 4, Karim Lasri 1, 5, Ibrahim Farouq 1, 6, Lakshminaray | Methodology: (Lai et al., 2022), where a model flags content likely to infringe platform rules, which is then reviewed by humans who decide whether or not to moder | Key Findings: (Vidgen et al., 2020) or originate from largely un- moderated platforms, such as Gab (Kennedy et al., 2022), where hatred is much more prevalent and t | Conclusions: Performance overestimation We demonstrate that evaluating HSD on biased datasets leads to a large overestimation of real-world performance, the latter"
local_pdf: [[PDFs/2024/2024-Tonneau-NaijaHate.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach annotated dataset for hate speech detection"
data_metrics: "Not specified"
---
# NaijaHate: Evaluating Hate Speech Detection on Nigerian Twitter Using Representative Data

## Metadata

**Authors:** Tonneau, Manuel; Castro, Pedro Vitor Quinta de; Lasri, Karim; Farouq, Ibrahim; Subramanian, Lakshminarayanan; Orozco-Olvera, Victor; Fraiberger, Samuel P.

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2403.19260](https://doi.org/10.48550/arXiv.2403.19260)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Tonneau-NaijaHate.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2403.19260
- **DOI:** https://doi.org/10.48550/arXiv.2403.19260

## Abstract

To address the global issue of online hate, hate speech detection (HSD) systems are typically developed on datasets from the United States, thereby failing to generalize to English dialects from the Majority World. Furthermore, HSD models are often evaluated on non-representative samples, raising concerns about overestimating model performance in real-world settings. In this work, we introduce NAIJAHATE, the first dataset annotated for HSD which contains a representative sample of Nigerian tweets. We demonstrate that HSD evaluated on biased datasets traditionally used in the literature consistently overestimates real-world performance by at least two-fold. We then propose NAIJAXLM-T, a pretrained model tailored to the Nigerian Twitter context, and establish the key role played by domainadaptive pretraining and finetuning in maximizing HSD performance. Finally, owing to the modest performance of HSD systems in realworld conditions, we find that content moderators would need to review about ten thousand Nigerian tweets flagged as hateful daily to moderate 60% of all hateful content, highlighting the challenges of moderating hate speech at scale as social media usage continues to grow globally. Taken together, these results pave the way towards robust HSD systems and a better protection of social media users from hateful content in low-resource settings.

## Authors

[[Manuel Tonneau]], [[Pedro Vitor Quinta de Castro]], [[Karim Lasri]], [[Ibrahim Farouq]], [[Lakshminarayanan Subramanian]], [[Victor Orozco-Olvera]], [[Samuel P. Fraiberger]]

## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

13 citations (Semantic Scholar/DOI) [2025-08-27] 13 citations (Semantic Scholar/DOI) [2025-08-23]
