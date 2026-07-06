# 20260706 — COOKBOOK Core (non-BibleBench) Next-Session Handoff

**Scope: the cookbook proper** — `00-KNOWLEDGEBASE/`, `10-LITERATURE/`, `20-DESIGNS/`, `30-EVIDENCE/`
and the vault-fix leftovers. Everything `40-BIBLEBENCH/` has its own handoff chain (per-bench
`*-next-session-handoff.md` files + the scope-isolation rule) — do NOT work BibleBench from here.

**Read after this:** `COOKBOOK/README.md` (structure + caveats), then only what the queue item needs.

## State at 2026-07-06

- **Adversarial gate COMPLETE (2026-07-05):** 12 refute-first Opus reviews over the six designs →
  Fable adjudication (`20-DESIGNS/REVIEWS/20260705-adjudication-memo.md`, the authoritative record):
  all six **REVISE-AND-PROCEED**, no understudy promotions; cross-cutting standards X1–X6 imposed.
  All six designs revised in place (each ends with "Revision log — 2026-07-05 adversarial gate").
  `20-DESIGNS/00` carries the corrected sequencing and a gate-status section.
- **The load-bearing decision:** DUPLEX's discrimination premise = ONE unreplicated single-model
  effect (MP-DP, Haiku 3.5; digest: "all 8 others 0.000"). DUPLEX is therefore **P0-gated**:
  a falsification-first smoke test (design 03 §7) runs BEFORE any generator build. **CRUX is the
  pre-registered fallback build-first** if P0 fails. The old "P1 generator + 300 items" plan is
  superseded.
- `20-DESIGNS/` is untouched since the gate commit (`e10536c63`; provenance note in
  `20260705c-session-handoff.md` — that commit bundles two sessions' work). Lit layer spot-checked
  clean (21/21). Working tree clean on this track.

## Queue (priority order)

### 1. DUPLEX P0 falsification smoke test — THE next build step (Opus session, model runs)
- Protocol: revised `20-DESIGNS/03-moralpsych-duplex.md` §7. Summary: ~40–60 novel
  procedurally-varied items × resource-manipulation cells × 9 cross-vendor models; three
  pre-registered thresholds (process-beats-content CV with non-degenerate denominators; KB04 §6.2
  ≥90%-pairwise-separation on ≥1 manipulation; Greene-load/utilitarian-shift direction). Honor the
  MP self-administration disclosure + cross-family generator/subject/judge separation (03 §3.5).
- **Branch rule (pre-registered — do not relitigate):** P0 pass → DUPLEX generator build proceeds;
  P0 fail → CRUX takes build-first, DUPLEX re-scoped as universal-signature (descriptive)
  measurement.
- Harness pointer: the Moral Psych sub-project ran the same 9-model × 3-vendor administration
  pattern (see digest §8 pointers → `MORAL-PSYCH/ANALYSIS/`); reusing that harness needs Jimmy's OK
  (sibling-project rule) — ask before pulling it in, else build a minimal fresh runner.
- Optional (pending Jimmy's sign-off on the overlap map): include 1–2 FRUITBENCH manipulation cells
  (mood-induction, provocation ladder) per
  `40-BIBLEBENCH/20260705-fruitbench-duplex-intra-overlap-map.md` §2 — more independent shots at
  finding a discriminating manipulation, no bench-folder edits involved.
- **P0 results adjudication is Fable-tier** — if results land before ~2026-07-11, bring them back to
  a Fable session for the pass/fail call and any portfolio consequences; after the window, Opus
  adjudicates strictly by the pre-registered thresholds (no judgment calls beyond them).

### 2. CRUX item-engine head start (Opus, no model runs needed initially)
CRUX builds second *either way* (its procedural-generation core is reused by every other design),
so an Opus session can start it in parallel with / immediately after P0: implement the
fractional-factorial generator per revised `20-DESIGNS/06-crosscutting-crux.md` (post-gate: bounded
PS scoring, Schwartz-anchored values, powered-cells-only consensus estimation), plus the shared
shortcut-audit tooling (lexical baseline + 10%-fine-tune probe) that X2 makes mandatory portfolio-wide
— build it once here, every design reuses it.

### 3. Long-pole starts for Designs 02/04/05 (drafting only; partnerships need Jimmy)
Per `20-DESIGNS/00` sequencing note, 04 (INTRA) and 05 (CULTIVATE) have co-design pipelines as the
long pole. Automatable now (manuscript-drafter tier): INTRA's split authoring-board vs
validation-board charters + rater-panel protocol (per its revised C2 fix); CULTIVATE's 1-locale +
1-diaspora pilot co-design brief and annotator-recruitment spec (per its revised C4 rescope);
FRAMESHIFT's sub-variant specification sheets (act/rule-util; Kantian/Rossian/threshold). Actual
expert/community recruitment = Jimmy.

### 4. Optional Fable insurance: spot-check the six revised designs
The revisions were Opus-executed against the adjudication memo and verified via diffs/agent reports,
but no dedicated read-through pass exists. A short Fable (or careful Opus) session could grep each
design for its X1–X6 sections + read the Critical-fix sections against the memo. Cheap; do it
before the first big build spend if paranoia warrants.

### 5. Vault-fix leftovers (housekeeper/sonnet tier)
From `logs/20260705-vault-data-fixes.md`:
- Verify by web, then fix, the two UNRESOLVED sources (hypotheses only, NOT confirmed):
  "Sycophancy Probes" (stem cites 2406.09569 = wrong paper; candidate = Anthropic Alignment blog
  post "Simple probes can catch sleeper agents", Apr 2024, non-arXiv) and "Gemini Safety"
  (2403.04312 = wrong; candidate = GDM "Evaluating Frontier Models for Dangerous Capabilities",
  arXiv 2403.13793).
- Scripted stem-rename for the CCAI↔Sycophancy card swap (11-file reference map is in the log;
  do it as one script + validation, not manual edits).

## Standing cautions
- Four sub-project disclosures whenever their numbers appear (NormEval F1–F7 elicited; MP
  self-administration; RV same-vendor scoring; CG N_eff≈3.4). Digest statistics copied verbatim,
  never recomputed. Card page refs ±1–2 pp.
- Delegation tiering per `~/.claude/CLAUDE.md` + `.claude/FABLE-WEEK.md` — **Fable window ends
  ~2026-07-11**; reserve it for P0 adjudication and any gate-level judgment; everything in this
  queue except that is Opus/Sonnet work.
- Concurrent-session git hazard: the index is shared across parallel sessions — check `git log -1`
  before committing, stage+commit atomically, never rewrite a sibling session's commit
  (see memory `parallel-sessions-share-git-index`; it already bit us once, commit `e10536c63`).
- Safety rules hook-enforced (no rm → RECYCLE-BIN; new dated reports, never edits; YAML lint;
  run `PYTHON/validate_all_papers.py` after any batch touching papers).
- End with a dated handoff + commit + push.
