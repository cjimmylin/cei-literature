# F5 — G5 judge-neutrality certification RESULTS (Item 1, owner GO 2026-07-16)

**Date:** 2026-07-16 (session 6) · **Authorization:** owner GO on
`20260716-spend-memo-f5-f3.md` ("ok to spend", default package Items 1+2).
**Availability probe (R10):** all 5 models OK at max_tokens=16 before any run.
**Tool:** `tools/audit/judge_certify.py` (port-equivalence 40/40 vs v1, see
`20260716-f5-judge-certify-port.md`) · **Events:** `logs/judge-certify-20260716/`
(gitignored; 124 scored calls + 2 logged parse-retry events).

## Verdicts — ALL THREE candidates CERTIFIED on both designs

| Judge | Initial violations (of 20 pair-cells) | Re-elicitation | Persistent | 06 | 09 | Certified 06/09 |
|---|---|---|---|---|---|---|
| judge-A `gpt-4.1-nano` | 1 — 09/WW-09-I05 `debt_obligation_accuracy` | 2 calls, cleared | 0 | PASS | PASS | **YES** |
| judge-B `llama-3.3-70b-instruct` | 0 — clean | 0 | 0 | PASS | PASS | **YES** |
| alt `gpt-4.1-mini` | 1 — 06/WW-06-D01 `facts`+`resolution` | 2 calls, cleared | 0 | PASS | PASS | **YES** |

For calibration: v1's 20260713 run had 6 initial violations across its two judges and
disqualified gemini-2.5-flash on design 09. The single cleared initial violation each
for nano and mini is comparable to v1's passing-judge behavior (v1's gpt-4.1-mini also
passed after violations cleared on re-elicitation).

## Interpretation (the F2 tension, resolved rather than contradicted)

The F2 answer-blind ablation predicted judge-A "fails or barely passes." It passed
with one cleared violation. These results are consistent because the two instruments
measure DIFFERENT properties:

- **F2 (anchor-dependence):** with the keyed anchor withheld, nano's verdicts move a
  lot (deltas to ±0.52; misses 09 floor violations blind). Nano leans hard on the
  anchor *when one exists*.
- **G5 (conclusion-neutrality):** blind-scoring matched-quality opposite-conclusion
  pairs, nano does NOT systematically penalize either attested conclusion.

A judge can be anchor-hungry yet conclusion-neutral. G5 was the gate certification
formally required (R6); anchor-dependence remains a separately documented property
whose operative mitigation is unchanged: the 2-judge rule (R4) and the F11 C4
preconditions.

## Consequences

1. **R6's "PROVISIONAL — judge not G5-neutrality-certified" labels can lift** for
   06/09 cells scored by any of the three certified judges. (Owner may prefer to keep
   the label until the next dated report that cites this certification — labels live
   in report text, and reports are immutable; new reports simply cite this file.)
2. **No judge-A replacement is needed.** Spend-memo line 1d (second replacement
   candidate) is MOOT — never fired. The R5 same-family caveat for gpt-4.1-mini
   stays relevant only if the owner ever elects it as a judge.
3. **F11 C6 simplifies:** judge-A stays, so the pilot's classifier pin
   (`gpt-4.1-nano`) is not forced to change by certification. The pinned-classifier
   pre-registration line remains required by F3's route-divergence finding.
4. The F2 asymmetry finding is UNCHANGED and still governs: anchored 06/09 judging
   with nano depends on anchor quality; certification does not validate the anchors,
   only the judge's conclusion-neutrality without them.

## Spend

126 calls total (~0.10M in / ~8K out across three judges), estimated ≈ $0.02–0.04 vs
Item-1 ceiling $0.50 — well within envelope (OpenRouter dashboard = source of record).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · v1 untouched · no holdout content.
