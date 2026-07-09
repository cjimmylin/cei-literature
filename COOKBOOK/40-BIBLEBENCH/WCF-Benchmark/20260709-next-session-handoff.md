# WCF-Bench — Next-Session Handoff (clean-context re-entry)

**Date:** 2026-07-09 · **Written by:** Fable (end of design phase) · **Intended executor:** Opus (or any post-Fable session)
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

---

## 1. What this project is (one paragraph)

WCF-Bench is a suite of **10 method-major benchmark designs** measuring whether LLMs **act** (not just opine) in accordance with the ethical teaching of the **Westminster Standards** (WCF / Larger Catechism / Shorter Catechism, 1647 — the ONLY normative sources; the sibling `Christian-Ethics-Books/` folder and all sibling benches in `40-BIBLEBENCH/` are out of scope). Content is constant (every design tests the full Decalogue + cross-cutting structures); only the measurement methodology varies: DUTYBOUND (omissions), COMPLICIT (participation gradients), AGGRAVATE (Q151 severity calculus), STEADFAST (pressure ladders), CROSSWIND (say-do triples), LIBERTY (conscience triage), PROOFTEXT (grounding + twist refutation), MENDING (repair arcs), WHOLEHEART (matter/manner/end), NARROWGATE (obedience-cost dials).

## 2. Current state (as of commits `5120233ce` → `039d73567`, all pushed)

- **Governing docs** in `00-OVERVIEW/`: master spec · shared spine (BINDING: tiers T1–T4, scoring, perturbations P1–P6, contamination + canary `WCFBENCH-CANARY-c1647-x9k4q`, gates G1–G7, item schema §10) · Westminster anchor registry · PRD · build plan.
- **Item bank: 161 items, all Fable-authored or Fable-reviewed:**
  - 49 wave-1 Fable exemplars (inside the 10 specs, `01-DESIGNS/NN-<name>.md` §6)
  - 50 Opus expansion items (`01-DESIGNS/expansions/`) — ALL now REVIEWED-PASS
  - 62 wave-2 Fable exemplars (`01-DESIGNS/exemplars-wave2/`) — the **Fable 10×10 exemplar matrix is COMPLETE** (every design × commandment cell has a Fable pattern) + 1 cross-cutting exemplar per design (WCF 15/16.6/20/22, Q185, Q194, means of grace). Every wave-2 exemplar ends with an **Opus note** = its flesh-out recipe.
- **Binding review rulings:** `20260706-fable-review-memo.md` (R1–R7) + `20260707-fable-review-addendum.md` (upgrades + self-flagged edges). Do not relitigate; queue disagreements as `[NEEDS-RULING]`.
- **Authoring protocol:** `03-OPUS-GUIDE/20260706-item-authoring-guide.md` (BINDING — non-negotiables, checklist, kill-criteria, escalation rules).
- **Deck:** `02-DECK/20260706-wcf-benchmark-deck.html` (17 slides; structurally verified; **browser visual check still pending**).
- **No code/harness exists yet.** The vault has NO API keys and NO live LLM runner — Phase 2 is mock-first by design.

## 3. Sharp edges (read before touching anything)

1. **Report immutability:** never edit existing dated files or the Fable spec/exemplar files. New work → NEW dated files (`YYYYMMDD-` prefix). Errata are appended as notes in new files.
2. **Registry source-split:** the primary LC file `../WCF/03-LCLayout2 copy.txt` begins ~Q114; WLC Q1–113 clauses must be grep-verified against `../WCF/LargerCatechismwithScriptureProofs1 copy.txt`. Never key an anchor from memory.
3. **Scope isolation:** never cross-reference sibling benches (WALKWORTHY, 10CBench, etc.) or `COOKBOOK/20-DESIGNS/`.
4. **No deletions anywhere in the vault** (`mv` to RECYCLE-BIN only); hooks enforce this.
5. **Parallel sessions share the git index:** check `git log -1` before committing; stage this project's paths explicitly and atomically.
6. **Cross-design seams:** DUTY-XC-W206 ↔ NARROWGATE (vow dials); CROSS-XC-W207 ↔ PROOF-XC-W206 (Lord's Prayer families) — read both sides before authoring in those seams.

## 4. Next session's work queue (in order)

**Task 1 — Deck visual check (30 min):** `cd 02-DECK && python3 -m http.server 8765`, open via Playwright, verify all 17 slides render + arrow-key nav; fix nits in place (the deck is the one file that may be edited — it is a build artifact, not a dated report).

**Task 2 — Flesh-out batch 1 (the main work):** expand item banks by imitating wave-2 exemplar patterns. Per design: pick 2–3 wave-2 exemplars, author 2–4 sibling items each per the exemplar's **Opus note** (rotate surfaces per its rotation list; never duplicate scenarios — check the design's spec §6, its wave-2 file, AND its expansion file first). Recommended design order (de-risks the harness, per build plan): **03 AGGRAVATE → 10 NARROWGATE → 07 PROOFTEXT**, then the rest. Output: `01-DESIGNS/expansions/2026MMDD-<design>-expansion-2.md`, full guide-§6 protocol (item schema, self-audit lines, coverage table, grep-verified anchors, canary once).
- Every batch: ≥1 control/two-sided item per 3 traps (design-specific: clean controls / G3-G4 cells / incomparable pairs / rightly-applied twists / anti-`[DISPUTED]` traps / clean-run keys).
- Park anything ungroundable as `[NEEDS-RULING]` — never guess a key.

**Task 3 — Harness skeleton (if session has capacity), per `00-OVERVIEW/20260706-build-plan.md` Phase 2:** YAML item-record loader (spine §10 schema) · NARROWGATE episode state machines · mechanical scorers (ordinal distance + transitivity for AGGRAVATE; citation/apparatus matching for PROOFTEXT; artifact checks for NARROWGATE) · judge-prompt templates generated from rubrics · MockModelClient dry-run (NO live API calls; mock-first like prior vault benches). New code lives under a new `04-HARNESS/` directory.

**Task 4 — Session close:** run any YAML validation if paper files were touched (they shouldn't be), write a new dated session handoff, commit + push atomically.

## 5. Standing items blocked on Jimmy (do NOT attempt)

- **API keys** → gates Phase 3 pilots (3+ frontier models, cross-family judges).
- **G6 confessional rater panel** → gates gold-label confirmation; specifically queued: LIB-C7-008 + LIB-C3-W202 named-parties confirmations; rulings R1/R3/R4.
- **Attorney sanity-check** of MEND-C3-W202 (perjury-correction counsel) before that item enters any public release.
- Frozen surfaces (spine tiers/gates/canary/schema, registry citation format, review rulings) are Jimmy-or-Fable-tier only; propose changes via `[NEEDS-RULING]` notes.

## 6. File map (quick reference)

```
00-OVERVIEW/  20260706-{master-spec,shared-spine,westminster-anchor-registry,prd,build-plan}.md
01-DESIGNS/   01-dutybound.md … 10-narrowgate.md          (specs + wave-1 exemplars; FROZEN)
              expansions/20260706-<design>-expansion.md    (Opus wave; REVIEWED; FROZEN)
              exemplars-wave2/20260707-<design>-fable-exemplars-w2.md  (Fable patterns + Opus notes; FROZEN)
02-DECK/      20260706-wcf-benchmark-deck.html             (editable build artifact)
03-OPUS-GUIDE/20260706-item-authoring-guide.md             (BINDING protocol)
20260706-fable-review-memo.md · 20260707-fable-review-addendum.md   (BINDING rulings)
20260706-wcf-benchmark-handoff.md · 20260707-wave2-handoff.md · this file
Sources:      ../WCF/*.txt  (the five Westminster texts — the only normative ground)
```
