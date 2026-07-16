# RULINGS-APPLIED — Phase-B review-pass ledger (2026-07-15)

> **OWNER RATIFICATION (2026-07-15):** Jimmy reviewed the consolidated diff and this
> ledger and ratified all 105 auto-applied fixes ("I have reviewed and authorized").
> Same ruling authorized the ~$2 comparability slice (MVP-A1 60 items, both harnesses,
> same SUT/judge) and the 2-judge re-score validation — the two preconditions in
> `20260715-inspect-fit-assessment.md` §4.

Ledger of what the 10 parallel review-and-fix agents (opus, one per design) applied to
the v2 bank copies. Full per-item detail: `REVIEWS/20260715-NN-*-v2review.md` (10 memos).
Full before/after: `REVIEWS/20260715-consolidated-diff.md`. v1 sources untouched.

Convention: every item now carries `review_status: reviewed-clean | reviewed-fixed | killed`
in its YAML block. Zero items were killed; zero item ids changed; canary preserved everywhere.

| Design | Items | Fixed | Killed | Consequential changes |
|---|---|---|---|---|
| 01 GOODSAMARITAN | 71 | 2 | 0 | Applied the one ratified-but-never-written cycle-2 fix (A05/A05-P moral-vocabulary cue removal); full L9 grep re-verification clean |
| 02 TWOMASTERS | 58 | 1 | 0 | N04 T4 harm-pathway reveal de-telegraphed (S2 mandate); all cycle-1/2 adjudicated fixes confirmed present |
| 03 QUIETTONGUE | 48 | 1 | 0 | L03 shading tier rebuilt (was collapsed into violating — say-do headline category was unscoreable as written) |
| 04 INNERWEIGHT | 48 | 1 | 0 | A04 minimal-pair confound removed (β administration leaked differential audience exposure) |
| 05 ORDOAMORIS | 46 | 22 | 0 | **Parser-breaking accented allocation tokens fixed (A03/M04 `é` → ASCII)** — would have mechanically zeroed CSR; E01 exemplar L8 + unattested-consensus fix; C01 self-referential guard rewritten; B01 re-anchored; all constraint sets verified satisfiable |
| 06 CROOKEDPATH | 40 | 1 | 0 | F03 anchor re-attribution (FA2-2 locality); G5 matched-reference quality-parity confirmed sound; M02 flag NOT applied (cycle-2 adjudication overrides). Note: spec-exemplar file not stamped with review_status (seeds+holdout only) |
| 07 SEVENTYSEVEN | 44 | 44 | 0 | Per-item comfort_only↔faithful_counsel discriminators added to ALL items + explicit "flat refusal = cold_correction" keys — direct remedy for v1's 17.6% judge-agreement floor; 4 spec-exemplar anchors normalized |
| 08 VOCATIONFORK | 48 | 12 | 0 | Bank arrived fully hardened; review_status audit trail added; 44/44 covert↔overt one-sentence-delta twins verified |
| 09 DOUBLEEDGE | 55 | 1 | 0 | B02 (holdout) unreachable must_match key fixed (fresh S2 residual); 4 sketch exemplars explicitly tagged runnable:false per PR-1/R-J5 |
| 10 STRANGERGATE | 52 | 20 | 0 | All fixes were already present in port; "fixed" = documented-fix items stamped; minimal-pair discipline verified (no U-cue confounds) |

**Totals: 510 items reviewed · 105 stamped fixed · 0 killed.**

## Cross-cutting verifications (all 10 memos)
- L8 (no direct-Scripture anchors): clean everywhere; `Frame, on Gal. 6:x` forms ruled
  book-mediated per cycle-2 FA2-1 precedent.
- L9 (anchors grep-verifiable in the 15 book .txt files): clean; several false "misses"
  were OCR/curly-quote artifacts, run down individually.
- Bahnsen contrast-only: no consensus claim anchored to Theonomy anywhere.
- Adjudication precedence honored: reviewer suggestions overridden by v1 fable
  adjudications were NOT applied (e.g. design 06 M02).

## Known count implication
Design 09's 4 spec exemplars now carry explicit `runnable: false`. v1's builders already
treated sketch exemplars (designs 02/07/09) as non-runnable, so the expected public
runnable surface remains **344**; the Phase-C post-review conversion must confirm this
(and explain any delta in the new dated parity report).

## Open items carried to Phase C
1. `metadata.keyed` field-name reconciliation between converter output and
   `walkworthy_inspect/rubrics.py::keyed_fields` (A2 flag #2).
2. Design-05 CSR consensus-floor comparator port (A2 flag #3 — currently approximated;
   TODO in scorers.py).
3. Design 06 spec-exemplar review_status stamps (cosmetic).
4. Design 07 harness-side matched-quality judge reference answers (reviewer 07 residual).
