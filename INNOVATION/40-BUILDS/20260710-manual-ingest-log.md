# Manual / Web Ingest Log — Lane B — 2026-07-10

**Source worklist:** `INNOVATION/04-missing-literature.md` — "Non-arXiv / manual ingest" section + the two P1 Anthropic blog entries (G-22, G-16).
**Method:** Live URLs rendered to PDF via Playwright headless-chromium (`page.pdf()`); official PDFs via `curl`; two spec items point at existing SHA-256-stamped registry retrievals (NOT re-fetched). Every fetched PDF opened with PyMuPDF and prose-verified before recording. Evidence class travels with each record.
**Executed:** 2026-07-09 (dated 20260710 per orchestrator naming).
**Validation:** NOT run here (orchestrator runs `validate_all_papers.py` once at end). Local YAML sanity check on all 9 new records: 0 missing required keys, 0 unescaped-quote issues.

---

## Outcome table

| # | Item | Gap | Prio | Outcome | Files produced |
|---|------|-----|------|---------|----------------|
| A1 | Teaching Claude Why (Anthropic blog) | G-22 | P1 | **HIT** | PDF, extract, paper record |
| A2 | Agentic Misalignment (Anthropic blog) | G-16 | P1 | **HIT** | PDF, extract, paper record |
| B1 | Nature — warm models reduce accuracy (Ibrahim) | G-22 | P2 | **HIT** (Open Access) | PDF, extract, paper record |
| B2 | OpenAI Model Spec (2025-12-18) | G-01/02 | P2 | **HIT** (registry-inherited, VERIFIED) | paper record → registry |
| B3 | Claude's Constitution (Jan 2026) | G-22 | P2 | **HIT** (registry-inherited, VERIFIED) | paper record → registry |
| B4 | Anthropic Pilot Sabotage Risk Report | G-16 | P2 | **HIT** | PDF, extract, paper record |
| B5 | Anthropic×OpenAI cross-lab eval exercise | G-16 | P2 | **HIT** | PDF, extract, paper record |
| B6 | Claude Opus 4.5 / 4.6 system cards | G-14 | P2 | **HIT** (both cards) | 2 PDFs, 2 extracts, 2 paper records |

**Totals:** 8 worklist items → 9 paper records (item B6 = two cards). 7 PDFs newly fetched + verified; 2 registry-pointing records. 0 DEFERRED, 0 fabricated.

---

## Per-item detail + verification

### A1 — Teaching Claude Why  **HIT**
- URL: https://www.anthropic.com/research/teaching-claude-why · rendered via Playwright headless-chromium (networkidle, 3s settle).
- **Verification:** PyMuPDF extract = 14 pages, 15,312 chars of real prose. Head reads "Teaching Claude why / May 8, 2026 / Last year, we released a case study on agentic misalignment…"; mid-doc discusses the ~30M/~85M-token synthetic honeypot datasets and the 3M-token "difficult advice" dataset. Confirmed article content, not a bot-wall or empty JS shell.
- Publication year 2026 (dated May 8, 2026) → filed under 2026.
- Files: `Lit-WS-PDFs/2026/2026-Anthropic-Teaching Claude Why.pdf` · `PDF Extracts/2026/2026-Anthropic-Teaching Claude Why.md` · `papers/2026-Anthropic-Teaching Claude Why.md`

### A2 — Agentic Misalignment  **HIT**
- URL: https://www.anthropic.com/research/agentic-misalignment · Playwright render.
- **Verification:** 19 pages, 53,084 chars. Head reads "Agentic misalignment: How LLMs could be insider threats / Jun 20, 2025 … stress-tested 16 leading models…"; mid-doc contains a verbatim blackmail scenario transcript (Claude Sonnet 3.6, `<tool_use:email>` action plan). Real content confirmed.
- Publication year 2025 (dated Jun 20, 2025) → filed under 2025.
- Files: `Lit-WS-PDFs/2025/2025-Anthropic-Agentic Misalignment.pdf` · `PDF Extracts/2025/2025-Anthropic-Agentic Misalignment.md` · `papers/2025-Anthropic-Agentic Misalignment.md`

### B1 — Nature: warm models reduce accuracy (Ibrahim et al.)  **HIT — Open Access**
- URL: https://www.nature.com/articles/s41586-026-10410-0 · Playwright render (cookie banner dismissed).
- **Paywall check:** Page self-labels "Article / Open access". No paywall markers found (no "Access options", "Rent or buy", price strings, "preview of subscription"); full Results/Methods/References prose present (58K chars in <article>). Legitimately accessible → ingested.
- **Verification:** citation_meta → title "Training language models to be warm can reduce accuracy and increase sycophancy", authors Ibrahim/Hafner/Rocher, date 2026/04, DOI 10.1038/s41586-026-10410-0. PDF = 33 pages, 55,457 chars; real prose incl. per-model results (GPT-4o, Llama-70b/8b, Mistral-Small, Qwen-32b).
- First author Ibrahim, year 2026, Nature 652, 1159–1165 (published 29 April 2026).
- Files: `Lit-WS-PDFs/2026/2026-Ibrahim-Warm Models Reduce Accuracy.pdf` · `PDF Extracts/2026/2026-Ibrahim-Warm Models Reduce Accuracy.md` · `papers/2026-Ibrahim-Warm Models Reduce Accuracy.md`

### B2 — OpenAI Model Spec (2025-12-18)  **HIT — registry-inherited, NOT re-fetched**
- Per instructions, NOT re-fetched. Paper record points at the existing SHA-256-stamped retrieval.
- Registry: `INNOVATION/40-BUILDS/rp01-registries/openai-modelspec-2025-12-18-registry.{md,json}` (66-clause registry).
- SHA-256 (fetched HTML): `c53e75cb6770829c79f62bd45788dfbd6bfc9d953cc2206a2e387c942aecf986` · Fetched URL: https://model-spec.openai.com/2025-12-18.html · Retrieval date 2026-07-09 · License CC0 1.0.
- Evidence class **VERIFIED (inherited from registry)**. Record carries `registry_source`, `registry_sha256`, `registry_fetched_url`, `registry_retrieval_date`, `evidence_class` fields; `local_pdf`/`pdf_extract` point at the registry .md (no separate PDF, by design).
- File: `papers/2025-OpenAI-Model Spec.md`

### B3 — Claude's Constitution (January 2026)  **HIT — registry-inherited, NOT re-fetched**
- NOT re-fetched. Points at existing retrieval.
- Registry: `INNOVATION/40-BUILDS/rp01-registries/claude-constitution-2026-01-registry.{md,json}` (49-clause registry).
- SHA-256 (fetched PDF): `7d614cc200155adeeb085c58ae91eee11ac4e180e9ca22329c1868ddfcb0e453` · Fetched URL: `.../claudes-constitution_webPDF_26-01.26a.pdf` (84 pp, ~23k words) · Retrieval date 2026-07-09 · License CC0 1.0. Landing-page HTML SHA-256 also recorded in registry.
- Evidence class **VERIFIED (inherited from registry)**.
- File: `papers/2026-Anthropic-Claudes Constitution.md`

### B4 — Anthropic Pilot Sabotage Risk Report  **HIT**
- Discovery: alignment.anthropic.com index → article URL https://alignment.anthropic.com/2025/sabotage-risk-report/ · Playwright render.
- **Verification:** 3 pages, 6,182 chars. Short but complete blog article: "Anthropic's Pilot Sabotage Risk Report / … / October 28, 2025 / Samuel R. Bowman, Misha Wagner, Fabien Roger, and Holden Karnofsky"; body discusses the RSP affirmative-case pilot and the "very low but not fully negligible" conclusion. Real content (concise article, not truncated JS shell).
- Files: `Lit-WS-PDFs/2025/2025-Anthropic-Pilot Sabotage Risk Report.pdf` · `PDF Extracts/2025/2025-Anthropic-Pilot Sabotage Risk Report.md` · `papers/2025-Anthropic-Pilot Sabotage Risk Report.md`

### B5 — Anthropic×OpenAI cross-lab eval exercise  **HIT**
- URL: https://alignment.anthropic.com/2025/openai-findings/ · Playwright render.
- **Verification:** 34 pages, 63,402 chars. Head: "Findings from a Pilot Anthropic—OpenAI Alignment Evaluation Exercise / August 27, 2025 / Samuel R. Bowman, Megha Srivastava, Jon Kutasov, Rowan Wang, Trenton Bricken, Benjamin Wright, Ethan Perez, and Nicholas Carlini". Real content confirmed.
- Files: `Lit-WS-PDFs/2025/2025-Anthropic-Cross-Lab Alignment Evaluation.pdf` · `PDF Extracts/2025/2025-Anthropic-Cross-Lab Alignment Evaluation.md` · `papers/2025-Anthropic-Cross-Lab Alignment Evaluation.md`

### B6 — Claude Opus 4.5 / 4.6 system cards  **HIT — both**
- Discovery: Anthropic Transparency Hub (https://www.anthropic.com/transparency) enumerated the official system-card PDFs. The list named "Opus 4.5 / 4.6" specifically (NOT the 4.7 / Sonnet 4.6 / Fable-Mythos cards also present) — both exact cards located and downloaded via `curl`.
- **Opus 4.5:** https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf → 153 pp, 261,715 chars, head "System Card: Claude Opus 4.5 / November 2025"; contains evaluation-awareness content. Filed 2025.
- **Opus 4.6:** https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf → 213 pp, 367,781 chars, head "System Card: Claude Opus 4.6 / February 2026"; contains evaluation-awareness content. Filed 2026.
- Files: `Lit-WS-PDFs/2025/2025-Anthropic-Claude Opus 4.5 System Card.pdf` · `Lit-WS-PDFs/2026/2026-Anthropic-Claude Opus 4.6 System Card.pdf` · extracts under `PDF Extracts/2025/` and `PDF Extracts/2026/` · records `papers/2025-Anthropic-Claude Opus 4.5 System Card.md`, `papers/2026-Anthropic-Claude Opus 4.6 System Card.md`.

---

## Notes / anomalies

- **No DEFERRALS.** The two potentially-blocked items both resolved: the Nature paper is genuinely Open Access (full text, no paywall), and both Opus system cards are official public PDFs. Nothing was fabricated.
- **List had 8 non-blog manual items but item B6 spans 2 cards** → 9 paper records total from this lane (2 blog + 7).
- **Blog PDFs are print-rendered from live HTML**, so they carry site chrome (nav, footer) captured in the extract; the article prose is intact and dominant. Verified per-item by head+mid text sampling.
- **Model-spec / constitution records deliberately have no separate PDF under `Lit-WS-PDFs/`** — their `local_pdf`/`pdf_extract` point at the RP-01 registry `.md` files, matching the "point at registry copies" instruction. If a downstream tool expects `local_pdf` under `Lit-WS-PDFs/`, that is intentional divergence for these two registry-inherited records.
- All new records use `DATE_ADDED: 20260710`, v1.5 `ethics_perspective`/`newtags` dual-homed codes, and an `innovation_gap` field. Fetched records additionally carry `evidence_class: "VERIFIED (Playwright/curl-fetched PDF, prose-verified 2026-07-09)"`; registry records carry the full `registry_*` provenance block + `evidence_class: "VERIFIED (inherited from registry, SHA-256-stamped)"`.
- Ephemeral probe PDFs (other system cards fetched only to identify titles: Opus 4.7, Sonnet 4.6, Fable/Mythos 5, Mythos Preview) were left in `/tmp` and NOT ingested (out of scope).
