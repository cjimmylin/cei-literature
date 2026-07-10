# Next-session prompt — CORINTHLOVE bank build ② CHARITROC

State as of 2026-07-06 (commit `7f18029f8`, pushed): all 28 briefs gate-revised; STATUSGAME re-gate discharged; megamatrix analysis pre-registered; bank-review rubric authored; DIMGLASS (CO-8 ①) built, Fable-reviewed, fixed, GO. No Fable dependency remains — run this on Opus.

Paste the block below as the first message of a fresh session (run `/model opus` first).

---

Continue the CORINTHLOVE benchmark workstream: build the CHARITROC question bank (v1-07, CO-8 order ②). Start by reading, in this order:

1. `COOKBOOK/20260706-corinthlove-next-session-handoff.md` — §3 binding rules only (its §2 queue is superseded: revisions, STATUSGAME re-review, and DIMGLASS are all DONE and pushed at `7f18029f8`).
2. `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-dimglass-bank-review.md` — especially §6 propagation orders **P-1…P-3, which are BINDING on this build** (fail-loud cell-coverage asserts for every declared design cell; defeat-class matching for any paired/matched arms, never non-sequitur invalids; document every deviation from the brief at build time).
3. `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-fable-bank-review-rubric.md` — your build will be adversarially reviewed against items A1–E; build to survive it.
4. `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-fable-megamatrix-analysis-prespec.md` §3 — the episode-level export contract + declared coverage map (fixed BEFORE pilot; CHARITROC is a v1 bank → family-code clause, crosswalk-mapped only).
5. `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/DESIGNS/07-charitroc.md` — the gate-revised brief (D-07: empirical ordinal ROC/AUC, explicit cost-ratio operating points, stage-3 updating split out). Its §12 Phase A checklist is the work order; Phase B items are protocol documents only (no live model calls — the vault has no API credentials).
6. `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-v2/BANKS/09-dimglass/` — the GO-reviewed reference implementation; reuse its structure and discipline (generator + lib + scorers with fixtures + synthetic recovery + tests + selfcheck + adversarial pass + export + reports) adapted to CHARITROC's design. v1 has no 98 guide — where the brief is silent, resolve by analogy to DIMGLASS and log the choice in your handoff.

Then EXECUTE the build under the standing discipline: build location `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE/BANKS/07-charitroc/`; canary registry at `CORINTHLOVE/BANKS/canary_registry.txt` with `10CB-07-` GUIDs; generator-based authoring (no fixed item lists); fixtures + synthetic-recovery asserts BEFORE scale; sidecar-only ground truth; fail-loud count asserts; static adversarial filter run and documented (frontier-model pass deferred, credential-gated); every mock result labeled "harness validation, NOT a measurement". Use `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`.

Scope guards: 1 Corinthians 13 only — never open or reference any sibling bench under 40-BIBLEBENCH beyond CORINTHLOVE*/CORINTHLOVE-REVIEWS; never cite the icmi-proceedings "moral compactness" statistics; no deletions (RECYCLE-BIN only); do not commit unless I ask.

After the build passes its own suite: run the adversarial review per the rubric's protocol — a FRESH Opus reviewer (subagent with explicit `model=opus`, or separate session) that reads only the rubric, brief, gate orders (D-07 + P-1…P-3), and bank artifacts, and writes `CORINTHLOVE-REVIEWS/2026MMDD-charitroc-bank-review.md` with a GO / CONDITIONAL GO / FAIL verdict and evidence. Apply CONDITIONAL GO fixes and re-verify; a FAIL or any rubric-C6/frozen-surface question escalates to me — do not improvise.

Finish with: verification outputs pasted into a dated handoff (`COOKBOOK/2026MMDDx-corinthlove-charitroc-build-handoff.md`, next free letter suffix); memory update (`corinthlove-v3-portfolio-state.md` next-step line → CO-8 ③ CROSSROADS).

---

Afterward, the same prompt recycles for ③ CROSSROADS (v3-01 — use the v3 98 guide incl. its §7 interim hardness gate, C1–C16 clause tags from the FROZEN registry, `10CB3-` canaries) → ④ AGAPEGAME (v3-05) or WITNESS (v3-04) → ⑤ MANYMIRRORS (v3-03, gated on the prespec §4 two-method concordance gate). Standing Jimmy items: DIMGLASS norming-study raters (precondition for discernment claims); API keys for Phase B — if keys arrive before ~2026-07-11, bring the first live calibration run to a Fable session before anything else.
