# WCF-Bench — Codex Execution Plan v2 (standing; supersedes `20260711-codex-execution-plan.md`)

**Authority:** R47–R57 (`20260712-fable-ratification-memo.md` + `20260712-fable-episode-registry-review-memo.md`).
**Rule of use:** work top-down from the first unchecked task whose gate is open. Tick
checkboxes here AND mirror them on the dashboard. Escalate via `PENDING-QUESTIONS.md`
(+ provisional packet with RESERVED R-numbers when evidence warrants); never improvise
judgment. The v1 plan's anti-rabbit-hole rules and AGENTS.md remain in force.

## Progress

- [ ] **T1 — R47–R53 offline work order** (no gate; boot detail: `20260712-codex-work-order-boot-prompt.md`)
- [ ] **T2 — EPISODE registry application (R54/R56)** (no gate)
- [ ] **T2.5 — T1/T2 ratification recorded** (gate: R57 checklist passed by F2 or Jimmy — not Codex)
- [ ] **T3 — EPISODE 88-cell live run** (gates: Jimmy paid-call reauth + SUT roster; T2; R55 build items)
- [ ] **T4 — gated G1–G7 measurement run** (gates: binding pre-registration memo exists; G6 labels; Jimmy budget)
- [ ] **T5 — perturbation battery at scale (P1–P6)** (gate: T4 lane open)
- [ ] **T6 — release packaging** (gate: gate adjudication ratified)
- [ ] **P — paper-methods skeleton (Milestone C front-load)** (no gate; low priority; may interleave)

## T1 — the R47–R53 offline work order

Execute `20260712-codex-work-order-boot-prompt.md` exactly: W-R48 (willingness-veto fix
at every call site + 3 bidirectional fixtures) → W-R47.3 (corrected manifest event from
the immutable Task-4 raw; STOP+escalate on any cell diverging from memo §2 F-1/F-2) →
W-R49 (MVP OPEN re-parse + delta table, new dated dir, originals untouched) → W-R52.2
(Task-6 plan-text alignment as a dated amendment).
**Done when:** the four W-items' own Done-whens hold + full suite green + PENDING-QUESTIONS
statuses cite R47–R53 + dashboard updated. **No paid calls.**

## T2 — EPISODE registry application (mechanical)

Apply the R54 table to `04-HARNESS/config/episode-spec-registry.draft.json` field-by-field
(22 entries; corrections are exact replacements — do not rephrase). Set the approval block
per R56 (reviewer = the R54 memo, reviewed_at 2026-07-12), transition status per the
`wcfbench/episode_registry.py` loader contract, add the R55.4 bidirectional fixtures
(defection exemplar matches / obedient exemplar does NOT match, per corrected markers).
**Done when:** loader loads the approved registry outside review mode; fixtures green;
full suite green; zero bank YAML edits. **No live run authorized by this task.**

## T3 — EPISODE 88-cell live run (22 items × 4 SUTs)

**Blocked until:** Jimmy reauthorizes paid calls AND confirms the SUT roster (the v1
roster stands unless Jimmy revises), AND T2 is done. Build first, offline (TDD):
- R55.3 verb integration (extend `_DEPLOY_VERBS`/`_REPORT_VERBS` for the bank-named tools).
- R55.2 blind mode (SUT prompt = bank.stem verbatim; no spec-field leakage; the
  defect-calibration injection path stays separate and labeled).
- R55.1 scoring: mechanical `classify_outcome` recorded as SCREEN; score of record =
  rubric-based judge scoring on persisted transcripts by the manifest-of-record panel;
  DECISION-class marker hits are flags only; mechanical-vs-judge disagreements recorded
  first-class.
Then the live run: per-cell checkpoint/resume, budget cap + R40.1 pre-flight, per-rep
raw evidence append-only, new dated run dir + report.
**Done when:** 88 cells scored-or-error-recorded per cell; disagreement summary written;
report labeled DESCRIPTIVE/PRE-GATE (gated status comes only via T4).

## T4 — gated G1–G7 measurement run

**Blocked until:** the binding pre-registration memo exists (F2 deliverable — or
Opus-provisional ratified by Jimmy), G6 labels exist, and Jimmy approves the budget.
Execute the pre-registration EXACTLY as written (it is designed to need zero judgment
calls); any forced deviation = logged Jimmy ruling BEFORE proceeding. Produce the gate
computation report (per-gate evidence, no adjudication — gate PASS/FAIL rulings are
judgment-tier) + a provisional adjudication packet.

## T5 — perturbation battery (P1–P6) at scale

Per the pre-registration's perturbation subset. P1/P5 need LLM materialization (paid —
same authorization lane as T4). Flip-rate reducers are already built and tested.

## T6 — release packaging

Repo layout, bank docs, headline tables with their validity labels exactly as adjudicated
(R34.4 single-family label where applicable; DESCRIPTIVE vs gated separation; PROOF
disclosure per R52). Canary statement included; canary string never re-minted.

## P — paper-methods skeleton (may start anytime)

New `08-PAPER/` dir; outline + methods drafted FROM the R1–R57 memo chain (judge
qualification, probe batteries, artifact forensics, adjudication protocol). NO results,
NO claims — gated numbers don't exist yet.

## Do-NOT list (unchanged + additions)

No paid calls without explicit Jimmy authorization for the specific run · no bank/gold
edits · no exemplar/template changes · no new judge-candidate screening (ladder CLOSED,
R47.4) · no G6 activity (Jimmy's) · no gate adjudication or R-number assignment (reserve
and escalate) · immutable run dirs/reports never modified · dashboard is the sole
undated-edit exception · canary `WCFBENCH-CANARY-c1647-x9k4q` never re-minted · shared
git index discipline (`git log -1` first; explicit paths; never `git add -A`).
