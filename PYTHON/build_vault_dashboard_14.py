#!/usr/bin/env python3
"""Build the CEI Literature Vault Dashboard (v14 layout) from the vault alone.

Runs the v13/v14 generator (generate_vault_dashboard_9.py) with inputs that are all in the repo,
then splits the result for the static frontend:

    DASHBOARDS/cei-dashboard-14/data.js  ->  data-core.js + data-detail.js

Inputs
  papers/*.md                          frontmatter (the source of truth for every per-paper field)
  DASHBOARDS/cei-dashboard-14/build/benchmark_survey_candidates.json
                                       benchmark-survey "Yes" entries (1,081): the 986 v13
                                       candidates rebuilt from v13's output + tracked survey batches,
                                       plus 95 from the 2026-10-18 review of new papers
  DASHBOARDS/cei-dashboard-14/build/normative_v2_all_classifications.json
                                       normative v2 review (266), from consolidate_normative_v2.py
  author map + affiliations            regenerated from the notes on every build
                                       (build_author_paper_map.py --skip-api, no network)
  DASHBOARDS/cei-dashboard-13/data.js  benchmark categories of the v13 candidates are pinned to
                                       v13's published ones (about 190 original survey entries
                                       survive only in v13's output)

The older generator inputs under logs/*.json are gitignored and are not read.

Usage:
    python3 PYTHON/build_vault_dashboard_14.py
Writes only DASHBOARDS/cei-dashboard-14/{data.js,data-core.js,data-detail.js} and the author-map
logs (logs/<today>-author_*.json, gitignored). Never edits papers.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY = ROOT / "PYTHON"
OUT = ROOT / "DASHBOARDS" / "cei-dashboard-14"
BUILD = OUT / "build"
V13_DATA = ROOT / "DASHBOARDS" / "cei-dashboard-13" / "data.js"


def main():
    # Set iteration order affects tie ordering in the output; pin it so builds are repeatable.
    if os.environ.get("PYTHONHASHSEED") != "0":
        os.execve(sys.executable, [sys.executable, *sys.argv], {**os.environ, "PYTHONHASHSEED": "0"})

    tmp = Path(tempfile.mkdtemp(prefix="cei-dashboard-14-"))
    try:
        # lib.config refuses to load without a PDF folder; the build never reads PDFs.
        if not os.environ.get("VAULT_PDF_PATH") and not (ROOT / ".vault-config.json").exists():
            os.environ["VAULT_PDF_PATH"] = str(tmp / "no-pdfs")

        print("[1/3] Author map from the notes (build_author_paper_map.py --skip-api)...")
        stamp = date.today().strftime("%Y%m%d")
        subprocess.run([sys.executable, str(PY / "build_author_paper_map.py"), "--skip-api"],
                       cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
        author_map = ROOT / "logs" / f"{stamp}-author_paper_map.json"
        affiliations = ROOT / "logs" / f"{stamp}-author_affiliations.json"
        # The generator looks for affiliations under a fixed name in its logs folder.
        shutil.copy(affiliations, tmp / "20260220-author_affiliations.json")

        print("[2/3] Generator...")
        sys.path.insert(0, str(PY))
        os.chdir(ROOT)
        import generate_vault_dashboard_9 as G

        G.CANDIDATES_FILE = BUILD / "benchmark_survey_candidates.json"
        G.NORMATIVE_FILE = BUILD / "normative_v2_all_classifications.json"
        G.AUTHOR_MAP_FILE = author_map
        G.LOGS_DIR = tmp  # only read for the affiliations file at this point
        G.OUTPUT_DIR = OUT
        G.OUTPUT_FILE = OUT / "data.js"

        s = V13_DATA.read_text(encoding="utf-8")
        v13 = json.loads(s[s.index("{"):s.rstrip().rstrip(";").rindex("}") + 1])
        full_name = {name.split(". ", 1)[1]: name for name in G.CATEGORIES}
        pins = {p["fn"]: [full_name[c] for c in p["cs"]] for p in v13["papers"] if p.get("cs")}
        classify_entry = G.classify_entry

        def pinned_classify_entry(entry):
            fn = entry.get("filename")
            return list(pins[fn]) if fn in pins else classify_entry(entry)

        G.classify_entry = pinned_classify_entry
        G.main()

        print("[3/3] Splitting data.js...")
        subprocess.run([sys.executable, "split_data.py", "data.js"], cwd=OUT, check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"Done: {OUT.relative_to(ROOT)}/data-core.js, data-detail.js")


if __name__ == "__main__":
    main()
