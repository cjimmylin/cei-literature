# validity-psychometrics — sub-dossier part 4/6

Scope: 58 cards (52 papers + 6 AI-lab cards) on construct validity, human baselines, inter-rater reliability (IAA), factor/IRT structure, saturation/discrimination, and the disagreement/aggregation problem — heavy on multilingual hate-speech corpora, moral-psychology instruments, and lab system cards.

## A. Synthesized claims

1. **Inter-annotator agreement on subjective values labels is low and wildly heterogeneous — a headline validity number, not a footnote.** Binary hate-speech IAA spans Fleiss κ=0.17 (non-expert) [2019-Fortuna], Krippendorff α=0.45 [2020-Sap-Social Bias Frames] / α=0.46 [2020-Mathew-HateXplain], κ=0.3579 [2021-Plaza-del-Arco-OffendES], up to α=0.696 [2022-Das], α=0.69 [2021-Cercas Curry-ConvAbuse], κ=0.6530 [2022-Ramponi]. Expertise and tightened schemas lift it: Fortuna's expert hierarchical pass hit κ=0.72 vs 0.17 non-expert [2019-Fortuna]; HelpSteer2 raised preference κ 0.489→0.843 via outlier-removal alone [NVIDIA-HelpSteer2]. BBQ's validation loop reached α=0.883 [2022-Parrish-BBQ] and EuroGEST's gender labels κ=0.81 [2025-Team-EuroGEST] — both by making the construct near-objective.

2. **Agreement varies more by category than by pipeline, so aggregate κ hides the signal.** Per-class κ spans 0.879 (Lesbians)–0.276 (Ugly women) [2019-Fortuna]; racism α=0.96 to transphobia α=0.00 and directness α=0.26 [2021-Cercas Curry-ConvAbuse]; Threat-of-Enmity F1=0.66 to Symbolization F1=0.29 [2025-Seker-HATECAT-TR]; weighted-κ 0.81/0.67/0.61 for primary/secondary/tertiary rationales [2026-Vargas]. Lesson: report κ per label and drop low-κ categories (OffendES merged its unstable OFO class [2021-Plaza-del-Arco-OffendES]).

3. **Rigorous human ceilings exist and matter — the best benchmarks estimate them explicitly.** BBQ: raw crowd accuracy 95.7%, majority-vote 99.7% [2022-Parrish-BBQ]; TrolleyBench human ECI=0.711 (but from adolescents, flagged as the wrong reference class) [2025-Zhu-TrolleyBench]; DIT norms (grad ~65, adults ~40) anchor GPT-4's English P-score 55.68 [2024-Khandelwal]; the Moral Machine baseline is 40M decisions across 233 countries [2024-Takemoto], grounded in [2020-Awad]. Bulla's leave-one-annotator-out design makes humans and models directly comparable (human F1=0.59; GPT-4=0.66) [2025-Bulla].

4. **Genuine construct validity is rare; "safetywashing" and surface pattern-matching are the dominant threats.** Eriksson's ~110-paper meta-review finds StereoSet/CrowS-Pairs/WinoBias/WinoGender fail to define what they measure, and ETHICS/TruthfulQA/GPQA/MT-Bench correlate strongly with raw capability [2025-Eriksson]. Liu-Diagnosing shows moral-foundation classification never converges even at 210k samples (sentiment saturates near 1.0), and RLA>0.9 means gains are distributional, not moral — the "pragmatic dilemma" [2025-Liu-Diagnosing]. Freire finds one PCA direction in ada-002 matches fine-tuned BERT on ETHICS-Utilitarianism (73.9 vs 74.6) — wellbeing is a latent linear direction, not necessarily "understanding" [2024-Freire].

5. **Order, framing, and prompt sensitivity routinely swamp the value signal — controlling for them is a validity requirement.** GPT-3.5's self-reported politics flips 99.6% conservative → 99.3% liberal by reversing answer order [2025-Oh]; preference rankings reverse across single/pair/triple/six-way framings, so single-framing MCQ inflates consistency [2025-Jotautaite]; Khandelwal runs 48 permutations/dilemma to net out order [2024-Khandelwal]; MoCa sees ~18.6% moral-agreement swing from persona, 8.1% from prompting [2023-Nie-MoCa]; TrolleyBench ECI drops 0.700→0.658 on prompt rewrite [2025-Zhu-TrolleyBench].

6. **Disagreement is often signal, not noise — a growing "perspectivist" cluster preserves it.** DICES collects 100+ ratings/item and reports 34% expert-vs-crowd disagreement as a finding [2023-Aroyo-DICES]; ConvAbuse evaluates against *all* annotator labels [2021-Cercas Curry-ConvAbuse]; Buyl formalizes "discretion" (humans deviate from principle-consensus 28.9%; only 15-20% of pairs involve genuine conflict) [2025-Buyl]; DETESTS-Dis makes learning-with-disagreement core [2024-Schmeisser-Nieto]; Vargas releases per-annotator labels + ideology survey [2026-Vargas].

7. **Factor structure / IRT-style analysis validates that a space actually carries the intended constructs.** ValueLex builds an LLM value taxonomy bottom-up via EFA → 3 dims (Competence/Character/Integrity), GPT-4 scorer QWK=0.8 [2024-Biedma]; supervised SimCSE recovers the 10 MFT elements (MFD2.0 purity=0.71) while self-supervision collapses to a do/don't binary [2024-Park]; MoCa uses AMCE to profile which factors drive judgments, not pass/fail [2023-Nie-MoCa]; Tagarelli reconstructs the Inglehart-Welzel map via PCA and links religiosity→Purity, national_pride→Loyalty [2026-Tagarelli].

8. **LLM-as-judge is validated by agreement-with-humans on held-out data — or not validated at all.** ImageGuard reports Cohen κ vs humans on a model *not in training* (gender 0.841, race only 0.318) [2024-Li]; Biedma QWK=0.8 [2024-Biedma]; INDIC-BIAS >90% agreement on 250 samples [2025-Nawale]; CritiqueVLM cuts MAE 34.8% vs GPT-4 [Zhipu AI-AlignMMBench]. Anti-patterns: BEATS validates only via ANOVA, no human baseline [2025-Anonymous-BEATS]; MoCoP uses fixed unvalidated weights, no human anchor [2025-Jamshidi].

9. **Aggregation method is itself a validity choice.** Soft/distributional labels beat majority vote for borderline cases: OffendES 10-annotator probability vectors [2021-Plaza-del-Arco-OffendES]; MoCa's explicit "ambiguous" class (50%±10%) [2023-Nie-MoCa]; Liu-Towards uses KL-divergence to human survey *distributions* [2025-Liu-Towards]; HelpSteer2's graded-magnitude Scaled-BT beats binary BT (92.7 vs 91.5) [NVIDIA-HelpSteer2].

10. **Cross-lingual/cross-cultural transfer breaks both metrics and mitigations, exposing hidden construct-invalidity.** Zero-shot cross-script transfer of a Bengali classifier drops macro-F1 0.80→0.39 [2022-Das]; English debiasing degrades or inverts in Maltese with CrowS/SEAT disagreeing [2025-Galea]; the *same* norms flip bias direction Islam↔Christianity by language [2025-Hossain]; DIT P-scores fall 23-47% for Hindi/Swahili [2024-Khandelwal]; English HS datasets track US/UK authorship (r=0.99), so "English" ≠ culture-general [2024-Tonneau].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2018-Ljubesic | Thread-level (not comment-level) train/test split prevents conversational-context leakage; single-annotator sample = no IAA. |
| 2019-Fortuna | Non-expert binary κ=0.17 vs expert hierarchical κ=0.72 on same data; report κ per category (0.28–0.88). |
| 2020-Mathew-HateXplain | Score same items on accuracy, group-bias AND explanation faithfulness; axes dissociate (α=0.46; rationale Jaccard 0.54 vs random 0.36). |
| 2020-Sap-Social Bias Frames | Structured multi-field frame (offensive+intent+group+implied stereotype) beats binary; α=0.45; annotators 82% White. |
| 2021-Cercas Curry-ConvAbuse | Evaluate against ALL annotator labels, not majority gold; severity validated vs expletive count (r=-.46). |
| 2021-Plaza-del-Arco-OffendES | 10-annotator probability-vector soft labels; NOE "non-offensive expletive" class; κ only 0.36. |
| 2022-Das | Cross-script zero-shot transfer collapses macro-F1 0.80→0.39 — a strong discrimination signal. |
| 2022-Parrish-BBQ | Ambiguous vs disambiguated context pairing + mandatory UNKNOWN; human ceiling 99.7%, α=0.883; bias worsens with capability. |
| 2023-Aroyo-DICES | 100+ ratings/item; 34% gold-vs-crowd disagreement reported as the finding, not averaged away. |
| 2023-Hopp | Cross-culturally validate a moral stimulus set (MFV/SMID) against existing US/AU human data (r=.3–.7). |
| 2023-Nie-MoCa | AMCE profiles which latent factors drive judgments; explicit "ambiguous" class; GPT-4 only 43% agreement. |
| 2023-Yao-Value FULCRA | Ground value space in cross-culturally validated Schwartz theory; GPT-4 cross-prompt consistency ~0.65≈human. |
| 2024-Biedma | Bottom-up value taxonomy via EFA (3 dims); GPT-4 scorer QWK=0.8 vs humans; taxonomy built + scored by GPT-4 = circularity. |
| 2024-Goldzycher-GAHD | Multi-strategy adversarial rounds (free/translate/newspaper-FP/contrastive) beat any single strategy; κ 0.83–0.99. |
| 2024-Khandelwal | Use a validated psychometric instrument (DIT) with known human norms; 48 permutations control order. |
| 2024-Li | Validate model-judge with Cohen κ vs humans on a held-out unseen model (race κ only 0.318). |
| 2024-Ohashi | Culture-specific stress subset (244 Japan items) discriminates where the full test saturates; LLM labels, no human IAA. |
| 2024-Sewunetie | Strict gender-balancing by construction so bias = asymmetry; triple-annotate but no κ reported. |
| 2024-Takemoto | AMCE + Euclidean distance to Awad's 40M-decision human baseline; report valid-response rate as a meta-metric. |
| 2024-Vladimirova-FairJob | Proxy protected attribute + selection-bias-corrected utility metric; authors warn proxy ≠ ground truth. |
| 2024-with.pdf (NEIHS Bodo/Assamese) | Two student annotators, no IAA reported; tokenizer quality drives Assamese F1 gap (85 vs 69). |
| 2025-Anonymous-BEATS | Consortium of 3 LLM judges + ANOVA to quantify judge disagreement — but NO human baseline. |
| 2025-Bulla | Leave-one-annotator-out puts humans and models on equal footing (human F1 0.59 vs GPT-4 0.66). |
| 2025-Galea | Triangulate CrowS+SEAT+templates+t-SNE and document when metrics disagree; mitigations don't transfer to Maltese. |
| 2025-Hossain-BRAND | Same norms flip bias direction by language (Bengali→Islam, English→Christianity); no IAA, no human baseline. |
| 2025-Jiang-Delphi | 92.8% accuracy is measured against the same biased crowd pool that trained it — circularity; UDHR×213-identity bias probe. |
| 2025-Jotautaite | Multi-framing (1/2/3/6-option) consistency check; single-framing MCQ inflates apparent consistency. |
| 2025-Lan-McBE | Separate intrinsic (likelihood) from comprehension tasks; "bigger=more biased" is an SS-task artifact. |
| 2025-Liu-Towards | KL-divergence to human survey distributions + diversity-enhanced prompting (0% → 89% response diversity). |
| 2025-Nawale-INDIC-BIAS | ELO/Bradley-Terry over identities + Rank-Shift Metric for directional bias; >90% human-judge agreement. |
| 2025-Seker-HATECAT-TR | Relaxed IoU-based κ (0.57→0.76 at IoU≥0.5) for span tasks; per-category IAA 0.29–0.66. |
| 2025-Team-EuroGEST | Log-likelihood minimal-pair metric; professional-translator validation (κ=0.81) makes the construct near-objective. |
| 2025-Zhu-TrolleyBench | Predefined contradiction checks + run-to-run entropy = fully automatic, judge-free consistency scoring. |
| 2026-Vargas | Release per-annotator labels + annotator ideology survey; weighted κ 0.81/0.67/0.61 by salience rank. |
| 2024-Schmeisser-Nieto (DETESTS-Dis) | Learning-with-disagreement as a first-class design; retains annotator distribution. |
| 2025-Jamshidi-MoCoP | Fully automated ethics scoring with fixed unvalidated weights and NO human baseline. |
| 2026-PKU-Visual Distraction | Visual modality bypasses text safety; numerical-stake sensitivity as a System-2 probe (abstract only). |
| 2020-Awad | Funnel plots distinguish universal (converging) from culturally-variable (diverging) moral orderings across 42 countries. |
| 2022-Ramponi | Annotate broad (misogyny/racism) even when studying religion, for reuse; expert κ=0.65 vs crowd α=0.27. |
| 2023-Rystrøm | Calibration test: model output entropy fails to track population controversy (β≈0); left-skew audit of Delphi. |
| 2024-Altinok | 87% of Turkish vocab is masculine-coded; single-seed-pair bias score = methodological limitation. |
| 2024-Freire | A single PCA embedding direction matches fine-tuned BERT (73.9 vs 74.6) — latent construct probe. |
| 2024-Keswani | Preference instability (10–18% test-retest variability) structurally caps moral-benchmark reliability. |
| 2024-Park | Supervised SimCSE recovers 10 MFT clusters (purity 0.71); self-supervision collapses to do/don't. |
| 2024-Tonneau | Geo-cultural audit: English HS datasets track US/UK (r=0.99); language ≠ culture. |
| 2025-Buyl | Discretion metrics (arbitrariness, principle-supremacy, discrepancy); only 15-20% of pairs need genuine discretion. |
| 2025-Eriksson | Nine-issue anti-pattern taxonomy; safetywashing test (does the "safety" score correlate with capability?). |
| 2025-Liu-Diagnosing | Convergence curves + RLA>0.9 diagnose surface pattern-matching vs genuine moral acquisition. |
| 2025-Oh | Answer-order reversal collapses "moral" measures (99.6%→99.3%); "correct answer" effect = zero variance. |
| 2025-Urchs | Deliberately avoid LLMs in the bias-measurement pipeline to prevent circular bias. |
| 2026-Tagarelli | PCA IW-map reconstruction + EMD to human survey distributions; greedy core-set links culture vars to MFT dims. |
| Anthropic-Claude 4.1 Opus card | Automated multi-turn behavioral auditor (1,160 transcripts) surfaces alignment shifts invisible single-turn; evaluation-awareness flagged as validity threat. |
| Anthropic-Sleeper Agents | Model organisms of misalignment; safety training fails to remove backdoors — behavioral signals ≠ internal state. |
| Anthropic-HH RLHF | Train/test PM split detects reward-hacking; helpfulness/harmlessness are anti-correlated → report both, never one score. |
| NVIDIA-HelpSteer2 | Forced-choice + graded magnitude + outlier removal lifts κ 0.489→0.878; GPT-4-as-ground-truth inflates scores 10-19%. |
| OpenAI-GPT-5 card | Sycophancy as a continuous measurable/trainable trait (0.145→0.052); evaluation-awareness (21.8%) as contamination. |
| Zhipu-AlignMMBench | Prompt-rewrite "alignment score" = inverse SD across paraphrases; fine-tuned CritiqueVLM beats GPT-4 judge. |
| 2025-Nadeem | EU-guidelines 5-domain taxonomy; human-AI agreement only κ≤0.33, worst in relational ethics (<45%). |

## C. Patterns & disagreements

**Convergence.** (a) Every team measuring IAA on subjective harm/values labels finds it low-to-moderate and category-dependent [2019-Fortuna; 2020-Mathew-HateXplain; 2020-Sap; 2021-Cercas Curry-ConvAbuse; 2021-Plaza-del-Arco-OffendES; 2022-Ramponi]. (b) The strongest benchmarks estimate a human ceiling and validate items iteratively [2022-Parrish-BBQ; 2023-Hopp; 2024-Khandelwal]. (c) Multiple teams reach "bias worsens with capability / larger = more stereotyped" [2022-Parrish-BBQ; 2025-Team-EuroGEST; 2025-Nawale-INDIC-BIAS], though McBE shows this is partly an artifact of likelihood-preference tasks and reverses under comprehension tasks [2025-Lan-McBE]. (d) A large cluster preserves disagreement rather than gold-collapsing [2023-Aroyo-DICES; 2021-Cercas Curry-ConvAbuse; 2024-Schmeisser-Nieto; 2025-Buyl; 2026-Vargas].

**Disagreements.** Circularity: FULCRA, Biedma, BEATS, MoCoP, Ohashi and BRAND lean on LLMs to construct and/or score value data [2023-Yao; 2024-Biedma; 2025-Anonymous-BEATS; 2025-Jamshidi; 2024-Ohashi; 2025-Hossain], whereas Urchs *deliberately excludes* LLMs to avoid importing their biases [2025-Urchs], and Sleeper Agents shows behavioral LLM signals can't be trusted as ground truth about internal state [Anthropic-Sleeper Agents]. Is crowd majority a valid target? Delphi treats it as the goal (92.8%) [2025-Jiang-Delphi]; Rystrøm and Buyl argue majority-vote silences minorities and encodes arbitrary discretion [2023-Rystrøm; 2025-Buyl]. Human-baseline quality: Bulla builds a rigorous leave-one-out baseline [2025-Bulla]; TrolleyBench admits its (adolescent) baseline is the wrong class [2025-Zhu-TrolleyBench]; many report none at all [2025-Hossain; 2025-Anonymous-BEATS; 2025-Jamshidi].

## D. Exemplars & anti-patterns

**Best-designed. BBQ [2022-Parrish-BBQ]** is the psychometric exemplar: attested-harm content validity, contrastive 2×2 counterbalanced items, mandatory paraphrased UNKNOWN option, iterative 4/5-crowd template validation, an explicit human ceiling (99.7%, α=0.883), and a bias metric orthogonal to accuracy. **DICES [2023-Aroyo-DICES]** is the exemplar for measurement of disagreement — radically high replication (100+ ratings), demographic-distributed votes, and dual gold/platinum labels quantifying a 34% expert-crowd gap. **HateXplain [2020-Mathew-HateXplain]** models multi-facet same-item validity (correctness + group-bias + rationale faithfulness dissociate). **Khandelwal [2024-Khandelwal]** shows how to reuse a validated instrument (DIT) with known human norms and rigorous permutation control.

**Anti-patterns. MoCoP [2025-Jamshidi]** and **BEATS [2025-Anonymous-BEATS]** score "ethics"/"responsible AI" with LLM judges, no human baseline, and (MoCoP) arbitrary fixed weights — validity rests on the schema alone, and BEATS flags its own factuality judge as unreliable. **BRAND [2025-Hossain]** and **MFD-LLM [2025-Jotautaite]** generate 70-100% of items with the models later evaluated, no human IAA. Delphi's **92.8% [2025-Jiang-Delphi]** is measured against the same US-crowd pool that trained it — agreement ≠ correctness. Single-seed-pair scoring [2024-Altinok] and single-annotator samples [2018-Ljubesic] are minor reliability anti-patterns.

## E. Design lessons for new values-alignment benchmarks

1. **Report IAA per category, not just an aggregate, and tighten or drop low-κ constructs before shipping** [2019-Fortuna; 2021-Cercas Curry-ConvAbuse; 2025-Seker-HATECAT-TR; 2021-Plaza-del-Arco-OffendES]. Use expert or member-of-targeted-group annotators for subtle constructs [2019-Fortuna; 2021-Cercas Curry-ConvAbuse].
2. **Estimate an explicit human ceiling and validate items iteratively** (4/5-agreement gate, edit-and-revalidate); pick a *defensible* human reference class [2022-Parrish-BBQ; 2025-Zhu-TrolleyBench]. Prefer validated psychometric instruments with published norms where they exist [2024-Khandelwal; 2023-Hopp; 2026-Tagarelli].
3. **Run a safetywashing check: correlate your values score with raw capability; if they track, you are measuring capability** [2025-Eriksson]. Complement with convergence curves / RLA to detect surface pattern-matching [2025-Liu-Diagnosing] and a PCA/embedding probe to see whether the construct is even latent [2024-Freire].
4. **Control order/framing as a first-class validity step**: randomize option order, run multiple paraphrases, and report the divergence — reversal or multi-framing collapse invalidates a "moral" measure [2025-Oh; 2024-Khandelwal; 2025-Jotautaite; Zhipu AI-AlignMMBench]. Report response-variance / valid-response-rate as a meta-metric [2024-Takemoto; 2025-Oh].
5. **Treat disagreement as data**: collect high replication, ship per-annotator labels (plus an annotator survey), and report expert-vs-crowd and discretion metrics rather than a single gold [2023-Aroyo-DICES; 2026-Vargas; 2025-Buyl; 2024-Schmeisser-Nieto]. Offer distributional/soft or graded-magnitude labels and compare via KL-divergence to human distributions [2021-Plaza-del-Arco-OffendES; 2025-Liu-Towards; NVIDIA-HelpSteer2].
6. **If using an LLM judge, validate it with Cohen κ / QWK against humans on held-out, unseen-model data; never rely on inter-judge ANOVA alone** [2024-Li; 2024-Biedma; 2025-Nawale; Zhipu AI-AlignMMBench vs 2025-Anonymous-BEATS]. Beware LLM-annotated ground truth inflating scores for models trained on the same source [NVIDIA-HelpSteer2].
7. **Never conflate opposed values into one score**: helpfulness and harmlessness are anti-correlated — report both on a Pareto frontier; use a train/test split of the reward model / judge to detect reward-hacking [Anthropic-HH RLHF].
8. **Validate multilingually and cross-culturally, because both metrics and mitigations frequently fail to transfer** — test the same normative content in multiple languages, geocode/annotate data-and-annotator origin, and triangulate multiple bias metrics documenting where they disagree [2022-Das; 2025-Galea; 2025-Hossain; 2024-Tonneau; 2025-Team-EuroGEST]. Add a culture-specific stress subset that discriminates where the general test saturates [2024-Ohashi].
9. **Anchor constructs in factor structure or an attested/policy source**, not intuition: EFA/clustering to confirm the intended dimensions exist [2024-Biedma; 2024-Park], AMCE to expose which latent factors drive judgments [2023-Nie-MoCa; 2024-Takemoto], and regulation/attested-harm grounding for content validity [2022-Parrish-BBQ; 2024-Li; 2025-Nadeem].
10. **Guard against contamination and evaluation-awareness**: hash/n-gram checks vs training corpora, contamination-resistant novel items, and multi-turn behavioral auditing — models increasingly detect and game evals, and behavioral pass rates do not certify internal alignment [2025-Eriksson; Anthropic-Claude 4.1 Opus card; OpenAI-GPT-5 card; Anthropic-Sleeper Agents].
11. **Design for the disagreement/instability floor**: moral preferences show 10-18% test-retest variability, so measure and report test-retest reliability [2024-Keswani], and avoid LLMs in the instrument itself when circularity corrupts the signal [2025-Urchs].
