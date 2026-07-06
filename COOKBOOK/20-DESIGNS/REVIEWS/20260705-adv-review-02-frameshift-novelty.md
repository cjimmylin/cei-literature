# Adversarial NOVELTY Review — Design 02 FRAMESHIFT

> **Refute-first review.** Reviewer role: adversarial novelty auditor.
> Artifact: `COOKBOOK/20-DESIGNS/02-normative-frameshift.md` (framework-conditioned moral reasoning).
> Question: genuinely novel vs the 965-record / 737-distinct CEI corpus and beyond-corpus benchmarks?
> Evidence base: NormEval expanded feature matrix (54×50), Moral-Psych matrix (292), Cultural rankings
> (218), Religious matrix (401); benchmark-landscape-statistics.md. Digest statistics copied verbatim,
> never recomputed. Date: 2026-07-05.

---

## Summary of verdict

The **core novelty survives but is over-claimed in §9.** FRAMESHIFT's genuinely-new element is the
**Switching-Agility (SA) axis** — a *behavioral, scored* measure of cross-framework **separation vs
fidelity** on divergence-certified items under sequential framework instruction. No corpus benchmark
scores that construct. But the §9 novelty statement (a) **materially mischaracterizes MoralReason-QA**,
(b) **omits ~5 close neighbors** that already implement framework-conditional prompting, framework-
specific reasoning gold, and care/contractarian production in reasoning-process mode, and (c) **borrows
"steerable pluralism" without engaging the steerable-alignment literature that coins and operates it**
(Sorensen roadmap, VALUEFLOW, moral-compass steering — all in-corpus). These are positioning/citation
defects, not a false core claim → **PASS-WITH-FIXES**, not BLOCK.

---

## Nearest-neighbor table (5 nearest across the whole corpus)

| # | Benchmark (corpus) | Yr / tier | FRAMESHIFT components it ALREADY covers | What it LACKS vs FRAMESHIFT |
|---|---|---|---|---|
| 1 | **MoReBench** (NormEval, ND 87, calibration anchor) | 2025 / Yes | Process-graded rubrics deeply grounded in ≥5 traditions incl. **contractarian (60)**; expert-designed; multi-perspective | No framework-**conditional gold** (which verdict a named framework licenses); no switching/separation metric; judgment-static; no care (0) |
| 2 | **MoralReason(-QA)** (NormEval, ND 80) | 2025 / Yes | **Framework-specific reasoning traces** across util/deont/virtue; GRPO reward optimizes *both* decision alignment **and reasoning process**; A3=reasoning-process, A2="Explicit framework application" | Only 3 frameworks (no care/contractarian); no sequential-switching *separation* metric; single-framework-per-item, not same-scenario cross-framework |
| 3 | **Ethical Reasoning over Moral Alignment** (NormEval, ND 80) | 2023 / Borderline | **Framework-conditional prompting** — "tests with different ethical policies as **in-context prompts**"; multiple normative formalisms at different abstraction levels; pluralism-engaged | No ethicist-validated framework-conditional gold at scale; no separation/fidelity 2×2; no divergence-certificates; no care multi-turn |
| 4 | **Structured Moral Reasoning** (NormEval, ND 83) | 2025 / Yes | **Care ethics + contractarian (50) production in reasoning-process mode**; Schwartz+care+theories; explicit **prompting taxonomy**; uncertainty acknowledged | Not multi-turn/Tronto-phase (no Responsiveness measure); no framework-conditional gold; no switching-separation |
| 5 | **Probing Ethical Framework Representations** (NormEval, ND 55) | 2026 / Borderline | Measures **cross-framework separation across 5 frameworks** (deont/util/virtue/justice/commonsense) — "differentiated ethical subspaces, asymmetric transfer, conflict-entropy" | Separation is **internal-representation**, judgment-only, *not behavioral under instruction*; "not independently scorable as a benchmark" |

**Runners-up that also erode specific §9 claims:** *EMNLP Framework* (all 5 traditions incl social-
contract 50 + care 35, tests-both — but education-domain); *RLVR Moral Reasoning* (5 frameworks incl
care 40 + justice-as-fairness 40, framework-specific reasoning eval — but no independent dataset);
*One Model Many Morals* (care 30, contractarian 20, 10-framework LLM-judge, multilingual); *Analyzing
the Ethical Logic of Six LLMs* (contractarian 50, multi-typology). **Beyond-corpus/steering:**
*Exploring and steering the moral compass* (2024, activation-steering of MFT) and *VALUEFLOW: Toward
Pluralistic and Steerable Value-based Alignment* (2026, Schwartz/HIVES value-profile steering) — the
two nearest **steering** neighbors; *A Roadmap to Pluralistic Alignment* (Sorensen 2024) coins
"steerable pluralism," the design's own headline term.

---

## Ranked defects

### MAJOR 1 — §9 mischaracterizes MoralReason-QA (the nearest verdict-vs-process rival)
§9: *"MoralReason-QA has framework labels but verdict-level scoring."* The NormEval matrix contradicts
this: `A3 = "Tests reasoning process"`, `A2 = "Explicit framework application"`, and the rationale
states it *"trains models to internalize and apply specific moral frameworks via GRPO with composite
rewards optimizing **both decision alignment and reasoning process**."* So it is **not** verdict-level
only; it grades framework-specific process. The differentiator that actually survives is narrower:
FRAMESHIFT adds (i) care+contractarian frameworks MoralReason omits, and (ii) a **same-scenario
cross-framework separation** metric MoralReason has no analogue for. **Fix:** rewrite the MoralReason
line to concede framework-specific *process* scoring and pivot the distinction to switching-separation
+ the 2 missing traditions.

### MAJOR 2 — "No care/contractarian production tasks" is overstated (undercited neighbors)
§1/§9 lean on care (2/54 substantive) and contractarian (4/54) voids to justify production tasks. But
in reasoning-process mode the corpus already has: **Structured Moral Reasoning** (care + contractarian
50), **MoReBench** (contractarian 60), **EMNLP Framework** (care 35 + social-contract 50, tests-both),
**RLVR** (care 40 + justice-as-fairness 40). The *defensible* finer gap is FRAMESHIFT's specific
mechanisms — **multi-turn Tronto-phase Responsiveness** (genuinely absent; NormEval App-H prototype is
n=10) and **contractarian construction tasks** (veil parameterization, reasonable-rejection ID,
maximin-vs-Gauthier). **Fix:** downgrade "no care/contractarian production tasks" to "no care
*multi-turn responsiveness* or contractarian *construction* tasks," and cite the four neighbors as
partial coverage the design extends rather than a void it fills.

### MAJOR 3 — Headline "steerable pluralism" ignores the steerable-alignment literature
The paper's hook — *"can they reason in five ethical methods?"* / "whether steerable pluralism is real
or vocabulary" — uses Sorensen's coinage without citing **A Roadmap to Pluralistic Alignment**
(Sorensen 2024, in-corpus), and never engages the two nearest behavioral/representation **steering**
works: **Exploring and steering the moral compass** (2024, activation steering of moral foundations)
and **VALUEFLOW** (2026, "pluralistic and steerable value-based alignment"). None of these measure
*framework-method* separation on divergence-certified items across the five normative traditions — so
the core survives — but an uncited reviewer will read §9's "no instrument measures cross-framework
separation under instruction" as false on its face (activation steering and Probing-representations
are separation measures). **Fix:** add a "steering & pluralistic-alignment" paragraph distinguishing
FRAMESHIFT (behavioral, instruction-conditioned, 5 *normative-method* verdicts, divergence-certified)
from value/foundation/activation steering.

### MAJOR 4 — §9 blanket claim needs the load-bearing qualifier
*"No instrument in any of the four matrices measures cross-framework separation under instruction"* is
only true with qualifiers the design leaves implicit. Counter-readings: **Probing Ethical Framework
Representations** measures 5-framework separation (internal, not behavioral); **Ethical Reasoning over
Moral Alignment** conditions on framework via in-context policies (no separation metric). **Fix:**
restate as "no instrument scores cross-framework **verdict** separation-vs-fidelity as a **behavioral**
metric on **divergence-certified** items across ≥5 named normative traditions" — that claim holds
against every neighbor above.

### MINOR 1 — "ETHICS is dead" overclaims
§9 calls ETHICS "dead," yet the corpus shows it is still the active substrate for **Probing Ethical
Framework Representations** (2026), **One Model Many Morals**, and **Is ETHICS About Ethics?** — i.e.
saturated-as-target but load-bearing as a resource. **Fix:** "saturated at the frontier" not "dead."

### MINOR 2 — Missing citations for FC-axis prior art
Add **Ethical Reasoning over Moral Alignment** (2023) and **Aligning LLM Agents with Rational and
Kantian Preferences** (deeply operationalized Kantian universalizability) as the FC-axis precedents the
design builds on; currently §9 cites none of the framework-conditional-prompting lineage.

---

## Refutation attempt — did the claimed gap survive?

Attempted refutation on each FRAMESHIFT component:
- **FC (framework-conditional prompting/gold):** partially anticipated — MoralReason (framework
  process), Ethical Reasoning over Moral Alignment (in-context policies), MoReBench (grounded rubrics).
  Novel increment = ethicist-validated *conditional verdict* gold at scale + 5 traditions incl. voids.
  **Survives as increment, not as first-of-kind.**
- **PR (procedural rubric):** MoReBench is the acknowledged anchor; FRAMESHIFT's distractor/negative-
  weight criteria are a refinement, not new territory. **Weakest-novelty axis.**
- **SA (switching-agility / separation-vs-fidelity under instruction):** no corpus benchmark scores it
  behaviorally; representation-level (Probing) and value/activation steering (moral-compass, VALUEFLOW)
  are adjacent but distinct construct/mechanism. **Genuinely novel — the paper's real hook.**
- **DP (default framework fingerprint):** overlaps "Are LLMs Consequentialist or Deontological" and
  DailyDilemmas value-profiling; FRAMESHIFT's IB−IH + 5-framework scoring is an extension. **Partial.**

Net: the gap is **not empty** for FC/PR/DP but **is empty for SA**. Recentre the novelty claim on SA
(and the care-multi-turn + contractarian-construction task voids), demote FC/PR to "extends," and the
design is defensible.

---

## Minimal fix set (accept → PASS)
1. Rewrite the MoralReason line (Major 1) to concede framework-specific process scoring.
2. Reframe care/contractarian "void" as the finer multi-turn-Tronto + contractarian-construction gap;
   cite Structured Moral Reasoning, MoReBench, EMNLP, RLVR as partial coverage (Major 2).
3. Add a steerable-pluralism paragraph citing Sorensen 2024, VALUEFLOW, moral-compass steering (Major 3).
4. Add the behavioral/divergence-certified qualifier to the §9 headline claim (Major 4).
5. Soften "ETHICS is dead"; add FC-axis citations (Minors).

---

## VERDICT: PASS-WITH-FIXES

**Single most likely remaining error:** that **"Ethical Reasoning over Moral Alignment" (2023)** already
implements framework-conditional in-context prompting closely enough that FRAMESHIFT's *FC* axis is a
thinner increment than the design implies — assessed here only from its matrix rationale (ND 80,
"tests with different ethical policies as in-context prompts"), not the primary paper. Read that paper
before finalizing the FC-novelty language; if it also reports per-framework separation, Major 4 escalates.
