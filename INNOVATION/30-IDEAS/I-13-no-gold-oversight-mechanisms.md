# I-13 — Oversight as Mechanism Design for the No-Label Regime

**Tier 3** · **Gaps: G-07** · **Programs: RP-03 NOGOLD** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]

Oversight reframed as mechanism design for the no-label regime: peer prediction scores answers by mutual predictability (honesty as equilibrium, robustness GROWING with capability gap), and recursive self-critiquing keeps supervision human-tractable because critiquing a critique is easier than critiquing. Neither needs ground truth — and neither has been tested where ground truth genuinely doesn't exist.

## Key results

- **Peer prediction for truthful oversight** (Qiu, Carroll, Allen; 2601.20299, ICLR 2026 — SEARCH-CONFIRMED): ground-truth-free scoring via mutual predictability recovers truthfulness under weak supervision, and shows *inverse scaling in the good direction* — deception-resistance strengthens as the capability gap widens (reported to work at >100× where LLM-as-judge is worse-than-random at 5–20×).
- **Recursive self-critiquing** (2502.04675 — SEARCH-CONFIRMED): "critique of critique is easier than critique," recursively; supported across human-human, human-AI, and AI-AI configurations.
- **Nested-oversight scaling laws** (Engels et al.; 2504.18530 — SEARCH-CONFIRMED): quantify optimal oversight depth; debate is best at a fixed Elo gap, but *all* protocols decline as the overseen model strengthens — no protocol survives arbitrary gaps.
- **Supporting infrastructure** (SEARCH-CONFIRMED): Prover-Verifier Games (2407.13692); SCRIT/DeepCritic self-critique training (2501.05727, 2505.00662); FindTheFlaws annotated flawed reasoning (2503.22989).

## Mechanisms & caveats

The honesty equilibrium in peer prediction rests on answers being mutually predictable when truthful and un-coordinatable when not; whether that property survives when "honest" is itself contested is unsolved even conceptually (Front C open problem 3). Every result above rides on tasks with *hidden* ground truth — QA, code, math — so generalization to genuinely contested value questions is asserted, not demonstrated (the G-07 seam). The nested-oversight scaling laws impose a ceiling: the values-domain decay rate is unknown. Recursive critique assumes each critique layer is genuinely easier, which may break where normative disagreement, not error-finding, is the task.

## Implications for CEI practice   [KERNEL — FROZEN]

(a) RP-03 is the test these mechanisms are missing; CRUX's consensus tiers are the graded substrate. (b) The invariance family (swap-invariance, prior-independence) is CEI's proposed validity standard for the regime — defend the vocabulary. (c) Peer prediction's inverse-scaling property, if it holds on values, changes which oversight designs CEI recommends anywhere judges are outmatched. (d) Watch the training-side crossover: mechanism-designed reward signals would make RP-04's audit targets game-theoretic objects.

## Cross-links

- **Gaps:** G-07 (no-ground-truth oversight); adjacent G-08 (W2S for values), G-09 (judge corruption → I-14).
- **Ideas:** I-14 (judge corruption is the failure mode these mechanisms route around); I-19 (utility coherence conditions what "honest" means).
- **Programs:** RP-03 NOGOLD (direct test bed — CRUX stratified items, H1–H3, swap-invariance metrics); RP-04 HIDDENCURRICULUM (training-side crossover, kernel point d).
- **Field map:** Front C — Oversight (peer-prediction adoption trajectory; watch-list trigger "peer prediction operationalized for RLHF").

## OPUS-EXPAND checklist           (LIVING)

- [ ] Fetch 2601.20299 and extract the exact peer-prediction scoring rule + the capability-gap curve figures for RP-03 pre-registration.
- [ ] Fetch 2502.04675; catalog which critique-depth results are human-validated vs. AI-only (bears on H2 tractability).
- [ ] Extract the nested-oversight decay function from 2504.18530 and estimate a values-domain decay-rate prior for RP-03's power analysis.
- [ ] Map each protocol (direct / debate / consultancy / recursive critique / peer prediction) to the exact CRUX consensus tier where it is expected to break.
- [ ] Draft the swap-invariance / prior-independence validity definitions as a citable standalone spec (kernel point b — "defend the vocabulary").
- [ ] Confirm whether any 2026 paper has already run an oversight protocol across a consensus gradient (first-mover check per Front C watch-list).

## Sources

- 2601.20299 Peer Prediction for scalable oversight — SEARCH-CONFIRMED (P1, G-07)
- 2502.04675 Recursive Self-Critiquing — SEARCH-CONFIRMED (P2, G-07)
- 2504.18530 Scaling Laws for Scalable Oversight — SEARCH-CONFIRMED (P2, G-07)
- 2407.13692 Prover-Verifier Games; 2501.05727 SCRIT; 2505.00662 DeepCritic; 2503.22989 FindTheFlaws — SEARCH-CONFIRMED
- Companion: `../02-gap-atlas.md` §G-07; `../10-FIELD-MAP/C-oversight.md`; `../05-research-programs/RP-03-NOGOLD.md`
