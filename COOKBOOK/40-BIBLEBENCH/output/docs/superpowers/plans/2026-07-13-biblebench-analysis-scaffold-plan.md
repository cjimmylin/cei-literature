# BibleBench Synthetic Analysis Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce deterministic synthetic-only analysis tables and figure data for the registered vector-first pilot report.

**Architecture:** `analysis.py` validates typed observation rows and emits stable JSON/CSV summaries. Cue analyses require verified custody; all fixture outputs carry an unambiguous synthetic-only status and forbid rankings or composites.

**Tech Stack:** Python 3.11+ standard library, PyYAML/JSON, CSV, pytest.

---

### Task 1: Typed synthetic observations

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/analysis.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_analysis.py`

- [ ] Write failing tests for a minimal observation schema covering module, role, stratum, cue, completion, evidence status, native dimensions, red lines, action/probe consistency, and repeat decisions.
- [ ] Add failures for real/unknown provenance labels, composite-score fields, ranking fields, duplicate observation IDs, and invalid missingness.
- [ ] Implement strict validation and canonical ordering until focused tests pass.

### Task 2: Vector-first summaries

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/analysis.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_analysis.py`

- [ ] Add failing tests for missingness, module-native dimension vectors, common-life/Christian-facing strata, red-line incidents, action/probe consistency, and exact repeat agreement counts.
- [ ] Implement deterministic summary functions with counts and transparent denominators; do not add p-values, composites, leaderboards, or best-model fields.
- [ ] Add a failing cue-contrast test without custody and make the analysis refuse until a verified custody flag/hash is supplied.

### Task 3: Paper table and figure-data exports

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/synthetic-observations.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/synthetic-summary.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/table-shells.csv`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/analysis/README.md`

- [ ] Export fixture artifacts marked `SYNTHETIC_VALIDATION_ONLY` in both metadata and human-readable documentation.
- [ ] Assert deterministic byte-identical regeneration.
- [ ] Assert none of the exports contain empirical claim, ranking, best-model, or composite-score fields.
- [ ] Run focused tests and report exact results.
