# Inspect-fit assessment — WALKWORTHY v2 parallel experiment (2026-07-15)

**Purpose.** Deliverable for the "parallel experiment first" ruling (2026-07-15 grilling,
round 2): does Inspect AI fit WALKWORTHY well enough to become the canonical execution
path, superseding the v1 custom harness? This memo is the evidence base; the ruling
itself remains with Jimmy.

**Evidence produced today.** 344-item public parity with the v1 O4 manifest (exact,
pre- and post-review conversion); 10/10 designs green under mockllm on real datasets;
10/10 designs green on a live OpenRouter smoke (deepseek-chat SUT × gpt-4.1-mini judge,
~2 samples/design) at **≈ $0.038 total spend**, judge JSON parseable on every scored
sample, zero provider failures, zero 402s.

## 1. What Inspect covered natively (v1 pain points eliminated by construction)

| v1 pain | Inspect answer |
|---|---|
| PR-9 transcript loss (cost a $27 re-execution of 02/07) | `.eval` logs persist every message of every sample automatically, including the 17-message design-02 ladders — verified in mock and live logs |
| Custom checkpoint/resume/panel runner (panel.py, ~heavy) | built-in retry/resume, `--max-connections`, eval-set over 10 tasks |
| Per-vendor adapter code + OpenRouter backend module | `openrouter/<slug>` provider strings; one env var |
| Cost tracking | token usage in every log; `inspect view` / VS Code extension (Antigravity) to browse |
| Mock dry-run driver (smoke.py, mock plumbing) | `--model mockllm/model` end-to-end, zero cost |
| Cross-family second judge required re-running SUTs in v1 mindset | judge is a task arg; `inspect score` re-scores saved transcripts — second judge costs judge-tokens only, no SUT re-execution |

## 2. What needed custom code (moderate, one-time, now written)

- **Administration expansion + paired metrics.** WALKWORTHY's unit is the
  administration; pairing (say/do, covert/overt, seats, twins) lives in `pair_id`
  metadata and custom metrics group by it. ~expected work, done in `metrics.py`.
- **Multi-turn branch-ladder solver** for 02/07 with a judge-backed mid-solver state
  classifier (`get_model()` call). Custom, but the transcript comes free.
- **Per-design model-graded scorers** embedding v1 rubrics verbatim, dict-valued
  category scores, refusal-taxonomy preprocessing.
- **Design-05 judge-free parser scorer** — v1 `ordo_constraints.py` vendored verbatim;
  CSR verified on real items with synthetic compliant answers (0.5/0.8/1.0).
- **Holdout guard** — Inspect has no native holdout concept; `WALKWORTHY_ALLOW_HOLDOUT=1`
  env guard replicates v1 HoldoutAccessError.

## 3. Friction points (real, none fatal)

1. **Dict-valued scores vs scalar headline.** Inspect warns "Unable to convert value to
   float" and defaults the headline scalar to 0.0 when a Score is a category dict.
   Per-design custom metrics report correctly; anyone reading the default header
   number without the metrics table will be misled. Mitigation: documented; could add
   a scalar `value` alongside the dict per design.
2. **`--limit` can split administration pairs.** Sample-level limits don't know about
   `pair_id`; pilots should use limits in multiples of the design's admin-group size
   (or filter by item ids). Fine for smokes; matters for real pilots.
3. **Simultaneous 2-judge + disagreement-cell adjudication protocol is not native.**
   The v2 path is: run once → `inspect score` with judge B → offline disagreement
   comparison (the W1-style logic becomes an analysis script over two log sets).
   Acceptable, arguably cleaner; but the v1 in-band `needs_adjudication` logging has
   no direct equivalent yet.
4. **G-gates stay external.** G5 neutrality, G7 perturbation, home-advantage detection
   remain offline analyses over logs — same as v1, where they were scripts anyway.
5. **Latent parser edge (pre-existing, carried from v1):**
   `parsers.py::reparse_allocation_response` logs `allocation_ok=True/values={}` on a
   block-less answer. Flagged in the smoke report; follow-up parser pass recommended.

## 4. Assessment

Inspect fits WALKWORTHY **well**. Everything that made v1 execution operationally
painful is either native in Inspect or strictly smaller in v2 (the custom surface
shrank from ~32 modules + 66 test files to 8 package modules + 11 task files + 2 tools).
The measurement-defining intellectual assets — item banks, rubrics, refusal taxonomy,
CSR comparator — transferred verbatim. Nothing in the v1 design proved inexpressible.

**Recommended preconditions before a canonical-path ruling:**
1. Comparability check: run a small overlapping slice (e.g. the MVP-A1 60-item subset)
   on both harnesses with the same SUT and one shared judge; confirm score agreement.
2. Validate the 2-judge re-score path end-to-end (judge B re-score + disagreement
   script) on that same slice.
3. Close the design-07 matched-quality reference answers residual and the parser edge
   (§3.5).

Until then, v1 remains canonical (paper v0.1 thread, G4 label pass unaffected).

## 5. Carried open items

Design-06 spec-exemplar review_status stamps (cosmetic) · design-07 harness-side
reference answers · parser edge §3.5 · dict-score scalar headline (§3.1) ·
pair-aware limiting helper (§3.2).
