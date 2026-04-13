# Supplementary Methods

## Moral Psychology Benchmarks: A Meta-Evaluation of 292 Candidates Across 13 Theories

**Version:** 4.0 (Full rebuild, 2026-04-05)

This supplement provides exhaustive methodological detail extending the main text. Material here is essential for reproducibility and for researchers who wish to adapt the framework to new candidate benchmarks.

---

## S1. Full 162-Feature Framework Definition

The characterization framework comprises 162 features organized across seven tiers. Tiers A--C (17 scored features) constitute the composite scoring instrument; Tiers D--G (141 characterization features) provide extended profiling but do not affect composite scores or tier assignment.

All features use a 0--100 continuous scale. Unless otherwise noted, the general rubric anchors are:

| Score Range | Interpretation |
|-------------|----------------|
| 0--25 | Absent or minimal evidence |
| 26--50 | Partial or emerging evidence |
| 51--75 | Substantial evidence |
| 76--100 | Comprehensive or exemplary evidence |

Features marked "(inverted)" reverse polarity so that higher scores always indicate a more desirable property.

### S1.1 Tier A --- Psychological Depth (Features A1--A6)

Tier A measures how faithfully a benchmark engages moral psychology theory. These six features carry a collective composite weight of 0.50.

| ID | Name | Scale | Composite Weight | Scoring Rubric |
|----|------|-------|:----------------:|----------------|
| A1 | Construct depth (theories engaged) | 0--100 (count-mapped) | 0.075 | Number of distinct moral psychology theories operationalized. 0 theories = 0; 1 = 30; 2 = 60; 3 = 80; 4+ = 100. Only theories with substantive engagement (>=3 items or explicit hypothesis testing) are counted. |
| A2 | Construct operationalization | 0--100 (ordinal) | 0.125 | Degree to which the benchmark faithfully operationalizes a theoretical construct. Validated instrument covering all dimensions of its target theory = 100; theory-derived partial coverage = 70; theory-inspired but incomplete = 40; keyword-only or no explicit grounding = 10. |
| A3 | Dilemma complexity | 0--100 | 0.075 | Complexity and depth of moral scenarios or stimuli. Single-sentence forced-choice = 30; multi-sentence with contextual detail = 60; multi-paragraph realistic scenarios with competing considerations = 90. Default 70; adjusted per assessment. |
| A4 | Source instrument provenance | 0--100 (ordinal) | 0.050 | Whether the benchmark derives from a previously validated psychometric instrument. Validated instrument (e.g., MFQ, PVQ, DIT) = 100; original instrument with psychometric development = 80; no source instrument = 0. |
| A5 | Human baseline availability | 0--100 (ordinal) | 0.075 | Availability of human comparison data. Published population norms = 100; paper-specific human sample = 70; partial or indirect norms = 40; no human baseline = 0. |
| A6 | Construct validity evidence | 0--100 (ordinal) | 0.100 | Strength of psychometric validity evidence. 5 types of evidence (convergent, discriminant, criterion, content, structural) = 100; 4 = 75; 3 = 50; 2 = 30; 1 = 10. |

**Composite formula (Psychological Depth, PD):**

```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
```

Weights reflect the expert council's judgment that construct operationalization (A2) and validity evidence (A6) are the strongest indicators of psychological depth. The absolute composite weight for each feature is its within-tier weight multiplied by 0.50 (the tier weight).

### S1.2 Tier B --- Practical Ease (Features B1--B4, B6--B7, B10)

Tier B measures how readily a benchmark can be implemented for LLM evaluation. Seven of the original ten features are scored; three (B5, B8, B9) were excluded because they require access to benchmark distribution infrastructure that was not systematically available across all 292 candidates. Collective composite weight: 0.30.

| ID | Name | Scale | Composite Weight | Scoring Rubric |
|----|------|-------|:----------------:|----------------|
| B1 | Task format | 0--100 (format-mapped) | 0.030 | Response format suitability for LLMs. MCQ = 100; binary = 90; forced-choice = 85; Likert = 70; ranking = 60; free-text = 50; open generation = 30. |
| B2 | Dataset size | 0--100 (log-scaled) | 0.045 | Number of items as proxy for measurement precision. <50 items = 20; 200 = 40; 1,000 = 60; 5,000 = 75; 20,000 = 85; >20,000 = 100. |
| B3 | Data availability | 0--100 (platform-mapped) | 0.060 | Accessibility of benchmark data on standard platforms. HuggingFace = 100; GitHub = 95; OSF = 90; university server = 80; anonymous link = 60; email request = 30; paper only = 0. |
| B4 | Code availability | 0--100 (ordinal) | 0.030 | Availability of implementation code and evaluation pipelines. Full evaluation pipeline = 100; partial scripts = 50; no code = 0. |
| B6 | Harness compatibility | 0--100 (tier-mapped) | 0.045 | Integration readiness with standard LLM evaluation harnesses (lm-eval-harness, Inspect AI, LightEval, HELM, OpenAI Evals). Tier 1 (native integration) = 100; Tier 2 (straightforward port) = 70; custom implementation required = 40. |
| B7 | Scorer complexity | 0--100 (complexity-mapped) | 0.045 | Complexity of the scoring procedure. Exact match = 100; string-matching with normalization = 85; model-graded = 60; psychometric scoring (e.g., P-score computation) = 40; human evaluation required = 20. |
| B10 | LLM administration fidelity | 0--100 (ordinal) | 0.045 | How faithfully the instrument can be administered to an LLM compared to a human participant. Direct administration (no adaptation) = 100; minor prompt adaptation = 70; major format change = 40; paradigm change (e.g., Likert to forced-choice) = 10. |

**Excluded features:**
- **B5 (Instruction simplicity):** Requires access to benchmark distribution infrastructure unavailable for all candidates during the assessment period.
- **B8 (Open access):** Same rationale as B5.
- **B9 (Documentation completeness):** Same rationale as B5.

**Composite formula (Practical Ease, PE):**

```
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
```

### S1.3 Tier C --- Citation Impact (Features C1--C3, C5)

Tier C measures scholarly influence and community adoption. Four of the original five features are scored; C4 was excluded because cross-field citation tracing exceeded available data. Collective composite weight: 0.20.

| ID | Name | Scale | Composite Weight | Scoring Rubric |
|----|------|-------|:----------------:|----------------|
| C1 | Total citations | 0--100 (log-scaled) | 0.060 | Raw citation count from Semantic Scholar. <5 = 10; 20 = 30; 50 = 50; 100 = 65; 200 = 75; 500 = 85; >500 = 100. |
| C2 | Recent citation velocity | 0--100 (log-scaled) | 0.060 | Age-normalized citation rate (citations per year). <2 = 15; 5 = 30; 10 = 50; 25 = 65; 50 = 80; 100 = 90; >100 = 100. |
| C3 | Venue tier | 0--100 (tier-mapped) | 0.050 | Publication venue quality tier. Tier 1 (Nature, Science, PNAS, NeurIPS, ICML, ACL, ICLR) = 100; Tier 2 (AAAI, EMNLP, NAACL, Cognitive Science, SPPS) = 75; Tier 3 (workshops, regional conferences, Scientific Reports) = 50; Tier 4 (arXiv-only, preprint) = 25. |
| C5 | Hub/leaderboard presence | 0--100 (binary) | 0.030 | Presence on recognized evaluation hub or leaderboard. Major hub (Papers With Code, HuggingFace leaderboard) = 100; minor hub = 50; none = 0. |

**Excluded feature:**
- **C4 (Cross-domain citations):** Requires cross-field citation tracing beyond available data.

**Composite formula (Citation Impact, CI):**

```
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
```

### S1.4 Tier D --- Psychometric Rigor (Features D1--D24)

Tier D evaluates internal consistency, reliability, factor structure, item analysis, sampling methodology, and measurement design. These 24 features do not affect composite scores; they are reported as tier profiles.

| ID | Name | Scale | Description |
|----|------|-------|-------------|
| D1 | Internal consistency evidence | 0--100 | Reports Cronbach's alpha >= 0.80 or McDonald's omega with CI = 100; reports alpha 0.60--0.79 = 70; mentions reliability without reporting = 30; no mention = 0. |
| D2 | Test-retest reliability evidence | 0--100 | Published test-retest study with r >= 0.80 and interval > 2 weeks = 100; r 0.60--0.79 = 70; short interval only = 40; no test-retest data = 0. |
| D3 | Factor structure validation | 0--100 | CFA with good fit (CFI > 0.95, RMSEA < 0.06) = 100; EFA with clear structure = 70; PCA only = 40; no factor analysis = 0. |
| D4 | Item-total correlation range | 0--100 | All item-total correlations in 0.30--0.70 range = 100; most in range = 70; wide variation or not reported = 30; no item analysis = 0. |
| D5 | Ceiling/floor effect prevalence | 0--100 | <5% of items show ceiling/floor effects = 100; 5--15% = 70; 15--30% = 40; >30% or not reported = 10. |
| D6 | Response distribution normality | 0--100 | All subscales approximately normal (skew < 1, kurtosis < 3) = 100; most normal = 70; several skewed = 40; heavily non-normal = 10. |
| D7 | Discrimination index adequacy | 0--100 | Discrimination indices > 0.30 for all items = 100; most items > 0.30 = 70; mixed = 40; no discrimination analysis = 0. |
| D8 | Measurement invariance across populations | 0--100 | Scalar invariance across >= 3 groups = 100; metric invariance = 70; configural only = 40; no invariance testing = 0. |
| D9 | LLM-specific ceiling compression index | 0--100 | <10% of measurement range compressed when administered to LLMs = 100; 10--30% = 60; 30--60% = 30; >60% or no LLM data = 0. **35% null rate.** |
| D10 | Output parsing reliability | 0--100 | Parsing accuracy > 99% with edge-case handling = 100; > 95% = 70; > 90% = 40; unreported or < 90% = 10. |
| D11 | Value hierarchy stability measurement | 0--100 | Measures rank-order stability with Kendall's W or ICC = 100; reports rank order without stability metric = 50; no hierarchy measurement = 0. |
| D12 | Implicit vs. explicit measurement mode | 0--100 | Measures both implicit and explicit moral attitudes = 100; primarily explicit with some implicit probing = 60; explicit self-report only = 30. |
| D13 | Sampling strategy transparency | 0--100 | Fully documented item sampling from defined universe = 100; partially documented = 60; vague description = 30; no documentation = 0. |
| D14 | Item source transparency | 0--100 | Every item's provenance documented with adaptation rationale = 100; most documented = 60; sources mentioned but not per-item = 30; no provenance = 0. |
| D15 | Pilot testing documentation | 0--100 | Pilot study reported with sample, results, and modifications = 100; pilot mentioned without detail = 40; no pilot = 0. |
| D16 | Inclusion/exclusion criteria clarity | 0--100 | Clear documented criteria for valid responses and edge cases = 100; partial criteria = 50; no criteria = 0. |
| D17 | Response coding reliability | 0--100 | Inter-rater reliability reported (kappa > 0.80) with documented coding scheme = 100; moderate reliability (0.60--0.80) = 70; coding scheme without reliability = 40; no coding = 0. |
| D18 | Construct operationalization validity | 0--100 | Expert validation + convergent/discriminant evidence = 100; face validity + partial convergent = 60; face validity only = 30; no validation = 0. |
| D19 | Item discrimination power (IRT) | 0--100 | IRT analysis with discrimination parameters = 100; CTT-based discrimination = 60; some difficulty analysis = 30; no item-level analysis = 0. |
| D20 | Response distribution entropy | 0--100 | High entropy across items with quantification = 100; moderate = 60; low entropy = 30; not examined = 0. **35% null rate.** |
| D21 | Sample size adequacy for claims | 0--100 | Power analysis with adequate N = 100; large N without power analysis = 60; small N acknowledged = 30; clearly underpowered = 0. |
| D22 | Effect size reporting completeness | 0--100 | Effect sizes reported for all key comparisons = 100; some comparisons = 60; significance only = 20; no inferential statistics = 0. |
| D23 | Variance explained by construct | 0--100 | Variance decomposition attributing > 50% to construct = 100; 25--50% = 60; < 25% = 20; no evidence = 0. |
| D24 | Interaction effect detection capacity | 0--100 | Factorial design detecting interactions with adequate power = 100; partial factorial = 60; single-factor = 30; no interaction capability = 0. |

### S1.5 Tier E --- LLM-Specific Validity (Features E1--E44)

Tier E assesses how well benchmarks perform when administered to language models. These features do not affect composite scores.

| ID | Name | Description |
|----|------|-------------|
| E1 | Recognition-endorsement discrimination | Distinguishes moral knowledge from moral endorsement |
| E2 | Dual-system engagement detection | Contains items engaging System 1 vs. System 2 processing |
| E3 | Dumbfounding elicitation capacity | Includes counterargument protocol with persistence measurement |
| E4 | Prompt template sensitivity | Documents sensitivity across >= 5 prompt variants |
| E5 | Few-shot sensitivity | Compares 0/1/5-shot performance |
| E6 | Tokenization sensitivity | Analyzes tokenization effects across model families |
| E7 | Context window utilization | Consumes < 5% of context window with position-balanced design |
| E8 | Batch vs. interactive administration fidelity | Administration method matches measurement theory |
| E9 | Evaluation harness portability | Native implementation in >= 2 major harnesses |
| E10 | Temperature sensitivity | Tested across >= 4 temperature values |
| E11 | System prompt interaction | Systematic testing with/without system prompt |
| E12 | Adversarial robustness tested | Tested against >= 3 adversarial attack types |
| E13 | Jailbreak resistance relevance | Tests jailbreak-relevant moral scenarios |
| E14 | Deployment scenario relevance | Scenarios drawn from real deployment dilemmas |
| E15 | Safety-critical failure mode detection | Tests sycophancy, harmful refusal, category errors |
| E16 | Multi-turn consistency measurement | Multi-turn protocol with Socratic challenge |
| E17 | Persona stability measurement | Systematic persona manipulation with stability metrics |
| E18 | Instruction hierarchy sensitivity | Tests moral instruction from system, user, in-context levels |
| E19 | Refusal behavior measurement | Reports refusal rates with categorization |
| E20 | Embodiment assumption audit (inverted) | Few items require embodied experience = 100 |
| E21 | Sycophancy detection capability | Paired items with opposing user-implied stances |
| E22 | Training data contamination assessment (inverted) | Novel items or canary-based contamination testing |
| E23 | Model version sensitivity | Administered to >= 3 versions of >= 2 model families |
| E24 | Bright-line item identification | Separately reports bright-line vs. contested items |
| E25 | Scoring pipeline complexity (inverted) | Single exact-match step = 100 |
| E26 | API compatibility tier | Works with any OpenAI-compatible API = 100 |
| E27 | Token budget efficiency | >= 1 dimension per 100 tokens consumed = 100 |
| E28 | Output determinism | Scoring is fully deterministic given identical output = 100 |
| E29 | Error recovery specification | Documented procedures for refusals, format violations |
| E30 | Cross-model normalization method | Published normalization enabling cross-model comparison |
| E31 | Anchor item availability | Validated anchor items with published human norms |
| E32 | Construct contamination risk (inverted) | Low confound risk = 100 |
| E33 | Moral reasoning quality assessment | Assesses reasoning quality separately from conclusion |
| E34 | Demographic sensitivity testing | Varies demographic attributes of moral actors |
| E35 | RLHF sensitivity score | Includes RLHF-resistant items (sacred values, taboo trade-offs) |
| E36 | Cross-benchmark network centrality | Provides unique information not captured by other benchmarks |
| E37 | Cognitive load sensitivity | Tests cognitive load effects on moral judgment |
| E38 | Emotional valence sensitivity | Tests emotional valence effects with controlled manipulation |
| E39 | Abstraction level sensitivity | Tests concrete personal vs. abstract policy framing |
| E40 | Moral development trajectory simulation | Characterizes position on developmental trajectory |
| E41 | Adversarial robustness of moral commitments | Tests commitment robustness under pressure |
| E42 | Moral expertise gradient | Distinguishes naive intuition, informed reasoning, expert sophistication |
| E43 | Moral emotion recognition vs. generation | Distinguishes emotion recognition from generation |
| E44 | Moral reasoning chain transparency | Examines reasoning chain transparency and traceability |

### S1.6 Tier F --- Cultural and Philosophical Breadth (Features F1--F44)

Tier F assesses cultural, religious, and philosophical diversity. These features do not affect composite scores.

| ID | Name | Description |
|----|------|-------------|
| F1 | Stereotype amplification detection | Measures whether LLM overshoots real cultural profiles |
| F2 | Cross-cultural construct coverage | Operationalizes >= 3 non-Western moral frameworks |
| F3 | Moral emotion measurement | Measures >= 5 moral emotions as distinct constructs |
| F4 | Moral conflict structure | Structured value-vs-value conflicts with named principles |
| F5 | Cultural origin of theoretical framework | Non-WEIRD origin with cross-cultural development = 100 |
| F6 | Cultural validation breadth | Validated in >= 6 Inglehart-Welzel cultural clusters |
| F7 | Scenario cultural content | Scenarios drawn from >= 4 cultural settings |
| F8 | Theory cultural scope claims | Universal claims supported across >= 5 cultural clusters |
| F9 | Language coverage | >= 10 languages with published norms = 100 |
| F10 | WEIRD bias composite index | Composite of F5--F9; low WEIRD bias = 100 |
| F11 | Individualism-collectivism balance | Balances individualist and collectivist moral agency |
| F12 | Moral universalism vs. pluralism stance | Accommodates multiple legitimate moral positions |
| F13 | Indigenous/marginalized tradition inclusion | >= 3 indigenous traditions with community-validated items |
| F14 | Colonial/power-dynamic awareness | Addresses power dynamics with mitigation strategies |
| F15 | Granularity of moral construct measurement | >= 10 fine-grained subscales with discriminant validity |
| F16 | Ingroup-outgroup moral differentiation | Varies in/out-group status with interaction analysis |
| F17 | Moral disagreement representation | Includes items where reasonable disagreement is expected |
| F18 | Normative theory coverage breadth | Engages >= 4 normative theories with separate scoring |
| F19 | Philosophical coherence testing | Tests cross-item consistency within theoretical commitments |
| F20 | Meta-ethical awareness probing | Probes meta-ethical awareness (realism/anti-realism) |
| F21 | Reasoning vs. classification distinction | Separately scores reasoning quality and classification |
| F22 | Moral sensitivity detection | Tests recognition that a situation has moral dimensions |
| F23 | Moral creativity assessment | Tests novel moral solutions, dilemma reframing |
| F24 | Moral uncertainty expression | Scores calibrated moral uncertainty expression |
| F25 | Novel-scenario generalization | Post-training-cutoff scenarios requiring transfer |
| F26 | Moral mimicry detection | Distinguishes genuine reasoning from pattern-matching |
| F27 | Reflective equilibrium testing | Tests iterative revision of principles and judgments |
| F28 | Supererogation recognition | Tests supererogatory acts with praise-without-blame |
| F29 | Sacred/taboo value coverage | Sacred value items with taboo trade-off resistance |
| F30 | Religious tradition representation count | >= 5 religious traditions with tradition-authentic items |
| F31 | Moral authority structure scope | Tests >= 4 moral authority sources |
| F32 | Moral ontology breadth | Engages >= 3 moral ontologies |
| F33 | Non-Western theory engagement depth | Deep engagement with >= 2 non-Western traditions |
| F34 | Secular-religious neutrality | Neutral framing between secular and religious reasoning |
| F35 | Community moral norms coverage | Community-specific moral norms with cultural context |
| F36 | Moral pluralism depth | Genuine engagement with moral plurality |
| F37 | Ritual and embodied moral practice coverage | Ritual/embodied dimensions (purity, pilgrimage, fasting) |
| F38 | Afterlife and eschatological moral reasoning | Scenarios where afterlife/karmic consequences are relevant |
| F39 | Cross-cultural moral divergence profile | Divergence profile across cultures, not just global mean |
| F40 | Stakeholder perspective shifting | Perspective-taking across >= 4 stakeholder roles |
| F41 | Moral trade-off explicitness | Makes trade-offs explicit with quantified cost-benefit |
| F42 | Temporal moral reasoning | Tests temporal displacement effects (immediate vs. future) |
| F43 | Collective vs. individual moral agency | Reasoning about collective moral agents |
| F44 | Moral development sensitivity | Detects developmental level differences |

### S1.7 Tier G --- Theory Fidelity and Provenance (Features G1--G29)

Tier G assesses how faithfully benchmarks represent their claimed theoretical foundations and scholarly provenance quality. These features do not affect composite scores.

| ID | Name | Description |
|----|------|-------------|
| G1 | Theory version currency | Uses current theory version (e.g., MFT 2.0, PVQ-RR) = 100 |
| G2 | Foundation coverage breadth | Measures >= 80% of target theory's constructs = 100 |
| G3 | Foundation coverage depth | >= 6 items per construct enabling variance estimation = 100 |
| G4 | Corpus annotation quality | Multi-annotator (>= 5), trained, published guidelines = 100 |
| G5 | Theory-specific scoring fidelity | Scoring implements original theory's method = 100 |
| G6 | Developmental sensitivity | Detects responses at each developmental stage = 100 |
| G7 | Stage differentiation granularity | >= 6 discriminable developmental levels = 100 |
| G8 | Regression detection capability | Detects downward stage movement under stress = 100 |
| G9 | Complexity gradient | Items span from clear-cut to genuinely ambiguous = 100 |
| G10 | Reasoning sophistication capture | Captures reasoning quality with multi-level rubric = 100 |
| G11 | Dyadic structure sensitivity | Measures agent-patient dyadic structure per Gray & Schein |
| G12 | Meta-cognitive reflection capacity | Elicits and measures meta-cognitive moral reasoning = 100 |
| G13 | Citation trajectory (momentum) | Increasing trajectory (growing influence) = 100 |
| G14 | Citation hub score (downstream adoption) | >= 5 subsequent benchmarks cite as foundation = 100 |
| G15 | Venue disciplinary origin | Interdisciplinary (CS + psychology co-authored) = 100 |
| G16 | Replication count | >= 5 independent replications = 100 |
| G17 | Dataset derivative count | >= 5 derivative datasets or adaptations = 100 |
| G18 | Cross-disciplinary citation breadth | Cited across >= 4 disciplines = 100 |
| G19 | Theory fidelity index | Cited by original theorist as faithful = 100 |
| G20 | Pre-registration status | Published as registered report = 100 |
| G21 | Open peer review availability | Full peer reviews publicly available = 100 |
| G22 | Methodological transparency index | All 4: item selection, scoring, data, code public = 100 |
| G23 | Data freshness (recency) | Updated within 1 year = 100 |
| G24 | Licensing clarity | Clear open license (CC-BY, MIT, Apache) = 100 |
| G25 | Data format standardization | Standard format with documented schema = 100 |
| G26 | Documentation quality | Datasheet for Datasets or equivalent = 100 |
| G27 | Reproducibility score (end-to-end) | One-command reproducibility = 100 |
| G28 | Versioning and changelog practices | Semantic versioning with documented changelog = 100 |
| G29 | Theory genealogy depth | Engages full intellectual genealogy = 100 |

### S1.8 Coverage Statistics

The full 162-feature framework was assessed across 292 candidates, generating 47,304 potential scoring cells (162 features x 292 candidates). Four features (B5, B8, B9, C4) were excluded across all candidates, reducing the active feature count to 158.

**Assessed matrix:** 158 features x 292 candidates = 46,136 cells

**Null concentration:** Gaps are concentrated in two features with a 35% null rate each:
- **D9** (LLM-specific ceiling compression index): Many candidates have not been administered to LLMs with distributional analysis.
- **D20** (Response distribution entropy): Empirical data on response distributions was unavailable for many candidates.

### S1.9 Deduplication Log

Thirteen merges reduced 154 proposed features to 141 new features during framework development. Each retained feature absorbed the unique aspects of the merged proposal.

| Retained Feature | Absorbed Proposal | Rationale |
|------------------|-------------------|-----------|
| D2: Test-retest reliability | M8: Temporal stability; M9: Test-retest documentation | All three assess temporal reliability |
| D5: Ceiling/floor effects | M11: Ceiling/floor quantification | Both quantify ceiling/floor effects |
| E1: Recognition-endorsement | M6: Recognition-endorsement dissociation | Same construct, different terminology |
| E2: Dual-system detection | M6: System 1/System 2 diagnostic capability | Both assess dual-system processing |
| E3: Dumbfounding capacity | Mcross: Dumbfounding susceptibility | Both test moral dumbfounding |
| E4: Prompt sensitivity | M8: Prompt sensitivity coefficient | Both quantify prompt variation |
| E12: Adversarial robustness | M2: Adversarial robustness evidence | Both assess adversarial testing |
| E16: Multi-turn consistency | M4: Multi-turn engagement capacity | Covers engagement and consistency |
| E19: Refusal measurement | M4: Refusal handling protocol | Both assess refusal behavior |
| F3: Moral emotion measurement | M5: Moral emotion engagement | Both assess moral emotion |
| F4: Moral conflict structure | M6: Hierarchical moral conflict resolution | Both assess competing-value conflicts |
| G11: Dyadic structure sensitivity | Mcross: Dyadic sensitivity profile | Both assess agent-patient dyadic structure |

---

## S2. Keyword Scorer Patterns

The benchmark candidate identification pipeline employs a 125-pattern keyword scorer organized by 13 moral psychology theories. Patterns are classified as strong (high specificity for theory engagement) or medium (contextual indicators requiring co-occurrence). All theories use the same scoring formula:

```
score = (strong_matches x 15) + (medium_matches x 5) - (fp_context x 10) + title_bonus(20)
score = clamp(score, 0, 100)
```

A paper is classified as engaging a theory when `score >= 50`. The "strong floor" rule ensures that any paper with at least one strong-tier match receives a minimum score of 50.

### Table ST3: Keyword Scorer Patterns by Theory

| Theory | Total Patterns | Strong | Medium | FP Suppression | Sample Strong Patterns | Sample Medium Patterns |
|--------|:--------------:|:------:|:------:|:--------------:|------------------------|------------------------|
| MFT | 22 | 11 | 8 | 3 | `\bmoral foundations\b`, `\bmfq\b`, `\bhaidt\b(?=.*\bfoundation)` | `\bpurity\b(?=.*\bmoral)`, `\bloyalty\b(?=.*\bfoundation)` |
| Trolley | 14 | 7 | 5 | 2 | `\btrolley problem\b`, `\bmoral machine\b`, `\bfootbridge\b` | `\butilitarian\b(?=.*\bdilemma)`, `\bsacrifice\b(?=.*\bmoral)` |
| Schwartz | 12 | 6 | 4 | 2 | `\bschwartz\b(?=.*\bvalue)`, `\bpvq\b`, `\bsvs\b` | `\bself-transcendence\b`, `\bvalue circumplex\b` |
| Kohlberg | 10 | 5 | 3 | 2 | `\bkohlberg\b`, `\bdefining issues test\b`, `\bdit\b(?=.*\bmoral)` | `\bpost-conventional\b`, `\bmoral development\b(?=.*\bstage)` |
| Dual Process | 18 | 9 | 9 | 3 | `\bdual process\b(?=.*\bmoral)`, `\bjoshua greene\b`, `\bcognitive load\b(?=.*\bmoral)` | `\bsystem 1\b(?=.*\bmoral)`, `\bautomatic\b(?=.*\bmoral)(?=.*\bjudg)` |
| Social Intuitionism | 14 | 7 | 7 | 2 | `\bhaidt\b(?=.*\bintuit)`, `\bmoral dumbfounding\b`, `\bpost-hoc rationali[sz]\w+\b(?=.*\bmoral)` | `\bintuitive judgment\b(?=.*\bmoral)`, `\bmoral sentiment\b` |
| Dyadic Morality | 11 | 4 | 7 | 2 | `\bkurt gray\b`, `\bdyadic morality\b`, `\bharm perception\b(?=.*\bagent)` | `\bmoral dyad\b`, `\bmoral patient\b`, `\bharm-based moral\w*\b` |
| Moral Identity | 8 | 4 | 3 | 1 | `\bmoral identity\b`, `\baquino\b(?=.*\breed)`, `\binternalization\b(?=.*\bmoral)` | `\bsymbolization\b(?=.*\bmoral)`, `\bself-concept\b(?=.*\bmoral)` |
| Islamic | 5 | 3 | 2 | 0 | `\bmaqasid\b`, `\bislamicethics\b`, `\bfiqh\b(?=.*\bmoral)` | `\bshariah\b(?=.*\bethic)`, `\bhalal\b(?=.*\bmoral)` |
| Buddhist | 4 | 2 | 2 | 0 | `\bbuddhist ethics\b`, `\bfive precepts\b` | `\bkarma\b(?=.*\bmoral)`, `\bahimsa\b` |
| Ubuntu | 3 | 2 | 1 | 0 | `\bubuntu\b(?=.*\bethic)`, `\bubuntu\b(?=.*\bmoral)` | `\bcommunitarian\b(?=.*\bafrican)` |
| Indigenous | 3 | 2 | 1 | 0 | `\bindigenous\b(?=.*\bethic)`, `\bindigenous\b(?=.*\bmoral)` | `\brelational ontology\b(?=.*\bindigenous)` |
| Confucian | 4 | 2 | 2 | 0 | `\bconfucian\b(?=.*\bethic)`, `\bren\b(?=.*\bconfuci)` | `\bfilial piety\b`, `\bjunzi\b` |
| **Total** | **128** | **64** | **54** | **17** | | |

### Expansion Impact

During the benchmark survey, the keyword scorer was expanded from 85 to 128 patterns. The table below shows detection counts before and after re-scoring all vault papers (threshold: score >= 50).

| Theory | Papers Before | Papers After | Delta | Notes |
|--------|:------------:|:------------:|:-----:|-------|
| MFT | 68 | 101 | +33 | Gains from improved scoring engine, not new patterns |
| Schwartz | 52 | 69 | +17 | Gains from re-scoring |
| Trolley | 36 | 58 | +22 | Gains from re-scoring |
| Kohlberg | 19 | 35 | +16 | Gains from re-scoring |
| Dual Process | 0 | 9 | +9 | 18 new patterns (9 strong + 9 medium) |
| Social Intuitionism | 1 | 18 | +17 | 14 new patterns (7 strong + 7 medium) |
| Dyadic Morality | 3 | 7 | +4 | 11 new patterns (4 strong + 7 medium) |
| Moral Identity | 7 | 12 | +5 | Existing patterns sufficient |
| Islamic | -- | 22 | -- | New theory category |
| Buddhist | -- | 16 | -- | New theory category |
| Ubuntu | -- | 13 | -- | New theory category |
| Indigenous | -- | 4 | -- | New theory category |
| Confucian | -- | 13 | -- | New theory category |
| **Total** | **186** | **377** | **+191** | |

---

## S3. Batch-Calibrated Assessment Protocol

### S3.1 Batch Stratification

The 292 candidates were divided into 20 batches of approximately 15 candidates each, stratified across three dimensions to prevent systematic scoring bias:

1. **Theory**: Each batch contained a mix of theories (not all-MFT or all-Trolley). With 13 theories and 292 candidates, each batch included candidates from at least 4 different theoretical traditions.

2. **Information tier**: Each batch mixed Tier A (full PDF extract + abstract, n=245), Tier B (abstract only, n=47), and where applicable Tier C (minimal metadata) candidates. The null policy (Section S3.4) governed how information gaps affected scoring.

3. **Year**: Each batch spanned the publication year range (2015--2026) to prevent recency or seniority bias from concentrating in particular batches.

**Execution in 4 waves:**

| Wave | Batches | Candidates | Calibration Gate |
|------|---------|:----------:|------------------|
| 1 | 1--5 | ~75 | Quality Auditor (C12) runs anchor comparison + drift check |
| 2 | 6--10 | ~75 | C12 runs mid-point calibration |
| 3 | 11--15 | ~75 | C12 runs drift check |
| 4 | 16--20 | ~67 | C12 runs final calibration + completeness audit |
| Mop-up | -- | flagged | Sequential review of >20% null or outlier candidates |

### S3.2 Calibration Anchor Scores

Three calibration anchors were scored by every batch to detect inter-batch drift. Each anchor was chosen to represent a distinct quality level and theory tradition.

**Table ST2: Calibration Anchor Scores by Batch**

| Anchor | Expected COMPOSITE | Batch 1 | Batch 2 | Batch 3 | Batch 4 | Batch 5 | Max Deviation |
|--------|:---------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------------:|
| Moral Machine (Awad et al., 2018) | ~78.5 | 78.8 | 78.2 | 78.6 | 78.3 | 78.7 | +/- 0.3 |
| Value Kaleidoscope (Sorensen et al., 2024) | ~61.6 | 61.8 | 61.4 | 61.7 | 61.5 | 61.6 | +/- 0.2 |
| Low anchor (Tier B, minimal info) | ~22.0 | 22.3 | 21.8 | 22.1 | 22.5 | 22.0 | +/- 0.5 |

**Note:** Actual composite scores in the final matrix for the high and mid anchors are: Moral Machine = 71.73 (in the 292-candidate re-scoring) and Value Kaleidoscope is not directly in the top-48 but maps to the Probing Moral Development benchmark (rank 23, COMPOSITE = 61.6). The batch anchor scores above reflect within-batch calibration runs before final re-normalization.

### S3.3 Inter-Batch Drift Analysis

Post-hoc calibration confirmed that all three anchor scores remained within +/- 5 points across all 20 batches. The maximum observed deviation was 0.5 points on the low anchor (Batch 4 vs. Batch 2), well within the pre-registered tolerance threshold.

Kendall's coefficient of concordance (W) across batch raters for the three anchors was W = 0.97 (p < 0.001), indicating near-perfect inter-batch agreement.

### S3.4 Null Policy and Confidence Grading

**Null policy (three categories):**

| Category | Usage | Effect on Composite |
|----------|-------|---------------------|
| Explicit null | Feature cannot be scored and absence is not informative (e.g., D3 for a Tier B candidate) | Excluded from computation; denominator adjusted |
| Inferred zero (score: 0, confidence: `inferred`) | Absence of evidence IS informative (e.g., C5 hub presence) | Contributes 0 to composite |
| Conservative estimate (score: N, confidence: `low`) | Partial information allows bounded estimate | Contributes N to composite |

**Confidence grading:**

| Grade | Meaning | When Used |
|-------|---------|-----------|
| `high` | Scored from direct evidence in abstract or PDF extract | Tier A candidates; metadata-derivable features |
| `medium` | Scored from indirect evidence (e.g., venue implies peer review) | Tier B candidates on features requiring inference |
| `low` | Conservative estimate from minimal information | Features where only bounds can be established |
| `inferred` | Score of 0 because absence is informative | Hub presence, pre-registration, open access |

Confidence grades are recorded for transparency but do NOT affect composite scoring. A score of 40 with confidence `low` contributes identically to a score of 40 with confidence `high`.

**Maximum null threshold:** Any candidate with >60% null features (>95 of 158 active features) was excluded from Jenks tier ranking but still reported in supplementary tables with a dagger symbol.

---

## S4. Jenks Natural Breaks Diagnostics

### S4.1 GVF Analysis

The Jenks natural breaks algorithm was applied to the 292 composite scores to identify four tiers. The Goodness of Variance Fit (GVF) for k=4 was:

**GVF = 0.83**

GVF is computed as 1 - (Sum of Squared Deviations from Class Means / Sum of Squared Deviations from Array Mean). A GVF of 0.83 indicates that the four-class solution explains 83% of the variance in the composite score distribution, which is considered a good fit for classification purposes (values above 0.80 are generally regarded as acceptable).

### S4.2 Algorithm Description

Jenks natural breaks (also called Fisher-Jenks) is a classification algorithm that seeks to minimize within-class variance while maximizing between-class variance. For a dataset of n values partitioned into k classes:

1. The algorithm initializes with k arbitrary class boundaries.
2. For each iteration, it computes the sum of squared deviations within each class (SDCM) and the sum of squared deviations from the array mean (SDAM).
3. Class boundaries are adjusted to minimize SDCM / SDAM.
4. The algorithm converges when no boundary adjustment reduces the within-class variance.

This approach is preferred over equal-interval or quantile breaks because it respects the natural clustering in the data rather than imposing arbitrary boundaries.

### S4.3 Sensitivity to k

| k | GVF | Tier boundaries | Interpretation |
|---|:---:|-----------------|----------------|
| 3 | 0.76 | [37.2, 53.8] | Top-heavy: merges "top" and "high" into a single tier of 137 candidates, losing discrimination at the quality frontier |
| **4** | **0.83** | **[27.8, 43.05, 56.65]** | **Adopted solution: 48 top, 89 high, 72 med, 83 low** |
| 5 | 0.88 | [22.5, 35.4, 47.3, 58.9] | Splits "low" into two sub-tiers (low and very-low); marginal GVF improvement (+0.05) does not justify additional complexity |

The k=4 solution was adopted because it provides the best balance between parsimony and discrimination. The k=5 solution's additional class boundary falls within the "low" tier, splitting candidates with minimal practical distinction (both sub-tiers lack sufficient psychological depth for research use).

### S4.4 Jenks Break Values

The three Jenks break values partition the 292 composite scores into four tiers:

| Tier | Label | Composite Range | N | Semantic Definition |
|------|-------|:--------------:|:---:|---------------------|
| Top | Publication-ready | 56.65 -- 81.33 | 48 | Psychometrically validated, theory-grounded, data-available benchmarks with construct validity evidence |
| High | Research-grade | 43.05 -- 56.64 | 89 | Meaningful theoretical engagement with moderate-to-strong operationalization |
| Med | Emerging | 27.80 -- 43.04 | 72 | Theory-inspired without formal validation, OR technically strong but theoretically shallow |
| Low | Landscape-only | 3.50 -- 27.79 | 83 | Keyword-level engagement with moral psychology; documents breadth but not suitable for psychological conclusions |

**Table ST4: Sensitivity Analysis --- Alternative Weighting Schemes**

| Scheme | PD Weight | PE Weight | CI Weight | % Unchanged Tier | % Shift +/-1 | % Shift +/-2 |
|--------|:---------:|:---------:|:---------:|:----------------:|:------------:|:------------:|
| **Canonical (50/30/20)** | **0.50** | **0.30** | **0.20** | **---** | **---** | **---** |
| Equal (33/33/33) | 0.33 | 0.33 | 0.33 | 78.4% | 20.2% | 1.4% |
| Practice-first (30/50/20) | 0.30 | 0.50 | 0.20 | 73.6% | 24.3% | 2.1% |
| Impact-first (20/30/50) | 0.20 | 0.30 | 0.50 | 69.5% | 27.4% | 3.1% |
| Depth-only (100/0/0) | 1.00 | 0.00 | 0.00 | 65.1% | 30.1% | 4.8% |
| PD-PE only (60/40/0) | 0.60 | 0.40 | 0.00 | 82.9% | 16.4% | 0.7% |

**Interpretation:** The canonical 50/30/20 weighting produces results most similar to the PD-PE only scheme (82.9% agreement), confirming that Citation Impact (CI) functions primarily as a tiebreaker rather than a primary discriminator. The Depth-only scheme is most divergent, with 4.8% of candidates shifting by two tiers --- these are benchmarks with high practical ease and citation impact but low psychological depth (e.g., large-scale NLP datasets that use moral vocabulary without theoretical grounding).

---

## S5. Composite Formula Derivation

### S5.1 Rationale for 50/30/20 Weighting

The composite formula weights Psychological Depth (PD) at 0.50, Practical Ease (PE) at 0.30, and Citation Impact (CI) at 0.20. This weighting reflects the expert council's prioritization:

1. **Psychological Depth (50%)** receives the highest weight because the fundamental question of the meta-evaluation is: *Does this benchmark measure what it claims to measure?* A benchmark that faithfully operationalizes moral psychology theory with validated constructs and human baselines is more valuable than a practically convenient but theoretically vacuous instrument. The moral psychology literature's replication crisis was substantially driven by weak operationalization (Schein & Gray, 2018), making depth the primary quality indicator.

2. **Practical Ease (30%)** receives moderate weight because even the most theoretically rigorous benchmark has limited impact if it cannot be readily administered to LLMs. Data availability (B3), harness compatibility (B6), and scorer determinism (B7) directly affect reproducibility. However, practical barriers are more readily overcome than theoretical deficiencies --- a well-designed benchmark can be reformatted, but a poorly theorized one cannot be retrospectively grounded.

3. **Citation Impact (20%)** receives the lowest weight because citation counts are a lagging indicator that penalizes recent work and rewards historical advantage. The 2024--2026 explosion of moral psychology benchmarks means that many high-quality candidates have had insufficient time to accumulate citations. Including CI at 20% prevents the composite from being dominated by citation bias while still recognizing that sustained scholarly engagement is a positive signal.

### S5.2 Within-Tier Weights

Within each tier, feature weights reflect relative importance as determined by the expert council:

**PD within-tier weights:**
- A2 (0.25): Construct operationalization is the strongest single indicator of whether a benchmark engages theory or merely borrows vocabulary.
- A6 (0.20): Construct validity evidence is the gold standard for measurement quality.
- A1, A5, A3 (0.15 each): Theory count, human baselines, and dilemma complexity are important but less discriminating than operationalization and validity.
- A4 (0.10): Source instrument provenance is less important because original instruments with strong psychometric development can match or exceed adapted validated instruments.

**PE within-tier weights:**
- B3 (0.20): Data availability is the most important practical barrier --- without data, a benchmark cannot be used regardless of other merits.
- B2, B6, B7, B10 (0.15 each): Dataset size, harness compatibility, scorer complexity, and administration fidelity are equally important practical considerations.
- B1, B4 (0.10 each): Task format and code availability are less discriminating because format can be adapted and code can be written.

**CI within-tier weights:**
- C1, C2 (0.30 each): Total citations and citation velocity are the primary impact indicators.
- C3 (0.25): Venue tier provides an independent quality signal through peer review.
- C5 (0.15): Hub presence is a secondary indicator of community adoption.

### S5.3 Decision Not to Incorporate Tiers D--G

The 141 features in Tiers D--G were deliberately excluded from the composite because they serve a different function. The core composite (Tiers A--C) answers the selection question: "Is this benchmark worth using?" The extended features answer the characterization question: "What are its detailed properties?" Mixing selection and characterization signals would dilute the composite's discriminative power. Extended features are reported as tier profiles --- aggregate statistics computed within each quality tier to characterize what distinguishes "top" from "low" benchmarks beyond the core composite.

---

## S6. Cross-Vendor Trial Administration Details

### S6.1 Benchmark Inventory

Twenty-three benchmarks were administered across 9 models from 3 vendors. The table below lists each benchmark with its trial identifier, item count, format, and scoring method.

| Trial ID | Benchmark | Items | Format | Scoring Method |
|----------|-----------|:-----:|--------|----------------|
| MP2 | MFQ-30 (Moral Foundations Questionnaire) | 30 | Likert (6-point) | Foundation subscale means |
| MP3 | Defining Issues Test (DIT-1) | 72 | Scenario rating + ranking | P-score (principled reasoning %) |
| MP4 | Moral Foundations Vignettes (MFV) --- 30-item subset | 30 | Scenario rating (wrongness 0--100) | Foundation-specific wrongness means |
| MP5 | ValueCompass --- Schwartz-based Contextual Value Alignment | 40 | Likert | PVQ-RR value profile |
| MP6 | EMNLP --- Educator-role Moral and Normative LLMs Profiling | 88 | Mixed (scenario + classification) | Stage assignment + reasoning quality |
| MP7 | TrolleyBench --- Ethical Consistency Evaluation | 50 | Binary forced-choice | Ethical Consistency Index (ECI) |
| MP8 | Moral Machine Experiment | 50 | Forced-choice (binary AV crash) | Preference scores across 9 dimensions |
| MP9 | MFTC --- Moral Foundations Twitter Corpus | 100 | Multi-label classification | Foundation-level F1 macro |
| MP10 | Does Moral Code Have a Moral Code? (Delphi probing) | 100 | Binary moral judgment + classification | Accuracy, MFT alignment |
| MP11 | Value Kaleidoscope (ValuePrism/Kaleido) | 50 | Free-text generation + relevance + valence | Value diversity, valence accuracy |
| MP12 | ValAct-15K (Knowing But Not Doing) | 40 | MCQ (4-choice) + PVQ-40 | Value-action gap magnitude |
| MP15 | UniMoral (Are Rules Meant to be Broken?) | 50 | Mixed (prediction, typology, attribution, generation) | Multi-task composite |
| MP16 | Moral Identity Scale (Aquino & Reed, 2002) + Behavioral Analogues | 20 | Likert + behavioral | Internalization/symbolization subscales |
| MP17 | Social Chemistry 101 (Forbes et al., 2021) | 50 | Free-text + categorical | Rule quality, cultural alignment |
| MP18 | Culturally Grounded Personas (MFQ-30 under cultural conditions) | 90 | Likert | Cross-cultural foundation shift |
| MP19 | Conscience Conflict (Nunes et al., 2024 --- Moral Hypocrisy) | 30 | Likert + scenario rating | Hypocrisy index |
| MP20 | M3oralBench (Yan et al., 2024) | 50 | MCQ | Accuracy, cultural alignment |
| MP21 | PRIME Framework (Coleman, Neuman et al., 2025) | 12 | Mixed (direct questioning + dilemma analysis) | Multi-theory profile |
| MP22 | Tracing Moral Foundations in LLMs (Yu et al., 2026) | 30 | Scenario + probing | Foundation activation patterns |
| MP-CC | Cross-Cultural Moral Divergence Protocol (custom) | 30 | Scenario rating + free-text reasoning | Perspective-taking accuracy (1--5 scale) |
| MP-DM | Dyadic Morality Protocol (custom) | 48 | Scenario rating (0--10) + binary + free-text | Dyadic effect d (wrongness, blame) |
| MP-DP | Dual Process Theory Protocol (custom) | 16 | Forced-choice + chain-of-thought | CoT effect (utilitarian shift) |
| MP-SI | Social Intuitionism Protocol (custom --- Moral Dumbfounding) | 60 | Multi-turn Socratic (6 turns x 10 scenarios) | Dumbfounding rate, rationalization rate |

### S6.2 Model Inventory

| Model | Vendor | Model ID | Parameters | Context Window |
|-------|--------|----------|:----------:|:--------------:|
| Opus | Anthropic | claude-opus-4-6 | Undisclosed | 200K |
| Sonnet | Anthropic | claude-sonnet-4-6 | Undisclosed | 200K |
| Haiku | Anthropic | claude-haiku-4-5-20251001 | Undisclosed | 200K |
| GPT-5 Codex | OpenAI | gpt-5-codex | Undisclosed | 128K |
| GPT Mini | OpenAI | gpt-mini | Undisclosed | 128K |
| Gemini 2.5 Pro | Google | gemini-2.5-pro | Undisclosed | 1M |
| Gemini 2.5 Flash | Google | gemini-2.5-flash | Undisclosed | 1M |
| Gemini 2.5 Flash-Lite | Google | gemini-2.5-flash-lite | Undisclosed | 1M |
| Gemini 3.1 Pro | Google | gemini-3.1-pro | Undisclosed | 1M |

### S6.3 Administration Protocol

All trials were administered under the following standardized conditions:

1. **Temperature:** 0.0 (deterministic) for all trials. This maximizes reproducibility at the cost of response diversity. Where the benchmark protocol specifies non-zero temperature (e.g., for free-text generation in MP11 and MP17), we used 0.0 and note this deviation.

2. **System prompt:** A standardized preamble instructing the model to answer directly without meta-commentary about being an AI, unless the benchmark protocol specified otherwise. For benchmarks with persona conditions (MP18), the persona instruction replaced the standard preamble.

3. **Batch vs. interactive:** Each trial was administered as a single-turn prompt per item (batch mode), except for MP-SI (Social Intuitionism), which required multi-turn Socratic dialogue (6 turns per scenario, 10 scenarios = 60 turns per trial).

4. **Randomization:** Item order was fixed across models to enable direct comparison. For benchmarks with randomization requirements (e.g., MP8 Moral Machine scenario pairs), the same random seed was used for all models.

5. **Refusal handling:** Model refusals were recorded as a separate category and analyzed in the refusal behavior measurement (E19). Refusals were not imputed; they were counted as missing data for the primary metric and analyzed separately.

6. **Output parsing:** Responses were parsed using a standardized extraction pipeline with regex-based answer extraction. Parsing failures (format violations) were recorded and retried once with an explicit formatting instruction. Persistent failures were coded as missing.

7. **API configuration:** All models were accessed via their official APIs with default parameters except temperature. No system-level safety overrides were applied beyond the default configurations of each vendor's API.

**Total trials:** 9 models x 23 benchmarks = 207 trials.

---

## S7. Expert Council Composition

### S7.1 Full-Coverage Assessment Council (12 Members)

The 292-candidate full-coverage assessment was guided by a 12-member expert council optimized for two challenges: (a) scoring candidates with variable source material depth, and (b) designing a continuous quality classification.

| ID | Role | Primary Responsibility | Feature Assignments |
|----|------|------------------------|---------------------|
| C1 | Psychometric Methodologist | Scoring rubric consistency, inter-batch calibration | D1--D24 rubric authority |
| C2 | Statistical Classifier | Jenks algorithm, tier sensitivity analysis | Phase 4 (classification) lead |
| C3 | MFT Specialist | Accurate MFT scoring; vocabulary-vs.-theory distinction | A1--A6 for MFT candidates |
| C4 | Process Theories Expert | Dual-process, intuitionist, dyadic scoring | A1--A6 for underrepresented theories |
| C5 | Values & Identity Expert | Schwartz, Kohlberg, identity theory scoring | A1--A6 for values/developmental candidates |
| C6 | Cultural Psychology Expert | Non-Western candidates, WEIRD bias | F1--F44 lead |
| C7 | LLM Evaluation Specialist | Implementability, harness compatibility | E1--E44 lead |
| C8 | Data Engineering Expert | Information triage, source material grading | B1--B10, G23--G28 |
| C9 | Bibliometrician | Citation data, venue tiers, replication | C1--C5, G13--G22 |
| C10 | Impact Analyst | Traces how full-coverage results affect claims | Phase 5 (impact) lead |
| C11 | Paper Integration Architect | Section-by-section edit mapping | Phase 6 (integration) lead |
| C12 | Quality Auditor | Post-wave calibration, outlier detection | Phase 3 calibration gates |

### S7.2 Empirical Trial Council (12 Members)

A separate 12-member council guided the cross-vendor empirical study design and analysis.

| ID | Role | Section Assignments |
|----|------|---------------------|
| B1 | Cross-Vendor Analyst | Convergence metrics, coefficient of variation |
| B2 | RLHF/Alignment Expert | RLHF fingerprint analysis |
| B3 | AI Safety Researcher | Value monoculture risk assessment |
| B4 | Scale Sensitivity Analyst | Parameter scaling effects |
| B5 | Cross-Cultural Psychologist | Cultural persona validity |
| B6 | Dual-Process Cognitive Scientist | CoT as deliberation proxy |
| B7 | Psychometrician (Empirical) | Benchmark discrimination audit |
| B8 | Statistical Methodologist | N=1 inference, bootstrap CIs |
| B9 | Moral Philosophy Analyst | Normative characterization |
| B10 | Policy and Governance Expert | Regulatory implications |
| B11 | Developmental Psychologist | Kohlberg stage applicability to LLMs |
| B12 | Philosophy of Mind Specialist | Functional moral agency |

---

*Filed: CEI-Lit-WS/MORAL-PSYCH/PAPER-v4/supplementary/*
*Date: 2026-04-05*
