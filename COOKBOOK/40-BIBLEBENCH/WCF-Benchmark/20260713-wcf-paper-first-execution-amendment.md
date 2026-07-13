# WCF-Bench Paper-First Execution Amendment

**Date:** 2026-07-13
**Status:** BINDING, unnumbered Jimmy-ratified operating amendment
**Authority:** Jimmy approved implementation in writing after reviewing the proposed rule
**Effect on R-chain:** none; R1–R68 and all frozen scientific decisions remain unchanged
**Spend authority:** none; this document never authorizes a live or paid call

## Purpose

WCF-Bench exists to produce a scientifically credible, publishable paper supported by
valid empirical evidence. Infrastructure is instrumental, not a project deliverable.
This amendment prevents implementation, review, governance, and documentation work from
silently displacing the next empirical result or mandatory paper artifact.

Safety, evidence integrity, frozen-bank and run-directory rules, examinee blindness,
binding rulings, and explicit budget gates remain controlling. The amendment changes the
stopping rule: once those requirements and the task's registered minimum are satisfied,
the work moves to evidence collection or the paper.

## Binding operating rule

1. **Every session advances the paper.** A session must deliver at least one of:
   empirical evidence; mandatory paper content; citation verification; release packaging;
   or removal/narrowing of a blocker that directly prevents one of those outputs.
2. **Only material blockers stop execution.** A finding may block the next empirical or
   paper milestone only when it threatens result validity, the authorized spending cap,
   frozen-data/run integrity, examinee blindness, reproducibility of the reported study,
   or a binding Jimmy ruling.
3. **Acceptance criteria are the finish line.** Once the plan's minimum sufficiency gate
   passes, stop engineering. Robustness improvements, rare hypothetical cases,
   abstractions, refactors, convenience tooling, additional dashboards, deployment
   hardening, and polish are deferred unless they satisfy rule 2.
4. **Reviews are bounded.** Each implementation task receives at most one specification
   review and one code-quality review against its predefined acceptance criteria.
   Findings must say which rule-2 risk they create; recommendations do not silently become
   prerequisites.
5. **Re-review is verification, not rediscovery.** After blockers are fixed, the re-review
   verifies only those named blockers. It must not reopen a general audit or add polish.
6. **Second-cycle stop.** If a second fix cycle surfaces a new potential blocker, stop and
   ask Jimmy to choose among: fix it, run with the limitation disclosed, narrow the claim,
   or defer it. Codex may not autonomously begin another hardening cycle.
7. **Run when ready.** Once the minimum valid runner is green and the exact run is
   authorized, execute it. After the registered retry allowance, per-cell model failures
   are recorded as results/errors and are not debugging projects.
8. **The dashboard points to evidence or paper.** Its next milestone must be an empirical
   result or paper deliverable unless Jimmy explicitly authorizes a bounded implementation
   exception. Internal test counts and lines of code are supporting evidence, not the
   headline milestone.

## Session controls

At session open, record or identify:

- the next paper-facing milestone;
- the minimum sufficiency gate;
- the exact session-close artifact;
- any rule-2 blocker;
- the engineering timebox; and
- any Jimmy-authorized exception.

At session close, record this allocation estimate:

> Empirical execution __% · paper work __% · infrastructure __% · governance/admin __%

If infrastructure plus governance/admin dominate two consecutive sessions without new
empirical evidence, a mandatory paper artifact, or removal of a rule-2 blocker, the next
session is **RUN OR ESCALATE**. It may not begin another implementation/review loop without
Jimmy's written exception.

## Exception record

Any deviation must be recorded in the dashboard and current handoff with: reason, scope,
approver, approval date, timebox, and completion/expiration condition. An exception is
bounded authority; it does not alter scientific rulings, spending authorization, or other
closed gates.

## Current application

The T3 EPISODE runner's final budget-integrity and score-validity fixes were material
rule-2 blockers. Once their named regressions passed, further infrastructure work was
closed and the authorized empirical run became the required next milestone. After T3,
the critical path returns to the remaining gated experiment and paper-result fill; model
behavior is not investigated beyond the registered retry/error-recording contract.
