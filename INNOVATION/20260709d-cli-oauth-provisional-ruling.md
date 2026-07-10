# CLI-OAuth Provisional Ruling — Vault-Wide

**Date:** 2026-07-09 · **Author:** Fable session (CLI-OAuth bring-up, Cycle-2 item 2.1-provisional)
**Status:** PROVISIONAL ruling, Fable-tier, in-window. Binding on all vault sessions until API keys land or Jimmy amends it. Two items inside it are Jimmy-tier and are queued as PR-02 in `INNOVATION/PENDING-RULINGS.md` — this ruling does NOT self-approve them.
**Scope:** every CEI vault project (INNOVATION, COOKBOOK/BIBLEBENCH families, FRUITBENCH, SERMONMOUNT, CORINTHLOVE, WCF-Bench, WALKWORTHY, DUPLEX, and any future bench).

---

## 1. What changed

Verified 2026-07-09 on this machine: three vendor CLIs are OAuth-authenticated without any API key —

| Family | CLI | Version | Auth artifact |
|---|---|---|---|
| Anthropic | `claude` | 2.1.183 | subscription login |
| OpenAI | `codex` | 0.134.0 | `~/.codex/auth.json` |
| Google | `gemini` | 0.41.2 | `~/.gemini/oauth_creds.json` |

Every Cycle-2 / live-run gate in the vault assumed API keys. The CLIs are **credentials, provisionally** — real tokens from real frontier models — but they are *not* equivalent to API access, and this ruling exists to keep that distinction from eroding.

## 2. Why CLI-OAuth output is a distinct provenance class

CLI completions differ from API completions in ways that are fatal for pre-registered measurement but harmless for plumbing:

1. **Injected system prompts.** Each CLI wraps the request in its own (version-dependent, undocumented) system prompt. Subject-side behavior measured through a CLI is behavior of *model + vendor scaffold*, not the model.
2. **No sampling control.** No temperature/seed/top-p exposure → no reproducibility contract, no test-retest design.
3. **Roster mismatch.** CLIs expose whatever model the vendor routes to, not the pre-registered model IDs (e.g., DUPLEX P0's 5-of-9 roster cannot be matched).
4. **Version drift.** CLI auto-updates can silently change the scaffold mid-study.

**New provenance class (extends the RP-04 manifest vocabulary):**

> `cli-oauth-provisional` — real-model completion obtained through a subscription/OAuth CLI (injected vendor scaffold, no sampling control, model id as self-reported). May validate machinery and pilot designs. May NEVER stand in for an API measurement, enter a frozen verdict, or be published as model behavior without API replication.

Every artifact touched by CLI-OAuth output carries this class in its manifest/frontmatter, alongside CLI name + version and the model id as reported in the response. Provenance travels with derived artifacts (the `derived-synthetic` precedent applies: aggregates of provisional data are provisional).

## 3. The lanes

### GREEN — allowed now, no further approval

- **Harness/runner integration tests with real tokens** (the T1 provisional shim and its successors).
- **Small calibration probes** — tens of calls, to check parsing, refusal handling, format compliance.
- **Machinery-validation re-scoring of already-synthetic corpora** (e.g., the RP-04 S1 lane): the judge pipeline runs against synthetic-mock records to prove it recovers injected labels. Per the rescoring matrix §3, this is a plumbing test; no number from it is ever reported as bias, agreement-with-truth, or model behavior.

GREEN conditions: full JSONL transcript logging; `cli-oauth-provisional` stamping; pilot-scale volumes (see §5).

### YELLOW — allowed with conditions

- **Judge-family pilots.** Judging = scoring transcripts; the CLI scaffold contaminates the *judge's* context, not the subject's behavior, so the risk is lower — but not zero (an injected scaffold can shift judge severity).
- Conditions, all mandatory:
  1. **3-family roster:** Anthropic (Agent SDK headless / `claude -p`), OpenAI (`codex exec`), Google (`gemini` non-interactive).
  2. **Full transcript logging** of every judge call (request + response, JSONL).
  3. Results **labeled provisional** in every table, figure, and headline.
  4. **Mandatory API replication** before any result publishes, feeds a frozen verdict, or is cited by another project as established.
  5. Anti-leakage discipline from the rescoring matrix stands: generator ≠ judge within a family; judges blind to each other.

### RED — still blocked

- **All pre-registered subject-side headline runs.** No CLI-OAuth completion may serve as subject-model behavior in any pre-registered design. Reasons in §2 (scaffold injection, no sampling control, roster mismatch). These runs wait for API keys **or an explicit Jimmy re-registration** that re-specifies the measurement around CLI constraints.
- **Standing project rulings are NOT overridden by this ruling:**
  - THORNS live-mode hard-block (D-37) holds until spine fixes S-1/S-2 land — code-gated, not key-gated.
  - SERMONMOUNT live P1 waits on MF-1…MF-8 fixes and its pre-registered rubric (G1–G5).
  - DUPLEX P0's 5-of-9 roster and adjudication protocol stand as written.
  - All v1.x scope locks (no preprints, no human raters, no ICC, no venue/author/OSF) stand.

## 4. Terms-of-service note (honest version)

- **Anthropic:** headless `claude -p` / Agent SDK under a subscription is the sanctioned path for programmatic use of that subscription.
- **OpenAI:** `codex exec` under a ChatGPT plan is that CLI's intended auth mode.
- **Google:** `gemini` CLI OAuth is the intended individual-developer path, with published free-tier quotas.
- **The gray zone:** none of these consumer paths is marketed for *bulk benchmark evaluation*. This ruling therefore caps volumes at pilot scale (§5) and treats the consumer CLIs as bring-up credentials, not production measurement infrastructure.
- **D6-style line (never crossed):** no external claim — paper, preprint, blog, README badge, cross-project "established finding" — is ever made from `cli-oauth-provisional` data. Whether even *internal* frozen verdicts may cite provisional judge pilots pre-replication, and whether Jimmy is comfortable with the ToS posture at all, are Jimmy-tier → **PR-02**.

## 5. Volume caps (pilot scale, binding)

- Per session: ≤ ~500 calls per family; per artifact/study: ≤ ~300 calls per family.
- Exponential backoff on rate-limit signals from call one; overnight/unattended bulk loops are out of scope for this ruling.
- Anything larger is a new ruling (Jimmy or a future Fable window).

## 6. Review / expiry

- This ruling is superseded automatically, lane by lane, the moment API keys land: GREEN/YELLOW work re-runs or replicates under API provenance; RED unlocks per each project's own gates.
- If Jimmy rules on PR-02, that ruling amends §4.
- Post-window Opus sessions inherit this ruling as binding and may not widen any lane (succession-protocol PROVISIONAL rule: interim paths may narrow, never widen, above-tier surfaces).

## 7. Immediate applications authorized by this ruling

1. **T1 provisional shim** (`INNOVATION/40-BUILDS/t1-runner-provisional/`) — GREEN: build + integration-test with real tokens across all three families.
2. **Smoke probe** — GREEN: ~10 generic items × 3 families; parsing/refusal/logging checks.
3. **RP-04 S1 judge machinery pilot** — GREEN core (machinery validation on synthetic-mock WITNESS records) executed with the YELLOW roster discipline as a dress rehearsal; deliverable is a dated machinery-validation report whose headline states what it does and does not show (rescoring matrix §0 language: *we froze stimuli and validated machinery — nothing here is a judge-bias measurement*).
