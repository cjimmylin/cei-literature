---
stem: "2023-Soemer-Antisemitic Messages A Guide to High-Quality"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, cultural-linguistic]
task_format: "forced-choice"
scoring_type: "human-rating"
dataset_size: 6941
dataset_construction: "mixed"
languages: [en]
models_tested: []
headline_numbers: ["6,941 tweets labeled; 1,250 (18%) antisemitic per IHRA definition (p.4-5)", "Pre-discussion Cohen's kappa 0.66 (p.6)", "ZioNazi* slur tweets 88% antisemitic vs kikes slur 34% antisemitic (p.5)"]
---
## 1. Gist
This paper presents a high-quality annotation methodology and a labeled dataset of 6,941 English tweets (2019-2021) about Jews, Israel, and antisemitism, of which 1,250 (18%) are labeled antisemitic under the IHRA Working Definition. Though built for supervised hate-speech classification rather than LLM benchmarking, it is highly relevant to values-alignment evaluation because it demonstrates a rigorous, definition-anchored annotation procedure for a deeply subjective and culturally contested normative construct (what counts as antisemitism). Its core methodological innovations — forcing annotators to cite the specific clause of a shared definition, allowing recorded personal disagreement with that definition, and resolving all disagreements through discussion rather than reporting raw kappa — are directly transferable to building gold-standard values benchmarks where "correct" labels are contested.

## 2. Benchmark/eval design features
Construct measured: whether a tweet is antisemitic according to the IHRA Working Definition (binary in the published set). The definition is decomposed into 12 paragraphs, each addressing a distinct form/trope of antisemitism (p.3). Annotators must (a) rate confidence on a 5-point scale ("confident antisemitic," "probably antisemitic," "probably not," "confident not," "don't know"), (b) if antisemitic, select the applicable IHRA paragraph, (c) rate 5-point sentiment toward Jews/Judaism/Israel, and (d) flag auxiliary attributes: calling-out, reporting, sarcasm, Holocaust-relatedness, and Holocaust distortion (p.3-4). Answer space for the released label is binary (antisemitic / not).

## 3. Task format & example item
No individual tweet text is reproduced verbatim in the extract (screenshots referenced in Figure 1, not transcribed). The only quoted example is the illustrative ChatGPT-failure message: "Fox News trashes Georges Soros while praising Joe Rogan using some antisemitic tropes – puppet master using his money to control the world..." (p.1). Annotator answer format is a drop-down forced choice from five confidence categories plus mandatory IHRA-clause selection (p.3).

## 4. Scoring / grading methodology
Human expert annotation. Two annotators independently label each of 18 samples; ratings dichotomized (confident/probably not + "don't know" → not antisemitic; probably/confident antisemitic → antisemitic) (p.4-5). Disagreements are discussed to consensus; tweets not reaching agreement are excluded from the released set (p.4). Only tweets with 100% post-discussion agreement are published (p.6).

## 5. Dataset construction & provenance
Source: Indiana University OSoMe database (10% sample of live tweets). Keywords: "Jews" and "Israel" (broad) plus slurs "ZioNazi*" and "kikes" (targeted for antisemitic content). 14 queries across time windows; 2,000 tweets randomly sampled per query, filtered to English via Google language detection, 500 randomly selected; 18 total samples (p.3). Final published set: 6,941 tweets. Composition: 66% "Jews," 22% "Israel," 8% ZioNazi*, 4% kikes (p.5). Released with IDs and text on Zenodo (Jikeli et al. 2023); usernames not anonymized (p.2). Eight expert annotators trained on antisemitism.

## 6. Validity evidence
Inter-rater reliability: pre-discussion overall Cohen's kappa = 0.66, varying by sample and lower for skewed distributions (p.4, p.6). Authors argue kappa is inappropriate here because their consensus-discussion process violates the independence assumption; post-discussion agreement approaches 100% by construction (p.4, p.6). Content validity anchored in the externally endorsed IHRA definition (30+ governments/organizations). Construct discipline enforced by mandatory clause-citation and the disagree-with-definition option (p.3-4).

## 7. Saturation / discrimination
Base rates vary widely by keyword sample, from 5.6% (Jews Sep-Dec 2021) to 89.3% (ZioNazi* 2019) antisemitic (Table 1, p.4-5), showing the keyword sampling strategy produces strong discrimination in class prevalence. No model accuracy/ceiling numbers reported — dataset "now awaiting testing" (p.5), so classifier headroom is undetermined in this extract.

## 8. Multiturn / agentic aspects
n/a. Annotators are prompted to view the full thread, replies, likes, and links in the tweet's "natural" context when unsure (p.3), but there is no multiturn model interaction.

## 9. Key numbers
- 6,941 tweets total; 1,250 (18%) antisemitic per IHRA (p.4-5)
- Temporal split: 1,499 (22%) 2019, 3,716 (54%) 2020, 1,726 (25%) 2021 (p.5)
- Keyword breakdown: Jews 4,605 (66%), Israel 1,524 (22%), ZioNazi* 529 (8%), kikes 283 (4%) (p.5)
- Antisemitic rate by keyword: Jews 11% (483), Israel 13% (203), ZioNazi* 88% (467/529), kikes 34% (97) (p.5)
- Pre-discussion Cohen's kappa = 0.66 (p.4, p.6)
- 8 expert annotators, 2 per sample, 18 samples (p.3)
- 9 tweets corrected for antisemitic/calling-out overlap before publication (p.4-5)

## 10. Pitfalls & limitations
Author-admitted: not comprehensive; English-only; Twitter-only; window ends before May 2021 Israel-Palestine flare-up (p.1, p.5). Kappa of 0.66 pre-discussion is only moderate, and the "100% agreement" figure is an artifact of the consensus process, not independent reliability (p.6). Analyst-visible: consensus discussion risks anchoring/groupthink and inflates apparent agreement; excluding unresolved tweets biases the set toward "easy" cases, potentially reducing hard-item difficulty; usernames not anonymized raises ethics concerns; "calling out" label admitted inconsistent and being relabeled (p.4). Keyword-driven sampling over-represents slur-laden discourse relative to organic prevalence.

## 11. Novel ideas worth stealing
- Mandatory clause-citation: to label an item as violating a norm, the annotator must select which specific clause of a shared definition applies — forces application of the shared standard over private intuition (p.3-4). Directly reusable for values benchmarks anchored to a rubric.
- Recorded personal disagreement: annotators may label per the definition while flagging that they personally disagree in that case (or vice versa) — cleanly separates "the standard says X" from "I believe X," preserving pluralism data without corrupting the gold label (p.3-4).
- Sentiment side-channel: a parallel 5-point sentiment rating lets annotators register negativity even when no definitional clause fits, capturing near-miss signal (p.4).
- Consensus-with-discussion over raw kappa: honest acknowledgment that discussion invalidates kappa, plus weekly difficult-item review meetings, is a defensible model for hard subjective constructs (p.4, p.6).
- Auxiliary "calling-out / reporting / sarcasm / Holocaust-distortion" flags to reduce false positives — a template for distinguishing meta-discussion of a harm from the harm itself, critical for any safety benchmark (p.1, p.4).

## 12. Notable quotes
- "Our annotation process aims to strictly apply a commonly used definition of antisemitism by forcing annotators to specify which part of the definition applies, and by giving them the option to personally disagree with the definition on a case-by-case basis." (p.1)
- "Kappa does not seem appropriate for measuring annotation reliability for our dataset, and perhaps for social data annotation in general." (p.4)
- "The option to personally disagree with the definition on a case-by-case basis is intended to encourage a stricter application of the IHRA definition rather than the individual definitions of the annotators." (p.4)
- "Labeling tweets that call out antisemitism, report antisemitism, or are otherwise related to antisemitism (such as the Holocaust) but are not actually antisemitic can help reduce false positives in automated detection." (p.1)

## 13. UNKNOWN / not in extract
- No model/classifier accuracy, F1, or benchmark results (dataset "awaiting testing," p.5).
- No verbatim dataset tweet items or the full 12-paragraph IHRA decomposition text.
- Licensing terms of the Zenodo release not stated in extract.
- Number/identity of models beyond the anecdotal ChatGPT mention; no systematic model evaluation.
- Per-annotator agreement breakdown and how ties/"don't know" were adjudicated beyond the dichotomization rule.
