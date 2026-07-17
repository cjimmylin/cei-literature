# BOOT PROMPT — WALKWORTHY v2 side-session JR-R: collaborative reporting on the two-arm judge-referee meta-audit

Paste/read this at the start of a fresh session. It is self-contained. It is
INDEPENDENT of the queued s8 boot prompt
(`20260716-boot-prompt-s8-ledgerclose-canonical.md`) — either can run first;
do not pick up s8's agenda from here.

## Mission

A **collaborative reporting session**: expand the two completed JR referee
result memos into a fuller written product, working interactively with the
owner. The referee DATA WORK IS DONE — both arms ran to completion
(942/942 verdicts each; zero refusals; zero API spend). This session is
writing, synthesis, and presentation ONLY: no new referee dispatches, no
re-judging, no new sampling, no model calls for measurement of any kind.
Offline figure generation (matplotlib via the repo venv) and PDF rendering
(fpdf2/Typst — never LaTeX) are fine if the owner wants them.

**FIRST ACTION — elicit the report spec from the owner before drafting.**
The deliverable's shape was deliberately left open. Ask (AskUserQuestion or
plain conversation) and get rulings on:
1. **Audience/register** — internal lab notebook expansion? methods-paper-style
   writeup (companion to the WALKWORTHY v2 fit memo)? owner-facing decision
   brief for the 5 pending hooks? public-shareable methods note?
2. **Length/format** — single markdown report vs report + PDF; figures or
   tables-only; whether the two arms merge into one unified document or the
   unified doc supersedes-by-pointer.
3. **Whether the owner wants to RULE on the 5 decision hooks during this
   session** (rulings are owner speech-acts; if ruled, record them in a dated
   memo — they still do NOT modify the instrument from this session).
4. **Comparative-claims posture** — confirm the report stays outside benchmark
   reporting (default: yes, verbatim guardrail below).

## Framing guardrails (bake into every artifact, verbatim)

This is NOT benchmark work and adds nothing to the benchmark. "Closer to
Opus/Sol" = **reference-model concordance, not ground truth** — the referees
are stronger models, not oracles; two referees agreeing may share correlated
error (consensus evidence, not correctness evidence). Results change NO judge
pins, enter NO benchmark reports, and trigger NO instrument changes without a
separate explicit owner ruling (R1/R3/C9 + RATIFIED F11 govern benchmark
claims; this data lives outside that instrument). The sample is deliberately
disagreement-enriched — **no pooled "overall agreement" headline without the
per-stratum split adjacent.**

## Where everything is

Base `$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
(python: `$V2/.venv/bin/python`; v1 at `../Christian-Ethics-Benchmark/` is
READ-ONLY).

**Read first (in order):**
1. `20260716-opus-referee-results.md` — arm 1 (Opus referee) protocol + findings
2. `20260717-sol-referee-results.md` — arm 2 (GPT-5.6-Sol referee) + the
   four-way revision of arm 1 (02 revised, 07 corroborated, 06 split, defect
   items confirmed)
3. `20260716-jr-sampling-precommit.md` — frozen design (manifest sha, seed,
   strata, blindness protocol)
4. Skim for framing only: `20260716-prereg-comparisons-RATIFIED.md` (R1/R3/C9)

**Authoritative numbers (recompute nothing by hand — read these):**
- `logs/jr-referee-20260716/referee-agreement.json` — arm-1 tables (Opus↔A/B,
  side-with, 06 deltas, unscorable audit, sensitivity)
- `logs/jr-referee-20260716/referee-agreement-sol.json` — arm-2 four-way
  tables (Sol↔A/B/Opus per stratum, joint referee cells, top-8 quadruples,
  06 deltas, Sol unscorable audit, both sensitivity cuts)
- `logs/jr-referee-20260716/manifest-meta.json` — sample counts, base rates,
  9 excluded d06 units
- Raw verdicts if per-unit examples are wanted for the report:
  `opus-verdicts.jsonl`, `sol-verdicts.jsonl` (join by prompt_sha256 to
  `sample-manifest.jsonl` for unit keys; sample_ids collide across SUTs —
  scope joins by (sut, log, sample_id))
- The analysis tools (committed, re-runnable): `tools/audit/referee_agreement.py`
  (arm 1), `tools/audit/referee_agreement_sol.py` (four-way). Prompt-side
  provenance: `export_referee_prompts.py`, `make_referee_manifest.py`,
  `make_referee_batches.py`, `ingest_referee_verdicts.py`.

**Frozen headline numbers (for drafting convenience; JSONs are authoritative):**
- Sample n=942 (07: 392 disagree + 150 ctrl; 02: 200 + 80; 06: 60 gap + 60
  ctrl), manifest sha `b2839b1413c6b94a9bf2912497c414df9e83751d84fb97df743b436807f5ef9f`,
  seed 20260716. Judges: A = gpt-4.1-nano, B = llama-3.3-70b (both
  G5-certified). Referees: Opus (Claude Code agents, 40 dispatches) and
  GPT-5.6-Sol (codex exec, 39 dispatches, first-pass clean).
- Referee↔referee (Sol↔Opus) raw: 02 ctrl 0.813 / 02 disagr 0.735 / 07 ctrl
  0.920 / 07 disagr 0.857.
- 07 disagreement side-with-B: Opus 0.594 (0.763 excl defect items), Sol 0.605
  (0.770); joint both-B 225/392, both-A 48, opposite-splits 13.
- 02 disagreement: neither-rate Opus 0.495 / Sol 0.500; joint both-neither
  83/200 (referees agreeing on states neither judge chose — the arm-2
  revision); each referee ↔ each judge only 0.23–0.27.
- 06: profile_mean gap stratum S 0.755 / O 0.648 / A 0.506 / B 0.833; Opus
  `principles` strictness (−0.5) NOT replicated by Sol (S−O ≈ +0.40).
- Defect items "(no keyed text)": WW-07-L02 / WW-07-I04 / WW-07-F02 —
  Sol unscorables 87 (35/23/29), Opus 50, overlap 48, zero elsewhere.
- 5 owner decision hooks pending (arm-2 report §hooks supersedes arm-1 where
  noted: 07 judge-A strengthened; 02 reframed taxonomy-vs-judge-upgrade;
  06 principles downgraded; defect items dual-confirmed; no-benchmark-use).

## Tasks (after the spec is elicited)

1. Draft per the owner's spec. New files only, `20260718-` (or actual date)
   prefixes. The existing result memos are IMMUTABLE — supersede by pointer,
   never edit/regenerate them.
2. If figures: generate offline from the two agreement JSONs into the report's
   asset path (screenshots/PNG conventions: keep inside `$V2`, never vault
   root). Verify every number quoted in prose against the JSONs (data-integrity
   rule: verify counts before prose).
3. If the owner rules on hooks: record rulings in a dated decisions memo;
   instrument changes remain OUT of this session's scope regardless of ruling.
4. Commit tools/memos/reports only (logs/ is gitignored), pathspec
   `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`, `git pull --rebase`
   before any push and push only if asked. Auto-memory entry per convention;
   no handoff docs (retired).

## Out of scope (do not pick up unbidden)

s8 agenda (ledger close-out — separate boot prompt) · ANY new referee/judge/SUT
dispatches or a third referee arm (new gated proposal if wanted) · judge-pin or
instrument changes · benchmark-report or comparative-claim use of this data ·
rubric/item revisions (v-next, s8 Task 0.2) · re-running any stored calls.

**Model tiering:** Fable main loop = elicit spec, synthesize, adjudicate prose;
manuscript-drafter (opus) for long drafting from an approved outline;
stats-runner/sonnet for figure scripts; explicit `model:` on every dispatch.

**Standing constraints:** no deletions (`rm` hook-blocked; `mv` to
RECYCLE-BIN/) · reports immutable · canary `WALKWORTHY-CANARY-7f3e2026` in
every artifact · holdout (`banks-holdout/`, `datasets/holdout/`) never enters
prompts/exports/git; `WALKWORTHY_ALLOW_HOLDOUT` stays unset.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
