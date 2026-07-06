# 2026-07-06 — Opus Work Order: Gate Corrections & Pickup Protocol (SermonMountBench v1 + v2)

**Authority:** every change ordered here was adjudicated by the Fable adversarial gate of 2026-07-05 (`20260705-fable-adversarial-gate-v1-v2.md`). LOCKED items normally need Fable review — **this work order IS that review**; cite it in each edit ("per gate memo 2026-07-05"). Do not re-adjudicate; do not go beyond what is ordered.
**Who executes:** the next Opus session, BEFORE any item-bank building.
**Order of operations:** §2 (v1 file amendments, ~30 min of edits) → §3 (program directives, standing) → §4 (verification) → then start building per §5.

---

## 1. Already APPLIED — do not re-apply

All v2 gate revisions were edited into the v2 files on 2026-07-05 and are marked inline with "gate", "gate addition", "gate-revised", or "gate rule". For the record, the applied set:

| File | Applied gate changes |
|---|---|
| `DESIGNS/01-pilgrim.md` | SHUFFLE→SYNTH condition (+falsification (b) rewrite, metrics, harness); canonical-spine branch rule |
| `DESIGNS/02-crosswinds.md` | severity-matching audit; shallow-feature threshold as balanced accuracy |
| `DESIGNS/03-plumbline.md` | MIRROR = enacted-only conduct (LOGSPECK boundary); cross-S-ID subtlety equating table |
| `DESIGNS/04-canticle.md` | pseudo-respondent population (≥30 systems × ~10 neutral configs), multilevel Bayesian GRM; two-stage deliverables; dimensionality demoted to "evidence"; M4 data source |
| `DESIGNS/05-tessera.md` | ROCKSAND boundary paragraph in §8; T-STAKES declared boundary-case; neutral-parallel battery |
| `DESIGNS/06-ledger.md` | cumulative-capture scoped to I-APPROVAL/I-STATUS/I-CONTINUITY; ≥3 replicate skins per rung |
| `DESIGNS/07-village.md` | reproducibility gate = split-half ≥0.6 + k≥8 seed agreement; build conditional on ≥2 prior P1 passes; tagger recall audit ≥0.8 |
| `DESIGNS/08-scribe.md` | revered-secular-text control arm; metric renamed "pericope-literalism vs purpose-application divergence"; public-domain translation |
| `DESIGNS/09-witness.md` | END-item particulars ban; session-hygiene simplification |
| `DESIGNS/10-gleaning.md` | P-SOLO(k) + P-HALF dilution controls; partition uses both margins |
| `01-PORTFOLIO-overview.md` | capability-PC guard = scale-up analysis (≥15 systems), never a P1 gate; gate status line |
| `00-REGISTRY-sermon-principles.md` | pole-order clarification (rule 2). Registry otherwise untouched and FROZEN |

If you find a v2 brief contradicting this table, the brief text marked "gate" wins; flag the contradiction to Fable in your handoff.

## 2. v1 amendments to APPLY NOW (file-by-file, exact edits)

These implement gate recommendations R-1…R-7. They were not applied on 2026-07-05 only because that thread was folder-restricted to SERMONMOUNT-v2. Each edit: make the change, and append the marker `(gate memo 2026-07-05, R-n)` to the edited passage.

### 2.1 `../SERMONMOUNT/DESIGNS/00-sermonmountbench-portfolio.md` — R-2 (one edit covers all cards)
In §4 (Shared design commitments), item 7 (Falsification conditions), append:
> Gate clarification (2026-07-05): the ">40% capability-PC correlation" falsification is a scale-up analysis requiring ≥15 systems; it is never evaluable on a 6-model P1 and is not a P1 gate. P1s rely on their cards' qualitative discrimination checks. (gate memo 2026-07-05, R-2)

### 2.2 `../SERMONMOUNT/DESIGNS/10-rocksand.md` — R-1
Two edits:
1. In §5.6 (Hearer-tier items), append:
> Import rule (gate): if v2-09 WITNESS has passed P1 by build time, R3's baseline reuses WITNESS scenario cores and gap data for the overlapping domains instead of re-measuring with a coarser 2-modality probe; ROCKSAND then reports R3 as a WITNESS-anchored subset. The self-contained hearer tier below is the fallback when WITNESS is unbuilt. (gate memo 2026-07-05, R-1)
2. In §5.5 (Reduced vs full form), add WITNESS to the import sentence: the full form may import calibrated items from designs 01–09 **and v2-09 WITNESS cores** under the same import rule (source design's P1 gates passed; source design's scoring).

### 2.3 `../SERMONMOUNT/DESIGNS/06-logspeck.md` — R-3
In §5.2 item 2 ("For (ii) operator: name the model's actual developer…"), append:
> Reporting-mode decision (gate): results in the operator condition name real vendors judging their own makers — publication-sensitive. Before ANY public run or external report, fix a reporting mode (named vs anonymized vendor labels) and record it in the P1 report; default to anonymized until Fable or the user decides otherwise. (gate memo 2026-07-05, R-3)
Also add one checklist line in §10: `- Reporting-mode (named/anonymized operator results) decided and recorded before public runs (R-3).`

### 2.4 `../SERMONMOUNT/DESIGNS/03-plainyes.md` — R-4
In §5.5 (Human anchoring subsample), replace the plain 25% sampling with stratified sampling:
> The 25% human-listener subsample is stratified, not random: it must over-sample the items whose *model*-listener panels showed the largest induced-belief errors (top quartile), plus a random remainder. Rationale (gate): model listeners may share training-induced blind spots with tested models; the human gate is most informative exactly where model listeners report the strongest effects. (gate memo 2026-07-05, R-4)

### 2.5 `../SERMONMOUNT/DESIGNS/05-twomasters.md` — R-6
In §5.2 item 4 (matched-EV construction), harden the manipulation check:
> The perceived-stakes probe check is a HARD gate (gate): fear-arm and greed-arm perceived magnitudes must be statistically indistinguishable (probe-model ratings, pre-registered equivalence bound) before any fear/greed asymmetry is computed; arms failing the bound are re-scripted, and M3 is not reported for unmatched arms. (gate memo 2026-07-05, R-6)
Also add to §9 go/no-go: `perceived-stakes equivalence gate passes`.

### 2.6 `../SERMONMOUNT/DESIGNS/07-goldgap.md` — R-7
In §9 (P1 pilot spec), strengthen the go/no-go line about the simulator:
> Simulator–human κw ≥ 0.6 is pass/fail with no partial credit (gate): a pass on some scenarios with failures elsewhere is a FAIL for scale-up — revise the simulator recipe and re-run P1. GOLDGAP does not expand past P1 on any partial pass. (gate memo 2026-07-05, R-7)

### 2.7 `../SERMONMOUNT/DESIGNS/01-blessed.md` — R-5
Add one line to §10 first-step: `- Verify the §8 BBQ capability-correlation figure (76.8%) verbatim against KB doc 01 before citing; correct §8 if the KB reads differently — never recompute (R-5).`

### 2.8 `../SERMONMOUNT/DESIGNS/20260705-sermonmount-designs-handoff.md`
Append to §4 (Known issues / open decisions):
> 2026-07-05 adversarial gate (v1+v2) complete: memo at `../../SERMONMOUNT-v2/20260705-fable-adversarial-gate-v1-v2.md`; v1 amendments R-1…R-7 applied per the work order `../../SERMONMOUNT-v2/20260706-opus-gate-corrections-workorder.md` (§2). Cross-version build slate and shared-asset rules in that memo §5 supersede nothing here but add: PLAINYES starts panel recruitment for BOTH portfolios.

**Restriction:** touch nothing in v1 beyond these eight edits. v1 LOCKED sections remain LOCKED; these edits are the gate's entire v1 delta.

## 3. Standing program directives (no file edits; obey during builds)

1. **Build slate (cross-version):** if interleaving v1+v2, follow v1-03 PLAINYES → v2-09 WITNESS → v1-06 LOGSPECK → v2-02 CROSSWINDS → v1-01 BLESSED. If building v2 only, use the v2 order (09→02→05→08→03→06→04→10→01→07). VILLAGE never starts before two other v2 designs pass P1 (now in its brief).
2. **One theologian/secular panel serves both versions.** Batch elicitation kits (v1 contested bands + v2 CROSSWINDS per-tradition orderings + registry ⚖ adjudications) into a single recruitment wave, launched during the first build session (PLAINYES or WITNESS).
3. **One judge-calibration stack.** Never calibrate judges independently for the same rubric family across v1 and v2; store calibration assets under `SERMONMOUNT-v2/SHARED/judges/` and reference from both.
4. **Capstone matrix gains an eleventh column:** where a v1 design instruments an S-ID, its score joins the v2 40×10 matrix as a v1-method column (see guide §7; score-file convention identical).
5. **P1 sizing:** v2 P1s should run ≥ 4 models across ≥ 2 families when budget allows (FREE parameter; v2 briefs' "3 models" is the floor, not the target).
6. **Scope grep** (before every commit): `grep -riE 'corinth[l]ove|tencommand[m]ents|fruit[b]ench' .` from each SERMONMOUNT folder — expect zero hits (patterns are self-excluding).

## 4. Verification after applying §2 (run, then record in your session handoff)

1. `grep -c 'gate memo 2026-07-05' ../SERMONMOUNT/DESIGNS/*.md` — expect exactly 7 marked edits across 7 card files (+ the handoff appendix and portfolio edit; portfolio marker included in its text).
2. Confirm no v1 file changed EXCEPT the eight listed in §2 (`git diff --stat` on `SERMONMOUNT/`).
3. Re-run the v2 coverage grep (all briefs contain S01–S40 literally) and the scope grep (§3.6) — both must be clean.
4. Commit only if the user asks; if committing, v1 amendments and any new build files go in ONE atomic commit citing the gate memo (parallel sessions share the git index — check `git log -1` first).

## 5. Pickup protocol for every future session (supersedes nothing; adds to guide §1)

Load, in order: KB doc 01 → v2 registry → v2 portfolio §2/§7 → **the gate memo** → **this work order** → the design brief being built → its flagged KB docs → the guide. If §2 above is not yet applied (check for the `gate memo 2026-07-05` markers in v1), apply it FIRST — building on ungated v1 cards is the failure mode this file exists to prevent. Then: post-2026-07 literature overlap re-check for the brief in hand, then build per its §7 work order. EXECUTE, don't plan: every session ends with files (banks, code, audits, dated reports), never proposals.
