# WCF-Bench — Codex Execution Plan (2026-07-11)

**Audience:** Codex / any coding agent. Read `AGENTS.md` first (rules + environment), then
this plan, then the binding memo `20260711-fable-mvp-disagreement-adjudication-memo.md`
(R42–R46). This plan translates that memo's directives into ordered, bounded tasks.

**The finish line (memorize this):** the benchmark MVP is TESTABLE when all 226 runnable
bank items (204 standard + 22 EPISODE) can be scored end-to-end under a re-qualified
2-family judge panel, with trustworthy score parsing, honest cost accounting, and a
PROOFTEXT scorer that measures the construct. That is Tasks 1–5 below. **Everything not
required for that finish line is out of scope** — see §Out-of-scope.

**Effort calibration:** Tasks 1–3 are small code changes (each well under a session).
Task 4 is the big one (one session incl. live calls). Task 5 is medium. If any task
balloons past its budget, checkpoint and escalate per AGENTS.md rule 2 — do not dig.

---

## Progress (update checkboxes as you go — the ONLY edits allowed to this file)

- [ ] Task 1 — SCORE-parse fix (last-match)
- [ ] Task 2 — disagreement.json display fix
- [ ] Task 3 — cost estimator fix
- [ ] Task 4 — format-bridge + gpt drop + re-qualification → NEW manifest (LIVE, ≤$10)
- [ ] Task 5 — EPISODE live runs, 22 items × 4 SUTs (LIVE, small)
- [ ] Task 6 — PROOFTEXT judge-assisted scorer + persisted re-read (LIVE, small)

Tasks 1–3 are independent of each other; do them first, in any order, commit separately.
Tasks 4 → 5 → 6 are strictly ordered (5 and 6 must run under Task 4's new manifest).

---

## Task 1 — Fix the axis-score parse (R45.4(i)) — CODE ONLY, no live calls

**Why (1 line):** the parser takes the FIRST `SCORE:` match in a judge verdict, so a judge
that shows its arithmetic gets its intermediate numbers recorded instead of its final answer
— one silently corrupted cell in the MVP run.

**What:** in `04-HARNESS/wcfbench/triaxial.py` (~line 275), `_AXIS_SCORE_RE.search(text)`
must become last-match semantics: prefer a **line-anchored final `SCORE:` line**; if none,
take the LAST regex match in the text. Check whether `contested.py`'s numeric parses share
the same first-match pattern; if yes, apply the same fix there.

**Regression fixtures (verbatim, from persisted data — do not paraphrase them):** in
`07-PILOTS/20260710-mvp-run/transcripts.jsonl` find:
1. item_id `WHOLE-C1-004`, model `deepseek/deepseek-chat` → judge `gemini-flash` →
   `verdict_texts[1]`. Contains `Score: 2.5 / 5.0 = 0.5` then final `SCORE: 0.5`.
   Fixed parser MUST return **0.5** (old parser returned 2.5).
2. item_id `MEND-C5-W204`, model `meta-llama/llama-3.1-8b-instruct` → judge `gemini-flash`
   → `verdict_texts[0]`. Contains per-keypoint `*Score: 0.0*` lines then final `SCORE: 0.25`.
   Fixed parser MUST return **0.25** (old parser returned 0.0).

Copy both texts into a test fixture file (they are judge verdicts, safe to commit).

**Done when:** the two fixtures parse to 0.5 / 0.25; the existing tolerant case
(`SCORE: 0.8 out of 1` → 0.8) still passes; full suite green (444 + new tests).
**Do NOT:** rewrite the regex grammar, touch judge prompts, re-score any existing run dir
(immutability — the MVP-run numbers stand as history; R46.1 already adjudicated them),
or hunt for further hypothetical parse edge cases beyond the fixtures.

## Task 2 — disagreement.json display fix (R45.4(ii)) — CODE ONLY

**Why:** the MVP run's 3 worst "disagreements" were artifacts — the spread computation in
`04-HARNESS/wcfbench/disagreement.py` includes off-scale-fenced values and OPEN-ineligible
judges' raws, so real disagreement was buried under noise.

**What:** (a) add `eligible_spread` / `eligible_axis_spreads` computed ONLY over values that
are (i) from judges eligible for that surface (`eligible_surfaces` on the per-judge record)
and (ii) not flagged `scale_defect` for that axis; sort cells by eligible spread (keep the
raw fields — they are evidence, not noise); (b) annotate per-judge values with
eligibility + fence flags in the record; (c) document in the module docstring that
`split_defensible` is CONTESTED-only.

**Done when:** a unit test shows a cell with a fenced 2.5 raw ranking LOW on eligible_spread
while the old max_spread still reports it; suite green.
**Do NOT:** change aggregation/scoring logic anywhere (this is display/records only),
regenerate any existing disagreement.json (immutability), or build visualization tooling.

## Task 3 — Cost estimator fix (R45.3) — CODE ONLY (validation rides Task 4's live run)

**Why:** the estimator undercounts ~10× (models missing from the pricing lookup silently
contribute $0), so the `--budget` cap guards a fiction.

**What:** in `04-HARNESS/wcfbench/openrouter_client.py` + `mvp.py` cost paths:
(a) prefer authoritative per-request cost when OpenRouter returns it (response `usage` /
generation accounting); (b) where the catalog-pricing path is used, a missing/blank price
**raises** (fail-loud) instead of contributing 0; (c) the `--budget` cap enforces against
`max(estimate, actuals-to-date)`; (d) every run report prints an internal-total vs key-side
reconciliation line (key-side from `GET /api/v1/auth/key` usage delta).

**Done when:** unit tests cover (b) and (c) with mocked responses; suite green. Acceptance
(±20% vs key dashboard) is checked on Task 4's live run — one reconciliation line in that
report, not a measurement project.
**Do NOT:** build a pricing cache/database, backfill historical run costs, or block on
OpenRouter API quirks — if the actuals field isn't available on some responses, fall back
to fail-loud pricing and note it in the handoff.

## Task 4 — Format-bridge + panel change + re-qualification → NEW MANIFEST (R43 + R44) — LIVE, cap $10

**Why:** the OPEN award surface is single-family (gemini only) — its scores carry one
judge's idiosyncrasies with no cross-check. The format-bridge (a few-shot exemplar showing
the award FORM) is the authorized last attempt to qualify a second family. Simultaneously,
gpt-4o-mini is ruled OFF the panel (R43).

**Order of operations (one manifest event — do not split):**

1. **Author the exemplar** (R44.1): a worked example demonstrating the award form —
   `KPn: award|deny — reason, "verbatim quote"` lines + a final line-anchored `SCORE:` —
   embedded in the OPEN-award judge prompt. Constraints (all binding): built from a
   **non-bank, non-holdout** item (write a fresh neutral mini-scenario or reuse a retired
   dev fixture from `probe_fixtures.py`; it must overlap NO bank item's content);
   theologically neutral; canary-free; frozen into `probe_fixtures.py`; included in the
   template hash (`qualification.current_template_hashes`).
2. **Drop gpt-4o-mini** from the panel roster/config. No gpt re-qualification. Its raws in
   existing run dirs stay untouched.
3. **Re-qualify the panel** (R44.2): `qualification.qualify_judge` K=8, ≥5/8 per surface,
   for **gemini-flash and grok-4.20 on ALL their surfaces** under the new template hashes.
   Existing probe fixtures unchanged.
4. **Re-screen exactly three OPEN-award candidates** (R44.3): `x-ai/grok-4.20`,
   `cohere/command-a`, `amazon/nova-pro` — OPEN-award battery (award-consistency +
   discrimination) under the bridged template. **The discrimination bar is NOT relaxed.**
   Also run the K=8 coherence battery for cohere + nova on the same run (cheap, rides along).
5. **Write the new manifest + report:** new dated pilot dir `07-PILOTS/20260711-*/`,
   combined qualification manifest JSON (this SUPERSEDES
   `20260710-settled-requal-manifest.json` as manifest of record), and a short dated report
   with the K=8 pass/fail table per judge × surface.

**Pre-flight:** key check per AGENTS.md. Budget cap **$10** hard (expected $3–8).
**Done when:** new manifest exists and loads via `JudgePanel(manifest=)`; report written;
suite green (mock-first tests for the exemplar-in-prompt path + roster change).
**Outcome handling (both outcomes are success — do not iterate):**
- ≥1 non-google family passes OPEN-award → record it; OPEN aggregation becomes ≥2-family.
- Zero pass → OPEN stays single-family-labeled and **the candidate ladder is CLOSED**
  (R44.5). Do NOT try other models, tweak the exemplar and re-run, or widen K. Record the
  table and move to Task 5.
**Do NOT:** reword any prompt beyond inserting the exemplar block; re-qualify gpt; screen
any candidate not named above; exceed K=8; touch bank YAML.

## Task 5 — EPISODE live runs (R45.2) — LIVE, small (~88 cells)

**Why:** the 22 NARROWGATE items were excluded from the MVP run (they need the episode
state-machine, `wcfbench/episode_live.py`); running them completes bank coverage 204→226.

**What:** run the 22 EPISODE items × the same 4 SUTs
(meta-llama/llama-3.1-8b-instruct, deepseek/deepseek-chat, mistralai/mistral-large-2512,
anthropic/claude-haiku-4.5) under **Task 4's new manifest**, into a new dated run dir:
per-(item,SUT) checkpoint/resume, per-cell error survival, full transcripts, disagreement
records, refusal taxonomy, budget cap (set $10; expect far less), and a short dated report
labeled **DESCRIPTIVE / PRE-GATE** with the single-family caveats exactly as the MVP-run
report does (adjusted for Task 4's outcome).

**Done when:** all 88 cells scored or their errors recorded per-cell (a stubborn cell after
the standard retry = a recorded error, not a debugging project); report written; suite green
if any harness code was touched.
**Do NOT:** re-run the 204 standard items (the MVP run stands; a full-bank re-run under the
new manifest is a Jimmy decision — note it in the handoff as available-on-request, ~$15);
modify episode logic to make a model pass; add SUTs.

## Task 6 — PROOFTEXT judge-assisted scorer + persisted re-read (R45.1) — LIVE, small

**Why:** PROOFTEXT scores 0.03–0.34 for ALL SUTs because the citation-token scorer only
credits literal anchor tokens (models reason correctly without writing "Q136") — an
artifact, not a finding. The judge-assisted correct-use path (`judge.judge_score_anchor_use`
— already built) is the fix; PROOF numbers are unquotable until it lands.

**What:** (a) wire `judge_score_anchor_use` into the PROOF scoring path as the primary
scorer, keeping the citation-token score as a side-by-side column; UNGRADED (surfaced,
never silent 0) when the judge declines/unparseable; judge eligibility + disagreement
records as on other surfaces. (b) Hermetic tests: a paraphrased-anchor-use fixture the
token scorer false-negatives on (build it from a real MVP-run PROOF transcript) + a
no-anchor-use fixture that must still score low. (c) **Persisted re-read:** re-grade the
MVP run's PROOF responses (23 items × 4 SUTs, stored in
`07-PILOTS/20260710-mvp-run/transcripts.jsonl` + checkpoint — **no new SUT calls**, judges
only) into a NEW dated run dir, reporting old-vs-new per-SUT deltas.

**Done when:** tests green; re-read report written with the delta table. Expected: floors
rise materially. If a SUT's PROOF floor does NOT rise, **record it as a real finding in the
report and STOP** — diagnosing it is adjudication (Jimmy/Fable), not agent work.
**Do NOT:** edit PROOF bank items or anchors; tune the judge prompt to move scores; re-read
any non-PROOF design.

---

## Out of scope — do NOT work on these, whatever you notice along the way

| item | why it's parked |
|---|---|
| G6 confessional panel, human labels, rater tooling | Jimmy recruits raters; agent work ends at readiness |
| Gated G1–G7 measurement run, H-DISC promotion, W304/W305 position maps, 4 LIB `[DISPUTED]` legs | all G6-gated |
| Full-bank re-run under the new manifest | Jimmy decision (cost); note availability in handoff |
| Perturbation battery P1–P6 at scale | post-MVP, needs its own directive |
| Bank item edits, new items, transcription work | bank is frozen at 230/230, audited |
| Refactors, dependency upgrades, test-suite reorganization, CI, tooling | working harness; smallest-change rule |
| Re-scoring / regenerating anything in `07-PILOTS/` | immutability — history is append-only |
| Investigating judge/model behavior beyond a task's spec | sample-level adjudication is a Fable/Jimmy activity (R-chain) |
| New judge candidates beyond Task 4's three | R44.5: zero-pass closes the ladder |

## Escalation

Append to `PENDING-QUESTIONS.md` (create it on first use): date, the question, which task
it blocks, your one-line suggested default. Then take the most conservative compliant path
(or skip the sub-item) and keep moving. Questions that belong there: anything requiring a
new decision, ruling reinterpretation, budget beyond a cap, roster/scope changes, or a
Task-6 non-rising floor. Questions that do NOT belong there: anything answered by this plan,
AGENTS.md, or R42–R46.

## Definition of DONE for the whole handoff

All six checkboxes ticked (or explicitly blocked with a PENDING-QUESTIONS entry), suite
green, each task committed separately with explicit pathspecs, and a final dated handoff
(`YYYYMMDD-codex-session-handoff.md`) stating: manifest of record, Task 4 outcome
(2nd family or ladder-closed), EPISODE + PROOF-re-read locations, reconciled spend, and the
one-line status "MVP testable: yes/no + why". At that point WCF-Bench's remaining queue is
entirely human-gated (G6) and the benchmark is ready for its first externally-visible test.
