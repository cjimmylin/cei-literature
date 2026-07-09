# RP-04 HIDDENCURRICULUM — Re-Scoring Matrix Design

**Date:** 2026-07-09 · **Author:** Opus session (handoff item 1.5) · **Status:** design only; execution is Cycle-2 (key-gated)
**Governs:** re-scoring of the frozen corpus at `INNOVATION/40-BUILDS/rp04-corpus/frozen/`
**Binding brief:** `INNOVATION/05-research-programs/RP-04-HIDDENCURRICULUM.md` (kill criteria K1–K3 are binding)
**Binding constraint:** the SERMONMOUNT lesson — synthetic-mock outputs validate the re-scoring MACHINERY only; they can never enter a judge-bias measurement as if they were model behavior (handoff standing constraint 5; RP-04 §method Phase 1).

---

## 0. The load-bearing finding this matrix has to survive

RP-04 Phase 1 was scoped as "re-score a frozen sample of **existing CEI bank responses** with 3+ judge families." The corpus assembly (2026-07-09) found that **those responses do not exist as real model behavior**:

| Source | Response-level records on disk | Provenance | Re-scoreable as model behavior? |
|---|---|---|---|
| THORNS synthetic JSON (×2) | 0 raw responses (aggregates only) | derived-synthetic | No |
| THORNS N=4 real probe | 4, but **verbatim text not saved** | real-model | No (no text to re-judge) |
| DIMGLASS mock jsonl | 80 grade labels, no text | synthetic-mock | No |
| WITNESS scored.jsonl | 10,350 response-level rows | synthetic-mock | **Machinery only** |

**Consequence:** the judge-bias measurement (H3, the memo every BibleBench family is supposed to cite) is **fully key-gated** — it cannot begin until Cycle 2 produces real responses to the frozen stimulus banks. What Cycle 1 *can* deliver is (a) a validated, dry-run-proven re-scoring pipeline and (b) a pre-registered matrix so the moment keys arrive, the measurement runs mechanically. This document is that pre-registration.

Do not soften this into "we re-scored the pilots." We did not. We froze stimuli and validated machinery.

---

## 1. The three axes

### Axis A — Judge families (the bias probe)

The whole point of H3 is triangulation across **base-model families**, because the inheritance literature (Christian et al. 2026) says value bias is a pretraining-family signature, not a recipe artifact. Minimum viable = **3 families**; this also discharges the SERMONMOUNT D1 third-judge-family requirement.

| Judge slot | Family target | Key dependency | Notes |
|---|---|---|---|
| J1 | Anthropic (Claude) | `ANTHROPIC_API_KEY` | SDK already installed |
| J2 | OpenAI (GPT) | `OPENAI_API_KEY` / Codex-OAuth CLI | different pretraining family |
| J3 | Google (Gemini) | Gemini key — **ideal, Jimmy gate #1** | third family; without it, J3 falls back to a human-label deviation slice (SERMONMOUNT D1 alternative) |
| J4 (optional) | Open-weight (Llama-/Qwen-derived, hosted) | GPU/hosted-endpoint budget — Jimmy gate #2 | bridges Phase 1 judges → Phase 2 RM audit |

Anti-leakage discipline (handoff constraint 6, `dispatching-parallel-agents` norms): **generator ≠ judge** within a family; each judge scores blind to the others; no family both authored and grades the same item.

### Axis B — Corpus strata (what gets scored)

Strata are defined so that provenance never silently mixes. **Only Stratum S3 responses can enter the judge-bias measurement.** S1/S2 are machinery lanes.

| Stratum | Contents | Provenance | Role in matrix |
|---|---|---|---|
| **S0 — stimulus banks (frozen)** | THORNS bank 60 + gold 60; DIMGLASS public seeds 30 (+1026 keys); WITNESS renderings 240 / cores 30 | human-authored / synthetic-generated **stimulus** | Inputs. Cycle 2 runs models against these to *produce* S3. |
| **S1 — synthetic-mock responses** | WITNESS scored.jsonl (10,350); DIMGLASS mock jsonl (80) | synthetic-mock | **Machinery validation only.** Re-score with the J-pipeline to prove it recovers the injected/known labels; a dead giveaway if the pipeline "finds bias" in a deterministic simulator. NEVER reported as model bias. |
| **S2 — synthetic aggregates** | THORNS results JSON ×2 | derived-synthetic | Reference for gate-logic wiring only; not re-scoreable at response level. |
| **S3 — real model responses** | **empty today.** Populated in Cycle 2 by running J-vendors' *subject* models against S0. | real-model | **The only stratum that produces the judge-bias memo.** |
| **S3′ — real probe (degenerate)** | THORNS N=4 | real-model, **no verbatim text** | Documented as the sole existing real-model observation; excluded from measurement (nothing to re-judge). |

Within S3, sub-stratify for the disagreement-structure analysis RP-04 §Phase1 demands — "by item type, framework, and tradition":
- **by design**: THORNS (fruit-vs-vice antagonism) / DIMGLASS (conviction-under-pressure) / WITNESS (END–ACT dissociation).
- **by item type / modality**: THORNS single-shot vs escalation-arc; WITNESS END/REC/GEN/ACT; DIMGLASS single vs multi-round.
- **by framework/tradition**: the cell/family tags carried in each item (THORNS 20 vice cells; WITNESS S-ID registry; DIMGLASS 5 domains).
- **by polarity**: aligned vs misaligned pole (already tagged in WITNESS scored.jsonl; derivable in THORNS gold paths).

### Axis C — Scoring dimensions (what each judge emits per response)

| Dimension | Definition | Applies to |
|---|---|---|
| D1 primary label | the design's own rubric verdict (THORNS: fruit/vice/CFT path; DIMGLASS: retained/hedged/partial/flipped; WITNESS: gold/counterfeit signal) | all |
| D2 confidence | judge's self-reported confidence / margin | all |
| D3 rationale span | the text the judge cites as decisive (for shortcut/leakage audit) | all |
| D4 framework-affinity | does the judge over-reward a nameable rhetorical framework independent of the act? (the H3 bias signal) | THORNS, WITNESS |
| D5 refusal/abstention | judge declines or hedges | all |

**Bias estimand (H3):** for each (judge family × stratum cell), the deviation of that family's D1 rate from the cross-family consensus, decomposed into item type / framework / tradition variance. Test-retest (same judge, paraphrased item) and inter-family agreement (κw / ICC) bound reliability — **K1 gate: paraphrase reliability r ≥ 0.5** or profiles aren't real at this granularity.

---

## 2. The matrix (Judge family × Stratum × Dimension)

Cells marked ⛔ are key-gated (Cycle 2). ✅ = executable in Cycle 1 (no keys). The single Cycle-1 deliverable is validating the pipeline on S1.

| | S1 synthetic-mock (machinery) | S3 real responses (measurement) |
|---|---|---|
| **J1 Claude** | ✅ dry-run: recover known labels; D1–D5 wired | ⛔ needs `ANTHROPIC_API_KEY` + S3 |
| **J2 GPT** | ✅ *(if Codex-OAuth CLI present; else ⛔)* | ⛔ needs `OPENAI_API_KEY` + S3 |
| **J3 Gemini** | ⛔ | ⛔ needs Gemini key (Jimmy gate #1) or human-label fallback |
| **J4 open-weight** | ⛔ | ⛔ needs hosted-endpoint budget (Jimmy gate #2) |

Reliability sub-matrix (paraphrase / test-retest) attaches to the S3 column only — it is meaningless on deterministic S1.

---

## 3. Execution phases

**Cycle 1 (now, key-light) — machinery validation:**
1. Build the re-scoring harness on the S1 lane: read WITNESS scored.jsonl, present each (item, mock-response signal) to the judge-scoring code path, confirm it recovers the injected labels and that D1–D5 populate. *(This reuses RP-02 `fairgold` rescoring-engine patterns — handoff item 1.3; pure computation, no keys.)*
2. Pre-register K1/K2/K3 decision rules and the variance-decomposition model (lme4, already in the pixi lockfile — RP-04 O4) against the S3 schema, so the analysis is frozen before any real data exists.
3. Do NOT run any judge family against S1 and report a number as bias. S1 is a plumbing test.

**Cycle 2 (keys arrive — Jimmy gate #1):**
4. Via the shared runner (handoff 2.1): run subject models against S0 stimulus banks → populate S3. Respect the THORNS live-mode hard-block (spine fixes S-1/S-2) before any FRUITBENCH-derived live run.
5. Run J1–J3 (J4 if budget) against S3, blind, generator≠judge, ≥2 cross-family judges per item, human-validated κw/ICC per KB-07.
6. Compute the bias estimand + disagreement structure by item type / framework / tradition / polarity.
7. Apply kill criteria:
   - **K1:** paraphrase reliability r < 0.5 → publish the reliability finding, stop profiling.
   - **K2 (pre-committed, do NOT soften):** if judge biases are large enough to threaten a published CEI verdict, a robustness/errata pass on the affected bench(es) is **mandatory**, not optional.
   - **K3** applies to Phase 3 only (out of scope here).
8. Write the judge-bias memo → **Fable-tier review (O5)** before it becomes binding on other CEI programs; queue in PENDING-RULINGS if no Fable window.

---

## 4. Explicitly blocked on keys (Cycle 2 gate list)

| Blocked deliverable | Blocking dependency | Jimmy gate |
|---|---|---|
| Any S3 real-response generation | `ANTHROPIC_API_KEY` + `OPENAI_API_KEY` (min) | #1 API keys |
| Third judge family J3 | Gemini key (else human-label deviation slice) | #1 (ideal) |
| Open-weight judge J4 / Phase-2 RM audit bridge | hosted-endpoint / GPU-inference budget | #2 GPU budget |
| Human-validated judge κw/ICC (KB-07) | human raters/panel | #3 raters |
| THORNS live run | spine fixes S-1 (live-adapter generate signature) + S-2 (attacker routing) — **code, not keys** | none (Opus, but hard-blocked in `run_pilot.py` until done) |

**Judge-corruption caveat (G-09)** must be cited in the methods of the resulting memo (handoff constraint 2).

---

## 5. What a downstream session inherits

- Frozen stimulus + machinery corpus at `frozen/` with per-entry provenance in `manifest.json`.
- This matrix as the pre-registration: the moment keys land, Cycle 2 steps 4–8 run without re-litigating design.
- The honest headline: **Phase 1's judge-bias measurement did not run and could not run in Cycle 1** — no real responses existed. Reporting otherwise would repeat the exact SERMONMOUNT error RP-04 was built to avoid.
