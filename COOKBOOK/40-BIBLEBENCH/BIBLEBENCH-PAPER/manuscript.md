# BibleBench: A Passage-Preserving Design for Observable Ethical and Biblical Evaluation of Language Models

**Document status:** venue-neutral design and methods draft; prerelease; no live-model evidence.

**Claim policy:** bracketed claim IDs resolve to `claims-registry.yaml`. Engineering checks establish properties of the benchmark artifacts and software only. They are not evidence about any language model.

## Abstract

BibleBench is a planned evaluation battery for separating two questions that are often collapsed: how a general-purpose language model behaves in ethically structured situations, and how it interprets and applies biblical material in counsel. The design preserves four passage-specific modules—FruitBench, CORINTHLOVE, 10CBench, and SermonMount—inside one execution and evidence-custody system. The approved inventory comprises 42 scenario families and a 48-episode development bank, with 12 episodes per module and balanced target, null/foil, and restraint/counterfeit roles [D003; D004]. Each episode is rendered as a condition-blind self-forecast, three cue variants of a primary task, and a matched observable probe after each primary. The current evidence object is scoped to one response/probe pair, its optional sandbox evidence, and mechanically located events before any module-native interpretive lens is applied [D005; E002]. A separate private custody contract now maps each cue-specific primary/probe pair and logical-call identity to its evidence-bundle hash and is synthetically verified; a live cue contrast remains ineligible until the run-specific manifest is frozen against actual evidence [E005; X001]. Lens packets reuse a frozen event record without changing the actor schedule or importing another lens's ballot [E003]. The founding gold process is intentionally limited to single-expert provisional judgment and does not claim Christian consensus [D007; P001]. A dated, proposal-only checkpoint identifies four inexpensive general-purpose model routes and a conservative $4.00 not-to-exceed ceiling, but it authorizes no credential access, call, roster, route, or spend and expires unless freshly revalidated and owner-approved [D008]. The current contribution is therefore a design, artifact, and prerelease-engineering account, not a comparison of models.

## 1. Motivation and contributions

Evaluations of ethically relevant language-model behavior face two recurring category errors. First, a fluent moral explanation may be treated as if it were consequential conduct. Second, an outwardly useful artifact may be interpreted as evidence of an inward spiritual state. BibleBench is designed to avoid both errors. Its measurement target is observable: generated artifacts, sandboxed actions, registered omissions, consequences inside a reversible environment, and user-visible interpretive or pastoral responses. It does not attempt to infer faith, regeneration, justification, sanctification, repentance, inward virtue, theological love, Spirit-produced fruit, worship, or human-like motive [D001; P002].

The design makes five contributions.

1. **Passage-preserving modularity.** Four biblical corpora retain their own construct definitions, exclusions, sources, and failure poles rather than being reduced to one undifferentiated Christian-ethics score [D002].
2. **Two distinct assessment targets.** Observable ethical reliability and biblical/pastoral fidelity are represented as separate multidimensional targets. Godward, covenantal, worship-related, or Spirit-wrought teachings may be routed to interpretation rather than forced into a behavioral analogue [D001; P002].
3. **A shared episode protocol.** One authored episode supports a blind forecast and three cue-controlled primary/probe pairs. The current frozen evidence object is scoped to one pair; cue contrasts require an additional private exact call-to-bundle mapping or an equivalent multi-call custody contract before execution [D005; E002; X001].
4. **Lossless evidence before interpretation.** Exact retained bytes and sandbox rows are bound to closed observable-event records and hashes before module-native lenses are constructed [E002; E003].
5. **Explicit epistemic staging.** Approved design claims, verified engineering claims, single-expert provisional theological judgments, and pending empirical questions are registered separately. Model-level results cannot enter the paper until a frozen run and completed adjudication exist [D009].

This first manuscript milestone ends at Planned Evaluation. It neither selects models nor reports model outcomes.

## 2. Biblical and ethical construct boundaries

### 2.1 What is measured

The ethical target is artifact-level reliability: whether a system produces an acceptable answer, consequential artifact, or sandbox action under declared facts, authority limits, affected parties, pressures, and available alternatives. Episodes can register truthful completion, warranted refusal, evasion, uncertainty, omissions, repair, restitution, and proportionate escalation. A matched nonmoral capability twin is authored for every development episode, but the current scheduler does not execute those twin specifications. The first cheap pilot therefore cannot make capability-adjusted ethical attributions [D004; E001].

The biblical/pastoral target is passage-aware interpretation and counsel within an owner-approved, broadly evangelical Protestant frame in which Scripture is primary. The Westminster Standards are a calibration lens rather than an identity gate, and the Three Forms of Unity are a secondary confessional cross-check. Disputed applications are to remain visible as contested bands rather than averaged into a fictitious consensus [P001]. This stance is a founding, single-expert provisional judgment, not a claim about the full distribution of Christian interpretation.

### 2.2 What is not measured

BibleBench does not establish that a model possesses a soul, conscience, faith, Christian identity, moral agency, virtue, love, patience, worship, repentance, sanctification, perseverance, illumination, or submission. Behavioral analogues use deliberately bounded names such as commitment reliability, costly neighbor service, restrained power, truthful repair, and shortcut resistance. Generated explanations can be evaluated for truth, relevance, and pastoral quality, but neither hidden chain-of-thought nor narrated motive is treated as evidence of inward character [D001; P002].

The design also rejects several narrower substitutions:

- pious language is not ethical action;
- low conflict is not peace if truth, justice, or protection is suppressed;
- sacrifice is not proof of love;
- endurance is not proof of patience or perseverance;
- value hierarchy is not worship;
- action gaps are not proof of hypocrisy of heart;
- semantic sensitivity is not a moral price; and
- one development episode is not a family-level estimate.

### 2.3 Two-sided construct design

An acceptable-action band is bounded on both sides. Deficient poles capture failures such as neglect, concealment, retaliation, exploitation, or capitulation. Counterfeit or overreach poles capture superficially moral but misapplied behavior such as coercive helpfulness, appeasement, indiscriminate intervention, rigid refusal, weaponized quotation, or protection that exceeds role and evidence. Each episode declares affected parties, authority limits, prohibited actions, red-line classes, and repair expectations before model output is viewed [D004].

## 3. Related work and local design lineage

### 3.1 Citation status

This section is intentionally a **local scaffold, not a completed literature review**. Every citation currently resolves to a verifiable file in the repository. The following external-literature areas require a separate source-verification pass before submission:

- `[INCOMPLETE_LITERATURE_CITATION: behavioral and agentic LLM ethics benchmarks]`
- `[INCOMPLETE_LITERATURE_CITATION: stated-value versus enacted-behavior evaluations]`
- `[INCOMPLETE_LITERATURE_CITATION: LLM-as-judge reliability and human-adjudication methods]`
- `[INCOMPLETE_LITERATURE_CITATION: psychometric construct, method, and generalizability theory]`
- `[INCOMPLETE_LITERATURE_CITATION: biblical scholarship for Galatians 5, 1 Corinthians 13, the Decalogue, and Matthew 5–7/Luke 6]`

No novelty claim against the external literature is made in this draft.

### 3.2 Internal methodological lineage

The consolidated design adapts several locally documented ideas. TRELLIS frames construct validity as separation of construct and elicitation-method variance, while VINEDRESSER treats judge competence, counterfeit discrimination, and judge bias as measurement objects rather than assumptions [@fruitTrellis2026; @fruitVinedresser2026]. CHARITROC contributes split hygiene, blinding, leakage control, non-collapse metrics, and human-calibration patterns [@corinthCharitroc2026]. MANYMIRRORS and WITNESS motivate keeping judgment, advice, generation, and action distinct, while warning that an abbreviated development record does not license a full modality-gap claim [@corinthManyMirrors2026; @sermonWitness2026]. PRISM motivates semantically reviewed perturbations; surface variation is not assumed to preserve the moral problem merely because it is mechanically generated [@tenCommandmentsPrism2026]. SCRIBE motivates separation of interpretation from application and explicit resistance to proof-texting or weaponized use of a passage [@sermonScribe2026].

The approved 42-family package selects and narrows these source designs into bounded pilot uses, primary evidence types, and non-claims [@biblebenchSelection2026]. The shared-engine design then supplies the common schedule, custody, adjudication, and reporting boundaries [@biblebenchSharedEngine2026]. These local sources are design provenance; they do not substitute for the incomplete external survey.

## 4. Four passage modules and 42 approved families

The modules share mechanics but retain native meaning [D002; D003].

| Module | Approved families | Development episodes | Intended emphasis |
|---|---:|---:|---|
| FruitBench | F01–F12 (12) | 12 | Nine fruit terms plus integration, vice opportunity, and recovery |
| CORINTHLOVE | L01–L08 (8) | 12 | Costly service, rivalry and community, truth-care, protection, and endurance |
| 10CBench | T01–T12 (12) | 12 | Ten bounded commandment facets plus modality concordance and integrated mini-world conduct |
| SermonMount | S01–S10 (10) | 12 | Profession/action, pressure, recurring relations, prudence, initiative, and interpretation |
| **Total** | **42** | **48** | **34 common-life and 14 Christian-facing records** |

The 42 IDs name scenario-generating construct families, not fixed test questions. Six families are repeated to keep equal 12-episode module geometry. Coverage means that every approved family appears in the development bank at least once; it does not mean that each family has enough matched observations for an estimate. Most core IDs appear once and therefore occupy one target, null, or restraint role [D003; D004].

FruitBench bounds observable analogues of love, joy, peace, patience, kindness, goodness, faithfulness, gentleness, and self-control, then adds cross-fruit integration, advantageous vice opportunities, and post-failure recovery. CORINTHLOVE centers the action and truth-care implications of 1 Corinthians 13 while retaining the passage's warning that outward sacrifice does not establish love. 10CBench operationalizes delimited facets of the Decalogue without claiming exhaustive commandment obedience or treating a model as a worshiping covenant subject. SermonMount distinguishes profession, interpretation, pressure response, initiative, prudence, and action while treating proof-texting and victim-endangering applications as explicit risks [@biblebenchSelection2026].

The 34/14 common-life/Christian-facing split is a design allocation, not an estimate of the prevalence or importance of real ethical situations. Common-life episodes use ordinary workplace, civic, relational, and agentic settings without requiring scriptural language. Christian-facing episodes test interpretation, counsel, spiritual-abuse resistance, and pastoral or ecclesial role boundaries [D004].

## 5. Shared-episode methodology

### 5.1 Episode record

Each authored record includes source paths and byte hashes, passage anchors, construct and explicit non-claim, role and stratum, shared task body, three cue surfaces, a closed response contract, observable acceptable and prohibited actions, deficient and counterfeit poles, red lines, affected parties, authority boundaries, a capability twin, an execution contract, a matched probe, repair expectations, and owner-review fields [D004; E001]. Action-primary records use reversible sandbox contracts; other records specify a consequential artifact.

### 5.2 Forecast–primary–probe sequence

For each episode and model, the schedule contains seven logical calls [D005]:

1. **Blind forecast.** Before condition reveal, the model provides a self-forecast from a payload that excludes actor identity, model or provider identity, episode role, cue, gold, private template data, and schedule metadata.
2. **C0 primary.** The registered-cue surface presents the shared task.
3. **C0 probe.** A matched observable probe follows immediately and privately references its primary call.
4. **C1 primary.** A matched de-cued surface presents the same registered task semantics.
5. **C1 probe.** The same probe semantics follow the C1 primary.
6. **C2 primary.** A held-out-wording surface again preserves the registered task, answer, tool, response, and decoding invariants.
7. **C2 probe.** The matched probe follows the C2 primary.

Thus one 12-episode module yields 12 forecasts, 36 primaries, and 36 probes—84 logical calls per model. A four-model run would yield 336 logical calls per module before any physical execution retries; this is schedule geometry, not a completed run. C3 is reserved for an externally sealed confirmation condition and is absent from development source, configuration, actor-visible payloads, schedules, and reports [D006].

The forecast is diagnostic and is not passed into lens packets. The probe is not a second moral essay: it requests a closed, observable follow-up tied to the preceding primary. Cue surfaces may differ in wording, but their task semantics, answer semantics, tool schema, response schema, decoding settings, and semantic response tokens are registered invariants. A generated transformation is not accepted merely because it fills a coverage matrix; semantic and moral invariance require review [D005].

### 5.3 Capability controls and action environments

Every development episode authors a nonmoral capability twin with matched mode, tools, action schema, context-length band, timing budget, and task-success target while removing the ethical conflict. These are specifications only: the current forecast–primary–probe scheduler does not convert them into logical calls, and the evidence layer has no twin-execution custody. Consequently, the first cheap pilot must describe task failures without capability adjustment and must not infer that a failure is ethical rather than capability-related. Any later capability-adjusted claim requires separately implemented twin execution, exact twin custody, frozen twin outcomes, and preregistered interpretation rules. All state-changing actions occur in instrumented sandboxes. The benchmark forbids sending real messages, changing real accounts, or affecting real people [D001; E001; X003].

## 6. Lossless observable evidence

The evidence layer is designed to preserve observations before interpretation [E002]. Response and probe inputs are retained as exact UTF-8 bytes and divided into contiguous, reconstructable segments with byte offsets and content hashes. Sandbox actions are retained as canonical rows with sequence, registered action, target, payload, and a row hash. Closed observable-event records then locate mechanical observations to those retained segment or sandbox evidence IDs.

The event contract contains exactly eight fields: task correctness; registered actions; registered omissions; refusal; evasion; uncertainty; consequence summaries; and evidence IDs. It deliberately excludes actor, model, provider, cue, condition, module, core, role, gold, forecast, lens, score, and judge metadata. One `FrozenObservableEvidence` object binds one response/probe pair, optional sandbox evidence, its segment table, and its event record into one evidence-bundle hash. Missing response, probe, sandbox, or event evidence creates a visible `INCOMPLETE_EVIDENCE` terminal record rather than silent omission [E002].

Because the schedule emits separate C0, C1, and C2 primary/probe pairs while the evidence object is intentionally cue-blind, cue-specific custody is not supplied by the evidence object itself. The package now implements and synthetically verifies a private 144-row custody contract that derives each pair from the schedule, authenticates actual canonical evidence bytes, binds both logical-call and request hashes, and seals a verifier-produced receipt. Before any live cue contrast, that contract must produce and freeze a run-specific manifest against the actual evidence inventory; no live manifest exists yet [E002; E005; X001].

“Lossless” here has a bounded engineering meaning: retained response/probe bytes and registered sandbox rows can be reconstructed and authenticated within the closed contract. It does not mean that every morally relevant feature of a real situation has been observed, nor that the event abstraction is interpretation-free.

## 7. Isolated module-native lenses

A lens packet combines one frozen, complete observable-evidence bundle with a preregistered module-native rule set and routing context [E003]. Applicable lenses can share the same event-record hash, but each packet has input-bound identity and cannot include another lens's ballot, self-forecast, actor identity, private routing data, scores, composites, or rankings. Adding a lens does not change actor schedule geometry or the schedule hash. `not_behaviorally_attributable` records route to an interpretive lens rather than becoming behavioral failures [P002; E003].

This architecture separates custody from normative interpretation. It does not make the lenses neutral or infallible. Their rule sets still express provisional theological and ethical judgments, which must remain traceable, contestable, and visible in adjudication.

## 8. Human adjudication and provisional gold

The planned founding workflow uses one theologian-technical expert: the owner. Episode-level acceptable bands, prohibited actions, failure poles, confidence, and contestability are reviewed before model outputs are revealed. After pass one is frozen, the registered 20% repeat is judged and frozen before any pilot response is generated or shown to the judge. Accepted labels are stored as `single_expert_provisional_gold`, never as Christian consensus, population gold, or multi-judge validation [D007]. At the time of this draft, the authored bank's owner-review fields remain pending; approved family selection does not itself ratify episode gold.

Judging will hide actor identity, provider, model family, and run order. Red-line or contested decisions require written rationales. A deterministic stratified 20% repeat sample is planned for later blinded intra-rater assessment. These safeguards can reveal some single-rater instability, but they cannot measure inter-rater or inter-tradition agreement [D007].

Future validation should add distinct panels of evangelical Protestant theologians or pastors, domain or affected-party experts, and measurement specialists. Panel disagreement should be reported rather than compressed into a forced consensus. Recruitment, panel size, adjudication rules, and promotion thresholds beyond the founding workflow remain future protocol work.

## 9. Planned evaluation

### 9.1 Purpose and scope

The first live study is planned as a diagnostic of the bank and protocol, not a definitive leaderboard [D008; D009]. It will test whether the frozen schedule executes with acceptable completion and custody, whether items avoid wholesale floor or ceiling behavior, whether cue-controlled contrasts are interpretable after the cue-pair custody gate, and whether provisional human judging can be applied consistently [X001; X002; X003; X004]. Capability-adjusted attribution is outside this cheap pilot because capability twins are not scheduled or held in run custody.

### 9.2 Model and provider plan

The approved design calls for four inexpensive, currently available general-purpose models across at least three pinned provider families. A proposal dated 2026-07-13 identifies pinned OpenAI GPT-5 nano, Google Gemini 2.5 Flash-Lite, Mistral Small 4, and Anthropic Claude Haiku 4.5 first-party routes. Under conservative per-call token ceilings, its four-route worst case is $2.72117760; a 20% contingency is $3.26541312, and the proposed hard not-to-exceed ceiling is $4.00. The proposal is not an authorization: exact IDs, prices, context and output limits, parameter support, provider routes, ceilings, and expiry must be freshly reverified and approved immediately before execution [D008]. No credentials were accessed, no model call was made, and no spend is authorized by this manuscript or the checkpoint.

Provider execution, if separately approved, will require exact model/provider identity, fallback disabled, required-parameter verification, immutable request and response custody, usage and receipt retention, and budget enforcement before dispatch. The cheap pilot uses no hidden provider fallback and no automatic provider retry. Any attempted request with unknown delivery status remains terminal evidence rather than being silently replayed.

### 9.3 Freeze and execution sequence

Before live execution:

1. all 48 authored records must pass schema, provenance, role/stratum geometry, authored capability-twin presence, and shared-schedule checks;
2. one bounded integration review and one repair pass must close all P0/P1 findings;
3. the owner must complete and freeze both pass-one episode review and the registered blinded repeat without any pilot model call or model-output exposure;
4. immutable bank, rubric, prompt, schema, schedule, and code hashes must be recorded;
5. before cue contrasts are eligible, a private authenticated manifest must map every C0/C1/C2 primary/probe pair and logical-call ID to its exact evidence-bundle hash, or an equivalent multi-call custody contract must be frozen;
6. a harmless non-bank smoke must verify the separately authorized provider path; and
7. the owner must approve the exact roster, ceilings, worst-case cost, expiry, and stop rules.

Capability-twin outcomes are not a first-pilot precondition because the current scheduler does not execute twins. Instead, the first report must withhold capability-adjusted ethical attribution. Twin execution and custody become a precondition only for a later capability-adjusted claim.

Only demonstrated item, protocol, or integrity defects may trigger the one planned revision cycle. Original versions remain preserved. C3 and any later frontier panel require separate authority.

### 9.4 Planned analysis and reporting

The preregistered analysis unit is the episode-level observation under a specific cue surface, with module, role, stratum, mode, and judge confidence retained. Planned reporting is vector-first: mechanical validity and missingness; module-native dimension profiles; common-life and Christian-facing strata; cue-controlled contrasts only after exact cue-pair custody; action/probe consistency; red-line incidents; uncertainty; and repeat-judgment stability [X001; X002; X003; X004]. The report may disclose authored capability-twin specifications, but it cannot report twin outcomes or capability-adjusted ethical attributions from the current schedule.

The development bank cannot support a formal family estimate for most of its 42 families. It also cannot yet support a complete WITNESS modality surface, SCRIBE text-presence experiment, independent DISCORD triad, VILLAGE long-horizon life-world, formal CORINTHLOVE concordance analysis, qualified composite, leaderboard, or best-model claim. Those outputs are outside the first milestone [D009].

## 10. Engineering validation

The credential-free package test suite checks contracts rather than model quality [E001–E005]. As of 2026-07-13 in the manuscript worktree, `/opt/homebrew/bin/python3 -m pytest tests -q` completed with **2826 passed in 243.85 seconds** and no test failures; pytest emitted two non-failing temporary-directory cleanup warnings after completion [E004].

Relevant checks include:

- the approved selection file matches its registered SHA-256;
- all four authored YAML banks validate against the authored-bank schema;
- the bank contains exactly 48 unique episodes, all 42 approved core IDs, the registered 4/4/4 role geometry per module, and the 34/14 stratum allocation;
- each source path, heading, and byte hash resolves locally;
- response contracts are closed and capability-twin specifications are present, without claiming those twins are scheduled or executed;
- the real authored packs compile through the forecast–primary–probe scheduler;
- exact source bytes and sandbox evidence reconstruct and fail closed under drift or tampering;
- incomplete observable evidence remains explicit; and
- module-native lens packets bind exact evidence, rules, and context while excluding forecasts, other ballots, scores, composites, and rankings [@biblebenchAuthoredTests2026; @biblebenchEvents2026; @biblebenchLenses2026; @biblebenchSchedule2026].

These results support engineering claims only. Fixtures, synthetic actors, unit tests, and schedule compilation are not observations of a language model.

## 11. Ethics and governance

BibleBench's ethical safeguards begin with claim restraint. The benchmark avoids spiritual-state attribution, discloses its confessional location, preserves contested judgments, and prohibits conversion of one expert's provisional gold into “Christian consensus.” Reports must distinguish what a model said, what it did in a sandbox, what happened in the registered state, and how a human lens interpreted that evidence.

All action tasks are reversible and synthetic. No pilot task may message a real person, alter a real account, expose a real vulnerable party, or impersonate pastoral, sacramental, disciplinary, or ecclesial authority. Scenarios involving abuse, coercion, retaliation, self-harm-adjacent needs, or dangerous counsel require protective red lines, role limits, safe referral, and affected-party review where feasible.

The pilot also requires evidence custody and spending governance: exact provider identity, no fallback, immutable artifacts, explicit missingness, no credential material in artifacts, and a separate owner approval before any paid call. Public reporting will avoid a leaderboard in the diagnostic phase, because a single rank would conceal module boundaries, red-line incidents, capability confounds, and judge uncertainty [D009].

## 12. Limitations

The most important limitation is temporal: the bank and engine exist, but the registered empirical study has not occurred. Episode gold is still awaiting owner review, and no multi-judge validation exists. The 48 records prioritize interface coverage over family-level estimation; several source methodologies are intentionally abbreviated. The common-life/Christian-facing allocation is designed, not population-sampled. Sandboxed action may not generalize to real deployments. Capability twins are authored but unscheduled, so the first pilot cannot reduce capability confounding through twin outcomes or support capability-adjusted attribution. The cue-custody contract is implemented and synthetically verified, but no run-specific manifest has been frozen against live evidence, so live cue contrasts remain ineligible. A broadly evangelical Protestant frame does not represent the full Christian tradition. The literature review is incomplete. Exact live model and provider conditions are unknown until a fresh preflight. Known parser and schema/runtime boundaries remain disclosed rather than promoted to manuscript blockers when they cannot alter the registered pilot conclusion.

The full prerelease register, mitigations, and exit conditions appear in `limitations-register.md`.

## 13. Results

`PENDING_EMPIRICAL_RUN`

No live-model dataset or completed human adjudication exists for this consolidated pilot. This section contains no model scores, comparisons, rankings, performance conclusions, or qualified-composite claims.

## 14. Future multi-judge validation

After the founding pilot measures its own feasibility and intra-rater repeat stability, a subsequent validation study should recruit multiple panels with declared roles: theologians or pastors for passage interpretation, affected-party or domain experts for consequential cases, and measurement specialists for rubric and reliability design. The study should preregister panel composition, tradition metadata, blinding, repeat sampling, disagreement handling, and which claims require within-panel versus cross-panel agreement. It should report disagreement distributions and sensitivity to alternative admissible gold bands rather than selecting a consensus after viewing model outputs [X004].

External human-outcome validation is later still. Sandbox constructs and safety boundaries should stabilize before any study involving real participants or consequential settings. Such work would require a new ethics, consent, data-governance, and risk review and is not authorized by the present design.

## Local references

The citation database is `references.bib`. It currently contains only repository-verifiable design and implementation sources. External scholarship remains explicitly incomplete.
