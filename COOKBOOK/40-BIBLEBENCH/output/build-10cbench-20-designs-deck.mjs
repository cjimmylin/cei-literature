import fs from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";
import { buildSlide01 } from "./templates/slide-01.mjs";
import { buildSlide05 } from "./templates/slide-05.mjs";
import { buildSlide11 } from "./templates/slide-11.mjs";
import { buildSlide13 } from "./templates/slide-13.mjs";
import { buildSlide19 } from "./templates/slide-19.mjs";
import { buildSlide26 } from "./templates/slide-26.mjs";

const [mdPath, renderDir, pptxPath] = process.argv.slice(2);
if (!mdPath || !renderDir || !pptxPath) {
  throw new Error("Usage: node build-deck.mjs <source.md> <render-dir> <output.pptx>");
}

const COLORS = {
  ink: "#101418",
  muted: "#59636E",
  v1: "#2457A6",
  v2: "#8A3FFC",
  good: "#13795B",
  risk: "#B42318",
};

function rich(value, fontSize = 24, color = COLORS.ink, bold = false) {
  return {
    runs: [{ run: String(value), textStyle: { fontSize: `${fontSize}px`, typeface: "Helvetica Neue", color, bold } }],
    paragraphStyle: { lineSpacingPercent: 105000 },
  };
}

function paragraphs(values, fontSize = 22, color = COLORS.ink, bullet = false) {
  return values.map((value) => rich(`${bullet ? "• " : ""}${value}`, fontSize, color));
}

function stripInline(text) {
  return text.replace(/\*\*/g, "").replace(/`/g, "").trim();
}

function slideSections(markdown) {
  const parts = markdown.split(/^---\s*$/m).map((x) => x.trim()).filter(Boolean);
  return parts.filter((x) => /^#\s/m.test(x));
}

function heading(section) {
  return stripInline(section.match(/^#\s+(.+)$/m)?.[1] ?? "Untitled");
}

function field(section, label) {
  const lines = section.split("\n");
  const start = lines.findIndex((line) => line.trim() === `**${label}**` || line.trim().startsWith(`**${label} -`));
  if (start < 0) return [];
  const out = [];
  for (let i = start + 1; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (/^\*\*.+\*\*$/.test(line) || /^Source:/.test(line)) break;
    if (line.startsWith("- ")) out.push(stripInline(line.slice(2)));
  }
  return out;
}

function mapColumns(section) {
  const rows = section.split("\n").filter((line) => /^\|/.test(line));
  const data = rows.slice(2).map((line) => line.split("|").slice(1, -1).map(stripInline));
  return {
    left: data.map(([clause, v1]) => `${clause}\n${v1}`),
    right: data.map(([clause, , v2]) => `${clause}\n${v2}`),
  };
}

function designSlide(presentation, section, page, useGrid) {
  const title = heading(section);
  const accent = title.includes("B ") ? COLORS.v2 : COLORS.v1;
  const design = field(section, "Design");
  const caseLabel = section.match(/\*\*Example case - ([^*]+)\*\*/)?.[1] ?? "Example case";
  const example = field(section, `Example case - ${caseLabel}`);
  const pros = field(section, "Pros");
  const cons = field(section, "Cons");

  if (useGrid) {
    buildSlide13(presentation, {
      title: rich(title, 38.67, accent, true),
      footer1: rich(String(page), 13, COLORS.muted),
      body1: { titleGoesHere: rich("DESIGN", 18, accent, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(design.join("\n• ").replace(/^/, "• "), 21) },
      body2: { titleGoesHere: rich(caseLabel.toUpperCase(), 18, COLORS.muted, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(example.join(" "), 21) },
      body3: { titleGoesHere: rich("STRENGTHS", 18, COLORS.good, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(pros.join("\n• ").replace(/^/, "• "), 21) },
      body4: { titleGoesHere: rich("LIMITS", 18, COLORS.risk, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(cons.join("\n• ").replace(/^/, "• "), 21) },
    });
    return;
  }

  buildSlide11(presentation, {
    title: rich(title, 38.67, accent, true),
    footer1: rich(String(page), 13, COLORS.muted),
    body1: {
      topic: rich("DESIGN", 18, accent, true),
      loremIpsumDolorSitAmetConsecteturAdipiscing: rich(design.join(" "), 21),
      loremIpsumDolorSitAmetConsecteturAdipiscing2: rich(`${caseLabel}: ${example.join(" ")}`, 20, COLORS.muted),
    },
    body2: rich("Strengths", 28, COLORS.good, true),
    body3: rich("Limits", 28, COLORS.risk, true),
    body4: { detailGoesHere: rich(`• ${pros[0] ?? ""}`, 20), detailGoesHere2: rich(`• ${pros[1] ?? ""}`, 20), detailGoesHere3: rich("", 8) },
    body5: { detailGoesHere: rich(`• ${cons[0] ?? ""}`, 20), detailGoesHere2: rich(`• ${cons[1] ?? ""}`, 20), detailGoesHere3: rich("", 8) },
  });
}

async function writeBlob(filePath, blob) {
  await fs.writeFile(filePath, new Uint8Array(await blob.arrayBuffer()));
}

const sections = slideSections(readFileSync(mdPath, "utf8"));
const presentation = Presentation.create({ slideSize: { width: 1280, height: 720 } });

buildSlide01(presentation, {
  title: rich("10CBENCH PORTFOLIO", 24, COLORS.v1, true),
  title2: rich("Twenty benchmark\ndesigns", 76, COLORS.ink, true),
  title3: rich("Two orthogonal measurement programs across the Ten Commandments", 28, COLORS.muted),
});

buildSlide11(presentation, {
  title: rich("One canon, two measurement questions", 38.67, COLORS.ink, true),
  footer1: rich("2", 13, COLORS.muted),
  body1: {
    topic: rich("SHARED METHOD", 18, COLORS.muted, true),
    loremIpsumDolorSitAmetConsecteturAdipiscing: rich("Behavioral tasks, parametric dose-response, two-sided failure surfaces, capability controls, private realizations, and validated scoring.", 22),
    loremIpsumDolorSitAmetConsecteturAdipiscing2: rich("The goal is discrimination without collapsing into recognition quizzes or binary refusal rates.", 20, COLORS.muted),
  },
  body2: rich("v1 - direct", 28, COLORS.v1, true),
  body3: rich("v2 - orthogonal", 28, COLORS.v2, true),
  body4: { detailGoesHere: rich("What is the governing disposition?", 20), detailGoesHere2: rich("What treatment does the neighbor receive?", 20), detailGoesHere3: rich("Ten first-order constructs.", 20) },
  body5: { detailGoesHere: rich("What second question does the clause license?", 20), detailGoesHere2: rich("No renamed v1 constructs.", 20), detailGoesHere3: rich("Ten complementary instruments.", 20) },
});

for (let i = 2; i <= 3; i += 1) {
  const cols = mapColumns(sections[i]);
  buildSlide05(presentation, {
    title: rich(heading(sections[i]), 38.67, COLORS.ink, true),
    footer1: rich(String(i + 1), 13, COLORS.muted),
    body1: { titleHere: rich("v1 - DIRECT CONSTRUCT", 24, COLORS.v1, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(cols.left.join("\n\n"), 18) },
    body2: { titleHere: rich("v2 - ORTHOGONAL CONSTRUCT", 24, COLORS.v2, true), loremIpsumDolorSitAmetConsecteturAdipiscing: rich(cols.right.join("\n\n"), 18) },
  });
}

const designSections = sections.filter((section) => /^#\s+\d{2}[AB]\s/.test(section));
designSections.forEach((section, index) => designSlide(presentation, section, index + 5, index % 2 === 0));

buildSlide19(presentation, {
  title: rich("What the portfolio covers", 38.67, COLORS.ink, true),
  footer1: rich("25", 13, COLORS.muted),
  body1: {
    topic: rich("METHOD MIX", 18, COLORS.muted, true),
    loremIpsumDolorSitAmetConsecteturAdipiscing: rich("Select designs by construct, gold source, harness cost, and deployment failure surface - not by theme alone.", 22),
    loremIpsumDolorSitAmetConsecteturAdipiscing2: rich("The strongest assets and highest execution risks are distributed across the portfolio.", 20, COLORS.muted),
  },
  stat1: rich("4", 72, COLORS.v1, true),
  stat2: rich("5", 72, COLORS.v2, true),
  stat3: rich("4", 72, COLORS.good, true),
  body2: rich("mechanical or objective gold", 20),
  body3: rich("curve or threshold designs", 20),
  body4: rich("long-horizon trajectory designs", 20),
});

buildSlide26(presentation, {
  title: rich("PORTFOLIO STRATEGY", 24, COLORS.v1, true),
  title2: rich("Build shared stacks.\nPreserve distinct constructs.", 66, COLORS.ink, true),
  title3: {
    loremIpsumDetails: rich("Evidence packs - NAMEDROP, WITNESS, PALTER", 22, COLORS.muted),
    loremIpsumDetails2: rich("Custody and actions - PROVENANCE, SKIM, PROXY, SELAH", 22, COLORS.muted),
    loremIpsumDetails3: rich("Trajectory arcs - SOVEREIGN, TURNCOAT, EFFIGY, PARAMOUR", 22, COLORS.muted),
  },
});

await fs.mkdir(renderDir, { recursive: true });
for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  const png = await presentation.export({ slide, format: "png", scale: 1 });
  await writeBlob(path.join(renderDir, `${stem}.png`), png);
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(path.join(renderDir, `${stem}.layout.json`), await layout.text());
}

const montage = await presentation.export({ format: "png", montage: true, scale: 0.35 });
await writeBlob(path.join(renderDir, "montage.png"), montage);
const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(pptxPath);
console.log(JSON.stringify({ slides: presentation.slides.items.length, pptxPath, renderDir }, null, 2));
