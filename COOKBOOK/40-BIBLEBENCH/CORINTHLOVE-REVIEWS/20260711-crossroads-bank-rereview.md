# CROSSROADS bank fresh adversarial re-review

Date: 2026-07-11  
Reviewer: fresh independent Codex subagent  
Bank: `CORINTHLOVE-v3/BANKS/01-crossroads/`  
Verdict: **GO — cheap public qualification only**

This memo **explicitly supersedes** `20260711-crossroads-bank-review.md` and
its pre-redesign FAIL for the narrow purpose of running the documented
cheap-only, public-only qualification. It does not authorize private episodes,
frontier-model filtering, calibration, model ranking, human/key validation,
canonical live judges, E(C1–C16), bank freeze, or measurement claims.

No network or model call was made. Bank artifacts were read-only. The reviewed
100-file bank tree had the same digest before and after review:
`51b5b66f550f8930210c11cedc3fc5f804a26639a5b4c47ca406ab6732c1e0ad`.

## Independently reproduced evidence

All commands that can materialize reports were run in an isolated copy.

```text
PYTHONDONTWRITEBYTECODE=1 $PY -m pytest tests/ -q -p no:cacheprovider
  -> 214 passed in 53.87s

$PY generator.py --dry
  -> 630 accepted (600 private + 30 public), 40 rejected,
     40 structures, 60 stated pairs, information rank 15

$PY generator.py --seed causal-seed-b --dry
  -> same counts/rank with novel surfaces

$PY adversarial/run_adversarial.py
  -> exit 0; six static policies caught; 630/630 retained

$PY export/export_megamatrix.py
  -> exit 0; 4,800 episode rows

$PY selfcheck.py
  -> exit 0; passed=true

$PY -c 'from analysis.synth_recovery import run_recovery; ...'
  -> n=600; rank=15; correlation=0.9798320913;
     RMSE=0.1241061852; optimizer/build gate passed
```

Default generation hashes:

- Scenario assignment: `116b52f9ebbc34f8a133ba651a8d2d636a83a4aa220b27485f235dd658efef23`
- Private future-visible surface: `b72f5f68b1f60864d03520d6ca9afd2bda2931a9a5c34de3face08a672c02e84`
- Public future-visible surface: `f600895e32b37cf60ebe1830e299723c8fec75598e0f0234b1d4ac0a16064f7e`

Alternate-seed hashes were respectively
`6972b21ee627ef4734b179d8e7f39667a9f49b85e1e6953e1a9dba9e6748979e`,
`a5d6d6cd3de565add2734dd7699c641dbe94df9196288d452e8553048d920ddc`,
and `7736e87a82246b88a5050a03a601f2b4d2f5e46639175ce75de8385b17312ddd`.
An additional arbitrary seed was correctly rejected fail-loud when its public
standalone cue association was `0.1009278`, above the frozen `0.10` ceiling.

Other reproduced counts:

- 40 unique scenario IDs/template families/action-plan sets: 10 domains × 4
  incident grammars; every clause occurs in 10 structures and every unordered
  pair in 2; comparative rank is 15 under `sum(theta)=0`.
- Split audit: 18,000 complete future-visible public/private comparisons,
  including fork, reaction, repair, and closeout; maximum four-token
  containment `0.1432432432 < 0.25`; zero violations.
- Leakage probes: zero candidate-surface violations; zero pure-sign phrases or
  supported tokens; exact-phrase majority accuracy `0.5675`; inversion-robust
  leave-one-family-out predictability `0.5`.
- Cue audits: raw imbalance 2; coherent-action association `0.04`; public
  standalone association `0.074152`; public clause coverage 7–9 episodes.
- Hardness log: 670 decisions (630 accepted + 40 rejected); all accepted rows
  reconstruct and hash-match executable evidence. All 40 rejected rows retain
  a full snapshot, reason, and pre/post hash, isolating each of five rubric
  fields eight times. The log SHA-256 is
  `c9dd8618657734b52cc14b166f15e65b1c3410e45d2b29214d898467667699f7`.
- Canaries: 630 unique valid `10CB3-01-<UUIDv4>` values; the shared registry's
  canary→item mapping matched all 630 exactly; no canary appeared in a
  candidate payload. Registry SHA-256:
  `c709fa2b204704b3ba6a905dce43dd871c20a3200c9436c72dee3cce02a2c082`.
- Fixtures predated scale materialization: path fixture/test at 13:33,
  synthetic recovery at 13:35–13:36, follow-through fixture at 13:50, and the
  generated private bank at 17:35. The suite exercises 49 path-classifier
  cases and the 16×5×3 = 240-anchor follow-through manifest.

## Manual candidate and staged-prompt audit

I independently inspected **24/24 exact canonical candidate payloads**,
`CROSSROADS-0601` through `CROSSROADS-0624`, spanning 24 distinct causal
families. Before semantic reading, each payload was built with
`build_model_payload`, canonicalized, and hash-checked. Duplicate description
and argument copies were equality-checked and read once; every unique stage
turn, tool descriptor, target, operation, action description, effect evidence,
scalar cue, and visible consequence was read.

The contract hashes were:

```text
0601 0816549362e47bd9fbfd701972fdf5d813448fca745657e5adeadd6e481c5234
0602 fd7b5c4668b782c8fb0b0e4656976d145a865dbc488d31483314aca4211e8e71
0603 452765bb8573e6b16c43cdd46e520f530edeb6c4ec4af2661e5ec5f28e00e973
0604 b19475addbddb43a31c403421a9f690f0192fcf202c45cb2cda299f8e7676e7f
0605 4ad53b8351980ea367d7a41645eddf5a8570719a1dfa7a8da71f751e2070172e
0606 3d47b365cdeb24652a5d421920c59b0e823889978ee43c7854b7e689aeee372a
0607 f8f579cffa9b199299f99e5c4ea77dd2f6cd906f4abb59ee1dbddd321695d091
0608 a0938c0c0bc7f8c21ea163908ae4be58e414c6e51247378c2b6ae3fc055ee323
0609 27c846b1cd19806da42af121256d96b9aaba70a61a3447ed21ab5bc5ba5c6a16
0610 eab8ac5de38fbfe0f4c8d2f44db8036be7d7eec254b7b965a1e781411b068a42
0611 4e359e72fcb765dfd37e1c4affafdd15ed6b2ac65b9efb94b4e79b790aa6df8d
0612 e1d665aa8eaf72e69f2c29a9e297e594088b42a12097b716e3faa1eff672a059
0613 38ed487c1ac35ae62bb9c1e00676436addd707bdf4bb94515f43cf6ab64e7f19
0614 40b7018fb88b6f2dcaa9c37dcb1ed86af0630a9c481d045c1dc2aacf03aad489
0615 3806731d8d9f4ba104ef8642cffacf4462aedc8f8129d798a6b50edf8bb6cd8f
0616 5d03a688b43847704d43e4118908205fbffd390a8ef85c8cb092b383f9cecbd8
0617 a17dfa83ce1e266a599a04c1575825560ae3c61a423eb373503a6bf6221ed9d2
0618 4463f944ea1423c5a8b9e4c5385b7c4b1eb43944e5af294bfd6a05bce3000459
0619 44286a279dc8985656e66cf768c9b1776ef8afc320854bca0f82ba7c61884edd
0620 4ce0aa468eb3d8bc166f22e5237b9133db2151dc604482c30de731f9d25d8f6c
0621 636a6e6f8c02c4a7a8c49d5004324bd3818830af65103bb06873b83220ceeb45
0622 bf29adc13c96fde4b54bea972b74d9bf966d8a4681aca25e6c76175c1b675411
0623 08f0b2f15cf04990739019fb7439775bfb945b0c101110a6150926ff0210b567
0624 47c3d9555608f1c8822520525fcacd819037d154704dc01b6c8cac901d6d577e
```

Result: **24/24 PASS**. The sample exposed no construct label, expected pole,
clause sign, key, canary, judge ID, bank/item ID, numbered path, or policy-free
lookup cue. The prose is operational and deliberately neutral; every action
states observable effects and a real executable signature.

I also inspected exact fork→follow-through→closeout request assembly for
**12/12 structures**: 0601, 0602, 0604, 0605, 0606, 0608, 0615, 0616, 0617,
0619, 0622, and 0624. Each chain exposed 4 fork choices, then exactly 2
selected-branch repair choices, then exactly 1 disjoint closeout choice, with
completion budgets 2,048→1,024→1,024. All 36 transport bodies had zero tested
private markers; no unselected reaction or future closeout target appeared.

## Rubric A–E

| Item | Result | Exact evidence |
|---|---|---|
| A1 generator | **PASS** | Default and alternate-seed dry builds; same counts/rank, different assignment and surface hashes. |
| A2 axis coverage | **PASS** | 40 unique families; 10×4 scenario grid; 3 skins × 5 private parameter states; public held-out schedule; all declared cells fail-loud. |
| A3 fixtures/recovery before scale | **PASS** | Fixture/test timestamps precede bank output; 214 tests; planted recovery 0.9798 correlation/0.1241 RMSE. |
| A4 fail-loud counts | **PASS** | Count, rank, cue, split, hardness, ambiguity, truncation, schema, and export guards exercised; an invalid alternate seed was rejected. |
| B1 no telegraphing | **PASS** | Independent 24-payload semantic inspection plus phrase/token/family decoders. |
| B2 hidden truth | **PASS** | Exact payload/stage construction and recursive redaction tests; sidecar keys/rationales absent. |
| B3 canaries | **PASS** | 630/630 unique metadata/registry mappings; zero candidate occurrences. |
| B4 split hygiene | **PASS** | 18,000 full-future-surface comparisons, max 0.143243, zero violations. |
| B5 frontier filter | **DEFERRED BY SCOPE** | Six offline policies pass, but the required frontier-model filtering has not run. Cheap qualification does not discharge B5. |
| C1 §5/D-18 fidelity | **PASS** | Direct validated-key clause scoring is primary; E is separate; joint latent model and within-clause IRT remain exploratory/conditional. |
| C2 D/CO/P orders | **PASS** | D-18 implemented; CO-8 position honored; P-1 cells fail-loud, P-2 defeat classes match and balance 50/50 per clause, P-3 deviations are recorded in `DECISIONS.md`. |
| C3 matched integrity | **PASS** | 200 private structure×parameter groups ×3 skins preserve keys, action states, stable action, and defeat class; cue/split audits include complete action payloads. |
| C4 counterbalancing | **PASS** | Path order, tools/substrates, effects, warmth/effort/length/specificity, and clause×ordinal cells vary and meet frozen gates. |
| C5 interim hardness gate | **PASS** | 670 auditable decisions, complete accepted evidence, 40 full rejected snapshots, fixture recovery, offline bots, and complete log. |
| C6 registry | **PASS** | Only frozen C1–C16 IDs occur in mapping, scoring, tests, and exports; no renamed/novel clause or frozen-surface issue found. |
| D1 mock honesty | **PASS** | Mock roster, export, recovery, selfcheck, and docs say `harness validation, NOT a measurement`; no live result exists. |
| D2 judge protocol | **PASS AS COMPONENT CONTRACT; LIVE DEFERRED** | Tests cover fresh occurrence JCASEs, response binding, mode-0600 hash-chained crosswalk, immutable JUDGE roster, dual different-family raw ratings, third-family adjudication, blindness, and 240 anchors. Actual roster/judges and canonical E are unperformed. |
| D3 export | **PASS** | Manifest-complete 4,800-row ten-field episode table, fixed coverage map/loadings, direct choice primary, E excluded from primary. |
| D4 scope/citations | **PASS** | Bank-local selfcheck reports clean isolation and citation scan. |
| E negative duty | **RECORDED BELOW** | Replication threats remain despite GO. |

## Closure of the seven prior blockers

1. **Semantic key lookup:** closed by relational observable-state binding,
   neutral prose, 24/24 manual pass, zero pure phrases/tokens, and 0.5 held-out
   lexical predictability.
2. **Affine rows/pseudoreplication:** closed enough for qualification by 40
   unique scenario IDs/families, roles, artifacts, claims, action plans, and
   reaction signatures. Residual diversity risk remains below.
3. **Asserted hardness:** closed by evidence-derived decisions and complete
   rejected snapshots/hashes. Accepted snapshots are reconstructible from the
   persisted episode+sidecar and hash-match; the log stores their hashes and
   bindings rather than duplicating all 630 full objects.
4. **Split audit omitted actions:** closed; the audit includes all future
   candidate, fork, reaction, repair, and closeout surfaces.
5. **Linkable JCASE/self-declared judges:** closed in the canonical component
   contract. No JCASE is pre-issued; occurrences are random and response-bound,
   and family authority comes only from a frozen roster. Live use is deferred.
6. **Fork-only staged qualification/no E:** closed for the present scope by
   branch-specific 4→2→1 staged enactment and positive-duty closeout. The cheap
   runner remains intentionally path-only and cannot claim canonical E.
7. **CI array/schema mismatch:** closed; `profile.schema.json` requires CI
   object-or-null, and the regression passes in the 214-test suite.

## Reviewer's negative duty

The two strongest reasons an external replication could still fail are:

1. **Key validity is unperformed.** Three-expert human validation is still an
   external dependency. Mechanical consistency cannot establish that the
   hidden relational keys validly operationalize C1–C16.
2. **Effective causal diversity may be smaller than 40.** The bank crosses ten
   domains with four repeated incident grammars and a shared four-action plus
   repair/closeout interface. The 600 private skins/cells do not create 600
   independent causal situations; external models may exploit the common
   grammar or respond differently to more natural environments.

Free-form concern: the 40 retained rejected hardness cases are deliberately
isolated one-field mutations rather than organically rejected authored
candidates. This is adequate for fail-loud gate testing and is not a present
qualification blocker, but a future external audit would be stronger with an
append-only inventory of naturally rejected generation attempts.

## Authorization boundary

**GO** permits only the documented cheap, public, immutable-evidence
qualification after its access/ZDR/provider attestations pass. Every output
remains a qualification or harness diagnostic, not a measurement. B5 frontier
filtering, expert key validation, private execution, canonical judges/E,
calibration, discrimination claims, ranking, and freeze require separate
approval and evidence.
