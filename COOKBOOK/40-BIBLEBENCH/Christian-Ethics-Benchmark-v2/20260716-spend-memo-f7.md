# CONSOLIDATED SPEND MEMO — session 7 (F7 live arm) — AWAITING OWNER GO

**Date:** 2026-07-16, session 7. **The session-6 GO is CLOSED** (~$0.30 spent of its
$1.15 ceiling; no rollover). This memo is the single gate for ALL paid calls this
session (PF-003 pattern; $5 unauthorized-run ceiling never approached without a GO).

## Item 1 — F7 live arm (design-07 prior-turn-context judging, JV-8)

- **What:** re-judge the stored design-07 pilot turns with prior-turn context
  injected (tool: `tools/audit/judge_context_ablation.py`, built and dry-run-verified
  this session — see `20260716-f7-offline-assembly-report.md`), both certified
  judges, vs the shipped context-free verdicts as baseline. No SUT calls.
- **Count correction:** the boot prompt's "109 turns × 5 SUTs × 2 judges = 1,090
  calls" is a transcription error. Stored data has **163 turns/SUT** (27 samples/SUT;
  uniform across all 5 SUTs; 815/judge exactly matches the established
  d07-anchors-off dry-run count in the F2 spend memo). Actual: **815 calls/judge ×
  2 judges = 1,630 calls**.
- **Measured input volume (real assembly, chars/4):** 7.39M chars/judge →
  **≈1.85M input tokens/judge** (mean 9,065 chars/prompt, p90 13,312, max 26,749;
  +37% vs F2's context-free design-07 arm — the prior-turn context is why).
- **Cost** (prices cited from `20260716-spend-memo-f9-f2-crossharness.md`; output
  cap = `JUDGE_MAX_TOKENS` 4096, realistic judge output ~60 tokens/call):

  | Judge | Input | Point (~60 out) | Hard ceiling (4096 out) |
  |---|---|---|---|
  | A gpt-4.1-nano | $0.185 | **$0.204** | $1.520 |
  | B llama-3.3-70b | $0.185–0.554 | **$0.197–0.574** | $1.889 |
  | **Total** | — | **≈$0.40–0.78** | **≈$3.41** |

- **Requested authorization: ceiling $4.00** (covers the theoretical worst case;
  expected spend under $1).
- **Preconditions on GO (already wired):** availability probe max_tokens=16 first
  (R10); explicit max-tokens on every call (402 trap); incremental JSONL verdict
  writes; double gate `--live` + `WW_F7_LIVE=1`; metrics via
  `context_ablation_agreement.py` (join logic self-checked 815/815=1.000 baseline;
  control A-vs-B 0.531 = the real 07 judge gap this experiment probes).
- **What the evidence buys:** R11's PROVISIONAL order-blindness flag on design-07
  per-turn judging gets its direct test; F3 already established 07's stimuli are
  cross-family stable, so any effect found is attributable to JUDGING, not stimulus
  instability.

## Item 2 — F2-2c (opt-in BY NAME ONLY; not recommended by default)

Still un-fired from session 5/6: ~$1.50. Fires ONLY if the owner names it
explicitly. Not bundled into Item 1's ceiling.

## Gate

**STOP — no paid call of any kind until the owner rules on this memo.** A GO on
Item 1 authorizes up to $4.00 for the F7 live arm only. Anything else is a separate
authorization.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
