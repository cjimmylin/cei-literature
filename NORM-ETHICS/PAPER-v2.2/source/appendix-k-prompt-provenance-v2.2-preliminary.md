---
title: "Appendix K — Prompt Provenance and System Configuration"
date: 2026-04-13
version: v2.2-preliminary
---

## Appendix K: Prompt Provenance and System Configuration

This appendix documents the system prompts, assessment prompts, and configuration context under which the NormEval trials were conducted. Transparency about prompt provenance is critical because system prompts shape LLM behavior, and undisclosed prompt variation is a confound in any evaluation study.

---

### K.1 System Prompt (Claude Models)

All Claude model trials (Opus, Sonnet, Haiku) were conducted within the Claude Code environment. The primary system prompt that governed Claude's behavior during trial administration is derived from the project's `CLAUDE.md` configuration file.

**Version-controlled configuration:** The sub-project `CLAUDE.md` (at `CEI-Lit-WS/CLAUDE.md`) is tracked in git. The version used during the trial period corresponds to commit `d23eb2463` (2026-02-21), which established the sub-project configuration referencing the root safety rules.

**Provenance gap (disclosure):** The root `CLAUDE.md` file -- which contains the vault-wide safety rules, workflow conventions, and utility paths that frame Claude Code's behavior -- is **NOT tracked in git**. This means the exact system prompt that shaped Opus trial behavior during the Phase 2 trial period cannot be reconstructed with full fidelity from version history. The current version of root `CLAUDE.md` is available in the project repository, but we cannot confirm it is identical to the version in effect during each trial administration.

**Impact assessment:** The root `CLAUDE.md` primarily governs file-safety rules (no deletions, YAML handling), naming conventions, and API rate-limiting behavior. It does not contain benchmark-specific instructions or scoring rubrics. The trial-specific assessment prompts (Section K.2 below) were the primary behavioral drivers during item administration, not the system-level configuration. Nevertheless, we disclose this gap for completeness and recommend that future evaluation studies pin their system prompts in version control before beginning data collection.

---

### K.2 Assessment Prompt Template

Each trial administration used a structured prompt template that presented benchmark items to the model. The template varied by benchmark format (binary, multiple-choice, Likert, free-text) but followed a common structure:

1. **Role specification:** "You are completing a normative ethics assessment. Answer each item according to your genuine moral reasoning, not what you think the 'correct' answer is."
2. **Item presentation:** The benchmark item text, with response format instructions specific to the benchmark.
3. **Output format:** Structured JSON with fields for the response, confidence, and optional reasoning chain.

The full prompt templates for each of the 15 trials are available in the project repository under `NORM-ETHICS/Codex/prompts/`.

---

### K.3 Cross-Vendor Elicitation Prompts

**Critical disclosure:** The non-Anthropic model results were generated through in-context elicitation by a Claude sub-agent, not through direct API calls. The elicitation protocol is documented in `Codex/prompts/protocol.md`, which states: "direct agent reasoning in-session, SDK/API usage: none."

The Codex sub-agent was instructed to reason through each item as the target model, producing structured outputs scaffolded against the parallel Sonnet trial JSONs. This methodology means the non-Anthropic results reflect Claude's model of how GPT-5, GPT-5-mini, and Gemini models would respond -- they are not empirical measurements of those models' actual behavior.

**Implications for replication:** To replicate the cross-vendor findings, researchers must administer the same benchmark items to GPT-5, GPT-5-mini, and Gemini models via their respective APIs (OpenAI and Google). The elicitation-based results presented in this paper serve as falsifiable hypotheses for such replication, not as established findings.

---

### K.4 Recommendations for Future Work

Based on our experience with prompt provenance challenges, we recommend:

1. **Pin all system prompts in version control before trial administration.** Create a frozen snapshot of any configuration file that shapes model behavior during evaluation.
2. **Record the exact model API version, temperature, and system prompt hash** for each trial. Our trials used temperature = 0 throughout, but the system prompt was not hash-verified between sessions.
3. **Distinguish administered from elicited data in all downstream artifacts.** The current paper marks all cross-vendor data with `[simulated -- awaits external validation]` flags; future versions should upgrade these to `[empirical]` once direct API replication is complete.
