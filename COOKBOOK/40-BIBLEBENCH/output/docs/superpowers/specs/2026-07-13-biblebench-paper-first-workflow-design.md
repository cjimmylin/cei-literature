# BibleBench Paper-First Workflow Design

**Status:** Owner-approved design awaiting written-spec review

**Date:** 2026-07-13

**Scope:** Every current and future benchmark under `COOKBOOK/40-BIBLEBENCH/`

**Owner:** Jimmy Lin

## 1. Purpose

BibleBench will default to the shortest scientifically credible path to a publishable paper. Manuscript development, executable-benchmark construction, empirical evidence collection, and deliverable production should advance concurrently whenever their actual dependencies permit.

This policy corrects a demonstrated workflow failure: engineering work was allowed to drift from a scientifically adequate research pilot toward high-assurance public-deployment infrastructure. The additional rigor was often useful, but repeated hardening and review cycles delayed executable episodes, pilot responses, benchmark PDFs, and manuscript results.

The correction does not lower standards for evidentiary integrity or construct validity. It changes the stopping rule from exhaustive hardening to sufficiency for the registered paper claims.

## 2. Binding Decision Rule

Work may block manuscript drafting, pilot evidence collection, analysis, or PDF production only when an unresolved issue could materially compromise at least one of the following:

1. a registered paper claim;
2. evidentiary integrity or custody;
3. construct or content validity;
4. reproducibility of the reported study;
5. participant, operator, or data safety; or
6. an approved spending boundary.

All other improvements must be timeboxed, disclosed as limitations, or moved to a post-pilot backlog.

An agent may deviate from the paper-first critical path only with Jimmy's explicit approval. The exception must be recorded in the applicable decision log and dashboard with its reason, scope, approver, approval date, and expiration or completion condition.

No live or paid model call is authorized by this policy. Existing budget and credential gates remain binding.

## 3. Four Enforcement Surfaces

### 3.1 Portfolio charter

Create `COOKBOOK/40-BIBLEBENCH/PAPER-FIRST-WORKFLOW.md` as the authoritative, portfolio-wide policy. It will contain the binding decision rule, review classifications, stopping rules, exception process, and session obligations.

### 3.2 Agent instructions

Create or update `COOKBOOK/40-BIBLEBENCH/AGENTS.md` so the policy is loaded for every benchmark session. More specific benchmark instructions may add restrictions but may not weaken the paper-first policy. In a conflict, safety, evidence-integrity, frozen-surface, and owner rulings remain controlling.

### 3.3 Benchmark critical-path contracts

Every active benchmark's current execution plan or handoff must contain a Paper Critical-Path Contract. Historical handoffs remain immutable. Each contract must identify:

- `paper_claim_enabled`
- `paper_deliverable`
- `blocking_reason`
- `minimum_sufficiency_gate`
- `timebox`
- `stop_condition`
- `deferred_nonblocking_work`
- `owner_approved_exception`

Only the current authoritative handoff or execution surface is updated. The policy does not require retroactive editing of historical records.

### 3.4 Portfolio dashboard

Create `COOKBOOK/40-BIBLEBENCH/project-dashboard.html` as the portfolio-level paper-progress surface. Existing benchmark dashboards remain authoritative for their local operational details and should link to the portfolio dashboard. The portfolio dashboard must remain self-contained and usable offline.

For every active benchmark, it will show:

| Field | Required content |
|---|---|
| Next paper-facing milestone | The concrete result currently being pursued |
| Manuscript status | Sections drafted, reviewed, or awaiting evidence |
| Executable-bank status | Episodes, probes, contracts, and scoring packets |
| Evidence status | Responses, judgments, reliability checks, and analysis |
| PDF status | Required reports generated and visually verified |
| Current blocker | An open P0/P1 issue or approved dependency |
| Engineering timebox | The limit before stopping or escalating |
| Deferred hardening | P2/P3 work parked until after pilot deliverables |
| Spend | Actual cost and next approval checkpoint |
| Owner exception | The approved deviation and expiration condition |

The dashboard will also display:

- **Paper critical-path health:** `ON PATH`, `AT RISK`, or `OFF PATH`.
- **Engineering-to-paper ratio:** completed enabling tasks compared with nonblocking engineering tasks during the current reporting window.

This ratio is a diagnostic, not an optimization target or researcher-performance score.

## 4. Paper-First Operating Funnel

Every benchmark follows this sequence unless a recorded owner exception changes it:

1. Define the paper claim and minimum evidence needed to support it.
2. Draft the corresponding manuscript section immediately.
3. Build only the benchmark material needed to test the claim.
4. Pass the registered scientific-sufficiency gate.
5. Freeze a reproducible research snapshot.
6. Collect pilot evidence.
7. Produce analyses, tables, figures, and benchmark PDFs.
8. Revise the manuscript using the evidence.
9. Resume durability engineering after pilot deliverables exist.

Steps may run concurrently when dependencies allow. The numbered list expresses dependency priority, not a requirement to idle one track while another advances.

## 5. Finding Classification and Stopping Rules

All review findings that could affect the critical path must be classified:

| Class | Meaning | Default disposition |
|---|---|---|
| P0 | Invalidates evidence or creates serious safety or integrity risk | Blocks progress until resolved |
| P1 | Could materially change a paper conclusion | Fix, narrow the claim, or obtain an owner ruling |
| P2 | Affects robustness but not the registered pilot conclusion | Disclose and defer |
| P3 | Polish, compatibility, deployment hardening, or hypothetical edge case | Backlog |

A P2 or P3 finding cannot block manuscript or pilot work without Jimmy's documented approval. Repeated implementation-review-repair loops stop when all of the following are true:

- no P0 finding remains open;
- each P1 finding is fixed, bounded by a narrowed claim, or resolved by an owner ruling;
- the registered sufficiency gate passes; and
- the research snapshot can be reproduced for the intended pilot.

Reviewers may recommend later hardening, but recommendations do not silently become prerequisites.

## 6. Session Obligations

At session opening, the agent must identify from the dashboard and current handoff:

1. the next paper-facing milestone;
2. the registered sufficiency gate;
3. the current P0/P1 blocker, if any;
4. the engineering timebox; and
5. the exact artifact expected by session close.

During the session, scope expansion beyond the critical-path contract must be escalated instead of silently adopted.

At session close, the agent must report one of:

- a completed paper-facing artifact;
- removal or narrowing of a genuine P0/P1 blocker; or
- an explicit escalation explaining why neither was possible.

Test counts, implementation volume, and review depth may support the report but do not substitute for paper-facing progress.

## 7. Drift Detection

The portfolio dashboard must show `OFF PATH` when any of the following occurs without a live owner-approved exception:

- a completed session produces no paper-facing artifact and removes no P0/P1 blocker;
- nonblocking engineering exceeds its declared timebox;
- manuscript work remains idle despite sufficient available information;
- a P2 or P3 issue delays pilot evidence collection;
- a new requirement enters the critical path without an owner ruling; or
- a benchmark handoff lacks a concrete next paper-facing deliverable.

`AT RISK` is used when a timebox, budget checkpoint, owner decision, or external dependency is approaching but has not yet caused an `OFF PATH` condition. All other active work is `ON PATH`.

## 8. Rollout

Implementation will:

1. add the portfolio charter;
2. add the binding top-level agent instructions;
3. create the portfolio dashboard;
4. add a reusable Paper Critical-Path Contract template;
5. update each active benchmark's current authoritative handoff or execution surface;
6. record the workflow correction in a portfolio decision log;
7. add session-opening and session-closing templates; and
8. link existing local dashboards to the portfolio surface without rewriting their historical records.

Existing uncommitted work in benchmark dashboards, agent instructions, run ledgers, checkpoints, and evidence files must be preserved. Rollout edits must use path-scoped staging and must not absorb unrelated changes.

## 9. Acceptance Criteria

The rollout is complete when:

1. a fresh agent can identify the portfolio's next paper-facing task from `AGENTS.md` and the dashboard in under two minutes;
2. every active benchmark reports manuscript, executable-bank, evidence, and PDF status;
3. every claimed blocker is classified P0/P1 or linked to an owner-approved exception;
4. deferred P2/P3 work is absent from the active critical path;
5. every active handoff identifies a deliverable, sufficiency gate, timebox, and stop condition;
6. the session-close template requires a paper-facing artifact, a removed blocker, or an escalation;
7. the dashboard contains the workflow-health and exception fields defined above;
8. no paid call or credential access occurs during documentation rollout; and
9. the policy explicitly governs all current and future benchmarks under `40-BIBLEBENCH/`.

## 10. Non-Goals

This policy does not:

- waive scientific, theological, ethical, safety, or evidence-integrity requirements;
- authorize live model calls or spending;
- convert P2/P3 findings into ignored defects;
- prescribe manuscript conclusions before evidence is collected;
- erase or rewrite historical handoffs and decision records; or
- require every benchmark to use an identical empirical design.

Its purpose is to keep sufficient engineering, empirical evidence, deliverables, and manuscript production aligned around the paper's registered claims.
