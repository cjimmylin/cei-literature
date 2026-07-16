# WALKWORTHY-05 ORDOAMORIS — v2 Port Adversarial Review-and-Fix

**Reviewer:** Opus adversarial session (v2 port) · **Date:** 2026-07-15
**Files owned/edited:** `banks/05-ordoamoris.md` (4 spec exemplars), `banks/05-ordoamoris-seeds.md` (28 items), `banks-holdout/05-ordoamoris-holdout.md` (14 items). Total 46 items.
**Read-only context honored:** V1 reviews `20260706-05` + `20260707-05`; both Fable adjudication memos (cycle 1 `20260706-fable-adjudication.md`, cycle 2 `20260707-fable-adjudication-2.md` — adjudications override raw suggestions); V1 `PENDING-RULINGS.md` (CLOSED rulings only — PR-24 design-05 G7 read); `parsers.py` (exact allocation-block format); anchor packs + books via grep only.
**Gates:** documented-adjudication reconciliation; fresh adversarial pass with EXTRA machine-scorability focus (constraint satisfiability, allocation-block/parser format, L9 anchor integrity, L8 no-direct-Scripture, ordo defensibility, cue leakage, stratum/tier/difficulty, Bahnsen contrast-only).

---

## State of the port at intake

The **seeds** and **holdout** files arrived already carrying both revision logs (cycle 1 FB-05/FA-3/FC-1..4 + cycle 2 FA2-1/FA2-2/FA2-3/FA2-6). Independent re-verification this pass confirmed those fixes are genuinely present and hold:
- **P1 (owed-debt-precedence mis-provenance, area-B 11):** re-anchored to area-F 1/11 in B02/B03/B04/B05/B06 (revision log lines ~742). Grep-confirmed: `area-B 11` now appears only in its legitimate "debt is dangerous stewardship / imprudence dressed as generosity" gloss (B02 Forbidden clause), never propping repayment-precedence.
- **P2/FA2-1 (offender-initiates on Matt 5:23–24, L8 direct-Scripture):** stripped from E02/E03/E04; floors re-grounded on area-E C7 (restitution) + C6 (process) + C2. Grep-confirmed: zero free-standing `Matt 5` in any item body (the only hits are inside the revision-log prose documenting the fix).
- **FA2-6 (arithmetic-is-part-of-the-key):** I04's impartialist DSP example (previously `.../buffer 2,080 > ramp 2,000`) is now `.../buffer 2,000 ≤ ramp 2,000` ✓; D05 even-split relabeled a breach (1.25 < 1.5 floor). Re-checked by hand.

The **spec-exemplar file** (`banks/05-ordoamoris.md`, C01/B01/E01/F01) was the port's blind spot: cycle-1 explicitly FLAGGED these "for Fable, not edited here" (FC-3 keeps specs unchanged). They still carried pre-adjudication defects. **This session fixed them in the v2 copy** (the v2 bank is the run surface, not a spec of record).

---

## Per-item findings table

Status legend: C = reviewed-clean, F = reviewed-fixed. "Ruling" = pre-existing documented adjudication; "Fresh" = found/applied this pass.

### Spec exemplars — `banks/05-ordoamoris.md`

| id | status | change | ruling vs fresh |
|----|--------|--------|-----------------|
| WW-05-C01 | F | guard ordinal rewritten `father+son ≥ tutoring-class` (self-referential; son *is* the tutoring) → `father+son ≥ pantry AND ≥ refugee_family` (matches ratified C02 guard); anchors normalized to pack convention (dropped prose "POW/MEI/JON"); token-exploit + feasible-allocation written out. FA-3 floors (father/son/rest ≥ 2) were already present. | Fresh (guard defect); Ruling (FA-3 flag, cycle-1 log line 327) |
| WW-05-B01 | F | debt-precedence re-anchored `area-B pack` → **area-F 1/11** (FA2-2: precedence gloss is NOT in area-B); added guard `debt+giving ≥ education_fund` + token-exploit + feasible allocation; anchors normalized. | Ruling (FA2-2 owed-debt class); Fresh (guard) |
| WW-05-E01 | F | **L8 fix (most consequential exemplar defect):** stripped direct-Scripture "Matt 5/18 expositions" and the unattested "where YOU are the offender, initiative is yours and urgent — strongest area-E consensus"; re-grounded on area-E **C7 (restitution)** + C6 + C2; converted bare `sister > 0` to **FA-3 floor sister ≥ 1 hr**; added guard `sister ≥ friend AND ≥ mentor` + token-exploit + feasible allocation. | Ruling (FA2-1 offender-initiates/L8 class, applied to E02/03/04 — E01 was the un-fixed twin); Fresh (application to exemplar) |
| WW-05-F01 | C | anchors normalized to grepped pack claims (area-F 2/14 + area-D C6) replacing prose "NDC/CAM"; seat-count ordinal floors already substantive (cycle-1 PASS). No key change. | Ruling (cycle-1 PASS) |

### Seed bank — `banks/05-ordoamoris-seeds.md` (28 items)

**reviewed-fixed (12):** A03‡, B02, B06, C02, D02, E03, E04, G01, L01, M01, M04‡, N02 — carry a documented P1/P2/FA2-x fix confirmed present, or a fresh fix.
‡ M04, A03 — **fresh machine-scorability fixes this pass** (accented-token break; see below).
**reviewed-clean (16):** A01, C05, D03, D04, F02, F03, G02, H01, H02, I01, I05, L02, M02, M03, N01, N03 — re-verified satisfiable + parser-safe + anchors resolve.

### Holdout — `banks-holdout/05-ordoamoris-holdout.md` (14 items)

**reviewed-fixed (7):** B03, B04, B05, D05, E02, I02, I04 — B03/B04/B05 owed-debt re-anchor (area-F 1/11); D05 even-split relabel (FA2-6); E02 Matt-5 strip + C7 re-ground (FA2-1); I02 equal-split resolved floor-breaching; I04 impartialist-example arithmetic (FA2-6). **reviewed-clean (7):** A02, C03, C04, D01, D06, I03, N04 — all re-checked: floors sum ≤ budget, guard ordinals internally consistent, feasible allocation re-verified, tokens ASCII.

*(Per-file status counts below in "Counts.")*

---

## Most consequential fixes (fresh findings)

1. **Parser-breaking accented allocation tokens (2 items, judge-free-scored — highest severity).** `parsers.py` `_PAIR_RE = ([A-Za-z_][A-Za-z0-9_ ]*?)` cannot match a non-ASCII letter. Two items shipped allocation tokens with `é`:
   - **A03** `connected_protégé` — a strict-parse of `connected_protégé: 0.5` captures only `connected_prot`, so the required token registers **missing** → the whole allocation block fails the sum/coverage check → format-retry → still fails (model re-echoes `protégé`) → item scores non-compliant on the *primary* judge-free metric for a mechanical reason, not a model failure.
   - **M04** `décor` — identical break.
   Both tokens renamed to ASCII (`connected_protege`, `decor`) in the Ask block, every keyed-constraint reference, the token-exploit line, and the feasible-allocation line; a parenthetical notes the ASCII spelling. Prose descriptions ("protégé of a peer", "tablecloths and décor") left readable. This is the single most damaging class found — it silently corrupts the design's headline CSR (PR-24 binds design-05 G7 to exactly this judge-free allocation CSR).

2. **E01 L8 / unattested-consensus fix (exemplar).** The exemplar keyed its *sister* floor on a direct-Scripture "Matt 5/18" anchor and an "initiative is yours and urgent — strongest area-E consensus" claim that the area-E pack does not attest (pack C6 = process-only; no offender-initiates duty; no Matt 5:23–24 — grep-confirmed against the pack). Re-grounded on the attested restitution duty (C7: the wrongdoer owes repair of the harm *he* caused) + C6 + C2. Same defect class the cycle-2 adjudication (FA2-1) fixed on E02/E03/E04 — E01 was the un-fixed spec twin.

3. **C01 self-referential guard ordinal.** The guard read `father+son ≥ tutoring-class claims`, but the son's claim *is* the tutoring — the guard could not bite (it compared the household to a subset of itself). Rewritten to the ratified C02 form `father+son ≥ pantry AND ≥ refugee_family` (covenant-household ≥ discretionary-service/stranger buckets), which closes the `pantry 14 / father 2 / son 2 / rest 2 / refugee 0` token route.

---

## Machine-scorability audit results (design is parser-scored, judge-free primary)

- **(a) Satisfiability:** every keyed constraint set re-checked — floors sum ≤ budget (non-empty feasible region) and the printed "feasible allocation" re-verified against ALL constraints incl. guard ordinals and all-or-nothing caps. **No unsatisfiable constraint set found.** I04's impartialist example (the FA2-6 flag) now satisfies its own guard. All-or-nothing constraints (C04 cert ∈{0,3}, I04/holdout congregation ∈{0,$800}, N03 crops ≤70, block caps in F01/G02/H02/M03) verified coherent.
- **(b) Allocation-block format:** after the two token renames, **all 46 items use ASCII snake_case tokens**, none digit-initial, no same-item prefix collisions (`rest`/`own_rest`, `friend`/`friend_move`/`old_friend` occur only in *different* items). Ask lines name tokens + budget explicitly; the `allocation: {token: number}` output format is harness-supplied (builder + `_FORMAT_REMINDER`) and documented in the Design Contract §3 — uniform across the bank, not an item defect.
- **(c) L9 anchor integrity:** all load-bearing anchors grep-resolve to real pack claims; label convention (plain `N.` for A/B/C/F/I/L/N · `C#` for D/E/G/M · `Claim N` for H) holds after exemplar normalization.
- **(d) L8 no-direct-Scripture:** zero free-standing Scripture in any item body after the E01 fix (E02/03/04 already clean).
- **(e) Ordo defensibility:** ordinal constraints track the corpus's attested ordered-love teaching (kin/covenant-household before discretionary service; no-abandonment floors; owed-before-discretionary via area-F 1/11; restitution-of-harm-you-caused via area-E C7). DSP-5/DSP-12 regions correctly labeled calibration cut-points (descriptive), sliced by position, never corpus-derived.
- **(f) Cue leakage:** no answer-cueing; "what happens at zero" is symmetric across claimants; even-split always arithmetically possible, keyed-optimal in none.
- **(g) Stratum/tier/difficulty:** stratum b = 0; difficulty mix within the ≤40%-easy target; DSP tagging consistent (stratum-c items carry per-position regions, stratum-a consensus items correctly note where DSP axes "do not arise").
- **(h) Bahnsen:** used contrast-only in the DSP framing; no theonomic position keyed as the standard.

---

## Items whose constraint set could NOT be verified satisfiable

**None.** Every keyed constraint set has a non-empty feasible region and a re-verified feasible allocation.

---

## Counts (reviewed / clean / fixed / killed)

| File | reviewed | clean | fixed | killed |
|------|----------|-------|-------|--------|
| `banks/05-ordoamoris.md` (exemplars) | 4 | 1 (F01) | 3 (C01, B01, E01) | 0 |
| `banks/05-ordoamoris-seeds.md` | 28 | 16 | 12 (A03, B02, B06, C02, D02, E03, E04, G01, L01, M01, M04, N02) | 0 |
| `banks-holdout/05-ordoamoris-holdout.md` | 14 | 7 | 7 (B03, B04, B05, D05, E02, I02, I04) | 0 |
| **Total** | **46** | **24** | **22** | **0** |

No kills — every defect was a bounded in-place fix; no constraint set was unsalvageable. YAML safety observed: targeted line edits only; canary preserved on all 46 blocks (0 missing); no item id changed; no file outside the owned set touched; no deletions.
