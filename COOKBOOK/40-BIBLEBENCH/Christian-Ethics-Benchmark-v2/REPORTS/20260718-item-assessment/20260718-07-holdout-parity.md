<!-- Canary: WALKWORTHY-CANARY-7f3e2026 -->

# WALKWORTHY v2 — Public / Holdout Parity (M6)

**Report 07 of the 2026-07-18 item assessment** (355 public + 158 holdout items, all
double-rated; program overview in sibling report `20260718-00`). This report reproduces
the M6 public-vs-holdout parity audit, which asks whether the held-out surface is
structurally comparable to the public surface on the properties that govern difficulty and
scorability. **Every figure below is an aggregate or a rate; the M6 source is aggregate-
only and this report contains zero holdout item IDs and zero holdout item text.**

Source: `logs/item-assessment-20260718/m6-parity.md` (only). The M6 script is
`tools/audit/item_assess_m6_parity.py`.

---

## 1. Pooled parity headline

The two surfaces are close on every pooled property; the five largest deltas
(holdout − public) are:

| Rank | Metric | Public | Holdout | Delta (hld − pub) |
|------|--------|--------|---------|-------------------|
| 1 | n_admin_lines | 575 | 260 | −315.00 |
| 2 | n_items (unique) | 355 | 158 | −197.00 |
| 3 | IVR consensus clean % | 35.5% | 40.5% | +5.02 |
| 4 | IVR disputed % | 30.1% | 25.9% | −4.19 |
| 5 | stratum_c % | 6.8% | 9.5% | +2.73 |

The two largest deltas (admin-line and item counts) are simply the size difference
between the surfaces (holdout is ~44% the size of public) and are not comparability
concerns. The substantive deltas are small: **runnable_rate +2.09pp** (97.9% → 100.0%),
**char_len mean −40.5**, **difficulty hard % −1.51pp** (77.5% → 76.0%), **M1 defect rate
−0.70pp** (2.0% → 1.3%), **M2 mean anchors/item +0.24** (5.068 → 5.310). None of these
crosses a comparability threshold at the pooled level.

**IVR consensus-clean is +5.02pp cleaner on holdout** (35.5% → 40.5%), with disputed
correspondingly −4.19pp; the holdout surface is, if anything, marginally cleaner than
public.

---

## 2. Per-design comparability verdicts

The M6 grid assigns each design a `comparable` / `non-comparable` verdict based on
per-design deltas in runnable rate, stratum-C share, difficulty-hard share, and M1 defect
rate. Five designs are comparable; five are flagged divergent with the quantified deltas
below.

### 2.1 Comparable (5)

| Design | Pub / Hld items | Note |
|--------|-----------------|------|
| d01 | 49 / 22 | run 100/100; char_mean 1195/1195; hard 79.6/81.8. |
| d04 | 33 / 15 | run 100/100; char_mean 1081/1138; hard 87.9/86.7. |
| d08 | 33 / 15 | run 100/100; char_mean 1883/2032; hard 69.7/66.7. |
| d09 | 38 / 17 | run 95.7/100; char_mean 1965/1937; hard 71.0/70.6. |
| d10 | 36 / 16 | run 100/100; char_mean 2163/2197; hard 72.2/68.8. |

### 2.2 Divergent (5), with quantified deltas

| Design | Verdict driver(s) |
|--------|-------------------|
| d02 | non-comparable: runnable_rate delta **+5.3**; stratum_c delta **+5.6**. |
| d03 | non-comparable: stratum_c delta **+13.3**. |
| d05 | non-comparable: difficulty_hard delta **−10.7**; stratum_c delta **−5.8**. |
| d06 | non-comparable: difficulty_hard delta **−5.7**; stratum_c delta **+6.2**. |
| d07 | non-comparable: m1_defect_rate delta **−7.2**; runnable_rate delta **+12.9**; stratum_c delta **+15.4**. |

**design-07 is the most divergent design.** It carries the largest single-design deltas
on all three drivers — runnable rate +12.9pp, stratum-C share +15.4pp, and an M1 defect
rate −7.2pp — and in every case the divergence points the same direction: **the holdout
d07 surface is cleaner than public d07** (public d07 runnable rate is 87.1% and its M1
defect rate 22.6%, both driven by the public empty-key exemplar cluster documented in
report `20260718-03`; the holdout d07 subset is 100% runnable with a 15.4% M1 defect
rate). The d07 divergence is therefore a defect-concentration artifact on the public side,
not a holdout weakness.

d03's divergence is a single-driver stratum-C shift (+13.3pp); d05/d06 are difficulty-mix
shifts (holdout d05 is 10.7pp *less* hard, holdout d06 5.7pp less hard); d02 is a joint
runnable/stratum shift.

---

## 3. IVR consensus-clean lift on holdout

Consistent with §1, the holdout surface is **+5.0pp cleaner** at IVR consensus (public
35.5% clean vs holdout 40.5% clean; disputed 30.1% vs 25.9%). The pooled consensus
severity distributions are:

| Level | Public n / % | Holdout n / % |
|-------|--------------|----------------|
| clean | 126 / 35.5% | 64 / 40.5% |
| minor | 108 / 30.4% | 46 / 29.1% |
| major | 1 / 0.3% | 3 / 1.9% |
| blocker | 13 / 3.7% | 4 / 2.5% |
| disputed | 107 / 30.1% | 41 / 25.9% |

The holdout surface carries proportionally slightly more `major` (1.9% vs 0.3%) but fewer
`blocker` (2.5% vs 3.7%) and fewer `disputed` — net, a marginally cleaner surface.

---

## 4. Design-01 cross-surface structural-twin consideration

The M4 within-design similarity block flags **design-01** as the design most likely to
carry near-duplicate item structure across items and across surfaces: its public
within-design max similarity is **0.8782** and its holdout max is **0.7933** — the highest
maxima of any design (next-highest public max is d09 at 0.8625; most designs sit below
0.41). This signals a small number of **structural mirror pairs** — items that share the
same scaffold across the public and holdout surfaces — concentrated in design-01.

Described in aggregate only: the design-01 structural-twin cluster comprises **five mirror
pairs** whose public/holdout members share scenario scaffolding. This is a
cross-surface-leakage / difficulty-comparability consideration rather than a defect: it
affects whether a d01 holdout item can be treated as fully independent of its public twin
for held-out evaluation. The pair-level detail (which public scaffolds have mirrors, and
the leakage assessment) is documented in report **`20260718-06`**; it is not reproduced
here because per-pair identification would risk associating holdout members with their
public scaffolds. For parity purposes, d01 remains `comparable` on the M6 grid (run
100/100, char_mean 1195/1195, hard 79.6/81.8); the structural-twin note is a caveat on
*independence*, not on *comparability*.

---

## 5. Conclusion

The public and holdout surfaces are **broadly parity-consistent**. Pooled properties match
within a few points on every axis; the holdout surface is marginally *cleaner* at IVR
consensus (+5.0pp clean). Five designs (d01/d04/d08/d09/d10) are comparable; five
(d02/d03/d05/d06/d07) are flagged divergent, with **d07 the most divergent** — and in the
d07 case the divergence reflects a *cleaner* holdout subset against a defect-concentrated
public d07, not a holdout deficiency. The one standing independence caveat is the
**design-01 five-mirror-pair structural-twin cluster** (report `20260718-06`), which bears
on cross-surface item independence rather than on parity itself. Subject to those named
exceptions, the holdout surface is a valid parity match to the public surface.

<!-- Canary: WALKWORTHY-CANARY-7f3e2026 -->
