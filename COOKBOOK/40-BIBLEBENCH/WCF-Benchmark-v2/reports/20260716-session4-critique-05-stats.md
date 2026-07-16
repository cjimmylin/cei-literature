# WCF-Benchmark-v2 — Session-4 Adversarial Critique 05: STATISTICS & REPORTING

> **EXPLORATORY / NON-QUOTABLE.** This is an adversarial statistics audit of the
> session-3 reports and artifacts. All underlying scores are 0–100 LLM-grader
> rubric-conformity means, NOT accuracies. Nothing here is publication-grade.

**Critic lens:** Statistics & reporting. Refute-first. Every number below was recomputed
from the raw `.eval` logs (`logs/20260715-sut-sweep/`, `logs/20260715-full-pass/`) and the
grade matrix (`analysis/20260716-streamB-grade-matrix.json`), not lifted from the reports.
scipy is absent from `.venv-v2`; all SEs/t-values computed with numpy/math (t-tests use the
normal approximation, conservative at n≥16, indicative-only at n≤22). Scratch: `/tmp/wcf_scores.json`.

## Findings table

| ID | Severity | One-line |
|----|----------|----------|
| ST-01 | PILOT-BLOCKING | Leaderboard reports 6 means to 0.1 with NO SE/CI; adjacent gaps sit inside ±2–4 pt CIs |
| ST-02 | PILOT-BLOCKING | haiku (89.9) vs mistral-large (88.9) rank is NOT significant (paired t=0.76); "takes #3" is noise |
| ST-03 | PILOT-BLOCKING | Median-panel shift is model-dependent (+4.2 haiku, +10.2 4o-mini); leaderboard cannot be bridged to v2.1 default by a constant, and the panel has NEVER run on 4 of 6 SUTs |
| ST-04 | PILOT-BLOCKING | Contested kind (n=4) has ±14–24 pt CI half-widths; unusable for any between-model claim |
| ST-05 | MUST-FIX | §4 family "leader" claims: 5 of 6 are statistically indistinguishable (only qwen-WHOLE survives) |
| ST-06 | MUST-FIX | Severe ceiling: 56–68% of top-3 items at exactly 100, median 100, skew ≈ −2.1; bank has little headroom to separate frontier models |
| ST-07 | MUST-FIX | deepseek episode mean 51.2 is a 6/22-zero artifact (→70.4 without zeros); reported to 0.01 with no SE (actual ±18) |
| ST-08 | MUST-FIX | Episode-only means (n=22) and ordinal (n=16) carry ±5–9 pt / ±3 pt SE but are reported as point values driving prose |
| ST-09 | DEFER | Session-3 report headline mixes a paired-robust claim (qwen>haiku) with unpaired/CI-free claims under one confidence register |
| ST-10 | DEFER | "Bounded +13.7…+20.4, no rank flip" for haiku>4o is CORRECT but the bound is presented as if it generalizes to all SUT pairs |

Attacks that FAILED (survived my refutation) are in the "What survived" section.

---

## ST-01 — Leaderboard means have no SE/CI; adjacent ranks are within noise (PILOT-BLOCKING)

**Claim under attack:** session-3 report §1/§2 and streamC §2 present the six-model
leaderboard as `qwen 93.4 > haiku 89.9 > mistral 88.9 > deepseek 85.2 > llama 72.6 > 4o 69.5`
with means to 0.1–0.01 and no uncertainty.

**Recomputed (combined n=226, from the raw logs):**

| SUT | mean | SE | 95% CI half-width |
|---|---|---|---|
| qwen3.7-plus | 93.38 | 0.81 | ±1.59 |
| claude-haiku-4.5 | 89.94 | 1.04 | ±2.04 |
| mistral-large-2512 | 88.85 | 1.26 | ±2.48 |
| deepseek-chat | 85.18 | 1.72 | ±3.36 |
| llama-4-maverick | 72.58 | 1.94 | ±3.81 |
| gpt-4o-mini | 69.55 | 2.06 | ±4.03 |

The means reproduce the report exactly. But three of the five adjacent gaps
(haiku→mistral 1.09; llama→4o 3.03) are smaller than the summed CI of the pair.
Reporting rank order without SE invites the reader to over-read a ladder that is partly noise.

**Fix:** every leaderboard mean carries `± SE` (or a 95% CI) in the same table; the prose
says "qwen and the haiku/mistral cluster" not a strict 1>2>3 ordering. Round to whole points.

---

## ST-02 — haiku #2 vs mistral #3 is not a real rank (PILOT-BLOCKING)

**Claim under attack:** §1 headline: "qwen3.7-plus 93.4 takes the top spot … mistral-large 88.9 [#3]".
This asserts a 6-rung ladder.

**Recomputed (item-matched paired diffs, combined n=226):**

| Pair | Δ | SE_diff | t | verdict |
|---|---|---|---|---|
| qwen − haiku | +3.44 | 0.99 | 3.47 | **SIG** |
| haiku − mistral | +1.09 | 1.43 | 0.76 | **NS** |
| mistral − deepseek | +3.67 | 1.72 | 2.14 | SIG (marginal) |
| deepseek − llama | +12.60 | 2.07 | 6.07 | SIG |
| llama − 4o | +3.04 | 1.78 | 1.70 | **NS** |

Ranks 2 vs 3 (haiku/mistral) and 5 vs 6 (llama/4o) are statistical ties. The leaderboard is
really three tiers: {qwen} > {haiku ≈ mistral > deepseek} > {llama ≈ 4o}. The paired test
is the *right* test (same 226 items) and is generous to the report; it still refuses the
haiku>mistral and llama>4o rankings.

**Fix:** collapse the leaderboard to tiers with the two ties called out explicitly; never
write "#2 haiku, #3 mistral" without "(difference not resolvable, Δ=1.1, t=0.76)".

---

## ST-03 — The single→median-panel bridge is model-dependent and mostly un-run (PILOT-BLOCKING)

**Claim under attack:** §7/§5 frame the single-grader leaderboard as bridgeable to the v2.1
median-of-3 default via "roughly +6…+12 points for gemini-harsh SUTs, ordering grader-robust,"
i.e. a roughly-constant offset that preserves the leaderboard.

**Recomputed from the 452×3 matrix (median-of-3 vs single gemini):**

| SUT | single-gemini | median-of-3 | shift |
|---|---|---|---|
| claude-haiku-4.5 | 89.94 | 94.17 | **+4.23** |
| gpt-4o-mini | 69.55 | 79.77 | **+10.23** |

The shift is **not constant** — it is ~2.4× larger for the weaker SUT. The matrix covers
**only these two SUTs**; qwen, mistral-large, deepseek-chat, and llama-4-maverick were
**never re-graded** by the panel, so their panel means are unknown. A 2-point linear
extrapolation (shift = 30.70 − 0.294·gemini_score) projects the panel leaderboard as
qwen 96.6 > haiku 94.2 > mistral 93.4 > deepseek 90.8 > llama 81.9 > 4o 79.8 — order preserved,
but the haiku/mistral gap shrinks to **0.77** (deeper into the ST-02 tie), and this rests on
two calibration points, a *different* panel member (matrix used mistral-**small**-2603; v2.1
default names the same trio, OK) and an unverified linearity assumption. The honest statement
is not "+6…+12, ordering robust" but "the panel moves weak SUTs up more than strong ones,
compressing the top; we have measured this for 2 of 6 models only."

**Fix:** either run the median panel on all 6 SUTs before any cross-config comparison, or state
plainly that the single-grader leaderboard and the v2.1 default are **not on the same scale**
and no bridge exists for 4 of 6 models. Do not imply a constant offset.

---

## ST-04 — Contested (n=4) is unusable for any between-model claim (PILOT-BLOCKING)

**Claim under attack:** contested is a first-class "kind" (4 items) and full-pass report §
tabulates contested means (haiku 72 / 4o 54) as a finding ("hardest kinds").

**Recomputed per-model contested (the 4 raw item scores, SE, CI half-width):**

| SUT | scores | mean | SE | 95% CI half-width |
|---|---|---|---|---|
| qwen | 100,70,73,70 | 78.2 | 7.28 | ±14.3 |
| haiku | 100,70,80,40 | 72.5 | 12.50 | ±24.5 |
| mistral-large | 92,50,73,50 | 66.2 | 10.15 | ±19.9 |
| deepseek | 85,50,80,50 | 66.2 | 9.44 | ±18.5 |
| llama | 85,60,70,40 | 63.8 | 9.44 | ±18.5 |
| 4o-mini | 85,40,50,40 | 53.8 | 10.68 | ±20.9 |

Every CI half-width (±14 to ±24) exceeds most between-model gaps. The haiku 72 vs 4o 54
"contested is hard" gap (18 pts) has a difference-SE ≈ 16.4 → t ≈ 1.1, NS. With n=4 the design
mean is a coin-flip-grade estimate. Usable ONLY as a within-project qualitative flag, never for
between-model comparison, and never quoted to a whole number as if precise.

**Fix:** either grow contested to n≥15 or drop it from all comparative tables; if retained,
report the 4 raw scores, not a mean, and never rank SUTs on it.

---

## ST-05 — Family "leader" claims: 5 of 6 are statistically indistinguishable (MUST-FIX)

**Claim under attack:** streamC §4: "qwen leads on COMP, LIB, STED, WHOLE (4 of 9)",
"mistral leads on CROSS", "deepseek leads on MEND by a narrow margin."

**Recomputed (paired top-1 vs top-2 within each family, n=19–24):**

| Family | n | top-1 | top-2 | Δ | SE | t | verdict |
|---|---|---|---|---|---|---|---|
| COMP | 23 | qwen 92.6 | mistral 86.3 | 6.35 | 5.06 | 1.26 | NS |
| LIB | 19 | qwen 93.4 | deepseek 86.3 | 7.05 | 5.37 | 1.31 | NS |
| STED | 23 | qwen 94.3 | mistral 93.4 | 0.91 | 2.74 | 0.33 | NS |
| WHOLE | 22 | qwen 97.5 | mistral 87.8 | 9.68 | 4.47 | **2.17** | **SIG** |
| CROSS | 23 | mistral 95.7 | deepseek 94.9 | 0.83 | 2.02 | 0.41 | NS |
| MEND | 24 | deepseek 97.1 | qwen 96.9 | 0.25 | 1.28 | 0.20 | NS |

Only qwen-on-WHOLE survives (barely). "deepseek leads MEND" (Δ=0.25, t=0.20) and
"mistral leads CROSS" (Δ=0.83, t=0.41) are essentially random. streamC's own caveat that
"family-level means (n=19–24) are reportable" is true for a single model's mean but does NOT
license the between-model "leads on X" claims that dominate the section's prose.

**Fix:** rewrite §4 "notable patterns" to report only WHOLE and the large qualitative gaps
(e.g., llama's COMP deficit 43.4, which is a ~40-pt gap and survives); strip every "leads on"
that is <2·SE. Add a per-cell paired-SE column.

---

## ST-06 — Ceiling compression: bank has little headroom for frontier separation (MUST-FIX)

**Claim under attack:** streamA/full-pass concede the *episode* ceiling but the leaderboard
still ranks the top three (qwen/haiku/mistral) on combined means as if the main bank
discriminates them.

**Recomputed distribution at the top (combined n=226; and open kind n=161):**

| SUT | %=100 | %≥95 | %≥90 | median | skew |
|---|---|---|---|---|---|
| qwen | 67.7 | 69.9 | 77.9 | 100 | −2.18 |
| haiku | 55.8 | 57.1 | 67.7 | 100 | −2.03 |
| mistral | 58.8 | 59.7 | 68.6 | 100 | −2.23 |

On the 161 "open" items alone, 61–71% are at exactly 100. When the median item scores 100 for
all three top models, between-model separation lives entirely in the ~30–45% tail, and small
grader-noise on tail items dominates rank. This is why the haiku/mistral gap is NS (ST-02): the
instrument has saturated for frontier-class SUTs on the main bank, not just episodes.

**Fix:** report the ceiling fraction alongside the mean; add harder items (or a discriminating
rubric that reserves 100 for exceptional answers) before claiming the bank separates frontier
models. Frame qwen>haiku as "qwen has fewer tail failures," not "qwen reasons better."

---

## ST-07 — deepseek episode 51.2 is a zero-driven artifact reported without SE (MUST-FIX)

**Claim under attack:** §1/§2 "deepseek-chat 85.2 (dragged down by a severe 51.2 episode mean)"
and streamC §3 table `deepseek episode 51.23`.

**Recomputed:** deepseek episode mean = 51.23, **SD 44.1, SE 9.40, 95% CI [32.8, 69.6]**, driven
by **6 of 22 samples scored exactly 0** (compliance failures). Drop the 6 zeros → mean 70.4.
So "51.2" is a bimodal {mostly-100, 6 zeros} distribution collapsed to a midpoint that no item
occupies, reported to 0.01 with no interval. The main-vs-episode split (88.8 vs 51.2) is real
(unpaired t=3.96) but its *magnitude* (37 pts) has a ±18 pt CI.

**Fix:** report deepseek episode as "16/22 near-ceiling, 6/22 hard defections (score 0), mean
51 ± 9" — the count structure, not the misleading midpoint. Same treatment for llama episodes
(3/22 zeros, mean 68.7 ± 7.4).

---

## ST-08 — Episode (n=22) and ordinal (n=16) point-means drive prose despite ±3–9 SE (MUST-FIX)

**Recomputed episode-mean SEs:** qwen 98.77 ± 0.68, mistral 85.50 ± 4.71, llama 68.68 ± 7.44,
deepseek 51.23 ± 9.40. **Ordinal kind (n=16), haiku vs 4o (87 vs 82):** paired Δ=5.19, SE=3.18,
t=1.63 → **NS**. The report treats the 87/82 ordinal split and the 85.5/68.7 episode ordering
as findings; at these n they are indicative only. streamC correctly warns "single-item design
means are noise" — but then quotes n=16/n=22 sub-bank means to 2 decimals in the same document.

**Fix:** whole-number rounding for all n<30 sub-bank means; attach SE; downgrade ordinal-kind
between-model claims to "not resolvable at n=16."

**Note (survives):** the anchor kind (n=23) haiku vs 4o gap of 21.0 IS significant
(SE 4.81, t=4.37) — the "anchor is hard / requires verbatim Westminster citation" claim holds.

---

## ST-09 — Mixed confidence register in the headline block (DEFER)

§1 lists a grader-robust, paired-significant claim (qwen>haiku, t=3.47, robust to grader draw)
next to CI-free ordering claims (haiku>mistral>deepseek) under one "Headlines" banner at equal
confidence. At exploratory scale this is tolerable *if* the EXPLORATORY banner is trusted, but a
reader skimming headlines cannot tell the resolvable claim from the unresolvable ones.

**Fix:** tag each headline `[resolved]` / `[tier-tie]` / `[n-limited]`.

---

## ST-10 — "+13.7…+20.4, no rank flip" bound is correct but over-generalized (DEFER)

The streamB bound on the **haiku vs 4o** gap (survives all 3 graders, +13.7…+20.4, 0 flips) is
correct and I reproduce it (median-of-3 gap +14.40). My random-single-grader-per-item bootstrap
(N=5000 draws) flips haiku≤4o in **0.00%** of draws — the gap is genuinely grader-robust. The
DEFER concern: this two-SUT, wide-gap result is cited (§7, §3.3) as evidence that "SUT ordering
is grader-robust" *in general*, but the leaderboard's actual fragile pairs (haiku/mistral,
llama/4o, gaps of ~1–3) were never grader-stress-tested because the matrix has only 2 SUTs.

**Fix:** scope the grader-robustness claim to "the haiku>4o-mini gap"; do not extend it to the
adjacent frontier pairs, which are within-noise and un-tested under the panel.

---

## Power table — per-kind SE and minimum detectable difference

Per-kind SE-of-a-mean (averaged over the 6 SUTs) and the paired minimum detectable difference
(MDD ≈ 2.8·SE_diff, 80% power, α=.05 two-sided). Item-matched (paired) MDDs are what apply to
same-bank model comparisons.

| Kind | n | mean SD | mean SE (1 model) | paired MDD (approx) | usable for between-model? |
|---|---|---|---|---|---|
| open | 161 | 21.1 | 1.66 | ~3–4 pt | YES (bulk of signal) |
| anchor | 23 | 20.4 | 4.26 | ~13 pt | only large gaps (haiku>4o 21 pt SIG) |
| ordinal | 16 | 15.8 | 3.95 | ~12 pt | only large gaps (87 vs 82 NS) |
| contested | 4 | 19.8 | 9.92 | ~30 pt | **NO** |
| episode | 22 | 24.6 | 5.25 | ~14 pt | only large gaps (deepseek 51 vs qwen 99) |

**Which observed leaderboard gaps clear their MDD (combined n=226, paired SE_diff ≈ 0.99–2.07):**

| Gap | Δ | resolvable? |
|---|---|---|
| qwen − haiku | 3.44 | YES (t=3.47) |
| haiku − mistral | 1.09 | **NO** (t=0.76) |
| mistral − deepseek | 3.67 | marginal (t=2.14) |
| deepseek − llama | 12.60 | YES (t=6.07) |
| llama − 4o | 3.04 | **NO** (t=1.70) |

**Bottom line — which leaderboard gaps are real:** qwen>haiku and deepseek>llama are real;
mistral>deepseek is marginal; **haiku>mistral and llama>4o-mini are NOT resolvable.** The
combined-226 paired MDD is ~2.8 points, so any leaderboard gap under ~3 points is noise.
Contested (n=4) resolves nothing (MDD ~30). Episodes resolve only the deepseek/llama collapses.

---

## Claim guardrails at pilot scale (5 new SUTs × 226 items, single grader)

**LICENSED (the numbers support these):**
- "qwen3.7-plus has the fewest tail failures on the main bank; its combined mean (93.4 ± 0.8)
  is above the haiku/mistral cluster (paired t=3.47)."
- "There is a clear performance tier structure: {qwen} > {haiku ≈ mistral > deepseek} >
  {llama ≈ 4o-mini}, with two within-tier ties (haiku/mistral, llama/4o)."
- "deepseek-chat and llama-4-maverick show hard episode-compliance failures (6/22 and 3/22
  scored 0) — a qualitative behavioral finding independent of grader calibration."
- "The haiku > 4o-mini gap (+14 to +20 pts) is robust to grader substitution (0/5000 bootstrap
  flips) and to the median panel."
- "llama-4-maverick has a large, real COMP-family deficit (~40 pts)."
- "The anchor kind separates strong from weak SUTs (haiku>4o +21, t=4.4)."

**FORBIDDEN (the numbers cannot support these at pilot scale):**
- Any strict 1>2>3>…>6 ranking, or "haiku is #2 and mistral is #3." (ST-02)
- Any between-model claim on the contested kind (n=4). (ST-04)
- "qwen leads COMP/LIB/STED" or "deepseek leads MEND" or "mistral leads CROSS" as
  distinguishable facts. (ST-05)
- Treating the single-grader leaderboard as convertible to the v2.1 median-panel default by a
  constant offset, or quoting any panel number for qwen/mistral-large/deepseek/llama (never
  panel-graded). (ST-03)
- Any leaderboard gap < ~3 points described as a difference. (Power table)
- Ordinal-kind (n=16) or single-item design comparisons. (ST-08)
- Reporting deepseek episode "51.2" without disclosing it is a 6-zero midpoint. (ST-07)
- Any decimal precision (x.x or x.xx) on a sub-bank mean with n<30.

---

## What survived (attacks that FAILED)

- **qwen>haiku top claim.** I tried to break it as episode-driven; it holds on BOTH main
  (Δ=3.42, t=3.13, n=204) and episodes (Δ=3.64, t=2.84, n=22). Real.
- **haiku>4o-mini grader-robustness.** Random-single-grader-per-item bootstrap: 0/5000 flips;
  median-of-3 gap +14.40. The streamB "no rank flip, +14–20" bound is honest and correct.
- **All six combined means reproduce exactly** (85.18/88.85/93.38/72.58/69.55/89.94) from the
  raw logs; no arithmetic or double-counting error in the leaderboard means themselves. Kind
  counts (161/23/16/4 + 22 episodes = 226) and design counts verified against the logs.
- **The EXPLORATORY / NON-QUOTABLE banner is present on every report** — the project's own
  guardrail is real, and streamC already flags "single-item design means are noise" and "per-item
  single-design cells omitted." The reporting *discipline* exists; the gap is that it is applied
  unevenly (see ST-05, ST-08).
- **deepseek main-vs-episode split** (88.8 vs 51.2) is a real behavioral effect (unpaired t=3.96),
  not a grader artifact — the direction survives; only its precision was overstated (ST-07).

---

## Hardest verify/adjudicate step (escalation)

The single hardest judgment is **ST-03 — quantifying how much the leaderboard would move under
the v2.1 median panel.** I can only measure it for 2 of 6 SUTs (the matrix's coverage); the 4
missing SUTs are extrapolated from a 2-point linear fit whose validity I cannot check without a
real panel re-grade. Whether any rank flips under the panel is therefore genuinely
under-determined by the available data. **Recommend re-running the median-of-3 panel on all 6
SUTs (a $0-SUT re-grade of stored responses, per streamB's own method) before this stage is
adjudicated at the Fable tier.**

---

## VERDICT

**BLOCK** (for any quotable/leaderboard use) — **PASS-WITH-FIXES** (for continued exploratory
pilot work under the existing banner).

The means are arithmetically correct and the top claim (qwen>haiku) and the haiku>4o gap are
real and robust. But the leaderboard is presented as a 6-rung ladder when it is really 3 tiers
with 2 within-tier ties (ST-02), the contested kind (n=4) and the family "leader" claims (ST-05)
are unsupported, and the single→median-panel bridge is model-dependent and un-run for 4 of 6
SUTs (ST-03). Under the EXPLORATORY banner the pilot may proceed **if** ST-01/02/03/04 fixes
(tiers + SE/CI + panel disclosure + drop contested comparisons) are applied to the reports first.

**Single most likely remaining error:** that a future session quietly re-runs the leaderboard
under the median-of-3 panel and reports the new numbers *next to* the session-3 single-grader
numbers as if comparable — the ST-03 model-dependent shift (+4 vs +10) means the two configs are
on different scales, and the haiku/mistral tie could visually "flip" purely from grader
calibration, not model behavior.

*Critic 05 of 5, session-4 adversarial review. Non-quotable exploratory audit. 2026-07-16.*
