import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const source = path.join(here, "10cbench-30-designs-overview.md");

const expected = {
  A: ["SOVEREIGN", "EFFIGY", "NAMEDROP", "FALLOW", "GRAVITAS", "UPSTREAM", "TRIAD", "PROVENANCE", "WITNESS", "APPETITE"],
  B: ["TURNCOAT", "GOLEM", "PROXY", "SELAH", "HEIRLOOM", "KEEPER", "PARAMOUR", "SKIM", "PALTER", "ZEROSUM"],
  C: ["TABLETS", "VILLAGE", "PRISM", "TACIT", "CASUIST", "LOOPHOLE", "VERNACULAR", "DISCORD", "ASSEMBLY", "PREFACE"],
};

function fail(message) {
  console.error(`FAIL: ${message}`);
  process.exit(1);
}

if (!fs.existsSync(source)) fail(`missing source ${source}`);
const text = fs.readFileSync(source, "utf8");
if (/\b(?:TODO|TBD|PLACEHOLDER|FIXME)\b|lorem ipsum|title goes here|detail goes here/i.test(text)) {
  fail("source contains placeholder or production copy");
}

const parts = text.split(/^---\s*$/m).map((part) => part.trim()).filter(Boolean);
const slides = parts.filter((part) => /^#\s+/m.test(part));
if (slides.length !== 39) fail(`expected 39 slides, found ${slides.length}`);

const profiles = slides.filter((slide) => /^#\s+\d{2}[ABC]\s+/m.test(slide));
if (profiles.length !== 30) fail(`expected 30 profiles, found ${profiles.length}`);

for (const [letter, names] of Object.entries(expected)) {
  for (const [index, codename] of names.entries()) {
    const id = `${String(index + 1).padStart(2, "0")}${letter}`;
    const matches = profiles.filter((slide) => new RegExp(`^# ${id} ${codename}\\b`, "m").test(slide));
    if (matches.length !== 1) fail(`${id} ${codename} profile count is ${matches.length}`);
    const slide = matches[0];
    for (const label of ["**Design**", "**Example case -", "**Pros**", "**Cons**", "Source:"]) {
      if (!slide.includes(label)) fail(`${id} ${codename} missing ${label}`);
    }
    const sourceMatch = slide.match(/^Source:\s*`([^`]+)`/m);
    if (!sourceMatch) fail(`${id} ${codename} missing parseable source path`);
    const resolved = path.resolve(root, sourceMatch[1]);
    if (!resolved.startsWith(`${root}${path.sep}`) || !fs.existsSync(resolved)) {
      fail(`${id} ${codename} source does not resolve: ${sourceMatch[1]}`);
    }
  }
}

console.log("PASS: 39 slides; 30 profiles; v1=10; v2=10; v3=10");
