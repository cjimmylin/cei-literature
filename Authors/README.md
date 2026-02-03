# Authors CRM

This directory serves as a central database for all authors associated with the papers in this literature vault. Each author has a dedicated markdown file containing their professional information and links to their work within this database.

## Structure

### File Naming
- **Format**: `FullName.md` (e.g., `Ruben E. Laukkonen.md`).
- **Constraint**: Avoid initial-only names (e.g., `R. Laukkonen.md`) unless the full name is strictly unknown.

### Content Format
Refers to `TEMPLATE.md` for the exact schema. Key sections:
- **YAML Frontmatter**: Metadata (Affiliation, Links, etc.).
- **Biographical Summary**: Third-person narrative.
- **Research & Impact**: Detailed focus areas.
- **Papers**: Wikilinks to `papers/` files.

## Workflows for Agents
- **Enrichment**: See `.agent/workflows/enrich_author_profile.md` for the step-by-step generic workflow.
- **Maintenance**: Periodically check for small files (< 600 bytes) which indicate unenriched placeholders.

## Project Status (Jan 2026)
- **Batch A & B**: Fully Enriched (Bios + Research Interests).
- **Batch C-Z**: Files Created & Linked for 2025 Papers, but detailed enrichment (Bio/Interests) is pending.
