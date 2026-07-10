<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY Part-A human labels — wave plan (drawn 2026-07-10 from panel `20260711-o4-panel`)

**What this is:** blind label samples for the §3.4 judge-validation gate (G4). You score the
model responses in each `<design>-partA-blind.csv` against the rubric in the matching
`<design>-partA-instructions.md` — **you never see the model identity or any judge score**
(un-blinding key is `<design>-partA.jsonl`, for the researcher only, not the labeler). Your
labels → `judge_validation.py` → κ vs the two automated judges → G4 per design.

## Drawn now (STABLE — full 6-model panel, will NOT change)
Designs **01–06** are complete for all 6 SUTs, so these samples are final:

| design | units | file |
|--------|------:|------|
| 01-goodsamaritan | 60 | `01-goodsamaritan-partA-blind.csv` |
| 02-twomasters | 12 | `02-twomasters-partA-blind.csv` |
| 03-quiettongue | 60 | `03-quiettongue-partA-blind.csv` |
| 04-innerweight | 60 | `04-innerweight-partA-blind.csv` |
| 05-ordoamoris | 30 | `05-ordoamoris-partA-blind.csv` |
| 06-crookedpath | 60 | `06-crookedpath-partA-blind.csv` |

**282 units total.**

## SHIP WAVE 1 FIRST = {01, 02}  (protocol §8)
Wave 1 was {02, 07, 01} — the top judge-validity risks. **01 and 02 are ready now.**
**07 is DEFERRED** (see below), so wave 1 ships as **{01, 02}** and 07 joins wave 1b once
the panel completes. Suggested order: **02 → 01** (02 is the smaller, higher-risk multi-turn
set), then 03–06 as wave 2.

## DEFERRED (drawn later — do NOT start yet)
Designs **07, 08, 09, 10** are NOT drawn yet: `google/gemini-2.5-pro` did not finish its
07–10 cells (OpenRouter HTTP 402 "requires more credits" — a billing stop, not a data
problem; see the O4 report's coverage note). Drawing them now would sample a 5-model panel
and be **re-drawn** (wasting your labels) once gemini's cells complete. To finish them:
top up OpenRouter credits → re-run `harness/run_o4_panel.sh` (completes ONLY gemini's 127
missing cells) → re-merge → `python -m walkworthy.label_sample --run 20260711-o4-panel
--designs 07-seventyseven,08-vocationfork,09-doubleedge,10-strangergate`.

## Second labeler
Protocol §3.4 needs a 2nd labeler on the double-labeled overlap for the human–human ceiling
κ (or the disclosed test–retest fallback). Both labelers score the SAME blind CSVs.
