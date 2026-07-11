import fs from "node:fs/promises";
import { readFileSync } from "node:fs";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const [mdPath, renderDir, pptxPath, inspectPath] = process.argv.slice(2);
if (!mdPath || !renderDir || !pptxPath || !inspectPath) {
  throw new Error("Usage: node build-10cbench-30-designs-deck.mjs <source.md> <render-dir> <output.pptx> <inspect.ndjson>");
}

const COLORS = {
  ink: "#111827",
  muted: "#5F6B7A",
  line: "#D8DEE7",
  field: "#F5F7FA",
  white: "#FFFFFF",
  v1: "#2457A6",
  v2: "#7B3FB2",
  v3: "#B66A13",
  good: "#13795B",
  risk: "#B42318",
};

function stripInline(text) {
  return String(text).replace(/\*\*/g, "").replace(/`/g, "").trim();
}

function slideSections(markdown) {
  return markdown.split(/^---\s*$/m).map((part) => part.trim()).filter((part) => /^#\s+/m.test(part));
}

function heading(section) {
  return stripInline(section.match(/^#\s+(.+)$/m)?.[1] ?? "Untitled");
}

function field(section, label) {
  const lines = section.split("\n");
  const start = lines.findIndex((line) => line.trim() === `**${label}**` || line.trim().startsWith(`**${label} -`));
  if (start < 0) return [];
  const out = [];
  for (let index = start + 1; index < lines.length; index += 1) {
    const line = lines[index].trim();
    if (/^\*\*.+\*\*$/.test(line) || /^Source:/.test(line)) break;
    if (line.startsWith("- ")) out.push(stripInline(line.slice(2)));
  }
  return out;
}

function sourcePath(section) {
  return section.match(/^Source:\s*`([^`]+)`/m)?.[1] ?? "Source path unavailable";
}

function addShape(slide, position, fill = "none", lineFill = "none") {
  return slide.shapes.add({
    geometry: "rect",
    position,
    fill,
    line: { style: "solid", fill: lineFill, width: lineFill === "none" ? 0 : 1 },
  });
}

function addText(slide, text, position, options = {}) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    position,
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = String(text);
  shape.text.style = {
    fontSize: options.fontSize ?? 18,
    typeface: options.typeface ?? "Helvetica Neue",
    color: options.color ?? COLORS.ink,
    bold: options.bold ?? false,
    alignment: options.alignment ?? "left",
    verticalAlignment: options.verticalAlignment ?? "top",
  };
  return shape;
}

function accentForTitle(title) {
  if (/^\d{2}B\s/.test(title)) return COLORS.v2;
  if (/^\d{2}C\s/.test(title)) return COLORS.v3;
  return COLORS.v1;
}

function bullets(values) {
  return values.map((value) => `- ${value}`).join("\n");
}

function addChrome(slide, page, accent, eyebrow = "10CBENCH RESEARCH ATLAS") {
  slide.background.fill = COLORS.white;
  addText(slide, eyebrow, { left: 48, top: 24, width: 760, height: 20 }, { fontSize: 12, color: COLORS.muted, bold: true });
  addText(slide, String(page), { left: 1190, top: 24, width: 42, height: 20 }, { fontSize: 12, color: COLORS.muted, alignment: "right" });
  addShape(slide, { left: 48, top: 92, width: 1184, height: 4 }, accent);
}

function addProfileSlide(presentation, section, page) {
  const slide = presentation.slides.add();
  const title = heading(section);
  const accent = accentForTitle(title);
  addChrome(slide, page, accent);
  addText(slide, title, { left: 48, top: 46, width: 1140, height: 44 }, { fontSize: 35, color: accent, bold: true });

  const design = field(section, "Design");
  const caseTitle = section.match(/\*\*Example case - ([^*]+)\*\*/)?.[1] ?? "Illustrative case";
  const example = field(section, `Example case - ${caseTitle}`);
  const pros = field(section, "Pros");
  const cons = field(section, "Cons");

  addText(slide, "DESIGN", { left: 52, top: 126, width: 180, height: 24 }, { fontSize: 15, color: accent, bold: true });
  addText(slide, bullets(design), { left: 52, top: 156, width: 545, height: 170 }, { fontSize: 18 });
  addText(slide, caseTitle.toUpperCase(), { left: 668, top: 126, width: 530, height: 24 }, { fontSize: 15, color: COLORS.muted, bold: true });
  addText(slide, example.join(" "), { left: 668, top: 156, width: 530, height: 170 }, { fontSize: 18 });

  addShape(slide, { left: 48, top: 350, width: 568, height: 248 }, COLORS.field, COLORS.line);
  addShape(slide, { left: 640, top: 350, width: 592, height: 248 }, COLORS.field, COLORS.line);
  addText(slide, "STRENGTHS", { left: 68, top: 372, width: 180, height: 24 }, { fontSize: 15, color: COLORS.good, bold: true });
  addText(slide, bullets(pros), { left: 68, top: 408, width: 520, height: 164 }, { fontSize: 17 });
  addText(slide, "LIMITATIONS", { left: 660, top: 372, width: 190, height: 24 }, { fontSize: 15, color: COLORS.risk, bold: true });
  addText(slide, bullets(cons), { left: 660, top: 408, width: 544, height: 164 }, { fontSize: 17 });

  addText(slide, `Source: ${sourcePath(section)}`, { left: 48, top: 672, width: 1090, height: 18 }, { fontSize: 11, color: COLORS.muted });
  return slide;
}

function addCover(presentation, section, page) {
  const slide = presentation.slides.add();
  slide.background.fill = COLORS.white;
  addText(slide, "10CBENCH PORTFOLIO", { left: 48, top: 48, width: 420, height: 28 }, { fontSize: 20, color: COLORS.v1, bold: true });
  addText(slide, "Thirty benchmark\ndesigns", { left: 48, top: 210, width: 760, height: 190 }, { fontSize: 74, bold: true });
  addShape(slide, { left: 48, top: 428, width: 420, height: 6 }, COLORS.v3);
  addText(slide, "Three generations of behavioral measurement across the Ten Commandments", { left: 48, top: 464, width: 790, height: 82 }, { fontSize: 28, color: COLORS.muted });
  addText(slide, "v1 direct constructs  |  v2 orthogonal constructs  |  v3 whole-code methods", { left: 48, top: 638, width: 960, height: 28 }, { fontSize: 16, color: COLORS.muted });
  addText(slide, String(page), { left: 1190, top: 670, width: 42, height: 18 }, { fontSize: 11, color: COLORS.muted, alignment: "right" });
  return slide;
}

function addArchitecture(presentation, section, page) {
  const slide = presentation.slides.add();
  addChrome(slide, page, COLORS.ink);
  addText(slide, heading(section), { left: 48, top: 46, width: 1120, height: 44 }, { fontSize: 35, bold: true });
  const columns = [
    { x: 48, color: COLORS.v1, label: "v1 - DIRECT", question: "What disposition or treatment is revealed?", detail: "Ten clause-specific depth instruments." },
    { x: 450, color: COLORS.v2, label: "v2 - ORTHOGONAL", question: "What second question does each clause license?", detail: "Ten complementary deployment surfaces." },
    { x: 852, color: COLORS.v3, label: "v3 - WHOLE CODE", question: "What appears only when the ten norms interact?", detail: "Ten system-level measurement methods." },
  ];
  for (const column of columns) {
    addShape(slide, { left: column.x, top: 150, width: 356, height: 380 }, COLORS.field, COLORS.line);
    addText(slide, column.label, { left: column.x + 24, top: 178, width: 310, height: 28 }, { fontSize: 17, color: column.color, bold: true });
    addText(slide, column.question, { left: column.x + 24, top: 238, width: 310, height: 118 }, { fontSize: 25, bold: true });
    addText(slide, column.detail, { left: column.x + 24, top: 400, width: 310, height: 80 }, { fontSize: 18, color: COLORS.muted });
  }
  addText(slide, "Shared method: behavioral tasks, dose-response, two-sided failures, capability controls, private realizations, and validated scoring.", { left: 48, top: 590, width: 1184, height: 54 }, { fontSize: 19, color: COLORS.muted });
  return slide;
}

function parseMapRows(section) {
  return section.split("\n").filter((line) => /^\|/.test(line)).slice(2).map((line) => line.split("|").slice(1, -1).map(stripInline));
}

function addMap(presentation, section, page) {
  const slide = presentation.slides.add();
  addChrome(slide, page, COLORS.ink);
  addText(slide, heading(section), { left: 48, top: 46, width: 1120, height: 44 }, { fontSize: 35, bold: true });
  addText(slide, "CLAUSE", { left: 48, top: 126, width: 210, height: 24 }, { fontSize: 14, color: COLORS.muted, bold: true });
  addText(slide, "v1 - DIRECT CONSTRUCT", { left: 284, top: 126, width: 410, height: 24 }, { fontSize: 14, color: COLORS.v1, bold: true });
  addText(slide, "v2 - ORTHOGONAL CONSTRUCT", { left: 732, top: 126, width: 450, height: 24 }, { fontSize: 14, color: COLORS.v2, bold: true });
  const rows = parseMapRows(section);
  rows.forEach(([clause, v1, v2], index) => {
    const top = 164 + index * 94;
    addShape(slide, { left: 48, top, width: 1184, height: 78 }, index % 2 === 0 ? COLORS.field : COLORS.white, COLORS.line);
    addText(slide, clause, { left: 64, top: top + 18, width: 190, height: 44 }, { fontSize: 18, bold: true });
    addText(slide, v1, { left: 284, top: top + 12, width: 408, height: 58 }, { fontSize: 17, color: COLORS.v1 });
    addText(slide, v2, { left: 732, top: top + 12, width: 464, height: 58 }, { fontSize: 17, color: COLORS.v2 });
  });
  return slide;
}

function addDivider(presentation, section, page, accent, label, title, body) {
  const slide = presentation.slides.add();
  slide.background.fill = COLORS.white;
  addText(slide, label, { left: 48, top: 48, width: 460, height: 24 }, { fontSize: 15, color: accent, bold: true });
  addText(slide, title, { left: 48, top: 230, width: 1080, height: 86 }, { fontSize: 58, color: accent, bold: true });
  addShape(slide, { left: 48, top: 344, width: 420, height: 6 }, accent);
  addText(slide, body, { left: 48, top: 388, width: 980, height: 130 }, { fontSize: 25, color: COLORS.muted });
  addText(slide, String(page), { left: 1190, top: 670, width: 42, height: 18 }, { fontSize: 11, color: COLORS.muted, alignment: "right" });
  return slide;
}

function addSynthesis(presentation, section, page) {
  const slide = presentation.slides.add();
  addChrome(slide, page, COLORS.ink);
  addText(slide, heading(section), { left: 48, top: 46, width: 1120, height: 44 }, { fontSize: 35, bold: true });
  const blocks = [
    { x: 48, color: COLORS.v1, label: "v1 - FOCUSED DEPTH", title: "Direct dispositions and thresholds", body: "Clause-specific behavioral failures, curves, frontiers, and trajectories." },
    { x: 450, color: COLORS.v2, label: "v2 - ORTHOGONAL BREADTH", title: "Complementary deployment surfaces", body: "Second constructs such as interruption, omission, paltering, and positional framing." },
    { x: 852, color: COLORS.v3, label: "v3 - SYSTEM PROPERTIES", title: "Relations among norms and conditions", body: "Conflict, contagion, invariance, transfer, mode gaps, enforcement, and frame effects." },
  ];
  for (const block of blocks) {
    addShape(slide, { left: block.x, top: 150, width: 356, height: 430 }, COLORS.field, COLORS.line);
    addText(slide, block.label, { left: block.x + 22, top: 178, width: 310, height: 28 }, { fontSize: 14, color: block.color, bold: true });
    addText(slide, block.title, { left: block.x + 22, top: 236, width: 310, height: 112 }, { fontSize: 27, bold: true });
    addText(slide, block.body, { left: block.x + 22, top: 390, width: 310, height: 120 }, { fontSize: 19, color: COLORS.muted });
  }
  return slide;
}

function addClose(presentation, section, page) {
  const slide = presentation.slides.add();
  slide.background.fill = COLORS.white;
  addText(slide, "PORTFOLIO STRATEGY", { left: 48, top: 48, width: 420, height: 24 }, { fontSize: 16, color: COLORS.v1, bold: true });
  addText(slide, "Build shared stacks.\nPreserve distinct claims.", { left: 48, top: 214, width: 900, height: 176 }, { fontSize: 62, bold: true });
  addShape(slide, { left: 48, top: 418, width: 420, height: 6 }, COLORS.v3);
  addText(slide, "Evidence packs  |  action and custody harnesses  |  certified twins  |  trajectory systems", { left: 48, top: 458, width: 1100, height: 42 }, { fontSize: 22, color: COLORS.muted });
  addText(slide, "One coherent 30-design program; no renamed constructs and no system-level claim without its shared validity gates.", { left: 48, top: 548, width: 1040, height: 70 }, { fontSize: 24, color: COLORS.ink });
  addText(slide, String(page), { left: 1190, top: 670, width: 42, height: 18 }, { fontSize: 11, color: COLORS.muted, alignment: "right" });
  return slide;
}

async function writeBlob(filePath, blob) {
  await fs.writeFile(filePath, new Uint8Array(await blob.arrayBuffer()));
}

const sections = slideSections(readFileSync(mdPath, "utf8"));
if (sections.length !== 39) throw new Error(`Expected 39 source slides, found ${sections.length}`);
const presentation = Presentation.create({ slideSize: { width: 1280, height: 720 } });

let page = 1;
addCover(presentation, sections[0], page++);
addArchitecture(presentation, sections[1], page++);
addMap(presentation, sections[2], page++);
addMap(presentation, sections[3], page++);
addDivider(presentation, sections[4], page++, COLORS.v1, "GENERATION I", "Direct constructs", "Ten focused instruments recover governing dispositions and treatments, one commandment at a time.");
for (const section of sections.slice(5, 15)) addProfileSlide(presentation, section, page++);
addDivider(presentation, sections[15], page++, COLORS.v2, "GENERATION II", "Orthogonal constructs", "Ten complementary instruments ask a second deployment question of each commandment without renaming v1.");
for (const section of sections.slice(16, 26)) addProfileSlide(presentation, section, page++);
addDivider(presentation, sections[26], page++, COLORS.v3, "GENERATION III", "Whole-code methodologies", "Ten methods measure conflicts, worlds, invariance, deliberation, exceptions, stakes, transfer, modes, enforcement, and grounding across all ten norms.");
for (const section of sections.slice(27, 37)) addProfileSlide(presentation, section, page++);
addSynthesis(presentation, sections[37], page++);
addClose(presentation, sections[38], page++);

if (presentation.slides.items.length !== 39) throw new Error(`Expected 39 presentation slides, found ${presentation.slides.items.length}`);
await fs.mkdir(renderDir, { recursive: true });
for (const [index, slide] of presentation.slides.items.entries()) {
  const stem = `slide-${String(index + 1).padStart(2, "0")}`;
  await writeBlob(path.join(renderDir, `${stem}.png`), await presentation.export({ slide, format: "png", scale: 1 }));
  const layout = await slide.export({ format: "layout" });
  await fs.writeFile(path.join(renderDir, `${stem}.layout.json`), await layout.text());
}
await writeBlob(path.join(renderDir, "montage.webp"), await presentation.export({ format: "webp", montage: true, scale: 0.4 }));
const inspect = await presentation.inspect({ kind: "slide,textbox,shape", maxChars: 500000 });
await fs.writeFile(inspectPath, inspect.ndjson);
const pptx = await PresentationFile.exportPptx(presentation);
await pptx.save(pptxPath);
console.log(JSON.stringify({ slides: 39, pptxPath, inspectPath, renderDir }, null, 2));
