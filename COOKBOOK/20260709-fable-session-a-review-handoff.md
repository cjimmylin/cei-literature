# 20260709 — Handoff: Fable Session-A validity review (DUPLEX-P0)

**Session:** Fable main loop, 2026-07-09. **Deliverable landed:**
`20-DESIGNS/DUPLEX-P0/20260709-fable-session-a-review.md` (BINDING).

## What was done

- Staleness guard passed; **credentials checked: none present** → no pivot to the live P0 branch
  call; session executed as the planned validity sign-off.
- Three Opus verification subagents read all runner/analysis code (gates/stats, orchestrator/
  frames/adapters/items, bank JSON, new tests, entrypoint search) and returned quoted evidence;
  Fable adjudicated in the main loop. One main-loop grep (V-4 temperature path).
- All 7 boot-prompt items ruled + entrypoint decision + test-overfit check. **Verdict:
  CONDITIONAL-GO** — no design-level invalidity; runner is validity-cleared for a real P0 run
  conditional on F-1…F-5.

## Rulings at a glance

- **RATIFIED:** SA-1 G1 per-model→CV aggregation (+ pin `extended_thinking`/`forced_immediate`
  as the G1 contrast; + amendment A-1), SA-2 content baseline (same A-1), SA-3 runtime frame
  re-wrap (no pre-run hand-tuning; compliance breakdown added to §5.3 reporting), SA-4
  ET−greene_fallback contrast (composite-contrast disclosure; pin `min_effect=0.02`), SA-7 M030
  substring safe on this bank (robustness fix anyway). SA-9 tests CLEAR.
- **OVERTURNED:** SA-5 Codex `returncode!=0`=refusal (conflates admin errors; no retry; checkpoint
  makes it permanent) → F-1. SA-6 UNMEASURABLE keyed on condition name (miscodes non-Anthropic
  dead cells; **no V-4 temperature-drop path exists upstream at all** — run would abort on first
  `extended_thinking` call) → F-2.
- **Protocol amendment A-1 (additive):** per-item-grain G1 sensitivity both axes; primary numeric
  PASS + reversed sensitivity → PROVISIONAL (third trigger, same consequences as G1-b thin base).
  FAIL never softened (G-all intact).
- **SA-8:** run entrypoint (`run_p0.py` wiring the four flags + pinned G1 conditions + smoke
  test) is now a BINDING run precondition → F-4.

## Next session (Opus builder)

Land **F-1…F-5** from the memo's fix-package table, red→green, each test quoting the governing
sentence from the memo/protocol; append rows to the checklist-evidence table; then a NON-BUILDING
audit pass over F-1/F-2 only (WS-1 §3 standing order). All five block the real P0 run. No further
Fable gate — memo pre-specifies everything; out-of-scope discoveries → STOP-and-escalate.

After F-1…F-5: remaining chain is unchanged — credentials (Jimmy) → run entrypoint → P0 run →
mechanical adjudication per the protocol (+A-1).

## Known issues / notes

- Anthropic extended-thinking × temperature incompatibility means F-2's drop path is effectively
  mandatory, not contingent — verify against current API docs when implementing.
- Uncommitted at handoff time: this memo + handoff + memory update (committed together,
  path-scoped, this session).
