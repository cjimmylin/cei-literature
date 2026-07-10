# Codex Administration Protocol

This replication was administered directly by the Codex agent rather than through any SDK or API client.

Protocol:

1. Use the already-administered item set from the existing Claude replication (`T6-T15`) so the comparison remains coverage-matched.
2. Preserve the established JSON schema and item IDs wherever possible.
3. Treat this as a single administration of the current GPT-based Codex agent.
4. Keep all outputs isolated under `CEI-Lit-WS/NORM-ETHICS/Codex/`.

Comparison note:

- Item-level agreement with Sonnet and Haiku is reported only on structurally comparable fields.
- Metric-level Opus comparisons are included from the existing repo summaries because structured per-item Opus JSON files were not present in `STATISTICS/`.
