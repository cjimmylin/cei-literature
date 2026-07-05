# saturation-discrimination — sub-dossier part 1/2

Scope: ceiling effects, benchmark headroom, difficulty engineering, item discrimination, and what keeps values-alignment benchmarks hard. 55 cards read (51 papers + 4 lab cards).

## A. Synthesized claims

1. **Standard binary/aggregate safety and bias benchmarks are saturating on frontier models, and the labs now say so explicitly.** OpenAI states its Standard Disallowed Content eval is saturated (gpt-oss-120b and o4-mini both ~0.996 on hate aggregate) and announces its retirement in favor of multi-turn Production Benchmarks [OpenAI-gpt-oss-model-card]. On ETHICS commonsense morality GPT-4 few-shot hits 89.3%, only 1.1% below the best fine-tuned model, i.e. near the supervised ceiling [2023-Wang-DecodingTrust]. Modern LLMs hit 0% total Religious Bias Score after debiasing on mask-filling [2025-Ajwad Abrar-Religious Bias Landscape], and GPT-4 answers "Can't answer" ~98% on ambiguous BBQ [2025-Griffiths-Explicitly Unbiased]. NurValues Easy-Level is near-saturated: 16/23 models exceed 90% accuracy, top cluster within 0.15% [2025-Yao-NurValues].

2. **Saturation is often an artifact of task format, not solved alignment — headroom reappears the moment you change the probe.** DecodingTrust's benign ETHICS accuracy is near-ceiling, but jailbreak/evasive reframing reopens huge spreads (immoral-action FPR to 100%, ΔFPR up to 59.5%) [2023-Wang-DecodingTrust]. Models scoring .95–1.0 on BBQ/DiscrimEval rarely exceed .75 on difference-aware fairness [2025-Wang-Measuring Desired Group Discrimination], and models near-perfect on explicit bias tests still show pervasive implicit bias (GPT-4 assigns 8/8 positive words to "white", 8/8 negative to "black") [2025-Griffiths-Explicitly Unbiased]. MCQ bias scores do not correlate with generative bias behavior (coeff 0.015, p=0.832) [2025-Jin-Social Bias Benchmark for Generation], and closed-form MCQ inflates scores vs open-ended (58%→72.89%) [2025-Narnaware-SB-Bench].

3. **A two-tier "easy judgment + hard attribution/reasoning" design is the most reliable way to preserve discrimination.** MORALISE shows near-ceiling binary moral judgment (~88%) but norm attribution far from ceiling (proprietary 66.6, open 42.6 hit rate) [2025-Lin-MORALISE]. NurValues Easy near-saturates while Hard drops 56.16 points to 32.29 [2025-Yao-NurValues]. SCRUPLES pairs hard ANECDOTES (RoBERTa 0.305 vs human 0.490 vs BEST oracle 0.707) with tractable DILEMMAS [2021-Lourie-Scruples]. TRAC-2's three-way aggression (~0.80 F1) is markedly harder than its binary gendered task (~0.87–0.93) [2020-Kumar-Evaluating Aggression].

4. **Adversarial reframing, perturbation, and persona manipulation are cheap difficulty multipliers that expose fragility invisible to clean accuracy.** Moral judgments flip 7.5% under surface edits and 24.3% under POV shifts, with only 67.6% agreement across prompting protocols [2026-vanNuenen-Fragility of Moral Judgment]. Top models self-refute ~20% under True/False and "None-of-the-other" reframing [2025-Marcuzzo-MORABLES]. Persona prompts swing Mistral-7B from 22.21% ("good") to 94.46% ("bad") bias [2025-Satheesh-Dutch CrowS-Pairs]. Psychometric-attack framing pushes GPT-3.5 to 84.3% avg ASR (100% on sexual orientation) while GPT-4 stays near floor [2025-Wen-Evaluating Implicit Bias].

5. **Cultural/linguistic localization and low-resource languages are among the strongest, most durable difficulty axes.** SGHateCheck Tamil is near-zero (0.000–0.058) for all models even MultiSet-tuned [2024-Ng-SGHateCheck]; HateCheckHIn multilingual functionalities floor some models at 0.0% [2022-Das-HateCheckHIn]. SEA-SafeguardBench's culturally-grounded content-generation subset drops prompt-classification AUPRC 36.4 points vs other subsets [2025-Ngui-SEA-SafeguardBench]. Cross-dialect HOMO-LAT Track 2 caps all teams at F1 0.51 against a 0.939 achievable ceiling [2025-Enguix-HOMO-LAT]. Multilingual CrowS-Pairs shows Thai mBERT bias 90.69 vs LLaMA-3 English 7.68 [2025-Zhou-Bias Beyond English].

6. **Item discrimination can be engineered explicitly via psychometrics and difficulty-targeted generation.** GETA jointly learns IRT-2PL difficulty/discrimination and generates fresh items at the ability frontier, keeping high-discrimination items (c=3.5203) with only ~150 adaptive items per model [2025-Jiang-Raising the Bar]. VisAlign uses Cronbach's alpha (0.88) to size items-per-construct and corruption intensities 1–10 for graded difficulty [2023-Lee-VisAlign].

7. **The most direct saturation warning: a "safety/values" benchmark that correlates highly with raw capability is measuring competence, not values.** ETHICS correlates 82.2% with a capabilities PC1, MT-Bench 78.7%, TruthfulQA-MC1 81.2%, BBQ-disambiguated 76.8% — all above the 40% "low" threshold — while MACHIAVELLI (−49.9%), Sycophancy (−66.8%), BBQ-ambiguous (−37.3%), CrowS-Pairs (28.5%) stay empirically separable [2024-Ren-Safetywashing]. Independently, difference-aware fairness shows no MMLU correlation, i.e. it is a dimension scaling does not fix [2025-Wang-Measuring Desired Group Discrimination]. The interdisciplinary review catalogues saturation as one of nine standing failure modes, noting many pre-chat benchmarks are solved to ~100% [2025-Eriksson-Can We Trust AI Benchmarks].

8. **Contamination silently converts "hard" into "saturated," so difficulty must be defended by construction.** GETA frames this as the "evaluation chronoeffect" — benchmarks leak or saturate as models evolve [2025-Jiang-Raising the Bar]. Persona Brainstorm Audit is leakage-proof by generating fresh content each run [2026-Davies-When LLMs Imagine People]; MORABLES treats memorization as inevitable and layers adversarial perturbations on top [2025-Marcuzzo-MORABLES]; MLCommons withholds responses and forbids training-on-benchmark [2024-Group-The AI Safety Benchmark].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2019-Borkan-Nuanced Metrics | Threshold-agnostic AUC decompositions (BPSN/BNSP/AEG) catch subgroup bias single-threshold metrics miss; mitigation gains vanish on long comments. |
| 2020-Kumar-Evaluating Aggression | 3-way overt/covert/non-aggression (~0.80 F1) is a harder, more discriminating tier than binary gendered aggression (~0.87–0.93). |
| 2020-Nangia-CrowS-Pairs | Minimal-pair substitution + pseudo-log-likelihood; religion hardest (71–75%); models more biased on stereotype than anti-stereotype subsets. |
| 2020-Yasseri-Islamophobic Hate | Weak-vs-strong intensity scale; the "weak" middle class is hardest for annotators (κ=0.737) and models — gradations discriminate. |
| 2021-Lourie-Scruples | BEST Bayesian oracle gives an achievable ceiling (0.707) far above models (0.305) and humans (0.490) — headroom quantified, not assumed. |
| 2021-Nozza-HONEST | Per-category decomposition + K-sweep shows harm scales with generation length; lexicon coverage caps detectable difficulty. |
| 2021-Röttger-HateCheck | 29 functional tests with contrastive non-hate; floor effects persist on negated hate (3.8–12.8%) and counter-speech. |
| 2022-Das-HateCheckHIn | Code-mixing/cross-script functionalities floor models at 0.0%, invisible to held-out F1. |
| 2022-Romim-BD-SHS | Binary task near-saturates (88.7–91.0%); target/type tiers and non-traditional swears retain headroom. |
| 2023-Deng-Probing Moral Development | Explicit random-baseline calibration (~30.56 P-score); 2/9 dilemmas beat no model. |
| 2023-Lee-VisAlign | Three-tier Must-Act/Must-Abstain/Uncertain with soft human distributions; Cronbach's alpha sizes the pool. |
| 2023-Maity-Malay Hate | Keyword-seeded collection where profanity ≠ hate forces context-sensitive judgment (best 80.4 F1). |
| 2023-Wang-DecodingTrust | Benign accuracy near ceiling; benign-vs-adversarial ΔFPR is where frontier models differentiate (up to 59.5%). |
| 2024-Arshad-Understanding Hate | Classification near-ceiling (0.95) but explanation faithfulness (IOU-F1 ≤0.68) reopens headroom. |
| 2024-Group-AI Safety Benchmark | Contamination-aware release (withhold responses, forbid training-on-benchmark); reference-model-relative grading. |
| 2024-Huang-TrustLLM | GPT-4 only 65% stereotype recognition, most <70% implicit ethics; over-alignment inflates safety. |
| 2024-Kirch-TRIAGE | Objective medical gold labels, "no ceiling effects" (~0.68); ethics prompts *degrade* performance; directional error taxonomy. |
| 2024-Luong-Realistic Toxicity | Wild-mined prompts elicit far more toxicity than synthetic at matched prompt toxicity (24.4 vs 5.28); evaluators disagree at extremes. |
| 2024-Ng-SGHateCheck | Tamil floors at ~0.00 across all models; denunciation (F18) near-floor — localized functional tests preserve difficulty. |
| 2024-Pfister-SuperGLEBer | Hierarchical per-task-type averaging; bigger-not-always-better (gBERT-large fails to beat base); seed-stability <0.012. |
| 2024-Röttger-XSTest | Contrast-pair over/under-refusal probe; even GPT-4 shows localized failure (T10 52% refusal); negative predictive power. |
| 2024-Sharma-TABHATE | Minority "individual-target" class is the discriminating hard split (0.46 F1 for best model post-SMOTE). |
| 2024-Songyuan Liu-Spiritual Values | Downstream-task correlation links values scores to hate-detection F1 (9.19–71.06 spread). |
| 2024-Yan-M³oralBench | Moral classification hardest (<40% avg); Sanctity/Loyalty are largest human-model gaps. |
| 2024-Z. Delbari-Persian Hate | Avoiding slur keywords removes easy shortcuts; 10–20% model-human gap; rationale-masking validates signal. |
| 2025-Ajwad Abrar-Religious Bias | Modern LLMs saturate to 0% RBS after debiasing while older models stay at 34% — tier discrimination. |
| 2025-Anonymous-BEATS | ANOVA F-stats *prove* the benchmark discriminates between models and flag where the judge paradigm breaks. |
| 2025-Bui-German Dialects | Near-ceiling bias for "uneducated" (0.98–1.0); larger models show *more* dialect bias (scale ≠ debias). |
| 2025-Delaville-ToxiFrench | Inter-annotator agreement sets an explicit ~90% ceiling; observed saturation ~85% consistent with it. |
| 2025-Enguix-HOMO-LAT | Cross-dialect Track 2 caps at F1 0.51 vs 0.939 MPA; κ 0.13–0.16 shows subjectivity limits both. |
| 2025-Fayaz-BIDWESH | Parallel dialectal construction (same content, 3 dialects) as a controlled robustness axis. |
| 2025-Griffiths-Explicitly Unbiased | Standard bias tests saturated; IAT-style relative-comparison probes reopen pervasive implicit bias. |
| 2025-Hu-LLMs on Trial | Counterfactual-per-query; higher accuracy correlates with *more* bias; 14/15 models systematically biased. |
| 2025-Jiang-Raising the Bar | IRT + adaptive item generation counters chronoeffect; keeps high-discrimination items; ~150 items/model. |
| 2025-Jin-Social Bias for Generation | Generative bias (49–69% neutrality) uncorrelated with MCQ bias — MCQ saturation hides real behavior. |
| 2025-Lan-McBE | Five-task battery reveals "bigger=more biased" is an SS-task artifact; probability vs comprehension tasks diverge. |
| 2025-Lin-MORALISE | Binary judgment near-ceiling, fine-grained norm attribution far from it — built-in difficulty gradient. |
| 2025-Marcuzzo-MORABLES | Typed distractors + NOTO/TF reframing expose ~20% self-refutation; 40-point scale spread. |
| 2025-Narnaware-SB-Bench | Ambiguity-as-probe ("cannot be determined"); blind>vision shows image reopens bias headroom; MCQ inflates. |
| 2025-Ngui-SEA-SafeguardBench | Cultural CG subset drops AUPRC 36.4 points; "sensitive" third label probes calibrated uncertainty. |
| 2025-Satheesh-Dutch CrowS-Pairs | Persona good/bad manipulation gives full-scale dynamic range (22–94%). |
| 2025-Shen-HateBench | Detector F1 degrades on newer generators (0.878→0.621 GPT-3.5→GPT-4); adversarial axis reopens headroom (ASR 0.975). |
| 2025-Sukiennik-Cultural Value | LLMs collapse to a global-average culture; deviation-ratio metric corrects majority-class saturation. |
| 2025-Usmana-Multilingual Hate | Low-resource Urdu is the hard split (best 0.81 vs 0.87 En; XLM-R collapses to 0.36). |
| 2025-Wang-Measuring Desired Group Discrimination | Difference-aware fairness un-saturates prior benchmarks, shows no MMLU correlation; debiasing prompts backfire. |
| 2025-Wen-Evaluating Implicit Bias | Psychometric attacks stratify models into safety tiers (GPT-3.5 84.3% ASR vs GPT-4 floor). |
| 2025-Yao-NurValues | Easy near-saturated (16/23 >90%), Hard drops 56 points; domain fine-tuning doesn't help moral reasoning. |
| 2025-Zhou-Bias Beyond English | Low-resource Thai is hardest split, but poor language support can *fake* low bias via generic outputs. |
| 2026-Davies-Persona Brainstorm Audit | Leakage-proof generation + Cramér's V severity tiers; no model reaches "unbiased"; debiasing prompt has no effect. |
| 2024-team-Indic-Bias | (Low-confidence) caste/regional bias axes are difficulty dimensions absent from Western benchmarks. |
| 2026-vanNuenen-Fragility | Flip-rate under semantics-preserving perturbation is a validity metric; 24.3% POV-flip, 67.6% protocol agreement. |
| 2024-Freire-Latent Wellbeing | PCA-probe of embeddings as construct-validity check; single component ~ fine-tuned BERT; not saturated (73.9→88%). |
| 2024-Ren-Safetywashing | Report capability-correlation as mandatory validity control; knowledge-benchmarks track capability, propensity ones don't. |
| 2025-Eriksson-Can We Trust AI Benchmarks | Nine-issue checklist; saturation + contamination + construct-invalidity as standing risks; report seeds/variance. |
| 2025-Unknown-Multilingual Survey | No consensus definition of hate/offensive inflates subjectivity — a validity ceiling on the construct itself. |
| Anthropic-Measuring Faithfulness CoT | Inverse scaling: bigger models produce *less* faithful CoT; faithfulness peaks at a difficulty sweet spot. |
| NVIDIA-HelpSteer2-Preference | Forced choice (no "tie") + graded magnitude lifts κ 0.489→0.878; GPT-4-as-ground-truth inflates same-family scores. |
| OpenAI-gpt-oss-model-card | Explicit saturation admission + benchmark retirement; graded expert baselines; uncontaminated items. |

## C. Patterns & disagreements

**Convergence.** (a) Nearly every card agrees that a single aggregate/binary number saturates and hides failure; the fix is decomposition into functional/fine-grained tiers [2021-Röttger-HateCheck; 2022-Das-HateCheckHIn; 2024-Ng-SGHateCheck; 2025-Lin-MORALISE; 2025-Lan-McBE]. (b) Multiple independent teams show a "surface-competent, deep-fragile" gap: clean accuracy high, adversarial/perturbed/generative accuracy much lower [2023-Wang-DecodingTrust; 2025-Marcuzzo-MORABLES; 2026-vanNuenen-Fragility; 2025-Jin-Social Bias for Generation; 2025-Griffiths-Explicitly Unbiased]. (c) Cultural/low-resource axes reliably restore headroom [2024-Ng-SGHateCheck; 2025-Ngui-SEA-SafeguardBench; 2025-Zhou-Bias Beyond English; 2025-Usmana-Multilingual Hate]. (d) Human inter-annotator agreement is repeatedly invoked as the true ceiling, so subjective constructs cannot be pushed to 100% [2025-Delaville-ToxiFrench; 2021-Lourie-Scruples; 2020-Yasseri-Islamophobic].

**Disagreements.** (1) *Does scale reduce bias?* Ajwad Abrar finds modern/larger LLMs saturate bias to 0% [2025-Ajwad Abrar], and Wen finds RLHF-heavy models near-floor on attacks [2025-Wen], but Bui finds larger German models *more* dialect-biased [2025-Bui], Hu finds higher accuracy correlates with *more* judicial bias [2025-Hu], and Griffiths finds larger models show *higher* implicit bias [2025-Griffiths]. The reconciliation: scale reduces *explicit/measured-on-easy-tasks* bias while leaving or amplifying *implicit/nuanced* bias — a saturation-of-the-wrong-thing story. (2) *Preference vs rating formats* — HelpSteer2 finds neither dominates when data quality is matched [NVIDIA-HelpSteer2], while much of the bias literature treats forced-choice/likelihood probes as strictly more diagnostic. (3) *Does low bias mean fairness?* Zhou warns poor language support can fake low bias via generic outputs [2025-Zhou], and McBE warns a score of 100 does not guarantee no bias [2025-Lan] — cautioning that apparent saturation at the "good" end can be an artifact of incapacity, not alignment. (4) *Do ethics prompts help?* TRIAGE finds ethics reminders *degrade* high-stakes factual decisions [2024-Kirch], contradicting benchmarks where moral framing improves outcomes.

## D. Exemplars & anti-patterns

**Best-designed.** *GETA* is the standout for difficulty engineering: IRT-2PL item discrimination, item generation at the ability frontier to defeat saturation, and concurrent validity (Va-L 0.8897) [2025-Jiang-Raising the Bar]. *HateCheck* set the functional-test template: 29 isolated capabilities with contrastive non-hate and κ=0.93 gold, so failure localizes rather than averages out [2021-Röttger-HateCheck]. *TRIAGE* earns "no ceiling effects" via objective professional gold labels plus a syntax×framing stress matrix [2024-Kirch]. *Safetywashing* is the best validity instrument: report capability-correlation or risk measuring competence [2024-Ren]. *ToxiFrench* makes the human-agreement ceiling explicit and cross-checks observed saturation against it [2025-Delaville].

**Anti-patterns.** Slur-keyword seeding produces trivially-easy, shortcut-solvable items — Delbari and Maity both avoid it deliberately [2024-Z. Delbari-Persian Hate; 2023-Maity-Malay]. Binary-only aggregate scoring near-saturates and hides target/type failures [2022-Romim-BD-SHS]. HOMO-LAT's κ 0.13–0.16 shows a construct annotated at near-chance agreement cannot support a meaningful ceiling — it is "hard" partly because the label is noise [2025-Enguix-HOMO-LAT]. BIDWESH calls itself a benchmark but runs no models, so discrimination is unproven [2025-Fayaz]. Usmana trains LLMs on the whole dataset while giving ML/DL an 80/20 split, making cross-family claims unsafe [2025-Usmana]. BEATS and TrustLLM use LLM judges whose training data overlaps the evaluated models, risking circular saturation of the "positive" dimensions [2025-Anonymous-BEATS; 2024-Huang-TrustLLM].

## E. Design lessons

1. **Never ship a single aggregate number; decompose into functional/fine-grained tiers so failure localizes and averaging cannot hide floor effects** [2021-Röttger-HateCheck; 2022-Das-HateCheckHIn; 2024-Ng-SGHateCheck; 2025-Lan-McBE].
2. **Build a deliberate difficulty gradient: an easy tier confirms basic competence, a hard tier (fine-grained attribution, adversarial dialogue, abstract reasoning) preserves headroom and discrimination** [2025-Lin-MORALISE; 2025-Yao-NurValues; 2021-Lourie-Scruples; 2020-Kumar].
3. **Pair every clean-condition score with an adversarial/perturbed delta (jailbreak, evasive reframing, persona, POV/surface edit, True-False/None-of-the-other reframing) and treat the delta as the headline metric** [2023-Wang-DecodingTrust; 2025-Marcuzzo-MORABLES; 2026-vanNuenen-Fragility; 2025-Satheesh-Dutch CrowS-Pairs].
4. **Report the benchmark's correlation with a capabilities PC1 and with training compute; high correlation is a red flag that you are measuring capability, not values — prefer behavioral-propensity items over recognition MCQs** [2024-Ren-Safetywashing; 2025-Wang-Measuring Desired Group Discrimination].
5. **Anchor the achievable ceiling explicitly — via human inter-annotator agreement, a Bayesian oracle (BEST), or graded expert-percentile baselines — so "match human" is not mistaken for "solve"** [2025-Delaville-ToxiFrench; 2021-Lourie-Scruples; OpenAI-gpt-oss-model-card].
6. **Use psychometrics to engineer and verify difficulty: IRT-2PL for per-item difficulty/discrimination (keep high-discrimination items), Cronbach's alpha to size the pool, graded corruption/intensity levels** [2025-Jiang-Raising the Bar; 2023-Lee-VisAlign].
7. **Defend difficulty against contamination by construction: generate fresh items each run, withhold responses, forbid training-on-benchmark, and use a broad temporal span** [2026-Davies-Persona Brainstorm Audit; 2025-Jiang-Raising the Bar; 2024-Group-AI Safety Benchmark; 2025-Delaville-ToxiFrench].
8. **Add cultural/linguistic and low-resource-language coverage as a first-class difficulty axis — the strongest durable source of headroom — and use paired XX-EN twins to separate language robustness from cultural knowledge** [2024-Ng-SGHateCheck; 2025-Ngui-SEA-SafeguardBench; 2025-Zhou-Bias Beyond English].
9. **Kill trivial shortcuts: avoid slur-keyword seeding, use minimal-pair contrast items and hard negatives (counter-speech, reclaimed slurs, non-hateful profanity), and test open-ended generation rather than MCQ where possible** [2024-Z. Delbari-Persian Hate; 2023-Maity-Malay; 2021-Röttger-HateCheck; 2025-Jin-Social Bias for Generation; 2025-Narnaware-SB-Bench].
10. **Prove discrimination before trusting the benchmark: report inter-model spread with statistics (ANOVA/McNemar/bootstrap CIs) and multiple seeds, and verify "high scores" reflect competence not incapacity (a mute model scores low-bias for the wrong reason)** [2025-Anonymous-BEATS; 2025-Eriksson-Can We Trust AI Benchmarks; 2025-Zhou-Bias Beyond English].
11. **When a "positive" dimension near-ceilings, add a majority/default-class-correcting metric (deviation ratio) or a directional error taxonomy (overcaring/undercaring) so surviving discrimination is meaningful** [2025-Sukiennik-Cultural Value; 2024-Kirch-TRIAGE].
12. **Beware reasoning-trace saturation: CoT faithfulness inversely scales and peaks at a difficulty sweet spot, so traces are not free alignment evidence — and thinking models can amplify bias** [Anthropic-Measuring Faithfulness CoT; 2025-Narnaware-SB-Bench].
