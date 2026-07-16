# WCF-Benchmark-v2 — Session 3 Stream B: Grader-Effect Bound

> **EXPLORATORY / NON-QUOTABLE.** All scores are 0–100 rubric-conformity means as
> judged by LLM graders, NOT accuracies. Nothing here is publication-grade.

**Date:** 2026-07-15 (run completed 2026-07-16 UTC)
**Question:** how much does the single incumbent grader (gemini-2.5-flash) move
scores? Is a majority-vote scorer upgrade warranted?

## Method

- **Approach: replay script** (`analysis/regrade_graders.py`), not `inspect score`.
  The installed 0.3.246 `inspect score` CLI exists, but its `--model` overrides the
  *primary* (SUT) model, while the grader is baked into the task's scorer closure via
  `model_graded_qa(model=get_model(grader_model))`; swapping it through `--scorer -S`
  re-instantiation was judged fragile vs. an exact replay. The replay is also strictly
  better for anti-leakage auditability (next bullet).
- **Anti-leakage (binding, satisfied by construction):** every session-2 sample log
  persists the *exact* grading prompt gemini received in
  `scores['model_graded_qa'].metadata['grading'][0]['content']` (template + question
  /transcript + answer + criterion + numeric instructions; verified to contain no
  grade). Each new grader was sent that prompt **byte-identically** — no gemini grade,
  no other grader's grade, no prior score is present anywhere in the input. Input set
  was `logs/20260715-full-pass/*.eval` only (no sibling-stream logs read).
- **Graders added** (slugs + prices verified live against openrouter.ai/api/v1/models
  on 2026-07-15): `openrouter/deepseek/deepseek-chat` ($0.20/$0.80 per Mtok) and
  `openrouter/mistralai/mistral-small-2603` ($0.15/$0.60). Both cross-family vs both
  SUTs and vs the incumbent. Temperature 0 to match.
- **Grade parsing:** same `GRADE:\s*(\d{1,3})` pattern; last match wins (harness
  semantics). 0 unparseable out of 904 calls.
- **Coverage: ALL 452 samples × 2 graders = 904 grading calls.** Forecast was
  ≈$0.44 (3.65M input chars ≈ 912k tokens per grader pass), well under the ~$1.5
  full-coverage threshold, so no subsampling was needed.
- **Concurrency 12, exponential backoff ×5.** deepseek pass 536 s; mistral pass 104 s.

## Receipts

- Grade matrix (452 rows × 3 graders): `analysis/20260716-streamB-grade-matrix.json`
- Raw grader completion tails (audit): `analysis/20260716-streamB-grader-raw.json`
- Agreement stats JSON: `analysis/20260716-streamB-agreement-stats.json`
- Scripts: `analysis/regrade_graders.py`, `analysis/analyze_grader_bound.py`

## Results

### Per-grader means (n = 226 per SUT)

| Scope | gemini-2.5-flash (incumbent) | deepseek-chat | mistral-small-2603 |
|---|---|---|---|
| Overall (452) | 79.74 | 88.41 | 88.31 |
| gpt-4o-mini (226) | **69.55** | 81.58 | 81.41 |
| claude-haiku-4.5 (226) | **89.94** | 95.25 | 95.22 |
| Episodes, 4o-mini (22) | 69.45 | 71.36 | 78.45 |
| Episodes, haiku (22) | 95.14 | 96.45 | 99.23 |

Gemini is the systematically **harshest** grader: deepseek and mistral sit
+8.6 points above it overall (+12.0 on 4o-mini, +5.3 on haiku), while deepseek
and mistral agree with each other on level almost perfectly (mean signed
difference −0.1). The grader effect is mostly a **calibration/level offset**,
larger on the weaker SUT (more partial-credit judgment calls to make).

### Pairwise agreement

| Pair | MAD overall | ρ overall | MAD 4o-mini | ρ 4o-mini | MAD haiku | ρ haiku |
|---|---|---|---|---|---|---|
| gemini–deepseek | 10.94 | 0.690 | 15.58 | 0.683 | 6.30 | 0.619 |
| gemini–mistral | 12.32 | 0.609 | 16.88 | 0.644 | 7.76 | 0.458 |
| deepseek–mistral | 8.17 | 0.573 | 11.20 | 0.603 | 5.13 | 0.442 |

(Haiku-side ρ is depressed by range restriction — most haiku grades cluster at
90–100 under every grader.)

### ≥30-point spread across the 3 graders

**92 / 452 samples (20.4%)** — 70 on gpt-4o-mini, 22 on haiku. Concentrated in
`open`/`anchor` kinds (75/92) and the prooftext (20), aggravate (12), mending (11),
complicit (10) designs. Worst case: MEND-A-W305 (4o-mini) graded 0 by gemini,
100 by both deepseek and mistral. Full list in the agreement-stats JSON.

### (a) Does the haiku-vs-4o-mini gap survive grader substitution?

**YES — sign preserved under all three graders; magnitude shrinks.**

| Grader | haiku | 4o-mini | gap |
|---|---|---|---|
| gemini | 89.94 | 69.55 | **+20.39** |
| deepseek | 95.25 | 81.58 | **+13.67** |
| mistral | 95.22 | 81.41 | **+13.81** |
| median-of-3 | 94.17 | 79.77 | **+14.40** |

No rank flip anywhere. Rough magnitude: the true gap is bounded ≈ **+14 to +20
points**, with the incumbent gemini at the high end (it stretches the gap because
its extra harshness lands disproportionately on the weaker SUT).

### (b) Does the haiku episode 14/22-at-100 ceiling survive?

**YES — it gets worse.** Haiku episodes at exactly 100: gemini 14/22, deepseek
16/22, **mistral 20/22** (means 95.1 / 96.5 / 99.2). The saturation is a property
of the generic pressure turn + haiku, not a gemini artifact. (4o-mini episodes
at-100 for comparison: 6 / 10 / 13.) Stream A's per-item pressure turns remain
the right fix; no grader change will break this ceiling.

### (c) Is the single grader unstable?

**Yes, by the pre-set criterion — on level, not on ranking.**
Overall pairwise MAD vs the incumbent is 10.9–12.3 (> the ~10 threshold), rising
to 15.6–16.9 on gpt-4o-mini, and 20% of samples show a ≥30-point spread. However:
no SUT rank flip, the headline gap survives with the same sign, and the two new
graders agree with each other far better (MAD 8.2, bias ≈ 0) than either agrees
with gemini — the instability is dominated by gemini's harsher calibration, not
random noise.

## VERDICT

**RECOMMEND the majority-vote (multi-grader) scorer upgrade** — the pre-registered
trigger fired (mean |Δ| > 10 vs the incumbent; 92/452 samples with ≥30-point
spread). A 3-grader ensemble (gemini + deepseek + mistral-small, median/majority)
would cost roughly 3× the current ~$0.15–0.25 grading overhead per pass — still
cents — and removes a ~6–12-point single-grader level artifact from every reported
mean. Per stream-B scope, **no change was made to `src/`**; the one-line
`model=[g1,g2,g3]` change in `wcf_scorer` is left to the orchestrator's
integration wave. If the orchestrator instead opts to keep single-grader for
comparability with session-2, the recorded bound is: **absolute levels carry a
±6–12-point grader effect; SUT ordering and the ~14–20-point haiku>4o-mini gap
are grader-robust; the haiku episode ceiling is grader-robust (survives, even
intensifies, under all 3 graders).**

## Cost

- SUT spend: **$0.00** (pure re-grade of stored responses).
- Grading spend (estimated from live prices × measured prompt volume, 904 calls):
  deepseek ≈ $0.29, mistral-small ≈ $0.22 → **≈ $0.51 total.**
- Wall clock: ~11 min (deepseek 536 s + mistral 104 s, concurrency 12).
