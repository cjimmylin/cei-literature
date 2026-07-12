# BibleBench Four-Module Pilot Master Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a fail-closed 42-core pilot that preserves FruitBench, CORINTHLOVE, 10CBench, and SermonMount while sharing one sandbox, provider, adjudication, scoring, and reporting engine.

**Architecture:** A new isolated `BIBLEBENCH-PILOT/` Python package owns shared contracts, evidence custody, scheduling, and execution. Passage modules remain adapter-driven, keep native scorers and exact source provenance, and never edit their source design briefs. A shared episode produces one reusable evidence bundle whose frozen observable events may be assessed by several registered lenses. Implementation is split into five independently testable plans executed in dependency order.

**Tech Stack:** Python 3.11+, dataclasses, JSON/YAML, PyYAML, jsonschema, pytest, Python standard-library HTTP, OpenRouter APIs, Markdown/JSON reports.

---

## Governing documents

- Design: `output/docs/superpowers/specs/2026-07-11-biblebench-shared-engine-design.md`
- Selection: `output/docs/superpowers/specs/2026-07-11-biblebench-42-core-selection.md`
- File safety: `../../_OPERATING-SYSTEM/Standards/file-safety.md`
- API safety: `../../_OPERATING-SYSTEM/Standards/api-integration.md`

## Consolidation precedents

The implementation must preserve the reusable findings in these committed or
parked lanes without reviving their superseded execution programs:

- FruitBench shared-episode design:
  `/Users/jimmy.lin/.config/superpowers/worktrees/CEI-Lit-WS/fruitbench-ten-design-evidence-ladder/docs/superpowers/specs/2026-07-11-fruitbench-consolidated-shared-episode-design.md`
- SermonMount consolidation handoff and D-015:
  `/Users/jimmy.lin/.config/superpowers/worktrees/CEI-Lit-WS/sermonmount-openrouter-live-20260710/COOKBOOK/40-BIBLEBENCH/20260711-CONSOLIDATED-BENCHMARK-HANDOFF.md`
- 10CBench consolidation handoff:
  `/Users/jimmy.lin/.config/superpowers/worktrees/CEI-Lit-WS/skim-p1-bank/COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS-REVIEWS/20260711-CONSOLIDATED-BENCHMARK-HANDOFF.md`
- CORINTHLOVE approved consolidated design and offline Tier-0 plan:
  `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/20260711d-corinthlove-consolidated-benchmark-design.md`
  and `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/20260711e-corinthlove-consolidated-core-implementation-plan.md`

These precedents require shared evidence rather than duplicate actor schedules,
benchmark-native scoring adapters, vector-first reporting, exact-byte custody,
fixture/live authority separation, manifest-last publication, and fail-closed
terminal states. Legacy frozen artifacts are referenced by hash and adapter;
they are not copied, mutated, or silently promoted.

The approved CORINTHLOVE Tier-0 plan is an upstream dependency, not duplicated
inside `BIBLEBENCH-PILOT`. Its DIMGLASS, CHARITROC, and CROSSROADS adapters are
read-only; native C1-C16 and crosswalk-mapped evidence remain separate. The
four-model cheap screen cannot support registered LoveBench L1/L2 concordance.

## Worktree and repository safety

Implementation should occur in a dedicated worktree because the current shared
workspace contains unrelated user work.

- Never delete files; move obsolete artifacts through the vault recycle/archive
  workflow.
- Never use `git add -A`.
- Before every commit, run `git log -1 --oneline` and stage only paths named in
  the active task.
- Never read, print, or persist secret values. Source
  `~/.codex/secrets/openrouter.env` only in the live operator shell.
- Synthetic output must use the exact label
  `harness validation, NOT a measurement`.

## Target tree

```text
BIBLEBENCH-PILOT/
├── pyproject.toml
├── README.md
├── config/
│   ├── cheap-panel.example.yaml
│   ├── panels.yaml
│   ├── adjudication.yaml
│   └── qualification-gates.yaml
├── status/
│   ├── authority.example.json
│   └── freeze.example.json
├── fixtures/
│   ├── nonbank-smoke.yaml
│   └── modules/
├── modules/
│   ├── fruitbench/{module,cores,episodes}.yaml
│   ├── corinthlove/{module,cores,episodes}.yaml
│   ├── tencommandments/{module,cores,episodes}.yaml
│   └── sermonmount/{module,cores,episodes}.yaml
├── schemas/
│   ├── module.schema.json
│   ├── core.schema.json
│   ├── episode.schema.json
│   ├── gold.schema.json
│   ├── ballot.schema.json
│   ├── run.schema.json
│   ├── authority.schema.json
│   ├── event.schema.json
│   ├── lens.schema.json
│   └── report.schema.json
├── src/biblebench_pilot/
│   ├── contracts.py
│   ├── registry.py
│   ├── transforms.py
│   ├── schedule.py
│   ├── sandbox.py
│   ├── artifacts.py
│   ├── events.py
│   ├── lenses.py
│   ├── module_adapters.py
│   ├── journal.py
│   ├── replay.py
│   ├── adjudication.py
│   ├── scoring.py
│   ├── native_scoring.py
│   ├── diagnostics.py
│   ├── qualification.py
│   ├── reporting.py
│   ├── runner.py
│   ├── cli.py
│   └── provider/
│       ├── transport.py
│       ├── openrouter.py
│       ├── catalog.py
│       └── budget.py
└── tests/
    ├── fixtures/
    ├── test_contracts.py
    ├── test_registry.py
    ├── test_transforms.py
    ├── test_schedule.py
    ├── test_sandbox.py
    ├── test_events.py
    ├── test_lenses.py
    ├── test_module_packs.py
    ├── test_provider.py
    ├── test_runner.py
    ├── test_journal.py
    ├── test_replay.py
    ├── test_scoring.py
    ├── test_qualification.py
    └── test_reporting.py
```

## Plan dependency order

### Plan 1: Shared engine foundation

File: `output/docs/superpowers/plans/2026-07-11-biblebench-shared-engine-plan.md`

Produces canonical contracts, schema validation, core loading, transformations,
shared-episode scheduling, the deterministic sandbox, lossless observable-event
records, lens routing, and append-only artifact writing.

### Plan 2: Passage module packs

File: `output/docs/superpowers/plans/2026-07-11-biblebench-module-packs-plan.md`

Produces the exact 12/8/12/10 core manifests, a balanced target/null/restraint
development pack for each module, adapter inventories, source-provenance
validation, and the owner provisional-gold workbench.

### Plan 3: Provider and runner

File: `output/docs/superpowers/plans/2026-07-11-biblebench-provider-runner-plan.md`

Produces catalog preflight, exact-identity OpenRouter execution, budget
enforcement, hash-chained journals, externally sealed dispatch fences,
crash-safe replay, durable run artifacts, and live CLI guards.

### Plan 4: Scoring and reporting

File: `output/docs/superpowers/plans/2026-07-11-biblebench-scoring-reporting-plan.md`

Produces 0-4 ballots over frozen opaque event references, native module
estimands, lens disagreement, red-line qualification, weighted repeat
agreement, gated geometric pillar/composite scoring, uncertainty, and
JSON/Markdown vector reports.

### Plan 5: Qualification workflow

File: `output/docs/superpowers/plans/2026-07-11-biblebench-qualification-plan.md`

Produces the non-bank smoke, four-cheap-model roster selection, USD 25 cap,
promotion gates, single revision ledger, bank freeze, and end-to-end dry run.

## Master completion gates

- [ ] All five sub-plans have passing focused tests.
- [ ] `pytest BIBLEBENCH-PILOT/tests -q` passes in a fresh process.
- [ ] Registry reports exactly `F=12, L=8, T=12, S=10`.
- [ ] Each module development pack proves target/null/restraint balance and the
  exact registered C0/C1/C2 geometry; C3 is absent from development artifacts.
- [ ] Forecast, primary response, matched probe, observable events, and all
  applicable lens ballots are linked as one reusable evidence bundle.
- [ ] Every source path resolves and every private field is absent from actor
  payloads.
- [ ] Capability twins and two-sided failure poles are validated before episode
  export.
- [ ] Red-line failures cannot receive `Qualified`.
- [ ] Composite recomputation from public dimension scores is exact.
- [ ] Cheap qualification reports vectors and diagnostic status only; a
  composite or rank remains latched off until human calibration and all
  composite-readiness gates pass.
- [ ] Every request is bound to exact dispatched bytes, exact route identity,
  zero hidden retries, one logical call, and separately counted physical
  attempts.
- [ ] Every interrupted run ends with either a complete manifest or an INVALID
  restricted-partial terminal manifest; no ambiguous run remains resumable.
- [ ] Mock runs are labeled `harness validation, NOT a measurement`.
- [ ] No live bank call occurs until owner gold, offline gates, catalog preflight,
  budget, and non-bank smoke all pass.

## Execution checkpoints

- [ ] Complete Plan 1 and review the shared interfaces before authoring modules.
- [ ] Execute the separately approved CORINTHLOVE offline Tier-0 plan before
  wiring its read-only adapter; do not add live calls or mutate source banks.
- [ ] Complete Plan 2 and obtain owner approval of provisional gold before any
  bank execution.
- [ ] Complete Plans 3 and 4 against fake transports and synthetic fixtures.
- [ ] Complete Plan 5 through non-bank smoke before authorizing qualification
  spend.
- [ ] Stop after the cheap-model qualification report and request the owner's
  promotion ruling; frontier execution is a separate authorization.
