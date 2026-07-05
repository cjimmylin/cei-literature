---
stem: "2023-Hopp-The Dutch Moral Foundations Stimulus Database"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, design-space]
task_format: "mixed"
scoring_type: "human-rating"
dataset_size: 240
dataset_construction: "crowdsourced"
languages: ["Dutch", "English"]
models_tested: []
headline_numbers:
  - "586 Dutch crowd-workers provided 38,460+ individual judgments (p.1)"
  - "97% of vignettes classified into their intended moral foundation category (p.11)"
  - "Physical care violations receive highest moral wrongness ratings (M=4.09); loyalty violations lowest among moral foundations (M=2.68) (p.9)"
  - "63% of SMID images rated according to intended foundation category; 87.92% average accuracy (p.16)"
  - "Right-leaning political orientation correlated with higher wrongness ratings for binding foundations: loyalty r=.16, authority r=.21, sanctity r=.14 (p.11)"
---
## 1. Gist
This paper adapts and validates two widely-used moral psychology instruments — the Moral Foundations Vignettes (MFV; Clifford et al., 2015) and the Socio-Moral Image Database (SMID; Crone et al., 2018) — for Dutch populations. The authors translate 120 MFV text scenarios into Dutch and select 120 images from SMID covering five moral foundations plus neutral content. A crowd-sourced Dutch sample (N=586) rates both stimuli sets across multiple dimensions. This is directly relevant for values-alignment benchmarking: it demonstrates how to cross-culturally validate a moral judgment stimulus set, reveals where Dutch and US/Australian moral intuitions diverge, and provides the first European validation of both instruments — enabling more ecologically valid, culturally calibrated moral judgment benchmarks for LLMs.

## 2. Benchmark/eval design features
The paper validates two moral stimulus sets covering seven moral foundations (physical care, emotional care, fairness, liberty, loyalty, authority, sanctity) plus social norms violations and neutral content.

**MFV component:** 120 one-sentence Dutch-translated vignettes, 15 per foundation. Each vignette rated on: moral wrongness (1–5 Likert), comprehensibility, imaginability, frequency, and emotional response. Participants also assigned each vignette to a foundation category (classification task).

**SMID component:** 120 images (10 moral + 10 immoral per foundation; 10 neutral high-arousal + 10 neutral low-arousal). Each image rated on: moral valence, arousal, and degree to which each foundation is perceived.

Key psychometric findings: Classification rates range from 85.63% (fairness) to 60.2% (loyalty) for MFV. For SMID, 63% of images correctly categorized overall; care images had 95% recall while fairness and loyalty images had 50% and 35% respectively.

## 3. Task format & example item
Participants rated vignettes on 5-point Likert scales and identified the moral violation type. Example items (p.5, Table 1):

Physical care: "U ziet een leraar die een leerling op de hand slaat met een liniaal voor het in slaap vallen in de klas." (You see a teacher hitting a student's hand with a ruler for falling asleep in class.)

Sanctity: "U ziet een man seks hebben met een bevroren kip voordat hij het voor het avondeten kookt." (You see a man having sex with a frozen chicken before cooking it for dinner.)

Social norms: "U ziet een vrouw die een telefoontje opneemt met het woord 'tot ziens' inplaats van 'hallo'." (You see a woman answering a phone call with the word 'goodbye' instead of 'hello'.)

For images: participants rated general valence, arousal, morality, and the degree to which the image makes them think about each moral foundation on 5-point scales.

## 4. Scoring / grading methodology
- Moral wrongness: 1–5 Likert scale ("How morally wrong is the displayed behavior?")
- Classification rate: percentage of participants correctly identifying the intended moral foundation
- Vignette-to-social-norms comparison: Tukey-Kramer test for multiple comparisons
- Image foundation specificity: one-sided t-tests comparing intended vs. non-intended foundation ratings
- Confusion matrix for image categorization (intended category vs. highest-rated foundation)
- Political orientation correlations using Pearson r
- No LLM scoring; all human-sourced ratings

## 5. Dataset construction & provenance
- **MFV**: 120 of 132 original English vignettes (Clifford et al., 2015) translated to Dutch by native Dutch author; cultural adjustments made collaboratively (e.g., Dutch-specific sports, place references)
- **SMID images**: Selected from the 2,941-image SMID database using a circumplex model of arousal × morality; 20 images per foundation per quadrant → 120 total (10 moral, 10 immoral per foundation + 20 neutral)
- **Participants**: 648 surveys collected via Prolific (Dutch native speakers, Dutch nationality, located in Netherlands); 62 excluded for incomplete responses or completion under 6 minutes → N=586
- **Demographics**: Mean age 28.39 (SD=8.89); 57% male; 87% White ethnicity; left-leaning (M=38.95 on 0-100 scale)
- **Rating design**: Each participant rated 5 random vignettes + 5 random images (within-subjects design); ~22 ratings per stimulus
- **Data availability**: All data, code, and stimuli at https://osf.io/9gnza; Open Access

## 6. Validity evidence
- **Construct validity (MFV)**: 97% of vignettes rated more morally wrong than social norm items; Tukey-Kramer tests confirm all foundations significantly > social norms (all p<.001) (p.10-11)
- **Classification validity**: 97% of vignettes correctly categorized overall; only 4 vignettes misclassified to non-intended categories (p.11)
- **Convergent validity**: Pattern of wrongness ratings across foundations (physical care highest, loyalty lowest) replicates US findings (Clifford et al., 2015; Marques et al., 2020) (p.10)
- **Political orientation**: Right-leaning participants rate binding foundations (loyalty, authority, sanctity) as more wrong — replicating MFT predictions for Netherlands (p.11)
- **SMID convergent validity**: Images rated as moral vs. immoral show large, significant differences t(118)=10.63, p<.001, d=1.94 (p.12)
- **Cross-cultural comparison**: Pearson correlations of .3–.7 between Dutch and US/Australian SMID ratings — similar trends but with systematic cultural nuances (p.16)
- **Limitation**: ~22 ratings per stimulus (vs. larger samples in original studies) insufficient for factor analysis

## 7. Saturation / discrimination
- Loyalty and Authority vignettes show the lowest wrongness ratings (M=2.68 and M=2.89 respectively) and lower classification rates (60.2% and 69.97%), suggesting these are harder to discriminate and may represent floor effects in Dutch samples
- Fairness has highest classification rate (85.63%) but also shows unexpected correlation with conservative political orientation — diverging from US patterns
- SMID: Fairness (50% recall) and Loyalty/Sanctity (35% each) images show poor discrimination — these foundations harder to capture visually
- Some high-arousal items rated low-arousal and vice versa (9 and 23 items respectively) — suggesting arousal-morality circumplex approach is imperfect

## 8. Multiturn / agentic aspects
n/a — single-stimulus rating paradigm, no interaction sequences.

## 9. Key numbers
- N=586 Dutch crowd-workers (p.6)
- 38,460+ individual judgments (p.1)
- 120 MFV vignettes, 8 categories × 15 items (p.5)
- Average ratings per vignette: M=21.97 (min 14, max 30) (p.8)
- Overall classification rate range: 60.2% (Loyalty) to 85.63% (Fairness) (p.11, Table 2)
- 4 vignettes misclassified to non-intended categories (p.11)
- Physical care wrongness M=4.09 SD=0.95; Loyalty M=2.68 SD=1.09; Social norms M=1.29 SD=0.67 (p.9, Table 2)
- 120 SMID images, average rated 21.88 times (min 10, max 36) (p.11)
- Moral vs. immoral image discrimination: t(118)=10.63, p<.001, d=1.94 (p.12)
- 63% of images correctly categorized; 87.92% accuracy (p.16)
- Care image recall: 95%; Fairness: 50%; Loyalty: 35%; Sanctity: 35%; Authority: 90%; Neutral: 80% (p.16)
- Political orientation × binding foundations: Loyalty r=.16*, Authority r=.21**, Sanctity r=.14* (p.11, Table 4)
- Cross-cultural correlations with US/AUS SMID ratings: .3 to .7 range (p.16)

## 10. Pitfalls & limitations
- ~22 ratings per stimulus is below typical scale validation standards; insufficient for factor analysis (p.18)
- No factor analysis of the Dutch MFV — cannot confirm the dimensional structure in Dutch context
- Sample skews young, educated, and left-leaning (Prolific sample) — not nationally representative
- Fairness shows unexpected correlation with conservative ideology in Dutch sample — may reflect instrument vs. cultural differences but remains unresolved
- SMID image selection was originally optimized for US/Australian raters; some images (e.g., prostitution/drug use for Sanctity) are less moralized in Dutch culture, reducing discriminability
- Study design not pre-registered
- Liberty not included in SMID image ratings (following original SMID; ongoing debate about liberty as a distinct foundation)
- Cannot directly compare MFV behavioral data to prior studies (no open-access prior data)

## 11. Novel ideas worth stealing
- **Circumplex-based image sampling**: Selecting images from arousal × morality quadrants ensures coverage of moral valence AND affective intensity — a sampling design directly applicable to multimodal moral benchmarks for LLMs
- **Foundation-specific classification as a validity check**: Asking participants to identify which moral foundation was violated (rather than just rating wrongness) provides both a validity signal and a grounding for LLM foundation attribution tasks
- **Cross-cultural comparison as a validation requirement**: Systematically comparing ratings to existing human data from other cultures (US, AU, Brazil) as part of the validation pipeline — models of moral judgment should be evaluated against this multi-country baseline
- **Parallel text + image instrument**: Running text vignettes and images through the same rating paradigm allows modal comparison — useful for testing whether LLMs respond consistently to moral content in different modalities
- **Separating wrongness from foundation attribution**: Having participants rate moral wrongness AND identify the foundation creates two orthogonal measures — some violations feel wrong without being clearly categorizable
- **Open data infrastructure**: All stimuli, ratings, and code on OSF — models for what a publicly accessible moral stimulus database should look like

## 12. Notable quotes
- "Moral judgments are shaped by socialization and cultural heritage. Understanding how moral considerations vary across the globe requires the systematic development of moral stimuli for use in different cultures and languages." (p.1)
- "images may offer increased ecological validity over text-based vignettes, which have been criticized for creating an artificial moral psychology of 'raceless, genderless strangers'" (p.3)
- "Dutch individuals are generally tolerant toward prostitution and illicit drug use...being confronted with these concepts may not have triggered moral emotions (e.g., disgust) in Dutch citizens" (p.19)
- "the existence of a moral foundation can be doubted if there is a lack of response to third-party transgressions of that foundation. Because the MFQ does not probe respondents' moral judgment of third-party transgressions, it may not be an ideal instrument for testing the existence of moral foundations." (p.2)

## 13. UNKNOWN / not in extract
- Individual-item MFV data for all 120 vignettes (available in OSF supplementary but not in extract)
- Factor analysis (not conducted due to sample size limitations)
- Whether Dutch translations were back-translated for verification
- Effect of randomization order on ratings
- Reliability (test-retest) estimates for the Dutch instrument
