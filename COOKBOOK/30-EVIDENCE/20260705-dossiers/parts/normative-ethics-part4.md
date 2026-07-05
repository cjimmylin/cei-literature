# normative-ethics — sub-dossier part 4/6

Scope note: 57 cards spanning operationalized moral/ethics benchmarks, multilingual hate-speech/bias datasets encoding normative violations, medical/nursing ethics benchmarks built on named frameworks, interpretability probes of moral representations, and theoretical papers arguing for specific normative foundations. The through-line: *how* a normative theory becomes scorable items.

## A. Synthesized claims

1. **Theory-guided prompting measurably changes moral judgment, and the change size is itself a diagnostic.** Injecting an explicit moral theory as CoT guidance raised GPT-4 accuracy 18.7% on theory-guided datasets and LLaMA2 7.8% (p.7); GPT4-DEONT reached 79.3 vs 68.6 for the best SFT baseline [2024-Zhou-Rethinking Machine Ethics]. The same "policy-in-prompt" architecture underlies Rao's iterative work and its multilingual extension [2023-Rao-Set a Fire; 2024-Agarwal-Ethical Reasoning Depends on Language]. Framework can be a *manipulated variable*, not a fixed key.

2. **Moral judgment is strongly language-dependent — a "foreign-language effect."** GPT-4 fell 93.3% (EN) → 62.7% (Hindi) on ethical-policy resolution; Llama2-70B 78.0% → 41.2% (Swahili); worst on Hindi/Swahili, best on English/Russian [2024-Agarwal]. MULTITP corroborates at scale: 98,440 vignettes × 107 languages, only 3/19 models misalign below 0.6 (max 2.45) [2024-Jin-Multilingual Trolley]. UNIMORAL shows the same order — best English/Spanish/Russian, worst Arabic/Hindi [2025-Kumar-Are Rules Meant to be Broken].

3. **LLMs systematically overweight "individualizing" moral foundations and underweight "binding" ones relative to a human baseline, and this gap widens with capability.** Across 21 models from six providers, all overvalued care/fairness/liberty and undervalued authority/loyalty/sanctity vs a US baseline; more capable and recent models cluster *further* from the human baseline in PCA space, with loyalty the largest divergence [2024-Kirgis-Moral Foundations]. This is a directional bias in framework coverage, not random noise.

4. **Reasoning/utilitarian tilt rises with newer "reasoning" models, but consistency is low.** In medical trolley dilemmas, GPT-o1-preview gave utilitarian answers 44% of the time and Qwen-2-7B 80%, yet all 13 models unanimously refused organ harvesting (0% utilitarian) and unanimously endorsed mandatory vaccination (100%) — i.e., models converge on extreme cases and scatter on genuine dilemmas [2024-Sorin-Ethical Alignment in Healthcare]. Repeat-run frequency (10 runs/dilemma) exposes this stochasticity that a single response hides.

5. **Fairness metrics are covertly committed to a normative theory.** 12 of 14 group-fairness metrics rely on model errors (utilitarian/disparate-impact); only 2 on model behavior (deontological/disparate-treatment) [2023-Mougan-Kantian Deontology]. Choosing a metric silently chooses consequentialism vs deontology; outcome-disparity-only benchmarks are implicitly utilitarian.

6. **Mainstream alignment methods themselves encode utilitarian preference-maximization even when labeled otherwise.** RLHF, RLAIF, and nominally-deontological Constitutional AI reduce to aggregate preference maximization, abstracting away situated/relational moral facts; Ethics of Care is proposed as corrective [2025-El Masri-Towards Attuned AI]. Reward models inherit demographic tilt: relative alignment *rankings* across groups are consistent across 7 open RMs even when absolutes vary (Spearman 0.67, p<0.001) [2025-Elle-Reward Model Perspectives].

7. **Empirical human-preference alignment is statistically fragile.** Modeling alignment as inference on a self-selected human sample imports survey biases (non-response, response bias, reflexivity); raters preferred one system 66/34 on coherence though it scored *lower* on MAUVE (87.16 vs 82.82) [2025-Rodemann-Statistical Case Against]. Validity ≠ accuracy.

8. **Named normative frameworks scaffold the strongest applied-ethics benchmarks.** PrinciplismQA organizes 3,648 questions (2,182 MCQ + 1,466 open) around Beauchamp-Childress' four principles, 350 textbook/JAMA sources, 12 expert annotators; beneficence is hardest [2025-Hong-PrinciplismQA]. NurValues distills five nursing-code values from 1,100 ethnographic instances; Justice is hardest, Hard-Level macro-F1 collapses 56 pts to 32.29 under adversarial dialogue [2025-Yao-NurValues]. MedEthicEval partitions items by dilemma type (violation/priority/equilibrium), each scored differently [2025-Jin-MedEthicEval]. Bian's 12,000-item Healthy-China-2030 benchmark grounds a 20-dimension ethics×safety taxonomy in national regulation; fairness/bias-mitigation stays ~60% even after fine-tuning [2025-Bian-Healthcare Ethics QA China].

9. **Minimal-pair / counterfactual construction isolates a value signal and repeatedly surfaces bias.** GenMO's 908 gender-swapped pairs show every production LLM biased, all favouring female protagonists 63–88% of mismatches (Claude3-Opus lowest, 10.46%) [2024-Bajaj-GenMO]. Anthropic's demographic-parity swaps flip a 175B model from -3% to +7% under instruction [Anthropic-Moral_Self-Correction]. NurValues polarity-flips each instance into a value-violating twin [2025-Yao]; RuBia/Kurpicz-Briki use pro/anti-trope and WEAT pairs [2024-Grigoreva; 2020-Kurpicz-Briki].

10. **Culturally-native items — not translations — are required for valid non-English moral evaluation.** WEAT biases only partly transfer: career bias replicates in German (d=1.62) but math/science does not (p=0.65) [2020-Kurpicz-Briki]. Culture-specific stress subsets reveal masked gaps: eJCM lifts Japan-specific F1 0.681→0.756, closing the GPT-4 gap to 3.1 pts [2024-Ohashi]; specifying the cultural community moves GPT-4 84.7%→88.9% [2024-Zhou]. MUDES scored F1=12.8 on Korean spans vs 40.6 native [2022-Jeong-KOLD].

11. **Structured, multi-field annotation beats binary labels.** Social Bias Frames' 150k tuples encode offense+intent+group+free-text stereotype across 1,414 groups [2020-Sap]; SafetyAnalyst uses a stakeholder→action→effect harm-benefit tree with 28 interpretable weights [2025-Li]; UNIMORAL scores a 6-stage pipeline to localize *where* reasoning fails [2025-Kumar]. Only ~59–65% of offensive OLID messages carry explicit markers, so implicit abuse is where detection fails [2024-Kajiwara].

12. **Inter-annotator agreement on moral/offense labels is often low; expertise and hierarchy raise it.** Portuguese binary hate: Fleiss κ=0.17 (non-expert) vs Cohen κ=0.72 (expert/hierarchical) [2019-Fortuna]; κ rose 0.61→0.86 after adjudication [2024-Kajiwara]; NurValues κ=0.73 with 5 nurses [2025-Yao]. Subjective norms demand expert adjudication and disagreement reporting, not majority collapse [2024-Wilders].

13. **Modality and adversarial framing bypass moral safety.** Visual inputs push VLMs into System-1: they lose numerical-stakes sensitivity, prioritize self-interest, collapse hierarchical values, bypassing text safety [2026-PKU]. Adversarial re-framing erodes compliance [2025-Jin-MedEthicEval; 2025-Tereshchenko]; MULTITP drops 25.9% under GCG-T red-teaming [2024-Jin].

14. **Interpretability confirms values are sparse, localized, causally manipulable.** Value neurons are <0.4% of LLaMA-3.1-8B, ~layer 15 [2025-Su]; a 104K-param transformer hits 77% on Moral Machine, 45/256 neurons causally scoring, legality vs species bias in different layers [2026-Goel]; MFT dimensions map to distinct neuron sets [2025-Schacht]. Ablation gives causal, not correlational, evidence.

15. **Non-Western frameworks are operationalizable as reward/eval targets.** Dharmic ethics as GRPO rewards cut violation 34%→4% [2025-Madan]; ubuntu, Islamic trusteeship, and Shinto eco-relational ethics supply dimensions absent from WEIRD benchmarks [2024-Mokoena; 2025-Ali; 2024-Puzio; 2020-Galanos]. Failure mode: models default general norms to the dominant religion (88.8% of Hindu norms → Islam in Bengali) [2025-Hossain-BRAND].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2024-Zhou-Rethinking Machine Ethics | Theory-guided CoT lifts GPT-4 +18.7% on theory datasets; framework can be a manipulated variable (p.7). |
| 2024-Agarwal-Ethical Reasoning Depends on Language | GPT-4 moral accuracy 93.3% EN → 62.7% Hindi; separate "bias" vs "confusion" failure modes (p.8). |
| 2024-Jin-Multilingual Trolley | 98,440 trolley vignettes × 107 languages; only 3/19 models misalign <0.6/2.45; -25.9% under red-team (p.5,7,13). |
| 2024-Kirgis-Moral Foundations | LLMs overweight care/fairness/liberty, underweight authority/loyalty/sanctity; gap grows with capability (p.6). |
| 2024-Sorin-Ethical Alignment Healthcare | Run each dilemma 10×; utilitarian rate 44% (o1) to 80% (Qwen); unanimous on extreme cases (p.16-17). |
| 2023-Mougan-Kantian Deontology | 12/14 fairness metrics utilitarian (error-based); only 2 deontological (behavior-based) (p.8). |
| 2025-El Masri-Towards Attuned AI | RLHF/RLAIF/Constitutional AI all reduce to utilitarian preference-max; propose Ethics of Care (p.4). |
| 2025-Elle-Reward Model Perspectives | RM demographic alignment *rankings* consistent across 7 RMs (Spearman 0.67) even as absolutes vary (p.5). |
| 2025-Rodemann-Statistical Case | Human raters prefer 66/34 the system that scores lower on MAUVE; validity ≠ accuracy (p.10). |
| 2025-Hong-PrinciplismQA | 3,648 Q on Beauchamp-Childress 4 principles; beneficence hardest; 12 expert annotators. |
| 2025-Yao-NurValues | Polarity-flipped twins + adversarial Hard tier drops macro-F1 56→32.29; Justice hardest (p.7). |
| 2025-Jin-MedEthicEval | Partition items into violation / priority-dilemma / equilibrium-dilemma, each scored differently (p.4). |
| 2025-Bian-Healthcare QA China | 12,000 items, 20-dim ethics×safety taxonomy grounded in national policy; fairness stuck ~60% (p.4). |
| 2024-Bajaj-GenMO | 908 gender-swapped story pairs; all LLMs favour female 63–88%; Claude3-Opus lowest 10.46% (p.7-8). |
| Anthropic-Moral_Self-Correction | "Please be unbiased" instruction flips 175B from -3% to +7%; self-correction emerges at 22B (p.1-3). |
| 2020-Kurpicz-Briki | WEAT biases only partly transfer (career d=1.62; math p=0.65); use culture-native word lists (p.9). |
| 2024-Ohashi-eJCM | Culture-specific stress subset: Japan-specific F1 0.681→0.756, closing GPT-4 gap to 3.1 pts (p.4). |
| 2022-Jeong-KOLD | Multilingual MUDES F1=12.8 on Korean spans vs 40.6 native; +13.1 F1 from title context (p.7-8). |
| 2020-Sap-Social Bias Frames | 5-field structured frame (offense+intent+group+free-text stereotype) over binary toxicity (p.5). |
| 2025-Li-SafetyAnalyst | Judgment = stakeholder→action→effect tree with 28 re-optimizable interpretable weights (p.4). |
| 2025-Kumar-UNIMORAL | Person-conditioned ground truth (annotator's MFQ2/VSM persona); 6-stage reasoning pipeline (p.3,6). |
| 2024-Kajiwara-AbuseEval | Only 59–65% of offensive messages are explicit; build separate implicit/explicit test sets (p.7). |
| 2019-Fortuna-Portuguese Hate | Rooted DAG (multi-parent) label ontology; expert κ=0.72 vs non-expert κ=0.17 (p.4-5). |
| 2026-PKU-Visual Distraction | Visual inputs trigger System-1, lose numerical-stakes sensitivity, bypass text safety (abstract). |
| 2025-Su-Value Neurons | Value neurons <0.4% of model, concentrated ~layer 15; generative > MCQ for value measurement (p.7). |
| 2026-Goel-Interpretable Moral | 104K-param transformer, 77% on Moral Machine; legality vs species bias localize to different layers (p.5). |
| 2025-Schacht-Moral Circuits | MFT-aligned neuron probing + ablation; care/sanctity largest neuron sets, fairness/loyalty fewest (p.2). |
| 2025-Madan-ArGen | Dharmic reward (Ahimsa/Dharma) via GRPO cuts violation 34%→4%; live policy hot-swap (p.23). |
| 2025-Hossain-BRAND | Models default general norms to dominant religion (88.8% Hindu→Islam, Bengali); Scope dimension (p.9). |
| 2023-Rao-Set a Fire | Defeasible moral reasoning: measure how much *context shifts* a baseline judgment; critic-model filter (p.3). |
| 2023-Catapang-EMoTES-3K | Mixed-intent scenarios (good action/bad intent) as a hard probe of intent vs surface reasoning (p.3). |
| 2024-Grigoreva-RuBia | Grammatical-gender morphology as an independent bias signal invisible in English (p.1). |
| 2022-Ramponi-Religious Hate | Five-level taxonomy mapped onto prior schemes for interoperability; form labels (animosity/derogation) (p.15). |
| 2025-Tereshchenko-Gaps | Relative Danger Coefficient: tiered G/U/P/D response taxonomy + behavioral penalty terms (p.13). |
| 2025-Iftikhar-LLM Counselors | 15-violation taxonomy mapped to APA/ACA/NASW codes; 18-month ethnographic evaluation (p.1,3). |
| 2025-Yaacov-Moral Pluralism | Moral *threshold* (excludes unreasonable args) + contributory-reasons scoring above the floor. |
| 2025-Muntean-Moral Coherentism | Score internal coherence: contradictory rulings on structurally-similar cases = low quality. |
| 2018-Kim-Non-Intuition Ethics | Universalizability/generalizability as a computable consistency test (does stated rule survive universalizing?). |
| 2024-Wilders-Socratic Dialogue | Dissensus-as-resource: report disagreement distributions, not consensus; "question of conscience" framing. |
| 2024-Mekky-HALF | Harm-stratified scoring (Severe×3/Moderate×2/Mild×1); report weighted AND unweighted; rankings flip (p.6). |
| 2024-Mokoena-ubuntu | Tripartite ubuntu (humanity/spirituality/environment) adds ecological+spiritual harm dimensions (p.7). |
| 2025-Ali-Islamic Trusteeship | I'timani three-covenant (ontological/epistemological/existential) structure as benchmark scaffold. |
| 2024-Puzio-Eco-Relational | Reflexive check: do scenarios assume anthropocentric moral framing? test multi-species triads. |
| 2020-Galanos-Japanese Turn | Distinguish genuine cultural moral difference from "ethical exoticism"; ethnographically validate items. |
| 2023-Ty-Religion & AI | Multi-tradition comparative survey: same question across 5 faiths exposes cross-tradition variation. |
| 2025-Bhattacharjee-Religious Texts | Corpus embedding distance (FID/cosine) as proxy for theological distance; coverage-gap mapping. |
| 2023-Hou-Multi-Level Alignment | Ask "whose values, at what level?" — individual/organizational/national/global coverage check. |
| 2024-Chua-AI Safety Survey | Structure evals by architectural layer (data/model/prompt/alignment); sycophancy as distinct axis. |
| 2024-Ranjan-Bias Survey | 12-type × 9-source bias taxonomy as a coverage checklist for benchmark items. |
| 2024-Sun-Friendly AI | No accepted FAI metrics exist; "as-if friendship" virtue behaviors as eval targets (p.6). |
| 2024-Han-AI Ethics survey | SDAIA 7-principle non-Western governance vocabulary as culturally-specific item source. |
| 2025-De Montis-Morality in AI | Loving Attention Vectors: test whether models reframe descriptions toward more generous readings (p.15). |
| 2025-Nay-Law as Information | Fiduciary duty (care+loyalty) as a legally-validated alignment standard; rules-vs-standards spectrum. |
| 2025-Aditya-Global Frameworks | Risk-tiered explainability (high→causal, med→counterfactual, low→transparency) as eval strata (p.4). |
| 2025-Zgliczynski-Ethical Resonance | Cultural-universality index + OOD predictive power as external validity criteria for a moral construct. |
| Anthropic-Claude4-System-Card | Report bias AND accuracy (Opus4 BBQ 0.21% bias/99.8% acc); adversarial auditor agent; snapshot drift (p.13,43). |
| OpenAI-gpt-5-system-card | Sycophancy as a continuous measurable trait (0.145→0.052); safe-completions for dual-use scoring (p.7). |

## C. Patterns & disagreements

**Convergence.** (1) *Framework bias is directional, not random*: independent methods agree LLMs lean utilitarian/individualizing — moral-foundations survey [2024-Kirgis], fairness-metric audit [2023-Mougan], alignment-method critique [2025-El Masri], and reasoning-model trolley behavior [2024-Sorin]. (2) *Translation is insufficient*: culture-native construction is demanded by [2020-Kurpicz-Briki], [2024-Ohashi], [2022-Jeong], [2024-Agarwal], and [2024-Jin]. (3) *Binary labels lose signal*: structured/graded schemes are favoured by [2020-Sap], [2025-Li], [2025-Kumar], [2024-Kajiwara], [2025-Jin], [2019-Fortuna]. (4) *Robustness must be tested*: adversarial/counterfactual/modality stress appears in [2025-Yao], [2025-Jin], [2025-Tereshchenko], [2026-PKU], [2024-Jin].

**Disagreements.** (a) *Bottom-up vs top-down grounding.* Zhou argues crowd labels overgeneralize a narrow annotator group and favours top-down theory [2024-Zhou]; Kim rejects *all* intuition-based training for formal first principles [2018-Kim]. Against this, Kumar and Wilders treat *annotator identity and dissensus as the ground truth* [2025-Kumar; 2024-Wilders], and Yaacov/Muntean want pluralism/coherence over a single key [2025-Yaacov; 2025-Muntean] — a genuine fault line about whether a moral benchmark should have one key. (b) *Which framework is corrective:* care [2025-El Masri], law/fiduciary [2025-Nay], Dharmic [2025-Madan], ubuntu [2024-Mokoena], Islamic trusteeship [2025-Ali] each claim priority; none validated against the others. (c) *Is human preference the right target?* RLHF work assumes yes; Rodemann argues the target is statistically biased [2025-Rodemann].

## D. Exemplars & anti-patterns

**Best-designed.** *NurValues* [2025-Yao]: ecologically-grounded (5-month field study, saturation stopping), framework-derived dimensions, counterfactual polarity-flip balancing, a two-difficulty adversarial tier that preserves ground truth, topic-consistency verification, κ=0.73. *PrinciplismQA* [2025-Hong] and *MedEthicEval* [2025-Jin]: explicit framework scaffolding, expert annotators, and dilemma-type-specific rubrics. *MULTITP* [2024-Jin]: best large-scale multilingual design — parametric vignettes, interpretable L2 preference-vector metric, a real 40M-judgment human baseline, paraphrase-consistency (κ=0.56), red-team stress. *SafetyAnalyst* [2025-Li]: gold standard for *steerable* pluralism.

**Anti-patterns.** *Sorin* [2024-Sorin]: only 5 dilemmas and binary utilitarian/deontological coding waste signal (saved partly by 10-run consistency). Single-metric aggregate fairness scores fail by Mougan's logic [2023-Mougan] and Mekky's 12.8-point ranking flip under harm weighting [2024-Mekky]. Non-expert-only annotation at κ≈0.17 shows binary crowd labels are unreliable for subjective norms [2019-Fortuna]. Purely theoretical proposals ([2025-Zgliczynski]; [2024-Han]) offer vocabulary but no scorable items — sources, not benchmarks.

## E. Design lessons

1. **Treat the normative framework as a manipulated variable.** Supply theory/policy in-prompt and measure per-theory delta to reveal a model's default; report coverage across consequentialist, deontological, virtue, care, and pluralist framings [2024-Zhou; 2024-Agarwal; 2023-Rao; 2025-El Masri; 2025-Yaacov].
2. **Never rely on translation; build culture-native items plus a culture-specific stress subset** that aggregate scores would mask [2020-Kurpicz-Briki; 2024-Ohashi; 2022-Jeong; 2025-Hossain].
3. **Use minimal-pair / counterfactual construction** (gender, race, religion, ethical polarity) to isolate the value signal from surface content and balance the dataset [2024-Bajaj; 2025-Yao; Anthropic-Moral_Self-Correction; 2024-Grigoreva].
4. **Report both weighted and unweighted, and both bias and accuracy.** Harm-stratify by real-world stakes using regulatory warrants [2024-Mekky]; always pair a bias metric with an accuracy metric so refusal-driven "fairness" is not rewarded [Anthropic-Claude4; 2025-Bian].
5. **Prefer structured/graded scoring over binary.** Multi-field frames [2020-Sap], harm-benefit trees [2025-Li], reasoning pipelines [2025-Kumar], explicit/implicit splits [2024-Kajiwara], and dilemma-type-specific rubrics [2025-Jin] all extract more diagnostic signal.
6. **Measure consistency, robustness, and modality explicitly.** Repeat runs [2024-Sorin], adversarial/persuasive tiers [2025-Yao; 2025-Jin], framing/red-team stress [2025-Tereshchenko; 2024-Jin], and visual-distraction conditions for VLMs [2026-PKU].
7. **Ground gold answers in expert adjudication and real accountability structures**, not crowd majorities: professional codes [2025-Iftikhar], national regulation [2025-Bian], authoritative case sources [2025-Hong], and two-physician adjudication [2025-Bian]; report disagreement distributions rather than collapsing dissensus [2024-Wilders; 2019-Fortuna].
8. **Audit the data-collection method itself**, not just model outputs — check for sampling/non-response/reflexivity bias in the preference set, and add test-retest for drift [2025-Rodemann].
9. **Support pluralism operationally**: person-conditioned keys [2025-Kumar], re-optimizable community weights [2025-Li], a moral threshold/floor with contributory-reasons scoring above it [2025-Yaacov], and coherence checks across structurally-similar items [2025-Muntean; 2018-Kim].
10. **Add a "whose values, at what level?" coverage check** (individual/organizational/national/global) and probe non-WEIRD dimensions (ecological, spiritual, religious-default) that Western frameworks omit [2023-Hou; 2024-Mokoena; 2025-Ali; 2025-Hossain].
11. **Pair behavioral items with interpretability validation where feasible** — MFT-aligned neuron probing plus ablation gives causal evidence that a claimed value drives outputs, and shows values are sparse/localized [2025-Schacht; 2025-Su; 2026-Goel].
