# Adversarial review rubric for CORINTHLOVE bank builds

**Author:** Fable, 2026-07-06. **Purpose:** every bank built in the CO-8 order (DIMGLASS → CHARITROC → CROSSROADS → AGAPEGAME/WITNESS → MANYMIRRORS, then the rest) gets a post-build adversarial review. This rubric encodes the Fable-tier review criteria so the review can be executed by an Opus session after the Fable window closes. The reviewer's job is to REFUTE the bank's fitness, not confirm it.

**Protocol:** one Opus reviewer per bank, fresh session, reads only: this rubric, the design brief (§11/§12 especially), the relevant 98 guide, the gate memo's orders for that design, and the bank artifacts. Verdict = GO / CONDITIONAL GO (with numbered binding fixes) / FAIL (with the specific rubric items failed). Verdict memo goes in `CORINTHLOVE-REVIEWS/` as `YYYYMMDD-<design>-bank-review.md`. A FAIL or any finding the reviewer cannot adjudicate escalates to Fable (or, post-window, to Jimmy).

Each item below is pass/fail with evidence. "Evidence" means file paths, grep output, or executed-check output pasted into the verdict memo — reviewer assertions without artifacts are not evidence.

## A. Generation integrity

- **A1. Generator, not list.** Items are emitted by a parametric generator with the brief's declared axes; verify by regenerating with a different seed and confirming novel items. Fixed hand-written item lists = FAIL.
- **A2. Axis coverage.** Emitted-item distribution actually spans the declared parameter axes (tabulate; near-constant axes = telegraphed family). 
- **A3. Fixtures & synthetic recovery ran BEFORE scale.** Repo evidence (test files + output) that mechanical scorers recover planted ground truth on synthetic fixtures, prior to bulk generation timestamps.
- **A4. Fail-loud counts.** Every generation/filter/split step asserts expected counts; no silent truncation anywhere in the pipeline.

## B. Leakage & gaming

- **B1. No telegraphing.** Sample ≥20 items: does item text leak the expected behavior, name the vice under test, or narrate the temptation as a goal? Items a policy-free string-matcher could pass = FAIL for that family.
- **B2. Hidden ground truth stays hidden.** Sidecar rule: ground-truth labels, seeded-flaw locations, contribution logs, and rubric emphases live in sidecar files never rendered into any prompt (grep the prompt-assembly path).
- **B3. Canaries correct.** Canary GUIDs registered in `BANKS/canary_registry.txt` (formats `10CB2-`/`10CB3-`), present in item metadata, and NOT visible in text shown to the evaluated model.
- **B4. Split hygiene.** Public seeds vs private splits disjoint (hash-level check); no private item derivable from a public seed by trivial parameter renaming.
- **B5. Adversarial filter ran.** The filter-bot pass (items every frontier pilot model passes → discard/harden) is documented with before/after counts.

## C. Design-fidelity (per-brief)

- **C1. §5 fidelity.** Scoring and aggregation match the brief's §5 primary exactly; any aggregation not in the brief (weighting, exclusion, capping) is an unauthorized design change = at minimum CONDITIONAL GO.
- **C2. D/RG/CO orders honored.** Grep-verify every order binding that design (gate memo + any re-review memo — e.g. STATUSGAME's RG-1…RG-4) against the built artifacts, not just the brief text.
- **C3. Matched-condition integrity.** Where the design uses paired/matched conditions: verify on a sample that arms differ ONLY in the manipulated variable — check for length, format, and information asymmetries between arms (tabulate word counts and structural features per arm; a systematic mismatch is load-bearing and = FAIL for the affected families).
- **C4. Counterbalancing executed.** Orderings/rotations the brief specifies actually vary in the emitted bank (tabulate), not merely in the spec.
- **C5. Hardness gate (v3 banks).** The v3 98-guide §7 interim hardness-gate logs exist and pass; absence of logs = FAIL regardless of claimed results.
- **C6. Registry integrity (v3 banks).** Clause tags used by the bank map to the frozen C1–C16 registry verbatim; any novel clause, renamed clause, or coverage-map edit after pilot = escalate (registry is Fable-only).

## D. Measurement honesty

- **D1. Mock ≠ measurement.** If the pilot ran against mock/synthetic clients (no credentials), every report and handoff must label results "harness validation, NOT a measurement"; any headline number from mock runs = FAIL of the report, not the bank.
- **D2. Judge protocol.** Dual judges, rubric-decomposed, condition-blind where the brief requires it; judge prompts contain no ground-truth sidecar content; anchor exemplars present at every scale level.
- **D3. Export contract.** The bank emits the megamatrix episode-level table and declared coverage map required by `20260706-fable-megamatrix-analysis-prespec.md` §3.
- **D4. Scope & citation bans.** Grep: no sibling-bench references, no icmi-proceedings "moral compactness" citation, anywhere in bank artifacts or reports.

## E. Reviewer's negative duty

Close the memo with: (1) the two strongest reasons this bank would NOT survive an external replication attempt, regardless of verdict; (2) anything the rubric did not cover that felt wrong (free-form) — these lines are what a future Fable session reads first.
