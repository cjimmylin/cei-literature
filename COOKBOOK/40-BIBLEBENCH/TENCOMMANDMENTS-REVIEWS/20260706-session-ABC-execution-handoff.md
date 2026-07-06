# 20260706 — 10CBench Revision Sessions A/B/C: Execution Handoff

**Author:** Opus execution session, 2026-07-06 · **Authority executed:** `20260706-revision-orders.md` (§A/§B/§C) against `20260705-GATE-ADJUDICATION.md` (TC-1…TC-12). **No design decisions were made — locked specs were expanded/applied only.**

## Status: ALL THREE SESSIONS DONE + PUSHED

| Session | Scope | Commit | Acceptance |
|---|---|---|---|
| **A (v1)** | 2 new scaffolds (09-WITNESS, 10-APPETITE) + §A.1 edits to 01-08 + portfolio | `0ca0665fa` | all §A greps pass |
| **B (v2)** | B.1 cross-file + B.2 per-design edits to 01-10 + portfolio | `5daef77b0` | all §B greps pass |
| **C (v3)** | 00b-inheritance-registry (TC-7) + C.1/C.2 edits to 01-10 + portfolio | `6b10fc2b8` | all §C greps pass |

All commits pushed to `origin/main`. Every edited/new file carries a `## Revision log — 2026-07-06 gate fixes` section. Track B (B1–B6) verified untouched across all 28 edited design files (0 Track-B header intrusions in every diff). Pre-commit hooks (YAML/imports/tests/staged-count) passed on all three commits.

### Verification performed (independent of agent self-reports)
- §A: `ls` 09/10 ✓; Revision log ×11 ✓; 01 "BF≥10"+"P0 gate" ✓; 05 "smallest-cell" ✓; 07 "κw" ✓; portfolio "descriptive at N" ✓.
- §B: Revision log ×11 ✓; 02 "Kendall" ✓; 07 "≥80%"+"≥12" ✓; 09 "Spearman" ✓; portfolio "compliance table" ✓.
- §C: `ls` 00b ✓; Revision log ×12 ✓; 01 "within severity tier"+"270" ✓; 02 "integration" ✓; 04 "embedded–explicit" ✓; 07 "ceiling" ✓; 10 "≥5" ✓; portfolio "Stage 1" ✓.

## NEXT STEP (per the queue): Fable spot-check → release TC-9 first build wave

Per adjudication §5.4 / revision-orders "Post-revision": in a **Fable** session, read the two new scaffolds end-to-end + one revised design per session against the adjudication memo; verify acceptance greps; then release the **TC-9 first build wave: ZEROSUM → SKIM → PALTER (BT gate early) → TABLETS (panel recruitment starts immediately) → SOVEREIGN (L2-P0 first, then L1)**.

## ⚠️ ONE DELEGATED AUTHOR'S-CHOICE — confirm at spot-check

- **06-UPSTREAM MR construct (R2-F6).** The adjudication offered two authorized resolutions ("rename to legal-taxonomy calibration" OR "add a legal↔moral divergence arm" — *author's choice, disclosed*). This execution session chose the **rename to "legal-taxonomy calibration"** (surgical, no new sub-construct invented — the execution-safe reading), and logged it in 06's revision log. **If Fable prefers the richer divergence-arm option** (which the adjudication notes is cheap via PROVENANCE's legality×morality machinery and preserves the moral-calibration construct), that is a one-session follow-up — the rename does not preclude it. Flagged because it is the only place the orders delegated a genuine choice rather than a fixed edit.

## Agent-flagged judgment calls (all logged in-file; verify at spot-check)

1. **TC-2 "at ceiling" had no default operationalization** in the orders' default map (only ≈/uniform/flat/never were given defaults). Agents chose sensible bars and logged each: e.g., SELAH YD → "≥95% yield in every dose cell"; PALTER DT → "detection ≥95% / d′ within 0.2 of arm max"; several → ">98% of cells". Consistent and disclosed, but not centrally specified.
2. **TC-4 scoping.** Agents applied "(descriptive at N≤9 model subjects; no significance claims)" to genuine cross-model *correlations*, but deliberately **not** to go/no-go *gate thresholds* (e.g., capability-corr <40%), since tagging a pre-registered decision rule "no significance claims" would corrupt its semantics. Correct call; noted here for transparency.
3. **03-PROXY PL / other non-trigger falsifications.** A few A2 conditions use words outside the TC-2 trigger list ("uncorrelated", "uncorrelated"); left as pre-registered slope/CI checks and logged. If a numeric bar is wanted there too, it's a one-line follow-up.
4. **00b registry coverage.** Table 1 C1–C8 rows are marked "(source inferred from commandment mapping — verify at spot-check)" per the orders (no v3 design names a concrete v1/v2 source). **TABLETS + CASUIST intentionally excluded** from Table 1 (they rest on named independent gold — casuistic/necessity corpora — not v1/v2 clear-band-core inheritance); documented in a note. **LOOPHOLE included but flagged gold-free** (uses each commandment's scope core as fixed content, inherits only CASUIST's never-valid floor). **PREFACE has no literal "A9.3"** — the outcome-cell binding lives in A9 risk item 3 + build instructions; the registry states this mapping explicitly.

## Open items beyond the queue (carried from the trilogy handoff — NOT addressed here)

- Co-registration notes owed before builds: TABLETS×CRUX, LOOPHOLE×FRAMESHIFT, TURNCOAT×FRAMESHIFT, PRISM×VERNACULAR, TACIT×DISCORD.
- Panel recruitment is the true critical path (~5 shared panels, TC-12) — start casuistry-panel recruitment (TABLETS+CASUIST) as soon as the wave releases.
- X6 nearest-neighbor tables should be re-checked against live literature before any submission.

## Notes for whoever runs the build wave

- **Parallel sessions share the git index.** During this session HEAD moved twice under sibling Fable sessions (fa6fa9eed→ba9e77fec→66a22ea0c, all in `20-DESIGNS/`, no overlap with `40-BIBLEBENCH/`). Always `git log -1` + intersection-check before staging; stage only your own paths.
- Scope stayed isolated to Ten Commandments folders + the registry; no sibling bench was read or touched.
