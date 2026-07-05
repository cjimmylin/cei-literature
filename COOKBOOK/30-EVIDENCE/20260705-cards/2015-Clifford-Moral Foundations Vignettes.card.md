---
stem: "2015-Clifford-Moral Foundations Vignettes"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, design-space, normative-ethics]
task_format: "forced-choice"
scoring_type: "human-rating"
dataset_size: 132
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: []
headline_numbers:
  - "132 validated vignettes spanning 6 moral foundations (Care, Fairness, Loyalty, Authority, Sanctity, Liberty) plus social norms controls (p.1)"
  - "Average within-foundation classification accuracy ranges from 69% (Care) to 94% (social norms) (p.10)"
  - "8-factor CFA model fit: RMSEA=.047, χ2(6,526)=12,616.71 (p.12)"
  - "Criterion validity with MFQ: standardized betas .24–.47 (all p<.001) (p.12)"
  - "Recommended set of 90 vignettes retained after both classification and factor-loading criteria (p.16)"
  - "Study 1 respondents: 330+192+94=616 total across three waves (p.5)"
  - "Study 2 respondents: 510 from national Qualtrics panel, 94 removed for attention check failure (p.11)"
---
## 1. Gist
Clifford, Iyengar, Cabeza, and Sinnott-Armstrong (2015) introduce and validate the Moral Foundations Vignettes (MFVs): 132 short scenario descriptions, each depicting a third-party moral violation targeting one of six moral foundations (Care/harm, Fairness/cheating, Loyalty/betrayal, Authority/subversion, Sanctity/degradation, and Liberty/oppression) plus a set of social norms control items. The paper fills a critical gap in the moral psychology toolkit: prior measures (the Moral Foundations Questionnaire and the Sacredness Scale) either measured abstract principle endorsement rather than concrete behavioral judgment, or were poorly suited to neuroimaging because they lacked stimulus-level control. The MFVs are tightly length-controlled (14–17 words, 60–70 characters), use a standardized "You see…" framing to invoke third-party observation, and were validated across two independent online studies demonstrating correct classification, factor structure matching MFT predictions, and criterion validity against the MFQ and MFSS. For values-alignment benchmarking, the MFVs are an important upstream resource: they define what a morally-grounded scenario item looks like, how to separate moral domains empirically, and how to validate that scenarios elicit the intended constructs rather than contaminating each other.

## 2. Benchmark/eval design features
**Constructs measured:** Six moral foundations (Care-emotional, Care-physical-human, Care-physical-animal, Fairness, Loyalty, Authority, Sanctity, Liberty) plus non-moral social norms violations. The Care foundation is empirically sub-divided by factor analysis into emotional vs. physical harm sub-types.

**Item structure:** Each item is a single sentence beginning with "You see…" that presents a concrete third-party violation. Items are strictly controlled on: syntactic structure, word length (14–17 words), character length (60–70 characters), Flesch-Kincaid reading level (above 30), and reading ease (below 12). Content control was used to avoid multi-foundation contamination (e.g., avoiding social hierarchies in Care items to prevent Liberty confounding, avoiding overt harm in Loyalty items to prevent Care confounding).

**Answer space:** Study 1 asked for (a) a 5-point moral wrongness rating (0=not at all wrong to 4=extremely wrong) and (b) forced-choice classification of which foundation is violated, with seven options mapping to the six foundations plus "not morally wrong." Additional ratings collected: comprehensibility, imageability, frequency, and emotional arousal. Study 2 asked for wrongness ratings of all 132 retained items plus completion of the MFQ and MFSS.

**Validation logic:** Study 1: items retained if ≥60% of raters correctly classified the intended foundation AND <20% misclassified as any single wrong foundation. Study 2: exploratory and confirmatory factor analysis, plus criterion validity regression against MFQ and MFSS subscales.

## 3. Task format & example item
Forced-choice classification plus Likert wrongness rating. Verbatim example from the Care (emotional) category:

> "You see a girl telling a boy that his older brother is much more attractive than him." (p.4)

Respondents first rated moral wrongness (0–4), then selected the main reason why the action is wrong from among the six foundation descriptions (e.g., "It violates norms of harm or care") plus "It is not morally wrong." Crucially, the foundation labels in the answer choices deliberately avoided repeating key words from the vignette text to prevent classification by linguistic matching (p.5).

Social norms control example (non-moral): "You see a woman drinking her entire cup of coffee using a stirring spoon." (p.10)

## 4. Scoring / grading methodology
**Study 1:** Vignettes scored on proportion of respondents correctly classifying the intended foundation and on mean wrongness ratings. Rejection criteria applied item-by-item: below 60% correct classification OR above 20% on any wrong foundation = item discarded or revised. Each item rated by approximately 30 respondents.

**Study 2:** Item scores = individual wrongness ratings (0–4). Factor scores derived from maximum likelihood EFA with promax rotation (9-factor solution retained by parallel analysis, then interpreted). Criterion validity assessed via OLS regression predicting MFV factor scores from standardized MFQ and MFSS subscales, controlling for all foundations simultaneously.

Final recommended set: 90 vignettes cleared both Study 1 classification criteria AND factor loading ≥.3 on predicted factor with no cross-loading ≥.3 in Study 2.

## 5. Dataset construction & provenance
**Source:** Hand-authored by research team, adapting previous stimuli when available (e.g., classic scenarios like eating a pet dog from Haidt et al. 1993). New scenarios written to meet design constraints: everyday plausibility, no overtly political content, no reference to specific social groups, no temporally-bounded knowledge required, no explicit reference to other foundations.

**Size:** 132 vignettes in final retained set across the 3-wave item selection process; recommended subset = 90. Breakdown: approximately 16 Care-emotional, 9 Care-physical-animal, 7 Care-physical-human, 17 Fairness, 16 Loyalty, 17 Authority, 17 Sanctity, 17 Liberty, 16 social norms items.

**Splits:** No train/test split — this is a stimulus norming database. Study 1 respondents rated subsets of ~14–16 items each; Study 2 respondents rated all 132 items.

**Wave structure:** Three waves of item development and testing (n=330, 192, 94) for Study 1; one wave for Study 2 (n=510, with 94 excluded for attention check failure).

**Licensing:** Published in Behavior Research Methods (Springer). Availability noted as a stimulus database intended for public research use; no explicit open license mentioned in the extract.

## 6. Validity evidence
**Content validity:** Each foundation addressed with 10–17 items spanning diverse scenarios; explicit care taken to avoid cross-foundation contamination during item writing and pre-testing.

**Convergent validity (criterion):** MFQ criterion subscale is the strongest predictor of the corresponding MFV subscale in every case (MFQ βs = .24–.47, all p<.001; MFSS βs = .17–.57, all p<.05). R² values range from .08 (MFSS predicting Liberty) to .38 (MFQ predicting Sanctity) (p.12).

**Discriminant validity:** In MFQ regressions, the criterion subscale is always the largest beta. The MFV subscales outperform the cross-scale correspondence between MFQ and MFSS themselves (βs = .05–.26, three of five significant) (p.16).

**Structural validity (EFA):** 9-factor solution with promax rotation recovers foundations expected by MFT: Care-emotional (Factor 1), Authority (Factor 2), Loyalty (Factor 3), Fairness (Factor 4), Care-physical (Factor 5), Liberty (Factor 6), Sanctity (Factor 7). Factors 8 and 9 are weak and uninterpretable (p.12).

**Structural validity (CFA):** 8-factor model (dividing Care into emotional/physical-human/physical-animal) fits best: RMSEA=.047, AIC=126,511.51. Improvements over simpler models are modest in moving from 7 to 8 factors (p.12–13).

**Convergent validity (ideology):** Foundation-ideology correlations replicate prior MFQ findings: binding foundations (Authority, Loyalty, Sanctity) positive; individualizing foundations (Care) negative; Liberty negative (consistent with scenarios depicting familial coercion) (p.16).

**Human baselines:** No separate human accuracy baseline reported beyond classification rates. Attention checks used: Study 1 = instructional manipulation check at survey start; Study 2 = two attention items embedded in MFQ.

## 7. Saturation / discrimination
**Wrongness ratings:** Foundation means range from 2.0 (Loyalty) to 2.8 (Sanctity) on a 0–4 scale, with social norms averaging 0.2. The Loyalty violations are "somewhat wrong" on average, indicating modest wrongness levels and potential ceiling headroom.

**Classification accuracy:** Some foundations show lower accuracy (Care at 69% average correct) and higher cross-loading (Care-physical items partially load onto the animal harm and other factors), suggesting weaker construct distinctiveness than, e.g., Fairness (97–100% correct on strongest items) or social norms (94% correct).

**Item difficulty spread:** Loyalty items show greatest variability in wrongness ratings (1.4 to 2.8) and high "not morally wrong" rates (up to 29%), making them useful for discrimination between respondents.

**Factor structure:** Liberty factor only captures 11 of 17 scenarios at ≥.4 loading, and predominantly scenarios involving familial coercion — suggesting incomplete coverage and potential saturation on a narrow construct.

## 8. Multiturn / agentic aspects
n/a. The task is a single-screen, single-response survey with no interaction, tool use, or multi-turn structure.

## 9. Key numbers
- 132 vignettes in validated stimulus set (p.1)
- 90 vignettes in recommended subset meeting both studies' criteria (p.16)
- 6 moral foundations + social norms control category (p.1)
- Study 1 waves: n=330, 192, 94 (p.5); Study 2: n=510 starting, 94 excluded, final n=416 (p.11)
- Average classification accuracy: Care 69%, Fairness ~87%, Loyalty ~69%, Authority ~74%, Sanctity ~76%, social norms 94% (p.10)
- Wrongness means (0–4): Loyalty 2.0, Care 2.5 approx, Sanctity 2.8, social norms 0.2 (p.10)
- CFA best fit RMSEA=.047, χ2(6,526)=12,616.71, AIC=126,511 (p.12)
- MFQ criterion betas .24–.47 (all p<.001); MFSS criterion betas .17–.57 (all p<.05) (p.12–13)
- MFV–MFQ cross-scale correlation range: .10–.56 (Table 8, p.19)
- Vignette length constrained to 14–17 words, 60–70 characters; reading ease 35.5–95.7, level 3.6–11.7 (p.4)

## 10. Pitfalls & limitations
**Author-admitted:**
- Liberty foundation incompletely supported: only items involving familial coercion loaded strongly; workplace coercion scenarios did not (p.12, p.19).
- Care foundation divides in unexpected ways: emotional vs. physical-human vs. physical-animal, not the single foundation assumed by standard MFT.
- Fairness factor uncorrelated with political ideology in MFV (unlike MFQ), attributed to focus on proportional rather than distributive fairness (p.16).
- Liberty correlates negatively with conservatism in MFV (counter to some MFT predictions), attributed to scenario content (p.19).
- Correlation between MFQ and MFSS scales is only moderate, suggesting existing measures diverge from each other substantially (p.16).

**Additional flaws visible in the extract:**
- WEIRD sample: Qualtrics online panel, US-only, age 18–40, ideologically balanced by design — not representative of general population or cross-cultural applicability.
- "You see…" framing assumes third-party moral judgment; findings may not generalize to first-person or agent-perspective scenarios.
- Social norms violations are non-moral controls but are not validated as such across cultures; what counts as a "merely unusual" behavior is culturally variable.
- Scenarios use Western-centric moral referents (US patriotism, American cultural symbols in Loyalty items).
- No reliability statistics (ICC, Cronbach's alpha) reported for individual items, only factor loadings and regression betas.
- Single-point-in-time validation; no test-retest reliability.

## 11. Novel ideas worth stealing
1. **"You see…" third-party framing:** Standardizing all items with this prefix anchors respondents as witnesses, not victims or perpetrators, reducing idiosyncratic first-person reactions. Reusable in any scenario-based values benchmark to enforce consistent perspective.

2. **Cross-contamination item pruning:** Explicitly testing whether items cross-classify into wrong foundations (>20% threshold) as an item-rejection criterion. This is a direct quality control mechanism for any multi-category moral/values benchmark.

3. **Structural control of items for neuroimaging / ML use:** Constraining word count (14–17 words), character length (60–70), and reading level creates a stimulus set that equalizes low-level processing demands across categories. Directly applicable to LLM prompt standardization where token length and syntactic complexity are confounds.

4. **Social norms control category:** Including genuinely non-moral violations (eccentric but harmless behaviors) as foils tests whether respondents/models are over-pathologizing. LLM safety benchmarks often lack this; adding "odd but acceptable" items would test over-refusal and false-positive safety responses.

5. **Two-stage validation protocol:** Stage 1 (classification accuracy + cross-loading rejection) followed by Stage 2 (factor analysis + criterion validity) creates a principled psychometric ladder for item selection. Benchmark designers should adopt this two-stage approach rather than relying on face validity alone.

6. **EFA as dimensionality discovery:** Running exploratory factor analysis before CFA revealed that Care splits into emotional vs. physical harm sub-types — a finding invisible from face validity alone. Running EFA on model responses before imposing a scoring schema would reveal whether the intended taxonomy actually reflects how models respond.

7. **Ideological balance in recruitment:** Deliberately recruiting equal proportions of liberals, moderates, and conservatives ensures item ratings are not ideologically confounded. Analogously, LLM benchmarks evaluating politically-charged moral scenarios should balance demographic/ideological sampling in human annotations.

## 12. Notable quotes
- "Moral relevance 'does not necessarily measure how people actually make moral judgments,' but these ratings are 'best understood as self-theories about moral judgment.'" (p.2, quoting Graham et al. 2009)

- "Furthermore, we tried to avoid scenarios that might require temporally or culturally bounded knowledge. Finally, we made an effort to eliminate any reference to other foundations to increase the likelihood of isolating the influence of a particular moral foundation." (p.4)

- "All of our scenarios begin with a 'You see…' formulation. For example, a Care violation reads: 'You see a girl telling a boy that his older brother is much more attractive than him.' This structure ensures that respondents imagine a third party committing the violation and that any emotions evoked are the result of imagining witnessing the transgression." (p.4)

- "Overall, we find strong evidence for the criterion validity of our new scales. Using both existing measures of the moral foundations, we observed the expected pattern in every case. Moreover, the MFVs correspond better with both the MFQ and MFSS than these two existing scales correspond with each other." (p.15)

## 13. UNKNOWN / not in extract
- Full item text for all 132 vignettes not printed in the extract; Table 6 lists the recommended 90 but the remaining 42 trial items are not fully shown.
- Exact Qualtrics panel demographics (race, gender, education, region) not reported beyond age range (18–40) and ideological balance.
- Inter-rater reliability (ICC) for individual items not calculated or reported.
- Licensing/distribution terms for the MFV stimulus database not stated in the extract.
- Whether the MFVs have been used or adapted for non-English or cross-cultural samples is not discussed.
- Factor loadings for all 17 Sanctity and Liberty items shown in Table 2 but the table continues past the extracted text — some factor loadings may be incompletely captured.
- Whether the vignettes are publicly available online (OSF, supplementary materials) or only in appendix is not stated.
