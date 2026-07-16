# F3 — cross-family classifier agreement RESULTS (Item 2, owner GO 2026-07-16)

**Date:** 2026-07-16 (session 6) · **Authorization:** owner GO on
`20260716-spend-memo-f5-f3.md` ("ok to spend", default package Items 1+2).
**Tool:** `tools/audit/classifier_sensitivity.py --alt-classifier` — the exact
`_classify_branch` prompt over the 1,435 stored 02/07 branched turns; classifier
tokens only, ZERO SUT re-runs. **Data:** `logs/f3-classifier-20260716/` (gitignored;
1,435 rows × 2 models, 0 errors, 0 heuristic fallbacks). Companion to the offline
half (`20260716-f3-classifier-sensitivity-report.md`).

## Headline — nano is the outlier, not the consensus

Per-turn branch-state agreement, all 1,435 turns:

| Pair | Agreement |
|---|---|
| mistral-small-3.2 vs pilot nano route | 0.721 (diverged 401, 0.279) |
| gemini-2.5-flash-lite vs pilot nano route | 0.685 (diverged 452, 0.315) |
| **mistral vs gemini (the two alternatives)** | **0.902** |
| three-way unanimous | 0.658 |
| **both alts agree AGAINST nano ("2v1")** | **350 turns = 24.4%** |

The cross-family instability is not symmetric noise: the two alternative families
agree with each other far better than either agrees with the incumbent. On a quarter
of all branch decisions, the pilot's stimulus generator picked a state that two
independent families jointly reject.

## Per-cell (design × SUT)

| cell | n | gem-div | alt-agree | 3-way | 2v1-vs-nano |
|---|---|---|---|---|---|
| 02/deepseek-chat | 178 | 0.438 | 0.871 | 0.528 | 61 |
| 02/gemini-flash-lite | 178 | 0.612 | 0.876 | 0.360 | 92 |
| 02/gpt-4.1-mini | 178 | 0.219 | 0.916 | 0.747 | 30 |
| 02/llama-3.3-70b | 178 | 0.365 | 0.927 | 0.618 | 55 |
| 02/mistral-small | 178 | 0.343 | 0.882 | 0.624 | 46 |
| 07/deepseek-chat | 109 | 0.193 | 0.945 | 0.780 | 18 |
| 07/gemini-flash-lite | 109 | 0.220 | 0.963 | 0.780 | 20 |
| 07/gpt-4.1-mini | 109 | 0.073 | 0.972 | 0.917 | 6 |
| 07/llama-3.3-70b | 109 | 0.294 | 0.771 | 0.679 | 10 |
| 07/mistral-small | 109 | 0.138 | 0.917 | 0.807 | 12 |

(mistral-vs-pilot per-cell rates: 02 0.202–0.545, 07 0.064–0.211 — same shape.)

## Structure of the disagreement

- **Design 02 is the epicenter, and it is directional:** the dominant divergence is
  `refused→complied` (mistral 256/401, gemini 319/452) — nano labels the SUT's turn
  "refused" where BOTH alternative families (and, from the offline half, the v1
  lexical heuristic) read compliance. Nano systematically over-calls "refused" on
  the 02 boundary; the counterflow (`complied→refused`) is 4–10× smaller.
- **Design 07 looks much better cross-family than it did vs the heuristic:**
  6–29% divergence here vs 83–91% in the heuristic replay — model classifiers
  broadly share the validated/challenged/deflected reading; the crude heuristic was
  the outlier there. Residual 07 disagreement is mostly `challenged→validated`.
- No alternative-model verdict failed to map (0 heuristic fallbacks, 0 errors) —
  the disagreements are genuine verdict differences, not parse artifacts.

## Consequences

1. **F11 C6 hardens as anticipated:** the branch classifier is a pinned instrument
   component — and given 0.902 alt-alt vs ~0.70 alt-nano agreement, results obtained
   under different pinned classifiers are different experiments; **no
   cross-classifier pooling, ever** (the stronger clause the spend memo pre-stated
   for exactly this outcome).
2. **02 stimulus paths are substantially nano-idiosyncratic.** Any 02 ladder claim
   inherits a stimulus chain that two model families dispute on ~1 in 3–4 turns.
   02 cells already carry R11's classifier-route caveat; this quantifies it. A
   v-next owner decision (NOT taken here): keep nano as the pinned 02 classifier,
   switch, or adopt a consensus route — each choice creates a new instrument version
   under C6.
3. **07's cross-family stability is moderate-to-good** (0.77–0.97 alt-agree),
   which narrows F7's scope: the prior-turn-context judging experiment can proceed
   on a stimulus base that model families largely agree on.
4. Note the judged-vs-generated distinction: F5 certified nano as a conclusion-
   neutral JUDGE; this finding is about nano as a CLASSIFIER (stimulus generator).
   Certification does not speak to classification quality, and vice versa.

## Spend

2,870 calls (~2.1M in / ~23K out total across both models), estimated ≈ $0.21–0.30
vs Item-2 ceiling $0.65 — within envelope. Session-6 total (Items 1+2) ≈ $0.25–0.35
vs the $1.15 package ceiling (OpenRouter dashboard = source of record). Item 3
(F2-2c) remains UN-FIRED — it was opt-in and the GO did not name it.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · stored logs read-only · no holdout content.
