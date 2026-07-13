# BibleBench Provisional Gold and Methods Manuscript Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a judge-ready, non-ratifying provisional-gold review packet for all 48 frozen development episodes while drafting the paper through Methods and Planned Evaluation.

**Architecture:** The frozen authored episode YAML remains the source of truth. A deterministic offline exporter validates those banks and emits review records that copy observable criteria but leave all owner-only judgments explicitly pending. The paper lane consumes only approved design facts, verified engineering facts, and registered prospective claims; it never treats fixtures, test counts, or unreviewed packet content as LLM evidence.

**Tech Stack:** Python 3.14, PyYAML, JSON Schema, pytest, Markdown, YAML, BibTeX, Git.

---

### Task 1: Import the ratified paper-first governance surfaces

**Files:**
- Import: `COOKBOOK/40-BIBLEBENCH/PAPER-FIRST-WORKFLOW.md`
- Import: `COOKBOOK/40-BIBLEBENCH/ACTIVE-CRITICAL-PATHS.md`
- Import: `COOKBOOK/40-BIBLEBENCH/PAPER-FIRST-DECISIONS.md`
- Import: `COOKBOOK/40-BIBLEBENCH/project-dashboard.html`
- Import: `COOKBOOK/40-BIBLEBENCH/AGENTS.md`
- Import: `COOKBOOK/40-BIBLEBENCH/templates/PAPER-CRITICAL-PATH-CONTRACT.md`
- Import: `COOKBOOK/40-BIBLEBENCH/templates/SESSION-OPEN-CLOSE.md`

- [ ] **Step 1: Confirm the ratified portfolio merge commit and exact file set**

Run: `git show --stat --oneline 940bc04aa`

Expected: the seven paper-first governance files are the only imported surfaces.

- [ ] **Step 2: Import the merge relative to its first parent**

Run: `git cherry-pick -m 1 940bc04aa`

Expected: one commit adding the ratified policy, active register, decision log, dashboard, inherited instructions, and templates without changing benchmark evidence.

- [ ] **Step 3: Verify governance bytes against main**

Run: `for f in AGENTS.md PAPER-FIRST-WORKFLOW.md ACTIVE-CRITICAL-PATHS.md PAPER-FIRST-DECISIONS.md project-dashboard.html templates/PAPER-CRITICAL-PATH-CONTRACT.md templates/SESSION-OPEN-CLOSE.md; do cmp "COOKBOOK/40-BIBLEBENCH/$f" "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/$f"; done`

Expected: exit 0 and no output.

### Task 2: Build the non-ratifying provisional-gold exporter

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/schemas/provisional-gold-review.schema.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/adjudication.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_adjudication.py`

- [ ] **Step 1: Write failing tests for packet geometry and owner boundaries**

Tests must require 48 unique review records, exact episode SHA-256 linkage, copied observable criteria, `single_expert_provisional_gold`, `owner_review_status: pending`, blank owner decision fields, no model output, and no silently ratified gold.

Run: `/opt/homebrew/bin/python3 -m pytest tests/test_adjudication.py -q`

Expected: failure because the exporter and schema do not exist.

- [ ] **Step 2: Implement the minimal deterministic exporter**

Implement `build_review_packet(package_root: Path) -> dict` and `write_review_artifacts(package_root: Path, output_dir: Path) -> tuple[Path, Path, Path]`. Load the authored-bank schema, validate every module bank, bind each record to the source episode hash, and leave owner-only fields pending and blank.

- [ ] **Step 3: Add the registered repeat-sample procedure without unblinding the judge**

The packet must register `sample_size: 10`, module/role stratification, opaque repeat IDs, and generation only after pass-one freeze. It must not expose a selected repeat mapping in the pass-one review packet.

- [ ] **Step 4: Run focused tests**

Run: `/opt/homebrew/bin/python3 -m pytest tests/test_adjudication.py tests/test_authored_episode_banks.py -q`

Expected: all focused tests pass.

### Task 3: Generate the human review packet and judge guide

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/adjudication/provisional-gold-review.yaml`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/adjudication/PROVISIONAL-GOLD-JUDGE-GUIDE.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/adjudication/packet-manifest.json`

- [ ] **Step 1: Generate artifacts from frozen authored banks**

Run: `PYTHONPATH=src /opt/homebrew/bin/python3 -m biblebench_pilot.adjudication --package-root . --output-dir adjudication`

Expected: YAML review packet, Markdown judge guide, and JSON manifest are written with no network or credentials.

- [ ] **Step 2: Verify review usability and custody**

Run a deterministic regeneration into a temporary directory and compare SHA-256 values. Confirm the guide explains observable behavior versus theological interpretation, `NOT_APPLICABLE`, confidence, contestability, repair, red-line handling, and single-expert limitations.

- [ ] **Step 3: Confirm no owner judgment was prefilled**

Run: `/opt/homebrew/bin/python3 -m pytest tests/test_adjudication.py -q`

Expected: every owner-only field remains blank or `pending`.

### Task 4: Draft the venue-neutral methods manuscript and claims registry

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/manuscript.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/claims-registry.yaml`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/references.bib`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/limitations-register.md`

- [ ] **Step 1: Draft manuscript sections through Planned Evaluation**

Include motivation, contributions, construct boundaries, local related-work scaffold, four-module/42-family architecture, 48-episode shared methodology, observable-event extraction, isolated lenses, human adjudication, planned cheap-model protocol, engineering validation, ethics, limitations, and future multi-judge validation.

- [ ] **Step 2: Keep results explicitly prospective**

The Results section must contain `PENDING_EMPIRICAL_RUN`; it must contain no model rankings, performance numbers, or empirical conclusions.

- [ ] **Step 3: Populate the typed claims registry**

Every claim must use exactly one approved class: `DESIGN_CLAIM`, `ENGINEERING_CLAIM`, `PROVISIONAL_THEOLOGICAL_JUDGMENT`, `EMPIRICAL_CLAIM_PENDING`, or `EMPIRICAL_CLAIM`. The empirical-claim class must remain empty before the run.

- [ ] **Step 4: Validate manuscript assertions**

Search for unsupported result language and verify every engineering number against repository evidence. Any unresolved citation is labeled as a manuscript completion item rather than invented.

### Task 5: Integrate, review, and update the paper-first surfaces

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/ACTIVE-CRITICAL-PATHS.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/project-dashboard.html`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/README.md`

- [ ] **Step 1: Run one bounded scientific review**

Review only P0/P1 concerns: evidentiary custody, owner-only judgment boundaries, construct validity, unsupported manuscript claims, and reproducibility. P2/P3 findings are recorded and deferred.

- [ ] **Step 2: Run the full credential-free suite**

Run: `/opt/homebrew/bin/python3 -m pytest tests -q`

Expected: zero failures; the known non-failing pytest temporary-directory cleanup warning may remain.

- [ ] **Step 3: Update living paper-first status**

Mark the 48-episode sufficiency P1 resolved, record the provisional-gold packet and manuscript draft, set human owner adjudication as the next P1 gate, and preserve the no-spend boundary.

- [ ] **Step 4: Commit path-scoped artifacts**

Run `git log -1` immediately before each commit. Stage only this task's paper, adjudication, validation, active-contract, dashboard, and plan files. Do not stage unrelated benchmark run or dashboard changes.

## Stop condition

Stop after a judge-ready packet, methods manuscript draft, typed claims registry, limitations register, green offline validation, and updated portfolio surfaces exist. Do not make model calls, access credentials, choose a paid roster, or continue P2/P3 hardening.
