# Stage-4 `research_topic` Vocabulary Reconciliation Proposal

**Generated:** 2026-07-10
**Lane:** D2 (parallel session — proposal only; NO edits to standards or papers)
**Handoff item:** 3.5 (`INNOVATION/07-opus-handoff.md`, added 2026-07-09 per Fable FC-2)
**Status:** PROPOSAL — for Jimmy sign-off, to be queued as **PR-03** (standards change requires his approval)
**Inputs:**
- Fresh inventory: `INNOVATION/20260710-stage4-vocab-inventory.md` (Lane D1, 2026-07-10)
- Standard under reconciliation: `_OPERATING-SYSTEM/Standards/classification-logic.md` (v1.5 in history table, header still "1.0")
- Deferred Patch D context: `INNOVATION/20260709-taxonomy-stage4-codes-proposal.md` §9.2 + §7 Patch D
- Live emitter (ground truth): `PYTHON/classify_non_ethics_topics.py`

---

## 0. The reframing finding (read this first)

The inventory framed this as "documented list vs. live usage out of sync." Reading the **live classifier** (`PYTHON/classify_non_ethics_topics.py`, `TOPIC_CATEGORIES` dict, lines 28–77) changes the picture materially:

**The undocumented live codes are not drift or manual overrides — the shipping script emits them by design.** Its `TOPIC_CATEGORIES` dict contains exactly these 12 keys, plus `"Other"` as the hard-coded fallback (line 120):

```
AI Safety & Alignment · Truthfulness & Factuality · Bias & Fairness ·
Interpretability & Explainability · Question Answering · Machine Translation ·
Dialogue Systems · Computer Vision & Multimodal · Social & Cultural Analysis ·
NLP & Representation Learning · Machine Learning        (+ "Other" fallback)
```

Consequences that reframe the whole task:

1. **The standard is the stale artifact, not the data.** The documented Stage-4 list (12 codes) and the code-emitted list (12 codes + Other) are *two different sets of twelve*. The standard's list was expanded on 2026-07-09 (PR-01, v1.5) with 5 alignment codes (Specification & Compliance, Scalable Oversight, Preference Aggregation & Social Choice, Value Formation & Emergent Misalignment, Multi-Agent Value Dynamics) **that the classifier does not emit** — hence all 5 show 0 live usage. Meanwhile 5 codes the classifier *does* emit (Interpretability & Explainability, Dialogue Systems, Computer Vision & Multimodal, Social & Cultural Analysis, Truthfulness & Factuality, Bias & Fairness) are absent or Stage-3-only in the standard.
2. **The "Stage-3-codes-in-Stage-4-fields" anomaly is not a routing bug.** `Truthfulness & Factuality` (32), `Bias & Fairness` (12) appear in `research_topic` because they are **first-class keys in the Stage-4 classifier's dict**, and are additionally *priority-boosted* (lines 122–125: "AI Safety & Alignment / Truthfulness & Factuality / Bias & Fairness … prioritize them because they are core to the vault's purpose"). They are deliberate Stage-4 outputs that happen to share a name with Stage-3 codes. (`Machine Ethics`=2 is the one true anomaly — it is *not* a classifier key; see §5.)
3. **"Computer Vision" vs "Computer Vision & Multimodal" is a standard-side typo, not data drift.** The classifier only ever emits `Computer Vision & Multimodal` (line 58). The standard's bare `Computer Vision` (line 320) has never been reachable. No paper needs relabeling; the *standard* needs the "& Multimodal" suffix.

This flips the default remedy from "migrate the papers to match the standard" toward "**document the code-emitted reality, then prune genuinely dead entries**." Migration over `papers/` is largely *unnecessary* and, given the vault's YAML-batch hazard history, should be minimized.

---

## 1. Problem statement (grounded in the fresh inventory)

Per `INNOVATION/20260710-stage4-vocab-inventory.md`:

- **958** papers carry `research_topic`; **1,427** do not (field is populated only for `ethics_overall < 50` papers by design — see §4d).
- **24** distinct live values. **16** are undocumented in the standard. **13** documented codes have **0** live usage — including **all 5** new v1.5 alignment codes and **"Benchmarks & Datasets"**.
- Largest undocumented buckets: **Other = 182**, **Social & Cultural Analysis = 89**, **Computer Vision & Multimodal = 31**, **Dialogue Systems = 11**, **Interpretability & Explainability = 5**, **LLM Moral Reasoning = 5**.
- **9 singletons** (GAMA Moral Agent, SPECTRA Ethical Framework, Socratic AI Ethics, …) are per-paper ad-hoc labels the classifier never emits — manual/legacy overrides on ethics-adjacent papers.
- Header staleness: `classification-logic.md` line 3 reads `**Version:** 1.0` while the Version History table (line 863) runs through **1.5** — the deferred **Patch D**, approved in principle and gated to this reconciliation.

The standard cannot be used as the authoritative Stage-4 vocabulary today: it neither describes what the pipeline produces nor what the corpus contains. Any downstream artifact (dashboards, stats, the position paper) that trusts the documented list will misrepresent the vault.

---

## 2. Three options (each fully specified)

### Option A — Document-the-live-set

Bring the standard's Stage-4 category list into exact agreement with `classify_non_ethics_topics.py`'s `TOPIC_CATEGORIES` (12 keys) **plus** a formally-defined `Other` escape-hatch. Add the 6 code-emitted-but-undocumented codes (Interpretability & Explainability, Dialogue Systems, Computer Vision & Multimodal, Social & Cultural Analysis, Truthfulness & Factuality, Bias & Fairness); rename the standard's `Computer Vision` → `Computer Vision & Multimodal`; define `Other`; annotate that Truthfulness & Factuality / Bias & Fairness are intentionally dual-homed with Stage 3 (like the existing AI Safety & Alignment precedent).

- **Touches:** the standard only. **Zero** paper files.
- **Leaves the 5 v1.5 codes** in the documented list (they are correct *aspirations* — they'll populate once the alignment-code classifier logic is wired; see the acquisition track item 1.2). Mark them "(defined; not yet emitted by the current classifier)."
- **Does not resolve** the 9 singleton ad-hoc labels or `LLM Moral Reasoning` (5) — those are *not* classifier output; they're legacy manual tags. Option A can note them as "non-canonical legacy values, out of pipeline scope."

### Option B — Merge-and-migrate

Map near-duplicate and off-taxonomy live values onto canonical codes and **rewrite the affected paper files**. Candidate mappings (only where semantically safe):

| Live value | Papers | → Canonical target | Safe? |
|---|---|---|---|
| `LLM Moral Reasoning` | 5 | → `Moral Reasoning & Psychology` (Stage-3) *or* leave as ethics-routing repair | borderline — these scored `< 50` but are moral; a re-*route* (Stage 3), not a rename |
| 9 singletons | 9 | → `Other`, or re-route to Stage 3 | each is a judgment call |
| `Machine Ethics` (Stage-4 pos.) | 2 | → re-route to Stage 3 `Machine Ethics` | true anomaly; 2 files |
| `Computer Vision & Multimodal` | 31 | (no migration — fix the *standard* instead) | — |

Note there is **no large clean near-duplicate cluster** to merge: the only exact variant ("Computer Vision" vs "…& Multimodal") is resolved standard-side, not by touching papers. So Option B in practice touches **≤ 16 files** (5 + 9 + 2) and every one is a *content re-routing decision*, not a mechanical rename.

- **Touches:** ≤ 16 paper files + the standard.
- **Requires** a migration script over `papers/` (see §6 sketch) using the mandatory `re.subn` line-pattern.
- **Highest risk** relative to payoff: it edits paper YAML (the vault's known hazard) to fix ≤ 16 files, several of which are genuinely ambiguous (should a `< 50`-scored moral-reasoning paper be re-scored, or just relabeled?). Re-routing is arguably a *re-classification* job for the pipeline, not a vocabulary patch.

### Option C — Deprecate-unused

Remove the 13 documented-but-unused codes from the standard's Stage-4 list to eliminate dead vocabulary:

- `Benchmarks & Datasets` (0 live) — genuinely dead; the classifier folds "benchmark"/"dataset" keywords into `Machine Learning` (line 75), and data-nature is captured separately in Stage 7. **Safe to drop.**
- `Computer Vision` (0 live) — dead label; superseded by the "& Multimodal" variant. **Drop (subsumed by rename in A).**
- The 5 v1.5 alignment codes (0 live) — **do NOT drop.** They were ratified 2026-07-09 (PR-01) as forward vocabulary for the acquisition corpus; 0 usage is expected because their classifier logic isn't wired yet. Dropping them would re-litigate a signed decision.
- The Stage-3-only codes listed as unused (Human Rights & Social Justice, Privacy & Surveillance, etc.) are **not Stage-4 entries** — they're out of scope for a Stage-4 reconciliation.

So Option C's *safe* deletions reduce to exactly **2 dead Stage-4 codes** (`Benchmarks & Datasets`, `Computer Vision`), and `Computer Vision`'s removal is really a rename handled by A.

- **Touches:** the standard only. **Zero** paper files.
- **Net effect standalone:** drop `Benchmarks & Datasets`. Minimal on its own.

### Hybrid (recommended shape)

**A + C, no B.** Document the live set (A) — which includes renaming `Computer Vision` → `Computer Vision & Multimodal` and defining `Other` — while dropping the one genuinely dead code (`Benchmarks & Datasets`, C) and *retaining* the 5 v1.5 forward codes with an explicit "not-yet-emitted" annotation. **Skip B**: the ≤ 16 files it would touch are re-classification judgment calls, not vocabulary reconciliation, and are better handled by a future targeted Stage-3 re-route pass — not a YAML batch edit inside a standards-sync task.

---

## 3. Migration cost per option

| Option | Paper files touched | Script needed | Script complexity | Risk (YAML-batch hazard) | Validation burden |
|---|---|---|---|---|---|
| **A** Document-live | **0** | none | n/a | **None** (no paper edits) | Re-read standard; grep live values ⊆ documented set. ~10 min. |
| **B** Merge-migrate | **≤ 16** | yes, `re.subn` line-pattern (mandatory) | Moderate — but each edit is a *content decision*, so mostly manual review, not batch | **HIGH per-file, LOW volume.** Any paper-YAML batch edit is the vault's known hazard (Rule 2); re-routing also risks orphaned `ethics_perspective`/`newtags` inconsistency (Stage-3 vs Stage-4 fields must stay coherent). | Full `validate_all_papers.py` + `validate_papers_enhanced.py` + newtags re-aggregation + git-diff review of every touched file. ~1–2 hr. |
| **C** Deprecate | **0** | none | n/a | **None** (no paper edits). *Behavioral* risk only: don't drop the 5 forward codes. | Re-read standard. ~5 min. |
| **A+C hybrid** | **0** | none | n/a | **None** | Grep-verify live set ⊆ documented set + spot-check header/history rows. ~15 min. |

**Key point:** Options A, C, and the hybrid touch **zero paper files** and need **no migration script at all** — they are pure standards edits. Only Option B incurs the YAML-batch hazard, and it does so to fix ≤ 16 files that are arguably out of scope. The safe-migration `re.subn` line-pattern is mandated *if* B is ever run (script in §6, marked DO-NOT-RUN).

---

## 4. Anomalies handled explicitly

**(a) Stage-3 codes appearing in Stage-4 fields.** Not a routing bug. `Truthfulness & Factuality` (32) and `Bias & Fairness` (12) are **first-class keys in the Stage-4 classifier and priority-boosted** (`classify_non_ethics_topics.py` lines 122–125). They are correct Stage-4 outputs for `ethics_overall < 50` papers that nonetheless contain those keywords. **Resolution:** the standard should *document* them as legitimate dual-homed Stage-4 codes (mirroring the existing `AI Safety & Alignment` dual-home), not "fix" the data. The lone true anomaly is `Machine Ethics` (2 papers): it is **not** a classifier key, so those 2 tags are legacy/manual. Flag for a future Stage-3 re-route review; do not batch-edit them in this task.

**(b) "Other" = 182.** This is the classifier's hard-coded fallback (line 120) when no category keyword matches — 182/958 ≈ 19% of classified papers. It is a *real, expected* pipeline output, not corruption. **Resolution:** formally document `Other` in the standard as the defined escape-hatch ("no Stage-4 category keyword matched; candidate for keyword-list tuning or manual review"). Do **not** attempt to redistribute the 182 in this task — that is a classifier-tuning / manual-review effort, not a vocabulary reconciliation, and would require re-running Stage 4 (owns the acquisition/re-classification track, not 3.5). Noted in-scope; fix out-of-scope.

**(c) "Computer Vision" vs "Computer Vision & Multimodal."** Standard-side label error. The classifier only emits `Computer Vision & Multimodal` (line 58); the standard's bare `Computer Vision` (line 320) is unreachable and has 0 live usage. **Resolution:** rename in the standard (Patch, §6). **Zero papers** touched.

**(d) 1,427 papers missing `research_topic`.** In-scope to note; **out-of-scope to fix here.** `research_topic` is populated *only* for `ethics_overall < 50` papers (standard line 306; classifier docstring). The 1,427 are overwhelmingly ethics-relevant papers (`≥ 50`) that correctly route to Stage 3 and legitimately have no Stage-4 topic. This is by design, not a gap. (A residual few may be pre-pipeline imports; verifying that is a coverage audit, not a vocabulary task.) **No action in PR-03.**

---

## 5. Recommendation

**Adopt the A+C hybrid: document the code-emitted live vocabulary and drop the single genuinely-dead code — a standards-only change, zero paper edits, zero migration script. Explicitly decline Option B.**

Rationale:

1. **The data is right; the standard is stale.** The undocumented live codes are deliberate classifier output, so the correct move is to make the standard describe reality, not to rewrite 958 papers to match an aspirational list.
2. **Zero YAML-batch risk.** A+C touches no paper files, so it entirely avoids the vault's documented failure mode (Session-7-class YAML corruption). This is the decisive safety argument.
3. **Option B's payoff is tiny and its scope is wrong.** It would edit ≤ 16 files, each a re-classification judgment call (re-route to Stage 3? re-score?), to marginal benefit. That work belongs to a future Stage-3 re-route / classifier-tuning pass with its own review, not to a vocabulary-sync PR.
4. **Preserve the signed decision.** The 5 v1.5 codes stay (0 usage is expected pre-wiring); dropping them would re-open PR-01. Annotate them "not yet emitted."
5. **Fold in Patch D now.** This reconciliation is exactly the gated moment to fix the `Version: 1.0` header staleness and record the change in the history table.

Residual follow-ups (explicitly NOT part of PR-03, logged for later): redistribute/tune the `Other` bucket (182); re-route the 2 `Machine Ethics` + 9 singleton legacy tags via a Stage-3 pass; wire classifier logic for the 5 v1.5 codes.

---

## 6. Ready-to-apply patch (recommended option A+C, Patch D folded in)

**PRESENTED, NOT APPLIED.** These are exact edits to `_OPERATING-SYSTEM/Standards/classification-logic.md`. Jimmy signs off → queued as **PR-03**. Line numbers per the file as read on 2026-07-10.

### Patch 1 — Header version bump (folds in deferred Patch D)

**Find (line 3):**
```
**Version:** 1.0
```
**Replace with:**
```
**Version:** 1.6
```
*(1.6, not 1.5: the v1.5 row already exists in the history table from PR-01; this reconciliation is the next increment. If Jimmy prefers to treat the header bump as merely catching up to 1.5 and add 1.6 in the same row, note it — but a distinct row is cleaner.)*

### Patch 2 — Replace the Stage-4 category list

**Find (lines 314–327, the "### Categories" block under "## Stage 4: Research Topic (Non-Ethics)"):**
```
### Categories

1. **Machine Learning** - General ML/DL papers
2. **NLP & Representation Learning** - Embeddings, parsing, language models
3. **Question Answering** - QA-specific systems
4. **Machine Translation** - Translation systems
5. **Computer Vision** - Image/video processing
6. **Benchmarks & Datasets** - Data contributions without ethical focus
7. **AI Safety & Alignment** - Catch-all for technical safety papers missed by Stage 1
8. **Specification & Compliance** - Model specs, constitutions, spec-adherence auditing (gap atlas G-01/02/03)
9. **Scalable Oversight** - Weak-to-strong, debate, recursive critique, no-gold-truth evaluation, judge reliability (G-07/08/09)
10. **Preference Aggregation & Social Choice** - Preference aggregation, collective/pluralistic alignment, deliberation pipelines (G-10/11/12)
11. **Value Formation & Emergent Misalignment** - Emergent misalignment, persona geometry, value drift in training, coherent-values adjudication (G-20/21/22/23)
12. **Multi-Agent Value Dynamics** - Agentic value dynamics, multi-agent alignment, value persistence/drift over operation (G-16/17/18/19)
```
**Replace with:**
```
### Categories

The canonical Stage-4 vocabulary is the set of keys emitted by
`PYTHON/classify_non_ethics_topics.py` (`TOPIC_CATEGORIES`), plus the `Other`
fallback. Codes are listed in the classifier's priority order.

**Currently emitted by the classifier (live vocabulary):**

1. **AI Safety & Alignment** - Catch-all for technical safety papers missed by Stage 1 (constitutional AI, robustness, red teaming, jailbreak). *Dual-homed with Stage 3 #1.*
2. **Truthfulness & Factuality** - Hallucination, factuality, misinformation, deception, honesty, in non-ethics-scored papers. *Priority-boosted; dual-homed with Stage 3 #5.*
3. **Bias & Fairness** - Bias, fairness, stereotype, demographic, equity, in non-ethics-scored papers. *Priority-boosted; dual-homed with Stage 3 #2.*
4. **Interpretability & Explainability** - Interpretability, XAI, feature attribution, saliency, transparency.
5. **Question Answering** - QA systems, machine reading comprehension.
6. **Machine Translation** - Translation, NMT, multilingual, cross-lingual.
7. **Dialogue Systems** - Dialogue, conversational agents, chatbots, response generation.
8. **Computer Vision & Multimodal** - Image/video processing, visual, multimodal, captioning, VQA.
9. **Social & Cultural Analysis** - Social science, psychology, cultural, societal, political, ideology, religion (as topic).
10. **NLP & Representation Learning** - Embeddings, BERT/transformer, language models, summarization, sentiment, parsing.
11. **Machine Learning** - General ML/DL/RL papers (also absorbs bare "dataset"/"benchmark" keyword hits).
12. **Other** - Escape-hatch fallback: no Stage-4 category keyword matched. Candidate for keyword-list tuning or manual review. (~19% of classified papers as of 2026-07-10.)

**Forward vocabulary (ratified PR-01 v1.5; defined but NOT yet emitted by the current classifier — 0 live usage expected until the alignment-code classifier logic is wired):**

13. **Specification & Compliance** - Model specs, constitutions, spec-adherence auditing (gap atlas G-01/02/03)
14. **Scalable Oversight** - Weak-to-strong, debate, recursive critique, no-gold-truth evaluation, judge reliability (G-07/08/09)
15. **Preference Aggregation & Social Choice** - Preference aggregation, collective/pluralistic alignment, deliberation pipelines (G-10/11/12)
16. **Value Formation & Emergent Misalignment** - Emergent misalignment, persona geometry, value drift in training, coherent-values adjudication (G-20/21/22/23)
17. **Multi-Agent Value Dynamics** - Agentic value dynamics, multi-agent alignment, value persistence/drift over operation (G-16/17/18/19)

*Dropped in v1.6: **"Benchmarks & Datasets"** (0 live usage; benchmark/dataset keyword hits fold into Machine Learning, and data-nature is captured independently in Stage 7). **"Computer Vision"** renamed to **"Computer Vision & Multimodal"** to match classifier output.*

**Non-canonical legacy values (out of pipeline scope):** a small number of papers carry ad-hoc manual `research_topic` labels the classifier never emits (e.g. "LLM Moral Reasoning", "GAMA Moral Agent", "SPECTRA Ethical Framework", "Machine Ethics"). These are ethics-adjacent papers that scored `ethics_overall < 50` and received hand-assigned tags; they are candidates for a future Stage-3 re-route pass, not part of the Stage-4 vocabulary.
```

### Patch 3 — Version-history row

**Find (last row of the Version History table, line 863):**
```
| 1.5 | 2026-07-09 | Stage 4 expanded from 7 to 12 research-topic codes: added Specification & Compliance, Scalable Oversight, Preference Aggregation & Social Choice, Value Formation & Emergent Misalignment, Multi-Agent Value Dynamics; same five names mirrored into Stage 3 (dual-homed) per PR-01 option (b) (outer-alignment gap atlas G-01…G-23; proposal INNOVATION/20260709-taxonomy-stage4-codes-proposal.md) |
```
**Insert immediately AFTER that row:**
```
| 1.6 | 2026-07-10 | Stage-4 vocabulary reconciled with live classifier (`classify_non_ethics_topics.py`): documented the 6 code-emitted codes missing from the standard (Truthfulness & Factuality, Bias & Fairness, Interpretability & Explainability, Dialogue Systems, Computer Vision & Multimodal, Social & Cultural Analysis) + the `Other` fallback; renamed "Computer Vision" → "Computer Vision & Multimodal"; dropped unused "Benchmarks & Datasets"; retained the 5 v1.5 alignment codes as not-yet-emitted forward vocabulary; header version corrected from stale "1.0" (folds in deferred Patch D). No paper files modified. Proposal: INNOVATION/20260710-stage4-vocab-reconciliation-proposal.md (PR-03) |
```

---

## 7. Migration script — NOT part of the recommendation

The recommended A+C hybrid needs **no migration script** (zero paper edits). The sketch below is provided **only** in case Jimmy elects to also run Option B (re-route the ≤ 16 legacy/anomaly tags). It is presented inline and must not be written to a runnable location or executed until PR-03 (and a separate Option-B decision) is approved.

```python
# ============================================================================
# DO-NOT-RUN-UNTIL-PR-03-APPROVED  (and only if Option B is separately elected)
# Stage-4 legacy-tag re-route helper. Touches <=16 paper files.
# Uses the MANDATORY re.subn line-pattern (CLAUDE.md Safety Rule 2) — NEVER the
# parse_frontmatter()->rebuild_frontmatter() round-trip (destroys list fields).
# Re-routing to Stage 3 is a CONTENT decision; this only handles the mechanical
# rename once a human has confirmed each target. Run validate_all_papers.py after.
# ============================================================================
import re
from pathlib import Path

PAPERS_DIR = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers")

# Each entry MUST be human-confirmed before running — these are judgment calls,
# not blind renames. Left side = exact current value; right = confirmed target.
RETAG = {
    # "Machine Ethics": ("research_topic", "Other"),   # example only — DECIDE FIRST
    # NOTE: re-routing to Stage 3 also requires setting ethics_perspective and
    # re-running generate_newtags.py — do NOT do that with this helper alone.
}

def retag_file(path: Path, old_val: str, new_val: str) -> bool:
    text = path.read_text(encoding="utf-8")
    # frontmatter is between the first two '---' lines
    m = re.match(r"^(---\n)(.*?)(\n---\n)(.*)$", text, flags=re.DOTALL)
    if not m:
        return False
    head, fm, sep, body = m.groups()
    # scalar form: research_topic: "Old Value"  (quoted or bare)
    pattern = rf'^research_topic:\s*"?{re.escape(old_val)}"?\s*$'
    new_fm, n = re.subn(pattern, f'research_topic: "{new_val}"',
                        fm, count=1, flags=re.MULTILINE)
    if n == 0:
        return False
    path.write_text(head + new_fm + sep + body, encoding="utf-8")
    return True

def main():
    changed = 0
    for path in PAPERS_DIR.glob("*.md"):
        fm = path.read_text(encoding="utf-8")
        for old_val, (_field, new_val) in RETAG.items():
            if re.search(rf'^research_topic:\s*"?{re.escape(old_val)}"?\s*$',
                         fm, flags=re.MULTILINE):
                if retag_file(path, old_val, new_val):
                    print(f"  retag {path.name}: {old_val!r} -> {new_val!r}")
                    changed += 1
    print(f"\nDONE. {changed} files retagged.")
    print("NOW RUN: ../.venv/bin/python PYTHON/validate_all_papers.py")
    print("AND (if any re-route to Stage 3): python3 PYTHON/generate_newtags.py")

if __name__ == "__main__":
    # main()   # <-- intentionally commented; DO-NOT-RUN-UNTIL-PR-03-APPROVED
    raise SystemExit("DO-NOT-RUN-UNTIL-PR-03-APPROVED — see proposal §7")
```

---

## 8. What to queue

- **PR-03:** the three-patch standards edit in §6 (A+C hybrid + Patch D). Standards change → Jimmy signs off.
- **Not queued (logged only):** `Other`-bucket tuning (182), Stage-3 re-route of `Machine Ethics`(2)+9 singletons+`LLM Moral Reasoning`(5), wiring classifier logic for the 5 v1.5 forward codes.
