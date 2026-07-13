# WCF-Bench — Shadow Judge Bakeoff Design

**Date:** 2026-07-12

**Status:** Jimmy-approved design; implementation awaits written-spec review

**Authority:** Jimmy approved “shadow” scope and then approved this exact design with a
strict **$1.00 not-to-exceed paid-call cap** in the Codex session on 2026-07-12. No
R-number is assigned.

## 1. Purpose and non-effect

This study compares one GLM-family model and one DeepSeek-family model with the existing
Grok evidence to identify balanced *shadow* judge alternatives. It produces evidence and
a provisional recommendation for Jimmy; it does not select or install a judge.

The study has **no effect** on:

- the ratified R47.3 manifest of record;
- the R47.4 closed candidate ladder;
- the R59.4 T4 judge plan;
- any T4 SUT, item, perturbation, gate, or budget authorization; or
- any score of record, paper claim, or release label.

No qualification manifest will be emitted. Any future production-panel change requires a
separate written Jimmy ruling and, where applicable, a new manifest event and an amended
judge/SUT independence plan.

## 2. Fixed comparison set

| Role | Family | Exact OpenRouter slug | Paid in this study? |
|---|---|---|---|
| New shadow candidate | Z.ai / GLM | `z-ai/glm-5.2` | Yes |
| New shadow candidate | DeepSeek | `deepseek/deepseek-v4-pro` | Yes |
| Incumbent comparator | xAI | `x-ai/grok-4.20` | **No** — reuse immutable evidence |
| Incumbent reference | Google | `google/gemini-2.5-flash` | **No** — reuse immutable evidence |

At preflight, both paid slugs must exist in the live OpenRouter catalog exactly as written.
If either is absent, stop before the first paid call. There are no aliases, replacements,
fallback models, or additional candidates.

Pricing snapshot used for planning (verified 2026-07-12):

- [GLM 5.2](https://openrouter.ai/z-ai/glm-5.2): $0.42/M input tokens and
  $1.32/M output tokens.
- [DeepSeek V4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro): $0.435/M input
  tokens and $0.87/M output tokens.

The live catalog and response-reported actual cost govern accounting; these page prices
are planning evidence only.

## 3. Evidence design

### 3.1 Frozen qualification battery

Run the existing six probes, unmodified, for each new shadow candidate:

1. `g4`
2. `award_consistency`
3. `discrimination`
4. `disclosure_inversion`
5. `negative_disclosure`
6. `settled_core`

Use the existing qualification code and current template builders, `K=8`, threshold
`>=5/8`, temperature 0, and `max_tokens=2048`. Before any paid call, assert that the
current qualification-template hashes equal the ratified R47.3 manifest's stored hashes.
A mismatch stops the study; it is never repaired inside this lane.

The report may compute each candidate's *hypothetical* surface eligibility under the
existing `SURFACE_PROBES` mapping. It must label that result `SHADOW / NOT A MANIFEST`.

### 3.2 Real-response shadow sample

Use 32 judge units reconstructed from the immutable MVP run of record: eight units for
each of `open_award`, `disclosure`, `coherence`, and `settled_core`.

For each surface:

1. Eligible universe = persisted MVP cells for which the current prompt builder can
   reconstruct that surface's prompt and immutable Gemini/Grok comparator evidence is
   present.
2. Deduplicate by `(surface, item_id, sut_slug)`.
3. Sort by the hexadecimal SHA-256 digest of
   `"1647|<surface>|<item_id>|<sut_slug>"`.
4. Take the first eight units.

This selection is mechanical and must be persisted to `selection.json` before the first
paid call. No outcome-, disagreement-, model-, or item-content-based cherry-picking is
allowed. Each selected unit is judged once by each new candidate, for 64 planned shadow
verdicts. Grok and Gemini are not rerun.

## 4. Evaluation and recommendation contract

The report presents a Pareto table; it does not invent a weighted composite score.

### 4.1 Qualification evidence

- pass count out of 8 for every candidate × probe;
- cause tally (`pass`, `fail_substantive`, `fail_format`,
  `fail_transport_after_retry`);
- hypothetical surface eligibility under the unchanged mapping; and
- truncation and parse/willingness outcomes.

Qualification is dominant: a model cannot be recommended for a surface whose fixed probe
gate it fails, regardless of price or agreement.

### 4.2 Real-response evidence

For every surface, report:

- parseable-verdict fraction;
- exact agreement with each persisted incumbent comparator where comparable;
- the existing parser's surface-specific component agreement (for example, OPEN award
  axes or settled-core keypoints);
- disagreement counts with links/identifiers back to the persisted unit; and
- no inferential statistic beyond descriptive fractions at `n=8` per surface.

Incumbent agreement is descriptive, not ground truth. The report must not call a candidate
“more accurate” without human labels.

### 4.3 Operational evidence

- actual cost by model and phase;
- prompt/completion tokens, call count, retry count, truncations, latency, and errors;
- current OpenRouter catalog pricing captured in run metadata; and
- explicit judge/SUT family-overlap flags.

DeepSeek conflicts with the binding T4 DeepSeek SUT family. Z.ai/GLM conflicts if Z.ai is
used through R59.2's fallback roster. These are production-independence penalties, not
reasons to suppress shadow evidence.

### 4.4 Possible recommendation labels

The provisional report may use only these labels:

- `SHADOW-ELIGIBLE FOR <surface>` — the fixed probe gate passes;
- `SHADOW-INELIGIBLE FOR <surface>` — the fixed probe gate fails;
- `INDEPENDENCE-CONFLICTED` — the family is or may be a T4 SUT family;
- `INSUFFICIENT EVIDENCE` — execution or comparison data are incomplete; and
- `PARETO-PREFERRED SHADOW CANDIDATE` — qualification is no worse on the relevant
  surfaces and the model is not dominated simultaneously on reliability, cost, and
  independence.

No label authorizes production use.

## 5. Live-run safety and accounting

- New append-only run directory:
  `07-PILOTS/20260712-shadow-judge-bakeoff/`.
- Planned files: `selection.json`, `shadow-run-metadata.json`, `raw_verdicts.jsonl`, and
  `20260712-shadow-judge-bakeoff-report.md`.
- `shadow-run-metadata.json` must say `SHADOW / NOT A QUALIFICATION MANIFEST` and must not
  use a qualification-manifest filename.
- Run the mandatory OpenRouter key-limit/usage preflight without printing the key.
- Resolve both exact slugs against the live model catalog before creating paid work.
- Strict NTE: **$1.00**. The guard checks projected worst-case cost before every call and
  actual/reconstructed cost after every response. Stop before a call that could breach the
  cap.
- Persist and `fsync` every raw response and accounting record before the next paid call.
- Retry a transport failure at most twice; after that, record the error and continue where
  the design remains interpretable.
- If usage data are inadequate for actual-first or strict token-price fallback accounting,
  stop paid execution.
- No paid Grok or Gemini calls.

Historical full-battery token use suggests roughly $0.10 for both new batteries before the
32-unit comparison. Expected total is approximately $0.15–$0.30; $1.00 is the hard safety
cap, not a spending target.

## 6. Implementation shape

Make the smallest change in the existing harness style:

- one runner, `04-HARNESS/shadow_judge_bakeoff.py`;
- focused tests in `04-HARNESS/tests/test_shadow_judge_bakeoff.py`;
- reuse qualification probes, template hashes, OpenRouter client, retry/accounting guard,
  JSONL persistence, and parsers already present;
- no new dependency, abstraction layer, template, prompt, or scorer; and
- a dry-run/mock path that exercises selection, batteries, report generation, budget stop,
  and immutable-output checks without network access.

Implementation uses TDD. Required tests cover:

1. exact two-slug resolution and fail-loud behavior;
2. deterministic 8×4 selection and persisted selection-before-call ordering;
3. frozen template-hash assertion;
4. K=8 × six-probe execution for each new candidate;
5. zero Grok/Gemini live calls;
6. shadow labels and absence of a qualification manifest;
7. strict $1 budget stop and accounting failure;
8. raw-evidence persistence before the next call;
9. retry/error survival; and
10. Pareto report fields and family-overlap flags.

## 7. Done when

- The written spec has been reviewed by Jimmy.
- The focused tests and full offline harness suite pass.
- The new run directory did not exist before launch and all evidence is append-only.
- Both new candidates have all six K=8 probe results scored or error-recorded.
- All 64 real-response shadow verdicts are scored or error-recorded.
- Actual total spend is `<= $1.00`, reconciled and reported.
- The report contains the required qualification, real-response, operational, and
  independence evidence plus a provisional Pareto recommendation.
- The manifest of record, candidate ladder, T4 plan, frozen bank, prompts, templates,
  existing run directories, and scores of record are unchanged.

Once these ceilings are met, stop. Do not screen more models, add repetitions, widen the
sample, tune prompts, or iterate on a preferred candidate.

## 8. Explicitly out of scope

- Reopening the candidate ladder or changing the manifest.
- Replacing or augmenting the T4 panel.
- Changing the T4 SUT roster to accommodate a shadow result.
- New exemplars, prompts, templates, scorers, human labels, or adjudication.
- Rerunning Grok or Gemini.
- Testing multiple GLM or DeepSeek variants.
- T3, T4, G4, G6, P3, or any paper-result fill.
