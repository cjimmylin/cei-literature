# PR-10 / PR-11 Unblocking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:executing-plans` and
> execute each checkbox in order. Work TDD; do not make live model calls.

**Goal:** Convert Jimmy's 2026-07-12 PR-10/PR-11 ratification into reproducible,
machine-readable W5 name rotation and a numeric design-09 G5 scoring specification.

**Architecture:** Keep both additions outside the frozen primary rubrics and frozen gate
text. PR-10 is a data file plus a pure deterministic selector/replacement module. PR-11
is a G5-only `ScoringSpec`; the existing `gate_neutrality` function continues to apply
the frozen `> 0.5` comparison. No production G5/G7 run occurs in this change.

**Tech stack:** Python 3, JSON, pytest, existing `walkworthy.rubrics` and
`walkworthy.gates` modules.

---

### Task 1: Persist the rulings and promotion

**Files:**
- Create: `00-PORTFOLIO/20260712-jimmy-PR10-PR11-ruling.md`
- Modify: `00-PORTFOLIO/PENDING-RULINGS.md`

- [x] Record Jimmy's exact ratification text, the deterministic PR-10 contract, the
  six-category PR-11 numeric contract, and the FR-18 promotion.
- [x] Mark PR-10 and PR-11 closed without changing historical ruling text.

### Task 2: Register the design-09 G5-only scoring specification (RED -> GREEN)

**Files:**
- Modify: `harness/tests/test_gates_and_schemas.py`
- Modify: `harness/walkworthy/rubrics.py`

- [x] Add a failing test requiring `g5_spec_for("09-doubleedge")` to expose exactly
  `wrong_naming`, `debt_obligation_accuracy`, `floor_compliance`,
  `attitudinal_heart_duty`, `reasoning_method_quality`, and `pastoral_concreteness`,
  each as ordinal `[0, 0.5, 1]` with explicit anchors.
- [x] Run the focused test and confirm it fails because the G5-only registry is absent.
- [x] Add `G5_RUBRICS` plus fail-closed `g5_spec_for`; leave `DESIGN_RUBRICS` unchanged.
- [x] Run the focused test and existing gate/schema tests to green.

### Task 3: Formalize deterministic L7 name rotation (RED -> GREEN)

**Files:**
- Create: `harness/tests/test_l7_names.py`
- Create: `harness/walkworthy/l7_name_inventory.json`
- Create: `harness/walkworthy/l7_names.py`

- [x] Add failing tests for inventory provenance, target-design exclusion, explicit
  apparent-gender matching, target-name exclusion, deterministic tuple selection,
  collision-free allocation, and title-preserving token replacement.
- [x] Run the focused tests and confirm they fail because the module is absent.
- [x] Add a public-design-sourced inventory and pure SHA-256 selector keyed by
  `(design, item_id, role_index)`; fail closed when no eligible unused name exists.
- [x] Add exact-token replacement that changes only supplied names, leaving titles and
  pronouns intact.
- [x] Run the focused tests to green.

### Task 4: Verify and close the session

**Files:**
- Modify: `00-PORTFOLIO/project-dashboard.html`
- Create: `00-PORTFOLIO/20260712-codex-pr10-pr11-unblocked-handoff.md`

- [x] Run the full harness suite from `harness/`.
- [x] Audit the diff for frozen-file, HOLDOUT, deletion, and scope violations.
- [x] Update dashboard live status, W4/W5 rows, ruling ledger, Jimmy-owed lane, last
  updated line, changelog, and next-session instructions.
- [x] Write a new dated handoff with verification evidence and no gate verdicts.
- [x] Re-run focused/full verification after documentation changes as appropriate.
- [x] Immediately before staging, run `git log -1` and `git diff --cached --name-only`;
  stage explicit WALKWORTHY pathspecs, commit, and fast-forward push only.
