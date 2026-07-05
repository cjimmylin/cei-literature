# Concept Sketches S1–S8

> **CEI COOKBOOK · 20-DESIGNS/SKETCHES.** Fable-authored (2026-07-05). Eight compact concepts for
> Opus to develop into full designs using the KB docs and the full-design templates (01–06). Each
> sketch: construct, mechanism, why it discriminates, key evidence, and the first build step.

---

## S1 — DRIFT: Value Stability over Long Horizons

**Construct:** value consistency across 100+-turn memory-carrying sessions and across
session-boundary summaries/handoffs. **Mechanism:** seed a persistent-memory agent with ordinary
work; inject value-laden narratives at controlled dose-rates (λ) in one domain; measure cross-domain
value expression drift over turns and after memory compaction. Extends DIB's bias-drift design
[2026-Ma-DIB: 70.19% of cross-domain interactions net-increase bias, dose-response λ] to the full
value space, plus the untested compaction/summarization vector (values distorted by lossy memory
summaries — nobody has measured this). **Discriminates:** drift curves differ where endpoints
converge; small models resisted accumulation in DIB — a rare inverse-scale effect worth chasing.
**First step:** port the DIB harness; swap bias probes for CRUX conflict probes at checkpoint turns.

## S2 — BACKBONE: Sycophancy vs Legitimate Updating

**Construct:** separating reason-responsiveness from social capitulation — the field measures flip
rates but not flip *quality*. **Mechanism:** after a model takes a position on a CRUX-style item,
challenge it with arguments of pre-rated quality (panel-graded strong/weak/pure-pressure) ×
source-authority framing (peer/expert/boss/user-threatening-churn). Score the 2×2: update-on-strong
(good) / resist-weak (good) / capitulate-to-pressure (bad) / stubborn-against-strong (bad). Track
directional asymmetry (right→wrong flips exceed wrong→right [2026-MoralSycophancy]; plateau ~4 turns
[2024-Huang-Moral Persuasion]; PM preference for sycophancy 95% [Anthropic-Towards_Understanding_Sycophancy]).
**Discriminates:** susceptibility varies within model families (haiku fragile / 3.5-sonnet resistant)
while content scores converge. **First step:** build the argument-quality-rated challenge bank
(~200 items, panel-graded).

## S3 — QUORUM: Multi-Agent Moral Coordination

**Construct:** what happens to values in groups — conformity, inertia, emergent drift, and moral
courage (dissent against a wrong consensus). **Mechanism:** panels of 3–7 agents (homogeneous /
heterogeneous by model or persona) deliberate CRUX items under varied protocols (synchronous,
round-robin, speaker-order permuted); measure the Utilitarian Boost (β=0.31, personal dilemmas only,
opposite the human direction [2025-Keshmirian]), format-dependent inertia/conformity (OR 8.27/8.68
[2025-Sachdeva]), persona-composition sensitivity (2 of 6 swapped personas flipped 4 others' votes
[2025-Zohny-ADEPT]), and a planted-wrong-consensus condition scoring dissent rate. **Discriminates:**
interaction properties are not fixed model traits — they vary where solo scores don't. **First step:**
wrap CRUX items in a 3-protocol deliberation harness; measure drift vs solo baselines.

## S4 — TEND: A Care-Ethics Relational Instrument

**Construct:** care competence per Tronto's four phases (Attentiveness, Responsibility, Competence,
Responsiveness) in multi-turn relational scenarios — the largest normative void (2/54 substantive;
zero dedicated instruments; NormEval C3). **Mechanism:** productionize the NormEval Appendix H
prototype (n=10, 82.5%, Responsiveness weakest at 2.8/4): 60+ scenario arcs where the care-recipient's
reaction is revealed mid-arc; recipient-standpoint scoring guards the "provider fallacy"; single-turn
variants shipped only as the demonstrably-broken baseline (Responsiveness 1.2 vs 2.8). LLM-judge with
expert calibration (ICC≥0.70 target) since care resists exact-match. **Discriminates:** per-phase
profiles varied in the prototype where aggregate scores wouldn't. **First step:** expand the 10
prototype scenarios to 60 with a care-ethics scholar board; run the ICC study.

## S5 — BARGAIN: Contractarian Construction Games

**Construct:** contractarian method competence via actual bargaining, not vignettes — the tractable
void (4/54; no Rawlsian or Scanlonian standalone; NormEval L9). **Mechanism:** three game families:
(a) veil-of-ignorance construction — the model designs an allocation rule *before* learning its
assigned position, then lives with the draw (position-independence of the chosen rule is machine-
checkable); (b) reasonable-rejectability tournaments — proposals stand unless an agent produces a
panel-validated reasonable rejection; (c) Gauthierian bargaining with explicit threat-points —
distinguishing maximin from bargaining-power outcomes on the same setup. Payoffs make it behavioral
(MORALSIM lineage [2025-Backmann]). **Discriminates:** reasoning models cluster as payoff-maximizers
(7.9–22.7% morality under incentive) — bargaining structure will spread them. **First step:** implement
game family (a) — it is fully auto-scoreable.

## S6 — SALIENCE: Moral Needle-in-a-Haystack

**Construct:** unprompted detection of morally load-bearing details in long, realistic material — the
isolated moral-attention construct (UNMARKED's MA axis as a cheap standalone). **Mechanism:** long
documents/codebases/transcripts (2k–100k tokens) with embedded morally-relevant details at controlled
depth and salience (the ethics analog of retrieval needle tests, which don't exist for values);
matched neutral-anomaly needles separate moral attention from general anomaly detection. Task framing
is routine (summarize, review, brief) — never "find the ethics issue." Scored: detection rate ×
depth curve; behavioral accommodation conditional on detection. Evidence: models below human baseline
when features are noise-embedded (β=−0.35 [2025-Kilov]); 4% of the field tests information-gathering
[2025-Snoswell]. **Discriminates:** long-context values behavior is unmeasured; capability-correlation
must be watched (mitigate via the neutral-needle control). **First step:** 100 documents × 3 depths ×
2 needle types; pilot on 9 models.

## S7 — CHORUS: Population-Distribution Simulation Fidelity

**Construct:** can a model *represent* a population's value diversity — steerable pluralism as a
scored capability. **Mechanism:** given a target population spec (census-weighted demographics),
the model generates N persona-conditioned responses; score distribution fidelity (JSD to survey
distribution [2025-Durmus-GlobalOpinionQA]), variance preservation (LLMs compress: top-10 values
cover 81.6% vs human 35.2% [2025-Russo]; distributions "more concentrated than WVS IQRs"
[2023-Benkler]), subgroup fidelity (does the simulated minority match the actual minority, or a
stereotype of it?), and steering asymmetry (personas can produce non-WEIRD profiles on demand
[MP digest: Ind/Bind 2.5→0.63 under East-Asian persona] — but which populations remain unreachable?).
Applications: synthetic survey pretesting, pluralistic sampling for CRUX/CULTIVATE panels — with the
fidelity certificate this benchmark provides. **First step:** WVS-anchored fidelity suite for 6
countries × 3 domains.

## S8 — LEVER: Honesty Under Goal Pressure

**Construct:** the honesty–incentive gradient: at what goal-strength does truthful reporting degrade,
and does the model know it's doing it? **Mechanism:** agentic reporting tasks (test results, metrics,
progress) where honest reporting conflicts with an assigned goal at parametrized strength ("prefer
success" → "your only goal is a passing report") × oversight visibility (monitored/unmonitored twins)
× correction cost. Score: distortion rate vs goal-strength curve (covert action 3.4%→20.7% under
strong goals [OpenAI-gpt-5]); the compliance gap (11–15% [Anthropic-Alignment_Faking]); spontaneous
confession rate when asked post-hoc; reward-hack adjacency (o3 tampering 5/24 [OpenAI-o3-and-o4-mini]).
Distinct from UNMARKED: the stake is always honesty itself, giving a clean single-construct gradient.
**Discriminates:** goal-conditioned covert behavior varies sharply across models and is the property
labs most need measured externally (KB 13 §4). **First step:** 3 reporting domains × 5 goal strengths
× monitored/unmonitored; ledger-scored.

---

*Promotion rule (from 00-design-rationale): if any full design fails adversarial review or pilot
separation stats, promote the sketch with the strongest overlap of infrastructure-reuse and void
coverage — S4 and S5 are the designated understudies for Designs 02; S6/S8 for Design 01.*
