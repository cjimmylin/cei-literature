# WCF-Benchmark-v2 — Session 21 Boot Prompt (next-direction decision)

> Paste as the opening prompt of a fresh session. Authored 2026-08-06 at the
> owner's request, while other priorities were being worked — no execution
> happened between s20's close and this prompt being written; state below is
> unchanged from s20. Orient via `INDEX.md`, then read this file in full
> before touching anything. **This session's first job is a decision, not
> execution** — see §2.

## 0. Verified state entering s21 (unchanged since 2026-07-31)

- **The project's first accepted deliverable exists and is closed out.**
  `reports/20260731-session20-v1x-paper-draft.md` — a venue-generic v1.x
  paper (no target venue, DOI, or author list) drafted from the project's
  first-ever quotable results. **The owner reviewed it and accepted it
  without requesting revision** (2026-08-06 context: confirmed via the
  owner's own "move forward" instruction after review). A 12-page PDF was
  built from it: `reports/20260731-session20-v1x-paper-draft.pdf`
  (gitignored, disk-only, rebuildable via `reports/20260731-session20-build-pdf.py`).
- **Verify before trusting this file**, the same discipline used at every
  prior handoff in this project: `git log -1 -- COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/`
  from the `CEI-Lit-WS/` repo root should show `1443e2d0d` or later, dated
  2026-07-31, as the last commit **touching this folder specifically** — the
  repo's overall `HEAD` will be newer and unrelated (other sub-projects,
  e.g. WALKWORTHY, share this trunk and commit independently; do not read
  `git log -1` with no pathspec as this project's state). `git status --short`
  from repo root should show nothing under this folder unless you have new
  uncommitted work.
- **What the paper establishes** (all traced to
  `reports/20260731-session19-quotable-results-report.md`, the project's
  only quotable source): a completed 5-SUT × 345-item × 3-epoch run
  (5,175 responses) under the frozen strict-v2 dual-judge instrument
  (ICC(2,1)=0.985), gated by a mandatory judge-gap triage (90% of sampled
  high-disagreement cells are idiom-driven, not genuine judge disagreement).
  Headline: a three-tier ranking, {gpt-5-mini, minimax-m3, qwen} tied-top
  (not significantly distinguishable from each other) > haiku > gpt-4o-mini;
  the bank's 146-item frontier-core generalizes its difficulty across the
  whole roster (11–21 pt gap for every SUT, not just the two it was
  authored against). Six disclosures plus the strict-v3 rejected-candidate
  episode are carried in full in the paper's own Limitations & Methods
  Integrity section — read that section rather than re-deriving disclosure
  language from memory.
- **Bank state:** v2.5, frozen, 345 scored items (345, never 317 — see the
  paper §2 for the corrected-count disclosure), 22 episode items still out
  of Scenario-A scope throughout.
- **Nothing has executed in this project since s20 closed.** No new
  judging, no re-triage, no bank changes, no PDF re-render.

## 1. Tiering (unchanged)

Main loop: decompose, adjudicate, adversarial review, final synthesis.
Delegate drafting/formatting/mechanical work down-tier per
`.claude/agents/` (root vault) — `manuscript-drafter` (opus) for prose from
a spec, `pdf-builder` (sonnet) for renders, `stats-runner` (sonnet) for
any fresh computation. Pass `model` explicitly on every dispatch (the
global tiering hook checks `tool_input.model`, not agent frontmatter).

## 2. Mission: this session starts with a decision, not a task

**No next task has been chosen.** At s20's close the owner was told "the
next step is the owner's to name," and as of this prompt being written,
it hasn't been. Do not default to any of the options below on your own
initiative — surface them, and any others you notice, and let the owner
choose before doing substantive work. This is exactly the
"informational-question-is-not-an-execution-authorization" pattern this
vault tracks generally: being asked to boot this project back up is not
the same as being told which direction to take it.

**Candidate directions** (not a ranked recommendation — present as options):

1. **Target-venue selection & submission prep.** The paper is
   intentionally venue-generic v1.x right now (no venue, no DOI, no author
   list, per binding directive carried from s19→s20). If the owner wants
   to move toward an actual submission, that's a new, explicit decision —
   it was deferred, not ruled out.
2. **Scale up the SUT roster.** Add more/premium models for a follow-on
   measurement under the same frozen instrument — the current 5-SUT roster
   was a deliberate scope, not a ceiling on what the harness can run.
3. **A small rubric-clarification pass.** The MEND-N-018 self-contradiction
   (item's partial-credit note vs. its GATE clause disagree by 40 points
   for the identical case; found in s19's judge-gap triage, disclosed but
   explicitly not fixed in s19 or s20) is a scoped, bounded fix if the
   owner wants it done. Out of scope unless explicitly authorized — do not
   fold it into a larger rubric review.
4. **Resolve a documentation gap.** The paper's Benchmark Composition
   section carries one open `<!-- VERIFY -->` comment: the T2a/T2b tier
   sub-band split is used consistently in the schema and in prior project
   material but its exact semantic distinction (beyond both sitting at
   tier 2) was never found documented. Minor, but worth closing if anyone
   is touching that section again.
5. **Investigate the open scientific question the paper explicitly leaves
   unresolved:** does the top-tier tie (gpt-5-mini/minimax-m3/qwen — not
   significantly distinguishable at n=345) reflect a genuine shared
   capability ceiling, or a ceiling in the current bank? The paper states
   this is out of scope for it; resolving it would need new measurement
   (e.g., harder frontier-core items, or a different discriminating design)
   — a nontrivial new work item, not a quick follow-up.
6. **Treat WCF-Bench-v2 as complete for now and park it.** The project has
   a shipped, accepted, quotable paper — that may be a legitimate stopping
   point if other priorities are more pressing. If so, say so explicitly so
   this file can be updated to reflect "parked," matching how other
   projects in this vault (e.g. COOKBOOK core) get formally parked with a
   dated re-entry pointer rather than left ambiguous.

Once the owner picks a direction (or names something not listed here),
that becomes this session's actual scope — treat everything above as
context, not a queue to work through in order.

## 3. What NOT to do until direction is chosen

- Do not start new judging, re-triage, or any bank/instrument change.
- Do not edit `reports/20260731-session20-v1x-paper-draft.md`'s substance —
  it's an accepted, closed artifact. If a revision is ever authorized,
  supersede it with a new dated file rather than editing in place, per this
  project's report-immutability convention (see s9's `.master.md`
  tree-hygiene precedent for what NOT committing intermediate/mutated
  artifacts looks like in practice).
- Do not pick a venue, mint a DOI, or draft an author list on your own
  initiative — all explicitly deferred, not decided.
- Do not re-render the PDF unless the source `.md` actually changes.

## 4. Standing flags + safety (HOOK-ENFORCED; apply to subagents)

Bank v2.5 FROZEN, scored bank 345, episodes (22) OUT. No deletions (`mv` →
`RECYCLE-BIN/`). Report immutability (new `YYYYMMDD-` files, never edit an
existing dated report/paper in place). Deletion-guard scans whole command
strings — rephrase, don't fight it. pytest baseline 137 passed + 1 known
env failure (`test_frontier_core_task_size`) —
`.venv-v2/bin/python -m pytest tests/ -q` — re-check if you touch `src/` or
`analysis/` for any reason.

## 5. Close-out (once this session's actual scope is decided and done)

Commit is owner-gated — explicit pathspecs (never `git add -A`), write the
commit message to a file, `git commit -F <file>` (never pipe `git commit`),
verify with `git log -1 --stat`, `pull --rebase --autostash` → push →
`git rev-list --count origin/main..HEAD` == 0. Update `INDEX.md`'s current-
state line. Memory: new session checkpoint pointing at
[[20260731-wcf-v2-s20-paper-draft-landed]] with the outcome. Only write a
session-22 boot prompt if this session's chosen work actually lands
cleanly — and if the owner parks the project (option 6 above), write that
outcome into `INDEX.md` explicitly rather than leaving the next entry point
ambiguous.
