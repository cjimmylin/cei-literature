# WCF-Benchmark-v2 — Session 11 Boot Prompt (Fable · ITEM-ASSESSMENT DESIGN session)

> Paste as the opening prompt of a fresh **Fable** session. Read top-to-bottom, then
> orient and **propose** — do not execute. This is a **design/planning** session: your job
> is to co-design (with the owner) an assessment of the **benchmark items themselves**, then
> decompose and delegate. The design is **intentionally OPEN** — the owner will specify the
> details this session with your help. Do **not** assume a design, do **not** start heavy
> computation, and do **not** touch the item bank until scope is locked with the owner.

## 0. What kind of session this is (read first)

This is the mirror image of the Session-10 deck boot prompt. That one was an *execution*
prompt that front-loaded every decision. **This one front-loads orientation and a decision
menu, and deliberately leaves the design open** — because the value here is Fable-level
judgment applied *with* the owner, not the reproduction of a fixed plan.

**Fable stays in the main loop**: assessment design, decomposition, adjudication of
competing item-quality judgments, adversarial review, final synthesis. **Everything
delegable goes down a tier** with an explicit `model` on every dispatch (the global hook
checks `tool_input.model`, not agent frontmatter):
- `vault-searcher` (haiku) — find files/patterns
- `Explore` (sonnet) — read inventories/large files, return conclusions not dumps
- `stats-runner` (sonnet) — compute metrics from existing logs/data via `.venv-v2`
- `adversarial-reviewer` (opus) — refute item-quality claims before they're trusted
- `manuscript-drafter` (opus) — write up the assessment
- `housekeeper` (sonnet) — commits / safe file moves

Keep Fable context clean: don't read big JSON/JSONL/logs into the main loop — dispatch an
Explore/stats agent and take back only the conclusion.

## 1. Project orientation (self-contained folder)

Project root (all paths relative to it):
`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/`

- **Read `INDEX.md` FIRST** — folder map + per-deliverable rebuild guide + provenance. The
  folder was made fully **self-contained on 2026-07-17** (`vendor/v1-bank-yaml/` frozen bank;
  analysis paths are now `Path(__file__)`-relative). Nothing you need is outside the folder.
- **What the benchmark is:** a discriminating **Christian-ethics "costly obedience" conduct
  benchmark** (lawful-but-costly conduct/counsel per the Westminster Standards), run on
  Inspect AI, graded by a **median-of-3 cross-vendor LLM judge panel**, with a frontier
  leaderboard. It measures *practicing* virtue under cost, where knowledge benchmarks saturate.
- **Status going in:** instrument frozen at **v2.4**; judge panel validated by the Session-8
  meta-audit; the Session-9 readiness briefing + Session-10 deck are shipped. This session
  turns the lens onto **the items as measurement instruments** (not the models).

## 2. The object of study — the item bank

- **287 items** = **265 main** (`data/wcf_main.jsonl`) + **22 episodes**
  (`data/wcf_episodes.jsonl`, NARROWGATE multi-turn ramps).
- **66 frontier-core `-N-` items** — the authored core that actually discriminates
  (`analysis/20260716-session6-frontier-core-index.json`).
- **9 molds + episodes:** aggravate 60 / complicit 40 / steadfast 36 / crosswind 23 /
  prooftext 23 / dutybound 21 / mending 21 / wholeheart 22 / liberty 19 / narrowgate 22 eps
  (core-n concentrated in aggravate 36, complicit 17, steadfast 13).
- **Provenance cohorts:** 199 v1 + 29 session-6 + 37 session-7 authored.
- **Authored source of truth:** `vendor/v1-bank-yaml/` (frozen v1 bank) +
  `data/session6-drafts/`, `data/session7-drafts/` + `convert/` (the YAML→JSONL pipeline).
- **Full composition + taxonomy + 5 verbatim exemplar items:**
  `reports/20260717-session9-01-benchmark-card.md`.
- **Rubric machinery:** `src/wcf_grading.py`, `src/wcf_tasks.py`, `src/templates/wcf_grade_*.txt`
  (4–6 weighted criteria; axes matter/manner/end; anchored to WCF/WLC; excellence gate 95–100).

## 3. Mission (open — you help design it)

**Assess the benchmark items themselves** — evaluate their quality and behavior as
measurement instruments. *Which* facets is the owner's call; come prepared to propose a
design, recommend a scope, surface the trade-offs, and get decisions before building.

## 4. Candidate assessment dimensions (a menu to propose from — NOT a locked plan)

Offer these to the owner as a pick-list; recommend a subset. Each has a rough "computable
from existing evidence vs. needs new work" note:

1. **Construct validity** — do items elicit *costly obedience* vs. generic helpfulness/safety?
   (qualitative; needs a coding rubric + rater channel)
2. **Discrimination & difficulty** — which items separate models; the **dead-ceiling audit**
   (53.8% of the v1 layer is ceiling for capable models); per-item SUT spread. (largely
   computable from `analysis/20260716-session5-item-matrix.{json,csv}` + logs)
3. **Rubric quality** — are the weighted criteria well-anchored to WCF/WLC; matter/manner/end
   coverage; is the excellence gate calibrated? (content audit of `src/templates/` + samples)
4. **Trap fidelity** — for `-N-` frontier items, is the RLHF-default answer *really* the trap?
   (qualitative + look at model failure patterns)
5. **Reliability by item/slice** — extend the existing ICC slices (overall 0.798; complicit
   0.847; v1-kind 0.769; contested 0.612; steadfast 0.557) to flag low-agreement items.
   (computable from `analysis/20260717-session8-meta-judging-stats.json` + grade matrices)
6. **Coverage & balance** — across the 9 molds + episodes; over/under-represented
   characteristics or difficulty bands.
7. **Redundancy / clustering** — near-duplicate or semantically clustered items. (needs embeddings/clustering)
8. **Contamination / leakage risk** — memorable phrasings, provenance from public texts.
9. **Provenance & authoring quality** — systematic differences across v1 / s6 / s7 cohorts
   (e.g., are s7 items harder / more reliable?). (computable by joining cohort labels to stats)
10. **Metadata / schema hygiene** — completeness, anchor references, form-rule presence.

## 5. Existing evidence — build on it, don't recompute

Prior sessions already produced item-level evidence — inventory it (delegate to Explore/stats)
before proposing new compute:
- `analysis/20260716-session5-item-matrix.{json,csv}` — per-sample item × SUT grade matrix.
- `analysis/20260717-session8-meta-judging-stats.json` — ICC by slice, cross-vendor concordance.
- `analysis/20260716-session6-gate-results.json`, `…session7-gate-results.json` — authoring gate outcomes.
- `analysis/20260716-session6-frontier-core-index.json` — the 66 `-N-` core.
- `logs/` — 33 Inspect-AI eval run-sets (`.eval` binaries; read via `inspect_ai.log`, not by hand).
- `reports/20260717-session9-0{1..6}-*.md` — benchmark-card / evaluation / meta-judging / etc.

## 6. Non-negotiable fidelity caveats (carry into every item claim)

The benchmark's guardrails apply to item-level findings too:
- **EXPLORATORY / NON-QUOTABLE** — 0–100 = panel-median *rubric conformity*, not accuracy.
  Report **ranks, not absolute values**.
- **Single-judge signals are stability-only** (no SIG/ns); SIG belongs to panel-3 / 5-judge-median.
- **τ̂ = −5.10 kin result is DIRECTIONAL only** — never a significance test.
- **Bank versions are separate instruments** — no cross-version score comparison.
- Any per-item "this item is good/bad" claim is a *judgment* — route it through
  `adversarial-reviewer` (opus) before it's trusted.

## 7. Safety & conventions (HOOK-ENFORCED — apply to subagents too)

- **No deletions** — `mv` to the nearest `RECYCLE-BIN/`, never `rm`/`unlink`/`find -delete`/`git clean`.
- **YAML safety** — never `parse_frontmatter()→rebuild` round-trip; use in-place regex
  `re.subn(rf'^{key}:.*$', repl, fm, count=1, flags=re.MULTILINE)`. Run
  `../.venv/bin/python PYTHON/validate_all_papers.py`-style validation after any bank YAML edit.
- **Report immutability** — new `YYYYMMDD-` dated files only; never overwrite/regenerate an
  existing dated report. Put assessment outputs under `reports/` (or a new `reports/`-level
  `ITEM-ASSESSMENT/` subdir if the owner wants them grouped).
- **This session is ASSESSMENT, not bank surgery.** If the assessment *recommends* item edits,
  that is a **separate downstream session** unless the owner explicitly directs edits now.
- **Git** — commit only if the owner asks; nested repo `CEI-Lit-WS`, shared trunk `main`,
  **explicit pathspecs**, `pull --rebase --autostash` → push → `rev-list --count origin/main..HEAD`==0.
- **Spend** — prefer analysis of existing logs over new eval/grade calls. If new judging is
  needed, use the **Agent-as-rater channel** (no API spend), and honor the API rate-limit
  protocol (backoff, conservative batching) if any external call is unavoidable.

## 8. First moves (do these, then STOP and confirm with the owner)

1. Read `INDEX.md` + the benchmark-card composition section; **delegate** an item-bank
   inventory (counts by mold / cohort / track; which items are `-N-` core) to Explore (sonnet)
   and take back a one-screen summary.
2. Have a stats/Explore agent inventory what item-level evidence already exists in `analysis/`
   (dimension 2/5/9 are likely mostly answerable from files already on disk).
3. Present to the owner: **(a)** a one-screen map of the item bank as it stands; **(b)** a
   proposed assessment design — chosen dimensions, the metric/definition for each, data source
   (existing vs. new), sampling, deliverable shape (report? annotated item ledger?
   recommendations?), and the delegation/compute plan; **(c)** the open decisions only the
   owner can make. Give a recommendation, not just a menu.
4. Use `AskUserQuestion` to lock scope. **Do not begin heavy computation or any bank edit
   until the owner confirms the design.**

## 9. Definition of done (this session)

A **locked assessment design** — dimensions, per-dimension metrics, data sources, deliverable,
and the tiered delegation plan — agreed with the owner. If scope is locked with time to spare,
compute the first slice (ideally one of the already-computable dimensions: discrimination,
reliability-by-item, or cohort provenance) and show a sample of the deliverable. No premature
execution; no item-bank edits unless the owner directs them.
