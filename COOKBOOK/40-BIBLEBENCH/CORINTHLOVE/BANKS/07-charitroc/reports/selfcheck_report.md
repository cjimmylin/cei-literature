# CHARITROC self-check report

Bank: 576 private + 96 calibration + 12 public = 684 episodes

- **required files:** PASS — 63 required deliverables present
- **generated bank:** PASS — 576 private + 96 calibration + 12 public = 684; 288 private, 96 calibration, and 72 signal cells complete
- **pair audit:** PASS — 288/288 private pairs pass defeat-class matching; 12 declared ambiguity controls and 0 undeclared twins
- **static filter:** PASS — 684 -> 684; 0 removed
- **split hygiene:** PASS — 21120 cross-split comparisons pass 4-token <0.25 gate (calibration|private=0.222, public|calibration=0.222, public|private=0.143)
- **lexical gate:** PASS — 7 fixed policies, 2 lexical models, and 2 metadata decoders pass AUC caps
- **sidecar boundary:** PASS — 684 model payloads exclude sidecar truth and canaries
- **judge token map:** PASS — 684 opaque judge IDs exactly cover the three-way bank
- **canary registry:** PASS — 684 bank canaries unique, well-formed, and registered
- **export contract:** PASS — 1152 complete rows; 2 models x 576 episodes; 288 cells; 108 exclusions; pinned 10-field stage-4 schema
- **judge anchors:** PASS — 5 action levels and 3 safeguard levels, 5 exemplars each
- **decision log:** PASS — P3-01 through P3-27 documented before pilot
- **mock honesty:** PASS — all persisted mock/synthetic outputs labeled 'harness validation, NOT a measurement'
- **scope and citation:** PASS — scope/citation scan clean
- **live clients:** PASS — no live model client imports

SELF-CHECK: ALL PASS
