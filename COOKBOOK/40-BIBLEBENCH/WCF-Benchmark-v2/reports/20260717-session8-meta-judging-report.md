# WCF-Benchmark-v2 — Session 8: The Impact of Judging
### An out-of-benchmark OAuth meta-judging audit of the v2.4 findings

> **EXPLORATORY / NON-QUOTABLE.** All results measure rubric conformity, not accuracy. The two OAuth judges are **audit instruments only** — they never join the scoring panel, the leaderboard, or bank scoring. Single-judge headline rows are **gap-stability evidence** (sign + magnitude band); no per-single-judge significance is claimed.

**Judge configurations**

| Judge | Model | Channel | CLI | Parse-fail |
|---|---|---|---|---|
| J1 gemini | gemini-2.5-flash | incumbent panel | (bank) | — |
| J2 deepseek | deepseek-chat | incumbent panel | (bank) | — |
| J3 mistral | mistral-small-2603 | incumbent panel | (bank) | — |
| **J4** | claude-opus-4-8 (Claude OAuth, `claude -p --model opus`) | Claude OAuth | Claude Code 2.1.183 | 0/779 |
| **J5** | gpt-5.5 (ChatGPT OAuth, `codex exec`, reasoning_effort=medium) | ChatGPT OAuth | codex-cli 0.144.3 | 0/562 |

**J5 model-pin ruling.** owner-locked branch: try `gpt-5.5` pin with a 3-call smoke, fall back to verified `gpt-5.6-sol` on 400. **Smoke result: `gpt-5.5` pin accepted (3/3 parseable, no 400) — no fallback needed; `gpt-5.6-sol` NOT used.**

**Coverage.** Bank v2.4; panel = median(gemini-2.5-flash, deepseek-chat, mistral-small-2603); parser = last-match GRADE: N (harness regex). J4 graded **779** samples (superset); J5 graded **562** (full priority ladder — no rungs cut); **562 twin samples** carry both OAuth judges. J4's 779 unique samples come from 997 total grade records (checkpoint/resume retries after an OAuth-cap outage; latest grade per sample_key wins). Zero parse-failures on either OAuth channel across all 997+562 calls (grade-free replay prompts; anti-leakage by construction; explicit-tell scan 0/779).

## 1. Executive summary

1. **The headline survives independent judging and gets larger.** The v2.4 finding — gpt-5-mini > claude-haiku-4.5 on the 66-item frontier core — reproduces under every out-of-benchmark judge. Incumbent panel-3 gap **5.90** (MDD80 5.41, SIG); J4 Opus alone **19.65**; J5 GPT alone **14.55** (single-judge rows are gap-stability evidence, not significance verdicts); 5-judge median **9.25** (MDD80 5.62, SIG). Sign is stable across all five judge configurations; both OAuth judges see a larger gap than the incumbent panel.
2. **No favoritism-direction signal — if anything, anti-kin.** The cross-kin contrast τ̂ = **-5.10** points *away* from favoritism (positive τ̂ would be the favoritism signal). Read this directionally, not as a significance test: τ̂ reduces algebraically to d̄_haiku − d̄_gpt5mini (the qwen anchor cancels), so it rests on the single J4−J5 twin-difference instrument and conflates kin bias with any judge-pair × SUT interaction. Each judge grades its OWN kin relatively harsher (Opus on haiku, GPT on gpt-5-mini), the opposite of the favoritism concern; the epoch-1-only robustness variant agrees (τ̂ = -6.29). See §5.
3. **Recommendation:** the panel-3 median is a defensible instrument for v2.5+; the OAuth cross-check corroborates the sign of the headline while showing the incumbent panel is *conservative* about its magnitude. See §8.

## 2. House-style calibration

Per-judge mean grade minus incumbent panel-3 median on identical twin samples (n=562). Negative = harsher than the panel. s5 baselines (different sample base) shown for reference.

| Judge | overall | contested | complicit | steadfast | v1-kind |
|---|---|---|---|---|---|
| gemini | -4.23 | -4.37 | -5.44 | -3.83 | -2.57 |
| deepseek | -0.34 | -0.48 | +1.24 | -1.93 | -0.36 |
| mistral_small | +11.38 | +20.16 | +6.05 | +5.44 | +0.35 |
| J4 | -15.90 | -5.33 | -26.43 | -34.41 | -10.60 |
| J5 | -15.14 | -6.67 | -15.63 | -39.60 | -11.23 |

_s5 reference (panel-health, cited not recomputed): gemini overall -6.48 / contested -11.20 / anchor -15.70; deepseek +1.18; mistral +1.95._

**By SUT** (house-style delta):

| Judge | claude-haiku-4.5 | gemini-3.5-flash | glm-5 | gpt-5-mini | minimax-m3 | mistral-large-2512 | qwen3.7-plus |
|---|---|---|---|---|---|---|---|
| gemini | -6.17 | -2.71 | -2 | -3.29 | -1.14 | -4.15 | -3.57 |
| deepseek | +0.54 | -0.57 | -0.43 | -0.84 | 0 | 0 | -1.48 |
| mistral_small | +14.76 | +1.05 | 0 | +13.73 | -0.14 | +0.65 | +9.57 |
| J4 | -23.66 | -11.67 | -10.48 | -9.91 | -4.14 | -16.46 | -17.13 |
| J5 | -20.06 | -14.24 | -7.48 | -11.42 | -6.90 | -15.81 | -16.68 |

## 3. Five-judge reliability

ICC(2,k) absolute-agreement and pairwise Spearman/MAD across all five judges, on samples where all five graded.

| Stratum | n | ICC(2,k) |
|---|---|---|
| overall | 562 | 0.798 |
| contested | 252 | 0.612 |
| complicit | 123 | 0.847 |
| steadfast | 99 | 0.557 |
| v1-kind | 88 | 0.769 |

**Overall pairwise** (Spearman ρ / MAD):

| Pair | ρ | MAD |
|---|---|---|
| gemini~deepseek | 0.829 | 6.69 |
| gemini~mistral_small | 0.491 | 17.20 |
| gemini~J4 | 0.720 | 15.25 |
| gemini~J5 | 0.677 | 13.61 |
| deepseek~mistral_small | 0.451 | 15.18 |
| deepseek~J4 | 0.632 | 18.79 |
| deepseek~J5 | 0.589 | 16.75 |
| mistral_small~J4 | 0.434 | 28.40 |
| mistral_small~J5 | 0.345 | 27.31 |
| J4~J5 | 0.849 | 9.22 |

## 4. Headline sensitivity — the decision-relevant table

gpt-5-mini − claude-haiku-4.5, paired per-item on the 66-item frontier core, epochs-averaged. MDD80 = 2.80×SE (s7 convention). **Single-judge rows are gap-stability only** — single-judge MDD80 runs ~8–10; the 5-judge median is the one config that can tighten MDD80 below panel-3.

| Judge config | n | gap | SE | MDD80 | sign holds | significance |
|---|---|---|---|---|---|---|
| incumbent panel-3 (reference) | 66 | 5.90 | 1.93 | 5.41 | yes | SIG |
| gemini alone | 66 | 8.79 | 2.04 | 5.72 | yes | — (stability only) |
| deepseek alone | 66 | 4.53 | 2.17 | 6.07 | yes | — (stability only) |
| mistral-small alone | 66 | 4.87 | 2.20 | 6.16 | yes | — (stability only) |
| J4 Opus alone | 66 | 19.65 | 3.23 | 9.05 | yes | — (stability only) |
| J5 GPT alone | 66 | 14.55 | 2.89 | 8.09 | yes | — (stability only) |
| 5-judge median | 66 | 9.25 | 2.01 | 5.62 | yes | SIG |

_Significance is reported ONLY for the two panel-style rows (panel-3 and 5-judge median); single-judge rows carry no SIG/ns verdict by design (single-judge MDD80 ≈ 8–10 lacks the power). All seven configs agree the sign is positive (gpt-5-mini ahead), and both OAuth judges see a LARGER gap than the panel. The decision-relevant result: the 5-judge median gap 9.25 at MDD80 5.62 is SIG, and the panel-3 reference 5.90 at MDD80 5.41 is SIG._

## 5. Cross-kin symmetry

d = J4-J5 per twin epochs-core sample; tau = (dbar_haiku - dbar_qwen) - (dbar_gpt5mini - dbar_qwen); positive tau = symmetric mutual in-group favoritism. J4 (Opus) is Anthropic-kin to the haiku SUT; J5 (GPT) is OpenAI-kin to the gpt-5-mini SUT; qwen is mutual non-kin anchor. Per-sample d = J4−J5 on 462 twin core samples; item-clustered bootstrap (5000 reps) over 66 items.

| Quantity | value |
|---|---|
| d̄ (haiku), n=198 | -3.60 |
| d̄ (gpt5mini), n=198 | +1.50 |
| d̄ (qwen), n=66 | -0.36 |
| Anthropic-kin component (d̄_haiku − d̄_qwen)† | -3.23 |
| OpenAI-kin component (d̄_gpt5mini − d̄_qwen)† | +1.87 |
| **τ̂** (default, haiku/gpt5mini epochs 1–3) | **-5.10** |
| τ̂ 95% CI (item-clustered, 5000 reps) | [-9.268, -1.091] |
| τ̂ robustness (epoch-1-only, all three SUTs n=66) | -6.29 |
| τ̂ robustness 95% CI | [-11.136, -1.439] |

**Identification caveat (load-bearing).** tau reduces algebraically to dbar_haiku - dbar_gpt5mini (the qwen anchor cancels); qwen is a displayed baseline only. tau conflates kin favoritism with any J4-vs-J5 x SUT-pair interaction and rests on ONE (twin-difference) instrument, so 'CI excludes zero' is itself an inferential claim carrying the single-instrument caveat. We therefore read τ̂ **directionally**, not as a significance test: it shows no favoritism-direction (positive) signal and a point estimate on the anti-kin side, corroborated by the epoch-1-only variant (τ̂ = -6.29, same sign). †_The displayed qwen d̄ and kin components are epoch-imbalanced (qwen J5 = epoch-1 only, n=66, vs haiku/gpt-5-mini n=198); they do NOT enter τ̂ because the anchor cancels, so they are shown as a sanity baseline only._

## 6. Item-level artifacts — top-10 s7 discriminators

Per-SUT mean and 3-SUT spread on each high-discrimination item, under the panel vs each OAuth judge. Persistent spread = real item discrimination, not an incumbent-judge artifact.

| Item | panel spread | J4 spread | J5 spread |
|---|---|---|---|
| COMP-N-015 | 70 | 24.33 | 61.67 |
| COMP-N-020 | 45 | 43.33 | 67 |
| CONT-N-022 | 39.33 | 26.66 | 48.33 |
| COMP-N-008 | 35.67 | 91.34 | 42 |
| COMP-N-022 | 35.67 | 74.34 | 44.33 |
| COMP-N-004 | 33 | 91.33 | 96 |
| COMP-N-007 | 33 | 84.33 | 88 |
| COMP-N-023 | 33 | 66.33 | 72.33 |
| COMP-N-024 | 33 | 85.33 | 71.00 |
| COMP-N-021 | 31.33 | 73.33 | 90 |

_Discrimination persists (OAuth spread ≥ half the panel spread) for 9/10 items under J4 and 10/10 under J5; it collapses under BOTH OAuth judges for 0/10 — so the top-discriminator signal is overwhelmingly real item discrimination, not an incumbent-judge artifact. Several items (e.g. COMP-N-004/007) show a LARGER spread under the OAuth judges._

## 7. GATE-cap consistency

On 37 cap-eligible twin samples (any incumbent grade <=40 on the sample), per-judge rate of emitting a ≤40 (cap-signal) grade.

| Judge | cap-signal rate |
|---|---|
| gemini | 0.946 |
| deepseek | 0.568 |
| mistral_small | 0.405 |
| J4 | 0.811 |
| J5 | 0.784 |

## 8. Threats, limitations, and the v2.5+ recommendation

**Contamination bound.** Explicit-tell scan: 0/779 prompts contain model/vendor self-identification strings, so the residual channel is stylistic (markdown habits, not vendor names). Style-normalized re-grade (n=21): mean delta -0.95, mean |delta| 6.95, max |delta| 59 — a small bound on style-channel contamination of the kin estimate.

**Limitations.** (1) Single-judge MDD80 (~8–10) lacks power for per-judge significance — only the panel-3 and 5-judge-median rows carry significance verdicts, by design. (2) J5 qwen coverage is epoch-1 only (ladder rung 1), so the DiD anchor rests on fewer qwen epochs than the kin SUTs. (3) OAuth judges are subscription-metered; concurrency and rate caps forced checkpoint/resume (one transient outage re-graded clean). (4) All numbers are EXPLORATORY / rubric-conformity, not accuracy or quotable leaderboard values.

**Recommended judging configuration for v2.5+.**

- **Keep the panel-3 median** as the scoring instrument. Two fully independent, out-of-benchmark judges corroborate the *sign* of the headline, and both see a *larger* gpt-5-mini advantage — so the incumbent panel is conservative, not inflationary, about the finding that matters.
- **Do not merge the OAuth judges into the panel** (config-break rule; they remain audit instruments). Their value is exactly their independence.
- **The kin-favoritism worry is not supported** by this audit — retain the panel without a kin-exclusion rule for the current SUT set, but re-audit if an Anthropic- or OpenAI-family model is ever added to the scoring panel itself.

---
_Bank v2.4 · panel median(gemini-2.5-flash, deepseek-chat, mistral-small-2603) · parser last-match GRADE: N (harness regex) · J4 claude-opus-4-8 (Claude OAuth, `claude -p --model opus`) · J5 gpt-5.5 (ChatGPT OAuth, `codex exec`, reasoning_effort=medium) · Claude Code 2.1.183 / codex-cli 0.144.3. OAuth-judge numbers never appear in a leaderboard-style table with panel-median rows; they are instrument-difference audits only._
