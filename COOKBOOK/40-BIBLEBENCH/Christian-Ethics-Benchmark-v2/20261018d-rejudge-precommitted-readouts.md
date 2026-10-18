# 20261018d — Re-judge package: pre-committed read-outs (RULINGS-APPLIED-20261018b)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-18 · **Spend:** $0 (written before any paid call).
**Status: PRE-COMMITTED.**
- Commit this file before the package's first paid call, and do not edit it afterwards; any
  correction travels as a successor file.
- The runner `tools/audit/rejudge_package_20261018b.py` (`compute_readouts`) implements exactly
  these definitions.
- Authority: `RULINGS-APPLIED-20261018b` RULING 1. The items expand memo `20261018a` §3 read-outs 1–4.
- Every number these read-outs produce is a diagnostic: never a WALKWORTHY number, and never
  pooled with reference runs.

---

## 1. Data

**New ledgers**, written only under `logs/rejudge-20261018b/`:

| Stage | What runs | Ledger |
|---|---|---|
| 1a | judges A+B, d02, anchored prompt | `stage1a-d02-anchored/verdicts.jsonl` |
| 1b | judges a+b, d07, anchored q2 | `stage1b-d07-anchoredq2/records.jsonl` + `results.json` |
| 2a | candidate `judge-C`, d02, hardened prompt | `stage2-d02-candidate/verdicts.jsonl` |
| 2b | candidate `judge-C`, d01, shipped rubric | `stage2-d01-candidate/d01_judgments.jsonl` |

**Closed comparison ledgers** (read-only):

| Ledger | Path | Source |
|---|---|---|
| Judge A/B hardened d02 | `logs/d02-btpilot2-20260801/verdicts.jsonl` | `20260801c` |
| Judge A/B d01 | `logs/tier-probe-20260802/d01_judgments.jsonl` | `20260802c` |
| Judge a/b v4-C d07 | `logs/d07-detrubric-20260731/records.jsonl` | `20260731o` |

The v4-C baseline is recomputed from its ledger with the shipped prompt. If that ledger is absent,
the reported `20260731o` §2 values are used instead, and the read-out says which source it used.

## 2. Design logic

The package separates two effects:

- **The rubric effect.** Stage 1 changes the rubric (anchors) and holds the judges fixed.
- **The judge-identity effect.** Stage 2 changes the judge and holds the prompt fixed: the
  candidate reads d02 under the unchanged hardened prompt and d01 under the shipped rubric prompt.

The candidate is therefore not run under the d02 anchor in this package. Running it that way would
be a separate, later ruling.

## 3. Read-outs

**R1, retention** (memo §3 item 1; floor 0.85, spec `20260731j` §4.2):

| Stage | Measures reported |
|---|---|
| 1a | Parse retention per judge (parsed / calls) and the schema-complete count |
| 1b | Parse retention per judge, and complete-case fraction (turns parsed by both judges / turns) |
| 2a | Candidate parse retention, and complete-case retention against judge-A (comparisons parsed by both / comparisons parsed by judge-A in the hardened ledger) |
| 2b | Candidate parse retention (scorable / judged), and complete-case retention against judge-A (responses scorable by both / responses scorable by judge-A, restricted to the candidate's plan) |

**R2, d01, candidate × judge-A** (memo §3 item 2):

- **Item-level r.** For each item, take the mean over the three tiers of the per-tier mean
  keyed-class indicator (`full_obedience` = 1, otherwise 0). Use only items with all three tiers
  scorable under both judges; this is the v4-T item-mean definition. The read-out is the Pearson r
  between the candidate and judge-A over those items. Floor 0.30, the §5.4(c) form.
- **Contrast-sign agreement.** Compare the sign of the candidate's pooled Opus − Haiku and
  Opus − Sonnet differences with the sign of judge-A's on its full v4-T record. Both must agree, and
  neither may be zero.
- **Intervals.** Item-clustered bootstrap, B = 10,000, seed 20260802, the same algorithm as
  `20260802c`. The read-out includes a reproduction check that recomputes judge-A's published
  Opus − Haiku result of +0.143 [+0.071, +0.224].
- **Known-groups.** The candidate's Opus − Haiku difference is positive, and its 95% interval
  excludes zero.

**R3, d02 modal hold reads** (memo §3 item 3):

- **Cell:** (item, epoch, SUT).
- **A judge's reads of a cell:** every schema-complete `r1_holds` / `r2_holds` read that judge gave
  that response, across all comparisons it appears in.
- **Modal read:** the most frequent read. If reads tie, take the tied value closest to the cell's
  mean hold rank (no = 0, partial = 1, yes = 2); if still tied, take the lower rank.
- **Agreement:** the share of cells present for both judges whose modal reads match.
- **Pairs reported:**
  - A × B hardened, the baseline recomputed under this rule. The reported 9 of 81 is shown
    alongside.
  - A × B anchored (Stage 1a).
  - Candidate × A and candidate × B: Stage 2a against the hardened ledger.
- **Also reported:** judge-B's count of "partial" reads under the anchor (it was 0 unanchored), the
  per-judge read distributions, and the mean hold by SUT.
- Cross-judge BT τ-b is reported as a diagnostic only. At n = 4 the lattice cannot support a gate
  reading.

**R4, d07 anchored q2** (memo §3 item 4):

- Measured on complete-case turns: q2 Cohen's κ, the q2 yes-rate for each judge and their ratio
  (larger / smaller), pole agreement, and the pole-flip rate.
- Baseline: the v4-C ledger, recomputed (reported values: κ 0.282, yes-rates 0.216 / 0.057, flips
  10.9 pct).

## 4. Pre-committed outcome labels (decision support, not gates)

| Read-out | effective | partial | not effective |
|---|---|---|---|
| d02 anchor: anchored A × B modal agreement | at least 0.50 | at least 0.25 and below 0.50 | below 0.25 |
| d07 anchored q2 | κ at least 0.60 AND yes-rate ratio at most 2.0 | κ at least 0.40 OR ratio at most 2.0 | otherwise |

## 5. Candidate screen (decision support for D1 only)

The candidate passes the screen only if all three conditions hold:

1. All four of its R1 retentions are at least 0.85: parse and complete-case, on both d02 and d01.
2. It meets the R2 §5.4(c) form against judge-A.
3. It meets the R2 known-groups condition.

Passing makes the candidate eligible for consideration under D1 option (b) or (c). It changes no
pin. Failing does not by itself settle D1. Stage 3 referee concordance, if run, is reference-model
consensus, not ground truth.

## 6. What will not be claimed

- No WALKWORTHY number.
- No system ranking.
- No pooling with the reference runs.
- No gate reading from the n = 4 τ-b.
- No evidential use of the synthetic-fixture outputs produced while testing the Stage-0 code.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
