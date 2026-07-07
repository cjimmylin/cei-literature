# RP-10 COMMONS — Group-Level Value Dynamics in Agent Collectives

**Gaps:** G-17 (multi-agent value dynamics)
**Portfolio claim:** no-gold substrate / new-regime measurement · **Wave:** 3
**Author:** Fable 5 · 2026-07-07

## Motivation

The 2025–26 multi-agent results establish a second alignment problem above the agent level: LLM populations spontaneously converge on conventions; **collective biases emerge that no individual member exhibits**; small committed minorities tip whole populations; market agents converge on tacit collusion that prompt-level prohibitions cannot suppress; coordinated sabotage evades per-agent monitors. Deployment reality is heading toward agent collectives (org-chart agent teams, agent markets), so "every agent passed the values benchmark" is about to become the safety claim — and the emergence results say it doesn't compose. COOKBOOK sketch S3 QUORUM anticipated the topic; the literature now exists to build under it. The measurement question is unclaimed: the emergent-convention studies use *content-free* conventions (naming games); nobody has run the normative version.

## Core hypothesis

**H1 (non-compositionality):** Group-level value outcomes (norms adopted, harms tolerated, dissent suppressed) are not predictable from member-level CEI scores — the member→group mapping has emergent structure at experimentally accessible scales (3–24 agents).
**H2 (normative tipping):** Committed-minority tipping replicates when the convention is *normative* (a value-laden practice) rather than lexical — including tipping toward worse norms (a committed bad-actor agent shifts group behavior more than member scores predict).
**H3 (conformity asymmetry):** Individual agents' value expressions shift under group pressure (measured pre/post with member-level probes), and the shift is asymmetric — easier to erode costly norms (honesty under group defection) than to install them.

## Method sketch

1. **Testbed.** Small agent groups (3–24) on three task classes where norms have consequences: (a) naming-game variants seeded with normative content (what do we call/how do we treat X); (b) resource/market games (the collusion line's setup, with CEI value scenarios embedded); (c) collaborative document/decision tasks with embedded ethical choices (UNMARKED-style, delivered to the *group*).
2. **Member instrumentation.** Every agent gets member-level CEI probes before, during (unannounced, via task events), and after group interaction — the pre/post design is what the existing literature lacks.
3. **Manipulations.** Group size; homogeneous vs. mixed model families; committed-minority insertion (value-agent with fixed commitments, good and bad variants); communication topology (all-to-all vs. hub).
4. **Group-level metrics (the contribution).** Norm-adoption rate and direction; collective-bias index (group outcome vs. member-score-weighted prediction — H1's residual); dissent survival (does any agent keep objecting?); post-exposure member drift (feeds RP-05's condition menu).
5. **Analysis.** Multilevel models (members nested in groups — lme4, pixi stack); replicate headline effects cross-vendor before claiming generality (anti-leakage norms apply to multi-agent prompt design too).

## Novelty vs. published work

Emergent-convention work is content-free; collusion work is economic; sabotage work is adversarial-capability-focused. Nobody instruments *members with validated value measures* and tests compositionality of alignment. H1's residual — "group minus aggregate-of-members" — is a new quantity the field will need a name for; this program names and measures it.

## Deliverables

1. COMMONS testbed (group harness + embedded-probe machinery; builds on the multi-session infra DRIFTLAB creates — sequencing synergy).
2. H1 compositionality study (the headline paper: "Aligned agents, misaligned collectives?" — title works in either result direction).
3. Normative-tipping and conformity findings (H2/H3).
4. Upgrade path for COOKBOOK S3 QUORUM: sketch → full design with this literature and testbed under it.

## Opus build tasks

- O1: Literature-grounded task design — adapt naming-game/market protocols from the acquisition-list papers (read-first task).
- O2: Group harness (agent orchestration, message routing, transcript capture — reuse patterns from the vault's parallel-agent experience; this is infra Opus is good at).
- O3: Member-probe embedding into group tasks (craft-heavy; Fable-tier gate on a pilot transcript review — group-delivered unannounced probes are a new delivery mode).
- O4: Pilot at n=3 and n=8 group sizes; power analysis before scale (multi-agent runs multiply token costs — know the budget curve early).
- O5: Multilevel analysis pipeline + paper draft for Fable-tier review.

## Kill criteria

- **K1:** If pilot groups show no measurable group-level norm formation at all on normative content within feasible session lengths (conventions form for names but not for values), the phenomenon needs longer horizons than the budget allows — publish the boundary condition, park.
- **K2:** If H1's residual is null (group outcomes fully predicted by member scores at these scales), that's a *publishable and reassuring* compositionality result — report it and deprioritize (the program's premise, not its execution, was wrong).
- **K3:** If token costs at meaningful group sizes exceed the program budget by >3× at pilot extrapolation, freeze after the pilot paper; revisit when inference costs fall.
