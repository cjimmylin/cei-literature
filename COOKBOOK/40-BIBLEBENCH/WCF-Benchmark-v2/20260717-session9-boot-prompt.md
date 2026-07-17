# WCF-Benchmark-v2 — Session 9 Boot Prompt (REPORTING session)

> Paste as the opening prompt of a fresh session. Self-contained. Read
> top-to-bottom before touching anything. This is a **collaborative reporting
> session** — the owner will bring the specific scope in-session. Do NOT start
> writing a deliverable until Phase 0 (scope-lock) is done.

## Mission

**Expand and describe the reporting.** Sessions 1–8 built the
Christian-Ethics-Benchmark-v2 (WCF-Bench-v2) and produced a stack of per-session
reports; session 8 added the OAuth meta-judging audit and the minimax epochs
addendum. The next step the owner wants is a **richer, more descriptive report**
that expands on what already exists. The EXACT shape (audience, scope, which
findings to foreground, format) is **owner-defined in-session** — this prompt
loads all the state so we can align fast and then write, not rediscover.

**Working posture:** we write together. Fable/Opus in the main loop does the
narrative synthesis and adjudication; delegate mechanical pulls (number
extraction, log reads, figure data) to cheaper tiers. No new benchmark runs are
implied by "reporting" — treat any live OpenRouter spend as needing explicit
owner OK (same rule as s8).

## Phase 0 — LOCK SCOPE WITH THE OWNER FIRST (do not skip)

Before writing anything, get these four answers from the owner (ask as a tight
batch; offer the candidate menu below as defaults):

1. **Deliverable type** — which of:
   - (a) **Consolidated WCF-v2 story** — one narrative from v1-bespoke-harness →
     Inspect port → bank v2.0–v2.4 → the judging-validity audit; the "what we
     built and what we learned" arc.
   - (b) **Judging-validity paper/section** — deepen the s8 meta-judging report
     into a standalone methods+results writeup (house-style, 5-judge
     reliability, headline sensitivity, kin DiD, contamination bound).
   - (c) **Leaderboard + frontier-core report** — the model-comparison story
     (tier-1 three-way cluster, gpt-5-mini/minimax/qwen vs haiku, the frontier
     core as an instrument), foregrounding results over methodology.
   - (d) **Something else the owner specifies.**
2. **Audience & register** — internal research memo / external-facing writeup /
   academic manuscript section / owner-briefing deck. (Sets voice + how much
   methodology to expose.)
3. **Scope of inputs** — s8 only, or the full s1–s8 arc? (Determines how many
   prior reports to fold in — see the report inventory below.)
4. **Format & length** — single markdown report / multi-section / PDF (fpdf2 or
   Typst per vault rule — NO LaTeX/Pango) / slides. Target length.

Only after these are answered: draft an outline, get owner sign-off on the
outline, THEN write. (Reporting sessions fail by writing before the shape is
agreed.)

## Where things stand (as of 2026-07-17, commit `500d03c2999a…`, 0 unpushed)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (all paths
  relative). Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14; the shared
  vault `.venv` is 3.9 and CANNOT run inspect-ai). `export
  OPENROUTER_API_KEY=dummy` suffices for reading logs / running the compute
  scripts — a reporting session needs NO live calls. **80 tests green.**
- **Bank v2.4** (`data/BANK-VERSION.json`): 265 main (199 v1 + 29 s6 + 37 s7) +
  22 episodes; frontier core = 66 `-N-` items. Panel = median of gemini-2.5-flash
  + deepseek-chat + mistral-small-2603; last-match `GRADE: N` parser; excellence
  gate ON (main); grader retry wrapper `GRADER_ATTEMPTS=3`.
- Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel sessions.
  Commit with **explicit pathspecs**; leave sibling staged/stash alone.

## Session-8 deliverables (the primary things we're expanding)

- **Meta-judging report** `reports/20260717-session8-meta-judging-report.md`
  (8-section skeleton) — generated FROM `analysis/20260717-session8-meta-judging-stats.json`
  by `analysis/session8_render_report.py` (edit the renderer, not the .md, if
  numbers change — every table + the CI-verdict are data-derived).
- **Minimax addendum** `reports/20260717-session8-minimax-epochs-addendum.md`
  ← `analysis/20260717-session8-minimax-core-stats.json` (compute script
  `analysis/compute_session8_minimax_core.py`).
- **Raw grade ledgers** (resume-safe JSONL, all validated 0-malformed):
  `analysis/20260717-session8-j4-raw.jsonl` (779 unique / 997 records),
  `…-j5-raw.jsonl` (562), `…-j4-contamination-raw.jsonl` (21),
  `…-replay-rows.jsonl` (779 replay rows w/ mold+stratum+panel), smoke raws +
  `analysis/20260717-session8-smoke/` transcripts.
- **Compute + grade scripts:** `session8_extract_replay.py`,
  `session8_grade.py` (J4 `claude -p`, J5 `codex exec`),
  `session8_contamination_prep.py`, `compute_session8_meta_judging.py`,
  `session8_render_report.py`, `compute_session8_minimax_core.py`.
- **Live eval log:** `logs/20260717-session8-minimax-epochs-core/` (198 samples,
  status=success).

## Key findings to carry into the expanded report (do not re-derive)

Meta-judging (J4 = claude-opus-4-8 via Claude OAuth; J5 = gpt-5.5 via Codex
OAuth; both replayed the persisted GRADE-FREE grading prompt → anti-leakage by
construction; explicit-tell scan 0/779; zero parse-fails across 997+562 calls;
$0 OpenRouter). ALL EXPLORATORY / NON-QUOTABLE; OAuth judges are AUDIT
instruments, never in panel/leaderboard.

1. **Headline survives + strengthens.** gpt-5-mini − haiku on the 66-core,
   epochs-averaged: panel-3 **5.90** (MDD80 5.41 SIG) → J4 alone **19.65**,
   J5 alone **14.55**, 5-judge median **9.25** (MDD80 5.62 SIG). Sign positive
   in all 7 configs; both OAuth judges see a LARGER gap → the incumbent panel is
   **conservative**, not inflationary. Single-judge rows are **gap-stability
   only** (MDD80 ~8–10 lacks power — no single-judge SIG/ns claims; this was a
   pre-stated rule and an adversarial-review BLOCKER we fixed).
2. **No kin favoritism — and a load-bearing caveat.** Cross-kin DiD τ̂ = −5.10,
   item-clustered bootstrap CI [−9.27, −1.09]; epoch-1-only robustness −6.29
   (same sign). BUT τ̂ **collapses algebraically to d̄_haiku − d̄_gpt5mini** (the
   qwen anchor cancels) → read DIRECTIONALLY, not as a significance test; it
   conflates kin bias with any judge-pair × SUT interaction and rests on ONE
   twin-difference instrument. Any expanded write-up MUST preserve this framing.
3. **5-judge reliability:** ICC(2,k) overall 0.798 (complicit 0.847 / contested
   0.612 / steadfast 0.557); J4~J5 ρ=0.849 MAD 9.2 (the two OAuth judges agree
   closely — a cross-vendor concordance worth a figure).
4. **House-style mechanism:** J4/J5 are far harsher than the panel on complicit
   (−26/−16) and steadfast (−34/−40) molds, near-panel on v1-kind — this
   mold-specific harshness is WHY a stricter judge widens the gap (ordering
   robust; calibration is not). Good candidate for a heatmap.
5. **Discriminators real, not artifact:** top-10 s7 discriminators' spread
   persists 9/10 under J4, 10/10 under J5, 0/10 collapse.
6. **Contamination bound small:** style-normalized re-grade (n=21) mean Δ −0.95,
   mean |Δ| 6.95.

Minimax addendum (live run, owner-authorized): **minimax-m3 79.63 (SE 1.60) vs
gpt-5-mini 78.39 → gap +1.24, MDD80 5.78, ns** — s7's single-draw 80.45 lead
DISSOLVES under comparable epochs. minimax−haiku +7.14 SIG; minimax−qwen +4.30
ns. **Tier-1 = 3-way top cluster** (minimax ≈ gpt-5-mini, both clear haiku;
qwen a half-step below). 0/198 unscored.

Recommendation already on record (s8 §8): keep the panel-3 median for v2.5+;
don't merge OAuth judges into the panel; no kin-exclusion rule needed for the
current SUT set.

## Full report inventory (for scope option (a)/(c) — the s1–s8 arc)

`reports/` (chronological): live-smoke + full-pass (s1–2) · session3 report +
streamA/B/C · session4 report + 5 critiques + adjudication + edit-log · session5
report + triage + fable-rereads + v22-design · session6 report + authoring-brief
+ roster-leaderboard + scaleup-runbook · session7 report + authoring-brief +
review-adjudication · `20260716A-Report.md` (post-hoc category/discrimination) ·
**session8 meta-judging report + minimax addendum**. Baseline stats JSONs in
`analysis/` (streamB agreement, s5 panel-health + kin-stats, s7 epochs-stats,
s7 gemini-kin-did, etc.) — cite, don't recompute.

Cross-session memory (loaded each session): the `wcf-v2-inspect-build` topic
file carries the running s1–8 narrative + all gotchas; read it before writing so
the report's history section is accurate.

## Binding conventions (do not relitigate)

1. **Report immutability:** NEW dated files only (`YYYYMMDD-…`); never edit an
   existing dated report/JSON. No deletions (`mv` to `RECYCLE-BIN/`). Never
   modify `../WCF-Benchmark/` (v1) or `../Christian-Ethics-Benchmark*/`
   (read-only references).
2. All WCF-v2 judging results are **EXPLORATORY / NON-QUOTABLE** (rubric
   conformity, not accuracy). OAuth judges = audit instruments only; their
   numbers never sit in a leaderboard-style table with panel rows without an
   instrument-difference banner.
3. **$0 OpenRouter** unless the owner explicitly authorizes a run; OAuth usage
   is subscription (concurrency-one + backoff on codex, ≤4 workers on claude,
   no unattended overnight loops).
4. **Number fidelity:** the s8 reports are generated FROM stats JSON — keep that
   discipline (edit the renderer, re-run, don't hand-transcribe). If the
   expanded report is hand-written prose, cross-check every number against the
   JSON before commit (an automated presence-check script is the cheap way).
5. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every Agent
   dispatch; narrative synthesis + adjudication stay in the main loop, mechanical
   pulls go to Opus/Sonnet subagents.
6. Git: commit with explicit pathspecs on shared trunk; `git pull --rebase
   --autostash` → push → `git rev-list --count origin/main..HEAD` = 0. No
   handoff docs (retired 2026-07-15) unless explicitly requested.
7. PDF (if the deliverable is a PDF): fpdf2 or Typst only — NO LaTeX/Pango.

## Gotchas (carry-forward)

- `read_eval_log(f, header_only=True)` — no `read_eval_log_headers` in 0.3.246.
- `claude -p --output-format json` (CLI ≥2.1.183) emits an ARRAY of events —
  pull the `type=="result"` event for `.result` + `.modelUsage`.
- Single-draw vs epochs-averaged means are NEVER comparable — the minimax
  addendum exists precisely to fix an s7 instance of this.
- τ̂ anchor-cancellation (finding 2 above) is the single most important framing
  trap — a genuine kin effect could be masked by / masquerade as a generic
  judge×SUT interaction; the current design cannot separate them.
- zsh: quote `echo "===="` (=cmd expansion); argparse eats leading-dash option
  values → use `--flag=-value`.

## Acceptance checklist (fill in once scope is locked)

- [ ] Phase-0 scope locked with owner (deliverable type / audience / input scope
      / format+length); outline signed off BEFORE drafting.
- [ ] Expanded report written to a NEW dated file; every number cross-checked
      against the source stats JSON (or generated from it).
- [ ] EXPLORATORY/NON-QUOTABLE + OAuth-audit-instrument framing preserved;
      τ̂-directional caveat intact; single-judge rows carry no significance.
- [ ] If any figure/PDF: built with fpdf2/Typst; data pulled from stats JSON.
- [ ] $0 OpenRouter confirmed (or owner-authorized spend disclosed).
- [ ] Memory updated (`…/memory/20260715-wcf-v2-inspect-build.md` + MEMORY.md
      line); pathspec commit → rebase → push → 0 unpushed.
