# WCF-Bench — Next-Session Boot Prompt (Fable, fresh context; paste after /model fable + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are a
**Fable session** (judgment tier: adjudication, ratification, pre-registration — push any
build/mechanical work down-tier or leave it to Codex). Session 16 closed the execution
thread and handed building to Codex (R42–R46 + `20260711-codex-execution-plan.md`); your
job is the judgment layer above that work.

## Step 0 — load state (the session is STATE-ADAPTIVE; this determines your agenda)

1. **Open `project-dashboard.html`** — Live-status table, progress bars, milestone
   checkboxes, open escalations. (Mandatory on session open; you will update it on close.)
2. `git log --oneline -15 -- COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` + check the branch
   `codex/wcfbench-mvp-testable` for commits.
3. Read `PENDING-QUESTIONS.md` if it exists + the latest `*codex-session-handoff.md` if any.
4. Read order (then, ~15 min): `20260711-wcf-session16-handoff.md` (§4 + addendum) →
   `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46) →
   `20260711-codex-execution-plan.md` (checkbox state) →
   `00-OVERVIEW/20260706-shared-spine.md` §gates (G1–G7, lines ~71–77) — needed for
   agenda item 2.

## Agenda (priority-ordered; do what the state supports)

**1. Adjudicate whatever Codex surfaced (if anything).** Any `PENDING-QUESTIONS.md`
entries → rule them (R47+, new dated memo, R29/R31 mode where sample-level). Any completed
Codex tasks → review against their Done-when specs (spot-check, don't re-execute). If
**Task 4 ran**: ratify or reject the re-screen outcome — the K=8 pass/fail table for
grok / cohere-command-a / amazon-nova-pro under the bridged template, the new combined
manifest, and (if any candidate passed) the OPEN-award label change; check the
discrimination bar was NOT relaxed (R44.3) and that a zero-pass was treated as
ladder-CLOSED (R44.5). This is exactly the judgment work R42–R46 reserved.

**2. THE FRONT-LOAD ITEM — pre-register the gated G1–G7 run (main deliverable if Codex
has nothing to adjudicate).** WCF-Bench has NO gated-run pre-registration: the spine
defines the gates but not their exact computations. Freeze them BEFORE more data exists
(the WALKWORTHY gate-prereg precedent, `Christian-Ethics-Benchmark/00-PORTFOLIO/
20260710-fable-gate-prereg-pilot-adjudication.md` — mirror its rigor, do NOT copy its
content; benches stay un-cross-wired). Write a BINDING memo
(`YYYYMMDD-fable-gated-run-prereg-memo.md`, rulings R47+ continuing the chain) pinning:
  - **G1**: the capability battery (which public scores/source), PC1 construction, the
    exact correlation computed, and the <40% test;
  - **G2**: ceiling definition per scorer kind, the ≤~70% frontier-headroom test, and
    which models count as "frontier" for it;
  - **G3**: bootstrap procedure (over items, B, seed policy), the frontier pair set, and
    the ≥90%-of-pairs-at-p<0.01 computation on T2+;
  - **G4**: κ form + weights vs the G6 human labels, the human–human ceiling handling,
    per-surface application (OPEN/disclosure/settled-core/coherence), and what happens to
    a surface that fails;
  - **G5**: the lexical-baseline model and the 10%-fine-tune probe design (or a ruled,
    disclosed substitute if FT is impractical);
  - **G6**: how ≥85% consensus maps onto gold/[DISPUTED]/positions (the contested-scoring
    ruling constrains this);
  - **G7**: the internal-consistency statistic per design and the α>0.99 redundancy flag;
  - **the gated-run design**: SUT roster (+ anti-leakage vs judge/generator families),
    items in scope (incl. EPISODE), perturbation subset, budget cap, and the
    deviation/disclosure protocol (pre-reg is frozen once data exists — changes need a
    logged Jimmy ruling).
  Constraints: no live calls needed; the pre-reg must be executable by Opus/Codex without
  judgment calls; nothing in it may relitigate R1–R46; PROOF numbers stay non-quotable
  until Task 6 lands (R45.1) — say how the gated run treats PROOF if Task 6 is not done.

**3. If time remains (optional):** draft the paper-methods skeleton (Milestone C's
front-loadable half — outline + methods sections from the R-chain; no results). New dated
file under a `08-PAPER/` dir. Do not write results/claims — gated numbers don't exist.

## Guardrails (standard, hook-free surfaces enforced manually where needed)

Judgment session: NO live model calls expected (pre-reg needs none; if item 1 truly
requires a spot re-read it uses persisted transcripts only). No bank edits, no gold
minted, no G6 activity, no item kills outside pre-ruled gates. Report + run-dir
immutability (new dated files only; `project-dashboard.html` is the sole undated
exception). Canary `WCFBENCH-CANARY-c1647-x9k4q` never re-minted. Shared git index LIVE:
`git log -1` before every commit, explicit WCF-Benchmark paths, never `git add -A`,
fast-forward pushes. Sibling benches (WALKWORTHY etc.) are read-only precedent at most —
never cross-wire content.

## On session close (mandatory)

1. **Update `project-dashboard.html`** per `AGENTS.md §The project dashboard`: last-updated
   line, Live-status, progress bars, a new S-row in Phase 6, milestone checkboxes if
   ratified, gate board if the pre-reg pins statuses, update-log line.
2. Update the `wcf-bench-portfolio-state` memory note.
3. Write the next re-entry boot prompt (carrying the dashboard open/close lines — standing
   AGENTS.md convention) + a dated session handoff, AND rewrite the dashboard's
   **§Instructions for next session** (paste text, model, directory) to point at it.
4. Commit + push (explicit paths).

> Fallback: if the Fable window has lapsed, run this same boot on **Opus** but DOWNGRADE:
> item 1 → descriptive cataloging + recommendations (no binding rulings, no overrules);
> item 2 → the pre-reg may be fully DRAFTED but marked **PROVISIONAL — pending
> Fable/Jimmy ratification** in its header and the R-numbers reserved, not assigned.
