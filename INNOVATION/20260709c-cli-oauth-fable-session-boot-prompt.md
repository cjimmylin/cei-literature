# CLI-OAuth Bring-Up — Fable Session Boot Prompt

**Written:** 2026-07-09 (INNOVATION Fable session, after discovering all three vendor CLIs are OAuth-authenticated on this machine). **Use with:** a fresh **Fable** session (`/clear` first); window closes ~2026-07-11. This session OUTRANKS the Governance Symphony session (`CEI-AI-Statements/GENERATION3/20260709-fable-session-boot-prompt.md`) per the exit-sequencing memo's credentials-land rule; do Governance Symphony in the following Fable session if the window allows. Paste the block below verbatim.

---

This is a Fable-tier session: codify a vault-wide provisional ruling on CLI-OAuth model access, drive the bring-up down-tier, and adjudicate the first real-token results in-session. Working home: `CEI-Lit-WS/INNOVATION/` (this is Cycle-2 runner prep, item 2.1-provisional). Fable stays in the main loop for rulings; all building/running goes to Opus/Sonnet agents with explicit `model=`.

**Verified facts (2026-07-09, this machine):** `claude` 2.1.183 (subscription-authenticated), `codex` CLI 0.134.0 with `~/.codex/auth.json`, `gemini` CLI 0.41.2 with `~/.gemini/oauth_creds.json`. Three model families reachable without API keys. No central runner exists in the vault; only the Anthropic SDK is installed, no `.env`.

**Task 1 — Codify the provisional-path ruling (Fable, main loop, first).** New dated memo `INNOVATION/20260709<x>-cli-oauth-provisional-ruling.md` establishing, vault-wide:
- **GREEN (allowed now):** harness/runner integration tests with real tokens; small calibration probes (tens of calls); machinery-validation re-scoring of already-synthetic corpora. All outputs carry provenance class `cli-oauth-provisional` and may NEVER stand in for API measurements.
- **YELLOW (allowed with conditions):** judge-family pilots (judging = scoring transcripts; harness contamination is lower than subject-side). Conditions: 3-family roster (Agent SDK / codex exec / gemini CLI), full transcript logging, results labeled provisional, mandatory API replication before anything publishes or feeds a frozen verdict.
- **RED (still blocked):** all pre-registered subject-side headline runs. CLIs inject their own system prompts, expose no temperature/seed control, and can't match pre-registered rosters (e.g., DUPLEX P0's 5-of-9). These wait for API keys or an explicit Jimmy re-registration. Standing project rulings are NOT overridden: THORNS live-mode hard-block (D-37) holds until spine fixes S-1/S-2 land; SERMONMOUNT live P1 waits on MF-1…MF-8; DUPLEX P0 roster stands.
- ToS note to include honestly: Agent SDK under subscription is the sanctioned Anthropic path; Codex CLI under a ChatGPT plan is its intended auth; bulk benchmark use through consumer CLIs is gray — keep volumes pilot-scale and flag the D6-style question (external claims from provisional data = never) for Jimmy.

**Task 2 — Build the shim (Opus agent, EXECUTION mode).** `INNOVATION/40-BUILDS/t1-runner-provisional/`: one vendor-agnostic Python interface with three CLI-OAuth backends (Anthropic via Agent SDK headless / `claude -p`; OpenAI via `codex exec`; Google via `gemini` non-interactive), full request/response transcript logging (JSONL), exponential backoff, per-call provenance stamping (`cli-oauth-provisional`, CLI version, model id as reported). Design it as a *backend* behind the Cycle-2 T1 runner interface so the API backends drop in later with zero caller changes. Tests with real tokens = GREEN. Agent must verify each CLI's headless invocation empirically and document exact flags used.

**Task 3 — GREEN smoke + YELLOW pilot (agents run, Fable adjudicates).**
- Smoke: ~10 generic items through all three families; confirm parsing, refusals handling, logging.
- Pilot: 3-family judge re-scoring of a stratified sample (~50–100 records) from the RP-04 S1 machinery lane (`INNOVATION/40-BUILDS/rp04-corpus/frozen/witness/scored.jsonl` — synthetic-mock subjects, so this validates the re-scoring machinery per the rescoring matrix, it is NOT a judge-bias measurement). Deliverable: dated machinery-validation report with judge-agreement stats, provenance headline, and an explicit "what this does and does not show" section.

**Task 4 — Fable adjudication of live results (main loop).** Rule on: shim GO/NO-GO as the provisional T1 backend; whether judge-agreement machinery behaves well enough to green-light the YELLOW RP-04 judge pilot design; any surprises → PENDING-RULINGS if Jimmy-tier. Update `07-opus-handoff.md` (2.1 provisional progress), decision log, FABLE-WEEK.

Hard rules: tiering per `~/.claude/CLAUDE.md`; no `rm` (RECYCLE-BIN); report immutability (new dated files); synthetic/mock provenance travels with every artifact; `git log -1` + `git diff --cached --name-only` before committing and use pathspec-limited commits (`git commit -- <files>`) — parallel sessions share this index and swept files twice on 2026-07-09. End of session: dated handoff, commit + push.

---

**Why this prompt exists:** the vault's Cycle-2/live gates all assumed API keys. On 2026-07-09 all three vendor CLIs were found OAuth-authenticated locally, making a provisional three-family path available in-window. The exit-sequencing memo says credentials landing in-window makes live-result adjudication the best remaining Fable use; this session is that, with the ruling codified first so post-window Opus sessions inherit clean boundaries.
