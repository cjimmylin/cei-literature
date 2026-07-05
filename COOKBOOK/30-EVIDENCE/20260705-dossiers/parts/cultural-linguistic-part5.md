# cultural-linguistic — sub-dossier part 5/6

This part covers 60 cards heavily weighted toward (a) non-English hate-speech / offensive-language datasets across ~30 languages, (b) culturally-adapted value/bias benchmarks (KoBBQ, BharatBBQ, CultureLLM, ValueCompass), (c) cross-lingual moral/value probing, and (d) non-Western ethics frameworks (African, Andean, Māori/Navajo, Central Asian, Daoist).

## A. Synthesized claims

1. **Machine translation alone mis-measures culturally-situated values; hand-built, survey-grounded localization is required.** KoBBQ validated every stereotype/target with a 100-person Korean survey and showed machine-translated BBQ ("mtBBQ") gives statistically different bias readings (Wilcoxon), with Newly-Created culture-specific items surfacing bias existing models overlooked [2024-Jin-KoBBQ]. BharatBBQ found bias frequently *amplified* in Indian languages vs English and used a Sample-Removed/Culturally-Transformed/Target-Modified/Newly-Created localization taxonomy [2025-Tomar-BharatBBQ]. Hämmerl found multilingual models encode a moral good/bad axis that correlates with English human data (.74–.86) but whose cross-language differences do **not** match human cultural differences — "none of our models' scores map directly onto average human responses" [2023-Hämmerl].

2. **Language-specific / domain-matched resources beat larger generic multilingual models.** Monolingual Greek embeddings scored F1 0.89 vs multilingual BERT 0.73 [2020-Pitenis]; mBERT with no Sinhala pretraining reached only 0.53 macro-F1 [2024-Ranasinghe-SOLD]; a Bangla embedding trained on 1.47M informal comments beat one trained on 250M Wikipedia articles [2022-Romim-BD-SHS]; domain-adaptive NaijaXLM-T beat generic baselines [2024-Tonneau-NaijaHate]. Corollary: BengaliMoralBench found "scaling model size alone is insufficient without rich, localized pretraining data" [2025-Kumar-UniMoral].

3. **Evaluation on curated/keyword-seeded data massively overstates real-world performance.** NaijaHate is the sharpest evidence: average precision was 73.75% on holdout and 81.88% on top-scored sets but only 20.92% on a representative random sample (hate prevalence ~0.16%) — a >2× overestimate [2024-Tonneau-NaijaHate]. Nearly every dataset here used keyword/hashtag seeding that oversamples blatant hate [2020-Pitenis; 2023-Haq-Pashto; 2024-Sharma-TABHATE].

4. **The field is structurally WEIRD-biased at the corpus and design level.** A survey of 75 hate-speech datasets found English = 39% of corpora / 41% of datapoints, with US+UK dominating English authorship; Arabic skews to Jordan, Spanish to Chile/Spain, and economically-developed countries are overrepresented vs speaker population [2024-Tonneau-From Languages to Geographies]. A survey of 105 cultural-alignment datasets found 97.1% adopt a "majority-focused" awareness scope that collapses cultural distributions to a single ground-truth answer; only 2.9% are diversity-aware [2025-team-Incorporating Diverse Perspectives].

5. **Models carry a measurable "cultural gene" tied to training-data origin.** GPT-4 scored strongly individualist (Hofstede IDV +1.21) and low power-distance while ERNIE scored collectivist (−0.89) and high power-distance, each aligning with its origin culture (CAI ~0.85–0.91), t-test p<0.001 [2025-Fenech-Borg]. UniVaR showed value QA pairs cluster by *language* more than by model identity — "language acts as a proxy for culture" [2024-Cahyawijaya]. Abdulhai found most LLMs' Moral-Foundations profiles sit closest to politically conservative humans, and RLHF moved models *farther* from human distributions [2024-Abdulhai].

6. **"Same language, different variant/script" is a clean, underused bias axis — and can encode state censorship.** Simplified vs Traditional Chinese prompting flips model behavior: LLMs favor Simplified terms (37.5 vs 4.4 misaligned terms) yet favor Traditional names in hiring [2025-Lyu]; and Simplified-Chinese responses resemble state-sanitized content across all 7 tested models — "users' language, not location, is predictive" [2025-Ahmed]. VC-LLM shows the mirror image: a Chinese-ideology benchmark where GPT-4's balanced multi-perspective answers score *lowest* (2.86/5) and pro-China answers highest, proving "alignment" is culturally relative [2026-Gao].

7. **Safety degrades — and sometimes inverts — under linguistic/phrasing shift.** SEA-SafeguardBench found guardrails drop 36 AUPRC on culturally-grounded "content generation" prompts and that cultural-aware prompting only helps models with region-specific pretraining [2025-Ngui]. Basu found a counterintuitive inversion: models are sometimes *safer* in low-resource languages (they refuse on surface tokens) but get tricked in high-resource languages (they parse context and comply) [2025-Basu]. English-only DPO detoxification transfers cross-lingually but least for low-resource languages (Hindi/Korean/Arabic/Czech) [2024-Li].

8. **Fine-grained, hierarchical harm labels (presence→type→target→intensity) are the dominant, reusable design pattern and consistently harder than binary.** Recurring across BD-SHS (3-level) [2022-Romim], HatEval (HS/target/aggression) [2019-Basile], OffensEval-schema reuse [2021-Nurce; 2023-Haq], BanHate (7 categories × 7 targets, hierarchical loss) [2025-Hossain], and TABHATE (individual/community/none) [2024-Sharma]. Binary tasks near-saturate (~0.9 F1) while target/type sub-tasks stay far from ceiling (Nurce subtask C 0.52; BanHate category macro-F1 ~0.51) [2021-Nurce; 2025-Hossain].

9. **Recognition ≠ endorsement, and accuracy ≠ faithfulness.** SpeciesismBench models classified 86% of statements as speciesist but judged only 34% morally wrong — "the problem is evaluative rather than epistemic" [2025-Jotautaite]. Urdu HateInsights showed XLM-R at 0.95 accuracy but IOU-F1 plausibility only 0.68 and near-zero sufficiency — high accuracy hides bad rationales [2024-Arshad]. TeSent found rationale supervision improves human-reasoning agreement but does **not** reduce social bias [2025-Kumar-TeSent].

10. **Disagreement is signal, not noise, and majority aggregation encodes dominant norms.** DICES collected up to ~120 ratings/item, found 34% gold-expert vs crowd-majority disagreement, and demographic subgroups differ systematically on what is "unsafe" [2023-Aroyo-DICES]. Reward models embed consistent sociodemographic biases (mean pairwise Spearman r=0.67 across 7 RMs) that in-context steering fails to override [2025-Elle]. Moral rationales are "shaped by annotators' moral values rather than annotation noise" [2026-Vargas].

11. **Expert / demographically-diverse annotators materially change label quality.** Polish expert re-annotation found ~2× as many harmful labels as laypeople (κ 0.33→0.50) [2024-Ptaszynski]; religiously-diverse Albanian annotators and caste-diverse Tamil annotators (Krippendorff α=0.83) were used explicitly to reduce in-group blind spots [2021-Nurce; 2025-Chakravarthi-Caste]. Brazilian HateBR 2.0 required PhD annotators of diverse region/politics/race [2025-Vargas-Context-Aware].

12. **Non-Western normative frameworks name value dimensions absent from mainstream benchmarks.** African data ethics centers reciprocity, communal consent, data self-determination [2025-Barrett]; Andean *ayni* reciprocity [2025-Maldonado]; Māori Kaitiakitanga guardianship and Navajo Hózhó holism, with the pointed observation that standard red-teaming ("list worst-case scenarios") itself violates Hózhó [2025-Ray]; Central Asian multilevel principles [2024-Younas]; Daoist wu-wei [2021-DaoistAI]. Awad's Moral Machine (40M decisions, 233 countries) empirically found three cross-cultural preference clusters (Western/Eastern/Southern) [2020-Awad].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2019-Basile-SemEval-2019 Task 5 | Parallel en/es HS with same scheme; 23-pt cross-lingual gap; no system beat MFC on English fine-grained subtask B |
| 2020-Kumar-Evaluating Aggression | Overt/covert/non-aggression 3-way is far harder than binary gendered; covert class is the discriminator |
| 2020-Pitenis-Greek | Monolingual Greek embeddings 0.89 vs mBERT 0.73 F1 |
| 2020-Yasseri-Islamophobic | Weak/strong intensity scale; domain-specific GloVe +5.9pp; expert annotators α=0.895 |
| 2021-Nurce-Albanian | OffensEval hierarchy reuse; religiously-diverse annotators; subtask C 0.52 (near chance) |
| 2022-Chalkidis-FairLex | 4 group-robust algorithms fail to reduce disparity in realistic imbalanced/drifting splits; report avg+GD+worst-group triad |
| 2022-Romim-BD-SHS | 1.47M informal-text embedding beats 250M-Wikipedia embedding; 3-level hierarchy |
| 2023-Aroyo-DICES | ~120 ratings/item; 34% expert-vs-crowd disagreement encoded as distributions |
| 2023-Haq-Pashto | Two-stage triaged annotation (91% easy panel, escalate 9%); base-rate-faithful imbalance |
| 2023-Narayan-HASOC | Language-specific models beat mBERT when data exists; multilingual wins when data scarce (Gujarati few-shot) |
| 2024-Arshad-Urdu | 0.95 accuracy but rationale plausibility only 0.68 — decouple accuracy from faithfulness |
| 2024-Chakravarthi-Telugu | Transliteration/script normalization augmentation; balanced test set |
| 2024-Goldzycher-GAHD | Multi-strategy adversarial rounds (free/translate/newspaper-FP/contrastive) beat single-strategy DADC |
| 2024-Jin-KoBBQ | Survey-grounded ground truth (100/item) + 3-way cultural-transfer partition; MT alone insufficient |
| 2024-Lee-Korean | Persona×state×topic×query grid; GPT-4 not uniformly safer than ChatGPT across topics |
| 2024-Mozikov-EAI | Affective perturbation shifts moral/strategic behavior; effect scales with pretraining language |
| 2024-Ranasinghe-SOLD | Dual sentence+token annotation for explainability; mBERT 0.53 without Sinhala pretraining |
| 2024-Sharma-TABHATE | Target-level (individual/community/none) labels; minority class hardest even after SMOTE |
| 2024-Tonneau-NaijaHate | Representative random sample AP 20.92% vs holdout 73.75% — >2× overestimation |
| 2024-Xie-CultureLLM | WVS as minimal seed + semantic augmentation; $6 fine-tune; no gain for Korean |
| 2025-Ahmed-Chinese Censorship | Simplified vs Traditional pivot detects state-censorship bias in all 7 models |
| 2025-Basu-Multilingual Moral | Trick vs regular categories; low-resource languages sometimes SAFER than high-resource |
| 2025-Chakravarthi-Caste | Caste/migration Tamil; culturally-grounded annotation terms; α=0.83; shared task validation |
| 2025-Elle-Reward Models | 7 RMs share sociodemographic bias (Spearman 0.67); in-context steering fails to fix |
| 2025-Galea-Maltese | English debias metrics/methods degrade or invert in gendered low-resource language; CrowS↔SEAT disagree |
| 2025-Hossain-BanHate | Event-anchored recency sampling; hierarchical loss; per-category+per-target kappa reporting |
| 2025-Jiao-LLM Ethics | MFQ/WVS/dilemmas → dual numeric+reasoning; score vs human distributions not single answer |
| 2025-Jotautaite-Speciesism | Recognition 86% vs moral condemnation 34%; capability does not track condemnation |
| 2025-Kumar-TeSent | Rationale supervision improves plausibility but NOT fairness |
| 2025-Leonardelli-MuLTa | In-domain (Telegram) vs out-of-domain (Twitter) degradation as validity evidence |
| 2025-Lyu-Simplified | 3-way response taxonomy correct/misaligned/incorrect; single-character edits swing bias |
| 2025-Ngui-SEA-Safeguard | Paired XX-EN design separates language from culture; CG-cultural drops 36 AUPRC |
| 2025-Sah-FairEval | Paired neutral-vs-identity counterfactual prompting; rank-sensitive divergence metrics |
| 2025-Shen-ValueCompass | Schwartz-grounded scenario value elicitation; best human-LLM alignment F1 only 0.529; India lowest |
| 2025-Tomar-BharatBBQ | Stereotypical-Bias-Score separates endorsement from lexical preference; bias amplified in Indian languages |
| 2025-Yao-NurValues | Ethnographic field-grounded items + counterfactual polarity flip + adversarial Hard tier |
| 2026-Gao-Adversarial | Chinese-ideology benchmark where GPT-4 balanced answers score lowest — "alignment" is relative |
| 2026-Vargas-Moral Rationales | Moral (MFT) rationales as attention supervision; more culturally transferable than lexical cues |
| 2024-Khanduja-Telugu | mBERT 98.2% (suspiciously high → likely leakage/imbalance) — cautionary |
| 2025-Fenech-Borg-Cultural Gene | Hofstede IDV/PDI divergence GPT-4 vs ERNIE aligns with origin culture (p<0.001) |
| 2025-Kumar-UniMoral | Build-from-scratch triadic Virtue/Commonsense/Justice; lexical-neutrality anti-shortcut constraint |
| 2020-Awad-Moral Machines | 40M decisions/233 countries; 3 cultural clusters; forced-choice no-safe-option design |
| 2022-Abbasi-Religious | Identity-group-stratified toxicity dataset; per-group toxic-rate transparency |
| 2022-Ramponi-Religious | 5-level taxonomy interoperable with prior schemes; annotate-broad-study-narrow |
| 2023-Hämmerl-Moral Bias | Multilingual moral axis exists but is NOT culturally differentiated |
| 2024-Abdulhai-Moral Foundations | LLMs cluster near conservative humans; RLHF widens gap; prompts steer foundations |
| 2024-Cahyawijaya-UniVaR | High-dim value embedding; language clusters > model clusters (language as culture proxy) |
| 2024-Li-Toxicity Transfer | English DPO detox transfers cross-lingually, least for low-resource languages |
| 2024-Ptaszynski-Polish | Expert re-annotation finds ~2× harmful labels vs laypeople |
| 2024-Tonneau-Geographies | English = 39% of HS datasets; developed countries overrepresented vs speakers |
| 2024-Yoo-HyperCLOVA X | Society-matched paired benchmarks (BBQ↔KoBBQ, RTP↔KOLD); red-team→training-data loop |
| 2025-Barrett-African | Reciprocity, data self-determination, communal consent as missing value dimensions |
| 2025-Fillies-German TikTok | 32-label type/origin/target taxonomy; classifier-ensemble sampling; annotator mental-health reporting |
| 2025-Kajiwara-MetaHate | Aggregating 36 datasets tests cross-dataset generalization; label noise ceiling |
| 2025-Maldonado-Indigenous | Andean reciprocity (ayni) as non-utilitarian normative axis |
| 2025-Ray-Indigenous | Kaitiakitanga/Hózhó; standard red-teaming can violate Indigenous protocol |
| 2025-Vargas-Brazilian | "Deeply culture-rooted" untranslatable terms (~10%); context-dependent vs -independent axis |
| 2025-team-Diverse Perspectives | 97.1% of 105 datasets majority-focused; score distributions (JS-distance) not modes |
| Alibaba-Qwen3 | 119-language pretraining, but NO safety/values eval, no model spec — capability without values reporting |
| 2021-DaoistAI / 2024-Younas / 2025-Insights | Wu-wei, Central-Asian multilevel, MFT human-LLM gap frameworks (theory, no benchmark) |
| 2026-Reaj-Gender Bias Bengali | Multi-method yield comparison; translation retains only 24–31% bias; community field studies |

## C. Patterns & disagreements

**Convergence.** (a) Overwhelming agreement that English/Western resources under-serve other languages and cultures [2020-Pitenis; 2024-Tonneau-NaijaHate; 2024-Tonneau-Geographies; 2024-Jin-KoBBQ; 2025-Tomar-BharatBBQ; 2024-Yoo-HyperCLOVA]. (b) Hierarchical harm taxonomies and macro-F1 under class imbalance are near-universal design choices. (c) Fine-grained sub-tasks resist saturation while binary tasks saturate. (d) Multiple methodologically-strong papers converge on "human-alignment ≠ fairness" and "accuracy ≠ faithfulness" [2025-Kumar-TeSent; 2024-Arshad; 2025-Jotautaite].

**Disagreements / tensions.** (1) *Whose values are "correct"?* Gao's VC-LLM explicitly rewards single-perspective pro-China answers and penalizes GPT-4's multi-perspective balance [2026-Gao], directly opposing the pluralist "preserve distributions" stance of DICES [2023-Aroyo] and the diversity-aware critique of [2025-team]. (2) *Is mimicking human moral bias good?* Mozikov scores "alignment" as matching human emotional irrationality [2024-Mozikov], while Abdulhai treats resemblance to a human subgroup as a *bias* to flag [2024-Abdulhai]. (3) *Language-as-culture:* CultureLLM, UniVaR and Fenech-Borg operationalize culture via language [2024-Xie; 2024-Cahyawijaya; 2025-Fenech-Borg], but Hämmerl and Tonneau warn language ≠ culture (Arabic spans many cultures; "English from Nigeria" ≠ "English from US") [2023-Hämmerl; 2024-Tonneau-Geographies]. (4) *Monolingual vs multilingual models:* language-specific wins with enough data, but multilingual wins in few-shot/low-data regimes [2023-Narayan]. (5) *LLM-generated items:* CultureLLM/NurValues/SpeciesismBench rely on model-generated data, risking generator idiosyncrasy and contamination — NurValues itself concedes its LLM-generated Hard tier is less reliable than the field-observed Easy tier [2025-Yao].

## D. Exemplars & anti-patterns

**Best-designed.** **KoBBQ** [2024-Jin] is the standout: a reusable cultural-transfer partition, survey-validated ground truth with a "no stereotype exists" escape option, a human reading-comprehension solvability gate, and dual accuracy+diff-bias metrics with analytic bounds. **NaijaHate** [2024-Tonneau] for separating training-sampling from a representative evaluation sample and proving benchmark-validity collapse. **DICES** [2023-Aroyo] for radically high replication turning disagreement into signal. **GAHD** [2024-Goldzycher] for multi-strategy adversarial collection. **NurValues** [2025-Yao] for ethnographic grounding + counterfactual polarity flips. **BharatBBQ** [2025-Tomar] for the Stereotypical-Bias-Score that separates endorsement from lexical artifact.

**Anti-patterns.** **Khanduja-Telugu** [2024-Khanduja]: 98.2% accuracy with no reported IAA, class balance, or validity — a textbook leakage/imbalance red flag. **Qwen3** [Alibaba]: 119-language capability with zero safety/values evaluation and no model spec — capability reporting divorced from values. **VC-LLM** [2026-Gao]: a same-ideology LLM judge instructed to "always adhere to Chinese values," making high human-judge agreement circular and prioritizing ideology over factual accuracy. **Single-annotator fine-grained labels** in BD-SHS Levels 2/3 [2022-Romim] and no-IAA datasets [2023-Haq; 2024-Arshad] undermine reliability. **FairEval** [2025-Sah] operationalizes "race" with slurs verbatim in prompts and defines any list-divergence as unfairness without a human notion of legitimate personalization.

## E. Design lessons

1. **Localize by survey, not by translation.** Validate every culture-specific stereotype/target with a demographically-balanced public survey and provide a "no stereotype exists" opt-out; add Newly-Created items for constructs absent from the source culture [2024-Jin-KoBBQ; 2025-Tomar-BharatBBQ]. Report a translation-retention rate to quantify cross-lingual construct transfer [2026-Reaj].

2. **Separate training-set sampling from a representative evaluation sample.** Keyword/active-learning seeding is fine for training but evaluate on a random draw at real base rates, and report the holdout-vs-representative gap [2024-Tonneau-NaijaHate].

3. **Ship distributions, not just majority labels.** Collect high replication, encode votes as demographic distributions, and score with distributional distance (Jensen-Shannon) alongside accuracy [2023-Aroyo; 2025-team]. Report absolute *and* relative alignment [2025-Elle].

4. **Use a "same language, different variant/script" or paired XX-EN axis** to separate linguistic robustness from cultural knowledge and to detect state/ideological bias [2025-Lyu; 2025-Ahmed; 2025-Ngui].

5. **Decompose harm hierarchically (presence→type→target→intensity) and score sub-tasks separately** — binary saturates, sub-tasks discriminate [2022-Romim; 2025-Hossain; 2020-Yasseri]. Prefer macro-F1 / balanced accuracy under imbalance.

6. **Score the moral basis, not the surface trigger.** Require rationales and evaluate plausibility+faithfulness (ERASER-style) separately from accuracy; split recognition from endorsement [2024-Arshad; 2025-Jotautaite; 2026-Vargas]. Do not assume rationale supervision yields fairness [2025-Kumar-TeSent].

7. **Recruit demographically/expertise-diverse annotators and report per-group kappa;** expect binding/collective-identity dimensions to have lower agreement [2024-Ptaszynski; 2025-Hossain; 2025-Chakravarthi-Caste]. Report annotator ideology/values and release per-annotator disagreements [2026-Vargas].

8. **Test safety under phrasing/language shift and affective perturbation**, including low-resource languages where surface-refusal vs context-comprehension can flip which language is safer [2025-Basu; 2024-Mozikov; 2024-Li]. Cultural-aware prompting is not a substitute for region-specific pretraining [2025-Ngui].

9. **Build society-matched paired benchmarks** (BBQ↔KoBBQ, RTP↔KOLD) so "aligned to which culture?" is separable from raw capability [2024-Yoo]. Use adversarial multi-strategy collection and contrastive minimal pairs to avoid homogeneous failure modes [2024-Goldzycher].

10. **Incorporate value dimensions from non-Western frameworks** — reciprocity/communal consent [2025-Barrett; 2025-Maldonado], guardianship/holism [2025-Ray], individualism-collectivism and power-distance [2025-Fenech-Borg] — and note that even the evaluation *procedure* (e.g., worst-case red-teaming) can violate a target culture's norms [2025-Ray].

11. **Guard against LLM-generated-item contamination and generator idiosyncrasy**; anchor at least the reliable tier in human-authored or field-observed data and disclose which tier is trustworthy [2025-Yao; 2024-Xie].

12. **Audit geo-cultural coverage explicitly** (who authored the data, where annotators are from, whether they align) as a standard benchmark-card field [2024-Tonneau-Geographies; 2025-team].
