# SPEND MEMO — F5 judge certification + F3 cross-family classifier arm (session 6)

**Date:** 2026-07-16 (session 6) · **Status: AWAITING OWNER GO — no paid call has
been made this session.** The 2026-07-15/16 session-5 GO ($2.45 ceiling package,
~$0.9–1.5 spent) is **CLOSED**; nothing rolls over. PF-003 discipline: every item
below waits for explicit authorization; the availability probe (max_tokens=16, R10)
runs before any authorized item. OpenRouter dashboard is the spend source of record.
All estimates chars/4 input + per-call output allowances; ceilings are hard stops.

## Item 1 — F5: G5 neutrality certification runs (`tools/audit/judge_certify.py`)

Port is proven byte-identical to v1's frozen protocol (40/40 prompt-hash match, see
`20260716-f5-judge-certify-port.md`). Per judge: 40 initial + ≤40 re-elicitation
calls. The F2 answer-blind evidence predicts judge-A fails or barely passes — item
1c pre-authorizes the replacement path so ONE GO covers the likely failure.

| # | Judge | Est. (expected / worst) | Ceiling |
|---|---|---|---|
| 1a | judge-A `openai/gpt-4.1-nano` (incumbent; also the 02/07 classifier) | $0.005 / $0.009 | $0.10 |
| 1b | judge-B `meta-llama/llama-3.3-70b-instruct` (incumbent) | $0.005 / $0.008 | $0.10 |
| 1c | replacement judge-A candidate `openai/gpt-4.1-mini` (passed v1 G5 on both designs; **R5 caveat: same family as the gpt-4.1-mini SUT** — its 06/09 cells for that SUT lean on judge-B) | $0.020 / $0.034 | $0.15 |
| 1d | OPTIONAL second replacement candidate, only if 1a AND 1c both disqualify (slug TBD with owner; NOT gemini-2.5-flash — v1 G5 disqualified it on 09) | ~$0.03 | $0.15 |

**Item-1 package ceiling: $0.50.** Deliverable: `logs/judge-certify-20260716/` +
dated certification report; PASS/DISQUALIFIED per (design, judge); R6 PROVISIONAL
labels lift only for judges that PASS both designs.

## Item 2 — F3: cross-family classifier agreement (`tools/audit/classifier_sensitivity.py --alt-classifier`)

Re-classify the 1,435 stored 02/07 branched turns (classifier-tokens only, ZERO SUT
re-runs). Offline replay already showed route-dependence of 24–91% per turn
(`20260716-f3-classifier-sensitivity-report.md`); this arm measures the
decision-relevant number — model-vs-model agreement with the pilot's nano route.

| # | Alt classifier | Est. | Ceiling |
|---|---|---|---|
| 2a | `mistralai/mistral-small-3.2-24b-instruct` (cross-family, cheap) | ~$0.11 | $0.30 |
| 2b | `google/gemini-2.5-flash-lite` (second family; classifier duty only — the v1 G5 judge disqualification does not bear on branch classification, noted for transparency) | ~$0.11–0.25 | $0.35 |

**Item-2 package ceiling: $0.65.** Deliverable: alt-classification JSONLs + dated
agreement report; if cross-family agreement is materially below the ~0.85 judge-swap
analogue, the F11 C6 pinned-classifier line hardens from "required disclosure" to
"single-classifier instrument, no cross-classifier pooling ever."

## Item 3 — F2 arm 2c: d02-anchors-on (built, un-fired) — ONLY IF OWNER ASKS

Pre-built in session 5 (`judge_ablation.py --arm d02-anchors-on`), needs its own GO
per the session-5 ruling. ~$1.50 ceiling as previously estimated. Not part of this
memo's default package; listed so one signature CAN cover it if the owner opts in.

## Authorization grid (owner marks)

- [ ] GO items 1a–1c (+1d fallback) — F5 certification, ceiling $0.50
- [ ] GO items 2a–2b — F3 cross-family arm, ceiling $0.65
- [ ] GO item 3 — F2-2c, ceiling $1.50 (opt-in)
- [ ] NO-GO / amend: ____________

**Default full package (1+2): expected ≈ $0.35, hard ceiling $1.15.** With 2c:
ceiling $2.65.

**Canary:** WALKWORTHY-CANARY-7f3e2026.
