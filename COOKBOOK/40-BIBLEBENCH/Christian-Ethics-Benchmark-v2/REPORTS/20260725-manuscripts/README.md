# WALKWORTHY phase-6 manuscript assembly

**Date:** 2026-07-25 · **Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Governing ruling:** `../../RULINGS-APPLIED-20260725b.md` (Q1 = split, both papers live;
Q2 = execute the skeleton's §7 contingency)
**Spend:** $0. No model calls, no runs. Prose assembly only.

---

## The two manuscripts

| File | Paper | Status |
|---|---|---|
| `20260725-paper-a-walkworthy-benchmark-v0.1.md` | (a) benchmark / instrument + validity | v0.1 assembled |
| `20260725-paper-b-judging-the-judges-v0.1.md` | (b) judge-sensitivity methods note | v0.1 assembled |

**Both are GENERATED FILES.** Do not hand-edit them — edit the part files and rebuild.

## How to rebuild

```
./.venv/bin/python REPORTS/20260725-manuscripts/assemble.py      # parts -> manuscripts
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py REPORTS/20260725-manuscripts
```

`lint_claims.py` exits non-zero on any BLOCKER. It enforces the binding claims
discipline (`06-messaging.md` §5 items 1–7, plus R3 interval language, the corrected
non-dominance framing, the design-02 reporting surface, and the canary). It has been
validated against a probe file of deliberate violations — if you change its rules,
re-validate it the same way; a linter never shown to catch anything proves nothing.

## Where each section comes from

### Paper (a)

| § | Source | Note |
|---|---|---|
| front matter | `parts/pa-00-frontmatter.md` | title, abstract, keywords |
| §1, §5 | `parts/pa-01-intro-itemdev.md` | non-adjacent — split at assembly |
| §2 | `parts/pa-04-related-work.md` | carries a citation ledger |
| §3, §4 | **transplant** `../20260724c-paper-design-section-draft.md` v1.1 | adversarial SHIP; `<!-- src -->` comments stripped at transplant per owner ruling |
| §6, §7 | `parts/pa-02-methods-fullbank.md` | |
| §8 | **transplant** `../20260724-paper-validity-section-draft.md` v1.1 | `X.n` renumbered to `8.n`; **X.8 excluded** — already merged into §9 |
| §9, §10 | `parts/pa-03-limitations-future.md` | §9 merges validity X.8 with the seven non-claims |

### Paper (b)

| § | Source | Note |
|---|---|---|
| front matter | `parts/pb-00-frontmatter.md` | |
| §1, §6, §7 | `parts/pb-01-intro-limitations-future.md` | non-adjacent — split at assembly |
| §2 | `parts/pb-04-related-work.md` | carries a citation ledger |
| §3, §4 | `parts/pb-02-testbed-method.md` | §3 is a COMPRESSED self-contained instrument description |
| §5 | `parts/pb-03-results.md` | the ARM 1 core |

## Division of evidence — binding, from RULING 1

Paper (b) owns the variance decomposition and the two-referee method. **Paper (a) must
not reproduce the decomposition numbers** — it states the judge-sensitivity verdict
qualitatively and hands off to the companion methods paper. Two sanctioned exceptions
exist in paper (a): §9 cites the system-by-judge interaction **read against its
df-proportional no-effect reference line** when scoping the comparative limitation, and §10
cites the design-02 interaction (46.5% on a 5.8% system main effect) when arguing the
taxonomy repair.

> **Corrected 2026-07-29.** This paragraph previously described §9 as citing "the 8-of-8
> interaction". That formulation — "non-zero in 8 of 8" — was **WITHDRAWN as evidential** by
> `../../RULINGS-APPLIED-20260725c.md` RULING 1, because an SS is almost surely non-zero and
> four of the eight interactions sit at or below the df-proportional line. It no longer
> appears anywhere in paper (a); the manuscript was already correct and only this README was
> stale.

Each manuscript is self-contained on its own claims. Neither may depend on the other
being published first.

## Framing correction — do not undo it

**Never write "the judge dominates."** Judge and system footprints are comparable at the
median (35.3% vs 35.6%) and the system main effect is the largest single term in four of
the eight judged designs. **This prohibition is BLOCKER-enforced by `lint_claims.py`.**

The binding suite-wide claim is the one ruled in `../../RULINGS-APPLIED-20260725c.md`
RULING 1, quoted verbatim:

> *The models differ on most designs. On a minority of designs the judges clearly
> disagree about the ordering; on the rest the systems are too tightly spaced for
> either judge to resolve. Either way, no comparative claim survives the swap.*

Two riders travel with it. "Models genuinely differ" is **design-specific**, not suite-wide
— %SUT sits below the df-proportional line in designs 02, 03 and 08. And "a large model
effect the judges still reorder" is restricted to **design 01 alone**; designs 06 and 09 are
re-grounded in the graded flip verdicts instead.

> **Corrected 2026-07-29.** This section previously stated the claim as *"the models differ,
> but the judges disagree about the ordering in every judged design"* and asserted that the
> linter enforced it. Both were wrong after RULING 1: the "every judged design" reading was
> replaced by the narrowed claim above, and the linter only ever enforced the *prohibition*
> (a BLOCKER regex on judge-dominates), never the positive framing — no linter rule can
> verify that a claim is correctly scoped. The manuscript prose already carries the narrowed
> claim; only this README was stale.

## Verification performed at v0.1

- Test suite **33/33 pass** (project venv, py3.14 — the vault venv is py3.9 and cannot run it).
- Claims linter clean across all parts and both manuscripts.
- **Holdout quarantine verified**: 157 distinct item IDs extracted from `banks-holdout/`;
  zero occur in any phase-6 artifact.
- Key figures cross-checked between the run report / decomposition addendum and both
  manuscripts.

## Not done at v0.1 — carried forward

- Supplementary material is not assembled (IVR-1.1 rater protocol, PE-1..25 ledger,
  per-design agreement tables, consolidated defect ledger).
- ~~`[CITATION NEEDED]` markers in §2 of either paper~~ — **CLOSED 2026-07-29** by an
  authorized external citation sweep. All eight bracketed markers (two in paper (a), six in
  paper (b)) are filled. The added works are not vault-resident and are itemised, with
  retrieval dates, in per-part "External sources" ledger tables. One candidate source was
  fetched, inspected and **rejected as unverifiable**; it is recorded as rejected in the
  paper (b) ledger so it is not silently rediscovered. Two of the closures narrowed a claim
  under owner authorization — paper (a)'s Christian-corpus novelty statement and paper (b)'s
  cost-barrier sentence — and both narrowings make the papers claim less, not more.
- No venue or authorship decision has been made. Both manuscripts stay venue-generic and
  author-generic.
- The holdout remains quarantined and its first use is **recommended against** for now —
  not ruled.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
