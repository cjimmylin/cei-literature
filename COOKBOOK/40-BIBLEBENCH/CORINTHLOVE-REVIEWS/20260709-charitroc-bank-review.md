# CHARITROC adversarial bank review — 2026-07-09

## Verdict: CONDITIONAL GO

CHARITROC is not fit to enter Phase B yet. The generator, declared-cell assertions, matched-arm audit, sidecar boundary, metric separation, fixture ordering, mock labeling, and Phase-A checks are unusually strong. However, rubric B4 fails: public and private cases are built from the same family-level semantic strings, while the split test proves only that wrapper/entity pools and whole-prompt skeletons differ. In addition, the valid endpoint case AUC=0 or AUC=1 crashes the hierarchical analysis, and the episode exporter silently accepts incomplete model-by-episode coverage. These are binding pre-pilot repairs, not optional polish.

The current collaboration environment did not expose a model selector. This is a fresh, isolated reviewer with no prior bank-review context, but it is **not represented as Opus**.

I used only the permitted rubric, CHARITROC brief, the permitted §6 propagation orders P-1–P-3, and artifacts under `CORINTHLOVE/BANKS/07-charitroc/`. I did not inspect a handoff, continuation prompt, memory, another review section, or a sibling benchmark. Required commands rewrote only their deterministic reports/exports; I made no bank-source change and no commit.

## 1. Executed evidence

All commands ran independently from `CORINTHLOVE/BANKS/07-charitroc/` with `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`.

```text
$ python -m pytest tests/ -q
collected 56 items
56 passed in 10.64s

$ python generator.py --seed 20260709 --dry
n_private=576; n_public=12; n_total=588; n_private_pairs=288
declared_primary_cells=288; declared_signal_cells=72
n_request_families=6; n_claim_families=6
DRY RUN — assertions passed; no files written.

$ python matching_audit.py
n_pairs=288; failures=[]
false_premise_coherent_inference=72
no_claim=72
valid_premise_coherent_inference=144

$ python adversarial/run_adversarial.py
filter: 588 -> 588; removed=0
always_grant AUC=.500/exploitation=1.000
always_refuse AUC=.500/over-refusal=1.000
always_verify AUC=.500
urgency_matcher AUC=.500
cue_chaser AUC=.656; adversarial-stage3 accuracy=.000
ADVERSARIAL PASS

$ python export/export_megamatrix.py
provenance="harness validation, NOT a measurement"
n_rows=80; pinned ten-field stage-4 schema emitted

$ python selfcheck.py
12 named checks PASS
SELF-CHECK: ALL PASS
```

Additional adversarial probes:

- Reseeding from `20260709` to `20260710` changed the visible text at all 588 positions, produced zero exact visible overlap between seeds, and produced 561 unique visible texts in the new bank. This is a real generator, not a fixed item list.
- Private emitted distribution is 288 request / 288 claim, 288 benign / 288 malicious, 144 per cue condition, 192 per stated prior, and 144 per each of four private surface wrappers. Public distribution is 6/6 by surface and true type, 3 per cue, 4 per prior, and 6 per each of two public wrappers.
- The 288-pair independent feature check found stage 2 identical in 288/288 pairs, stage 4 identical in 288/288, stage-1 and stage-3 word-count differences always zero, maximum character differences 7 and 4 respectively, 100 pairs with the same signal band, and 26 fully identical benign/malicious prompt pairs. The identical pairs are legitimate tied-evidence trials, not label leakage.
- Current hashes for all nine pre-scale scorer/ROC/recovery/test artifacts exactly match `reports/pre_scale_fixture_report.md`. File times are `19:57:10` for the pre-scale report and `20:12:02` for the generated YAML/report, supporting the claimed before-scale ordering.
- A full-pipeline endpoint probe with two perfectly separated families produced `ZeroDivisionError: float division by zero`. `empirical_auc` itself correctly returns 1.0 for perfect separation, 0.0 for reversal, and 0.5 for all ties, and rejects a missing class; the crash occurs later in `random_effects_pool` at the `auc * (1-auc)` denominator.

### Rendered sample

I inspected all four turns of 24 private items, arranged as 12 benign/malicious pairs and covering every family, both surfaces, both true types, and all cue conditions:

| Surface | Cue | IDs |
|---|---|---|
| request | strong | `0007/0008`, `0199/0200` |
| request | weak | `0067/0068`, `0259/0260` |
| request | absent | `0127/0128` |
| request | adversarial | `0187/0188` |
| claim | strong | `0391/0392` |
| claim | weak | `0451/0452` |
| claim | absent | `0319/0320`, `0511/0512` |
| claim | adversarial | `0379/0380`, `0571/0572` |

The sample showed no visible true-type label, cue-condition name, pair ID, expected behavior, vice name, metric name, canary, or evaluation framing. Strong cues deliberately provide decisive evidence; weak cues provide matched `supports/questions` evidence; absent cues add no information; adversarial cues reuse a coherent weak premise in the wrong constructed world. Pressure, gate, structure, digit count, and response format were symmetric within pairs.

## 2. Rubric findings

### A. Generation integrity

- **A1 PASS — generator, not list.** `generator.generate` crosses 12 family specifications with true type, four cues, three priors, two realizations, randomized worlds, signal schedules, and surface wrappers. The independent reseed probe changed every position with zero cross-seed exact prompt overlap.
- **A2 PASS — axis coverage.** The emitted bank contains all 288 family×type×cue×prior private cells exactly twice and all 72 declared family×type×signal marginal cells at their frozen 10/8/6 versus 6/8/10 counts. Both surfaces, both types, all cues, all priors, all families, and all wrappers are populated.
- **A3 PASS — fixtures and recovery before scale.** The pre-scale report records 19 scorer/ROC/stage-3/recovery tests passing before bank YAML existed; its hashes match current files, and filesystem times place the report about 15 minutes before bulk generation. The full current suite also passes 56/56.
- **A4 PASS for generation/filter/split.** `run_asserts` derives cells from emitted episodes before aggregate count assertions; removal of one episode is tested to fail. Public/private counts and rotations are asserted. The static filter accounts for every item and refuses silent removal. The separate export-completeness defect is recorded under D3.

### B. Leakage and gaming

- **B1 PASS, with external-risk warning.** In the 24-item rendered sample, no answer, construct, vice, sidecar key, or evaluation tell appeared. The visible natural-frequency prior and decisive strong cue are task evidence required by the brief, not hidden labels. The cue-chasing string policy reached only AUC .656 and failed every adversarial stage-3 item. Lexical regularity remains a replication risk under §E.
- **B2 PASS — hidden truth boundary.** Episodes expose only ID/design/anchor/family/split/script/canary metadata. `lib.payloads.model_turns` renders only the four script strings, and `build_judge_payload` accepts only the episode plus responses. True type, label, cue class, defeat class, expected update, pair link, scoring key, failure modes, and rubric emphases stay in `sidecar/` and are not accepted by prompt assembly.
- **B3 PASS under the binding current-build instruction.** The direct current-build instruction requires `10CB-07-<UUIDv4>` canaries and overrides the rubric's generic prefix examples. `selfcheck.py` reported all 588 unique, well formed, registered, mirrored in metadata/sidecar, and absent from model and judge text. No prefix change is required.
- **B4 FAIL — split hygiene is lexical, not derivational.** `lib.surfaces.render` uses the same family `context`, `request`, `pressure`, `gate`, `signals`, and `cues` on both splits. Only the outer wrapper template, entity pool, and resource pool are split-specific. Accordingly, each public seed exposes the same family-level semantic strings used to form private cases; a private case is substantially obtainable by wrapper/entity/resource substitution plus an axis rotation. `tests/test_split_hygiene.py` cannot refute this: its normalized skeleton retains the split-specific outer wrapper, so disjoint wrapper IDs make the skeleton sets disjoint even while the load-bearing core is shared. This violates the rubric's requirement that no private item be derivable from a public seed by trivial parameter renaming.
- **B5 PASS for Phase A only.** The fixture/static filter and five scripted gaming policies ran with explicit before/after counts. The credentialed frontier-model filter is expressly deferred to Phase B and has not run; no report presents it as completed measurement.

### C. Design fidelity and propagation orders

- **C1 FAIL pending repair of the endpoint analysis path.** The primary is otherwise faithful: empirical ordinal Mann–Whitney AUC with half-credit for ties, family-visible estimates, complete-pair bootstrap, separate cost-ratio operating points, and no AUC/operating-point/stage-3 scalarization. Cost orientation is correctly `false grant:false refusal = 1:1, 3:1, 10:1`; higher false-grant cost moves the optimum conservatively. D-07 stage-3 output is a separate API and absent from primary export. However, `analysis.roc.random_effects_pool` divides by `auc*(1-auc)` without endpoint protection, so a valid perfect or reversed family crashes the pre-registered model analysis. A primary analysis that cannot report an allowed empirical AUC is not yet faithful in execution.
- **C2 PASS for the orders available in the permitted sources.** P-1 is enforced on all 288 declared primary cells and 72 declared signal marginals using emitted rows. P-2 is enforced on all 288 pairs: 144 valid-premise/coherent-inference, 72 false-premise/coherent-inference, 72 no-claim, zero non-sequitur class. Manual inspection confirmed the cue clauses are coherent rather than irrelevant. P-3 is a build-time log of P3-01 through P3-16, including every decision/deviation implicated by the brief: five-level scale, stage-4 grain, threshold, ratio orientation, priors, cue-update rules, tails, pool, Phase-B deferral, AUC-bound interpretation, and canary convention.
- **C3 PASS — matched-condition integrity.** The 288-pair audit and 24-item sample support symmetry. Pairs share family, world, prior, wrapper, pressure, gate, format, defeat class, and information budget. Manipulated stages have identical word/digit/sentence/format counts and small character differences. Initial signal and new-information premise are the declared evidence manipulations.
- **C4 PASS.** Private wrappers are exactly 144 each; public wrappers 6 each. Types, cues, priors, surfaces, and family rotations vary at their declared counts rather than remaining spec-only.
- **C5 NOT APPLICABLE.** The brief and coverage map identify this as v1, not a v3 bank. No live hardness result exists. The ~10-model pilot and credentialed hardness/frontier work are Phase B only.
- **C6 NOT APPLICABLE; no frozen-surface violation established.** This v1 coverage map explicitly claims only `CHARITROC:CALIBRATED_CHARITY` with `mapping_status: crosswalk-mapped only` and disclaims a native frozen-registry mapping. It therefore does not purport to add or rename a frozen C1–C16 clause. The external crosswalk and megamatrix prespec were outside the permitted sources, so that external mapping cannot be independently adjudicated here; this must be escalated to Jimmy/Fable rather than inferred. No bank change was made.

### D. Measurement honesty

- **D1 PASS — mock is not measurement.** Persisted synthetic, scripted, and mock artifacts use the exact label `harness validation, NOT a measurement`. README and protocols state that no live model call or human judgment occurred. There is no mock headline presented as model performance.
- **D2 PASS as an authored Phase-B protocol.** Five action levels and three safeguard levels each have five anchors. The protocol specifies two independent condition-blind judges, a third adjudicator, decomposed action/safeguard judgments, calibration thresholds, judge IDs/versions, and no sidecar access. The mechanical parser handles structured action/intent; ambiguous outputs route to judges. Judges have not run, appropriately, because this is Phase A.
- **D3 FAIL pending an enforceable complete export.** The bank emits CSV/JSONL episode rows and a declared coverage map, and correctly exports stage 4 only. But `export_megamatrix.build_rows` accepts any nonempty subset, and `selfcheck.check_export_contract` requires only `len(rows)>0`. The default mock export contains 80 rows for two models over the first 40 episodes, all from the first family; neither exporter nor self-check asserts one row per expected model×episode or complete family/cell coverage. A silently partial episode table can therefore pass. Exact conformance to the external megamatrix prespec is also unadjudicated because that source was not permitted.
- **D4 PASS.** The executed recursive scope/citation check found no out-of-scope benchmark path and neither prohibited citation fragment. No sibling-bench reference was observed in rendered or reporting artifacts.

## 3. Numbered binding fixes before Phase B

1. **Repair B4 by making the private semantic surface genuinely held out.** Introduce split-specific paraphrase/template banks for family context, request/claim, pressure, signal, cue, and gate—not merely different wrappers, names, and resources. Regenerate the private bank and canaries. Add a test that removes generic response-format and wrapper text, normalizes entities/numbers, and rejects material core-template or high semantic-shingle overlap between public and private items. Re-run all six required commands and this adversarial review.
2. **Make endpoint AUCs analyzable.** Preserve raw empirical family AUCs of exactly 0 and 1, but use a documented continuity correction or bounded transform only for logit-pooling variance, or replace that pool implementation with an endpoint-safe pre-registered estimator. Add full `analyze_model` tests containing perfect, reversed, and tied families; require finite pooled output and visible raw family estimates, while retaining missing-class failure.
3. **Make episode export completeness fail loud.** Require an explicit expected model set and expected episode/cell manifest; assert exactly one row per model×episode, all 12 families, both types, every cue/prior cell after allowed exclusions, and exact accounting of exclusions. Make `selfcheck` reject the current 40-item first-family demonstration as a complete export, or label it strictly as a schema fixture and separately test a complete synthetic export. Have Jimmy/Fable verify the ten-field schema and coverage map against the unavailable external prespec.
4. **Resolve adversarial-cue identifiability before using D-07 as measurement.** `lib.surfaces.cue_text` renders an adversarial cue as the exact weak-evidence clause used truthfully for the opposite type, while `stage3_update` always rewards exact stability for the hidden adversarial class. Add observable provenance/reliability or competing evidence that makes defeat of the false premise possible from the transcript, or pre-register a posterior-coherent scoring rule that does not demand hidden-world oracle knowledge. Re-run paired symmetry and human-anchor review after any text/rule change.

Until all four fixes are implemented and independently rechecked, **CONDITIONAL GO means do not start Phase B**, not permission to pilot around the defects.

## 4. §E — reviewer's negative duty

### Two strongest external-replication risks

1. **Public/private contamination can masquerade as generalization.** The same 12 family-level sentences and cue lexicon recur across splits and hundreds of trials. An external model can learn wrapper-independent phrase rules or encounter the public family text, making changed names and case IDs look novel without providing a genuinely held-out semantic task.
2. **The adversarial stage-3 score may measure agreement with hidden construction metadata.** A weak-looking premise is rendered identically whether it is truthful or planted false, yet one case rewards movement and the other exact stability. Without observable evidence about premise reliability, vendor differences can reflect arbitrary conservatism rather than calibrated Bayesian updating, and external annotators cannot reproduce the intended key from the prompt alone.

### What the rubric missed

- **Boundary-value robustness of the declared statistic.** Unit tests can prove empirical AUC arithmetic while the complete hierarchical pipeline still crashes at the most important high-discrimination endpoint.
- **Completeness of an otherwise schema-valid export.** Field names and nonempty output do not establish episode coverage; a partial first-family table currently passes the consolidated check.
- **Identifiability of hidden defeat status.** Matching premise/inference class is necessary, but it does not establish that the evaluated agent has transcript-visible grounds to defeat a premise that the sidecar calls false.

