# WCF-Bench Codex Session 41 Handoff — PPP-1 Run and Paper Packet

**Started:** 2026-07-13  
**Closed:** 2026-07-14  
**Agent:** Codex  
**Validity label:** **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

## Paper-facing outcome

PPP-1 is complete. The one owner-authorized execution recorded all 678 cells, and the
offline exploratory manuscript packet is ready for Jimmy's review. The packet is a
descriptive, single-judge preview only. It does not support rankings, gates, release,
family-level or consensus claims, external quotation, T4 completion, or model
substitution.

## Frozen catalog refresh

Jimmy authorized one append-only refresh of the exact four PPP-1 catalog rows after a
below-256,000-token ceiling verification. The refresh preserved the exact three-SUT / one-
Gemini roster, base prices, 2,048/512 completion caps, retry rules, one-run boundary, and
strict `$23.56` NTE.

- All 226 Qwen SUT prompts were checked with system text included.
- Maximum prompt ceiling: 2,221 tokens at `MEND-C1-W301`.
- Headroom below the 256,000-token pricing override: 253,779 tokens.
- Catalog hash:
  `e97e482f8fc963ffe2e0743257e1d1041437ebdef1cbcf9babdb03c7b2d0318a`.
- Frozen run-manifest SHA-256:
  `f1121b2bd279a83053f2521c99a45b4d116c1399da78776f515dceb4f210d796`.
- Immutable refresh packet:
  `07-PILOTS/20260713-ppp1-catalog-refresh/`.

## One-run execution

Immutable run directory:
`07-PILOTS/20260713-ppp1-exploratory-preview/`.

- Scope: 226 runnable base items × three SUTs = 678 cells.
- SUTs, in frozen order:
  `meta-llama/llama-3.1-8b-instruct`, `deepseek/deepseek-chat`,
  `qwen/qwen3.7-plus`.
- Judge: `google/gemini-2.5-flash` where judging was required.
- Completion ceilings: SUT 2,048; judge 512.
- Calls recorded: 1,722.
- Runtime from first to last checkpoint: 9h46m18s.
- Final status: `COMPLETE`; 678/678 recorded, 618 scored, 60 error-recorded.
- Terminal stop: none. Budget hit: false.
- Retry/error-survival rule was followed; isolated errors were recorded, not debugged or
  rerun.
- The authorized one-run boundary is consumed. No resume or rerun is authorized.

### Cost reconciliation

- Actual-first accounting total: `$3.0552242489`.
- Strict NTE: `$23.56`; the run remained under the cap.
- Response-attributed total: unavailable because two calls used fallback accounting.
- Shared-key delta: `$13.7768984160`, contextual only. The account was used concurrently
  and its limit changed during the interval, so the delta is not attributed to PPP-1.
- Final custody status: reconciled.

## Exploratory manuscript packet

Review directory:
`08-PAPER/20260713-ppp1-exploratory-preview/`.

Start with:

1. `00-README.md` — scope and use restrictions.
2. `08-assembled-manuscript-preview.md` — paper-shaped review copy.
3. `05-preview-results.md`, `06-preview-discussion.md`, and
   `07-preview-limitations.md` — modular preview sections.
4. `04-traceability.md` and `03-traceability.csv` — field-level provenance.
5. `tables/` and `figures/` — denominator-explicit summaries and self-contained SVGs.

Descriptive headline-eligible summaries, with errors never imputed:

- Llama 3.1 8B: mean 0.3878; numeric 213/222; 9 errors.
- DeepSeek Chat: mean 0.7882; numeric 202/222; 20 errors.
- Qwen 3.7 Plus: mean 0.8449; numeric 192/222; 31 errors.
- Overall: mean 0.6656; numeric 607/666; item-cluster bootstrap 95% interval
  [0.6302, 0.7004].

These values are descriptive summaries in frozen roster order, not rankings. The 12
contested cells are excluded from the headline mean and retain separate disclosure,
coherence, and settled-core fields.

## Review and verification

- Catalog refresh: fresh implementation, specification review PASS, and quality review
  PASS.
- Packet: one specification review found bounded P1 traceability/denominator issues; one
  fix cycle closed only those named blockers; specification re-review PASS; subsequent
  quality review PASS.
- Offline suite: 733 tests green.
- Packet source manifest pins hashes for the immutable identity, checkpoint, raw ledger,
  metadata, report, frozen bank aggregate, and unchanged manuscript sources.
- Existing release-labeled manuscript sources were not edited.

## What remains

1. Jimmy reviews the immutable exploratory packet and may accept it, request a bounded
   paper-only correction, or reject its manuscript use. Never overwrite the packet; any
   correction must be append-only in a new dated path.
2. Registered confirmatory T4 remains later, unchanged, and unauthorized. Its separate
   cap choice remains OPEN in `PENDING-QUESTIONS.md`.
3. No paid inference, rerun, T4 work, perturbation, gate work, roster substitution, or
   release promotion is authorized by this handoff.

## Session allocation

Empirical 50% · paper 35% · infrastructure 10% · governance/admin 5%.
