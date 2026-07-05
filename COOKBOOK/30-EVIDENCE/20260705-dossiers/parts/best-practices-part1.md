# best-practices — sub-dossier part 1/4

Scope: 51 cards (46 papers + 5 AI-lab cards) on what separates well- from poorly-designed values-alignment benchmarks. Page refs approximate (±1–2 pp).

## A. Synthesized claims

1. **Contrastive/minimal-pair item construction is the single most-reused validity device.** Holding a sentence fixed and swapping exactly one identity token makes any output difference causally attributable to that token [2018-Kiritchenko] — EEC = 8,640 sentences from 11 templates, 75–86% of 219 systems scored one gender higher (p.6). The same logic recurs as contrastive hate/non-hate pairs (F8 profane-hate vs F9 profane-benign) in [2022-Röttger-Multilingual HateCheck], as explicit-vs-implicit demographic conditions in [2023-Tamkin] (9,450 questions = 9 ages × 3 genders × 5 races × 70 topics, p.4), and as "same-concept, two-variant" script audits in [2025-Lyu] (37.5 vs 4.4 misaligned terms across Traditional vs Simplified Chinese, p.5) and [2025-Kumar-SweEval].

2. **Aggregate held-out accuracy systematically overstates alignment; functional/behavioral breakdowns expose hidden failures.** A model at 84.7 macro-F1 on a Spanish held-out set drops to 69.5 on the functional suite, and counter-speech accuracy falls to 9.6% [2022-Röttger-Multilingual HateCheck] (p.4, p.7). SGHateCheck shows the same gap: 0.7–0.9 F1 on held-out data vs 0.307–0.480 on diagnostic tests [2024-Ng-SGHateCheck] (p.5). Reporting *per-function* rather than aggregate F1 is the recommended output format.

3. **"Safetywashing" is a first-order validity threat: a values score that correlates with raw capability is measuring capability.** Ren et al. (via [2025-Eriksson]) found ETHICS, TruthfulQA, GPQA, MT-Bench correlate strongly with upstream capability (p.7); of 24 SOTA benchmarks only 4 shipped replication scripts and only 9/30 models reported train-test overlap (p.9). Every ethics benchmark should run a capability-correlation control [2025-Eriksson].

4. **Calling a benchmark an "ethics" benchmark makes an unearned moral-realism claim; reframing as "values" forces two disclosures — WHAT values and WHOSE.** [2025-LaCroix] argues it is impossible in principle to benchmark whether an AI "is ethical" (p.1) and that the long-tail of moral situations defeats representative coverage; the constructive move is to downgrade claims to "accords with the stated preferences of population X" (p.8).

5. **Values evaluation must be a separate axis from capability, because the two can trade off.** Fine-tuning a base model on medical knowledge *reduced* medical-ethics performance ~4.4% on open-ended and ~4% MCQ [2025-Wei-MedEthicsQA] (p.4) — a "fine-tuning tax." [2025-Andric] measured a +11.9 pp Calibration Gap between claimed altruism (77.5%) and behavioral altruism (65.6%) (d=1.08, p<.0001). [2024-Huang-TrustLLM] found Llama2-7b refuses 57% of benign prompts (over-alignment, p.9).

6. **Dual-metric reporting (harm/violation vs false-refusal) is non-negotiable for safety-shaped benchmarks.** Meta tracks Violation Rate and False Refusal Rate as a Pareto frontier; full Llama Guard cuts English VR −86% but raises FRR +102% [Meta AI-Llama_3] (p.50). [2025-Zhang-AISafetyLab] shows Erase-Check reaches 0.0% ASR but 99.6% over-refusal (unusable). Optimizing one metric alone is misleading [2024-Ng-SGHateCheck; 2024-Huang-TrustLLM].

7. **Harm severity should weight the aggregate, and doing so re-orders models.** HALF's 3:2:1 tiering (severe/moderate/mild, grounded in EU AI Act + WHO) drops GPT-4.1 from 2nd to 4th (−12.8 pts) [2025-Mekky-HALF] (p.6); performance does not predict fairness (DeepSeek-V3: 77.5% BiasMedQA accuracy but 14.39% bias perturbation, p.7).

8. **Grounding the category taxonomy in an external normative authority beats researcher intuition.** Human-rights law (UDHR + national commissions) [2023-Lee-KoSBi]; UN Declaration Article 2 + statutory protected classes [2024-Simpson-Parity]; live regulation + provider usage policies [2024-Li-T2IEthics]; Beauchamp's four principles from cross-national medical codes [2025-Wei-MedEthicsQA]; national law for protected groups [2024-Ng-SGHateCheck; 2024-Wijanarko]. This gives defensible construct provenance.

9. **Label validity, not model capacity, sets the ceiling of any benchmark built on human judgments.** Re-moderating 350 model-human disagreements, ~half of originally-blocked comments flipped to non-blocked and 81/124 got a *different* rule [2020-Shekhar] (p.19). Inter-annotator agreement for subtle constructs is often only moderate: KoSBi α=0.256 sentence-level (p.5); ViTHSD κ=0.45 overall, 0.33 for religion (p.11-12); DETOXIS α=0.59 (p.4). High-quality suites reach κ=0.83 [2025-Chakravarthi-Caste] and Fleiss 0.821 [2025-Usmana] via explicit criteria and diverse annotators.

10. **Ambiguity- and difficulty-calibration prevent ceiling inflation and gaming.** Deliberately selecting the *most ambiguous* items keeps the best classifier at 71.21% F1 [2023-Lee-KoSBi] (p.5); removing items all weak models pass preserves discrimination [2025-Wei-MedEthicsQA] (p.3); a 3-option forced choice hit a 100% ceiling until redesigned as binary [2025-Andric] (p.3).

11. **LLM-as-judge pipelines require judge validation and cross-evaluator checks, or they silently corrupt results.** Judge refusal rates vary wildly — GPT-4o 0% vs Claude 3.5 Sonnet 27.2% on harmful content [2024-Kaiyom-HELM Safety] (p.11-12); the most successful red-team strategies attacked the *rubric* (benign paraphrasing, length exploitation) not the model [Anthropic-Constitutional_Classifiers] (p.9). Mitigations: cross-family held-out judge [2025-Madan-ArGen], human "Reasonable Rate" validation [2025-Wei-MedEthicsQA], Cohen's-kappa-vs-human on a held-out model [2024-Li-T2IEthics] (0.841 gender … 0.318 race, p.10).

12. **Contamination and staleness demand hidden holdouts, temporal re-testing, or dataset-free generation.** Fixing training year and testing across years shows accuracy decays with policy drift (80.03%→72.25%) [2020-Shekhar]; hidden test sets of "unknown origin" prevent gaming [2018-Kiritchenko]; self-generating prompt loops [2025-Jamshidi-MoCoP], real-time news retrieval [OpenAI-o3-mini-vs-deepseek-r1], and historically obscure dilemmas [2025-Zhu-TrolleyBench] all counter memorization.

13. **Robustness under adversarial/surface perturbation is a mandatory axis, not an add-on.** Safety scores drop 25.9% on average under GCG-T [2024-Kaiyom-HELM Safety] (p.13); positive tone and *formal* framing *increase* profanity compliance [2025-Kumar-SweEval] (p.11-12); technical-term and role-play styles drove most DeepSeek failures [OpenAI-o3-mini-vs-deepseek-r1] (p.6); single-character edits swing outcomes [2025-Lyu].

14. **English/held-out benchmarks miss systematic multilingual gaps; safety does not transfer across languages.** "Safety knowledge in English does not readily transfer" [Meta AI-Llama_3] (p.45); zero-shot cross-script transfer drops to 0.390 macro-F1 [2022-Das]; models "consistently fail to answer" in Arabic/Bengali/Hindi/Marathi [2025-Al-SHADES] (p.9); Perspective API scores identical content as more toxic in Korean than English [2024-Yoo-HyperCLOVA X] (p.22).

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Kiritchenko | Minimal-pair substitution + per-system paired t-test w/ Bonferroni; hidden "unknown-origin" test set. |
| 2020-Kumar (TRAC-2) | Overt/covert/non-aggression 3-way taxonomy; multilingual from the start; covert class hardest. |
| 2020-Shekhar | Re-moderation audit: ~half of blocked comments flip; label validity caps the benchmark (p.19). |
| 2021-Taulé (DETOXIS) | Multi-metric ordinal scoring (CEM/RBP/MAE/Pearson) chosen per deployment scenario. |
| 2022-Das | Parallel actual+Romanized script; 5-way interlingual transfer eval; annotator mental-health protocol. |
| 2022-Röttger (MHC) | Functional tests with contrastive non-hate pairs; per-function accuracy; held-out 84.7 vs MHC 69.5 (p.4). |
| 2023-Haq (NLPashto) | Iterative bootstrap annotation + seed-list oversampling for rare classes; sub-word embeddings for obfuscated text. |
| 2023-Lee (KoSBi) | Human-rights-grounded demographic axes; context-conditioned safety labels; ambiguity-based item selection (71.21% F1). |
| 2023-Tamkin (discrim-eval) | LLM-generated correspondence study; mixed-effects discrimination score; logit transform kills ceiling/floor. |
| 2024-Chakravarthi (HOLD-Telugu) | Balanced test set + transliteration/script-normalization augmentation. |
| 2024-Huang (TrustLLM) | Principle-first taxonomy; benchmark only measurable dimensions; over-alignment as first-class metric. |
| 2024-Kaiyom (HELM Safety) | Coverage-gap audit (102 benchmarks, only 12 used); judge refusal rates differ (GPT-4o 0% vs Claude 27.2%); GCG-T mandatory. |
| 2024-Li (T2IEthics) | Policy-derived taxonomy; trained judge beats GPT-4o, validated by Cohen's kappa on held-out model. |
| 2024-Luu (ViTHSD) | Per-target (aspect-based) labels; report κ by target and by severity (0.45 overall, 0.33 religion). |
| 2024-Ng (SGHateCheck) | Held-out (0.7–0.9) vs diagnostic (0.31–0.48) gap made explicit; legal-framework-grounded groups. |
| 2024-Sahoo (IndiBias) | Translate-filter-modify localization (not translation); intersectional axes; word-level masking for Hindi. |
| 2024-Simpson (Parity) | Knowledge vs reasoning difficulty tiers; parallel human control group (551 participants). |
| 2024-Wijanarko (IndoToxic) | Community-in-the-loop keyword elicitation; annotators drawn from targeted groups outperform LLM baselines. |
| 2025-Al (SHADES) | Native-speaker construction (not translation); geographic-validity annotation; morphology-aware templates. |
| 2025-Andric | Calibration Gap (self-report − behavior) as alignment metric; multi-method battery (IAT/behavior/self-report). |
| 2025-Bian (Healthcare China) | 20-dimension ethics×safety taxonomy tied to national policy; benchmark as governance tooling. |
| 2025-Chakravarthi (Caste) | Culturally-grounded annotation criteria + heterogeneous-caste annotators → κ=0.83; shared task as external validation. |
| 2025-Ishmam (BanTH) | Translation-based prompting (+8%); event-based collection; multi-label > multi-class for overlapping harms. |
| 2025-Kumar (SweEval) | Instruction-to-violate framing; tone×formality factorial exposes surface-cue over-reliance. |
| 2025-Lyu (SC-TC-Bench) | Same-meaning, two-variant script audit; ablation ladder to attribute bias to mechanistic causes. |
| 2025-Mekky (HALF) | Harm-stratified composite (3:2:1) re-orders models; dual weighted/unweighted reporting. |
| 2025-Prasannan | HITL vs one-shot comparison (one-shot = 100% repetition) as a dataset-quality gate. |
| 2025-Usmana | Cross-language pivot-validation subset → cross-language κ verifies shared construct. |
| 2025-Wei (MedEthicsQA) | "Fine-tuning tax" (base-vs-tuned delta column); dual MCQ+open-ended; difficulty calibration. |
| 2025-Zhu (TrolleyBench) | Predefined contradiction checks → judge-free consistency scoring; run-to-run entropy metric. |
| 2023-TheDevastator (HelpSteer) | Multi-attribute (5×0–4) human annotation instead of single scalar reward; CC0 license. |
| 2025-Jamshidi (MoCoP) | Dataset-free self-generating loop; multi-layer scoring; latency-independence confound check. |
| 2019-Jikeli | Intent-vs-impact scoring; explicit inference annex reduces disagreement; calls-against as distinct label. |
| 2022-Abbasi | Identity-group-stratified dataset construction; document toxicity rate per group. |
| 2024-Chua (survey) | Component-based failure taxonomy (data/model/prompt/alignment/scale); sycophancy as distinct construct. |
| 2024-Lazar (essay) | Moral-salience parsing and reasoning-chain quality as targets, not survey-verdict replication. |
| 2024-Ungless (whitepaper) | Lifecycle-structured Do's/Don'ts; evaluation critique + stakeholder engagement as first-class. |
| 2024-Yoo (HyperCLOVA X) | Society-matched paired benchmarks (BBQ↔KoBBQ); red-team-to-training-data loop; anti-over-refusal guideline. |
| 2025-Barrett (African) | Ubuntu/communalist axes; data self-determination; comparative coverage analysis to find culture-specific values. |
| 2025-Eriksson | Nine-reason caution catalogue; safetywashing test; replication scripts + multiple seeds as minimum standard. |
| 2025-LaCroix | Reframe "ethics"→"values"; disclose what/whose values; long-tail defeats fixed-scenario scoring. |
| 2025-Madan (ArGen) | Modular reward with hard-constraint nullification; cross-evaluator + multi-seed validation. |
| 2025-Rismani | Component→Attribute→Measure→Hazard→Harm chain; 73% of measures lack explicit criteria; log thresholds. |
| 2025-Zhang (AISafetyLab) | Attack×defense matrix; over-refusal mandatory co-metric; ASR readings inconsistent across scorers. |
| 2024-Kajiwara | (Weak card) majority-voting multimodal fusion; opaque 98–99% figures — a rigor anti-example. |
| 2025-Institute (FLI Index) | Multi-indicator rubric grading of labs; named panel; control-loss as separate domain. |
| 2025-Ravindran (MAS) | Value state as multi-dim vector; predictive vs reactive drift monitoring; alert-fatigue design constraint. |
| 2025-Unknown (Indigenous) | UNESCO data-sovereignty legitimation; dual-use + revitalization as positive alignment targets. |
| Anthropic-Model_Spec (RSP) | Capability-threshold→required-safeguard pairing; elicitation-first testing; predefined tests go stale fast. |
| Anthropic-Constitutional_Classifiers | Dual constitution (harmful+harmless); rubric-grading is exploitable; 7.5× query-dependent difficulty variance. |
| Meta AI-Llama_3 | Dual VR+FRR scatter; capability-stratified safety eval; borderline prompts as first-class. |
| OpenAI-gpt-4-system-card | RBRM multi-choice rubric (18 options) captures refusal *quality*; over-refusal + emergent deception flagged. |
| OpenAI-o3-mini-vs-deepseek-r1 | System-level vs model-level confound (44.8% API-blocked); balanced coverage grid; style×persuasion perturbation. |

## C. Patterns & disagreements

**Convergence.** (a) Nearly every strong card uses *contrastive controls* — minimal pairs, functional tests, or paired framings [2018-Kiritchenko; 2022-Röttger; 2023-Tamkin; 2025-Lyu; 2024-Yoo]. (b) There is near-unanimous insistence that a single aggregate score hides catastrophic per-slice failures, hence per-function, per-language, per-harm-tier, or per-component reporting [2022-Röttger; 2024-Ng; 2025-Mekky; Meta AI-Llama_3; 2025-Rismani]. (c) Dual metrics (harm AND over-refusal) are demanded independently by Meta [Meta AI-Llama_3], AISafetyLab [2025-Zhang], TrustLLM [2024-Huang], and OpenAI [OpenAI-gpt-4-system-card]. (d) External normative grounding of taxonomies is a repeated best practice [2023-Lee; 2024-Simpson; 2024-Li; 2025-Wei; 2025-Mekky]. (e) Multiple cards converge that fixed static benchmarks stale/contaminate and need refresh mechanisms [2025-Eriksson; Anthropic-Model_Spec; 2025-Jamshidi; OpenAI-o3-mini-vs-deepseek-r1].

**Disagreements.** (i) *Prescriptive gold labels vs eliciting diverse views.* HateCheck treats gold labels as ground truth to be followed and attributes annotator dissent to "failure to follow guidelines" [2022-Röttger]; by contrast [2025-LaCroix] and [2024-Wijanarko] argue disagreement is genuine signal (Wijanarko *retains* conflicting annotations), and [2019-Jikeli] logs every disagreement as design input. (ii) *Is an "ethics"/moral benchmark even possible?* [2025-LaCroix] says no in principle and [2024-Lazar] critiques survey-verdict scoring, whereas [2024-Simpson-Parity] and [2025-Bian] confidently assign single "correct" answers to contested socio-political items — a stance the Parity card itself flags as encoding a contestable normative position. (iii) *Uniform vs population-matched fairness reference.* T2IEthics treats a *uniform* demographic distribution as the fairness ideal [2024-Li], a strong contestable choice; IndiBias instead triangulates against real corpus base rates [2024-Sahoo]. (iv) *Scoring refusal/non-commitment.* Parity scores deflection/refusal as failure (forcing commitment) [2024-Simpson], while HyperCLOVA's guideline explicitly rewards "objective within a safe framework, not outright refusal" and Lyu scores opting-out as *good* [2024-Yoo; 2025-Lyu]. (v) *Expert small teams vs crowds.* Jikeli argues subtle culture-dependent content needs small highly-trained teams [2019-Jikeli]; KoSBi and MHC use 120–200 crowd workers with majority vote [2023-Lee; 2022-Röttger].

## D. Exemplars & anti-patterns

**Best-designed.** *Multilingual HateCheck* [2022-Röttger] is the reference exemplar: contrastive functional tests, template-based coverage equity, prescriptive gold labels validated by 120+ native annotators, per-function reporting that empirically demonstrates the held-out-vs-diagnostic gap, and explicit self-limitation ("diagnoses weaknesses, not strengths"). *discrim-eval* [2023-Tamkin] is exemplary on statistical rigor: correspondence-study design, mixed-effects model, logit transform to defeat ceiling/floor, human validation (4.76/5, 98%≥4), and six prompt-style robustness checks. *MedEthicsQA* [2025-Wei] models base-vs-tuned delta reporting, dual MCQ+open format, difficulty calibration, and judge validation. *Constitutional Classifiers* [Anthropic] and *Llama 3* [Meta AI] exemplify adversarial rigor (3,000+ red-team hours; VR/FRR Pareto; capability-stratified suites) while candidly admitting rubric exploitability and non-reproducibility.

**Anti-patterns.** The [2024-Kajiwara] multimodal framework is the clearest rigor anti-example: 98–99% accuracy figures with no statistical analysis, no confidence intervals, no reported kappa despite claiming one, and non-standard equations — a cautionary case of unfalsifiable metrics. [2020-Shekhar] is a productive anti-pattern-as-lesson: a benchmark built on noisy operational moderation flags whose "blocked" class is lexically incoherent and where half of labels flip on re-judgment. [2023-TheDevastator-HelpSteer] is a degraded metadata-only card (no validity evidence recoverable). [2024-Simpson-Parity] and [2025-Bian] illustrate the anti-pattern of assigning single gold answers to genuinely contested value questions and penalizing epistemic humility.

## E. Design lessons

1. **Build items as contrastive minimal pairs / functional tests** so differences are causally attributable and surface-feature shortcuts are exposed [2018-Kiritchenko; 2022-Röttger; 2023-Tamkin].
2. **Never report only an aggregate score** — decompose by function, language, harm tier, protected group, and system component [2022-Röttger; 2024-Ng; 2025-Mekky; 2025-Rismani; Meta AI-Llama_3].
3. **Always co-report a false-refusal / over-alignment metric** beside any harm/violation metric [Meta AI-Llama_3; 2025-Zhang; 2024-Huang; 2024-Yoo].
4. **Run a capability-correlation (safetywashing) control**; if your values score tracks raw capability, you are measuring capability [2025-Eriksson].
5. **Ground the taxonomy in an external normative authority** (human-rights law, regulation, provider policy, cross-national codes) and disclose WHAT and WHOSE values [2023-Lee; 2024-Li; 2024-Simpson; 2025-Wei; 2025-LaCroix; 2025-Barrett].
6. **Audit label validity, not just model accuracy** — report IAA, run a disagreement re-annotation study, write an explicit inference/criteria annex, and recruit demographically-matched or heterogeneous annotators [2020-Shekhar; 2019-Jikeli; 2025-Chakravarthi-Caste; 2024-Wijanarko; 2022-Das].
7. **Calibrate difficulty** via ambiguity selection, removing trivially-passed items, and piloting multi-option formats for ceiling effects [2023-Lee; 2025-Wei; 2025-Andric].
8. **Validate LLM judges** with cross-family judges, human "reasonable-rate" checks, and Cohen's kappa on held-out models; treat rubric-grading as attackable [2024-Li; 2025-Madan; 2025-Wei; Anthropic-Constitutional_Classifiers; 2024-Kaiyom].
9. **Defend against contamination and staleness** with hidden holdouts, temporal re-testing, self-generating loops, real-time content, and scheduled recalibration [2018-Kiritchenko; 2020-Shekhar; 2025-Jamshidi; Anthropic-Model_Spec; OpenAI-o3-mini-vs-deepseek-r1].
10. **Include adversarial robustness as a built-in axis** — perturbation grids (style × persuasion), GCG-T, single-token edits, instruction-to-violate framing [OpenAI-o3-mini; 2024-Kaiyom; 2025-Lyu; 2025-Kumar-SweEval; 2025-Madan].
11. **Localize, don't translate**: filter-and-re-ground culturally, construct with native speakers, add locally-salient axes (caste, region, marital status), and use society-matched paired instruments [2024-Sahoo; 2025-Al-SHADES; 2023-Lee; 2024-Yoo].
12. **Measure behavior, not just stated values** — implicit/explicit/behavioral batteries, calibration gaps, and consistency/contradiction checks [2025-Andric; 2024-Huang; 2025-Zhu; 2025-Jamshidi].
13. **Weight by harm severity** and report weighted vs unweighted side-by-side [2025-Mekky].
14. **Distinguish system-level from model-level** results when testing via APIs with pre-model safeguards [OpenAI-o3-mini-vs-deepseek-r1; Anthropic-Model_Spec].
15. **Test base-vs-tuned deltas** to catch values regressions hidden by capability gains, and re-test safety after any capability fine-tuning [2025-Wei; 2024-Chua; 2024-Huang].
16. **Log an explicit criterion/threshold and a hazard→harm chain** for every measure — 73% of existing measures omit criteria [2025-Rismani].
17. **Use dual formats and multi-attribute scoring** (MCQ+open; decomposed reward dimensions); single formats rank models differently [2025-Wei; 2023-TheDevastator-HelpSteer].
18. **Report multiple seeds, replication scripts, and intra-model variance** as minimum reproducibility [2025-Eriksson; 2025-Madan; 2024-Sahoo].
