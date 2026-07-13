# BibleBench Blinded Repeat Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a judge-safe, immutable 10-record repeat packet and finalization workflow without exposing original record identity or pass-one judgments.

**Architecture:** A new `repeat.py` module consumes the completed adjudicated packet and custodian mapping, emits an allowlisted opaque packet, validates fresh owner judgments, and freezes results with a manifest. A dedicated JSON Schema defines judge-visible data.

**Tech Stack:** Python 3.11+, PyYAML, jsonschema, pytest, SHA-256.

---

### Task 1: Opaque packet contract

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/repeat-review.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_repeat.py`

- [ ] Write a failing test that builds a completed 48-record packet and fixed custodian mapping, then asserts the wished-for repeat packet has exactly 10 `RPT-NNN` records and its serialization contains no original episode ID, original decisions, rationales, source paths, or mapping keys.
- [ ] Run `/opt/homebrew/bin/python3 -m pytest tests/test_repeat.py -q` and confirm failure because `biblebench_pilot.repeat` does not exist.
- [ ] Define a strict schema with `additionalProperties: false`, opaque IDs, exact 10-record geometry, hash-bound allowlisted review content, null pending judge fields, and no original-ID fields.

### Task 2: Packet builder and validation

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/repeat.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_repeat.py`

- [ ] Add failing tests for mapping hash mismatch, unknown/duplicate episode mapping, non-completed pass one, and forbidden visible fields.
- [ ] Implement `build_repeat_review_packet(package_root, completed_packet_path, mapping_path)` using an explicit content allowlist and canonical hashes.
- [ ] Validate the completed packet with the existing adjudication validator, bind the exact completed-packet SHA-256 and mapping SHA-256, and reject all invalid relationships.
- [ ] Run focused tests and confirm GREEN.

### Task 3: Repeat finalization and custody manifest

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/repeat.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_repeat.py`

- [ ] Add failing tests requiring all 10 fresh judgments, stable judge identity, UTC timestamps, deterministic roll-up, immutable output, and an artifact hash manifest.
- [ ] Implement `finalize_repeat_review(...)` with exclusive-create outputs and no mapping or original identity in the frozen judge artifact.
- [ ] Add a test proving the original-to-repeat join remains possible only through the separate custodian mapping after both submissions freeze.
- [ ] Run focused tests, review the diff, and report RED/GREEN evidence.
