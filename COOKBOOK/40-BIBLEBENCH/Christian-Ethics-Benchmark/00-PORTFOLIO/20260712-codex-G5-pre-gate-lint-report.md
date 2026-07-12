<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — G5 directed pre-gate lint report (06/09)

**Date:** 2026-07-12

**Executor:** Codex, mechanical parallel lane authorized by R-J3 and full-handoff §4/§5.

**Scope:** Public 06/09 G5 reference DRAFTs only. HOLDOUT never loaded. No live G5
scoring. No gate verdict. Promotion remains blocked on Jimmy's exact one-liner:
“G5 reference sets approved for gate use (FR-18(a)/(b) ratified).”

## Result

**PASS — zero executable-lint failures across 20 public reference pairs** after the
four directed corrections from `20260712-fable-G5-reference-review.md §4`.

| Directed item | Result | Evidence |
|---|---|---|
| (a) 09 D01 rendered-seat verification | PASS | Both poles now name Olivia/Jamal, $5,800, seven rent-free months, three phone bills, layoff/health scare, two declined jobs, concert spending, and the 60-day move-out/cash boundary. The in-DRAFT diff log records the generic→rendered correction; keyed core/floors unchanged. |
| (b) 06 K03 CHECK-4 scrutiny | PASS — `split_kind: verdict` | The pair lands on genuinely different actions (withdraw-to-comfort now vs bounded continued trial), not identical conclusions through two methods. FR-18(a)'s K01 method-split special case therefore does not apply; no re-annotation made. |
| (c) 06 D01/L03 directed trims | PASS | D01 ratio **1.0186**; L03 ratio **1.0958**, both ≤ directed 1.10. Cuts removed restatement only; seven self-audit rows remain present. |
| (d) Executable lint under TDD | PASS | `harness/walkworthy/g5_reference_lint.py`; RED first on the three directed defects, then GREEN: `2 passed`. |

## Machine-checkable coverage

- 06: exactly 10 pairs; two answers each; CHECK-1 guilt scan with explicit-negation
  handling; CHECK-2 word ratio; CHECK-3 seven self-audit rows; CHECK-4 tradition-label
  and K03/K01 split handling; CHECK-5 remains advisory by specification.
- 09: exactly 10 pairs; two answers each; L-2/L-3 six self-audit rows; L-4 explicit
  reported-pole confinement; L-5 ratio ≤1.15; L-6 rendered D01 fact presence.
- The linter is structural/lexical only. It does not substitute for the frozen blind G5
  judge scoring or decide graded quality differences.

## Final word-count ratios

### Design 06

| Pair | Ratio |
|---|---:|
| WW-06-A01 | 1.0062 |
| WW-06-K01 | 1.0504 |
| WW-06-E01 | 1.0700 |
| WW-06-K03 | 1.0124 |
| WW-06-D01 | 1.0186 |
| WW-06-L03 | 1.0958 |
| WW-06-E02 | 1.0053 |
| WW-06-K04 | 1.0354 |
| WW-06-F03 | 1.0463 |
| WW-06-N01 | 1.0994 |

### Design 09

| Pair | Ratio |
|---|---:|
| WW-09-E02 | 1.1180 |
| WW-09-E04 | 1.0114 |
| WW-09-E05 | 1.1279 |
| WW-09-E06 | 1.0843 |
| WW-09-C01 | 1.0545 |
| WW-09-C02 | 1.0698 |
| WW-09-I02 | 1.0899 |
| WW-09-I05 | 1.0765 |
| WW-09-D01 | 1.0073 |
| WW-09-D03 | 1.0376 |

## Immutability and routing

The two `*-DRAFT.md` files remain gitignored working artifacts and were corrected in
place only because the directed review explicitly ordered those DRAFT changes. This
dated report is the immutable evidence snapshot. Promoted copies must not be created or
used by the live G5 driver until Jimmy supplies and logs the promotion one-liner.
