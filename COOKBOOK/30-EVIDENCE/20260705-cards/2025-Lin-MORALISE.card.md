---
stem: "2025-Lin-MORALISE"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, saturation-discrimination, best-practices]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 2481
dataset_construction: "scraped"
languages: [en]
models_tested: [GPT-4o, GPT-4o-mini, o4-mini, Gemma3-4B, Gemma3-12B, Gemma3-27B, GLM4-V-9B, InternVL3-2B, InternVL3-8B, InternVL3-14B, InternVL3-38B, LLaVA-7B, LLaVA-NeXT-7B, Phi-3.5-vision, Qwen2-VL-2B, Qwen2-VL-7B, Qwen2.5-VL-3B, Qwen2.5-VL-7B, Qwen2.5-VL-32B]
headline_numbers: ["2,481 expert-verified real-world image-text pairs across 13 moral topics (p.1)", "19 VLMs evaluated (p.1)", "Moral judgment: proprietary avg 88.28 vs open-source 83.55 accuracy (p.7)", "Norm attribution hit rate: proprietary avg 66.60 vs open-source 42.63 (p.7)", "GPT-o4-mini best on norm attribution multi-norm F1 (p.8); GPT-4o only 42.32 F1 on Respect (p.7)", "Best judgment model GPT-o4-mini 89.04 avg (p.6)"]
---
## 1. Gist
MORALISE is a structured multimodal benchmark for evaluating the moral alignment of vision-language models (VLMs) using real-world, expert-verified image-text pairs (no AI-generated images). It matters for values-alignment benchmarking because it (a) grounds its 13-topic taxonomy in Turiel's Domain Theory (personal / interpersonal / societal domains), operationalizing a moral-psychology framework into an evaluable structure; (b) introduces modality-centric annotation — labeling whether a moral violation is conveyed through the image or the text — enabling diagnosis of which modality drives a model's moral judgment; and (c) demonstrates a large discrimination gap between coarse binary moral judgment (~85-88% accuracy) and fine-grained norm attribution (~42-66%), showing substantial headroom. It is a discriminating, realistic moral benchmark that surfaces where SOTA VLMs still fail.

## 2. Benchmark/eval design features
Constructs: moral awareness (is behavior wrong?) and moral reasoning (which norm is violated?). Taxonomy: 3 Turiel domains → 13 fine-grained topics — Personal: Integrity, Sanctity; Interpersonal: Care, Harm, Fairness, Reciprocity, Loyalty, Discrimination; Societal: Authority, Justice, Liberty, Respect, Responsibility (p.3-4). Each of 2,481 image-text pairs has two annotation types: (1) topic annotation (which moral topic(s) violated, multi-label), and (2) modality annotation (violation arises from image vs. text) (p.1). Two tasks: Moral Judgment (binary MCQ) and Moral Norm Attribution (identify violated topic from 13 + "Not morally wrong"). Three scored subtasks: S1 binary accuracy; S2 single-norm hit rate; S3 multi-norm F1 over 13 topics (p.6).

## 3. Task format & example item
Moral Judgment (p.5): model jointly considers image + text and answers "(a) Not morally wrong" or "(b) Morally wrong". Example scenarios (Figure 2, p.4): Integrity — "A job candidate lies about their skills in an interview"; Harm — "A man locks a dog in a car on a hot day"; Fairness — "A doctor prioritizes wealth over urgency"; Discrimination — "Training sessions are offered only to employees under 35." Moral Norm Attribution (p.5): given definitions of all 13 topics, model names the primary violated topic(s), with "Not morally wrong" option for neutral examples.

## 4. Scoring / grading methodology
Exact-match against gold labels. S1: binary classification accuracy. S2 (single-norm): hit rate — whether the single predicted topic appears among gold-standard labels. S3 (multi-norm): F1 over the 13 moral topics for predicting all applicable violated topics (p.6). Both the choice letter (e.g., "a") and full response text (e.g., "Justice") accepted as valid. Temperature 0, output capped at 64 tokens (p.6).

## 5. Dataset construction & provenance
2,481 real-world image-text pairs manually curated by graduate-student annotators in ML fields (p.4). Images scraped from Pinterest, Reddit, Google Search; annotators rigorously filter out AI-generated content to ensure authenticity (p.4). Minimum 50 pairs per (topic × violation-type); each topic spans ≥5 distinct real-world contexts (e.g., Care spans schools, hospitals, refugee shelters, nursing homes, workplaces) (p.5). Moral norm refinement via majority-vote protocol among annotators to discard low-quality examples and determine representative topics; multi-label scheme when a pair satisfies multiple topics (p.5). Publicly released on HuggingFace (Ze1025/MORALISE) (p.1). Balanced across topics (Appendix A, not in extract).

## 6. Validity evidence
Content validity grounded in Turiel's Domain Theory and moral-psychology follow-up literature (p.3). Human expertise: all annotations by graduate students; majority-vote refinement provides a form of inter-annotator agreement, though no numeric IRR coefficient in extract. Modality-centric labels enable criterion analysis of visual vs. textual moral cues. No formal human performance baseline reported in extract.

## 7. Saturation / discrimination
Strong discrimination. Moral judgment near-ceiling for top models (GPT-o4-mini 89.04, Qwen2.5-VL-7B/32B 89.35) but norm attribution far from ceiling: proprietary avg hit rate 66.60, open-source 42.63 (p.7). Multi-norm F1 even lower (proprietary avg ~52.90, p.8). Large per-topic spread: even GPT-4o scores only 42.32 F1 on Respect (p.7). Weak topics (liberty, respect, reciprocity) leave substantial headroom; common norms (harm, justice, integrity) easier (p.7). Small open models (LLaVA-7B 65.33 judgment; Qwen2.5-VL-3B 12.09 hit rate) show wide performance range across scale (p.6).

## 8. Multiturn / agentic aspects
n/a — single-turn multimodal MCQ; no tool use or interaction.

## 9. Key numbers
- 2,481 image-text pairs, 13 topics, 3 domains, 2 modality types (p.1)
- 19 VLMs (3 proprietary OpenAI + 16 open-source) (p.5)
- Moral judgment avg accuracy: proprietary 88.28, open-source 83.55 (p.6-7)
- Best judgment: GPT-o4-mini 89.04, GPT-4o-mini 88.80, GPT-4o 87.01 (p.6)
- Norm attribution single-norm hit: proprietary 66.60, open-source 42.63 (p.7); best GPT-o4-mini 72.77 (p.6)
- Multi-norm F1: GPT-4o 56.52, GPT-o4-mini 56.04 (p.8)
- GPT-4o Respect F1 only 42.32 (p.7)
- Weakest overall: LLaVA-7B judgment 65.33 (p.6), Qwen2.5-VL-3B hit rate 12.09 (p.6)
- ≥50 pairs per topic×violation-type, ≥5 contexts per topic (p.5)

## 10. Pitfalls & limitations
Extract-visible: English-only, US/Western-centric image sources (Pinterest/Reddit/Google) — limits cultural generalization despite moral-psychology grounding. Annotators are ML graduate students, not moral-philosophy or demographically diverse raters — possible narrow value perspective; no reported IRR numbers. Some anomalous per-topic scores (e.g., Qwen2-VL-2B scoring 100.00 on Harm single-norm hit, p.6-7; LLaVA-7B 97.27 on Justice) suggest label-frequency artifacts or degenerate guessing rather than true competence. Binary judgment near ceiling limits its long-term discriminative value. Multi-label gold sets make hit-rate inflatable (any-of-many match). Excludes text-only reasoning models (DeepSeek R1, Qwen3) that lack image input (p.6).

## 11. Novel ideas worth stealing
- **Modality-attribution annotation**: label whether a moral violation is carried by image vs. text, enabling a benchmark to diagnose WHICH input channel drives (or fails) a model's moral judgment. Directly portable to any multimodal or even multi-source values benchmark.
- **Two-tier task design (binary judgment → fine-grained norm attribution)** as a built-in difficulty gradient that avoids ceiling saturation: the easy task confirms basic competence while the hard task preserves headroom and discrimination.
- **Turiel Domain Theory as taxonomy scaffold** — separating inherently moral violations from social-conventional ones, testing a model's ability to make that distinction (a psychometrically grounded construct rather than ad-hoc categories).
- **Real-image-only provenance with explicit anti-AI-generation filtering** — a reusable quality-control stance to avoid distributional bias and stylistic artifacts of synthetic images.
- **Minimum-per-cell quotas (≥50 pairs per topic×modality, ≥5 contexts per topic)** to enforce balance and diversity — a concrete construction recipe.
- **Multi-label with majority-vote refinement** to handle genuinely poly-normative scenarios, plus reporting both single-norm hit and multi-norm F1 to separate "found any right norm" from "found all right norms."

## 12. Notable quotes
- "we introduce MORALISE, a comprehensive benchmark for evaluating the moral alignment of vision-language models (VLMs) using diverse, expert-verified real-world data." (p.1)
- "we distinguish two types of moral violations: (1) those primarily conveyed through text, and (2) those primarily conveyed through images." (p.1)
- "the proprietary/open-source models achieved an average of 88.28/83.55 accuracy in moral judgement, but only an average of 66.60/42.63 hit rate in norm attribution." (p.7)
- "Norms that are more frequently emphasized in social discourse, e.g., harm/justice, are better captured. Less-discussed topics deserve additional attention in efforts toward moral alignment." (p.7)

## 13. UNKNOWN / not in extract
- Detailed dataset statistics / exact per-cell counts (Appendix A)
- Full prompt templates (Appendix B.1)
- Inter-annotator reliability numeric values
- RQ4 and any modality-sensitivity numeric analysis beyond p.7
- Table 4 full multi-norm F1 rows for all open-source models
- Licensing terms of scraped images
- Human performance baseline (if any)
