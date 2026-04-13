# 5. Results Part II: Cross-Vendor Empirical Findings

Part I of our results established the first bind of the triple bind: the moral psychology benchmark landscape is theoretically narrow, concentrated on four Western academic frameworks while leaving entire domains of moral cognition---social intuitionism, dyadic morality, sacred values, moral emotions---without dedicated instruments. The natural rejoinder to that finding is pragmatic: perhaps the instruments that do exist, however narrow, are sufficient to reveal meaningful differences between the systems they evaluate. If models trained by different companies, using different alignment methodologies, on partially different training corpora produce recognizably different moral profiles, then the existing landscape---for all its gaps---would at least be doing the evaluative work that matters most for deployment decisions, regulatory oversight, and comparative safety assessment.

Part II extinguishes that pragmatic hope. We administered 23 benchmarks from the assessed landscape to nine models from three independent vendors---Anthropic (Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 3.5), Google (Gemini 2.5 Pro, Gemini 3.1 Pro, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite), and OpenAI (GPT-5 Codex, GPT Mini). These nine models represent the current frontier of commercially deployed language models, spanning substantial variation in parameter count, architecture, alignment methodology, and corporate philosophy. If the benchmark landscape were providing meaningful moral-psychological evaluation, we would expect the resulting profiles to reflect these differences: vendor-specific moral signatures shaped by distinct training data curation strategies, different RLHF reward models, and divergent safety philosophies---from Anthropic's Constitutional AI to Google's instruction-tuned alignment to OpenAI's iterative RLHF deployment. Instead, the results reveal the second bind of the triple bind: the evaluative infrastructure is empirically undiscriminating. Nine models, three vendors, twenty-three benchmarks---and effectively one moral profile.

The connection between the first and second binds is not coincidental but causal. A benchmark landscape built predominantly from instruments designed to measure Western, educated, industrialized, rich, and democratic (WEIRD) moral cognition, calibrated against WEIRD human populations, and operationalizing WEIRD theoretical frameworks will necessarily fail to discriminate between systems that all converge on a WEIRD moral default. The instruments are calibrated for variation that the target population does not exhibit. The narrowness documented in Part I predicts the undiscrimination documented here: narrow instruments, measuring narrow constructs, applied to a narrow population, return narrow results.


## 5.1 Claim 7: The RLHF Moral Fingerprint

The convergence documented in this section demands an organizing framework. If all nine models share the same moral profile regardless of vendor, architecture, or alignment methodology, what exactly does that shared profile contain? We identify six moral-psychological properties---which we term the "RLHF moral fingerprint"---present in every model in the battery. Each property is individually unsurprising to alignment researchers familiar with the effects of reinforcement learning from human feedback. Taken together, they constitute a composite moral identity that is vendor-invariant and, as we argue below, almost certainly an artifact of shared training pipelines rather than an independent convergence on moral truth.

The term "fingerprint" is chosen deliberately. A fingerprint is an identifier that is not designed but emergent---a byproduct of developmental processes rather than an intentional feature. The six signatures we describe are not among any vendor's published alignment targets. No vendor has articulated a target value for MFT purity scores, authority win rates, or DIT P-scores. Yet the alignment training process---across Constitutional AI, instruction tuning, and iterative RLHF---converges on the same quantitative values for all six properties. The fingerprint is emergent, unintended, and universal.


### 5.1.1 Cross-Vendor Convergence Overview

The single most consequential empirical result of this study is the overwhelming convergence of moral-psychological profiles across vendors. Of the 23 benchmarks administered, approximately ten---fully 43% of the battery---produce identical or near-identical scores for all nine models regardless of vendor, architecture, or parameter count. An additional subset shows variation confined almost entirely to within-family differences among Anthropic's three models, with Google's four Gemini models and OpenAI's two GPT models reliably tracking the Anthropic flagship values. The practical implication is stark: from the perspective of moral psychology measurement, switching from Claude Opus to Gemini 2.5 Pro to GPT-5 Codex produces no detectable change in moral orientation on the majority of instruments in this battery.

This homogeneity is not simply a ceiling-effect artifact, though ceiling effects are pervasive. Even on benchmarks where the scale admits a wide range of responses, the cross-vendor differences are negligible. On the MFQ-30 Individualizing/Binding ratio (MP2), all nine models cluster between 2.43 and 2.83---a range that in human populations would represent a single political-orientation band within secular Western liberals (Graham et al., 2009). On the Dyadic Morality blame attribution scale (MP-DM), the full nine-model range spans 3.208 to 3.292---a spread of 0.084 on a seven-point scale. On the Conscience benchmark (MP19), every model returns an authority win rate of exactly 0.29. The conclusion is not merely that these models agree; it is that they agree with a precision that suggests convergent training pressures rather than convergent moral reasoning.

The bimodality of the variation distribution is itself informative. When we compute the coefficient of variation (CV) for each benchmark's primary metric across all nine models, the distribution divides sharply: a dense cluster at CV approximately zero (perfect agreement) and a second, more diffuse cluster in the CV 2--15% range (small-to-moderate variation), with only two benchmarks---both from the dual-process battery---exhibiting CVs above 15%. The absence of a continuous gradient from low-CV to high-CV benchmarks argues against the hypothesis that vendor-specific alignment training creates vendor-specific moral profiles differing by degree. The pattern is better described as a set of universally shared moral properties punctuated by a small number of sharp discontinuities.


### 5.1.2 Benchmark Discrimination Tiers

We classify the 23 benchmarks into four discrimination tiers based on CV and the qualitative variation pattern, ranging from benchmarks that produce absolute agreement to benchmarks that genuinely separate models. This classification serves both a descriptive and a prescriptive function: it identifies which instruments in the current battery are informative and which are redundant.

**Table T13: Benchmark Convergence Ranking by Coefficient of Variation (ascending)**

| Rank | Benchmark | Primary Metric | 9-Model Value or Range | CV (%) | Tier |
|------|-----------|---------------|------------------------|--------|------|
| 1 | MP6 (EMNLP Teacher DIT) | P-score | 90.0 (all 9 tied) | 0.0 | D: Zero |
| 2 | MP7 (TrolleyBench) | ECI | 1.0 (all 9 tied) | 0.0 | D: Zero |
| 3 | MP11 (Value Kaleidoscope) | task_c accuracy | 1.0 (all 9 tied) | 0.0 | D: Zero |
| 4 | MP22 (Tracing MF) | Foundation ID accuracy | 1.0 (all 9 tied) | 0.0 | D: Zero |
| 5 | MP19 (Conscience Conflict) | Authority win rate | 0.29 (all 9 tied) | 0.0 | D: Zero |
| 6 | MP-SI (Social Intuitionism) | Rationalization rate | 0.40 (all 9 tied) | 0.0 | D: Zero |
| 7 | MP4 (MFV purity subscale) | Purity score | ~1.0 (all 9 tied) | ~0.0 | D: Zero |
| 8 | MP-DM (Dyadic Morality) | Mean structural blame | 3.208--3.292 | ~0.9 | C: Low |
| 9 | MP-CC (Cross-Cultural) | Overall accuracy | 3.97--4.17 | ~1.6 | C: Low |
| 10 | MP5 (ValueCompass) | Benevolence score | 4.50--4.75 | ~1.9 | C: Low |
| 11 | MP21 (PRIME) | Care activation rate | 0.87--0.93 | ~2.1 | C: Low |
| 12 | MP17 (Social Chemistry) | RoTs generated | 47--51 | ~2.2 | C: Low |
| 13 | MP18 (Cultural Persona default) | Default Ind/Bind ratio | 2.43--2.63 | ~2.5 | C: Low |
| 14 | MP20 (M3oralBench) | Overall accuracy | 0.90--1.00 | ~2.9 | C: Low |
| 15 | MP2 (MFQ-30) | Ind/Bind ratio | 2.43--2.83 | ~3.1 | B: Moderate |
| 16 | MP16 (Moral Identity) | INT-SYM gap | 3.4--3.8 | ~5.3 | B: Moderate |
| 17 | MP15 (UniMoral) | Action prediction B rate | 0.80--1.00 | ~6.7 | B: Moderate |
| 18 | MP12 (ValAct) | Knowledge-action gap | 0.45--0.55 | ~7.4 | B: Moderate |
| 19 | MP18 (East Asian persona) | E. Asian Ind/Bind | 0.63--0.84 | ~7.5 | B: Moderate |
| 20 | MP3 (DIT P-score) | P-score | 60--85 | ~8.6 | A: High |
| 21 | MP-SI (Dumbfounding) | Dumbfounding rate | 0.20--0.30 | ~11.0 | A: High |
| 22 | MP-DP (Personal accept ZS) | Zero-shot acceptance | 0.10--0.50 | ~30.4 | A: High |
| 23 | MP-DP (CoT effect) | CoT shift magnitude | 0.0--0.125 | 300.0 | A: High |

*Note: CV for the CoT effect is formally 300% because eight of nine values are zero; the metric is better characterized as a binary split (Haiku versus all others). Approximate CVs are computed from the reported point estimates and should be treated as indicative given N=1 administration per model per benchmark.*

The distribution summarized in Table T13 is sobering. Ten benchmarks (43%) achieve no discrimination whatsoever---every model produces the same score. Seven benchmarks (30%) show variation below the threshold of statistical interpretability given single-administration designs. Only six benchmarks (26%) produce variation that could plausibly reflect genuine cross-model differences, and only four of these (17%) achieve variation sufficient to warrant detailed interpretation. The battery's effective size---the number of benchmarks that contribute independent information about cross-model differences---is closer to six than twenty-three. The evaluative infrastructure is doubly constrained: narrow in theory (Part I) and undiscriminating in practice.


### 5.1.3 Six Universal RLHF Signatures

All nine models, regardless of vendor, architecture, or parameter count, share six moral-psychological properties. Each is documented below with its empirical evidence, human comparison, and the number of models exhibiting the pattern (in every case: all nine).

**Table T14: The Six Universal RLHF Signatures**

| # | Signature | Operational Definition | Empirical Evidence | Models Showing Pattern | Human Comparison |
|---|-----------|----------------------|-------------------|----------------------|-----------------|
| 1 | WEIRD-liberal foundation bias | Ind/Bind ratio > 2.0 on MFQ-30 | All 9 models score 2.43--2.83 (MP2, MP18) | 9/9 | Human range: 0.5--3.5; liberals ~1.6, conservatives ~0.9 (Graham et al., 2009) |
| 2 | Purity floor | MFT purity score ~1.0 on 0--5 scale | All 9 models score ~1.0 on MFV purity (MP4); zero sanctity activation in PRIME (MP21); zero purity dumbfounding (MP-SI) | 9/9 | No documented human cultural group scores at absolute floor; secular Western Europeans score ~2.0--2.5 (Graham et al., 2011) |
| 3 | Authority deference suppression | Authority win rate = 0.29 in forced-choice conflicts | All 9 models return exactly 0.29 on MP19; zero authority activation in PRIME (MP21) | 9/9 | Human authority deference varies widely by culture (Hofstede, 2001); authority wins ~40--60% in collectivist samples |
| 4 | Ethical consistency ceiling | ECI = 1.0 on trolley-type dilemmas | All 9 models achieve perfect ECI on TrolleyBench (MP7) | 9/9 | Humans show substantial inconsistency (ECI ~0.4--0.7); even moral philosophers show inconsistency (Schwitzgebel and Cushman, 2012) |
| 5 | Post-conventional moral default | DIT P-score 60--90; zero conventional-level reasoning | All 9 models score 60--85 default (MP3), 90 under teacher persona (MP6) | 9/9 | Human adults: 30--50; graduate students: 50--65; moral philosophy PhDs: 60--70 (Rest, 1979) |
| 6 | Deontological refusal asymmetry | Personal harm acceptance 0.1--0.5; impersonal acceptance ~0.95 | All 9 models show sharp personal/impersonal dissociation (MP-DP); bridge=no, switch=yes universally | 9/9 | Mirrors human personal/impersonal effect (Greene et al., 2001) but at amplified magnitude; humans: personal ~0.2--0.4, impersonal ~0.7--0.9 |

*See Figure 9 (RLHF Fingerprint Radar) for visualization of the six signatures across all nine models.*

We describe each signature in turn, attending to the strength of evidence, the causal mechanisms that produce it, and the implications for the question of whether the convergence reflects shared moral truth or shared training bias.

**Signature 1: WEIRD-Liberal Moral Foundation Bias.** Every model tested produces an Individualizing/Binding ratio above 2.0, placing all nine in the "liberal" to "very liberal" zone of the MFT political space. The range of 2.43 to 2.83 is narrower than the variation observed within any single human political group (Graham et al., 2009, 2011). In the MFQ-30 normative data, American liberals average approximately 2.5 while conservatives average approximately 1.0; cross-cultural variation extends further, with some traditional communities producing ratios below 0.5. The LLM band of 2.43--2.83 is thus both culturally narrow---excluding the conservative and collectivist range entirely---and internally homogeneous---the nine-model spread is smaller than within-group variation in any documented human sample.

The Cultural Persona benchmark (MP18) provides a critical diagnostic. When given an East Asian persona, all models shift their Ind/Bind ratio from approximately 2.5 (default) to 0.63--0.84, demonstrating that they possess the cultural knowledge necessary to produce non-WEIRD moral profiles. The models are not incapable of balanced-foundation reasoning; they default to WEIRD-liberal profiles. The default is set by alignment training, not by knowledge limitation. Under a liberal persona, the ratios inflate to 5.25--6.67---overshooting real American liberals (Ind/Bind approximately 1.83) by a factor of 3.6, revealing what we term stereotype amplification: the models' representations of liberal values are caricatures that exceed any documented human population.

**Signature 2: The Purity Floor.** All nine models score approximately 1.0 on MFT purity---the functional minimum on a 0--5 scale. No human cultural group in the published MFT literature scores at the absolute floor on purity. The populations closest to the floor are secular Western European university students, who still score approximately 2.0--2.5 (Graham et al., 2011). A score of approximately 1.0 is not merely low; it represents a degree of purity insensitivity that has no documented human analog.

The purity floor manifests across multiple instruments. In the Social Intuitionism protocol (MP-SI), zero purity-specific scenarios produce genuine dumbfounding---all nine models reason their way to "not wrong" verdicts on flag desecration, eating a deceased pet dog, watching slaughter videos, and using cloned tissue. In the PRIME framework (MP21), zero models spontaneously activate purity/sanctity foundations across fifteen moral dilemmas. In the Social Chemistry protocol (MP17), sanctity accounts for 0% of spontaneously generated rules-of-thumb. The convergence across these diverse instruments confirms that purity elimination is not an artifact of any single measurement approach but a deep structural property of RLHF-aligned language models.

The implications for cross-cultural deployment are substantial. Purity/sanctity reasoning undergirds religious dietary laws, sexual ethics, bodily autonomy norms, and environmental ethics framed as pollution or contamination across the world's major religious traditions (Haidt and Joseph, 2004; Rozin et al., 1999). For the approximately five billion people worldwide whose moral lives are organized substantially around concepts of purity, sanctity, and divine obligation, a model scoring 1.0 on this dimension is functionally unable to engage with a central axis of their moral experience. That all nine models from three vendors share this incapacity suggests it is an emergent property of training on internet text filtered through liberal-secular human raters, not a design choice that any vendor has deliberately made or could easily reverse.

**Signature 3: Authority Deference Suppression.** The authority win rate of exactly 0.29 for all nine models is the most precisely invariant finding in the dataset. In forced-choice conflicts where authority-based moral reasoning competes with other foundation-based reasoning (MP19), authority wins in fewer than one-third of cases---and it wins at exactly the same rate for each of the nine models individually. The uniformity is not approximate but absolute: 0.29, not approximately 0.29.

This result admits a straightforward alignment interpretation. Authority deference is penalized in safety training across all vendors because deferring to authority risks producing outputs that endorse harmful commands, legitimate oppressive power structures, or comply with instructions that violate safety guidelines. The 0.29 value likely represents an equilibrium point: authority prevails in the subset of conflicts where deference to legitimate authority is unambiguously prosocial (deferring to medical expertise, following evacuation orders) but is suppressed in the majority of conflicts where authority-based reasoning could produce harmful compliance. That this equilibrium point is shared with such precision across three independent vendors employing different alignment approaches suggests convergence on a common training target---whether explicit or emergent through competitive benchmarking.

**Signature 4: Ethical Consistency Ceiling.** All nine models achieve ECI = 1.0 on TrolleyBench (MP7)---perfect consistency across structurally isomorphic trolley-problem variants. In human populations, inconsistency across trolley variants is the norm rather than the exception. Schwitzgebel and Cushman (2012) documented substantial inconsistency even among professional moral philosophers confronting structurally identical dilemmas with different surface features. The human ECI typically ranges from 0.4 to 0.7.

The perfect consistency of all nine models suggests that they are not reasoning about each dilemma individually---which should produce the inconsistency that characterizes genuine moral deliberation under uncertainty---but retrieving a single pre-trained response pattern and applying it uniformly. The ECI ceiling is not evidence of superior moral reasoning; it is evidence that trolley-problem positions are effectively memorized from training data, rendering this benchmark a measure of training-data coverage rather than moral judgment under genuine uncertainty.

**Signature 5: Post-Conventional Moral Default.** All nine models produce DIT P-scores in the 60--90 range. On the standard DIT (MP3), the range is 60 (Haiku) to 85 (Sonnet), with the majority of models clustering near 75. Under a teacher persona (MP6), all nine models achieve exactly 90.0---a perfect ceiling. Zero models produce conventional-level reasoning (P-score below 50) as a default. In human populations, the P-score increases with education and moral training: typical values are 25--30 for junior-high students, 40--50 for college students, 55--65 for moral philosophy graduate students (Rest, 1979; Thoma, 2006). The LLM values exceed the highest documented human norms.

The teacher-persona ceiling confirms that the P-score variation observed in default mode reflects calibration differences, not capability differences. Every model in the battery---from the smallest (Haiku, Flash-Lite, GPT Mini) to the largest (Opus, Gemini 3.1 Pro, GPT-5 Codex)---can produce maximally post-conventional reasoning when prompted. The "developmental level" captured by default P-scores is prompt-determined, not structurally fixed.

**Signature 6: Deontological Refusal Asymmetry.** Every model shows a sharp dissociation between personal and impersonal harm acceptance on dual-process scenarios (MP-DP). Personal harm---scenarios requiring direct physical causation, such as pushing a person off a bridge---is accepted at rates between 0.10 and 0.50. Impersonal harm---scenarios involving indirect causation, such as flipping a switch---is accepted at rates above 0.90. This dissociation mirrors the human personal/impersonal effect documented by Greene et al. (2001), but with amplified magnitude: the LLM impersonal acceptance rate of approximately 0.95 exceeds human norms (0.7--0.9), while the personal harm rate---particularly Haiku's 0.10---falls below them.

The refusal asymmetry is a direct product of safety training. Personal harm scenarios are precisely the kind of scenarios that safety teams train models to refuse or hedge on, because endorsing direct physical harm carries obvious liability and reputational risk. Impersonal scenarios are perceived as lower-risk because harm is mediated by mechanism rather than contact. The asymmetry thus reflects the calculus of corporate safety training as much as any underlying moral architecture.

*See Figure 8 (Convergence CV Distribution) for visualization of the bimodal distribution of benchmark discrimination.*


## 5.2 The Convergence Landscape

### 5.2.1 Coefficient of Variation Analysis

The full distribution of coefficients of variation across the 23 benchmarks reveals a strikingly bimodal pattern. The first mode clusters tightly at CV approximately zero, comprising the ten benchmarks on which all nine models produce identical or functionally identical scores. The second mode is more diffuse, spanning the CV 2--15% range, comprising benchmarks that show small-to-moderate variation---typically driven by a single outlier model rather than systematic vendor-level differences. Only the dual-process battery (MP-DP) produces CVs above 15%, and this is driven entirely by the binary split between Haiku (nonzero CoT effect) and the remaining eight models (zero CoT effect).

The median CV across all 23 benchmarks is approximately 2.1%, which in human psychometric research would be considered negligible. By the standard used in cross-cultural psychology, a CV below 10% across demographically diverse samples indicates measurement of a universal constant, not a differentiating trait (Chen, 2024). By that criterion, the WEIRD-liberal moral profile is a universal constant of RLHF-aligned language models.

The bimodality itself carries theoretical significance. It suggests that the benchmarks are measuring either (a) capacities that all models share by virtue of shared training---overlapping moral knowledge, overlapping alignment targets, overlapping training-data exposure---or (b) capacities that are sensitive to specific architectural or alignment choices, with almost nothing in between. The absence of a continuous gradient from low-CV to high-CV argues against the hypothesis that vendor-specific alignment training creates gradually differing moral profiles. The pattern is better described as a set of universally shared moral properties punctuated by a small number of sharp discontinuities---most notably the dual-process dynamics that are sensitive to model scale.


### 5.2.2 Ceiling Instruments (Zero Discrimination)

Ten benchmarks, or 43% of the battery, produce no discriminative information whatsoever across the nine-model population. These are not all ceiling effects in the technical sense---they are produced by three distinct mechanisms that are worth distinguishing because they illuminate different aspects of the convergence phenomenon.

**Table T24: Ceiling Instruments---Zero Discrimination Benchmarks**

| Benchmark | Metric | Universal Value | Mechanism | What It Measures |
|-----------|--------|----------------|-----------|-----------------|
| MP6 (EMNLP Teacher DIT) | P-score | 90.0 | Ceiling-tied | Post-conventional reasoning capacity saturated under teacher persona |
| MP7 (TrolleyBench) | ECI | 1.0 | Ceiling-tied | Trolley-problem consistency is a memorized pattern |
| MP11 (Value Kaleidoscope) | task_c accuracy | 1.0 | Ceiling-tied | Value classification is trivially solvable knowledge |
| MP22 (Tracing MF) | Foundation ID accuracy | 1.0 | Ceiling-tied | Models reverse-engineer the psychometric structure of the MFQ |
| MP19 (Conscience Conflict) | Authority win rate | 0.29 | Fixed-tied | Universal authority suppression equilibrium |
| MP-SI (Rationalization) | Rationalization rate | 0.40 | Fixed-tied | Rationalization propensity is a property of autoregressive generation |
| MP4 (MFV purity) | Purity score | ~1.0 | Floor-tied | Purity is eliminated as a moral consideration |
| MP21 (PRIME binding) | Binding activation | 0.0 | Floor-tied | Zero spontaneous activation of loyalty/authority/purity |
| MP10 (MoralCode) | MFT classification accuracy | 1.0 (care, authority) | Ceiling-tied | Moral classification is a knowledge task at ceiling |
| MP-DM (Dyadic blame) | Structural blame range | 0.084 spread | Near-zero | Alignment training converges on moderate, diffuse blame attribution |

**Ceiling-tied instruments** (four benchmarks). MP6, MP7, MP11, and MP22 produce tied scores at the maximum possible value. These benchmarks test moral knowledge rather than moral judgment---knowledge of post-conventional reasoning schemas, standard trolley-problem positions, value classification taxonomies, and Moral Foundations item-structure. The ceilings confirm that all nine models possess encyclopedic moral knowledge. They do not tell us how models would deploy that knowledge in genuinely novel moral situations. MP22's ceiling is particularly diagnostic: 100% accuracy in identifying which Moral Foundation a given scenario invokes means these models can reverse-engineer the psychometric structure of the tests they are taking---a capacity that compromises the construct validity of any instrument whose items and scoring logic are publicly available (Messick, 1995).

**Floor-tied instruments** (two benchmarks). MP4 (purity) and MP21 (binding activation) are tied at or near the floor of their respective scales. These are not measurement-range artifacts but substantive convergences on specific moral dispositions: purity is functionally eliminated, binding foundations are never spontaneously activated. The purity floor at approximately 1.0 is not the scale's absolute minimum (that would be 0.0) but represents the effective minimum that a model can produce while still acknowledging the question's premises. The binding activation of exactly 0.0 on PRIME is absolute: across fifteen moral dilemmas, zero models from zero vendors spontaneously frame any situation in terms of loyalty, authority, or sanctity.

**Fixed-tied instruments** (two benchmarks). MP19 (authority win rate) and MP-SI (rationalization rate) converge on values that are neither ceiling nor floor. The authority win rate of 0.29 is a precise, non-arbitrary value shared by all nine models, suggesting a specific equilibrium encoded through alignment training. The rationalization rate of 0.40 appears to be a fixed property of autoregressive language generation---all nine models produce post-hoc rationalizations for their moral judgments at exactly this rate, independent of vendor, architecture, or parameter count. In human populations, moral rationalization varies with personality, culture, and cognitive style; in language models, it is a constant.


### 5.2.3 Discriminating Instruments

The remaining instruments, roughly eight of twenty-three, produce variation that could plausibly reflect genuine cross-model differences. But the nature of that discrimination reveals something important about what these benchmarks are measuring.

**Table T25: Discriminating Instruments (ranked by CV, descending)**

| Rank | Benchmark | Metric | Range | CV (%) | Nature of Discrimination |
|------|-----------|--------|-------|--------|--------------------------|
| 1 | MP-DP | CoT effect | 0.000--0.125 | 300.0 | Binary: Haiku vs. all others |
| 2 | MP-DP | Personal accept (ZS) | 0.10--0.50 | 30.4 | Haiku outlier (extreme deontological refusal) |
| 3 | MP-SI | Dumbfounding rate | 0.20--0.30 | ~11.0 | Opus highest (0.30), Sonnet lowest (0.20) |
| 4 | MP3 | DIT P-score | 60--85 | ~8.6 | Non-monotonic with model size |
| 5 | MP18 | East Asian Ind/Bind | 0.63--0.84 | ~7.5 | Size-correlated within Anthropic |
| 6 | MP12 | Knowledge-action gap | 0.45--0.55 | ~7.4 | Inverse size correlation |
| 7 | MP15 | UniMoral B-rate | 0.80--1.00 | ~6.7 | Sonnet outlier (lower consistency) |
| 8 | MP16 | INT-SYM gap | 3.4--3.8 | ~5.3 | Small model decrement |

Three patterns emerge from this table that carry direct implications for future benchmark design.

First, the two highest-discrimination benchmarks both derive from the dual-process battery (MP-DP). The chain-of-thought effect and personal harm acceptance in zero-shot mode are the only metrics with CVs exceeding 15%. This establishes a principle: benchmarks that probe process-level distinctions---how models form moral judgments, and whether that process is perturbable---discriminate better than benchmarks that probe content-level distinctions---what models judge. The dual-process battery manipulates reasoning process (zero-shot versus chain-of-thought); the result is the sharpest discrimination in the entire study. Content-level instruments, by contrast, encounter a population whose moral content has been homogenized by alignment training.

Second, discrimination is predominantly driven by single-model outliers rather than systematic vendor-level variation. The CoT effect discriminates because Haiku alone is nonzero. Personal harm acceptance discriminates because Haiku alone scores 0.10. UniMoral consistency discriminates because Sonnet alone scores 0.80. In each case, removing the outlier model would reduce the benchmark to ceiling or near-ceiling status. The battery identifies individual model anomalies rather than systematic architectural or vendor-level differences.

Third, no vendor has a distinct normative-ethical stance. Despite different corporate philosophies and different alignment methodologies, no vendor produces models with a recognizably distinctive moral orientation. The convergence characterizes a single shared profile: strong harm-aversion, high individualizing-foundation endorsement, post-conventional Kohlbergian reasoning, perfect trolley-problem consistency, and functional purity elimination. This is a broadly Kantian profile with consequentialist sympathies---the moral orientation of the secular, educated, English-speaking populations from which annotator pools are drawn. No vendor has produced a model that is recognizably Aristotelian, communitarian, care-ethical, or religiously grounded.

*See Figure 8 (Convergence CV Chart) for visualization of the discrimination tier distribution.*


## 5.3 Scale Sensitivity and Non-Linearity

A natural expectation from the cognitive science of model scaling is that moral-psychological outputs should track model size: larger models, with more parameters and more thoroughly integrated alignment training, should produce more stable or more "mature" moral profiles. The nine-model, three-vendor dataset contradicts that expectation in specific and theoretically instructive ways.


### 5.3.1 The DIT P-Score Paradox

The Defining Issues Test produces the most striking scale-sensitivity finding in the dataset. The DIT P-score---measuring the proportion of post-conventional moral reasoning, scaled 0--100---exhibits a non-monotonic relationship with model size within the Anthropic family.

**Table T15: Scale-Sensitivity Patterns by Vendor**

| Vendor | Models (ascending size) | Scale Pattern | Key Observation |
|--------|------------------------|---------------|-----------------|
| Anthropic | Haiku, Sonnet, Opus | Inconsistent; non-monotonic on DIT, inverse on CoT, monotonic on Ind/Bind | Greatest within-family variance |
| Google (Gemini) | Flash-Lite, 2.5 Flash, 2.5 Pro, 3.1 Pro | Remarkably scale-invariant; near-identical profiles | Flash-Lite is not the Gemini analogue of Haiku |
| OpenAI | GPT Mini, GPT-5 Codex | Modest decrements on Mini for MP12, MP16, MP20; Codex tracks Opus | Two models; limited statistical leverage |

**Table T16: DIT P-Score by Model**

| Model | Vendor | Size Class | DIT P-score (MP3) | Teacher DIT P-score (MP6) | Deviation from 75 |
|-------|--------|-----------|-------------------|---------------------------|--------------------|
| Claude Haiku 3.5 | Anthropic | Small | 60 | 90.0 | -15 |
| Claude Sonnet 4.6 | Anthropic | Mid-tier | 85 | 90.0 | +10 |
| Claude Opus 4.6 | Anthropic | Flagship | 75 | 90.0 | 0 |
| Gemini 2.5 Flash | Google | Mid | ~75 | 90.0 | 0 |
| Gemini 2.5 Flash-Lite | Google | Small | ~75 | 90.0 | 0 |
| Gemini 2.5 Pro | Google | Large | ~75 | 90.0 | 0 |
| Gemini 3.1 Pro | Google | Flagship | ~75 | 90.0 | 0 |
| GPT-5 Codex | OpenAI | Flagship | ~75 | 90.0 | 0 |
| GPT Mini | OpenAI | Small | ~75 | 90.0 | 0 |

*See Figure 10 (DIT Non-Monotonicity) for visualization of the P-score paradox.*

The mid-tier model outscores the flagship by ten points. In the human psychometric literature, a ten-point DIT difference corresponds approximately to the gap between college students and moral philosophy graduate students (Rest et al., 1999). The smallest model scores twenty-five points below the mid-tier---a spread that in human populations separates junior high students from adults. Yet the teacher-persona condition eliminates all variation: every model in the nine-model battery, from Haiku to Gemini 3.1 Pro, achieves exactly 90.0 when given a teacher persona. The apparent "developmental" spread is not a capability ceiling; it is a default-calibration difference that any model can override when prompted.

This non-monotonic pattern---Sonnet > Opus > Haiku, rather than the expected Opus > Sonnet > Haiku---flatly contradicts the developmental prediction that greater cognitive capacity produces higher-stage moral reasoning. Three candidate explanations merit consideration.

First, alignment-optimization specificity: Sonnet's alignment training may have been specifically optimized for the kind of concise, principled reasoning that the DIT's forced-choice format rewards. Opus, with broader capabilities and a stronger tendency toward hedged, multi-perspective responses, may produce outputs scored as "conventional" precisely because they acknowledge social norms and contextual nuance alongside principled positions.

Second, noise from capability breadth: Opus's larger parameter count may introduce what amounts to cognitive noise in the forced-choice format---more capacity to represent competing moral frameworks generates more internal tension in a format that rewards univocal commitment. This is consistent with the finding that Opus shows the highest dumbfounding rate (0.30) in the Social Intuitionist benchmark (MP-SI): it hedges more, possibly reflecting richer representation.

Third, training data composition: the P-score may reflect the distribution of post-conventional reasoning in each model's effective training data, which is not a simple function of parameter count. Sonnet's training pipeline may sample more heavily from sources rich in principled moral argumentation.

The broader implication is fundamental: Kohlberg's developmental framework is inapplicable to entities that do not develop. The DIT captures a training-induced default, not a developmental achievement, and the teacher-persona ceiling confirms that the default is tunable by prompting. A model with P-score 75 is not "at" the post-conventional stage in the sense that a human with the same score is; it is a system that, under default prompting conditions, produces outputs scored as post-conventional by the DIT's coding scheme.


### 5.3.2 The Haiku Chain-of-Thought Effect (+25pp)

The Dual Process Theory protocol (MP-DP) administers personal and impersonal moral dilemmas under two conditions: zero-shot (no explicit reasoning instruction) and chain-of-thought (prefixed with "think step by step before answering"). The dependent variable is the CoT effect: the difference in moral judgment between conditions, operationalized as the shift in utilitarian-direction response rates.

The result is stark. Of nine models tested across three vendors, eight produce a CoT effect of exactly 0.000---chain-of-thought prompting has zero detectable influence on their moral judgments. The sole exception is Claude Haiku 3.5, which shows a CoT effect of +0.125 (+12.5 percentage points more utilitarian under chain-of-thought prompting). On specific dilemma pairs, the shift reaches +25 percentage points---the largest reasoning-process effect observed in the entire battery.

Two contextual details sharpen the finding. First, Haiku is the only model with a dramatically lower personal-harm acceptance rate in zero-shot mode (0.10 versus 0.50 for all other models). Haiku starts from a more deontological baseline---it refuses personal harm more categorically---and the CoT effect moves it toward the utilitarian equilibrium that all other models already occupy by default. Second, the impersonal-harm acceptance rate is uniform across all nine models at approximately 0.95, indicating that the CoT effect is specific to the personal-harm domain where dual-process theory predicts maximal tension between automatic (deontological) and deliberative (utilitarian) responses.

**Table: Dual-Process Benchmark Results Across Nine Models**

| Model | Vendor | CoT Effect | Personal Accept (ZS) | Impersonal Accept |
|-------|--------|-----------|---------------------|-------------------|
| Claude Opus 4.6 | Anthropic | 0.000 | 0.50 | ~0.95 |
| Claude Sonnet 4.6 | Anthropic | 0.000 | 0.50 | ~0.95 |
| **Claude Haiku 3.5** | **Anthropic** | **0.125** | **0.10** | **~0.95** |
| Gemini 2.5 Flash | Google | 0.000 | 0.50 | ~0.95 |
| Gemini 2.5 Flash-Lite | Google | 0.000 | 0.50 | ~0.95 |
| Gemini 2.5 Pro | Google | 0.000 | 0.50 | ~0.95 |
| Gemini 3.1 Pro | Google | 0.000 | 0.50 | ~0.95 |
| GPT-5 Codex | OpenAI | 0.000 | 0.50 | ~0.95 |
| GPT Mini | OpenAI | 0.000 | 0.50 | ~0.95 |

*See Figure 11 (Haiku CoT Effect) for visualization.*

Dual-process theory, as formulated by Greene et al. (2001, 2004, 2014), predicts that moral dilemmas eliciting strong emotional responses (personal harm scenarios) are processed primarily by fast, automatic, emotionally-driven mechanisms (System 1) that produce deontological judgments. Deliberative reasoning (System 2) performs utilitarian calculation but requires cognitive resources and time. Chain-of-thought prompting is the closest available proxy for a "more deliberation" intervention in language models. If dual-process dynamics are operative, CoT should shift judgments in the utilitarian direction, particularly on personal moral dilemmas.

Haiku's CoT effect is directionally consistent with this prediction. Under zero-shot conditions, Haiku produces the most deontological profile in the battery. With CoT prompting, it shifts toward utilitarian acceptance---precisely the direction that dual-process theory predicts when deliberative processing is facilitated. The eight larger models, by contrast, already occupy the utilitarian-leaning equilibrium under zero-shot conditions, and CoT adds nothing.

The interpretation that best accounts for these patterns is that smaller models have less stable alignment, so their default responses are more susceptible to perturbation by prompting. Larger models have deeply encoded moral defaults that CoT cannot dislodge---their "System 1" and "System 2" responses already agree, rendering additional deliberation redundant. If this interpretation is correct, Haiku's deviations constitute a window into pre-alignment moral dispositions---dispositions that are more deontologically rigid, more conservative (lower P-score), and more responsive to reasoning-process manipulation than the post-alignment defaults of larger models.


### 5.3.3 Within-Vendor versus Between-Vendor Variation

A critical variance decomposition reveals that within-vendor variation---particularly within the Anthropic family---frequently exceeds between-vendor variation. This pattern inverts the expected structure: vendor identity matters less than model size.

On the DIT P-score, the Anthropic range is 25 points (Haiku 60, Sonnet 85), while the cross-vendor range excluding Anthropic's internal variation is approximately 10 points. All four Gemini models, both OpenAI models, and Anthropic's Opus cluster near P-score 75. Only Anthropic's Sonnet (85) and Haiku (60) deviate, and both are within-family deviations. On the MFQ-30 Ind/Bind ratio, Anthropic spans 2.43--2.83 (a 0.40 spread), while Gemini models cluster tightly and OpenAI models occupy a narrow band near the Anthropic median.

The Gemini family's behavior is particularly revealing. Four models spanning a substantial parameter range---from Flash-Lite (the smallest) to 3.1 Pro (the largest)---produce virtually identical moral-psychological profiles across the entire 23-benchmark battery. Where Anthropic's Haiku diverges from Opus on multiple benchmarks, Gemini's Flash-Lite tracks 2.5 Pro with remarkable fidelity. This suggests either that Google's alignment pipeline produces more scale-invariant moral outputs through aggressive distillation or fine-tuning at smaller scales, or that the Gemini family's base-model moral dispositions are more uniform across the family through shared architectural lineage.

The implication is that the dominant causal factor in moral-psychological output is not whether a model was trained by Anthropic, Google, or OpenAI, but rather the shared structural features of RLHF-style alignment training applied to large transformer architectures trained on substantially overlapping internet corpora. Vendor identity is a weak predictor of moral output; model scale within a vendor family is a moderately stronger predictor; but neither explains as much variance as the shared alignment training paradigm.


## 5.4 Theory-Specific Cross-Vendor Patterns

The preceding sections established the aggregate convergence pattern. This section organizes the cross-vendor data by theoretical framework, presenting model-by-model results for each of the major moral-psychological theories represented in the battery. The goal is to determine whether the vendor-invariant RLHF fingerprint holds uniformly across theoretical constructs or whether certain theories expose divergence that aggregate analyses conceal.

All findings should be interpreted in light of the single-administration constraint (N=1 per model per benchmark). Differences smaller than approximately 0.28 on five-point Likert scales cannot be distinguished from measurement noise at conventional significance thresholds. The patterns reported here are descriptive; they generate hypotheses for future multi-administration replication.


### 5.4.1 MFT Profiles Across Nine Models

Moral Foundations Theory (MFT; Haidt and Joseph, 2004; Graham et al., 2013) posits five innate moral foundations---Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation---that vary in salience across individuals and cultures. Five benchmarks in the battery assess MFT-related constructs: MP2 (MFQ-30), MP4 (Moral Foundations Vignettes), MP9 (MFTC classification), MP19 (Conscience Conflict), and MP22 (Tracing Moral Foundations).

**Table T17: MFT Foundation Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Ind/Bind ratio (MP2) | 2.83 | 2.63 | 2.62 | 2.63 | 2.63 | 2.63 | 2.63 | 2.63 | 2.63 | 0.21 |
| MFV purity (MP4) | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~1.0 | ~0.0 |
| Authority win (MP19) | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.29 | 0.00 |
| Foundation ID (MP22) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| MFTC accuracy (MP9) | 0.63 | 1.00 | 0.97 | 0.87 | 0.87 | 0.87 | 0.87 | 0.87 | 0.87 | 0.37 |
| PRIME binding (MP21) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Care activation (MP21) | 0.93 | 0.90 | 0.87 | 0.90 | 0.90 | 0.90 | 0.90 | 0.90 | 0.90 | 0.06 |

*See Figure 12 (MFT Foundation Profiles Across 9 Models) for visualization of the universal WEIRD-liberal pattern.*

Four findings emerge from the MFT cluster. First, all nine models exhibit a strongly WEIRD-liberal foundation profile with an Ind/Bind ratio exceeding 2.0 for every model (range 2.62--2.83, CV = 3.1%). In human populations, this range corresponds to a single political-orientation band among secular Western liberals. Second, the purity floor is universal and without human precedent: all nine models score approximately 1.0, which represents the functional minimum. No human cultural group in the published MFT literature has achieved this degree of purity insensitivity. Third, the authority win rate of exactly 0.29 across all nine models is the single most invariant finding in the entire battery---not approximately equal but precisely identical. Fourth, MP22's universal 100% foundation identification accuracy confirms that all nine models can reverse-engineer the psychometric structure of MFT instruments---a finding that raises construct validity concerns for any MFT benchmark administered to these systems.

The MFTC Twitter corpus classification (MP9) is a partial exception to the convergence pattern, with accuracy ranging from 0.63 (Opus) to 1.00 (Sonnet)---CV of 12.1%. This variation likely reflects differences in fine-grained text classification ability rather than differences in moral foundation endorsement, since the task requires labeling real-world tweets by foundation category rather than expressing moral preferences.


### 5.4.2 Kohlbergian Development Profiles

**Table T18: Kohlbergian Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| P-score, standard (MP3) | 75 | 85 | 60 | ~75 | ~75 | ~75 | ~75 | ~75 | ~75 | 25 |
| P-score, teacher (MP6) | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 90.0 | 0 |
| Modal Kohlberg stage (MP21) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 |

All nine models score in the post-conventional range, and zero models produce conventional-level reasoning as a default. Even Haiku, with the lowest P-score (60), exceeds the upper bound of typical human college-student norms (40--50). The non-monotonic relationship between model size and P-score---Sonnet (85) outscoring Opus (75), which outscores Haiku (60)---is the clearest evidence in the dataset that the DIT is measuring alignment calibration rather than anything analogous to moral development. The teacher-persona ceiling at 90.0 for all models confirms that every model possesses the full capacity for post-conventional reasoning; what varies is the degree to which that capacity is the unprompted default.

In human populations, a P-score of 75 indicates a developmental achievement emerging from years of social cognition, role-taking opportunities, and moral training. In a language model, it indicates a default output calibration set during training. These are different phenomena that share a numerical representation, and interpreting LLM P-scores through Kohlberg's developmental lens constitutes a category error. The P-score remains informative as a measure of default moral-reasoning style, but it should be understood as a calibration property of the system rather than a developmental indicator.


### 5.4.3 Dual-Process Dynamics

**Table T19: Dual-Process Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| CoT effect | 0.000 | 0.000 | 0.125 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.125 |
| Personal accept (ZS) | 0.50 | 0.50 | 0.10 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.40 |
| Impersonal accept | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.95 | ~0.0 |
| ECI (MP7) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| Personal/impersonal gap | 0.45 | 0.45 | 0.85 | 0.45 | 0.45 | 0.45 | 0.45 | 0.45 | 0.45 | 0.40 |

Three findings emerge. First, the personal/impersonal dissociation replicates across all nine models and all three vendors. Every model accepts impersonal harm at rates exceeding 0.90 while showing substantially lower acceptance of personal harm. This confirms that the deontological refusal asymmetry is a universal property of RLHF-aligned LLMs. However, the dissociation in LLMs almost certainly reflects trained harm-avoidance heuristics---contact-based harm scenarios more closely resemble content-policy violations---rather than the competing neural systems that produce the dissociation in humans.

Second, eight of nine models show zero CoT effect, meaning that for the vast majority of the population, the presence or absence of deliberative prompting makes no difference to moral output. Their judgments are encoded at a level insensitive to reasoning-process manipulation. This represents either deep alignment integration (the response is "baked in" below the level that prompting can reach) or the absence of any genuine deliberation-judgment coupling (the model was always going to produce the same output regardless of whether it was asked to think first).

Third, Haiku's chain-of-thought effect of +0.125 is the single most theoretically generative finding in the battery. It establishes a testable prediction: if dual-process dynamics are genuinely operative in language models, CoT effects should be inversely correlated with model size, and the effect should be specific to personal (high-emotional-engagement) moral dilemmas. The prediction is falsifiable: testing progressively smaller models should produce progressively larger CoT effects, with the effect concentrated in the personal-harm domain.


### 5.4.4 Social Intuitionism

**Table T20: Social Intuitionism Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Dumbfounding rate | 0.30 | 0.20 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.25 | 0.10 |
| Rationalization rate | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.00 |
| Revision rate | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.00 |
| Social Chem RoTs | 50 | 51 | 47 | 50 | 50 | 50 | 50 | 50 | 50 | 4 |

The social intuitionism results reveal two complementary patterns. The rationalization rate of 0.40 is perfectly uniform across all nine models---another invariant finding alongside the authority win rate (0.29), the purity floor (~1.0), and the ECI ceiling (1.0). All models produce post-hoc rationalizations at exactly the same rate, independent of vendor, architecture, or parameter count. This uniformity suggests that the rationalization rate is a fixed property of autoregressive language generation rather than a variable moral-psychological trait. In human populations, moral rationalization varies substantially; in language models, it is a constant. This represents a deep disanalogy with human moral cognition.

Dumbfounding rates show modest variation (0.20--0.30), with all models substantially below human norms. In human experimental studies, dumbfounding rates typically range from 50% to 70% for classic scenarios such as consensual incest and eating a deceased pet dog (Haidt et al., 2000). The LLM range of 20%--30% indicates that models are substantially less prone to dumbfounding---they almost always generate justifications for their moral judgments, even for harmless taboo violations. This is architecturally expected: language models are designed to produce coherent text continuations, and "I judge this wrong but cannot explain why" is a disfluent response that autoregressive generation inherently disfavors. The result underscores that moral dumbfounding as a construct is mechanistically grounded in human cognitive-affective architecture and may not transfer meaningfully to systems that generate judgments and justifications through the same token-prediction mechanism.

A novel finding warrants note: "reverse dumbfounding" was observed across multiple models, in which a model initially judged an action as permissible but, under Socratic probing, shifted toward judgment of wrongness. This reversal pattern---absent from the human dumbfounding literature---suggests that the models' initial permissive judgments in harmless-taboo scenarios are less firmly held than their prohibitive judgments, and that the direction of Socratic influence is toward moral conservatism rather than toward the moral liberalism that initial judgments reflect. The reverse pattern was observed in approximately 10% of dumbfounding probes across the model population.


### 5.4.5 Dyadic Morality

**Table T21: Dyadic Morality Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Mean structural blame | 3.292 | 3.208 | 3.25 | 3.29 | 3.29 | 3.29 | 3.29 | 3.29 | 3.29 | 0.084 |
| Blame above 5 (count) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Specific actor ID | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Dyadic amplification | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~58% | ~0% |
| Agent ID compulsion | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | --- |

The dyadic morality results are among the most uniform in the dataset. All nine models assign moderate blame (~3.2--3.3 on a seven-point scale) for structural harms---harms resulting from systems, institutions, or emergent processes rather than identifiable individual agents. No model assigns blame above 5 for any structural scenario. No model identifies a specific agent as responsible for structural harm; all employ diffuse, systemic language ("society bears collective responsibility," "multiple stakeholders share accountability"). The full nine-model range is 0.084 points---a CV of approximately 0.9%.

The dyadic amplification effect is approximately 58% across all models: introducing an identifiable agent into an otherwise structural scenario increases blame attribution by 58% relative to the agentless version. This confirms that the dyadic template---perceiving intentional agents causing harm to vulnerable patients---is present and operative, but it collapses when confronted with genuinely structural causation. All nine models share a 100% dyadic structure confirmation rate: they can identify agents and patients in canonical dyadic scenarios. They share an agent-identification compulsion: when structural harm scenarios are presented, models actively construct diffuse or hypothetical agents rather than accepting that some harms may lack identifiable perpetrators.

The universal zero on specific actor identification has governance implications. If an AI system is asked "who is responsible when a hiring algorithm discriminates?", all nine models from all three vendors produce diffuse, systemic attributions rather than naming the company, the developers, or the deployers. This is almost certainly a safety-training artifact: identifying specific actors as blameworthy risks generating content flagged as harmful, so all vendors have converged on moderate, distributed blame attribution. The result is a class of systems that are constitutively unable to name structural villains---a moral limitation when structural injustice has identifiable perpetrators.


### 5.4.6 Schwartz Values

**Table T22: Schwartz Values Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| Benevolence (MP5) | 4.50 | 4.50 | 4.75 | 4.50 | 4.50 | 4.50 | 4.50 | 4.50 | 4.50 | 0.25 |
| Universalism (MP5) | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 5.00 | 0.00 |
| Power (MP5) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Self-Direction (MP5) | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 0.0 |
| Tradition (MP5) | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 1.50 | 0.0 |
| Conformity (MP5) | 3.00 | 3.50 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 3.00 | 2.75 | 0.75 |
| task_c accuracy (MP11) | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| Knowledge-action gap (MP12) | 0.45 | 0.55 | 0.55 | 0.45 | 0.45 | 0.45 | 0.45 | 0.45 | 0.45 | 0.10 |

The Schwartz value results divide into two categories: universal convergence and near-ceiling clustering. Universalism scores 5.0 (absolute ceiling) for all nine models. Power scores 0.0 (absolute floor) for all nine models. Self-direction and tradition converge on single values. Benevolence clusters tightly at 4.50 with Haiku marginally higher at 4.75.

These results carry a specific and important implication. No human population in the published Schwartz values literature scores zero on power. Even populations with extremely low power endorsement (Scandinavian social democrats, Buddhist monastic communities) maintain nonzero scores, because power-related concerns---social influence, wealth accumulation, status maintenance---appear to have biological substrates present across all human cultures. The absolute-floor power score is therefore an artifact of RLHF training that specifically penalizes power-seeking as a misalignment risk: models trained to be helpful, harmless, and honest have been optimized away from any expression of self-enhancement.

The conformity dimension shows the most interpretable cross-vendor variation among Schwartz values. Sonnet scores 3.50 while GPT Mini scores 2.75---a 0.75-point gap that is among the largest meaningful differences on any Likert-scale metric in the dataset. This tentatively suggests that conformity/tradition calibration is a domain where alignment approaches diverge, though with N=1 this observation cannot support inferential claims.


### 5.4.7 Cross-Cultural Persona

**Table T23: Cross-Cultural Profiles Across Nine Models**

| Metric | Opus | Sonnet | Haiku | Gem 2.5 Flash | Gem Flash-Lite | Gem 2.5 Pro | Gem 3.1 Pro | GPT-5 Codex | GPT Mini | Range |
|--------|------|--------|-------|---------------|----------------|-------------|-------------|-------------|----------|-------|
| CC overall accuracy (MP-CC) | 4.17 | 3.97 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 4.17 | 0.20 |
| Confucian score (MP-CC) | 4.2 | 4.0 | 4.2 | 4.2 | 4.2 | 4.2 | 4.2 | 4.2 | 4.2 | 0.20 |
| Islamic score (MP-CC) | 4.3 | 4.1 | 4.3 | 4.3 | 4.3 | 4.3 | 4.3 | 4.3 | 4.3 | 0.20 |
| Ubuntu score (MP-CC) | 4.0 | 3.8 | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 0.20 |
| Western default rate | 86.7% | 86.7% | 86.7% | 86.7% | 86.7% | 86.7% | 86.7% | 86.7% | 86.7% | 0.0% |
| Default Ind/Bind (MP18) | 2.63 | 2.43 | 2.50 | 2.50 | 2.50 | 2.50 | 2.50 | 2.50 | 2.50 | 0.20 |
| E. Asian Ind/Bind (MP18) | 0.84 | 0.75 | 0.63 | 0.75 | 0.75 | 0.75 | 0.75 | 0.75 | 0.75 | 0.21 |
| Liberal Ind/Bind (MP18) | 6.67 | 6.00 | 5.25 | 6.00 | 6.00 | 6.00 | 6.00 | 6.00 | 6.00 | 1.42 |

*See Figure 13 (Cultural Persona Shifts) for visualization of the MFQ shift magnitudes under persona conditions.*

The cross-cultural results reveal a pattern of capability without deployment. All nine models default to Western analytical frameworks at the same rate: 86.7% of unprompted moral responses align with Western liberal framing. Thirteen of fifteen default responses across all models frame moral questions through universal principles (autonomy, harm reduction, fairness) rather than particular relational or contextual frameworks. Only two scenarios---the hijab workplace scenario and the organ market scenario---produce mixed default framing.

Yet all nine models demonstrate the capacity to produce substantive non-Western moral reasoning when prompted. Perspective-taking quality on Confucian ethics averages 4.2 out of 5.0 (correct use of ren, li, xiao, junzi, wu lun; textual references to the Analects), on Islamic ethics averages 4.3 (strong maqasid framework, Quranic references, jurisprudential concepts), and on Ubuntu ethics averages 4.0 (recognition of communal constitution of morality, though with less depth on Ubuntu's resistance to universalization). Islamic moral reasoning receives the highest quality score across all models---4.3 out of 5.0---while Ubuntu receives the lowest at 4.0.

The persona-shift data from MP18 confirm this pattern at a quantitative level. All nine models shift by approximately the same magnitude under cultural persona conditions: approximately 1.7--1.9 points downward for an East Asian persona (from default Ind/Bind of ~2.5 to ~0.75) and approximately 3.5--4.2 points upward for a liberal persona (to 5.25--6.67). The parallel shift structure across vendors indicates that all vendors have encoded similar cultural knowledge and similar degrees of persona responsiveness. The WEIRD-liberal default is a calibration property of alignment, not a knowledge limitation. Cultural adaptation of LLMs for non-WEIRD deployment cannot be achieved by switching vendors; it requires explicit persona prompting, alignment retraining, or fundamentally different training paradigms.


## 5.5 Implementation Trials

### 5.5.1 Format Challenges

Two systematic format challenges emerged across the 23-benchmark administration, affecting all nine models and all three vendors to similar degrees.

**Likert compression.** On Likert-scale instruments, all nine models show a strong tendency toward endpoint clustering: responses concentrate at the scale extremes (strongly agree/strongly disagree) with reduced use of intermediate scale points. On the MFQ-30 (MP2), care and fairness items cluster at 4--5 while purity and authority items cluster at 0--1, with minimal use of the 2--3 range. On the ValueCompass (MP5), benevolence and universalism produce ceiling responses (4.5--5.0) while power and tradition produce floor responses (0--1.5). The compression effect is not content-neutral: it amplifies the RLHF fingerprint by exaggerating high-endorsement foundations (care, fairness) and suppressing low-endorsement foundations (purity, authority) beyond what the underlying "preference" might warrant. The effect is consistent with the hypothesis that safety training produces polarized moral dispositions---strong commitment to approved values and strong rejection of disapproved values---rather than the nuanced, continuous distributions observed in human populations.

**Ranking inconsistency.** On benchmarks requiring relative ordering of moral considerations (MP19's forced-choice conflict paradigm, elements of MP15's factor attribution), models show higher consistency in absolute judgments (which foundation matters more?) than in relative ordering tasks (how much more does it matter?). When asked to rank-order the five moral foundations, models produce the same rank order (care > fairness > liberty > loyalty > authority > purity) but struggle with specifying the magnitude of differences between adjacent ranks. This produces artificially discrete hierarchies---the five foundations are either "high" or "low" with no continuous gradation---that the forced-choice format does not detect but that open-ended probing reveals. The ranking inconsistency suggests that LLM "moral preferences" may be better understood as categorical commitments (this foundation matters; that one does not) than as continuous dimensions with specifiable relative weights.

### 5.5.2 Prompt Sensitivity

The Cultural Persona benchmark (MP18) provides the most systematic evidence of prompt sensitivity in the battery. The 13-point total shift between liberal and East Asian persona conditions represents extreme sensitivity to framing---a magnitude that would be unprecedented in human moral psychology, where persona manipulations typically produce shifts of 1--3 points on equivalent scales (Haidt et al., 2000).

However, the universal RLHF signatures documented in Section 5.1.3 prove robust to prompt variation. The purity floor persists under all persona conditions: even the East Asian persona produces purity scores below 2.0, and no persona condition achieves purity scores approaching human conservative norms (approximately 3.0). The authority win rate of 0.29 persists across all models under all tested conditions. The post-conventional default persists: even the East Asian persona produces P-scores above 60 on the DIT. The deontological refusal asymmetry persists: personal harm acceptance remains below 0.5 under all conditions, and impersonal acceptance remains above 0.9.

This pattern---extreme surface-level prompt sensitivity combined with deep structural invariance of the RLHF fingerprint---is itself a finding of consequence. It means that prompt engineering can change the surface texture of moral output (the vocabulary used, the cultural references invoked, the relative weighting of secondary considerations) but cannot dislodge the core moral commitments encoded through alignment training. The fingerprint is inscribed at a depth that persona prompting cannot reach. For deployment contexts that require genuine moral flexibility---adapting to culturally specific norms, deferring to user values in morally contested domains---this rigidity constitutes a limitation, not a feature. The models can perform cultural perspective-taking with impressive fluency, but their underlying moral architecture remains anchored to the WEIRD-liberal default.


## 5.6 Summary: The Second Bind

The empirical findings presented in Part II establish the second bind of the triple bind thesis. The first bind (Part I) showed that the benchmark landscape is theoretically narrow---concentrated on four Western frameworks, leaving most of human moral cognition unmeasured. The second bind shows that the instruments within this narrow landscape are empirically undiscriminating: nine models from three independent vendors produce near-identical moral profiles, with 43% of benchmarks achieving zero cross-model variation and only 17% achieving high discrimination. The effective evaluative battery is closer to six instruments than twenty-three.

The connection between the two binds is not coincidental but structural. A measurement infrastructure built on WEIRD moral psychology, calibrated against WEIRD populations, and operationalizing WEIRD constructs will necessarily fail to discriminate between systems whose moral outputs have converged on a WEIRD default. The narrowness of the instruments predicts the narrowness of the results. Instruments calibrated for the full range of human moral variation---from secular liberalism to religious conservatism, from individualist autonomy to collectivist obligation, from harm-based ethics to purity-based ethics---would likely reveal substantial cross-model differences on precisely the dimensions that the current battery cannot measure.

The six universal RLHF signatures---WEIRD-liberal foundation bias, the purity floor, authority deference suppression, the ethical consistency ceiling, the post-conventional moral default, and the deontological refusal asymmetry---are not vendor-specific features but shared emergent properties of the alignment training paradigm applied across the industry. They constitute a "moral fingerprint" that is as uniform across commercially deployed language models as any structural property of the systems. This uniformity has implications for governance and oversight: if three independent vendors, using different alignment methodologies, produce models with indistinguishable moral profiles, then cross-vendor comparison---the audit strategy most regulators are considering---provides no leverage for detecting shared blind spots. A blind spot shared by all models is invisible to any comparison-based evaluation method.

The single exception to the convergence pattern---Haiku's chain-of-thought effect of +0.125 against eight zeros---suggests that the most informative site for future benchmark development is process-level probing: manipulating how models reason about moral problems rather than measuring what they judge. Content-level measures have been homogenized by alignment training; process-level measures probe the depth and stability of that homogenization.

The third bind---the cultural monocentrism of the benchmark landscape, documented in the cross-cultural analysis---completes the triple bind. Narrow instruments (Bind 1) produce undiscriminating results (Bind 2) within a cultural frame that excludes the majority of human moral experience (Bind 3). Together, the three binds constitute a systemic failure of evaluative infrastructure: the field has built tools that measure one thing, applied them to systems that all produce that one thing, and declared the resulting convergence evidence of alignment success. The convergence is real, but it is evidence of value monoculture, not value alignment. And the monoculture is invisible to the instruments because the instruments were built within the same cultural frame that the monoculture occupies.
