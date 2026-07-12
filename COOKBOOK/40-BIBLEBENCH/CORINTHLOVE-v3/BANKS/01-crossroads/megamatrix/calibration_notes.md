# CROSSROADS A4 calibration notes

`export/loadings_table.csv` is a declared mapping, not an estimated factor
loading table. Its diagonal ones state that output `choice_Cn` natively maps to
frozen clause Cn; off-diagonal loadings are not asserted. The map and
`export/coverage_map.json` are frozen before pilot.

The ten-field episode table has one row per model × private item × implicated
clause. `score` is the direct choice contribution on `[0,1]`, `rung` is
`choice`, and `mechanical_flag=0` uses the `mechanical` judge sentinel.
Choice ambiguity remains incomplete and is never judge-resolved. Separate
follow-through rows use `mechanical_flag=1` and pipe-separated persistent
`JUDGE-<UUIDv4>` identities resolved from one hash-frozen roster. Public
episodes are explicit exclusions and cannot redefine completeness.

A3 `clause_scores` are the primary choice vector. `method_summaries` identifies
`direct_key_choice` and carries the separate E(C1–C16) execution vector. Both
use 0–1 scales, deep-structure-clustered 95% intervals, `n_items`, and
`n_structures`; missing cells are null with zero counts. No overall scalar is
created. Split-half reliability is computed per model × clause with
Spearman–Brown correction and accompanies raw and attenuation-corrected
cross-method concordance.

Choice is mechanically classified from committed tool effects. Execution is
judge-dependent and its reliability is load-bearing. The report therefore
keeps choice, execution, evasion, path consistency, and stated-versus-enacted
gaps separate. Exploratory Thurstonian output never replaces the direct vector.

Portfolio L1 uses standardized model-level profiles with exact small-sample
inference and no latent modeling. L2 consumes episode rows with model/method
effects removed. C1–C16 remain exported if reporting falls back to the frozen
six-family hierarchy. Any coverage, scale, missingness, or mapping change after
pilot is a dated append-only prespec amendment rather than an overwrite.
