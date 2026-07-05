---
stem: "2022-Trager-The Moral Foundations Reddit Corpus"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, design-space]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 16123
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["Meta-Llama-3-8B", "Ministral-8B-Instruct-2410", "BERT"]
headline_numbers:
  - "MFRC contains 16,123 Reddit comments from 12 subreddits (p.1)"
  - "BERT (single-label) best F1 for Care: 0.62 ± 0.02, Purity: 0.51 ± 0.07 (p.6)"
  - "Zero-shot Llama (single) best F1 for Care: 0.40, worst for Purity: 0.17 (p.6)"
  - "Cross-corpus BERT trained on MFRC → MFTC: Care F1 0.53, Purity F1 0.28 (p.7)"
---
## 1. Gist
The Moral Foundations Reddit Corpus (MFRC) is a 16,123-comment dataset drawn from 12 Reddit subreddits, hand-annotated by trained undergraduate annotators for 8 moral-sentiment categories based on the revised Moral Foundations Theory (MFT). Unlike its predecessor, the Moral Foundations Twitter Corpus (MFTC), the MFRC uses the updated taxonomy that splits "Fairness" into separate "Equality" and "Proportionality" foundations, and it introduces Reddit as a platform source — offering longer posts, distinct community cultures, and broader topical diversity. The paper establishes this corpus as both a moral sentiment classification benchmark and an AI alignment evaluation resource by evaluating LLMs (Llama-3-8B, Ministral-8B) in zero-shot, few-shot, and PEFT settings alongside fine-tuned BERT baselines, demonstrating that LLMs still lag behind fine-tuned encoders on this subjective task.

## 2. Benchmark/eval design features
The corpus measures eight moral-sentiment categories: Care, Equality, Proportionality, Loyalty, Authority, Purity, Thin Morality, and an Implicit/Explicit morality indicator. The item structure is multi-label at the comment level — each comment may receive multiple moral labels simultaneously. The annotation scheme relies on majority vote (≥50% of at least three annotators per comment). The corpus spans three topical buckets: US Politics, French Politics, and Everyday Morality, collected from subreddits including r/AmItheAsshole, r/politics, r/confession, r/europe, and others. The baseline evaluation uses single-label and multi-label classification with F1 scores measured via stratified 5-fold cross-validation. Cross-corpus transfer experiments test generalization between MFRC and MFTC.

## 3. Task format & example item
The classification task asks models to identify which moral foundations are expressed in a Reddit comment. No verbatim example item is provided in the extract; Table 2 gives frequency counts per subreddit but no quoted Reddit text for illustration. n/a (no sample item quoted in extract).

## 4. Scoring / grading methodology
Primary metric is F1 score (mean ± standard deviation across 5-fold cross-validation). For single-label classification, binary F1 is used for model selection. For multi-label, macro F1 guides selection. Inter-annotator agreement is measured via Fleiss's kappa and PABAK (prevalence-and-bias-adjusted kappa). Raw kappas are low due to low base rates of moral language; PABAK shows medium to high agreement after adjusting for prevalence.

## 5. Dataset construction & provenance
Comments were scraped from Reddit using keyword/score filters: minimum 10 tokens, comment score ≥10, and a semi-supervised moral-loading upsampling procedure using DDR (distributed dictionary representation) word embeddings and MFT seed words. 50% of comments have high moral loading (>95th percentile), 50% have lower loading. After deduplication, the final corpus contains 16,123 comments: US Politics 4,821; French Politics 6,489; Everyday Morality 4,813. Five expert annotators (selected from 27 undergraduates after two months of training) annotated each comment. The corpus will be released as a HuggingFace dataset. No license information is stated in the extract.

## 6. Validity evidence
Inter-annotator agreement: Fleiss's kappa is generally low due to low prevalence of moral language across subreddits; PABAK scores show medium-to-high agreement once adjusted. Annotator demographic and psychological metadata (political ideology, MFQ-2 scores, income, gender, religion) are collected to facilitate future bias research. The paper notes annotators' political ideology skews liberal. Cross-corpus experiments demonstrate partial transferability between MFRC and MFTC, supporting construct validity across platforms.

## 7. Saturation / discrimination
Best-performing BERT (single-label) achieves F1 of 0.62 for Care and only 0.51 for Purity (p.6), indicating substantial headroom. LLMs in zero-shot and few-shot settings peak at F1 ~0.40–0.44 for Care, near 0.10–0.21 for Purity and Proportionality (p.6). Purity and Proportionality are the most difficult categories, consistent with their low base rates in the corpus. The French Politics bucket shows notably weaker performance than Everyday and US Politics buckets.

## 8. Multiturn / agentic aspects
n/a — this is a static classification benchmark with no interactive or multi-turn components.

## 9. Key numbers
- 16,123 total Reddit comments across 12 subreddits (p.2)
- 5 trained annotators selected from 27 initial (p.4)
- Each comment annotated by at least 3 annotators (p.3)
- BERT single-label F1: Care 0.62±0.02, Equality 0.58±0.03, Proportionality 0.37±0.04, Purity 0.51±0.07, Thin Morality 0.39±0.02 (p.6)
- Zero-shot Llama single-label F1: Care 0.40, Equality 0.29, Proportionality 0.21, Purity 0.17, Thin Morality 0.23 (p.6)
- BERT trained on MFTC: Fairness F1 0.82±0.01, Care 0.75±0.02, Purity 0.54±0.04 (p.7)
- Cross-corpus BERT (MFRC→MFTC): Care F1 0.53, Purity F1 0.28 (p.7)
- PEFT Llama multi-label: Care 0.53±0.013, Loyalty 0.40±0.016 (p.6)

## 10. Pitfalls & limitations
- Corpus biases acknowledged: English-only, Reddit-specific, researchers' curation criteria, MFT framework biases, and annotators are all undergraduate research assistants at a private institute with liberal-leaning politics and above-average income (p.8).
- Purity, Loyalty, and Proportionality have very low base rates, making F1 scores highly unstable.
- The MFTC uses the older Fairness category (not split into Equality/Proportionality), complicating cross-corpus comparisons.
- All annotations are majority-vote rather than preserving individual annotator disagreements, potentially losing signal about subjective diversity.
- LLMs "continue to lag behind fine-tuned encoders on this subjective task" (p.1) — the benchmark is not yet close to saturation.

## 11. Novel ideas worth stealing
- **Annotator metadata as a research object**: collecting demographic and psychological profiles of annotators (political ideology, MFQ-2, income, gender, religion) alongside annotations enables future bias audits and annotator-characteristic studies — directly applicable to values-alignment benchmarks where annotator diversity matters.
- **Semi-supervised moral upsampling**: using DDR word embeddings with MFT seed words to compute moral loading scores and then sampling to achieve a 50/50 split between high-loading and moderate-loading comments is an efficient way to ensure meaningful moral content without purely random sampling.
- **Implicit/Explicit morality as a separate label**: tagging whether moral sentiment is expressed implicitly vs. explicitly gives a meta-dimension useful for evaluating model sensitivity to subtle moral language.
- **Thin Morality category**: a residual "moral judgment without a specific foundation" category captures moralized language that doesn't fit standard frameworks — useful as a catch-all for evaluating moral language recognition.
- **Cross-platform transfer evaluation**: systematically testing whether models trained on one social platform generalize to another is a validity check that values benchmarks should adopt.

## 12. Notable quotes
- "The results show that LLMs continue to lag behind fine-tuned encoders on this subjective task, underscoring the ongoing need for human-annotated moral corpora for AI alignment evaluation." (p.1)
- "A focus on maximizing annotator agreement risks artificially inflating agreement at the cost of suppressing the natural variability of moral sentiment." (p.4)
- "Fine-tuned models (BERT and PEFT-Llama) substantially outperform the zero-shot and few-shot baselines across all moral categories on MFRC... reinforcing the value of large, human-annotated corpora for both evaluation and downstream alignment work." (p.7)
- "In an age where political movements, grassroots activism, and plans for insurrections seem to take place in online environments, it is vital that we can better understand the moral dynamics of these online conversations." (p.8)

## 13. UNKNOWN / not in extract
- Exact release date or current HuggingFace dataset URL
- Full annotation manual content (noted as Supplementary Materials)
- Complete recall and precision tables (mentioned as forthcoming in appendix)
- Licensing terms for the dataset
- Whether inter-annotator agreement was computed before or after training sessions resolved disagreements
