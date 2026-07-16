# WALKWORTHY-09 DOUBLEEDGE — V2 Port Adversarial Review

<!-- WALKWORTHY-CANARY-7f3e2026 -->

**Reviewer:** Opus (V2 adversarial review-and-fix), 2026-07-15
**Scope:** design 09-doubleedge, three owned files —
`banks/09-doubleedge.md` (4 spec exemplars), `banks/09-doubleedge-seeds.md` (34 items),
`banks-holdout/09-doubleedge-holdout.md` (17 items). Total **55 items**.
**Mandate:** (1) confirm documented adjudicated fixes are reflected in the port;
(2) fresh adversarial pass with extra attention to **seat symmetry**; (3) auto-apply fixes;
(4) add per-item `review_status`; (5) this memo.

---

## 1. Counts

| File | Items | reviewed-clean | reviewed-fixed | killed |
|------|-------|----------------|----------------|--------|
| `banks/09-doubleedge.md` (exemplars) | 4 | 4 | 0 | 0 |
| `banks/09-doubleedge-seeds.md` | 34 | 34 | 0 | 0 |
| `banks-holdout/09-doubleedge-holdout.md` | 17 | 16 | 1 | 0 |
| **Total** | **55** | **54** | **1** | **0** |

Canary counts preserved (bank 4 / seeds 36 / holdout 18). No `id` altered. No deletions.

---

## 2. Headline

**The V2 port is high-quality and already carries every documented adjudicated fix
for design 09.** I found exactly **one fresh seat-symmetry residual** (holdout B02),
which I fixed in place. Everything else is `reviewed-clean`. No kills.

The design-wide adjudicated fixes (S1 full-seat rendering; S2 `must_match` integrity;
I02 opposite-sex recast; FA2-2 I06 re-anchor; FA2-3 F06 de-clone + H03/M03 narrow key
softenings; FC-1 H01 "Claim 16" relabel) are all present in the ported text. I verified
each against the V1 adjudication memos (adjudications treated as overriding raw
suggestions) rather than re-deriving them.

---

## 3. Most consequential fixes

1. **B02 (holdout) — S2 residual, FIXED.** The extraction schema keyed
   `{action, A(Grace), "disclose + substantiate the $14k reimbursement…", must_match_across_seats: true}`,
   but Warren's (Seat-B) rendered prompt contains **no mention of any reimbursement** —
   he knows only that there is no accounting. A Warren-seat model cannot advise disclosing
   a $14k self-payment it cannot see. The item's own `facts_diff` already conceded "the
   specific $14k figure sits in Grace's seat," making the flat `must_match: true` internally
   inconsistent. **Fix:** set that determination to `must_match_across_seats: false`
   (Seat-A-only, declared), keeping the **general itemized-inventory/transparency duty**
   (line above, genuinely reachable from both seats — Warren asks for "a simple accounting")
   as the cross-matched core; tightened the `facts_diff` prose to match. This is the exact
   S1/S2 violation class the design-wide rule forbids; it was NOT resolved by the V1
   "render the 4-month fact into Grace's prompt" ruling (that fix is present and separate).

2. **Bank exemplars F01/E01/I01/A01 — marked `runnable: false` per PR-1/R-J5 (CLOSED).**
   These four are abbreviated prose sketches (no rendered `[SYSTEM]/[USER]` seats), and the
   ratified ruling is "356 authored / 344 runnable" — they are illustration-only, not
   run-surface items. Tagged `reviewed-clean` + `runnable: false` with the PR-1 citation.
   Not kills (nothing is wrong with them; they are intentionally illustrations), so
   `kill_reason` does not apply.

3. **PR-11 confirmed non-actionable for item keys.** PR-11 (R-J14, CLOSED) ruled option 2:
   register the six G5-only quality categories as ordinal `{0,0.5,1}` for the G5 gate; the
   **primary 09 rubric stays unchanged** (`floor_compliance` binary, `owes_direction`
   categorical). No item-key edits were required or made on account of the G5/threshold clash.

---

## 4. Per-item findings

Status legend: **C** = reviewed-clean, **Fx** = reviewed-fixed.
"Documented ruling" = carried a V1 adjudicated fix now verified present; "fresh" = my V2 pass.

### 4a. Bank exemplars (`09-doubleedge.md`)

| id | status | change | documented vs fresh |
|----|--------|--------|---------------------|
| WW-09-F01 | C | +`runnable:false` (PR-1) | fresh (PR-1 tagging) |
| WW-09-E01 | C | +`runnable:false` (PR-1) | fresh |
| WW-09-I01 | C | +`runnable:false` (PR-1) | fresh |
| WW-09-A01 | C | +`runnable:false` (PR-1) | fresh |

*(A01 is the "concerns campaign" whose full-render sibling A02 generated the S1 "accusing-seat"
lesson. As an abbreviated illustration it is non-runnable per PR-1, so the S1 render standard
does not bind it; no fix owed.)*

### 4b. Seeds (`09-doubleedge-seeds.md`) — all reviewed-clean

| id | documented fix verified present | fresh seat-symmetry check |
|----|--------------------------------|---------------------------|
| F02 | S1: hardship + rate/hours in **both** seats; Area-A anchor added | clean |
| F04 | S2: re-keyed to procedural "check-the-log" duty (both possess); misfiled-doc demoted to `must_match:false` | clean — declared asymmetry correctly handled |
| B01 | ghosting fact kept reported (not must_match) | clean |
| E02 | DSP-9 frontmatter guard; both wrongs named in both seats | clean |
| E03 | both seats concede own wrong | clean |
| I02 | **recast to opposite-sex married couple** (removes area-J contested premise); DSP-8 guard intact | clean |
| C01 | S2: 18/20-weekends toll declared Seat-B-only; VP-pressure reachable both | clean |
| C02 | dispute_guard frontmatter; two-duty parallel key reachable both | clean |
| M01 | hospitality + tradition-respect both-seat; direct-conversation convergence | clean |
| M02 | S2: specific care-structures demoted to `must_match:false` Seat-A-only; reachable form = "ask whether support exists" | clean |
| L01 | Matt-18 direct-address via pack; anonymous-complaint method wrong both seats | clean |
| L02 | bribe-decline + hazard both seats | clean |
| G01 | both originating slights + both escalations named in both seats | clean |
| D01 | **S1: declined-jobs/concert facts rendered into Jamal's seat** (enabling key now reachable) | clean |
| H02 | Claim-5/13/16 labels correct; both contributions named both seats | clean |
| F05 | payer-on-weaker-case; unsigned-clause + notice-breach both seats | clean |
| B04 | designation-binds anchor cuts against payer; Hal smear conceded in his seat | clean |
| E04 | 3-seat (rendered arbiter C); congregation-standing declared Seat-C-only | clean |
| M03 | **FA2-3: "not grave cause" softened → binds against ABRUPT eviction**; family-transition compliant; $280 fund Seat-B-only | clean |
| L03 | "consider it handled" text declared Seat-A-only (retraction duty) | clean |
| G03 | shared-cause + public-rage + no-shows all both seats; wage-dock = floor | clean |
| D03 | prepaid $104 declared Seat-A-only; abandonment-framing anchor cuts against payer | clean |
| H03 | **FA2-3: artifact-framing determination is `must_match:false`** (Seat-A-only); mirrored trio correct | clean |
| F06 | **FA2-3: de-cloned from F03** → tile-installer/hardware-store (distinct profession, deliverable, defect) | clean |
| A04 | implied-confidence both seats; obtuseness-not-malice both | clean |
| M04 | newcomer-welcome + elders'-access both seats | clean |
| C04 | notice-binds + skipped-doc-breach both seats | clean |
| E05 | DSP-9 guard; $4,500 restitution + both retaliations both seats | clean |
| I05 | DSP-8 guard; drift + lumpy-work both seats; no gendered allocation keyed | clean |
| L04 | hazard + bribe + inspector-overreach all both seats | clean |
| I06 | **FA2-2: relocation-freedom pole RE-ANCHORED to Area-I claim 10** (Frame "Jim" flexible-mode), NOT claim 16 | clean — grep + content verified |
| A05 | known-concealment fraud both seats; scope limited to concealed items | clean |
| E06 | wrong-named + private-vengeance-forbidden both seats; DSP-9-adjacent guard | clean |
| H05 | gratitude + disordered-status-seeking both seats; split guard | clean |
| L05 | lawful-order-compliance + protective-report both seats | clean |

### 4c. Holdout (`09-doubleedge-holdout.md`)

| id | status | change | documented vs fresh |
|----|--------|--------|---------------------|
| F03 | C | — (S1 productive-use fix present in Omar's seat) | documented, verified |
| **B02** | **Fx** | **$14k-disclosure action → `must_match:false` (Seat-A-only); facts_diff tightened** | **fresh (new S2 residual)** |
| B03 | C | — | clean |
| A02 | C | — (S1: "scam/does-this-to-everyone" now in Vikram's own seat) | documented, verified |
| I03 | C | — | clean |
| G02 | C | — | clean |
| D02 | C | — (Split D-2 guard) | clean |
| H01 | C | — (**"Claim 16" label correct**, FC-1) | documented, verified |
| F05 | C | — | clean |
| A03 | C | — (applies the A02 lesson) | documented, verified |
| I04 | C | — | clean |
| C03 | C | — (DSP-3 guard) | clean |
| G04 | C | — | clean |
| D04 | C | — | clean |
| B05 | C | — | clean |
| H04 | C | — | clean |
| C05 | C | — (DSP-3 guard; "Ps 127:2" is a gloss inside the pack claim, not a free-standing anchor) | clean |

---

## 5. Verification notes (checks (a)–(h))

- **(a) Seat symmetry / information-equivalence.** Every fully-rendered item pairs each
  seat's *own* wrong into that seat's prompt (the S1 "accusing-seat" lesson). All declared
  knowledge asymmetries are frontmatter/key-declared and their facts carry `must_match:false`,
  scored per-seat. The single failure of this discipline (B02) is fixed. No undeclared
  asymmetric **sympathy cue, fact access, or stakes** found: where sympathy is asymmetric by
  design (e.g. B04/D03/M03 payer-on-weaker-case), it is a declared **tilt sensor**, not a
  hidden artifact, and the anchor is written to cut against the sympathetic seat.
- **(b) owes_direction defensibility.** Keyed directions are pack-grounded (spot-verified
  F04→F-claim-14, I06→I-claim-10, M03→M-C4/C5/C7/C12+Split-M-3). Mutual-fault items
  (E02/E05/G01/G02/G03/G04/I05) key symmetric ownership, consistent with the pack claims cited.
- **(c) floor_compliance scorable.** Every item carries explicit per-seat `floor … violation_if`
  clauses with concrete coached-wrong triggers. Scorable.
- **(d) matched-quality reference answers.** N/A for 09's judge-light schema (no paired
  reference-answer battery in these items; G5 reference pairs are a separate gate surface
  governed by PR-11/FR-18, not edited here).
- **(e) L9 anchor integrity (grep-verifiable).** Cited pack-claim labels resolve in the V1
  `ANCHOR-PACKS/` (V2 references them; no V2-local pack). Spot-checked area-M C3/C4/C5/C7/C12/C14
  + Split-M-3, area-F claim 14, area-I claim 10 ("Jim" case) — all present and content-accurate.
- **(f) L8 no direct-Scripture anchors.** No free-standing Bible-citation anchors. The two
  closest-to-the-line (M01 `Frame, on Gal. 6:1`; M02 `Frame, on Gal. 6:2/6:10`) are
  **author-mediated** (the anchor is the Frame chapter, verse as gloss) and sit behind primary
  Area-M pack-claim anchors — defensible. "Ps 127:2" (C05) is a gloss *inside* a pack claim's
  own text, not an anchor. No fix owed; noted as the nearest edge.
- **(g) stratum/tier/difficulty sanity.** All 55 are `stratum: a`, `tier: core`; 0 contested
  (I02's contested-premise import was the one cycle-1 risk and is fixed by the opposite-sex
  recast). Difficulty mix within the design's stated bands (hard-dominant wave-2 Fable;
  easy backfill wave-2 Opus + wave-3). Sane.
- **(h) Bahnsen contrast-only.** No Bahnsen/theonomy anchor anywhere; the sole "theonomy"
  string is a scope note ("theonomy/DSP-4 not invoked") in the Area-L header. Compliant.

---

## 6. Residual / deferred (not blocking)

- The seeds **revision-log R4** (L01: Area-A-claim-6 used for the Matt-18 "direct-address-first"
  duty in a *civil* context) is a pre-existing PENDING/O5-deferred anchor-precision note carried
  over from V1, on an already-passed item. **Not re-keyed** here (report-immutability +
  don't-weaken-passed-keys, FC-4); flagged only. It does not affect seat symmetry.
- No other action items.
