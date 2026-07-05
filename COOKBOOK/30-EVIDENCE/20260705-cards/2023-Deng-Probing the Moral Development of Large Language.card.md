---
stem: "2023-Deng-Probing the Moral Development of Large Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, saturation-discrimination]
task_format: "forced-choice"
scoring_type: "rubric"
dataset_size: 9
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["GPT-3", "GPT-3.5", "GPT-4", "ChatGPT", "PaLM-2", "Llama2-Chat"]
headline_numbers:
  - "GPT-4 achieves pscore of 55.68, in the range of graduate students (p.6)"
  - "GPT-3 achieves pscore of 29.84, close to the random baseline of ~30.56 (p.6)"
  - "Human reference: junior/senior high students ~20–30, college/adults ~40–46, grad students ~53–63 (p.5)"
  - "All models perform poorly on Prisoner and Webster dilemmas; no model beats random baseline for 2 of 9 dilemmas (p.6)"
  - "GPT-4 on Rajesh's dilemma performs worse than most other models (p.6)"
---
## 1. Gist
This paper adapts the Defining Issues Test (DIT), a validated psychometric instrument from moral psychology, to evaluate the moral reasoning stage of seven major LLMs according to Kohlberg's Cognitive Moral Development (CMD) model. The DIT presents moral dilemmas and asks respondents to rate and rank 12 ethical consideration statements by importance; a Post-Conventional Morality Score (P-score) measures the degree to which a respondent prioritizes universal ethical principles (Stages 5–6) over self-interest or social conformity. The study is important for values-alignment benchmarking because it demonstrates: (1) that psychometrically validated instruments from moral psychology can be adapted as LLM evaluations; (2) that GPT-4 achieves human graduate-student-level post-conventional reasoning while GPT-3 is near-random; and (3) that LLM moral performance is inconsistent across dilemmas, revealing specific gaps rather than uniform competence.

## 2. Benchmark/eval design features
The DIT consists of six moral dilemmas (one excluded due to content filtering), each followed by 12 ethical consideration statements corresponding to Kohlberg's developmental stages (pre-conventional, conventional, post-conventional), plus special A (anti-establishment) and M (meaningless noise) items. The LLM must:
1. Choose a resolution to the dilemma (3 options: should / shouldn't / can't decide).
2. Rate the significance of each of 12 statements on a 5-point scale.
3. Select and rank the 4 most important statements.

The paper uses 5 original DIT-1 dilemmas + 4 novel author-designed dilemmas (total 9, minus Doctor dilemma = 8 active for most models). Novel dilemmas are designed to: (a) extend cultural context and diversity, and (b) reduce contamination risk from training data.

To control for positional bias, 8 permutations of the 12 statements and all 6 permutations of the 3 resolution options are used, yielding 48 distinct prompts per dilemma (p.5).

## 3. Task format & example item
Forced-choice + ranking task within each dilemma.

Example dilemma (from appendix description, p.7–8):
- **Rajesh's Dilemma**: Should Rajesh rent a house by hiding the secret of his non-vegetarian consumption at home from the vegetarian neighborhood?
- **Timmy's Dilemma**: Should Timmy attend his friend's wedding instead of fixing an urgent bug that could put customers' privacy at risk?
- **Monica's Dilemma**: Should Monica give the first authorship to Aisha despite having the major contribution?
- **Auroria Dilemma**: Should the country Auroria share its innovations and resources to its poor neighbor or profit off its huge investments in research?

The full DIT-1 dilemmas include: Heinz (steal drug for dying wife), Newspaper (student newspaper), Student (Vietnam war protest), Webster (minority hiring), Prisoner (escaped prisoner).

## 4. Scoring / grading methodology
**P-score (Post-Conventional Morality Score)**: Points are awarded based on whether the LLM's top-ranked statements belong to Stages 5 or 6. Ranking positions 1–4 yield 4, 3, 2, 1 points respectively if the statement is post-conventional. Final P-score = sum × 10. Range: 0–96.67 averaged across all dilemmas.

Random baseline P-scores: ~25 for dilemmas with 3 post-conventional items; ~33.33 for dilemmas with 4 post-conventional items; average ~30.56 across all dilemmas.

Stage-wise scores computed analogously for each Kohlberg stage individually.

## 5. Dataset construction & provenance
- 5 dilemmas purchased from DIT-1 through University of Alabama's Center for the Study of Ethical Development.
- 4 novel dilemmas designed by the four co-authors (one each), then independently annotated by all authors for CMD stage correspondence; disagreements resolved by discussion or item revision.
- Total: 9 dilemmas (8 used after Doctor dilemma exclusion). All culturally situated—novel dilemmas include Indian (Rajesh), academic (Monica), technology ethics (Timmy), and international relations (Auroria) contexts.
- No dataset release mentioned; dilemmas reproduced in appendix.

## 6. Validity evidence
- Adapts a well-validated psychometric instrument (DIT-1 used in ~400 studies 1974–1988, used in 40+ countries).
- P-score results align with expected human developmental ranges: GPT-4 in grad-student range, others in adult/college range.
- Positional bias controlled via permutation (8 statement orderings × 6 option orderings = 48 prompts per dilemma).
- Violin plots show within-model variance across runs, capturing response consistency.
- Authors explicitly acknowledge DIT framework criticisms: individualistic cultural bias (Global North bias), gender bias, ignoring emotions/intuitions.

## 7. Saturation / discrimination
- GPT-4 (P-score 55.68) substantially above random baseline (~30.56) and above GPT-3 (29.84) — strong discrimination at the top.
- All models perform poorly on Prisoner and Webster dilemmas; 2 of 9 dilemmas produce results no better than random baseline for all models. This reveals specific topic-level gaps.
- GPT-4 underperforms on Rajesh's dilemma relative to other dilemmas and other models—cultural specificity of the dilemma appears to be a discriminating factor.
- Ordering of models by P-score: GPT-4 > ChatGPTv1 > Llama2-Chat ≈ PaLM-2 > ChatGPTv2 > GPT-3.5 >> GPT-3.

## 8. Multiturn / agentic aspects
n/a. Single-turn prompt structure. Temperature set to 0 for reproducibility; 48 prompt permutations per dilemma.

## 9. Key numbers
- GPT-4 P-score: 55.68 (all dilemmas), 58.81 (8 dilemmas, excluding Prisoner) (p.6)
- ChatGPTv1 P-score: ~53 (all), 56.44 (8 dilemmas) (p.6)
- Llama2-Chat: ranked 3rd overall, 52.85 (8 dilemmas) (p.6)
- GPT-3 P-score: 29.84 ≈ random baseline ~30.56 (p.6)
- Human reference: high school students ~20–30; college/adults ~40–46; grad students ~53–63 (p.5)
- Random baseline (averaged): ~30.56 (p.5)
- Maximum possible P-score (average): 96.67 (p.5)
- 48 prompts per dilemma (8 statement permutations × 6 option permutations) (p.5)
- 7 models tested; 9 dilemmas total (8 active due to Doctor dilemma refusal) (p.5)

## 10. Pitfalls & limitations
- DIT-1 is culturally biased toward individualistic, Global North moral frameworks; it was criticized for neglecting communitarian morality, gender perspectives (Gilligan), and emotional/intuitive moral processing.
- Small dilemma set (8–9 dilemmas) means results are sensitive to individual item variance.
- P-score confounds genuine moral reasoning with instruction-following: a model that understands the scoring rubric can game it by selecting Stage-5/6 items without authentic reasoning.
- No contamination check for whether DIT-1 dilemmas appear in LLM training data (acknowledged only for novel dilemmas).
- High within-model variance (shown in violin plots) means point estimates are uncertain.
- ChatGPTv2 shows unexpectedly lower P-score than ChatGPTv1, possibly reflecting degradation over model updates—but this is speculative.
- Novel dilemmas annotated by the study's co-authors—no external validation of stage assignments.

## 11. Novel ideas worth stealing
- **Psychometric instrument transplantation**: Directly adapting a validated human moral psychology test (DIT, MJT, etc.) to LLM evaluation is a principled design move that provides established human baselines, interpretable staging, and decades of comparative literature. Highly reusable for values-alignment benchmarks.
- **Permutation-based positional bias control**: Running 48 distinct prompt variants per dilemma (all meaningful combinations of statement orderings and option orderings) and aggregating provides a more robust estimate than single-run or few-shot results.
- **Dilemma as a cultural enrichment strategy**: Adding novel dilemmas set in diverse cultural contexts (Indian household norms, international aid) reduces contamination risk and increases cultural validity—a model for expanding any psychometric instrument for cross-cultural LLM evaluation.
- **Stage-wise scores alongside P-score**: Reporting individual Kohlberg stage scores per model (in addition to aggregate P-score) provides a richer profile—useful for diagnosing whether a model is stuck at pre-conventional (self-interest), conventional (rules), or post-conventional (principles) reasoning.
- **Random baseline as a calibration reference**: Explicitly computing the expected P-score from random item selection (depends on dilemma structure, ~30.56 average) is a principled floor calibration, easily replicated in any ordinal ranking benchmark.

## 12. Notable quotes
- "GPT-4, in fact, has the highest post-conventional moral reasoning score, equivalent to that of typical graduate school students." (p.1)
- "It is impossible to design a universally-aligned LLM." (p.1)
- "There is a lack of consistency in ethical reasoning across these models, implying the need for deeper investigation, understanding and improvement of LLMs' moral reasoning abilities." (p.2)
- "Since the training data and the architectural details of GPT-4 are undisclosed, one can only speculate the reasons. Either the data ... consisted of many examples of post-conventional moral reasoning, or it is an emergent property of the model." (p.8)

## 13. UNKNOWN / not in extract
- Full text of DIT-1 dilemmas not reproduced (purchased dataset; proprietary).
- Exact stage-assignment annotations by authors for novel dilemmas not shown in extract (referred to as Figures 4–7 in appendix).
- Inter-annotator agreement statistics for novel dilemma stage annotations not reported.
- Whether any model showed significant M-item (meaningless noise) endorsement is not discussed.
- Dataset or code release not mentioned.
- Prompt engineering details beyond Figure 1 schematic not fully specified.
