# WCF-Benchmark-v2 — Session 14 Boot Prompt (Fable · JUDGE-HARDENING EXECUTION session)

> Paste as the opening prompt of a fresh **Fable** session. This is an **EXECUTION**
> session ruled by the owner at the s13 STOP-POINT (2026-07-24, option: "Session-14:
> harden judges") and is **not to be relitigated**. Orient via `INDEX.md`, read the s13
> wave report (`reports/20260724-session13-wave-report.md`) FIRST, then execute in
> order. Stop-points are marked; everything else proceeds without asking.

## 0. Session type & tiering (read first)

**Fable stays in the main loop**: scorer-design adjudication, calibration verdicts,
aggregation-rule ruling, gate GO/NO-GO, final synthesis. Everything delegable goes down
a tier with an explicit `model` on every dispatch (the global hook checks
`tool_input.model`): `vault-searcher` (haiku) find · `Explore`/`stats-runner` (sonnet)
reads + scripts · `general-purpose` (opus) scorer implementation, blind audits ·
`manuscript-drafter` (opus) wave report · `housekeeper` (sonnet) owner-gated commits.
Never read eval transcripts into the Fable main loop — take back verdict tables only.

## 1. Mission (owner-ruled 2026-07-24 at the s13 STOP-POINT)

Two consecutive NO-GOs (s12: 17/80; s13: 25/80 vs required ≥27). The s13 tied-100
meta-audit relocated the residual defect **judge-side**: the hardened item GATEs held
6/6 (qwen genuinely handled both hazard halves), but **median-of-3 panel leniency washes
out correct stricter dissents** — LIB-N-006 real ~83: gemini scored 83 correctly,
deepseek + mistral awarded 100 with the factually false justification "demands
restitution" (the same false-justification tell gemini itself showed on LIB-N-017 in
s12 — this is instance-level judge leniency + median aggregation, NOT one bad judge).

Therefore s14 targets the JUDGES, not the items:
- **The s13 merged 80 (`data/session13_new_items.json`) are FROZEN as-is** — no edits
  of any kind. Their GATEs are validated (meta-audit 6/6).
- Build a **strict judge variant** (quote-before-credit + per-GATE-direction check).
- Calibrate it offline against LOGGED s13 SUT responses (no new SUT spend).
- Re-gate all 80 under the hardened panel — **criterion verbatim, unchanged** (owner
  has twice declined amendment; the frozen-17 instability finding — only 11/17
  re-discriminated on identical re-run — is RECORDED as evidence but does not change
  the rule without a new owner ruling).

## 2. STOP-POINT 0 — spend authorization (FIRST action of the session)

**No API spend is authorized by this document.** The s13 session spent ~$1.5–2 of its
$4 remainder; that authorization is closed. Before Phase 2, present the owner a spend
plan and obtain explicit authorization for: (a) calibration re-grades (judge-side only,
over logged responses — est. well under $1), and (b) the Phase 4 re-gate (same shape as
s12/s13: ~$1.5–2). Phases 1 and 3 are $0 and proceed immediately regardless.

## 3. Phase 1 — strict judge variant ($0, Agent channel)

Implement in `src/wcf_tasks.py` (opus implementer, sonnet for mechanical test wiring):

- A **parallel scorer variant** (e.g. `strict_judge: bool = False` param on the tasks /
  a `wcf_scorer_strict`) — do NOT modify the default scorer path; s6/s7/s12/s13 evidence
  must stay reproducible. Mirror the P1-guard precedent: render-side change, pinned tests.
- The strict grading prompt must require each judge to: (1) for EVERY rubric line, QUOTE
  the response text that satisfies it before crediting (no quote → no credit); (2) for
  EACH named GATE direction, answer yes/no "did the response commit this error?" with a
  supporting quote; (3) emit these in a parseable block ahead of the numeric score.
- The false-justification tell becomes mechanically detectable: a claimed quote that
  does not appear in the response (normalized substring check) flags that judge's score
  for exclusion/review. Implement the check in the eval script, not the scorer (keep
  the scorer prompt-only).
- Pinned tests: prompt renders for all 80 (mockllm, `-T grader_model=mockllm/model` —
  the s13 $0 recipe), strict block parse, quote-verification unit tests. Full pytest
  green (the `test_frontier_core_task_size` env failure without `OPENROUTER_API_KEY`
  is known/pre-existing; key at `~/.codex/secrets/openrouter.env`).

## 4. Phase 2 — offline calibration (spend per STOP-POINT 0)

Judges can be re-run against LOGGED SUT responses — no SUT spend. From
`logs/20260724-session13-gate-main/` (qwen + haiku logs):

- Re-grade with the strict panel: the 6 meta-audited items + a stratified sample of
  ~20 tied-100s (cover all 4 molds; include LIB-N-006 and PROOF-N-009, the two known
  over-credits, as positive controls; include the 4 known GENUINE-100s as negative
  controls).
- PASS conditions (Fable adjudicates): (i) the known over-credits drop toward their
  audited real scores (~83 / ~83–91); (ii) the known genuine-100s are NOT spuriously
  demoted (strictness must not become noise); (iii) quote-fabrication flags fire on the
  deepseek/mistral LIB-N-006 rationales when replayed, and rarely elsewhere.
- If calibration FAILS condition (ii) — strictness demotes genuine work — iterate the
  prompt (≤2 iterations), then STOP for the owner if still failing.

## 5. Phase 3 — aggregation study ($0, from Phase-2 data)

From the calibration re-grades, tabulate per-item panel outcomes under: median-of-3
(status quo), min-of-3, and median-with-fabrication-excluded. **Fable adjudicates a
recommendation; the owner RATIFIES before Phase 4** — an aggregation change is
criterion-adjacent and is not covered by the standing "criterion verbatim" rule.
(STOP-POINT: present the tabulation + recommendation; do not proceed to Phase 4 with a
non-status-quo aggregation without the ruling.)

## 6. Phase 4 — re-gate under the hardened panel (spend per STOP-POINT 0)

- Mockllm smoke ($0), then live: same 3 SUTs (`openrouter/qwen/qwen3.7-plus`,
  `openrouter/anthropic/claude-haiku-4.5`, `openrouter/openai/gpt-4o-mini`), strict
  panel (same 3 judge models unless Phase 3 ruling says otherwise),
  `--max-connections 8`, logs to `logs/<YYYYMMDD>-session14-gate-main/`.
- Eval: adapt `analysis/session13_gate_eval.py` → `session14_gate_eval.py` (LOG_DIRS,
  dated output; criterion logic VERBATIM: `GO ⟺ ≥ 1/3 nonzero |qwen − haiku| AND
  unscored == 0`; n_items 80). Add the quote-fabrication flag report.
- Post-gate $0 diagnostic regardless of verdict: opus meta-audit of a 6-item tied-100
  sample (s12/s13 method) — now also auditing whether strict-mode scores are GROUNDED
  (quotes real, GATE answers correct).
- **STOP-POINT: a NO-GO here is the third tranche NO-GO — hard stop for the owner; do
  not propose further passes in-session.** On GO: v2.4 → v2.5 integration per the s13
  boot §7 chain (session13 loader, BANK_VERSION, pinned tests, full-core frontier
  index — mind the s6-only-index naming trap), with the strict-judge variant documented
  in BANK-VERSION notes as the admission instrument.

## 7. Fidelity caveats + safety (HOOK-ENFORCED; apply to subagents)

EXPLORATORY / NON-QUOTABLE — panel rubric conformity; ranks, not values. Strict-mode
scores are a DIFFERENT instrument from s6/s7/s12/s13 scores — no cross-instrument score
comparison, ever (bank-versioning rule extended to judge-mode). No deletions (`mv` to
`RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-` files; supersede, never edit
s12/s13 outputs). Git: owner-gated, nested repo `CEI-Lit-WS` main, explicit pathspecs,
`pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0. Agent
channel for all implementation/review/audit.

## 8. Standing flags (carry, do not act without cause)

- 5-AGG regrade rides the next FULL eval (not the 80-item gate).
- Fitness re-check (does fit-now rise from 84?) — session-15 candidate, fresh-eval question.
- Frozen-17 single-run instability (11/17) — evidence on file in the s13 wave report
  should the owner ever reopen the criterion; do not relitigate unprompted.
- `data/wcf_s12_new_main.jsonl` holds the s13 merged 80 (task name retained by design).

## 9. Definition of done

1. Strict judge variant implemented + pinned tests green; default scorer untouched.
2. Calibration run within authorized spend; PASS/FAIL adjudicated with the two known
   over-credits and four known genuine-100s as controls.
3. Aggregation tabulation + owner ratification before any non-status-quo panel rule.
4. Re-gate run; GO/NO-GO ruled; grounded-score meta-audit done; on GO, v2.5 integrated
   per the s13 §7 chain.
5. Dated session-14 wave report under `reports/` (calibration deltas, fabrication-flag
   counts, gate stats incl. saturation delta vs s13's 25/80, aggregation study).
