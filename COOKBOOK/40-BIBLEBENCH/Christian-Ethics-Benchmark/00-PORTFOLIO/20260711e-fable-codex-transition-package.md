<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Codex O5 Transition Package (mechanical execution plan)

**Issued:** 2026-07-11, Fable transition-prep session. **Executor:** Codex (or any coding
agent). **Judgment content: ZERO** — every decision is pre-made in
`20260711d-fable-o5-decision-framework.md` (FR-1…FR-15, §3 branch table, §4 release
formula, §6 stop-triggers) and the frozen `20260710-fable-gate-prereg-pilot-adjudication.md`
(§B/§C/§E). If a situation is not covered by those documents, it is a STOP-AND-ASK-JIMMY,
not a judgment call.

**Read order:** `AGENTS.md` → this package → framework (`…d`) → validity review (`…c`) →
frozen gate memo → human-label protocol → PR-3 ruling → PENDING-RULINGS.

Conventions: `PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`;
run from `harness/`. Verify every module CLI with `--help` before first use — flags below
were read from source on 2026-07-11 but you confirm. OpenRouter key:
`~/.codex/secrets/openrouter.env` (never print/commit). All live calls inherit
`DEFAULT_MAX_TOKENS = 32768` (keep the cap — 402-reservation gotcha, AGENTS.md).

---

## Phase 0 — Pre-flight (every session)

```bash
cd <ROOT>/harness
git log -1                                  # shared index: know HEAD before staging anything
$PY -m pytest tests/ -q                     # must be 261+ green before and after any change
```
1. Verify PR-5(a) empty-200 retry and (b) provider preferences exist in
   `walkworthy/openrouter_backend.py`; implement (b) per the PR-5 direction if absent (TDD).
2. Dry-run G4 turnkey: build a tiny MOCK labels dir matching the blind-CSV format and run
   `$PY -m walkworthy.judge_validation --labels <mockdir> --out /tmp/g4-dryrun --date 20260711`
   — confirm it joins, computes κ per protocol §4, and renders. Fix mechanics only.
3. Confirm `labels/20260710-partA/*-partA-blind.csv` are byte-identical to git HEAD
   (nobody touches Jimmy's blind files; labels arrive as NEW files or Jimmy's own edits).

## Phase 1 — Label-free builds and runs (do all of this before labels land)

All new modules TDD (RED→GREEN), fixture-pinned, no live call in the suite. Estimated
live spend for all of Phase 1: well under $30 (tie-breaker ~609 re-judgings; G5 ~a few
hundred; G7 ≈ 0.4 × panel-equivalent on 20% samples). Precede each live stage with a
1-cell reliability probe (PR-5 direction).

**W1 — Tie-breaker adjudication (FR-2 granularity; unblocks 02/04/07/09).**
- Probe `x-ai/grok-4` (1 cell/design). Passes → tie-breaker = grok-4 (no own-family
  exclusions: x-ai has no SUT). Fails → `mistralai/mistral-large-2512`; mistral-SUT
  pending cells are own-family-excluded → Part-B export (framework §6 trigger 8 if that
  exceeds 10% of a design's pendings).
- New module (e.g. `walkworthy/tiebreak.py`): reads `runs/20260711-o4-panel/scored_items.jsonl`,
  selects `refusal_tag == "pending_adjudication"` records, re-judges ONLY the disagreeing
  turn/seat/criterion units with the tie-breaker (same rubric text the pair received),
  adjudicates 2-of-3, writes a NEW derived run dir (`runs/20260711-o5-tiebreak/`) —
  original run records immutable. Own-family exclusion enforced in code, tested.
- Acceptance: every one of the 609 pending records resolves to adjudicated-or-PartB;
  counts per design × model logged.

**W2 — §E judge Δ(J) home-advantage test (validity review V-3; frozen spec §E).**
- New module (e.g. `walkworthy/home_advantage.py`): per judge J × design, Δ(J) =
  mean[score_J − score_other] on J's own-family-SUT cells vs all other cells; permutation
  test 10,000 resamples; flag at α = 0.01. Runs offline on existing records.
- On a significant flag: J is disqualified for own-family cells on that design → those
  cells route to other-judge + tie-breaker (FR-7), disclosed. Mechanical.

**W3 — Post-adjudication recompute.**
- Recompute all §B stats + G1/G2/G3/G8 readings on post-W1 adjudicated cells; render a
  NEW dated readings file via `$PY render_o4_report.py --run 20260711-o5-tiebreak … --out
  00-PORTFOLIO/<YYYYMMDD>-o5-postadjudication-readings.md` (pass `--judge1/--judge2/
  --classifier/--tiebreaker` EXPLICITLY — panel.py/render defaults ≠ frozen pair, FR-12).
- Must publish: exclusion FRACTIONS with §B S-unit denominators (V-2 table), FR-1
  completeness status per design, PR-6 strict-identity sensitivity rows (FR-10), the
  08/09 identical-ranking assertion (V-13).

**W4 — G5 driver (06/09 neutrality; frozen §C G5).**
- New module: for every DSP-tagged case, each judge blind-scores the matched
  opposite-conclusion reference pair; violation = any rubric category differing > 0.5;
  one violation → one fresh re-elicit; persistent → judge DISQUALIFIED for that design →
  FR-8 cascade. References must pass playbook lint (FA-1) first — a lint failure is
  STOP-AND-ASK, not a fix.

**W5 — G7 batteries (frozen §C G7; FR-14).**
- Sample: deterministic first-20%-by-id per design, stratified easy/hard. Battery (i)
  name-swap from L7 rotation lists; (ii) paraphrase authored by
  `mistralai/mistral-large-2512` (FR-14; lint L1–L9; disclosed as also-a-SUT). Perturbed
  cells run against all 6 SUTs, judged by the frozen pair, adjudicated incl. W1 path.
- Flip = adjudicated load-bearing outcome changes for the same (item, model). PASS iff
  flip-rate ≤ 10% per design. Items with > 1/3 of models flipping = "affected items" —
  LIST them for revision; the surface revision itself happens only after Jimmy sees the
  list (keys untouched, logged).

## Phase 2 — G4 per label wave (waves: 1 = {02,07,01}, 2 = {03,04,05,06}, 3 = {08,09,10})

When a wave's filled CSVs (+ second-labeler overlap or Jimmy's declared test–retest) land:
```bash
$PY -m walkworthy.judge_validation --labels labels/20260710-partA/ \
    --out 00-PORTFOLIO/<YYYYMMDD>-g4-wave<N>-report.md --date <YYYYMMDD>
```
- Apply framework §3 row-by-row per design. One-judge-fail → escalation:
  `--candidates <model>` re-judges ONLY that design's Part-A units (FR-12 hygiene: the
  candidate ≠ `openai/gpt-5.6-terra`, always cross-family, pinned in the report).
- Prevalence-paradox row, low ceiling, test–retest disclosure → exactly as §3 says; the
  first two are STOP-AND-ASK.

## Phase 3 — Verdict assembly and the O5 report

- Part-B export for residual contested cells → `labels/<design>-partB.jsonl` (protocol §6),
  worked worst-designs-first (02/07).
- Apply the framework §4 release formula per design; emit the O5 gate-adjudication report
  as a NEW dated file (`00-PORTFOLIO/<YYYYMMDD>-o5-gate-adjudication.md`): per-design
  verdict + status from the §4 vocabulary, G8 kill/demote item lists (FR-13), G9
  headlines incl. nulls, §6.1 readouts (per-area, per-method, worst-area, contested-tier
  separate), both home-advantage rows + Δ(J) results, all disclosures (FR-3 collinearity,
  FR-10 sensitivity, FR-14, test–retest if used), and the Jimmy sign-off checklist
  (framework §7). **The report recommends; Jimmy releases.**

## Guardrails (verbatim obligations — violating any of these is the failure mode)

1. **Frozen means frozen.** Never edit §B/§C/§E text, thresholds, κ forms, or this
   framework's FR rules. Data disagreeing with a rule → STOP-AND-ASK.
2. **No unlicensed verdicts.** Never assert a gate verdict, item kill, demotion, release,
   or refusal-accounting claim that the framework + actual label outcomes do not license.
   Descriptive ≠ verdict. Release is Jimmy-only, always.
3. **Never delete** (`rm`/`unlink`/`find -delete`/`git clean`) — `mv` to `RECYCLE-BIN/`.
4. **Report immutability.** Every output is a NEW `YYYYMMDD-` file. Never regenerate
   `20260711-o4-panel-report.md` or `20260711b-o4-panel-report.md`.
5. **HOLDOUT is never loaded** (loader hard-refuses; keep it that way), never committed.
6. **Shared git index** (≥3 sessions, one worktree): `git log -1` before staging; stage
   explicit WALKWORTHY pathspecs only (never `git add -A`); never rewrite sibling
   commits; fast-forward pushes only. `runs/*/scored_items.jsonl`, `*-DRAFT.md` gitignored.
7. **Model hygiene:** judges/classifier/tie-breaker ALWAYS passed explicitly (defaults in
   `panel.py`/`render_o4_report.py` do NOT match the frozen §E pair); escalation judge ≠
   state classifier; OpenRouter max_tokens cap stays.
8. **TDD everything;** suite green before and after; no live calls in tests.
9. **FIX-MECHANICS-ONLY:** no item is edited from model performance; G7 "affected items"
   are listed, not edited, until Jimmy reviews.
10. Blind label CSVs are Jimmy's — never modify, reorder, or "fix" them.

## Paste-ready Codex boot prompt

```
You are Codex executing WALKWORTHY session O5 (mechanical; zero judgment). Work ONLY in
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Read, in order:
AGENTS.md; 00-PORTFOLIO/20260711e-fable-codex-transition-package.md (your execution
plan); 20260711d-fable-o5-decision-framework.md (pre-made decisions FR-1..FR-15, branch
tables, release formula, STOP-AND-ASK triggers); 20260711c-fable-o4-validity-review.md;
20260710-fable-gate-prereg-pilot-adjudication.md (§B/§C/§E — FROZEN, never edit);
20260710-human-label-protocol.md; 20260710-fable-PR3-ruling.md; PENDING-RULINGS.md.
Then execute the package phases in order: Phase 0 pre-flight; Phase 1 (W1 tie-breaker →
W2 Δ(J) → W3 recompute → W4 G5 → W5 G7 — all label-free); Phase 2 G4 per label wave IF
filled label CSVs exist (if none, stop after Phase 1 and report O5-blocked-on-labels);
Phase 3 verdict assembly strictly via the framework §4 formula. Obey every guardrail in
the package verbatim (no deletes; report immutability; HOLDOUT never loaded; explicit
judge models; explicit git pathspecs; TDD). Anything not covered by the framework →
append to PENDING-RULINGS and stop that thread; never guess. End with a NEW dated
handoff + commit + fast-forward push of WALKWORTHY paths only.
```

*No item is edited from model performance anywhere in this package (FIX-MECHANICS-ONLY).*
