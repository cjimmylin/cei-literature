# BibleBench Judge UI Lane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local, contamination-safe interface for completing the 48-record pass-one adjudication packet without mutating authoritative YAML.

**Architecture:** A Python builder validates the frozen review packet and emits one self-contained HTML file with embedded read-only episode data, CSS, and JavaScript. Browser localStorage holds drafts; JSON import/export is the only data interchange. Python tests inspect the generated artifact and exercise the same mechanical validation contract.

**Tech Stack:** Python 3.11+, HTML5, CSS, dependency-free JavaScript, pytest, PyYAML, jsonschema.

---

### Task 1: Specify the judge-draft contract

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/judge-draft.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_judge_interface.py`

- [ ] **Step 1: Write failing schema tests**

Require `artifact_status: DRAFT_INCOMPLETE|DRAFT_COMPLETE`, exact source packet hash, 48 unique records, and only owner-editable fields. Reject provider/model/run-order/repeat-membership fields and any non-null prefilled owner decision.

```python
FORBIDDEN = {"model", "provider", "actor", "run_order", "repeat_member", "suggested_answer"}
assert not FORBIDDEN.intersection(walk_keys(exported_draft))
assert len({row["episode_id"] for row in exported_draft["records"]}) == 48
```

- [ ] **Step 2: Run the test and verify failure**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_judge_interface.py -q`

Expected: FAIL because the schema and builder do not exist.

- [ ] **Step 3: Implement the closed JSON Schema**

Use `additionalProperties: false` at every object level. Mirror the existing allowed decision/confidence/contestability enums and require rationale/issue arrays according to the finalizer's mechanical rules.

- [ ] **Step 4: Re-run the schema tests**

Expected: schema tests PASS; builder tests still FAIL.

### Task 2: Build the self-contained interface

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/judge_ui.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/adjudication/judge-interface.html`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_judge_interface.py`

- [ ] **Step 1: Add builder tests**

Test exactly 48 records, the source packet SHA-256, no external URL, no `<script src>`, no `<link href>`, no forms, no fetch/XHR/WebSocket/EventSource, no repeat membership, and this CSP:

```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; connect-src 'none'; form-action 'none'; frame-ancestors 'none'; base-uri 'none'">
```

- [ ] **Step 2: Implement the Python builder**

Load and validate `provisional-gold-review.yaml` with existing adjudication code, embed only authorized review content, escape `</script>` safely, and write deterministic UTF-8 bytes. Refuse a packet containing any completed owner decision.

- [ ] **Step 3: Implement one-record navigation**

Provide module/role filters, progress counts, previous/next controls, keyboard shortcuts, a record index, and visible `pending` state. Never calculate or display a substantive recommendation.

- [ ] **Step 4: Generate and test**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && PYTHONPATH=src /opt/homebrew/bin/python3 -m biblebench_pilot.judge_ui && /opt/homebrew/bin/python3 -m pytest tests/test_judge_interface.py -q`

Expected: one deterministic HTML file and PASS.

### Task 3: Implement lossless draft handling and mechanical validation

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/judge_ui.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_judge_interface.py`

- [ ] **Step 1: Add round-trip and validation tests**

Assert JSON export/import preserves every owner field byte-for-byte after JSON normalization; reload uses a namespaced localStorage key bound to packet hash; incomplete records export as `DRAFT_INCOMPLETE`; and complete coherent records export as `DRAFT_COMPLETE`.

- [ ] **Step 2: Implement local autosave and import/export**

Use only `localStorage`, `Blob`, and `FileReader`. Never write authoritative YAML, invoke a server, or transmit data.

- [ ] **Step 3: Implement neutral warnings**

Warnings may say `Required field is empty`, `Value is outside the allowed set`, or `Current fields are internally inconsistent`. They may not name the answer that would resolve the error.

- [ ] **Step 4: Run focused and existing adjudication tests**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_judge_interface.py tests/test_adjudication.py -q`

Expected: PASS.

### Task 4: Document and commit the lane

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/adjudication/JUDGE-INTERFACE-README.md`

- [ ] **Step 1: Write operating instructions**

Document offline opening, local autosave, explicit export, backup, reset, draft status, and the existing fail-closed finalizer. State that the interface supplies no answer guidance and that blinded repeat work happens only after pass-one freeze.

- [ ] **Step 2: Rebuild twice and compare hashes**

Run the builder twice and compare `shasum -a 256 adjudication/judge-interface.html`; expected hashes are identical.

- [ ] **Step 3: Run the lane test set**

Run the Task 3 command. Expected: PASS.

- [ ] **Step 4: Commit the lane**

Run `git log -1 --oneline`, path-stage only judge-UI files, schema, and tests, then commit with `BibleBench: add offline pass-one judge interface`.
