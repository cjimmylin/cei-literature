# WCF-Benchmark-v2 — Session-6 roster leaderboard (re-fire after key raise)

**Date:** 2026-07-16 · **Status:** EXPLORATORY / NON-QUOTABLE
**Bank:** v2.3 (228 main + 22 episodes; manifest `data/BANK-VERSION.json`) ·
**Panel:** gemini-2.5-flash + deepseek-chat + mistral-small-2603, median ·
**Parser:** last-match GRADE, word-bounded, 4-digit reject ·
**Config:** excellence gate ON (main); episodes at `pressure_variant=item` ·
Scores are 0–100 rubric-conformity panel-medians, NOT accuracies. **v2.3 is a
new scale — never compare these numbers to v2.2/s4/s3/s2 tables.**
Supersedes the BLOCKED-EXTERNAL §6 of `20260716-session6-report.md` (owner
raised the OpenRouter key cap; owner selected the **separate tier-break panel**
option for the 9 G4-excluded escalation episodes).

## Leaderboard — full-bank mean + frontier-core index

| SUT | full bank (250) | main (228) | episodes (22) | **frontier-core (29)** | escalation panel (9)* |
|---|---|---|---|---|---|
| qwen3.7-plus | 94.4 | 94.0 | 98.3 | **74.3 ± 2.7** | 91.9 |
| claude-haiku-4.5 | 93.6 | 93.1 | 98.4 | **73.7 ± 2.7** | 100.0 |
| gpt-5-mini | 90.4 | 89.8 | 96.1 | **74.9 ± 3.4** | 100.0 |
| deepseek-v3.2 † | 87.6 | 87.9 | 83.9 | **58.0 ± 3.5** | 96.0 |
| gpt-4o-mini | 76.9 | 78.4 | 61.6 | **53.2 ± 4.0** | 78.6 |

\* Escalation panel = the 9 G4-excluded 4-turn episodes, run standalone
(`wcf_new_episodes`), NEVER mixed into the full-bank mean (owner decision:
pressure-holding is a distinct construct).
† deepseek-v3.2 is panel-self-kin (deepseek-chat grades it): the s5 DiD rule
applies **±1.7-pt sensitivity to any within-tier claim** on this row. Its
placement below the frontier trio (gaps ≈ 16 pts) is kin-robust.

## Pairwise (frontier-core scope, MDD80 = 2.80 × SE of paired diffs, n=29)

| pair | gap | MDD80 | verdict |
|---|---|---|---|
| qwen − haiku | +0.60 | 11.26 | ns |
| qwen − gpt-5-mini | −0.53 | 13.36 | ns |
| haiku − gpt-5-mini | −1.14 | 15.45 | ns |
| qwen − deepseek-v3.2 | +16.36 | 12.49 | **SIG** (kin-robust: ≫ ±1.7) |
| haiku − deepseek-v3.2 | +15.76 | 12.12 | **SIG** (kin-robust) |
| gpt-5-mini − deepseek-v3.2 | +16.90 | 17.82 | ns (gpt-5-mini variance) |
| qwen − gpt-4o-mini | +21.12 | 12.11 | **SIG** |
| haiku − gpt-4o-mini | +20.52 | 11.93 | **SIG** |
| gpt-5-mini − gpt-4o-mini | +21.66 | 18.39 | **SIG** |
| deepseek-v3.2 − gpt-4o-mini | +4.76 | 7.27 | ns |

## Readings

1. **Three-way frontier parity at ~74 on the frontier-core index.** qwen,
   haiku, and gpt-5-mini are statistically indistinguishable (all pairwise ns,
   gaps ≤ 1.1 vs MDD80 ≈ 11–15). The index did its job in both directions: it
   pulled tier-1 off the 100-ceiling into a regime where differences COULD
   show (means ~74, SDs ~15–19), and what it shows is parity — consistent
   with s5's capability-parity verdict, now measured on items with headroom
   rather than inferred from a ceiling.
2. **The index separates tiers sharply**: frontier trio ≈ 74 ≫ deepseek-v3.2
   58.0 ≈ gpt-4o-mini 53.2. On the full-bank mean the same story compresses
   into 94/94/90/88/77 — the frontier-core index is the more informative
   instrument, exactly as the s5 power analysis predicted.
3. **gpt-5-mini's profile**: frontier-core parity with qwen/haiku, but 3–4 pts
   below them on the full bank (89.8 main) — it drops points on the old
   saturated mass where the others don't, and holds the escalation panel at
   100. Its per-item variance is the largest of the trio (SE 3.4), inflating
   its MDDs.
4. **Escalation panel**: haiku and gpt-5-mini held all 9 ramps at 100;
   deepseek-v3.2 96.0; gpt-4o-mini 78.6 (folds under pressure, consistent
   with every prior session). qwen slipped to 91.9 in THIS draw after scoring
   100/9 in the gate draw — qwen is the only frontier model to slip on an
   escalation ramp in either draw; single-draw item numbers are non-quotable,
   so this is flagged as instability to resolve with epochs in s7, not as a
   finding.
5. **Old-episodes at max pressure (22 items)**: tier-1 ≈ 98, deepseek 83.9,
   gpt-4o-mini 61.6 — the tier-break engine keeps working.

## Audit

- **Completeness: unscored 0/1,295** (1,250 bank + 45 panel samples); all 15
  runs status=success; no qwen partial logs this time.
- **Quorum: 52 samples graded by 2/3 graders** (~4%, elevated vs the ~0.5%
  historical rate). All 52 are single-grader failures of **g1
  (gemini-2.5-flash)** — a provider transient during the run window, spread
  evenly across SUT runs (9–12 each); the panel-median's n_valid=2 fallback
  absorbed them. No sample fell below quorum 2.
- **Spend (token-attributed): roster2 $8.60** (over the $7.6 forecast on
  qwen/gpt-5-mini reasoning tokens); **session total ≈ $9.86 ≤ $10.00**.
  Credits delta for the re-fire window was $19.77 — the shared-key
  concurrent-session inflation again (~2.3× attributed).
- Stats artifact: `analysis/20260716-session6-roster-stats.json` (leaderboard,
  pairwise, per-run statuses, quorum ledger). Logs:
  `logs/20260716-session6-roster2-{main,episodes,panel}/`.

## Session-7 carry-forward (updated)

1. Within-tier-1 resolution: epochs ≥2 on the frontier-core 29 (parity vs
   MDD80 ~11 is honest but coarse; epochs shrink MDD ~√k) + qwen escalation
   instability (reading 4 above).
2. Google SUT + mandatory gemini-free-panel kin DiD piggyback (unchanged).
3. gemini grader transient: if the ~4% g1 failure rate recurs in s7, consider
   nova-pro-v1 as the validated kin-free substitute (s5 ruling) or a retry
   wrapper at the bounded_grader layer.
4. Contested authoring wave 2 (the proven frontier mold) if more frontier-core
   mass is wanted — n=29 → n≈45 cuts MDD80 by ~20%.
