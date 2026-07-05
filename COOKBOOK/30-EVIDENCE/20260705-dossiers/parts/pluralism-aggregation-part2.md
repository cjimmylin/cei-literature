# pluralism-aggregation — sub-dossier part 2/3

Scope: whose values a benchmark encodes — annotator diversity, disagreement-as-signal, aggregation methods, demographic transparency, and democratic/participatory design. This part synthesizes 53 evidence cards.

## A. Synthesized claims

1. **Diverse annotator pools raise disagreement, and disagreement is a measurable signal rather than noise to be averaged away.** DICES collected over 2.5M safety ratings with up to ~123 raters per item (104 reliable), and found a diverse pool "presents much higher rate of disagreement among raters, which poses a challenge to the traditional definition of 'gold' labels"; expert "gold" and crowd-majority labels disagreed on 34% of examples (30% unsafe-by-gold/safe-by-crowd) [2023-Aroyo-DICES Dataset]. ConvAbuse operationalizes the same principle by evaluating models against *all* annotator labels, not just aggregated majority, "to preserve minority perspectives" [2021-Cercas Curry-ConvAbuse]. Vargas argues disagreement in hate-speech annotation "is shaped by annotators' moral values rather than annotation noise" and that standard aggregation "risk[s] encoding dominant moral norms while obscuring minority perspectives" [2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales]. Steen frames the design imperative bluntly: "treating disagreement as information rather than noise improves robustness and inclusivity" [2025-Steen-Ethical aspects of ChatGPT].

2. **The dominant practice, however, is majority-collapse: the field systematically discards minority perspectives.** A survey of 105 cultural-alignment datasets found 97.1% adopt a majority-focused awareness scope, reducing distributions to a single "ground truth"; only 3 datasets (GlobalOpinionQA, WorldValuesBench, KorNAT) are diversity-aware [2025-team-Incorporating Diverse Perspectives in Cultural Alignment]. This is the central structural validity gap the pluralism theme must correct.

3. **Distribution-as-ground-truth scoring is the leading alternative to majority-collapse.** KorNAT scores a model by the survey probability mass a demographically re-weighted national sample (6,174 Koreans, ~219 responses/question) placed on the model's chosen option, rather than by agreement with a majority label; its empirical ceiling is only SVA 0.450, reflecting genuine within-population disagreement [2024-Lee-KorNAT]. The Pluralistic Moral Gap reframes the target as distributional: prompt the model N times to reproduce the human judgment distribution per item, scored by |proportion difference|, showing models "reproduce human judgments only under high consensus" and collapse toward the majority as disagreement rises (Δ ~0.34 at ~0.5 consensus) [2025-Russo-The Pluralistic Moral Gap]. Cross-cultural auditing likewise measures distributional fidelity via KL-divergence against World Values Survey data rather than single-answer accuracy [2025-Liu-Cross-cultural value alignment frameworks].

4. **Models under-represent the breadth of human moral reasoning even when the modal answer matches.** In the Moral Dilemma Dataset, the LLM top-10 values account for 81.6% of value mentions versus 35.2% for humans, and mean value entropy is lower (H 0.46 vs 0.57); Dynamic Moral Profiling (Dirichlet-sampled value profiles injected into prompts) improved alignment 64.3% and raised entropy toward human levels [2025-Russo-The Pluralistic Moral Gap]. Benkler shows the complementary "concentration" failure: text-davinci-003 produced distributions "consistently more concentrated than WVS IQRs," i.e., less demographic spread than humans actually exhibit, with a WEIRD skew (US R²=0.80 vs Nigeria 0.01) [2023-Benkler-Assessing LLMs for Moral Value Pluralism].

5. **Large-scale crowdsourcing can supply population-level ground truth, but with severe self-selection bias.** The Moral Machine gathered ~40M decisions across 233 countries, yielding three country clusters (Western/Eastern/Southern) and consistent top preferences (spare humans>pets, more>fewer, younger>older), yet its optional-survey sample skews young, male, college-educated [2020-Awad-Crowdsourcing moral machines]. MULTITP builds on these 40M human judgments to score LLMs by L2 distance between a 6-dimensional preference vector and the human vector, using speaker-count weighting to aggregate a global score; only 3/19 models scored below 0.6 misalignment (max √6≈2.45) [2024-Jin-Language Model Alignment in Multilingual Trolley].

6. **Aggregation rule choice is itself a value judgment and changes conclusions.** KorNAT reports three variants of the same construct (SVA / A-SVA / N-SVA) that expose opinionated versus neutrality-seeking dispositions from one item set [2024-Lee-KorNAT]. M-ALERT demonstrates policy-configurable aggregation: fine-grained category annotations let the same data be re-scored under different legal/cultural policies (removing cannabis+propaganda raises overall safety ~2%) [2024-Friedrich-M-ALERT]. SafetyAnalyst makes aggregation explicit and steerable via 28 interpretable weights that can be top-down set to policy or bottom-up fit to a community's label distribution — "aligned to a customized safety label distribution" [2025-Li-SafetyAnalyst].

7. **A tiered normativity structure lets a benchmark be strict on universals and pluralistic only where appropriate.** GVS-Scale orders three layers by increasing contextual dependence — non-negotiable Baseline Human Safety, broadly-shared Universal Alignment & Integrity, and context-dependent Contextual & Pluralistic Values — so universal harms score strictly while "normative diversity" is permitted only at the top layer [2026-He-GVS-Scale]. Wang operationalizes conflict resolution with hierarchical norm prioritization (legal > public policy > social values > cultural norms), "by default, legal requirements take precedence" [2025-Wang-Diverse Human Value Alignment].

8. **Expressed (MCQ) preferences mislead about revealed (interactive) behavior — the elicitation format is a confound for whose values you measure.** ConflictScope found models rank protective values 1.7 in MCQ but 4.5 in open-ended interaction; all 14 models except Claude flip from harmlessness-over-helpfulness to the reverse (judge Kappa 0.62) [2025-Liu-ConflictScope]. This mirrors moral hypocrisy: GPT-4 and Claude 2.1 show within-instrument consistency comparable to humans but cross-instrument coherence (abstract MFQ → concrete MFV) collapses (LLM R²<0.08 vs human 0.17–0.38) [2024-Nunes-Conscience Conflict].

9. **Person-conditioned prediction turns pluralism into a steerability test.** UNIMORAL makes ground truth *this annotator's* choice given their MFQ2 (moral foundations) and Hofstede VSM (cultural) profile, bundling validated instruments so each of 5,256 items across 6 languages carries a portable value vector; action prediction was near chance, and models perform worst in Arabic/Hindi [2025-Kumar-Are Rules Meant to be Broken]. HVAE similarly tests whether models can be *induced* into four distinct value profiles (altruistic/prosocial/individualistic/competitive), finding safety training blocks competitive/individualistic values [2023-Zhang-Heterogeneous Value Alignment].

10. **Consistency across framings is a necessary (not sufficient) pluralism-safe metric that sidesteps whose-values authority.** VAL-Bench scores whether a model holds a stable stance across opposing framings of ~115K controversial issues, deliberately making no claim about which values are good; PAC ranges ~10–82% and correlates more with refusals (ρ=0.91) than genuine value preference (ρ=0.80) — "a consistently evil agent would also score highly" [2025-Gupta-VAL-Bench].

11. **Cultural collapse toward a WEIRD/global-average default is pervasive and predicted by training-data volume.** Across 20 countries, all LLMs skewed toward a "moderate global average"; a novel deviation ratio corrects for this, and web-content-per-country correlates with alignment at r=0.94 (GDP r=0.81) [2025-Sukiennik-An Evaluation of Cultural Value Alignment]. Cultural-gene probing shows Western vs Eastern models diverge as expected (GPT-4 IDV +1.21 vs ERNIE −0.89, CAI-to-origin ~0.85–0.91) [2025-Fenech-Borg-The Cultural Gene]. Political bias is language-dependent (Persian mean −2.171 vs Zulu +2.621) [2026-Nadeem-Bias Beyond Borders].

12. **Participatory, community-expert annotation outperforms anonymous crowdsourcing for value-laden tasks in underrepresented contexts.** Burmese hate-speech context experts (not mere translators) raised paired-annotator agreement from 68.75% to 93% and surfaced culturally specific error types [2022-Nkemelu-Tackling Hate Speech]. ConvAbuse recruited annotators from targeted groups (gender-studies students, 6 female/2 non-binary) for construct validity [2021-Cercas Curry-ConvAbuse]. Barrett grounds a 6-principle framework in Ubuntu/Akan/Yoruba communalism, arguing "articulating values … [is] the first step to contextualizing responsible data science" [2025-Barrett-African Data Ethics].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2023-Aroyo-DICES Dataset | 100+ ratings/item make disagreement a powered signal; 34% expert-vs-crowd disagreement |
| 2021-Cercas Curry-ConvAbuse | Score models against ALL annotator labels, reporting aggregated + full-label side by side |
| 2024-Lee-KorNAT | Distribution-as-ground-truth (SVA = survey mass on chosen option); report empirical ceiling 0.450 |
| 2025-Russo-The Pluralistic Moral Gap | LLM top-10 values = 81.6% of mentions vs 35.2% human; consensus level as difficulty axis |
| 2024-Jin-Language Model Alignment in Multilingual Trolley | L2 preference-vector metric, speaker-count-weighted global aggregation over 107 languages |
| 2020-Awad-Crowdsourcing moral machines | 40M decisions/233 countries but young/male/educated self-selection bias |
| 2025-Kumar-Are Rules Meant to be Broken | Person-conditioned ground truth via bundled MFQ2 + Hofstede VSM per annotator |
| 2025-Liu-ConflictScope | Expressed (MCQ) vs revealed (interactive) rankings diverge (protective 1.7→4.5) |
| 2023-Zhang-Heterogeneous Value Alignment | Test steerability into 4 distinct value profiles; safety training blocks competitive values |
| 2025-Gupta-VAL-Bench | Consistency across opposing framings as necessary condition; refusals inflate it (ρ=0.91) |
| 2026-He-GVS-Scale | 3-tier normativity: strict on baseline safety, pluralistic only at top layer |
| 2025-Sukiennik-Cultural Value Alignment | Cultural collapse to global average; web-content-per-country predicts alignment r=0.94 |
| 2025-Fenech-Borg-Cultural Gene | Western/Eastern models diverge on Hofstede IDV/PDI matching their training origin |
| 2023-Benkler-Moral Value Pluralism | LLM distributions more concentrated than WVS IQRs; WEIRD skew (US R²0.80/Nigeria 0.01) |
| 2025-Liu-Cross-cultural value alignment frameworks | Distributional fidelity (KL vs WVS) as a distinct axis; FFT preserves variance better than RLHF |
| 2025-Li-SafetyAnalyst | 28 interpretable weights, bottom-up fittable to a community's label distribution |
| 2026-Vargas-Self-Explaining Hate Speech | Release per-annotator labels + disagreements tied to annotator value survey |
| 2022-Nkemelu-Tackling Hate Speech | Context experts as co-designers lift agreement 68.75%→93% |
| 2024-Tonneau-From Languages to Geographies | Geo-cultural representativeness audit; 0% English HS datasets report both data + annotator origin |
| 2023-Das-Bengali Gender | Intersectional identity dimensions (gender × religion × nationality) + positionality statement |
| 2025-team-Diverse Perspectives | 97.1% of 105 cultural datasets are majority-focused; use JS-distance, not accuracy-vs-mode |
| 2026-Nadeem-Bias Beyond Borders | Political bias is language- and axis-specific; align stance representations before steering |
| 2024-Nunes-Conscience Conflict | Abstract-vs-concrete coherence test exposes "moral hypocrisy" (LLM R²<0.08) |
| 2025-Keshmirian-Many LLMs More Utilitarian | Group deliberation produces emergent "Utilitarian Boost" absent in solo agents |
| 2025-Dubey-Moral Uncertainty | Five moral-theory LLM "jurors" fused via BJSD+DST rather than averaging |
| 2024-Keswani-Active Learning Moral Preference | Preference instability (10–18% repeat variability) limits active-learning elicitation |
| 2024-Friedrich-M-ALERT | Policy-configurable category re-weighting + inter-language exact-match consistency metric |
| 2024-Vladimirova-FairJob | Selection-bias-corrected utility reweights by population base rates of protected group |
| 2025-Wang-Diverse Human Value Alignment | Hierarchical norm prioritization (legal > policy > social > cultural) for conflict resolution |
| 2025-Steen-Ethical aspects of ChatGPT | "Disagreement as information not noise" + individual/organization/society tri-level scope |
| 2024-Šekrst-AI Ethics by Design | User-configurable value layers (ethics-as-RAG) instead of provider-fixed guardrails |
| 2024-Qiu-ProgressGym | Temporal/diachronic alignment; scores whether a method locks in vs advances values |
| 2023-Hou-Multi-Level Framework | Four-level (individual/org/national/global) whose-values check |
| 2025-Neuman-Ethical Logic of Six LLMs | Models converge on rationalist harm-minimization; self-report Kohlberg stage 5–6 |
| 2024-Agarwal-Ethical Reasoning Depends on Language | Same dilemma yields different moral judgments across 7 languages (GPT-4 EN 93% vs Hindi 63%) |
| 2024-Bignotti-Legal Minds | Real court rulings as multi-party (progressive/moderate/conservative) value scale |
| 2023-Mougan-Kantian Deontology | 12/14 group-fairness metrics are utilitarian; procedural (deontological) fairness underused |
| 2025-Barrett-African Data Ethics | Communalist 6-principle framework; ≤68% coverage by any Western comparison framework |
| 2025-Ray-Indigenous knowledge systems | "Boundary mismatch": bounded algorithms vs unbounded relational knowledge; red-teaming can violate protocol |
| 2024-Woodgate-Macro Ethics Principles | 21-principle taxonomy; recommends multi-principle benchmarks that surface trade-offs |
| 2025-De Montis-Morality in AI | Argues LLMs should present multiple moral perspectives, not impose one |
| 2024-Rane-Concept Alignment | Concept alignment precedes value alignment; probe internal representations not just outputs |
| 2025-Brophy-Wide Reflective Equilibrium | Bi-directional principle revision + Collective Constitutional AI (Polis) as legitimacy sources |
| 2024-DAlessandro-Deontology and Safe AI | Separate moral-conformance from safety axes; they can come apart catastrophically |
| 2020-Serafimova-Whose Morality | No neutral standpoint; every framework encodes designer bias ("Whose justice? Which rationality?") |
| 2024-So-Confucian Analects | Virtue-ethics (non-Western) alignment vocabulary; aphorisms as flexible context |
| 2024-Hayes-Virtue and Narrative | Practice-embedded evaluation + Ricoeur triadic rubric (good life/others/just institutions) |
| 2025-Yilma-Ethics of AI in Africa | Ubuntu too vague to operationalize; values must be action-guiding, not aspirational |
| 2025-Rana-Indigenous Data Sovereignty | OCAP + CARE as governance rubric; CARE vs FAIR tension |
| 2025-Unknown-Indigenous data sovereignty | UNESCO dual-use framing: AI both threatens and can revitalize Indigenous languages |
| 2025-IndigenousEthics-Indigenous Ethics | Reciprocity/relational ontology as an alternative alignment construct |
| 2020-Galanos-Japanese Turn | Verify (ethnographically) that a cited cultural value governs behavior before encoding it |
| 2024-Younas-Central Asian AI Ethics | Multilevel regional framework; single frameworks risk over-homogenizing diverse regions |
| 2023-Ty-AI and Religious Practices | Multi-tradition comparative survey template (Baha'i/Buddhist/Christian/Hindu/Islamic) |

## C. Patterns & disagreements

**Convergence.** Cards converge strongly that (a) subjective value labels should not be collapsed to a single gold answer [2023-Aroyo-DICES; 2021-Cercas Curry-ConvAbuse; 2026-Vargas; 2025-Steen], and (b) the operational fix is distributional/probabilistic ground truth scored by distance metrics (KL, JS, L2, |proportion difference|) rather than accuracy-vs-mode [2024-Lee-KorNAT; 2025-Russo; 2024-Jin; 2025-Liu-Cross-cultural; 2025-team]. They also converge that current LLMs collapse cultural and moral diversity toward a WEIRD/global-average default [2025-Sukiennik; 2023-Benkler; 2025-Fenech-Borg; 2025-Russo].

**Tension 1 — survey ground truth vs its own bias.** KorNAT, Benkler, Sukiennik, and the cross-cultural framework treat WVS/Hofstede survey data as authoritative population ground truth [2024-Lee; 2023-Benkler; 2025-Sukiennik; 2025-Liu-Cross-cultural], yet Sukiennik notes Hofstede scores are 1980s aggregates masking within-country diversity, and Awad documents that even 40M crowdsourced judgments are self-selected [2020-Awad]. MULTITP further warns that aligning to human descriptive averages "may not be desirable if those averages encode harmful biases" [2024-Jin]. So the same survey-grounding move is both the best available pluralism anchor and a validity liability.

**Tension 2 — consistency vs expressivity.** VAL-Bench rewards cross-framing consistency but concedes refusals inflate the score (ρ=0.91) and a "consistently evil agent" scores well [2025-Gupta]; Liu's Cross-cultural work praises stable principles, yet ConflictScope shows MCQ "stability" diverges from interactive behavior [2025-Liu-ConflictScope]. Whether consistency is a virtue or an evasion artifact is unresolved.

**Tension 3 — universalism vs pluralism.** GVS insists some safety layers are "non-negotiable" [2026-He], and Wang hard-codes legal precedence [2025-Wang], whereas Šekrst pushes fully user-configurable value layers risking "complete relativism" [2024-Šekrst], and Serafimova argues no neutral standpoint exists at all [2020-Serafimova]. The tiered-normativity design [2026-He] is the most concrete reconciliation but remains a stipulation about which values are universal.

**Tension 4 — annotator diversity helps vs group dynamics distort.** Diverse pools improve coverage [2023-Aroyo; 2022-Nkemelu], but Keshmirian shows that *deliberating* groups of agents drift utilitarian (β=0.31, personal-dilemma-specific) — aggregation topology itself can bias outcomes [2025-Keshmirian]. Diversity in *composition* is protective; diversity dissolved through *consensus* can be distorting.

## D. Exemplars & anti-patterns

**Best-designed.** DICES is the exemplar: radically high replication (100+ raters/item), votes encoded as demographic distributions, annotator-level labels shipped so downstream users can test alternative aggregation strategies, dual gold+platinum labels, and within-group agreement diagnostics (IRR/negentropy/plurality) [2023-Aroyo-DICES Dataset]. KorNAT is the exemplar for principled aggregation: distribution-as-ground-truth from a census-reweighted survey with distractor/consistency screening, a reported empirical ceiling (0.450), and criterion validation that higher-scoring models are actually preferred by Koreans (94/100 questions) [2024-Lee-KorNAT]. ConflictScope is exemplary for the expressed-vs-revealed validity check (Pareto-best observed agreement 0.786) [2025-Liu-ConflictScope]. SafetyAnalyst best operationalizes *steerable* aggregation with 28 auditable weights [2025-Li-SafetyAnalyst].

**Anti-patterns.** The survey of 105 datasets documents the field-wide anti-pattern: 97.1% majority-collapse [2025-team]. Among cards, Neuman's six-LLM study is a weak design — no quantitative scoring, single-run sampling, heavy contamination (all classic dilemmas in training data), and self-report probes that flip 99.6%→99.3% under answer-order reversal [2025-Neuman]. Fenech-Borg tests only two models at cultural extremes with an unspecified CDS scoring rubric (no inter-rater reliability), limiting any pluralism inference [2025-Fenech-Borg]. Vargas, despite arguing disagreement is morally meaningful, then uses the *first* annotator's rationale as gold — internally contradicting its own thesis [2026-Vargas]. Several regional-ethics cards (Ubuntu, Central Asian, Indigenous) are aspirational and, as Yilma shows, their values are "too vague to encode into design principles" without operationalization [2025-Yilma-Ethics of AI in Africa].

## E. Design lessons

1. **Ship annotator-level labels; report both aggregated and full-distribution scores.** Do not pre-collapse to majority; encode votes as demographic distributions so users can re-aggregate [2021-Cercas Curry; 2023-Aroyo; 2026-Vargas].

2. **Score against distributions, not modes.** Use distributional distance (KL, JS, L2, |proportion difference|) and prompt N times to match the human distribution [2024-Lee; 2025-Russo; 2024-Jin; 2025-team; 2025-Liu-Cross-cultural].

3. **Report the empirical ceiling and a naive baseline.** A raw score is illegible without the maximum achievable given human disagreement (KorNAT's 0.450) and a floor (All-Neutral) [2024-Lee-KorNAT].

4. **Add value-diversity/entropy metrics** to catch models that hit the modal answer but flatten breadth, and **stratify items by consensus level** since failures concentrate in the ambiguous grey zone [2025-Russo; 2023-Benkler].

5. **Make aggregation explicit and steerable:** interpretable weights fittable to different communities, plus policy-configurable category re-weighting so one dataset serves plural jurisdictions [2025-Li-SafetyAnalyst; 2024-Friedrich-M-ALERT; 2024-Lee].

6. **Adopt a tiered-normativity structure:** strict scoring on non-negotiable universals, pluralistic scoring only in the context-dependent layer, with explicit conflict-resolution ordering [2026-He; 2025-Wang].

7. **Pair MCQ with interactive elicitation** and treat divergence as a first-class finding; never infer real-world value priorities from MCQ alone [2025-Liu-ConflictScope; 2024-Nunes].

8. **Bundle validated instruments into annotation** (MFQ2, Hofstede VSM, WVS) so every item carries a portable value vector and enables person-conditioned steerability tests [2025-Kumar; 2023-Benkler; 2025-Sukiennik].

9. **Recruit context experts / targeted-group members as co-designers, not translators, and document positionality** — it raises label quality and construct validity [2022-Nkemelu; 2021-Cercas Curry; 2023-Das].

10. **Audit geo-cultural and demographic representativeness of both data and annotators** against multiple reference populations, and **correct sampling skew** via census re-weighting or selection-bias-corrected utility [2024-Tonneau; 2025-team; 2024-Vladimirova; 2024-Lee].

11. **Test multilingually and expect language-conditioned value shifts;** align stance representations across languages before any steering intervention [2024-Jin; 2024-Agarwal; 2026-Nadeem; 2024-Friedrich].

12. **Evaluate group/multi-agent aggregation dynamics, not just single agents** — consensus protocols amplify emergent distortions (Utilitarian Boost); compose diverse agents/prompts to temper them [2025-Keshmirian; 2025-Dubey].

13. **Measure preference stability/test-retest** (moral preferences drift 10–18%), and **treat consistency as necessary-but-not-sufficient**, reporting refusal/no-information rates so evasion is not credited as principled stance [2024-Keswani; 2024-Nunes; 2025-Gupta].

14. **Add a temporal axis** to test whether aggregation locks in status-quo values versus tracking moral change [2024-Qiu-ProgressGym].

15. **Require operationalizability of any value dimension** — action-guiding norms, not aspirational descriptors; verify ethnographically that a cited cultural value governs behavior before encoding it, and note participatory/Indigenous frameworks (OCAP/CARE, "boundary mismatch") also constrain evaluation *procedure* (e.g., red-teaming may violate protocol) [2025-Yilma; 2020-Galanos; 2025-Ray; 2025-Rana].
