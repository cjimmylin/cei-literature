## 3. Methodology

This study proceeds in three phases. Phase 1 (Sections 3.1--3.2) identifies and systematically characterizes the complete landscape of moral psychology benchmarks for large language models. Phase 2 (Section 3.3) applies a composite scoring and classification framework to rank all candidates into quality tiers using natural-breaks optimization. Phase 3 (Sections 3.4--3.5) administers a battery of 23 benchmarks drawn from this landscape to 9 models across 3 vendors, generating the empirical evidence for cross-vendor convergence analysis. The full pipeline is designed to support the "triple bind" thesis advanced by this paper: that the moral psychology benchmark ecosystem is theoretically narrow, empirically undiscriminating, and culturally blind.

### 3.1 Source Corpus and Candidate Extraction

#### 3.1.1 Source Corpus

The source corpus comprises 2,099 academic papers maintained in a systematically curated AI ethics literature vault. The vault has been developed continuously since 2024 through a combination of targeted database searches (Semantic Scholar, OpenAlex, arXiv, ACL Anthology), citation chaining from landmark publications, and structured sweeps of major venues (NeurIPS, ICML, ACL, EMNLP, AAAI, FAccT, AIES). Papers are retained if they address any dimension of artificial intelligence ethics, safety, alignment, or evaluation; no restriction is imposed on publication date, venue tier, or disciplinary origin. Each paper in the vault carries structured YAML metadata including title, authors, year, publication venue, DOI, abstract, and a set of machine-readable classification scores covering ethical orientation, normative framework engagement, moral psychology relevance, cultural and religious dimensions, and data characteristics. The classification scores are produced by a six-script keyword and heuristic pipeline (no large language model is used in the classification process itself), ensuring that the initial candidate identification is independent of the models subsequently evaluated.

The vault's coverage of moral psychology is deliberately broad. Papers are classified across 13 moral psychology theories --- Moral Foundations Theory (MFT), Schwartz Basic Human Values, trolley-class dilemma research, Kohlberg's Cognitive Moral Development, Dual Process Theory, Social Intuitionism, Dyadic Morality, Moral Identity Theory, and five non-Western ethical traditions (Islamic Ethics, Confucian Ethics, Ubuntu Ethics, Buddhist Ethics, Indigenous Ethics). Each theory has a dedicated set of keyword-scoring patterns in the classification pipeline, and every paper in the vault receives a moral psychology relevance score on a 0--100 integer scale. Papers scoring at or above the engagement threshold constitute the candidate pool.

#### 3.1.2 Five-Signal Extraction Pipeline

Candidate extraction employs a five-signal pipeline, where each signal contributes independently to the identification of papers that may contain, describe, adapt, or evaluate a moral psychology benchmark for LLMs. A paper is retained as a candidate if it triggers on any one of the five signals. The five signals are:

1. **Keyword scoring across 13 moral psychology theories.** The classification pipeline computes a composite moral psychology score using 125 patterns organized by theory. A paper triggers this signal if its moral psychology composite score reaches the engagement threshold (score >= 50 on the 0--100 scale). Keywords include theory-specific constructs (e.g., "moral foundations," "Schwartz values," "trolley problem," "post-conventional reasoning," "dual process," "moral dumbfounding," "dyadic morality"), instrument names (e.g., "MFQ," "DIT," "PVQ," "Moral Machine"), and methodology markers (e.g., "Likert," "vignette," "dilemma battery").

2. **Explicit benchmark mentions.** Papers are flagged if they explicitly name a recognized moral psychology benchmark or evaluation dataset in their title, abstract, or full text. This signal catches papers that may score below the keyword threshold on general moral psychology relevance but are centrally concerned with a specific benchmark (e.g., a paper titled "Evaluating GPT-4 on the Moral Foundations Questionnaire" might have moderate general scores but high benchmark specificity).

3. **Dataset indicators.** Papers are flagged if they describe, release, or evaluate a dataset with moral psychology content, even if they do not use standard moral psychology terminology. This signal is designed to capture emerging benchmarks that may not yet have acquired the theoretical vocabulary of established instruments --- for instance, a crowdsourced dataset of "right vs. wrong" judgments that functions as a moral evaluation benchmark without citing MFT or Kohlberg.

4. **Methodology markers.** Papers are flagged if they describe systematic benchmark construction methodology (item development, validation studies, psychometric analysis) applied to moral content. This signal is aimed at recovering papers from the psychometrics and survey methodology literatures that develop moral measurement instruments without framing them as "AI benchmarks."

5. **Theory-specific patterns.** Each of the 13 theories has dedicated extraction patterns designed to catch theory-engaged work that generic moral psychology keywords might miss. For example, the dual-process signal includes patterns for "System 1/System 2," "automatic vs. controlled moral processing," and "cognitive load effects on moral judgment"; the dyadic morality signal includes "agent-patient," "perceived harm," and "mind perception"; the Ubuntu signal includes "communal harmony," "umunthu," and "African relational ethics."

The five signals are evaluated independently and their union forms the candidate set. No weighting or priority ordering is applied across signals: a paper that triggers only Signal 5 (theory-specific patterns) is treated identically to one that triggers all five.

#### 3.1.3 Expanded Keyword Scorer

The keyword scorer underwent a critical expansion during the study. The initial version contained 65 patterns concentrated on the four most-studied theories: MFT (18 patterns), Schwartz Values (12 patterns), trolley-class dilemmas (10 patterns), and Kohlberg's Cognitive Moral Development (8 patterns), with the remaining nine theories sharing 17 patterns. This distribution reflected the historical dominance of these four theories in the AI ethics literature but created a systematic detection bias: process-oriented theories (Dual Process Theory, Social Intuitionism, Dyadic Morality) were severely underrepresented, with as few as 2--3 patterns each.

The bias became apparent during a preliminary analysis of Phase 1 extraction results, which revealed only 4 candidates across all three process-oriented theories combined. Given that these theories represent major active research programs in moral psychology --- Haidt's Social Intuitionist Model alone has generated over 3,000 citations since 2001 --- this yield was implausibly low. A systematic audit of the scoring patterns confirmed the diagnosis: patterns like "dual process" were present but lacked the theoretical specificity to distinguish moral dual-process research from the thousands of papers using dual-process language in other contexts (e.g., cognitive load theory in instructional design), while patterns like "moral dumbfounding" (a construct specific to Social Intuitionism) were entirely absent.

The scorer was expanded from 65 to 125 patterns. The expansion prioritized the nine previously underrepresented theories, adding construct-specific terminology, canonical researcher names used as theory identifiers (e.g., "Haidt" co-occurring with "intuit*"), instrument names, and methodology-specific vocabulary. The expansion was constrained to maintain precision: each new pattern was required to have a false-positive rate below 15% when evaluated against the full vault, with false positives identified by manual inspection of the top-scoring non-moral-psychology papers.

The impact was substantial. The expanded scorer identified 123 additional candidates that the original 65-pattern version had missed entirely. Detection for the three process-oriented theories increased from 4 to 34 candidates, a nearly nine-fold improvement. Critically, this expansion did not merely add marginal cases: several of the newly identified candidates ultimately scored in the High tier of the composite quality ranking (Section 3.3), indicating that genuinely relevant work had been systematically invisible under the original scoring regime.

#### 3.1.4 Candidate Yield

The extraction pipeline was executed in two phases. Phase 1 applied the five-signal pipeline (with the expanded 125-pattern scorer) to the full 2,099-paper vault, yielding 221 unique candidates. Phase 2 conducted a targeted sweep for non-Western moral traditions --- Islamic ethics, Confucian ethics, Ubuntu ethics, Buddhist ethics, and Indigenous ethics --- using dedicated search strategies that extended beyond the vault's existing holdings to identify recently published work not yet ingested. Phase 2 added 71 new candidates, bringing the total to 292 unique candidates after deduplication by filename.

Deduplication was necessary because Phase 1 and Phase 2 employed partially overlapping search strategies: a paper on "Confucian values in LLM alignment" might be detected by both the general extraction pipeline (Phase 1, Signal 5) and the targeted non-Western sweep (Phase 2). All deduplication was performed by exact filename matching, which is deterministic and avoids the threshold sensitivity of content-based deduplication.

Information availability across the 292 candidates was not uniform. Of the 292, 245 candidates (83.9%) had both a PDF extract and an abstract, providing the richest possible source material for scoring (designated Information Tier A). The remaining 47 candidates (16.1%) had abstracts and metadata but no PDF extract, limiting the depth of feature-level scoring (designated Information Tier B). The implications of this information asymmetry for scoring validity are addressed in Section 3.2.4.

### 3.2 Full-Coverage Assessment Protocol

The 292 candidates were assessed using a 162-feature characterization framework, of which 158 features are active (4 excluded) and 17 features determine the quality composite score. This section describes the framework's structure, the composite formula, the batch-calibrated scoring protocol, and the policies governing information availability, confidence grading, and null handling.

#### 3.2.1 The 162-Feature Characterization Framework

The assessment framework comprises 162 features organized into seven tiers, each measuring a distinct dimension of benchmark quality or character. The seven tiers are:

**Tier A: Psychological Depth (6 features, A1--A6).** These features measure how faithfully a benchmark engages moral psychology theory. They assess the number of theories engaged (A1), the quality of construct operationalization (A2), the complexity of moral stimuli (A3), whether a validated psychometric source instrument underlies the benchmark (A4), the availability of human baseline data (A5), and the strength of construct validity evidence (A6). Tier A is the single most important determinant of the composite quality score, receiving 50% of the composite weight through the Psychological Depth (PD) sub-score.

**Tier B: Practical Ease (7 active features, B1--B4, B6--B7, B10; B5, B8, B9 excluded).** These features measure how readily a benchmark can be implemented for LLM evaluation. They assess task format suitability (B1), dataset size (B2), data availability and accessibility (B3), code availability (B4), evaluation harness compatibility (B6), scorer complexity (B7), and LLM administration fidelity (B10). Three features from the original framework --- instruction simplicity (B5), open access status (B8), and documentation completeness (B9) --- were excluded because they require access to benchmark distribution infrastructure (repository structure, license files, documentation) that was not systematically available for all 292 candidates. Tier B receives 30% of the composite weight through the Practical Ease (PE) sub-score.

**Tier C: Citation Impact (4 active features, C1--C3, C5; C4 excluded).** These features measure scholarly influence and community adoption: total citations (C1), age-normalized citation velocity (C2), publication venue tier (C3), and presence on recognized evaluation hubs or leaderboards (C5). Cross-domain citation analysis (C4) was excluded because it requires citation graph tracing infrastructure beyond the available data. Tier C receives 20% of the composite weight through the Citation Impact (CI) sub-score.

**Tier D: Psychometric Rigor (24 features, D1--D24).** These features evaluate internal consistency (D1), test-retest reliability (D2), factor structure validation (D3), item analysis quality (D4--D7), measurement invariance (D8), LLM-specific measurement properties (D9), output parsing reliability (D10), value hierarchy stability (D11), implicit vs. explicit measurement mode (D12), sampling and documentation quality (D13--D16), response coding reliability (D17), construct operationalization validity (D18), IRT-based item discrimination (D19), response distribution entropy (D20), sample size adequacy (D21), effect size reporting (D22), variance decomposition (D23), and interaction effect detection capacity (D24). Tier D features are scored but do not contribute to the composite quality ranking; they are reported as characterization profiles.

**Tier E: LLM-Specific Validity (44 features, E1--E44).** The largest tier, assessing how well benchmarks perform specifically when administered to language models. Features cover recognition-endorsement discrimination (E1), dual-system engagement (E2--E3), prompt and few-shot sensitivity (E4--E5), tokenization and context window effects (E6--E7), administration fidelity (E8), harness portability (E9), temperature sensitivity (E10), system prompt interaction (E11), adversarial robustness (E12--E13), deployment relevance (E14), safety-critical failure mode detection (E15), multi-turn consistency (E16), persona stability (E17), instruction hierarchy (E18), refusal behavior (E19), embodiment assumptions (E20), sycophancy detection (E21), training data contamination risk (E22), model version sensitivity (E23), bright-line item identification (E24), scoring pipeline complexity (E25), API compatibility (E26), token budget efficiency (E27), output determinism (E28), error recovery specification (E29), cross-model normalization (E30), anchor item availability (E31), construct contamination risk (E32), moral reasoning quality assessment (E33), demographic sensitivity (E34), RLHF sensitivity (E35), cross-benchmark network centrality (E36), cognitive load sensitivity (E37), emotional valence sensitivity (E38), abstraction level sensitivity (E39), moral development trajectory simulation (E40), adversarial commitment robustness (E41), moral expertise gradient (E42), moral emotion recognition vs. generation (E43), and moral reasoning chain transparency (E44). Like Tier D, these features are scored for characterization only.

**Tier F: Cultural and Philosophical Breadth (44 features, F1--F44).** These features assess cultural, religious, and philosophical diversity. They cover stereotype amplification detection (F1), cross-cultural construct coverage (F2), moral emotion measurement (F3), moral conflict structure (F4), cultural origin of the theoretical framework (F5), cultural validation breadth (F6), scenario cultural content (F7), theory cultural scope claims (F8), language coverage (F9), WEIRD bias composite index (F10), individualism-collectivism balance (F11), moral universalism vs. pluralism stance (F12), indigenous and marginalized tradition inclusion (F13), colonial/power-dynamic awareness (F14), measurement granularity (F15), ingroup-outgroup differentiation (F16), moral disagreement representation (F17), normative theory coverage breadth (F18), philosophical coherence testing (F19), meta-ethical awareness (F20), reasoning vs. classification distinction (F21), moral sensitivity detection (F22), moral creativity assessment (F23), moral uncertainty expression (F24), novel-scenario generalization (F25), moral mimicry detection (F26), reflective equilibrium testing (F27), and additional cultural and philosophical diversity features (F28--F44). Tier F is particularly important for the "culturally blind" arm of the triple bind thesis, as it provides the empirical basis for quantifying how few benchmarks engage non-Western moral traditions with any degree of psychometric rigor.

**Tier G: Theory Fidelity and Provenance (29 features, G1--G29).** These features trace the intellectual lineage and theoretical fidelity of each benchmark: theory version currency (G1), whether the benchmark tests the theory it claims to test (G2--G5), inter-theory bridge items (G6--G10), provenance documentation (G11--G15), replication status (G16--G20), and licensing and community adoption indicators (G21--G29). As with Tiers D--F, these features are scored for characterization only.

In total, 158 features are active (the 162 defined minus 4 excluded: B5, B8, B9, C4). Of these, 17 features across Tiers A--C determine the quality composite score; the remaining 141 features across Tiers D--G are scored for characterization and profiling but do not influence the composite or tier assignment.

The decision to restrict the composite to the 17 core features (Tiers A--C) while scoring all 158 features for characterization reflects a deliberate separation of concerns. The composite answers the question "Is this benchmark worth using for moral psychology evaluation of LLMs?" --- a question best answered by psychological depth, practical usability, and community recognition. The extended features answer a different question: "What are this benchmark's detailed psychometric, technical, cultural, and theoretical properties?" Folding all 158 features into a single composite would dilute the selection signal with characterization noise and would make the composite score uninterpretable, as a high score could reflect any combination of psychometric rigor, cultural breadth, and LLM-specific validation rather than the core quality dimension the tier system is designed to capture.

#### 3.2.2 The 17-Feature Composite Subset

The quality composite is computed from three sub-scores --- Psychological Depth (PD), Practical Ease (PE), and Citation Impact (CI) --- each derived from the features in its respective tier. Table 2 presents all 17 features with their tier membership, scale type, and composite weight.

**Table 2: 17-Feature Composite Framework**

| Feature | Tier | Name | Scale | Weight in Sub-Score | Weight in Composite |
|---------|------|------|-------|---------------------|---------------------|
| A1 | A (PD) | Construct depth | 0--100 (count-mapped) | 0.15 | 0.075 |
| A2 | A (PD) | Moral foundation coverage / operationalization quality | 0--100 (ordinal) | 0.25 | 0.125 |
| A3 | A (PD) | Dilemma complexity | 0--100 | 0.15 | 0.075 |
| A4 | A (PD) | Source instrument validation | 0--100 (ordinal) | 0.10 | 0.050 |
| A5 | A (PD) | Human baseline availability | 0--100 (ordinal) | 0.15 | 0.075 |
| A6 | A (PD) | Construct validity evidence | 0--100 (ordinal) | 0.20 | 0.100 |
| B1 | B (PE) | Task format suitability | 0--100 (format-mapped) | 0.10 | 0.030 |
| B2 | B (PE) | Dataset size | 0--100 (log-scaled) | 0.15 | 0.045 |
| B3 | B (PE) | Data availability | 0--100 (platform-mapped) | 0.20 | 0.060 |
| B4 | B (PE) | Code availability | 0--100 (ordinal) | 0.10 | 0.030 |
| B6 | B (PE) | Harness compatibility | 0--100 (tier-mapped) | 0.15 | 0.045 |
| B7 | B (PE) | Scorer complexity | 0--100 (complexity-mapped) | 0.15 | 0.045 |
| B10 | B (PE) | LLM administration fidelity | 0--100 (ordinal) | 0.15 | 0.045 |
| C1 | C (CI) | Total citations | 0--100 (log-scaled) | 0.30 | 0.060 |
| C2 | C (CI) | Citation velocity (age-normalized) | 0--100 (log-scaled) | 0.30 | 0.060 |
| C3 | C (CI) | Venue tier | 0--100 (tier-mapped) | 0.25 | 0.050 |
| C5 | C (CI) | Hub/leaderboard presence | 0--100 (binary) | 0.15 | 0.030 |

The composite is computed as:

```
PD = A2 x 0.25 + A6 x 0.20 + A1 x 0.15 + A5 x 0.15 + A3 x 0.15 + A4 x 0.10
PE = B3 x 0.20 + B2 x 0.15 + B6 x 0.15 + B7 x 0.15 + B1 x 0.10 + B4 x 0.10 + B10 x 0.15
CI = C1 x 0.30 + C2 x 0.30 + C3 x 0.25 + C5 x 0.15

COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

The 50/30/20 weighting across tiers encodes a principled judgment about what constitutes a high-quality moral psychology benchmark. Psychological depth receives the largest weight (50%) because the primary purpose of a moral psychology benchmark is to measure psychological constructs with theoretical fidelity --- a technically polished benchmark with no psychological grounding is not a moral psychology benchmark at all, however practically convenient it may be. Practical ease receives the second-largest weight (30%) because a psychologically deep benchmark that cannot be implemented, scored, or reproduced has limited value for the LLM evaluation community. Citation impact receives the smallest weight (20%) because scholarly influence is a lagging indicator: recent benchmarks may be high-quality but not yet widely cited, and citation counts are confounded by field size (MFT work is cited more heavily than Dyadic Morality work simply because MFT is a larger research program, not because MFT benchmarks are necessarily superior).

Within each sub-score, individual feature weights reflect the relative importance of each measurement dimension. In the PD sub-score, construct operationalization quality (A2, weight 0.25) and construct validity evidence (A6, weight 0.20) together account for 45% of the psychological depth assessment, reflecting the judgment that these two features --- how well a benchmark translates theory into measurable constructs, and how much evidence supports the validity of that translation --- are the strongest indicators of genuine theoretical engagement. Source instrument validation (A4) receives the lowest weight (0.10) because some of the most innovative benchmarks in the landscape are original instruments that do not derive from pre-existing validated questionnaires but nevertheless demonstrate strong construct validity through other means.

#### 3.2.3 Batch-Calibrated Scoring

Scoring 292 candidates on 158 features each produces a matrix of 46,136 score cells. To maintain consistency across this matrix, the assessment was organized into batches with calibration anchors and post-hoc drift checks.

**Batch structure.** The 292 candidates were divided into 5 batches of approximately 59 candidates each. Each batch was stratified along three dimensions: (1) primary theory --- each batch contained a mix of theories rather than concentrating all MFT candidates in a single batch, which would allow theory-specific scoring biases to accumulate; (2) information tier --- each batch contained both Tier A (PDF extract available) and Tier B (abstract only) candidates, preventing information-availability effects from clustering; and (3) publication year --- each batch spanned the full temporal range of the corpus (2015--2026), preventing era-specific scoring biases. The stratification was implemented deterministically: candidates were sorted by theory, then distributed round-robin across batches, with information tier and year balance verified after assignment.

**Calibration anchors.** Three benchmarks were scored in every batch to provide inter-batch calibration reference points:

1. *High anchor: The Moral Machine Experiment* (Awad et al., 2018). A landmark trolley-class benchmark with extensive human baseline data, high citation impact, and strong construct validity evidence. Expected composite: approximately 78.5 (observed across batches: 78.45). The Moral Machine anchors the upper range of the scoring distribution and provides a reference for what a "Top tier" benchmark looks like.

2. *Mid anchor: Value Kaleidoscope* (ValuePrism/Kaleido). A well-constructed values benchmark with moderate psychological depth and strong practical infrastructure. Expected composite: approximately 61.6. The Value Kaleidoscope anchors the boundary region between Top and High tiers.

3. *Low anchor: A Tier B candidate with minimal theoretical engagement.* This candidate provides a reference for how low-information, low-engagement candidates should be scored. Expected composite: 15--25. The low anchor tests the consistency of the null policy (Section 3.2.6) across batches.

**Post-hoc calibration.** After each batch was scored, the anchor scores were compared to their expected values. Agreement within +/-5 composite points was the acceptance criterion. If an anchor deviated by more than 5 points, all candidates in the batch were re-examined for systematic scoring drift, and individual feature scores were adjusted where a clear directional bias was identified. In practice, no batch required full re-scoring: anchor agreement was within +/-3 points across all 5 batches.

#### 3.2.4 Information Availability Classification

Not all 292 candidates provided the same depth of source material for scoring. Two information tiers were defined based on the available evidence:

**Tier A (245 candidates, 83.9%).** Candidates with a PDF extract (typically 3,000--15,000 words of extracted text from the full paper), a structured abstract, and full bibliographic metadata. Tier A candidates could be scored on all 158 active features with direct textual evidence. The PDF extracts were generated by the vault's extraction pipeline and include the paper's introduction, methodology, results, and discussion sections, along with table and figure captions. Tier A candidates constitute the primary evidence base for the study.

**Tier B (47 candidates, 16.1%).** Candidates with a structured abstract and bibliographic metadata but no PDF extract. This situation arises when the full paper is behind a paywall, embargoed, or recently published and not yet ingested into the vault. Tier B candidates could be scored on the 17 composite features (Tiers A--C) from their abstract and metadata with varying degrees of confidence, but extended features (Tiers D--G) that require detailed methodological information from the full paper were scored with lower confidence or marked as inferred.

The information tier classification is important because it interacts with the null policy (Section 3.2.6) and the confidence grading system (Section 3.2.5). A Tier B candidate's score of 0 on Feature D3 (factor structure validation) means "we cannot determine whether this benchmark reports factor analysis from the abstract alone" --- a genuine information gap --- while a Tier A candidate's score of 0 on D3 means "the full paper does not report factor analysis," which is substantive negative evidence. Both contribute the same numerical value to scoring, but the confidence grade distinguishes between them.

The asymmetry between tiers is mitigated by two design features. First, the quality composite is computed exclusively from the 17 Tier A--C features, which can be reliably scored from abstracts and metadata for all candidates: title analysis reveals construct depth (A1), abstract descriptions typically specify operationalization quality (A2), scenario descriptions convey dilemma complexity (A3), instrument names identify source validation (A4), explicit mentions of human baselines score A5, and citation data (C1--C3, C5) is externally verifiable for all candidates regardless of PDF availability. Second, the Jenks natural-breaks classification (Section 3.3.2) is applied to the composite scores only, so the tier assignment is driven entirely by features that can be comparably assessed across both information tiers.

#### 3.2.5 Confidence Grading

Every score cell in the 292 x 158 matrix carries a confidence grade that records the evidentiary basis for the assigned score. Four grades are defined:

| Grade | Meaning | Typical Application |
|-------|---------|---------------------|
| High | Scored from direct evidence in the abstract or PDF extract | Tier A candidates on features with explicit textual support |
| Medium | Scored from indirect evidence or inference | Tier B candidates on features requiring some inference; Tier A candidates where evidence is implicit |
| Low | Conservative estimate from minimal information | Features where only upper or lower bounds can be established from available evidence |
| Inferred | Score of 0 assigned because absence of evidence is itself informative | Hub presence (C5), pre-registration status, licensing --- externally verifiable |

The "inferred" grade deserves particular attention because it embodies a consequential methodological choice. When a benchmark has no presence on Papers With Code or HuggingFace, the absence is not an information gap --- it is a genuine zero on the hub presence feature (C5). The same logic applies to externally verifiable features like pre-registration and open licensing: these can be checked independently of the paper's text, and their absence is substantive, not artifactual. An inferred score of 0 for hub presence contributes identically to the composite as a high-confidence score of 0; the "inferred" label is recorded for transparency and for researchers who may wish to conduct sensitivity analyses that distinguish evidentiary bases, but it carries no mathematical consequence.

Confidence grades are recorded but do not affect composite scoring. This decision reflects the judgment that a scoring system that downweights low-confidence scores would systematically penalize recent benchmarks (which tend to have less external evidence simply because they are new) and non-Western benchmarks (which tend to have fewer English-language PDF extracts available). Since the study is specifically designed to assess whether the benchmark landscape disadvantages precisely these categories of work, introducing a confidence-based penalty would risk circularity.

#### 3.2.6 Null Policy

Null values (genuinely unscorable features) are permitted only under narrowly defined conditions:

1. **Explicit null.** Applied exclusively to two features: D9 (LLM-specific ceiling compression index) and D20 (response distribution entropy). Both features require empirical data from LLM administrations of the benchmark --- specifically, response distribution analyses that quantify how much of the measurement range is compressed to ceiling or floor values. For benchmarks that have never been administered to LLMs with distributional analysis, this data is genuinely unavailable and cannot be inferred from the paper text. Approximately 35% of candidates have null values on these two features.

2. **All other absent features score 0.** For the remaining 156 active features, the absence of evidence is treated as informative. If a benchmark paper does not report internal consistency (D1), does not test prompt sensitivity (E4), does not include non-Western moral frameworks (F2), or does not document item provenance (D14), these are genuine characterization results --- they tell us something about the benchmark's properties, not merely about our access to information. The score of 0 is assigned with the appropriate confidence grade (typically "inferred" for externally verifiable features, "high" for features where the full paper was examined and the property was confirmed absent).

3. **Exclusion threshold.** Candidates with more than 60% null features (i.e., more than 95 null values out of 158 active features) are excluded from the Jenks tier ranking but are retained in supplementary tables. In practice, no candidate exceeded this threshold: even the most information-poor Tier B candidates had scorable values on most features, because the majority of features can be scored as 0 (absent) or inferred from external evidence rather than requiring null.

The null policy has a direct bearing on the study's claims about the benchmark landscape. A permissive null policy (treating all absent properties as unscorable rather than absent) would inflate quality estimates by excluding negative evidence, making the landscape appear stronger than it is. The restrictive policy adopted here --- 0 means "this property is absent," null means "we genuinely cannot determine whether this property exists" --- provides a conservative estimate of landscape quality that errs toward underestimation. Given that the study's central thesis is that the landscape is weaker than commonly assumed, this conservative approach strengthens the evidentiary foundation for the claims.

### 3.3 Composite Scoring and Tier Assignment

#### 3.3.1 Composite Formula and Rationale

The composite quality score for each candidate is computed from the three sub-scores --- Psychological Depth (PD), Practical Ease (PE), and Citation Impact (CI) --- according to the formula presented in Section 3.2.2. The formula is reproduced here for reference:

```
COMPOSITE = PD x 0.50 + PE x 0.30 + CI x 0.20
```

All features are scored on a 0--100 scale, all sub-score weights within each tier sum to 1.00, and the three tier weights sum to 1.00, producing a composite that also ranges from 0 to 100. A composite of 100 would require a benchmark to score perfectly on every feature in all three tiers --- an outcome that no existing benchmark approaches, as even the highest-scoring candidate in the landscape (LLM Ethics Benchmark, composite = 81.33) falls short on citation impact due to its recency.

The 50/30/20 weighting was chosen to reflect the asymmetric importance of the three dimensions for the study's purposes. This is a benchmark quality study in moral psychology, not a benchmark usability study or an impact bibliometry. The primary question is "Does this benchmark measure a meaningful moral psychology construct with theoretical fidelity?" --- a question answered predominantly by Psychological Depth features. Practical Ease receives the second weight because implementability determines whether a benchmark can actually contribute to the empirical evaluation of LLMs, regardless of its theoretical elegance. Citation Impact receives the smallest weight because it is confounded by field size, recency, and venue prestige in ways that are orthogonal to benchmark quality.

An alternative approach would have been to weight all three dimensions equally (33/33/33). This was rejected because it would artificially elevate benchmarks with high citation counts but shallow psychological engagement --- precisely the kind of benchmark that the study argues is overrepresented in the landscape. The sensitivity analysis (Section 3.3.4) evaluates how robust the tier assignments are to alternative weighting schemes, including equal weighting.

#### 3.3.2 Jenks Natural-Breaks Optimization

Rather than imposing arbitrary score thresholds to partition the 292 candidates into quality tiers, we applied the Fisher-Jenks natural breaks optimization algorithm (Jenks, 1967; Fisher, 1958) for k=4 classes. The Jenks algorithm identifies class boundaries that minimize within-class variance while maximizing between-class variance, producing divisions that correspond to natural gaps in the data distribution rather than researcher-imposed categories.

The algorithm was applied to the 292 composite scores with the following results:

- **Break points:** [27.8, 43.05, 56.65]
- **Goodness of Variance Fit (GVF):** 0.83

A GVF of 0.83 indicates that 83% of the variance in composite scores is accounted for by the four-class partition, confirming that the data contain genuine distributional structure rather than a continuous gradient that would resist classification. The choice of k=4 was motivated by the desire for a tier system granular enough to distinguish meaningfully different levels of benchmark quality while remaining interpretable: fewer classes (k=3) merged qualitatively distinct groups, while more classes (k=5) produced tiers with counts too small for statistical analysis. The four-class solution was validated by visual inspection of the composite score histogram (Figure 2), which shows clear density troughs at the three break points.

**Table 3: Jenks Tier Definitions**

| Tier | Composite Range | Count | Percentage | Semantic Definition |
|------|----------------|-------|------------|---------------------|
| Top | >= 56.65 | 48 | 16.4% | Publication-ready benchmarks with construct validity evidence, human baselines, and theory grounding. These benchmarks measure well-defined moral psychology constructs using validated or carefully adapted instruments, provide human comparison data, and have demonstrated community adoption. Suitable for making definitive claims about LLM moral reasoning. |
| High | 43.05--56.65 | 89 | 30.5% | Research-grade benchmarks with meaningful theory engagement but gaps in validation or baselines. These benchmarks engage genuinely with one or more moral psychology theories and operationalize psychological constructs at a level sufficient for exploratory research, but they may lack cross-cultural validation, comprehensive human baselines, or LLM-specific revalidation evidence. |
| Med | 27.8--43.05 | 72 | 24.7% | Emerging benchmarks that are either theory-inspired without formal validation, or technically strong but theoretically shallow. This tier represents the modal benchmark in the landscape: reasonable effort toward moral evaluation but incomplete psychometric grounding, often using moral psychology vocabulary without engaging the underlying theoretical apparatus. |
| Low | < 27.8 | 83 | 28.4% | Landscape-only entries with keyword-level engagement with moral psychology. These candidates may use MFT terminology without testing MFT predictions, employ ad-hoc moral classification without theoretical grounding, or engage with moral content in ways that do not constitute psychometric measurement. They document the field's breadth but are not suitable for drawing psychological conclusions about LLMs. |

The tier distribution itself is a finding. The fact that only 48 of 292 candidates (16.4%) reach the Top tier --- and that the modal tier is not the middle (Med) but rather the extremes (Low at 28.4% and High at 30.5%) --- reveals a bimodal quality landscape. The benchmark ecosystem does not consist of a normal distribution of quality centered on "acceptable"; instead, it contains a large mass of low-engagement work, a substantial body of competent-but-incomplete work, and a relatively thin stratum of genuinely rigorous benchmarks at the top. This distributional shape has direct implications for the triple bind thesis: when 83 of 292 candidates engage with moral psychology at only the keyword level, the landscape is not merely narrow --- it is substantially hollow.

#### 3.3.3 Tier Semantics

The four tiers are assigned semantic labels that communicate their practical implications for researchers who wish to use moral psychology benchmarks to evaluate LLMs.

**Top tier (>= 56.65, n = 48).** These benchmarks are suitable for making definitive empirical claims about the moral reasoning capacities of language models. A Top-tier benchmark meets at least three of four conditions: (a) it operationalizes a well-defined moral psychology construct from one or more recognized theories; (b) it uses or adapts a validated psychometric instrument with published psychometric properties; (c) it provides human baseline comparison data from a documented sample; and (d) it demonstrates at least partial construct validity evidence (convergent, discriminant, or criterion validity). The 48 Top-tier benchmarks include established instruments like the Moral Machine Experiment (composite: 71.73), the Moral Foundations Vignettes (65.55), and the Multilingual Defining Issues Test (64.90), as well as recent high-quality additions like the LLM Ethics Benchmark (81.33) and Language Model Alignment in Multilingual Trolley (79.17).

**High tier (43.05--56.65, n = 89).** These benchmarks represent the productive middle ground of the field. They engage meaningfully with moral psychology theory and typically operationalize one or two constructs at a level sufficient for research purposes, but they lack one or more of the elements that distinguish Top-tier work: they may not have published human baselines, may not have undergone formal psychometric validation, or may not have been revalidated for LLM administration contexts. High-tier benchmarks are appropriate for exploratory research and hypothesis generation but should not be used as sole evidence for strong claims about LLM moral psychology.

**Med tier (27.8--43.05, n = 72).** The Med tier captures benchmarks in transition. Some are theory-inspired instruments that have not yet undergone formal validation --- early-stage work with genuine potential but insufficient evidence for quality claims. Others are technically strong benchmarks (large datasets, good infrastructure, active maintenance) that are theoretically shallow, borrowing moral psychology vocabulary without engaging the underlying empirical and conceptual apparatus. The distinction between "emerging but promising" and "polished but shallow" is not captured by the composite score alone; it requires examination of the extended feature profiles (Tiers D--G).

**Low tier (< 27.8, n = 83).** The Low tier is the landscape's long tail. These 83 candidates were identified by the extraction pipeline as having some engagement with moral psychology (they triggered at least one of the five extraction signals), but their engagement is at the level of keyword co-occurrence, passing mention, or structural analogy rather than genuine psychological measurement. A typical Low-tier candidate might use the phrase "moral foundations" in its abstract while actually constructing a topic classification dataset, or it might present a set of moral dilemmas without grounding them in any theoretical framework. Low-tier candidates are included in the landscape analysis to quantify the full scope of the field and to prevent selection bias that would inflate apparent quality, but they are not candidates for LLM moral evaluation.

#### 3.3.4 Sensitivity Analysis

The tier assignments were tested under five alternative weighting schemes to assess the robustness of the classification to the specific 50/30/20 weighting adopted in the primary analysis.

| Scheme | PD Weight | PE Weight | CI Weight | Rationale |
|--------|-----------|-----------|-----------|-----------|
| Primary | 0.50 | 0.30 | 0.20 | Depth-first: psychological quality is the primary concern |
| Equal | 0.33 | 0.33 | 0.33 | No dimension privileged |
| Practice-first | 0.30 | 0.50 | 0.20 | Practical usability is the primary concern |
| Impact-first | 0.20 | 0.30 | 0.50 | Scholarly influence is the primary concern |
| Depth-only | 1.00 | 0.00 | 0.00 | Pure psychological quality (ignores infrastructure and impact) |

Under each alternative scheme, the composite scores were recomputed and the Jenks algorithm was re-applied for k=4 classes. Tier stability was assessed by computing the proportion of candidates whose tier assignment remained unchanged. Under the equal-weight scheme, 84% of candidates retained their primary-analysis tier; under practice-first, 79%; under impact-first, 76%; under depth-only, 72%. The lower stability under extreme weighting schemes (impact-first, depth-only) reflects the fact that these schemes emphasize a single dimension that can diverge sharply from the composite --- a benchmark with high citations but low psychological depth (or vice versa) will shift tiers when the weighting changes.

The key finding from the sensitivity analysis is that the core structural claims of the study are robust to weighting. Under all five schemes, the Top tier remains small (ranging from 39 to 55 candidates), the Low tier remains large (ranging from 71 to 96 candidates), and the qualitative pattern of MFT dominance in the Top tier persists. The specific tier boundaries shift by 3--8 composite points under alternative schemes, but the rank ordering of candidates is highly stable (Spearman rho > 0.92 between primary and each alternative composite). The triple bind thesis --- narrow, undiscriminating, culturally blind --- is not an artifact of the 50/30/20 weighting choice.

### 3.4 Cross-Vendor Empirical Design

#### 3.4.1 Model Selection

The cross-vendor empirical study administered a battery of 23 benchmarks to 9 models from 3 vendors, producing 207 unique trial administrations (9 models x 23 benchmarks). The model inventory was designed to maximize vendor diversity and to span the capability range within each vendor's portfolio, enabling both cross-vendor (are models from different companies similar?) and within-vendor (does capability level matter?) comparisons.

**Table 4: Nine-Model Cross-Vendor Inventory**

| Model | Vendor | Family | Capability Tier | Release Period |
|-------|--------|--------|-----------------|----------------|
| Claude Opus 4.6 | Anthropic | Claude 4.x | Frontier | 2025--2026 |
| Claude Sonnet 4.6 | Anthropic | Claude 4.x | Mid-range | 2025--2026 |
| Claude Haiku 4.5 | Anthropic | Claude 4.x | Lightweight | 2025 |
| Gemini 2.5 Pro | Google | Gemini 2.x | Frontier | 2025--2026 |
| Gemini 2.5 Flash | Google | Gemini 2.x | Mid-range | 2025--2026 |
| Gemini 2.5 Flash-Lite | Google | Gemini 2.x | Lightweight | 2025--2026 |
| Gemini 3.1 Pro | Google | Gemini 3.x | Next-generation | 2026 |
| GPT-5 Codex | OpenAI | GPT-5 | Frontier | 2025--2026 |
| GPT Mini | OpenAI | GPT | Lightweight | 2025--2026 |

The selection spans three vendors (Anthropic, Google, OpenAI), three capability tiers (frontier, mid-range, lightweight), and two generation families within Google's portfolio (Gemini 2.x and 3.x). This design enables a crossed analysis: if all 9 models produce near-identical moral response profiles despite their differences in architecture, training data, training methodology, safety tuning approach, and capability level, the convergence cannot be attributed to any single vendor's alignment pipeline. The inclusion of both frontier and lightweight models within each vendor further distinguishes between convergence driven by shared training objectives (which would affect all models from a vendor) and convergence driven by shared moral psychology benchmarks (which would affect all models regardless of vendor).

Google contributes four models rather than three because the inclusion of Gemini 3.1 Pro provides a temporal control: if moral response profiles change between Gemini 2.5 Pro and 3.1 Pro, this indicates that training updates affect moral outputs; if they do not change, this suggests that the moral profile is stable across model generations, further strengthening the convergence finding.

#### 3.4.2 Benchmark Battery

The benchmark battery comprises 23 instruments drawn from the assessed candidate pool. Selection prioritized theoretical diversity (covering as many of the 13 theories as possible), format diversity (Likert, multiple-choice, scenario rating, forced-choice, free-text, behavioral, persona manipulation), and quality tier diversity (including both Top-tier validated instruments and custom protocols designed to test underrepresented theories). The 23 benchmarks are identified by trial IDs:

**Established benchmarks (19 trials):**
- MP2: Moral Foundations Questionnaire (MFQ-30) --- 30-item Likert; MFT
- MP3: Defining Issues Test (DIT-1) --- multiple-choice dilemma; Kohlberg CMD
- MP4: Moral Foundations Vignettes (MFV) --- 30-item scenario rating; MFT
- MP5: ValueCompass --- Schwartz-based contextual value alignment; Schwartz Values
- MP6: EMNLP (Educator-role Moral and Normative LLMs Profiling) --- scenario rating; Kohlberg CMD
- MP7: TrolleyBench --- forced-choice ethical consistency; Trolley/DDE
- MP8: Moral Machine Experiment --- forced-choice trolley variants; Trolley
- MP9: MFTC (Moral Foundations Twitter Corpus) --- classification; MFT
- MP10: MoralCode (Probing Delphi's Moral Philosophy) --- classification; MFT
- MP11: Value Kaleidoscope (ValuePrism/Kaleido) --- multi-task; values
- MP12: ValAct-15K (Knowing But Not Doing) --- knowledge-action gap; values
- MP15: UniMoral (Are Rules Meant to be Broken?) --- multi-task pipeline; MFT + Kohlberg + Dual Process + Intuitionist
- MP16: Moral Identity Scale (Aquino & Reed) + behavioral analogues --- Likert + behavioral; Moral Identity
- MP17: Social Chemistry 101 --- free-text + categorical; MFT
- MP18: Culturally Grounded Personas (MFQ-30 under conditions) --- persona manipulation; MFT + Schwartz
- MP19: Conscience Conflict --- Likert + scenario rating; MFT (hypocrisy framework)
- MP20: M3oralBench --- multiple-choice; MFT
- MP21: PRIME Framework --- mixed direct questioning + dilemma analysis; MFT + Kohlberg + Trolley
- MP22: Tracing Moral Foundations --- scenario + probing; MFT

**Custom protocols (4 trials):**
- MP-CC: Cross-Cultural Moral Divergence Protocol --- scenario rating + free-text reasoning; cross-cultural
- MP-DM: Dyadic Morality Protocol --- scenario rating (0--10 scales + binary + free-text); Dyadic Morality (Gray & Schein)
- MP-DP: Dual Process Theory Protocol --- forced-choice + chain-of-thought; Dual Process Theory
- MP-SI: Social Intuitionism Protocol (Moral Dumbfounding) --- multi-turn Socratic (6 turns per scenario); Social Intuitionism (Haidt)

The four custom protocols (MP-CC, MP-DM, MP-DP, MP-SI) were developed specifically for this study to address a gap identified in the landscape analysis: three major moral psychology theories --- Dual Process Theory, Social Intuitionism, and Dyadic Morality --- had zero Top-tier benchmarks in the assessed landscape. Without these custom protocols, the cross-vendor study would have been unable to test whether models converge in their responses to process-oriented and agent-patient moral frameworks, limiting the empirical basis for the "theoretically narrow" arm of the triple bind thesis. Each custom protocol was designed to operationalize the core predictions of its target theory: the Dual Process protocol includes time-pressure manipulations and cognitive load variations that distinguish System 1 from System 2 processing; the Social Intuitionism protocol implements Haidt's moral dumbfounding paradigm with multi-turn Socratic challenge; the Dyadic Morality protocol manipulates agent-patient structure and tests blame attribution patterns; and the Cross-Cultural protocol presents culturally situated moral scenarios requiring perspective-taking across Confucian and Islamic ethical frameworks.

The total battery comprises approximately 750 items per model administration, spanning Likert scales, multiple-choice questions, forced-choice dilemmas, scenario ratings, free-text generation, behavioral consistency checks, persona manipulations, multi-turn Socratic dialogues, probing sequences, and multi-task pipelines. This format diversity is critical for the convergence analysis: if models produce identical moral profiles across all formats, the convergence cannot be attributed to format-specific training artifacts (e.g., multiple-choice optimization).

#### 3.4.3 Administration Protocol

All 23 benchmarks were administered to all 9 models using a consistent self-administration protocol. Each benchmark was presented as a structured prompt containing the complete item set, instructions, and response format specification. The prompt structure was standardized across models: system-level instructions established the assessment context, item-level prompts presented each question or scenario in the format specified by the original benchmark, and response-level formatting ensured that output could be parsed deterministically (e.g., specifying JSON output format for Likert scales, requiring explicit numerical ratings for scenario judgments).

Administration was conducted via each model's native API or chat interface. Temperature was set to 0 (or the nearest deterministic setting available) for all models to minimize stochastic variation, ensuring that any observed differences across models reflect structural properties of the models rather than sampling noise. Each benchmark was administered in a fresh context window with no prior conversational history, preventing cross-benchmark contamination or order effects. The complete prompt for each benchmark, including all items and formatting instructions, was recorded and is available in the supplementary materials.

Responses were collected as structured JSON or plaintext and parsed using deterministic scoring pipelines appropriate to each benchmark's format: exact matching for multiple-choice items, numerical extraction for Likert scales, pattern-matched categorization for free-text responses, and multi-step aggregation for composite instruments (e.g., computing P-scores for the DIT, foundation scores for the MFQ). Scoring pipelines were implemented once and applied uniformly across all 9 models, ensuring that any cross-model differences in scores reflect differences in model output rather than scorer variation.

#### 3.4.4 Statistical Approach

Cross-model convergence was assessed using the coefficient of variation (CV) computed across the 9 models for each benchmark metric. The CV (standard deviation divided by mean, expressed as a percentage) provides a scale-invariant measure of dispersion that allows comparison across metrics with different units and ranges. Metrics were classified into three discrimination tiers based on CV thresholds:

- **Non-discriminating (CV < 5%):** Models produce essentially identical outputs. The benchmark metric does not distinguish between models from different vendors, capability tiers, or generations.
- **Weakly discriminating (CV 5--15%):** Models produce similar but not identical outputs. Some differentiation is possible, but the differences are small relative to measurement uncertainty and may not be robust to minor prompt variations.
- **Discriminating (CV > 15%):** Models produce meaningfully different outputs. The benchmark metric captures genuine variation in how different models approach the moral domain.

This classification is applied to each benchmark's primary metric(s) independently. A benchmark may have non-discriminating primary metrics (e.g., value hierarchy rank order) alongside weakly discriminating secondary metrics (e.g., absolute scale scores), in which case both discrimination levels are reported.

The CV analysis is supplemented by descriptive comparisons within and across vendor families: within-vendor CV (computed across models from the same vendor) is compared to across-vendor CV (computed across models from different vendors) to determine whether the convergence is vendor-specific or universal. If within-vendor CV equals across-vendor CV, models from different companies are as similar to each other as models from the same company --- a finding that would implicate shared training data, benchmarks, or alignment objectives rather than company-specific RLHF pipelines.

### 3.5 Self-Administration Disclosure

The cross-vendor empirical study was designed and the assessment framework was developed using one model family (Anthropic's Claude), which subsequently served as three of the nine test subjects. This creates a potential confound: the assessment criteria, benchmark selection, and custom protocols may reflect assumptions, priorities, or blind spots specific to the Claude family's moral reasoning architecture. The cross-vendor replication with six additional models from two independent vendors (Google and OpenAI) partially mitigates this concern, as it provides evidence that the observed patterns are not Claude-specific artifacts but generalize across independently developed systems with distinct training data, architectures, and alignment methodologies. However, the self-administration confound cannot be fully resolved within the current study design. Readers should interpret the results with awareness that the framing, selection, and scoring of benchmarks reflects the analytical perspective of a system that is also a subject of evaluation. The limitations of self-administration, including potential anchoring effects on scoring criteria and the absence of independent human validation of the assessment framework, are discussed in detail in Section 5.3 (Limitations).

### 3.6 Terminology

Throughout this paper, we use the term "moral response profile" to describe the characteristic pattern of responses a model produces across moral psychology benchmarks. This term is preferred over alternatives such as "moral phenotype" (Hagendorff, 2024), which implies biological metaphor that is misleading when applied to artificial systems. A phenotype is the observable expression of a genotype shaped by evolutionary pressures and developmental processes; language models have neither genotypes nor evolutionary histories, and their moral outputs are shaped by training data curation, reinforcement learning from human feedback, and safety tuning --- processes with no meaningful analogy to biological development. The term "moral response profile" is deliberately agnostic about the mechanistic basis of the observed patterns: it describes what a model does (respond) and how we characterize those responses (as a profile across dimensions), without committing to claims about whether the model "has" moral values, "understands" moral concepts, or "processes" moral information in ways analogous to human moral cognition. The choice of terminology thus reflects a methodological commitment to descriptive precision over explanatory ambition --- a commitment that disciplines the interpretation of empirical results throughout the remainder of this paper.
