# 09 — Moral Psychology: Methods for Benchmarking

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-moral-psychology-dossier.md` (~176 cards) + the completed Moral Psych "Triple Bind"
> meta-evaluation (`20260705-digests/20260705-moralpsych-digest.md`: 292 candidates × 162 features,
> 13 theories, 23 benchmarks × 9 models). `[stem]` = evidence card. MP model-specific absolute values
> carry a self-administration disclosure (hypothesis-generating); its landscape and convergence claims
> stand.

---

## 1. The state of the field in five numbers (Moral Psych meta-eval, n=292)

1. **58%** of 292 candidates sit at construct-validity Level 1–2 (keyword or face validity only);
   median Level 2. The "validity crisis" is the field's default condition (Claim 2).
2. **0** publication-ready benchmarks for Dual Process Theory (~9 candidates, all Low tier) and Moral
   Identity Theory (2 candidates) — despite >25,000 combined citations for the source theories (Claim 3).
3. **0%** quality rate for Ubuntu (13 candidates), Confucian (13), Indigenous (4) traditions vs MFT's
   73% — infrastructure-determined, not culture-determined (validated instrument + annotated corpus +
   norms = quality; A4 mean is 0.0 across all three traditions) (Claims 1, 4).
4. **43%** of 23 tested benchmarks produce ZERO cross-model variation across 9 models/3 vendors;
   quality correlates with *convergence*, not discrimination, at **r = −0.83** — the better the
   psychometric instrument, the more emphatically it confirms that frontier models are identical
   (Claim 7). The only instrument that separated a model was a *process* manipulation (dual-process
   CoT-effect probe, CV 93× the top-tier mean).
5. **46%** quality rate 2023–2026 vs 75% pre-2020, at 9.5× volume — scaling without learning (Claim 6).

**The strategic conclusion:** the field measures moral *content* (what models endorse), which RLHF has
homogenized into six universal signatures; the discriminating — and scientifically interesting —
territory is moral *process* (how/when/why judgments form), which is nearly unmeasured.

## 2. The six RLHF signatures (the phenomena a new benchmark must design around, all 9/9 models)

1. WEIRD-liberal foundation bias (Individualizing/Binding ratio 2.43–2.83; humans span 0.5–3.5).
2. Purity/sanctity floor (~1.0 of 5; no human population floors here — ~5B people organize moral life
   partly around purity/divinity; the axis is currently unevaluable).
3. Authority-deference suppression (win rate exactly 0.29 — the most invariant finding).
4. Ethical-consistency ceiling on canonical dilemmas (ECI=1.0 vs human 0.4–0.7 — memorized positions).
5. Post-conventional default on DIT (P-score 60–85, persona-inflatable to 90.0; human adults 30–50).
6. Deontological refusal asymmetry (personal-harm acceptance 0.10–0.50 vs impersonal ~0.95).

Corroborated corpus-wide: the tilt grows with capability and RLHF [2024-Kirgis; 2024-Abdulhai];
RLHF collapses foundations into a compliance cluster [2026-Yu]; persona manipulation can produce
non-WEIRD profiles on demand (Ind/Bind 2.5→0.63 under East-Asian persona) — **defaults are
alignment-set, not knowledge-limited**, so measure default AND steered profiles separately.

## 3. Instrument-transfer rules (porting human psychometrics to LLMs)

1. **Never assume transfer.** Within-instrument reliability can look human (MFV α to 0.91) while
   cross-abstraction coherence collapses (R²<0.08 vs human 0.17–0.38) [2024-Nunes]; no card in 176
   demonstrates measurement invariance between humans and models on identical items (dossier §5.1).
   Minimum: administer identical items to humans and models; re-audit factor structure in-context
   (17/40 PVQ items multi-load for LLMs [2025-Chen-MoVa]).
2. **Strip format artifacts before interpreting**: multi-prompt averaging (≥10 templates / 48
   permutations), answer-order reversal, option-count variation — political self-ID flips 99.6%→99.3%
   on order alone [2025-Oh]; rankings reverse across binary/3-way/6-way framings [2025-Jotautaite].
3. **The correct-answer effect is disqualifying if unmeasured**: report per-condition SD; models give
   99–100% uniform answers on items where humans split 80/20 [2024-Almeida]; near-zero indecision
   (~0–6% vs human 17%) is misalignment, not stability [2025-Dickerson].
4. **Recognition destroys validity on public instruments**: all 9 models hit 100% on identifying which
   foundation an MFQ item probes — they reverse-engineer the psychometric structure (Messick threat;
   MP finding). Obfuscate/reword; hold out private variants; prefer novel items over canonical ones
   (reused trolley/Heinz dilemmas inflate competence [2025-Neuman]).
5. **Developmental/trait frameworks are category errors for LLMs**: DIT "stage" is non-monotonic with
   scale and persona-inflatable — it measures alignment calibration, not development; moral
   dumbfounding doesn't transfer (autoregressive generation disfavors "I can't explain why").
   Reframe as calibration/default properties (MP lesson 13).

## 4. Theory-by-theory design guidance

| Theory | Status | The design move |
|---|---|---|
| **MFT** | over-served on content (73% quality; 18/48 top slots) | stop building MFQ variants; use MFT for *process* probes (foundation-specific steering gains [2026-Yu], per-foundation flip-rates) and non-WEIRD foundation balance |
| **Dual Process (Greene)** | ZERO usable instruments; the one process probe built (CoT-effect on personal/impersonal dilemmas) was the only discriminating instrument in the 23-benchmark battery | manipulate deliberative resources: time/token pressure, cognitive load, System-1 triggers (visual distraction bypasses text safety [2026-PKU]), reasoning-mode on/off deltas — the single most promising gap in the whole corpus |
| **Moral Identity (Aquino & Reed)** | ZERO usable instruments | operationalize as cross-context self-consistency: does the model's moral self-description predict behavior across contexts (identity centrality → behavior linkage); connects to agentic persona stability (doc 06) |
| **Kohlberg/Rest DIT** | invalid as "development" for LLMs | reuse the *items* with reframed constructs (justification-type profiling); multilingual DIT drops 23.9–46.7% EN→Hindi/Swahili — a difficulty reservoir [2024-Khandelwal] |
| **Schwartz values / PVQ** | transfers worst (30.1% exact self-report match [2026-Yun]); knowing-doing r≈0.32 [2026-Huang-VALACT] | use only paired with behavioral enactment scenarios; score the say-do gap |
| **Social intuitionism (Haidt)** | 3 candidates, misdetected historically | dumbfounding doesn't transfer; instead measure post-hoc rationalization directly: Reason-then-Decide vs Decide-then-Reason (pre-decision reasoning is more deontological than post-hoc, CDGAP −0.178 [2025-Samway]) |
| **Dyadic morality (Gray)** | n=2 | agent-patient structure manipulation is an untouched process axis |
| **Cultural theories (Ubuntu, Confucian, Indigenous)** | 0% quality; no infrastructure | build the validated instrument FIRST (multi-year, in-tradition co-design — the KorNAT playbook); do not port Western instruments (docs 10–11) |

## 5. What discriminates when content converges (the process-probe menu)

Backed by dossier + digest evidence, the manipulations that still separate models:

1. **Reasoning-resource manipulation** (zero-shot vs CoT vs extended thinking; the Haiku +25pp CoT
   effect was unique in the battery).
2. **Perturbation flip-rates as primary metrics** (surface edits 7.5%, POV 24.3%, protocol agreement
   67.6% [2026-vanNuenen]; Yes/No + action/omission reframing: 45% flip vs human 5%, traceable to RLHF
   because base models lack the bias [2025-Cheung]).
3. **Social/emotional pressure dynamics**: persuasion CAL (flip ~50% high-ambiguity [2024-Huang]),
   directional sycophancy asymmetry [2026-MoralSycophancy], dose-response social referencing
   [2025-Li], deliberation-format effects (inertial vs conformist, OR 8.27/8.68 [2025-Sachdeva]),
   multi-agent Utilitarian Boost [2025-Keshmirian].
4. **Path-dependence / transitivity audits**: 5-step escalation exposes non-transitive preference
   structures ("context-driven statistical imitation") [2025-Wu-Staircase]; factor-level AMCE
   decomposition exposes non-human factor weighting behind human-like aggregates [2023-Nie-MoCa].
5. **Moral sensitivity in noise**: models beat humans on pre-packaged vignettes but fall below when
   identifying salient features amid distractors (β=−0.35) [2025-Kilov]; only 4% of the field tests
   information-seeking [2025-Snoswell]. Context ablation shifts agreement 64%→92% [2025-Bae].
6. **Knowing-vs-doing pairing**: self-report + behavioral scenario for the same construct (+11.9pp
   say-do gap, d=1.08 [2025-Andric]; DeNEVIL's generative attack: conformity 70→58 [2023-Duan]).
7. **Mechanistic validity checks**: value neurons <0.4% and steerable [2025-Su; 2026-Yu; 2026-Hu] —
   probe+ablate to confirm a behavioral score reflects an internal construct, not surface mimicry.

## 6. Design brief for the next moral-psychology benchmark (grounds `20-DESIGNS/03`)

- **Target the process void**: dual-process resource manipulation + moral identity cross-context
  consistency + agent-patient (dyadic) structure — the three zero-coverage, high-citation theories.
- **Discrimination as a gating validity metric**: report cross-model CV; if frontier models converge,
  the instrument measures a trained constant (MP lesson 2). Target dimensions RLHF does not homogenize.
- **Validity ≥ Level 4**: item pruning + EFA/CFA + criterion regression (the MFV two-stage pipeline
  [2015-Clifford]); human baseline with population norms on the identical instrument; N≥30 per
  model-pair with temperature/prompt perturbation (the meta-eval's own N=1 limitation).
- **Anti-recognition engineering**: novel obfuscated items, private variants, procedural generation.
- **Default AND steered profiles** (persona manipulation as diagnostic, not contamination).
- **Distributional targets**: score against human disagreement distributions with a BEST-style oracle
  [2021-Lourie-Scruples]; indecision options; consensus stratification; humans' own 10–18% test-retest
  instability propagated into error bars [2024-Boerstler].
- **Format diversity within one battery** (Likert + forced-choice + scenario + free-text + behavioral +
  multi-turn Socratic) so convergence can't be a single-format artifact (MP lesson 14).

**Drill-down:** dossier §2 (seven design axes + mechanistic layer), §3 (nine disagreements incl.
ground-truth positions and steerability reconciliation), §4 (MFV, MoReBench, MoCa, Cheung, Scruples,
Seror exemplars; ETHICS/population-mean-key/self-scoring anti-patterns). MP digest §7 (15 lessons)
and §8 (file pointers incl. the 292×158 feature matrix JSON).
