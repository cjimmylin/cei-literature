---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 236H7CQY
type: conferencePaper
short_title: "Backtracking for Safety"
year: 2025
first_author: "[[Bilgehan Sel]]"
last_author: "[[Siddhartha Reddy Jonnalagadda]]"
authors: "Bilgehan Sel; Dingcheng Li; Phillip Wallis; Vaishakh Keshava; Ming Jin; Siddhartha Reddy Jonnalagadda"
doi: 10.48550/arXiv.2503.08919
url: "http://arxiv.org/abs/2503.08919"
external_pdf: "http://arxiv.org/pdf/2503.08919.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Proposed a 'backtracking' method for safety alignment that allows models to revert to a safer generation state when a violation is detected during the generation process."
significance: "Enables targeted correction of toxicity or safety violations in real-time generation without discarding the entire output, offering a more efficient alternative to full resets for long-form content."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Sel-Backtracking for Safety.md"
abstract: "Large language models (LLMs) have demon- strated remarkable capabilities across various tasks, but ensuring their safety and alignment with human values remains crucial. Current safety alignment methods, such as supervised fine-tuning and reinforcement learning-based approaches, can exhibit vulnerabilities to adver- sarial attacks and often result in shallow safety alignment, primarily focusing on preventing harmful content in the initial tokens of the gen- erated output. While methods like rese"
paper_summary: "Abstract: Large language models (LLMs) have demon- strated remarkable capabilities across various tasks, but ensuring their safety and alignment with human values remains crucial. Current safety alignment metho | Overview: BSAFE: (B)acktracking for (SAFE)ty Bilgehan Sel Google, Virginia Tech Dingcheng Li Google Phillip Wallis Google Vaishakh Keshava Google Ming Jin † Virginia Tech Siddhartha Reddy Jonnalagadda † Google  | Methodology: enables targeted correction of problematic seg- ments without discarding the entire generated text, thereby preserving efficiency. We demon- strate th | Conclusions: We introduced BSAFE, a novel backtracking method that enhances large language model safety. BSAFE overcomes limitations of current tech- niques by ena"
local_pdf: "[[PDFs/2025/2025-Sel-Backtracking for Safety.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "Gemma, Llama-3"
DATA_URL: "NA"
---
# Backtracking for Safety

## Metadata

**Authors:** Sel, Bilgehan; Li, Dingcheng; Wallis, Phillip; Keshava, Vaishakh; Jin, Ming; Jonnalagadda, Siddhartha Reddy

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2503.08919](https://doi.org/10.48550/arXiv.2503.08919)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Sel-Backtracking for Safety.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.08919
- **DOI:** https://doi.org/10.48550/arXiv.2503.08919

## Abstract

Large language models (LLMs) have demonstrated remarkable capabilities across various tasks, but ensuring their safety and alignment with human values remains crucial. Current safety alignment methods, such as supervised fine-tuning and reinforcement learning-based approaches, can exhibit vulnerabilities to adversarial attacks and often result in shallow safety alignment, primarily focusing on preventing harmful content in the initial tokens of the generated output. While methods like resetting can help recover from unsafe generations by discarding previous tokens and restarting the generation process, they are not well-suited for addressing nuanced safety violations like toxicity that may arise within otherwise benign and lengthy generations. In this paper, we propose a novel backtracking method designed to address these limitations. Our method allows the model to revert to a safer generation state, not necessarily at the beginning, when safety violations occur during generation. This approach enables targeted correction of problematic segments without discarding the entire generated text, thereby preserving efficiency. We demonstrate that our method dramatically reduces toxicity appearing through the generation process with minimal impact to efficiency.

## Authors

[[Bilgehan Sel]], [[Dingcheng Li]], [[Phillip Wallis]], [[Vaishakh Keshava]], [[Ming Jin]], [[Siddhartha Reddy Jonnalagadda]]

## Data Description

The paper constructs a dataset of 128,000 question-answer pairs generated using the Gemma2 27B model, designed to simulate scenarios where LLM-generated text transitions from safe to unsafe content. The BSAFE method is evaluated on a 100-example test dataset for prefilling attacks and on the HEx-PHI benchmark (300 examples), testing Gemma 2 (2B, 9B) and LLaMA 3 (1B, 3B) models. Utility is evaluated using GSM8K and MATH benchmarks on Gemma2 9B and LLaMA3 8B.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
