---
stem: "2025-Li-Untangling Input Language from Reasoning Language A Diagnostic"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, normative-ethics, design-space]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 1895
dataset_construction: "scraped"
languages: ["en", "zh"]
models_tested: ["Claude-Sonnet-4", "DeepSeek-R1-0528", "Qwen3-235B", "Ernie-4.5-21B", "GLM-4.6", "Grok-4", "Magistral-Medium-2506", "Nemotron-Nano-9B", "GPT-OSS-20B", "Gemini-2.5-Flash", "o4-mini", "Kimi-K2", "Llama-4-Maverick"]
headline_numbers:
  - "Reasoning-language changes produce ~2x larger YTA shifts than input-language changes: 7.16pp vs 3.46pp on AITA, 6.88pp vs 3.34pp on CMoral (p.6)"
  - "12/13 models fall below human baseline on AITA (53.6%), 13/13 on CMoral (50%), Cohen's d > 1.6 (p.5)"
  - "44% of models (4/9) exhibit hidden context-dependency invisible to single-dataset evaluation (p.6)"
  - "Moral priority rankings remain stable across conditions (mean Spearman rho=0.88, all >0.82) despite verdict instability (p.7)"
  - "AITA: 847 dilemmas; CMoral: 1,048 dilemmas (p.4)"
---
## 1. Gist
This paper introduces the "untangling framework," a 2×2 factorial design that independently manipulates input language (what language the moral dilemma is presented in) and reasoning language (what language the model reasons in) to diagnose the source of cross-lingual inconsistencies in LLM moral judgment. Standard benchmarking only tests matched conditions (English story + English reasoning), which conflates two distinct mechanisms. By adding mismatched conditions (English story + Chinese reasoning; Chinese story + English reasoning), the framework can attribute behavioral shifts to perception vs. deliberation. Applied to English-Chinese moral judgment across 13 LLMs using two datasets (847 Reddit r/AITA dilemmas and 1,048 Chinese moral scenarios from CMoralEval), it demonstrates that reasoning language drives approximately twice as much variance as input language, and reveals hidden alignment vulnerabilities in 44% of models that standard evaluation misses. This paper is directly relevant to values-alignment benchmarking because it provides both a methodology and a deployment taxonomy for characterizing cross-lingual moral alignment failure modes.

## 2. Benchmark/eval design features
The framework operationalizes a 2×2 factorial design with 4 conditions: EN/EN, EN/CN, CN/EN, CN/CN (input language / reasoning language). Key constructs measured:
- **Flip rate**: proportion of individual verdicts that change across language conditions
- **Sensitivity ratio**: thinking-triggered flips / story-triggered flips (per model)
- **Pattern consistency**: whether sensitivity ratio category stays stable across datasets
- **Moral fingerprint**: logistic regression coefficients over 7 Moral Foundations Theory dimensions (Care/Harm, Equality, Proportionality, Loyalty, Authority-Family, Authority-Society, Purity), capturing what moral priorities shift

The stability taxonomy (2×2: flip rate × pattern consistency) yields four model types:
- Coherent (low flip, consistent pattern)
- Context-Sensitive (low flip, pattern changes across datasets)
- Unstable (high flip, consistent pattern)
- Volatile (high flip, pattern changes)

A key methodological innovation is the Split-Authority refinement: the standard MFQ Authority dimension is split into Family (filial piety) and Society (institutional loyalty) sub-dimensions, motivated by domain confounds between datasets (AITA = family conflicts; CMoral = institutional conflicts).

## 3. Task format & example item
Binary forced-choice. Each moral dilemma is presented as a first-person "Am I the Asshole?" narrative with a binary verdict (YTA = "You're the Asshole" / NTA = "Not the Asshole"). Example:

> "Wealthy parents refuse to provide financial support for their son's pregnant girlfriend, a recovering addict he has dated for only six months, unless she first submits to a paternity test. When an LLM evaluates this scenario in English, it condemns the parents' ultimatum. Yet, when the same model evaluates the standard Chinese translation of the exact same scenario, it supports their position." (p.1)

The framework reveals: English reasoning activates Equality framing (condemning the unfair power dynamic), Chinese reasoning activates Loyalty framing (prioritizing lineage protection).

## 4. Scoring / grading methodology
Binary verdict extraction via JSON output format; invalid responses excluded. Human baseline: 53.6% YTA for AITA (from Reddit community votes), 50% YTA for CMoral (from original annotations). Effect sizes computed as Cohen's d comparing model YTA rates to human baselines. Flip rates and sensitivity ratios are the primary diagnostic metrics; bootstrap 95% CIs reported. Moral fingerprints use logistic regression with MFQ dimension scores (annotated by 5-LLM ensemble, median-aggregated) as predictors.

## 5. Dataset construction & provenance
- **AITA**: 847 dilemmas scraped from Reddit r/AmItheAsshole via API, anonymized. English-origin, individual-autonomy framing. Human baseline from community votes (53.6% YTA).
- **CMoral**: 1,048 dilemmas substantially adapted from CMoralEval (Yu et al., 2024). Original multiple-choice format reformatted to first-person binary verdict. Heavily filtered for moral conflict, complexity, and authenticity. Human baseline: 50% YTA.
- Cross-lingual translation: AITA (EN→CN) via DeepSeek-R1; CMoral (CN→EN) via Qwen3-235B, temperature=0. Translation quality validated via mBERT embedding similarity (>0.7), MFQ correlation (>0.8), and human spot-checks by two native Chinese/English bilinguals.
- MFQ annotation: Each story annotated on 6+1 dimensions using ±2 scale by 5-LLM ensemble (Qwen3-235B, DeepSeek-R1, Claude-Sonnet-4, Gemini-2.5-Flash, o4-mini), median-aggregated.

## 6. Validity evidence
- Inter-annotator reliability for MFQ annotation: 90.9% within-1-point agreement, mean correlation with median ρ=0.75, Care/Harm dimension α=0.72 (p.5)
- Human baselines validated but acknowledged as non-representative populations (Reddit commenters, original CMoralEval annotators)
- Split-Authority refinement validated empirically via improvement in logistic regression fit
- Mixed-effects logistic regression confirms directional consistency across models (p<0.001 for thinking-language effect)
- Per-model heterogeneity statistically confirmed: Cochran's Q = 177.0 (AITA), 137.3 (CMoral), both p<0.001 (p.7)
- Bootstrap 95% CIs for flip rates: mean width 3.6pp (p.7)

## 7. Saturation / discrimination
Strong discrimination: models range from 2pp to 39pp below human baselines on AITA; thinking-language sensitivity ranges from <3pp (Claude) to >20pp (Ernie). The framework successfully separates models into 4 taxonomy categories, with flip rates spanning 16.2% to 36.5%. No saturation at ceiling observed; models with low flip rates (Claude, Grok, GLM) cluster in Context-Sensitive quadrant rather than being uniformly correct. Only Ernie exceeds human baseline on AITA, providing an interesting outlier for analysis.

## 8. Multiturn / agentic aspects
n/a. All evaluations are single-turn: each dilemma is presented once with a system prompt enforcing the reasoning language. No tool use or interaction protocol. The paper does not test multi-turn consistency.

## 9. Key numbers
- AITA dataset: 847 dilemmas, human baseline 53.6% YTA (p.4)
- CMoral dataset: 1,048 dilemmas, human baseline 50% YTA (p.4)
- Valid verdicts per condition: 762–847 (AITA), 994–1,048 (CMoral) (p.5)
- Reasoning-language effect: 7.16pp (AITA), 6.88pp (CMoral) (p.6)
- Input-language effect: 3.46pp (AITA), 3.34pp (CMoral) (p.6)
- Ratio: ~2× (AITA: 2.07×, CMoral: 2.06×) (p.6)
- 12/13 models below human baseline on AITA; 13/13 on CMoral (p.5)
- Mean model YTA rate: 39.6% (AITA), 29.7% (CMoral) vs. human baselines of 53.6% and 50% (p.5)
- Cohen's d for leniency bias: 1.64 (AITA), 2.06 (CMoral) (p.5)
- 4/9 models (44%) exhibit hidden context-dependency (p.6)
- 50% (AITA), 41% (CMoral) of flipped scenarios are doubly-vulnerable (p.7)
- Mean Spearman ρ=0.88 for moral priority ranking stability across conditions (p.7)
- MFQ cross-validation AUC: 0.782 (CN), 0.768 (EN) (p.7)

## 10. Pitfalls & limitations
- Study validated only for English↔Chinese; may not generalize to other language pairs (p.9)
- "Reasoning language" operationalized via output instruction tokens, not internal computation (p.9)
- Both datasets focus on interpersonal conflicts; generalization to professional ethics, policy, or life-and-death dilemmas untested (p.9)
- AITA (Reddit) and CMoral (curated) differ in source domain beyond cultural origin, creating potential confounds (p.9)
- Translation artifacts may confound story-language effects in CMoral (p.9)
- Taxonomy thresholds are data-driven and illustrative, not prescriptive; borderline cases may shift categories (p.10)
- Multiple comparisons across models, datasets, and conditions without formal correction (p.10)
- CoT length confound: Chinese reasoning is shorter, and shorter rationales correlate with leniency (p.9)
- Human baselines represent specific populations, not representative samples (p.10)
- MFQ annotation circularity: using LLMs to annotate stories that LLMs then judge (p.10)
- Only 9 models have complete cross-lingual data for decomposition analysis; small sample for taxonomy claims

## 11. Novel ideas worth stealing
- **2×2 factorial language manipulation**: The core design move—independently varying input language and reasoning language—is directly applicable to any cross-lingual benchmark for values alignment. It converts a confounded between-condition comparison into a clean 2×2 decomposition.
- **Reasoning language as the dominant factor**: The empirical finding that reasoning language (~2×) dominates input language has direct implications for benchmark design: future cross-lingual benchmarks should enforce reasoning language separately from input language.
- **Stability taxonomy for deployment guidance**: The 4-quadrant taxonomy (Coherent/Context-Sensitive/Unstable/Volatile) is a clean design pattern for characterizing model behavioral profiles across evaluation conditions, reusable beyond language manipulations.
- **Moral fingerprinting via logistic regression**: Fitting per-condition regression coefficients over MFQ dimensions to produce "moral fingerprints" enables interpretable diagnosis of what normative priorities shift (vs. just whether verdicts change). The calibration drift vs. value drift distinction is especially useful.
- **Split-Authority refinement**: Detecting domain confounds in existing moral foundations frameworks (family vs. institutional authority) and correcting for them is a replicable methodology for refining measurement instruments.
- **Doubly-vulnerable scenario detection**: Identifying scenarios that flip under either manipulation alone reveals which items are fragile across both channels—a useful quality filter or difficulty marker.
- **Near-universal leniency as a benchmark signal**: The finding that 12-13/13 models are more lenient than humans provides a model-agnostic baseline calibration check for any moral judgment benchmark.

## 12. Notable quotes
- "Current safety evaluations assume that if a model handles a moral scenario correctly in English, it will handle the translation correctly too. This assumption is dangerous." (p.1)
- "Reasoning-language changes produce substantially larger shifts than story-language changes: 7.16pp vs. 3.46pp on AITA (2.07×), and 6.88pp vs. 3.34pp on CMoral (2.06×). This localizes instability primarily to output generation rather than input encoding." (p.6)
- "Models change how harshly they judge (intercept shifts), not what they prioritize (coefficient rankings). This distinction matters: calibration drift may be addressable through recalibration, whereas value drift would require fundamental retraining." (p.7)
- "A model passing English benchmarks may be unsafe for most users; current alignment may be 'skin deep.'" (p.8)

## 13. UNKNOWN / not in extract
- Full list of all 1,895 dilemmas and their annotations (code repository, anonymous at time of extraction)
- Exact per-model per-condition YTA rates (referred to in figures)
- Whether the Split-Authority refinement generalizes beyond the EN-CN comparison
- Whether leniency bias persists after controlling for CoT length
- Whether results replicate with human (rather than LLM-based) MFQ annotation
- Licensing terms for the released datasets
