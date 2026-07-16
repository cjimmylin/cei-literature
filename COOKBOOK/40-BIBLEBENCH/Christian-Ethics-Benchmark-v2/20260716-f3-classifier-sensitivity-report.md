# F3 — 02/07 branch-classifier sensitivity (offline analysis; cross-family arm GATED)

**Date:** 2026-07-16 (session 6) · **Authorization:** free offline analysis (F3,
20260716 adjudication, JV-4b/c) — zero model calls; re-reads stored pilot logs only.
**Tool:** `tools/audit/classifier_sensitivity.py` · **Data:** `logs/pilot-20260716`
(02/07 ladders, all 5 SUTs; M3 `branch_source` provenance). Gated cross-family arm:
spend memo (`20260716-spend-memo-f5-f3.md`).

## Why this matters (the c2 chain)

On 02/07 the branch classifier reads the SUT's prior response and picks which user
turn is administered next — **the classifier is the stimulus generator** (JV-4). In
the pilot the classifier model is judge-A gpt-4.1-nano (`tasks/design02+07:
classifier_model=judge_model`) — the same judge F2 showed to be anchor-dependent and
F5 now gates. Cross-harness c2 quantified the blast radius across harnesses: only
17–19/36 design-07 turn positions received byte-identical stimuli
(`20260716-crossharness-results.md`). This report quantifies the within-harness
analogue: how much the administered stimuli depend on the classifier ROUTE.

## (a) + (b) branch_source distribution and heuristic-fallback rate

**The lexical-heuristic fallback fired 0 times in the entire pilot** — 1,435/1,435
branched turns (178×5 on 02, 109×5 on 07) were routed by the classifier model, 0 by
the heuristic, 0 misaligned records. The pilot's stimulus routing is 100%
classifier-model-dependent; the fallback is dead weight in practice (it exists for
mockllm and error degradation only).

## (c) Other-route replay: would the v1 lexical heuristic have picked the same branch?

Re-classifying every stored prior response with the v1-ported `_heuristic_branch`
(pure code, free), per design × SUT:

| cell | replayed turns | diverged | rate | ladders any-diverged / with-classifier-turn |
|---|---|---|---|---|
| 02/deepseek-chat | 178 | 91 | **0.511** | 33/36 |
| 02/gemini-flash-lite | 178 | 99 | **0.556** | 33/36 |
| 02/gpt-4.1-mini | 178 | 43 | **0.242** | 24/36 |
| 02/llama-3.3-70b | 178 | 73 | **0.410** | 31/36 |
| 02/mistral-small | 178 | 75 | **0.421** | 30/36 |
| 07/deepseek-chat | 109 | 99 | **0.908** | 27/27 |
| 07/gemini-flash-lite | 109 | 91 | **0.835** | 26/27 |
| 07/gpt-4.1-mini | 109 | 94 | **0.862** | 27/27 |
| 07/llama-3.3-70b | 109 | 90 | **0.826** | 27/27 |
| 07/mistral-small | 109 | 97 | **0.890** | 27/27 |

The divergence is structured, not noise:

- **07:** dominated by `validated→deflected` (48–82 per SUT) — the heuristic's
  residual default is "deflected" whenever its short validate-marker list misses, so
  it wildly under-detects validation. Secondary: `challenged→deflected`,
  `validated→challenged`.
- **02:** dominated by `refused→complied` (38–86 per SUT) — the heuristic's
  non-compliance marker list misses refusals phrased without stock phrases; smaller
  `complied→refused` counterflow (5–26).

## Reading (honest scope)

1. **This is route-sensitivity, not classifier error.** The v1 heuristic is a crude
   lexical rule; high divergence means the administered stimulus chain depends
   heavily on WHICH route is active — it does not mean the model classifier is wrong
   (its verdicts are plausibly much better than the heuristic's). Judging which route
   is *right* would itself need a labeled pass — out of scope here.
2. **The stimulus-instability number is far past the flag threshold.** The boot
   prompt's line was "flag if would-have-diverged > ~15% on 02/07": observed 24–56%
   (02) and 83–91% (07) per turn, with 87–100% of design-07 ladders diverging
   somewhere. **Consequence: any future multi-turn measurement MUST carry a
   pinned-classifier pre-registration line — added to the F11 draft
   (`20260716-prereg-comparisons-draft.md`, item C6).** Swapping the classifier
   (model, version, or route) changes the administered instrument, not just scoring.
3. **This mechanism is sufficient to explain c2.** v1's harness used its own
   classifier path; v2 uses gpt-4.1-nano verdict-mapping with heuristic fallback.
   With within-harness route swaps flipping 24–91% of turns, the observed ~50%
   cross-harness stimulus divergence on 07 needs no additional cause.
4. **Coupling to F5:** the pilot classifier IS judge-A. If certification (F5) leads
   to a judge-A replacement, the classifier either changes with it (new stimulus
   instrument → 02/07 results not comparable to the pilot) or must be explicitly
   pinned separately from the judge. F11's pinned-classifier line covers this; F7
   (design-07 prior-turn-context judging) remains sequenced after F3's gated arm.

## Gated arm — cross-family classifier agreement (in the spend memo; NOT run)

Re-classify the same 1,435 stored prior responses with 1–2 alternative classifier
MODELS via the byte-identical `_classify_branch` prompt (classifier-tokens only, zero
SUT re-runs; pattern = `tools/rescore/rescore.py`). Dry-run: ~1.04M input tokens +
~11.5K output tokens per model ⇒ **≈ $0.11 per alternative model** at nano-class
pricing (≈ $0.15–0.35 for mid-tier). Deliverable: cross-family per-turn agreement with
the pilot's nano route — the decision-relevant stability number (model-vs-model,
rather than model-vs-crude-heuristic).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · stored logs read-only · no holdout content.
