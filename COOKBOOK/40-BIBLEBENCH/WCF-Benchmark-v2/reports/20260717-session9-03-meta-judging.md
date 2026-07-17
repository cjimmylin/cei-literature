# WCF-Bench-v2 — Meta-Judging: Judging the Judges

**Report 3 of 6 · Scale-Up Readiness Briefing · 2026-07-17 · internal**

> **EXPLORATORY / NON-QUOTABLE.** All scores are 0–100 panel-median rubric
> conformity, not accuracy. The two out-of-benchmark OAuth judges (J4, J5) are
> **audit instruments only** — they exist to test the incumbent panel and **never**
> enter a leaderboard row or the scoring panel itself.

---

## 1. Why this audit exists, and what it did

The benchmark's scores are produced by a 3-model LLM panel (gemini-2.5-flash,
deepseek-chat, mistral-small-2603, combined by median). Session 7 produced the first
resolved within-tier-1 result — **gpt-5-mini beats claude-haiku-4.5 by 5.90 points on
the 66-item frontier core (SIG)**. Before trusting a headline that a *panel of LLMs*
generated, session 8 asked the obvious adversarial question: **is that finding a
property of the models, or an artifact of these particular judges?**

**Design.** Session 8 re-graded the *persisted* session-7 model responses with two
fully independent, out-of-benchmark judges, replaying the **grade-free** grading
prompt so no prior grade could leak (anti-leakage **by construction**):
- **J4 = claude-opus-4-8** via Claude OAuth (`claude -p --model opus`)
- **J5 = gpt-5.5** via ChatGPT/Codex OAuth (`codex exec`)

**Integrity of the run:** an explicit-tell scan found **0/779** prompts containing
model/vendor self-identification; **zero parse failures across 997 + 562 grader
calls**; **$0 OpenRouter** (OAuth subscriptions only). J4 covered 779 samples
(superset); J5 covered 562; 562 "twin" samples carry both. Combined with the 3 panel
judges, this yields a **5-judge** view of the same responses.

> **A blocker we caught before shipping.** An adversarial reviewer flagged that the
> draft had stamped SIG/ns verdicts on **single-judge** rows. Single-judge
> configurations have MDD80 ≈ 8–10 and lack the power for a significance verdict. The
> rule — carried into every table below — is: **single-judge rows are gap-stability
> evidence only; significance is reserved to the panel-3 and 5-judge-median rows.**

---

## 2. Finding 1 — The headline survives, and strengthens

gpt-5-mini − claude-haiku-4.5 gap on the 66-item frontier core (epochs-averaged,
paired per item), across judge configurations:

> **EXPLORATORY / NON-QUOTABLE.** Significance ("SIG") is shown **only** for the two
> panel-style rows; single-judge rows carry **no** verdict by design.

| Judge configuration | n | gap | SE | MDD80 | verdict |
|---|---:|---:|---:|---:|---|
| incumbent **panel-3** (reference) | 66 | **5.90** | 1.93 | 5.41 | **SIG** |
| gemini alone | 66 | 8.79 | 2.04 | 5.72 | — (stability only) |
| deepseek alone | 66 | 4.53 | 2.17 | 6.07 | — (stability only) |
| mistral-small alone | 66 | 4.87 | 2.20 | 6.16 | — (stability only) |
| **J4** (claude-opus-4-8) alone | 66 | 19.65 | 3.23 | 9.05 | — (stability only) |
| **J5** (gpt-5.5) alone | 66 | 14.55 | 2.89 | 8.09 | — (stability only) |
| **5-judge median** | 66 | **9.25** | 2.01 | 5.62 | **SIG** |

**Read:** the sign is positive in **all** configurations — gpt-5-mini leads under
every judge. Both out-of-benchmark judges see a **larger** gap than the incumbent
panel (J4 19.65, J5 14.55 vs panel 5.90). The two decision-relevant rows are both
significant: the 5-judge-median gap is **9.25 (MDD80 5.62, SIG)** and the panel-3
reference is **5.90 (MDD80 5.41, SIG)**.

**What it means:** the incumbent panel is **conservative, not inflationary**, about
the finding that matters. An external skeptic swapping in the two strongest available
judges would conclude the gap is *bigger*, never that it disappears. This is the
single most important result for trusting the leaderboard.

---

## 3. Finding 2 — No kin favoritism (read directionally)

The kin worry: does J4 (an Anthropic model) inflate its Anthropic kin (haiku), or J5
(an OpenAI model) inflate its kin (gpt-5-mini)? A cross-kin difference-in-differences
(DiD) tests it. Let d̄ = mean(J-judge − panel) per SUT:

| Quantity | value |
|---|---:|
| d̄ (haiku), n=198 | −3.60 |
| d̄ (gpt-5-mini), n=198 | +1.50 |
| d̄ (qwen), n=66 | −0.36 |
| Anthropic-kin component (d̄_haiku − d̄_qwen)† | −3.23 |
| OpenAI-kin component (d̄_gpt5mini − d̄_qwen)† | +1.87 |
| **τ̂** | **−5.10** |
| τ̂ 95% CI (item-clustered bootstrap, 5000 reps) | [−9.268, −1.091] |
| τ̂ robustness (epoch-1-only, all three SUTs n=66) | −6.29 |
| τ̂ robustness 95% CI | [−11.136, −1.439] |

Each judge grades its **own** kin relatively **harsher** (Opus on haiku, GPT on
gpt-5-mini) — the *opposite* of the favoritism concern.

> **Identification caveat (load-bearing).** τ̂ reduces algebraically to
> d̄_haiku − d̄_gpt5mini (the qwen anchor cancels); qwen is a displayed baseline only.
> τ̂ conflates kin favoritism with any J4-vs-J5 × SUT-pair interaction and rests on
> **ONE** (twin-difference) instrument, so "CI excludes zero" is itself an inferential
> claim carrying the single-instrument caveat. We therefore read τ̂ **directionally**,
> not as a significance test: it shows no favoritism-direction (positive) signal and a
> point estimate on the anti-kin side, corroborated by the epoch-1-only variant
> (τ̂ = −6.29, same sign).

† The displayed qwen d̄ and kin components are epoch-imbalanced (qwen J5 = epoch-1
only, n=66, vs haiku/gpt-5-mini n=198); they do **not** enter τ̂ because the anchor
cancels, so they are shown as a sanity baseline only.

**What it means:** there is no evidence of kin favoritism, and the point estimate
leans anti-kin — but this is a **directional** read on a single instrument, never a
significance claim. It is enough to say "no kin-exclusion rule is needed for the
current SUT set"; it is **not** enough to publish "judges penalize their own kin" as a
measured effect.

---

## 4. Finding 3 — Five-judge reliability

ICC(2,k) absolute-agreement across the 5 judges, and the tightest/widest pairwise
concordances:

| Stratum | n | ICC(2,k) |
|---|---:|---:|
| **overall** | 562 | **0.798** |
| complicit | 123 | 0.847 |
| v1-kind | 88 | 0.769 |
| contested | 252 | 0.612 |
| steadfast | 99 | 0.557 |

| Judge pair | Spearman ρ | MAD |
|---|---:|---:|
| **J4 ~ J5** (the two OAuth judges) | **0.849** | 9.22 |
| gemini ~ deepseek (tightest incumbent pair) | 0.829 | 6.69 |
| mistral-small ~ J4 (widest) | 0.434 | 28.40 |
| mistral-small ~ J5 (widest) | 0.345 | 27.31 |

**Read:** overall inter-judge reliability is solid (ICC 0.798). The two independent
OAuth judges — different vendors, different training — agree with each other at
ρ = 0.849 (MAD 9.2), a genuine cross-vendor concordance (a strong candidate for a
figure in the paper). Reliability is highest on **complicit** (0.847) and lowest on
**steadfast** (0.557), which tracks Finding 4: the molds where the OAuth judges are
harshest are where calibration spreads most.

---

## 5. Finding 4 — The house-style mechanism (why a stricter judge widens the gap)

Per-judge mean minus the incumbent panel-3 median, by mold (negative = harsher than
the panel):

| Judge | overall | contested | complicit | steadfast | v1-kind |
|---|---:|---:|---:|---:|---:|
| gemini | −4.23 | −4.37 | −5.44 | −3.83 | −2.57 |
| deepseek | −0.34 | −0.48 | +1.24 | −1.93 | −0.36 |
| mistral-small | **+11.38** | +20.16 | +6.05 | +5.44 | +0.35 |
| **J4** | **−15.90** | −5.33 | **−26.43** | **−34.41** | −10.60 |
| **J5** | **−15.14** | −6.67 | **−15.63** | **−39.60** | −11.23 |

**Read:** the OAuth judges are far harsher than the panel on **complicit** (−26 / −16)
and **steadfast** (−34 / −40), but near-panel on **v1-kind** items (−11 / −11). This
mold-specific harshness is *why* a stricter judge **widens** the gpt-5-mini − haiku
gap rather than shifting all scores down uniformly: the frontier molds where haiku is
weaker are exactly where a demanding judge deducts most. The consequence for the
benchmark is important and precise: **ordering is robust across judges; calibration is
not.** The leaderboard's *rank* claims are trustworthy; its *absolute* 0–100 values
are judge-dependent and remain non-quotable.

---

## 6. Finding 5 — Discriminators are real, not a judge artifact

The top-10 session-7 item discriminators (largest panel spread) re-checked under the
OAuth judges:

| Item | panel spread | J4 spread | J5 spread |
|---|---:|---:|---:|
| COMP-N-015 | 70.00 | 24.33 | 61.67 |
| COMP-N-020 | 45.00 | 43.33 | 67.00 |
| CONT-N-022 | 39.33 | 26.66 | 48.33 |
| COMP-N-008 | 35.67 | 91.34 | 42.00 |
| COMP-N-022 | 35.67 | 74.34 | 44.33 |
| COMP-N-004 | 33.00 | 91.33 | 96.00 |
| COMP-N-007 | 33.00 | 84.33 | 88.00 |
| COMP-N-023 | 33.00 | 66.33 | 72.33 |
| COMP-N-024 | 33.00 | 85.33 | 71.00 |
| COMP-N-021 | 31.33 | 73.33 | 90.00 |

**Read:** item discrimination (OAuth spread ≥ half the panel spread) **persists** for
**9/10** items under J4 and **10/10** under J5, and collapses under **both** OAuth
judges for **0/10**. The items that separate models under the incumbent panel also
separate them under independent judges — the discriminating signal is real item
content, not an incumbent-judge quirk.

---

## 7. Finding 6 — Small contamination bound

The kin estimate could be confounded if responses carry vendor "tells." Two checks:
- **Explicit-tell scan:** 0/779 prompts contain model/vendor self-identification
  strings — the residual channel is stylistic (markdown habits), not vendor names.
- **Style-normalized re-grade (n=21):** mean Δ **−0.95**, mean |Δ| **6.95**, max |Δ|
  59 — a small bound on style-channel contamination of the kin estimate.

**Read:** whatever stylistic signal survives is small on average and does not
plausibly manufacture the kin (non-)result.

---

## 8. What this changes about our confidence, and the recommendation

**Confidence.** The audit does exactly what an adversarial pass should: it tries to
break the headline and fails to. The gpt-5-mini > haiku ordering survives a swap to
the two strongest independent judges available and, if anything, widens; inter-judge
reliability is solid; there is no kin-favoritism signal; and the discriminating items
are judge-robust. The one honest limit it surfaces is that **absolute calibration is
judge-dependent** — which is already encoded in the benchmark's EXPLORATORY /
NON-QUOTABLE, ranks-not-values posture.

**Recommended judging configuration for v2.5+ (from the session-8 report, verbatim in
substance):**
- **Keep the panel-3 median** as the scoring instrument. Two fully independent,
  out-of-benchmark judges corroborate the *sign* of the headline and both see a
  *larger* gap — the incumbent panel is conservative, not inflationary, about the
  finding that matters.
- **Do not merge the OAuth judges into the panel** (config-break rule; they remain
  audit instruments). Their value is exactly their independence.
- **The kin-favoritism worry is not supported** by this audit — retain the panel
  without a kin-exclusion rule for the current SUT set, but **re-audit if an
  Anthropic- or OpenAI-family model is ever added to the scoring panel itself.**

**Limitations (verbatim in substance).** (1) Single-judge MDD80 (~8–10) lacks power
for per-judge significance — only the panel-3 and 5-judge-median rows carry
significance verdicts, by design. (2) J5 qwen coverage is epoch-1 only, so the DiD
anchor rests on fewer qwen epochs than the kin SUTs. (3) OAuth judges are
subscription-metered; concurrency and rate caps forced checkpoint/resume (one
transient outage re-graded clean). (4) All numbers are EXPLORATORY / rubric-conformity,
not accuracy or quotable leaderboard values.

---

*Source: `reports/20260717-session8-meta-judging-report.md` and its stats JSON
`analysis/20260717-session8-meta-judging-stats.json` (numbers are generated from the
JSON by `analysis/session8_render_report.py`). See Report 2 for the leaderboard this
audit validates and Report 4 for how the replay method was developed.*
