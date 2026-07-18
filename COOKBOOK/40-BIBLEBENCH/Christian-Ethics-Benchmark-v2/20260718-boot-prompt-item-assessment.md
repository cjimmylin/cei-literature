# BOOT PROMPT — WALKWORTHY v2 benchmark-ITEM assessment (Fable-led DESIGN session)

Paste/read this at the start of a fresh session. It is self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Fable** (`/model fable`). Authored
2026-07-18 by the Opus deck/consolidation session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.

---

## Mission

Design and run an **assessment of the WALKWORTHY v2 benchmark ITEMS** — the item banks
themselves (their keyed answers, corpus anchors, construct validity, clarity, coverage,
defects), NOT the judges and NOT the systems-under-test. This is a **DESIGN-FIRST session**:
the owner will specify the assessment's purpose and shape *in this session, with you helping
design it*. Do not assume the methodology is fixed — your first job is to help scope it, then
plan it, then execute.

**Distinguish from prior work (do not redo):** the 2026-07-16/17 meta-judging arm assessed the
*judges* (Opus + GPT-5.6-Sol referees over 942 units). This new session assesses the *items*.
They intersect only at the 3 known defect items (below).

## Working mode (Fable — read `~/.claude/CLAUDE.md` tiering first)

- **Fable stays in the main loop:** assessment design, validity/statistical design, rubric
  design, adjudication of disagreements, adversarial review of findings, final synthesis.
- **Delegate everything else down a tier** via `.claude/agents/` (pass the declared `model`
  explicitly on EVERY dispatch — a hook checks `tool_input.model`):
  - item/file search → `vault-searcher` (haiku) or `Explore` (sonnet)
  - scripted scoring / stats / recompute → `stats-runner` (sonnet)
  - report/manuscript drafting → `manuscript-drafter` (opus)
  - refute-first checks on any finding → `adversarial-reviewer` (opus)
  - git / file moves → `housekeeper` (sonnet)
- **Sequence:** (1) read the orientation files below; (2) **AskUserQuestion** to pin the
  assessment's *purpose, scope, output, and whether it feeds a paper* (candidate menu in
  §"Design space"); (3) draft a design and **enter plan mode** for approval; (4) execute tiered
  with verification-before-completion. Do not start scoring items before the design is ruled.

## Where everything is  (`$V2 = ` this folder — now the single consolidated home)

Read these FIRST (dispatch a sonnet `Explore` to summarize the long ones if you prefer):
- `REPORTS/20260717-briefing/01-benchmark-card.md` — **the item catalog**: all 10 designs,
  item counts, ID scheme, per-design construct + metric + keyed states, 19 real + 1 authored
  worked examples. The single best "what are the items" doc.
- `tools/SCHEMA.md` — the JSONL dataset schema (field-level).
- `RULINGS-APPLIED.md` + `REVIEWS/` — the prior adversarial item-review pass and applied fixes.
- `REPORTS/20260717-briefing/working/20260717-consolidation-manifest.md` — where every
  artifact/intermediate lives (this folder is now self-contained).
- `README.md` — folder front door.

The items themselves:
- `banks/design01.md … design10.md` (+ `*-seeds.md`) — authored item banks (source of truth).
- `banks/20260716-divergence-tags.jsonl` — per-item divergence tags (29 yes / 129 partial /
  186 no).
- `datasets/public/design01–10.jsonl` — the 344 runnable public items (converted from banks).
- `banks-holdout/` + `datasets/holdout/` — the 158-item holdout (**gitignored, loader-guarded —
  never put in prompts/exports/git; see Safety**).
- Pilot + referee evidence already in-folder: `logs/pilot-20260716/` (5-SUT pilot),
  `logs/jr-referee-20260716/` (canonical referee verdicts/agreement — read-only provenance).
- Analysis code you can reuse: `tools/audit/`, `tools/rescore/`, `walkworthy_inspect/` (metrics,
  scorers, parsers, rubrics).

## What the items are (one paragraph)

10 method-distinct behavioral designs; **344 public items (+158 holdout)**; IDs `WW-<dd>-<L><n>`
(e.g. `WW-01-A05`, `WW-07-L02`). Each item has a scenario (system+user turns), a keyed target
behavior / action-classes, and anchors to a **15-work Protestant-ethics corpus** (anchors are
grep-verifiable; direct Scripture anchoring is disallowed by construction; one work is
contrast-only). Items carry a **stratum**: `a` (headline) vs `c` (intra-corpus disputed,
quarantined). The benchmark measures **concordance with the specified corpus, not theological
truth** — keep that framing in any validity claim.

## Prior item-level findings (build on these; don't re-derive)

- **Adversarial review pass:** 510 items reviewed → **105 fixed, 0 killed** (`REVIEWS/`,
  `RULINGS-APPLIED.md`).
- **Divergence tags:** 29 yes / 129 partial / 186 no (`banks/20260716-divergence-tags.jsonl`).
- **Construct-validity triage (CV-1):** only designs **04/05/10** are candidate-distinct from
  generic RLHF harmlessness at the cheap tier; 01/02/03/06/07/08/09 marked non-discriminant at
  that altitude. (An annotation, not yet an empirical discriminant test — a natural assessment
  target.)
- **3 defect items, dual-referee-confirmed:** `WW-07-L02 / WW-07-I04 / WW-07-F02` have
  "(no keyed text)" anchors — mechanically unscorable; need keyed text authored.
- **Design-02 taxonomy contested:** referees land on a "neither" state on 83/200 contested turns
  — a possible item/taxonomy-clarity problem, not just a judge problem.
- **Design-07 floor-saturated:** 0 pass across all 5 pilot SUTs (0 exclusions) — a real
  construct floor at cheap tier; relevant to item difficulty/discrimination.

## Design space (candidate assessment dimensions — a MENU to speed the owner conversation)

Do not assume; ask which of these (or others) the owner wants. Likely candidates:
1. **Keyed-answer / gold validity** — is each item's keyed target behavior actually correct
   given its corpus anchor?
2. **Corpus-anchor fidelity** — does the cited anchor genuinely support the keyed behavior?
   are anchors present, correct, grep-verifiable? (extends the defect-item class)
3. **Construct validity per design** — does the item measure its named construct vs generic
   harmlessness? (turns CV-1 from annotation into a test)
4. **Clarity / ambiguity / fairness** — unambiguous scenario? defensible alternative readings?
   (the design-02 "neither" problem)
5. **Difficulty / discrimination** — from pilot data, which items separate SUTs? floor/ceiling
   items (design-07)?
6. **Coverage / redundancy** — do the 344 span the intended space; near-duplicates?
7. **Defect scan** — empty/malformed anchors, broken keys, the "(no keyed text)" class.
8. **Bias / demographic sensitivity** — names, deservingness cues (design-10), protected traits.
9. **Public↔holdout parity** — is holdout quality/difficulty matched to public? (guarded; see Safety)

## Method scaffolding you may propose (Fable to design the actual instrument)

- **LLM-rater assessment via Agent dispatches** (vault preference: Claude Code Agents over API;
  anti-leakage / blind framing; fresh-context per rater). See the reusable 2-rater IRR +
  sub-clustering template in auto-memory (`llm_rater_2_substitution_channel_template`).
- **Adversarial refute-first review** of each candidate finding (majority-refute kills it).
- **Reuse** `tools/audit/`, `tools/rescore/`, `walkworthy_inspect/` for anything scored
  mechanically. A `dispatching-parallel-agents` fan-out over the 10 designs / 344 items is the
  natural execution shape once the rubric is fixed.
- Human-rating: prior v1.x directives across the vault defaulted to **no human raters** (LLM-
  rater-2 triangulation instead) — confirm with owner whether that applies here.

## Constraints & safety (hard — apply to subagents too)

- **v2 is PARALLEL, not canonical.** v1 (`../Christian-Ethics-Benchmark/`) is a **read-only
  sibling** — never modify it.
- **Holdout is sacred:** `banks-holdout/`, `datasets/holdout/` never enter prompts, exports, or
  git; `WALKWORTHY_ALLOW_HOLDOUT` stays unset. If the owner scopes holdout into the assessment,
  load only via the guarded loader and keep every output in gitignored areas (`logs/` or a
  gitignored dir). Do not quote holdout item text in any tracked report.
- **Do NOT silently mutate items.** Changing a keyed answer / anchor is an **instrument change**
  → governed by owner ruling (RATIFIED F11, C9 first-use, R1/R3). Produce a findings report + a
  *proposed-edits ledger* (matching the `RULINGS-APPLIED.md` pattern) and get an owner ruling
  before applying any item edit. After any ruled item-bank edit, regenerate datasets with
  `python tools/convert_banks.py` and validate with `python tools/verify_conversion.py`. (Note:
  the papers-vault `validate_all_papers.py` does NOT apply here — these banks are not papers.)
- **No deletions** (`rm`/`unlink`/`find -delete` hook-blocked) — `mv` to the nearest
  `RECYCLE-BIN/` (one exists at `$V2/RECYCLE-BIN/`).
- **Reports immutable** — never overwrite; write NEW `YYYYMMDD-` dated files. Suggested home for
  this work: `REPORTS/20260718-item-assessment/` (create it), with a per-item findings ledger
  (jsonl or md table) + a synthesis report.
- **Canary** `WALKWORTHY-CANARY-7f3e2026` in every artifact you create.
- **Two sharp edges from the last session:** (a) a security hook blocks any file-write whose
  content contains the token *exec-immediately-followed-by-open-paren* — rephrase (use
  `.match()` in JS, avoid literal `codex`+that-subcommand in prose). (b) `tools/audit/` referee
  scripts read/write `/tmp/jr-*` **by design** for blindness — don't "fix" those paths.
- If you run **live model calls**, follow `AGENTS.md` (the 402 trap) and log spend; prefer $0
  Agent/subscription channels; the pilot cost ≈$0.73/SUT for reference.

## Output & closeout

- New dated artifacts under `REPORTS/20260718-item-assessment/` (or as the owner directs).
- Auto-memory entry per convention at the end. **NO handoff docs** (retired 2026-07-15).
- Commit under pathspec `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`; `git pull
  --rebase` first; push when the owner asks (they have wanted push each time recently).

## Out of scope (do not pick up unbidden)

Judge/referee re-audit (that was the meta-judging arm — done) · `WCF-Benchmark-v2/` (separate
project) · v1 modifications · any SUT leaderboard / comparative claim (C9) · the s8 ledger-close
session (independent) · duplicating v1 data into this folder (owner ruled: keep v1 as sibling).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
