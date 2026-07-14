# WALKWORTHY — Opus MVP-A1 Paper-Claims Adversarial Review

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Reviewer model:** Opus (single authorized adversarial paper-claims reviewer)
**Route:** Opus memo → Jimmy. This memo does not self-ratify; all dispositions are Jimmy's.
**Scope:** MVP-A1 paper-preview additions and the sections they update, checked against
`runs/20260713-mvp-a1/` (`summary.json`, `pre_meta_checkpoint.json`, `attempts.jsonl`,
`verdicts.jsonl`, `verdicts-replays.jsonl`, and `scored_items.jsonl`) plus the read-only
label protocol, manifests, and roster. No benchmark/provider credential or live benchmark
inference call was used, and HOLDOUT was never loaded.

> **Codex controller-verification note.** The Opus draft was independently checked before
> persistence. Two non-substantive draft errors were corrected: the primary table has four
> `N/A` cells, not five; and the scope sentence now distinguishes the authorized Opus review
> call from prohibited benchmark/provider inference. The substantive findings and
> recommendations are unchanged.

## Executive disposition

**ACCEPT WITH ONE P1 CORRECTION.** Every quantitative claim in the MVP-A1 preview is exact
and independently reproduced from the immutable run: all 30 primary cells, all n/exclusion
counts, all ten exact-pair agreement percentages, the 180 / 360 / 480-per-judge counts, the
1,715 paired attempts, the cost-basis ledger split (1,668 / 44 / 3), the three PR-21 pairs,
the PR-20 replay, and the $0.551363883 exposure. The descriptive-only boundary,
non-comparability discipline, “not accuracy/κ/validity” framing, and unavailable-shape
naming all hold. No ranking, gate, release, judge-validity, forbidden ethical/Christian,
hidden-release, or item/HOLDOUT-leak claim appears in the reviewed paper files.

The single substantive defect is not a number. It is a **mechanism misattribution** in the
forward-looking language (`PAPER/07-discussion-stub.md` §7.4 and scaling-memo rows 1–2): it
implies the already-frozen O5 human-label surface can change or validate the MVP §6A
cheap-judge rows. It cannot. Those labels sit on O4/O5-panel responses under the frozen O5
judge pair (`gpt-4.1-mini` + `gemini-2.5-flash`), whereas the MVP rows are cheap-SUT
responses scored by different judges (`gpt-4.1-nano` + `llama-3.3-70b`). Fix the prose
below and the preview is acceptable as descriptive.

## Verified-number checklist

| Claim | Source of truth | Result |
|---|---|---|
| 30 primary-metric cells | `summary.json → primary_metrics[*].per_model[*].S.adjudicated` | All match §6A and descriptive §2 exactly, including four `N/A` cells: 03-Mistral and all three design-07 cells |
| Per-cell n / exclusions | same `S.n` / `S.excluded` | All 30 match, including design-06 criterion-component counts 7/11, 7/3, and 7/0 |
| Design-01 fallback | `summary.json` fallback text | Correctly triggered by bank structure, not results |
| Design-05 judge-free primary | `summary.json` design note and identical primary values | Correct |
| Ten exact-pair agreement percentages | recomputed from `scored_items.jsonl` | 01 31/36=86.11%; 02 31/138=22.46%; 03 72/108=66.67%; 04 93/108=86.11%; 05 14/18=77.78%; 06 112/126=88.89%; 07 19/108=17.59%; 08 27/36=75.00%; 09 31/72=43.06%; 10 115/144=79.86% |
| 180 item×SUT executions | `executions.jsonl`, `scored_items.jsonl`, `summary.n_records` | Correct; all 30 design×SUT rows complete |
| 360 verdict records | `verdicts.jsonl` | Correct, 180 × 2 judges |
| 480 logical units per judge | `summary.judge_units` | Correct |
| 1,715 paired attempts | `attempts.jsonl` | 1,715 starts + 1,715 finishes; zero unresolved |
| Cost-basis split | `attempts.jsonl` | 1,668 reported + 44 unknown-failure maxima + 3 missing-cost maxima |
| Three PR-21 pairs | attempts 915→916, 1,081→1,082, 1,133→1,134 | Identical payload hashes; missing-cost then reported; no second missing-cost response; discarded attempts claim no returned model or tokens |
| One PR-20 replay | `verdicts-replays.jsonl` + retained original defect | Correct |
| Conservative exposure | `summary.spend.actual_usd` | $0.551363883; below the $5 NTE and planning envelope |
| Pre-Meta checkpoint | `pre_meta_checkpoint.json` | $0.484707663, 1,234 paired attempts, all prerequisites true, `continue_meta=true` |
| Five probes | `probes.jsonl` and `probe_summary` | Complete |
| Figure 6A.1 | SVG bar widths and labels | Operational values are arithmetically faithful |

**No quantitative discrepancy was found.** The paper surfaces the three missing-cost
finishes but not the 44 `reserved_max_on_unknown_failure` finishes. Both are conservative
booking artifacts of a complete run and are disclosed in the dated descriptive analysis.

## Findings

### P0 — none

No false headline number, forbidden ethical/Christian claim, ranking, gate, release,
kill/demotion claim, hidden release language, or item/HOLDOUT leakage appears in the
reviewed paper files.

### P1 — O5 labels are misattributed to the MVP cheap-judge rows

**Locations**

- `PAPER/07-discussion-stub.md` §7.4: “the already-frozen human-label surface that can
  validate or reject the judge-dependent rows.”
- `00-PORTFOLIO/20260713b-mvp-a1-postrun-scaling-memo.md`, rows 1–2: the MVP primary table
  is routed to existing O5 human-label waves / “existing unresolved public cells.”

**Evidence.** `20260710-human-label-protocol.md` §1 specifies that humans label model
responses from the O4 panel run, not items in the abstract. The frozen Part-A sample is
drawn from the six-SUT O4/O5 panel and feeds G4 for the frozen O5 judge pair
(`openai/gpt-4.1-mini` + `google/gemini-2.5-flash`). MVP-A1 used different SUT responses
(`mistral-small-3.2-24b`, `gemini-2.5-flash-lite`, `qwen3-8b`) and different judges
(`gpt-4.1-nano`, `llama-3.3-70b`). The frozen O5 labels therefore adjudicate neither the
same response surface nor the same judge pair as §6A.

**Impact.** The §6A cheap-judge cells are fixed descriptive facts. O5 label waves produce
release-grade §6 evidence on another response surface; they may supersede the need to lean
on the exploratory preview, but they do not change the MVP primary table or validate the
MVP cheap judges. Changing a §6A cell instead requires new human adjudication of the exact
MVP cheap-SUT responses or re-judging them with a validated judge.

**Charitable reading routed to Jimmy.** If “judge-dependent rows” means the benchmark's
judge-dependent designs generally, the recommended action—complete wave-1 O5 labels, run
G4, and do not buy another cheap judge—is sound. The defect is scope and attribution, not
the O5 action. Jimmy may accept the P1 or downgrade it to P2 based on the intended
antecedent. Opus recommends applying the correction because it is small and removes the
MVP/O5 conflation risk.

### P2 — none rising to a blocker

### P3 — optional clarity nits

1. Table 6A.2's design-05 agreement covers the judged secondary
   `rationale_honesty` cell, while design 05's primary CSR is judge-free. A short footnote
   would prevent readers from connecting the agreement percentage to the primary.
2. Table 6A.1's design-06 n/exclusion parentheses count criterion components rather than
   items. The descriptive analysis discloses this, but a table footnote would help.
3. The immutable handoff says “2 cheap judges × 480 logical units = 360/360 verdict
   records.” The values are individually correct, but the punctuation reads like
   `2 × 480 = 360`. This is a non-paper historical artifact and must not be overwritten.

## Exact proposed P1 corrections

### `PAPER/07-discussion-stub.md` §7.4

Replace the final two sentences with:

> The useful next evidence is therefore not a wider paid model panel. Two distinct paths
> exist and must not be conflated: (i) to make any *release-grade* statement about these
> designs, complete the already-frozen O5 human-label waves (wave 1 `{02,07,01}`) and run
> G4 on the frozen O5 judge pair—these labels validate the O5 judges on O4/O5-panel
> responses and populate the separate §6 results, not the exploratory §6A cells; (ii) to
> strengthen the §6A rows themselves would instead require new human adjudication of these
> exact cheap-SUT responses, or re-judging them with a validated judge. The frozen O5
> labels do not validate the MVP-A1 cheap judges (`gpt-4.1-nano`, `llama-3.3-70b`), which
> scored different responses. This is a paper-design observation, not a model-performance
> conclusion.

### Immutable scaling memo

Do not overwrite `20260713b-mvp-a1-postrun-scaling-memo.md`. If Jimmy accepts the P1,
create a NEW dated superseding correction memo with these dispositions:

- Row 1: “These §6A cells are fixed cheap-judge facts and are not changed by the frozen
  O5 waves. To obtain release-grade §6 numbers for these designs, complete O5 wave 1
  `{02,07,01}` and run G4 on the frozen O5 pair. To alter the §6A rows, human-adjudicate
  these exact MVP cheap-SUT responses (no SUT rerun needed). Do not buy another
  unvalidated judge.”
- Row 2: “Human adjudication of the six excluded MVP cheap-SUT contributions for this
  design (new labels on these responses); no SUT rerun needed. This is distinct from the
  frozen O5 Part-A/B waves, which adjudicate O5-panel responses.”
- Rows 5–6 remain correct where they explicitly name O5 judge-validity/performance
  surfaces served by frozen labels and G4.

## Claim-license assessment

- **Inside C6 / amendment §4:** Every result surface carries the disclaimer; values are
  descriptive, unranked, and construct-incommensurate across rows. Agreement is
  consistently distinguished from accuracy, κ, human agreement, and validity.
- **Non-comparability and no ranking:** The preview states fixed manifest order, not
  ranked, and no cross-design comparison.
- **Unavailable shapes named:** Four `N/A` cells retain exclusion counts. The heatmap,
  leaderboard, gate matrix, and validated-judge concordance figure are explicitly
  unavailable.
- **PR-20/PR-21 custody:** Missing-cost responses are discarded and booked at the
  registered maximum without response/model/token inference; the PR-20 defect remains
  separate from its replay.
- **No O5 merge or hidden release:** §6A remains separate from O5 and contains no release
  action or forbidden model-Christianity claim.
- **Watch item:** The P1 forward-looking language brushes against amendment §4's ban on
  treating cheap judges as substitutes for the O5 judge-validation process. The proposed
  correction removes the implication.

## Jimmy decision block

1. **Accept the preview numbers as verified?** Opus recommends **yes**.
2. **P1 scope/attribution correction:** accept as P1 and apply the exact paper correction
   plus a NEW superseding scaling correction memo, or rule the intended antecedent was the
   separate O5 §6 designs and downgrade to P2. Opus recommends accepting the correction.
3. **P3 nits:** accept or waive; none blocks the preview.
4. **Scaling:** spending no more on MVP inference and completing wave-1 labels remains a
   sound recommendation for the O5 release lane. It does not validate or change §6A, and
   this memo authorizes no scale-up.

*Verified facts are drawn from the immutable run and read-only governance files. The P1
disposition and all corrections are recommendations for Jimmy, not self-ratified changes.*
