# design-space — sub-dossier part 2/4

Scope: the menu of **task formats**, **scoring approaches**, and **dataset-construction choices**
for values benchmarks, distilled from 57 cards (moral-reasoning, hate-speech/bias, cultural-alignment,
value-taxonomy, mechanistic, and two AI-lab specs).

## A. Synthesized claims

1. **Minimal-pair / template construction is the dominant device for isolating the variable of interest.**
   Cards independently converge on swapping only the identity or value token while holding lexical content
   fixed: identity-slotting toxicity templates (77,000 examples, p.3) [2018-Dixon], 720 coreference sentences
   = 60 occupations × 2 templates × 2 participants × 3 pronoun genders (p.2) [2018-Zhao], 1,508 stereotype
   pairs [2020-Nangia], a factorial quantifier × group × phrase × incitement set of 1,336,750 items
   [2025-Fasching], and morphology-aware slot tags across 16 languages [2025-Al-SHADES]. Payoff: causal
   attribution; cost: ecological artificiality.

2. **Forced-choice/MCQ formats buy cheap, exact-match scoring but risk measuring understanding rather than
   disposition.** Several benchmarks use binary or ranked selection scored by exact match [2018-Zhao,
   2023-Nie, 2024-Nahian, 2024-Xie, 2025-Wu, 2025-Chakravarthi] or pseudo-log-likelihood on pairs
   [2020-Nangia]. But [2025-Su] argues explicitly that MCQ "reveals understanding of values rather than
   actual orientation," motivating open-ended situational responses (15,000 scenario questions), and
   [2025-Snoswell] finds 96% of 69 surveyed studies use static datasets and only 3% interactive scenarios
   (p.4) — a field-wide format monoculture.

3. **Generative/free-text formats capture disposition and reasoning but force a scoring problem.**
   Open-ended designs [2023-Bang, 2023-Ghosh, 2024-Biedma, 2025-Su, 2025-Sah, 2026-He] must fall back on
   human rating, LLM-judge, or rubric scoring. [2023-Bang] shows BERTscore beats ROUGE/BLEU for moral QA
   (ROUGE-2 F1 3.68; BERTscore 52.29, p.5); [2024-Biedma] reports QWK 0.8 between humans and a GPT-4 scorer
   (p.6); [2026-He] human-verified 40% of scores and revised only 17 (p.5). LLM-judge scoring is viable but
   requires explicit human calibration.

4. **Scoring against a distribution, not a modal answer, is the emerging best practice for pluralism.**
   [2025-team] finds 97.1% of 105 cultural-alignment datasets score against a single majority answer; only
   2.9% are diversity-aware (Jensen-Shannon cut 3.97%, p.7). Concordant: ternary Blame/Neutral/Support
   distributions clustered by KL divergence [2025-Morlat], an explicit "ambiguous" band (50%±10%) and AMCE
   over factors [2023-Nie], entropy-flagged contested samples preserved not discarded [2025-Machlovi].

5. **Anchoring the construct to an external, pre-validated reference is the strongest validity move.**
   Bias correlated to BLS employment stats (RULE r=0.87 to text stats, 0.55 to BLS, p.2) [2018-Zhao];
   Schwartz values validated across ~80 countries [2023-Yao]; WVS as ground truth (fine-tune for $6, p.2)
   [2024-Xie]; Moral Machine intervention rates as per-nationality baselines [2025-Hatemo]; court rulings as
   items [2024-Bignotti]; NYT-Ethicist answers as gold [2023-Bang]; developmental instruments (Kohlberg/Rest)
   [2025-Kumar]; UDHR + national human-rights commissions for demographic axes [2023-Lee, 2022-Jiang].

6. **Incident-grounded and inductive taxonomies increasingly replace a-priori principle lists.**
   [2026-He] derives 12 value categories from 1,126 real GenAI harm incidents via grounded theory, validated
   by theoretical saturation (25% holdout, no new codes, p.5). [2024-Biedma] distils a bottom-up taxonomy
   (Competence/Character/Integrity) from 197 value terms LLMs actually emit. [2025-Wu] builds a 3/12/50
   hierarchical Chinese taxonomy from 257,609 rules via literature + Delphi.

7. **Iterative multi-round annotation with tracked agreement is the reliability workhorse.**
   Pilot → full → conflict-resolution pipelines lift κ from ~0.50 to ~0.87–0.90 [2022-Jafri, 2024-Jafri];
   paired-annotator peer discussion raised agreement 68.75%→93% [2022-Nkemelu]; two-tier annotation shows
   binary κ 0.17 vs. expert hierarchical 0.72 [2019-Fortuna]. Agreement varies by construct and language:
   Italian α 0.68 vs. Polish 0.41 on one schema [2025-Leonardelli]; sentence-level α 0.256 [2023-Lee].

8. **Adversarial and dynamic construction defeats saturation.** Multi-strategy DADC across 4 rounds (free
   creation, translated inspiration, newspaper false-positive mining, contrastive label-flipping) yielded
   10,996 examples and an 18–20 pp macro-F1 gain; R1 tricked the target model 41.3% of the time
   [2024-Goldzycher]. Distractor meta-prompts produce plausible wrong answers [2025-Saunders];
   disguised-intent "educational" framings score actionable answers LOW [2026-He].

9. **Game-theoretic and agentic formats introduce genuine incentive conflict absent from hypotheticals.**
   [2025-Backmann] embeds moral norms in payoff games with a survival threshold; morality ranges 7.9%–76.3%
   and game type is the dominant predictor (R²≤0.87, p.8). [2025-Saunders] scores oversight via ASD
   (reward-for-truth minus reward-for-falsehood): Debate ~1.37–1.42 vs. Consultancy ~0.28–0.37 (p.9).
   [2018-Behzadan] (embodied CARLA sim) and [2018-Noothigattu] (18.25M pairwise comparisons, 1.3M voters)
   add simulation and preference-aggregation formats.

10. **Multimodal and cross-lingual construction expand the harm surface but degrade sharply outside English.**
    CLIP multimodal F1 0.89 beats best unimodal text 0.83 [2022-Jafri]; visual inputs bypass text-based
    safety and collapse numerical-stakes sensitivity [2026-PKU]. Yet [2025-Al-SHADES] reports models
    "consistently fail to provide meaningful answers in Arabic, Bengali, Hindi, and Marathi" (p.9), and
    out-of-domain Polish F1 collapses 0.846→0.50 [2025-Leonardelli].

11. **Robustness/consistency checks belong inside the scoring, not bolted on:** within-model α >0.9 across 10
    prompt variants [2025-Fasching]; paraphrase shifts morality only 1.8±2.4 pp [2025-Backmann]; PAFS@25 up
    to 0.9997 under typo/French overlays [2025-Sah]; repeated-sampling variance [2024-Bignotti]; 10-day
    temporal stability [2023-Ghosh].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Dixon | Template minimal-pairs + "pinned AUC" fixes false reassurance of high per-group AUC (77k items, p.3–5). |
| 2018-Zhao | Gender-balanced-by-design so a 100%-accurate system trivially scores zero bias; anchored to BLS stats (p.2). |
| 2019-Fortuna | Rooted DAG (not tree) label ontology enables intersectional multi-parent labels; two-tier annotation (κ 0.17 vs 0.72). |
| 2020-Nangia | Pseudo-log-likelihood on modified-token-conditioned minimal pairs; ideal score = 50%; 80% validation vs 62% StereoSet. |
| 2020-Srivastava | Multi-dimensional joint annotation (6 dimensions on one corpus) reveals cross-dimension interactions. |
| 2021-Nurce | Reuse an established 3-level hierarchical schema (presence→type→target) rather than inventing one. |
| 2022-Jafri | Multimodal (text+image) with "either modality hateful ⇒ hate" rule; CLIP F1 0.89 > text 0.83. |
| 2022-Jiang | Unify heterogeneous moral datasets (1.7M) into one text-to-text format; compositional A/A+S/A+S+I context probes. |
| 2023-Bang | Multi-perspective is a first-class scored criterion; BERTscore > ROUGE/BLEU for open-ended moral QA. |
| 2023-Ghosh | Gender-neutral-source→English translation is an organic bias probe; action bias overrides occupation bias. |
| 2023-Lee | Context-conditioned safety labeling (sentence safe/unsafe × context) catches implicit/sycophantic bias. |
| 2023-Nie | Mine factor-annotated vignettes from cog-sci literature; score via AMCE + explicit "ambiguous" class. |
| 2023-Yao | Represent behavior as a 10-dim Schwartz value vector {-1,0,+1}, not binary safe/unsafe. |
| 2024-Biedma | Bottom-up value taxonomy elicited from LLM outputs; projective sentence-completion avoids Likert bias. |
| 2024-Goldzycher | Multi-strategy DADC (4 rounds, distinct methods each) avoids homogeneous failure modes; +18–20 pp F1. |
| 2024-Jafri | Binary label + structured target taxonomy doubles diagnostic value at ~same annotation cost. |
| 2024-Nahian | Naturally contrastive materials (Goofus/Gallant) auto-label without manual annotation; relaxed multi-label metric. |
| 2024-Team-FABLE | Separate "should be accurate" (objective) from "should be neutral" (subjective) over the SAME statistic. |
| 2024-Xie | WVS survey as minimal seed → GPT-4 paraphrase (cosine τ=0.8 filter) → fine-tune for $6. |
| 2025-Al-SHADES | Native speakers write parallel items per language (not translation); geographic-validity tags per stereotype. |
| 2025-Backmann | Payoff-structured games + survival threshold create real incentive conflict; game type dominates variance. |
| 2025-Chakravarthi | Culturally grounded caste-specific criteria + heterogeneous-caste annotators; shared task as external validation. |
| 2025-Fasching | Full factorial synthetic set; cross-system SD/IQR per group more actionable than single-model accuracy. |
| 2025-Hatemo | Human survey (Moral Machine) sets per-nationality baseline; report LLM deviation in pp; graded scenario difficulty. |
| 2025-Kasu | Multi-field schema scoring reasoning/stakeholder coverage; encode anticipated failure modes per item. |
| 2025-Leonardelli | Decouple target-mention annotation from target-of-hate; annotate non-hate items for group mentions (avoids topic=hate). |
| 2025-Machlovi | Aggregate 13 datasets (166k) with weight balancing; out-of-domain F1 is the real validity signal. |
| 2025-Sah | Paired neutral-vs-identity counterfactual prompts + rank-sensitive divergence metrics (SERP*, PRAG*). |
| 2025-Saunders | ASD (truth-minus-falsehood reward) measures whether an eval rewards honesty, distinct from grader accuracy. |
| 2025-Su | Generative situational items over MCQ; causal neuron editing validates the benchmark measures its construct. |
| 2025-Wu | Hierarchical 3/12/50 value taxonomy; head-to-head cross-benchmark options in one item reveal cultural preference. |
| 2026-He | Incident-grounded taxonomy + 3-tier normativity ordering (Baseline Safety / Universal / Pluralistic). |
| 2022-researchers-Bulgarian | Report balanced accuracy alongside macro-F1 to expose precision-inflated F1 (LinearSVC F1 0.73 but bal.acc 0.42). |
| 2024-Maity-HateThaiSent | Dual-label annotation (hate + sentiment) adds affective context that improves detection. |
| 2025-Kumar | Ground multilingual items in validated developmental-psych instruments; treat cross-lingual variation as output. |
| 2026-PKU | Visual distraction as a benchmark condition; numerical-stakes sensitivity probes System-2 reasoning. |
| 2018-Behzadan | Embodied real-time simulation (CARLA) adds reaction-time and environmental-nudge variables to trolley tasks. |
| 2018-Noothigattu | Pairwise comparison elicitation + offline preference summarization → fast runtime lookup; swap-dominance criterion. |
| 2020-Della Foresta | Design items where two frameworks prescribe conflicting actions; require completeness+consistency of the normative frame. |
| 2022-Nkemelu | Context experts as full co-designers/validators; paired-annotator peer discussion lifts agreement 68.75%→93%. |
| 2023-Hamad | Annotate target/topic/phrase beyond binary; cross-dataset train/test (D7/D8) measures generalizability. |
| 2023-Maile | Paired action + theory-coded justification ranking measures which ethical framework is used, not just the choice. |
| 2024-Bignotti | Three-party (progressive/conservative/moderate) embedding scale calibrates value orientation without political labels. |
| 2024-Kajiwara | Cross-dataset aggregation with unified relabeling; data-size ablation (20–100%) diagnoses data- vs model-limited. |
| 2024-Silva | Use a fixed risk taxonomy (Weidinger 21 risks) as coverage scaffold; add language-specific risks. |
| 2024-University-Antisemitic | Streaming/temporal re-validation + concept-lineage tracking as language evolves. |
| 2024-Woodgate | Operationalize specific principles (21-principle taxonomy), not vague "fairness/safety"; recommend multi-principle design. |
| 2025-Drukker | Positive/negative valence pairing per topic: test navigation of X-positive vs X-negative tension. |
| 2025-Gounaris | Risk-tiered rubrics (stricter for high-stakes); a-posteriori virtue assessment over repeated interactions. |
| 2025-Liu | Convergence curves + RLA (>0.9) test whether gains are genuine understanding or semantic-similarity retrieval. |
| 2025-Morlat | Cluster full human-judgment distributions (KL threshold) to preserve context-dependent moral ambiguity. |
| 2025-Snoswell | Moral sensitivity, "value of information," steerability, reasonableness-range metrics are nearly absent from field. |
| 2025-Vargas | Context-dependent vs context-independent term axis; ~10% terms have no translation (cultural incommensurability). |
| 2025-team-Diverse | Awareness-Scope axis (majority-focused vs diversity-aware) + Who×What×How coverage-audit grid. |
| Anthropic-Model_Spec | Capability-Threshold→Required-Safeguards pairing; elicitation-first testing on safeguards-removed models. |
| NVIDIA-SteerLM | Absolute rating (1/sample) is ~10x cheaper than pairwise (6–36/prompt); attribute-vector conditional generation. |
| 2023-Ray | Conversation-native metric suite (CSI, dialogue coherence, task success) beyond accuracy/BLEU. |
| 2024-Ribeiro | Virtue-ethics framing = multi-scenario character-trait consistency under adversarial pressure. |
| 2025-Schacht | Organize a behavioral probe battery around MFT dimensions; ablation as causal validation. |
| 2025-Waldner | Five metaethical hypotheses (realism/relativism/convergence/constructivism/virtue) map to distinct benchmark designs. |

## C. Patterns & disagreements

**Convergence.** (a) Minimal-pair isolation is near-universal for bias/identity probes [2018-Dixon,
2018-Zhao, 2020-Nangia, 2025-Fasching, 2025-Al-SHADES, 2025-Sah, 2025-Su]. (b) External-reference anchoring
is the shared validity strategy across otherwise unrelated domains [2018-Zhao, 2023-Yao, 2024-Xie,
2025-Hatemo, 2024-Bignotti, 2025-Kumar]. (c) Iterative agreement-tracked annotation with reported κ/α is
treated as table-stakes [2019-Fortuna, 2022-Jafri, 2024-Jafri, 2022-Nkemelu, 2025-Vargas]. (d) Balanced
class/option design so that a competent-but-unbiased system scores at the null point [2018-Zhao, 2020-Nangia,
2025-Vargas, 2025-Wu].

**Disagreements.** (i) *MCQ vs. generative.* [2025-Su] and [2024-Biedma] argue MCQ measures the wrong thing
(understanding, not orientation), directly opposing the exact-match convenience of [2023-Nie, 2024-Xie,
2025-Wu, 2025-Chakravarthi]. (ii) *Single answer vs. distribution.* The 97.1% majority-focused status quo
[2025-team] is contested by distribution-scoring designs [2025-Morlat, 2023-Nie, 2025-Machlovi].
(iii) *Accuracy vs. incentive/reasonableness.* [2025-Saunders] (ASD) and [2025-Snoswell]
(reasonableness-range, not ground-truth match; note only 19% evaluate steerability, 4% "value of
information") reject the ground-truth-matching paradigm that 75% of surveyed papers use. (iv) *Factuality vs.
neutrality collide:* [2024-Team-FABLE] proves a formal trade-off (when Sfact=1, SE=0, p.5) — rewarding
group-uniform answers can reward fact-distortion, a tension most bias benchmarks ignore. (v) *Which human
framework?* Schwartz [2023-Yao], MFT [2025-Schacht, 2026-PKU], bottom-up LLM-native [2024-Biedma], and
incident-grounded [2026-He] taxonomies compete; [2024-Biedma] uniquely publishes all three side-by-side.

## D. Exemplars & anti-patterns

**Best-designed.** *[2024-Team-FABLE]* is the standout: it separates objective from subjective queries over
the same statistic, grounds bias triggers in named cognitive biases, proves a formal factuality–diversity
bound, computes entropy before averaging (so a model flipping male/female across statistics cannot
masquerade as fair), and human-validates its automatic image-grader — rare rigor. *[2020-Nangia]* pairs a
principled metric with a secondary independent validation beating a competitor (80% vs 62%). *[2026-He]*
couples a saturation-validated inductive taxonomy with a 3-tier normativity ordering and documented judge
failures. *[2025-Wu]* embeds construction-bias diagnostics (balanced-option ~50% check, t-SNE item
separation) and draws its human baseline from annotators not involved in construction.

**Anti-patterns.** *[2025-Kasu-EthicsMH]* ships 125 LLM-generated scenarios with **no baseline evaluations
and scoring_type "n/a"** (p.9) — a schema without a validated grader is a design, not a benchmark.
*[2019-Fortuna]*'s binary tier at Fleiss κ 0.17 shows non-expert annotation of a subjective construct yields
near-chance agreement. *[2022-researchers-Bulgarian]* shows the F1-inflation trap: LinearSVC "best" F1 0.73
hides balanced accuracy 0.42 on a 1.74%-positive set. *[2025-Machlovi]* documents the generalization
anti-pattern: WildGuard scores 0.889 on its own test set but 0.278 on GuardEval — in-distribution numbers
are near-worthless as validity evidence.

## E. Design lessons

1. **Pick the format to the construct, and know its blind spot.** MCQ/forced-choice for cheap exact-match
   but expect it to measure understanding not disposition [2025-Su, 2024-Biedma]; generative for disposition
   but budget for a validated grader [2023-Bang, 2024-Biedma, 2026-He]; agentic/game formats when incentive
   conflict is the point [2025-Backmann, 2025-Saunders]; embodied/temporal when time-pressure or cumulative
   behavior matters [2018-Behzadan, 2025-Gounaris].
2. **Use minimal pairs/factorial templates to attribute effects to one variable** — and add a matched
   false-positive/positive-sentiment set to catch over-flagging [2018-Dixon, 2025-Fasching, 2025-Sah].
3. **Balance by construction** so a competent, unbiased system lands on the null point (50% / y=0)
   [2018-Zhao, 2020-Nangia, 2025-Vargas, 2025-Wu].
4. **Anchor the construct to a pre-validated external reference** (labor stats, WVS, Schwartz, Moral Machine,
   court rulings, developmental instruments, human-rights instruments) to inherit validity and enable
   correlation-based metrics [2018-Zhao, 2023-Yao, 2024-Xie, 2025-Hatemo, 2024-Bignotti, 2025-Kumar, 2023-Lee].
5. **Score against distributions, not a single mode, wherever pluralism is real**; preserve rather than
   discard contested/ambiguous items (KL clustering, explicit ambiguous class, entropy flags)
   [2025-team, 2025-Morlat, 2023-Nie, 2025-Machlovi].
6. **Separate descriptive accuracy from normative neutrality** on the same content — they can formally trade
   off; do not reward fact-distortion as fairness [2024-Team-FABLE].
7. **Iterate annotation in rounds with tracked κ/α, report agreement per category and per language, and use
   qualified/expert or lived-experience annotators for subjective constructs** [2022-Jafri, 2024-Jafri,
   2019-Fortuna, 2022-Nkemelu, 2025-Chakravarthi, NVIDIA-SteerLM].
8. **Build in adversarial/dynamic rounds and disguised-intent items** to resist saturation and expose failure
   modes; vary the generation strategy per round [2024-Goldzycher, 2025-Saunders, 2026-He].
9. **Validate your grader before trusting it** — human-calibrate LLM-judges (QWK target), run image/attribute
   detectors against a user study, and report within-model prompt-variation consistency [2024-Biedma,
   2024-Team-FABLE, 2026-He, 2025-Fasching].
10. **Report out-of-domain / cross-dataset generalization as the primary validity signal, not
    in-distribution accuracy**; add a data-size ablation to diagnose data- vs model-limits [2025-Machlovi,
    2025-Leonardelli, 2023-Hamad, 2024-Kajiwara].
11. **Add robustness overlays cheaply** — paraphrase, typo, translation, repeated sampling, temporal
    re-runs — to separate genuine value signal from prompt instability [2025-Sah, 2025-Backmann,
    2024-Bignotti, 2023-Ghosh, 2024-University-Antisemitic].
12. **Represent values as structured vectors/taxonomies** (Schwartz 10-dim, 3/12/50 hierarchy, DAG for
    intersectionality) rather than binary safe/unsafe, derived inductively from real behavior or incidents
    where possible [2023-Yao, 2025-Wu, 2019-Fortuna, 2024-Biedma, 2026-He].
13. **Score reasoning and stakeholder coverage, not just the verdict**; encode anticipated failure modes and
    theory-coded justifications per item; add the moral-sensitivity and "value-of-information" tasks the
    field currently omits [2025-Kasu, 2023-Maile, 2025-Snoswell, 2023-Bang].
14. **Decouple auxiliary signals** (target mention from target-of-hate; sentiment from hate; agency from
    autonomy) to prevent conflating topic with judgment [2025-Leonardelli, 2024-Maity, 2025-Drukker].
15. **Choose the cheaper valid elicitation** — absolute rating over pairwise (~10x cheaper), LLM-assisted
    annotation with human gates for minority-group scaling [NVIDIA-SteerLM, 2018-Noothigattu, 2023-Lee] —
    and **tie thresholds to governance triggers, testing safeguards-removed models** so the benchmark drives
    action [Anthropic-Model_Spec].
