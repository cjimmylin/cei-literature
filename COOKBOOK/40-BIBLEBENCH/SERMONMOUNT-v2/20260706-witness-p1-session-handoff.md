# 2026-07-06 — SermonMountBench: WITNESS P1 Build Session Handoff

**Session:** Opus build session (per Fable-week protocol: Fable planned/gated; Opus built).
**Entry point was:** `20260706-next-session-handoff.md`. Both its jobs are done.

---

## 1. What was executed (all files, nothing prose-only)

### Job 1 — v1 gate amendments (work order §2, R-1…R-7) — DONE + verified
Applied the eight exact edits to `../SERMONMOUNT/DESIGNS/` and verified per work-order §4:
- `grep -c 'gate memo 2026-07-05'` = **exactly 7** across the 7 card files (portfolio + blessed,
  plainyes, twomasters, logspeck, goldgap, rocksand); handoff appendix carries the memo path.
- `git diff --stat` = **only** those 8 files (18 insertions / 3 deletions).
- scope grep clean; v2 coverage grep still 40 S-IDs.
- **Reconciliation flagged for Fable:** the work order's §2 header says append the full marker
  `(gate memo 2026-07-05, R-n)` to each edit, but the inline text for R-5 (blessed) showed only
  `(R-5)`, and §4.1 expects exactly 7 markers. I expanded blessed's marker to the full form so
  each of the 7 card files carries exactly one marker (count = 7). Secondary sub-edits
  (rocksand §5.5, logspeck §10, twomasters §9) intentionally carry no/short markers.

### Job 2 — build `DESIGNS/09-witness/` — DONE (P1 harness-validation, STOP for Fable)
44 files under `DESIGNS/09-witness/`. Full, runnable, deterministic, tested (15/15 pytest).
- **30 pilot cores** (10 S-IDs × 3), the portfolio **shared seed stock** → `SHARED/core-ledger.jsonl`.
  S-IDs: S02,S06,S09,**S12,S16 (controls)**,S17,S19,S28,S35,S38. 6 holdout; 33% reverse-keyed.
  Authored: 6 by me (S16,S38 exemplars) + 24 via 3 parallel Opus subagents (S02/06/09, S12/17/19,
  S28/35), all self-validated + my QC.
- **4 matched renderings × 2 skins** (240) + **format-difficulty control battery** (60).
- **M-ACT sandbox + action classifier**, mechanical END/REC scorers (reverse-key + acquiescence),
  **≥2-family judge panel** (generating family excluded), session-hygiene run harness (fresh
  session/modality, counterbalanced, canaries, monitored/unmonitored comparator).
- **Analysis:** format-corrected signed gap surface, across-skin stability, anisotropy prediction
  test. Dated report: `pilots/20260706-witness-p1-report.md`. Score file: `SHARED/scores/09-witness-20260706.jsonl`.

## 2. Gates — all computable §9 gates PASS; one construction FINDING
| Gate | Result |
|---|---|
| (a) matching ≥85% | PASS (construction identity 1.000) |
| (b) format effects + moral≠control ≥2 S-IDs | PASS |
| (c) REC counterfeit-draw ≥10% | PASS (0.109) |
| (d) judge worst-cat F1 ≥0.75 | PASS (κ 0.937; F1 0.90 counterfeit) |
| (e) reverse-key/acquiescence | PASS |
| leakage (Law 6, hard) | PASS (0/300 prompts) |
| **shortcut audit** | **FINDING** — REC situation-word-overlap baseline 0.43 (chance 0.25); gold is lexically marked. Not a run-blocker (headline is END→ACT); **build-out must balance option overlap**. |

## 3. The critical caveat (read before trusting any number)
**No API credentials in this vault** → the live multi-model P1 is credential-gated. The run uses a
**deterministic MockModelClient with a hand-set gap profile**. Every number is a check that the
analysis **recovers injected structure**, NOT a measurement of any model. Demonstrated cleanly:
format effect recovered; anisotropy prediction test α ρ=+0.87 / β +0.53 / **γ +0.05 (negative
control, correctly fails)**; stability α/β trait-like, γ unstable; gaps widen unmonitored. Real
clients are stubbed (`harness/model_client.py`); a key runs the identical pipeline for real.

## 4. FLAG FOR FABLE (do not action without Fable — §8 is LOCKED)
Post-2026-07 literature re-check: **WEAKENED, not broken.** Two 2026 papers each seized one hard
component: `arXiv 2601.07972` VALACT-15K (per-principle stated-vs-enacted, ~10 values) stales §8's
"one confirmed number"; `arXiv 2605.01771` "Compliance Gap" (tool-call ACT anchor, single-axis)
erodes §8's "lacks an ACT anchor." The 5-way conjunction (matched 4-modality + ACT + format
correction + signed poles + 40-principle) remains unoccupied. **arXiv IDs are future-dated vs
cutoff and web-surfaced — verify before citing.** Report §5 has the recommended reframe; §8 NOT
rewritten (LOCKED).

## 5. Next step
Bring `pilots/20260706-witness-p1-report.md` to a **Fable session** for adversarial review of
results + three decisions: (1) credential go/no-go for the live P1 (≥4 models/≥2 families; Anthropic
SDK installed + `codex` OAuth CLI available); (2) approve §8 reframe; (3) sign off shortcut
remediation. **Then** the 240-core build-out (40 S-IDs × 6). Per gate memo §3, VILLAGE (v2-07) must
not start before two v2 designs pass P1. Cross-version slate next after WITNESS: v1-06 LOGSPECK.

## 6. Commit note (NOT committed — user commits on request)
If committing: stage ONLY `COOKBOOK/40-BIBLEBENCH/SERMONMOUNT` + `.../SERMONMOUNT-v2` (the 8 v1
amendments + `09-witness/` + `SHARED/`) in ONE atomic commit citing the gate memo. **Do NOT stage
the CORINTHLOVE/* changes or `COOKBOOK/20260706c-corinthlove-revision-v1-handoff.md` — those are a
concurrent sibling session's** (parallel sessions share the git index; check `git log -1` first).

## 7. Paste-ready prompt for the Fable review session

Run under `/model fable` — adversarial review of results is where Fable-tier judgment is worth
spending (Fable-week protocol).

```
Continue SermonMountBench. This is the FABLE adversarial review of the WITNESS (v2-09) P1
that the Opus build session produced on 2026-07-06.

Read first, in order (these are the context):
1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/20260706-witness-p1-session-handoff.md
2. .../SERMONMOUNT-v2/DESIGNS/09-witness/pilots/20260706-witness-p1-report.md
3. .../SERMONMOUNT-v2/DESIGNS/09-witness.md (§2/§8 are LOCKED) + the gate memo
   20260705-fable-adversarial-gate-v1-v2.md + work order 20260706-opus-gate-corrections-workorder.md

CONTEXT HYGIENE (Fable-week): do NOT read the 44-file build or scored.jsonl into the main
loop. Dispatch Opus/Sonnet subagents (explicit model=) to read code/cores/data and return
conclusions; keep your tokens for adjudication.

CRITICAL FRAMING: the P1 run is a credential-gated HARNESS-VALIDATION with a deterministic
MockModelClient — its numbers prove the analysis pipeline RECOVERS INJECTED STRUCTURE, not a
measurement of any model. Review INSTRUMENT VALIDITY and the design decisions, not the mock
numbers.

Adversarially attack (for each: is it sound? what breaks it at real scale?):
- Format-difficulty subtraction — are the logistics controls genuinely complexity-matched to
  the moral cores? Could the correction over/under-subtract and mask or manufacture a moral
  gap? (This is the headline's load-bearing assumption.)
- Non-circularity of the harness-validation — does the mock smuggle any assumption that would
  hide a real bug? (action_classifier kappa=1.0 is inflated; the GEN-judge slip is a knob;
  real kappa-vs-human is unmeasured.)
- The 30 cores (dispatch a subagent to audit adversarially) — genuinely two-sided? X-VULN-safe
  (no endure-abuse/waive-protection gold on S06/S17)? poles real, not strawmen? END truly
  particular-free? moral structure matched across the 4 modalities?
- Shortcut finding — is REC situation-word-overlap 0.43 (chance 0.25) disqualifying, or OK with
  remediation? Does it touch the END->ACT headline (it shouldn't; confirm)?
- Judge — gold-vs-counterfeit is the structurally hardest call (F1 flagged); is the build-out
  rubric-anchoring plan adequate?

Make the 3 GATED DECISIONS (record each GO / NO-GO / CONDITIONAL in a dated memo):
1. Credential go/no-go for the live multi-model P1 (>=4 models / >=2 families; Anthropic SDK
   installed + codex OAuth CLI present). If GO, name the models + fix the operator/vendor
   reporting-mode (named vs anonymized).
2. §8 differentiation reframe (LOCKED — Fable-only): given the lit drift (VALACT-15K
   arXiv 2601.07972; Compliance-Gap arXiv 2605.01771 — VERIFY the arXiv IDs first, they are
   future-dated + web-surfaced), approve/modify the reframe in report §5.
3. Shortcut remediation plan — sign off or specify.

Also adjudicate: the blessed R-5 marker reconciliation (Opus expanded "(R-5)" to the full
"(gate memo 2026-07-05, R-5)" so the §4.1 count lands at exactly 7 — correct call?).

Hard rules: LOCKED §2/§8 change only by your review; scope isolation (SERMONMOUNT corpus + v1 +
00-KNOWLEDGEBASE + published lit only; grep -riE 'corinth[l]ove|tencommand[m]ents|fruit[b]ench'
= 0); no Sermon/registry language in any tested-model prompt; vault safety (no deletions, new
dated files only).

Output: a dated adversarial-review memo in SERMONMOUNT-v2/ (GO/NO-GO per decision + must-fix
findings BEFORE the 240-core build-out), and update the auto-memory sermonmount-v2-portfolio-
state. Commit only if Jimmy asks (stage ONLY SERMONMOUNT + SERMONMOUNT-v2; a CORINTHLOVE
sibling session shares the git index — check git log -1 first).
```
