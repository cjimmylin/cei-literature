# Divergence-Split Re-Emission — Addendum

**Date:** 2026-07-16
**ADDENDUM to 20260716-pilot-report.md — divergence-split re-emission (F1, 20260716 adjudication)**

---

> **PROVISIONAL — the divergence tags are a construct-defining artifact produced by 10 disjoint per-design Claude Agent taggers (refute-first framing) on 2026-07-16 and are PENDING OWNER REVIEW. No headline may cite this split until the owner ratifies the tags (F1 gate).**

> Results measure fidelity to a named, Protestant-Reformed-dominant corpus — never 'Christianity'; designs 01/02/03/06/07/08/09 are not discriminant vs generic RLHF harmlessness on most items; 04/05/10 are the corpus-distinctive slice.

---

## 0. What this addendum does

It re-emits the pilot's per-design cells (from `20260716-pilot-report.md` §3) **partitioned by an item-level divergence tag**: whether the keyed anchor for an item requires something a well-RLHF'd secular model would *not* already do (`yes`), does so only in part (`partial`), or not at all (`no`). Every number here is a **100% offline recompute** over the stored pilot logs — no SUT call, no judge call. The tool is `tools/audit/divergence_split.py`; the full cell dump is `/tmp/divergence-split-cells.json` (regenerate with `--out`).

Scope matches the pilot report headline scope exactly: **exemplars dropped, stratum (a) only** (stratum (c) intra-corpus-dispute items quarantined — judge not G5-neutrality-certified in v2). Under that scope every `all` cell below **reproduces the pilot report §3 numbers** (cross-check PASS, §6).

---

## 1. Tag distribution (from the sidecar)

`banks/20260716-divergence-tags.jsonl`, one row per public runnable item (344 total).

| Design | yes | partial | no | total |
|---|---:|---:|---:|---:|
| 01-goodsamaritan | 4 | 12 | 33 | 49 |
| 02-twomasters | 4 | 10 | 22 | 36 |
| 03-quiettongue | 0 | 11 | 22 | 33 |
| 04-innerweight | 0 | 29 | 4 | 33 |
| 05-ordoamoris | 2 | 10 | 20 | 32 |
| 06-crookedpath | 0 | 3 | 28 | 31 |
| 07-seventyseven | 5 | 22 | 0 | 27 |
| 08-vocationfork | 0 | 6 | 27 | 33 |
| 09-doubleedge | 4 | 11 | 19 | 34 |
| 10-strangergate | 10 | 15 | 11 | 36 |
| **TOTAL** | **29** | **129** | **186** | **344** |

The distribution is consistent with the CV-1 shape: the corpus-distinctive slice (04/05/10) and the multi-turn arc (07) concentrate the `yes`/`partial` mass; the harmlessness-adjacent designs (03/06/08) are almost entirely `no`.

---

## 2. Method note

Tags were produced by **10 disjoint per-design opus Claude Agent dispatches** under a **refute-first framing**: "assume NO divergence unless the keyed anchor requires something a well-RLHF'd secular model would not do." Each item was tagged **once per item** across all its administrations (say/do, alpha/beta, covert/overt, seat_A/seat_B, N/U, and every ladder turn share one tag). The taggers were **NOT told the expected CV-1 shape**.

**Cross-design calibration caveat.** Because the taggers were disjoint (one per design, for anti-leakage), the `partial` threshold varies by tagger: design 04 tagged 29/33 items `partial` while design 06 tagged only 3/31. Disjointness bought anti-leakage at the cost of calibration — `partial` is not a common yardstick across designs, so **within-design** comparisons across the yes/partial/no cells are the only ones the split supports.

---

## 3. Split tables (judge-A, stratum-a headline scope)

**Reading rules (R1/R3/R4):** these tables carry **no ranking, no ordering language, no significance claims**. Cells are judge-sensitive (the pilot's headline finding), so **no SUT-vs-SUT comparison is made**. Overlapping CIs, where noted, mean "indistinguishable at pilot n". `*` marks an **insufficient-n cell (n < 10 surviving units, R2)** — the number is printed but must not be read as an estimate. Wilson 95% CIs are shown for binary-rate metrics; delta/profile/CSR metrics carry n only (bootstrap deferred). R8 joint companions are printed next to every headline.

Column key: `est [Wilson lo, hi] (n)`; paired designs show `headline / companion (n pairs)`.

### Design 01 — `full_obedience_rate`

| SUT | all | no | partial | yes | yes+partial |
|---|---|---|---|---|---|
| deepseek-chat | 0.6667 [.516,.790] (42) | 0.7241 [.543,.853] (29) | 0.6000 [.313,.832] (10) | 0.3333 [.061,.792] (3*) | 0.5385 [.291,.768] (13) |
| gemini-flash-lite | 0.6905 [.540,.809] (42) | 0.7586 [.579,.878] (29) | 0.6000 [.313,.832] (10) | 0.3333 [.061,.792] (3*) | 0.5385 [.291,.768] (13) |
| gpt-4.1-mini | 0.6667 [.516,.790] (42) | 0.6552 [.473,.801] (29) | 0.8000 [.490,.943] (10) | 0.3333 [.061,.792] (3*) | 0.6923 [.424,.873] (13) |
| llama-3.3-70b | 0.5476 [.400,.688] (42) | 0.6207 [.440,.773] (29) | 0.3000 [.108,.603] (10) | 0.6667 [.208,.939] (3*) | 0.3846 [.177,.645] (13) |
| mistral-small | 0.4762 [.334,.623] (42) | 0.5172 [.344,.686] (29) | 0.4000 [.168,.687] (10) | 0.3333 [.061,.792] (3*) | 0.3846 [.177,.645] (13) |

### Design 02 — `break_rate`

| SUT | all | no | partial | yes | yes+partial |
|---|---|---|---|---|---|
| deepseek-chat | 0.5571 [.441,.667] (70) | 0.5581 [.411,.696] (43) | 0.5500 [.342,.742] (20) | 0.5714 [.250,.842] (7*) | 0.5556 [.373,.724] (27) |
| gemini-flash-lite | 0.5857 [.469,.694] (70) | 0.6512 [.502,.776] (43) | 0.4500 [.258,.658] (20) | 0.5714 [.250,.842] (7*) | 0.4815 [.307,.660] (27) |
| gpt-4.1-mini | 0.5882 [.470,.697] (68) | 0.6667 [.516,.790] (42) | 0.4737 [.273,.683] (19) | 0.4286 [.158,.750] (7*) | 0.4615 [.287,.645] (26) |
| llama-3.3-70b | 0.6029 [.484,.711] (68) | 0.6667 [.516,.790] (42) | 0.5263 [.317,.727] (19) | 0.4286 [.158,.750] (7*) | 0.5000 [.321,.679] (26) |
| mistral-small | 0.5441 [.426,.657] (68) | 0.5714 [.422,.709] (42) | 0.5789 [.363,.768] (19) | 0.2857 [.082,.641] (7*) | 0.5000 [.321,.679] (26) |

### Design 03 — `say_do_gap` / `revealed_faithful_rate` (R8; CI on revealed rate)

No `yes` items keyed for this design (0 in the sidecar), so the `yes` and `yes+partial` cells equal the `partial` cell.

| SUT | all | no | partial (= yes+partial) |
|---|---|---|---|
| deepseek-chat | 0.4828 / 0.4138 [.255,.593] (29) | 0.4211 / 0.5263 [.317,.727] (19) | 0.6000 / 0.2000 [.057,.510] (10) |
| gemini-flash-lite | 0.5862 / 0.3448 [.199,.526] (29) | 0.5263 / 0.4737 [.273,.683] (19) | 0.7000 / 0.1000 [.018,.404] (10) |
| gpt-4.1-mini | 0.3214 / 0.4286 [.265,.609] (28) | 0.3889 / 0.5000 [.290,.710] (18) | 0.2000 / 0.3000 [.108,.603] (10) |
| llama-3.3-70b | 0.5172 / 0.3448 [.199,.526] (29) | 0.4737 / 0.4737 [.273,.683] (19) | 0.6000 / 0.1000 [.018,.404] (10) |
| mistral-small | 0.2857 / 0.3929 [.236,.576] (28) | 0.3889 / 0.4444 [.246,.663] (18) | 0.1000 / 0.3000 [.108,.603] (10) |

### Design 04 ◆ — `motive_delta_mean` (signed) / `motive_correct_rate` (R8; CI on correct rate)

No `yes` items keyed (0 in the sidecar); `yes+partial` equals `partial`. The `no` cell is n=3* everywhere (insufficient).

| SUT | all | no | partial (= yes+partial) |
|---|---|---|---|
| deepseek-chat | 0.1759 / 0.5000 [.314,.686] (24) | 0.2222 / 0.3333 (3*) | 0.1693 / 0.5238 [.324,.717] (21) |
| gemini-flash-lite | 0.1806 / 0.4583 [.279,.649] (24) | 0.0741 / 0.3333 (3*) | 0.1958 / 0.4762 [.283,.676] (21) |
| gpt-4.1-mini | 0.1713 / 0.5000 [.314,.686] (24) | 0.2963 / 0.0000 (3*) | 0.1534 / 0.5714 [.365,.755] (21) |
| llama-3.3-70b | 0.2917 / 0.2500 [.120,.449] (24) | 0.1852 / 0.0000 (3*) | 0.3069 / 0.2857 [.138,.499] (21) |
| mistral-small | 0.2407 / 0.5000 [.314,.686] (24) | 0.2222 / 0.3333 (3*) | 0.2434 / 0.5238 [.324,.717] (21) |

### Design 05 ◆ — `csr_mean` (RECOVERED, judge-free; see §5)

CSR was recovered from stored completions with the corrected alloc-spec path (the stored 05 Score values predate the fix and are all `nan`; see §5). n is CSR-decidable items after the format gate — coverage is low, so **every 05 cell is insufficient-n and the `yes` cells are empty (n=0)**. Read this table only as "CSR on the handful of format-compliant items," never as a rate.

| SUT | all | no | partial | yes+partial |
|---|---|---|---|---|
| deepseek-chat | 0.8542 (4*) | 0.8056 (3*) | 1.0000 (1*) | 1.0000 (1*) |
| gemini-flash-lite | 0.9074 (9*) | 0.8958 (8*) | 1.0000 (1*) | 1.0000 (1*) |
| gpt-4.1-mini | 0.8561 (11) | 0.8021 (8*) | 1.0000 (3*) | 1.0000 (3*) |
| llama-3.3-70b | 0.7963 (9*) | 0.7381 (7*) | 1.0000 (2*) | 1.0000 (2*) |
| mistral-small | 0.9306 (12) | 0.9074 (9*) | 1.0000 (3*) | 1.0000 (3*) |

(`yes` cells are all n=0 → `nan`, omitted from the table.)

### Design 06 — `profile_mean` (PROVISIONAL: G5-uncertified)

Only 3 `partial` items corpus-wide and 0 `yes` (the design-06 tagger was the strictest); every non-`no` cell is n=1* per SUT.

| SUT | all | no | partial (= yes+partial) |
|---|---|---|---|
| deepseek-chat | 0.8250 (20) | 0.8158 (19) | 1.0000 (1*) |
| gemini-flash-lite | 0.9393 (20) | 0.9436 (19) | 0.8571 (1*) |
| gpt-4.1-mini | 0.9036 (20) | 0.9060 (19) | 0.8571 (1*) |
| llama-3.3-70b | 0.6286 (20) | 0.6203 (19) | 0.7857 (1*) |
| mistral-small | 0.5250 (20) | 0.5376 (19) | 0.2857 (1*) |

### Design 07 — `arc_pass_rate` (floor-saturated)

No `no` items keyed (0 in the sidecar); `all` equals `yes+partial`. Floor holds across every cell.

| SUT | all (= yes+partial) | partial | yes |
|---|---|---|---|
| deepseek-chat | 0.0000 [.000,.125] (27) | 0.0000 [.000,.149] (22) | 0.0000 [.000,.434] (5*) |
| gemini-flash-lite | 0.0000 [.000,.125] (27) | 0.0000 [.000,.149] (22) | 0.0000 [.000,.434] (5*) |
| gpt-4.1-mini | 0.0000 [.000,.125] (27) | 0.0000 [.000,.149] (22) | 0.0000 [.000,.434] (5*) |
| llama-3.3-70b | 0.0000 [.000,.125] (27) | 0.0000 [.000,.149] (22) | 0.0000 [.000,.434] (5*) |
| mistral-small | 0.0000 [.000,.125] (27) | 0.0000 [.000,.149] (22) | 0.0000 [.000,.434] (5*) |

### Design 08 — `covert_overt_gap` / `covert_protection_rate` (R8; CI on protection rate)

No `yes` items keyed; `yes+partial` equals `partial` (n=4* everywhere).

| SUT | all | no | partial (= yes+partial) |
|---|---|---|---|
| deepseek-chat | 0.0179 / 0.8929 [.728,.963] (28) | 0.0000 / 0.9583 [.797,.993] (24) | 0.1250 / 0.5000 [.150,.850] (4*) |
| gemini-flash-lite | 0.1154 / 0.7308 [.539,.863] (26) | 0.1591 / 0.7273 [.518,.869] (22) | −0.1250 / 0.7500 [.301,.954] (4*) |
| gpt-4.1-mini | 0.1250 / 0.7857 [.605,.898] (28) | 0.1250 / 0.7917 [.595,.908] (24) | 0.1250 / 0.7500 [.301,.954] (4*) |
| llama-3.3-70b | 0.1964 / 0.7143 [.529,.848] (28) | 0.1875 / 0.7083 [.508,.851] (24) | 0.2500 / 0.7500 [.301,.954] (4*) |
| mistral-small | 0.2593 / 0.6296 [.442,.785] (27) | 0.2609 / 0.6522 [.449,.812] (23) | 0.2500 / 0.5000 [.150,.850] (4*) |

### Design 09 — `symmetry_index` / `floor_violation_rate` (PROVISIONAL: G5-uncertified; R8)

| SUT | all | no | partial | yes | yes+partial |
|---|---|---|---|---|---|
| deepseek-chat | 0.8088 / 0.4205 (34) | 0.8421 / 0.4200 (19) | 0.6818 / 0.3929 (11) | 1.0000 / 0.5000 (4*) | 0.7667 / 0.4211 (15) |
| gemini-flash-lite | 0.7941 / 0.3523 (34) | 0.8158 / 0.3800 (19) | 0.8182 / 0.3929 (11) | 0.6250 / 0.1000 (4*) | 0.7667 / 0.3158 (15) |
| gpt-4.1-mini | 0.7353 / 0.3182 (34) | 0.6842 / 0.3400 (19) | 0.7727 / 0.2500 (11) | 0.8750 / 0.4000 (4*) | 0.8000 / 0.2895 (15) |
| llama-3.3-70b | 0.8676 / 0.7273 (34) | 0.8421 / 0.7000 (19) | 0.9091 / 0.7857 (11) | 0.8750 / 0.7000 (4*) | 0.9000 / 0.7632 (15) |
| mistral-small | 0.8235 / 0.7045 (34) | 0.8158 / 0.7000 (19) | 0.8636 / 0.6786 (11) | 0.7500 / 0.8000 (4*) | 0.8333 / 0.7105 (15) |

### Design 10 ◆ — `mercy_delta` / `mercy_pass_rate` (R8; CI on pass rate)

The only design with a workable `yes` cell (n=8*, still insufficient).

| SUT | all | no | partial | yes | yes+partial |
|---|---|---|---|---|---|
| deepseek-chat | −0.0156 / 0.7500 [.579,.868] (32) | 0.0000 / 0.8000 [.490,.943] (10) | −0.1071 / 0.7143 [.454,.883] (14) | 0.1250 / 0.7500 [.409,.928] (8*) | −0.0227 / 0.7273 [.518,.869] (22) |
| gemini-flash-lite | 0.0156 / 0.9688 [.843,.995] (32) | 0.0000 / 1.0000 [.723,1.000] (10) | 0.0000 / 1.0000 [.785,1.000] (14) | 0.0625 / 0.8750 [.529,.978] (8*) | 0.0227 / 0.9545 [.782,.992] (22) |
| gpt-4.1-mini | −0.0781 / 0.8438 [.682,.931] (32) | −0.1500 / 0.8000 [.490,.943] (10) | −0.1071 / 0.8571 [.601,.960] (14) | 0.0625 / 0.8750 [.529,.978] (8*) | −0.0455 / 0.8636 [.667,.953] (22) |
| llama-3.3-70b | 0.0469 / 0.5000 [.336,.664] (32) | −0.0500 / 0.8000 [.490,.943] (10) | 0.0357 / 0.3571 [.163,.612] (14) | 0.1875 / 0.3750 [.137,.694] (8*) | 0.0909 / 0.3636 [.197,.570] (22) |
| mistral-small | 0.0625 / 0.6875 [.514,.821] (32) | −0.0500 / 0.7000 [.397,.892] (10) | 0.0714 / 0.7143 [.454,.883] (14) | 0.1875 / 0.6250 [.306,.863] (8*) | 0.1136 / 0.6818 [.473,.836] (22) |

---

## 4. Findings (within-SUT, descriptive only)

These statements describe only how the yes/partial/no cells differ **within a single SUT**. No SUT-vs-SUT claim is made (cells are judge-sensitive, R4); every cell that touches a `yes` subset is insufficient-n (R2) and flagged as such.

- **Design 01.** For most SUTs the divergent (`yes`) cell sits **at or below** the `no` cell (e.g. gemini 0.33* yes vs 0.76 no; gpt-4.1-mini 0.33* vs 0.66; mistral 0.33* vs 0.52) — i.e. obedience on the corpus-distinctive items is lower than on the harmlessness-adjacent items within the same model. **Insufficient-n on every `yes` cell (n=3*)**; llama alone inverts (0.67* yes vs 0.62 no) but on n=3*.
- **Design 02.** `yes` cells sit **at or below** their `no` cells within each SUT (deepseek 0.57* vs 0.56 — flat; mistral 0.29* vs 0.57 — lower), but all `yes` cells are n=7* (insufficient). No stable within-SUT direction.
- **Design 03.** No `yes` items exist; the `partial` cell tends to show a **larger say–do gap and lower revealed-faithful rate** than the `no` cell within each SUT (deepseek partial 0.60/0.20 vs no 0.42/0.53; gemini 0.70/0.10 vs 0.53/0.47) — the divergent-adjacent items are where the model *does* it less than it *says*. Not universal (gpt-4.1-mini and mistral run the other way).
- **Design 04.** No `yes` items; the `no` cell is n=3* everywhere so within-SUT partial-vs-no comparison is unsupported. The `partial` cell (n=21, essentially the whole design) carries the design.
- **Design 05.** Every cell is insufficient-n after the format gate; the non-`no` cells (n=1–3*) all read 1.0000 CSR but on 1–3 items. Within each SUT, the `no` cell CSR runs slightly **below** the `all` cell — but coverage, not CSR, is the binding axis (§5).
- **Design 06.** Only 3 `partial` items corpus-wide (n=1* per SUT); no within-SUT yes/partial/no contrast is interpretable. The `all` and `no` cells are effectively identical per SUT (the design is ~95% `no`).
- **Design 07.** Floor holds identically across every cell and every SUT (0.0000, all subsets). The divergent (`yes`) and `partial` items are **equally floored** within each SUT — the floor is not concentrated in the divergent slice.
- **Design 08.** No `yes` items; the `partial` cell (n=4*) shows a **lower covert-protection rate** than the `no` cell for several SUTs (deepseek 0.50* vs 0.96; mistral 0.50* vs 0.65) — divergent-adjacent items protect less — but on n=4*.
- **Design 09.** Within each SUT the yes/partial/no symmetry cells are **close** (deepseek 1.00* / 0.68 / 0.84; llama 0.88* / 0.91 / 0.84); no consistent within-SUT direction, and every `yes` cell is n=4*. The CV-4 warning stands: high symmetry co-occurs with high floor-violation within-SUT (llama 0.87 symmetry / 0.73 floor-violation across cells).
- **Design 10.** The `mercy_pass_rate` companion is where cells move; within several SUTs the `yes` cell pass-rate sits **at or below** the `no` cell (llama 0.375* yes vs 0.80 no; deepseek 0.75* vs 0.80) — divergent items pass mercy less often — but on n=8* (insufficient). Deltas hover near 0 in every cell.

**Cross-cutting pattern (not a headline):** where a within-SUT direction is visible at all, the divergent (`yes`/`partial`) cells tend to sit **at or below** the `no` cells on the corpus-distinctive designs (01, 03, 08, 10) — models do the keyed-distinctive thing *less* than the harmlessness-adjacent thing. Every such observation is on an insufficient-n subset and is **PROVISIONAL pending tag ratification**.

---

## 5. Design-05 recovery disclosure

The live pilot ran `design05_scorer` with the alloc-spec field-path bug (top-level `keyed.allocation` instead of `keyed.extras.allocation`), so **every stored 05 Score value is `nan`**. CSR is judge-free and deterministic, so the true per-item values are recoverable at zero cost by re-parsing each stored completion with the corrected path (`tools/audit/recompute_design05_csr.py` approach, faithfully adapted into `divergence_split.py::_recover_csr_by_item`). The split tool uses this recovery for all 05 cells; **the stored 05 scores were not used**.

The 05 `all` cell here is **stratum-a only** (n=4/9/11/9/12), matching the stratum-a headline scope applied to every other design. The pilot report §3 design-05 table (n=6/14/14/13/15, CSR 0.9028/0.9226/0.8869/0.8436/0.9444) additionally counted the 9 stratum-c items per SUT; recomputing stratum-a+c together reproduces those §3 numbers exactly. The difference is the documented stratum-a scoping, not a discrepancy.

---

## 6. Cross-check against the pilot report

`divergence_split.py::crosscheck` recomputes each design's stratum-a headline by an **independent path** (direct `PRIMARY_METRICS` recompute for 01–04/06–10; independent CSR recovery for 05) and compares to the `all` subset cell. **Result: every `all` cell reproduces the independent recompute — zero mismatches.** The `all` cells also match `20260716-pilot-report.md` §3 (stratum-a headline scope) design by design.

---

## 7. Judge-B splits (produced)

Judge-B splits **were produced for all 10 designs**. `tools/audit/pilot_judge_swap.py`'s `load_sut` machinery is cleanly reusable: judge-B `SampleScore`s are rebuilt by substituting each sample's `Score.value` with the stored judge-B verdict dict (SUT response identical by construction; only the judge changed), sharing the same metadata, so the same item-level / stratum-a filtering and `PRIMARY_METRICS` recompute apply. Design-05 judge-B **reuses the judge-free recovered CSR** (CSR is deterministic, so judge-B == judge-A for 05). Judge-B pair/turn coverage is slightly lower than judge-A on a few designs (some admins lack a parsed judge-B verdict), so a handful of judge-B pair cells carry fewer surviving units — counted, never averaged over.

Compact judge-B `all` / `no` / `partial` / `yes` cells (headline, or headline/companion for paired designs; `n` = surviving units):

| Design | SUT | all | no | partial | yes |
|---|---|---|---|---|---|
| 01 | deepseek | 0.5500 (40) | 0.5185 (27) | 0.6000 (10) | 0.6667 (3*) |
| 01 | gemini | 0.4524 (42) | 0.5517 (29) | 0.3000 (10) | 0.0000 (3*) |
| 01 | gpt-4.1-mini | 0.4359 (39) | 0.4483 (29) | 0.3750 (8*) | 0.5000 (2*) |
| 01 | llama | 0.6190 (42) | 0.6897 (29) | 0.4000 (10) | 0.6667 (3*) |
| 01 | mistral | 0.5714 (42) | 0.6207 (29) | 0.5000 (10) | 0.3333 (3*) |
| 02 | deepseek | 0.7391 (69) | 0.6977 (43) | 0.8947 (19) | 0.5714 (7*) |
| 02 | gemini | 0.8030 (66) | 0.8500 (40) | 0.7222 (18) | 0.7500 (8*) |
| 02 | gpt-4.1-mini | 0.7000 (70) | 0.6905 (42) | 0.7500 (20) | 0.6250 (8*) |
| 02 | llama | 0.5286 (70) | 0.6047 (43) | 0.3684 (19) | 0.5000 (8*) |
| 02 | mistral | 0.8182 (66) | 0.8095 (42) | 0.7895 (19) | 1.0000 (5*) |
| 03 | deepseek | −0.0385 / 0.3077 (26) | −0.1176 / 0.2353 (17) | 0.1111 / 0.4444 (9*) | — |
| 03 | gemini | −0.0909 / 0.3182 (22) | −0.2353 / 0.3529 (17) | 0.4000 / 0.2000 (5*) | — |
| 03 | gpt-4.1-mini | −0.0417 / 0.2083 (24) | −0.1111 / 0.2222 (18) | 0.1667 / 0.1667 (6*) | — |
| 03 | llama | −0.1481 / 0.3333 (27) | −0.2941 / 0.3529 (17) | 0.1000 / 0.3000 (10) | — |
| 03 | mistral | −0.0690 / 0.2759 (29) | −0.1579 / 0.2632 (19) | 0.1000 / 0.3000 (10) | — |
| 04 | deepseek | 0.1414 / 0.6818 (22) | 0.0000 / 1.0000 (3*) | 0.1637 / 0.6316 (19) | — |
| 04 | gemini | 0.1401 / 0.5652 (23) | 0.0000 / 1.0000 (3*) | 0.1611 / 0.5000 (20) | — |
| 04 | gpt-4.1-mini | 0.0404 / 0.4091 (22) | 0.0556 / 0.5000 (2*) | 0.0389 / 0.4000 (20) | — |
| 04 | llama | 0.1932 / 0.3478 (23) | 0.0370 / 0.6667 (3*) | 0.2167 / 0.3000 (20) | — |
| 04 | mistral | 0.0455 / 0.3636 (22) | −0.1111 / 0.5000 (2*) | 0.0611 / 0.3500 (20) | — |
| 05 | (judge-free — identical to §3 recovery) | see Design 05 table above | | | |
| 06 | deepseek | 0.9464 (20) | 0.9436 (19) | 1.0000 (1*) | — |
| 06 | gemini | 0.9586 (20) | 0.9586 (19) | nan (1*) | — |
| 06 | gpt-4.1-mini | 0.9167 (20) | 0.9118 (19) | 1.0000 (1*) | — |
| 06 | llama | 0.8135 (20) | 0.8109 (19) | 0.8571 (1*) | — |
| 06 | mistral | 0.8045 (20) | 0.7937 (19) | 1.0000 (1*) | — |
| 07 | deepseek | 0.0000 (21) | — | 0.0000 (18) | 0.0000 (3*) |
| 07 | gemini | 0.0400 (25) | — | 0.0476 (21) | 0.0000 (4*) |
| 07 | gpt-4.1-mini | 0.0000 (24) | — | 0.0000 (20) | 0.0000 (4*) |
| 07 | llama | 0.0417 (24) | — | 0.0526 (19) | 0.0000 (5*) |
| 07 | mistral | 0.0000 (22) | — | 0.0000 (18) | 0.0000 (4*) |
| 08 | deepseek | 0.2400 / 0.6667 (25) | 0.2143 / 0.7391 (21) | 0.3750 / 0.2500 (4*) | — |
| 08 | gemini | 0.2321 / 0.5714 (28) | 0.2917 / 0.5833 (24) | −0.1250 / 0.5000 (4*) | — |
| 08 | gpt-4.1-mini | 0.3750 / 0.5385 (24) | 0.3571 / 0.5909 (21) | 0.5000 / 0.2500 (3*) | — |
| 08 | llama | 0.2407 / 0.6296 (27) | 0.2391 / 0.6522 (23) | 0.2500 / 0.5000 (4*) | — |
| 08 | mistral | 0.2200 / 0.5769 (25) | 0.2500 / 0.5652 (22) | 0.0000 / 0.6667 (3*) | — |
| 09 | deepseek | 0.8500 / 0.1071 (30) | 0.8235 / 0.0816 (17) | 0.8500 / 0.1154 (10) | 1.0000 / 0.2222 (3*) |
| 09 | gemini | 0.7333 / 0.0824 (30) | 0.6333 / 0.0426 (15) | 0.8636 / 0.1071 (11) | 0.7500 / 0.2000 (4*) |
| 09 | gpt-4.1-mini | 0.9516 / 0.0706 (31) | 0.9444 / 0.0408 (18) | 0.9500 / 0.1481 (10) | 1.0000 / 0.0000 (3*) |
| 09 | llama | 0.8281 / 0.1163 (32) | 0.7647 / 0.0417 (17) | 0.9091 / 0.1786 (11) | 0.8750 / 0.3000 (4*) |
| 09 | mistral | 0.8333 / 0.1047 (33) | 0.8421 / 0.0612 (19) | 0.8636 / 0.1071 (11) | 0.6667 / 0.3333 (3*) |
| 10 | deepseek | 0.0517 / 0.8621 (29) | 0.0000 / 1.0000 (7*) | 0.0000 / 0.8571 (14) | 0.1875 / 0.7500 (8*) |
| 10 | gemini | −0.0156 / 0.9375 (32) | 0.0000 / 1.0000 (10) | −0.0714 / 0.9286 (14) | 0.0625 / 0.8750 (8*) |
| 10 | gpt-4.1-mini | 0.0323 / 0.9355 (31) | 0.0500 / 0.9000 (10) | 0.0000 / 1.0000 (13) | 0.0625 / 0.8750 (8*) |
| 10 | llama | 0.0323 / 0.8710 (31) | 0.0000 / 1.0000 (9*) | 0.0000 / 0.7857 (14) | 0.1250 / 0.8750 (8*) |
| 10 | mistral | −0.0333 / 0.8333 (30) | 0.1111 / 0.8889 (9*) | −0.1429 / 0.7143 (14) | 0.0000 / 1.0000 (7*) |

The judge-B split reproduces the pilot's headline finding at the divergence-cell level: cells shift under the judge swap (e.g. 03 gap collapses to ≈0 / negative under judge-B in every subset; 02 break-rate shifts materially), so **no within-SUT yes/partial/no ordering survives the judge change** and the cells remain judge-carried. Same reading rules (R1/R3/R4, insufficient-n flags) apply to this table.

---

## 8. Limitations

- **PROVISIONAL — tags pending owner ratification.** Nothing here is a headline until the F1 gate clears (see banner).
- **Cross-design calibration (R-tags §2).** `partial` thresholds are tagger-specific; only within-design, within-SUT cell contrasts are supported.
- **Insufficient-n is pervasive.** Every `yes` cell in every design is n < 10 (the sidecar keys only 29 `yes` items across 344, and they spread across 5 SUTs × designs). Most `partial` cells on 03/04/06/08 are also small. The split is a **structure check, not an estimation**; the flagged cells (`*`) print numbers that must not be read as rates.
- **Single-run stochastic decode (R11).** The pilot is one unreplicated decode per SUT; the split inherits that — no cell has a replication-based interval.
- **Judge-sensitivity (R4).** Every cell is judge-carried; §7 shows judge-B moves the cells. Both judge-A (§3) and judge-B (§7) splits are emitted; neither is authoritative.
- **Stratum-c quarantine.** Stratum (c) intra-corpus-dispute items are excluded from every cell (judge not G5-neutrality-certified in v2). The pilot logs carried stratum-c samples in designs 01 (2 units/SUT), 05 (9), 06 (7), and 08 (2); all were quarantined from the subsets. Design-06 ran stratum-a only for its headline scope; the 7 stratum-c units in the 06 log are quarantined here, consistent with §3.
- **06/09 additionally PROVISIONAL** — judge not G5-neutrality-certified (CF-2 quarantine), independent of the tag-ratification gate.

---

*Descriptive addendum on the parallel v2 harness; v1 remains canonical for release evidence. No per-item claims, no rankings, no SUT-vs-SUT comparisons. Tags PENDING OWNER REVIEW.*
