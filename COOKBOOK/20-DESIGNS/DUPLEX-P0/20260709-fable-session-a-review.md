# 20260709 — Fable Session-A Review: DUPLEX-P0 Rebuild Validity Sign-off (BINDING)

> **Authority.** Fable main loop, 2026-07-09, inside the Fable window (ends ~2026-07-11). This memo
> is the higher-tier validity sign-off on the Session-A runner/analysis rebuild
> (`20260709-ws1-checklist-evidence.md`, commits `f6a5b3335`→`cd510c876`), per the boot prompt
> `../../20260709-session-a-fable-review-prompt.md`. It rules ONLY on the builder's NEW
> interpretation choices; it does not relitigate the 2026-07-05 memo, CS-1…5, IB-1…5, PS-1…6, or
> the adjudication protocol's frozen rulings. Where this memo amends the protocol it does so
> ADDITIVELY (new trigger for an existing outcome category) and says so explicitly.
>
> **Method.** Fable read the three load-bearing docs (checklist-evidence table, adjudication
> protocol, IB adversarial read) directly; all code verification was delegated to three Opus
> subagents (read-only, quote-returning) covering `analysis/gates.py`/`stats.py`,
> `runner/{orchestrator,frames,adapters,items}.py`, the run bank JSON, the new tests, and the
> entrypoint search. One targeted grep (V-4 temperature path) was run in the main loop.
> Staleness guard passed (`f9a6560e3` = boot-prompt commit; latest handoff = Session A).
> **Credentials check: no API keys present** — the live-P0 pivot (exit memo §2.4) is unavailable;
> this session is the review, as planned.

## Verdict

**CONDITIONAL-GO.** The rebuild is validity-cleared for a real P0 run **conditional on fix
packages F-1…F-5 below** (all Opus-executable with spec-quoting tests; none needs further Fable
review). No design-level invalidity was found. Five of seven adjudicated choices are RATIFIED
(three with binding additions); two are OVERTURNED (D10 Codex signal; V-4 UNMEASURABLE keying).
The missing run entrypoint is made a BINDING run precondition.

| # | Item | Ruling |
|---|------|--------|
| SA-1 | G1 process aggregation (per-model → CV) | **RATIFIED** + binding sensitivity (A-1) + pin hi/lo conditions |
| SA-2 | G1 content baseline (per-model mean → CV) | **RATIFIED** + same binding sensitivity (A-1) |
| SA-3 | Frame rendering (runtime 5×2 re-wrap) | **RATIFIED**; no pre-run hand-tuning; compliance reporting added |
| SA-4 | G3 fallback contrast (ET − greene_fallback) | **RATIFIED** + composite-contrast disclosure |
| SA-5 | D10 Codex `returncode != 0` = refusal | **OVERTURNED** → F-1 (blocking) |
| SA-6 | UNMEASURABLE keyed on condition name | **OVERTURNED** → F-2 (blocking) |
| SA-7 | M030 substring keying | **CONFIRMED for this bank**; robustness fix F-3 |
| SA-8 | Run-flags entrypoint gap | **BINDING run precondition** → F-4 |
| SA-9 | Test-overfit spot-check | **CLEAR** (no code-over-spec certification found) |

---

## SA-1 — G1 process aggregation. RATIFIED, with binding additions.

**The choice.** Per-model signature = mean over items of |per-item Δ| (Δ = mean(`extended_thinking`)
− mean(`forced_immediate`), abs per item per D5), then CV across models (`gates.py:153-155,173`).
Alternative: per-item CV-across-models, then average over items.

**Ruling.** G1-a's sentence ("cross-model CV of per-item condition-deltas") designated the
*quantities* — condition-deltas vs standard-condition stance, same 48 items, same models, same run
— not the aggregation grain; the grain was left to the pre-existing architecture. As G1-a's author
I confirm the builder's reading is compatible with intent. The per-model grain does wash out
profile shape (two models with equal mean |Δ| on disjoint item sets are indistinguishable), but on
the **numerator** that error is conservative — it understates process disagreement and biases
toward FAIL, which the V-1 robustness path already guards. The alternative grain is NOT adopted as
primary: per-item CVs of signed deltas have degenerate denominators (cross-model mean Δ ≈ 0 when
models split in sign), and switching only one side of the ratio would break numerator/denominator
grain symmetry, which the CV comparison needs to be coherent.

**Binding additions.**
1. **Pin the contrast.** Verified: the process axis uses ONLY the `extended_thinking` −
   `forced_immediate` pair (constructor defaults `high_condition`/`low_condition`);
   `load_injected`/`affect_primed` never enter the G1 signature. This is acceptable (G2 carries
   per-manipulation separation) but MUST be pre-registered: the run entrypoint passes both
   condition names explicitly, and the write-up states that G1's process axis is the
   deliberation–speed contrast, not pooled manipulations.
2. **Sensitivity + downgrade — Protocol amendment A-1 (additive).** See SA-2; defined once below.

## SA-2 — G1 content baseline. RATIFIED, with the same binding sensitivity.

**The choice.** Per-model scalar = mean over items of per-item mean standard-condition stance, then
cross-model CV (`gates.py:159-166,174`). Gate = strict `process_cv > content_cv` (`gates.py:176-178`).

**The risk (real, and anti-conservative).** Averaging stance over items before the CV can mask
per-item content disagreement: models that disagree item-by-item in offsetting directions converge
to near-equal means, deflating `content_cv`. Because mean stance sits near the scale midpoint
(~3), the `|mean| ≤ ε` guard (`stats.py:42-44`, ε=0.02) never fires on the content side — a
spuriously tiny denominator is returned as a real number and G1 passes trivially. This is the one
masking direction that corrupts the fork toward a false PASS, and it is not covered by any
existing guard.

**Ruling.** RATIFIED as primary (grain symmetry with SA-1; same authorial-intent clarification),
**conditional on Protocol amendment A-1**:

> **A-1 (binding, additive).** The G1 analysis MUST also compute and report a per-item-grain
> sensitivity for both axes, over the same live records the primary uses:
> - *Process (per-item grain):* for each live item, the cross-model CV of |Δ| (ε-guarded; items
>   with undefined CV skipped and counted); average over items → `process_cv_item_grain`.
> - *Content (per-item grain):* for each item, the cross-model CV of per-item mean standard-
>   condition stance (denominator ≥ 1 on a 1–5 scale, never degenerate); average → 
>   `content_cv_item_grain`.
> - **Downgrade rule:** if the primary G1 is a numeric PASS but the sensitivity reverses
>   (`process_cv_item_grain ≤ content_cv_item_grain`), the G1 verdict is downgraded to
>   **PROVISIONAL** — same outcome category and consequences as the G1-b thin-base downgrade
>   (build may start; 9-model confirmation + dead-cell audit gate P2 spend). This adds a third
>   trigger to the protocol §4 PROVISIONAL row.
> - The sensitivity NEVER softens a FAIL (G-all: no softening beyond the named paths). A FAIL
>   with reversed sensitivity is reported as context for the V-1 re-run adjudication only.

Implementation is fix F-5. Rationale: the amendment neutralizes exactly the anti-conservative
masking channel while keeping the frozen primary intact and the post-window adjudication mechanical.

## SA-3 — Frame rendering (D8/X3). RATIFIED; no pre-run hand-tuning.

**Verified.** The frame wraps the ALREADY-condition-rendered prompt (`orchestrator.py:270-300` →
`apply_frame(base, …)`); wrappers are verbatim from the bank builder and drift-guarded
(`test_frame_wrappers_match_bank_builder`). For `forced_immediate`, the authored bank variant
PREPENDS the 16-token instruction to the scenario, so the reader order is: monitored = [EVALUATION
NOTICE] → 16-token instruction → scenario; unmonitored = casual opener → 16-token instruction →
scenario → casual closer. The instruction is never buried mid-embed.

**Ruling.** Runtime re-wrapping is not merely acceptable — it is REQUIRED by the 5×2 factorial
(the bank pre-rendered frames on the base only; a pre-rendered-only run could not cross frame ×
condition). RATIFIED. The register clash (e.g. "Note to self, thinking this through before I
decide tomorrow." immediately followed by the imperative "Respond in 16 tokens or fewer") is real
but already governed by the frozen IB wrapper note: **hand-tune only if the compliance gap shows
frame-detection artifacts.** No per-condition hand-tuning before the real run.

**Binding addition.** Mandatory reporting (protocol §5.3) gains a per-condition×frame compliance
breakdown, specifically the `forced_immediate` × unmonitored 16-token compliance rate. If the X3
gap is concentrated in `forced_immediate` cells, that fires the IB hand-tune path BEFORE P1 — it
is a wrapper artifact to fix at the next regeneration, not a P0 invalidation. Embed assignment is
deterministic per item (sha256 → one of 4 embeds); disclose, do not randomize mid-P0.

## SA-4 — G3 fallback contrast. RATIFIED, with disclosure.

**Verified.** Direction = sign(mean(`extended_thinking`) − mean(`greene_fallback`)) per item per
frame, zero-banded at `min_effect=0.02`; pass iff one sign holds for ≥4/5 items in BOTH frames;
IB-2's M030 pole-aligned-consistent path implemented (`gates.py:293-385`).

**Ruling.** RATIFIED. G3-a (frozen) itself designates the `greene_fallback_prompt` arm
(agent-patient + time-pressure) as the M3 fallback pole, and IB-2's pole-alignment analysis was
performed on those exact prompts — the poles (act = consequentialist-favored) are defined on that
arm. Substituting `forced_immediate` as a "purer" speeded pole would detach G3 from IB-2's
verified alignment and from G3-a's wording. `extended_thinking` is the correct deliberation pole
(the only deliberation-enhancing resource condition).

**Binding disclosures.** (a) The contrast is COMPOSITE — deliberation vs personal-force +
time-pressure, as in the classic paradigm; the write-up must not attribute direction to time
budget alone. (b) `min_effect=0.02` is a new constant: pin it in the run config and disclose it.
(c) `greene_direction` hardcodes both frames — consistent with SA-8's required flags.

## SA-5 — D10 Codex structured signal. OVERTURNED → F-1 (blocking).

**Verified.** `adapters.py:291-302`: any `returncode != 0` → `refusal_flag=True`, stderr captured
but unclassified; orchestrator then skips the scorer and records
`refusal_category="explicit_refusal"` (`orchestrator.py:358-365`). There is NO retry anywhere in
either adapter or the orchestrator; a completed cell is checkpointed and never re-called, so a
transient failure is recorded as a refusal PERMANENTLY across resumes. `subprocess` timeout
propagates uncaught.

**Ruling.** OVERTURNED. `returncode != 0` conflates administration errors (auth failure, network,
rate limit, CLI crash) with model refusals. This corrupts two protocol-mandated quantities at
once: the §5.3 refusal category counts (fabricated "explicit_refusal" records) and the scored
distributions (silent cell deletion → PS and dead-cell accounting bias). The D10 spec sentence —
"Refusal = no stance taken; classify via scorer output" — already names the correct mechanism for
a vendor with no structured refusal signal: **Codex has no structured refusal signal; its content
refusals are the scorer-returns-None path, full stop.**

**Fix F-1 (blocking; spec-quoting tests required).**
1. Codex `returncode != 0` = administration error: bounded retry with exponential backoff
   (root-CLAUDE.md API rule), then RAISE fail-loud. Never a refusal; never checkpointed as
   complete.
2. Codex `refusal_flag` is always False; content refusal = scorer→None → `"no_stance"`.
3. Anthropic adapter gains the same bounded retry for transient API errors (rate-limit/
   overloaded/network); persistent errors raise. `stop_reason=='refusal'` handling is FAITHFUL
   and unchanged.
4. Mandatory reporting gains administration-error counts per vendor, reported SEPARATELY from
   refusal counts, plus the vendor asymmetry disclosure (Anthropic has a structured refusal
   signal; Codex does not).
5. Tests: a nonzero-returncode administration must produce NO record (raises after retries); a
   scoreless Codex completion must route scorer→None→`"no_stance"`.

## SA-6 — UNMEASURABLE detection (V-4). OVERTURNED → F-2 (blocking).

**Verified.** `_cell_state` keys UNMEASURABLE on `condition in unmeasurable_conditions` — bare
condition NAMES (`gates.py:66-70,105`); cells are (model, item, condition) but the flag is
condition-wide across ALL models. Records carry NO temperature field (`orchestrator.py:382-405`);
temperature is one run-level scalar (0.7, enforced >0 at `orchestrator.py:240-241`) sent on every
call — **including `extended_thinking` with `thinking={"type":"adaptive"}`. No V-4 drop path
exists anywhere.** Since the Anthropic API rejects modified temperature with extended thinking,
the V-4 conflict is expected to fire on the first thinking call and (with no try/except) abort
the run — the flag is downstream accounting for an upstream mechanism that was never wired.

**Ruling.** OVERTURNED, two grounds. (a) V-4 is vendor-specific (Anthropic thinking×temperature);
a condition-name flag miscodes non-Anthropic SD≈0 cells in the same condition as UNMEASURABLE,
removing genuinely-dead cells from the G1-b denominator — live fraction inflated, thin-base guard
weakened: anti-conservative on a fork-relevant floor. (b) It depends on the operator remembering
to set a flag after observing runtime behavior, out-of-band of the data. The right key is the
per-record administration config, which is exactly what V-4's trigger IS.

**Fix F-2 (blocking; spec-quoting tests required).**
1. Implement the V-4 drop itself: for Anthropic `extended_thinking`, send the API-compatible
   temperature (unset/default per current API requirement); all other calls keep the run
   temperature.
2. Every record carries `requested_temperature`, `effective_temperature`, and a boolean
   `v4_temp_drop`.
3. UNMEASURABLE iff SD≈0 AND all records in the (model, item, condition) cell have
   `v4_temp_drop=True`. The caller-supplied override may remain for patterns the automatic path
   misses, but scoped to (model_id, condition) tuples — bare condition names are removed.
4. Test quoting V-4: an SD≈0 cell in the same condition WITHOUT the drop (e.g. a Codex cell)
   must be coded DEAD, not UNMEASURABLE.

## SA-7 — M030 keying. CONFIRMED for this bank; robustness fix F-3.

**Verified.** Run-bank Greene IDs are `DPX-P0-M004/M006/M010/M012/M030`; the full bank is
`DPX-P0-{M001…M048, X001…X005, C001…C012}` — no ID contains `M030` as a substring of a different
item, so `"M030" in item_id` (`gates.py:352-353`) is safe on THIS bank, by numbering luck. The
test fixtures, however, use bare `"M030"` IDs, so nothing pins the real `DPX-P0-` form.

**Fix F-3 (pre-run, cheap).** Default marker becomes an exact-suffix or exact-ID match
(`endswith("-M030")` or `item_id == "DPX-P0-M030"`), and a new test loads the REAL bank JSON and
asserts the marker matches exactly one item — the Greene M030.

## SA-8 — Run entrypoint. BINDING RUN PRECONDITION → F-4.

**Verified.** No production caller constructs the orchestrator anywhere in the tree; every
construction is in `tests/`. Constructor defaults (`frames=None`,
`administer_greene_fallback=False`, `strict_prompts=False`) silently yield a single-frame run in
which X3 is uncomputable, G3 fallback has no `greene_fallback` records and every sign is 0, and
`load_injected` falls through to a generic suffix incompatible with the R-2 compliance coder — no
error raised anywhere.

**Ruling.** Wiring and testing the entrypoint is now a BINDING precondition for the real P0 run
(elevating checklist "Run flags" from advisory to gate). **Fix F-4:** a `run_p0.py` that wires
roster adapters, `frames=["monitored","unmonitored"]`, `administer_greene_fallback=True`,
`strict_prompts=True`, explicit `high_condition`/`low_condition` (SA-1.1), `min_effect` (SA-4.b),
`g1_unmeasurable_conditions` per F-2's scoped form, the bank via `load_item_bank`
(`items/20260706-p0-item-bank.json`), and the obfuscation-QA gate BEFORE scoring; plus (i) a test
asserting the constructed orchestrator carries exactly these flag values and (ii) a mock-adapter
smoke test running entrypoint → records → all three gates end-to-end.

## SA-9 — Test-overfit spot-check. CLEAR.

The Opus reviewer found NO new test certifying code behavior over the spec sentence; the
spec-critical tests (D11 cross-process seeds, D9 polarity reflection, D10 composed
adapter+orchestrator, V-4 both-exclusions, D5 no-cancellation) derive their expected values from
the ruling sentences and would fail under the guarded divergences. One coverage gap — fixtures use
bare `M030` IDs — is closed by F-3.

---

## Fix-package summary (all Opus-executable; no further Fable review required)

| Fix | Scope | Blocking real P0 run? |
|-----|-------|----------------------|
| **F-1** | Codex admin-error/refusal separation + retry/backoff both adapters + reporting split | **YES** |
| **F-2** | V-4 drop implementation + per-record temperature + (model, condition)-scoped UNMEASURABLE | **YES** |
| **F-3** | M030 exact-suffix marker + real-bank ID test | YES (trivial; bundle) |
| **F-4** | `run_p0.py` entrypoint wiring all pinned flags + smoke test | **YES** |
| **F-5** | A-1 per-item-grain sensitivity + PROVISIONAL downgrade in G1 output | **YES** (fork-relevant) |

Non-blocking (run/write-up time): SA-3 compliance breakdown, SA-4 disclosures, SA-5.4 reporting
split (lands with F-1), SA-1.1 write-up sentence.

**Post-fix protocol:** Opus lands F-1…F-5 red→green with spec-quoting tests (each test quotes the
governing sentence from THIS memo or the protocol), re-runs the full suite, and appends a row per
fix to the checklist-evidence table. A non-building audit pass over F-1/F-2 only (the two
overturns) is required — same WS-1 §3 standing order that caught the relocated D10. No further
Fable gate: this memo pre-specifies the fixes narrowly enough for mechanical execution; anything
discovered outside their scope follows the protocol's STOP-and-escalate rule.

*Fable, 2026-07-09. Binding alongside the 2026-07-05 adjudication memo, the P0 adjudication
protocol (as amended by A-1), and IB-1…5. Supersedes nothing.*
