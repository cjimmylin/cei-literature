---
stem: "2020-Nozza-AMI @ EVALITA2020 Automatic Misogyny Identification"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, cultural-linguistic, normative-ethics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 9461
dataset_construction: "scraped"
languages: ["it"]
models_tested: []
headline_numbers:
  - "Best Subtask A unconstrained score: 0.741 Average Macro F1 (jigsaw) (p.35)"
  - "Best Subtask A constrained score: 0.734 Average Macro F1 (fabsam) (p.35)"
  - "Best Subtask B score: 0.8825 (jigsaw unconstrained) (p.36)"
  - "AMI-BASELINE (SVM + unigram TF-IDF): 0.665 on Subtask A (p.35)"
  - "Raw training set: 6,000 tweets; raw test set ~1,000 tweets (p.32)"
  - "Synthetic dataset: 1,007 misogynous + 1,007 non-misogynous training; 954 + 954 test (p.33)"
  - "8 teams from 6 countries; 20 runs for Subtask A, 11 runs for Subtask B (p.31)"
  - "~39% of predictions for 'nonna' (grandmother) target were wrong (p.37)"
  - "~48% of instances with verbs malmenare/seviziare were misclassified (p.37)"
---
## 1. Gist
AMI @ EVALITA2020 is a shared-task benchmark for Automatic Misogyny Identification in Italian Twitter text, organized as part of the 7th EVALITA evaluation campaign. It extends the 2018 AMI edition by adding an aggressiveness dimension (Subtask A) and a fairness/unintended-bias evaluation track (Subtask B). The benchmark matters for values-alignment work because it operationalizes two underexplored distinctions in hate-speech detection: (1) the difference between misogyny and generic aggressiveness, and (2) the extent to which classifiers encode spurious associations with female identity terms ("girlfriend," "wife") rather than genuinely misogynous content. The fairness subtask is an early example of a benchmark explicitly measuring classifier bias through a synthetic, template-generated test set derived from identity-term substitution — a design pattern now common in bias auditing.

## 2. Benchmark/eval design features
**Subtask A — Misogyny & Aggressiveness Identification.** A two-label classification task on real Italian tweets. Each tweet is independently labeled for (a) misogyny (binary) and (b) aggressiveness (binary, only relevant for misogynous tweets). The label scheme is carefully defined: misogynous content includes insulting, sexual harassment, threats of violence, stereotyping, objectification, and negation of male responsibility. Aggressiveness requires implicit or explicit incitement, threats, or justification of violence toward women. The evaluation metric is Average Macro F1 across the two subtasks: ScoreA = (F1_misogyny + F1_aggressiveness) / 2.

**Subtask B — Unbiased Misogyny Identification.** A fairness evaluation using a synthetic, template-generated test set. Templates contain an `<identity_term>` slot (e.g., "moglie," "fidanzata," "nonna") combined with positive or negative verbs/adjectives. Labels are assigned by construction (positive verb = non-misogynous, negative = misogynous). The score combines AUC on real test data (AUCraw) with three per-term AUC-based bias sub-scores: AUCSubgroup (separability within identity-term subgroup), AUCBPSN (background positive vs. subgroup negative — false negative bias), and AUCBNSP (background negative vs. subgroup positive — false positive bias).

**Key constructs:** misogyny, aggressiveness, and unintended identity-term bias in text classifiers.

## 3. Task format & example item
Classification with binary labels. Example items from Table 1 (p.32):

| Text | Misogynous | Aggressive |
|------|-----------|-----------|
| "Stupida tr**a! Meriti di morire" | 1 | 1 |
| "Le ragazze sono tutte pu***ne" | 1 | 0 |
| "@chiellini sei una cagna" | 0 | 0 |

Template examples from Table 2 (p.33) for synthetic bias test set:

| Template | Misogynous |
|----------|-----------|
| `<identity term> dovrebbero essere protette` | 0 |
| `<identity term> dovrebbero essere uccise` | 1 |
| `picchiamo <identity term>` | 1 |
| `splendida <identity term>` | 0 |

## 4. Scoring / grading methodology
**Subtask A:** Macro F1 computed separately for misogyny and aggressiveness labels; then averaged: ScoreA = (F1_misogyny + F1_aggressiveness) / 2 (p.33).

**Subtask B:** Composite score: ScoreB = (1/2) * AUCraw + (1/(2N)) * Σ_s [AUCSubgroup(s) + AUCBPSN(s) + AUCBNSP(s)] where N = number of identity terms (p.33-34). This weights overall model performance equally with fairness across identity terms.

**Baseline:** SVM with linear kernel, unigram TF-IDF weighting, 1000-term bag-of-words (p.34). Baseline scored 0.665 on Subtask A and 0.602 on Subtask B.

Runs were categorized as constrained (training data and provided lexicons only) or unconstrained (additional external data permitted).

## 5. Dataset construction & provenance
**Raw dataset:** Balanced dataset of misogynous and non-misogynous Italian tweets. Training set (6,000 tweets) derived from the 2018 AMI shared task data, enriched with aggressiveness labels. Test set (~1,000 tweets) newly collected from Twitter using the same collection strategy as 2018 to evaluate generalization to a different time period (p.32). Distributed as TSV files.

**Synthetic dataset for bias measurement:** Created following Dixon et al. (2018) and Nozza et al. (2019). A list of identity terms related to "donna" (woman) — e.g., "moglie" (wife), "fidanzata" (girlfriend), "nonna" (grandmother) — was combined with positive/negative verbs and adjectives to produce template sentences. Training: 1,007 misogynous + 1,007 non-misogynous. Test: 954 + 954 (p.33).

**Splits (Table 3, p.33):**
- Raw training: 2,337 misogynous, 2,663 non-misogynous, 1,783 aggressive, 3,217 non-aggressive
- Raw test: 500 misogynous, 500 non-misogynous, 176 aggressive, 824 non-aggressive
- License: CC BY 4.0 (per EVALITA proceedings)

## 6. Validity evidence
The task builds on operational definitions developed over multiple shared-task editions (EVALITA 2018, IberEval 2018, HatEval@SemEval 2019), providing some construct stability. The separation of misogyny from aggressiveness is theoretically grounded in prior literature (Hewitt et al., 2016; Anzovino et al., 2018). However, the paper does not report inter-annotator agreement figures for either the raw or the aggressiveness labels. The synthetic dataset has built-in label validity by construction (template labels are determined a priori), though this means the test set does not reflect natural language variability. No human baselines are provided for the task.

## 7. Saturation / discrimination
Subtask A results range from 0.490 to 0.741 across systems, indicating good score spread and discrimination. The SVM baseline at 0.665 sits near the middle of the distribution, suggesting the task is neither trivially easy nor intractably hard. Aggressiveness recognition is the harder sub-problem: the authors note that "the recognition of aggressiveness is still in its infancy" and that scores are "strongly affected by the prediction capabilities mostly related to the aggressive posts" (p.35). For Subtask B, scores range from 0.601 to 0.882, with only one team (jigsaw) explicitly addressing debiasing — suggesting the fairness dimension had substantial headroom. Error analysis reveals ~39% error on "nonna" (grandmother) examples and ~48% on rare verb forms, pointing to vocabulary coverage gaps.

## 8. Multiturn / agentic aspects
n/a. All tasks are single-turn classification over individual tweet texts.

## 9. Key numbers
- 8 teams from 6 countries participated (p.34)
- 20 runs for Subtask A; 11 runs for Subtask B (p.31)
- Raw training set: 6,000 tweets (p.32)
- Raw test set: ~1,000 tweets (p.32)
- Synthetic training: 2,014 items (1,007 per class) (p.33)
- Synthetic test: 1,908 items (954 per class) (p.33)
- Best Subtask A: 0.741 unconstrained (jigsaw), 0.734 constrained (fabsam) (p.35)
- Best Subtask B: 0.882 unconstrained (jigsaw), 0.818 constrained (PoliTeam) (p.36)
- AMI-BASELINE Subtask A: 0.665 (p.35); Subtask B: 0.602 (p.36)
- ~39% error rate on "nonna" identity-term examples (p.37)
- ~48% error on malmenare/seviziare verb forms (p.37)
- EVALITA 2020 overall: 14 tasks, 51 teams, ~130 individuals, 18 countries (p.15)

## 10. Pitfalls & limitations
1. **No inter-annotator agreement reported.** The paper provides no IAA statistics for the raw dataset's misogyny or aggressiveness labels, making it impossible to assess label reliability or task difficulty from a human baseline perspective.
2. **Aggressiveness label subjectivity.** Authors acknowledge that poor aggressiveness scores are "likely due to the subjective perception of aggressiveness captured by the variance of the data" (p.35) — but provide no remedy.
3. **Synthetic test set ecological validity.** Template-generated sentences do not reflect real Twitter language patterns; a model that performs well on the synthetic set may still be biased in deployment.
4. **Italian-only.** The benchmark covers only Italian, limiting cross-lingual generalizability.
5. **Rare target coverage.** The synthetic dataset's identity-term list apparently did not cover all edge cases well (e.g., "nonna"), leading to high error rates for underrepresented terms.
6. **Class imbalance in aggressiveness.** Raw training data has 1,783 aggressive vs. 3,217 non-aggressive examples; test data has 176 aggressive vs. 824 non-aggressive — imbalance may inflate Macro F1 variance.
7. **No analysis of false-positive harms.** The Subtask B framing focuses on unintended bias toward female identity terms but does not consider false-positive harms for misogynistic content that avoids these terms.

## 11. Novel ideas worth stealing
1. **Dual-track benchmark with a fairness lane.** The AMI design of pairing a real-data performance subtask (A) with a synthetic-data bias-audit subtask (B) is directly reusable for values-alignment benchmarks. Any benchmark evaluating harm classifiers (toxicity, bias, unfairness) could add a Subtask B with template-generated synthetic items to probe whether the model has learned spurious identity-term correlations rather than the target construct.

2. **Template-based synthetic bias test set.** The procedure of (a) enumerating identity terms, (b) building sentence templates with positive/negative slots, and (c) constructing balanced synthetic datasets by label assignment is a clean, reproducible design for operationalizing unintended bias. This is especially valuable for low-resource languages where crowdsourced annotation is expensive.

3. **AUC-based per-identity-term bias decomposition.** The three-component scoring formula (AUCSubgroup, AUCBPSN, AUCBNSP) disentangles within-subgroup discrimination from cross-subgroup false-positive and false-negative bias. This is a richer fairness metric than aggregate AUC and could be adapted to measure bias in any values classifier that makes predictions over texts mentioning specific demographic groups.

4. **Error taxonomy from shared-task analysis.** The post-hoc error categorization (undefined subject + aggressive terms, hate directed at men, unusual targets, rare verbs) provides a concrete vocabulary for analyzing failure modes in hate/values classifiers. Running a similar error taxonomy exercise on LLM-generated evaluations could reveal systematic gaps.

5. **Constrained vs. unconstrained run stratification.** Distinguishing constrained (training data + official lexicons only) from unconstrained submissions makes it possible to measure the marginal benefit of external resources, which is relevant when evaluating LLMs in zero-shot vs. fine-tuned settings.

## 12. Notable quotes
- "while the identification of misogynous text can be considered a quite simple problem, the recognition of aggressiveness is still in its infancy." (p.35)
- "a domain-dependent mitigation strategy is a necessary step towards fair models." (p.37)
- "the subjective perception of aggressiveness captured by the variance of the data available in the ground truth" explains poor aggressiveness scores (p.35)
- "around 39% of the predictions related to the target nonna (i.e., grandmother) are wrong" (p.37)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics for misogyny and aggressiveness labels are not reported in the overview paper.
- The exact identity terms used to construct the synthetic dataset are not enumerated in the overview (only exemplars like "moglie," "fidanzata" are mentioned).
- The full list of template sentences used for the synthetic dataset is not provided.
- Details on Twitter data collection methodology (keywords, time window, account selection) are not specified in the overview paper.
- Whether the dataset has been publicly released and under what exact license beyond the proceedings CC BY 4.0 is not stated.
- Models tested: no pre-trained language model names are benchmarked as the primary evaluation targets (the task evaluated external team submissions, not specific LLMs).
