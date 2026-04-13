---
title: "Mapping the Normative Ethics Benchmark Landscape"
subtitle: "Data Availability Statement"
date: 2026-04-13
---

## Data Availability

All artifacts associated with this paper are openly released to support replication, extension, and re-analysis.

**Interactive Dashboards.** Four deployed dashboards present the feature matrix, composite scoring, trial results, and cross-vendor analysis at progressively refined levels of UX and accessibility:

- v1 (original 9-tab interface): https://cjimmylin.github.io/cei-normeval-dashboard/
- v2 (UX-improved, accessible, print-ready): https://cjimmylin.github.io/cei-normeval-dashboard-v2/
- v3 (feature reference table + scoring equation): https://cjimmylin.github.io/cei-normeval-dashboard-v3/
- v4 (cold-readable with Guide tab, glossary, framework explainer, and preliminary-data disclosures): https://cjimmylin.github.io/cei-normeval-dashboard-v4/

**Persistent Deposit.** The complete 54-benchmark × 41-feature matrix, all trial data (both administered and elicited — see §3 and §6.1 for methodology distinctions), composite scoring scripts, and prompt templates (Appendix K) are deposited at Zenodo: [DOI pending — will be inserted before submission].

**License.** Code and analysis scripts are released under MIT License. Data artifacts (feature matrix, trial outputs, dashboards) are released under Creative Commons Attribution 4.0 International (CC-BY-4.0). Third-party benchmark items remain under their original licenses; we redistribute only summary statistics and item-level scores, not source items.

**Reproducibility note.** Trials administered to Claude models (Opus, Sonnet, Haiku) used Anthropic's API; cross-vendor results presented in the current draft were generated via in-context elicitation by a Codex sub-agent and are documented separately in the project's `Codex/` directory (see also §6.1 limitations and Appendix J council deliberation). External replication using non-Anthropic APIs is planned but not yet complete.

**Contact.** Inquiries and collaboration requests may be directed to the corresponding author via the GitHub issue tracker linked in the dashboard footer.
