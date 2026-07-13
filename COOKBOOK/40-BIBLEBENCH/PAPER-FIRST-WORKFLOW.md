# BibleBench Paper-First Workflow

**Authority:** Binding for every current and future benchmark under this directory.

**Owner ruling:** PF-001, ratified by Jimmy Lin on 2026-07-13.

## Purpose

BibleBench defaults to the shortest scientifically credible path to a publishable paper. Manuscript development, executable-bank construction, empirical evidence collection, and deliverable production proceed concurrently whenever their actual dependencies permit.

The stopping rule is scientific sufficiency for the registered paper claims, not exhaustive hardening for hypothetical public deployment.

## Decision rule

Work may block manuscript drafting, pilot evidence collection, analysis, or PDF production only when an unresolved issue could materially compromise:

1. a registered paper claim;
2. evidentiary integrity or custody;
3. construct or content validity;
4. reproducibility of the reported study;
5. participant, operator, or data safety; or
6. an approved spending boundary.

All other improvements are timeboxed, disclosed as limitations, or moved to the post-pilot backlog.

## Owner exception

Deviation requires Jimmy's explicit approval recorded in `PAPER-FIRST-DECISIONS.md` and `project-dashboard.html`. The record must include its reason, scope, approval date, affected paper milestone, and expiration or completion condition.

An agent may recommend a deviation. It may not silently make one.

## Four paper-progress tracks

Every active benchmark reports these separately:

1. **Manuscript:** sections drafted, reviewed, and awaiting evidence.
2. **Executable bank:** episodes, probes, contracts, scorers, and judge materials.
3. **Evidence:** pilot responses, human judgments, reliability checks, analyses, tables, and figures.
4. **PDF deliverables:** reports generated and visually verified.

Engineering work is reported as enabling or nonblocking. Test counts and implementation volume support progress claims but do not substitute for progress on these four tracks.

## Paper-first operating funnel

1. Define the paper claim and minimum evidence.
2. Draft the corresponding manuscript section immediately.
3. Build only the benchmark material needed to test the claim.
4. Pass the registered scientific-sufficiency gate.
5. Freeze a reproducible research snapshot.
6. Collect pilot evidence.
7. Produce analyses, tables, figures, and benchmark PDFs.
8. Revise the manuscript using the evidence.
9. Resume durability engineering after pilot deliverables exist.

Steps run concurrently when dependencies permit. This sequence expresses dependency priority; it does not require one track to idle while another can advance.

## Review classification

| Class | Meaning | Default disposition |
|---|---|---|
| P0 | Invalidates evidence or creates serious safety or integrity risk | Blocks until resolved |
| P1 | Could materially change a paper conclusion | Fix, narrow the claim, or obtain an owner ruling |
| P2 | Affects robustness but not the registered pilot conclusion | Disclose and defer |
| P3 | Polish, compatibility, deployment hardening, or hypothetical edge case | Backlog |

A P2 or P3 finding cannot block manuscript, pilot, analysis, or PDF work without Jimmy's recorded approval.

Repeated implementation-review-repair loops stop when:

- no P0 finding remains open;
- every P1 is fixed, bounded by a narrowed claim, or resolved by an owner ruling;
- the registered sufficiency gate passes; and
- the intended pilot snapshot is reproducible.

Review recommendations do not silently become prerequisites.

## Required critical-path contract

Every active benchmark must have concrete values for:

- `paper_claim_enabled`
- `paper_deliverable`
- `blocking_reason`
- `minimum_sufficiency_gate`
- `timebox`
- `stop_condition`
- `deferred_nonblocking_work`
- `owner_approved_exception`

The living contracts are in `ACTIVE-CRITICAL-PATHS.md`. New benchmarks enter that register before engineering begins.

## Session opening

Before work, read `project-dashboard.html`, `ACTIVE-CRITICAL-PATHS.md`, and the benchmark's current local state. State:

1. the next paper-facing milestone;
2. the minimum sufficiency gate;
3. the current P0/P1 blocker, if any;
4. the engineering timebox; and
5. the expected closing artifact.

Scope expansion beyond the registered contract is escalated rather than silently adopted.

## Session closing

Report one of:

- a completed paper-facing artifact;
- removal or narrowing of a genuine P0/P1 blocker; or
- an explicit escalation explaining why neither was possible.

Update the living dashboard and active contract when their state materially changes. Preserve historical handoffs and append-only records.

## Dashboard health

- **ON PATH:** work is advancing a registered deliverable or removing a genuine P0/P1 blocker within its timebox.
- **AT RISK:** a timebox, budget checkpoint, owner decision, or external dependency is approaching.
- **OFF PATH:** progress has drifted without a current owner-approved exception.

The dashboard shows `OFF PATH` when:

- a completed session produces no paper-facing artifact and removes no P0/P1 blocker;
- nonblocking engineering exceeds its timebox;
- manuscript work remains idle despite sufficient available information;
- a P2 or P3 issue delays pilot collection;
- a new requirement enters the critical path without an owner ruling; or
- an active contract lacks a concrete next paper-facing deliverable.

## Boundaries

This policy does not authorize live model calls, network calls, spending, credential access, frozen-surface edits, or historical-record rewrites. Existing safety, evidence-integrity, budget, credential, and owner gates remain binding.

The policy does not ignore P2/P3 defects. It records and schedules them after the paper-critical pilot unless Jimmy explicitly rules otherwise.
