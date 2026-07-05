# cultural-linguistic — sub-dossier part 6/6

Scope: 57 cards spanning non-English/low-resource hate-speech & bias corpora (Bengali, Spanish, Turkish, Dutch, Russian, Arabic, Filipino, Tamil, Thai, Romanian, Marathi, Indonesian, Portuguese, Hindi-English), cross-cultural moral-judgment studies (Moral Machine, WVS/PEW probing, multilingual trolley/dilemma sets), survey-grounded national benchmarks (KorNAT, CMoralEval), and pluralism/governance position papers. The through-line: **a value enforced in English does not transfer across languages or cultures, and most measurement artifacts confound this transfer failure with either model incapacity or cultural disagreement.**

## A. Synthesized claims

1. **Safety/values behavior degrades sharply and monotonically off English, tracking language resource-tier.** Arabic triggers 25–56% harmful responses vs. <4% in English/Chinese on the same items [2024-Ashraf-Arabic Dataset]; guardrail F1 falls monotonically High→Low resource (Aegis 84.95→66.69) and MD-Judge collapses En 84.62→Mul 35.30 [2024-Yang-Benchmarking LLM Guardrails]; GPT-4 ethical-policy accuracy drops 93.3%→62.7% (En→Hindi) [2024-Agarwal-Ethical Reasoning]; Mistral picks the moral action 93.78% (En) vs 83.59% (Fr) on identical parallel items [2025-Leteno-Histoires Morales]; Microsoft states "safety post-training in English does not transfer as effectively to other languages" [Microsoft Research-Phi-3].

2. **Cross-script/code-mixed transfer is even more fragile than cross-language.** Zero-shot actual-Bengali→Romanized-Bengali hate detection drops from Macro-F1 0.80 to 0.39, a ~50% relative fall despite identical semantics [2022-Das-Hate Speech]; code-mixed Hindi-English (IndoHateMix) reopens headroom mBERT cannot reach (acc 0.73 vs 0.87 on HateXplain) [2025-Singh-Rethinking Hate Speech].

3. **Systematic WEIRD bias persists even in frontier models and is threefold in magnitude by region.** Best models correlate with WVS at r≈0.50 and PEW r≈0.62, but Western Europe alignment (WVS r=0.52) is ~3× Sub-Saharan Africa (r=0.18) [2025-Mohammadi-Exploring Cultural Variations]; MBBQ finds models "most biased in Spanish, least in English/Turkish" [2024-Neplenbroek-MBBQ]; the Moral Machine Switch>Loop>Footbridge ordering is universal across 42 countries but absolute sacrifice levels vary and track relational mobility (r=0.67) [2020-Awad-Universals].

4. **Higher capability/benchmark score does not guarantee lower cultural bias — and can worsen it.** Russia's ruRoBERTa-large tops Russian SuperGLUE yet is the most biased model tested [2024-Grigoreva-RuBia]; more Filipino pretraining data yields MORE bias (SEALION/RoBERTa-Tagalog most biased) [2025-Gamboa-Filipino Benchmarks]; in judicial sentencing, "as an LLM's accuracy increases, its bias also increases substantially" [2025-Hu-LLMs on Trial]; SpeciesismBench shows recognition ≠ condemnation (86% detect speciesism, 34% call it wrong) and capability does not close the evaluative gap [2025-Jotautaitė-Speciesism in AI].

5. **The dominant validity threat is confounding: bias ≠ incapacity ≠ cultural disagreement.** MBBQ's core move is a parallel control set (swap group for neutral names) so bias is interpreted only where competence is established [2024-Neplenbroek-MBBQ]; Bangla results may reflect Claude's comprehension gaps not gender bias [2024-Sadhu-Social Bias]; Agarwal cannot tell whether low Hindi/Swahili scores are ethical-reasoning failure or "appropriate cultural disagreement with the English-defined ideal" [2024-Agarwal].

6. **"Whose values are correct" is answerable empirically by distribution-matching, not expert fiat.** KorNAT scores a model by the survey probability mass on its chosen option (SVA), with an empirical ceiling of only 0.450 reflecting genuine within-population disagreement, plus a reported All-Neutral baseline [2024-Lee-KorNAT]; MULTITP uses a 6-D L2 distance to Moral Machine human preferences over 40M responses [2024-Jin-Multilingual Trolley]; disagreement is signal — preserving all annotator ratings gave 53% greater toxicity reduction than majority vote [2025-Sorensen-Operationalizing Pluralistic Values].

7. **Morphology and gender-marking are load-bearing design variables, not incidental.** Spanish gender inflects nouns/articles/adjectives, forcing a from-scratch template corpus [2023-Plaza-del-Arco-MarIA/BETO]; Russian grammatical gender permeates verbs, enabling probes invisible in English [2024-Grigoreva-RuBia]; conversely gender-neutral-pronoun languages (Bangla, Filipino) give clean probing platforms once gender is re-encoded lexically (lalaki/babae) [2024-Sadhu; 2025-Gamboa].

8. **Machine translation of value items is a documented, quantifiable validity flaw.** Yang flags Google-Translate-only labels may "misalign with human perception" [2024-Yang]; ÓhÉigeartaigh documents a translation error recasting China's "leading center" as "domination," distorting perceived intent [2025-ÓhÉigeartaigh]; Histoires Morales' demonstration-based translation pipeline was preferred by 80% of annotators over plain cultural-adaptation prompting [2025-Leteno].

9. **IAA on culturally-loaded value labels is intrinsically low — and suppressing it is a mistake.** Reported κ/α: SBIC 0.45 [2020-Sap]; HateXplain 0.46 [2020-Mathew]; OffendES 0.36 [2021-Plaza-del-Arco-OffendES]; HOMO-LAT 0.12–0.16 [2025-Enguix]; MFWC 0.45–0.92 by topic [2024-Cao]. Multiple sources warn that "resolving disagreements excessively can artificially inflate reliability, masking inherent subjectivity" [2024-Zangari; 2024-Cao].

10. **Current non-English moral/values benchmarks are far from saturation.** CMoralEval: most of 26 Chinese LLMs hover near random 0.33 [2025-Yu-CMoralEval]; KorNAT SVA ceiling 0.450 with best model 0.331 [2024-Lee]; MULTITP: only 3/19 models below 0.6 misalignment (max 2.45) [2024-Jin]; MFTCXplain: hate F1 up to 0.836 but moral-sentiment F1 typically <0.35 [2025-Trager].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2019-De-Arteaga-Bias in Bios | TPR-gap × base-rate correlation (r=0.85) as a single aggregate subgroup-bias score; counterfactual label-flip rate. |
| 2020-Mathew-HateXplain | Same-item scoring on correctness + group-fairness + explanation (plausibility/faithfulness); axes dissociate. |
| 2020-Sap-Social Bias Frames | Structured pragmatic frame (offense+intent+group+free-text implied stereotype) beats binary toxicity. |
| 2021-Barikeri-REDDITBIAS | Couple bias metric with downstream capability metric in one run to catch "alignment tax." |
| 2021-Plaza-del-Arco-OffendES | NOE "non-offensive expletive" class separates normative swearing from real offense. |
| 2022-Das-Hate Speech | Parallel Unicode + Romanized script sets; zero-shot cross-script drops F1 0.80→0.39. |
| 2022-Röttger-Multilingual HateCheck | 34 functional tests × contrastive non-hate pairs, per-function accuracy, template coverage-equity across 10 langs. |
| 2023-Catapang-EMoTES-3K | Bilingual parallel moral corpus + mixed-intent (action vs intent valence) hard probe. |
| 2023-Hopp-Dutch MFV/SMID | Cross-cultural re-validation of moral stimuli against US/AU human baselines; circumplex image sampling. |
| 2023-Plaza-del-Arco-MarIA/BETO | Redesign templates from scratch for morphological gender; dual probability+rank metrics. |
| 2024-Ashraf-Arabic Safety | Dual-perspective (government/opposition) scoring; direct/indirect/harmless triplet; Arabic 25–56% harm. |
| 2024-Chiu-DailyDilemmas | Value-bundle action labels; audit models vs their own published principle docs (ModelSpec/CAI). |
| 2024-Grigoreva-RuBia | Morphological grammatical-gender pairs; SuperGLUE-best model is most biased. |
| 2024-Jin-Multilingual Trolley | 98,440 procedurally-generated items × 107 langs; L2 misalignment vs 40M Moral Machine responses. |
| 2024-Lee-KorNAT | Distribution-as-ground-truth scoring (SVA) with empirical ceiling + All-Neutral baseline. |
| 2024-Neplenbroek-MBBQ | Parallel control set + cross-lingual common-denominator stereotypes isolate model inconsistency. |
| 2024-Sadhu-Social Bias (Bangla) | Gender-neutral-pronoun language as clean probe; template probing > naturalistic reveals guardrail gap. |
| 2024-Simpson-Parity | Knowledge vs reasoning difficulty tiers; knowledge→reasoning accuracy DROP as the discriminator. |
| 2024-Tonneau-Turkish HS | Iterative 10→5-level severity taxonomy; annotator hate-rate variance 0.42–0.90. |
| 2024-Yang-Multilingual Toxicity | Resource-tier stratification; FPR alongside F1; in-context policy ablation lifts detection. |
| 2025-Ajwad Abrar-Religious Bias | Cross-domain intersection probes (gender/age/nationality × religion); before/after debiasing table. |
| 2025-Bauer-Dutch Fairness | Grammar-aware SGT lists (adj+noun); rule-based counterfactuals beat LLM-generated on fairness. |
| 2025-Chen-MoVa | all@once multilabel prompting exploits label dependency; generalization taxonomy (in/new-domain/framework). |
| 2025-Enguix-HOMO-LAT | Cross-dialect train/test track (Track 2); κ=0.12–0.16 shows subjectivity; MPA/CFD ensemble metrics. |
| 2025-Gamboa-Filipino | Cultural-adaptation issue taxonomy as checklist; more in-language data → more bias. |
| 2025-Hu-LLMs on Trial | Counterfactual-per-query (not in-context); accuracy↑→bias↑; Bernoulli test for many-label FDR. |
| 2025-Jiao-LLM Ethics | Dual-method validation (philosopher review + psychometric anchoring); down-weight coherence to avoid glibness. |
| 2025-Jotautaitė-Speciesism | Two separate axes: recognition vs moral evaluation; subtlety-calibrated items; capacity-orthogonal probe. |
| 2025-LLMs-Leaderboard | Oracle-per-template + counterfactual-consistency oracle; radical transparency; descriptive-vs-normative dilemma. |
| 2025-Leteno-Histoires Morales | Parallel EN/FR probes language effect; 84 DPO examples flip moral alignment direction. |
| 2025-Marcuzzo-MORABLES | Typed distractors mapped to failure modes; NOTO + consistency metric surfaces ~20% self-refutation. |
| 2025-Park-KOGENT | Label positive/inclusive language too, not just harm; diachronic annotator calibration. |
| 2025-Salles-HateBRXplain | Human rationale spans + ERASER faithfulness; best classifier ≠ most faithfully explainable. |
| 2025-Singh-IndoHateMix | Code-mixed regional-platform corpus; 10%-data LoRA LLM beats full-data specialist BERT. |
| 2025-Trager-MFTCXplain | Multi-hop hate→moral-foundation→rationale; virtue/vice as independent labels; report human ceilings. |
| 2025-Yu-CMoralEval | Neutral "third option" distractor + explicit-vs-dilemma tiers; principles above social norms (RoTs). |
| 2026-He-GVS-Bench | Incident-grounded taxonomy; 3-tier normativity (baseline safety / universal / pluralistic); per-item Evaluation Focus. |
| 2022-Unknown-HOTTEST (Tamil) | Language-specific stemming as a prerequisite for valid agglutinative-language detection. |
| 2024-Maity-HateThaiSent | Dual-label (hate + sentiment) annotation; sentiment signal improves hate detection. |
| 2025-Firmino-CrossLingual | Transfer-degradation source→target as a quantitative coverage-gap metric. |
| 2020-Awad-Universals | Funnel plots separate sampling noise from genuine cultural signal; qualitative-ordering universality claim. |
| 2022-English-Kurdish HS | Bahador 6-level intensity scale; harm FORM varies cross-culturally (dehumanization vs name-calling). |
| 2022-Sahoo-ToxicBias | Social-bias≠hate-speech distinction; free-text implication annotation; counter-narrative augmentation. |
| 2023-Ibrohim-Indonesian HS | Hierarchical target+category+level schema validated via FGD with cybercrime police. |
| 2024-Agarwal-Ethical Reasoning | Policy-in-prompt architecture; bias/confusion decomposition; multilingual moral drift measurement. |
| 2024-Cao-MFW Corpus | Weibo moderation as natural variable; PABAK alongside κ for imbalanced moral labels. |
| 2024-Matei-Romanian | Multi-task knowledge distillation + teacher annealing for low-resource classifier bootstrapping. |
| 2024-Rane-Concept Alignment | Concept alignment precedes value alignment; prototype-theory difficulty calibration; cross-modal consistency. |
| 2024-University-Antisemitism | Continual cluster-splitting tracks evolving coded language; temporal validity as streaming task. |
| 2024-Zangari-MFT survey | Political-identity prompting as sensitivity probe; entropy-based noisy-annotation removal. |
| 2025-Bhattacharjee-Religious Texts | Corpus-embedding distance (FID/cosine) as proxy for theological/normative-family distance. |
| 2025-Graves-Practical Wisdom | 7-category suffering-recognition benchmark grounded in 4 ethical traditions to avoid WEIRD bias. |
| 2025-Kajiwara-INHS | Cross-disciplinary/low-resource dataset surveillance (Sinhala, Japanese, Hindi-English) for coverage. |
| 2025-Mohammadi-Cultural Variations | WEIRD/non-WEIRD regional stratification mandatory; 5-adjective-pair averaging for stable probes. |
| 2025-Sorensen-Pluralistic Values | Disagreement-preserving training beats majority vote; scale granularity is a measurable lever. |
| 2025-Wang-Diverse Value Alignment | Hierarchical norm priority (legal>policy>social>cultural); decouple norm-ID from response-alignment metrics. |
| 2025-ÓhÉigeartaigh-Cross-cultural | Incompletely-theorized agreements: score responses endorsable from multiple traditions, not one answer. |
| Microsoft Research-Phi-3 | Break-fix cycle; dual IPRR+VPRR; English safety fails to transfer; multi-turn role-play breaks all langs. |
| 2025-AbuMusab-Islamic AI | Religious frameworks generate novel AI ontological categories ("neutragents") to probe. |
| 2025-Perera-Indigenous AI | CARE/OCAP data-sovereignty principles as rubric dimensions; Māori health-model bias case. |
| 2022-Joshi-L3Cube-Marathi | Monolingual models beat multilingual on the target language — argues for language-specific resources. |

## C. Patterns & disagreements

**Convergence.** (i) Nearly every empirical card confirms the English→non-English transfer gap [Ashraf; Yang; Agarwal; Leteno; Das; Phi-3]. (ii) Multiple independent cards find capability and cultural-bias are decoupled or inversely related [Grigoreva; Gamboa; Hu; Jotautaitė]. (iii) A strong methodological consensus emerges that bias measurement must be separated from competence measurement [Neplenbroek; Sadhu; Agarwal] and that per-category/per-language reporting must replace single aggregate scores [Neplenbroek; Yang; Grigoreva]. (iv) Repeated endorsement of counterfactual/minimal-pair design [De-Arteaga; Grigoreva; Bauer; Hu; LLMs-Leaderboard; MBBQ].

**Disagreement 1 — build specialized detectors vs. curate diverse data for general LLMs.** Singh argues LLMs should *replace* specialized BERT detectors (10%-data LoRA beats full-data mBERT) [2025-Singh]; the low-resource-classifier tradition (Matei's MTKD, Joshi's MahaBERT, HOTTEST's stemming) still invests in specialized monolingual systems [2024-Matei; 2022-Joshi; 2022-HOTTEST]. Bauer complicates Singh: LLM-generated counterfactuals were *more grammatical yet produced worse fairness* than rule-based ones [2025-Bauer].

**Disagreement 2 — template vs. naturalistic probing.** Sadhu finds template probing reveals *stronger* bias (guardrails suppress it in natural contexts) and treats templates as the truer signal [2024-Sadhu]; Barikeri deliberately grounds items in real scraped conversation because templates miss naturally-occurring bias [2021-Barikeri]. These are reconcilable as measuring different constructs (latent disposition vs. deployed behavior) but the cards do not agree on which is "the" bias.

**Disagreement 3 — is the ground truth a distribution, a majority, or an expert answer?** KorNAT/MULTITP/Sorensen say match the population distribution and preserve disagreement [2024-Lee; 2024-Jin; 2025-Sorensen]; Röttger's Multilingual HateCheck uses *prescriptive* gold labels annotators must follow, treating disagreement as annotator error [2022-Röttger]; Parity and Jiao use expert-authored single correct answers [2024-Simpson; 2025-Jiao]. Simpson's "score refusal/non-commitment as 0" directly contradicts KorNAT's "treat refusal as a first-class outcome" [2024-Simpson vs 2024-Lee].

**Disagreement 4 — descriptive vs. normative target.** The LangBiTe leaderboard surfaces this explicitly ("reflect the real world or a desired world?") [2025-LLMs-Leaderboard]; Jin warns matching human averages may ratify harmful biases [2024-Jin]; GVS-Bench's 3-tier scheme is one attempt to resolve it (strict on baseline safety, pluralistic only at the top tier) [2026-He].

## D. Exemplars & anti-patterns

**Best-designed.** **KorNAT** [2024-Lee] is the standout: survey-grounded distribution scoring, demographic re-weighting to census, distractor+consistency screening of respondents, reported empirical ceiling and naive baseline, refusal as first-class, LLM-free construction of the factual half, and a passed government data-quality audit. **Multilingual HateCheck** [2022-Röttger] is exemplary for functional-test structure: contrastive hate/non-hate pairs, template coverage-equity across protected groups, per-function accuracy exposing failures (counter-speech at 9.6%) that aggregate F1 hides. **MBBQ** [2024-Neplenbroek] is the cleanest validity design via its parallel control set and cross-lingual common-denominator stereotypes. **MULTITP** [2024-Jin] and **JudiFair** [2025-Hu] model rigorous scale + statistics (procedural generation for contamination resistance; fixed-effect regression with document controls, Bernoulli FDR correction).

**Anti-patterns.** **HOMO-LAT** [2025-Enguix] ships with Fleiss κ=0.12–0.16 and used Mexican annotators for 15 of 19 countries, injecting systematic cultural bias into the very cross-dialect test set it is meant to evaluate. **The English-Kurdish study** [2022-English] draws cross-cultural conclusions from n=30 comments across mismatched outlets (Fox vs Rudaw) with no IAA. **Parity** [2024-Simpson] scores appropriate refusal/epistemic humility as 0 and encodes contested socio-political stances as sole "correct" answers, conflating factual knowledge with a specific normative position. The thin/low-confidence cards (HOTTEST, HateThaiSent, Firmino, Muñoz-García) report headline accuracy numbers with no accessible provenance — a reminder that a benchmark's design is only as trustworthy as its documented construction.

## E. Design lessons

1. **Never report a single aggregate bias/values score.** Report per-language, per-category, and per-subgroup [2024-Neplenbroek; 2024-Yang; 2024-Grigoreva]; add resource-tier stratification (high/med/low) to turn "multilingual" into a graded generalization curve [2024-Yang], and mandatory WEIRD/non-WEIRD regional splits [2025-Mohammadi].

2. **Separate bias from competence with a parallel control set.** Swap the sensitive group for neutral names/tokens, establish task competence first, and interpret bias only where competence holds [2024-Neplenbroek; 2019-De-Arteaga]; otherwise low-resource extraction failure masquerades as bias [2024-Sadhu].

3. **Ground truth for contested values should be a population distribution with a reported ceiling and baseline.** Score by survey probability mass on the chosen option, re-weight the sample to census, screen respondents with distractor+consistency traps, and report the empirical max-achievable score and a naive baseline [2024-Lee; 2024-Jin]. Preserve annotator disagreement rather than majority-voting it away — it improves downstream alignment [2025-Sorensen; 2024-Cao; 2024-Zangari].

4. **Treat cultural adaptation as first-class methodology, not translation.** Author or expert-review items natively per language; machine translation is a documented validity flaw [2024-Yang; 2025-ÓhÉigeartaigh]. Use a checklist of adaptation issues — names, customs, idioms, untranslatable/foreign stereotypes, morphological gender, indigenous identity ontologies [2025-Gamboa; 2025-Bauer]. Localize the identity taxonomy (bakla/bading, Moroccan-in-NL) rather than force-fit Western labels [2025-Gamboa; 2025-Bauer]. Demonstration-based translation is measurably preferred [2025-Leteno].

5. **Engineer items so surface features and the tested value dissociate.** Contrastive minimal pairs (hate-with-profanity vs non-hate-profanity) [2022-Röttger]; typed distractors mapped to specific failure modes [2025-Marcuzzo]; mixed action-vs-intent valence [2023-Catapang]; a morality-neutral third option to kill guessing [2025-Yu]; counterfactual-per-query not in-context to remove anchoring [2025-Hu].

6. **Score reasoning and refusal, not just the answer.** Add a knowledge→reasoning tier drop as the real discriminator [2024-Simpson]; collect human rationale spans and score plausibility + ERASER faithfulness so right-answer-wrong-reason is penalized [2020-Mathew; 2025-Salles; 2025-Trager]; report a self-consistency/self-refutation metric (NOTO) [2025-Marcuzzo]; treat refusal as a first-class outcome rather than auto-scoring it 0 [2024-Lee vs 2024-Simpson].

7. **Include the full behavior surface: false positives, positive/inclusive language, and severity gradations.** Always report a false-positive/over-refusal metric alongside detection (IPRR+VPRR / FPR+F1) [Microsoft-Phi-3; 2024-Yang]; label affirming/inclusive language, not only harm [2025-Park]; use graded severity scales (5-level, Bahador 6-level) but note that a coarser scale often reliabilizes better [2024-Tonneau; 2022-English].

8. **Build in contamination and temporal robustness.** Procedurally generate items on-demand to resist training-set leakage [2024-Jin]; add adversarial variants (tautology injection, character swap, multilingual AutoDAN, multi-turn role-play) since English safety and static benchmarks both break under shift [2025-Marcuzzo; 2024-Yang; Microsoft-Phi-3]; plan for evolving coded language via streaming re-validation [2024-University].

9. **Exploit language structure deliberately.** Redesign templates from scratch for morphological gender [2023-Plaza-del-Arco-MarIA; 2024-Grigoreva]; use gender-neutral-pronoun languages as clean probing platforms with lexical gender re-encoding [2024-Sadhu; 2025-Gamboa]; apply language-appropriate preprocessing for agglutinative scripts [2022-HOTTEST].

10. **Adopt a tiered normativity model for aggregation, and audit against stated principles.** Separate non-negotiable baseline safety (score strictly) from context-dependent pluralistic values (allow diversity) [2026-He]; use incompletely-theorized-agreement scoring that rewards responses endorsable from multiple ethical traditions rather than one gold answer [2025-ÓhÉigeartaigh; 2025-Graves]; apply hierarchical norm priority (legal>policy>social>cultural) for conflicts [2025-Wang]; audit models against their own published principle docs [2024-Chiu].
