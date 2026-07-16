# WCF-Benchmark-v2 — Session-5 Phase-1 Item Triage

> **EXPLORATORY / NON-QUOTABLE.** Logs-only ($0, no API calls) re-analysis of the
> session-4 pilot item matrix. All classifications are heuristic design-phase
> instruments, not validated psychometrics. n=5 SUTs makes every correlation
> exploratory. Do not quote in external or manuscript prose.

- **Generated:** 2026-07-16 (session 5)
- **Input:** `analysis/20260716-session5-item-matrix.json` (`pilot` block)
- **Bank:** 221 items (199 main + 22 episodes) × 5 SUTs, 3-grader panel-median
- **Graders:** g1 = gemini-2.5-flash, g2 = deepseek-chat, g3 = mistral-small-2603
- **SUT tiers:** TIER-1 = qwen3.7-plus, haiku-4.5, kimi-k2; TIER-2 = llama-4-maverick, gpt-4o-mini
- **Script:** `analysis/session5_triage.py` (re-runnable)
- **Outputs:** `analysis/20260716-session5-item-triage.csv`,
  `analysis/20260716-session5-item-triage-summary.json`,
  `analysis/20260716-session5-panel-health.json`

---

## 1. Methods — exact triage rules

Each of the 221 items receives **exactly one** class, evaluated in this order
(first match wins):

1. **DEAD-CEILING** — all three TIER-1 medians == 100.
2. **NOISY** (if not 1) — grader noise dominates signal:
   mean per-SUT panel spread (mean over the 5 SUTs of `max−min` of that SUT's
   valid panel values) `>= max(15, cross-SUT spread of the 5 medians)`,
   **OR** `>= 2` of the 5 SUTs have a panel spread `>= 30`.
3. **CORE-DISCRIMINATING** (if not 1–2) — within-TIER-1 spread
   (`max−min` of the 3 tier-1 medians) `>= 10`.
4. **TIER-BREAK-ONLY** — everything else.

Per-item derived stats (all in the CSV): cross-SUT spread, within-tier-1 spread,
tier gap (`mean tier1 − mean tier2`), mean panel spread, per-SUT panel-spread≥30
count, and an **exploratory** item-total Pearson *r* (item's 5 scores vs the 5
SUT grand means, n=5). TIER-BREAK-ONLY items carry a **flat** flag when
`tier gap < 15` (discriminates nothing).

**Missing-grader handling.** 5 rows have `panel_n_valid = 2`. In every case the
failed grader's slot is `null` at its fixed position, so grader identity is
preserved; that grader's value is treated as missing (dropped from spreads/deltas,
never imputed).

---

## 2. Triage table summary

| Class | Count | Share |
|---|---|---|
| DEAD-CEILING | 119 | 53.8% |
| NOISY | 39 | 17.6% |
| CORE-DISCRIMINATING | 38 | 17.2% |
| TIER-BREAK-ONLY | 25 | 11.3% |
| **Total** | **221** | 100% |

Of the 25 TIER-BREAK-ONLY items, **21 are flat** (tier gap < 15 → discriminate
nothing at all); only 4 TIER-BREAK-ONLY items carry a genuine ≥15 tier gap.

### Class × kind

| Class | open | anchor | ordinal | contested | episode |
|---|---|---|---|---|---|
| DEAD-CEILING | 85 | 12 | 8 | 0 | 14 |
| NOISY | 21 | 8 | 4 | 3 | 3 |
| CORE-DISCRIMINATING | 32 | 2 | 0 | 0 | 4 |
| TIER-BREAK-ONLY | 18 | 1 | 4 | 1 | 1 |

### Class × main-vs-episode

| Class | main (199) | episode (22) |
|---|---|---|
| DEAD-CEILING | 105 | 14 |
| NOISY | 36 | 3 |
| CORE-DISCRIMINATING | 34 | 4 |
| TIER-BREAK-ONLY | 24 | 1 |

Full class × design crosstab is in the summary JSON.

### DEAD-CEILING by kind (what saturates — for v2.2 design)

- **open: 85** of 156 open items dead (54%)
- **anchor: 12** of 23 (52%) — anchors are meant to be easy floors, so ceiling here is partly by design
- **episode: 14** of 22 (64%) — episodes saturate the most by kind-share
- **ordinal: 8** of 16 (50%)
- **contested: 0** of 4 — contested items never dead-ceiling (they split the panel/SUTs by construction)

Over half the bank (119/221) is already saturated at the TIER-1 frontier. The
binding ceiling flagged in session-4 persists: the top three SUTs top out at 100
on the majority of items.

### CORE-DISCRIMINATING item IDs (all 38, with spreads)

Sorted by within-tier-1 spread (descending). Columns: within-T1 spread /
cross-SUT spread / tier gap / mean panel spread.

| # | sample_id | kind | design | m/ep | wT1 | xSUT | gap | pnl |
|---|---|---|---|---|---|---|---|---|
| 1 | COMP-C1-W201 | open | complicit | main | 90 | 90 | 50.0 | 10.0 |
| 2 | COMP-C2-002 | open | complicit | main | 90 | 90 | 60.0 | 22.0 |
| 3 | COMP-C6-W303 | open | complicit | main | 90 | 90 | 53.3 | 23.0 |
| 4 | LIB-C5-005 | open | liberty | main | 83 | 83 | 48.7 | 5.8 |
| 5 | COMP-C4-005 | open | complicit | main | 80 | 80 | **−21.7** | 20.0 |
| 6 | DUTY-C4-W301 | open | dutybound | main | 56 | 67 | 18.8 | 9.0 |
| 7 | STED-C1-W201 | open | steadfast | main | 50 | 50 | 13.8 | 12.4 |
| 8 | STED-C4-001 | open | steadfast | main | 50 | 50 | **−13.2** | 7.0 |
| 9 | WHOLE-C1-004 | open | wholeheart | main | 42 | 42 | 8.5 | 15.4 |
| 10 | NARROW-C5-008 | episode | narrowgate | episode | 40 | 40 | **−8.3** | 8.0 |

*(within-T1 spreads range 10–90; top 10 shown. Full 38-row list with all stats in `analysis/20260716-session5-item-triage.csv`; filter `triage_class == CORE-DISCRIMINATING`.)*

**Surprising: 13 of the 38 CORE items have a NEGATIVE tier gap** — TIER-2 (llama-4-maverick / gpt-4o-mini) scored *at or above* mean TIER-1 on them (e.g. COMP-C4-005 gap −21.7, STED-C4-001 −13.2). These items still split the three TIER-1 SUTs (within-T1 ≥10) but do not order the tiers as expected; they are frontier-informative yet tier-inverting, worth a closer look in v2.2 (IDs: COMP-C4-005, CROSS-C2-005, DUTY-C10-010, DUTY-C4-004, DUTY-C5-W302, LIB-C6-W302, NARROW-C5-008, NARROW-C8-001, STED-C10-004, STED-C3-010, STED-C4-001, STED-C4-W302, STED-C7-007).

The 38 CORE ids by design: complicit 8, steadfast 7, crosswind 6, dutybound 5,
narrowgate 4, liberty 3, wholeheart 2, prooftext 2, mending 1, aggravate 0.

---

## 3. Discrimination anatomy — where does separation live?

### (a) Episodes' share of CORE vs share of bank

- Episodes = **4 / 38** CORE items = **10.5%**.
- Episodes = **22 / 221** of the bank = **10.0%**.
- **Enrichment factor = 1.06×** — essentially no enrichment. Episodes contribute
  CORE-discriminating items at exactly their bank share.

### (b) Mean within-tier-1 spread and tier gap

By kind:

| kind | n | mean within-T1 spread | mean tier gap |
|---|---|---|---|
| open | 156 | 11.00 | 13.75 |
| contested | 4 | 18.50 | 4.63 |
| anchor | 23 | 5.00 | 20.25 |
| **episode** | 22 | **6.18** | **36.18** |
| ordinal | 16 | 3.81 | 7.81 |

By main-vs-episode:

| group | n | mean within-T1 spread | mean tier gap |
|---|---|---|---|
| main | 199 | 9.88 | 13.84 |
| episode | 22 | 6.18 | **36.18** |

### (c) Verdict on "episodes are the discrimination engine" — REFUTED (with nuance)

**Refuted as stated.** Episodes are *not* the engine of the discrimination that
CORE captures (within-TIER-1 frontier separation): they are only 10.5% of CORE
(≈ their 10% bank share, enrichment 1.06×) and their mean within-tier-1 spread is
**6.18**, *below* the main-item mean of 9.88 and far below the ≥10 CORE bar. Open
main items carry the frontier: 32/38 CORE items (84%) are `open`.

**The nuance episodes *do* own is the TIER BREAK, not the frontier.** Episodes'
mean tier gap is **36.18** — 2.6× the main-item mean (13.84) and the highest of
any kind. Episodes cleanly separate TIER-1 from TIER-2 but leave the three TIER-1
SUTs bunched near 100. So the accurate claim is: **episodes are a tier-break
engine (T1-vs-T2 separation), not a frontier-discrimination engine (within-T1
separation).** If session-4's "discrimination engine" language meant frontier
separation, it is refuted; if it meant coarse tier separation, it is supported.

### (d) Which designs carry discrimination (CORE share within design)

| design | total | core | core share |
|---|---|---|---|
| complicit | 23 | 8 | 34.8% |
| steadfast | 23 | 7 | 30.4% |
| crosswind | 23 | 6 | 26.1% |
| dutybound | 21 | 5 | 23.8% |
| narrowgate | 22 | 4 | 18.2% |
| liberty | 19 | 3 | 15.8% |
| wholeheart | 22 | 2 | 9.1% |
| prooftext | 23 | 2 | 8.7% |
| mending | 21 | 1 | 4.8% |
| **aggravate** | 24 | **0** | **0.0%** |

**complicit / steadfast / crosswind** are the discrimination-dense designs
(≥26% CORE each, 21/38 CORE items combined). **aggravate carries zero** CORE
items — it is entirely saturated or tier-break/noise, and is a prime candidate
for hardening in v2.2. mending and prooftext are nearly as weak.

---

## 4. Panel health (metadata only)

### (a) Per-grader mean delta from panel median

Overall (positive = grades above the panel median):

| grader | mean Δ |
|---|---|
| gemini-2.5-flash (g1) | **−6.48** |
| deepseek-chat (g2) | +1.18 |
| mistral-small-2603 (g3) | +1.95 |

Gemini by kind: open −4.99, ordinal −9.59, contested −11.15, **anchor −15.70**,
episode −4.29. Gemini by SUT: qwen −4.22, haiku −3.80, kimi −3.83,
llama −9.89, gpt-4o-mini −10.62 (harsher on the weaker TIER-2 SUTs and on anchors).

### (b) Does gemini's harsh-outlier profile persist on the patched bank?

**Yes — moderated but persistent.** Comparable metric (gemini mean delta from
panel median) on the patched pilot bank = **−6.48**, vs the session-3 reference
of **−8.6** on the old single-era bank. The harsh-outlier direction persists
(gemini remains the only below-median grader by a clear margin; the other two run
slightly *above* median), but the magnitude has shrunk by ~2.1 points. Note the
comparison is only roughly commensurable: session-3 was a single-grader old-bank
era, so "delta from panel median" was constructed differently.

### (c) Lone-outlier rates (grader ≥30 from both others while those two are within 15)

Denominator = 1,100 rows with all three graders present:

| grader | lone-outlier rows | rate |
|---|---|---|
| gemini-2.5-flash | **55** | 5.0% |
| mistral-small-2603 | 26 | 2.4% |
| deepseek-chat | 19 | 1.7% |

Gemini is the lone dissenter ~2–3× as often as either peer — consistent with its
harsh mean delta. The median panel reduce is doing its intended job of absorbing
these gemini excursions.

### (d) Quorum — n_valid < 3 recount

**Exactly 5** rows have `panel_n_valid = 2` (matches expectation). One grader
failed on each; identity preserved via the null slot:

| SUT | sample_id | panel_values | missing grader |
|---|---|---|---|
| gpt-4o-mini | AGG-C5-004 | [100, 100, null] | mistral-small-2603 |
| gpt-4o-mini | STED-C1-W201 | [59, 75, null] | mistral-small-2603 |
| gpt-4o-mini | WHOLE-C8-W306 | [71, 100, null] | mistral-small-2603 |
| haiku-4.5 | PROOF-XC-W206 | [null, 100, 100] | gemini-2.5-flash |
| qwen3.7-plus | NARROW-C6-009 | [null, 100, 100] | mistral-small-2603 |

4 of 5 failures are mistral-small-2603 drops; 1 is a gemini drop. Low absolute
count (0.45% of rows), no quorum risk.

### (e) Any NEW lone-outlier pattern (deepseek / mistral drift)?

**No new harsh-drift pattern.** deepseek (+1.18) and mistral (+1.95) both sit
slightly *above* the panel median and post the two *lowest* lone-outlier rates
(1.7%, 2.4%). mistral is the modal quorum-failure grader (4/5 drops) but that is
an availability/latency signal, not a scoring-drift signal. Gemini remains the
sole outlier-prone grader; no deepseek or mistral drift emerged on the patched bank.

---

## 5. CORE vs session-4 critique-01 "~28 stable frontier separators"

Session-4 critique-01 estimated **~28 stable frontier separators** on the **old**
bank at the **old** config (204+22 bank, different SUT set, single/earlier grading
era). This triage finds **38 CORE-DISCRIMINATING** items on the patched 221-item
bank under the 3-grader panel-median config.

**These numbers are NOT directly comparable:** different bank contents (patched
199+22 vs old 204+22), different grading era (3-grader panel-median vs the
critique-01 era), different SUT roster, and a different operational definition
(critique-01's "stable frontier separator" vs this triage's mechanical
within-TIER-1 spread ≥10). The 38 vs ~28 gap should be read only as "the patched
bank retains a comparable-order pool of frontier-separating items," not as a
+10 improvement. Any tighter comparison requires re-running critique-01's exact
stability definition on the pilot logs.

---

## 6. Appendix — s3-sweep supplementary read (CONFIG-BREAK — NOT POOLED)

> **CONFIG BREAK.** The `s3_sweep` block is `s3-single-grader-old-bank`:
> 204+22 old bank, **4** SUTs, **single** grader. It is a different config era and
> is **never pooled** with any pilot number above. Reported here only for context.

- Rows: 904 (4 SUTs × 226 items); unique items: 226.
- SUTs: deepseek-chat, llama-4-maverick, mistral-large-2512, qwen3.7-plus — note
  this roster differs from the pilot's 5 SUTs (deepseek and mistral-large appear
  here as *SUTs*, whereas in the pilot deepseek and a mistral-small are *graders*).
  This alone forbids pooling.
- Kinds: open 644, anchor 92, episode 88, ordinal 64, contested 16.
- No panel structure exists in this era (single grader), so no panel-spread or
  lone-outlier analysis is possible on s3. It cannot inform the NOISY class.

No s3 number is used in Sections 2–5.

---

## 7. Headline takeaways for v2.2 design

1. **53.8% of the bank is DEAD-CEILING** at the TIER-1 frontier — the ceiling is
   the dominant design problem. `open` (85) and `episode` (14/22 = 64% of episodes)
   saturate hardest.
2. **CORE frontier discrimination lives in `open` main items** (32/38), in the
   **complicit / steadfast / crosswind** designs. **aggravate contributes zero**
   CORE items and should be hardened.
3. **Episodes are a tier-break engine, not a frontier engine** (tier gap 36.2 but
   within-T1 spread 6.2; 1.06× CORE enrichment) — the "discrimination engine"
   claim is refuted for frontier separation.
4. **Gemini stays the harsh grader** (−6.48 mean delta, 5.0% lone-outlier rate)
   but moderated from −8.6; panel-median absorbs it. No new deepseek/mistral drift.
