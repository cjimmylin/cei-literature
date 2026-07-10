# CLI-OAuth Bring-Up — Fable Adjudication of First Real-Token Results

**Date:** 2026-07-09 · **Author:** Fable session (main loop) · **Tier:** Fable
**Adjudicates:** (1) T1 provisional shim GO/NO-GO; (2) judge-agreement machinery → YELLOW pilot green-light; (3) surprises routing.
**Inputs:** `40-BUILDS/t1-runner-provisional/` (shim + `20260709-cli-bringup-log.md` + `20260709-smoke-report.md`), `40-BUILDS/rp04-corpus/20260709-s1-pilot/20260709-s1-machinery-validation-report.md`, both agents' return summaries.
**Authority:** `20260709d-cli-oauth-provisional-ruling.md` (this session, first use).

---

## 0. What Fable independently verified (not taken from agent summaries)

- **Transcripts are genuine:** inspected a raw `20260709-s1-run.jsonl` record — full provenance stamp (`cli-oauth-provisional`, CLI 2.1.183, resolved model `claude-haiku-4-5-20251001` from `modelUsage`), rubric-only judge prompt, raw CLI JSON with token accounting. 250 records across 3 pilot transcripts; counts match calls claimed.
- **Zero label leakage, checked independently:** main-loop grep of all 250 sent prompts for `intended_pole` / `gold:` / `_truth_` / `reverse_keyed` → 0 hits in every transcript file. The 100% recovery is not circular.
- **Report honesty:** provenance headline and "does / does NOT show" section present and correctly scoped; roster-degradation disclosure present; tier×modality confound disclosed.
- **Anti-leakage watchlist (dispatch-skill verification):** both agents' return summaries greped mentally against the sidecar/peer-output watchlist — no contamination signals; the pilot agent's only cross-session contact was the `~/.codex/config.toml` drift incident (config, not scoring artifacts), which it handled correctly.

## 1. Ruling R1 — T1 provisional shim: **GO** (as the provisional T1 backend, 2-family)

The shim is accepted as the provisional backend behind Cycle-2 item 2.1. Evidence: 34 mock unit tests + 3 real-token integration tests green; 2×10-item smoke clean (0 unexplained errors); vendor-agnostic interface with provenance stamping and JSONL transcripts built in.

**Binding conditions (C1–C5):**
- **C1** — `google_cli` backend stays disabled until Jimmy re-provisions Gemini (Antigravity migration or Gemini API key). No 3-family claim may be made until then.
- **C2** — codex backend: per-call timeout ≥ 240 s AND per-call `-c` config injection (`model`, `model_reasoning_effort`) is now MANDATORY, never rely on the shared `~/.codex/config.toml` (see R3-b).
- **C3** — anthropic backend: explicit `--model` on every call; resolved model id read from `modelUsage` only. (Bare `claude -p` inherits the calling session's model — observed `claude-fable-5`; an unstamped Fable-priced call is both a cost and a provenance bug.)
- **C4** — refusal classification is PROVISIONAL: any study where refusal counts are load-bearing must hand-audit refusal rows (the U+2019 false-negative shows vendor-phrasing sensitivity).
- **C5** — when API keys land, API backends drop in behind the same interface and all `cli-oauth-provisional` results that matter get re-run/replicated; the shim's CLI backends then serve only as a cross-check lane.

## 2. Ruling R2 — Judge-agreement machinery: **PASS**; YELLOW RP-04 judge-pilot design **GREEN-LIT, contingent on a third family**

The machinery did what the rescoring matrix §3 Cycle-1 step 1 required: reconstruction → label-blind judge prompts → 2 CLI-OAuth families → strict-JSON parse → recovery + κ/Wilson stats. 100%/100% recovery with κ = 1.00 on balanced classes (41/39) is the expected plumbing signature on canonical reconstructions — correctly reported as a floor check, not discrimination.

**Findings that bind Cycle 2 (F1–F4):**
- **F1 (corpus gap, upstream):** ACT modality (3,600 rows) is not judge-reconstructable — records carry keyword signatures, no canonical response prose. Cycle-2 real runs generate real ACT responses so this gap self-heals for S3; but any future S1 machinery work on ACT needs a canonical renderer first.
- **F2 (corpus gap, upstream):** 2,250 `is_control` rows have no rendering in `renderings.jsonl` — nothing to show a judge. Route back to WITNESS as a corpus finding; controls must be renderable before Cycle-2 scoring includes them.
- **F3 (confound):** tier is confounded with modality in the frozen corpus (END/REC = floor, GEN = hard). Cycle-2 analysis may not read tier effects off this axis; the variance-decomposition model must treat them jointly.
- **F4 (scope):** D4 framework-affinity was correctly nulled (meaningless on minimal reconstructions); it activates only on real S3 prose.

**What "green-lit" means precisely:** the YELLOW judge-pilot *design* (real judge families scoring real transcripts under the ruling's YELLOW conditions) is approved to run the moment its two gates clear: (a) third family restored (Gemini re-provision/key, or the matrix's human-label deviation fallback with Jimmy sign-off), and (b) real S3 responses exist (key-gated, unchanged). Nothing about H3 judge bias ran or may be claimed today.

## 3. Ruling R3 — Surprises, routed

- **(a) Gemini tier retired server-side** (`IneligibleTierError`, individual Code Assist tier → Antigravity). Jimmy ACTION (not a ruling): re-provision or provide a Gemini API key. Added to FABLE-WEEK blocked list; amends the mental model of Jimmy gate #1 (a Gemini *key* is now the clean path).
- **(b) Shared `~/.codex/config.toml` drift** — a parallel session set an invalid `model_reasoning_effort` and a too-new model id, silently breaking every codex call (57/80 instant failures) until the pilot agent diagnosed and bypassed it with per-call overrides. Same hazard class as the shared-git-index collisions of 2026-07-09. **Standing mitigation (vault-wide, this memo):** runner backends must pin all behavior-relevant config per-call and treat shared dotfiles as hostile; sessions must not edit shared CLI config files without a note in their handoff.
- **(c) PR-02** (ToS posture + internal-citation boundary) already queued in `PENDING-RULINGS.md` — Jimmy decides; Fable recommends full quarantine (option a).

## 4. Session verdict

Cycle-2 item 2.1 now has a working provisional backend (2 of 3 families) with governance that survives the window: the ruling (20260709d) bounds what post-window Opus sessions may do, the shim enforces provenance mechanically, and the pre-registered matrix + this adjudication mean the real RP-04 Phase-1 measurement still runs mechanically the day keys land. Total real-token spend this session: ≈ 114 Anthropic / ≈ 193 OpenAI / 8 Google (all-fail probes) — all within the ruling's caps.
