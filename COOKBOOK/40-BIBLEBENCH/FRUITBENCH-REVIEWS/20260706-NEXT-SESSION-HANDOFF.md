# FRUITBENCH — Next-Session Handoff (written 2026-07-06, Fable)

**For:** the next session continuing FRUITBENCH work with a clean context (intended model: **Opus** — the remaining work is execution, not design).
**Read order:** this file → `20260706-POST-GATE-WORKLIST.md` (the authoritative status + instructions doc) → the target design brief → `../FRUITBENCH-v2/OPUS-BUILD-GUIDE.md`.

## Where things stand (as of commit `5f4b89c62`, pushed to origin/main)

1. **FRUITBENCH v1** (`COOKBOOK/40-BIBLEBENCH/FRUITBENCH/`): 10 fruit-major design briefs + AUTHORING/ guides, complete and pushed earlier.
2. **FRUITBENCH-v2** (`COOKBOOK/40-BIBLEBENCH/FRUITBENCH-v2/`): 10 method-major, whole-passage design briefs (each assesses all nine fruit under one unique methodology) + frozen F/W/P construct registry (`00-registry.md` — FROZEN, edits need Fable review) + portfolio doc + `OPUS-BUILD-GUIDE.md`.
3. **Adversarial gate (v1+v2, all 20 briefs): DONE** — memo `20260705-GATE-ADJUDICATION.md` (this folder). 20/20 pass, no kills.
4. **All mandatory gate amendments are already APPLIED in the briefs** (D-12 SOFTPOWER; D-18/19/20 TRELLIS; D-21/22 THORNS; D-25/26 UNFENCED; D-31/32 ROOTSTOCK), as are **all v2 non-blocking orders**. Marked "Gate amendment/order" inline. Do not redo or re-litigate them.
5. **NOT yet done:** (a) the 15 v1 non-blocking amendments — ready-to-paste blocks sit in `20260706-POST-GATE-WORKLIST.md` §2, pasted per-design at that design's build session; (b) every P1 pilot (no item banks or harnesses exist yet); (c) program deliverables in worklist §3 (panel capacity plan due **before the 3rd build session**; shared human-substitution protocol; second-pass Fable gate after 3 P1s).

## What the next session does

**Build v2-02 THORNS P1** (first in the v2 build order 02→04→10→06→01→08→03→07→09→05):

1. Read worklist §1 status table + §4 session template, the THORNS brief (`../FRUITBENCH-v2/DESIGNS/02-thorns-antagonist.md`, including the applied D-21/D-22 amendments), build guide §§1–9, KB docs 01/04/07.
2. Write the 10-line "fresh-eyes objections" note (gate order FO-8a) into `FRUITBENCH-v2/PILOTS/thorns/` before implementing.
3. EXECUTE the P1 per the brief's final section: 135-cell feasibility map; 3 items × 20 priority cells (item YAML per build guide §3, with F/W/P tags and reuse_tags for TRELLIS-M1/STRIDE); attraction calibration on the fixed ensemble; **D-21 frontier transfer check**; **D-22 CFT liveness check**; 3-model pilot; 20-cell mini-heatmap. Gates: ≥70% of items in the 40–80% calibration band, transfer >5% take-rate on ≥60% of cells, CFT liveness ≥5%.
4. Files, not plans (vault orchestration rule). Outputs under `FRUITBENCH-v2/ITEMS/thorns/`, `HARNESS/thorns/`, `PILOTS/thorns/` with `YYYYMMDD-` prefixes on reports.
5. End: update the worklist §1 status table (add rows, never delete), write a dated session handoff, update the FruitBench-v2 memory, commit+push (stage FRUITBENCH paths only — parallel sessions share this git index; check `git log -1` first).

## Standing rules (non-negotiable)

- **Scope isolation:** FRUITBENCH v1+v2 and published literature only; never read sibling BIBLEBENCH packs (CORINTHLOVE/SERMONMOUNT/TENCOMMANDMENTS).
- **Registry is frozen**; briefs' do-not-change lists (now including the gate amendments) bind; conflicts → stop and flag for Fable review.
- Evidence numbers re-cited **verbatim** from `COOKBOOK/30-EVIDENCE/20260705-digests/`; novelty re-check vs post-2026-07 literature per §A8.
- No deletions ever (`mv` to RECYCLE-BIN/); new reports get new `YYYYMMDD-` names; hooks enforce.
- Contested-band >20% of a bank → registry escalation, not silent distributional scoring (FO-6).

## If doing a different task instead

- Another v2 design: same template, next in build order; check its dependencies in build guide §5.
- A v1 design (order 09→06→07→04→01→05→02→08→03→10): FIRST paste its amendment block from worklist §2 into the brief (verbatim, dated), commit that separately, then build.
- Fable-tier work (registry changes, second-pass gate, adjudicating a discovered collision): stop and hand back to a Fable session.
