# F9 Live Micro-Check — design-05 solver-level format retry

**Date:** 2026-07-16 (session 5) · **Authorization:** owner GO
(`20260716-owner-ruling-f1-and-spend-go.md`), spend memo Item 1, ceiling $0.30.
**Runs:** design05 × deepseek-chat + mistral-small (the pilot's worst/best format
non-compliance, 79%/46%), judge-A gpt-4.1-nano, `--max-tokens 4096
--max-connections 4`, logs at `logs/f9-microcheck-20260716/` (gitignored).

## Result — the retry closes the format-compliance residual entirely at this n

| | pilot (no retry) | micro-check first-pass | retry fired | retry recovered | final non-compliant | coverage n (CSR) | CSR |
|---|---|---|---|---|---|---|---|
| deepseek-chat | 22/28 non-compliant (79%) | 10/28 ok | 18 | 17 | **0/28** | 27 (vs 6 pilot) | 0.9074 (pilot 0.9028, n=6) |
| mistral-small | 13/28 non-compliant (46%) | 11/28 ok | 17 | 15 | **0/28** | 27 (vs 15 pilot) | 0.9136 (pilot 0.9444, n=15) |

Reading (R9 framing — coverage axis stays a separate signal):

- **Post-retry format non-compliance dropped 79%/46% → 0% on both SUTs.** One
  `_FORMAT_REMINDER` re-prompt is sufficient at this tier; genuine refusal-to-allocate
  did not occur in this draw (a still-failing retry would have parsed as non-compliant
  DATA — the path is mock-verified).
- **First-pass compliance is reported separately and stays low** (10/28, 11/28 —
  consistent with the pilot's residual): `format_retry_used` accounting works as
  designed; retry compliance never masquerades as first-pass compliance. Both numbers
  must appear in any future 05 cell (per-item fields are in Score.value and store
  `ww_format_retry`).
- **CSR on the recovered coverage is stable** (0.907/0.914 vs pilot 0.903/0.944):
  widening coverage from 6→27 and 15→27 items did not move the constraint-satisfaction
  estimate materially — evidence the pilot's decidable-item CSR was not a
  compliance-selection artifact, at least for these two SUTs.
- The 2–3 unrecovered retries per SUT emitted imperfect blocks (`ok=False`,
  `non_compliant=False` — tokens/sum defects) that the bounded offline re-parse could
  still value-extract; 1 item/SUT remains undecidable on constraints (unchanged from
  pilot semantics).

## Spend

deepseek 42,952 in / 41,802 out; mistral 37,623 in / 38,802 out; judge-A ≈71k in /
740 out total. **≈ $0.07–0.09 total — under the $0.30 ceiling.**

## Consequence

F9 is validated live. The v2 design-05 instrument now matches v1's one-retry semantics
with clean two-axis accounting; the cross-harness 05 comparison (spend memo Item 3) is
unconfounded on retry behavior. Remaining 05 caveats (R9: format-gated metric,
gameable-by-numbers) unchanged.
