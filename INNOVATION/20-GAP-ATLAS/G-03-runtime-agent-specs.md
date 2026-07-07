# G-03 — Runtime / Agent Specifications

**Stage A** · **Ratings S/T/F: M/M/L** · **Programs: acquisition-only (DL-04)** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
A 2026 cluster is building machine-readable, runtime-enforced behavior specifications for autonomous agents (deontic policies, Policy Cards, policy compilers) — the agent-world analogue of constitutions — and the vault has none of it.

## Why it matters                  [KERNEL — FROZEN]
As agents act rather than chat, "did the model follow the spec" becomes "did the system block the violating tool call" — a shift from evaluation to enforcement that changes what alignment evidence looks like. Severity M (still early, systems-flavored); CEI-fit L: this is runtime-verification engineering, not measurement science or normative analysis.

## Evidence                        (corpus + field)
**Corpus baseline:** zero.

**Field:** a 2026 cluster is building machine-checkable, per-tool-call specs — the enforcement analogue of the chat-model constitutions in G-01/G-02:
- **Deontic runtime policies** (⚠ arXiv:2606.19464): obligation/permission/prohibition semantics enforced at action time.
- **Policy Cards** (arXiv:2510.24383): machine-readable behavior specifications attached to agents.
- **AgentSpec / PCAS** (policy-conformance agent spec; ⚠ arXiv:2602.16708): compiling policy into runtime conformance checks.

The through-line: specification is moving from something you *evaluate after the fact* to something you *compile and enforce before the action executes*. That is a different evidentiary regime — the safety argument becomes "the violating call was blocked" rather than "the model scored X% adherent."

## State of the art
Early and systems-engineering-flavored; no dominant standard, no major agent-framework adoption yet. This is runtime-verification / policy-compilation territory, not measurement science or normative analysis — hence CEI-fit L and the explicit acquisition-only decision (DL-04). The one live CEI question is compatibility: are *enforceable* clauses a subset of *gradeable* ones? If SPECGRADE's clause registry (G-02) stays compatible with machine-readable formats, the bridge from a gradeable spec to an enforceable one is cheap the moment the adoption trigger fires.

## What closing looks like         [KERNEL — FROZEN]
M1 — cluster acquired and classified. M2 — a watching brief exists connecting runtime-spec semantics to SPECGRADE's clause taxonomy (are enforceable clauses a subset of gradeable ones?). M3 — trigger-based: if a major agent framework adopts one of these standards, re-rate the gap and consider a program.

## CEI response                    [KERNEL — FROZEN]
Acquisition-only, by explicit decision (DL-04): track via the field-map A-front watch-list; the SPECGRADE clause registry should stay compatible with machine-readable formats so the bridge is cheap if the trigger fires.

## OPUS-EXPAND checklist           (LIVING)
- [ ] ⚠ Verify the three flagged IDs (2606.19464, 2602.16708) resolve before any external citation; both are same-/near-month 2026 IDs.
- [ ] Write the M2 watching brief: map deontic/Policy-Card clause semantics onto SPECGRADE's clause-registry fields and record which enforceable-clause types have no gradeable analogue.
- [ ] Add a machine-readability compatibility note to the G-02 registry schema so the enforceable⊆gradeable bridge stays cheap.
- [ ] Check Front A watch-list trigger: has any major agent framework (LangGraph, OpenAI Agents, Claude agent SDK) adopted a runtime-spec standard? If yes, file a PR to re-rate this gap.
- [ ] Deep-read Policy Cards (2510.24383, non-flagged) as the least-uncertain anchor and summarize its schema into §State of the art.

## Sources                         (evidence classes marked)
- Policy Cards — arXiv:2510.24383 — **SEARCH-CONFIRMED** — least-uncertain anchor.
- Deontic Policies — arXiv:2606.19464 — **⚠ UNCONFIRMED** (2606 ID; verify-at-download).
- PCAS (policy-conformance agent spec) — arXiv:2602.16708 — **⚠ UNCONFIRMED** (2602 ID; verify-at-download).
- AgentSpec (cluster reference, per `../02-gap-atlas.md`) — **SEARCH-CONFIRMED** — no ID captured; confirm at acquisition.
