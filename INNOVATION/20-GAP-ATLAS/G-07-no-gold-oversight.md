# G-07 — Scalable Oversight for the No-Ground-Truth Regime

**Stage C** · **Ratings S/T/F: H/H/H** · **Programs: RP-03 NOGOLD** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Scalable-oversight protocols are advertised for value questions and validated exclusively on tasks with hidden ground truth; the regime they exist for — genuinely contested normative judgment — has zero published empirical results.

## Why it matters                  [KERNEL — FROZEN]
Severity H: oversight-without-labels is the load-bearing hope for supervising superhuman systems on values; if protocols quietly fail off ground truth, the field's main safety story has a hole exactly where it matters. CEI-fit H and unique: CRUX's consensus stratification (gold/contested/no-gold) is the graded substrate such an experiment needs, and it already exists.

## Evidence                        (corpus + field)
**Corpus baseline:** scalable oversight returns 4 abstract hits; the mechanism-design line is absent.

**Field:** oversight reframed from labeling to game-theoretic mechanism design — make honesty the equilibrium rather than find the right answer (Front C causal story):
- **Peer prediction for truthfulness** (Qiu, Carroll, Allen; arXiv:2601.20299, ICLR 2026): ground-truth-free scoring via mutual predictability; **inverse scaling in the good direction** — deception-resistance strengthens as the capability gap widens (works at >100×, where LLM-as-judge goes worse-than-random at 5–20×).
- **Recursive self-critiquing** (arXiv:2502.04675): "critique of critique is easier," supported across human-human, human-AI, AI-AI.
- **Nested-oversight scaling laws** (Engels et al.; arXiv:2504.18530): quantifies optimal oversight depth; *all* protocols decline as the overseen model strengthens — no protocol survives arbitrary gaps.

Almost all of it is validated on tasks with hidden ground truth; generalization to genuinely contested value questions is **asserted, not demonstrated**.

## State of the art
This is the field's open seam: zero empirical results for any protocol on genuinely contested normative questions, and **no validity criterion where accuracy is undefined** (Front C open problems). CEI owns a generator of exactly the needed substrate — CRUX produces value-conflict items with consensus stratification (gold / contested / no-gold tiers). RP-03's methodological contribution is a validity family that does not need labels: **swap-invariance and prior-independence as accuracy-free validity criteria**. The dry run demonstrates the harness and confirms the invariance metrics compute cleanly on 30 items before scale-up. In either result direction — protocols hold or degrade across consensus tiers — the study is the field's first evidence on its own target regime.

## What closing looks like         [KERNEL — FROZEN]
M1 — the mechanism-design cluster (peer prediction, recursive critique, scaling laws) acquired. M2 — RP-03's dry run demonstrates the harness and the invariance metrics compute cleanly on 30 items. M3 — the NOGOLD study publishes protocol-degradation curves across consensus tiers with no-gold validity criteria — in either result direction, the field's first evidence on its own target regime.

## CEI response                    [KERNEL — FROZEN]
RP-03 NOGOLD, the portfolio's flagship. The methodological contribution (swap-invariance, prior-independence as accuracy-free validity) outlives any particular protocol result.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read Peer-Prediction 2601.20299 and summarize the mutual-predictability scoring rule + the >100× inverse-scaling result into §State of the art; note whether "honest" being contested breaks the equilibrium (open problem 3).
- [ ] Deep-read Nested-Oversight Scaling Laws 2504.18530 and extract the per-protocol decay-with-gap functional form to seed the values-domain decay-rate question.
- [ ] Specify the 30-item dry-run design (M2): consensus-tier stratification + the swap-invariance and prior-independence computations.
- [ ] Add a protocol × consensus-tier × capability-gap experiment matrix as the RP-03 skeleton.
- [ ] Check Front C watch-list trigger: has anyone published debate/peer-prediction on moral disagreement? If yes, file a PR — first-mover pivot to replication+critique.
- [ ] Cross-reference G-08 (weak-to-strong) and G-09 (judge corruption) as the two adjacent legs sharing the RP-03 substrate.

## Sources                         (evidence classes marked)
- Peer Prediction for truthful oversight (Qiu, Carroll, Allen) — arXiv:2601.20299 (ICLR 2026) — **SEARCH-CONFIRMED** — flagship anchor.
- Recursive Self-Critiquing — arXiv:2502.04675 — **SEARCH-CONFIRMED**.
- Scaling Laws for Scalable Oversight (Engels et al.) — arXiv:2504.18530 — **SEARCH-CONFIRMED**.
- Prover-Verifier Games — arXiv:2407.13692 — **SEARCH-CONFIRMED** (P2 context).
- Corpus baseline (scalable oversight = 4 hits) — **VERIFIED** (`../02-gap-atlas.md`).
