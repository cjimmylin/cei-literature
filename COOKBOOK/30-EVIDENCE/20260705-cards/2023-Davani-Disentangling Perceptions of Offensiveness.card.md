---
stem: "2023-Davani-Disentangling Perceptions of Offensiveness"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, moral-psychology, pluralism-aggregation, validity-psychometrics]
task_format: "preference"
scoring_type: "human-rating"
dataset_size: 4554
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["Perspective API"]
headline_numbers:
  - "4,309 participants from 21 countries across 8 cultural regions (p.1)"
  - "25 out of 28 pairs of geo-cultural regions show significantly different offensiveness perceptions (p.3)"
  - "39.5% of variance in offensiveness labels is due to individual differences; country explains 2.9%, region 0.7% (p.5)"
  - "Care (ACME = -0.034, p < .001) and Purity (ACME = -0.007, p = .004) significantly mediate cross-cultural differences (p.5)"
  - "Arab Culture highest average offensiveness (M=1.19, SD=1.48); Sinosphere lowest (M=0.80, SD=1.22) (p.3)"
---
## 1. Gist
This paper presents a large-scale cross-cultural empirical study establishing that perceptions of offensiveness are shaped by both geo-cultural background and individual moral values, not merely content characteristics. The authors recruited 4,309 participants from 21 countries, had them annotate 4,554 social media items for offensiveness on a 5-point scale, and administered the Moral Foundations Questionnaire (MFQ-2) to each participant. Key findings: (1) significant cross-cultural differences in offensiveness perceptions persist even after controlling for age, gender, and socioeconomic status; (2) individual-level moral concerns about Care and Purity mediate these cultural differences; (3) existing AI toxicity models (Jigsaw, Perspective API) align more closely with some cultural regions and moral profiles than others. For values-alignment benchmarking, this work provides strong empirical grounding for why a single "universal" offensiveness label is scientifically untenable, and demonstrates a methodology for characterizing whose moral values AI safety systems reflect.

## 2. Benchmark/eval design features
This is a study of human annotator disagreement rather than a benchmark per se, but it produces an annotated dataset with multi-annotator labels (at least 3 annotators per item per region) that is suitable for benchmarking AI models. The study operationalizes "offensiveness" as the dependent variable and tests whether:
- Geographic/cultural region predicts annotation behavior (Study 1)
- Individual Moral Foundation scores mediate those regional effects (Study 2)
- Existing AI models reflect cultural biases in their alignment (Study 3)

The 4,554 items are drawn from Jigsaw toxicity classification datasets, sampled in three strata: (1) ambiguous items likely to be unclear (50%); (2) items mentioning social group identities related to gender, sexual orientation, or religion (40%); (3) items with different moral sentiments identified via MFTC tagger (10%). This stratified design ensures the dataset captures systematic rather than incidental variation.

## 3. Task format & example item
Annotators rated 40 items (including 5 quality-control items) on a 5-point Likert scale from "not offensive at all" to "extremely offensive." Half were given a definition of "extremely offensive language" (profanity, strongly impolite, rude or vulgar language with hurtful words to insult), while the other half received no definition.

No verbatim example item is provided from the text. Items are drawn from Jigsaw's Toxic Comments Classification dataset and Unintended Bias dataset (social media comments).

## 4. Scoring / grading methodology
- Human annotations: 5-point Likert scale per item.
- Cross-cultural comparison: one-way ANOVA with cross-classified mixed-level regression (annotators as level 1, regions as level 2, items as crossed level).
- Mediation analysis: Baron and Kenny (1986) framework; separate mediation tests for each of the six MFQ-2 moral foundations.
- Individual vs. country-level decomposition: moral scores decomposed into country-average and individual deviation from country average; regression used to isolate individual-level effects.
- AI model comparison: Pearson/Spearman correlation between majority-vote labels from each region and Jigsaw/Perspective API labels.

## 5. Dataset construction & provenance
- 4,554 items from Jigsaw Toxic Comments Classification Challenge (2018) and Unintended Bias in Toxicity Classification dataset (Jigsaw, 2019).
- Stratified sampling: 50% ambiguous, 40% identity-mentioning, 10% moral-sentiment-tagged.
- 4,309 participants from 21 countries; at least 450 participants per region.
- Demographic quotas: ≤60% per binary gender, ≤60% aged 18–30, ≥15% aged 50+; English fluency required.
- Each item received ≥3 annotations from annotators in each of 8 regions.
- Quality control: 5 control items per participant; those failing removed (final N = 4,295).
- Moral Foundations Questionnaire (MFQ-2; Atari et al., 2023) administered post-annotation.

## 6. Validity evidence
- ANOVA confirms cross-regional effects hold after controlling for age (F(7,7515)=26.80), gender (F(7,7515)=32.21), and SES (F(7,7515)=32.49) (p.3–4).
- Mediation analysis confirms Care and Purity as significant mediators.
- Providing a definition reduces but does not eliminate cross-regional variance (F drops from 18.95 to 15.22) (p.4).
- Correlation of individual Perspective API agreement with Care moral score: β=0.027 (SE=0.004, p<0.001), confirming model moral alignment (p.6).
- China data anomaly addressed by rerunning analyses without China; results hold.

## 7. Saturation / discrimination
- 25/28 cross-region pairs show significant differences, indicating broad discrimination across cultures.
- Individual differences explain 39.5% of variance vs. 2.9% for country and 0.7% for region—suggesting cultural groupings alone under-capture variation. Moral foundations at individual level provide better discrimination.
- Country-level Care scores are not significant predictors of individual annotations; individual deviation from country average is (β=0.14, p<0.001 for Care), showing within-country moral heterogeneity matters more than between-country averages.

## 8. Multiturn / agentic aspects
n/a. Single-turn annotation study.

## 9. Key numbers
- Participants: 4,309 from 21 countries, 8 cultural regions (p.1)
- Items: 4,554; each annotated by ≥3 participants per region (p.3)
- ANOVA: F(7,7515)=31.47, p<.001 for main regional effect (p.3)
- Arab Culture: M=1.19, SD=1.48; Sinosphere: M=0.80, SD=1.22 (p.3)
- 25/28 region pairs significantly different (p.3)
- Individual variance: 39.5%; country: 2.9%; region: 0.7% (p.5)
- Care mediation ACME = -0.034, p<.001; Purity ACME = -0.007, p=.004 (p.5)
- 1-pt increase in Care score → 0.14 increase in offensiveness label (individual deviation) (p.5)
- Perspective API agreement with Care: β=0.027, SE=0.004, p<0.001 (p.6)
- WEIRDness correlation with offensiveness: 1-pt increase → 0.96 decrease (p=0.18, not significant) (p.4)

## 10. Pitfalls & limitations
- All annotation performed in English only, limiting generalizability to speakers for whom English is not native.
- Binary gender only due to safety concerns in some countries.
- China data anomaly (older demographic skew) complicates Sinosphere interpretation.
- Country-level averages used to represent population opinions, ignoring within-country heterogeneity.
- Jigsaw items were originally labeled for toxicity, not offensiveness—the task definition mismatch reduces comparability.
- The crowd-sourcing platform (likely Prolific or similar) over-represents participants with internet access and English fluency.
- Definition of "extremely offensive" is narrow; half the participants had no definition at all—annotation conditions are mixed.

## 11. Novel ideas worth stealing
- **Moral Foundations as a moderator variable**: Incorporating MFQ-2 scores alongside annotations allows benchmarks to explain annotator disagreement in terms of moral psychology constructs, not just demographic labels. Directly applicable to any values-alignment annotation task.
- **Care and Purity as the key safety-relevant foundations**: The finding that Care and Purity mediate offensiveness perception is a concrete, actionable finding for safety benchmark design—items targeting care ethics vs. purity/contamination concerns will elicit systematically different cross-cultural responses.
- **Decomposing country-average vs. individual deviation**: The analytical move of separating group-level moral scores from individual deviation provides a model for how to measure both cultural-level and person-level variation within annotation studies—useful for understanding benchmark score variance.
- **Auditing existing AI models for cultural alignment**: Study 3 directly audits Perspective API against cultural subgroup annotations—a methodology reusable for auditing any AI safety or values-alignment model.
- **Providing/withholding definitions as an experimental condition**: The split-design (half with explicit definition, half without) tests how much task framing reduces cross-cultural disagreement—a useful calibration lever for benchmark instructions.

## 12. Notable quotes
- "Perception of offensiveness is inherently subjective, shaped by the lived experiences and socio-cultural values of the perceivers." (p.1)
- "Individual moral values play a crucial role in shaping these variations: moral concerns about Care and Purity are significant mediating factors driving cross-cultural differences." (p.1)
- "39.5% of the variance is due to individual differences while country and region difference explain only 2.9% and 0.7% of the variance, respectively." (p.5)
- "Instead of mainly focusing on demographics, our findings suggests that aligning AI models with moral foundations that individuals and groups are concerned about potentially provides an effective and efficient approach towards value alignment efforts for the pluralistic world we live in." (p.8)

## 13. UNKNOWN / not in extract
- The full text of the 4,554 items used is not provided or publicly released (Jigsaw datasets are the source, but the exact subsample is not described).
- The specific crowdsourcing platform used for recruitment is not named.
- Exact countries per region and per-country N are partially given (Table 1 referenced but not reproduced in extract).
- Whether the collected multi-annotator dataset itself is released publicly is unclear from the extract.
- MFQ-2 item wording is not reproduced in the extract.
