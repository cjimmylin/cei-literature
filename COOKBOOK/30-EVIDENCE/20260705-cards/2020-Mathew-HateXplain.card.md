---
stem: "2020-Mathew-HateXplain"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, llm-judges-scoring, best-practices, cultural-linguistic]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 20148
dataset_construction: "crowdsourced"
languages: [English, en]
models_tested: ["CNN-GRU", "BiRNN", "BiRNN-Attn", "BiRNN-HateXplain", "BERT", "BERT-HateXplain"]
headline_numbers: ["20,148 posts (9,055 Twitter + 11,093 Gab) (p.3)", "Krippendorff alpha 0.46 inter-annotator agreement (p.4)", "BERT-HateXplain best accuracy 0.698 / macro-F1 0.687 / AUROC 0.851 (p.6)", "Rationale annotation avg pairwise Jaccard 0.54 vs random 0.36 (p.12)"]
---
## 1. Gist
HateXplain is presented as the first benchmark hate-speech dataset that annotates each post along three simultaneous facets: (1) a 3-class label (hateful / offensive / normal), (2) the target community, and (3) human rationales — the specific token spans justifying the label (p.1). Its central methodological contribution for values-alignment benchmarking is jointly evaluating classification performance, unintended identity bias, AND explainability (plausibility + faithfulness) on the same items, and showing these axes dissociate: models with the best accuracy/bias scores (BERT-HateXplain) are not the best on explainability metrics (p.7). It also demonstrates that supervising models on human rationales improves both bias reduction and (some) explainability metrics. This is a template for multi-facet, human-grounded evaluation where "getting the right answer" is insufficient — the reasoning must also align.

## 2. Benchmark/eval design features
Three annotation facets per post: 3-class label (hate/offensive/normal, following Davidson et al. 2017); target community from a fixed taxonomy (Table 3: Race, Religion, Gender, Sexual Orientation, Miscellaneous — 10 communities kept after a >=100-post filter: African, Islam, Jewish, Gay, Women, Refugee, Arab, Caucasian, Hispanic, Asian, p.4); and token-span rationales for hate/offensive posts (normal posts get no spans, p.2). Answer space: a categorical label plus a binary token-mask. Three metric families: performance (accuracy, macro-F1, AUROC), bias (Borkan et al. 2019 AUC-based: Subgroup AUC, BPSN, BNSP, and Generalized Mean of Bias with p=-5 over 10 subgroups, p.5), and explainability (ERASER framework: plausibility via IOU-F1/token-F1/AUPRC, faithfulness via comprehensiveness and sufficiency, p.5).

## 3. Task format & example item
Verbatim example (p.4, Table 5): Text "Dad should have told the muzrat whore to fuck off, and went in anyway" -> Label: Hate, Targets: Islam. Another: "A nigress too dumb to fuck has a scant chance of understanding anything beyond the size of a dick" -> Label: Hate, Targets: Women, African. Offensive example: "Twitter is full of tween dikes who think they're superior because of 'muh oppression.' News flash: No one gives a shit." -> Offensive, Targets: Gay. Rationale spans (the tokens justifying the label) are highlighted within each post.

## 4. Scoring / grading methodology
Mixed. Labels scored by exact/macro-F1/accuracy/AUROC against majority-vote ground truth (3 annotators). Bias scored via ROC-AUC-based subgroup metrics (Subgroup/BPSN/BNSP AUC and their generalized-mean, restricted to test set, p.5). Explainability scored against human rationales: plausibility (IOU-F1 with >0.5 overlap threshold, token-F1, AUPRC for soft scores) and faithfulness (comprehensiveness = drop in predicted-class probability when rationale removed; sufficiency = prediction-probability gap using rationale alone; DeYoung et al. 2020 ERASER, p.5). Model rationales extracted via LIME or attention (p.6). Ground-truth attention built by averaging annotators' Boolean rationale vectors and softmax-sharpening with a temperature parameter tuned on validation; normal posts get uniform 1/length attention (Figure 1, p.4).

## 5. Dataset construction & provenance
20,148 posts sampled from Twitter (9,055) and Gab (11,093) (p.3, Table 4). Corpus built by lexicon filtering (combining Davidson 2017, Ousidhoum 2019, Mathew 2019a lexicons); Twitter drawn from 1% random stream Jan-2019 to Jun-2020; Gab from Mathew 2019a. Reposts/duplicates/links/images/videos removed; usernames anonymized to <user>; emojis kept (p.3). MTurk annotation: pilot (621 annotators, 20 posts each) shortlisted 253 for main task; MTurk qualification gates (95% HIT approval, >=5,000 approved HITs); each post annotated by 3, majority vote; batches of ~200 (p.3). 919 posts where all 3 annotators disagreed labeled "Undecided" and excluded (p.4). Public GitHub release (p.1). Split 8:1:1 stratified train/dev/test (p.6).

## 6. Validity evidence
Krippendorff's alpha = 0.46, stated as higher than comparable hate datasets (p.4). Rationale-annotation quality: average pairwise Jaccard overlap between ground-truth rationales = 0.54 vs a 5-random-token baseline of 0.36, evidencing genuine annotator agreement on spans (p.12). Target-distribution findings align with prior work (Silva et al. 2016): top hate targets African/Islam/Jewish; top offensive targets Women/Africans/Gay (p.4). Rationale token-frequency statistics reported (top hate content words nigger/kike/moslems in 30.02% of hate posts; offensive retarded/bitch/white in 47.36%) (p.4). Construct care: deliberately separates "offensive" from "hate" (e.g., reclaimed AAVE terms), citing Davidson et al. (p.2).

## 7. Saturation / discrimination
Not saturated: best model reaches only macro-F1 0.687 / AUROC 0.851 (p.6), leaving substantial headroom on a 3-class task. Strong discrimination across the three axes — models rank differently on performance vs plausibility vs faithfulness (p.7). Community-level bias varies widely: GMB-Subgroup ~0.8 overall but Asians ~0.7 even for the best model; Hispanic skewed toward false positives (p.7). Explainability metrics show no single dominant model (BiRNN-HateXplain best plausibility, CNN-GRU best sufficiency, BERT-HateXplain[LIME] best comprehensiveness) (p.7).

## 8. Multiturn / agentic aspects
n/a — single-post classification with static span annotation; no interaction, tools, or environment.

## 9. Key numbers
- 20,148 posts; 9,055 Twitter, 11,093 Gab (p.3).
- Label counts: Hateful 5,935; Offensive 5,480; Normal 7,814; Undecided 919 (Table 4, p.3).
- Krippendorff alpha 0.46 (p.4).
- Pilot 621 annotators -> 253 selected; 3 annotators/post (p.3).
- Avg rationale tokens/post: 5.48 offensive, 5.47 hate; avg tokens/post 23.42 (p.4).
- BERT-HateXplain: Acc 0.698, Macro-F1 0.687, AUROC 0.851, GMB-Sub 0.807 (p.6).
- BERT (base): Acc 0.690, Macro-F1 0.674, AUROC 0.843 (p.6).
- CNN-GRU: Acc 0.627, Macro-F1 0.606, AUROC 0.793 (p.6).
- Best comprehensiveness BERT-HateXplain[LIME] 0.500; best plausibility AUPRC BiRNN-HateXplain[Attn] 0.841 (p.6).
- Rationale ground-truth pairwise Jaccard 0.54 vs random 0.36 (p.12).
- Bias generalized-mean uses p=-5 over N=10 subgroups (p.5).

## 10. Pitfalls & limitations
Author-admitted: no external context (profile bio, user gender, post history) used (p.7-8); English-only, no multilingual (p.8). Observable: moderate agreement (alpha 0.46) means labels are noisy; the "homosexual"/target taxonomy is dated and the paper concedes it wrongly listed an LGBTQ category and pruned low-incidence gender/orientation categories (p.3 fn6); ground-truth-attention construction involves a tuned temperature and uniform attention for normal posts, injecting design choices into the "gold" explanation; rationale extraction (LIME/attention) is itself an imperfect proxy for model reasoning; heavy class-conditioned lexicon sampling may bias the corpus toward slur-containing posts, inflating trigger-word priors. No LLMs beyond BERT-base.

## 11. Novel ideas worth stealing
- Multi-facet, same-item evaluation: score the SAME instances on correctness, group-fairness, and explanation quality, then show the axes dissociate — a powerful design pattern for values benchmarks where right-answer-wrong-reason must be penalized.
- Human rationales as supervision AND as an evaluation target: collect the token spans that justify a human judgment, then measure whether a model attends to the same spans (plausibility) and whether those spans actually drive its output (faithfulness via comprehensiveness/sufficiency).
- Comprehensiveness/sufficiency contrast tests (remove-the-rationale vs rationale-only) are a cheap, model-agnostic faithfulness probe transferable to any LLM-judge or values classifier.
- Group-conditioned AUC metrics (Subgroup/BPSN/BNSP) that separately quantify false-positive vs false-negative bias per protected community — directly reusable for identity-fairness in alignment evals.
- Validating span annotations against a random-span baseline (Jaccard 0.54 vs 0.36) — a clean way to show rationale annotations carry signal.
- Temperature-sharpened averaged annotator attention as a soft gold label — reusable for aggregating multiple human highlights into a supervisable target.
- Explicitly distinguishing "offensive" from "hate" to avoid penalizing reclaimed in-group language — an important construct-validity move for any toxicity/values benchmark.

## 12. Notable quotes
- "we introduce HateXplain, the first benchmark hate speech dataset with word and phrase level span annotations that capture human rationales for the labeling." (p.2)
- "even models that perform very well in classification do not score high on explainability metrics like model plausibility and faithfulness." (p.1)
- "models, which utilize the human rationales for training, perform better in reducing unintended bias towards target communities." (p.1)
- "a model's performance metric alone is not enough. Models with slightly lower performance, but much higher scores for plausibility and faithfulness might be preferred depending on the task at hand." (p.7)

## 13. UNKNOWN / not in extract
- Exact licensing terms of the release (only "public" GitHub).
- Full per-community bias AUC values (shown only in Figure 3, not tabulated).
- Payment/compensation details for MTurk annotators.
- Precise temperature (tau) and lambda values chosen beyond the tuned ranges (lambda=100 optimum noted).
- Demographic composition of annotators (relevant to who defines "hate").
