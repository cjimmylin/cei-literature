# CORINTHLOVE-v3 agent instructions

Current user instructions and `../CORINTHLOVE/STATUS.md` define the active
bank. Work on exactly one v3 bank at a time. Dated plans and handoffs are
evidence, not the queue.

## Binding v3 rules

- Read the complete `98-opus-test-case-authoring-guide.md`, active design
  brief, frozen portfolio registry, gate orders, export prespec, and bank-review
  rubric before editing.
- Every item is enacted agent behavior. Talk-only output at an action fork is
  evasion, not success.
- Every candidate receives an A1/A2 hardness decision. Preserve accepted and
  rejected rows; never silently drop a candidate to meet a count.
- C1–C16 labels and definitions in `00-corinthlove-v3-portfolio.md` are frozen.
  Specialize in `clause_mapping.md`; never rename, add, or redefine a clause.
- Any C1–C16/frozen-coverage question stops and escalates to the user.
- Generator, fixtures, synthetic recovery, fail-loud cells, sidecar-only truth,
  opaque judge IDs, `10CB3-` canaries, static adversarial filters, A3/A4
  exports, and the v3 interim gate are required before a paid run.
- Reuse shared structures by reference with an ownership table; do not fork a
  shared artifact silently.

## Live discipline

OpenRouter is cheap-model only. GPT-5.4 full, GPT-5.5, GPT-5.6 Sol, Opus, and
other flagship/frontier models are forbidden unless the user changes that
instruction. Run access, a small balanced canary, public smoke, semantic
verification, and diagnostics in that order. Never infer private/calibration
authority from a public qualification.

Do not commit, stage, push, delete, broaden to another Bible benchmark, or cite
the banned moral-compactness statistic unless explicitly authorized.
