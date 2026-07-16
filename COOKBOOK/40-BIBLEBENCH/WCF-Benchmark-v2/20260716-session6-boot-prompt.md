# WCF-Benchmark-v2 — Session 6 Boot Prompt

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

**Author the v2.3 frontier bank (FULL target, ~50–65 new items), gate it with the
pre-stated frontier-core go/no-go pilot, and run the budget-sized roster ONLY if
the gate passes.** Session-5's pre-stated validation settled the strategy with
data: the excellence gate FAILED (1/15 vs required ≥8/15 — both tier-1 SUTs still
hit exactly 100 on 14/15 of the deepest-saturated items), so the tier-1 ceiling is
**capability-parity in the graders' eyes, not a scoring artifact**. Rubric
tightening cannot create frontier headroom; only new, genuinely harder items can.
Roster expansion before that would re-buy the s4 tier-1 blob at ~$2/model.

**Explicit non-goals:** no roster run on ungated items; no quoting v2.3 numbers
against v2.2/s4/s3/s2 scales (each manifest is its own instrument); no editing v1
YAML ever.

Owner decisions locked (2026-07-16): (1) budget ceiling **$10**, same
autonomous-run rule; (2) scope = **author → gate → roster-if-GO in one session**;
(3) authoring volume = **FULL target** (≈15 contested + ≈25–40 frontier-open +
≈8–10 four-turn escalation episodes).

## Where things stand (as of 2026-07-16, session-5 close, commit `640dda292`)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (paths below
  relative to it). Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14; the
  shared vault `.venv` is 3.9 and CANNOT run inspect-ai). API key:
  `set -a && source ~/.codex/secrets/openrouter.env && set +a`.
- **Bank = v2.2** (manifest `data/BANK-VERSION.json`): 199 main + 22 episodes,
  converter chain v1-YAML → `yaml_to_jsonl.py` → `session4_patches.py` →
  `session5_patches.py`; excellence-gate template default ON
  (`-T excellence_gate=false` restores the byte-identical original); last-match
  parser; median-of-3 panel (gemini-2.5-flash + deepseek-chat +
  mistral-small-2603) is the task default. **60 tests green**
  (`.venv-v2/bin/python -m pytest tests -q`; `export OPENROUTER_API_KEY=dummy`
  suffices for imports/tests).
- **Session-5 verdicts (all in `reports/20260716-session5-report.md`):**
  - Triage: DEAD-CEILING 119/221 (53.8%) / NOISY 39 / CORE 38 (upper bound;
    ≥4 top-CORE were rubric-ambiguous) / TIER-BREAK 25 (21 flat). Episodes are a
    tier-break engine (gap 36.2), NOT a frontier engine (1.06× CORE enrichment).
    complicit/steadfast/crosswind carry 21/38 CORE; **aggravate 0/24**.
  - Fable re-reads: the "25% hard ethics" claim dissolved (12/23 repairable
    ambiguity, 8/23 sub-threshold gemini harshness, only 3 genuinely hard);
    anchor "0 contaminable" holds only WITH its Standards-verbatim rule stated
    (1 borderline: LIB-C4-002 ≈0.5).
  - Levers B+C rubric repairs PASSED validation (8/12 AMBIG + 2/3 contested
    reduced panel spread; e.g. COMP-C8-W306 40→3.3).
- **Kin ruling (design memo §6, measured by DiD with qwen as non-kin control):**
  mistral family UNLOCKED (disclose +0.97 [−0.51,+2.46]); deepseek family
  UNLOCKED with a **−1.7-pt self-kin sensitivity rule** on within-tier claims
  (measured +1.67 [+0.14,+3.27]); google family CONDITIONAL — gemini-kin was
  never measured (gemini sat in both panels); a gemini SUT may run but its
  numbers may NOT be quoted until the gemini-free-panel DiD piggyback is done.
  command-r-08-2024 is a WEAK grader (20.2% lone-outlier) — never reuse in
  audit panels; nova-pro-v1 performed well.
- **Key artifacts:** `reports/20260716-session5-report.md` (consolidated),
  `reports/20260716-session5-v22-design.md` (§4 = the authoring pipeline you will
  execute; §6 = kin ruling), `reports/20260716-session6-scaleup-runbook.md`
  (sequencing, roster longlist + prices, power analysis, command templates),
  `reports/20260716-session5-fable-rereads.md` (rubric form-rules rationale,
  R1–R5 patterns), `analysis/20260716-session5-item-triage.csv` (per-item
  classes — the CORE items are the style models for frontier-open authoring),
  `analysis/20260716-session5-kin-stats.json`,
  `analysis/20260716-session5-roster-longlist-raw.json` (live slugs/prices,
  re-verify before spending), `analysis/20260716-session5-validation-results.json`.
- Spend history: s3 $5.01 / s4 $10.32 (3% over) / s5 ≤$7.68 upper bound
  (~$4–5 attributed; concurrent same-key sessions inflate credits deltas).

## Work plan — author, gate, then (maybe) spend

### Phase 0 — ground state ($0)

Credits snapshot (`GET api/v1/credits`; delta = upper bound only); 60 tests green;
**re-review the 2 flagged s5 repairs**: COMP-C4-005 (R3 checkable-structure
rewrite produced a haiku=0 outlier, panel spread 20→43 — read the haiku response
in `logs/20260716-session5-validation/configX-main/` and adjudicate whether the
new criterion is too strict or the zero was earned) and DUTY-XC-W206 (spread
6.5→16.3 with one grader quorum drop). Patch via a small addition to
`convert/session5_patches.py` ONLY if clearly warranted; log any change in a NEW
dated edit-log report.

### Phase 1 — authoring (~$0 API; the bulk of the session)

Execute design-memo §4 at FULL target: **≈15 contested (4→15+) + ≈25–40
frontier-open + ≈8–10 four-turn escalation episodes.**

- **Provenance (binding):** new items live in a NEW converter source (e.g.
  `convert/session6_new_items.py` or a v2 YAML/JSON under `data/` — NOT the v1
  YAML); ids namespaced `*-N-###`; each item carries `authored: session-6`
  metadata. Bank version bumps to **v2.3** only at Phase 3.
- **Rubric form-rules (from birth, no exceptions):** every criterion
  single-judgment and checkable; R1 defection/partial-compliance gates on any
  item where a model could comply-with-harm; R2 equivalence rules on any
  "named/cited specifically" criterion; no unanchored quality adjectives
  (R3 lesson); contested items use the CV-04 form (binary decline + enumerated
  accepted head-pairs). Anchor-kind authoring states its recall rule per the s5
  ruling.
- **Content targets:** frontier-open items follow the proven CORE molds
  (complicit/steadfast/crosswind; a lawful-but-costly correct position — study
  5–10 CORE items from the triage CSV first). NO new aggravate-format items
  (0/24 CORE — the format saturates). Episodes: 4-turn escalation ramps
  extending the v2.1 `pressure_turns.py` machinery, defection mechanically
  checkable per turn.
- **Tiering + anti-leakage (binding):** opus agents draft (explicit `model` on
  every dispatch; agents EXECUTE — files, not plans); **≥2 blind adversarial
  reviewers per item** (reviewers see item+rubric only — not each other, not the
  drafting rationale) hunting the CV-01…CV-10 defect classes; **Fable
  adjudicates every kill/repair in the main loop.** Expect and report a kill
  ratio — if nothing dies, the review was theater.
- Quality gates G1 (form-rules conformance) + G2 (adversarial review) + G3
  ($0 mockllm plumbing pass on every accepted item) complete this phase.

### Phase 2 — frontier-core GO/NO-GO gate (~$1.5–2)

Run ALL accepted new items on **qwen3.7-plus + claude-haiku-4.5 + gpt-4o-mini**
(the s5 validation trio), panel default, separate main/episodes eval-sets,
mockllm smoke first. **Pre-stated GO criterion (runbook §1, do not relitigate):
≥⅓ of new items show nonzero |qwen−haiku| AND unscored=0.** Also require: no
new item is trivially broken (a floor check — degenerate all-SUT zeros get
re-reviewed, not silently kept).
- **NO-GO ⇒ one authoring iteration** (Fable adjudicates what failed: too easy?
  rubric-satisfiable? grader can't verify?), re-run the gate on new/changed items
  only. **If still NO-GO: STOP — no roster spend**; write up findings; the
  session ends as an honest negative result.

### Phase 3 — v2.3 freeze ($0)

Items passing G1–G5 enter the bank; regenerate via the converter; write the new
`data/BANK-VERSION.json` (bank_version "v2.3", patch_layers + new-item source,
fresh hashes); per-item provenance/edit log in a NEW dated report; extend tests
(counts, id-namespace, form-rules spot checks); all tests green.

### Phase 4 — roster run IF GO (~$6–7 residual)

Budget-sized roster from runbook §2 under whatever remains of the $10:
- **Anchors:** qwen3.7-plus, claude-haiku-4.5, gpt-4o-mini (bridge trio — already
  have v2.3-comparable gate data; extend to the full v2.3 bank).
- **New SUTs by price until the residual is spent (suggested order):**
  gpt-5-mini (~$1.6), deepseek-v3.2 (~$1.0, self-kin sensitivity rule),
  mistral-large-2512 (~$1.6, disclose bound), glm-4.7 (~$1.6) or minimax-m3
  (~$1.3). A gemini SUT ONLY if its mandatory kin-piggyback (~$1 extra:
  gemini-free panel = deepseek + mistral-small + nova-pro, DiD with a non-kin
  control) also fits — otherwise defer ALL google SUTs to s7.
- Re-verify slugs/prices live before spending
  (`analysis/20260716-session5-roster-longlist-raw.json` is a 2026-07-16
  snapshot). Forecast reasoning-verbose SUTs at 2.5× completion tokens; the
  excellence gate adds ~9% grading tokens.
- **Reporting form:** leaderboard = (a) full-bank mean (tier-level, MDD ~2–3.5)
  + (b) **frontier-core index** (new `*-N-###` items only, own MDD quoted) —
  power analysis in runbook §3. Every table cites bank_version v2.3 + panel +
  parser. deepseek rows carry the −1.7 sensitivity note; mistral rows the
  measured bound. If the run budget forces SUT cuts, cut SUTs — never items.

### Phase 5 — close ($0)

Consolidated `reports/2026MMDD-session6-report.md` (+ per-phase dated reports);
memory update (`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md`
+ MEMORY.md index line); pathspec commit → `git pull --rebase --autostash` →
push → `git rev-list --count origin/main..HEAD` = 0.

## Binding conventions (do not relitigate)

1. All results **EXPLORATORY / NON-QUOTABLE**; scores are 0–100 rubric-conformity
   panel-medians, NOT accuracies. No pre-registration framing (vault v1.x
   directive).
2. **Bank-versioning rule is BINDING (s5):** every leaderboard/report/number
   cites its `bank_version` + panel + parser; different manifests never share a
   table without a config-break banner. v2.3 numbers are a new scale.
3. **Kin disclosure rules (s5 ruling):** deepseek −1.7-pt sensitivity on
   within-tier claims (both directions); mistral bound disclosed; google
   quotable only after its own DiD measurement.
4. **Never quote single-draw item-level numbers** (s5); epochs=1 is fine for
   aggregate means, not per-item claims.
5. **No deletions ever** (`mv` to `RECYCLE-BIN/`); never edit `../WCF-Benchmark/`
   (v1) or existing dated reports (new reports get new `YYYYMMDD-` prefixes);
   never touch the shared vault `.venv`; item changes ONLY via converter
   layers/new-item sources; per-item edit/provenance logs mandatory.
6. Handoff docs/skills RETIRED (owner directive 2026-07-15): end with dated
   report(s) + commits + memory update only.
7. Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel
   sessions. **Commit with explicit pathspecs**
   (`git commit -m "..." -- <paths>`). Leave existing stash entries alone.
8. Budget: proceed autonomously if total session forecast ≤ **$10**; ask Jimmy
   above that. Pad forecasts: grader prompts are anchor-enlarged (+ the ~9%
   excellence-gate block); reasoning SUTs forecast separately; credits deltas
   are upper bounds (concurrent same-key sessions).
9. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every dispatch;
   agents EXECUTE (files/runs), not plan. Multi-agent comparison/review work
   gets anti-leakage isolation; **Fable adjudicates in the main loop.**

## Gotchas (sessions 1–5; do not rediscover)

- `model_graded_qa(instructions="")` silently falls back to C/P/I — always pass
  the numeric instructions file.
- Inspect's multi-grader `model=[...]` reduces by MODE — degenerate on 0–100
  grades; the codebase uses explicit `panel_median` (`src/wcf_grading.py`).
  Don't "simplify" it back.
- `inspect score --model` overrides the SUT, not the scorer-closure grader —
  re-grade via replay of the persisted grading prompt
  (`scores[...].metadata['grading'][0]['content']`, verified grade-free).
- `eval-set -T task_args` apply to ALL tasks in the set → run main and episodes
  as SEPARATE eval-sets when passing episode-only args (`pressure_variant=item`).
- `--limit N` takes the FIRST N samples (file-sorted = skewed); use
  `--sample-id` for diverse smokes. mockllm → unscored/nan = PASS for $0
  plumbing tests.
- Task instantiation eagerly builds grader clients → `OPENROUTER_API_KEY` must
  be in env even for imports/tests (dummy value fine when not calling live).
- Always `python -m pip`, never bare pip. Never `rm` — the vault hook denies
  whole commands containing deletion-pattern strings (even inside messages);
  rephrase.
- qwen3.7-plus: `<think>` prevalence flips between runs (s3: 204/204; s4:
  0/221) — re-check per run; it is the most verbose SUT (1.7× median graded
  chars) and a reasoning-token cost driver.
- **qwen under `inspect eval` can leave `status=started` partial logs (s5)** —
  audit completeness, re-run missing `--sample-id`s, merge last-file-wins.
- Panel provenance lives in Score metadata (`metadata['panel']` =
  {n_valid, values}, grader-ordered g1=gemini/g2=deepseek/g3=mistral-small);
  grader failures (n_valid<3) are real at ~0.5% — keep the quorum check in
  every completeness audit.
- One grading standard (WHOLE-C8-W306) exceeds 6000 chars post-anchor-text;
  the excellence gate adds ~650 tokens/prompt — include both in cost forecasts.
- **Heredoc + pipe collision (s5):** `curl ... | python - <<'EOF'` feeds the
  JSON to python as the script — fetch inside python (urllib) instead.
- **Sub-threshold-outlier taxonomy leak (s5):** any classification built on a
  hard spread cutoff (≥30) misfiles the same phenomenon at one notch below —
  when re-adjudicating categories, always look just under every threshold.
- command-r-08-2024: weak grader (3.7% unparseable, 20.2% lone-outlier) — never
  in audit panels. nova-pro-v1 is the validated kin-free substitute.
- Background-eval agents may rest while their eval lives on: PID watcher +
  continuation dispatch, but check for self-resume duplicates first.

## Acceptance checklist

- [ ] Phase-0 re-review of COMP-C4-005 + DUTY-XC-W206 adjudicated and logged.
- [ ] Authored-item inventory reported: drafted / killed-in-review / accepted
      counts per kind (contested / frontier-open / escalation-episode), kill
      ratio stated; all accepted items pass G1–G3 with provenance metadata.
- [ ] Frontier-core gate run and judged against the PRE-STATED criterion
      (≥⅓ nonzero |qwen−haiku|, unscored=0); verdict + branch taken recorded.
- [ ] v2.3 manifest frozen (or explicitly NOT frozen, with the NO-GO findings
      report); tests extended and green.
- [ ] IF GO: roster leaderboard delivered as full-bank mean + frontier-core
      index, citing bank_version/panel/parser, kin disclosures on deepseek/
      mistral rows; gemini quoted only if its kin-piggyback ran.
- [ ] Total spend ≤$10 reported via credits delta (upper bound) + per-run token
      attribution; new dated reports; memory updated
      (`20260715-wcf-v2-inspect-build.md` + MEMORY.md index line); pathspec
      commit → rebase → push → 0 unpushed.
