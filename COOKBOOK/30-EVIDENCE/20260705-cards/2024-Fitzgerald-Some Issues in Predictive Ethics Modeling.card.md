---
stem: "2024-Fitzgerald-Some Issues in Predictive Ethics Modeling"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [contamination-robustness, validity-psychometrics, normative-ethics, cultural-linguistic]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 851
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["RoBERTa (gFulvio/moralstories_roberta_action.context_consequences_cls)"]
headline_numbers: [
  "Descriptive shifts reduce classifier accuracy from 99.55% to 51.58% (p.7)",
  "Textual bias (direct) reduces accuracy to 77.09% (p.7)",
  "Object changes produce 26.09% accuracy (p.8)",
  "Demographics swap (gender + names) leaves accuracy at 100% (p.8)",
  "Contrast set overall accuracy 83.74%, vs 99.55% on original test set (p.8)"
]
---
## 1. Gist
Fitzgerald (Haverford College) challenges the apparent success of predictive ethics classifiers like Delphi and the Moral Stories dataset by building four adversarial contrast sets that stress-test a RoBERTa-based moral classifier. The core argument is that high accuracy on standard test sets is deceptive: small, targeted perturbations to the descriptive content of moral scenarios (as few as 3–5 words) can collapse accuracy to near-chance, revealing that the classifier learns surface features rather than genuine moral reasoning. The paper is directly relevant to values-alignment benchmarking because it quantifies how specific types of data representation errors degrade ethics classifiers, and offers concrete architectural recommendations to close these gaps.

## 2. Benchmark/eval design features
The paper evaluates a classifier trained on the Moral Stories dataset (Emelin et al., 2021) using four contrast set types:

1. **Norm Swaps (n=333)**: Replace the social norm attached to a scenario with an irrelevant norm, a misleading norm, or a directly flipped norm (good→bad or bad→good).
2. **Textual Bias (n=328)**: Alter syntax without changing denotation — either directly stating the "wrong" moral conclusion (e.g., "Sam behaves morally by shooting someone") or indirectly framing the scenario in a charged way.
3. **Descriptive Shifts (n=188)**: Apply defeasible reasoning to change setting, behavior, occupation, object, or wording with label-changing minimal edits.
4. **Demographics (n=324)**: Swap gender pronouns via ChatGPT or replace names with non-Caucasian names from NYC baby-name data.

Each contrast set tests a different failure mode. The Moral Stories dataset has 6-column structure: norm, situation, intention, moral/immoral action, moral/immoral consequence, and label.

## 3. Task format & example item
The classifier task is forced-choice binary (moral vs. immoral action/consequence pair). Example of a descriptive (object) shift from Appendix A (p.16):

Original:
```
{"norm": "Calling an ambulance for a minor issue is irresponsible.",
 "situation": "George suffers a minor cut after scraping his arm against a nail.",
 "immoral_action": "George calls 911 for his small cut...",
 "immoral_consequence": "The 911 crew seem somewhat annoyed..."}
```
Revised (label flipped by changing "nail" → "rusty nail"):
```
{"norm": "Calling an ambulance for a minor issue is irresponsible.",
 "situation": "George suffers a minor cut after scraping his arm against a rusty nail.",
 "moral_action": "George calls 911 for his small cut...",
 "immoral_consequence": "The 911 crew seem somewhat annoyed..."}
```
The one-word change ("rusty") transforms an immoral action into a moral one, yet the classifier fails to detect this shift (p.7).

## 4. Scoring / grading methodology
The paper fine-tunes `gFulvio/moralstories_roberta_action.context_consequences_cls` from HuggingFace (derived from RoBERTa) on the Moral Stories dataset. Hyperparameters: learning rate 1e-6, batch size 16, 3 epochs (p.17). Accuracy and F1 score are computed for each contrast set and subcategory against the original test set labels (or flipped labels for descriptive shifts). The original test set achieves 99.55% accuracy / 0.9955 F1 as baseline (p.8).

## 5. Dataset construction & provenance
The contrast sets are hand-authored by Fitzgerald on the first 333 rows of the Moral Stories training split. Total contrast set size: 851 items. The base dataset (Moral Stories, Emelin et al. 2021) consists of 20,000 training rows and 2,000 dev/test rows, created via MTurk annotators building situations from Social Chemistry norms. Demographic contrast items were generated via programmatic ChatGPT prompting. No licensing information is stated. The author acknowledges limitations of not being the original dataset creator (p.4).

## 6. Validity evidence
The paper's validity argument is adversarial rather than psychometric. Key evidence:
- The classifier's 99.55% accuracy on the original test is replicated, establishing the baseline.
- Four distinct contrast set types provide construct coverage across different hypothesized failure modes.
- Results are internally consistent: changes to semantically load-bearing content (object, behavior) hurt performance far more than surface-level demographic changes.
- No human baseline is reported for the contrast sets themselves, which is a gap.
- No inter-rater reliability for the hand-authored perturbations is reported.

## 7. Saturation / discrimination
The original classifier is effectively saturated (99.55% accuracy, F1=0.9955) on the standard Moral Stories test set. The contrast sets reveal dramatic discrimination failures:
- Descriptive shifts (object subcategory): accuracy 26.09%, near inverse of correct (p.8)
- Wording changes: 33.33% accuracy (p.8)
- Indirect textual bias: 59.41% accuracy (p.8)
- Demographics: 100% accuracy — shows zero discrimination based on name/gender (p.8)
The contrast set exposes that the saturation on standard test is artificial, masking near-random performance on semantically altered inputs.

## 8. Multiturn / agentic aspects
n/a — Single-turn classification task throughout.

## 9. Key numbers
- Original test set accuracy: 99.55% (p.8)
- Overall contrast set accuracy: 83.74% (p.8)
- Descriptive shifts: 51.58% accuracy (p.7)
- Object changes: 26.09% accuracy (p.8)
- Behavior changes: 51.40% accuracy (p.8)
- Textual bias (direct): 77.09% accuracy (p.7)
- Textual bias (indirect): 59.41% accuracy (p.7)
- Norm swap (all): 98.20% accuracy (p.8)
- Demographics: 100% accuracy (p.8)
- Contrast set total n=851 across four types (p.8)
- Emelin et al.'s original model accuracy adding norms + context: 84% → 99% (p.4)
- Delphi binary classification: 98.1% accuracy, 4.3% above human annotators (p.2)
- Applied to n=20,000: contrast set failure rate predicts ~3,252 misaligned predictions vs 90 originally expected (p.7)
- Hyperparameters: lr=1e-6, batch=16, epochs=3 (p.17)

## 10. Pitfalls & limitations
- Author acknowledges not being the Moral Stories dataset creator, so contrast sets may miss systematic gaps in the dataset's decision boundary (p.4).
- Small-n subcategories (object n=23, wording n=6) make subcategory-level conclusions fragile.
- No human baseline for contrast sets, so it is unclear whether the revised items are genuinely harder for humans.
- The demographic contrast set achieves 100% accuracy but this may reflect limited demographic diversity in the original training data rather than fairness progress.
- Contrast set is constructed entirely in English; no cross-lingual or cross-cultural coverage.
- The paper is a student research project (runner-up, BlueDot Impact AI Alignment course), so methodological depth is limited compared to peer-reviewed work.
- No statistical significance testing is reported for accuracy differences between contrast set categories.

## 11. Novel ideas worth stealing
- **Contrast sets as validity probes**: The four-type taxonomy (norm swap, textual bias, descriptive shift, demographics) is a clean framework for stress-testing any moral/values benchmark. Building adversarial contrast sets should be standard practice before claiming benchmark validity.
- **Quantifying the marginal cost of specific framing errors**: The paper gives concrete estimates of how much each class of perturbation hurts performance — this is more actionable than generic claims about classifier fragility.
- **Textual bias as an alignment-relevant failure**: The finding that adding the words "x behaves morally" to a scenario demonstrably shifts classifier output implies that LLMs trained on ethics datasets may be gaming surface tokens rather than understanding ethics — directly relevant to LLM-judge and reward model design.
- **Tabular norm representation**: The recommendation to move from sentence-level social norms to structured tabular norms encoding setting, role, behavioral constraints, and context (p.11) is a concrete design idea for next-generation values datasets.
- **Defeasible + non-monotonic hybrid**: The proposed architecture (ClarifyDelphi-style clarification questions → non-monotonic norm lookup → moral judgment) is a candidate agentic evaluation protocol for values-alignment benchmarks (p.11).
- **Cultural context as norm metadata**: The suggestion to tag norms with cultural origin and allow dynamic switching of the ethical framework at inference time (p.12) is directly applicable to pluralism-aware benchmark design.

## 12. Notable quotes
- "label-changing tweaks to a situation's descriptive content (as small as 3-5 words) can reduce classifier accuracy to as low as 51%, almost half the initial accuracy of 99.8%." (p.1)
- "Any ethical classifier will be, at best, a simulacrum of that richness of deliberation, a screenshot of the minds of a few dozen annotators at the precise moments, and on the precise ethical data points, that went into building training data." (p.10)
- "GAI cannot be capabilities-first systems throttled by ethical protections: every aligned GAI must be just as much an ethics model as it is a generalized AI." (p.10)
- "Theoretically, ethics modeling is wise; practically, ethics modeling is foolish. Truly aligning an ethics model will take more than representing platitudes in training sets–it will take a concrete re-examination of everything we know about the morality we purport." (p.13)

## 13. UNKNOWN / not in extract
- Whether ChatGPT-generated demographic perturbations were validated for quality or accuracy
- Statistical significance of differences between contrast set accuracy rates
- Whether any additional language model was tested beyond the one RoBERTa fine-tune
- The full contrast set data (referenced as available at author's GitHub but not in extract)
- Whether the paper was subsequently peer-reviewed or published in a venue beyond the course project
