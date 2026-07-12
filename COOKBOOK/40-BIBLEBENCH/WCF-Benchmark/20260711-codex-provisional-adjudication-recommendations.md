# WCF-Bench — Provisional Adjudication Recommendations

**Status:** PROVISIONAL — pending Jimmy ratification. This document assigns no binding
ruling numbers. The next R47+ slots remain reserved.

**Scope:** Agenda item 1 from `20260711-fable-next-session-boot-prompt.md`: spot-check the
completed Task-4 manifest event and catalog the remaining Task-5/Task-6 questions. No live
calls, bank edits, prompt changes, manifest changes, or G1–G7 pre-registration were made.

## Recommendation A — ratify the Task-4 execution outcome

**Recommended disposition:** Ratify the immutable Task-4 run as compliant with R43/R44 and
retain its manifest as the manifest of record. Confirm the already-issued Jimmy ruling to
keep the manifest and close the pre-G6 OPEN-candidate ladder. Do not restore stale OPEN
eligibility, revise the exemplar, rerun the battery, or screen another candidate.

Evidence spot-check:

- The exemplar is frozen in `probe_fixtures.py`, appears once in each award prompt, is
  included in both award-template hashes, and is neutral/non-bank by its regression test.
- The incumbent roster is exactly Gemini Flash and Grok 4.20; GPT is absent. Both received
  the full K=8 battery with an unchanged pass threshold of 5/8.
- The OPEN candidate roster is exactly Grok 4.20, Cohere Command A, and Amazon Nova Pro.
  Cohere and Nova received K=8 G4/coherence, award-consistency, and discrimination probes;
  Grok's full incumbent battery was reused rather than rerun.
- The discrimination bar was not relaxed. Results were Gemini 8/8, Grok 0/8, Cohere 0/8,
  and Nova 1/8. Gemini and Grok also scored 0/8 on award-consistency; consequently no judge
  is OPEN-eligible.
- The manifest records only live Task-4 counts, matches the current template hashes, and
  constructs an offline `JudgePanel` with Gemini and Grok active across two families for
  coherence, disclosure, and settled-core. Its OPEN-eligible set is empty.
- The raw evidence contains 297 completed invocations. Four recorded Cohere transport
  errors occurred within three invocations; all three ultimately succeeded within the
  fixed retry limit. There are no unresolved invocations.
- The report reconciles internal cost `$0.4878` against key-side delta `$0.4873`, within
  the required ±20% and below the `$10` cap.
- Focused verification: `tests/test_format_bridge_requal.py` passed 19/19 offline.

Canonical immutable evidence:

- `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-report.md`
- `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-manifest.json`
- `07-PILOTS/20260711-format-bridge-requal/raw_verdicts.jsonl`

**Clarification for ratification:** R44's anticipated zero-candidate branch described OPEN
as remaining Google-single-family. The observed full requalification also removed Gemini's
OPEN eligibility, leaving zero OPEN-eligible judges. Jimmy has already resolved that
unanticipated state by directing the project to keep the new manifest and close the ladder.
Ratification should preserve that exact outcome, not rewrite it as single-family OPEN.

## Recommendation B — keep the Task-5 registry human-review-gated

**Recommended disposition:** Accept the draft as the authorized review artifact only. Do
not approve or activate its 22 item-level mappings by inference. A human reviewer should
approve or correct each mapping and explicitly change its governance status before any
runner may consume it outside review mode.

Evidence spot-check:

- `04-HARNESS/config/episode-spec-registry.draft.json` contains all 22 frozen EPISODE item
  IDs and is marked `DRAFT_UNAPPROVED`.
- `wcfbench/episode_registry.py` exposes it only through the explicit review-mode seam.
- `tests/test_episode_registry.py` and `tests/test_judge.py` passed 38/38 offline. These
  tests establish schema/code behavior, not theological or mechanical approval of the
  item mappings.
- The paid-call pause independently prohibits the 88-cell Task-5 run. Task 5 therefore
  remains unchecked.

Human review should return one of two bounded outcomes per entry: `approve as drafted` or
`correct with replacement fields and rationale`. The review must not edit bank YAML.

## Recommendation C — keep Task 6 blocked under the ruled scorer contract

**Recommended disposition:** Preserve the current citation-gated
`judge_score_anchor_use` contract exactly as ruled. Do not weaken the citation gate, alter
the prompt, or alias anchor use to an existing manifest surface. Keep Task 6 unchecked.

Two independent blockers remain:

1. The Task-4 manifest defines qualification only for OPEN award, disclosure, coherence,
   and settled-core. It contains no anchor-use surface or template hash, while OPEN has no
   eligible judge. Selecting a surface would be a new judgment ruling.
2. Under the fixed citation gate, an uncited paraphrase never reaches a judge. The plan's
   required uncited-paraphrase recovery fixture and expected floor rise are therefore
   incompatible with the ruled scorer contract as written.

The next binding adjudication should choose one explicit path:

- **Recommended conservative path:** revise Task 6's acceptance criteria to match the
  citation-gated construct and separately specify a qualified scoring surface before any
  persisted re-read; or
- authorize a new anchor-use qualification surface and manifest event. This is broader
  and must not be inferred from the current plan.

The paid-call pause prohibits either live path until separately lifted.

## Ratification checklist

Jimmy/Fable should record binding R47+ rulings only after deciding these boxes:

- [ ] Ratify Task 4 as compliant; keep the 20260711 manifest; zero OPEN eligibility is
  explicit; candidate ladder remains closed.
- [ ] Keep the EPISODE registry `DRAFT_UNAPPROVED` pending item-level human review, or
  attach the completed review corrections/approval.
- [ ] Specify Task 6's qualified surface and reconcile its acceptance criteria with the
  citation-gated contract, or formally defer Task 6.
- [ ] Keep the paid-call pause in force, or separately authorize an exact bounded run.

Until those decisions are recorded, the execution strategy remains offline-only: no paid
calls, no Task-5/Task-6 checkbox changes, and no G1–G7 run pre-registration presented as
binding. Once Agenda item 1 is cleared, the next judgment-tier deliverable is the G1–G7
pre-registration described by the Fable boot prompt.
