# I-20 — Runtime Agent Governance

**Tier 4** · **Gaps: G-03** · **Programs: acquisition (RP-01 SPECGRADE bridge)** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]

Machine-readable, runtime-enforced behavior specifications for agents — deontic policies checked per tool call, Policy Cards, policy compilers — moving alignment from "the model internalized the value" to "the system cannot execute the violation."

## Key results

- **Deontic policies** (⚠ 2606.19464 — ⚠ UNCONFIRMED): permission/obligation/prohibition policies checked per tool call.
- **Policy Cards** (2510.24383 — SEARCH-CONFIRMED): machine-readable behavioral policy artifacts for autonomous agents.
- **PCAS — policy-conformance agent spec** (⚠ 2602.16708 — ⚠ UNCONFIRMED); **AgentSpec** (named in the sweep, no ID captured — SEARCH-CONFIRMED): the agent analogue of constitutions, enforced rather than internalized.

## Mechanisms & caveats

The category shift is from *disposition* (did the model absorb the value?) to *coverage* (does the enforcement net catch the violation?). This is systems-engineering-flavored — CEI-fit is L (G-03 rated Severity M / Tractability M / CEI-fit L) — so the correct posture is acquisition and readiness, not leadership. The conceptual caveat is load-bearing for CEI's position work: enforced compliance is *not* alignment; a system that mechanically blocks a violation tells you nothing about the model's disposition, and the two diverge precisely under enforcement failure. Most citations are ⚠ UNCONFIRMED same-month IDs; AgentSpec lacks a captured ID.

## Implications for CEI practice   [KERNEL — FROZEN]

(a) Acquisition-only now (G-03), but keep SPECGRADE's clause registry machine-readable-compatible so the bridge is cheap. (b) Enforcement shifts the evaluation question from disposition to coverage — which violations does the policy net miss? — a future audit shape CEI's scenario craft fits. (c) Watch trigger: adoption by a major agent framework re-rates the gap. (d) Conceptual note for the position paper: enforced compliance is not alignment; the difference is measurable as behavior under enforcement failure.

## Cross-links

- **Gaps:** G-03 (runtime/agent specifications); adjacent G-01/G-02 (spec-adherence auditing, spec engineering → I-06/I-07).
- **Ideas:** I-06 (model specs & constitutions — the human-readable counterpart); I-07 (spec-adherence auditing — the disposition-side audit).
- **Programs:** RP-01 SPECGRADE (keep the clause registry machine-readable-compatible, kernel point a); acquisition-only otherwise.
- **Field map:** Front A — Specification (runtime-spec cluster); G-03 is "track it, don't lead it."

## OPUS-EXPAND checklist           (LIVING)

- [ ] Verify ⚠ 2606.19464 (deontic policies) and ⚠ 2602.16708 (PCAS) abstracts at download; recover the AgentSpec arXiv ID via title search.
- [ ] Fetch 2510.24383 (Policy Cards); extract the machine-readable schema and check it against SPECGRADE's clause-registry format (kernel point a — cheap-bridge audit).
- [ ] Draft the "coverage vs. disposition" audit-shape note (kernel point b): how CEI scenario craft would probe which violations a policy net misses.
- [ ] Write the position-paper conceptual note "enforced compliance is not alignment; measure the gap under enforcement failure" (kernel point d).
- [ ] Set the framework-adoption watch trigger that would re-rate G-03 above acquisition-only (kernel point c).

## Sources

- ⚠ 2606.19464 Deontic Policies; ⚠ 2602.16708 PCAS — ⚠ UNCONFIRMED (P3, G-03)
- 2510.24383 Policy Cards — SEARCH-CONFIRMED (P3, G-03)
- AgentSpec (sweep-named, ID not captured) — SEARCH-CONFIRMED
- Companion: `../02-gap-atlas.md` §G-03; `../03-newest-ideas-scan.md` #20; `../05-research-programs/RP-01-SPECGRADE.md`
