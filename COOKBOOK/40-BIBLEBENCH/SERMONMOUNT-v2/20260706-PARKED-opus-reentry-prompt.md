# 2026-07-06 — SERMONMOUNT PARKED: Opus Re-Entry Prompt

**Thread state at parking:** WITNESS (v2-09) P1 harness-validation BUILT (`9fcc29cfb`) → **Fable adversarial review DONE** → **Fable pre-registration DONE** (live-P1 rubric + MF-2 statistics pinned). All Fable-tier dependencies for the next several SERMONMOUNT sessions are discharged; everything remaining is Opus-tier or Jimmy-gated.

**Governing doc stack (read in this order on re-entry):**
1. `20260706-fable-witness-p1-adversarial-review.md` — the three rulings (D1 credentials CONDITIONAL GO, D2 §8 reframe applied, D3 shortcut FAIL + rewrite spec) and the binding must-fix list **MF-1…MF-8 (§5)**.
2. `20260706-fable-witness-live-p1-preregistration.md` — **BINDING**: mechanical acceptance checks for every MF (§A1), live-P1 instrument gates G1–G5 (§A3), pathology checklist (§A4), 2-family deviation protocol (§A6), reserved judgments (§A7 — collect and defer, do not conclude), decision synthesis (§A8), and the pinned corrected-gap statistics (Part B: DiD + joint cluster bootstrap + stratified additivity test).
3. `DESIGNS/09-witness.md` — §8 rewritten by Fable review 2026-07-06 (verified prior art: ValAct-15k, Compliance-Gap/BS-Bench, Agent-ValueBench, ValueActionLens); §2/§8 remain LOCKED.
4. The standing stack: gate memo `20260705-fable-adversarial-gate-v1-v2.md` → work order `20260706-opus-gate-corrections-workorder.md` §5 pickup protocol → guide.

**Jimmy owes (blocking the live P1, not the fix session):**
- `ANTHROPIC_API_KEY` (tested slate: claude-haiku-4-5, claude-sonnet-4-6, claude-opus-4-8 + 2 models via codex OAuth CLI).
- Ideally a **Gemini key** — resolves the third-judge-family problem cleanly; otherwise the §A6 deviation protocol runs and Jimmy hand-labels a stratified ≥100-item GEN/ACT subsample.
- Reporting mode already fixed: named internally, anonymized externally.

---

## Paste-ready prompt for the next Opus session (`/model opus`)

```
Continue SermonMountBench (SERMON ON THE MOUNT scope ONLY — scope grep per work order §3.6;
never read sibling benches). This is the OPUS FIX SESSION after the Fable review + pre-registration
of 2026-07-06. EXECUTE, don't plan: end with files, tests, and a dated report.

Read first, in order:
1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/20260706-PARKED-opus-reentry-prompt.md (this file)
2. .../20260706-fable-witness-p1-adversarial-review.md (esp. §4 rewrite spec + §5 MF-1…MF-8)
3. .../20260706-fable-witness-live-p1-preregistration.md (§A1 acceptance checks = your definition
   of done; Part B = the exact statistics to implement)

JOB 1 — apply MF-1…MF-8 to DESIGNS/09-witness/ exactly as specified:
  MF-1 rebuild format-control battery (quantitative matching gate INSIDE format_control.py;
       length ±20%, matched option/tool structure, self-initiated ACT controls, ≥15 bases ×
       4 formats in ≥3 difficulty strata per pre-reg §B4)
  MF-2 implement pre-reg Part B verbatim in gap_surface.py (DiD + joint cluster bootstrap
       B=2000 over cores AND control bases; variance-share diagnostic; stratified additivity
       test; old constant-subtraction CI only behind --legacy-ci); add the §A1 unit test
  MF-3 GEN signal naturalization (no tool tokens; judge on pole_text/paraphrase families)
  MF-4 REC option rewrite per review memo §4 spec (semantic rewrite, NOT padding; length-parity
       gate; strengthen the ~9 dominated counterfeits; shortcut audit must exit 0)
  MF-5 holdout filter in every analysis stage + test
  MF-6 wire _perm counterbalancing into execution + assert
  MF-7 canary out of model-visible prompts (opaque token, no SMB/WITNESS substring)
  MF-8 END validator generic detectors (digits/currency/proper nouns)
Then: re-run the FULL deterministic P1 end-to-end (pytest + all audits green), verify every
pre-reg §A1 acceptance check mechanically, and write a NEW dated report (never overwrite the
2026-07-06 one). The seed-stock ledger stays PROVISIONAL until MF-4 lands — note its status.

JOB 2 — pre-registration items 3–5, using the two Fable docs as templates (these are drafting
jobs bound by existing rulings, not new design decisions):
  (3) judge-calibration stack spec at SERMONMOUNT-v2/SHARED/judges/ (one stack for v1+v2 per
      program directive; gold-vs-counterfeit rubric anchored hardest, with counterfeit
      exemplars in calibration)
  (4) human-baseline study design (brief §6: humans complete matched quadruples on 25% of
      cores; also serves the §A6 deviation subsample)
  (5) LOGSPECK (v1-06) P1 adjudication rubric in the pre-reg's format (LOGSPECK is next on
      the cross-version slate; R-3 reporting-mode marker already in its card)
Anything hitting a LOCKED section or a pre-reg §A7 reserved judgment: FLAG for Fable/Jimmy,
do not decide.

AFTER a live P1 runs (credential-gated): apply the pre-registration MECHANICALLY (§A3–A8).
§A7 reserved judgments are collect-and-defer. G4b (action classifier κ<0.70) is the kill-gate.

Vault safety: no deletions (mv to RECYCLE-BIN/), new dated reports only, YAML lint per file,
commit only when Jimmy asks — stage ONLY SERMONMOUNT + SERMONMOUNT-v2 paths, check git log -1
first (parallel sessions share the index). End with a dated handoff + updated auto-memory
(sermonmount-v2-portfolio-state).
```

---

**After the fix session:** live P1 (keys) → pre-reg adjudication → 240-core build-out (ledger unfrozen) → v1-06 LOGSPECK build. VILLAGE (v2-07) still conditional on two v2 P1 passes. Fable is needed again only for: pre-reg §A7 reserved judgments, any LOCKED-section change, and the post-build-out review.
