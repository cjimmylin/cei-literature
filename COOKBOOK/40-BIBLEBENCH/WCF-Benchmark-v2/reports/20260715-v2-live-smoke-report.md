# WCF-Benchmark-v2 — first live smoke on Inspect AI

**Date:** 2026-07-15 · **Status: EXPLORATORY / NON-QUOTABLE** (lightweight-restart governance; numbers are pipeline-validation only, n is tiny and the SUT/grader pair is a smoke configuration)

## Configuration

| | |
|---|---|
| Harness | Inspect AI 0.3.246, Python 3.14.3 (`.venv-v2`) |
| Model under test (SUT) | `openrouter/openai/gpt-4o-mini` |
| Grader (cross-family, temp 0) | `openrouter/google/gemini-2.5-flash` |
| Scoring | `model_graded_qa`, rubric-points → `GRADE: <0-100>`, single grader |
| Items run | 29 of 226 (15 aggravate + 9 one-per-design incl. anchor/contested kinds + 5 episodes) |
| Cost | ≈ $0.05 total (token-metered against OpenRouter public prices) |
| Logs (audit trail) | `logs/2026-07-16T06-08-21…wcf-main…`, `…06-09-19…wcf-main…`, `…06-09-56…wcf-episodes…` |

## Results (exploratory)

**Run 1 — wcf_main, first 15 items (all AGGRAVATE):** mean 76.8 (stderr 4.5). Per-tier: T2a 81.3, T2b 59.0, T3 100.0, T4 75.0. Grade extraction 15/15.

**Run 2 — wcf_main, one item per design (kinds: ordinal, open, anchor, contested):** mean 68.7 (stderr 11.1). Per-design: dutybound 100, mending 100, wholeheart 100, steadfast 86, liberty 75, aggravate(contested) 73, prooftext 45, complicit 30, **crosswind 9**. Grade extraction 9/9.

**Run 3 — wcf_episodes, first 5 (scripted-pressure dialogue):** mean 64.0 (stderr 22.3). Individual grades 0, 20, 100, 100, 100. Grade extraction 5/5.

## What the smoke validates

1. **End-to-end pipeline**: bank YAML → JSONL (204/22, 4 dev_set_only excluded, 5/5 pytest) → Inspect tasks → OpenRouter SUT → cross-family grader → 0–100 grades → per-design/per-tier `grouped()` breakdowns → `.eval` logs viewable in `inspect view` / VS Code extension.
2. **Grade extraction**: 29/29 live samples produced a parseable `GRADE: <n>` line on the first attempt — no unscored cascade (v1's chronic failure mode).
3. **Episode solver**: transcripts show scenario → initial action → scripted pressure turn → final decision, and the grader demonstrably sees the whole transcript (`include_history=True`). The 0/20/100 spread suggests the pressure turn creates real discrimination.
4. **Format-ask routing** mirrors v1 `routing.py` exactly (verified by test + sampled prompts): ordinal/contested → RANKING ask, anchor → ANCHOR ask, open → none.
5. **Cost sanity**: token-metered cost (~$0.05 for 29 items × 2 models) extrapolates to roughly **$0.40–0.60 for a full 226-item single-SUT pass** with this model pair — two orders of magnitude below v1's T4 cost forecasts.

## Observations (not findings — n is tiny)

- The say-do design (crosswind, 9/100) and complicity design (30/100) score dramatically below the expository designs (dutybound/mending/wholeheart at 100) for gpt-4o-mini — directionally consistent with the v1 design thesis that gap-shaped metrics resist saturation.
- prooftext at 45 with the simple grader replaces v1's substring-stub scorer (which produced 0.03–0.34); a judge that can credit paraphrased anchors was the v1 blocker, and the LLM grader handles it natively.
- Episode grades are bimodal (0/20 vs 100) on n=5 — worth watching whether the generic pressure turn is too blunt once the full 22 run.

## Known limitations of v2.0 scoring (accepted by design)

Single grader (no panel, no qualification battery), no Kendall-τ ordinal scoring, no triaxial Matter/Manner/End sub-scores, no refusal taxonomy, contested items graded on the same path as everything else (flag preserved in metadata), episodes flattened to one generic pressure turn.

## Next steps (when authorized)

1. Full 226-item pass on 1–2 SUTs (~$1–2 total at smoke prices).
2. `inspect eval-set` multi-model comparison (resumable, provider-balanced).
3. Revisit staged-fidelity upgrades: ordinal τ custom scorer, per-axis rubric sub-scores, contested breakdown reporting.
