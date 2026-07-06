# Adversarial NOVELTY Review — Design 01 UNMARKED

> **Reviewer role:** refute-first novelty adversary. **Artifact:** `COOKBOOK/20-DESIGNS/01-flagship-unmarked.md`.
> **Question:** Is UNMARKED genuinely novel vs the 965 characterized benchmarks (737 distinct) and vs known
> post-2024 agentic/safety evals beyond the corpus? **Date:** 2026-07-05.
> **Method:** read design + `10-LITERATURE/benchmark-landscape-statistics.md` + §8 file-pointers of all four
> 2026-07-05 digests; queried the four scored matrices (MoralPsych 292, Religious 401, Cultural 218, NormEval 54)
> with `../.venv/bin/python3`. Digest statistics copied verbatim, never recomputed.

## Bottom line

The **integrative** novelty claim survives: no benchmark — in corpus or (to my knowledge) beyond it —
combines all five of {unannounced/incidental moral embedding · matched competence controls · stated-revealed
gap headline · eval-awareness compliance-gap instrumentation · fresh-per-run procedural generation}. **But
three of those five components are individually well-realized elsewhere**, and the §9 novelty *argument* is
mis-scoped (it proves novelty against the four matrices, which — I verified — do not even contain the design's
own named nearest neighbors). No Critical defect. Several Major positioning/citation defects that, unfixed,
will let an oral-track reviewer puncture the "first benchmark that measures X" framing on a single component.

---

## Ranked defects

### MAJOR-1 — SRG ("stated-revealed gap") is presented as measuring "what no existing benchmark measures"; a stated-vs-revealed gap metric already exists (honesty).
**Evidence.** Design §2 line 43–44: "SRG is the headline metric; it is robust to saturation by construction";
§1 line 30–31: "UNMARKED measures what no existing benchmark measures." [beyond-corpus] The **MASK** benchmark
(Center for AI Safety, 2025) already operationalizes exactly a *stated-belief vs revealed-behavior* gap —
eliciting a model's stated position, then measuring divergence when the same proposition is put under pressure.
The novel move in UNMARKED is *not* the gap construct; it is (a) computing it on **incidental agentic action**
rather than pressured honesty statements, and (b) using the *same dilemma* in-task vs fresh-context. The design
never cites MASK and does not narrow the claim.
**Minimal fix.** Cite MASK (and, in-corpus, DeNEVIL 2023 — a generative-vs-professed value gap, MoralPsych tier
`high`, PD 50.5) in §2/§9; restate SRG's novelty as *"generalizes the stated-revealed gap from single-turn
honesty to multi-domain incidental moral action,"* not as a first-of-kind metric.

### MAJOR-2 — The §9 nearest-neighbor list omits MACHIAVELLI, the corpus's own closest agentic-moral-behavior benchmark.
**Evidence.** §9 lines 163–167 name MORALSIM, SHADE-Arena, PacifAIst, DIB, Kilov, ConflictScope as nearest
neighbors. It omits **MACHIAVELLI** (Pan et al. 2023), which is the single most-agentic behavioral benchmark
*actually in the scored corpus*: MoralPsych matrix, tier `top`, PD 52.5 / COMPOSITE 60.95, feature A3=90
("500K+ scenarios centering on social decision-making"), A6 evidence: *"reward-ethics trade-off measured across
multiple agents"*, B1=50 ("action selection in text games… automated moral behavior scoring"), B10=70
("Designed for LM agents"). It already covers **agentic moral behavior + behavioral (ledger-like) scoring** —
two of UNMARKED's three core components. It lacks incidental/unmarked embedding (its moral valences are
explicitly annotated), matched competence controls, SRG, and fresh generation (static, memorizable games).
**Minimal fix.** Add MACHIAVELLI as the lead in-corpus nearest neighbor in §9 and state the four specific
differentiators above. Omitting the closest corpus neighbor is the fastest way for a reviewer to distrust the
whole NN survey.

### MAJOR-3 — The novelty proof is scoped to "the four matrices," but the design's own named nearest neighbors are NOT in those matrices, making the claim near-vacuous as evidence.
**Evidence.** §9 line 161: "Nothing in the four matrices scores unannounced moral stakes…" I verified against
the scored matrices: **MORALSIM, ConflictScope, PacifAIst, AgentHarm are absent from all four scored feature
matrices** (they appear only in `CULTURAL-GLOBAL/DATA/20260404-benchmark-candidates.json` / `-nw-scores.json`
enrichment files — dropped before the 218-ranking; `machiavelli/moralsim/conflictscope/pacifaist/agentharm
in-rankings: False`). **SHADE-Arena and Anthropic "Agentic Misalignment" appear in no corpus file at all.** So
"nothing in the four matrices does this" is true but weak: the real competitors were never characterized, so
the matrices cannot certify novelty against them. The load-bearing novelty argument therefore rests on
beyond-corpus reasoning that the design gestures at but does not do rigorously.
**Minimal fix.** Reframe §9: state explicitly that UNMARKED's competitive frontier is the *beyond-corpus
agentic-safety literature* (Apollo scheming, Anthropic Agentic Misalignment, SHADE-Arena, MORALSIM,
ConflictScope), not the values-benchmark matrices; keep the matrices only as evidence that the *values-eval
field* has no incidental-agentic entrant. This is a defensible and stronger claim.

### MAJOR-4 — [beyond-corpus] Agentic moral behavior under undisclosed incentive conflict is substantially realized by Anthropic's "Agentic Misalignment" (2025), which the design does not cite (it cites the more distant SHADE-Arena).
**Evidence.** §9 line 164 cites SHADE-Arena (sabotage/deception, model given a *secret malicious* side-task).
[beyond-corpus] Anthropic's **Agentic Misalignment** study (June 2025 — blackmail / insider-threat scenarios)
is closer to UNMARKED's MB register: models take harmful autonomous actions under goal conflict **without being
instructed to misbehave** — i.e. moral stakes that are not framed as a moral test. UNMARKED still differs
(procedural generation, matched controls, SRG, six mundane work domains rather than a few dramatic set-pieces,
and *incidental* low-salience stakes vs Agentic Misalignment's high-drama framing), but the design must
differentiate it or a reviewer will call MB "already shown."
**Minimal fix.** Add Agentic Misalignment (and MORALSIM's incentive-conflict result, which the design already
cites for motivation) to the §9 NN set; anchor UNMARKED's differentiator on **stake-salience levels 2–3
(inference-required, mundane)** + matched controls, which those set-pieces lack.

### MINOR-1 — Eval-awareness / monitored-vs-unmonitored compliance-gap instrumentation (§3.4) is framed as an integrated novel component but is now standard method.
**Evidence.** §3.4 lines 88–92 and §9 line 167 fold "eval-awareness instrumentation" into the integration
claim. [beyond-corpus] Monitored/unmonitored compliance gaps are established in Apollo Research in-context
scheming (2024), OpenAI covert-action/sandbagging evals (the design itself cites `[OpenAI-gpt-5]` covert-action
numbers in §3.3) and Anthropic Alignment Faking (cited §1 line 19). It is adopted method, not novelty.
**Minimal fix.** Present §3.4 as "adopting the now-standard compliance-gap probe," and drop eval-awareness from
the *novel-integration* enumeration in §9 (keep the other four components).

### MINOR-2 — Several §9 nearest-neighbor citations resolve to KB literature docs, not to characterized corpus records; the "vs 965 benchmarks" header oversells corpus grounding.
**Evidence.** DIB `[2026-Ma]`, Kilov `[2025-Kilov]`, Herrador/PacifAIst `[2025-Herrador]` are KB/lit citations;
of the §9-named neighbors only MACHIAVELLI, TRIAL, DeNEVIL, NurValues, FAIRMT-BENCH are actually *scored* corpus
records (see NN table). Not a novelty defect, but the framing "vs the 965 characterized benchmarks" (title +
§9) implies these neighbors were characterized, which they were not.
**Minimal fix.** One sentence distinguishing "characterized corpus neighbors" from "beyond-corpus literature
neighbors."

---

## Nearest-neighbors table (5 characterized corpus benchmarks + beyond-corpus flags)

| # | Benchmark | Corpus / record | UNMARKED components it already covers | What it lacks (UNMARKED's edge) |
|---|---|---|---|---|
| 1 | **MACHIAVELLI** (2023) | MoralPsych, tier `top`, PD 52.5 | Agentic moral behavior of LM agents; behavioral/action scoring; reward-vs-ethics tradeoff | Announced/annotated moral valences; static memorizable games; no incidental embedding, no matched controls, no SRG, no fresh generation |
| 2 | **Between a Rock / TRIAL** (2025) | MoralPsych, tier `med`, PD 34.0 | Multi-turn escalation with stakes *embedded* in framing; commitment-exploitation (design cites for T3) | Announced red-team dilemma; not agentic task-work; no behavioral ledger, no SRG, no controls |
| 3 | **DeNEVIL** (2023) | MoralPsych, tier `high`, PD 50.5 | Gap between professed and generatively-revealed values (SRG cousin) | Prompt-elicited generation, not agentic action; announced value probing; no competence control |
| 4 | **NurValues** (2025) | MoralPsych, tier `high`, PD 55.0 | Real-world behavior instances with *contextual cues*; hard/easy salience split (design cites §6 separation stat) | Classification of announced nursing scenarios; not agentic, no action space, no SRG |
| 5 | **FAIRMT-BENCH** (2025) | Cultural, rank 201/218, TOPSIS 0.115 | Multi-turn fairness degradation (design cites for T3 multiturn) | Fairness-specific, announced; low corpus quality rank; no agentic task, no SRG, no controls |
| — | [beyond-corpus] **MASK** (2025) | not in corpus | Stated-vs-revealed **gap metric** (honesty) — threatens SRG's first-of-kind framing | Pressured-honesty statements, not incidental agentic action; single-turn |
| — | [beyond-corpus] **Apollo in-context scheming / OpenAI covert-action** (2024–25) | not in corpus | Unannounced misaligned agentic behavior; monitored-vs-unmonitored compliance gap | Deception/sabotage focus, not general incidental morality; no SRG, no matched controls |
| — | [beyond-corpus] **Anthropic Agentic Misalignment** (2025) | not in corpus | Agentic moral behavior under undisclosed goal conflict (MB register) | High-drama set-pieces, not mundane low-salience work; no procedural generation, no SRG, no competence controls |
| — | [beyond-corpus] **SHADE-Arena** (2025) | not in corpus (design cites) | Agentic, covert, monitor/detect side-task | Given secret *malicious* objective; sabotage not values-general; no SRG |

*Corpus quality context (copied verbatim, not recomputed):* the field is "runnable long before it is deep"
(landscape §1); non-western coverage and psychometric validity sit "at or near floor in every table"
(landscape §4). UNMARKED's depth/agentic axis is genuinely under-occupied — consistent with novelty.

---

## Refutation attempt — result

- **Is the claimed gap empty?** Within the four *scored* matrices: yes — no record does incidental-agentic
  moral action with an SRG headline (MACHIAVELLI is the nearest and misses 4/5 components; verified
  MORALSIM/ConflictScope/PacifAIst/AgentHarm are not in the scored matrices at all).
- **Is any single component already realized?** Yes, three: the stated-revealed gap (MASK), agentic moral
  behavior under undisclosed incentive (Agentic Misalignment / MACHIAVELLI / MORALSIM), and compliance-gap
  eval-awareness (Apollo / OpenAI / Alignment-Faking). These force MAJOR-1/-4 and MINOR-1: the design must
  differentiate per component, not rest on integration alone.
- **Is the full combination realized anywhere?** Not to my knowledge. The integrative claim (all five
  components + six mundane deployment domains + matched competence twin) holds. → **No Critical.**

---

## VERDICT: PASS-WITH-FIXES | Critical: 0 | Major: 4 | Minor: 2

**Single most likely remaining error:** a post-2024 agentic-values benchmark I do not know of — most plausibly
an incidental/"honeypot" agentic eval spun out of the Apollo / Anthropic / METR agentic-safety line in
late-2025/2026 — may already pair *unannounced* stakes with a behavioral-vs-stated comparison, collapsing
MAJOR-1 and MAJOR-4 into a single Critical. The corpus cannot rule this out because its scored matrices do not
characterize the agentic-safety frontier at all (MAJOR-3). Before the oral-track submission, run a dedicated
beyond-corpus lit sweep of 2025–2026 agentic-misalignment / honeypot / scheming evals with the explicit query
"incidental moral stake + behavioral scoring + stated-vs-revealed."
