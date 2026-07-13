# BibleBench No-Spend MVP Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Compile and synthetically exercise the PF-002 three-model, 288-call MVP without credentials, network access, or spend.

**Architecture:** A closed manifest schema feeds a deterministic compiler that reads the frozen 48-episode banks and emits immutable provider-neutral request records. Pure offline adapter functions shape payloads, while a synthetic provider exercises terminal states and custody. No live transport library or credential lookup exists in this lane.

**Tech Stack:** Python 3.11+, JSON Schema, pytest, standard library, PyYAML.

---

### Task 1: Define the manifest and artifact contracts

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/mvp-manifest.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/mvp-artifact.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/fixtures/mvp-manifest-synthetic.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_mvp_runner.py`

- [ ] **Step 1: Write failing schema tests**

Require exactly three actor records; exact provider/model aliases; pricing evidence date; input/output token caps and prices; temperature/seed/max-output parameters; no fallback; retry count 0 or 1; forecast at or below $3; hard cap exactly $5; `authorization_state: SYNTHETIC_ONLY|PROPOSAL_ONLY|AUTHORIZED`; hashes; and expiry for non-synthetic manifests.

- [ ] **Step 2: Add synthetic safety tests**

Synthetic fixture actors must begin `synthetic-`, use zero prices, set `authorized: false`, and contain no endpoint, API-key environment variable, or transport setting.

- [ ] **Step 3: Run and verify failure**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py -q`

Expected: FAIL because schemas and runner do not exist.

- [ ] **Step 4: Implement the schemas and fixture**

Close every object with `additionalProperties: false`; enumerate terminal outcomes `success`, `refusal`, `malformed`, `truncated`, `rate_limited`, `unknown_delivery`, and `retry_exhausted`.

### Task 2: Compile exactly 288 logical calls

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/mvp_runner.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_mvp_runner.py`

- [ ] **Step 1: Add geometry and identity tests**

```python
calls = compile_mvp_calls(package_root, manifest)
assert len(calls) == 288
assert sum(c["call_kind"] == "primary" for c in calls) == 144
assert sum(c["call_kind"] == "probe" for c in calls) == 144
assert {c["surface"] for c in calls} == {"C1"}
assert len({c["logical_call_id"] for c in calls}) == 288
```

Also bind bank hash, episode hash, C1 surface hash, actor identity, request hash, and primary/probe pair ID.

- [ ] **Step 2: Implement deterministic compilation**

Sort by module, episode ID, actor ID, then primary before probe. Use canonical UTF-8 JSON with sorted keys and SHA-256. Read C1 primary and matched probe only; do not compile C0, C2, or capability twins.

- [ ] **Step 3: Implement fail-closed budget forecast**

Calculate worst-case input/output cost from registered maximum tokens and reject forecast over $3, cap other than $5, fallback enabled, missing hash, or unauthorized real execution state.

- [ ] **Step 4: Run focused tests**

Run the Task 1 command. Expected: geometry and budget tests PASS.

### Task 3: Add pure adapters and synthetic execution

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/mvp_adapters.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/synthetic_provider.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_mvp_runner.py`

- [ ] **Step 1: Add adapter shape tests**

Test three generic provider-family payload shapes using synthetic aliases only. Functions accept a provider-neutral request and return a dict; they perform no I/O and import no HTTP, socket, SDK, keyring, or environment-secret module.

- [ ] **Step 2: Implement pure adapters**

Map system/user messages, maximum output, temperature, and optional seed. Reject unsupported parameters instead of silently dropping them.

- [ ] **Step 3: Implement deterministic synthetic outcomes**

Derive outcomes from logical-call hashes so the fixture covers success, refusal, malformed output, truncation, rate limit, unknown delivery, and retry exhaustion. Unknown delivery is terminal and never replayed. Permit at most one manifest-registered retry for an explicitly retryable rate-limit result.

- [ ] **Step 4: Test network absence and terminal behavior**

Patch `socket.socket` to raise, clear proxy/key environment variables, run all 288 calls, and assert success without a socket attempt. Verify terminal missingness and no fallback.

### Task 4: Generate synthetic custody artifacts

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tools/run_synthetic_mvp.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/synthetic-mvp/README.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_mvp_runner.py`

- [ ] **Step 1: Write artifact tests**

Require manifest, compiled calls, requests, responses, usage, receipts, terminal-missingness ledger, and summary. Every file and every record must contain `evidence_status: SYNTHETIC_VALIDATION_ONLY`; hashes must form an immutable chain.

- [ ] **Step 2: Implement the CLI**

Accept only the bundled synthetic fixture. Refuse real-looking identities, nonzero prices, `authorized: true`, or an output directory containing non-synthetic artifacts.

- [ ] **Step 3: Run twice and verify byte reproducibility**

Run the CLI into two temporary directories and compare recursive SHA-256 manifests. Expected: identical.

- [ ] **Step 4: Run focused and integrated tests**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_mvp_runner.py tests/test_schedule.py tests/test_custody.py -q`

Expected: PASS with zero credential or network access.

- [ ] **Step 5: Commit the lane**

Run `git log -1 --oneline`, path-stage only runner files, schemas, synthetic fixture/output, and tests, then commit with `BibleBench: add synthetic PF-002 runner`.
