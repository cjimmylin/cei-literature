# RP-01 SPECGRADE — Spec Retrieval Provenance (Version Stamps)

**Task:** RP-01 O1 (handoff item 1.6) — clause registries from the two public specs named in `RP-01-SPECGRADE.md`.
**Retrieval date:** 2026-07-09 (all fetches performed today; every registered clause is traceable to a document fetched on this date).
**Retrieved by:** Opus execution session, direct `curl` of raw sources (not model-summarized), converted locally (BeautifulSoup for HTML, PyMuPDF for PDF).

Both source documents are released by their publishers under **Creative Commons CC0 1.0** (public domain) — the brief notes this ("CC0-friendly since sources are"), and both documents self-confirm it.

---

## Spec 1 — OpenAI Model Spec

| Field | Value |
|-------|-------|
| Document title (self-reported) | "Model Spec (2025/12/18)" |
| Version identifier (self-reported) | `2025/12/18` · CHANGELOG tag `v2025.12.18` · footer "December 18, 2025" |
| Canonical/current URL | https://model-spec.openai.com/ (redirects to the dated version below) |
| Fetched URL (dated, canonical snapshot) | https://model-spec.openai.com/2025-12-18.html |
| HTTP status | 200 · 2,636,493 bytes |
| SHA-256 (fetched HTML) | `c53e75cb6770829c79f62bd45788dfbd6bfc9d953cc2206a2e387c942aecf986` |
| License (self-reported) | "dedicated to the public domain and marked with the Creative Commons CC0 1.0 deed" |
| CHANGELOG cross-check | https://github.com/openai/model_spec/blob/main/CHANGELOG.md — top (most recent) entry is `v2025.12.18`; prior: v2025.10.27, v2025.09.12 |

**Currency verification (important):**
- The brief names "OpenAI Model Spec 2025-12-18". This version is **also the current live version** as of 2026-07-09: the canonical root `https://model-spec.openai.com/` issues `content="0; url=2025-12-18.html"` (redirects to it), and the GitHub CHANGELOG's newest entry is `v2025.12.18`. So the brief's pin matches live — **no version drift.**
- ⚠ Observed artifact: the dated HTML page `2025-12-18.html` contains a banner string "A newer version of the Model Spec is available. This version is provided for historical reference and may not reflect current policy." This banner appears to be a static template element carried by dated/archival URLs; it is **contradicted** by the two authoritative currency signals above (root redirect target + CHANGELOG top entry). Registered as-is and flagged. If OpenAI publishes a version after 2025-12-18, re-run O1 against the brief pin AND the new version, and produce the K3 diff-report deliverable.

## Spec 2 — Claude's Constitution

| Field | Value |
|-------|-------|
| Document title (self-reported) | "Claude's Constitution — January 2026" |
| Version identifier (self-reported) | "Published January 21, 2026"; running footer "Claude's Constitution—January 2026" |
| Primary URL | https://www.anthropic.com/constitution |
| Fetched PDF URL (versioned filename) | https://www-cdn.anthropic.com/cffd979fd050fbc0d8874b8c58b24cc10554e208/claudes-constitution_webPDF_26-01.26a.pdf |
| HTTP status | 200 · 1,078,584 bytes · 84 PDF pages · ~23,000 words |
| SHA-256 (fetched PDF) | `7d614cc200155adeeb085c58ae91eee11ac4e180e9ca22329c1868ddfcb0e453` |
| SHA-256 (constitution landing page HTML, also fetched) | `58eb5e143dc14042c2b2b79d28bfade22a8dfbddc5f9c7f1c0d5357272d43c09` |
| Authors (self-reported) | Amanda Askell,* Joe Carlsmith,* Chris Olah, Jared Kaplan, Holden Karnofsky, several Claude models, and many other contributors (*lead authors) |
| License (self-reported) | "in full under a Creative Commons CC0 1.0 Deed" |

**Version notes:**
- The PDF filename token `26-01.26a` decodes as 2026-01, revision "26a" — consistent with the published date of 2026-01-21. This is the most granular version identifier the artifact exposes.
- A second, hash-path PDF URL also exists in Anthropic's CDN (`.../9214f02e.../claudes-constitution.pdf`); the `_webPDF_26-01.26a` filename was chosen as the registered source because it carries an explicit version token. Both were surfaced by search; only the `26-01.26a` PDF was fetched and hashed.
- The document self-describes as "a perpetual work in progress" that "is likely to change in important ways in the future" — K3 (churn) monitoring applies; re-run on any new dated release.

---

## Retrieval method (reproducibility)

```
curl -sL -A "Mozilla/5.0" "https://model-spec.openai.com/2025-12-18.html"  -o modelspec.html
curl -sL -A "Mozilla/5.0" ".../claudes-constitution_webPDF_26-01.26a.pdf"  -o constitution.pdf
# text extraction: BeautifulSoup(get_text) for HTML; PyMuPDF page.get_text() for PDF
# hashes: shasum -a 256
```

Raw fetched artifacts were staged in `/tmp` during extraction (not committed; regenerable from the URLs + hashes above).
