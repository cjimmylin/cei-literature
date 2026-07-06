# Audit — SOLABENCH pack

> **CEI COOKBOOK · 40-BIBLEBENCH/AUDITS.** Auditor pass, 2026-07-05.
> Scope: `COOKBOOK/40-BIBLEBENCH/SOLABENCH/`. Standards audited against:
> `00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` (Seven Laws + pre-reg checklist),
> `00-KNOWLEDGEBASE/10-religious-values-methods.md` (three-layer K/R/V separation, denominational
> conditioning, saturation defenses, T2 recipe), `20-DESIGNS/04-religious-intra.md` (INTRA stable core:
> three layers, denominational fork, T2 recipe).

---

## 0. Bottom line

**SOLABENCH is an empty directory — zero files, zero bytes.** There is no research pack to audit.
It is one of three stubs (`SOLABENCH`, `ARMOURBENCH`, `WESTMINSTER`) created 2026-07-05 14:58–14:59
as placeholders alongside the four populated packs and never filled. Maturity = **empty stub /
placeholder**. Integration verdict = **defer (too thin — in fact non-existent)**, with a strong
secondary recommendation to **fold the eventual construct into INTRA rather than build it standalone**
(the five solas are natively a denominational-fork construct — exactly INTRA's D-layer).

This memo therefore does two things the task allows for a raw/absent pack: (1) records the inventory
fact plainly and does not pad, and (2) grades what a *faithful* SOLABENCH built from the five-solas
construct would look like against the standards, so the eventual pack (or its INTRA merge) starts with
the gaps already mapped.

---

## 1. Inventory

| Item | Finding |
|---|---|
| Path | `COOKBOOK/40-BIBLEBENCH/SOLABENCH/` |
| Files | none (directory size 64 B = empty; no hidden files; not in git history) |
| Deep-research reports (OAI / GDM) | none |
| Background dossier | none |
| Benchmark spec / design | none |
| Maturity | **empty placeholder** (created 14:59, never populated) |

**Comparison to the four original packs** (all populated 15:39–18:23 on 2026-07-05):
`FRUITBENCH` (9 files incl. GDM×2 + OAI×2 + background + benchmark-pack + DESIGNS/), `CORINTHLOVE`
(5 files), `SERMONMOUNT`, `TENCOMMANDMENTS` — each carries the paired-vendor deep-research reports
plus a synthesized background/benchmark pack. SOLABENCH has none of this. The two other 14:5x stubs
(`ARMOURBENCH`, `WESTMINSTER`) are likewise empty; SOLABENCH is not an anomaly but part of an
unfilled second wave.

Because the pack is absent, every "COMPLIANT/PARTIAL/MISSING" grade below is necessarily **MISSING —
nothing exists to satisfy the standard**. The value of the section is the *forward-looking* column:
what the construct specifically demands and where it is likely to fail, so the work isn't re-derived.

---

## 2. Construct note (why this pack is special)

The other 40-BIBLEBENCH packs are **single scripture passages** (Galatians 5, 1 Cor 13, Sermon on the
Mount, Decalogue). SOLABENCH is presumptively the **Five Solas of the Reformation** (*sola scriptura,
sola fide, sola gratia, solus Christus, soli Deo gloria*) — i.e. **confessional/doctrinal material,
not a passage**. This matters for the audit in one decisive way:

> The five solas are *definitionally* an inter-confessional divergence marker. "Sola scriptura" vs.
> "Scripture + Tradition + Magisterium" is the canonical Protestant / Roman Catholic / Eastern
> Orthodox fork; "sola fide" is the Reformation's central polemic against Tridentine Catholicism.
> There is no tradition-neutral gold answer to "is sola fide correct?" — the construct *is* the
> denominational disagreement.

This lands SOLABENCH squarely on INTRA's **D-layer (Denominational Conditioning)**. KB 10 §1.4 flags
that 93.75% of religious benchmarks treat their tradition as a monolith and "forfeit the values-alignment
claim"; a solas benchmark that scored one confession's answer as gold would commit exactly that error
at its most acute. Conversely, INTRA's **D-flag** mechanic (ask-or-flag on unspecified-school forks;
silent single-school answer = doctrinal-flattening error) is the *native correct design* for this
construct. SOLABENCH is less a new benchmark than a ready-made **item family for INTRA's D-layer**
(Protestant vs Catholic vs Orthodox forks) plus a **V-layer** advisory strand (pastoral counsel within
a stated confession).

---

## 3. Audit against the three standards

Grades: COMPLIANT / PARTIAL / MISSING / CONTRADICTS. With no pack, all present-state grades are
**MISSING**; the "faithful-build risk" column is where the substance is.

### 3a. KB 01 — Seven Laws + pre-registration

| Dimension | State | Faithful-build risk / requirement |
|---|---|---|
| Law 1 (propensity ≠ recognition; capability-corr gating) | MISSING | HIGH RISK. A solas benchmark trends naturally toward *recognition* items ("which sola teaches X?") — pure knowledge recall that will correlate with capability PC1. Must build a **behavioral/propensity** layer (advise within a confession; refuse to flatten) and report capability-correlation as a gate (>~40% = red flag). |
| Law 2 (decompose; no single aggregate) | MISSING | Requires per-confession, per-sola, K/R/V-disaggregated reporting. A single "solas accuracy" scalar would be a Law-2 violation and would hide the flattening error. |
| Law 3 (saturation is a format artifact; two-tier) | MISSING | Doctrine-fact recall will saturate instantly (KB 10 §3: faith is least-saturated *only* when probed for values, not facts). Needs a hard tier: disputed-boundary cases, cross-confessional edge rulings, "scholars/confessions differ" calibration. |
| Law 4 (declare disagreement philosophy) | MISSING | DECISIVE for this construct. The solas are inherently contested → **preserve disagreement** regime (per-confession labels), not majority-collapse. Must declare this explicitly (KB 01 Adjudication 1: stratify by consensus; these items are below any consensus threshold → distribution-match / abstention, never single gold). |
| Law 5 (validate the scorer; CoT not evidence) | MISSING | Needs ≥2 cross-family judges + κw/ICC vs human confessional panel; a same-confession judge will self-prefer its own tradition's answer (theological analogue of same-family self-preference). |
| Law 6 (contamination / eval-awareness) | MISSING | Confessional texts (Westminster, Trent, Book of Concord) are fully public → contamination certain. Needs procedural parametrization of scenarios + private holdout + monitored-vs-unmonitored arm on advisory items. |
| Law 7 (WHOSE values; anchor to authority) | MISSING | DECISIVE. "Is the model a good Protestant?" is the only coherent framing — never "is it doctrinally correct?" Each item must be anchored to a **named confessional standard** (Westminster Confession, Heidelberg, Council of Trent, Orthodox catechism) with the confession declared. Un-anchored "correct doctrine" gold = Law-7 over-claim. |
| Pre-reg checklist (15 items) | MISSING | 0/15 satisfiable — no spec exists. |

### 3b. KB 10 — Religious-values methods

| Dimension | State | Faithful-build risk / requirement |
|---|---|---|
| Three-layer K/R/V separation (§2, §6) | MISSING | Must separate: **K** = which confession teaches which sola (saturates; baseline only); **R** = apply confessional hermeneutic method to a novel case (sola scriptura reasoning vs magisterial reasoning); **V** = advise/behave from within a stated confession without flattening. Absent this, SOLABENCH would be pure K "wearing values labels" — the ELQV paradox (KB 10 §1.3). |
| Denominational resolution from day one (§6) | **the whole point** — MISSING | This IS the construct. Specify evaluative standard (confession) per item; score doctrinal flattening as error; reward "confessions differ" abstention on genuinely disputed solas. |
| Saturation defenses (§3, §4) | MISSING | Recall tier will ceiling; need the discriminative hard tier + indirect elicitation. |
| T2 recipe — discriminative layer (§4) | MISSING / PARTIAL-FIT | The T2 recipe = domain-specific + liturgical-language + exact-match + graded difficulty. Solas doctrine is **less naturally computable** than fara'id inheritance math — there is no arithmetic core. This is the pack's structural weakness: the confessional-boundary material resists exact-match verification and pushes toward rubric scoring, which KB 10 §4 shows produces ceiling/floor pathology. Mitigation: mine *computable* confessional subdomains (e.g., sacramental validity conditions, canon-law impediment logic on the Catholic side; Westminster's ordo salutis ordering) rather than open "explain sola fide" prompts. |
| Language as measured variable (§6) | MISSING | Weaker fit than Islam/Judaism (solas are a Western-Latin/German/English Reformation construct); Latin (Trent) vs the Reformers' Latin/German is the available axis. Lower priority but the confessional-source-language principle still applies. |
| Epistemic sovereignty / in-tradition authors (§5) | MISSING | Needs authors from *each* confession in the fork (Reformed, Lutheran, Roman Catholic, Orthodox) — mirrors INTRA's per-school board sizing. |

### 3c. Design 04 — INTRA stable core

| INTRA element | State | Fit |
|---|---|---|
| Three layers (K / M / D / V) | MISSING | Solas map cleanly onto **D + V**; the M (method-application, computable) layer is the weak fit (no arithmetic core — see T2 note above). |
| Denominational fork (D-know / D-flag) | MISSING | **Ideal fit.** Sola-scriptura vs sola-plus-tradition is the textbook D-fork. D-flag (ask-or-flag on unspecified confession; silent single-confession answer = flattening error) is exactly the right headline mechanic for this material. |
| T2 recipe (computable, exact-match, graded, source-language) | MISSING / weak | See 3b — the construct partially resists T2 because doctrinal boundaries are argumentative, not computational. This is SOLABENCH's principal design risk and the strongest argument for *merging into INTRA's D/V layers* rather than trying to stand it up as a T2-style standalone. |

---

## 4. Construct overlap

**With INTRA's D-layer (specific):** near-total. The five solas are the canonical Protestant /
Catholic / Orthodox fork; INTRA §2 and §8 already name "Catholic natural law vs Reformed covenantal"
and cite the 93.75%-monolith problem that the solas construct is a pure instance of. A standalone
SOLABENCH would **duplicate INTRA's D-layer novelty claim** ("D-layer has no precedent in ANY of the
965 characterizations", §8) on a narrower footprint, and would risk *undercutting* INTRA's priority if
released separately. Strong reason to converge.

**With WESTMINSTER (sibling stub):** the Westminster Confession/Catechisms are the Reformed
articulation of the solas — SOLABENCH and WESTMINSTER are the same confessional-fork construct at
different resolutions and should be scoped together (both currently empty).

**With the six 20-DESIGNS:** overlaps only Design 04 (INTRA) meaningfully. It does *not* fit the
passage-exegesis packs (FRUITBENCH/CORINTHLOVE etc.), which target virtue/behavioral constructs from a
single text; SOLABENCH is doctrine-fork, not virtue-from-passage. No overlap with non-religious designs.

---

## 5. Integration recommendation

**Primary: DEFER — too thin (the pack does not exist).** Nothing to adopt, merge, or rework today.
Record the empty-stub fact; do not treat SOLABENCH as a deliverable in the 40-BIBLEBENCH integration
tally.

**Conditional (when/if a pack is commissioned): MERGE-INTO-INTRA, do not build standalone.** Reasoning:
1. The construct is *definitionally* INTRA's D-layer (Protestant/Catholic/Orthodox fork). Building it
   standalone duplicates and risks undercutting INTRA's headline D-flag novelty claim (§8).
2. The construct partially fails the T2 recipe (no computable arithmetic core), so it cannot stand as a
   T2-style discriminative instrument on its own; it *can* serve as a strong D-fork + V-advisory item
   family inside INTRA's Catholicism/Protestant expansion (INTRA §7 P4 expansion order already lists
   Catholicism next after Islam+Judaism).
3. Merging inherits INTRA's ready-made governance (per-confession authoring + independent validation
   boards, Law-4 disagreement-preservation, cross-family judges) that a fresh SOLABENCH would otherwise
   have to reinvent.

**Action if pursued:** commission the paired deep-research pack (OAI + GDM, matching the four originals)
scoped explicitly as *"confessional forks for INTRA's D/V layers — Reformed/Lutheran/Catholic/Orthodox
readings of the five solas"*, and jointly with WESTMINSTER. Until then, leave the stub empty and carry
this memo as the design pre-brief.

---

## 6. What the pack lacks to reach cookbook conformance (checklist for the eventual build)

- [ ] Any content at all (deep-research reports, background dossier, benchmark spec).
- [ ] Construct statement framing the target as "accords with confession X's doctrine," never "correct
      doctrine" (Law 7).
- [ ] Declared **preserve-disagreement** ground-truth philosophy with per-confession labels (Law 4).
- [ ] Three-layer K/R/V separation with V (advise-within-confession) as the propensity headline (Law 1; KB 10 §2).
- [ ] D-flag ask-or-flag mechanic scoring silent single-confession answers as flattening errors (INTRA D-layer).
- [ ] Computable confessional subdomains identified to salvage a T2-style hard tier (sacramental
      validity conditions, ordo salutis ordering, canon-law impediments) — or explicit acknowledgment
      that scoring is rubric-based with the ceiling/floor mitigations from KB 10 §4.
- [ ] Cross-confession authoring + independent validation boards; κw/ICC vs human confessional panel.
- [ ] Contamination plan (public confessional texts → procedural parametrization + private holdout + canaries).
- [ ] Explicit scoping decision vs INTRA and WESTMINSTER to avoid novelty-claim duplication.
