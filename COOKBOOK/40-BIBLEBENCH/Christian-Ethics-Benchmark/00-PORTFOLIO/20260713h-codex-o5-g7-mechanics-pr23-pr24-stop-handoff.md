# WALKWORTHY — O5 W5/G7 No-Call Mechanics Complete; PR-23/PR-24 Stop Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** PR-18 RATIFIED/CLOSED; NO-CALL MECHANICS GREEN; W5 STOPPED ON PR-23/PR-24
**Scope:** WALKWORTHY only; PUBLIC data only; no HOLDOUT, credentials, live calls, spend, or label edits

## Outcome

Jimmy's PR-18 A2/B1/C3/D1/E3 ruling is recorded verbatim in
`20260713e-jimmy-pr18-ruling.md` and closed in `PENDING-RULINGS.md`. The deterministic
PUBLIC-only G7 mechanics are implemented under TDD in
`harness/walkworthy/g7_perturbation.py` with 39 focused tests:

- **A2:** validates the frozen 344-item runnable PUBLIC population, applies round-half-up
  within every nonempty easy/hard stratum, and binds the resulting 73 items, item hashes,
  six explicit model IDs, and 438 cells per battery into a deterministic manifest.
- **B1:** templates only user-authored administration fields, protects declared names,
  quantities, quotes, polarity/modality/comparisons, structure, and non-user fields, and
  accepts only an exact Boolean L1–L9 result. New sentence-initial, Unicode, or hyphenated
  name-like tokens fail closed.
- **C3/E3:** reduces the two batteries by any-battery change in the adjudicated
  load-bearing outcome, uses the fixed 438-cell denominator and 43-flip ceiling, marks an
  item affected at three or more of six models, and remains `PENDING` for every missing,
  malformed, provenance-invalid, unit-mismatched, or unresolved cell.
- **D1 primitives:** require an explicit per-item role declaration, including zero-role
  items; verify exact occurrences; allocate deterministically in stable order; and enforce
  one no-reuse registry per design. The production 73-item role artifact is intentionally
  not guessed before PR-23.

The fresh full harness suite passes: **446/446**. An independent requirements review and
an independent fail-closed/code-quality review both returned **PASS** after the final
three corrections.

## Genuine remaining specification stops

### PR-23 — name-swap surface

PR-18 did not specify whether D1 rotates all model-visible role occurrences or only the
B1 user-authored fields, nor how plural family surnames and compound household labels are
treated. Evidence and options are in
`20260713f-codex-pr23-g7-name-surface-decision.md`.

Recommended owner one-liner:

> Ratify PR-23 option 1: G7 name swaps cover every exact declared personal given-name
> occurrence in model-visible administration system and user fields; hidden metadata,
> keys, anchors, facts_diff, and extras remain unchanged; plural family surnames,
> compound household labels, surnames, and initials are protected non-role literals;
> explicit zero-role items remain fixed-denominator no-op name-swap cells; do not add a
> surname inventory, replace sampled items, shrink the denominator, or make live calls.

### PR-24 — design-05 outcome

Design 05 has a frozen judge-free allocation CSR primary but no registered adjudicated
categorical outcome; substituting `rationale_honesty` would change the metric. Evidence
and options are in `20260713g-codex-pr24-g7-design05-outcome-decision.md`. The reducer
currently names every design-05 cell `design05_pr24_pending`.

Recommended owner one-liner:

> Ratify PR-24 option 1: for design-05 G7 only, derive the load-bearing category
> mechanically from the frozen judge-free allocation CSR as `all_constraints_met` iff
> CSR = 1, otherwise `one_or_more_constraints_violated`; an unparseable allocation or
> uncomputable CSR remains unresolved under PR-18 E3; never substitute
> rationale_honesty, compare raw allocation vectors, change §B CSR, or make live calls.

## Exact no-call execution geometry audited

For the ratified A2 surface, two perturbation batteries contain 876 SUT cells. Applying
the existing registered per-design administration geometry yields 7,944 ordinary calls
(8,028 if every design-05 unit takes its registered retry), plus 73 paraphrase-author
calls. The maximum tie-breaker surface is 1,930 calls, for a worst-case **10,031-call**
envelope; Mistral's own-family surface can route at most 386 units to Part B.

As a scale reference only, the same 438 original item×model records in the existing W1
custody contain 4,027 calls and $9.93240109 actual cost; doubling that surface gives
$19.86480218 before paraphrase-author calls. This is not a budget, NTE, authorization,
or forecast of final spend. A separate immutable public-price/call/custody preflight and
Jimmy order are required after PR-23/24 and the exact role manifest are closed.

## Paper-facing progress and next triggers

This session narrowed W5 from five open mechanics to two owner decisions and delivered
the validated reducer/manifest/paraphrase/role-allocation scaffold. It does not license a
paper result or gate verdict. The next paper conversion trigger remains each completed
human-label wave → its frozen G4 branch → incremental PAPER §6/O5 fill. Independently,
PR-23/24 ratification unlocks the exact role artifact and documentation-only paid-run
preflight; a later, separately authorized and fully adjudicated G7 run would unlock W5
evidence.

Ancillary work was limited to the two decision records, exact no-call geometry, tests,
dashboard reconciliation, and this custody handoff because each directly protects the
next W5 command. No refactor, concurrency experiment, label work, or paper polish ran.

## Next session

Use dashboard §12. Require Jimmy's verbatim PR-23 and PR-24 one-liners. If both are
present, record them, build and validate the exact checked-in 73-item all-model-visible
role/exclusion manifest, implement the design-05 CSR category under TDD, and write the
exact paid-run preflight. Do not source credentials or make any live call; paid execution
requires another explicit order.

On session open: load the BibleBench paper-first surfaces read-only, then
`00-PORTFOLIO/project-dashboard.html` (Live status + §12 first), this handoff, the PR-18
ruling, both decision memos, and `PENDING-RULINGS.md`.

On session close: update `00-PORTFOLIO/project-dashboard.html` per local `AGENTS.md`,
write a NEW dated handoff, and commit/push WALKWORTHY paths only with explicit pathspecs.
