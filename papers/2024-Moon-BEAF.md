---


Human View: true
Human View Date: 2026-01-24
Human View note: "Hallucination in VLM"
Not AI: 
key: 3R3QE4AR
type: document
short_title: BEAF
year: 2025
first_author: "[[Y. Moon]]"
last_author: "[[Oh, T]]"
authors: "[[Moon, Y.]]; [[Nam, H.]]; [[Choi, W.]]; [[Oh, T.]]"
url: "https://arxiv.org/abs/2407.13442"
local_pdf: "[[PDFs/2024/2024-Moon-BEAF.pdf]]"
external_pdf: "https://arxiv.org/pdf/2407.13442.pdf"
national_ethnic_cultural: American
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: American
pdf_extract: "PDF Extracts/2024/2024-Moon-BEAF.md"
tags: 
paper_summary: "Overview: BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-language Models Moon Ye-Bin1∗ Nam Hyeon-Woo1∗ Wonseok Choi2 Tae-Hyun Oh1,2,3 1Dept. of EE, POSTECH, Korea 2Grad. School of AI,  | Key Findings: benchmark. This benchmark comprises a dataset enhanced along the vision-axis and metrics that are aware of changes. We manipulate scenes by selectivel | Conclusions: We present a comprehensive analysis of hallucination using our BEAF bench- mark. Unlike conventional hallucination benchmarks that measure accuracy by"
abstract: "Vision language models (VLMs) perceive the world through a combination of a visual encoder and a large language model (LLM). The visual encoder, pre-trained on large-scale vision-text datasets, provides zero-shot generalization to visual data, and the LLM endows its high reasoning ability to VLMs. It leads VLMs to achieve high performance on wide benchmarks without fine-tuning, exhibiting zero or few-shot capability. However, recent studies show that VLMs are vulnerable to hallucination. This undesirable behavior degrades reliability and credibility, thereby making users unable to fully trust the output from VLMs. To enhance trustworthiness and better tackle the hallucination of VLMs, we curate a new evaluation dataset, called the BEfore-AFter hallucination dataset (BEAF), and introduce new metrics: True Understanding (TU), IGnorance (IG), StuBbornness (SB), and InDecision (ID). Unlike prior works that focus only on constructing questions and answers, the key idea of our benchmark is to manipulate visual scene information by image editing models and to design the metrics based on scene changes. This allows us to clearly assess whether VLMs correctly understand a given scene by observing the ability to perceive changes. We also visualize image-wise object relationship by virtue of our two-axis view: vision and text. Upon evaluating VLMs with our dataset, we observed that our metrics reveal different aspects of VLM hallucination that have not been reported before. Project page: \url{https://beafbench.github.io/}"
ethics_overall: No
virtue_ethics: Yes
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Truthfulness & Factuality"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for hallucination detection dataset"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://beafbench.github.io/"
---
 BEAF: Observing BEfore-AFter Changes to Evaluate Hallucination in Vision-language Models

## Authors

[[Moon, Y]], [[Nam, H]], [[Choi, W]], [[Oh, T]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Moon-BEAF.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2407.13442

## Abstract

Vision language models (VLMs) perceive the world through a combination of a visual encoder and a large language model (LLM). The visual encoder, pre-trained on large-scale vision-text datasets, provides zero-shot generalization to visual data, and the LLM endows its high reasoning ability to VLMs. It leads VLMs to achieve high performance on wide benchmarks without fine-tuning, exhibiting zero or few-shot capability. However, recent studies show that VLMs are vulnerable to hallucination. This undesirable behavior degrades reliability and credibility, thereby making users unable to fully trust the output from VLMs. To enhance trustworthiness and better tackle the hallucination of VLMs, we curate a new evaluation dataset, called the BEfore-AFter hallucination dataset (BEAF), and introduce new metrics: True Understanding (TU), IGnorance (IG), StuBbornness (SB), and InDecision (ID). Unlike prior works that focus only on constructing questions and answers, the key idea of our benchmark is to manipulate visual scene information by image editing models and to design the metrics based on scene changes. This allows us to clearly assess whether VLMs correctly understand a given scene by observing the ability to perceive changes. We also visualize image-wise object relationship by virtue of our two-axis view: vision and text. Upon evaluating VLMs with our dataset, we observed that our metrics reveal different aspects of VLM hallucination that have not been reported before. Project page: \url{https://beafbench.github.io/}

## Detailed Summary

This paper introduces **BEAF** (BEfore-AFter), a benchmark designed to evaluate hallucination in Vision-Language Models (VLMs) by testing their ability to perceive scene changes. Current VLM benchmarks often rely on text-only questions that can be answered through language priors ("Is there a cat in the room?"). BEAF moves the evaluation to the "vision-axis" by using image pairs where an object has been removed or altered using AI editing tools.

The authors categorize VLM errors into a new taxonomy: **True Understanding (TU)**, **IGnorance (IG)**, **StuBbornness (SB)**, and **InDecision (ID)**. Their research reveals that many models suffer from "Stubbornness"—they hallucinate the existence of an object in the "After" image simply because they saw it in the "Before" image, ignoring the visual evidence of the change.

## Paper Outline

1.  **Introduction**: VLMs vulnerabilities; The limits of text-axis hallucination metrics.
2.  **Related Work**: VLM Hallucination benchmarks; Contrastive evaluation.
3.  **BEAF Benchmark**:
    *   **Dataset Construction**: Instruction-based image editing (InstructPix2Pix).
    *   **The Metrics**: Defining TU, IG, SB, and ID.
4.  **Experiments**: Standard benchmark comparisons; Human validation.
5.  **Observations**: Visualization of object relationships in vision-text space.
6.  **Conclusion**: The importance of scene-change awareness for VLM reliability.

## Methods Summary

The authors create the BEAF dataset by manipulating source images ("Before") to create "After" images where specific objects are added, removed, or changed.
- **Image Editing**: They use image-to-image models guided by natural language prompts.
- **Evaluation Loop**: VLMs are asked the same question about both the "Before" and "After" images.
- **Metric Logic**: If a model answers "Yes" to both when an object was removed, it is marked as **Stubborn**. If it flips its answer correctly, it shows **True Understanding**.

## Results Summary

1.  **Failure of Priors**: VLMs frequently rely on language priors or their initial visual "imprint" rather than dynamic visual updates.
2.  **Metric Sensitivity**: The BEAF metrics (especially SB and ID) reveal reliability issues that standard accuracy scores miss.
3.  **Model Rankings**: Models like LLaVA-1.5 show better TU than earlier baselines but still struggle with high SB in complex scenes.

## Conclusions

Hallucination in VLMs is not just a failure of vision, but a failure to *update* beliefs based on new visual evidence. BEAF establishes that scene-change awareness is a crucial bottleneck for creating trustworthy multimodal agents.

## Artifact Contributions

*   **BEAF Hallucination Dataset**: A benchmark suite of Before/After image pairs.
*   **Evaluation Metrics (TU, IG, SB, ID)**: A new framework for measuring VLM consistency.

## Data Description

The paper introduces BEAF (BEfore-AFter), a hallucination evaluation benchmark for vision-language models. The dataset contains 2,227 images (500 original from MS-COCO and 1,727 manipulated via object removal/inpainting) with 26,118 image-question pairs. Four novel metrics (True Understanding, Ignorance, Stubbornness, InDecision) are proposed to assess VLM hallucination by tracking answer changes before and after visual scene manipulation.


## Notes


## Citation Info

792 citations (Semantic Scholar/arXiv) [2025-08-27]
