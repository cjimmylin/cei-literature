# WALKWORTHY — Paste-Ready Prompt for the Next Session

<!-- WALKWORTHY-CANARY-7f3e2026 -->
Copy everything inside the block below into a fresh session (Opus is the right tier for this work — `/model opus` if the session is on Fable).

---

```
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks).

START by reading, in order:
1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/00-PORTFOLIO/20260709-next-session-handoff.md
   — the re-entry document: current state, authority stack, and the exact task list for this session (§4).
2. The authority stack it names in its §2 (charter → playbook → master plan), skimming for the rules you'll
   need: holdout policy, lint rules L1–L9, FC-1/FC-2/FC-4 mandates, and the frozen pre-registered gates.

THEN execute the handoff's §4 task list top-down (slimmed Session O1):
holdout split → residual fixes → easy-tier backfill for banks 09/10 (with separate-agent R1–R3 review)
→ portfolio coverage-matrix refresh → atomic commit.

Ground rules for this session:
- EXECUTION mode throughout: produce files, not plans. Verify agent outputs exist on disk.
- The charter, playbook, master-plan gates, and both adjudication memos are BINDING. Do not redesign
  anything; judgment calls beyond them go to 00-PORTFOLIO/PENDING-RULINGS.md (create if absent) and the
  item is parked, not guessed.
- Repo rules: no deletions ever (mv to RECYCLE-BIN/); HOLDOUT/ is gitignored and never committed;
  new reports = new YYYYMMDD- files; check git log -1 before committing (parallel sessions share this
  worktree); every Agent call carries an explicit model= parameter.
- Checkpoint-commit after each completed §4 item (session-limit kills have hit this project twice).
- End with: a verification sweep (item counts, coverage, canary, L8 grep), a new dated session handoff
  in 00-PORTFOLIO/, a memory update, and a final commit.

If this session has API keys available (ask Jimmy if unclear), ALSO proceed to Session O2 per the master
plan §2 (mock-first harness; still NO live model calls until O3).
```

---

**Notes for Jimmy (not part of the prompt):**
- This session needs no API keys. Keys + your ~60-item/design human labels unblock O3/O4 (the live panel).
- If you get a Fable session before ~2026-07-11, don't spend it on this O1 list — its best WALKWORTHY use is adjudicating the first REAL panel results, per the handoff §5.
