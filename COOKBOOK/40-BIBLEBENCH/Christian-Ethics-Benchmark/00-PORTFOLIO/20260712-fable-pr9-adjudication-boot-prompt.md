<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Definitive boot prompt: next Fable session (PR-9 adjudication + ratification sweep)

**Staged:** 2026-07-12 by Claude (Fable). **Supersedes** the operational state of
`20260711i` (pre-Grok, mine) and `20260711m` (post-Grok, Codex's draft) — both remain as
immutable records. Additions over `m`: authority check (Fable-vs-Opus), delegation
discipline, the ratification sweep while Jimmy is present, and the full closing
obligations (§12 replacement + memory). Paste the block below with **Jimmy present**.

---

```text
New Fable session (fresh context): WALKWORTHY — PR-9 ADJUDICATION (post-Grok) +
RATIFICATION SWEEP. Jimmy must be present. SCOPE LOCK: work ONLY inside
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/ — no sibling benches.

AUTHORITY CHECK FIRST: confirm you are actually running on Fable (claude-fable-5).
If NOT, say so and downgrade the session: record Jimmy's rulings verbatim and write
the mechanical Codex orders, but do NOT issue the delegated FR-16 ruling yourself —
master-plan §1/O5 delegates rulings to Fable windows or Jimmy; on a lower tier, put
the FR-16 question to Jimmy directly and log his answer. Keep judgment in the main
loop; delegate any heavy read/search/draft to an Opus subagent with explicit
model=opus — never fan out Fable agents.

ON OPENING (dashboard protocol): read 00-PORTFOLIO/project-dashboard.html (Live
status, rulings ledger, contingencies C-1..C-15, §12) and the NEWEST dated handoff in
00-PORTFOLIO/ — the state may have moved past this prompt (Codex sessions land
frequently); verify what exists and SKIP anything already ruled or moot. Then read
yourself (all short): PENDING-RULINGS.md (PR-9 incl. the quantified evidence append),
20260711l-codex-pr9-decision-evidence.md, 20260711n-codex-pr9-decision-support-handoff.md,
20260711d-fable-o5-decision-framework.md §2+§6 (FR-1..FR-15 + STOP triggers), AGENTS.md.
FROZEN — interpret but NEVER rewrite: 20260710-fable-gate-prereg-pilot-adjudication.md
§B/§C/§E and FR-1..FR-15.

STATE ALREADY ESTABLISHED — DO NOT REDO:
- O5 Phase 0 complete; suite 276 green. Forward transcript persistence FIXED for
  future runs; the historical O4 run still lacks 723 of 907 required 02/07 turn
  responses.
- Grok-4 reliability probe already RAN and FAILED (0/10, HTTP 404). STOP trigger 8 is
  active. Never re-probe, never ask about re-probing.
- Quantified decision surface (Codex, verified twice): current selector = 609 records
  / 1,767 unresolved cells (Mistral-exposed 104 records / 295 cells); full §B
  needs_adjudication surface = 3,172 cells (Mistral-exposed 225 / 580); increment
  outside the selector = 121 records / 285 cells; 20 non-tie-breakable pendings
  (11 × design-05 allocation-parse, 9 × design-09 arbiter-first).
- Exact historical six-SUT 02/07 cost = $26.681701 (378 records, 10,037 calls) — the
  re-execution cost baseline (not the old ~$10–15 guess).
- Known mechanical dependency: the Part-B exporter emits record-level rows but
  protocol §6 is cell-level — FR-16 must fix BOTH surface and export granularity.

TASK 1 — FR-16 RULING (the delegated item; subject to the authority check):
Fix the W1 selection surface. Recommendation to weigh, not rubber-stamp: cover the
FULL §B needs_adjudication surface (the 609-record refusal-tag selector was an
FR-scoping error, now corrected by evidence); route the 20 non-tie-breakable records
to their proper §B/Part-B handling, never the third judge; specify cell-level Part-B
export granularity. Issue as a NEW dated ruling doc; update PENDING-RULINGS; flag for
Jimmy ratification.

TASK 2 — JIMMY'S THREE ONE-LINERS (record his exact words in the ruling log):
(1) Transcripts: authorize a NEW immutable six-SUT 02/07 re-execution (cost baseline
    $26.68, full-turn persistence now guaranteed) OR supply recovered transcripts.
(2) STOP-8 / tie-breaker: accept Mistral plus the Part-B human surface FR-16 implies
    (use the quantified 104/295 vs 225/580 numbers), OR issue a logged §E
    replacement-model amendment (distinct family, explicit slug, reliability-probed
    before W1).
(3) C-4/C-5 prerequisites: order the missing 06/09 G5 reference authoring now under
    the two-agent rule (yes/no), and authorize Codex to formalize the machine-readable
    L7 rotation list while W1 is blocked (yes/no). Leave neither ambiguous.
If any one-liner is deferred, W1 stays blocked-on-Jimmy — log it and move on.

TASK 3 — RATIFICATION SWEEP (Jimmy is in the room; clear the whole backlog once):
collect and log one-liners on PR-1 (option c, 356/344), PR-2 (ADVICE_SYSTEM), PR-3
(§6.4 interpretation), PR-4 (OpenRouter sanctioned), PR-6 (near-agreement mean +
sensitivity row), PR-8 (FR-1..FR-15 bundle — highest-consequence FR-3/FR-1/FR-5/FR-14),
and the W4 06-reference fixes. None block W1; ALL block release language later.

TASK 4 — ZERO-JUDGMENT CODEX ORDERS: write a NEW dated amendment incorporating FR-16
and Jimmy's rulings. Exact post-clearance sequence: 276-test baseline → NEW immutable
02/07 re-execution (verify complete turn transcripts against the data-contract test) →
TDD cell-aware Part-B exporter + tie-breaker → W1 → then W2..W5 in order. Never skip
to W2. Explicit model slugs everywhere (panel.py defaults ≠ frozen pair).

CONSTRAINTS: NO G4-dependent gate verdicts (labels absent); FIX-MECHANICS-ONLY;
report immutability (NEW dated files); HOLDOUT never loaded; never delete (mv to
RECYCLE-BIN/); the ruling session makes NO OpenRouter calls; shared git index —
git log -1 AND git diff --cached --name-only before staging (sibling staged files
have been swept twice), explicit WALKWORTHY pathspecs, fast-forward pushes only;
every ruling logged + ratification-flagged; anything beyond authority →
PENDING-RULINGS, never guessed.

ON CLOSING: update project-dashboard.html IN PLACE — Live status, rulings ledger,
contingencies C-1..C-5, forecasts if materially changed, Last-updated line, Changelog
row, and REPLACE §12 "Instructions for the next session" with whatever comes next
(likely the Codex W1-resume orders). Write a NEW dated handoff; update Claude memory;
commit + fast-forward push WALKWORTHY paths only.
```
