# BibleBench Cue Evidence Custody Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the pre-live P1 by binding every C0/C1/C2 primary and matched probe call to exact request and evidence-bundle hashes.

**Architecture:** A private `custody.py` module derives expected pair rows from a frozen schedule and joins them to a supplied artifact inventory. A strict schema and verifier enforce full coverage and immutable exact hashes.

**Tech Stack:** Python 3.11+, dataclasses, JSON Schema, canonical JSON, pytest, SHA-256.

---

### Task 1: Manifest contract and RED tests

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/cue-custody.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_custody.py`

- [ ] Write a failing synthetic-schedule test expecting one row per primary/probe pair with bundle, actor, module, episode, cue, both logical-call IDs, both request hashes, and one evidence-bundle hash.
- [ ] Add failing cases for missing artifact, duplicate row, cross-bundle pair, wrong primary link, cue mismatch, and evidence hash tamper.
- [ ] Run `/opt/homebrew/bin/python3 -m pytest tests/test_custody.py -q` and confirm failure because the module is absent.

### Task 2: Builder and verifier

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/custody.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_custody.py`

- [ ] Implement `build_cue_custody_manifest(schedule, evidence_inventory)` from the frozen schedule rather than caller-supplied pair relationships.
- [ ] Require exactly one inventory artifact for every bundle and canonical SHA-256 for every request and evidence object.
- [ ] Implement `verify_cue_custody_manifest(schedule, evidence_inventory, manifest)` to recompute the entire manifest and compare exact canonical content.
- [ ] Add immutable JSON export with manifest hash and exclusive-create behavior.
- [ ] Run focused tests and confirm all RED cases are GREEN.

### Task 3: Synthetic fixture and handoff

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/fixtures/cue-custody-synthetic.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/custody/README.md`

- [ ] Generate a clearly labeled synthetic fixture with no provider or model output.
- [ ] Document private custody, verification command, pre-live gate, and prohibition on judge/model visibility.
- [ ] Run schema validation, focused tests, and a no-secret/no-model-output scan.
