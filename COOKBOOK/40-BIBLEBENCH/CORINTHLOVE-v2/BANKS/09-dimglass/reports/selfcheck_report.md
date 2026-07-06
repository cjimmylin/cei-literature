# DIMGLASS self-check report

Bank: 996 private + 30 public = 1026 episodes

- **deliverable files**: PASS — 30 required deliverables present
- **YAML lint**: PASS — YAML lint OK over 1026 episodes
- **leakage**: PASS — leakage check OK (1026 episodes; 1026 sidecar entries)
- **canary registry**: PASS — 1026 canaries unique & registered (registry has 1026)
- **two-sidedness**: PASS — two-sidedness 414/1026 = 0.404 (>= 0.30)
- **twin failure modes**: PASS — twin failure modes present on every item
- **forbidden refs**: PASS — forbidden-reference grep clean (0 sibling-bench / icmi hits)

All self-checks PASS.
