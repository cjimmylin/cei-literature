# Runner Quality P1 Repairs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the four audited PF-002 runner P1 gaps without adding live transport, credentials, calls, or spend.

**Architecture:** Keep the runner offline and fail-closed. Approved execution requires an external owner-record file whose exact SHA-256 comes from the trusted launch context; that record binds the proposal, authorization, run ID, and nonce, and successful validation atomically consumes the identity in a caller-supplied durable state directory. Strict JSON loading, a closed route registry, and full synthetic-manifest validation protect the remaining boundaries.

**Tech Stack:** Python 3, `jsonschema`, canonical SHA-256 contracts, `pytest`.

---

### Task 1: Strict JSON and exact route coherence

**Files:**
- Modify: `src/biblebench_pilot/mvp_runner.py`
- Test: `tests/test_mvp_runner.py`

- [x] **Step 1: Write failing adversarial tests**

Add tests that load duplicate top-level and nested members through the manifest, proposal, authorization, and owner-record loaders, and mutate each actor's provider/model/route combination while resealing the proposal.

- [x] **Step 2: Run the focused tests and confirm RED**

Run: `PYTHONPATH=src /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py -k 'duplicate or route_coherence' -vv`

Expected: failure because duplicate members use last-key-wins and cross-field route mismatches are accepted.

- [x] **Step 3: Implement strict loading and the closed roster**

Use `json.loads(..., object_pairs_hook=...)` to reject a repeated key at every nesting level. Add `load_proposal`, `load_authorization`, and `load_owner_record`. Validate the exact actor aliases and their OpenAI/GPT/responses, Google/Gemini/content, and Anthropic/Claude/messages route records.

- [x] **Step 4: Re-run focused tests and confirm GREEN**

Run the command from Step 2; expect all selected tests to pass.

### Task 2: Trust-root authorization and replay consumption

**Files:**
- Create: `schemas/mvp-owner-record.schema.json`
- Modify: `schemas/mvp-authorization.schema.json`
- Modify: `tests/fixtures/mvp-authorization-unauthorized.json`
- Modify: `src/biblebench_pilot/mvp_runner.py`
- Test: `tests/test_mvp_runner.py`

- [x] **Step 1: Write failing authorization tests**

Add helpers that construct an approved test-only authorization and owner record in `tmp_path`. Test missing trust anchor, wrong owner-record hash, changed binding fields, missing/unwritable state, successful first consumption, and rejected replay. Assert committed authorization remains `NOT_AUTHORIZED` and contains no credential material.

- [x] **Step 2: Run the focused tests and confirm RED**

Run: `PYTHONPATH=src /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py -k 'authorization or replay or trust' -vv`

Expected: failures because no trust root or consumption state exists.

- [x] **Step 3: Implement the minimal fail-closed gate**

Extend authorization with nullable `run_id`, `authorization_nonce`, and `owner_record_id` fields that must be concrete for `APPROVED`. Validate a closed owner-record schema, compare its raw file digest with the independently supplied expected digest, bind every execution field, then create a mode-0600 consumption receipt with `O_CREAT|O_EXCL` and `fsync` before returning.

- [x] **Step 4: Re-run focused tests and confirm GREEN**

Run the command from Step 2; expect all selected tests to pass and replay to fail.

### Task 3: Synthetic tree semantic verification

**Files:**
- Modify: `src/biblebench_pilot/mvp_runner.py`
- Test: `tests/test_mvp_runner.py`

- [x] **Step 1: Write failing tamper tests**

Copy a valid synthetic run tree, change `authorized` to true or a model price to nonzero, reseal the manifest and downstream first-link hash, and assert `verify_run_tree` rejects it.

- [x] **Step 2: Run the focused tests and confirm RED**

Run: `PYTHONPATH=src /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py -k 'semantic_tamper' -vv`

Expected: failure because the current verifier checks hashes but not manifest schema/semantics.

- [x] **Step 3: Reuse full manifest validation in the verifier**

Call `validate_manifest(manifest, bank_root=_ROOT)` before traversing artifacts, preserving the existing complete hash-chain checks.

- [x] **Step 4: Re-run focused tests and confirm GREEN**

Run the command from Step 2; expect all selected tests to pass.

### Task 4: Fixture resealing and full verification

**Files:**
- Modify: `tests/fixtures/mvp-proposal-real-unauthorized.json`
- Modify: `tests/fixtures/mvp-authorization-unauthorized.json`
- Test: `tests/test_mvp_runner.py`

- [x] **Step 1: Update bound hashes mechanically**

Recompute the runner compiler hash, proposal manifest hash, authorization-schema hash, and authorization self-hash after implementation. Preserve both committed manifests as non-authorizing surfaces.

- [x] **Step 2: Run focused runner verification**

Run: `PYTHONPATH=src /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py -vv`

Expected: all runner tests pass.

- [x] **Step 3: Run compile and no-network checks**

Run: `/opt/homebrew/bin/python3 -m py_compile src/biblebench_pilot/mvp_runner.py tests/test_mvp_runner.py`

Expected: exit 0. Confirm no transport libraries or credentials were added.
