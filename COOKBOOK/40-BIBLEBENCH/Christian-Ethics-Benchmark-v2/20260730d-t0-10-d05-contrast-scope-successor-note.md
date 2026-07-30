# T0-10 — Successor note: scope of the published design-05 C1 contrast result

**Date:** 2026-07-30 · **Tier:** 0 (offline recompute, $0) · **Item:** T0-10
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Authorization:** `RULINGS-APPLIED-20260729d.md` (Tier 0 of the repair queue)

This note CORRECTS THE SCOPE LABEL of a published number without editing any immutable
report. It succeeds, and must be read alongside:

- `20260725-fullbank-3ep-run-report.md`, headline finding 2 and the design-05 section
  ("0 of 10 pairwise contrasts have a Bonferroni-widened interval that excludes zero",
  described there as "the full pre-registered C1 contrast set");
- `REPORTS/20260725-manuscripts/20260725-paper-a-walkworthy-benchmark-v0.1.md`, the two
  passages citing "0 of 10" as pre-registered pairwise contrasts.

Recompute artifacts: `tools/audit/t0_10_d05_stratum_contrasts.py` (durable, git-tracked)
and raw output `logs/fullbank-3ep-20260724/20260730-t0-10-d05-stratum-contrasts.txt`.
The recompute passed its G0 gate: its all-strata panel reproduces the original
`c1_design05_contrasts.py` output byte-identically over the 21 numeric lines through the
headline, before any variant was computed.

## 1. The defect

The pre-registration (`20260716-prereg-comparisons-RATIFIED.md`, C1) scopes the primary
contrast family to "stratum-(a) cells only." The script that produced the published
number, `logs/fullbank-3ep-20260724/c1_design05_contrasts.py`, filters exemplars but
applies NO stratum filter: the published "0 of 10" was computed over stratum (a) and
stratum (c) pooled (19 + 9 non-exemplar items). The published description of that number
as "the full pre-registered C1 contrast set" is therefore a scope misdescription.

## 2. What the recompute shows

1. **Stratum-(a)-only, same machinery: 0 of 10 contrasts exclude zero.** The published
   verdict is unchanged under the pre-registered scope. The defect is the label, not the
   conclusion.
2. **Cell sizes, stratum-(a).** Bank universe is 19 non-exemplar items (not 18 as the
   planning snapshot stated). Scored per system: deepseek 19, gpt41mini 19, mistral 18,
   gemini 18, llama 18. The single missing item is `WW-05-L01`, which has no scored
   administration in any of the three epochs for exactly those three systems — the
   administration is absent from their logs, not present-with-NaN. This is a
   data-completeness diagnostic carried to the Gate A memo; it is not chased further here.
3. **Stratum source agreement.** `datasets/public/design05.jsonl` metadata and the eval-log
   sample metadata agree on the stratum of all 32 items; the bank was used as source of
   truth and nothing hinges on the choice.

## 3. Adjudication

### 3.1 The number of record for pre-registered claims

The pre-registered C1 design-05 cell is the **stratum-(a)-only computation: 0 of 10
contrasts exclude zero.** Any future text calling the design-05 result "pre-registered"
refers to this computation. The published pooled computation is RELABELED, not withdrawn:
it stands as a **sensitivity check across strata**, and it agrees with the pre-registered
result in headline, direction, and every per-contrast verdict.

The merits argument for why the pooled check is informative rather than contaminating —
made explicitly, as required, not assumed: stratum (c) is excluded from comparative
families because judges are not G5-certified on disputed items, i.e. the exclusion
protects against judge unreliability. Design 05's primary metric,
`constraint_satisfaction_rate`, is parsed allocation against keyed constraints and never
touches a judge, so the hazard the exclusion guards against cannot operate on this
surface. That reasoning justifies *reporting the pooled number as a labeled sensitivity
check*. It does NOT justify calling the pooled number pre-registered: a pre-registered
scope binds regardless of whether its motivation applies to a particular cell, and
post-hoc re-scoping on the merits is precisely the flexibility pre-registration exists to
remove. Hence the relabeling above rather than a defense of the original label.

### 3.2 The C5 floor

RULING 1b as ratified sets the single-turn floor at "n≥20 scored non-exemplar admins per
cell." Admins means administrations (item × epoch). The stratum-(a) design-05 cells hold
54–55 scored non-exemplar admins per system (maximum possible 57), so **every cell passes
the ratified floor and the stratum-(a) result is reportable.** The planning snapshot's
claim that the cell "would not be reportable at all" is refuted on the ratified text; it
holds only under an items-as-effective-n reading (18–19 epoch-averaged items vs 20) that
the pre-registration does not state.

One tension is worth recording as instrument diagnostics rather than resolving here: the
contrast construction epoch-averages first, so its inferential n is items (18–19), while
the floor counts admins (54–55). A floor drafted in admins therefore guarantees less than
the standard-error construction implies. Restating the floor in effective-n units would be
an instrument change (Tier 3 material, not authorized, noted only).

### 3.3 Corrections to the planning snapshot

For the record, two factual claims in the 2026-07-30 boot prompt's T0-10 entry are
corrected by this note: the stratum-(a) cell is 19 items in the bank (18 scored for three
of five systems, 19 for two), and the cell is reportable under the ratified C5 floor.

## 4. Impact

- The manuscripts' design-05 verdict — no pairwise contrast excludes zero on the one
  judge-free surface — is **unchanged** under the pre-registered scope. No published
  quantity changes value.
- The manuscripts' other leg (judge-swap ordering flips) is untouched by any of this.
- Required future wording: pre-registered claims cite the stratum-(a) computation; the
  pooled computation may be cited only as a sensitivity check with its label.
- No edit is made to any immutable report or to the manuscripts by this note; successor
  notes are the correction vehicle of record.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
