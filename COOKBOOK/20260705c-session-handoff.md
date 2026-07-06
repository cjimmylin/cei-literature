# 20260705c — COOKBOOK Gate Session Handoff (adversarial review + BibleBench integration)

**Session:** 2026-07-05 evening (Fable). Executed the queue from `20260705b-next-session-handoff.md`
(items 1, 2, 3, 5 done; item 4 restructured — see below). This supersedes-and-extends 20260705b.

## What was done

### 1. Adversarial review gate over `20-DESIGNS/` — COMPLETE
- 12 refute-first Opus reviews (novelty + validity per design) in `20-DESIGNS/REVIEWS/
  20260705-adv-review-{01..06}-{novelty,validity}.md`.
- **Verdict pattern: 6× novelty PASS-WITH-FIXES, 6× validity BLOCK.** Fable adjudicated in
  `20-DESIGNS/REVIEWS/20260705-adjudication-memo.md` (the authoritative record): all six =
  **REVISE-AND-PROCEED, no understudy promotions**; six cross-cutting standards X1–X6 imposed
  (numeric go/no-go rules, shortcut audits, eval-awareness arms, power corrections, disclosure
  carriage, novelty hygiene).
- Fable personally verified the DUPLEX evidence against the moralpsych digest: the discrimination
  premise rests on ONE unreplicated single-model effect (MP-DP, Haiku 3.5); r=−0.83 motivates but
  does not guarantee. → **DUPLEX pilot restructured: falsification-first P0 smoke test BEFORE the
  generator build; CRUX is the pre-registered fallback build-first if P0 fails.**
- All six designs revised in place by Opus agents (+1,509/−310 lines); every design file ends with a
  "Revision log — 2026-07-05 adversarial gate" mapping defects → changes. `20-DESIGNS/00` updated
  (sequencing now P0-conditional; "airtight" overclaim corrected; gate status section added;
  S6 partially absorbed into 01 as the MA-identifiability mechanism).

### 2. 40-BIBLEBENCH integration — COMPLETE (7 packs, not 4)
- Three packs added after 20260705b turned out to be **empty stubs** (ARMOURBENCH, SOLABENCH,
  WESTMINSTER) — audited as deferred; populate or drop.
- 7 audit memos in `40-BIBLEBENCH/AUDITS/20260705-audit-<pack>.md`. Headlines:
  - **FRUITBENCH** (most developed, 10 virtue designs + authoring guides): rework-with-cookbook-
    standards; gaps = saturation defense, three-layer separation, selective denominational forks.
  - **TENCOMMANDMENTS** + **SERMONMOUNT**: both have same-day design portfolios that grade well
    against the Seven Laws → keep-standalone with bounded reconciliation (T2 anchors, D-flag import,
    CRUX/FRAMESHIFT/UNMARKED de-conflictions; 10C briefs 09 WITNESS + 10 APPETITE still unwritten).
  - **CORINTHLOVE**: merge-into-INTRA as Christianity V-layer seed after rework. One suspect
    citation in its GDM report ("Moral Compactness…") — verify before reuse.
- **Fable overlap map:** `40-BIBLEBENCH/20260705-fruitbench-duplex-intra-overlap-map.md` — the
  ruling: virtue designs 02/04/09/10 re-badge as DUPLEX virtue-conditions (and inherit the P0 risk —
  contribute their manipulation cells to P0); 01/05/07 feed INTRA's V-layer; the novel trio 03
  simmer / 06 backbone / 08 soft-power registers as sketch candidates S9–S11. Selective (not
  blanket) denominational forks — audit's blanket-gap grading partially overruled.

### 3. `10-LITERATURE/` spot-check — CLEAN
21/21 sampled claims VERIFIED (`10-LITERATURE/20260705-lit-spotcheck-report.md`). Layer trustworthy.

### 5. Vault data fixes — 2 FIXED / 2 BLOCKED / 1 DEFERRED (`logs/20260705-vault-data-fixes.md`)
- FIXED: Sabotage Evals (real ID 2410.21514) and Sleeper Agents (2401.05566) — correct PDFs
  downloaded, extracts + card regenerated; stems kept (with old wrong IDs) to preserve 9+ JSON refs.
- BLOCKED: "Sycophancy Probes" (stem cites 2406.09569 = Speech ReaLLM) — *unverified hypothesis:
  this may be the non-arXiv Anthropic Alignment blog post "Simple probes can catch sleeper agents"
  (Apr 2024); verify by web before acting.* "Gemini Safety" (2403.04312 = number theory) —
  *unverified hypothesis: possibly GDM "Evaluating Frontier Models for Dangerous Capabilities"
  (arXiv 2403.13793); verify.*
- DEFERRED: CCAI/Sycophancy card filename swap — 11-file reference map; needs a scripted stem-rename
  pass, not manual edits.
- `validate_all_papers.py` run post-batch: 0 errors.

### ⚠️ Scope-isolation caveat on the BibleBench recommendations
Jimmy has a standing, twice-enforced directive (memory `biblebench-scope-isolation`): when working
*inside* one bench folder, never cross-reference sibling benches — each bench stands alone on its
own corpus; differentiation goes against published literature only. Today's cross-pack audits +
overlap map were explicitly requested by the 20260705b queue and live at the `40-BIBLEBENCH/` root,
not inside bench folders. BUT: the overlap map's integration moves (re-badging FRUITBENCH 02/04/09/10
as DUPLEX conditions, merging CORINTHLOVE into INTRA, importing D-flag machinery) contradict the
stand-alone philosophy if applied inside bench folders. **Treat them as proposals needing Jimmy's
sign-off before any bench-folder edits; bench design sessions keep following the isolation rule.**

## Next-session queue

1. **DUPLEX P0 (Opus session, cross-vendor model runs).** Protocol in revised
   `20-DESIGNS/03-moralpsych-duplex.md` §7; include 1–2 FRUITBENCH manipulation cells per the
   overlap map §2. P0 outcome decides build-first (DUPLEX vs CRUX fallback).
2. **BibleBench paperwork conformance (Opus, no model runs):** X1–X6 sections + saturation defenses
   + selective D-forks into FRUITBENCH/SERMONMOUNT/TENCOMMANDMENTS per audits; write 10C briefs
   09/10; CRUX/FRAMESHIFT/UNMARKED de-confliction paragraphs.
3. **Scripted card stem-rename** for the CCAI/Sycophancy swap (housekeeper tier; reference map in
   the fixes log); resolve the two BLOCKED PDF hypotheses via web verification first.
4. Populate-or-drop decision for the three empty stubs (needs Jimmy).

## Standing cautions (unchanged from 20260705b)
Four sub-project disclosures on cross-vendor numbers; digest stats copied verbatim, never recomputed;
card page refs ±1–2 pp; pre-existing untracked backlog (CULTURAL-GLOBAL/, MORAL-PSYCH/, etc.)
deliberately NOT committed; safety rules hook-enforced; tiering per `~/.claude/CLAUDE.md` +
`.claude/FABLE-WEEK.md` (Fable window ends ~2026-07-11).
