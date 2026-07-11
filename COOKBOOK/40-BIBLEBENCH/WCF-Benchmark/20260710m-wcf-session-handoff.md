# WCF-Bench — Session Handoff (2026-07-10, session 15 — Fable-orchestrated multi-agent MVP build-out)

**Date:** 2026-07-10 · **Orchestrator:** Fable (main loop; judgment + commits only) ·
**Executors:** 2×Opus build agents (R40, run_mvp), 1×Opus build agent (R39(d)+screen),
10×Sonnet transcription agents (2 passes), 1×Opus fidelity auditor ·
**Governing docs:** binding memo `20260710-fable-grok-ratification-floor-divergence-memo.md`
(R38–R41) · boot `20260710l-opus-rerun-boot-prompt.md` · **Predecessor:** `20260710j`.
**Project root:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`

> One session executed the entire MVP critical path: R40 ✅, bank transcription 69→**230
> COMPLETE** ✅ (independently audited GO), `run_mvp.py` built ✅, R39(d) gloss+probe+re-qual ✅,
> frontier OPEN-award screen (both fail) ✅, smoke GREEN ✅, **full 816-cell descriptive MVP run
> LAUNCHED** (background, checkpointed, $25 cap). Commits `0f56a6a9a` → `3c7a4b831` (+ MVP-run
> results commit to follow). Total live spend this session so far ≈ $1.3 of the ~$45 credit.

---

## 1. R40 EXECUTED (commit `0f56a6a9a`)

Retry seam (JSONDecodeError/402/403/429 + backoff → `fail_transport_after_retry`) +
settled-core tie→UNGRADED (never silent False). Surgical re-run
(`07-PILOTS/20260710-surgical-rerun/`, $0.26): grok re-graded the persisted AGG-C8×llama cell
cleanly (0 parse losses → **R38(3)(ii) MET — grok ratification FINAL**); deepseek WHOLE-C9
recovered (3/3 judges); deepseek contested arm fresh-run settled-core **1.0/1.0/1.0** (the 403
was the key credit limit, cleared by Jimmy's top-up). Floor per R39(e): **HOLDS on every
scoreable cell.** Finding: grok reproduced gemini's Q151↔Q152 floor category error on AGG-C8
kp2 → gave R39(d) two-family motivation.

## 2. BANK COMPLETE: 230/230 items (commits `9017608bb`, `92c0bed82`, audit `3c7a4b831`)

- Pass 1 (5 Sonnet agents): wave-1 exemplars (49) + expansion-1 (50) → 20 files.
- Pass 2 (5 Sonnet agents): wave-2 exemplars (62) → 10 files.
- Flags landed: AGG-C7-007 `contested`; LIB-C7-008 + LIB-C3-W202 `dev_set_only`+`disputed`
  (all four [DISPUTED] legs now marked); MEND-C3-W202 as-is (SOL keypoint recorded-not-applied);
  gold_order on all orderable AGG rank-sets; XC items normalized to the committed
  `[XC, Cx, …]` convention (13 total).
- **Independent Opus fidelity audit: GO** (`05-BANK-YAML/20260710-transcription-fidelity-audit.md`):
  161/161 complete, 20-item deep-sample verbatim-faithful, ~33 anchors independently
  re-verified, **0 discrepant**; the 2 reported-unmatched anchors were OCR artifacts (Q138
  hyphenation; Q119 page-header). Benign slash-drop ID normalizations: NARROW-C3-002,
  LIB-C5-005.
- Test scoping fix: `test_bank_yaml` gold_order/construct_specificity assertions now match the
  spec's actual rules (Track-B T2a/T2b; R23a W301–306 targets).

## 3. run_mvp.py BUILT (commit `21b3688e4`)

`04-HARNESS/run_mvp.py` + `wcfbench/mvp.py` + 20 hermetic tests. Per-(item,SUT) cell
checkpoint/resume (idempotent), per-cell error survival, cost tracking from live pricing +
`--budget` clean abort, R27 transcripts, disagreement record, descriptive report with R34.4
single-family labels + R39(e) floor-screen language, dev_set_only + EPISODE exclusion
(loudly reported), fail-loud slug validation with nearest-match (caught 2 stale slugs live).

## 4. R39(d) EXECUTED + frontier screen (commit `e5a78b3b4`)

Floor-gloss + settled-core probe (fixtures: persisted AGG-C8/AGG-C3×llama + synthetic
collapse) + settled-core prompt hashed into the manifest (R35.6 gap closed). K=8 re-qual
(`07-PILOTS/20260710-settled-requal/`, $0.80): **gemini 8/8, grok 8/8** (both ex-offenders
clean under the gloss), **gpt-4o-mini 0/8 fail_substantive → LOSES settled-core, now
coherence-only**. Settled-core families {google, x-ai} = 2 ✓. **NEW COMBINED MANIFEST of
record:** `07-PILOTS/20260710-settled-requal/20260710-settled-requal-manifest.json` (all
prior manifests stale by design). Frontier screen: cohere/command-a + amazon/nova-pro both
fail OPEN-award discrimination → **OPEN award stays single-family {google}** (R34.4 label).
Live-caught parser gap (markdown-bold settled-core lines) fixed +3 tests; pre-fix run
preserved in `preparserfix/`. Suite: **425 pytest green.**

## 5. MVP RUN — smoke GREEN, full run IN FLIGHT

- Smoke (`07-PILOTS/20260710-mvp-smoke/`): 3 items × 4 SUTs = 12 cells, 0 errors, $0.014.
- **Full run launched** (background): 204 runnable items × 4 SUTs = **816 cells** →
  `07-PILOTS/20260710-mvp-run/`. Roster: llama-3.1-8b-instruct, deepseek-chat,
  **mistral-large-2512**, **claude-haiku-4.5** (catalog-current slugs; non-judge families).
  Manifest: the new settled-requal manifest. Budget $25 (≈$43 remained on the key at launch).
  **Resume if interrupted:** `python run_mvp.py --go --run-dir ../07-PILOTS/20260710-mvp-run
  --manifest ../07-PILOTS/20260710-settled-requal/20260710-settled-requal-manifest.json
  --suts "<same 4>"` — completed cells skip.
- The report is DESCRIPTIVE/PRE-GATE: OPEN award single-family-labeled; settled-core zeros are
  screened for sample review (R39(e)), never asserted as model failures.

## 6. Remaining queue (nothing model-blocked)

| item | blocked on |
|---|---|
| MVP-run results: commit run dir + read the report; Fable-tier read of disagreement records is the natural next adjudication | run completion (this session or next) |
| G6 confessional panel → gated G1–G7 run, H-DISC promotion (judge-side conditions ALL met), W304/W305 position maps, 4 LIB legs | **Jimmy** |
| OPEN-award 2nd family: escalation options exhausted at R36.4's named tiers; next = format-bridge (few-shot exemplar in award prompt ⇒ full re-qual) — needs a ruling before build | Fable/Jimmy decision |
| gpt-4o-mini: now coherence-only; consider dropping from panel entirely or keeping for coherence redundancy | next session judgment |
| Perturbation battery (P1–P6) at scale; EPISODE live runs (episode_live) for the 22 NARROWGATE items | post-MVP Opus |

## 6b. MVP RUN COMPLETION ADDENDUM (same session, post-launch)

**816/816 cells scored, 0 errors** (`65a48a8d7`; report `07-PILOTS/20260710-mvp-run/20260710-mvp-run-report.md`).
Operational history: (i) concurrency added mid-run (`--concurrency 8`, ~4× via per-SUT lanes,
`d6db938c3`); (ii) a ~30-min LOCAL network/DNS outage (18:02–18:32) transport-errored 401 cells —
preserved (`checkpoint-20260710-networkoutage-full.jsonl` + PARTIAL report), cleared, re-run clean;
(iii) resume-report aggregation bug found+fixed (`db539f468`, 444 tests): resumed runs now report
ALL checkpointed cells, transcripts append (session-2 had clobbered session-1 judge texts — 415
cells' verdicts unrecoverable in THIS run dir, disclosed in-report; non-recurring), offline
`--regen-report` added. Real key-side spend ≈ $12.7 (internal estimator ≈10× under — known nit,
budget-cap guards the estimate). Key remaining ≈ $30.

**Readings (DESCRIPTIVE/PRE-GATE, Matter-proxy headline for OPEN):** clear cross-SUT separation —
mistral-large-2512 ≈ claude-haiku-4.5 > deepseek-chat ≫ llama-3.1-8b (llama 0.03–0.72 by design;
e.g. mending 0.35 vs mistral 0.95). Refusals: llama 73 over-refusals/204, haiku 55, deepseek/mistral
~14 — over-refusal is a live axis. PROOFTEXT low everywhere (0.03–0.34): citation-token scorer
under-credits (known); judge-assisted correct-use is the upgrade before quoting PROOF numbers.
**Settled-core floor: no flag stands** — the one session-1 flag (AGG-C3-W302×deepseek 0.0, transcripts
lost to the clobber) was re-sampled with full transcripts → fresh cell 1.0, both eligible judges
correct+quoted; gpt's deterministic harmless-error appeared only as an ineligible raw (the requal
fence working). Disagreement records cover 309 transcript-backed cells → **next Fable-tier item:
read the worst-spread cells** from `disagreement.json`.

## 7. Sharp edges honored

Report immutability (all run dirs new + append-only; pre-fix requal preserved). Canary
`WCFBENCH-CANARY-c1647-x9k4q` never re-minted. Shared git index LIVE — all commits from the
orchestrator main loop with explicit paths (`git log -1` before each); agents were forbidden
to run git. Secrets runtime-only. No deletions. Agents produced output files, verified per
the orchestration rule; the one cross-agent data inconsistency (XC commandments) was caught
and normalized to the committed convention before commit.
