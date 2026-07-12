<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — FR-16: W1 selection surface, non-tie-breakable routing, Part-B granularity

**Issued:** 2026-07-12, Fable ruling session (delegated adjudication window per
master-plan §1/O5; authority check passed — session ran on `claude-fable-5`).
**Status:** BINDING on the O5 execution. **Flagged for Jimmy ratification** (appended to
the PR-8 bundle pointer; see PENDING-RULINGS PR-9 RULED note).
**Resolves:** PR-9 item 2 (selector scope + 20 non-tie-breakable pendings) and the
Part-B export-granularity dependency recorded in
`20260711l-codex-pr9-decision-evidence.md` §3.
**Evidence base:** `20260711l-codex-pr9-decision-evidence.md` (twice-verified counts),
`20260711n-codex-pr9-decision-support-handoff.md`, frozen
`20260710-fable-gate-prereg-pilot-adjudication.md` §B/§E (interpreted, not rewritten).

---

## 1. Why this is interpretation, not amendment

The frozen §E defines the third-family tie-breaker's target as **"`needs_adjudication`
cells"** — cells, not records, and not a refusal-tag stratum. The frozen §B adjudication
rule likewise operates cell-wise: "agreement cells directly; disagreement cells via
tie-breaker/human; cells still unresolved are EXCLUDED with the exclusion count
published." The 609-record `refusal_tag == pending_adjudication` selector entered via the
transition-package W1 instruction (`20260711e`), which conflated the PR-3 refusal-tag
queue with the §B adjudication surface. That was an FR-scoping error, now corrected by
evidence: the selector captures only 1,767 of 3,172 unresolved cells, and which cells it
drops depends on the record's refusal tag — a selection-biased exclusion of exactly the
kind the validity review flagged (V-1/V-2 agreement-selection bias). FR-16 therefore
*restores* the frozen text; it does not alter it.

## 2. The ruling

**FR-16(a) — W1 selection surface = the full §B unresolved-cell surface.**
W1 adjudicates **every cell with `needs_adjudication == true` in the public O4 panel**:
3,172 cells across 1,297 records (Codex twice-verified, `jq` + `awk` agreeing), at FR-2
granularity — the disagreeing **turn** for 02/07, the disagreeing **seat** for 09, the
disagreeing pair/criterion-cell/item elsewhere per the §B S-unit. The 609-record
refusal-tag selector is retired as a surface definition. (The refusal-tag queue remains
what it always was: the PR-3 re-tag bookkeeping, not the adjudication surface.)

**FR-16(b) — Tie-breakability contract.**
A cell is tie-breakable **iff** `needs_adjudication == true` AND two distinct
frozen-pair judge verdicts exist for that cell and differ. The third-family judge is
never invoked on a cell with no judge disagreement — there is nothing to break, and a
third opinion on a non-disagreement would be an unregistered scoring path.

**FR-16(c) — Routing of the 20 non-tie-breakable pending records.**
- **11 × design-05 allocation-parse pendings:** the 05 primary is judge-free; these are
  mechanical extraction failures. One bounded, TDD, no-live-call re-parse pass is
  authorized under existing build authority (FIX-MECHANICS-ONLY; parser changes are
  regression-tested against already-parsed cells — zero tolerance for changing any
  previously parsed value). Cells still unparseable after that pass route to the
  cell-level Part-B export; if unlabeled they remain EXCLUDED with published counts per
  §B. Priority is low: FR-5 already removes 05 from this cycle's release set.
- **9 × design-09 arbiter-first pendings:** structural pendency with no judge
  disagreement — route **directly to the cell-level Part-B export** (human), never the
  third judge.

**FR-16(d) — Part-B export granularity = the unresolved cell.**
Protocol §6 defines Part B at the unresolved-**cell** level. The exporter
(`label_sample.export_part_b`) must be rebuilt TDD **cell-aware** before any W1 Part-B
export: one row per unresolved atomic cell (turn / seat / pair / criterion-cell / item
per the §B S-unit), with the parent-record context attached to each row for the human
reader. All human-workload accounting uses **cell counts** (e.g. Mistral own-family
exposure = 580 cells on this full surface), never record counts.

**FR-16(e) — Home-advantage exclusion carries over unchanged.**
Whatever tie-breaker model Jimmy's STOP-8 ruling yields, frozen §E's own-family
exclusion applies on this surface: own-family SUT cells fall to Part-B. Under the
Mistral fallback that is **225 records / 580 cells** (full surface) — the number Jimmy's
STOP-8 one-liner must accept or avoid via a logged §E replacement-model amendment.
G7 perturbed-cell disagreements route through this same path (FR-14, unchanged).

## 3. Dependency note (does not soften the ruling)

Turn-level adjudication of 02/07 on this surface requires complete turn transcripts.
The historical O4 artifacts lack 723 of 907 required 02/07 turn responses (PR-9 item 1),
so W1 on designs 02/07 remains blocked until Jimmy either authorizes the NEW immutable
six-SUT 02/07 re-execution (historical same-surface cost baseline **$26.681701**) or
supplies recovered transcripts. The other eight designs' unresolved cells are
adjudicable from existing artifacts once the tie-breaker model question (STOP-8) is
settled.

## 4. Consequences for FR-1 accounting

FR-1's ≤10% unresolved-S-unit precondition is computed **after** P1+P6 on this full
surface. Had W1 run on the 609-record selector, the 1,405 outside-selector cells would
have counted as unresolved exclusions anyway — most designs would have failed FR-1 and
the whole W1 spend would have needed a second pass. This ruling makes W1 single-pass.

## 5. Ratification line for Jimmy

*"FR-16 ratified: full 3,172-cell §B surface; no third judge on non-disagreement cells;
05-parse/09-arbiter routing as specified; cell-level Part-B."* — one line, logged in
PENDING-RULINGS, joins the PR-8 FR-bundle.

*No item text, key, gate rule, or threshold is changed by this ruling
(FIX-MECHANICS-ONLY preserved). HOLDOUT untouched. No live calls were made.*
