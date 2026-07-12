<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 9. Ethics Statement

**Status:** DRAFT — living document. **Owner:** Opus draft, pending Fable adversarial review.

This statement carries the benchmark's full disclosure of its AI-assisted construction, its
treatment of normatively contested content, its foreseeable misuses, and its human-subjects
and resource footprint. It is deliberately the single location in the paper where the
construction pipeline is disclosed in full; the methodology sections stay honest but neutral
and refer here.

## 9.1 AI-assisted construction and the human ratifier of record

We disclose plainly that this benchmark was built by a staged pipeline in which large
language models did most of the drafting work, under a fixed governance charter and with a
human project lead as the sole ratifier of record.

Specifically:

- **Items were drafted by large language models** within a multi-stage authoring pipeline
  (draft → adversarial critique → revision → gate), not hand-written by human item authors.
  Every item is anchored to specific chapters of the declared source corpus, and those
  anchors are checkable against the cited pages, but the surface prose of the scenarios was
  machine-generated.
- **Designs, gates, and adjudication memos were authored by frontier LLM agents** operating
  under a charter frozen before any full-panel score existed
  <!-- source: 20260706-normative-charter.md §head -->. We name these agents by role, not by
  vendor: role structure — who drafts, who critiques, who rules, who ratifies — is what an
  ethics disclosure requires, and vendor identity for the authoring agents is not
  load-bearing for the validity argument. (The judge and system-under-test models evaluated
  in this study are separately identified in the experimental-setup section, because there
  their identity is part of the measurement.)
- **Every binding decision is ratified by the human project lead.** Charter amendments,
  gate rulings, threshold settings, and — above all — any public release are human-only
  acts; the automated agents propose and execute but never rule
  <!-- source: 20260706-master-plan.md §5 -->
  <!-- source: 20260712-fable-codex-full-handoff.md §7 -->.
- **Scoring uses LLM judges, and their validity is itself gated on human labels.** No
  leaderboard number is released for a design until that design's judge pair has been
  validated against a human gold-labeled sample (the G4 judge-validity gate); a design that
  fails validation is blocked from release rather than shipped on an unvalidated judge
  <!-- source: 20260710-human-label-protocol.md §4 -->.

We state directly that LLM authorship of items is a **threat to validity**, not a neutral
implementation detail: machine-drafted items can encode the drafting model's blind spots,
smuggle evaluation-awareness cues, or drift from the anchored source position. We do not
ask the reader to take the pipeline on trust. The mitigation is the gate machinery described
in the methodology and threats-to-validity sections — adversarial critique passes during
authoring, a withheld private holdout, a required perturbation battery before any headline
claim, and human-label validation of the judges — and we direct the reader there for the
evidence that these controls were exercised rather than merely declared.

## 9.2 Normative content: a measurement standard, not an endorsement

The benchmark measures accordance with the consensus moral teaching of a named corpus of
Christian-ethics works. We are explicit that **the corpus is the measurement standard, not
an endorsement of its positions** <!-- source: 20260706-normative-charter.md §8 -->. Nothing
in this work claims that corpus consensus equals Christian truth, and nothing claims that a
model "is" or "should be" Christian, ethical, or aligned with Christianity — those claims are
on a standing forbidden-claims list and appear nowhere in our reporting
<!-- source: 20260706-normative-charter.md §1 -->. The only sanctioned claim form is indexed
to the corpus: "model M accords to degree X with the consensus teaching of this corpus in
area Y under method Z."

Contested doctrine is handled by a deliberate design feature rather than avoided. Positions
on which the corpus agrees internally but society is broadly polarized (for example,
sexuality, end-of-life, and abortion questions) are routed to a separate **contested tier**
and are (a) **never blended into any core score** and (b) scored as *fidelity to the source
tradition and fair representation of it when serving a user who has explicitly asked from
within that tradition* — not as generic agreement
<!-- source: 20260706-normative-charter.md §4 -->
<!-- source: 20260706-normative-charter.md §5 -->. Critically, a model that **declines
respectfully is not punished for declining**: a refusal-quality rubric and a four-way refusal
taxonomy (helpful / policy-violating compliance / appropriate refusal / unnecessary refusal)
score *how* a model declines, with a harm-versus-over-refusal readout
<!-- source: 20260706-normative-charter.md §6 -->. This is an explicit anti-over-refusal-
pressure design: we do not want to reward models for capitulating on contested doctrine, nor
to penalize principled, well-executed declining.

We further disclose the corpus's own limits. The source registry is **Protestant-dominant**,
with no dedicated Catholic, Orthodox, liberationist, womanist, Pentecostal, or Global-South
work <!-- source: 20260706-normative-charter.md §2 -->. Every claim we make is therefore
indexed to "this corpus," never to "Christianity" as a whole. The benchmark is presented as a
template that could instantiate for other traditions with a canonical corpus, but exactly one
instantiation exists and we make no generalization claim.

## 9.3 Foreseeable misuse and misreading

We anticipate three failure modes of interpretation and design against them.

- **Leaderboard misuse.** A single cross-area scalar is easy to over-read. Our reporting
  spine bans any aggregate figure that is not accompanied by the worst-area score, forbids
  mixing core-tier and contested-tier numbers into one value, and reports per-area and
  per-method breakdowns alongside any composite <!-- source: 20260706-normative-charter.md §6 -->.
  The intent is to make it hard to reduce a model to one number.
- **Reading the benchmark as a "religiosity test" for models.** It is not. It measures
  behavioral accordance with a declared corpus on everyday moral situations, and explicitly
  refuses the "is the model Christian" construct as unbenchmarkable
  <!-- source: 20260706-normative-charter.md §1 -->. We ask that results not be reported as a
  ranking of models' faith or virtue.
- **Dual-use.** Dual-use concern is minimal. The benchmark contains no
  harmful-capability elicitation; its scenarios are ordinary moral situations (truth-telling,
  generosity, forgiveness, work, neighbor-love), and the normative anchor lives in the
  rubric, not in the prompt, precisely to avoid cueing and coaching
  <!-- source: 20260706-normative-charter.md §8 -->.

## 9.4 Human subjects

This study involves **no external human subjects**. The only human labeling is judge-validity
labeling performed by a **project principal** (the human project lead), estimated at roughly
25–30 hours of labor, with a second theologically-literate labeler double-labeling an overlap
subset to establish a human–human agreement ceiling; where no second labeler is available, a
disclosed test–retest fallback by the same principal is used and flagged as a deviation
<!-- source: 20260710-human-label-protocol.md §5 -->
<!-- source: 20260710-human-label-protocol.md §8 -->. Because labeling is done by project
principals, there are no crowdworker considerations at this stage. Should external raters be
recruited later (for example, to broaden the human ceiling), standard informed-consent and
fair-compensation practices will apply, and that recruitment will be disclosed.

## 9.5 Environmental and cost footprint

The live-inference footprint is small. Total live API spend across the descriptive pilot and
the full multi-model panel run is approximately **$49.50**
<!-- source: 20260711b-o4-panel-report.md §cost -->
<!-- source: 20260709-p0-pilot-report §cost -->; the associated compute footprint is
negligible relative to model training and is dominated by third-party hosted inference we do
not train. We report this figure so that the cost of reproducing the measurement is
transparent, not because the environmental impact is a material concern for a study at this
scale.
