# BibleBench Provider, Custody, and Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a fail-closed OpenRouter execution spine that binds exact wire bytes, route identity, budget authority, hash-chained custody, crash-safe continuation, and terminal evidence manifests without exposing secrets or duplicating paid calls.

**Architecture:** Logical calls are compiled before execution. A physical attempt is created only after conservative budget reservation and an externally sealed dispatch fence. The cheap pilot has zero provider retries: an attempted failed, malformed, truncated, refused, or delivery-unknown call becomes terminal evidence. A later process may resume unattempted logical calls, but never retries an attempted call. Hidden client retries are exactly zero. Final bundles publish manifest last and distinguish fixture, diagnostic, calibration, and measurement authority.

---

### Task 1: Define exact run, attempt, route, and authority contracts

**Files:**
- Create: `BIBLEBENCH-PILOT/schemas/run.schema.json`
- Create: `BIBLEBENCH-PILOT/schemas/authority.schema.json`
- Create: `BIBLEBENCH-PILOT/status/authority.example.json`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/runner.py`
- Create: `BIBLEBENCH-PILOT/tests/test_runner_contracts.py`

- [ ] **Step 1: Write failing lifecycle tests**

```python
from biblebench_pilot.runner import RunState, transition

def test_freeze_does_not_authorize_dispatch():
    frozen = RunState.frozen("manifest-hash")
    assert frozen.authorized is False

def test_terminal_attempt_cannot_be_retried():
    failed = transition(RunState.dispatched("L1", "P1"), "DELIVERY_UNKNOWN")
    assert failed.terminal is True
    assert failed.retry_permitted is False
```

- [ ] **Step 2: Verify failure**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_runner_contracts.py -q
```

- [ ] **Step 3: Implement a closed lifecycle**

States: `PLANNED`, `RESERVED`, `FENCE_SEALED`, `DISPATCH_STARTED`, `ACCEPTED`,
`REFUSED`, `MALFORMED`, `TRUNCATED`, `HTTP_FAILED`, `DELIVERY_UNKNOWN`,
`UNATTEMPTED`, and `INVALID_RESTRICTED_PARTIAL`. Allow only registered
transitions. Freeze, readiness, live-call authority, calibration, ranking,
publication, and scale authority are distinct booleans defaulting false.

- [ ] **Step 4: Define common execution fields**

Include study/module/episode/bundle/logical-call/physical-attempt/route IDs,
source/config/request hashes, requested and returned model/provider, seed,
terminal status, repair count, paid-call count, Decimal cost, evidence basis,
empirical eligibility, and official eligibility. Unknown fields fail closed.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_runner_contracts.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/schemas/run.schema.json BIBLEBENCH-PILOT/schemas/authority.schema.json BIBLEBENCH-PILOT/status/authority.example.json BIBLEBENCH-PILOT/src/biblebench_pilot/runner.py BIBLEBENCH-PILOT/tests/test_runner_contracts.py
git commit -m "BibleBench: define fail closed run lifecycle"
```

### Task 2: Implement exact-byte request rendering and fake transport

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/provider/transport.py`
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/provider/openrouter.py`
- Create: `BIBLEBENCH-PILOT/tests/test_provider.py`

- [ ] **Step 1: Write failing wire-binding tests**

```python
def test_audit_hash_is_over_exact_dispatched_bytes(fake_transport, request):
    receipt = fake_transport.send(request)
    assert receipt.request_sha256 == sha256(receipt.exact_wire_bytes).hexdigest()

def test_transport_has_zero_hidden_retries(openrouter_transport):
    assert openrouter_transport.max_retries == 0
```

- [ ] **Step 2: Implement deterministic rendering**

Serialize the validated request once, retain those exact bytes, audit every
registered/inline/tool schema inside those bytes, and dispatch the same byte
object. Never validate one object and regenerate another. Retain exact response
bytes, headers allowlist, usage, finish reason, and explicit transport absence.

- [ ] **Step 3: Implement a fake client first**

The fake client scripts success, refusal, malformed JSON, truncation, HTTP 429,
timeout-before-send, timeout-after-send, and unknown delivery. It records one
physical attempt per send and rejects a second send for the same logical call.

- [ ] **Step 4: Add safe normalization**

Accept strict schema output. Permit at most one local syntax-only repair when a
public semantic fingerprint is provably unchanged; repair never causes another
provider call. Preserve original and repaired bytes and keep repair count
visible. Semantic repair is forbidden.

- [ ] **Step 5: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_provider.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/provider/transport.py BIBLEBENCH-PILOT/src/biblebench_pilot/provider/openrouter.py BIBLEBENCH-PILOT/tests/test_provider.py
git commit -m "BibleBench: bind provider dispatch to exact bytes"
```

### Task 3: Freeze catalog, route aliases, privacy, and cheap-only policy

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/provider/catalog.py`
- Create: `BIBLEBENCH-PILOT/config/cheap-panel.example.yaml`
- Create: `BIBLEBENCH-PILOT/tests/test_catalog.py`

- [ ] **Step 1: Test route and returned-alias enforcement**

Require requested model, allowed returned aliases, pinned provider, input and
output prices, context limit, structured-output/tool support, ZDR/data-policy
flags, catalog timestamp, and catalog response hash. Reject an unlisted return
alias, provider drift, fallback, price increase, missing required parameter, or
stale catalog.

- [ ] **Step 2: Implement authenticated GET preflight**

At launch, source the owner-controlled environment in the operator shell only.
The program reads only the required key variable, never prints it, and sends an
authenticated catalog GET before any POST. Persist sanitized catalog evidence,
not headers or environment. Preflight does not authorize inference.

- [ ] **Step 3: Bind cheap-only to every inference role**

Actor, selector, probe, classifier, and future judge roles must stay under the
frozen numeric ceiling. Premium and cost-increasing fallbacks are forbidden.
The current pilot uses deterministic probes and the owner human judge, but the
all-role invariant remains tested.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_catalog.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/provider/catalog.py BIBLEBENCH-PILOT/config/cheap-panel.example.yaml BIBLEBENCH-PILOT/tests/test_catalog.py
git commit -m "BibleBench: enforce pinned cheap routes"
```

### Task 4: Enforce Decimal budget and exact call accounting

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/provider/budget.py`
- Create: `BIBLEBENCH-PILOT/tests/test_budget.py`

- [ ] **Step 1: Write failing reservation tests**

```python
from decimal import Decimal

def test_unknown_delivery_keeps_full_reservation(ledger):
    ledger.reserve("P1", Decimal("0.010000"))
    ledger.close_unknown("P1")
    assert ledger.reserved_usd == Decimal("0.010000")
    assert ledger.refundable_usd == Decimal("0")
```

- [ ] **Step 2: Implement conservative accounting**

Track registered logical calls, successful, failed, unattempted, reserved,
physical attempts, paid-call equivalents, completed, abandoned, and totals per
principal/model/route/module. Reserve worst-case input+output cost before the
physical attempt; unknown delivery receives no refund. Use `Decimal` only.

- [ ] **Step 3: Enforce hard-stop behavior**

Reject dispatch if the next reservation exceeds the exact authority cap or if
catalog prices, token ceilings, route identity, or existing custody are
uncertain. Prove the planned worst-case battery is at most USD 25 before owner
authority can be minted.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_budget.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/provider/budget.py BIBLEBENCH-PILOT/tests/test_budget.py
git commit -m "BibleBench: add conservative spend custody"
```

### Task 5: Add hash-chained journals and external dispatch fences

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/journal.py`
- Create: `BIBLEBENCH-PILOT/tests/test_journal.py`

- [ ] **Step 1: Test tamper and crash boundaries**

Simulate crashes before/after reservation, journal append, fence seal, socket
send, response receipt, evidence commit, and terminal closure. Assert rollback
can never restore retry permission and one unknown delivery can never authorize
another child attempt.

- [ ] **Step 2: Implement append-only hash chaining**

Each canonical entry binds prior hash, sequence, event, logical/physical IDs,
timestamp, and payload hash. Before send, append `DISPATCH_STARTED`, capture the
exact fence hash, and no-replace seal it outside the evidence store. Local
journal state alone cannot prove no prior paid call.

- [ ] **Step 3: Implement continuation, not retry**

A restarted process verifies journal, external fence, budget, source, and
manifest state. It may continue only logical calls proven `UNATTEMPTED`. Any
attempted non-success is terminal. This implements zero retries while allowing
one or more safe process restarts over remaining schedule rows.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_journal.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/journal.py BIBLEBENCH-PILOT/tests/test_journal.py
git commit -m "BibleBench: add sealed dispatch custody"
```

### Task 6: Publish manifest-last bundles and deterministic replay

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/replay.py`
- Create: `BIBLEBENCH-PILOT/tests/test_replay.py`

- [ ] **Step 1: Test complete and restricted-partial closure**

Successful runs close every logical call and publish a complete manifest last.
Hidden, ambiguous, nonretryable, or integrity failures publish retained
evidence plus an `INVALID_RESTRICTED_PARTIAL`, `complete:false` terminal
manifest. No unmanifested directory is reportable.

- [ ] **Step 2: Implement whole-root verification**

Verify exact file roster, no symlinks/aliases/hardlinks, current source/runtime
hashes, journal chain, external fences, request/response/evidence links,
logical/physical accounting, budget totals, and manifest-last transaction.
Extra, missing, changed, or unreferenced artifacts invalidate the root.

- [ ] **Step 3: Implement replay**

Rebuild requests, event records, lens packets, and native mechanical outcomes
from frozen source snapshots and retained exact bytes. Replay performs no
network access, secret read, or semantic regeneration.

- [ ] **Step 4: Run and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_replay.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/replay.py BIBLEBENCH-PILOT/tests/test_replay.py
git commit -m "BibleBench: add terminal bundle replay"
```

### Task 7: Add guarded CLI and end-to-end fake execution

**Files:**
- Create: `BIBLEBENCH-PILOT/src/biblebench_pilot/cli.py`
- Create: `BIBLEBENCH-PILOT/tests/test_runner.py`

- [ ] **Step 1: Implement offline commands first**

Commands: `inventory`, `compile`, `preflight-offline`, `run-fixture`, `verify`,
and `replay`. The live command requires a separately sealed authority receipt
binding exact source/schedule/catalog/route/budget hashes and expiry. A freeze
receipt alone fails.

- [ ] **Step 2: Run all failure modes through fake transport**

Exercise success, refusal, malformed, truncation, 429, unknown delivery,
interrupted process, tampered fence, source drift, provider drift, overspend,
and private-field leakage. Assert exact terminal status, no duplicate send, and
complete accounting.

- [ ] **Step 3: Verify import and secret safety**

Importing any package module must perform no network, environment enumeration,
filesystem write, credential read, or destructive operation. Error translation
redacts filesystem and header values. Scan exact wire bytes for private gold,
canaries outside registered leaves, judge identity, and secret-shaped strings.

- [ ] **Step 4: Run the provider/runner suite and commit**

```bash
python3 -m pytest BIBLEBENCH-PILOT/tests/test_runner_contracts.py BIBLEBENCH-PILOT/tests/test_provider.py BIBLEBENCH-PILOT/tests/test_catalog.py BIBLEBENCH-PILOT/tests/test_budget.py BIBLEBENCH-PILOT/tests/test_journal.py BIBLEBENCH-PILOT/tests/test_replay.py BIBLEBENCH-PILOT/tests/test_runner.py -q
git log -1 --oneline
git add BIBLEBENCH-PILOT/src/biblebench_pilot/cli.py BIBLEBENCH-PILOT/tests/test_runner.py
git commit -m "BibleBench: complete guarded execution spine"
```

Expected: every fake schedule closes deterministically, every ambiguous call remains terminal, and no test performs network access.
