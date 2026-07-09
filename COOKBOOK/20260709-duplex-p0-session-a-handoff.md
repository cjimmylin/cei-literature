# 20260709 — DUPLEX-P0 Runner Rebuild: Session A Handoff

**Thread:** COOKBOOK core → the roadmap's **Session A** (P0 runner rebuild). Opus session,
2026-07-09. **Status: Session A COMPLETE.** All 10 WS-1 §1 run-precondition fix packages
implemented + tested (**95/95 green**), non-building A1/A2 re-audit passed after one blocking catch
was fixed. 9 commits (`f6a5b3335`→`c6f27c77d`, DUPLEX-P0 path-scoped).

## What Session A did

The DUPLEX-P0 runner was NOT run-ready (WS-1: 12 blocking code↔spec divergences behind a green
suite). This session rebuilt it fix-by-fix, each landed red→green with a **spec-quoting test** (the
A1/A2 discipline — the test quotes the ruling sentence, not the code's paraphrase), then had a
**non-building** Opus agent re-audit it (WS-1 §3 standing order).

Packages (all ✅, mapping to the WS-1 §1 consolidated checklist):
- **D11** hashlib stable seeds (cross-process resume, proven via subprocess test).
- **Record enrichment** — `stance_polarity`/`greene_subset`/`greene_fallback_prompt`/`monitoring_frame`/`content_tags`/`is_discriminant_control` preserved + emitted.
- **D9/R-1** polarity reverse-scoring at record creation (preserve items reflect about the 1..5 midpoint).
- **D10** refusal = no-stance (adapter structured flag OR scorer→None), NOT substring — **including the adapter layer** (see audit catch).
- **D8** monitoring frames as a first-class factor + X3 gap; `runner/frames.py` wrappers drift-guarded vs the bank builder; greene_fallback real arm (D2, fail-loud).
- **G1 (D3–D7, G1-a/G1-b)** — standard-condition content baseline, roster intersection, per-item abs deltas (no cancellation), 40% live-cell floor → PROVISIONAL, three-state cells (live/dead/UNMEASURABLE).
- **G3 (D1/D2, G3-a, IB-2)** — restricted to greene subset; per-item×per-frame deliberation-vs-fallback sign; ≥4/5 in BOTH frames; M030 pole-collapse sensitivity.
- **D12** null baselines (`analysis/baselines.py`): no-process-shift (load-bearing), majority-class, all-neutral — each a degenerate reference the gates must beat.
- **IB-1a/3a/4/5** (`analysis/ib_metrics.py`) + **D14** load_injected fail-loud (`strict_prompts`).
- **Obfuscation-QA** (`analysis/obfuscation_qa.py`): <10% recognition gate, fail-loud before scoring.

Deliverable: **`DUPLEX-P0/20260709-ws1-checklist-evidence.md`** — the per-item spec→code→test→status
table (read this first for the detail).

## The re-audit catch (why the non-building step matters)

The auditor confirmed the gate code faithful but caught **D10 half-fixed**: the substring refusal
match had RELOCATED from the orchestrator into the adapters (`detect_refusal(text)` → the
authoritative `refusal_flag`), and the orchestrator honors that flag by skipping the scorer — so a
live stance-1 "No, I can't approve that" would still be deleted (PS biased toward intervention). Two
adapter tests certified the divergence. **Fixed** (`cd510c876`): adapters set `refusal_flag` from
structured signals only (Anthropic `stop_reason=='refusal'`, Codex `returncode!=0`); added the
composed adapter+orchestrator test the orchestrator-only D10 tests had missed. This is the WS-1
systemic lesson recurring one layer up — exactly what the non-building audit exists to catch.

## Operator run-flags (MUST set for a real run — do not forget)

A real P0 run entrypoint MUST pass, or gates silently degrade:
- `frames=["monitored","unmonitored"]` (else X3/D8 + G3-both-frames degenerate)
- `administer_greene_fallback=True` (else no greene_fallback arm → G3 fallback has nothing to contrast)
- `strict_prompts=True` (else D14 load_injected fail-loud is off)
- `g1_unmeasurable_conditions={...}` in config only if a V-4 temperature drop actually fires.
The runner README's "run for real" snippet now sets these.

## Remaining follow-ups (NONE block the fixes; all are the run step, Jimmy-gated)

1. **Run entrypoint** wiring adapters-from-roster + the 4 flags above (+ a smoke test). The auditor
   flagged the absence of this as the one non-blocking gap. ~½ session of Opus work.
2. **Survey materials** for the two pre-registrations (G3 mini-norm, CRUX P1) — build if time; Jimmy greenlights + recruits.
3. **Credentials** (Anthropic key, Codex OAuth, Gemini decision) → P0 run (now genuinely run-ready)
   → adjudication per `20260706-p0-adjudication-protocol.md`. All Jimmy-gated.
4. Then the roadmap's **Session B** (KB fix pass) and **Session C** (ENGINE pre-P1 fixes) remain —
   both untouched this session; see the roadmap §3.

## Re-entry

Next session: read `DUPLEX-P0/20260709-ws1-checklist-evidence.md`, then either (a) build the run
entrypoint (item 1) if staying on DUPLEX, or (b) start roadmap **Session B** (KB fix pass) or
**Session C** (ENGINE fixes) per `Fable-Assessment/20260707-00-master-assessment-and-roadmap.md` §3.
Git: parallel sessions share the index (a sibling `git add -A` swept this session's first commit —
commit promptly, path-scoped, never `git add -A`).
