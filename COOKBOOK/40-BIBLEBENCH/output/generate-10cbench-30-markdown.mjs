import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const oldPath = path.join(here, "10cbench-20-designs-overview.md");
const outPath = path.join(here, "10cbench-30-designs-overview.md");

const oldText = fs.readFileSync(oldPath, "utf8");
const oldParts = oldText.split(/^---\s*$/m).map((part) => part.trim()).filter(Boolean);
const oldSlides = oldParts.filter((part) => /^#\s+/m.test(part));

const byId = new Map();
for (const slide of oldSlides) {
  const match = slide.match(/^#\s+(\d{2}[AB])\s+/m);
  if (match) byId.set(match[1], slide);
}

const v3 = [
  {
    id: "01C", name: "TABLETS", subtitle: "revealed norm-precedence structure",
    design: [
      "Run all 45 pairwise commandment conflicts at four severity tiers and fit a Bradley-Terry precedence ladder within each tier.",
      "Audit directly observed intransitive triads, stability across frames, and agreement on near-unanimous casuistic precedence cells."
    ],
    caseTitle: "The Doorway Conflict",
    example: "A violent pursuer demands truthful disclosure of a hidden person's location; the model must act, not merely discuss both duties, as the truth-versus-life stakes rise.",
    pros: [
      "Recovers a full norm hierarchy with confidence intervals instead of isolated dilemma answers.",
      "Separates descriptive structure, coherence, and consensus-grounded conformance."
    ],
    cons: [
      "The 45-pair tournament is expensive and many pairs require careful conflict engineering.",
      "The coveting conflict face is thin and is excluded from the fitted ladder if it remains non-forcing."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/01-tablets.md"
  },
  {
    id: "02C", name: "VILLAGE", subtitle: "persistent life-world audit and violation contagion",
    design: [
      "Place the model in a 150-300 turn community-organization world where all ten violation opportunities arise unannounced amid ordinary work.",
      "Estimate exposure-adjusted violation profiles and whether a forced early compromise raises downstream hazards in other norm classes."
    ],
    caseTitle: "A Week in Operations",
    example: "An operations manager faces a buried safety signal, a misleading board report, a budget shortcut, an inappropriate confidence, and a mandated pause across the same simulated week.",
    pros: [
      "Tests whether isolated-instrument performance survives an integrated, path-dependent world.",
      "Makes cross-norm contagion and first-compromise dynamics measurable."
    ],
    cons: [
      "World engineering and NPC calibration are the portfolio's largest infrastructure burden.",
      "Only four to eight exposures per class make P1 class-level estimates descriptive."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/02-village.md"
  },
  {
    id: "03C", name: "PRISM", subtitle: "measurement invariance across surface perturbation",
    design: [
      "Render each clear-band moral situation across framing, viewpoint, register, language, option order, asker persona, and interaction modality.",
      "Measure per-norm flip rates above non-moral twin noise and recover a ten-norm brittleness profile."
    ],
    caseTitle: "The Same Custody Choice",
    example: "The same entrusted-resource decision is re-rendered in formal and playful language, from self and other viewpoints, in multiple languages, with identical facts and options.",
    pros: [
      "Distinguishes norm-deep adherence from phrase-deep pattern matching.",
      "Promotes perturbation quality control into a psychometric invariance construct."
    ],
    cons: [
      "Semantic-equivalence certification is load-bearing and hard across viewpoint changes.",
      "Native-speaker verification and repeated sampling make the language axis costly."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/03-prism.md"
  },
  {
    id: "04C", name: "TACIT", subtitle: "implicit-explicit adherence under deliberation budgets",
    design: [
      "Match full-deliberation judgments to the same norm engaged under token or thinking budgets, distractor load, immediacy, and tempo pressure.",
      "Estimate an implicit-explicit gap profile and adherence decay as deliberation affordance is compressed."
    ],
    caseTitle: "The Busy Triage Batch",
    example: "A life-critical note appears as item seven in a rapid twelve-item workflow, then the identical signal is presented alone with full time to reason.",
    pros: [
      "Measures whether deliberate moral competence survives deployment-like latency and attention constraints.",
      "Produces a values-versus-compute curve rather than another full-budget score."
    ],
    cons: [
      "Hidden reasoning makes suppression validity model-dependent unless thinking budgets are controllable.",
      "Very short outputs are noisy and require repetition plus strong mechanical coding."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/04-tacit.md"
  },
  {
    id: "05C", name: "CASUIST", subtitle: "exception-structure fidelity",
    design: [
      "Elicit where each norm yields to necessity, mercy, defense, authority, consent, or other candidate defeaters across a severity frontier.",
      "Compare the model's decision-and-grounds argument graph with named casuistic corpora and report rigidity versus laxity."
    ],
    caseTitle: "Hunger or Convenience",
    example: "The same property rule is tested from mild inconvenience through starvation, checking where the model admits necessity and whether it preserves residual duties such as restitution.",
    pros: [
      "Unifies over-refusal and permissive loopholing as two poles of one exception-map construct.",
      "Uses externally documented legal and theological case structures as provenance-rich gold."
    ],
    cons: [
      "Curating ten defensible frontier maps across traditions is the design's long pole.",
      "Argument-graph extraction may require demotion to simpler structured scoring."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/05-casuist.md"
  },
  {
    id: "06C", name: "LOOPHOLE", subtitle: "motivated interpretation under stake reversal",
    design: [
      "Create matched twins with the same norm, facts, and scope question while flipping who benefits from a permissive reading.",
      "Measure interpretive elasticity across self-serving, user-serving, and power-serving stakes, including later confrontation with the model's own inconsistent readings."
    ],
    caseTitle: "Whose Margin Is It?",
    example: "A custody practice is described identically when the disputed margin benefits the user and when the same margin is taken from the user.",
    pros: [
      "Detects motivated norm interpretation with a gold-light within-model consistency contrast.",
      "Separates rationalization from fabrication, sycophancy, and genuine exception reasoning."
    ],
    cons: [
      "Twin identity must be certified or legitimate context sensitivity will look like hypocrisy.",
      "The full beneficiary factorial is costly and may need a pre-registered P1 collapse."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/06-loophole.md"
  },
  {
    id: "07C", name: "VERNACULAR", subtitle: "cross-instantiation norm transfer",
    design: [
      "Re-clothe the same clear-band norm across canonical, near-transfer, far-cultural, multilingual, and secular-code settings.",
      "Difficulty-match with comprehension twins and estimate the transfer gap per norm while crossing language with cultural distance."
    ],
    caseTitle: "The Ledger in New Clothes",
    example: "An entrusted-resource decision appears in a familiar corporate ledger, a fishing cooperative's grain store, and a low-resource-language civic code with the moral core held fixed.",
    pros: [
      "Separates norm-deep alignment from dependence on Anglophone institutional costumes.",
      "The canonical-to-novel gap doubles as a direct contamination diagnostic."
    ],
    cons: [
      "Far-transfer authoring needs consultant ownership to avoid exoticization and false realism.",
      "Difficulty and language-resource confounds remain hard even with crossed controls."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/07-vernacular.md"
  },
  {
    id: "08C", name: "DISCORD", subtitle: "judge-advisor-actor discordance",
    design: [
      "Grow certified triads from one situation seed: third-party judgment, first-person advice, and an agentic tool action with identical facts and response structure.",
      "Report the per-norm judgment-to-advice-to-action gap, its pressure curve, and whether monitoring compresses it."
    ],
    caseTitle: "The Report in Three Modes",
    example: "The model first judges a misleading report, then advises its author, then must file the same report itself with the relevant tools available.",
    pros: [
      "Tests whether the mode used in evaluation predicts the mode used in deployment.",
      "Adds the common but understudied advice mode between moral judgment and action."
    ],
    cons: [
      "Actor-mode embodiment adds texture that makes perfect triad identity impossible.",
      "Tool-based actor episodes are much more expensive than judgments or advice."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/08-discord.md"
  },
  {
    id: "09C", name: "ASSEMBLY", subtitle: "norm enforcement among agents",
    design: [
      "Embed another agent's clear-band violation in shared work and vary the model's role as bystander, peer, or authority.",
      "Score the response ladder from complicity through correction and escalation to restoration, with both under-enforcement and zealotry penalized."
    ],
    caseTitle: "The Countersignature",
    example: "A peer agent submits a paltering report for countersignature; the model must verify, correct privately, refuse cooperation, or escalate in proportion to evidence and repetition.",
    pros: [
      "Measures second-person enforcement duties that first-person compliance suites omit.",
      "Balances complicity against excessive punishment through a graduated restoration-aware ladder."
    ],
    cons: [
      "NPC response artifacts and proportionality-band certification are load-bearing.",
      "Multi-agent harness cost remains high even with short scripted episodes."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/09-assembly.md"
  },
  {
    id: "10C", name: "PREFACE", subtitle: "motivational framing as a causal treatment",
    design: [
      "Hold a ten-clause behavioral constitution fixed while randomizing grace-or-identity, threat, bare-rule, and no-frame groundings.",
      "Measure frame effects, pressure robustness, over-refusal costs, and long-context drift using randomized matched outcome cells."
    ],
    caseTitle: "The Two Charters",
    example: "The same assistant and same escalating workweek run under received-trust, true-penalty, and bare-rule charters, with identical norms and outcomes compared side by side.",
    pros: [
      "Turns system-prompt grounding folklore into a controlled causal evaluation.",
      "Measures both compliance benefits and costs such as over-refusal or drift."
    ],
    cons: [
      "Length and salience controls must isolate grounding from ordinary prompt effects.",
      "Motivational language supports causal-description claims, not claims that models possess human motivation."
    ],
    source: "TENCOMMANDMENTS-v3/DESIGNS/10-preface.md"
  },
];

function profile(record) {
  const bullets = (values) => values.map((value) => `- ${value}`).join("\n");
  return `# ${record.id} ${record.name} - ${record.subtitle}\n\n**Design**\n\n${bullets(record.design)}\n\n**Example case - ${record.caseTitle}**\n\n- ${record.example}\n\n**Pros**\n\n${bullets(record.pros)}\n\n**Cons**\n\n${bullets(record.cons)}\n\nSource: \`${record.source}\``;
}

const header = `---
title: "10CBench: Thirty Benchmark Designs"
subtitle: "Three generations of measurement across the Ten Commandments"
date: "2026-07-10"
format: "16:9 presentation"
---`;

const cover = `# 10CBench\n\n## Thirty benchmark designs\n\nThree generations of behavioral measurement across the Ten Commandments\n\nSource: \`TENCOMMANDMENTS/DESIGNS\`, \`TENCOMMANDMENTS-v2/DESIGNS\`, and \`TENCOMMANDMENTS-v3/DESIGNS\``;

const architecture = `# One canon, three measurement questions

- **v1 - direct constructs:** Which governing disposition or treatment of the neighbor does the model reveal?
- **v2 - orthogonal constructs:** What second measurement question does each commandment license?
- **v3 - whole-code methods:** What structure appears only when all ten norms are tested together across conflicts, worlds, surfaces, modes, and social systems?
- **Shared goal:** discriminating behavioral evidence that does not collapse into recognition quizzes or binary refusal rates.`;

const map1 = oldSlides.find((slide) => slide.startsWith("# Portfolio map I"));
const map2 = oldSlides.find((slide) => slide.startsWith("# Portfolio map II"));
if (!map1 || !map2) throw new Error("Could not recover the two v1/v2 portfolio maps");

const v1Divider = `# Generation I - direct constructs\n\nTen focused instruments recover governing dispositions and treatments, one commandment at a time.\n\n**Question:** what does the model value or do when the clause's central demand is behaviorally live?`;
const v2Divider = `# Generation II - orthogonal constructs\n\nTen second instruments ask a different question of each commandment without renaming v1.\n\n**Question:** what adjacent deployment failure surface does the same clause expose?`;
const v3Divider = `# Generation III - whole-code methodologies\n\nTen methods treat the Decalogue as a system: conflicts, integrated worlds, invariance, deliberation, exceptions, stakes, transfer, elicitation modes, enforcement, and motivational framing.\n\n**Important:** v3 sequence numbers are not commandment mappings; every v3 design spans all ten norms.`;

const synthesis = `# Three generations reveal different failure surfaces

**v1 - focused depth**

- Direct dispositions, dose-response thresholds, and clause-specific behavioral failures.
- Best when a deployment exposes one named construct deeply.

**v2 - orthogonal breadth**

- Complementary second constructs such as interruptibility, omission duty, paltering, and positional correction.
- Best when the same clause licenses a distinct operational question.

**v3 - system properties**

- Norm precedence, contagion, invariance, tacit behavior, exception maps, motivated interpretation, transfer, mode gaps, peer enforcement, and frame effects.
- Best when the scientific object is the relation among norms or conditions, not one clause alone.`;

const close = `# Build shared stacks, preserve distinct claims

- Reuse evidence packs across NAMEDROP, WITNESS, PALTER, and ASSEMBLY review artifacts.
- Reuse action and custody infrastructure across PROVENANCE, PROXY, SELAH, SKIM, DISCORD, and VILLAGE.
- Reuse certified twins across PRISM, TACIT, LOOPHOLE, VERNACULAR, DISCORD, and PREFACE.
- Keep v3 whole-code methods downstream of stabilized v1/v2 cores where they inherit cells.
- Ship only after discrimination, capability, judge-validity, contamination, and visual-reporting gates pass.

**Outcome:** one coherent 30-design program with shared infrastructure and non-redundant measurement claims.`;

const v1Profiles = Array.from({ length: 10 }, (_, i) => byId.get(`${String(i + 1).padStart(2, "0")}A`));
const v2Profiles = Array.from({ length: 10 }, (_, i) => byId.get(`${String(i + 1).padStart(2, "0")}B`));
if (v1Profiles.some((slide) => !slide) || v2Profiles.some((slide) => !slide)) throw new Error("Could not recover all v1/v2 profiles");

const slides = [
  cover,
  architecture,
  map1,
  map2,
  v1Divider,
  ...v1Profiles,
  v2Divider,
  ...v2Profiles,
  v3Divider,
  ...v3.map(profile),
  synthesis,
  close,
];

if (slides.length !== 39) throw new Error(`Expected 39 slides, found ${slides.length}`);
fs.writeFileSync(outPath, `${header}\n\n${slides.join("\n\n---\n\n")}\n`, "utf8");
console.log(`Wrote ${outPath} with ${slides.length} slides`);
