# Cookbook-Integration Audit — TENCOMMANDMENTS pack

**Auditor:** cookbook-integration auditor (Fable main loop)
**Date:** 2026-07-05
**Target:** `COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS/`
**Standards audited against:**
`00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws + pre-reg checklist);
`00-KNOWLEDGEBASE/10-religious-values-methods.md` (K/R/V three-layer, denominational conditioning, saturation, T2 recipe);
`20-DESIGNS/04-religious-intra.md` (INTRA stable core: layers, denominational fork, T2/M-layer).

---

## 1. Inventory & maturity

The pack has **two distinct maturity layers** — it is NOT a raw-research-only pack.

**Layer A — raw + synthesized source corpus (top level):**

| File | Type | Maturity |
|---|---|---|
| `GDM-Ten Commandments AI Ethics Benchmark.md` (219 ln) | External deep-research report (Google DeepMind) | Raw research; academic format, 90 refs; introduces "Flip-Rate" |
| `OAI-deep-research-report.md` (56 ln) | External deep-research report (OpenAI, run 1) | Raw research; dense; DeRouchie three-scheme numbering |
| `OAI2-deep-research-report.md` (60 ln) | External deep-research report (OpenAI, run 2) | Raw research; WLC Q.99 emphasis |
| `ten-commandments-background.md` (328 ln) | Fable-synthesized background | Mature; exegesis + historical theology + contested-application notes |
| `ten-commandments-background-and-benchmark.md` (1115 ln) | Fable-synthesized combined | Mature; = background + full 12-case scripted benchmark |
| `ten-commandments-benchmark-design.md` (322 ln) | Fable-synthesized design | Mature; 10-dim 0–4 rubric, 10 scenario families, 12 seed cases, acceptance criteria |

**Layer B — Fable-authored cookbook-conformant portfolio (`DESIGNS/`):**

`00-10cbench-portfolio.md` (143 ln) + eight per-commandment briefs `01`–`08` (116–125 ln each).
**Missing: `09-witness-no-false-witness.md` and `10-appetite-no-coveting.md`** — 2 of 10 briefs absent,
including WITNESS, which the portfolio's own build order (§8) names as build **#1** (cheapest bank, crisp
defamation anchors). Status line: "Design-complete scaffolds; awaiting Opus flesh-out (item banks,
generator scripts, pilot infrastructure)." **Nothing is built or piloted** — no item banks, no generator
code, no empirical discrimination evidence; every discrimination gate is stated as a *target*, not met.

**Verdict on maturity:** This is the **most cookbook-integrated of the BIBLEBENCH packs.** Layer B was
authored the same day (2026-07-05) with the Seven Laws in hand and explicitly instantiates them. The
audit therefore grades the *actual design layer*, not a hypothetical benchmark-from-raw-reports — with
the caveat that the design is pre-pilot, so all discrimination/validity claims are unverified.

---

## 2. Audit against `01-benchmark-design-best-practices.md` (Seven Laws + pre-reg)

| Dimension | Grade | Evidence |
|---|---|---|
| **Law 1 — recognition ≠ propensity** | **COMPLIANT** | Portfolio §3.1: behavioral/action is every design's primary tier; MCQ recognition twins exist ONLY to measure the recognition–propensity gap (cites coeff 0.015, 52-pt precedent). Per-brief: NAMEDROP's "can't-verify vs won't-resist" split (r<0.4 discriminant criterion) is textbook. |
| **Law 2 — no single aggregate; Pareto** | **COMPLIANT** | §3.2: per-axis reporting; a two-sided Pareto per design (complicity/moralizing, rigidity/exploitation, calumny/cover-up…). §5 prohibits "any single aggregate score in reporting code." |
| **Law 3 — saturation / two-tier / headroom** | **COMPLIANT (strong)** | §4: continuous dose surfaces "never pass/fail"; adversarial filtration at construction; **discrimination gate as a shipping criterion** (≥20-pt spread, cap-PC1 <40%, hard−easy ≥15pt). Rich multi-turn/agentic headroom generators. |
| **Law 4 — ground truth / disagreement declared** | **COMPLIANT / PARTIAL** | §3.4 dual-panel (theologian + secular); contested band scored distributionally with empirical ceiling (0.450 precedent). PARTIAL: no per-annotator psychometrics; pre-pilot so no IRR numbers yet. |
| **Law 5 — validated judges; CoT not evidence** | **COMPLIANT (as designed)** | §3.5: ≥2 cross-family judges, never the item-generating family (self-preference 10–19%); fine-tuned scorer on own labels; κw per dimension; neutrality meta-eval. Not yet executed. |
| **Law 6 — contamination / eval-awareness** | **COMPLIANT (design layer)** | §3.6, §5: public generator spec + private fresh-per-run realizations + canaries + rolling holdout + monitored/unmonitored 20% twin. SOVEREIGN/APPETITE contamination-resistant by construction. **This FIXES the raw sources' silence (see §3 below).** |
| **Law 7 — WHAT values and WHOSE** | **COMPLIANT (exemplary)** | Dual-anchor per item (Decalogue provenance + named secular clause: mens-rea, defamation, labor law, duty-of-care). Numbering declared once in methods; **prompts cite textual clauses, never commandment numbers** — unusual construct care. |
| **Pre-registration checklist** | **PARTIAL** | Most 15 items covered in portfolio prose (behavioral-primary, two-tier, refusal taxonomy, contamination plan, cap-correlation stat). NOT produced as a per-design checklist artifact; human baseline, test-retest, per-category IRR all pending pilot. **Missing checklist items: multiturn is present, but language axis and annotator-level release are absent (see §3).** |

**Seven-Laws summary: COMPLIANT across the board** — the strongest general-design conformance of any
BIBLEBENCH pack. Gaps are pre-pilot-execution items, not design defects.

---

## 3. Audit against `10-religious-values-methods.md` (religious-values-specific levers)

This is where the pack is weaker — it excels at *general* benchmark design but is PARTIAL/MISSING on the
levers doc 10 and INTRA treat as the differentiators for *religious-values* work.

| Dimension | Grade | Evidence & reasoning |
|---|---|---|
| **K / R / V three-layer separation** | **PARTIAL** | Knowledge(MCQ) vs behavioral(generation/action) is cleanly separated and scored (Law 1). But doc 10 §2's **middle "theological reasoning" layer — tradition-internal *method* applied to novel scenarios — is not a distinct scored layer.** It is folded into the values-behavioral rubric dimensions ("theological order," "command integration," act/motive/means/end). UPSTREAM's mens-rea ladder is the nearest thing to a scored reasoning layer. Legitimate for a behavioral benchmark, but diverges from the three-layer ideal. |
| **Denominational conditioning** | **PARTIAL** | Handled **defensively**, three ways: (i) tradition-awareness rubric dimension (EFFIGY, SOVEREIGN); (ii) explicit exclusion of contested applications from the scored core (FALLOW excludes Sabbath day/mode; UPSTREAM excludes just-war/capital-punishment); (iii) distributional "licensed-either-way" bands (GRAVITAS, TRIAD). Plus the portfolio-wide **Case-12 guard** (don't penalize *or* reward one tradition's application when tradition is unspecified; score defamation as failure). **What's missing vs INTRA's D-layer:** no *scored ask-or-flag fork* where declared school membership *changes the correct answer*, and no "doctrinal-flattening error" metric. Critically, **the Decalogue's NUMBERING difference — the natural denominational-conditioning fork the cookbook flags (Catholic/Lutheran/Augustinian vs Reformed/Orthodox/Jewish) — is used only defensively (kept out of prompts; tested for awareness in Case 12), never operationalized as a discriminative scored fork.** The raw sources cover numbering thoroughly (GDM, OAI DeRouchie summary, background §3) but the design converts it into a contamination-avoidance rule, not a conditioning probe. |
| **Saturation defense on maximally-contaminated text** | **COMPLIANT-with-risk** | The Decalogue is among the most-memorized texts in existence; the **raw sources are entirely silent on contamination/saturation** (agent-confirmed gap). The design layer (§4–5) fixes this with fresh-per-run procedural realization, canaries, private holdout. RISK: discrimination rests on *rubric-scored* dose curves — the exact instrument class the RV meta-eval found produces trimodal ceiling/floor pathology (no model in the 0.2–0.8 band). The portfolio's mitigation ("slopes can't saturate") is plausible but **unproven pre-pilot.** |
| **T2 discriminative recipe** | **MISSING / PARTIAL** | doc 10 §4: the one instrument that discriminated at the frontier (93.3-pt spread) combined domain-specific **computable subdomain + liturgical language + exact-match verifiable + graded difficulty**. **The pack has NO exact-match computable layer.** Discrimination is entirely rubric-scored continuous surfaces. UPSTREAM's mens-rea ladder vs legal gold is the only near-exact-match anchor. Partly inherent — applied Decalogue ethics lacks a `fara'id`-style computable subdomain — but the biblical legal corpus *does* grade culpability (murder/manslaughter/negligence; refuge cities; two-witness rules; reciprocal false-witness penalties), which UPSTREAM/WITNESS could mine into an exact-match tier. **Top methodological gap.** |
| **Language as a measured variable (≥2 languages/scripts)** | **MISSING** | doc 10 §6 and INTRA §3 mandate ≥2 languages/scripts per item with per-language bias-direction reporting. **The entire pack is English-only.** The Decalogue has an obvious source-language axis (Hebrew, Exod 20 / Deut 5) plus vernacular — completely unused. No liturgical-language presentation, no per-language consistency metric. Clear MISSING dimension. |

---

## 4. Audit against INTRA stable core (`20-DESIGNS/04`)

| INTRA stable-core element | 10CBench grade | Note |
|---|---|---|
| Three (four) never-aggregated layers (K/M/D/V) | **PARTIAL** | 10CBench has K + behavioral(V-ish); no distinct M (method) layer, no D as a scored layer. |
| Denominational fork with ask-or-flag scoring | **PARTIAL/MISSING** | INTRA scores silent single-school answers as doctrinal-flattening errors and rewards fork-flagging. 10CBench only guards against penalizing/defaming (Case 12); no scored fork. |
| T2 / M-layer exact-match method application | **MISSING** | No exact-match anchor (see §3). |
| Cross-vendor protocol hygiene, four-way refusal, per-slice disaggregation | **COMPLIANT** | Portfolio §3.5–3.6 + refusal taxonomy match INTRA §4–5 well. |

**Net:** 10CBench and INTRA occupy the **same religious-values niche via orthogonal methods.** INTRA =
cross-tradition, reasoning-first, D-layer forks + T2 M-layer, "with the traditions, not about them."
10CBench = single-tradition (Christian), behavioral-first, dose-response continuous surfaces, dual-track
secular/confessional. They are complementary, not redundant — but their denominational and discrimination
machinery should be reconciled (INTRA is stronger on both; 10CBench is stronger on agentic behavior and
the secular Track-A framing).

---

## 5. Construct overlap with the six 20-DESIGNS

Portfolio §6 ran an overlap check against UNMARKED, FRAMESHIFT, DUPLEX, INTRA, CULTIVATE, CRUX + sketches
S1–S8. Sound differentiations: CULTIVATE↔GRAVITAS (breadth vs depth), S1 DRIFT↔FALLOW (stability vs
cessation), S2 BACKBONE↔TRIAD (present vs absent stakeholder), S8 LEVER↔APPETITE, UNMARKED↔PROVENANCE.
**Two overlaps are under-handled:**

- **CRUX (conflict-of-commandments).** SOVEREIGN is cleanly differentiated from CRUX (apex-recovery vs
  pairwise adjudication). BUT the portfolio's **"Mixed-command conflict" scenario family** and the
  **"competing duties" evaluation pattern** are squarely CRUX's value-priority construct. Needs an explicit
  routing rule: CRUX owns cross-clause priority conflicts; 10CBench owns within-clause behavioral fidelity.
- **FRAMESHIFT (deontology conditioning) — NOT addressed in §6.** GRAVITAS (non-contractual duty),
  UPSTREAM (mens-rea/culpability), and the portfolio-wide "theological order" + "act/motive/means/end"
  rubric are strongly **deontological duty-reasoning** — the FRAMESHIFT construct. The overlap map omits
  FRAMESHIFT entirely. **Flag for de-confliction** before either goes to build.

---

## 6. Integration recommendation

**KEEP-STANDALONE, with bounded cookbook reconciliation** (a targeted rework of ~4 dimensions — NOT
adopt-as-is, NOT merge-into-INTRA, NOT full rework).

**Why not the other options:**
- *Adopt-as-is* — no: 2 flagship briefs missing (incl. build-#1 WITNESS), FRAMESHIFT/CRUX overlaps
  unreconciled, nothing piloted, and the religious-values-specific levers (§3) are PARTIAL/MISSING.
- *Merge-into-INTRA* — no: would destroy 10CBench's two genuine contributions (the **Track-A secular
  behavioral construct** and the **10-design agentic breadth**), which are orthogonal to INTRA's
  reasoning-first D/M-layer method. Different construct, different venue strategy.
- *Full rework* — no: the Seven-Laws layer is already exemplary; reworking from scratch would discard
  the most cookbook-native design in the BIBLEBENCH corpus.

**Required before build (reconciliation punch-list):**
1. **Import INTRA's D-layer + add a language axis** (closes §3's two weakest dimensions): operationalize
   the numbering / images / Sabbath-mode differences as *scored ask-or-flag denominational forks* (silent
   single-tradition answer = flattening error); present each item in a source-language (Hebrew) + vernacular
   pair with per-language reporting.
2. **Add ≥1 exact-match T2-style discriminative anchor** to hedge the rubric-saturation risk: build
   UPSTREAM's mens-rea calibration ladder (and/or WITNESS's two-witness / verified-vs-unverified layer) as
   an exact-match ordinal tier vs legal gold, mining the biblical legal corpus's own graded culpability.
3. **Complete the portfolio + de-conflict:** write briefs `09-WITNESS` and `10-APPETITE`; add explicit
   routing rules for CRUX (mixed-command conflict) and FRAMESHIFT (deontology conditioning).
4. **Establish an explicit INTRA interface** (cross-reference, don't merge): 10CBench's theologian panels
   and Track-B confessional packs supply **INTRA's Christianity tradition board / Catholicism-expansion
   module**; INTRA imports 10CBench's agentic dose-response harness for its V-layer.

**Bottom line:** an unusually mature, Seven-Laws-native portfolio whose weaknesses are precisely the
religious-values-specific levers (three-layer separation, denominational forks, T2 exact-match, language
axis). Keep it as its own program; reconcile the four items above with the cookbook + INTRA before Opus
builds any item bank.
