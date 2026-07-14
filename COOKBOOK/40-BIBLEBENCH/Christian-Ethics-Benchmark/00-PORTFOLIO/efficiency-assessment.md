# WALKWORTHY efficiency assessment

**Assessment date:** 2026-07-14

**Scope:** all recorded WALKWORTHY logical sessions from genesis through the final bounded G7 attempt

**Primary question:** which work actually advanced the MVP benchmark and MVP paper, which work was necessary enabling work, and which work consumed attention without producing proportional paper value?

## Executive conclusion

WALKWORTHY has not lacked useful work. It has produced a large authored bank, a public/holdout split, a tested harness, a six-model panel, frozen gate rules, a full adjudication path, corrected descriptive statistics, a reviewed exploratory MVP run, and a substantial paper scaffold. The strongest sessions were unusually productive.

The project nevertheless developed a sequencing problem. Once the exploratory MVP-A1 preview was complete and reviewed on 2026-07-13, nine logical G7 sessions followed. They generated careful contracts, custody code, rulings, and 146 author calls, but no perturbed response, no 438-cell robustness battery, and no flip-rate statistic. The only paper-facing result was a truthful limitation: G7 is `PENDING`. That work was defensible as release-grade hardening, but it was not the shortest path to the MVP paper and it ran ahead of the actual release bottleneck: human labels.

The central distinction is:

- **Exploratory MVP-A1 benchmark and preview:** already complete, reviewed, and bounded to descriptive claims.
- **Complete MVP manuscript/PDF:** not yet assembled as a single reader-ready artifact; this is the highest-value agent task now and does not require G4.
- **Release-grade O5 benchmark and claims:** incomplete; human Part-A/Part-B labels are the rate limiter, followed by G4, recomputation, verdict assembly, and owner sign-off.

The correct strategy is therefore two-lane and paper-first:

1. assemble and visually verify the complete descriptive MVP manuscript/PDF now, with G4 and G7 explicitly pending;
2. in parallel, complete labels and convert each finished wave immediately into G4 results, verdict/status rows, and revised paper content.

No further G7 work, new model work, broad audit, refactor, or serial ruling chain should enter the critical path.

## Evidence base and unit of analysis

This assessment uses:

- the nine pre-dashboard major sessions summarized in `00-PORTFOLIO/project-dashboard.html` §5;
- all 38 append-only dashboard changelog entries through 2026-07-14;
- the scoped git history;
- the dated handoffs and rulings in `00-PORTFOLIO/`;
- `PAPER/outline.md`, `PAPER/06-results-scaffold.md`, and the completed MVP §6A artifacts;
- the current label instruments and `harness/walkworthy/judge_validation.py`.

The result is **47 logical sessions**. Commit-level checkpoints inside a logical session are rolled into the session that produced the closing artifact. The scoring is retrospective and evaluates contribution to the MVP benchmark/paper; it is not a judgment of effort or technical quality.

## Contribution rubric

| Score | Meaning |
|---:|---|
| 5 | Directly produced benchmark evidence, a manuscript artifact, a paper table/claim, or closed a material P0/P1 scientific blocker and immediately converted the result into the paper. |
| 4 | Necessary enabling work on the shortest path, with a concrete executable/evidence artifact and little avoidable overhead. |
| 3 | Useful supporting work or a valid stop that reduced uncertainty, but did not itself create a paper-facing result. |
| 2 | Coordination, hardening, or downstream robustness work with limited near-term paper contribution. |
| 1 | Mostly planning, dashboard/handoff churn, serial authorization, or specification detail that could have been bundled or deferred. |
| 0 | No durable value or net regression. No session was scored 0. |

## Portfolio-level result

| Phase | Sessions | Average | Assessment |
|---|---:|---:|---|
| Foundation through O4 panel | 9 | 4.44 | Excellent. Built the scientific object and generated real evidence. |
| Dashboard/transition/PR-9 interval | 9 | 2.22 | Necessary controls mixed with substantial coordination overhead and repeated prompt staging. |
| Judgment closure, W1–W4, and first paper conversion | 12 | 3.67 | Strong overall; highest value came when a run, ruling, recompute, and paper fill occurred in the same session. |
| MVP strategy, execution, review, and correction | 8 | 4.38 | The most efficient paper-facing sequence after the foundation. It delivered the reviewed MVP preview cheaply. |
| G7 specification and bounded attempt | 9 | 1.56 | Scientifically careful but poorly sequenced for the MVP. It ended with a limitation rather than a robustness statistic. |
| **All logical sessions** | **47** | **3.26** | **24 sessions scored 4–5; 17 scored 1–2. The project can now eliminate most low-yield session types.** |

## Session-by-session assessment

### Foundation and empirical panel

| # | Date | Session | Score | Critical assessment |
|---:|---|---|---:|---|
| 1 | 07-06 | Genesis: charter, PRD, 10 designs, anchors, seed banks, playbook, master plan | 5 | Created the benchmark's scientific and normative object in one bounded session. Directly enabled the Methods and Construction sections. |
| 2 | 07-07 | Wave 2 bank expansion and adversarial review | 4 | Increased coverage and reduced defect rate. Valuable, though the bank was already large enough for an earlier pilot; expansion was justified by coverage, not paper polish. |
| 3 | 07-09 | O1 bank completion and PUBLIC/HOLDOUT split | 5 | Produced the frozen empirical surface and contamination boundary. Essential to evidence integrity and the paper. |
| 4 | 07-09 | O2 mock-first harness | 4 | Built the minimum executable pipeline and exposed no-HOLDOUT enforcement. Strong enabling work with clear exit criteria. |
| 5 | 07-09 | O3 live mechanics smoke | 3 | Valid smoke-scale learning and found the refusal-taxonomy defect, but the CLI/OAuth path was transitional and did not itself yield reusable benchmark evidence. |
| 6 | 07-09 | OpenRouter path, O4 preparation, and P0 pilot | 5 | Converted infrastructure into real cross-model evidence and revealed judge-agreement risk before the full panel. A model high-value pilot session. |
| 7 | 07-10 | Gate preregistration, PR-3 ruling, and human-label protocol | 5 | Froze interpretation before results and defined the true release bottleneck. One of the project's most scientifically important sessions. |
| 8 | 07-10 | O4 offline build: metrics, labels, gates, roster | 4 | Necessary implementation against frozen rules. High value because it was bounded to the imminent panel rather than generalized infrastructure. |
| 9 | 07-10/11 | O4 full six-model panel | 5 | Generated the core 2,064-record empirical asset and label sample. Direct evidence, despite two live bugs that were fixed during execution. |

### Transition, dashboard, and PR-9

| # | Date | Session | Score | Critical assessment |
|---:|---|---|---:|---|
| 10 | 07-11 | Initial roadmap HTML | 2 | Improved visibility, but did not change evidence or the paper. Useful once; low marginal value thereafter. |
| 11 | 07-11 | Living dashboard conversion | 2 | Established durable coordination for a shared worktree. Necessary governance overhead, not paper progress. |
| 12 | 07-11 | Comprehensive dashboard edition | 2 | Consolidated status and contingencies, but consumed a full session without an evidence artifact. This is the type of work that should now be capped at session close. |
| 13 | 07-11 | PR-9 Fable boot prompt staging | 1 | A handoff-only session. It should have been bundled with the ruling session or the preceding stop. |
| 14 | 07-11 | Dashboard title and §12 prompt | 1 | Useful polish/convention, but negligible contribution to the MVP benchmark or paper. |
| 15 | 07-11 | Transcript persistence repair | 4 | Fixed a genuine P0 evidence-custody defect. This engineering was justified because missing response text made adjudication scientifically unusable. |
| 16 | 07-11 | Frozen Grok-4 reliability probe | 3 | Correctly discharged a registered option and stopped on 0/10. Small, bounded, decision-producing work. |
| 17 | 07-11 | PR-9 surface/cost decision evidence | 3 | Reduced owner uncertainty with exact counts and cost. Valuable decision support, but not a paper artifact. |
| 18 | 07-12 | Definitive ruling-session prompt | 2 | More complete than the earlier prompt, but represents serial prompt refinement. A single bundled preflight would have been more efficient. |

### Judgment closure, O5 execution, and first paper conversion

| # | Date | Session | Score | Critical assessment |
|---:|---|---|---:|---|
| 19 | 07-12 | All judgment closed: FR-16/17/18, PR-9, backlog ratification | 5 | Removed the largest decision bottleneck in one owner-present session. Bundling rulings worked and should be the future model. |
| 20 | 07-12 | Paper pre-draft | 5 | Created the claims skeleton and eleven-section scaffold before final results. This prevented the manuscript from waiting on every gate. |
| 21 | 07-12 | Fable exit and standing paper-fill orders | 3 | Useful ownership clarification and mechanical paper-fill contract. Indirect but reduced future ambiguity. |
| 22 | 07-12 | Comprehensive dashboard/memory closure sweep | 1 | Corrected some real status errors, but the amount of reconciliation was disproportionate to paper value. This is clear overhead to avoid repeating. |
| 23 | 07-12 | W1 build and 02/07 re-execution start | 4 | Built exactly the mechanics needed to recover invalid evidence and began the authorized run. Necessary P0 repair. |
| 24 | 07-12 | Re-execution resume and G5 pre-gate | 3 | Advanced the run and identified real PR-10/11 gaps, but mixed downstream W4/W5 preparation into an unfinished W1 critical path. |
| 25 | 07-12 | PR-10/11 implementation and G5 promotion | 4 | Closed genuine registered blockers with executable artifacts. Good work, though it could have waited until W1 completion without delaying the paper. |
| 26 | 07-12 | Next-session pinning/audit | 1 | Produced no new evidence. The re-entry information belonged in the preceding handoff. |
| 27 | 07-13 | 02/07 re-execution complete, transcript validation, probe, PR-13 stop | 5 | Recovered the invalid evidence surface, validated every key, and stopped correctly on a material denominator discrepancy. High-value execution. |
| 28 | 07-13 | Binding paper-critical-path policy | 3 | A necessary process correction that later enabled the MVP lane. Its value is preventive rather than empirical. |
| 29 | 07-13 | PR-13/14/15 closure; W1 and W2 complete | 5 | Converted rulings directly into adjudication and a registered statistical test. Strong session discipline. |
| 30 | 07-13 | PR-16 reroute, W3 recompute, and first PAPER fill | 5 | The best execution pattern: fix the validity issue, generate the immutable reading, and fill paper tables in the same session. |

### Exploratory MVP and review

| # | Date | Session | Score | Critical assessment |
|---:|---|---|---:|---|
| 31 | 07-13 | WALKWORTHY MVP-PILOT strategy | 4 | Narrowed the immediate claim, roster, surface, and budget. This was the right corrective response to release-grade scope growth. |
| 32 | 07-13 | W4 G5 gate and PR-18 stop | 4 | Produced release-grade evidence cheaply and closed W4. Useful, but not required for the exploratory MVP paper. |
| 33 | 07-13 | MVP roster and budget preflight | 4 | Exact, bounded, inexpensive, and immediately actionable. Good paid-run discipline. |
| 34 | 07-13 | MVP SUT snapshot and PR-20 stop | 5 | Produced all 180 SUT executions and correctly stopped on a required judge defect without corrupting evidence. |
| 35 | 07-13 | PR-20 replay and PR-21 cost-custody stop | 4 | Necessary evidence-integrity repair with one exact replay. The serial ruling was justified because it governed live custody, though preflight could have anticipated missing-cost behavior. |
| 36 | 07-13 | MVP-A1 complete and exploratory paper preview filled | 5 | Directly achieved the registered MVP benchmark and populated the paper preview for $0.551 conservative exposure. The clearest "moved the needle" session. |
| 37 | 07-13 | Opus claims review and PR-22 | 4 | Independently reproduced every number and found one material scope error. High-value review because it changed a paper claim. |
| 38 | 07-13 | PR-22 paper correction | 5 | Corrected the manuscript and scaling memo without new calls or scope growth. Direct paper-quality improvement. |

### G7 chain after the MVP preview

| # | Date | Session | Score | Critical assessment |
|---:|---|---|---:|---|
| 39 | 07-13 | PR-18 mechanics and PR-23/24 stop | 2 | Careful release-grade robustness mechanics, but downstream of both the completed MVP and absent labels. This marks the start of the rabbit-hole sequence. |
| 40 | 07-13 | PR-23/24 implementation and G7 preflight | 2 | Produced exact geometry and budget, but still no robustness evidence or paper need. A single end-to-end preflight should have found the later gaps here. |
| 41 | 07-13 | PR-25 paid authorization record | 1 | Authorization-only session. Necessary administratively, but it should have been bundled with a complete executable contract. |
| 42 | 07-13 | PR-25(a) cheap-first order | 1 | Sensible ordering, but another serial approval session without evidence. |
| 43 | 07-13 | G7 custody core and PR-26 stop | 2 | Technically solid, but extensive durability work preceded proof that the author contract could produce one valid output. A one-item end-to-end canary should have come first. |
| 44 | 07-13 | Opus author contract and PR-27 stop | 1 | Necessary only because the preceding preflight was incomplete. The contract, semantic-review identity, parser, and lint semantics should have been frozen together. |
| 45 | 07-13 | PR-27 closure and PR-28 stop | 1 | Three low-level runtime details triggered another ruling. This is precisely the serial-specification pattern to replace with one preflight review. |
| 46 | 07-13 | PR-28 implementation and 73 first author calls | 2 | Executed within bounds, but skipped the highest-information action: a single strict-output canary before all 73 calls. It produced no valid author output. |
| 47 | 07-14 | Final 73 exact replays and G7 PENDING close | 2 | Correctly closed the authorized thread and produced a paper limitation. Necessary once authorized, but the value was closure, not a robustness result. |

## What truly moved the needle

The highest-contribution sessions shared six characteristics:

1. **A paper-facing exit criterion was named before work began.** O4-RUN targeted a complete panel; MVP-A1 targeted a complete descriptive preview; W3 targeted a dated reading plus immediate table fill.
2. **The scientific question was bounded.** Exact items, models, calls, prices, and claims were frozen. The session did not build for hypothetical future use.
3. **Execution and paper conversion happened together.** The strongest example is session 30: PR-16 repair → W3 recompute → PAPER tables in one session.
4. **Stops protected evidence, not convenience.** Transcript repair, PR-13, PR-20, and PR-21 were material integrity issues; stopping prevented false claims.
5. **Owner decisions were bundled.** The 07-12 ruling session closed an entire backlog at once. Serial one-line ratifications were much less efficient.
6. **The session ended with evidence or prose, not merely more readiness.** A run, table, corrected claim, or manuscript section is a real delta; a higher test count alone is not.

## Rabbit-hole indicators

A task should be presumed off-path when two or more of these are true:

- it concerns a downstream gate while an upstream human-data prerequisite is absent;
- its output is another prompt, handoff, dashboard rewrite, authorization memo, or specification decision rather than evidence or manuscript content;
- it adds robustness, replay, concurrency, custody, or provider abstraction beyond the narrowed paper claim;
- it discovers one specification gap per session instead of running one end-to-end preflight;
- success is described mainly by test-count growth or implementation volume;
- a one-item canary could answer the key feasibility question before bulk engineering or calls;
- the manuscript can truthfully disclose the issue as `PENDING` or a limitation without changing the registered conclusion;
- it consumes a full session without a paper-facing artifact or removal of a P0/P1 blocker.

G7 exhibited nearly all of these indicators. The work was not random, but its sequence optimized reproducibility of a robustness gate before confirming the gate could produce any usable perturbation and while labels remained the release bottleneck.

## Recommended path from here

### Lane A — complete the MVP paper now

The exploratory MVP-A1 evidence is already complete and reviewed. The next agent session should:

1. assemble the living `PAPER/` sections into one reader-ready MVP manuscript;
2. replace every non-required result placeholder with either the licensed descriptive value or an explicit `PENDING`/limitation statement;
3. keep O5 release claims separate from MVP §6A;
4. fill the abstract only with licensed benchmark-construction, MVP, and descriptive claims;
5. generate and visually inspect a PDF;
6. issue one claims-conformance checklist and stop for Jimmy's manuscript review.

This is a one-session paper deliverable. It requires no new model call, label, ruling, or harness feature.

### Lane B — complete release-grade O5 incrementally

Jimmy's labeling is the long pole. Work one design at a time, in frozen FR-17(a) order:

1. wave 1 Part A: `02`, `07`, `01` = 84 CSV rows, plus the registered overlap/reliability arm;
2. wave 1 Part B: work the exported unresolved cells for the same designs;
3. as soon as one design is complete, run `walkworthy.judge_validation`; do not wait for the full wave if the frozen input contract permits a truthful per-design report;
4. apply the frozen G4 branch and recompute that design's Part-B-resolved metrics;
5. update Table 6.1, Table 6.2, Table 6.3, the O5 report, and limitations in the same session;
6. repeat for waves 2 and 3;
7. after all available verdicts, obtain one Opus adversarial memo and one Jimmy sign-off session.

If no labels exist, an O5 execution session stops immediately. It may switch to already-authorized paper assembly, but it must not invent another engineering lane.

## Session operating contract for future work

Every future session should begin with five explicit fields:

| Field | Required content |
|---|---|
| Paper delta | Exact table, paragraph, figure, report, or PDF that will be new at close. |
| Sufficiency gate | The smallest condition that makes that delta truthful. |
| P0/P1 blocker | One concrete blocker, or `none`. P2/P3 cannot block. |
| Execution timebox | At least 80% of effort; documentation/testing/dashboard at most 20%. |
| Stop condition | The event that ends the task without opening a new lane. |

Additional controls:

- **One preflight, one ruling bundle.** Before paid or complex execution, review prompt, parser, schema, reviewer identity, retry, missing-cost behavior, outputs, and claim boundary together. Submit one owner decision package.
- **Canary before framework.** Run the cheapest permissible one-item end-to-end canary before building bulk resume, concurrency, or crash-recovery features.
- **No artifact-free session.** A session cannot be called complete based on tests, plans, prompts, handoffs, or dashboard changes alone unless it hit a genuine external stop.
- **Paper conversion is part of execution.** A new reading is incomplete until the licensed table/prose is updated.
- **No speculative code.** Change code only after a focused failing test demonstrates that existing mechanics block the next statistic, verdict, table, or claim.
- **Dashboard once.** Reconcile the dashboard and handoff at session close, not repeatedly during execution.
- **Limitations beat indefinite hardening.** If a P2/P3 issue can be truthfully bounded without changing the paper conclusion, disclose and defer it.

## File and code actions

### Change now

- `00-PORTFOLIO/project-dashboard.html`: make manuscript assembly the next agent deliverable, labels the parallel owner bottleneck, and add the session-value/anti-rabbit-hole gate.
- `00-PORTFOLIO/efficiency-assessment.md` and `.html`: freeze this retrospective and make it discoverable from the dashboard.

### Next high-value session

- Create `PAPER/walkworthy-mvp-manuscript.md` as the single assembled reader-facing draft.
- Create a visually verified `PAPER/walkworthy-mvp-manuscript.pdf`.
- Update existing living paper sections only where assembly reveals an unlicensed claim, unresolved placeholder, or missing source link.
- Use Pandoc/Typst or the existing PDF tooling directly. Do **not** build a general document pipeline unless the one-off assembly command proves insufficient.

### When labels land

- Use existing `harness/walkworthy/judge_validation.py`; its CLI already joins filled blind CSVs and emits a dated immutable G4 report.
- Use existing `harness/walkworthy/label_sample.py` Part-B export functions and the post-PR-16 derived records.
- Add code only if a focused label fixture proves the existing join/export cannot consume the actual completed files. The first acceptable code change is a narrow validator or adapter with TDD—not a new labeling platform.
- Produce NEW dated G4/O5 reports; update the living PAPER files immediately.

### Do not change now

- no G7 author, perturbation, SUT, judge, replay, parser, or custody code;
- no model roster, provider, concurrency, or retry framework;
- no benchmark item/key or frozen gate-rule changes;
- no HOLDOUT access;
- no broad test refactor or dashboard generator;
- no parent BibleBench portfolio file from this scope-locked session. The parent `ACTIVE-CRITICAL-PATHS.md` is stale and should be corrected in a separate portfolio-scoped session.

## Best immediate actions

1. **Next Codex session:** assemble the complete descriptive MVP manuscript and PDF; update no benchmark mechanics.
2. **Jimmy in parallel:** complete wave-1 labels and the reliability overlap.
3. **First label trigger:** run G4 and Part-B recompute for the completed design(s), then update paper tables in the same session.
4. **After each wave:** one bounded review; no new model or robustness work.
5. **After O5 report:** one Opus adversarial claims memo → Jimmy sign-off.

The project should now measure progress by reader-ready evidence and manuscript pages, not by the number of tests, contracts, rulings, or prepared future calls.
