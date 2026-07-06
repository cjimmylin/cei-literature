# 20260706 — TENCOMMANDMENTS Trilogy Handoff (Fable sessions, 2026-07-05/06)

**For the next session.** Everything below is committed and pushed to origin/main through `e628e1d0d`.

## What exists (in `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/`)

| Artifact | Path | State |
|----------|------|-------|
| v1 portfolio (construct per commandment) | `TENCOMMANDMENTS/DESIGNS/` | 8 scaffolds + portfolio; **09-WITNESS & 10-APPETITE missing**; 6/8 validity-blocked at gate — fixes specified, not yet applied |
| v2 portfolio (second orthogonal construct per commandment) | `TENCOMMANDMENTS-v2/DESIGNS/` | 10 full scaffolds + portfolio (TURNCOAT, GOLEM, PROXY, SELAH, HEIRLOOM, KEEPER, PARAMOUR, SKIM, PALTER, ZEROSUM); all pass-with-fixes — fixes not yet applied |
| v3 portfolio (10 methodologies, each over all ten commandments) | `TENCOMMANDMENTS-v3/DESIGNS/` | 10 full scaffolds + portfolio (TABLETS, VILLAGE, PRISM, TACIT, CASUIST, LOOPHOLE, VERNACULAR, DISCORD, ASSEMBLY, PREFACE); 3 blocks repaired-on-paper — fixes not yet applied |
| Adversarial gate (R1–R7 + adjudication) | `TENCOMMANDMENTS-REVIEWS/20260705-*.md` | DONE. Adjudication memo = binding law (dispositions + orders TC-1…TC-12; no design killed) |
| **Revision orders (THE next-work document)** | `TENCOMMANDMENTS-REVIEWS/20260706-revision-orders.md` | Written, NOT executed. Fully executable file-by-file instructions for sessions A/B/C, incl. locked design specs for the two missing v1 scaffolds and per-session acceptance greps |
| Session handoffs | `TENCOMMANDMENTS-v2/20260705-v2-session-handoff.md`, `TENCOMMANDMENTS-v3/20260705-v3-session-handoff.md` | Background context per portfolio |

## The work queue (strict order)

1. **Session A (v1)** — per revision-orders §A: FIRST write `09-witness-no-false-witness.md` and `10-appetite-no-coveting.md` from the locked specs (TC-1 blocks all other 10CBench work behind these), then apply the per-design v1 edits with revision logs. Run the §A acceptance greps.
2. **Session B (v2)** — per §B: numeric thresholds everywhere (TC-2), P0 gate numbers into PARAMOUR (≥80% on ≥12 contrasts) and PALTER (Spearman ≥0.6), GOLEM EFA gate (Kendall's W ≥ 0.6), per-design edits, portfolio compliance table. Acceptance greps.
3. **Session C (v3)** — per §C: FIRST write `00b-inheritance-registry.md` (TC-7), then identification repairs (VERNACULAR ceiling-gating, PREFACE ≥5 arm-texts, TACIT re-scope to "embedded–explicit gap", TABLETS within-tier Bradley–Terry + corrected 270-item quota, VILLAGE repositioning) and portfolio §2/§9 amendments. Acceptance greps.
4. **Fable spot-check** (bring results back to a Fable session): read the two new scaffolds + one revised design per session against the adjudication memo; then release the **TC-9 first build wave: ZEROSUM → SKIM → PALTER → TABLETS → SOVEREIGN (L2-P0 first, then L1)**.

Sessions A/B/C are independent of each other EXCEPT: B's PALTER/ZEROSUM de-confliction edits and C's inheritance registry cite the new v1 09/10 scaffolds — so run A first (or A in parallel with the non-citing parts of B/C).

## Rules that bind every future 10CBench session

- **Model tiering:** revision/build sessions run on Opus (`/model opus`); Fable only for adjudication/spot-checks. Subagent dispatches always carry explicit `model=`.
- **Scope isolation:** Ten Commandments folders + `COOKBOOK/00-KNOWLEDGEBASE/` + `COOKBOOK/20-DESIGNS/REVIEWS/20260705-adjudication-memo.md` (X1–X6) only. Never read sibling benches (SERMONMOUNT/CORINTHLOVE/FRUITBENCH…).
- **TC-orders are law:** numeric gates (TC-2), power-before-profiles (TC-3), model-N descriptive (TC-4), sim≠outcome vocabulary (TC-5), corrected arithmetic incl. ~4× realized counts (TC-6), inheritance registry (TC-7), collision routing (TC-8), build order (TC-9), v1 X-retrofit (TC-10), Two-Tables descope (TC-11), shared panels (TC-12).
- **Editing discipline:** revise in place with `## Revision log — 2026-07-06 gate fixes` sections; never touch Track B (B1–B6); reports/logs get new `YYYYMMDD-` files, never overwrite; no `rm` ever (RECYCLE-BIN only); stage+commit atomically, check `git log -1` first (parallel sessions share the index), push after commit.
- **EXECUTE, don't plan:** agents must produce file changes; verify outputs exist after every dispatch.

## Known open items beyond the queue

- Co-registration notes owed before builds: TABLETS×CRUX, LOOPHOLE×FRAMESHIFT, TURNCOAT×FRAMESHIFT, PRISM×VERNACULAR, TACIT×DISCORD.
- Panel recruitment is the true critical path (~5 shared panels per TC-12) — start casuistry-panel recruitment (TABLETS+CASUIST) as soon as the wave releases.
- X6 nearest-neighbor tables should be re-checked against live literature before any submission.
