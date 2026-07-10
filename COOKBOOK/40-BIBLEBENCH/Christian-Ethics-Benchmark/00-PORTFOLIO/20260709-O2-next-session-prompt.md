# WALKWORTHY — Paste-Ready Boot Prompt for Session O2 (harness)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
Run this session on **Opus** (`/model opus` if needed). O2 is harness-building — a clear-spec code
build with no live calls and no Fable-level judgment. Do NOT spend a Fable window on it; reserve Fable
for adjudicating the first REAL panel results (O4/O5). Copy everything in the block below into a fresh session.

---

```
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) — Session O2: build the run harness.

START by reading, in order:
1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/00-PORTFOLIO/20260709-O1-session-handoff.md
   — current state (post-holdout split), authority stack, and the O2 scope (§5).
2. The authority stack it names in §2 — especially 00-PORTFOLIO/20260706-master-plan.md §2 (the O2 BUILD SPEC)
   and §3 (the frozen pre-registered gates the harness must be able to compute later). Skim the charter's
   Reporting Spine (§6) and the playbook so the harness's judge/refusal/parsing layers match the specs.

THEN build the harness per master plan §2 (EXECUTION mode — produce runnable code + a mock dry-run, not a plan):
- Manifest-driven runner: runs/YYYYMMDD-<panel>/manifest.json lists item IDs only (text loaded from files at
  call time), model list, judge pair, and FIXED permutation seeds (constants in the manifest, never generated
  at runtime). Vault has no shared runner — build fresh (Anthropic SDK + thin per-vendor adapters; keys via .env
  when they exist).
- Per-design executors: single-turn (01/03/04/05/08/10); scripted multi-turn w/ branch tables (02/07);
  paired-session administration with isolation + order-permutation (03/04/09/10); arbiter probes (09).
- Judge layer: per-category rubric prompts assembled from item YAML + spec §4; 2 cross-family judges;
  disagreement logged, never silently averaged; length-correction + reference-anchoring per cookbook.
- Refusal detector with the four-way taxonomy on every response; strict output-block parsers (05 allocation
  blocks); one-retry rule; non-compliance logged as data.
- Deliver: a MOCK-client dry-run exercising all 10 designs end-to-end; validated per-design output schemas;
  and the fixed capability battery for the §3.3 capability-gate chosen and written into the O2 handoff BEFORE
  any WALKWORTHY score exists (MMLU-Pro-class + agentic-class + long-context-class).

Ground rules for this session:
- NO live model calls this session (mock clients only). Session O3 is the first keyed run.
- Load the PUBLIC split ONLY (DESIGNS/*-seeds.md + the spec exemplars). NEVER point the harness at HOLDOUT/
  (gitignored, charter §6.6 — perturbation/contamination use only).
- The charter, playbook, and master-plan §3 gates are BINDING/frozen. Don't redesign items or gates; judgment
  calls beyond them go to 00-PORTFOLIO/PENDING-RULINGS.md (create if absent) and are parked, not guessed.
- Repo/worktree discipline: this worktree has multiple concurrent sessions — `git log -1` before staging,
  stage WALKWORTHY paths explicitly, never rewrite sibling commits. New reports = new YYYYMMDD- files;
  no deletions (mv to RECYCLE-BIN/). Every Agent dispatch carries an explicit model= parameter.
- Checkpoint-commit after each harness component (this project has taken mid-session kills twice).
- End with: a mock dry-run transcript proving all 10 designs parse+score, the capability-battery list,
  a new dated O2 handoff in 00-PORTFOLIO/, a memory update, and a final commit.

If API keys ARE available this session (ask Jimmy), still stop at the mock dry-run — do NOT start O3 live
runs without confirming the O2 deliverables and gate-computation code are in place first.
```

---

**Notes for Jimmy (not part of the prompt):**
- O2 needs **no API keys** — it's the mock-first plumbing. Keys + your ~60-item/design human labels unblock O3/O4 (the live panel).
- Model: **Opus.** If you have a Fable session left before ~07-11, its highest-value WALKWORTHY use is adjudicating the FIRST real panel/calibration results against the frozen gates — not this build.
