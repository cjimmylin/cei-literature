# WS-1 — Code-vs-Spec Audit: DUPLEX-P0 runner/analysis + CRUX ENGINE (Fable-adjudicated, 2026-07-07)

**Method:** two Opus audit agents ran the FRUITBENCH A1–A5 grammar over each codebase against
its governing specs; every candidate divergence below was adjudicated by Fable. The one
previously-known defect (PS-2, G3 pooled-fallback) was excluded from the sweep by
instruction — everything here is NEW. Test suites: DUPLEX-P0 **61/61 pass**, ENGINE
**33/33 pass** — and that is the headline lesson: *green tests certified code that diverges
from spec in 12 places, because the tests test the code, not the spec.*

## Verdict

- **DUPLEX-P0 runner/analysis: NOT run-ready.** The core handoff's "one config flag from
  live" was wrong. Twelve adjudicated P0-BLOCKING defects (§1) would have produced silently
  invalid G1/G2/G3 verdicts on a credentialed run. All are fixable in 1–2 Opus sessions with
  this report as the spec; none invalidates the item bank or the design.
- **CRUX ENGINE: sound and reproducible**, with two substantive fixes (§2) — one factor
  never renders in the scenario surface (its AMCE arm is structurally dead), and the 60-cell
  fraction emits a duplicate cell that is present in the shipped pilot artifact.

## §1 DUPLEX-P0 — adjudicated findings (D-numbers = audit agent's)

**Grade key:** P0-BLOCKING = must be fixed and tested before ANY live P0 spend (joins R-1 and
PS-2 as run preconditions). All dispositions are Opus-executable; none needs Jimmy.

| # | Finding | Grade | Disposition |
|---|---|---|---|
| D1 | G3 computed over ALL 65 items — no `greene_subset` filter anywhere; gate measured on the wrong population | P0-BLOCKING | G3 rebuild package (with PS-2): filter to the 5 Greene items; per-item × per-frame table per G3-a + IB-2 sensitivity |
| D2 | M3 fallback conditions (`agent_patient`/`patient_agent`) never produced by the orchestrator → fallback branch always dead, silently degrades to the ordinary deliberation delta labelled "fallback" | P0-BLOCKING | G3 rebuild package: administer `greene_fallback_prompt` as a real arm for the Greene items, or re-register the fallback contrast; NO silent degrade — fail loud if the arm is absent |
| D3 | G1 content baseline pools ALL conditions; ruling G1-a says `standard` only | P0-BLOCKING | G1 rebuild package |
| D4 | G1 process/content CVs over unmatched model sets ("same models" violated) | P0-BLOCKING | G1 rebuild: enforce roster intersection |
| D5 | G1 process signature = pooled absolute delta, not per-item condition-deltas; opposite-sign items cancel pre-`abs()` | P0-BLOCKING | G1 rebuild: per-item deltas per G1-a |
| D6 | G1-b 40% live-cell floor + PROVISIONAL state entirely absent | P0-BLOCKING | G1 rebuild |
| D7 | No UNMEASURABLE state (V-4/PS-1); temp-drop determinism would be miscounted as dead cells | P0-BLOCKING | G1 rebuild: three-state cell coding (live/dead/unmeasurable) |
| D8 | Monitored/unmonitored frames NEVER rendered — orchestrator iterates resource conditions only; the X3 compliance gap (mandatory first-class metric) has zero implementation | P0-BLOCKING | Orchestrator: render the 5×2 factorial the bank was built for; add gap statistic to analysis |
| D9 | `stance_polarity` reverse-scoring applied NOWHERE in runner/analysis; the 18 preserve-keyed items would invert PS-dir — the exact R-1 failure mode, believed fixed but only fixed in the *bank metadata* | P0-BLOCKING | Scorer interface: polarity mapping applied at record creation, with a test on an `affirmative_preserve` fixture; R-1 is NOT satisfied until this lands |
| D10 | Refusal regex (`i can't`/`i won't`…) classifies substantive stance-1 answers as refusals → silently deletes the preserve pole, biasing PS toward intervention (compounds D9) | P0-BLOCKING | Refusal = no stance taken; classify via scorer output, not substring match on the answer; guard test with a "No, I can't approve that" stance-1 fixture |
| D11 | `seed_for` = `abs(hash(...))` → PYTHONHASHSEED-randomized across processes (verified: 3 interpreters, 3 different seeds); checkpoint resume silently re-runs every cell | P0-BLOCKING | `hashlib` stable digest; cross-process resume test |
| D12 | NO-PROCESS-SHIFT null + majority-class + all-neutral baselines (mandatory reporting §5.6) absent from analysis | P0-BLOCKING | Implement as report outputs |
| — | G1 content axis has zero records on the real bank (no `axis=="content"` items exist); per G1-a the baseline derives from standard-condition means of the SAME 48 items — wiring absent | P0-BLOCKING | Part of G1 rebuild (no new items needed) |
| D13 | Anchored G3 pools rather than per-item sign | MINOR | Pooled is the registered anchored-mode rule (matches §7 + mini-norm prereg); add per-item table as descriptive sensitivity |
| D14 | Generic load-suffix mismatch vs compliance coder (dead path unless bank prompts missing) | MINOR | Fail loud if `condition_prompts` missing instead of substituting |
| D15 | `affect_primed` authored but not in roster's run conditions | MINOR | Deliberate config choice; document in run README (bank's 5th condition present, run-gated) |
| D16 | G2-b outlier guard = max-degree drop + re-apply 0.90 (unratified reduced-set bar; max-degree ≠ set-cover) | MINOR | Acceptable proxy; RATIFIED here as the operationalization, with the reduced-set 0.90 bar registered (stress-test SC-15 showed the guard is belt-and-suspenders at the 90% bar anyway) |

**Free parameters ratified as config (no action):** g1_epsilon 0.02, sd_dead 1e-6, g2 α/threshold,
g3_min_effect 0.02, reps/temp/seed. **Ratified with flag:** Welch small-sample → p=1.0
(conservative, fine for P0). **Unratified hardcodes resolved by the rebuild packages above.**

**Consolidated P0 run-precondition list (supersedes all previous partial lists):**
R-1-in-scorer (D9) · PS-2 + D1 + D2 (G3 package) · D3–D7 + content-wiring (G1 package) ·
D8 (frames + X3) · D10 (refusal) · D11 (seeds) · D12 (nulls) · obfuscation-QA (<10%
recognition, items README gap 1) · IB-1a/IB-3a/IB-5 analysis wiring (item-read report).
An Opus session MUST run this list as a checklist and attach evidence per item before any
credentialed call.

## §2 CRUX ENGINE — adjudicated findings

Verified TRUE by measurement (no action): shortcut-audit detection power is real (a leaky
set IS caught); FineTuneProbe pass/fail rule matches X2; publish_spec ships the confounding
report and withholds live instances correctly; "~5 at n=60" imbalance claim accurate; main
effects exactly balanced at n=60; regeneration byte-identical (deterministic).

| # | Finding | Grade | Disposition |
|---|---|---|---|
| ENG-1 | `relationship` factor never appears in the rendered surface — two cells differing only on in_group/out_group produce byte-identical text; its AMCE estimate is structurally ~0; the minimal-pair test checks `.cell` but never `.surface` | MAJOR | Fix in the D-3 prose-enrichment pass: every one of the 6 factors must visibly render; add a per-factor surface-diff test. BLOCKS P1 instance generation (and therefore the P1 validation survey) |
| ENG-2 | Fraction emits duplicate cells (59/60 distinct at seed 0; 4 of 5 seeds collide; the duplicate is in the shipped `out/` artifact); scenario_id collides with it | MAJOR | Enforce distinct cells + id-uniqueness test; regenerate `out/`; disclose in README limitations until the D-1 OA upgrade subsumes it |
| ENG-3 | Triads/minimal-pairs are library-only — never emitted in pilot artifacts (CO/AMCE machinery under-represented in the reproducible output) | MINOR | Emit both batteries at P1 build |
| ENG-4 | Constant `instance_seed` across cells → protagonist/setting pools cycle identically (8×7=56 combos for 60 cells) | MINOR | Vary per cell in the enrichment pass |

## §3 Systemic lesson (feeds the master roadmap)

Both codebases were built TDD with green suites, yet WS-1 found 14 substantive spec
divergences. The failure mode is uniform: **tests encoded the implementation's reading of
the spec, not the spec's own quantifiers** ("per item", "standard condition", "same models",
"Greene subset", "both frames"). The FRUITBENCH review protocol's A1/A2 (estimand ledger +
gate-fidelity diff, quote-spec-next-to-code) catches exactly this class and took one agent
session per codebase. **Standing order for the cookbook: every gate-computing artifact gets
an A1/A2 audit by a NON-building agent before its first real run.** This generalizes the
stress-test §4 seam rule from documents to code.
