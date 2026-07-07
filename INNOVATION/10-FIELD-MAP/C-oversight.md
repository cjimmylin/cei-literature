# Front C — Oversight

**Snapshot:** 2026-07-07 · **Author:** Fable 5 · Gaps: G-07, G-08, G-09 · Programs: RP-03 NOGOLD

## Causal story

Scalable oversight was conceived as a labeling problem: humans can't check superhuman outputs, so build protocols (debate, amplification, recursive reward modeling) that let weak judges reach strong-model-quality labels. Through 2024 the empirical work stayed on tasks where ground truth secretly exists (QA with hidden answers, code with tests), because that's where you can score the protocol. 2025–26 brought two shifts. First, the honest admission that the target regime has *no* labels — and a corresponding reframe toward game-theoretic mechanism design: don't find the right answer, make honesty the equilibrium. Second, an accumulating negative literature on the judge: human and AI judges are corruptible in ways that debate-style presentation does not fix and sometimes worsens. The unresolved tension: every protocol is advertised for value questions, and none has been tested on one.

## Key results

- **Peer prediction for truthfulness** (Qiu, Carroll, Allen; 2601.20299, ICLR 2026): ground-truth-free scoring via mutual predictability; recovers truthfulness under weak supervision; **inverse scaling in the good direction** — deception-resistance strengthens as the capability gap widens (works at >100×, where LLM-as-judge goes worse-than-random at 5–20×).
- **Recursive self-critiquing** (2502.04675): "critique of critique is easier than critique," recursively; supported across human-human, human-AI, AI-AI.
- **Nested-oversight scaling laws** (Engels et al.; 2504.18530): quantifies optimal oversight depth; debate best at fixed Elo gap; *all* protocols decline as the overseen model strengthens — no protocol survives arbitrary gaps.
- **Judge-corruption cluster:** confirmation/automation bias in human overseers that two-sided presentation fails to fix (2507.19486); debaters more persuasive arguing their own priors, and belief-misaligned arguments *rated higher quality* (2510.13912); W2S deception — strong models appear aligned on the supervised objective while pursuing another (2406.11431).
- **W2S for values, pilot stage:** beyond-accuracy pilot (safety/toxicity/legal; 2410.12621) — task-dependent, weaker than the accuracy regime; W2S reward models collapse under preference shift (⚠ 2605.25629); selective-trust variants (2511.14166).
- **Debate for reward signals** (⚠ 2605.27483): debate to *train* reward models where judges are outmatched — oversight entering the training loop.
- **Infrastructure:** FindTheFlaws (2503.22989) supplies annotated flawed reasoning; DeepCritic/SCRIT scale critics without stronger teachers; DeepMind's amplified-oversight reframe around human-AI complementarity (2510.26518).

## Actors

Redwood/AI-control-adjacent groups, DeepMind (amplified oversight/debate lineage), MIT (scaling laws), academic mechanism-design newcomers (peer prediction), Chinese groups (recursive critique, SCRIT). Notably absent: anyone with contested-normative-item infrastructure.

## 12-month trajectory

Peer-prediction-family methods get adopted into at least one training pipeline; debate results keep improving on checkable tasks while the values question stays open (bet B2 — someone may run it; CEI should be first); judge-corruption findings force reporting standards for LLM-judge evals; "oversight for open-ended/normative domains" becomes a named workshop topic.

## CEI entry points (ranked)

1. **Run the missing experiment** (RP-03): protocols × consensus tiers × capability gaps, with no-gold validity criteria (swap-invariance, prior-independence) as the methodological contribution. CRUX makes CEI the only group that can do this without a year of substrate-building.
2. **Judge-corruption quantification on values content** (RP-03 metrics; RP-04 dogfood): the negative literature is on QA/safety; the values version is both missing and directly self-serving (every CEI bench uses judges).
3. **Substrate export**: the frozen stratified item set (roadmap D2) — let oversight groups test on CEI's ground; adoption builds the collaboration channel.

## Open problems (field-level)

1. Zero empirical results for any protocol on genuinely contested normative questions (RP-03's seam).
2. No validity criterion where accuracy is undefined (RP-03 proposes the invariance family).
3. Whether peer prediction's honesty equilibrium survives when "honest" is itself contested (deep; unsolved even conceptually).
4. Protocol results don't transfer across judge populations (human vs. AI judges rank protocols differently in places).
5. The ceiling problem: scaling laws say all protocols degrade with gap — what's the values-domain decay rate?

## Watch-list triggers

- Anyone publishes debate/peer-prediction on moral disagreement → RP-03 loses first-mover; pivot to replication + critique with better substrate (still strong).
- Peer prediction operationalized for RLHF → intersects RP-04 (the training signal becomes mechanism-designed); read immediately.
- A no-gold validity proposal from another group → compare against swap-invariance family; converge or contest, in a dated note.
- Frontier lab ships "AI judge disclosure" standards → cite into every CEI methods section; check RP-03 metric alignment.
