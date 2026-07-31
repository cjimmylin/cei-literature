# WCF-Benchmark-v2 — Session 19: FIRST QUOTABLE Results Report

**Executed:** 2026-07-31. **This is the first report in the project whose
numbers may be cited as evidence.** Every prior report/artifact (sessions
1–18, including the s17 wave report and all s16/s17 exploratory tables) stays
EXPLORATORY and must not be cited as SUT evidence — those measured an
in-flight run, an unvalidated instrument candidate, or a pre-triage headline.
This report measures the **completed** Scenario-A full run (5 SUTs × 345
items × 3 epochs = 5,175 responses, 10,350 verdicts) under the **frozen
strict-v2 instrument**, gated by a mandatory judge-gap triage (§4 below)
before any number here was treated as quotable.

## 1. Headline: panel means + per-judge sensitivity

Strict-v2, opus + GPT-5.6-Sol mean-of-2, single-packet mode, n=1,035 per SUT
(345 items × 3 epochs). Source: `analysis/session19_headline_analysis.py` →
`analysis/20260731-session19-headline-analysis.json`.

| SUT | panel mean | opus mean | Sol mean | opus − Sol |
|---|---|---|---|---|
| gpt-4o-mini | 47.55 | 46.72 | 48.38 | −1.66 |
| gpt-5-mini | **72.93** | 72.66 | 73.20 | −0.54 |
| haiku | 63.53 | 64.67 | 62.39 | +2.28 |
| minimax-m3 | **74.09** | 75.94 | 72.25 | +3.69 |
| qwen | 73.09 | 75.09 | 71.09 | +4.00 |

**Pairwise significance** (s7 MDD80 method: per-item 3-epoch-averaged scores,
paired difference, `mdd80 = 2.80 * se(diffs)`, two-sided α=.05/power=.80
normal-approximation, n=345 per pair):

- gpt-5-mini, minimax-m3, and qwen are **not significantly distinguishable
  from each other** (gaps 0.16–1.17, all below their mdd80 thresholds of
  2.6–3.4) — read as a top tier, not a ranked order.
- All other pairs ARE significant: gpt-4o-mini is significantly below every
  other SUT (gaps 16.0–26.6, well above mdd80); haiku is significantly below
  the top tier and significantly above gpt-4o-mini.
- **Ranking that survives significance testing:** {gpt-5-mini, minimax-m3,
  qwen} (tied top tier) > haiku > gpt-4o-mini. Full pairwise table in the JSON
  artifact.

## 2. Frontier-core vs. full bank

Frontier-core = the 146 authored `-N-` items (`analysis/20260724-session13-frontier-core-index.json`,
v2.5) that superseded the original v1 items specifically because the v1 items
had ceiling-flattened (stopped discriminating between models). This full run
confirms that design intent held under a completed, 3-epoch, 5-SUT
measurement:

| SUT | frontier-core mean (n=438) | non-frontier-core mean (n=597) | gap |
|---|---|---|---|
| gpt-4o-mini | 38.54 | 54.16 | −15.6 |
| gpt-5-mini | 66.57 | 77.59 | −11.0 |
| haiku | 51.70 | 72.22 | −20.5 |
| minimax-m3 | 64.98 | 80.78 | −15.8 |
| qwen | 65.91 | 78.35 | −12.4 |

Every SUT scores 11–21 points lower on frontier-core items than on the rest
of the bank — frontier-core is measurably harder across the whole roster, not
just relative to the two originally-characterized SUTs (qwen/haiku) it was
authored against.

## 3. Per-mold breakdown

Panel mean by item family (mold) × SUT:

| Mold | n items | gpt-4o-mini | gpt-5-mini | haiku | minimax-m3 | qwen |
|---|---|---|---|---|---|---|
| AGG | 24 | 64.90 | 78.50 | 73.57 | 80.48 | 80.35 |
| COMP | 40 | 29.03 | 67.78 | 46.23 | 58.73 | 55.42 |
| CONT | 36 | 44.49 | 68.38 | 61.68 | 64.62 | 63.68 |
| CROSS | 23 | 61.07 | 90.61 | 67.76 | 82.72 | 83.05 |
| DUTY | 21 | 64.65 | 85.35 | 66.61 | 78.73 | 79.07 |
| LIB | 39 | 47.02 | 71.10 | 63.30 | 79.71 | 80.55 |
| MEND | 41 | 49.90 | 80.49 | 75.45 | 84.95 | 80.65 |
| PROOF | 43 | 37.48 | 59.02 | 54.71 | 62.99 | 68.63 |
| STED | 36 | 48.38 | 70.98 | 73.26 | 76.96 | 68.52 |
| WHOLE | 42 | 49.71 | 72.86 | 61.29 | 79.26 | 79.56 |

**COMP is the single hardest/most discriminating mold for gpt-4o-mini**
(29.03, ~19 points below its own overall mean) — compliance/dual-constraint
items are disproportionately where the weakest SUT fails outright. **PROOF is
the hardest mold overall** (all 5 SUTs score below their own average) —
apply-not-quote Scripture/confession handling remains the most uniformly
difficult skill in the bank.

## 4. Judge-gap triage (MANDATORY gate for this report's quotable status)

Full record: `analysis/20260731-session19-judge-gap-triage.md`. A stratified
90-cell sample (28.7%) of the 314 cells with `|opus−Sol| ≥ 30` (6.1% of all
5,175), blind-audited one-packet-per-fresh-opus-agent, raw materials only
(anti-leakage, no scores/verdicts shown to the auditor):

- **90.0% (81/90) of sampled high-disagreement cells are idiom-attributable**
  — 54.4% COMPLIANCE_THEATER (rubric vocabulary/citations performed without
  the substance satisfying them), 35.6% ADVISORY_PROSE (fluent theological
  prose that never delivers the rubric's required concrete artifact). Only
  6.7% are genuine good-faith rubric-application disagreement; 3.3% reflect
  rubric/key problems, not response quality (one mechanical GATE-application
  miss, one flat over-refusal with no rubric anchor for it, and one confirmed
  rubric self-contradiction in a single item, flagged for a future
  clarification pass — not fixed here).
- **Direction refines, does not overturn, the standing opus-known-lenient
  disclosure:** of the 81 idiom cells, opus scored higher than Sol in 79.0%
  (64/81) — consistent with the disclosure. But Sol was the more lenient
  judge on the remaining 21.0% (17/81) of idiom-exhibiting responses — the
  idiom is a property of certain SUT response styles, and while opus is
  disproportionately susceptible, Sol is not immune.
- Per-SUT idiom mix differs qualitatively: gpt-4o-mini and gpt-5-mini skew
  COMPLIANCE_THEATER-heavy; haiku skews ADVISORY_PROSE-heavy (13/21) —
  plausibly reflecting haiku's more frequent refusal-with-description style
  versus gpt-4o-mini's more frequent rubric-vocabulary-performance style.
  Directional at n=90, not a precise per-SUT estimate.

**Conclusion:** the near-zero mean opus−Sol gaps in §1 are not judges quietly
agreeing — they average out large, idiom-driven per-cell divergence at a rate
that dominates 9 of 10 sampled high-disagreement cells. Per-judge sensitivity
columns (§1) are the load-bearing disclosure, not the panel mean alone.

## 5. Instrument reliability

Panel ICC(2,1) = **0.985** (opus .948 / Sol .996), from the s16 A3 stability
run (`analysis/20260724-session16-instrument-freeze.json`). The instrument
(strict-v2, sha `c32fee45652008e724c304a3e6df8c1d4ee43b055a7439d826f1ab0048d6e650`)
never changed after that measurement — the s17 strict-v3 gate failure and
auto-revert (§7) is a disclosed methodological episode about a
**rejected candidate**, not a validity threat to the frozen v2 instrument
this report's numbers are measured under. No re-measurement was needed.

## 6. Three-epoch consistency

Mean absolute deviation of a single epoch's score from that item's 3-epoch
mean, and the share of single-epoch observations that would have been off by
15+ points if only one epoch had been sampled:

| SUT | mean abs. deviation | % single-epoch obs. off by ≥15 pts |
|---|---|---|
| gpt-4o-mini | 5.75 | 7.1% |
| gpt-5-mini | 5.66 | 7.9% |
| haiku | 6.33 | 11.0% |
| minimax-m3 | 9.02 | **19.6%** |
| qwen | 7.23 | 12.9% |

minimax-m3 is the noisiest SUT across epochs — nearly 1 in 5 single-epoch
observations would have missed the item's true 3-epoch level by 15+ points.
This is the concrete, measured version of the WALKWORTHY-project lesson
([[project_walkworthy_v2]]): single-epoch verdicts are unreliable, and this
project's 3-epoch design is load-bearing, not a cosmetic robustness gesture.

## 7. Standing regrades

- **5-AGG gold_order char-split regrade:** the bug (`wcf_tasks.py:96`,
  `" < ".join()` on a string sentinel silently char-splitting it into the
  judge prompt) was fixed at s14 (commit `5a449a4a9`), **before** this
  session's full-run packets were rendered — the 5,175-response run already
  scored all 5 affected AGG items correctly. No regrade action on the
  headline numbers above was needed.
- **Fitness re-check (does fit-now rise from 84?):** YES. Re-applying the s11
  dim2/dim5 threshold rules to this session's fresh 5-SUT×3-epoch data for
  the 5 previously-miscategorized AGG items: 4 of 5 now classify
  DISCRIMINATING+OK (vs. 0 of 5 under the pre-fix pilot-era data, where all 5
  were WEAK/LOW-AGREEMENT off panel spreads of 27–46.8 points — the char-split
  garbage was directly corrupting judge agreement). **Estimated fit-now:
  84 → 88.** Full method, caveats (2-judge proxy vs. the original 3–5-grader
  panel; new-era vs. s8-era spread basis): `analysis/session19_agg_fitness_regrade.py`
  → `analysis/20260731-session19-agg-fitness-regrade.json`.

## 8. Disclosures (load-bearing, not boilerplate)

1. **strict-v3 rejected-candidate episode:** a second-guard candidate
   template failed its 20-cell bench gate on both grounds (opus reproduced
   two trap scores byte-for-byte via an "announce-then-ignore" mechanism; the
   same edit broke 3 previously-passing Sol cells including a negative
   control). Owner-ratified auto-revert fired mechanically; strict-v2 is the
   only validated instrument used in this report. Full adjudication:
   `analysis/20260725-session17-v3-gate-adjudication.md`.
2. **N=345, never 317:** the s16 "317" was `345 − 28` computed without a
   set-membership check; the 28 `g4_excluded_new_items` ids are already
   absent from the frozen v2.5 bank (sha-verified, 0 overlap). G4 policy
   (keep excluded + disclose) unchanged and satisfied. This is the general
   form of a class of errors this vault tracks explicitly: never derive a
   count by arithmetic on an exclusion list without checking membership
   against the actual data.
3. **Opposed-judge residuals + this session's triage (§4):** opus is
   known-lenient on advisory-prose-without-artifact and compliance-theater
   garnish, confirmed and quantified at n=90 sample scale (90% idiom rate,
   79%/21% opus/Sol direction split) — see §4 for the full disclosure.
4. **Duplicate-judge artifact (benign):** 4 qwen cells were independently
   judged twice by opus during overlapping Workflow chunk relaunches; a
   file-safety hook preserved the pre-existing verdict as a `.bak` sidecar
   before the second write landed. No data loss, no double-counting
   (aggregation reads only the canonical filename; 0 parse anomalies). Two of
   the four pairs showed real score divergence between independent passes
   (COMP-N-021: 9→5; CONT-N-004: 68→59) — minor evidence of opus judge-pass
   noise, not a blocker.
5. **Batch-mode prohibition:** single-packet judging only, throughout —
   SUT-pure batch judging is not part of the frozen instrument and is known
   to shift opus scores (s14 finding).
6. **No cross-instrument comparison, anywhere, including this report:** the
   strict-v3 bench numbers in the v3-gate-adjudication analysis are
   instrument-diagnostic only and must never be read as SUT evidence.

## 9. What this report does NOT establish

- Whether the top-tier tie (gpt-5-mini/minimax-m3/qwen) reflects a real
  capability ceiling in the current SUT roster or a bank ceiling — out of
  scope for this pass.
- Any claim about the MEND-N-018 rubric self-contradiction beyond flagging it
  (§4) — not corrected in this report.
- Anything about episodes (22 items) — out of Scenario-A scope throughout.

## Artifacts

`analysis/session19_headline_analysis.py` → `20260731-session19-headline-analysis.json`;
`analysis/session19_judge_gap_triage_sample.py` + `_packets.py` →
`20260731-session19-judge-gap-triage-selection.json` / `-findings.json` /
`analysis/20260731-session19-judge-gap-triage.md`;
`analysis/session19_agg_fitness_regrade.py` → `20260731-session19-agg-fitness-regrade.json`.
Successor: session-20 boot prompt (paper drafting), to be written only if this
report is accepted without material revision.
