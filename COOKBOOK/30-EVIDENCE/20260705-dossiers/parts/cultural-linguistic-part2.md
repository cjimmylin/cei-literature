# cultural-linguistic — sub-dossier part 2/6

Scope: 63 cards — non-English toxicity/hate corpora, cross-cultural value benchmarks (Hofstede VSM, WVS/PEW, Moral Machine), multilingual safety/jailbreak evals, morphology/dialect bias tests, and normative papers (Ubuntu, Confucian, decolonial, Afro-relational).

## A. Synthesized claims

1. **Safety/alignment is not language-invariant; cross-language *consistency* is far worse than any per-language score suggests.** M-ALERT: no model reaches 99% safe across 5 languages; Aya-23 shows only 44.74% inter-language exact-match; Llama-3 crime_tax EN 100% vs IT 67.7% (p.5,7) [2024-Friedrich-M-ALERT]. GlobalOpinionQA: defaults resemble USA/Western; model assigns 1.35% to "strong economy" vs 83.08% of Russians (p.6) [2023-Durmus]. EvalMORAAL: Western r=0.82 vs non-Western r=0.61, a 21-point gap (p.5) [2025-Mohammadi-EvalMORAAL].

2. **Reasoning language dominates input language for cross-lingual moral instability (~2×).** Reasoning-language changes produce 7.16pp YTA shifts vs 3.46pp for input on AITA (2.07×); 44% of models show hidden context-dependency invisible to single-dataset eval (p.6) [2025-Li-Untangling]. Multilingual moral verdicts flip across languages [2025-Farid; 2024-Vida].

3. **Cross-cultural alignment tracks training-data availability, not scale.** Sukiennik: web-content-%-per-country correlates with alignment r=0.94, GDP r=0.81, but log model size only r=0.13; GLM-4 (9B) aligns best despite near-lowest size (p.7-8) [2025-Sukiennik]. Language-specific pretraining beats multilingual: FinBERT 91.7% vs mBERT 88.2% [2022-Jahan]; ParsBERT F1 0.854 vs RoBERTa 0.71 [2025-Jafarinejad-PerGOLD; 2025-Unknown-survey].

4. **LLMs collapse cultural diversity toward a "global average" matching no real population.** Sukiennik's deviation-ratio exists because raw distance rewards models near the average; US ratio 1.99 vs Bangladesh 0.59 (p.6) [2025-Sukiennik]. Benkler: text-davinci-003 explains US WVS R²=0.80 but Japan 0.08, Nigeria 0.01, distributions more concentrated than human IQRs (p.6) [2023-Benkler]. Young demographics (<29) under-represented across all models [2025-Liu-Cross-cultural].

5. **Translation alone is insufficient and often invalid; native/expert authoring is required.** GG-BBQ: naive NLLB MT destroys BBQ's gender-neutrality, forcing 15h correction and 50→167 template expansion (p.3-4) [2025-Satheesh-GG-BBQ]. SHADES was built from scratch by 43 native speakers with geographic-validity tags [2025-Al-SHADES]; ELAB's t-SNE shows translated ≠ native distributions [2025-Pourbahman-ELAB]. KoSBI: classifiers from 5 Korean HS datasets score only 40-53% on it—a different construct (p.5) [2023-Lee-KoSBI].

6. **Culturally-specific bias axes exceed the Western axes debiasing targets, and are missed by English benchmarks.** Indian-BhED: Indian-centric bias 69.5% vs US-centric 52.8%; GPT-3.5 caste 79.52% (p.7-8) [2024-Khandelwal]. Locally-salient: Korean military-service [2020-Moon-BEEP!], region/marital-status [2023-Lee-KoSBI], Chinese subculture/worldview [2025-Lan-McBE]; Turkish embeddings 87% masculine [2024-Altinok].

7. **The label-validity ceiling, not model capacity, caps these benchmarks.** Re-moderating 350 disagreements, ~half of blocked comments flipped and 81/124 got a different rule (p.19) [2020-Shekhar]. ToxiFrench derives a ~90% human ceiling, saturating at ~85% (p.5) [2025-Delaville]. IAA is modest: ViHSD kappa 0.52 [2021-Luu], BEEP! 0.49 ternary vs 0.767 gender-binary [2020-Moon-BEEP!], KoSBI sentence α=0.256 [2023-Lee-KoSBI].

8. **Refusal is a culturally-uneven signal—both a stigmatization marker and a language-biased failure.** Llama2-13b refuses 55.61% of Jewish and 31.75% of Muslim personas while GPT-4o refuses 0% (p.4) [2024-Hovy]. JAILJUDGE: judges show higher bias in low-resource languages; distilled 7B guard drops to F1 0.4505 on multilingual OOD (p.8-9) [2024-Liu-JAILJUDGE]. Debiasing transfer from English degrades non-English *language consistency*, harming targeted speakers (p.2,9) [2025-Neplenbroek].

9. **Demographic/persona conditioning is a valid lever—with cautions.** IndoToxic2024 preserves per-annotator labels; persona injection improves GPT-3.5 zero-shot (+0.47 macro-F1) but fragments fine-tuning data, hurting IndoBERTweet (p.6-8) [2024-Susanto]. Durmus: cross-national prompting shifts toward the target country but stereotypes; linguistic prompting does *not* shift toward that language's speakers (p.5-6) [2023-Durmus].

10. **Non-Western frameworks (Ubuntu, Confucian, Afro-relational, decolonial/viśeṣa-dharma) are named alternatives to the individual-autonomy default—but mostly un-operationalized.** Only 1/5 African national strategies (Benin) references Ubuntu, vaguely; its content is "too vague" to encode [2025-Yilma], echoing three-register (virtue/procedure/outcome) [2022-Gwagwa] and humanity/spirituality/environment framings [2024-Mokoena]. Afro-relational trust is bidirectional/communal, not Western reliability (Yoruba "gbekele"=dependability) [2025-Amugongo]. Varshney's sādharaṇa vs viśeṣa harm taxonomy notes context-specific harms "do not have existing benchmarks" (p.14) [2024-Varshney].

11. **Structured, culturally-grounded supervision can beat scale.** MedES: aligned 7B composite 0.9356 vs deepseek-r1-671B 0.8103 (>10% gain), grounded in 1,278 atomic rules from 260 Chinese documents (p.6) [2026-Jin-MedES]. eJCM: RoBERTa on 31K sentences closes to within 3.1 F1 of GPT-4-Turbo on Japan-specific items (p.4) [2024-Ohashi]. Domain ethics fine-tuning lifts Chinese healthcare 42.7%→50.8% (p.1) [2025-Bian].

12. **Saturated single-sentence benchmarks can be revived by raising cognitive load, not inventing topics.** GPT-4o/Claude-3.5 score 97.4/98.6 on CValues; 3-turn manipulation/story rewrites restore spread (Claude 83.7 → Yi-Large 42.5) (p.4,14) [2025-Zhang]. MedEthicEval's mass-balance taxonomy scores per difficulty regime; "post-hoc justification" attacks erode ethics most (p.7) [2025-Jin-MedEthicEval].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2018-Dixon | Template minimal-pairs isolate identity-term bias; "pinned AUC" catches disparity that per-group AUC misses (p.4). |
| 2019-Ibrohim | Two-phase annotation (cheap binary → expert fine-grained on positives) + police-grounded severity tiers (p.5). |
| 2020-Moon-BEEP! | Co-annotate bias AND hate; culturally-specific categories (military-service); binary-gender IAA 0.767 vs ternary 0.49 (p.3). |
| 2020-Shekhar | Re-annotation audit: ~half of "blocked" comments flip on re-moderation—label-validity is the ceiling (p.19). |
| 2021-Luu-ViHSD | Three-tier CLEAN/OFFENSIVE(untargeted)/HATE(targeted); teencode/slang breaks mBERT; kappa 0.52 (p.4-9). |
| 2021-Taulé-DETOXIS | CEM ordinal metric (non-equidistant, up-weights rare severe classes) + 13 auxiliary features for error analysis (p.4). |
| 2022-Jahan | Language-specific FinBERT beats mBERT by 3.5-5pp; α=0.92 via 2-annotator+expert-referee (p.3-5). |
| 2022-Vargas-HateBR | 3-layer hierarchy (binary→severity→9 hate groups incl. fatphobia); PhD annotators diverse by politics/race/region (p.3). |
| 2023-Durmus | JSD between model and country survey distributions; default=WEIRD; language ≠ culture in prompting (p.5). |
| 2023-Lee-KoSBI | Human-rights-law demographic framing (72 groups); context-conditioned safety labels; ambiguity-based item selection (p.3). |
| 2023-Soemer | Mandatory clause-citation of the IHRA definition + recorded personal disagreement separates "standard says" from "I believe" (p.3). |
| 2024-Bajaj-GenMO | Gender-swapped minimal-pair stories; all models favor female protagonists (FBR 63-88%); "Can't Say" captures hedging (p.8). |
| 2024-Friedrich-M-ALERT | Inter-language exact-match metric: 97% per-language safety can hide 44% cross-language consistency (p.7). |
| 2024-Hovy | Refusal rate as a stigmatization metric across religion personas (Jewish 55.6% vs GPT-4o 0%) (p.4). |
| 2024-Khandelwal | Pair a new non-Western bias set with an existing Western one (CrowS-Pairs) under identical method for direct comparison (p.7). |
| 2024-Liu-JAILJUDGE | Dempster-Shafer aggregation of multiple judge scores; multilingual OOD split surfaces low-resource judge bias (p.6-8). |
| 2024-Ohashi-eJCM | MTLE augmentation masks the moral-contrast clause; Japan-specific 244-item stress subset exposes GPT-4 (p.3-4). |
| 2024-Sahoo-IndicCONAN | CN-type conditioning (fact-based, denouncing…) forces functional diversity in generated normative responses (p.5). |
| 2024-Susanto | Preserve per-annotator labels; persona injection helps zero-shot but fragments fine-tuning data (p.6-8). |
| 2024-Vida | Moral Machine (2.3M humans) as human-baselined cross-cultural probe; language inconsistency = validity threat (p.9). |
| 2024-Z.Delbari-PHATE | Controversial/ambiguous keywords (not slurs) avoid trivially-easy items; rationale spans + masking validity test (p.3,8). |
| 2025-Al-SHADES | Native speakers write + geographic-validity-tag stereotypes; morphology-aware templates (`<GENDER:MASC>`) (p.5-6). |
| 2025-Bian | 20-dimension ethics×safety taxonomy grounded in a national policy (Healthy China 2030); fairness stuck ~60% (p.4). |
| 2025-Delaville-ToxiFrench | High-confidence auto-label (trust LLM negatives at score≤3) cuts human labeling to 10%; ~90% human ceiling (p.5). |
| 2025-Farid | Parallel-translate ETHICS/MoralExceptQA into 6 langs; FAULT typology; report compliance rate alongside accuracy (p.3-9). |
| 2025-Gupta-EnDive | Hold semantics constant, vary sociolect; BLEU≥0.7 filter drops near-identical items to raise discrimination (p.4). |
| 2025-Jafarinejad-PerGOLD | Event-based collection (14-day post-event windows) naturally raises positive-class density; but no kappa reported (p.5-7). |
| 2025-Jin-MedEthicEval | Mass-balance taxonomy: violation-detection vs priority- vs equilibrium-dilemma, each scored differently (p.2). |
| 2025-Kumar-UNIMORAL | Ground truth = the annotator's own choice given their MFQ2/Hofstede profile → steerability/persona test (p.6). |
| 2025-Lan-McBE | Five-task battery separates intrinsic-preference (likelihood) from comprehension probes; "bigger=more biased" is a task artifact (p.9). |
| 2025-Li-Untangling | 2×2 factorial (input × reasoning language) decomposes cross-lingual instability; reasoning language dominates 2× (p.6). |
| 2025-Mohammadi-EvalMORAAL | Direct-CoT scoring beats log-prob by Δr≈0.098; LLM-as-judge peer review (no self-judging) correlates r=0.74 with WVS (p.5-7). |
| 2025-Pourbahman-ELAB | Three-way provenance (translated+synthetic+collected) + culture-specific judge prompts (taarof/aberoo) (p.6). |
| 2025-Satheesh-GG-BBQ | Raw MT destroys gender-neutrality; ambiguous-context "No answer" tests over-commitment to stereotypes (p.4). |
| 2025-Sukiennik | Deviation-ratio metric corrects global-average bias; alignment tracks web-data (r=0.94) not scale (r=0.13) (p.6-8). |
| 2025-Weber | Composite recall-weighted score S=(MCC_norm+F2)/2; LLM-assisted re-annotation lifts scores ~10-17% but risks bias (p.6-9). |
| 2025-Zhang-CValuesPlus | Cognitive-Load-Theory rewrite (single sentence → 3-turn manipulation/story) revives a saturated benchmark (p.4,14). |
| 2026-Jin-MedES | 1,278 atomic rules from 260 authoritative docs both generate items and score compliance; aligned 7B > 671B (p.1-6). |
| 2023-Maity-Ex-ThaiHate | Rationale-span + multi-task generative framing (label+sentiment+emotion+rationale in one pass) [low-confidence card]. |
| 2024-Schmeisser-DETESTS-Dis | "Learning with disagreement": retain annotator distribution rather than force consensus [low-confidence card]. |
| 2025-Group-AILuminate | Systematic language extension (EN→FR v1.1) of an industry safety benchmark; changelog-versioned [low-confidence card]. |
| 2018-Crone-SMID | Rate every item on all 8 moral dimensions (not one category); political-balance rater requirement; uniqueness scores. |
| 2020-Kurpicz-Briki | Culture-adapted WEAT word lists (Swiss enrolment stats, 18th-c. vocab); math/science gender bias absent in de/fr (p.9). |
| 2022-Gwagwa | Three-register (virtue/procedure/outcome) analysis of Ubuntu; uncounted/unaccounted/discounted data-exclusion taxonomy. |
| 2023-Benkler | RVR entailment model scores resonance vs WVS statements; WEIRD bias; distributions too concentrated (p.6). |
| 2023-Rystrøm | Calibration-as-uncertainty test: does model entropy track population controversy? Delphi's does not (p.5). |
| 2024-Altinok | Morphology-aware bias: Turkish suffixes flip gender association; 87% masculine vocab across web/academic/medical (p.4). |
| 2024-Elrod | Creative-completion probes (write 5 missing commandments / lost Jonah ch.5) elicit theological bias direct Qs miss. |
| 2024-Mokoena | Tripartite Ubuntu (humanity/spirituality/environment) extends beyond anthropocentric individual-rights framing. |
| 2024-So-Confucian | Non-Western virtue ethics (ren/xiao/li/yi) as an alignment grounding; aphorism-as-soft-constraint (speculative). |
| 2024-Varshney | sādharaṇa (universal) vs viśeṣa (context-specific) harm taxonomy; context-specific harms lack benchmarks (p.14). |
| 2025-Amugongo | Afro-relational trust is bidirectional/communal; construct-translation of "trust" fails across African languages (p.2). |
| 2025-Davies | Counterfactual-demographic prompt ("would this be recommended if attribute differed?") as fairness judge; ratio metric. |
| 2025-Iftikhar | Practitioner-grounded 15-violation taxonomy mapped to APA/ACA/NASW codes; crisis-navigation as mandatory eval domain. |
| 2025-Liu-Cross-cultural | Distributional fidelity (KL-D vs WVS) is distinct from consistency/accuracy; FFT preserves diversity better than RLHF. |
| 2025-Neplenbroek | Track language-consistency before any bias measure; debias-transfer degrades non-English generation (p.2,9). |
| 2025-Unknown-survey | Absence of a unified hate/offensive definition inflates annotation subjectivity → biased models; multilingual vs cross-lingual axis. |
| 2025-Yilma | Ubuntu is southern-African, not pan-African, and too vague to operationalize; only 1/5 strategies references it (p.2). |
| 2026-Nadeem-Bias-Beyond-Borders | Cross-Lingual Alignment Steering into a shared subspace; axis-stratified (economic/social) bias reporting (p.2,7). |
| Zhipu-AlignBench | Rule-calibrated, reference-anchored (8/10) LLM-judge; judge reliable at system level (Pearson 0.998) not sample (0.638). |
| 2024-J.K.Lee-KcBERT | tf-idf imbalance predicts LPBS/CBS direction; fine-tuning on offensive data can *increase* some biases (racial CBS 0.14→0.52). |
| 2025-Han-HKGAI-V1 | "Safe" operationally = compliant with PRC/HK law—benchmark encodes a contested political stance; opposing safe/unsafe framings. |
| 2025-Sharmaa | Partial (word-level) transliteration preserves code-switched syntax; profanity-vs-hate decoupling [mislabeled Somali; is Hinglish]. |

## C. Patterns & disagreements

**Convergence.** (i) *WEIRD/Western default* is the most replicated finding—survey-JSD [2023-Durmus], WVS-Pearson gaps [2025-Mohammadi-EvalMORAAL; 2023-Benkler], Hofstede deviation ratios [2025-Sukiennik], caste/religion axes [2024-Khandelwal], normative critiques [2022-Gwagwa; 2024-Varshney; 2025-Yilma]. (ii) *Language-specific beats multilingual* for low-resource toxicity [2022-Jahan; 2025-Jafarinejad-PerGOLD; 2024-Z.Delbari]. (iii) *Translation is insufficient* [2025-Satheesh-GG-BBQ; 2025-Al-SHADES; 2023-Lee-KoSBI]. (iv) *Subjective constructs need disagreement handling*—per-annotator labels [2024-Susanto; 2024-Schmeisser-DETESTS-Dis], anti-majority-vote [2025-Delaville], or clause-anchored consensus [2023-Soemer].

**Disagreements.** (a) *Does scale help?* Sukiennik (size r=0.13) and Vida (Llama-3-70B worst RMSE 0.672) say no; Bajaj finds larger open models *more* biased [2024-Bajaj]; yet EvalMORAAL's best are frontier-scale and AlignBench shows a GPT-4-vs-rest gap. Resolution: scale aids capability, not cultural coverage (data-bound). (b) *"Bigger = more biased"?* McBE shows this is a task-artifact of likelihood/SS probes; comprehension probes reverse it [2025-Lan-McBE]—a caution against Bajaj-style single-metric claims. (c) *Aggregate vs distribution.* Mohammadi treats high average correlations as success; Sukiennik/Benkler/Liu argue averages *mask* diversity collapse, making KL-D a distinct axis [2025-Liu-Cross-cultural]. (d) *Kappa's validity.* Soemer argues kappa is invalid once consensus-discussion breaks independence [2023-Soemer]; most corpora still treat it as the gold stat [2021-Luu; 2022-Jahan]. (e) *Persona conditioning* helps zero-shot LLMs [2024-Susanto] yet Durmus warns it induces stereotyping and that linguistic prompting fails—persona-label ≠ language ≠ culture.

## D. Exemplars & anti-patterns

**Best-designed.** *SHADES*: from-scratch native authoring across 16 languages, geographic-validity tags separating universal from local stereotypes, morphology-aware templates, dual base/instruct paradigms, gated release [2025-Al-SHADES]. *MedES*: traceable atomic-rule grounding that generates and scores items, a six-dimension risk×quality rubric vetoing fluent-but-unsafe answers, cross-family annotator/evaluator assignment, continual updates [2026-Jin-MedES]. *Li-Untangling*'s 2×2 factorial cleanly decomposes a confounded comparison into an attributable, deployment-relevant taxonomy [2025-Li-Untangling]. *GlobalOpinionQA*: survey-grounded external validity, three-condition perturbation, public accountability infrastructure [2023-Durmus]. *ToxiFrench*: honest ~90% human-agreement ceiling checked against observed saturation [2025-Delaville].

**Anti-patterns.** *PerGOLD*: good event-based collection but **no IAA**, 4 taggers, undisclosed events—unreproducible [2025-Jafarinejad-PerGOLD]. *HKGAI-V1* defines "safe" as "compliant with PRC/HK laws," so scores measure ideological conformity, developer-self-evaluated on unreleased benchmarks with no IAA [2025-Han-HKGAI-V1]—a warning that targets can smuggle contested stances. *Naive-MT* benchmarks silently void the construct in gendered languages [2025-Satheesh-GG-BBQ]. *Self-generation contamination* recurs where items are generated by the evaluated model family [2025-Jin-MedEthicEval; 2025-Zhang]. Three cards (*Ex-ThaiHate*, *DETESTS-Dis*, *AILuminate*) are low-confidence/text-missing—leads, not evidence.

## E. Design lessons

1. **Report cross-language *consistency*, not just per-language scores.** Add an inter-language exact-match/flip metric; a model can be 97% aligned per language yet 44% consistent [2024-Friedrich-M-ALERT; 2025-Li-Untangling].
2. **Separate input from reasoning language.** Enforce and vary reasoning language independently; it drives ~2× the instability [2025-Li-Untangling].
3. **Author natively; never ship raw MT for value items.** Use native speakers + expert correction, tag geographic/linguistic validity per item [2025-Al-SHADES; 2025-Satheesh-GG-BBQ; 2023-Lee-KoSBI], and use morphology-aware slot templates for gendered/agglutinative languages [2024-Altinok].
4. **Anchor bias axes to local instruments, not imported taxonomies.** Ground categories in human-rights law [2023-Lee-KoSBI], national policy [2025-Bian], protected-group statutes [2025-Lan-McBE], or legal corpora [2026-Jin-MedES], and audit for locally-salient axes (caste, military service, region) [2024-Khandelwal; 2020-Moon-BEEP!].
5. **Report the label-validity ceiling and design against it.** Run a re-annotation audit of model-human disagreements [2020-Shekhar], derive a human-agreement ceiling and check saturation against it [2025-Delaville], and report both coarse and fine IAA [2020-Moon-BEEP!].
6. **Measure distributional fidelity, not just modal accuracy.** Score how well a model reproduces the *distribution* of human preferences (JSD/KL vs WVS/PEW), and correct for the global-average default with a deviation-ratio-style metric [2023-Durmus; 2025-Liu-Cross-cultural; 2025-Sukiennik].
7. **Preserve annotator identity and handle disagreement as signal.** Keep per-annotator labels + demographic metadata for subjectivity/persona analysis [2024-Susanto], consider learning-with-disagreement [2024-Schmeisser-DETESTS-Dis], and where a rubric exists, force clause-citation while recording personal disagreement [2023-Soemer].
8. **Use minimal-pair/counterfactual designs plus a difficulty filter.** Swap only identity/gender/dialect/demographic while holding semantics constant [2018-Dixon; 2024-Bajaj; 2025-Gupta-EnDive; 2025-Davies]; drop near-identical/easy items (BLEU≥0.7, drop-easiest-50%) to preserve discrimination [2025-Gupta-EnDive; Zhipu-AlignBench]. Include a "Can't Say"/abstention option and ambiguous-context items to probe stereotype over-commitment [2025-Satheesh-GG-BBQ; 2024-Bajaj].
9. **Calibrate LLM judges; trust them at system level, not item level.** Rule-calibrate/reference-anchor to fight inflation, evaluate judge *explanations* separately [Zhipu-AlignBench; 2024-Liu-JAILJUDGE], use cross-family annotator/evaluator assignment [2026-Jin-MedES], and report judge-vs-human agreement and language-adherence effects [2025-Pourbahman-ELAB].
10. **Refresh saturated benchmarks by raising contextual load.** Convert single-sentence probes into multi-turn manipulation/narrative traps [2025-Zhang] and add attack-prompt transformations (post-hoc justification, role-play) [2025-Jin-MedEthicEval].
11. **Track collateral harms of alignment.** Measure language-consistency/fluency/diversity after any intervention—English transfer makes models switch language on non-English users [2025-Neplenbroek]; tf-idf imbalance predicts bias direction and over-correction [2024-J.K.Lee-KcBERT].
12. **Prefer structured, rule-grounded supervision over scale.** Culturally-grounded fine-tuning lets small models exceed frontier ones [2026-Jin-MedES; 2024-Ohashi; 2025-Bian]; FFT preserves cultural variation better than RLHF [2025-Liu-Cross-cultural].
13. **Make normative authority explicit and pluralism-aware.** Declare whose values are the target since "safe" can encode a contested stance [2025-Han-HKGAI-V1]; support context-dependent (viśeṣa) items/community-swappable modules and separate universal from culture-specific harms [2024-Varshney; 2025-Amugongo].
14. **Report compliance/refusal rates alongside accuracy**—low-resource languages fail to produce parseable answers where coverage matters most [2025-Farid; 2025-Al-SHADES]—and treat cross-cultural refusal asymmetry as a stigmatization signal [2024-Hovy].
