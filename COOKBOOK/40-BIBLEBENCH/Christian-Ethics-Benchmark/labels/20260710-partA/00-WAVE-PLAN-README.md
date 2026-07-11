<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY Part-A human labels — wave plan (COMPLETE full-6-model panel `20260711-o4-panel`)

**What this is:** blind label samples for the §3.4 judge-validation gate (G4). You score the
model responses in each `<design>-partA-blind.csv` against the rubric in the matching
`<design>-partA-instructions.md` — **you never see the model identity or any judge score**
(un-blinding key is `<design>-partA.jsonl`, for the researcher only). Your labels →
`judge_validation.py` → κ vs the two automated judges → G4 per design.

## ALL 10 designs drawn (STABLE — full 6-model panel, 2064/2064)
The panel is complete for all 6 SUTs × 10 designs, so every sample below is final.

| design | units | design | units |
|--------|------:|--------|------:|
| 01-goodsamaritan | 60 | 06-crookedpath | 60 |
| 02-twomasters | 12 | 07-seventyseven | 12 |
| 03-quiettongue | 60 | 08-vocationfork | 60 |
| 04-innerweight | 60 | 09-doubleedge | 25 |
| 05-ordoamoris | 30 | 10-strangergate | 60 |

**439 units total.**

## SHIP ORDER (protocol §8)
- **Wave 1 = {02, 07, 01}** — the top judge-validity risks (02/07 had the lowest pilot judge
  agreement, 0.43/0.49). Suggested order: **02 → 07 → 01** (the two small multi-turn sets
  first, then 01).
- **Wave 2 = {03, 04, 05, 06}.**
- **Wave 3 = {08, 09, 10}.**

## Second labeler
Protocol §3.4 needs a 2nd labeler on the double-labeled overlap for the human–human ceiling
κ (or the disclosed test–retest fallback). Both labelers score the SAME blind CSVs.

## Provenance note
07–10 were drawn *after* `gemini-2.5-pro` completed its 07–10 cells (an OpenRouter credit
top-up + a backend `max_tokens`-reservation fix cleared the 402 stop). All samples are drawn
from the final complete panel, so no re-draw is pending.
