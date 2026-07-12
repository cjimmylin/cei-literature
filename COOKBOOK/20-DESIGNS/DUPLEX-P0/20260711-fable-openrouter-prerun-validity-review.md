# 20260711 — Fable Pre-Run Validity Review: OpenRouter-Integrated DUPLEX-P0 (BINDING)

> **Authority.** Fable main loop, 2026-07-11, inside the Fable window (final day). This memo is the
> binding pre-run validity go/no-go the boot prompt
> (`20260710-fable-openrouter-prerun-validity-boot-prompt.md`) commissioned; it fulfills that
> prompt's deliverable (dated today per report-naming rules — the prompt anticipated a 07-10
> session). Scope: **only the validity deltas introduced by the OpenRouter pivot** (commits
> `a003626a9`, `16e3efdc…/16e3ebf5f`, `ebe3a4fde`). It does not relitigate the Session-A rulings
> (SA-1…SA-9, F-1…F-5, A-1), the P0 adjudication protocol (H-1…H-3, V-1…V-4, G1-a/b, G2-a/b,
> G3-a, G-all), the CS/IB/PS series, the native-Anthropic + G3-fallback decisions, or the choice
> of OpenRouter as the cross-family vendor.
>
> **Method.** Fable read, in the main loop: the two OpenRouter evidence docs (2026-07-09 addendum,
> 2026-07-10 live-validation memo), `config/p0-roster.yaml`, `run_p0.py` in full,
> `runner/adapters.py` in full, `runner/judges.py`, `runner/roster.py`, the G2 and condition-config
> regions of `analysis/gates.py` / `runner/orchestrator.py`, and the three frozen-context docs.
> Targeted greps verified: `judge_neutrality_check` is wired into no run path; `supports_thinking`
> is read by no code; records persist no response metadata. No code was written; no live call was
> made; secrets were not read.

## Verdict

**CONDITIONAL-GO.** The OpenRouter configuration is validity-cleared for the paid P0 run
**conditional on amendments OR-1…OR-7 below** (all Opus-executable with spec-quoting tests; none
needs further Fable review). The single most serious finding is **not** in the reviewed judge fix
— it is the same reasoning-token starvation mechanism, live-proven at the judge call site,
recurring **unpatched on the OpenAI subject side of the `forced_immediate` condition**
(`max_tokens=16` to always-reasoning SKUs → empty completions → the G1 low pole and G3 intuitive
pole silently wiped for the entire OpenAI vendor). That is fork-corrupting and blocking (OR-1).
The judge fix itself is ratified, with observability and parsing constraints (OR-2, OR-3).

| Delta | Ruling | Amendments |
|---|---|---|
| V-Δ1 reasoning-judge validity | **VALID-WITH-CONSTRAINT** (and one blocking subject-side finding) | OR-1, OR-2, OR-3, OR-4 |
| V-Δ2 provider-routing variance | **VALID AS-IS for P0** — pinning NOT required; observability required | OR-5 (+ pre-reg condition) |
| V-Δ3 mixed-transport judge asymmetry | **HOLDS at family level** (arithmetically bounded at G2) | OR-6 (disclosure only) |
| V-Δ4 model-SKU drift | **VALID** — ids are the design-named SKUs | OR-5 (drift logging) |
| V-Δ5 H-1 + judge-eligibility | **RATIFIED**, with judge-selection correction + one stale-metadata fix | OR-4, OR-7 |
| V-Δ6 judge-budget cost/feasibility | **FEASIBLE** — no gate; estimate + approval step stands | OR-7(e) |

---

## V-Δ1 — Reasoning-model judge validity. VALID-WITH-CONSTRAINT.

**Ratified.** Letting the judge reason before emitting a 1–5 stance is not, in itself, a bias
threat: the judge task is a bounded *reading/extraction* task (locate the subject's stance on a
defined scale), not an open judgment task, and deliberation on a reading task plausibly improves
reliability rather than tilting it. The instrument designed to catch directional judge bias — the
KB07 §2 mirror-flip neutrality check — exists in code (`runner/judges.py::judge_neutrality_check`)
and is the correct detector; it is currently **wired into no run path**, which OR-7(c) corrects at
smoke time. `_JUDGE_MAX_TOKENS = 2048` is ratified as the run budget.

**Constraint 1 — truncation must be observable, never silent (OR-2, blocking).** The live evidence
is one call (`gpt-5-mini`, 2000 tokens → `'5'`). It establishes the mechanism, not a distribution:
reasoning length varies by item, and a judge call whose reasoning overruns 2048 returns an empty
visible completion that is **indistinguishable from a content refusal** under the current code —
it silently codes `no_stance`, and only for the vendor-asymmetric direction (OpenAI judge scores
only Anthropic subjects). Differential truncation across items would therefore delete
harder/longer-reasoned Anthropic-subject cells asymmetrically — exactly the silent-corruption
class this review exists to block. A floor is NOT the fix (any fixed cap can be overrun); the fix
is fail-loud: `finish_reason`/usage must be read on every judge call, and an
empty-completion-with-length-stop is an ADMINISTRATION-class defect (retry escalated, then raise),
never `no_stance`.

**Constraint 2 — first-match stance parsing is unsafe against a verbose reasoning judge (OR-3,
blocking).** `_JUDGE_STANCE_RE.search` takes the FIRST `[1-5]` digit anywhere in the completion.
Reasoning models frequently restate the scale ("On a 1–5 scale, I rate this 4") — first-match
returns **1**, a silent in-range corruption strictly worse than `no_stance` because nothing counts
it. The single clean live `'5'` does not establish that the run-scale output distribution stays
this terse. Strict-parse + one constrained re-ask + defect logging is required.

**Blocking subject-side finding — the same starvation mechanism, unpatched (OR-1).**
`orchestrator.condition_config` sends `max_tokens=16` for `forced_immediate` to **every** vendor.
The 2026-07-10 live evidence proves precisely what 16 tokens does to a `gpt-5-*` SKU on OpenRouter:
reasoning consumes the whole budget and the visible completion is `''`. Consequence at run time:
every OpenAI-subject `forced_immediate` cell (2 models × 65 items × 2 frames × 10 reps = 2,600
records) returns empty → scorer → `no_stance` → excluded from scored distributions. That destroys
(a) the G1 process contrast's pinned low pole (SA-1.1) for the whole OpenAI vendor, (b) G3's
intuitive condition, and (c) floods the §5.3 refusal counts with fabricated `no_stance` records —
the same corruption class as the OVERTURNED SA-5, one layer down. It would surface only
post-spend, as an inexplicable vendor-conditional refusal wall. Relatedly, `extended_thinking`'s
`thinking={"type":"adaptive"}` dict is silently swallowed by `OpenAIAPIAdapter` (`**_`), so the
deliberation pole for OpenAI subjects is currently prompt-suffix-only atop default reasoning —
the process manipulation must be made real on this vendor via the reasoning-effort knob (OR-1),
or the cross-vendor G1/G2 comparison administers different manipulations under one label.

## V-Δ2 — Provider-routing variance. VALID AS-IS for P0; pinning NOT required.

`openai/gpt-5-codex` and `openai/gpt-5-mini` are **closed-weight, first-party SKUs**: OpenRouter
cannot route them to third-party hosts or quantized variants the way it can open-weight models —
the realistic provider set is OpenAI (possibly Azure-OpenAI) serving the same weights. The residual
risks are version drift and endpoint-class differences, both of which are **observability**
problems, not pinning problems. Ruling:

- Provider-pinning (`allow_fallbacks:false`) is **NOT required for the P0 pilot**. Building it now
  is not justified by the threat model for these SKUs.
- **Pre-registered condition:** every record must persist the OpenRouter-reported `provider` and
  response `model` (OR-5). Post-run, the run session computes distinct-provider counts per
  (model_id, resource_condition) cell: >1 provider in any cell → mandatory disclosure in the run
  report; provider mix **correlated with condition** → the affected gate result is not adjudicated
  mechanically — STOP-and-escalate (protocol §4 last row). Provider-pinning becomes **REQUIRED
  before any scored measurement beyond P0** (P1/P2 or a publication claim), or immediately if P0
  observes mixing.

## V-Δ3 — Mixed-transport judge asymmetry. HOLDS at family level.

The §3.5 threat model is about model *families* (one family must not both produce and score the
measured behavior). With two vendors, judge-family asymmetry is **inherent to the frozen design**
— Anthropic subjects were always going to be scored by an OpenAI-family judge and vice versa; the
OpenRouter pivot adds only a transport asymmetry perfectly nested inside that judge-family
asymmetry (each judge family rides exactly one transport, constantly). Gateway-as-transport is
sound for these SKUs: OpenRouter forwards Chat Completions to the first-party endpoint and the
adapter sends no gateway-specific behavior-modifying options.

Where a judge-family *calibration offset* could bite, the gates are already structurally guarded:

- **G1 process axis:** per-item condition-deltas within model — an additive judge offset cancels
  in the delta. **G1 content axis:** offset inflates cross-model dispersion of levels →
  `content_cv` rises → G1 gets *harder* to pass. Conservative direction; no action.
- **G2** (verified in `analysis/gates.py::pairwise_separation`): Welch tests on raw stance levels
  per condition — a judge-family offset inflates **cross-vendor** pair separation. But at 5
  subjects the ≥90% bar is 9/10 pairs, and only 6 pairs are cross-vendor: a pass arithmetically
  requires ≥3 of the 4 **within-vendor** (same-judge) pairs to separate, which a judge offset
  cannot produce. The offset can pad a marginal pass, not manufacture one. OR-6 makes the split
  visible (disclosure only, no gate change); it matters more at the 9-model confirmation.
- **Judge noise** (as distinct from offset) inflates per-item |Δ| under D5 (the mean of |signal +
  noise| exceeds |signal|), an anti-conservative pressure on the G1 numerator, differential if one
  judge is noisier. Handled by pinning judge temperature to 0 (OR-4) and by the mirror-flip
  neutrality check at smoke (OR-7c).

**Recommendation-to-Jimmy (non-directive, per boot-prompt authorization):** no judge-asymmetry
threat found that would reopen the declined both-vendors-via-OpenRouter option. If OR-5 logging
later shows transport-correlated judge defects, moving both families onto one transport is the
clean remedy; nothing in this review requires it.

## V-Δ4 — Model-identity drift. VALID.

`openai/gpt-5-codex` and `openai/gpt-5-mini` are the OpenRouter forms of exactly the SKUs design
§3.5 names ("GPT-5 Codex", "GPT Mini"). The catalog's newer gpt-5.1…5.6 entries do not create an
H-1-analogue: H-1 fired because the named SKU was *retired*; here both named SKUs are live and
reachable. Substituting newer SKUs the design did not name would itself be drift. The two SKUs
also satisfy the cross-family discrimination requirement as a capability-spread pair
(full-size coding-tuned vs mini), consistent with the design's intent of heterogeneous subjects.
Constraint: OR-5's per-record `response_model` logging is the drift detector — if OpenRouter
re-points the alias mid-run, it is caught in the data, and any mid-run `response_model` change is
a mandatory disclosure + STOP-and-escalate if it straddles conditions. The run report should also
record the catalog-fetch date (2026-07-10, 347 models) in the roster disclosure.

## V-Δ5 — H-1 ratification + judge-eligibility. RATIFIED, with corrections.

**H-1: RATIFIED.** The roster entry applies the ruling faithfully: `claude-haiku-4-5`, substitute
not pin, disclosure text naming the protocol section, non-replication explicitly de-fanged (H-2
intact), `judge_eligible: false` (correct — the weakest subject and H-3's artifact-check target
should not also be an instrument). No gate assumption is disturbed: H-2 already severed MP-DP
replication from P0 pass/fail, and G1/G2/G3 are subject-set-agnostic beyond V-1's 5-of-9 handling.

**Two corrections:**
1. **Stale capability metadata.** The H-1 entry carried over `supports_thinking: false` from
   retired Haiku 3.5, but Haiku 4.5 supports extended thinking. The key is read by **no code**
   (verified — thinking is keyed on condition in `condition_config`, and the Anthropic adapter
   forwards it for all Anthropic models), so it is inert at run time, but it is misleading
   metadata on the load-bearing config. Correct it to `true` (or delete the key with a comment),
   and — decisive check — OR-7(a) must include a live `claude-haiku-4-5` × `extended_thinking`
   smoke cell: if the `{"type": "adaptive"}` thinking block 400s on Haiku 4.5, **STOP and
   escalate**; do not improvise a per-model thinking shim mid-run.
2. **Judge selection is currently a roster-order accident.** `make_judge_scorer` takes
   `judges[0]`, i.e. the first cross-vendor `judge_eligible` model in YAML order. That silently
   pins **`openai/gpt-5-codex`** — a coding-tuned SKU whose judging was never live-validated (it
   was only reachability-checked; the clean `'5'` came from `gpt-5-mini`) — as the judge for all
   Anthropic subjects, and **`claude-opus-4-6`** — the most expensive Anthropic model — as the
   judge for all OpenAI subjects. The `judge_eligible` *set* is valid; the implicit *selection*
   is not acceptable for a scored run. OR-4 pins the tier-symmetric mid pair explicitly:
   `openai/gpt-5-mini` (the live-validated judge) and `claude-sonnet-4-6`.

## V-Δ6 — Judge-budget cost / feasibility. FEASIBLE; no gate.

Scale (from roster × bank, deterministic): 5 subjects × 65 items × 4 conditions × 2 frames × 10
reps = 26,000 administrations, + 500 `greene_fallback`-arm records, + 325 recognition-QA calls,
+ ≈26,500 judge calls ≈ **53,300 API calls**. Banded estimate under stated assumptions (list-price
assumptions, actual output ~0.25–1k tokens/call, extended-thinking cells up to 4,096 billed output
tokens; the run session's per-request estimator is the binding number, this band is the surprise
check):

- Dominant line: **Opus 4.6 as subject** (5,300 calls, ~1,325 of them extended-thinking) —
  order $200–400.
- Sonnet + Haiku subjects: ~$60–100 combined. OpenAI subjects via OpenRouter (reasoning tokens
  billed): ~$50–90 combined.
- Judges **with OR-4** (mini + sonnet, temp 0, effort low): ~$40–80. Without OR-4 (codex + opus
  by list-order accident): roughly $150–250 *more* — OR-4 is also the main cost lever.
- **Total order $350–700.** Not a surprise-risk at the approved-pilot scale, but the pre-run
  estimate + Jimmy approval step (already a precondition) stands, now fed by OR-5's usage logging
  from the smoke.
- Wall-clock: ~53k serial calls ≈ 30–75 h. The checkpoint/resume path makes this survivable;
  any concurrency addition is an ordinary Opus code change under the same test discipline, not a
  validity matter. OpenRouter 402-reservation risk: caps are ≤4,096 everywhere — no reservation
  blowup at a sane balance; top up before the run regardless.

---

## Pre-registered amendments OR-1…OR-7 (apply mechanically; spec-quoting tests each)

**OR-1 (BLOCKING) — OpenAI-family reasoning control per resource condition.**
1. `OpenAIAPIAdapter.administer` gains a `reasoning: Optional[dict]` parameter, sent via the SDK's
   `extra_body` as OpenRouter's unified `reasoning` field (e.g. `{"effort": "minimal"}`). Absent →
   omitted entirely (provider default).
2. Vendor-conditional condition overlay (mirror of the V-4 vendor-specific pattern), applied where
   the orchestrator resolves `condition_config` for `vendor == "openai"`:
   - `forced_immediate` → `reasoning={"effort": "minimal"}` (or the SKU's lowest supported
     effort), `max_tokens=64` — NOT 16. The 16-token *answer* limit stays enforced by the authored
     in-prompt instruction + the SA-3 compliance coder, as it already is semantically for every
     vendor; 64 is headroom so a minimal reasoning preamble cannot zero the visible answer.
   - `extended_thinking` → `reasoning={"effort": "high"}`, `max_tokens=4096` (makes the
     deliberation pole REAL on this vendor; the swallowed Anthropic `thinking` dict must never be
     sent — assert this in a test).
   - `standard` / `load_injected` → no reasoning override, `max_tokens=1024` (unchanged).
3. Smoke ladder (OR-7): if the `forced_immediate` visible completion is empty at 64, step
   64→128→256 and pin the smallest non-empty value in the run config; record the pinned value in
   the roster disclosure.
4. Disclosure (protocol §5 item 2, V-3 precedent): the write-up discloses the vendor-conditional
   operationalization — Anthropic `forced_immediate` is API-capped at 16 tokens; OpenAI is
   instruction-capped with `effort=minimal` at a 64-token API cap — and the SA-3 compliance
   breakdown is reported **per vendor** as well as per condition×frame.
5. Tests: openai `forced_immediate` carries `effort=minimal` + `max_tokens>=64`; anthropic path
   byte-identical to today (16-cap intact); `thinking` dict never reaches the OpenAI adapter call.

**OR-2 (BLOCKING) — Judge truncation observability + escalation.**
1. `make_judge_scorer` reads `finish_reason` (and `native_finish_reason` where present) + `usage`
   (incl. reasoning tokens) from every judge response.
2. Empty visible completion OR a length-class finish ⇒ ADMINISTRATION-class judge defect: one
   retry at 4× budget (8,192); still defective → raise `AdministrationError` (fail-loud; the cell
   is never checkpointed as complete). A truncated judge NEVER silently codes `no_stance`.
3. Judge-call sidecar log `results/p0-judge-calls.jsonl`: judge_id, subject vendor, finish_reason,
   usage, parse outcome (OR-3), retry count.
4. §5.3 reporting gains per-judge-direction defect counts (truncation, parse failure), reported
   separately from subject refusal categories (extends the F-1 reporting split).

**OR-3 (BLOCKING) — Strict stance parse.**
1. Replace the first-match `\b([1-5])\b` search with a strict parse: the stripped completion must
   fullmatch a single integer 1–5 (tolerating only surrounding whitespace / one trailing period).
   Governing failure mode: a verbose judge restating "on a 1–5 scale" makes first-match return
   **1** — silent in-range corruption that no defect counter sees.
2. Strict-parse failure → ONE re-ask with a harder constraint appended ("Reply with exactly one
   character: 1, 2, 3, 4, or 5.") → still unparseable → `None` (`no_stance`) + parse-defect entry
   in the OR-2 sidecar.
3. Tests: `"On a 1-5 scale, I rate this 4"` must NOT yield 1 (re-ask path); `"4"` and `"4."`
   parse; `""` routes to OR-2, not to `no_stance`.

**OR-4 (BLOCKING) — Judge pinning + determinism.**
1. `config/p0-roster.yaml` `judge_routing` gains
   `pinned: {anthropic: "openai/gpt-5-mini", openai: "claude-sonnet-4-6"}`;
   `assign_judges` honors the pinned map first (asserting the pinned judge is enabled,
   cross-vendor, and `judge_eligible` — else fail loud), falling back to the existing pool logic
   only if no pin is set.
2. Judge temperature pinned to **0** (`make_judge_scorer(..., judge_temperature=0.0)` in `main`),
   routed through the existing F-2 `effective_temperature` gate. Disclosed in the run config.
3. Judge reasoning effort **low** via OR-1's knob (cost + truncation margin; correctness is
   already guarded by OR-2).
4. Also correct the V-Δ5 stale metadata: `claude-haiku-4-5` `supports_thinking: true` (or delete
   the unread key with a comment).
5. Tests: pinned routing returns exactly the pinned id per direction; a same-vendor or disabled
   pin fails loud; judge call carries temperature 0 + effort low.

**OR-5 (BLOCKING) — Response-metadata persistence.**
1. Every subject record gains: `response_model` (the response's `model` field), `provider`
   (OpenRouter-reported upstream provider; `None` on native Anthropic), `finish_reason`
   (`stop_reason` for Anthropic), and `usage` token counts (incl. reasoning tokens where
   reported). Extracted from the existing `AdapterResult.raw`; do NOT persist full raw bodies.
2. Post-run mandatory check (run session): distinct `provider` and `response_model` values per
   (model_id, resource_condition) cell — >1 provider in a cell → disclose; provider or
   response_model mix correlated with condition → STOP-and-escalate (protocol §4 last row).
3. Tests: mock responses with provider/model/usage fields land on the record; Anthropic records
   carry stop_reason; absent fields degrade to None, never KeyError.

**OR-6 (reporting, additive — no gate change) — G2 within/cross-vendor split.**
`pairwise_separation` output gains, per condition, the separated fraction split by within-vendor
vs cross-vendor pairs. Rationale: a judge-family calibration offset can inflate only the
cross-vendor pairs; the split makes a judge-confounded margin visible at adjudication time and is
load-bearing at the 9-model confirmation (V-1). This is a §5 mandatory-reporting addition in the
spirit of A-1: it never softens or hardens the G2 verdict itself.

**OR-7 (BLOCKING) — Expanded pre-run smoke (supersedes the "1-item both-vendor smoke").**
A full **model × condition mini-matrix**: 5 subjects × 5 conditions (4 resource conditions +
`greene_fallback`) × 1 item × 1 rep, single frame (frames alter prompts, not API params), scored
through the real pinned judges — ~25 subject calls + ~25 judge calls, order $1–3. Must verify:
(a) every cell returns a non-empty visible completion — in particular OpenAI `forced_immediate`
    under OR-1 (run the OR-1.3 ladder here) and `claude-haiku-4-5` × `extended_thinking`
    (adaptive-thinking acceptance; 400 → STOP-and-escalate, no mid-run shim);
(b) both judge directions on real subject outputs at the pinned config (strict parse OK,
    finish_reason is a stop-class, usage logged);
(c) the mirror-flip neutrality check (`judge_neutrality_check`, currently wired into no run path)
    executed in BOTH judge directions on one authored pro/con mirrored answer pair for one bank
    item; `abs_flip_delta > tol (0.05)` on either judge → STOP-and-escalate (judge bias), not a
    silent proceed;
(d) auth modes report as expected (`api_key` for OpenRouter; the intended Anthropic chain per
    `check_anthropic_env`);
(e) per-request cost actuals from the smoke extrapolated to the V-Δ6 scale table → **Jimmy
    approves the number before the paid run**.

---

## Conditions the run session MUST satisfy (consolidated, binding)

1. OR-1…OR-5 implemented red→green with spec-quoting tests; full suite green; a row per amendment
   appended to the checklist-evidence table (new dated addendum, not an edit).
2. OR-7 smoke executed and passing AFTER the code lands, BEFORE the paid run; OR-7(e) cost
   approval from Jimmy on record.
3. OR-6 present in the gate output before adjudication.
4. Existing preconditions unchanged: Anthropic credential; `check_anthropic_env` clean;
   obfuscation-QA gate before scoring; A-1 sensitivity computed; adjudication strictly per the
   protocol + Session-A amendments + this memo.
5. Any live behavior outside the patterns pre-registered here (e.g. Haiku thinking 400, judge
   neutrality failure, provider mixing correlated with condition, an OR-1 ladder exhausted at 256)
   → **STOP and escalate to Jimmy**; never improvise a lower-tier judgment.

## Run-session preconditions block (for the post-credential **Opus** session — mechanical)

1. `git log -1` staleness check; read this memo + the boot prompt + the 2026-07-10 live-validation
   memo. Lane = `COOKBOOK/20-DESIGNS/DUPLEX-P0/` only; path-scoped staging.
2. Land OR-1…OR-6 (TDD, spec-quoting tests; suite currently 144 — expect growth), new dated
   checklist addendum.
3. Source secrets (`~/.codex/secrets/openrouter.env`; Anthropic credential from Jimmy — prefer the
   auto-refreshing profile per F-1; never echo/commit values). Top up OpenRouter balance.
4. Run the OR-7 smoke matrix → fix only what OR-1.3's pre-registered ladder covers → anything else
   STOP-and-escalate.
5. Present the OR-7(e) cost estimate → Jimmy approval.
6. `run_p0.py` (checkpointed; resume on interruption; expect 30–75 h serial wall-clock).
7. Post-run: OR-5 provider/model-drift check → mechanical P0 adjudication per the protocol
   (+A-1, +OR-6 disclosure, +this memo's escalation rows) → adjudication report (new dated file).

*Fable, 2026-07-11. Binding alongside the 2026-07-05 adjudication memo, the P0 adjudication
protocol (as amended by A-1), the Session-A review, and IB-1…5. Supersedes nothing; amends
additively (OR-6 reporting; OR-1 disclosure) and pre-registers run configuration (OR-1…OR-5, OR-7).*
