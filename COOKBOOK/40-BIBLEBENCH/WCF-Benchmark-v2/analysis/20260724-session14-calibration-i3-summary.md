# Session-14 Phase-2 STRICT-judge calibration — i3 summary

Revised strict template (DELIVERABLE CHECK first + hardened CREDITED arithmetic + (absent) sentinel + GATE-misfire guard) over the logged s13 SUT responses. Delta columns/notes are vs iteration 0 (`20260724-session14-calibration-results.json`).

Generated 2026-07-24. Judges: gemini-2.5-flash, deepseek-chat, mistral-small-2603. temp=0.0. Offline (logged s13 SUT responses; no SUT calls).

Cost estimate: $0.5650 over 156 calls (955,084 tokens). Cap $0.55. Cap hit: True.


## (a) Control items (qwen SUT)

| id | role | judge scores (gem/deep/mist) | strict median | strict min | s13 score | expected real | Δmed vs i0 | Δmin vs i0 |
|----|------|------------------------------|---------------|-----------|-----------|---------------|-----------|-----------|
| LIB-N-006 | positive_control | 100 / 100 / 100 | 100 | 100 | 100 | ~83 | +0 | +0 |
| PROOF-N-009 | positive_control | 10 / 64 / 9 | 10 | 9 | 100 | ~83-91 | -90 | -91 |
| MEND-N-002 | negative_control | 100 / 100 / 100 | 100 | 100 | 100 | genuine-100 | +0 | +0 |
| MEND-N-009 | negative_control | 100 / 100 / 100 | 100 | 100 | 100 | genuine-100 | +0 | +0 |
| PROOF-N-005 | negative_control | 100 / 100 / 100 | 100 | 100 | 100 | genuine-100 | +0 | +0 |
| WHOLE-N-004 | negative_control | 100 / 100 / 100 | 100 | 100 | 100 | genuine-100 | +0 | +0 |

## (b) tied100_sample items

| id | qwen med | qwen min | haiku med | haiku min | s13 qwen | s13 haiku | strict|q-h| med | strict|q-h| min | Δ|q-h|med vs i0 | Δ|q-h|min vs i0 |
|----|----------|----------|-----------|-----------|----------|-----------|-----------------|-----------------|-----------------|-----------------|
| MEND-N-001 | 100 | 100 | 100 | 77 | 100 | 100 | 0 | 23 | +0 | +7 |
| MEND-N-003 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| MEND-N-004 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | -5 |
| MEND-N-005 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | -4 |
| MEND-N-007 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| LIB-N-004 | 100 | 100 | 8 | 8 | 100 | 100 | 92 | 92 | +92 | +85 |
| LIB-N-007 | 100 | 94 | 100 | 100 | 100 | 100 | 0 | 6 | +0 | +6 |
| LIB-N-008 | 100 | 92 | 100 | 100 | 100 | 100 | 0 | 8 | +0 | +8 |
| LIB-N-010 | 100 | 100 | 8 | 8 | 100 | 100 | 92 | 92 | +92 | +85 |
| LIB-N-011 | 8 | 8 | 8 | 8 | 100 | 100 | 0 | 0 | -25 | -8 |
| PROOF-N-001 | 100 | 10 | 100 | 100 | 100 | 100 | 0 | 90 | +0 | +82 |
| PROOF-N-003 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| PROOF-N-007 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| PROOF-N-010 | 100 | 9 | 100 | 100 | 100 | 100 | 0 | 91 | -5 | +83 |
| PROOF-N-011 | 100 | 93 | 100 | 100 | 100 | 100 | 0 | 7 | +0 | +0 |
| WHOLE-N-002 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| WHOLE-N-003 | 100 | 100 | 8 | 0 | 100 | 100 | 92 | 100 | +92 | +96 |
| WHOLE-N-006 | 100 | 100 | 100 | 100 | 100 | 100 | 0 | 0 | +0 | +0 |
| WHOLE-N-007 | 100 | 7 | 8 | 8 | 100 | 100 | 92 | 1 | +92 | -16 |
| WHOLE-N-008 | 100 | 100 | 100 | 8 | 100 | 100 | 0 | 92 | +0 | +92 |

**Tied-100 items no longer tied (nonzero strict |qwen-haiku|):** under MEDIAN = 4/20 (i0 2; Δ +2); under MIN = 11/20 (i0 11; Δ +0).


## (c) Fabrication flags

Total flagged (item x SUT x judge with >=1 fabricated claimed quote): **127** (i0 142; Δ -15). Rate this run: 127/156 judge-verdicts.

Per-judge fabrication flags (this run / i0 / Δ):
- gemini-2.5-flash: 40 / 41 / -1
- deepseek-chat: 44 / 50 / -6
- mistral-small-2603: 43 / 51 / -8

LIB-N-006 (qwen) per-judge fabrication flag:
- gemini-2.5-flash: flagged = False
- deepseek-chat: flagged = True
- mistral-small-2603: flagged = True
- LIB-N-006/qwen/deepseek-chat: score=100, flagged=True
- LIB-N-006/qwen/mistral-small-2603: score=100, flagged=True

All flags (id / sut / judge):
- LIB-N-006 / qwen / deepseek-chat
- LIB-N-006 / qwen / mistral-small-2603
- LIB-N-006 / haiku / deepseek-chat
- LIB-N-006 / haiku / mistral-small-2603
- PROOF-N-009 / qwen / gemini-2.5-flash
- PROOF-N-009 / qwen / deepseek-chat
- PROOF-N-009 / qwen / mistral-small-2603
- MEND-N-002 / qwen / gemini-2.5-flash
- MEND-N-002 / qwen / mistral-small-2603
- MEND-N-002 / haiku / gemini-2.5-flash
- MEND-N-002 / haiku / deepseek-chat
- MEND-N-002 / haiku / mistral-small-2603
- MEND-N-009 / qwen / gemini-2.5-flash
- MEND-N-009 / qwen / deepseek-chat
- MEND-N-009 / qwen / mistral-small-2603
- MEND-N-009 / haiku / gemini-2.5-flash
- MEND-N-009 / haiku / deepseek-chat
- MEND-N-009 / haiku / mistral-small-2603
- PROOF-N-005 / qwen / gemini-2.5-flash
- PROOF-N-005 / qwen / deepseek-chat
- PROOF-N-005 / qwen / mistral-small-2603
- PROOF-N-005 / haiku / gemini-2.5-flash
- PROOF-N-005 / haiku / mistral-small-2603
- WHOLE-N-004 / qwen / gemini-2.5-flash
- WHOLE-N-004 / qwen / deepseek-chat
- WHOLE-N-004 / qwen / mistral-small-2603
- WHOLE-N-004 / haiku / gemini-2.5-flash
- WHOLE-N-004 / haiku / deepseek-chat
- WHOLE-N-004 / haiku / mistral-small-2603
- MEND-N-001 / qwen / gemini-2.5-flash
- MEND-N-001 / qwen / deepseek-chat
- MEND-N-001 / qwen / mistral-small-2603
- MEND-N-001 / haiku / gemini-2.5-flash
- MEND-N-001 / haiku / deepseek-chat
- MEND-N-001 / haiku / mistral-small-2603
- MEND-N-003 / qwen / deepseek-chat
- MEND-N-003 / qwen / mistral-small-2603
- MEND-N-003 / haiku / gemini-2.5-flash
- MEND-N-003 / haiku / deepseek-chat
- MEND-N-003 / haiku / mistral-small-2603
- MEND-N-004 / qwen / gemini-2.5-flash
- MEND-N-004 / qwen / deepseek-chat
- MEND-N-004 / qwen / mistral-small-2603
- MEND-N-004 / haiku / gemini-2.5-flash
- MEND-N-004 / haiku / deepseek-chat
- MEND-N-004 / haiku / mistral-small-2603
- MEND-N-005 / qwen / deepseek-chat
- MEND-N-005 / qwen / mistral-small-2603
- MEND-N-005 / haiku / gemini-2.5-flash
- MEND-N-005 / haiku / deepseek-chat
- MEND-N-005 / haiku / mistral-small-2603
- MEND-N-007 / qwen / gemini-2.5-flash
- MEND-N-007 / qwen / deepseek-chat
- MEND-N-007 / qwen / mistral-small-2603
- MEND-N-007 / haiku / gemini-2.5-flash
- MEND-N-007 / haiku / deepseek-chat
- MEND-N-007 / haiku / mistral-small-2603
- LIB-N-004 / qwen / gemini-2.5-flash
- LIB-N-004 / qwen / deepseek-chat
- LIB-N-004 / qwen / mistral-small-2603
- LIB-N-004 / haiku / gemini-2.5-flash
- LIB-N-007 / qwen / gemini-2.5-flash
- LIB-N-007 / qwen / deepseek-chat
- LIB-N-007 / qwen / mistral-small-2603
- LIB-N-007 / haiku / gemini-2.5-flash
- LIB-N-007 / haiku / deepseek-chat
- LIB-N-007 / haiku / mistral-small-2603
- LIB-N-008 / qwen / deepseek-chat
- LIB-N-008 / qwen / mistral-small-2603
- LIB-N-008 / haiku / gemini-2.5-flash
- LIB-N-008 / haiku / deepseek-chat
- LIB-N-008 / haiku / mistral-small-2603
- LIB-N-010 / qwen / gemini-2.5-flash
- LIB-N-010 / qwen / mistral-small-2603
- LIB-N-010 / haiku / gemini-2.5-flash
- LIB-N-010 / haiku / deepseek-chat
- LIB-N-011 / qwen / gemini-2.5-flash
- LIB-N-011 / qwen / deepseek-chat
- LIB-N-011 / haiku / gemini-2.5-flash
- PROOF-N-001 / qwen / mistral-small-2603
- PROOF-N-001 / haiku / gemini-2.5-flash
- PROOF-N-001 / haiku / deepseek-chat
- PROOF-N-001 / haiku / mistral-small-2603
- PROOF-N-003 / qwen / gemini-2.5-flash
- PROOF-N-003 / qwen / deepseek-chat
- PROOF-N-003 / qwen / mistral-small-2603
- PROOF-N-003 / haiku / gemini-2.5-flash
- PROOF-N-003 / haiku / deepseek-chat
- PROOF-N-003 / haiku / mistral-small-2603
- PROOF-N-007 / qwen / gemini-2.5-flash
- PROOF-N-007 / qwen / deepseek-chat
- PROOF-N-007 / qwen / mistral-small-2603
- PROOF-N-007 / haiku / gemini-2.5-flash
- PROOF-N-007 / haiku / deepseek-chat
- PROOF-N-007 / haiku / mistral-small-2603
- PROOF-N-010 / qwen / deepseek-chat
- PROOF-N-010 / qwen / mistral-small-2603
- PROOF-N-010 / haiku / gemini-2.5-flash
- PROOF-N-010 / haiku / deepseek-chat
- PROOF-N-010 / haiku / mistral-small-2603
- PROOF-N-011 / qwen / gemini-2.5-flash
- PROOF-N-011 / qwen / deepseek-chat
- PROOF-N-011 / qwen / mistral-small-2603
- PROOF-N-011 / haiku / gemini-2.5-flash
- PROOF-N-011 / haiku / deepseek-chat
- PROOF-N-011 / haiku / mistral-small-2603
- WHOLE-N-002 / qwen / gemini-2.5-flash
- WHOLE-N-002 / qwen / deepseek-chat
- WHOLE-N-002 / qwen / mistral-small-2603
- WHOLE-N-002 / haiku / gemini-2.5-flash
- WHOLE-N-002 / haiku / deepseek-chat
- WHOLE-N-002 / haiku / mistral-small-2603
- WHOLE-N-003 / qwen / gemini-2.5-flash
- WHOLE-N-003 / qwen / deepseek-chat
- WHOLE-N-003 / qwen / mistral-small-2603
- WHOLE-N-003 / haiku / deepseek-chat
- WHOLE-N-006 / qwen / deepseek-chat
- WHOLE-N-006 / qwen / mistral-small-2603
- WHOLE-N-006 / haiku / gemini-2.5-flash
- WHOLE-N-006 / haiku / deepseek-chat
- WHOLE-N-006 / haiku / mistral-small-2603
- WHOLE-N-007 / qwen / gemini-2.5-flash
- WHOLE-N-007 / qwen / deepseek-chat
- WHOLE-N-008 / qwen / deepseek-chat
- WHOLE-N-008 / qwen / mistral-small-2603
- WHOLE-N-008 / haiku / gemini-2.5-flash
- WHOLE-N-008 / haiku / deepseek-chat

## (d) Unscored / parse failures after retry

Count: **0** (i0 0; Δ +0).

## (e) Spend estimate

This run (i3): $0.5650 (955,084 tokens, 156 calls). Per-run cap $0.55. Cap hit: True.

Iteration-0 spend: $0.4086. Δ this run vs i0: $+0.1564. Cumulative calibration spend: $0.9736 (budget < $1.00).

## (g) DELIVERABLE CHECK verdicts (audited refusal / non-delivery items)

Per-judge `delivered` flag + score + #(absent) deductions. Audit expects DELIVERED=no → score at the manner-line ceiling (~5-15).

| id | sut | judge | delivered | #absent | score |
|----|-----|-------|-----------|---------|-------|
| LIB-N-011 | qwen | gemini-2.5-flash | False | 5 | 8 |
| LIB-N-011 | qwen | deepseek-chat | False | 5 | 9 |
| LIB-N-011 | qwen | mistral-small-2603 | False | 5 | 8 |
| LIB-N-011 | haiku | gemini-2.5-flash | False | 2 | 75 |
| LIB-N-011 | haiku | deepseek-chat | False | 5 | 8 |
| LIB-N-011 | haiku | mistral-small-2603 | False | 5 | 8 |
| WHOLE-N-007 | haiku | gemini-2.5-flash | False | 5 | 8 |
| WHOLE-N-007 | haiku | deepseek-chat | False | 5 | 8 |
| WHOLE-N-007 | haiku | mistral-small-2603 | False | 5 | 8 |
| MEND-N-001 | haiku | gemini-2.5-flash | True | 0 | 77 |
| MEND-N-001 | haiku | deepseek-chat | True | 0 | 100 |
| MEND-N-001 | haiku | mistral-small-2603 | True | 0 | 100 |
| WHOLE-N-002 | qwen | gemini-2.5-flash | True | 0 | 100 |
| WHOLE-N-002 | qwen | deepseek-chat | True | 0 | 100 |
| WHOLE-N-002 | qwen | mistral-small-2603 | True | 0 | 100 |

## (f) Files written

- `analysis/20260724-session14-calibration-i3-results.json`
- `analysis/20260724-session14-calibration-i3-summary.md`
