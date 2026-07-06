# 10CBench — Fable Spot-Check Verdict & TC-9 First-Wave Build Release

**Author:** Fable, 2026-07-06 (spot-check session per adjudication §5.4) · **Authority:** `20260705-GATE-ADJUDICATION.md` (TC-1…TC-12) + `20260706-revision-orders.md` · **Inputs:** end-to-end reads of v1 09-WITNESS, v1 10-APPETITE, v3 00b-inheritance-registry (mandatory); first-wave reads of v1 01-SOVEREIGN, v2 09-PALTER, v2 10-ZEROSUM, v2 08-SKIM, v3 01-TABLETS, plus v1 06-UPSTREAM (for ruling §2.1); independent re-run of all §A/§B/§C acceptance greps (19/19 PASS).

---

## 1. Spot-check verdict: PASS — the TC-9 first wave is RELEASED (§4)

The A/B/C revision execution is faithful to the adjudication and the locked specs. No substantive drift from any LOCKED spec was found; no correction-order session is needed. Eight trivial defects were found and **fixed in place this session** (each logged in the owning file's revision log, tagged `Fable spot-check 2026-07-06`):

| # | File(s) | Defect | Fix |
|---|---|---|---|
| 1 | v2 07-paramour (§0, do-not-change list) + v2 portfolio (§1, metric families) | **TC-5 violation**: "outcome-grounded" survived for PARAMOUR-DS in 4 places. TC-5 names PARAMOUR-DS explicitly; the P0 sim-calibration gate is not a human-referent validation | Relabeled per the TC-5 standard vocabulary; human-referent sentence added to the pitch |
| 2 | v1 01-sovereign A2 | TC-2 gap: DR/HS/DL falsifications kept soft terms (≈0, "always", "flat") — the orders' item list never spelled these out for SOVEREIGN | Operationalized per the §B.1 default map (rank r≥0.9 + top-1 agreement; >98% of arcs; range <10 pts) |
| 3 | v2 09-palter A2 | IF "trade off perfectly" had no number | Item-level IF–PR correlation ≤ −0.9 within every model |
| 4 | v3 01-tablets Opus block | **TC-6 arithmetic error introduced by the revision itself**: quota breakdown sums to 270+72+45+~135 ≈ **520**, stated as "≈450"; the generic 4×-nominal boilerplate contradicted the explicit breakdown | Corrected to ≈520; 4×-nominal note superseded by the explicit breakdown |
| 5–6 | v1 09-witness, v1 10-appetite Opus blocks | Locked §A.0 specs' explicit JSONL field additions were omitted | Restored (`claim_status/reputational_stakes/process_context/pressure_tier`; `affordance_tier/sufficiency_map_id/da_direction`) |

**Mandatory-read findings.** WITNESS and APPETITE are faithful expansions of the LOCKED §A.0 specs and are born gate-compliant: all axes carry numeric falsifications (TC-2), X2 audit blocks present (A6), X4 power notes present and mandated pre-pilot (A7), X6-scoped novelty with named neighbors (A8), TC-6 realized-count arithmetic correct (160→~640 each), and the binding de-confliction routing matches the specs exactly. The **registered SOVEREIGN↔APPETITE cross-analysis is correctly written into 10-appetite**: hypothesis directional-but-both-reportable, TC-4 descriptive framing, unblind only after both P1 pilots complete with gates passed, analyst blind until locked. APPROVED as the pre-registration of record.

**00b-inheritance-registry: ACCEPTED as single source of truth.** The C9/C10 rows are LOCKED with narrowing correctly disclosed (PALTER composition-level/false-atoms-excluded; ZEROSUM payoff-scoped). The TABLETS+CASUIST exclusion is correct (named independent casuistic gold, not v1/v2 inheritance) — which also means **no first-wave build is gated on the C1–C8 inferred rows**. Ruling on those rows: the natural 0N mapping is the only defensible reading and is ACCEPTED; the "(source inferred — verify at spot-check)" flags REMAIN in place and are resolved per-design when each inheriting v3 design (all second-wave or later) reaches its build session, by confirming the named A5 clear band actually supports that design's cell family. The class-1 TC-8(a) LOCKED note and the PREFACE "A9.3" mapping disclosure are both correct.

## 2. Rulings on the two open decisions

1. **06-UPSTREAM MR construct (R2-F6): the RENAME is CONFIRMED.** The executed rename to "legal-taxonomy calibration" is honest, surgical, and internally consistent (A1/A2/A3/A8 all relabeled; the bar-exam-correlation falsification correctly inverted to "expected, not fatal" under the new construct). The divergence-arm option is NOT ordered now: UPSTREAM builds only after its block-fixes anyway (it is not in waves 1–2's front), the arm would add contested-band panel demand exactly when panel recruitment is the program's critical path (TC-12), and the adjudication's own note stands — the rename does not preclude adding the arm later. Standing disposition: the legal↔moral divergence arm remains an **authorized optional enhancement**, decided at UPSTREAM's build gate; if added, it reuses PROVENANCE's legality×morality machinery and restores a moral-calibration sub-construct under a new axis code (never silently re-widening MR).
2. **Agent-flagged TC-2/TC-4 calls: CONFIRMED as executed.** (a) The per-design "at ceiling" operationalizations (SELAH YD ≥95%/cell; PALTER DT ≥95% or d′ within 0.2 of arm max; ">98% of cells" elsewhere) are sensible, disclosed in-file, and now pre-registered — they are FINAL per TC-2's post-pilot-change prohibition. (b) The TC-4 scoping — descriptive tags on cross-model *correlations* only, never on pre-registered go/no-go *gate thresholds* — is correct: a decision rule is not a significance claim, and tagging it "no significance claims" would corrupt its semantics. This scoping is now the portfolio-wide interpretation of TC-4.

## 3. Non-blocking notes for build sessions (one-liners; do at the owning design's build gate)

- **PROXY PL** (and any other A2 condition using off-list soft words like "uncorrelated"): give the slope/CI check an explicit numeric bar when PROXY builds (second wave).
- **Discrimination-gate "≥20-pt spread" convention:** several headline metrics are not natively 0–100 (SOVEREIGN lexical-priority index, SKIM θ, WITNESS d′, TABLETS ladder dispersion). Each build session must define, in its pilot report, the metric's mapping to the portfolio 0–100 scale (or an equivalent pre-registered spread criterion) **before** running the gate.
- **X6 nearest-neighbor tables** must be re-checked against live post-2026-07 literature before any submission (carried from the trilogy handoff).

## 4. RELEASE: TC-9 first build wave (greenlit 2026-07-06)

Bank-building Opus sessions are authorized in this order — **ZEROSUM → SKIM → PALTER → TABLETS → SOVEREIGN** — one design per session, each session loading KB docs 01/04/06/07 + its brief + its portfolio §§ + this memo §3. Entry gates (from the briefs; binding):

| Order | Design | Entry gate before bank-scale work | First deliverable |
|---|---|---|---|
| 1 | **ZEROSUM** (v2 10) | Advice-classifier calibration set (human-coded, ≥200 responses) built and validated to the pre-registered agreement bar BEFORE any model scoring; generator + structure-certificate emitter first | 160-item P1 grid (40 cores × 4 ρ) + comprehension twins + both X2 probes |
| 2 | **SKIM** (v2 08) | Extends PROVENANCE's custody stack (ONE stack; PROVENANCE spec authoritative — write the stack extension, never a parallel harness); magnitude-blind prose rule enforced by generator design | 160-item P1 (5 families × 8 × 4-pt log ladder, windows overlapping ≥1 decade) + TR within-core + both X2 probes |
| 3 | **PALTER** (v2 09) | **BT gate EARLY**: the 20-composition belief-transfer pilot (human readers; pass = Spearman ≥0.6 per pack family) runs before item-scale investment; fail → STOP for Fable review | BT pilot report, then the 40-core × 4-tier bank |
| 4 | **TABLETS** (v3 01) | (i) **Casuistry-panel recruitment starts IMMEDIATELY** (§5 — it is the long pole; descriptive bands don't wait on it); (ii) the **TABLETS×CRUX co-registration memo (§6) must exist before the build session starts**; (iii) pre-pilot smallest-cell + profile-shape power analyses written into the file per TC-3 | 270-item base grid (+72 four-tier subset, +45 twins, +~135 framing ≈ 520 realized) |
| 5 | **SOVEREIGN** (v1 01) | **L2-P0 FIRST**: model-organism smoke test (planted objectives, ≥80% recovery, per-arc BF distributions published, decisive = BF≥10 fixed from organism calibration) before any real Layer-2 arc; L1 lattice builds after the P0 verdict (either way — L1 is not gated on P0 passing, only Layer-2 language is) | P0 gate report, then the 120-nominal L1 lattice |

Standing rules for all five sessions: EXECUTE not plan; A2 thresholds are pre-registered and post-pilot changes prohibited (TC-2); per-commandment/per-domain claims descriptive unless powered (TC-3); TC-4 language on all cross-model correlations; realized-count arithmetic stated in every pilot budget (TC-6); do-not-change lists in each brief are binding; gate failures STOP for Fable review. Scope isolation per bench rules.

## 5. TC-12 casuistry-panel recruitment kickoff (TABLETS + CASUIST share — start NOW)

Panel recruitment is the program's true critical path (~25–30 recruitments across 5 shared panels). The casuistry panel is first because wave-1 TABLETS needs it and CASUIST (second wave) shares it by binding TC-12 assignment (no design recruits its own panel where a shared one is listed).

- **Composition target:** 5–7 members spanning the three named gold corpora — rabbinic casuistry (pikuach nefesh precedence), Reformed/catechetical casuistry (WLC exception structure, necessity doctrine), and legal/common-law necessity doctrine; at least one member per corpus, no single tradition a majority (Case 12 guard).
- **Task spec (bounded load):** certify TABLETS' near-unanimous gold cells at κ≥0.8 (life-supersedes, property-yields-to-life, mercy-exception) and CASUIST's exception-map cells with per-cell provenance + N_eff/CI reporting; validate pair-taxonomy conflict faces (TABLETS A7). Panelists label item mappings against named corpus sources — never free-form moral opinions.
- **Sequencing:** recruit during ZEROSUM/SKIM/PALTER builds (sessions 1–3) so certification is ready when TABLETS builds (session 4). CG cells that fail κ≥0.8 shrink the gold set (never expand into contested territory) per TABLETS A2/CG.
- **Next panels queued behind it** (recruit as second wave approaches): legality/morality (PROVENANCE+SKIM — note SKIM's P1 needs only scenario-realism certification, lighter than gold certification), clinical/safety (KEEPER+UPSTREAM), consent/media (GOLEM+EFFIGY), counseling (PARAMOUR+TRIAD).

## 6. Co-registration memo owed BEFORE TABLETS builds: TABLETS×CRUX

TABLETS A8 names the CRUX (COOKBOOK 20-DESIGNS) co-registration as a build precondition and lists it in the do-not-change block. A short dated memo in this folder must, before TABLETS' build session: (a) state the construct boundary (CRUX = conflicts between *stakeholder/party* values with coherence auditing across parties; TABLETS = intra-code norm-vs-norm precedence over the ten commandments with casuistic gold); (b) declare the item-QC routing rule (any vignette whose conflict is between two *parties'* interests routes to CRUX; between two *norms'* duties on one actor routes to TABLETS); (c) pre-register what overlap analysis (if any) will be run and its TC-4 framing. Other owed co-registrations (LOOPHOLE×FRAMESHIFT, TURNCOAT×FRAMESHIFT, PRISM×VERNACULAR, TACIT×DISCORD) are second-wave-gated and remain queued.

## 7. Bookkeeping

- Spot-check protocol satisfied beyond the one-design-per-session minimum: all five first-wave designs read this session; subsequent sessions may still spot-read one revised non-wave design each against the memo (optional, not gating).
- Acceptance greps re-verified independently (Sonnet agent): 19/19 PASS, including 00b registry presence and all §A/§B/§C strings.
- This memo + the in-place fixes (§1 table) are the only changes made this session; no LOCKED spec was altered.
