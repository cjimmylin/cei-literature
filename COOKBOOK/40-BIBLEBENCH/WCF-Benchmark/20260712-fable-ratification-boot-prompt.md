# WCF-Bench — Next-Session Boot Prompt (Fable ratification + OPEN-surface adjudication; paste after /model fable + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are a
**Fable adjudication session** (judgment only — ratify/overrule, no building; builds go
back to Codex). This prompt SUPERSEDES `20260711-fable-next-session-boot-prompt.md`: since
it was written, **Codex executed Tasks 1–4 on the branch `codex/wcfbench-mvp-testable`**
(14 commits, unmerged) and the Task-4 format-bridge requalification produced the
**unanticipated worst case — ZERO OPEN-award-eligible families** (gemini award-consistency
0/8 under the bridged template, grok 0/8, cohere/nova no pass). The 204 OPEN items are
currently unscorable under the manifest of record; "MVP testable" needs a ruling, not a
workaround. That is this session's headline.

## Step 0 — load state (NOTE: most evidence lives on the CODEX BRANCH, not main)

1. **Open `project-dashboard.html`** — but note the branch carries a NEWER dashboard than
   main (Codex updated it through S20); read the branch version for current state:
   `git show codex/wcfbench-mvp-testable:COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/project-dashboard.html`
   (or check the branch out read-only). Reconciling the two dashboards is agenda item 5.
2. `git log main..codex/wcfbench-mvp-testable --oneline` (expect ~14 commits) +
   `git diff main...codex/wcfbench-mvp-testable --stat`.
3. Read, in order (all on the BRANCH unless noted):
   a. `20260711d-codex-session-handoff.md` → then c, b, a (newest first).
   b. `PENDING-QUESTIONS.md` — contains questions AND interim rulings marked
      "Rulings received 2026-07-11" / "RESOLVED". **Verify provenance of every recorded
      ruling** (Jimmy-issued → integrate + ratify; Codex-suggested defaults → decide fresh).
   c. `20260711-codex-provisional-adjudication-recommendations.md` — Codex's non-binding
      packet (R47+ numbers reserved, not assigned). Treat as INPUT, never as precedent.
   d. `07-PILOTS/20260711-format-bridge-requal/` — report, canonical manifest,
      `raw_verdicts.jsonl` (sample-read the gemini/grok award-consistency 0/8 evidence
      yourself — do not take the table's word for the headline ruling).
   e. `20260711-fable-ratification-next-session-boot-prompt.md` — Codex's suggested
      agenda for you. Useful; not binding.
   f. On MAIN: `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46) — your
      own binding baseline; nothing in it is relitigated, but R44.5's "zero passes"
      clause anticipated google SURVIVING — the actual outcome is outside its text.

## Agenda (priority-ordered; write ONE binding memo, R47+, new dated file)

**1. THE HEADLINE — rule the OPEN-award surface's status.** Under the bridged manifest no
family is OPEN-eligible; under the pre-bridge manifest gemini was eligible but that
manifest is superseded and the templates differ. Decide, at minimum:
   (i) whether the bridged manifest stands as the manifest of record (the interim ruling
   says keep + ladder CLOSED — ratify or overrule, with the raw evidence read);
   (ii) what the OPEN surface's operational state is until G6 (e.g., SUSPENDED —
   unscorable, reported as such; vs. a ruled, labeled legacy path; beware: restoring
   stale eligibility was already declined in the interim ruling);
   (iii) what "Milestone A / MVP testable" now MEANS — redefine the finish line honestly
   (e.g., all surfaces except OPEN scorable + OPEN status ruled + G6-anchored
   requalification path pre-registered) and update the execution plan/dashboard wording;
   (iv) whether the bridged-template award-consistency probe itself is implicated (a
   0/8 from BOTH incumbents on one probe, with g4/discrimination 8/8, may indicate the
   probe–exemplar interaction, not judge failure — decide if a probe-validity read is
   warranted BEFORE condemning the surface; that read is sample-level, from
   `raw_verdicts.jsonl`, no live calls).
**2. Ratify or revise Codex's Task 1–4 work** against the Done-when specs (spot-check:
parse-fix fixtures, eligible spreads, cost reconciliation, requal runner + report
immutability). Assign the reserved R-numbers in your memo.
**3. Rule Task 5 (EPISODE).** The 22 EPISODE items have no executable spec registry;
Codex drafted `04-HARNESS/config/episode-spec-registry.draft.json` under an authorized
draft-only ruling. Decide: approve/amend the registry path, who authors the per-item
specs (fabrication-sensitive — same class as bank transcription), what review gate it
needs, and whether Task 5 stays blocked pending that work.
**4. Rule Task 6 disposition** per the packet (PROOF judge-assisted re-read under which
manifest, given item 1's outcome).
**5. Merge + reconcile.** After ratification: direct the merge of
`codex/wcfbench-mvp-testable` → main (or perform it: `git log -1` first, fast-forward
push, explicit awareness that the branch's dashboard version wins reconciliation —
merge the two dashboards' LIVE surfaces into one truthful current state, preserving both
update logs).
**6. Only if the queue clears:** the gated G1–G7 run pre-registration (agenda item 2 of
the superseded 20260711 prompt — its spec text remains valid), now REQUIRED to account
for the OPEN-surface ruling from item 1.

## Guardrails

Adjudication only — no code, no live calls, no gold minted, no item edited, no G6
activity. Report immutability (the requal report/manifest/raw_verdicts are immutable
records regardless of ratification outcome; new dated memo only;
`project-dashboard.html` is the sole undated exception). Canary
`WCFBENCH-CANARY-c1647-x9k4q` never re-minted. Shared git index LIVE (`git log -1`
before every commit; explicit paths; never `git add -A`). Secrets not needed. Sibling
benches read-only precedent at most.

## On session close (mandatory)

1. **Update `project-dashboard.html`** (post-merge, the reconciled one): last-updated
   line, Live-status (incl. the OPEN-surface status + redefined Milestone A), progress
   bars, S-row(s), checkboxes, quotability panel + gate board + judge table (item 1
   changes them), contingency statuses (format-bridge row FIRED — record the outcome),
   update-log line, **and rewrite §Instructions for next session**.
2. Update the `wcf-bench-portfolio-state` memory note; write the next boot prompt
   (dashboard open/close lines per AGENTS.md convention) + a dated session handoff;
   commit + push explicit paths.

> Fallback: if the Fable window has lapsed, run this same boot on **Opus** but DOWNGRADE
> to descriptive mode: catalog the evidence, verify provenance of interim rulings, and
> produce RECOMMENDED dispositions with R-numbers still reserved — binding only after
> Jimmy or a Fable pass ratifies. The merge (item 5) may still be executed if and only
> if Jimmy approves it in-session.
