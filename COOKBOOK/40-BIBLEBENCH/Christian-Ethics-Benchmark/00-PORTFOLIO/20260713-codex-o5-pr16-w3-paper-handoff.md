# WALKWORTHY O5 — PR-16/FR-7 + W3 + first PAPER fill complete

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13. **Agent:** Codex. **Scope:** WALKWORTHY only.
**Status:** W1, W2, PR-16 FR-7, W3, and the first licensed paper fill are complete.
W4 G5 is next, followed by W5 G7. This file is dated-immutable.

## Completed

- Logged Jimmy's PR-16 option-1 ratification verbatim and closed PR-16.
- Built `harness/walkworthy/home_reroute.py` under TDD and two independent reviews.
  It pins the authorized W1 source; restricts PUBLIC run paths; validates exact source,
  checkpoint, event, model, and score provenance; proves nonselected invariance; and
  locks a completed derived run against overwrite.
- Produced `runs/20260713-o5-home-reroute/`: 2,064 unique records; 63 units / 249
  cells; 11 reused + 52 new Mistral calls; 245 resolved; 4 Part B; 0 defects; 11
  PR-15 overlaps superseded; post-reroute unresolved surface 1,174 cells; incremental
  cost $0.0534336 (105,240 prompt + 2,016 completion tokens).
- Extended W3 to require the exact 63-event surface and cross-check every replacement
  value against the unique persisted OpenAI verdict and matching persisted Mistral
  event. Final suite: 344/344.
- Published immutable W3 source of record:
  `00-PORTFOLIO/20260713b-o5-postadjudication-readings.md`. The earlier
  `20260713-o5-postadjudication-readings.md` is retained as the immutable snapshot with
  a stale Next paragraph and is superseded by `20260713b`.
- Mechanically filled only licensed surfaces in `PAPER/06-results-scaffold.md`:
  Table 6.1, Table 6.2 G1–G3 statistics, FR-10 sensitivity disclosure, and Table 6.4.
  Only design 05 receives PASS/FAIL interpretation because it alone currently meets
  FR-1 across all six SUTs; other designs show numbers with `FR-1 N` and no verdict.
- Wrote the claims-conformance checklist and an Opus adversarial-review request. Opened
  PR-17 for the standing prompt's required routing ratification; no Opus memo or Jimmy
  acceptance is claimed.

## Paper-facing result

The paper now contains corrected post-adjudication descriptive statistics rather than
the inherited pre-W1 readings. FR-5 is confirmed. Both mandatory G9 vectors are filled.
Design 10's strict-identity sensitivity flips G1 PASS→FAIL and G2 FAIL→PASS; this is
disclosed, while the already-ratified PR-6 registered rule remains the headline rule.
G4/G5/G6/G7, all new statuses, §6.3, §6.5, §6.6, discussion, and abstract remain
unfilled because no current artifact licenses them.

## Jimmy inputs

1. Recommended PR-17 one-liner:
   `Ratify paper claims review routed Opus memo → Jimmy per
   20260712-codex-paper-fill-boot-prompt.md (master-plan §5 conditional; Fable window
   closed).`
2. Part-A labels: 0/439 (release critical path), then Part-B labels.
3. Later release sign-off.

PR-17 does not block W4/W5.

## Next session — W4 G5 → W5 G7

On session open: load `00-PORTFOLIO/project-dashboard.html` (Live status + §12 first),
then this handoff, `AGENTS.md`, the transition package W4/W5 specs, FR-18, PR-10, and
PR-11. Do not rerun or overwrite W1/W2/PR-16/W3.

Execute W4 G5 for 06/09 with the promoted reference sets and explicit judge models,
then W5 G7 with the versioned L7 mapping and registered perturbation mechanics. Use
cheap models only for tests; production measurement models must be the registered
explicit slugs. If labels remain absent after W5, stop at Phase-1-complete and report
`O5 blocked on labeling`; do not assemble release verdicts.

On session close: update the dashboard per `AGENTS.md`, write a NEW dated handoff,
verify, commit, and fast-forward push WALKWORTHY paths only.

## Browser note

The dashboard was updated in place. The in-app browser refused the local `file://`
dashboard under its URL security policy and explicitly prohibited workarounds, so no
visual-browser verification was possible. Use the direct local dashboard link from the
session response.
