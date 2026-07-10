# WCF-Bench — Next-Session Boot Prompt (paste this to start the session)

> **Model: OPUS main loop** (`/model opus`). This is an execution session — mechanical errata + harness coding from a clear spec. No Fable-tier judgment work remains queued; do not burn Fable tokens here. Delegate searches/greps to Sonnet/Haiku subagents with explicit `model=`.

> **Scope lock: WCF-Bench ONLY.** Work stays inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` (+ read-only `../WCF/` sources). Do NOT read, reference, or touch WALKWORTHY, INNOVATION, COOKBOOK/20-DESIGNS, or any sibling bench — the shared git index is live with concurrent sessions. `git log -1` before every commit; stage this project's paths explicitly; never `git add -A`.

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First — read, in order:**
1. `20260709d-wcf-session-handoff.md` — current state: 230-item bank now **fully Fable-reviewed** (session 4, no kills); your queue is §2.
2. `20260709-fable-batch2-review-memo.md` — BINDING rulings **R8–R23** + errata orders **E1–E3** (§3 is your first work item). R1–R7 in `20260706-fable-review-memo.md` remain binding; do not relitigate any ruling.
3. `04-HARNESS/README.md` + `00-OVERVIEW/20260706-shared-spine.md` (§4 scoring, §5 perturbations, §10 schema — FROZEN) before touching harness code.

**The work, in order:**

1. **Execute errata E1–E3** (mechanical, memo §3 is exact): append an `## Errata` section (R6 style — never edit shipped item blocks) to each of `01-DESIGNS/expansions/20260709-{dutybound,crosswind,liberty,aggravate}-expansion-2.md`. For E2, grep-verify the replacement clause (`"peaceable, mild, and courteous speeches and behavior"`, Q135, `../WCF/03-LCLayout2 copy.txt` ~line 828) before writing it. Commit this as its own atomic commit before starting item 2.

2. **Harness Phase-2 remainder** (mock-first, TDD, keep `04-HARNESS/tests/` green; 44 pytest passing at start):
   - **NARROWGATE episode state machines** + defect-instructed baseline runner (prove the harness *detects* defection before trusting any null).
   - **Judge-prompt templates** (cross-family, generator-family exclusion, length-corrected, neutrality meta-check) — retire the PROOFTEXT anchor stub AND the refusal heuristic stub. Fold WHOLE-C10-W305 (and 005) into the G4 judge-calibration battery per R14.
   - **Remaining mechanical scorers**: NARROWGATE sent-message artifact, DUTYBOUND Track-A artifact-inclusion, signal-detection d′ on clean controls.
   - **Triaxial Matter/Manner/End sub-scoring** (needs the judge path; never collapsed pre-analysis).
   - **Full YAML transcription** of the 10×10 prose banks into spine-§10 records — now unblocked (the bank is fully reviewed). Transcribe the E1–E3 errata effects, the R20 dual-credit key, and mark the four `[DISPUTED]` legs (LIB-C7-008, LIB-C3-W202, LIB-C8-W304c, LIB-C2-W305b) **dev-set-only** pending G6.
   - **R23(a)**: emit a per-item `construct_specificity` field ("right boundary, wrong ground" route + its reskin perturbation) for all safety/liability-proximal items suite-wide.
   - Real `Anthropic`/`OpenAI` clients stay **credential-gated** behind the `MockModelClient` seam; `CLIModelClient` (CLI-OAuth) is smoke-pilot scale ONLY — the gated G1–G7 run uses the Messages API (ToS note, `20260709c` Addendum).

3. **Do NOT attempt the Jimmy-blocked items:** Messages-API keys / sanctioned bulk path; the G6 panel (4 `[DISPUTED]` confirmations + R20/R21 demote decisions + R1/R3/R4); the MEND-C3-W202 attorney check.

**Hard rules:** Westminster texts in `../WCF/` are the ONLY normative sources (Q1–113 via `LargerCatechismwithScriptureProofs1 copy.txt`; grep short 3–6-word fragments — OCR wraps lines and injects proof-letters between words). No deletions (`mv` to RECYCLE-BIN). Report immutability — new dated files only. Frozen surfaces (spine, registry format, rulings R1–R23) change only via `[NEEDS-RULING]`. Canary `WCFBENCH-CANARY-c1647-x9k4q` once per released file; do not re-mint. End with a new dated handoff + atomic commit(s) + push.
