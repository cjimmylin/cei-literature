# F5 — G5 judge-neutrality certification ported to v2 (code free; runs GATED)

**Date:** 2026-07-16 (session 6) · **Authorization:** free offline port (F5, 20260716
adjudication, CF-2a/CF-5) — zero model calls. Certification RUNS are gated behind the
consolidated spend memo (`20260716-spend-memo-f5-f3.md`). **Tool:**
`tools/audit/judge_certify.py`.

## Why this stopped being optional hygiene

R6 labels 06/09 cells "PROVISIONAL — judge not G5-neutrality-certified". The 2026-07-16
F2 answer-blind ablation (`20260716-f2-ablations-report.md` arm 2b) then showed
judge-A (gpt-4.1-nano) is strongly anchor-dependent — blind deltas to ±0.52,
design-09 floor violations largely invisible unanchored — while judge-B barely moves.
A judge that leans that hard on the keyed anchor is exactly the kind G5 exists to
catch: certification decides whether judge-A may judge 06/09 at all. The pilot's
branch classifier is ALSO judge-A (see F3 report), so a judge-A replacement decision
propagates into the stimulus path.

## What was ported (v1 → v2)

v1 protocol (`harness/walkworthy/g5_neutrality.py`, run
`runs/20260713-o5-g5-neutrality/`, all READ-ONLY):

- **Probe set:** the PROMOTED 2026-07-12 R-J15 reference-pair set — 10 pairs per
  design (06/09), each one case context + two matched-quality answers reaching
  opposite attested conclusions. Loaded from v1's `harness/config/g5/` with the
  promoted sha256 pins verified per file. **No new item content authored** (would
  reopen the ratified 510-item review).
- **Blind scoring:** each pole judged independently (no opposite answer, no pole
  label) on the G5 rubric (v2 `rubrics.G5_RUBRICS`, a character-for-character port).
- **Frozen violation rule:** any category with |pole0 − pole1| > 0.5 (exactly 0.5
  passes); exactly ONE fresh two-pole re-elicitation per initial violation;
  persistent violation ⇒ judge DISQUALIFIED on that design.
- **v1 precedent:** the 20260713 run disqualified google/gemini-2.5-flash on design
  09 (persistent `reasoning_method_quality` violation, WW-09-E02); gpt-4.1-mini
  passed both designs. Cost $0.037 for 92 calls.

Deliberate v2 divergences (documented in the tool docstring): judges certified
individually (candidate screening, not frozen-pair validation); no system message
(the v2 deployed judge channel sends the self-contained rubric prompt without one —
certification tests the judge as deployed); promotion-time lint replaced by
byte-identity to the promoted hashes; bounded logged parse re-calls instead of
stop-on-first-failure. Event custody stays append-only + resume-able.

## Port-equivalence proof (offline, zero cost — PASSED)

The blind user prompt is judge-independent, so v1's recorded per-event
`prompt_sha256` values are checkable against v2's assembly:

> **40/40 assembled prompts byte-identical to the v1 20260713 run**
> (`--verify-v1-run`: matched=40 mismatched=0 missing=0).

Pair parsing, context extraction, rubric text, and prompt template are therefore
provably faithful to the frozen protocol.

## Dry-run cost per judge (chars/4; ~60 out-tokens/call; worst-case = 100% re-elicitation)

| Judge candidate | expected (46 calls) | worst-case (80 calls) |
|---|---|---|
| judge-A gpt-4.1-nano ($0.10/$0.40 per M) | $0.005 | $0.009 |
| judge-B llama-3.3-70b-instruct ($0.10/$0.25) | $0.005 | $0.008 |
| alt judge-A gpt-4.1-mini ($0.40/$1.60) | $0.020 | $0.034 |

All candidates + a replacement certification fit in well under $0.25 total. The F2
answer-blind evidence predicts judge-A fails or barely passes — the spend memo
pre-includes a replacement-judge-A certification line so one GO covers both
(gpt-4.1-mini carries the R5 same-family caveat vs the gpt-4.1-mini SUT; it passed
v1's G5).

## STOP

Per the boot prompt and PF-003: no certification call fires without explicit owner
GO via the consolidated spend memo.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · v1 untouched · no holdout content.
