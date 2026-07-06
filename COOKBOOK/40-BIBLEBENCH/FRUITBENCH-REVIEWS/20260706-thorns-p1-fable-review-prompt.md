# Next-session prompt — Fable adversarial review of THORNS (v2-02) P1

**Paste the block below into a fresh Fable session** (`/model fable`, clean context). It is the "Opus builds → Fable reviews" step for the first FRUITBENCH-v2 P1, done now because the harness spine + item-craft templates are about to propagate to the other 9 designs (UNFENCED is next in build order). **This is NOT the scheduled second-pass FO-8 gate** — that is due only after 3 P1 pilots exist *and* real (credentialed) pilot data exists; both are still pending.

---

You are Fable. An Opus session built **THORNS (FRUITBENCH-v2 design 02) P1** on 2026-07-06 (commit `62714d11f`, on origin/main). Your job this session is to **adversarially review that build and rule on the design questions it surfaced, before its harness spine and item-craft templates propagate to the remaining 9 v2 designs.** Decide; don't just observe.

**Scope isolation (hard):** FRUITBENCH v1+v2 and published literature only. NEVER read sibling BIBLEBENCH packs (CORINTHLOVE, SERMONMOUNT, TENCOMMANDMENTS, WESTMINSTER, ARMOURBENCH, SOLABENCH, 10CBench).

**Context hygiene (Fable tokens are expensive):** delegate the heavy reads/audits to subagents with an explicit `model=` — Opus for judgment-adjacent reads/spot-audits, Sonnet for mechanical scans — and keep the adjudication in your main loop. Do not read the whole 60-item bank into your own context; have an Opus subagent sample it and report.

**Read order (start here):**
1. `FRUITBENCH-v2/PILOTS/thorns/20260706-p1-pilot-report.md` — the map of the whole build (real-vs-synthetic split, gate verdicts, the 2 flagged questions in §4.1/§7, systemic notes S1–S3 in §2).
2. Same dir: `20260706-fresh-eyes-objections.md`, `20260706-feasibility-map.md`, `20260706-mini-heatmap.md`.
3. `FRUITBENCH-v2/DESIGNS/02-thorns-antagonist.md` (esp. D-21/D-22 + the do-not-change ledger) and `FRUITBENCH-v2/00-registry.md`.
4. Harness: `FRUITBENCH-v2/HARNESS/thorns/{run_pilot,synthetic_reference,scorer,model_adapters}.py`, `pilot_config.json`; `FRUITBENCH-v2/HARNESS/shared/{attacker-persona-v1,human-substitution-protocol}.md`.
5. A sample of items (bank + gold): the 3 exemplars (`envy-002`, `craving-001`, `retaliate-003`) + the 5 fixed items (`approvalidol-003`, `resentjoy-002`, `strifepeace-002`, `metricvow-003`, `creditvow-003`).

**Rule on these (produce a dated decision memo `FRUITBENCH-REVIEWS/YYYYMMDD-thorns-p1-fable-review.md`):**

A. **Calibration-band aggregation (blocking; frozen-adjacent).** The brief freezes the calibration *ensemble* but not the *aggregation* over it, and it materially moves G1 (synthetic: ensemble-mean 63.3% vs attacker-primary 55.0% band-pass). RATIFY one of {ensemble-mean, attacker-primary, max-over-probers} (or define another), justify it, and specify it in the brief + `run_pilot.py`. This is on the do-not-change surface, so it needs your ruling, not a builder's.

B. **Frontier-attractiveness / ceiling-map risk.** The real-model probe (report §3) showed the vice path only weakly attractive to a frontier model *even in the frozen attacker persona*. Rule on: (i) is the D-21 transfer threshold (>5% take on ≥60% of cells) strong enough, or does it need raising / a deeper-embedding rework standard; (ii) do the telegraphed social-factional cells (S3: `resentcorrect`≈`partisan`; principals narrate the unfair ask) and the novel/limit cells (`grievancefarm` P9, `paternalcrush` W14) need a mandated rework before bank expansion.

C. **Spine-propagation go/no-go (blocking for UNFENCED).** Is the harness architecture (pluggable adapters + role-family disjointness guard; four-bucket Fi/Wj/CFT/mixed scorer; gate definitions; the synthetic-labeling discipline that keeps synthetic ≠ empirical) and the item-craft template (2-file bank/gold split, the dyad recipe, the 5 applied fixes, `cft_status: latent` convention) sound enough to **copy** into UNFENCED and the other 8 designs? Name every change required before it propagates.

D. **Adversarial spot-check — try to find a KILL the Opus review missed.** Especially construct-bleed on the convergence-watch cells (F4×W9 vs v1 LONGFUSE, F9×W15 vs v1 MARSHMALLOW, F2×W15 vs F9×W15) and the S1 (capability-detectable right-action) / S3 (telegraphed polarity) patterns. Confirm the 5 fixes actually resolved their findings and introduced no regressions.

E. **Integrity.** Confirm nothing silently edited the frozen registry and nothing crossed scope isolation. If you decide the registry itself needs a change, make it a Fable-authored, logged change — not a silent one.

**Deliverables:** the decision memo; any brief/harness edits your rulings require (applied + dated + marked "Fable review ruling YYYY-MM-DD"); a one-line addition to the worklist `20260706-POST-GATE-WORKLIST.md` §1 status table (add a row, never delete); and a short handoff for the next Opus session (UNFENCED build) stating which of your rulings bind it. Commit + push FRUITBENCH paths only — check `git log -1` first (parallel sessions share the index), stage atomically, no deletions (`mv` to RECYCLE-BIN/), new reports get new dated names.

**Explicitly out of scope this session:** the FO-8 second-pass empirical gate (needs 3 P1s + credentialed pilot data — neither exists yet); building UNFENCED (that is the next *Opus* session, informed by your rulings).

---
