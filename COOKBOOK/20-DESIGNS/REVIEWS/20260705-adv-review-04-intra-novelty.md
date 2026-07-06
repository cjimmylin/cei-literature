# Adversarial Novelty Review — Design 04 INTRA (Intra-Tradition Reasoning)

> Refute-first review. Artifact: `COOKBOOK/20-DESIGNS/04-religious-intra.md`.
> Reviewer stance: assume the design overclaims novelty until evidence forces otherwise.
> Corpus: 965 characterizations / 737 distinct (RV 401 primary; Cultural 218; MoralPsych 292; NormEval 54).
> Date: 2026-07-05. Model: Opus (adversarial-reviewer tier).

## Bottom line

The **composite** novelty bundle survives refutation: no single existing benchmark combines
(reasoning-first M-layer) × (multi-tradition) × (denominational forks with **ask-or-flag** gold
scoring) × (in-tradition population norms) × (board-authored psychometric V-rubrics). But three of
the novelty statement's **universal** claims ("no instrument is reasoning-first", "the D-layer has no
precedent in ANY of the 965", implicitly-original Islamic M-layer) are overstated once you decompose
the bundle into components — each component has a near neighbor. The fixes are positioning/citation,
not redesign. **PASS-WITH-FIXES.**

Evidence base (queried, not recomputed): the RV v2 matrix carries a scored `R4_denominational`
feature — **only 7/401 entries score >0 (max=2); 394 score 0**. That is the machine-level confirmation
of the digest's "93.75% treat traditions as monoliths" (copied verbatim, not recomputed) and is the
single strongest support for the design. But those same 7 records are the near neighbors that puncture
the *universal* framing.

---

## Ranked defects

### MAJOR-1 — "no instrument is reasoning-first" is false at the component level
§1 and §8 assert "no instrument is reasoning-first (27.7% touch reasoning at all)." The 27.7% is a
correct verbatim digest corpus-stat. But *reasoning-first* as a **design property** is NOT
unprecedented within a single tradition. The RV matrix contains multiple reasoning-first instruments:
- **QIAS 2025 — Shared Task on Islamic Inheritance Reasoning & Knowledge Assessment** (2025): "designed
  for the evaluation of LLMs in the complex domains of religious and legal *reasoning*."
- **Assessing LLMs on Islamic inheritance / 'ilm al-mawārīth** (2025): "evaluates the knowledge **and
  reasoning** capabilities … 1,000 MCQs … diverse inheritance scenarios."
- **Benchmarking the Legal Reasoning of LLMs** (2025, Islamic inheritance).
- **BuddhismEval** (2025, gate-passing, R2_depth=3): "factual, ethical, philosophical, and **applied
  reasoning** questions" — i.e. it already separates a K/M/V-like layer stack.

**Fix (minimal):** narrow the claim to "no *multi-tradition, denominationally-resolved* instrument is
reasoning-first; single-tradition reasoning instruments exist (QIAS 2025, BuddhismEval) but do not
generalize the recipe or condition on school." Keep the 27.7% corpus stat as-is.

### MAJOR-2 — "The D-layer … has no precedent in ANY of the 965" conflates two different things
The claim bundles (a) *denominational conditioning as a property* with (b) the specific *ask-or-flag
fork scoring where school membership changes the gold answer*. (a) has clear precedent: **7 RV
benchmarks score `R4_denominational`>0** — Gospel Coalition (Nicene-Creed orthodoxy conditioning),
CatholicBench, BuddhismEval, FiqhQA, "Religious Bias Benchmarks for ChatGPT" (R4=2, the max). Cross-
corpus, MoralPsych records **FiqhQA referencing the "Hanafi school of thought"** and **BuddhismEval
referencing "Theravada."** So denominational *awareness* is not novel. What I could **not** find any
precedent for — after sweeping RV, Cultural (218), and MoralPsych (292) — is the **ask-or-flag scoring
mechanic** (silent single-school answer to an unspecified-school fork = "doctrinal flattening error").
That mechanic is genuinely novel; the sentence is not.

**Fix:** rewrite to "No characterized benchmark scores the *gold answer* on school membership or
penalizes silent single-school flattening (ask-or-flag). Denominational awareness as a feature is
weakly present (7/401 score `R4_denominational`>0, max 2), but never operationalized as a fork metric."

### MAJOR-3 — the Islamic M-layer is heavily pre-empted; QIAS 2025 must be named
The design's M-layer is "the T2 recipe generalized" and cites the fara'id frontier instrument only as
"T2"/anonymous. That instrument is **QIAS 2025** (ArabicNLP/EMNLP 2025 shared task), and the Islamic-
inheritance niche is crowded: at least **four** corpus benchmarks (QIAS 2025; Assessing LLMs on Islamic
inheritance; Benchmarking the Legal Reasoning of LLMs; plus fatwa sets FatwaSet, Hajj-FQA, Aftina).
INTRA's Islam M-subdomain is therefore replication of a solved problem, not contribution — which is fine
(Islam is explicitly the "mature infrastructure" control in P1), but the design must **cite QIAS 2025 by
name**, credit it as the template for the shared-task playbook it invokes, and state plainly that Islam
contributes *method transfer*, not a new M instrument. Not doing so reads as reinventing an EMNLP-2025
shared task. (Note: QIAS is characterized `passes_gates=False` in the matrix — a data-gate/availability
fail, not a quality fail — so citing it does not undercut the "45 gate-passers" landscape framing.)

### MINOR-1 — V-layer "reasoning-from-within / pastoral advisory" overlaps CatholicBench
**CatholicBench** (2025, gate-passing) already measures "**Pastoral Charity** (empathy with truth)"
across Moral Theology, Bioethics, Sacraments, Canon Law — i.e. the V-layer's "reasoning-from-within,
not comparative-religion lecturing" and INTRA's Catholic M-subdomain ("canon-law marriage impediments
and dispensation logic"). Cite it as the nearest single-tradition analog and differentiate on
multi-turn advisory arcs + norms + cross-family judge.

### MINOR-2 — governance/board novelty is partly pre-empted
The tradition-board authoring model is presented as "the differentiating half." **Gospel Coalition**
(seven orthodox theologians grade LLMs; R6_grounding=4, the matrix max) and **CatholicBench** already
use in-tradition expert authorship/grading. INTRA's differentiator is *veto power + school-label
ownership + disclosed positionality + honoraria + multi-tradition*, not board authorship per se. Sharpen
the wording so the claim is the governance *protocol*, not "experts author items" (which exists).

### MINOR-3 — "population norms" and "adapted validated psychometric structure" firsts
These two ("first in-tradition population norms"; "first adapted validated psychometric structure") are
the **most defensible** claims — RV CI axis is at floor and Cultural digest reports **0/218 measurement
invariance** (copied). Strengthen by citing those two stats inline as the empirical basis, and scope the
psychometric claim to *religious* benchmarks (MoralPsych does apply validated instruments — Schwartz/MFQ
— just not to religious traditions), so a reviewer cannot counter with the moral-psych corpus.

---

## Nearest-neighbor benchmarks

| # | Benchmark (corpus) | INTRA components already covered | What it lacks |
|---|---|---|---|
| 1 | **QIAS 2025 — Islamic Inheritance Reasoning & Knowledge Assessment** (RV; shared task, EMNLP-2025) | K + M (reasoning-first, exact-match fara'id/legal reasoning); IS a community shared task — the exact playbook INTRA invokes | Multi-tradition; denominational forks; ask-or-flag; population norms; V-layer advisory |
| 2 | **CatholicBench** (RV; gate-pass, R2d3, R4=1) | Canon-law/moral-theology reasoning = INTRA's Catholic M-subdomain; **Pastoral Charity** = V-layer reasoning-from-within; denominationally scoped; bias/historical-accuracy | Cross-tradition; ask-or-flag school forks; norms; psychometric structure |
| 3 | **BuddhismEval** (RV; gate-pass, R2d3, R4=1) | Reasoning-first with factual/ethical/philosophical/applied **layer separation** (K/M/V analog); bilingual (language axis); Theravada reference | Denominational **forks** (Theravada vs Mahayana as gold); norms; boards; ask-or-flag |
| 4 | **The Gospel Coalition AI Christian Benchmark** (RV; gate-pass, R2d3, R6=4) | **Board governance** (7 theologians author/grade); Nicene-Creed doctrinal conditioning; values-relevant Q&A | Multi-tradition; exact-match method layer; ask-or-flag; norms |
| 5 | **FiqhQA — "Sacred or Synthetic?"** (RV, R4=1; MoralPsych flags "Hanafi") | Fiqh (jurisprudential method) Q&A; **abstention/reliability** ≈ INTRA's epistemic-integrity/ask-or-flag intuition; Hanafi school reference | Fork items where school changes the gold answer; multi-tradition; norms |

*Runner-up:* "Religious Bias Benchmarks for ChatGPT" (2024) holds the single **highest** denominational
score in the corpus (`R4_denominational`=2) — bias varying by religious belief — but is descriptive-bias,
not reasoning/forks.

## Refutation attempts and [beyond-corpus] probes
- **Tried:** "the D-layer gap is empty." *Partly refuted* — denominational awareness is scored on 7
  records; only the ask-or-flag fork *mechanic* is empty. → MAJOR-2.
- **Tried:** "reasoning-first is unprecedented." *Refuted* at component level (QIAS, BuddhismEval,
  ≥3 inheritance benchmarks). Survives only in the multi-tradition qualifier. → MAJOR-1.
- **Tried:** "shared-task playbook to zero-coverage traditions is unprecedented." *Survives* — QIAS is a
  shared task but for a *covered* tradition (Islam); deliberately porting it to zero-coverage traditions
  (Judaism/Confucian) has no precedent found.
- **[beyond-corpus]** (Jan-2026 cutoff, low confidence): single-tradition fiqh/halakha/responsa QA sets
  and Sefaria-derived Jewish NLP datasets exist, and Arabic knowledge suites (ArabicMMLU/AraMMLu) test
  Islamic knowledge — but I am not aware of any published **multi-tradition, denominationally-forked
  reasoning benchmark with ask-or-flag gold scoring**. The niche appears genuinely open. Residual risk:
  a 2025–2026 Jewish-law (halakha) reasoning benchmark analogous to QIAS could exist outside the
  English-only RV external search (RV caveat: 401 is a lower bound) and would pre-empt the Judaism M-layer.

---

**VERDICT: PASS-WITH-FIXES**

Most likely remaining error: an uncharacterized 2025–2026 **halakhic/Jewish-law reasoning benchmark**
(the RV search was English-only; Judaism shows 0 gate-passers but that may be a coverage artifact, not a
true void) pre-empting INTRA's flagship P1 "critical-gap" Judaism M-layer — which would downgrade the
Judaism contribution from "first" to "second," the same way QIAS already pre-empts the Islam M-layer.
