# WCF-Bench Codex Session 40 Handoff — PPP-1 Catalog-Drift Gate

**Date:** 2026-07-13

**Executor:** Codex with fresh PPP-1 implementation and named-blocker review agents

**Paper milestone:** PPP-1 exploratory manuscript preview

**Spend:** `$0`; authentication/catalog metadata only, no inference

## Outcome

Jimmy authorized the wrapper-local PPP-1 interruption-custody fix. Commit `5056df116`
implements only that change and its regression. A fresh reviewer re-reviewed
only the named blocker and returned PASS. Fresh controller verification is **25/25 focused**
and **725/725 full**.

The already-authorized live command then reached only the R40.1 authentication/catalog
preflight and failed closed with exit code 2 before creating the output directory or making
an inference call. The live exact-four-row catalog hash was
`e97e482f8fc963ffe2e0743257e1d1041437ebdef1cbcf9babdb03c7b2d0318a`; the frozen hash is
`8aaf8aed304c97244239224bedd4e0677762ea1c69fa8005c429737a49b74268`.

One sanitized follow-up catalog GET localized the difference to
`qwen/qwen3.7-plus`. Its base prompt and completion prices remain `0.00000032` and
`0.00000128`; the live row adds an override beginning at `min_prompt_tokens=256000` with
prompt/completion prices `0.00000096` and `0.00000384`, plus cache fields. The other three
roster rows are identical to the frozen snapshot.

There is no PPP-1 run directory, no inference, and no paid spend. The one-run / strict
`$23.56` authority remains unconsumed. This is a new owner gate; no autonomous third
controller cycle is allowed.

## Jimmy decision required

Authorize or reject one append-only metadata refresh/re-freeze of the exact four-row
PPP-1 snapshot/hash after Codex verifies every PPP-1 prompt ceiling remains below the new
Qwen 256,000-token override threshold. The bounded recommended disposition preserves the
exact roster, base prices, 2,048/512 output caps, retry rules, strict `$23.56` NTE, and
one-run authority; no inference occurs until the refreshed hash is ratified.

Suggested exact ruling:

> I authorize one append-only PPP-1 four-row catalog refresh and re-freeze after Codex
> verifies every PPP-1 prompt ceiling remains below 256,000 tokens. Preserve the exact
> three-SUT/one-Gemini roster, base prices, 2,048/512 token caps, retry rules, one-run
> boundary, and strict $23.56 NTE. If the refreshed manifest verifies those conditions,
> execute the already-authorized paid run once, then build the exploratory manuscript
> packet. No substitutions, perturbations, gates, reruns, or T4 work.

## Files and state

- Runner fix: `04-HARNESS/ppp1_run.py`, `04-HARNESS/tests/test_ppp1_run.py`, commit
  `5056df116`.
- Execution plan: `20260713o-codex-ppp1-execution-plan.md` — Task 1 review checked;
  Tasks 2–3 remain unchecked.
- Escalation: `PENDING-QUESTIONS.md` — interruption choice resolved; catalog refresh open.
- Paid authority: `20260713n-jimmy-ppp1-paid-authorization-record.md` — unconsumed.
- Output directory: absent; do not create it before the next ratified attempt.

## Next session

On session open: load `project-dashboard.html` (Live-status first).

Read this handoff, `PENDING-QUESTIONS.md`, the authorization record, and
`20260713o-codex-ppp1-execution-plan.md`. Ask Jimmy to ratify or reject the exact catalog
refresh ruling above. Make no inference call and do not enter T4 while this gate is open.

If ratified, perform only the bounded offline ceiling verification and append-only
four-row snapshot/hash refresh. If all conditions match the ruling, execute PPP-1 once
under the existing authority and immediately build the labeled exploratory manuscript
packet. Stop for Jimmy review.

On session close: update the dashboard per `AGENTS.md §The project dashboard`, then
open/reload it in the browser and leave the verified next-session view open for Jimmy.

## Session allocation

Empirical execution 0% · paper work 0% · infrastructure 35% · governance/admin 65%.
The named custody blocker closed, but the fail-closed catalog preflight surfaced a new
owner-gated metadata-identity change before any paid inference.
