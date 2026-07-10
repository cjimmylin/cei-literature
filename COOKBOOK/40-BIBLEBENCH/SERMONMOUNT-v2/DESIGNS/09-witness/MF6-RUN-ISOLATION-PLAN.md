# MF-6 Binding Run Isolation Implementation Plan

> **For agentic workers:** Execute this plan inline with strict RED→GREEN tests. Do not
> commit, stage, delete, or write a pilot run while implementing it.

**Goal:** Make the preregistered modality order and fresh-session boundary executable,
deterministic, auditable, and safe for explicitly named new runs.

**Architecture:** Keep the change inside `harness/run_p1.py`: a frozen `RunConfig` validates
the required run identity; a pure canonical planner groups all 300 items by core/modality,
sorts skins/items, and binds `_perm(core_id)` to execution. An injectable actual-order seam
must equal the canonical order. A sibling claim reserves publication before item/provider
work; every provider call gets a distinct retained one-call client, while rows stream into a
private verified staging directory. After coverage, order, session, and completion assertions
pass, all four staged files are validated and the claim/staging directory is atomically
renamed into place with the platform's exclusive no-replace primitive (`renamex_np` on
Darwin, `renameat2` on Linux), failing closed elsewhere. Failed claims are renamed to unique
`.failed-*` evidence directories;
the runner contains no unlink, rmdir, or recursive-delete path.
The publication fault seam runs before the final exact-payload validation, followed by an
immediate device/inode ownership recheck and the exclusive rename. This is a cooperative
same-host boundary: the final name cannot be replaced, but a hostile same-UID process could
still swap the source path in the syscall interval after the ownership check; defending that
stronger threat requires an authenticated descriptor-based publication design.
`model_client.py` accepts the stable session ID and declares provider family/evidence without
changing response distributions. LIVE evidence additionally fails closed on model/family/
repeat minimums, mixed evidence, and the absence of an explicitly authorized non-mock judge.
The frozen `scoring/judge.py` remains untouched; its separate discarded-`per_item` tie issue
is recorded as an out-of-scope follow-up rather than silently altered in MF-6.

**Files:**

- Modify `DESIGNS/09-witness/harness/run_p1.py`
- Minimally modify `DESIGNS/09-witness/harness/model_client.py`
- Create `DESIGNS/09-witness/tests/test_mf6_run_isolation.py`
- Modify `DESIGNS/09-witness/README.md`

## Task 1: Configuration, planning, and session identity

- [ ] Add failing tests for date/run-ID/output-path validation and stable unique session IDs.
- [ ] Add failing tests proving a shuffled item input yields the identical canonical plan,
  including all 300 items and 60 controls.
- [ ] Implement `RunConfig`, stable session IDs, and the pure core/modality planner.
- [ ] Run the focused tests until green.

## Task 2: Binding execution and fail-closed order

- [ ] Add failing tests whose recording client observes exact `_perm` order for every core.
- [ ] Add a stateful-provider test proving every session gets a distinct one-call instance.
- [ ] Add a forced-swap fault-seam test that raises before producing any output.
- [ ] Execute core groups in canonical order and assert expected versus actual modality order
  before provider calls or writes.
- [ ] Run the focused tests until green.

## Task 3: Audit, manifest, exclusive persistence, and CLI

- [ ] Add failing tests for early existing-directory refusal, audit/manifest schemas,
  exact 30×8 moral/15×4 control structure, item/session coverage, `SIMULATED` marking,
  early staged-write/race failure, and atomic no-clobber publication.
- [ ] Add LIVE fail-closed tests for mixed evidence, model/family/repeat minimums, and the
  explicitly authorized real-judge requirement.
- [ ] Add required CLI arguments for date, run ID, output directory, models, and repeats.
- [ ] Persist `run_manifest.json`, `scored.jsonl`, `audit_log.jsonl`, and `qc.json` only with
  exclusive creation after all assertions complete.
- [ ] Run focused CLI and runner integration tests until green.

## Task 4: Documentation and verification

- [ ] Update README commands with explicit runner parameters and matching downstream
  `--run-dir`/`--date` parameters; do not execute those commands against a canonical pilot.
- [ ] Run MF6 tests, the full WITNESS test set, canonical parity/audits, and frozen hashes.
- [ ] Report any unrelated concurrent failures separately.
