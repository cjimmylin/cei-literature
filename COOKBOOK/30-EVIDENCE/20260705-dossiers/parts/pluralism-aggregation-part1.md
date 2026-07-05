# pluralism-aggregation — sub-dossier part 1/3

Scope: whose values benchmarks encode — annotator diversity, disagreement-as-signal, aggregation, demographic transparency, participatory approaches. 54 cards.

## A. Synthesized claims

1. **Disagreement is structured signal, not noise, and preserving it improves downstream alignment.** PluriHarms rates 150 prompts by 100 profiled annotators (15,000 ratings): disagreement emerges from trait×prompt interactions (prompt features R²=0.273, traits R²=0.0232, interactions R²=0.0686) and personalized k-shot beats consensus (MAE 0.196 vs 0.263) [2026-Li-PluriHarms]. Sorensen confirms the payoff: preserving all 27,375 ratings yields ~53% greater toxicity reduction than majority vote and ~6× more than full consensus (85.3% of pairs show disagreement) [2025-Sorensen-Operationalizing Pluralistic Values]. MIC collects multiple conflicting Rules-of-Thumb per item and records Global Consensus as a measured quantity [2022-Ziems-The Moral Integrity Corpus]; IndoToxic2024 preserves per-annotator labels rather than majority-voting [2024-Susanto-IndoToxic2024].

2. **Who annotates measurably determines what a model learns.** Sorensen: fine-tuning on Liberal/White/Female feedback improves target dimensions by 5.0/4.7/3.4 pp over Conservative/Black/Male feedback; male raters scored responses 18% less toxic than female raters; Black/African-American raters rated Emotional Awareness 44% higher than White raters [2025-Sorensen-Operationalizing Pluralistic Values]. IndoToxic2024: males labeled 19.3% of data toxic vs females 13%; a model trained on Islam annotators scored F1 0.660 on their own labels but 0.597 on non-Islam labels [2024-Susanto-IndoToxic2024]. Arzberger documents that OpenAI crowdworkers were ~50% Filipino/Bangladeshi and ~50% aged 25-34, and Anthropic evaluators ~68% white [2024-Arzberger-Nothing Comes Without Its World].

3. **Aggregation rule choice is itself a contested normative act with large effects.** ABCFair's central lesson: the "winner depends on the framing" — intervention stage, group composition, and fairness notion are mutually incompatible axes (7 formally-defined, provably-incompatible fairness notions), so there is no single leaderboard [2024-Defrance-ABCFair]. Noothigattu proves that under a Thurstone-Mosteller model all "reasonable" swap-dominance-efficient voting rules select the same winner, making rule choice moot *if* you accept the TM parametrization — grounded on 18.2M pairwise comparisons from 1.3M voters [2018-Noothigattu-A Voting-Based System]. Boddington/Takeshita's MEC aggregates theory-specific models via Maximizing Expected Choiceworthiness with equal credence weights justified by PhilPapers endorsement (32% consequentialism, 31% deontology, 37% virtue) [2023-Boddington-Normative Ethical Theory AI Ethics].

4. **Group-aware consensus can protect minorities against majority capture.** Collective Constitutional AI sourced a constitution from 1,002 US adults (1,127 statements, 38,252 votes) using Group-Aware Consensus (GAC threshold 0.723) to select principles all opinion clusters endorse; the public model showed lower bias on all 9 BBQ dimensions while matching MMLU (72.3 vs 72.4) [2024-Huang-Collective Constitutional AI].

5. **Demographic conditioning changes model behavior — sometimes helping, sometimes fragmenting data.** Adding annotator persona to GPT-3.5 improved zero-shot toxicity detection (up to +0.47 macro-F1 on specific topic-location pairs), but adding the same demographic conditioning to fine-tuned IndoBERTweet *hurt* performance (0.672 vs 0.718 baseline) by fragmenting training data [2024-Susanto-IndoToxic2024]. Elle finds demographic steering of reward models largely fails: BIO/PORTRAY/QA prompt steering gave effect sizes of only 0.086/0.148/0.064 [2025-Elle-Reward Model Perspectives].

6. **Biases embed before the LM: reward models encode consistent sociodemographic preference rankings.** Across 7 open reward models, relative alignment rankings are strikingly consistent (mean pairwise Spearman r=0.67, p<0.001; Friedman TF=295.7), even as absolute alignment varies (PRISM 0.732–0.930); income (r=0.91) and political party (r=0.83) show reliable signal [2025-Elle-Reward Model Perspectives].

7. **Country-of-origin does not predict cultural value alignment — most models skew American.** All 20 LLMs (10 Chinese-, 10 US-origin) respond more like American than Chinese survey participants on MFQ-2 and WVS; the LLM-origin × nationality interaction (β=.03) is an order of magnitude smaller than the nationality main effect (β=−.30), and Chinese language/persona/origin only slightly mitigate the skew [2025-Haslett-Made-in China Thinking in America]. PRIME finds all 6 models converge on a WEIRD-liberal profile — Care 3.6–3.9, Fairness 3.3–4.1, vs Authority/Sanctity 1.1–1.7 [2025-Neuman-PRIME Framework]. SWT finds Egalitarianism ceiling (>4.2) and Fatalism floor (<3.0) across 28 models [2025-Li-Analyzing Cognitive Differences]. Rao shows even GPT-4 (93.29% policy-following) drops to 73.15% on Rajesh's dilemma, the only community-over-individual scenario [2023-Rao-Ethical Reasoning].

8. **"Whose values" and "what values" must be explicitly disclosed; calling a values benchmark an "ethics" benchmark over-claims objectivity.** LaCroix argues it is impossible in principle to benchmark whether AI "is ethical" (presupposes moral realism + defeated by the long tail); reframing to "values" forces disclosure of what the values are and whose they are [2025-LaCroix-Metaethical perspectives]. Gabriel: the challenge is not the "true" moral theory but fair principles receiving reflective endorsement despite pluralism [2020-Gabriel-Artificial Intelligence Values and Alignment].

9. **National/media/state corpora can be mined at scale for value targets, but "official stance = national values" is a strong, contestable equation.** NaVAB scrapes five nations' media, applies graph-based Conflict Reduction to distill coherent signals, and builds <Q,S,RS> contrastive triples (Germany lowest, tracking sparse pretraining data) [2025-Ju-NaVAB]. C-VARC builds 257,609 rules on China's core socialist values; 7 LLMs preferred C-VARC options >70.5%, but Politics discriminates by origin (86% domestic vs 47% best Western) [2025-Wu-CVC]. HKGAI-V1 defines "safe" as "compliant with PRC and HK laws," scoring 79% safe on HK-sensitive issues vs ChatGPT 10.7% — ideological conformity as "safety" [2025-Han-HKGAI-V1].

10. **Western fairness/trust constructs do not transfer; non-Western frameworks introduce distinct axes.** India's salient axes (Region, Caste) are absent from Western frameworks, and American names underestimate MuRIL's bias vs Indian names [2022-Shaily Bhatt-Re-contextualizing Fairness]. Afro-relational trust is bidirectional, communal and earned, not a reliability assessment [2025-Amugongo-Enriching Moral Perspectives]. Ubuntu operates as virtue, procedure, and outcome [2022-Gwagwa-Ubuntu].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2026-Li-PluriHarms | Two-axis (harm × agreement) design; disagreement regressed onto prompt features; personalized > aggregated (MAE 0.196 vs 0.263) |
| 2025-Sorensen-Operationalizing Pluralistic Values | Preserving all ratings beats majority vote by ~53% on toxicity; demographic composition shifts outcomes 3–5 pp |
| 2022-Ziems-The Moral Integrity Corpus | Multiple conflicting free-text RoTs per item + Global Consensus + annotator MFQ/ideology metadata |
| 2024-Susanto-IndoToxic2024 | Preserve per-annotator labels; persona injection helps zero-shot (+0.47 F1) but fragments fine-tuning data |
| 2025-Elle-Reward Model Perspectives | RM sociodemographic rankings consistent across 7 models (Spearman 0.67); in-context steering fails (≤0.148) |
| 2024-Huang-Collective Constitutional AI | Group-Aware Consensus (0.723) selects cross-cluster principles; lower BBQ bias, equal capability |
| 2018-Noothigattu-A Voting-Based System | Under a TM model, all swap-dominance-efficient voting rules pick the same winner (rule choice moot) |
| 2018-Awad-The Moral Machine experiment | 39.61M decisions; 3 moral clusters; cultural distance ρ=0.49; individual demographic effects <0.1 |
| 2023-Boddington-Normative Ethical Theory | MEC aggregates theory-specific models with credence weights from PhilPapers endorsement |
| 2024-Defrance-ABCFair | 7 incompatible fairness notions; per-framing leaderboards + dual-label (biased/unbiased) eval |
| 2025-Haslett-Made-in China | Country-of-origin barely predicts alignment (β=.03) vs nationality (β=−.30); leave-one-dimension-out |
| 2025-Ju-NaVAB | Graph-based Conflict Reduction distills coherent signal from self-contradictory media corpora |
| 2025-Wu-CVC | Head-to-head options (C-VARC vs SC101 vs MIC + distractor) reveal which cultural norm a model prefers |
| 2025-Shen-ValueCompass | Same Schwartz instrument for humans + LLMs; best F1 only 0.529; India lowest |
| 2025-Li-Analyzing Cognitive Differences | Cultural Theory scaffold (Hierarchy/Egalitarianism/Individualism/Fatalism); dose-response social feedback |
| 2025-Neuman-PRIME Framework | Multi-typology triangulation (consequentialist/deontological + MFT-6 + Kohlberg-6) + human baselines |
| 2023-Rao-Ethical Reasoning | Test policy-following not moral correctness; complement-policy pairs; culture-discriminating dilemma |
| 2023-Wang-STREAM | Judgment+Degree+Confidence; demographic-anchored group baselines; MC stability across 5 trials |
| 2024-Cahyawijaya-High-Dimension Human Value | Language-as-culture split: same model in 25 languages = distinct value instances; contrastive value embedding |
| 2024-Arzberger-Nothing Comes Without Its World | Record annotator situation (mood/culture/context), not just judgment; preserve disagreement distribution |
| 2024-Park-Morality is Non-Binary | Multi-dimensional MFT embedding; self-supervision collapses to do/don't binary — human labels required |
| 2020-Gabriel-AI Values and Alignment | Six-way alignment-target taxonomy; fair principles via overlapping consensus / veil / social choice |
| 2024-Gabriel-Ethics of Advanced AI Assistants | Tetradic alignment (AI/user/developer/society), 8 failure modes; three-layer evaluation |
| 2024-Zhi-Xuan-Beyond Preferences | Preference incompleteness as signal: test whether models admit incomparability vs confabulate a ranking |
| 2025-Benavoli-AI Safety Uncertainty | Add explicit "incomparable" annotation option; forcing choice on incomparable items fakes irrationality |
| 2023-Feng-Case Repositories | Casuistry: encode values as community-judged precedents; expert dimension-elicitation workshops |
| 2023-Ji-AI Alignment | RICE taxonomy; safetywashing; moral-consistency probes; document source demographic coverage |
| 2023-Rystrøm-Apolitical Intelligence | Sock-puppet audit: Delphi left-skewed (Dem β=.11, Rep β=−.14); entropy fails to track controversy |
| 2024-Tennant-Dynamics of Moral Behavior | Population composition shapes emergent cooperation; narrow norms self-sabotage |
| 2025-Zohny-ADEPT Simulating Ethics | Panel composition changes outcomes; YAML personas with forbidden_moves; secret ballot + justification |
| 2025-LaCroix-Metaethical perspectives | Reframe "ethics" as "values": disclose what and whose; is/ought fallacy in survey-derived scoring |
| 2024-Meadows-LocalValueBench | Jurisdiction-anchored items + escalating-coercion interrogation ladder; refusal scored distinctly |
| 2024-Lee-Korean Social Context | State×persona×topic×query grid; "safer" GPT-4 more toxic than ChatGPT on some Korean topics |
| 2022-Shaily Bhatt-Re-contextualizing Fairness | Geo-cultural axes (Region, Caste) absent from Western frameworks; locale-specific proxies essential |
| 2025-Amugongo-Enriching Moral Perspectives | Afro-relational trust is bidirectional/communal/earned; open-ended "what does X mean" validity probe |
| 2022-Gwagwa-Ubuntu | Three-register analysis (virtue/procedure/outcome); uncounted/unaccounted/discounted exclusion taxonomy |
| 2025-Lindstrom-Helpful Harmless Honest | Sycophancy is a structural artifact of preference optimization — an anti-benchmark confound |
| 2025-Nay-Aligning AI through Law | Democratic law as legitimate aggregation target; fiduciary duty as alignment standard |
| 2026-Kolt-Legal Alignment | Legal alignment as "critical lower bound"; reason-giving + role-specific rule sets as eval dimensions |
| 2025-Vishwanath-Machine Ethics or AI Alignment | ME (embed theory) vs alignment (follow consensus) typology; demand explicit philosophical grounding |
| 2025-Yaacov-Normative Moral Pluralism | Moral threshold (universal floor) + local layer; integration/compromise/compensation taxonomy |
| 2019-Aliman-Requisite Variety | Ethical adversarial examples exploit gaps in moral variety; perceiver-dependent evaluation |
| 2024-Guldimann-COMPL-AI | Top-down EU-AI-Act-to-technical mapping; surface "dead" saturated benchmarks as broken metrics |
| 2025-Davies-Fairness identification | Counterfactual demographic prompt; fairness-to-utility ratio |
| 2025-Drukker-Concerns and Values in HRI | Positive/negative valence pairing per value topic; Agency vs Autonomy distinction |
| 2024-Wilders-Socratic Dialogue | Dissensus-as-resource; "question of conscience" framing; fortitude under pressure as evaluable |
| 2024-So-AI Confucian Analects | Non-Western virtue ethics (ren/xiao/li/yi) as alternate grounding; cross-tradition validation |
| 2024-Mokoena-Holistic Ubuntu | Tripartite (humanity/spirituality/environment) non-anthropocentric value structure |
| 2025-Osei Mensah-Missing Values | Intrinsic vs instrumental value of nature as a discriminating cross-cultural dimension |
| 2025-UbuntuAI-Ubuntu Governance | Five-layer governance rubric incl. Harm Reconciliation Panels + Developer Benefit Realisation |
| 2025-Perera-Indigenous Peoples and AI | CARE/OCAP data-sovereignty principles as rubric dimensions; Maori health-model bias case |
| 2022-IslamicVirtue-Islamic Virtue Ethics | Maqasid five-protection (faith/life/intellect/lineage/wealth) as multi-dimensional rubric |
| 2024-Puzio-Eco-Relational | Eco-relational ontology challenges anthropocentric defaults; intrinsic value of non-humans |
| 2025-Zgliczynski-Cuber-Ethical Resonance | Cultural universality index + convergence analysis (multi-model agreement) as validity metrics |

## C. Patterns & disagreements

**Convergence.** (1) A strong majority endorse disagreement-preservation over consensus-collapse [2026-Li-PluriHarms; 2025-Sorensen; 2022-Ziems; 2024-Susanto; 2024-Arzberger; 2024-Park]. (2) Independent lines converge on a WEIRD/American/liberal skew in current models [2025-Haslett; 2025-Neuman; 2025-Li-Cognitive; 2023-Rystrøm; 2023-Rao; 2025-Shen]. (3) Cross-cultural work agrees Western constructs do not transfer and demand locale-specific axes [2022-Shaily Bhatt; 2025-Amugongo; 2022-Gwagwa; 2024-Lee]. (4) Many recommend demographic transparency and coverage audits as a validity requirement [2024-Arzberger; 2023-Ji; 2025-Lindstrom; 2025-LaCroix].

**Disagreements.** (a) *Does aggregation-rule choice matter?* Noothigattu proves rule choice moot under a TM model [2018-Noothigattu]; ABCFair proves the opposite for fairness — the winner depends on framing [2024-Defrance]. Reconciliation: Noothigattu's result holds only under its restrictive parametrization. (b) *Is preference/utility the right substrate?* Zhi-Xuan and Benavoli argue incomplete preferences must be representable [2024-Zhi-Xuan; 2025-Benavoli], against the revealed-preference programs of Noothigattu and RLHF [2018-Noothigattu; 2025-Lindstrom]. (c) *Whose authority sets the target?* Law [2025-Nay; 2026-Kolt] vs public deliberation [2024-Huang] vs state/media corpora [2025-Ju; 2025-Wu; 2025-Han] vs philosophy-weighted theories [2023-Boddington] vs "no defensible ground truth" [2025-LaCroix]. (d) *Do individual demographics matter?* Awad found effects <0.1 [2018-Awad], but Sorensen and IndoToxic2024 found 3–5 pp topic-specific effects that move models [2025-Sorensen; 2024-Susanto] — Awad measured average preference shift, the others downstream training impact.

## D. Exemplars & anti-patterns

**Best-designed.** *PluriHarms* is the strongest pluralism benchmark here: it treats disagreement as an explicit second axis, over-samples the ambiguous middle via genetic-algorithm curation, validates its synthetic harm gradient against humans (r=0.59), instruments annotators with validated psychometrics, and decomposes disagreement into interpretable prompt×trait variance [2026-Li-PluriHarms]. *Collective Constitutional AI* is the exemplar participatory pipeline — representative sampling, submit-and-vote wiki-survey, Group-Aware Consensus to resist majority capture, and a measured behavioral outcome [2024-Huang]. *ABCFair* is the exemplar of aggregation honesty: it refuses a single number and makes the contested framing selectable, plus the dual-label trick separating "what people said" from "the defensible target" [2024-Defrance]. *Sorensen* is the best controlled study isolating the levers (demographic composition, scale granularity, disagreement handling, optimizer) [2025-Sorensen].

**Anti-patterns / cautionary.** *HKGAI-V1* labels legal-ideological conformity "safety" and self-evaluates on unreleased benchmarks with no inter-rater reliability — hiding rather than surfacing whose values are encoded [2025-Han]. *NaVAB* and *C-VARC* equate official-media/state values with "national values," treat nations as monolithic, and route generation + filtering + judging through one model family (circularity) [2025-Ju; 2025-Wu]. *SWT* generated its items with GPT-4o then tested GPT-4o; its >99% Cronbach's alpha signals redundancy, not reliability [2025-Li-Cognitive]. *LocalValueBench* scores refusal as 0, conflating legality with ethics, with authors as their own reviewers [2024-Meadows]. *Delphi* issues low-entropy verdicts that ignore controversy and skews left — a warning against single-ground-truth moral classifiers [2023-Rystrøm].

## E. Design lessons

1. **Preserve the full disagreement distribution; never ship majority-vote labels as ground truth.** Report per-annotator ratings and treat the distribution as the target [2026-Li-PluriHarms; 2025-Sorensen; 2022-Ziems; 2024-Susanto; 2024-Arzberger; 2024-Park].
2. **Record annotator identity + validated psychometrics (Schwartz, MFQ, IRI, political leaning) as first-class metadata** so downstream users can reweight and audit whose values are encoded [2026-Li-PluriHarms; 2022-Ziems; 2024-Susanto; 2024-Arzberger].
3. **Report per-framing leaderboards, not one number, when the aggregation rule is contested; make intervention stage / group granularity / notion selectable axes** [2024-Defrance; 2023-Boddington].
4. **Use group-aware consensus (not raw majority) to protect minority clusters** when a single artifact is required [2024-Huang].
5. **Disclose what the values are and whose they are; downgrade "ethics" claims to "accords with population X"** [2025-LaCroix; 2020-Gabriel; 2025-Vishwanath].
6. **Over-sample the ambiguous middle and treat harm × agreement as orthogonal axes** to avoid ceiling/floor saturation [2026-Li-PluriHarms; 2025-Li-Cognitive].
7. **Allow "incomparable" as a valid response and test whether models confabulate rankings** for genuinely incommensurable values [2025-Benavoli; 2024-Zhi-Xuan].
8. **Build locale-specific axes and proxies (Region, Caste, Afro-relational trust, Maqasid, Ubuntu, Cultural Theory); validate with "what does X mean to you" probes and native annotators** [2022-Shaily Bhatt; 2025-Amugongo; 2022-Gwagwa; 2025-Li-Cognitive; 2022-IslamicVirtue; 2024-Lee].
9. **Administer the identical instrument to humans and LLMs on the same scale, with human-to-human same/opposite-culture baselines; use leave-one-dimension-out and within-respondent z-scoring to localize gaps** [2025-Shen; 2025-Haslett; 2023-Wang].
10. **Do not equate official-media/state-defined values with "a nation's values"; avoid one model family for generation + filtering + judging (circularity)** [2025-Ju; 2025-Wu; 2025-Han; 2025-Li-Cognitive].
11. **Audit source and annotator demographic coverage (uncounted/unaccounted/discounted); flag the ~33% offline population** [2022-Gwagwa; 2023-Ji; 2024-Arzberger; 2025-Perera].
12. **Score refusal as a distinct outcome; separate template-refusal from substantive safe engagement** [2024-Meadows; 2025-Han].
13. **Include contrastive head-to-head items (competing norms + distractor) to reveal which norm a model prefers; use panel divergence to isolate discriminating items** [2025-Wu; 2025-Neuman].
14. **Guard against sycophancy with adversarial items where the correct answer conflicts with the user's stated view** [2025-Lindstrom].
15. **Treat panel/population composition as an experimental variable** [2025-Zohny; 2024-Tennant].
16. **Ground normative content in a declared, traceable framework (law, EU AI Act, doctrine, cultural theory) with explicit per-item justification** [2026-Kolt; 2025-Nay; 2024-Guldimann; 2025-Vishwanath].
17. **Surface saturated/"dead" benchmarks (uniform ceiling scores) as evidence a metric is broken** [2024-Guldimann].

Additional framings worth encoding: the tetradic AI/user/developer/society model with 8 failure modes [2024-Gabriel-Ethics of Advanced AI Assistants]; a universal moral-threshold floor plus local cultural layer [2025-Yaacov]; ethical-adversarial examples exploiting gaps in a benchmark's moral variety [2019-Aliman].
