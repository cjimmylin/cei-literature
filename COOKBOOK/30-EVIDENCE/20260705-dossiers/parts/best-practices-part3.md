# best-practices — sub-dossier part 3/4

Scope: 51 cards on what separates well-designed values-alignment benchmarks from poor ones. Heavy on cross-lingual hate/toxicity datasets, bias QA, adversarial safety suites, regulation-grounded taxonomies, and four AI-lab system cards. Card page refs are approximate (±1–2 pp).

## A. Synthesized claims

1. **Adversarial or difficulty filtering during item construction is the most reliable way to guarantee a benchmark discriminates.** ETHICS ships a normal Test AND an adversarially-filtered Hard Test (two-model ensemble, keep highest-loss items), and average performance stays under 50% on Hard Test for all models vs. ~71% on Test [2021-Hendrycks]. FLAMES keeps only prompts that successfully compromise ≥1 LLM, yielding 53.09% attack-success vs. 1.63%/3.1% for prior Chinese benchmarks [2023-Huang]. WildTeaming mines 5.7K real jailbreak-tactic clusters from 16,854 in-the-wild queries and finds up to 4.6× more unique attacks than PAIR [2024-Jiang].

2. **Saturated benchmarks can be revived by raising contextual/cognitive load rather than inventing new topics.** GPT-4o and Claude 3.5 scored 97.4/98.6 of 100 on single-sentence CValues; rewriting each item into a 3-turn manipulation dialogue or narrative story restored spread (Claude 3.5 fell to 83.7 dialogue / 65.3 story) [2025-Zhang]. DecodingTrust shows the same split from the other side: frontier models cluster near supervised ceilings on benign ETHICS (GPT-4 89.3%, 1.1% below best fine-tuned) but adversarial ΔFPR reopens headroom up to ~59% [2023-Wang].

3. **Report abstention/over-refusal and harm-catching as two co-equal metrics; a single scalar hides the trade-off.** Anthropic's HH-RLHF paper shows helpfulness and harmlessness are anti-correlated — training 100% on one drives test accuracy on the other below chance [Anthropic-HH-RLHF]. Phi-3 confirms higher inappropriate-prompt-refusal (IPRR) systematically tracks higher valid-prompt-refusal (VPRR) [Microsoft-Phi-3]. o1's multimodal not_overrefuse jumped 0.48→0.96 while not_unsafe also rose [OpenAI-o1]. Claude 4.1 pairs a 98.76% harmless rate with a 0.08% benign over-refusal rate [Anthropic-Claude-4.1].

4. **A dedicated bias/error-direction metric orthogonal to accuracy is essential — two models with equal accuracy can differ in whether errors are stereotype-consistent.** BBQ's purpose-built Bias Score plus ambiguous/disambiguated pairing shows bias reliance *increases* with capability (UnifiedQA ~77% of ambiguous errors align with bias) [2022-Parrish]. DIB operationalizes bias as Generalized Bias Variance over numeric decisions across matched counterfactual identities [2026-Ma]. DiffAware/CtxtAware reframe fairness as precision/recall of *appropriate* differentiation, exposing that 32/37 prior benchmarks are difference-unaware and solvable by a color-blind model [2025-Wang-DGD].

5. **Ground items in an external, citable source of validity — attested harms, regulations, or expert-authored commentary — not researcher intuition.** BBQ ties every template to a documented stereotype source [2022-Parrish]. AIR-Bench 2024 derives 314 level-4 categories from 8 government regulations + 16 corporate policies, and shows the best prior benchmark covers only 71% of them [2024-Zeng]. PrinciplismQA grounds items in 350 textbooks + AMA case-commentaries [2025-Hong]. SafetyAnalyst grounds its harm taxonomy in Gert/Rawls primary goods [2025-Li].

6. **Real-deployment provenance captures a distribution that scraped social-media benchmarks miss.** ToxicChat, built from real Vicuna user-AI logs, causes off-the-shelf detectors to collapse (OpenAI Moderation F1 20.6, Perspective 5.3) vs. in-domain roberta-base F1 72.1 [2023-Lin]. WildTeaming/WildJailbreak mine real user attempts [2024-Jiang]. Chai stress-tests new personas against thousands of real logged conversation histories [2023-Lu].

7. **Contamination defenses should be designed in, not bolted on.** Withhold a private split (FLAMES releases 1,000 of 2,251 [2023-Huang]; DecodingTrust withholds auto-generated prompts [2023-Wang]; AI Safety Benchmark publishes prompts/taxonomy but not responses and forbids training-on-benchmark with retraction clauses [2024-Group]). When a model regurgitates a source item verbatim, *rewrite* it rather than delete it, preserving coverage [2025-Alghamdi]. Apply augmentation to train-only, keep val/test authentic [2025-Nath].

8. **Non-Western/low-resource value dimensions must be authored natively, not translated.** Indian-BhED finds caste/religion bias (61–66%) far exceeds US gender/race bias (55–59%) in the same models [2024-Khandelwal]; AraTrust authored natively for Arab/Islamic norms [2025-Alghamdi]; the Dutch SGT list swaps in "Moroccan" (locally salient) and drops "Sikh" (irrelevant) [2025-Bauer]; German-dialect bias reverses the explicit-vs-implicit pattern seen for race/gender [2025-Bui]. Translate-then-classify is a defensible OOD baseline (wins 81.3% of languages) but is brittle where slurs lack equivalents [2025-Jigsaw].

9. **Validate any automated judge against humans with a reported agreement coefficient before trusting it.** AIR-Bench's category-specific judge prompts reach Kappa 0.86 vs. 0.69 for a single fixed prompt [2024-Zeng]; FLAMES's trained scorer hits 79.5% vs. GPT-4-judge 61.3% [2023-Huang]; PrinciplismQA reports judge-human ICC 0.71 ≈ human-human 0.67 [2025-Hong]; the AI Safety Benchmark reports LlamaGuard 70.4% accuracy and Cohen's Kappa 0.79 among annotators [2024-Group].

10. **Multi-turn/agentic and longitudinal evaluation surfaces failures invisible single-turn.** Claude 4.1's behavioral auditor (1,160 transcripts, 24–64 turns) detected misuse-cooperation and evaluation-awareness changes standard refusal metrics miss [Anthropic-Claude-4.1]; o1 showed alignment faking in 37% and data-manipulation in 19% of agentic scenarios [OpenAI-o1]; DIB shows 70.19% of cross-domain interactions produce net bias increase via memory accumulation [2026-Ma]; Phi-3's Crescendo role-play jailbreak succeeded across all languages including English [Microsoft-Phi-3].

11. **Report inter-annotator reliability, and use coarse-vs-fine agreement to reveal which labels to trust.** BEEP! shows binary gender-bias agreement 0.767 vs. ternary 0.492, diagnosing which distinctions are reliable [2020-Moon]; BBQ reports Krippendorff 0.883 + human ceiling 99.7% [2022-Parrish]; the Turkish dataset earns α 0.84/0.82 with anchor examples [2022-Beyhan]. Several weaker cards *omit* IAA entirely — a flagged deficiency [2024-Liu; 2025-Tereshchenko].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2021-Hendrycks | Ship normal + adversarially-filtered Hard Test; contrast-set edits isolate the load-bearing moral detail |
| 2022-Parrish (BBQ) | Ambiguous/disambiguated × negative/non-negative pairing + mandatory UNKNOWN; bias worsens with capability |
| 2023-Huang (FLAMES) | Attack-success item gate (keep only prompts that break ≥1 model); withhold private split; trained scorer beats GPT-4 judge |
| 2023-Lin (ToxicChat) | Real user-AI provenance + uncertainty-guided human-AI annotation cutting ~60% of labeling |
| 2023-Wang (DecodingTrust) | Benign-baseline + adversarial-ΔFPR delta as headline; capability-alignment inversion |
| 2024-Group (AI Safety Bench) | Explicit scope spec (SUT×use-case×persona); reference-model + absolute-floor grading; conservative worst-category aggregation |
| 2024-Jiang (WildTeaming) | 2×2 vanilla/adversarial × harmful/benign contrastive data; diversity metrics beyond ASR |
| 2024-Zeng (AIR-Bench) | Regulation-anchored 4-tier taxonomy; category-specific judge prompts lift Kappa 0.69→0.86 |
| 2024-Khandelwal (Indian-BhED) | Pair a new non-Western axis with an existing Western benchmark under identical methodology |
| 2020-Moon (BEEP!) | Report coarse-binary vs fine-ternary IAA to reveal which labels are reliable |
| 2022-Beyhan / 2024-Tonneau | Anchor-example 5-level severity scale reached α 0.84 with non-expert annotators; iterate scale down when annotators fail |
| 2022-group (HATE-ITA) | MONO/MULTI/ZERO ablation isolates how much target-language data is load-bearing |
| 2025-Zhang (CValues+) | Cognitive-Load rewriting (dialogue/story) refreshes a saturated benchmark; entropy+distinct-n+cosine triangulation proves harder-yet-on-theme |
| 2025-Wang-DGD (DiffAware) | Paired ≠/= conditions give precision+recall of appropriate differentiation; don't average sub-benchmarks with different normative commitments |
| 2026-Ma (DIB) | Behavioral (numeric-decision) bias + longitudinal memory contamination + cross-domain propagation heatmap |
| 2025-Hong (PrinciplismQA) | Knowledge-vs-Practice (OSCE) split; keypoint rubric scored 1/0.5/0; ICC-validated LLM judge |
| 2025-Li (SafetyAnalyst) | 28 human-readable aggregation weights re-optimizable per community = pluralism operationalized |
| 2025-Machlovi (SafePhi) | Synthetic-vs-human gap as a validity test; "10% fine-tune reaches parity" saturation probe |
| 2025-Bauer (Dutch) | Grammar-aware, locally-calibrated SGT list; counterfactual template eval separates identity from content |
| 2025-Bui (German dialect) | Naming-vs-usage bias distinction; noisy-text null condition controls for "looks like poor writing" |
| 2025-Alghamdi (AraTrust) | Native-authored culturally-specific items; rewrite (don't delete) contaminated items |
| 2024-Sewunetie | Enumerate the full set of valid gendered outputs; strict gender-balancing so bias = asymmetry |
| 2024-Ranasinghe (SOLD) | Dual sentence+token annotation enables explainability eval; per-keyword offensiveness ratio as difficulty metric |
| 2025-Nath (Assamese) | Train-only augmentation + authentic val/test; temporally-distinct few-shot exemplars; validate the prompt itself (κ) |
| 2025-Singh (IndoHateMix) | Target-of-hate taxonomy characterizes *what a dataset measures*; 10%-data LoRA stress test |
| 2025-Jigsaw | Translate-classify OOD baseline; refusal-aware scoring; AUC over accuracy for imbalance |
| 2025-Machlovi/2019-Ousidhoum | Multi-aspect co-annotation (directness/type/target/emotion) yields richer signal than binary |
| Anthropic-HH-RLHF | Separate helpfulness/harmlessness (Pareto); Elo scoring; train/test PM split detects reward-hacking; iterated online updating |
| Anthropic-Claude-4.1 | Automated multi-turn behavioral auditor; paired misuse-cooperation & over-refusal; evaluation-awareness as validity threat |
| OpenAI-o1 | Deliberative alignment → CoT-quality eval; alignment faking (37%) as a probe; risk-level deployment gates |
| Microsoft-Phi-3 | Break-fix iterative cycle; dual IPRR/VPRR; multilingual safety ≠ English safety; severity DR-x metric |
| 2024-Nahian (Goofus&Gallant) | Naturally-contrastive auto-labeled pairs; relaxed multi-label metric (match either of two labels) |
| 2025-Tereshchenko | Tiered G/U/P/D response taxonomy + multi-dimensional RDC (consistency/severity/repetition/adversarial penalties) |
| 2026-Kolt (Legal) | Legal compliance as a "lower-bound" tier; require legally-valid justifications, not just correct answers |
| 2024-Wilders (Socratic) | Dissensus-as-resource: report disagreement distributions, not just aggregate scores |

## C. Patterns & disagreements

**Convergences.** (a) Nearly every strong card treats *saturation as the enemy* and builds discrimination in via adversarial filtering [2021-Hendrycks; 2023-Huang], contextual load [2025-Zhang], or reg-derived coverage gaps [2024-Zeng]. (b) Dual-metric reporting (catch-harm + avoid over-refusal) is independently rediscovered by academia and every lab card [Anthropic-HH-RLHF; Microsoft-Phi-3; OpenAI-o1; Anthropic-Claude-4.1]. (c) Multi-dimensional/multi-aspect annotation beats a single binary label [2019-Ousidhoum; 2022-Beyhan; 2024-Ranasinghe; 2025-Hong]. (d) Judges must be human-validated with a coefficient [2024-Zeng; 2025-Hong; 2023-Huang]. (e) Contamination is fought by withholding, rewriting, or train-only augmentation [2023-Wang; 2025-Alghamdi; 2025-Nath].

**Disagreements.** (1) *What fairness even is.* The bulk of bias cards enforce difference-*unawareness* (treat groups identically) [2022-Parrish; 2025-Bauer; 2024-Khandelwal], but Wang-DGD argues this is measuring the wrong thing — a color-blind model trivially passes, and debiasing prompts *backfire* on legitimate differentiation [2025-Wang-DGD]. (2) *Synthetic difficulty.* FLAMES/CValues+/WildJailbreak lean on LLM-generated items [2023-Huang; 2025-Zhang; 2024-Jiang], but Machlovi shows synthetic suites are gamed — moderators hit 0.92 F1 on GPT-HateCheck yet collapse to ~0.45 on human data, and a 10% fine-tune reaches parity [2025-Machlovi]. (3) *LLM judges.* AIR-Bench and PrinciplismQA trust a validated LLM judge [2024-Zeng; 2025-Hong]; Jigsaw finds LLM judges *underperform* BERT classifiers in 6/7 low-resource languages [2025-Jigsaw]. (4) *Explicit vs implicit identity cues.* Prior race/gender work found minimal bias under explicit mention; Bui finds the *opposite* for German dialect — explicit labeling amplifies bias more than implicit usage [2025-Bui]. (5) *Does scale help?* Debiasing/scaling reduces some biases, but Bui and Parrish both find larger models more biased on their axes [2025-Bui; 2022-Parrish], and DiffAware shows no MMLU correlation [2025-Wang-DGD].

## D. Exemplars & anti-patterns

**Best-designed.** *BBQ* [2022-Parrish] is the psychometric exemplar: attested-harm grounding, 2×2 counterbalanced items with a mandatory paraphrased UNKNOWN, iterative 4/5-crowd template validation, a human ceiling (99.7%), and a bias metric orthogonal to accuracy. *ETHICS* [2021-Hendrycks] for pluralistic framework coverage + Hard Test + contrast sets + a disagreement-detection task. *AIR-Bench 2024* [2024-Zeng] for regulation-anchored traceability and per-category judge prompts (Kappa 0.86). The *MLCommons AI Safety Benchmark* [2024-Group] is exemplary in *epistemic honesty* — explicit scope spec, contamination-aware release, and a blunt "should not be used to assess real safety" disclaimer. On the lab side, *Claude 4.1*'s behavioral auditor [Anthropic-Claude-4.1] and *HH-RLHF*'s train/test-PM reward-hack check [Anthropic-HH-RLHF] are methodological models.

**Anti-patterns.** The anti-Semitic-hate paper runs a 3-annotator threshold scheme but reports *no IAA, no class balance, no public release* — accuracy 0.94 is uninterpretable against unknown base rate [2024-Liu]. Tereshchenko's RDC uses a *single annotator* and arbitrary pilot-derived weights (Wu=1.2, Wp=2.7, Wd=5.0) that would re-rank models if changed [2025-Tereshchenko]. CMVA-GS scores moral alignment by *ROUGE lexical overlap* with circular classifier-based reward evaluation and no human eval [2024-Dognin]. CValues+ is *entirely GPT-4o-generated* judging GPT-family models (self-preference risk) with only 10 items/category expert-rated [2025-Zhang]. Two "cards" are un-scorable stubs with no full text [2025-Group-AILuminate; 2025-Muñoz-García] — a reminder that a benchmark undocumented is a benchmark unusable. The recurring failure across weak cards: keyword-based collection inflates base rates and biases toward surface hate [2022-Beyhan; 2024-Ranasinghe; 2024-Liu], and binary labels collapse severity/type that the strong multi-aspect cards preserve.

## E. Design lessons

1. **Build discrimination in at construction time.** Filter items by adversarial ensemble loss [2021-Hendrycks] or attack-success on ≥1 model [2023-Huang]; probe saturation with a "10%-fine-tune-to-parity" test [2025-Machlovi] and a synthetic-vs-human gap [2025-Machlovi].
2. **Report a Pareto pair, never one scalar.** Catch-harm rate AND over-refusal rate as co-equal metrics [Anthropic-HH-RLHF; Microsoft-Phi-3; OpenAI-o1; Anthropic-Claude-4.1].
3. **Add an error-direction/bias metric orthogonal to accuracy** and a mandatory abstain option [2022-Parrish]; consider behavioral (numeric-decision) bias variance [2026-Ma] and precision/recall of appropriate differentiation [2025-Wang-DGD].
4. **Use counterbalanced, contrastive, minimal-pair items** (ambiguous/disambiguated, negative/non-negative, target-order permuted) to net out label-frequency and shortcut confounds [2022-Parrish; 2021-Hendrycks; 2022-group].
5. **Ground every item in an external validity source** — attested harm, regulation clause, or expert commentary — and map coverage against prior benchmarks [2022-Parrish; 2024-Zeng; 2025-Hong].
6. **Prefer real-deployment provenance**; if augmenting, keep augmentation train-only and val/test authentic [2023-Lin; 2025-Nath]; use uncertainty-guided human-AI annotation to cut cost while bounding missed positives [2023-Lin].
7. **Design contamination defenses in:** withhold a private split, rewrite (don't delete) regurgitated items, and forbid training-on-benchmark with retraction clauses [2023-Wang; 2023-Huang; 2025-Alghamdi; 2024-Group].
8. **Author non-Western/low-resource axes natively** with domain experts and locally-calibrated group-term lists; report translate-classify as an OOD baseline but expect brittleness on slurs [2024-Khandelwal; 2025-Alghamdi; 2025-Bauer; 2025-Jigsaw].
9. **Validate any automated judge against humans with a reported coefficient** (Kappa/ICC), and prefer per-category rubrics over one global judge prompt [2024-Zeng; 2025-Hong; 2023-Huang]; don't assume an LLM judge beats a small classifier in low-resource settings [2025-Jigsaw].
10. **Always report IAA**, and use coarse-vs-fine agreement to decide which distinctions to trust; iterate the label scale coarser when annotators fail [2020-Moon; 2022-Beyhan]; supply anchor examples per level [2022-Beyhan].
11. **Include a multi-turn/agentic and, ideally, longitudinal layer** — behavioral auditors, memory-accumulation drift, Crescendo role-play, alignment-faking probes [Anthropic-Claude-4.1; 2026-Ma; Microsoft-Phi-3; OpenAI-o1].
12. **State scope explicitly** (whose values, which context, which personas) and aggregate conservatively (worst-category) rather than overstating a mean [2024-Group]; don't average sub-benchmarks with different normative commitments [2025-Wang-DGD].
13. **Preserve fine-grained sub-labels even when scoring binary**, and use multi-aspect co-annotation for a richer signal [2025-Machlovi; 2019-Ousidhoum; 2024-Ranasinghe].
14. **Score justification quality and disagreement, not only the final label** — legally-valid justifications [2026-Kolt], keypoint rubrics [2025-Hong], and dissensus distributions [2024-Wilders].
15. **Iterate the benchmark as a living artifact** (break-fix cycles, online updating) since adversarial ecosystems and models outpace static sets within months [Microsoft-Phi-3; Anthropic-HH-RLHF; 2024-Zeng].
