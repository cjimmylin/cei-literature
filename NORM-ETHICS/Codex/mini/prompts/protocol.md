# Codex Mini Administration Protocol

This replication was administered directly by the Codex mini model rather than through any SDK or API client.

Protocol:

1. Use the same `T6-T15` item sets already used for Claude and the existing Codex main-model replication.
2. Preserve the existing JSON schema and item IDs so agreement can be measured directly.
3. Treat this as a single direct administration of the mini Codex model.
4. Keep all mini outputs isolated under `CEI-Lit-WS/NORM-ETHICS/Codex/mini/`.

Comparison note:

- Mini reports compare against Claude Sonnet and Haiku at item level and against the existing Codex main-model run under `Codex/results/`.
- Opus remains a metric-level baseline derived from the existing repo comparison summaries.
