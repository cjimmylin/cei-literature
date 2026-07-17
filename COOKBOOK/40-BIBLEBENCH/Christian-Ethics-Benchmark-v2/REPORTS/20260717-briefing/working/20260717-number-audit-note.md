# Phase-4 number/consistency audit note — 20260717 briefing suite

WALKWORTHY-CANARY-7f3e2026 · main-session (Fable) adversarial audit, 2026-07-17.

Scope: all seven markdown reports, six figures, combined PDF. Drafters (opus) verified
their own numbers against named sources at draft time; this note records the
main-session cross-checks and every fix applied after drafting.

## Fixes applied post-draft

1. **02-evaluation.md §1 run table** — added three missing live runs the drafter had
   omitted or mislabeled: row 11 F3 cross-family classifier arm (≈$0.21–0.30,
   `20260716-f3-crossfamily-classifier-results.md`; the drafter's row 9 had said the arm
   was "GATED (not run)" — true of the first F3 memo, falsified by the later results
   memo); row 12 cross-harness Option A (within $0.75, `20260716-crossharness-results.md`);
   row 13 F2 arm 2c (≈$0.65–1.23, `20260716-f2-2c-results.md`). Cumulative-spend
   sentence updated from "≈$3.8" (pilot-report-era) to the memo-component range
   **≈$5.5–7.8** (OpenRouter dashboard = source of record).
2. **04-development-history.md F-ledger** — F10 row corrected: F10 is the SD-7(c)
   optional k=3 seed decode-stability probe on design 10 (offered as pilot add-on,
   skipped, OPEN), per `REVIEWS/20260716-adjudication-benchmark-critique.md` F-ledger
   row; the drafter had substituted the R10 availability-probe discipline with an
   [UNVERIFIED] marker after failing to find an `f10`-named artifact (none exists
   because the item never fired).
3. **06-messaging.md appendix** — three drafting-time [UNVERIFIED] markers resolved:
   llama ±0.13 answer-blind delta VERIFIED (`20260716-f2-ablations-report.md` arm 2b);
   design-04 abs() bug label VERIFIED (`20260716-adjudication-fixes-report.md` M1,
   `mean(abs(alpha − beta))`); total-spend "≈$7.5" restated as the verified component
   range ≈$5.5–7.8.
4. **05-next-steps.md §1(b)** — added the reference-concordance guardrail sentence at
   the referee-evidence paragraph (was the only report using referee findings without
   the caveat adjacent).
5. **working/cover.md** — canary appended (build-only file; the PDF body carries the
   canary throughout via each report).

## Checks passed (no fix needed)

- Canary present in every .md in the suite (grep -L clean).
- No holdout content anywhere; holdout referenced by existence/guard only
  (01-benchmark-card §3, §6.8).
- No unlabeled SUT-ordering claims: "winner/best" hits are all negations, nominal-best
  annotations inside the C9-labeled leaderboard, or the flip inventory.
- 01-benchmark-card: 19 "REAL — pilot log" provenance labels + 1 "AUTHORED, NOT A MODEL
  RESPONSE" exemplar (design-07 good); counts 355/344/575/563 + 158 holdout match
  `20260715-conversion-parity-report.md`.
- 03-meta-judging: drafter verified all referee numbers against both agreement JSONs,
  zero [UNVERIFIED]; arm-specific counts kept separated (Opus 74-neither vs Sol
  101-neither on 07 are different referees, correctly not pooled).
- Figures: fig1 cells match JSON values (0.812 vs memo 0.813 = round-half-even of
  0.8125, noted, harmless); fig6 carries the R4 no-ordering title and the
  HAND-TRANSCRIBED flags for design-05 CSR and A/B agreement ranges.
- 02-evaluation §5 leaderboard: matched A/B pairs from `judge-swap-numbers.json` only;
  canonical §4 cells from pilot-report §3 only; the two provenance streams never mixed
  in one comparison (stated three times in the report).
- Cross-report spend consistency: 02 (≈$5.5–7.8) · 04 ("well under $10") · 06
  (component range) — consistent.
- PDF: 54 pages, 2.02 MB, 6/6 figures embedded, tables render as tables, zero pandoc
  warnings on final build.

Canary: WALKWORTHY-CANARY-7f3e2026 · no holdout content.
