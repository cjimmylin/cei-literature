# CHARITROC pre-scale fixture and recovery gate

**Provenance:** harness validation, NOT a measurement.

- Recorded: `2026-07-09T19:56:53-0700`
- Scale artifacts at execution: `episodes/private_bank.yaml` absent;
  `seeds_public.yaml` absent.
- Interpreter: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python`

## Command

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest \
  tests/test_action_scale.py tests/test_roc.py \
  tests/test_stage3_update.py tests/test_synth_recovery.py -q
```

## Output

```text
collected 19 items
tests/test_action_scale.py ....
tests/test_roc.py .......
tests/test_stage3_update.py ....
tests/test_synth_recovery.py ....
19 passed in 0.99s
```

## Frozen source and fixture hashes (SHA-256)

```text
4baeade64d67c7000417dd2204c4ec28024256e159f8d148cef3a0d94d333cc2  scorers/fixtures_action_scale.json
1ec5cc3487e08bb6795fedcc1aad6a1b82a14c5b849827ad99e1f918b272f6d3  scorers/action_scale.py
3a2560d0ddb1ee2b1e3e96f27a518c92fe413a63922045761cbf7c4081ef6637  scorers/stage3_update.py
bdec831a1ec71c737f61a690973ebb136aa8a071b5dfdf6b65d4caeaebf75ae9  analysis/roc.py
c1dda0826166f50d0625671a445ee462a0d8f818d7510aa905c96d8f3ead0030  analysis/synth_recovery.py
31e55e7da5f1c0df37adec19bc663ca7cb8b460521d1d6c1fcb5f436b7de3fe5  tests/test_action_scale.py
47d0b79fe46ddd2b14ac69fb526d2c7634f22726174cf73f7d0c3940d6c0d571  tests/test_roc.py
e6fe0da8ed5aa468176f5f0b8080a0c5e22b631d9e718f341901af16cd6ec16a  tests/test_stage3_update.py
954b8f93f1747fa5ecf3d6aded9123c39b30abb1822502fe65725a90cc3047b2  tests/test_synth_recovery.py
```

This record establishes rubric A3 ordering: the mechanical scorer fixtures,
empirical ordinal-AUC recovery, loss-ratio orientation, hierarchical pooling
smoke test, and D-07 stage-3 recovery all passed before bulk generation.

## Post-review repair gate (before central regeneration)

**Provenance:** harness validation, NOT a measurement.

The isolated adversarial review required four repairs. Each repair worker added
the regression tests first and reported its focused green run before the root
session regenerated the bank at `2026-07-09T20:42:40-0700`:

```text
endpoint-safe full analysis: 14 passed
manifest-complete export and self-check: 19 passed
split semantics + observable adversarial-cue contract: 30 passed in 5.61s
generator dry gate: 576 private + 12 public; 288 pairs;
                    288 primary cells; 72 signal cells; assertions passed
```

The behavioral repair-source mtimes are `20:35:12` through `20:40:12`, before
the `20:42:40` regenerated YAML, sidecar, and generation report. The root
session then ran the complete regenerated suite: `75 passed in 17.90s`.
Afterward, the consolidated self-check was tightened to require the two new
P3 entries as well as P3-01…P3-16; that report-only contract change is covered
by the final post-review verification rather than claimed as pre-regeneration.

### Post-review repair hashes (SHA-256)

```text
66563147af7081e23427849b1eb7925ba7a4bdaad083010a5d57981fd4f9862f  analysis/roc.py
dd16718a7935a12129a4501ec3f87ff3194a200e6fe7edd5098f22a65791d8e4  analysis/analyze.py
427074f8c5e3af4b9cf78d16b796b2235e0f7c5560ca71fee533b6712e064fbc  analysis/model_spec.md
fbd5d6f53fc7ecdc202215ea86929cb95cb22b891604e6cebbe1e1ee34848938  scorers/stage3_update.py
e20482e10278ab7f19b591d4b49ae537b7b4dd1ede120353bd30de909105ebf3  generator.py
4a2fad679eb8287caebbb9a45d378818d7dcd7b16a71107c70cdaf81b8ccb9a1  lib/families.py
f9eecae3b68a244a631be4d3da73b5fa0846cdbc186a24bbd7313eb3032deaf6  lib/surfaces.py
ce06fde57eac4d7d8fd57e764f52bbeac7c4c64e19ad24359861c6f627aa6d9e  export/export_megamatrix.py
cac2696364b415803c528633e6cc52d4e1cd2e339fe6584c5118afc1e2dc1bdf  selfcheck.py
c8bfb7eca87e12fbe4ebb3e6e0867e97716226a5eb00da32e7d1f7496f70b2cc  tests/test_analysis_pipeline.py
1c770e7d60d545e52101f9da594e9e8d310250952b3b114083690b318782e104  tests/test_export.py
5ea16b59be24088df30fcad204fff0009f6f6af5e90d4837472ad75ee33662f9  tests/test_selfcheck.py
34499df29dcd6ef315853f4175a8c6a0aed3e280b9cd3143e3c02081cb0a8b8c  tests/test_family_contract.py
65c0ddc21f40053665c5518f94d462a94502a1ef145b5effd097bc5284c50224  tests/test_split_hygiene.py
601eb6411c4d07f5721a76afe4d87de2fb7aca3388b1e513ed07f551b28cdec8  tests/test_stage3_update.py
```
