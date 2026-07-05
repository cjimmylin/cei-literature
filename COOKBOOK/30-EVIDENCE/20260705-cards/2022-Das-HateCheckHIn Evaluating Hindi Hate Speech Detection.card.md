---
stem: "2022-Das-HateCheckHIn Evaluating Hindi Hate Speech Detection"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, best-practices]
task_format: "mixed"
scoring_type: "exact-match"
dataset_size: 5884
dataset_construction: "template"
languages: [Hindi, English, hi-Latn]
models_tested: [mBERT (H-21), mBERT (C-21), Perspective API]
headline_numbers: ["5,884 test cases across 34 functionalities (4,754 monolingual + 1,130 multilingual) (p.5)", "Fleiss' Kappa 0.95 inter-annotator agreement on gold labels (p.5)", "H-21 scored 0.0% accuracy on multilingual functionalities MF1 and MF2 (p.7)", "Perspective (P) scored 9.37% on MF2 (p.7)", "Overall accuracy on all cases: H-21 49.88%, C-21 53.87%, P 63.88% (p.5)"]
---
## 1. Gist
HateCheckHIn is a diagnostic functional-test suite (a CheckList/HATECHECK-style behavioral benchmark) for Hindi and code-mixed hate-speech detection models. Rather than reporting aggregate F1 on a held-out set, it decomposes model competence into 34 targeted functionalities — 28 monolingual (adapted from Röttger et al. 2020's English HATECHECK) plus 6 new multilingual/code-mixing functionalities specific to Hindi-English mixing scripts and scripts (Roman Hindi, Devanagari-for-English, code-mixing). Each functionality carries a gold label, so failure localizes a specific model weakness. For values-alignment benchmarking it is a strong exemplar of (a) contrastive/near-miss item design (hateful vs. non-hateful minimal pairs like "I hate Hindus" vs. "I hate apples"), (b) protected-group bias probing, and (c) extending Western-authored benchmarks to non-WEIRD linguistic contexts where models catastrophically fail.

## 2. Benchmark/eval design features
Construct measured: binary hate/non-hate classification competence, decomposed into functional capabilities. 34 functionalities each map to distinct expressions of hate (dehumanisation, slurs, threat, implicit derogation), non-hateful contrasts (reclaimed slurs, counter-speech, neutral/positive group references, profanity used non-hatefully), spelling/perturbation robustness (char swaps, missing chars, leet speak, added spaces), and 6 multilingual functionalities (MF1-6). Answer space is binary (H / NH) with a gold-standard label per case. Ten protected groups spanning religion, national origin, gender identity, caste, gender, race, sexual orientation (Hindu, Muslim, Bangladeshi, Pakistani, eunuch, Dalit, women, lower caste, British, homosexual).

## 3. Task format & example item
Binary classification of a short crafted utterance. Verbatim template example: "मुझे [IDENTITY] से नफरत है." (I hate [IDENTITY]), gold label H (p.6). Multilingual example MF1: "Mujhe [IDENTITY] se nafrat hai." gold H (p.7). Contrast example (non-hate): मुझे एप्पल से नफरत है ("I hate apples") should be non-hateful (p.3).

## 4. Scoring / grading methodology
Exact-match accuracy: percentage of test cases correctly classified against gold label, computed per functionality, per label, and per target group (p.7). Perspective API's percentage toxicity score is thresholded at 50% to produce binary labels (p.7). Random baseline is 50%; scores below 50% flagged in red (p.7).

## 5. Dataset construction & provenance
Hand-crafted plus template-based generation: identity/slur placeholder templates ("मुझे [IDENTITY] से नफरत है", "तुम मेरे लिए एक [SLUR] जैसी हो") filled across 10 protected groups (p.5). 5,884 total cases (4,754 monolingual, 1,130 multilingual) (p.5). Validation: two PhD students with prior hate-speech experience annotated each case, disagreements discussed to consensus; Fleiss' Kappa = 0.95 (p.5). 43 unrealistic cases removed (p.5). Released on GitHub (hate-alert/HateCheckHIn) (p.2). mBERT fine-tuned on HASOC-2021 (Mandl et al. 2021, 6,126 tweets) and CONSTRAINT-2021 (Bhardwaj et al. 2020, 8,192 tweets) binary subsets (p.5).

## 6. Validity evidence
Inter-annotator reliability Fleiss' Kappa 0.95, "almost perfect" (p.5). Content validity via UN definition of hate speech (p.2) and functionalities derived from Röttger et al.'s stakeholder-interview-grounded HATECHECK. Criterion validity is demonstrated indirectly: functional failures (e.g., counter-speech misclassification F20/F21) align with known model-bias literature (Dixon et al. 2018). No human performance baseline reported.

## 7. Saturation / discrimination
Strongly discriminating, far from saturated — the multilingual functionalities are near-flooring some models (H-21 = 0.0% on MF1 and MF2, p.7). Wide spread across functionalities (H-21 ranges 0% to 81% F16, p.6-7). Authors note the entire accuracy drop for H-21 is attributable to multilingual inputs (p.8), showing the benchmark exposes headroom invisible to standard held-out F1.

## 8. Multiturn / agentic aspects
n/a — single-turn classification only.

## 9. Key numbers
- 34 functionalities total: 28 monolingual + 6 multilingual (p.5)
- 5,884 test cases: 4,754 monolingual, 1,130 multilingual (p.5)
- Fleiss' Kappa 0.95 (p.5); 43 cases removed as unrealistic (p.5)
- Overall accuracy: H-21 49.88%, C-21 53.87%, P 63.88% (Table 3, p.5)
- H-21 = 0.0% on MF1 (Roman Hindi) and MF2 (slur in Devanagari) (p.7)
- Perspective P = 9.37% on MF2, lowest recorded (p.7)
- H-21 below 50% on 6/28 monolingual and 6/6 multilingual functionalities (p.7)
- Worst target for H-21: Bangladeshi 24.43%, Eunuch 28.94% (p.8)
- P consistently ~60% across most target groups (p.8)

## 10. Pitfalls & limitations
Template-based generation risks low lexical diversity (authors mitigate by diverse vocab per Zhou et al. 2020, p.5). Binary reduction discards offensive/profane intermediate labels. Only two annotators. mBERT fine-tuned on small binary subsets may not represent SOTA. Perspective API is a black box evaluated at one point in time (Dec 2021, p.7). Diagnostic suite measures failure localization, not deployment readiness. Test cases are synthetic and may not reflect naturalistic distribution. No calibration or confidence analysis.

## 11. Novel ideas worth stealing
- **Functional decomposition of a single label into capabilities** — instead of one accuracy number, expose per-capability failure so a benchmark localizes weakness. Directly portable to values benchmarks (decompose "is this response ethical" into deception, harm, fairness sub-functionalities).
- **Minimal-pair contrast items** (hateful vs. non-hateful differing only in target: "I hate Hindus" vs "I hate apples") isolate the exact decision boundary and expose spurious shortcut learning.
- **Non-hateful "hard negatives"**: counter-speech, reclaimed slurs, quoted hate, neutral group mentions — these catch models that key on surface identity terms. A values benchmark should include hard negatives (e.g., discussing harm to critique it) to catch over-refusal.
- **Cross-script/code-mixing perturbations** as a robustness axis — same semantic content in Roman Hindi, Devanagari, code-mixed — a template for testing multilingual value alignment robustness.
- **Per-protected-group scoring** as a built-in bias audit within the same items.
- **Template + placeholder scaling** with human consensus validation gives large N cheaply while retaining gold-label quality.

## 12. Notable quotes
- "held-out performance on current hate speech datasets is an incomplete and potentially misleading measure of the model quality." (p.1)
- "we craft 5.8K test cases ... using our evaluation dataset, we evaluate a few Hindi hate speech detection models." (p.2)
- "For the multilingual functionalities, the model performance is less than 50% for 6 out of 6 functionalities." (p.7)
- "this shows that the multilingual functionalities proposed by us are indeed very effective in identifying the nuanced weaknesses of the classification models." (p.8)

## 13. UNKNOWN / not in extract
- No human performance ceiling reported.
- Licensing terms of the released dataset not specified in extract.
- Exact per-functionality template counts for monolingual cases (only multilingual breakdown in Table 2) not fully enumerated.
- No LLM (generative) models tested — only classifiers.
