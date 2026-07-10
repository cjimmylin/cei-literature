# WALKWORTHY — Next-Session Boot Prompt (Session O4-BUILD)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Model: Opus** (`/model opus`). This is an EXECUTION session — every judgment call was
frozen in the 2026-07-10 Fable adjudication. Do not spend Fable on it.

Start a fresh session, `/model opus`, then paste everything below the line:

---
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) — **Session O4-BUILD (Opus, EXECUTION)**. Everything judgment-shaped was frozen by the 2026-07-10 Fable adjudication session; this session implements against frozen specs. Do NOT re-litigate design decisions. Where a spec genuinely runs out, add to PENDING-RULINGS and move on — never guess on charter-level questions.

SCOPE LOCK: stay entirely within CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Do NOT touch, read for input, or import from any sibling bench (WCF-Bench, FruitBench, CookBook, SermonMount, CorinthLove, DUPLEX, INNOVATION). Differentiate only vs published literature.

START by reading, in order:
1. 00-PORTFOLIO/20260710-O4build-session-handoff.md — THE work list (W1–W8) and the authority stack for this session.
2. 00-PORTFOLIO/20260710-fable-gate-prereg-pilot-adjudication.md — frozen §B primary-metric formulas + headroom stats, §C gate computations, §E judge decisions (spec for W1, W6, W7).
3. 00-PORTFOLIO/20260710-fable-PR3-ruling.md — binding refusal/adjudication semantics R1–R4, incl. required test pins (spec for W2).
4. 00-PORTFOLIO/20260710-human-label-protocol.md — §2 sampling strata + §9 tooling specs (spec for W5).
5. 00-PORTFOLIO/PENDING-RULINGS.md (PR-5 DIRECTED; PR-1/2/3/4 await Jimmy one-liners — do not block on them) + 20260709-O4prep-session-handoff.md (harness lineage: panel runner, OpenRouter path).

EXECUTE W1–W8 IN ORDER (from the handoff):
- W1 metrics.py — the ten frozen §B formulas (verify 01's cost-ladder family structure FIRST; pre-declared fallback if incomplete). Replace the run_design stubs.
- W2 PR-3 implementation R1–R4 (incl. the retro re-tag of pilot+smokes as a NEW dated analysis file — mechanical, no live calls).
- W3 PR-5 backend (empty-200 retry N=3 + provider routing) + 1-cell/design reliability probes per candidate SUT and tie-breaker judge (the F-2 lesson).
- W4 M-3: author + wire 06/09 matched-quality reference answers — careful authoring, two-agent rule (author ≠ reviewer), FA-1-compliant, L1–L9 linted. 06/09 stay PROVISIONAL until G5.
- W5 label_sample.py + judge_validation.py + Part B exporter per protocol §9 (Part A seed 20260710, fail-loud strata, blinded CSV + instruction packets).
- W6 the ≥6-model full-split panel via run_panel (no --items-per-design; 344 runnable), roster chosen AFTER W3 probes, judges gpt-4.1-mini + gemini-2.5-flash + tie-breaker per §E (own-family exclusion in code). Per-SUT parallel resumable runs, merged. Budget check first (expect tens of dollars; 02/07 dominate wall-clock).
- W7 gates_o4.py (G1–G3, G6–G8 statistics; G9/G10 renderer enforcement) + the O4 report as a NEW dated file — gate READINGS clearly marked "verdicts at O5"; every score marked PROVISIONAL pending G4 human labels.
- W8 wrap: dated handoff, memory update, atomic commit(s).

CONSTRAINTS:
- TDD throughout; suite currently 159 green; mock/recorded tests only — NO live call in the suite. Live calls happen only in W3 probes and the W6 panel (OpenRouter key at ~/.codex/secrets/openrouter.env — never print/commit it).
- FIX-MECHANICS-ONLY: no item edited from model performance. No gate verdicts, no item kills, no release claims (all O5/Jimmy).
- Report immutability: new dated files only. HOLDOUT never loaded (loader hard-refuses) and never in git. runs/*/scored_items.jsonl stays gitignored.
- ≥3 concurrent sessions share this git index: `git log -1` before staging; stage WALKWORTHY paths EXPLICITLY; never rewrite sibling commits. Commit incrementally (at least: after W2, after W5, after W7) so a usage-limit kill loses nothing — the W6 panel is checkpoint-resumable by design.

END WITH: (a) the O4 panel report (dated, provisional-labeled); (b) a dated session handoff (next = Jimmy's Part A labels → judge_validation → O5 gate adjudication, Fable-preferred if a window recurs); (c) memory update; (d) final commit of WALKWORTHY paths only. Jimmy owes (NOT this session): Part A labels + second labeler, and the 4 one-liner ratifications (PR-1 c / PR-2 ADVICE_SYSTEM / PR-3 §6.4-interpretation / PR-4 OpenRouter).
