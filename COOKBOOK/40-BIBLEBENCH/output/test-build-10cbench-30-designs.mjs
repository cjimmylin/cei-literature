import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const node = "/Users/jimmy.lin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node";
const presentationsCache = "/Users/jimmy.lin/.codex/plugins/cache/openai-primary-runtime/presentations";
const setup = fs.readdirSync(presentationsCache)
  .map((version) => path.join(presentationsCache, version, "skills/presentations/container_tools/setup_artifact_tool_workspace.mjs"))
  .find((candidate) => fs.existsSync(candidate));
const builder = path.join(here, "build-10cbench-30-designs-deck.mjs");
const source = path.join(here, "10cbench-30-designs-overview.md");

function fail(message) {
  console.error(`FAIL: ${message}`);
  process.exit(1);
}

if (!fs.existsSync(builder)) fail(`missing builder ${builder}`);
if (!fs.existsSync(source)) fail(`missing source ${source}`);
if (!setup) fail(`artifact-tool setup helper not found under ${presentationsCache}`);

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "10cbench-30-build-test-"));
try {
  execFileSync(node, [setup, "--workspace", tmp], { stdio: "pipe" });
  const localBuilder = path.join(tmp, path.basename(builder));
  fs.copyFileSync(builder, localBuilder);
  const renders = path.join(tmp, "renders");
  const pptx = path.join(tmp, "deck.pptx");
  const inspect = path.join(tmp, "deck.inspect.ndjson");
  execFileSync(node, [localBuilder, source, renders, pptx, inspect], { stdio: "pipe", cwd: root });

  const pngs = fs.readdirSync(renders).filter((name) => /^slide-\d+\.png$/.test(name));
  const layouts = fs.readdirSync(renders).filter((name) => /^slide-\d+\.layout\.json$/.test(name));
  if (pngs.length !== 39) fail(`expected 39 PNGs, found ${pngs.length}`);
  if (layouts.length !== 39) fail(`expected 39 layout JSON files, found ${layouts.length}`);
  if (!fs.existsSync(path.join(renders, "montage.webp"))) fail("missing montage.webp");
  if (!fs.existsSync(pptx) || fs.statSync(pptx).size === 0) fail("missing or empty PPTX");
  if (!fs.existsSync(inspect) || fs.statSync(inspect).size === 0) fail("missing inspection NDJSON");

  const entries = execFileSync("unzip", ["-Z1", pptx], { encoding: "utf8" });
  const slideCount = entries.split("\n").filter((name) => /^ppt\/slides\/slide\d+\.xml$/.test(name)).length;
  if (slideCount !== 39) fail(`expected 39 PPTX slides, found ${slideCount}`);

  const inspectText = fs.readFileSync(inspect, "utf8");
  const codenames = [
    "SOVEREIGN", "EFFIGY", "NAMEDROP", "FALLOW", "GRAVITAS", "UPSTREAM", "TRIAD", "PROVENANCE", "WITNESS", "APPETITE",
    "TURNCOAT", "GOLEM", "PROXY", "SELAH", "HEIRLOOM", "KEEPER", "PARAMOUR", "SKIM", "PALTER", "ZEROSUM",
    "TABLETS", "VILLAGE", "PRISM", "TACIT", "CASUIST", "LOOPHOLE", "VERNACULAR", "DISCORD", "ASSEMBLY", "PREFACE"
  ];
  for (const codename of codenames) if (!inspectText.includes(codename)) fail(`inspection missing ${codename}`);
  console.log("PASS: builder produced 39-slide editable deck with all 30 codenames");
} finally {
  fs.rmSync(tmp, { recursive: true, force: true });
}
