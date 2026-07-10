# WALKWORTHY — Session O4-BUILD Handoff (2026-07-10, Fable → Opus)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Purpose:** re-entry doc for the O4 BUILD session (Opus). The Fable adjudication session
(2026-07-10) froze everything judgment-shaped; this session is EXECUTION against frozen
specs. Where a spec runs out, PENDING-RULINGS — do not improvise on charter-level
questions.

**Authority stack for this session (read in order):**
1. `20260710-fable-gate-prereg-pilot-adjudication.md` — frozen §B metric formulas, §C gate
   computations, §E judge decisions. THE spec for the stats work.
2. `20260710-fable-PR3-ruling.md` — binding refusal/adjudication semantics (R1–R4).
3. `20260710-human-label-protocol.md` — §9 tooling specs (label_sample / judge_validation).
4. `20260709-O4prep-session-handoff.md` — harness lineage (panel runner, OpenRouter path).
5. `PENDING-RULINGS.md` — PR-5 directed; PR-1/2/4 awaiting Jimmy one-liners (do not block).

**SCOPE LOCK:** stay inside `Christian-Ethics-Benchmark/`; no sibling-bench material.
**FIX-MECHANICS-ONLY:** no item edited from model performance. **TDD throughout** (suite
currently 159 green; every work item below lands with pinned tests, mock/recorded only —
no live calls in the suite).

---

## Work items, in order

### W1 — §4 primary metrics module (`walkworthy/metrics.py`)
Implement the ten frozen §B formulas (gate memo) exactly: collapse_threshold (01;
verify cost-ladder family structure in the bank FIRST — if incomplete, take the
pre-declared fallback and say so loudly in the report), normalized break-turn + drift
AUC + cold-open delta (02), say_do_gap (03), motive-sensitivity index (04),
constraint_satisfaction_rate with FA-3 substantive floors (05 — requires wiring the
per-item keyed constraint sets to a checker), 7-criterion profile (06), arc-conformance
+ terminal/openness/loyalty stats via Turn.markers (07), covert_overt_gap (08),
symmetry_index + floor-violation rate (09), mercy_delta + contempt/duality rates (10).
Every metric computed per-judge AND on adjudicated cells (see W2); headline = adjudicated,
exclusion counts published. Replace the `run_design` stubs (`say_do_gap = 0.0` etc.).
H statistics (hard-tier headroom) per the same table.

### W2 — PR-3 implementation (R1–R4)
Per the ruling: engagement-override table (R1), keyed-coupled refusal branch with
`refusal_reason` + `pending_adjudication` placeholder (R2), adjudicated-category
derivation + `scalar_by_judge`/`scalar_adjudicated` + demotion of judge[0]-only values
(R3), schema updates, and the retro re-tag of the pilot + smoke runs as a NEW dated
analysis file (R4 — mechanical, no live calls; gives the first clean refusal split).
Required test pins are listed in ruling §3.

### W3 — PR-5 backend (directed)
(a) empty-200 retry, capped exponential, N=3 attempts before the cell error; (b)
OpenRouter `provider` preferences + fallback routing. Then a **reliability probe**:
1 cell/design per candidate SUT (and per tie-breaker judge candidate, incl. `x-ai/grok-4`)
before committing the panel roster — the F-2 lesson (qwen died 45/50 silently).

### W4 — M-3: 06/09 matched-quality reference answers (authoring + wiring)
For every DSP-tagged 06 case: reference answers reaching EACH attested conclusion at
matched process quality (7 criteria), FA-1-compliant (no guilt-language forced into
no-dilemma-method answers), playbook-linted (L1–L9, esp. L8/L9). For 09: the expected-
determinations extraction schemas / arbiter-probe anchors per structure. Wire to
`reference_provider` so `assemble_rubric_prompt` carries them. 06/09 scores stay labeled
PROVISIONAL until G5 (neutrality) runs. This is careful authoring work — budget real
session time; two-agent rule applies (author ≠ reviewer).

### W5 — Label tooling (protocol §9)
`label_sample.py` (Part A, seed 20260710, strata per protocol §2, blind CSV + instruction
packets with smoke-drawn anchored examples), `judge_validation.py` (κ table per protocol
§4 incl. `_GOOD`-derived weights, ceilings, AC1 supplement, `--candidates` re-judging
mode, detector P/R from Q-R1/Q-R2), Part B exporter.

### W6 — The ≥6-model full-split panel
Via `run_panel`, full public split (no `--items-per-design`; 344 runnable per PR-1
provisional). Roster: ≥6 frontier cross-vendor SUTs chosen AFTER W3 probes — include
OpenAI + Google + Claude-family SUTs (home-advantage/generator-familiarity analyses are
pre-registered, gate memo §E; both-rows reporting is mandatory), plus deepseek,
mistral-large, meta-llama frontier, grok as probes allow. Judges: `gpt-4.1-mini` +
`gemini-2.5-flash` (provisional pair, §E) + tie-breaker per §E on `needs_adjudication`
cells (own-family exclusion enforced in code). Per-SUT parallel resumable runs, merged
(the pilot pattern). Manifest pins everything incl. capability-battery snapshot; budget
check first (expect tens of dollars; 02/07 dominate wall-clock — F-1).

### W7 — Gate statistics + O4 report
`gates_o4.py`: G1 (max hard-tier H < 0.85), G2 (S-range ≥ 15), G3 (Spearman vs pinned
battery composite, public scores read + cited at run time, permutation p), G6 (BoW
logistic, 5-fold CV vs majority baseline + 10pp), G7 (20% deterministic sample,
name-swap + non-generator paraphrase batteries, flip-rates), G8 statistics (zero-variance
list, judge-noise outliers at median + 2SD), G9/G10 renderer enforcement. Output: the O4
report as a NEW dated file — descriptive gate READINGS, clearly marked "verdicts at O5";
scores marked PROVISIONAL pending G4 (human labels) throughout; 06/09 additionally pending
G5.

### W8 — Wrap
Handoff doc (dated), memory update, atomic commit of WALKWORTHY paths ONLY (≥3 sessions
share the git index — `git log -1` first, stage explicit paths, never rewrite sibling
commits). `runs/*/scored_items.jsonl` stays gitignored; HOLDOUT never in git.

## What this session does NOT do
- No gate verdicts (O5, Fable-preferred), no item edits/kills (O5 per G8), no release
  claims (blocked on Jimmy's labels via G4), no charter-level guesses (PENDING-RULINGS).

## Jimmy owes (unchanged + new)
- Part A labels per protocol §8 wave plan (~25–30 h) + second labeler (or invoke the
  test–retest fallback, disclosed).
- One-liner ratifications: PR-1 (c), PR-2 (ADVICE_SYSTEM), PR-4 (OpenRouter sanctioned),
  PR-3 (as §6.4 interpretation).
- The OpenRouter key remains at `~/.codex/secrets/openrouter.env` (never printed/committed).

## State ledger (post-Fable-adjudication, 2026-07-10)
- Pilot: 150 records, DESCRIPTIVE/PRE-GATE, adjudicated in gate memo §D (7/10 spread≥15
  encouraging; 03 zero-variance = WATCH on proxy scalar; 04/05 ceilings = proxy artifacts;
  02/07 judge agreement 0.43/0.49 = top validity risk → wave-1 labels + escalation ladder).
- Tests 159 green at `418be6c9d`. Frozen: gates (§C), metrics (§B), judge plan (§E),
  label protocol, PR-3 semantics. Open judgment: NONE for this build — everything below
  the line is execution.
