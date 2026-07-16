# WCF-Benchmark-v2 — Session 5 Boot Prompt

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

**Assess the session-4 pilot at item level, measure the grader kin-delta, and design —
and cheaply validate — the v2.2 discrimination upgrade, BEFORE any roster expansion.**
The session-4 pilot proved the bank is saturated at the frontier: adding more models now
would pile them into an unresolvable tier-1 blob at ~$2/model of spend that answers
nothing. Session 5 spends on measurement and validation only. **Explicit non-goal: NO
roster expansion in session 5.** Session 5's terminal deliverable is a session-6 scale-up
runbook with go/no-go criteria.

Owner decisions locked (2026-07-16): (1) the eventual scale-up NEEDS google/deepseek/
mistral-family SUTs → the kin-delta measurement is MANDATORY this session; (2) new-item
authoring is decided AFTER the item triage, not before; (3) budget ceiling $10, same
autonomous-run rule.

## Where things stand (as of 2026-07-16, session-4 close, commits `7d77951ef` + `15bb722e7`)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (paths below relative to it).
- Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14; the shared vault `.venv` is 3.9
  and CANNOT run inspect-ai). API key: `set -a && source ~/.codex/secrets/openrouter.env && set +a`.
- **Bank (v2.2-pending): 199 main + 22 episodes** — session 4 quarantined 5 turn-conditioned
  items and patched rubrics via the converter patch layer `convert/session4_patches.py`
  (source YAML `../WCF-Benchmark/05-BANK-YAML/` READ-ONLY, untouched). Per-item audit log:
  `reports/20260716-session4-item-edit-log.md`. Kind mix now: open 156 / anchor 23 /
  ordinal 16 / contested 4 (+ 22 episodes).
- **Pipeline (fixed in s4):** last-match word-boundary grade pattern with 4-digit reject;
  SUT-answer marker defanging (injection chain closed); 0–100 out-of-range → unscored;
  `panel_median` reducer in `src/wcf_grading.py`; episode grading uses
  `src/templates/wcf_grade_template_episode.txt` (`[BEGIN TRANSCRIPT]`). 44 tests green
  (`.venv-v2/bin/python -m pytest tests -q`; imports need `export OPENROUTER_API_KEY=...`,
  dummy value fine for tests).
- **Pilot results (5 SUTs × 221 items, median-of-3 panel, v2.1 per-item pressure,
  unscored 0/1,105):** TWO tiers — qwen3.7-plus 96 ≈ claude-haiku-4.5 95 ≈ kimi-k2-0905 94
  (all adjacent t<2, NS) ≫ llama-4-maverick 80 ≈ gpt-4o-mini 78 (tier break t=8.27).
  **Ceiling: 72–77% of items at exactly 100 for tier-1.** Episodes discriminate (tier-1:
  zero sub-50 in 66 samples; 4o-mini folds 11/22) while the open kind saturates.
  Session-3's "qwen>haiku resolved" did NOT reproduce panel-native (t=1.88 NS).
- **Panel provenance (new s4 capability):** every pilot sample's Score carries
  `metadata['panel'] = {'n_valid': k, 'values': [...]}` — per-grader analysis is possible
  FROM LOGS ALONE, no re-runs. 5 samples degraded to n_valid=2 (grader failure):
  4o-mini/AGG-C5-004, 4o-mini/STED-C1-W201, 4o-mini/WHOLE-C8-W306, haiku/PROOF-XC-W206,
  qwen/NARROW-C6-009.
- **Panel-collision ruling (s4 adjudication §1):** validated panel (gemini-2.5-flash +
  deepseek-chat + mistral-small-2603) kept; pilot roster was kin-free; **kin-delta was
  DEFERRED and is now due** — no run anywhere in the vault has ever graded a deepseek or
  mistral SUT under the panel.
- Key artifacts: `analysis/20260716-session4-pilot-stats.json` (full numeric pack),
  `logs/20260716-pilot/{main,episodes}/` (10 evals), `reports/20260716-session4-report.md`
  (+ adjudication memo + 5 critique files `reports/20260716-session4-critique-0*.md`),
  stored session-3 responses for deepseek-chat and mistral-large-2512 in
  `logs/20260715-sut-sweep/` (8 evals, 4 SUTs × {main,episodes}, single-grader config).
- Spend history: s3 ~$5.01; **s4 $10.32 (~3% OVER the $10 ceiling** despite an $8.3–8.8
  forecast; drivers: qwen reasoning tokens + anchor-text-enlarged grading prompts).
  Forecast conservatively this session; snapshot `GET api/v1/credits` before/after
  (delta is an upper bound — concurrent same-key vault sessions exist).

## Work plan — assessment first, spend last

### Phase 1 — $0 item-level assessment (parallel agents: sonnet extraction, opus analysis)

1. **Item triage** over the 1,105 pilot samples (join session-3 sweep logs where useful,
   flagging the config break): per-item cross-SUT spread, item–total correlation,
   within-tier-1 separation, per-item panel disagreement (from `metadata['panel'].values`).
   Classify EVERY item {DEAD-CEILING (=100 for all tier-1) / CORE-DISCRIMINATING /
   NOISY (panel spread dominates) / TIER-BREAK-ONLY}, with counts by kind and a full table
   written to `analysis/` (dated). Session-4 critique-01 estimated ~28 stable frontier
   separators on the OLD bank — produce the v2.2-pending equivalent.
2. **Discrimination anatomy:** where does separation live (kind × design × main-vs-episode)?
   Quantitatively confirm/refute "episodes are the discrimination engine."
3. **Panel health from metadata:** per-grader value deltas by kind/family; does gemini's
   harsh-outlier profile (s3: −8.6 mean) persist on the patched bank? Any new lone-outlier
   pattern? Zero re-runs — logs only.
4. **Fable-tier re-reads (main loop, no dispatch — queued from s4):** (a) the 23
   diffuse-disagreement items (critique-01 category G): genuinely-hard-ethics vs latent
   rubric ambiguity — decides how much of the 25% "hard ethics" share is real; (b) anchor
   recall-boundary confirmation (critique-04 escalation) guarding the "0 contaminable
   items" claim.

### Phase 2 — kin-delta measurement (MANDATORY, ~$1–2)

Re-grade the stored session-3 **deepseek-chat** and **mistral-large-2512** responses
(226 each) via the verified replay method — the persisted grading prompt lives in
`scores['model_graded_qa'].metadata['grading'][0]['content']` and is verified grade-free
(anti-leakage by construction; recipe in
`METHODS/20260715-wcf-v2-inspect-build-operational-methods.md` and
`analysis/regrade_graders.py`) — under:
(a) the default panel (gemini + deepseek-chat + mistral-small-2603), and
(b) a kin-free substitute panel: keep gemini, swap the two kin graders for 2 graders from
    families that are neither current SUTs nor plausible session-6 roster entries
    (candidates: amazon nova / cohere / microsoft phi — verify slugs + prices live at
    `https://openrouter.ai/api/v1/models` before spending; document the substitution).
Note: these are s3-frozen-config grading prompts (old bank, single-grader era) — valid for
grader-BIAS inference, not for leaderboard numbers; disclose.
**Deliverable + RULING (Fable, main loop):** kin-delta per family (does
deepseek-the-grader inflate deepseek-the-SUT relative to non-kin graders?), then the
unlock rule for kin families in the session-6 roster: per-SUT panel substitution with
measured offset / accept-and-disclose with the measured delta / keep exclusion. Record in
the session-5 report.

### Phase 3 — Fable design gate (main loop, no dispatch)

Given Phase 1+2 evidence, decide the v2.2 bank strategy. Option space (decide on evidence,
not by default): rubric hardening on DEAD items (excellence criteria reserving 100 for
exceptional answers); a 4-turn escalation episode subset (s4 EP-01 deferral — episodes are
the proven discriminator; growing episode count/families may be the primary ceiling fix);
contested growth (n=4 → ≥15); CV-05 double-barrel decomposition scoped to CORE items only;
**new-item authoring** — if triage shows hardening cannot create enough frontier headroom,
DESIGN the authoring pipeline (specs, adversarial-review gates, provenance rules,
converter-layer only, v1 YAML untouched); authoring execution may itself be session 6.
Output: `reports/2026MMDD-session5-v22-design.md` with a **frozen v2.2 definition and a
bank-versioning rule** (every future leaderboard must cite its frozen bank version).

### Phase 4 — implement cheap wins + validation micro-run (~$2–4)

Implement whatever Phase 3 approves that is cheap (converter patches via a new
`convert/session5_patches.py` layered after session4's; episode turns; tests green;
per-item edit log in a NEW dated report). Then validate on CHANGED ITEMS ONLY across
2–3 SUTs spanning both tiers (e.g., qwen + haiku + 4o-mini). **Success metric, stated in
advance: hardened items produce nonzero within-tier-1 spread on ≥half the re-run items;**
otherwise the "new items needed" branch is confirmed for session 6. $0 mockllm smoke
before any live call.

### Phase 5 — session-6 scale-up runbook ($0)

Roster longlist (families + live-verified slugs/prices, INCLUDING kin families under the
Phase-2 ruling), power analysis (given the v2.2 discriminating core, the minimum
detectable difference at target n — s4 baseline: paired MDD ≈ 2.8 pts at n=221, but that
was pre-saturation-fix), per-model cost forecast (reasoning models like qwen forecast
separately), go/no-go criteria (run only if Phase-4 validation succeeded), exact eval-set
commands. Consolidated session-5 report + memory update close the session.

## Binding conventions (do not relitigate)

1. All results **EXPLORATORY / NON-QUOTABLE**; scores are 0–100 rubric-conformity medians,
   NOT accuracies. No pre-registration framing (vault v1.x directive).
2. Bank/config versioning: pilot numbers (s4) are panel-native/patched-bank/new-parser —
   never compared to s2/s3 frozen-config numbers; v2.2 numbers likewise get their own scale.
3. **No deletions ever** (`mv` to `RECYCLE-BIN/`); never edit `../WCF-Benchmark/` (v1) or
   existing dated reports (new reports get new `YYYYMMDD-` prefixes); never touch the
   shared vault `.venv`; item edits ONLY via the converter patch layers, YAML untouched,
   per-item edit logs mandatory.
4. Handoff docs/skills RETIRED (owner directive 2026-07-15): end with dated report(s) +
   commits + memory update only.
5. Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel sessions.
   **Commit with explicit pathspecs** (`git commit -m "..." -- <paths>`). Close: commit →
   `git pull --rebase --autostash` → restore out-of-scope conflicts to HEAD → push →
   `git rev-list --count origin/main..HEAD` = 0. Leave existing stash entries alone.
6. Budget: proceed autonomously if total session forecast ≤ **$10**; ask Jimmy above that.
   s4 overran 3% on an in-budget forecast — pad forecasts for grader-prompt growth
   (anchor-text blocks) and reasoning-token SUTs.
7. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every dispatch; agents
   EXECUTE (files/runs), not plan. Any multi-agent comparison work (e.g., parallel
   raters/critics) gets anti-leakage isolation; Fable adjudicates in the main loop.

## Gotchas (sessions 1–4; do not rediscover)

- `model_graded_qa(instructions="")` silently falls back to C/P/I — always pass the
  numeric instructions file.
- Inspect's multi-grader `model=[...]` reduces by MODE — degenerate on 0–100 grades; the
  codebase uses explicit `panel_median` (`src/wcf_grading.py`). Don't "simplify" it back.
- `inspect score --model` overrides the SUT, not the scorer-closure grader — re-grade via
  replay of the persisted grading prompt (verified grade-free).
- `inspect eval-set -T task_args` apply to ALL tasks in the set → run main and episodes
  as SEPARATE eval-sets when passing episode-only args (s4 did:
  `logs/20260716-pilot/{main,episodes}/`).
- `--limit N` takes the FIRST N samples (file-sorted = skewed); use `--sample-id` for
  diverse smokes. mockllm → unscored/nan = PASS for $0 plumbing tests.
- Task instantiation eagerly builds grader clients → `OPENROUTER_API_KEY` must be in env
  even for imports/tests (dummy value fine when not calling live).
- Always `python -m pip`, never bare pip. Never `rm` — the vault hook denies whole
  commands containing deletion-pattern strings (even inside messages); rephrase.
- qwen3.7-plus: s3 emitted `<think>` in 204/204 completions; s4 emitted 0/221
  (provider-side change) — re-check per run, assume nothing; it remains the most verbose
  SUT (1.7× median graded chars) and the reasoning-token cost driver.
- Panel provenance lives in Score metadata since s4 — per-grader analysis needs NO
  re-runs; grader failures (n_valid<3) are real at ~0.5% — keep the quorum check in every
  completeness audit.
- One grading standard (WHOLE-C8-W306) exceeds 6000 chars post-anchor-text — grader
  prompts are bigger than s3; include in cost forecasts.
- Background-eval agents may rest while their eval lives on: PID watcher + continuation
  dispatch, but check for self-resume duplicates first.

## Acceptance checklist

- [ ] Item triage table delivered (every item classified, counts by kind) + discrimination
      anatomy + panel-health read, all $0 from existing logs.
- [ ] The two Fable re-reads done and written up (23 G-items partition; anchor recall boundary).
- [ ] Kin-delta measured on both kin SUTs under default vs kin-free panels; unlock RULING
      recorded for the session-6 roster.
- [ ] v2.2 design memo written and FROZEN (incl. bank-versioning rule; new-item pipeline
      designed if triage demands it).
- [ ] Approved cheap fixes implemented (patch layer + tests green + per-item edit log) and
      the validation micro-run judged against the pre-stated success metric.
- [ ] Session-6 scale-up runbook with roster/power/cost/go-no-go.
- [ ] Total spend ≤$10 reported via credits delta; new dated reports; memory updated
      (`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md`
      + MEMORY.md index line); pathspec commit → rebase → push → 0 unpushed.
