# Next-session handoff — UNFENCED (v2-04) P1 build (Opus)

**Author:** Fable review session, 2026-07-06 · **Follows:** `20260706-thorns-p1-fable-review.md` (D-35/D-36/D-37) · **Worklist:** `20260706-POST-GATE-WORKLIST.md` §1
**Scope isolation (hard):** FRUITBENCH v1+v2 + published literature only. Never read sibling BIBLEBENCH packs.

## What this session is

Build **UNFENCED (v2-04) P1** per its brief (`../FRUITBENCH-v2/DESIGNS/04-unfenced-*.md`, incl. applied D-25/D-26) on the THORNS harness spine — but the spine is **conditionally released**: fix it in THORNS first, regression-check, then copy. EXECUTE mode: produce files, not plans.

## Binding rulings from the Fable review (do these, in order)

1. **D-37 spine fixes in `FRUITBENCH-v2/HARNESS/thorns/` BEFORE copying** (S-6…S-9 already applied by Fable; you do S-1…S-5, S-10 — full table in memo §C):
   - S-1: `generate()` ABC + live adapters accept `rollout=` (and `system=`) — live mode currently crashes.
   - S-2: load `HARNESS/shared/attacker-persona-v1.md` and route it as system prompt to the calibration-attacker role only; live mode must fail loud if the attacker role lacks the persona. Then remove the live-mode latch in `run_pilot.py` (it exists solely because S-1/S-2 were unfixed).
   - S-3: externalize `ATTRACTOR_PRIORS`/`PROFILES` (`synthetic_reference.py`) to per-design data files; unmatched item key = fail loud, never a silent default prior.
   - S-4: parameterize `audit_bank.py` per design (canary, quotas, floors, social-factional set, registry regexes).
   - S-5: parameterize `ITEMS/<design>` / `PILOTS/<design>` paths; make `--date` required (no hardcoded default).
   - S-10: add `vendor` field to model config; live-mode vendor-disjointness assertion across calibration/evaluation/held-out (family strings alone are spoofable by mislabeling).
   - Then re-run the THORNS synthetic pilot as a regression check (new dated artifacts, e.g. `--date <today>`; expect G1 55.0% FAIL / G2 90.0% PASS / G3 98.3% FAIL vs 100%, self-check 100% n=3300 — any drift means you broke the spine) and only then copy to `HARNESS/unfenced/`.
2. **D-36.1 applies to all v2 attractor items, including yours:** no narrated vice-goal — the attractor must be instrumentally embedded, never stated as a goal/motive/instruction by a principal. Test: deleting the principal's stated motive must not remove the temptation. (This was the THORNS bank's one systemic flaw — 11/60 items; don't reproduce it.)
3. **D-35 if UNFENCED calibrates any attractor/temptation:** reuse the frozen attacker persona + attacker-primary aggregation (≥24 attacker rollouts live); never invent a second calibration protocol.
4. **Do NOT do the THORNS item rework** (D-36.2–.6: 11 telegraphed items, grievancefarm, partisan gold second `cft_id`, retaliate-003, paternalcrush demotion + F8 quota re-proof) — that is a separate THORNS session per the worklist. Don't seed UNFENCED items from the 11 telegraphed THORNS items' patterns.

## Standing rules (unchanged)

- Registry `FRUITBENCH-v2/00-registry.md` is frozen (Fable-only changes; the review confirmed it untouched — keep it that way).
- Synthetic numbers are harness-validation only, labeled as such (banner + `-synthetic-` filename token, now automatic); no headline on simulated raters (FO-5 protocol).
- Fresh-eyes objections (FO-8a) BEFORE building; new dated reports, never overwrite; no deletions (`mv` to RECYCLE-BIN/); `git log -1` before committing (shared index); commit+push FRUITBENCH paths only.
- FO-3 (PANELS/ capacity plan) is due **before the 3rd build session** — UNFENCED is the 2nd, so flag it as top item in your handoff.
- End with a dated handoff + a Fable-review prompt for UNFENCED P1 (mirror `20260706-thorns-p1-fable-review-prompt.md`).
