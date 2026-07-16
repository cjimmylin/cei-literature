# Consolidated Spend Memo — F9 micro-check · F2 judge ablations · v1↔v2 cross-harness (Option A)

**Date:** 2026-07-16 (session 5) · **Status:** ⛔ **STOP — awaiting explicit owner
(Jimmy) authorization. No paid call fires before a written GO, per run.**

**Authorization state:** the 2026-07-16 pilot authorization ($7.90 envelope) is **SPENT
AND EXPIRED** (≈$3.63 used). It does not roll over. This memo is a fresh PF-003-style
ask; every line item needs its own explicit GO (a single "GO all" also suffices if the
owner says so). All prices assume the OpenRouter developer API
(`source ~/.codex/secrets/openrouter.env`); availability probe (max_tokens=16) runs
before any paid design run (R10) at negligible cost.

All free/offline work is already DONE this session (F9 code + mock verify; F2 tools
built + dry-run verified; F1 tags + divergence-split addendum; cross-harness design
memo). The items below are the only paid steps.

---

## Item 1 — F9 live micro-check (design-05 format retry)

Purpose: confirm the solver-level `_FORMAT_REMINDER` retry lifts real-SUT format
compliance and that `format_retry_used` accounting separates first-pass vs retry
compliance on live traffic (pilot residual: 46–79% non-compliance per SUT).

- Scope: design05 × 2 SUTs — **deepseek-chat** (worst, 79% non-compliant) +
  **mistral-small** (best, 46%) — spans the residual range. 32 admins/SUT + ≤20
  retries/SUT + 32 judge-A secondary calls/SUT. `--limit`/item-ids acceptable (05 is
  unpaired), but full 32 is already tiny.
- Estimate: ≈ $0.10 total. **Per-run ceiling: $0.30.**
- Deliverable: dated micro-check report — first-pass vs post-retry compliance per SUT
  via `tools/audit/recompute_design05_csr.py` (already emits the split fields).

## Item 2 — F2 judge ablations (offline re-judge of stored pilot logs; judge tokens only, zero SUT calls)

Tooling is built and dry-run-verified (`tools/audit/judge_ablation.py`,
`tools/audit/ablation_agreement.py`; baseline reproduces pilot agreement numbers).
Volumes below are exact dry-run counts over `logs/pilot-20260716` (all 5 SUTs); costs
use gpt-4.1-nano $0.10/$0.40 per M (judge-A) and llama-3.3-70b ≈$0.10–0.30/$0.25–0.40
(judge-B, endpoint-dependent — probe will pin it).

| Arm | Calls/judge | In-tokens/judge | Est. (A+B) | Ceiling |
|---|---|---|---|---|
| **2a. d07-anchors-off** (attribution of the 0.48-vs-0.22 agreement story) | 815 | 1.35M | $0.31–0.61 | **$0.80** |
| **2b. answer-blind** (JV-2 leniency delta; designs 03/06/09, all stored samples) | 925 | 0.85M | $0.21–0.41 | **$0.60** |
| **2c. d02-anchors-on** (OPTIONAL reverse arm; generic 02 anchor block, tool-local) | 1,610 | 2.87M | $0.63–1.23 | **$1.50** |

Recommendation: 2a + 2b now (they answer F2's core questions); 2c only if the owner
wants the reverse-arm attribution in the same pass. Analysis after firing is free
(`ablation_agreement.py`), reported in a new dated file.

## Item 3 — v1↔v2 cross-harness comparison, Option A (design: `20260716-crossharness-design.md`)

v1 side is the **stored** 2026-07-13 MVP-A1 run (no v1 execution, no v1 writes). Paid
side: v2 runs the 60-item MVP-A1 slice × 2 overlapping SUTs (mistral-small,
gemini-flash-lite) + judge-B rescore.

- Estimate: ≈ $0.29. **Ceiling: $0.75.**
- Sequencing: after Item 1 (aligns 05 retry semantics) and ideally after 2a (decomposes
  the design-07 anchor confound c1).

---

## Totals

| Package | Estimate | Sum of ceilings |
|---|---|---|
| Recommended core (1 + 2a + 2b + 3) | ≈ $0.9–1.4 | **$2.45** |
| Everything incl. optional 2c | ≈ $1.5–2.6 | **$3.95** |

Each item individually sits under the PF-003 $5 routine ceiling, but per standing
practice all paid steps in this session collect here and **none fires without the
owner's explicit GO**. Hard stop applies mid-run too: a per-item running `model_usage`
tally aborts any run that reaches its ceiling.

**Execution order on GO:** availability probe → Item 1 → 2a → 2b → (2c) → Item 3, one
dated report per item, no report overwrites.

⛔ **END OF SESSION WORK — awaiting owner ruling.**
