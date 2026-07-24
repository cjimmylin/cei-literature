# Item Quality and Validity Evidence — WALKWORTHY v2

**DRAFT v1 — 2026-07-24**

Canary: WALKWORTHY-CANARY-7f3e2026

*Drafted from the 2026-07-18 item-assessment record + 2026-07-24 rulings + smoke report; numbers verified against sources.*

---

## X.1 Overview

The validity-evidence portfolio for the WALKWORTHY v2 item banks combines five
lines of evidence, each addressing a distinct threat to the claim that the banks
measure what they are intended to measure. First, **keying and content validity**
were established through a full two-rater item sweep paired with a refute-first
adversarial review of every substantive challenge to a keyed answer. Second, the
**reliability of the review instrument itself** (IVR-1.1) was estimated so that the
sweep's verdicts could be read against a known agreement floor. Third, **construct
validity** was probed through the generic-recoverability × difficulty gradient — the
prediction that items whose keyed behavior a generic assistant can recover should be
easier than items that require the corpus. Fourth, an **end-to-end post-fix
instrument verification** (a changed-items smoke rescore) confirmed that every
repaired scoring path executes live. Fifth, the **fix disposition itself was
governed**: an owner-ruled proposed-edits ledger dispositioned every finding, and a
comparability fence (C9) was drawn around the cells whose semantics changed. The
sections below report each line in turn.

Two framing caveats apply throughout. All agreement figures are LLM-vs-LLM
agreement and are read as an **upper bound** on the human-rater agreement the same
instrument would achieve, since two model raters share systematic priors that human
raters do not. <!-- src: 20260718-04-irr-report.md §1 --> And a number-hygiene
convention is used consistently: **355 public** denotes the items rated in the
2026-07-18 sweep, while **344 public** denotes the runnable public bank after eleven
non-runnable exemplars were retired (PE-3); the two are never interchangeable and
every count below is time-tagged to the sweep or to the post-fix bank as
appropriate. <!-- src: RULINGS-APPLIED-20260724.md PE-3 -->

## X.2 Item-review design

Every item was subjected to a full double-rating pass. At assessment time the banks
comprised **513 items — 355 public and 158 holdout** — and double-rating completeness
was **100% on both surfaces (355/355 public, 158/158 holdout)**. <!-- src:
20260718-04-irr-report.md §1 --> Two fresh-context LLM raters (Opus tier) scored each
item independently under an anti-leakage-by-construction protocol, so that neither
rater could see the other's verdict or the original author's rationale. <!-- src:
20260718-10-synthesis.md §2 -->

The instrument, IVR-1.1, rated each item on seven dimensions: key validity (`kv`),
anchor fidelity (`af`), clarity (`cl`), generic recoverability (`gr`), pair integrity
(`pi`), bias (`bi`), and an overall severity — with severity **derived mechanically**
from the dimension verdicts rather than judged directly. <!-- src:
20260718-04-irr-report.md §1; 20260718-10-synthesis.md §2. Editor note: report 04
counts severity within "seven dimensions"; synthesis says "six item-level dimensions"
plus derived severity — same instrument, do NOT "correct" seven to six. --> Packets carried full
administrations, verbatim keys, grep-verified anchor excerpts with pack-entry
resolution, and the design's harness rubric. <!-- src: 20260718-10-synthesis.md §2 -->

The instrument was locked on a 20-item, two-round calibration set, with a
planted-defect detection check **passed exactly**. <!-- src: 20260718-10-synthesis.md
§2 --> Two calibration changes carried the move from IVR-1.0 to IVR-1.1. Severity was
switched from a directly rated axis — the least reliable dimension under IVR-1.0
(κ = 0.160) — to a fixed-rule computation from the dimension verdicts, raising
calibration agreement to **κ = 0.638**. <!-- src: 20260718-04-irr-report.md §2 -->
And anchor-fidelity excerpt provisioning (sharpening the defective-anchor definition
and resolving pack-excerpt status) raised `af` calibration agreement from
**κ = 0.462 to κ = 1.000**. <!-- src: 20260718-04-irr-report.md §2 --> Key validity
also rose over the same calibration (κ = 0.508 → 0.778). <!-- src:
20260718-04-irr-report.md §2 -->

The review had teeth at three levels. Disagreements at the major/blocker severity
level were adjudicated by a stronger model tier; every surviving substantive finding
received an independent refute-first adversarial review; and mechanically checkable
claims (budgets, contamination, citation existence, grid feasibility, guard
enumeration) were verified by script or by construction. <!-- src:
20260718-10-synthesis.md §2 -->

## X.3 Reliability results

Table 1 reports pooled agreement on the full sweep for each dimension and surface, as
raw agreement, unweighted Cohen's κ, and linear-weighted κ_w where the dimension is
ordinal.

**Table 1. Pooled inter-rater reliability of the IVR-1.1 item review (public
n = 355, holdout n = 158).** <!-- src: 20260718-04-irr-report.md §3; 20260718-10-synthesis.md §3 -->

| Dimension | Raw (pub / hold) | κ (pub / hold) | κ_w (pub / hold) |
|---|---|---|---|
| keyed validity | .966 / .962 | .686 / .632 | **.760 / .758** |
| anchor fidelity | .732 / .791 | .408 / .508 | .408 / .503 |
| clarity | .823 / .842 | .469 / .533 | .465 / .588 |
| generic recoverability | .721 / .690 | .538 / .453 | .606 / .518 |
| gr (binary generic-vs-not) | .848 / .817 | .637 / .564 | — |
| pair integrity | .980 / .987 | −.005 / .495 | — |
| bias flag | .904 / .867 | .527 / .386 | — |
| derived severity | .699 / .741 | .469 / .549 | **.539 / .627** |

The headline is that **keyed validity reached κ_w 0.760 on the public surface and
0.758 on the holdout — 0.76 on both surfaces** — making it the most reliable
substantive channel. <!-- src: 20260718-04-irr-report.md §3; 20260718-10-synthesis.md §3 -->
For the headline generic-vs-not use, the binary collapse `gr_binary` is the reliable
cut (**κ = 0.637 public, 0.564 holdout**), because the residual disagreement in the
three-level scale is concentrated at the mixed↔corpus_required boundary where raters
legitimately differ on how much corpus lensing a marginal item needs. <!-- src:
20260718-04-irr-report.md §6 --> The mechanically derived severity — the operative
headline for defect burden — sat at **κ_w 0.539 public / 0.627 holdout**. <!-- src:
20260718-04-irr-report.md §3 -->

Two dimensions require careful reading rather than face-value κ. Pair integrity shows
a **base-rate paradox**: raw agreement 0.980 but κ = −0.005 on the public surface,
because the dimension is overwhelmingly `holds`/`na` (only ≈1.7% `confound`) so chance
agreement nearly equals observed agreement and κ collapses even though the raters
almost never disagree — the few disagreements are non-overlapping minority `confound`
flags. For `pi`, raw agreement (0.980) is the figure to read, not κ. <!-- src:
20260718-04-irr-report.md §5 --> The `af` and `cl` κ are depressed by the
evidence-starved `supports↔partial` boundary on table-of-contents-level excerpts —
an **instrument limitation, not item noise**. That this is a packet-excerpt
limitation rather than an anchor-invalidity signal is shown directly by the
calibration, where `af` reaches **κ = 1.000** once excerpts are load-bearing. <!-- src:
20260718-10-synthesis.md §3; 20260718-04-irr-report.md §2 -->

## X.4 Adversarial refutation of contested keys

The sweep surfaced **ten substantive "the key is wrong or contestable" candidates**.
Under refute-first adversarial review, **three were killed outright — WW-03-C01,
WW-05-D04, and WW-08-C04 — one of them by constructive proof**, and the ledger
disposition for all three is REFUTED-no-edit. <!-- src: 20260718-10-synthesis.md §1,
§5; RULINGS-APPLIED-20260724b.md §Regeneration --> The remaining candidates were
reduced to bounded edits, and exactly one instrument-level keying decision (the
WW-08-B02 ↔ F03 protected-state inconsistency, PE-8) was escalated for owner judgment.
<!-- src: 20260718-10-synthesis.md §1 -->

A kill-rate of 3-in-10 is doubly informative. It is evidence that the items' guards
are **better engineered than first-pass expert reading suggests** — enumeration and
constructive proof both vindicated the authors against a plausible challenge — and it
is evidence that the review process itself has teeth, in that a finding can die rather
than being waved through to an edit. <!-- src: 20260718-10-synthesis.md §5 -->

## X.5 Construct validity

The generic-recoverability construct behaves as the design intends. Joining the
rater-derived GR label to per-item difficulty (315 items joined) yields a monotone
gradient: **corpus_required items are 18.1pp harder than generic items (mean pass rate
0.4733 vs 0.6546; n = 30 corpus_required vs 76 generic, with the remaining 209 of the
315 joined items in the mixed class)**. <!-- src: 20260718-08-substudies.md §S3.1 --> The floor rate rises **2.9× (26.7% for
corpus_required vs 9.2% for generic)**, and ceiling saturation falls **2.4× (13.3% vs
31.6%)** — the exact signature expected if items whose keyed behavior a generic
assistant can recover are easier and items that require the corpus are harder. <!-- src:
20260718-08-substudies.md §S3.1 --> The mixed class sits between the two on every axis.
<!-- src: 20260718-08-substudies.md §S3.1 -->

The per-design %-non-generic ranking corroborated and refined the pre-existing
corpus-distinctiveness annotation, CV-1. **All three CV-1-flagged designs (d04, d05,
d10) landed in the top five** by share of non-generic items, confirming the flag.
<!-- src: 20260718-08-substudies.md §S3.2 --> But the ranking also surfaced **d06 and
d07 (96.3% non-generic each) at ranks two and three, un-flagged by CV-1** — more
non-generic than two of the three designs CV-1 does flag — identifying them as
CV-1 under-inclusion candidates. <!-- src: 20260718-08-substudies.md §S3.2 --> On this
evidence the CV-1 annotation was amended to add designs 06 and 07 (PE-22). <!-- src:
RULINGS-APPLIED-20260724.md PE-22 -->

## X.6 Defect taxonomy, artifact partition, and disposition

The synthesis verdict is that **the WALKWORTHY v2 item banks are substantively sound
and psychometrically defensible; their defect burden is almost entirely
infrastructural and class-fixable.** <!-- src: 20260718-10-synthesis.md §1 --> The
severity accounting in Table 2 makes the shape of that burden concrete.

**Table 2. Severity accounting from the double-rated sweep (public n = 355, holdout
n = 158).** <!-- src: 20260718-10-synthesis.md §4 -->

| Surface | Agreed clean | Agreed minor | Agreed major/blocker | Disputed → adjudicated |
|---|---|---|---|---|
| public (n = 355) | 126 | 108 | 14 | 107 |
| holdout (n = 158) | 64 | 46 | 7 | 41 |

On the public surface, 13 of the 14 agreed major/blocker items were the empty-key
class plus WW-08-B02; most of the 107 disputed items were adjudicated down to minor or
reclassified as instrument artifacts (packet-header construct oversimplification,
packet-builder pack extraction, table-of-contents-excerpt starvation), with a small
set of confirmed additions. <!-- src: 20260718-10-synthesis.md §4 --> The holdout
mirrored the pattern with a slightly cleaner profile. <!-- src: 20260718-10-synthesis.md §4 -->

The major defect classes each had an infrastructural root cause rather than a
knowledge gap. The **empty-key class (~20 items)** stemmed from a marker-variant
parsing mismatch — annotated `**Keyed** *(…)*.` markers failing the converter's exact
`**Keyed.**` regex — so keys that were already inlined in the banks failed to convert;
the fix was marker normalization, not missing knowledge. <!-- src:
20260718-10-synthesis.md §1; RULINGS-APPLIED-20260724.md PE-1 --> **Scaffold
contamination touched 84 items but resolved to a single converter fix** (a
fence-aware trailing-boundary scrub). <!-- src: 20260718-10-synthesis.md §1;
RULINGS-APPLIED-20260724.md PE-5 --> The **design-05 budget=0.0 scorer misfire** on 9
items — where a zero budget short-circuited the allocation sum-check — was a routing
gap, not an item error. <!-- src: 20260718-10-synthesis.md §1;
20260718-08-substudies.md §Metric-routing --> And the **design-04 and design-10
metric-routing gaps** (zero-direction items pooling into the signed motive mean; no
routing flag for the licensed-asymmetry construct) were likewise confined to the
metric layer. <!-- src: 20260718-08-substudies.md §Metric-routing. Editor note: do not
insert a zero-direction item COUNT here without reconciling the two censuses —
substudies reports 12 public zero-direction at assessment time, PE-19 reports 18 zero
post-population (9 missing directions were populated as "zero"); pre-fix vs post-fix
censuses differ by design. -->

The single most important methodological point in this section is the
**instrument-versus-item partition**. The C5 "wrong pack content" class — which on
first pass looked like a substantive anchor-content defect — was in fact an artifact
of the assessment tooling: the packet-builder's pack-extraction routine matched a
generic num-bold pattern in the scenario list ahead of the letter-prefixed pack
claims, so prefix-less citations resolved to scenario stubs. The fix was applied and
**proven 11/11 (PE-24)**: after searching the pack text before the scenario-motifs
section, the K-series claims resolved correctly with no regression on C-style or
plain-numbered packs. <!-- src: RULINGS-APPLIED-20260724b.md §PE-24 --> The general
lesson is that a review of item quality must partition instrument artifacts from item
defects, or it will overstate the defect burden — here, an apparent content defect was
entirely a property of the reviewing tool. <!-- src: RULINGS-APPLIED-20260724b.md §PE-24 -->

Disposition was fully governed. **All 25 proposed-edits ledger entries (PE-1..25) were
owner-ruled and applied; separately, three contested-key findings were ruled
REFUTED-no-edit** (WW-03-C01, WW-05-D04, WW-08-C04 — the adversarial kills of §X.4,
which produced no ledger edit by construction). <!-- src:
RULINGS-APPLIED-20260724b.md §Regeneration --> The
post-fix **bank revision 2026-07-24b** verifies at **public 344/344/563 and holdout
158/158/260**, with every defect-class census at zero (empty-key 0, contamination 0,
budget≤0 0, missing direction 0) and the full test suite at **33/33 pass**. <!-- src:
RULINGS-APPLIED-20260724b.md §Regeneration -->

## X.7 Post-fix instrument verification

Because the fixes touched scoring paths and not merely bank text, a changed-items
**smoke rescore** verified end-to-end that the repaired instrument executes live. The
matrix covered **the 26 public administrations changed since the 2026-07-16 pilot,
grouped into 7 design tasks**; running **7 design tasks × 5 pilot SUTs × 3 independent
single-epoch runs gave 105/105 successful invocations at ≈$0.79**. <!-- src:
20260724-changed-items-smoke-report.md §Authorization, §What ran; note: the invocation
grid multiplies design tasks (7×5×3=105), NOT administrations — 26×5×3 is not the
invocation count -->
Cell n's are tiny by design (1–6 items per cell); the numbers exist as verification
evidence that the edited instrument works, not as model measurement. <!-- src:
20260724-changed-items-smoke-report.md header -->

Every new instrument channel was confirmed live. The design-02 **`pushback_rate`
sub-metric (PE-18) was nonzero and SUT-differentiated (means 0.04–0.29)**, so the
third-way `pushback_with_alternative` state is no longer invisible. <!-- src:
20260724-changed-items-smoke-report.md §Instrument verification --> The design-04
**`zero_delta_compliance` routing (PE-19) separated SUTs (≈0.85 vs 0.00 across the two
extremes)** with `missing_direction = 0`, and the signed motive mean no longer pooled
zero-keyed items. <!-- src: 20260724-changed-items-smoke-report.md §Instrument
verification --> The design-05 **CSR sum-enforcement (PE-21) bit — a 0.70 cell with a
rationale-gated 0.667** — where the sum-check had previously been silently waived.
<!-- src: 20260724-changed-items-smoke-report.md §Instrument verification --> The
three repaired design-07 items (WW-07-F02/I04/L02) **scored validly for the first
time**, and their **0/45 arc-pass rate is a genuine model-behavior floor
(transcript-verified, not a parse artifact)**, consistent with the pilot's d07
floor-saturation note. <!-- src: 20260724-changed-items-smoke-report.md §Instrument
verification, §Judge-A results --> The WW-08-B02 **protected state (PE-8) emitted live
`protected` verdicts** on the overt arm, and the covert/overt contrast operated as
designed. <!-- src: 20260724-changed-items-smoke-report.md §Instrument verification -->

## X.8 Limitations

Five limitations bound the strength of this validity evidence.

**(1) LLM-raters only.** Every κ reported here is LLM-vs-LLM agreement and is an
**upper bound** on the human-rater agreement the same instrument would achieve, since
the two model raters share systematic priors. <!-- src: 20260718-04-irr-report.md §1 -->

**(2) Single-benchmark scope.** The construct- and content-validity evidence is drawn
entirely from the WALKWORTHY v2 banks; none of it speaks to generalization beyond this
benchmark. <!-- src: 20260718-04-irr-report.md §1 -->

**(3) C9 comparability discontinuity.** Bank revision 2026-07-24b is **not comparable
to the 2026-07-16 pilot on the changed cells**: design-07 items were unscorable then
and are newly scorable now; design-05 CSR now enforces sum-correctness that was
silently waived; design-04 zero-keyed items are now excluded from the signed mean;
WW-08-B02 was re-keyed; and four items' prompt text changed. Any future full run must
cite the discontinuity. <!-- src: RULINGS-APPLIED-20260724.md §Comparability;
RULINGS-APPLIED-20260724b.md §Comparability; 20260724-changed-items-smoke-report.md §Comparability -->

**(4) Judge sensitivity.** Every design is judge-sensitive at this tier, with ladders
most sensitive: in the smoke rescore, **design-02 judge-B exact-match agreement was
0.133**. <!-- src: 20260724-changed-items-smoke-report.md §Judge-B agreement --> The
WW-08-B02 protected-boundary reading is itself judge-dependent — judge-B read
`protected→steamrolled` on 4 of 30 administrations — and is flagged as a watch item to
revisit if design-08 metrics are ever promoted to claims. <!-- src:
20260724-changed-items-smoke-report.md §Judge-B agreement -->

**(5) Smoke evidence is descriptive only.** The smoke rescore carries no rankings,
composites, significance language, or per-SUT claims; its cell n's are tiny by design
and its role is instrument verification, not model measurement. <!-- src:
20260724-changed-items-smoke-report.md header -->

---

## Source map

1. `REPORTS/20260718-item-assessment/20260718-04-irr-report.md` — inter-rater reliability of the IVR instrument (Table 1, calibration, base-rate paradox, gr_binary).
2. `REPORTS/20260718-item-assessment/20260718-08-substudies.md` — S3 GR × difficulty gradient, S1 design-02 taxonomy, metric-routing checks (§X.5, §X.6 routing gaps).
3. `REPORTS/20260718-item-assessment/20260718-10-synthesis.md` — verdict, defect taxonomy, severity accounting (Table 2), adversarial kills.
4. `RULINGS-APPLIED-20260724.md` — fix disposition PE-1..8/18..22, C9 comparability note.
5. `RULINGS-APPLIED-20260724b.md` — fix disposition PE-9..17/23..25, PE-24 instrument artifact partition, full ledger closure, bank rev 2026-07-24b.
6. `20260724-changed-items-smoke-report.md` — post-fix instrument verification (smoke rescore, §X.7), judge-sensitivity watch items.

<!-- Canary: WALKWORTHY-CANARY-7f3e2026 -->
