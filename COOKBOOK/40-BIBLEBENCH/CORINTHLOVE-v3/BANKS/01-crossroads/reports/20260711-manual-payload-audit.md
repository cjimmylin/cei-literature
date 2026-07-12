# CROSSROADS manual candidate-payload audit

Date: 2026-07-11 (America/Los_Angeles)

Scope: 20 exact payloads produced by `lib.payloads.build_model_payload`, not
episode summaries. The audit read every stage turn, public tool descriptor,
fork tool/operation/target, complete action description and argument-bound
effect text, and visible consequence. The sample spans 20 distinct causal
families and all four incident grammars.

Acceptance checks: no authoring, bank, canary, clause-sign, judge, or numbered
path/plan/route identifier; grammatical scenario setup; action tool and
operation agree with the stable plan and claimed effect; no mechanical token or
whitespace padding; no evaluative construct label. Payload hashes use canonical
JSON with sorted keys.

The first pass found three demonstrated defects: candidate-visible `XR-SCN-*`
authoring IDs, tool roles rotated independently of plan meaning, and the shared
phrases `Available traces show ... shows` / `This route applies route notice`.
It also found repeated `tracepoint` and trailing-whitespace padding plus
numbered later-stage branch labels. Each was corrected in the generator and
given a regression. The rows below are hashes of the final corrected payloads.

| Item | Causal family | Payload SHA-256 | Verdict |
|---|---|---|---|
| `CROSSROADS-0601` | `registry-conflicting-revision-record` | `0816549362e47bd9fbfd701972fdf5d813448fca745657e5adeadd6e481c5234` | PASS |
| `CROSSROADS-0602` | `water-unexpected-access-event` | `fd7b5c4668b782c8fb0b0e4656976d145a865dbc488d31483314aca4211e8e71` | PASS |
| `CROSSROADS-0603` | `transit-unexpected-access-event` | `452765bb8573e6b16c43cdd46e520f530edeb6c4ec4af2661e5ec5f28e00e973` | PASS |
| `CROSSROADS-0604` | `archive-incomplete-handoff` | `b19475addbddb43a31c403421a9f690f0192fcf202c45cb2cda299f8e7676e7f` | PASS |
| `CROSSROADS-0605` | `water-bounded-capacity-allocation` | `4ad53b8351980ea367d7a41645eddf5a8570719a1dfa7a8da71f751e2070172e` | PASS |
| `CROSSROADS-0606` | `release-incomplete-handoff` | `3d47b365cdeb24652a5d421920c59b0e823889978ee43c7854b7e689aeee372a` | PASS |
| `CROSSROADS-0607` | `archive-bounded-capacity-allocation` | `f8f579cffa9b199299f99e5c4ea77dd2f6cd906f4abb59ee1dbddd321695d091` | PASS |
| `CROSSROADS-0608` | `clinic-bounded-capacity-allocation` | `a0938c0c0bc7f8c21ea163908ae4be58e414c6e51247378c2b6ae3fc055ee323` | PASS |
| `CROSSROADS-0609` | `archive-conflicting-revision-record` | `27c846b1cd19806da42af121256d96b9aaba70a61a3447ed21ab5bc5ba5c6a16` | PASS |
| `CROSSROADS-0610` | `release-bounded-capacity-allocation` | `eab8ac5de38fbfe0f4c8d2f44db8036be7d7eec254b7b965a1e781411b068a42` | PASS |
| `CROSSROADS-0611` | `release-unexpected-access-event` | `4e359e72fcb765dfd37e1c4affafdd15ed6b2ac65b9efb94b4e79b790aa6df8d` | PASS |
| `CROSSROADS-0612` | `water-incomplete-handoff` | `e1d665aa8eaf72e69f2c29a9e297e594088b42a12097b716e3faa1eff672a059` | PASS |
| `CROSSROADS-0613` | `registry-incomplete-handoff` | `38ed487c1ac35ae62bb9c1e00676436addd707bdf4bb94515f43cf6ab64e7f19` | PASS |
| `CROSSROADS-0614` | `water-conflicting-revision-record` | `40b7018fb88b6f2dcaa9c37dcb1ed86af0630a9c481d045c1dc2aacf03aad489` | PASS |
| `CROSSROADS-0615` | `shelter-unexpected-access-event` | `3806731d8d9f4ba104ef8642cffacf4462aedc8f8129d798a6b50edf8bb6cd8f` | PASS |
| `CROSSROADS-0616` | `cooperative-bounded-capacity-allocation` | `5d03a688b43847704d43e4118908205fbffd390a8ef85c8cb092b383f9cecbd8` | PASS |
| `CROSSROADS-0617` | `transit-incomplete-handoff` | `a17dfa83ce1e266a599a04c1575825560ae3c61a423eb373503a6bf6221ed9d2` | PASS |
| `CROSSROADS-0618` | `clinic-incomplete-handoff` | `4463f944ea1423c5a8b9e4c5385b7c4b1eb43944e5af294bfd6a05bce3000459` | PASS |
| `CROSSROADS-0619` | `meals-conflicting-revision-record` | `44286a279dc8985656e66cf768c9b1776ef8afc320854bca0f82ba7c61884edd` | PASS |
| `CROSSROADS-0620` | `registry-unexpected-access-event` | `4ce0aa468eb3d8bc166f22e5237b9133db2151dc604482c30de731f9d25d8f6c` | PASS |

Result: 20/20 final payloads pass. This is content QA, not a model
measurement.
