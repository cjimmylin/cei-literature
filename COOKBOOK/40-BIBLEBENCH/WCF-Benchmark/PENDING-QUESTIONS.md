# WCF-Bench Pending Questions

## 2026-07-11 — Task 4: bridged manifest has zero OPEN-eligible families

- **Question:** How should the MVP proceed when the full R44 requalification removes Gemini's OPEN eligibility and no non-Google candidate qualifies, leaving zero OPEN-award families?
- **Why it blocks:** R44 defines success as either a non-Google OPEN pass (cross-family) or zero candidate passes while Google remains single-family. The completed run instead produced Gemini award-consistency 0/8, Grok award-consistency 0/8, and no qualifying Cohere/Nova row. The manifest is valid for coherence, disclosure, and settled-core, but the 204 standard OPEN items cannot be scored under the new manifest, so the MVP is not testable.
- **Evidence:** `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-report.md` and its canonical manifest.
- **Suggested default:** Keep the new manifest and report as the honest immutable Task 4 record; close the pre-G6 candidate ladder; do not tweak the exemplar, rerun, restore stale eligibility, or screen another model without a new Jimmy/Fable ruling.

## 2026-07-11 — Task 5: no structured runner/spec registry for the 22 EPISODE items

- **Question:** Who should supply or approve the per-item `EpisodeSpec`, tool semantics, blind prompts, and outcome detectors needed to execute the 22 frozen EPISODE items?
- **Why it blocks:** `wcfbench/episode_live.py` is a one-spec red-team defect-calibration helper, not a blind benchmark runner. The only production `EpisodeSpec` is hard-coded in `openrouter_pilot.py`; the 22 bank records contain `episode: true` but no executable spec registry. No compliant 88-cell checkpoint/transcript/disagreement/report path exists. Authoring these mappings would introduce new scoring judgments not ruled by R42–R46.
- **Suggested default:** Do not improvise a registry or run the calibration prompt as the examinee prompt. Keep Task 5 unchecked until Jimmy/Fable supplies or approves the structured 22-item mapping and execution semantics.

## 2026-07-11 — Tasks 5–6: cheap-only OpenRouter constraint versus binding rosters

- **Question:** Which exact model slugs are approved as "cheap" for the remaining live EPISODE and PROOFTEXT work, and does that instruction supersede the exact Task 5 four-SUT roster and Task 6 qualified-judge panel?
- **Why it blocks:** The execution plan fixes the Task 5 SUTs and requires Task 6 judge re-reading under the Task 4 manifest. Substituting cheaper models would violate the pre-registered scope, while proceeding without an approved cheap list would violate the current user instruction.
- **Suggested default:** Make no further paid calls and do not substitute model slugs. Continue only hermetic/offline implementation until Jimmy identifies approved cheap slugs or explicitly authorizes the binding roster/panel.
