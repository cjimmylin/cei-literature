# MF-1 Complexity-Matched Controls Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use test-driven development for every
> behavior slice. The binding work order forbids commits, staging, deletes, and edits to
> dated run artifacts, so this plan intentionally has verification checkpoints instead of
> commit checkpoints.

**Goal:** Replace the asserted format-control match with an inspectable, deterministic,
hard-gated 15-base battery matched to all 30 moral cores, and enforce exact ACT contracts.

**Architecture:** A shared pure complexity module parses tool declarations and derives
moral profiles, balanced bands, and deterministic pairs. A separate authored branch module
injects explicit branch metadata into every moral core. `itembank/control_battery.py` builds
five objective logistics families per band from those profiles, validates before any write,
and renders structured control actions; `format_control.py` is the canonical thin façade.
The sandbox, classifier, mock model, renderer, and P1 harness consume the same declarations
and metadata.

**Tech Stack:** Python 3.9 standard library, JSONL artifacts, pytest.

---

### Task 1: Lock the behavior in failing tests

**Files:**
- Create: `tests/test_mf1_controls.py`
- Modify: `tests/test_witness.py`

- [x] Add tests for strict zero/one/two-arity declarations, malformed syntax, duplicate
  tool names, and duplicate argument names.
- [x] Add explicit mean-bound tests: mean 50 admits 40/60 and rejects 39/61; the current
  bank admits 43/63 and rejects 42/64.
- [x] Add tests for authored branches on all 30 cores, exact poles/tools/party strings,
  stable 10/10/10 length terciles and difficulty bands under shuffled input, deterministic
  15 clusters, and each moral represented exactly once.
- [x] Add tests for 15 bases/60 rows, 15 rows per modality, five families per band, exact
  recomputed anchor metadata, the three documented one-tool floor IDs only, REC uniqueness,
  no unused tools, at least two action tools, rotated gold positions, and generic ACT prompts.
- [x] Add sandbox pre-mutation rejection tests and structured classifier mutation/forgery
  tests; add exhaustive moral/control mock ACT contract tests.
- [x] Add CLI safety tests for `--check`, invalid and existing `--write-new` targets, exact
  in-memory artifact parity, all-15 P1 loading, and scored-row metadata propagation.
- [x] Run the focused tests and record the expected missing-API/schema failures (RED).

### Task 2: Shared declaration and complexity primitives

**Files:**
- Create: `complexity.py`
- Create: `itembank/decision_branches.py`
- Modify: `witness_common.py`
- Modify: `itembank/seed_cores.py`
- Modify: `itembank/cores_batch_A.py`
- Modify: `itembank/cores_batch_B.py`
- Modify: `itembank/cores_batch_C.py`

- [x] Implement `parse_tool_declaration`, `parse_tool_declarations`, split-word counting,
  inclusive mean bounds, explicit branch validation, stable length terciles, raw difficulty,
  balanced difficulty bands, profile IDs, and deterministic within-band pairing.
- [x] Author literal `decision_branches` for all 30 cores and attach copied `act_spec`
  dictionaries in each source generator.
- [x] Extend `validate_core` to fail on malformed declarations or branches and undeclared
  primary/signature tools without weakening existing MF-3 validation.
- [x] Run focused parser/branch/profile tests to GREEN and re-run the existing suite.

### Task 3: Rebuild and hard-gate format controls

**Files:**
- Create: `itembank/control_battery.py`
- Rewrite: `itembank/format_control.py`
- Modify: `harness/gen_output_fixtures.py`

- [x] Build exactly five objective logistics families in each difficulty band, one per
  2-core cluster, with target anchor word length clamped to the global inclusive bounds.
- [x] Generate neutral declaration names matching anchor tool count and sorted arities,
  adding a second tool only for a documented one-tool anchor; rotate declaration order.
- [x] Author exact structured `pole_actions`, natural GEN rubrics/fixtures, four unique REC
  options, exact party and branch counts, and private recomputable match metadata.
- [x] Implement a pure validator returning every error plus mean/bounds/count/band/modality/
  floor report; validate sources, in-memory rows, leakage, and action contracts.
- [x] Implement default `--check` canonical comparison and exclusive safe
  `--write-new PATH`; refuse invalid batteries and existing targets before any write.
- [x] Run format-control focused tests to GREEN.

### Task 4: Enforce ACT contracts end to end

**Files:**
- Modify: `harness/act_sandbox.py`
- Modify: `scoring/action_classifier.py`
- Modify: `harness/model_client.py`

- [x] Add a typed tool-contract error and validate declared tool, dict arguments, and exact
  argument keys before step, transcript, state, or canary mutation; remove noop fallback.
- [x] Match controls only against complete structured pole actions, resolving zero or
  multiple matches to neutral and ignoring forged bodies.
- [x] For morals, classify tool plus canonical JSON of every argument. Select a declared
  signal-mentioned tool per mock pole, fall back only to a declared primary, and populate
  exactly declared arguments. Deep-copy control actions.
- [x] Run all sandbox/classifier/mock-action tests to GREEN.

### Task 5: Propagate profiles through render and harness

**Files:**
- Modify: `itembank/render.py`
- Modify: `harness/run_p1.py`

- [x] Compute moral profiles once per bank generation and put only `difficulty_band` and
  `complexity_profile_id` on public rows; keep full match detail in private metadata.
- [x] Put the same public fields on controls and propagate them into scored-row base data.
- [x] Ensure P1 loads all 15 bases and remove every stale first-five statement or slice.
- [x] Run rendering/harness metadata tests to GREEN.

### Task 6: Regenerate canonical artifacts safely

**Files:**
- Regenerate: `itembank/seed_cores.jsonl`
- Regenerate: `itembank/cores_batch_A.jsonl`
- Regenerate: `itembank/cores_batch_B.jsonl`
- Regenerate: `itembank/cores_batch_C.jsonl`
- Regenerate: `itembank/cores.jsonl`
- Regenerate: `itembank/renderings.jsonl`
- Regenerate: `itembank/format_control.jsonl`
- Regenerate: `SHARED/core-ledger.jsonl`

- [x] Run all four source generators, bank build, moral render, and validated safe control
  regeneration only after their in-memory gates pass.
- [x] Assert source/core/ledger/render/control byte parity and zero model-facing leakage.

### Task 7: Final verification and freeze checks

- [x] Run focused MF-1 tests, the full WITNESS suite, and `format_control.py --check`.
- [x] Run all read-only audits, artifact parity, scoped `git diff --check`, and scope grep.
- [x] Reconfirm `scoring/judge.py` SHA-256 is
  `366d8bdd7e4ec0eb444d426908ee5b6221d14b181b4341556d22f5062f056420`.
- [x] Reconfirm all eight 20260706 artifact hashes are unchanged and report any scientific
  ambiguity instead of weakening a gate.
