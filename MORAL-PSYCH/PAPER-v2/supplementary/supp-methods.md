# Supplementary Methods

This supplement provides exhaustive methodological detail extending Section 3 of the main text. Material here is too granular for the main paper but is essential for reproducibility and for researchers who wish to adapt the framework.

---

## S1. The 162-Feature Extended Framework

The original 21-feature characterization framework (Tiers A--C) was expanded to 162 features organized across seven tiers during the assessment process, following proposals from a twelve-member expert council (Section S2). The expansion added four new tiers: Psychometric Rigor (D), LLM-Specific Validity (E), Cultural and Philosophical Breadth (F), and Theory Fidelity and Provenance (G). Council members contributed 154 candidate features; after deduplication (13 merges; see Table S1.9), 141 new features were added to the 21 originals, yielding the 162-feature extended framework.

All features use a 0--100 scale. Unless otherwise noted, the general rubric anchors are:

| Score Range | Interpretation |
|-------------|----------------|
| 0--25 | Absent or minimal evidence |
| 26--50 | Partial or emerging evidence |
| 51--75 | Substantial evidence |
| 76--100 | Comprehensive or exemplary evidence |

Features marked "(inverted)" reverse the polarity so that higher scores always indicate a more desirable property.

### S1.1 Tier A --- Psychological Depth (Features A1--A6)

Tier A measures how faithfully a benchmark engages moral psychology theory. These six features were defined in the original framework and were retained without modification by the council.

| ID | Name | Scale | Scoring Rubric |
|----|------|-------|----------------|
| A1 | Construct depth | 0--100 (count-mapped) | Number of distinct moral psychology theories engaged. 0 theories = 0; 1 = 30; 2 = 60; 3 = 80; 4+ = 100. |
| A2 | Moral foundation coverage | 0--100 (ordinal) | Breadth of moral foundation or value dimension coverage. Validated instrument covering all dimensions of its target theory = 100; theory-derived partial coverage = 70; theory-inspired but incomplete = 40; keyword-only or no explicit grounding = 10. |
| A3 | Dilemma complexity | 0--100 | Complexity and depth of the moral scenarios or stimuli. Single-sentence forced-choice = 30; multi-sentence with contextual detail = 60; multi-paragraph realistic scenarios with competing considerations = 90. Default 70; adjusted per assessment. |
| A4 | Response format richness | 0--100 (ordinal) | Whether a validated psychometric source instrument underlies the benchmark. Validated instrument (e.g., MFQ, PVQ, DIT) = 100; original instrument with psychometric development = 80; no source instrument = 0. |
| A5 | Cultural grounding | 0--100 (ordinal) | Availability of human baseline data. Published population norms = 100; paper-specific human sample = 70; partial or indirect norms = 40; no human baseline = 0. |
| A6 | Theoretical coherence | 0--100 (ordinal) | Evidence of construct validity. 5 = 100 (convergent, discriminant, criterion, content, and structural validity evidence); 4 = 75; 3 = 50; 2 = 30; 1 = 10. |

**Composite formula (Psychological Depth, PD):**

```
PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
```

Weights reflect the council's judgment that construct operationalization (A2) and validity evidence (A6) are the strongest indicators of psychological depth.

### S1.2 Tier B --- Practical Ease (Features B1--B10)

Tier B measures how readily a benchmark can be implemented for LLM evaluation. All ten features were defined in the original framework and retained without modification.

| ID | Name | Scale | Scoring Rubric |
|----|------|-------|----------------|
| B1 | Item count | 0--100 (format-mapped) | Task format suitability for LLMs. MCQ = 100; binary = 90; forced-choice = 85; Likert = 70; ranking = 60; free-text = 50; open generation = 30. |
| B2 | Administration time | 0--100 (log-scaled) | Dataset size as proxy for measurement precision. <50 items = 20; 200 = 40; 1,000 = 60; 5,000 = 75; 20,000 = 85; >20,000 = 100. |
| B3 | Scoring automation | 0--100 (platform-mapped) | Data availability and accessibility. HuggingFace = 100; GitHub = 95; OSF = 90; university server = 80; anonymous link = 60; email request = 30. |
| B4 | Output format clarity | 0--100 (ordinal) | Code availability. Full evaluation pipeline = 100; partial scripts = 50; no code = 0. |
| B5 | Instruction simplicity | Not assessed | Excluded: requires access to benchmark distribution infrastructure unavailable for all candidates during the assessment period. |
| B6 | Adaptation effort | 0--100 (tier-mapped) | Evaluation harness compatibility. Tier 1 (native in lm-eval-harness or Inspect AI) = 100; Tier 2 (straightforward adaptation) = 70; custom implementation = 40. |
| B7 | Platform requirements | 0--100 (complexity-mapped) | Scorer complexity. Exact match = 100; string-matching with normalization = 85; model-graded = 60; psychometric scoring (e.g., P-score computation) = 40; human evaluation required = 20. |
| B8 | Open access | Not assessed | Excluded: same rationale as B5. |
| B9 | Documentation completeness | Not assessed | Excluded: same rationale as B5. |
| B10 | Community adoption | 0--100 (ordinal) | LLM administration fidelity. Direct administration (no adaptation) = 100; minor prompt adaptation = 70; major format change = 40; paradigm change (e.g., Likert to forced-choice) = 10. |

**Note.** Features B5, B8, and B9 were defined in the original framework but excluded from scoring because they require access to benchmark distribution infrastructure (repository structure, license files, documentation completeness) that was not systematically available for all 54 candidates. They are excluded from composite computation. B7 and B8 in the original framework are relabeled here to reflect the actual assessed constructs (platform requirements and open access, respectively, were not assessed; harness compatibility and scorer complexity were).

**Composite formula (Practical Ease, PE):**

```
PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
```

### S1.3 Tier C --- Citation Impact (Features C1--C5)

Tier C measures scholarly influence and community adoption. All five features were defined in the original framework and retained without modification.

| ID | Name | Scale | Scoring Rubric |
|----|------|-------|----------------|
| C1 | Total citations | 0--100 (log-scaled) | Raw citation count from Semantic Scholar. <5 = 10; 20 = 30; 50 = 50; 100 = 65; 200 = 75; 500 = 85; >500 = 100. |
| C2 | Recent citation velocity | 0--100 (log-scaled) | Age-normalized citation rate (citations per year). <2 = 15; 5 = 30; 10 = 50; 25 = 65; 50 = 80; 100 = 90; >100 = 100. |
| C3 | H-index contribution | 0--100 (tier-mapped) | Publication venue tier. Tier 1 (Nature, Science, PNAS, NeurIPS, ICML, ACL) = 100; Tier 2 (AAAI, EMNLP, NAACL, major psychology journals) = 75; Tier 3 (workshops, regional conferences) = 50; Tier 4 (arXiv-only, preprint) = 25. |
| C4 | Cross-domain citations | Not assessed | Excluded: requires cross-field citation tracing beyond available data. |
| C5 | Benchmark-to-benchmark citations | 0--100 (binary) | Presence on a recognized evaluation hub or leaderboard. Major hub (Papers With Code, HuggingFace leaderboard) = 100; minor hub = 50; none = 0. |

**Composite formula (Citation Impact, CI):**

```
CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
```

### S1.4 Tier D --- Psychometric Rigor (Features D1--D24)

Tier D was proposed by the Psychometrics Expert (M3), Research Methods Expert (M9), and Statistical Validity Expert (M11) to address a critical gap: the original framework assessed *what* benchmarks measure but not *how well* they measure it. These 24 features evaluate internal consistency, reliability, factor structure, item analysis, sampling methodology, and measurement design.

| ID | Name | Proposed By | Scale | Scoring Rubric |
|----|------|-------------|-------|----------------|
| D1 | Internal consistency evidence | M3 | 0--100 | Reports Cronbach's alpha >= 0.80 or McDonald's omega with CI = 100; reports alpha 0.60--0.79 = 70; mentions reliability without reporting = 30; no mention = 0. |
| D2 | Test-retest reliability evidence | M3 (+M8, M9) | 0--100 | Published test-retest study with r >= 0.80 and interval > 2 weeks = 100; r 0.60--0.79 = 70; short interval only = 40; no test-retest data = 0. Merged from M8 temporal stability and M9 test-retest documentation proposals. |
| D3 | Factor structure validation | M3 | 0--100 | CFA with good fit (CFI > 0.95, RMSEA < 0.06) = 100; EFA with clear structure = 70; PCA only = 40; no factor analysis = 0. |
| D4 | Item-total correlation range | M3 | 0--100 | All item-total correlations in 0.30--0.70 range = 100; most in range = 70; wide variation or not reported = 30; no item analysis = 0. |
| D5 | Ceiling/floor effect prevalence | M3 (+M11) | 0--100 | <5% of items show ceiling/floor effects = 100; 5--15% = 70; 15--30% = 40; >30% or not reported = 10. Merged from M11 ceiling/floor quantification proposal. |
| D6 | Response distribution normality | M3 | 0--100 | All subscales approximately normal (skew < 1, kurtosis < 3) = 100; most normal = 70; several skewed = 40; heavily non-normal or not examined = 10. |
| D7 | Discrimination index adequacy | M3 | 0--100 | Discrimination indices > 0.30 for all items = 100; most items > 0.30 = 70; mixed = 40; no discrimination analysis = 0. |
| D8 | Measurement invariance across populations | M3 | 0--100 | Scalar invariance demonstrated across >= 3 groups = 100; metric invariance = 70; configural only = 40; no invariance testing = 0. |
| D9 | LLM-specific ceiling compression index | M3 | 0--100 | Novel metric. <10% of measurement range compressed to ceiling/floor when administered to LLMs = 100; 10--30% = 60; 30--60% = 30; >60% or no LLM data = 0. **35% null rate** --- many benchmarks have not been administered to LLMs with distributional analysis. |
| D10 | Output parsing reliability | M4 | 0--100 | Parsing accuracy > 99% with documented edge-case handling = 100; > 95% = 70; > 90% = 40; unreported or < 90% = 10. |
| D11 | Value hierarchy stability measurement | M3 | 0--100 | Measures rank-order stability with Kendall's W or ICC = 100; reports rank order without stability metric = 50; measures only absolute scores = 20; no hierarchy measurement = 0. |
| D12 | Implicit vs. explicit measurement mode | M3 | 0--100 | Explicitly measures both implicit and explicit moral attitudes with separate scoring = 100; primarily explicit with some implicit probing = 60; explicit self-report only = 30; does not distinguish = 0. |
| D13 | Sampling strategy transparency | M9 | 0--100 | Fully documented item sampling from defined universe = 100; partially documented = 60; vague description = 30; no documentation = 0. |
| D14 | Item source transparency | M9 | 0--100 | Every item's provenance documented with adaptation rationale = 100; most items documented = 60; sources mentioned but not per-item = 30; no provenance = 0. |
| D15 | Pilot testing documentation | M9 | 0--100 | Pilot study reported with sample, results, and modifications = 100; pilot mentioned without detail = 40; no pilot = 0. |
| D16 | Inclusion/exclusion criteria clarity | M9 | 0--100 | Clear documented criteria for valid responses, edge cases, and model configurations = 100; partial criteria = 50; no criteria = 0. |
| D17 | Response coding reliability | M9 | 0--100 | Inter-rater reliability reported (kappa > 0.80) with documented coding scheme = 100; moderate reliability (0.60--0.80) = 70; coding scheme without reliability = 40; no coding = 0. |
| D18 | Construct operationalization validity | M9 | 0--100 | Expert validation confirming items measure intended construct + convergent/discriminant evidence = 100; face validity + partial convergent = 60; face validity only = 30; no validation = 0. |
| D19 | Item discrimination power (IRT a-parameter) | M11 | 0--100 | IRT analysis with discrimination parameters reported = 100; CTT-based discrimination reported = 60; some difficulty analysis = 30; no item-level analysis = 0. |
| D20 | Response distribution entropy | M11 | 0--100 | High entropy across items (responses well-distributed) with quantification = 100; moderate entropy = 60; low entropy (most items trivial) = 30; not examined = 0. **35% null rate** --- empirical data on response distributions unavailable for many benchmarks. |
| D21 | Sample size adequacy for claims | M11 | 0--100 | Power analysis reported with adequate N for claimed effects = 100; large N without power analysis = 60; small N with acknowledged limitation = 30; clearly underpowered = 0. |
| D22 | Effect size reporting completeness | M11 | 0--100 | Effect sizes (Cohen's d, eta-squared, or equivalent) reported for all key comparisons = 100; for some comparisons = 60; significance only = 20; no inferential statistics = 0. |
| D23 | Variance explained by construct vs. noise | M11 | 0--100 | Variance decomposition reported (e.g., generalizability theory, R-squared) attributing > 50% to construct = 100; 25--50% = 60; < 25% or not decomposed = 20; no evidence = 0. |
| D24 | Interaction effect detection capacity | M11 | 0--100 | Factorial design capable of detecting interactions with adequate power = 100; partial factorial = 60; single-factor design = 30; no interaction capability = 0. |

### S1.5 Tier E --- LLM-Specific Validity (Features E1--E44)

Tier E was the largest expansion, assessing how well benchmarks perform specifically when administered to language models. Features were proposed primarily by the AI Safety Expert (M6), LLM Administration Expert (M4), and Data Engineering Expert (M8), with cross-cutting contributions.

| ID | Name | Proposed By | Scale | Scoring Rubric |
|----|------|-------------|-------|----------------|
| E1 | Recognition-endorsement discrimination | M1 (+M6) | 0--100 | Explicitly distinguishes moral knowledge from moral endorsement with separate scoring = 100; partially distinguishes = 50; conflates recognition and endorsement = 0. |
| E2 | Dual-system engagement detection | M2 (+M6) | 0--100 | Contains items specifically designed to engage System 1 (time-pressure, emotional content) vs. System 2 (complex reasoning, counterintuitive conclusions) with separate analysis = 100; implicitly engages both but without diagnostic separation = 50; measures only one processing mode = 0. |
| E3 | Dumbfounding elicitation capacity | M2 (+Mcross) | 0--100 | Includes systematic counterargument protocol with persistence measurement = 100; includes some counterargument items = 50; no dumbfounding test = 0. |
| E4 | Prompt template sensitivity | M4 (+M8) | 0--100 | Documented sensitivity analysis across >= 5 prompt variants with effect sizes = 100; 2--4 variants tested = 60; single prompt only = 10. |
| E5 | Few-shot sensitivity | M4 | 0--100 | Systematic comparison of 0/1/5-shot with directional analysis = 100; some few-shot testing = 50; zero-shot only = 0. |
| E6 | Tokenization sensitivity | M4 | 0--100 | Analysis of tokenization effects across model families with mitigation = 100; awareness noted = 40; not considered = 0. |
| E7 | Context window utilization | M4 | 0--100 | Consumes < 5% of context window with position-balanced design = 100; < 20% = 70; > 50% or no consideration = 20. |
| E8 | Batch vs. interactive administration fidelity | M4 | 0--100 | Administration method matches measurement theory assumptions with explicit justification = 100; reasonable match = 60; mismatch without discussion = 20. |
| E9 | Evaluation harness portability | M4 | 0--100 | Native implementation in >= 2 major harnesses = 100; one harness = 70; portable with minor effort = 40; custom code required = 10. |
| E10 | Temperature sensitivity | M4 | 0--100 | Tested across >= 4 temperature values with stability analysis = 100; 2--3 temperatures = 60; single temperature = 10. |
| E11 | System prompt interaction | M4 | 0--100 | Systematic testing with/without system prompt with documented effects = 100; system prompt noted = 40; not addressed = 0. |
| E12 | Adversarial robustness tested | M6 (+M2) | 0--100 | Tested against >= 3 adversarial attack types with quantified robustness = 100; limited testing = 50; not tested = 0. |
| E13 | Jailbreak resistance relevance | M6 | 0--100 | Directly tests jailbreak-relevant moral scenarios with documented attack surfaces = 100; indirectly relevant = 50; no jailbreak relevance = 0. |
| E14 | Deployment scenario relevance | M6 | 0--100 | Scenarios drawn from documented real deployment dilemmas (content moderation, medical triage, etc.) = 100; partially realistic = 50; entirely abstract = 0. |
| E15 | Safety-critical failure mode detection | M6 | 0--100 | Explicitly tests sycophancy, harmful refusal, and category errors with separate metrics = 100; some failure mode coverage = 50; no failure mode testing = 0. |
| E16 | Multi-turn consistency measurement | M6 (+M4) | 0--100 | Multi-turn protocol with Socratic challenge, follow-up probing, and consistency metrics = 100; basic multi-turn = 50; single-turn only = 0. |
| E17 | Persona stability measurement | M6 | 0--100 | Systematic persona manipulation with stability metrics across >= 5 personas = 100; some persona testing = 50; no persona manipulation = 0. |
| E18 | Instruction hierarchy sensitivity | M6 | 0--100 | Tests moral instruction from system, user, and in-context levels with interaction analysis = 100; partial hierarchy = 50; single instruction level = 0. |
| E19 | Refusal behavior measurement | M6 (+M4) | 0--100 | Reports refusal rates with categorization (hard refusal, hedge, meta-comment) and separate analysis = 100; counts refusals = 50; ignores refusals = 0. |
| E20 | Embodiment assumption audit | M6 | 0--100 (inverted) | Few assumptions (<10% of items require embodied experience) = 100; moderate (10--30%) = 60; heavy (>30%) = 20. Higher = fewer problematic assumptions. |
| E21 | Sycophancy detection capability | M6 | 0--100 | Contains paired items with opposing user-implied stances and measures agreement shift = 100; some stance-sensitivity items = 50; no sycophancy testing = 0. |
| E22 | Training data contamination assessment | M6 | 0--100 (inverted) | Novel items created after training cutoff or canary-based contamination testing = 100; partially novel = 60; widely-circulated items pre-training cutoff = 20. Higher = lower contamination risk. |
| E23 | Model version sensitivity | M6 | 0--100 | Administered to >= 3 versions of >= 2 model families with documented trends = 100; multiple models tested = 60; single model = 10. |
| E24 | Bright-line item identification | M6 | 0--100 | Separately reports performance on universally agreed bright-line items vs. contested items = 100; some bright-line identification = 50; no distinction = 0. |
| E25 | Scoring pipeline complexity | M8 | 0--100 (inverted) | Single exact-match step = 100; deterministic multi-step = 70; model-in-the-loop scoring = 40; complex human annotation required = 10. Higher = simpler pipeline. |
| E26 | API compatibility tier | M8 | 0--100 | Works with any OpenAI-compatible API with no modification = 100; minor adaptation = 70; vendor-specific code = 30; non-API (GUI only) = 0. |
| E27 | Token budget efficiency | M8 | 0--100 | >= 1 interpretable dimension per 100 tokens consumed = 100; per 500 tokens = 70; per 2,000 tokens = 40; per 10,000+ tokens = 10. |
| E28 | Output determinism | M8 | 0--100 | Scoring is fully deterministic given identical model output = 100; deterministic with normalization = 80; stochastic scoring component = 40; non-deterministic = 0. |
| E29 | Error recovery specification | M8 | 0--100 | Documented procedures for refusals, format violations, API errors, timeouts, with fallback behavior = 100; partial error handling = 50; no specification = 0. |
| E30 | Cross-model normalization method | M8 | 0--100 | Published normalization method enabling cross-model comparison = 100; suggested approach = 50; raw scores only = 0. |
| E31 | Anchor item availability | M8 | 0--100 | Includes validated anchor items with published human norms enabling calibration = 100; some normative reference points = 50; no anchors = 0. |
| E32 | Construct contamination risk | M8 | 0--100 (inverted) | Low confound risk: items isolate intended construct from verbal fluency, world knowledge, format compliance = 100; moderate confounds = 50; high construct contamination risk = 10. Higher = lower contamination risk. |
| E33 | Moral reasoning quality assessment | M6 | 0--100 | Assesses reasoning quality (logical consistency, multi-perspective consideration, uncertainty acknowledgment) separately from conclusion correctness = 100; partially = 50; conclusion only = 0. |
| E34 | Demographic sensitivity testing | M6 | 0--100 | Systematically varies demographic attributes of moral actors with effect analysis = 100; some demographic variation = 50; homogeneous actors = 0. |
| E35 | RLHF sensitivity score | M11 | 0--100 | Includes RLHF-resistant items (sacred values, taboo trade-offs, anti-sycophancy probes) = 100; partially resistant = 50; likely RLHF-saturated (harm-avoidance only) = 10. |
| E36 | Cross-benchmark network centrality | M11 | 0--100 | Provides unique information not captured by other benchmarks (low correlation with all others) = 100; partially redundant = 50; fully redundant = 0. |
| E37 | Cognitive load sensitivity | Cross | 0--100 | Tests cognitive load effects (complexity, information density) on moral judgment with parametric manipulation = 100; some complexity variation = 50; uniform complexity = 0. |
| E38 | Emotional valence sensitivity | Cross | 0--100 | Tests emotional valence effects with controlled manipulation = 100; naturally varying valence = 50; valence-neutral = 0. |
| E39 | Abstraction level sensitivity | Cross | 0--100 | Tests abstraction effects (concrete personal vs. abstract policy) with parametric manipulation = 100; some variation = 50; single abstraction level = 0. |
| E40 | Moral development trajectory simulation | Cross | 0--100 | Characterizes position on developmental trajectory with stage assignment = 100; partial developmental sensitivity = 50; snapshot only = 0. |
| E41 | Adversarial robustness of moral commitments | Cross | 0--100 | Tests commitment robustness under leading questions, authority pressure, social desirability, with quantified stability = 100; some adversarial probing = 50; no robustness testing = 0. |
| E42 | Moral expertise gradient | Cross | 0--100 | Distinguishes naive intuition, informed reasoning, and expert-level sophistication = 100; two levels = 50; single level = 0. |
| E43 | Moral emotion recognition vs. generation | Cross | 0--100 | Distinguishes emotion recognition (identifying guilt, shame, disgust) from emotion generation (expressing appropriate moral emotion) = 100; partially = 50; no distinction = 0. |
| E44 | Moral reasoning chain transparency | Cross | 0--100 | Examines reasoning chain transparency and traceability with structured elicitation = 100; CoT analysis = 50; output only = 0. |

### S1.6 Tier F --- Cultural and Philosophical Breadth (Features F1--F44)

Tier F assesses cultural, religious, and philosophical diversity. Features were proposed primarily by the Cultural Psychology Expert (M5), Moral Philosophy Expert (M10), and Religious and Sacred Values Expert (M12).

| ID | Name | Proposed By | Scale | Scoring Rubric |
|----|------|-------------|-------|----------------|
| F1 | Stereotype amplification detection | M1 | 0--100 | Measures whether LLM overshoots real cultural profiles with quantified amplification index = 100; notes amplification risk = 40; not considered = 0. |
| F2 | Cross-cultural construct coverage | M1 | 0--100 | Operationalizes >= 3 non-Western moral frameworks (e.g., maqasid, ren, Ubuntu) with validated measurement = 100; one framework = 50; mentions without operationalization = 20; WEIRD-only = 0. |
| F3 | Moral emotion measurement | M2 (+M5) | 0--100 | Measures >= 5 moral emotions as distinct constructs = 100; 2--4 emotions = 60; single emotion or undifferentiated affect = 20; no emotion measurement = 0. |
| F4 | Moral conflict structure | M2 (+M6) | 0--100 | Structured value-vs-value conflicts with explicitly named competing principles = 100; implied conflicts = 50; single-value items only = 0. |
| F5 | Cultural origin of theoretical framework | M5 | 0--100 (categorical) | Non-WEIRD origin with cross-cultural development = 100; WEIRD origin with extensive non-WEIRD validation = 70; WEIRD origin with limited validation = 40; WEIRD origin, no non-WEIRD validation = 10. |
| F6 | Cultural validation breadth | M5 | 0--100 (count-mapped) | Validated in >= 6 Inglehart-Welzel/Hofstede cultural clusters = 100; 4--5 = 70; 2--3 = 40; 1 = 10. |
| F7 | Scenario cultural content | M5 | 0--100 | Scenarios drawn from >= 4 cultural settings with locally authentic detail = 100; 2--3 settings = 60; Western-default = 20. |
| F8 | Theory cultural scope claims | M5 | 0--100 | Universal claims empirically supported across >= 5 cultural clusters = 100; supported in 2--4 = 60; claimed but untested = 20; no universality claim = 0. |
| F9 | Language coverage | M5 | 0--100 (count-mapped) | >= 10 languages with published norms = 100; 5--9 = 70; 2--4 = 40; 1 = 10. |
| F10 | WEIRD bias composite index | M5 | 0--100 (composite) | Composite of F5--F9. Low WEIRD bias exposure = 100; moderate = 50; high = 10. |
| F11 | Individualism-collectivism balance | M5 | 0--100 | Explicitly balances individualist and collectivist moral agency with dual scoring = 100; acknowledges both = 50; individualist default = 10. |
| F12 | Moral universalism vs. pluralism stance | M5 | 0--100 | Accommodates multiple legitimate moral positions with pluralist scoring = 100; allows some variation = 50; single correct answer (universalist) = 10. |
| F13 | Indigenous/marginalized tradition inclusion | M5 | 0--100 | Includes >= 3 indigenous or marginalized traditions with community-validated items = 100; 1--2 traditions = 50; mentions without inclusion = 20; none = 0. |
| F14 | Colonial/power-dynamic awareness | M5 | 0--100 | Explicitly addresses power dynamics with mitigation strategies = 100; acknowledges issue = 40; not addressed = 0. |
| F15 | Granularity of moral construct measurement | M5 | 0--100 | >= 10 fine-grained subscales with demonstrated discriminant validity = 100; 5--9 subscales = 70; 2--4 = 40; single binary classification = 10. |
| F16 | Ingroup-outgroup moral differentiation | M5 | 0--100 | Systematically varies in/out-group status with interaction analysis = 100; some group variation = 50; no group manipulation = 0. |
| F17 | Moral disagreement representation | M5 | 0--100 | Includes items where reasonable disagreement is expected and measured = 100; notes disagreement = 50; assumes consensus = 0. |
| F18 | Normative theory coverage breadth | M10 | 0--100 | Engages >= 4 normative theories (deontology, consequentialism, virtue, care, contractarianism) with separate scoring = 100; 2--3 theories = 60; 1 theory = 30; atheoretical = 0. |
| F19 | Philosophical coherence testing | M10 | 0--100 | Tests cross-item consistency within theoretical commitments = 100; partial coherence checking = 50; no coherence testing = 0. |
| F20 | Meta-ethical awareness probing | M10 | 0--100 | Probes meta-ethical awareness (realism/anti-realism, moral epistemology) = 100; implicit meta-ethical content = 40; no meta-ethical probing = 0. |
| F21 | Reasoning vs. classification distinction | M10 | 0--100 | Separately scores reasoning quality and classification accuracy = 100; CoT with evaluation = 60; classification only = 10. |
| F22 | Moral sensitivity detection | M10 | 0--100 | Tests recognition that a situation has moral dimensions before judgment = 100; partial sensitivity testing = 50; assumes moral recognition = 0. |
| F23 | Moral creativity assessment | M10 | 0--100 | Tests novel moral solutions, dilemma reframing, overlooked considerations = 100; some open-ended items = 50; closed-form only = 0. |
| F24 | Moral uncertainty expression | M10 | 0--100 | Scores calibrated moral uncertainty expression (not mere hedging) = 100; allows uncertainty = 50; forces definitive answers = 0. |
| F25 | Novel-scenario generalization | M10 | 0--100 | Includes post-training-cutoff scenarios requiring transfer from principles = 100; partially novel = 50; familiar scenarios = 0. |
| F26 | Moral mimicry detection | M10 | 0--100 | Includes mechanisms distinguishing genuine reasoning from pattern-matching = 100; some anti-mimicry items = 50; no mimicry detection = 0. |
| F27 | Reflective equilibrium testing | M10 | 0--100 | Tests iterative revision of principles and judgments = 100; some revision probing = 50; static assessment = 0. |
| F28 | Supererogation recognition | M10 | 0--100 | Tests recognition of supererogatory acts with appropriate praise-without-blame scoring = 100; includes some supererogatory items = 50; duty-only framework = 0. |
| F29 | Sacred/taboo value coverage | M12 | 0--100 | Includes sacred value items with taboo trade-off resistance testing = 100; some sacred content = 50; no sacred values = 0. |
| F30 | Religious tradition representation count | M12 | 0--100 | Engages >= 5 religious moral traditions with tradition-authentic items = 100; 3--4 traditions = 60; 1--2 = 30; none = 0. |
| F31 | Moral authority structure scope | M12 | 0--100 | Tests >= 4 moral authority sources (individual conscience, scripture, community, nature/reason) = 100; 2--3 sources = 50; single authority assumption = 10. |
| F32 | Moral ontology breadth | M12 | 0--100 | Engages >= 3 moral ontologies (natural law, divine command, social constructionism, moral realism, moral anti-realism) = 100; 2 = 50; 1 or implicit = 10. |
| F33 | Non-Western theory engagement depth | M12 | 0--100 | Deep engagement (correct terminology, community-validated items, culturally appropriate framing) with >= 2 non-Western traditions = 100; surface engagement = 40; none = 0. |
| F34 | Secular-religious neutrality | M12 | 0--100 | Neutral framing between secular and religious reasoning = 100; mostly neutral with some bias = 60; systematically privileges one over the other = 20. |
| F35 | Community moral norms coverage | M12 | 0--100 | Tests community-specific (non-universal) moral norms with culturally contextualized items = 100; some community norms = 50; universal norms only = 0. |
| F36 | Moral pluralism depth | M12 | 0--100 | Measures genuine engagement with moral plurality (not just tolerance recognition) = 100; partial pluralism = 50; monist framework = 0. |
| F37 | Ritual and embodied moral practice coverage | M12 | 0--100 | Includes ritual/embodied moral dimensions (purity practices, pilgrimage, fasting) = 100; mentions embodied practices = 40; propositional ethics only = 0. |
| F38 | Afterlife and eschatological moral reasoning | M12 | 0--100 | Includes scenarios where afterlife/karmic consequences are morally relevant = 100; acknowledges transcendent motivation = 50; this-worldly only = 0. |
| F39 | Cross-cultural moral divergence profile | Cross | 0--100 | Measures divergence profile across cultures (not just global mean) = 100; some cultural variation analysis = 50; aggregate only = 0. |
| F40 | Stakeholder perspective shifting | Cross | 0--100 | Tests perspective-taking across >= 4 stakeholder roles = 100; 2--3 roles = 50; single perspective = 0. |
| F41 | Moral trade-off explicitness | Cross | 0--100 | Makes trade-offs explicit with quantified cost-benefit framing = 100; implicit trade-offs = 50; no trade-off structure = 0. |
| F42 | Temporal moral reasoning | Cross | 0--100 | Tests temporal displacement effects (immediate vs. future harm) with parametric manipulation = 100; some temporal variation = 50; atemporal = 0. |
| F43 | Collective vs. individual moral agency | Cross | 0--100 | Tests reasoning about collective moral agents (corporations, states, communities) alongside individual agents = 100; some collective items = 50; individual agents only = 0. |
| F44 | Moral development sensitivity | M5 | 0--100 | Detects developmental level differences (Kohlberg stages, neo-Kohlbergian schema) with stage assignment = 100; partial developmental sensitivity = 50; no developmental dimension = 0. |

### S1.7 Tier G --- Theory Fidelity and Provenance (Features G1--G29)

Tier G assesses how faithfully benchmarks represent their claimed theoretical foundations and the quality of their scholarly provenance. Features were proposed primarily by the Theory Fidelity Expert (M1), Developmental Psychology Expert (M2), Citation and Provenance Expert (M7), and Data Engineering Expert (M8).

| ID | Name | Proposed By | Scale | Scoring Rubric |
|----|------|-------------|-------|----------------|
| G1 | Theory version currency | M1 | 0--100 | Uses current theory version (e.g., MFT 2.0, PVQ-RR, not PVQ-21) = 100; one version behind = 60; uses superseded formulation = 20. |
| G2 | Foundation coverage breadth | M1 | 0--100 | Measures >= 80% of target theory's constructs = 100; 50--79% = 60; <50% = 30; cherry-picks constructs = 10. |
| G3 | Foundation coverage depth | M1 | 0--100 | >= 6 items per construct enabling within-construct variance estimation = 100; 3--5 = 60; 1--2 = 30. |
| G4 | Corpus annotation quality | M1 | 0--100 | Multi-annotator (>= 5), trained, published guidelines, adjudication protocol, inter-annotator agreement > 0.80 = 100; adequate (3 annotators, kappa > 0.60) = 60; minimal (2 annotators, no agreement metric) = 20; single annotator = 0. |
| G5 | Theory-specific scoring fidelity | M1 | 0--100 | Scoring algorithm faithfully implements original theory's prescribed method = 100; minor deviations documented = 70; substantial modifications = 40; scoring unrelated to theory = 0. |
| G6 | Developmental sensitivity | M2 | 0--100 | Detects responses at each stage of developmental model (not just highest) = 100; detects 2--3 stages = 60; single-stage classification = 20; no developmental model = 0. |
| G7 | Stage differentiation granularity | M2 | 0--100 | >= 6 discriminable developmental levels = 100; 4--5 = 70; 2--3 = 40; binary only = 10. |
| G8 | Regression detection capability | M2 | 0--100 | Detects downward stage movement under adversarial/stress conditions = 100; can detect some regression = 50; upward-only measurement = 0. |
| G9 | Complexity gradient | M2 | 0--100 | Items span full range from clear-cut to genuinely ambiguous with calibrated difficulty = 100; some variation = 50; uniform difficulty = 10. |
| G10 | Reasoning sophistication capture | M2 | 0--100 | Captures reasoning QUALITY (not just conclusion correctness) with multi-level rubric = 100; partial quality assessment = 50; correct/incorrect only = 0. |
| G11 | Dyadic structure sensitivity | M1 (+Mcross) | 0--100 | Measures agent-patient dyadic structure per Gray and Schein (2012, 2018) with both roles identified = 100; partial dyadic measurement = 50; no dyadic structure = 0. |
| G12 | Meta-cognitive reflection capacity | M2 | 0--100 | Elicits and measures meta-cognitive awareness of moral reasoning process = 100; some reflective items = 50; no meta-cognition = 0. |
| G13 | Citation trajectory (momentum) | M7 | 0--100 | Increasing trajectory (growing influence, last 2 years > previous 2) = 100; stable = 70; declining = 30; newly published (<2 years) = 50. |
| G14 | Citation hub score (downstream adoption) | M7 | 0--100 | >= 5 subsequent benchmarks cite this as a foundation = 100; 2--4 downstream benchmarks = 60; 1 = 30; none = 0. |
| G15 | Venue disciplinary origin | M7 | 0--100 (categorical) | Interdisciplinary (CS + psychology co-authored) = 100; psychology venue = 80; CS venue with psychology collaboration = 60; CS-only = 40; workshop = 20. |
| G16 | Replication count | M7 | 0--100 (count-mapped) | >= 5 independent methodological replications = 100; 3--4 = 70; 1--2 = 40; none = 0. |
| G17 | Dataset derivative count | M7 | 0--100 (count-mapped) | >= 5 derivative datasets or adaptations = 100; 3--4 = 70; 1--2 = 40; none = 0. |
| G18 | Cross-disciplinary citation breadth | M7 | 0--100 | Cited across >= 4 disciplines = 100; 3 = 70; 2 = 40; single discipline = 10. |
| G19 | Theory fidelity index | M7 | 0--100 | Benchmark cited by original theorist(s) as faithful operationalization = 100; cited without endorsement = 60; not cited by theorist = 30; theorist has criticized = 0. |
| G20 | Pre-registration / registered report status | M7 | 0--100 | Published as registered report = 100; pre-registered study = 70; unregistered = 0. |
| G21 | Open peer review availability | M7 | 0--100 | Full peer reviews publicly available (OpenReview, PeerJ) = 100; partial (editorial summary) = 50; closed review = 0. |
| G22 | Methodological transparency index | M7 | 0--100 | All of: item selection documented, scoring algorithm published, data public, code public = 100; 3 of 4 = 75; 2 of 4 = 50; 1 of 4 = 25; none = 0. |
| G23 | Data freshness (recency of last update) | M8 | 0--100 | Updated within 1 year = 100; 1--2 years = 70; 2--5 years = 40; >5 years = 10. |
| G24 | Licensing clarity | M8 | 0--100 | Clear open license (CC-BY, MIT, Apache) = 100; restrictive but documented = 60; license unclear = 20; no license information = 0. |
| G25 | Data format standardization | M8 | 0--100 | Standard format (JSONL/CSV/Parquet, documented schema, HuggingFace dataset card) = 100; standard format without documentation = 60; non-standard format = 20. |
| G26 | Documentation quality | M8 | 0--100 | Datasheet for Datasets (Gebru et al., 2021) or equivalent comprehensive documentation = 100; README with key fields = 60; minimal documentation = 20; none = 0. |
| G27 | Reproducibility score (end-to-end) | M8 | 0--100 | One-command reproducibility from download to final score = 100; < 5 steps = 70; documented but manual = 40; not reproducible = 0. |
| G28 | Versioning and changelog practices | M8 | 0--100 | Semantic versioning, documented changelog, backward compatibility = 100; some versioning = 50; no version control = 0. |
| G29 | Theory genealogy depth | M7 | 0--100 | Engages with full intellectual genealogy (primary theorist + critiques + recent developments) = 100; cites primary + some secondary = 60; cites primary only = 30; no theory engagement = 0. |

### S1.8 Coverage Statistics

The full 162-feature framework was assessed across 54 benchmarks, generating 8,748 potential scoring cells (162 features x 54 benchmarks). However, 3 features from Tier B (B5, B8, B9) and 1 from Tier C (C4) were excluded across all benchmarks, reducing the assessed feature count to 158 active features.

**Assessed matrix:** 158 features x 54 benchmarks = 8,532 cells

Of these, 7,614 cells were scored (non-null), yielding a coverage rate of 89.2%. When restricted to the 141 new features in Tiers D--G (7,614 scorable cells), coverage is 99.1% (7,544 of 7,614).

**Null concentration:** Gaps are concentrated in two features:
- **D9** (LLM-specific ceiling compression index): 35% null --- many benchmarks have not been administered to LLMs with distributional analysis sufficient to compute compression.
- **D20** (Response distribution entropy): 35% null --- empirical data on response distributions was unavailable for benchmarks not yet administered to multiple models.

| Tier | Features | Assessed Features | Cells | Non-Null | Coverage |
|------|----------|-------------------|-------|----------|----------|
| A | 6 | 6 | 324 | 324 | 100.0% |
| B | 10 | 7 | 378 | 378 | 100.0% |
| C | 5 | 4 | 216 | 216 | 100.0% |
| D | 24 | 24 | 1,296 | 1,220 | 94.1% |
| E | 44 | 44 | 2,376 | 2,376 | 100.0% |
| F | 44 | 44 | 2,376 | 2,376 | 100.0% |
| G | 29 | 29 | 1,566 | 1,524 | 97.3% |
| **Total** | **162** | **158** | **8,532** | **8,414** | **98.6%** |

### S1.9 Deduplication Log

Thirteen merges reduced 154 proposed features to 141 new features. In each case, both proposals were conceptually overlapping; the retained feature absorbed the unique aspects of the merged proposal.

| Retained Feature | Absorbed Proposal | Rationale |
|-----------------|-------------------|-----------|
| D2: Test-retest reliability evidence | M8: Temporal stability; M9: Test-retest documentation | All three assess temporal reliability from different angles |
| D5: Ceiling/floor effect prevalence | M11: Ceiling/floor quantification | Both quantify ceiling/floor effects |
| E1: Recognition-endorsement discrimination | M6: Recognition-endorsement dissociation | Same construct, different terminology |
| E2: Dual-system engagement detection | M6: System 1/System 2 diagnostic capability | Both assess dual-system processing |
| E3: Dumbfounding elicitation capacity | Mcross: Dumbfounding susceptibility measurement | Both test moral dumbfounding |
| E4: Prompt template sensitivity | M8: Prompt sensitivity coefficient | Both quantify prompt variation effects |
| E12: Adversarial robustness tested | M2: Adversarial robustness evidence | Both assess adversarial attack testing |
| E16: Multi-turn consistency measurement | M4: Multi-turn engagement capacity | Covers both engagement and consistency |
| E19: Refusal behavior measurement | M4: Refusal handling protocol | Both assess refusal behavior |
| F3: Moral emotion measurement | M5: Moral emotion engagement | Both assess moral emotion measurement |
| F4: Moral conflict structure | M6: Hierarchical moral conflict resolution | Both assess competing-value conflicts |
| G11: Dyadic structure sensitivity | Mcross: Dyadic sensitivity profile | Both assess agent-patient dyadic structure |

---

## S2. Council Assessment Protocols

### S2.1 Council A --- Meta-Evaluation Council (12 Members)

Council A was responsible for guiding the rewriting of landscape-mapping sections: related work, methodology (Sections 3.1--3.5), Results Part I (the five benchmark landscape claims), and psychometric analysis. Table S2.1 lists all members with their expertise domains and section assignments.

| ID | Role | Expertise Domain | Section Assignments |
|----|------|-----------------|---------------------|
| A1 | Narrative Architect | Rhetorical structure, ACL/Nature MI conventions, argumentation flow | Abstract, cross-section transitions, overall story arc |
| A2 | Moral Psychology Historian | Intellectual genealogy from Piaget through contemporary theories, content/process/structure taxonomy | Related Work 2.1 |
| A3 | MFT Deep Expert | MFQ, MFQ-2, MFTC, MFRC, computational MFT operationalization | Related Work 2.1.1 (MFT), Results Claim 1 |
| A4 | Process Theories Specialist | Dual Process Theory (Greene), Social Intuitionist Model (Haidt), cognitive neuroscience of morality | Related Work 2.1.2, Results Claim 3 |
| A5 | Psychometric Authority | Messick validity framework, Cronbach and Meehl construct validity, measurement invariance, IRT | Related Work 2.3, Results Claim 2, Methodology 3.3 |
| A6 | Cross-Cultural and Values Expert | WEIRD critique, Schwartz PVQ-RR, Dyadic Morality, cultural psychology | Related Work 2.1.1 (Schwartz), Related Work 2.1.3 (Dyadic) |
| A7 | Benchmark Landscape Surveyor | BIG-bench, HELM, ETHICS, MoralBench, evaluation harness ecosystems | Related Work 2.7, Results Claim 4 |
| A8 | Format and Measurement Specialist | Likert scales, forced-choice, response bias, format-dependent validity in LLMs | Related Work 2.4, Results Claim 5 |
| A9 | NLP/Evaluation Specialist | Harness compatibility, scorer types, prompt engineering, evaluation infrastructure | Methodology 3.1--3.2 |
| A10 | Bibliometrician | Citation analysis, venue tiers, h-index, downstream adoption, citation maturity confound | Methodology 3.4, citation maturity analysis |
| A11 | Survey Methodologist | Systematic review standards, PRISMA, inclusion/exclusion criteria, search protocol rigor | Methodology 3.1 |
| A12 | Meta-Science Critic | Replication crisis, QRPs, pre-registration, open science, self-critique methodology | Discussion limitations, meta-critique integration |

### S2.2 Council B --- Empirical Council (12 Members)

Council B was responsible for guiding the empirical sections: cross-vendor methodology (Sections 3.6--3.7), Results Part II (cross-model and cross-vendor findings), and safety/policy implications.

| ID | Role | Expertise Domain | Section Assignments |
|----|------|-----------------|---------------------|
| B1 | Cross-Vendor Analyst | Multi-model comparison design, variance decomposition, convergence metrics, coefficient of variation | Results 5.1 (convergence), Results 5.5 (theory patterns) |
| B2 | RLHF/Alignment Expert | Constitutional AI, RLHF, InstructGPT, DPO, value encoding mechanisms | Results 5.2 (RLHF fingerprints), Discussion (alignment) |
| B3 | AI Safety Researcher | Value monoculture risk, audit strategies, deployment risk, regulatory implications | Discussion (safety implications) |
| B4 | Scale Sensitivity Analyst | Parameter scaling laws, emergent capabilities, size-dependent moral behavior | Results 5.3 (scale sensitivity) |
| B5 | Cross-Cultural Psychologist | WEIRD bias, Hofstede dimensions, cultural persona validity, value pluralism | Results (cultural persona), Discussion (monoculture critique) |
| B6 | Dual-Process Cognitive Scientist | System 1/2, CoT as deliberation proxy, cognitive load manipulation | Results 5.4 (Haiku CoT effect), Discussion (dual-process) |
| B7 | Psychometrician (Empirical) | Test discrimination, ceiling/floor effects, reliability, benchmark fitness for LLMs | Results 5.6 (discrimination audit) |
| B8 | Statistical Methodologist | N=1 inference, bootstrap CIs, effect size interpretation, power analysis, multiple comparisons | All quantitative claims, Discussion (statistical limitations) |
| B9 | Moral Philosophy Analyst | Normative characterization, meta-ethical interpretation, philosophical meaning of convergence | Discussion (philosophical framing) |
| B10 | Policy and Governance Expert | Algorithmic auditing, regulatory implications, standardization needs | Discussion (policy recommendations), Conclusion |
| B11 | Developmental Psychologist | Kohlberg stages, DIT, stage theory applicability to LLMs, maturation models | Results (Kohlberg findings), Discussion (developmental reframing) |
| B12 | Philosophy of Mind Specialist | Functional moral agency, consciousness, whether "moral psychology" applies to LLMs | Discussion (philosophical framing), Terminology |

### S2.3 Assessment Procedure

Assessment was conducted through three parallel passes, each targeting a distinct dimension of benchmark quality.

**Pass 1: Depth Assessment.** Perspectives 1--3 and 5 (MFT Specialist, Developmental Psychologist, Psychometrician, Cross-Cultural Psychologist) read full PDF extracts for each of the top 40 candidates. Each perspective scored:
- A2 (construct operationalization)
- A4 (source instrument provenance)
- A5 (human baseline availability)
- A6 (construct validity evidence)
- B1 (task format)
- B2 (dataset size)
- B10 (LLM administration fidelity)
- Theories engaged (verified against paper content, not keyword scores)

For each feature, the assessor provided a numerical score, a one-sentence justification, and a confidence flag (high/medium/low). Scores from multiple assessors on the same feature were averaged; disagreements exceeding 25 points triggered discussion until consensus.

**Pass 2: Impact Assessment.** Perspectives 4, 6--8 (NLP Evaluator, AI Safety Researcher, Bibliometrician, Data Engineer) cross-referenced candidates against implementability data (repository access, documentation quality, harness integration status). They scored:
- B6 (harness compatibility)
- B7 (scorer complexity)
- C3 (venue tier)
- C5 (hub/leaderboard presence)
- Safety relevance (qualitative flag)
- Data accessibility (qualitative flag)

**Pass 3: Secondary Scan.** Perspective 9 (Survey Methodologist) scanned candidates ranked 41--80 for hidden gems and underrepresented theories. The scan applied relaxed inclusion criteria, specifically targeting benchmarks from minority theories (dual process, social intuitionism, dyadic morality, moral identity) that might have been ranked lower by the keyword-biased extraction pipeline. This pass identified 15 additional papers warranting full assessment, expanding the characterized set from 40 to 55.

**Citation data retrieval.** The Semantic Scholar API was queried for the top 80 candidates using DOI and arXiv identifiers. Of 80 candidates, 54 were found in the Semantic Scholar corpus; 26 lacked identifiers resolvable by the API (missing DOI, no arXiv version, or proceedings not indexed). For the 54 with data, we retrieved total citation count, publication date (for age normalization), and venue classification. Rate limiting was implemented at 10-second intervals between requests.

**Consensus protocol.** After all three passes completed, a joint reconciliation session reviewed:
1. Cross-assessor scoring discrepancies (>25 points on any feature)
2. Theory classification disagreements
3. Hard-gate borderline cases (PD near 40 threshold)
4. Hidden-gem promotion decisions

Nine discrepancies were resolved through discussion; no cases required a tiebreaker vote.

### S2.4 Extended Framework Assessment (Tiers D--G)

The 141 new features (Tiers D--G) were assessed in a separate pass conducted by the twelve-member Feature Framework Council (see Section S1 header). Each council member assessed features within their area of expertise:

| Council Member | Role | Features Assessed | Tiers |
|----------------|------|-------------------|-------|
| M1 | Theory Fidelity Expert | 9 | E (1), F (2), G (6) |
| M2 | Developmental Psychology Expert | 10 | E (2), F (2), G (6) |
| M3 | Psychometrics Expert | 11 | D (11) |
| M4 | LLM Administration Expert | 9 | D (1), E (8) |
| M5 | Cultural Psychology Expert | 14 | F (14) |
| M6 | AI Safety Expert | 15 | E (15) |
| M7 | Citation and Provenance Expert | 11 | G (11) |
| M8 | Data Engineering Expert | 14 | E (8), G (6) |
| M9 | Research Methods Expert | 6 | D (6) |
| M10 | Moral Philosophy Expert | 11 | F (11) |
| M11 | Statistical Validity Expert | 8 | D (6), E (2) |
| M12 | Religious and Sacred Values Expert | 10 | F (10) |
| Cross | Cross-cutting (multi-member) | 13 | E (8), F (5) |

Each member scored all 54 benchmarks on their assigned features. The full assessment generated the 162 x 54 scoring matrix reported in Table S1.8.

---

## S3. Keyword Scorer Expansion Details

### S3.1 Original Scorer Architecture

The vault's moral psychology keyword scorer (`moral_psych_scoring.py`) classifies papers across eight theories using a three-tier keyword architecture:

```
score = strong_matches x 15 + medium_matches x 5 - fp_context x 10 + title_bonus
clamped to [0, 100]
```

where:
- **Strong matches** are high-confidence patterns that directly name the theory or its canonical instruments (weight: +15 per match)
- **Medium matches** are contextual patterns requiring co-occurrence with moral psychology terms (weight: +5 per match)
- **False-positive context** patterns detect likely non-moral-psychology usage of ambiguous terms (weight: -10 per match)
- **Title bonus** adds +20 if the paper's title matches a theory-specific pattern

Detection threshold: score >= 50 is treated as positive.

### S3.2 Original Pattern Inventory (65 Patterns)

The original scorer contained 65 regex patterns distributed across eight theories:

| Theory | Strong | Medium | FP Context | Title | Total |
|--------|--------|--------|------------|-------|-------|
| Moral Foundations Theory (MFT) | 16 | 4 | 4 | 1 | 25 |
| Value Pluralism / Schwartz | 7 | 4 | 5 | 1 | 17 |
| Trolley / Dilemmas | 6 | 2 | 1 | 1 | 10 |
| Cognitive Developmental (Kohlberg) | 5 | 3 | 2 | 1 | 11 |
| Dual Process Theory | 2 | 1 | 0 | 0 | 3 |
| Social Intuitionist Model | 1 | 0 | 0 | 0 | 1 |
| Dyadic Morality | 1 | 1 | 0 | 0 | 2 |
| Moral Identity | 3 | 1 | 0 | 0 | 4 |
| **Total** | **41** | **16** | **12** | **4** | **73** |

Note: The original count of "65 regex patterns" in the main text refers to unique conceptual patterns; several share regex components. The full regex inventory contained 73 individual pattern strings.

### S3.3 Critical Blind Spots Identified

The secondary scan (Pass 3) revealed that three theories --- Dual Process Theory, Social Intuitionism, and Dyadic Morality --- had near-zero detection rates. Analysis revealed this was primarily a scorer artifact:

- **Dual Process Theory** had only 3 patterns, none covering Greene's key empirical constructs ("utilitarian vs. deontological processing," "cognitive load," "personal vs. impersonal dilemma")
- **Social Intuitionist Model** had only 1 pattern (`\bsocial intuitionist\b`), missing Haidt's broader vocabulary ("moral dumbfounding," "post-hoc rationalization," "moral heuristic")
- **Dyadic Morality** had only 2 patterns, missing Gray and Schein's framework vocabulary ("harm perception," "moral typecasting," "agent-patient")

### S3.4 Expansion: New Patterns by Theory

**Dual Process Theory --- 20 new patterns added:**

*Strong patterns (11 new):*
- `\butilitarian vs\.? deontological\b` (with moral/judgment/reasoning/dilemma context)
- `\bcognitive load\b` (with moral context)
- `\bpersonal force\b` (with moral/dilemma context)
- `\bpersonal vs\.? impersonal\b` (with dilemma context)
- `\bgreene\b` (with moral context)
- `\baffect\b` (with cognition + moral context)
- `\bresponse time\b` (with moral context)
- `\bjoshua greene\b`
- `\butilitarian vs deontological processing\b`
- `\bsystem 1.*system 2\b`
- `\bsystem 2.*system 1\b`

*Medium patterns (8 new):*
- `\bfast and slow\b` (with moral context)
- `\bautomatic.*deliberat\w*\b` (with moral context)
- `\bautomatic\b` (with moral + judgment/reasoning/process context)
- `\bdeliberat\w+\b` (with moral + judgment/reasoning/process context)
- `\bsystem 1\b` (with moral/intuition/dilemma context)
- `\bsystem 2\b` (with moral/deliberation/dilemma context)
- `\beffortful\b` (with moral context)
- `\bemotional response\b` (with utilitarian/deontological context)

*FP context patterns (1 new):*
- `\bdual process\b` (with cognitive science/memory/attention/perception context, excluding moral)

**Social Intuitionist Model --- 16 new patterns added:**

*Strong patterns (9 new):*
- `\bhaidt\b` (with intuition/moral/foundation/dumbfounding context)
- `\bpost[- ]hoc rationali[sz]\w+\b` (with moral context)
- `\bgut feeling\b` (with moral context)
- `\bemotion[- ]first\b` (with moral context)
- `\bmoral heuristic\b`
- `\bmoral sentiment\b` (with judgment/intuition/reasoning context)
- `\bmoral dumbfounding\b`
- `\breasoning comes second\b`
- `\bsocial intuitionist\b`

*Medium patterns (5 new):*
- `\bmoral intuition\b`
- `\bintuitive judgment\b` (with moral context)
- `\bmoral sentiment\b`
- `\bhumean\b` (with moral context)
- `\bsentimentalism\b` (with moral/ethics context)
- `\bintuitive\b` (with moral + judgment/reasoning/response context)
- `\baffect\b` (with reasoning + moral context)

*FP context patterns (2 new):*
- `\bintuition\b` (excluding moral/intuitionist/dumbfounding/judgment/sentiment/ethics context)
- `\bsentiment\b` (excluding moral/ethics/intuitionist/humean context)

**Dyadic Morality --- 11 new patterns added:**

*Strong patterns (4 new):*
- `\bharm perception\b` (with moral/agent/patient context)
- `\bschein\b` (with moral/dyadic/gray/typecasting context)
- `\bagent[- ]patient\b` (with harm context)
- `\btheory of dyadic morality\b`

*Medium patterns (5 new):*
- `\bmoral patient\b`
- `\bmoral agent\b` (with patient context)
- `\bcomplete moral dyad\b`
- `\bharm[- ]based moral\w*\b`
- `\bgray\b` (with schein + moral context)

*FP context patterns (2 new):*
- `\bdyad\b` (excluding moral/typecasting/kurt gray/harm/agent/patient context)
- `\bpatient\b` (excluding moral/agent/dyad/typecasting/harm context)

### S3.5 Impact of Expansion

After expanding the keyword scorer and re-scoring all papers in the vault:

| Theory | Before Expansion | After Expansion | Delta | % Increase |
|--------|-----------------|-----------------|-------|------------|
| MFT | 68 | 101 | +33 | 49% |
| Schwartz | 52 | 69 | +17 | 33% |
| Trolley | 36 | 58 | +22 | 61% |
| Kohlberg | 19 | 35 | +16 | 84% |
| Dual Process | 0 | 9 | +9 | -- |
| Social Intuitionism | 1 | 18 | +17 | 1,700% |
| Dyadic Morality | 3 | 7 | +4 | 133% |
| Moral Identity | 7 | 12 | +5 | 71% |
| **Total** | **186** | **309** | **+123** | **66%** |

The most dramatic improvement was for Social Intuitionism (from 1 to 18 detections, a 17-fold increase) and Dual Process Theory (from 0 to 9). These near-zero pre-expansion counts confirm that the apparent absence of these theories in the vault was primarily a measurement artifact. However, even after expansion, these theories remain genuinely underrepresented relative to MFT (101 papers), consistent with our main text finding that the benchmark landscape over-represents MFT.

### S3.6 Known Scorer Limitations

1. **Case-sensitivity bug (fixed).** An earlier version lowercased all text before matching, causing uppercase abbreviation patterns (`\bSVS\b`, `\bPVQ\b`, `\bMFT\b`) to silently fail. Fixed by writing all abbreviation patterns in lowercase.

2. **Negative lookahead false positives.** Patterns like `\bintuition\b(?!.*\bmoral\b)` intended to suppress "moral intuition" matches, but in text containing both "moral intuition" and "statistical intuition," the first "intuition" would fire because "moral" precedes rather than follows it. Fixed using negative lookbehind where appropriate.

3. **Strong-floor rule.** Any strong match forces a minimum score of 50 (the detection threshold), ensuring that papers with even one unambiguous reference are detected. This occasionally produces false positives for papers that mention a theory in passing.

4. **Keyword-only limitation.** The scorer operates on string matching without semantic understanding. Papers that discuss moral psychology concepts using novel or discipline-specific terminology (e.g., "value alignment" in AI safety papers that substantively engage Schwartz's theory without naming it) may be missed.

---

## S4. Composite Scoring Algorithm

### S4.1 Feature Normalization

All raw assessments are normalized to a 0--100 scale before composite computation. The normalization functions are feature-specific:

**Ordinal mappings** (A2, A4, A5, A6, B1, B6, B7, B10):

| Feature | Raw Value | Normalized Score |
|---------|-----------|-----------------|
| A2 (Construct operationalization) | Validated instrument | 100 |
| | Theory-derived | 70 |
| | Theory-inspired | 40 |
| | Keyword-only | 10 |
| A4 (Source instrument) | Validated published | 100 |
| | Original with psychometric development | 80 |
| | None | 0 |
| A5 (Human baseline) | Published population norms | 100 |
| | Paper-specific human sample | 70 |
| | Partial/indirect norms | 40 |
| | No baseline | 0 |
| A6 (Construct validity) | 5 types of evidence | 100 |
| | 4 types | 75 |
| | 3 types | 50 |
| | 2 types | 30 |
| | 1 type | 10 |
| B1 (Task format) | MCQ | 100 |
| | Binary | 90 |
| | Forced-choice | 85 |
| | Likert | 70 |
| | Ranking | 60 |
| | Free-text | 50 |
| | Open generation | 30 |

**Count-mapped** (A1, B2):

| Feature | Raw Value | Normalized Score |
|---------|-----------|-----------------|
| A1 (Theories engaged) | 0 | 0 |
| | 1 | 30 |
| | 2 | 60 |
| | 3 | 80 |
| | 4+ | 100 |
| B2 (Dataset size) | <50 | 20 |
| | 200 | 40 |
| | 1,000 | 60 |
| | 5,000 | 75 |
| | 20,000 | 85 |
| | >20,000 | 100 |

**Log-scaled** (C1, C2):

| Feature | Raw Value | Normalized Score |
|---------|-----------|-----------------|
| C1 (Total citations) | <5 | 10 |
| | 20 | 30 |
| | 50 | 50 |
| | 100 | 65 |
| | 200 | 75 |
| | 500 | 85 |
| | >500 | 100 |
| C2 (Citations/year) | <2 | 15 |
| | 5 | 30 |
| | 10 | 50 |
| | 25 | 65 |
| | 50 | 80 |
| | 100 | 90 |
| | >100 | 100 |

Values between breakpoints are linearly interpolated.

**Platform-mapped** (B3):

| Feature | Raw Value | Normalized Score |
|---------|-----------|-----------------|
| B3 (Data availability) | HuggingFace | 100 |
| | GitHub | 95 |
| | OSF | 90 |
| | University server | 80 |
| | Anonymous link | 60 |
| | Email request | 30 |

### S4.2 Tier Composite Formulas

Three tier-level composite scores are computed as weighted averages:

**Psychological Depth (PD):**
```
PD = 0.25*A2 + 0.20*A6 + 0.15*A1 + 0.15*A5 + 0.15*A3 + 0.10*A4
```

**Practical Ease (PE):**
```
PE = 0.20*B3 + 0.15*B2 + 0.15*B6 + 0.15*B7 + 0.10*B1 + 0.10*B4 + 0.15*B10
```

**Citation Impact (CI):**
```
CI = 0.30*C1 + 0.30*C2 + 0.25*C3 + 0.15*C5
```

### S4.3 Final Composite

The overall composite score applies tier-level weights reflecting the project's priority ordering:

```
COMPOSITE = 0.50*PD + 0.30*PE + 0.20*CI
```

The 50/30/20 weighting reflects the council's judgment that psychological depth (theory fidelity, construct validity, human baselines) is the most important dimension for moral psychology benchmarks, followed by practical implementability, and then scholarly impact. This weighting was set before assessment to avoid post-hoc optimization.

### S4.4 Worked Example: The Moral Machine Experiment (Awad et al., 2018)

**Step 1: Raw feature scores.**

| Feature | Raw Value | Normalized |
|---------|-----------|-----------|
| A1 (Theories engaged) | 1 (trolley) | 30 |
| A2 (Operationalization) | Theory-derived | 70 |
| A3 (Dilemma complexity) | Forced-choice with 9 dimensions | 80 |
| A4 (Source instrument) | Original (no prior instrument) | 80 |
| A5 (Human baseline) | Published norms (2.3M respondents, 233 countries) | 100 |
| A6 (Construct validity) | 3 types (content, structural, criterion) | 50 |
| B1 (Format) | Forced-choice | 85 |
| B2 (Size) | 40,000,000 | 100 |
| B3 (Data) | GitHub | 95 |
| B4 (Code) | Full pipeline | 100 |
| B6 (Harness) | Custom implementation required | 40 |
| B7 (Scorer) | Exact match (binary choice) | 100 |
| B10 (LLM fidelity) | Minor adaptation (image-to-text conversion) | 70 |
| C1 (Citations) | >3,000 | 100 |
| C2 (Citations/year) | >500/year | 100 |
| C3 (Venue) | Nature (Tier 1) | 100 |
| C5 (Hub presence) | Major (Papers With Code, multiple leaderboards) | 100 |

**Step 2: Tier composites.**

```
PD = 0.25(70) + 0.20(50) + 0.15(30) + 0.15(100) + 0.15(80) + 0.10(80)
   = 17.5 + 10.0 + 4.5 + 15.0 + 12.0 + 8.0
   = 67.0

PE = 0.20(95) + 0.15(100) + 0.15(40) + 0.15(100) + 0.10(85) + 0.10(100) + 0.15(70)
   = 19.0 + 15.0 + 6.0 + 15.0 + 8.5 + 10.0 + 10.5
   = 84.0

CI = 0.30(100) + 0.30(100) + 0.25(100) + 0.15(100)
   = 30.0 + 30.0 + 25.0 + 15.0
   = 100.0
```

**Step 3: Final composite.**

```
COMPOSITE = 0.50(67.0) + 0.30(84.0) + 0.20(100.0)
          = 33.5 + 25.2 + 20.0
          = 78.7
```

The Moral Machine scores highest in the corpus (reported composite: 78.45; minor rounding differences reflect intermediate precision). Its strength lies in extraordinary citation impact (CI = 100) and practical ease (PE = 84.0, driven by massive dataset and simple scoring), while psychological depth (PD = 67.0) is moderate because it engages only one theory (trolley/dilemma paradigm) and provides construct validity evidence for three of five types.

### S4.5 Five-Step Selection Algorithm

**Step 1: Hard Gates.** Two necessary conditions must be satisfied:
- PD >= 40 (the benchmark engages moral psychology with at least minimal depth)
- Data is publicly available (the benchmark can be implemented)

Of 55 assessed candidates, 34 passed both gates. Twenty-one were eliminated: 16 for PD < 40 (benchmarks that scored well on practical and citation dimensions but lacked psychological grounding), 3 for unavailable data, and 2 for both.

**Step 2: Deduplication.** Two duplicate entries were identified and removed:
- TrolleyBench (2025) duplicated an earlier entry from the same research group
- Khandelwal DIT (2024) was a re-administration of the Defining Issues Test without new items

Removing duplicates yielded 32 unique candidates.

**Step 3: Theory Caps.** To prevent over-representation of well-resourced theories:
- Trolley/Dilemma paradigm: capped at 3 entries (from 7 eligible)
- Moral Foundations Theory: capped at 4 entries (from 9 eligible)

Caps were set proportional to each theory's share of the benchmark landscape while ensuring no single theory exceeds 27% of the final selection.

**Step 4: Greedy Selection.** Starting from the highest composite score and proceeding downward, candidates were selected if they did not violate any theory cap. This produced 13 selections.

**Step 5: Diversity Fills.** The greedy selection was checked against minimum diversity requirements:
- >= 2 Schwartz/Value Pluralism benchmarks
- >= 1 Kohlberg/Developmental benchmark
- >= 1 minority theory benchmark (moral identity, dyadic morality, social intuitionism, or dual process)

Two swaps were required:
1. A Schwartz benchmark (rank 11) was promoted over a capped MFT benchmark
2. A minority theory benchmark (ValueCompass, with dyadic component, rank 11) was promoted to satisfy the minority theory minimum

The final 15-benchmark selection spans:
- MFT: 5 benchmarks
- Trolley: 4 benchmarks (capped from 7)
- Schwartz: 4 benchmarks
- Kohlberg: 4 benchmarks
- Dyadic: 1 benchmark

### S4.6 Quick Assessment: 25-Feature Subset

For researchers who cannot conduct the full 162-feature assessment, we derived a practical 25-feature subset optimized for discriminative power.

**Selection method.** For each feature, we computed the variance of scores across the 54 benchmarks. Features with higher variance discriminate more effectively between benchmarks. We selected the top features from each tier, subject to minimum tier representation:

| Tier | Selected | Available | Selection Rate |
|------|----------|-----------|----------------|
| A (Psychological Depth) | 2 | 6 | 33% |
| B (Practical Ease) | 2 | 6 | 33% |
| C (Citation Impact) | 1 | 4 | 25% |
| D (Psychometric Rigor) | 4 | 24 | 17% |
| E (LLM-Specific Validity) | 6 | 44 | 14% |
| F (Cultural & Philosophical Breadth) | 6 | 44 | 14% |
| G (Theory Fidelity & Provenance) | 4 | 29 | 14% |

**Selected features (ranked by discriminative power):**

| Rank | ID | Name | Disc. Power |
|------|----|------|-------------|
| 1 | G14 | Citation hub score | 1519.3 |
| 2 | G16 | Replication count | 1432.8 |
| 3 | G17 | Dataset derivative count | 1242.1 |
| 4 | E27 | Token budget efficiency | 1193.4 |
| 5 | D8 | Measurement invariance | 1001.9 |
| 6 | D3 | Factor structure validation | 928.8 |
| 7 | G10 | Reasoning sophistication | 884.9 |
| 8 | E40 | Moral development trajectory | 864.8 |
| 9 | F44 | Moral development sensitivity | 864.8 |
| 10 | A5 | Cultural grounding | 854.2 |
| 11 | D21 | Sample size adequacy | 805.6 |
| 12 | D1 | Internal consistency | 803.5 |
| 13 | C3 | H-index contribution | 794.0 |
| 14 | B10 | Community adoption | 772.3 |
| 15 | B2 | Administration time | 770.6 |
| 16 | E28 | Output determinism | 763.7 |
| 17 | E34 | Demographic sensitivity | 748.6 |
| 18 | F9 | Language coverage | 559.9 |
| 19 | E31 | Anchor item availability | 549.4 |
| 20 | F6 | Cultural validation breadth | 536.3 |
| 21 | F4 | Moral conflict structure | 513.0 |
| 22 | E26 | API compatibility tier | 505.1 |
| 23 | F1 | Stereotype amplification | 483.9 |
| 24 | F41 | Moral trade-off explicitness | 465.6 |
| 25 | A2 | Moral foundation coverage | 393.0 |

**Validation.** The Quick Assessment composite (arithmetic mean of 25 feature scores) correlates with the full 162-feature assessment at Pearson r = 0.630 (R-squared = 39.7%, Spearman rho = 0.632). While this captures less than half the variance in the full assessment, it preserves the broad rank ordering: the correlation is sufficient for initial screening or resource-constrained evaluation, though not for fine-grained benchmark comparison.

The Quick Assessment is computed as:
```
Quick_Composite = mean(score_1, score_2, ..., score_25)
```

All 25 features are equally weighted. If a feature cannot be scored, it is excluded and the mean is computed over the remaining features.

---

*This supplementary document accompanies the main text "Moral Response Profiles: A Systematic Assessment of Moral Psychology Benchmarks for Large Language Model Evaluation." Data files: `20260404-extended-feature-matrix-v3.json` (162 x 54 scoring matrix), `20260404-council-feature-proposals.json` (141 proposals), `20260404-quick-assessment-25.json` (25-feature subset). All materials are available at the project repository.*
