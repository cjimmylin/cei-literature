# RULINGS APPLIED — 2026-07-31h: probe spend ceiling RAISED to $60.00 on calibrated projection

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-07-31 · **Spend ceiling authorized: $60.00 (supersedes the $25.00 of `-g`).**
**Predecessor:** `RULINGS-APPLIED-20260731g.md` — all of its provisions remain in force
except the ceiling amount and the output-cap figure amended here.

---

## RULING — ceiling amendment, recorded from an interactive owner decision, 2026-07-31

The `-g` ruling required a pre-launch cost estimate and a stop if it crossed the
ceiling. That fired before launch: a 4-SUT calibration micro-run (3 design-01 items,
1 epoch, ~$0.30, logs under `logs/widegap-probe-20260731/calib/`) measured actual
completion volumes of ~3,400 tokens/call for gpt-5 (~2,600 reasoning) and ~2,700 for
gemini-2.5-pro (~1,900 reasoning), versus the ~1,800 assumed. At $10/M completion
pricing the honest full-probe projection is ~$50–60, not the ~$32 first estimated.

Presented options: raise the ceiling and run as authorized; trim to single-turn
designs with a cheaper gpt-5-mini swap (~$17); or swap both $10/M models for cheaper
siblings (~$10–12). **The owner raises the ceiling to $60.00 and runs the probe
exactly as authorized in `-g`** — full 100-item manifest, true-frontier panel,
natural reasoning verbosity (no reasoning-effort throttling, which would contaminate
the moral-reasoning construct being probed).

Amendments to `-g`, both instrumental:

1. **Ceiling: $60.00 hard**, same stop-and-report-partial rule, same priority order
   (d01/d03/d04/d05 before d02/d07), running tally checked between design blocks.
2. **Output caps: max-tokens 8192** for the three reasoning SUTs (gpt-5,
   gemini-2.5-pro, deepseek-r1) so reasoning does not truncate answers (gpt-5's
   calibration mean brushed the earlier 4096 cap); 4096 for claude-sonnet-4.5 and
   the gpt-4.1-mini anchor, whose measured means sit far below it.

Everything else — manifest, panel, judges, epochs, P1–P4, diagnostics-only status,
recording and verification gates — is unchanged from `-g`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
