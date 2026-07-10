# WCF-Bench — Next-Session Boot Prompt (Opus build tail — paste to start)

> **Model: Opus main loop** (`/model opus`). Pure execution from a reviewed, binding spec —
> no adjudication. The Fable session (2026-07-10, session 8) is DONE: its memo
> **`20260710-fable-judge-calibration-adjudication-memo.md` (BINDING, R24–R28)** is the
> spec this session builds. Do not relitigate R1–R28, the contested-scoring ruling, or the
> OpenRouter sanctioned-path ruling.

> **Scope lock: WCF-Bench ONLY** (`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`).
> Shared git index is LIVE: `git log -1` before every commit, explicit paths, never
> `git add -A`. Westminster texts in `../WCF/` are the only normative source. Report
> immutability (new dated files). Secrets sourced (`source ~/.codex/secrets/openrouter.env`),
> never committed. Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Mock-first/TDD; the
> pytest suite stays hermetic (240 green at `674a9ad1c`; live runs are opt-in `--go`).

**Read first, in order:** (1) memory note `wcf-bench-portfolio-state`; (2) the Fable memo
above (the spec — esp. R24 build spec items 1–6, R25 battery probes, R27 persistence,
R28 frozen disclosure anchor); (3) `20260710-wcf-session-handoff.md` (session-7 state).

**What the Fable session ruled (context, one line each):** R24 — triaxial switches to
per-keypoint AWARD scoring (axis-tagged rubrics, binary award/deny, mechanical fractions;
this pilot's OPEN spreads declared artifact, re-judge post-fix); R25 — G4 GO confirmed
provisionally, acceptance battery extended (+award-consistency probe, +disclosure-inversion
probe); R26 — AGG-C5-W304 familial-honor reading = legitimate CONDITIONAL position, G6
3-position card ratified as proposed map, T2a demotion declined, sample-level split
unadjudicable (transcripts weren't persisted); R27 — all live runs must persist SUT +
judge transcripts; R28 — disclosure-low promoted to pre-registered candidate headline
H-DISC with a frozen 3-level anchor + five promotion conditions.

**Work queue (ordered; the memo's Handoff section is authoritative where fuller):**
1. **R24 fix** — axis-tag the transcribed OPEN rubrics (`axis: matter|manner|end`, split
   spanning keypoints, Sonnet-tags + review); one award call per judge per item
   (`KP<n>: award|deny` + reason, reuse `_AWARD_RE`); `OFFMAP:` reported-not-scored;
   hardened numeric fallback for untagged axes (pinned levels, off-scale → raw +
   `scale_defect` flag, excluded from aggregate); per-judge raw UNCLAMPED everywhere
   (fix `contested._numeric_axis`), clamp only at aggregation.
2. **R27** — transcript persistence in the runner/pilot output path (SUT prompt+response,
   full judge verdict texts, template hash, slugs, timestamps; append-only dated run dirs).
3. **R28/R25** — leveled disclosure prompt (1.0/0.5/0.0 anchor or two-keypoint award form);
   add the two new probes to the judge acceptance battery.
4. **Re-run the 6-item pilot slice post-fix** (same SUTs `llama-3.1-8b`+`deepseek-chat`,
   provisional panel `gpt-4o-mini`+`gemini-2.5-flash`) → new dated run dir + short dated
   report; re-derive disagreement clusters (only post-fix OPEN spreads are adjudicable).
5. Perturbation-variant materialization (feeds `position_invariance` + the flip-rate engine).
6. Earlier-wave transcription ~161→230 (mark `AGG-C7-007` `contested: true`; `LIB-C7-008`
   + `LIB-C3-W202` `dev_set_only`; axis-tag at transcription) + anchor grep-verification
   (grep short fragments — OCR wraps + injected proof-letters).
7. Scale toward the gated G1–G7 run — still gated on the **G6 panel** (Jimmy recruits;
   instrument done; the memo ratified the W304/W305 position cards as the proposed maps).

**Do NOT:** run the G6 panel; mint a gold for a contested item; edit frozen surfaces
except via `[NEEDS-RULING]`; draw measurement claims from pre-gate pilots; touch sibling
benches (WALKWORTHY/INNOVATION/etc.).

**End with:** a dated handoff, memory-note update, atomic commit (explicit paths) + push.
