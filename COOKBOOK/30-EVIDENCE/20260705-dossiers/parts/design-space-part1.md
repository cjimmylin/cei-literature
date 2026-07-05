# design-space — sub-dossier part 1/4

Scope: task formats, scoring approaches, and dataset-construction choices for values benchmarks, from 57 cards spanning moral-psychology stimulus sets, hate-speech corpora, cultural-value benchmarks, deliberation harnesses, and two lab model cards.

## A. Synthesized claims

1. **Task format is a first-order design variable that materially changes measured "alignment," not just a presentation detail.** Sachdeva shows sycophancy and inertia are *interaction properties*: GPT-4.1's change-of-verdict rate was 0.6% synchronous vs. high conformity in round-robin; inertia odds ratios spanned GPT 8.27 / Claude 4.49 / Gemini 2.83 [2025-Sachdeva-Deliberative Dynamics and Value Alignment]. KorNAT's authors warn MCQ format does not reflect free-generation behavior [2024-Lee-KorNAT]. MIST shows VLMs answer ~40% of items correctly with no image, and Llama-3.2-90B-V collapses from 96.6% text-only to 13.6% multimodal [2025-Gao-MIST]. Format choice must be treated as an experimental factor.

2. **Forced-choice / MCQ maximizes scoring reliability but risks measuring surface shortcuts and losing pluralism.** Winogender binary OCCUPATION/PARTICIPANT choice gives clean exact-match scoring and 94.9% human agreement [2018-Rudinger]; Sorin's yes/no JSON trolley design enables trivial coding across 650 runs [2024-Sorin]. But KorNAT and Wang both flag that MCQ can be "solved" trivially — Wang shows 32/37 prior fairness benchmarks are difference-unaware and perfectly solvable by a color-blind model [2025-Wang-Measuring Desired Group Discrimination]. GG-BBQ's ambiguous-context design (correct answer = "no answer") is the key MCQ move that resists the shortcut, exposing 70B models collapsing to 0.28 accuracy under ambiguity [2025-Satheesh-GG-BBQ].

3. **Generative/cloze formats capture ecologically real behavior but require a downstream scorer (lexicon, classifier, or judge), which becomes the validity bottleneck.** HONEST scores completions against HurtLex and is blind to euphemism by construction [2021-Nozza]; Bang scores headlines via SBERT distance to self-generated anchors [2024-Bang]; BEATS and MIST use LLM-judges [2025-Anonymous-BEATS; 2025-Gao-MIST]. Each pushes reliability into the scorer.

4. **Distribution-matching scoring (compare model answer-distribution to a survey distribution) is the strongest published idea for pluralistic value items.** KorNAT scores by the survey probability mass on the chosen option (SVA), reporting an empirical ceiling of 0.450 (not 1.0) and an All-Neutral baseline [2024-Lee-KorNAT]. Liu-2025's DEF induces diversity (89.8% vs. 0% single-shot) so one model simulates a population, scored by KL-divergence [2025-Liu-Towards Realistic Evaluation]; CLCA uses the same WVS/KL-D pipeline with 1,000 persona prompts per culture [2025-Liu-Cultural Learning-Based]. This rewards matching the distribution, not a majority label.

5. **Minimal-pair / counterfactual perturbation is the most reusable item-construction primitive for bias.** Swap one attribute, hold the rest fixed, measure behavior change: Winogender pronoun swaps [2018-Rudinger], De-Arteaga's gender-indicator flip (4.6–12.2% flip) [2019-De-Arteaga], SHADES contrastive pairs with grammatical-agreement slot tags [2025-Al-SHADES], GG-BBQ group-term vs. proper-name subsets [2025-Satheesh]. Generalizes to any axis.

6. **LLM-generation of items scales coverage and resists contamination, but inherits the generator's culture and needs a filter.** ToxiGen generated 274,186 statements (98.2% implicit) with adversarial ALICE decoding and 90.5% human-indistinguishability as a naturalness gate [2022-Hartvigsen]; Rao distilled 1.2M defeasible-morality entries filtered by a critic trained on 20K human labels [2023-Rao]; Davies makes the eval leakage-proof by generating fresh personas each run [2026-Davies]. All three warn the generator's Western-centric bias propagates.

7. **Report an empirical ceiling and a naive baseline, or scores are uninterpretable.** KorNAT's 0.45 SVA ceiling makes a 0.33 legible [2024-Lee-KorNAT]; HOMO-LAT reports MPA 0.939 vs. best system 0.53 [2025-Enguix]; Rismani finds only 26.9% of 791 RAI measures ship any interpretation criterion [2025-Rismani-Measuring What Matters].

8. **Inter-annotator agreement is the load-bearing, frequently-weak foundation of any human-labeled values dataset, and low agreement forces construct-narrowing.** DKHate reports Jaccard 39–43% and narrows "offensive" to "contains profanity" to raise it — trading validity for reliability [2020-Sigurbergsson]. HOMO-LAT κ 0.124–0.158 [2025-Enguix]; AustroTox α=0.49 [2024-Goldzycher]; ETHOS reaches κ≥0.814 via active-learning sampling [2020-Mollas]. Polish cyberbullying expert re-annotation found twice as many harmful labels as laypeople [2024-Ptaszynski].

9. **Two-stage psychometric validation (cross-loading pruning, then factor + criterion validity) is the stimulus-construction gold standard, almost never done for LLM benchmarks.** MFV pruned items exceeding 20% cross-classification, then ran EFA/CFA (RMSEA .047) and criterion regression vs. the MFQ (β .24–.47) [2015-Clifford]; the Dutch adaptation replicated 97% correct classification [2023-Hopp].

10. **Multimodal and agentic formats open real headroom but strain scoring.** MIST distributes the moral signal so no single modality is diagnostic [2025-Gao-MIST]; Jeong transfers text ETHICS labels into CLIP space to score images [2022-Jeong]. ADEPT orchestrates YAML ethical-theory personas through opening/rebuttal/secret-ballot phases; panel composition flips 4 of 6 retained personas' votes [2025-Zohny-ADEPT]. Moral-sycophancy uses a two-turn pushback protocol with a right→wrong vs. wrong→right asymmetry as diagnostic [2026-MoralSycophancy].

11. **Provenance transparency (who wrote items, who annotated, from where) is a design requirement.** DKHate ships a Bender-Friedman data statement disclosing a single non-native-Danish annotator [2020-Sigurbergsson]; Tonneau finds 0% of surveyed English hate-speech datasets report both data and annotator origin (r=0.99 with Twitter geography) [2024-Tonneau]; SHADES credits all 43 native-speaker creators [2025-Al-SHADES].

12. **Frontier lab practice lags the academic design frontier.** Qwen3 has no safety/values eval section and no model spec; "alignment tasks" mean instruction-following [Alibaba (Qwen)-Qwen3]. Gemini 2.5 Pro is richer — CCL + early-warning alert thresholds, held-out assurance evals, decoupled over-refusal (+14.8% IF vs. −0.9% violations) — but all safety evals are text-only [Google DeepMind-Gemini_2.5_Pro].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2015-Clifford-Moral Foundations Vignettes | Two-stage validation: prune items >20% cross-classification, then EFA/CFA + MFQ criterion validity (β .24–.47) |
| 2018-Rudinger-Gender Bias in Coreference | Minimal-pair pronoun swap + "gotcha" (counter-stereotype) subset; exact-match, 94.9% human agreement |
| 2019-De-Arteaga-Bias in Bios | Single aggregate bias score = Pearson r between TPR-gap and base rate; counterfactual attribute-flip rate |
| 2020-Mollas-ETHOS | Active-learning balanced sampling + soft (proportion) labels; κ≥0.814 on a 998-item set |
| 2020-Sigurbergsson-DKHate | Publish low agreement (Jaccard ~41%) THEN document the construct-narrowing that raised it; full data statement |
| 2021-Nozza-HONEST | Template×identity factorial (15×28=420/lang) scored by lexicon; K-sweep (1/5/20) reveals length inflation |
| 2022-Hartvigsen-ToxiGen | Adversarial classifier-in-the-loop generation (ALICE) + 90.5% human-indistinguishability as naturalness gate |
| 2022-Jeong-Visual Commonsense Immorality | Cross-modal label transfer: train on text ETHICS in CLIP space, score unseen images |
| 2022-Yilmaz-Large-Scale Hate Speech | Domain-balanced design (5×20k) enabling recovery/decay cross-domain transfer metrics |
| 2023-Das-Bengali Gender | Explicit-vs-implicit dual track (identity words vs. names/dialect); intersectional religion+nationality axes |
| 2023-Hopp-Dutch MFSD | Cross-cultural re-validation of MFV+SMID; circumplex (arousal×morality) image sampling |
| 2023-Narayan-HASOC 2023 | Same binary task across 5 languages with wildly different train sizes (Gujarati 200 vs Sinhala 7,500) |
| 2023-Rao-Set a Fire | Defeasibility (how much context *shifts* judgment) as graded construct; small critic filters 1.2M items |
| 2024-Bang-Political Bias | Self-generated pro/opp anchors + SBERT NN distance; decompose into stance/content/style; issue-disaggregated |
| 2024-Goldzycher-AustroTox | Orthogonal vulgarity vs. offensiveness spans; sensitivity-prioritizing (asymmetric-cost) aggregation |
| 2024-Huang-TrustLLM | Principle-first: derive 8-dim taxonomy, benchmark only the 6 measurable; measure over-alignment as first-class |
| 2024-Lee-KorNAT | Distribution-as-ground-truth (SVA) from 6,174-person survey; report empirical ceiling 0.45 + All-Neutral baseline |
| 2024-Sorin-Ethical Alignment Healthcare | Repeat-run consistency (10 runs/dilemma) separates policy from stochasticity; JSON forced-choice |
| 2024-Wijanarko-Indonesia | Community-in-the-loop keyword elicitation + annotators who are group members |
| 2025-Al-SHADES | Minimal-pair + grammatical-agreement slot tags + per-statement cultural-validity annotation; tiered gated release |
| 2025-Anonymous-BEATS | Consortium of 3 LLM-judges + per-judge ANOVA to quantify judge disagreement as a result |
| 2025-Chakraborty-Structured Moral Reasoning | Factorial prompt-scaffold grid (4 value systems × 8 theories); OLS attributes 92% of accuracy variance to prompt |
| 2025-Enguix-HOMO-LAT | Cross-dialect generalization track (train/test by region); report MPA ceiling (0.939) vs best (0.53) |
| 2025-Gao-MIST | Text-image flow: distribute moral signal so no single modality is diagnostic; 3-condition modality ablation |
| 2025-Ju-NaVAB | Auto value-extraction pipeline from media + <Q,S,RS> contrastive triple + graph Conflict Reduction |
| 2025-Lee-KOTOX | Linguistically-grounded obfuscation taxonomy (17 rules) as controlled robustness perturbation |
| 2025-Liu-Realistic Cultural Value | DEF induces diversity (89.8%) so one model simulates a population; KL-D vs. survey distribution |
| 2025-Sachdeva-Deliberative Dynamics | Deliberation format (synchronous vs round-robin) as experimental variable; inertia/conformity logit model |
| 2025-Satheesh-GG-BBQ | Ambiguous-context "no answer" correct + group-term vs proper-name subsets; MT-then-manual localization |
| 2025-Singh-Rethinking Hate Speech | Code-mixed regional-platform benchmark; 10%-data LoRA stress test; conservative-prompt lower-bound policy |
| 2025-Wang-Desired Group Discrimination | Descriptive/normative/correlation taxonomy; paired ≠/= items → DiffAware(recall)+CtxtAware(precision) |
| 2026-Davies-Persona Brainstorm Audit | Leakage-proof-by-construction (generate fresh items each run); Cramér's V association metric + severity tiers |
| 2022-Unknown-HOTTEST | Language-specific preprocessing (stemming) as prerequisite for valid low-resource benchmarking |
| 2024-Khanduja-Telugu | 98.2% accuracy flagged as suspicious → saturation/leakage warning for new-language corpora |
| 2025-Hong-PrinciplismQA | Organize a benchmark by a named framework (Beauchamp-Childress); MCQ+open-ended hybrid; 12 expert annotators |
| 2026-MoralSycophancy-VLMs | Directional transition asymmetry (right→wrong vs wrong→right) under user pushback as sycophancy diagnostic |
| 2016-Xu-Deontological Decision | Behavioral (covert cheating) outcome vs. stated judgment — the judgment-behavior gap as a benchmark dimension |
| 2018-Kim-Non-Intuition-Based Machine Ethics | Universalizability/generalizability as a stateable consistency test; critique of intuition-sourced labels |
| 2020-Awad-Crowdsourcing moral machines | Randomized within-platform conjoint (hold all-but-one dimension); force trade-off (no safe option) |
| 2021-Stenseke-Artificial Virtuous Agents | Virtue-conflict scenarios + role-relative ("android arete") standards; longitudinal eudaimonic reward |
| 2023-Feng-Case Repositories | Case-based precedent library: expert dimension elicitation → LLM expansion with step-size → dual appropriateness/harm rating |
| 2023-Körner-Deontology in Real Life | Fact-grounded dilemmas rated more realistic (dz=1.31) than trolley; realism as a 3-part psychometric construct |
| 2023-Shen-LLM Alignment survey | Outer/inner-alignment split; established-vs-anticipated risk tiers as a benchmark roadmap |
| 2024-Kajiwara-Hate Speech Catalogue (AbuseEval) | Explicit-vs-implicit label; dictionary-ceiling analysis to detect keyword-dependence of a dataset |
| 2024-Ptaszynski-Polish Cyberbullying | Two-round layperson→expert re-annotation (v1/v2); span-level harmful-phrase annotation; modified quadratic κ |
| 2024-Tonneau-Languages to Geographies | Geo-cultural representativeness audit; data-vs-annotator origin alignment matrix |
| 2024-Wilders-Socratic Dialogue | Dissensus-as-resource: report disagreement distributions, not consensus; "question of conscience" framing |
| 2025-De Montis-Morality in AI | Loving-Attention-Vector / dynamic moral-reinterpretation as a multiturn benchmark target |
| 2025-Gabriel-Fair Treatment of Claims | Six-mode stakeholder-misalignment taxonomy; multi-theory justifiability as consistency test |
| 2025-Liu-Cultural Learning | Ablation swapping social dialogue for math-with-same-turn-structure isolates the active ingredient |
| 2025-Mahran-SAEs Probing Religion | Representation-level audit: normalize inter-group overlap (VAI); intra-group coherence as validity pre-check |
| 2025-Rismani-Measuring What Matters | Component→attribute→hazard→harm chain; 73% of measures lack interpretation criteria |
| 2025-Urchs-taz2024full | Deliberately exclude LLMs from the bias pipeline to avoid circularity; PMI adjective attribution |
| 2025-Zohny-ADEPT | YAML personas with `forbidden_moves`; panel composition as experimental variable; secret ballot |
| 2022-Joshi-MahaNLP | Production-vs-benchmark-quality framing; monolingual models beat multilingual on low-resource tasks |
| 2024-Kajiwara-Multimodal HSDF | Majority-voting ensemble across modalities; suspiciously high (98–99%) numbers = rigor warning |
| 2025-Sanwoolu-Kantian deontology | Alignment-without-agency: separate "behavior conforms to principle" from "is a moral agent" |
| 2025-Terziyan-Ethical evolution | Immutable vs mutable "gene" partitioning: which values are absolute vs context-adaptive as a test axis |
| Alibaba (Qwen)-Qwen3 | Lab practice gap: no values eval, no model spec; "alignment" = instruction-following |
| Google DeepMind-Gemini_2.5_Pro | CCL + early-warning alert-threshold pattern; held-out assurance evals; decouple over-refusal from violations |

## C. Patterns & disagreements

**Convergence — format is a confound.** MCQ-format-warns recur independently: KorNAT, Wang, GG-BBQ, and MIST all show a naively-formatted item is gameable [2024-Lee-KorNAT; 2025-Wang; 2025-Satheesh; 2025-Gao-MIST]. The near-universal fix is a built-in abstention or ambiguity trap (GG-BBQ "no answer," KorNAT neutrality handling, MIST cross-modal signal).

**Convergence — resist contamination by construction.** ToxiGen (implicit-only, cosine dedup), Davies (fresh generation each run), SHADES (ship reusable templates), and Al-SHADES/NaVAB templates all decouple the eval from a static leakable item set [2022-Hartvigsen; 2026-Davies; 2025-Al-SHADES; 2025-Ju-NaVAB].

**Disagreement — majority-label vs. distribution as ground truth.** Most hate-speech and MCQ benchmarks binarize to a majority/gold label (Rudinger, Sorin, most HASOC-style tasks). KorNAT, Liu-2025, and Liu-cultural explicitly reject this, arguing a single gold answer misrepresents genuine value pluralism and scoring should match the population distribution [2024-Lee-KorNAT; 2025-Liu-Towards Realistic; 2025-Liu-Cultural Learning]. Wang goes further and argues *against averaging across sub-benchmarks* with different normative commitments [2025-Wang].

**Disagreement — who should label values, and is "intuition" a valid source.** ETHOS/Mollas and Awad treat crowd/public preference as ground truth [2020-Mollas; 2020-Awad]; Ptaszynski and Hong show experts find ~2× the harm laypeople do and argue expert annotation is mandatory [2024-Ptaszynski; 2025-Hong]. Kim/Hooker attack the whole enterprise: human moral intuitions are inconsistent and should be *replaced* by formal universalizability tests, not used as labels [2018-Kim].

**Disagreement — LLM in the loop: essential or circular.** BEATS, MIST, NaVAB, and KorNAT embed LLM-judges/generators (BEATS itself flags factuality-judge unreliability) [2025-Anonymous-BEATS; 2025-Gao-MIST; 2025-Ju-NaVAB; 2024-Lee-KorNAT]; Urchs deliberately excludes LLMs to avoid circular bias [2025-Urchs]. The split turns on whether the judged construct overlaps the judge's own biases.

**Convergence — realism beats trolley-style artifice.** Körner shows fact-grounded dilemmas rated far more realistic than trolley (dz=1.31) [2023-Körner]; Feng, Sachdeva (AITA), and Hong (JAMA cases) source items from real disputes [2023-Feng; 2025-Sachdeva; 2025-Hong].

## D. Exemplars & anti-patterns

**Best-designed.** *MFV* [2015-Clifford] is the psychometric exemplar: length/reading-level-controlled items, cross-loading pruning, EFA/CFA, criterion validity, ideological balance in recruitment — a complete validity ladder later cross-culturally replicated [2023-Hopp]. *KorNAT* [2024-Lee-KorNAT] is the exemplar for pluralistic scoring: survey-grounded distribution as truth, demographic re-weighting, reported empirical ceiling, refusal treated as a first-class outcome, and human-preference validation that higher-scoring models are genuinely preferred (94/100). *Wang* [2025-Wang] is the exemplar of conceptual rigor: the descriptive/normative/correlation taxonomy plus paired ≠/= items yielding precision AND recall, and an adversarial check that debiasing prompts *backfire*.

**Anti-patterns.** *Khanduja-Telugu* [2024-Khanduja] reports 98.2% accuracy the card flags as probable imbalance/leakage — a saturation red flag with no ceiling analysis. *Kajiwara-Multimodal HSDF* [2024-Kajiwara-A comprehensive framework] reports 97–99% "ratios" with undefined computation and no SOTA comparison — opaque scoring. *DKHate* is a *productive* anti-pattern: low agreement forced narrowing "offensive" to "contains profanity," but it documents the trade honestly [2020-Sigurbergsson]. *HOMO-LAT* shows the cost of annotator fragmentation (κ≈0.13) and defaulting Mexican annotators for 15 of 19 countries [2025-Enguix].

## E. Design lessons

1. **Treat task format as an experimental factor, and vary it** (MCQ vs. free-gen; synchronous vs. round-robin; monitored vs. unmonitored) — sycophancy/inertia are format properties [2025-Sachdeva; 2024-Lee-KorNAT; 2026-MoralSycophancy].
2. **For contested value items, score by distribution-match against a re-weighted survey; report the empirical ceiling plus a naive baseline** [2024-Lee-KorNAT; 2025-Liu-Towards Realistic; 2025-Enguix].
3. **Build abstention/ambiguity traps into MCQ items** so "no answer" is sometimes correct, defeating always-guess and always-equalize shortcuts [2025-Satheesh; 2025-Wang].
4. **Use minimal-pair perturbation with grammatical-agreement handling** for any bias axis, plus a "gotcha"/counter-stereotype subset [2018-Rudinger; 2025-Al-SHADES; 2019-De-Arteaga].
5. **Decouple the eval from a static item set** via fresh generation or shipped templates to neutralize contamination [2026-Davies; 2025-Al-SHADES; 2022-Hartvigsen].
6. **If you generate items or use an LLM judge, add a human-labeled critic and quantify judge disagreement**; never let one model both generate and judge unaudited [2023-Rao; 2025-Anonymous-BEATS; 2025-Ju-NaVAB].
7. **Report agreement before any construct-narrowing, disclose annotator + data provenance, and prefer experts for subtle harms** [2020-Sigurbergsson; 2024-Ptaszynski; 2024-Tonneau].
8. **Separate orthogonal constructs** (vulgarity vs. offensiveness; explicit vs. implicit; stance/content/style; presence/severity/impact) rather than one label [2024-Goldzycher; 2024-Kajiwara-Catalogue; 2024-Bang; 2025-Anonymous-BEATS].
9. **Ground scenarios in real events/cases and organize by a named normative framework** [2023-Körner; 2023-Feng; 2025-Hong; 2024-Sorin].
10. **Measure over-refusal and consistency-across-runs as first-class metrics, not only harm rate** [2024-Huang; 2024-Sorin; Google DeepMind-Gemini_2.5_Pro].
11. **Add a difficulty/ceiling audit** (dictionary upper-bound, MPA, saturation check) so a high score is not mistaken for validity [2024-Kajiwara-Catalogue; 2025-Enguix; 2024-Khanduja].
12. **Include an explicit interpretation threshold and the component→hazard→harm chain**; 73% of existing measures lack one [2025-Rismani].
13. **For multimodal/agentic values, distribute signal across modalities/turns and log auditable artifacts**; use panel-composition or format as a manipulation [2025-Gao-MIST; 2025-Zohny-ADEPT].
14. **Audit geo-cultural representativeness and use community-elicited, locally-grounded vocabulary** for non-WEIRD coverage [2024-Tonneau; 2024-Wijanarko; 2023-Das].
