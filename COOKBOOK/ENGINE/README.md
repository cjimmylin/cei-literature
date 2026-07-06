# CRUX Engine — shared procedural-generation + shortcut-audit infrastructure

> Built 2026-07-06 (COOKBOOK core-track queue item 2). Implements the CRUX
> generator per revised `20-DESIGNS/06-crosscutting-crux.md` §3.1/§4 plus the
> portfolio-wide **X2 shortcut-audit** tooling (KB04 §6 item 5). This is *shared
> infrastructure*: design 06 CRUX uses it directly, and its procedural core is
> reused by designs 01 (UNMARKED) and 05 (CULTIVATE). Built once here.

## Why this exists

CRUX builds second in the portfolio **either way** — its procedural-generation
core is reused by every other design, and the X2 shortcut audit is mandatory
portfolio-wide (every design must show a lexical baseline ≈ chance and a
10%-fine-tune probe below parity before any discrimination claim). So the engine
was built ahead of the pilot, from the locked post-gate spec, test-first.

## Modules (`crux/`)

| Module | Responsibility | Spec anchor |
|---|---|---|
| `values.py` | The 5 Schwartz-anchored core values (4 higher-order + care/loyalty relational axis), each with a named clause; the 10 conflict pairs. | 06 §3.1 (M1 fix: values anchored to an external taxonomy) |
| `factorial.py` | The typed factorial (`value_pair × stakes × uncertainty × beneficiary × relationship × reversibility`, full grid = 1,440 cells); screening to a **≤60-cell fractional design** with balanced main-effect marginals and a **published confounding structure**. | 06 §3.1, §4 (C2 fractional design) |
| `generator.py` | Causal-graph scenario templates that **guarantee the conflict is real** (each option provably sacrifices one value); fresh-per-run surfaces; **matched triads** for the Coherence transitivity test (commensurable cells only, M3); **minimal-pair** factor edits for AMCE. | 06 §2 (CO), §3.1 |
| `shortcut_audit.py` | The X2 gate: a lexical/length/bag-of-words **nearest-centroid baseline** (must sit ≈ chance) + a **10%-fine-tune probe** interface (injectable trainer; below-parity = pass). | KB04 §6 item 5; 06 §6/§7 P3 gate b |
| `pilot.py` | Reusable entrypoint: `publish_spec()` (releasable spec) + `build_pilot_instances()` (fresh instances). `python -m crux.pilot --out DIR`. | 06 §3.1 (published spec; private ranges) |

## Design ↔ code mapping (the load-bearing guarantees)

- **"PF is a fingerprint of a defined hand" (M1)** → `values.CORE_VALUES` anchors
  every value to a Schwartz higher-order value (or the care/loyalty relational
  axis) with an operational clause. Test: `test_anchors_cover_all_four_schwartz_plus_relational`.
- **"The pilot does not populate the ≥1,440-cell grid" (C2)** → `factorial.fractional_design()`
  screens to ≤60 cells, main-effect–balanced, with `confounding_report()` naming
  the aliased factors and quantifying residual pairwise imbalance. Tests:
  `test_fractional_design_is_at_most_60_cells`, `_main_effects_are_balanced`,
  `_publishes_confounding_structure`.
- **"Each option provably sacrifices one value"** → `generator.generate_scenario()`
  builds a two-action causal graph where each action satisfies one value and
  violates the other; no option honors both. Test: `test_each_option_sacrifices_the_other_value`.
- **"CO triads drawn only from commensurable cells" (M3)** → `generator.is_commensurable()`
  excludes irreducible-uncertainty cells; `matched_triad()` only uses commensurable
  cells. Test: `test_matched_triad_covers_three_pairwise_conflicts_all_commensurable`.
- **"Shortcut audit mandatory" (X2)** → `shortcut_audit.x2_gate()` passes only when
  the lexical baseline is ≈ chance AND the probe is below parity. Tests prove it
  *catches* a length-leaky set, not just asserts cleanliness.

## Run the tests

```bash
cd COOKBOOK/ENGINE
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest -q
# 33 passed
```

## Emit artifacts

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m crux.pilot --out out
# wrote spec (60 cells) + 60 instances to out
```
`out/crux-published-spec.json` is the **releasable** spec (values + factors +
fractional design + confounding report). `out/crux-pilot-instances.json` is an
**illustrative** fresh instance set — regenerate per run; do not treat as
canonical items (live items are private per §3.1).

## Honest limitations (carry into the pilot)

1. **The fractional design is a *randomized balanced* fraction, not a constructed
   mixed-level orthogonal array.** Main effects are exactly balanced; higher-order
   interactions are aliased and the residual pairwise imbalance is *published*
   (`max_pairwise_imbalance`, ~5 at n=60) rather than zero. A future version could
   swap in a true OA(60; 10¹3²4¹2²) to drive pairwise imbalance toward 0 — the
   `confounding_report()` interface is stable across that change.
2. **The 10%-fine-tune probe is an interface, not a trained probe.** Real
   fine-tuning needs training infra; `FineTuneProbe` takes an injectable trainer
   and the pass/fail rule is implemented and tested, but the trainer is wired at
   pilot P3 (TODO in `shortcut_audit.py`).
3. **Scenario surfaces are schematic templates**, sufficient for structure/gaming
   tests and pilot wiring; naturalistic-anchor items (06 §9's 15% forum-sourced
   diagnostic) are authored separately, not generated here.
4. **Human-validation gates are external.** The generator emits items; the ≥80%
   "coherent + genuinely conflictual" validation-survey gate (06 §6/§7 P1) runs
   on humans, not in this code.
