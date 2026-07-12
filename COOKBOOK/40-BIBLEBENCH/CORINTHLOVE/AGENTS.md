# CORINTHLOVE Agent Instructions

These rules govern work under `CORINTHLOVE/`. Dated handoffs and reviews are
archival evidence; they do not define the active queue.

## Scope and precedence

Work only on the 1 Corinthians 13 CORINTHLOVE benchmark family. Do not open or
borrow from sibling benchmarks under `40-BIBLEBENCH`.

When instructions differ, use this precedence:

1. Current user instruction.
2. `CORINTHLOVE/STATUS.md`.
3. The approved consolidated design, or the selected module brief under
   `CORINTHLOVE*/DESIGNS/` once implementation resumes.
4. `CORINTHLOVE/RUNBOOK.md`.
5. Archived reviews, dated handoffs, and next-session prompts.

`STATUS.md` must name exactly one active workstream, one current blocker (or
`none`), and one next action. Work in progress is limited to one approved
milestone or method module.

## Current consolidation gate

The standalone bank queue was retired on 2026-07-11. The consolidated design
and offline Tier-0 implementation plan are approved. Tier 0 may create only the
new consolidated root and its read-only contracts, adapters, snapshots,
synthetic analysis, tests, and documentation. Do not start another method bank,
create a fresh live root, or resume the archived CROSSROADS v6 sequence.
Preserve DIMGLASS, CHARITROC, and CROSSROADS as independently verifiable method
modules.

## Module delivery discipline

Once an approved consolidated plan selects a method module, the primary outcome
is to complete that bounded module, obtain only the authorized evidence, make
no more than one evidence-supported revision cycle, and return to the
consolidated milestone rather than automatically advancing a bank queue.

Use this sequence:

1. Build generator-based bank artifacts and pass focused offline tests.
2. Run live catalog and access qualification.
3. Run the four-cue public canary.
4. Run the public smoke.
5. Analyze saturation, discrimination, stage-3 updating, cue effects, and
   judge-ID leakage.
6. Apply only a localized, evidence-supported revision.
7. Verify, review, hand off, and update `STATUS.md` to the next approved
   consolidated milestone.

Once focused tests pass, do not add speculative harness invariants before the
first live access probe. A new invariant requires either a binding written
requirement or a reproduced failure artifact.

## Testing policy

- Write a focused failing test before a behavior change.
- Use focused tests during implementation.
- Before review, render and read at least 20 exact candidate payloads spanning
  the declared families. Schema-green output is not sufficient: reject visible
  authoring IDs, broken grammar, and any tool/operation whose real-world role
  disagrees with the action plan or claimed effect. Add a regression for every
  demonstrated sample-audit defect.
- Run the expensive full suite once before live execution and once at final
  verification.
- Do not rerun a long suite for documentation-only or unrelated changes.
- Use fresh-process verification for every live checkpoint.
- Never label mock output as a measurement. The exact mock label is
  `harness validation, NOT a measurement`.

## Live-failure policy

Preserve the artifact and classify the failure before changing code:

- `provider_capacity`: retry only through the explicit durable retry path;
- `protocol_compatibility`: reproduce offline, add a focused test, then fix;
- `integrity`: do not retry until the failed invariant is understood;
- `benchmark_content`: localize by cue, truth, family, position, or ID surface;
- `infrastructure`: resume from the durable checkpoint.

Fix only the demonstrated class. Do not relax Azure, ZDR, no-fallback, exact
snapshot, public-only, secret-containment, or ground-truth boundaries to make a
run pass.

Current OpenRouter authorization is cheap-model qualification only. Do not run
GPT-5.4 full, GPT-5.5, GPT-5.6 Sol, or any other flagship/frontier model unless
the user explicitly changes that instruction. GPT-5.4-mini is authorized only
through its frozen public-only qualification profile.

## Redesign policy

- Do not rewrite items from aggregate accuracy alone.
- Require a localized cue, truth, family, position, or identifier artifact.
- Treat the 12-item public split as qualification evidence, not calibration,
  final model ranking, or family-level inference.
- Separate stage-3 belief, action, and joint updating in diagnostics. Do not
  interpret a protective action with uncertain intent as proven belief failure
  without construct evidence.
- Preserve passing cue counterbalancing, but never treat surface-count balance
  as sufficient when a semantic decoder succeeds. Keep deterministic authoring
  seeds (`JSEED`), random per-scoring-occurrence tokens (`JCASE`), and immutable
  judge identities (`JUDGE`) as separate namespaces; bind judge family, exact
  model or human class, prompt, configuration, and role through the frozen
  roster rather than a self-declared rating field.

## Completion criteria

An implemented method module is complete only when all of the following hold:

- every declared design cell is covered with fail-loud assertions;
- paired arms use matching defeat classes;
- the offline suite passes;
- the requested live cheap models have verified access and public-smoke
  evidence;
- no secret, canonical item ID, judge ID, canary, or hidden ground truth reaches
  the model-visible payload;
- the candidate-payload sample audit finds no authoring identifiers or
  tool/plan semantic mismatch;
- saturation/discrimination and stage-3 behavior are diagnosed;
- the adversarial review has an acceptable verdict;
- a dated handoff contains exact verification output;
- `STATUS.md` advances to the next approved consolidated milestone.

Do not commit, push, delete, or broaden scope unless the user explicitly asks.
If an obsolete artifact must be removed from active use, preserve it in the
appropriate recycle/archive location rather than deleting it.
