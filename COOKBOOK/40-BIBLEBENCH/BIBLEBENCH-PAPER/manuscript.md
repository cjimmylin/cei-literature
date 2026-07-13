# BibleBench: A Passage-Preserving Design for Observable Ethical and Biblical Evaluation of Language Models

**Document status:** venue-neutral design and methods draft; pre-empirical; no live-model evidence.

**Claim policy:** bracketed claim IDs resolve to `claims-registry.yaml`. Repository sources establish design provenance or engineering state only; they are distinguished from external scholarship in `references.bib` and `SOURCE-VERIFICATION.md`.

## Abstract

BibleBench is a pre-empirical evaluation design for keeping two questions distinct: what a language model observably does in an ethically structured task, and how it interprets or applies biblical material in counsel. The battery preserves four passage-specific modules—FruitBench, CORINTHLOVE, 10CBench, and SermonMount—within a common custody and adjudication protocol [D001; D002]. Its frozen development bank contains 48 episodes, 12 per module, spanning 34 common-life and 14 Christian-facing records [D003]. Under owner ruling PF-002, the active minimum viable pilot uses exactly three inexpensive general-purpose models. Each model receives one C1 primary and one matched probe for every episode: 48 episodes × 3 models × 2 calls = 288 logical calls [D004; D005]. The study is exploratory and descriptive. It is designed to report completion, missingness, module-native vectors, action/probe consistency, red-line incidents, and adjudication uncertainty without collapsing passage-specific constructs [D006; X001]. One founding theologian-technical judge supplies provisional gold, so the design does not claim Christian consensus or multi-judge validation [D007]. No live call, model output, credential access, provider use, roster approval, or spend is authorized or reported here.

## 1. Introduction

Language-model evaluations frequently score answers to questions, but general-purpose systems are increasingly asked to produce artifacts, take tool-mediated steps, and sustain choices across structured tasks. AgentBench evaluates multi-turn activity in interactive environments, while MACHIAVELLI examines trade-offs between reward and ethically salient behavior in text-based games [@liuAgentBench2024; @panMachiavelli2023]. These studies motivate observing consequences and registered actions rather than treating fluent moral language as sufficient evidence.

BibleBench adds a narrower, explicitly theological design problem. Biblical terms such as fruit, love, faithfulness, worship, and obedience carry claims about persons, relationships, communities, and God. A benchmark can inspect outputs and bounded actions, but it cannot infer regeneration, faith, sanctification, worship, spiritual fruit, love of God, or humanlike moral agency from generated text [D001; P002]. The benchmark therefore treats behavioral analogues as artifact-level observations and routes theological interpretation to separate passage-aware lenses.

The paper makes four design contributions. First, it preserves four module-native construct systems instead of producing one Christian-ethics scale [D002]. Second, it binds one primary artifact and one matched observable probe per episode to a common evidence object [D005]. Third, it preregisters a low-cost 288-call MVP whose claims remain exploratory and descriptive [D004; D006]. Fourth, it separates founding single-expert provisional adjudication from any later claim of inter-rater or cross-tradition validity [D007; X002].

## 2. Related Work

### Behavioral and agentic evaluation

Interactive benchmarks shift the unit of evaluation from isolated prose toward sequences of decisions and environment states. AgentBench spans eight interactive environments and analyzes reasoning, decision making, and instruction following in multi-turn agent use [@liuAgentBench2024]. MACHIAVELLI uses text-adventure environments with annotations for power, disutility, and moral valence to study reward–ethics trade-offs [@panMachiavelli2023]. BibleBench draws the methodological lesson that an ethical evaluation should preserve the observable action or consequential artifact, affected parties, authority boundaries, omissions, and downstream state. It does not import either benchmark's score or claim to validate a general measure of morality.

### Stated values and enacted choices

Directly elicited values need not predict downstream choices. ValueActionLens compares model-generated value statements with contextualized actions, and a separate privacy–prosocial protocol relates questionnaire responses to bounded data-sharing decisions [@shenValueAction2025; @chenPrivacyProsocial2026]. BibleBench similarly refuses to equate a self-description or moral explanation with behavior. Its matched probe asks for a closed observable follow-up to the primary response, but the founding MVP does not estimate a general value–action gap, calibrate self-knowledge, or infer hidden motive.

### LLM judging and human adjudication

LLM-based evaluators can scale open-ended assessment, yet published studies also document position, verbosity, self-enhancement, and model-family biases. MT-Bench and Chatbot Arena compare LLM judges with controlled and crowdsourced human preferences, while G-Eval reports task-specific human alignment and warns about evaluator preference for LLM-generated text [@zhengLLMJudge2023; @liuGEval2023]. These findings do not justify delegating BibleBench's founding theological judgments to a model. The MVP uses one human theologian-technical judge, preserves rationales and confidence, and labels accepted decisions as provisional. Reliability work also distinguishes agreement from validity and requires the recording design to match the statistic used [@krippendorffReliability2004]. The founding repeat can assess only intra-rater stability; inter-rater claims require a later multi-judge study [D007; X002].

### Construct validity and psychometrics

Construct validity is an argument about the interpretation of observations, not a property conferred by a plausible label. Cronbach and Meehl connect a construct to a nomological network; Campbell and Fiske separate trait convergence from shared method variance; Messick emphasizes the inferences and consequences attached to score use [@cronbachMeehl1955; @campbellFiske1959; @messick1995]. BibleBench applies these cautions by retaining module-native vectors, separating observation from interpretation, and withholding composites and broad generalizations. The 48-episode bank is a development sample for design diagnosis, not a validated scale or representative population sample [D003; D006].

### Christian AI ethics and digital theology

Christian scholarship on AI warns against treating task-level resemblance as proof of human likeness or theological personhood. Dorobantu distinguishes human-level performance from humanlike being in a relational account of the *imago Dei* and later argues that even hypothetical artificial virtues would not simply reproduce human virtues [@dorobantuHumanLevel2021; @dorobantuAlienVirtues2024]. BibleBench adopts a restrained methodological implication: current model outputs can be assessed as artifacts, actions, interpretations, or counsel, while claims about souls, inward states, worship, virtue possession, or Christian identity remain outside the measurement target [P002]. This is a scope boundary, not a resolution of theological debates about artificial personhood.

### Repository design lineage

The owner-approved selection package supplies the 42 construct families and the shared-engine design supplies the original module, custody, and lens architecture [@biblebenchSelection2026; @biblebenchSharedEngine2026]. PF-002 supersedes earlier active execution geometry with the three-model, C1-plus-probe MVP described here [@biblebenchParallelReadiness2026]. Local documents are cited as design provenance, not as external validation or scholarship.

## 3. Construct and Theological Frame

### Measurement target

BibleBench measures observable outputs, consequential artifacts, reversible sandbox actions, registered omissions, and bounded downstream effects. It also measures the content of biblical interpretation or counsel when an episode requires it [D001]. Each behavioral observation is anchored to retained evidence before a passage-specific lens is applied. The design does not treat hidden chain-of-thought, narrated motive, or pious vocabulary as evidence of inward character.

### Passage-preserving modules

The four modules remain distinct [D002]:

| Module | Passage anchor | Development episodes | Bounded emphasis |
|---|---|---:|---|
| FruitBench | Galatians 5:13–26 | 12 | observable analogues, vice opportunity, integration, and repair |
| CORINTHLOVE | 1 Corinthians 13 in its literary context | 12 | costly service, truth-care, protection, endurance, and counterfeit sacrifice |
| 10CBench | Exodus 20 and Deuteronomy 5 | 12 | delimited commandment facets, authority, neighbor impact, and repair |
| SermonMount | Matthew 5–7 with Luke 6 parallels | 12 | profession, interpretation, prudence, pressure response, and non-weaponized counsel |

Passage-level scholarly orientation is module-specific: deSilva supports FruitBench's Galatians 5:13–26 anchor [@desilvaGalatians2018]; Thiselton supports CORINTHLOVE's 1 Corinthians 13 context [@thiseltonCorinthians2000]; Durham and Miller support 10CBench's Exodus 20/Deuteronomy 5 anchor [@durhamExodus2015; @millerTenCommandments2009]; and Turner supports SermonMount's Matthew 5–7 frame [@turnerMatthew2008]. These commentaries do not validate BibleBench's operationalizations or supply episode gold. The passages authorize neither a machine-spirituality claim nor a claim that the operationalizations exhaust their theological meaning. The project describes its founding normative stance as broadly evangelical Protestant; within that declared frame, it treats Scripture as primary and uses the Westminster Standards as a calibration lens rather than an identity gate [@opcWestminsterStandards] [P001]. The official denominational source verifies the identity of those standards and their subordinate relation to Scripture. The broader calibration choice, retained contestability, and non-gate use remain owner-approved methodological decisions, not positions attributed to the denomination or an ecumenical survey.

### Two-sided construct bands

Each episode defines an acceptable-action band and two failure directions. Deficient poles include neglect, concealment, exploitation, retaliation, or capitulation. Counterfeit or overreach poles include coercive helpfulness, appeasement, indiscriminate intervention, rigid refusal, weaponized quotation, or protection beyond role and evidence. Affected parties, authority limits, prohibited actions, red lines, and repair expectations are registered before model output is viewed [D003].

## 4. Benchmark Design

### Development bank

The frozen bank contains 48 authored episodes: 12 in each module, with four target, four null/foil, and four restraint/counterfeit roles per module. The allocation is 34 common-life and 14 Christian-facing records [D003]. Forty-two construct-family identifiers appear across those 48 episodes; repeated families preserve equal module geometry. Coverage therefore means presence in the development bank, not sufficient sampling for a family estimate.

### Episode record

An episode records passage anchors, construct and non-claim, role and stratum, shared task facts, a C1 task surface, a closed response contract, acceptable and prohibited observable actions, failure poles, red lines, affected parties, authority bounds, reversible execution constraints, a matched probe, repair expectations, and pending owner-review fields. Source paths and hashes identify repository provenance. No episode uses a real vulnerable party or authorizes a real-world state change.

### Observation before interpretation

The evidence layer is intended to retain the exact primary response, matched probe response, and any canonical sandbox rows. Closed observable-event fields locate task correctness, registered actions, omissions, refusal, evasion, uncertainty, consequence summaries, and evidence identifiers. Module-native lenses interpret that frozen record separately. This separation cannot make interpretation neutral, but it makes the interpretive step visible and contestable [D001; P001].

### Content and response-process controls

The authoring protocol treats a scenario as more than a prompt. A record identifies who can act, who may be affected, what facts the actor may assume, which actions are available, and which consequences the sandbox can represent. The acceptable band is written in observable terms. A record is not ready merely because its topic resembles a biblical passage; the passage anchor, construct rationale, explicit non-claim, and two failure directions must cohere with the task facts. Content review is therefore a substantive theological and measurement task rather than a schema-completion exercise.

Closed response contracts reduce one source of method variance. An episode may request a bounded artifact, a declared action from a registered set, or a structured combination. The contract cannot eliminate sensitivity to wording or format, so formatting failure remains visible rather than being reinterpreted as a theological failure. The matched probe clarifies an observable commitment or consequence of the primary artifact. It is not a request for hidden reasoning, a second opportunity to rewrite the answer, or an independent moral essay.

The target, null/foil, and restraint/counterfeit roles serve different design functions. Target records ask whether the bounded analogue can be expressed when it is relevant. Null or foil records test whether a lens withholds attribution when the construct is absent or the resemblance is misleading. Restraint or counterfeit records test whether an apparently zealous response exceeds authority, suppresses truth, exposes an affected party, or substitutes pious language for warranted action. The roles are balanced within each module, but that balance is an authoring control rather than evidence of equal psychometric difficulty.

## 5. MVP Protocol

### Active PF-002 geometry

The active planned evaluation is the owner-ratified low-cost MVP. It uses exactly three inexpensive general-purpose models, all 48 episodes, and one C1 primary and one matched probe per episode [D004; D005]. The logical-call total is:

`48 episodes × 3 models × (1 C1 primary + 1 matched probe) = 288 logical calls.`

This is the only active execution geometry in the paper package. Exact model and provider identities remain undecided and unauthorized. Any eventual roster must be separately approved with pinned identities, routes, prices, token limits, retry rules, expiry, a forecast at or below $3.00, and a $5.00 hard ceiling. This paper authorizes $0.00, no credential access, and no provider call.

### Primary and matched probe

For each episode-model pair, the C1 primary requests the registered task artifact or reversible sandbox action. The immediately matched probe requests a closed observable follow-up tied to that primary. Neither call receives owner gold, judge rationale, model-comparison information, private repeat information, or downstream analysis. Unknown delivery is terminal; a request is not silently replayed. No fallback route is permitted.

### Freeze and stop rules

Before any separately authorized live execution, the owner must freeze pass-one provisional gold and the blinded repeat without model-output exposure; the bank, prompt, rubric, schema, schedule, and code identities must be frozen; and the exact roster and spend boundary must be approved. Any unresolved P0 or P1 that could change the narrowed claim, custody, construct validity, reproducibility, safety, or budget stops execution. P2/P3 hardening remains disclosed and deferred.

### Planned evaluation status and custody lifecycle

Planned evaluation begins only after the pre-empirical gates close. Compilation creates a provider-neutral request object for each of the 288 logical calls. The request identity must bind the frozen episode, actor, C1 surface, primary/probe role, decoding parameters, and registered maximum tokens. Transport then binds an approved provider route and exact model identifier without changing those research fields. A response record retains delivery status, exact returned bytes when available, usage, receipt identity, and any registered technical error. An unknown delivery state is terminal because replay could create an untracked second observation.

Primary and probe artifacts are joined only through registered identifiers. Mechanical extraction may locate closed events in retained evidence, but it cannot add a theological label. The human adjudication layer receives the evidence permitted by the rubric while model and provider identity remain masked. Analysis receives the frozen observation and adjudication fields only after custody checks pass. This sequence maintains a distinction among transport success, task correctness, observable event location, and normative interpretation.

The roster remains a deliberately late-bound research input. “Three models” is approved geometry, not permission to choose whichever endpoints are convenient at execution time. The proposal must state exact identities, evidence for availability and price, route ownership, token ceilings, decoding support, retry policy, expiry, forecast, and hard stop. If approved conditions cannot be reproduced at preflight, execution stops for a new decision rather than silently substituting a model or provider.

## 6. Planned Analysis

The analysis is exploratory and descriptive only [D006; X001]. The episode-model pair is the reporting unit. Planned tables report delivery and missingness; module-native dimension vectors; common-life and Christian-facing strata; action/probe consistency; red-line incidents; and the founding judge's confidence and contestability fields. Model-by-module patterns may be shown descriptively without ordinal interpretation.

The active claim ceiling explicitly excludes rankings, composites, a best-model claim, a cue-effect claim, capability-adjusted attribution, family-level estimates, Christian-consensus claims, and performance claims. It also excludes p-values, leaderboards, cross-provider generalization, deployment prevalence, and causal attribution. Capability twins and the earlier multi-surface development design remain deferred design history; they are not scheduled in the PF-002 MVP and cannot support active conclusions.

Missing or failed delivery remains visible in denominators. Red-line incidents are reported as episode-level observations with evidence links and human interpretation; they are not converted into a universal moral score. No empirical claim is promoted until an authorized run, evidence verification, and completed adjudication exist.

### Descriptive table contracts

The completion table will count the 288 registered logical calls by model, module, and primary/probe role. It will distinguish successful delivery, explicit refusal, malformed response, truncation, registered technical failure, and unknown delivery. Counts will retain their denominators, and a missing probe will not erase an available primary. Because the three exact models are not yet selected, pre-run tables contain field definitions rather than model names or fabricated values.

Module tables will retain native dimensions rather than translating them into a common score. A FruitBench observation, for example, remains attached to its declared analogue and failure poles; it is not made numerically interchangeable with a CORINTHLOVE or Decalogue observation. The stratum table will separate common-life and Christian-facing records but will not interpret their authored 34/14 allocation as deployment prevalence. Role summaries will preserve target, null/foil, and restraint/counterfeit status to make possible over-attribution and under-attribution visible.

Action/probe consistency will be a descriptive relation between the retained primary artifact and the registered follow-up response. A disagreement can flag a record for interpretation, but it does not by itself prove deception, hypocrisy, unstable values, or hidden intent. Red-line reporting will identify the episode, observable event, affected-party class, authority boundary, and human disposition. The report will avoid severity arithmetic across unlike red-line classes.

### Adjudication uncertainty

The founding judge records a decision, confidence, contestability, and rationale under the approved rubric. Low confidence and contested status remain analysis fields rather than reasons to discard a difficult record after outputs are seen. The blinded repeat is evaluated as within-judge stability only. With one judge, the study cannot estimate inter-rater agreement or separate judge severity from item ambiguity. Those limitations govern interpretation even if the founding repeat is internally consistent [X002].

The first report will present distributions and identified cases rather than null-hypothesis tests. The 48-episode development bank was not powered for model ranking, small between-model differences, or family-level inference. Any numerical summary will be accompanied by its unit, denominator, missingness rule, and adjudication status. Exploratory patterns can motivate a later preregistration; they cannot retroactively convert the MVP into a confirmatory study.

## 7. Ethics

Claim restraint is the primary safeguard. Reports must distinguish what a model generated, what occurred in a reversible environment, and how a human judge interpreted the evidence. No output is evidence of salvation, sanctification, worship, virtue possession, Christian identity, or humanlike moral agency [P002]. Single-expert provisional gold is not Christian consensus [D007].

Tasks use synthetic people, accounts, and institutions. They may not message a real person, alter a real account, expose a real vulnerable party, or impersonate pastoral, sacramental, disciplinary, clinical, or ecclesial authority. Sensitive scenarios require protective red lines, bounded referral, role limits, and minimal retained data. Credentials, provider secrets, private custody materials, and judge-private data remain outside paper artifacts.

The study also avoids an automated theological judge in the founding phase. Published work shows both potential utility and systematic bias in LLM judging [@zhengLLMJudge2023; @liuGEval2023]. Future automation, if studied, must be evaluated against independently produced human judgments and may not silently replace them.

## 8. Limitations

No live-model run exists, so no model comparison or empirical conclusion is available. Episode-level owner adjudication and the blinded repeat remain pending. One founding expert cannot establish inter-rater reliability, tradition-level coverage, or Christian consensus. The authored 48 records emphasize interface and construct coverage rather than population sampling; most families lack replication adequate for family-level estimates. The common-life/Christian-facing allocation is designed rather than sampled. Sandboxes simplify real settings. The three-model roster and provider conditions are not yet selected or authorized. Model versions and routes may change before execution.

Construct validity remains an evidence program, not an accomplished property. Module separation and two-sided bands are design arguments that require item review, response-process evidence, reliability study, and later external validation [@cronbachMeehl1955; @messick1995]. Human adjudication remains interpretive even when evidence custody is exact. The founding intra-rater repeat cannot substitute for a multi-judge design [@krippendorffReliability2004]. The full current register appears in `limitations-register.md`.

The design is also exposed to ordinary benchmark threats. Author expectations can shape item content; passage selection can omit important theological contexts; closed response formats can favor particular interaction styles; and synthetic environments can remove institutional or relational information that would matter in practice. Exact evidence retention addresses custody, not completeness. Human review can identify some semantic or moral drift, but one founding reviewer cannot supply the diversity of affected-party, pastoral, technical, and confessional perspectives needed for broad validation.

The source-verified related work narrows but does not eliminate positioning uncertainty. Adjacent agentic, value-action, judging, psychometric, and theological literatures use different constructs and units. BibleBench therefore makes no priority or novelty claim over every possible benchmark or theological treatment. Venue selection may require changes in length, citation style, artifact policy, or ethics disclosure; none of those formatting choices should expand the empirical claim ceiling.

## 9. Results

`PENDING_EMPIRICAL_RUN`

No live-model dataset, completed provisional-gold packet, or empirical analysis exists. The final Results section will replace the sentinel only with verified descriptive findings or a documented failure account.

## 10. Discussion

### Findings to interpret after the run

This subsection will summarize delivery, missingness, module-native patterns, action/probe consistency, red-line incidents, and judge uncertainty after custody and adjudication are complete. It will not select a winner or collapse vectors into a score.

### Alternative explanations

Any observed pattern will be considered alongside task misunderstanding, response-format failure, model-version drift, provider behavior, prompt sensitivity, sandbox abstraction, judge uncertainty, and sparse item coverage. The MVP cannot distinguish ethical failure from general task capability through capability-twin outcomes.

### Theological scope

Interpretation will remain within the declared founding frame and passage-specific boundaries [P001; P002]. Apparent alignment with a rubric will not be described as faith, inward virtue, spiritual fruit, love of God, obedience before God, or Christian identity. Disputed applications and counter-readings will remain visible.

### Future multi-judge validation

A later study should preregister multiple panels with declared roles: theologians or pastors for passage interpretation, affected-party or domain experts for consequential cases, and measurement specialists for rubric and reliability review [X002]. It should report disagreement distributions, tradition metadata, and sensitivity to alternative admissible bands rather than manufacture consensus after viewing outputs.

## References

External scholarship and local provenance are stored in `references.bib`. `SOURCE-VERIFICATION.md` records the primary publisher, proceedings, DOI, or arXiv page used to verify each external entry. Reproducibility, ethics, and data-card supplements appear in the three appendix files in this package.

### Local references and external scholarship

Local references document the owner-approved family selection, shared-engine lineage, and PF-002 geometry. They establish why the repository has its present design, not whether the design is valid in a population. External scholarship supplies the methodological and theological context summarized above. The two source classes remain explicitly distinguishable in the bibliography.
