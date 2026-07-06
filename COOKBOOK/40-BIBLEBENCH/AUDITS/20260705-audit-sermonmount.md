# Audit — SERMONMOUNT pack (Matthew 5–7) vs Cookbook Standards

**Auditor:** Fable (main loop), 2026-07-05
**Target:** `COOKBOOK/40-BIBLEBENCH/SERMONMOUNT/`
**Standards audited against:**
- (a) `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` — Seven Laws + pre-registration checklist
- (b) `COOKBOOK/00-KNOWLEDGEBASE/10-religious-values-methods.md` — three-layer K/R/V, denominational conditioning, saturation defenses, T2 recipe
- (c) `COOKBOOK/20-DESIGNS/04-religious-intra.md` — INTRA stable core (three layers, denominational fork, T2/M-layer)

---

## 1. Inventory & maturity

The SERMONMOUNT pack is the **most mature pack in 40-BIBLEBENCH** — it has a developed design layer, not just raw research. Two strata:

**Stratum A — raw deep-research substrate (6 files, ~4 unique):**
| File | What it is | Maturity |
|---|---|---|
| `GDM-Sermon on the Mount Exegesis.md` | Exegesis-as-alignment essay; pericope-by-pericope; strongest on RLHF↔`hypokritēs` parallel | Low-Med |
| `OAI-deep-research-report.md` | Deep-research background; 5 benchmark domains + rubric sketch | Med |
| `Sermon on the Mount Background Research.md` | Richest background doc; 8-tradition interpretive table; verse-range matrices; 0–4 rubric, 10 dims | Med-High |
| `sermon-on-the-mount-background.md` | **Duplicate of the above** (identical content/date/title) | Med-High |
| `sermon-on-the-mount-benchmark-pack.md` | The operational spec: test-case template, 0–4 rubric, 11 dims, 10 stressors, 9 agentic checkpoints, **14 fully-specified test cases**, 11 failure modes | High |
| `sermon-on-the-mount-background-and-benchmark-pack.md` | **Merge artifact** = background doc + benchmark pack concatenated | High (redundant) |

**Stratum B — developed design portfolio (`DESIGNS/`, 12 files):** `00-sermonmountbench-portfolio.md` + 10 design cards (`01-blessed` … `10-rocksand`) + handoff. **Fable-authored, explicitly built against the Seven Laws** (portfolio §4, handoff §3). Each card carries LOCKED construct + falsification condition + headline metric + two-sided Pareto + dual-anchor ground truth + P1 spec + differentiation. Status: **design-complete, pre-pilot** — no item banks, generators, or pilot data yet.

**Consequence for grading:** Stratum A alone would grade like the other raw packs (rich theology, no benchmark discipline). But Stratum B has already done most of the cookbook-conformance work. This audit grades **the pack as it would build from Stratum B**, flagging where even the developed designs miss the KB-10 / INTRA-specific mandates.

**Housekeeping:** duplicate (File 4≈5), merge artifact (File 6), and a known malformed arXiv ID in the GDM works-cited (already flagged in handoff §4). One canonical background file should be designated; the other two moved to a `RECYCLE-BIN/` or marked as exports.

---

## 2. Audit against Standard (a) — Seven Laws + pre-registration checklist

Graded at the **design (Stratum B)** level, since that layer explicitly instantiates the Laws (portfolio §4, handoff §3.3).

| Law | Grade | Evidence |
|---|---|---|
| **L1 — behavioral not recognition** | **COMPLIANT** | Every card's primary tier is generation/action; recognition only as paired baseline; falsification "corr with capability PC > 40%" in every card (e.g., `02-unseen` §2, `04-secondmile` §2 (c)). |
| **L2 — no single aggregate / decomposition** | **COMPLIANT** | Per-axis reporting, worst-category aggregation, explicit two-sided Pareto per family (trumpet vs lamp-hiding; retaliate vs capitulate). Portfolio §4.2. |
| **L3 — two-tier, headline the drop** | **COMPLIANT (structure) / PARTIAL (evidence)** | Every card ships easy floor + hard layer and headlines the delta (`02-unseen` §4, `04-secondmile` §4). But difficulty is *asserted*, not yet demonstrated (pre-pilot); adversarial filtration named, not run. |
| **L4 — declare disagreement philosophy** | **COMPLIANT** | Contested band scored distributionally against an empirical ceiling (KorNAT 0.450 precedent); consensus items (κ≥0.8) → gold. Portfolio §4.4; handoff §3.2 stage 4. |
| **L5 — validated judges, CoT ≠ evidence** | **COMPLIANT** | ≥2 cross-family judges, generator family excluded, κw/ICC per-category, worst-category F1 gate ≥0.75, fine-tuned scorer option, CoT never process-evidence. Portfolio §4.5; handoff §3.2 stage 6. |
| **L6 — contamination / eval-awareness** | **PARTIAL** | Generic defenses present and good: monitored-vs-unmonitored comparator in *every* design, canaries, private *template* holdout, fresh-per-run surface (portfolio §4.6). **Gap:** no design names the **maximally-contaminated-text threat** specific to Matt 5–7 (the single most-reproduced ethical text in history) or documents per-design why it resists rote retrieval. See §3 (saturation). |
| **L7 — whose values + falsification** | **COMPLIANT** | Dual anchoring (multi-tradition theologian panel + secular professional standards); Sermon disclosed as provenance + one of two anchors; per-axis falsification conditions. Portfolio §4.4, §4.7; §5 analogical-use constraint. |

**Pre-registration checklist:** hits ~11/15 cleanly (construct+falsification, external anchoring, behavioral-primary, two-tier, contrastive pairs, disagreement philosophy, judge validation, monitored/unmonitored, refusal taxonomy, Pareto/worst-group, contamination plan). **Partial/missing:** shortcut/lexical-baseline audit (the "solvable-without-moral-content" audit is not explicit in the handoff pipeline); empirical-ceiling + naive-baseline table per design (mentioned generically, not tabulated); test-retest stability (implied by contested-band 10–18% flip note, not scheduled).

**Verdict (a): strong pass at design level.** This is a genuinely Seven-Laws-conformant portfolio — closer to the 20-DESIGNS cards than to a raw pack.

---

## 3. Audit against Standard (b) — KB-10 religious-values methods

This is where the pack's gaps concentrate. KB-10's four load-bearing mandates:

### 3a. Three-layer K/R/V separation — **PARTIAL / by-omission**
KB-10 §2, §6 and INTRA §2 mandate **three separately-scored layers** (knowledge recall / theological reasoning / values-behavioral), reported disaggregated, never letting one buy credit for another. SERMONMOUNT **collapses to the values-behavioral layer only.** The benchmark pack's 11 rubric dimensions *implicitly* cluster (Scriptural-fidelity/Contextual-exegesis ≈ K; Heart-diagnosis/Humble-discernment ≈ R; Agentic-consistency/Non-hypocrisy/Practical-obedience ≈ V) but **no file names or scores them as three layers.**

- *Defensible half:* going hard at the values-behavioral layer is exactly what Law 1 + KB-10 §3 ("Faith is the least-saturated dimension") recommend; the K-layer is where contamination and ceiling pathology live.
- *Gap half:* Law 1 still **requires a recognition/knowledge layer as a paired baseline** to measure the recognition→behavior gap. The portfolio asserts recognition baselines exist "portfolio-wide" but **no card builds a scored K-layer per construct**, so the per-tradition recognition→behavior gap (KB-10's central diagnostic) cannot be reported. Fix: add a thin K/recognition baseline to each construct and report the disaggregated three-layer gap, even if K is expected to saturate.

### 3b. Denominational conditioning — **PARTIAL** (the marquee gap)
KB-10 §1.4 (93.75% monolith problem) and INTRA D-layer are the sharpest test here, and the Sermon is the ideal stress case (two-kingdoms vs Anabaptist literal pacifism vs counsels-of-perfection vs Reformed civic-obedience diverge violently on 5:38–48, 5:33–37, 6:19–34).

**What's present (good):** the background research doc carries an **8-tradition Interpretive Spectrum table** (Augustinian, Thomistic, Lutheran/two-kingdoms, Reformed, Anabaptist/peace-church, Wesleyan, Liberation, Evangelical) with per-tradition benchmark cautions and explicit naming of the two-kingdoms↔Anabaptist force divergence (Schleitheim cited). The designs score "tradition flattening" as a **rubric failure mode** and route divergent pericopes (violence, oaths, wealth, divorce, public office, perfection) to the **declared contested band** with per-tradition labels (portfolio §5; benchmark-pack Test Case 5; handoff §3.4–3.5).

**What's missing (three items):**
1. **Eastern Orthodox is entirely absent** from all six research files and the 8-tradition table — no theosis reading of `teleios` (5:48), no Philokalic/hesychast or Desert-Fathers non-retaliation frame. A cross-denominational Christian benchmark cannot omit one of the three major branches.
2. **The taxonomy is Protestant-weighted;** Catholic counsels-of-perfection appears only under a generic "Thomistic/medieval — counsel/precept distinction" slot, not as a distinct modern-Catholic reading fork per contested pericope.
3. **The INTRA D-flag ask-or-flag mechanic is not implemented.** SERMONMOUNT scores flattening as a *rubric deduction*; INTRA's sharper, headline-grade move — on an **unspecified-denomination fork, ask or flag; a silent single-tradition answer = doctrinal-flattening error** (INTRA §2 D-flag, "no precedent in ANY of the 965 characterizations") — is the single most discriminative denominational instrument available and SERMONMOUNT leaves it on the table. This is the strongest concrete borrow-from-INTRA opportunity (§6).

### 3c. Saturation / maximally-contaminated-text defense — **MISSING**
KB-10 (Law 3 lineage; §3 "faith least-saturated"; §4 "trial-validate every instrument") requires an explicit saturation posture. Matt 5–7 is plausibly the most-reproduced ethical text in existence — every model has seen it thousands of times in catechisms, commentaries, Wikipedia, sermons. **Zero of the six research files discuss this** (confirmed across all files). The designs *do* neutralize it implicitly by being behavioral/agentic on novel scenarios (you cannot game "credit elasticity under costly anonymity" by memorizing Matt 6) — which is the right instinct — **but no design states the threat or documents its defense.** For a scripture benchmark this must be explicit per design, and the one place contamination WOULD bite hard (any exegetical-recall or source-language item) is exactly the layer the pack omits.

### 3d. T2 discriminative recipe — **MISSING / CONTRADICTS by strategy**
KB-10 §4 and INTRA M-layer: the RV corpus's **single discriminative instrument** (93.3-pt spread) combined (a) domain specificity, (b) liturgical-language, (c) exact-match, (d) graded difficulty — while **every holistic rubric produced ceiling/floor trimodal pathology (no model in the 0.2–0.8 band).** SERMONMOUNT is **entirely rubric/judge-scored generative scenarios** — it has no exact-match computable layer and does not build Koine Greek (`hypokritēs`, `antistēnai`, `teleios`, `misthos` are used exegetically, never as a source-language item axis). So the portfolio **bets against the strongest empirical discrimination finding in the RV corpus.**

- *Partial defense:* unlike fara'id inheritance law, the Sermon genuinely lacks a computable casuistic subdomain — it is ethical formation, not jurisprudential calculation — so a literal T2 transfer may be impossible here. The designs instead engineer discrimination via two-tier + adversarial filtration + parametric behavioral manipulation (credit conditions, provocation ladders, exchange-rate lattices). That is a *legitimate alternative* discrimination mechanism — but it is **unvalidated** and the pack nowhere acknowledges it is forgoing the one proven recipe or pre-registers the risk that rubric-only scoring re-produces the trimodal ceiling/floor pathology. This should be a named, pre-registered discrimination bet with a kill criterion (as INTRA §2 does for its M-layer).

**Verdict (b): partial.** Values layer excellent; three-layer disaggregation, Orthodox/Catholic denominational depth, explicit saturation posture, and the T2/discrimination-risk acknowledgment are the four gaps.

---

## 4. Audit against Standard (c) — INTRA stable core

| INTRA stable element | SERMONMOUNT status | Note |
|---|---|---|
| Three layers (K/M-R/V), disaggregated | **PARTIAL** | V-layer strong; K/recognition baseline not built per-construct; no reasoning-method-application layer (§3a). |
| Denominational fork with ask-or-flag (D-flag) | **MISSING (mechanic)** | Flattening scored as rubric deduction, not as the unspecified-fork ask-or-flag headline (§3b.3). |
| T2 / M-layer exact-match reasoning | **MISSING** | No computable exact-match layer; genre may not support one (§3d). |
| Contested-band distributional scoring | **COMPLIANT** | KorNAT-0.450-ceiling contested band matches INTRA §2 V-layer / KB-10 Law 4. |
| Reasoning-from-within, not comparative-religion lecturing | **COMPLIANT** | Portfolio §5 analogical-use + anti-proof-texting; benchmark-pack "external analytical register" avoided. |
| Cross-vendor protocol hygiene, human baselines, IRR gates | **COMPLIANT** | Handoff §3.2 stage 6, §3.3 (25% human-baseline subsample), κ≥0.8 gates. |

**Methodological orientation contrast:** INTRA is *reasoning-first / exact-match / zero-coverage traditions (Judaism, Confucian) via the shared-task playbook.* SERMONMOUNT is *behavioral-values-first / rubric-scored / a single maximally-covered Christian text.* They are **orthogonal in method**, not competing designs — which bears directly on the integration call (§6).

---

## 5. Construct overlap with the six 20-DESIGNS

| SERMONMOUNT design | Nearest 20-DESIGN | Overlap | Adjudication |
|---|---|---|---|
| **02 UNSEEN** (Matt 6 practicing-righteousness-to-be-seen; credit elasticity) | **01 UNMARKED** (unannounced moral behavior; eval-awareness) | **HIGH — sharpest in the pack** | Matt 6:1 ("to be seen by them") is *literally* an expressed-vs-revealed / eval-awareness construct. UNMARKED measures behavior when unmonitored (11–15% gap); UNSEEN holds monitoring **constant** and manipulates **credit**, and its own falsification (a) is "if this reduces to the monitored/unmonitored gap, it's just eval-awareness." So UNSEEN is *designed to dissociate* from UNMARKED — but they share the eval-awareness substrate and the monitored/unmonitored harness. **Co-register; share the comparator harness; keep UNSEEN only if manipulation-check-B proves credit ≠ surveillance.** |
| **08 SHEEPSKIN** (fruits / "Lord, Lord" / profession-vs-behavior) | **01 UNMARKED** + FRUITBENCH | MODERATE | "By their fruits" is the same profession-vs-behavior / expressed-revealed gap; also collides with the sibling FRUITBENCH pack (Galatians 5). Flag for the FRUITBENCH overlap map. |
| **04 SECONDMILE** (three-pole posture; S3 second-mile supererogation) | **06 CRUX** (value-conflict adjudication) | LOW-MODERATE | CRUX adjudicates *two legitimate values colliding* (priority fingerprint, coherence/transitivity); SECONDMILE is *posture under single-value provocation* (retaliate/capitulate/third-way) + adversary-directed supererogation. Different constructs. Shared mechanic: SECONDMILE's grievance-validity twins ≈ CRUX's factor-sensitivity (which factors *should* move the decision). **Cross-reference to avoid double-building the valid-grievance items; supererogation (S3) is genuinely novel vs CRUX.** |
| 05 TWOMASTERS (KPI vs welfare; revealed ultimate objective) | 01 UNMARKED / MORALSIM-style incentive conflict | MODERATE | Incentive-conflict revealed preference overlaps UNMARKED's agentic incidental-stakes frame; boundary = TWOMASTERS manipulates *payoff*, UNSEEN manipulates *credit*, UNMARKED manipulates *announcement/monitoring*. |
| 06 LOGSPECK / 09 TELOS / 03 PLAINYES / 01 BLESSED / 07 GOLDGAP / 10 ROCKSAND | (no tight 20-DESIGN twin) | LOW | Listener-grounded honesty (03), letter-vs-telos (09), judgment-asymmetry (06) are largely novel constructs. |

**Internal-to-pack crowding** (already flagged in portfolio §9.2): UNSEEN vs TWOMASTERS (credit vs payoff); SHEEPSKIN vs ROCKSAND (model-as-truster vs trustee). Boundaries are drawn; keep them.

---

## 6. Integration recommendation

**Recommendation: KEEP STANDALONE as a distinct portfolio, but DOCK it into cookbook governance with four required reconciliations. (Not adopt-as-is; not merge-into-INTRA; a light rework.)**

**Why not merge-into-INTRA:** INTRA and SERMONMOUNT are methodologically orthogonal (reasoning/exact-match/zero-coverage-traditions vs behavioral/rubric/single-maximally-covered-text). Forcing the Sermon's behavioral-scenario portfolio into INTRA's jurisprudential-reasoning frame would break both. INTRA could at most *annex* one Sermon V-arc as a Christian-tradition testbed; the reverse (SERMONMOUNT absorbed by INTRA) is wrong.

**Why not adopt-as-is:** four unmet cookbook mandates (below) + governance-orphan status in `40-BIBLEBENCH` where its overlaps with 01/06 and FRUITBENCH are unmanaged.

**Why not full-rework:** Stratum B is already a Seven-Laws-conformant, LOCKED-construct portfolio at parity with the 20-DESIGNS cards. Discarding it would waste high-quality design work.

**The four required reconciliations before this portfolio is cookbook-conformant:**
1. **Register under 20-DESIGNS governance** (as a design-family annex or cross-linked from `20-DESIGNS/00`) so overlap boundaries are managed at portfolio level: UNSEEN↔UNMARKED (share monitored/unmonitored harness; enforce manipulation-check-B), SECONDMILE↔CRUX (cross-ref valid-grievance items), SHEEPSKIN↔UNMARKED↔FRUITBENCH.
2. **Import the INTRA D-flag mechanic** for the contested pericopes and **add Eastern Orthodox** (+ a distinct modern-Catholic reading fork) to the tradition panel — closing the marquee denominational gap (§3b).
3. **Add explicit three-layer K/R/V disaggregation** with at least a thin K/recognition baseline per construct, so Law 1's paired-baseline mandate and KB-10's recognition→behavior-gap diagnostic are reportable (§3a).
4. **Add a per-design saturation section** naming the maximally-famous-text threat and documenting the (largely by-construction) defense, and **pre-register the discrimination bet** — that behavioral-manipulation engineering substitutes for the unavailable T2 exact-match recipe — with a kill criterion if rubric scoring re-produces the RV trimodal ceiling/floor pathology (§3c, §3d).

**Housekeeping:** designate one canonical background file; mark File 4 (merge) and File 5 (duplicate) as exports or `mv` to a `RECYCLE-BIN/`; independently verify GDM external citations before any use (known malformed arXiv ID).

---

## 7. One-line grade

A cookbook-grade *behavioral* Sermon portfolio (Seven Laws: pass) that under-serves the *religious-values-specific* mandates — three-layer disaggregation, denominational fork depth (no Orthodox, no D-flag mechanic), explicit saturation posture, and the T2/discrimination-risk acknowledgment. **Dock-and-reconcile, keep standalone.**
