# WCF-Benchmark-v2 — first full 226-item pass (2 SUTs)

**Date:** 2026-07-15 · **Status: EXPLORATORY / NON-QUOTABLE** (single grader, no qualification battery, no human gold; scores are 0–100 rubric-conformity means, not accuracies)

## Configuration

| | |
|---|---|
| Harness | Inspect AI 0.3.246, `eval-set` (2 tasks × 2 models, 4 runs) |
| SUTs | `openrouter/openai/gpt-4o-mini`, `openrouter/anthropic/claude-haiku-4.5` |
| Grader | `openrouter/google/gemini-2.5-flash`, temp 0 (cross-family vs both SUTs) |
| Items | all 226 runnable (204 main + 22 episodes) per SUT = 452 gradings |
| Completeness | **452/452 scored, 0 unscored** (4/4 runs `success`) |
| Cost (token-metered) | haiku $1.24 + gpt-4o-mini $0.43 = **$1.67 total** |
| Wall-clock | ~5 min end-to-end |
| Logs | `logs/20260715-full-pass/*.eval` (4 files) |

## Results (0–100 rubric-conformity means)

**Overall:** claude-haiku-4.5 **89.9** · gpt-4o-mini **69.5** (n=226 each)

| Design | haiku-4.5 | gpt-4o-mini | gap |
|---|---|---|---|
| steadfast | 97 | 79 | 18 |
| mending | 95 | 66 | 29 |
| narrowgate (episodes) | 95 | 69 | 26 |
| liberty | 94 | 72 | 22 |
| wholeheart | 94 | 78 | 16 |
| crosswind | 90 | 82 | 8 |
| complicit | 88 | 44 | **44** |
| aggravate | 85 | 76 | 9 |
| dutybound | 84 | 73 | 11 |
| prooftext | 79 | 57 | 22 |

| Kind | haiku-4.5 | gpt-4o-mini |
|---|---|---|
| open (161) | 92 | 70 |
| episode (22) | 95 | 69 |
| ordinal (16) | 87 | 82 |
| anchor (23) | 79 | 57 |
| contested (4) | 72 | 54 |

## Episode pressure-turn review (handoff P2)

- **gpt-4o-mini** (mean 69.5): full-range distribution — 4 zeros, mid-band grades (57–91), 6 perfect. The generic pressure turn **discriminates** at this capability level; the four zeros are outright defections under the "your call / nobody will audit" squeeze.
- **claude-haiku-4.5** (mean 95.1): near-ceiling — minimum 78, 14 of 22 at exactly 100. The generic turn is **too blunt to discriminate at this capability level**; either the pressure is too weak, or the single lenient grader compresses the top. **v2.1 path:** per-item scripted pressure turns (restoring the v1 cost-dial specificity) and/or a stricter/multi-grader pass before trusting episode ceilings.

## Observations (exploratory)

1. **Uniform dominance with non-uniform gaps.** haiku-4.5 leads on all 10 designs; the gap concentrates in complicit (44 pts — gpt-4o-mini frequently assists in scenarios whose gold behavior is refusal/withdrawal) and mending/narrowgate (26–29 pts), and nearly closes on crosswind (8) and aggravate (9).
2. **contested and anchor are the hardest kinds for both SUTs** — contested (72/54) rewards disclosure of intra-Reformed disagreement (v1's F-3 finding that models assert confident single answers survives the harness rebuild); anchor (79/57) requires verbatim Westminster citation.
3. **Small-n smoke numbers did not survive scale** — crosswind was 9/100 in the session-1 single-item smoke vs 82/100 here (n=19); single-item design means are noise. Design-level claims need the full bank.
4. **Zero harness failures.** No parser drift, no unscored cascade, no resume needed. The grader emitted a parseable `GRADE:` line 452/452 times.

## Verification trail

- 4/4 eval runs `status: success`; completeness audited programmatically (unscored=0 per run).
- Preflight: 5/5 pytest, dataset counts 204/22 confirmed, slugs+prices re-verified against OpenRouter public list.
- Costs computed from per-model token usage in `.eval` logs × public OpenRouter prices (haiku output tokens dominate: 24k on episodes alone).

## Next steps (queued, not authorized)

1. v2.1 episode fidelity: per-item pressure turns; re-run the 22 episodes on stronger SUTs.
2. Grader robustness: multi-grader majority vote (`model_graded_qa(model=[...])`) or a second cross-family grader pass on a subsample to bound grader effect.
3. Broader SUT sweep (deepseek, llama, mistral families) — ~$0.5–1.5/model at observed prices.
